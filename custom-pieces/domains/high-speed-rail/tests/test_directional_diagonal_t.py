"""Diagonal native ports, direct smooth routes and immutable compiler inputs."""
from __future__ import annotations

from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))

from scp_hsr.directional_diagonal_t import (
    INFO, RECIPE, PORTS, LANE_OFFSET, directional_routes, directional_layout,
    build_models, build_rules, _cached_models, _physical_centers, _distance,
    _compile_models, _flat_union, _floor_bucket_keys,
)
from scp_hsr.directional_t_verify import measure_route_quality, _TURN_LIMITS
from scp_hsr.directional_t import (_compile_models as _shared_compile_models,
                               _flat_union as _shared_flat_union, _plan_area)
from scp_hsr.rail_feature_verify import _weights
from scp_hsr.test_support import donor


class DiagonalDirectionalTTests(unittest.TestCase):
    def test_external_ports_are_exact_native_asymmetric_coordinates(self):
        ports = {'N': {'in': (173.1, 8., 15.5), 'out': (178.9, 8., 15.5)},
                 'S': {'in': (-8., -178.9, 15.5), 'out': (-8., -173.2, 15.5)},
                 'E': {'in': (184., -189.1, 15.5), 'out': (184., -194.9, 15.5)}}
        self.assertEqual(PORTS, ports)
        self.assertAlmostEqual(LANE_OFFSET, 2.9/math.sqrt(2.))
        vectors = {'N': (-1., -1.), 'S': (1., 1.), 'E': (-1., 1.)}
        routes = directional_routes()
        self.assertEqual(set(routes), {'S>N', 'N>S', 'N>E', 'E>N', 'S>E', 'E>S'})
        for movement, points in routes.items():
            source, target = movement.split('>')
            self.assertEqual(points[0], ports[source]['in'])
            self.assertEqual(points[-1], ports[target]['out'])
            self.assertEqual({point[2] for point in points}, {15.5})
            for a, b, expected in ((points[0], points[1], vectors[source]),
                                   (points[-2], points[-1], tuple(-v for v in vectors[target]))):
                self.assertAlmostEqual(math.dist(a, b), 4.)
                vector = (b[0]-a[0], b[1]-a[1])
                self.assertAlmostEqual(vector[0]/vector[1], expected[0]/expected[1])
                self.assertGreater(sum(u*v for u, v in zip(vector, expected)), 0.)

    def test_direct_turns_retain_strict_quality_limits_and_no_large_heading_kinks(self):
        for movement, points in directional_routes().items():
            report = measure_route_quality(points, _TURN_LIMITS)
            if movement in ('S>N', 'N>S'):
                self.assertLess(report['length_ratio'], 1.00001)
                self.assertLess(report['total_turn_degrees'], 1.)
            else:
                self.assertLess(report['length_ratio'], 1.25)
                self.assertGreater(report['minimum_sampled_radius_m'], 62.)
                self.assertLess(abs(report['total_turn_degrees']-90.), 1.)
            self.assertLess(report['maximum_raw_encoded_turn_degrees'], .7)
            self.assertLess(report['maximum_endpoint_curvature_per_m'], .0005)

    def test_all_three_physical_arms_are_diagonal_and_native_phase_aligned(self):
        centers = _physical_centers()
        self.assertEqual(set(centers), {'main', 'north_curve', 'south_curve'})
        self.assertEqual(centers['main'][0], (-8., -176., 15.5))
        self.assertEqual(centers['main'][-1], (176., 8., 15.5))
        self.assertEqual(centers['north_curve'][0], (176., 8., 15.5))
        self.assertEqual(centers['south_curve'][0], (-8., -176., 15.5))
        self.assertEqual(centers['north_curve'][-1], (184., -192., 15.5))
        self.assertEqual(centers['south_curve'][-1], (184., -192., 15.5))
        for points in centers.values():
            for a, b in (points[:2], points[-2:]):
                self.assertAlmostEqual(abs(b[0]-a[0]), abs(b[1]-a[1]))
        self.assertEqual((-176.-(-8.)) % 16., 8.)
        self.assertEqual((184.-192.) % 16., 8.)

    def test_sparse_footprint_has_no_native_continuation_cell_and_fresh_mutable_data(self):
        layout = directional_layout()
        info = INFO[RECIPE]
        self.assertEqual(info['footprint'], (13, 14))
        self.assertEqual(len(layout), 42)
        self.assertEqual(list(layout), info['cells'])
        self.assertNotIn((12, 0), layout)
        self.assertTrue(all(data['routes'] for data in layout.values()))
        decks = [deck for data in layout.values() for deck in data['decks']]
        self.assertEqual(len(decks), 3)
        self.assertEqual({deck['width'] for deck in decks}, {15.})
        self.assertTrue(all(deck['precise_union'] and not deck['support'] for deck in decks))
        before = deepcopy(directional_layout())
        decks[0]['points'][0] = (123., 456., 789.)
        layout[next(iter(layout))]['routes'][0]['points'][0] = (123., 456., 789.)
        self.assertEqual(directional_layout(), before)

    def test_global_support_plan_is_reserved_with_full_top_contact_and_spacing(self):
        info = INFO[RECIPE]
        centers = info['support_centers']
        self.assertEqual(len(centers), 37)
        self.assertGreaterEqual(min(math.dist(a, b) for n, a in enumerate(centers)
                                    for b in centers[n+1:]), 16.)
        segments = [(a, b) for points in _physical_centers().values()
                    for a, b in zip(points, points[1:])]
        for x, north in centers:
            self.assertIn((round(x/16.), round(-north/16.)), info['cells'])
            for dx in (-.65, 0., .65):
                for dy in (-.65, 0., .65):
                    self.assertLess(min(_distance((x+dx, north+dy), a, b) for a, b in segments), 7.49)

    def test_new_construction_grid_uses_only_new_allocation_and_proper_rotations(self):
        info = INFO[RECIPE]
        spec = {'recipe': RECIPE, 'cells': info['cells'], 'footprint': info['footprint'],
                'tile_ids': [0x7F5FF000+0x100*x+0x10*row for x, row in info['cells']],
                'puzzle_id': 'f8ff', 'preview_id': '7f5ffff5', 'effect_name': 'fixture'}
        rules = build_rules(spec)
        self.assertIn('AutoTileBase = 0x7F5FF000', rules)
        self.assertIn('Costs = 4200', rules)
        self.assertEqual(rules.count('Rotate = '), 3)
        self.assertNotIn('Transpose', rules)
        broken = deepcopy(spec)
        broken['cells'].pop()
        with self.assertRaisesRegex(ValueError, 'cells/footprint'):
            build_rules(broken)


