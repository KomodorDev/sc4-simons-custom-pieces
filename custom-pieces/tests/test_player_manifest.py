"""Compact dependency plans use synthetic resources and no source builders."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest

ROOT = next(path for path in Path(__file__).resolve().parents if (path / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp.dbpf import pack_dbpf
from scp.install import FOLDER, NETWORK_INI, RUL0
from scp.player_manifest import (INSTALL_MANIFEST, build_install_manifest, load_install_manifest,
                                 prepare_dependencies)
from scp.prebuilt import CONTROLLER, KIND, MENU, MODEL_PREFIX


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class PlayerManifestTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.source = self.base / 'source'
        self.payload = self.base / 'payload'
        self.plugins = self.base / 'Plugins'
        self.game = self.base / 'game'
        self.work = self.base / 'work'
        self.plugins.mkdir()
        self.game.mkdir()
        self.installation = SimpleNamespace(plugins=self.plugins, extra_plugins=(), game_folder=self.game)
        self.key = (0x7AB50E44, 0x1ABE787D, 0x04000200)
        self.resource = b'exact stored dependency bytes'
        self.original = self.plugins / 'OriginalTextures.dat'
        self.original.write_bytes(pack_dbpf({self.key: self.resource, (1, 2, 3): b'other source bytes'}))
        self.capture = pack_dbpf({self.key: self.resource})
        self.controller = self.plugins / 'NetworkAddonMod_Controller.dat'
        self.controller.write_bytes(pack_dbpf({RUL0: b'native rules', NETWORK_INI: b'native ini'}))
        self.profile = {'id': 'nam50-rhd', 'donors': [
            {'filename': self.controller.name, 'sha256': digest(self.controller.read_bytes())},
            {'filename': 'SCP_Texture_Capture.dat', 'sha256': digest(self.capture)},
        ]}
        files = []
        for name, resources in {
                CONTROLLER: {RUL0: b'custom rules', NETWORK_INI: b'custom ini'},
                MENU: {(0x6534284A, 0x2A3858E4, 0xABC123): b'menu'},
                '20_Pieces/SCP_synthetic-piece.dat': {(*MODEL_PREFIX, 0xABC124): b'model'}}.items():
            raw = pack_dbpf(resources)
            path = self.payload / FOLDER / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
            files.append({'path': f'{FOLDER}/{name}', 'bytes': len(raw), 'sha256': digest(raw)})
        self.payload_manifest = {'schema_version': 1, 'kind': KIND, 'plugin_folder': FOLDER,
                                 'source_commit': 'a' * 40, 'verified_build_manifest_sha256': 'b' * 64,
                                 'profile': self.profile, 'pieces': [{'id': 'synthetic-piece'}],
                                 'files': files, 'dependency_audit': {'textures': [], 'shadows': []},
                                 'exclusive_instance_ids': ['00abc123']}
        self.write(self.payload / 'manifest.json', self.payload_manifest)
        self.write(self.source / 'project.jsonc', {
            'profile': 'config/profile.jsonc',
            'domains': {'fixture': {'path': 'domains/fixture', 'registry': 'domains/fixture/domain.jsonc'}}})
        self.write(self.source / 'domains/fixture/domain.jsonc', {'pieces': ['synthetic-piece/piece.jsonc']})
        self.piece_file = self.source / 'domains/fixture/synthetic-piece/piece.jsonc'
        self.write(self.piece_file, {'id': 'synthetic-piece', 'name': 'Synthetic piece', 'status': 'implemented',
                                     'game_tests': {'placement': 'unverified'}})
        self.write(self.source / 'config/profile.jsonc', {'id': self.profile['id'], 'files': {
            'controller': self.profile['donors'][0],
            'textures': {**self.profile['donors'][1], 'audit': 'evidence/texture.jsonc'}}})
        self.write(self.source / 'config/installer.jsonc', {'schema_version': 1, 'selection': 'all-implemented'})
        self.write(self.source / 'domains/highway/menu-layout.jsonc', {'layouts': {'one': {}, 'two': {}}})
        self.write(self.source / 'evidence/texture.jsonc', {
            'status': 'complete', 'matching_index_entries': 1, 'tgi': self.tgi,
            'scope': {'archive': '<NAM Plugins>/OriginalTextures.dat'},
            'matches': [{'archive_sha256': digest(self.original.read_bytes()),
                         'stored_resource_sha256': digest(self.resource)}],
            'capture': {'sha256': digest(self.capture)},
            'private_note': 'Not needed by players; omit this from the generated data.'})
        self.manifest = build_install_manifest(self.source, self.payload)

    @property
    def tgi(self):
        return '-'.join(f'{value:08x}' for value in self.key)

    def write(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding='utf-8')

    def test_generation_omits_authoring_paths_and_evidence_prose(self):
        self.assertEqual(self.manifest['pieces'], [{'id': 'synthetic-piece', 'name': 'Synthetic piece'}])
        self.assertEqual(self.manifest['assembly_menu_layouts'], 3)
        serialized = json.dumps(self.manifest)
        for forbidden in ('evidence/', 'private_note', 'Not needed by players', '<NAM Plugins>'):
            self.assertNotIn(forbidden, serialized)
        self.write(self.source / INSTALL_MANIFEST, self.manifest)
        self.assertEqual(load_install_manifest(self.source, self.payload, 'a' * 40), self.manifest)

    def test_generation_requires_complete_selection_and_original_donor_hashes(self):
        piece = json.loads(self.piece_file.read_text())
        piece['status'] = 'draft'
        self.write(self.piece_file, piece)
        with self.assertRaisesRegex(ValueError, 'complete implemented'):
            build_install_manifest(self.source, self.payload)
        piece['status'] = 'implemented'
        self.write(self.piece_file, piece)
        profile_file = self.source / 'config/profile.jsonc'
        profile = json.loads(profile_file.read_text())
        profile['files']['textures']['sha256'] = '0' * 64
        self.write(profile_file, profile)
        with self.assertRaisesRegex(ValueError, 'donor fingerprints differ'):
            build_install_manifest(self.source, self.payload)

    def test_manifest_rejects_payload_binding_and_capture_path_tampering(self):
        for key, value, error in (
                ('source_commit', 'b' * 40, 'differs'),
                ('payload_manifest_sha256', '0' * 64, 'differs'),
                ('pieces', [{'id': 'missing-piece', 'name': 'Missing'}], 'piece selection')):
            changed = deepcopy(self.manifest)
            changed[key] = value
            self.write(self.source / INSTALL_MANIFEST, changed)
            with self.assertRaisesRegex(ValueError, error):
                load_install_manifest(self.source, self.payload)
        changed = deepcopy(self.manifest)
        changed['captures'][0]['filename'] = '../capture.dat'
        self.write(self.source / INSTALL_MANIFEST, changed)
        with self.assertRaisesRegex(ValueError, 'dependency capture'):
            load_install_manifest(self.source, self.payload)

    def test_dependency_preparation_preserves_exact_stored_bytes_and_original(self):
        original = self.original.read_bytes()
        roots, captures = prepare_dependencies(self.manifest, self.installation, self.work)
        self.assertEqual(len(roots), 1)
        self.assertEqual((roots[0] / 'SCP_Texture_Capture.dat').read_bytes(), self.capture)
        self.assertEqual(self.original.read_bytes(), original)
        self.assertEqual(captures, [{'filename': 'SCP_Texture_Capture.dat', 'sha256': digest(self.capture)}])
        self.assertFalse((self.plugins / FOLDER).exists())

    def test_game_capture_plan_reads_only_the_selected_game_original(self):
        self.original.rename(self.game / self.original.name)
        self.manifest['captures'][0]['sources'][0]['location'] = 'game'
        roots, _ = prepare_dependencies(self.manifest, self.installation, self.work)
        self.assertEqual((roots[0] / 'SCP_Texture_Capture.dat').read_bytes(), self.capture)

    def test_resource_bundle_plan_preserves_resources_from_game_and_nam(self):
        other_key = (0x7AB50E44, 0x1ABE787D, 0x04000201)
        other_raw = b'exact game dependency bytes'
        game_archive = self.game / 'SimCity_4.dat'
        game_archive.write_bytes(pack_dbpf({other_key: other_raw}))
        captured = pack_dbpf({self.key: self.resource, other_key: other_raw})
        payload_manifest = deepcopy(self.payload_manifest)
        payload_manifest['profile']['donors'][1]['sha256'] = digest(captured)
        self.write(self.payload / 'manifest.json', payload_manifest)
        profile_file = self.source / 'config/profile.jsonc'
        profile = json.loads(profile_file.read_text())
        profile['files']['textures'].update(sha256=digest(captured), capture_kind='resource-bundle')
        self.write(profile_file, profile)
        self.write(self.source / 'evidence/texture.jsonc', {
            'status': 'complete', 'capture_kind': 'resource-bundle',
            'capture': {'file': 'SCP_Texture_Capture.dat', 'sha256': digest(captured)},
            'sources': [{'filename': path.name, 'location': location,
                         'archive_sha256': digest(path.read_bytes()), 'resources': [{
                             'tgi': '-'.join(f'{value:08x}' for value in key),
                             'stored_resource_sha256': digest(raw)}]}
                        for path, location, key, raw in (
                            (self.original, 'plugins', self.key, self.resource),
                            (game_archive, 'game', other_key, other_raw))]})
        data = build_install_manifest(self.source, self.payload)
        self.write(self.source / INSTALL_MANIFEST, data)
        data = load_install_manifest(self.source, self.payload)
        roots, _ = prepare_dependencies(data, self.installation, self.work)
        self.assertEqual((roots[0] / 'SCP_Texture_Capture.dat').read_bytes(), captured)

    def test_existing_capture_cannot_bypass_original_checks(self):
        (self.plugins / 'SCP_Texture_Capture.dat').write_bytes(self.capture)
        roots, captures = prepare_dependencies(self.manifest, self.installation, self.work)
        self.assertEqual((roots, captures), ([], []))
        self.original.write_bytes(pack_dbpf({self.key: b'changed'}))
        with self.assertRaisesRegex(ValueError, 'fingerprint mismatch'):
            prepare_dependencies(self.manifest, self.installation, self.work)
        self.assertFalse(self.work.exists())

    def test_duplicate_original_and_resource_hash_mismatch_fail_before_writes(self):
        duplicate = self.plugins / 'duplicate' / self.original.name
        duplicate.parent.mkdir()
        duplicate.write_bytes(self.original.read_bytes())
        with self.assertRaisesRegex(ValueError, 'Expected one original'):
            prepare_dependencies(self.manifest, self.installation, self.work)
        duplicate.unlink()
        self.manifest['captures'][0]['sources'][0]['resources'][0]['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'resource changed'):
            prepare_dependencies(self.manifest, self.installation, self.work)
        self.assertFalse(self.work.exists())

    def test_minimal_runtime_installs_repeats_and_undoes_without_site_packages(self):
        package = self.base / 'runtime/scp'
        package.mkdir(parents=True)
        for name in ('__init__', 'install', 'prebuilt', 'dbpf', 'player_manifest'):
            shutil.copy2(ROOT / 'framework/scp' / f'{name}.py', package)
        compact = self.base / 'compact.json'
        self.write(compact, self.manifest)
        program = '''
import hashlib, json, sys
from pathlib import Path
from types import SimpleNamespace
from scp.install import FOLDER, install_prebuilt, rollback_install
from scp.player_manifest import prepare_dependencies
from scp.prebuilt import verify_payload
base = Path(sys.argv[1])
plugins, payload, work = base/'Plugins', base/'payload', base/'work'
manifest = json.loads((base/'compact.json').read_text())
roots, _ = prepare_dependencies(manifest, SimpleNamespace(plugins=plugins, extra_plugins=(), game_folder=base/'game'), work)
options = dict(source_commit='a'*40, expected_manifest_sha256=manifest['payload_manifest_sha256'],
               expected_piece_ids=['synthetic-piece'], expected_profile=verify_payload(payload)['profile'], extra_roots=roots)
def hashes():
    return {p.relative_to(plugins/FOLDER).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (plugins/FOLDER).rglob('*') if p.is_file()}
first = install_prebuilt(payload, plugins, base/'backups', **options)
previous = hashes()
repeat = install_prebuilt(payload, plugins, base/'backups', **options)
rollback_install(plugins, base/'backups', repeat['backup_id'], extra_roots=roots)
assert hashes() == previous
rollback_install(plugins, base/'backups', first['backup_id'], extra_roots=roots)
assert not (plugins/FOLDER).exists()
assert not any(name.split('.')[0] in {'numpy', 'PIL', 'shapely'} for name in sys.modules)
assert not any(name in sys.modules for name in ('scp.build', 'scp.catalog', 'scp.adaptive_network', 'scp.track_paths'))
'''
        result = subprocess.run([sys.executable, '-S', '-B', '-c',
                                 f"import sys; sys.path.insert(0, {str(package.parent)!r});" + program,
                                 str(self.base)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
