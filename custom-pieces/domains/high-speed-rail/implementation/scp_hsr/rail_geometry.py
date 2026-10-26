"""Sweep NAM's actual rail profile through multi-route HSR/GHSR pieces.

This module makes physical decks, independently of the train directions in a
PATH resource.  A two-track deck must consequently be supplied once, rather
than once for each direction.  Points use SC4PATH (x, y, height) coordinates;
the generated S3D uses (x, height, -y).

The ground rail donor is the elevated profile translated down exactly 15 m.
Its train PATH height is 1 m, whereas elevated HSR uses 15.5 m.  Transitional
decks interpolate between those *model* offsets, instead of assuming that the
two donors have the same distance between the train path and textured bed.

These are procedural textured junctions. They do not invent moving switch
blades, signals, a new train simulation, or evidence of in-game testing.
"""
from __future__ import annotations

import math
import json
from functools import lru_cache

from scp.models import parse_s3d, pack_s3d
from .single_track_models import (
    EPS, _clip, _convex, _lerp, _native, _normal, _pack, _pillar,
    _quad, _require, _subtract_polygons, _template, _triangulate,
)

ELEVATED_PATH_HEIGHT = 15.5
GROUND_PATH_HEIGHT = 1.0
GROUND_MODEL_OFFSET = -15.0
RAIL_RIBBON_HALF_WIDTH = 1.0
BALLAST_U = .61  # Existing native atlas's ballast patch between its two tracks.
BALLAST_HALF_SPAN = .04


def _height_offset(height, ground=False, transition=False):
    """Return the displacement from the native elevated profile.

    A level deck retains the donor's path-to-model difference. A transitional
    deck interpolates the audited native endpoints, including their 0.5 m
    difference in path-to-bed calibration.
    """
    if transition:
        return (height - ELEVATED_PATH_HEIGHT) * 15.0 / 14.5
    return height - (16.0 if ground else ELEVATED_PATH_HEIGHT)


def _deck_height_offset(deck, height, ground=False):
    """Optional per-deck calibration; absent fields preserve the original API.

    ``hsr`` retains the native elevated train-to-bed offset at every height;
    ``ghsr`` retains the native ground offset. ``blend`` joins both audited
    native endpoints and uses elevated calibration above15.5m, including the
    authored L4/30.5m flyover. This avoids stretching the ground calibration
    correction throughout the higher levels.
    """
    profile = deck.get('profile')
    if profile is None:
        return _height_offset(height, ground, bool(deck.get('transition', False)))
    _require(profile in ('hsr', 'ghsr', 'blend'), 'Unknown physical rail profile')
    if profile == 'hsr':
        return height - ELEVATED_PATH_HEIGHT
    if profile == 'ghsr':
        return height - 16.0
    return ((height - ELEVATED_PATH_HEIGHT) * 15.0 / 14.5
            if height <= ELEVATED_PATH_HEIGHT else height - ELEVATED_PATH_HEIGHT)


def _route(points, start_tangent=None, end_tangent=None):
    cleaned = []
    for point in points:
        _require(len(point) == 3 and all(math.isfinite(value) for value in point),
                 'Physical deck route contains an invalid point')
        converted = float(point[0]), float(point[2]), -float(point[1])
        if cleaned:
            distance = math.hypot(converted[0] - cleaned[-1][0], converted[2] - cleaned[-1][2])
            if distance <= EPS:
                _require(abs(converted[1] - cleaned[-1][1]) <= EPS,
                         'A rail deck cannot contain a vertical-only segment')
                continue
        cleaned.append(converted)
    _require(len(cleaned) >= 2, 'A physical rail deck needs two distinct points')
    lengths = [math.hypot(b[0] - a[0], b[2] - a[2]) for a, b in zip(cleaned, cleaned[1:])]
    tangents = [((b[0] - a[0]) / length, (b[2] - a[2]) / length)
                for a, b, length in zip(cleaned, cleaned[1:], lengths)]
    normals = [(t[1], -t[0]) for t in tangents]
    miters = [normals[0]]
    for previous, following in zip(normals, normals[1:]):
        total = previous[0] + following[0], previous[1] + following[1]
        magnitude = math.hypot(*total)
        _require(magnitude > EPS, 'A physical rail deck cannot reverse on itself')
        unit = total[0] / magnitude, total[1] / magnitude
        divisor = unit[0] * following[0] + unit[1] * following[1]
        _require(divisor > .5, 'A physical rail curve needs more intermediate points')
        miters.append((unit[0] / divisor, unit[1] / divisor))
    miters.append(normals[-1])
    for index, tangent in ((0, start_tangent), (-1, end_tangent)):
        if tangent is None:
            continue
        _require(len(tangent) == 2 and all(math.isfinite(value) for value in tangent),
                 'A rail deck endpoint tangent is invalid')
        length = math.hypot(*tangent)
        _require(length > EPS, 'A rail deck endpoint tangent cannot have zero length')
        miters[index] = -tangent[1] / length, -tangent[0] / length
    return cleaned, lengths, miters


