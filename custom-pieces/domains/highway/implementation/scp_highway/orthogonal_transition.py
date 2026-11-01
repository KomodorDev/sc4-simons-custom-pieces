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


def _fade(deck, station):
    return geometry.height(deck, station) / (15.0 if deck == "upper" else 7.5)


def appearance_blend(deck, station):
    """Blend asphalt colour continuously; expose native ground alpha only at landing."""
    return 1.0 - _fade(deck, station), 1.0 - geometry.cubic(geometry.height(deck, station) / 0.25)


def pavement_datum(deck, station):
    return DATUM[deck] * _fade(deck, station)


def pavement_bounds(deck, station):
    factor = _fade(deck, station)
    return (-8.0 + factor * (DD_MIN + 8.0),
            8.0 + factor * (DD_MAX - 8.0))


def _source_uv(deck, station, lateral, *, native_dd):
    if native_dd:
        u, v = (lateral - DD_MIN) / DD_WIDTH, (station - DD_OFFSET) / DD_WIDTH
    else:
        u, v = (lateral + 8.0) / 16.0, station / 16.0
    return (u, v) if deck == "upper" else (1.0 - u, 1.0 - v)


def _pavement_uv(deck, station, lateral, role):
    if role in ("native-dd", "native-ground"):
        return _source_uv(deck, station, lateral, native_dd=role == "native-dd")
    low, high = pavement_bounds(deck, station)
    u = (lateral - low) / (high - low)
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
    def __init__(self, dd, ground, texture_id):
        self.materials = {}
        for deck in ("upper", "lower"):
            for role, material in (("native-dd", dd["materials"][0]),
                                   ("native-ground", ground["materials"][0]),
                                   ("atlas", ramp_geometry.road_material(texture_id, ground["materials"][0]))):
                self.materials[f"{deck}-pavement-{role}"] = deepcopy(material)
            self.materials[f"{deck}-body"] = deepcopy(dd["materials"][1])
            self.materials[f"{deck}-barrier"] = deepcopy(dd["materials"][2])
        for record in support_specifications():
            self.materials[record["id"]] = deepcopy(dd["materials"][1])
        self.roles = tuple(self.materials)

    def texture_triangles(self, triangles):
        return triangles

    def paint(self, triangle, cell):
        codes = {round(p[5]) for p in triangle}
        _require(len(codes) == 1, "A clipped face crossed a material boundary")
        return self.roles[codes.pop()], tuple(tuple(p[:5]) for p in triangle)


def _point(deck, station, lateral, vertical, uv, code):
    return (*geometry.model_point(deck, station, lateral, vertical), *uv, float(code))


def _quad(points, normal=None):
    return ramp_geometry._triangulate(points, normal, minimum_normal_squared=1e-22)


def _pavement_and_body(deck, painter):
    faces = []
    for first, last in zip(geometry.STATIONS, geometry.STATIONS[1:]):
        role = _role(deck, first, last)
        code = painter.roles.index(f"{deck}-pavement-{role}")
        rings = []
        for station in (first, last):
            low, high = pavement_bounds(deck, station)
            offsets = (low, -3.75, -2.5, -1.25, 0.0, 1.25, 2.5, 3.75, high)
            rings.append([_point(deck, station, u, pavement_datum(deck, station),
                                  _pavement_uv(deck, station, u, role), code) for u in offsets])
        for index in range(len(rings[0]) - 1):
            faces += _quad([rings[0][index], rings[1][index], rings[1][index + 1],
                            rings[0][index + 1]], (0.0, 1.0, 0.0))
        concrete = painter.roles.index(f"{deck}-body")
        bottom = []
        for station in (first, last):
            low, high = pavement_bounds(deck, station)
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
        surface = geometry.height(deck, station) + pavement_datum(deck, station)
        if surface <= 0.0:
            continue
        low, high = pavement_bounds(deck, station)
        points = [_point(deck, station, u, vertical,
                         (u / 8.0, vertical / 8.0), concrete)
                  for u, vertical in ((low, pavement_datum(deck, station)),
                                      (low, pavement_datum(deck, station) - min(1.0, surface)),
                                      (high, pavement_datum(deck, station) - min(1.0, surface)),
                                      (high, pavement_datum(deck, station)))]
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


def _barriers(dd, deck, painter):
    code = painter.roles.index(f"{deck}-barrier")
    baseline = 15.0 if deck == "upper" else 7.5
    faces = []
    for starts, ends in _barrier_sections(dd, deck):
        side = 1.0 if starts[0][0] > 0.0 else -1.0
        for first, last in zip(geometry.STATIONS, geometry.STATIONS[1:]):
            if geometry.height(deck, first) == geometry.height(deck, last) == 0.0:
                continue
            points = []
            for station, source in ((first, 0), (first, 1), (last, 1), (last, 0)):
                a, b = starts[source], ends[source]
                fraction = (station - DD_OFFSET) / DD_WIDTH
                uv = (a[3] + fraction * (b[3] - a[3]), a[4])
                # The source's sub-millimetre origin offset fades with the deck datum.
                canonical = (a[0] - (DD_MIN + DD_MAX) / 2.0) * 16.0 / DD_WIDTH
                lateral = canonical + _fade(deck, station) * (a[0] - canonical)
                rise = (a[1] - baseline - DATUM[deck])
                taper = geometry.cubic(geometry.height(deck, station) / 2.0)
                vertical = pavement_datum(deck, station) + rise * taper
                points.append(_point(deck, station, lateral, vertical, uv, code))
            normal = ramp_geometry._normal(points[:3])
            # Native index winding already supplies the correct side, inner face, or crown.
            faces += _quad(points, normal)
    return faces


