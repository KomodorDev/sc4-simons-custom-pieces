"""Native-profile lofts for the six-tile orthogonal DD RHW transition.

The writer references native end materials, sweeps their complete barrier
cross-sections, closes the authored deck bodies, and supplies closed support
solids. A generated private-build atlas blends native asphalt appearances;
no NAM image bytes are maintained in the source tree.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from functools import lru_cache
import hashlib
import math
import struct

from scp.models import pack_s3d, parse_s3d, validate_s3d
from scp.recipes import combine_meshes
from scp.render_meshes import assert_render_budget
from scp.track_paths import S3D
from . import orthogonal_transition_geometry as geometry
from .orthogonal_transition_variants import LOWER_BEND_RIGHT
from . import ramp_geometry, ramp_paths

DD_DONOR = 0x57530000
GROUND_DONOR = 0x57030000
DD_MODEL_SHA256 = "3d94bcce2ff84c9bd06d3bbbc7a089b8eaa28cfe921c3d31e87a27300cffd3dd"
GROUND_MODEL_SHA256 = "81bf6080e261e2a902d8836ce480e970af8428d9f4a9b36d2290b3a8522f21dc"
TEXTURE = (0x7AB50E44, 0x1ABE787D)
TEXTURE_SHA256 = {
    0x5703000E: "c2b9ac53cc080ca8146f1345e13d43e91c883d9559ec3ec3293e7ff88a259e88",
    0x5713000E: "25a91179a26a82ba6307777b1957c5862bee61daf55c7638c4487d64b275c7b8",
}
DD_MIN = -7.999000072479248
DD_MAX = 8.00100040435791
DD_WIDTH = DD_MAX - DD_MIN
DD_OFFSET = DD_MIN + 8.0
DATUM = {"upper": 0.0010004043579101562, "lower": 0.0009999275207519531}
ATLAS_SIZE = (512, 1024)
ATLAS_COLUMN = {"upper": 8, "lower": 264}
ATLAS_ROW = 128
UPPER_SUPPORT_STATIONS = (12.0, 32.0, 52.0, 72.0)
LOWER_SUPPORT_STATIONS = (12.0, 32.0, 48.0)


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _fade(deck, station, *, variant="original"):
    return geometry.height(deck, station, variant=variant) / (15.0 if deck == "upper" else 7.5)


def appearance_blend(deck, station, *, variant="original"):
    """Blend asphalt colour continuously; expose native ground alpha only at landing."""
    return (1.0 - _fade(deck, station, variant=variant),
            1.0 - geometry.cubic(geometry.height(deck, station, variant=variant) / 0.25))


def pavement_datum(deck, station, *, variant="original"):
    return DATUM[deck] * _fade(deck, station, variant=variant)


def _width_fade(deck, station, *, variant, west):
    if variant == LOWER_BEND_RIGHT and deck == "upper" and west:
        # This inner edge must stop overhanging the adjacent ground road
        # before the upper slab underside reaches ground.
        altitude = geometry.height(deck, station, variant=variant)
        return max(0.0, (altitude - 1.1) / (15.0 - 1.1))
    return _fade(deck, station, variant=variant)


def pavement_bounds(deck, station, *, variant="original"):
    low, high = ((-DD_MAX, -DD_MIN) if geometry.native_cross_section_reflected(variant)
                 else (DD_MIN, DD_MAX))
    return (-8.0 + _width_fade(deck, station, variant=variant, west=True) * (low + 8.0),
            8.0 + _width_fade(deck, station, variant=variant, west=False) * (high - 8.0))


def _native_station(station, variant):
    """Native pose 2 reverses longitudinal sampling within the city tile."""
    return 16.0 - station if geometry.traffic_reversed(variant) else station


def _source_uv(deck, station, lateral, *, native_dd, variant="original"):
    station = _native_station(station, variant)
    if geometry.native_cross_section_reflected(variant):
        lateral = -lateral
    if native_dd:
        u, v = (lateral - DD_MIN) / DD_WIDTH, (station - DD_OFFSET) / DD_WIDTH
    else:
        u, v = (lateral + 8.0) / 16.0, station / 16.0
    return (u, v) if deck == "upper" else (1.0 - u, 1.0 - v)


def _pavement_uv(deck, station, lateral, role, *, variant="original"):
    geometry.is_mirrored(variant)
    if role in ("native-dd", "native-ground"):
        return _source_uv(deck, station, lateral, native_dd=role == "native-dd", variant=variant)
    low, high = pavement_bounds(deck, station, variant=variant)
    u = (lateral - low) / (high - low)
    # Atlas pixels retain their native source lateral order. Reflect the
    # field exactly once when the canonical cross-section is reflected.
    if geometry.native_cross_section_reflected(variant):
        u = 1.0 - u
    if deck == "lower":
        u = 1.0 - u
    return ((ATLAS_COLUMN[deck] + 128.0 * u) / ATLAS_SIZE[0],
            (ATLAS_ROW + 8.0 * station) / ATLAS_SIZE[1])


def _role(deck, first, last):
    if last <= geometry.COLLAR:
        return "native-dd"
    ground_start = geometry.ACTIVE_END if deck == "lower" else geometry.LENGTH - geometry.COLLAR
    return "native-ground" if first >= ground_start else "atlas"


def _native_models(context):
    dd_raw = context["dd_rhw"][*S3D, DD_DONOR]
    ground_raw = context["rhw4"][*S3D, GROUND_DONOR]
    _require(hashlib.sha256(dd_raw).hexdigest() == DD_MODEL_SHA256, "Orthogonal DD donor changed")
    _require(hashlib.sha256(ground_raw).hexdigest() == GROUND_MODEL_SHA256, "Ground RHW-4 donor changed")
    return parse_s3d(dd_raw), parse_s3d(ground_raw)


class _Painter:
    def __init__(self, dd, ground, texture_id, *, variant="original"):
        self.materials = {}
        for deck in ("upper", "lower"):
            for role, material in (("native-dd", dd["materials"][0]),
                                   ("native-ground", ground["materials"][0]),
                                   ("atlas", ramp_geometry.road_material(texture_id, ground["materials"][0]))):
                self.materials[f"{deck}-pavement-{role}"] = deepcopy(material)
            self.materials[f"{deck}-body"] = deepcopy(dd["materials"][1])
            self.materials[f"{deck}-barrier"] = deepcopy(dd["materials"][2])
        for record in support_specifications(variant=variant):
            self.materials[record["id"]] = deepcopy(dd["materials"][1])
        self.roles = tuple(self.materials)

    def texture_triangles(self, triangles):
        return triangles

    def paint(self, triangle, cell):
        codes = {round(p[5]) for p in triangle}
        _require(len(codes) == 1, "A clipped face crossed a material boundary")
        return self.roles[codes.pop()], tuple(tuple(p[:5]) for p in triangle)


def _point(deck, station, lateral, vertical, uv, code, *, variant="original"):
    return (*geometry.model_point(deck, station, lateral, vertical, variant=variant), *uv, float(code))


def _quad(points, normal=None):
    return ramp_geometry._triangulate(points, normal, minimum_normal_squared=1e-22)


def _paired_body_strip(rings, offsets, first, last, normal, concrete):
    """Use the roof's own split for the floor, with exact ground-clamp cuts."""
    sides = []
    body_rings = [[(*point[:3], lateral / 8.0, station / 8.0, float(concrete))
                   for point, lateral in zip(ring, ring_offsets)]
                  for station, ring, ring_offsets in zip((first, last), rings, offsets)]
    before, after = body_rings

    def bottom(point):
        return (point[0], max(0.0, point[1] - 1.0), *point[2:])

    for index in range(len(before) - 1):
        corners = [before[index], after[index], after[index + 1], before[index + 1]]
        for triangle in _quad(corners):
            heights = [p[1] for p in triangle]
            if max(heights) <= 0.0:
                continue
            polygons = ([triangle] if min(heights) >= 1.0 or max(heights) <= 1.0 else
                        [_clip_plane(triangle, 1, 1.0, direction) for direction in (1.0, -1.0)])
            for polygon in polygons:
                sides += _quad([bottom(point) for point in polygon], (0.0, -1.0, 0.0))
    for side, index in ((-1, 0), (1, -1)):
        a, b = before[index], after[index]
        edges = [(a, b)]
        if min(a[1], b[1]) < 1.0 < max(a[1], b[1]):
            fraction = (1.0 - a[1]) / (b[1] - a[1])
            crossing = tuple(x + fraction * (y - x) for x, y in zip(a, b))
            crossing = (crossing[0], 1.0, *crossing[2:])
            edges = [(a, crossing), (crossing, b)]
        for start, end in edges:
            corners = (start, bottom(start), bottom(end), end)
            points = [(*p[:3], p[2] / 16.0, (p[1] - min(a[1], b[1])) / 8.0,
                       float(concrete)) for p in corners]
            sides += _quad(points, (side * normal[0], 0.0, side * normal[1]))
    return sides


