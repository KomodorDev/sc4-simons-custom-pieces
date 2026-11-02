"""Authoring controls for the second grid phase, without changing alignment A."""
from copy import deepcopy
import hashlib
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.dbpf import decompress, entries
from scp.paths import local_settings
from scp.track_paths import PATH
from scp.verify import parse_paths
from scp_highway import ghsr_approaches as approaches
from scp_highway import ghsr_crossing as author


def specification(alignment_b=True):
    return {'id': approaches.ALIGNMENT_B_PIECE_ID if alignment_b else approaches.PIECE_ID,
            'domain': 'highway',
            'recipe': approaches.ALIGNMENT_B_RECIPE if alignment_b else approaches.RECIPE,
            'footprint': [2, 1] if alignment_b else [1, 2],
            'cells': [[0, 0], [1, 0]] if alignment_b else [[0, 0], [0, 1]],
            'tile_ids': ['7f500000', '7f500010'], 'native_ghsr_approaches': True}


def native_fixture():
    """Literal original route data, separate from either authoring function."""
    def path(transport, lane, entry, exit_, first, last):
        return {'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
                'compatibility': 0, 'points': [first, last]}
    dd = [path(1, 0, 2, 3, (8., 3.2, 15.), (-3.2, -8., 15.)),
          path(1, 1, 2, 3, (8., -3.2, 15.), (3.2, -8., 15.)),
          path(1, 1, 3, 2, (-3.2, -8., 7.5), (8., 3.2, 7.5)),
          path(1, 0, 3, 2, (3.2, -8., 7.5), (8., -3.2, 7.5))]
    dd_second = [path(1, 0, 3, 2, (3.2, -8., 15.), (8., -3.2, 15.)),
                 path(1, 1, 3, 2, (-3.2, -8., 15.), (8., 3.2, 15.)),
                 path(1, 1, 2, 3, (8., 3.2, 7.5), (-3.2, -8., 7.5)),
                 path(1, 0, 2, 3, (8., -3.2, 7.5), (3.2, -8., 7.5))]
    def encode(routes):
        lines = ['SC4PATHS', '1.2', '4', '0', '0']
        for route in routes:
            lines += [str(route[key]) for key in ('transport', 'lane', 'entry', 'exit', 'compatibility')]
            lines.append('2')
            lines += [','.join(map(str, point)) for point in route['points']]
        return ('\r\n'.join(lines) + '\r\n').encode('ascii')
    rail = b'SC4PATHS\r\n1.1\r\n2\r\n0\r\n1\r\n7\r\n0\r\n1\r\n0\r\n2\r\n-2.9,8,1\r\n-8,2.8,1\r\n7\r\n0\r\n0\r\n1\r\n2\r\n-8,-2.9,1\r\n2.9,8,1\r\n'
    return {'dd_rhw': {(*PATH, 0x5753A905): encode(dd), (*PATH, 0x5753A985): encode(dd_second)},
            'hsr': {(*PATH, 0x5DC01A00): rail}}


def fixture_channels():
    with patch.object(author, '_guard_sources'), patch.object(author, '_retained_models', return_value=b'model'):
        return author.build_alignment_b_channels(native_fixture())


