"""Directed road PATHs, exact city-grid cuts, and proper planar rotations.

Coordinates are SC4PATH metres: east, north, and height. Construction cells
are (column, row), with centres at (16*column, -16*row). The module never
borrows Monorail transport numbers or the HSR domain's reference elevation.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from functools import lru_cache
import math

EPSILON = 1e-7
TILE_SIZE = 16.0
CAR = 1
PEDESTRIAN = 2


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _snap(value):
    closest = round((value + 8.0) / 16.0) * 16.0 - 8.0
    return closest if abs(value - closest) < EPSILON else value


def edge(point, tangent=None):
    """Return native W/N/E/S = 0/1/2/3 for a local endpoint.

    An endpoint at a tile corner is ambiguous without its travel tangent;
    callers must make the intended crossing explicit rather than guessing.
    """
    x, y = point[:2]
    choices = [i for i, distance in enumerate((x + 8.0, y - 8.0, x - 8.0, y + 8.0))
               if abs(distance) < EPSILON]
    if len(choices) == 2 and tangent is not None:
        dx, dy = tangent[:2]
        choices = [i for i in choices if abs((dx, dy)[i % 2]) > EPSILON]
    _require(len(choices) == 1, f"A road endpoint must cross one unambiguous tile side: {point}")
    return choices[0]


def polyline_fragments(points):
    """Cut sampled XYZ points at every exact tile-side intersection.

    Each returned pair is (cell, local_points). Consecutive fragments in the
    same cell are joined; a later re-entry remains a separate directed path.
    Heights use the same linear interpolation as the compiled mesh samples.
    """
    _require(len(points) >= 2, "A road route needs at least two points")
    _require(all(len(p) == 3 and all(math.isfinite(v) for v in p) for p in points),
             "Road route points must contain three finite coordinates")
    output = []
    for first, last in zip(points, points[1:]):
        _require(math.dist(first[:2], last[:2]) > 1e-12, "A road route contains a stationary planar segment")
        cuts = [0.0, 1.0]
        for axis in (0, 1):
            delta = last[axis] - first[axis]
            if abs(delta) < 1e-12:
                continue
            low, high = sorted((first[axis], last[axis]))
            for grid in range(math.floor((low + 8.0) / 16.0), math.ceil((high + 8.0) / 16.0) + 1):
                fraction = (16.0 * grid - 8.0 - first[axis]) / delta
                if 1e-11 < fraction < 1.0 - 1e-11:
                    cuts.append(fraction)
        cuts = sorted(set(round(value, 13) for value in cuts))
        for low, high in zip(cuts, cuts[1:]):
            middle = tuple(first[a] + (low + high) * 0.5 * (last[a] - first[a]) for a in range(3))
            cell = math.floor((middle[0] + 8.0) / 16.0), math.floor((8.0 - middle[1]) / 16.0)
            pair = []
            for fraction in (low, high):
                world = tuple(first[a] + fraction * (last[a] - first[a]) for a in range(3))
                pair.append((_snap(world[0] - 16.0 * cell[0]),
                             _snap(world[1] + 16.0 * cell[1]), world[2]))
            if output and output[-1][0] == cell and math.dist(output[-1][1][-1], pair[0]) < EPSILON:
                if math.dist(output[-1][1][-1], pair[1]) > EPSILON:
                    output[-1][1].append(pair[1])
            else:
                output.append((cell, pair))
    return output


def slice_routes(routes):
    """Return tile-local real car/pedestrian routes, retaining lane identities.

    Input routes require ``points`` and may supply ``transport`` (1 or 2),
    ``lane``, ``junction``, and ``id``. Interior route ends require an explicit
    ``allow_interior_ends`` flag: these are suitable only when the caller has
    deliberately supplied the matching junction continuation in that tile.
    Ordinary native joins must finish on a tile side.
    """
    result = defaultdict(list)
    for number, route in enumerate(routes):
        transport = route.get("transport", CAR)
        _require(transport in (CAR, PEDESTRIAN), "Highway routes must use actual car or pedestrian transport")
        parts = polyline_fragments(route["points"])
        for index, (cell, points) in enumerate(parts):
            tangents = [(points[1][a] - points[0][a] for a in (0, 1)),
                        (points[-1][a] - points[-2][a] for a in (0, 1))]
            tangent_in, tangent_out = map(tuple, tangents)
            ends = []
            for endpoint, tangent, terminal in ((points[0], tangent_in, index == 0),
                                                (points[-1], tangent_out, index == len(parts) - 1)):
                on_side = any(abs(abs(endpoint[axis]) - 8.0) < EPSILON for axis in (0, 1))
                if not on_side:
                    _require(terminal and route.get("allow_interior_ends", False),
                             f"Road route {route.get('id', number)} has an unjoined interior endpoint in {cell}")
                    ends.append(255)
                else:
                    ends.append(edge(endpoint, tangent))
            result[cell].append({"transport": transport, "lane": int(route.get("lane", 0)),
                                 "entry": ends[0], "exit": ends[1],
                                 "junction": bool(route.get("junction", False)), "points": points,
                                 "id": route.get("id", f"route-{number}"),
                                 "tangent_in": tangent_in, "tangent_out": tangent_out})
    return dict(result)


def encode_paths(routes, *, allow_empty=False):
    """Encode SC4PATHS 1.2 without replacing highway transport with rail.

    Class numbers are unique within each transport/entry/exit combination.
    This avoids duplicate classes after several authored movements are cut
    into the same city tile. The source ``lane`` is retained in comments.
    """
    _require(routes or allow_empty, "A PATH resource needs at least one road route")
    used_classes = defaultdict(set)
    lines = ["SC4PATHS", "1.2", str(len(routes)), "0", "0"]
    for route in routes:
        transport = route.get("transport", CAR)
        _require(transport in (CAR, PEDESTRIAN), "Only real road traffic is supported by this compiler")
        pair = transport, route["entry"], route["exit"]
        lane = int(route.get("lane", 0))
        while lane in used_classes[pair]:
            lane += 1
        used_classes[pair].add(lane)
        lines += [f"-- SCP {route.get('id', 'road')} source_lane={route.get('lane', 0)}",
                  str(transport), str(lane), str(route["entry"]), str(route["exit"]),
                  str(int(route.get("junction", False))), str(len(route["points"]))]
        lines += [",".join(format(float(value), ".9f").rstrip("0").rstrip(".") if value else "0"
                           for value in point) for point in route["points"]]
    return ("\r\n".join(lines) + "\r\n").encode("ascii")


def rotate_points(points, quarter_turns=1, origin=(0.0, 0.0)):
    """Rotate clockwise in quarter turns; never reflect traffic handedness."""
    output = []
    for east, north, height in points:
        x, y = east - origin[0], north - origin[1]
        for _ in range(quarter_turns % 4):
            x, y = y, -x
        output.append((x + origin[0], y + origin[1], height))
    return output


def rotate_routes(routes, quarter_turns=1, origin=(0.0, 0.0)):
    result = deepcopy(routes)
    for route in result:
        route["points"] = rotate_points(route["points"], quarter_turns, origin)
        if "entry" in route:
            route["entry"] = (route["entry"] + quarter_turns) % 4 if route["entry"] != 255 else 255
            route["exit"] = (route["exit"] + quarter_turns) % 4 if route["exit"] != 255 else 255
        for key in ("tangent_in", "tangent_out"):
            if key in route:
                route[key] = rotate_points([(*route[key], 0.0)], quarter_turns)[0][:2]
    return result


def construction_flags(routes):
    """Encode diagonal versus orthogonal road approaches from actual tangents."""
    sides = [0, 0, 0, 0]
    for route in routes:
        for side, tangent in ((route["entry"], route["tangent_in"]),
                              (route["exit"], route["tangent_out"])):
            if side == 255:
                continue
            dx, dy = tangent
            value = 2 if abs(dx) < EPSILON or abs(dy) < EPSILON else (
                (3 if dx * dy > 0.0 else 1) if side in (1, 3) else (1 if dx * dy > 0.0 else 3))
            sides[side] = 2 if value == 2 or sides[side] == 2 else value
    return sum(value << (8 * side) for side, value in enumerate(sides))


def mark_junctions(tile_routes, *, tolerance=1e-5):
    """Mark real car split/merge paths sharing a directed tile-side endpoint.

    Both divergent paths and converging paths are flagged. Pedestrian routes
    remain independent, and opposite-direction traffic is never inferred to
    be a junction merely because its endpoints happen to coincide.
    """
    result = deepcopy(tile_routes)
    for routes in result.values():
        groups = defaultdict(list)
        for route in routes:
            if route["transport"] != CAR:
                continue
            for key, point in (("start", route["points"][0]), ("end", route["points"][-1])):
                groups[key, tuple(round(value / tolerance) for value in point)].append(route)
        for group in groups.values():
            if len(group) > 1:
                for route in group:
                    route["junction"] = True
    return result


def deduplicate_routes(tile_routes):
    """Coalesce identical saved car lanes before assigning lane classes."""
    result = {}
    for cell, routes in tile_routes.items():
        seen = {}
        for route in routes:
            key = (route["transport"], route["entry"], route["exit"],
                   tuple(tuple(round(value, 8) for value in point) for point in route["points"]))
            if key not in seen:
                seen[key] = deepcopy(route)
            else:
                seen[key]["junction"] = seen[key]["junction"] or route.get("junction", False)
        result[cell] = list(seen.values())
    return result


def _surface_turn(start, finish, heading_in, heading_out, count=81):
    """Build an actual ground turn with exact incoming/outgoing tangents."""
    factor = 4.0 * (math.sqrt(2.0) - 1.0) / 3.0
    difference = [finish[axis] - start[axis] for axis in (0, 1)]
    along_in = sum(a * b for a, b in zip(difference, heading_in))
    along_out = sum(a * b for a, b in zip(difference, heading_out))
    _require(along_in > 0.0 and along_out > 0.0, "Surface turn headings must reach their actual destination lane")
    radius = min(along_in, along_out)
    if max(along_in, along_out) < 2.0 * radius:
        # A near-circular left turn can occupy the whole available box. This
        # also avoids inventing a short straight directly through a grid
        # corner on the diagonal ramp mouth's internal reference axis.
        curve_start, curve_end = start, finish
        radius_in, radius_out = along_in, along_out
    else:
        curve_start = tuple(start[a] + (along_in - radius) * heading_in[a] for a in (0, 1))
        curve_end = tuple(finish[a] - (along_out - radius) * heading_out[a] for a in (0, 1))
        radius_in = radius_out = radius
    controls = [curve_start, tuple(curve_start[a] + factor * radius_in * heading_in[a] for a in (0, 1)),
                tuple(curve_end[a] - factor * radius_out * heading_out[a] for a in (0, 1)), curve_end]
    points = [] if math.dist(start, curve_start) < 1e-8 else [start]
    for index in range(count):
        t = index / (count - 1)
        weights = ((1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3)
        points.append(tuple(sum(w * p[axis] for w, p in zip(weights, controls)) for axis in (0, 1)))
    if math.dist(curve_end, finish) >= 1e-8:
        points.append(finish)
    return points


def _avenue_boundary(u, v, travel_direction, *, beyond):
    """Find the next exact native Avenue port beyond a local turn endpoint."""
    from .ramp_geometry import world_coordinates
    candidates = []
    root = math.sqrt(2.0)
    center = world_coordinates(u, v)
    for axis in (0, 1):
        for number in range(math.floor((center[axis] + 8.0) / 16.0) - 3,
                            math.floor((center[axis] + 8.0) / 16.0) + 4):
            grid = 16.0 * number - 8.0
            possible = u - (grid - 4.0) * root if axis == 0 else (grid + 4.0) * root - u
            distance = (possible - v) * travel_direction * (1 if beyond else -1)
            if distance >= 1e-7:
                candidates.append((distance, possible))
    _require(candidates, "Could not find the native Avenue joining boundary")
    return min(candidates)[1]


def compact_access_routes(ramps=None):
    """Compile four right-turn highway/Avenue transfers at ground level.

    Each complete route begins and ends on an actual native tile-side lane:
    an outer DD lane at one end and a measured outer Avenue lane at the
    other. Ramp mouths are deliberately internal nodes, never unjoined
    direction-255 endpoints. Avenue through lanes and its two pedestrian
    channels belong to the retained native tile owner and must be included
    separately by the final module compiler.
    """
    from .ramp_geometry import compact_ramps, highway_coordinates, world_coordinates
    ramps = compact_ramps() if ramps is None else ramps
    result = []
    outer = 11.2 / math.sqrt(2.0)
    for ramp in ramps:
        on = ramp["direction"] == "on"
        mouth = ramp["points"][0 if on else -1]
        mouth_u, mouth_v = highway_coordinates(mouth)
        highway_direction = -1 if ramp["deck"] == "lower" else 1
        # A right turn reaches only the adjacent Avenue carriageway. The
        # opposing carriageway has no crossing PATH or asphalt turn apron.
        avenue_direction = ramp["side"]
        arm = "NW" if avenue_direction == 1 else "SE"
        # Off-ramp direction names the destination. On-ramp direction
        # names its source, whose traffic heads towards the junction.
        travel = -avenue_direction if on else avenue_direction
        avenue_u = travel * outer
        avenue_v = mouth_v + avenue_direction * 18.0
        port_v = _avenue_boundary(avenue_u, avenue_v, travel, beyond=not on)
        port = world_coordinates(avenue_u, port_v)
        avenue_point = avenue_u, avenue_v
        mouth_point = mouth_u, mouth_v
        if on:
            turn = _surface_turn(avenue_point, mouth_point, (0, travel), (highway_direction, 0))
            world_turn = [world_coordinates(u, v) for u, v in turn]
            points = [port] + world_turn + ramp["points"][1:]
            movement = f"{arm}->{ramp['deck']}-highway"
        else:
            turn = _surface_turn(mouth_point, avenue_point, (highway_direction, 0), (0, travel))
            world_turn = [world_coordinates(u, v) for u, v in turn]
            points = ramp["points"][:-1] + world_turn + [port]
            movement = f"{ramp['deck']}-highway->{arm}"
        result.append({"id": movement, "ramp_id": ramp["id"], "points": points,
                       "transport": CAR, "lane": 1, "junction": True,
                       "surface_points": world_turn, "avenue_port": port,
                       "native_high_port": ramp["native_high_port"]})
    return result


MODULES = {
    "access-core": ("DD RHW-4 and Avenue Access Core", ((0, -1), (-1, 0), (0, 0), (1, 0), (0, 1))),
    "northwest-junction": ("Avenue Northwest Ramp Junction", ((-2, -2), (-1, -2), (0, -2), (-2, -1), (-1, -1), (-2, 0))),
    "southeast-junction": ("Avenue Southeast Ramp Junction", ((1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3))),
    "lower-exit-branch": ("DD RHW-4 Lower Diagonal Exit Branch", ((2, -3), (3, -3), (2, -2))),
    "lower-entry-branch": ("DD RHW-4 Lower Diagonal Entry Branch", ((-3, 2), (-2, 2), (-3, 3))),
    "lower-exit-grade": ("Compact Lower Diagonal Exit Grade", ((1, -3), (1, -2))),
    "lower-entry-grade": ("Compact Lower Diagonal Entry Grade", ((-3, 1), (-2, 1))),
    "upper-exit-branch": ("DD RHW-4 Upper Diagonal Exit Branch", ((-2, 3), (-4, 4), (-3, 4), (-2, 4), (-4, 5), (-3, 5))),
    "upper-entry-branch": ("DD RHW-4 Upper Diagonal Entry Branch", ((4, -4), (5, -4), (4, -3), (5, -3), (3, -2), (4, -2))),
    "upper-exit-grade": ("Compact Upper Diagonal Exit Grade", ((0, 2), (-1, 3), (0, 3), (-1, 4))),
    "upper-entry-grade": ("Compact Upper Diagonal Entry Grade", ((4, -1), (3, -1), (2, 0), (3, 0))),
    "diagonal-half-a": ("DD RHW-4 Diagonal Continuation A", ((-1, 1),)),
    "diagonal-half-b": ("DD RHW-4 Diagonal Continuation B", ((-1, 2),)),
}
EXTRA_PLACEMENTS = (("diagonal-half-a", (1, -1)), ("diagonal-half-b", (2, -1)))
MODEL_ONLY_CELLS = frozenset(((1, 3), (3, 1), (1, -3), (-3, 1), (-3, 5), (5, -3)))
WORLD_GRID_ORIGIN = (-4, -4)


def module_catalog():
    """Return thirteen reusable types and fifteen non-overlapping placements.

    ``world_origin_cell`` is the component's minimum column/row in the native
    construction grid. ``cells`` are normalized local sparse construction
    cells. Assembly placements use a common positive ten-by-ten grid,
    whose cell (0,0) corresponds to world (-4,-4). All highway/avenue services
    sharing a city tile belong to its single declared component.
    """
    types, placements, owners = [], [], {}
    for key, (name, cells) in MODULES.items():
        origin = min(c[0] for c in cells), min(c[1] for c in cells)
        normalized = [(c[0] - origin[0], c[1] - origin[1]) for c in cells]
        normalized.sort(key=lambda c: (c[1], c[0]))
        model_only = [(c[0] - origin[0], c[1] - origin[1]) for c in cells if c in MODEL_ONLY_CELLS]
        types.append({"key": key, "name": name, "recipe": "highway_ddrhw_compact_" + key.replace("-", "_"), "geometry_key": key,
                      "cells": [list(c) for c in normalized],
                      "footprint": [max(c[0] for c in normalized) + 1, max(c[1] for c in normalized) + 1],
                      "world_origin_cell": list(origin), "world_cells": [list(c) for c in cells],
                      "authors_surface_atlas": False,
                      "engineering": {"max_grade_percent": 30.0, "pavement_path_offset_m": 0.0,
                                      "car_corridor_half_width_m": 1.25, "car_corridor_height_m": 3.8,
                                      "model_only_cells": [list(c) for c in model_only]}})
        placements.append({"key": key, "geometry_key": key,
                           "origin": [origin[axis] - WORLD_GRID_ORIGIN[axis] for axis in (0, 1)], "rotation": 0})
        for cell in cells:
            _require(cell not in owners, f"Module ownership overlaps at {cell}")
            owners[cell] = key
    for index, (key, origin) in enumerate(EXTRA_PLACEMENTS, 1):
        _require(origin not in owners, "Native continuation overlaps an authored module")
        owners[origin] = f"{key}-{index}"
        repeat = f"{key}-repeat" if index <= 2 else f"{key}-repeat-{index}"
        placements.append({"key": repeat, "geometry_key": key,
                           "origin": [origin[axis] - WORLD_GRID_ORIGIN[axis] for axis in (0, 1)], "rotation": 0})
    _require(len(owners) == 53, "The gentler assembly's exact cell partition changed")
    footprint = [max(cell[axis] for cell in owners) - WORLD_GRID_ORIGIN[axis] + 1 for axis in (0, 1)]
    return {"types": types, "placements": placements, "world_grid_origin": list(WORLD_GRID_ORIGIN),
            "footprint": footprint, "occupied_cells": [list(c) for c in sorted(owners, key=lambda c: (c[1], c[0]))],
            "cell_owners": [{"cell": list(c), "key": owners[c]} for c in sorted(owners, key=lambda c: (c[1], c[0]))]}


def component_routes(piece):
    """Return source-derived local car polylines for icons without game files."""
    from .ramp_geometry import world_coordinates
    key = piece.get("geometry_key") or piece["recipe"].removeprefix("highway_ddrhw_compact_").replace("_", "-")
    _require(key in MODULES, f"Unknown compact highway module {key}")
    cells = set(MODULES[key][1])
    origin = min(c[0] for c in cells), min(c[1] for c in cells)
    paths = []
    for route in compact_access_routes():
        for cell, points in polyline_fragments(route["points"]):
            if cell in cells:
                paths.append([(p[0] + 16 * (cell[0] - origin[0]), p[1] - 16 * (cell[1] - origin[1]), p[2]) for p in points])
    sources = []
    lane = 3.2 / math.sqrt(2.0)
    for lateral in (-lane, lane):
        sources.append([world_coordinates(-200.0, lateral, 15.0), world_coordinates(200.0, lateral, 15.0)])
        sources.append([world_coordinates(200.0, lateral, 7.5), world_coordinates(-200.0, lateral, 7.5)])
    for lateral in (4.8 / math.sqrt(2.0), 11.2 / math.sqrt(2.0)):
        sources.append([world_coordinates(lateral, -200.0), world_coordinates(lateral, 200.0)])
        sources.append([world_coordinates(-lateral, 200.0), world_coordinates(-lateral, -200.0)])
    for line in sources:
        for cell, points in polyline_fragments(line):
            if cell in cells:
                paths.append([(p[0] + 16 * (cell[0] - origin[0]), p[1] - 16 * (cell[1] - origin[1]), p[2]) for p in points])
    return paths


@lru_cache(maxsize=1)
def _procedural_geometry():
    from .ramp_geometry import (compact_ramps, compact_ramp_triangles, road_triangles,
                                union_ground_pavement, partition_triangles)
    ramps = compact_ramps()
    routes = compact_access_routes(ramps)
    from .slip_lanes import surfaces, WHITE
    faces = [triangle for ramp in ramps for triangle in compact_ramp_triangles(ramp)]
    faces.extend(face for face in surfaces(ramps) if abs(face[0][3]-WHITE) < 1e-8)
    for route in routes:
        faces.extend(road_triangles(route["surface_points"], width=3.5, thickness=0.1,
                                    barriers=False, edge_markings=False))
    faces = union_ground_pavement(faces)
    tiles = partition_triangles(faces)
    owners = {tuple(record["cell"]) for record in module_catalog()["cell_owners"]}
    _require(set(tiles) <= owners, f"Actual road envelope exceeds declared component ownership: {set(tiles) - owners}")
    paths = deduplicate_routes(slice_routes(routes))
    model_only = {cell for cell in owners if cell not in paths and sum(cell) not in (0, 1)
                  and cell[0] - cell[1] not in (-1, 0, 1)}
    _require(model_only == MODEL_ONLY_CELLS,
             "The actual road and native channels differ from the declared model-only tile contract")
    continuation_cells = {tuple(cell) for key, (_name, cells) in MODULES.items()
                          if key.startswith("diagonal-half-") for cell in cells}
    continuation_cells.update(cell for _key, cell in EXTRA_PLACEMENTS)
    _require(not continuation_cells & (set(paths) | set(tiles)),
             "A reused native continuation cell contains unique ramp traffic or authored road faces")
    return ramps, tiles, paths


def _native_cell(context, cell):
    """Select complete audited native channels for one global city tile."""
    from .native import channels
    models, highway, avenue = [], [], []
    total, difference = sum(cell), cell[0] - cell[1]
    if total in (0, 1):
        donor, turns = (0x5753A380, 0) if total == 0 else (0x5753A300, 2)
        model, highway = channels(context["dd_rhw"], donor, False, turns)
        models.append((model, model["meshes"], (0.0, 0.0, 0.0)))
    if difference in (-1, 0, 1):
        donor, turns = (0x5753A305, 0) if difference == 0 else (0x5753A300, 0 if difference == 1 else 2)
        model, avenue = channels(context["dd_rhw"], donor, True, turns)
        models.append((model, model["meshes"], (0.0, 0.0, 0.0)))
    return models, highway, avenue


def _route_metadata(route, role):
    output = deepcopy(route)
    output["junction"] = bool(output.get("junction", output.get("compatibility", 0)))
    output["id"] = output.get("id", role)
    points = output["points"]
    output["tangent_in"] = tuple(points[1][a] - points[0][a] for a in (0, 1))
    output["tangent_out"] = tuple(points[-1][a] - points[-2][a] for a in (0, 1))
    return output


def compile_module(spec, context):
    """Compile one exact reusable module, retaining all shared native services.

    Return [(normalized_cell, saved_S3D_bytes, saved_PATH_bytes)] in the
    allocated source cell order. The coordinated global layout is sliced
    before this selection, so no component silently overwrites another.
    """
    from scp.models import parse_s3d, pack_s3d
    from scp.recipes import combine_meshes
    from .native import material_template, channels
    from .ramp_geometry import pack_road_model, cut_native_branch_openings, support_triangles, ATLAS_UV
    from .ramp_materials import NativeRoadPainter
    key = spec.get("geometry_key") or spec["recipe"].removeprefix("highway_ddrhw_compact_").replace("_", "-")
    records = {record["key"]: record for record in module_catalog()["types"]}
    _require(key in records, f"Unknown compact highway module {key}")
    declaration = records[key]
    _require(spec["cells"] == declaration["cells"] and spec["footprint"] == declaration["footprint"],
             "Allocated module cells differ from the proved physical tile partition")
    origin = declaration["world_origin_cell"]
    texture = int(spec["tile_ids"][0], 16)
    ramps, procedural_tiles, additional_paths = _procedural_geometry()
    base, _routes = channels(context["dd_rhw"], 0x5753A380, False, 0)
    material = material_template(context)
    surface_roads = [{"points": movement["surface_points"]}
                     for movement in compact_access_routes(ramps)]
    painter = NativeRoadPainter(context, list(ramps)+surface_roads)
    compiled = []
    for local in map(tuple, spec["cells"]):
        cell = local[0] + origin[0], local[1] + origin[1]
        native_models, highway_routes, avenue_routes = _native_cell(context, cell)
        parts = []
        if native_models:
            native_raw = pack_s3d(combine_meshes(native_models))
            ground = [tuple((p[0] + 16.0 * cell[0], p[1], p[2] + 16.0 * cell[1], *p[3:]) for p in tri)
                      for tri in procedural_tiles.get(cell, ())
                      if all(abs(p[1]) < 1e-8 and abs(p[3] - ATLAS_UV["asphalt"][0]) < 1e-8 for p in tri)]
            opened, _report = cut_native_branch_openings(native_raw, cell, ramps, ground_pavement=ground)
            native = parse_s3d(opened)
            parts.append((native, native["meshes"], (0.0, 0.0, 0.0)))
        faces = list(procedural_tiles.get(cell, ()))
        if cell in {(-1,1), (-1,2), (1,-1), (2,-1), (-4,4), (4,-4)}:
            faces.extend(support_triangles())
        if faces:
            authored = parse_s3d(pack_road_model(faces, texture, material_template=material, model_template=base,
                                               native_painter=painter, cell=cell))
            parts.append((authored, authored["meshes"], (0.0, 0.0, 0.0)))
        _require(parts, f"Declared module cell {cell} has no actual visible model")
        model = pack_s3d(combine_meshes(parts))
        routes = [_route_metadata(route, "native-highway") for route in highway_routes]
        routes += [_route_metadata(route, "native-avenue") for route in avenue_routes]
        routes += deepcopy(additional_paths.get(cell, []))
        routes = mark_junctions(deduplicate_routes({cell: routes}))[cell]
        expected_empty = list(local) in declaration["engineering"]["model_only_cells"]
        _require(bool(routes) != expected_empty, f"The declared model-only PATH contract differs in {local}")
        compiled.append((local, model, encode_paths(routes, allow_empty=expected_empty)))
    return compiled


def construction_fields(spec, compiled):
    """Derive construction ownership and road flags from actual saved routes."""
    from .native import parse_paths
    key = spec["geometry_key"]
    record = next(item for item in module_catalog()["types"] if item["key"] == key)
    origin = record["world_origin_cell"]
    width, depth = spec["footprint"]
    rows = [["."] * (width + 2) for _ in range(depth + 1)]
    cons = deepcopy(rows)
    rows[0][-1] = cons[0][-1] = "<"
    rows[-1][0] = cons[-1][0] = "^"
    palette = []
    for index, (local, _model, raw) in enumerate(compiled):
        symbol = chr(ord("a") + index)
        rows[local[1]][local[0]] = symbol
        world = local[0] + origin[0], local[1] + origin[1]
        native_avenue = world[0] - world[1] in (-1, 0, 1)
        native_highway = sum(world) in (0, 1)
        routes = [_route_metadata(route, "saved") for route in parse_paths(raw)]
        # Native Avenue paths remain one measured diagonal corridor. The
        # custom road field owns the highway, ramps, and actual turning legs.
        road_routes = [route for route in routes if not (route["points"][0][2] == 0 and route["points"][-1][2] == 0)]
        road_routes += [route for route in routes if route["junction"] and route["transport"] == CAR]
        if not native_highway and not road_routes and not native_avenue:
            road_routes = routes
        fields = []
        if native_highway or road_routes or not native_avenue:
            fields.append(f"dirtroad: 0x{construction_flags(road_routes):08X}")
        if native_avenue:
            # These words are independently measured native A300/A305 flags.
            difference = world[0] - world[1]
            word = 0x01030103 if difference == 0 else 0x01000003 if difference == 1 else 0x00030100
            fields.append(f"avenue: 0x{word:08X}")
        palette.append(symbol + " - " + " ".join(fields))
        cons[local[1]][local[0]] = "+" if native_highway or road_routes or not native_avenue else "\\"
    return ["".join(row) for row in rows], palette, ["".join(row) for row in cons]


def build_piece(spec, context):
    from .recipes import finish_piece, construction
    compiled = compile_module(spec, context)
    assets = finish_piece(spec, context, compiled)
    declarations = spec.get("authored_texture_ids", [])
    record = next(item for item in module_catalog()["types"] if item["key"] == spec["geometry_key"])
    _require(not record["authors_surface_atlas"] and not declarations,
             "Native-textured highway modules must not reserve an unused authored atlas")
    rows, fields, cons = construction_fields(spec, compiled)
    return assets, construction(spec, rows, fields, cons)


def check_paths(resources, piece):
    """Delegate saved PATH inspection to the independent road verifier."""
    from .ramp_verify import check_paths as inspect
    return inspect(resources, piece)


def check_models(resources, piece, donors=None):
    """Delegate saved indexed-face and traffic-corridor inspection."""
    from .ramp_verify import check_models as inspect
    return inspect(resources, piece, donors)


def check_construction_fields(fields, piece, resources):
    """Delegate emitted construction inspection without regenerating models."""
    from .ramp_verify import check_construction_fields as inspect
    return inspect(fields, piece, resources)
