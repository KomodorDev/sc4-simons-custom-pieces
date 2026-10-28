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
from scp.subject_identity import canonical_piece_id
from scp_hsr.hsr_compact_fan import RECIPES, compact_info, compact_layout, compact_routes, model_inputs
from scp_hsr.hsr_compact_fan_verify import CONTRACTS, check_paths
from scp_hsr.hsr_atomic_junctions import atomic_info
from scp_hsr.hsr_components import _sweep_component_profile
from scp_hsr.directional_t_verify import _TURN_LIMITS
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
from scp_hsr.rail_geometry import _route

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.jsonc').is_file())
CORE = 'hsr_component_l2_paired_fan_compact_core'
STRAIGHT = 'hsr_component_l2_paired_straight_recessed_web'
DIVERGE = 'hsr_component_l2_short_mainline_diverge_core'
MERGE = 'hsr_component_l2_short_opposed_merge_core'
STEM_NORTH = (8., 0., -16., -24., -28.)


def _point(point):
    return tuple(round(value, 6) for value in point)


def encoded_fan():
    info = compact_info(CORE)
    tiles = [f'{0x7ff00000+x*0x100+y*0x10:08x}' for x, y in info['cells']]
    spec = {'id': CORE.replace('_', '-'), 'recipe': CORE, 'cells': info['cells'],
            'footprint': info['footprint'], 'structural_cells': info['structural_cells'], 'tile_ids': tiles}
    resources = {(*PATH, int(tile, 16)): encode_paths(data['routes'])
                 if data['routes'] else EMPTY_STRUCTURAL_PATH
                 for tile, data in zip(tiles, compact_layout(CORE).values())}
    return spec, resources


def sampled_native_profile(deck):
    """Exercise the real shoulder warp without requiring a private NAM donor.

    Only native surface production is replaced by eight-metre profile probes
    and rail triangles. Route points, lengths, and taper settings come from
    the fan's actual authored deck, and the production shoulder warp runs.
    """
    points, lengths, _ = _route(deck['points'], deck.get('start_tangent'), deck.get('end_tangent'))
    sections, surfaces = [], []
    for north in (*STEM_NORTH, -72.):
        distance = 0.
        for first, last, length in zip(points, points[1:], lengths):
            dz = last[2]-first[2]
            if abs(dz) > 1e-12 and min(first[2], last[2])-1e-10 <= -north <= max(first[2], last[2])+1e-10:
                fraction = (-north-first[2])/dz
                center = tuple(a+fraction*(b-a) for a, b in zip(first, last))
                normal = dz/length, -(last[0]-first[0])/length
                station = distance+fraction*length
                break
            distance += length
        else:
            raise AssertionError(f'Actual fan deck has no section at north {north}')

        def vertex(offset, height):
            return (center[0]+offset*normal[0], height,
                    center[2]+offset*normal[1], offset/8., station/16.)

        surfaces.append(('wall', (vertex(-4., 14.), vertex(4., 14.), vertex(-4., 15.))))
        surfaces.append(('rail', (vertex(-.6, 16.2), vertex(.6, 16.2), vertex(-.6, 16.3))))
        sections.append({'north': north, 'center': center, 'normal': normal, 'station': station})
    # This is the independently measured native paired inside-wall position;
    # the shoulder transformation uses it to retain parapet thickness.
    source = {'inner': 5.996547698974609, 'outer': 7.5}
    original = deepcopy(surfaces)
    with patch('scp_hsr.hsr_components._sweep_native_profile',
               return_value=(surfaces, [], points, lengths)):
        changed = _sweep_component_profile(source, deck)[0]
    return sections, original, changed