def _pavement_and_body(deck, painter, *, variant="original"):
    faces = []
    paired_floor = variant == LOWER_BEND_RIGHT
    # The four retained models are authored in the canonical plan before any
    # whole-world reflection. The new lower curve is its own canonical plan.
    source_variant = variant if paired_floor else "original"
    for first, last in zip(geometry.STATIONS, geometry.STATIONS[1:]):
        role = _role(deck, first, last)
        code = painter.roles.index(f"{deck}-pavement-{role}")
        rings, offsets_by_ring = [], []
        for station in (first, last):
            low, high = pavement_bounds(deck, station, variant=variant)
            offsets = (low, -3.75, -2.5, -1.25, 0.0, 1.25, 2.5, 3.75, high)
            offsets_by_ring.append(offsets)
            rings.append([_point(deck, station, u, pavement_datum(deck, station, variant=variant),
                                  _pavement_uv(deck, station, u, role, variant=variant), code,
                                  variant=source_variant) for u in offsets])
        for index in range(len(rings[0]) - 1):
            faces += _quad([rings[0][index], rings[1][index], rings[1][index + 1],
                            rings[0][index + 1]], (0.0, 1.0, 0.0))
        concrete = painter.roles.index(f"{deck}-body")
        if paired_floor:
            normal = geometry.frame(deck, (first + last) / 2.0, variant=source_variant)[1]
            faces += _paired_body_strip(rings, offsets_by_ring, first, last, normal, concrete)
            continue
        bottom = []
        for station in (first, last):
            low, high = pavement_bounds(deck, station, variant=variant)
            altitude = geometry.height(deck, station)
            surface = altitude + pavement_datum(deck, station)
            thickness = min(1.0, surface)
            bottom.append([_point(deck, station, u, pavement_datum(deck, station) - thickness,
                                   (u / 8.0, station / 8.0), concrete) for u in (low, high)])
        if max(geometry.height(deck, first), geometry.height(deck, last)) > 0.0:
            faces += _quad([bottom[0][0], bottom[0][1], bottom[1][1], bottom[1][0]], (0., -1., 0.))
            for side, top_index, bottom_index in ((-1, 0, 0), (1, -1, 1)):
                top_first, top_last = rings[0][top_index], rings[1][top_index]
                points = []
                for p in (top_first, bottom[0][bottom_index], bottom[1][bottom_index], top_last):
                    points.append((*p[:3], p[2] / 16.0, (p[1] - min(top_first[1], top_last[1])) / 8.0,
                                   float(concrete)))
                normal = geometry.frame(deck, (first + last) / 2.0)[1]
                faces += _quad(points, (side * normal[0], 0., side * normal[1]))
    # Close the complete authored slab, without placing artificial walls at internal tile cuts.
    concrete = painter.roles.index(f"{deck}-body")
    for station, outward in ((0.0, (0., 0., -1.)), (geometry.LENGTH, (0., 0., 1.))):
        datum = pavement_datum(deck, station, variant=variant)
        surface = geometry.height(deck, station, variant=variant) + datum
        if surface <= 0.0:
            continue
        low, high = pavement_bounds(deck, station, variant=variant)
        points = [_point(deck, station, u, vertical,
                         (u / 8.0, vertical / 8.0), concrete, variant=source_variant)
                  for u, vertical in ((low, datum), (low, datum - min(1.0, surface)),
                                      (high, datum - min(1.0, surface)), (high, datum))]
        faces += _quad(points, outward)
    return faces


