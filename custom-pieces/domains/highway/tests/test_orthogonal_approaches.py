"""Independent controls for the three reviewed orthogonal native sockets."""
from copy import deepcopy
import hashlib
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))

from scp import jsonc
from scp.dbpf import entries, decompress, exemplar
from scp.paths import local_settings
from scp.verify import parse_paths
from scp_highway import orthogonal_approaches as approaches


def specification():
    cells = [[column, row] for row in range(6) for column in range(2)]
    return {'id': 'ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile',
            'recipe': 'highway_ddrhw_orthogonal_l0_transition', 'domain': 'highway',
            'footprint': [2, 6], 'cells': cells,
            'tile_ids': [f'{0x7F600000 + 0x100 * column + 0x10 * row:08x}' for column, row in cells],
            'native_orthogonal_approaches': True}


def core_fields():
    return {'CellLayout': ['ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', '^...'],
            'ConsLayout': ['++.<', '++..', '++..', '++..', '++..', '++..', '^...'],
            'CheckType': [f'{symbol} - dirtroad: 0x02000200' for symbol in 'abcdefghijkl'],
            'AutoTileBase': ['0x7F600000'], 'Piece': ['0.0, 0.0, 0, 0, 0x7F600F00'],
            'Costs': ['1000'], 'ReplacementIntersection': ['0, 0']}


def padded_fields():
    old = core_fields()
    rows, checks, cons = approaches.add_approaches(specification(), old['CellLayout'],
                                                 old['CheckType'], old['ConsLayout'])
    return {**old, 'CellLayout': rows, 'CheckType': checks, 'ConsLayout': cons}


