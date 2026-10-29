"""Adversarial menu-build checks use a synthetic baseline and real transforms.

Only the ordinary build verifier and local catalogue/donor discovery are
substituted. Experimental verification, resource checks, file closure, source
proof, packaging, and the public verify dispatcher execute their real code.
No case reads or changes an installed Plugins directory.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import struct
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import verify as verification
from scp.build import NETWORK_INI, RUL0, package_build
from scp.dbpf import encode_exemplar, exemplar, pack_dbpf
from scp.menu import DESCRIPTION, ICON, MENU_EXEMPLAR, TITLE
from scp.menu_experiment import (ASSEMBLY_CHECKS, ASSEMBLY_GUIDE, ASSEMBLY_MENU_KIND,
                                 ASSEMBLY_PROOF, CHECKS, CONTROLLER, GUIDE, KIND, MENU, PROOF,
                                 build_assembly_menu, build_menu_experiment, write_assembly_icons)
from scp.menu_experiment_resources import make_assembly_icon
from scp.rul0 import compose_rul0
from scp.verify import strict_dbpf


def fingerprint(path, raw):
    return {'path': path, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def menu_resource(piece):
    button_id = int(piece['menu']['id'], 16)
    values = [(0x10, [40]), (0x20, piece['name']), (0x4001, [1]),
              (0x49CAC341, [125]), (0x8A2602B8, [button_id]),
              (0x8A2602B9, [int(piece['menu']['order'], 16)]), (0x8A2602BB, [button_id]),
              (0x8A416A99, [*TITLE, button_id]), (0x8A94EEE0, [250]),
              (0xCA416AB5, [*DESCRIPTION, button_id])]
    properties = []
    for prop_id, value in values:
        is_text = isinstance(value, str)
        array = is_text or len(value) > 1
        properties.append({'id': f'0x{prop_id:08x}', 'type': '0x0c00' if is_text else '0x0300',
                           'key_type': '0x0080' if array else '0x0000', 'values': value,
                           'repetitions': len(value) if array else None})
    result = {(*MENU_EXEMPLAR, button_id): encode_exemplar({'parent': [0, 0, 0], 'properties': properties}),
              (*ICON, button_id): b'Preserved original icon ' + piece['id'].encode()}
    for prefix in (TITLE, DESCRIPTION):
        text = piece['name'] + (' title' if prefix == TITLE else ' description')
        result[*prefix, button_id] = struct.pack('<HH', len(text), 0x1000) + text.encode('utf-16-le')
    return result


def props(raw):
    return {int(prop['id'], 16): prop['values'] for prop in exemplar(raw)['properties']}


class MenuExperimentTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='scp-menu-orchestration-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.project, self.source, self.plugins = [self.root / name for name in ('project', 'source', 'Plugins')]
        for path in (self.project, self.source, self.plugins):
            path.mkdir()
        self.output = self.root / 'experiment'
        self.folder = 'zzz_Simons_Custom_Pieces'
        self.normal_pieces = []
        for index, name in enumerate(('alpha', 'unused', 'beta')):
            self.normal_pieces.append({'id': 'fixture-' + name, 'name': 'Fixture ' + name,
                'description': 'Synthetic piece ' + name, 'puzzle_id': f'{0xF800 + index:04x}',
                'menu': {'id': f'{0x6A47F800 + index:08x}', 'order': f'{0x7200F800 + index:08x}'},
                'asset_file': f'{self.folder}/20_Pieces/SCP_fixture-{name}.dat'})
        self.layout = {'assembly_id': 'fixture-assembly', 'member_order': 'first-use-in-assembly',
            'cycle_button': {'id': '6a47fef0', 'order': '7200fef0', 'title': 'Fixture: cycle parts',
                             'description': 'Tab chooses another separate reusable part.'},
            'submenu': {'id': 'd3c7a001', 'order': '7200fef1', 'title': 'Fixture: individual buttons',
                        'description': 'Choose one component from the test submenu.'}}
        # Source catalogue order deliberately differs from assembly first-use order.
        self.scene = {'placements': [{'piece_id': 'fixture-beta'}, {'piece_id': 'fixture-alpha'},
                                      {'piece_id': 'fixture-beta'}]}
        self.config = self.project / 'domains/test/menu-layout.jsonc'
        self.write_layout()
        self.catalog = {'domains': {'high-speed-rail': {'path': 'domains/test'}},
                        '_assemblies': [{'id': 'fixture-assembly', 'domain': 'high-speed-rail',
                                         'path': 'domains/test/01_assemblies/fixture-assembly',
                                         'scene': deepcopy(self.scene)}],
                        'pieces': [{key: value for key, value in piece.items() if key != 'asset_file'}
                                   for piece in self.normal_pieces]}
        self.assembly_icon = self.project / self.catalog['_assemblies'][0]['path'] / 'icon.png'
        self.assembly_icon.parent.mkdir(parents=True)
        self.icon_routes = [[(-40., 0., 15.5), (40., 0., 15.5)],
                            [(0., -60., 30.5), (0., 0., 15.5)]]
        self.assembly_icon.write_bytes(make_assembly_icon(self.icon_routes, network_label='HSR'))
        deltas, menus = [], {}
        for piece in self.normal_pieces:
            root = int(piece['puzzle_id'], 16)
            states = [root + number * 0x10000 for number in range(8)]
            delta = 'RotationRing=' + ','.join(f'{state:08x}' for state in states) + '\r\n'
            delta += ''.join(f'[HighwayIntersectionInfo_0x{state:08x}]\r\nPiece=0,0,0,0,0x12340005\r\n'
                             for state in states)
            deltas.append(delta)
            menus.update(menu_resource(piece))
        native = b'; native retained byte for byte\r\n[Ordering]\r\nRotationRing=100,10100\r\n[Other]\r\nvalue=1\r\n'
        controller, composition = compose_rul0(native, deltas)
        self.payloads = {f'{self.folder}/{CONTROLLER}': pack_dbpf({RUL0: controller, NETWORK_INI: b'native network ini'}),
                         f'{self.folder}/{MENU}': pack_dbpf(menus)}
        for index, piece in enumerate(self.normal_pieces):
            self.payloads[piece['asset_file']] = pack_dbpf({(0x296678F7, 0x69668828, 0x7F500000 + index):
                                                            ('Traffic PATH ' + piece['id']).encode(),
                                                           (0x5AD0E817, 0xBADB57F1, 0x7F500000 + index):
                                                            ('Compiled geometry ' + piece['id']).encode()})
        self.documentation = {'README.txt': b'Frozen build instructions\n',
                              'docs/example.md': b'# Frozen source documentation\n',
                              'docs/prior-assembly/evidence/report.txt': b'Frozen source report\n'}
        self.base = {'schema_version': 1, 'version': 'synthetic', 'plugin_folder': self.folder,
                     'pieces': deepcopy(self.normal_pieces), 'overlay': {'rul0': composition},
                     'files': [fingerprint(path, raw) for path, raw in self.payloads.items()],
                     'documentation': [fingerprint(path, raw) for path, raw in self.documentation.items()],
                     'release': {'public_release_ready': False, 'blocked': ['Synthetic test baseline']},
                     'installed': False, 'in_game_tested': False}
        for path, raw in {**self.payloads, **self.documentation}.items():
            destination = self.source / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw)
        write_json(self.source / 'manifest.json', self.base)
        self.normal_verifications = 0
        self.normal_verification_attempts = 0
        self.real_verify = verification.verify_build

        def dispatch(path, write_report=True):
            actual = json.loads((Path(path) / 'manifest.json').read_text())
            if 'menu_experiment' in actual:
                return self.real_verify(path, write_report=write_report)
            # This tiny normal fixture intentionally has no usable game models.
            # Require the complete exact fixture instead of bypassing its checks.
            self.normal_verification_attempts += 1
            if actual != self.base:
                raise ValueError('Synthetic normal baseline differs from approved fixture')
            for relative, raw in {**self.payloads, **self.documentation}.items():
                if (Path(path) / relative).read_bytes() != raw:
                    raise ValueError('Synthetic normal baseline payload changed')
            self.normal_verifications += 1
            return {'static_checks_passed': True, 'synthetic_baseline': True}

        for patcher in (patch.dict('scp.menu_experiment._BASELINE_REPORTS', {}, clear=True),
                        patch('scp.verify.verify_build', side_effect=dispatch),
                        patch('scp.menu_experiment.load_catalog', return_value=self.catalog),
                        patch('scp.menu_experiment._assembly_icon_routes', return_value=self.icon_routes),
                        patch('scp.menu_experiment._assembly_icon_network', return_value='HSR'),
                        patch('scp.build.audit_inputs', return_value=({}, {}, ['synthetic-donor'], {}))):
            patcher.start()
            self.addCleanup(patcher.stop)

    def write_layout(self):
        write_json(self.config, {'schema_version': 1, 'layouts': {'fixture-test': self.layout}})

    def build(self, **kwargs):
        return build_menu_experiment(self.project, self.source, self.output,
                                     layout_id=kwargs.pop('layout_id', 'fixture-test'),
                                     plugins=self.plugins, extra_roots=[], **kwargs)

    def manifest(self):
        return json.loads((self.output / 'manifest.json').read_text())

    def rewrite_manifest(self, value):
        write_json(self.output / 'manifest.json', value)

    def prepare_single_button_layout(self):
        self.layout.pop('submenu')
        self.layout['cycle_button']['title'] = 'Fixture assembly'
        self.write_layout()

    def build_single_button(self, **kwargs):
        return build_assembly_menu(self.project, self.source, self.output,
                                   layout_id='fixture-test', plugins=self.plugins, extra_roots=[], **kwargs)

    def test_single_assembly_button_replaces_member_presentations_and_preserves_all_piece_assets(self):
        self.prepare_single_button_layout()
        result = self.build_single_button()
        self.assertEqual(result['assembly_menu_buttons'], 1)
        self.assertEqual(result['member_buttons_hidden'], 2)
        self.assertFalse(result['submenus_dll_required'])
        self.assertFalse(result['installed'])
        manifest = self.manifest()
        self.assertEqual(manifest['menu_experiment']['kind'], ASSEMBLY_MENU_KIND)
        self.assertEqual(manifest['assembly_selection']['assembly_id'], 'fixture-assembly')
        self.assertEqual(manifest['source_provenance']['manifest'], f'{ASSEMBLY_PROOF}/manifest.json')
        menu = strict_dbpf((self.output / self.folder / MENU).read_bytes())
        self.assertEqual(menu[*ICON, 0x6A47FEF0], self.assembly_icon.read_bytes())
        self.assertEqual((self.output / ASSEMBLY_PROOF / 'icon.png').read_bytes(),
                         self.assembly_icon.read_bytes())
        originals = strict_dbpf(self.payloads[f'{self.folder}/{MENU}'])
        self.assertEqual({key[2] for key in menu if key[:2] == MENU_EXEMPLAR}, {0x6A47FEF0, 0x6A47F801})
        for piece in (self.normal_pieces[0], self.normal_pieces[2]):
            self.assertFalse(any(key[2] == int(piece['menu']['id'], 16) for key in menu))
        for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION):
            self.assertEqual(menu[*prefix, 0x6A47F801], originals[*prefix, 0x6A47F801])
        for piece in self.normal_pieces:
            self.assertEqual((self.output / piece['asset_file']).read_bytes(), self.payloads[piece['asset_file']])
        self.assertEqual((self.output / ASSEMBLY_PROOF / 'menu.proof').read_bytes(), self.payloads[f'{self.folder}/{MENU}'])
        for path, raw in self.documentation.items():
            self.assertEqual((self.output / ASSEMBLY_PROOF / 'documentation' / path).read_bytes(), raw)
        self.assertNotEqual((self.output / 'README.txt').read_bytes(), self.documentation['README.txt'])
        self.assertIn('Assembly: fixture-assembly', (self.output / 'README.txt').read_text())
        self.assertFalse((self.output / 'docs/example.md').exists())
        self.assertFalse((self.output / 'docs/prior-assembly').exists())
        self.assertIn('does not require Submenus DLL', (self.output / ASSEMBLY_GUIDE).read_text())
        checks = json.loads((self.output / ASSEMBLY_CHECKS).read_text())
        self.assertEqual(len(checks['cases']), 9)
        self.assertNotIn('Submenus_DLL_version', checks['environment_required'])
        self.assertTrue(all(row['status'] == 'unverified' and not row['observations'] for row in checks['cases']))
        report = self.real_verify(self.output, write_report=False)['menu_experiment']
        self.assertEqual(report['individual_submenu_buttons'], 0)
        self.assertEqual(report['new_presentation_resources'], 4)
        self.assertEqual(report['removed_member_presentation_resources'], 8)
        self.assertEqual(report['unrelated_piece_buttons_preserved'], 1)

    def test_missing_or_stale_canonical_icon_rejects_before_creating_build_output(self):
        self.prepare_single_button_layout()
        self.assembly_icon.unlink()
        with self.assertRaisesRegex(ValueError, 'Missing canonical assembly icon'):
            self.build_single_button()
        self.assertFalse(self.output.exists())
        self.assembly_icon.write_bytes(b'Stale assembly artwork')
        with self.assertRaisesRegex(ValueError, 'RGBA PNG'):
            self.build_single_button()
        self.assertFalse(self.output.exists())

    def test_icon_refresh_changes_only_assembly_artwork_without_native_inputs(self):
        self.assembly_icon.write_bytes(b'Stale assembly artwork')
        evidence = self.assembly_icon.parent / 'evidence/icon.json'
        artwork = {self.assembly_icon, evidence}
        before = {path.relative_to(self.root): path.read_bytes()
                  for path in self.root.rglob('*') if path.is_file() and path not in artwork}
        with patch('scp.build.audit_inputs', side_effect=AssertionError('Icon refresh needs no native inputs')):
            result = write_assembly_icons(self.project)
        self.assertEqual(result['icons'], ['domains/test/01_assemblies/fixture-assembly/icon.png'])
        self.assertFalse(result['built'])
        self.assertFalse(result['installed'])
        self.assertEqual(self.assembly_icon.read_bytes(), make_assembly_icon(self.icon_routes, network_label='HSR'))
        provenance = json.loads(evidence.read_text())
        self.assertEqual(provenance['output']['sha256'], hashlib.sha256(self.assembly_icon.read_bytes()).hexdigest())
        self.assertIn('no compiled model rendering', provenance['basis'])
        self.assertEqual(provenance['in_game_appearance'], 'unverified')
        self.assertEqual(provenance['labels'], {'brand': 'SCP', 'brand_position': 'top-left',
                         'category': 'ASM', 'network': 'HSR', 'footer_position': 'bottom-centre'})
        self.assertEqual(provenance['footer_ink_rows_px'], [33, 37])
        after = {path.relative_to(self.root): path.read_bytes()
                 for path in self.root.rglob('*') if path.is_file() and path not in artwork}
        self.assertEqual(after, before)

    def test_changed_domain_network_rejects_stale_icon_before_creating_build_output(self):
        self.prepare_single_button_layout()
        with patch('scp.menu_experiment._assembly_icon_network', return_value='GHSR'):
            with self.assertRaisesRegex(ValueError, 'canonical cycle artwork'):
                self.build_single_button()
        self.assertFalse(self.output.exists())

    def test_unresolved_domain_network_does_not_partially_refresh_artwork(self):
        before = self.assembly_icon.read_bytes()
        with patch('scp.menu_experiment._assembly_icon_network', side_effect=ValueError('Unknown assembly network')):
            with self.assertRaisesRegex(ValueError, 'Unknown assembly network'):
                write_assembly_icons(self.project)
        self.assertEqual(self.assembly_icon.read_bytes(), before)
        self.assertFalse((self.assembly_icon.parent / 'evidence/icon.json').exists())

    def test_saved_candidate_verification_does_not_depend_on_current_icon_source(self):
        from PIL import Image

        self.prepare_single_button_layout()
        with Image.open(self.assembly_icon) as icon:
            alternate = BytesIO()
            icon.save(alternate, format='PNG', compress_level=0)
        self.assertNotEqual(alternate.getvalue(), make_assembly_icon(self.icon_routes, network_label='HSR'))
        self.assembly_icon.write_bytes(alternate.getvalue())
        write_assembly_icons(self.project)
        self.assertEqual(self.assembly_icon.read_bytes(), alternate.getvalue())
        self.build_single_button()
        self.assembly_icon.unlink()
        self.assertTrue(self.real_verify(self.output, write_report=False)['static_checks_passed'])

    def test_saved_candidate_rejects_changed_icon_pixels_even_with_an_updated_menu_file_hash(self):
        self.prepare_single_button_layout()
        self.build_single_button()
        path = self.output / self.folder / MENU
        resources = strict_dbpf(path.read_bytes())
        resources[*ICON, 0x6A47FEF0] = make_assembly_icon()
        altered = pack_dbpf(resources)
        path.write_bytes(altered)
        manifest = self.manifest()
        manifest['files'] = [fingerprint(row['path'], altered)
                             if row['path'] == f'{self.folder}/{MENU}' else row
                             for row in manifest['files']]
        self.rewrite_manifest(manifest)
        with self.assertRaisesRegex(ValueError, 'canonical cycle artwork'):
            self.real_verify(self.output, write_report=False)

    def test_single_button_package_retains_source_proof_and_reverifies_without_installing(self):
        self.prepare_single_button_layout()
        self.build_single_button()
        archive_path = self.root / 'assembly-menu.zip'
        result = package_build(self.output, archive_path)
        self.assertFalse(result['public_release'])
        with zipfile.ZipFile(archive_path) as archive:
            self.assertIsNone(archive.testzip())
            self.assertIn(ASSEMBLY_GUIDE, archive.namelist())
            self.assertIn(f'{ASSEMBLY_PROOF}/controller.proof', archive.namelist())
            self.assertIn(f'{ASSEMBLY_PROOF}/menu.proof', archive.namelist())
            destination = self.root / 'assembly-extracted'
            archive.extractall(destination)
        self.assertTrue(self.real_verify(destination, write_report=False)['static_checks_passed'])

    def test_assembly_delivery_rejects_legacy_submenu_and_already_grouped_source(self):
        with self.assertRaisesRegex(ValueError, 'one cycle button'):
            self.build_single_button()
        self.assertFalse(self.output.exists())
        self.prepare_single_button_layout()
        self.build_single_button()
        with self.assertRaisesRegex(ValueError, 'combining assembly cycles'):
            build_assembly_menu(self.project, self.output, self.root / 'nested',
                                layout_id='fixture-test', plugins=self.plugins, extra_roots=[])

    def test_repeated_placements_of_one_type_still_get_one_assembly_button(self):
        self.prepare_single_button_layout()
        self.catalog['_assemblies'][0]['scene'] = {'placements': [{'piece_id': 'fixture-alpha'}] * 3}
        result = self.build_single_button()
        self.assertEqual(result['assembly_component_types'], 1)
        self.assertEqual(result['member_buttons_hidden'], 1)
        controller = (self.output / self.folder / CONTROLLER).read_bytes()
        self.assertEqual(controller, self.payloads[f'{self.folder}/{CONTROLLER}'])

    def test_assembly_menu_cli_help_and_historical_layout_selector_compatibility(self):
        help_result = subprocess.run([sys.executable, '-B', str(ROOT / 'scp.py'), 'assembly-menu', '--help'],
                                     capture_output=True, text=True, check=False)
        self.assertEqual(help_result.returncode, 0, help_result.stderr)
        self.assertIn('--layout', help_result.stdout)
        self.prepare_single_button_layout()
        write_json(self.config, {'schema_version': 1, 'layouts': {'trumpet': self.layout}})
        result = build_menu_experiment(self.project, self.source, self.output,
                                      plugins=self.plugins, extra_roots=[])
        self.assertEqual(result['assembly_menu_buttons'], 1)

    def test_build_preserves_all_assets_unselected_button_and_exact_unique_first_use_order(self):
        before = {path.relative_to(self.source).as_posix(): path.read_bytes()
                  for path in self.source.rglob('*') if path.is_file()}
        result = self.build()
        self.assertTrue(result['static_checks_passed'])
        self.assertFalse(result['installed'])
        self.assertEqual(result['assembly_component_types'], 2)
        manifest = self.manifest()
        self.assertEqual(manifest['menu_experiment']['member_ids'], ['fixture-beta', 'fixture-alpha'])
        self.assertEqual(len(manifest['pieces']), 3)
        self.assertFalse(manifest['release']['public_release_ready'])
        for piece in self.normal_pieces:
            self.assertEqual((self.output / piece['asset_file']).read_bytes(), self.payloads[piece['asset_file']])
        menu = strict_dbpf((self.output / self.folder / MENU).read_bytes())
        original_menu = strict_dbpf(self.payloads[f'{self.folder}/{MENU}'])
        unused = int(self.normal_pieces[1]['menu']['id'], 16)
        for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION):
            self.assertEqual(menu[*prefix, unused], original_menu[*prefix, unused])
        cycle = props(menu[*MENU_EXEMPLAR, 0x6A47FEF0])
        self.assertEqual(cycle[0x8A2602BB], [0x6A47F802])
        self.assertEqual(cycle[0x8A2602B8], [0x6A47FEF0])
        submenu = props(menu[*MENU_EXEMPLAR, 0xD3C7A001])
        self.assertEqual(submenu[0x8A2602CA], [0x29])
        self.assertEqual(submenu[0x8A2602CC], [1])
        for piece in (self.normal_pieces[0], self.normal_pieces[2]):
            button = props(menu[*MENU_EXEMPLAR, int(piece['menu']['id'], 16)])
            self.assertEqual(button[0x8A2602CA], [0xD3C7A001])
            self.assertEqual(button[0x8A2602CC], [2])
        controller = strict_dbpf((self.output / self.folder / CONTROLLER).read_bytes())
        original_controller = strict_dbpf(self.payloads[f'{self.folder}/{CONTROLLER}'])
        self.assertEqual(controller[NETWORK_INI], original_controller[NETWORK_INI])
        actual_rows = re.findall(rb'^(RotationRing|AddTypes)\s*=\s*([^\r\n]+)', controller[RUL0], re.M)
        custom = [(keyword, int(values.split(b',')[0], 16)) for keyword, values in actual_rows
                  if int(values.split(b',')[0], 16) >= 0xF800]
        self.assertEqual(custom, [(b'RotationRing', 0xF802), (b'AddTypes', 0xF800), (b'RotationRing', 0xF801)])
        suffix = self.base['overlay']['rul0']['suffix'].encode('ascii')
        self.assertTrue(controller[RUL0].endswith(suffix))
        checks = json.loads((self.output / CHECKS).read_text())
        self.assertEqual(len(checks['cases']), 10)
        self.assertTrue(all(row['status'] == 'unverified' and not row['observations'] for row in checks['cases']))
        self.assertIn('one reusable component at a time', (self.output / GUIDE).read_text())
        self.assertEqual(before, {path.relative_to(self.source).as_posix(): path.read_bytes()
                                  for path in self.source.rglob('*') if path.is_file()})
        self.assertEqual(self.normal_verifications, 1)

    def test_process_cache_reuses_unchanged_baseline_but_still_checks_actual_asset_bytes(self):
        self.build()
        initial = json.loads((self.output / 'verification.json').read_text())
        self.assertFalse(initial['source_build_verification_reused_in_process'])
        self.assertEqual(self.normal_verification_attempts, 1)
        report = self.real_verify(self.output, write_report=False)
        self.assertTrue(report['source_build_verification_reused_in_process'])
        self.assertEqual(self.normal_verification_attempts, 1)
        relative = self.normal_pieces[1]['asset_file']
        (self.output / relative).write_bytes(b'Changed unused asset after the cached pass')
        with self.assertRaisesRegex(ValueError, 'file hash/size mismatch'):
            self.real_verify(self.output, write_report=False)
        self.assertEqual(self.normal_verification_attempts, 1)

    def test_rehashed_changed_source_proof_requires_new_canonical_baseline_validation(self):
        self.build()
        self.assertEqual(self.normal_verification_attempts, 1)
        relative = f'{PROOF}/manifest.json'
        source_proof = json.loads((self.output / relative).read_text())
        source_proof['cache_probe'] = 'A changed source contract requires a fresh normal check'
        write_json(self.output / relative, source_proof)
        changed = fingerprint(relative, (self.output / relative).read_bytes())
        manifest = self.manifest()
        manifest['cache_probe'] = source_proof['cache_probe']
        manifest['menu_experiment']['source_inputs']['manifest'] = changed
        manifest['documentation'] = [changed if row['path'] == relative else row
                                     for row in manifest['documentation']]
        self.rewrite_manifest(manifest)
        # All declared proof hashes and the allowed experiment transformation
        # now agree. Only a fresh canonical baseline check can reject this.
        with self.assertRaisesRegex(ValueError, 'Synthetic normal baseline differs'):
            self.real_verify(self.output, write_report=False)
        self.assertEqual(self.normal_verification_attempts, 2)
        self.assertEqual(self.normal_verifications, 1)

    def test_missing_or_traversing_source_proof_is_rejected(self):
        self.build()
        proof = self.output / PROOF / 'menu.proof'
        original = proof.read_bytes()
        proof.unlink()
        with self.assertRaises(ValueError):
            self.real_verify(self.output, write_report=False)
        proof.write_bytes(original)
        manifest = self.manifest()
        manifest['menu_experiment']['source_inputs']['menu']['path'] = '../menu.dat'
        self.rewrite_manifest(manifest)
        with self.assertRaisesRegex(ValueError, 'source evidence path'):
            self.real_verify(self.output, write_report=False)

    def test_unknown_and_null_experiment_discriminators_cannot_fall_through_to_normal_verification(self):
        self.build()
        original = self.manifest()
        for marker in (None, {}, {'kind': 'unknown', 'schema_version': 1},
                       {'kind': KIND, 'schema_version': 99}):
            with self.subTest(marker=marker):
                manifest = deepcopy(original)
                manifest['menu_experiment'] = marker
                self.rewrite_manifest(manifest)
                with self.assertRaisesRegex(ValueError, 'Unsupported menu experiment'):
                    self.real_verify(self.output, write_report=False)

    def test_rehashed_unused_piece_asset_is_still_rejected(self):
        self.build()
        relative = self.normal_pieces[1]['asset_file']
        replacement = pack_dbpf({(0x296678F7, 0x69668828, 0x7F500001): b'Silently replaced unused PATH'})
        (self.output / relative).write_bytes(replacement)
        manifest = self.manifest()
        manifest['files'] = [fingerprint(relative, replacement) if row['path'] == relative else row
                             for row in manifest['files']]
        self.rewrite_manifest(manifest)
        with self.assertRaisesRegex(ValueError, 'exact allowed menu transformation'):
            self.real_verify(self.output, write_report=False)

    def test_unknown_layout_and_malformed_identifier_fail_without_creating_output(self):
        with self.assertRaisesRegex(ValueError, 'Unknown assembly menu layout'):
            self.build(layout_id='missing-layout')
        self.assertFalse(self.output.exists())
        for value in ('zzzzzzzz', '../badid', None, 1234, '00000000'):
            with self.subTest(value=value):
                self.layout['cycle_button']['id'] = value
                self.write_layout()
                with self.assertRaises(ValueError):
                    self.build()
                self.assertFalse(self.output.exists())

    def test_existing_output_is_never_overwritten(self):
        self.output.mkdir()
        retained = self.output / 'retain.txt'
        retained.write_bytes(b'Existing user output')
        with self.assertRaisesRegex(ValueError, 'output already exists'):
            self.build()
        self.assertEqual(retained.read_bytes(), b'Existing user output')
        self.assertEqual([path.name for path in self.output.iterdir()], ['retain.txt'])

    def test_packaged_experiment_round_trip_reverifies_with_frozen_proof(self):
        self.build()
        archive_path = self.root / 'experiment.zip'
        result = package_build(self.output, archive_path)
        self.assertFalse(result['public_release'])
        self.assertFalse(result['compiled_payloads_changed'])
        extracted = self.root / 'extracted'
        with zipfile.ZipFile(archive_path) as archive:
            self.assertIsNone(archive.testzip())
            self.assertIn(f'{PROOF}/manifest.json', archive.namelist())
            self.assertIn(f'{PROOF}/controller.proof', archive.namelist())
            self.assertIn(f'{PROOF}/menu.proof', archive.namelist())
            from scp.dbpf import EXTENSIONS
            payloads = {item['path'] for item in self.manifest()['files']}
            self.assertEqual({name for name in archive.namelist()
                              if Path(name).suffix.lower() in EXTENSIONS}, payloads)
            self.assertIn(CHECKS, archive.namelist())
            self.assertNotIn('verification.json', archive.namelist())
            archive.extractall(extracted)
        report = self.real_verify(extracted, write_report=False)
        self.assertTrue(report['static_checks_passed'])
        self.assertEqual(report['menu_experiment']['piece_types_preserved'], 3)
        self.assertEqual(report['menu_experiment']['component_types_in_cycle'], 2)
        self.assertFalse(report['in_game_menu_tested'])

    def test_frozen_experiment_cannot_refresh_documentation_or_become_public_package(self):
        self.build()
        for kwargs in ({'refresh_docs': True, 'project_root': self.project},
                       {'release': True, 'project_root': self.project}):
            with self.subTest(kwargs=kwargs):
                destination = self.root / ('release.zip' if kwargs.get('release') else 'refreshed.zip')
                with self.assertRaisesRegex(ValueError, 'frozen proof documentation.*public releases'):
                    package_build(self.output, destination, **kwargs)
                self.assertFalse(destination.exists())

    def test_unknown_file_and_altered_frozen_game_check_template_are_rejected(self):
        self.build()
        extra = self.output / 'undeclared.dat'
        extra.write_bytes(b'Unexpected content')
        with self.assertRaisesRegex(ValueError, 'file closure'):
            self.real_verify(self.output, write_report=False)
        extra.unlink()
        checks = json.loads((self.output / CHECKS).read_text())
        checks['cases'][0]['status'] = 'passed'
        write_json(self.output / CHECKS, checks)
        with self.assertRaisesRegex(ValueError, 'hash/size mismatch'):
            self.real_verify(self.output, write_report=False)

    def test_installed_presentation_collision_and_changed_authoring_definition_reject(self):
        with patch('scp.build.audit_inputs', return_value=({}, {(1, 2, 0xD3C7A001): ['foreign.dat']}, [], {})):
            with self.assertRaisesRegex(ValueError, 'identifier collides'):
                self.build()
        self.assertFalse(self.output.exists())
        self.catalog['pieces'][2]['description'] = 'Changed after compiling baseline'
        with self.assertRaisesRegex(ValueError, 'definition differs'):
            self.build()
        self.assertFalse(self.output.exists())

    def test_cache_key_rejects_identical_symlinked_donor_and_changed_donor_bytes(self):
        from scp.menu_experiment import _baseline_cache_key
        donor = self.root / 'donor.dat'
        raw = b'Original external donor archive'
        donor.write_bytes(raw)
        write_json(self.source / 'input-audit.json', {'donors': [
            {'path': str(donor), 'sha256': hashlib.sha256(raw).hexdigest()}]})
        proof = {'manifest': {'sha256': 'a' * 64}}
        _baseline_cache_key(self.source, proof, self.real_verify)
        retained = self.root / 'retained-donor.dat'
        donor.rename(retained)
        donor.symlink_to(retained)
        with self.assertRaisesRegex(ValueError, 'regular unlinked file'):
            _baseline_cache_key(self.source, proof, self.real_verify)
        donor.unlink()
        donor.write_bytes(b'Changed external donor archive')
        with self.assertRaisesRegex(ValueError, 'recorded fingerprint'):
            _baseline_cache_key(self.source, proof, self.real_verify)


if __name__ == '__main__':
    unittest.main()
