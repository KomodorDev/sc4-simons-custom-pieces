"""Direct native-donor checks for the three additional crossing recipes.

Optional audited NAM inputs are read once; no Plugins scan, installation,
framework-output replacement, or city changes occur in these tests.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp_hsr.crossings import build_crossing, check_paths, check_models, INFO, PATH, S3D
from scp_hsr.crossings import _read_paths
from scp import jsonc
from scp.paths import local_settings
from scp.dbpf import entries, decompress
from scp.models import parse_s3d
from scp.verify import parse_rules


class CrossingDonorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local = local_settings(ROOT)
        config = jsonc.load(local) if local.is_file() else {}
        plugins = os.environ.get('SCP_TEST_NAM_PLUGINS', config.get('plugins'))
        if not plugins or not Path(plugins).is_dir():
            raise unittest.SkipTest('Audited NAM donors unavailable; set SCP_TEST_NAM_PLUGINS')
        profile = jsonc.load(ROOT / 'config/profiles/nam50-rhd.jsonc')
        cls.context, cls.donors = {}, {}
        for label in ('controller', 'hsr', 'urail'):
            expected = profile['files'][label]
            candidates = list(Path(plugins).rglob(expected['filename']))
            if len(candidates) != 1:
                raise RuntimeError(f"Expected one native donor {expected['filename']}")
            raw = candidates[0].read_bytes()
            if hashlib.sha256(raw).hexdigest() != expected['sha256']:
                raise RuntimeError(f'Native {label} donor differs from the audited profile')
            cls.context[label] = {key: decompress(value) for key, value in entries(raw).items()}
            cls.donors.update(cls.context[label])
        allocated = [
            ('hsr_straight_ghsr', 'hsr-straight-ghsr', 'f7a2', ['7f500000'], '7f500ff5'),
            ('diagonal_hsr_straight_ghsr', 'diagonal-hsr-straight-ghsr', 'f7a3', ['7f501000', '7f501010'], '7f501ff5'),
            ('diagonal_hsr_diagonal_ghsr', 'diagonal-hsr-diagonal-ghsr', 'f7a4', ['7f502000', '7f502010'], '7f502ff5'),
        ]
        cls.specs, cls.built = {}, {}
        for n, (recipe, slug, puzzle, tiles, preview) in enumerate(allocated):
            path = ROOT / 'domains/high-speed-rail/00_pieces' / slug / 'piece.json'
            if path.is_file():
                spec = json.loads(path.read_text())
            else:
                spec = {'id': slug, 'recipe': recipe, 'name': slug, 'puzzle_id': puzzle,
                        'tile_ids': tiles, 'preview_id': preview,
                        'effect_name': f'preview_scp_crossing____{n + 2:03d}'}
            cls.specs[recipe] = spec
            cls.built[recipe] = build_crossing(spec, cls.context)

    def test_all_recipes_pass_independent_models_and_paths(self):
        for recipe, (resources, _) in self.built.items():
            with self.subTest(recipe=recipe):
                paths = check_paths(resources, self.specs[recipe], self.donors)
                models = check_models(resources, self.specs[recipe], self.donors)
                self.assertEqual(paths['rotations_and_mirrors_checked'], 8)
                self.assertTrue(paths['no_crosslevel_routes'])
                self.assertTrue(models['native_buffer_comparison'])
                self.assertTrue(models['preview_matches_tiles'])

    def test_returned_rules_have_eight_native_states_and_no_menu_ring(self):
        for recipe, (_, rules) in self.built.items():
            with self.subTest(recipe=recipe):
                rings, sections = parse_rules(rules)
                self.assertEqual(rings, [])
                root = int(self.specs[recipe]['puzzle_id'], 16)
                self.assertEqual(set(sections), {root + n * 0x10000 for n in range(8)})
                self.assertNotIn(INFO[recipe]['family'], rules)
                self.assertNotIn(' rail:', rules)
                self.assertNotIn('AddTypes', rules)

    def test_native_pedestrian_and_underground_rail_paths_are_excluded(self):
        for recipe, (resources, _) in self.built.items():
            with self.subTest(recipe=recipe):
                for tile in self.specs[recipe]['tile_ids']:
                    version, terrain, paths = _read_paths(resources[*PATH, int(tile, 16)])
                    self.assertEqual((version, terrain, len(paths)), ('1.2', 0, 4))
                    self.assertEqual({p['transport'] for p in paths}, {7})
                    self.assertEqual({point[2] for path in paths for point in path['points']}, {1., 15.5})

    def test_unrelated_ground_model_meshes_are_excluded(self):
        for recipe, (resources, _) in self.built.items():
            with self.subTest(recipe=recipe):
                for tile in self.specs[recipe]['tile_ids']:
                    model = parse_s3d(resources[*S3D, int(tile, 16)])
                    self.assertEqual(len(model['meshes']), 2)
                    self.assertFalse({b'Sidewalk', b'Rail'} &
                                     {m['name'].rstrip(b'\0') for m in model['meshes']})

    def test_diagonal_pair_internal_correction_is_exactly_two_tenths(self):
        recipe = 'diagonal_hsr_diagonal_ghsr'
        resources = self.built[recipe][0]
        changes = []
        for n, (tile, original_id) in enumerate(zip(self.specs[recipe]['tile_ids'], (0x59F3D150, 0x59F3D160))):
            original = [r for r in _read_paths(self.context['urail'][*PATH, original_id])[2] if r['transport'] == 7]
            actual = [r for r in _read_paths(resources[*PATH, int(tile, 16)])[2] if r['points'][0][2] == 1.]
            for before, after in zip(original, actual):
                self.assertEqual((before['entry'], before['exit']), (after['entry'], after['exit']))
                for p, q in zip(before['points'], after['points']):
                    if p != q:
                        changes.append((n, p, q))
                        self.assertEqual(p[1:], q[1:])
                        self.assertEqual(p[1], -8. if n == 0 else 8.)
                        self.assertAlmostEqual(abs(p[0] - q[0]), .1)
        self.assertEqual(changes, [(0, (-2.8, -8., 1.), (-2.9, -8., 1.)),
                                   (1, (2.8, 8., 1.), (2.9, 8., 1.))])

    def test_undoing_internal_correction_breaks_exact_continuity(self):
        recipe = 'diagonal_hsr_diagonal_ghsr'
        resources = dict(self.built[recipe][0])
        tile = int(self.specs[recipe]['tile_ids'][0], 16)
        key = (*PATH, tile)
        original = resources[key]
        resources[key] = original.replace(b'-2.9,-8,1\r\n', b'-2.8,-8,1\r\n', 1)
        self.assertNotEqual(original, resources[key])
        with self.assertRaisesRegex(ValueError, 'endpoints'):
            check_paths(resources, self.specs[recipe])

    def test_cross_level_shortcut_is_rejected(self):
        recipe = 'diagonal_hsr_straight_ghsr'
        resources = dict(self.built[recipe][0])
        key = (*PATH, int(self.specs[recipe]['tile_ids'][0], 16))
        resources[key] = re.sub(rb',15\.5(?=\r?\n)', b',1', resources[key], count=1)
        with self.assertRaisesRegex(ValueError, 'endpoints|shortcut'):
            check_paths(resources, self.specs[recipe])

    def test_native_diagonal_shadow_orientations_match_registered_donors(self):
        ini = self.context['controller'][0, 0x8A5971C5, 0x8A5993B9].decode('latin1')
        expected = {0x59F3D200: (0x5DD31500, 1),
                    0x59F3D210: (0x5DD01A00, 0), 0x59F3D220: (0x5DD01A00, 2)}
        found = {}
        for raw in ini.splitlines():
            line = raw.split(';', 1)[0]
            if '=' not in line:
                continue
            value = line.split('=', 1)[1]
            if not re.match(r'\s*0x59F3D(?:200|210|220)\s*,', value, re.I):
                continue
            parts = [int(p.strip(), 0) for p in value.split(',')]
            if parts[1] == 0xFFFFFFF0 and parts[2] in {0x5DD31500, 0x5DD01A00}:
                found[parts[0]] = (parts[2], parts[4] if len(parts) > 4 else 0)
        self.assertEqual(found, expected)

    def test_native_ground_donor_paths_remain_unchanged(self):
        native = (self.context['urail'][*PATH, 0x59F3D150], self.context['urail'][*PATH, 0x59F3D160])
        before = tuple(hashlib.sha256(raw).digest() for raw in native)
        build_crossing(self.specs['diagonal_hsr_diagonal_ghsr'], self.context)
        self.assertEqual(before, tuple(hashlib.sha256(self.context['urail'][*PATH, iid]).digest()
                                      for iid in (0x59F3D150, 0x59F3D160)))


if __name__ == '__main__':
    unittest.main()
