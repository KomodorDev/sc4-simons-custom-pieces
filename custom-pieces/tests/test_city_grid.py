"""Independent checks for the city grid's coordinates and actual raster use."""
from __future__ import annotations

import json
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))
from scp.models import parse_s3d, pack_s3d
from scp_hsr.test_support import donor
try:
    import numpy as np
    from scp.city_grid import make_camera, make_city_grid, tile_boundaries, world_to_s3d
    from scp.preview import model_triangles, render_fast_view, render_view
except ModuleNotFoundError:
    np = None


@unittest.skipIf(np is None, 'NumPy preview dependency is unavailable')
class CityGridTests(unittest.TestCase):
    def setUp(self):
        self.model = parse_s3d(donor())
        self.vertices = np.concatenate([position for position, uv, texture in model_triangles(self.model)])
        self.textures = {0x0bf6e09b: np.ones((4, 4, 4))}
        self.bounds = (-40, -40, 40, 40)

    def camera(self, azimuth=0, elevation=90, **kwargs):
        return make_camera(self.vertices, azimuth, elevation, 480, 400,
                           bounds_world_m=self.bounds, padding=70, **kwargs)

    def test_north_is_negative_s3d_z_and_up_in_north_up_plan(self):
        np.testing.assert_array_equal(world_to_s3d(32, 48, 15.5), [32, 15.5, -48])
        camera = self.camera()
        origin = camera.project_world(0, 0)
        east = camera.project_world(16, 0)
        north = camera.project_world(0, 16)
        self.assertGreater(east[0], origin[0])
        self.assertAlmostEqual(east[1], origin[1])
        self.assertAlmostEqual(north[0], origin[0])
        self.assertLess(north[1], origin[1])

    def test_boundaries_are_half_a_tile_from_signed_tile_centres(self):
        self.assertEqual(tile_boundaries(-40, 40), [-40, -24, -8, 8, 24, 40])
        self.assertNotIn(0, tile_boundaries(-40, 40))
        self.assertEqual(tile_boundaries(-24, 56, origin=16), [-24, -8, 8, 24, 40, 56])
        for boundary in tile_boundaries(-120, 200):
            self.assertEqual((boundary - 8) % 16, 0)

    def test_grid_origin_and_world_points_use_exact_model_camera(self):
        camera = self.camera(45, 36)
        image, metadata = make_city_grid(camera, self.bounds)
        np.testing.assert_array_equal(metadata['origin_pixel'], camera.project_s3d([0, 0, 0]))
        for line in metadata['grid_lines']:
            coordinate = line['coordinate_m']
            if line['axis'] == 'east':
                expected = [[coordinate, 0, 40], [coordinate, 0, -40]]
            else:
                expected = [[-40, 0, -coordinate], [40, 0, -coordinate]]
            np.testing.assert_allclose(line['pixels'], camera.project_s3d(expected), atol=1e-12)
        self.assertEqual(metadata['tile_metres'], 16)
        self.assertEqual({arrow['direction'] for arrow in metadata['direction_arrows']}, {'N', 'E'})
        self.assertGreater(metadata['tile_scale']['east_pixels'], 0)
        self.assertEqual(image.size, (480, 400))
        json.dumps(metadata, allow_nan=False)

    def test_oblique_basis_matches_independent_expected_projection(self):
        camera = self.camera(45, 30)
        root_half = math.sqrt(.5)
        np.testing.assert_allclose(camera.right, [root_half, 0, -root_half], atol=1e-12)
        np.testing.assert_allclose(camera.up, [-root_half / 2, math.sqrt(3) / 2, -root_half / 2], atol=1e-12)
        basis = np.stack((camera.right, camera.up, camera.towards))
        np.testing.assert_allclose(basis @ basis.T, np.eye(3), atol=1e-12)
        delta_east = camera.project_world(16, 0) - camera.project_world(0, 0)
        delta_north = camera.project_world(0, 16) - camera.project_world(0, 0)
        np.testing.assert_allclose(delta_east / camera.scale, [16 * root_half, 8 * root_half])
        np.testing.assert_allclose(delta_north / camera.scale, [16 * root_half, -8 * root_half])

    def test_southwest_origin_labels_exact_twenty_by_twenty_three_tile_rectangle(self):
        bounds = (-120, -216, 200, 152)
        origin = (-112, -208)
        camera = make_camera(self.vertices, 0, 90, 1400, 1600,
                             bounds_world_m=bounds, padding=90)
        image, metadata = make_city_grid(camera, bounds, origin_world_m=origin)
        east = [label for label in metadata['tile_labels'] if label['axis'] == 'X']
        north = [label for label in metadata['tile_labels'] if label['axis'] == 'Y']
        self.assertEqual([label['text'] for label in east], [f'X{index}' for index in range(20)])
        self.assertEqual([label['text'] for label in north], [f'Y{index}' for index in range(23)])
        self.assertEqual([label['tile_index'] for label in east], list(range(20)))
        self.assertEqual([label['tile_index'] for label in north], list(range(23)))
        self.assertTrue(all('+' not in label['text'] and '-' not in label['text']
                            for label in metadata['tile_labels']))
        basis = metadata['display_coordinate_basis']
        self.assertEqual(metadata['display_axis_labels'], {'east': 'X', 'north': 'Y'})
        self.assertFalse(metadata['origin_marker_visible'])
        self.assertEqual(basis['east_index_range'], [0, 19])
        self.assertEqual(basis['north_index_range'], [0, 22])
        self.assertFalse(basis['authoring_world_coordinates_changed'])
        self.assertEqual(metadata['east_boundaries_m'], list(range(-120, 201, 16)))
        self.assertEqual(metadata['north_boundaries_m'], list(range(-216, 153, 16)))
        self.assertEqual(metadata['east_boundaries_m'][0], origin[0] - 8)
        self.assertEqual(metadata['north_boundaries_m'][0], origin[1] - 8)
        self.assertEqual(metadata['east_boundaries_m'][1], origin[0] + 8)
        self.assertEqual(metadata['north_boundaries_m'][1], origin[1] + 8)
        for axis in ('east_boundaries_m', 'north_boundaries_m'):
            self.assertTrue(all(second - first == 16 for first, second in
                                zip(metadata[axis], metadata[axis][1:])))

    def test_crossing_is_display_tile_seven_thirteen_without_moving_authoring_world(self):
        bounds = (-120, -216, 200, 152)
        origin = (-112, -208)
        original_bytes = pack_s3d(self.model)
        for azimuth, elevation in ((0, 90), (45, 31), (225, 31)):
            with self.subTest(azimuth=azimuth):
                camera = make_camera(self.vertices, azimuth, elevation, 1400, 1600,
                                     bounds_world_m=bounds, padding=90)
                background, metadata = make_city_grid(camera, bounds, origin_world_m=origin)
                self.assertEqual(metadata['origin_world_m'], [-112, -208])
                np.testing.assert_allclose(metadata['origin_pixel'],
                                           camera.project_s3d([-112, 0, 208]))
                crossing_display = [(0 - origin[0]) / 16, (0 - origin[1]) / 16]
                self.assertEqual(crossing_display, [7, 13])
                np.testing.assert_allclose(camera.project_world(origin[0] + 7 * 16,
                                                                origin[1] + 13 * 16),
                                           camera.project_s3d([0, 0, 0]))
                self.assertEqual(original_bytes, pack_s3d(self.model))

    def test_generic_negative_coordinate_labels_keep_minus_without_positive_plus(self):
        background, metadata = make_city_grid(self.camera(), self.bounds)
        east = [label['text'] for label in metadata['tile_labels'] if label['axis'] == 'X']
        self.assertEqual(east, ['X-2', 'X-1', 'X0', 'X1', 'X2'])

    def test_grid_retains_origin_metadata_without_drawing_origin_artwork(self):
        from PIL import Image, ImageDraw

        # Record actual drawing operations, so a hidden origin flag alone
        # cannot pass while an origin cross/ring or caption is still rendered.
        draw = ImageDraw.Draw(Image.new('RGB', (480, 400)))
        with patch('scp.city_grid.ImageDraw.Draw', return_value=draw):
            with patch.object(draw, 'ellipse', wraps=draw.ellipse) as ellipses, \
                    patch.object(draw, 'line', wraps=draw.line) as lines, \
                    patch.object(draw, 'text', wraps=draw.text) as texts:
                background, metadata = make_city_grid(self.camera(45, 36), self.bounds)

        self.assertFalse(metadata['origin_marker_visible'])
        np.testing.assert_array_equal(metadata['origin_pixel'],
                                      self.camera(45, 36).project_world(0, 0))
        ellipses.assert_not_called()
        self.assertEqual(lines.call_count, len(metadata['grid_lines']) + 2)
        written = [call.args[1] for call in texts.call_args_list]
        expected = [label['text'] for label in metadata['tile_labels']]
        self.assertEqual(written, expected + ['E', 'N', '1 tile = 16 m | labels mark tile centres'])
        self.assertTrue(all('origin' not in text.lower() and ',' not in text for text in written))

    def test_camera_frames_model_heights_and_ground_corners_together(self):
        vertices = np.concatenate((self.vertices, [[0, 150, 0]]))
        camera = make_camera(vertices, 225, 36, 480, 400, bounds_world_m=self.bounds, padding=70)
        ground = [[-40, 0, -40], [-40, 0, 40], [40, 0, -40], [40, 0, 40]]
        pixels = camera.project_s3d(np.concatenate((vertices, ground)))
        self.assertGreaterEqual(pixels[:, 0].min(), 70 - 1e-9)
        self.assertLessEqual(pixels[:, 0].max(), 410 + 1e-9)
        self.assertGreaterEqual(pixels[:, 1].min(), 70 - 1e-9)
        self.assertLessEqual(pixels[:, 1].max(), 330 + 1e-9)

    def test_raster_keeps_grid_behind_geometry_and_preserves_model_bytes(self):
        original_bytes = pack_s3d(self.model)
        camera = self.camera()
        background, metadata = make_city_grid(camera, self.bounds)
        plain, plain_depth = render_fast_view(self.model, self.textures, 0, 90, 480, 400,
                                             camera=camera, return_depth=True)
        image, depth = render_fast_view(self.model, self.textures, 0, 90, 480, 400,
                                       camera=camera, background_image=background, return_depth=True)
        opaque = np.isfinite(depth)
        self.assertTrue(opaque.any())
        self.assertTrue((~opaque).any())
        np.testing.assert_array_equal(depth, plain_depth)
        np.testing.assert_array_equal(np.asarray(image)[opaque], np.asarray(plain)[opaque])
        np.testing.assert_array_equal(np.asarray(image)[~opaque], np.asarray(background)[~opaque])
        self.assertFalse(np.array_equal(np.asarray(plain)[~opaque], np.asarray(image)[~opaque]))
        self.assertEqual(original_bytes, pack_s3d(self.model))

    def test_optional_camera_does_not_change_default_render_pixels(self):
        for azimuth, elevation in ((0, 90), (45, 36), (225, 36)):
            with self.subTest(azimuth=azimuth, elevation=elevation):
                expected = render_view(self.model, self.textures, azimuth, elevation, 320, 240)
                actual = render_fast_view(self.model, self.textures, azimuth, elevation, 320, 240)
                self.assertEqual(expected.tobytes(), actual.tobytes())

    def test_mismatched_background_or_camera_is_rejected(self):
        from PIL import Image
        with self.assertRaisesRegex(ValueError, 'Background image size'):
            render_fast_view(self.model, self.textures, 0, 90, 480, 400,
                             camera=self.camera(), background_image=Image.new('RGB', (1, 1)))
        with self.assertRaisesRegex(ValueError, 'camera angles'):
            render_fast_view(self.model, self.textures, 45, 36, 480, 400, camera=self.camera())
        with self.assertRaisesRegex(ValueError, 'camera image size'):
            render_fast_view(self.model, self.textures, 0, 90, 320, 240, camera=self.camera())


if __name__ == '__main__':
    unittest.main()
