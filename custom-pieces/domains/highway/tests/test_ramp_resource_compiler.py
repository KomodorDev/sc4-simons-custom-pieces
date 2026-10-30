"""Verify real road resources, complete service envelopes, and traffic seams."""
from pathlib import Path
import math
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / "framework"), str(ROOT / "domains/highway/implementation")]

from scp.models import parse_s3d, positions, validate_s3d
from scp.track_paths import _parse_paths
from scp_highway import ramp_geometry as geometry
from scp_highway import ramp_paths as paths


def triangles(raw):
    model = parse_s3d(raw)
    for mesh in model["meshes"]:
        vi, ii, pi, _mi = mesh["frames"][0]
        block = model["vertices"][vi]
        points = [struct.unpack_from("<5f", block["data"], offset)
                  for offset in range(0, len(block["data"]), block["stride"])]
        indices = model["indices"][ii]["values"]
        for kind, first, count in model["primitives"][pi]:
            if kind != 0:
                raise AssertionError("Unexpected non-triangular primitive")
            for index in range(first, first + count, 3):
                yield tuple(points[i] for i in indices[index:index + 3])


class RampResourceCompilerTests(unittest.TestCase):
    def setUp(self):
        # Ends use real diagonal DD lane offsets and actual tile sides. This
        # synthetic transition tests the compiler; it claims no native turn.
        self.profile = geometry.sample_grade_curve(
            [(8.0, 3.2), (18.0, 13.2), (30.0, 9.2), (40.0, 19.2)],
            start_height=7.5, flat_start=5.0, flat_end=4.0, max_grade=0.4)

    def test_saved_paths_are_car_routes_with_exact_local_tile_seams(self):
        records = paths.slice_routes([{"id": "lower-off", "points": self.profile["points"]}])
        seams = {}
        for cell, routes in records.items():
            saved = _parse_paths(paths.encode_paths(routes))
            for route in saved:
                self.assertEqual(route["transport"], 1)
                for endpoint, side, label in ((route["points"][0], route["entry"], "entry"),
                                              (route["points"][-1], route["exit"], "exit")):
                    expected = ((-8.0, None), (None, 8.0), (8.0, None), (None, -8.0))[side]
                    for axis, value in enumerate(expected):
                        if value is not None:
                            self.assertAlmostEqual(endpoint[axis], value, places=8)
                    world = (endpoint[0] + 16 * cell[0], endpoint[1] - 16 * cell[1], endpoint[2])
                    seams.setdefault(tuple(round(value, 7) for value in world), []).append(label)
        self.assertEqual(sum(len(value) == 1 for value in seams.values()), 2)
        for labels in seams.values():
            if len(labels) == 2:
                self.assertCountEqual(labels, ["entry", "exit"])

    def test_full_width_and_barriers_participate_in_tile_ownership(self):
        centerline = [(0.0, -8.0, 7.5), (0.0, 8.0, 7.5)]
        # The spine stays in column zero; its 20 m deck crosses both sides.
        tiles = geometry.compile_road_tiles([{"points": centerline, "width": 20.0}], 0x5F900000)
        self.assertEqual(set(tiles), {(-1, 0), (0, 0), (1, 0)})
        for raw in tiles.values():
            model = parse_s3d(raw)
            self.assertTrue(validate_s3d(model)["all_vertex_positions_finite"])
            for block in model["vertices"]:
                for east, height, south in positions(block):
                    self.assertLessEqual(abs(east), 8.000001)
                    self.assertLessEqual(abs(south), 8.000001)
                    self.assertGreaterEqual(height, 6.9 - 1e-6)
                    self.assertLessEqual(height, 8.4 + 1e-6)

    def test_saved_road_has_an_actual_underside_and_raised_barriers(self):
        raw = geometry.compile_road_tiles(
            [{"points": [(0.0, -8.0, 7.5), (0.0, 8.0, 7.5)]}], 0x5F900000)[0, 0]
        heights = {round(point[1], 5) for block in parse_s3d(raw)["vertices"] for point in positions(block)}
        self.assertTrue({6.9, 7.5, 8.4}.issubset(heights))
        surfaces = {round(triangle[0][3], 4) for triangle in triangles(raw)}
        self.assertTrue({0.125, 0.375, 0.625}.issubset(surfaces))

    def test_saved_ground_landing_has_no_collapsed_concrete_barriers_and_keeps_graded_taper(self):
        concrete_u = geometry.ATLAS_UV['concrete'][0]
        for profile in (None, geometry.NATIVE_BARRIER_PROFILE):
            with self.subTest(profile=profile):
                raw = geometry.compile_road_tiles([{
                    'points': [(0., -8., 0.), (0., 8., 0.)],
                    'barrier_profile': profile}], 0x5F900000)[0, 0]
                self.assertFalse(any(all(abs(point[3] - concrete_u) < 1e-7 for point in face)
                                     for face in triangles(raw)))
        graded = geometry.compile_road_tiles([{
            'points': [(0., -8., .5), (0., 0., 0.), (0., 8., 0.)],
            'barrier_profile': geometry.NATIVE_BARRIER_PROFILE}], 0x5F900000)[0, 0]
        concrete = [face for face in triangles(graded)
                    if all(abs(point[3] - concrete_u) < 1e-7 for point in face)]
        self.assertTrue(any(min(point[1] for point in face) == 0.
                            and max(point[1] for point in face) > .5 for face in concrete))
        # South=-north: the final flat collar lies at negative model z.
        self.assertFalse(any(all(point[1] == 0. for point in face)
                             and min(point[2] for point in face) < -1e-7 for face in concrete))

    def test_pavement_height_follows_the_actual_saved_car_path(self):
        models = geometry.compile_road_tiles([{"points": self.profile["points"]}], 0x5F900000)
        records = paths.slice_routes([{"points": self.profile["points"]}])
        for cell, routes in records.items():
            road = [triangle for triangle in triangles(models[cell])
                    if all(abs(point[3] - geometry.ATLAS_UV["asphalt"][0]) < 1e-7 for point in triangle)]
            for route in routes:
                for x, y, height in route["points"][::17]:
                    found = False
                    for triangle in road:
                        a, b, c = triangle
                        determinant = (b[2] - c[2]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[2] - c[2])
                        if abs(determinant) < 1e-12:
                            continue
                        one = ((b[2] - c[2]) * (x - c[0]) + (c[0] - b[0]) * (-y - c[2])) / determinant
                        two = ((c[2] - a[2]) * (x - c[0]) + (a[0] - c[0]) * (-y - c[2])) / determinant
                        if min(one, two, 1 - one - two) >= -1e-5:
                            actual = one * a[1] + two * b[1] + (1 - one - two) * c[1]
                            if abs(actual - height) < 1e-4:
                                found = True
                                break
                    self.assertTrue(found, (cell, (x, y, height)))

    def test_rotations_retain_traffic_handedness_and_grade(self):
        original = self.profile["points"]
        for quarter in range(4):
            rotated = paths.rotate_points(original, quarter)
            restored = paths.rotate_points(rotated, -quarter)
            for first, last in zip(original, restored):
                self.assertLess(math.dist(first, last), 1e-9)
            self.assertEqual([point[2] for point in original], [point[2] for point in rotated])
            # Clockwise proper rotations preserve signed bend orientation.
            a, b, c = [rotated[index] for index in (0, 100, 200)]
            cross = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
            self.assertLess(cross, 0.0)

    def test_resource_has_no_rail_transport_or_unjoined_interior_endpoint(self):
        with self.assertRaisesRegex(ValueError, "unjoined interior"):
            paths.slice_routes([{"points": [(0.0, 0.0, 7.5), (8.0, 3.2, 7.5)]}])
        with self.assertRaisesRegex(ValueError, "car or pedestrian"):
            paths.slice_routes([{"transport": 7, "points": [(0.0, -8.0, 7.5), (0.0, 8.0, 7.5)]}])

    def test_grade_limit_rejects_a_shortcut_without_moving_its_native_anchors(self):
        controls = [(8.0, 3.2), (10.0, 5.2), (14.0, 7.2), (16.0, 9.2)]
        with self.assertRaisesRegex(ValueError, "insufficient length|needs.*grade"):
            geometry.sample_grade_curve(controls, start_height=7.5, flat_start=1.0, flat_end=1.0)
        self.assertEqual(self.profile["points"][0], (8.0, 3.2, 7.5))
        self.assertEqual(self.profile["points"][-1], (40.0, 19.2, 0.0))

    def test_junction_marking_covers_splits_and_merges_but_preserves_pedestrians(self):
        records = { (0, 0): [
            {"transport": 1, "points": [(0.0, -8.0, 7.5), (0.0, 8.0, 7.5)], "junction": False},
            {"transport": 1, "points": [(0.0, -8.0, 7.5), (8.0, 0.0, 7.5)], "junction": False},
            {"transport": 1, "points": [(-8.0, 0.0, 7.5), (0.0, 8.0, 7.5)], "junction": False},
            {"transport": 2, "points": [(0.0, -8.0, 7.5), (0.0, 8.0, 7.5)], "junction": False}]}
        updated = paths.mark_junctions(records)[0, 0]
        self.assertEqual([route["junction"] for route in updated], [True, True, True, False])

    def test_surface_atlas_is_a_complete_opaque_fsh_with_authored_colors(self):
        raw = geometry.create_surface_atlas()
        magic, size, count, directory, name, offset = struct.unpack_from("<4sII4s4sI", raw)
        self.assertEqual((magic, size, count, directory, name, offset),
                         (b"SHPI", len(raw), 1, b"GIMX", b"0000", 24))
        code, width, height = struct.unpack_from("<IHH", raw, offset)
        self.assertEqual((code & 255, width, height), (0x7D, 128, 128))
        self.assertEqual(set(raw[43::4]), {255})
        self.assertEqual(set(tuple(raw[start:start + 4]) for start in range(40, len(raw), 4)),
                         {(blue, green, red, alpha) for red, green, blue, alpha in geometry.COLORS})

    def test_compact_ramps_keep_native_high_ports_and_full_width_clearance(self):
        ramps = {ramp["id"]: ramp for ramp in geometry.compact_ramps()}
        self.assertEqual(ramps["lower-off"]["points"][0], (56.0, 51.2, 7.5))
        self.assertEqual(ramps["upper-off"]["points"][0], (-72.0, -83.2, 15.0))
        for ramp in ramps.values():
            expected = 69.98798604746474 if ramp["deck"] == "lower" else 101.9401344063455
            self.assertAlmostEqual(ramp["length_plan_m"], expected, places=7)
            self.assertLess(ramp["grade_max_percent"], 23.0 if ramp["deck"] == "lower" else 30.0)
            for point in ramp["points"]:
                if point[2] < ramp["height_m"] - 1e-7:
                    self.assertGreaterEqual(abs(geometry.highway_coordinates(point)[1]), 13.0 - 1e-7)

    def test_compact_surface_movements_join_real_lanes_without_interior_ends(self):
        movements = paths.compact_access_routes()
        self.assertEqual({movement["id"] for movement in movements}, {
            "lower-highway->NW", "NW->lower-highway", "upper-highway->SE", "SE->upper-highway"})
        lanes = (11.2, -11.2)
        for movement in movements:
            port = movement["avenue_port"]
            self.assertTrue(any(abs(port[0] + port[1] - lane) < 1e-7 for lane in lanes))
            self.assertEqual(port[2], 0.0)
            points = movement["surface_points"]
            # A geometric right turn has a negative planar cross product.
            incoming = (points[1][0] - points[0][0], points[1][1] - points[0][1])
            outgoing = (points[-1][0] - points[-2][0], points[-1][1] - points[-2][1])
            self.assertLess(incoming[0] * outgoing[1] - incoming[1] * outgoing[0], 0.0)
            lateral = [geometry.highway_coordinates(point)[0] for point in points]
            self.assertTrue(all(value > 0. for value in lateral) or all(value < 0. for value in lateral))
        for routes in paths.slice_routes(movements).values():
            self.assertTrue(all(route["entry"] != 255 and route["exit"] != 255 for route in routes))

    def test_module_ownership_is_sparse_unique_and_reuses_native_continuations(self):
        catalog = paths.module_catalog()
        self.assertEqual(len(catalog["types"]), 13)
        self.assertEqual(len(catalog["placements"]), 15)
        self.assertEqual(len(catalog["occupied_cells"]), 53)
        self.assertEqual(catalog["footprint"], [10, 10])
        self.assertEqual(catalog["world_grid_origin"], [-4, -4])
        self.assertEqual(len({tuple(item["cell"]) for item in catalog["cell_owners"]}), 53)
        self.assertEqual(len({item["recipe"] for item in catalog["types"]}), 13)
        self.assertEqual(sum(len(item["cells"]) for item in catalog["types"]), 51)
        self.assertLess(max(len(item["cells"]) for item in catalog["types"]), 9)
        self.assertEqual(sum(len(item["engineering"]["model_only_cells"]) for item in catalog["types"]), 6)
        self.assertEqual({item["engineering"]["max_grade_percent"] for item in catalog["types"]}, {30.0})
        paths._procedural_geometry()

    def test_lower_branch_opening_preserves_the_upper_deck_and_opposing_barrier(self):
        ramp = next(item for item in geometry.compact_ramps() if item["id"] == "lower-off")
        nearest = min(ramp["points"], key=lambda point: abs(geometry.highway_coordinates(point)[1] - 8.0))
        station = geometry.highway_coordinates(nearest)[0]
        changed = []
        for height in (7.5, 15.0):
            road = {"points": [geometry.world_coordinates(station - 4., 0., height),
                               geometry.world_coordinates(station + 4., 0., height)],
                    "width": 16.0, "thickness": 1.0, "barrier_profile": geometry.NATIVE_BARRIER_PROFILE,
                    "edge_markings": False}
            for cell, raw in geometry.compile_road_tiles([road], 0x5F900000).items():
                opened, report = geometry.cut_native_branch_openings(raw, cell, [ramp])
                if height == 15.0:
                    self.assertEqual(opened, raw)
                    self.assertFalse(report["changed"])
                else:
                    changed.append(report["changed"])
                    # The branch owns only its right-side barrier: every
                    # opposite-side upper-height barrier vertex remains.
                    def opposite_faces(payload):
                        return {tuple(tuple(round(value, 5) for value in vertex) for vertex in face)
                                for face in triangles(payload)
                                if min(vertex[1] for vertex in face) >= height - 1e-5
                                and max(vertex[1] for vertex in face) > height + 1e-5
                                and all(geometry.highway_coordinates((vertex[0] + 16 * cell[0],
                                          -vertex[2] - 16 * cell[1]))[1] < -6.8 for vertex in face)}
                    self.assertEqual(opposite_faces(opened), opposite_faces(raw))
        self.assertTrue(any(changed))

    def test_explicit_model_only_cells_encode_native_zero_route_header(self):
        self.assertEqual(paths.encode_paths([], allow_empty=True), b"SC4PATHS\r\n1.2\r\n0\r\n0\r\n0\r\n")
        with self.assertRaisesRegex(ValueError, "at least one"):
            paths.encode_paths([])

    def test_intersecting_ground_aprons_remain_closed_after_float32_encoding(self):
        from scp_highway import ramp_verify
        # Preserve the historical intersecting-apron regression as a generic
        # geometry fixture. These opposing turns are no longer permitted
        # movements in the actual right-turn-only assembly.
        junction, outer = 20. * math.sqrt(2.), 11.2 / math.sqrt(2.)
        turns = (paths._surface_turn((12., junction), (-outer, junction - 18.), (-1, 0), (0, -1)),
                 paths._surface_turn((outer, junction - 18.), (-12., junction), (0, 1), (-1, 0)))
        source = [triangle for turn in turns for triangle in geometry.road_triangles(
            [geometry.world_coordinates(u, v) for u, v in turn], width=3.5, barriers=False, edge_markings=False)]
        united = geometry.union_ground_pavement(source)
        faces = []
        for cell, local in geometry.partition_triangles(united).items():
            raw = geometry.pack_road_model(local, 0x5F900000)
            faces.extend(ramp_verify._triangles(raw, cell))
        # This exact saved-path interval previously followed a skinny union
        # edge whose separately rounded float32 vertices created a hairline
        # gap. The replacement apron covers the entire interval strictly.
        first = (-13.680185161, 8.0, 0.0)
        last = (-13.67138115, 7.906665644, 0.0)
        self.assertTrue(ramp_verify._covered(first, last, faces))
        for face in faces:
            for east, north, height in face["points"]:
                self.assertEqual(height, 0.0)
                self.assertEqual(east * 16.0, round(east * 16.0))
                self.assertEqual(north * 16.0, round(north * 16.0))

    def test_centre_pier_reaches_true_native_planes_without_coplanar_caps(self):
        faces = geometry.support_triangles()
        self.assertEqual(len(faces), 8)
        for face in faces:
            self.assertEqual({point[1] for point in face}, {0.0, 15.0})
            self.assertTrue(all(abs(point[0]) <= 0.4 and abs(point[2]) <= 0.4 for point in face))
            self.assertTrue(all(point[3:] == geometry.ATLAS_UV["concrete"] for point in face))
        # Native lane lines in the two complementary halves are x-y=
        # +/-4.8 and +/-11.2. Even the nearest channel stays outside the
        # 1.25 m car half-width plus the square pier's transverse projection.
        closest_lane_distance = 4.8 / math.sqrt(2.0)
        pier_projection = 0.4 * math.sqrt(2.0)
        self.assertGreater(closest_lane_distance - pier_projection, 1.25)


if __name__ == "__main__":
    unittest.main()
