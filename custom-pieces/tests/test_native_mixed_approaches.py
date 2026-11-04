"""Section-aware native DD/GHSR helpers, tested with synthetic donor bytes."""
from copy import deepcopy
import hashlib
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import native_approaches as native
from scp import adaptive_network as adaptive
from scp.dbpf import encode_exemplar, pack_dbpf
from scp.build import audit_inputs, NETWORK_INI, RUL0
from scp.verify import check_emitted_runtime_addresses
from scp_highway import ghsr_approaches as crossing
from test_native_approaches import model
import test_adaptive_network as adaptive_fixture


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


class MixedNativeApproachTests(unittest.TestCase):
    def setUp(self):
        self.spec = {'id': crossing.PIECE_ID, 'domain': 'highway', 'recipe': crossing.RECIPE,
                     'footprint': [1, 2], 'cells': [[0, 0], [0, 1]],
                     'tile_ids': ['7f5c0000', '7f5c0010'], 'native_ghsr_approaches': True}
        self.baseline = (b'; native bytes retained\r\n[RailMonoRailIntersectionSolutions]\r\n'
                         b'Rot1=0x00010100,0x02000200,0x5dc31500,0,0\r\n'
                         b'; native GHSR marker retained\r\n[MonoRailDirtRoadIntersectionSolutions]\r\n'
                         b'; native DD marker retained\r\n[StreetAvenueIntersectionSolutions]\r\n'
                         b'; adaptive native retained\r\n[Other]\r\nkeep=yes\r\n')
        self.donors = {native.RUL1: self.baseline}
        for target, group, reference in ((0x57530200, 0x6BE08658, 0x27812820),
                                          (0x57530900, 0x6BE08658, 0x27812820),
                                          (0x5DC01A00, 0xEBE084C2, 0x27812823)):
            self.donors[*native.S3D, target] = model()
            self.donors[*native.PATH, target] = (
                b'SC4PATHS\n1.1\n1\n0\n1\n7\n0\n0\n1\n2\n-8,-2.9,1\n2.9,8,1\n'
                if target == 0x5DC01A00 else
                b'SC4PATHS\n1.2\n1\n0\n0\n1\n0\n2\n3\n0\n2\n8,3.2,15\n-3.2,-8,15\n')
            self.donors[0x6534284A, group, target] = encode_exemplar({'parent': [0, 0, 0],
                'properties': [{'id': 0x10, 'type': 0x300, 'key_type': 0, 'values': [11]},
                               {'id': reference, 'type': 0x300, 'key_type': 0x80,
                                'values': [*native.S3D, *([target] * (5 if reference == 0x27812823 else 1))]}]})
        self.domain = SimpleNamespace(approaches=crossing.approaches, rul1_sections=crossing.rul1_sections,
            NATIVE_RUL1_SHA256=sha(self.baseline),
            NATIVE_CONTROLLER_SHA256={crossing.RUL2: sha(b'native RUL2 retained')},
            NATIVE_DEPENDENCY_SHA256={k: sha(v) for k, v in self.donors.items() if k != native.RUL1})
        patcher = patch('scp.native_approaches.domain_module', return_value=self.domain)
        self.provider = patcher.start()
        self.addCleanup(patcher.stop)

    def compose(self, pieces=None, baseline=None):
        return native.compose_rul1(self.baseline if baseline is None else baseline,
                                  [self.spec] if pieces is None else pieces, self.donors)

    def test_metadata_is_opt_in_and_both_legacy_flags_cannot_duplicate_helpers(self):
        for value in (None, 0, 1, 'true', [], {}):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'boolean'):
                native.approaches({**self.spec, 'native_ghsr_approaches': value})
        self.assertEqual(native.approaches({**self.spec, 'native_ghsr_approaches': False}), [])
        with self.assertRaisesRegex(ValueError, 'legacy DD'):
            native.approaches({**self.spec, 'native_dd_approaches': True})
        for field, value in (('id', 'unreviewed'), ('recipe', 'other'), ('domain', 'high-speed-rail'),
                             ('footprint', [2, 1]), ('cells', [[0, 0], [1, 0]])):
            with self.subTest(field=field), self.assertRaises(ValueError):
                native.approaches({**self.spec, field: value})

    def test_four_external_helpers_use_actual_opposite_dd_phases(self):
        rows = native.approaches(self.spec)
        self.assertEqual([(r['cell'], r['native_tile_id'], r['native_rotation']) for r in rows],
                         [([1, 0], '57530900', 2), ([-1, 1], '57530200', 0),
                          ([-1, 0], '5dc01a00', 1), ([1, 1], '5dc01a00', 3)])
        self.assertEqual(len({tuple(r['cell']) for r in rows}), 4)
        self.assertTrue(all(r['cell'] not in self.spec['cells'] for r in rows))
        self.assertTrue(all(r['optional'] and r['experimental'] for r in rows))
        rows[0]['cell'][0] = 99
        self.assertEqual(native.approaches(self.spec)[0]['cell'], [1, 0])

    def test_all_sixteen_helper_poses_match_twelve_deduplicated_section_keys(self):
        sections = native.expected_solution_sections([self.spec])
        self.assertEqual({name: len(rows) for name, rows in sections.items()},
                         {crossing.DD_SECTION: 8, crossing.GHSR_SECTION: 4})
        for row in native.approaches(self.spec):
            for turn in range(4):
                a, b = [adaptive.rotate_flags(int(item['flags'], 16), turn) for item in row['networks']]
                self.assertEqual(sections[row['section']][a, b],
                                 (int(row['native_tile_id'], 16), (row['native_rotation'] + turn) % 4, 0))

    def test_optional_construction_keeps_exact_two_models_and_active_network_flags(self):
        layout, checks, cons = crossing.add_approaches(self.spec, ['a.<', 'b..', '^..'],
            ['a - dirtroad: 0x03010000 monorail: 0x01000003',
             'b - dirtroad: 0x00000301 monorail: 0x00030100'], ['+.<', '+..', '^..'])
        self.assertEqual(layout, ['ja h<'.replace(' ', ''), 'ibk.', '.^..'])
        self.assertEqual(cons, ['.+.<', '.+..', '.^..'])
        fields = {'CellLayout': layout, 'CheckType': checks, 'AutoTileBase': ['0x7f5c0000']}
        report = check_emitted_runtime_addresses(fields, self.spec)
        self.assertEqual((report['cells_checked'], report['wrong_model_selections']), (2, 0))
        self.assertEqual(checks[:2], ['a - dirtroad: 0x03010000 monorail: 0x01000003',
                                     'b - dirtroad: 0x00000301 monorail: 0x00030100'])
        for row in checks[2:]:
            self.assertTrue(row.endswith(', 0xFFFFFFFF optional'))
        for bad in (['a.<', 'bh.', '^..'], ['a.<', 'b..', '.^.']):
            with self.assertRaises(ValueError):
                crossing.add_approaches(self.spec, bad, checks[:2], ['+.<', '+..', '^..'])

    def test_two_section_proof_reverses_in_application_order_and_keeps_native_bytes(self):
        raw, record = self.compose()
        self.assertEqual(record['schema_version'], 2)
        self.assertEqual(len(record['sections']), 2)
        self.assertEqual(len(record['native_dependencies']), 9)
        restored = raw
        for edit in reversed(record['sections']):
            start, length = edit['insertion_offset'], len(edit['insertion'].encode())
            restored = restored[:start] + restored[start + length:]
        self.assertEqual(restored, self.baseline)
        report = native.verify_rul1({native.RUL1: raw}, [self.spec], {native.OVERLAY: record}, self.donors)
        self.assertEqual(report['native_dd_rul1_solutions_checked'], 8)
        self.assertEqual(report['native_ghsr_rul1_solutions_checked'], 4)
        self.assertEqual(report['native_approach_sections_checked'], 2)
        self.assertFalse(report['native_dd_game_behavior_tested'])

    def test_two_sections_compose_with_an_existing_adaptive_avenue_overlay(self):
        ground = adaptive_fixture.piece()
        raw, adaptive_record = adaptive.compose_rul1(self.baseline, [adaptive_fixture.delta(ground)], [ground])
        raw, record = self.compose([self.spec, ground], raw)
        report = native.verify_rul1({native.RUL1: raw}, [self.spec, ground],
                                   {'rul1': adaptive_record, native.OVERLAY: record}, self.donors)
        self.assertEqual(report['adaptive_rul1_solutions_checked'], 4)
        self.assertTrue(report['native_rul1_bytes_preserved'])

    def test_each_native_target_and_its_exact_model_reference_is_required(self):
        self.assertEqual(len(native.dependency_keys([self.spec])), 9)
        for target in (0x57530200, 0x57530900, 0x5DC01A00):
            changed = dict(self.donors)
            del changed[*native.S3D, target]
            with self.subTest(target=hex(target)), self.assertRaisesRegex(ValueError, 'Missing audited'):
                native.compose_rul1(self.baseline, [self.spec], changed)
        key = 0x6534284A, 0xEBE084C2, 0x5DC01A00
        from scp.dbpf import exemplar
        for mutate in ('wrong-reference', 'missing-zoom', 'other-zoom'):
            record = exemplar(self.donors[key])
            if mutate == 'wrong-reference': record['properties'][1]['id'] = '0x27812820'
            elif mutate == 'missing-zoom': record['properties'][1]['values'].pop()
            else: record['properties'][1]['values'][-1] += 1
            changed = {**self.donors, key: encode_exemplar(record)}
            self.domain.NATIVE_DEPENDENCY_SHA256[key] = sha(changed[key])
            with self.subTest(mutation=mutate), self.assertRaisesRegex(ValueError, 'audited native model'):
                native.compose_rul1(self.baseline, [self.spec], changed)

    def test_both_sections_reject_collisions_missing_sections_and_duplicate_headers(self):
        for section in (crossing.DD_SECTION, crossing.GHSR_SECTION):
            row = crossing.rul1_sections(self.spec)[section][0]
            line = f'TYPE9=0x{row[0]:08x},0x{row[1]:08x},0x{row[2]:08x},{row[3]},{row[4]}\r\n'.encode()
            marker = ('[' + section + ']').encode()
            for baseline in (self.baseline.replace(marker, marker + b'\r\n' + line),
                             self.baseline.replace(marker, b'[Renamed]'),
                             self.baseline + marker + b'\r\n'):
                with self.subTest(section=section), self.assertRaises(ValueError):
                    self.compose(baseline=baseline)

    def test_dangling_native_frames_require_the_exact_reviewed_inventory_and_frozen_bytes(self):
        from scp.models import parse_s3d, pack_s3d
        key = *native.S3D, 0x5DC01A00
        parsed = parse_s3d(self.donors[key])
        parsed['meshes'].append({'name': b'Historical ignored frame\0', 'flags': 0,
                                 'frames': [(1, 1, 1, 1)]})
        self.donors[key] = pack_s3d(parsed)
        self.domain.NATIVE_DEPENDENCY_SHA256[key] = sha(self.donors[key])
        with self.assertRaisesRegex(ValueError, 'invalid render references'):
            self.compose()
        self.domain.NATIVE_IGNORED_MODEL_FRAMES = {key: ((1, 0, (1, 1, 1, 1)),)}
        self.compose()
        self.domain.NATIVE_IGNORED_MODEL_FRAMES[key] = ((0, 0, (1, 1, 1, 1)),)
        with self.assertRaisesRegex(ValueError, 'invalid render references'):
            self.compose()
        self.domain.NATIVE_IGNORED_MODEL_FRAMES[key] = ((1, 0, (1, 1, 1, 1)),)
        self.donors[key] += b'tamper'
        with self.assertRaises(ValueError):
            self.compose()

    def test_native_continuation_rejects_changed_controller_bytes_and_missing_propagators(self):
        rows = [
            '0x5dc01a00,1,0,0x0d001a00,1,0=0x5dc01a00,1,0,0x5dc01a00,3,0',
            '0x5dc01a00,2,0,0x0d001a00,2,0=0x5dc01a00,2,0,0x5dc01a00,0,0',
            '0x57530200,0,0,0x57000200,2,0=0x57530200,0,0,0x57530900,2,0',
            '0x57530200,3,0,0x57000200,1,0=0x57530200,3,0,0x57530900,1,0',
            '0x57530900,0,0,0x57000200,2,0=0x57530900,0,0,0x57530200,2,0',
            '0x57530900,3,0,0x57000200,1,0=0x57530900,3,0,0x57530200,1,0',
        ]
        raw = ('\r\n'.join(rows) + '\r\n').encode()
        with patch.object(crossing, 'NATIVE_RUL2_SHA256', sha(raw)):
            report = crossing.check_native_continuation({crossing.RUL2: raw})
            self.assertEqual(report['native_continuation_rows_checked'], 6)
            self.assertFalse(report['game_behavior_tested'])
            with self.assertRaisesRegex(ValueError, 'pinned'):
                crossing.check_native_continuation({crossing.RUL2: raw + b'foreign'})
        changed = raw.replace(rows[2].encode(), b'; removed native DD phase propagator')
        with patch.object(crossing, 'NATIVE_RUL2_SHA256', sha(changed)):
            with self.assertRaisesRegex(ValueError, 'continuation rows'):
                crossing.check_native_continuation({crossing.RUL2: changed})

    def test_new_opt_in_requires_real_ghsr_dependency_closure_and_rejects_foreign_overrides(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            payloads = {
                'controller': {RUL0: b'native RUL0', NETWORK_INI: b'native INI', native.RUL1: self.baseline,
                               crossing.RUL2: b'native RUL2 retained'},
                'dd_rhw': {k: v for k, v in self.donors.items() if k[2] in (0x57530200, 0x57530900)},
                'hsr': {k: v for k, v in self.donors.items() if k[2] == 0x5DC01A00},
            }
            files = {}
            for label, resources in payloads.items():
                path = root / ('NetworkAddonMod_Controller.dat' if label == 'controller' else label + '.dat')
                path.write_bytes(pack_dbpf(resources))
                files[label] = {'filename': path.name, 'sha256': sha(path.read_bytes())}
            catalog = {'_root': root, 'plugin_folder': 'zzz_Simons_Custom_Pieces',
                       '_profile': {'files': files}}
            spec = {**self.spec, 'dependencies': ['controller', 'dd_rhw', 'hsr']}
            audit_inputs(catalog, root, [spec], extra_roots=[])
            foreign = root / 'foreign.dat'
            foreign.write_bytes(pack_dbpf({native.RUL1: b'foreign RUL1'}))
            with self.assertRaisesRegex(ValueError, 'Conflicting shared NAM overlay'):
                audit_inputs(catalog, root, [spec], extra_roots=[])
            foreign.write_bytes(pack_dbpf({(*native.S3D, 0x5DC01A00): b'foreign GHSR model'}))
            with self.assertRaisesRegex(ValueError, 'Foreign or missing native DD'):
                audit_inputs(catalog, root, [spec], extra_roots=[])
            for raw in (b'foreign RUL2', b'native RUL2 retained'):
                foreign.write_bytes(pack_dbpf({crossing.RUL2: raw}))
                with self.subTest(foreign=raw), self.assertRaisesRegex(ValueError, 'Conflicting shared NAM overlay'):
                    audit_inputs(catalog, root, [spec], extra_roots=[])
            # A legacy selection has no new continuation requirement. Keep
            # its historical admission behavior even with a foreign RUL2.
            legacy = {**spec, 'native_ghsr_approaches': False}
            audit_inputs(catalog, root, [legacy], extra_roots=[])
            foreign.unlink()
            payloads['controller'][crossing.RUL2] = b'changed native RUL2'
            controller_path = root / files['controller']['filename']
            controller_path.write_bytes(pack_dbpf(payloads['controller']))
            files['controller']['sha256'] = sha(controller_path.read_bytes())
            with self.assertRaisesRegex(ValueError, 'Native approach controller dependency changed'):
                audit_inputs(catalog, root, [spec], extra_roots=[])

    def test_section_proof_mutations_and_native_tampering_fail_with_frozen_donors_absent(self):
        raw, record = self.compose()
        for case in ('order', 'offset', 'section', 'declaration', 'dependency', 'extra', 'native'):
            proof, changed = deepcopy(record), raw
            if case == 'order': proof['sections'].reverse()
            elif case == 'offset': proof['sections'][0]['insertion_offset'] = True
            elif case == 'section': proof['sections'][1]['section'] = crossing.DD_SECTION
            elif case == 'declaration': proof['selected_declarations'][0]['approaches'][1]['native_tile_id'] = '57530900'
            elif case == 'dependency': proof['native_dependencies'][0]['sha256'] = '0' * 64
            elif case == 'extra': proof['sections'][0]['extra'] = True
            else:
                changed = raw.replace(b'keep=yes', b'keep=bad')
                proof['base_sha256'] = sha(changed)
            with self.subTest(case=case), self.assertRaises(ValueError):
                native.verify_rul1({native.RUL1: changed}, [self.spec], {native.OVERLAY: proof}, {})


if __name__ == '__main__':
    unittest.main()
