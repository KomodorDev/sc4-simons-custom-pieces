"""Current resource descriptors reject missing, stale and unsafe build inputs."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import struct
import tempfile
import unittest

from scp.dbpf import pack_dbpf, tgi_string
from scp.verification_fixtures import resource_descriptor, verification_resources


class VerificationResourceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.directory = self.root/'build'
        self.directory.mkdir()
        self.descriptor_path = self.root/'checks/resources.json'
        self.descriptor_path.parent.mkdir()
        self.pieces = []
        for number in range(3):
            resources = {(0x5ad0e817, number, 1): f'current model {number}'.encode(),
                         (0x296678f7, number, 2): f'current path {number}'.encode()}
            name = f'pieces/track-{number}.dat'
            raw = pack_dbpf(resources)
            path = self.directory/name
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(raw)
            self.pieces.append({'id': f'track-{number}', 'recipe': f'track_{number}',
                                'asset_file': name, 'bytes': len(raw),
                                'sha256': hashlib.sha256(raw).hexdigest(),
                                'resource_count': len(resources),
                                'resource_sha256': {tgi_string(key): hashlib.sha256(value).hexdigest()
                                                    for key, value in resources.items()}})
        self.descriptor = {'schema_version': 3, 'id': 'current-assembly-resources',
                           'assembly_id': 'current-assembly', 'pieces': self.pieces,
                           'purpose': 'Current exact resources; no copied archives.',
                           'physical_observation': {'world_cells': 42}}
        self.manifest = {'pieces': [{key: piece[key] for key in ('id', 'recipe', 'asset_file')}
                                    for piece in self.pieces], 'documentation': []}
        self.save()

    def save(self):
        self.descriptor_path.write_text(json.dumps(self.descriptor))
        (self.directory/'manifest.json').write_text(json.dumps(self.manifest))

    def verify(self, **options):
        return verification_resources(self.descriptor_path, self.directory, **options)

    def repin_archive(self, index=0):
        piece = self.pieces[index]
        raw = (self.directory/piece['asset_file']).read_bytes()
        piece.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        self.save()

    def test_exact_current_resources_and_explicit_selection_pass(self):
        self.assertEqual(self.verify(selected_piece_ids=['track-2', 'track-0', 'track-1'],
                                     assembly_id='current-assembly'), self.directory.resolve())
        self.assertEqual(resource_descriptor(self.descriptor_path), self.descriptor)

    def test_piece_count_is_generic_and_resource_map_is_optional(self):
        self.descriptor['pieces'] = [dict(self.pieces[0])]
        self.descriptor['pieces'][0].pop('resource_sha256')
        self.manifest['pieces'] = self.manifest['pieces'][:1]
        self.save()
        self.assertEqual(self.verify(), self.directory.resolve())

    def test_current_build_may_include_documentation_and_other_package_resources(self):
        (self.directory/'README.md').write_text('Current instructions.')
        (self.directory/'controller.dat').write_bytes(b'checked by whole-package verifier')
        self.assertEqual(self.verify(), self.directory.resolve())

    def test_only_explicit_optional_absent_build_can_skip(self):
        absent = self.root/'not-built'
        self.assertIsNone(verification_resources(self.descriptor_path, absent, required=False))
        with self.assertRaises(FileNotFoundError):
            verification_resources(self.descriptor_path, absent)

    def test_missing_descriptor_never_skips_even_with_absent_optional_build(self):
        self.descriptor_path.unlink()
        with self.assertRaises(FileNotFoundError):
            verification_resources(self.descriptor_path, self.root/'absent', required=False)

    def test_malformed_descriptor_never_skips_even_with_absent_optional_build(self):
        self.descriptor_path.write_text('{"schema_version":')
        with self.assertRaisesRegex(ValueError, 'Malformed'):
            verification_resources(self.descriptor_path, self.root/'absent', required=False)

    def test_descriptor_requires_current_schema_and_identity(self):
        for key, value in (('schema_version', 2), ('schema_version', True),
                           ('id', ''), ('assembly_id', None), ('pieces', []), ('pieces', {})):
            with self.subTest(key=key, value=value):
                original = deepcopy(self.descriptor)
                self.descriptor[key] = value
                self.save()
                with self.assertRaises(ValueError):
                    self.verify(required=False)
                self.descriptor = original

    def test_duplicate_json_property_is_not_silently_accepted(self):
        self.descriptor_path.write_text('{"schema_version": 2, "schema_version": 3}')
        with self.assertRaisesRegex(ValueError, 'Duplicate JSON'):
            self.verify(required=False)

    def test_archive_metadata_requires_real_positive_counts_and_sha256(self):
        for key, value in (('bytes', 0), ('bytes', True), ('bytes', 1.5),
                           ('resource_count', -1), ('resource_count', True),
                           ('sha256', '0'*63), ('sha256', 'A'*64)):
            with self.subTest(key=key, value=value):
                original = self.pieces[0][key]
                self.pieces[0][key] = value
                self.save()
                with self.assertRaises(ValueError):
                    self.verify()
                self.pieces[0][key] = original

    def test_duplicate_piece_identities_and_asset_paths_fail(self):
        for key in ('id', 'asset_file'):
            with self.subTest(key=key):
                original = self.pieces[1][key]
                self.pieces[1][key] = self.pieces[0][key]
                self.save()
                with self.assertRaisesRegex(ValueError, 'duplicate'):
                    self.verify()
                self.pieces[1][key] = original

    def test_descriptor_asset_paths_must_be_safe_and_canonical(self):
        for asset in ('../outside.dat', '/absolute.dat', 'pieces\\track.dat',
                      './track.dat', 'pieces//track.dat', 'C:/track.dat', 'bad\0path.dat'):
            with self.subTest(asset=asset):
                self.pieces[0]['asset_file'] = asset
                self.save()
                with self.assertRaisesRegex(ValueError, 'relative|escapes|canonical'):
                    self.verify()

    def test_symlink_cannot_escape_actual_build(self):
        path = self.directory/self.pieces[0]['asset_file']
        outside = self.root/'outside.dat'
        outside.write_bytes(path.read_bytes())
        path.unlink()
        path.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, 'escapes'):
            self.verify(required=False)

    def test_in_root_aliases_cannot_duplicate_actual_archive(self):
        path = self.directory/self.pieces[1]['asset_file']
        path.unlink()
        path.symlink_to(self.directory/self.pieces[0]['asset_file'])
        with self.assertRaisesRegex(ValueError, 'duplicate resolved'):
            self.verify()

    def test_present_build_file_is_not_an_optional_skip(self):
        wrong = self.root/'file'
        wrong.write_text('not a directory')
        with self.assertRaisesRegex(ValueError, 'not a directory'):
            verification_resources(self.descriptor_path, wrong, required=False)

    def test_broken_build_symlink_is_not_an_optional_skip(self):
        wrong = self.root/'broken-build'
        wrong.symlink_to(self.root/'absent')
        with self.assertRaisesRegex(ValueError, 'broken symbolic link'):
            verification_resources(self.descriptor_path, wrong, required=False)

    def test_present_build_missing_manifest_or_archive_never_skips(self):
        (self.directory/'manifest.json').unlink()
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            self.verify(required=False)
        self.save()
        (self.directory/self.pieces[0]['asset_file']).unlink()
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            self.verify(required=False)

    def test_malformed_present_manifest_never_skips(self):
        for raw in ('[1,2]', '{"pieces":', '{"pieces": []}'):
            with self.subTest(raw=raw):
                (self.directory/'manifest.json').write_text(raw)
                with self.assertRaises(ValueError):
                    self.verify(required=False)

    def test_selected_manifest_identity_recipe_and_asset_must_match(self):
        for key, value in (('id', 'different-track'), ('recipe', 'different_recipe'),
                           ('asset_file', 'pieces/different.dat')):
            with self.subTest(key=key):
                original = self.manifest['pieces'][0][key]
                self.manifest['pieces'][0][key] = value
                self.save()
                with self.assertRaisesRegex(ValueError, 'differs'):
                    self.verify()
                self.manifest['pieces'][0][key] = original

    def test_manifest_missing_extra_and_duplicate_selected_types_fail(self):
        original = deepcopy(self.manifest['pieces'])
        variants = [original[:-1], original + [{'id': 'extra', 'recipe': 'extra', 'asset_file': 'extra.dat'}],
                    original + [dict(original[0])]]
        for pieces in variants:
            with self.subTest(pieces=pieces):
                self.manifest['pieces'] = pieces
                self.save()
                with self.assertRaises(ValueError):
                    self.verify()

    def test_independent_selection_and_assembly_identity_are_enforced(self):
        for options in ({'selected_piece_ids': ['track-0']},
                        {'selected_piece_ids': ['track-0', 'track-1', 'track-2', 'extra']},
                        {'selected_piece_ids': ['track-0', 'track-1', 'track-1']},
                        {'selected_piece_ids': 'track-0'}, {'selected_piece_ids': 14},
                        {'assembly_id': 'another-assembly'}):
            with self.subTest(options=options):
                with self.assertRaises(ValueError):
                    self.verify(**options)

    def test_archive_byte_count_and_hash_pin_current_bytes(self):
        path = self.directory/self.pieces[0]['asset_file']
        original = path.read_bytes()
        for raw in (original+b'extra', original.replace(b'current model', b'changed model')):
            with self.subTest(length=len(raw)):
                path.write_bytes(raw)
                with self.assertRaisesRegex(ValueError, 'bytes changed'):
                    self.verify(required=False)

    def test_resource_count_is_read_from_actual_archive(self):
        self.pieces[0].pop('resource_sha256')
        self.pieces[0]['resource_count'] = 3
        self.save()
        with self.assertRaisesRegex(ValueError, 'count differs'):
            self.verify()

    def test_valid_hash_does_not_excuse_malformed_dbpf(self):
        (self.directory/self.pieces[0]['asset_file']).write_bytes(b'not a game archive')
        self.repin_archive()
        with self.assertRaisesRegex(ValueError, 'DBPF'):
            self.verify()

    def test_duplicate_actual_tgis_fail_even_when_dat_hash_is_repinned(self):
        path = self.directory/self.pieces[0]['asset_file']
        raw = bytearray(path.read_bytes())
        offset = struct.unpack_from('<I', raw, 40)[0]
        raw[offset+20:offset+32] = raw[offset:offset+12]
        path.write_bytes(raw)
        self.repin_archive()
        with self.assertRaisesRegex(ValueError, 'duplicate resource'):
            self.verify()

    def test_optional_resource_map_requires_exact_tgis_and_hashes(self):
        original = deepcopy(self.pieces[0]['resource_sha256'])
        for value in ({}, {'not-a-tgi': '0'*64},
                      {key: 'not-a-sha' for key in original}):
            with self.subTest(value=value):
                self.pieces[0]['resource_sha256'] = value
                self.save()
                with self.assertRaisesRegex(ValueError, 'exact TGI'):
                    self.verify()

    def test_resource_map_detects_changed_decoded_bytes_after_dat_repin(self):
        path = self.directory/self.pieces[0]['asset_file']
        path.write_bytes(path.read_bytes().replace(b'current model', b'changed model'))
        self.repin_archive()
        with self.assertRaisesRegex(ValueError, 'decompressed resource hashes differ'):
            self.verify()


if __name__ == '__main__':
    unittest.main()
