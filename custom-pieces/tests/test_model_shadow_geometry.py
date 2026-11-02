"""Source geometry, native relative-pose math, and invisible carrier checks."""
from pathlib import Path
import math
import struct
import sys
import unittest

from PIL import Image

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.model_shadow_geometry import (DEFAULT_SUN, LOCAL_SUN, PACKED_POSITION_UV,
    encode_mask_fsh, generate_shadow_carriers, project_to_ground,
    referenced_model_triangles, rotate_y)
from scp.models import pack_s3d, parse_s3d, positions, validate_s3d
from scp.test_support import plane


class ModelShadowGeometryTests(unittest.TestCase):
    def setUp(self):
        self.ids = (0x7F508810, 0x7F508811, 0x7F508812, 0x7F508813)
        self.triangles = [
            ((-18., 15., -5.), (20., 15., -5.), (20., 15., 3.)),
            ((-18., 15., -5.), (20., 15., 3.), (-18., 15., 3.)),
            ((-12., 7.5, -3.), (13., 7.5, -3.), (13., 7.5, 5.)),
            ((0., .5, 12.), (2., .5, 12.), (3., 8., 3.)),
            # A vertical wall has a nonzero area shadow under the actual sun.
            ((22., 0., -2.), (22., 9., -2.), (22., 9., 4.)),
        ]

    def build(self, **kwargs):
        return generate_shadow_carriers(self.triangles, self.ids, **kwargs)

    def test_native_relative_selection_matches_original_all_sixteen_poses(self):
        self.assertEqual(rotate_y(DEFAULT_SUN, -1), LOCAL_SUN)
        for object_rotation in range(4):
            for camera_rotation in range(4):
                selected = (object_rotation - camera_rotation - 1) % 4
                world_sun = rotate_y(DEFAULT_SUN, camera_rotation)
                for triangle in self.triangles:
                    for point in triangle:
                        expected = project_to_ground(rotate_y(point, object_rotation), world_sun)
                        local = project_to_ground(rotate_y(point, selected), LOCAL_SUN)
                        transformed = rotate_y((local[0], 0., local[1]), camera_rotation + 1)
                        self.assertAlmostEqual(transformed[0], expected[0], places=11)
                        self.assertAlmostEqual(transformed[2], expected[1], places=11)

    def test_all_source_triangles_accounted_for_in_each_pose(self):
        result = self.build()
        for variant in result['report']['variants']:
            kept = variant['source_triangle_indices']
            edge_on = variant['edge_on_triangle_indices']
            self.assertFalse(set(kept) & set(edge_on))
            self.assertEqual(sorted(kept + edge_on), list(range(len(self.triangles))))
            self.assertIn(4, kept)
        self.assertFalse(result['report']['tile_clipping'])
        self.assertFalse(result['report']['in_game_tested'])
        self.assertFalse(result['report']['texture_alpha_sampled'])

    def test_overhang_and_different_deck_heights_remain_in_masks(self):
        result = self.build()
        for variant in result['report']['variants']:
            bounds = variant['projected_bounds_xz_m']
            pose = variant['relative_pose']
            for triangle in self.triangles:
                for point in triangle:
                    projected = project_to_ground(rotate_y(point, pose))
                    for axis in range(2):
                        self.assertLess(bounds[axis][0], projected[axis])
                        self.assertGreater(bounds[axis][1], projected[axis])
            self.assertTrue(any(abs(v) > 16 for pair in bounds for v in pair))
        lowered = [tuple((x, y / 2, z) for x, y, z in tri) for tri in self.triangles]
        other = generate_shadow_carriers(lowered, self.ids)
        self.assertNotEqual(result['textures'], other['textures'])

    def test_single_mesh_no_visible_primitives_and_affine_float32_quad(self):
        result = self.build()
        for raw, variant in zip(result['models'], result['report']['variants']):
            model = parse_s3d(raw)
            self.assertEqual(len(model['meshes']), 1)
            self.assertEqual(model['primitives'], [[]])
            self.assertEqual(model['vertices'][0]['format'], PACKED_POSITION_UV)
            self.assertEqual(len(positions(model['vertices'][0])), 4)
            self.assertEqual(validate_s3d(model)['triangles'], 0)
            self.assertEqual(model['materials'][0]['textures'],
                             [int(variant['texture_id'], 16)])
            points = positions(model['vertices'][0])
            self.assertEqual(max(p[1] for p in points) - min(p[1] for p in points), 64.)
            projected = [project_to_ground(p) for p in points]
            a, b, c, d = projected
            u = (b[0] - a[0], b[1] - a[1])
            v = (d[0] - a[0], d[1] - a[1])
            det = u[0] * v[1] - u[1] * v[0]
            self.assertGreater(abs(det), 1.)
            for point, expected in zip(projected, variant['quad_uv']):
                delta = point[0] - a[0], point[1] - a[1]
                actual = ((delta[0] * v[1] - delta[1] * v[0]) / det,
                          (u[0] * delta[1] - u[1] * delta[0]) / det)
                for actual_value, target in zip(actual, expected):
                    self.assertAlmostEqual(actual_value, target, places=6)
            self.assertLessEqual(variant['maximum_float32_projection_error_m'], 1e-4)

    def test_degenerate_fallback_also_has_zero_draw_area(self):
        for raw in self.build(draw_mode='degenerate-triangle')['models']:
            model = parse_s3d(raw)
            self.assertEqual(model['indices'][0]['values'], (0, 0, 0))
            self.assertEqual(model['primitives'], [[(0, 0, 3)]])
            self.assertEqual(validate_s3d(model)['triangles'], 1)
            point = positions(model['vertices'][0])[0]
            self.assertEqual([positions(model['vertices'][0])[i]
                              for i in model['indices'][0]['values']], [point] * 3)

    def test_normal_texture_masks_have_alpha_border_and_no_halo(self):
        result = self.build()
        for variant in result['report']['variants']:
            raw = result['textures'][int(variant['texture_id'], 16)]
            size = variant['mask_size']
            self.assertEqual(len(raw), 40 + size * size * 4)
            self.assertEqual(raw[:4], b'SHPI')
            self.assertEqual(struct.unpack_from('<2H', raw, 28), (size, size))
            alpha = Image.frombytes('RGBA', (size, size), raw[40:], 'raw', 'BGRA').getchannel('A')
            box = alpha.getbbox()
            self.assertIsNotNone(box)
            self.assertGreaterEqual(min(box[0], box[1]), 1)
            self.assertLess(max(box[2], box[3]), size)
            self.assertEqual(alpha.getpixel((0, 0)), 0)

    def test_source_extraction_ignores_unreferenced_vertices_and_keeps_vertical_faces(self):
        source = plane(-20., 20., -4., 4., 15.)
        source['vertices'][0]['data'] += struct.pack('<5f', 999., 999., 999., 0., 0.)
        raw = pack_s3d(source)
        triangles = referenced_model_triangles(raw)
        self.assertEqual(len(triangles), 2)
        self.assertFalse(any(999. in point for tri in triangles for point in tri))
        self.assertEqual(pack_s3d(source), raw)
        vertical = plane()
        vertical['vertices'][0]['data'] = b''.join(struct.pack('<5f', *p, 0., 0.)
            for p in ((4., 0., -2.), (4., 8., -2.), (4., 8., 2.), (4., 0., 2.)))
        self.assertEqual(len(referenced_model_triangles(pack_s3d(vertical))), 2)

    def test_source_extraction_rejects_unknown_model_transform(self):
        model = plane()
        model['trailing'][0] = (b'PROP', b'PROP' + struct.pack('<II', 12, 1))
        with self.assertRaisesRegex(ValueError, 'source model transforms'):
            referenced_model_triangles(pack_s3d(model))

    def test_bad_geometry_ids_and_budgets_fail_before_resources_are_returned(self):
        for triangles, ids in (([], self.ids), (self.triangles, self.ids[:3]),
                               (self.triangles, (1, 1, 2, 3)),
                               ([((0, 0, 0), (1, 1, 1), (2, 2, 2))], self.ids),
                               ([((0, 0, 0), (math.nan, 1, 0), (1, 2, 0))], self.ids)):
            with self.assertRaises(ValueError):
                generate_shadow_carriers(triangles, ids)
        for options in ({'maximum_texture_size': 128}, {'maximum_texture_size': 300},
                        {'supersample': 9}, {'metres_per_pixel': 0},
                        {'card_height_m': 0}, {'draw_mode': 'visible-quad'}):
            with self.assertRaises(ValueError):
                self.build(**options)
        with self.assertRaises(ValueError):
            encode_mask_fsh(Image.new('L', (16, 32)))

    def test_repeated_build_is_deterministic_and_does_not_mutate_input(self):
        snapshot = repr(self.triangles)
        self.assertEqual(self.build(), self.build())
        self.assertEqual(repr(self.triangles), snapshot)


if __name__ == '__main__':
    unittest.main()
