"""Targeted guards for independent upper decks and slope-seated supports."""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import sys
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))

from scp_hsr.hsr_mesh import (_height_aware_union, _plan_area, _Undersides,
                             _support, _plane, _underside_geometry, support_centers,
                             _compile_models,
                             _sweep_native_profile)
from scp_hsr.hsr_mesh_verify import audit_bed_union, audit_supports
from scp.models import parse_s3d
from scp_hsr.rail_feature_verify import _triangles
from scp_hsr.test_support import donor
from scp_hsr.single_track_models import _native
from scp_hsr.rail_repair_verify import _overlap


def square(height, gx=0., gz=0.):
    points = [(x, height+gx*x+gz*z, z, x/8., z/8.)
              for x, z in ((0., 0.), (8., 0.), (8., 8.), (0., 8.))]
    return [(points[0], points[1], points[2]), (points[0], points[2], points[3])]


class HSRMeshPlaneUnionTests(unittest.TestCase):
    def test_bbox_rejection_preserves_exact_vertices_uvs_and_face_order(self):
        def plate(x, z, h, gx=0., gz=0.):
            p = [(a, h+gx*a+gz*b, b, a/8., b/8.)
                 for a, b in ((x, z), (x+4., z), (x+4., z+4.), (x, z+4.))]
            return [(p[0], p[1], p[2]), (p[0], p[2], p[3])]
        # These current-geometry fingerprints were measured immediately
        # before moving the identical bbox predicate ahead of plane fitting.
        # All coordinates use binary-exact fractions; no donor or libm data
        # enters this exact vertex/UV/order comparison.
        cases = [
            (plate(0., 0., 16.25)+plate(2., 1., 16.25)+plate(0., 0., 31.25),
             '678d2ade53e3bb3da30995b5b3453ad02faa2a83b7ed68d4088f9a19a7a437be'),
            (plate(0., 0., 16.25, .125, -.0625)+plate(2., 1., 16.25, .125, -.0625)+
             plate(0., 0., 31.25, .125, -.0625),
             '750989308d2ebecf8ea545337bdc1b07a34a0ab9fb373883407e1b93f7df2e85'),
            (plate(0., 0., 16.25, .125, -.0625)+plate(4., 1., 30.25, -.0625, .125)+
             plate(8., 0., 31.25),
             '605c00d1437f566617a873493ccc86881e772974c0329e27d51938fbae287ee2')]
        for faces, expected in cases:
            output = json.dumps(_height_aware_union(faces), separators=(',', ':')).encode()
            self.assertEqual(hashlib.sha256(output).hexdigest(), expected)

    def test_two_identical_floor_copies_are_emitted_once(self):
        floors = square(16.2)
        union = _height_aware_union(floors+floors)
        self.assertAlmostEqual(sum(_plan_area(list(t)) for t in union), 64.)

    def test_same_map_position_on_two_levels_retains_both_complete_surfaces(self):
        union = _height_aware_union(square(16.2)+square(31.2))
        self.assertAlmostEqual(sum(_plan_area(list(t)) for t in union), 128.)
        for expected in (16.2, 31.2):
            self.assertAlmostEqual(sum(_plan_area(list(t)) for t in union
                                       if abs(t[0][1]-expected) < 1e-6), 64.)

    def test_a_real_slope_is_preserved_and_same_slope_duplicates_are_joined(self):
        slope = square(16.2, .07, -.03)
        union = _height_aware_union(slope+slope+square(31.2, .07, -.03))
        self.assertAlmostEqual(sum(_plan_area(list(t)) for t in union), 128.)
        for triangle in union:
            gx, gz, intercept = _plane(triangle)
            self.assertAlmostEqual(gx, .07)
            self.assertAlmostEqual(gz, -.03)
            self.assertTrue(abs(intercept-16.2) < 1e-6 or abs(intercept-31.2) < 1e-6)

    def test_different_crossing_slopes_are_not_flattened_into_one_surface(self):
        union = _height_aware_union(square(16.2, .1)+square(16.2, -.1))
        self.assertAlmostEqual(sum(_plan_area(list(t)) for t in union), 128.)

    def test_native_micrometre_bed_noise_uses_the_audited_coplanarity(self):
        union = _height_aware_union(square(16.2)+square(16.200002))
        self.assertAlmostEqual(sum(_plan_area(list(t)) for t in union), 64.)

    def test_warped_graded_deck_never_paints_its_ballast_over_its_own_rails(self):
        source = _native(donor())
        deck = {'points': [(0., 0., 30.5), (4., .5, 30.1),
                           (8., .75, 29.7), (12., .75, 29.3)],
                'width': 8., 'profile': 'hsr', 'precise_union': True,
                'clearance_half_width': 2.6}
        surfaces = _sweep_native_profile(source, deck)[0]
        floors = [(kind, tri) for kind in ('rail', 'bed')
                  for actual, tri in surfaces if actual == kind]
        def painted_overlap(parts):
            rails = [tri for kind, tri in parts if kind == 'rail']
            beds = [tri for kind, tri in parts if kind == 'bed']
            return sum(_overlap([(v[0], v[2]) for v in a], [(v[0], v[2]) for v in b])
                       for a in rails for b in beds)
        # A plane comparison alone cannot classify the independently
        # triangulated narrow rail and wide ballast on a warped sweep.
        self.assertGreater(painted_overlap(_height_aware_union(floors, tagged=True)), 1.)
        owned = _height_aware_union(floors, single_sheet=True, tagged=True)
        self.assertLess(painted_overlap(owned), 1e-9)
        lower = [triangle for kind, triangle in owned]
        upper = [tuple((x, h+15., z, u, v) for x, h, z, u, v in tri) for tri in lower]
        both = _height_aware_union(lower+upper)
        self.assertAlmostEqual(sum(_plan_area(list(tri)) for tri in both),
                               2.*sum(_plan_area(list(tri)) for tri in lower), places=7)


