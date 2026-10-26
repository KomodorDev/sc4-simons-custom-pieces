"""Keep portable connector source-contract regressions with their owning library.

These checks validate authored metadata without requiring native game inputs,
a saved build, or a consumer application.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest


CUSTOM_ROOT = next(parent for parent in Path(__file__).resolve().parents if (parent / "project.json").is_file())
DOMAIN = Path("domains/high-speed-rail")
CROSSING = "hsr-component-modular-crossing-core"
CORNER = "hsr-component-tight-paired-curve90-l4-to-mid"
PILOT_IDS = [CROSSING, CORNER]
sys.path.insert(0, str(CUSTOM_ROOT / "framework"))

from scp import connector_metadata as metadata
from scp import jsonc


def read_json(path):
    return jsonc.load(path) if path.suffix == ".jsonc" else json.loads(path.read_text())


class ConnectorSourceRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = read_json(CUSTOM_ROOT / DOMAIN / "connector-profiles.json")
        cls.profiles = metadata.resolve_profiles(cls.registry)
        cls.raw = {}
        for slug in PILOT_IDS:
            directory = CUSTOM_ROOT / DOMAIN / "00_pieces" / slug
            cls.raw[slug] = {name: read_json(directory / filename) for name, filename in (
                ("piece", "piece.json"), ("connections", "connections.json"), ("groups", "connector-groups.jsonc"))}
        cls.pilot = metadata.load_library(CUSTOM_ROOT, PILOT_IDS)

    def validate(self, slug, *, piece=None, connections=None, groups=None, profiles=None):
        raw = self.raw[slug]
        return metadata.validate_piece(
            deepcopy(raw["piece"] if piece is None else piece),
            deepcopy(raw["connections"] if connections is None else connections),
            deepcopy(raw["groups"] if groups is None else groups),
            deepcopy(self.profiles if profiles is None else profiles),
        )

    def test_resolved_profiles_inherit_optional_defaults_without_mutating_source(self):
        before = deepcopy(self.registry)
        resolved = metadata.resolve_profiles(self.registry)
        parent = resolved["hsr-orth-scp-paired15-t2-opposed-rhd-v1"]
        high = resolved["hsr-l4-orth-scp-paired15-t2-opposed-rhd-v1"]
        middle = resolved["hsr-h23000mm-orth-scp-paired15-t2-opposed-rhd-v1"]
        self.assertEqual(parent["network"], high["network"])
        self.assertEqual(parent["endpoint_grade"], high["endpoint_grade"])
        self.assertNotIn("expected_deck_width_m", high)
        self.assertNotIn("lanes", high)
        self.assertEqual(high["path_height_m"], 30.5)
        self.assertEqual(middle["path_height_m"], 23.0)
        self.assertIsNone(middle["nominal_level"])
        self.assertEqual(self.registry, before)

    def test_missing_profile_parent_is_rejected(self):
        registry = deepcopy(self.registry)
        registry["profiles"]["hsr-l4-orth-scp-paired15-t2-opposed-rhd-v1"]["extends"] = "missing-parent"
        with self.assertRaises(ValueError):
            metadata.resolve_profiles(registry)

    def test_profile_inheritance_cycle_is_rejected(self):
        registry = deepcopy(self.registry)
        registry["profiles"]["hsr-orth-scp-paired15-t2-opposed-rhd-v1"]["extends"] = "hsr-l4-orth-scp-paired15-t2-opposed-rhd-v1"
        with self.assertRaises(ValueError):
            metadata.resolve_profiles(registry)

    def test_actual_pilot_covers_all_twelve_ports_in_six_groups(self):
        pieces = self.pilot["pieces"]
        self.assertEqual(set(pieces), set(PILOT_IDS))
        self.assertEqual(self.pilot["status"], "metadata_validated")
        self.assertEqual(sum(len(piece["groups"]) for piece in pieces.values()), 6)
        self.assertEqual(sum(len(group["members"]) for piece in pieces.values() for group in piece["groups"]), 12)
        for slug, piece in pieces.items():
            actual = [port["source_port_id"] for group in piece["groups"] for port in group["members"]]
            expected = [port["id"] for port in self.raw[slug]["connections"]["ports"]]
            self.assertCountEqual(actual, expected)
            self.assertEqual(len(actual), len(set(actual)))
            planner_ids = [port["id"] for group in piece["groups"] for port in group["members"]]
            self.assertEqual(len(planner_ids), len(set(planner_ids)))
            self.assertTrue(set(planner_ids).isdisjoint(expected))

    def test_public_journeys_and_forbidden_transfers_use_planner_ids(self):
        for slug, piece in self.pilot["pieces"].items():
            source = self.raw[slug]["connections"]
            names = {port["source_port_id"]: port["id"] for group in piece["groups"] for port in group["members"]}
            legacy_fields = {"compatible_counterparts", "transposed_compatible_counterparts",
                             "candidate_counterpart_count", "counterpart_list_scope"}
            expected = deepcopy(source)
            for port in expected["ports"]:
                for name in legacy_fields:
                    port.pop(name, None)
            actual = deepcopy(piece["connections"])
            self.assertIn("compatibility_policy", actual)
            for name in ("purpose", "compatibility_policy"):
                actual.pop(name, None)
                expected.pop(name, None)
            self.assertEqual(actual, expected)
            for group in piece["groups"]:
                for member in group["members"]:
                    self.assertTrue(legacy_fields.isdisjoint(member))
            self.assertEqual(len(piece["journeys"]), len(source["journeys"]))
            for actual, original in zip(piece["journeys"], source["journeys"]):
                self.assertEqual(actual["entry_port"], names[original["entry_port"]])
                self.assertEqual(actual["exit_port"], names[original["exit_port"]])
                self.assertEqual(actual["source_entry_port"], original["entry_port"])
                self.assertEqual(actual["source_exit_port"], original["exit_port"])
                self.assertEqual(actual["source_id"], original["id"])
                self.assertEqual(actual["id"], actual["entry_port"]+">"+actual["exit_port"])
            self.assertEqual(len(piece["forbidden_transfers"]), len(source["forbidden_transfers"]))
            for actual, original in zip(piece["forbidden_transfers"], source["forbidden_transfers"]):
                self.assertEqual(actual["from_port"], names[original["from_port"]])
                self.assertEqual(actual["to_port"], names[original["to_port"]])
                self.assertEqual(actual["source_from_port"], original["from_port"])
                self.assertEqual(actual["source_to_port"], original["to_port"])

    def test_unknown_port_is_rejected(self):
        groups = deepcopy(self.raw[CROSSING]["groups"])
        groups["groups"][0]["members"][0]["source_port_id"] = "nonexistent-port"
        with self.assertRaises(ValueError):
            self.validate(CROSSING, groups=groups)

    def test_published_structural_schema_runs_before_semantic_validation(self):
        for change in ('extra-member-field', 'invalid-id', 'missing-purpose'):
            with self.subTest(change=change):
                groups = deepcopy(self.raw[CROSSING]['groups'])
                if change == 'extra-member-field':
                    groups['groups'][0]['members'][0]['unexpected'] = True
                elif change == 'invalid-id':
                    groups['groups'][0]['members'][0]['id'] = 'INVALID ID'
                else:
                    del groups['purpose']
                with self.assertRaises(ValueError):
                    self.validate(CROSSING, groups=groups)

    def test_optional_profiles_can_be_omitted_without_changing_geometry(self):
        for slug in PILOT_IDS:
            with self.subTest(piece=slug):
                groups = deepcopy(self.raw[slug]['groups'])
                for group in groups['groups']:
                    group.pop('profile_id')
                resolved = self.validate(slug, groups=groups, profiles={})
                original = self.pilot['pieces'][slug]
                self.assertEqual(resolved['cells'], original['cells'])
                self.assertEqual(resolved['boundary_bundles'], original['boundary_bundles'])
                self.assertEqual([group['id'] for group in resolved['groups']], [group['id'] for group in original['groups']])
                for actual, expected in zip(resolved['groups'], original['groups']):
                    for key in ('anchor_m', 'tile_seam_center_m', 'outward_normal', 'members', 'channels'):
                        self.assertEqual(actual[key], expected[key], (slug, actual['id'], key))

    def test_contradictory_allowed_and_forbidden_journeys_are_rejected(self):
        connections = deepcopy(self.raw[CORNER]['connections'])
        connections['forbidden_transfers'][0]['to_port'] = 'Eout'
        with self.assertRaises(ValueError):
            self.validate(CORNER, connections=connections)

    def test_unknown_channel_and_conflicting_cut_associations_are_rejected(self):
        for failure in ('unknown-channel', 'wrong-cut'):
            groups = deepcopy(self.raw[CORNER]['groups'])
            first, second = groups['groups'][0]['members']
            if failure == 'unknown-channel':
                first['channel_id'] = 'absent-channel'
            else:
                second['channel_id'], second['cut_id'] = first['channel_id'], first['cut_id']
            with self.subTest(failure=failure), self.assertRaises(ValueError):
                self.validate(CORNER, groups=groups)

    def test_double_port_membership_is_rejected(self):
        groups = deepcopy(self.raw[CROSSING]["groups"])
        groups["groups"][1]["members"][0]["source_port_id"] = groups["groups"][0]["members"][0]["source_port_id"]
        with self.assertRaises(ValueError):
            self.validate(CROSSING, groups=groups)

    def test_duplicate_planner_member_id_is_rejected(self):
        groups = deepcopy(self.raw[CROSSING]["groups"])
        groups["groups"][1]["members"][0]["id"] = groups["groups"][0]["members"][0]["id"]
        with self.assertRaises(ValueError):
            self.validate(CROSSING, groups=groups)

    def test_planner_member_direction_must_match_source(self):
        groups = deepcopy(self.raw[CROSSING]["groups"])
        member = groups["groups"][0]["members"][0]
        member["direction"] = "out" if member["direction"] == "in" else "in"
        with self.assertRaises(ValueError):
            self.validate(CROSSING, groups=groups)

    def test_schema_one_string_members_are_not_accepted(self):
        groups = deepcopy(self.raw[CROSSING]["groups"])
        groups["schema_version"] = 1
        for group in groups["groups"]:
            group["members"] = [member["source_port_id"] for member in group["members"]]
        with self.assertRaises(ValueError):
            self.validate(CROSSING, groups=groups)

    def test_uncovered_primary_ports_are_rejected(self):
        groups = deepcopy(self.raw[CROSSING]["groups"])
        removed = groups["groups"].pop()
        groups["boundary_bundles"] = [bundle for bundle in groups["boundary_bundles"] if removed["id"] not in bundle["connector_ids"]]
        with self.assertRaises(ValueError):
            self.validate(CROSSING, groups=groups)

    def test_profile_at_wrong_height_is_rejected(self):
        groups = deepcopy(self.raw[CORNER]["groups"])
        groups["groups"][1]["profile_id"] = "hsr-l4-orth-scp-paired15-t2-opposed-rhd-v1"
        with self.assertRaises(ValueError):
            self.validate(CORNER, groups=groups)

    def test_different_edges_on_same_cell_cannot_share_boundary_bundle(self):
        groups = deepcopy(self.raw[CROSSING]["groups"])
        south = next(bundle for bundle in groups["boundary_bundles"] if bundle["edge"] == "south")
        east = next(bundle for bundle in groups["boundary_bundles"] if bundle["edge"] == "east")
        south["connector_ids"].extend(east["connector_ids"])
        groups["boundary_bundles"].remove(east)
        with self.assertRaises(ValueError):
            self.validate(CROSSING, groups=groups)

    def test_wrong_source_cell_is_rejected(self):
        groups = deepcopy(self.raw[CORNER]["groups"])
        groups["boundary_bundles"][0]["source_cell"] = [0, 0]
        with self.assertRaises(ValueError):
            self.validate(CORNER, groups=groups)

    def test_owned_neighbour_makes_boundary_internal_in_every_direction(self):
        # Synthetic masks move the original cell when needed to keep indices nonnegative.
        cases = {
            "north": ([1, 2], [0, 1], [0, 0]),
            "south": ([1, 2], [0, 0], [0, 1]),
            "west": ([2, 1], [1, 0], [0, 0]),
            "east": ([2, 1], [0, 0], [1, 0]),
        }
        for edge, (footprint, original_cell, neighbour) in cases.items():
            with self.subTest(edge=edge):
                piece = deepcopy(self.raw[CROSSING]["piece"])
                connections = deepcopy(self.raw[CROSSING]["connections"])
                groups = deepcopy(self.raw[CROSSING]["groups"])
                piece["footprint"] = footprint
                piece["cells"] = [original_cell, neighbour]
                piece["tile_ids"].append("7f700000")
                for port in connections["ports"]:
                    port["endpoint_m"][0] += 16 * original_cell[0]
                    port["endpoint_m"][1] -= 16 * original_cell[1]
                for bundle in groups["boundary_bundles"]:
                    bundle["source_cell"] = list(original_cell)
                with self.assertRaisesRegex(ValueError, "internal|exposed"):
                    self.validate(CROSSING, piece=piece, connections=connections, groups=groups)

    def test_explicit_section_offset_accepts_shifted_pair_without_changing_source(self):
        original = deepcopy(self.raw[CORNER])
        connections = deepcopy(original["connections"])
        groups = deepcopy(original["groups"])
        for port in connections["ports"]:
            if port["id"] in {"Sin", "Sout"}:
                port["endpoint_m"][0] += 1.0
        south = next(group for group in groups["groups"] if group["id"] == "curve-end-a")
        south["section_offset_m"] = 1.0
        validated = self.validate(CORNER, connections=connections, groups=groups)
        shifted = next(group for group in validated["groups"] if group["id"] == "curve-end-a")
        self.assertEqual(shifted["anchor_m"], [1.0, -56.0, 30.5])
        self.assertEqual({port["section_offset_m"] for port in shifted["members"]}, {-2., 2.})
        self.assertEqual(self.raw[CORNER], original)

    def test_loading_is_read_only_for_authoritative_piece_records(self):
        paths = [CUSTOM_ROOT / DOMAIN / "00_pieces" / slug / filename for slug in PILOT_IDS for filename in ("piece.json", "connections.json", "checks/manual-tests.json")]
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
        metadata.load_library(CUSTOM_ROOT, PILOT_IDS)
        self.assertEqual(before, {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths})

    def test_source_binding_detects_even_prose_only_source_change(self):
        relatives = [Path("project.json"), DOMAIN / "domain.json", DOMAIN / "connector-profiles.json"]
        relatives.extend(DOMAIN / "00_pieces" / slug / filename for slug in PILOT_IDS for filename in ("piece.json", "connections.json", "connector-groups.jsonc"))
        with tempfile.TemporaryDirectory(prefix="scp-planner-binding-") as temporary:
            root = Path(temporary)
            for relative in relatives:
                destination = root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(CUSTOM_ROOT / relative, destination)
            self.assertEqual(metadata.load_library(root, PILOT_IDS)["status"], "metadata_validated")
            piece_path = root / DOMAIN / "00_pieces" / CROSSING / "piece.json"
            changed = read_json(piece_path)
            changed["purpose"] += " Source-binding regression fixture."
            piece_path.write_text(json.dumps(changed))
            with self.assertRaises(ValueError):
                metadata.load_library(root, PILOT_IDS)

    def test_profile_reference_rejects_absolute_and_parent_traversal_paths(self):
        relatives = [Path("project.json"), DOMAIN / "domain.json", DOMAIN / "connector-profiles.json"]
        relatives.extend(DOMAIN / "00_pieces" / slug / filename for slug in PILOT_IDS for filename in ("piece.json", "connections.json", "connector-groups.jsonc"))
        with tempfile.TemporaryDirectory(prefix="scp-planner-path-") as temporary:
            root = Path(temporary)
            for relative in relatives:
                destination = root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(CUSTOM_ROOT / relative, destination)
            self.assertEqual(metadata.load_library(root, PILOT_IDS)["status"], "metadata_validated")
            domain_path = root / DOMAIN / "domain.json"
            original = read_json(domain_path)
            for unsafe in (str(root / DOMAIN / "connector-profiles.json"), "../high-speed-rail/connector-profiles.json"):
                with self.subTest(path=unsafe):
                    altered = deepcopy(original)
                    altered["connector_profiles"] = unsafe
                    domain_path.write_text(json.dumps(altered))
                    with self.assertRaises(ValueError):
                        metadata.load_library(root, PILOT_IDS)

    def test_legacy_json_sidecar_is_not_a_fallback(self):
        relatives = [DOMAIN / "domain.json", DOMAIN / "connector-profiles.json"]
        relatives.extend(DOMAIN / "00_pieces" / slug / filename for slug in PILOT_IDS for filename in ("piece.json", "connections.json", "connector-groups.jsonc"))
        with tempfile.TemporaryDirectory(prefix="scp-planner-no-fallback-") as temporary:
            root = Path(temporary)
            for relative in relatives:
                destination = root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(CUSTOM_ROOT / relative, destination)
            sidecar = root / DOMAIN / "00_pieces" / CROSSING / "connector-groups.jsonc"
            sidecar.with_suffix(".json").write_text(json.dumps(jsonc.load(sidecar)))
            sidecar.unlink()
            with self.assertRaises(FileNotFoundError):
                metadata.load_library(root, PILOT_IDS)


if __name__ == "__main__":
    unittest.main()
