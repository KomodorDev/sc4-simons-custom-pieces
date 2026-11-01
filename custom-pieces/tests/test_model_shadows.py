"""Reject native carrier binding errors independently of geometry authoring."""
from copy import deepcopy
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

from PIL import Image

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import model_shadows as shadows
from scp.adaptive_network import validate_active_resources
from scp.build import preflight_allocations, RUL0
from scp.dbpf import encode_exemplar, exemplar, pack_dbpf
from scp.models import pack_s3d, parse_s3d
from scp.shadows import encode_shadow_fsh
from scp.test_support import plane
from scp.verify import strict_dbpf


def piece(adaptive=False, ground=False):
    result = {'id': 'shadow-fixture', 'name': 'Shadow fixture', 'footprint': [1, 1],
              'cells': [[0, 0]], 'tile_ids': ['7f580000'], 'preview_id': '7f580ff5',
              'puzzle_id': 'f809', 'effect_name': 'shadow_fixture', 'menu': {'id': '6a47f809'},
              'recipe': 'highway_fixture',
              'dependencies': ['controller', 'model_shadow_lighting'],
              'shadow_mode': 'model-carrier', 'shadow_mappings': [],
              'model_shadows': {'schema_version': 1, 'sun_profile': 'sc4-default-67p5-45',
                                'cells': [{'cell': [0, 0], 'cast_shadow': not ground}]}}
    if not ground:
        result['model_shadows']['cells'][0]['resource_base'] = '7f580800'
    if adaptive:
        result['adaptive_ground'] = {'schema_version': 1, 'cells': [
            {'cell': [0, 0], 'resolved_tile_id': '7f590000', 'rotation': 2,
             'texture_donor_id': '04000200', 'street_flags': '02020404',
             'avenue_flags': '01000003', 'prop': True}]}
    return result


def compiled(spec):
    rows = [row for row in shadows.bindings(spec) if row['cast_shadow']]
    result = {}
    for row in rows:
        models = []
        for iid in row['texture_ids']:
            model = plane(-20., 20., -12., 12., height=8.)
            model['vertices'][0]['format'] = 0x80004001
            sx, sz = (-0.27059805393218994 / -0.7071067690849304,
                      -0.6532814502716064 / -0.7071067690849304)
            vertices = [(-20., 0., -12., 0., 0.), (20. + 64. * sx, 64., -12. + 64. * sz, 1., 0.),
                        (20. + 64. * sx, 64., 12. + 64. * sz, 1., 1.), (-20., 0., 12., 0., 1.)]
            model['vertices'][0]['data'] = b''.join(struct.pack('<5f', *point) for point in vertices)
            model['primitives'] = [[]]
            material = (struct.pack('<IBBBBHIBB', 0, 0, 0, 0, 0, 0, 0, 0, 1)
                        + struct.pack('<IBBBBHHB', iid, 0, 0, 0, 0, 0, 0, 1) + b'\0')
            model['materials'] = [{'raw': material, 'textures': [iid]}]
            models.append(pack_s3d(model))
        result[tuple(row['cell'])] = {'models': tuple(models), 'textures': {
            iid: encode_shadow_fsh(Image.new('L', (8, 8), 255)) for iid in row['texture_ids']}}
    return result


def resources(spec):
    result = {(0x296678F7, 0xA966883F, 0x7F580000): b'protected canonical traffic'}
    shadows.add_resources(result, spec, compiled(spec))
    return strict_dbpf(pack_dbpf(result))


def change_property(resources, key, pid, value=None, *, remove=False, kind=None):
    record = exemplar(resources[key])
    if remove:
        record['properties'] = [prop for prop in record['properties'] if int(prop['id'], 16) != pid]
    else:
        found = next((prop for prop in record['properties'] if int(prop['id'], 16) == pid), None)
        if found is None:
            found = {'id': f'0x{pid:08x}', 'type': '0x0b00', 'key_type': '0x0000', 'values': value}
            record['properties'].append(found)
        found['values'] = value
        if kind:
            found['type'] = kind
    resources[key] = encode_exemplar(record)


