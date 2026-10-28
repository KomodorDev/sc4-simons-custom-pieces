"""Reject valid S3D files that exceed the custom-piece rendering budget."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file()) / 'framework'))

from scp.models import ModelError, pack_s3d, parse_s3d, validate_s3d
from scp.verify import check_piece_models, check_piece_render_budget, S3D
from scp_hsr.test_support import donor


def oversized():
    model = parse_s3d(donor())
    model['meshes'][0]['name'] = b'SCP oversized regression fixture\0'
    model['indices'][0]['values'] *= 40
    model['primitives'][0] = [(0, 0, len(model['indices'][0]['values']))]
    validate_s3d(model)  # Structurally valid is insufficient for game rendering.
    return pack_s3d(model)


class RenderBudgetVerificationTests(unittest.TestCase):
    def setUp(self):
        self.spec = {'tile_ids': ['7f500000'], 'preview_id': '7f500ff5', 'footprint': [1,1]}
        self.resources = {(*S3D, key): donor()
                          for key in [*range(0x7f500000, 0x7f500005), 0x7f500ff5]}

    def test_every_zoom_is_checked_before_recipe_specific_geometry(self):
        self.resources[*S3D, 0x7f500004] = oversized()
        with patch('scp.verify._check_piece_geometry') as geometry:
            with self.assertRaises(ModelError):
                check_piece_models(self.resources, self.spec, None)
            geometry.assert_not_called()

    def test_placement_preview_is_checked_separately_from_tile_models(self):
        self.resources[*S3D, 0x7f500ff5] = oversized()
        with self.assertRaises(ModelError):
            check_piece_render_budget(self.resources, self.spec)

    def test_native_groups_keep_their_existing_independent_contract(self):
        model = parse_s3d(oversized())
        model['meshes'][0]['name'] = b'native donor fixture\0'
        self.resources[*S3D, 0x7f500000] = pack_s3d(model)
        self.assertTrue(check_piece_render_budget(self.resources, self.spec)
                        ['all_authored_groups_within_budget'])

    def test_preview_loader_rejects_oversized_export_before_drawing(self):
        try:
            from scp import preview
        except ModuleNotFoundError as error:
            if error.name == 'numpy':
                self.skipTest('NumPy preview dependency is unavailable')
            raise
        spec = {**self.spec, 'asset_file': 'piece.dat'}
        with patch('scp.preview.read_resource', return_value=oversized()):
            with self.assertRaises(ModelError):
                preview.read_piece_preview(Path('/tmp/scp-budget-fixture'), spec)


if __name__ == '__main__':
    unittest.main()
