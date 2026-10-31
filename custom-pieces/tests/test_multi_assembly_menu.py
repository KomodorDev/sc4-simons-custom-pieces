"""Exercise disjoint assembly menus with real archives and frozen source proof.

Only normal-build verification, catalogue discovery, donor discovery, and icon
route discovery use the existing small synthetic fixture. The multi-assembly
builder, resource transformations, verifier dispatcher, cache, and packaging
execute their production code. No test reads or changes installed game files.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import re
import sys
import unittest
from unittest.mock import patch
import zipfile

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

import test_menu_experiment as fixture
from scp.build import NETWORK_INI, RUL0, package_build
from scp.dbpf import encode_exemplar, exemplar, pack_dbpf
from scp.menu import DESCRIPTION, ICON, MENU_EXEMPLAR, TITLE
from scp.menu_experiment import CONTROLLER, MENU
from scp.menu_experiment_resources import make_assembly_icon
from scp.rul0 import compose_rul0, ordering_span
from scp.verify import strict_dbpf


KIND = 'assembly-disjoint-button-cycles-v1'


class MultiAssemblyMenuTests(unittest.TestCase):
    # Reuse setup, rather than inherit its TestCase and rerun all legacy tests.
    write_layout = fixture.MenuExperimentTests.write_layout

    def setUp(self):
        fixture.MenuExperimentTests.setUp(self)
        self.layout_ids = ['fixture-one', 'fixture-two', 'fixture-three']
        self.normal_pieces = []
        for index, name in enumerate(('alpha', 'unused', 'beta', 'gamma', 'delta', 'epsilon', 'zeta')):
            self.normal_pieces.append({'id': 'fixture-' + name, 'name': 'Fixture ' + name,
                'description': 'Synthetic piece ' + name, 'puzzle_id': f'{0xF800 + index:04x}',
                'menu': {'id': f'{0x6A47F800 + index:08x}', 'order': f'{0x7200F800 + index:08x}'},
                'asset_file': f'{self.folder}/20_Pieces/SCP_fixture-{name}.dat'})
        self.groups = [
            [self.normal_pieces[2], self.normal_pieces[0]],
            [self.normal_pieces[4], self.normal_pieces[3]],
            [self.normal_pieces[6], self.normal_pieces[5]],
        ]
        self.layouts = {}
        self.catalog['_assemblies'] = []
        for index, (identifier, pieces) in enumerate(zip(self.layout_ids, self.groups)):
            assembly_id = 'fixture-assembly-' + ('one', 'two', 'three')[index]
            self.layouts[identifier] = {'assembly_id': assembly_id,
                'member_order': 'first-use-in-assembly',
                'cycle_button': {'id': f'{0x6A47FEF0 + index:08x}',
                                 'order': f'{0x7200FEF0 + index:08x}',
                                 'title': 'Fixture assembly ' + str(index + 1),
                                 'description': 'Tab selects one separately placed reusable component.'}}
            scene = {'placements': [{'piece_id': piece['id']} for piece in [*pieces, pieces[0]]]}
            assembly = {'id': assembly_id, 'domain': 'high-speed-rail',
                        'path': 'domains/test/01_assemblies/' + assembly_id, 'scene': scene}
            self.catalog['_assemblies'].append(assembly)
            icon = self.project / assembly['path'] / 'icon.png'
            icon.parent.mkdir(parents=True, exist_ok=True)
            icon.write_bytes(make_assembly_icon(self.icon_routes, network_label='HSR'))
        self.catalog['pieces'] = [{key: value for key, value in piece.items() if key != 'asset_file'}
                                  for piece in self.normal_pieces]
        self.write_layouts()
        deltas, menus = [], {}
        for piece in self.normal_pieces:
            root = int(piece['puzzle_id'], 16)
            states = [root + number * 0x10000 for number in range(8)]
            delta = 'RotationRing=' + ','.join(f'{state:08x}' for state in states) + '\r\n'
            delta += ''.join(f'[HighwayIntersectionInfo_0x{state:08x}]\r\nPiece=0,0,0,0,0x12340005\r\n'
                             for state in states)
            deltas.append(delta)
            menus.update(fixture.menu_resource(piece))
        native = b'; native retained byte for byte\r\n[Ordering]\r\nRotationRing=100,10100\r\n[Other]\r\nvalue=1\r\n'
        controller, composition = compose_rul0(native, deltas)
        self.payloads = {
            f'{self.folder}/{CONTROLLER}': pack_dbpf({RUL0: controller, NETWORK_INI: b'native network ini'}),
            f'{self.folder}/{MENU}': pack_dbpf(menus),
        }
        for index, piece in enumerate(self.normal_pieces):
            self.payloads[piece['asset_file']] = pack_dbpf({
                (0x296678F7, 0x69668828, 0x7F500000 + index): ('Traffic PATH ' + piece['id']).encode(),
                (0x5AD0E817, 0xBADB57F1, 0x7F500000 + index): ('Compiled geometry ' + piece['id']).encode(),
            })
        self.base['pieces'] = deepcopy(self.normal_pieces)
        self.base['overlay'] = {'rul0': composition}
        self.base['files'] = [fixture.fingerprint(path, raw) for path, raw in self.payloads.items()]
        for path, raw in self.payloads.items():
            destination = self.source / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw)
        fixture.write_json(self.source / 'manifest.json', self.base)

    def write_layouts(self):
        fixture.write_json(self.config, {'schema_version': 1, 'layouts': self.layouts})

    def build(self, **kwargs):
        from scp.menu_experiment import build_assembly_menus
        return build_assembly_menus(self.project, self.source, self.output,
                                    layout_ids=kwargs.pop('layout_ids', self.layout_ids),
                                    plugins=self.plugins, extra_roots=[], **kwargs)

    def manifest(self):
        return json.loads((self.output / 'manifest.json').read_text())

    def rewrite_manifest(self, value):
        fixture.write_json(self.output / 'manifest.json', value)

    def replace_record(self, relative, raw):
        destination = self.output / relative
        destination.write_bytes(raw)
        manifest = self.manifest()
        manifest['files'] = [fixture.fingerprint(relative, raw) if item['path'] == relative else item
                             for item in manifest['files']]
        self.rewrite_manifest(manifest)

    def test_three_buttons_have_separate_actual_tab_families_and_preserve_every_piece(self):
        result = self.build()
        self.assertEqual(result['assembly_menu_buttons'], 3)
        self.assertEqual(result['member_buttons_hidden'], 6)
        self.assertFalse(result['installed'])
        manifest = self.manifest()
        self.assertEqual(manifest['menu_experiment']['kind'], KIND)
        original = strict_dbpf(self.payloads[f'{self.folder}/{MENU}'])
        current = strict_dbpf((self.output / self.folder / MENU).read_bytes())
        added_ids = {int(layout['cycle_button']['id'], 16) for layout in self.layouts.values()}
        unused_id = int(self.normal_pieces[1]['menu']['id'], 16)
        self.assertEqual({key[2] for key in current if key[:2] == MENU_EXEMPLAR}, added_ids | {unused_id})
        for index, (layout_id, pieces) in enumerate(zip(self.layout_ids, self.groups)):
            button_id = int(self.layouts[layout_id]['cycle_button']['id'], 16)
            properties = fixture.props(current[*MENU_EXEMPLAR, button_id])
            self.assertEqual(properties[0x8A2602BB], [int(pieces[0]['menu']['id'], 16)])
            self.assertNotIn(0x8A2602CA, properties)
            self.assertNotIn(0x8A2602CC, properties)
            icon = self.project / self.catalog['_assemblies'][index]['path'] / 'icon.png'
            self.assertEqual(current[*ICON, button_id], icon.read_bytes())
            for piece in pieces:
                for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION):
                    self.assertNotIn((*prefix, int(piece['menu']['id'], 16)), current)
        for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION):
            self.assertEqual(current[*prefix, unused_id], original[*prefix, unused_id])
        for piece in self.normal_pieces:
            self.assertEqual((self.output / piece['asset_file']).read_bytes(), self.payloads[piece['asset_file']])

        controller = strict_dbpf((self.output / self.folder / CONTROLLER).read_bytes())
        baseline = strict_dbpf(self.payloads[f'{self.folder}/{CONTROLLER}'])
        self.assertEqual(controller[NETWORK_INI], baseline[NETWORK_INI])
        first, last = ordering_span(controller[RUL0])
        rows = []
        for line in controller[RUL0][first:last].decode('ascii').splitlines():
            match = re.fullmatch(r'\s*(RotationRing|AddTypes)\s*=\s*([^;]+)(?:;.*)?', line, re.I)
            if match:
                rows.append((match[1].lower(), tuple(int(value.strip(), 16) for value in match[2].split(','))))
        for pieces in self.groups:
            roots = [int(piece['puzzle_id'], 16) for piece in pieces]
            positions = [index for index, row in enumerate(rows) if row[1][0] in roots]
            self.assertEqual(positions, list(range(positions[0], positions[0] + len(pieces))))
            actual = [rows[index] for index in positions]
            self.assertEqual([row[0] for row in actual], ['rotationring', 'addtypes'])
            self.assertEqual([row[1] for row in actual],
                             [tuple(root + number * 0x10000 for number in range(8)) for root in roots])
        self.assertEqual([row for row in rows if row[1][0] == 0xF801],
                         [('rotationring', tuple(0xF801 + number * 0x10000 for number in range(8)))])
        report = self.real_verify(self.output, write_report=False)
        self.assertTrue(report['static_checks_passed'])
        self.assertEqual(report['menu_experiment']['assembly_menu_buttons'], 3)
        self.assertEqual(report['menu_experiment']['member_buttons_hidden'], 6)
        self.assertFalse(report['in_game_menu_tested'])

    def test_overlapping_assembly_members_reject_before_creating_output(self):
        self.catalog['_assemblies'][2]['scene']['placements'][0]['piece_id'] = self.groups[0][0]['id']
        with self.assertRaisesRegex(ValueError, '(?i)(overlap|disjoint|shared|repeated)'):
            self.build()
        self.assertFalse(self.output.exists())

    def test_highway_buttons_and_adaptive_controller_overlay_are_preserved(self):
        from scp.adaptive_network import RUL1
        self.catalog['domains'] = {'highway': {'path': 'domains/test'}}
        for index, piece in enumerate(self.normal_pieces):
            piece['domain'] = 'highway'
            piece['menu']['order'] = f'{0xFFFFF800 + index:08x}'
        self.catalog['pieces'] = [{key: value for key, value in piece.items() if key != 'asset_file'}
                                  for piece in self.normal_pieces]
        menus = {}
        for piece in self.normal_pieces:
            resources = fixture.menu_resource(piece)
            key = (*MENU_EXEMPLAR, int(piece['menu']['id'], 16))
            record = exemplar(resources[key])
            for prop in record['properties']:
                if int(prop['id'], 16) == 0x4001:
                    prop['id'] = '0x00004005'
                    prop['values'] = [0]
            resources[key] = encode_exemplar(record)
            menus.update(resources)
        for index, layout in enumerate(self.layouts.values()):
            layout['cycle_button']['order'] = f'{0xFFFFFEF0 + index:08x}'
        for assembly in self.catalog['_assemblies']:
            assembly['domain'] = 'highway'
            (self.project / assembly['path'] / 'icon.png').write_bytes(
                make_assembly_icon(self.icon_routes, network_label='HW'))
        self.write_layouts()
        controller_path = f'{self.folder}/{CONTROLLER}'
        controller = strict_dbpf(self.payloads[controller_path])
        rul1_bytes = b'Exact synthetic adaptive Avenue overlay retained across menu preparation\r\n'
        controller[RUL1] = rul1_bytes
        self.payloads[controller_path] = pack_dbpf(controller)
        self.payloads[f'{self.folder}/{MENU}'] = pack_dbpf(menus)
        self.base['pieces'] = deepcopy(self.normal_pieces)
        self.base['overlay']['rul1'] = {'synthetic_fixture': True}
        self.base['files'] = [fixture.fingerprint(path, raw) for path, raw in self.payloads.items()]
        for path, raw in self.payloads.items():
            (self.source / path).write_bytes(raw)
        fixture.write_json(self.source / 'manifest.json', self.base)
        with patch('scp.menu_experiment._assembly_icon_network', return_value='HW'):
            self.build(domain_id='highway')
        actual_controller = strict_dbpf((self.output / controller_path).read_bytes())
        self.assertEqual(actual_controller[RUL1], rul1_bytes)
        actual_menu = strict_dbpf((self.output / self.folder / MENU).read_bytes())
        for key, raw in actual_menu.items():
            if key[:2] == MENU_EXEMPLAR:
                properties = fixture.props(raw)
                self.assertEqual(properties[0x4005], [0])
                self.assertNotIn(0x4001, properties)
        self.assertTrue(self.real_verify(self.output, write_report=False)['static_checks_passed'])

    def test_case_normalized_duplicate_button_ids_reject_before_creating_output(self):
        self.layouts['fixture-two']['cycle_button']['id'] = self.layouts['fixture-one']['cycle_button']['id'].upper()
        self.write_layouts()
        with self.assertRaisesRegex(ValueError, '(?i)(overlap|duplicate|distinct|collision|collid)'):
            self.build()
        self.assertFalse(self.output.exists())

    def test_empty_duplicate_unknown_and_scalar_layout_selections_reject(self):
        for selected in ([], ['fixture-one', 'fixture-one'], ['fixture-one', 'missing'], 'fixture-one', None):
            with self.subTest(selected=selected):
                with self.assertRaises(ValueError):
                    self.build(layout_ids=selected)
                self.assertFalse(self.output.exists())

    def test_unknown_and_null_multi_discriminators_cannot_use_normal_verification(self):
        self.build()
        original = self.manifest()
        for marker in (None, {}, {'kind': KIND, 'schema_version': 99},
                       {'kind': 'unknown-multiple-assemblies', 'schema_version': 1}):
            with self.subTest(marker=marker):
                manifest = deepcopy(original)
                manifest['menu_experiment'] = marker
                self.rewrite_manifest(manifest)
                attempts = self.normal_verification_attempts
                with self.assertRaises(ValueError):
                    self.real_verify(self.output, write_report=False)
                self.assertEqual(self.normal_verification_attempts, attempts)

    def test_rehashed_controller_cannot_merge_or_split_a_group(self):
        self.build()
        relative = f'{self.folder}/{CONTROLLER}'
        resources = strict_dbpf((self.output / relative).read_bytes())
        self.assertIn(b'AddTypes=', resources[RUL0])
        resources[RUL0] = resources[RUL0].replace(b'AddTypes=', b'RotationRing=', 1)
        self.replace_record(relative, pack_dbpf(resources))
        with self.assertRaises(ValueError):
            self.real_verify(self.output, write_report=False)

    def test_each_group_proof_is_required_even_after_a_cached_pass(self):
        self.build()
        self.assertEqual(self.normal_verification_attempts, 1)
        cached = self.real_verify(self.output, write_report=False)
        self.assertTrue(cached['source_build_verification_reused_in_process'])
        proof = self.manifest()['menu_experiment']['source_inputs']
        records = [(key, item) for key, item in proof.items() if key not in {'manifest', 'controller', 'menu'}]
        self.assertGreaterEqual(len(records), 3)
        for key, item in records:
            with self.subTest(proof=key):
                path = self.output / item['path']
                raw = path.read_bytes()
                path.unlink()
                try:
                    with self.assertRaises(ValueError):
                        self.real_verify(self.output, write_report=False)
                finally:
                    path.write_bytes(raw)
        self.assertEqual(self.normal_verification_attempts, 1)

    def test_cache_rechecks_unchanged_assets_and_rejects_rehashed_unused_payload(self):
        self.build()
        self.real_verify(self.output, write_report=False)
        relative = self.normal_pieces[1]['asset_file']
        raw = b'Changed unrelated standalone asset after a cached verification'
        (self.output / relative).write_bytes(raw)
        with self.assertRaises(ValueError):
            self.real_verify(self.output, write_report=False)
        self.assertEqual(self.normal_verification_attempts, 1)
        self.replace_record(relative, raw)
        with self.assertRaises(ValueError):
            self.real_verify(self.output, write_report=False)
        self.assertEqual(self.normal_verification_attempts, 1)

    def test_rehashed_changed_base_proof_requires_fresh_canonical_verification(self):
        self.build()
        manifest = self.manifest()
        relative = manifest['menu_experiment']['source_inputs']['manifest']['path']
        proof = json.loads((self.output / relative).read_text())
        proof['cache_probe'] = 'Changed normal source metadata cannot inherit an earlier validation'
        fixture.write_json(self.output / relative, proof)
        changed = fixture.fingerprint(relative, (self.output / relative).read_bytes())
        manifest['cache_probe'] = proof['cache_probe']
        manifest['menu_experiment']['source_inputs']['manifest'] = changed
        manifest['documentation'] = [changed if item['path'] == relative else item
                                     for item in manifest['documentation']]
        self.rewrite_manifest(manifest)
        with self.assertRaisesRegex(ValueError, 'Synthetic normal baseline differs'):
            self.real_verify(self.output, write_report=False)
        self.assertEqual(self.normal_verification_attempts, 2)

    def test_package_round_trip_preserves_all_proof_and_reverifies(self):
        self.build()
        archive_path = self.root / 'three-assemblies.zip'
        result = package_build(self.output, archive_path)
        self.assertFalse(result['public_release'])
        extracted = self.root / 'extracted'
        with zipfile.ZipFile(archive_path) as archive:
            self.assertIsNone(archive.testzip())
            for item in self.manifest()['menu_experiment']['source_inputs'].values():
                self.assertIn(item['path'], archive.namelist())
            archive.extractall(extracted)
        report = self.real_verify(extracted, write_report=False)
        self.assertTrue(report['static_checks_passed'])
        self.assertEqual(report['menu_experiment']['assembly_menu_buttons'], 3)
        self.assertFalse(report['in_game_menu_tested'])
        self.assertFalse((self.plugins / self.folder).exists())


if __name__ == '__main__':
    unittest.main()
