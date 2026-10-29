"""Exact-piece refresh must preserve every unselected evidence file and view."""
from copy import deepcopy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scp.content import refresh_catalog_content


def connections(identifier):
    return {'subject_id': identifier, 'ports': [], 'journeys': [],
            'forbidden_transfers': [], 'source': {'resource_fingerprints': {}}}


class ExactPieceRefreshTests(unittest.TestCase):
    def test_only_selected_evidence_is_read_or_refreshed_and_dependencies_are_deferred(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            domain = root/'domains/hsr'
            selected = {'id': 'selected', 'domain': 'hsr', 'name': 'Selected'}
            sibling = {'id': 'sibling', 'domain': 'hsr', 'name': 'Sibling'}
            assemblies = []
            for identifier, members in (('affected', ['selected', 'sibling']), ('unrelated', ['sibling'])):
                assemblies.append({'id': identifier, 'domain': 'hsr',
                                   'path': 'domains/hsr/01_assemblies/'+identifier,
                                   'scene': {'placements': [{'id': piece_id, 'piece_id': piece_id} for piece_id in members]}})
            catalog = {'pieces': [selected, sibling], 'domains': {'hsr': {'path': 'domains/hsr', 'name': 'HSR'}},
                       '_assemblies': assemblies}
            protected = [domain/'connection-classes.jsonc', domain/'00_pieces/INVENTORY.md',
                         domain/'01_assemblies/INVENTORY.md', domain/'README.md']
            for directory in (domain/'00_pieces/sibling', domain/'01_assemblies/affected', domain/'01_assemblies/unrelated'):
                protected.extend(directory/name for name in ('connections.json', 'checks/manual-tests.json', 'README.md', 'TESTING.md'))
            for path in protected:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b'Intentionally unreadable cached evidence: '+path.name.encode()+b'\n')
            original = {path: path.read_bytes() for path in protected}
            read_text = Path.read_text
            read_bytes = Path.read_bytes

            def guarded_text(path, *args, **kwargs):
                self.assertNotIn(path, protected, 'Unselected metadata must not be read')
                return read_text(path, *args, **kwargs)

            def guarded_bytes(path, *args, **kwargs):
                self.assertNotIn(path, protected, 'Unselected evidence must not be read')
                return read_bytes(path, *args, **kwargs)

            record = connections('selected')
            before = deepcopy(record)
            with patch('scp.catalog.load_catalog', return_value=catalog), \
                    patch.object(Path, 'read_text', guarded_text), \
                    patch.object(Path, 'read_bytes', guarded_bytes), \
                    patch('scp.connectivity.assembly_connectivity', side_effect=AssertionError('No automatic assembly extraction')), \
                    patch('scp.inventory.write_inventories', side_effect=AssertionError('No global inventory refresh')):
                result = refresh_catalog_content(root, records={'selected': record}, changed_piece_ids={'selected'},
                                                 scope_to_changed=True)
            self.assertEqual(original, {path: path.read_bytes() for path in protected})
            self.assertEqual(json.loads((domain/'00_pieces/selected/connections.json').read_text()), record)
            self.assertTrue((domain/'00_pieces/selected/checks/manual-tests.json').is_file())
            self.assertEqual(record, before)
            self.assertEqual(result['changed_piece_ids'], ['selected'])
            self.assertEqual((result['pieces'], result['assemblies']), (1, 0))
            self.assertEqual(result['skipped_missing_records'], [])
            self.assertEqual(result['deferred_assembly_ids'], ['affected'])
            self.assertTrue(result['connection_classes_refresh_required'])
            self.assertTrue(result['inventory_refresh_required'])
            self.assertEqual(result['inventory'], {})

    def test_empty_exact_scope_reads_no_cached_records_and_does_no_work(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            catalog = {'pieces': [{'id': 'unrelated', 'domain': 'hsr'}],
                       'domains': {'hsr': {'path': 'domains/hsr'}}, '_assemblies': []}
            with patch('scp.catalog.load_catalog', return_value=catalog), \
                    patch('pathlib.Path.read_text', side_effect=AssertionError('No metadata reads')), \
                    patch('scp.content.write_subject_content', side_effect=AssertionError('No subject writes')), \
                    patch('scp.inventory.write_inventories', side_effect=AssertionError('No inventory writes')):
                result = refresh_catalog_content(root, records={}, changed_piece_ids=set(), scope_to_changed=True)
            self.assertEqual((result['pieces'], result['assemblies']), (0, 0))
            self.assertEqual(result['deferred_assembly_ids'], [])
            self.assertFalse(result['connection_classes_refresh_required'])
            self.assertFalse(result['inventory_refresh_required'])

    def test_exact_scope_requires_explicit_known_changed_ids_and_fresh_records(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            catalog = {'pieces': [{'id': 'selected', 'domain': 'hsr'}], 'domains': {'hsr': {'path': 'domains/hsr'}}}
            for kwargs in ({'records': {}}, {'records': {}, 'changed_piece_ids': {'unknown'}},
                           {'records': {}, 'changed_piece_ids': {'selected'}}):
                with self.subTest(kwargs=kwargs), patch('scp.catalog.load_catalog', return_value=catalog), \
                        patch('scp.content.write_subject_content') as write_subject, \
                        patch('scp.inventory.write_inventories') as inventory:
                    with self.assertRaises(ValueError):
                        refresh_catalog_content(root, scope_to_changed=True, **kwargs)
                    write_subject.assert_not_called()
                    inventory.assert_not_called()


if __name__ == '__main__':
    unittest.main()
