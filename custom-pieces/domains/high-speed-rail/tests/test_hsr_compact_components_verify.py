"""Literal compact contracts, portable PATHs and moved native collar checks."""
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp_hsr.hsr_compact_components_verify import CONTRACTS, OFFSET_96
from scp_hsr.hsr_components_verify import check_paths, audit_adapter_native_profiles
from scp_hsr.hsr_components_layout import component_layout, INFO
from scp_hsr.hsr_components import INFO as MODEL_INFO
from scp_hsr.hsr_mesh_verify import measure_journey_quality
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
from scp.track_paths import PATH, encode_paths
from scp_hsr.test_support import spec_for, floor


def generated_paths(recipe):
    spec = spec_for(recipe)
    layout = component_layout(recipe)
    return spec, {
        (*PATH, int(tile, 16)): encode_paths(layout[tuple(cell)]['routes'])
        if layout[tuple(cell)]['routes'] else EMPTY_STRUCTURAL_PATH
        for cell, tile in zip(spec['cells'], spec['tile_ids'])}


def compact_profile():
    planes = []
    for height in (31.189326, 29.01067):
        planes += floor(-7.5, 7.5, 80., 88., absolute_y=height)
        planes += floor(-4., 4., -8., 0., absolute_y=height)
        planes += floor(12., 20., -8., 0., absolute_y=height)
    for first, last in ((-7.5, -5.9965477), (5.9965477, 7.5)):
        planes += floor(first, last, 80., 88., absolute_y=31.98933)
    for first, last in ((-4., -2.6), (2.6, 4.), (12., 13.4), (18.6, 20.)):
        planes += floor(first, last, -8., 0., absolute_y=31.98933)
    return planes


class CompactComponentContractsTests(unittest.TestCase):
    def test_four_literal_masks_native_ports_and_support_plans_match_generated_parts(self):
        self.assertEqual(len(CONTRACTS), 4)
        for recipe, contract in CONTRACTS.items():
            with self.subTest(recipe=recipe):
                actual = INFO[recipe]
                self.assertEqual(tuple(actual['footprint']), contract['footprint'])
                self.assertEqual(actual['cells'], contract['cells'])
                self.assertEqual(actual['structural_cells'], contract['structural_cells'])
                self.assertEqual(MODEL_INFO[recipe]['support_centers'],
                                 [(x, -south) for x, south in contract['support_centres_xz']])
                spec, paths = generated_paths(recipe)
                report = check_paths(paths, spec)
                self.assertEqual(report['external_ports_checked'], len(contract['ports']))
                self.assertEqual(report['unique_complete_journeys_checked'], len(contract['movements']))
                self.assertEqual(report['rotations_checked'], 4)
                self.assertEqual(report['maximum_encoded_grade'], 0.)
                for measured in report['journey_quality'].values():
                    self.assertLessEqual(measured['maximum_curvature_change_per_m2'], .0015)

    def test_missing_encoded_connections_and_missing_structural_mask_are_rejected(self):
        for recipe, contract in CONTRACTS.items():
            with self.subTest(recipe=recipe):
                spec, paths = generated_paths(recipe)
                changed = dict(paths)
                first_real = next(key for key, raw in paths.items() if raw != EMPTY_STRUCTURAL_PATH)
                changed[first_real] = EMPTY_STRUCTURAL_PATH
                with self.assertRaises(ValueError):
                    check_paths(changed, spec)
                with self.assertRaisesRegex(ValueError, 'structural'):
                    check_paths(paths, {**spec, 'structural_cells': []})

    def test_shortening_the_fourteen_metre_offset_to_64m_still_fails_curvature_easing(self):
        # Independently authored analytic test path; no generator is queried.
        # Preserve the established radius and curvature-change standards so
        # the failure specifically proves why the 64 m variant was rejected.
        points = []
        for index in range(129):
            distance = index*.5
            t = min(1., max(0., (distance-8.)/48.))
            q = 10.*t**3-15.*t**4+6.*t**5
            points.append((2.+14.*q, -56.+distance, 15.5))
        limits = {**OFFSET_96, 'min_length_m': 64., 'max_length_m': 67.,
                  'max_total_turn_degrees': 60., 'min_radius_m': 24.}
        self.assertEqual(limits['max_curvature_change_per_m2'], .0015)
        with self.assertRaisesRegex(ValueError, 'curvature changes abruptly'):
            measure_journey_quality(points, limits)

    def test_new_adapter_collar_uses_its_actual_88m_south_coordinate(self):
        planes = compact_profile()
        result = audit_adapter_native_profiles(planes, paired_south_north_m=-88.)
        self.assertEqual(result['native_adapter_profile_sections_checked'], 12)
        self.assertFalse(result['paired_collar_internal_walls'])
        with self.assertRaisesRegex(ValueError, 'width, continuity or thickness'):
            audit_adapter_native_profiles(planes)

    def test_compact_collar_rejects_an_internal_wall_and_missing_underside(self):
        planes = compact_profile()
        wall = ((0., 31.5, 80., .1, 0.), (0., 31.8, 88., .1, 0.),
                (0., 31.5, 88., .1, 0.))
        with self.assertRaisesRegex(ValueError, 'internal wall'):
            audit_adapter_native_profiles(planes+[wall], paired_south_north_m=-88.)
        without_underside = [tri for tri in planes if min(vertex[1] for vertex in tri) > 30.]
        with self.assertRaisesRegex(ValueError, 'width, continuity or thickness'):
            audit_adapter_native_profiles(without_underside, paired_south_north_m=-88.)


if __name__ == '__main__':
    unittest.main()
