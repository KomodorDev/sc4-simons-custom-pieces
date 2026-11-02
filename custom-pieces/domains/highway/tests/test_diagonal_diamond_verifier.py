"""Mutation checks keep the prototype verifier independent of its generator."""

import copy
import importlib.util
from pathlib import Path
import unittest


DOMAIN = Path(__file__).resolve().parents[1]


def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, DOMAIN / "tools" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GENERATOR = load_tool("diagonal_diamond_geometry")
VERIFIER = load_tool("verify_diagonal_diamond")


class IndependentDiamondVerifierTests(unittest.TestCase):
    def setUp(self):
        self.design = GENERATOR.load_design(DOMAIN / "01_assemblies" /
                                            "ddrhw-l1-and-l2-diagonal-avenue-diamond" / "design.jsonc")
        self.geometry = GENERATOR.build_geometry(self.design)

    def test_current_saved_contract_covers_every_distinct_arm_and_discloses_indirect_returns(self):
        result = VERIFIER.verify_geometry(self.design, self.geometry)
        self.assertEqual(result["required_distinct_arm_journeys"], 12)
        self.assertEqual(result["possible_indirect_returns_via_avenue"], ["NE", "SW"])
        self.assertFalse(result["compiled_resource_checks"])
        self.assertEqual(result["game_tests"], "not-run")

    def test_missing_avenue_turn_is_a_missing_journey(self):
        self.geometry["routes"] = [route for route in self.geometry["routes"]
                                   if route["id"] != "upper-off-to-NW"]
        with self.assertRaisesRegex(ValueError, "Missing or unexpected directed route IDs|Missing distinct-arm journeys"):
            VERIFIER.verify_geometry(self.design, self.geometry)

    def test_disconnected_native_looking_endpoint_does_not_pass_on_graph_labels(self):
        turn = next(route for route in self.geometry["routes"] if route["id"] == "upper-off-to-NW")
        turn["points"][0][0] += 0.1
        with self.assertRaisesRegex(ValueError, "disconnected saved endpoints"):
            VERIFIER.verify_geometry(self.design, self.geometry)

    def test_ramp_grade_is_measured_from_samples_instead_of_trusting_claimed_metadata(self):
        ramp = next(route for route in self.geometry["routes"] if route["id"] == "upper-off")
        ramp["points"][200][2] -= 2
        ramp["grade_max_percent"] = 0
        with self.assertRaisesRegex(ValueError, "height reverses|grade exceeds"):
            VERIFIER.verify_geometry(self.design, self.geometry)

    def test_roads_and_traffic_paths_cannot_silently_have_different_shapes(self):
        road = next(road for road in self.geometry["roads"] if road["id"] == "ramp-upper-off")
        road["points"] = copy.deepcopy(road["points"])
        road["points"][100][0] += 1
        with self.assertRaisesRegex(ValueError, "road and route samples differ"):
            VERIFIER.verify_geometry(self.design, self.geometry)

    def test_nonfinite_saved_geometry_and_invented_compilation_status_are_rejected(self):
        invalid = copy.deepcopy(self.geometry)
        invalid["roads"][0]["points"][3][0] = float("nan")
        with self.assertRaisesRegex(ValueError, "invalid coordinates"):
            VERIFIER.verify_geometry(self.design, invalid)
        self.design["compiled"] = True
        with self.assertRaisesRegex(ValueError, "unregistered, uncompiled"):
            VERIFIER.verify_geometry(self.design, self.geometry)

    def test_declared_highway_graph_cannot_hide_a_displaced_ground_level_route(self):
        route = next(route for route in self.geometry["routes"] if route["id"] == "highway-upper-through")
        route["points"] = [[x + 10000, y, 0] for x, y, _ in route["points"]]
        with self.assertRaisesRegex(ValueError, "highway samples leave"):
            VERIFIER.verify_geometry(self.design, self.geometry)

    def test_ramp_road_width_is_checked_separately_from_traffic_route_width(self):
        road = next(road for road in self.geometry["roads"] if road["id"] == "ramp-upper-off")
        road["width_m"] = 1000
        with self.assertRaisesRegex(ValueError, "wrong width"):
            VERIFIER.verify_geometry(self.design, self.geometry)

    def test_ground_ramp_cannot_cross_the_avenue_outside_its_intersection(self):
        route = next(route for route in self.geometry["routes"] if route["id"] == "upper-off")
        route["points"][-8] = [(20 + 64) / (2 ** 0.5), (20 - 64) / (2 ** 0.5), 0]
        with self.assertRaisesRegex(ValueError, "reverses outside|leaves its declared corridor"):
            VERIFIER.verify_geometry(self.design, self.geometry)


if __name__ == "__main__":
    unittest.main()
