"""Independent literal ports, topology and geometry for reusable HSR parts."""
from __future__ import annotations

from collections import Counter, defaultdict
import itertools
import math
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))

from scp_hsr.hsr_components_layout import (INFO, RECIPES, component_layout, component_routes,
                                       physical_decks, deck_half_widths)
from scp_hsr.directional_t_verify import measure_route_quality
from scp_hsr.hsr_components_verify import CONTRACTS
from scp_hsr.rail_geometry import _global_decks


STRAIGHT = 'hsr_component_upper_paired_straight'
RAMP = 'hsr_component_paired_ramp_l2_to_l4'
CROSSING = 'hsr_component_modular_crossing_core'
ADAPTER = 'hsr_component_upper_paired_to_single_adapter'
PAIRED = 'hsr_component_upper_paired_curve90_'
SINGLE = 'hsr_component_oneway_curve90_'

# The shortened opposed merge's north branch now joins the mainline at its
# western external boundary; the separate straight owns their continuation.
INTERIOR_JUNCTION_DEGREES = {}


def _point(point):
    return tuple(round(value, 6) for value in point)


def _fragments(recipe):
    return [(route['movement'], [_point((x+16.*column, y-16.*row, z))
                                for x, y, z in route['points']])
            for (column, row), data in component_layout(recipe).items()
            for route in data['routes']]


