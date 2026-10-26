"""Stress the existing matcher with artificial shared-edge HSR/Street records.

Only the HSR prototype coordinates come from the real two-piece pilot. Street
height 0, engine token 9001, section width 8, and its paths are synthetic inputs,
not NAM facts or compiled Street support. These resolved fixtures bypass source
extraction and physical geometry checks; they exercise simultaneous matching.
"""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scp-planner/src"))
from scp_planner.metadata import find_matches, load_library

CROSSING = "hsr-component-modular-crossing-core"
CURVE = "hsr-component-tight-paired-curve90-l4-to-mid"


def layered_fixture(pilot):
    """Keep one boundary per prototype and add a fictional lower Street layer."""
    result = []
    for slug, original_end, label in ((CROSSING, "upper-end-b", "a"),
                                      (CURVE, "curve-end-a", "b")):
        original = pilot["pieces"][slug]
        rail = deepcopy(next(g for g in original["groups"] if g["id"] == original_end))
        rail["id"] = "rail-"+label
        rail["boundary_bundle_id"] = "boundary-"+label
        street = deepcopy(rail)
        street["id"], street["component_id"] = "street-"+label, "synthetic-street"
        street["profile_id"] = "synthetic-street-pair"
        street["profile"].update(network="street", engine_transport=9001,
                                 section_id="synthetic-street-section",
                                 expected_deck_width_m=8., path_height_m=0.)
        street["anchor_m"][2] = street["tile_seam_center_m"][2] = 0.
        for group in (rail, street):
            old_ids = {port["id"]: group["id"]+"-"+port["direction"] for port in group["members"]}
            for channel in group["channels"]:
                channel["id"] = group["id"]+"-"+channel["id"]
                if group is street:
                    channel.update(kind="lane", traffic_modes=["synthetic-car"])
                for cut in channel["cuts"]:
                    cut["id"] = group["id"]+"-"+cut["id"]
                    cut["member_ids"] = [old_ids[x] for x in cut["member_ids"]]
            for port in group["members"]:
                port["id"] = old_ids[port["id"]]
                port["channel_id"] = group["id"]+"-"+port["channel_id"]
                port["cut_id"] = group["id"]+"-"+port["cut_id"]
                if group is street:
                    port.update(source_port_id="synthetic-source-"+port["id"],
                                service_network="street", engine_transport=9001, traffic_modes=["synthetic-car"])
                    port["endpoint_m"][2] = 0.
                    port["resource_keys"] = []
        bundle = {"id": rail["boundary_bundle_id"], "source_cell": rail["source_cell"],
                  "edge": rail["edge"], "connector_ids": [rail["id"], street["id"]]}
        result.append({"id": "synthetic-piece-"+label, "cells": deepcopy(original["cells"]),
                       "groups": [rail, street], "boundary_bundles": [bundle],
                       "supported_orientations": deepcopy(original["supported_orientations"])})
    return result


def only_layer(piece, prefix):
    result = deepcopy(piece)
    result["groups"] = [g for g in result["groups"] if g["id"].startswith(prefix)]
    result["boundary_bundles"][0]["connector_ids"] = [g["id"] for g in result["groups"]]
    return result


class BoundaryEdgeCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pilot = load_library(ROOT / "custom-pieces", [CROSSING, CURVE])

    def setUp(self):
        self.a, self.b = layered_fixture(self.pilot)

    def test_hsr_and_street_match_together_at_one_pose(self):
        matches = find_matches(self.a, self.b)
        self.assertEqual({(m["a_group_id"], m["b_group_id"]) for m in matches},
                         {("rail-a", "rail-b"), ("street-a", "street-b")})
        for match in matches:
            self.assertEqual(match["relative_rotation_ccw"], 0)
            self.assertEqual(match["relative_position_m"], [0., 64.])
            self.assertEqual(len(match["bundle_group_pairs"]), 2)

    def test_hsr_only_is_valid_when_both_boundaries_really_have_only_hsr(self):
        matches = find_matches(only_layer(self.a, "rail-"), only_layer(self.b, "rail-"))
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["relative_position_m"], [0., 64.])

    def test_matching_hsr_cannot_silently_drop_required_street(self):
        self.assertEqual(find_matches(self.a, only_layer(self.b, "rail-")), [])

    def test_wrong_street_height_rejects_the_whole_boundary(self):
        street = self.b["groups"][1]
        street["profile"]["path_height_m"] = 1.
        street["anchor_m"][2] = street["tile_seam_center_m"][2] = 1.
        for port in street["members"]:
            port["endpoint_m"][2] = 1.
        self.assertEqual(find_matches(self.a, self.b), [])

    def test_wrong_street_network_rejects_the_whole_boundary(self):
        street = self.b["groups"][1]
        street["profile"]["network"] = "road"
        for port in street["members"]:
            port["service_network"] = "road"
        self.assertEqual(find_matches(self.a, self.b), [])

    def test_wrong_street_engine_class_rejects_the_whole_boundary(self):
        street = self.b["groups"][1]
        street["profile"]["engine_transport"] = 9002
        for port in street["members"]:
            port["engine_transport"] = 9002
        self.assertEqual(find_matches(self.a, self.b), [])

    def test_wrong_street_flow_rejects_the_whole_boundary(self):
        for port in self.b["groups"][1]["members"]:
            port["direction"] = "in"
        self.assertEqual(find_matches(self.a, self.b), [])

    def test_one_transform_cannot_be_chosen_independently_for_each_layer(self):
        # Deliberately move one resolved layer by a whole tile. This is a
        # matching stress input, not a valid authored same-tile sidecar: the
        # source-boundary validator is not being tested by this fixture.
        street = self.b["groups"][1]
        for key in ("anchor_m", "tile_seam_center_m"):
            street[key][0] += 16.
        for port in street["members"]:
            port["endpoint_m"][0] += 16.
        rail_match = find_matches(only_layer(self.a, "rail-"), only_layer(self.b, "rail-"))
        street_match = find_matches(only_layer(self.a, "street-"), only_layer(self.b, "street-"))
        self.assertEqual(rail_match[0]["relative_position_m"], [0., 64.])
        self.assertEqual(street_match[0]["relative_position_m"], [-16., 64.])
        self.assertEqual(find_matches(self.a, self.b), [])

    def test_missing_endpoint_data_fails_explicitly(self):
        del self.b["groups"][1]["members"][0]["endpoint_m"]
        with self.assertRaises(ValueError):
            find_matches(self.a, self.b)

    def test_successful_synthetic_match_is_not_physical_or_game_verification(self):
        for match in find_matches(self.a, self.b):
            self.assertEqual(match["status"], "candidate")
            for check in ("physical_seams", "construction_clearance", "geometry_collisions", "in_game"):
                self.assertEqual(match["checks"][check], "unverified")


if __name__ == "__main__":
    unittest.main()
