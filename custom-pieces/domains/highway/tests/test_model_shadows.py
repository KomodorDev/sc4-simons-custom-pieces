"""Saved highway shadow geometry must agree with its actual masks and cards."""
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import model_shadows
from scp.model_shadow_geometry import encode_mask_fsh, generate_shadow_carriers
from scp.models import pack_s3d, parse_s3d
from scp.preview import decode_fsh
from scp.test_support import plane
from scp_highway.model_shadows import add_shadows, elevated_triangles
from scp_highway import shadow_verify
from scp_highway.shadow_verify import check_resources

S3D = model_shadows.S3D
TEXTURE = model_shadows.TEXTURE


def specification(cast=True):
    row = {'cell': [0, 0], 'cast_shadow': cast}
    if cast:
        row['resource_base'] = '7f500800'
    return {'id': 'shadow-test', 'name': 'Shadow test', 'footprint': [1, 1],
            'cells': [[0, 0]], 'tile_ids': ['7f500000'], 'shadow_mode': 'model-carrier',
            'shadow_mappings': [], 'model_shadows': {'schema_version': 1,
                'sun_profile': model_shadows.SUN_PROFILE, 'cells': [row]}}


def source_model(triangles, unused=False):
    model = plane()
    points = [point for triangle in triangles for point in triangle]
    model['vertices'][0]['format'] = 0x80004001
    model['vertices'][0]['data'] = b''.join(struct.pack('<5f', *point, 0., 0.) for point in points)
    if unused:
        model['vertices'][0]['data'] += struct.pack('<5f', 999., 999., 999., 0., 0.)
    model['indices'][0]['values'] = tuple(range(len(points)))
    model['primitives'] = [[(0, 0, len(points))]]
    material = bytearray(model['materials'][0]['raw'])
    struct.pack_into('<I', material, 0, 0x2A)
    model['materials'][0]['raw'] = bytes(material)
    return pack_s3d(model)


