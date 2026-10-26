"""Independent contracts and negative controls for the refined HSR parts."""
from copy import deepcopy
from collections import defaultdict
import math
from pathlib import Path
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp_hsr.hsr_refined_components_verify import (
    CONTRACTS, audit_refined_journeys, audit_y_native_profiles,
)
from scp_hsr.hsr_components_verify import check_paths
from scp_hsr.hsr_components_layout import component_layout, INFO
from scp_hsr.hsr_components import INFO as MODEL_INFO
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
from scp_hsr.interchange_verify import _encoded_routes, _clearance_segments
from scp_hsr.directional_t_verify import _journeys
from scp.track_paths import PATH, encode_paths
from scp_hsr.test_support import spec_for, floor


def generated(recipe):
    spec = spec_for(recipe)
    layout = component_layout(recipe)
    resources = {
        (*PATH, int(tile, 16)): encode_paths(layout[tuple(cell)]['routes'])
        if layout[tuple(cell)]['routes'] else EMPTY_STRUCTURAL_PATH
        for cell, tile in zip(spec['cells'], spec['tile_ids'])}
    journeys = _journeys(_encoded_routes(resources, spec, CONTRACTS[recipe]), CONTRACTS[recipe])
    return spec, resources, journeys


def y_profiles():
    faces = []
    for height in (31.189326, 29.01067):
        faces += floor(88.5, 103.5, -8., 0., absolute_y=height)
    for first, last in ((88.5, 90.0034523), (101.9965477, 103.5)):
        faces += floor(first, last, -8., 0., absolute_y=31.98933)
    for first, last in ((-8., 0.), (192., 200.)):
        for height in (16.189326, 14.01067):
            faces += floor(first, last, 92., 100., absolute_y=height)
        for near, far in ((92., 93.4), (98.6, 100.)):
            faces += floor(first, last, near, far, absolute_y=16.98933)
    return faces