class GHSRCrossingAlignmentBAuthorTests(unittest.TestCase):
    def test_phase_b_owns_the_other_two_cell_grid_phase(self):
        self.assertEqual(author.ALIGNMENT_B_CELLS, ((0, 0), (1, 0)))
        self.assertEqual(author.ALIGNMENT_B_FOOTPRINT, (2, 1))
        self.assertEqual(author.CELLS, ((0, 0), (0, 1)))
        self.assertEqual(author.FOOTPRINT, (1, 2))
        self.assertEqual(author.ALIGNMENT_B_RECIPE, approaches.ALIGNMENT_B_RECIPE)

    def test_writer_uses_native_dd_poses_and_the_other_rail_poses(self):
        with patch.object(author, '_guard_sources'), patch.object(author, '_retained_models', return_value=b'model') as models:
            context = native_fixture()
            before = deepcopy(context)
            channels = author.build_alignment_b_channels(context)
        self.assertEqual([cell for cell, _model, _paths in channels], [(0, 0), (1, 0)])
        self.assertEqual(models.call_args_list[0].args, (context, 0x5753A905, 0, 1))
        self.assertEqual(models.call_args_list[1].args, (context, 0x5753A985, 2, 3))
        self.assertEqual(context, before)

    def test_both_saved_tiles_explicitly_retain_native_elevations(self):
        for _cell, _model, raw in fixture_channels():
            self.assertEqual(raw.splitlines()[:5], [b'SC4PATHS', b'1.2', b'6', b'0', b'1'])
            routes = parse_paths(raw)['routes']
            self.assertEqual([route['transport'] for route in routes], [1, 1, 1, 1, 7, 7])
            self.assertEqual([route['points'][0][2] for route in routes], [15., 15., 7.5, 7.5, 1., 1.])

    def test_native_helper_seam_coordinates_override_rounded_core_exteriors(self):
        routes = [parse_paths(raw)['routes'][4:] for _cell, _model, raw in fixture_channels()]
        self.assertEqual(routes[0][0]['points'][0], (8., 2.9, 1.))
        self.assertEqual(routes[0][0]['points'][-1], (2.9, 8., 1.))
        self.assertEqual(routes[0][1]['points'][0], (-2.8, 8., 1.))
        self.assertEqual(routes[0][1]['points'][-1], (8., -2.9, 1.))
        self.assertEqual(routes[1][0]['points'][0], (-8., -2.9, 1.))
        self.assertEqual(routes[1][0]['points'][-1], (-2.9, -8., 1.))
        self.assertEqual(routes[1][1]['points'][0], (2.8, -8., 1.))
        self.assertEqual(routes[1][1]['points'][-1], (-8., 2.9, 1.))

    def test_all_six_core_journeys_meet_at_the_common_east_west_seam(self):
        routes = [parse_paths(raw)['routes'] for _cell, _model, raw in fixture_channels()]
        first = []
        second = []
        for index, members in enumerate(routes):
            for route in members:
                for endpoint, edge in ((0, route['entry']), (-1, route['exit'])):
                    if edge == (2 if index == 0 else 0):
                        east, north, height = route['points'][endpoint]
                        row = (route['transport'], round(east + 16 * index, 9), round(north, 9), height, endpoint)
                        (first if index == 0 else second).append(row)
        self.assertEqual(len(first), 6)
        self.assertEqual(len(second), 6)
        for transport, east, north, height, endpoint in first:
            self.assertEqual(second.count((transport, east, north, height, -1 if endpoint == 0 else 0)), 1)

    def test_interior_collars_are_one_metre_at_exactly_45_degrees(self):
        for column, (_cell, _model, raw) in enumerate(fixture_channels()):
            for route in parse_paths(raw)['routes'][4:]:
                interior = 0 if route['entry'] == (2 if column == 0 else 0) else -1
                neighbour = 1 if interior == 0 else -2
                a, b = route['points'][interior], route['points'][neighbour]
                self.assertAlmostEqual(math.dist(a, b), 1., places=9)
                self.assertAlmostEqual(abs(a[0] - b[0]), abs(a[1] - b[1]), places=9)
                self.assertEqual(a[2], b[2])

    def test_exterior_collars_match_the_complementary_native_helper_heading(self):
        # Native helper chord offsets are literal original-NAM measurements.
        expected = {(0, 0): (-10.9, 10.9), (0, 1): (5.2, -5.1),
                    (1, 0): (10.9, -10.9), (1, 1): (-5.2, 5.1)}
        for column, (_cell, _model, raw) in enumerate(fixture_channels()):
            for index, route in enumerate(parse_paths(raw)['routes'][4:]):
                exterior = 0 if route['entry'] == (1 if column == 0 else 3) else -1
                neighbour = 1 if exterior == 0 else -2
                a, b = route['points'][exterior], route['points'][neighbour]
                dx, dy = expected[column, index]
                if exterior == -1:
                    dx, dy = -dx, -dy
                self.assertAlmostEqual(math.dist(a, b), 3., places=9)
                self.assertAlmostEqual((b[0] - a[0]) * dy - (b[1] - a[1]) * dx, 0., places=8)
                self.assertGreater((b[0] - a[0]) * dx + (b[1] - a[1]) * dy, 0.)

    def test_report_distinguishes_external_authoring_from_preserved_internal_seams(self):
        with patch.object(author, '_guard_sources'):
            report = author.alignment_b_path_transition_report(native_fixture())
        self.assertEqual(len(report['routes']), 4)
        self.assertAlmostEqual(report['maximum_external_endpoint_shift_m'], .1)
        self.assertEqual(report['maximum_internal_endpoint_shift_m'], 0.)
        self.assertLess(report['maximum_lateral_deviation_from_source_chord_m'], .101)
        self.assertTrue(report['external_native_helper_coordinates_preserved'])
        self.assertFalse(report['game_operation_verified'])
        self.assertFalse(author.ALIGNMENT_B_TRANSITION_METADATA['core_donor_external_path_coordinates_preserved'])
        self.assertTrue(author.ALIGNMENT_B_TRANSITION_METADATA['core_donor_internal_path_coordinates_preserved'])

    def test_missing_or_changed_helper_chord_cannot_be_silently_blended(self):
        rail = author._ground_paths(native_fixture()['hsr'][*PATH, 0x5DC01A00])
        route = {'transport': 7, 'lane': 0, 'entry': 2, 'exit': 1, 'compatibility': 0,
                 'points': [(8., 2.9, 1.), (2.8, 8., 1.)]}
        changed = deepcopy(rail)
        changed[1]['points'][0] = (-8., -2.4, 1.)
        with self.assertRaisesRegex(ValueError, 'reviewed directed native helper|reviewed 0.1 m correction'):
            author._alignment_b_rail_collar(route, 0, changed)

    def test_helper_bindings_cover_both_decks_and_rail_with_no_owned_overlap(self):
        piece = specification()
        rows = approaches.approaches(piece)
        expected = [([0, 1], [0, 0], 3, '57530900', 2),
                    ([1, -1], [1, 0], 1, '57530200', 0),
                    ([0, -1], [0, 0], 1, '5dc01a00', 3),
                    ([1, 1], [1, 0], 3, '5dc01a00', 1)]
        self.assertEqual([(r['cell'], r['end_cell'], r['outward_edge'], r['native_tile_id'], r['native_rotation'])
                          for r in rows], expected)
        self.assertTrue(all(row['cell'] not in piece['cells'] for row in rows))
        self.assertTrue(all(row['optional'] and row['experimental'] for row in rows))

    def test_helper_grid_has_two_by_three_clearance_and_no_extra_owned_tiles(self):
        layout, checks, constraints = approaches.add_approaches(specification(), *author.alignment_b_core_construction_data())
        self.assertEqual(layout, ['ji.', 'ab<', 'hk.', '^..'])
        self.assertEqual(constraints, ['...', '++<', '...', '^..'])
        self.assertEqual(sum(row.count('+') for row in constraints), 2)
        self.assertEqual(len(checks), 6)
        self.assertEqual(sum('0xFFFFFFFF optional' in row for row in checks), 4)

    def test_native_rul1_solutions_are_shared_by_both_grid_alignments(self):
        self.assertEqual(approaches.rul1_sections(specification()), approaches.rul1_sections(specification(False)))
        self.assertEqual(sum(map(len, approaches.rul1_sections(specification()).values())), 12)

    def test_mixed_owner_recipe_cells_or_footprint_are_rejected(self):
        for key, value in [('recipe', approaches.RECIPE), ('id', approaches.PIECE_ID),
                           ('footprint', [1, 2]), ('cells', [[0, 0], [0, 1]])]:
            with self.subTest(key=key):
                piece = specification()
                piece[key] = value
                with self.assertRaises(ValueError):
                    approaches.approaches(piece)

    def test_original_alignment_a_helper_and_construction_outputs_are_unchanged(self):
        layout, checks, cons = approaches.add_approaches(specification(False), *author.core_construction_data())
        self.assertEqual(layout, ['jah<', 'ibk.', '.^..'])
        self.assertEqual(cons, ['.+.<', '.+..', '.^..'])
        self.assertEqual(checks, ['a - dirtroad: 0x03010000 monorail: 0x01000003',
                                  'b - dirtroad: 0x00000301 monorail: 0x00030100',
                                  'h - monorail: 0x04000100 dirtroad: 0x00000301, 0xFFFFFFFF optional',
                                  'i - monorail: 0x04000100 dirtroad: 0x03010000, 0xFFFFFFFF optional',
                                  'j - rail: 0x01010000 monorail: 0x00030100, 0xFFFFFFFF optional',
                                  'k - rail: 0x00000101 monorail: 0x01000003, 0xFFFFFFFF optional'])


