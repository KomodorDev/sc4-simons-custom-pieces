"""Interchange geometry and construction invariants use an original donor."""
from __future__ import annotations

from pathlib import Path
import math
import sys
import unittest
from collections import defaultdict
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))
from scp_hsr.interchange_models import build_rules, construction_symbols, EMPTY_STRUCTURAL_PATH
from scp_hsr.rail_geometry import build_geometry, build_tiled_geometry
from scp.models import parse_s3d, validate_s3d
from scp_hsr.test_support import donor, triangles


def vertices(raw):
    return [point for triangle in triangles(raw) for point in triangle]


class InterchangeModelTests(unittest.TestCase):
    def setUp(self):
        self.native = donor()

    def test_per_deck_profiles_match_ground_elevated_and_l4(self):
        for height, profile, expected in ((1., 'ghsr', (-1., 2.)), (15.5, 'hsr', (14., 17.)),
                                           (30.5, 'blend', (29., 32.))):
            deck = {'points': [(0., -8., height), (0., 8., height)], 'width': 15, 'profile': profile}
            raw = build_geometry(self.native, [deck], supports=False)
            points = vertices(raw)
            self.assertAlmostEqual(min(p[1] for p in points), expected[0])
            self.assertAlmostEqual(max(p[1] for p in points), expected[1])

    def test_blended_ramp_hits_both_audited_native_end_profiles(self):
        deck = {'points': [(0., -8., 1.), (0., 0., 15.5), (0., 8., 30.5)],
                'width': 7.5, 'profile': 'blend', 'precise_union': True}
        raw = build_geometry(self.native, [deck], supports=False)
        points = vertices(raw)
        self.assertAlmostEqual(min(p[1] for p in points), -1.)
        self.assertAlmostEqual(max(p[1] for p in points), 32.)
        at_middle = [p[1] for p in points if abs(p[2]) < 1e-5]
        self.assertTrue(any(abs(height - 16.2) < 1e-5 for height in at_middle))

    def test_flyover_supports_move_outside_lower_rail_corridor(self):
        decks = [
            {'points': [(-32., 0., 15.5), (32., 0., 15.5)], 'width': 15, 'profile': 'hsr', 'safe_supports': True},
            {'points': [(0., -32., 30.5), (0., 32., 30.5)], 'width': 7.5, 'profile': 'hsr', 'safe_supports': True},
        ]
        raw = build_geometry(self.native, decks)
        high_posts = [triangle for triangle in triangles(raw)
                      if max(p[1] for p in triangle) > 25 and max(p[1] for p in triangle) - min(p[1] for p in triangle) > 10]
        self.assertTrue(high_posts)
        self.assertTrue(all(abs(p[2]) >= 10.15 - .65 - 1e-5 for triangle in high_posts for p in triangle))
        self.assertTrue(validate_s3d(parse_s3d(raw))['all_vertex_indices_valid'])

    def test_parallel_flyover_uses_portal_posts_outside_lower_line(self):
        decks = [
            {'points': [(0., -32., 15.5), (0., 32., 15.5)], 'width': 15, 'profile': 'hsr', 'safe_supports': True},
            {'points': [(0., -32., 30.5), (0., 32., 30.5)], 'width': 7.5, 'profile': 'hsr', 'safe_supports': True},
        ]
        raw = build_geometry(self.native, decks)
        high_posts = [triangle for triangle in triangles(raw)
                      if max(p[1] for p in triangle) > 25 and max(p[1] for p in triangle) - min(p[1] for p in triangle) > 10]
        self.assertTrue(high_posts)
        self.assertTrue(all(abs(p[0]) >= 10.15 - .65 - 1e-5 for triangle in high_posts for p in triangle))
        # The portal beam is below the upper slab and comfortably above the
        # lower model's17m parapet top and its declared5m clearance margin.
        self.assertTrue(any(abs(p[1] - 28.2) < 1e-5 for p in vertices(raw)))

    def test_axis_port_policy_prevents_dead_track_past_mainline_endpoint(self):
        layout = {
            (0, 0): {'decks': [{'points': [(0., -8., 15.5), (0., 0., 15.5)], 'width': 7.5,
                                'geometry_id': 'stub', 'extend_endpoints': 'ports'}]},
            (1, 0): {'decks': [{'points': [(-8., -6., 15.5), (8., -6., 15.5)], 'width': 7.5,
                                'geometry_id': 'other', 'extend_endpoints': 'ports'}]},
        }
        raw = build_tiled_geometry(self.native, layout, supports=False)[(0, 0)]
        self.assertGreaterEqual(min(p[2] for p in vertices(raw)), -1e-5)

    def test_diagonal_port_policy_covers_offset_cross_section(self):
        tangent = (1 / math.sqrt(2), 1 / math.sqrt(2))
        layout = {(0, 0): {'decks': [{'points': [(-8., 0., 15.5), (0., 8., 15.5)], 'width': 7.5,
                                     'geometry_id': 'diag', 'extend_endpoints': 'ports',
                                     'start_tangent': tangent, 'end_tangent': tangent}]}}
        raw = build_tiled_geometry(self.native, layout, supports=False)[(0, 0)]
        points = vertices(raw)
        self.assertAlmostEqual(min(p[0] for p in points), -8.)
        self.assertAlmostEqual(min(p[2] for p in points), -8.)

    def test_grouped_ascii_cell_symbols_support_large_construction_grids(self):
        cells = [(x, row) for row in range(12) for x in range(28)]
        flags = {cell: 0x02000200 if cell[0] % 2 else 0x00020002 for cell in cells}
        labels, by_flag = construction_symbols(cells, flags)
        self.assertEqual(len(by_flag), 2)
        self.assertEqual(len(set(labels.values())), 2)
        self.assertTrue(all(label.isascii() and label.isalpha() for label in labels.values()))
        info = {'cells': cells, 'footprint': (28, 12), 'construction_flags': flags, 'cost': 1000}
        layout = {cell: {'routes': [], 'decks': []} for cell in cells}
        base = 0x7F550000
        spec = {'recipe': 'interchange_fixture', 'cells': [list(c) for c in cells], 'footprint': [28, 12],
                'tile_ids': [f'{base + x * 0x100 + row * 0x10:08x}' for x, row in cells],
                'puzzle_id': 'f7ff', 'preview_id': '7f551ff5', 'effect_name': 'fixture'}
        with patch('scp_hsr.interchange_models._layout_data', return_value=(info, layout)):
            rules = build_rules(spec)
        self.assertEqual(rules.count('CheckType = '), 2)
        self.assertEqual(rules.count('Rotate = '), 3)
        self.assertNotIn('Transpose', rules)
        self.assertTrue(rules.isascii())

    def test_structural_empty_path_matches_native_zero_route_header(self):
        self.assertEqual(EMPTY_STRUCTURAL_PATH.decode().split(), ['SC4PATHS', '1.2', '0', '0', '0'])

    def test_portal_posts_cannot_use_unreserved_land_inside_bounding_box(self):
        layout = {(0, 0): {'decks': []}, (2, 0): {'decks': []}}
        for row in range(4):
            layout[(1, row)] = {'decks': [
                {'points': [(0., 8., height), (0., -8., height)], 'width': width,
                 'geometry_id': identifier, 'profile': 'hsr', 'safe_supports': True,
                 'extend_endpoints': False}
                for height, width, identifier in ((15.5, 15., 'lower'), (30.5, 7.5, 'upper'))]}
        # The bounding rectangle has room for portals on either side. Only
        # row0 reserves their foundation cells; later rows must not silently
        # put tall columns into unoccupied land inside that rectangle.
        with self.assertRaisesRegex(ValueError, 'No safe support location'):
            build_tiled_geometry(self.native, layout)

    def test_spatial_union_keeps_model_bytes_identical_to_ordered_full_scan(self):
        decks = [
            {'points': [(0., -24., 15.5), (0., 24., 15.5)], 'width': 15., 'profile': 'hsr', 'precise_union': True},
            {'points': [(2., -24., 15.5), (3., -8., 15.5), (8., 0., 15.5), (24., 2., 15.5)],
             'width': 7.5, 'profile': 'hsr', 'precise_union': True},
            {'points': [(128., -24., 1.), (128., 24., 1.)], 'width': 15., 'profile': 'ghsr', 'precise_union': True},
        ]
        indexed = build_geometry(self.native, decks, supports=False)
        with patch('scp_hsr.rail_geometry._index_corridors', side_effect=lambda corridors, enabled: corridors):
            full_scan = build_geometry(self.native, decks, supports=False)
        self.assertEqual(indexed, full_scan)

    def test_native_width_shoulder_stub_does_not_paint_ghost_rails(self):
        decks = [
            {'points': [(2., -8., 15.5), (2., 8., 15.5)], 'width': 7.5, 'profile': 'hsr'},
            {'points': [(0., -8., 15.5), (0., 8., 15.5)], 'width': 15., 'profile': 'hsr',
             'rail_ribbons': False},
        ]
        raw = build_geometry(self.native, decks, supports=False)
        found = []
        for triangle in triangles(raw):
            if not all(abs(vertex[1] - 16.2) < 1e-5 for vertex in triangle):
                continue
            a, b, c = triangle
            denominator = (b[2] - c[2]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[2] - c[2])
            if abs(denominator) < 1e-10:
                continue
            first = ((b[2] - c[2]) * (2 - c[0]) + (c[0] - b[0]) * -c[2]) / denominator
            second = ((c[2] - a[2]) * (2 - c[0]) + (a[0] - c[0]) * -c[2]) / denominator
            third = 1 - first - second
            if min(first, second, third) >= -1e-6:
                found.append(first * a[3] + second * b[3] + third * c[3])
        self.assertTrue(found)
        self.assertTrue(all(abs(value - .5) < 1e-5 for value in found))

    def test_artificial_grid_cut_cannot_leave_a_parapet_in_train_envelope(self):
        from scp_hsr.rail_features import _slice
        from scp_hsr.interchange_verify import _clearance_segments
        controls = [(2., -24.), (2., -8.), (8., 0.), (24., 0.)]
        points = []
        for number in range(65):
            t, u = number / 64, 1 - number / 64
            points.append(tuple(u**3 * controls[0][axis] + 3*u*u*t * controls[1][axis]
                                + 3*u*t*t * controls[2][axis] + t**3 * controls[3][axis]
                                for axis in (0, 1)) + (15.5,))
        layout = {}
        for identifier, route, width in (('main', [(0., -24., 15.5), (0., 8., 15.5)], 15.),
                                          ('branch', points, 7.5)):
            for cell, part in _slice(route).items():
                layout.setdefault(cell, {'decks': []})['decks'].append({
                    'points': part, 'width': width, 'geometry_id': identifier,
                    'profile': 'hsr', 'precise_union': True, 'simplify_collinear': True,
                    'extend_endpoints': 'ports'})
        models = build_tiled_geometry(self.native, layout, supports=False)
        buckets = defaultdict(list)
        for (x, row), raw in models.items():
            for triangle in triangles(raw):
                world = tuple((v[0] + x*16, v[1], v[2] + row*16, *v[3:]) for v in triangle)
                for bx in range(math.floor((min(v[0] for v in world)-1e-4)/4),
                                math.floor((max(v[0] for v in world)+1e-4)/4)+1):
                    for bz in range(math.floor((min(v[2] for v in world)-1e-4)/4),
                                    math.floor((max(v[2] for v in world)+1e-4)/4)+1):
                        buckets[bx, bz].append(world)
        checked = _clearance_segments([(0, 0, points)], buckets)
        self.assertEqual(checked, len(points) - 1)

    def test_collinear_grade_keeps_ground_to_elevated_calibration_break(self):
        from scp_hsr.rail_features import _slice
        points = [(0., -120. + 128. * number / 16, 1. + 29.5 * number / 16) for number in range(17)]
        layout = {cell: {'decks': [{'points': part, 'width': 7.5, 'geometry_id': 'ramp',
                                    'profile': 'blend', 'simplify_collinear': True,
                                    'extend_endpoints': 'ports'}]}
                  for cell, part in _slice(points).items()}
        models = build_tiled_geometry(self.native, layout, supports=False)
        crossing_z = 120. - 128. * 14.5 / 29.5
        self.assertTrue(any(abs(vertex[1] - 16.2) < 1e-5 and abs(vertex[2] + cell[1] * 16 - crossing_z) < 1e-4
                            for cell, raw in models.items() for vertex in vertices(raw)))

    def test_port_trim_preserves_remote_curve_returning_across_endpoint_plane(self):
        from scp_hsr.rail_features import _slice
        points = [(-8., 0., 15.5), (24., 0., 15.5), (24., 24., 15.5), (-24., 24., 15.5)]
        layout = {cell: {'decks': [{'points': part, 'width': 7.5, 'geometry_id': 'returning',
                                    'profile': 'hsr', 'simplify_collinear': True,
                                    'extend_endpoints': 'ports'}]}
                  for cell, part in _slice(points).items()}
        models = build_tiled_geometry(self.native, layout, supports=False)
        self.assertTrue(any(vertex[0] + cell[0] * 16 < -16
                            and vertex[2] + cell[1] * 16 < -20
                            for cell, raw in models.items() for vertex in vertices(raw)))

    def test_graded_merge_opens_raised_parapet_through_train_headroom(self):
        from scp_hsr.interchange_verify import _clearance_segments
        ramp = [(3., -8., 15.4), (3., 8., 15.48)]
        decks = [{'points': [(0., -8., 15.5), (0., 8., 15.5)], 'width': 7.5,
                  'profile': 'hsr', 'precise_union': True},
                 {'points': ramp, 'width': 7.5, 'profile': 'hsr', 'precise_union': True}]
        raw = build_geometry(self.native, decks, supports=False)
        buckets = defaultdict(list)
        for triangle in triangles(raw):
            for x in range(math.floor((min(v[0] for v in triangle)-1e-4)/4),
                           math.floor((max(v[0] for v in triangle)+1e-4)/4)+1):
                for z in range(math.floor((min(v[2] for v in triangle)-1e-4)/4),
                               math.floor((max(v[2] for v in triangle)+1e-4)/4)+1):
                    buckets[x, z].append(triangle)
        self.assertEqual(_clearance_segments([(0, 0, ramp)], buckets), 1)

    def test_returning_segment_cannot_put_its_parapet_across_same_route(self):
        from scp_hsr.interchange_verify import _clearance_segments
        points = [(0., -24., 15.5), (0., 24., 15.5), (5., 24., 15.5), (5., -24., 15.5)]
        raw = build_geometry(self.native, [{'points': points, 'width': 7.5,
                                           'profile': 'hsr', 'precise_union': True}], supports=False)
        buckets = defaultdict(list)
        for triangle in triangles(raw):
            for x in range(math.floor((min(v[0] for v in triangle)-1e-4)/4),
                           math.floor((max(v[0] for v in triangle)+1e-4)/4)+1):
                for z in range(math.floor((min(v[2] for v in triangle)-1e-4)/4),
                               math.floor((max(v[2] for v in triangle)+1e-4)/4)+1):
                    buckets[x, z].append(triangle)
        self.assertEqual(_clearance_segments([(0, 0, points)], buckets), 3)


if __name__ == '__main__':
    unittest.main()
