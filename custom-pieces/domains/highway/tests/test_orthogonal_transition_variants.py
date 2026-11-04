"""Portable geometry and identity controls for the orthogonal transitions."""
from dataclasses import FrozenInstanceError
import math
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "framework"))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp_highway import orthogonal_transition_geometry as geometry
from scp_highway import orthogonal_transition_variants as variants
from scp_highway import ramp_paths


class TransitionVariantControls(unittest.TestCase):
    def test_lower_bend_is_a_distinct_recipe_outside_the_upper_bend_family(self):
        key = variants.LOWER_BEND_RIGHT
        record = variants.record_for(key)
        self.assertEqual(variants.SUPPORTED_PIECE_IDS, (*variants.PIECE_IDS, record.piece_id))
        self.assertEqual(variants.SUPPORTED_RECIPES, (*variants.RECIPES, record.recipe))
        self.assertNotIn(key, variants.VARIANTS)
        self.assertIsNotNone(re.fullmatch(r"[a-z][a-z0-9-]{1,63}", record.piece_id))
        self.assertEqual((record.shifted_deck, record.physical_reflection,
                          record.traffic_reversed, record.native_cross_section_reflection),
                         ("lower", False, True, True))
        piece = {"domain": "highway", "id": record.piece_id, "recipe": record.recipe}
        with self.assertRaises(ValueError):
            variants.variant_of(piece)
        self.assertEqual(variants.variant_of({**piece, "transition_variant": key}), key)
        with self.assertRaises(ValueError):
            variants.variant_of({**piece, "transition_variant": key, "recipe": variants.MIRRORED_RECIPE})

    def test_lower_bend_keeps_straight_upper_and_exact_directed_lane_sockets(self):
        key = variants.LOWER_BEND_RIGHT
        routes = {route["id"]: route["points"] for route in geometry.traffic_routes(variant=key)}
        self.assertEqual({name: (points[0], points[-1]) for name, points in routes.items()},
                         {"upper-lane-0": ((18.5, -88., 0.), (18.5, 8., 15.)),
                          "upper-lane-1": ((13.5, -88., 0.), (13.5, 8., 15.)),
                          "lower-lane-0": ((13.5, 8., 7.5), (-2.5, -88., 0.)),
                          "lower-lane-1": ((18.5, 8., 7.5), (2.5, -88., 0.))})
        self.assertTrue(all(point[0] == 18.5 for point in routes["upper-lane-0"]))
        self.assertEqual(geometry.frame("lower", 36., variant=key)[0], (8., 28.))
        self.assertEqual(geometry.height("lower", 36., variant=key), 3.75)
        sliced = ramp_paths.slice_routes(geometry.traffic_routes(variant=key))
        self.assertEqual(set(geometry.CELLS) - set(sliced), {(0, 0)})
        self.assertTrue(set(sliced) <= set(geometry.CELLS))
        self.assertEqual(geometry.model_only_cells(variant=key), ((0, 0),))

    def test_lower_bend_source_lane_grades_and_sampled_lower_vehicle_headroom(self):
        key = variants.LOWER_BEND_RIGHT
        peaks = {}
        for route in geometry.traffic_routes(variant=key):
            points = route["points"]
            peaks[route["id"]] = max(abs(b[2]-a[2])/math.dist(a[:2], b[:2])
                                     for a, b in zip(points, points[1:]))
        self.assertAlmostEqual(peaks["upper-lane-0"], 15./78., places=12)
        self.assertAlmostEqual(peaks["upper-lane-1"], 15./78., places=12)
        self.assertTrue(all(.155 < peaks[name] < .156 for name in ("lower-lane-0", "lower-lane-1")))
        clearance = []
        for station in geometry.STATIONS:
            for lateral in (side*(1.25+.25*i) for side in (-1, 1) for i in range(11)):
                east, lower_height, south = geometry.model_point("lower", station, lateral, variant=key)
                if 7.999 <= east <= 24.001 and -8. <= south <= 88.:
                    upper_height = geometry.height("upper", south+8., variant=key)
                    clearance.append(upper_height-1.-lower_height)
        self.assertGreater(min(clearance), 4.5)

    def test_finite_records_keep_physical_and_traffic_choices_independent(self):
        expected = ((False, False, False, False), (True, True, False, False),
                    (True, False, True, True), (False, True, True, True))
        self.assertEqual(variants.VARIANTS,
                         ("original", "mirrored", "opposite-side", "opposite-side-mirrored"))
        self.assertEqual(len(set(variants.PIECE_IDS)), 4)
        self.assertEqual(len(set(variants.RECIPES)), 4)
        for index, (key, flags) in enumerate(zip(variants.VARIANTS, expected)):
            record = variants.record_for(key)
            self.assertEqual((record.physical_reflection, record.traffic_reversed,
                              record.native_cross_section_reflection, record.opposite_side), flags)
            self.assertEqual((record.piece_id, record.recipe),
                             (variants.PIECE_IDS[index], variants.RECIPES[index]))
            self.assertEqual(geometry.is_mirrored(key), flags[0])
            self.assertEqual(geometry.traffic_reversed(key), flags[1])
            self.assertEqual(geometry.native_cross_section_reflected(key), flags[2])
            self.assertEqual(geometry.is_opposite_side(key), flags[3])
            with self.assertRaises(FrozenInstanceError):
                record.physical_reflection = not record.physical_reflection

    def test_every_identity_fits_the_catalogue_limit(self):
        self.assertEqual(variants.PIECE_IDS[2:],
            ("ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile",
             "ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored"))
        for value in variants.PIECE_IDS:
            self.assertIsNotNone(re.fullmatch(r"[a-z][a-z0-9-]{1,63}", value))

    def test_exact_identity_recipe_and_variant_pairing_is_required(self):
        for identity_index, piece_id in enumerate(variants.PIECE_IDS):
            for recipe_index, recipe in enumerate(variants.RECIPES):
                for variant_index, key in enumerate(variants.VARIANTS):
                    piece = {"id": piece_id, "recipe": recipe, "domain": "highway",
                             "transition_variant": key}
                    if identity_index == recipe_index == variant_index:
                        self.assertEqual(variants.variant_of(piece), key)
                    else:
                        with self.assertRaisesRegex(ValueError, "identity or variant"):
                            variants.variant_of(piece)

    def test_absent_variant_preserves_only_the_original_identity(self):
        for index, piece_id in enumerate(variants.PIECE_IDS):
            piece = {"id": piece_id, "recipe": variants.RECIPES[index], "domain": "highway"}
            if index == 0:
                self.assertEqual(variants.variant_of(piece), "original")
            else:
                with self.assertRaises(ValueError):
                    variants.variant_of(piece)
        piece = {"id": variants.PIECE_ID, "recipe": variants.RECIPE,
                 "domain": "high-speed-rail"}
        with self.assertRaises(ValueError):
            variants.variant_of(piece)

    def test_unknown_variants_and_invented_prefixed_identities_are_rejected(self):
        for key in (None, True, False, [], {}, "", "side", "reflected"):
            with self.subTest(variant=key), self.assertRaisesRegex(ValueError, "variant"):
                variants.record_for(key)
        for key in variants.VARIANTS:
            piece = {"id": variants.PIECE_ID + "-invented", "recipe": variants.record_for(key).recipe,
                     "domain": "highway", "transition_variant": key}
            with self.assertRaises(ValueError):
                variants.variant_of(piece)

    def test_added_paths_reverse_the_other_existing_shape_and_swap_native_classes(self):
        for added, physical in (("opposite-side", "mirrored"),
                                ("opposite-side-mirrored", "original")):
            reference = {row["id"]: row for row in geometry.traffic_routes(variant=physical)}
            for route in geometry.traffic_routes(variant=added):
                deck = route["id"].split("-")[0]
                previous = reference[f"{deck}-lane-{1 - route['lane']}"]
                self.assertEqual(route["points"], list(reversed(previous["points"])))
                self.assertEqual(route["transport"], 1)
                self.assertFalse(route["junction"])

    def test_new_external_lane_contacts_have_literal_required_directions_and_classes(self):
        contacts = {
            "opposite-side": {
                "upper-lane-0": ((-2.5, 8., 15.), (13.5, -88., 0.)),
                "upper-lane-1": ((2.5, 8., 15.), (18.5, -88., 0.)),
                "lower-lane-0": ((2.5, -88., 0.), (2.5, 8., 7.5)),
                "lower-lane-1": ((-2.5, -88., 0.), (-2.5, 8., 7.5)),
            },
            "opposite-side-mirrored": {
                "upper-lane-0": ((2.5, -88., 0.), (18.5, 8., 15.)),
                "upper-lane-1": ((-2.5, -88., 0.), (13.5, 8., 15.)),
                "lower-lane-0": ((13.5, 8., 7.5), (13.5, -88., 0.)),
                "lower-lane-1": ((18.5, 8., 7.5), (18.5, -88., 0.)),
            },
        }
        for key, expected in contacts.items():
            for row in geometry.traffic_routes(variant=key):
                self.assertEqual((row["points"][0], row["points"][-1]), expected[row["id"]])
                self.assertEqual(row["lane"], int(row["id"][-1]))

    def test_added_paths_keep_twelve_cell_frame_and_the_correct_model_only_cell(self):
        for key, empty in (("opposite-side", (1, 0)), ("opposite-side-mirrored", (0, 0))):
            routes = ramp_paths.slice_routes(geometry.traffic_routes(variant=key))
            self.assertEqual(set(geometry.CELLS) - set(routes), {empty})
            self.assertEqual(geometry.model_only_cells(variant=key), (empty,))
            self.assertEqual(set(routes) | {empty}, {(x, y) for y in range(6) for x in range(2)})

    def test_added_road_frames_and_heights_retain_the_other_existing_physical_shape(self):
        for added, physical in (("opposite-side", "mirrored"),
                                ("opposite-side-mirrored", "original")):
            for deck in ("upper", "lower"):
                for station in geometry.BREAKS:
                    for lateral in (-8., -2.5, 0., 2.5, 8.):
                        self.assertEqual(geometry.model_point(deck, station, lateral, variant=added),
                                         geometry.model_point(deck, station, lateral, variant=physical))

    def test_added_peak_absolute_lane_grades_are_unchanged(self):
        def grades(variant):
            values = {}
            for route in geometry.traffic_routes(variant=variant):
                deck = route["id"].split("-")[0]
                grade = max(abs(b[2] - a[2]) / math.dist(a[:2], b[:2])
                            for a, b in zip(route["points"], route["points"][1:]))
                values[deck] = max(values.get(deck, 0.), grade)
            return values
        for added, physical in (("opposite-side", "mirrored"),
                                ("opposite-side-mirrored", "original")):
            self.assertEqual(grades(added), grades(physical))
            self.assertLess(grades(added)["upper"], .20)
            self.assertLess(grades(added)["lower"], .20)

    def test_only_added_metadata_exposes_independent_side_and_traffic_fields(self):
        original = geometry.engineering_metadata()
        mirrored = geometry.engineering_metadata(variant="mirrored")
        self.assertNotIn("transition_variant", original)
        self.assertEqual(mirrored["transition_variant"], "mirrored")
        new_fields = {"physical_reflection", "traffic_reversed", "native_cross_section_reflection",
                      "canonical_lane_index_by_native_source_class", "base_traffic_variant"}
        self.assertFalse(new_fields.intersection(original))
        self.assertFalse(new_fields.intersection(mirrored))
        for key, axes, directions in (("opposite-side", (0., 0., 16.), ("southbound", "northbound")),
                                      ("opposite-side-mirrored", (16., 16., 0.), ("northbound", "southbound"))):
            metadata = geometry.engineering_metadata(variant=key)
            self.assertEqual(tuple(metadata[name] for name in
                ("dd_axis_east_m", "ground_lower_axis_east_m", "ground_upper_axis_east_m")), axes)
            self.assertEqual((metadata["upper_travel_direction"], metadata["lower_travel_direction"]), directions)
            self.assertEqual(metadata["canonical_lane_index_by_native_source_class"], [1, 0])
            self.assertTrue(metadata["native_cross_section_reflection"])


if __name__ == "__main__":
    unittest.main()
