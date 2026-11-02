"""Independently measure the source-only parallel-ramp proposal.

These checks examine sampled routes and full six-metre ribbons. They do not
compile a game model, verify structural loads, or record game observations.
"""
from collections import defaultdict
from itertools import combinations
import math
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp_highway import parallel_ramp_review as proposal
from scp_highway import ramp_paths
from scp_highway.native import parse_paths


def _uv(point):
    """Use the measured native centre, independently of the proposal helper."""
    return ((point[0] + point[1]) / math.sqrt(2),
            (point[1] - point[0] + 8) / math.sqrt(2))


def _world(u, v):
    return (4 + (u - v) / math.sqrt(2), -4 + (u + v) / math.sqrt(2))


def _section(route, kind):
    selected = next(s for s in route['segments'] if s['kind'] == kind)
    return route['points'][selected['start_index']:selected['end_index'] + 1]


def _direction(first, last):
    length = math.dist(first[:2], last[:2])
    return ((last[0] - first[0]) / length, (last[1] - first[1]) / length)


def _clip(poly, signed_distance):
    """Clip a convex polygon without using the provider's face partitioner."""
    if not poly:
        return []
    output = []
    before = poly[-1]
    a = signed_distance(before)
    for after in poly:
        b = signed_distance(after)
        if (a >= 0) != (b >= 0):
            fraction = a / (a - b)
            output.append(tuple(x + fraction * (y - x) for x, y in zip(before, after)))
        if b >= 0:
            output.append(after)
        before, a = after, b
    return output


def _area(poly):
    return abs(sum(a[0] * b[1] - a[1] * b[0]
                   for a, b in zip(poly, poly[1:] + poly[:1]))) / 2


def _polygon_cells(poly):
    """Count positive-area intersections, excluding a mere shared tile edge."""
    if len(poly) < 3 or _area(poly) < 1e-9:
        return set()
    result = set()
    for col in range(math.floor((min(p[0] for p in poly) + 8) / 16),
                     math.floor((max(p[0] for p in poly) + 8) / 16) + 1):
        for row in range(math.floor((8 - max(p[1] for p in poly)) / 16),
                         math.floor((8 - min(p[1] for p in poly)) / 16) + 1):
            clipped = poly
            for axis, boundary, sense in ((0, 16 * col - 8, 1), (0, 16 * col + 8, -1),
                                          (1, -16 * row - 8, 1), (1, -16 * row + 8, -1)):
                clipped = _clip(clipped, lambda p, a=axis, b=boundary, s=sense: s * (p[a] - b))
            if len(clipped) >= 3 and _area(clipped) > 1e-7:
                result.add((col, row))
    return result


def _path_cells(points):
    """Cut individual chords at the fixed city grid, independently."""
    output = set()
    for first, last in zip(points, points[1:]):
        cuts = [0., 1.]
        for axis in (0, 1):
            delta = last[axis] - first[axis]
            if abs(delta) < 1e-12:
                continue
            low, high = sorted((first[axis], last[axis]))
            for index in range(math.floor((low + 8) / 16), math.ceil((high + 8) / 16) + 1):
                at = (16 * index - 8 - first[axis]) / delta
                if 1e-10 < at < 1 - 1e-10:
                    cuts.append(at)
        cuts = sorted(set(cuts))
        for start, end in zip(cuts, cuts[1:]):
            fraction = (start + end) / 2
            east = first[0] + fraction * (last[0] - first[0])
            north = first[1] + fraction * (last[1] - first[1])
            output.add((math.floor((east + 8) / 16), math.floor((8 - north) / 16)))
    return output