class HighwaySavedShadowTests(unittest.TestCase):
    def test_explicit_disable_keeps_elevated_models_and_paths_without_a_lighting_input(self):
        spec = specification()
        allocated = model_shadows.allocation_fields(spec)
        spec['model_shadows']['enabled'] = False
        elevated = source_model([((-8., 15., -8.), (8., 15., -8.), (8., 15., 8.))])
        original = {(*S3D, 0x7F500000): elevated,
                    (0x296678F7, 0xA966883F, 0x7F500000): b'protected traffic'}
        with patch('scp_highway.model_shadows.generate_shadow_carriers',
                   side_effect=AssertionError('Disabled shadows must not be generated')):
            actual = add_shadows(spec, {}, [((0, 0), elevated, b'protected traffic')], dict(original))
        self.assertEqual(actual, original)
        self.assertEqual(model_shadows.allocation_fields(spec), allocated)
        report = check_resources(actual, spec)['model_shadow_geometry']
        self.assertTrue(report['shadow_generation_disabled'])
        self.assertEqual(report['retained_shadow_resources'], 0)

    def setUp(self):
        self.piece = specification()
        self.row = model_shadows.bindings(self.piece)[0]
        self.faces = [
            ((-18., 15., -4.), (20., 15., -4.), (20., 15., 4.)),
            ((-18., 15., -4.), (20., 15., 4.), (-18., 15., 4.)),
            ((-12., 7.5, 9.), (14., 7.5, 9.), (14., 7.5, 13.)),
            ((23., 0., -3.), (23., 9., -3.), (23., 9., 4.)),
            ((23., 0., -3.), (23., 9., 4.), (23., 0., 4.)),
            ((-10., -4., -15.), (1., 6., -9.), (7., 6., -15.)),
            ((-24., 0., -21.), (-10., 0., -21.), (-10., 0., -17.)),
            ((-20., -8., -24.), (-8., -8., -24.), (-8., -8., -18.)),
        ]
        self.raw = source_model(self.faces, unused=True)
        self.resources = self.build(self.raw)

    def build(self, raw, triangles=None):
        resources = {(*S3D, 0x7F500000 + zoom): raw for zoom in range(5)}
        carrier = generate_shadow_carriers(elevated_triangles(raw) if triangles is None else triangles,
                                           self.row['texture_ids'], card_height_m=64.)
        return model_shadows.add_resources(resources, self.piece, {(0, 0): carrier})

    def report(self, resources=None, piece=None):
        return check_resources(self.resources if resources is None else resources,
                               self.piece if piece is None else piece)['model_shadow_geometry']

    def mutate_mask(self, pose, function):
        result = dict(self.resources)
        key = (*TEXTURE, self.row['texture_ids'][pose])
        mask = decode_fsh(result[key]).getchannel('A')
        function(mask)
        result[key] = encode_mask_fsh(mask)
        return result

    def test_actual_masks_cover_both_decks_vertical_faces_ground_clips_and_overhang(self):
        report = self.report()
        self.assertFalse(report['in_game_tested'])
        self.assertFalse(report['tile_clipping'])
        self.assertEqual(report['hosts_checked'], 1)
        host = report['hosts'][0]
        self.assertEqual(host['referenced_faces'], 8)
        self.assertEqual(host['ground_or_below_faces_excluded'], 2)
        self.assertEqual(host['ground_crossing_faces_clipped'], 1)
        self.assertEqual(host['vertical_faces_retained'], 2)
        self.assertEqual(host['proper_object_camera_poses_checked'], 16)
        self.assertLessEqual(host['maximum_native_pose_error_m'], 1e-9)
        self.assertEqual(len(host['variants']), 4)
        self.assertTrue(all(variant['ground_shadow_area_m2'] > 0 for variant in host['variants']))

    def test_wrong_saved_relative_pose_mask_fails(self):
        resources = dict(self.resources)
        first, second = [(*TEXTURE, iid) for iid in self.row['texture_ids'][:2]]
        resources[first], resources[second] = resources[second], resources[first]
        with self.assertRaisesRegex(ValueError, 'mask (omits|contains)'):
            self.report(resources)

    def test_missing_saved_mask_resource_fails_explicitly(self):
        resources = dict(self.resources)
        del resources[*TEXTURE, self.row['texture_ids'][2]]
        with self.assertRaisesRegex(ValueError, 'missing a card model or alpha mask'):
            self.report(resources)

    def test_missing_mask_area_fails_even_when_remaining_alpha_is_nonempty(self):
        def erase(mask):
            mask.paste(0, (mask.width // 2, 0, mask.width, mask.height))
        with self.assertRaisesRegex(ValueError, 'mask omits'):
            self.report(self.mutate_mask(0, erase))

    def test_phantom_neighbouring_geometry_in_saved_mask_fails(self):
        def add(mask):
            mask.paste(255, (4, 4, 14, 14))
        with self.assertRaisesRegex(ValueError, 'mask contains phantom'):
            self.report(self.mutate_mask(0, add))

    def test_translated_saved_card_fails_without_changing_any_mask(self):
        resources = dict(self.resources)
        key = (*S3D, self.row['model_ids'][0])
        model = parse_s3d(resources[key])
        block = model['vertices'][0]
        vertices = [struct.unpack_from('<5f', block['data'], at) for at in range(0, len(block['data']), 20)]
        block['data'] = b''.join(struct.pack('<5f', x + 2, y, z, u, v) for x, y, z, u, v in vertices)
        resources[key] = pack_s3d(model)
        with self.assertRaisesRegex(ValueError, 'card is translated'):
            self.report(resources)

    def test_changed_canonical_deck_height_makes_old_shadow_fail(self):
        raw = source_model([tuple((x, y + 4 if y > 0 else y, z) for x, y, z in face)
                            for face in self.faces])
        resources = dict(self.resources)
        resources.update({(*S3D, 0x7F500000 + zoom): raw for zoom in range(5)})
        with self.assertRaisesRegex(ValueError, 'wrong source geometry|mask '):
            self.report(resources)

    def test_unclipped_ground_and_below_ground_source_is_rejected(self):
        resources = self.build(self.raw, self.faces)
        with self.assertRaisesRegex(ValueError, 'wrong source geometry|mask '):
            self.report(resources)

    def test_canonical_zoom_geometry_cannot_silently_change(self):
        resources = dict(self.resources)
        resources[*S3D, 0x7F500004] = source_model(self.faces[:2])
        with self.assertRaisesRegex(ValueError, 'zoom geometry differs'):
            self.report(resources)

    def test_false_cast_declaration_is_checked_against_real_referenced_geometry(self):
        with self.assertRaisesRegex(ValueError, 'hides above-ground'):
            self.report(piece=specification(False))
        raw = source_model([self.faces[-2], self.faces[-1]])
        resources = {(*S3D, 0x7F500000 + zoom): raw for zoom in range(5)}
        report = self.report(resources, specification(False))
        self.assertEqual(report['hosts_checked'], 0)
        self.assertEqual(report['ground_only_hosts_checked'], 1)

    def test_source_alpha_test_and_blending_require_a_different_shadow_contract(self):
        for flag in (0x01, 0x10):
            with self.subTest(flag=flag):
                model = parse_s3d(self.raw)
                material = bytearray(model['materials'][0]['raw'])
                struct.pack_into('<I', material, 0, 0x2A | flag)
                model['materials'][0]['raw'] = bytes(material)
                raw = pack_s3d(model)
                resources = dict(self.resources)
                resources.update({(*S3D, 0x7F500000 + zoom): raw for zoom in range(5)})
                with self.assertRaisesRegex(ValueError, 'alpha-test or blending'):
                    self.report(resources)

    def test_cached_verification_rechecks_changed_saved_bytes(self):
        first = self.report()
        self.assertEqual(first, self.report())
        resources = self.mutate_mask(0, lambda mask: mask.paste(0, (0, 0, mask.width, mask.height)))
        with self.assertRaisesRegex(ValueError, 'mask is empty'):
            self.report(resources)

    def test_warmed_result_cannot_bypass_a_changed_live_pose_validator(self):
        self.report()
        with patch.object(shadow_verify, '_world_projection_check',
                          side_effect=ValueError('changed live pose check')):
            with self.assertRaisesRegex(ValueError, 'changed live pose check'):
                self.report()

    def test_warmed_source_cannot_bypass_changed_ground_clipping(self):
        self.report()
        with patch.object(shadow_verify, '_clip_face',
                          side_effect=ValueError('changed live ground clip')):
            with self.assertRaisesRegex(ValueError, 'changed live ground clip'):
                self.report()

    def test_warmed_result_cannot_bypass_changed_sun_constants(self):
        self.report()
        with patch.object(shadow_verify, 'SUN', (0.5, -0.7, -0.3)):
            with self.assertRaisesRegex(ValueError, 'Native RKT2 selection'):
                self.report()

    def test_subpixel_and_edge_on_faces_are_not_discarded_as_a_blanket_error(self):
        thin = ((-23., 5., 20.), (12., 5., 20.), (12., 5., 20.002))
        raw = source_model(self.faces + [thin])
        self.assertEqual(self.report(self.build(raw))['hosts_checked'], 1)


if __name__ == '__main__':
    unittest.main()