class HsrComponentsLayoutTests(unittest.TestCase):
    def test_core_literal_native_ports(self):
        expected = {
            STRAIGHT: {'S>N': ((2., -8., 30.5), (2., 8., 30.5)),
                       'N>S': ((-2., 8., 30.5), (-2., -8., 30.5))},
            RAMP: {'S>N': ((2., -120., 15.5), (2., 8., 30.5)),
                   'N>S': ((-2., 8., 30.5), (-2., -120., 15.5))},

        }
        for recipe, movements in expected.items():
            routes = component_routes(recipe)
            self.assertEqual(set(routes), set(movements))
            for movement, endpoints in movements.items():
                self.assertEqual((routes[movement][0], routes[movement][-1]), endpoints)

    def test_curves_have_exact_native_right_hand_ports(self):
        expected = {
            'right': {'S>E': ((2., -104., 30.5), (104., -2., 30.5)),
                      'E>S': ((104., 2., 30.5), (-2., -104., 30.5))},
            'left': {'S>W': ((98., -104., 30.5), (-8., 2., 30.5)),
                     'W>S': ((-8., -2., 30.5), (94., -104., 30.5))},
        }
        for hand, movements in expected.items():
            routes = component_routes(PAIRED+hand)
            self.assertEqual(set(routes), set(movements))
            for movement, endpoints in movements.items():
                self.assertEqual((routes[movement][0], routes[movement][-1]), endpoints)
            for levels, heights in (('l2_to_l4', (15.5, 30.5)), ('l4_to_l2', (30.5, 15.5))):
                route, = component_routes(SINGLE+hand+'_'+levels).values()
                self.assertEqual(route[0], (0. if hand == 'right' else 96., -104., heights[0]))
                self.assertEqual(route[-1], (104. if hand == 'right' else -8., 0., heights[1]))

    def test_external_chords_are_flat_native_facing_and_at_least_eight_metres(self):
        for recipe in RECIPES:
            # Exact tile partitions retain original samples. Curved ends
            # match literal custom ports; native ends are checked for a
            # cumulative eight-metre flat collar by their independent
            # verifier, even when the first encoded chord is only 0.5 m.
            if CONTRACTS[recipe]['kind'] == 'partition_component':
                continue
            for movement, points in component_routes(recipe).items():
                source, target = movement.split('>')
                vectors = CONTRACTS[recipe]['port_vectors']
                for (first, last), direction in ((points[:2], vectors[source+'in']),
                                                 (points[-2:], vectors[target+'out'])):
                    dx, dy = last[0]-first[0], last[1]-first[1]
                    length = math.hypot(dx, dy)
                    self.assertGreaterEqual(length, 8.-1e-9, (recipe, movement))
                    self.assertAlmostEqual(dx/length, direction[0], places=9)
                    self.assertAlmostEqual(dy/length, direction[1], places=9)
                    self.assertEqual(first[2], last[2])

    def test_every_cell_seam_preserves_the_exact_permitted_directed_journeys(self):
        # This graph is built from the sliced local records rather than the
        # generator's complete routes. Shared XYZ nodes are deliberately global:
        # an accidental equal-height seam would create additional journeys.
        for recipe in RECIPES:
            graph = defaultdict(set)
            incoming, outgoing = Counter(), Counter()
            fragments = _fragments(recipe)
            for _, points in fragments:
                first, last = points[0], points[-1]
                self.assertNotEqual(first, last)
                graph[first].add(last)
                outgoing[first] += 1
                incoming[last] += 1
            # The independent contract permits intentional splits and merges.
            # Ports with more than one movement can legitimately have degree2;
            # the opposed merge has one literal two-in/one-out interior join;
            # every other interior seam retains exactly one continuation.
            contract = CONTRACTS[recipe]
            starts = {_point(point): label for label, point in contract['ports'].items()
                      if label.endswith('in')}
            ends = {_point(point): label for label, point in contract['ports'].items()
                    if label.endswith('out')}
            self.assertEqual(set(outgoing)-set(incoming), set(starts), recipe)
            self.assertEqual(set(incoming)-set(outgoing), set(ends), recipe)
            for start, source in starts.items():
                visited, todo = set(), [start]
                while todo:
                    point = todo.pop()
                    if point in visited:
                        continue
                    visited.add(point)
                    todo.extend(graph[point]-visited)
                expected = {target for candidate, target in contract['movements']
                            if candidate == source}
                self.assertEqual({ends[p] for p in visited if p in ends}, expected, recipe)
            target_counts = Counter(target for source, target in contract['movements'])
            source_counts = Counter(source for source, target in contract['movements'])
            internal = INTERIOR_JUNCTION_DEGREES.get(recipe, {})
            actual_internal = {
                point: {'incoming': incoming[point], 'outgoing': outgoing[point]}
                for point in set(incoming) | set(outgoing)
                if point not in starts and point not in ends
                and (incoming[point] > 1 or outgoing[point] > 1)
            }
            self.assertEqual(actual_internal, internal, recipe)
            for point, count in incoming.items():
                limit = target_counts[ends[point]] if point in ends else internal.get(point, {}).get('incoming', 1)
                self.assertLessEqual(count, limit, recipe)
            for point, count in outgoing.items():
                limit = source_counts[starts[point]] if point in starts else internal.get(point, {}).get('outgoing', 1)
                self.assertLessEqual(count, limit, recipe)

    def test_full_slab_reservation_includes_literal_structure_only_cells(self):
        paired_right = {(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                        (0, 2), (1, 2), (2, 2), (0, 3), (1, 3),
                        (0, 4), (1, 4), (0, 5), (0, 6)}
        single_right = {(2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                        (1, 1), (2, 1), (3, 1), (0, 2), (1, 2),
                        (0, 3), (1, 3), (0, 4), (0, 5), (0, 6)}
        paired_structural = {(1, 0), (0, 1), (3, 1), (4, 1), (2, 2), (1, 3), (1, 4)}
        for hand in ('left', 'right'):
            transform = lambda cells: {(6-x, row) if hand == 'left' else (x, row) for x, row in cells}
            self.assertEqual(set(component_layout(PAIRED+hand)), transform(paired_right))
            self.assertEqual(set(INFO[PAIRED+hand]['structural_cells']), transform(paired_structural))
            for levels in ('l2_to_l4', 'l4_to_l2'):
                recipe = SINGLE+hand+'_'+levels
                self.assertEqual(set(component_layout(recipe)), transform(single_right))
                self.assertEqual(set(INFO[recipe]['structural_cells']), transform({(3, 1), (1, 3)}))
        for recipe in RECIPES:
            layout = component_layout(recipe)
            structural = set(INFO[recipe]['structural_cells'])
            for cell, data in layout.items():
                self.assertEqual(not data['routes'], cell in structural)
                if cell in structural:
                    self.assertEqual(INFO[recipe]['construction_flags'][cell], 0)

    def test_all_cell_keys_are_unique_within_the_engine_byte_map(self):
        for recipe in RECIPES:
            info = INFO[recipe]
            width, depth = info['footprint']
            self.assertLessEqual(width, 16)
            self.assertLessEqual(depth, 16)
            self.assertEqual(len({((row << 4)+column+1) & 255 for column, row in info['cells']}),
                             len(info['cells']))
            self.assertEqual(info['cells'], sorted(info['cells'], key=lambda cell: (cell[1], cell[0])))
            # Prices are independently pinned; the sparse fan keeps its price
            # after four empty cells were removed from its ownership mask.
            self.assertEqual(info['cost'], CONTRACTS[recipe]['cost'])

    def test_paired_curves_have_one_full_deck_and_constant_four_metre_track_spacing(self):
        for hand in ('right', 'left'):
            recipe = PAIRED+hand
            decks = physical_decks(recipe)
            self.assertEqual(len(decks), 1)
            self.assertEqual(decks[0]['width'], 15.)
            forward, reverse = component_routes(recipe).values()
            self.assertEqual(len(forward), len(reverse))
            for first, last, center in zip(forward, reversed(reverse), decks[0]['points']):
                self.assertAlmostEqual(math.dist(first, last), 4., places=9)
                self.assertLess(math.dist(tuple((a+b)/2. for a, b in zip(first, last)), center), 1e-9)
            restored, = _global_decks(component_layout(recipe))
            self.assertEqual(len(restored['points']), len(decks[0]['points']))
            self.assertLess(max(math.dist(a, b) for a, b in zip(restored['points'], decks[0]['points'])), 1e-12)

    def test_turn_quality_and_height_changes_are_measured_from_actual_samples(self):
        limits = {'max_raw_turn_degrees': 3., 'min_radius_m': 50.,
                  'max_length_ratio': 1.55, 'max_total_turn_degrees': 90.01,
                  'max_sample_turn_degrees': 4.6, 'max_endpoint_curvature_per_m': .001,
                  'max_curvature_change_per_m2': .008, 'max_grade_change_per_m': .011}
        for recipe in RECIPES:
            for movement, points in component_routes(recipe).items():
                for first, last in zip(points, points[1:]):
                    run = math.dist(first[:2], last[:2])
                    self.assertGreater(run, 1e-8)
                    self.assertLessEqual(abs(last[2]-first[2])/run, .156251)
                if 'curve90' not in recipe:
                    continue
                tight = CONTRACTS[recipe]['kind'] == 'tight_paired_curved_grade'
                quality = measure_route_quality(points, {**limits, 'min_radius_m': 24.} if tight else limits)
                self.assertGreater(quality['minimum_sampled_radius_m'], 24. if tight else 53.)
                turn = sum(math.atan2((b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0]),
                                      (b[0]-a[0])*(c[0]-b[0])+(b[1]-a[1])*(c[1]-b[1]))
                           for a, b, c in zip(points, points[1:], points[2:]))
                expected = -90. if movement in ('S>E', 'W>S') else 90.
                self.assertAlmostEqual(math.degrees(turn), expected, places=8)

    def test_true_crossing_contains_four_routes_on_two_separate_levels(self):
        routes = component_routes(CROSSING)
        crossings = []
        for (first_name, first), (last_name, last) in itertools.combinations(routes.items(), 2):
            a, b = first
            c, d = last
            u, v = (b[0]-a[0], b[1]-a[1]), (d[0]-c[0], d[1]-c[1])
            determinant = u[0]*v[1]-u[1]*v[0]
            if not determinant:
                continue
            delta = c[0]-a[0], c[1]-a[1]
            t = (delta[0]*v[1]-delta[1]*v[0])/determinant
            s = (delta[0]*u[1]-delta[1]*u[0])/determinant
            if 0. < t < 1. and 0. < s < 1.:
                self.assertEqual(abs(a[2]-c[2]), 15.)
                crossings.append((first_name, last_name))
        self.assertEqual(len(crossings), 4)
        from scp_hsr.hsr_partition_components import model_inputs
        _, context = model_inputs(CROSSING)
        self.assertEqual({deck['width'] for deck in context['surface_decks']}, {15.})
        self.assertEqual(set(component_layout(CROSSING)), {(0, 0)})

    def test_adapter_joins_native_pair_to_two_centred_fillers_on_separate_columns(self):
        routes = component_routes(ADAPTER)
        self.assertEqual((routes['S>N'][0], routes['S>N'][-1]),
                         ((2., -120., 30.5), (16., 8., 30.5)))
        self.assertEqual((routes['N>S'][0], routes['N>S'][-1]),
                         ((0., 8., 30.5), (-2., -120., 30.5)))
        self.assertEqual(INFO[ADAPTER]['footprint'], (2, 8))
        self.assertEqual(INFO[ADAPTER]['cells'], [(column, row) for row in range(8)
                                                 for column in range(2) if (column, row) != (1, 7)])
        self.assertEqual(INFO[ADAPTER]['structural_cells'], [(1, 5), (1, 6)])
        # Complete single tracks move apart without swapping sides.  These
        # samples are aligned by north-coordinate, independently of the two
        # slightly different travelled distances used to taper their widths.
        for northbound, southbound in zip(routes['S>N'], reversed(routes['N>S'])):
            self.assertEqual(northbound[1:], southbound[1:])
            self.assertGreaterEqual(northbound[0]-southbound[0], 4.-1e-10)
        limits = {'max_raw_turn_degrees': 3., 'min_radius_m': 120.,
                  'max_length_ratio': 1.02, 'max_total_turn_degrees': 30.,
                  'max_sample_turn_degrees': 4.6, 'max_endpoint_curvature_per_m': .001,
                  'max_curvature_change_per_m2': .008, 'max_grade_change_per_m': .011}
        for points in routes.values():
            measure_route_quality(points, limits)

    def test_adapter_taper_has_exact_native_outer_width_and_independent_eight_metre_outputs(self):
        west, east = physical_decks(ADAPTER)
        self.assertEqual((west['name'], east['name']), ('adapter_west', 'adapter_east'))
        for deck in (west, east):
            halves = deck_half_widths(deck)
            self.assertEqual(halves[:2], [5.5, 5.5])
            self.assertEqual(halves[-2:], [4., 4.])
            self.assertTrue(all(b <= a for a, b in zip(halves, halves[1:])))
            self.assertEqual(deck['taper_extra_half_width'], 1.5)
            self.assertEqual(deck['taper_start_distance'], 8.)
            total = sum(math.dist(a[:2], b[:2]) for a, b in zip(deck['points'], deck['points'][1:]))
            self.assertAlmostEqual(deck['taper_end_distance'], total-8., places=9)
            self.assertLess(max(abs(a-b) for a, b in zip(halves, halves[1:])), .02)
        pair_left = west['points'][0][0]-deck_half_widths(west)[0]
        pair_right = east['points'][0][0]+deck_half_widths(east)[0]
        self.assertEqual((pair_left, pair_right), (-7.5, 7.5))
        # At the north end both footprints exactly match ordinary8m fillers;
        # the central8m gap is intentionally open rather than a slab of ballast.
        west_end = west['points'][-1][0]+deck_half_widths(west)[-1]
        east_end = east['points'][-1][0]-deck_half_widths(east)[-1]
        self.assertEqual((west_end, east_end), (4., 12.))

    def test_returned_geometry_is_fresh_and_unknown_recipe_is_rejected(self):
        for function in (component_layout, component_routes, physical_decks):
            with self.assertRaisesRegex(ValueError, 'Unknown HSR component'):
                function('missing_component')
        layout = component_layout(RAMP)
        layout[0, 0]['routes'][0]['points'][0] = (999., 999., 999.)
        self.assertNotEqual(component_layout(RAMP)[0, 0]['routes'][0]['points'][0], (999., 999., 999.))
        routes = component_routes(PAIRED+'left')
        routes['S>W'][0] = (999., 999., 999.)
        self.assertEqual(component_routes(PAIRED+'left')['S>W'][0], (98., -104., 30.5))


if __name__ == '__main__':
    unittest.main()
