#!/usr/bin/env python3
"""Sample the first DD RHW Y design; emit no game resources or connector exports.

The report describes native-anchored source polylines and provisional clearance
bounds. It is not a saved-PATH check, a model check, or an in-game observation.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import math
from pathlib import Path
import sys

import numpy as np

HIGHWAY = Path(__file__).resolve().parents[1]
FRAMEWORK = HIGHWAY.parents[1] / "framework"
if str(FRAMEWORK) not in sys.path:
    sys.path.insert(0, str(FRAMEWORK))
from scp import jsonc

SUBJECT = HIGHWAY / "01_assemblies/ddrhw-compact-diagonal-y-junction"
ROUTES = (
    ("A-B", ("A", "L2", 1, "native-to-core"), ("B", "L2", 1, "core-to-native")),
    ("B-A", ("B", "L1", 0, "native-to-core"), ("A", "L1", 0, "core-to-native")),
    ("A-C", ("A", "L2", 0, "native-to-core"), ("C", "L2", 0, "core-to-native")),
    ("C-A", ("C", "L1", 1, "native-to-core"), ("A", "L1", 1, "core-to-native")),
    ("B-C", ("B", "L1", 1, "native-to-core"), ("C", "L2", 1, "core-to-native")),
    ("C-B", ("C", "L1", 0, "native-to-core"), ("B", "L2", 0, "core-to-native")),
)
HEADER = '''// title: "Compact DD RHW Y source geometry"
// summary: "Record the first native-anchored six-route design and its bounded source checks."
//
// Used when: Reviewing or regenerating the first compact DD RHW Y source candidate.
// Read by: Authors, independent source reviewers, and the schematic renderer.
// Updated by: domains/highway/tools/ddrhw_y_geometry.py from the design brief and native audit.
// Affects: Proposed lane routes, source grade and proximity checks, and provisional layout bounds; no game resources or observations.
'''


def bezier(points, t):
    """Evaluate a planar Bezier polynomial at all supplied parameters."""
    degree = len(points) - 1
    result = np.zeros((len(t), 2))
    for index, point in enumerate(points):
        basis = math.comb(degree, index) * (1-t)**(degree-index) * t**index
        result += basis[:, None] * point
    return result


def planar_route(start, end, incoming, outgoing, parameters, bulge):
    """Keep exact flat collars, then sample an eased planar curve."""
    collar = parameters["native_collar_m"]
    handle = parameters["handle_m"]
    p0, p5 = start + incoming*collar, end - outgoing*collar
    controls = [p0, p0+incoming*handle, p0+incoming*(2*handle),
                p5-outgoing*(2*handle), p5-outgoing*handle, p5]
    t = np.linspace(0.0, 1.0, 1501)
    xy = bezier(controls, t)
    if bulge:
        derivative = bezier([5*(controls[k+1]-controls[k]) for k in range(5)], t)
        derivative /= np.linalg.norm(derivative, axis=1)[:, None]
        normal = np.column_stack([-derivative[:, 1], derivative[:, 0]])
        xy += (bulge*np.sin(np.pi*t)**4)[:, None] * normal
    # Separate linear pieces make both collars exact in the resulting polyline.
    collar_stations = np.linspace(0.0, collar, max(2, math.ceil(collar)+1))
    xy = np.vstack([start + collar_stations[:-1, None]*incoming, xy,
                    end - collar_stations[-2::-1, None]*outgoing])
    station = np.r_[0.0, np.linalg.norm(np.diff(xy, axis=0), axis=1).cumsum()]
    regular = np.linspace(0.0, station[-1], math.ceil(station[-1]/parameters["sampling_step_m"])+1)
    breaks = np.r_[collar_stations, station[-1]-collar_stations]
    target = np.unique(np.r_[regular, breaks])
    return np.column_stack([np.interp(target, station, xy[:, k]) for k in range(2)]), target


def posed_members(native_audit, parameters):
    """Move measured outside cells by whole native-grid steps, retaining poses."""
    diagonal, orthogonal = parameters["diagonal_cell"], parameters["orthogonal_cell"]
    desired = {"A": [-diagonal, diagonal], "B": [-diagonal, -diagonal], "C": [orthogonal, 0]}
    members, sockets = {}, []
    for original in native_audit["first_alignment_socket_example"]:
        socket = copy.deepcopy(original)
        arm = socket["arm"]
        old = np.asarray(socket["outside_cell_col_row"], dtype=float)
        new = np.asarray(desired[arm], dtype=float)
        delta = np.array([16*(new[0]-old[0]), -16*(new[1]-old[1]), 0.0])
        socket["outside_cell_col_row"] = desired[arm]
        socket["outside_world_centre_en_m"] = [16*desired[arm][0], -16*desired[arm][1]]
        for member in socket["members"]:
            member["endpoint_enh_m"] = (np.asarray(member["endpoint_enh_m"])+delta).tolist()
            key = (arm, member["level"], member["lane"], member["direction"])
            if key in members:
                raise ValueError(f"Duplicate measured native member: {key}")
            members[key] = member
        sockets.append(socket)
    if len(members) != 12:
        raise ValueError("Expected twelve complete exterior native members")
    return members, sockets


def route_measurements(points, station, start, end, collar):
    """Measure the actual source polyline, including native endpoint collars."""
    steps = np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1)
    grades = np.diff(points[:, 2])/steps
    tangent = np.gradient(points[:, :2], axis=0)
    acceleration = np.gradient(tangent, axis=0)
    curvature = np.abs(tangent[:, 0]*acceleration[:, 1]-tangent[:, 1]*acceleration[:, 0]) / np.linalg.norm(tangent, axis=1)**3
    errors = []
    for member, selector, distance, sign in (
        (start, station <= collar+1e-10, station, 1),
        (end, station >= station[-1]-collar-1e-10, station[-1]-station, -1),
    ):
        target = np.asarray(member["endpoint_enh_m"]) + sign*distance[selector, None]*np.asarray(member["unit_travel_tangent_enh"])
        errors.append(float(np.linalg.norm(points[selector]-target, axis=1).max()))
    if max(errors) > 1e-9:
        raise ValueError(f"Native source collar mismatch: {errors}")
    return {"length": float(steps.sum()), "max_step": float(steps.max()),
            "maximum_grade": float(np.abs(grades).max()),
            "minimum_radius": float(1.0/curvature.max()),
            "native_collar_maximum_position_error_m": max(errors),
            "start_endpoint_error_m": float(np.linalg.norm(points[0]-start["endpoint_enh_m"])),
            "end_endpoint_error_m": float(np.linalg.norm(points[-1]-end["endpoint_enh_m"]))}


def generate(parameters, native_audit):
    """Return six complete directed source polylines and their native bindings."""
    members, sockets = posed_members(native_audit, parameters)
    output, used = {}, []
    for name, start_key, end_key in ROUTES:
        start, end = members[start_key], members[end_key]
        if any(member["transport"] != 1 or member["compatibility"] != 0 for member in (start, end)):
            raise ValueError("Only the measured real car members are supported")
        if start["lane"] != end["lane"]:
            raise ValueError("This candidate preserves every native lane class")
        used.extend([start_key, end_key])
        beginning, ending = np.asarray(start["endpoint_enh_m"]), np.asarray(end["endpoint_enh_m"])
        incoming = np.asarray(start["unit_travel_tangent_enh"][:2])
        outgoing = np.asarray(end["unit_travel_tangent_enh"][:2])
        climbing = ending[2] != beginning[2]
        xy, station = planar_route(beginning[:2], ending[:2], incoming, outgoing,
                                   parameters, parameters["bulge_m"] if climbing else 0.0)
        q = np.clip((station/station[-1]-parameters["rise_start_fraction"])
                    /(parameters["rise_end_fraction"]-parameters["rise_start_fraction"]), 0.0, 1.0)
        smooth = q*q*q*(10.0+q*(-15.0+6.0*q))
        height = beginning[2] + (ending[2]-beginning[2])*smooth
        points = np.column_stack([xy, height])
        measurement = route_measurements(points, station, start, end, parameters["native_collar_m"])
        output[name] = {"points": points, "measurements": measurement,
                        "native_start": list(start_key), "native_end": list(end_key),
                        "engine_lane_class": start["lane"], "transport": 1, "compatibility": 0}
    if len(set(used)) != 12 or set(used) != set(members):
        raise ValueError("Every complete external native member must be used exactly once")
    return output, sockets


def pair_clearance(routes, parameters):
    """Exhaustive sampled proximity with conservative polyline spacing margins.

    These checks bound round horizontal neighbourhoods of source route segments.
    They do not establish full vehicle bodies, pavement unions, barriers, native
    mesh projections, supports, or structural capacity.
    """
    results = []
    width, height = parameters["vehicle_width_m"], parameters["vehicle_height_m"]
    road_width, depth = parameters["provisional_pavement_width_m"], parameters["provisional_deck_depth_m"]
    for name_a, name_b in itertools.combinations(routes, 2):
        a, b = routes[name_a], routes[name_b]
        allowance = a["measurements"]["max_step"] + b["measurements"]["max_step"]
        grade = max(a["measurements"]["maximum_grade"], b["measurements"]["maximum_grade"])
        vehicle_min, road_min = math.inf, math.inf
        for offset in range(0, len(a["points"]), 128):
            chunk = a["points"][offset:offset+128]
            xy = np.linalg.norm(chunk[:, None, :2]-b["points"][None, :, :2], axis=2)
            dz = np.abs(chunk[:, None, 2]-b["points"][None, :, 2])
            vehicle_min = min(vehicle_min, float(np.where(dz < height+allowance*grade, xy, np.inf).min()))
            # Exact coplanar adjacent roads require a coordinated pavement owner;
            # this experiment checks their distinct vehicle envelopes only.
            gate = (dz < height+depth+allowance*grade) & (dz > 1e-7)
            road_min = min(road_min, float(np.where(gate, xy, np.inf).min()))
        results.append({"routes": [name_a, name_b], "plan_sampling_allowance_m": allowance,
                        "vehicle_distance_lower_bound_m": None if math.isinf(vehicle_min) else vehicle_min-allowance,
                        "noncoplanar_road_vehicle_distance_lower_bound_m": None if math.isinf(road_min) else road_min-allowance,
                        "vehicle_bound_pass": vehicle_min-allowance > width,
                        "provisional_road_vehicle_bound_pass": road_min-allowance > (road_width+width)/2})
    return results


def projection_bounds(routes, width):
    """Bound the sampled, unclipped illustrative strips, not construction owners."""
    centre, strips = [], []
    for route in routes.values():
        xy = route["points"][:, :2]
        direction = np.gradient(xy, axis=0)
        direction /= np.linalg.norm(direction, axis=1)[:, None]
        normal = np.column_stack([-direction[:, 1], direction[:, 0]])
        centre.append(xy)
        strips.extend([xy-width/2*normal, xy+width/2*normal])
    def bounds(points):
        values = np.vstack(points)
        low, high = values.min(axis=0), values.max(axis=0)
        columns = [math.floor((low[0]+8)/16), math.ceil((high[0]+8)/16)-1]
        rows = [math.floor((-high[1]+8)/16), math.ceil((-low[1]+8)/16)-1]
        return {"east_min_max_m": [float(low[0]), float(high[0])],
                "north_min_max_m": [float(low[1]), float(high[1])],
                "illustrative_grid_columns": columns, "illustrative_grid_rows": rows,
                "illustrative_grid_rectangle_tiles": [columns[1]-columns[0]+1, rows[1]-rows[0]+1]}
    return {"scope": "Sampled source strips, unclipped at sockets; includes native approach overlap and is not an owned-tile footprint.",
            "centrelines": bounds(centre), "provisional_road_strips": bounds(strips)}


def build_design(brief, audit, source_fingerprints=None):
    """Build a portable source report from parsed brief and native-audit objects."""
    p = brief["geometry_parameters"]
    if not 0.0 < p["rise_start_fraction"] < p["rise_end_fraction"] < 1.0:
        raise ValueError("The two level endpoint runs must surround an active ramp interval")
    if p["sampling_step_m"] <= 0 or p["native_collar_m"] <= 0:
        raise ValueError("Sampling step and native collar length must be positive")
    routes, sockets = generate(p, audit)
    checks = pair_clearance(routes, p)
    limit = brief["requirements"]["maximum_grade_percent"]/100
    if not math.isfinite(limit) or not 0 < limit <= 0.30:
        raise ValueError("The source grade limit must be positive and no greater than thirty percent")
    return {"schema_version": 1, "title": "Compact DD RHW Y first source candidate",
            "scope": "First grid alignment only; native-anchored source polylines, not compiled pieces or compatibility exports.",
            "input_fingerprints": source_fingerprints or {},
            "coordinate_frame": "east, north, height in metres; tile centres are (16*column, -16*row)",
            "parameters": p, "experimental_maximum_grade": limit,
            "native_socket_members": sockets,
            "routes": {name: data["points"].tolist() for name, data in routes.items()},
            "route_measurements": {name: data["measurements"] for name, data in routes.items()},
            "route_metadata": {name: {"from_arm": data["native_start"][0], "to_arm": data["native_end"][0],
                                      "from_deck": data["native_start"][1], "to_deck": data["native_end"][1],
                                      "from_lane": data["engine_lane_class"], "to_lane": data["engine_lane_class"],
                                      "engine_transport": data["transport"], "compatibility": data["compatibility"]}
                               for name, data in routes.items()},
            "pair_checks": checks,
            "projection_bounds": projection_bounds(routes, p["provisional_pavement_width_m"]),
            "checks": {"all_twelve_native_members_used_once": True,
                       "exact_native_endpoint_and_collar_checks": True,
                       "source_polyline_grade_pass": all(x["measurements"]["maximum_grade"] <= limit for x in routes.values()),
                       "sampled_vehicle_clearance_pass": all(x["vehicle_bound_pass"] for x in checks),
                       "provisional_sampled_road_vehicle_clearance_pass": all(x["provisional_road_vehicle_bound_pass"] for x in checks)},
            "unverified": ["Actual native pavement datums and full physical profiles, including the approximately 1 mm donor differences.",
                           "Continuous analytic curve radius; the radius measurement is sampled and diagnostic.",
                           "Coplanar pavement unions, barrier openings, deck solids, supports, overhangs, and swept vehicle bodies.",
                           "Construction ownership, reusable module cuts, game identifiers, saved resources, placement, and native dragging.",
                           "Other grid alignments, installation, visible traffic, Route Query, demolition, and save/reload."]}


def build_report(brief_path, audit_path):
    """Read public JSONC sources and bind their exact input fingerprints."""
    fingerprints = {"design_brief_sha256": hashlib.sha256(brief_path.read_bytes()).hexdigest(),
                    "native_design_inputs_sha256": hashlib.sha256(audit_path.read_bytes()).hexdigest(),
                    "geometry_tool_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return build_design(jsonc.load(brief_path), jsonc.load(audit_path), fingerprints)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brief", type=Path, default=SUBJECT/"checks/design-brief.jsonc")
    parser.add_argument("--native-audit", type=Path, default=SUBJECT/"evidence/native-design-inputs.jsonc")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    report = build_report(args.brief, args.native_audit)
    args.output.mkdir(parents=True, exist_ok=True)
    destination = args.output/"design-geometry.jsonc"
    if not destination.exists():
        destination.write_text(HEADER, encoding="utf-8")
    jsonc.dump(destination, report)
    print(f"Six source routes; {len(report['pair_checks'])} pair checks; checks={report['checks']}")
    return 0 if all(report["checks"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
