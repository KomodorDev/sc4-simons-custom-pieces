"""Check useful geometric and traffic limits of the unregistered highway study."""

import copy
import importlib.util
import math
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "diagonal_diamond_geometry.py"
SPEC = importlib.util.spec_from_file_location("diagonal_diamond_geometry", MODULE_PATH)
GEOMETRY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GEOMETRY)


class DiagonalDiamondGeometryTests(unittest.TestCase):
    def setUp(self):
        self.design = {"geometry": dict(GEOMETRY.DEFAULTS)}
        self.result = GEOMETRY.build_geometry(self.design)

    def test_upper_ramps_keep_full_height_until_the_whole_width_clears_lower_deck(self):
        parameters = self.result["metadata"]["parameters"]
        for route in self.result["routes"]:
            if route["id"] not in ("upper-off", "upper-on"):
                continue
            for east, north, height in route["points"]:
                lateral_position = abs((north - east) / math.sqrt(2))
                if height < 15 - 1e-8:
                    nearest_ramp_edge = lateral_position - parameters["ramp_width_m"] / 2
                    required_edge = parameters["highway_width_m"] / 2 + parameters["lateral_clearance_m"]
                    self.assertGreaterEqual(nearest_ramp_edge, required_edge)

    def test_numerical_ramp_grades_pass_the_assumed_limit_in_both_directions(self):
        for route in self.result["routes"]:
            if route["kind"] != "ramp":
                continue
            heights = [point[2] for point in route["points"]]
            descending = route["direction"] == "off"
            for first, second in zip(route["points"], route["points"][1:]):
                run = math.hypot(second[0] - first[0], second[1] - first[1])
                self.assertLessEqual(100 * abs(second[2] - first[2]) / run, self.design["geometry"]["max_grade_percent"] + 1e-7)
            if descending:
                self.assertTrue(all(a >= b - 1e-10 for a, b in zip(heights, heights[1:])))
                self.assertAlmostEqual(heights[-1], 0)
            else:
                self.assertTrue(all(a <= b + 1e-10 for a, b in zip(heights, heights[1:])))
                self.assertAlmostEqual(heights[0], 0)
            self.assertAlmostEqual(heights[0], heights[1])
            self.assertAlmostEqual(heights[-1], heights[-2])

    def test_graph_connects_all_distinct_arms_without_a_direct_deck_transfer(self):
        graph = {}
        arms = {"SW", "NE", "NW", "SE"}
        for route in self.result["routes"]:
            graph.setdefault(route["from"], set()).add(route["to"])
            self.assertNotEqual(route["from"], route["to"])
        for movement in self.result["required_movements"]:
            pending = [movement["from"]]
            seen = set()
            reached = set()
            while pending:
                current = pending.pop()
                for target in graph.get(current, ()):
                    if target in arms:
                        reached.add(target)
                    elif target not in seen:
                        seen.add(target)
                        pending.append(target)
            self.assertIn(movement["to"], reached, movement)
        direct_highway_edges = {(route["from"], route["to"]) for route in self.result["routes"] if route["kind"] == "highway-through"}
        self.assertEqual(direct_highway_edges, {("SW", "NE"), ("NE", "lower-branch-in"), ("lower-branch-in", "lower-branch-out"), ("lower-branch-out", "SW")})

    def test_internal_node_positions_match_even_after_world_rotation(self):
        nodes = {}
        for route in self.result["routes"]:
            for node, point in ((route["from"], route["points"][0]), (route["to"], route["points"][-1])):
                if node in {"SW", "NE", "NW", "SE"}:
                    continue  # External arms contain separate incoming/outgoing lanes.
                if node in nodes:
                    self.assertLess(math.dist(nodes[node], point), 1e-8, node)
                nodes[node] = point

    def test_ramps_stay_on_the_right_side_and_have_forward_highway_tangents(self):
        by_id = {route["id"]: route for route in self.result["routes"]}
        for name in ("upper-off", "upper-on", "lower-off", "lower-on"):
            route = by_id[name]
            local = route["points_uvz"]
            side = -1 if name.startswith("upper") else 1
            self.assertTrue(all(side * point[1] > 0 for point in local))
            direction = 1 if side < 0 else -1
            for a, b in ((local[0], local[1]), (local[-2], local[-1])):
                self.assertGreater(direction * (b[0] - a[0]), 0)
                self.assertLess(abs(b[1] - a[1]) / abs(b[0] - a[0]), 0.01)

    def test_too_short_or_uncleared_ramps_are_rejected(self):
        short = copy.deepcopy(self.design)
        short["geometry"]["lower_ramp_plan_length_m"] = 24
        with self.assertRaisesRegex(ValueError, "lateral shift"):
            GEOMETRY.build_geometry(short)
        overlap = copy.deepcopy(self.design)
        overlap["geometry"]["descent_clear_v_m"] = 8
        with self.assertRaisesRegex(ValueError, "whole ramp width"):
            GEOMETRY.build_geometry(overlap)
        steep = copy.deepcopy(self.design)
        steep["geometry"]["max_grade_percent"] = 8
        with self.assertRaisesRegex(ValueError, "exceeding"):
            GEOMETRY.build_geometry(steep)

    def test_lower_ramps_are_three_tiles_and_upper_ramps_five_without_hidden_sections(self):
        parameters = self.result["metadata"]["parameters"]
        self.assertEqual(parameters["lower_ramp_plan_length_m"], 48)
        self.assertEqual(parameters["upper_ramp_plan_length_m"], 80)
        self.assertEqual(parameters["junction_offset_m"], 28)
        self.assertEqual(self.result["metadata"]["slip_lane_corridor_width_m"], 62)
        for route in self.result["routes"]:
            if route["kind"] != "ramp":
                continue
            local = route["points_uvz"]
            target = 80 if route["id"].startswith("upper") else 48
            self.assertTrue(all(abs(point[1]) <= 28 + 1e-9 for point in local))
            sampled_length = sum(math.dist(first[:2], second[:2]) for first, second in zip(local, local[1:]))
            self.assertAlmostEqual(sampled_length, target, delta=0.01)
            self.assertAlmostEqual(route["length_plan_m"], sampled_length)
            self.assertGreater(route["length_3d_m"], sampled_length)
            self.assertLess(abs(local[-1][0] - local[0][0]), target)
            self.assertEqual(len(route["plan"]["cubic_segments_canonical_uv"]), 1)

    def test_compact_ramps_have_exact_horizontal_tangents_at_both_ends(self):
        for route in self.result["routes"]:
            if route["kind"] != "ramp":
                continue
            controls = route["plan"]["cubic_segments_canonical_uv"][0]
            self.assertEqual(controls[0][1], controls[1][1])
            self.assertEqual(controls[2][1], controls[3][1])
            self.assertGreater(controls[1][0], controls[0][0])
            self.assertGreater(controls[3][0], controls[2][0])

    def test_reported_plan_radius_agrees_with_independent_sample_circumcircles(self):
        ramp = next(route for route in self.result["routes"] if route["id"] == "upper-off")
        radii = []
        for a, b, c in zip(ramp["points_uvz"], ramp["points_uvz"][1:], ramp["points_uvz"][2:]):
            ab, ac, bc = math.dist(a[:2], b[:2]), math.dist(a[:2], c[:2]), math.dist(b[:2], c[:2])
            cross = abs((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]))
            if cross > 1e-12:
                radii.append(ab * ac * bc / (2 * cross))
        self.assertAlmostEqual(min(radii), ramp["radius_min_plan_m"], delta=0.03 * ramp["radius_min_plan_m"])

    def test_two_tile_lower_alternative_exceeds_the_declared_experimental_grade_limit(self):
        two_tile = copy.deepcopy(self.design)
        two_tile["geometry"]["lower_ramp_plan_length_m"] = 32
        two_tile["geometry"]["lower_highway_join_m"] = GEOMETRY.solve_highway_half_length(two_tile["geometry"], 32)
        with self.assertRaisesRegex(ValueError, "exceeding.*40"):
            GEOMETRY.build_geometry(two_tile)
        # The limit is a declared experiment setting, rather than a claim that
        # a still steeper geometric route cannot be drawn.
        two_tile["geometry"]["max_grade_percent"] = 60
        alternative = GEOMETRY.build_geometry(two_tile)
        ramp = next(route for route in alternative["routes"] if route["id"] == "lower-off")
        self.assertGreater(ramp["grade_max_percent"], 40)
        self.assertAlmostEqual(ramp["length_plan_m"], 32, delta=0.01)
        self.assertLess(ramp["radius_min_plan_m"], ramp["width_m"] / 2)

    def test_lower_branch_joins_are_internal_to_the_longer_upper_highway(self):
        by_id = {route["id"]: route for route in self.result["routes"]}
        self.assertEqual(len(by_id), 26)
        self.assertEqual(by_id["lower-off"]["from"], "lower-branch-in")
        self.assertEqual(by_id["lower-on"]["to"], "lower-branch-out")
        self.assertEqual(by_id["highway-lower-approach"]["from"], "NE")
        self.assertEqual(by_id["highway-lower-departure"]["to"], "SW")
        parameters = self.result["metadata"]["parameters"]
        self.assertLess(parameters["lower_highway_join_m"], parameters["highway_half_length_m"])
        self.assertAlmostEqual(by_id["lower-off"]["points_uvz"][0][0], parameters["lower_highway_join_m"])
        self.assertAlmostEqual(by_id["lower-on"]["points_uvz"][-1][0], -parameters["lower_highway_join_m"])

    def test_source_parameters_are_retained_and_inconsistent_length_is_rejected(self):
        self.assertEqual(self.result["metadata"]["parameters"], self.design["geometry"])
        invalid = copy.deepcopy(self.design)
        invalid["geometry"]["highway_half_length_m"] += 1
        with self.assertRaisesRegex(ValueError, "does not match"):
            GEOMETRY.build_geometry(invalid)

    def test_turns_do_not_overshoot_their_target_lane_or_reverse(self):
        for route in self.result["routes"]:
            if route["kind"] != "surface-turn":
                continue
            points = route["points_uvz"]
            for axis in (0, 1):
                start, finish = points[0][axis], points[-1][axis]
                low, high = sorted((start, finish))
                for point in points:
                    self.assertGreaterEqual(point[axis], low - 1e-9)
                    self.assertLessEqual(point[axis], high + 1e-9)
                direction = 1 if finish > start else -1
                self.assertTrue(all(direction * (b[axis] - a[axis]) >= -1e-9 for a, b in zip(points, points[1:])))

    def test_surface_intersections_are_four_arm_conflicts_not_proved_game_junctions(self):
        self.assertEqual(len(self.result["intersections"]), 2)
        self.assertTrue(all(item["arms"] == 4 for item in self.result["intersections"]))
        self.assertTrue(all(item["signals_or_priority"] == "unimplemented" for item in self.result["intersections"]))
        self.assertIn("unverified", self.result["metadata"]["native_seams"])


if __name__ == "__main__":
    unittest.main()
