"""Capture extraction must not require or rewrite unrelated cached records."""
from copy import deepcopy
from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scp.connectivity import PATH
from scp.dbpf import pack_dbpf
from scp_hsr.hsr_connections import main, materialize


def fixture_piece(identifier, *, draft=False):
    return {'id': identifier, 'domain': 'high-speed-rail', 'recipe': 'fixture',
            'status': 'draft' if draft else 'experimental', 'footprint': [1, 1],
            'cells': [[0, 0]], 'tile_ids': ['7f500000'], 'preview_id': '7f500ff5'}


RAW_PATH = b'SC4PATHS\n1.2\n1\n0\n0\n7\n0\n3\n1\n0\n2\n0,-8,15.5\n0,8,15.5\n'


def fixture_capture(directory, pieces, *, baseline=False):
    directory.mkdir(parents=True)
    for piece in pieces:
        (directory/(piece['id']+'.dat')).write_bytes(pack_dbpf({(*PATH, 0x7f500000): RAW_PATH}))
    if baseline:
        payload = {'pieces': {piece['id']: {'piece': piece, 'file': piece['id']+'.dat'} for piece in pieces}}
        filename = 'baseline.json'
    else:
        payload = {'pieces': [{**piece, 'asset_file': piece['id']+'.dat'} for piece in pieces]}
        filename = 'manifest.json'
    (directory/filename).write_text(json.dumps(payload))


