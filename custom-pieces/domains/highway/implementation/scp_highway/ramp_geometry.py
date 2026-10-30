"""Actual asphalt/deck/barrier meshes for compact highway slip ramps.

Road routes use PATH (east, north, height) coordinates. Encoded model vertices
use (east, height, -north). Every face is clipped into its actual city tile;
roadway shoulders, barriers, and explicitly requested support columns all
participate in construction ownership, not only the sampled traffic spine.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import math
import struct

from scp.models import pack_s3d, parse_s3d, validate_s3d

EPSILON = 1e-8
COLORS = ((53, 55, 58, 255), (147, 151, 153, 255),
          (235, 235, 218, 255), (231, 176, 44, 255))
# Sample solid interiors, so linear filtering cannot bleed neighboring colors.
ATLAS_UV = {name: (0.125 + 0.25 * index, 0.5)
            for index, name in enumerate(("asphalt", "concrete", "white", "yellow"))}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def create_surface_atlas(size=128):
    """Return an authored opaque BGRA FSH atlas, independent of NAM artwork."""
    _require(size in (32, 64, 128, 256), "Road atlas size must be 32, 64, 128, or 256 pixels")
    pixels = bytearray()
    for _row in range(size):
        for column in range(size):
            red, green, blue, alpha = COLORS[min(3, column * 4 // size)]
            pixels.extend((blue, green, red, alpha))
    block_size = 16 + len(pixels)
    return (struct.pack("<4sII4s4sI", b"SHPI", 24 + block_size, 1, b"GIMX", b"0000", 24)
            + struct.pack("<I6H", (block_size << 8) | 0x7D, size, size, 0, 0, 0, 0)
            + pixels)


def road_material(texture_id, template=None):
    """Create an opaque one-texture material or replace one audited atlas ID.

    A supplied template retains all native flags, depth settings, sampling
    modes, and texture naming bytes. Its original texture must occur exactly
    once in its encoded material; ambiguous byte replacements are rejected.
    """
    if template is not None:
        output = deepcopy(template)
        _require(len(output["textures"]) == 1, "Road material template must have exactly one texture")
        before = struct.pack("<I", output["textures"][0])
        _require(output["raw"].count(before) == 1, "Road material template texture reference is ambiguous")
        output["raw"] = output["raw"].replace(before, struct.pack("<I", texture_id))
        output["textures"] = [texture_id]
        return output
    raw = (struct.pack("<IBBBBHIBB", 0, 0, 1, 1, 0, 0, 0, 0, 1)
           + struct.pack("<IBBBBHHB", texture_id, 0, 0, 1, 1, 0, 0, 1) + b"\0")
    return {"raw": raw, "textures": [texture_id]}


def _normal(triangle):
    first, second, third = triangle
    u = tuple(second[a] - first[a] for a in range(3))
    v = tuple(third[a] - first[a] for a in range(3))
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def _triangulate(polygon, desired=None):
    result = []
    for index in range(1, len(polygon) - 1):
        triangle = polygon[0], polygon[index], polygon[index + 1]
        normal = _normal(triangle)
        if sum(value * value for value in normal) < 1e-16:
            continue
        if desired is not None and sum(a * b for a, b in zip(normal, desired)) < 0.0:
            triangle = triangle[0], triangle[2], triangle[1]
        result.append(triangle)
    return result


def _clip(polygon, distance):
    if not polygon:
        return []
    result = []
    previous = polygon[-1]
    last_distance = distance(previous)
    for current in polygon:
        current_distance = distance(current)
        if (current_distance >= -EPSILON) != (last_distance >= -EPSILON):
            fraction = last_distance / (last_distance - current_distance)
            result.append(tuple(a + fraction * (b - a) for a, b in zip(previous, current)))
        if current_distance >= -EPSILON:
            result.append(current)
        previous, last_distance = current, current_distance
    return result


def _vertex(point, lateral, normal, color, vertical=0.0):
    x, y, height = point
    return (x + lateral * normal[0], height + vertical,
            -(y + lateral * normal[1]), *ATLAS_UV[color])


def route_frames(points):
    """Return cumulative plan lengths and continuous constant-width miters."""
    _require(len(points) >= 2 and all(len(p) == 3 and all(math.isfinite(v) for v in p) for p in points),
             "A swept road needs at least two finite XYZ points")
    lengths, tangents = [0.0], []
    for first, last in zip(points, points[1:]):
        length = math.hypot(last[0] - first[0], last[1] - first[1])
        _require(length > EPSILON, "Road mesh contains a stationary planar segment")
        lengths.append(lengths[-1] + length)
        tangents.append(((last[0] - first[0]) / length, (last[1] - first[1]) / length))
    normals = []
    for index in range(len(points)):
        first = tangents[max(0, index - 1)]
        second = tangents[min(len(tangents) - 1, index)]
        normal_one, normal_two = (-first[1], first[0]), (-second[1], second[0])
        denominator = 1.0 + sum(a * b for a, b in zip(normal_one, normal_two))
        _require(denominator > 0.25, "A road kink is too sharp for a safe miter")
        normal = tuple((a + b) / denominator for a, b in zip(normal_one, normal_two))
        _require(math.hypot(*normal) <= 2.0, "A road miter exceeds twice its authored half-width")
        normals.append(normal)
    return lengths, normals


def _ribbon(points, normals, low, high, color, vertical=0.0):
    # A twisting graded quad is not planar. Its centre line is an explicit
    # triangulation seam, so the saved traffic spine always sits exactly on
    # the saved pavement, including interpolated tile-side intersections.
    if low < -EPSILON and high > EPSILON:
        return (_ribbon(points, normals, low, 0.0, color, vertical)
                + _ribbon(points, normals, 0.0, high, color, vertical))
    result = []
    for index, (first, last) in enumerate(zip(points, points[1:])):
        polygon = [_vertex(point, offset, normal, color, vertical)
                   for point, normal, offset in ((first, normals[index], low), (first, normals[index], high),
                                                 (last, normals[index + 1], high), (last, normals[index + 1], low))]
        result.extend(_triangulate(polygon, (0.0, 1.0, 0.0)))
    return result


def _box(center, half_width, bottom, top):
    x, y = center
    vertices = [(x + a * half_width, height, -(y + b * half_width), *ATLAS_UV["concrete"])
                for height in (bottom, top) for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    output = []
    for indices, normal in (((0, 1, 2, 3), (0, -1, 0)), ((4, 5, 6, 7), (0, 1, 0)),
                            ((0, 1, 5, 4), (0, 0, 1)), ((1, 2, 6, 5), (1, 0, 0)),
                            ((2, 3, 7, 6), (0, 0, -1)), ((3, 0, 4, 7), (-1, 0, 0))):
        output.extend(_triangulate([vertices[index] for index in indices], normal))
    return output


def road_triangles(points, *, width=6.0, thickness=0.6, barrier_width=0.25,
                   barrier_height=0.9, barriers=True, edge_markings=True,
                   divider=False, supports=(), barrier_ranges=None, barrier_profile=None):
    """Sweep a physical one-way road, including its actual service envelope.

    ``points`` follow the pavement surface at the traffic PATH elevation.
    Barrier faces taper with the pavement height close to ground level.
    ``barrier_ranges`` maps -1/1 sides to allowed distance ranges: a branch
    owner must omit the barrier across a real traffic split/merge opening.
    ``supports`` contains explicit (east, north, underside_height) tuples;
    the caller owns their clearance from all neighboring traffic corridors.
    """
    _require(width > 2.0 and thickness > 0.0 and 0.0 < barrier_width < width / 4.0,
             "Road width, thickness, and barrier profile must be positive and usable")
    _require(all(point[2] >= -EPSILON for point in points), "A highway ramp cannot descend below ground")
    lengths, normals = route_frames(points)
    half = width / 2.0
    output = _ribbon(points, normals, -half, half, "asphalt")
    for index, (first, last) in enumerate(zip(points, points[1:])):
        ends = [(first, normals[index]), (last, normals[index + 1])]
        underside = [(*point[:2], max(0.0, point[2] - thickness)) for point, _ in ends]
        polygon = [_vertex(point, offset, normal, "concrete")
                   for point, normal, offset in ((underside[0], ends[0][1], -half), (underside[0], ends[0][1], half),
                                                 (underside[1], ends[1][1], half), (underside[1], ends[1][1], -half))]
        if max(first[2], last[2]) > EPSILON:
            output.extend(_triangulate(polygon, (0.0, -1.0, 0.0)))
        for side in (-1, 1):
            face = [_vertex(point, side * half, normal, "concrete")
                    for point, normal in ((first, normals[index]), (last, normals[index + 1]),
                                          (underside[1], normals[index + 1]), (underside[0], normals[index]))]
            outward = side * normals[index][0], 0.0, -side * normals[index][1]
            output.extend(_triangulate(face, outward))
            intervals = None if barrier_ranges is None else barrier_ranges.get(side, ())
            midpoint = (lengths[index] + lengths[index + 1]) / 2.0
            # A fully grounded profile collapses into nonzero-area concrete
            # strips on the asphalt. End the barrier at the final graded
            # segment instead of retaining those coplanar landing faces.
            enabled = (barriers and max(first[2], last[2]) > EPSILON
                       and (intervals is None or any(low <= midpoint <= high for low, high in intervals)))
            if enabled and barrier_profile is not None:
                _require(len(barrier_profile) >= 2 and all(0.0 <= inset < half and height >= 0.0
                                                           for inset, height in barrier_profile),
                         "Barrier profile must remain inside its actual road half-width")
                for (inset_one, height_one), (inset_two, height_two) in zip(barrier_profile, barrier_profile[1:]):
                    polygon = []
                    for point, normal, inset, height in ((first, normals[index], inset_one, height_one),
                                                         (first, normals[index], inset_two, height_two),
                                                         (last, normals[index + 1], inset_two, height_two),
                                                         (last, normals[index + 1], inset_one, height_one)):
                        taper = min(1.0, max(0.0, point[2]) / 1.5)
                        polygon.append(_vertex(point, side * (half - inset), normal, "concrete", height * taper))
                    output.extend(_triangulate(polygon))
                continue
            if enabled:
                low, high = sorted((side * (half - barrier_width), side * half))
                wall_heights = [barrier_height * min(1.0, max(0.0, point[2]) / 1.5) for point, _ in ends]
                bottom = [_vertex(point, offset, normal, "concrete")
                          for point, normal, offset in ((first, normals[index], low), (first, normals[index], high),
                                                        (last, normals[index + 1], high), (last, normals[index + 1], low))]
                top = [(vertex[0], vertex[1] + wall_heights[0 if n < 2 else 1], *vertex[2:])
                       for n, vertex in enumerate(bottom)]
                output.extend(_triangulate(top, (0.0, 1.0, 0.0)))
                for a, b in ((0, 3), (1, 2)):
                    output.extend(_triangulate((bottom[a], bottom[b], top[b], top[a])))
    if edge_markings:
        for side in (-1, 1):
            center = side * (half - barrier_width - 0.4)
            output.extend(_ribbon(points, normals, center - 0.06, center + 0.06, "white", vertical=0.012))
    if divider:
        # An authored two-lane deck has an actual white lane separator.
        # It is dashed in exact 3 m painted/5 m gap intervals along the spine.
        for index, (first, last) in enumerate(zip(points, points[1:])):
            low, high = lengths[index], lengths[index + 1]
            for dash in range(math.floor(low / 8.0), math.floor(high / 8.0) + 1):
                start, end = max(low, dash * 8.0), min(high, dash * 8.0 + 3.0)
                if end <= start:
                    continue
                fractions = [(distance - low) / (high - low) for distance in (start, end)]
                pair = [tuple(a + fraction * (b - a) for a, b in zip(first, last)) for fraction in fractions]
                pair_normals = [tuple(a + fraction * (b - a) for a, b in zip(normals[index], normals[index + 1]))
                                for fraction in fractions]
                output.extend(_ribbon(pair, pair_normals, -0.06, 0.06, "white", vertical=0.012))
    for east, north, top in supports:
        _require(top > 0.0, "A support must reach an elevated actual underside")
        output.extend(_box((east, north), 0.4, 0.0, top))
    return output


def partition_triangles(triangles):
    """Clip real model faces to tile bounds, including their width and UVs."""
    output = defaultdict(list)
    for triangle in triangles:
        xs, zs = [p[0] for p in triangle], [p[2] for p in triangle]
        low_x, high_x = math.floor((min(xs) + 8.0) / 16.0), math.floor((max(xs) + 8.0 - EPSILON) / 16.0)
        low_z, high_z = math.floor((min(zs) + 8.0) / 16.0), math.floor((max(zs) + 8.0 - EPSILON) / 16.0)
        if low_x > high_x:  # A vertical face exactly on a construction side has one owner.
            high_x = low_x
        if low_z > high_z:
            high_z = low_z
        for column in range(low_x, high_x + 1):
            for row in range(low_z, high_z + 1):
                polygon = list(triangle)
                for distance in (lambda p: p[0] - (16.0 * column - 8.0),
                                 lambda p: 16.0 * column + 8.0 - p[0],
                                 lambda p: p[2] - (16.0 * row - 8.0),
                                 lambda p: 16.0 * row + 8.0 - p[2]):
                    polygon = _clip(polygon, distance)
                local = [(p[0] - 16.0 * column, p[1], p[2] - 16.0 * row, *p[3:]) for p in polygon]
                output[column, row].extend(_triangulate(local))
    return {cell: faces for cell, faces in output.items() if faces}


def pack_road_model(triangles, texture_id, *, material_template=None, model_template=None,
                    native_painter=None, cell=(0, 0)):
    """Pack actual XYZ/UV triangles into conservative 512-vertex groups."""
    _require(triangles, "A road model needs actual triangles")
    material = road_material(texture_id, material_template)
    model = {"version": (1, 5), "vertices": [], "indices": [], "primitives": [],
             "materials": [material], "anim_header": struct.pack("<H", 1) + b"\0" * 12,
             "meshes": [], "trailing": [(b"PROP", b"PROP" + struct.pack("<II", 12, 0)),
                                         (b"REGP", b"REGP" + struct.pack("<II", 12, 0))]}
    if model_template is not None:
        _require(struct.unpack_from("<H", model_template["anim_header"])[0] == 1,
                 "A road model template must have one static frame")
        model["version"] = model_template["version"]
        model["anim_header"] = model_template["anim_header"]
        model["trailing"] = deepcopy(model_template["trailing"])
    groups = defaultdict(list)
    if native_painter is None:
        groups["legacy"] = list(triangles)
    else:
        for triangle in native_painter.texture_triangles(triangles):
            painted = native_painter.paint(triangle, cell)
            if painted is not None:
                role, face = painted
                groups[role].append(face)
        model["materials"] = [deepcopy(native_painter.materials[role]) for role in groups]

    for material_index, (role, faces) in enumerate(groups.items()):
        data, lookup, indices = bytearray(), {}, []

        def finish():
            group = len(model["meshes"])
            model["vertices"].append({"flags": 0, "format": 2, "stride": 20, "data": bytes(data)})
            model["indices"].append({"flags": 0, "stride": 2, "values": tuple(indices)})
            model["primitives"].append([(0, 0, len(indices))])
            name = b"SCP highway road\0" if role == "legacy" else ("SCP NAM "+role+"\0").encode("ascii")
            model["meshes"].append({"name": name, "flags": 0,
                                     "frames": [(group, group, group, material_index)]})

        for triangle in faces:
            encoded = [struct.pack("<5f", *p) for p in triangle]
            if indices and (len(lookup) + len(set(encoded).difference(lookup)) > 512 or len(indices) >= 1536):
                finish()
                data, lookup, indices = bytearray(), {}, []
            for vertex in encoded:
                if vertex not in lookup:
                    lookup[vertex] = len(lookup)
                    data.extend(vertex)
                indices.append(lookup[vertex])
        if indices:
            finish()
    validate_s3d(model)
    raw = pack_s3d(model)
    validate_s3d(parse_s3d(raw))
    return raw


def compile_road_tiles(roads, texture_id, *, material_template=None, model_template=None):
    """Compile all supplied road envelopes into exactly one S3D per city tile.

    Each road contains ``points`` and optional keyword parameters accepted by
    ``road_triangles``. Native branch/crossing ownership must be coordinated
    by the caller; overlapping authored pavement is rejected by the later
    saved-resource verifier, rather than being hidden by a picture.
    """
    faces = []
    for road in roads:
        arguments = {key: value for key, value in road.items() if key not in ("id", "points")}
        faces.extend(road_triangles(road["points"], **arguments))
    return {cell: pack_road_model(triangles, texture_id, material_template=material_template, model_template=model_template)
            for cell, triangles in partition_triangles(faces).items()}


def sample_grade_curve(controls, *, start_height, end_height=0.0, flat_start=0.0,
                       flat_end=4.0, taper=2.0, count=401, max_grade=0.4):
    """Sample a cubic road and continuous trapezoidal grade at fixed anchors.

    City-grid/native joining anchors belong in ``controls``. This function
    never moves them to preserve a desired length. Returned measurements use
    the resulting full horizontal route, including both level collars.
    """
    _require(len(controls) == 4 and count >= 17, "A grade curve needs four controls and at least 17 samples")
    points, lengths = [], [0.0]
    for index in range(count):
        t = index / (count - 1)
        weights = ((1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3)
        point = tuple(sum(w * p[axis] for w, p in zip(weights, controls)) for axis in (0, 1))
        if points:
            lengths.append(lengths[-1] + math.dist(points[-1], point))
        points.append(point)
    transition = lengths[-1] - flat_start - flat_end
    _require(flat_start >= 0.0 and flat_end >= 0.0 and taper > 0.0 and transition > 2.0 * taper,
             "Ramp has insufficient length for its flat collars and both grade tapers")
    grade = abs(end_height - start_height) / (transition - taper)
    _require(grade <= max_grade + 1e-10, f"Grid-snapped ramp needs {100 * grade:.3f}% grade; bound is {100 * max_grade:.3f}%")

    def progress(distance):
        if distance <= 0.0:
            return 0.0
        if distance >= transition:
            return 1.0
        if distance < taper:
            integral = distance * distance / (2.0 * taper)
        elif distance <= transition - taper:
            integral = distance - taper / 2.0
        else:
            remaining = transition - distance
            integral = transition - taper - remaining * remaining / (2.0 * taper)
        return integral / (transition - taper)

    sampled = [(*point, start_height + (end_height - start_height) * progress(distance - flat_start))
               for point, distance in zip(points, lengths)]
    return {"points": sampled, "length_plan_m": lengths[-1], "grade_max_percent": 100.0 * grade,
            "flat_start_m": flat_start, "flat_end_m": flat_end, "grade_taper_m": taper,
            "controls": [list(p) for p in controls]}


NATIVE_BARRIER_PROFILE = ((0.0, 0.0), (0.21875, 0.328125), (0.265625, 1.390625),
                          (0.5625, 1.390625), (0.625, 0.328125), (0.828125, 0.0))


def highway_coordinates(point):
    """Return native-axis u/v coordinates around measured centre (4,-4)."""
    x, y = point[:2]
    return (x + y) / math.sqrt(2.0), (y - x + 8.0) / math.sqrt(2.0)


def world_coordinates(u, v, height=0.0):
    return 4.0 + (u - v) / math.sqrt(2.0), -4.0 + (u + v) / math.sqrt(2.0), height


def compact_ramps(count=401):
    """Return four native-anchored compact curves, rather than schematic ends.

    The lower E-edge port is (56,51.2,7.5); the upper W-edge port is
    (-72,-83.2,15). Each is one diagonal construction step (16 m on both
    city axes, or 16*sqrt(2) m along the highway) beyond the original join.
    The other ports follow the deliberate same-side on-ramp
    transform. Ground junction centres are (-16,16) and (24,-24), with
    v=+/-20*sqrt(2); the latter is an authored internal grid-corner junction,
    rather than a native tile-centre anchor. Ground mouths remain internal
    nodes and must be concatenated with real surface-turn paths before PATH
    slicing. Full-width clearance uses the measured 16 m highway deck.
    """
    result = []
    lane = 3.2 / math.sqrt(2.0)
    junction = 20.0 * math.sqrt(2.0)
    for deck, side, start, height in (("lower", 1, (56.0, 51.2), 7.5),
                                      ("upper", -1, (-72.0, -83.2), 15.0)):
        first_u = sum(start) / math.sqrt(2.0)
        last_u = 12.0 if deck == "lower" else -12.0
        direction = -1.0 if deck == "lower" else 1.0
        handle = 0.38 * abs(first_u - last_u)
        controls_uv = ((first_u, side * lane), (first_u + direction * handle, side * lane),
                       (last_u - direction * handle, side * junction), (last_u, side * junction))
        controls = [world_coordinates(u, v)[:2] for u, v in controls_uv]
        controls[0] = start  # Preserve the exact measured boundary decimals.
        level = sample_grade_curve(controls, start_height=height, end_height=height, count=count)
        lengths, _normals = route_frames(level["points"])
        clearance = 8.0 + 3.0 + 2.0
        clear_index = next(index for index, point in enumerate(level["points"])
                           if abs(highway_coordinates(point)[1]) >= clearance)
        ramp = sample_grade_curve(controls, start_height=height, flat_start=lengths[clear_index],
                                  flat_end=4.0, taper=2.0, count=count, max_grade=0.3)
        # A sampled cubic has an exact analytic endpoint tangent, but its
        # first finite chord is slightly oblique. Give the saved PATH an
        # explicit 1 cm native-direction joining chord inside the already
        # level mainline collar; no extra approach distance is appended.
        collar = (start[0] + direction * 0.01 / math.sqrt(2.0),
                  start[1] + direction * 0.01 / math.sqrt(2.0), height)
        ramp["points"].insert(1, collar)
        ramp["length_plan_m"] = sum(math.dist(a[:2], b[:2]) for a, b in zip(ramp["points"], ramp["points"][1:]))
        ramp.update({"id": f"{deck}-off", "deck": deck, "direction": "off", "side": side,
                     "height_m": height, "width_m": 6.0, "clearance_abs_v_m": clearance,
                     "native_high_port": tuple((*start, height)), "junction_v_m": side * junction})
        result.append(ramp)
        on = deepcopy(ramp)
        on.update({"id": f"{deck}-on", "direction": "on"})
        on["points"] = [world_coordinates(-highway_coordinates(point)[0], highway_coordinates(point)[1], point[2])
                        for point in reversed(ramp["points"])]
        # Reflection/reversal keeps traffic on the same right side. It is
        # deliberately not a 180-degree rotation of an exit-ramp resource.
        on["native_high_port"] = on["points"][-1]
        on["controls"] = [list(world_coordinates(-highway_coordinates((*point, 0.0))[0],
                                                  highway_coordinates((*point, 0.0))[1])[:2])
                          for point in reversed(ramp["controls"])]
        result.append(on)
    return result


def outside_highway_corridor(triangles, side, half_width=8.0):
    """Keep new branch faces outside the retained native highway pavement.

    Input model faces are global. This removes coincident ramp asphalt and
    underside faces inside the existing deck; native barriers still require
    an actual opening cut where the branch crosses them.
    """
    _require(side in (-1, 1), "A highway branch must declare its right-side corridor")
    output = []
    for triangle in triangles:
        polygon = _clip(list(triangle), lambda p: side * ((-p[2] - p[0] + 8.0) / math.sqrt(2.0)) - half_width)
        output.extend(_triangulate(polygon))
    return output


def compact_ramp_triangles(ramp):
    """Return native-thickness physical ramp faces outside the mainline."""
    faces = road_triangles(ramp["points"], width=6.0, thickness=1.0, barrier_width=0.828125,
                           barrier_profile=NATIVE_BARRIER_PROFILE, barrier_height=1.390625)
    return outside_highway_corridor(faces, ramp["side"])


def support_triangles(centers=((0.0, 0.0),), *, half_width=0.4,
                      lower_height=7.5, upper_height=15.0):
    """Return real centre piers meeting both actual native deck planes.

    The donor's 1 m Substructure meshes are vertical outer skirts, rather
    than a horizontal underside at each cell centre. The concrete therefore
    reaches the saved pavement planes at 7.5 and 15 m. Four continuous side
    faces avoid coplanar horizontal patches on the actual native pavement;
    the ground and both native decks close its visible vertical span.
    """
    _require(0.0 < half_width < 1.0 and 0.0 < lower_height < upper_height,
             "A centre pier needs a narrow profile and increasing deck heights")
    result = []
    for center in centers:
        x, north = center
        vertices = [(x + a * half_width, height, -(north + b * half_width), *ATLAS_UV["concrete"])
                    for height in (0.0, upper_height) for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
        for indices, normal in (((0, 1, 5, 4), (0, 0, 1)), ((1, 2, 6, 5), (1, 0, 0)),
                                ((2, 3, 7, 6), (0, 0, -1)), ((3, 0, 4, 7), (-1, 0, 0))):
            result.extend(_triangulate([vertices[index] for index in indices], normal))
    return result


def _subtract_convex(polygon, footprint):
    """Subtract one actual road footprint while interpolating original UVs."""
    if not polygon:
        return []
    if (max(p[0] for p in polygon) < min(p[0] for p in footprint) - EPSILON
            or min(p[0] for p in polygon) > max(p[0] for p in footprint) + EPSILON
            or max(p[2] for p in polygon) < min(p[1] for p in footprint) - EPSILON
            or min(p[2] for p in polygon) > max(p[1] for p in footprint) + EPSILON):
        return [polygon]
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(footprint, footprint[1:] + footprint[:1]))
    boundary = footprint if area > 0.0 else list(reversed(footprint))
    pending, outside = polygon, []
    for a, b in zip(boundary, boundary[1:] + boundary[:1]):
        edge_length = math.dist(a, b)
        if edge_length <= 1e-10:
            continue
        def signed(point, a=a, b=b, edge_length=edge_length):
            # The tolerance is metres, not square metres. Tiny edges created
            # by an earlier union cut must not acquire centimetre-wide fuzzy
            # half-planes merely because their cross products are small.
            return ((b[0] - a[0]) * (point[2] - a[1]) - (b[1] - a[1]) * (point[0] - a[0])) / edge_length
        if any(signed(point) < -EPSILON for point in pending):
            part = _clip(pending, lambda point: -signed(point))
            if len(part) >= 3:
                outside.append(part)
        pending = _clip(pending, signed)
        if len(pending) < 3:
            break
    return outside


def _branch_footprints(ramp):
    points = ramp["points"]
    _lengths, normals = route_frames(points)
    half = ramp.get("width_m", 6.0) / 2.0
    output = []
    for index, (first, last) in enumerate(zip(points, points[1:])):
        # Only the level branch crossing opens its own deck's barrier. A
        # lower road passing below an upper deck never cuts that upper deck.
        if min(first[2], last[2]) < ramp["height_m"] - 1e-7:
            continue
        output.append([(point[0] + lateral * normal[0], -(point[1] + lateral * normal[1]))
                       for point, normal, lateral in ((first, normals[index], -half),
                                                      (first, normals[index], half),
                                                      (last, normals[index + 1], half),
                                                      (last, normals[index + 1], -half))])
    return output


def union_ground_pavement(triangles):
    """Create one watertight ground apron on an exact 1/16 m binary grid.

    Every grid square intersecting an authored ground road is retained, so
    the union never narrows its physical pavement. Maximum outward expansion
    is one square diagonal (0.088389 m). Equal runs are coalesced into exact
    rectangles; this is not a dense surface tessellation. Binary coordinates
    remain exact in float32 after every integer tile translation, avoiding
    microscopic T-junction cracks along the saved double-precision PATHs.
    Elevated pavement, deck walls, markings, and barriers remain unchanged.
    """
    accepted, rows = [], defaultdict(set)
    step = 1.0 / 16.0
    for triangle in triangles:
        is_ground = (all(abs(p[1]) < 1e-8 and abs(p[3] - ATLAS_UV["asphalt"][0]) < 1e-8 for p in triangle)
                     and abs(_normal(triangle)[1]) > 1e-10)
        if not is_ground:
            accepted.append(triangle)
            continue
        low = math.floor(min(p[2] for p in triangle) / step)
        high = math.ceil(max(p[2] for p in triangle) / step - 1e-9)
        for row in range(low, high):
            polygon = _clip(list(triangle), lambda p, row=row: p[2] - row * step)
            polygon = _clip(polygon, lambda p, row=row: (row + 1) * step - p[2])
            if len(polygon) < 3:
                continue
            area = abs(sum(a[0] * b[2] - b[0] * a[2] for a, b in zip(polygon, polygon[1:] + polygon[:1])))
            if area < 1e-13:
                continue
            first = math.floor(min(p[0] for p in polygon) / step)
            last = math.ceil(max(p[0] for p in polygon) / step - 1e-9)
            rows[row].update(range(first, last))
    active, rectangles = {}, []
    previous_row = None
    for row in sorted(rows):
        intervals, first, previous = [], None, None
        for column in sorted(rows[row]):
            if previous is not None and column != previous + 1:
                intervals.append((first, previous + 1))
                first = None
            if first is None:
                first = column
            previous = column
        if first is not None:
            intervals.append((first, previous + 1))
        if previous_row is not None and row != previous_row + 1:
            rectangles.extend((a, b, start, previous_row + 1) for (a, b), start in active.items())
            active = {}
        retained = {}
        for interval in intervals:
            retained[interval] = active.pop(interval, row)
        rectangles.extend((a, b, start, row) for (a, b), start in active.items())
        active, previous_row = retained, row
    if previous_row is not None:
        rectangles.extend((a, b, start, previous_row + 1) for (a, b), start in active.items())
    for left, right, bottom, top in rectangles:
        # Split rectangles at city sides before triangulating. Clipping a
        # large rectangle's diagonal afterwards would invent non-binary
        # intersection coordinates and undo the exact float32 grid benefit.
        xs = [left] + [128 + 256 * n for n in range(math.floor((left - 128) / 256) + 1,
                                                    math.ceil((right - 128) / 256))] + [right]
        zs = [bottom] + [128 + 256 * n for n in range(math.floor((bottom - 128) / 256) + 1,
                                                      math.ceil((top - 128) / 256))] + [top]
        for x0, x1 in zip(xs, xs[1:]):
            for z0, z1 in zip(zs, zs[1:]):
                polygon = [(x * step, 0.0, z * step, *ATLAS_UV["asphalt"])
                           for x, z in ((x0, z0), (x1, z0), (x1, z1), (x0, z1))]
                accepted.extend(_triangulate(polygon, (0.0, 1.0, 0.0)))
    return accepted


def cut_native_branch_openings(raw, cell, ramps, *, ground_pavement=()):
    """Cut real native barrier/outer-wall openings and retain every material.

    ``raw`` is the native tile S3D in local model coordinates. ``cell`` and
    ramp points use the same world construction grid. Native roadway tops,
    the opposing barrier, the other deck, supports, UVs, and texture IDs are
    retained. Only faces inside the actual branch service footprint and at
    the target deck's right-side barrier/outer wall are subtracted.
    """
    source = parse_s3d(raw)
    _require(struct.unpack_from("<H", source["anim_header"])[0] == 1,
             "Native branch opening requires a static native S3D")
    candidates = [(ramp, _branch_footprints(ramp)) for ramp in ramps]
    ground_cuts = [[(p[0], p[2]) for p in triangle] for triangle in ground_pavement
                   if all(abs(p[1]) < 1e-8 for p in triangle) and abs(_normal(triangle)[1]) > 1e-10]
    output = {key: deepcopy(value) for key, value in source.items()
              if key not in ("vertices", "indices", "primitives", "materials", "meshes")}
    output.update({"vertices": [], "indices": [], "primitives": [], "materials": [], "meshes": []})
    material_indices = {}
    examined, removed = 0, 0
    changed = False
    for mesh in source["meshes"]:
        _require(len(mesh["frames"]) == 1, "Native branch opening cannot discard animated geometry")
        vi, ii, pi, mi = mesh["frames"][0]
        vb = source["vertices"][vi]
        _require(vb["stride"] == 20, "Native branch opening needs original XYZ/UV vertices")
        points = [struct.unpack_from("<5f", vb["data"], offset) for offset in range(0, len(vb["data"]), 20)]
        original, kept = [], []
        index_buffer = source["indices"][ii]["values"]
        for kind, first, count in source["primitives"][pi]:
            _require(kind == 0 and count % 3 == 0, "Native branch opening needs triangle-list primitives")
            original.extend(tuple(points[index] for index in index_buffer[n:n + 3]) for n in range(first, first + count, 3))
        for triangle in original:
            world = [(p[0] + 16.0 * cell[0], p[1], p[2] + 16.0 * cell[1], *p[3:]) for p in triangle]
            pieces = [world]
            if mesh["name"].rstrip(b"\0") == b"Avenue" and all(abs(p[1]) < 1e-6 for p in world):
                for footprint in ground_cuts:
                    pieces = [part for polygon in pieces for part in _subtract_convex(polygon, footprint)]
                    if not pieces:
                        break
            for ramp, footprints in candidates:
                height, side = ramp["height_m"], ramp["side"]
                lateral = [side * (-p[2] - p[0] + 8.0) / math.sqrt(2.0) for p in world]
                heights = [p[1] for p in world]
                barrier = (min(heights) >= height - 1e-5
                           and height + 1e-5 < max(heights) <= height + 1.390625 + 1e-5)
                outer_wall = (min(heights) >= height - 1.0001 and max(heights) <= height + 1e-5
                              and max(heights) - min(heights) > 0.01
                              and max(abs(v - 8.0) for v in lateral) < 0.001)
                if min(lateral) < 6.8 or max(lateral) > 8.001 or not (barrier or outer_wall):
                    continue
                examined += 1
                for footprint in footprints:
                    remaining = []
                    for polygon in pieces:
                        remaining.extend(_subtract_convex(polygon, footprint))
                    pieces = remaining
                    if not pieces:
                        break
            fragments = [triangle for polygon in pieces for triangle in _triangulate(polygon)]
            before_bytes = b"".join(struct.pack("<5f", *p) for p in world)
            after_bytes = b"".join(struct.pack("<5f", *p) for part in fragments for p in part)
            if before_bytes != after_bytes:
                changed = True
                removed += 1
            kept.extend(tuple((p[0] - 16.0 * cell[0], p[1], p[2] - 16.0 * cell[1], *p[3:]) for p in part)
                        for part in fragments)
        if not kept:
            continue
        if mi not in material_indices:
            material_indices[mi] = len(output["materials"])
            output["materials"].append(deepcopy(source["materials"][mi]))
        material = material_indices[mi]
        data, lookup, indices = bytearray(), {}, []

        def finish():
            group = len(output["meshes"])
            vertices, indices_out = deepcopy(vb), deepcopy(source["indices"][ii])
            vertices["data"], indices_out["values"] = bytes(data), tuple(indices)
            output["vertices"].append(vertices)
            output["indices"].append(indices_out)
            output["primitives"].append([(0, 0, len(indices))])
            output["meshes"].append({"name": b"SCP opened " + mesh["name"], "flags": mesh["flags"],
                                     "frames": [(group, group, group, material)]})

        for triangle in kept:
            encoded = [struct.pack("<5f", *point) for point in triangle]
            if indices and (len(lookup) + len(set(encoded).difference(lookup)) > 512 or len(indices) >= 1536):
                finish()
                data, lookup, indices = bytearray(), {}, []
            for point in encoded:
                if point not in lookup:
                    lookup[point] = len(lookup)
                    data.extend(point)
                indices.append(lookup[point])
        if indices:
            finish()
    if not changed:
        return raw, {"changed": False, "candidate_faces": examined, "opened_faces": 0}
    validate_s3d(output)
    result = pack_s3d(output)
    validate_s3d(parse_s3d(result))
    return result, {"changed": True, "candidate_faces": examined, "opened_faces": removed}
