"""Mutation controls and optional private-native integration for the DD core."""
from copy import deepcopy
from pathlib import Path
import hashlib
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.dbpf import entries, decompress, pack_dbpf
from scp.paths import local_settings
from scp.track_paths import PATH, S3D
from scp.verify import parse_rules, check_emitted_runtime_addresses
from scp_highway import native, recipes, verify, menu


def specification():
    return {'id': 'test-native-crossing', 'name': 'Measured native DD RHW-4 crossing',
            'description': 'Native car and pedestrian channels; game observations pending.',
            'recipe': native.RECIPE, 'domain': 'highway', 'footprint': [3, 3],
            'cells': [list(cell) for cell in native.CELLS],
            'tile_ids': ['5f810100', '5f810010', '5f810110', '5f810210', '5f810120'],
            'preview_id': '5f81fff0', 'puzzle_id': 'c600',
            'effect_name': 'preview_scp_dd_cross____001',
            'menu': {'id': '6a47c600', 'order': 'ffffff05', 'style': 'ddrhw-crossing'}}


class NativeCrossingPortableTests(unittest.TestCase):
    def setUp(self):
        self.spec = specification()
        self.assets = {(*PATH, int(tile, 16)): native.encode_paths(routes)
                       for tile, routes in zip(self.spec['tile_ids'], verify.expected_paths())}

    def test_complete_saved_graph_consumes_every_route_in_four_proper_rotations(self):
        report = verify.check_paths(self.assets, self.spec)
        self.assertEqual(report['complete_directed_journeys'], 10)
        self.assertEqual(report['matched_internal_lane_seams'], 20)
        self.assertEqual(report['route_fragments_consumed'], 30)
        self.assertEqual(report['proper_rotations_checked'], 4)
        self.assertEqual(report['pedestrian_channels'], 2)
        self.assertFalse(report['game_operation_tested'])

    def test_lost_avenue_lane_cannot_hide_behind_the_four_highway_lanes(self):
        tile = int(self.spec['tile_ids'][2], 16)
        routes = native.parse_paths(self.assets[*PATH, tile])
        routes.pop(5)
        self.assets[*PATH, tile] = native.encode_paths(routes)
        with self.assertRaisesRegex(ValueError, 'literal native route measurements'):
            verify.check_paths(self.assets, self.spec)

    def test_saved_lane_displacement_fails_without_trusting_metadata(self):
        tile = int(self.spec['tile_ids'][3], 16)
        routes = native.parse_paths(self.assets[*PATH, tile])
        x, y, h = routes[0]['points'][0]
        routes[0]['points'][0] = (x, y + .1, h)
        self.assets[*PATH, tile] = native.encode_paths(routes)
        with self.assertRaisesRegex(ValueError, 'literal native route measurements'):
            verify.check_paths(self.assets, self.spec)

    def test_exact_native_network_flags_and_runtime_autotile_addresses(self):
        ring, rules = parse_rules(recipes.construction(self.spec))
        fields = {}
        for key, value in rules[int(self.spec['puzzle_id'], 16)]:
            fields.setdefault(key, []).append(value)
        verify.check_construction_fields(fields, self.spec, self.assets)
        report = check_emitted_runtime_addresses(fields, self.spec)
        self.assertEqual(report['wrong_model_selections'], 0)
        self.assertEqual(report['cells_checked'], 5)
        self.assertEqual(len(ring[0]), 8)
        self.assertNotIn('Transpose', recipes.construction(self.spec))

    def test_changed_network_flag_is_not_accepted_as_equivalent(self):
        _ring, rules = parse_rules(recipes.construction(self.spec))
        fields = {}
        for key, value in rules[int(self.spec['puzzle_id'], 16)]:
            fields.setdefault(key, []).append(value)
        fields['CheckType'][0] = 'a - avenue: 0x00030100'
        with self.assertRaisesRegex(ValueError, 'measured native highway/Avenue construction flags'):
            verify.check_construction_fields(fields, self.spec, self.assets)

    def test_highway_menu_keeps_native_road_menu_property_and_rejects_changed_icon(self):
        resources, report = menu.build_menu_resources(menu.portable_baseline(), self.spec)
        self.assertEqual(report['menu'], 'Roads')
        self.assertFalse(report['in_game_menu_tested'])
        resources[*menu.ICON, int(self.spec['menu']['id'], 16)] += b'changed'
        with self.assertRaisesRegex(ValueError, 'Wrong highway menu icon'):
            menu.validate_menu_resources(resources, menu.portable_baseline(), self.spec)


class NativeCrossingPrivateIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings = local_settings(ROOT)
        if not settings.is_file():
            raise unittest.SkipTest('Private NAM settings are unavailable')
        folder = Path(jsonc.load(settings)['plugins'])
        cls.context = {}
        for label, filename, fingerprint in (
            ('dd_rhw', 'RealHighway_DD_RHW-4.dat', 'ccf8dabd3930fce92d0baa872ff974e3a536ddcc40762505a2e70eafcf9c0dfb'),
            ('rhw_core', 'RealHighway_Core.dat', '8a172e4d7f628e09af3e153ef2effb34a2bcf876ff3c8f76210cb48d660aa191')):
            matches = list(folder.rglob(filename)) if folder.is_dir() else []
            if not matches:
                raise unittest.SkipTest('Audited native NAM highway archives are unavailable')
            if len(matches) != 1:
                raise ValueError('Ambiguous native highway archive')
            raw = matches[0].read_bytes()
            if hashlib.sha256(raw).hexdigest() != fingerprint:
                raise ValueError('Native highway archive changed; re-audit rather than skip')
            cls.context[label] = {key: decompress(value) for key, value in entries(raw).items()}

    def test_real_saved_dat_reopens_and_passes_independent_routes_and_native_model_fingerprints(self):
        spec = specification()
        resources, _rules = recipes.build_piece(spec, self.context)
        saved = {key: decompress(value) for key, value in entries(pack_dbpf(resources)).items()}
        self.assertEqual(verify.check_paths(saved, spec)['complete_directed_journeys'], 10)
        models = verify.check_models(saved, spec, None)
        self.assertTrue(models['native_channel_fingerprints_verified'])
        self.assertEqual(models['native_paired_deck_width_m'], 16.)
        self.assertFalse(models['game_rendering_tested'])
        self.assertEqual(menu.menu_donor(self.context), menu.portable_baseline())

    def test_one_changed_model_vertex_fails_portable_native_fingerprint(self):
        spec = specification()
        resources, _rules = recipes.build_piece(spec, self.context)
        key = (*S3D, int(spec['tile_ids'][2], 16))
        raw = bytearray(resources[key]); raw[64] ^= 1; resources[key] = bytes(raw)
        with self.assertRaisesRegex(ValueError, 'model fingerprint changed'):
            verify.check_models(resources, spec, None)


if __name__ == '__main__':
    unittest.main()
