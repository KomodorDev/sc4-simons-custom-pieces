"""Assembly artwork shows actual placed routes while retaining native states."""
from io import BytesIO
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

from PIL import Image

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.menu_experiment import _assembly_icon_network
from scp.menu_experiment_resources import make_assembly_icon, validate_assembly_icon
from scp_hsr.icons import assembly_icon_network, assembly_icon_routes


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
        raw = make_assembly_icon(routes, network_label='HSR')
        validate_assembly_icon(raw, routes=routes, network_label='HSR')
        image = Image.open(BytesIO(raw)).convert('RGBA')
        normal = image.crop((44, 0, 88, 44))
        bright_lower = {(x, y) for y in range(3, 41) for x in range(3, 41)
                        if (lambda p: p[0] > 180 and p[1] > 160 and p[2] < p[1])(
                            normal.getpixel((x, y)))}
        # This fixture's upper-left route shares the five-row brand area.
        self.assertTrue(any(y < 11 for _, y in bright_lower))
        self.assertTrue(any(x > 34 for x, _ in bright_lower))
        self.assertFalse(any(x > 20 and y < 16 for x, y in bright_lower))
        self.assertTrue(any(p[1] > p[0] + 60 and p[2] > 120
                            for p in normal.crop((21, 28, 33, 34)).getdata()))
        frames = [image.crop((44 * n, 0, 44 * (n + 1), 44)) for n in range(4)]
        self.assertEqual(len({frame.tobytes() for frame in frames}), 4)
        self.assertTrue(all(p[0] == p[1] == p[2] for p in frames[0].getdata()))
        self.assertEqual(image.size, (176, 44))
        self.assertEqual(image.mode, 'RGBA')

    def test_small_labels_remain_visible_with_padding_and_full_route_extent_in_every_state(self):
        routes = [[(-80., 0., 15.5), (80., 0., 15.5)],
                  [(0., -80., 30.5), (0., 80., 30.5)]]
        image = Image.open(BytesIO(make_assembly_icon(routes, network_label='HSR'))).convert('RGBA')
        for number in range(4):
            with self.subTest(state=number):
                frame = image.crop((44 * number, 0, 44 * (number + 1), 44))
                # Recognizable three-by-five letters must remain visible at
                # native size, including the locked state.
                for top, positions in ((5, (5, 9, 13)),
                                       (33, (9, 13, 17, 24, 28, 32))):
                    for left in positions:
                        self.assertTrue(all(any(min(frame.getpixel((x, y))[:3]) > 170
                                                for x in range(left, left + 3))
                                            for y in range(top, top + 5)))
                ink_colour = frame.getpixel((10, 33))
                self.assertFalse(any(frame.getpixel((x, y)) == ink_colour
                                     for y in (38, 39, 40) for x in range(9, 35)))
                # No reserved label band reduces the original 34-pixel route
                # area. Endpoint antialiasing may occupy the inward pixel.
                for x, y in ((5, 22), (39, 22), (22, 5), (22, 39)):
                    self.assertGreater(max(max(frame.getpixel((x + dx, y + dy))[:3])
                                           for dx in (-1, 0, 1) for dy in (-1, 0, 1)), 110)

    def test_network_identity_is_explicit_and_changes_only_the_small_footer(self):
        self.assertEqual(assembly_icon_network('straight-stem-trumpet'), 'HSR')
        with self.assertRaises(ValueError):
            assembly_icon_network('unknown-assembly')
        routes = [[(-80., 0., 15.5), (80., 0., 15.5)]]
        hsr = make_assembly_icon(routes, network_label='HSR')
        ghsr = make_assembly_icon(routes, network_label='GHSR')
        self.assertNotEqual(hsr, ghsr)
        with Image.open(BytesIO(hsr)) as first, Image.open(BytesIO(ghsr)) as second:
            for number in range(4):
                for box in ((44 * number, 0, 44 * (number + 1), 33),
                            (44 * number, 38, 44 * (number + 1), 44)):
                    self.assertEqual(first.crop(box).tobytes(), second.crop(box).tobytes())
        with self.assertRaisesRegex(ValueError, 'canonical cycle artwork'):
            validate_assembly_icon(hsr, routes=routes, network_label='GHSR')

    def test_shared_generator_uses_the_owning_domain_network_without_an_hsr_fallback(self):
        assembly = {'id': 'example-junction', 'domain': 'example-network'}
        adapter = Mock()
        adapter.assembly_icon_network.return_value = 'MIX'
        with patch('scp.providers.domain_module', return_value=adapter) as provider:
            self.assertEqual(_assembly_icon_network(assembly), 'MIX')
        provider.assert_called_once_with({'domain': 'example-network'}, 'icons')
        adapter.assembly_icon_network.assert_called_once_with('example-junction')
        with patch('scp.providers.domain_module', return_value=object()):
            with self.assertRaisesRegex(ValueError, 'declared assembly icon network adapter'):
                _assembly_icon_network(assembly)

    def test_actual_routes_require_a_short_renderable_uppercase_network_label(self):
        routes = [[(0., 0., 15.5), (80., 0., 15.5)]]
        for label in (None, '', 'hsr', 'HSR5', 'ABCDE', 'HS R', 'HSR\n', '?', 123, True):
            with self.subTest(label=label), self.assertRaises(ValueError):
                make_assembly_icon(routes, network_label=label)
        for label in ('H', 'HSR', 'GHSR', 'MIX'):
            with self.subTest(label=label):
                validate_assembly_icon(make_assembly_icon(routes, network_label=label),
                                       routes=routes, network_label=label)

    def test_geometry_change_requires_an_icon_refresh_but_reencoding_is_allowed(self):
        routes = [[(-80., 0., 15.5), (80., 0., 15.5)],
                  [(0., -80., 30.5), (0., 0., 15.5)]]
        raw = make_assembly_icon(routes, network_label='HSR')
        revised = [routes[0], [(40., -80., 30.5), (0., 0., 15.5)]]
        with self.assertRaisesRegex(ValueError, 'canonical cycle artwork'):
            validate_assembly_icon(raw, routes=revised, network_label='HSR')
        with Image.open(BytesIO(raw)) as image:
            reencoded = BytesIO()
            image.save(reencoded, format='PNG', compress_level=0)
        validate_assembly_icon(reencoded.getvalue(), routes=routes, network_label='HSR')
        self.assertNotEqual(raw, reencoded.getvalue())

    def test_invalid_geometry_and_missing_source_routes_fail_explicitly(self):
        for routes in ([], [[(0., 0., 15.5)]], [[(0., 0., 15.5), (float('nan'), 1., 15.5)]],
                       [[(0., 0., 15.5), (0., 0., 30.5)]]):
            with self.subTest(routes=routes), self.assertRaises(ValueError):
                make_assembly_icon(routes, network_label='HSR')
        with self.assertRaisesRegex(ValueError, 'cardinal'):
            assembly_icon_routes({'placements': [{'piece_id': 'one', 'origin_m': [0, 0],
                                                   'rotation_degrees_ccw': 45}]},
                                 [{'id': 'one', 'recipe': 'example_recipe'}])


if __name__ == '__main__':
    unittest.main()
