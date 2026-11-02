"""Physical geometry for the approved compact, parallel DD RHW diamond.

The approved source routes remain exact. The straight native decks retain
all pavement inside q=8 m; independently placed ramp models contain every
curved high throat outside that real edge. Graded straight models and flat
right-turn terminals meet at functional cuts independently of PATH ownership.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from functools import lru_cache
import math

from . import ramp_geometry as geometry
from . import ramp_paths as paths
from .parallel_ramp_review import review
from .parallel_layout import GROUPS, STRAIGHT_MODEL_HOSTS, owner
from .ramp_materials import NativeRoadPainter
from .slip_lanes import WHITE

ROOT_TWO = math.sqrt(2.0)
GROUND_MOUTH_WIDTH_M = 3.5
GROUND_MOUTH_TAPER_M = 3.0


def _require(condition, message):
    if not condition:
        raise ValueError(message)


@lru_cache(maxsize=1)
def _source():
    return next(row for row in review()['candidates'] if row['id'] == 'parallel-inward-upper')


def routes():
    """Add shoulder auxiliary lanes while retaining physical ramp geometry."""
    from .parallel_slip_lanes import apply
    return [apply(route) for route in _source()['routes']]


def _stem(route):
    return route['deck'] + ('-exit' if route['direction'] == 'off' else '-entry')


def _section(route, kind):
    return next(row for row in route['segments'] if row['kind'] == kind)


def _station(point, route, lengths):
    # The midpoint of a narrow indexed face stays close to its source spine.
    best = None
    for index, (a, b) in enumerate(zip(route['points'], route['points'][1:])):
        dx, dy = b[0] - a[0], b[1] - a[1]
        squared = dx * dx + dy * dy
        t = min(1.0, max(0.0, ((point[0] - a[0]) * dx + (point[1] - a[1]) * dy) / squared))
        q = tuple(a[k] + t * (b[k] - a[k]) for k in range(3))
        score = sum((point[k] - q[k]) ** 2 for k in (0, 1))
        if best is None or score < best[0]:
            best = score, lengths[index] + t * math.sqrt(squared)
    return best[1]


def _role_for_station(route, distance, lengths):
    grade = _section(route, 'straight-parallel-descent')
    low, high = lengths[grade['start_index']], lengths[grade['end_index']]
    if route['direction'] == 'off':
        return 'departure' if distance < low else 'grade' if distance < high else 'terminal'
    return 'terminal' if distance < low else 'grade' if distance < high else 'departure'


def _model_key(route, role):
    if role == 'terminal':
        return 'northwest-terminal' if route['deck'] == 'lower' else 'southeast-terminal'
    return _stem(route) + '-' + role


def _supported_pier(support):
    footprint = support['footprint_en']
    tops = support['top_corner_heights_m']
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(footprint, footprint[1:] + footprint[:1]))
    if area < 0:
        footprint, tops = list(reversed(footprint)), list(reversed(tops))
    vertices = [(p[0], h, -p[1], *geometry.ATLAS_UV['concrete'])
                for h, p in [(0.0, p) for p in footprint]]
    vertices += [(p[0], h, -p[1], *geometry.ATLAS_UV['concrete']) for p, h in zip(footprint, tops)]
    faces = []
    for indices in ((0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7), (4, 5, 6, 7)):
        faces.extend(geometry._triangulate([vertices[i] for i in indices]))
    return faces


def _paint_ribbon(points, low=-.125, high=.125):
    _lengths, normals = geometry.route_frames(points)
    for index, (first, last) in enumerate(zip(points, points[1:])):
        polygon = []
        for point, normal, lateral, across in ((first, normals[index], low, 0.0),
                                               (first, normals[index], high, 1.0),
                                               (last, normals[index + 1], high, 1.0),
                                               (last, normals[index + 1], low, 0.0)):
            polygon.append((point[0] + lateral * normal[0], point[2] + .01,
                            -point[1] - lateral * normal[1], WHITE, across))
        yield from geometry._triangulate(polygon, (0.0, 1.0, 0.0))


def _inside_native(faces, side, inner=4.375):
    output = []
    for triangle in faces:
        polygon = list(triangle)
        polygon = geometry._clip(polygon, lambda p: 8.0 - side * (-p[2] - p[0] + 8.0) / ROOT_TWO)
        polygon = geometry._clip(polygon, lambda p: side * (-p[2] - p[0] + 8.0) / ROOT_TWO - inner)
        output.extend(geometry._triangulate(polygon, (0.0, 1.0, 0.0)))
    return output


def slip_paint(route):
    """Uniform 0.25 m paint following the actual new ramp, never an old curve.

    A dashed separator becomes the straight edge of a hatched gore exactly
    where the inner ramp stripe leaves that edge. All hatch cores are parallel
    45-degree strips and clipped inside the actual two gore boundaries.
    """
    if route.get('highway_slip_profile'):
        from .parallel_slip_lanes import surfaces
        return surfaces(route)
    points = route['points'] if route['direction'] == 'off' else list(reversed(route['points']))
    _lengths, normals = geometry.route_frames(points)
    height, side = route['height_m'], route['side']
    u0, _v0 = geometry.highway_coordinates(points[0])
    direction = 1.0 if geometry.highway_coordinates(points[1])[0] > u0 else -1.0
    inner, outer = [], []
    # Paint lies safely beside, rather than underneath, the Jersey foot.
    paint_offset = 3.0 - .828125 - .4
    for p, n in zip(points, normals):
        if abs(p[2] - height) > 1e-7:
            break
        pair = [(p[0] + sign * paint_offset * n[0], p[1] + sign * paint_offset * n[1], p[2])
                for sign in (-1.0, 1.0)]
        pair.sort(key=lambda q: side * geometry.highway_coordinates(q)[1])
        inner.append(pair[0]); outer.append(pair[1])
    faces = _inside_native(_paint_ribbon(outer), side)
    faces += _inside_native(_paint_ribbon(inner), side)
    uv = [(direction * (geometry.highway_coordinates(p)[0] - u0),
           side * geometry.highway_coordinates(p)[1]) for p in inner]
    gore = []
    for (sa, qa), (sb, qb) in zip(uv, uv[1:]):
        if max(qa, qb) <= 4.5:
            continue
        if qa < 4.5:
            sa += (sb - sa) * (4.5 - qa) / (qb - qa); qa = 4.5
        if qb < 4.5:
            sb = sa + (sb - sa) * (qa - 4.5) / (qa - qb); qb = 4.5
        cap = [(sa, 4.5), (sb, 4.5), (sb, min(8.0, qb)), (sa, min(8.0, qa))]
        if cap[2][1] <= 4.5 and cap[3][1] <= 4.5:
            continue
        gore.append(cap)
    nose = min((p[0] for poly in gore for p in poly), default=17.0)
    finish = max((p[0] for poly in gore for p in poly), default=17.0)
    # Constant lane-edge dashes retain their native quarter-metre width.
    for index in range(math.ceil(max(0.0, nose) / 5.0)):
        low, high = index * 5.0 + 1.0, min(nose, index * 5.0 + 3.5)
        if high <= low:
            continue
        a = geometry.world_coordinates(u0 + direction * low, side * 4.5, height)
        b = geometry.world_coordinates(u0 + direction * high, side * 4.5, height)
        faces += _inside_native(_paint_ribbon([a, b]), side)
    if finish > nose:
        a = geometry.world_coordinates(u0 + direction * nose, side * 4.5, height)
        b = geometry.world_coordinates(u0 + direction * finish, side * 4.5, height)
        faces += _inside_native(_paint_ribbon([a, b]), side)
    # Clip exact 45-degree, constant-width hatch bands in source (s,q) space.
    for polygon in gore:
        for n in range(math.floor((min(p[0] - p[1] for p in polygon) - .18) / 1.5),
                       math.ceil((max(p[0] - p[1] for p in polygon) + .18) / 1.5) + 1):
            centre = n * 1.5
            clipped = geometry._clip(polygon, lambda p: p[0] - p[1] - centre + .125 * ROOT_TWO)
            clipped = geometry._clip(clipped, lambda p: centre + .125 * ROOT_TWO - p[0] + p[1])
            if len(clipped) < 3:
                continue
            world = []
            for s, q in clipped:
                e, north, h = geometry.world_coordinates(u0 + direction * s, side * q, height + .01)
                world.append((e, h, -north, WHITE, .5 + (s - q - centre) / (.25 * ROOT_TWO)))
            faces += geometry._triangulate(world, (0.0, 1.0, 0.0))
    return faces


def terminal_pavement(route):
    """Narrow only the grounded right turn, preserving its full-width join.

    The grade/terminal interface stays six metres wide. Moving away from
    that cut, a three-metre smoothstep taper reaches the earlier compact
    design's 3.5 m ground lane. Its Avenue-parallel collar keeps that width,
    exposing the native adaptive sidewalk beside the adjacent car lane.
    No fixed sidewalk geometry or paint is added across the driveway.
    """
    points = route['points']
    lengths, normals = geometry.route_frames(points)
    turn = _section(route, 'ground-right-quarter-turn')
    off = route['direction'] == 'off'
    cut = turn['start_index'] if off else turn['end_index']
    indices = range(cut, len(points)) if off else range(cut + 1)
    rows = []
    for index in indices:
        _require(abs(points[index][2]) < 1e-8, 'A narrowed terminal must be wholly grounded')
        distance = abs(lengths[index] - lengths[cut])
        t = min(1.0, distance / GROUND_MOUTH_TAPER_M)
        smooth = t * t * (3.0 - 2.0 * t)
        half = 3.0 + (GROUND_MOUTH_WIDTH_M / 2.0 - 3.0) * smooth
        rows.append((points[index], normals[index], half))
    faces = []
    for first, last in zip(rows, rows[1:]):
        # Retain the traffic spine as an explicit triangulation boundary.
        for left, right in ((-1.0, 0.0), (0.0, 1.0)):
            polygon = [geometry._vertex(point, lateral * half, normal, 'asphalt')
                       for (point, normal, half), lateral in
                       ((first, left), (first, right), (last, right), (last, left))]
            faces.extend(geometry._triangulate(polygon, (0.0, 1.0, 0.0)))
    return faces


@lru_cache(maxsize=1)
def _procedural():
    models = {key: [] for key in GROUPS}
    paint = []
    ramps = routes()
    for route in ramps:
        physical = {**route, 'points': route.get('mesh_points', route['points']),
                    'segments': route.get('mesh_segments', route['segments'])}
        lengths, _normals = geometry.route_frames(physical['points'])
        faces = geometry.compact_ramp_triangles(route)
        for face in faces:
            centre = (sum(p[0] for p in face) / 3.0, -sum(p[2] for p in face) / 3.0,
                      sum(p[1] for p in face) / 3.0)
            role = _role_for_station(physical, _station(centre, physical, lengths), lengths)
            if (role == 'terminal' and all(abs(p[1]) < 1e-8
                    and abs(p[3] - geometry.ATLAS_UV['asphalt'][0]) < 1e-8 for p in face)):
                # Replace the old six-metre flat apron instead of overlaying
                # a narrow lane on top of pavement that still masks sidewalks.
                continue
            models[_model_key(route, role)].append(face)
        models[_model_key(route, 'terminal')].extend(terminal_pavement(route))
        for support in route['supports']:
            models[_stem(route) + '-grade'].extend(_supported_pier(support))
        paint.extend(slip_paint(route))
    # Four explicit native centre piers remain clear of the Avenue and ramps.
    for cell in ((-1, 1), (-1, 2), (1, -1), (2, -1)):
        models[owner(STRAIGHT_MODEL_HOSTS[cell])].extend(
            geometry.support_triangles(centers=((16.0 * cell[0], -16.0 * cell[1]),)))
    # Paint belongs to the exact straight native model owner, never the ramp.
    for cell, faces in geometry.partition_triangles(paint).items():
        _require(cell in {c for _name, cells, _role in GROUPS.values() for c in cells},
                 'Parallel slip paint invents a construction cell')
        models[owner(STRAIGHT_MODEL_HOSTS.get(cell, cell))].extend(
            tuple((p[0] + 16 * cell[0], p[1], p[2] + 16 * cell[1], *p[3:])
                                        for p in face) for face in faces)
    # Each functional mesh can overhang only the already approved city union.
    expected = set(map(tuple, _source()['owned_cells']))
    for key, faces in models.items():
        _require(set(geometry.partition_triangles(faces)) <= expected,
                 f'Physical model {key} leaves the approved 31-cell plot')
    return ramps, models


def procedural_geometry():
    """Return independent lists of complete physical models per function."""
    ramps, models = _procedural()
    return deepcopy(ramps), deepcopy(models)


def cut_sections():
    """Source interface witnesses; the verifier must derive its own witnesses."""
    result = []
    for route in routes():
        segment = _section(route, 'straight-parallel-descent')
        lengths, normals = geometry.route_frames(route['points'])
        for index, label in ((segment['start_index'], 'start'), (segment['end_index'], 'end')):
            point, normal = route['points'][index], normals[index]
            result.append({'route_id': route['id'], 'physical_cut': label, 'centre_enh': point,
                           'normal_en': normal, 'width_m': 6.0, 'underside_thickness_m': 1.0,
                           'barrier_profile': list(geometry.NATIVE_BARRIER_PROFILE),
                           'station_m': lengths[index]})
    return result


class ParallelRoadPainter(NativeRoadPainter):
    """Keep the actual native repeat spatial through tight ground-turn miters.

    Nearest-chord projection clamps to a shared vertex in the outside wedge
    between two turn chords. Both the unmarked transverse crop and station
    can then become constant over a nonzero-area pavement triangle. Keep the
    measured native U crop, and extend the nearest flat chord's longitudinal
    tangent beyond its finite end for that ground wedge. One metre along that
    tangent remains exactly 1/16 of a native texture repeat. The field is
    evaluated per world vertex, so clipping and physical piece boundaries
    cannot restart its phase. Elevated wear and material flags remain exact.
    """

    def __init__(self, context, roads):
        super().__init__(context, roads)
        self._ground_station_cache = {}

    def _ground_station(self, point, owner):
        identity = tuple(round(value, 7) for value in point), owner
        if identity in self._ground_station_cache:
            return self._ground_station_cache[identity]
        best = None
        for index in self.road_segments[owner]:
            a, b, station, length, tx, ty, _owner = self.segments[index]
            raw = (point[0] - a[0]) * tx + (point[1] - a[1]) * ty
            along = min(length, max(0.0, raw))
            height = a[2] + along / length * (b[2] - a[2])
            score = ((point[0] - a[0] - along * tx) ** 2
                     + (point[1] - a[1] - along * ty) ** 2
                     + 4.0 * (point[2] - height) ** 2)
            if best is None or score < best[0]:
                # Only an actual flat ground chord can extend its station.
                extended = raw if abs(a[2]) < 1e-8 and abs(b[2]) < 1e-8 else along
                best = score, station + extended
        self._ground_station_cache[identity] = best[1]
        return best[1]

    def paint(self, triangle, cell=(0, 0)):
        result = super().paint(triangle, cell)
        if result is None:
            return result
        world = [(p[0] + 16 * cell[0], -p[2] - 16 * cell[1], p[1]) for p in triangle]
        centre = tuple(sum(p[axis] for p in world) / 3.0 for axis in range(3))
        owner = self._frame(centre)[3]
        if result[0] == 'barrier':
            frames = [self._frame(point, owner) for point in world]
            normalized = [(point[2] - frame[2]) / max(1e-7, min(1.0, frame[2] / 1.5))
                          for point, frame in zip(world, frames)]
            # The generic donor painter's 3 cm crown guard also accepts a
            # genuine 1.59 cm bevel in the tightly clipped native bridge.
            # Preserve a true crown; map a real bevel by its actual height.
            approximate_crown = all(abs(height - 1.390625) < .03 for height in normalized)
            exact_crown = all(abs(height - 1.390625) < 2e-5 for height in normalized)
            if approximate_crown and not exact_crown:
                revised = []
                for painted, height in zip(result[1], normalized):
                    v = (1.0 - .2880359888076782 * max(0.0, height) / .328125
                         if height <= .328125 else
                         .7119640111923218 * max(0.0, (1.390625 - height) / 1.0625))
                    revised.append((*painted[:4], v))
                return 'barrier', tuple(revised)
            return result
        if result[0] != 'ramp' or not all(abs(point[1]) < 1e-8 for point in triangle):
            return result
        return 'ramp', tuple((*painted[:4], self._ground_station(point, owner) / 16.0)
                             for painted, point in zip(result[1], world))