def _deck_template(source, width, source_lane):
    if abs(width - 15.0) < EPS:
        template, inner_half = [('bed' if triangle in source['bed'] else 'wall', triangle)
                                for triangle in source['triangles']], source['inner']
    else:
        template, inner_half = _template(source, source_lane, width)
    # Keep the rail-bearing atlas bands separate from the surrounding concrete.
    # Otherwise a curved branch's broad concrete bed can paint over the rails
    # of a continuing mainline. These ribbons retain native UVs exactly.
    centers = (-2.0, 2.0) if abs(width - 15.0) < EPS else (0.0,)
    ribbons = []
    for kind, triangle in template:
        if kind != 'bed':
            continue
        for center in centers:
            polygon = _clip(list(triangle), lambda v, center=center: v[0] - center + RAIL_RIBBON_HALF_WIDTH)
            polygon = _clip(polygon, lambda v, center=center: center + RAIL_RIBBON_HALF_WIDTH - v[0])
            ribbons.extend(('rail', piece) for piece in _triangulate(polygon))
    # Native outer-bed UVs include cable troughs and a wrapped dark edge. At
    # an opened junction those can resemble trenches across another route.
    # Replace only the non-rail floor with the native central ballast patch;
    # extracted rail ribbons and actual parapets retain their original UVs.
    # Mirrored1.25m strips preserve the donor's approximately8 texels/metre,
    # instead of stretching a narrow atlas column across an entire15m deck.
    # The floor continues beneath intact side profiles, so opening a junction
    # parapet never exposes a hole where its old concrete profile used to sit.
    bed = next(triangle for kind, triangle in template if kind == 'bed')
    first, last = max(((a, b) for a in bed for b in bed), key=lambda pair: abs(pair[0][2] - pair[1][2]))
    v_slope = (last[4] - first[4]) / (last[2] - first[2])
    v_intercept = first[4] - v_slope * first[2]
    template = [(kind, triangle) for kind, triangle in template if kind != 'bed'] + ribbons
    count = math.ceil(width / 1.25)
    for index in range(count):
        left, right = -width / 2 + width * index / count, -width / 2 + width * (index + 1) / count
        u_left, u_right = BALLAST_U - BALLAST_HALF_SPAN, BALLAST_U + BALLAST_HALF_SPAN
        if index % 2:
            u_left, u_right = u_right, u_left
        vertices = [(cross, source['bed_y'], longitudinal, u, v_slope * longitudinal + v_intercept)
                    for cross, longitudinal, u in ((left, -8, u_left), (right, -8, u_right),
                                                    (right, 8, u_right), (left, 8, u_left))]
        template.extend(('bed', triangle) for triangle in _quad(vertices, (0, 1, 0)))
    return template, inner_half


def _convex_parts(polygon):
    """Match the actual two swept triangles when an inner miter folds."""
    turns = [(b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
             for a, b, c in zip(polygon, polygon[1:] + polygon[:1], polygon[2:] + polygon[:2])]
    if min(turns) >= -EPS:
        return [polygon]
    result = []
    for index in range(1, len(polygon) - 1):
        part = [polygon[0], polygon[index], polygon[index + 1]]
        area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(part, part[1:] + part[:1]))
        if abs(area) > EPS:
            result.append(_convex(part))
    return result


