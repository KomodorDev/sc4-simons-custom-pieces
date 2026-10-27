"""Protect the revised fan, its reused junction, and independent PATH limits.

These source and encoded-route tests do not claim game operation. Complete
saved model ownership, track clearance, and native profiles are checked by
the compiled-resource verifier and the complete assembly audit separately.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

from scp.track_paths import PATH, encode_paths
from scp_hsr.hsr_compact_fan import RECIPES, compact_info, compact_layout, compact_routes, model_inputs
from scp_hsr.hsr_compact_fan_verify import CONTRACTS, check_paths
from scp_hsr.hsr_atomic_junctions import atomic_info
from scp_hsr.directional_t_verify import _TURN_LIMITS
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.json').is_file())
FAN = 'hsr_component_l2_paired_fan_compact_join'
DIVERGE = 'hsr_component_l2_short_mainline_diverge_core'
MERGE = 'hsr_component_l2_short_opposed_merge_core'


def _point(point):
    return tuple(round(value, 6) for value in point)


def encoded_fan():
    info = compact_info(FAN)
    tiles = [f'{0x7ff00000+x*0x100+y*0x10:08x}' for x, y in info['cells']]
    spec = {'id': FAN.replace('_', '-'), 'recipe': FAN, 'cells': info['cells'],
            'footprint': info['footprint'], 'structural_cells': info['structural_cells'], 'tile_ids': tiles}
    resources = {(*PATH, int(tile, 16)): encode_paths(data['routes'])
                 if data['routes'] else EMPTY_STRUCTURAL_PATH
                 for tile, data in zip(tiles, compact_layout(FAN).values())}
    return spec, resources


class CompactFanSourceTests(unittest.TestCase):
    def test_only_the_retained_fan_is_registered_with_its_literal_ownership_and_supports(self):
        self.assertEqual(RECIPES, (FAN,))
        self.assertEqual(set(CONTRACTS), {FAN})
        info = compact_info(FAN)
        self.assertEqual(info['footprint'], (7, 5))
        self.assertEqual(info['cells'], [(3, 0), (3, 1), (3, 2), (2, 3), (3, 3), (4, 3),
                                         (1, 4), (2, 4), (3, 4), (4, 4), (5, 4)])
        self.assertEqual(info['structural_cells'], [(2, 3), (4, 3)])
        self.assertEqual(info['support_centers'], [(48., 0.), (48., -16.), (48., -32.),
                                                  (48., -48.), (32., -64.), (64., -64.)])
        self.assertEqual(list(compact_layout(FAN)), info['cells'])
        mapping, context = model_inputs(FAN)
        self.assertEqual(len(mapping), 11)
        self.assertTrue(all('compact_native_corner' not in deck for deck in context['surface_decks']))
        for x, north in context['support_centers']:
            self.assertIn((math.floor((x+8)/16), math.floor((-north+8)/16)), set(mapping.values()))

    def test_fan_ports_use_p01a_angles_and_meet_the_reused_rotated_piece_exactly(self):
        info = compact_info(FAN)
        self.assertEqual(info['ports']['N'], {'in': (46., 8., 15.5), 'out': (50., 8., 15.5)})
        expected = {'Wout': (22.39851855221686, -72., 15.5),
                    'Ein': (73.60148144778314, -72., 15.5)}
        actual = {'Wout': info['ports']['W']['out'], 'Ein': info['ports']['E']['in']}
        for label in expected:
            self.assertLess(math.dist(actual[label], expected[label]), 1e-9)
        diverge, merge = atomic_info(DIVERGE), atomic_info(MERGE)
        sx, sy, sh = diverge['ports']['S']['out']
        fan_east_world = tuple(v + d for v, d in zip(actual['Ein'], (64., 80., 0.)))
        self.assertLess(math.dist(fan_east_world, (176.-sx, -sy, sh)), 1e-9)
        fan_west_world = tuple(v + d for v, d in zip(actual['Wout'], (64., 80., 0.)))
        self.assertLess(math.dist(fan_west_world,
                                 tuple(v+d for v, d in zip(merge['ports']['N']['in'], (32., 0., 0.)))), 1e-9)
        tangent = diverge['port_vectors']['Sout']
        self.assertEqual(info['port_vectors']['Ein'], tuple(-v for v in tangent))
        self.assertEqual(info['port_vectors']['Wout'], (-tangent[0], tangent[1]))
        self.assertEqual(info['port_vectors']['Wout'], merge['port_vectors']['Nin'])
        scene = json.loads((ROOT/'domains/high-speed-rail/01_assemblies/straight-stem-trumpet/assembly.json').read_text())
        copies = [row for row in scene['placements'] if row['piece_id'] == DIVERGE.replace('_', '-')]
        self.assertEqual([(row['origin_m'], row['rotation_degrees_ccw']) for row in copies],
                         [([-96., 0.], 0), ([176., 0.], 180)])
        self.assertFalse(any(row['piece_id'] == 'hsr-component-l2-compact-fan-diverge'
                             for row in scene['placements']))

    def test_local_fragments_have_only_the_two_permitted_directed_journeys(self):
        graph = defaultdict(set)
        for (column, row), data in compact_layout(FAN).items():
            for route in data['routes']:
                first, last = (_point((x+16*column, north-16*row, height))
                               for x, north, height in (route['points'][0], route['points'][-1]))
                graph[first].add(last)
        exits = {(22.398519, -72., 15.5): 'W', (50., 8., 15.5): 'N'}
        for start, expected in {(46., 8., 15.5): {'W'}, (73.601481, -72., 15.5): {'N'}}.items():
            reached, pending = set(), [start]
            while pending:
                point = pending.pop()
                if point not in reached:
                    reached.add(point)
                    pending.extend(graph[point]-reached)
            self.assertEqual({exits[point] for point in reached if point in exits}, expected)

    def test_two_fan_arms_are_reflected_reverses_at_the_same_native_l2_height(self):
        routes = compact_routes(FAN)
        self.assertEqual(set(routes), {'N>W', 'E>N'})
        first, last = routes['N>W'], list(reversed(routes['E>N']))
        self.assertEqual(len(first), len(last))
        self.assertLess(max(math.dist(a, (96.-b[0], b[1], b[2]))
                            for a, b in zip(first, last)), 2e-9)
        self.assertTrue(all(point[2] == 15.5 for route in routes.values() for point in route))

    def test_encoded_routes_satisfy_the_independent_literal_ports_and_strict_curve_limits(self):
        spec, resources = encoded_fan()
        result = check_paths(resources, spec)
        self.assertEqual(result['external_ports_checked'], 4)
        self.assertEqual(result['permitted_movements_checked'], 2)
        self.assertEqual(result['literal_port_tangents_checked'], 4)
        self.assertEqual(result['maximum_encoded_grade'], 0.)
        for quality in result['journey_quality'].values():
            self.assertGreater(quality['minimum_sampled_radius_m'], 24.)
            self.assertLessEqual(quality['maximum_curvature_change_per_m2'], .0015)
            self.assertLessEqual(max(quality['native_endpoint_curvature_per_m'].values()), .0005)
        self.assertEqual(_TURN_LIMITS['min_radius_m'], 24.)
        self.assertEqual(_TURN_LIMITS['max_curvature_change_per_m2'], .0015)
        self.assertEqual(_TURN_LIMITS['max_endpoint_curvature_per_m'], .0005)

    def test_missing_paths_and_old_ports_are_rejected_without_changing_the_source(self):
        spec, resources = encoded_fan()
        changed = dict(resources)
        tile = next(key for key, raw in changed.items() if raw != EMPTY_STRUCTURAL_PATH)
        changed[tile] = EMPTY_STRUCTURAL_PATH
        with self.assertRaises(ValueError):
            check_paths(changed, spec)
        stale = deepcopy(CONTRACTS[FAN])
        stale['ports']['Wout'] = (16.562689, -72., 15.5)
        with patch.dict(CONTRACTS, {FAN: stale}), self.assertRaises(ValueError):
            check_paths(resources, spec)


if __name__ == '__main__':
    unittest.main()
