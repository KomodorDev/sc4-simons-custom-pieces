"""Saved review refresh rejects corrupt evidence and keeps consolidated views."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp.content import new_manual_record

SPEC = importlib.util.spec_from_file_location(
    'scp_test_review_refresh', ROOT / 'domains/high-speed-rail/tools/apply_junction_review.py')
REVIEW = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REVIEW)


def evidence():
    return {
        'source_build_version': 'reviewed-build',
        'reviewed_piece_count': 3, 'flagged_piece_count': 1,
        'verdict_counts': {'review-needed': 1, 'no-objection-recorded': 2},
        'flagged_piece_ids_by_verdict': {'review-needed': ['flagged']},
        'pieces': [
            {'id': 'flagged', 'verdict': 'review-needed', 'flag_recommended': True,
             'reason_codes': ['clustered-supports'], 'reasons': ['Two piers are too close.']},
            {'id': 'cleared', 'verdict': 'no-objection-recorded', 'flag_recommended': False,
             'reason_codes': [], 'reasons': []},
            {'id': 'later', 'verdict': 'no-objection-recorded', 'flag_recommended': False,
             'reason_codes': [], 'reasons': []},
        ],
    }


class ReviewRefreshTests(unittest.TestCase):
    def setUp(self):
        self.known = {identifier: {'id': identifier, 'domain': 'high-speed-rail'}
                      for identifier in ('flagged', 'cleared', 'later')}

    def test_saved_current_review_counts_and_flags_validate_without_mutation(self):
        path = ROOT / 'domains/high-speed-rail/junction-design-review.json'
        raw = path.read_bytes()
        review = json.loads(raw)
        known = {piece['id']: piece for piece in REVIEW.load_catalog(ROOT)['pieces']}
        result = REVIEW.validate_saved_review(review, known)
        self.assertEqual(result['counts'], {'no-objection-recorded': 98, 'review-needed': 32})
        self.assertEqual(len(result['flagged']), 32)
        self.assertEqual(path.read_bytes(), raw)

    def test_corrupt_review_records_fail_before_any_mutation(self):
        changes = (
            lambda value: value['pieces'].append(deepcopy(value['pieces'][0])),
            lambda value: value['pieces'][0].update(id='deleted-piece'),
            lambda value: value.update(reviewed_piece_count=4),
            lambda value: value.update(flagged_piece_count=2),
            lambda value: value['verdict_counts'].update({'review-needed': 2}),
            lambda value: value['flagged_piece_ids_by_verdict'].update({'review-needed': ['cleared']}),
            lambda value: value['pieces'][0].update(flag_recommended=False),
            lambda value: value['pieces'][0].update(verdict='unrecognized-verdict'),
            lambda value: value['pieces'][0].update(reasons=[]),
        )
        for change in changes:
            value = evidence()
            change(value)
            with self.subTest(review=value), self.assertRaises(ValueError):
                REVIEW.validate_saved_review(value, self.known)

    def test_another_domain_cannot_be_written_through_the_rail_path(self):
        known = deepcopy(self.known)
        known['flagged']['domain'] = 'highway'
        with self.assertRaisesRegex(ValueError, 'another domain'):
            REVIEW.validate_saved_review(evidence(), known)

    def test_refresh_uses_piece_readmes_preserves_records_and_never_recreates_guide(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'project.json').write_text('{}\n')
            domain = root / 'domains/high-speed-rail'
            domain.mkdir(parents=True)
            review_path = domain / 'junction-design-review.json'
            review_path.write_text(json.dumps(evidence(), indent=2)+'\n')
            review_bytes = review_path.read_bytes()
            collections_path = domain / 'collections.json'
            collections_path.write_text(json.dumps({'collections': {
                'ordinary': ['cleared'], 'junctions-needing-redesign': ['cleared']}})+'\n')
            observations = {}
            connections = {}
            for identifier in self.known:
                local = domain / '00_pieces' / identifier
                (local / 'checks').mkdir(parents=True)
                piece = {'id': identifier, 'name': identifier.title(), 'domain': 'high-speed-rail',
                         'footprint': [1, 1], 'description': 'Fixture '+identifier+'.'}
                if identifier in ('cleared', 'later'):
                    piece['design_review'] = {
                        'status': 'review-needed', 'summary': 'Keep the relevant observation.',
                        'reasons': ['Explicit support concern.'],
                        'reviewed_build': 'reviewed-build' if identifier == 'cleared' else 'newer-build'}
                (local / 'piece.json').write_text(json.dumps(piece, indent=2)+'\n')
                (local / 'README.md').write_text('# Fixture\n\nKeep this authored paragraph exactly.\n')
                connection = {'subject_id': identifier, 'source': {'resource_fingerprints': {}},
                              'ports': [], 'journeys': [], 'forbidden_transfers': []}
                record = new_manual_record(identifier, 'piece', connection, {})
                connections[local / 'connections.json'] = json.dumps(connection).encode()
                observations[local / 'checks/manual-tests.json'] = json.dumps(record).encode()
            for file, raw in {**connections, **observations}.items():
                file.write_bytes(raw)

            def catalog(_):
                return {'version': 'fixture', 'domains': {'high-speed-rail': {
                    'path': 'domains/high-speed-rail', 'name': 'High-speed rail'}},
                    'pieces': [json.loads((domain / '00_pieces' / identifier / 'piece.json').read_text())
                               for identifier in self.known],
                    'piece_sets': json.loads(collections_path.read_text())['collections'],
                    '_assemblies': []}

            with patch.object(REVIEW, 'load_catalog', side_effect=catalog), patch(
                    'scp.catalog.load_catalog', side_effect=catalog), patch(
                    'scp.inventory.load_catalog', side_effect=catalog):
                result = REVIEW.apply_saved_review(root)
                generated = {file: file.read_bytes() for file in root.rglob('*') if file.is_file()}
                REVIEW.apply_saved_review(root)
                self.assertEqual(generated, {file: file.read_bytes()
                                             for file in root.rglob('*') if file.is_file()})
            self.assertEqual(result['flagged'], 1)
            self.assertFalse(result['game_models_changed'])
            self.assertFalse(result['installed'])
            self.assertEqual(review_path.read_bytes(), review_bytes)
            for file, raw in {**connections, **observations}.items():
                self.assertEqual(file.read_bytes(), raw)
            selected = json.loads(collections_path.read_text())['collections']
            self.assertEqual(selected['ordinary'], ['cleared'])
            self.assertEqual(selected['flagged-junctions'], ['flagged'])
            self.assertEqual(selected['junctions-needing-review'], ['flagged'])
            self.assertNotIn('junctions-needing-redesign', selected)
            flagged = domain / '00_pieces/flagged/README.md'
            self.assertIn('Keep this authored paragraph exactly.', flagged.read_text())
            self.assertIn('**REVIEW NEEDED**', flagged.read_text())
            self.assertIn('## Connections and journeys', flagged.read_text())
            self.assertIn('## Test checklist', flagged.read_text())
            cleared = json.loads((domain / '00_pieces/cleared/piece.json').read_text())
            later = json.loads((domain / '00_pieces/later/piece.json').read_text())
            self.assertNotIn('design_review', cleared)
            self.assertEqual(later['design_review']['reviewed_build'], 'newer-build')
            inventory = domain / '00_pieces/INVENTORY.md'
            self.assertIn('flagged/README.md#design-review', inventory.read_text())
            self.assertTrue((domain / '01_assemblies/INVENTORY.md').is_file())
            self.assertFalse((domain / 'docs').exists())


if __name__ == '__main__':
    unittest.main()