def _road_quads(points):
    """Intersect successive offset lines to construct each six-metre miter."""
    tangents = [_direction(a, b) for a, b in zip(points, points[1:])]
    edges = []
    for index, point in enumerate(points):
        one = tangents[max(0, index - 1)]
        two = tangents[min(index, len(tangents) - 1)]
        n1, n2 = (-one[1], one[0]), (-two[1], two[0])
        determinant = one[0] * two[1] - one[1] * two[0]
        if abs(determinant) < 1e-10:
            offset = (3 * n2[0], 3 * n2[1])
        else:
            delta = (3 * (n2[0] - n1[0]), 3 * (n2[1] - n1[1]))
            distance = (delta[0] * two[1] - delta[1] * two[0]) / determinant
            offset = (3 * n1[0] + distance * one[0], 3 * n1[1] + distance * one[1])
        edges.append(((point[0] + offset[0], point[1] + offset[1], point[2]),
                      (point[0] - offset[0], point[1] - offset[1], point[2])))
    return [(a[0], a[1], b[1], b[0]) for a, b in zip(edges, edges[1:])]


def _overlap(one, two):
    """Separating-axis test for positive-area overlap of convex road strips."""
    for poly in (one, two):
        for a, b in zip(poly, poly[1:] + poly[:1]):
            axis = (b[1] - a[1], a[0] - b[0])
            first = [p[0] * axis[0] + p[1] * axis[1] for p in one]
            second = [p[0] * axis[0] + p[1] * axis[1] for p in two]
            if max(first) <= min(second) + 1e-9 or max(second) <= min(first) + 1e-9:
                return False
    return True


class ParallelRampReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = proposal.review()
        cls.candidates = cls.report['candidates']

    def test_native_high_ports_and_exact_one_step_upper_shift(self):
        expected = {'lower-off': (56., 51.2, 7.5), 'lower-on': (-51.2, -56., 7.5),
                    'upper-off': (-72., -83.2, 15.), 'upper-on': (83.2, 72., 15.)}
        for candidate in self.candidates:
            inward = candidate['id'] == 'parallel-inward-upper'
            for route in candidate['routes']:
                high = route['points'][0 if route['direction'] == 'off' else -1]
                old = expected[route['id']]
                shift = ((16., 16., 0.) if route['direction'] == 'off' else (-16., -16., 0.))
                for axis in range(3):
                    target = old[axis] + (shift[axis] if inward and route['deck'] == 'upper' else 0)
                    self.assertAlmostEqual(high[axis], target, places=10)
                collar = _section(route, 'flat-native-direction-collar')
                tangent = _direction(collar[0], collar[-1])
                sign = -1 if route['deck'] == 'lower' else 1
                self.assertAlmostEqual(tangent[0], sign / math.sqrt(2), places=9)
                self.assertAlmostEqual(tangent[1], sign / math.sqrt(2), places=9)

    def test_actual_parallel_descents_meet_avenue_at_right_angles(self):
        avenue = (-1 / math.sqrt(2), 1 / math.sqrt(2))
        for candidate in self.candidates:
            for route in candidate['routes']:
                points = _section(route, 'straight-parallel-descent')
                across = [_uv(point)[1] for point in points]
                self.assertLess(max(across) - min(across), 1e-10)
                tangent = _direction(points[0], points[-1])
                self.assertAlmostEqual(sum(a * b for a, b in zip(tangent, avenue)), 0., places=10)
                self.assertGreater(math.dist(points[0][:2], points[-1][:2]),
                                   25 if route['deck'] == 'lower' else 50)
                self.assertEqual(min(p[2] for p in points), 0.)
                self.assertEqual(max(p[2] for p in points), 7.5 if route['deck'] == 'lower' else 15.)

    def test_terminal_arcs_really_turn_right_and_stay_on_adjacent_carriageway(self):
        outer = 11.2 / math.sqrt(2)
        for candidate in self.candidates:
            for route in candidate['routes']:
                points = _section(route, 'ground-right-quarter-turn')
                self.assertTrue(all(p[2] == 0 for p in points))
                uv = [_uv(point) for point in points]
                avenue_point = uv[-1] if route['direction'] == 'off' else uv[0]
                sign = route['side'] * (1 if route['direction'] == 'off' else -1)
                self.assertAlmostEqual(avenue_point[0], sign * outer, places=10)
                self.assertGreater(min(sign * p[0] for p in uv), 0)
                for a, b, c in zip(points, points[1:], points[2:]):
                    first, last = (b[0] - a[0], b[1] - a[1]), (c[0] - b[0], c[1] - b[1])
                    cross = first[0] * last[1] - first[1] * last[0]
                    self.assertLess(cross, -1e-10)
                    radius = math.dist(a[:2], b[:2]) * math.dist(b[:2], c[:2])
                    radius *= math.dist(a[:2], c[:2]) / (2 * abs(cross))
                    self.assertAlmostEqual(radius, 6 if candidate['id'] == 'parallel-inward-upper' else 8,
                                           places=7)
                # Count the curved chords; neither a zero-radius corner nor
                # a single diagonal chord can pass the radius measurements.
                self.assertGreater(len(points), 40)

    def test_all_serialized_path_chords_keep_real_car_transport_and_30_percent_bound(self):
        for candidate in self.candidates:
            for route in candidate['routes']:
                split = ramp_paths.slice_routes([{'id': route['id'], 'transport': 1,
                                                  'points': route['points']}])
                maximum = 0.
                for cell, fragments in split.items():
                    self.assertIn(cell, set(map(tuple, route['path_cells'])))
                    for saved in parse_paths(ramp_paths.encode_paths(fragments)):
                        self.assertEqual(saved['transport'], 1)
                        self.assertIn(saved['entry'], range(4))
                        self.assertIn(saved['exit'], range(4))
                        for a, b in zip(saved['points'], saved['points'][1:]):
                            maximum = max(maximum, abs(b[2] - a[2]) / math.dist(a[:2], b[:2]))
                self.assertLessEqual(maximum, .300001)
                self.assertGreater(maximum, .17)

    def test_descending_full_width_sweep_clears_native_deck_even_after_float32_encoding(self):
        for candidate in self.candidates:
            for route in candidate['routes']:
                # Float32 is the saved model coordinate format. This is an
                # encoding control, not a claim that a new S3D was built.
                points = [struct.unpack('<3f', struct.pack('<3f', *p)) for p in route['points']]
                height = 7.5 if route['deck'] == 'lower' else 15
                minimum = math.inf
                for quad in _road_quads(points):
                    if min(p[2] for p in quad) < height - 1e-5:
                        inner = min(route['side'] * _uv(p)[1] for p in quad)
                        minimum = min(minimum, inner - 8)
                required_gap = 1 if candidate['id'] == 'parallel-inward-upper' else 2
                self.assertGreaterEqual(minimum, required_gap - .0001)

    def test_distinct_full_road_strips_have_clear_three_dimensional_corridors(self):
        for candidate in self.candidates:
            by_route = {}
            for route in candidate['routes']:
                cells = defaultdict(list)
                for quad in _road_quads(route['points']):
                    for cell in _polygon_cells(quad):
                        cells[cell].append(quad)
                by_route[route['id']] = cells
            for first, second in combinations(candidate['routes'], 2):
                one, two = by_route[first['id']], by_route[second['id']]
                for cell in one.keys() & two.keys():
                    for a in one[cell]:
                        for b in two[cell]:
                            if not _overlap(a, b):
                                continue
                            # Match the existing provider's one-metre deck
                            # and 3.8 m car corridor, without assuming wheelbase.
                            first_range = (min(p[2] for p in a) - 1, max(p[2] for p in a) + 3.8)
                            second_range = (min(p[2] for p in b) - 1, max(p[2] for p in b) + 3.8)
                            self.assertTrue(first_range[1] < second_range[0]
                                            or second_range[1] < first_range[0],
                                            (candidate['id'], first['id'], second['id'], cell))

    def test_independently_clipped_ribbons_and_paths_reproduce_declared_cells(self):
        for candidate in self.candidates:
            model, traffic = set(), set(map(tuple, candidate['stamp_cells']))
            traffic.update(map(tuple, candidate['avenue_cells']))
            for route in candidate['routes']:
                cells = set()
                for quad in _road_quads(route['points']):
                    clipped = _clip(list(quad), lambda p: route['side'] * _uv(p)[1] - 8)
                    cells.update(_polygon_cells(clipped))
                self.assertEqual(cells, set(map(tuple, route['model_cells'])))
                actual_paths = _path_cells(route['points'])
                self.assertEqual(actual_paths, set(map(tuple, route['path_cells'])))
                model.update(cells)
                traffic.update(actual_paths)
            owned = model | traffic
            self.assertEqual(owned, set(map(tuple, candidate['owned_cells'])))
            rectangle = (max(c[0] for c in owned) - min(c[0] for c in owned) + 1,
                         max(c[1] for c in owned) - min(c[1] for c in owned) + 1)
            expected = (31, (8, 8)) if candidate['id'] == 'parallel-inward-upper' else (40, (10, 10))
            self.assertEqual((len(owned), rectangle), expected)

    def test_actual_native_avenue_width_and_pedestrian_channels_fit_the_proposed_avenue_cells(self):
        # Independently measured from the saved native Avenue-only S3D and
        # PATHs: the complete pavement reaches |u|=8sqrt(2), and the two
        # pedestrian tracks lie at |u|=10.818734m. These checks preserve that
        # envelope, but cannot establish a new adaptive-sidewalk opening.
        for candidate in self.candidates:
            extent = max(abs(_uv(p)[1]) for r in candidate['routes']
                         for p in r['points'] if p[2] == 0)
            width = 8 * math.sqrt(2)
            polygon = [_world(u, v) for u, v in ((-width, -extent), (width, -extent),
                                                 (width, extent), (-width, extent))]
            avenue = set(map(tuple, candidate['avenue_cells']))
            self.assertLessEqual(_polygon_cells(polygon), avenue)
            for u in (-10.818734, 10.818734):
                self.assertLessEqual(_path_cells([_world(u, -extent), _world(u, extent)]), avenue)

    def test_explicit_supports_fit_below_their_road_and_avoid_other_road_corridors(self):
        for candidate in self.candidates:
            for route in candidate['routes']:
                parallel = _section(route, 'straight-parallel-descent')
                for support in route['supports']:
                    footprint = support['footprint_en']
                    self.assertAlmostEqual(_area(footprint), .64, places=9)
                    self.assertGreater(min(support['top_corner_heights_m']), 0)
                    for corner, top in zip(footprint, support['top_corner_heights_m']):
                        nearest = []
                        for a, b in zip(parallel, parallel[1:]):
                            delta = (b[0] - a[0], b[1] - a[1])
                            length2 = sum(v * v for v in delta)
                            at = sum((corner[i] - a[i]) * delta[i] for i in (0, 1)) / length2
                            if 0 <= at <= 1:
                                point = (a[0] + at * delta[0], a[1] + at * delta[1])
                                nearest.append((math.dist(corner, point), a[2] + at * (b[2] - a[2])))
                        distance, pavement = min(nearest)
                        self.assertLess(distance, 3)
                        self.assertAlmostEqual(top, pavement - 1, places=8)
                    for other in candidate['routes']:
                        if other['id'] == route['id']:
                            continue
                        for quad in _road_quads(other['points']):
                            if _overlap(footprint, quad):
                                self.assertLess(max(support['top_corner_heights_m']),
                                                min(p[2] for p in quad) - 1,
                                                (route['id'], other['id']))

    def test_separate_ramp_faces_clear_the_retained_central_highway_piers(self):
        original = {(-1, 1), (-1, 2), (1, -1), (2, -1), (-4, 4), (4, -4)}
        for candidate in self.candidates:
            retained = original & set(map(tuple, candidate['stamp_cells']))
            self.assertEqual(len(retained), 4 if candidate['id'] == 'parallel-inward-upper' else 6)
            piers = [[(16 * col + east, -16 * row + north)
                      for east, north in ((-.4, -.4), (.4, -.4), (.4, .4), (-.4, .4))]
                     for col, row in retained]
            for route in candidate['routes']:
                for quad in _road_quads(route['points']):
                    outside = _clip(list(quad), lambda p: route['side'] * _uv(p)[1] - 8)
                    if len(outside) < 3 or _area(outside) < 1e-9:
                        continue
                    for pier in piers:
                        self.assertFalse(_overlap(outside, pier),
                                         (candidate['id'], route['id'], pier))


if __name__ == '__main__':
    unittest.main()
