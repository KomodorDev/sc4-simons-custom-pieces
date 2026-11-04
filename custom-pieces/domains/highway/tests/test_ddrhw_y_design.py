"""Reject broken native contacts, climbing braids, and grade corruptions."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import sys
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'framework'))
from scp import jsonc


def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'domains/highway/tools'/f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GEOMETRY = load_tool('ddrhw_y_geometry')
VERIFY = load_tool('verify_ddrhw_y_design')
SUBJECT = ROOT/'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction'


class DDRHWYSourceDesignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.brief = jsonc.load(SUBJECT/'checks/design-brief.jsonc')
        cls.native = jsonc.load(SUBJECT/'evidence/native-design-inputs.jsonc')
        cls.design = GEOMETRY.build_design(cls.brief, cls.native)

    def test_measured_candidate_has_six_safe_source_journeys(self):
        result = VERIFY.verify(self.design, self.brief, self.native, negative_controls=True)
        self.assertTrue(result['passed'])
        self.assertEqual(result['native_members_checked'], 12)
        self.assertEqual(len(result['continuous_pair_checks']), 15)
        self.assertTrue(all(row['rejected'] for row in result['negative_controls'].values()))
        self.assertFalse(result['game_operation_tested'])

    def test_zero_bulge_produces_an_actual_climbing_route_collision(self):
        brief = deepcopy(self.brief)
        brief['geometry_parameters']['bulge_m'] = 0.
        collision = GEOMETRY.build_design(brief, self.native)
        with self.assertRaisesRegex(ValueError, 'vehicle corridors overlap: B-C / C-B'):
            VERIFY.verify(collision, brief, self.native)

    def test_displaced_native_endpoint_is_rejected(self):
        broken = deepcopy(self.design)
        broken['routes']['A-B'][0][0] += .05
        with self.assertRaisesRegex(ValueError, 'Native endpoint moved'):
            VERIFY.verify(broken, self.brief, self.native)

    def test_swapped_native_lane_class_is_rejected(self):
        broken = deepcopy(self.design)
        broken['route_metadata']['B-C']['from_lane'] = 0
        with self.assertRaisesRegex(ValueError, 'Native lane metadata changed'):
            VERIFY.verify(broken, self.brief, self.native)

    def test_interior_grade_spike_is_rejected(self):
        broken = deepcopy(self.design)
        points = broken['routes']['B-C']
        points[len(points)//2][2] += .5
        with self.assertRaisesRegex(ValueError, 'Source grade exceeds'):
            VERIFY.verify(broken, self.brief, self.native)

    def test_flat_stem_route_cannot_hide_an_interior_height_change(self):
        broken = deepcopy(self.design)
        points = broken['routes']['A-B']
        points[len(points)//2][2] += .001
        with self.assertRaisesRegex(ValueError, 'flat stem journey changes height'):
            VERIFY.verify(broken, self.brief, self.native)

    def test_native_audit_pose_must_match_its_donor_routes(self):
        broken = deepcopy(self.native)
        broken['first_alignment_socket_example'][1]['native_clockwise_quarter_turns'] = 2
        with self.assertRaisesRegex(ValueError, 'posed contact|posed member|four real lane members'):
            VERIFY.verify(self.design, self.brief, broken)

    def test_segment_distance_controls_cover_crossings_and_nonintersecting_edges(self):
        actual = VERIFY.segment_distances(
            np.array([[0., 0.]]), np.array([[10., 0.]]),
            np.array([[5., -3.], [0., 5.], [13., 4.], [5., 0.]]),
            np.array([[5., 3.], [10., 5.], [13., 10.], [15., 0.]]))[0]
        np.testing.assert_allclose(actual, [0., 5., 5., 0.], atol=1e-12)


if __name__ == '__main__':
    unittest.main()