class IntrinsicMaterializeTests(unittest.TestCase):
    def test_explicit_selection_accepts_single_use_iterables_and_both_source_formats(self):
        for baseline in (False, True):
            for selection_kind in ('list', 'tuple', 'generator'):
                with self.subTest(baseline=baseline, selection_kind=selection_kind), TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    first, second = fixture_piece('first'), fixture_piece('second')
                    source = root/'capture'
                    fixture_capture(source, [first], baseline=baseline)
                    # A captured sibling has no readable resources. Exact selection
                    # must not extract it or require its asset-file metadata.
                    filename = 'baseline.json' if baseline else 'manifest.json'
                    payload = json.loads((source/filename).read_text())
                    if baseline:
                        payload['pieces']['second'] = {'piece': second, 'file': 'must-not-read.dat'}
                    else:
                        payload['pieces'].append(second)
                    (source/filename).write_text(json.dumps(payload))
                    selection = {'list': ['first'], 'tuple': ('first',),
                                 'generator': (identifier for identifier in ['first'])}[selection_kind]
                    with patch('scp.catalog.load_catalog', return_value={'pieces': [first, second]}), \
                            patch('scp_hsr.hsr_connections.reviewed_contract', return_value=None), \
                            patch('scp.content.refresh_catalog_content', return_value={}) as refresh:
                        result = materialize(root, **{'baseline' if baseline else 'build': source}, piece_ids=selection)
                    self.assertEqual(result['extracted_piece_ids'], ['first'])
                    self.assertEqual(set(refresh.call_args.kwargs['records']), {'first'})
                    self.assertEqual(refresh.call_args.kwargs['changed_piece_ids'], frozenset({'first'}))
                    self.assertTrue(refresh.call_args.kwargs['scope_to_changed'])

    def test_explicit_invalid_selections_fail_before_resource_reads_or_writes(self):
        selections = ([], ['first', 'first'], ['draft'], ['unknown'], ['road'], ['missing'],
                      ['first', 'missing'], 'first', [None], [['first']])
        for baseline in (False, True):
            for identifiers in selections:
                for single_use in (False, True):
                    if isinstance(identifiers, str) and single_use:
                        continue
                    with self.subTest(baseline=baseline, identifiers=identifiers, single_use=single_use), TemporaryDirectory() as temporary:
                        root = Path(temporary)
                        first, missing = fixture_piece('first'), fixture_piece('missing')
                        road = {**fixture_piece('road'), 'domain': 'highway'}
                        catalog = {'pieces': [first, missing, road, fixture_piece('draft', draft=True)]}
                        source = root/'capture'
                        fixture_capture(source, [first], baseline=baseline)
                        selection = (value for value in identifiers) if single_use else identifiers
                        with patch('scp.catalog.load_catalog', return_value=catalog), \
                                patch('pathlib.Path.read_bytes', side_effect=AssertionError('No resource reads before selection validation')), \
                                patch('pathlib.Path.write_text') as write_text, \
                                patch('pathlib.Path.write_bytes') as write_bytes, \
                                patch('scp.content.refresh_catalog_content') as refresh:
                            with self.assertRaises(ValueError):
                                materialize(root, **{'baseline' if baseline else 'build': source}, piece_ids=selection)
                            refresh.assert_not_called()
                            write_text.assert_not_called()
                            write_bytes.assert_not_called()

    def test_all_selected_source_definitions_are_checked_before_any_write(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            first, second = fixture_piece('first'), fixture_piece('second')
            source = root/'capture'
            fixture_capture(source, [first, {**second, 'preview_id': '7f600ff5'}])
            with patch('scp.catalog.load_catalog', return_value={'pieces': [first, second]}), \
                    patch('scp_hsr.hsr_connections.reviewed_contract', return_value=None), \
                    patch('pathlib.Path.write_text') as write_text, \
                    patch('pathlib.Path.write_bytes') as write_bytes, \
                    patch('scp.content.refresh_catalog_content') as refresh:
                with self.assertRaisesRegex(ValueError, 'second: preview_id differs'):
                    materialize(root, build=source, piece_ids=['first', 'second'])
                refresh.assert_not_called()
                write_text.assert_not_called()
                write_bytes.assert_not_called()

    def test_exact_extraction_with_real_refresh_preserves_all_unselected_evidence(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            first, second = fixture_piece('first'), fixture_piece('second')
            source = root/'capture'
            fixture_capture(source, [first])
            domain = root/'domains/high-speed-rail'
            assembly_path = 'domains/high-speed-rail/01_assemblies/affected'
            catalog = {'pieces': [first, second],
                       'domains': {'high-speed-rail': {'path': 'domains/high-speed-rail', 'name': 'HSR'}},
                       '_assemblies': [{'id': 'affected', 'path': assembly_path,
                                        'scene': {'instances': [{'piece_id': 'first'}, {'piece_id': 'second'}]}}]}
            protected = [domain/'connection-classes.jsonc', domain/'00_pieces/INVENTORY.md']
            for directory in (domain/'00_pieces/second', root/assembly_path):
                protected.extend(directory/name for name in ('connections.json', 'checks/manual-tests.json', 'README.md'))
            for path in protected:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b'Preserve this cached evidence without parsing it.\n')
            before = {path: path.read_bytes() for path in protected}
            with patch('scp.catalog.load_catalog', return_value=catalog), \
                    patch('scp_hsr.hsr_connections.reviewed_contract', return_value=None), \
                    patch('scp.connectivity.assembly_connectivity', side_effect=AssertionError('No implicit assembly extraction')), \
                    patch('scp.inventory.write_inventories', side_effect=AssertionError('No global inventory refresh')):
                result = materialize(root, build=source, piece_ids=(identifier for identifier in ['first']))
            self.assertEqual(result['extracted_piece_ids'], ['first'])
            self.assertEqual(result['deferred_assembly_ids'], ['affected'])
            self.assertEqual((result['pieces'], result['assemblies']), (1, 0))
            self.assertEqual(before, {path: path.read_bytes() for path in protected})
            self.assertTrue((domain/'00_pieces/first/connections.json').is_file())
            self.assertTrue((domain/'00_pieces/first/checks/manual-tests.json').is_file())

    def test_cli_forwards_repeated_exact_piece_selection(self):
        argv = ['hsr_connections', '--root', 'library', '--build', 'compiled',
                '--piece', 'first', '--piece', 'second']
        with patch('sys.argv', argv), patch('scp_hsr.hsr_connections.materialize', return_value={}) as extract, \
                redirect_stdout(StringIO()):
            main()
        extract.assert_called_once_with(Path('library'), baseline=None, build=Path('compiled'),
                                        piece_ids=['first', 'second'])

    def test_only_captured_non_drafts_are_extracted_and_refreshed(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            build = root/'dist/capture'
            build.mkdir(parents=True)
            captured = fixture_piece('captured')
            cached = fixture_piece('unrelated-cached')
            uncached = fixture_piece('unrelated-uncached')
            draft = fixture_piece('unfinished', draft=True)
            legacy_path = root/'unrelated-cached/connections.json'
            legacy_path.parent.mkdir()
            legacy_bytes = b'{"ports":[{"compatible_counterparts":[{"piece_id":"historical"}]}]}\n'
            legacy_path.write_bytes(legacy_bytes)
            raw = b'SC4PATHS\n1.2\n1\n0\n0\n7\n0\n3\n1\n0\n2\n0,-8,15.5\n0,8,15.5\n'
            (build/'captured.dat').write_bytes(pack_dbpf({(*PATH, 0x7f500000): raw}))
            manifest_pieces = [{**captured, 'asset_file': 'captured.dat'},
                               {**draft, 'asset_file': 'does-not-exist.dat'}]
            (build/'manifest.json').write_text(json.dumps({'pieces': manifest_pieces}))
            catalog = {'pieces': [cached, draft, captured, uncached]}
            before = deepcopy(catalog)
            with patch('scp.catalog.load_catalog', return_value=catalog), \
                    patch('scp_hsr.hsr_connections.reviewed_contract', return_value=None), \
                    patch('scp.connectivity.link_counterparts', side_effect=AssertionError('No catalogue matching')), \
                    patch('scp.content.refresh_catalog_content', return_value={'refreshed': True}) as refresh:
                result = materialize(root, build=build)
            self.assertEqual(refresh.call_count, 1)
            call = refresh.call_args
            self.assertEqual(call.args, (root.resolve(),))
            self.assertEqual(set(call.kwargs['records']), {'captured'})
            self.assertEqual(call.kwargs['changed_piece_ids'], frozenset({'captured'}))
            record = call.kwargs['records']['captured']
            self.assertEqual(record['subject_id'], 'captured')
            self.assertTrue(record['ports'])
            self.assertTrue(all('compatible_counterparts' not in port for port in record['ports']))
            self.assertEqual(result['extracted_piece_ids'], ['captured'])
            self.assertEqual(result['skipped_draft_piece_ids'], ['unfinished'])
            self.assertFalse(result['counterpart_matching_performed'])
            self.assertEqual(legacy_path.read_bytes(), legacy_bytes)
            self.assertEqual(catalog, before)

    def test_empty_capture_passes_an_explicit_empty_change_set(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            build = root/'build'
            build.mkdir()
            (build/'manifest.json').write_text('{"pieces": []}')
            with patch('scp.catalog.load_catalog', return_value={'pieces': [fixture_piece('not-captured')]}), \
                    patch('scp.content.refresh_catalog_content', return_value={}) as refresh:
                result = materialize(root, build=build)
            self.assertEqual(refresh.call_args.kwargs, {'records': {}, 'changed_piece_ids': frozenset()})
            self.assertEqual(result['extracted_piece_ids'], [])


if __name__ == '__main__':
    unittest.main()