def _sweep(source, deck, ground):
    points, lengths, miters = _route(deck['points'], deck.get('start_tangent'), deck.get('end_tangent'))
    width = float(deck.get('width', 15.0))
    _require(math.isfinite(width) and (abs(width - 15.0) < EPS or 6.0 <= width <= 8.0),
             'A physical rail deck must be 15 m dual-track or 6–8 m single-track')
    template, inner_half = _deck_template(source, width, deck.get('source_lane', 2.0))
    if not deck.get('rail_ribbons', True):
        # A native-width shoulder/end stub can supply the correct concrete
        # profile while the actual approaching movement curves supply rails.
        # Drawing decorative straight rails here would erase curved tracks.
        template = [(kind, triangle) for kind, triangle in template if kind != 'rail']
    half, distance = width / 2, float(deck.get('uv_offset', 0.0))
    triangles, corridors = [], []
    # A returning curve can cross its endpoint's grid plane again far from
    # that endpoint. Only the contiguous approach needs the native port cut;
    # applying that half-plane to the complete curve deletes valid tracks.
    scoped_planes = []
    for axis, boundary, sign, endpoint in deck.get('scoped_clip_planes', []):
        indices = list(range(len(lengths)))
        if endpoint == -1:
            indices.reverse()
        selected = set()
        for number in indices:
            selected.add(number)
            if min(sign * (point[axis] - boundary) for point in points[number:number + 2]) >= width:
                break
        scoped_planes.append(((axis, boundary, sign), selected, endpoint))
    for number, (a, b, length) in enumerate(zip(points, points[1:], lengths)):
        triangle_start = len(triangles)
        corridor_start = len(corridors)
        na, nb = miters[number:number + 2]

        def position(cross, native_height, fraction):
            center, normal = _lerp(a, b, fraction), _lerp(na, nb, fraction)
            return (center[0] + cross * normal[0],
                    native_height + _deck_height_offset(deck, center[1], ground),
                    center[2] + cross * normal[1])

        footprint = _convex([(position(cross, source['bed_y'], fraction)[0],
                              position(cross, source['bed_y'], fraction)[2])
                             for cross, fraction in ((-half, 0), (half, 0), (half, 1), (-half, 1))])
        rail_polygons, clearance_polygons = [], []
        centers = ((-2.0, 2.0) if abs(width - 15.0) < EPS else (0.0,)) if deck.get('rail_ribbons', True) else ()
        for center in centers:
            rail_polygons.append(_convex([
                (position(cross, source['bed_y'], fraction)[0],
                 position(cross, source['bed_y'], fraction)[2])
                for cross, fraction in ((center - RAIL_RIBBON_HALF_WIDTH, 0),
                                         (center + RAIL_RIBBON_HALF_WIDTH, 0),
                                         (center + RAIL_RIBBON_HALF_WIDTH, 1),
                                         (center - RAIL_RIBBON_HALF_WIDTH, 1))]))
            if deck.get('precise_union', False):
                start = (a[0] + center * na[0], a[2] + center * na[1])
                end = (b[0] + center * nb[0], b[2] + center * nb[1])
                dx, dz = end[0] - start[0], end[1] - start[1]
                span = math.hypot(dx, dz)
                normal = dz / span, -dx / span
                # The default3m envelope has0.1m margin per side. New
                # double-track repairs can opt into a wider clearance mask.
                clearance_half = float(deck.get('clearance_half_width', 1.6))
                if 'clearance_half_width' in deck:
                    _require(math.isfinite(clearance_half) and 1.5 <= clearance_half < inner_half,
                             'Train-clearance half width must fit inside the native parapets')
                clearance_polygons.append(_convex([
                    (point[0] + cross * normal[0], point[1] + cross * normal[1])
                    for point, cross in ((start, -clearance_half), (start, clearance_half),
                                         (end, clearance_half), (end, -clearance_half))]))
        offsets = [_deck_height_offset(deck, p[1], ground) for p in (a, b)]
        corridors.append({'polygon': footprint,
                          'rail_polygons': rail_polygons,
                          'clearance_polygons': clearance_polygons,
                          'low': source['bottom'] + min(offsets),
                          'high': source['top'] + max(offsets),
                          'bed_low': source['bed_y'] + min(offsets),
                          'bed_high': source['bed_y'] + max(offsets)})
        if deck.get('precise_union', False):
            gradient_x = (offsets[1] - offsets[0]) * (b[0] - a[0]) / (length * length)
            gradient_z = (offsets[1] - offsets[0]) * (b[2] - a[2]) / (length * length)
            intercept = offsets[0] - gradient_x * a[0] - gradient_z * a[2]
            values = [gradient_x * x + gradient_z * z + intercept for x, z in footprint]
            corridors[-1].update(height_plane=(gradient_x, gradient_z, intercept),
                                 native_low=source['bottom'], native_high=source['top'], native_bed=source['bed_y'],
                                 low=source['bottom'] + min(values), high=source['top'] + max(values),
                                 bed_low=source['bed_y'] + min(values), bed_high=source['bed_y'] + max(values))
        for kind, triangle in template:
            pairs = [(x, y) for x in triangle for y in triangle if abs(x[2] - y[2]) > 1]
            first, last = max(pairs, key=lambda pair: abs(pair[0][2] - pair[1][2]))
            slope = (last[4] - first[4]) / (last[2] - first[2])
            vertices = []
            for vertex in triangle:
                fraction = min(1.0, max(0.0, (vertex[2] + 8.0) / 16.0))
                xyz = position(vertex[0], vertex[1], fraction)
                v_start = vertex[4] - slope * (vertex[2] + 8.0)
                vertices.append((*xyz, vertex[3], v_start + slope * (distance + fraction * length)))
            triangles.append((kind, tuple(vertices)))
        bottom = [(*position(cross, source['bottom'], fraction), .07, (distance + fraction * length) / 16)
                  for cross, fraction in ((-half, 0), (half, 0), (half, 1), (-half, 1))]
        triangles.extend(('underside', triangle) for triangle in _quad(bottom, (0, -1, 0)))
        if deck.get('precise_union', False):
            corridor = corridors.pop()
            rail_parts = [part for rail in corridor['rail_polygons'] for part in _convex_parts(rail)]
            for index, part in enumerate(_convex_parts(corridor['polygon'])):
                corridors.append({**corridor, 'polygon': part,
                                  'rail_polygons': rail_parts if index == 0 else [],
                                  'clearance_polygons': clearance_polygons if index == 0 else []})
        planes = [plane for plane, selected, endpoint in scoped_planes if number in selected]
        if planes:
            segment_triangles, segment_corridors = _trim_sweep(triangles[triangle_start:], corridors[corridor_start:], planes)
            triangles[triangle_start:] = segment_triangles
            corridors[corridor_start:] = segment_corridors
        distance += length
    # Closed end faces prevent open slab ends when a curved profile protrudes
    # outside its nominal tile. Neighbouring profiles cover these at joins.
    for endpoint_index, endpoint, normal, sign in ((0, points[0], miters[0], -1), (-1, points[-1], miters[-1], 1)):
        triangle_start = len(triangles)
        tangent = -normal[1], normal[0]
        rectangles = [(-half, half, source['bottom'], source['bed_y']),
                      (-half, -inner_half, source['bed_y'], source['top']),
                      (inner_half, half, source['bed_y'], source['top'])]
        for left, right, low, high in rectangles:
            vertices = [(endpoint[0] + cross * normal[0],
                         native_height + _deck_height_offset(deck, endpoint[1], ground),
                         endpoint[2] + cross * normal[1],
                         .02 + .09 * (cross + half) / width, (native_height - low) / 3)
                        for cross, native_height in ((left, low), (right, low), (right, high), (left, high))]
            triangles.extend(('cap', triangle) for triangle in _quad(vertices, (sign * tangent[0], 0, sign * tangent[1])))
        planes = [plane for plane, selected, index in scoped_planes if index == endpoint_index]
        if planes:
            triangles[triangle_start:] = _trim_sweep(triangles[triangle_start:], [], planes)[0]
    planes = deck.get('clip_planes', [])
    if planes:
        triangles, corridors = _trim_sweep(triangles, corridors, planes)
    return triangles, corridors, points, lengths


