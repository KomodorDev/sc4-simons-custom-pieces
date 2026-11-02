#!/usr/bin/env python3
"""Independently check saved prototype samples, never SimCity 4 resources."""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import sys


ARMS = {"SW", "NE", "NW", "SE"}
REQUIRED = {(a, b) for a in ARMS for b in ARMS if a != b}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _distance(first, second):
    return math.dist(first, second)


def verify_geometry(design, geometry):
    """Measure the saved points without calling the geometry generator."""
    params = design["geometry"]
    roads, routes = geometry["roads"], geometry["routes"]
    _require(geometry.get("schema_version") == 1, "Unsupported sampled geometry schema")
    _require(design.get("compiled") is False and design.get("registered") is False,
             "This checker supports an unregistered, uncompiled prototype only")
    _require(geometry["metadata"]["parameters"] == params, "Export parameters differ from the design")
    _require(len({road["id"] for road in roads}) == len(roads), "Duplicate road ID")
    _require(len({route["id"] for route in routes}) == len(routes), "Duplicate route ID")
    for item in roads + routes:
        points = item["points"]
        _require(len(points) >= 2, item["id"] + ": too few samples")
        _require(all(len(point) == 3 and all(isinstance(value, (int, float))
                     and not isinstance(value, bool) and math.isfinite(value) for value in point)
                     for point in points), item["id"] + ": invalid coordinates")
        _require(all(point[2] >= -1e-8 for point in points), item["id"] + ": below ground")
        _require(isinstance(item["width_m"], (int, float)) and item["width_m"] > 0,
                 item["id"] + ": invalid width")

    road_by_id = {road["id"]: road for road in roads}
    _require(set(road_by_id) == {"highway-upper", "highway-lower", "avenue",
             "ramp-upper-off", "ramp-upper-on", "ramp-lower-off", "ramp-lower-on"},
             "Expected two decks, an avenue, and four ramp surfaces")
    for name, height, width in (("highway-upper", params["upper_height_m"], params["highway_width_m"]),
                                ("highway-lower", params["lower_height_m"], params["highway_width_m"]),
                                ("avenue", 0, params["avenue_width_m"])):
        road = road_by_id[name]
        _require(road["width_m"] == width, name + ": unexpected surface width")
        _require(all(abs(point[2] - height) < 1e-8 for point in road["points"]),
                 name + ": incorrect height")
        for x, y, _ in road["points"]:
            cross_axis = (x + y) if name == "avenue" else (y - x)
            _require(abs(cross_axis) < 1e-7, name + ": not on the declared diagonal axis")

    graph, node_points = defaultdict(list), defaultdict(list)
    route_by_id = {route["id"]: route for route in routes}
    expected_kinds = {name: "highway-through" for name in ("highway-upper-through", "highway-lower-through",
                                                          "highway-lower-approach", "highway-lower-departure")}
    expected_kinds.update({deck + "-" + direction: "ramp" for deck in ("upper", "lower") for direction in ("off", "on")})
    expected_kinds.update({"avenue-" + direction + "-bound-" + str(index): "avenue-through"
                           for direction in ("nw", "se") for index in range(1, 6)})
    expected_kinds.update({deck + "-off-to-" + arm: "surface-turn" for deck in ("upper", "lower") for arm in ("NW", "SE")})
    expected_kinds.update({arm + "-to-" + deck + "-on": "surface-turn" for deck in ("upper", "lower") for arm in ("NW", "SE")})
    _require(set(route_by_id) == set(expected_kinds), "Missing or unexpected directed route IDs")
    for route in routes:
        _require(route["kind"] == expected_kinds[route["id"]], route["id"] + ": incorrect route kind")
        local = [[(x + y) / math.sqrt(2), (y - x) / math.sqrt(2), z] for x, y, z in route["points"]]
        if route["kind"] == "highway-through":
            upper = route["id"] == "highway-upper-through"
            height = params["upper_height_m"] if upper else params["lower_height_m"]
            outer, inner = params["highway_half_length_m"], params["lower_highway_join_m"]
            source, target, start_u, end_u = {
                "highway-upper-through": ("SW", "NE", -outer, outer),
                "highway-lower-approach": ("NE", "lower-branch-in", outer, inner),
                "highway-lower-through": ("lower-branch-in", "lower-branch-out", inner, -inner),
                "highway-lower-departure": ("lower-branch-out", "SW", -inner, -outer),
            }[route["id"]]
            side, direction = (-1, 1) if upper else (1, -1)
            _require((route["from"], route["to"]) == (source, target), route["id"] + ": wrong highway arms")
            _require(all(abs(v - side * params["highway_lane_offset_m"]) < 1e-7
                         and abs(z - height) < 1e-7 for _, v, z in local),
                     route["id"] + ": highway samples leave their deck or lane spine")
            _require(abs(local[0][0] - start_u) < 1e-7 and abs(local[-1][0] - end_u) < 1e-7,
                     route["id"] + ": wrong highway boundary")
            _require(all(direction * (b[0] - a[0]) > 0 for a, b in zip(local, local[1:])),
                     route["id"] + ": highway samples reverse")
        elif route["kind"] == "avenue-through":
            direction = 1 if "nw-bound" in route["id"] else -1
            _require(all(abs(u - direction * params["avenue_lane_offset_m"]) < 1e-7
                         and abs(v) <= params["junction_offset_m"] + params["avenue_approach_length_m"] + 1e-7 for u, v, _ in local),
                     route["id"] + ": avenue samples leave their declared lane")
            _require(all(direction * (b[1] - a[1]) > 0 for a, b in zip(local, local[1:])),
                     route["id"] + ": avenue samples reverse")
        elif route["kind"] == "surface-turn":
            side = -1 if "upper" in route["id"] else 1
            _require(all(abs(u) <= params["avenue_width_m"] / 2 + 1e-7
                         and abs(v - side * params["junction_offset_m"]) <= 18 + 1e-7 for u, v, _ in local),
                     route["id"] + ": turn leaves its declared intersection zone")
    for route in routes:
        graph[route["from"]].append(route["to"])
        node_points[route["from"]].append(route["points"][0])
        node_points[route["to"]].append(route["points"][-1])
        _require(route["from"] != route["to"], route["id"] + ": immediate U-turn edge")
        if route["kind"] not in {"ramp", "highway-through"}:
            _require(all(abs(point[2]) < 1e-8 for point in route["points"]),
                     route["id"] + ": surface connector is elevated")
    for node, endpoints in node_points.items():
        if node not in ARMS:
            _require(all(_distance(endpoints[0], point) < 1e-7 for point in endpoints),
                     node + ": disconnected saved endpoints")

    # External arms are terminal boundaries. They must never become shortcut
    # transfer nodes between incoming and outgoing lanes or highway decks.
    reached, returns = set(), set()
    for source in ARMS:
        pending, visited = list(graph[source]), set()
        while pending:
            node = pending.pop()
            if node in ARMS:
                if node == source:
                    returns.add(source)
                else:
                    reached.add((source, node))
                continue
            if node not in visited:
                visited.add(node)
                pending.extend(graph[node])
    _require(reached == REQUIRED, "Missing distinct-arm journeys: " + str(sorted(REQUIRED - reached)))
    _require(set(design["required_movements"]) == {a + "->" + b for a, b in REQUIRED},
             "Design movement list differs from the complete twelve-movement brief")

    ramps = [route for route in routes if route["kind"] == "ramp"]
    _require({route["id"] for route in ramps} == {"upper-off", "upper-on", "lower-off", "lower-on"},
             "Expected exactly four directed ramps")
    ramp_reports = []
    clearance = params["highway_width_m"] / 2 + params["ramp_width_m"] / 2 + params["lateral_clearance_m"]
    for ramp in ramps:
        points = ramp["points"]
        _require(points == road_by_id["ramp-" + ramp["id"]]["points"],
                 ramp["id"] + ": road and route samples differ")
        _require(ramp["width_m"] == road_by_id["ramp-" + ramp["id"]]["width_m"] == params["ramp_width_m"],
                 ramp["id"] + ": wrong width")
        upper, on = ramp["id"].startswith("upper"), ramp["id"].endswith("on")
        height = params["upper_height_m"] if upper else params["lower_height_m"]
        local = [[(x + y) / math.sqrt(2), (y - x) / math.sqrt(2), z] for x, y, z in points]
        direction, side = (1, -1) if upper else (-1, 1)
        mouth = params["avenue_width_m"] / 2
        half = params["highway_half_length_m"] if upper else params["lower_highway_join_m"]
        start_u, end_u = ((direction * mouth, direction * half) if on else (-direction * half, -direction * mouth))
        start_v, end_v = ((side * params["junction_offset_m"], side * params["highway_lane_offset_m"])
                          if on else (side * params["highway_lane_offset_m"], side * params["junction_offset_m"]))
        _require(abs(local[0][0] - start_u) < 1e-7 and abs(local[-1][0] - end_u) < 1e-7
                 and abs(local[0][1] - start_v) < 1e-7 and abs(local[-1][1] - end_v) < 1e-7,
                 ramp["id"] + ": wrong ramp corridor endpoints")
        _require(all(direction * (b[0] - a[0]) > 0 and (end_v - start_v) * (b[1] - a[1]) >= -1e-7
                     for a, b in zip(local, local[1:])), ramp["id"] + ": ramp reverses outside its corridor")
        _require(all(min(start_u, end_u) - 1e-7 <= u <= max(start_u, end_u) + 1e-7
                     and min(start_v, end_v) - 1e-7 <= v <= max(start_v, end_v) + 1e-7 for u, v, _ in local),
                 ramp["id"] + ": ramp leaves its declared corridor")
        expected_from_to = {"upper-off": ("SW", "se-off-mouth"), "upper-on": ("se-on-mouth", "NE"),
                            "lower-off": ("lower-branch-in", "nw-off-mouth"),
                            "lower-on": ("nw-on-mouth", "lower-branch-out")}
        _require((ramp["from"], ramp["to"]) == expected_from_to[ramp["id"]],
                 ramp["id"] + ": wrong branch nodes")
        start_height, end_height = (0, height) if on else (height, 0)
        _require(abs(points[0][2] - start_height) < 1e-8 and abs(points[-1][2] - end_height) < 1e-8,
                 ramp["id"] + ": wrong ramp endpoint heights")
        grades, length = [], 0.0
        for first, second in zip(points, points[1:]):
            horizontal = math.hypot(second[0] - first[0], second[1] - first[1])
            _require(horizontal > 1e-9, ramp["id"] + ": repeated or vertical samples")
            length += horizontal
            grades.append(100 * abs(second[2] - first[2]) / horizontal)
            _require((second[2] - first[2]) * (1 if on else -1) >= -1e-8,
                     ramp["id"] + ": ramp height reverses")
        _require(max(grades) <= params["max_grade_percent"] + 1e-6, ramp["id"] + ": grade exceeds assumed limit")
        target_length = params["upper_ramp_plan_length_m"] if upper else params["lower_ramp_plan_length_m"]
        _require(abs(length - target_length) <= 0.01, ramp["id"] + ": exceeds or misses the requested full ramp length")
        _require(grades[0] < 0.5 and grades[-1] < 0.5, ramp["id"] + ": endpoint grade is not near horizontal")
        for x, y, z in points:
            v = (y - x) / math.sqrt(2)
            _require(v < 0 if upper else v > 0, ramp["id"] + ": ramp uses the left side")
            if abs(v) < clearance:
                _require(abs(z - height) < 1e-7, ramp["id"] + ": ramp changes height inside the mainline envelope")
        ramp_reports.append({"id": ramp["id"], "horizontal_length_m": round(length, 6),
                             "tile_length_equivalents": round(length / 16, 6),
                             "max_sampled_grade_percent": round(max(grades), 6)})

    # Explicit topology: each ramp's terminal joins only a surface connector;
    # no invented edge may join the stacked highway directions at height.
    for name in ("highway-upper-through", "highway-lower-through"):
        _require(name in route_by_id, "Missing highway through route")
    _require(len(geometry["intersections"]) == 2 and all(item["arms"] == 4 for item in geometry["intersections"]),
             "Expected two four-arm surface intersections")
    for item, side in zip(geometry["intersections"], (-1, 1)):
        x, y, z = item["position"]
        _require(abs((x + y) / math.sqrt(2)) < 1e-7 and abs((y - x) / math.sqrt(2) - side * params["junction_offset_m"]) < 1e-7
                 and abs(z) < 1e-7, "Surface intersection moved from its declared ground position")
    return {"schema_version": 1, "passed": True, "scope": "saved sampled geometry and declared directed graph only",
            "compiled_resource_checks": False, "game_tests": "not-run",
            "required_distinct_arm_journeys": len(reached),
            "journeys": [a + "->" + b for a, b in sorted(reached)],
            "possible_indirect_returns_via_avenue": sorted(returns),
            "surface_intersections": 2, "ramps": ramp_reports,
            "provisional_lateral_envelope_clearance_m": clearance,
            "limits": ["Widths and maximum grade are design assumptions, rather than native interface measurements.",
                       "Centre-line samples do not prove swept traffic clearance, curvature standards, or native joins.",
                       "Supports, deck solids, pavement unions, signals, construction ownership, resource encoding, and rotations are not checked.",
                       "No game placement, Route Query, visible traffic, or human observation has run."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--design", type=Path, required=True)
    parser.add_argument("--geometry", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "framework"))
    from scp import jsonc
    design, geometry = jsonc.load(args.design), json.loads(args.geometry.read_text())
    digest = hashlib.sha256(args.design.read_bytes()).hexdigest()
    _require(geometry["source"]["design_sha256"] == digest, "Saved geometry belongs to a different design source")
    result = verify_geometry(design, geometry)
    result["sources"] = {"design_sha256": digest, "geometry_sha256": hashlib.sha256(args.geometry.read_bytes()).hexdigest(),
                         "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(f"PASS: {result['required_distinct_arm_journeys']} distinct-arm journeys, four ramp grades, and provisional lateral envelopes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
