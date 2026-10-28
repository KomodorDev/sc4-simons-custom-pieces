"""Installer boundary tests use tiny synthetic DBPFs, never the real Plugins.

The build verifier is mocked because these tests exercise installation and
rollback rather than reconstructing NAM geometry. File hashes, native donor
fingerprints, foreign DBPF overlays, receipts and snapshots are checked by the
real installer and DBPF index reader.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import struct
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file()) / 'framework'))
from scp.install import (FOLDER, RECEIPT, OPERATION_LOCK, RUL0, NETWORK_INI,
                         _foreign_overlays, install_build, rollback_install, uninstall)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def archive(resources):
    """Independent fixture writer: uncompressed DBPF 1.0, index version 7."""
    header = bytearray(96)
    header[:4] = b'DBPF'
    struct.pack_into('<II', header, 4, 1, 0)
    struct.pack_into('<I', header, 32, 7)
    body, index = bytearray(), bytearray()
    for key, raw in sorted(resources.items()):
        index.extend(struct.pack('<IIIII', *key, 96 + len(body), len(raw)))
        body.extend(raw)
    struct.pack_into('<III', header, 36, len(resources), 96 + len(body), len(index))
    return bytes(header + body + index)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.plugins = self.root / 'Plugins'
        self.plugins.mkdir()
        self.backups = self.root / 'backups'
        native = self.plugins / '770-network-addon-mod'
        native.mkdir()
        self.controller = native / 'NetworkAddonMod_Controller.dat'
        self.controller.write_bytes(archive({RUL0: b'native menu\r\n', NETWORK_INI: b'native ini\r\n'}))
        self.native_bytes = self.controller.read_bytes()
        self.unrelated = self.plugins / 'unrelated.txt'
        self.unrelated.write_text('Keep this file exactly.\n')
        self.output = self.make_build('build-v1', b'custom version one')
        verifier_patch = patch('scp.build.verify_build', return_value={'status': 'verified'})
        self.verifier = verifier_patch.start()
        self.addCleanup(verifier_patch.stop)

    def make_build(self, name, payload):
        output = self.root / name
        folder = output / FOLDER
        folder.mkdir(parents=True)
        files = {'00_SCP_Controller_NAM50.dat': archive({RUL0: b'merged ' + payload,
                                                       NETWORK_INI: b'mapped ' + payload}),
                 '10_SCP_Pieces_NAM50.dat': archive({(0x5AD0E817, 0xBADB57F1, 0x5DD0F204): payload})}
        records = []
        for filename, raw in files.items():
            (folder / filename).write_bytes(raw)
            records.append({'path': f'{FOLDER}/{filename}', 'sha256': digest(raw), 'bytes': len(raw)})
        manifest = {'schema_version': 1, 'plugin_folder': FOLDER, 'files': records,
                    'profile': {'id': 'synthetic-nam50-rhd', 'donors': [
                        {'filename': self.controller.name, 'sha256': digest(self.native_bytes)}]}}
        (output / 'manifest.json').write_text(json.dumps(manifest))
        (output / 'README.md').write_text('Build documentation stays outside Plugins.\n')
        return output

    def install(self, output=None, **kwargs):
        return install_build(output or self.output, self.plugins, self.backups, **kwargs)

    def managed_hashes(self):
        folder = self.plugins / FOLDER
        return {p.relative_to(folder).as_posix(): digest(p.read_bytes())
                for p in folder.rglob('*') if p.is_file()}

    def assert_native_untouched(self):
        self.assertEqual(self.controller.read_bytes(), self.native_bytes)
        self.assertEqual(self.unrelated.read_text(), 'Keep this file exactly.\n')

    def assert_clean_rejection(self):
        self.assertFalse((self.plugins / FOLDER).exists())
        self.assertFalse(self.backups.exists())
        self.assert_native_untouched()

    def test_first_install_owns_exact_declared_files_and_receipt(self):
        result = self.install()
        self.verifier.assert_called_once_with(self.output)
        self.assertEqual(result['status'], 'installed')
        actual = set(self.managed_hashes())
        self.assertEqual(actual, {'00_SCP_Controller_NAM50.dat', '10_SCP_Pieces_NAM50.dat', RECEIPT})
        self.assertFalse((self.plugins / 'README.md').exists())
        metadata = json.loads((self.backups / result['backup_id'] / 'backup.json').read_text())
        self.assertEqual(metadata['previous_state'], 'absent')
        self.assert_native_untouched()

    def test_verifier_failure_does_not_write_plugins_or_backups(self):
        self.verifier.side_effect = ValueError('semantic audit failed')
        with self.assertRaisesRegex(ValueError, 'semantic audit'):
            self.install()
        self.assert_clean_rejection()
        self.assertFalse((self.plugins / OPERATION_LOCK).exists())

    def test_existing_operation_lock_is_preserved(self):
        lock = self.plugins / OPERATION_LOCK
        lock.write_text('another operation owns this lock')
        with self.assertRaisesRegex(ValueError, 'Another SCP operation'):
            self.install()
        self.assertEqual(lock.read_text(), 'another operation owns this lock')
        self.assert_clean_rejection()

    def test_parallel_install_is_rejected_while_first_operation_runs(self):
        entered, release = threading.Event(), threading.Event()
        results = []

        def verify(output):
            entered.set()
            if not release.wait(5):
                raise TimeoutError('Test did not release the blocked installer')
            return {}

        def run_first():
            try:
                results.append(self.install())
            except BaseException as exc:
                results.append(exc)

        self.verifier.side_effect = verify
        worker = threading.Thread(target=run_first)
        worker.start()
        try:
            self.assertTrue(entered.wait(5))
            with self.assertRaisesRegex(ValueError, 'Another SCP operation'):
                self.install()
        finally:
            release.set()
            worker.join(5)
        self.assertFalse(worker.is_alive())
        self.assertEqual(len(results), 1)
        self.assertIsInstance(results[0], dict)
        self.assertEqual(results[0]['status'], 'installed')
        self.assertEqual(self.verifier.call_count, 1)
        self.assertFalse((self.plugins / OPERATION_LOCK).exists())

    def test_tampered_build_rejected_even_if_verifier_is_mocked(self):
        (self.output / FOLDER / '10_SCP_Pieces_NAM50.dat').write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'size mismatch|changed files'):
            self.install()
        self.assert_clean_rejection()

    def test_same_size_build_tampering_is_detected(self):
        path = self.output / FOLDER / '10_SCP_Pieces_NAM50.dat'
        raw = path.read_bytes()
        path.write_bytes(raw[:-1] + bytes([raw[-1] ^ 1]))
        with self.assertRaisesRegex(ValueError, 'changed files'):
            self.install()
        self.assert_clean_rejection()

    def test_undeclared_build_file_is_rejected(self):
        (self.output / FOLDER / 'unexpected.dat').write_bytes(b'foreign')
        with self.assertRaisesRegex(ValueError, 'undeclared'):
            self.install()
        self.assert_clean_rejection()

    def test_duplicate_manifest_path_is_rejected(self):
        path = self.output / 'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['files'].append(manifest['files'][0])
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            self.install()
        self.assert_clean_rejection()

    def test_manifest_path_cannot_escape_generated_folder(self):
        path = self.output / 'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['files'][0]['path'] = f'{FOLDER}/../../outside.dat'
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'Unsafe relative'):
            self.install()
        self.assert_clean_rejection()

    def test_nam_fingerprint_mismatch_is_rejected_before_backup(self):
        self.controller.write_bytes(self.native_bytes + b'NAM updated')
        with self.assertRaisesRegex(ValueError, 'fingerprint mismatch'):
            self.install()
        self.assertFalse((self.plugins / FOLDER).exists())
        self.assertFalse(self.backups.exists())
        self.assertEqual(self.controller.read_bytes(), self.native_bytes + b'NAM updated')

    def test_duplicate_named_native_donor_is_rejected(self):
        duplicate = self.plugins / 'other' / self.controller.name
        duplicate.parent.mkdir()
        duplicate.write_bytes(self.native_bytes)
        with self.assertRaisesRegex(ValueError, 'Expected one regular'):
            self.install()
        self.assert_clean_rejection()

    def test_foreign_rul0_or_network_ini_overlay_is_rejected(self):
        for key in (RUL0, NETWORK_INI):
            with self.subTest(key=key):
                foreign = self.plugins / 'zzz_old_standalone_prototype.dat'
                foreign.write_bytes(archive({key: b'old standalone overlay'}))
                with self.assertRaisesRegex(ValueError, 'Foreign shared'):
                    self.install()
                self.assertEqual(foreign.read_bytes(), archive({key: b'old standalone overlay'}))
                foreign.unlink()
                self.assert_clean_rejection()

    def test_foreign_overlay_in_extra_plugins_root_is_rejected(self):
        extra = self.root / 'GamePlugins'
        extra.mkdir()
        for resource in (RUL0, NETWORK_INI):
            with self.subTest(resource=resource):
                foreign = extra / 'old-overlay.dat'
                foreign.write_bytes(archive({resource: b'foreign game installation overlay'}))
                with self.assertRaisesRegex(ValueError, 'Foreign shared'):
                    self.install(extra_roots=[extra])
                self.assert_clean_rejection()

    def test_profile_can_pin_a_donor_in_extra_plugins_root(self):
        extra = self.root / 'GamePlugins'
        extra.mkdir()
        donor = extra / 'High Speed Rail.dat'
        donor.write_bytes(archive({(1, 2, 3): b'synthetic extra-root donor'}))
        path = self.output / 'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['profile']['donors'].append({'filename': donor.name, 'sha256': digest(donor.read_bytes())})
        path.write_text(json.dumps(manifest))
        result = self.install(extra_roots=[extra])
        rollback_install(self.plugins, self.backups, result['backup_id'], extra_roots=[extra])
        self.assertFalse((self.plugins / FOLDER).exists())
        self.assert_native_untouched()

    def test_duplicate_named_donor_across_roots_is_rejected(self):
        extra = self.root / 'GamePlugins'
        extra.mkdir()
        (extra / self.controller.name).write_bytes(self.native_bytes)
        with self.assertRaisesRegex(ValueError, 'Expected one regular'):
            self.install(extra_roots=[extra])
        self.assert_clean_rejection()

    def test_backup_root_inside_extra_plugins_is_rejected(self):
        extra = self.root / 'GamePlugins'
        extra.mkdir()
        with self.assertRaisesRegex(ValueError, 'Backup root must be outside'):
            install_build(self.output, self.plugins, extra / 'backups', extra_roots=[extra])
        self.assert_clean_rejection()

    def test_duplicate_and_nested_extra_roots_are_rejected(self):
        nested = self.plugins / 'nested'
        nested.mkdir()
        for roots in ([self.plugins], [nested]):
            with self.subTest(roots=roots):
                with self.assertRaisesRegex(ValueError, 'Duplicate|Nested'):
                    self.install(extra_roots=roots)
        self.assert_clean_rejection()

    def test_unreceipted_managed_folder_is_never_overwritten(self):
        folder = self.plugins / FOLDER
        folder.mkdir()
        (folder / 'personal.txt').write_text('mine')
        with self.assertRaisesRegex(ValueError, 'no ownership receipt'):
            self.install()
        self.assertEqual((folder / 'personal.txt').read_text(), 'mine')
        self.assertFalse(self.backups.exists())

    def test_changed_missing_and_unknown_owned_files_block_upgrade(self):
        self.install()
        folder = self.plugins / FOLDER
        path = folder / '10_SCP_Pieces_NAM50.dat'
        original = path.read_bytes()
        variants = ('changed', 'missing', 'unknown')
        for variant in variants:
            with self.subTest(variant=variant):
                if variant == 'changed':
                    path.write_bytes(original + b'edit')
                elif variant == 'missing':
                    path.unlink()
                else:
                    (folder / 'personal.txt').write_text('mine')
                before = self.managed_hashes()
                with self.assertRaisesRegex(ValueError, 'unknown, missing or changed'):
                    self.install()
                self.assertEqual(self.managed_hashes(), before)
                if variant == 'unknown':
                    (folder / 'personal.txt').unlink()
                else:
                    path.write_bytes(original)

    def test_backup_root_inside_plugins_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Backup root must be outside'):
            install_build(self.output, self.plugins, self.plugins / 'backups')
        self.assert_clean_rejection()

    def test_backup_root_cannot_contain_plugins(self):
        with self.assertRaisesRegex(ValueError, 'must not contain Plugins'):
            install_build(self.output, self.plugins, self.root)
        self.assert_clean_rejection()

    def test_build_output_inside_plugins_is_rejected(self):
        inside = self.plugins / 'generated'
        shutil.copytree(self.output, inside)
        with self.assertRaisesRegex(ValueError, 'Build output must be outside'):
            install_build(inside, self.plugins, self.backups)
        self.assert_clean_rejection()

    def test_symlinked_build_file_is_rejected(self):
        path = self.output / FOLDER / '10_SCP_Pieces_NAM50.dat'
        real = self.root / 'real.dat'
        path.rename(real)
        path.symlink_to(real)
        with self.assertRaisesRegex(ValueError, 'linked|Symbolic links'):
            self.install()
        self.assert_clean_rejection()

    def test_symlinked_backup_root_and_parent_are_rejected(self):
        real = self.root / 'real-backups'
        real.mkdir()
        link = self.root / 'linked-backups'
        link.symlink_to(real, target_is_directory=True)
        for destination in (link, link / 'nested'):
            with self.subTest(destination=destination):
                with self.assertRaisesRegex(ValueError, 'Symbolic links'):
                    install_build(self.output, self.plugins, destination)
        self.assert_clean_rejection()

    def test_symlinked_managed_folder_is_rejected(self):
        real = self.root / 'personal'
        real.mkdir()
        (self.plugins / FOLDER).symlink_to(real, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Symbolic links'):
            self.install()
        self.assertEqual(list(real.iterdir()), [])
        self.assertFalse(self.backups.exists())

    def test_symlinked_foreign_plugin_directory_is_rejected(self):
        real = self.root / 'foreign'
        real.mkdir()
        (real / 'overlay.dat').write_bytes(archive({RUL0: b'foreign'}))
        (self.plugins / 'linked-mod').symlink_to(real, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Symbolic links|Symlink'):
            self.install()
        self.assert_clean_rejection()

    def test_foreign_scan_allows_local_regular_windows_dll_symlink(self):
        native = self.controller.parent
        for suffix in ('.dll', '.DLL'):
            with self.subTest(suffix=suffix):
                target = native / ('transparent-texture-fix' + suffix)
                raw = b'MZ' + b'synthetic Windows DLL fixture'
                target.write_bytes(raw)
                link = self.plugins / ('memo.transparent-texture-fix' + suffix)
                link.symlink_to(target.relative_to(self.plugins))
                _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller)
                self.assertTrue(link.is_symlink())
                self.assertEqual(target.read_bytes(), raw)
                link.unlink()
                target.unlink()
        self.assert_clean_rejection()

    def test_foreign_scan_allows_dll_target_in_explicit_extra_root(self):
        extra = self.root / 'GamePlugins'
        extra.mkdir()
        target = extra / 'native-fix.dll'
        target.write_bytes(b'MZ synthetic native fix')
        link = self.plugins / 'memo.native-fix.dll'
        link.symlink_to(target)
        _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller,
                          extra_roots=[extra])
        self.assertTrue(link.is_symlink())
        self.assertEqual(target.read_bytes(), b'MZ synthetic native fix')
        self.assert_clean_rejection()

    def test_foreign_scan_rejects_dll_target_outside_active_roots(self):
        target = self.root / 'external-fix.dll'
        target.write_bytes(b'MZ synthetic external fix')
        (self.plugins / 'memo.external-fix.dll').symlink_to(target)
        with self.assertRaisesRegex(ValueError, 'Symbolic links|Symlink'):
            _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller)
        self.assertEqual(target.read_bytes(), b'MZ synthetic external fix')
        self.assert_clean_rejection()

    def test_foreign_scan_rejects_dangling_dll_symlink(self):
        link = self.plugins / 'memo.missing-fix.dll'
        link.symlink_to(self.controller.parent / 'missing-fix.dll')
        with self.assertRaisesRegex(ValueError, 'Symbolic links|Symlink'):
            _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller)
        self.assertTrue(link.is_symlink())
        self.assert_clean_rejection()

    def test_foreign_scan_rejects_dll_symlink_to_directory(self):
        target = self.plugins / 'directory-named.dll'
        target.mkdir()
        (target / 'overlay.dat').write_bytes(archive({RUL0: b'hidden controller'}))
        (self.plugins / 'memo.directory.dll').symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Symbolic links|Symlink'):
            _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller)
        self.assert_clean_rejection()

    def test_foreign_scan_rejects_linked_data_plugins(self):
        for suffix in ('.dat', '.SC4Model', '.SC4Lot', '.SC4Desc'):
            with self.subTest(suffix=suffix):
                target = self.controller.parent / ('native-piece' + suffix)
                target.write_bytes(archive({(1, 2, 3): b'piece resource'}))
                link = self.plugins / ('linked-piece' + suffix)
                link.symlink_to(target)
                with self.assertRaisesRegex(ValueError, 'Symbolic links|Symlink'):
                    _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller)
                self.assertTrue(link.is_symlink())
                link.unlink()
                target.unlink()
        self.assert_clean_rejection()

    def test_foreign_scan_rejects_dll_named_alias_to_data_archive(self):
        target = self.controller.parent / 'hidden-overlay.dat'
        target.write_bytes(archive({RUL0: b'hidden controller'}))
        (self.plugins / 'memo.hidden-overlay.dll').symlink_to(target)
        with self.assertRaisesRegex(ValueError, 'Symbolic links|Symlink'):
            _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller)
        self.assert_clean_rejection()

    def test_foreign_scan_rejects_dbpf_disguised_as_dll(self):
        target = self.controller.parent / 'disguised-overlay.dll'
        target.write_bytes(archive({RUL0: b'hidden controller'}))
        (self.plugins / 'memo.disguised-overlay.dll').symlink_to(target)
        with self.assertRaisesRegex(ValueError, 'Symbolic links|Symlink'):
            _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller)
        self.assert_clean_rejection()

    def test_foreign_scan_rejects_dll_target_in_managed_folder(self):
        managed = self.plugins / FOLDER
        managed.mkdir()
        target = managed / 'owned-fix.dll'
        target.write_bytes(b'MZ synthetic owned fix')
        link = self.plugins / 'memo.owned-fix.dll'
        link.symlink_to(target)
        with self.assertRaisesRegex(ValueError, 'Symbolic links|Symlink'):
            _foreign_overlays(self.plugins, managed, self.controller)
        self.assertTrue(link.is_symlink())
        self.assertEqual(target.read_bytes(), b'MZ synthetic owned fix')
        self.assertFalse(self.backups.exists())
        self.assert_native_untouched()

    def test_foreign_scan_rejects_non_dll_link_to_dll(self):
        target = self.controller.parent / 'native-fix.dll'
        target.write_bytes(b'MZ synthetic native fix')
        (self.plugins / 'native-fix.dat').symlink_to(target)
        with self.assertRaisesRegex(ValueError, 'Symbolic links|Symlink'):
            _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller)
        self.assert_clean_rejection()

    def test_foreign_scan_valid_dll_link_still_rejects_foreign_overlay(self):
        target = self.controller.parent / 'native-fix.dll'
        target.write_bytes(b'MZ synthetic native fix')
        link = self.plugins / 'memo.native-fix.dll'
        link.symlink_to(target)
        for key in (RUL0, NETWORK_INI):
            with self.subTest(key=key):
                foreign = self.plugins / 'foreign-overlay.dat'
                raw = archive({key: b'foreign controller overlay'})
                foreign.write_bytes(raw)
                with self.assertRaisesRegex(ValueError, 'Foreign shared'):
                    _foreign_overlays(self.plugins, self.plugins / FOLDER, self.controller)
                self.assertEqual(foreign.read_bytes(), raw)
                self.assertTrue(link.is_symlink())
                foreign.unlink()
        self.assert_clean_rejection()

    def test_valid_dll_symlink_does_not_block_verified_install(self):
        target = self.controller.parent / 'native-fix.dll'
        raw = b'MZ synthetic native fix'
        target.write_bytes(raw)
        link = self.plugins / 'memo.native-fix.dll'
        link.symlink_to(target.relative_to(self.plugins))
        result = self.install()
        self.assertEqual(result['status'], 'installed')
        self.assertTrue(link.is_symlink())
        self.assertEqual(target.read_bytes(), raw)
        self.assert_native_untouched()

    def test_upgrade_and_rollback_restore_previous_files_and_receipt_exactly(self):
        first = self.install()
        previous = self.managed_hashes()
        output2 = self.make_build('build-v2', b'custom version two')
        second = self.install(output2)
        self.assertNotEqual(first['backup_id'], second['backup_id'])
        self.assertNotEqual(previous, self.managed_hashes())
        result = rollback_install(self.plugins, self.backups, second['backup_id'])
        self.assertEqual(result['previous_state'], 'present')
        self.assertEqual(previous, self.managed_hashes())
        self.assert_native_untouched()
        rollback_install(self.plugins, self.backups, first['backup_id'])
        self.assertFalse((self.plugins / FOLDER).exists())

    def test_upgrade_cannot_omit_installed_piece_ids(self):
        path = self.output / 'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['pieces'] = [{'id': 'hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg'}, {'id': 'hsr-l2-over-tram-ground-mixed-crossing-90deg'}]
        path.write_text(json.dumps(manifest))
        self.install()
        receipt = json.loads((self.plugins / FOLDER / RECEIPT).read_text())
        self.assertEqual(receipt['piece_ids'], ['hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg', 'hsr-l2-over-tram-ground-mixed-crossing-90deg'])
        subset = self.make_build('subset-build', b'only diagonal piece')
        path = subset / 'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['pieces'] = [{'id': 'hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg'}]
        path.write_text(json.dumps(manifest))
        before, backups = self.managed_hashes(), set(self.backups.iterdir())
        with self.assertRaisesRegex(ValueError, 'New build omits installed pieces.*saved cities'):
            self.install(subset)
        self.assertEqual(before, self.managed_hashes())
        self.assertEqual(backups, set(self.backups.iterdir()))

    def test_upgrade_can_add_pieces_without_dropping_existing_ids(self):
        path = self.output / 'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['pieces'] = [{'id': 'hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg'}]
        path.write_text(json.dumps(manifest))
        self.install()
        superset = self.make_build('superset-build', b'diagonal plus tram')
        path = superset / 'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['pieces'] = [{'id': 'hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg'}, {'id': 'hsr-l2-over-tram-ground-mixed-crossing-90deg'}]
        path.write_text(json.dumps(manifest))
        result = self.install(superset)
        self.assertEqual(result['status'], 'installed')
        receipt = json.loads((self.plugins / FOLDER / RECEIPT).read_text())
        self.assertEqual(receipt['piece_ids'], ['hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg', 'hsr-l2-over-tram-ground-mixed-crossing-90deg'])

    def test_receipt_piece_dat_paths_independently_prevent_silent_piece_removal(self):
        path = self.output / 'manifest.json'
        manifest = json.loads(path.read_text())
        raw = archive({(1, 2, 3): b'tram piece asset'})
        relative = f'{FOLDER}/20_Pieces/SCP_hsr-l2-over-tram-ground-mixed-crossing-90deg.dat'
        donor = self.output / relative
        donor.parent.mkdir()
        donor.write_bytes(raw)
        manifest['files'].append({'path': relative, 'sha256': digest(raw), 'bytes': len(raw)})
        path.write_text(json.dumps(manifest))
        self.install()
        receipt_path = self.plugins / FOLDER / RECEIPT
        receipt = json.loads(receipt_path.read_text())
        del receipt['piece_ids']
        receipt_path.write_text(json.dumps(receipt))
        subset = self.make_build('subset-build', b'only diagonal piece')
        before = self.managed_hashes()
        with self.assertRaisesRegex(ValueError, 'New build omits installed pieces.*SCP_hsr-l2-over-tram-ground-mixed-crossing-90deg.dat'):
            self.install(subset)
        self.assertEqual(before, self.managed_hashes())

    def test_first_install_rollback_removes_only_owned_folder(self):
        result = self.install()
        rollback = rollback_install(self.plugins, self.backups, result['backup_id'])
        self.assertEqual(rollback['status'], 'rolled_back')
        self.assertEqual(rollback['previous_state'], 'absent')
        self.assertFalse((self.plugins / FOLDER).exists())
        self.assert_native_untouched()

    def test_first_install_rollback_removes_stale_overlay_after_nam_update(self):
        result = self.install()
        updated = self.native_bytes + b'NAM updated after installing'
        self.controller.write_bytes(updated)
        rollback_install(self.plugins, self.backups, result['backup_id'])
        self.assertFalse((self.plugins / FOLDER).exists())
        self.assertEqual(self.controller.read_bytes(), updated)
        self.assertEqual(self.unrelated.read_text(), 'Keep this file exactly.\n')

    def test_rollback_cannot_restore_previous_overlay_after_nam_update(self):
        self.install()
        second = self.install(self.make_build('build-v2', b'v2'))
        self.controller.write_bytes(self.native_bytes + b'NAM update')
        before = self.managed_hashes()
        with self.assertRaisesRegex(ValueError, 'fingerprint mismatch'):
            rollback_install(self.plugins, self.backups, second['backup_id'])
        self.assertEqual(before, self.managed_hashes())

    def test_uninstall_and_rollback_restore_exact_files_and_receipt(self):
        self.install()
        previous = self.managed_hashes()
        result = uninstall(self.plugins, self.backups)
        self.assertEqual(result['status'], 'uninstalled')
        self.assertFalse((self.plugins / FOLDER).exists())
        snapshot = self.backups / result['backup_id'] / 'previous' / FOLDER
        self.assertEqual(previous, {p.relative_to(snapshot).as_posix(): digest(p.read_bytes())
                                    for p in snapshot.rglob('*') if p.is_file()})
        rollback_install(self.plugins, self.backups, result['backup_id'])
        self.assertEqual(previous, self.managed_hashes())
        self.assert_native_untouched()

    def test_uninstall_removes_stale_upgrade_without_restoring_old_overlay(self):
        self.install()
        self.install(self.make_build('build-v2', b'v2'))
        updated = self.native_bytes + b'NAM update'
        self.controller.write_bytes(updated)
        result = uninstall(self.plugins, self.backups)
        self.assertFalse((self.plugins / FOLDER).exists())
        self.assertEqual(self.controller.read_bytes(), updated)
        with self.assertRaisesRegex(ValueError, 'fingerprint mismatch'):
            rollback_install(self.plugins, self.backups, result['backup_id'])
        self.assertFalse((self.plugins / FOLDER).exists())

    def test_uninstall_refuses_unknown_changed_and_unreceipted_files(self):
        self.install()
        folder = self.plugins / FOLDER
        (folder / 'personal.txt').write_text('mine')
        before = self.managed_hashes()
        backups = set(self.backups.iterdir())
        with self.assertRaisesRegex(ValueError, 'unknown, missing or changed'):
            uninstall(self.plugins, self.backups)
        self.assertEqual(before, self.managed_hashes())
        self.assertEqual(backups, set(self.backups.iterdir()))

    def test_uninstall_rollback_refuses_new_managed_installation(self):
        self.install()
        removed = uninstall(self.plugins, self.backups)
        self.install()
        before = self.managed_hashes()
        with self.assertRaisesRegex(ValueError, 'remain absent'):
            rollback_install(self.plugins, self.backups, removed['backup_id'])
        self.assertEqual(before, self.managed_hashes())

    def test_restore_rollback_refuses_a_new_foreign_overlay(self):
        self.install()
        second = self.install(self.make_build('build-v2', b'v2'))
        (self.plugins / 'new-foreign-overlay.dat').write_bytes(archive({RUL0: b'foreign'}))
        before = self.managed_hashes()
        with self.assertRaisesRegex(ValueError, 'Foreign shared'):
            rollback_install(self.plugins, self.backups, second['backup_id'])
        self.assertEqual(before, self.managed_hashes())

    def test_removal_can_resolve_a_new_foreign_overlay_conflict(self):
        self.install()
        foreign = self.plugins / 'new-foreign-overlay.dat'
        foreign.write_bytes(archive({RUL0: b'foreign'}))
        raw = foreign.read_bytes()
        uninstall(self.plugins, self.backups)
        self.assertFalse((self.plugins / FOLDER).exists())
        self.assertEqual(foreign.read_bytes(), raw)
        self.assert_native_untouched()

    def test_rollback_refuses_changed_current_file(self):
        result = self.install()
        (self.plugins / FOLDER / '10_SCP_Pieces_NAM50.dat').write_bytes(b'personal edit')
        before = self.managed_hashes()
        with self.assertRaisesRegex(ValueError, 'unknown, missing or changed'):
            rollback_install(self.plugins, self.backups, result['backup_id'])
        self.assertEqual(before, self.managed_hashes())

    def test_rollback_refuses_backup_from_different_install(self):
        first = self.install()
        self.install(self.make_build('build-v2', b'v2'))
        before = self.managed_hashes()
        with self.assertRaisesRegex(ValueError, 'does not belong'):
            rollback_install(self.plugins, self.backups, first['backup_id'])
        self.assertEqual(before, self.managed_hashes())

    def test_rollback_refuses_tampered_previous_snapshot(self):
        self.install()
        second = self.install(self.make_build('build-v2', b'v2'))
        snapshot = self.backups / second['backup_id'] / 'previous' / FOLDER
        (snapshot / '10_SCP_Pieces_NAM50.dat').write_bytes(b'corrupt backup')
        before = self.managed_hashes()
        with self.assertRaisesRegex(ValueError, 'Backup snapshot'):
            rollback_install(self.plugins, self.backups, second['backup_id'])
        self.assertEqual(before, self.managed_hashes())

    def test_rollback_rejects_path_traversal_in_backup_id(self):
        result = self.install()
        before = self.managed_hashes()
        with self.assertRaisesRegex(ValueError, 'Invalid backup identifier'):
            rollback_install(self.plugins, self.backups, '../' + result['backup_id'])
        self.assertEqual(before, self.managed_hashes())

    def test_exchange_failure_restores_old_managed_folder(self):
        self.install()
        previous = self.managed_hashes()
        output2 = self.make_build('build-v2', b'v2')
        real_rename = Path.rename

        def fail_staged_rename(path, destination):
            if path.name.startswith('.scp-stage-'):
                raise OSError('simulated directory exchange failure')
            return real_rename(path, destination)

        with patch.object(Path, 'rename', fail_staged_rename):
            with self.assertRaisesRegex(OSError, 'simulated'):
                self.install(output2)
        self.assertEqual(previous, self.managed_hashes())
        self.assertFalse(any(p.name.startswith('.scp-') for p in self.plugins.iterdir()))
        self.assert_native_untouched()


if __name__ == '__main__':
    unittest.main()