class DiagonalDirectionalCacheTests(unittest.TestCase):
    def test_cache_keys_native_bytes_full_layout_and_supports_and_returns_fresh_dicts(self):
        _cached_models.cache_clear()
        native = donor()
        try:
            with patch('scp_hsr.directional_diagonal_t._compile_models', return_value={(0, 0): b'original'}) as compile:
                first = build_models(native)
                first[0, 0] = b'caller modification'
                self.assertEqual(build_models(native), {(0, 0): b'original'})
                self.assertEqual(compile.call_count, 1)
                layout = deepcopy(directional_layout())
                data = next(data for data in layout.values() if data['decks'])
                data['decks'][0]['points'][0] = (123., 456., 15.5)
                with patch('scp_hsr.directional_diagonal_t.directional_layout', return_value=layout):
                    build_models(native)
                self.assertEqual(compile.call_count, 2)
                build_models(native+b'other donor bytes')
                self.assertEqual(compile.call_count, 3)
                with patch.dict(INFO[RECIPE], support_centers=[(0., 0.)]):
                    build_models(native)
                self.assertEqual(compile.call_count, 4)
                self.assertEqual(_cached_models.cache_info().maxsize, 2)
                self.assertLessEqual(_cached_models.cache_info().currsize, 2)
        finally:
            _cached_models.cache_clear()