def _trim_sweep(triangles, corridors, planes):
    clipped_triangles = []
    for kind, triangle in triangles:
        polygon = list(triangle)
        for axis, boundary, sign in planes:
            polygon = _clip(polygon, lambda v, axis=axis, boundary=boundary, sign=sign: sign * (v[axis] - boundary))
        clipped_triangles.extend((kind, piece) for piece in _triangulate(polygon))
    clipped_corridors = []
    for corridor in corridors:
        def clip_footprint(footprint):
            polygon = [(x, 0., z, 0., 0.) for x, z in footprint]
            for axis, boundary, sign in planes:
                polygon = _clip(polygon, lambda v, axis=axis, boundary=boundary, sign=sign: sign * (v[axis] - boundary))
            return [(v[0], v[2]) for v in polygon]
        polygon = clip_footprint(corridor['polygon'])
        if len(polygon) >= 3:
            copy = dict(corridor)
            copy['polygon'] = polygon
            copy['rail_polygons'] = [clipped for rail in corridor['rail_polygons']
                                     if len(clipped := clip_footprint(rail)) >= 3]
            copy['clearance_polygons'] = [clipped for rail in corridor.get('clearance_polygons', [])
                                          if len(clipped := clip_footprint(rail)) >= 3]
            clipped_corridors.append(copy)
    return clipped_triangles, clipped_corridors


class _CorridorIndex:
    """Discard spatially irrelevant cuts while retaining their exact order."""
    def __init__(self, corridors):
        self.corridors, self.bins = corridors, {}
        for index, corridor in enumerate(corridors):
            polygon = corridor['polygon']
            bbox = (min(p[0] for p in polygon), max(p[0] for p in polygon),
                    min(p[1] for p in polygon), max(p[1] for p in polygon))
            corridor['_bbox'] = bbox
            for x in range(math.floor((bbox[0] - EPS) / 16), math.floor((bbox[1] + EPS) / 16) + 1):
                for z in range(math.floor((bbox[2] - EPS) / 16), math.floor((bbox[3] + EPS) / 16) + 1):
                    self.bins.setdefault((x, z), []).append(index)

    def for_triangle(self, triangle):
        bbox = (min(p[0] for p in triangle), max(p[0] for p in triangle),
                min(p[2] for p in triangle), max(p[2] for p in triangle))
        selected = set()
        for x in range(math.floor((bbox[0] - EPS) / 16), math.floor((bbox[1] + EPS) / 16) + 1):
            for z in range(math.floor((bbox[2] - EPS) / 16), math.floor((bbox[3] + EPS) / 16) + 1):
                selected.update(self.bins.get((x, z), []))
        return [self.corridors[index] for index in sorted(selected)]


def _index_corridors(corridors, enabled):
    return _CorridorIndex(corridors) if enabled else corridors


def _subtract_corridors(triangle, corridors, *, bed=False, wall=False):
    if isinstance(corridors, _CorridorIndex):
        corridors = corridors.for_triangle(triangle)
    fragments = [list(triangle)]
    for corridor in corridors:
        if not fragments:
            break
        low = corridor['bed_low'] if bed else corridor['low']
        high = corridor['bed_high'] if bed else corridor['high']
        if wall and 'height_plane' in corridor:
            # At a graded merge, one parapet can sit a few centimetres above
            # its neighbour's top. Opening only the overlapping slab leaves
            # that raised sliver across the train. Open the wall through the
            # declared headroom; floors and bridge undersides stay complete.
            high = corridor['bed_high'] + 5.
        # Texture beds sharing the same elevation are replaced exactly once.
        # Decks at separated heights remain complete, even at a plan crossing.
        tolerance = .035 if bed else .001
        lower, upper = low - tolerance, high + tolerance
        footprint = corridor['polygon']
        xmin, xmax, zmin, zmax = corridor.get('_bbox') or (
            min(point[0] for point in footprint), max(point[0] for point in footprint),
            min(point[1] for point in footprint), max(point[1] for point in footprint))
        result = []
        for polygon in fragments:
            if (max(vertex[0] for vertex in polygon) < xmin - EPS
                    or min(vertex[0] for vertex in polygon) > xmax + EPS
                    or max(vertex[2] for vertex in polygon) < zmin - EPS
                    or min(vertex[2] for vertex in polygon) > zmax + EPS):
                result.append(polygon)
                continue
            if max(vertex[1] for vertex in polygon) < lower or min(vertex[1] for vertex in polygon) > upper:
                result.append(polygon)
                continue
            if 'height_plane' in corridor:
                gx, gz, intercept = corridor['height_plane']
                native_low = corridor['native_bed'] if bed else corridor['native_low']
                native_high = corridor['native_bed'] if bed else corridor['native_high']
                if wall:
                    native_high = corridor['native_bed'] + 5.
                def above_low(vertex):
                    return vertex[1] - (native_low + gx * vertex[0] + gz * vertex[2] + intercept - tolerance)
                def below_high(vertex):
                    return native_high + gx * vertex[0] + gz * vertex[2] + intercept + tolerance - vertex[1]
            else:
                def above_low(vertex):
                    return vertex[1] - lower
                def below_high(vertex):
                    return upper - vertex[1]
            below = _clip(polygon, lambda vertex: -above_low(vertex))
            above = _clip(polygon, lambda vertex: -below_high(vertex))
            middle = _clip(_clip(polygon, above_low), below_high)
            if len(below) >= 3 and any(above_low(vertex) < -EPS for vertex in below):
                result.append(below)
            if len(above) >= 3 and any(below_high(vertex) < -EPS for vertex in above):
                result.append(above)
            if len(middle) >= 3:
                result.extend(_subtract_polygons(middle, corridor['polygon']))
        fragments = result
    return [triangle for polygon in fragments for triangle in _triangulate(polygon)]


