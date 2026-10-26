"""Test continuous saved-surface equivalence and reject unrelated changes.

Synthetic original XYZUV meshes exercise re-triangulation, interior coverage,
texture edits, physical movement, winding and the literal micrometre corner.
No NAM assets or full model generation are needed.
"""
from __future__ import annotations

from copy import deepcopy
import unittest

from scp_hsr.hsr_surface_equivalence import audit_corner_equivalence
from scp_hsr.single_track_models import _native, _pack
from scp_hsr.test_support import donor


def _vertex(x, z, y=16.2):
    return x, y, z, .3+.1*x+.04*z, .2+.05*x-.07*z


def _quad(reverse_diagonal=False):
    a,b,c,d = _vertex(0.,0.),_vertex(0.,1.),_vertex(1.,1.),_vertex(1.,0.)
    return [(a,b,d),(b,c,d)] if reverse_diagonal else [(a,b,c),(a,c,d)]


def _raw(triangles):
    return _pack(_native(donor()), triangles)


class CornerEquivalenceTests(unittest.TestCase):
    def test_full_affine_field_survives_a_different_diagonal(self):
        report = audit_corner_equivalence(_raw(_quad()), _raw(_quad(True)))
        self.assertTrue(report['continuous_oriented_surface_and_affine_uv_equivalence'])
        self.assertEqual(report['exact_common_oriented_xyzuv_triangles'], 0)
        self.assertGreater(report['before_to_after']['affine_intersections_checked'], 0)
        self.assertGreater(report['after_to_before']['affine_intersections_checked'], 0)

    def test_unchanged_encoded_model_passes_without_coverage_exemptions(self):
        raw = _raw(_quad())
        report = audit_corner_equivalence(raw,raw)
        self.assertEqual(report['exact_common_oriented_xyzuv_triangles'], 2)

    def test_missing_interior_face_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'outside the literal strip'):
            audit_corner_equivalence(_raw(_quad()), _raw(_quad()[:1]))

    def test_unrelated_texture_phase_edit_is_rejected(self):
        changed = [tuple((*v[:4],v[4]+.043) for v in tri) for tri in _quad()]
        with self.assertRaisesRegex(ValueError, 'outside the literal strip'):
            audit_corner_equivalence(_raw(_quad()),_raw(changed))

    def test_unrelated_physical_displacement_is_rejected(self):
        changed = [tuple((v[0],v[1]+.001,*v[2:]) for v in tri) for tri in _quad()]
        with self.assertRaisesRegex(ValueError, 'outside the literal strip'):
            audit_corner_equivalence(_raw(_quad()),_raw(changed))

    def test_forty_micrometre_boundary_rounding_keeps_strict_texture_mapping(self):
        changed = [tuple(_vertex(x-.00004 if x==1. else x,z,y) for x,y,z,u,v in tri)
                   for tri in _quad()]
        report = audit_corner_equivalence(_raw(_quad()),_raw(changed))
        self.assertEqual(report['position_tolerance_m'],4e-6)
        self.assertEqual(report['uv_tolerance'],3e-6)
        self.assertEqual(report['full_3d_surface_distance_bound_m'],1e-4)

    def test_half_millimetre_boundary_hole_is_rejected_despite_matching_texture(self):
        changed = [tuple(_vertex(x-.0005 if x==1. else x,z,y) for x,y,z,u,v in tri)
                   for tri in _quad()]
        with self.assertRaisesRegex(ValueError,'outside the literal strip'):
            audit_corner_equivalence(_raw(_quad()),_raw(changed))

    def test_half_millimetre_interior_height_shift_is_rejected(self):
        changed = [tuple((x,y+.0005,z,u,v) for x,y,z,u,v in tri) for tri in _quad()]
        with self.assertRaisesRegex(ValueError,'outside the literal strip'):
            audit_corner_equivalence(_raw(_quad()),_raw(changed))

    def test_reversed_surface_winding_is_rejected(self):
        changed = [tuple(reversed(tri)) for tri in _quad()]
        with self.assertRaisesRegex(ValueError, 'outside the literal strip'):
            audit_corner_equivalence(_raw(_quad()),_raw(changed))

    def test_added_surface_inside_literal_corner_can_change(self):
        tiny = [((-7.9999995,15.,7.1,.1,.1),(-7.9999995,16.,7.1,.1,.2),
                 (-7.9999995,16.,7.9,.2,.2))]
        report = audit_corner_equivalence(_raw(_quad()),_raw(_quad()+tiny))
        self.assertTrue(report['continuous_oriented_surface_and_affine_uv_equivalence'])

    def test_face_on_the_literal_corner_boundary_is_inside_the_allowed_box(self):
        old = [((-8.,15.,7.1,.1,.1),(-8.,16.,7.1,.1,.2),(-8.,16.,7.9,.2,.2))]
        new = [tuple((x+.0000005,y,z,u+.02,v+.03) for x,y,z,u,v in tri) for tri in old]
        report = audit_corner_equivalence(_raw(_quad()+old),_raw(_quad()+new))
        self.assertTrue(report['continuous_oriented_surface_and_affine_uv_equivalence'])

    def test_shifted_corner_surface_outside_literal_strip_is_rejected(self):
        displaced = [((-7.999,15.,7.1,.1,.1),(-7.999,16.,7.1,.1,.2),
                      (-7.999,16.,7.9,.2,.2))]
        with self.assertRaisesRegex(ValueError, 'outside the literal strip'):
            audit_corner_equivalence(_raw(_quad()),_raw(_quad()+displaced))

    def test_reports_do_not_share_mutable_cached_state(self):
        raw=_raw(_quad())
        first=audit_corner_equivalence(raw,raw)
        first['literal_allowed_tile_local_xyz'][0][0]=-999.
        self.assertEqual(audit_corner_equivalence(raw,raw)['literal_allowed_tile_local_xyz'][0][0],-8.)


if __name__ == '__main__':
    unittest.main()
