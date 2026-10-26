"""Binary-format checks and optional real-NAM package integration tests.

The integration cases use only temporary output folders. They never install
anything or modify donor archives. Set SCP_TEST_NAM_PLUGINS, or supply the
private local/settings.json used by the CLI, to enable them on an audited workstation.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import sys
import tempfile
import unittest
import zipfile

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.catalog import load_catalog
from scp.build import build_project, package_build, preflight_allocations
from scp.dbpf import entries, decompress, exemplar, encode_exemplar, pack_dbpf
from scp.verify import strict_dbpf, verify_build, RUL0, PATH, S3D, MENU_EXEMPLAR


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class BinaryFormatTests(unittest.TestCase):
    def test_valid_minimal_dbpf(self):
        raw = pack_dbpf({(1, 2, 3): b'first', (1, 2, 4): b'second'})
        self.assertEqual(strict_dbpf(raw), {(1, 2, 3): b'first', (1, 2, 4): b'second'})

    def test_overlapping_resource_offsets_are_rejected(self):
        raw = bytearray(pack_dbpf({(1, 2, 3): b'first', (1, 2, 4): b'second'}))
        index = struct.unpack_from('<I', raw, 40)[0]
        struct.pack_into('<I', raw, index + 20 + 12, 96)
        with self.assertRaisesRegex(ValueError, 'overlapping'):
            strict_dbpf(bytes(raw))

    def test_duplicate_resource_keys_are_rejected(self):
        raw = bytearray(pack_dbpf({(1, 2, 3): b'first', (1, 2, 4): b'second'}))
        index = struct.unpack_from('<I', raw, 40)[0]
        raw[index + 20:index + 32] = raw[index:index + 12]
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            strict_dbpf(bytes(raw))

    def test_index_past_eof_is_rejected(self):
        raw = bytearray(pack_dbpf({(1, 2, 3): b'first'}))
        index = struct.unpack_from('<I', raw, 40)[0]
        struct.pack_into('<I', raw, 40, index + 1)
        with self.assertRaisesRegex(ValueError, 'index'):
            strict_dbpf(bytes(raw))


class AllocationPreflightTests(unittest.TestCase):
    def setUp(self):
        self.piece = {'id':'allocation-check','recipe':'interchange_test',
                      'puzzle_id':'f8f0','tile_ids':['7f5f0000'],'preview_id':'7f5f0ff5',
                      'effect_name':'preview_allocation_check','menu':{'id':'6a47f8f0'}}
        self.context = {'controller':{RUL0:b'[HighwayIntersectionInfo_0x0000C200]\r\n'}}

    def test_clean_allocations_are_checked_without_compiling_models(self):
        report = preflight_allocations(self.context, {}, [self.piece])
        self.assertEqual(report['allocated_identifier_conflicts'],0)
        self.assertEqual(report['native_puzzle_ids_checked'],1)
        self.assertEqual(report['allocated_resources_checked'],19)

    def test_any_native_rotation_with_the_same_puzzle_root_is_rejected(self):
        self.context['controller'][RUL0] += b'[HighwayIntersectionInfo_0x0003F8F0]\r\n'
        with self.assertRaisesRegex(ValueError, 'already used by NAM'):
            preflight_allocations(self.context, {}, [self.piece])

    def test_installed_zoom_and_shadow_collisions_are_found_before_generation(self):
        for prefix in (S3D, (0x7AB50E44,0x2BC2759A)):
            with self.subTest(prefix=prefix), self.assertRaisesRegex(ValueError, 'collide'):
                preflight_allocations(self.context, {(*prefix,0x7f5f0004):['other.dat']}, [self.piece])


class RealNAMBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config_path = ROOT / 'local/settings.json'
        config = json.loads(config_path.read_text()) if config_path.is_file() else {}
        plugins = os.environ.get('SCP_TEST_NAM_PLUGINS', config.get('plugins'))
        if not plugins or not Path(plugins).is_dir():
            raise unittest.SkipTest('Audited local NAM unavailable; set SCP_TEST_NAM_PLUGINS to enable integration tests')
        cls.sandbox = tempfile.TemporaryDirectory(prefix='scp-build-tests-')
        cls.base = Path(cls.sandbox.name).resolve()
        cls.default_output, cls.combined_output = cls.base / 'default', cls.base / 'combined'
        extra = config.get('extra_plugins', [])
        try:
            crossings = load_catalog(ROOT)['piece_sets']['hsr-crossings']
            build_project(ROOT, plugins, cls.default_output, include=crossings, extra_roots=extra)
            build_project(ROOT, plugins, cls.combined_output,
                          include=['hsr-diagonal-ghsr', 'tram-under-hsr'], extra_roots=extra)
        except BaseException:
            cls.sandbox.cleanup()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.sandbox.cleanup()

    def setUp(self):
        self.case_dir = Path(tempfile.mkdtemp(prefix='case-', dir=self.base))

    def tearDown(self):
        shutil.rmtree(self.case_dir)

    def copy_fixture(self, combined=False, portable=False):
        source = self.combined_output if combined else self.default_output
        destination = self.case_dir / 'build'
        shutil.copytree(source, destination)
        if portable:
            (destination / 'input-audit.json').unlink()
        return destination

    def manifest(self, output):
        return json.loads((output / 'manifest.json').read_text())

    def mutate_dat(self, output, relative, mutation):
        path = output / relative
        resources = {key: decompress(value) for key, value in entries(path.read_bytes()).items()}
        mutation(resources)
        raw = pack_dbpf(resources)
        path.write_bytes(raw)
        manifest = self.manifest(output)
        record = next(item for item in manifest['files'] if item['path'] == relative)
        record.update(sha256=digest(raw), bytes=len(raw))
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')

    def test_default_and_explicit_piece_selection(self):
        default, combined = self.manifest(self.default_output), self.manifest(self.combined_output)
        self.assertEqual(len(default['pieces']), 4)
        self.assertNotIn('tram-under-hsr', [p['id'] for p in default['pieces']])
        default_report = verify_build(self.default_output, write_report=False)
        self.assertEqual(default_report['construction']['separate_piece_menu_roots'], 4)
        self.assertEqual({p['id'] for p in combined['pieces']}, {'hsr-diagonal-ghsr', 'tram-under-hsr'})
        report = verify_build(self.combined_output, write_report=False)
        self.assertEqual(report['construction']['separate_piece_menu_roots'], 2)
        self.assertEqual(report['construction']['states_per_root'], 8)
        self.assertTrue(report['local_donor_comparison'])
        self.assertFalse(report['in_game_menu_tested'])
        self.assertFalse(report['in_game_traffic_tested'])

    def test_models_and_paths_preserve_audited_prototype_assets(self):
        # Frozen fingerprints from the separately audited prototype DATs. These
        # literals do not read old source folders or import their builders.
        expected = {
            (*PATH, 0x5DD0F200): 'e0c611cd05d391dafa2f7910559a1136308be2e41500d4dd105dfc0aa718c23a',
            (*PATH, 0x5DD0F210): '3a7ed9ef965c75a9fe9188472868c73364faaabb49dc8fa341b889937a622914',
            (*S3D, 0x5DD0F200): '1aae543aac52f035d745eb17aec9242a56f0956412cbb1b5c2034f3844a8605e',
            (*S3D, 0x5DD0F210): '6a5a868ec52b5c5a6888bec534dac6e437cfb03dea8bd29a7407e8c23dd9ed52',
            (*S3D, 0x5DD0F225): 'c71e96626dd88b574c855aa62cc57d99a0793599f0c29431fa5487ce568b03b6',
            (*PATH, 0x5DD0F100): '2efb4616299953898021444e602a04bab17647faa7979c211dac5e3cc371aa9c',
            (*S3D, 0x5DD0F100): '184aad5a2eb9ae2f88675f872351e90b9698c5ae73ae966201660d1264780c6c',
        }
        resources = {}
        for piece in self.manifest(self.combined_output)['pieces']:
            resources.update({k: decompress(v) for k, v in
                              entries((self.combined_output / piece['asset_file']).read_bytes()).items()})
        for key, fingerprint in expected.items():
            self.assertEqual(digest(resources[key]), fingerprint, f'Changed existing asset {key}')

    def test_portable_zip_verifies_without_local_donors_or_paths(self):
        destination = self.case_dir / 'scp-development.zip'
        package_build(self.combined_output, destination)
        extracted = self.case_dir / 'portable'
        with zipfile.ZipFile(destination) as archive:
            self.assertNotIn('input-audit.json', archive.namelist())
            self.assertNotIn(str(Path.home()), archive.read('manifest.json').decode('utf8'))
            archive.extractall(extracted)
        report = verify_build(extracted, write_report=False)
        self.assertTrue(report['static_checks_passed'])
        self.assertFalse(report['local_donor_comparison'])
        self.assertEqual(report['documentation_files_checked'], len(self.manifest(extracted)['documentation']))
        self.assertTrue((extracted/'docs/STRUCTURE.md').is_file())
        subject = extracted/'docs/domains/high-speed-rail/00_pieces/tram-under-hsr'
        self.assertTrue((subject/'README.md').is_file())
        self.assertIn('## Connections and journeys', (subject/'README.md').read_text())
        self.assertFalse((subject/'CONNECTIONS.md').exists())
        self.assertFalse((extracted/'docs/local').exists())

    def test_current_documentation_package_verifies_without_rebuilding_compiled_payloads(self):
        from scp.export import compiled_manifest_sha256
        source = self.case_dir/'current-source'
        source.mkdir()
        (source/'README.md').write_text('# Current final views\n')
        (source/'preview-top.png').write_bytes(b'exact final image fixture')
        output = self.copy_fixture(combined=True, portable=True)
        before = {path: path.read_bytes() for path in output.rglob('*') if path.is_file()}
        destination = self.case_dir/'current.zip'
        package_build(output, destination, project_root=source, refresh_docs=True)
        self.assertEqual(set(before), {path for path in output.rglob('*') if path.is_file()})
        for path, raw in before.items():
            self.assertTrue(path.read_bytes() == raw, 'Packaging changed original build file: '+str(path))
        extracted = self.case_dir/'extracted'
        with zipfile.ZipFile(destination) as archive:
            archive.extractall(extracted)
        report = verify_build(extracted, write_report=False)
        self.assertTrue(report['static_checks_passed'])
        self.assertEqual(report['documentation_files_checked'], 3)
        self.assertEqual((extracted/'docs/preview-top.png').read_bytes(), b'exact final image fixture')
        self.assertEqual(compiled_manifest_sha256(self.manifest(extracted)),
                         compiled_manifest_sha256(self.manifest(output)))
        for item in self.manifest(output)['files']:
            self.assertEqual((extracted/item['path']).read_bytes(), before[output/item['path']])

    def test_changed_bytes_fail_even_before_semantic_checks(self):
        output = self.copy_fixture()
        relative = self.manifest(output)['pieces'][0]['asset_file']
        path = output / relative
        raw = bytearray(path.read_bytes()); raw[-1] ^= 1; path.write_bytes(raw)
        with self.assertRaisesRegex(ValueError, 'hash/size'):
            verify_build(output, write_report=False)

    def test_cross_level_path_fails_even_after_rehashing(self):
        output = self.copy_fixture(portable=True)
        relative = self.manifest(output)['pieces'][0]['asset_file']

        def mutation(resources):
            key = (*PATH, 0x5DD0F200)
            before = resources[key]
            resources[key] = re.sub(rb',15\.5(?=\r?\n)', b',1', before, count=1)
            self.assertNotEqual(before, resources[key])

        self.mutate_dat(output, relative, mutation)
        with self.assertRaisesRegex(ValueError, 'Traffic paths|shortcut'):
            verify_build(output, write_report=False)

    def test_wrong_menu_root_fails_even_after_rehashing(self):
        output = self.copy_fixture(portable=True)
        relative = 'zzz_Simons_Custom_Pieces/10_SCP_Menu.dat'

        def mutation(resources):
            key = (*MENU_EXEMPLAR, 0x6A47F7A1)
            record = exemplar(resources[key])
            prop = next(p for p in record['properties'] if int(p['id'], 16) == 0x8A2602BB)
            prop['values'] = [0x6A47F7A0]
            resources[key] = encode_exemplar(record)

        self.mutate_dat(output, relative, mutation)
        with self.assertRaisesRegex(ValueError, 'root-button'):
            verify_build(output, write_report=False)

    def test_existing_nam_ring_edit_is_rejected_after_rehashing(self):
        output = self.copy_fixture(portable=True)
        relative = 'zzz_Simons_Custom_Pieces/00_SCP_Controller_NAM50.dat'

        def mutation(resources):
            resources[RUL0] = b'AddTypes = F7A1\r\n' + resources[RUL0]

        self.mutate_dat(output, relative, mutation)
        with self.assertRaisesRegex(ValueError, 'Original RUL0'):
            verify_build(output, write_report=False)

    def test_rotation_rings_outside_ordering_fail_even_when_manifest_and_native_bytes_agree(self):
        output = self.copy_fixture(portable=True)
        relative = 'zzz_Simons_Custom_Pieces/00_SCP_Controller_NAM50.dat'

        def mutation(resources):
            overlay = self.manifest(output)['overlay']['rul0']
            insertion = overlay['ordering_insertion'].encode('ascii')
            suffix = overlay['suffix'].encode('ascii')
            actual = resources[RUL0]
            self.assertEqual(actual.count(insertion),1)
            self.assertTrue(actual.endswith(suffix))
            native = actual[:-len(suffix)].replace(insertion,b'',1)
            self.assertEqual(digest(native),overlay['base_sha256'])
            # Move the exact same recorded block after the last native puzzle
            # section. The appendix, manifest metadata and recovered native
            # resource still agree; the game section context is now wrong.
            headers = re.findall(rb'^\s*\[([^\]]+)\]',native,re.M)
            self.assertTrue(headers)
            self.assertNotEqual(headers[-1],b'Ordering')
            resources[RUL0] = native+insertion+suffix

        self.mutate_dat(output, relative, mutation)
        with self.assertRaisesRegex(ValueError, '(?i)ordering|rotation ring'):
            verify_build(output, write_report=False)

    def test_duplicate_tgi_across_package_dats_is_rejected(self):
        output = self.copy_fixture()
        manifest = self.manifest(output)
        relative = manifest['pieces'][0]['asset_file']
        menu = entries((output / 'zzz_Simons_Custom_Pieces/10_SCP_Menu.dat').read_bytes())
        duplicate_key, duplicate_value = next(iter(menu.items()))
        self.mutate_dat(output, relative, lambda resources: resources.update({duplicate_key: decompress(duplicate_value)}))
        with self.assertRaisesRegex(ValueError, 'more than one'):
            verify_build(output, write_report=False)

    def test_unlisted_files_are_rejected(self):
        output = self.copy_fixture()
        (output / 'forgotten-old-plugin.dat').write_bytes(b'not a package payload')
        with self.assertRaisesRegex(ValueError, 'closure'):
            verify_build(output, write_report=False)

    def test_symlink_inside_output_is_rejected(self):
        output = self.copy_fixture()
        try:
            (output / 'linked-manifest.json').symlink_to(output / 'manifest.json')
        except (OSError, NotImplementedError) as error:
            self.skipTest(f'OS cannot create symlink: {error}')
        with self.assertRaisesRegex(ValueError, 'symlink'):
            verify_build(output, write_report=False)


if __name__ == '__main__':
    unittest.main()
