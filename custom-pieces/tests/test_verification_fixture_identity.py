"""Declared subject aliases do not weaken frozen resource-descriptor checks."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from scp import jsonc
from scp.dbpf import pack_dbpf, tgi_string
from scp.verification_fixtures import resource_descriptor, verification_resources


class VerificationFixtureIdentityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='scp-resource-descriptor-alias-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.directory = self.root / 'build'
        self.directory.mkdir()
        self.old_piece, self.new_piece = 'historical-track', 'hsr-l2-two-track-straight'
        self.old_assembly, self.new_assembly = 'historical-layout', 'hsr-trumpet-straight-stem'
        self.recipe = 'original_recipe'
        ledger = self.root / 'config/subject-id-migration.jsonc'
        ledger.parent.mkdir()
        jsonc.dump(ledger, {'schema_version': 1,
            'pieces': [{'old_id': self.old_piece, 'new_id': self.new_piece,
                        'recipe': self.recipe, 'domain': 'high-speed-rail'}],
            'assemblies': [{'old_id': self.old_assembly, 'new_id': self.new_assembly,
                            'domain': 'high-speed-rail'}]},
            title='Declared identity migration', summary='Keep synthetic resource facts unchanged.')
        self.resources = {(0x5ad0e817, 0xbadb57f1, 0x7f500000): b'unchanged model',
                          (0x296678f7, 0xa966883f, 0x7f500000): b'unchanged path'}
        raw = pack_dbpf(self.resources)
        self.asset = 'pieces/historical-track.dat'
        archive = self.directory / self.asset
        archive.parent.mkdir()
        archive.write_bytes(raw)
        self.piece = {'id': self.old_piece, 'recipe': self.recipe,
                      'asset_file': self.asset, 'bytes': len(raw),
                      'sha256': hashlib.sha256(raw).hexdigest(),
                      'resource_count': len(self.resources),
                      'resource_sha256': {tgi_string(key): hashlib.sha256(value).hexdigest()
                                          for key, value in self.resources.items()}}
        self.descriptor = {'schema_version': 3, 'id': 'historical-layout-resources',
                           'assembly_id': self.old_assembly, 'pieces': [self.piece]}
        self.manifest = {'pieces': [{'id': self.new_piece, 'recipe': self.recipe,
                                    'asset_file': self.asset}]}
        self.descriptor_path = self.root / 'checks/resources.json'
        self.descriptor_path.parent.mkdir()
        self.save()

    def save(self):
        self.descriptor_path.write_text(json.dumps(self.descriptor) + '\n', encoding='utf-8')
        (self.directory / 'manifest.json').write_text(json.dumps(self.manifest) + '\n', encoding='utf-8')

    def verify(self, **options):
        arguments = {'selected_piece_ids': [self.new_piece], 'assembly_id': self.new_assembly,
                     'root': self.root}
        arguments.update(options)
        return verification_resources(self.descriptor_path, self.directory, **arguments)

    def test_declared_piece_and_assembly_aliases_preserve_original_descriptor_bytes(self):
        before = {path: path.read_bytes() for path in self.root.rglob('*') if path.is_file()}
        self.assertEqual(self.verify(), self.directory)
        self.assertEqual(resource_descriptor(self.descriptor_path), self.descriptor)
        self.assertEqual(resource_descriptor(self.descriptor_path)['pieces'][0]['id'], self.old_piece)
        self.assertEqual(before, {path: path.read_bytes() for path in self.root.rglob('*') if path.is_file()})

    def test_a_preserved_old_id_manifest_matches_only_the_declared_current_selection(self):
        self.manifest['pieces'][0]['id'] = self.old_piece
        self.save()
        self.assertEqual(self.verify(), self.directory)
        self.assertEqual(self.verify(selected_piece_ids=[self.old_piece], assembly_id=self.old_assembly),
                         self.directory)

    def test_current_descriptor_and_preserved_old_manifest_use_the_same_exact_alias(self):
        self.piece['id'] = self.new_piece
        self.descriptor['assembly_id'] = self.new_assembly
        self.manifest['pieces'][0]['id'] = self.old_piece
        self.save()
        self.assertEqual(self.verify(), self.directory)

    def test_unlisted_piece_or_assembly_identifiers_are_never_guessed(self):
        for options in ({'selected_piece_ids': ['historical-track-almost']},
                        {'assembly_id': 'historical-layout-almost'}):
            with self.subTest(options=options), self.assertRaisesRegex(ValueError, 'identit'):
                self.verify(**options)
        self.manifest['pieces'][0]['id'] = 'historical-track-almost'
        self.save()
        with self.assertRaisesRegex(ValueError, 'identity.*differs'):
            self.verify()

    def test_declared_alias_never_changes_a_recipe_or_asset_filename(self):
        for key, value in (('recipe', 'different_recipe'),
                           ('asset_file', 'pieces/hsr-l2-two-track-straight.dat')):
            original = self.manifest['pieces'][0][key]
            with self.subTest(key=key):
                self.manifest['pieces'][0][key] = value
                self.save()
                with self.assertRaisesRegex(ValueError, 'identity, recipe or asset path differs'):
                    self.verify()
            self.manifest['pieces'][0][key] = original

    def test_changed_archive_bytes_remain_rejected_for_a_declared_alias(self):
        path = self.directory / self.asset
        path.write_bytes(path.read_bytes() + b'changed')
        with self.assertRaisesRegex(ValueError, 'archive bytes changed'):
            self.verify()

    def test_changed_resource_hashes_remain_rejected_after_archive_repinning(self):
        changed = dict(self.resources)
        changed[next(iter(changed))] = b'changed model'
        raw = pack_dbpf(changed)
        (self.directory / self.asset).write_bytes(raw)
        self.piece.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        self.save()
        with self.assertRaisesRegex(ValueError, 'decompressed resource hashes differ'):
            self.verify()

    def test_changed_numeric_resource_identity_is_not_an_identity_alias(self):
        changed = dict(self.resources)
        previous = next(iter(changed))
        changed[previous[0], previous[1], previous[2] + 0x100] = changed.pop(previous)
        raw = pack_dbpf(changed)
        (self.directory / self.asset).write_bytes(raw)
        self.piece.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        self.save()
        with self.assertRaisesRegex(ValueError, 'decompressed resource hashes differ'):
            self.verify()

    def test_old_and_current_ids_cannot_duplicate_one_selected_subject(self):
        with self.assertRaisesRegex(ValueError, 'unique after declared aliases'):
            self.verify(selected_piece_ids=[self.old_piece, self.new_piece])

    def test_old_and_current_ids_cannot_duplicate_one_manifest_subject(self):
        self.manifest['pieces'].append({'id': self.old_piece, 'recipe': self.recipe,
                                        'asset_file': 'pieces/another.dat'})
        self.save()
        with self.assertRaisesRegex(ValueError, 'duplicate piece identities after declared aliases'):
            self.verify()

    def test_old_and_current_ids_cannot_duplicate_one_descriptor_subject(self):
        other = deepcopy(self.piece)
        other.update(id=self.new_piece, asset_file='pieces/another.dat')
        self.descriptor['pieces'].append(other)
        self.save()
        with self.assertRaisesRegex(ValueError, 'duplicate piece identities after declared aliases'):
            self.verify()

    def test_optional_absent_build_still_checks_exact_declared_selection(self):
        absent = self.root / 'not-built'
        self.assertIsNone(verification_resources(self.descriptor_path, absent,
                          selected_piece_ids=[self.new_piece], assembly_id=self.new_assembly,
                          required=False, root=self.root))
        with self.assertRaisesRegex(ValueError, 'selected identities differ'):
            verification_resources(self.descriptor_path, absent,
                                   selected_piece_ids=['unlisted-track'], required=False, root=self.root)


if __name__ == '__main__':
    unittest.main()