@lru_cache(maxsize=1)
def support_specifications():
    """Explicit complete solids; dimensions are authored choices, not load ratings."""
    records = []
    for station in UPPER_SUPPORT_STATIONS:
        top = geometry.height("upper", station) + pavement_datum("upper", station) - 1.0
        west = -9.2 if station == 12.0 else -6.4
        records += [{"id": f"upper-pier-{int(station)}", "deck": "upper", "station_m": station,
                     "lateral_range_m": [west - 0.4, west + 0.4], "station_half_length_m": 0.4,
                     "bottom_m": 0.0, "top_m": top - 0.3},
                    {"id": f"upper-cap-{int(station)}", "deck": "upper", "station_m": station,
                     "lateral_range_m": [min(-7.0, west - 0.4), 7.0], "station_half_length_m": 0.45,
                     "bottom_m": top - 0.3, "top_m": top}]
    for station in LOWER_SUPPORT_STATIONS:
        top = geometry.height("lower", station) + pavement_datum("lower", station) - 1.0
        for side in (-1, 1):
            centre = side * 6.4
            records.append({"id": f"lower-pier-{int(station)}-{'west' if side < 0 else 'east'}",
                            "deck": "lower", "station_m": station,
                            "lateral_range_m": [centre - 0.4, centre + 0.4],
                            "station_half_length_m": 0.4, "bottom_m": 0.0, "top_m": top})
    _require(all(r["top_m"] > r["bottom_m"] for r in records), "A support solid collapsed")
    return tuple(records)


def _support_box(record, painter):
    deck, station = record["deck"], record["station_m"]
    (east, south), normal = geometry.frame(deck, station)
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


def build_channels(context, *, texture_id=None):
    """Compile the twelve owned cells using one allocated private-build atlas."""
    texture_id = texture_id if texture_id is not None else context.get("orthogonal_transition_texture_id")
    _require(type(texture_id) is int and 0 < texture_id <= 0xFFFFFFFF,
             "Orthogonal transition requires its allocated authored texture ID")
    dd, ground = _native_models(context)
    painter = _Painter(dd, ground, texture_id)
    faces = []
    for deck in ("upper", "lower"):
        faces += _pavement_and_body(deck, painter)
        faces += _barriers(dd, deck, painter)
    for support in support_specifications():
        faces += _support_box(support, painter)
    partition = partition_triangles(faces)
    # The native DD donor's measured +1 mm origin offset is physical overhang,
    # not an extra construction cell. Preserve it in its nearest owned host.
    owned = defaultdict(list)
    for cell, triangles in partition.items():
        host = min(1, max(0, cell[0])), min(5, max(0, cell[1]))
        _require(cell == host or (cell[0] == 2 and 0 <= cell[1] < 6),
                 f"Unexpected transition model projection beyond the owned rectangle: {cell}")
        dx, dz = 16.0 * (cell[0] - host[0]), 16.0 * (cell[1] - host[1])
        owned[host].extend(tuple((p[0] + dx, p[1], p[2] + dz, *p[3:]) for p in tri)
                           for tri in triangles)
    routes = ramp_paths.slice_routes(geometry.traffic_routes())
    _require(set(geometry.CELLS) - set(routes) == set(geometry.MODEL_ONLY_CELLS),
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


def build_textures(context, texture_id):
    """Blend measured native asphalt in a generated atlas with isolated gutters."""
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
            phase = (station - DD_OFFSET) / DD_WIDTH
            ground_phase = station / 16.0
            if deck == "lower":
                phase, ground_phase = 1.0 - phase, 1.0 - ground_phase
            blend, alpha_blend = appearance_blend(deck, station)
            for column in range(-2, 130):
                u = ((column % 128) + 0.5) / 128.0
                first = sample(images[0x5713000E], u, phase)
                last = sample(images[0x5703000E], u, ground_phase)
                target[base + column, row] = tuple(
                    min(255, max(0, round(a + (alpha_blend if channel == 3 else blend) * (b - a))))
                    for channel, (a, b) in enumerate(zip(first, last)))
    return {(*TEXTURE, texture_id): _encode_fsh(atlas)}


def engineering_metadata():
    result = geometry.engineering_metadata()
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
                   "support_solids": deepcopy(list(support_specifications())),
                   "support_geometry_scope": "Closed oriented rectangular piers and caps; structural capacity unverified",
                   "shadow_policy": "disabled", "pedestrian_routes": 0})
    return result
