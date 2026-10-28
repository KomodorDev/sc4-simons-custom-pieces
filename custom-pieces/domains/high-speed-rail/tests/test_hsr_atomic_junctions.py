"""Check bounded symmetric HSR junction-tail atomization without game claims.

Purpose: protect current geometry, literal native/custom interfaces, bounded
analytic-context differences, encoded symmetry and strict curve-quality limits.
Current saved-model fingerprints are checked by the assembly resource audit.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import unittest

from scp.track_paths import PATH, encode_paths, _parse_paths
from scp_hsr.hsr_atomic_junctions import (
    RECIPES, _source, atomic_info, atomic_layout, atomic_routes, model_inputs,
    compilation_parts,
)
from scp_hsr.directional_t_verify import measure_route_quality, _TURN_LIMITS
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
from scp_hsr.hsr_atomic_components_verify import check_paths

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'project.json').is_file())
PIECES = ROOT/'domains/high-speed-rail/00_pieces'
DIVERGE, MERGE = RECIPES


def interpolated_north(points, east):
    for a, b in zip(points, points[1:]):
        if a[0] <= east <= b[0]:
            return a[1]+(east-a[0])*(b[1]-a[1])/(b[0]-a[0])
    raise AssertionError(f'No route section at {east}')


def encoded_movement(recipe, movement):
    parts = []
    for (column, row), data in atomic_layout(recipe).items():
        encoded = _parse_paths(encode_paths(data['routes']))
        for source, actual in zip(data['routes'], encoded):
            if source['movement'] == movement:
                parts.append([(x+16*column, n-16*row, h) for x, n, h in actual['points']])
    starts = {tuple(part[0]): part for part in parts}
    ends = {tuple(part[-1]) for part in parts}
    first = next(part for part in parts if tuple(part[0]) not in ends)
    points = list(first)
    while tuple(points[-1]) in starts:
        points.extend(starts[tuple(points[-1])][1:])
    return points


class AtomicJunctionSourceTests(unittest.TestCase):
    def test_current_junction_geometry_keeps_its_frozen_source_bytes(self):
        for identifier, digest in {
            'hsr-component-l2-short-mainline-diverge-core': 'cba97aca000381fee6d99dce0e63cf35d6be467b57b4e4b0b2db82ef4001cd9c',
            'hsr-component-l2-short-opposed-merge-core': '61083be80c1a6d067e4bd05e6434d5eb110b4485bd77452cfa671cad0cb9f6e9',
        }.items():
            self.assertEqual(hashlib.sha256((PIECES/identifier/'geometry.json').read_bytes()).hexdigest(), digest)

    def test_native_ports_custom_branch_ends_and_supports_are_literal(self):
        first, second = atomic_info(DIVERGE), atomic_info(MERGE)
        self.assertEqual(first['footprint'], (4, 1))
        self.assertEqual(first['cells'], [(0, 0), (1, 0), (2, 0), (3, 0)])
        self.assertEqual(first['ports'], {
            'W': {'in': (-8., -2., 15.5), 'out': (-8., 2., 15.5)},
            'E': {'out': (56., -2., 15.5), 'in': (56., 2., 15.5)},
            'S': {'out': (38.39851855221686, -8., 15.5)},
        })
        self.assertEqual(first['support_centers'], [(0., 0.), (16., 0.), (32., 0.), (48., 0.)])
        self.assertEqual(second['footprint'], (4, 1))
        self.assertEqual(second['cells'], [(x, 0) for x in range(4)])
        self.assertEqual(second['ports']['E'], {'out': (56., -2., 15.5), 'in': (56., 2., 15.5)})
        self.assertAlmostEqual(second['ports']['N']['in'][0], 38.39851855221686, places=10)
        self.assertEqual(second['ports']['N']['in'][1:], (8., 15.5))
        self.assertEqual(second['ports']['S']['in'], (9.601481447783137, -8., 15.5))
        self.assertEqual(second['support_centers'], [(16.*x, 0.) for x in range(4)])
        for recipe in RECIPES:
            mapping, inputs = model_inputs(recipe)
            self.assertEqual(len(mapping), len(atomic_info(recipe)['cells']))
            selected_supports = [(east, north) for east, north in inputs['support_centers']
                                 if (round(east/16.), round(-north/16.)) in mapping.values()]
            self.assertEqual(len(selected_supports), len(mapping))

    def test_encoded_direct_slip_sections_remain_mirror_reverses(self):
        west = [(x-96., n, h) for x, n, h in encoded_movement(DIVERGE, 'W>S')]
        east = [(x+48., n, h) for x, n, h in encoded_movement(MERGE, 'S>E')]
        reflected = [(-x, n, h) for x, n, h in reversed(east)]
        self.assertEqual(len(west), len(reflected))
        self.assertLessEqual(max(math.dist(a, b) for a, b in zip(west, reflected)), 2e-9)

    def test_reworked_north_merge_reuses_the_exact_reflected_reversed_diverge_branch(self):
        branch = atomic_routes(DIVERGE)['W>S']
        expected = [(x, -north, height) for x, north, height in reversed(branch)]
        actual = atomic_routes(MERGE)['N>W']
        self.assertEqual(len(actual), len(expected))
        self.assertLess(max(math.dist(a, b) for a, b in zip(expected, actual)), 2e-9)
        self.assertEqual(actual[-1], (-8., 2., 15.5))
        tangent = atomic_info(DIVERGE)['port_vectors']['Sout']
        self.assertEqual(atomic_info(MERGE)['port_vectors']['Nin'], (-tangent[0], tangent[1]))

    def test_reworked_merge_keeps_every_mainline_and_direct_south_route_fragment(self):
        unchanged = [[cell, {**data, 'routes': [route for route in data['routes'] if route['movement'] != 'N>W']}]
                     for cell, data in _source(MERGE)['layout']]
        digest = hashlib.sha256(json.dumps(unchanged, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        self.assertEqual(digest, 'a925be3cf41e6e996b48374aec8d266988ba180f6ef12747f63501d14f22b561')
        expected = {
            ('surface_context', 'native_east_west_main'): 'f3158f8eb882cfcc89d6afbdf31c454af1908ecf24ad259743931901d4910204',
            ('retained_surface_context', 'native_east_west_main'): 'f3158f8eb882cfcc89d6afbdf31c454af1908ecf24ad259743931901d4910204',
            ('surface_context', 'direct_south_east_merge'): '10ef1f1934c5841582ca202692203db025e47b070ccdc5139829e727cf26b685',
            ('retained_surface_context', 'direct_south_east_merge'): '84c9b3c1f89d972d0398bd58d219711d44815bd3987eb3525d74e718a12b70c4',
        }
        for (context, name), wanted in expected.items():
            deck = next(deck for deck in _source(MERGE)[context]['surface_decks'] if deck['name'] == name)
            self.assertEqual(hashlib.sha256(json.dumps(deck, sort_keys=True, separators=(',', ':')).encode()).hexdigest(), wanted)

    def test_new_merge_encoded_paths_satisfy_independent_literal_ports_and_curve_limits(self):
        info, layout = atomic_info(MERGE), atomic_layout(MERGE)
        tiles = [f'{0x7ff00000+x*0x100+y*0x10:08x}' for x, y in info['cells']]
        spec = {'id': MERGE.replace('_', '-'), 'recipe': MERGE, 'cells': info['cells'],
                'footprint': info['footprint'], 'structural_cells': info['structural_cells'], 'tile_ids': tiles}
        resources = {(*PATH, int(tile, 16)): encode_paths(data['routes'])
                     if data['routes'] else EMPTY_STRUCTURAL_PATH
                     for tile, data in zip(tiles, layout.values())}
        result = check_paths(resources, spec)
        self.assertEqual(result['external_ports_checked'], 6)
        self.assertEqual(result['unique_complete_journeys_checked'], 4)
        for quality in result['journey_quality'].values():
            if quality['minimum_sampled_radius_m'] is not None:
                self.assertGreaterEqual(quality['minimum_sampled_radius_m'], 24.)
            else:
                self.assertEqual(quality['total_turn_degrees'], 0.)
            self.assertLessEqual(quality['maximum_curvature_change_per_m2'], .0015)
        self.assertEqual(result['maximum_encoded_grade'], 0.)

    def test_owned_analytic_contexts_differ_only_inside_the_bounded_joining_tile(self):
        before = _source(DIVERGE)['retained_surface_context']['surface_decks'][1]['points']
        deck = next(d for d in _source(DIVERGE)['surface_context']['surface_decks']
                    if d['name'] == 'direct_west_south_curve')
        after = deck['points']
        knots = sorted({p[0] for p in before if 8. <= p[0] <= 24.}
                       | {p[0] for p in after if 8. <= p[0] <= 24.})
        deviation = max(abs(interpolated_north(before, x)-interpolated_north(after, x)) for x in knots)
        self.assertGreater(deviation, .0243)
        self.assertLessEqual(deviation, .0245)
        self.assertEqual([p for p in after if p[0] >= 24.], [p for p in before if p[0] >= 24.])
        self.assertTrue(all(p[1:] == [-2., 15.5] for p in after if p[0] <= 10.5))
        # Both owned contexts must agree at the far endpoint and later samples.
        self.assertEqual(after[-1], [96., -120., 15.5])
        self.assertEqual(after[-100:], before[-100:])

    def test_existing_curve_limits_pass_without_relaxation(self):
        source = _source(DIVERGE)
        deck = next(d for d in source['surface_context']['surface_decks'] if d['name'] == 'direct_west_south_curve')
        report = measure_route_quality(deck['points'], _TURN_LIMITS)
        self.assertGreater(report['minimum_sampled_radius_m'], 57.)
        self.assertLess(report['maximum_curvature_change_per_m2'], .0011)
        self.assertLess(report['maximum_endpoint_curvature_per_m'], .0003)
        self.assertEqual(_TURN_LIMITS['min_radius_m'], 24.)
        self.assertEqual(_TURN_LIMITS['max_curvature_change_per_m2'], .0015)
        self.assertEqual(_TURN_LIMITS['max_endpoint_curvature_per_m'], .0005)

    def test_encoded_paths_keep_the_current_source_revision_fingerprints(self):
        # DIVERGE retains its earlier compiled PATH fingerprint. MERGE binds
        # the revised source's encoded paths; actual saved DAT verification
        # remains a separate build check rather than an implied game result.
        expected = {
            DIVERGE: '3d1aa91de0f3833eba19922270fb2ab2fd821682b329a4e08e50be5265270a85',
            MERGE: '7935e98203ec9166f7fa4ee39e68c7f249c6caa54ff944d10f866566267b5539',
        }
        for recipe, digest in expected.items():
            fingerprints = [[list(cell), hashlib.sha256(
                encode_paths(data['routes']) if data['routes'] else EMPTY_STRUCTURAL_PATH
            ).hexdigest()] for cell, data in atomic_layout(recipe).items()]
            self.assertEqual(hashlib.sha256(json.dumps(fingerprints, separators=(',', ':')).encode()).hexdigest(), digest)

    def test_real_platform_wing_is_retained(self):
        data = _source(DIVERGE)
        mapping = {tuple(local): tuple(source) for local, source in data['surface_context']['selected_cells']}
        self.assertEqual(mapping[3, 0], (4, 0))
        decision = data['atomization_evidence']['physical_rejection']
        self.assertEqual(decision['local_xy'], [4, 0])
        self.assertEqual(decision['path_deviation_m'], 0.)
        self.assertEqual(decision['deck_extension_beyond_native_width_m'], .5)

    def test_two_analytic_contexts_have_disjoint_complete_output_and_support_ownership(self):
        for recipe, revised_cell in ((DIVERGE, (0, 0)), (MERGE, (3, 0))):
            with self.subTest(recipe=recipe):
                parts = compilation_parts(recipe)
                self.assertEqual(len(parts), 2)
                self.assertEqual(set(parts[0][0]), {revised_cell})
                self.assertNotIn(revised_cell, parts[1][0])
                self.assertEqual(set(parts[0][0]) | set(parts[1][0]), set(atomic_info(recipe)['cells']))
                source_cells = []
                supports = []
                for mapping, inputs in parts:
                    self.assertEqual(set(map(tuple, (cell for cell, data in inputs['layout']))), set(mapping.values()))
                    self.assertEqual(len(inputs['support_centers']), len(mapping))
                    source_cells.extend(mapping.values())
                    supports.extend(inputs['support_centers'])
                self.assertEqual(len(source_cells), len(set(source_cells)))
                self.assertEqual(len(supports), len(set(supports)))

    def test_retained_tiles_keep_their_owned_literal_analytic_surface_inputs(self):
        expected = {
            DIVERGE: '7741ec4ffb241b54a2ea0f01de5fd0e0d3d3d490668f766a006e64ee22d9a368',
        }
        for recipe, digest in expected.items():
            kept = _source(recipe)['retained_surface_context']
            self.assertEqual(hashlib.sha256(json.dumps(kept, sort_keys=True, separators=(',', ':')).encode()).hexdigest(), digest)

    def test_diverge_alignment_is_separate_from_literal_surface_contexts(self):
        source = _source(DIVERGE)
        rule = source['south_parapet_alignment']
        self.assertEqual(rule['left_branch'], 'direct_west_south_curve')
        self.assertEqual(rule['left_inner_half_width_m'], 2.6)
        self.assertEqual(rule['left_selection_limit_local_east_m'], 32.)
        self.assertNotIn('right_local_east_cap_m', rule)
        self.assertEqual(rule['right_join'], 'continuous_branch_inside_outline')
        self.assertEqual(rule['right_inner_half_width_m'], 2.6)
        self.assertEqual(rule['right_inner_join_local_east_m'], 40.361872522872716)
        self.assertEqual(rule['right_outer_join_local_east_m'], 43.669002829692054)
        self.assertNotIn('local_east_caps_m', rule)
        self.assertEqual(rule['source_east_offset_m'], 16.)
        self.assertEqual(rule['minimum_train_half_width_m'], 2.5)
        for mapping, inputs in compilation_parts(DIVERGE):
            for deck in inputs['surface_decks']:
                self.assertEqual(deck['south_parapet_alignment'], rule)
        for key in ('surface_context', 'retained_surface_context'):
            self.assertTrue(all('south_parapet_alignment' not in deck
                                for deck in source[key]['surface_decks']))
        self.assertNotIn('south_parapet_alignment', _source(MERGE))
        for mapping, inputs in compilation_parts(MERGE):
            self.assertTrue(all('south_parapet_alignment' not in deck
                                for deck in inputs['surface_decks']))


if __name__ == '__main__':
    unittest.main()