def _middle3(points, lengths):
    remaining = sum(lengths) / 2
    for a, b, length in zip(points, points[1:], lengths):
        if remaining <= length:
            return _lerp(a, b, remaining / length)
        remaining -= length
    return points[-1]


def _support_points(points, lengths):
    """Keep elevated concrete posts at intervals of at most sixteen metres."""
    count = max(1, math.ceil(sum(lengths) / 16.0))
    for index in range(count):
        remaining = sum(lengths) * (index + .5) / count
        for a, b, length in zip(points, points[1:], lengths):
            if remaining <= length:
                yield _lerp(a, b, remaining / length)
                break
            remaining -= length


def _sample_distance(points, lengths, distance):
    distance = max(0., min(sum(lengths), distance))
    for a, b, length in zip(points, points[1:], lengths):
        if distance <= length:
            return _lerp(a, b, distance / length), ((b[0] - a[0]) / length, (b[2] - a[2]) / length)
        distance -= length
    length = lengths[-1]
    return points[-1], ((points[-1][0] - points[-2][0]) / length, (points[-1][2] - points[-2][2]) / length)


def _nearest_route_point(center, points):
    best = None
    for a, b in zip(points, points[1:]):
        dx, dz = b[0] - a[0], b[2] - a[2]
        fraction = max(0., min(1., ((center[0] - a[0]) * dx + (center[1] - a[2]) * dz) / (dx * dx + dz * dz)))
        point = _lerp(a, b, fraction)
        distance = math.hypot(center[0] - point[0], center[1] - point[2])
        if best is None or distance < best[0]:
            best = distance, point
    return best


def _support_blockers(source, center, top, own, decks, swept, ground):
    blockers = []
    for index, other in enumerate(decks):
        if index == own:
            continue
        distance, point = _nearest_route_point(center, swept[index][2])
        margin = float(decks[own].get('support_margin', 2.0))
        if distance > float(other.get('width', 15.0)) / 2 + .65 + margin:
            continue
        offset = _deck_height_offset(other, point[1], ground)
        low, high = source['bottom'] + offset, source['top'] + offset
        # A post ending at the underside of a same-level adjoining deck is
        # structurally shared, not a train obstruction. A taller post crossing
        # any lower slab or train envelope is forbidden.
        if low < top - .05 and high > 0:
            blockers.append((index, low, max(high, point[1] + 5.0)))
    return blockers


def _within_support_bounds(center, bounds, cells=None):
    if bounds is not None and not (bounds[0] + .65 <= center[0] <= bounds[1] - .65
                                   and bounds[2] + .65 <= center[1] <= bounds[3] - .65):
        return False
    if cells is not None:
        xs = range(math.floor((center[0] - .65 + 8 + EPS) / 16),
                   math.floor((center[0] + .65 + 8 - EPS) / 16) + 1)
        rows = range(math.floor((center[1] - .65 + 8 + EPS) / 16),
                     math.floor((center[1] + .65 + 8 - EPS) / 16) + 1)
        return all((x, row) in cells for x in xs for row in rows)
    return True


def _portal_beam(center, normal, half_span, top):
    tangent = -normal[1], normal[0]
    points = [(center[0] + side * half_span * normal[0] + front * .65 * tangent[0], height,
               center[1] + side * half_span * normal[1] + front * .65 * tangent[1], .07 + side * .03, height / 16)
              for height in (top - .8, top) for side, front in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    triangles = []
    for face in ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5),
                 (2, 3, 7, 6), (3, 0, 4, 7)):
        vertices = [points[index] for index in face]
        outward = (sum(v[0] for v in vertices) / 4 - center[0],
                   sum(v[1] for v in vertices) / 4 - (top - .4),
                   sum(v[2] for v in vertices) / 4 - center[1])
        triangles.extend(_quad(vertices, outward))
    return triangles


