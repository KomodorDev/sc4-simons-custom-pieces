"""Runtime sidewalk PATH dependencies cannot replace canonical source cells."""
from collections import defaultdict
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

from scp import jsonc
from scp.connector_metadata import validate_piece


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "domains/highway/00_pieces"

# Explicit physical channel associations for these saved source fixtures. A
# split or merge retains a separate ramp channel, including its single cut.
CHANNELS = {
    "access-core": [
        ("upper-mainline", ["1-W-in-4", "1-N-out-16"]),
        ("upper-mainline", ["1-W-in-6", "1-N-out-13"]),
        ("lower-mainline", ["1-N-in-12", "1-W-out-5"]),
        ("lower-mainline", ["1-N-in-15", "1-W-out-3"]),
        ("avenue-mainline", ["1-N-in-1", "1-E-out-9"]),
        ("avenue-mainline", ["1-N-in-2", "1-E-out-10"]),
        ("avenue-mainline", ["1-S-in-11", "1-W-out-7"]),
        ("avenue-mainline", ["1-S-in-14", "1-W-out-8"]),
        ("avenue-walkways", ["2-N-in-1", "2-E-out-3"]),
        ("avenue-walkways", ["2-S-in-4", "2-W-out-2"]),
    ],
    "northwest-junction": [
        ("avenue-mainline", ["1-W-in-1", "1-S-out-6"]),
        ("avenue-mainline", ["1-W-in-2", "1-S-out-7"]),
        ("avenue-mainline", ["1-E-in-8", "1-N-out-3"]),
        ("avenue-mainline", ["1-E-in-9", "1-N-out-5"]),
        ("avenue-mainline", ["1-S-out-4"]),
        ("avenue-mainline", ["1-E-in-10"]),
        ("avenue-walkways", ["2-W-in-1", "2-S-out-3"]),
        ("avenue-walkways", ["2-E-in-4", "2-N-out-2"]),
    ],
    "southeast-junction": [
        ("avenue-mainline", ["1-W-in-2", "1-E-out-7"]),
        ("avenue-mainline", ["1-W-in-3", "1-E-out-8"]),
        ("avenue-mainline", ["1-S-in-9", "1-N-out-4"]),
        ("avenue-mainline", ["1-S-in-10", "1-N-out-5"]),
        ("avenue-mainline", ["1-W-in-1"]),
        ("avenue-mainline", ["1-N-out-6"]),
        ("avenue-walkways", ["2-W-in-1", "2-E-out-3"]),
        ("avenue-walkways", ["2-S-in-4", "2-N-out-2"]),
    ],
}


def source_fixture(key):
    """Keep real source bytes; construct only the previously absent sidecar."""
    identifier = "ddrhw-diagonal-" + key
    directory = DIRECTORY / identifier
    piece = jsonc.load(directory / "piece.jsonc")
    connections = json.loads((directory / "connections.json").read_text())
    channels, associations = [], {}
    for number, (component, names) in enumerate(CHANNELS[key], 1):
        channel = "channel-" + str(number)
        pedestrian = component == "avenue-walkways"
        channels.append({"id": channel, "component_id": component,
                         "kind": "walkway" if pedestrian else "road-lane",
                         "traffic_modes": ["pedestrian" if pedestrian else "car"]})
        for name in names:
            assert name not in associations
            associations[name] = component, channel
    ports = {port["id"]: port for port in connections["ports"]}
    assert associations.keys() == ports.keys()
    boundaries = defaultdict(lambda: defaultdict(list))
    for name, port in ports.items():
        source, = port["boundary_sources"]
        component, _ = associations[name]
        boundaries[tuple(source["cell"]), source["edge"]][component].append(name)
    groups, bundles, member_number = [], [], 0
    for boundary_number, ((cell, edge), parts) in enumerate(sorted(boundaries.items()), 1):
        bundle = {"id": f"boundary-{boundary_number}", "source_cell": list(cell),
                  "edge": ("west", "north", "east", "south")[edge], "connector_ids": []}
        for component, names in sorted(parts.items()):
            group = {"id": f"group-{len(groups) + 1}", "component_id": component, "members": []}
            for name in names:
                member_number += 1
                group["members"].append({"id": f"member-{member_number}", "source_port_id": name,
                                         "direction": ports[name]["direction"],
                                         "channel_id": associations[name][1], "cut_id": f"cut-{member_number}"})
            groups.append(group)
            bundle["connector_ids"].append(group["id"])
        bundles.append(bundle)
    components = [{"id": component, "network": "pedestrian" if component == "avenue-walkways" else "road"}
                  for component in sorted({component for component, _ in CHANNELS[key]})]
    groups = {"schema_version": 3, "purpose": "Test actual adaptive source PATH dependency separation.",
              "piece_id": identifier, "source_binding": {
                  "piece_sha256": hashlib.sha256((directory / "piece.jsonc").read_bytes()).hexdigest(),
                  "connections_sha256": hashlib.sha256((directory / "connections.json").read_bytes()).hexdigest()},
              "components": components, "channels": channels, "groups": groups, "boundary_bundles": bundles}
    return piece, connections, groups