class OrthogonalApproachTests(unittest.TestCase):
    def test_three_end_bindings_use_actual_allocated_cells_and_complementary_poses(self):
        rows = approaches.approaches(specification())
        self.assertEqual([(row['cell'], row['end_cell'], row['end_tile_id'], row['outward_edge'],
                           row['native_tile_id'], row['native_rotation']) for row in rows], [
            ([1, -1], [1, 0], '7f600100', 1, '57530000', 0),
            ([0, 6], [0, 5], '7f600050', 3, '57030000', 0),
            ([1, 6], [1, 5], '7f600150', 3, '57030000', 2),
        ])
        self.assertEqual([row['networks'] for row in rows], [
            [{'name': 'monorail', 'flags': '01000400'}, {'name': 'dirtroad', 'flags': '02000200'}],
            [{'name': 'road', 'flags': '01000001'}, {'name': 'dirtroad', 'flags': '02000200'}],
            [{'name': 'road', 'flags': '00010100'}, {'name': 'dirtroad', 'flags': '02000200'}],
        ])
        self.assertEqual([row['native_model_reference'] for row in rows], ['rkt0', 'direct', 'direct'])
        self.assertTrue(all(row['optional'] and row['experimental'] for row in rows))
        self.assertTrue(all(row['cell'] not in specification()['cells'] for row in rows))

    def test_absent_and_false_keep_old_construction_unchanged_without_binding_validation(self):
        for piece in ({}, {'native_orthogonal_approaches': False}):
            self.assertEqual(approaches.approaches(piece), [])
            self.assertEqual(approaches.rul1_sections(piece), {})
            self.assertEqual(approaches.existing_rul1_sections(piece), {})
            fields = core_fields()
            self.assertEqual(approaches.add_approaches(piece, fields['CellLayout'], fields['CheckType'],
                                                      fields['ConsLayout']),
                             (fields['CellLayout'], fields['CheckType'], fields['ConsLayout']))
            self.assertEqual(approaches.check_construction_approaches(fields, piece), fields)

    def test_other_registered_highway_pieces_do_not_gain_orthogonal_helpers(self):
        files = list((ROOT / 'domains/highway/00_pieces').glob('*/piece.jsonc'))
        self.assertGreaterEqual(len(files), 38)
        for path in files:
            piece = jsonc.load(path)
            if piece['id'] != specification()['id']:
                with self.subTest(piece=piece['id']):
                    self.assertEqual(approaches.approaches(piece), [])
                    self.assertEqual(approaches.rul1_sections(piece), {})

    def test_truthy_or_falsey_non_booleans_are_rejected(self):
        for value in (1, 0, None, 'true', [], {}):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'exact boolean'):
                approaches.approaches({**specification(), 'native_orthogonal_approaches': value})

    def test_finite_owner_geometry_order_and_modes_fail_closed(self):
        piece = specification()
        changes = [('id', piece['id'] + '-other'), ('recipe', 'highway_another'),
                   ('domain', 'high-speed-rail'), ('footprint', [6, 2]),
                   ('cells', piece['cells'][:-1]), ('cells', list(reversed(piece['cells']))),
                   ('cells', [[False, 0], *piece['cells'][1:]]),
                   ('cells', [piece['cells'][0], *piece['cells'][:-1]]),
                   ('native_dd_approaches', True), ('native_ghsr_approaches', True),
                   ('adaptive_ground', {'network': 'avenue'}), ('tile_ids', piece['tile_ids'][:-1]),
                   ('tile_ids', ['bad', *piece['tile_ids'][1:]]),
                   ('tile_ids', [piece['tile_ids'][0], *piece['tile_ids'][:-1]])]
        for field, value in changes:
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                approaches.approaches({**piece, field: value})

    def test_declared_rows_are_independent_copies_and_bind_to_new_allocation(self):
        piece = specification()
        first = approaches.approaches(piece)
        first[0]['cell'][0] = 90
        first[0]['networks'][0]['flags'] = '00000000'
        self.assertEqual(approaches.approaches(piece)[0]['cell'], [1, -1])
        self.assertEqual(approaches.approaches(piece)[0]['networks'][0]['flags'], '01000400')
        moved = {**piece, 'tile_ids': [f'{int(tile, 16) + 0x1000:08X}' for tile in piece['tile_ids']]}
        self.assertEqual([row['end_tile_id'] for row in approaches.approaches(moved)],
                         ['7f601100', '7f601050', '7f601150'])

    def test_exact_native_rul1_tables_have_eight_rows_without_flips(self):
        expected = {
            'MonoRailDirtRoadIntersectionSolutions': (
                (0x01000400, 0x02000200, 0x57530000, 0, 0),
                (0x00040001, 0x00020002, 0x57530000, 1, 0),
                (0x04000100, 0x02000200, 0x57530000, 2, 0),
                (0x00010004, 0x00020002, 0x57530000, 3, 0)),
            'RoadDirtRoadIntersectionSolutions': (
                (0x01000001, 0x02000200, 0x57030000, 0, 0),
                (0x00000101, 0x00020002, 0x57030000, 1, 0),
                (0x00010100, 0x02000200, 0x57030000, 2, 0),
                (0x01010000, 0x00020002, 0x57030000, 3, 0)),
        }
        self.assertEqual(approaches.rul1_sections(specification()), expected)
        self.assertEqual(approaches.existing_rul1_sections(specification()), expected)

    def test_direct_ground_model_does_not_invent_a_network_exemplar(self):
        pins = approaches.NATIVE_DEPENDENCY_SHA256
        self.assertEqual(len(pins), 5)
        self.assertEqual({key[2] for key in pins}, {0x57530000, 0x57030000})
        self.assertIn((0x6534284A, 0x6BE08658, 0x57530000), pins)
        self.assertFalse(any(key[0] == 0x6534284A and key[2] == 0x57030000 for key in pins))

    def test_padding_preserves_all_fields_and_moves_only_the_caret_row(self):
        old, piece = core_fields(), specification()
        untouched = deepcopy(old)
        new = padded_fields()
        self.assertEqual(old, untouched)
        self.assertEqual(new['CellLayout'], ['.Z..', 'ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', 'YX..', '^...'])
        self.assertEqual(new['ConsLayout'], ['....', '++.<', '++..', '++..', '++..', '++..', '++..', '....', '^...'])
        self.assertEqual(new['CheckType'][-3:], [
            'Z - monorail: 0x01000400 dirtroad: 0x02000200, 0xFFFFFFFF optional',
            'Y - road: 0x01000001 dirtroad: 0x02000200, 0xFFFFFFFF optional',
            'X - road: 0x00010100 dirtroad: 0x02000200, 0xFFFFFFFF optional'])
        self.assertEqual(approaches.check_construction_approaches(new, piece), old)
        self.assertEqual(sum(row.count('+') for row in new['ConsLayout']), 12)

    def test_padding_rejects_existing_cells_and_moved_core_coordinate_origins(self):
        original = core_fields()
        for field, index, value in [('CellLayout', 6, '^.a.'), ('ConsLayout', 6, '^.+.'),
                                    ('CellLayout', 0, 'ab<.'), ('ConsLayout', 6, '.^..'),
                                    ('CellLayout', 1, 'cd...')]:
            changed = deepcopy(original)
            changed[field][index] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                approaches.add_approaches(specification(), changed['CellLayout'], changed['CheckType'], changed['ConsLayout'])

    def test_saved_helper_mutations_are_rejected_before_owned_core_checks(self):
        original = padded_fields()
        mutations = []
        for old, new in [('01000400', '04000100'), ('02000200', '03010000'),
                         (' optional', ''), (', 0xFFFFFFFF', ''), ('monorail:', 'avenue:')]:
            changed = deepcopy(original)
            changed['CheckType'][-3] = changed['CheckType'][-3].replace(old, new)
            mutations.append(changed)
        for field, index, value in [('ConsLayout', 0, '.+..'), ('CellLayout', 0, '....'),
                                    ('CellLayout', 0, '.ZZ.'), ('CellLayout', 7, 'XY..'),
                                    ('CellLayout', 8, '^.a.'), ('CellLayout', 1, 'ab<.'),
                                    ('ConsLayout', 8, '.^..')]:
            changed = deepcopy(original)
            changed[field][index] = value
            mutations.append(changed)
        changed = deepcopy(original); changed['CheckType'].append(changed['CheckType'][-1]); mutations.append(changed)
        changed = deepcopy(original); changed['CellLayout'].append('....'); mutations.append(changed)
        for index, changed in enumerate(mutations):
            with self.subTest(index=index), self.assertRaises(ValueError):
                approaches.check_construction_approaches(changed, specification())

    def test_helper_verifier_leaves_owned_core_and_preview_for_independent_verification(self):
        fields = padded_fields()
        fields['AutoTileBase'] = ['0x11111111']
        fields['Piece'] = ['changed preview']
        fields['CheckType'][0] = 'a - dirtroad: 0x00000000'
        fields['ConsLayout'][1] = '.+.<'
        restored = approaches.check_construction_approaches(fields, specification())
        self.assertEqual(restored['AutoTileBase'], ['0x11111111'])
        self.assertEqual(restored['Piece'], ['changed preview'])
        self.assertEqual(restored['CheckType'][0], 'a - dirtroad: 0x00000000')
        self.assertEqual(restored['ConsLayout'][0], '.+.<')

    def test_unpinned_or_missing_native_rule_resources_are_rejected(self):
        for controller in ({}, {approaches.RUL0: b'foreign rule'},
                           {approaches.RUL0: b'foreign', approaches.RUL1: b'foreign', approaches.RUL2: b'foreign'}):
            with self.subTest(resources=list(controller)), self.assertRaisesRegex(ValueError, 'pinned native'):
                approaches.check_native_continuation(controller)


class ActualNativeOrthogonalContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings_path = local_settings(ROOT)
        if not settings_path.is_file():
            raise unittest.SkipTest('Original NAM 50 inputs are unavailable in this source-only checkout')
        settings = jsonc.load(settings_path)
        roots = [Path(settings['plugins']).expanduser(), *(Path(item).expanduser() for item in settings.get('extra_plugins', []))]
        cls.archives = {}
        for label, filename in (('controller', 'NetworkAddonMod_Controller.dat'),
                                ('dd_rhw', 'RealHighway_DD_RHW-4.dat'), ('rhw4', 'RealHighway_RHW-4.dat')):
            matches = list({path for root in roots if root.is_dir() for path in root.rglob(filename)})
            if len(matches) != 1:
                raise unittest.SkipTest('Exactly one original ' + filename + ' is required for native integration')
            raw = matches[0].read_bytes()
            cls.archives[label] = (raw, {key: decompress(value) for key, value in entries(raw).items()})

    def test_original_starters_solutions_continuations_and_endpoint_bytes(self):
        for label, expected in approaches.NATIVE_ARCHIVE_SHA256.items():
            self.assertEqual(hashlib.sha256(self.archives[label][0]).hexdigest(), expected)
        report = approaches.check_native_continuation(self.archives['controller'][1])
        self.assertEqual(report['native_starters_checked'], 2)
        self.assertEqual(report['existing_native_rul1_solutions_checked'], 8)
        self.assertEqual(report['native_continuation_rows_checked'], 8)
        self.assertTrue(report['native_rul1_unchanged'] and report['native_rul2_unchanged'])
        self.assertFalse(report['game_behavior_tested'])
        for key, expected in approaches.NATIVE_DEPENDENCY_SHA256.items():
            label = 'dd_rhw' if key[2] == 0x57530000 else 'rhw4'
            self.assertEqual(hashlib.sha256(self.archives[label][1][key]).hexdigest(), expected)
        self.assertFalse(any(key[0] == 0x6534284A and key[2] == 0x57030000
                             for _, resources in self.archives.values() for key in resources))
        props = {int(prop['id'], 16): prop['values'] for prop in exemplar(
            self.archives['dd_rhw'][1][0x6534284A, 0x6BE08658, 0x57530000])['properties']}
        self.assertEqual(props[0x10], [11])
        self.assertEqual(props[0x27812820], [0x5AD0E817, 0xBADB57F1, 0x57530000])

    def test_actual_path_directions_and_heights_match_all_three_socket_poses(self):
        from scp_highway.native import rotate_route
        for label, target, pose, expected in [
            ('dd_rhw', 0x57530000, 0, [(1, 3, 15.), (1, 3, 15.), (3, 1, 7.5), (3, 1, 7.5)]),
            ('rhw4', 0x57030000, 0, [(1, 3, 0.), (1, 3, 0.)]),
            ('rhw4', 0x57030000, 2, [(3, 1, 0.), (3, 1, 0.)]),
        ]:
            raw = self.archives[label][1][0x296678F7, 0xA966883F, target]
            routes = [rotate_route(route, pose) for route in parse_paths(raw)['routes']
                      if route['transport'] == 1 and {route['entry'], route['exit']} == {1, 3}]
            with self.subTest(target=hex(target), pose=pose):
                self.assertEqual([(route['entry'], route['exit'], route['points'][0][2]) for route in routes], expected)
                self.assertTrue(all(abs(point[0]) == 2.5 and abs(point[1]) == 8.
                                    for route in routes for point in route['points']))


if __name__ == '__main__':
    unittest.main()
