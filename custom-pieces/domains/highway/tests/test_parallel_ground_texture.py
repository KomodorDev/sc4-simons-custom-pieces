"""Regress actual saved tight-turn pavement wedges without native image bytes."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp_highway.parallel_geometry import ParallelRoadPainter

# Real decoded S3D triangles from the first failed southeast terminal build.
# Each sampled one constant MIS U/V despite having real pavement area.
CAPTURED_WEDGES = (
    ((8.0, -17.639771699905396, 0.0),
     (7.906491279602051, -18.383939504623413, 0.0),
     (7.906859397888184, -18.383988618850708, 0.0)),
    ((17.6812664270401, -8.29320764541626, 0.0),
     (18.26921534538269, -8.219905853271484, 0.0),
     (18.606886386871338, -8.14660358428955, 0.0)),
)


class ParallelGroundTextureTests(unittest.TestCase):
    def setUp(self):
        evidence = ROOT / ('domains/highway/01_assemblies/'
                           'ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/'
                           'evidence/parallel-ramp-review.json')
        candidate = next(c for c in json.loads(evidence.read_text())['source_geometry_review']['candidates']
                         if c['id'] == 'parallel-inward-upper')
        # This test measures station geometry, not material/image provenance.
        with patch('scp_highway.ramp_materials.native_materials', return_value={}):
            self.painter = ParallelRoadPainter({}, candidate['routes'])

    def paint(self, points, cell=(0, 0)):
        triangle = tuple((e - 16 * cell[0], h, -n - 16 * cell[1], .125, .5)
                         for e, n, h in points)
        return self.painter.paint(triangle, cell)

    def test_actual_failed_ground_wedges_keep_spatial_native_repeat(self):
        for points in CAPTURED_WEDGES:
            with self.subTest(points=points):
                role, saved = self.paint(points)
                self.assertEqual(role, 'ramp')
                self.assertTrue(all(p[3] == .59375 for p in saved))
                self.assertGreater(max(p[4] for p in saved) - min(p[4] for p in saved), 1e-5)
                self.assertEqual([p[:3] for p in saved], [(e, h, -n) for e, n, h in points])

    def test_actual_clipped_barrier_bevel_is_not_misread_as_a_flat_crown(self):
        points = ((-50.65943694114685, -40., 8.890625),
                  (-50.65996837615967, -40.00191688537598, 8.890625),
                  (-50.65846395492554, -40., 8.874685287475586))
        triangle = tuple((e, h, -n, .375, .5) for e, n, h in points)
        role, saved = self.painter.paint(triangle)
        self.assertEqual(role, 'barrier')
        self.assertGreater(max(p[4] for p in saved) - min(p[4] for p in saved), .001)
        self.assertEqual([p[:3] for p in saved], [(e, h, -n) for e, n, h in points])

    def test_same_world_corner_keeps_phase_across_component_cell_frames(self):
        for points in CAPTURED_WEDGES:
            original = self.paint(points)[1]
            translated = self.paint(points, (1, 1))[1]
            for first, second in zip(original, translated):
                self.assertAlmostEqual(first[3], second[3], places=12)
                self.assertAlmostEqual(first[4], second[4], places=12)

    def test_flat_chord_extrapolation_keeps_one_metre_of_texture_per_metre(self):
        painter = object.__new__(ParallelRoadPainter)
        painter.road_segments = {0: [0]}
        painter.segments = [((0., 0., 0.), (16., 0., 0.), 0., 16., 1., 0., 0)]
        painter._ground_station_cache = {}
        for x in (-1., 0., 8., 16., 17.):
            self.assertEqual(painter._ground_station((x, 2., 0.), 0), x)

    def test_graded_chord_does_not_acquire_unbounded_ground_extrapolation(self):
        painter = object.__new__(ParallelRoadPainter)
        painter.road_segments = {0: [0]}
        painter.segments = [((0., 0., 1.), (16., 0., 0.), 0., 16., 1., 0., 0)]
        painter._ground_station_cache = {}
        self.assertEqual(painter._ground_station((17., 0., 0.), 0), 16.)


if __name__ == '__main__':
    unittest.main()
