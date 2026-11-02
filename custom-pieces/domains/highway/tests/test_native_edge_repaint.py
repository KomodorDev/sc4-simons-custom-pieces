"""Keep old-edge paint erasure narrow and preserve the surrounding native UV field."""
from pathlib import Path
import math
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / "framework"), str(ROOT / "domains/highway/implementation")]

from scp_highway.ramp_geometry import compact_ramps
from scp_highway.slip_lanes import profile, shoulder_footprint, repaint_native_shoulder


def vertex(u, q, height, side):
    v = side * q
    east = 4. + (u - v) / math.sqrt(2.)
    south = 4. - (u + v) / math.sqrt(2.)
    return east, height, south, .5 - q / 16., 1. - u / 16.


def native_coordinates(point, side):
    east, _height, south = point[:3]
    return (east - south) / math.sqrt(2.), side * (-south - east + 8.) / math.sqrt(2.)


def area(polygon):
    return abs(sum(a[0] * b[2] - b[0] * a[2]
                   for a, b in zip(polygon, polygon[1:] + polygon[:1]))) / 2.


def upward(polygon):
    a, b, c = polygon[:3]
    return (b[2] - a[2]) * (c[0] - a[0]) - (b[0] - a[0]) * (c[2] - a[2])


class NativeEdgeRepaintTests(unittest.TestCase):
    def test_all_four_footprints_cover_only_the_measured_half_metre_paint_band(self):
        for ramp in compact_ramps():
            with self.subTest(ramp=ramp["id"]):
                footprints = shoulder_footprint(ramp)
                q_values = [ramp["side"] * (-south - east + 8.) / math.sqrt(2.)
                            for footprint in footprints for east, south in footprint]
                self.assertAlmostEqual(min(q_values), 4.3125, places=10)
                self.assertAlmostEqual(max(q_values), 4.8125, places=10)
                self.assertAlmostEqual(max(q_values) - min(q_values), .5, places=10)

    def test_surrounding_asphalt_and_longitudinal_texture_phase_are_preserved(self):
        for ramp in compact_ramps():
            data = profile(ramp)
            low, high = sorted((data["u0"] + data["direction"] * 5.,
                                data["u0"] + data["direction"] * 15.))
            polygon = [vertex(u, q, ramp["height_m"], ramp["side"])
                       for u, q in ((low, 3.), (high, 3.), (high, 7.), (low, 7.))]
            if upward(polygon) < 0:
                polygon.reverse()
            cuts = [(ramp["height_m"], ramp["side"], footprint)
                    for footprint in shoulder_footprint(ramp)]
            result = repaint_native_shoulder(polygon, cuts)
            changed = untouched = 0
            with self.subTest(ramp=ramp["id"]):
                for part in result:
                    for point in part:
                        u, q = native_coordinates(point, ramp["side"])
                        self.assertAlmostEqual(point[4], 1. - u / 16., places=11)
                        self.assertEqual(point[1], ramp["height_m"])
                        native_u = .5 - q / 16.
                        if abs(point[3] - native_u) > 1e-9:
                            changed += 1
                            self.assertGreaterEqual(q, 4.3125 - 1e-9)
                            self.assertLessEqual(q, 4.8125 + 1e-9)
                            self.assertAlmostEqual(point[3], 29.5 / 128., places=12)
                        elif q < 4.3125 - 1e-9 or q > 4.8125 + 1e-9:
                            untouched += 1
                self.assertGreater(changed, 0)
                self.assertGreater(untouched, 0)
                self.assertAlmostEqual(sum(area(part) for part in result), area(polygon), places=9)
                self.assertTrue(all(upward(part) >= -1e-10 for part in result))

    def test_inner_border_uses_its_original_native_asphalt_column(self):
        # The inner edge of the erased white band meets column 29's centre.
        self.assertEqual(.5 - 4.3125 / 16., 29.5 / 128.)
        # The untouched outer edge is column 25's centre.
        self.assertEqual(.5 - 4.8125 / 16., 25.5 / 128.)

    def test_unserved_height_and_unrelated_native_faces_stay_exact(self):
        ramp = compact_ramps()[0]
        data = profile(ramp)
        u = data["u0"] + data["direction"] * 10.
        polygon = [vertex(u + du, q, 15., ramp["side"])
                   for du, q in ((0., 3.), (1., 3.), (1., 7.), (0., 7.))]
        if upward(polygon) < 0:
            polygon.reverse()
        cuts = [(7.5, ramp["side"], footprint) for footprint in shoulder_footprint(ramp)]
        self.assertEqual(repaint_native_shoulder(polygon, cuts), [polygon])


if __name__ == "__main__":
    unittest.main()