class DiagonalFloorCompilationTests(unittest.TestCase):
    def test_wall_only_compiler_is_byte_identical_with_shared_floor_union(self):
        # Three intersecting diagonal decks exercise both other-deck wall
        # openings and each deck's own five-metre train clearance cuts.
        paths = [[(-4., -4., 15.5), (4., 4., 15.5)],
                 [(4., 4., 15.5), (2., 1., 15.5), (4., -4., 15.5)],
                 [(-4., -4., 15.5), (0., -2., 15.5), (4., -4., 15.5)]]
        layout = {(0, 0): {'routes': [], 'decks': [
            {'points': points, 'width': 15., 'geometry_id': str(index),
             'profile': 'hsr', 'precise_union': True, 'clearance_half_width': 2.6,
             'support': False, 'extend_endpoints': False}
            for index, points in enumerate(paths)]}}
        config = {'support_foundation_width': 1.3, 'support_centers': []}
        expected = _shared_compile_models(donor(), layout, config)
        with patch('scp_hsr.directional_diagonal_t._flat_union', _shared_flat_union):
            self.assertEqual(_compile_models(donor(), layout, config), expected)

    def test_diagonal_bucket_strip_is_conservative_and_avoids_square_bbox(self):
        triangle = [(0., 16.2, 0., 0., 0.), (160., 16.2, 160., 160., 160.),
                    (160., 16.2, 160.25, 160., 160.25)]
        keys = set(_floor_bucket_keys(triangle))
        self.assertLess(len(keys), 150)
        self.assertGreater(len(keys), 40)
        # Dense barycentric samples independently require every occupied
        # cell, including points precisely on strip and column boundaries.
        for i in range(81):
            for j in range(81-i):
                u, v = i/80., j/80.
                x = sum(weight*p[0] for weight, p in zip((1.-u-v, u, v), triangle))
                z = sum(weight*p[2] for weight, p in zip((1.-u-v, u, v), triangle))
                self.assertIn((math.floor(x/4.), math.floor(z/4.)), keys)

    def test_tight_union_preserves_full_slanted_coverage_priority_and_uvs(self):
        # Overlap, reversed winding, a long thin diagonal, and a small
        # crossing near its far end exercise exact clipping rather than
        # sampled cell occupancy. UVs encode their original world axes.
        def point(x, z, priority):
            return (x, 16.2, z, x/16.+priority, z/16.)
        first = (point(0., 0., 0.), point(160., 160., 0.), point(160., 160.5, 0.))
        crossing = (point(150., 149., 10.), point(152., 153., 10.), point(148., 153., 10.))
        source = [first, tuple(reversed(first)), crossing]
        output = _flat_union(source)
        baseline = _shared_flat_union(source)
        self.assertAlmostEqual(sum(_plan_area(list(face)) for face in output),
                               sum(_plan_area(list(face)) for face in baseline), places=7)
        for triangle in (first, crossing):
            for i in range(1, 20):
                for j in range(1, 20-i):
                    weights = (1.-i/20.-j/20., i/20., j/20.)
                    x = sum(w*p[0] for w, p in zip(weights, triangle))
                    z = sum(w*p[2] for w, p in zip(weights, triangle))
                    candidates = [(face, _weights(x, z, face)) for face in output]
                    candidates = [(face, weights) for face, weights in candidates if weights is not None]
                    self.assertTrue(candidates, (x, z))
                    for face, weights in candidates:
                        if min(weights) < 1e-7:
                            continue  # Adjacent UV patches may share their exact edge.
                        uv = tuple(sum(w*p[axis] for w, p in zip(weights, face)) for axis in (3, 4))
                        native_weights = _weights(x, z, first)
                        if native_weights is not None and min(native_weights) < 1e-7:
                            continue
                        priority = 0. if native_weights is not None else 10.
                        self.assertAlmostEqual(uv[0], x/16.+priority, places=6)
                        self.assertAlmostEqual(uv[1], z/16., places=6)

    def test_long_diagonal_with_many_overlaps_stays_in_exact_bounded_patches(self):
        def point(x, z, priority=0.):
            return (x, 16.2, z, x/16.+priority, z/16.)
        first = (point(0., 0.), point(160., 160.), point(160., 160.5))
        source = [first]
        for number in range(100):
            x = 1.+157.*number/99.
            source.append((point(x, x+.1*x/160., 10.),
                           point(x+.5, x+.5+.1*(x+.5)/160., 10.),
                           point(x+.5, x+.5+.4*(x+.5)/160., 10.)))
        result = _flat_union(source)
        self.assertAlmostEqual(sum(_plan_area(list(face)) for face in result), 40., places=7)
        for triangle in result:
            # Each exact patch spans no more than four metres, even though
            # its original parent mainline triangle is160m long.
            self.assertLessEqual(max(p[0] for p in triangle)-min(p[0] for p in triangle), 4.+1e-9)
            self.assertLessEqual(max(p[2] for p in triangle)-min(p[2] for p in triangle), 4.+1e-9)
            a, b, c = triangle
            self.assertGreater((b[0]-a[0])*(c[2]-a[2])-(b[2]-a[2])*(c[0]-a[0]), 0.)
            for p in triangle:
                self.assertAlmostEqual(p[3], p[0]/16., places=7)
                self.assertAlmostEqual(p[4], p[2]/16., places=7)
        for number in range(1, 160):
            x = float(number)
            z = x+.25*x/160.
            self.assertTrue(any(_weights(x, z, face) is not None for face in result))


if __name__ == '__main__':
    unittest.main()
