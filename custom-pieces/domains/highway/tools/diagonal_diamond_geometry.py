#!/usr/bin/env python3
"""Sample an unregistered highway design; this module emits no game resources."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys


DEFAULTS = {
    "upper_ramp_plan_length_m": 80.0,
    "lower_ramp_plan_length_m": 48.0,
    "highway_half_length_m": 87.11830092828814,
    "lower_highway_join_m": 51.61134880454402,
    "junction_offset_m": 28.0,
    "avenue_approach_length_m": 32.0,
    "highway_width_m": 12.0,
    "ramp_width_m": 6.0,
    "avenue_width_m": 24.0,
    "highway_lane_offset_m": 3.2,
    "avenue_lane_offset_m": 6.0,
    "upper_height_m": 15.0,
    "lower_height_m": 7.5,
    "max_grade_percent": 40.0,
    "samples_per_route": 401,
    "lateral_clearance_m": 2.0,
    "descent_clear_v_m": 12.0,
    "ground_landing_m": 4.0,
    "grade_taper_m": 2.0,
}


def load_design(path: str | Path) -> dict:
    """Read the library's maintained JSONC source through its shared parser."""
    framework = Path(__file__).resolve().parents[3] / "framework"
    if str(framework) not in sys.path:
        sys.path.insert(0, str(framework))
    from scp import jsonc

    return jsonc.load(Path(path))


def _world(u: float, v: float, z: float) -> list[float]:
    root_two = math.sqrt(2.0)
    return [(u - v) / root_two, (u + v) / root_two, z]


