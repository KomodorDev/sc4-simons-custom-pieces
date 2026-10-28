"""Subject renames preserve installation ownership, omission guards, and recovery."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scp import jsonc
from scp.dbpf import pack_dbpf
from scp.install import (FOLDER, RECEIPT, OPERATION_LOCK, RUL0, NETWORK_INI,
                         install_build, rollback_install)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class InstallIdentityMigrationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='scp-install-identity-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.source = self.root / 'source'
        config = self.source / 'config'
        config.mkdir(parents=True)
        self.old_id = 'historical-piece'
        self.new_id = 'hsr-l2-single-track-oneway-straight'
        jsonc.dump(config / 'subject-id-migration.jsonc', {
            'schema_version': 1, 'pieces': [{
                'old_id': self.old_id, 'new_id': self.new_id,
                'recipe': 'original_recipe', 'domain': 'high-speed-rail'}],
            'assemblies': []}, title='Declared subject migration',
            summary='Rename only this synthetic piece; preserve its resources and ownership.')
        self.plugins = self.root / 'Plugins'
        native = self.plugins / 'native'
        native.mkdir(parents=True)
        self.controller = native / 'NetworkAddonMod_Controller.dat'
        self.native = pack_dbpf({RUL0: b'native controller', NETWORK_INI: b'native network ini'})
        self.controller.write_bytes(self.native)
        self.backups = self.root / 'backups'
        self.resources = {(0x5ad0e817, 0xbadb57f1, 0x7f500000): b'unchanged model',
                          (0x296678f7, 0xa966883f, 0x7f500000): b'unchanged path'}
        self.archive = pack_dbpf(self.resources)
        verifier = patch('scp.build.verify_build', return_value={'status': 'verified'})
        verifier.start()
        self.addCleanup(verifier.stop)

    def build(self, label, *, identifiers=None, filenames=None):
        identifiers = [self.old_id] if identifiers is None else identifiers
        if filenames is None:
            filenames = [f'20_Pieces/SCP_{identifier}.dat' for identifier in identifiers]
        return self._build(label, identifiers, filenames)

    def _build(self, label, identifiers, filenames):
        output = self.root / label
        folder = output / FOLDER
        folder.mkdir(parents=True)
        payloads = {'00_SCP_Controller_NAM50.dat': pack_dbpf({RUL0: b'combined controller',
                                                            NETWORK_INI: b'combined network ini'})}
        payloads.update({name: self.archive for name in filenames})
        records = []
        for relative, raw in payloads.items():
            path = folder / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
            records.append({'path': f'{FOLDER}/{relative}', 'bytes': len(raw), 'sha256': digest(raw)})
        manifest = {'schema_version': 1, 'plugin_folder': FOLDER,
                    'pieces': [{'id': identifier} for identifier in identifiers],
                    'files': records, 'profile': {'donors': [{
                        'filename': self.controller.name, 'sha256': digest(self.native)}]}}
        (output / 'manifest.json').write_text(json.dumps(manifest), encoding='utf-8')
        return output

    def install(self, output):
        return install_build(output, self.plugins, self.backups, source_root=self.source)

    def snapshot(self):
        return {path.relative_to(self.plugins / FOLDER).as_posix(): path.read_bytes()
                for path in (self.plugins / FOLDER).rglob('*') if path.is_file()}

    def assert_rejected_unchanged(self, output, message):
        before = self.snapshot()
        backups = {path.name for path in self.backups.iterdir()}
        with self.assertRaisesRegex(ValueError, message):
            self.install(output)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual({path.name for path in self.backups.iterdir()}, backups)
        self.assertEqual(self.controller.read_bytes(), self.native)
        self.assertFalse((self.plugins / OPERATION_LOCK).exists())

    def test_declared_id_and_dat_rename_install_and_rollback_preserve_exact_old_state(self):
        self.install(self.build('old'))
        previous = self.snapshot()
        result = self.install(self.build('new', identifiers=[self.new_id]))
        current = self.snapshot()
        self.assertNotIn(f'20_Pieces/SCP_{self.old_id}.dat', current)
        self.assertEqual(current[f'20_Pieces/SCP_{self.new_id}.dat'], self.archive)
        self.assertEqual(json.loads(current[RECEIPT])['piece_ids'], [self.new_id])
        backup = self.backups / result['backup_id'] / 'previous' / FOLDER
        self.assertEqual((backup / RECEIPT).read_bytes(), previous[RECEIPT])
        self.assertEqual((backup / f'20_Pieces/SCP_{self.old_id}.dat').read_bytes(), self.archive)
        rollback_install(self.plugins, self.backups, result['backup_id'])
        self.assertEqual(self.snapshot(), previous)
        self.assertEqual(self.controller.read_bytes(), self.native)

    def test_dat_ownership_alone_accepts_only_the_exact_declared_basename_alias(self):
        self.install(self.build('old'))
        receipt_path = self.plugins / FOLDER / RECEIPT
        receipt = json.loads(receipt_path.read_text())
        del receipt['piece_ids']
        receipt_path.write_text(json.dumps(receipt), encoding='utf-8')
        previous_receipt = receipt_path.read_bytes()
        result = self.install(self.build('new', identifiers=[self.new_id]))
        self.assertEqual((self.backups / result['backup_id'] / 'previous' / FOLDER / RECEIPT).read_bytes(),
                         previous_receipt)

    def test_receipt_identity_alone_accepts_the_declared_alias(self):
        self.install(self._build('old', [self.old_id], []))
        self.assertEqual(self.install(self._build('new', [self.new_id], []))['status'], 'installed')

    def test_alias_never_permits_omitting_the_piece(self):
        self.install(self.build('old'))
        self.assert_rejected_unchanged(self._build('new', [], []), 'omits installed pieces')

    def test_unknown_installed_piece_still_blocks_replacement(self):
        self.install(self.build('old', identifiers=['unlisted-piece']))
        self.assert_rejected_unchanged(self.build('new', identifiers=[self.new_id]),
                                       'omits installed pieces.*unlisted-piece')

    def test_unknown_dat_suffix_is_not_a_declared_piece_alias(self):
        old_path = f'20_Pieces/SCP_{self.old_id}-extra.dat'
        self.install(self._build('old', [self.old_id], [old_path]))
        self.assert_rejected_unchanged(self.build('new', identifiers=[self.new_id]),
                                       'omits installed pieces.*historical-piece-extra')

    def test_nested_dat_path_is_not_treated_as_a_known_piece_basename(self):
        old_path = f'20_Pieces/SCP_{self.old_id}.dat/nested.dat'
        self.install(self._build('old', [self.old_id], [old_path]))
        self.assert_rejected_unchanged(self.build('new', identifiers=[self.new_id]),
                                       'omits installed pieces.*nested.dat')

    def test_case_changed_basename_is_not_a_declared_alias(self):
        self.install(self._build('old', [self.old_id], ['20_Pieces/SCP_Historical-piece.dat']))
        self.assert_rejected_unchanged(self.build('new', identifiers=[self.new_id]),
                                       'omits installed pieces.*Historical-piece.dat')

    def test_alias_cannot_hide_changed_receipt_owned_archive_bytes(self):
        self.install(self.build('old'))
        path = self.plugins / FOLDER / f'20_Pieces/SCP_{self.old_id}.dat'
        path.write_bytes(path.read_bytes() + b'unowned change')
        self.assert_rejected_unchanged(self.build('new', identifiers=[self.new_id]),
                                       'unknown, missing or changed files')

    def test_alias_cannot_hide_an_unowned_file(self):
        self.install(self.build('old'))
        (self.plugins / FOLDER / 'unowned.txt').write_bytes(b'keep this unowned file')
        self.assert_rejected_unchanged(self.build('new', identifiers=[self.new_id]),
                                       'unknown, missing or changed files')

    def test_alias_cannot_hide_changed_build_archive_hashes(self):
        self.install(self.build('old'))
        output = self.build('new', identifiers=[self.new_id])
        path = output / FOLDER / f'20_Pieces/SCP_{self.new_id}.dat'
        path.write_bytes(path.read_bytes().replace(b'unchanged model', b'changedxx model'))
        self.assert_rejected_unchanged(output, 'undeclared, missing or changed files')

    def test_old_and_current_archive_names_cannot_duplicate_one_declared_identity(self):
        self.install(self.build('old'))
        output = self._build('new', [self.new_id], [f'20_Pieces/SCP_{self.old_id}.dat',
                                                  f'20_Pieces/SCP_{self.new_id}.dat'])
        self.assert_rejected_unchanged(output, 'duplicate identities after declared aliases')


if __name__ == '__main__':
    unittest.main()
