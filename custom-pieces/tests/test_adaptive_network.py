"""Exercise active network bindings and preserved fixed-model safeguards."""
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import jsonc
from scp.adaptive_network import (RUL1, PROP, T21, S3D, PATH, TEXTURE, NETWORK_EXEMPLAR,
    bindings, allocation_fields, allocation_blocks, reservation_ids, resource_keys, validate_active_resources,
    compose_rul1, verify_rul1, expected_solutions)
from scp.catalog import auto_tile_base, validate_catalog
from scp.autotile import validate_auto_tile_addresses
from scp.dbpf import encode_exemplar, exemplar, pack_dbpf
from scp.verify import check_emitted_runtime_addresses, check_piece_models, strict_dbpf, RUL0, NETWORK_INI


def piece():
    return {'id': 'adaptive-fixture', 'footprint': [2, 1], 'cells': [[0, 0], [1, 0]],
            'tile_ids': ['7f580000', '7f580100'], 'preview_id': '7f580ff5',
            'adaptive_ground': {'schema_version': 1, 'cells': [
                {'cell': [0, 0], 'resolved_tile_id': '7f5a0000', 'rotation': 2,
                 'texture_donor_id': '04000200', 'street_flags': '02020404',
                 'avenue_flags': '01000003', 'prop': True}]}}


def prop(pid, values, kind=0x300, array=False):
    return {'id': pid, 'type': kind, 'key_type': 0x80 if array else 0, 'values': values}


def assets(spec):
    resources = {key: b'fixture' for key in resource_keys(spec)}
    for row in bindings(spec):
        if not row['prop']:
            continue
        tile, resolved = int(row['canonical_tile_id'], 16), int(row['resolved_tile_id'], 16)
        resources[*PROP, tile] = encode_exemplar({'parent': [0, 0, 0], 'properties': [
            prop(0x10, [0x1E]), prop(0x21, [tile]),
            prop(0x27812820, [*S3D, tile + 5], array=True), prop(0xE83A081D, [1], 0xB00)]})
        expected = {0x10: [0x21], 0x21: [resolved], 0xC9A5A1BE: [resolved], 0xEC3BD470: [15],
                    0xCA81B8D4: [4], 0xCC3E4755: [2], 0x88EDC789: [2],
                    0x88EDC793: list(range(16)), 0x88EDC795: [0, 1, 2, 3],
                    0x49D55951: [15, 15, 15, 15],
                    0x88EDC900: [1, 0, (-row['rotation']) % 4, 0x80000, 0, 0x80000,
                                0, 0, 0xFFFFF, 0xFFFFF, 0, resolved, tile]}
        resources[*T21, resolved] = encode_exemplar({'parent': [0, 0, 0],
            'properties': [prop(pid, values, array=len(values) > 1) for pid, values in expected.items()]})
    return resources


def delta(spec):
    return '\r\n'.join([';test delta', *[f'TYPE{i}=0x{a:08x},0x{b:08x},0x{c:08x},{d},{e}'
        for i, ((a, b), (c, d, e)) in enumerate(expected_solutions([spec]).items())], ''])