def _safe_supports(source, index, decks, swept, ground, existing, bounds, support_cells):
    deck = decks[index]
    route = deck.get('support_route', deck['points'])
    points, lengths, _ = _route(route)
    total = sum(lengths)
    count = max(1, math.ceil(total / 16.0))
    pillars, beams = [], []
    for number in range(count):
        desired = total * (number + .5) / count
        offsets = [0.] + [direction * distance for distance in (2., 4., 6., 8., 12., 16., 20., 24.) for direction in (-1, 1)]
        found = False
        for offset in offsets:
            distance = desired + offset
            if not .65 <= distance <= total - .65:
                continue
            point, tangent = _sample_distance(points, lengths, distance)
            top = source['bottom'] + _deck_height_offset(deck, point[1], ground)
            if top <= .05:
                found = True
                break
            center = point[0], point[2]
            if not _within_support_bounds(center, bounds, support_cells) or _support_blockers(source, center, top, index, decks, swept, ground):
                continue
            if any(math.dist(center, other) < 1.5 for other in [*existing, *(p[0] for p in pillars)]):
                # The already present pier supports the same structural area.
                found = True
                break
            pillars.append((center, top))
            found = True
            break
        if found:
            continue
        # A long upper line above a parallel lower line can need a portal
        # frame. Both posts stand outside lower rail corridors; its beam stays
        # above the lower train envelope with another5m structural clearance.
        point, tangent = _sample_distance(points, lengths, desired)
        center = point[0], point[2]
        top = source['bottom'] + _deck_height_offset(deck, point[1], ground)
        blockers = _support_blockers(source, center, top, index, decks, swept, ground)
        if blockers and top - .8 >= max(blocker[2] for blocker in blockers) + 5.0:
            normal = tangent[1], -tangent[0]
            for half_span in (10., 12., 16., 20., 24., 32.):
                centers = [(center[0] + sign * half_span * normal[0], center[1] + sign * half_span * normal[1]) for sign in (-1, 1)]
                if all(_within_support_bounds(candidate, bounds, support_cells)
                       and not _support_blockers(source, candidate, top - .8, index, decks, swept, ground)
                       for candidate in centers):
                    pillars.extend((candidate, top - .8) for candidate in centers)
                    beams.extend(_portal_beam(center, normal, half_span, top))
                    found = True
                    break
        _require(found, f"No safe support location for {deck.get('geometry_id', index)!r}; widen the reserved footprint or move the crossing")
    return pillars, beams


def _build_triangles(source, decks, supports, ground, support_bounds=None, support_cells=None):
    swept = [_sweep(source, deck, ground) for deck in decks]
    triangles, pillars, support_beams = [], {}, []
    all_rails = [{**corridor, 'polygon': polygon}
                 for other in swept for corridor in other[1] for polygon in corridor['rail_polygons']]
    spatial_union = any(deck.get('precise_union', False) for deck in decks)
    all_rails = _index_corridors(all_rails, spatial_union)
    for index, (surfaces, corridors, points, lengths) in enumerate(swept):
        other_corridors = [corridor for number, other in enumerate(swept) if number != index for corridor in other[1]]
        later_corridors = [corridor for other in swept[index + 1:] for corridor in other[1]]
        later_rails = [{**corridor, 'polygon': polygon}
                      for other in swept[index + 1:] for corridor in other[1] for polygon in corridor['rail_polygons']]
        other_corridors = _index_corridors(other_corridors, spatial_union)
        later_corridors = _index_corridors(later_corridors, spatial_union)
        later_rails = _index_corridors(later_rails, spatial_union)
        own_clearance = _index_corridors(
            [{**corridor, 'polygon': polygon} for corridor in corridors
             for polygon in corridor.get('clearance_polygons', [])], spatial_union)
        for kind, triangle in surfaces:
            if kind == 'bed':
                for fragment in _subtract_corridors(triangle, later_corridors, bed=True):
                    triangles.extend(_subtract_corridors(fragment, all_rails, bed=True))
            elif kind == 'rail':
                triangles.extend(_subtract_corridors(triangle, later_rails, bed=True))
            elif kind == 'underside':
                # Undersides need only one surface in a shared flat slab.
                triangles.extend(_subtract_corridors(triangle, later_corridors))
            else:
                for fragment in _subtract_corridors(triangle, other_corridors, wall=spatial_union):
                    triangles.extend(_subtract_corridors(fragment, own_clearance, wall=spatial_union))
        if supports and not ground and decks[index].get('support', True):
            if decks[index].get('safe_supports', False):
                additions, beams = _safe_supports(source, index, decks, swept, ground, pillars, support_bounds, support_cells)
                for center, top in additions:
                    key = round(center[0], 4), round(center[1], 4)
                    pillars[key] = min(pillars.get(key, top), top)
                support_beams.extend(beams)
                continue
            support_points, support_lengths = points, lengths
            if 'support_route' in decks[index]:
                support_points, support_lengths, _ = _route(decks[index]['support_route'])
            for middle in _support_points(support_points, support_lengths):
                top = source['bottom'] + _deck_height_offset(decks[index], middle[1], False)
                if top > .05:
                    key = round(middle[0], 4), round(middle[2], 4)
                    pillars[key] = min(pillars.get(key, top), top)
    for center, top in pillars.items():
        triangles.extend(_pillar(center, top))
    triangles.extend(support_beams)
    return triangles


def _pack_junction(source, triangles):
    raw = _pack(source, triangles)
    # A useful distinct mesh label in model editors; geometry/material data
    # otherwise use the same strict packer as the original one-way kit.
    model = parse_s3d(raw)
    model['meshes'][0]['name'] = b'SCP HSR GHSR rail junction\0'
    return pack_s3d(model)


def build_geometry(native_hsr: bytes, decks: list[dict], *, supports=True, ground=False) -> bytes:
    """Build a physical rail junction from distinct, explicitly sized decks.

    Each deck has ``points`` in SC4PATH coordinates, ``width`` 15 (two tracks)
    or 7.5 (one track), and optional ``start_tangent``, ``end_tangent``, and
    ``source_lane`` (+2/-2 for one track). ``transition=True`` interpolates the
    audited ground/elevated model endpoints along a graded route. ``supports``
    adds original concrete posts; ground decks never receive elevated posts.

    Later decks have texture priority in coplanar overlaps. Their footprints
    replace earlier bed triangles, rather than drawing coincident triangles.
    Every deck's parapets are opened where another same-height deck joins it.
    """
    _require(isinstance(decks, (list, tuple)) and decks, 'At least one physical rail deck is required')
    source = _native(native_hsr)
    return _pack_junction(source, _build_triangles(source, decks, supports, ground))


