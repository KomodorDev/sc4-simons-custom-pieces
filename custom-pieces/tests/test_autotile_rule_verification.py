"""Hand-authored emitted grids must match the executable's byte-key lookup."""
from copy import deepcopy
from pathlib import Path
import hashlib
import sys
import unittest

sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file()) / 'framework'))
from scp.verify import check_construction, check_emitted_runtime_addresses, RUL0


def fixture(cells, footprint, tile_ids, rows, checks, base):
    """Wrap literal test tables; no production rule writer is used."""
    piece = {'id': 'emitted-address-fixture', 'recipe': 'unimplemented',
             'puzzle_id': 'f8fe', 'tile_ids': tile_ids,
             'preview_id': '7f51fff5', 'effect_name': 'address_fixture',
             'footprint': footprint, 'cells': cells}
    fields = {'Piece': ['0,0,0,0,0x7F51FFF5'], 'PreviewEffect': ['address_fixture'],
              'CellLayout': rows, 'CheckType': checks,
              'ConsLayout': [row for row in rows],
              'AutoTileBase': [f'0x{base:08X}'], 'ReplacementIntersection': ['0,0'],
              'PlaceQueryID': [f'0x{int(tile_ids[0], 16):08X}'], 'Costs': ['1']}
    return piece, fields


class RuntimeRuleAddressTests(unittest.TestCase):
    def test_emitted_rule_rejects_byte_key_collision_with_old_and_aligned_base(self):
        # (16,0) and (0,1) both encode byte key 0x11. The later row wins.
        for base, ids in ((0x7f503000, ['7f504000', '7f503010']),
                          (0x7f508000, ['7f509000', '7f508010'])):
            with self.subTest(base=hex(base)):
                piece, fields = fixture([[16, 0], [0, 1]], [17, 2], ids,
                    ['................a<', 'b................', '^................'],
                    ['a - monorail: 0', 'b - monorail: 0'], base)
                fields['ConsLayout'] = ['................+<', '+................', '^................']
                root = 0xf8fe
                states = [root+index*0x10000 for index in range(8)]
                insertion = 'RotationRing = '+', '.join(f'0x{state:08X}' for state in states)+'\n'
                text = f'[HighwayIntersectionInfo_0x{root:08X}]\n'
                text += ''.join(f'{key}={value}\n' for key, values in fields.items() for value in values)
                for state in states[1:]:
                    text += f'[HighwayIntersectionInfo_0x{state:08X}]\nCopyFrom=0x{root:08X}\n'
                native = b'[Ordering]\n[HighwayIntersectionInfo_0x0000C200]\n'
                actual = native.replace(b'[Ordering]\n',
                    b'[Ordering]\n'+insertion.encode(),1)+text.encode()
                manifest = {'overlay': {'rul0': {'suffix': text,
                    'ordering_insertion': insertion,
                    'base_sha256': hashlib.sha256(native).hexdigest()}}}
                with self.assertRaisesRegex(ValueError, 'byte-key collision: 1 cells select the wrong cell models'):
                    check_construction({RUL0: actual}, [piece], manifest, None)

    def test_safe_literal_two_by_two_grid_uses_addition(self):
        # Base bits overlap the column offset. OR would give different IDs.
        piece, fields = fixture([[0, 0], [1, 0], [0, 1], [1, 1]], [2, 2],
            ['7f508100', '7f508200', '7f508110', '7f508210'],
            ['ab<', 'cd.', '^..'],
            [f'{symbol} - monorail: 0' for symbol in 'abcd'], 0x7f508100)
        report = check_emitted_runtime_addresses(fields, piece)
        self.assertEqual(report['cells_checked'], 4)
        self.assertEqual(report['unique_byte_keys'], 4)
        self.assertEqual(report['wrong_model_selections'], 0)

    def test_sparse_seventeen_column_grid_with_unique_keys_is_allowed(self):
        # Keys are 0x01, 0x11, 0x12: no physical (0,1) cell shares key0x11.
        piece, fields = fixture([[0, 0], [16, 0], [1, 1]], [17, 2],
            ['7f508000', '7f509000', '7f508110'],
            ['a...............b<', '.c...............', '^................'],
            [f'{symbol} - monorail: 0' for symbol in 'abc'], 0x7f508000)
        report = check_emitted_runtime_addresses(fields, piece)
        self.assertEqual(report['unique_byte_keys'], 3)

    def test_key_zero_at_far_corner_is_a_valid_lookup(self):
        piece, fields = fixture([[0, 0], [15, 15]], [16, 16],
            ['7f508000', '7f508ff0'],
            ['a...............<', *['.................']*14,
             '...............b.', '^................'],
            ['a - monorail: 0', 'b - monorail: 0'], 0x7f508000)
        self.assertEqual(check_emitted_runtime_addresses(fields, piece)['unique_byte_keys'], 2)

    def test_check_and_optional_border_cells_do_not_shift_modeled_origin(self):
        piece, fields = fixture([[0, 0], [1, 0], [0, 1], [1, 1]], [2, 2],
            ['7f508000', '7f508100', '7f508010', '7f508110'],
            ['c..o..', '...ab<', '...de.', '...^..'],
            ['c - monorail: 0, 0xffffffff check',
             'o - monorail: 0, 0xffffffff optional',
             *[f'{symbol} - monorail: 0' for symbol in 'abde']], 0x7f508000)
        report = check_emitted_runtime_addresses(fields, piece)
        self.assertEqual(report['cells_checked'], 4)
        self.assertEqual(report['modeled_origin'], [0, 0])

    def test_nonzero_modeled_origin_requires_adjusted_emitted_base(self):
        piece, fields = fixture([[2, 0], [2, 1], [1, 2], [2, 2]], [3, 3],
            ['7f508200', '7f508210', '7f508120', '7f508220'],
            ['..a<', '..b.', '.cd.', '^...'],
            [f'{symbol} - monorail: 0' for symbol in 'abcd'], 0x7f508100)
        report = check_emitted_runtime_addresses(fields, piece)
        self.assertEqual(report['modeled_origin'], [1, 0])
        fields['AutoTileBase'] = ['0x7f508000']
        with self.assertRaisesRegex(ValueError, r'modeled-origin normalization \(4 cells\)'):
            check_emitted_runtime_addresses(fields, piece)

    def test_emitted_cells_are_checked_instead_of_trusting_manifest(self):
        piece, fields = fixture([[0, 0], [1, 0]], [2, 1],
            ['7f508000', '7f508100'], ['ab<', '^..'],
            ['a - monorail: 0', 'b - monorail: 0'], 0x7f508000)
        changed = deepcopy(fields)
        changed['CheckType'][1] += ' optional'
        with self.assertRaisesRegex(ValueError, 'emitted modeled cells differ'):
            check_emitted_runtime_addresses(changed, piece)

    def test_literal_plus_cell_is_modeled_without_a_palette_entry(self):
        piece, fields = fixture([[0, 0]], [1, 1], ['7f508000'],
            ['+<', '^.'], [], 0x7f508000)
        report = check_emitted_runtime_addresses(fields, piece)
        self.assertEqual(report['unique_byte_keys'], 1)


if __name__ == '__main__':
    unittest.main()
