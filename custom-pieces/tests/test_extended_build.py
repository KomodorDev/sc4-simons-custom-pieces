"""Rehashed, portable-package tampering tests for crossings and current modular one-way HSR.

One real-NAM fixture is built in a temporary folder. Each mutation updates the
DAT's declared hash, and local donor paths are removed, so a rejection must
come from a portable structural/semantic check rather than stale file hashes.
These tests never replace framework output, install plugins, or open a city.
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

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import jsonc
from scp.paths import local_settings
from scp.build import build_project, package_build
from scp.dbpf import entries, decompress, pack_dbpf
from scp.models import parse_s3d, pack_s3d
from scp.verify import verify_build, parse_paths, RUL0, S3D, PATH, SHADOW


def path_bytes(parsed):
    """Re-encode inspected PATH fields without importing the recipe writer."""
    routes = parsed['routes']
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for route in routes:
        lines += list(map(str, [route['transport'], route['lane'], route['entry'], route['exit'],
                               route['compatibility'], len(route['points'])]))
        lines += [','.join(format(value, '.12g') for value in point) for point in route['points']]
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


class ExtendedPortablePackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local = local_settings(ROOT)
        config = jsonc.loads(local.read_text()) if local.is_file() else {}
        plugins = os.environ.get('SCP_TEST_NAM_PLUGINS', config.get('plugins'))
        if not plugins or not Path(plugins).is_dir():
            raise unittest.SkipTest('Audited NAM unavailable; set SCP_TEST_NAM_PLUGINS')
        cls.sandbox = tempfile.TemporaryDirectory(prefix='scp-extended-tests-')
        cls.base = Path(cls.sandbox.name).resolve()
        cls.fixture = cls.base / 'fixture'
        try:
            selected = ['hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg', 'hsr-l2-over-ghsr-ground-two-track-crossing-90deg',
                        'hsr-l2-over-ghsr-ground-two-track-crossing-upper-diagonal-45deg', 'hsr-l2-over-ghsr-ground-two-track-crossing-both-diagonal-90deg',
                        'hsr-l2-single-track-oneway-straight-width7500mm', 'hsr-l2-single-track-oneway-straight-diagonal',
                        'hsr-l2-two-track-mainline-split-90deg-right-compact']
            build_project(ROOT, plugins, cls.fixture, include=selected,
                          extra_roots=config.get('extra_plugins', []))
        except BaseException:
            cls.sandbox.cleanup()
            raise
        cls.manifest = json.loads((cls.fixture / 'manifest.json').read_text())
        cls.pieces = {piece['id']: piece for piece in cls.manifest['pieces']}

    @classmethod
    def tearDownClass(cls):
        cls.sandbox.cleanup()

    def setUp(self):
        self.case = Path(tempfile.mkdtemp(prefix='case-', dir=self.base))
        self.output = self.case / 'portable'
        shutil.copytree(self.fixture, self.output)
        (self.output / 'input-audit.json').unlink()

    def tearDown(self):
        shutil.rmtree(self.case)

    def mutate_dat(self, relative, mutation):
        path = self.output / relative
        resources = {key: decompress(value) for key, value in entries(path.read_bytes()).items()}
        manifest_path = self.output / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        mutation(resources, manifest)
        raw = pack_dbpf(resources)
        path.write_bytes(raw)
        record = next(record for record in manifest['files'] if record['path'] == relative)
        record.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')

    def mutate_piece(self, slug, mutation):
        self.mutate_dat(self.pieces[slug]['asset_file'], mutation)

    def test_current_selected_modules_and_zip_verify_without_local_donors(self):
        report = verify_build(self.output, write_report=False)
        self.assertTrue(report['static_checks_passed'])
        self.assertFalse(report['local_donor_comparison'])
        self.assertEqual(report['construction']['separate_piece_menu_roots'], len(self.pieces))
        self.assertEqual(report['construction']['states_per_root'], 8)
        self.assertNotIn('hsr-l2-over-tram-ground-mixed-crossing-90deg', self.pieces)
        self.assertEqual(len(self.pieces), 7)
        self.assertTrue({'hsr-l2-over-ghsr-ground-two-track-crossing-90deg', 'hsr-l2-over-ghsr-ground-two-track-crossing-upper-diagonal-45deg',
                         'hsr-l2-over-ghsr-ground-two-track-crossing-both-diagonal-90deg'} <= self.pieces.keys())
        self.assertFalse(any(value for key, value in report.items() if key.startswith('in_game_')))
        archive = self.case / 'all-pieces.zip'
        package_build(self.output, archive)
        extracted = self.case / 'extracted'
        with zipfile.ZipFile(archive) as zipped:
            self.assertNotIn('input-audit.json', zipped.namelist())
            zipped.extractall(extracted)
        self.assertTrue(verify_build(extracted, write_report=False)['static_checks_passed'])

    def test_each_new_crossing_rejects_a_crosslevel_path_after_rehashing(self):
        for slug in ('hsr-l2-over-ghsr-ground-two-track-crossing-90deg', 'hsr-l2-over-ghsr-ground-two-track-crossing-upper-diagonal-45deg',
                     'hsr-l2-over-ghsr-ground-two-track-crossing-both-diagonal-90deg'):
            with self.subTest(piece=slug):
                # Restore the fixture between the three independent mutations.
                shutil.rmtree(self.output)
                shutil.copytree(self.fixture, self.output)
                (self.output / 'input-audit.json').unlink()
                tile = int(self.pieces[slug]['tile_ids'][0], 16)
                def mutate(resources, manifest):
                    raw = resources[*PATH, tile]
                    changed, count = re.subn(rb',15\.5(?=\r?\n)', b',1', raw, count=1)
                    self.assertEqual(count, 1)
                    resources[*PATH, tile] = changed
                self.mutate_piece(slug, mutate)
                with self.assertRaisesRegex(ValueError, 'endpoints|shortcut|route|paths'):
                    verify_build(self.output, write_report=False)

    def test_reversed_oneway_path_is_rejected_after_rehashing(self):
        slug = 'hsr-l2-single-track-oneway-straight-width7500mm'
        tile = int(self.pieces[slug]['tile_ids'][0], 16)
        def mutate(resources, manifest):
            parsed = parse_paths(resources[*PATH, tile])
            route = parsed['routes'][0]
            route['entry'], route['exit'] = route['exit'], route['entry']
            route['points'].reverse()
            resources[*PATH, tile] = path_bytes(parsed)
        self.mutate_piece(slug, mutate)
        with self.assertRaisesRegex(ValueError, 'disconnected|revers|port'):
            verify_build(self.output, write_report=False)

    def test_negative_oneway_path_class_is_rejected_after_rehashing(self):
        slug = 'hsr-l2-single-track-oneway-straight-width7500mm'
        tile = int(self.pieces[slug]['tile_ids'][0], 16)
        def mutate(resources, manifest):
            parsed = parse_paths(resources[*PATH, tile])
            parsed['routes'][0]['lane'] = -99
            resources[*PATH, tile] = path_bytes(parsed)
        self.mutate_piece(slug, mutate)
        with self.assertRaisesRegex(ValueError, 'class'):
            verify_build(self.output, write_report=False)

    def test_split_junction_flag_is_rejected_after_rehashing(self):
        slug = 'hsr-l2-two-track-mainline-split-90deg-right-compact'
        def mutate(resources, manifest):
            tile = next(int(raw, 16) for raw in self.pieces[slug]['tile_ids']
                        if any(route['compatibility'] for route in
                               parse_paths(resources[*PATH, int(raw, 16)])['routes']))
            parsed = parse_paths(resources[*PATH, tile])
            self.assertGreaterEqual(sum(route['compatibility'] for route in parsed['routes']), 1)
            for route in parsed['routes']:
                route['compatibility'] = 0
            resources[*PATH, tile] = path_bytes(parsed)
        self.mutate_piece(slug, mutate)
        with self.assertRaisesRegex(ValueError, 'junction'):
            verify_build(self.output, write_report=False)

    def test_changed_shadow_pixels_are_rejected_after_rehashing(self):
        slug = 'hsr-l2-single-track-oneway-straight-diagonal'
        tile = int(self.pieces[slug]['tile_ids'][0], 16)
        def mutate(resources, manifest):
            key = (*SHADOW, tile + 4)
            raw = bytearray(resources[key])
            raw[43] ^= 1  # first pixel alpha, with all FSH header fields intact
            resources[key] = bytes(raw)
        self.mutate_piece(slug, mutate)
        with self.assertRaisesRegex(ValueError, 'silhouette'):
            verify_build(self.output, write_report=False)

    def test_wrong_shadow_zoom_size_is_rejected_after_rehashing(self):
        slug = 'hsr-l2-single-track-oneway-straight-width7500mm'
        tile = int(self.pieces[slug]['tile_ids'][0], 16)
        def mutate(resources, manifest):
            resources[*SHADOW, tile + 4] = resources[*SHADOW, tile + 3]
        self.mutate_piece(slug, mutate)
        with self.assertRaisesRegex(ValueError, 'zoom dimensions'):
            verify_build(self.output, write_report=False)

    def test_wrong_oneway_model_height_is_rejected_after_rehashing(self):
        slug = 'hsr-l2-single-track-oneway-straight-width7500mm'
        tile = int(self.pieces[slug]['tile_ids'][0], 16)
        def mutate(resources, manifest):
            model = parse_s3d(resources[*S3D, tile])
            for block in model['vertices']:
                data = bytearray(block['data'])
                for offset in range(0, len(data), block['stride']):
                    height = struct.unpack_from('<f', data, offset + 4)[0]
                    if height > 14.:
                        struct.pack_into('<f', data, offset + 4, height + 2.)
                block['data'] = bytes(data)
            changed = pack_s3d(model)
            for zoom in range(5):
                resources[*S3D, tile + zoom] = changed
        self.mutate_piece(slug, mutate)
        with self.assertRaisesRegex(ValueError, 'height|bed'):
            verify_build(self.output, write_report=False)

    def test_shifted_rail_texture_uvs_fail_even_when_all_models_and_preview_agree(self):
        slug = 'hsr-l2-single-track-oneway-straight-width7500mm'
        def mutate(resources, manifest):
            for key in list(resources):
                if key[:2] != S3D:
                    continue
                model = parse_s3d(resources[key])
                for block in model['vertices']:
                    self.assertEqual(block['stride'], 20)
                    data = bytearray(block['data'])
                    for offset in range(0, len(data), block['stride']):
                        u = struct.unpack_from('<f', data, offset + 12)[0]
                        struct.pack_into('<f', data, offset + 12, u + .1)
                    block['data'] = bytes(data)
                resources[key] = pack_s3d(model)
        self.mutate_piece(slug, mutate)
        # XYZ, material, shadow silhouette, zoom equality, and cursor preview
        # remain consistent; the failure must come from rail placement in UV.
        with self.assertRaisesRegex(ValueError, 'rail|UV'):
            verify_build(self.output, write_report=False)

    def test_oneway_rotation_cannot_become_a_mirror_even_after_manifest_rehashing(self):
        root = int(self.pieces['hsr-l2-single-track-oneway-straight-width7500mm']['puzzle_id'], 16)
        relative = 'zzz_Simons_Custom_Pieces/00_SCP_Controller_NAM50.dat'
        def mutate(resources, manifest):
            suffix = manifest['overlay']['rul0']['suffix']
            section = f'[HighwayIntersectionInfo_0x{root + 0x40000:08X}]\r\nCopyFrom = 0x{root:X}'
            self.assertIn(section, suffix)
            changed = suffix.replace(section, section + '\r\nTranspose = 1', 1)
            self.assertNotEqual(suffix, changed)
            resources[RUL0] = resources[RUL0][:-len(suffix.encode('ascii'))] + changed.encode('ascii')
            manifest['overlay']['rul0']['suffix'] = changed
        self.mutate_dat(relative, mutate)
        with self.assertRaisesRegex(ValueError, 'clone rotation or reflection'):
            verify_build(self.output, write_report=False)


if __name__ == '__main__':
    unittest.main()