def _bezier(controls: list[tuple[float, float]], count: int) -> list[list[float]]:
    result = []
    for index in range(count):
        t = index / (count - 1)
        weights = ((1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3)
        result.append([sum(weight * point[axis] for weight, point in zip(weights, controls)) for axis in (0, 1)])
    return result


def _lengths(points: list[list[float]]) -> list[float]:
    lengths = [0.0]
    for first, second in zip(points, points[1:]):
        lengths.append(lengths[-1] + math.hypot(second[0] - first[0], second[1] - first[1]))
    return lengths


def _compact_controls(params: dict, half: float, side: int = -1) -> list[tuple[float, float]]:
    mouth = params["avenue_width_m"] / 2
    handle = 0.38 * (half - mouth)
    return [(-half, side * params["highway_lane_offset_m"]), (-half + handle, side * params["highway_lane_offset_m"]), (-mouth - handle, side * params["junction_offset_m"]), (-mouth, side * params["junction_offset_m"])]


def solve_highway_half_length(params: dict, target_length_m: float | None = None) -> float:
    """Fit the complete sampled ramp to its requested horizontal arc length."""
    target = params["upper_ramp_plan_length_m"] if target_length_m is None else target_length_m
    lateral_span = params["junction_offset_m"] - params["highway_lane_offset_m"]
    if target <= lateral_span:
        raise ValueError("Requested ramp plan length must exceed its lateral shift to the avenue junction.")
    mouth = params["avenue_width_m"] / 2
    low, high = mouth + 1e-6, mouth + target
    for _ in range(60):
        middle = (low + high) / 2
        points = _bezier(_compact_controls(params, middle), params["samples_per_route"])
        length = _lengths(points)[-1]
        if length < target:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def _minimum_radius(segments: list[list[tuple[float, float]]]) -> float:
    """Sample analytic planar curvature; this is not a native design standard."""
    maximum_curvature = 0.0
    for controls in segments:
        for index in range(2001):
            t = index / 2000
            first = [3 * ((1 - t) ** 2 * (controls[1][axis] - controls[0][axis]) + 2 * (1 - t) * t * (controls[2][axis] - controls[1][axis]) + t * t * (controls[3][axis] - controls[2][axis])) for axis in (0, 1)]
            second = [6 * ((1 - t) * (controls[2][axis] - 2 * controls[1][axis] + controls[0][axis]) + t * (controls[3][axis] - 2 * controls[2][axis] + controls[1][axis])) for axis in (0, 1)]
            speed = math.hypot(*first)
            if speed <= 1e-12:
                raise ValueError("A ramp curve contains a stationary tangent.")
            maximum_curvature = max(maximum_curvature, abs(first[0] * second[1] - first[1] * second[0]) / speed ** 3)
    return 1 / maximum_curvature if maximum_curvature else math.inf


def _integrated_grade(distance: float, length: float, taper: float) -> float:
    """Integrate a unit trapezoidal grade, with flat grades at both ends."""
    if distance <= 0:
        return 0.0
    if distance >= length:
        return length - taper
    if distance < taper:
        return distance * distance / (2 * taper)
    if distance <= length - taper:
        return distance - taper / 2
    remaining = length - distance
    return length - taper - remaining * remaining / (2 * taper)


def _ramp(params: dict, route_id: str, side: int, direction: int, height: float, on: bool) -> dict:
    """Create an off-ramp first; reverse it geometrically for the same-side on-ramp."""
    upper = route_id.startswith("upper")
    half = params["highway_half_length_m"] if upper else params["lower_highway_join_m"]
    target_length = params["upper_ramp_plan_length_m"] if upper else params["lower_ramp_plan_length_m"]
    segments = [_compact_controls(params, half, side)]
    points_uv = _bezier(segments[0], params["samples_per_route"])
    lengths = _lengths(points_uv)
    clear = params["descent_clear_v_m"]
    clear_index = next((i for i, point in enumerate(points_uv) if abs(point[1]) >= clear), None)
    if clear_index is None:
        raise ValueError("Ramp never clears the declared stacked-road envelope.")
    descent_start = lengths[clear_index]
    landing = params["ground_landing_m"]
    transition = lengths[-1] - descent_start - landing
    taper = params["grade_taper_m"]
    if transition <= 2 * taper:
        raise ValueError("Ramp is too short for lateral clearance, both grade tapers, and the ground landing.")
    grade = height / (transition - taper)
    if 100 * grade > params["max_grade_percent"] + 1e-9:
        raise ValueError(f"{route_id} needs {100 * grade:.3f}% grade, exceeding the assumed {params['max_grade_percent']:.3f}% limit; increase the footprint.")
    points_local = []
    for point, length in zip(points_uv, lengths):
        z = height - grade * _integrated_grade(length - descent_start, transition, taper)
        points_local.append([point[0], point[1], max(0.0, z)])
    # u reflection provides opposite travel. On-ramps additionally reflect and
    # reverse the complete shape; their grade endpoints remain horizontal.
    if direction < 0:
        points_local = [[-u, v, z] for u, v, z in points_local]
    if on:
        points_local = [[-u, v, z] for u, v, z in reversed(points_local)]
    return {
        "id": route_id,
        "kind": "ramp",
        "width_m": params["ramp_width_m"],
        "points": [_world(*point) for point in points_local],
        "points_uvz": points_local,
        "height_m": height,
        "side": "SE" if side < 0 else "NW",
        "direction": "on" if on else "off",
        "length_plan_m": lengths[-1],
        "length_3d_m": sum(math.dist(first, second) for first, second in zip(points_local, points_local[1:])),
        "grade_max_percent": 100 * grade,
        "radius_min_plan_m": _minimum_radius(segments),
        "plan": {
            "kind": "single-cubic-exact-plan-length-slip-lane",
            "target_length_plan_m": target_length,
            "highway_half_length_m": half,
            "cubic_segments_canonical_uv": segments,
        },
        "profile": {
            "level_departure_length_m": descent_start,
            "descent_or_ascent_length_m": transition,
            "ground_landing_length_m": landing,
            "grade_taper_length_m": taper,
            "clearance_start_abs_v_m": abs(points_uv[clear_index][1]),
            "minimum_declared_clear_abs_v_m": clear,
        },
    }


def _turn(route_id: str, start: tuple[float, float], end: tuple[float, float], start_heading: tuple[int, int], end_heading: tuple[int, int], count: int) -> dict:
    # Separate quarter-ellipse handles prevent the tighter turn from
    # overshooting its destination lane before it adopts the lane heading.
    delta = [abs(end[axis] - start[axis]) for axis in (0, 1)]
    factor = 4 * (math.sqrt(2) - 1) / 3
    controls = [start, tuple(start[axis] + factor * delta[axis] * start_heading[axis] for axis in (0, 1)), tuple(end[axis] - factor * delta[axis] * end_heading[axis] for axis in (0, 1)), end]
    local = [[u, v, 0.0] for u, v in _bezier(controls, count)]
    return {"id": route_id, "kind": "surface-turn", "points": [_world(*point) for point in local], "points_uvz": local, "width_m": 3.0}


def build_geometry(design: dict) -> dict:
    """Return the roads, directed graph, and sampled geometric prototype."""
    params = {key: design.get("geometry", {}).get(key, design.get(key, value)) for key, value in DEFAULTS.items()}
    for key, value in params.items():
        if not isinstance(value, (float, int)) or isinstance(value, bool) or not math.isfinite(value) or value <= 0:
            raise ValueError(f"{key} must be a positive finite number.")
    if int(params["samples_per_route"]) != params["samples_per_route"] or params["samples_per_route"] < 101:
        raise ValueError("samples_per_route must be an integer of at least 101.")
    params["samples_per_route"] = int(params["samples_per_route"])
    if params["upper_height_m"] <= params["lower_height_m"]:
        raise ValueError("Upper deck must be higher than the lower deck.")
    if params["highway_lane_offset_m"] >= params["highway_width_m"] / 2:
        raise ValueError("Highway lane spine must lie inside its provisional deck.")
    if params["avenue_lane_offset_m"] >= params["avenue_width_m"] / 2:
        raise ValueError("Avenue lane spine must lie inside the avenue surface.")
    minimum_clear = params["highway_width_m"] / 2 + params["ramp_width_m"] / 2 + params["lateral_clearance_m"]
    if params["descent_clear_v_m"] < minimum_clear:
        raise ValueError("descent_clear_v_m does not clear the whole ramp width, lower deck width, and declared lateral buffer.")
    if params["junction_offset_m"] <= params["descent_clear_v_m"]:
        raise ValueError("Avenue intersections must lie beyond the stacked-road clearance envelope.")
    half = params["highway_half_length_m"]
    if half <= params["avenue_width_m"] / 2:
        raise ValueError("Highway half-length must extend beyond the avenue edges.")
    for position_key, target_key in (("highway_half_length_m", "upper_ramp_plan_length_m"), ("lower_highway_join_m", "lower_ramp_plan_length_m")):
        resolved_half = solve_highway_half_length(params, params[target_key])
        if not math.isclose(params[position_key], resolved_half, rel_tol=0, abs_tol=0.005):
            raise ValueError(f"{position_key} does not match the requested complete {target_key}; solve the joining position again.")
    lower_join = params["lower_highway_join_m"]
    if lower_join >= half:
        raise ValueError("Lower highway branch joins must lie inside the longer upper-ramp highway extent.")
    junction = params["junction_offset_m"]
    lane = params["highway_lane_offset_m"]
    av_lane = params["avenue_lane_offset_m"]
    mouth = params["avenue_width_m"] / 2
    approach = 18.0
    if junction <= approach + params["highway_width_m"] / 2:
        raise ValueError("Surface turning envelopes overlap the highway core.")
    if params["avenue_approach_length_m"] <= approach:
        raise ValueError("Avenue approach must extend beyond the surface turn connectors.")
    avenue_half = junction + params["avenue_approach_length_m"]
    routes = []
    roads = []
    highway_samples = [-half + 2 * half * index / (params["samples_per_route"] - 1) for index in range(params["samples_per_route"])]
    for deck, height, side, source, target, direction in (("upper", params["upper_height_m"], -1, "SW", "NE", 1), ("lower", params["lower_height_m"], 1, "NE", "SW", -1)):
        road_points = [_world(u, 0, height) for u in highway_samples]
        roads.append({"id": f"highway-{deck}", "kind": "highway", "deck": deck, "width_m": params["highway_width_m"], "points": road_points})
        if deck == "upper":
            segments = [("highway-upper-through", source, target, -half, half)]
        else:
            segments = [("highway-lower-approach", "NE", "lower-branch-in", half, lower_join), ("highway-lower-through", "lower-branch-in", "lower-branch-out", lower_join, -lower_join), ("highway-lower-departure", "lower-branch-out", "SW", -lower_join, -half)]
        for route_id, start, finish, first_u, last_u in segments:
            count = max(21, round((params["samples_per_route"] - 1) * abs(last_u - first_u) / (2 * half)) + 1)
            uvz = [[first_u + (last_u - first_u) * index / (count - 1), side * lane, height] for index in range(count)]
            routes.append({"id": route_id, "kind": "highway-through", "from": start, "to": finish, "deck": deck, "width_m": 3.0, "points_uvz": uvz, "points": [_world(*point) for point in uvz]})
    ramp_contracts = (("upper-off", -1, 1, params["upper_height_m"], False, "SW", "se-off-mouth"), ("upper-on", -1, 1, params["upper_height_m"], True, "se-on-mouth", "NE"), ("lower-off", 1, -1, params["lower_height_m"], False, "lower-branch-in", "nw-off-mouth"), ("lower-on", 1, -1, params["lower_height_m"], True, "nw-on-mouth", "lower-branch-out"))
    for route_id, side, direction, height, on, source, target in ramp_contracts:
        route = _ramp(params, route_id, side, direction, height, on)
        route.update({"from": source, "to": target})
        routes.append(route)
        roads.append({**route, "id": f"ramp-{route_id}"})
    cut_values = sorted({-avenue_half, avenue_half, -junction - approach, -junction + approach, junction - approach, junction + approach})
    avenue_points = [_world(0, -avenue_half + 2 * avenue_half * index / (params["samples_per_route"] - 1), 0) for index in range(params["samples_per_route"])]
    roads.append({"id": "avenue", "kind": "avenue", "width_m": params["avenue_width_m"], "points": avenue_points})
    avenue_nodes = {}
    for direction, lane_offset, source, target in ((1, av_lane, "SE", "NW"), (-1, -av_lane, "NW", "SE")):
        ordered = cut_values[::direction]
        tag = "nw-bound" if direction > 0 else "se-bound"
        nodes = [source] + [f"avenue-{tag}-{value:+.6f}" for value in ordered[1:-1]] + [target]
        for value, node in zip(ordered, nodes):
            avenue_nodes[(direction, value)] = node
        for index, (first, last) in enumerate(zip(ordered, ordered[1:])):
            local = [[lane_offset, first + (last - first) * i / 20, 0.0] for i in range(21)]
            routes.append({"id": f"avenue-{tag}-{index + 1}", "kind": "avenue-through", "from": nodes[index], "to": nodes[index + 1], "width_m": 3.0, "points_uvz": local, "points": [_world(*point) for point in local]})
    for deck, side, highway_direction, name in (("upper", -1, 1, "se"), ("lower", 1, -1, "nw")):
        v_junction = side * junction
        off_point = (-highway_direction * mouth, v_junction)
        on_point = (highway_direction * mouth, v_junction)
        for avenue_direction, arm in ((1, "NW"), (-1, "SE")):
            target_v = v_junction + avenue_direction * approach
            off_turn = _turn(f"{deck}-off-to-{arm}", off_point, (avenue_direction * av_lane, target_v), (highway_direction, 0), (0, avenue_direction), 81)
            off_turn.update({"from": f"{name}-off-mouth", "to": avenue_nodes[(avenue_direction, target_v)]})
            routes.append(off_turn)
            source_v = v_junction - avenue_direction * approach
            source_arm = "SE" if avenue_direction > 0 else "NW"
            on_turn = _turn(f"{source_arm}-to-{deck}-on", (avenue_direction * av_lane, source_v), on_point, (0, avenue_direction), (highway_direction, 0), 81)
            on_turn.update({"from": avenue_nodes[(avenue_direction, source_v)], "to": f"{name}-on-mouth"})
            routes.append(on_turn)
    required = [{"from": source, "to": target} for source, target in (("SW", "NE"), ("NE", "SW"), ("NW", "SE"), ("SE", "NW"), ("SW", "NW"), ("SW", "SE"), ("NE", "NW"), ("NE", "SE"), ("NW", "NE"), ("SE", "NE"), ("NW", "SW"), ("SE", "SW"))]
    all_points = [point for road in roads for point in road["points"]]
    bounds = {axis: [min(point[index] for point in all_points), max(point[index] for point in all_points)] for index, axis in enumerate(("east", "north", "height"))}
    return {
        "schema_version": 1,
        "metadata": {
            "title": design.get("title", "Diagonal double-decker highway and avenue diamond"),
            "status": "source-only-geometric-prototype",
            "parameters": params,
            "coordinates": "[east,north,height] metres; u=NE, v=NW",
            "bounds_m": bounds,
            "avenue_half_length_m": avenue_half,
            "minimum_lateral_separation_m": minimum_clear,
            "surface_intersection_turn_offset_m": approach,
            "slip_lane_corridor_width_m": 2 * (junction + params["ramp_width_m"] / 2),
            "ramp_length_definition": "The complete ramp's horizontal sampled arc length is the requested plan length; length_3d_m also includes its height change.",
            "native_seams": "unverified; corridor spines are not native lane boundaries",
            "clearance_scope": "Planar ramp width versus provisional deck envelope only; supports, deck thickness, vehicle solids, and swept turn corridors remain unverified.",
            "indirect_return_journeys": "Avenue-mediated returns to the same highway arm are possible; there are no direct deck-transfer or U-turn edges.",
            "construction": "No tile ownership, placement rules, game resources, controller, menu, installation, or in-game evidence is provided.",
        },
        "roads": roads,
        "routes": routes,
        "intersections": [{"id": name, "position": _world(0, side * junction, 0), "position_uvz": [0, side * junction, 0], "conflict_type": "surface-intersection-with-turning-conflicts", "arms": 4, "signals_or_priority": "unimplemented"} for name, side in (("junction-se", -1), ("junction-nw", 1))],
        "required_movements": required,
    }


generate_geometry = build_geometry


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--design", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    result = build_geometry(load_design(args.design))
    result["source"] = {"design_sha256": hashlib.sha256(args.design.read_bytes()).hexdigest(), "design_filename": args.design.name}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(result['roads'])} road surfaces and {len(result['routes'])} directed route segments.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
