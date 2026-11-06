"""Independent mixed Rail/Highways archive, proof, and collision regressions.

The approved normal fixture has deliberately tiny synthetic geometry. Only
ordinary baseline verification, catalogue discovery, donor discovery, and icon
route discovery are replaced; menu construction, saved-resource verification,
source restoration, family preservation, packaging, and closure checks are real.
No test reads or changes a game installation.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import re
import shutil
import sys
import unittest
from unittest.mock import patch
import zipfile

ROOT = next(path for path in Path(__file__).resolve().parents if (path / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

import test_menu_experiment as fixture
from scp.adaptive_network import RUL1
from scp.build import NETWORK_INI, RUL0, package_build
from scp.dbpf import encode_exemplar, exemplar, pack_dbpf
from scp.menu import DESCRIPTION, ICON, MENU_EXEMPLAR, TITLE
from scp.menu_experiment import CONTROLLER, MENU, build_assembly_menus
from scp.menu_experiment_resources import make_assembly_icon
from scp.piece_menu_families import apply as apply_families
from scp.rul0 import compose_rul0, ordering_span
from scp.verify import strict_dbpf


PREFIXES = (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)


def ordering(raw):
    """Read actual saved RUL0 rows without the production grouping helper."""
    first, last = ordering_span(raw)
    return [(match[1].decode().lower(), tuple(int(value, 16) for value in match[2].split(b',')))
            for match in re.finditer(rb'(RotationRing|AddTypes)\s*=\s*([^\r\n]+)', raw[first:last])]


class CrossDomainAssemblyMenuTests(unittest.TestCase):
    write_layout = fixture.MenuExperimentTests.write_layout

    def setUp(self):
        fixture.MenuExperimentTests.setUp(self)
        # A real normal-build source can contain family-composed RUL0 and RUL1.
        # Keep both to detect transforms that accidentally reset either layer.
        self.catalog['domains'] = {
            'high-speed-rail': {'path': 'domains/test-rail'},
            'highway': {'path': 'domains/test-highway'},
        }
        self.normal_pieces = []
        names = ('rail-one', 'rail-two', 'compact-one', 'compact-two',
                 'modular-one', 'modular-two', 'parallel-a-one', 'parallel-a-two',
                 'parallel-b-one', 'parallel-b-two', 'ghsr-a', 'ghsr-b',
                 'transition-a', 'transition-b', 'unused')
        for index, name in enumerate(names):
            domain = 'high-speed-rail' if index < 2 else 'highway'
            order = 0x7010F900 + index if index < 2 else 0xFFFFF900 + index
            self.normal_pieces.append({
                'id': 'fixture-' + name, 'name': 'Fixture ' + name,
                'description': 'Bounded mixed-network component', 'domain': domain,
                'puzzle_id': f'{0xF900 + index:04x}',
                'menu': {'id': f'{0x6A47F900 + index:08x}', 'order': f'{order:08x}'},
                'asset_file': f'{self.folder}/20_Pieces/SCP_fixture-{name}.dat',
            })
        for anchor, member in ((10, 11), (12, 13)):
            self.normal_pieces[member]['menu']['family_anchor'] = self.normal_pieces[anchor]['id']
        self.groups = [self.normal_pieces[index:index + 2] for index in range(0, 10, 2)]
        self.selections = [
            {'domain_id': 'high-speed-rail', 'layout_id': 'shared'},
            {'domain_id': 'highway', 'layout_id': 'shared'},
            {'domain_id': 'highway', 'layout_id': 'modular'},
            {'domain_id': 'highway', 'layout_id': 'parallel-a'},
            {'domain_id': 'highway', 'layout_id': 'parallel-b'},
        ]
        self.layouts = {'high-speed-rail': {}, 'highway': {}}
        self.catalog['_assemblies'] = []
        self.rail_parent = {'id': '6a47feec', 'order': '7010feec',
                            'title': 'Fixture Rail assemblies', 'description': 'Rail-only parent.'}
        self.highway_parent = {'id': '6a47feed', 'order': 'fffffeed',
                               'title': 'Fixture parallel alignments', 'description': 'Highway-only parent.'}
        for index, (selected, pieces) in enumerate(zip(self.selections, self.groups)):
            domain = selected['domain_id']
            assembly_id = 'fixture-assembly-' + str(index + 1)
            layout = {'assembly_id': assembly_id, 'member_order': 'first-use-in-assembly',
                      'cycle_button': {'id': f'{0x6A47FEF0 + index:08x}',
                                       'order': f'{(0x7010FEF0 if index == 0 else 0xFFFFFEF0) + index:08x}',
                                       'title': 'Fixture assembly ' + str(index + 1),
                                       'description': 'Tab stays in this separately placed component cycle.'}}
            if index == 0:
                layout['cycle_submenu'] = deepcopy(self.rail_parent)
            elif index >= 3:
                layout['cycle_submenu'] = deepcopy(self.highway_parent)
            self.layouts[domain][selected['layout_id']] = layout
            scene = {'placements': [{'piece_id': piece['id']} for piece in [pieces[1], pieces[0], pieces[1]]]}
            assembly = {'id': assembly_id, 'domain': domain,
                        'path': 'domains/fixtures/01_assemblies/' + assembly_id, 'scene': scene}
            self.catalog['_assemblies'].append(assembly)
            icon = self.project / assembly['path'] / 'icon.png'
            icon.parent.mkdir(parents=True, exist_ok=True)
            icon.write_bytes(make_assembly_icon(self.icon_routes, network_label='HSR' if index == 0 else 'HW'))
        self.write_layouts()
        patcher = patch('scp.menu_experiment._assembly_icon_network',
                        side_effect=lambda assembly: 'HSR' if assembly['domain'] == 'high-speed-rail' else 'HW')
        patcher.start(); self.addCleanup(patcher.stop)
        self.sync_source()

    def write_layouts(self):
        for domain, layouts in self.layouts.items():
            fixture.write_json(self.project / self.catalog['domains'][domain]['path'] / 'menu-layout.jsonc',
                               {'schema_version': 1, 'layouts': layouts})

    def sync_source(self):
        """Approve the entire tiny normal fixture, including its real families."""
        deltas, menus = [], {}
        for piece in self.normal_pieces:
            root = int(piece['puzzle_id'], 16)
            states = [root + turn * 0x10000 for turn in range(8)]
            deltas.append('RotationRing=' + ','.join(f'{state:08x}' for state in states) + '\r\n'
                          + ''.join(f'[HighwayIntersectionInfo_0x{state:08x}]\r\n'
                                    'Piece=0,0,0,0,0x12340005\r\n' for state in states))
            resources = fixture.menu_resource(piece)
            if piece['domain'] == 'highway':
                key = (*MENU_EXEMPLAR, int(piece['menu']['id'], 16))
                record = exemplar(resources[key])
                prop = next(prop for prop in record['properties'] if int(prop['id'], 16) == 0x4001)
                prop.update(id='0x00004005', values=[0])
                resources[key] = encode_exemplar(record)
            else:
                # Actual NAM 50 Rail donor measurement: property 0x4001 is
                # present with value 0, while 0x4005 is absent. Older generic
                # schema1 fixtures remain unchanged in their owning module.
                key = (*MENU_EXEMPLAR, int(piece['menu']['id'], 16))
                record = exemplar(resources[key])
                prop = next(prop for prop in record['properties'] if int(prop['id'], 16) == 0x4001)
                prop['values'] = [0]
                resources[key] = encode_exemplar(record)
            menus.update(resources)
        native = b'; exact native baseline\r\n[Ordering]\r\nRotationRing=100,10100\r\n[Other]\r\nValue=1\r\n'
        controller, composition = compose_rul0(native, deltas)
        controller, composition, menus, family_record = apply_families(
            controller, composition, menus, self.normal_pieces)
        self.payloads = {
            f'{self.folder}/{CONTROLLER}': pack_dbpf({RUL0: controller, NETWORK_INI: b'exact native network ini',
                                                     RUL1: b'exact adaptive/native approach RUL1'}),
            f'{self.folder}/{MENU}': pack_dbpf(menus),
        }
        for index, piece in enumerate(self.normal_pieces):
            self.payloads[piece['asset_file']] = pack_dbpf({
                (0x296678F7, 0x69668828, 0x7F600000 + index): ('PATH ' + piece['id']).encode(),
                (0x5AD0E817, 0xBADB57F1, 0x7F600000 + index): ('S3D ' + piece['id']).encode(),
            })
        self.catalog['pieces'] = [{key: value for key, value in piece.items() if key != 'asset_file'}
                                  for piece in self.normal_pieces]
        self.base['pieces'] = deepcopy(self.normal_pieces)
        self.base['overlay'] = {'rul0': composition, 'rul1': {'synthetic_fixture': True}}
        self.base['piece_menu_families'] = family_record
        self.base['files'] = [fixture.fingerprint(path, raw) for path, raw in self.payloads.items()]
        shutil.rmtree(self.source)
        for path, raw in {**self.payloads, **self.documentation}.items():
            destination = self.source / path
            destination.parent.mkdir(parents=True, exist_ok=True); destination.write_bytes(raw)
        fixture.write_json(self.source / 'manifest.json', self.base)

    def build(self, **kwargs):
        return build_assembly_menus(self.project, self.source, self.output,
                                    selections=kwargs.pop('selections', self.selections),
                                    plugins=self.plugins, extra_roots=[], **kwargs)

    def manifest(self):
        return json.loads((self.output / 'manifest.json').read_text())

    def replace_record(self, relative, raw):
        (self.output / relative).write_bytes(raw)
        manifest = self.manifest()
        for field in ('files', 'documentation'):
            manifest[field] = [fixture.fingerprint(relative, raw) if row['path'] == relative else row
                               for row in manifest[field]]
        for key, row in manifest['menu_experiment']['source_inputs'].items():
            if row['path'] == relative:
                manifest['menu_experiment']['source_inputs'][key] = fixture.fingerprint(relative, raw)
        fixture.write_json(self.output / 'manifest.json', manifest)

    def set_source_rail_selector(self, value):
        """Replace a complete approved source fixture, without changing its metadata."""
        relative = f'{self.folder}/{MENU}'
        resources = strict_dbpf(self.payloads[relative])
        for piece in self.normal_pieces:
            if piece['domain'] != 'high-speed-rail':
                continue
            key = (*MENU_EXEMPLAR, int(piece['menu']['id'], 16))
            record = exemplar(resources[key])
            next(prop for prop in record['properties'] if int(prop['id'], 16) == 0x4001)['values'] = [value]
            resources[key] = encode_exemplar(record)
        self.payloads[relative] = pack_dbpf(resources)
        (self.source / relative).write_bytes(self.payloads[relative])
        self.base['files'] = [fixture.fingerprint(path, raw) for path, raw in self.payloads.items()]
        fixture.write_json(self.source / 'manifest.json', self.base)

    def test_five_domain_qualified_cycles_preserve_families_assets_and_native_controller(self):
        result = self.build()
        self.assertEqual((result['assembly_menu_buttons'], result['member_buttons_hidden']), (5, 10))
        manifest = self.manifest()
        self.assertEqual(manifest['menu_experiment']['schema_version'], 2)
        self.assertEqual([row['domain_id'] for row in manifest['assembly_selections']],
                         ['high-speed-rail', 'highway', 'highway', 'highway', 'highway'])
        resources = strict_dbpf((self.output / self.folder / MENU).read_bytes())
        before = strict_dbpf(self.payloads[f'{self.folder}/{MENU}'])
        for index, selected in enumerate(self.selections):
            layout = self.layouts[selected['domain_id']][selected['layout_id']]
            iid = int(layout['cycle_button']['id'], 16)
            props = fixture.props(resources[*MENU_EXEMPLAR, iid])
            # Scene order is deliberately reversed from catalogue order.
            self.assertEqual(props[0x8A2602BB], [int(self.groups[index][1]['menu']['id'], 16)])
            if index == 0:
                self.assertEqual(props[0x4001], [0]); self.assertNotIn(0x4005, props)
            else:
                self.assertEqual(props[0x4005], [0]); self.assertNotIn(0x4001, props)
        for definition, parent in ((self.rail_parent, 0x29), (self.highway_parent, 0x31)):
            props = fixture.props(resources[*MENU_EXEMPLAR, int(definition['id'], 16)])
            self.assertEqual(props[0x8A2602CA], [parent]); self.assertEqual(props[0x8A2602CC], [1])
        for index in (10, 12, 14):
            for prefix in PREFIXES:
                key = (*prefix, int(self.normal_pieces[index]['menu']['id'], 16))
                self.assertEqual(resources[key], before[key])
        for index in (11, 13):
            self.assertFalse(any((*prefix, int(self.normal_pieces[index]['menu']['id'], 16)) in resources
                                 for prefix in PREFIXES))
        old_controller = strict_dbpf(self.payloads[f'{self.folder}/{CONTROLLER}'])
        current = strict_dbpf((self.output / self.folder / CONTROLLER).read_bytes())
        self.assertEqual(set(current), set(old_controller))
        self.assertEqual(current[RUL1], old_controller[RUL1]); self.assertEqual(current[NETWORK_INI], old_controller[NETWORK_INI])
        saved_rows = ordering(current[RUL0])
        all_selected_states = set()
        for pieces in self.groups:
            roots = [int(piece['puzzle_id'], 16) for piece in reversed(pieces)]
            positions = [at for at, row in enumerate(saved_rows) if row[1][0] in roots]
            self.assertEqual(positions, list(range(positions[0], positions[0] + 2)))
            self.assertEqual([saved_rows[at] for at in positions], [
                ('rotationring' if at == 0 else 'addtypes', tuple(root + turn * 0x10000 for turn in range(8)))
                for at, root in enumerate(roots)])
            states = {value for at in positions for value in saved_rows[at][1]}
            self.assertTrue(all_selected_states.isdisjoint(states)); all_selected_states.update(states)
        for anchor, member in ((10, 11), (12, 13)):
            expected = [('rotationring', tuple(int(self.normal_pieces[anchor]['puzzle_id'], 16) + turn * 0x10000 for turn in range(8))),
                        ('addtypes', tuple(int(self.normal_pieces[member]['puzzle_id'], 16) + turn * 0x10000 for turn in range(8)))]
            roots = {row[1][0] for row in expected}
            self.assertEqual([row for row in saved_rows if row[1][0] in roots], expected)
        for piece in self.normal_pieces:
            self.assertEqual((self.output / piece['asset_file']).read_bytes(), self.payloads[piece['asset_file']])
        report = self.real_verify(self.output, write_report=False)
        self.assertTrue(report['static_checks_passed']); self.assertFalse(report['in_game_menu_tested'])
        self.assertEqual(report['menu_experiment']['piece_types_preserved'], 15)
        guide = (self.output / 'docs/assembly-menus/README.md').read_text()
        self.assertIn('Transportation → Rail', guide); self.assertIn('Transportation → Highways', guide)
        checks = json.loads((self.output / 'docs/assembly-menus/game-checks.json').read_text())
        self.assertTrue(all(row['status'] == 'unverified' and not row['observations'] for row in checks['cases']))

    def test_rehashed_wrong_rail_or_highway_parent_and_network_properties_are_rejected(self):
        self.build(); relative = f'{self.folder}/{MENU}'; original = (self.output / relative).read_bytes()
        mutations = ((int(self.rail_parent['id'], 16), 0x8A2602CA, [0x31]),
                     (int(self.highway_parent['id'], 16), 0x8A2602CA, [0x29]),
                     (0x6A47FEF0, 0x4001, [1]), (0x6A47FEF1, 0x4005, [1]))
        for iid, propid, values in mutations:
            with self.subTest(iid=iid, property=propid):
                resources = strict_dbpf(original); key = (*MENU_EXEMPLAR, iid)
                record = exemplar(resources[key])
                next(prop for prop in record['properties'] if int(prop['id'], 16) == propid)['values'] = values
                resources[key] = encode_exemplar(record); self.replace_record(relative, pack_dbpf(resources))
                with self.assertRaises(ValueError):
                    self.real_verify(self.output, write_report=False)

    def test_measured_native_rail_zero_selector_record_and_parent_are_preserved(self):
        self.build()
        original = strict_dbpf(self.payloads[f'{self.folder}/{MENU}'])
        source = exemplar(original[*MENU_EXEMPLAR, int(self.groups[0][1]['menu']['id'], 16)])
        selector = next(prop for prop in source['properties'] if int(prop['id'], 16) == 0x4001)
        self.assertEqual(selector, {'id': '0x00004001', 'type': '0x0300',
                                    'key_type': '0x0000', 'values': [0], 'repetitions': None})
        actual = strict_dbpf((self.output / self.folder / MENU).read_bytes())
        for iid in (0x6A47FEF0, int(self.rail_parent['id'], 16)):
            with self.subTest(iid=iid):
                record = exemplar(actual[*MENU_EXEMPLAR, iid])
                self.assertEqual(record['parent'], source['parent'])
                self.assertEqual(next(prop for prop in record['properties'] if int(prop['id'], 16) == 0x4001), selector)
                self.assertFalse(any(int(prop['id'], 16) == 0x4005 for prop in record['properties']))
        self.assertTrue(self.real_verify(self.output, write_report=False)['static_checks_passed'])

    def test_rehashed_rail_selector_loss_wrong_category_or_changed_parent_rejects(self):
        self.build(); relative = f'{self.folder}/{MENU}'; original = (self.output / relative).read_bytes()
        for mutation in ('missing', 'renamed-highway', 'extra-highway', 'encoding', 'parent'):
            with self.subTest(mutation=mutation):
                resources = strict_dbpf(original); key = (*MENU_EXEMPLAR, 0x6A47FEF0)
                record = exemplar(resources[key])
                selector = next(prop for prop in record['properties'] if int(prop['id'], 16) == 0x4001)
                if mutation == 'missing':
                    record['properties'].remove(selector)
                elif mutation == 'renamed-highway':
                    selector['id'] = '0x00004005'
                elif mutation == 'extra-highway':
                    extra = deepcopy(selector); extra['id'] = '0x00004005'; record['properties'].append(extra)
                elif mutation == 'encoding':
                    selector['key_type'] = '0x0080'; selector['repetitions'] = 1
                else:
                    record['parent'] = [0x12345678, 0, 0]
                resources[key] = encode_exemplar(record); self.replace_record(relative, pack_dbpf(resources))
                with self.assertRaises(ValueError):
                    self.real_verify(self.output, write_report=False)

    def test_historical_synthetic_rail_one_selector_is_preserved_without_claiming_native_measurement(self):
        # Existing schema1 orchestration fixtures used1. Its continued support
        # is a source-preservation contract; the measured NAM50 donor uses0.
        self.set_source_rail_selector(1)
        self.build()
        resources = strict_dbpf((self.output / self.folder / MENU).read_bytes())
        original = strict_dbpf(self.payloads[f'{self.folder}/{MENU}'])
        source = exemplar(original[*MENU_EXEMPLAR, int(self.groups[0][1]['menu']['id'], 16)])
        expected = next(prop for prop in source['properties'] if int(prop['id'], 16) == 0x4001)
        for iid in (0x6A47FEF0, int(self.rail_parent['id'], 16)):
            record = exemplar(resources[*MENU_EXEMPLAR, iid])
            self.assertEqual(next(prop for prop in record['properties'] if int(prop['id'], 16) == 0x4001), expected)
            self.assertEqual(record['parent'], source['parent'])
        self.assertTrue(self.real_verify(self.output, write_report=False)['static_checks_passed'])

    def test_unsupported_source_rail_selector_is_rejected_before_output(self):
        self.set_source_rail_selector(2)
        with self.assertRaisesRegex(ValueError, '(?i)(rail|domain|network|selector)'):
            self.build()
        self.assertFalse(self.output.exists())

    def test_cross_domain_cycle_id_collision_rejects_before_output(self):
        self.layouts['highway']['shared']['cycle_button']['id'] = self.layouts['high-speed-rail']['shared']['cycle_button']['id'].upper()
        self.write_layouts()
        with self.assertRaisesRegex(ValueError, '(?i)(overlap|duplicate|collid|collision)'):
            self.build()
        self.assertFalse(self.output.exists())

    def test_cross_domain_parent_id_collision_rejects_before_output(self):
        for identifier in ('parallel-a', 'parallel-b'):
            self.layouts['highway'][identifier]['cycle_submenu']['id'] = self.rail_parent['id']
        self.write_layouts()
        with self.assertRaisesRegex(ValueError, '(?i)(conflict|domain|overlap|collid)'):
            self.build()
        self.assertFalse(self.output.exists())

    def test_cross_domain_presentation_overlaps_an_unrelated_piece_rejects(self):
        self.layouts['high-speed-rail']['shared']['cycle_button']['id'] = self.normal_pieces[-1]['menu']['id']
        self.write_layouts()
        with self.assertRaisesRegex(ValueError, '(?i)(overlap|collid|collision)'):
            self.build()
        self.assertFalse(self.output.exists())

    def test_cross_domain_state_and_member_menu_collisions_reject(self):
        original = deepcopy(self.normal_pieces)
        for field in ('puzzle_id', 'menu'):
            with self.subTest(field=field):
                self.normal_pieces = deepcopy(original)
                if field == 'puzzle_id':
                    self.normal_pieces[2]['puzzle_id'] = self.normal_pieces[0]['puzzle_id']
                else:
                    self.normal_pieces[2]['menu']['id'] = self.normal_pieces[0]['menu']['id']
                # A saved baseline is not generated for deliberately invalid
                # duplicate construction IDs: the group validator must reject
                # the frozen metadata before attempting any output transform.
                self.base['pieces'] = deepcopy(self.normal_pieces)
                self.catalog['pieces'] = [{key: value for key, value in piece.items() if key != 'asset_file'}
                                          for piece in self.normal_pieces]
                fixture.write_json(self.source / 'manifest.json', self.base)
                with self.assertRaisesRegex(ValueError, '(?i)(overlap|disjoint|shared|repeated)'):
                    self.build()
                self.assertFalse(self.output.exists())

    def test_scene_from_wrong_network_cannot_use_its_declared_menu_domain(self):
        self.catalog['_assemblies'][0]['scene']['placements'][0]['piece_id'] = self.normal_pieces[2]['id']
        with self.assertRaisesRegex(ValueError, '(?i)(domain|network)'):
            self.build()
        self.assertFalse(self.output.exists())

    def test_duplicate_domain_layout_pair_and_ambiguous_legacy_arguments_reject(self):
        invalid = ([], self.selections + [self.selections[0]], [{'domain_id': 'rail', 'layout_id': 'shared'}],
                   [{'domain_id': 'highway', 'layout_id': 'shared', 'extra': True}], 'shared')
        for selections in invalid:
            with self.subTest(selections=selections), self.assertRaises(ValueError):
                self.build(selections=selections)
            self.assertFalse(self.output.exists())
        for legacy in ({'domain_id': 'highway'}, {'layout_ids': ['shared', 'modular']}):
            with self.subTest(legacy=legacy), self.assertRaises(ValueError):
                self.build(**legacy)
            self.assertFalse(self.output.exists())

    def test_frozen_each_domain_group_and_icon_are_required_after_cached_verification(self):
        self.build(); self.real_verify(self.output, write_report=False)
        proof = self.manifest()['menu_experiment']['source_inputs']
        self.assertEqual(self.normal_verification_attempts, 1)
        for key in ('groups', 'icon-000', 'icon-004', 'controller', 'menu'):
            with self.subTest(key=key):
                path = self.output / proof[key]['path']; raw = path.read_bytes(); path.unlink()
                try:
                    with self.assertRaises(ValueError):
                        self.real_verify(self.output, write_report=False)
                finally:
                    path.write_bytes(raw)
        self.assertEqual(self.normal_verification_attempts, 1)

    def test_rehashed_wrong_frozen_group_domain_rejects(self):
        self.build(); proof = self.manifest()['menu_experiment']['source_inputs']['groups']
        bundle = json.loads((self.output / proof['path']).read_text())
        self.assertEqual(bundle['schema_version'], 2); self.assertNotIn('domain_id', bundle)
        bundle['groups'][0]['domain_id'] = 'highway'
        self.replace_record(proof['path'], json.dumps(bundle, sort_keys=True).encode())
        with self.assertRaises(ValueError):
            self.real_verify(self.output, write_report=False)

    def test_source_metadata_change_requires_fresh_normal_verification(self):
        self.build(); proof = self.manifest()['menu_experiment']['source_inputs']['manifest']
        frozen = json.loads((self.output / proof['path']).read_text())
        frozen['unexpected_source_change'] = True
        self.replace_record(proof['path'], json.dumps(frozen, sort_keys=True).encode())
        current = self.manifest(); current['unexpected_source_change'] = True
        fixture.write_json(self.output / 'manifest.json', current)
        with self.assertRaisesRegex(ValueError, 'Synthetic normal baseline differs'):
            self.real_verify(self.output, write_report=False)
        self.assertEqual(self.normal_verification_attempts, 2)

    def test_full_closure_and_unchanged_unrelated_assets_remain_checked(self):
        self.build(); self.real_verify(self.output, write_report=False)
        relative = self.normal_pieces[-1]['asset_file']; raw = (self.output / relative).read_bytes()
        self.replace_record(relative, raw + b'changed')
        with self.assertRaises(ValueError):
            self.real_verify(self.output, write_report=False)
        self.replace_record(relative, raw)
        extra = self.output / 'unfrozen-extra.dat'; extra.write_bytes(b'extra')
        with self.assertRaisesRegex(ValueError, '(?i)closure'):
            self.real_verify(self.output, write_report=False)

    def test_package_round_trip_restores_the_exact_normal_proof_without_catalogue(self):
        self.build(); archive_path = self.root / 'mixed-menus.zip'
        package_build(self.output, archive_path)
        extracted = self.root / 'extracted'
        with zipfile.ZipFile(archive_path) as archive:
            self.assertIsNone(archive.testzip()); archive.extractall(extracted)
        from scp.menu_experiment import _BASELINE_REPORTS
        _BASELINE_REPORTS.clear()
        with patch('scp.menu_experiment.load_catalog', side_effect=AssertionError('Portable verification needs no catalogue')):
            report = self.real_verify(extracted, write_report=False)
        self.assertTrue(report['static_checks_passed']); self.assertEqual(self.normal_verification_attempts, 2)
        self.assertFalse((self.plugins / self.folder).exists())

    def test_legacy_schema_one_rail_and_highway_archive_outputs_are_unchanged(self):
        """A qualified schema2 choice must not alter any legacy DAT payload."""
        for domain in ('high-speed-rail', 'highway'):
            with self.subTest(domain=domain):
                if domain == 'high-speed-rail':
                    # Two disjoint Rail groups are needed for the legacy API;
                    # move the second group's metadata and native menu type.
                    self.normal_pieces[2]['domain'] = self.normal_pieces[3]['domain'] = domain
                    for index in (2, 3):
                        self.normal_pieces[index]['menu']['order'] = f'{0x7010F900 + index:08x}'
                    second = deepcopy(self.layouts['highway']['shared'])
                    second['cycle_button']['order'] = '7010fef1'
                    self.layouts[domain]['second'] = second
                    self.catalog['_assemblies'][1]['domain'] = domain
                    icon = self.project / self.catalog['_assemblies'][1]['path'] / 'icon.png'
                    icon.write_bytes(make_assembly_icon(self.icon_routes, network_label='HSR'))
                    self.sync_source(); self.write_layouts(); ids = ['shared', 'second']
                else:
                    ids = ['modular', 'parallel-a', 'parallel-b']
                old_output = self.root / ('legacy-' + domain)
                qualified_output = self.root / ('qualified-' + domain)
                build_assembly_menus(self.project, self.source, old_output, layout_ids=ids,
                                     domain_id=domain, plugins=self.plugins, extra_roots=[])
                build_assembly_menus(self.project, self.source, qualified_output,
                                     selections=[{'domain_id': domain, 'layout_id': value} for value in ids],
                                     plugins=self.plugins, extra_roots=[])
                old_manifest = json.loads((old_output / 'manifest.json').read_text())
                new_manifest = json.loads((qualified_output / 'manifest.json').read_text())
                self.assertEqual(old_manifest['menu_experiment']['schema_version'], 1)
                self.assertEqual(new_manifest['menu_experiment']['schema_version'], 2)
                self.assertEqual(old_manifest['files'], new_manifest['files'])
                for row in old_manifest['files']:
                    self.assertEqual((old_output / row['path']).read_bytes(), (qualified_output / row['path']).read_bytes())
                old_groups_path = old_manifest['menu_experiment']['source_inputs']['groups']['path']
                old_groups = json.loads((old_output / old_groups_path).read_text())
                self.assertEqual(set(old_groups), {'schema_version', 'domain_id', 'groups'})
                self.assertEqual(old_groups['domain_id'], domain)
                self.assertTrue(all(set(row) == {'layout_id', 'layout', 'scene'} for row in old_groups['groups']))
                self.assertTrue(self.real_verify(old_output, write_report=False)['static_checks_passed'])


class CurrentCrossDomainSelectionTests(unittest.TestCase):
    def test_actual_trumpet_and_four_highway_layouts_have_disjoint_native_states(self):
        """Bind the portable archive fixture to the real five-layout selection."""
        from scp import jsonc
        from scp.catalog import load_catalog
        from scp.multi_assembly_menu import _cycle_roots, _groups
        from scp.piece_menu_families import declarations
        catalog = load_catalog(ROOT)
        requested = [('high-speed-rail', 'trumpet'),
                     ('highway', 'compact-diagonal-diamond'),
                     ('highway', 'modular-diagonal-diamond'),
                     ('highway', 'parallel-diagonal-diamond'),
                     ('highway', 'parallel-diagonal-diamond-alignment-b')]
        bundle = {'schema_version': 2, 'groups': []}
        for domain, layout_id in requested:
            registry = jsonc.load(ROOT / catalog['domains'][domain]['path'] / 'menu-layout.jsonc')
            layout = registry['layouts'][layout_id]
            assembly = next(row for row in catalog['_assemblies']
                            if row['domain'] == domain and row['id'] == layout['assembly_id'])
            group = {'domain_id': domain, 'layout_id': layout_id, 'layout': layout, 'scene': assembly['scene']}
            if 'terminal_components' in layout:
                ledger = catalog['_allocations']['assembly_aliases']
                group['alias_reservations'] = {key: ledger[key] for key in layout['terminal_components'].values()}
            bundle['groups'].append(group)
        groups = _groups({'pieces': catalog['pieces']}, bundle)
        self.assertEqual([len(pieces) for _, _, pieces in groups], [14, 13, 7, 15, 15])
        members = {piece['id'] for _, _, pieces in groups for piece in pieces}
        self.assertEqual(len(members), 64)
        roots = [_cycle_roots(layout, pieces) for layout, _, pieces in groups]
        self.assertEqual([len(row) for row in roots], [17, 13, 7, 15, 15])
        states = [{root + turn * 0x10000 for root in group for turn in range(8)} for group in roots]
        self.assertEqual(len(set.union(*states)), 67 * 8)
        family_groups = declarations(catalog['pieces'])
        actual_families = [{piece['id'] for piece in group} for group in family_groups]
        for family in actual_families:
            self.assertTrue(family.isdisjoint(members))
        self.assertTrue(any(any('ghsr' in name for name in family) for family in actual_families))
        self.assertTrue(any(any('transition-orthogonal-6tile' in name for name in family)
                            for family in actual_families))


if __name__ == '__main__':
    unittest.main()
