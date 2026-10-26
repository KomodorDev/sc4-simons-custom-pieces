"""Geometry invariants use a small original XYZ/UV donor, not installed NAM."""
from __future__ import annotations

from pathlib import Path
import struct
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))
from scp.models import parse_s3d, pack_s3d, validate_s3d
from scp_hsr.single_track_models import _subtract, _normal


from scp_hsr.test_support import donor, triangles


class RailMeshPrimitiveTests(unittest.TestCase):










    def test_footprint_subtraction_keeps_area_and_interpolated_uvs(self):
        polygon = [(-2, 0, -2, 0, 0), (2, 0, -2, 1, 0),
                   (2, 0, 2, 1, 1), (-2, 0, 2, 0, 1)]
        result = _subtract(polygon, [(-2, -2), (0, -2), (0, 2), (-2, 2)])
        self.assertAlmostEqual(sum(abs(_normal(t)[1]) / 2 for t in result), 8)
        for tri in result:
            for vertex in tri:
                self.assertGreaterEqual(vertex[0], -1e-6)
                self.assertAlmostEqual(vertex[3], (vertex[0] + 2) / 4)
                self.assertAlmostEqual(vertex[4], (vertex[2] + 2) / 4)

    def test_vertical_face_on_footprint_boundary_is_not_duplicated(self):
        triangle = [(0, 0, -1, 0, 0), (0, 2, -1, 0, 1), (0, 0, 1, 1, 0)]
        self.assertEqual(_subtract(triangle, [(0, -2), (2, -2), (2, 2), (0, 2)]), [])



if __name__ == '__main__':
    unittest.main()