class CompactFanSourceTests(unittest.TestCase):
    def test_parallel_stem_keeps_full_native_pair_width_before_the_arms_turn(self):
        decks = model_inputs(CORE)[1]['surface_decks']

        def paired_widths(profiles):
            return [max(vertex[0] for _, _, changed in profiles for vertex in changed[2*number][1])
                    - min(vertex[0] for _, _, changed in profiles for vertex in changed[2*number][1])
                    for number in range(len(STEM_NORTH))]

        current = [sampled_native_profile(deck) for deck in decks]
        for north, width in zip(STEM_NORTH, paired_widths(current)):
            with self.subTest(north=north):
                self.assertAlmostEqual(width, 15., places=8)
        # The former taper visibly squeezed the still-parallel stem. Reusing
        # that defect must fail the same measured-width requirement.
        old_decks = deepcopy(decks)
        for deck in old_decks:
            deck.update(taper_start_distance=8., taper_end_distance=48.)
        old_widths = paired_widths([sampled_native_profile(deck) for deck in old_decks])
        self.assertLess(old_widths[-1], 13.)
        with self.assertRaises(AssertionError):
            for width in old_widths:
                self.assertAlmostEqual(width, 15., places=8)

    def test_shoulder_width_fix_preserves_rails_and_the_eight_metre_lower_cut(self):
        for deck in model_inputs(CORE)[1]['surface_decks']:
            with self.subTest(deck=deck['name']):
                sections, original, changed = sampled_native_profile(deck)
                self.assertEqual([triangle for kind, triangle in changed if kind == 'rail'],
                                 [triangle for kind, triangle in original if kind == 'rail'])
                cut = sections[-1]
                self.assertEqual(cut['north'], -72.)
                self.assertGreater(cut['station'], 90.)
                normal, center = cut['normal'], cut['center']
                offsets = [(vertex[0]-center[0])*normal[0]+(vertex[2]-center[2])*normal[1]
                           for vertex in changed[-2][1]]
                self.assertAlmostEqual(max(offsets)-min(offsets), 8., places=8)
                for before, after in zip(original[-2][1], changed[-2][1]):
                    for expected, actual in zip(before, after):
                        self.assertAlmostEqual(actual, expected, places=10)

    def test_current_fan_family_has_only_the_core_and_matching_straight(self):
        self.assertEqual(RECIPES, (CORE, STRAIGHT))
        self.assertEqual(set(CONTRACTS), {CORE, STRAIGHT})
        info = compact_info(CORE)
        self.assertEqual(info['footprint'], (5, 3))
        self.assertEqual(info['cells'], [(2, 0), (1, 1), (2, 1), (3, 1),
                                         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)])
        self.assertEqual(info['structural_cells'], [(1, 1), (3, 1)])
        self.assertEqual(info['support_centers'], [(32., 0.), (32., -16.),
                                                  (16., -32.), (48., -32.)])
        self.assertEqual(list(compact_layout(CORE)), info['cells'])
        mapping, context = model_inputs(CORE)
        self.assertEqual(len(mapping), 9)
        self.assertEqual(len(context['layout']), 11)
        self.assertTrue(all('compact_native_corner' not in deck for deck in context['surface_decks']))
        compilation_cells = {tuple(cell) for cell, _ in context['layout']}
        for x, north in context['support_centers']:
            self.assertIn((math.floor((x+8)/16), math.floor((-north+8)/16)), compilation_cells)

    def test_fan_ports_use_p01a_angles_and_meet_the_reused_rotated_piece_exactly(self):
        info = compact_info(CORE)
        self.assertEqual(info['ports']['N'], {'in': (30., 8., 15.5), 'out': (34., 8., 15.5)})
        expected = {'Wout': (6.39851855221686, -40., 15.5),
                    'Ein': (57.60148144778314, -40., 15.5)}
        actual = {'Wout': info['ports']['W']['out'], 'Ein': info['ports']['E']['in']}
        for label in expected:
            self.assertLess(math.dist(actual[label], expected[label]), 1e-9)
        diverge, merge = atomic_info(DIVERGE), atomic_info(MERGE)
        sx, sy, sh = diverge['ports']['S']['out']
        fan_east_world = tuple(v + d for v, d in zip(actual['Ein'], (80., 48., 0.)))
        self.assertLess(math.dist(fan_east_world, (176.-sx, -sy, sh)), 1e-9)
        fan_west_world = tuple(v + d for v, d in zip(actual['Wout'], (80., 48., 0.)))
        self.assertLess(math.dist(fan_west_world,
                                 tuple(v+d for v, d in zip(merge['ports']['N']['in'], (48., 0., 0.)))), 1e-9)
        tangent = diverge['port_vectors']['Sout']
        self.assertEqual(info['port_vectors']['Ein'], tuple(-v for v in tangent))
        self.assertEqual(info['port_vectors']['Wout'], (-tangent[0], tangent[1]))
        self.assertEqual(info['port_vectors']['Wout'], merge['port_vectors']['Nin'])
        scene = json.loads((ROOT/'domains/high-speed-rail/01_assemblies/hsr-trumpet-straight-stem/assembly.json').read_text())
        copies = [row for row in scene['placements'] if row['piece_id'] == canonical_piece_id(DIVERGE, ROOT)]
        self.assertEqual([(row['origin_m'], row['rotation_degrees_ccw']) for row in copies],
                         [([-96., 0.], 0), ([176., 0.], 180)])
        # P26 owns the extracted western approach, so P07's local origin
        # moves east by one tile while this fan connection stays fixed.
        by_label = {row['label']: row for row in scene['placements']}
        self.assertEqual((by_label['P07']['piece_id'], by_label['P07']['origin_m'],
                          by_label['P07']['rotation_degrees_ccw']),
                         (canonical_piece_id(MERGE, ROOT), [48., 0.], 0))
        self.assertEqual((by_label['P26']['piece_id'], by_label['P26']['origin_m'],
                          by_label['P26']['rotation_degrees_ccw']),
                         ('hsr-l2-two-track-straight', [32., 0.], 270))
        self.assertFalse(any(row['piece_id'] == 'hsr-component-l2-compact-fan-diverge'
                             for row in scene['placements']))

    def test_local_fragments_have_only_the_two_permitted_directed_journeys(self):
        graph = defaultdict(set)
        for (column, row), data in compact_layout(CORE).items():
            for route in data['routes']:
                first, last = (_point((x+16*column, north-16*row, height))
                               for x, north, height in (route['points'][0], route['points'][-1]))
                graph[first].add(last)
        exits = {(6.398519, -40., 15.5): 'W', (34., 8., 15.5): 'N'}
        for start, expected in {(30., 8., 15.5): {'W'}, (57.601481, -40., 15.5): {'N'}}.items():
            reached, pending = set(), [start]
            while pending:
                point = pending.pop()
                if point not in reached:
                    reached.add(point)
                    pending.extend(graph[point]-reached)
            self.assertEqual({exits[point] for point in reached if point in exits}, expected)

    def test_two_fan_arms_are_reflected_reverses_at_the_same_native_l2_height(self):
        routes = compact_routes(CORE)
        self.assertEqual(set(routes), {'N>W', 'E>N'})
        first, last = routes['N>W'], list(reversed(routes['E>N']))
        self.assertEqual(len(first), len(last))
        self.assertLess(max(math.dist(a, (64.-b[0], b[1], b[2]))
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
        stale = deepcopy(CONTRACTS[CORE])
        stale['ports']['Wout'] = (16.562689, -72., 15.5)
        with patch.dict(CONTRACTS, {CORE: stale}), self.assertRaises(ValueError):
            check_paths(resources, spec)


if __name__ == '__main__':
    unittest.main()