def _barrier_sections(dd, deck):
    """Read each native longitudinal strip and both of its measured UV ends."""
    mesh = dd["meshes"][2 if deck == "upper" else 5]
    vi, ii, _pi, _mi = mesh["frames"][0]
    vb = dd["vertices"][vi]
    vertices = [struct.unpack_from("<5f", vb["data"], offset)
                for offset in range(0, len(vb["data"]), vb["stride"])]
    front, back = min(p[2] for p in vertices), max(p[2] for p in vertices)
    indices = dd["indices"][ii]["values"]
    strips = []
    for index in range(0, len(indices), 3):
        triangle = [vertices[i] for i in indices[index:index + 3]]
        starts = [p for p in triangle if p[2] == front]
        if len(starts) != 2:
            continue
        ends = []
        for point in starts:
            matches = [p for p in vertices if p[2] == back and p[:2] == point[:2] and p[4] == point[4]]
            _require(len(matches) == 1, "Native barrier UV cross-section is ambiguous")
            ends.append(matches[0])
        strips.append((starts, ends))
    _require(len(strips) == 10, "Native DD barrier must contain five strips on each side")
    return strips


def _barriers(dd, deck, painter, *, variant="original"):
    code = painter.roles.index(f"{deck}-barrier")
    baseline = 15.0 if deck == "upper" else 7.5
    faces = []
    source_variant = variant if variant == LOWER_BEND_RIGHT else "original"
    for starts, ends in _barrier_sections(dd, deck):
        side = 1.0 if starts[0][0] > 0.0 else -1.0
        for first, last in zip(geometry.STATIONS, geometry.STATIONS[1:]):
            if (geometry.height(deck, first, variant=variant)
                    == geometry.height(deck, last, variant=variant) == 0.0):
                continue
            points = []
            for station, source in ((first, 0), (first, 1), (last, 1), (last, 0)):
                a, b = starts[source], ends[source]
                fraction = (_native_station(station, variant) - DD_OFFSET) / DD_WIDTH
                uv = (a[3] + fraction * (b[3] - a[3]), a[4])
                # The source's sub-millimetre origin offset fades with the deck datum.
                canonical = (a[0] - (DD_MIN + DD_MAX) / 2.0) * 16.0 / DD_WIDTH
                reflected = geometry.native_cross_section_reflected(variant)
                west = (a[0] > 0.0) if reflected else (a[0] < 0.0)
                lateral = canonical + _width_fade(deck, station, variant=variant, west=west) * (a[0] - canonical)
                if reflected:
                    lateral = -lateral
                rise = (a[1] - baseline - DATUM[deck])
                taper = geometry.cubic(geometry.height(deck, station, variant=variant) / 2.0)
                vertical = pavement_datum(deck, station, variant=variant) + rise * taper
                points.append(_point(deck, station, lateral, vertical, uv, code, variant=source_variant))
            if geometry.native_cross_section_reflected(variant):
                points = [points[0], points[3], points[2], points[1]]
            normal = ramp_geometry._normal(points[:3])
            # Native index winding already supplies the correct side, inner face, or crown.
            faces += _quad(points, normal)
    return faces