class AdaptiveConnectorPathTests(unittest.TestCase):
    def setUp(self):
        self.piece, self.connections, self.groups = source_fixture("access-core")
        self.port = self.connections["ports"][0]
        prefix = "path:" + self.piece["id"] + ":"
        self.canonical = next(key for key in self.port["resource_keys"]
                              if key.startswith(prefix + "296678f7-a966883f-"))
        self.alias = next(key for key in self.port["resource_keys"]
                          if key.startswith(prefix + "296678f7-69668828-"))

    def validate(self):
        return validate_piece(self.piece, self.connections, self.groups, {})

    def replace_key(self, old, new):
        keys = self.port["resource_keys"]
        keys[keys.index(old)] = new

    def test_actual_core_and_junction_dependencies_preserve_every_source_fact(self):
        for key, counts in (("access-core", (20, 10, 90, 12)),
                            ("northwest-junction", (14, 8, 41, 10)),
                            ("southeast-junction", (14, 8, 41, 10))):
            with self.subTest(piece=key):
                piece, connections, groups = source_fixture(key)
                before = deepcopy((piece, connections, groups))
                resolved = validate_piece(piece, connections, groups, {})
                self.assertEqual((piece, connections, groups), before)
                self.assertEqual((len(resolved["connections"]["ports"]), len(resolved["journeys"]),
                                  len(resolved["forbidden_transfers"]), len(resolved["groups"])), counts)
                self.assertEqual(resolved["connections"]["source"], connections["source"])
                for original, retained in zip(connections["ports"], resolved["connections"]["ports"]):
                    self.assertEqual(original["resource_keys"], retained["resource_keys"])

    def test_unowned_canonical_path_is_rejected(self):
        self.replace_key(self.canonical, self.canonical.rsplit("-", 1)[0] + "-7fffffff")
        with self.assertRaisesRegex(ValueError, "not owned"):
            self.validate()

    def test_owned_canonical_path_from_another_source_cell_is_rejected(self):
        other = next(tile for tile in self.piece["tile_ids"] if not self.canonical.endswith("-" + tile))
        self.replace_key(self.canonical, self.canonical.rsplit("-", 1)[0] + "-" + other)
        with self.assertRaisesRegex(ValueError, "source cell differs"):
            self.validate()

    def test_alias_dependencies_cannot_replace_the_canonical_path(self):
        self.port["resource_keys"].remove(self.canonical)
        with self.assertRaisesRegex(ValueError, "source cell differs"):
            self.validate()

    def test_fingerprinted_alias_in_an_unknown_group_is_rejected(self):
        forged = self.alias.replace("-69668828-", "-deadbeef-")
        self.replace_key(self.alias, forged)
        fingerprints = self.connections["source"]["resource_fingerprints"]
        fingerprints[forged] = fingerprints[self.alias]
        with self.assertRaisesRegex(ValueError, "not a declared adaptive binding"):
            self.validate()

    def test_fingerprinted_alias_without_a_declared_resolved_tile_is_rejected(self):
        forged = self.alias.rsplit("-", 1)[0] + "-7fffff00"
        self.replace_key(self.alias, forged)
        fingerprints = self.connections["source"]["resource_fingerprints"]
        fingerprints[forged] = fingerprints[self.alias]
        with self.assertRaisesRegex(ValueError, "not a declared adaptive binding"):
            self.validate()

    def test_alias_binding_without_saved_resource_fingerprint_is_rejected(self):
        del self.connections["source"]["resource_fingerprints"][self.alias]
        with self.assertRaisesRegex(ValueError, "lacks a saved resource fingerprint"):
            self.validate()

    def test_alias_binding_with_invalid_saved_fingerprint_is_rejected(self):
        self.connections["source"]["resource_fingerprints"][self.alias] = "unverified"
        with self.assertRaisesRegex(ValueError, "lacks a saved resource fingerprint"):
            self.validate()

    def test_alias_dependencies_require_the_owning_piece_binding(self):
        del self.piece["adaptive_ground"]
        with self.assertRaisesRegex(ValueError, "not a declared adaptive binding"):
            self.validate()

    def test_another_piece_path_cannot_be_an_ignored_dependency(self):
        forged = self.alias.replace(self.piece["id"], "unrelated-piece")
        self.replace_key(self.alias, forged)
        with self.assertRaisesRegex(ValueError, "belongs to another piece"):
            self.validate()


if __name__ == "__main__":
    unittest.main()