def _global_decks(layout):
    """Reassemble explicitly identified curve fragments across tile borders."""
    groups = {}
    for (x, row), data in layout.items():
        if 'native_source' in data:
            continue
        for number, deck in enumerate(data['decks']):
            identifier = deck.get('geometry_id', ('unshared', x, row, number))
            copy = dict(deck)
            copy['points'] = [(point[0] + x * 16, point[1] - row * 16, point[2])
                              for point in deck['points']]
            groups.setdefault(identifier, []).append(copy)
    result = []
    for identifier, parts in groups.items():
        starts = [part for part in parts
                  if not any(other is not part and math.dist(other['points'][-1], part['points'][0]) < 1e-5
                             for other in parts)]
        _require(len(starts) == 1, f'Physical curve {identifier!r} has disconnected or cyclic fragments')
        part = starts[0]
        combined = dict(part)
        combined['points'] = list(part['points'])
        remaining = [other for other in parts if other is not part]
        while remaining:
            matches = [other for other in remaining if math.dist(combined['points'][-1], other['points'][0]) < 1e-5]
            _require(len(matches) == 1, f'Physical curve {identifier!r} has an ambiguous or missing join')
            part = matches[0]
            _require(abs(part.get('width', 15) - combined.get('width', 15)) < EPS,
                     'A physical curve changes deck width across a tile join')
            combined['points'].extend(part['points'][1:])
            remaining.remove(part)
        combined['end_tangent'] = part.get('end_tangent')
        if combined.get('simplify_collinear', False):
            if combined.get('profile') == 'blend':
                calibrated = [combined['points'][0]]
                for point in combined['points'][1:]:
                    previous = calibrated[-1]
                    if (previous[2] - 15.5) * (point[2] - 15.5) < 0:
                        fraction = (15.5 - previous[2]) / (point[2] - previous[2])
                        crossing = _lerp(previous, point, fraction)
                        calibrated.append((crossing[0], crossing[1], 15.5))
                    calibrated.append(point)
                combined['points'] = calibrated
            simplified = []
            for point in combined['points']:
                while len(simplified) >= 2:
                    a, b = simplified[-2:]
                    u, v = tuple(b[i] - a[i] for i in range(3)), tuple(point[i] - b[i] for i in range(3))
                    cross = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
                    length_u, length_v = math.sqrt(sum(value * value for value in u)), math.sqrt(sum(value * value for value in v))
                    calibrated_join = (combined.get('profile') == 'blend' and abs(b[2] - 15.5) < EPS
                                       and min(a[2], point[2]) < 15.5 < max(a[2], point[2]))
                    if (calibrated_join or sum(x * y for x, y in zip(u, v)) <= 0
                            or math.sqrt(sum(value * value for value in cross)) > 1e-7 * length_u * length_v):
                        break
                    simplified.pop()
                simplified.append(point)
            # Grid cuts are collinear samples, not physical bends. Leaving a
            # cut0.02m after a curve vertex can make a7.5m-wide miter fold back
            # on itself. Global geometry needs only the real curve vertices;
            # the final grid partition recreates all required tile seams.
            combined['points'] = simplified
        # Diagonal lanes meet axis-aligned cell edges beyond the perpendicular
        # cross-section through the centreline's nominal endpoint. Extend the
        # physical deck, then let the outer grid rectangle cut its correct
        # native diagonal half. Supports and texture phase retain the original
        # unextended route, so no extra endpoint pillar or tie-phase jump is
        # introduced.
        combined['support_route'] = list(combined['points'])
        policy = combined.get('extend_endpoints', True)
        planes, extension_lengths = [], []
        for endpoint, tangent_key, direction in ((0, 'start_tangent', -1), (-1, 'end_tangent', 1)):
            tangent = combined.get(tangent_key)
            if tangent is None:
                first, last = (combined['points'][0], combined['points'][1]) if endpoint == 0 else (combined['points'][-2], combined['points'][-1])
                tangent = last[0] - first[0], last[1] - first[1]
            length = math.hypot(*tangent)
            _require(length > EPS, 'Physical curve endpoint has no tangent')
            point = combined['points'][endpoint]
            if policy == 'ports':
                endpoint_planes = []
                for axis, value, component in ((0, point[0], tangent[0]), (2, -point[1], -tangent[1])):
                    nearest = round((value + 8) / 16) * 16 - 8
                    if abs(value - nearest) < 1e-5 and abs(component) > EPS:
                        endpoint_planes.append((axis, nearest, (1 if component > 0 else -1) * -direction))
                planes.extend((*plane, endpoint) for plane in endpoint_planes)
                extend = 15.0 if endpoint_planes and abs(tangent[0]) > EPS and abs(tangent[1]) > EPS else 0.0
            else:
                extend = 15.0 if (policy[0 if endpoint == 0 else 1] if isinstance(policy, (list, tuple)) else policy) else 0.0
            extension_lengths.append(extend)
            if extend:
                extension = (point[0] + direction * extend * tangent[0] / length,
                             point[1] + direction * extend * tangent[1] / length, point[2])
                if endpoint == 0:
                    combined['points'].insert(0, extension)
                else:
                    combined['points'].append(extension)
        if planes:
            combined['scoped_clip_planes'] = planes
        combined['uv_offset'] = -extension_lengths[0]
        result.append(combined)
    _require(result, 'No procedural rail decks in tiled layout')
    return result


