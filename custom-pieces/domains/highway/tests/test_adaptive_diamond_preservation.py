"""Saved-archive mutations must fail the independent preservation auditor."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = next(path for path in Path(__file__).resolve().parents if (path / 'project.jsonc').is_file())
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]
spec = importlib.util.spec_from_file_location('scp_adaptive_preservation_auditor',
    ROOT / 'domains/highway/tools/verify_adaptive_diamond.py')
auditor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auditor)

from scp.dbpf import encode_exemplar, pack_dbpf


class AdaptiveDiamondPreservationTests(unittest.TestCase):
    def setUp(self):
        self.reference_piece = {'id': 'saved-fixture', 'domain': 'highway', 'recipe': 'highway_fixture',
            'puzzle_id': 'f7c0', 'tile_ids': ['7f580000'], 'preview_id': '7f580ff5',
            'footprint': [1, 1], 'cells': [[0, 0]], 'orientation_count': 8,
            'effect_name': 'saved_fixture_effect', 'menu': {'id': '6a47f7c0'},
            'asset_file': 'zzz_Simons_Custom_Pieces/20_Pieces/SCP_saved-fixture.dat'}
        self.reference = {(*auditor.S3D, 0x7f580000 + zoom): b'saved canonical model' for zoom in range(5)}
        self.reference.update({(*auditor.SHADOW, 0x7f580000 + zoom): b'saved shadow' for zoom in range(5)})
        self.reference.update({(*auditor.PATH, 0x7f580000): b'saved canonical PATH',
            (*auditor.S3D, 0x7f580ff5): b'saved complete preview',
            (*auditor.EFFECT, 0x7f580ff5): b'saved preview effect',
            (0x2026960B, 0x2A592FD1, 0x7f580000): b'saved label',
            (*auditor.NETWORK, 0x7f580000): encode_exemplar({'parent': [0, 0, 0],
                'properties': [{'id': 0x10, 'type': 0x300, 'key_type': 0, 'values': [11]}]})})
        self.candidate_piece = deepcopy(self.reference_piece)
        self.candidate_piece['adaptive_ground'] = {'schema_version': 1, 'cells': [{
            'cell': [0, 0], 'resolved_tile_id': '7f59a000', 'rotation': 0,
            'texture_donor_id': '04003800', 'street_flags': '02020404',
            'avenue_flags': '01030103', 'prop': True}]}
        self.candidate = dict(self.reference)
        del self.candidate[*auditor.NETWORK, 0x7f580000]
        self.candidate.update({(*auditor.TEXTURE, 0x7f59a000 + appearance + zoom): b'copied appearance texture'
            for appearance in (0, 0x10, 0x20, 0x30) for zoom in range(5)})
        self.candidate.update({(*auditor.AVENUE_PATH, 0x7f59a000): b'posed runtime PATH',
            (*auditor.S3D, 0x7f580005): b'filtered active model',
            (*auditor.PROP, 0x7f580000): b'active prop', (*auditor.T21, 0x7f59a000): b'active T21'})

    def compare(self):
        return auditor.compare_piece_archive(self.reference_piece, self.candidate_piece,
            pack_dbpf(self.reference), pack_dbpf(self.candidate))

    def test_saved_canonical_resources_are_all_preserved(self):
        report = self.compare()
        self.assertEqual(report['added_runtime_resources'], 24)
        self.assertEqual(report['removed_network_exemplars'], 1)
        self.assertEqual(report['canonical_model_zooms_preserved'], 5)
        self.assertEqual(report['canonical_paths_preserved'], 1)
        self.assertEqual(report['canonical_shadows_preserved'], 5)
        self.assertTrue(all(row['reference_sha256'] == row['candidate_sha256']
                            for row in report['resources'] if row['status'] == 'unchanged'))

    def test_changed_canonical_path_is_rejected_from_saved_archive(self):
        self.candidate[*auditor.PATH, 0x7f580000] = b'changed canonical route'
        with self.assertRaisesRegex(ValueError, 'retained resource bytes changed'):
            self.compare()

    def test_changed_complete_preview_is_rejected_from_saved_archive(self):
        self.candidate[*auditor.S3D, 0x7f580ff5] = b'changed complete preview'
        with self.assertRaisesRegex(ValueError, 'retained resource bytes changed'):
            self.compare()

    def test_changed_canonical_zoom_is_rejected(self):
        self.candidate[*auditor.S3D, 0x7f580004] = b'changed distant zoom'
        with self.assertRaisesRegex(ValueError, 'retained resource bytes changed'):
            self.compare()

    def test_changed_static_dat_is_rejected_even_when_resource_closure_matches(self):
        self.candidate_piece = deepcopy(self.reference_piece)
        self.candidate = dict(self.reference)
        self.candidate[0x2026960B, 0x2A592FD1, 0x7f580000] = b'changed static label'
        with self.assertRaisesRegex(ValueError, 'unconverted asset DAT changed'):
            self.compare()

    def test_untouched_static_dat_is_byte_identical(self):
        self.candidate_piece = deepcopy(self.reference_piece)
        self.candidate = dict(self.reference)
        report = self.compare()
        self.assertTrue(report['dat_byte_identical'])
        self.assertEqual(report['added_runtime_resources'], 0)

    def test_removed_non_network_resource_is_rejected(self):
        del self.candidate[*auditor.EFFECT, 0x7f580ff5]
        with self.assertRaisesRegex(ValueError, 'removed beyond'):
            self.compare()

    def test_unexpected_runtime_resource_is_rejected(self):
        self.candidate[*auditor.PROP, 0x7f580100] = b'extra prop'
        with self.assertRaisesRegex(ValueError, 'additions differ'):
            self.compare()

    def test_omitted_exemplar_must_really_be_type_eleven(self):
        self.reference[*auditor.NETWORK, 0x7f580000] = encode_exemplar({'parent': [0, 0, 0],
            'properties': [{'id': 0x10, 'type': 0x300, 'key_type': 0, 'values': [4]}]})
        with self.assertRaisesRegex(ValueError, 'type-11'):
            self.compare()

    def test_piece_and_menu_identities_are_preserved(self):
        for field, value in (('puzzle_id', 'f7c1'), ('preview_id', '7f580ff6'), ('cells', [[1, 0]]),
                              ('tile_ids', ['7f580100'])):
            with self.subTest(field=field):
                self.candidate_piece[field] = value
                with self.assertRaisesRegex(ValueError, 'identity changed'):
                    self.compare()
                self.candidate_piece[field] = deepcopy(self.reference_piece[field])
        self.candidate_piece['menu']['id'] = '6a47f7c1'
        with self.assertRaisesRegex(ValueError, 'identity changed'):
            self.compare()


if __name__ == '__main__':
    unittest.main()
