"""Encoded-path and physical native-profile proofs for the new tight loop."""
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp_hsr.hsr_tight_loop_components_verify import (
    CONTRACTS, audit_tight_journeys, audit_tight_native_profiles,
)
from scp_hsr.hsr_tight_loop_components import canonical
from scp_hsr.hsr_components_layout import component_layout, component_routes, INFO
from scp_hsr.hsr_components import INFO as MODEL_INFO
from scp_hsr.hsr_components_verify import check_paths
from scp_hsr.directional_t_verify import _journeys
from scp_hsr.interchange_verify import _encoded_routes
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
from scp.track_paths import PATH, encode_paths
from scp_hsr.test_support import spec_for, floor


def generated(recipe):
    spec = spec_for(recipe)
    layout = component_layout(recipe)
    resources = {(*PATH, int(tile, 16)): encode_paths(layout[tuple(cell)]['routes'])
                 if layout[tuple(cell)]['routes'] else EMPTY_STRUCTURAL_PATH
                 for cell, tile in zip(spec['cells'], spec['tile_ids'])}
    journeys = _journeys(_encoded_routes(resources, spec, CONTRACTS[recipe]), CONTRACTS[recipe])
    return spec, resources, journeys


def native_profiles(first, last):
    triangles = []
    for height in (first+.689326, first-1.48933):
        triangles += floor(-7.5, 7.5, 48., 56., absolute_y=height)
    for near, far in ((-7.5, -5.9965477), (5.9965477, 7.5)):
        triangles += floor(near, far, 48., 56., absolute_y=first+1.48933)
    for height in (last+.689326, last-1.48933):
        triangles += floor(48., 56., -7.5, 7.5, absolute_y=height)
    for near, far in ((-7.5, -5.9965477), (5.9965477, 7.5)):
        triangles += floor(48., 56., near, far, absolute_y=last+1.48933)
    return triangles


class TightPairedLoopTests(unittest.TestCase):
    def test_both_literal_masks_supports_and_actual_encoded_paths(self):
        self.assertEqual(len(CONTRACTS), 2)
        for recipe, contract in CONTRACTS.items():
            with self.subTest(recipe=recipe):
                self.assertEqual(INFO[recipe]['footprint'], (4, 4))
                self.assertEqual(INFO[recipe]['cells'], contract['cells'])
                self.assertEqual(INFO[recipe]['structural_cells'], contract['structural_cells'])
                self.assertEqual(MODEL_INFO[recipe]['support_centers'],
                                 [(x, -south) for x, south in contract['support_centres_xz']])
                spec, paths, journeys = generated(recipe)
                report = check_paths(paths, spec)
                self.assertEqual(report['rotations_checked'], 4)
                self.assertEqual(report['unique_complete_journeys_checked'], 2)
                self.assertEqual(report['native_port_heights_m'],
                                 sorted({contract['ports']['Sin'][2], contract['ports']['Ein'][2]}))
                self.assertLess(report['maximum_encoded_grade'], .156251)
                for quality in report['journey_quality'].values():
                    self.assertGreaterEqual(quality['minimum_sampled_radius_m'], 24.)
                    self.assertLessEqual(quality['maximum_curvature_change_per_m2'], .0015)
                    self.assertLessEqual(quality['maximum_grade_change_per_m'], .011)
                pair = audit_tight_journeys(journeys, recipe)
                self.assertGreaterEqual(pair['paired_shared_sheet_points_checked'], 1000)
                self.assertLessEqual(pair['maximum_paired_shared_height_error_m'], 2e-6)

    def test_encoded_paired_grade_cannot_be_retimed_or_shifted(self):
        recipe = 'hsr_component_tight_paired_curve90_l4_to_mid'
        _, _, journeys = generated(recipe)
        for axis in (0, 2):
            changed = deepcopy(journeys)
            point = list(changed['Ein', 'Sout'][200])
            point[axis] += .01
            changed['Ein', 'Sout'][200] = tuple(point)
            with self.assertRaisesRegex(ValueError, 'shared-height sheet'):
                audit_tight_journeys(changed, recipe)

    def test_two_rotated_corners_form_the_literal112m_half_loop_without_cap(self):
        first = component_routes('hsr_component_tight_paired_curve90_l4_to_mid')
        second = component_routes('hsr_component_tight_paired_curve90_mid_to_l2')
        place_first = lambda p: (p[0], p[1]+144., p[2])
        place_second = lambda p: (p[1]+112., -p[0]+144., p[2])
        for movement in ('S>E', 'E>S'):
            a, b = [place_first(p) for p in first[movement]], [place_second(p) for p in second[movement]]
            if movement == 'S>E':
                self.assertEqual(a[0], (2., 88., 30.5))
                self.assertEqual(a[-1], b[0])
                self.assertEqual(a[-1], (56., 142., 23.))
                self.assertEqual(b[-1], (110., 88., 15.5))
            else:
                self.assertEqual(b[0], (114., 88., 15.5))
                self.assertEqual(b[-1], a[0])
                self.assertEqual(b[-1], (56., 146., 23.))
                self.assertEqual(a[-1], (-2., 88., 30.5))
        supports = [(x, 144.-south) for x, south in CONTRACTS[
            'hsr_component_tight_paired_curve90_l4_to_mid']['support_centres_xz']]
        supports += [(112.-south, 144.-x) for x, south in CONTRACTS[
            'hsr_component_tight_paired_curve90_mid_to_l2']['support_centres_xz']]
        self.assertEqual(len(supports), 12)
        self.assertGreaterEqual(min(math.dist(a, b) for i, a in enumerate(supports)
                                    for b in supports[i+1:]), 16.)

    def test_both_paths_share_every_physical_sheet_station_height(self):
        for recipe in CONTRACTS:
            routes, sheets = canonical(recipe)
            center = sheets[0]['points']
            first, last = routes['S>E'], list(reversed(routes['E>S']))
            self.assertEqual([p[2] for p in first], [p[2] for p in center])
            self.assertEqual([p[2] for p in last], [p[2] for p in center])
            for a, b in zip(first, last):
                self.assertAlmostEqual(math.dist(a[:2], b[:2]), 4., places=12)

    def test_all_three_physical_connection_heights_have_full_native_profiles(self):
        for recipe, contract in CONTRACTS.items():
            first, last = contract['ports']['Sin'][2], contract['ports']['Ein'][2]
            result = audit_tight_native_profiles(native_profiles(first, last), recipe)
            self.assertEqual(result['native_tight_corner_profile_sections_checked'], 12)
            self.assertEqual(result['native_paired_slab_width_m'], 15.)
            self.assertFalse(result['paired_collar_internal_walls'])

    def test_wrong_midpoint_missing_underside_and_internal_wall_are_rejected(self):
        recipe = 'hsr_component_tight_paired_curve90_l4_to_mid'
        with self.assertRaisesRegex(ValueError, 'width, continuity or thickness'):
            audit_tight_native_profiles(native_profiles(30.5, 22.5), recipe)
        triangles = native_profiles(30.5, 23.)
        without_underside = [tri for tri in triangles if not all(abs(p[1]-21.51067) < 1e-6 for p in tri)]
        with self.assertRaisesRegex(ValueError, 'width, continuity or thickness'):
            audit_tight_native_profiles(without_underside, recipe)
        wall = ((0., 31.5, 48., .1, 0.), (0., 31.8, 56., .1, 0.),
                (0., 31.5, 56., .1, 0.))
        with self.assertRaisesRegex(ValueError, 'internal wall'):
            audit_tight_native_profiles(triangles+[wall], recipe)


if __name__ == '__main__':
    unittest.main()
