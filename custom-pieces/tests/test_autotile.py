"""Runtime address regressions, independent of donors, catalog, and geometry."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file()) / 'framework'))

from scp.autotile import (
    AutoTileAddressError, engine_grid_key, game_tile_id,
    resolve_game_tile_ids, validate_auto_tile_addresses,
)


def allocation(base=0x7f508000, footprint=(37, 16), cells=None):
    placements = cells if cells is not None else [
        [x, y] for y in range(footprint[1]) for x in range(footprint[0])]
    piece = {'id': 'address-fixture', 'footprint': list(footprint),
             'tile_ids': [f'{base + (x << 8) + (y << 4):08x}' for x, y in placements]}
    if cells is not None:
        piece['cells'] = deepcopy(cells)
    return piece


class AutoTileTests(unittest.TestCase):
    def rejected(self, piece, message):
        with self.assertRaisesRegex(AutoTileAddressError, message) as caught:
            validate_auto_tile_addresses(piece)
        self.assertFalse(caught.exception.report['valid'])
        return caught.exception.report

    def test_base_plus_offset_uses_addition_even_when_base_bits_overlap(self):
        self.assertEqual(0x7f503000 + (25 << 8) + (4 << 4), 0x7f504940)
        self.assertEqual(game_tile_id(0x7f503000, 25, 4), 0x7f504940)
        self.assertNotEqual(game_tile_id(0x7f503000, 25, 4),
                            game_tile_id(0x7f503000, 9, 4))
        self.assertEqual(game_tile_id(0x7f508000, 25, 4), 0x7f509940)

    def test_different_bases_cannot_resolve_runtime_key_collisions(self):
        cells = [[0, 0], [19, 4], [20, 4], [3, 5], [4, 5]]
        for base in (0x7f503000, 0x7f508000):
            with self.subTest(base=f'{base:08x}'):
                report = self.rejected(allocation(base, (21, 6), cells), '2 allocated tile IDs')
                self.assertEqual(report['base'], f'{base:08x}')
                self.assertEqual(len(report['mismatches']), 2)
                self.assertEqual(len(report['engine_key_collisions']), 2)
                self.assertEqual(len({item['key'] for item in report['engine_grid_keys']}), 3)
                self.assertIn({'cell': [19, 4], 'allocated': f'{base + 0x1340:08x}',
                               'runtime': f'{base + 0x350:08x}'}, report['mismatches'])
                self.assertIn({'cell': [19, 4], 'key': '54', 'selected_cell': [3, 5],
                               'runtime': f'{base + 0x350:08x}'}, report['engine_grid_keys'])
                self.assertEqual(resolve_game_tile_ids(base, cells)[19, 4], base + 0x350)
                self.assertTrue(report['runtime_collisions'])

    def test_full_16_by_16_grid_covers_every_cell_and_all_five_zooms(self):
        report = validate_auto_tile_addresses(allocation(footprint=(16, 16)))
        self.assertTrue(report['valid'])
        self.assertEqual(report['cell_count'], 16 * 16)
        self.assertEqual(report['column_mask'], '00000f00')
        self.assertEqual(report['row_mask'], '000000f0')
        self.assertEqual(report['base_coordinate_overlap'], '00000000')
        self.assertEqual(len({item['key'] for item in report['engine_grid_keys']}), 256)
        self.assertIn({'cell': [15, 15], 'key': '00', 'selected_cell': [15, 15],
                       'runtime': '7f508ff0'}, report['engine_grid_keys'])
        for key in ('mismatches', 'runtime_collisions', 'zoom_collisions',
                    'engine_key_collisions', 'allocation_collisions'):
            self.assertEqual(report[key], [])

    def test_sparse_first_cell_and_integer_ids_infer_the_same_base(self):
        piece = allocation(cells=[[25, 4], [0, 15], [36, 0]])
        piece['tile_ids'] = [int(value, 16) for value in piece['tile_ids']]
        self.assertEqual(validate_auto_tile_addresses(piece)['base'], '7f508000')

    def test_unused_reserved_coordinates_do_not_require_clear_base_bits(self):
        piece = allocation(0x7f503000, cells=[[0, 0]])
        report = validate_auto_tile_addresses(piece)
        self.assertTrue(report['valid'])
        self.assertEqual(report['base_coordinate_overlap'], '00003000')
        self.assertEqual(report['mismatches'], [])

    def test_full_width_37_by_16_grid_is_rejected_despite_clear_base_bits(self):
        report = self.rejected(allocation(), 'engine byte keys alias')
        self.assertEqual(report['base_coordinate_overlap'], '00000000')
        self.assertTrue(report['mismatches'])

    def test_row_wrap_can_duplicate_allocations_and_runtime_keys(self):
        piece = allocation(0x7f508000, (2, 17), [[0, 0], [1, 0], [0, 16]])
        report = self.rejected(piece, 'engine byte keys alias')
        self.assertEqual(report['coordinate_field_overlap'], '00000100')
        self.assertEqual(len(report['runtime_collisions']), 2)
        self.assertEqual(len(report['allocation_collisions']), 1)

    def test_column_carry_collides_with_next_row_instead_of_wrapping_column(self):
        cells = [[0, 0], [16, 0], [0, 1]]
        self.assertEqual(engine_grid_key(16, 0), engine_grid_key(0, 1))
        self.assertNotEqual(engine_grid_key(16, 0), engine_grid_key(0, 0))
        resolved = resolve_game_tile_ids(0x7f508000, cells)
        self.assertEqual(resolved[16, 0], 0x7f508010)
        self.assertEqual(resolved[0, 0], 0x7f508000)

    def test_collision_winner_is_last_row_major_cell_despite_input_order(self):
        cells = [[0, 1], [16, 0], [0, 0]]
        self.assertEqual(resolve_game_tile_ids(0, cells)[16, 0], 0x10)
        self.assertEqual(resolve_game_tile_ids(0, cells),
                         resolve_game_tile_ids(0, list(reversed(cells))))

    def test_wide_sparse_grid_with_unique_keys_is_supported(self):
        cells = [[x, 0] for x in range(37)]
        report = validate_auto_tile_addresses(allocation(0x7f503000, (37, 16), cells))
        self.assertTrue(report['valid'])
        self.assertEqual(len({item['key'] for item in report['engine_grid_keys']}), 37)
        self.assertEqual(resolve_game_tile_ids(0x7f503000, cells)[36, 0], 0x7f505400)

    def test_modeled_bounding_box_origin_is_subtracted_by_runtime_lookup(self):
        resolved = resolve_game_tile_ids(0x7f508000, [[20, 5], [21, 5], [20, 6]])
        self.assertEqual(resolved, {(20, 5): 0x7f508000, (21, 5): 0x7f508100,
                                    (20, 6): 0x7f508010})
        report = validate_auto_tile_addresses(allocation(cells=[[20, 5], [21, 5], [20, 6]]))
        self.assertEqual(report['engine_origin'], [20, 5])
        self.assertEqual(report['base'], '7f509450')
        self.assertTrue(report['valid'])
        self.assertEqual(resolve_game_tile_ids(int(report['base'], 16),
                                              [[20, 5], [21, 5], [20, 6]])[20, 5],
                         0x7f509450)

    def test_nonzero_bbox_base_inference_does_not_depend_on_first_cell_order(self):
        piece = allocation(cells=[[21, 6], [20, 5], [21, 5]])
        self.assertEqual(validate_auto_tile_addresses(piece)['base'], '7f509450')

    def test_large_sparse_footprint_does_not_materialize_reserved_cells(self):
        report = validate_auto_tile_addresses(allocation(0, (0xffffffff, 0xffffffff), [[0, 0]]))
        self.assertTrue(report['valid'])
        self.assertEqual(report['cell_count'], 1)

    def test_duplicate_placements_and_duplicate_allocations_are_rejected(self):
        self.rejected(allocation(cells=[[0, 0], [0, 0]]), 'duplicate placements')
        piece = allocation(cells=[[0, 0], [1, 0]])
        piece['tile_ids'][1] = piece['tile_ids'][0]
        report = self.rejected(piece, 'allocated zoom resources collide')
        self.assertEqual(len(report['mismatches']), 1)
        self.assertEqual(len(report['zoom_collisions']), 5)
        self.assertEqual(len(report['allocation_collisions']), 1)

    def test_low_zoom_bits_and_zoom_overflow_are_rejected(self):
        self.rejected(allocation(0x7f508001, (1, 1)), 'low four zoom bits clear')
        report = self.rejected({'footprint': [1, 1], 'tile_ids': [0xfffffffe]},
                               'zoom IDs exceed unsigned 32-bit')
        self.assertIn('base and tile IDs must leave the low four zoom bits clear', report['errors'])

    def test_uint32_boundary_and_maximum_safe_coordinate(self):
        self.assertEqual(game_tile_id(0xfffffff0, 0, 0), 0xfffffff0)
        self.assertTrue(validate_auto_tile_addresses(allocation(0xfffffff0, (1, 1)))['valid'])
        self.assertEqual(game_tile_id(0, 0xffffff, 0), 0xffffff00)
        for args in ((-1, 0, 0), (0x100000000, 0, 0), (0, -1, 0),
                     (0, 0, -1), (0, 0x1000000, 0), (0, 0, 0x10000000),
                     (True, 0, 0), (0, False, 0), (0, 0, 1.0), ('7f508000', 0, 0),
                     (0xfffffff0, 1, 0), (0xfffffff0, 0, 1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                game_tile_id(*args)

    def test_direct_resolver_and_key_helpers_reject_malformed_inputs(self):
        for cells in (None, [], '0,0', [[0]], [[False, 0]], [[-1, 0]],
                      [[0, 0], [0, 0]], [[0x100000000, 0]]):
            with self.subTest(cells=cells), self.assertRaises(ValueError):
                resolve_game_tile_ids(0, cells)
        for args in ((False, 0), (-1, 0), (0, 1.0), (0x100000000, 0)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                engine_grid_key(*args)
        with self.assertRaises(ValueError):
            resolve_game_tile_ids(0xfffffff0, [[0, 0], [1, 0]])

    def test_invalid_shapes_and_ids_fail_with_diagnostic_reports(self):
        bad_pieces = [None, {}, {'footprint': [0, 1]}, {'footprint': [True, 1]},
            {'footprint': [0x1000001, 1]}, {'footprint': [1, 1], 'tile_ids': []},
            {'footprint': [1, 1], 'tile_ids': ['0x7f508000']},
            {'footprint': [1, 1], 'tile_ids': [True]},
            {'footprint': [1, 1], 'tile_ids': [0x100000000]},
            {'footprint': [1, 1], 'tile_ids': ['7f508000'], 'cells': [[1, 0]]},
            {'footprint': [1, 1], 'tile_ids': ['7f508000'], 'cells': [[False, 0]]},
            {'footprint': [1, 1], 'tile_ids': ['7f508000'], 'cells': [[0]]},
            {'footprint': [1, 1], 'tile_ids': ['7f508000'], 'cells': '0,0'}]
        for piece in bad_pieces:
            with self.subTest(piece=piece):
                self.rejected(piece, 'unsafe auto-tile addresses')


if __name__ == '__main__':
    unittest.main()
