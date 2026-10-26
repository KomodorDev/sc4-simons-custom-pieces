"""Check source-owned overview facts, boundary grouping, and readable wrapped cards."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "framework"))

try:
    from scp import connector_overview as overview
    from scp.preview import font
except ModuleNotFoundError:
    overview = None


def resolved_piece():
    """Synthetic resolved records exercise presentation, not a compiled network claim."""
    members = []
    channels = []
    for index, (flow, x, tangent) in enumerate((("in", 3., [0., 1.]), ("out", -1., [0., -1.])), 1):
        name, channel, cut = f"end-a-member-{index}", f"channel-{index}", f"cut-{index}"
        point = [x, -8., 30.5]
        members.append({"id": name, "source_port_id": f"legacy-{index}", "direction": flow,
                        "endpoint_m": point, "tangent": tangent, "grade": .1,
                        "edge": 3, "engine_transport": 7, "role": "primary", "service_network": "hsr",
                        "channel_id": channel, "cut_id": cut, "traffic_modes": ["train"]})
        channels.append({"id": channel, "component_id": "route", "kind": "rail", "traffic_modes": ["train"],
                         "cuts": [{"id": cut, "member_ids": [name], "endpoint_m": point,
                                   "heading_outward_degrees": 180., "grade_outward": -.1 if flow == "in" else .1}]})
    return {"id": "synthetic", "piece": {"name": "Synthetic test only"},
            "boundary_bundles": [{"id": "south-boundary", "source_cell": [0, 0], "edge": "south"}],
            "groups": [{"id": "end-a", "component_id": "route", "profile_id": None,
                        "profile": {"network": "hsr", "nominal_level": "l4"},
                        "boundary_bundle_id": "south-boundary", "section_offset_m": 1.,
                        "anchor_m": [1., -8., 30.5], "outward_normal": [0., -1.],
                        "members": members, "channels": channels}]}


@unittest.skipIf(overview is None, "Pillow/NumPy overview dependencies unavailable")
class ConnectorOverviewTests(unittest.TestCase):
    def test_explicit_channels_and_cuts_are_distinct_from_directed_members(self):
        piece = resolved_piece()
        group = piece["groups"][0]
        group["members"][1]["endpoint_m"] = group["members"][0]["endpoint_m"][:]
        group["members"][1].update(channel_id="channel-1", cut_id="cut-1")
        group["channels"] = group["channels"][:1]
        group["channels"][0]["cuts"][0]["member_ids"].append(group["members"][1]["id"])
        record = overview.build_records(piece)[0]
        self.assertEqual((record["physical_channel_count"], record["edge_cut_count"], len(record["members"])), (1, 1, 2))
        self.assertIsNone(record["channel_spacing_m"])

    def test_outward_grade_heading_and_offset_come_from_member_measurements(self):
        record = overview.build_records(resolved_piece())[0]
        first, last = record["members"]
        self.assertEqual([first["section_frame_offset_m"], last["section_frame_offset_m"]], [2., -2.])
        self.assertEqual([first["outward_slope_at_edge_percent"], last["outward_slope_at_edge_percent"]], [-10., 10.])
        self.assertIsNone(record["common_outward_grade_at_edge"])
        self.assertEqual(record["common_outward_heading_degrees"], 180.)
        self.assertEqual(record["channel_spacing_m"], 4.)
        self.assertFalse(record["centred_on_tile_boundary"])
        diagonal = overview.outward_measurement({"direction": "out", "tangent": [1., 1.], "grade": .03})
        self.assertAlmostEqual(diagonal["outward_heading_degrees"], 45.)
        self.assertEqual(diagonal["outward_slope_at_edge_percent"], 3.)

    def test_incoming_flat_grade_never_displays_negative_zero(self):
        value = overview.outward_measurement({"direction": "in", "tangent": [0., 1.], "grade": 0.})
        self.assertEqual(f"{value['outward_slope_at_edge_percent']:g}", "0")

    def test_different_member_headings_are_not_averaged(self):
        piece = resolved_piece()
        piece["groups"][0]["members"][1]["tangent"] = [1., -1.]
        record = overview.build_records(piece)[0]
        self.assertIsNone(record["common_outward_heading_degrees"])
        self.assertEqual([member["outward_heading_degrees"] for member in record["members"]], [180., 135.])
        self.assertIsNone(record["channel_spacing_m"])

    def test_actual_pieces_keep_six_groups_twelve_members_and_custom_height(self):
        from scp.connector_metadata import load_library
        root = Path(__file__).resolve().parents[1]
        identifiers = ["hsr-component-modular-crossing-core", "hsr-component-tight-paired-curve90-l4-to-mid"]
        library = load_library(root, identifiers)
        records = [record for piece in library["pieces"].values() for record in overview.build_records(piece)]
        self.assertEqual(len(records), 6)
        self.assertEqual(sum(len(record["members"]) for record in records), 12)
        custom = next(record for record in records if record["id"] == "curve-end-b")
        self.assertEqual(overview.level_and_height(custom), "Custom (23 m)")
        self.assertEqual(custom["anchor_enh_m"], [56., 0., 23.])
        self.assertEqual((custom["physical_channel_count"], custom["edge_cut_count"]), (2, 2))

    def test_groups_on_one_source_edge_share_one_card(self):
        first = overview.build_records(resolved_piece())[0]
        second = deepcopy(first)
        second.update(id="street-section", network="street", path_height_m=1.)
        cards = overview.make_boundary_cards([second, first])
        self.assertEqual(len(cards), 1)
        self.assertEqual([item["id"] for item in cards[0]["groups"]], ["end-a", "street-section"])
        self.assertEqual({item["marker"] for item in cards[0]["groups"]}, {"A"})

    def test_parallel_services_have_separate_panels_but_one_required_boundary(self):
        template = overview.build_records(resolved_piece())[0]
        records = []
        for index, network in enumerate(("hsr", "road", "pedestrian"), 1):
            record = deepcopy(template)
            record.update(id=f"service-{index}", component_id=f"component-{index}", network=network)
            records.append(record)
        card = overview.make_boundary_cards(records)[0]
        before = deepcopy(card["groups"])
        image = overview.render_boundary_card(card, 932, font)
        self.assertEqual(len(card["service_sections"]), 3)
        self.assertIn("All 3 service groups are required together", card["requirement"])
        self.assertEqual(card["groups"], before, "Presentation must preserve every resolved fact")
        self.assertEqual(len({section["colour"] for section in card["service_sections"]}), 3)
        for section, record in zip(card["service_sections"], records):
            self.assertEqual(section["group_id"], record["id"])
            self.assertTrue(section["required_together"])
            self.assertIn(record["network"].upper(), section["title"])
            left, top, right, bottom = section["bounds"]
            self.assertTrue(0 <= left < right < image.width)
            self.assertTrue(0 <= top < section["header_bounds"][3] < bottom < image.height)
            headings = [run for run in card["text_runs"] if run["kind"] == "service_heading"
                        and top <= run["bounds"][1] < bottom]
            self.assertEqual(len(headings), 1)
            measurements = [run for run in card["text_runs"] if run["kind"] == "section_heading"
                            and top <= run["bounds"][1] < bottom]
            self.assertEqual(len(measurements), 5)
            self.assertTrue(all(run["bounds"][1] > section["header_bounds"][3] for run in measurements))
        for first, second in zip(card["service_sections"], card["service_sections"][1:]):
            self.assertGreaterEqual(second["bounds"][1] - first["bounds"][3], 32)
        self.assertEqual(sum(row["label"] == "Level (path height)" for row in card["field_rows"]), 3)

    def test_marker_order_ignores_input_array_order_and_is_not_camera_order(self):
        record = overview.build_records(resolved_piece())[0]
        records = []
        for edge in ("East", "West", "North", "South"):
            item = deepcopy(record)
            item.update(id=edge.lower(), boundary=edge, boundary_bundle_id=edge.lower())
            records.append(item)
        expected = [("A", "south"), ("B", "north"), ("C", "west"), ("D", "east")]
        for order in (records, list(reversed(records))):
            self.assertEqual([(card["marker"], card["id"]) for card in overview.make_boundary_cards(order)], expected)
        self.assertEqual(overview.marker_label(26), "AA")

    def test_wrapped_long_ids_coordinates_and_profile_do_not_overlap(self):
        record = overview.build_records(resolved_piece())[0]
        record["id"] = "long-service-" * 10
        record["profile_id"] = "long-profile-" * 18
        for member in record["members"]:
            member["id"] += "-long-member-reference" * 8
            member["channel_id"] += "-channel-reference" * 6
            member["endpoint_m"] = [-123456.789, 123456.789, 123456.789]
        second = deepcopy(record)
        second["id"] += "second"
        card = overview.make_boundary_cards([record, second])[0]
        image = overview.render_boundary_card(card, 932, font)
        self.assertGreater(image.height, 3000)
        for run in card["text_runs"]:
            left, top, right, bottom = run["bounds"]
            self.assertTrue(0 <= left <= right <= image.width)
            self.assertTrue(0 <= top <= bottom <= image.height)
        for index, a in enumerate(card["text_runs"]):
            ax0, ay0, ax1, ay1 = a["bounds"]
            for b in card["text_runs"][index + 1:]:
                bx0, by0, bx1, by1 = b["bounds"]
                self.assertFalse(max(ax0, bx0) < min(ax1, bx1) and max(ay0, by0) < min(ay1, by1),
                                 (a["text"], b["text"]))

    def test_markdown_uses_the_same_full_member_facts_as_cards(self):
        records = overview.build_records(resolved_piece())
        cards = overview.make_boundary_cards(records)
        evidence = {"groups": records, "boundary_cards": [
            {"marker": card["marker"], "id": card["id"], "group_ids": [item["id"] for item in card["groups"]]}
            for card in cards], "conventions": [overview.grid_convention({"origin_world_m": [0., -48.]})]}
        text = overview.markdown_overview(evidence)
        self.assertIn("Level 4 (30.5 m)", text)
        self.assertIn("end-a-member-1", text)
        self.assertIn("`[3,-8,30.5]`", text)
        self.assertIn("-10", text)
        self.assertIn("Y = 3 − source row", text)
        self.assertIn("No profile reference", text)
        self.assertIn("Service group 1 / 1: HSR — Level 4 (30.5 m)", text)

    def test_selectable_parallel_cards_keep_service_sections_and_joint_requirement(self):
        records = overview.build_records(resolved_piece())
        second = deepcopy(records[0])
        second.update(id="road", network="road")
        records.append(second)
        cards = overview.make_boundary_cards(records)
        text = overview.markdown_overview({"groups": records, "boundary_cards": [
            {"marker": card["marker"], "id": card["id"], "group_ids": [item["id"] for item in card["groups"]]}
            for card in cards], "conventions": []})
        self.assertEqual(text.count("### Boundary "), 1)
        self.assertEqual(text.count("#### Service group "), 2)
        self.assertIn("All 2 service groups are required together at this edge.", text)
        self.assertIn("HSR — Level 4 (30.5 m)", text)
        self.assertIn("ROAD — Level 4 (30.5 m)", text)

    def test_overview_uses_shared_three_row_header_with_only_one_scale_caption(self):
        from scp.render_headers import FACTS_INK, SUBTITLE_INK, TITLE_INK
        class Pixel(list):
            def tolist(self):
                return list(self)
        class Camera:
            def project_world(self, *point):
                return Pixel([500., 150.])
            def metadata(self):
                return {"synthetic": True}
        piece = resolved_piece()
        local = {"origin_world_m": [0., 0.], "construction_reference": {
            "local_tiles_en": [0, 0], "caption_visible": True}}
        scene = overview.Image.new("RGB", (1904, 300), "white")
        _, evidence = overview.compose_figure(piece, overview.build_records(piece), scene, Camera(), local, font)
        rows = evidence["header"]["rows"]
        self.assertEqual(len(rows), 3)
        self.assertEqual([row["colour"] for row in rows], [TITLE_INK, SUBTITLE_INK, FACTS_INK])
        self.assertIn("Reusable piece / Southeast view / Connection overview", rows[1]["text"])
        self.assertIn("1 tile = 16 m", rows[2]["text"])
        self.assertEqual(sum(value.count("1 tile = 16 m") for value in evidence["figure_text"]), 1)
        self.assertGreaterEqual(evidence["viewport_offset_xy"][1], max(row["bounds"][3] for row in rows))


if __name__ == "__main__":
    unittest.main()
