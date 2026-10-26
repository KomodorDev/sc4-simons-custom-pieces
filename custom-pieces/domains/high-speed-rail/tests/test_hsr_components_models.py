"""Small physical regressions for taper masks and unchanged native sweeps."""
from copy import deepcopy
import json
from unittest.mock import patch
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))
from scp_hsr.hsr_components import _sweep_component_profile
from scp_hsr.hsr_mesh import _compile_models, _sweep_native_profile
from scp_hsr.hsr_components_layout import component_layout
from scp_hsr.hsr_components_verify import _section_intervals
from scp_hsr.test_support import donor, triangles


class ComponentModelRegressionTests(unittest.TestCase):
    def test_optional_sweep_hook_preserves_original_default_encoded_models(self):
        layout = component_layout('hsr_component_upper_paired_straight')
        config = {'support_centers': [(0., 0.)]}
        original = _compile_models(donor(), deepcopy(layout), config)
        explicit = _compile_models(donor(), deepcopy(layout), config,
                                   sweep_function=_sweep_native_profile)
        self.assertEqual(original, explicit)

    def test_explicit_surface_context_preserves_boundary_ownership_and_emits_only_selected_cells(self):
        # This two-tile slab extends beyond the selected first tile. Keeping
        # the complete boundary mask assigns those faces to the second tile
        # rather than attaching them as overhangs to the selected first tile.
        deck = {'points': [(0., -8., 30.5), (0., 24., 30.5)],
                'width': 15., 'profile': 'hsr', 'geometry_id': 'straight',
                'start_tangent': (0., 1.), 'end_tangent': (0., 1.),
                'precise_union': True, 'extend_endpoints': False}
        full_layout = {(0, 0): {'routes': [], 'decks': [deck]},
                       (0, -1): {'routes': [], 'decks': []}}
        full = _compile_models(donor(), full_layout, {'support_centers': []})
        from scp_hsr.rail_geometry import _global_decks
        selected = _compile_models(donor(), {(0, 0): {'routes': [], 'decks': []}},
            {'support_centers': [], 'surface_decks': _global_decks(full_layout),
             'surface_partition_cells': [[0, 0], [0, -1]]})
        self.assertEqual(set(selected), {(0, 0)})
        self.assertEqual(selected[0, 0], full[0, 0])

    def test_surface_cache_keys_include_native_bytes_every_deck_setting_and_sweep(self):
        from scp_hsr.hsr_mesh import _cached_surface_triangles
        _cached_surface_triangles.cache_clear()
        self.addCleanup(_cached_surface_triangles.cache_clear)
        first = donor()
        second = first.replace(b'original fixture', b'changedx fixture')
        self.assertNotEqual(first, second)
        surfaces = ([((0., 1., 0., 0., 0.), (1., 1., 0., 0., 0.),
                      (0., 1., 1., 0., 0.))], [])
        sweep_a, sweep_b = lambda *args: None, lambda *args: None
        one = json.dumps([{'setting': 1}], sort_keys=True)
        two = json.dumps([{'setting': 2}], sort_keys=True)
        with patch('scp_hsr.hsr_mesh._surface_triangles', return_value=surfaces) as compiler:
            expected = _cached_surface_triangles(first, one, sweep_a)
            self.assertEqual(_cached_surface_triangles(first, one, sweep_a), expected)
            self.assertEqual(compiler.call_count, 1)
            _cached_surface_triangles(second, one, sweep_a)
            _cached_surface_triangles(second, two, sweep_a)
            _cached_surface_triangles(second, two, sweep_b)
            self.assertEqual(compiler.call_count, 4)
            self.assertEqual(_cached_surface_triangles.cache_info().maxsize, 2)
            self.assertEqual(_cached_surface_triangles.cache_info().currsize, 2)
            # The first context was evicted by the bounded two-entry cache.
            _cached_surface_triangles(first, one, sweep_a)
            self.assertEqual(compiler.call_count, 5)

    def test_surface_cache_returns_immutable_copies_of_compiler_faces(self):
        from scp_hsr.hsr_mesh import _cached_surface_triangles, _sweep_native_profile
        _cached_surface_triangles.cache_clear()
        self.addCleanup(_cached_surface_triangles.cache_clear)
        face = [[0., 1., 0., 0., 0.], [1., 1., 0., 0., 0.], [0., 1., 1., 0., 0.]]
        with patch('scp_hsr.hsr_mesh._surface_triangles', return_value=([face], [face])):
            floors, undersides = _cached_surface_triangles(donor(), '[]', _sweep_native_profile)
            face[0][0] = 99.
            self.assertEqual(floors[0][0][0], 0.)
            self.assertEqual(undersides[0][0][0], 0.)
            with self.assertRaises(TypeError):
                floors[0][0][0] = 99.

    def test_widened_native_pair_collar_also_opens_the_widened_inside_walls(self):
        # The two widened single sheets overlap into a native-width pair.
        # Keeping the old narrow clearance mask leaves a 0.2 m unwanted lip
        # at the inside of each outer parapet. This fixture isolates that bug
        # without loading NAM or compiling the whole 128 m adapter.
        decks = []
        for x in (-2., 2.):
            decks.append({'points': [(x, -8., 30.5), (x, 8., 30.5)],
                'width': 8., 'profile': 'hsr', 'geometry_id': str(x),
                'start_tangent': (0., 1.), 'end_tangent': (0., 1.),
                'precise_union': True, 'extend_endpoints': False,
                'clearance_half_width': 2.6, 'taper_extra_half_width': 1.5,
                'taper_start_distance': 16., 'taper_end_distance': 32.})
        raw = _compile_models(donor(), {(0, 0): {'routes': [], 'decks': decks}},
                              {'support_centers': []},
                              sweep_function=_sweep_component_profile)[0, 0]
        actual = triangles(raw)
        for z in (-7.5, 0., 7.5):
            caps = _section_intervals(actual, z, 32.)
            self.assertEqual(len(caps), 2)
            for measured, expected in zip(caps, [(-7.5, -6.), (6., 7.5)]):
                for value, wanted in zip(measured, expected):
                    self.assertAlmostEqual(value, wanted, places=4)
            floor = _section_intervals(actual, z, 31.2, floor=True)
            self.assertEqual(len(floor), 1)
            self.assertAlmostEqual(floor[0][0], -7.5, places=4)
            self.assertAlmostEqual(floor[0][1], 7.5, places=4)


if __name__ == '__main__':
    unittest.main()