@lru_cache(maxsize=None)
def support_specifications(*, variant="original"):
    """Explicit complete solids; dimensions are authored choices, not load ratings."""
    records = []
    lower_bend = variant == LOWER_BEND_RIGHT
    embed = 0.15 if lower_bend else 0.0

    def support_top(deck, station):
        return (geometry.height(deck, station, variant=variant)
                + pavement_datum(deck, station, variant=variant) - 1.0 + embed)

    for station in UPPER_SUPPORT_STATIONS:
        top = support_top("upper", station)
        pier = -9.2 if station == 12.0 else (6.4 if lower_bend else -6.4)
        records += [{"id": f"upper-pier-{int(station)}", "deck": "upper", "station_m": station,
                     "lateral_range_m": [pier - 0.4, pier + 0.4], "station_half_length_m": 0.4,
                     "bottom_m": 0.0, "top_m": top - 0.3},
                    {"id": f"upper-cap-{int(station)}", "deck": "upper", "station_m": station,
                     "lateral_range_m": [min(-7.0, pier - 0.4), 7.0], "station_half_length_m": 0.45,
                     "bottom_m": top - 0.3, "top_m": top}]
    for station in LOWER_SUPPORT_STATIONS:
        top = support_top("lower", station)
        for side in (-1, 1):
            centre = side * 6.4
            records.append({"id": f"lower-pier-{int(station)}-{'west' if side < 0 else 'east'}",
                            "deck": "lower", "station_m": station,
                            "lateral_range_m": [centre - 0.4, centre + 0.4],
                            "station_half_length_m": 0.4, "bottom_m": 0.0, "top_m": top})
    _require(all(r["top_m"] > r["bottom_m"] for r in records), "A support solid collapsed")
    return tuple(records)


