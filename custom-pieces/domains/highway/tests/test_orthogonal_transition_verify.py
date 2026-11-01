"""Reject saved-route corruptions of the reviewed six-tile DD transition."""
from copy import deepcopy
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


def fixture():
    piece = {'id': check.PIECE_ID, 'recipe': check.RECIPE, 'domain': 'highway',
        'footprint': [2, 6], 'cells': [list(cell) for cell in check.CELLS],
        'tile_ids': [f'{0x7f700000 + x * 0x100 + y * 0x10:08x}' for x, y in check.CELLS],
        'shadow_mappings': [], 'model_shadows': {'enabled': False},
        'engineering': {'model_only_cells': [[0, 0]], 'max_grade_percent': 30.,
                        'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8}}
    resources = {(*PATH, int(tile, 16)): encode(check.expected_cell_routes()[cell])
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


if __name__ == '__main__':
    unittest.main()
