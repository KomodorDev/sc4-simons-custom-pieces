"""Check removable FLEX handles without changing permanent tile ownership."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import adaptive_network, jsonc
from scp.verify import check_emitted_runtime_addresses, parse_rules
from scp_highway import adaptive_ground, adaptive_verify
from scp_highway.native import encode_paths


RUL0 = b'[Ordering]\r\nRotationRing=1000,11000\r\n'
RUL1 = (b'[StreetAvenueIntersectionSolutions]\r\n'
        b'TYPE1=0x00000002,0x03010000,0x04004500,0,0\r\n[Next]\r\n')


def crossing():
    """Literal sparse three-cell fixture in a reviewed native Avenue corridor."""
    cells = [[0, 0], [1, 0], [0, 1]]
    rows = []
    for index, cell in enumerate(cells):
        difference = cell[0] - cell[1]
        rows.append({'cell': cell[:], 'resolved_tile_id': f'{0x7f5a0000 + 256 * index:08x}',
                     'rotation': 2 if difference == 1 else 0,
                     'texture_donor_id': '04003800' if difference == 0 else '04000200',
                     'street_flags': f'{0x02020404 + 0x10000 * index:08x}',
                     'avenue_flags': {0: '01030103', 1: '01000003', -1: '00030100'}[difference],
                     'prop': True})
    return {'id': 'small-adaptive-fixture', 'name': 'Small adaptive fixture',
            'geometry_key': 'access-core', 'footprint': [2, 2], 'cells': cells,
            'tile_ids': [f'{0x7f580000 + 256 * index:08x}' for index in range(3)],
            'puzzle_id': '7f600000', 'preview_id': '7f580ff5', 'effect_name': 'fixture_effect',
            'adaptive_ground': {'schema_version': 1, 'cells': rows,
                                'construction_helper': [1, 1]}}


def compiled(piece):
    raw = encode_paths([dict(transport=1, lane=1, entry=0, exit=2, compatibility=0,
                             points=[(-8.0, 0.0, 7.5), (8.0, 0.0, 7.5)])])
    return [(tuple(cell), b'construction does not inspect model buffers', raw)
            for cell in piece['cells']]


def emitted(piece):
    result = adaptive_ground.build_construction(piece, compiled(piece), RUL0, RUL1)
    _rings, rules = parse_rules(result['rul0'])
    fields = {}
    for key, value in rules[int(piece['puzzle_id'], 16)]:
        fields.setdefault(key, []).append(value)
    return result, rules, fields


class AdaptiveConstructionHelperTests(unittest.TestCase):
    def test_internal_corner_is_the_only_removable_cell_and_never_a_permanent_resource(self):
        piece = crossing()
        original = deepcopy(piece)
        legacy = deepcopy(piece)
        del legacy['adaptive_ground']['construction_helper']
        self.assertEqual(adaptive_network.construction_helper(piece), (1, 1))
        self.assertEqual(adaptive_network.fixed_cells(piece), [])
        self.assertEqual(adaptive_network.resource_keys(piece), adaptive_network.resource_keys(legacy))
        _raw, _rules, fields = emitted(piece)
        self.assertEqual(fields['CellLayout'], ['ab.<', 'cZ..', '^...'])
        self.assertEqual(fields['ConsLayout'], ['...<', '.+..', '^...'])
        self.assertEqual(fields['CheckType'][-1], 'Z - road: 0x02000200')
        self.assertEqual(sum('optional' in value for value in fields['CheckType']), 3)
        report = check_emitted_runtime_addresses(fields, piece)
        self.assertEqual(report['cells_checked'], 1)
        self.assertEqual(report['modeled_origin'], [1, 1])
        self.assertEqual(report['wrong_model_selections'], 0)
        independent = adaptive_verify.check_construction_fields(fields, piece, {})
        self.assertEqual(independent['static_cells_checked'], 0)
        self.assertTrue(independent['temporary_handle_required'])
        self.assertFalse(independent['game_behavior_tested'])
        self.assertEqual(piece, original)

    def test_four_native_rotations_keep_the_helper_disjoint_from_every_real_cell(self):
        piece = crossing()
        raw, rules, fields = emitted(piece)
        root = int(piece['puzzle_id'], 16)
        rings, _unused = parse_rules(raw['rul0'])
        self.assertEqual(rings, [[root + 0x10000 * turn for turn in range(8)]])
        for turn in range(4):
            with self.subTest(turn=turn):
                if turn:
                    self.assertEqual(rules[root + 0x10000 * turn],
                                     [('CopyFrom', f'0x{root:X}'), ('Rotate', str(turn))])
                self.assertEqual(rules[root + 0x10000 * (turn + 4)],
                                 [('CopyFrom', f'0x{root + 0x10000 * turn:X}')])
                def rotate(cell):
                    x, y = cell
                    for _ in range(turn):
                        x, y = 1 - y, x
                    return x, y
                real = {rotate(cell) for cell in piece['cells']}
                helper = rotate(adaptive_network.construction_helper(piece))
                self.assertEqual(len(real), 3)
                self.assertNotIn(helper, real)
                self.assertEqual(real | {helper}, {(0, 0), (1, 0), (0, 1), (1, 1)})
                self.assertEqual(check_emitted_runtime_addresses(fields, piece)['wrong_model_selections'], 0)

    def test_explicit_external_handle_supports_a_single_adaptive_cell(self):
        piece = crossing()
        piece['footprint'] = [1, 1]
        piece['cells'] = piece['cells'][:1]
        piece['tile_ids'] = piece['tile_ids'][:1]
        piece['adaptive_ground']['cells'] = piece['adaptive_ground']['cells'][:1]
        piece['adaptive_ground']['construction_helper'] = [1, 0]
        _raw, _rules, fields = emitted(piece)
        self.assertEqual(fields['CellLayout'], ['aZ<', '^..'])
        self.assertEqual(adaptive_network.fixed_cells(piece), [])
        self.assertEqual(check_emitted_runtime_addresses(fields, piece)['modeled_origin'], [1, 0])
        self.assertEqual(adaptive_verify.check_construction_fields(fields, piece, {})['static_cells_checked'], 0)

    def test_legacy_handle_is_unchanged_without_the_opt_in(self):
        path = ROOT / 'domains/highway/00_pieces/ddrhw-diagonal-access-core/piece.jsonc'
        piece = jsonc.load(path)
        self.assertNotIn('construction_helper', piece['adaptive_ground'])
        default, _rules, fields = emitted(piece)
        explicit = deepcopy(piece)
        explicit['adaptive_ground']['construction_helper'] = [3, 0]
        specified, _rules, _fields = emitted(explicit)
        self.assertEqual(default, specified)
        self.assertEqual(adaptive_network.construction_helper(piece), (3, 0))
        self.assertIn('.a.Z<', fields['CellLayout'])
        self.assertEqual(check_emitted_runtime_addresses(fields, piece)['modeled_origin'], [3, 0])

    def test_invalid_coordinates_and_overlap_are_rejected_before_emission(self):
        for value in ([True, 1], [1.0, 1], [1], '1,1', None, [-1, 1],
                      [3, 1], [1, 2], [0, 0], [1, 0], [0, 1]):
            with self.subTest(value=value):
                piece = crossing()
                piece['adaptive_ground']['construction_helper'] = value
                with self.assertRaisesRegex(ValueError, 'construction helper'):
                    adaptive_network.bindings(piece)

    def test_hybrid_piece_rejects_an_unnecessary_helper(self):
        piece = crossing()
        piece['adaptive_ground']['cells'].pop()
        with self.assertRaisesRegex(ValueError, 'entirely adaptive'):
            adaptive_network.bindings(piece)
        del piece['adaptive_ground']['construction_helper']
        self.assertIsNone(adaptive_network.construction_helper(piece))

    def test_saved_address_checker_rejects_wrong_extra_missing_and_nonroad_handles(self):
        piece = crossing()
        _raw, _rules, fields = emitted(piece)
        controls = []
        changed = deepcopy(fields)
        changed['CellLayout'][1] = 'c.Z.'
        controls.append(changed)
        changed = deepcopy(fields)
        changed['CellLayout'][0] = 'abZ<'
        controls.append(changed)
        changed = deepcopy(fields)
        changed['CellLayout'][1] = 'c...'
        controls.append(changed)
        for check in ('Z - road: 0x02000202', 'Z - dirtroad: 0x02000200',
                      'Z - road: 0x02000200 optional'):
            changed = deepcopy(fields)
            changed['CheckType'][-1] = check
            controls.append(changed)
        for changed in controls:
            with self.subTest(fields=changed):
                with self.assertRaises(ValueError):
                    check_emitted_runtime_addresses(changed, piece)
                with self.assertRaises(ValueError):
                    adaptive_verify.check_construction_fields(changed, piece, {})

    def test_independent_checker_rejects_changed_helper_constraint(self):
        piece = crossing()
        _raw, _rules, fields = emitted(piece)
        fields['ConsLayout'][1] = '....'
        with self.assertRaisesRegex(ValueError, 'tile ownership'):
            adaptive_verify.check_construction_fields(fields, piece, {})


if __name__ == '__main__':
    unittest.main()
