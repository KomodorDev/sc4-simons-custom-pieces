"""Reject saved-route corruptions of the reviewed six-tile DD transition."""
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.track_paths import PATH
from scp.verify import parse_paths
from scp_highway import orthogonal_transition_verify as check


def encode(routes, *, elevation=1):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', str(elevation)]
    for route in routes:
        lines.extend(str(route[key]) for key in ('transport', 'lane', 'entry', 'exit', 'compatibility'))
        lines.append(str(len(route['points'])))
        lines.extend(','.join(f'{v:.9f}' for v in point) for point in route['points'])
    return ('\n'.join(lines) + '\n').encode('ascii')


def fixture(*, mirrored=False):
    piece = {'id': check.PIECE_ID, 'recipe': check.RECIPE, 'domain': 'highway',
        'footprint': [2, 6], 'cells': [list(cell) for cell in check.CELLS],
        'tile_ids': [f'{0x7f700000 + x * 0x100 + y * 0x10:08x}' for x, y in check.CELLS],
        'shadow_mappings': [], 'model_shadows': {'enabled': False},
        'engineering': {'model_only_cells': [[0, 0]], 'max_grade_percent': 30.,
                        'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8}}
    if mirrored:
        piece['id'] = check.MIRRORED_PIECE_ID
        piece['recipe'] = check.MIRRORED_RECIPE
        piece['transition_variant'] = 'mirrored'
        piece['engineering']['model_only_cells'] = [[1, 0]]
    resources = {(*PATH, int(tile, 16)): encode(check.expected_cell_routes(mirrored=mirrored)[cell])
                 for cell, tile in zip(check.CELLS, piece['tile_ids'])}
    return piece, resources


def replace_cell(resources, piece, cell, mutation):
    tile = int(piece['tile_ids'][check.CELLS.index(cell)], 16)
    parsed = parse_paths(resources[*PATH, tile])
    mutation(parsed)
    resources[*PATH, tile] = encode(parsed['routes'], elevation=parsed['terrain'])


class OrthogonalTransitionPathTests(unittest.TestCase):
    def test_complete_saved_fixture_preserves_four_native_lanes_in_all_proper_rotations(self):
        piece, resources = fixture()
        report = check.check_paths(resources, piece)
        self.assertTrue(report['passed'])
        self.assertEqual(report['complete_directed_journeys'], 4)
        self.assertEqual(report['complete_native_boundary_members_checked'], 8)
        self.assertEqual(report['route_fragments_checked'], 26)
        self.assertEqual(report['model_only_cells'], [[0, 0]])
        self.assertEqual([r['quarter_turns'] for r in report['proper_rotations']], [0, 1, 2, 3])
        self.assertTrue(report['use_path_elevation'])
        self.assertTrue(report['native_ground_classes_preserved'])
        self.assertFalse(report['game_operation_tested'])
        self.assertGreater(report['maximum_grade_percent'], 19.)
        self.assertLess(report['maximum_grade_percent'], 20.)


    def test_missing_lane_or_entire_traffic_cell_is_rejected(self):
        for remove_all in (False, True):
            with self.subTest(remove_all=remove_all):
                piece, resources = fixture()
                replace_cell(resources, piece, (1, 3), lambda p: p['routes'].clear() if remove_all else p['routes'].pop())
                with self.assertRaisesRegex(ValueError, 'omits a lane'):
                    check.check_paths(resources, piece)

    def test_native_endpoint_displacement_and_wrong_height_are_rejected(self):
        for axis, change in ((0, .001), (2, -7.5)):
            with self.subTest(axis=axis):
                piece, resources = fixture()
                def corrupt(parsed):
                    p = list(parsed['routes'][0]['points'][0])
                    p[axis] += change
                    parsed['routes'][0]['points'][0] = tuple(p)
                replace_cell(resources, piece, (1, 0), corrupt)
                with self.assertRaisesRegex(ValueError, 'differs from independent'):
                    check.check_paths(resources, piece)

    def test_flattened_active_height_and_capacity_stub_are_rejected(self):
        piece, resources = fixture()
        replace_cell(resources, piece, (1, 2), lambda p: p['routes'][0]['points'].__setitem__(
            1, (*p['routes'][0]['points'][1][:2], 0.)))
        with self.assertRaisesRegex(ValueError, 'differs from independent'):
            check.check_paths(resources, piece)
        piece, resources = fixture()
        stub = {'transport': 1, 'lane': 0, 'entry': 0, 'exit': 3, 'compatibility': 0,
                'points': [(-7., -7.1, 0.), (-7.1, -7., 0.)]}
        replace_cell(resources, piece, (0, 0), lambda p: p['routes'].append(stub))
        with self.assertRaisesRegex(ValueError, 'differs from independent'):
            check.check_paths(resources, piece)

    def test_native_class_change_is_required_only_at_ground_end(self):
        for cell in ((1, 0), (0, 5)):
            with self.subTest(cell=cell):
                piece, resources = fixture()
                replace_cell(resources, piece, cell, lambda p: p['routes'][0].__setitem__('lane', 9))
                with self.assertRaisesRegex(ValueError, 'differs from independent'):
                    check.check_paths(resources, piece)

    def test_reversed_lane_and_wrong_engine_transport_are_rejected(self):
        for kind in ('reverse', 'transport'):
            with self.subTest(kind=kind):
                piece, resources = fixture()
                def corrupt(parsed):
                    route = parsed['routes'][0]
                    if kind == 'reverse':
                        route['points'].reverse()
                        route['entry'], route['exit'] = route['exit'], route['entry']
                    else:
                        route['transport'] = 7
                replace_cell(resources, piece, (0, 3), corrupt)
                with self.assertRaisesRegex(ValueError, 'differs from independent'):
                    check.check_paths(resources, piece)

    def test_elevation_flag_loss_is_rejected_even_when_saved_xyz_stays_correct(self):
        piece, resources = fixture()
        replace_cell(resources, piece, (1, 2), lambda p: p.__setitem__('terrain', 0))
        with self.assertRaisesRegex(ValueError, 'explicitly retain'):
            check.check_paths(resources, piece)

    def test_false_model_only_declaration_or_different_ownership_is_rejected(self):
        for kind in ('empty', 'cells', 'shadow'):
            with self.subTest(kind=kind):
                piece, resources = fixture()
                if kind == 'empty':
                    piece['engineering']['model_only_cells'].append([0, 1])
                elif kind == 'cells':
                    piece['cells'][0] = [2, 0]
                else:
                    piece['model_shadows']['enabled'] = True
                with self.assertRaises(ValueError):
                    check.check_paths(resources, piece)

    def test_lower_declared_grade_ceiling_still_applies_to_correct_curves(self):
        piece, resources = fixture()
        piece['engineering']['max_grade_percent'] = 18.
        with self.assertRaisesRegex(ValueError, 'declared lane-grade ceiling'):
            check.check_paths(resources, piece)

    def test_profiles_keep_whole_tile_outlets_opposing_handedness_and_flat_collars(self):
        self.assertAlmostEqual(check._integrals()[1], .1907977564225265, places=11)
        self.assertAlmostEqual(check.upper_height(69.), 3.4257737165664643, places=9)
        for component, height in (('upper', 15.), ('lower', 7.5)):
            for lane in (0, 1):
                self.assertEqual(check.lane_point(component, lane, 0.)[2], height)
                self.assertEqual(check.lane_point(component, lane, 3.)[2], height)
                self.assertEqual(check.lane_point(component, lane, 96.)[2], 0.)
        self.assertEqual(check.lane_point('upper', 0, 96.)[:2], (-2.5, -88.))
        self.assertEqual(check.lane_point('upper', 1, 96.)[:2], (2.5, -88.))
        self.assertEqual(check.lane_point('lower', 0, 96.)[:2], (18.5, -88.))
        self.assertEqual(check.lane_point('lower', 1, 96.)[:2], (13.5, -88.))

    def test_connector_semantics_classify_all_sixteen_pairs_and_name_real_ground_rhw(self):
        piece, _resources = fixture()
        facts = check.reviewed_facts(piece)
        self.assertEqual(len(facts['ports']), 8)
        self.assertEqual(len(facts['movements']), 4)
        self.assertEqual(len(facts['forbidden_transfers']), 12)
        self.assertEqual(len(facts['channels']), 4)
        self.assertEqual({p['variant'] for p in facts['ports'] if p['endpoint_m'][2] == 0.}, {'rhw-4-l0'})
        self.assertEqual(facts['path_hashes_by_cell'], [])
        self.assertEqual(facts['raw_path_fingerprint_status'], 'requires-checked-saved-build-freeze')
        self.assertFalse(set(facts['movements']) & set(facts['forbidden_transfers']))
        for channel in facts['channels']:
            self.assertEqual(tuple(channel['ports']), next(pair for pair in facts['movements'] if pair[0] in channel['ports']))

    def test_restored_construction_retains_owned_model_only_cell_and_literal_native_flags(self):
        piece, resources = fixture()
        fields = {'CellLayout': ['ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', '^...'],
                  'ConsLayout': ['++.<', '++..', '++..', '++..', '++..', '++..', '^...'],
                  'CheckType': [f'{chr(97+i)} - dirtroad: 0x{word:08x}'
                                for i, word in enumerate(check.CORE_ROAD_WORDS)], 'Costs': ['1000']}
        self.assertEqual(check.check_construction_fields(fields, piece, resources)['occupied_cells_checked'], 12)
        for kind in ('empty-ownership', 'wrong-flag', 'wrong-network', 'wrong-cost', 'wrong-anchor'):
            damaged = deepcopy(fields)
            if kind == 'empty-ownership':
                damaged['ConsLayout'][0] = '.+.<'
            elif kind == 'wrong-flag':
                damaged['CheckType'][2] = 'c - dirtroad: 0x02000200'
            elif kind == 'wrong-network':
                damaged['CheckType'][0] = 'a - avenue: 0x00000000'
            elif kind == 'wrong-cost':
                damaged['Costs'] = ['100']
            else:
                damaged['CellLayout'][-1] = '.^..'
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                check.check_construction_fields(damaged, piece, resources)


class MirroredOrthogonalTransitionPathTests(unittest.TestCase):
    def test_reflected_reversed_saved_lanes_preserve_four_journeys_and_all_rotations(self):
        piece, resources = fixture(mirrored=True)
        report = check.check_paths(resources, piece)
        self.assertTrue(report['passed'])
        self.assertEqual(report['route_fragments_checked'], 26)
        self.assertEqual(report['complete_native_boundary_members_checked'], 8)
        self.assertEqual(report['model_only_cells'], [[1, 0]])
        self.assertEqual([r['quarter_turns'] for r in report['proper_rotations']], [0, 1, 2, 3])
        self.assertTrue(report['no_lane_or_carriageway_transfers'])

    def test_every_mirrored_fragment_is_the_independent_reflection_and_reversal(self):
        original, mirrored = check.expected_cell_routes(), check.expected_cell_routes(mirrored=True)
        for (column, row), routes in mirrored.items():
            source = original[1-column, row]
            self.assertEqual(len(routes), len(source))
            for route in routes:
                match = next(p for p in source if p['component'] == route['component']
                             and p['source_class'] == route['source_class'])
                points = [(-x, north, height) for x, north, height in reversed(match['points'])]
                self.assertEqual(route['lane'], match['lane'])
                self.assertEqual(len(points), len(route['points']))
                self.assertTrue(all(math.dist(a, b) < 1e-10 for a, b in zip(points, route['points'])))

    def test_exact_native_ports_preserve_dd_pose_two_and_ground_opposing_poses(self):
        actual = {(p['component'], p['source_class'], p['direction']): p
                  for p in check.external_ports(mirrored=True)}
        for source_class, upper_x, lower_x in ((0, 2.5, -2.5), (1, -2.5, 2.5)):
            upper = actual['upper', source_class, 'out']
            lower = actual['lower', source_class, 'in']
            self.assertEqual(upper['point_m'], (upper_x, 8., 15.))
            self.assertEqual(lower['point_m'], (lower_x, 8., 7.5))
            self.assertEqual(upper['tangent'], (0., 1.))
            self.assertEqual(lower['tangent'], (0., -1.))
            self.assertEqual(actual['upper', source_class, 'in']['point_m'], (16.+upper_x, -88., 0.))
            self.assertEqual(actual['lower', source_class, 'out']['point_m'], (lower_x, -88., 0.))

    def test_wrong_identity_variant_pair_is_rejected(self):
        for identity, variant in ((check.PIECE_ID, 'mirrored'), (check.MIRRORED_PIECE_ID, None),
                                  (check.MIRRORED_PIECE_ID, 'original'), (check.MIRRORED_PIECE_ID, True)):
            piece, resources = fixture(mirrored=True)
            piece['id'] = identity
            if variant is None:
                piece.pop('transition_variant')
            else:
                piece['transition_variant'] = variant
            with self.subTest(identity=identity, variant=variant), self.assertRaisesRegex(ValueError, 'identity.*variant'):
                check.check_paths(resources, piece)

    def test_each_owner_requires_its_distinct_recipe_even_with_correct_variant_and_geometry(self):
        for mirrored in (False, True):
            piece, resources = fixture(mirrored=mirrored)
            piece['recipe'] = check.RECIPE if mirrored else check.MIRRORED_RECIPE
            with self.subTest(mirrored=mirrored), self.assertRaisesRegex(ValueError, 'owner or recipe'):
                check.check_paths(resources, piece)

    def test_original_payload_cannot_be_relabelled_as_mirrored(self):
        original, resources = fixture()
        piece, _ = fixture(mirrored=True)
        self.assertEqual(original['tile_ids'], piece['tile_ids'])
        with self.assertRaisesRegex(ValueError, 'differs from independent|omits a lane fragment'):
            check.check_paths(resources, piece)

    def test_mirrored_shape_without_reversed_travel_is_rejected(self):
        piece, resources = fixture(mirrored=True)
        def corrupt(parsed):
            route = parsed['routes'][0]
            route['points'].reverse()
            route['entry'], route['exit'] = route['exit'], route['entry']
        replace_cell(resources, piece, (0, 0), corrupt)
        with self.assertRaisesRegex(ValueError, 'differs from independent'):
            check.check_paths(resources, piece)

    def test_mirrored_height_class_missing_channel_and_false_empty_cell_are_rejected(self):
        for mutation in ('height', 'class', 'missing', 'empty'):
            piece, resources = fixture(mirrored=True)
            if mutation == 'empty':
                piece['engineering']['model_only_cells'] = [[0, 0]]
            else:
                def corrupt(parsed):
                    if mutation == 'missing':
                        parsed['routes'].pop()
                    elif mutation == 'class':
                        parsed['routes'][0]['lane'] += 2
                    else:
                        p = parsed['routes'][0]['points'][0]
                        parsed['routes'][0]['points'][0] = (*p[:2], p[2]-7.5)
                replace_cell(resources, piece, (0, 0), corrupt)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                check.check_paths(resources, piece)

    def test_mirrored_core_flags_retain_the_reflected_empty_shoulder_and_tangents(self):
        piece, resources = fixture(mirrored=True)
        fields = {'CellLayout': ['ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', '^...'],
                  'ConsLayout': ['##.<', '##..', '##..', '##..', '##..', '##..', '^...'],
                  'Costs': ['1000'], 'CheckType': [f'{chr(97+i)} - dirtroad: 0x{word:08X}'
                      for i, word in enumerate(check.MIRRORED_CORE_ROAD_WORDS)]}
        self.assertEqual(check.check_construction_fields(fields, piece, resources)['occupied_cells_checked'], 12)
        fields['CheckType'][1] = 'b - dirtroad: 0x02000200'
        with self.assertRaisesRegex(ValueError, 'endpoint-tangent flags'):
            check.check_construction_fields(fields, piece, resources)

    def test_mirrored_flat_base_uses_measured_code7_at_all_twenty_one_vertices(self):
        piece, _ = fixture(mirrored=True)
        fields = {'ConsLayout': ['##.<', '##..', '##..', '##..', '##..', '##..', '^...']}
        report = check.check_mirrored_terrain_constraints(fields, piece)
        self.assertEqual(report['native_constraint_code'], 7)
        self.assertEqual(report['inserted_equality_pairs'], 36)
        self.assertEqual([row['quarter_turns'] for row in report['proper_rotations']], [0, 1, 2, 3])
        self.assertTrue(all(row['constrained_vertices'] == 21 and row['flat_height_groups'] == 1
                            for row in report['proper_rotations']))
        self.assertFalse(report['absolute_world_height_fixed'])
        self.assertFalse(report['authored_path_heights_changed'])
        self.assertFalse(report['game_terrain_behavior_tested'])

    def test_mirrored_flat_base_rejects_ignored_plus_missing_and_sloped_constraints(self):
        piece, resources = fixture(mirrored=True)
        fields = {'CellLayout': ['ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', '^...'],
                  'ConsLayout': ['##.<', '##..', '##..', '##..', '##..', '##..', '^...'],
                  'Costs': ['1000'], 'CheckType': [f'{chr(97+i)} - dirtroad: 0x{word:08X}'
                      for i, word in enumerate(check.MIRRORED_CORE_ROAD_WORDS)]}
        for replacement in ('+', '.', '|'):
            damaged = deepcopy(fields)
            damaged['ConsLayout'][0] = replacement+'#.<'
            with self.subTest(replacement=replacement):
                with self.assertRaises(ValueError):
                    check.check_mirrored_terrain_constraints(damaged, piece)
                with self.assertRaises(ValueError):
                    check.check_construction_fields(damaged, piece, resources)
        old = deepcopy(fields)
        old['ConsLayout'] = [line.replace('#', '+') for line in old['ConsLayout']]
        with self.assertRaises(ValueError):
            check.check_mirrored_terrain_constraints(old, piece)

    def test_code7_corner_graph_detects_an_unconstrained_corner_in_every_rotation(self):
        constraints = ['+#.<', '##..', '##..', '##..', '##..', '##..', '^...']
        for turns in range(4):
            groups = check._terrain_vertex_components(constraints, turns)
            with self.subTest(turns=turns):
                self.assertEqual(sorted(map(len, groups)), [1, 20])

    def test_mirrored_flat_base_policy_cannot_change_original_transition(self):
        piece, resources = fixture()
        fields = {'CellLayout': ['ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', '^...'],
                  'ConsLayout': ['++.<', '++..', '++..', '++..', '++..', '++..', '^...'],
                  'Costs': ['1000'], 'CheckType': [f'{chr(97+i)} - dirtroad: 0x{word:08X}'
                      for i, word in enumerate(check.CORE_ROAD_WORDS)]}
        report = check.check_construction_fields(fields, piece, resources)
        self.assertNotIn('terrain_constraints', report)
        with self.assertRaisesRegex(ValueError, 'restricted to the mirrored'):
            check.check_mirrored_terrain_constraints(fields, piece)
        fields['ConsLayout'] = [line.replace('+', '#') for line in fields['ConsLayout']]
        with self.assertRaises(ValueError):
            check.check_construction_fields(fields, piece, resources)

    def test_facing_original_and_mirrored_keep_the_same_four_directed_dd_lanes(self):
        report = check.check_opposite_end_direction_pair()
        self.assertTrue(report['passed'])
        self.assertEqual(report['native_dd_lanes_checked'], 4)
        self.assertEqual(report['mirrored_quarter_turns'], 2)
        self.assertFalse(report['construction_or_game_connection_tested'])

    def test_default_original_expectations_and_accepted_connector_semantics_stay_exact(self):
        self.assertEqual(check.expected_cell_routes(), check.expected_cell_routes(mirrored=False))
        self.assertEqual(check.external_ports(), check.external_ports(mirrored=False))
        from scp import jsonc
        from scp_highway import orthogonal_transition_contracts
        piece = jsonc.load(ROOT/'domains/highway/00_pieces'/check.PIECE_ID/'piece.jsonc')
        accepted = orthogonal_transition_contracts.load_contract(piece, ROOT)
        self.assertEqual(accepted['reference_piece_id'], check.PIECE_ID)
        mirrored, _ = fixture(mirrored=True)
        self.assertNotEqual(orthogonal_transition_contracts.reference(piece), orthogonal_transition_contracts.reference(mirrored))


class LowerBendRightPathTests(unittest.TestCase):
    def setUp(self):
        self.variant = check.LOWER_BEND_RIGHT
        self.piece, self.original = fixture()
        self.piece.update(id=check.LOWER_BEND_RIGHT_PIECE_ID,
                          recipe=check.RECIPE + '_lower_bend_right', transition_variant=self.variant)
        self.piece['engineering']['max_grade_percent'] = 20.
        self.routes = check.expected_cell_routes(variant=self.variant)
        self.resources = {(*PATH, int(tile, 16)): encode(self.routes[cell])
                          for cell, tile in zip(check.CELLS, self.piece['tile_ids'])}

    def test_lower_bend_keeps_dd_phase_and_swaps_ground_outlets(self):
        ports = {port['id']: (port['point_m'], port['source_cell'], port['tangent'])
                 for port in check.external_ports(variant=self.variant)}
        self.assertEqual(ports['upper-lane-01-out'], ((18.5, 8., 15.), [1, 0], (0., 1.)))
        self.assertEqual(ports['lower-lane-01-in'], ((13.5, 8., 7.5), [1, 0], (0., -1.)))
        self.assertEqual(ports['upper-lane-01-in'], ((18.5, -88., 0.), [1, 5], (0., 1.)))
        self.assertEqual(ports['lower-lane-01-out'], ((-2.5, -88., 0.), [0, 5], (0., -1.)))
        for cell in ((0, 5), (1, 5)):
            self.assertEqual(sorted(route['lane'] for route in self.routes[cell]), [1, 2])
        result = check.check_paths(self.resources, self.piece)
        self.assertEqual(result['model_only_cells'], [[0, 0]])
        self.assertEqual([row['complete_directed_journeys'] for row in result['proper_rotations']], [4]*4)
        self.assertAlmostEqual(result['maximum_grade_percent'], 100.*15./78., places=5)

    def test_old_upper_bend_with_same_traffic_phase_is_rejected(self):
        upper_bend = check.expected_cell_routes(variant='opposite-side-mirrored')
        wrong = {(*PATH, int(tile, 16)): encode(upper_bend[cell])
                 for cell, tile in zip(check.CELLS, self.piece['tile_ids'])}
        with self.assertRaisesRegex(ValueError, 'PATH differs'):
            check.check_paths(wrong, self.piece)

    def test_lower_bend_requires_existing_core_words_and_native_flat_constraint(self):
        fields = {'CellLayout': ['ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', '^...'],
                  'ConsLayout': ['##.<', '##..', '##..', '##..', '##..', '##..', '^...'],
                  'Costs': ['1000'], 'CheckType': [f'{chr(97+i)} - dirtroad: 0x{word:08X}'
                      for i, word in enumerate(check.CORE_ROAD_WORDS)]}
        result = check.check_construction_fields(fields, self.piece, self.resources)
        self.assertEqual([row['constrained_vertices'] for row in result['terrain_constraints']['proper_rotations']],
                         [21]*4)
        fields['ConsLayout'][0] = '+#.<'
        with self.assertRaisesRegex(ValueError, 'construction changes'):
            check.check_construction_fields(fields, self.piece, self.resources)


if __name__ == '__main__':
    unittest.main()
