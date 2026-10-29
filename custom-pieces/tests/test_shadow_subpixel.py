"""Bounded structural-shadow quantization, using the actual rasterizer."""
from pathlib import Path
import sys
import unittest

from PIL import Image

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.models import pack_s3d
from scp.shadows import (
    PATH, SHADOW, S3D, ZOOM_SIZES, build_shadows, decode_shadow_fsh,
    encode_shadow_fsh, validate_piece_shadows,
)
from scp.test_support import plane

TILE = 0x7F584210
EMPTY_PATH = b'SC4PATHS\r\n1.2\r\n0\r\n0\r\n0\r\n'
TRAFFIC_PATH = (b'SC4PATHS\r\n1.2\r\n1\r\n0\r\n0\r\n'
                b'7\r\n0\r\n3\r\n1\r\n0\r\n2\r\n'
                b'0,-8,15.5\r\n0,8,15.5\r\n')


def fixture(model=None):
    # A12mm by30mm real corner sliver. Its8,16,32,64px masks are
    # transparent; its128px mask has one nonzero pixel with alpha8.
    model = model if model is not None else pack_s3d(plane(7.988, 8., -8., -7.97))
    resources = {(*S3D, TILE+zoom): model for zoom in range(5)}
    resources.update(build_shadows(model, TILE))
    resources[*PATH, TILE] = EMPTY_PATH
    piece = {'tile_ids': [f'{TILE:08x}'], 'cells': [[2, 1]], 'structural_cells': [[2, 1]]}
    return resources, piece


class StructuralSubpixelShadowTests(unittest.TestCase):
    def test_actual_geometry_quantizes_only_leading_coarse_structural_zooms_to_zero(self):
        resources, piece = fixture()
        original = dict(resources)
        masks = [decode_shadow_fsh(resources[*SHADOW, TILE+zoom]).getchannel('A')
                 for zoom in range(5)]
        self.assertEqual([mask.getbbox() for mask in masks],
                         [None, None, None, None, (127, 0, 128, 1)])
        self.assertEqual(sum(masks[-1].tobytes()), 8)
        report = validate_piece_shadows(resources, piece)
        self.assertEqual(resources, original)
        self.assertTrue(report['silhouettes_match_actual_s3d_geometry'])
        self.assertTrue(report['all_five_zoom_resources_valid'])
        evidence = report['subpixel_structural_zooms']
        self.assertEqual(len(evidence), 1)
        self.assertEqual(evidence[0]['tile'], f'{TILE:08x}')
        self.assertEqual(evidence[0]['cell'], [2, 1])
        self.assertEqual(evidence[0]['empty_zoom_indices'], [0, 1, 2, 3])
        self.assertEqual(evidence[0]['first_visible_zoom_index'], 4)
        self.assertEqual(evidence[0]['first_visible_width'], 128)
        self.assertTrue(all(item['alpha_bbox'] is None and item['coverage_pixels'] == 0.
                            and item['subpixel_structural_coverage']
                            for item in report['images'][:4]))
        self.assertFalse(report['in_game_shadow_selection_tested'])

    def test_undeclared_structural_cell_or_actual_traffic_path_cannot_use_the_exception(self):
        resources, piece = fixture()
        for changed in ({**piece, 'structural_cells': []},
                        {**piece, 'structural_cells': [[3, 1]]},
                        {'tile_ids': [f'{TILE:08x}']}):
            with self.subTest(piece=changed), self.assertRaisesRegex(ValueError, 'declared structural'):
                validate_piece_shadows(resources, changed)
        resources[*PATH, TILE] = TRAFFIC_PATH
        with self.assertRaisesRegex(ValueError, 'empty structural PATH header'):
            validate_piece_shadows(resources, piece)

    def test_missing_or_malformed_empty_path_header_is_rejected(self):
        resources, piece = fixture()
        no_path = dict(resources)
        del no_path[*PATH, TILE]
        with self.assertRaisesRegex(ValueError, 'PATH resource'):
            validate_piece_shadows(no_path, piece)
        resources[*PATH, TILE] = EMPTY_PATH+b'0\r\n'
        with self.assertRaisesRegex(ValueError, 'empty structural PATH header'):
            validate_piece_shadows(resources, piece)

    def test_all_five_transparent_masks_are_rejected_even_with_real_off_tile_geometry(self):
        resources, piece = fixture(pack_s3d(plane(9., 12.)))
        self.assertTrue(all(decode_shadow_fsh(resources[*SHADOW, TILE+n]).getchannel('A').getbbox() is None
                            for n in range(5)))
        with self.assertRaisesRegex(ValueError, 'highest zoom'):
            validate_piece_shadows(resources, piece)

    def test_nonprefix_empty_zooms_are_rejected_using_a_real_sampling_counterexample(self):
        # The8px lattice samples this20mm square; the16/32/64px lattices
        # miss it;128px resolves it again. The exception intentionally admits
        # only a leading empty prefix, so this oscillating case stays rejected.
        resources, piece = fixture(pack_s3d(plane(-7.885, -7.865, -7.885, -7.865)))
        visible = [decode_shadow_fsh(resources[*SHADOW, TILE+n]).getchannel('A').getbbox() is not None
                   for n in range(5)]
        self.assertEqual(visible, [True, False, False, False, True])
        with self.assertRaisesRegex(ValueError, 'leading coarser zooms'):
            validate_piece_shadows(resources, piece)

    def test_different_zoom_models_are_rejected_even_when_their_shadow_projections_match(self):
        resources, piece = fixture()
        changed = pack_s3d(plane(7.988, 8., -8., -7.97, height=30.5))
        resources[*S3D, TILE+4] = changed
        self.assertEqual(resources[*SHADOW, TILE+4], build_shadows(changed, TILE)[*SHADOW, TILE+4])
        with self.assertRaisesRegex(ValueError, 'identical S3D geometry'):
            validate_piece_shadows(resources, piece)

    def test_tampered_shadow_bytes_fail_before_the_structural_exception(self):
        resources, piece = fixture()
        for zoom in (0, 4):
            with self.subTest(zoom=zoom):
                changed = dict(resources)
                mask = Image.new('L', (ZOOM_SIZES[zoom], ZOOM_SIZES[zoom]), 0)
                if zoom == 0:
                    mask.putpixel((0, 0), 255)
                changed[*SHADOW, TILE+zoom] = encode_shadow_fsh(mask)
                with self.assertRaisesRegex(ValueError, 'differs from actual S3D'):
                    validate_piece_shadows(changed, piece)

    def test_normal_nonempty_shadows_keep_their_existing_behavior(self):
        resources, _ = fixture(pack_s3d(plane()))
        resources.pop((*PATH, TILE))
        report = validate_piece_shadows(resources, {'tile_ids': [TILE]})
        self.assertEqual(report['subpixel_structural_zooms'], [])
        self.assertTrue(all(item['alpha_bbox'] is not None for item in report['images']))


if __name__ == '__main__':
    unittest.main()