class RefinedComponentContractsTests(unittest.TestCase):
    def test_literal_masks_supports_ports_and_all_encoded_journeys(self):
        self.assertEqual(len(CONTRACTS), 2)
        for recipe, contract in CONTRACTS.items():
            with self.subTest(recipe=recipe):
                self.assertEqual(tuple(INFO[recipe]['footprint']), contract['footprint'])
                self.assertEqual(INFO[recipe]['cells'], contract['cells'])
                self.assertEqual(INFO[recipe]['structural_cells'], contract['structural_cells'])
                actual = {tuple(round(value, 9) for value in point)
                          for point in MODEL_INFO[recipe]['support_centers']}
                expected = {(round(x, 9), round(-south, 9))
                            for x, south in contract['support_centres_xz']}
                self.assertEqual(actual, expected)
                spec, paths, journeys = generated(recipe)
                report = check_paths(paths, spec)
                self.assertEqual(report['external_ports_checked'], len(contract['ports']))
                self.assertEqual(report['unique_complete_journeys_checked'], len(contract['movements']))
                self.assertEqual(report['rotations_checked'], 4)
                self.assertLessEqual(report['maximum_encoded_grade'], .156251)
                audit_refined_journeys(journeys, recipe)

    def test_new_north_and_south_support_plans_are_mirrors_with_full_spacing(self):
        for recipe, axis, count in (
                ('hsr_component_symmetric_graded_y', 96., 15),):
            points = CONTRACTS[recipe]['support_centres_xz']
            self.assertEqual(len(points), count)
            for x, south in points:
                self.assertTrue(any(math.dist((2.*axis-x, south), other) < 3e-9
                                    for other in points))
            self.assertGreaterEqual(min(math.dist(first, last)
                                        for number, first in enumerate(points)
                                        for last in points[number+1:]), 16.-1e-8)

    def test_lower_quarter_supports_reflect_across_its_diagonal(self):
        points = CONTRACTS['hsr_component_lower_oneway_curve90_right']['support_centres_xz']
        self.assertEqual(len(points), 10)
        for east, south in points:
            self.assertTrue(any(math.dist((south, east), other) < 3e-9
                                for other in points))
        self.assertGreaterEqual(min(math.dist(first, last)
                                    for number, first in enumerate(points)
                                    for last in points[number+1:]), 16.-1e-8)

    def test_y_flat_separation_distance_and_mirror_cannot_be_removed(self):
        recipe = 'hsr_component_symmetric_graded_y'
        _, _, journeys = generated(recipe)
        report = audit_refined_journeys(journeys, recipe)
        self.assertEqual(report['upper_flat_before_deck_separation_m'], 56.)
        self.assertLessEqual(report['maximum_3d_reflection_error_m'], 3e-6)
        changed = deepcopy(journeys)
        point = changed['Nin', 'Wout'][20]
        changed['Nin', 'Wout'][20] = (*point[:2], point[2]-.001)
        with self.assertRaisesRegex(ValueError, '56 m'):
            audit_refined_journeys(changed, recipe)
        changed = deepcopy(journeys)
        point = changed['Ein', 'Nout'][20]
        changed['Ein', 'Nout'][20] = (point[0]+.01, *point[1:])
        with self.assertRaisesRegex(ValueError, 'mirrored reverse'):
            audit_refined_journeys(changed, recipe)

    def test_all_three_native_ends_have_full_slab_underside_and_caps(self):
        report = audit_y_native_profiles(y_profiles())
        self.assertEqual(report['native_y_profile_sections_checked'], 18)
        self.assertEqual(report['native_y_paired_slab_width_m'], 15.)
        self.assertEqual(report['native_y_arm_slab_width_m'], 8.)
        self.assertFalse(report['paired_collar_internal_walls'])

    def test_y_pair_internal_wall_missing_arm_underside_and_narrow_head_fail(self):
        planes = y_profiles()
        wall = ((96., 31.5, -8., .1, 0.), (96., 31.8, 0., .1, 0.),
                (96., 31.5, 0., .1, 0.))
        with self.assertRaisesRegex(ValueError, 'internal wall'):
            audit_y_native_profiles(planes+[wall])
        without_arm_underside = [triangle for triangle in planes
                                 if not (all(p[0] >= 192. for p in triangle) and
                                         all(abs(p[1]-14.01067) < 1e-6 for p in triangle))]
        with self.assertRaisesRegex(ValueError, 'width, continuity or thickness'):
            audit_y_native_profiles(without_arm_underside)
        narrow = [triangle for triangle in planes
                  if not all(abs(p[1]-31.189326) < 1e-6 for p in triangle)]
        narrow += floor(92., 100., -8., 0., absolute_y=31.189326)
        with self.assertRaisesRegex(ValueError, 'width, continuity or thickness'):
            audit_y_native_profiles(narrow)

    def test_real_submicrometre_cap_triangle_outside_corridor_is_clear(self):
        records = [((0, 0), {}, [(200., -96., 15.5), (192., -96., 15.5)])]
        # This actual compiled native cap is 0.099999905 m outside the
        # required five-metre train corridor. Its tiny map area previously
        # confused the absolute orientation tolerance with collinearity.
        cap = ((192.000000099, 16.989326, 93.400000095, .1, 0.),
               (192.000000521, 16.989326, 92.000000954, .1, 0.),
               (192.000000200, 16.989326, 93.400000095, .1, 0.))
        self.assertEqual(_clearance_segments(records, defaultdict(lambda: [cap]),
                                             half_width=2.5), 1)

    def test_same_tiny_cap_inside_corridor_still_blocks_train(self):
        records = [((0, 0), {}, [(200., -96., 15.5), (192., -96., 15.5)])]
        cap = ((192.000000099, 16.989326, 95.400000095, .1, 0.),
               (192.000000521, 16.989326, 94.000000954, .1, 0.),
               (192.000000200, 16.989326, 95.400000095, .1, 0.))
        with self.assertRaisesRegex(ValueError, 'clearance envelope'):
            _clearance_segments(records, defaultdict(lambda: [cap]), half_width=2.5)


if __name__ == '__main__':
    unittest.main()
