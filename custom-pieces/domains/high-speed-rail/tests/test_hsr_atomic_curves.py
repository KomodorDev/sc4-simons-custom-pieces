"""Check bounded tail extraction, ordinary-straight joins and retained curves.

These source tests preserve the approved current curve types, independently
measure encoded routes and protect native collars, supports and texture phase.
Actual saved-model and whole-assembly checks remain separate requirements.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import unittest

from scp.track_paths import PATH, encode_paths, _parse_paths
from scp.subject_sources import piece_directory
from scp_hsr.hsr_atomic_curves import (
    RECIPES, atomic_info, atomic_layout, atomic_routes, model_inputs,
)
from scp_hsr.hsr_mesh_verify import measure_journey_quality
from scp_hsr.directional_t_verify import _TURN_LIMITS
from scp_hsr.track_shapes import _construction_flags
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
from scp_hsr.hsr_atomic_components_verify import check_paths

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.jsonc').is_file())
PIECES = ROOT/'domains/high-speed-rail/00_pieces'
DEPARTURE = 'hsr_component_l2_shortened_departure_curve'
RETURN = 'hsr_component_l2_shortened_return_curve'
CURRENT_GEOMETRY = {
    DEPARTURE: '7ed9e49ca138d574844feab776efc773103b929e3847604034827c43b5a722e2',
    RETURN: '0f04d613c74b98134ffd4466be454f3ac6cd646ecf424dab0d45e676ba1b2ef7',
}


class AtomicCurveSourceTests(unittest.TestCase):
    def test_current_curve_geometry_keeps_its_frozen_source_bytes(self):
        for recipe, digest in CURRENT_GEOMETRY.items():
            self.assertEqual(hashlib.sha256((piece_directory(recipe, ROOT)/'geometry.json')
                                           .read_bytes()).hexdigest(), digest)

    def test_literal_footprints_keep_all_required_curve_and_structural_cells(self):
        self.assertEqual(set(RECIPES), {DEPARTURE, RETURN})
        contracts = {
            DEPARTURE: ([(0, 0), (1, 0), (2, 0), (3, 0), (2, 1), (3, 1), (4, 1),
                         (3, 2), (4, 2), (4, 3), (4, 4), (4, 5)], [(0, 0), (2, 1), (4, 1)]),
            RETURN: ([(1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1),
                      (0, 2), (1, 2), (0, 3), (0, 4), (0, 5)], [(4, 0), (0, 1), (2, 1)]),
        }
        for recipe, (cells, structural) in contracts.items():
            new = atomic_layout(recipe)
            self.assertEqual(list(new), cells)
            self.assertEqual(atomic_info(recipe)['footprint'], (5, 6))
            self.assertEqual([cell for cell in new if not new[cell]['routes']], structural)
            self.assertFalse(any(row == 6 for column, row in new))

    def test_two_native_centreline_ends_and_exact_cardinal_encoded_chords(self):
        departure = atomic_routes(DEPARTURE)['W>S']
        returning = atomic_routes(RETURN)['S>E']
        self.assertEqual(departure[0], (22.398518552216863, 8., 15.5))
        self.assertEqual(departure[-2:], [(64., -87.875, 15.5), (64., -88., 15.5)])
        self.assertEqual(returning[:2], [(0., -88., 15.5), (0., -87.875, 15.5)])
        self.assertEqual(returning[-1], (41.60148144778314, 8., 15.5))
        self.assertEqual(atomic_info(DEPARTURE)['port_vectors']['Sout'], (0., -1.))
        self.assertEqual(atomic_info(RETURN)['port_vectors']['Sin'], (0., 1.))

    def test_saved_native_join_has_a_two_point_five_metre_flat_collar(self):
        for recipe, centre in ((DEPARTURE, 64.), (RETURN, 0.)):
            encoded = []
            for (column, row), data in atomic_layout(recipe).items():
                if data['routes']:
                    encoded.extend((x+16*column, north-16*row, height)
                                   for route in _parse_paths(encode_paths(data['routes']))
                                   for x, north, height in route['points'])
            collar = [point for point in encoded if point[1] <= -85.5]
            self.assertTrue(collar)
            self.assertTrue(all(point[0] == centre for point in collar))
            self.assertEqual(min(point[1] for point in collar), -88.)
            self.assertEqual(max(point[1] for point in collar), -85.5)
            self.assertTrue(all(point[2] == 15.5 for point in encoded))

    def test_all_encoded_paths_match_the_approved_current_dat_fingerprints(self):
        # Captured from the approved current compiled assets, including empty
        # structural PATHs, rather than computed from deleted geometry.
        expected = {
            DEPARTURE: '701020ad9bfe72b6c9291c8c7e694b5333355ecaea4924525651d77a9388d3f5',
            RETURN: 'cdd6e01fccaa9433dc30394a2b2bf979799277669e8a991d5bcb859f6b80888a',
        }
        for recipe, digest in expected.items():
            fingerprints = [[list(cell), hashlib.sha256(
                encode_paths(data['routes']) if data['routes'] else EMPTY_STRUCTURAL_PATH
            ).hexdigest()] for cell, data in atomic_layout(recipe).items()]
            self.assertEqual(hashlib.sha256(json.dumps(fingerprints, separators=(',', ':')).encode()).hexdigest(), digest)

    def test_tail_corrections_are_mirrored_and_directionally_reversed(self):
        departure = atomic_layout(DEPARTURE)[4, 5]['routes'][0]['points']
        returning = atomic_layout(RETURN)[0, 5]['routes'][0]['points']
        self.assertEqual(len(departure), len(returning))
        for (x, north, height), (xx, nn, hh) in zip(reversed(departure), returning):
            self.assertLessEqual(abs(x+xx), 8e-15)
            self.assertEqual((north, height), (nn, hh))

    def test_route_quality_with_the_reused_straight_retains_strict_curve_limits(self):
        for recipe in RECIPES:
            points = next(iter(atomic_routes(recipe).values()))
            points = (points+[(64., -104., 15.5)] if recipe == DEPARTURE else
                      [(0., -104., 15.5)]+points)
            # The unchanged custom northern cut has intentional nonzero
            # curvature; native endpoint curvature belongs to the south.
            limits = {**_TURN_LIMITS, 'max_endpoint_curvature_per_m': .02}
            result = measure_journey_quality(points, limits)
            self.assertGreater(result['minimum_sampled_radius_m'], 55.)
            self.assertLess(result['maximum_curvature_change_per_m2'], .0015)
            self.assertEqual(result['maximum_grade_change_per_m'], 0.)

    def test_native_straight_construction_categories_are_emitted_at_new_south_edges(self):
        for recipe, column, expected in ((DEPARTURE, 4, 0x02000100), (RETURN, 0, 0x02000300)):
            layout = atomic_layout(recipe); info = atomic_info(recipe)
            self.assertEqual(info['construction_flags'][column, 5], expected)
            self.assertEqual(_construction_flags(layout[column, 5]['routes']), expected)

    def test_independent_native_approach_curvature_passes_from_saved_paths(self):
        for recipe in RECIPES:
            info = atomic_info(recipe)
            tiles = [f'{0x7ff00000+column*0x100+row*0x10:08x}' for column, row in info['cells']]
            spec = {'id': recipe.replace('_', '-'), 'recipe': recipe,
                    'cells': info['cells'], 'footprint': info['footprint'],
                    'structural_cells': info['structural_cells'], 'tile_ids': tiles}
            resources = {(*PATH, int(tile, 16)):
                         encode_paths(data['routes']) if data['routes'] else EMPTY_STRUCTURAL_PATH
                         for tile, data in zip(tiles, atomic_layout(recipe).values())}
            measured = check_paths(resources, spec)['journey_quality']
            quality = next(iter(measured.values()))
            self.assertLessEqual(max(quality['native_endpoint_curvature_per_m'].values()), .0005)
            self.assertGreater(quality['minimum_sampled_radius_m'], 24.)
            self.assertLessEqual(quality['maximum_curvature_change_per_m2'], .0015)

    def test_support_transfer_preserves_remaining_centres_and_source_frame(self):
        for recipe, column in ((DEPARTURE, 4), (RETURN, 0)):
            info = atomic_info(recipe); mapping, context = model_inputs(recipe)
            self.assertEqual(len(info['support_centers']), 6)
            self.assertNotIn((16.*column, -96.), info['support_centers'])
            self.assertNotIn((column, 6), mapping)
            self.assertEqual(len(context['support_centers']), 6)
            self.assertEqual(info['origin_shift'], (80., 16.) if recipe == DEPARTURE else (-16., 16.))

    def test_current_sources_keep_their_complete_rejection_decisions(self):
        for recipe in RECIPES:
            new = json.loads((piece_directory(recipe, ROOT)/'geometry.json').read_text())
            decisions = new['atomization']['decision_rejections']
            self.assertEqual(len(decisions), 4)
            self.assertTrue(all(item['decision'] in ('reject', 'retain') for item in decisions))

    def test_return_texture_phase_is_anchored_to_its_unchanged_curve(self):
        new = json.loads((PIECES/'hsr-l2-single-track-oneway-curve-oblique-exit/geometry.json').read_text())
        after = new['surface_context']['surface_decks'][-1]
        anchor = [0.03534376208327217, -175.44817131476105, 15.5]

        def distance_to(deck, point):
            distance = float(deck.get('uv_offset', 0.))
            for a, b in zip(deck['points'], deck['points'][1:]):
                distance += math.hypot(b[0]-a[0], b[1]-a[1])
                if b == point:
                    return distance
            self.fail('The unchanged texture-phase anchor is missing')

        self.assertAlmostEqual(distance_to(after, anchor), 24.55191303742102, places=12)
        self.assertAlmostEqual(after['uv_offset'], -4.418609778511495e-05, places=16)


if __name__ == '__main__':
    unittest.main()