class AdaptiveNetworkTests(unittest.TestCase):
    def test_legacy_piece_has_no_extra_resources_or_changed_base(self):
        spec = piece(); spec.pop('adaptive_ground')
        self.assertEqual(bindings(spec), [])
        self.assertEqual(resource_keys(spec), set())
        self.assertEqual(auto_tile_base(spec), 0x7f580000)
        self.assertEqual(verify_rul1({}, [spec], {}, {}), {'adaptive_rul1_solutions_checked': 0})

    def test_bindings_derive_allocated_model_and_exemplar_ids(self):
        spec = piece(); row = bindings(spec)[0]
        self.assertEqual(row['canonical_tile_id'], '7f580000')
        self.assertEqual(row['prop_model_id'], '7f580005')
        self.assertEqual(row['prop_id'], '7f580000')
        self.assertEqual(row['t21_id'], '7f5a0000')
        row['cell'][0] = 99
        self.assertEqual(spec['adaptive_ground']['cells'][0]['cell'], [0, 0])

    def test_exact_resource_keys_include_twenty_textures_and_one_path(self):
        keys = resource_keys(piece())
        self.assertEqual(len(keys), 24)
        self.assertEqual(sum(key[:2] == TEXTURE for key in keys), 20)
        self.assertIn((*PATH, 0x7f5a0000), keys)
        self.assertIn((*S3D, 0x7f580005), keys)
        self.assertNotIn((*NETWORK_EXEMPLAR, 0x7f580000), keys)

    def test_pure_ground_cell_has_no_prop_model_or_t21(self):
        spec = piece(); spec['adaptive_ground']['cells'][0]['prop'] = False
        self.assertEqual(len(resource_keys(spec)), 21)
        self.assertEqual(allocation_fields(spec)['extra_model_ids'], [])

    def test_invalid_metadata_is_rejected(self):
        changes = [('rotation', True), ('rotation', 4), ('prop', 1), ('cell', [2, 0]),
                   ('cell', [False, 0]), ('resolved_tile_id', '7f5a0010'),
                   ('street_flags', '0202'), ('unknown', 1)]
        for field, value in changes:
            with self.subTest(field=field, value=value):
                spec = piece(); spec['adaptive_ground']['cells'][0][field] = value
                with self.assertRaises(ValueError):
                    bindings(spec)

    def test_duplicate_cells_or_appearance_families_are_rejected(self):
        for duplicate_cell in (True, False):
            spec = piece(); second = deepcopy(spec['adaptive_ground']['cells'][0])
            if not duplicate_cell:
                second['cell'] = [1, 0]
            spec['adaptive_ground']['cells'].append(second)
            with self.assertRaises(ValueError):
                bindings(spec)

    def test_complete_appearance_family_is_reserved_beyond_twenty_active_ids(self):
        fields = allocation_fields(piece())
        reserved = reservation_ids(fields)
        self.assertEqual(len(reserved), 257)
        self.assertIn(0x7f5a00ff, reserved)
        self.assertIn(0x7f580005, reserved)
        fields['extra_model_ids'].append('7f5a00fe')
        with self.assertRaisesRegex(ValueError, 'overlap'):
            reservation_ids(fields)

    def test_new_allocators_exclude_resolved_appearance_blocks(self):
        record = {'preview_id': '7f580ff5', 'tile_ids': ['7f580000'],
                  'adaptive_tile_ids': ['7f59a100'], 'extra_model_ids': ['7f580005']}
        self.assertEqual(allocation_blocks(record), {0x7f580000, 0x7f59a000})

    def test_catalog_rejects_texture_family_overlapping_canonical_resources(self):
        spec = jsonc.load(ROOT / 'domains/highway/00_pieces/ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg/piece.jsonc')
        row = piece()['adaptive_ground']['cells'][0]
        row['cell'] = spec['cells'][0]
        spec['adaptive_ground'] = {'schema_version': 1, 'cells': [row]}
        catalog = {'schema_version': 1, 'plugin_folder': 'zzz_Simons_Custom_Pieces',
                   'pieces': [spec], '_profile': {'schema_version': 1}}
        validate_catalog(catalog)
        row['resolved_tile_id'] = f'{int(spec["tile_ids"][0], 16) & 0xffffff00:08x}'
        with self.assertRaisesRegex(ValueError, 'overlap'):
            validate_catalog(catalog)

    def test_catalog_requires_permanent_adaptive_allocations(self):
        spec = jsonc.load(ROOT / 'domains/highway/00_pieces/ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg/piece.jsonc')
        row = piece()['adaptive_ground']['cells'][0]; row['cell'] = spec['cells'][0]
        spec['adaptive_ground'] = {'schema_version': 1, 'cells': [row]}
        allocation = {key: spec[key] for key in ('puzzle_id', 'tile_ids', 'preview_id')}
        allocation['menu_id'] = spec['menu']['id']
        catalog = {'schema_version': 1, 'plugin_folder': 'zzz_Simons_Custom_Pieces',
                   'pieces': [spec], '_profile': {'schema_version': 1},
                   '_allocations': {'schema_version': 1, 'pieces': {spec['id']: allocation}}}
        with self.assertRaisesRegex(ValueError, 'permanent resource reservation'):
            validate_catalog(catalog)
        allocation.update(allocation_fields(spec))
        validate_catalog(catalog)

    def test_valid_pose_compensates_the_resolved_tile_rotation(self):
        self.assertTrue(validate_active_resources(assets(piece()), piece())['active_bindings_checked'])

    def test_missing_rotation_property_is_rejected_independently_of_file_hashes(self):
        spec = piece(); resources = assets(spec); key = (*PROP, 0x7f580000)
        record = exemplar(resources[key])
        record['properties'] = [p for p in record['properties'] if int(p['id'], 16) != 0xE83A081D]
        resources[key] = encode_exemplar(record)
        with self.assertRaisesRegex(ValueError, 'rotation encoding'):
            validate_active_resources(resources, spec)

    def test_wrong_active_prop_model_is_rejected(self):
        spec = piece(); resources = assets(spec); key = (*PROP, 0x7f580000)
        record = exemplar(resources[key])
        next(p for p in record['properties'] if int(p['id'], 16) == 0x27812820)['values'][-1] += 1
        resources[key] = encode_exemplar(record)
        with self.assertRaisesRegex(ValueError, 'wrong model'):
            validate_active_resources(resources, spec)

    def test_wrong_t21_pose_or_mirroring_is_rejected(self):
        for pid, replacement in ((0xEC3BD470, [1]), (0xCA81B8D4, [5]), (0xC9A5A1BE, [0x7f5a0100]),
                                  (0x88EDC900, [1, 0, 0, 0x80000, 0, 0x80000, 0, 0, 0xFFFFF, 0xFFFFF, 0, 0x7f5a0000, 0x7f580000])):
            with self.subTest(property=hex(pid)):
                spec = piece(); resources = assets(spec); key = (*T21, 0x7f5a0000)
                record = exemplar(resources[key])
                next(p for p in record['properties'] if int(p['id'], 16) == pid)['values'] = replacement
                resources[key] = encode_exemplar(record)
                with self.assertRaises(ValueError):
                    validate_active_resources(resources, spec)

    def test_fixed_network_exemplar_on_adaptive_cell_is_rejected(self):
        for tile in (0x7f580000, 0x7f5a0000):
            spec = piece(); resources = assets(spec)
            resources[*NETWORK_EXEMPLAR, tile] = b'fixed model'
            with self.assertRaisesRegex(ValueError, 'fixed network'):
                validate_active_resources(resources, spec)

    def test_each_missing_appearance_variant_is_rejected(self):
        for appearance in (0, 0x10, 0x20, 0x30):
            resources = assets(piece()); del resources[*TEXTURE, 0x7f5a0000 + appearance + 4]
            with self.assertRaisesRegex(ValueError, 'missing'):
                validate_active_resources(resources, piece())

    def test_hybrid_auto_tile_base_uses_actual_fixed_cell_origin(self):
        spec = piece()
        self.assertEqual(auto_tile_base(spec), 0x7f580100)
        report = validate_auto_tile_addresses(spec)
        self.assertEqual(report['fixed_model_cells']['base'], '7f580100')
        fields = {'CellLayout': ['ab<', '^..'], 'CheckType': [
            'a - street: 0x02020404 avenue: 0x01000003, 0xFFFFFFFF optional',
            'b - dirtroad: 0x03010000'], 'AutoTileBase': ['0x7f580100']}
        self.assertEqual(check_emitted_runtime_addresses(fields, spec)['wrong_model_selections'], 0)
        fields['AutoTileBase'] = ['0x7f580000']
        with self.assertRaisesRegex(ValueError, 'wrong cell models'):
            check_emitted_runtime_addresses(fields, spec)

    def test_unmodeled_cell_requires_explicit_adaptive_binding(self):
        spec = piece(); spec.pop('adaptive_ground')
        fields = {'CellLayout': ['ab<', '^..'], 'CheckType': [
            'a - avenue: 0x01000003 optional', 'b - dirtroad: 0x03010000'],
            'AutoTileBase': ['0x7f580100']}
        with self.assertRaisesRegex(ValueError, 'modeled cells'):
            check_emitted_runtime_addresses(fields, spec)

    def test_pure_adaptive_construction_requires_the_native_removable_handle(self):
        spec = piece(); spec['cells'] = [[0, 0]]; spec['tile_ids'] = spec['tile_ids'][:1]
        fields = {'CellLayout': ['a..Z<', '^....'], 'CheckType': [
            'a - street: 0x02020404 avenue: 0x01000003, 0xFFFFFFFF optional',
            'Z - road: 0x02000200'], 'AutoTileBase': ['0x55387000']}
        self.assertEqual(auto_tile_base(spec), 0x55387000)
        self.assertEqual(check_emitted_runtime_addresses(fields, spec)['wrong_model_selections'], 0)
        fields['CheckType'][-1] = 'Z - road: 0x02000202'
        with self.assertRaisesRegex(ValueError, 'removable Road handle'):
            check_emitted_runtime_addresses(fields, spec)

    def test_rul1_composition_restores_exact_native_bytes(self):
        native = b';native\r\n[StreetAvenueIntersectionSolutions]\r\n;keep\r\n[Other]\r\nkeep=yes\r\n'
        raw, record = compose_rul1(native, [delta(piece())], [piece()])
        report = verify_rul1({RUL1: raw}, [piece()], {'rul1': record}, {RUL1: native})
        self.assertEqual(report['adaptive_rul1_solutions_checked'], 4)
        self.assertTrue(report['native_rul1_bytes_preserved'])

    def test_rul1_tamper_outside_insertion_is_rejected(self):
        native = b'[StreetAvenueIntersectionSolutions]\r\n[Other]\r\nkeep=yes\r\n'
        raw, record = compose_rul1(native, [delta(piece())], [piece()])
        with self.assertRaisesRegex(ValueError, 'Native RUL1 bytes'):
            verify_rul1({RUL1: raw.replace(b'keep=yes', b'keep=bad')}, [piece()], {'rul1': record}, {})

    def test_rul1_wrong_pose_is_rejected_even_with_updated_insertion(self):
        native = b'[StreetAvenueIntersectionSolutions]\r\n'
        raw, record = compose_rul1(native, [delta(piece())], [piece()])
        bad = record['insertion'].replace(',2,0', ',1,0', 1)
        raw = raw.replace(record['insertion'].encode(), bad.encode())
        record['insertion'] = bad
        with self.assertRaisesRegex(ValueError, 'cell poses'):
            verify_rul1({RUL1: raw}, [piece()], {'rul1': record}, {})

    def test_rul1_native_marker_collision_is_rejected(self):
        first = delta(piece()).splitlines()[1]
        native = ('[StreetAvenueIntersectionSolutions]\r\n' + first + '\r\n').encode()
        with self.assertRaisesRegex(ValueError, 'native RUL1'):
            compose_rul1(native, [delta(piece())], [piece()])

    def test_rul1_overlay_cannot_be_added_to_legacy_piece(self):
        spec = piece(); spec.pop('adaptive_ground')
        with self.assertRaisesRegex(ValueError, 'Fixed-model'):
            verify_rul1({RUL1: b'anything'}, [spec], {'rul1': {}}, {})

    def test_install_scanner_rejects_a_foreign_rul1_even_with_clean_rul0(self):
        from scp.install import _foreign_overlays
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve(); native = root / 'native.dat'
            locations = {RUL0: [native], NETWORK_INI: [native], RUL1: [root / 'foreign.dat']}
            with patch('scp.dbpf.index_plugins', return_value=locations):
                with self.assertRaisesRegex(ValueError, 'Foreign shared'):
                    _foreign_overlays(root, root / 'managed', native)
            del locations[RUL1]
            with patch('scp.dbpf.index_plugins', return_value=locations):
                _foreign_overlays(root, root / 'managed', native)

    def test_assembly_menu_transformation_keeps_adaptive_rul1_exact(self):
        from scp.menu_experiment import _transformed, _check_actual_resources
        member = {'id': 'member', 'menu': {'id': '6a47f7c0'}, 'puzzle_id': 'f7c0'}
        base = {'pieces': [member], 'overlay': {'rul0': {'fixture': 'composition'}, 'rul1': {'fixture': 'composition'}}}
        scene = {'placements': [{'piece_id': 'member'}]}
        layout = {'cycle_button': {'id': '6a47f7c1'}}
        controller = pack_dbpf({RUL0: b'original RUL0', NETWORK_INI: b'original INI', RUL1: b'original RUL1'})
        menu = pack_dbpf({(1, 2, 3): b'fixture menu'})
        with patch('scp.menu_experiment_resources.build_menu_experiment_resources',
                   return_value=({(1, 2, 3): b'changed menu'}, {})):
            changed, _, _, _, _ = _transformed(base, controller, menu, layout, scene)
        self.assertEqual(strict_dbpf(changed)[RUL1], b'original RUL1')
        bad = strict_dbpf(changed); bad[RUL1] = b'changed RUL1'
        with self.assertRaisesRegex(ValueError, 'changed adaptive RUL1'):
            _check_actual_resources(controller, menu, pack_dbpf(bad), menu, base, layout, [member])

    def test_visual_observation_dependencies_include_prop_and_t21_exemplars(self):
        from scp.content import new_manual_record, resource_fingerprints
        keys = {(*PROP, 0x7f580000): b'prop', (*T21, 0x7f5a0000): b't21',
                (*S3D, 0x7f580005): b'model'}
        fingerprints = resource_fingerprints('adaptive-fixture', keys)
        connections = {'subject_id': 'adaptive-fixture', 'ports': [], 'journeys': [], 'forbidden_transfers': []}
        record = new_manual_record('adaptive-fixture', 'piece', connections, fingerprints)
        visual = [case for case in record['cases'] if case['kind'] == 'in_game_render']
        self.assertTrue(visual)
        for case in visual:
            self.assertEqual(case['dependencies'], fingerprints)

    def test_adaptive_metadata_requires_an_independent_domain_proof(self):
        for proof in ({}, {'adaptive_ground': {}}, {'adaptive_ground': {'active_layer_verified': 1}}):
            with self.subTest(proof=proof):
                with patch('scp.verify.check_piece_render_budget', return_value={}), \
                     patch('scp.verify._check_piece_geometry', return_value=proof):
                    with self.assertRaisesRegex(ValueError, 'independent domain proof'):
                        check_piece_models(assets(piece()), piece(), None)
        proof = {'adaptive_ground': {'active_layer_verified': True}}
        with patch('scp.verify.check_piece_render_budget', return_value={}), \
             patch('scp.verify._check_piece_geometry', return_value=proof):
            self.assertTrue(check_piece_models(assets(piece()), piece(), None)
                            ['adaptive_ground']['active_layer_verified'])


if __name__ == '__main__':
    unittest.main()
