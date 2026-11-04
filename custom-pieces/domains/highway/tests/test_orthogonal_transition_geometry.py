"""Focused engineering controls for the approved six-tile transition."""
from collections import Counter
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / "framework"), str(ROOT / "domains/highway/implementation")]
from scp_highway import orthogonal_transition as writer
from scp_highway import orthogonal_transition_geometry as geometry
from scp_highway import ramp_paths
from scp_highway import ramp_geometry


class OrthogonalTransitionGeometryTests(unittest.TestCase):
    def test_six_tile_bounds_and_native_axis_assignment(self):
        self.assertEqual(geometry.CELLS, tuple((x, z) for z in range(6) for x in range(2)))
        self.assertEqual(geometry.LENGTH, 96.0)
        for station in (0.0, 1.0, 3.0):
            self.assertEqual(geometry.lane_point("upper", 0, station), (13.5, 8.0 - station, 15.0))
            self.assertEqual(geometry.lane_point("lower", 0, station), (18.5, 8.0 - station, 7.5))
        for station in (93.0, 94.0, 96.0):
            self.assertEqual(geometry.lane_point("upper", 0, station), (-2.5, 8.0 - station, 0.0))
            self.assertEqual(geometry.lane_point("lower", 0, station), (18.5, 8.0 - station, 0.0))

    def test_both_lowering_and_spreading_happen_in_the_same_run(self):
        middle = 36.0
        self.assertAlmostEqual(geometry.upper_plan(middle)[0], 8.0, places=12)
        self.assertAlmostEqual(geometry.height("lower", middle), 3.75, places=12)
        self.assertLess(geometry.height("upper", middle), 15.0)
        self.assertGreater(geometry.height("upper", middle), geometry.height("lower", middle))
        self.assertEqual(geometry.upper_plan(69.0), (0.0, 0.0, 0.0))
        self.assertEqual(geometry.height("lower", 69.0), 0.0)
        self.assertGreater(geometry.height("upper", 69.0), 3.0)

    def test_six_tile_actual_lane_grades_remain_below_the_reviewed_limits(self):
        peaks = {}
        for deck in ("upper", "lower"):
            peaks[deck] = 0.0
            for lane in (0, 1):
                points = [geometry.lane_point(deck, lane, s) for s in geometry.STATIONS]
                for first, last in zip(points, points[1:]):
                    grade = abs(last[2] - first[2]) / math.dist(first[:2], last[:2])
                    peaks[deck] = max(peaks[deck], grade)
        self.assertLess(peaks["upper"], 0.20)
        self.assertLess(peaks["lower"], 0.18)
        self.assertLessEqual(peaks["upper"], geometry.normalized_upper_grade() + 3e-5)
        self.assertLessEqual(peaks["lower"], 7.5 * 1.5 / 66.0)
        self.assertGreater(peaks["upper"], 0.19)
        self.assertGreater(peaks["lower"], 0.17)

    def test_cross_sections_are_horizontal_and_normal_to_the_curved_axis(self):
        for station in (12.0, 28.0, 36.0, 52.0, 68.0):
            first = geometry.model_point("upper", station, -8.0)
            last = geometry.model_point("upper", station, 8.0)
            self.assertEqual(first[1], last[1])
            self.assertAlmostEqual(math.dist(first, last), 16.0, places=12)
            derivative = geometry.upper_plan(station)[1]
            self.assertAlmostEqual((last[0] - first[0]) * derivative + last[2] - first[2], 0.0, places=12)

    def test_only_one_owned_cell_is_model_only(self):
        sliced = ramp_paths.slice_routes(geometry.traffic_routes())
        self.assertEqual(set(geometry.CELLS) - set(sliced), {(0, 0)})
        self.assertEqual(geometry.MODEL_ONLY_CELLS, ((0, 0),))
        self.assertEqual(len(sliced[0, 1]), 1)
        self.assertTrue(set(sliced) <= set(geometry.CELLS))

    def test_single_global_cut_preserves_every_complete_directed_lane(self):
        original = geometry.traffic_routes()
        self.assertEqual(len(original), 4)
        self.assertEqual({r["transport"] for r in original}, {1})
        for route in original:
            fragments = ramp_paths.polyline_fragments(route["points"])
            restored = []
            for (x, row), points in fragments:
                world = [(p[0] + 16.0 * x, p[1] - 16.0 * row, p[2]) for p in points]
                if restored:
                    self.assertLess(math.dist(restored[-1], world[0]), 2e-10)
                    world = world[1:]
                restored.extend(world)
            self.assertLess(math.dist(restored[0], route["points"][0]), 2e-10)
            self.assertLess(math.dist(restored[-1], route["points"][-1]), 2e-10)
            before = sum(math.dist(a, b) for a, b in zip(route["points"], route["points"][1:]))
            after = sum(math.dist(a, b) for a, b in zip(restored, restored[1:]))
            self.assertAlmostEqual(before, after, places=9)

    def test_path_elevation_is_explicit_even_for_the_empty_model_owner(self):
        sliced = ramp_paths.slice_routes(geometry.traffic_routes())
        for cell in geometry.CELLS:
            routes = sliced.get(cell, [])
            lines = writer._encode_paths(routes).decode("ascii").splitlines()
            self.assertEqual(lines[:5], ["SC4PATHS", "1.2", str(len(routes)), "0", "1"])

    def test_native_datum_is_retained_then_reaches_exact_ground(self):
        for deck in ("upper", "lower"):
            self.assertEqual(writer.pavement_datum(deck, 0.0), writer.DATUM[deck])
            self.assertEqual(writer.pavement_bounds(deck, 0.0), (writer.DD_MIN, writer.DD_MAX))
            self.assertEqual(writer.pavement_datum(deck, 96.0), 0.0)
            self.assertEqual(writer.pavement_bounds(deck, 96.0), (-8.0, 8.0))
            values = [writer.pavement_datum(deck, s) for s in geometry.STATIONS]
            self.assertTrue(all(a >= b >= 0.0 for a, b in zip(values, values[1:])))

    def test_native_materials_cover_the_flat_external_collars(self):
        self.assertEqual(writer._role("upper", 0.0, 3.0), "native-dd")
        self.assertEqual(writer._role("lower", 0.0, 3.0), "native-dd")
        self.assertEqual(writer._role("upper", 3.0, 3.25), "atlas")
        self.assertEqual(writer._role("lower", 69.0, 69.25), "native-ground")
        self.assertEqual(writer._role("upper", 93.0, 96.0), "native-ground")
        self.assertEqual(writer._source_uv("upper", 96.0, -8.0, native_dd=False), (0.0, 6.0))
        self.assertEqual(writer._source_uv("lower", 96.0, -8.0, native_dd=False), (1.0, -5.0))

    def test_elevated_shoulders_do_not_expose_the_underdeck_during_colour_blending(self):
        for deck in ("upper", "lower"):
            colours = []
            for station in geometry.STATIONS:
                colour, alpha = writer.appearance_blend(deck, station)
                self.assertGreaterEqual(colour, 0.0)
                self.assertLessEqual(colour, 1.0)
                self.assertGreaterEqual(alpha, 0.0)
                self.assertLessEqual(alpha, 1.0)
                if geometry.height(deck, station) >= 0.25:
                    self.assertEqual(alpha, 0.0)
                colours.append(colour)
            self.assertTrue(all(a <= b for a, b in zip(colours, colours[1:])))
            self.assertEqual(writer.appearance_blend(deck, 0.0), (0.0, 0.0))
            self.assertEqual(writer.appearance_blend(deck, 96.0), (1.0, 1.0))

    def test_supports_are_closed_complete_solids(self):
        records = writer.support_specifications()
        painter = type("Roles", (), {"roles": tuple(r["id"] for r in records)})()
        self.assertEqual(len(records), 14)
        for record in records:
            faces = writer._support_box(record, painter)
            self.assertEqual(len(faces), 12)
            edges = Counter()
            for triangle in faces:
                points = [tuple(round(v, 10) for v in p[:3]) for p in triangle]
                for first, last in zip(points, points[1:] + points[:1]):
                    edges[tuple(sorted((first, last)))] += 1
            self.assertEqual(set(edges.values()), {2}, record["id"])

    def test_upper_columns_stay_outside_the_complete_lower_road_slab(self):
        records = writer.support_specifications()
        painter = type("Roles", (), {"roles": tuple(r["id"] for r in records)})()
        for record in records:
            if not record["id"].startswith("upper-pier"):
                continue
            faces = writer._support_box(record, painter)
            self.assertLess(max(p[0] for tri in faces for p in tri), 8.0)
        first = next(r for r in records if r["id"] == "upper-pier-12")
        self.assertEqual(first["lateral_range_m"], [-9.6, -8.799999999999999])

    def test_fading_native_overhang_cannot_extrapolate_a_landing_strip(self):
        first, last = 92.5, 92.75
        low, high = writer.pavement_bounds("upper", first)
        _low_last, high_last = writer.pavement_bounds("upper", last)
        triangle = ((low, 0.0, first - 8.0, 0.0, 0.0, 0.0),
                    (high, 0.0, first - 8.0, 1.0, 0.0, 0.0),
                    (high_last, 0.0, last - 8.0, 1.0, 1.0, 0.0))
        historical = ramp_geometry.partition_triangles([triangle])
        old_maximum = max(p[2] + cell[1] * 16.0
                          for cell, faces in historical.items() for face in faces for p in face)
        self.assertGreater(old_maximum, last - 8.0 + 0.01)
        corrected = writer.partition_triangles([triangle])
        self.assertTrue(corrected)
        for cell, faces in corrected.items():
            for face in faces:
                for p in face:
                    self.assertGreaterEqual(p[2] + cell[1] * 16.0, first - 8.0 - 1e-9)
                    self.assertLessEqual(p[2] + cell[1] * 16.0, last - 8.0 + 1e-9)
                    self.assertTrue(all(-1e-9 <= v <= 1.0 + 1e-9 for v in p[3:5]))

    def test_exact_half_space_clipping_discards_fuzzy_outside_vertices(self):
        polygon = [(8.0 + 1.1e-8, 0.0, 0.0, 0.0, 0.0, 0.0),
                   (8.0 + 1.4e-9, 0.0, 0.25, 1.0, 1.0, 0.0),
                   (8.0 + 1.4e-9, 1.0, 0.25, 1.0, 1.0, 0.0)]
        self.assertEqual(writer._clip_plane(polygon, 0, 8.0, -1.0), [])

    def test_mirrored_decks_keep_native_heights_and_opposite_direction_sockets(self):
        routes = {route["id"]: route for route in geometry.traffic_routes(variant="mirrored")}
        self.assertEqual(routes["upper-lane-0"]["points"][0], (18.5, -88.0, 0.0))
        self.assertEqual(routes["upper-lane-0"]["points"][-1], (2.5, 8.0, 15.0))
        self.assertEqual(routes["lower-lane-0"]["points"][0], (-2.5, 8.0, 7.5))
        self.assertEqual(routes["lower-lane-0"]["points"][-1], (-2.5, -88.0, 0.0))
        self.assertEqual({route["lane"] for route in routes.values()}, {0, 1})

    def test_mirrored_paths_reflect_and_reverse_all_four_complete_lanes(self):
        original = geometry.traffic_routes()
        mirrored = geometry.traffic_routes(variant="mirrored")
        for first, second in zip(original, mirrored):
            self.assertEqual({k: v for k, v in first.items() if k != "points"},
                             {k: v for k, v in second.items() if k != "points"})
            for a, b in zip(reversed(first["points"]), second["points"]):
                self.assertAlmostEqual(b[0], 16.0 - a[0], places=12)
                self.assertEqual(b[1:], a[1:])
        sliced = ramp_paths.slice_routes(mirrored)
        self.assertEqual(set(geometry.CELLS) - set(sliced), {(1, 0)})
        self.assertEqual(geometry.model_only_cells(variant="mirrored"), ((1, 0),))
        self.assertTrue(set(sliced) <= set(geometry.CELLS))

    def test_mirrored_sections_reflect_the_entire_width_with_unchanged_grades(self):
        for deck in ("upper", "lower"):
            for station in (0., 12., 36., 52., 69., 96.):
                for lateral in (-8., -2.5, 2.5, 8.):
                    original = geometry.model_point(deck, station, lateral)
                    mirrored = geometry.model_point(deck, station, lateral, variant="mirrored")
                    self.assertAlmostEqual(mirrored[0], 16. - original[0], places=12)
                    self.assertEqual(mirrored[1:], original[1:])
        for station in (0., 12., 36., 52., 96.):
            x, first, second = geometry.upper_plan(station)
            self.assertEqual(geometry.upper_plan(station, variant="mirrored"), (16.-x, -first, -second))

    def test_reflected_faces_reverse_winding_and_keep_their_material_role(self):
        triangle = ((0., 3., 0., .1, .2, 4.), (0., 3., 2., .3, .4, 4.),
                    (2., 3., 0., .5, .6, 4.))
        reflected, = writer.reflect_triangles([triangle])
        self.assertGreater(ramp_geometry._normal(triangle)[1], 0.)
        self.assertGreater(ramp_geometry._normal(reflected)[1], 0.)
        for original, actual in zip((triangle[0], triangle[2], triangle[1]), reflected):
            self.assertEqual(actual, (16.-original[0], *original[1:]))
        self.assertEqual(writer.reflect_triangles([reflected]), [triangle])

    def test_reflected_complete_support_solids_remain_closed_and_outward(self):
        records = writer.support_specifications()
        painter = type("Roles", (), {"roles": tuple(r["id"] for r in records)})()
        for record in records:
            source = writer._support_box(record, painter)
            reflected = writer.reflect_triangles(source)
            center = tuple(sum(p[i] for triangle in reflected for p in triangle) / 36. for i in range(3))
            edges = Counter()
            for triangle in reflected:
                points = [tuple(round(v, 10) for v in p[:3]) for p in triangle]
                outward = tuple(sum(p[i] for p in points) / 3. - center[i] for i in range(3))
                normal = ramp_geometry._normal(points)
                self.assertGreater(sum(a*b for a, b in zip(normal, outward)), 0.)
                for first, last in zip(points, points[1:] + points[:1]):
                    edges[tuple(sorted((first, last)))] += 1
            self.assertEqual(set(edges.values()), {2}, record["id"])

    def test_mirrored_native_asphalt_phases_match_actual_rotated_donor_frames(self):
        for station in (0., 1., 3., 69., 93., 96.):
            for deck in ("upper", "lower"):
                for native_dd in (False, True):
                    u, v = writer._source_uv(deck, station, -2.5, native_dd=native_dd,
                                             variant="mirrored")
                    if native_dd:
                        expected_u = (-2.5 - writer.DD_MIN) / writer.DD_WIDTH
                        expected_v = (16. - station - writer.DD_OFFSET) / writer.DD_WIDTH
                    else:
                        expected_u, expected_v = 5.5 / 16., (16. - station) / 16.
                    if deck == "lower":
                        expected_u, expected_v = 1.-expected_u, 1.-expected_v
                    self.assertEqual((u, v), (expected_u, expected_v))
        original = writer._source_uv("upper", 0., 0., native_dd=True)
        reflected = writer._source_uv("upper", 0., 0., native_dd=True, variant="mirrored")
        self.assertEqual(original[0], reflected[0])
        self.assertGreater(abs(reflected[1] - (1.-original[1])), 1e-5)

    def test_mirrored_metadata_is_explicit_and_default_original_calls_are_unchanged(self):
        self.assertEqual(geometry.traffic_routes(), geometry.traffic_routes(variant="original"))
        self.assertEqual(writer.engineering_metadata(), writer.engineering_metadata(variant="original"))
        original, mirrored = writer.engineering_metadata(), writer.engineering_metadata(variant="mirrored")
        self.assertNotIn("transition_variant", original)
        self.assertEqual(mirrored["transition_variant"], "mirrored")
        self.assertEqual(mirrored["model_only_cells"], [[1, 0]])
        self.assertEqual(mirrored["native_dd_pose"], 2)
        self.assertEqual((mirrored["native_ground_upper_pose"], mirrored["native_ground_lower_pose"]), (2, 0))
        self.assertEqual(mirrored["upper_normalized_grade"], original["upper_normalized_grade"])
        self.assertEqual(mirrored["shadow_policy"], "disabled")

    def test_unknown_variants_fail_before_build_inputs_are_read(self):
        for variant in (None, True, False, "standard", "", "reflected"):
            for action in (lambda: geometry.traffic_routes(variant=variant),
                           lambda: geometry.engineering_metadata(variant=variant),
                           lambda: writer.build_channels({}, texture_id=1, variant=variant),
                           lambda: writer.build_textures({}, 1, variant=variant)):
                with self.subTest(variant=variant), self.assertRaisesRegex(ValueError, "variant"):
                    action()


if __name__ == "__main__":
    unittest.main()
