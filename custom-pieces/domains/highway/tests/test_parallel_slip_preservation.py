"""Exercise bounded preservation controls without proprietary model payloads."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location('_parallel_slip_preservation_tool',
    ROOT / 'domains/highway/tools/verify_parallel_slip_preservation.py')
audit = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(audit)


def face(points=None, *, texture=0x5712000E, name='SCP NAM ramp'):
    return {'points': tuple(points or ((0., 0., 7.5), (4., 0., 7.5), (0., 4., 7.5))),
            'texture': texture, 'mesh_name': name, 'material_sha256': 'pinned-material',
            'material': {'raw': b'fixture'}, 'upward': True,
            'uv': ((0., 0.), (1., 0.), (0., 1.))}


class ParallelSlipPreservationTests(unittest.TestCase):
    def test_unmasked_uvs_follow_the_actual_baseline_frame_and_reject_a_changed_sample(self):
        old = face(texture=audit.DD)
        old['uv'] = ((.4, 1.1), (.6, 1.1), (.4, 1.3))
        reference = audit._FaceIndex([old], size=.25)
        self.assertTrue(audit._native_vertex((1., 1., 7.5), (.45, 1.15),
                                             old['material_sha256'], reference))
        self.assertFalse(audit._native_vertex((1., 1., 7.5), (.46, 1.15),
                                              old['material_sha256'], reference))

    def test_actual_positive_encoded_sliver_keeps_its_exact_winding_sign(self):
        # Actual final slip build 1f8194b1..., cell [3,-3]. The decoder's
        # indexing flag is false below its area threshold; the sign is real.
        actual = face(((51.912251472473145, 55.22596073150635, 7.5),
                       (52.05601119995117, 55.36972093582153, 7.5),
                       (51.91225051879883, 55.22595977783203, 7.5)), texture=audit.DD)
        actual['upward'] = False
        self.assertEqual(audit._area(actual), 2.2737367544323206e-13)
        self.assertEqual(audit._kind(actual), 'deck')
        actual['points'] = tuple(reversed(actual['points']))
        with self.assertRaisesRegex(ValueError, 'reverses'):
            audit._kind(actual)

    def test_authored_uv_phase_may_change_while_every_physical_attribute_is_exact(self):
        before = face()
        after = deepcopy(before)
        after['uv'] = tuple((u, v + .375) for u, v in before['uv'])
        result = audit.compare_bodies([before], [after])
        self.assertEqual(result['exact_geometry_material_winding_triangles'], 1)
        self.assertEqual(result['authored_route_field_uv_triangles'], 1)
        self.assertEqual(result['exact_retained_native_uv_triangles'], 0)

    def test_missing_moved_reversed_or_rematerialized_body_face_is_rejected(self):
        before = face(texture=0x5EB4BEE9, name='SCP NAM barrier')
        for mutation in ('missing', 'position', 'winding', 'material'):
            after = deepcopy(before)
            if mutation == 'position':
                after['points'] = ((.001, 0., 7.5), *after['points'][1:])
            elif mutation == 'winding':
                after['points'] = tuple(reversed(after['points']))
            elif mutation == 'material':
                after['material_sha256'] = 'different-material'
            with self.subTest(mutation=mutation), self.assertRaisesRegex(ValueError, 'raw material|winding'):
                audit.compare_bodies([before], [] if mutation == 'missing' else [after])

    def test_candidate_name_cannot_grant_permission_to_repaint_a_native_barrier(self):
        before = face(texture=0x5EB4BEE9, name='Jersey barrier')
        after = deepcopy(before)
        after['mesh_name'] = 'SCP NAM barrier'
        after['uv'] = tuple((u + .1, v) for u, v in before['uv'])
        with self.assertRaisesRegex(ValueError, 'retained native'):
            audit.compare_bodies([before], [after])

    def test_native_avenue_uvs_remain_exact_even_under_an_authored_mesh_name(self):
        before = face(texture=0x0400380E, name='SCP NAM ramp')
        after = deepcopy(before)
        after['uv'] = tuple((u, v + .1) for u, v in before['uv'])
        with self.assertRaisesRegex(ValueError, 'retained native'):
            audit.compare_bodies([before], [after])

    def test_existing_support_helper_accepts_different_subdivision_in_both_directions(self):
        whole = face(texture=audit.DD)
        one = face(((0., 0., 7.5), (4., 0., 7.5), (2., 2., 7.5)), texture=audit.DD)
        two = face(((0., 0., 7.5), (2., 2., 7.5), (0., 4., 7.5)), texture=audit.DD)
        self.assertEqual(audit._coverage([whole], [one, two])['line_segments_checked'], 6)
        self.assertEqual(audit._coverage([one, two], [whole])['line_segments_checked'], 12)

    def test_missing_native_triangle_fails_the_centroid_and_edge_witnesses(self):
        whole = face(texture=audit.DD)
        one = face(((0., 0., 7.5), (4., 0., 7.5), (2., 2., 7.5)), texture=audit.DD)
        with self.assertRaisesRegex(ValueError, 'native DD coverage'):
            audit._coverage([whole], [one])

    def test_historical_native_hole_fill_needs_one_frozen_donor_and_keeps_removal_strict(self):
        # Actual newly retained saved02 triangle in source city cell[-3,4].
        # The historical mouths01 remap has a tiny hole here, even though
        # the complete triangle belongs to its frozen native DD donor.
        repaired = face(((-44.61283016204834, -61.678523540496826, 15.),
                         (-44.61279845237732, -61.678497552871704, 15.),
                         (-44.61282968521118, -61.67849659919739, 15.)), texture=audit.DD)
        repaired['material_sha256'] = '307aba7786d4b4f11dbc499eb54f7d05d01a114001919b8a5f7d55970fbb64ca'
        certificate = audit._native_fill_certificate(repaired)
        self.assertIsNotNone(certificate)
        self.assertEqual(certificate['native_city_cell'], [-3, 4])
        self.assertEqual(certificate['frozen_native_face_index'], 12)
        self.assertLessEqual(certificate['maximum_saved_vertex_distance_m'], 2e-6)
        self.assertTrue(certificate['whole_face_bounded_by_convexity'])
        with self.assertRaisesRegex(ValueError, 'native DD coverage'):
            audit._coverage([repaired], [])
        result = audit._coverage([repaired], [], permit_source_native_fill=True)
        self.assertFalse(result['historical_saved_reference_support_passed'])
        self.assertEqual(result['source_native_hole_fill_triangles'], 1)
        self.assertEqual(len(result['historical_reference_holes_repaired'][0]['historical_reference_gap_witnesses']), 6)
        self.assertTrue(result['source_native_hole_fill_projection']['passed'])

    def test_added_native_fill_outside_its_donor_or_with_wrong_material_plane_or_winding_is_rejected(self):
        donor = next(face for bucket in audit._native_donor_faces().bins.values() for face in bucket)
        approved = face(donor['points'], texture=audit.DD)
        approved['material_sha256'] = donor['material_sha256']
        self.assertIsNotNone(audit._native_fill_certificate(approved))
        for mutation in ('outside-donor', 'material', 'plane', 'winding'):
            changed = deepcopy(approved)
            if mutation == 'outside-donor':
                changed['points'] = tuple((x + 1000., y, h) for x, y, h in changed['points'])
            elif mutation == 'material':
                changed['material_sha256'] = 'unapproved-material'
            elif mutation == 'plane':
                changed['points'] = tuple((x, y, h + 5e-6) for x, y, h in changed['points'])
            else:
                changed['points'] = tuple(reversed(changed['points']))
            with self.subTest(mutation=mutation):
                self.assertIsNone(audit._native_fill_certificate(changed))
                with self.assertRaisesRegex(ValueError, 'native DD coverage'):
                    audit._coverage([changed], [], permit_source_native_fill=True)


if __name__ == '__main__':
    unittest.main()
