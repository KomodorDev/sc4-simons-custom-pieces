"""Assembly artwork shows actual placed routes while retaining native states."""
from io import BytesIO
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from PIL import Image

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.menu_experiment_resources import make_assembly_icon, validate_assembly_icon
from scp_hsr.icons import assembly_icon_routes


class AssemblyIconTests(unittest.TestCase):
    def test_placed_routes_use_the_piece_definition_and_actual_cardinal_pose(self):
        pieces = [{'id': 'one', 'recipe': 'example_recipe'}]
        scene = {'placements': [
            {'piece_id': 'one', 'origin_m': [32., -16.], 'rotation_degrees_ccw': 90},
            {'piece_id': 'one', 'origin_m': [-16., 64.], 'rotation_degrees': 270},
        ]}
        source = {'out': [(2., -8., 15.5), (2., 8., 30.5)]}
        with patch('scp_hsr.hsr_components_layout.component_routes', return_value=source) as provider:
            actual = assembly_icon_routes(scene, pieces)
        self.assertEqual(actual, [[(40., -14., 15.5), (24., -14., 30.5)],
                                  [(-24., 62., 15.5), (-8., 62., 30.5)]])
        self.assertEqual([call.args for call in provider.call_args_list],
                         [('example_recipe',), ('example_recipe',)])
        self.assertEqual(source['out'], [(2., -8., 15.5), (2., 8., 30.5)])

    def test_actual_north_up_layout_and_level_colours_survive_native_size(self):
        # The north/east L is independently recognizable by bright route
        # pixels at the top and right, with the northeast quadrant empty.
        routes = [[(0., 80., 15.5), (0., 0., 15.5), (80., 0., 15.5)],
                  [(40., 20., 30.5), (60., 20., 30.5)]]
        raw = make_assembly_icon(routes)
        validate_assembly_icon(raw, routes=routes)
        image = Image.open(BytesIO(raw)).convert('RGBA')
        normal = image.crop((44, 0, 88, 44))
        bright_lower = {(x, y) for y in range(3, 35) for x in range(3, 41)
                        if (lambda p: p[0] > 180 and p[1] > 160 and p[2] < p[1])(
                            normal.getpixel((x, y)))}
        self.assertTrue(any(y < 6 for _, y in bright_lower))
        self.assertTrue(any(x > 34 for x, _ in bright_lower))
        self.assertFalse(any(x > 20 and y < 16 for x, y in bright_lower))
        self.assertTrue(any(p[1] > p[0] + 60 and p[2] > 120
                            for p in normal.crop((21, 20, 31, 29)).getdata()))
        frames = [image.crop((44 * n, 0, 44 * (n + 1), 44)) for n in range(4)]
        self.assertEqual(len({frame.tobytes() for frame in frames}), 4)
        self.assertTrue(all(p[0] == p[1] == p[2] for p in frames[0].getdata()))
        self.assertEqual(image.size, (176, 44))
        self.assertEqual(image.mode, 'RGBA')

    def test_geometry_change_requires_an_icon_refresh_but_reencoding_is_allowed(self):
        routes = [[(-80., 0., 15.5), (80., 0., 15.5)],
                  [(0., -80., 30.5), (0., 0., 15.5)]]
        raw = make_assembly_icon(routes)
        revised = [routes[0], [(40., -80., 30.5), (0., 0., 15.5)]]
        with self.assertRaisesRegex(ValueError, 'canonical cycle artwork'):
            validate_assembly_icon(raw, routes=revised)
        with Image.open(BytesIO(raw)) as image:
            reencoded = BytesIO()
            image.save(reencoded, format='PNG', compress_level=0)
        validate_assembly_icon(reencoded.getvalue(), routes=routes)
        self.assertNotEqual(raw, reencoded.getvalue())

    def test_invalid_geometry_and_missing_source_routes_fail_explicitly(self):
        for routes in ([], [[(0., 0., 15.5)]], [[(0., 0., 15.5), (float('nan'), 1., 15.5)]],
                       [[(0., 0., 15.5), (0., 0., 30.5)]]):
            with self.subTest(routes=routes), self.assertRaises(ValueError):
                make_assembly_icon(routes)
        with self.assertRaisesRegex(ValueError, 'cardinal'):
            assembly_icon_routes({'placements': [{'piece_id': 'one', 'origin_m': [0, 0],
                                                   'rotation_degrees_ccw': 45}]},
                                 [{'id': 'one', 'recipe': 'example_recipe'}])


if __name__ == '__main__':
    unittest.main()
