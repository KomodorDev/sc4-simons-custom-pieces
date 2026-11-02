"""Check native helper declarations, reversible proofs, and controller closure.

All archives and donor pins are synthetic temporary inputs. The real RUL1
composer, dependency parser, input auditor, and menu proof paths run normally.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import struct
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import adaptive_network as adaptive
from scp import native_approaches as native
from scp.build import audit_inputs, NETWORK_INI, RUL0
from scp.dbpf import encode_exemplar, pack_dbpf
from scp.models import pack_s3d
from scp.verify import strict_dbpf
import test_adaptive_network as adaptive_fixture
import test_menu_experiment as menu_fixture
import test_multi_assembly_menu as multi_fixture


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def model():
    points = [(0., 0., 0., 0., 0.), (1., 0., 0., 1., 0.), (0., 0., 1., 0., 1.)]
    return pack_s3d({'version': (1, 5), 'vertices': [{'flags': 0, 'format': 0x80004001,
        'stride': 20, 'data': b''.join(struct.pack('<5f', *point) for point in points)}],
        'indices': [{'flags': 0, 'stride': 2, 'values': (0, 1, 2)}],
        'primitives': [[(0, 0, 3)]],
        'materials': [{'raw': struct.pack('<IBBBBHIBB', 0, 0, 0, 0, 0, 0, 0, 0, 0), 'textures': []}],
        'anim_header': struct.pack('<H', 1) + bytes(12),
        'meshes': [{'name': b'native fixture\0', 'flags': 0, 'frames': [(0, 0, 0, 0)]}],
        'trailing': []})


class NativeApproachTests(unittest.TestCase):
    def setUp(self):
        self.spec = {'id': 'native-fixture', 'domain': 'fixture', 'native_dd_approaches': True,
                     'dependencies': ['controller', 'dd_rhw']}
        self.declared = [{'cell': [-1, 0], 'end_cell': [0, 0], 'end_tile_id': '7f5b3010',
            'outward_edge': 0, 'native_tile_id': '57530900', 'native_rotation': 0,
            'monorail_flags': '01000400', 'dirtroad_flags': '03010000',
            'optional': True, 'experimental': True}]
        self.rows = tuple((adaptive.rotate_flags(0x01000400, turns),
                           adaptive.rotate_flags(0x03010000, turns), 0x57530900, turns, 0)
                          for turns in range(4))
        self.baseline = (b';native retained\r\n[MonoRailDirtRoadIntersectionSolutions]\r\n'
                         b'1=0x00020002,0x00000301,0x57007920,2,0\r\n'
                         b'TYPE1=0x01000400,0x02000200,0x57530000,0,0\r\n'
                         b'[StreetAvenueIntersectionSolutions]\r\n;native avenue\r\n'
                         b'[Other]\r\nkeep=yes\r\n')
        target = 0x57530900
        self.donors = {native.RUL1: self.baseline, (*native.S3D, target): model(),
            (*native.PATH, target): b'SC4PATHS\n1.1\n1\n0\n0\n1\n1\n0\n2\n2\n-8,15,0\n8,15,0\n',
            (*native.NETWORK_EXEMPLAR, target): encode_exemplar({'parent': [0, 0, 0], 'properties': [
                {'id': 0x10, 'type': 0x300, 'key_type': 0, 'values': [11]},
                {'id': 0x27812820, 'type': 0x300, 'key_type': 0x80,
                 'values': [*native.S3D, target]}]})}
        self.domain = SimpleNamespace(
            approaches=lambda piece: deepcopy(self.declared),
            rul1_rows=lambda piece: self.rows,
            NATIVE_RUL1_SHA256=sha(self.baseline),
            NATIVE_DEPENDENCY_SHA256={key: sha(value) for key, value in self.donors.items()
                                      if key != native.RUL1})
        patcher = patch('scp.native_approaches.domain_module', return_value=self.domain)
        self.provider = patcher.start()
        self.addCleanup(patcher.stop)

    def compose(self, pieces=None, raw=None):
        return native.compose_rul1(self.baseline if raw is None else raw,
                                  pieces or [self.spec], self.donors)

    def test_absent_or_false_flag_preserves_the_legacy_contract_without_domain_loading(self):
        for spec in ({'id': 'legacy'}, {'id': 'disabled', 'native_dd_approaches': False}):
            self.assertEqual(native.approaches(spec), [])
            self.assertEqual(native.compose_rul1(self.baseline, [spec], {}), (self.baseline, None))
            self.assertEqual(native.verify_rul1({}, [spec], {}, {}), {'adaptive_rul1_solutions_checked': 0})
        self.provider.assert_not_called()
        for bad in (None, 0, 1, 'true', []):
            with self.subTest(value=bad), self.assertRaisesRegex(ValueError, 'boolean'):
                native.approaches({'native_dd_approaches': bad})

    def test_helper_only_build_has_four_deduplicated_pairs_and_exact_native_restoration(self):
        pieces = [self.spec, {**self.spec, 'id': 'other-native-fixture'}]
        before = deepcopy(pieces)
        raw, record = self.compose(pieces)
        self.assertEqual(len(record['native_solutions']), 4)
        self.assertEqual(len(record['native_dependencies']), 3)
        self.assertEqual(len(record['selected_declarations']), 2)
        self.assertEqual(raw.replace(record['insertion'].encode(), b'', 1), self.baseline)
        report = native.verify_rul1({native.RUL1: raw}, pieces, {native.OVERLAY: record}, self.donors)
        self.assertEqual(report['native_dd_approach_cells_checked'], 2)
        self.assertEqual(report['native_dd_rul1_solutions_checked'], 4)
        self.assertEqual(report['adaptive_rul1_solutions_checked'], 0)
        self.assertEqual(pieces, before)
        self.assertFalse(report['native_dd_game_behavior_tested'])

    def test_native_and_adaptive_insertions_keep_independent_proofs(self):
        ground = adaptive_fixture.piece()
        first, legacy_record = adaptive.compose_rul1(self.baseline, [adaptive_fixture.delta(ground)], [ground])
        original_record = deepcopy(legacy_record)
        raw, record = self.compose([self.spec, ground], first)
        report = native.verify_rul1({native.RUL1: raw}, [self.spec, ground],
            {'rul1': legacy_record, native.OVERLAY: record}, self.donors)
        self.assertEqual(report['native_dd_rul1_solutions_checked'], 4)
        self.assertEqual(report['adaptive_rul1_solutions_checked'], 4)
        self.assertEqual(legacy_record, original_record)
        helper_removed = raw.replace(record['insertion'].encode(), b'', 1)
        self.assertEqual(helper_removed, first)
        self.assertEqual(helper_removed.replace(legacy_record['insertion'].encode(), b'', 1), self.baseline)

    def test_rehashed_proof_mutations_and_native_byte_tamper_are_rejected(self):
        raw, record = self.compose()
        cases = ['declaration', 'target', 'dependency-hash', 'solution', 'extra-field', 'offset',
                 'boolean-type', 'native-bytes']
        for case in cases:
            changed, current = deepcopy(record), raw
            if case == 'declaration':
                changed['selected_declarations'][0]['approaches'][0]['cell'][0] = -2
            elif case == 'target':
                changed['native_dependencies'][0]['tgi'] = '296678f7-69668828-57530900'
            elif case == 'dependency-hash':
                changed['native_dependencies'][0]['sha256'] = '0' * 64
            elif case == 'solution':
                changed['native_solutions'][0][3] = (changed['native_solutions'][0][3] + 1) % 4
            elif case == 'extra-field':
                changed['unexpected'] = True
            elif case == 'offset':
                changed['insertion_offset'] = True
            elif case == 'boolean-type':
                changed['game_behavior_tested'] = 0
            else:
                current = raw.replace(b'keep=yes', b'keep=bad')
                changed['base_sha256'] = sha(current.replace(changed['insertion'].encode(), b'', 1))
            with self.subTest(case=case), self.assertRaises(ValueError):
                native.verify_rul1({native.RUL1: current}, [self.spec], {native.OVERLAY: changed}, {})

    def test_missing_or_undeclared_helper_overlay_is_rejected(self):
        raw, record = self.compose()
        for resources, pieces, overlay in (({}, [self.spec], {}),
                ({native.RUL1: raw}, [self.spec], {}),
                ({native.RUL1: raw}, [{'id': 'legacy'}], {native.OVERLAY: record})):
            with self.assertRaises(ValueError):
                native.verify_rul1(resources, pieces, overlay, {})

    def test_native_marker_collision_and_duplicate_sections_are_rejected(self):
        a, b, c, d, e = self.rows[0]
        collision = f'TYPE9=0x{a:08x},0x{b:08x},0x{c:08x},{d},{e}\r\n'.encode()
        for raw in (self.baseline.replace(b'[StreetAvenue', collision + b'[StreetAvenue'),
                    self.baseline.replace(b'[StreetAvenue', collision.replace(b'TYPE9=', b'9=') + b'[StreetAvenue'),
                    self.baseline + b'[MonoRailDirtRoadIntersectionSolutions]\r\n'):
            with self.assertRaises(ValueError):
                self.compose(raw=raw)

    def test_domain_rows_must_exactly_match_declarations_without_reflections_or_duplicates(self):
        original = self.rows
        for rows in (original[:-1], (*original, original[0]),
                     ((*original[0][:4], 1), *original[1:]),
                     ((*original[0][:2], 0x57530200, 0, 0), *original[1:])):
            self.rows = rows
            with self.assertRaises(ValueError):
                self.compose()

    def test_actual_single_model_dependencies_reject_missing_wrong_group_or_changed_resources(self):
        self.assertEqual(native.dependency_keys([self.spec]), set(self.domain.NATIVE_DEPENDENCY_SHA256))
        self.assertNotIn((*native.S3D, 0x57530901), native.dependency_keys([self.spec]))
        for key in native.dependency_keys([self.spec]):
            donors = dict(self.donors)
            del donors[key]
            with self.subTest(missing=key), self.assertRaisesRegex(ValueError, 'Missing audited'):
                native.compose_rul1(self.baseline, [self.spec], donors)
        donors = dict(self.donors)
        donors[*native.S3D, 0x57530900] += b'tamper'
        with self.assertRaises(ValueError):
            native.compose_rul1(self.baseline, [self.spec], donors)
        wrong = dict(self.donors)
        wrong[0x296678F7, 0x69668828, 0x57530900] = wrong.pop((*native.PATH, 0x57530900))
        with self.assertRaisesRegex(ValueError, 'Missing audited'):
            native.compose_rul1(self.baseline, [self.spec], wrong)

    def test_pinned_native_unused_buffers_are_preserved_but_render_references_are_checked(self):
        from scp.models import parse_s3d
        key = (*native.S3D, 0x57530900)
        parsed = parse_s3d(self.donors[key])
        parsed['vertices'].insert(0, deepcopy(parsed['vertices'][0]))
        parsed['meshes'][0]['frames'] = [(1, 0, 0, 0)]
        raw = pack_s3d(parsed)
        self.donors[key] = raw
        self.domain.NATIVE_DEPENDENCY_SHA256[key] = sha(raw)
        self.compose()
        self.assertEqual(self.donors[key], raw)
        parsed['meshes'][0]['frames'] = [(2, 0, 0, 0)]
        self.donors[key] = pack_s3d(parsed)
        self.domain.NATIVE_DEPENDENCY_SHA256[key] = sha(self.donors[key])
        with self.assertRaisesRegex(ValueError, 'invalid render references'):
            self.compose()

    def test_helper_only_input_audit_rejects_foreign_rul1_and_target_overrides(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            controller = root / 'NetworkAddonMod_Controller.dat'
            controller.write_bytes(pack_dbpf({RUL0: b'native RUL0', NETWORK_INI: b'native INI',
                                               native.RUL1: self.baseline}))
            archive = root / 'native-dd.dat'
            archive.write_bytes(pack_dbpf({key: value for key, value in self.donors.items() if key != native.RUL1}))
            catalog = {'_root': root, 'plugin_folder': 'zzz_Simons_Custom_Pieces', '_profile': {'files': {
                label: {'filename': path.name, 'sha256': sha(path.read_bytes())}
                for label, path in [('controller', controller), ('dd_rhw', archive)]}}}
            audit_inputs(catalog, root, [self.spec], extra_roots=[])
            foreign = root / 'foreign.dat'
            foreign.write_bytes(pack_dbpf({native.RUL1: b'foreign override'}))
            with self.assertRaisesRegex(ValueError, 'Conflicting shared NAM overlay'):
                audit_inputs(catalog, root, [self.spec], extra_roots=[])
            foreign.write_bytes(pack_dbpf({(*native.S3D, 0x57530900): b'foreign model'}))
            with self.assertRaisesRegex(ValueError, 'Foreign or missing native DD'):
                audit_inputs(catalog, root, [self.spec], extra_roots=[])

    def test_cached_non_donor_context_does_not_enter_native_dependency_maps(self):
        path = Path('/synthetic/native-dd.dat')
        keys = native.dependency_keys([self.spec])
        resources = {key: self.donors[key] for key in keys}
        context = {'dd_rhw': resources, '_parallel_compiler_sha256': 'cached digest',
                   '_compiled_resources': {'private-cache': object()}}
        report = native.audit_dependencies([self.spec], context,
            {key: [path] for key in keys}, {'dd_rhw': path})
        self.assertEqual(report, native.expected_dependencies([self.spec]))

    def test_mixed_adaptive_runtime_addresses_accept_only_the_exact_optional_union(self):
        from scp.verify import check_emitted_runtime_addresses
        spec = adaptive_fixture.piece()
        spec.update(domain='fixture', native_dd_approaches=True)
        fields = {'CellLayout': ['hab<', '.^..'], 'CheckType': [
            'h - dirtroad: 0x03010000 monorail: 0x01000400, 0xffffffff optional',
            'a - street: 0x02020404 avenue: 0x01000003, 0xffffffff optional',
            'b - dirtroad: 0x03010000'], 'AutoTileBase': ['0x7f580100']}
        self.assertEqual(check_emitted_runtime_addresses(fields, spec)['wrong_model_selections'], 0)
        for rows in (['.ab<', '.^..'], ['hab<', 'h^..']):
            changed = {**fields, 'CellLayout': rows}
            with self.subTest(rows=rows), self.assertRaisesRegex(ValueError, 'Optional construction'):
                check_emitted_runtime_addresses(changed, spec)


def seed_menu_helper(test):
    """Add an exactly frozen RUL1 payload to the existing synthetic menu proof."""
    relative = f'{test.folder}/{menu_fixture.CONTROLLER}'
    resources = strict_dbpf(test.payloads[relative])
    resources[native.RUL1] = b'Native DD helper RUL1 retained exactly\r\n'
    test.payloads[relative] = pack_dbpf(resources)
    (test.source / relative).write_bytes(test.payloads[relative])
    test.base['overlay'][native.OVERLAY] = {'fixture': 'native helper source proof'}
    test.base['files'] = [menu_fixture.fingerprint(path, raw) for path, raw in test.payloads.items()]
    menu_fixture.write_json(test.source / 'manifest.json', test.base)


class NativeApproachSingleMenuTests(unittest.TestCase):
    write_layout = menu_fixture.MenuExperimentTests.write_layout

    def setUp(self):
        menu_fixture.MenuExperimentTests.setUp(self)
        seed_menu_helper(self)

    def test_single_assembly_keeps_helper_controller_bytes_and_manifest_proof(self):
        from scp.menu_experiment import build_assembly_menu
        menu_fixture.MenuExperimentTests.prepare_single_button_layout(self)
        build_assembly_menu(self.project, self.source, self.output, layout_id='fixture-test',
                            plugins=self.plugins, extra_roots=[])
        result = json.loads((self.output / 'manifest.json').read_text())
        self.assertEqual(result['overlay'][native.OVERLAY], self.base['overlay'][native.OVERLAY])
        relative = f'{self.folder}/{menu_fixture.CONTROLLER}'
        self.assertEqual(strict_dbpf((self.output / relative).read_bytes())[native.RUL1],
                         strict_dbpf(self.payloads[relative])[native.RUL1])
        self.assertTrue(self.real_verify(self.output, write_report=False)['static_checks_passed'])


class NativeApproachMultiMenuTests(unittest.TestCase):
    write_layout = menu_fixture.MenuExperimentTests.write_layout
    write_layouts = multi_fixture.MultiAssemblyMenuTests.write_layouts

    def setUp(self):
        multi_fixture.MultiAssemblyMenuTests.setUp(self)
        seed_menu_helper(self)

    def test_three_assembly_cycles_keep_helper_bytes_and_frozen_base_proof(self):
        from scp.menu_experiment import build_assembly_menus
        build_assembly_menus(self.project, self.source, self.output, layout_ids=self.layout_ids,
                             plugins=self.plugins, extra_roots=[])
        result = json.loads((self.output / 'manifest.json').read_text())
        self.assertEqual(result['overlay'][native.OVERLAY], self.base['overlay'][native.OVERLAY])
        relative = f'{self.folder}/{menu_fixture.CONTROLLER}'
        self.assertEqual(strict_dbpf((self.output / relative).read_bytes())[native.RUL1],
                         strict_dbpf(self.payloads[relative])[native.RUL1])
        self.assertTrue(self.real_verify(self.output, write_report=False)['static_checks_passed'])
        changed = strict_dbpf((self.output / relative).read_bytes())
        changed[native.RUL1] += b'tamper'
        raw = pack_dbpf(changed)
        (self.output / relative).write_bytes(raw)
        result['files'] = [menu_fixture.fingerprint(relative, raw) if item['path'] == relative else item
                           for item in result['files']]
        menu_fixture.write_json(self.output / 'manifest.json', result)
        with self.assertRaises(ValueError):
            self.real_verify(self.output, write_report=False)


if __name__ == '__main__':
    unittest.main()
