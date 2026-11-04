"""Portable controls for the reversed-only physical and texture hooks."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import numpy as np
from shapely.geometry import Point, Polygon, box

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "framework"))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp_highway import y_junction_geometry as original
from scp_highway import y_junction_reversed_geometry as reversed_geometry


class Painter:
    def role(self, name):
        if name != "body":
            raise AssertionError(name)
        return 0


class ReversedGeometryControls(unittest.TestCase):
    def test_city_partition_keeps_the_measured_small_raised_closing_triangle(self):
        # This actual45micrometre edge closed in the world, but its tiny
        # adjacent raised triangle was dropped by the historical cell cutter.
        enh = [(-1.5380060809651073, 18.675695129249878, 7.877330651503257),
               (-1.5380492307747462, 18.67570781082301, 7.877326106141737),
               (-1.5380754384707882, 18.675618487471652, 7.877476480165829)]
        triangle = tuple(original._vertex(e, n, h, (.2, .4), 2) for e, n, h in enh)
        self.assertEqual(original.orthogonal_transition.partition_triangles([triangle]), {})
        actual = reversed_geometry._partition_coherent_triangles([triangle])
        self.assertEqual(set(actual), {(0, -1)})
        self.assertEqual(len(actual[0, -1]), 1)
        world = tuple((p[0], p[1], p[2] - 16., *p[3:]) for p in actual[0, -1][0])
        self.assertEqual(world, triangle)

    def test_city_partition_retains_a_small_positive_fragment_at_a_tile_cut(self):
        triangle = tuple(original._vertex(e, n, 8., (e / 16., n / 16.), 0)
                         for e, n in ((7., 0.), (8.00001, 0.), (7., 1.)))
        actual = reversed_geometry._partition_coherent_triangles([triangle])
        self.assertEqual(set(actual), {(0, 0), (1, 0)})
        positive = actual[1, 0]
        self.assertEqual(len(positive), 1)
        self.assertGreater(Polygon([(p[0], -p[2]) for p in positive[0]]).area, 0.)
        area = sum(Polygon([(p[0], -p[2]) for p in face]).area
                   for faces in actual.values() for face in faces)
        self.assertAlmostEqual(area, Polygon([(p[0], -p[2]) for p in triangle]).area, places=14)

    def test_body_plane_intersection_keeps_a_nonzero_submicrometre_corner(self):
        footprint = Polygon([(0., 0.), (1e-6, 0.), (0., .4e-6)])
        height, uv = lambda point: 7.501, lambda point: (.5, 0.)
        self.assertEqual(original._triangulate_surface(footprint, height, 0, uv), [])
        actual = reversed_geometry._coherent_top_surface(footprint, height, 0, uv)
        self.assertEqual(len(actual), 1)
        retained = Polygon([(p[0], -p[2]) for p in actual[0]])
        self.assertAlmostEqual(retained.area, footprint.area, places=25)
        self.assertEqual(reversed_geometry._supported_top_crop(footprint, retained), 0.)

    def test_top_crop_uses_a_finite_distance_bound_including_corners(self):
        desired = box(0., 0., 1., 1.)
        area = reversed_geometry._supported_top_crop(desired, box(0., 0., 1. - .5e-9, 1.))
        self.assertAlmostEqual(area, .5e-9, places=15)
        with self.assertRaisesRegex(ValueError, "finite1nm"):
            reversed_geometry._supported_top_crop(desired, box(0., 0., 1. - 2e-9, 1.))
        # Each axis is less than1nm, but the finite corner's Euclidean
        # displacement exceeds1nm and must still be rejected.
        with self.assertRaisesRegex(ValueError, "finite1nm"):
            reversed_geometry._supported_top_crop(desired, box(0., 0., 1. - .8e-9, 1. - .8e-9))

    def test_curved_graded_top_uses_unchanged_wide_body_planes(self):
        class GradedPainter:
            roles = ["pavement", "body", "barrier"]

            def __init__(self):
                self.graded_end_windows = {}
                self.marking_fields = {}

            def role(self, name):
                return self.roles.index(name)

        points = np.array([(0., 0., 7.5), (4., 0., 8.), (8., 1., 9.)])
        station, normals = original._frame(points)
        road = {"id": "B-C", "points": points, "station": station, "normals": normals,
                "full_length": float(station[-1]), "rail_low": points[:, :2] - 3. * normals,
                "rail_high": points[:, :2] + 3. * normals,
                "inward_low": normals, "inward_high": -normals}
        previous = original._graded_faces([road], GradedPainter(), reverse_traffic=True)
        actual = reversed_geometry._graded_faces([road], GradedPainter(), [])
        body = lambda faces: [face for face in faces if round(face[0][5]) == 1]
        self.assertEqual(body(actual), body(previous))
        floors = []
        for face in body(actual):
            points3 = np.asarray(face)[:, :3]
            if np.cross(points3[1] - points3[0], points3[2] - points3[0])[1] >= -1e-12:
                continue
            xy = [(p[0], -p[2]) for p in face]
            from shapely.geometry import Polygon
            floors.append((Polygon(xy), np.linalg.solve(np.array([[*p, 1.] for p in xy]),
                                                        np.array([p[1] for p in face]))))
        roofs = [face for face in actual if round(face[0][5]) == 0]
        self.assertTrue(roofs)
        for face in roofs:
            q = np.mean(np.array([[p[0], -p[2]] for p in face]), axis=0)
            height = sum(p[1] for p in face) / 3.
            candidates = [height - float(np.r_[q, 1.] @ field)
                          for polygon, field in floors if polygon.buffer(2e-9).covers(Point(q))]
            self.assertTrue(candidates)
            self.assertLess(min(abs(value - 1.) for value in candidates), 1e-8)

    def test_full_width_fan_reaches_the_actual_shifted_C_native_inner_ring(self):
        class EmptyNativeRuns:
            @staticmethod
            def reserved_native_cells(_steps):
                return {"A": [], "B": [], "C": []}

        north = 7.999000072479248
        south = -8.00100040435791
        profiles = {("C", "upper"): {"width": north - south,
                    "centre": np.array([56., (north + south) / 2.])}}
        inner = 52.99899959564209
        point = Point(inner, north - 1e-8)
        default = original._unions(profiles, construction_routes=[], native_source=EmptyNativeRuns)
        actual = original._unions(profiles, construction_routes=[], native_source=EmptyNativeRuns,
                                   full_width_stations={"C": 56. - inner})
        self.assertFalse(default[0]["upper"].covers(point))
        self.assertTrue(actual[0]["upper"].covers(point))

    def test_opposing_texture_field_keeps_exact_native_domains(self):
        native_uv = lambda point: (point[0] / 16., point[1] / 16.)
        route_uv = lambda point: (.5 + point[1] / 16., point[0] / 16.)
        native = {"geometry": box(0, 0, 1, 1), "owner": "native-A",
                  "material_role": "pavement-native-A-upper", "uv": native_uv, "frame": {"native_arm": "A"}}
        ribbon = {"geometry": box(1, 0, 2, 1), "owner": "A-B",
                  "material_role": "pavement", "uv": route_uv, "frame": {"route": "A-B"}}
        with patch.object(original, "flat_surface_domains", return_value=[native, ribbon]):
            actual = reversed_geometry._surface_domains(box(0, 0, 2, 1),
                [{"id": "A-B", "station": [0., 32.]}], "upper", {}, [])
        self.assertIs(actual[0], native)
        self.assertIs(actual[0]["uv"], native_uv)
        self.assertEqual(actual[1]["uv"]((8., 2.)), (.375, 1.5))
        self.assertEqual(actual[1]["frame"]["directed_route"], "B-A")
        self.assertIs(ribbon["uv"], route_uv)

    def test_nominal_collar_has_a_full_metre_and_closed_internal_bottom_step(self):
        roof = 15.00100040435791
        patches = [{"geometry": box(0, 0, 1, 1), "height": 15.}]
        faces = reversed_geometry._underside_faces(box(0, 0, 2, 1), patches, roof, Painter())
        areas = {14.: 0., roof - 1.: 0.}
        step_area = 0.
        for face in faces:
            a, b, c = np.asarray(face)[:, :3]
            normal = np.cross(b - a, c - a)
            area = float(np.linalg.norm(normal)) / 2.
            if max(p[1] for p in face) - min(p[1] for p in face) < 1e-12:
                self.assertLess(normal[1], 0.)
                areas[face[0][1]] += area
            else:
                self.assertTrue(all(abs(p[0] - 1.) < 1e-12 for p in face))
                self.assertGreater(normal[0], 0.)
                step_area += area
        self.assertAlmostEqual(areas[14.], 1.)
        self.assertAlmostEqual(areas[roof - 1.], 1.)
        self.assertAlmostEqual(step_area, roof - 15., places=12)

    def test_no_extra_bottom_step_when_the_source_roof_matches_the_generic_roof(self):
        roof = 15.00100040435791
        faces = reversed_geometry._underside_faces(box(0, 0, 2, 1),
            [{"geometry": box(0, 0, 1, 1), "height": roof}], roof, Painter())
        self.assertTrue(faces)
        self.assertTrue(all(all(p[1] == roof - 1. for p in face) for face in faces))

    def test_bottom_step_owns_only_the_finite_adjacent_boundary_interval(self):
        roof = 15.00100040435791
        polygon = box(0, 0, 1, 1).union(box(1, 0, 2, .5))
        faces = reversed_geometry._underside_faces(polygon,
            [{"geometry": box(0, 0, 1, 1), "height": 15.}], roof, Painter())
        vertical = [face for face in faces if max(p[1] for p in face) - min(p[1] for p in face) > 1e-12]
        self.assertTrue(vertical)
        for face in vertical:
            # Model Z is south, so northY0..0.5 becomes Z-0.5..0.
            self.assertTrue(all(abs(p[0] - 1.) < 1e-12 and -.5 <= p[2] <= 0. for p in face))
        area = sum(float(np.linalg.norm(np.cross(np.asarray(face[1][:3]) - face[0][:3],
                    np.asarray(face[2][:3]) - face[0][:3]))) / 2 for face in vertical)
        self.assertAlmostEqual(area, .5 * (roof - 15.), places=12)

    def test_native_decimal_residue_cannot_create_a_one_millimetre_exterior_wall(self):
        roof = 15.00100040435791
        # The flat union is on the declared1nm grid; the source mask's raw
        # decimal falls0.1nm short. A1mm wall on that unrepresentable strip
        # would duplicate the genuine road outer wall after float32 packing.
        faces = reversed_geometry._underside_faces(box(0, 0, 1, 1),
            [{"geometry": box(0, 0, 1. - 1e-10, 1), "height": 15.}], roof, Painter())
        self.assertTrue(faces)
        self.assertTrue(all(all(p[1] == 14. for p in face) for face in faces))


if __name__ == "__main__":
    unittest.main()
