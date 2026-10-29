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


CUSTOM_ROOT = next(parent for parent in Path(__file__).resolve().parents if (parent / "project.jsonc").is_file())
DOMAIN = Path("domains/high-speed-rail")
CROSSING = "hsr-l4-over-hsr-l2-two-track-crossing-90deg"
CORNER = "hsr-h23000mm-and-l4-two-track-curve-ramp-90deg-tight"
PILOT_IDS = [CROSSING, CORNER]
sys.path.insert(0, str(CUSTOM_ROOT / "framework"))

from scp import connector_metadata as metadata
from scp import jsonc
from connector_source_fixture import write_connector_source_fixture


def read_json(path):
    return jsonc.load(path) if path.suffix == ".jsonc" else json.loads(path.read_text())


class ConnectorSourceRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        temporary = tempfile.TemporaryDirectory(prefix='scp-synthetic-source-contracts-')
        cls.addClassCleanup(temporary.cleanup)
        identifiers = PILOT_IDS + ['hsr-l2-mixed-fan-compact-recessed-web',
                                  'hsr-l2-two-track-mainline-opposed-merges-oblique-cuts']
        cls.fixture_root = write_connector_source_fixture(temporary.name, identifiers, source_root=CUSTOM_ROOT)
        cls.registry = read_json(CUSTOM_ROOT / DOMAIN / "connector-profiles.jsonc")
        cls.profiles = metadata.resolve_profiles(cls.registry)
        cls.raw = {}
        for slug in PILOT_IDS:
            directory = cls.fixture_root / DOMAIN / "00_pieces" / slug
            cls.raw[slug] = {name: read_json(directory / filename) for name, filename in (
                ("piece", "piece.json"), ("connections", "connections.json"), ("groups", "connector-groups.jsonc"))}
        cls.pilot = metadata.load_library(cls.fixture_root, PILOT_IDS)

    def validate(self, slug, *, piece=None, connections=None, groups=None, profiles=None):
        raw = self.raw[slug]
        return metadata.validate_piece(
            deepcopy(raw["piece"] if piece is None else piece),
            deepcopy(raw["connections"] if connections is None else connections),
            deepcopy(raw["groups"] if groups is None else groups),
            deepcopy(self.profiles if profiles is None else profiles),
        )

    def test_trumpet_sources_preserve_complete_measured_ends_and_physical_channels(self):
        expected = {
            "hsr-l2-mixed-fan-compact-recessed-web": {
                "Nin": "north-to-west-track", "Wout": "north-to-west-track",
                "Ein": "east-to-north-track", "Nout": "east-to-north-track"},
            "hsr-l2-two-track-mainline-opposed-merges-oblique-cuts": {
                "Win": "eastbound-mainline", "Eout": "eastbound-mainline",
                "Ein": "westbound-mainline", "Wout": "westbound-mainline",
                "Nin": "north-branch", "Sin": "south-branch"},
        }
        resolved = metadata.load_library(self.fixture_root, list(expected))["pieces"]
        for slug, channels in expected.items():
            with self.subTest(piece=slug):
                piece = resolved[slug]
                ports = {port["id"]: port for port in piece["connections"]["ports"]}
                members = [member for group in piece["groups"] for member in group["members"]]
                self.assertEqual({member["source_port_id"]: member["channel_id"] for member in members}, channels)
                self.assertEqual(len(members), len(ports))
                self.assertEqual({member["source_port_id"] for member in members}, set(ports))
                for member in members:
                    self.assertEqual(member["endpoint_m"], ports[member["source_port_id"]]["endpoint_m"])
                    self.assertEqual(member["tangent"], ports[member["source_port_id"]]["tangent"])
                    self.assertEqual(member["traffic_modes"], ["monorail"])
                self.assertTrue(all(group["construction_network"] == "monorail" for group in piece["groups"]))

    def test_trumpet_curved_cuts_do_not_invent_paired_profiles_or_section_origins(self):
        slugs = ["hsr-l2-mixed-fan-compact-recessed-web", "hsr-l2-two-track-mainline-opposed-merges-oblique-cuts"]
        resolved = metadata.load_library(self.fixture_root, slugs)["pieces"]
        for slug in slugs:
            with self.subTest(piece=slug):
                groups = resolved[slug]["groups"]
                curved = [group for group in groups if group["id"].endswith("curved-cut")]
                paired = [group for group in groups if group["id"].endswith("paired-end")]
                self.assertEqual(len(curved), 2)
                for group in curved:
                    self.assertEqual(group["nominal_level"], "l2")
                    self.assertIsNone(group.get("profile_id"))
                    self.assertIsNone(group["section_offset_m"])
                    self.assertIsNone(group["anchor_m"])
                    self.assertEqual(len(group["members"]), 1)
                    self.assertIsNone(group["members"][0]["section_offset_m"])
                    self.assertNotEqual(group["members"][0]["heading_outward_degrees"] % 90, 0)
                for group in paired:
                    expected_profile = ("hsr-l2-paired-recessed-web15-t2-opposed-rhd-v1"
                                        if slug == "hsr-l2-mixed-fan-compact-recessed-web"
                                        else "hsr-l2-orth-scp-paired15-t2-opposed-rhd-v1")
                    self.assertEqual(group["profile_id"], expected_profile)
                    self.assertEqual(group["section_offset_m"], 0)
                    self.assertIsNotNone(group["anchor_m"])
                    self.assertEqual(len(group["members"]), 2)

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

    def test_source_geometry_fixture_covers_all_twelve_ports_in_six_groups(self):
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

    def test_omitted_section_origin_stays_unknown_even_with_a_paired_profile(self):
        groups = deepcopy(self.raw[CROSSING]['groups'])
        groups['groups'][0].pop('section_offset_m')
        resolved = self.validate(CROSSING, groups=groups)['groups'][0]
        self.assertIsNone(resolved['section_offset_m'])
        self.assertIsNone(resolved['anchor_m'])
        self.assertTrue(all(member['section_offset_m'] is None for member in resolved['members']))
        self.assertEqual(resolved['profile']['path_height_m'], 30.5)
        baseline = self.validate(CROSSING)['groups'][0]
        self.assertEqual(baseline['section_offset_m'], 0.)
        for actual, original in zip(resolved['members'], baseline['members']):
            self.assertEqual(actual['endpoint_m'], original['endpoint_m'])
            self.assertEqual(actual['outward_tangent'], original['outward_tangent'])
            self.assertEqual(actual['grade_outward'], original['grade_outward'])

    def test_single_angled_cut_without_section_origin_preserves_actual_geometry(self):
        # Synthetic one-track subset tests source-format semantics; it is not
        # a declaration or a compatibility claim for the real paired curve.
        source = deepcopy(self.raw[CORNER])
        keep = {'Sin', 'Eout'}
        source['connections']['ports'] = [port for port in source['connections']['ports'] if port['id'] in keep]
        source['connections']['journeys'] = [journey for journey in source['connections']['journeys']
            if journey['entry_port'] in keep and journey['exit_port'] in keep]
        source['connections']['forbidden_transfers'] = []
        source['groups']['channels'] = source['groups']['channels'][:1]
        for group in source['groups']['groups']:
            group.pop('section_offset_m')
            group.pop('profile_id')
            group['members'] = [member for member in group['members'] if member['source_port_id'] in keep]
        port = next(port for port in source['connections']['ports'] if port['id'] == 'Eout')
        port['tangent'] = [2**-.5, 2**-.5]
        result = self.validate(CORNER, connections=source['connections'], groups=source['groups'])
        end = result['groups'][1]
        self.assertEqual(end['profile']['alignment'], 'angled')
        self.assertIsNone(end['anchor_m'])
        self.assertIsNone(end['section_offset_m'])
        self.assertEqual(end['members'][0]['endpoint_m'], port['endpoint_m'])
        self.assertEqual(end['members'][0]['tangent'], port['tangent'])
        self.assertIsNone(end['members'][0]['section_offset_m'])
        source['groups']['groups'][1]['section_offset_m'] = 0.
        explicit = self.validate(CORNER, connections=source['connections'], groups=source['groups'])['groups'][1]
        self.assertEqual(explicit['anchor_m'], [56., 0., 23.])
        self.assertEqual(explicit['section_offset_m'], 0.)
        self.assertEqual(explicit['members'][0]['endpoint_m'], port['endpoint_m'])
        self.assertEqual(explicit['members'][0]['tangent'], port['tangent'])

    def test_loading_is_read_only_for_temporary_piece_records(self):
        paths = [self.fixture_root / DOMAIN / "00_pieces" / slug / filename for slug in PILOT_IDS for filename in ("piece.json", "connections.json", "checks/manual-tests.json")]
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
        metadata.load_library(self.fixture_root, PILOT_IDS)
        self.assertEqual(before, {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths})

    def test_source_binding_detects_even_prose_only_source_change(self):
        relatives = [Path("project.jsonc"), DOMAIN / "domain.jsonc", DOMAIN / "connector-profiles.jsonc"]
        relatives.extend(DOMAIN / "00_pieces" / slug / filename for slug in PILOT_IDS for filename in ("piece.json", "connections.json", "connector-groups.jsonc"))
        with tempfile.TemporaryDirectory(prefix="scp-planner-binding-") as temporary:
            root = Path(temporary)
            for relative in relatives:
                destination = root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(self.fixture_root / relative, destination)
            self.assertEqual(metadata.load_library(root, PILOT_IDS)["status"], "metadata_validated")
            piece_path = root / DOMAIN / "00_pieces" / CROSSING / "piece.json"
            changed = read_json(piece_path)
            changed["purpose"] += " Source-binding regression fixture."
            piece_path.write_text(json.dumps(changed))
            with self.assertRaises(ValueError):
                metadata.load_library(root, PILOT_IDS)

    def test_profile_reference_rejects_absolute_and_parent_traversal_paths(self):
        relatives = [Path("project.jsonc"), DOMAIN / "domain.jsonc", DOMAIN / "connector-profiles.jsonc"]
        relatives.extend(DOMAIN / "00_pieces" / slug / filename for slug in PILOT_IDS for filename in ("piece.json", "connections.json", "connector-groups.jsonc"))
        with tempfile.TemporaryDirectory(prefix="scp-planner-path-") as temporary:
            root = Path(temporary)
            for relative in relatives:
                destination = root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(self.fixture_root / relative, destination)
            self.assertEqual(metadata.load_library(root, PILOT_IDS)["status"], "metadata_validated")
            domain_path = root / DOMAIN / "domain.jsonc"
            original = read_json(domain_path)
            for unsafe in (str(root / DOMAIN / "connector-profiles.jsonc"), "../high-speed-rail/connector-profiles.jsonc"):
                with self.subTest(path=unsafe):
                    altered = deepcopy(original)
                    altered["connector_profiles"] = unsafe
                    domain_path.write_text(json.dumps(altered))
                    with self.assertRaises(ValueError):
                        metadata.load_library(root, PILOT_IDS)

    def test_legacy_json_sidecar_is_not_a_fallback(self):
        relatives = [DOMAIN / "domain.jsonc", DOMAIN / "connector-profiles.jsonc"]
        relatives.extend(DOMAIN / "00_pieces" / slug / filename for slug in PILOT_IDS for filename in ("piece.json", "connections.json", "connector-groups.jsonc"))
        with tempfile.TemporaryDirectory(prefix="scp-planner-no-fallback-") as temporary:
            root = Path(temporary)
            for relative in relatives:
                destination = root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(self.fixture_root / relative, destination)
            sidecar = root / DOMAIN / "00_pieces" / CROSSING / "connector-groups.jsonc"
            sidecar.with_suffix(".json").write_text(json.dumps(jsonc.load(sidecar)))
            sidecar.unlink()
            with self.assertRaises(FileNotFoundError):
                metadata.load_library(root, PILOT_IDS)


if __name__ == "__main__":
    unittest.main()