def _support_box(record, painter, *, variant="original"):
    deck, station = record["deck"], record["station_m"]
    (east, south), normal = geometry.frame(deck, station, variant=variant)
    tangent = -normal[1], normal[0]
    half = record["station_half_length_m"]
    code = painter.roles.index(record["id"])
    vertices = []
    for height in (record["bottom_m"], record["top_m"]):
        for u, t in ((record["lateral_range_m"][0], -half),
                     (record["lateral_range_m"][1], -half),
                     (record["lateral_range_m"][1], half),
                     (record["lateral_range_m"][0], half)):
            x, z = east + u * normal[0] + t * tangent[0], south + u * normal[1] + t * tangent[1]
            vertices.append((x, height, z, x / 8.0, (z + height) / 8.0, float(code)))
    centre = (east + sum(record["lateral_range_m"]) / 2.0 * normal[0],
              (record["top_m"] + record["bottom_m"]) / 2.0,
              south + sum(record["lateral_range_m"]) / 2.0 * normal[1])
    faces = []
    for indices in ((0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
                    (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)):
        polygon = [vertices[i] for i in indices]
        desired = tuple(sum(p[a] for p in polygon) / 4.0 - centre[a] for a in range(3))
        faces += _quad(polygon, desired)
    return faces


def _encode_paths(routes):
    raw = ramp_paths.encode_paths(routes, allow_empty=True)
    lines = raw.decode("ascii").splitlines()
    _require(lines[:5] == ["SC4PATHS", "1.2", str(len(routes)), "0", "0"], "Unexpected PATH encoder header")
    lines[4] = "1"
    return ("\r\n".join(lines) + "\r\n").encode("ascii")


def _pack_model(triangles, painter, template):
    """Reuse indexed packing without the diagonal-only seam transform."""
    groups = defaultdict(list)
    for triangle in triangles:
        roles = {round(p[5]) for p in triangle}
        _require(len(roles) == 1, "A clipped face changed material role")
        groups[painter.roles[roles.pop()]].append(tuple(tuple(p[:5]) for p in triangle))
    parts = []
    for role, faces in groups.items():
        material = painter.materials[role]
        raw = ramp_geometry.pack_road_model(faces, material["textures"][0],
                                            material_template=material, model_template=template)
        model = parse_s3d(raw)
        for mesh in model["meshes"]:
            mesh["name"] = ("SCP DD transition " + role + "\0").encode("ascii")
        parts.append((model, model["meshes"], (0., 0., 0.)))
    model = combine_meshes(parts)
    validate_s3d(model)
    assert_render_budget(model)
    return pack_s3d(model)


def _clip_plane(polygon, axis, boundary, direction):
    """Clip one exact half-space; intersections must stay on their segments."""
    if not polygon:
        return []
    result = []
    previous = polygon[-1]
    before = direction * (previous[axis] - boundary)
    for current in polygon:
        after = direction * (current[axis] - boundary)
        if (before >= 0.0) != (after >= 0.0):
            fraction = before / (before - after)
            _require(0.0 <= fraction <= 1.0, "Tile clipping attempted to extrapolate a face")
            intersection = [a + fraction * (b - a) for a, b in zip(previous, current)]
            intersection[axis] = boundary
            result.append(tuple(intersection))
        if after >= 0.0:
            result.append(current)
        previous, before = current, after
    return result


def partition_triangles(triangles):
    """Use strict orthogonal cuts, with a bounded one-nanometre input snap.

    A fuzzy inside decision combined with an exact zero-plane intersection
    can extrapolate when two negative distances straddle the fuzzy cutoff.
    The new transition uses exact signs after its input snap. The shared
    historic clipping implementation and all previous pieces stay untouched.
    """
    output = defaultdict(list)
    snap = 1e-9
    for triangle in triangles:
        canonical = []
        for point in triangle:
            vertex = list(point)
            for axis in (0, 2):
                nearest = round((vertex[axis] + 8.0) / 16.0) * 16.0 - 8.0
                if abs(vertex[axis] - nearest) <= snap:
                    vertex[axis] = nearest
            canonical.append(tuple(vertex))
        xs, zs = [p[0] for p in canonical], [p[2] for p in canonical]
        low_x, high_x = math.floor((min(xs) + 8.0) / 16.0), math.floor((max(xs) + 8.0 - snap) / 16.0)
        low_z, high_z = math.floor((min(zs) + 8.0) / 16.0), math.floor((max(zs) + 8.0 - snap) / 16.0)
        high_x, high_z = max(low_x, high_x), max(low_z, high_z)
        for column in range(low_x, high_x + 1):
            for row in range(low_z, high_z + 1):
                polygon = canonical
                for axis, boundary, direction in ((0, 16.0 * column - 8.0, 1.0),
                                                   (0, 16.0 * column + 8.0, -1.0),
                                                   (2, 16.0 * row - 8.0, 1.0),
                                                   (2, 16.0 * row + 8.0, -1.0)):
                    polygon = _clip_plane(polygon, axis, boundary, direction)
                local = [(p[0] - 16.0 * column, p[1], p[2] - 16.0 * row, *p[3:]) for p in polygon]
                output[column, row].extend(ramp_geometry._triangulate(local))
    return {cell: faces for cell, faces in output.items() if faces}


def reflect_triangles(triangles):
    """Reflect complete world geometry and reverse winding, retaining attributes."""
    return [tuple((16.0 - p[0], *p[1:]) for p in (triangle[0], triangle[2], triangle[1]))
            for triangle in triangles]


def build_channels(context, *, texture_id=None, variant="original"):
    """Compile the twelve owned cells using one allocated private-build atlas."""
    mirrored = geometry.is_mirrored(variant)
    texture_id = texture_id if texture_id is not None else context.get("orthogonal_transition_texture_id")
    _require(type(texture_id) is int and 0 < texture_id <= 0xFFFFFFFF,
             "Orthogonal transition requires its allocated authored texture ID")
    dd, ground = _native_models(context)
    source_variant = variant if variant == LOWER_BEND_RIGHT else "original"
    painter = _Painter(dd, ground, texture_id, variant=source_variant)
    faces = []
    for deck in ("upper", "lower"):
        faces += _pavement_and_body(deck, painter, variant=variant)
        faces += _barriers(dd, deck, painter, variant=variant)
    for support in support_specifications(variant=source_variant):
        faces += _support_box(support, painter, variant=source_variant)
    if mirrored:
        faces = reflect_triangles(faces)
    partition = partition_triangles(faces)
    # The native DD donor's measured +1 mm origin offset is physical overhang,
    # not an extra construction cell. Preserve it in its nearest owned host.
    owned = defaultdict(list)
    for cell, triangles in partition.items():
        host = min(1, max(0, cell[0])), min(5, max(0, cell[1]))
        _require(cell == host or (cell[0] == (-1 if geometry.traffic_reversed(variant) else 2)
                                 and 0 <= cell[1] < 6),
                 f"Unexpected transition model projection beyond the owned rectangle: {cell}")
        dx, dz = 16.0 * (cell[0] - host[0]), 16.0 * (cell[1] - host[1])
        owned[host].extend(tuple((p[0] + dx, p[1], p[2] + dz, *p[3:]) for p in tri)
                           for tri in triangles)
    routes = ramp_paths.slice_routes(geometry.traffic_routes(variant=variant))
    _require(set(geometry.CELLS) - set(routes) == set(geometry.model_only_cells(variant=variant)),
             "Transition model-only declaration differs from actual complete lane cuts")
    result = []
    for cell in geometry.CELLS:
        fragments = deepcopy(routes.get(cell, []))
        if cell[1] == 5:
            for route in fragments:
                route["lane"] += 1
        _require(owned[cell], f"Transition cell {cell} has no actual model")
        model = _pack_model(owned[cell], painter, dd)
        result.append((cell, model, _encode_paths(fragments)))
    return result


def _encode_fsh(image):
    width, height = image.size
    pixels = image.tobytes("raw", "BGRA")
    block_size = 16 + len(pixels)
    return (struct.pack("<4sII4s4sI", b"SHPI", 24 + block_size, 1, b"GIMX", b"0000", 24)
            + struct.pack("<I6H", (block_size << 8) | 0x7D, width, height, 0, 0, 0, 0) + pixels)


def build_textures(context, texture_id, *, variant="original"):
    """Blend measured native asphalt in a generated atlas with isolated gutters."""
    geometry.is_mirrored(variant)
    from PIL import Image
    from scp.preview import decode_fsh
    _require(type(texture_id) is int and texture_id > 0, "Authored atlas requires an allocated ID")
    images = {}
    for iid, expected in TEXTURE_SHA256.items():
        raw = context["rhw4_textures"][*TEXTURE, iid]
        _require(hashlib.sha256(raw).hexdigest() == expected, "Native asphalt texture input changed")
        image = decode_fsh(raw).convert("RGBA")
        _require(image.size == (128, 128), "Native asphalt resolution changed")
        images[iid] = image.load()
    atlas = Image.new("RGBA", ATLAS_SIZE, (0, 0, 0, 0))
    target = atlas.load()

    def sample(source, u, v):
        # Exact repeat-wrapped bilinear convention used by the native UV field.
        x, y = (u % 1.0) * 128.0 - 0.5, (v % 1.0) * 128.0 - 0.5
        ix, iy = math.floor(x), math.floor(y)
        fx, fy = x - ix, y - iy
        return tuple(sum(source[(ix + a) % 128, (iy + b) % 128][c]
                         * (fx if a else 1.0 - fx) * (fy if b else 1.0 - fy)
                         for a, b in ((0, 0), (1, 0), (0, 1), (1, 1))) for c in range(4))

    for deck in ("upper", "lower"):
        base = ATLAS_COLUMN[deck]
        for row in range(ATLAS_SIZE[1]):
            station = (row - ATLAS_ROW + 0.5) / 8.0
            native_station = _native_station(station, variant)
            phase = (native_station - DD_OFFSET) / DD_WIDTH
            ground_phase = native_station / 16.0
            if deck == "lower":
                phase, ground_phase = 1.0 - phase, 1.0 - ground_phase
            blend, alpha_blend = appearance_blend(deck, station, variant=variant)
            for column in range(-2, 130):
                u = ((column % 128) + 0.5) / 128.0
                first = sample(images[0x5713000E], u, phase)
                last = sample(images[0x5703000E], u, ground_phase)
                target[base + column, row] = tuple(
                    min(255, max(0, round(a + (alpha_blend if channel == 3 else blend) * (b - a))))
                    for channel, (a, b) in enumerate(zip(first, last)))
    return {(*TEXTURE, texture_id): _encode_fsh(atlas)}


def engineering_metadata(*, variant="original"):
    result = geometry.engineering_metadata(variant=variant)
    result.update({"native_dd_model_sha256": DD_MODEL_SHA256,
                   "native_ground_model_sha256": GROUND_MODEL_SHA256,
                   "native_texture_sha256": {f"{iid:08X}": value for iid, value in TEXTURE_SHA256.items()},
                   "atlas_size_pixels": list(ATLAS_SIZE),
                   "atlas_native_pixels_per_16m": 128,
                   "atlas_colour_blend": "One minus remaining deck-height fraction",
                   "atlas_alpha_blend": "One minus cubic smoothstep of deck height divided by 0.25 m",
                   "native_pavement_datum_offsets_m": DATUM,
                   "datum_transition": "Native DD offset times remaining deck-height fraction; exact zero at ground",
                   "measured_native_outer_overhang_m": DD_MAX - 8.0,
                   "tile_clipping_policy": "At most 1e-9 m input grid snap; exact half-space classification and bounded segment intersections",
                   "support_solids": deepcopy(list(support_specifications(variant=variant))),
                   "support_geometry_scope": "Closed oriented rectangular piers and caps; structural capacity unverified",
                   "shadow_policy": "disabled", "pedestrian_routes": 0})
    if variant == "mirrored":
        result.update({"native_dd_pose": 2, "native_ground_upper_pose": 2, "native_ground_lower_pose": 0,
                       "native_longitudinal_sample_station_m": "16 minus authored station s, before each deck's native UV orientation",
                       "native_uv_reflection_policy": "Retain lateral U under geometry reflection; reverse native longitudinal sample phase for asphalt and barriers",
                       "support_coordinate_policy": "Retain canonical source roles and lateral dimensions; reflect every complete solid by east x becoming 16 minus x",
                       "model_winding_policy": "Reverse each reflected triangle's winding to preserve its outward face"})
    if geometry.is_opposite_side(variant) or variant == LOWER_BEND_RIGHT:
        reversed_traffic = geometry.traffic_reversed(variant)
        result.update({"native_dd_pose": 2 if reversed_traffic else 0,
                       "native_ground_upper_pose": 2 if reversed_traffic else 0,
                       "native_ground_lower_pose": 0 if reversed_traffic else 2,
                       "canonical_native_cross_section_reflected": True,
                       "native_longitudinal_sample_station_m": "16 minus authored station s" if reversed_traffic else "Authored station s",
                       "native_uv_reflection_policy": "Reflect exact source lateral XYZ and its affine UV field before the physical shape reflection; phase longitudinal samples by traffic direction",
                       "atlas_uv_policy": "Source-normal atlas pixels with one canonical lateral UV reflection",
                       "native_overhang_side": "west" if reversed_traffic else "east",
                       "model_winding_policy": "Reverse canonical reflected barrier winding and each whole-world reflected triangle separately",
                       "support_coordinate_policy": "Reflect complete canonical solids through east x becoming 16 minus x" if geometry.is_mirrored(variant) else "Retain canonical complete support solids"})
    if variant == LOWER_BEND_RIGHT:
        result.update({"underside_policy": "Paired roof triangulation, clipped at exact 1 m roof height; underside is clamped to ground",
                       "upper_inner_overhang_fade_end_path_height_m": 1.1,
                       "support_attachment_m": 0.15,
                       "support_coordinate_policy": "Upper supports use the straight deck frame; lower supports follow the curved lower deck frame"})
    return result