class HSRMeshSupportTests(unittest.TestCase):
    def test_head_follows_all_nine_real_slope_contacts(self):
        underside = _Undersides(square(14., .12, -.04))
        head = underside.head(4., 4.)
        self.assertEqual(len(head), 9)
        pillar = _support((4., 4.), head)
        top = {(round(v[0], 8), round(v[2], 8)): v[1]
               for tri in pillar for v in tri if v[1] > .05}
        for z in (3.35, 4., 4.65):
            for x in (3.35, 4., 4.65):
                self.assertAlmostEqual(top[round(x, 8), round(z, 8)], 14.+.12*x-.04*z)
        self.assertGreater(max(head)-min(head), .1)

    def test_pier_uses_lowest_deck_and_never_spans_the_gap_between_levels(self):
        index = _Undersides(square(14.)+square(29.))
        self.assertEqual(index.head(4., 4.), [14.]*9)
        partial = square(29.)+[(tuple((x, h, z, u, v) for x, h, z, u, v in tri))
                              for tri in square(14.)]
        self.assertEqual(_Undersides(partial).height(4., 4.), 14.)

    def test_incomplete_head_coverage_is_rejected(self):
        self.assertIsNone(_Undersides(square(14.)).head(0., 0.))

    def test_straight_support_plan_is_global_and_spaced_sixteen_metres(self):
        layout = {(x, 0): {'routes': [], 'decks': []} for x in range(4)}
        layout[0, 0]['decks'] = [{'points': [(-8., 0., 15.5), (56., 0., 30.5)],
                                  'width': 15., 'geometry_id': 'sloped',
                                  'profile': 'hsr', 'extend_endpoints': False}]
        centers = support_centers(layout)
        self.assertEqual(centers, [(0., -0.), (16., -0.), (32., -0.), (48., -0.)])
        triangles = _underside_geometry(layout[0, 0]['decks'])
        index = _Undersides(triangles)
        self.assertAlmostEqual(index.height(0., 0.), 14.01067+8.*15./64.)

    def test_a_foundation_may_not_extend_into_unreserved_neighbouring_land(self):
        # The deck may overhang its cell, but a new pillar still needs all
        # 1.3 m of its footprint reserved. Its centre alone is insufficient.
        layout = {(0, 0): {'routes': [], 'decks': [
            {'points': [(7.8, 8., 15.5), (7.8, -8., 15.5)], 'width': 8.,
             'geometry_id': 'edge', 'profile': 'hsr', 'extend_endpoints': False}]}}
        self.assertEqual(support_centers(layout), [])