def _partition_triangles(triangles, occupied):
    """Partition once across the grid, retaining intentional outer overhangs.

    A curve profile can overhang its centreline's occupied cell, as native
    diagonal rail models do. Fragments in an unoccupied neighbouring cell are
    attached to the closest occupied cell, instead of slicing off parapets or
    drawing duplicate geometry. No new network occupancy is invented here.
    """
    result = {cell: [] for cell in occupied}
    for triangle in triangles:
        low_x, high_x = min(v[0] for v in triangle), max(v[0] for v in triangle)
        low_z, high_z = min(v[2] for v in triangle), max(v[2] for v in triangle)
        if high_x - low_x < EPS:
            xs = [math.floor((low_x + 8 - EPS) / 16)]
        else:
            xs = range(math.floor((low_x + 8) / 16), math.floor((high_x + 8) / 16) + 1)
        if high_z - low_z < EPS:
            rows = [math.floor((low_z + 8 - EPS) / 16)]
        else:
            rows = range(math.floor((low_z + 8) / 16), math.floor((high_z + 8) / 16) + 1)
        for x in xs:
            for row in rows:
                polygon = list(triangle)
                for axis, boundary, sign in ((0, x * 16 - 8, 1), (0, x * 16 + 8, -1),
                                              (2, row * 16 - 8, 1), (2, row * 16 + 8, -1)):
                    polygon = _clip(polygon, lambda vertex, axis=axis, boundary=boundary, sign=sign:
                                    sign * (vertex[axis] - boundary))
                if len(polygon) < 3:
                    continue
                cell = (x, row)
                if cell not in result:
                    center_x = sum(v[0] for v in polygon) / len(polygon)
                    center_z = sum(v[2] for v in polygon) / len(polygon)
                    def distance(candidate):
                        dx = max(0, abs(center_x - candidate[0] * 16) - 8)
                        dz = max(0, abs(center_z - candidate[1] * 16) - 8)
                        return dx * dx + dz * dz, candidate
                    cell = min(occupied, key=distance)
                local = [(vertex[0] - cell[0] * 16, vertex[1], vertex[2] - cell[1] * 16,
                          *vertex[3:]) for vertex in polygon]
                result[cell].extend(_triangulate(local))
    return result


def _build_tiled_geometry(native_hsr: bytes, layout: dict, *, supports=True, ground=False) -> dict:
    """Union a complete multi-cell junction, then emit one model per cell.

    Each local deck fragment carries ``geometry_id``, shared only by fragments
    of the same physical centreline. This lets the whole junction open its
    parapets across tile seams before geometry is partitioned without overlap.
    Native height-adapter cells are left to the caller's exact donor copies.
    """
    source = _native(native_hsr)
    occupied = [cell for cell, data in layout.items() if 'native_source' not in data]
    _require(occupied, 'No procedural tiles in rail geometry layout')
    decks = _global_decks(layout)
    # Keep overhanging curve profiles inside the actual procedural bounding
    # rectangle. Adapter cells lie outside it and remain exact native copies.
    bounds = (16 * min(cell[0] for cell in occupied) - 8,
              16 * max(cell[0] for cell in occupied) + 8,
              16 * min(cell[1] for cell in occupied) - 8,
              16 * max(cell[1] for cell in occupied) + 8)
    triangles = _build_triangles(source, decks, supports, ground, support_bounds=bounds, support_cells=set(occupied))
    clipped = []
    for triangle in triangles:
        polygon = list(triangle)
        for axis, boundary, sign in ((0, bounds[0], 1), (0, bounds[1], -1),
                                      (2, bounds[2], 1), (2, bounds[3], -1)):
            polygon = _clip(polygon, lambda vertex, axis=axis, boundary=boundary, sign=sign:
                            sign * (vertex[axis] - boundary))
        clipped.extend(_triangulate(polygon))
    tiled = _partition_triangles(clipped, occupied)
    empty = [cell for cell, fragments in tiled.items() if not fragments]
    _require(not empty, f'Occupied rail cells have no physical model after union/clipping: {empty}')
    return {cell: _pack_junction(source, fragments) for cell, fragments in tiled.items()}


@lru_cache(maxsize=32)
def _cached_tiled_geometry(native_hsr, physical_layout_json, supports, ground):
    layout = {(x, row): {'decks': decks} for x, row, decks in json.loads(physical_layout_json)}
    return tuple(_build_tiled_geometry(native_hsr, layout, supports=supports, ground=ground).items())


def build_tiled_geometry(native_hsr: bytes, layout: dict, *, supports=True, ground=False) -> dict:
    """Build globally joined per-cell models; reuse identical immutable results.

    The process-local cache includes the complete donor bytes, occupied cells,
    every physical-deck field, endpoint tangents, ground level and support
    setting. It stores only immutable model bytes. A fresh mapping is returned
    for each call, so callers cannot modify another build's cached resources.
    """
    physical_layout = [[cell[0], cell[1], data['decks']]
                       for cell, data in layout.items() if 'native_source' not in data]
    key = json.dumps(physical_layout, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return dict(_cached_tiled_geometry(native_hsr, key, bool(supports), bool(ground)))
