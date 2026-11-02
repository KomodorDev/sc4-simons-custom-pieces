"""Portable resource-closure tests for non-rail providers and structural PATHs."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import struct
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from PIL import Image
from scp import build, verify
from scp.dbpf import encode_exemplar, exemplar, pack_dbpf, entries, decompress
from scp.models import pack_s3d, parse_s3d
from scp.recipes import effect_clone, label
from scp.rul0 import compose_rul0
from scp.shadows import build_shadows, encode_shadow_fsh
from scp.test_support import plane
from scp_highway import menu
from scp_highway.recipes import construction, validate_effect

TILE, PREVIEW = 0x7F500000, 0x7F500FF5
TEXTURE = (*verify.TEXTURE, TILE)
NATIVE_EFFECT = (*verify.EFFECT, 0x12345600)
NATIVE_MODEL = 0x12345605
DONOR_NAME = 'preview_fixture_donor___001'
AUTHORED_NAME = 'preview_fixture_piece___001'
DONOR_EFFECT = b'fixture_effect_head' + (DONOR_NAME.encode() + b'\0') * 4 + struct.pack('<II', NATIVE_MODEL, NATIVE_MODEL) + b'fixture_effect_tail'


def piece_definition():
    return {'schema_version': 1, 'id': 'domain-contract-fixture', 'domain': 'highway',
            'name': 'Domain resource fixture', 'description': 'Synthetic shared-contract test.',
            'recipe': 'highway_contract_fixture', 'enabled_by_default': False, 'status': 'experimental',
            'puzzle_id': 'f600', 'tile_ids': [f'{TILE:08x}'], 'preview_id': f'{PREVIEW:08x}',
            'effect_name': AUTHORED_NAME, 'footprint': [1, 1], 'cells': [[0, 0]], 'orientation_count': 8,
            'dependencies': ['controller'], 'authored_texture_ids': [f'{TILE:08x}'],
            'menu': {'id': '6a47f600', 'order': 'ffffff05', 'style': 'ddrhw-crossing'},
            'shadow_mode': 'generated', 'shadow_mappings': [{'tile': f'{TILE:08x}', 'source': f'{TILE:08x}', 'rotation': 0}],
            'provenance': {'redistribution': 'synthetic test resources'},
            'game_tests': {key: 'unverified' for key in ('placement', 'traffic_both_directions',
                'no_unwanted_transfers', 'rotations_and_mirrors', 'shadows', 'demolition', 'save_reload')},
            'asset_file': 'zzz_Simons_Custom_Pieces/20_Pieces/SCP_domain-contract-fixture.dat'}


def fixture_model(texture=TILE):
    model = plane(height=7.5)
    raw = struct.pack('<IBBBBHIBB', 0, 0, 0, 0, 0, 0, 0, 0, 1)
    raw += struct.pack('<IBBBBHHB', texture, 0, 0, 0, 0, 0, 0, 0)
    model['materials'] = [{'raw': raw, 'textures': [texture]}]
    return pack_s3d(model)


class ZeroRoutePathContractTests(unittest.TestCase):
    def test_actual_native_zero_route_header_is_accepted(self):
        # Exact decoded bytes measured from NAM MIS shoulder/barrier5792A449.
        native = b'SC4PATHS\r\n1.2\r\n0\r\n0\r\n0\r\n'
        self.assertEqual(verify.parse_paths(native), {'version': '1.2', 'terrain': 0, 'routes': []})

    def test_negative_route_count_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Invalid SC4PATH header'):
            verify.parse_paths(b'SC4PATHS\n1.2\n-1\n0\n0\n')

    def test_zero_route_header_does_not_hide_trailing_data(self):
        with self.assertRaisesRegex(ValueError, 'Unexpected trailing'):
            verify.parse_paths(b'SC4PATHS\n1.2\n0\n0\n0\n1\n')

    def test_zero_routes_still_require_zero_stops_and_valid_terrain(self):
        for stops, terrain in ((1, 0), (0, 2)):
            with self.subTest(stops=stops, terrain=terrain), self.assertRaises(ValueError):
                verify.parse_paths(f'SC4PATHS\n1.2\n0\n{stops}\n{terrain}\n'.encode())


class DomainDispatchAndAllocationTests(unittest.TestCase):
    def test_explicit_non_rail_domain_wins_over_a_rail_named_recipe(self):
        piece = {'domain': 'highway', 'recipe': 'rail_contract_fixture'}
        provider = SimpleNamespace(check_paths=lambda resources, source: {'domain': source['domain']})
        with patch('scp.providers.domain_module', return_value=provider) as resolve:
            self.assertEqual(verify.check_piece_paths({}, piece), {'domain': 'highway'})
        resolve.assert_called_once_with(piece, 'verify')

    def test_provider_unknown_recipe_failure_is_not_swallowed(self):
        def reject(resources, piece):
            raise ValueError('Unknown highway recipe remains rejected')
        with patch('scp.providers.domain_module', return_value=SimpleNamespace(check_paths=reject)):
            with self.assertRaisesRegex(ValueError, 'Unknown highway recipe remains rejected'):
                verify.check_piece_paths({}, {'domain': 'highway', 'recipe': 'unknown_contract_recipe'})

    def test_owned_texture_and_generated_shadow_are_both_reserved_before_build(self):
        piece = piece_definition(); context = {'controller': {build.RUL0: b'[Ordering]\r\n'}}
        for key in (TEXTURE, (*verify.SHADOW, TILE + 4)):
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, 'collide'):
                build.preflight_allocations(context, {key: ['fixture.dat']}, [piece])

    def test_unrelated_preview_bytes_fail_even_with_correct_reference_counts(self):
        spec = {'effect_name': 'preview_scp_dd_cross____001', 'preview_id': f'{PREVIEW:08x}'}
        arbitrary = b'not a native effect' + (spec['effect_name'].encode() + b'\0') * 4 + struct.pack('<II', PREVIEW, PREVIEW)
        with self.assertRaisesRegex(ValueError, 'pinned native effect bytes'):
            validate_effect(spec, arbitrary)


class SavedNonRailPackageContractTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix='scp-domain-contract-')
        self.addCleanup(self.directory.cleanup)
        self.output = Path(self.directory.name)
        self.piece = piece_definition()
        native_rul = b'[Ordering]\r\n\r\n[FixtureNative]\r\nkey=value\r\n'
        native_ini = b'[Shadow remapping]\r\n'
        delta = construction(self.piece, cells=['a<', '^.'], checks=['a - dirtroad: 0x02000200'], cons=['|<', '^.'])
        rul, composition = compose_rul0(native_rul, [delta])
        insertion = (';BEGIN SIMONS CUSTOM PIECES SHADOWS\r\n' +
                     f'scp_domain-contract-fixture = 0x{TILE:08x},0xFFFFFFF0,0x{TILE:08x},0x0000000F,0,0\r\n' +
                     ';END SIMONS CUSTOM PIECES SHADOWS\r\n')
        self.overlay = {'rul0': composition, 'network_ini': {'base_sha256': hashlib.sha256(native_ini).hexdigest(), 'insertion': insertion}}
        self.controller = {verify.RUL0: rul, verify.NETWORK_INI: native_ini + insertion.encode()}
        model = fixture_model()
        tile_record = {'parent': [0, 0, 0], 'properties': [
            {'id': '0x10', 'type': '0x300', 'key_type': '0', 'values': [11]},
            {'id': '0x20', 'type': '0xc00', 'key_type': '0x80', 'values': self.piece['name']},
            {'id': '0x27812823', 'type': '0x300', 'key_type': '0x80', 'values': [*verify.S3D, *range(TILE, TILE + 5)]}]}
        self.assets = {(*verify.S3D, TILE + zoom): model for zoom in range(5)}
        self.assets.update({(*verify.S3D, PREVIEW): model, (*verify.PATH, TILE): b'SC4PATHS\n1.2\n0\n0\n0\n',
            (*verify.EXEMPLAR, TILE): encode_exemplar(tile_record), (*verify.LTEXT, TILE): label(self.piece['name']),
            (*verify.EFFECT, PREVIEW): effect_clone(DONOR_EFFECT, DONOR_NAME, AUTHORED_NAME, NATIVE_MODEL, PREVIEW),
            TEXTURE: encode_shadow_fsh(Image.new('L', (8, 8), 255))})
        self.assets.update(build_shadows(model, TILE))
        self.menus, _audit = menu.build_menu_resources(menu.portable_baseline(), self.piece)
        self.recipes_provider = SimpleNamespace(effect_donor=lambda piece: (NATIVE_EFFECT, DONOR_NAME, NATIVE_MODEL),
                                                validate_effect=self.validate_fixture_effect)
        self.verify_provider = SimpleNamespace(check_paths=lambda resources, piece: {'fixture_paths_checked': True},
            check_models=self.fixture_model_report, check_construction_fields=lambda *args: {'fixture_flags_checked': True})
        def provider(piece, feature):
            return {'menu': menu, 'recipes': self.recipes_provider, 'verify': self.verify_provider}[feature]
        patcher = patch('scp.providers.domain_module', side_effect=provider)
        patcher.start(); self.addCleanup(patcher.stop)

    def fixture_model_report(self, resources, piece, donors):
        texture_ids = {texture for tile in piece['tile_ids'] for zoom in range(5)
                       for mat in parse_s3d(resources[*verify.S3D, int(tile, 16) + zoom])['materials']
                       for texture in mat['textures']}
        return {'texture_ids': sorted(texture_ids)}

    def validate_fixture_effect(self, piece, raw):
        restored = raw.replace(AUTHORED_NAME.encode(), DONOR_NAME.encode()).replace(struct.pack('<I', PREVIEW), struct.pack('<I', NATIVE_MODEL))
        if restored != DONOR_EFFECT:
            raise ValueError('Fixture preview effect differs from its portable donor')
        return {'portable_effect_checked': True}

    def write_package(self, texture_dependencies=None):
        payloads = {'zzz_Simons_Custom_Pieces/00_SCP_Controller_NAM50.dat': pack_dbpf(self.controller),
                    'zzz_Simons_Custom_Pieces/10_SCP_Menu.dat': pack_dbpf(self.menus),
                    self.piece['asset_file']: pack_dbpf(self.assets)}
        files = []
        for name, raw in payloads.items():
            path = self.output / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
            files.append({'path': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
        manifest = {'schema_version': 1, 'plugin_folder': 'zzz_Simons_Custom_Pieces', 'pieces': [self.piece],
                    'profile': {'id': 'fixture', 'donors': []}, 'files': files, 'documentation': [],
                    'overlay': self.overlay, 'dependency_audit': {'textures': texture_dependencies or [], 'shadows': []}}
        (self.output / 'manifest.json').write_text(json.dumps(manifest))

    def test_portable_non_rail_package_owns_atlas_and_generated_shadows(self):
        self.write_package()
        report = verify.verify_build(self.output, write_report=False)
        self.assertTrue(report['static_checks_passed'])
        self.assertEqual(report['external_textures'], 0)
        self.assertEqual(report['external_shadows'], 0)
        self.assertFalse(report['local_donor_comparison'])
        self.assertEqual(report['pieces'][0]['menu']['menu'], 'Highways')

    def test_owned_atlas_missing_from_own_asset_dat_is_rejected(self):
        del self.assets[TEXTURE]; self.write_package()
        with self.assertRaisesRegex(ValueError, 'Piece asset DAT contains missing'):
            verify.verify_build(self.output, write_report=False)

    def test_undeclared_atlas_resource_cannot_hide_in_asset_dat(self):
        self.assets[(*verify.TEXTURE, TILE + 16)] = self.assets[TEXTURE]; self.write_package()
        with self.assertRaisesRegex(ValueError, 'Piece asset DAT contains missing'):
            verify.verify_build(self.output, write_report=False)

    def test_generated_shadow_corruption_is_rejected_without_donors(self):
        self.assets[*verify.SHADOW, TILE + 4] = self.assets[*verify.SHADOW, TILE + 3]; self.write_package()
        with self.assertRaisesRegex(ValueError, 'Wrong shadow zoom dimensions'):
            verify.verify_build(self.output, write_report=False)

    def test_exemplar_zoom_pointer_is_independently_checked_for_non_rail(self):
        record = exemplar(self.assets[*verify.EXEMPLAR, TILE])
        for prop in record['properties']:
            if int(prop['id'], 16) == 0x27812823:
                prop['values'][-1] += 1
        self.assets[*verify.EXEMPLAR, TILE] = encode_exemplar(record); self.write_package()
        with self.assertRaisesRegex(ValueError, 'exemplar|zoom models'):
            verify.verify_build(self.output, write_report=False)

    def test_portable_effect_hook_rejects_unchanged_counts_with_changed_payload(self):
        self.assets[*verify.EFFECT, PREVIEW] += b'corrupt tail'; self.write_package()
        with self.assertRaisesRegex(ValueError, 'portable donor'):
            verify.verify_build(self.output, write_report=False)

    def test_owned_atlas_cannot_be_misreported_as_external_dependency(self):
        self.write_package(texture_dependencies=['7ab50e44-1abe787d-7f500000'])
        with self.assertRaisesRegex(ValueError, 'Declared texture dependencies'):
            verify.verify_build(self.output, write_report=False)


if __name__ == '__main__':
    unittest.main()