class ModelShadowResourceTests(unittest.TestCase):
    def test_existing_modes_do_not_create_resources_or_require_a_light_capture(self):
        spec = piece(); spec.pop('model_shadows'); spec['shadow_mode'] = 'generated'
        original = {(1, 2, 3): b'legacy bytes'}
        result = shadows.add_resources(dict(original), spec, {})
        self.assertEqual(result, original)
        self.assertEqual(shadows.resource_keys(spec), set())
        self.assertEqual(shadows.allocation_fields(spec), {'shadow_resource_families': []})
        self.assertEqual(shadows.audit_lighting_dependency({}, {}, [spec]), {'model_shadow_lighting_required': False})

    def test_actual_dat_closure_keeps_traffic_and_creates_no_clipped_shadow_resources(self):
        spec = piece(); actual = resources(spec)
        protected = (0x296678F7, 0xA966883F, 0x7F580000)
        self.assertEqual(actual[protected], b'protected canonical traffic')
        self.assertEqual(set(actual) - {protected}, shadows.resource_keys(spec))
        self.assertEqual(len(actual) - 1, 10)
        self.assertFalse(any(key[:2] == shadows.SHADOW for key in actual))
        report = shadows.validate_resources(actual, spec)
        self.assertEqual(report['carrier_hosts_checked'], 1)
        self.assertFalse(report['game_shadow_selection_tested'])

    def test_ground_only_hosts_have_no_phantom_carrier_or_network_shadow(self):
        spec = piece(ground=True)
        self.assertEqual(shadows.resource_keys(spec), set())
        self.assertEqual(shadows.reservation_ids(shadows.allocation_fields(spec)), [])
        actual = resources(spec)
        self.assertEqual(len(actual), 1)
        self.assertEqual(shadows.validate_resources(actual, spec)['ground_only_hosts_without_carriers'], 1)

    def test_false_cast_setting_cannot_hide_allocated_resource_fields(self):
        spec = piece(); spec['model_shadows']['cells'][0]['cast_shadow'] = False
        with self.assertRaisesRegex(ValueError, 'ownership order'):
            shadows.bindings(spec)

    def test_all_owned_cells_and_strict_boolean_settings_are_required(self):
        for value in (0, 1, None, 'true'):
            spec = piece(); spec['model_shadows']['cells'][0]['cast_shadow'] = value
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'must be a boolean'):
                shadows.bindings(spec)
        spec = piece(); spec['model_shadows']['cells'] = []
        with self.assertRaisesRegex(ValueError, 'every owned cell'):
            shadows.bindings(spec)

    def test_carriers_cannot_point_into_another_piece_or_reuse_canonical_models(self):
        for value in ('7f590800', '7f580000', '7f580810', '7f580900'):
            spec = piece(); spec['model_shadows']['cells'][0]['resource_base'] = value
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'reserved canonical-block'):
                shadows.bindings(spec)

    def test_whole_families_are_reserved_and_duplicate_reservations_rejected(self):
        fields = shadows.allocation_fields(piece())
        reserved = shadows.reservation_ids(fields)
        self.assertEqual(len(reserved), 256)
        self.assertIn(0x7F5808FF, reserved)
        fields['shadow_resource_families'] *= 2
        with self.assertRaisesRegex(ValueError, 'overlap'):
            shadows.reservation_ids(fields)

    def test_incoming_carrier_cannot_overwrite_existing_artwork_or_traffic(self):
        spec = piece(); original = {(*shadows.S3D, 0x7F580800): b'existing model'}
        with self.assertRaisesRegex(ValueError, 'overlap retained'):
            shadows.add_resources(original, spec, compiled(spec))
        self.assertEqual(original, {(*shadows.S3D, 0x7F580800): b'existing model'})

    def test_each_relative_model_reference_and_shadow_gate_is_verified(self):
        for pid, value, kind in ((0x27812822, [*shadows.S3D, *([0x7F580801] * 20)], None),
                                 (0x8A5E5DB8, [0], None), (0x029244DB, [1], None),
                                 (0x029244DB, [0], '0x0300'), (0x29F013E6, [0], None),
                                 (0x29F013E6, [1], '0x0300'), (0x69F14D33, [1], None)):
            with self.subTest(property=hex(pid), value=value):
                spec = piece(); actual = resources(spec)
                change_property(actual, (*shadows.PROP, 0x7F580804), pid, value, kind=kind)
                with self.assertRaisesRegex(ValueError, 'native model, shadow, or collision'):
                    shadows.validate_resources(actual, spec)

    def test_carrier_cannot_become_a_terrain_immovability_obstacle_when_marker_is_missing(self):
        spec = piece(); actual = resources(spec)
        change_property(actual, (*shadows.PROP, 0x7F580804), 0x29F013E6, remove=True)
        with self.assertRaisesRegex(ValueError, 'native model, shadow, or collision'):
            shadows.validate_resources(actual, spec)

    def test_full_geometry_rotation_or_competing_model_keys_are_rejected(self):
        for pid in (0xE83A081D, 0x27812820, 0x27812821, 0x27812823, 0x27812825):
            spec = piece(); actual = resources(spec)
            change_property(actual, (*shadows.PROP, 0x7F580804), pid, [1])
            with self.subTest(property=hex(pid)), self.assertRaisesRegex(ValueError, 'competing model key'):
                shadows.validate_resources(actual, spec)

    def test_old_fsh_shadow_is_rejected_even_with_valid_new_carrier(self):
        spec = piece(); actual = resources(spec)
        actual[*shadows.SHADOW, 0x7F580004] = b'old shadow'
        with self.assertRaisesRegex(ValueError, 'clipped network shadow'):
            shadows.validate_resources(actual, spec)

    def test_missing_resources_and_empty_alpha_are_rejected(self):
        spec = piece(); original = resources(spec)
        for key in shadows.resource_keys(spec):
            actual = dict(original); del actual[key]
            with self.subTest(resource=key), self.assertRaisesRegex(ValueError, 'missing model, texture'):
                shadows.validate_resources(actual, spec)
        original[*shadows.TEXTURE, 0x7F580810] = encode_shadow_fsh(Image.new('L', (8, 8), 0))
        with self.assertRaisesRegex(ValueError, 'nonempty bounded alpha'):
            shadows.validate_resources(original, spec)

    def test_visible_triangles_legacy_vertex_format_and_height_culling_regressions_are_rejected(self):
        for failure in ('visible-triangles', 'legacy-format', 'short-card'):
            spec = piece(); actual = resources(spec); key = (*shadows.S3D, 0x7F580800)
            model = parse_s3d(actual[key])
            if failure == 'visible-triangles':
                model['primitives'] = [[(0, 0, 6)]]
            elif failure == 'legacy-format':
                model['vertices'][0]['format'] = 2
            else:
                data = bytearray(model['vertices'][0]['data'])
                struct.pack_into('<f', data, 24, 8.)
                model['vertices'][0]['data'] = bytes(data)
            actual[key] = pack_s3d(model)
            with self.subTest(failure=failure), self.assertRaises(ValueError):
                shadows.validate_resources(actual, spec)

    def test_occupant_size_cannot_clip_a_shadow_outside_the_owned_tile(self):
        spec = piece(); actual = resources(spec)
        change_property(actual, (*shadows.PROP, 0x7F580804), 0x27812810, [16., 64., 16.])
        with self.assertRaisesRegex(ValueError, 'occupied dimensions clip'):
            shadows.validate_resources(actual, spec)

    def test_nonempty_or_unknown_model_transforms_are_rejected(self):
        for tag, payload in ((b'PROP', 1), (b'REGP', 1), (b'UNKN', 0)):
            spec = piece(); actual = resources(spec); key = (*shadows.S3D, 0x7F580800)
            model = parse_s3d(actual[key])
            model['trailing'] = [(tag, tag + struct.pack('<II', 12, payload))]
            actual[key] = pack_s3d(model)
            with self.subTest(tag=tag, payload=payload), self.assertRaisesRegex(ValueError, 'unknown model transforms'):
                shadows.validate_resources(actual, spec)

    def test_t21_pose_and_reference_follow_the_actual_selected_host(self):
        spec = piece(); actual = resources(spec)
        key = (*shadows.T21, 0x7F580000)
        record = exemplar(actual[key]); props = {int(p['id'], 16): p['values'] for p in record['properties']}
        self.assertEqual(props[0xC9A5A1BE], [0x7F580000])
        self.assertEqual(props[0x88EDC900][2], 0)
        self.assertEqual(props[0x88EDC900][-1], 0x7F580804)
        lot = list(props[0x88EDC900]); lot[2] = 1
        change_property(actual, key, 0x88EDC900, lot)
        with self.assertRaisesRegex(ValueError, 'T21 host, pose'):
            shadows.validate_resources(actual, spec)

    def test_adaptive_overlay_is_retained_and_its_carrier_cancels_the_host_pose(self):
        # Reuse an independently authored active-layer fixture, rather than
        # asking the new writer to invent the retained overlay being checked.
        from test_adaptive_network import assets as adaptive_assets
        spec = piece(adaptive=True)
        actual = adaptive_assets(spec)
        before = dict(actual)
        t21key = (*shadows.T21, 0x7F590000)
        old_record = exemplar(before[t21key])
        shadows.add_resources(actual, spec, compiled(spec))
        validate_active_resources(actual, spec)
        self.assertEqual({key: actual[key] for key in before if key != t21key},
                         {key: raw for key, raw in before.items() if key != t21key})
        props = exemplar(actual[t21key])['properties']
        self.assertEqual([p for p in props if int(p['id'], 16) != 0x88EDC901], old_record['properties'])
        lot = next(p['values'] for p in props if int(p['id'], 16) == 0x88EDC901)
        self.assertEqual(lot[2], 2)
        self.assertEqual(lot[-2:], [0x7F590000, 0x7F580804])

    def test_preflight_rejects_collision_with_a_new_alpha_texture(self):
        spec = piece(); key = (*shadows.TEXTURE, 0x7F580813)
        with self.assertRaisesRegex(ValueError, 'collide with installed'):
            preflight_allocations({'controller': {RUL0: b''}}, {key: ['foreign.dat']}, [spec])

    def test_wrong_or_unstated_sun_profile_is_rejected(self):
        for value in (None, 'custom-night-lighting'):
            spec = piece(); spec['model_shadows']['sun_profile'] = value
            with self.subTest(profile=value), self.assertRaisesRegex(ValueError, 'sunlight profile'):
                shadows.bindings(spec)

    def test_light_dependency_requires_the_exact_capture_and_rejects_overrides(self):
        spec = piece(); key = shadows.LIGHTING_EXEMPLAR
        with self.assertRaisesRegex(ValueError, 'lighting capture'):
            shadows.audit_lighting_dependency({}, {key: ['capture.dat']}, [spec])
        digest = type('Digest', (), {'hexdigest': lambda self: shadows.LIGHTING_SHA256})()
        with patch.object(shadows.hashlib, 'sha256', return_value=digest):
            context = {'model_shadow_lighting': {key: b'controlled fixture'}}
            for paths in ([], ['capture.dat', 'lighting-override.dat']):
                with self.subTest(paths=paths), self.assertRaisesRegex(ValueError, 'competing installed'):
                    shadows.audit_lighting_dependency(context, {key: paths}, [spec])
            report = shadows.audit_lighting_dependency(context, {key: ['capture.dat']}, [spec])
            self.assertEqual(report['sun_profile'], 'sc4-default-67p5-45')


if __name__ == '__main__':
    unittest.main()
