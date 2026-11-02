"""Native-row reuse proofs, direct lookup, and unchanged legacy helper bytes.

Portable controls use explicitly synthetic native bytes and donor pins. The
separate optional integration class rereads original NAM 50 inputs and makes
no installation or live-game claim.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = next(path for path in Path(__file__).resolve().parents if (path / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))

from scp import adaptive_network as adaptive, jsonc, native_approaches as native
from scp.build import audit_inputs, NETWORK_INI
from scp.dbpf import entries, decompress, encode_exemplar, pack_dbpf
from scp.paths import local_settings
from scp_highway import orthogonal_approaches as orthogonal
import test_adaptive_network as adaptive_fixture
import test_native_approaches as legacy_fixture
import test_native_mixed_approaches as mixed_fixture


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def specification(variant='original'):
    cells = [[x, y] for y in range(6) for x in range(2)]
    piece = {'id': 'ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile', 'domain': 'highway',
            'recipe': 'highway_ddrhw_orthogonal_l0_transition', 'footprint': [2, 6], 'cells': cells,
            'tile_ids': [f'{0x7f600000 + 0x100 * x + 0x10 * y:08x}' for x, y in cells],
            'native_orthogonal_approaches': True}
    if variant == 'mirrored':
        piece.update(id=piece['id'] + '-mirrored', recipe=piece['recipe'] + '_mirrored',
                     transition_variant='mirrored')
    return piece


# Exact literal original starter rows, kept independent of provider generation.
TABLES = {
    'MonoRailDirtRoadIntersectionSolutions': (
        (0x01000400, 0x02000200, 0x57530000, 0, 0),
        (0x00040001, 0x00020002, 0x57530000, 1, 0),
        (0x04000100, 0x02000200, 0x57530000, 2, 0),
        (0x00010004, 0x00020002, 0x57530000, 3, 0)),
    'RoadDirtRoadIntersectionSolutions': (
        (0x01000001, 0x02000200, 0x57030000, 0, 0),
        (0x00000101, 0x00020002, 0x57030000, 1, 0),
        (0x00010100, 0x02000200, 0x57030000, 2, 0),
        (0x01010000, 0x00020002, 0x57030000, 3, 0)),
}


def synthetic_baseline():
    lines = ['; synthetic retained native bytes']
    for section, rows in TABLES.items():
        lines.append('[' + section + ']')
        lines.extend(f'TYPE{i}=0x{a:08X},0x{b:08X},0x{c:08X},{d},{e}'
                     for i, (a, b, c, d, e) in enumerate(rows, 1))
    lines.extend(['[StreetAvenueIntersectionSolutions]', '; adaptive retained', '[Other]', 'keep=yes', ''])
    return '\r\n'.join(lines).encode('ascii')


class NativeOrthogonalProofTests(unittest.TestCase):
    def setUp(self):
        self.spec = specification()
        self.baseline = synthetic_baseline()
        self.donors = {native.RUL1: self.baseline}
        for target, reference in ((0x57530000, True), (0x57030000, False), (0x57530900, True)):
            self.donors[*native.S3D, target] = legacy_fixture.model()
            self.donors[*native.PATH, target] = b'SC4PATHS\n1.1\n1\n0\n0\n1\n1\n0\n2\n2\n-8,15,0\n8,15,0\n'
            if reference:
                self.donors[*native.NETWORK_EXEMPLAR, target] = encode_exemplar({
                    'parent': [0, 0, 0], 'properties': [
                        {'id': 0x10, 'type': 0x300, 'key_type': 0, 'values': [11]},
                        {'id': 0x27812820, 'type': 0x300, 'key_type': 0x80, 'values': [*native.S3D, target]}]})
        self.existing = deepcopy(TABLES)
        self.domain = SimpleNamespace(
            approaches=orthogonal.approaches, rul1_sections=orthogonal.rul1_sections,
            existing_rul1_sections=lambda piece: self.existing,
            NATIVE_RUL1_SHA256=sha(self.baseline),
            NATIVE_DEPENDENCY_SHA256={key: sha(self.donors[key]) for key in orthogonal.NATIVE_DEPENDENCY_SHA256})
        self.legacy_spec = {'id': 'legacy-helper-fixture', 'domain': 'fixture', 'native_dd_approaches': True}
        self.legacy_declaration = [{'cell': [-1, 0], 'end_cell': [0, 0], 'end_tile_id': '7f5b3010',
            'outward_edge': 0, 'native_tile_id': '57530900', 'native_rotation': 0,
            'monorail_flags': '01000400', 'dirtroad_flags': '03010000', 'optional': True, 'experimental': True}]
        self.legacy = SimpleNamespace(
            approaches=lambda piece: deepcopy(self.legacy_declaration),
            rul1_rows=lambda piece: tuple((adaptive.rotate_flags(0x01000400, turn),
                adaptive.rotate_flags(0x03010000, turn), 0x57530900, turn, 0) for turn in range(4)),
            NATIVE_RUL1_SHA256=sha(self.baseline),
            NATIVE_DEPENDENCY_SHA256={key: sha(value) for key, value in self.donors.items() if key[2] == 0x57530900})
        patcher = patch('scp.native_approaches.domain_module', side_effect=lambda piece, feature:
                        self.domain if feature == 'orthogonal_approaches' else self.legacy)
        self.provider = patcher.start()
        self.addCleanup(patcher.stop)

    def compose(self, pieces=None, raw=None):
        return native.compose_rul1(self.baseline if raw is None else raw,
                                  [self.spec] if pieces is None else pieces, self.donors)

    def verify(self, raw, record, pieces=None, donors=None):
        return native.verify_rul1({native.RUL1: raw}, [self.spec] if pieces is None else pieces,
                                 {native.OVERLAY: record}, self.donors if donors is None else donors)

    def test_absent_and_false_do_not_load_an_orthogonal_provider_or_change_legacy_results(self):
        for piece in ({'id': 'old'}, {'id': 'disabled', native.ORTHOGONAL_OVERLAY: False}):
            self.assertEqual(native.approaches(piece), [])
            self.assertEqual(native.compose_rul1(self.baseline, [piece], {}), (self.baseline, None))
            self.assertEqual(native.verify_rul1({}, [piece], {}, {}), {'adaptive_rul1_solutions_checked': 0})
        self.provider.assert_not_called()

    def test_opt_in_routes_exact_provider_and_rejects_non_booleans_and_combined_modes(self):
        self.assertEqual(native.approaches(self.spec), orthogonal.approaches(self.spec))
        self.provider.assert_called_with(self.spec, 'orthogonal_approaches')
        for value in (0, 1, None, 'true', [], {}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                native.approaches({**self.spec, native.ORTHOGONAL_OVERLAY: value})
        for mode in (native.OVERLAY, native.GHSR_OVERLAY):
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                native.approaches({**self.spec, mode: True})

    def test_direct_mode_has_five_dependencies_and_is_forbidden_without_explicit_orthogonal_opt_in(self):
        expected = {(*native.S3D, target) for target in (0x57530000, 0x57030000)}
        expected.update({(*native.PATH, target) for target in (0x57530000, 0x57030000)})
        expected.add((*native.NETWORK_EXEMPLAR, 0x57530000))
        self.assertEqual(native.dependency_keys([self.spec]), expected)
        self.assertEqual(len(native.dependency_records([self.spec], self.donors)), 5)
        self.legacy_declaration[0]['native_model_reference'] = 'direct'
        with self.assertRaisesRegex(ValueError, 'explicit reviewed orthogonal'):
            native.dependency_keys([self.legacy_spec])

    def test_missing_corrupt_or_extra_dependency_pins_fail_closed(self):
        for key in native.dependency_keys([self.spec]):
            changed = dict(self.donors); del changed[key]
            with self.subTest(missing=key), self.assertRaises(ValueError):
                native.compose_rul1(self.baseline, [self.spec], changed)
        changed = dict(self.donors); changed[*native.S3D, 0x57030000] += b'changed'
        with self.assertRaises(ValueError):
            native.compose_rul1(self.baseline, [self.spec], changed)
        self.domain.NATIVE_DEPENDENCY_SHA256[*native.NETWORK_EXEMPLAR, 0x57030000] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'exactly cover'):
            self.compose()

    def test_input_audit_requires_ground_donors_and_rejects_foreign_models_paths_or_controllers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            self.domain.NATIVE_CONTROLLER_SHA256 = {
                orthogonal.RUL0: sha(b'synthetic native RUL0'), orthogonal.RUL2: sha(b'synthetic native RUL2')}
            payloads = {
                'controller': {orthogonal.RUL0: b'synthetic native RUL0', native.RUL1: self.baseline,
                               orthogonal.RUL2: b'synthetic native RUL2', NETWORK_INI: b'synthetic native INI'},
                'dd_rhw': {key: value for key, value in self.donors.items() if key[2] == 0x57530000},
                'rhw4': {key: value for key, value in self.donors.items() if key[2] == 0x57030000},
            }
            records = {}
            for label, resources in payloads.items():
                path = root / ('NetworkAddonMod_Controller.dat' if label == 'controller' else label + '.dat')
                path.write_bytes(pack_dbpf(resources))
                records[label] = {'filename': path.name, 'sha256': sha(path.read_bytes())}
            catalog = {'_root': root, 'plugin_folder': 'zzz_Simons_Custom_Pieces', '_profile': {'files': records}}
            piece = {**self.spec, 'dependencies': ['controller', 'dd_rhw', 'rhw4']}
            audit_inputs(catalog, root, [piece], extra_roots=[])
            foreign = root / 'foreign.dat'
            for key, raw in [((*native.S3D, 0x57030000), self.donors[*native.S3D, 0x57030000]),
                             ((*native.PATH, 0x57030000), self.donors[*native.PATH, 0x57030000]),
                             (native.RUL1, self.baseline), (orthogonal.RUL2, b'synthetic native RUL2')]:
                foreign.write_bytes(pack_dbpf({key: raw}))
                with self.subTest(key=key), self.assertRaises(ValueError):
                    audit_inputs(catalog, root, [piece], extra_roots=[])
            # Native 57030000 has no network exemplar. A foreign exemplar
            # changes direct lookup identity even if its model reference is
            # numerically correct, or its group differs from known groups.
            for group in (0x6BE08658, 0xEBE084C2, 0x12345678):
                raw = encode_exemplar({'parent': [0, 0, 0], 'properties': [
                    {'id': 0x10, 'type': 0x300, 'key_type': 0, 'values': [11]},
                    {'id': 0x27812820, 'type': 0x300, 'key_type': 0x80,
                     'values': [*native.S3D, 0x57030000]}]})
                foreign.write_bytes(pack_dbpf({(0x6534284A, group, 0x57030000): raw}))
                with self.subTest(exemplar_group=group), self.assertRaisesRegex(ValueError, 'Direct native lookup'):
                    audit_inputs(catalog, root, [piece], extra_roots=[])
            foreign.unlink()
            (root / 'rhw4.dat').unlink()
            with self.assertRaisesRegex(ValueError, 'Expected one rhw4.dat'):
                audit_inputs(catalog, root, [piece], extra_roots=[])

    def test_reuse_only_schema_three_preserves_every_rul1_byte(self):
        before = deepcopy(self.spec)
        raw, proof = self.compose()
        self.assertEqual(raw, self.baseline)
        self.assertEqual(proof['schema_version'], 3)
        self.assertEqual(proof['sections'], [])
        self.assertEqual(proof['base_sha256'], sha(self.baseline))
        self.assertEqual(proof['existing_native_solutions'], [
            {'section': section, 'native_solutions': [list(row) for row in sorted(rows)]}
            for section, rows in sorted(TABLES.items())])
        report = self.verify(raw, proof)
        self.assertEqual(report['native_approach_cells_checked'], 3)
        self.assertEqual(report['native_dd_approach_cells_checked'], 1)
        self.assertEqual(report['native_ground_rhw_approach_cells_checked'], 2)
        self.assertEqual(report['native_approach_dependencies_checked'], 5)
        self.assertEqual(report['native_dd_dependencies_checked'], 3)
        self.assertEqual(report['native_ground_rhw_dependencies_checked'], 2)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 8)
        self.assertEqual(report['native_rul1_solutions_checked'], 8)
        self.assertFalse(report['native_dd_game_behavior_tested'])
        self.assertEqual(self.spec, before)

    def test_paired_variants_reuse_exactly_eight_rows_and_five_dependencies_without_insertion(self):
        pieces = [self.spec, specification('mirrored')]
        raw, proof = self.compose(pieces)
        self.assertEqual(raw, self.baseline)
        self.assertEqual(proof['sections'], [])
        self.assertEqual(len(proof['selected_declarations']), 2)
        self.assertEqual(len(proof['native_dependencies']), 5)
        self.assertEqual(sum(len(row['native_solutions']) for row in proof['existing_native_solutions']), 8)
        mirrored = proof['selected_declarations'][1]['approaches'][0]
        self.assertEqual((mirrored['cell'], mirrored['native_rotation'], mirrored['networks'][0]['flags']),
                         ([0, -1], 2, '04000100'))
        report = self.verify(raw, proof, pieces)
        self.assertEqual(report['native_approach_cells_checked'], 6)
        self.assertEqual(report['native_dd_approach_cells_checked'], 2)
        self.assertEqual(report['native_ground_rhw_approach_cells_checked'], 4)
        self.assertEqual(report['native_approach_dependencies_checked'], 5)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 8)
        changed = deepcopy(proof)
        changed['selected_declarations'][1]['approaches'][0]['native_rotation'] = 0
        with self.assertRaises(ValueError):
            self.verify(raw, changed, pieces)

    def test_mirrored_only_and_mixed_legacy_pair_preserve_native_and_legacy_insertions(self):
        mirrored = specification('mirrored')
        raw, proof = self.compose([mirrored])
        self.assertEqual(raw, self.baseline)
        self.assertEqual(self.verify(raw, proof, [mirrored])['native_approach_cells_checked'], 3)
        old_raw, old_proof = self.compose([self.legacy_spec])
        raw, proof = self.compose([self.legacy_spec, self.spec, mirrored])
        self.assertEqual(raw, old_raw)
        self.assertEqual(proof['sections'], [{key: old_proof[key] for key in
            ('section', 'native_solutions', 'insertion_offset', 'insertion')}])
        report = self.verify(raw, proof, [self.legacy_spec, self.spec, mirrored])
        self.assertEqual(report['native_rul1_solutions_checked'], 12)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 8)

    def test_reused_native_rows_must_exist_once_with_exact_target_pose_and_no_reflection(self):
        row = b'TYPE1=0x01000400,0x02000200,0x57530000,0,0\r\n'
        for replacement in (b'', row + row, row + row.replace(b'TYPE1=', b'OTHER='),
                            row.replace(b'57530000', b'57530900'), row.replace(b',0,0', b',2,0'),
                            row.replace(b',0,0', b',0,1')):
            with self.subTest(replacement=replacement), self.assertRaisesRegex(ValueError, 'missing, changed, or ambiguous'):
                self.compose(raw=self.baseline.replace(row, replacement))

    def test_missing_duplicate_or_renamed_native_sections_are_rejected(self):
        for section in TABLES:
            marker = ('[' + section + ']').encode()
            for raw in (self.baseline.replace(marker, b'[Renamed]'), self.baseline + marker + b'\r\n'):
                with self.subTest(section=section), self.assertRaises(ValueError):
                    self.compose(raw=raw)

    def test_provider_existing_rows_must_exactly_cover_declarations(self):
        cases = []
        changed = deepcopy(TABLES); changed.pop('RoadDirtRoadIntersectionSolutions'); cases.append(changed)
        changed = deepcopy(TABLES); changed[orthogonal.DD_SECTION] = changed[orthogonal.DD_SECTION][:-1]; cases.append(changed)
        changed = deepcopy(TABLES); changed[orthogonal.DD_SECTION] += changed[orthogonal.DD_SECTION][:1]; cases.append(changed)
        changed = deepcopy(TABLES); first = changed[orthogonal.DD_SECTION][0]; changed[orthogonal.DD_SECTION] = ((*first[:3], 2, 0), *changed[orthogonal.DD_SECTION][1:]); cases.append(changed)
        changed = deepcopy(TABLES); first = changed[orthogonal.DD_SECTION][0]; changed[orthogonal.DD_SECTION] = ((*first[:4], 1), *changed[orthogonal.DD_SECTION][1:]); cases.append(changed)
        changed = deepcopy(TABLES); changed['UnreviewedSection'] = changed.pop(orthogonal.GROUND_SECTION); cases.append(changed)
        for value in ({}, None, [], *cases):
            self.existing = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.compose()

    def test_schema_three_rejects_forged_reuse_dependency_declaration_or_native_baseline(self):
        raw, original = self.compose()
        for case in ('missing-reuse', 'empty-reuse', 'reuse-order', 'reuse-pose', 'duplicate-reuse',
                     'section', 'dependency', 'declaration', 'extra', 'schema-bool', 'game-bool',
                     'fake-insertion', 'native-retained-bytes'):
            proof, changed = deepcopy(original), raw
            if case == 'missing-reuse': del proof['existing_native_solutions']
            elif case == 'empty-reuse': proof['existing_native_solutions'] = []
            elif case == 'reuse-order': proof['existing_native_solutions'].reverse()
            elif case == 'reuse-pose': proof['existing_native_solutions'][0]['native_solutions'][0][3] ^= 2
            elif case == 'duplicate-reuse': proof['existing_native_solutions'].append(deepcopy(proof['existing_native_solutions'][0]))
            elif case == 'section': proof['existing_native_solutions'][0]['section'] = orthogonal.GROUND_SECTION
            elif case == 'dependency': proof['native_dependencies'][0]['sha256'] = '0' * 64
            elif case == 'declaration': proof['selected_declarations'][0]['approaches'][1]['native_rotation'] = 2
            elif case == 'extra': proof['unexpected'] = True
            elif case == 'schema-bool': proof['schema_version'] = True
            elif case == 'game-bool': proof['game_behavior_tested'] = 0
            elif case == 'fake-insertion': proof['sections'] = [{'insertion': 'foreign', 'insertion_offset': 0}]
            else:
                changed = raw.replace(b'keep=yes', b'keep=bad')
                proof['base_sha256'] = sha(changed)
            with self.subTest(case=case), self.assertRaises(ValueError):
                self.verify(changed, proof, donors={})

    def test_mixed_new_and_legacy_helpers_keep_only_the_legacy_insertion_bytes(self):
        legacy_raw, legacy_proof = self.compose([self.legacy_spec])
        raw, proof = self.compose([self.legacy_spec, self.spec])
        self.assertEqual(raw, legacy_raw)
        self.assertEqual(proof['schema_version'], 3)
        self.assertEqual(proof['sections'], [{key: legacy_proof[key] for key in
            ('section', 'native_solutions', 'insertion_offset', 'insertion')}])
        self.assertEqual(sum(len(item['native_solutions']) for item in proof['existing_native_solutions']), 8)
        self.assertEqual(len(proof['native_dependencies']), 8)
        report = self.verify(raw, proof, [self.legacy_spec, self.spec])
        self.assertEqual(report['native_rul1_solutions_checked'], 12)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 8)
        changed = deepcopy(proof); changed['sections'][0]['insertion_offset'] += 1
        with self.assertRaises(ValueError):
            self.verify(raw, changed, [self.legacy_spec, self.spec])

    def test_orthogonal_reuse_composes_with_the_independent_adaptive_overlay(self):
        ground = adaptive_fixture.piece()
        current, ground_proof = adaptive.compose_rul1(self.baseline, [adaptive_fixture.delta(ground)], [ground])
        raw, proof = self.compose([self.spec, ground], current)
        self.assertEqual(raw, current)
        self.assertEqual(proof['sections'], [])
        report = native.verify_rul1({native.RUL1: raw}, [self.spec, ground],
            {native.OVERLAY: proof, 'rul1': ground_proof}, self.donors)
        self.assertEqual(report['adaptive_rul1_solutions_checked'], 4)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 8)

    def test_schema_one_and_two_match_previous_implementation_golden_bytes_and_proofs(self):
        # Independently measured from the preceding committed implementation
        # using these preexisting synthetic fixtures; no Git is needed here.
        cases = [
            (legacy_fixture.NativeApproachTests, 1,
             '608fd0a2125524ca084a7d82c12e16f8e6109ee58c92179ef6ea23ddcaf065ea',
             '0f98efb9e72610093f90ccbc60d26ac6844baed885ce7fc3d9be689eb6f38a34'),
            (mixed_fixture.MixedNativeApproachTests, 2,
             '452275fd9cc80fd14926af4240bc640ab015b32269a840eb2dc6e888dea7dd88',
             '40158a24c3b54a6095bdd26a6d637a93eef182c3da64e939025f8ae42a0ea3b5'),
        ]
        for cls, schema, raw_sha, proof_sha in cases:
            fixture = cls(); fixture.setUp()
            try:
                raw, proof = fixture.compose()
                self.assertEqual(proof['schema_version'], schema)
                self.assertEqual(sha(raw), raw_sha)
                self.assertEqual(sha(json.dumps(proof, sort_keys=True, separators=(',', ':')).encode()), proof_sha)
            finally:
                fixture.doCleanups()


class ActualNativeOrthogonalProofTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings_path = local_settings(ROOT)
        if not settings_path.is_file():
            raise unittest.SkipTest('Original NAM 50 inputs are unavailable in this source-only checkout')
        settings = jsonc.load(settings_path)
        roots = [Path(settings['plugins']).expanduser(), *(Path(item).expanduser() for item in settings.get('extra_plugins', []))]
        cls.archives, cls.donors = {}, {}
        for name in ('NetworkAddonMod_Controller.dat', 'RealHighway_DD_RHW-4.dat',
                     'RealHighway_RHW-4.dat', 'High Speed Rail.dat'):
            matches = list({path for root in roots if root.is_dir() for path in root.rglob(name)})
            if len(matches) != 1:
                raise unittest.SkipTest('Exactly one original ' + name + ' is required for native integration')
            data = {key: decompress(value) for key, value in entries(matches[0].read_bytes()).items()}
            cls.archives[name] = data
            cls.donors.update(data)
        cls.baseline = cls.donors[native.RUL1]
        if sha(cls.baseline) != orthogonal.NATIVE_RUL1_SHA256:
            raise ValueError('Original NAM 50 RUL1 fingerprint changed')

    def test_original_native_rul1_bytes_are_identical_for_transition_only_with_five_real_dependencies(self):
        raw, proof = native.compose_rul1(self.baseline, [specification()], self.donors)
        self.assertEqual(raw, self.baseline)
        self.assertEqual(proof['schema_version'], 3)
        self.assertEqual(proof['sections'], [])
        self.assertEqual(len(proof['native_dependencies']), 5)
        self.assertEqual(sum(len(item['native_solutions']) for item in proof['existing_native_solutions']), 8)
        report = native.verify_rul1({native.RUL1: raw}, [specification()], {native.OVERLAY: proof}, self.donors)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 8)
        self.assertTrue(report['native_rul1_bytes_preserved'])
        self.assertFalse(report['native_dd_game_behavior_tested'])
        self.assertEqual(native.required_controller_resources([specification()]), {
            orthogonal.RUL0: orthogonal.NATIVE_RUL0_SHA256, orthogonal.RUL2: orthogonal.NATIVE_RUL2_SHA256})

    def test_actual_native_paired_variants_keep_rul1_byte_identity_and_shared_dependency_roster(self):
        pieces = [specification(), specification('mirrored')]
        raw, proof = native.compose_rul1(self.baseline, pieces, self.donors)
        self.assertEqual(raw, self.baseline)
        self.assertEqual(proof['sections'], [])
        self.assertEqual(len(proof['selected_declarations']), 2)
        self.assertEqual(len(proof['native_dependencies']), 5)
        report = native.verify_rul1({native.RUL1: raw}, pieces, {native.OVERLAY: proof}, self.donors)
        self.assertEqual(report['native_approach_cells_checked'], 6)
        self.assertEqual(report['native_approach_dependencies_checked'], 5)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 8)
        self.assertFalse(report['native_dd_game_behavior_tested'])

    def test_all_registered_legacy_highway_helpers_keep_native_bytes_and_schema_when_disabled(self):
        pieces = [jsonc.load(path) for path in sorted((ROOT / 'domains/highway/00_pieces').glob('*/piece.jsonc'))]
        pieces = [piece for piece in pieces if piece['id'] not in (orthogonal.PIECE_ID, orthogonal.MIRRORED_PIECE_ID)]
        original = deepcopy(pieces)
        old_raw, old_proof = native.compose_rul1(self.baseline, pieces, self.donors)
        self.assertEqual(old_proof['schema_version'], 2)
        for mode in ('absent', 'false'):
            selected = deepcopy(pieces)
            for piece in selected:
                if mode == 'false': piece[native.ORTHOGONAL_OVERLAY] = False
            raw, proof = native.compose_rul1(self.baseline, selected, self.donors)
            self.assertEqual(raw, old_raw)
            self.assertEqual(proof, old_proof)
        self.assertEqual(pieces, original)

    def test_transition_and_all_registered_legacy_helpers_preserve_every_old_insertion(self):
        pieces = [jsonc.load(path) for path in sorted((ROOT / 'domains/highway/00_pieces').glob('*/piece.jsonc'))]
        pieces = [piece for piece in pieces if piece['id'] not in (orthogonal.PIECE_ID, orthogonal.MIRRORED_PIECE_ID)]
        expected_ground = adaptive.expected_solutions(pieces)
        delta = '\r\n'.join([f'TYPE{i}=0x{a:08x},0x{b:08x},0x{c:08x},{d},{e}'
            for i, ((a, b), (c, d, e)) in enumerate(expected_ground.items())] + [''])
        baseline, ground_proof = adaptive.compose_rul1(self.baseline, [delta], pieces)
        old_raw, old_proof = native.compose_rul1(baseline, pieces, self.donors)
        raw, proof = native.compose_rul1(baseline, [*pieces, specification()], self.donors)
        self.assertEqual(raw, old_raw)
        self.assertEqual(proof['schema_version'], 3)
        self.assertEqual(proof['sections'], old_proof['sections'])
        report = native.verify_rul1({native.RUL1: raw}, [*pieces, specification()],
                                   {native.OVERLAY: proof, 'rul1': ground_proof}, self.donors)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 8)
        self.assertEqual(report['adaptive_rul1_solutions_checked'], len(expected_ground))
        self.assertFalse(report['native_dd_game_behavior_tested'])

    def test_retained_fifty_two_type_build_keeps_exact_saved_schema_two_and_rul1_bytes(self):
        build = ROOT / 'dist/ddrhw-ghsr-parallel-a-b-parts-final-02'
        path = build / 'manifest.json'
        if not path.is_file():
            self.skipTest('The retained historical 52-type build is not included in a source-only checkout')
        self.assertEqual(sha(path.read_bytes()), 'ae913d83fa8eaeee24d7643b924e0f0e22f5f411181f6c274cea78ad8b6fe834')
        frozen = json.loads(path.read_text())
        controller_record = next(item for item in frozen['files'] if item['path'].endswith('/00_SCP_Controller_NAM50.dat'))
        controller_path = build / controller_record['path']
        self.assertEqual(sha(controller_path.read_bytes()), controller_record['sha256'])
        saved = {key: decompress(value) for key, value in entries(controller_path.read_bytes()).items()}
        source = {piece['id']: piece for piece in (jsonc.load(path) for path in
                  (ROOT / 'domains/highway/00_pieces').glob('*/piece.jsonc'))}
        pieces = [source[piece['id']] for piece in frozen['pieces']]
        self.assertEqual(len(pieces), 52)
        original_proof = frozen['overlay'][native.OVERLAY]
        self.assertEqual(original_proof['schema_version'], 2)
        native.verify_rul1(saved, pieces, frozen['overlay'], self.donors)
        baseline = saved[native.RUL1]
        for edit in reversed(original_proof['sections']):
            start, inserted = edit['insertion_offset'], edit['insertion'].encode('ascii')
            self.assertEqual(baseline[start:start + len(inserted)], inserted)
            baseline = baseline[:start] + baseline[start + len(inserted):]
        current, proof = native.compose_rul1(baseline, pieces, self.donors)
        self.assertEqual(current, saved[native.RUL1])
        self.assertEqual(proof, original_proof)
        current, proof = native.compose_rul1(baseline, [*pieces, specification()], self.donors)
        self.assertEqual(current, saved[native.RUL1])
        self.assertEqual(proof['sections'], original_proof['sections'])
        self.assertEqual(proof['schema_version'], 3)
        report = native.verify_rul1({**saved, native.RUL1: current}, [*pieces, specification()],
            {**frozen['overlay'], native.OVERLAY: proof}, self.donors)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 8)


class RegisteredOrthogonalVariantMenuTests(unittest.TestCase):
    def test_each_registered_variant_has_one_unambiguous_recipe_owner_name_and_directory(self):
        from scp.subject_sources import piece_id_for_recipe, piece_name_for_recipe, piece_directory
        for recipe, identifier, name_fragment in ((orthogonal.RECIPE, orthogonal.PIECE_ID, 'Orthogonal Combined Transition'),
                                                  (orthogonal.MIRRORED_RECIPE, orthogonal.MIRRORED_PIECE_ID, 'Mirrored Orthogonal Transition')):
            with self.subTest(recipe=recipe):
                self.assertEqual(piece_id_for_recipe(recipe, ROOT), identifier)
                self.assertIn(name_fragment, piece_name_for_recipe(recipe, 'unused fallback', ROOT))
                self.assertEqual(piece_directory(recipe, ROOT), ROOT / 'domains/highway/00_pieces' / identifier)

    def test_registered_pair_uses_one_original_button_and_sixteen_unmodified_rotation_states(self):
        from scp.catalog import load_catalog
        from scp import piece_menu_families as families
        from scp.rul0 import compose_rul0
        import test_piece_menu_families as fixture
        catalog = load_catalog(ROOT)
        by_id = {piece['id']: piece for piece in catalog['pieces']}
        original, mirrored = (by_id[name] for name in (orthogonal.PIECE_ID, orthogonal.MIRRORED_PIECE_ID))
        self.assertNotIn('family_anchor', original['menu'])
        self.assertEqual(mirrored['menu']['family_anchor'], original['id'])
        self.assertEqual(catalog['piece_sets']['ddrhw-orthogonal-ground-transition'], [original['id'], mirrored['id']])
        for selected in ([original, mirrored], [mirrored, original]):
            raw, metadata = compose_rul0(fixture.NATIVE, [fixture.fragment(int(piece['puzzle_id'], 16)) for piece in selected])
            menus = {key: value for piece in selected for key, value in fixture.menu_fixture.menu_resource(piece).items()}
            changed, proof, presentations, record = families.apply(raw, metadata, menus, selected, available=catalog['pieces'])
            rows = fixture.rows(proof['ordering_insertion'])
            self.assertEqual([(kind, states[0]) for kind, states in rows],
                             [('rotationring', int(original['puzzle_id'], 16)), ('addtypes', int(mirrored['puzzle_id'], 16))])
            self.assertEqual([states for _kind, states in rows],
                             [[int(piece['puzzle_id'], 16) + turn * 0x10000 for turn in range(8)] for piece in (original, mirrored)])
            self.assertEqual(len({state for _kind, states in rows for state in states}), 16)
            self.assertEqual(changed[-len(metadata['suffix']):], raw[-len(metadata['suffix']):])
            for prefix in families.PREFIXES:
                original_key = (*prefix, int(original['menu']['id'], 16))
                self.assertEqual(presentations[original_key], menus[original_key])
                self.assertNotIn((*prefix, int(mirrored['menu']['id'], 16)), presentations)
            restored, original_metadata, checked = families.verify(changed, proof, selected, record)
            self.assertEqual((restored, original_metadata), (raw, metadata))
            self.assertEqual(checked['hidden_member_buttons'], 1)
            self.assertFalse(checked['in_game_menu_tested'])
        for selected in ([original], [mirrored]):
            raw, metadata = compose_rul0(fixture.NATIVE, [fixture.fragment(int(selected[0]['puzzle_id'], 16))])
            menus = fixture.menu_fixture.menu_resource(selected[0])
            self.assertEqual(families.apply(raw, metadata, menus, selected, available=catalog['pieces']),
                             (raw, metadata, menus, None))


if __name__ == '__main__':
    unittest.main()
