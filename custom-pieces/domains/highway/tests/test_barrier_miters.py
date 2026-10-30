"""Check all four native/ramp barrier junctions and outward surface winding."""
from pathlib import Path
import math
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / "framework"), str(ROOT / "domains/highway/implementation")]

from scp_highway import ramp_geometry as geometry


# Independent probes of the missing native-profile strips in the approved
# layout. Each pair names the two ramp-edge barriers; each triple inspects
# the low outer face, crown, and low inner face, respectively. Coordinates
# use longitudinal u, native-side v, and height above the deck.
WITNESSES = {
    "lower-off": ((62.794798944, 63.152083782, 63.532926083),
                  (49.944557032, 50.734879806, 51.538773586)),
    "lower-on": ((-62.794798944, -63.152083782, -63.532926083),
                 (-49.944557032, -50.734879806, -51.538773586)),
    "upper-off": ((-89.327115384, -89.912158409, -90.534302517),
                  (-70.832993931, -71.999890981, -73.187893012)),
    "upper-on": ((89.327115384, 89.912158409, 90.534302517),
                 (70.832993931, 71.999890981, 73.187893012)),
}
SECTIONS = ((7.9, .15, .328125 / .21875),
            (7.6, 1.390625, 0.),
            (7.3, .328125 * (.828125 - .7) / .203125, -.328125 / .203125))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def normal(face):
    a, b, c = face
    return cross(tuple(b[i] - a[i] for i in range(3)),
                 tuple(c[i] - a[i] for i in range(3)))


def covers(face, point):
    a, b, c = face
    u = tuple(b[i] - a[i] for i in range(3))
    v = tuple(c[i] - a[i] for i in range(3))
    w = tuple(point[i] - a[i] for i in range(3))
    n = cross(u, v)
    size = math.sqrt(dot(n, n))
    if size < 1e-10 or abs(dot(n, w)) > 2e-6 * size:
        return False
    uu, uv, vv, uw, vw = dot(u, u), dot(u, v), dot(v, v), dot(u, w), dot(v, w)
    denominator = uu * vv - uv * uv
    if denominator <= 1e-20:
        return False
    s = (uw * vv - vw * uv) / denominator
    t = (vw * uu - uw * uv) / denominator
    return min(s, t, 1. - s - t) >= -1e-6


class BarrierMiterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ramps = {ramp["id"]: ramp for ramp in geometry.compact_ramps()}
        cls.faces = {name: geometry.compact_ramp_triangles(ramp)
                     for name, ramp in cls.ramps.items()}

    def test_both_profile_crowns_face_upward(self):
        faces = geometry.road_triangles(
            [(0., -5., 15.), (0., 5., 15.)],
            edge_markings=False, barrier_profile=geometry.NATIVE_BARRIER_PROFILE)
        crowns = [face for face in faces
                  if all(abs(p[1] - 16.390625) < 1e-10 for p in face)]
        self.assertEqual(len(crowns), 4)
        self.assertTrue(all(normal(face)[1] > 0 for face in crowns))
        self.assertEqual({1 if face[0][0] > 0 else -1 for face in crowns}, {-1, 1})

    def test_both_barriers_close_outer_crown_and_inner_strip_at_every_mouth(self):
        for name, ramp in self.ramps.items():
            for barrier, positions in enumerate(WITNESSES[name]):
                for u, (v, height, slope) in zip(positions, SECTIONS):
                    with self.subTest(ramp=name, barrier=barrier, v=v):
                        east, north, elevation = geometry.world_coordinates(
                            u, ramp["side"] * v, ramp["height_m"] + height)
                        point = east, elevation, -north
                        matches = [face for face in self.faces[name] if covers(face, point)]
                        self.assertTrue(matches, point)
                        desired = (-ramp["side"] * slope / math.sqrt(2.), 1.,
                                   -ramp["side"] * slope / math.sqrt(2.))
                        self.assertTrue(any(dot(normal(face), desired) > 1e-10 for face in matches))

    def test_inward_overlap_stays_within_the_native_barrier_profile(self):
        for name, ramp in self.ramps.items():
            inward = [point for face in self.faces[name] for point in face
                      if abs((-point[2] - point[0] + 8.) / math.sqrt(2.)) < 8. - 1e-7]
            self.assertTrue(inward, name)
            for point in inward:
                v = abs((-point[2] - point[0] + 8.) / math.sqrt(2.))
                self.assertGreaterEqual(v, 7.171875 - 1e-7)
                self.assertGreaterEqual(point[1], ramp["height_m"] - 1e-7)
                self.assertLessEqual(point[1], ramp["height_m"] + 1.390625 + 1e-7)
                self.assertAlmostEqual(point[3], geometry.ATLAS_UV["concrete"][0])

    def test_temporary_inset_never_leaks_into_saved_vertex_coordinates(self):
        for name, faces in self.faces.items():
            self.assertTrue(all(len(point) == 5 and all(math.isfinite(v) for v in point)
                                for face in faces for point in face), name)
            # Packing each actual tile exercises the fixed XYZ/UV record size.
            for cell, tile_faces in geometry.partition_triangles(faces).items():
                geometry.pack_road_model(tile_faces, 0x5F900000)


if __name__ == "__main__":
    unittest.main()
