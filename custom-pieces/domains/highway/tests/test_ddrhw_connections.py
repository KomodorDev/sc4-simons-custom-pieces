"""Portable controls for outside-only, movable native DD approach requests."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.verify import parse_rules, check_emitted_runtime_addresses
from scp_highway import ddrhw_connections as connections
from scp_highway import recipes

BASES = {'ddrhw-diagonal-upper-exit-branch': 0x7F593000,
         'ddrhw-diagonal-upper-entry-branch': 0x7F594000,
         'ddrhw-modular-highway-stamp': 0x7F59D000,
         'ddrhw-parallel-upper-exit-slip': 0x7F5B3000,
         'ddrhw-parallel-upper-entry-slip': 0x7F5B4000}


def pieces():
    return {identifier: jsonc.load(ROOT / 'domains/highway/00_pieces' / identifier / 'piece.jsonc')
            for identifier in dict.fromkeys(end.piece_id for end in connections.ENDS)}


def legacy_fields(piece):
    width, depth = piece['footprint']
    rows = [['.'] * (width + 2) for _ in range(depth + 1)]
    rows[0][-1], rows[-1][0] = '<', '^'
    cons, checks = deepcopy(rows), []
    for index, (x, y) in enumerate(piece['cells']):
        symbol = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[index]
        rows[y][x], cons[y][x] = symbol, '+'
        checks.append(f'{symbol} - dirtroad: 0x00000301')
    return {'CellLayout': [''.join(row) for row in rows],
            'ConsLayout': [''.join(row) for row in cons], 'CheckType': checks,
            'AutoTileBase': [f'0x{BASES[piece["id"]]:08X}'],
            'Piece': ['unchanged preview'], 'Costs': ['1000']}


def extended(piece):
    old = legacy_fields(piece)
    rows, checks, cons = connections.add_approaches(
        piece, old['CellLayout'], old['CheckType'], old['ConsLayout'])
    return old, {**old, 'CellLayout': rows, 'CheckType': checks, 'ConsLayout': cons}


class NativeDDApproachTests(unittest.TestCase):
    def test_exact_six_ends_have_five_source_bound_owners(self):
        selected = pieces()
        self.assertEqual(len(selected), 5)
        rows = [(piece['id'], row) for piece in selected.values() for row in connections.approaches(piece)]
        self.assertEqual(len(rows), 6)
        self.assertEqual({row['end_tile_id'] for _, row in rows},
                         {'7f593020', '7f594200', '7f59d090', '7f59d900', '7f5b3010', '7f5b4100'})
        self.assertEqual({row['native_tile_id'] for _, row in rows}, {'57530900'})
        for identifier, row in rows:
            with self.subTest(piece=identifier, cell=row['cell']):
                self.assertNotIn(row['cell'], selected[identifier]['cells'])
                self.assertTrue(row['optional'] and row['experimental'])
                self.assertEqual(row['native_rotation'], 0)

    def test_legacy_absent_and_explicit_false_are_unchanged(self):
        for piece in pieces().values():
            for old in ({key: value for key, value in piece.items() if key != 'native_dd_approaches'},
                        {**piece, 'native_dd_approaches': False}):
                self.assertEqual(connections.approaches(old), [])
                self.assertEqual(connections.rul1_rows(old), ())
                fields = legacy_fields(old)
                self.assertEqual(connections.add_approaches(old, fields['CellLayout'], fields['CheckType'],
                                                            fields['ConsLayout']),
                                 (fields['CellLayout'], fields['CheckType'], fields['ConsLayout']))
                self.assertEqual(connections.check_construction_approaches(fields, old), fields)

    def test_non_boolean_and_unreviewed_owners_fail_closed(self):
        piece = next(iter(pieces().values()))
        for value in (1, 0, None, 'true', [], {}):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'exact boolean'):
                connections.approaches({**piece, 'native_dd_approaches': value})
        with self.assertRaisesRegex(ValueError, 'No reviewed'):
            connections.approaches({**piece, 'id': 'another-highway'})

    def test_changed_exterior_resource_recipe_or_cell_is_rejected(self):
        piece = pieces()['ddrhw-parallel-upper-exit-slip']
        for field, value in [('recipe', 'highway_another'), ('domain', 'high-speed-rail'),
                             ('tile_ids', ['7f5b3100', '7f5b3020']), ('cells', [[1, 0], [0, 2]])]:
            with self.subTest(field=field), self.assertRaises(ValueError):
                connections.approaches({**piece, field: value})

    def test_literals_have_four_proper_rotations_and_no_ground_mis_or_other_levels(self):
        expected = ((0x01000400, 0x03010000, 0x57530900, 0, 0),
                    (0x00040001, 0x01000003, 0x57530900, 1, 0),
                    (0x04000100, 0x00000301, 0x57530900, 2, 0),
                    (0x00010004, 0x00030100, 0x57530900, 3, 0))
        for piece in pieces().values():
            self.assertEqual(connections.rul1_rows(piece), expected)
        self.assertEqual(connections.solution_rows(pieces().values()), expected)
        self.assertEqual(len({row[:2] for row in expected}), 4)
        self.assertTrue(all(target == 0x57530900 and flip == 0 for _, _, target, _, flip in expected))
        accepted = {row[:2] for row in expected}
        self.assertNotIn((0, 0x03010000), accepted)
        self.assertNotIn((0x01000400, 0x02000200), accepted)
        self.assertNotIn((0x01000400, 0x00000301), accepted)

    def test_metadata_results_are_independent_copies(self):
        piece = next(iter(pieces().values()))
        first = connections.approaches(piece)
        first[0]['cell'][0] = 123
        self.assertEqual(connections.approaches(piece)[0]['cell'], [-1, 2])

    def test_native_through_spines_independently_fix_helper_flag_and_pose(self):
        from scp_highway.native import rotate_route
        from scp_highway.ramp_verify import _road_word
        from scp_highway.ramp_paths import _route_metadata, construction_flags
        # Numeric endpoints of the four real car routes in native57530900;
        # the two explicitly invalid capacity paths are not through traffic.
        routes = [
            {'transport': 1, 'lane': 0, 'entry': 3, 'exit': 2,
             'points': [(3.2, -8., 15.), (8., -3.2, 15.)]},
            {'transport': 1, 'lane': 1, 'entry': 3, 'exit': 2,
             'points': [(-3.2, -8., 15.), (8., 3.2, 15.)]},
            {'transport': 1, 'lane': 0, 'entry': 2, 'exit': 3,
             'points': [(8., 3.2, 7.5), (-3.2, -8., 7.5)]},
            {'transport': 1, 'lane': 1, 'entry': 2, 'exit': 3,
             'points': [(8., -3.2, 7.5), (3.2, -8., 7.5)]},
        ]
        marker = 0x01000400
        for quarter, row in enumerate(connections.SOLUTIONS):
            rotated = [rotate_route(route, quarter) for route in routes]
            self.assertEqual(_road_word(rotated), row[1])
            self.assertEqual(construction_flags([_route_metadata(route, 'native') for route in rotated]), row[1])
            self.assertEqual(row[0], marker)
            self.assertEqual(row[3:], (quarter, 0))
            marker = ((marker << 8) | (marker >> 24)) & 0xffffffff

    def test_padding_and_optional_cells_round_trip_every_legacy_field(self):
        for piece in pieces().values():
            with self.subTest(piece=piece['id']):
                old, new = extended(piece)
                self.assertEqual(connections.check_construction_approaches(new, piece), old)
                self.assertEqual(new['AutoTileBase'], old['AutoTileBase'])
                self.assertEqual(new['Piece'], old['Piece'])
                self.assertEqual(sum(row.count('+') for row in new['ConsLayout']), len(piece['cells']))
                self.assertEqual(len(new['CheckType']) - len(old['CheckType']),
                                 len(connections.approaches(piece)))

    def test_saved_rule_writer_keeps_actual_auto_tile_addresses_and_preview(self):
        for piece in pieces().values():
            old = legacy_fields(piece)
            text = recipes.construction(piece, old['CellLayout'], old['CheckType'], old['ConsLayout'])
            _, rules = parse_rules(text)
            fields = {}
            for key, value in rules[int(piece['puzzle_id'], 16)]:
                fields.setdefault(key, []).append(value)
            # The independent address checker must see the real static IDs;
            # adaptive cells are static in this deliberately small fixture.
            fixture_piece = {key: value for key, value in piece.items() if key != 'adaptive_ground'}
            report = check_emitted_runtime_addresses(fields, fixture_piece)
            self.assertEqual(report['wrong_model_selections'], 0)
            self.assertEqual(report['cells_checked'], len(piece['cells']))
            self.assertEqual(fields['AutoTileBase'], [f'0x{BASES[piece["id"]]:08X}'])
            self.assertEqual(int(fields['Piece'][0].split(',')[-1], 16), int(piece['preview_id'], 16))

    def test_actual_approach_mutations_fail_before_legacy_checks(self):
        piece = pieces()['ddrhw-modular-highway-stamp']
        _, original = extended(piece)
        mutations = []
        changed = deepcopy(original); changed['CheckType'][-1] = changed['CheckType'][-1].replace('03010000', '00000301'); mutations.append(changed)
        changed = deepcopy(original); changed['CheckType'][-1] = changed['CheckType'][-1].replace(' optional', ''); mutations.append(changed)
        changed = deepcopy(original); changed['CheckType'][-1] = changed['CheckType'][-1].replace('01000400', '00000000'); mutations.append(changed)
        changed = deepcopy(original); changed['ConsLayout'][0] = changed['ConsLayout'][0].replace('.', '+', 1); mutations.append(changed)
        changed = deepcopy(original); changed['CellLayout'][0] = changed['CellLayout'][0].replace('X', '.'); changed['CellLayout'][0] = '.' * len(changed['CellLayout'][0]); mutations.append(changed)
        changed = deepcopy(original); changed['CellLayout'][1] = changed['CellLayout'][1].replace('<', '.'); mutations.append(changed)
        changed = deepcopy(original); changed['CheckType'].append(changed['CheckType'][-1]); mutations.append(changed)
        for index, changed in enumerate(mutations):
            with self.subTest(index=index), self.assertRaises(ValueError):
                connections.check_construction_approaches(changed, piece)

    def test_writer_rejects_a_helper_over_an_existing_check_cell(self):
        piece = next(iter(pieces().values()))
        old = legacy_fields(piece)
        # An origin shifted right makes the nominal outside cell overlap an
        # existing cell; the helper must never overwrite that construction.
        old['CellLayout'][-1] = '.^' + old['CellLayout'][-1][2:]
        with self.assertRaises(ValueError):
            connections.add_approaches(piece, old['CellLayout'], old['CheckType'], old['ConsLayout'])

    def test_all_three_registered_plans_are_collision_free_in_four_global_rotations(self):
        for suffix in ('diamond', 'modular-diamond', 'parallel-diamond'):
            path = ROOT / ('domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-'
                           + suffix + '/assembly.jsonc')
            scene = jsonc.load(path)
            selected = {pose['piece_id']: jsonc.load(ROOT / 'domains/highway/00_pieces'
                        / pose['piece_id'] / 'piece.jsonc') for pose in scene['placements']}
            for quarter in range(4):
                rotated = deepcopy(scene)
                for pose in rotated['placements']:
                    east, north = pose['origin_m']
                    for _ in range(quarter):
                        east, north = -north, east
                    pose['origin_m'] = [east, north]
                    pose['rotation_degrees_ccw'] += 90 * quarter
                with self.subTest(assembly=suffix, quarter=quarter):
                    report = connections.check_helper_collisions(selected, rotated)
                    self.assertEqual(report['outside_approaches_checked'], 2)

    def test_helper_over_another_piece_or_repeated_helper_is_rejected(self):
        selected = pieces(); piece = selected['ddrhw-parallel-upper-exit-slip']
        blocked = {'id': 'blocked', 'cells': [[0, 0]]}
        scene = {'placements': [{'piece_id': piece['id'], 'origin_m': [0, 0]},
                                {'piece_id': 'blocked', 'origin_m': [-16, -16]}]}
        with self.assertRaisesRegex(ValueError, 'overlaps another'):
            connections.check_helper_collisions({piece['id']: piece, 'blocked': blocked}, scene)
        scene['placements'][1] = {'piece_id': piece['id'], 'origin_m': [0, 0]}
        with self.assertRaisesRegex(ValueError, 'duplicates custom'):
            connections.check_helper_collisions({piece['id']: piece}, scene)

    def test_legacy_assembly_report_has_no_new_opt_in_claim(self):
        piece = deepcopy(next(iter(pieces().values())))
        piece.pop('native_dd_approaches')
        scene = {'placements': [{'piece_id': piece['id'], 'origin_m': [0, 0]}]}
        self.assertIsNone(connections.check_selected_helper_collisions({piece['id']: piece}, scene))
        piece['native_dd_approaches'] = True
        result = connections.check_selected_helper_collisions({piece['id']: piece}, scene)
        self.assertEqual(result['outside_approaches_checked'], 1)
        self.assertIs(result['game_behavior_tested'], False)


if __name__ == '__main__':
    unittest.main()
