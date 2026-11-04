"""Physical counterpart with reversed traffic and driver-left road markings.

Construction retains the original ascending canonical curve order, independently
of the new directed PATH order. Native interfaces use the opposite real NAM
phase. No original socket dictionary, cache, curve, or installed asset is changed.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
from types import MappingProxyType

import numpy as np
import shapely
from shapely.geometry import LineString, Point, Polygon, box
from shapely.geometry.polygon import orient

from scp.track_paths import S3D
from . import ramp_paths
from . import y_junction_geometry as shared
from . import y_junction_reversed_native_models as native_models
from . import y_junction_reversed_source as source

SUBJECT = source.SUBJECT
SOCKETS = MappingProxyType({arm: MappingProxyType({
    **dict(record), "donor": native_models.SOCKETS[arm]["helper"][0],
    "pose": native_models.SOCKETS[arm]["helper"][1],
}) for arm, record in shared.SOCKETS.items()})
_WORLD_CACHE = {}


def _partition_coherent_triangles(triangles):
    """Retain every nonzero surface fragment through exact city-cell cuts.

    The historical partitioner drops faces below a fixed normal-area cutoff.
    Coherent raised tops can contain smaller finite closing triangles, so the
    reversed compiler uses the same exact clipper and1nm tile-boundary snap
    without that area cutoff. Native coordinates and all attributes otherwise
    follow the existing city transform.
    """
    output = {}
    snap = 1e-9
    for triangle in triangles:
        canonical = []
        for point in triangle:
            vertex = list(point)
            for axis in (0, 2):
                boundary = round((vertex[axis] + 8.) / 16.) * 16. - 8.
                if abs(vertex[axis] - boundary) <= snap:
                    vertex[axis] = boundary
            canonical.append(tuple(vertex))
        limits = []
        for axis in (0, 2):
            values = [point[axis] for point in canonical]
            low = math.floor((min(values) + 8.) / 16.)
            high = max(low, math.floor((max(values) + 8. - snap) / 16.))
            limits.append(range(low, high + 1))
        for column in limits[0]:
            for row in limits[1]:
                polygon = canonical
                for axis, boundary, direction in ((0, 16. * column - 8., 1.),
                        (0, 16. * column + 8., -1.), (2, 16. * row - 8., 1.),
                        (2, 16. * row + 8., -1.)):
                    polygon = shared.orthogonal_transition._clip_plane(polygon, axis, boundary, direction)
                local = [(point[0] - 16. * column, point[1], point[2] - 16. * row, *point[3:])
                         for point in polygon]
                faces = shared.ramp_geometry._triangulate(local, minimum_normal_squared=0.)
                if faces:
                    output.setdefault((column, row), []).extend(faces)
    return output


def _supported_top_crop(desired, retained):
    """Bound every omitted point by the existing1nm construction resolution.

    The retained top is already clipped to real body planes. This check
    never emits an unsupported face or extrapolates a height field. The
    inscribed round finite-edge buffer proves the Euclidean bound at corners
    too; positive omitted regions have no independent area allowance.
    """
    shared._require(not retained.is_empty and desired.covered_by(retained.buffer(1e-9, quad_segs=16)),
                    "Reversed graded top crop exceeds its finite1nm construction bound")
    return max(0., float(desired.difference(retained).area))


def _coherent_top_surface(region, height, code, uv):
    """Retain nonzero plane-intersection slivers instead of dropping corners."""
    result = []
    for part in shared._components(region):
        triangulation = shapely.constrained_delaunay_triangles(part)
        shared._require(abs(sum(face.area for face in triangulation.geoms) - part.area)
                        < max(1e-8, part.area * 1e-10), "Coherent top triangulation changed polygon area")
        for triangle in triangulation.geoms:
            points = [shared._vertex(e, n, height(np.array([e, n])), uv(np.array([e, n])), code)
                      for e, n in list(triangle.exterior.coords)[:3]]
            result += shared.ramp_geometry._triangulate(points, (0., 1., 0.), minimum_normal_squared=0.)
    return result


@dataclass(frozen=True)
class ReversedRibbonUV:
    original: object
    length_m: float

    def __call__(self, point):
        u, v = self.original(point)
        return 1. - u, self.length_m / 16. - v


def _surface_domains(asphalt, roads, deck, profiles, parent_mouths):
    domains = shared.flat_surface_domains(asphalt, roads, deck, profiles, parent_mouths)
    lengths = {road["id"]: float(road["station"][-1]) for road in roads}
    result = []
    for domain in domains:
        if domain["material_role"] == "pavement":
            owner = domain["owner"]
            domain = {**domain, "uv": ReversedRibbonUV(domain["uv"], lengths[owner]),
                      "frame": {**domain["frame"],
                                "canonical_physical_route": owner,
                                "directed_route": "-".join(reversed(owner.split("-"))),
                                "texture_orientation": "Reverse transverse and longitudinal route fields; keep yellow on driver-left"}}
        result.append(domain)
    return result


def _underside_faces(polygon, patches, roof, painter):
    """Keep a full metre below the nominal-height302 collar pavement.

    Native302's roof is one millimetre below the generic flat roof. Its bottom
    therefore also descends by that measured amount. Exact finite bottom-step
    walls close the internal boundary between the two constant-height patches.
    """
    lower = [patch for patch in patches if patch["height"] < roof - 1e-7]
    pending = polygon
    regions = []
    for patch in lower:
        # The authored flat union already uses a1nm input grid. Normalize
        # this auxiliary body-floor owner mask to that same grid; a raw
        # native decimal can otherwise leave a<0.1nm higher-bottom sliver
        # whose1mm step survives encoding while its plan strip collapses.
        # Actual native roofs, UVs, and source profile vertices do not move.
        mask = shapely.set_precision(patch["geometry"], grid_size=1e-9)
        region = pending.intersection(mask)
        if region.is_empty:
            continue
        regions.append((region, patch["height"] - shared.DEPTH))
        pending = pending.difference(region)
    faces = []
    for region, bottom in [*regions, (pending, roof - shared.DEPTH)]:
        triangles = shared._triangulate_surface(region, bottom, painter.role("body"),
                                                lambda p: (p[0] / 8., p[1] / 8.))
        faces.extend((triangle[0], triangle[2], triangle[1]) for triangle in triangles)
    for region, bottom in regions:
        for part in shared._components(region):
            part = orient(part, sign=1.)
            for ring in (part.exterior, *part.interiors):
                for first, last in zip(ring.coords, list(ring.coords)[1:]):
                    line = LineString([first, last])
                    # Native mouth/outer caps close actual outside boundaries.
                    # Only a boundary with the unchanged higher bottom owns
                    # an internal underside step.
                    joined = line.intersection(pending.boundary)
                    parts = [joined] if joined.geom_type == "LineString" else list(getattr(joined, "geoms", ()))
                    for joint in parts:
                        if joint.geom_type != "LineString" or joint.length < 1e-8:
                            continue
                        a, b = joint.coords[0], joint.coords[-1]
                        # Retain the low region's outward edge orientation.
                        if line.project(Point(a)) > line.project(Point(b)):
                            a, b = b, a
                        points = [shared._vertex(*xy, h, (xy[0] / 8., h / 8.), painter.role("body"))
                                  for xy, h in ((a, bottom), (b, bottom),
                                                (b, roof - shared.DEPTH), (a, roof - shared.DEPTH))]
                        outward = (b[1] - a[1], 0., b[0] - a[0])
                        faces += shared._quad(points, outward)
    return faces


def _core_interface(context):
    """Reference-only native faces; these are never copied into our DAT.

    Outside300pose1 already supplies the actual roof over the final1mm of
    C's nominal PATH. Authored underside and body close through E56. The
    independent checker composes only this bounded existing native roof with
    those new solids; it must still demand every authored floor face.
    """
    records = []
    for group in native_models.native_coreward_faces(context, "C"):
        triangles = []
        for fragment in group["fragments"]:
            polygon = list(fragment["triangle"])
            for axis, boundary, direction in ((2, -8., 1), (2, 8., -1)):
                polygon = shared.orthogonal_transition._clip_plane(polygon, axis, boundary, direction)
                if not polygon:
                    break
            triangles.extend(shared._quad(polygon))
        if triangles:
            records.append({**{key: value for key, value in group.items() if key != "fragments"},
                            "triangles": triangles,
                            "usage": "Already-rendered native interface reference only; no custom DAT copy"})
    shared._require(records, "Reversed C is missing its literal native interface")
    return records


def _core_caps(native_faces, interface, context, painter, north_interval):
    reference = native_faces + [tuple((*p[:5], 0.) for p in triangle)
                               for group in interface for triangle in group["triangles"]]
    faces, minimum = shared._core_owned_caps(reference, context, painter,
        native_source=native_models, east_boundary=56., north_interval=north_interval,
        side_boundary=-8., side_sign=-1.)
    # The outside helper's narrow north-side body portion is not copied;
    # provide the new finite side from the authored floor to the pinned roof.
    start = native_models.native_join_plane(context, "C")
    normal, station, axis = (0., 0., -1.), north_interval[1], np.array([1., 0.])
    for deck in ("upper", "lower"):
        base = 15. if deck == "upper" else 7.5
        bottom = base + shared.pavement_datum(base) - shared.DEPTH
        segments = shared._section_top_segments(reference, normal, station, axis, base, 2e-6)
        cuts = shared._section_cuts([segments], start, 56.)
        for a, b in zip(cuts, cuts[1:]):
            if b - a < 1e-9 or shared._section_height(segments, (a + b) / 2) is None:
                continue
            high = [shared._section_height(segments, value) for value in (a, b)]
            if any(value is None for value in high):
                continue
            faces += shared._section_wall(a, b, [bottom, bottom], high, normal, station,
                                          axis, painter, normal)
    return faces, minimum


def _graded_faces(graded, painter, flat_faces):
    """Share the existing body planes across pavement and raised rail tops.

    A curved ruled quad is not planar. Independently triangulating a narrower
    roof can make it less than a metre above the unchanged wider underside.
    The actual body mesh is the reference here: clip every top band to its
    finite planes, retain each rail's measured rise, and leave all body and
    support contact vertices unchanged. Endpoint overhangs may use only the
    adjacent actual flat body within the existing five-metre end windows.
    """
    body_code = painter.role("body")

    def area_mask(geometry):
        # An overlay may include coincident boundary lines beside polygons.
        # They have no top-surface area, and subsequent overlay can reject
        # a mixed-dimension input. Keep every positive polygon component.
        def polygons(value):
            if value.geom_type == "Polygon":
                return [value] if not value.is_empty else []
            return [part for child in getattr(value, "geoms", ()) for part in polygons(child)]
        parts = polygons(geometry)
        return shapely.union_all(parts) if parts else Polygon()

    def downward(triangle):
        points = np.asarray(triangle)[:, :3]
        return np.cross(points[1] - points[0], points[2] - points[0])[1] < -1e-12

    def body_records(faces):
        records = []
        for triangle in faces:
            if round(triangle[0][5]) != body_code or not downward(triangle):
                continue
            points = [(p[0], -p[2]) for p in triangle]
            polygon = Polygon(points)
            if polygon.area <= 1e-14:
                continue
            field = np.linalg.solve(np.array([[*p, 1.] for p in points]),
                                    np.array([p[1] + shared.DEPTH for p in triangle]))
            records.append((polygon, field))
        return records

    flat = body_records(flat_faces)
    flat_tree = shapely.STRtree([record[0] for record in flat])
    result = []
    painter.graded_top_plan_crop_area_by_road_m2 = {}
    for road in graded:
        crop_areas = {"pavement": 0., "barrier": 0.}
        original = shared._graded_faces([road], painter, reverse_traffic=True)
        bases = body_records(original)
        tree = shapely.STRtree([record[0] for record in bases])
        body_outline = area_mask(shapely.union_all([record[0] for record in bases]))
        roof_heights = np.array([p[2] + shared.pavement_datum(p[2]) for p in road["points"]])
        for triangle in original:
            role = painter.roles[round(triangle[0][5])]
            if role == "body":
                result.append(triangle)
                continue
            shared._require(role in ("pavement", "barrier"), "Unknown reversed graded top role")
            xy = [(p[0], -p[2]) for p in triangle]
            polygon = Polygon(xy)
            if polygon.area <= 1e-14:
                continue
            matrix = np.array([[*p, 1.] for p in xy])
            uv_field = np.linalg.solve(matrix, np.array([[p[3], p[4]] for p in triangle]))
            rises = np.zeros(3) if role == "pavement" else np.array([
                p[1] - np.interp(p[3] * 16., road["station"], roof_heights) for p in triangle])
            rise_field = np.linalg.solve(matrix, rises)
            windows = [(deck, area_mask(window))
                       for deck, window in painter.graded_end_windows.pop(id(triangle))]
            # Body triangles form a partition. Clip against each plane
            # independently; repeatedly subtracting internal shared edges
            # can manufacture microscopic leftover strips in GEOS.
            pending = area_mask(polygon.difference(body_outline))
            flat_regions = []
            retained = []

            def append(region, field):
                top = field + rise_field
                faces = _coherent_top_surface(region,
                    lambda p: float(np.r_[p, 1.] @ top), round(triangle[0][5]),
                    lambda p: tuple(np.r_[p, 1.] @ uv_field))
                for face in faces:
                    footprint = Polygon([(p[0], -p[2]) for p in face])
                    retained.append(footprint)
                    painter.graded_end_windows[id(face)] = [
                        (deck, area_mask(window.intersection(footprint))) for deck, window in windows]
                result.extend(faces)

            for index in tree.query(polygon, predicate="intersects"):
                footprint, field = bases[int(index)]
                selected = area_mask(polygon.intersection(footprint))
                if selected.area > 1e-14:
                    append(selected, field)
            if pending.area > 1e-14:
                # Inner miter vectors can project past the terminal graded
                # section. Only a real neighbouring flat slab at this same
                # endpoint height can support that finite raised-band part.
                for index in flat_tree.query(pending, predicate="intersects"):
                    footprint, field = flat[int(index)]
                    if np.linalg.norm(field[:2]) > 1e-8:
                        continue
                    altitude = float(field[2])
                    endpoint = next((deck for deck, height in (("lower", roof_heights[0]),
                                      ("upper", roof_heights[-1])) if abs(altitude - height) < 1e-8), None)
                    if endpoint is None:
                        continue
                    allowed = next(window for deck, window in windows if deck == endpoint)
                    selected = area_mask(area_mask(pending.intersection(footprint)).intersection(allowed))
                    if selected.area > 1e-14:
                        append(selected, field)
                        flat_regions.append(selected)
                pending = area_mask(pending.difference(shapely.union_all(flat_regions)))
            emitted = area_mask(shapely.union_all(retained))
            cropped = _supported_top_crop(polygon, emitted)
            crop_areas[role] += cropped
            if cropped > 0.:
                painter.graded_top_plan_crop_bound_m = 1e-9
        painter.graded_top_plan_crop_area_by_road_m2[road["id"]] = {
            **crop_areas, "total": sum(crop_areas.values())}
    return result


def world_geometry(context):
    """Compile a coordinated reversed physical world before type allocation."""
    # Reading source validates the exact original design/review derivation.
    report = source.source_report()
    native_inputs = (("dd_rhw", 0x57530900), ("dd_rhw", 0x57530000),
                     ("dd_rhw", 0x57530200), ("dd_rhw", 0x5753A380), ("mis", 0x57722000))
    hashes = tuple(hashlib.sha256(context[label][*S3D, donor]).hexdigest()
                   for label, donor in native_inputs)
    key = hashes + tuple(hashlib.sha256(path.read_bytes()).hexdigest() for path in (
        SUBJECT / "evidence/design-geometry.jsonc", SUBJECT / "checks/support-solids.jsonc",
        source.ORIGINAL / "evidence/design-geometry.jsonc", source.ORIGINAL / "evidence/source-verification.jsonc"))
    if key in _WORLD_CACHE:
        return _WORLD_CACHE[key]
    profiles = shared._native_profiles(context, native_source=native_models, sockets=SOCKETS)
    painter = shared._Painter(context, profiles)
    core_inner_east = native_models.native_join_plane(context, "C") - 3.
    core_full_width_station = SOCKETS["C"]["point"][0] - core_inner_east
    flat, graded, roads, reference, mouths = shared._unions(profiles,
        construction_routes=shared.source_routes(), sockets=SOCKETS, native_source=native_models,
        full_width_stations={"C": core_full_width_station})
    painter.marking_fields = shared.ribbon_markings(
        roads, profiles, SOCKETS, shared.BARRIER[-1][0], reverse_traffic=True)
    native_faces, patches, native_original, collar_data, barrier_masks = shared._native_collars(
        context, painter, native_source=native_models, sockets=SOCKETS, profiles=profiles,
        low_floor_kind="helper", roof_priority_kind="helper", visible_priority_mask=True)
    interface = _core_interface(context)
    north = [-p[2] for group in native_models.posed_native_faces(context, "C", False)
             if group["role"] == "pavement" for triangle in group["triangles"] for p in triangle]
    north_interval = (max(-8., min(north)), min(8., max(north)))
    for deck in flat:
        native_patch = [p["geometry"] for p in patches if p["deck"] == deck]
        interface_roof = [Polygon([(p[0], -p[2]) for p in triangle]) for group in interface
                          if group["role"] == "pavement" and group["deck"] == deck
                          for triangle in group["triangles"]]
        physical_interface = shapely.union_all(interface_roof)
        flat[deck] = shapely.union_all([flat[deck].difference(native_original[deck]),
                                       *native_patch, physical_interface], grid_size=1e-9)
        flat[deck] = flat[deck].difference(box(43., -100., 56., -8.))
        height = 15. + shared.DATUM_UPPER if deck == "upper" else 7.5 + shared.DATUM_LOWER
        patches.append({"geometry": physical_interface, "height": height, "deck": deck,
                        "kind": "existing-native-C-interface-roof-reference"})
    flat_faces = shared._flat_faces(flat, graded, roads, profiles, painter, reference, patches,
        barrier_masks, shared._peer_step_profiles(context, native_source=native_models,
            sockets=SOCKETS, low_floor_kind="helper"), mouths,
        surface_domains=_surface_domains, bottom_builder=_underside_faces)
    graded_faces = _graded_faces(graded, painter, flat_faces)
    flat_faces, graded_faces = shared._join_graded_barrier_tops(flat_faces, graded_faces, graded, painter)
    profile_joins = shared._native_inner_profile_joins(native_faces, flat_faces, context, painter,
        native_source=native_models, sockets=SOCKETS, core_north_interval=north_interval)
    core_caps, minimum = _core_caps(native_faces, interface, context, painter, north_interval)
    outer_walls = shared._peer_outer_walls(context, painter, native_source=native_models,
        sockets=SOCKETS, low_floor_kind="helper", floor_matched_underside=True)
    mouth_faces, mouth_records = shared._native_mouth_caps(flat, context, painter,
        native_source=native_models, floor_matched_underside=True)
    raised_mouth = shared._peer_raised_mouth_caps(native_faces, context, painter,
        native_source=native_models, sockets=SOCKETS, low_floor_kind="helper")
    support_faces, supports = shared._support_solids(painter, subject=SUBJECT)
    faces = flat_faces + graded_faces + native_faces + profile_joins + core_caps + outer_walls + mouth_faces + raised_mouth + support_faces
    partition = _partition_coherent_triangles(faces)
    paths = ramp_paths.slice_routes(source.source_routes())
    for cell in list(partition):
        if cell == (3, 0):
            continue
        keep = []
        for triangle in partition[cell]:
            if painter.roles[round(triangle[0][5])].endswith("-retained-core-collar"):
                dx, dz = 16 * (cell[0] - 3), 16 * cell[1]
                partition.setdefault((3, 0), []).append(tuple((p[0] + dx, p[1], p[2] + dz, *p[3:]) for p in triangle))
            else:
                keep.append(triangle)
        if keep:
            partition[cell] = keep
        else:
            partition.pop(cell)
    if (3, 1) in partition:
        boundary = partition[(3, 1)]
        # These finite side caps lie on the C owner's exact south boundary;
        # the generic cutter selected the other adjacent city tile. Their
        # full physical faces belong to C, with no plan area in the south cell.
        if all(painter.roles[round(triangle[0][5])] == "body"
               and all(abs(point[2] + 8.) < 1e-9 for point in triangle)
               for triangle in boundary):
            partition.setdefault((3, 0), []).extend(
                tuple((p[0], p[1], p[2] + 16., *p[3:]) for p in triangle)
                for triangle in partition.pop((3, 1)))
    reserved = {tuple(cell) for cells in native_models.reserved_native_cells(2).values() for cell in cells}
    for cell in list(set(partition) & reserved):
        for triangle in partition.pop(cell):
            hosts = []
            for axis, side, delta in ((0, -8., (-1, 0)), (0, 8., (1, 0)), (2, -8., (0, -1)), (2, 8., (0, 1))):
                host = cell[0] + delta[0], cell[1] + delta[1]
                if host not in reserved and host in partition and all(abs(p[axis] - side) < 1e-9 for p in triangle):
                    hosts.append(host)
            shared._require(hosts, "Reversed authored geometry enters a native traffic cell")
            host = hosts[0]
            dx, dz = 16 * (cell[0] - host[0]), 16 * (cell[1] - host[1])
            partition[host].append(tuple((p[0] + dx, p[1], p[2] + dz, *p[3:]) for p in triangle))
    shared._require(set(paths) <= set(partition), "Reversed PATH cell lacks a road model")
    native_models.check_reserved_native_corridor(partition)
    result = {"triangles": faces, "tiles": partition, "paths": paths, "roles": tuple(painter.roles),
        "materials": painter.materials, "painter": painter, "template": profiles["C", "upper"]["model"],
        "supports": supports, "flat_polygons": flat, "graded": graded, "native_collars": collar_data,
        "native_owned_interface_reference": interface,
        "engineering": {
            "y_junction_variant": "reversed",
            "shapely_version": shapely.__version__, "geos_version": shapely.geos_version_string,
            "physical_curve_order": "Original ascending canonical construction order; distinct from reversed directed PATH order",
            "source_design_sha256": key[-4], "support_contract_sha256": key[-3],
            "native_profile_resources": ["57530200", "57530900", "57530000"],
            "native_helper_pavement_datums_m": {"A": 0., "B": 0., "C": [shared.DATUM_LOWER, shared.DATUM_UPPER]},
            "standard_deck_depth_m": shared.DEPTH,
            "302_collar_underside_policy": "Exact source roof minus1m, with finite internal underside steps to unchanged generic slab",
            "underside_owner_mask_input_grid_m": 1e-9,
            "native_C_interface_policy": "Actual already-rendered outside300pose1 roof supplies only the finite55.998999596..56m interface; no copied DAT roof and no authored underside exemption",
            "authored_core_cap_planes_en_m": {"east": 56., "south": -8., "minimum_east": minimum},
            "native_C_full_width_station_m": core_full_width_station,
            "single_lane_deck_width_m": shared.WIDTH,
            "single_lane_asphalt_width_m": shared.WIDTH - 2 * shared.BARRIER[-1][0],
            "barrier_inner_base_inset_m": shared.BARRIER[-1][0],
            "barrier_cross_profile_inset_rise_m": [list(pair) for pair in shared.BARRIER],
            "graded_inner_shoulder_tapers": shared._taper_engineering(roads),
            "taper_station_frame": "Canonical physical construction frame, not reversed directed travel station",
            "graded_top_plane_policy": "Pavement and measured raised-rail profiles share the actual unchanged full-width body plane mesh; endpoint portions require the adjacent actual flat slab",
            "graded_top_plane_partition": "Exact finite plane-mask intersections; zero-area boundary components are not top surfaces",
            "city_partition_surface_policy": "Exact existing plane cuts and1nm boundary snap retain every nonzero triangle; no positive-area closing fragment cutoff",
            "graded_top_plan_boundary_crop_bound_m": getattr(painter, "graded_top_plan_crop_bound_m", 0.),
            "graded_top_plan_crop_area_by_road_m2": painter.graded_top_plan_crop_area_by_road_m2,
            "flat_asphalt_texture_domains": painter.flat_texture_domains,
            "flat_asphalt_uv_method": "Actual opposing native affine fans; reversed transverse/longitudinal single-owner route ribbon fields",
            "authored_native_mouth_caps": mouth_records,
            "authored_302_raised_mouth_cap_triangles": len(raised_mouth),
            "authored_inner_profile_join_triangles": len(profile_joins),
            "authored_302_outer_wall_triangles": len(outer_walls), "authored_core_cap_triangles": len(core_caps),
            "source_route_count": len(report["routes"]), "saved_physical_verification": "not supplied by writer",
        }}
    _WORLD_CACHE.clear()
    _WORLD_CACHE[key] = result
    return result
