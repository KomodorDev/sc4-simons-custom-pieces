"""Check separate ramp ownership, retained joins, and encoded R40 geometry."""
from collections import Counter, defaultdict
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp_highway import modular_ramps as modular
from scp_highway import ramp_geometry as geometry
from scp_highway import ramp_paths as paths
from scp_highway.native import parse_paths


def _world(cell, point):
    return point[0] + 16 * cell[0], point[1] - 16 * cell[1], point[2]


def _minimum_radius(points):
    values = []
    for a, b, c in zip(points, points[1:], points[2:]):
        cross = abs((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]))
        if cross > 1e-10:
            values.append(math.dist(a[:2], b[:2]) * math.dist(b[:2], c[:2])
                          * math.dist(a[:2], c[:2]) / (2.0 * cross))
    return min(values) if values else math.inf


class ModularRampGeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = modular.module_catalog()
        cls.ramps = {row['id']: row for row in modular.variant_ramps()}
        cls.procedural = modular.procedural_geometry()

    def test_literal_default_and_compact_ownership_exclude_the_straight_highway_stamp(self):
        self.assertEqual([(row['key'], len(row['cells'])) for row in self.catalog['types']], [
            ('lower-exit-r40', 4), ('lower-entry-r40', 4),
            ('upper-exit-r40', 6), ('upper-entry-r40', 6),
            ('northwest-terminal-r40', 9), ('southeast-terminal-r40', 12),
            ('lower-exit-compact', 3), ('lower-entry-compact', 3),
            ('upper-exit-compact', 6), ('upper-entry-compact', 6)])
        owned = [tuple(cell) for row in self.catalog['types'] if not row['key'].endswith('-compact')
                 for cell in row['world_cells']]
        self.assertEqual(len(owned), 41)
        self.assertEqual(len(set(owned)), 41)
        self.assertEqual(len(modular.stamp_cells()), 21)
        self.assertFalse(set(owned) & modular.stamp_cells())
        self.assertEqual(len(set(owned) | modular.stamp_cells()), 62)
        compact = [tuple(cell) for row in self.catalog['types'] if row['key'].endswith('-compact')
                   for cell in row['world_cells']]
        junctions = {cell for key in ('northwest-junction', 'southeast-junction') for cell in paths.MODULES[key][1]}
        self.assertEqual(len(compact), 18)
        self.assertEqual(len(set(compact)), 18)
        self.assertFalse(set(compact) & (modular.stamp_cells() | junctions))
        self.assertEqual(len(set(compact) | modular.stamp_cells() | junctions), 53)
        for row in self.catalog['types']:
            origin = row['world_origin_cell']
            reconstructed = {(c[0] + origin[0], c[1] + origin[1]) for c in row['cells']}
            self.assertEqual(reconstructed, set(map(tuple, row['world_cells'])))

    def test_actual_full_width_pavement_barriers_and_piers_have_declared_owners(self):
        _ramps, tiles, _routes = self.procedural
        owned = set(map(tuple, self.catalog['occupied_cells'])) | modular.stamp_cells()
        self.assertLessEqual(set(tiles), owned)
        for cell, faces in tiles.items():
            for face in faces:
                for east, height, south, *_uv in face:
                    self.assertLessEqual(abs(east), 8.000001, cell)
                    self.assertLessEqual(abs(south), 8.000001, cell)
                    self.assertGreaterEqual(height, -1e-8, cell)

    def test_all_retained_branch_triangles_remain_exact_source_values(self):
        old = paths._procedural_geometry()[1]
        new = self.procedural[1]
        branches = {cell for key, (_name, cells) in paths.MODULES.items()
                    if key.endswith('-branch') for cell in cells}
        self.assertEqual(len(branches), 18)
        for cell in branches:
            self.assertEqual(Counter(new.get(cell, ())), Counter(old.get(cell, ())), cell)

    def test_original_high_endpoint_path_and_mesh_samples_are_retained(self):
        old = {row['id']: row for row in geometry.compact_ramps()}
        for name, current in self.ramps.items():
            source = old[name]
            boundary = current['modular_profile']['retained_boundary_m']
            for key in ('points', 'mesh_points'):
                high = current[key] if current['direction'] == 'off' else list(reversed(current[key]))
                previous = source[key] if source['direction'] == 'off' else list(reversed(source[key]))
                boundary_axis = 0 if current['direction'] == 'off' else 1
                axis_value = boundary[boundary_axis]
                crossing = next(index for index, (a, b) in enumerate(zip(previous, previous[1:]))
                                if min(a[boundary_axis], b[boundary_axis]) <= axis_value
                                <= max(a[boundary_axis], b[boundary_axis]))
                self.assertEqual(high[:crossing + 2], previous[:crossing + 2], (name, key))
            self.assertGreaterEqual(current['modular_profile']['retained_high_collar_m'], 2.0)

    def test_literal_flat_ground_ports_and_exact_cardinal_joining_chords(self):
        expected = {
            'lower-off': ((-8.0, 35.76854249492381, 0.0), (-1.0, 0.0)),
            'lower-on': ((-35.76854249492381, 8.0, 0.0), (0.0, 1.0)),
            'upper-off': ((24.0, -51.76854249492381, 0.0), (1.0, 0.0)),
            'upper-on': ((51.76854249492381, -24.0, 0.0), (0.0, -1.0)),
        }
        for name, (port, outward) in expected.items():
            ramp = self.ramps[name]
            self.assertEqual(ramp['standard_ground_port'], port)
            points = ramp['points'] if ramp['direction'] == 'off' else list(reversed(ramp['points']))
            index = next(index for index, point in enumerate(points) if point == port)
            a, b = points[index - 1:index + 1]
            length = math.dist(a[:2], b[:2])
            self.assertEqual(a[2], 0.0)
            self.assertEqual(b[2], 0.0)
            for axis in range(2):
                self.assertAlmostEqual((b[axis] - a[axis]) / length, outward[axis], places=10)

    def test_encoded_custom_routes_keep_exact_tile_seams_and_actual_car_transport(self):
        selected = set(map(tuple, self.catalog['occupied_cells']))
        starts, ends = defaultdict(int), defaultdict(int)
        for cell, routes in self.procedural[2].items():
            if cell not in selected:
                continue
            for route in parse_paths(paths.encode_paths(routes)):
                self.assertEqual(route['transport'], 1)
                self.assertIn(route['entry'], range(4))
                self.assertIn(route['exit'], range(4))
                start = tuple(round(value, 8) for value in _world(cell, route['points'][0]))
                end = tuple(round(value, 8) for value in _world(cell, route['points'][-1]))
                starts[start] += 1
                ends[end] += 1
        # Eight stamp intersections and four native Avenue intersections.
        # A lower ramp's two owned PATH fragments use a stamp-owned middle
        # tile; its continuous physical model overhangs that highway tile.
        external = {point for point in starts.keys() | ends.keys() if starts[point] != ends[point]}
        self.assertEqual(len(external), 12)
        self.assertEqual(sum(starts[point] - ends[point] for point in external), 0)

    def test_encoded_grade_chords_stay_below_30_percent_and_match_retained_bounds(self):
        from scp_highway.straight_stamp_geometry import WING_CELLS
        for name, ramp in self.ramps.items():
            key = ramp['deck'] + ('-exit-r40' if ramp['direction'] == 'off' else '-entry-r40')
            cells = {tuple(c) for row in self.catalog['types'] if row['key'] == key for c in row['world_cells']}
            grades, radii = [], []
            for cell, source in paths.polyline_fragments(ramp['points']):
                if cell not in cells:
                    continue
                routes = paths.slice_routes([{'points': [_world(cell, p) for p in source]}])[cell]
                saved = parse_paths(paths.encode_paths(routes))[0]['points']
                # Do not invent a straight chord over a stamp-owned PATH
                # interval between two fragments of the same ramp owner.
                points = [_world(cell, p) for p in saved]
                grades.extend(abs(b[2] - a[2]) / math.dist(a[:2], b[:2]) * 100
                              for a, b in zip(points, points[1:]))
                if cell not in WING_CELLS[name]:
                    radii.append(_minimum_radius(points))
            self.assertLessEqual(max(grades), 30.0)
            expected = 25.43142572971316 if name.startswith('lower') else 29.60959566966601
            self.assertAlmostEqual(max(grades), expected, places=5, msg=name)
            # This radius bound applies to the former grade body, including
            # its retained upper collar, rather than the transferred throat.
            self.assertGreaterEqual(min(radii), 29.49, name)

    def test_inherited_high_transition_minima_are_reported_separately_from_new_r40_arcs(self):
        # These tight sampled transitions already existed inside/near the
        # auxiliary-lane handoff. Moving their owner must not silently turn
        # an R40 new-arc label into a whole-ramp minimum-radius claim.
        expected = {'lower-off': 1.7352766989404218, 'lower-on': 1.7352766989404165,
                    'upper-off': 3.4998096013736864, 'upper-on': 3.499809601354062}
        original = {ramp['id']: ramp for ramp in geometry.compact_ramps()}
        for name, ramp in self.ramps.items():
            self.assertAlmostEqual(_minimum_radius(ramp['points']), expected[name], places=6)
            self.assertAlmostEqual(_minimum_radius(original[name]['points']), expected[name], places=6)

    def test_new_circular_bends_really_measure_r40_and_ground_turns_remain_same_side(self):
        for name, ramp in self.ramps.items():
            canonical = (ramp['points'] if ramp['direction'] == 'off'
                         else [(-n, -e, z) for e, n, z in reversed(ramp['points'])])
            lower = ramp['deck'] == 'lower'
            interior = ([p for p in canonical if 11.0 < p[0] < 17.0 and p[1] > 35.0]
                        if lower else [p for p in canonical if -19.0 < p[0] < -7.0 and p[1] < -51.0])
            self.assertGreater(len(interior), 10, name)
            self.assertAlmostEqual(_minimum_radius(interior), 40.0, places=6, msg=name)
            ground = ramp['ground_points']
            self.assertTrue(all(p[2] == 0.0 for p in ground))
            # The route reaches only its adjacent carriageway. The opposite
            # side requires the separately directed on/off movement.
            outer_u = geometry.highway_coordinates(ramp['avenue_port'])[0]
            expected_sign = (1 if lower else -1) * (1 if ramp['direction'] == 'off' else -1)
            self.assertAlmostEqual(outer_u, expected_sign * 11.2 / math.sqrt(2.0), places=10)

    def test_longer_entrances_preserve_the_accepted_high_join_texture_phase(self):
        from scp_highway.ramp_materials import NativeRoadPainter
        originals = geometry.compact_ramps()
        turns = [{'points': row['surface_points']} for row in paths.compact_access_routes(originals)]
        with patch('scp_highway.ramp_materials.native_materials', return_value={}):
            previous = NativeRoadPainter({}, list(originals) + turns)
            current = modular._phase_matched_painter({}, list(self.ramps.values()))
        for name, ramp in self.ramps.items():
            boundary = ramp['modular_profile']['retained_boundary_m']
            old_frame = previous._frame(boundary)
            new_frame = current._frame(boundary)
            for axis in range(3):
                self.assertAlmostEqual(new_frame[axis], old_frame[axis], places=8, msg=name)


if __name__ == '__main__':
    unittest.main()
