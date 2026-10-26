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

from scp.track_paths import encode_paths, _parse_paths
from scp_hsr.hsr_atomic_junctions import (
    RECIPES, _source, atomic_info, atomic_layout, atomic_routes, model_inputs,
    compilation_parts,
)
from scp_hsr.directional_t_verify import measure_route_quality, _TURN_LIMITS
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH

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
            'hsr-component-l2-short-mainline-diverge-core': '7760cdba90db6e0b12959708faf677121a0f5913edae65ef83d524006004baa0',
            'hsr-component-l2-short-opposed-merge-core': '42ce9230a30a536d358db4a6b5f3137ab38e19b3c33836293c074836b17ff833',
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
        self.assertEqual(second['footprint'], (5, 1))
        self.assertEqual(second['cells'], [(x, 0) for x in range(5)])
        self.assertEqual(second['ports']['E'], {'out': (72., -2., 15.5), 'in': (72., 2., 15.5)})
        self.assertEqual(second['ports']['N']['in'], (48.562688696411044, 8., 15.5))
        self.assertEqual(second['ports']['S']['in'], (25.601481447783137, -8., 15.5))
        self.assertEqual(second['support_centers'], [(16.*x, 0.) for x in range(5)])
        for recipe in RECIPES:
            mapping, inputs = model_inputs(recipe)
            self.assertEqual(len(mapping), len(atomic_info(recipe)['cells']))
            self.assertEqual(len(inputs['support_centers']), len(mapping))

    def test_encoded_direct_slip_sections_remain_mirror_reverses(self):
        west = [(x-96., n, h) for x, n, h in encoded_movement(DIVERGE, 'W>S')]
        east = [(x+32., n, h) for x, n, h in encoded_movement(MERGE, 'S>E')]
        reflected = [(-x, n, h) for x, n, h in reversed(east)]
        self.assertEqual(len(west), len(reflected))
        self.assertLessEqual(max(math.dist(a, b) for a, b in zip(west, reflected)), 2e-9)

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

    def test_all_encoded_paths_match_the_approved_current_dat_fingerprints(self):
        # Captured from the approved compiled DATs, then checked against the
        # current source encoder. No predecessor folders or build are needed.
        expected = {
            DIVERGE: '3d1aa91de0f3833eba19922270fb2ab2fd821682b329a4e08e50be5265270a85',
            MERGE: 'bc054d99d4908ccfc83ef1cff449c5992b73752d42eb462342fce694a9fa3811',
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
        for recipe, revised_cell in ((DIVERGE, (0, 0)), (MERGE, (4, 0))):
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
            MERGE: 'dc859cc8deffe2a3da9facfa81401841159516943ec3786ac9d858004c8b2d96',
        }
        for recipe, digest in expected.items():
            kept = _source(recipe)['retained_surface_context']
            self.assertEqual(hashlib.sha256(json.dumps(kept, sort_keys=True, separators=(',', ':')).encode()).hexdigest(), digest)


if __name__ == '__main__':
    unittest.main()