class HSRMeshActualMeshTests(unittest.TestCase):
    def test_wider_single_clearance_keeps_closed_inside_parapet_faces(self):
        source = _native(donor())
        surfaces, corridors, _, _ = _sweep_native_profile(source,
            {'points': [(0., -8., 15.5), (0., 8., 15.5)], 'width': 8.,
             'profile': 'hsr', 'precise_union': True, 'clearance_half_width': 2.6})
        walls = [tri for kind, tri in surfaces if kind == 'inner_wall']
        self.assertEqual(len(walls), 4)
        self.assertEqual({round(abs(v[0]), 7) for tri in walls for v in tri}, {2.6})
        self.assertTrue(all(source['bed_y'] <= v[1] <= source['top']
                            for tri in walls for v in tri))
        polygons = [polygon for item in corridors for polygon in item['clearance_polygons']]
        self.assertGreaterEqual(max(x for polygon in polygons for x, z in polygon), 2.6)
        self.assertLessEqual(min(x for polygon in polygons for x, z in polygon), -2.6)

    def test_compiled_crossing_preserves_both_slabs_with_independent_full_width_audit(self):
        lower = [(0., -8., 15.5), (0., 8., 15.5)]
        upper = [(-8., 0., 29.5), (8., 0., 31.5)]
        decks = [{'points': points, 'width': width, 'geometry_id': str(index),
                  'profile': 'hsr', 'precise_union': True,
                  'clearance_half_width': 2.6, 'extend_endpoints': False}
                 for index, (points, width) in enumerate(((lower, 15.), (upper, 8.)))]
        result = _compile_models(donor(), {(0, 0): {'routes': [], 'decks': decks}},
                                 {'support_centers': [(0., 0.)]})
        mesh = list(_triangles(parse_s3d(result[0, 0])))
        report = audit_bed_union(mesh, [(None, None, lower), (None, None, upper)])
        self.assertEqual(report['full_width_bed_union_segments_checked'], 2)
        self.assertLess(report['maximum_uncovered_bed_area_m2'], 1e-5)
        support = audit_supports(mesh, {'support_centres_xz': [(0., 0.)],
                                       'foundation_width_m': 1.3,
                                       'minimum_support_spacing_m': 16.})
        self.assertEqual(support['support_contact_points_checked'], 9)

    def test_compiled_ramp_pier_has_nine_measured_slope_contacts(self):
        deck = {'points': [(-8., 0., 29.5), (8., 0., 31.5)], 'width': 8.,
                'geometry_id': 'ramp', 'profile': 'hsr', 'precise_union': True,
                'clearance_half_width': 2.6, 'extend_endpoints': False}
        result = _compile_models(donor(), {(0, 0): {'routes': [], 'decks': [deck]}},
                                 {'support_centers': [(0., 0.)]})
        report = audit_supports(list(_triangles(parse_s3d(result[0, 0]))),
                                {'support_centres_xz': [(0., 0.)], 'foundation_width_m': 1.3,
                                 'minimum_support_spacing_m': 16.})
        self.assertEqual(report['support_contact_points_checked'], 9)
        self.assertEqual(report['sloped_support_heads_checked'], 1)


if __name__ == "__main__":
    unittest.main()