class GHSRCrossingAlignmentBNativeAuthorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings_path = local_settings(ROOT)
        if not settings_path.is_file():
            raise unittest.SkipTest('Private NAM settings are unavailable')
        settings = jsonc.load(settings_path)
        profile = jsonc.load(ROOT / 'config/profiles/nam50-rhd.jsonc')
        roots = [Path(value).expanduser().resolve() for value in [settings['plugins'], *settings.get('extra_plugins', [])]]
        cls.context = {}
        for label in ('dd_rhw', 'hsr'):
            record = profile['files'][label]
            found = {path.resolve() for root in roots if root.is_dir() for path in root.rglob(record['filename'])}
            if not found:
                raise unittest.SkipTest('Audited native NAM source unavailable: ' + record['filename'])
            if len(found) != 1:
                raise ValueError('Ambiguous native NAM source: ' + record['filename'])
            raw = next(iter(found)).read_bytes()
            if hashlib.sha256(raw).hexdigest() != record['sha256']:
                raise ValueError('Native NAM source changed; re-audit rather than skip')
            cls.context[label] = {key: decompress(value) for key, value in entries(raw).items()}

    def test_alignment_a_native_model_and_path_bytes_match_the_previous_delivery(self):
        expected = [((0, 0), '39c7e3b884df2c673fe9e97147766b16f7d68576eb731ce5cb2411bc9e0feba8',
                     'c0647202666bf828612a49fd1576276379d848a4fa3a0fb5028cf1bb995f6db3'),
                    ((0, 1), '7567942cfc061b21dbe77696bba0a5f5dc91f1f92fab397bb8c656d0229af3bd',
                     'c053ea61baa8481a327223a057bddfb94f2fee25ed2b5137ee21d9851876422a')]
        self.assertEqual([(cell, hashlib.sha256(model).hexdigest(), hashlib.sha256(paths).hexdigest())
                          for cell, model, paths in author.build_channels(self.context)], expected)

    def test_actual_native_alignment_b_compiles_without_mutating_inputs(self):
        before = deepcopy(self.context)
        result = author.build_alignment_b_channels(self.context)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(model.startswith(b'3DMD') for _cell, model, _paths in result))
        self.assertEqual(self.context, before)

    def test_changed_original_resource_fingerprint_is_rejected(self):
        context = deepcopy(self.context)
        key = (*PATH, author.GHSR_DONOR)
        context['hsr'][key] += b'\r\n'
        with self.assertRaisesRegex(ValueError, 'Native DD/GHSR crossing source changed'):
            author.build_alignment_b_channels(context)


if __name__ == '__main__':
    unittest.main()
