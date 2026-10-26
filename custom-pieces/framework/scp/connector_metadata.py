"""Resolve and validate source-owned boundary/channel descriptions.

Profiles supply optional authoring defaults; matching never confirms physical seams,
construction clearance, model collisions, or operation inside SimCity 4.
"""
from copy import deepcopy
from functools import wraps
import hashlib
import json
import math
from pathlib import Path
import re

from . import jsonc
from importlib import resources

EPS = 2e-5
ROTATIONS = (0, 90, 180, 270)
NORMALS = {"west": (-1., 0.), "north": (0., 1.), "east": (1., 0.), "south": (0., -1.)}
EDGES = {"west": 0, "north": 1, "east": 2, "south": 3}
LIMITATIONS = ["physical_seams", "construction_clearance", "geometry_collisions", "in_game"]


class ConnectorDataError(ValueError):
    """A source-owned export failure with a stable code for consumers.

    Consumers must exclude these inputs rather than treating them as an
    incompatible piece or regenerating missing authoring data themselves.
    """
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def _export_need(condition, message, code="invalid_export"):
    if not condition:
        raise ConnectorDataError(code, message)


def _export_validated(function):
    @wraps(function)
    def checked(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ConnectorDataError:
            raise
        except OSError as error:
            raise ConnectorDataError("missing_source", str(error)) from error
        except (ValueError, KeyError, TypeError, IndexError, AttributeError, OverflowError) as error:
            raise ConnectorDataError("invalid_export", str(error)) from error
    return checked


def _need(condition, message):
    if not condition:
        raise ValueError(message)


def _validated(function):
    @wraps(function)
    def checked(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except (KeyError, TypeError, IndexError, AttributeError, OverflowError) as error:
            raise ValueError(f"Malformed {function.__name__} metadata: {error}") from error
    return checked


def _number(value):
    return type(value) in (int, float) and math.isfinite(value)


def _vector(value, size):
    return isinstance(value, (list, tuple)) and len(value) == size and all(_number(x) for x in value)


def _safe_relative(root, name):
    _need(isinstance(name, str) and name and "\\" not in name and not Path(name).is_absolute(), "Expected a relative source path")
    _need(".." not in Path(name).parts, "Parent traversal is not allowed")
    target = (root / name).resolve()
    _need(target.is_relative_to(root.resolve()), "Source path escapes its owning directory")
    return target


def _close(a, b):
    return len(a) == len(b) and math.dist(a, b) <= EPS


def rotate(point, degrees):
    """Rotate east/north coordinates counterclockwise, preserving any height."""
    _need(degrees in ROTATIONS, "Rotation must be 0, 90, 180, or 270 degrees")
    result = list(point)
    for _ in range(degrees // 90):
        result[0], result[1] = -result[1], result[0]
    return result


def _schema(name):
    source = Path(__file__).resolve().parents[2] / "schemas" / name
    if source.is_file():
        return jsonc.loads(source.read_text())
    return jsonc.loads(resources.files("scp.schemas").joinpath(name).read_text())


def validate_structure(value, schema, location="$", document=None):
    """Enforce the JSON Schema subset used by SCP's three published schemas.

    Structural validation runs before semantic cross-file validation. Definitions,
    required/extra fields, types, finite numbers, IDs, and array constraints are
    checked by the same schema files shipped in source exports and packages.
    """
    document = document or schema
    supported = {"$schema", "$ref", "$defs", "title", "description", "type", "properties", "required", "additionalProperties", "items", "minItems", "maxItems", "uniqueItems", "minProperties", "propertyNames", "minLength", "pattern", "minimum", "exclusiveMinimum", "const", "enum"}
    _need(set(schema) <= supported, f"{location}: unsupported schema keyword {set(schema)-supported}")
    if "$ref" in schema:
        target = document
        for key in schema["$ref"].removeprefix("#/").split("/"):
            target = target[key]
        return validate_structure(value, target, location, document)
    types = schema.get("type", [])
    types = [types] if isinstance(types, str) else types
    checks = {"object": isinstance(value, dict), "array": isinstance(value, list),
              "string": isinstance(value, str), "integer": type(value) is int,
              "number": _number(value), "boolean": type(value) is bool, "null": value is None}
    _need(not types or any(checks[t] for t in types), f"{location}: expected {types}")
    if "const" in schema:
        _need(type(value) is type(schema["const"]) and value == schema["const"], f"{location}: incorrect constant")
    if "enum" in schema:
        _need(value in schema["enum"], f"{location}: value outside enumeration")
    if isinstance(value, dict):
        _need(len(value) >= schema.get("minProperties", 0), f"{location}: empty object")
        _need(all(key in value for key in schema.get("required", [])), f"{location}: missing required field")
        properties = schema.get("properties", {})
        for key, item in value.items():
            if "propertyNames" in schema:
                validate_structure(key, schema["propertyNames"], location+".key", document)
            rule = properties.get(key, schema.get("additionalProperties", True))
            _need(rule is not False, f"{location}: unexpected field {key}")
            if isinstance(rule, dict):
                validate_structure(item, rule, location+"."+key, document)
    if isinstance(value, list):
        _need(schema.get("minItems", 0) <= len(value) <= schema.get("maxItems", math.inf), f"{location}: invalid array length")
        if schema.get("uniqueItems"):
            _need(len({json.dumps(x, sort_keys=True) for x in value}) == len(value), f"{location}: duplicate items")
        for index, item in enumerate(value):
            if "items" in schema:
                validate_structure(item, schema["items"], f"{location}[{index}]", document)
    if isinstance(value, str):
        _need(len(value) >= schema.get("minLength", 0), f"{location}: empty string")
        _need("pattern" not in schema or re.search(schema["pattern"], value), f"{location}: invalid identifier or fingerprint")
    if _number(value):
        _need(value >= schema.get("minimum", -math.inf), f"{location}: value below minimum")
        _need(value > schema.get("exclusiveMinimum", -math.inf), f"{location}: value below exclusive minimum")


@_validated
def resolve_profiles(registry):
    """Resolve optional version-2 defaults, never a physical mesh contract."""
    validate_structure(registry, _schema("connector-profiles.schema.json"))
    raw, resolved, pending = registry["profiles"], {}, set()
    def visit(identifier):
        _need(identifier in raw, f"Unknown profile parent: {identifier}")
        _need(identifier not in pending, f"Profile inheritance cycle: {identifier}")
        if identifier in resolved:
            return resolved[identifier]
        pending.add(identifier)
        item = raw[identifier]
        value = deepcopy(visit(item["extends"])) if item.get("extends") else {}
        value.update(deepcopy(item))
        pending.remove(identifier)
        resolved[identifier] = value
        return value
    for identifier in raw:
        visit(identifier)
    return resolved


def _cells(piece):
    footprint = piece.get("footprint")
    _need(isinstance(footprint, list) and len(footprint) == 2 and all(type(x) is int and x > 0 for x in footprint), "Invalid footprint")
    width, depth = footprint
    cells = piece.get("cells", [[x, y] for y in range(depth) for x in range(width)])
    _need(isinstance(cells, list) and cells and all(isinstance(c, list) and len(c) == 2 and
          all(type(x) is int for x in c) and 0 <= c[0] < width and 0 <= c[1] < depth for c in cells), "Invalid occupied cells")
    _need(len({tuple(c) for c in cells}) == len(cells), "Duplicate occupied cells")
    return deepcopy(cells)


@_validated
def validate_piece(piece, connections, groups, profiles):
    """Resolve one sidecar; validate every endpoint, channel, cut, and journey.

    `groups` is the complete connector sidecar; `profiles` is resolve_profiles'
    output. Coordinates remain in the piece's canonical east/north/height frame.
    File hashes are checked separately by load_pilot, which has the raw bytes.
    """
    validate_structure(groups, _schema("connector-groups.schema.json"))
    # Old measured records retain their exact bytes and historical endpoint
    # shortlists. Current resolved data contains this piece's intrinsic facts;
    # neighbour discovery belongs to the separate complete-boundary consumer.
    connections = deepcopy(connections)
    for port in connections.get("ports", []):
        for key in ("compatible_counterparts", "transposed_compatible_counterparts",
                    "candidate_counterpart_count", "counterpart_list_scope"):
            port.pop(key, None)
    connections["purpose"] = "Intrinsic saved-resource endpoints, service roles, directed journeys, and forbidden transfers for one piece."
    connections["compatibility_policy"] = "Complete-boundary compatibility is computed separately from validated exports; no counterpart shortlist is included."
    identifier = piece["id"]
    _need(piece.get("schema_version") == 1 and connections.get("schema_version") == 1, "Unsupported piece or connection schema")
    _need(groups.get("schema_version") == 3 and groups.get("piece_id") == identifier, "Wrong connector schema or piece ID")
    _need(connections.get("subject_id") == identifier and connections.get("subject_kind") == "piece", "Wrong connection subject")
    cells = _cells(piece)
    owned_cells = {tuple(cell) for cell in cells}
    tiles = piece.get("tile_ids", [])
    _need(len(tiles) == len(cells) and len(set(tiles)) == len(tiles), "Tile/cell mapping is invalid")
    tile_cells = {int(tile, 16): tuple(cell) for tile, cell in zip(tiles, cells)}
    ports = {p["id"]: p for p in connections.get("ports", [])}
    _need(ports and len(ports) == len(connections["ports"]), "Missing or duplicate measured ports")
    components = groups.get("components", [])
    component_map = {x["id"]: x for x in components}
    _need(component_map and len(component_map) == len(components), "Missing or duplicate components")
    _need(all(isinstance(x, str) and x and isinstance(v.get("network"), str) and v["network"] for x, v in component_map.items()), "Invalid component ID or network")
    channels = {x["id"]: x for x in groups["channels"]}
    _need(len(channels) == len(groups["channels"]), "Duplicate physical channel IDs")
    for channel in channels.values():
        _need(channel.get("component_id") is None or channel["component_id"] in component_map, "Unknown channel component")
    raw_groups = groups.get("groups", [])
    by_id = {x["id"]: x for x in raw_groups}
    _need(by_id and len(by_id) == len(raw_groups), "Missing or duplicate connector groups")
    _need(all(isinstance(x, str) and x for x in by_id), "Connector group IDs must be nonempty strings")
    bundles = groups.get("boundary_bundles", [])
    _need(isinstance(bundles, list) and bundles, "Missing boundary bundles")
    bundle_ids, cuts, group_bundles = set(), set(), {}
    for bundle in bundles:
        _need(isinstance(bundle.get("id"), str) and bundle["id"] and bundle["id"] not in bundle_ids, "Duplicate or missing boundary ID")
        bundle_ids.add(bundle["id"])
        cell, edge = bundle.get("source_cell"), bundle.get("edge")
        _need(isinstance(cell, list) and len(cell) == 2 and all(type(x) is int for x in cell) and tuple(cell) in owned_cells, "Boundary source cell is not occupied")
        _need(edge in NORMALS, "Unknown boundary edge")
        normal = NORMALS[edge]
        neighbour = (cell[0]+int(normal[0]), cell[1]-int(normal[1]))
        _need(neighbour not in owned_cells, "Boundary edge is internal to occupied cells, not exposed")
        cut = (*cell, edge)
        _need(cut not in cuts, "A physical boundary must have one bundle")
        cuts.add(cut)
        connector_ids = bundle.get("connector_ids", [])
        _need(isinstance(connector_ids, list) and connector_ids, "Empty boundary bundle")
        for group_id in connector_ids:
            _need(group_id in by_id and group_id not in group_bundles, "Unknown or duplicate bundled connector")
            group_bundles[group_id] = bundle
    _need(set(group_bundles) == set(by_id), "Every connector group needs exactly one boundary bundle")
    planner_ids = set(component_map) | set(by_id) | bundle_ids | set(channels)
    _need(len(planner_ids) == len(component_map)+len(by_id)+len(bundle_ids)+len(channels), "Library IDs must be unique across components, groups and boundaries")
    resolved, covered, port_components, source_to_planner = [], set(), {}, {}
    for raw in raw_groups:
        group_id, profile_id = raw["id"], raw.get("profile_id")
        _need(profile_id is None or (profile_id in profiles and not profiles[profile_id].get("abstract", True)), f"Unknown or abstract profile: {profile_id}")
        component = component_map.get(raw.get("component_id"))
        _need(component is not None, "Unknown connector component")
        profile = deepcopy(profiles[profile_id]) if profile_id else {}
        _need(profile.get("network", component["network"]) == component["network"], "Connector component network differs from profile")
        profile.setdefault("network", component["network"])
        profile.setdefault("nominal_level", raw.get("nominal_level"))
        if "nominal_level" in raw:
            profile["nominal_level"] = raw["nominal_level"]
        members = raw.get("members", [])
        _need(isinstance(members, list) and members and all(isinstance(x, dict) for x in members), "Connector members must be nonempty member objects")
        references = [x["source_port_id"] for x in members]
        _need(all(isinstance(x, str) and x in ports for x in references), "Unknown connector source port")
        _need(len(set(references)) == len(references) and not covered.intersection(references), "A source port belongs to more than one connector member")
        covered.update(references)
        bundle = group_bundles[group_id]
        cell, edge = bundle["source_cell"], bundle["edge"]
        normal = NORMALS[edge]
        left = (-normal[1], normal[0])
        centre = [16. * cell[0] + 8. * normal[0], -16. * cell[1] + 8. * normal[1]]
        section_offset = raw.get("section_offset_m", 0.)
        _need(_number(section_offset), "Section offset must be finite metres")
        section_centre = [centre[i] + left[i]*section_offset for i in (0, 1)]
        member_ports, group_cuts, group_channels = [], {}, {}
        for member in members:
            port_id, planner_id = member["source_port_id"], member.get("id")
            _need(isinstance(planner_id, str) and planner_id and planner_id not in planner_ids, "Duplicate or invalid directed-member ID")
            planner_ids.add(planner_id)
            port = ports[port_id]
            _need(member.get("direction") in ("in", "out") and member["direction"] == port.get("direction"), "Member direction differs from its source port")
            point, tangent = port.get("endpoint_m"), port.get("tangent")
            _need(_vector(point, 3) and _vector(tangent, 2) and abs(math.hypot(*tangent)-1.) <= EPS, "Invalid measured endpoint or tangent")
            _need(port.get("direction") in ("in", "out") and _number(port.get("grade")), "Invalid measured direction or grade")
            _need(port.get("service_network") == component["network"], "Measured service differs from component")
            for key in ("engine_transport", "role"):
                _need(key not in profile or port.get(key) == profile[key], f"Measured {key} differs from optional profile")
            if "path_height_m" in profile:
                _need(abs(point[2]-profile["path_height_m"]) <= EPS, "Endpoint height differs from optional profile")
            if "endpoint_grade" in profile:
                _need(abs(port["grade"]-profile["endpoint_grade"]) <= EPS, "Endpoint grade differs from optional profile")
            _need(port.get("edge") == EDGES[edge], "Measured port belongs to another boundary edge")
            delta = [point[i]-centre[i] for i in (0, 1)]
            offset = sum(delta[i]*left[i] for i in (0, 1))
            _need(abs(sum(delta[i]*normal[i] for i in (0, 1))) <= EPS and abs(offset) <= 8.+EPS, "Port is outside its source tile seam")
            source_cells = set()
            for key in port.get("resource_keys", []):
                if key.startswith("path:" + identifier + ":"):
                    tile = int(key.rsplit("-", 1)[-1], 16)
                    _need(tile in tile_cells, "PATH resource is not owned by this piece")
                    source_cells.add(tile_cells[tile])
            _need(source_cells == {tuple(cell)}, "PATH resource source cell differs from boundary")
            channel_id, cut_id = member["channel_id"], member["cut_id"]
            _need(channel_id in channels, "Unknown physical channel")
            channel = channels[channel_id]
            _need(channel.get("component_id", raw["component_id"]) == raw["component_id"], "Physical channel belongs to another component")
            modes = member.get("traffic_modes", channel["traffic_modes"])
            _need(set(modes) <= set(channel["traffic_modes"]), "Member traffic modes exceed channel permissions")
            sign = 1. if port["direction"] == "out" else -1.
            outward = [sign*x for x in tangent]
            _need(sum(outward[i]*normal[i] for i in (0,1)) > EPS, "Outward connection heading does not cross the declared edge")
            heading = math.degrees(math.atan2(outward[0], outward[1])) % 360.
            grade = sign*port["grade"]
            key = (channel_id, cut_id)
            if key in group_cuts:
                cut = group_cuts[key]
                _need(_close(cut["endpoint_m"], point) and _close(cut["outward_tangent"], outward) and abs(cut["grade_outward"]-grade) <= EPS, "One physical cut has inconsistent endpoint geometry")
            else:
                cut = {"id": cut_id, "member_ids": [], "endpoint_m": list(point), "outward_tangent": outward,
                       "heading_outward_degrees": heading, "grade_outward": grade}
                group_cuts[key] = cut
            cut["member_ids"].append(planner_id)
            group_channels.setdefault(channel_id, {**deepcopy(channel), "cuts": []})
            if cut not in group_channels[channel_id]["cuts"]:
                group_channels[channel_id]["cuts"].append(cut)
            member_ports.append({**deepcopy(port), **deepcopy(member), "traffic_modes": list(modes),
                                 "outward_tangent": outward, "heading_outward_degrees": heading,
                                 "grade_outward": grade, "section_offset_m": offset-section_offset})
            port_components[port_id] = raw["component_id"]
            source_to_planner[port_id] = planner_id
        heights = [p["endpoint_m"][2] for p in member_ports]
        height = heights[0] if max(heights)-min(heights) <= EPS else 0.
        profile.setdefault("path_height_m", height)
        profile.setdefault("engine_transport", member_ports[0]["engine_transport"])
        profile.setdefault("role", member_ports[0]["role"])
        profile.setdefault("alignment", "orth" if all(_close(p["outward_tangent"], normal) for p in member_ports) else "angled")
        resolved.append({**deepcopy(raw), "profile": deepcopy(profile), "members": member_ports,
                         "section_offset_m": section_offset, "source_cell": deepcopy(cell), "edge": edge,
                         "tile_seam_center_m": centre+[height], "anchor_m": section_centre+[height],
                         "channels": list(group_channels.values()), "construction_network": component.get("construction_network"),
                         "outward_normal": list(normal), "boundary_bundle_id": bundle["id"]})
    _need(covered == ports.keys(), "Connector groups do not cover all measured ports")
    _need({m["channel_id"] for g in resolved for m in g["members"]} == set(channels), "Unused physical channel declaration")
    cuts, cut_geometry = {}, {}
    for group in resolved:
        for channel in group["channels"]:
            for cut in channel["cuts"]:
                key = cut["id"]
                identity = (channel["id"], group["boundary_bundle_id"])
                _need(key not in cuts or cuts[key] == identity, "Physical cut ID reused for another channel or boundary")
                _need(key not in planner_ids, "Physical cut ID collides with another library identity")
                if key in cut_geometry:
                    old = cut_geometry[key]
                    _need(_close(old["endpoint_m"], cut["endpoint_m"]) and _close(old["outward_tangent"], cut["outward_tangent"]) and abs(old["grade_outward"]-cut["grade_outward"]) <= EPS, "Shared physical cut has inconsistent geometry across services")
                cut_geometry[key] = cut
                cuts[key] = identity
    for channel_id, channel in channels.items():
        covered_modes = {mode for group in resolved for member in group["members"] if member["channel_id"] == channel_id for mode in member["traffic_modes"]}
        _need(covered_modes == set(channel["traffic_modes"]), "Physical channel declares a mode without a source-backed directional record")
    journeys, forbidden = [], []
    permitted_pairs, forbidden_pairs = set(), set()
    for journey in connections.get("journeys", []):
        first, last = journey["entry_port"], journey["exit_port"]
        _need(first in ports and last in ports and ports[first]["direction"] == "in" and ports[last]["direction"] == "out", "Journey references invalid ports")
        _need(port_components[first] == port_components[last], "Journey crosses declared independent components")
        _need((first,last) not in permitted_pairs, "Duplicate permitted journey")
        permitted_pairs.add((first,last))
        journeys.append({**deepcopy(journey), "source_id": journey.get("id"), "source_entry_port": first, "source_exit_port": last,
                         "id": source_to_planner[first]+">"+source_to_planner[last],
                         "entry_port": source_to_planner[first], "exit_port": source_to_planner[last]})
    for transfer in connections.get("forbidden_transfers", []):
        first, last = transfer["from_port"], transfer["to_port"]
        _need(first in ports and last in ports, "Forbidden transfer references unknown source ports")
        _need(ports[first]["direction"] == "in" and ports[last]["direction"] == "out", "Forbidden transfer directions are invalid")
        _need((first,last) not in forbidden_pairs and (first,last) not in permitted_pairs, "Duplicate or contradictory forbidden journey")
        forbidden_pairs.add((first,last))
        forbidden.append({**deepcopy(transfer), "source_from_port": first, "source_to_port": last,
                          "from_port": source_to_planner[first], "to_port": source_to_planner[last]})
    return {"id": identifier, "piece": deepcopy(piece), "connections": deepcopy(connections),
            "metadata": deepcopy(groups), "cells": cells, "groups": resolved,
            "boundary_bundles": deepcopy(bundles), "channels": deepcopy(groups["channels"]), "journeys": journeys, "forbidden_transfers": forbidden,
            "supported_orientations": deepcopy(connections.get("supported_orientations", [])),
            "software_status": deepcopy(connections.get("software_status", {}))}


@_validated
def load_library(custom_root, piece_ids, domain_id="high-speed-rail"):
    """Load authored metadata through an explicit source-domain registration."""
    root = Path(custom_root).resolve()
    _need(isinstance(domain_id, str) and re.fullmatch(r"[a-z][a-z0-9-]*", domain_id), "Invalid domain ID")
    domain = _safe_relative(root, "domains/" + domain_id)
    registry = json.loads(_safe_relative(domain, "domain.json").read_text())
    _need(registry.get("schema_version") == 1 and registry.get("id") == domain_id, "Invalid HSR domain registry schema or ID")
    profile_path = _safe_relative(domain, registry.get("connector_profiles", "connector-profiles.json"))
    profiles = resolve_profiles(jsonc.loads(profile_path.read_text())) if profile_path.is_file() else {}
    registered = {Path(p).parent.name: p for p in registry["pieces"]}
    _need(isinstance(piece_ids, (list, tuple)) and piece_ids and len(set(piece_ids)) == len(piece_ids), "Pilot needs unique selected piece IDs")
    result = {}
    for identifier in piece_ids:
        _need(identifier in registered and re.fullmatch(r"[a-z][a-z0-9-]{1,63}", identifier), "Unknown pilot piece ID")
        _need(Path(registered[identifier]) == Path("00_pieces") / identifier / "piece.json", "Piece registry path differs from canonical source path")
        piece_path = _safe_relative(domain, registered[identifier])
        directory = piece_path.parent
        piece_bytes, connection_bytes = piece_path.read_bytes(), _safe_relative(directory, "connections.json").read_bytes()
        sidecar = jsonc.load(_safe_relative(directory, "connector-groups.jsonc"))
        piece_data = json.loads(piece_bytes)
        _need(piece_data.get("domain") == domain_id and piece_data.get("id") == identifier, "Piece identity differs from its domain registration")
        expected = sidecar.get("source_binding", {})
        _export_need(expected.get("piece_sha256") == hashlib.sha256(piece_bytes).hexdigest() and
              expected.get("connections_sha256") == hashlib.sha256(connection_bytes).hexdigest(),
              f"Stale source binding: {identifier}", "stale_source")
        result[identifier] = validate_piece(piece_data, json.loads(connection_bytes), sidecar, profiles)
    return {"schema_version": 1, "domain_id": domain_id, "status": "metadata_validated", "pieces": result, "profiles": profiles,
            "counts": {"pieces": len(result), "groups": sum(len(x["groups"]) for x in result.values()),
                       "ports": sum(len(x["connections"]["ports"]) for x in result.values()),
                       "boundary_bundles": sum(len(x["boundary_bundles"]) for x in result.values())},
            "checks": {key: "unverified" for key in LIMITATIONS}}



# Compatibility name for callers migrating from the protected pilot.
load_pilot = load_library


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def _registered_adapter(root, domain_id):
    """Load the explicitly registered domain classifier, never infer it from engine IDs."""
    import importlib
    import sys
    domain = root / "domains" / domain_id
    registry = jsonc.load(domain / "domain.json")
    name = registry.get("connector_adapter")
    _need(isinstance(name, str) and all(p.isidentifier() for p in name.split(".")), "Domain needs an explicit connector_adapter registration")
    location = domain / "implementation"
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))
    adapter = importlib.import_module(name)
    _need(callable(getattr(adapter, "reviewed_contract", None)) and callable(getattr(adapter, "service_classifier", None)), "Connector adapter needs reviewed_contract and service_classifier")
    return adapter


@_validated
def verify_compiled(custom_root, build, resolved, domain_id="high-speed-rail"):
    """Independently re-extract saved PATHs, verify bindings, and retain full polylines."""
    from .connectivity import piece_connectivity, _routes
    from .content import resource_fingerprints
    from .dbpf import decompress, entries
    from .models import parse_s3d, validate_s3d
    root, build = Path(custom_root).resolve(), Path(build).resolve()
    _need(build.is_relative_to(root), "Compiled build must be inside the source library")
    adapter = _registered_adapter(root, domain_id)
    manifest_path = build / "manifest.json"
    manifest_bytes = manifest_path.read_bytes()
    manifest = jsonc.loads(manifest_bytes.decode())
    built_pieces = {x["id"]: x for x in manifest["pieces"]}
    files = {x["path"]: x for x in manifest["files"]}
    result = {}
    port_fields = ("id", "direction", "service_network", "service_family", "variant", "role", "engine_transport", "edge", "endpoint_m", "tangent", "grade")
    def port_facts(record):
        return sorted(({key: port.get(key) for key in port_fields} for port in record["ports"]), key=lambda p: p["id"])
    def journey_facts(record):
        return sorted((j["entry_port"], j["exit_port"], j["service_network"]) for j in record["journeys"])
    for identifier, item in resolved.items():
        _need(identifier in built_pieces, f"{identifier}: absent from compiled build")
        built = built_pieces[identifier]
        comparable = lambda p: {k: v for k, v in p.items() if k not in ("asset_file", "purpose", "design_review")}
        _need(comparable(built) == comparable(item["piece"]), f"{identifier}: compiled definition differs from current source")
        archive = _safe_relative(build, built["asset_file"])
        data = archive.read_bytes()
        declared = files[built["asset_file"]]
        _need(len(data) == declared["bytes"] and _sha(data) == declared["sha256"], f"{identifier}: DAT differs from build manifest")
        payload = {key: decompress(raw) for key, raw in entries(data).items()}
        model = payload[0x5ad0e817, 0xbadb57f1, int(built["preview_id"], 16)]
        validate_s3d(parse_s3d(model))
        measured = piece_connectivity(item["piece"], payload, contract=adapter.reviewed_contract(item["piece"]), service_classifier=adapter.service_classifier)
        saved = item["connections"]
        _need(port_facts(measured) == port_facts(saved) and journey_facts(measured) == journey_facts(saved), f"{identifier}: compiled PATH facts differ from connections.json")
        actual_hashes = resource_fingerprints(identifier, payload)
        checked = 0
        for key, digest in saved["source"]["resource_fingerprints"].items():
            if key.startswith("construction:"):
                continue
            _need(actual_hashes.get(key) == digest, f"{identifier}: compiled resource fingerprint differs: {key}")
            checked += 1
        routes = json.loads(json.dumps(_routes(item["piece"], payload), allow_nan=False))
        from .verify import parse_paths
        for route in routes:
            parsed = parse_paths(payload[0x296678f7, 0xa966883f, int(route["tile_id"],16)])["routes"][route["source_route_index"]]
            col, row = route["cell"]
            route["points"] = [[east+16.*col, north-16.*row, height] for east,north,height in parsed["points"]]
        refs = {}
        for group in item["groups"]:
            for member in group["members"]:
                relevant = [r["id"] for r in routes if _route_matches_member(r, member)]
                _need(relevant, f"{identifier}: endpoint has no compiled route occurrence")
                refs[member["id"]] = relevant
        result[identifier] = {
            "dat_path": archive.relative_to(root).as_posix(), "dat_sha256": _sha(data),
            "model_sha256": _sha(model), "resource_fingerprints_checked": checked,
            "directional_ports_reextracted": len(measured["ports"]), "directed_journeys_reextracted": len(measured["journeys"]),
            "compiled_definition": "passed", "manifest_payload": "passed", "saved_resource_fingerprints": "passed",
            "actual_path_facts": "passed", "preview_model_structure": "passed", "construction_rules_reextracted": False,
            "routes": routes, "endpoint_route_refs": refs,
        }
    from .export import compiled_manifest_sha256
    return {"manifest_path": manifest_path.relative_to(root).as_posix(), "manifest_sha256": _sha(manifest_bytes),
            "compiled_manifest_sha256": compiled_manifest_sha256(manifest), "pieces": result}


def _route_matches_member(route, member):
    endpoint = 0 if member["direction"] == "in" else -1
    if route["engine_transport"] != member["engine_transport"] or not _close(route["points"][endpoint], member["endpoint_m"]):
        return False
    # The graph extractor uses 6-decimal-metre samples; full exported polylines
    # retain parsed PATH precision. Compare occurrence IDs in that graph frame.
    segment = route["points"][:2] if endpoint == 0 else route["points"][-2:]
    segment = [[round(value,6) for value in point] for point in segment]
    delta = [last-first for first,last in zip(*segment)]
    length = math.hypot(*delta[:2])
    if not length:
        return False
    sampled = [value/length for value in delta[:2]]
    return _close(sampled, member.get("sampled_tangent", member["tangent"])) and abs(delta[2]/length-member["grade"]) <= EPS


def _source_files(root, domain_id, piece_id, compiled):
    domain = root / "domains" / domain_id
    directory = domain / "00_pieces" / piece_id
    files = [directory/name for name in ("piece.json", "connections.json", "connector-groups.jsonc")]
    # The manifest's compiled facts have their own semantic fingerprint. Its
    # documentation snapshot must be allowed to change after final rendering.
    files += [domain/"domain.json", root/compiled["pieces"][piece_id]["dat_path"]]
    registry = jsonc.load(domain/"domain.json")
    profile_path = _safe_relative(domain, registry.get("connector_profiles", "connector-profiles.json"))
    if profile_path.is_file():
        files.append(profile_path)
    # Contract providers can import reviewed tangent/geometry helpers. Bind the
    # complete owning implementation, rather than only its thin adapter module.
    files += list((domain/"implementation").rglob("*.py"))
    files += list((root/"framework/scp").glob("*.py"))
    files += list((root/"schemas").glob("*.schema.json"))
    for path in files:
        _need(path.resolve().is_relative_to(root), "Source fingerprint file escapes library")
    return {path.relative_to(root).as_posix(): _sha(path.read_bytes()) for path in sorted(set(files))}


def _validate_export_routes(value, piece):
    routes = value["routes"]
    by_id = {route["id"]:route for route in routes}
    _need(len(by_id) == len(routes), "Duplicate exported route ID")
    tile_cells = {tile:cell for tile,cell in zip(piece["piece"]["tile_ids"], piece["cells"])}
    for route in routes:
        _need(route["tile_id"] in tile_cells and route["cell"] == tile_cells[route["tile_id"]], "Export route uses an unowned tile/cell")
    members = {member["id"]:member for group in piece["groups"] for member in group["members"]}
    refs = value["endpoint_route_refs"]
    _need(set(refs) == set(members), "Export route references do not cover every member")
    for identifier, member in members.items():
        actual = refs[identifier]
        expected = [route["id"] for route in routes if _route_matches_member(route,member)]
        _need(expected and len(actual) == len(set(actual)) and set(actual) == set(expected), "Export member references missing or mismatched route occurrences")



def build_exports(custom_root, piece_ids, build, domain_id="high-speed-rail"):
    """Compute deterministic consumer documents without modifying any source."""
    root = Path(custom_root).resolve()
    report = load_library(root, piece_ids, domain_id)
    compiled = verify_compiled(root, build, report["pieces"], domain_id)
    result = {}
    for piece_id, piece in report["pieces"].items():
        evidence = deepcopy(compiled["pieces"][piece_id])
        routes, refs = evidence.pop("routes"), evidence.pop("endpoint_route_refs")
        value = {
            "schema_version": 1, "purpose": "Generated resolved connection description; edit source declarations or compiled resources, then refresh.",
            "piece_id": piece_id, "domain_id": domain_id,
            "source_binding": {"compiled_build": Path(build).resolve().relative_to(root).as_posix(),
                               "compiled_manifest_sha256": compiled["compiled_manifest_sha256"],
                               "files": _source_files(root, domain_id, piece_id, compiled)},
            "coordinate_convention": {"units": "metres", "axes": ["east", "north", "height"], "tile_metres": 16,
                                      "heading": "outward; 0 degrees north, clockwise in plan view", "slope": "outward rise/run at the edge; percent = 100 * grade"},
            "resolved_piece": deepcopy(piece), "routes": routes, "endpoint_route_refs": refs,
            "verification": {"metadata": "passed", "compiled_paths": "passed", "compiled_resources": evidence,
                             "occupied_cells": "unverified", **{key: "unverified" for key in LIMITATIONS}},
        }
        value["content_sha256"] = _sha(_canonical(value))
        validate_structure(value, _schema("connector-data.schema.json"))
        result[piece_id] = value
    return result


def write_exports(custom_root, exports, domain_id="high-speed-rail"):
    """Publish only complete validated results; authored JSONC is never rewritten."""
    root = Path(custom_root).resolve()
    paths = {}
    for piece_id, value in exports.items():
        path = _safe_relative(root, f"domains/{domain_id}/00_pieces/{piece_id}/connector-data.json")
        path.write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")
        paths[piece_id] = path.relative_to(root).as_posix()
    return paths


@_export_validated
def load_exports(custom_root, piece_ids, domain_id="high-speed-rail"):
    """Read fresh library exports without running generation or parsing game resources."""
    root = Path(custom_root).resolve()
    report = load_library(root, piece_ids, domain_id)
    report["exports"] = {}
    for piece_id, piece in list(report["pieces"].items()):
        path = _safe_relative(root, f"domains/{domain_id}/00_pieces/{piece_id}/connector-data.json")
        _export_need(path.is_file(), f"{piece_id}: missing connector-data.json; run connectors refresh", "missing_export")
        value = jsonc.load(path)
        validate_structure(value, _schema("connector-data.schema.json"))
        _need(value["piece_id"] == piece_id and value["domain_id"] == domain_id, "Export identity mismatch")
        unhashed = {k:v for k,v in value.items() if k != "content_sha256"}
        _need(_sha(_canonical(unhashed)) == value["content_sha256"], f"{piece_id}: export content fingerprint mismatch")
        for name, digest in value["source_binding"]["files"].items():
            source = _safe_relative(root, name)
            _export_need(source.is_file(), f"{piece_id}: missing exported source {name}; restore its verified source before refreshing", "missing_source")
            _export_need(_sha(source.read_bytes()) == digest, f"{piece_id}: stale exported source {name}; run connectors refresh", "stale_export")
        _need(value["resolved_piece"] == piece, f"{piece_id}: export differs from resolved declarations")
        build = _safe_relative(root, value["source_binding"]["compiled_build"])
        manifest_path = build/"manifest.json"
        manifest = jsonc.load(manifest_path)
        from .export import compiled_manifest_sha256
        _export_need(compiled_manifest_sha256(manifest) == value["source_binding"]["compiled_manifest_sha256"],
                     f"{piece_id}: stale compiled manifest facts; run connectors refresh", "stale_export")
        selected = [item for item in manifest["pieces"] if item["id"] == piece_id]
        _need(len(selected) == 1, "Export compiled build does not own exactly one selected definition")
        dat = _safe_relative(build, selected[0]["asset_file"])
        compiled = {"manifest_path":manifest_path.relative_to(root).as_posix(), "pieces":{piece_id:{"dat_path":dat.relative_to(root).as_posix()}}}
        expected_bindings = _source_files(root, domain_id, piece_id, compiled)
        _export_need(value["source_binding"]["files"] == expected_bindings, f"{piece_id}: export source-binding coverage is incomplete or stale", "stale_export")
        _validate_export_routes(value,piece)
        report["exports"][piece_id] = {"path": path.relative_to(root).as_posix(), "sha256": _sha(path.read_bytes()), "source_binding": value["source_binding"], "verification": value["verification"]}
        report["pieces"][piece_id] = {**value["resolved_piece"], "routes": value["routes"], "endpoint_route_refs": value["endpoint_route_refs"], "export_verification": value["verification"]}
    report["source_format"] = "connector-data-v1"
    return report


def verify_overview(custom_root, piece_id, domain_id="high-speed-rail", plugins=None):
    """Check current artwork, selectable text, and recorded source/render fingerprints."""
    from .connector_overview import markdown_overview
    root = Path(custom_root).resolve()
    directory = _safe_relative(root, f"domains/{domain_id}/00_pieces/{piece_id}")
    evidence_path = directory / "evidence/connection-overview.json"
    _need(evidence_path.is_file(), f"{piece_id}: missing overview evidence; run connectors refresh")
    evidence = jsonc.load(evidence_path)
    image = directory / "connection-overview.png"
    _need(evidence.get("schema_version") == 1 and evidence.get("piece_id") == piece_id, "Wrong overview evidence identity")
    _need(image.is_file() and _sha(image.read_bytes()) == evidence["output_sha256"], f"{piece_id}: overview image differs from provenance")
    for name, digest in evidence["source_inputs"].items():
        path = _safe_relative(root, name)
        _need(path.is_file() and _sha(path.read_bytes()) == digest, f"{piece_id}: stale overview input {name}")
    _need(_sha((root/"framework/scp/connector_overview.py").read_bytes()) == evidence["generator_sha256"], "Stale overview renderer")
    _need(_sha(Path(__file__).read_bytes()) == evidence["metadata_resolver_sha256"], "Stale overview metadata resolver")
    for name, digest in evidence["shared_framework_sources"].items():
        _need(_sha(_safe_relative(root/"framework/scp", name).read_bytes()) == digest, f"Stale overview framework input: {name}")
    if "compiled_manifest_sha256" in evidence:
        from .export import compiled_manifest_sha256
        manifest = jsonc.load(_safe_relative(root, evidence["source_manifest"]))
        _need(compiled_manifest_sha256(manifest) == evidence["compiled_manifest_sha256"],
              f"{piece_id}: stale overview compiled manifest facts")
        compiled_sources = (("source_dat", "source_dat_sha256"),)
    else:
        compiled_sources = (("source_manifest", "manifest_sha256"), ("source_dat", "source_dat_sha256"))
    for key, digest_key in compiled_sources:
        _need(_sha(_safe_relative(root, evidence[key]).read_bytes()) == evidence[digest_key], f"{piece_id}: stale overview compiled source")
    from .connector_overview import BODY_SIZE, mono_font
    from .preview import TextureLibrary, renderer_settings, font
    from .models import parse_s3d
    from .dbpf import decompress, entries
    if plugins is None:
        fixture, settings = root/"local/validation-inputs/Plugins", root/"local/settings.json"
        plugins = fixture if fixture.is_dir() else jsonc.load(settings).get("plugins") if settings.is_file() else None
    _need(plugins is not None, "Overview texture freshness needs --plugins or configured texture inputs; use --no-render for data-only checks")
    payload = entries(_safe_relative(root,evidence["source_dat"]).read_bytes())
    model = parse_s3d(decompress(payload[0x5ad0e817,0xbadb57f1,int(evidence["source_preview_id"],16)]))
    _, textures = TextureLibrary(Path(plugins).expanduser()).for_model(model)
    _need(textures == evidence["textures"], f"{piece_id}: stale overview texture inputs")
    current_fonts = [{"name":list(face.getname()), "file_sha256":_sha(Path(face.path).read_bytes()) if getattr(face,"path",None) else None}
                     for face in (font(BODY_SIZE),font(BODY_SIZE,True),mono_font(BODY_SIZE,font))]
    _need(current_fonts == evidence["figure_typography"]["fonts"], "Stale overview font inputs")
    _need(renderer_settings() == evidence["renderer"], "Stale overview runtime renderer settings")
    text = markdown_overview(evidence)
    _need(_sha(text.encode()) == evidence["selectable_markdown_sha256"], "Overview selectable-text fingerprint mismatch")
    readme = (directory/"README.md").read_text()
    _need(text in readme, f"{piece_id}: README overview differs from card facts")
    return {"status": "passed", "boundary_cards": len(evidence["boundary_cards"]), "output_sha256": evidence["output_sha256"]}


def refresh_connections(custom_root, piece_ids, build, *, domain_id="high-speed-rail", plugins=None, render=True):
    """Re-extract and validate before publishing generated data and documentation."""
    exports = build_exports(custom_root, piece_ids, build, domain_id)
    figures = None
    if render:
        from .connector_overview import render_overviews
        figures = render_overviews(custom_root, piece_ids, build=build, plugins=plugins, domain_id=domain_id, resolved={"pieces": {identifier: value["resolved_piece"] for identifier, value in exports.items()}})
    paths = write_exports(custom_root, exports, domain_id)
    return {"status": "refreshed", "exports": paths, "overviews": figures,
            "compiled_paths": "passed", "manual_observations_changed": False, "installed": False}


def check_connections(custom_root, piece_ids, build, *, domain_id="high-speed-rail", render=True, plugins=None):
    """Read-only independent extraction plus exact generated-output freshness checks."""
    root = Path(custom_root).resolve()
    expected = build_exports(root, piece_ids, build, domain_id)
    report = load_exports(root, piece_ids, domain_id)
    for piece_id, value in expected.items():
        path = _safe_relative(root, report["exports"][piece_id]["path"])
        _need(jsonc.load(path) == value, f"{piece_id}: generated data differs from independently re-extracted resources")
    overviews = {piece_id: verify_overview(root, piece_id, domain_id, plugins=plugins) for piece_id in piece_ids} if render else None
    return {"status": "passed", "counts": report["counts"], "compiled_paths": "passed", "export_freshness": "passed",
            "overviews": overviews, "manual_observations_changed": False, "installed": False}
