"""Verify model-input ownership through the actual portable package reader.

The fixture uses real DBPF serialization, hashes, resource closure, and encoded
S3Ds. Native catalogue, construction, menu, and route semantics are substituted
to isolate this caller contract. The cache case executes the actual highway
cache with a small saved-model UV control, rather than a native-game audit.
"""
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

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'tests')]
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import verify
from scp.dbpf import encode_exemplar, pack_dbpf
from scp.models import pack_s3d, parse_s3d, validate_s3d
from scp_highway import ramp_verify
from test_render_meshes import fixture as model_fixture


class HighwayModelInputTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='scp-model-inputs-')
        self.addCleanup(temporary.cleanup)
        self.output = Path(temporary.name)
        self.folder = 'zzz_Simons_Custom_Pieces'
        self.payloads = {}
        self.pieces = []
        menus = {}
        for index, domain in enumerate(('highway', 'high-speed-rail')):
            tile = 0x7F5F0000 + index * 0x100
            preview = tile + 0xF5
            piece = {'id': f'fixture-{domain}', 'name': f'Fixture {domain}',
                     'domain': domain, 'recipe': 'fixture', 'tile_ids': [f'{tile:08x}'],
                     'preview_id': f'{preview:08x}', 'effect_name': f'preview_fixture_{index}',
                     'shadow_mappings': [], 'menu': {'id': f'{0x6A47FE00 + index:08x}'},
                     'asset_file': f'{self.folder}/20_Pieces/SCP_fixture-{domain}.dat'}
            self.pieces.append(piece)
            model = pack_s3d(model_fixture(1))
            properties = [
                {'id': '0x00000010', 'type': '0x0300', 'key_type': '0x0000',
                 'values': [11], 'repetitions': None},
                {'id': '0x27812823', 'type': '0x0300', 'key_type': '0x0080',
                 'values': [*verify.S3D, *range(tile, tile + 5)], 'repetitions': 7}]
            assets = {(*verify.S3D, tile + zoom): model for zoom in range(5)}
            text = piece['name']
            assets.update({
                (*verify.S3D, preview): model,
                (*verify.PATH, tile): b'fixture PATH',
                (*verify.LTEXT, tile): struct.pack('<HH', len(text), 0x1000) + text.encode('utf-16-le'),
                (*verify.EXEMPLAR, tile): encode_exemplar({'parent': [0, 0, 0], 'properties': properties}),
                (*verify.EFFECT, preview): piece['effect_name'].encode() * 4 + struct.pack('<I', preview) * 2})
            self.payloads[piece['asset_file']] = assets
            for prefix in (verify.MENU_EXEMPLAR, verify.ICON, verify.TITLE, verify.DESCRIPTION):
                menus[*prefix, int(piece['menu']['id'], 16)] = b'fixture menu resource'
        self.payloads[f'{self.folder}/00_SCP_Controller_NAM50.dat'] = {
            verify.RUL0: b'fixture controller', verify.NETWORK_INI: b'fixture network ini'}
        self.payloads[f'{self.folder}/10_SCP_Menu.dat'] = menus
        self.manifest = {'schema_version': 1, 'plugin_folder': self.folder,
                         'pieces': deepcopy(self.pieces), 'documentation': [],
                         'dependency_audit': {'textures': [], 'shadows': []}}
        self.write_fixture()
        self.enterContext(patch.object(verify, 'validate_catalog'))
        self.enterContext(patch.object(verify, 'load_local_donors', return_value=({}, {})))
        self.enterContext(patch.object(verify, 'check_construction', return_value={}))
        self.enterContext(patch.object(verify, 'validate_menu_resources', return_value={}))
        self.enterContext(patch.object(verify, 'check_piece_paths', return_value={}))
        provider = SimpleNamespace(verification_donor=lambda donors: None,
                                   validate_menu_resources=lambda *args, **kwargs: {},
                                   validate_effect=lambda piece, effect: None)
        self.enterContext(patch('scp.providers.domain_module', return_value=provider))

    def write_fixture(self):
        records = []
        for relative, resources in sorted(self.payloads.items()):
            raw = pack_dbpf(resources)
            path = self.output / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
            records.append({'path': relative, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
        self.manifest['files'] = records
        (self.output / 'manifest.json').write_text(json.dumps(self.manifest) + '\n')

    def inspect_model_inputs(self):
        calls = {}
        def inspect(resources, piece, donors):
            calls[piece['domain']] = dict(resources)
            return {'texture_ids': []}
        with patch.object(verify, 'check_piece_models', side_effect=inspect):
            self.assertTrue(verify.verify_build(self.output, write_report=False)['static_checks_passed'])
        return calls

    def test_highway_models_receive_exact_owned_dat_resources(self):
        calls = self.inspect_model_inputs()
        self.assertEqual(calls['highway'], self.payloads[self.pieces[0]['asset_file']])
        self.assertNotIn(verify.RUL0, calls['highway'])
        self.assertNotIn((*verify.S3D, int(self.pieces[1]['preview_id'], 16)), calls['highway'])

    def test_rail_models_keep_the_complete_combined_map(self):
        calls = self.inspect_model_inputs()
        combined = {key: value for resources in self.payloads.values() for key, value in resources.items()}
        self.assertEqual(calls['high-speed-rail'], combined)

    def assert_owned_closure_rejects_before_model_provider(self):
        self.write_fixture()
        with patch.object(verify, 'check_piece_models') as provider:
            with self.assertRaisesRegex(ValueError, 'Piece asset DAT contains missing, unexpected, or another piece resources'):
                verify.verify_build(self.output, write_report=False)
            provider.assert_not_called()

    def test_extra_owned_tgi_cannot_be_hidden_by_model_input_filtering(self):
        self.payloads[self.pieces[0]['asset_file']][1, 2, 3] = b'foreign resource'
        self.assert_owned_closure_rejects_before_model_provider()

    def test_removed_owned_resource_is_rejected_before_the_provider(self):
        del self.payloads[self.pieces[0]['asset_file']][*verify.S3D, int(self.pieces[0]['tile_ids'][0], 16) + 4]
        self.assert_owned_closure_rejects_before_model_provider()

    def test_moving_owned_model_to_another_dat_does_not_preserve_ownership(self):
        first, second = [self.payloads[piece['asset_file']] for piece in self.pieces]
        key = (*verify.S3D, int(self.pieces[0]['tile_ids'][0], 16) + 4)
        second[key] = first.pop(key)
        self.assert_owned_closure_rejects_before_model_provider()

    def test_unexpected_controller_tgi_still_fails_global_resource_closure(self):
        self.payloads[f'{self.folder}/00_SCP_Controller_NAM50.dat'][1, 2, 3] = b'foreign controller resource'
        self.write_fixture()
        with patch.object(verify, 'check_piece_models', side_effect=lambda *args: {'texture_ids': []}):
            with self.assertRaisesRegex(ValueError, 'Unexpected or missing package resource'):
                verify.verify_build(self.output, write_report=False)

    def test_owned_uv_change_reaches_the_real_cache_and_invalidates_success(self):
        ramp_verify._MODEL_AUDIT_CACHE.clear()
        self.addCleanup(ramp_verify._MODEL_AUDIT_CACHE.clear)
        key = (*verify.S3D, int(self.pieces[0]['tile_ids'][0], 16))
        def saved_uv_control(resources, piece):
            model = parse_s3d(resources[key])
            validate_s3d(model)
            if struct.unpack_from('<f', model['vertices'][0]['data'], 12)[0] != 0.:
                raise ValueError('owned UV control changed')
            return {'passed': True, 'texture_ids': []}
        def geometry(resources, piece, donors):
            return (ramp_verify.check_models(resources, piece, donors)
                    if piece['domain'] == 'highway' else {'texture_ids': []})
        with patch.object(ramp_verify, '_check_models_uncached', side_effect=saved_uv_control) as audit, \
             patch.object(verify, '_check_piece_geometry', side_effect=geometry):
            verify.verify_build(self.output, write_report=False)
            verify.verify_build(self.output, write_report=False)
            self.assertEqual(audit.call_count, 1)
            # Another piece changes while the highway's complete owned input stays identical.
            foreign = self.payloads[self.pieces[1]['asset_file']]
            foreign_key = (*verify.S3D, int(self.pieces[1]['tile_ids'][0], 16))
            changed = parse_s3d(foreign[foreign_key])
            data = bytearray(changed['vertices'][0]['data']); struct.pack_into('<f', data, 12, .25)
            changed['vertices'][0]['data'] = bytes(data); foreign[foreign_key] = pack_s3d(changed)
            self.write_fixture()
            verify.verify_build(self.output, write_report=False)
            self.assertEqual(audit.call_count, 1)
            owned = self.payloads[self.pieces[0]['asset_file']]
            changed = parse_s3d(owned[key])
            data = bytearray(changed['vertices'][0]['data']); struct.pack_into('<f', data, 12, .625)
            changed['vertices'][0]['data'] = bytes(data); owned[key] = pack_s3d(changed)
            self.write_fixture()
            with self.assertRaisesRegex(ValueError, 'owned UV control changed'):
                verify.verify_build(self.output, write_report=False)
            self.assertEqual(audit.call_count, 2)


if __name__ == '__main__':
    unittest.main()
