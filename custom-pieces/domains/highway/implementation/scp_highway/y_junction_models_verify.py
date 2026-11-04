"""Inspect actual Y S3D faces, native joins, road shells, and car corridors.

No authoring, loft, planar-union, partition, or support-placement routine is
imported. Checks operate on referenced saved triangles and actual saved PATH
segments. Whole-assembly checks close the module-boundary evidence separately.
"""
from __future__ import annotations

from collections import defaultdict
import hashlib
import itertools
import math
import re
import struct

import numpy as np
from shapely.geometry import Polygon, Point, LineString, box
from shapely.ops import unary_union, nearest_points
from shapely.strtree import STRtree
import shapely

from scp.dbpf import decompress, require
from scp.models import parse_s3d, validate_s3d
from scp.render_meshes import assert_render_budget
from scp.track_paths import PATH, S3D
from scp.verify import parse_paths
from . import y_junction_verify as contract
from .ramp_verify import _barycentric, _clip, _edge_capsule_intervals

POSITION_EPS = 4e-6
DATUM_LOWER = .0009999275207519531
DATUM_UPPER = .0010004043579101562
MATERIALS = {
    'pavement': 'ed1b4a35ab986ff74a56ac79a1a33f579c31bf9630e7bb2b79ad4a4d9b6739ca',
    'native-pavement': '307aba7786d4b4f11dbc499eb54f7d05d01a114001919b8a5f7d55970fbb64ca',
    'body': 'cf4e393b8ca3a2b3d0edba0f86bb197ddf82b65e85cf73cfa13ebd4d2a8c6f6e',
    'barrier': 'd81e8d70e3ab9182adb393f2bc6a61608c70f8129cdb06631409a4b19c73e306',
}
SUPPORT = re.compile(r'^support-(A-B|A-C|B-C|C-B)-(\d+)-(-?1)-(pier|cap|lower-cap)$')


def datum(height):
    return DATUM_LOWER+(height-7.5)/7.5*(DATUM_UPPER-DATUM_LOWER)


def _normal(points):
    return np.cross(np.subtract(points[1], points[0]), np.subtract(points[2], points[0]))


def _kind(role, *, variant='original'):
    require(variant in ('original', 'reversed'), 'Unknown finite Y model variant')
    if role == 'pavement' or re.fullmatch(r'pavement-native-[ABC]-(upper|lower)(-(helper|peer|retained-contact))?', role) or re.fullmatch(
            r'pavement-native-C-(upper|lower)-retained-core-collar', role):
        return 'pavement'
    if role.startswith('support-'):
        require(SUPPORT.fullmatch(role) is not None, 'Unknown Y support-solid role')
        return 'support'
    if re.fullmatch(r'(body|barrier)-native-[ABC]-(upper|lower)-(helper|peer|retained-contact)', role) or re.fullmatch(
            r'(body|barrier)-native-C-(upper|lower)-retained-core-collar', role):
        return role.split('-', 1)[0]
    if role == 'barrier-peer-foot-shim' or (variant == 'reversed' and role == 'barrier-helper-foot-shim'):
        return 'barrier'
    require(role in ('body', 'barrier'), 'Unknown Y physical mesh role: '+role)
    return role


def decode_faces(raw, world_cell, *, variant='original', native_cell_bounds=None):
    """Decode only referenced saved XYZ/UV triangle lists in world ENH."""
    model = parse_s3d(decompress(raw))
    validate_s3d(model)
    assert_render_budget(model)
    require(struct.unpack_from('<H', model['anim_header'])[0] == 1
            and all(chunk[8:] == b'\0'*4 for _label, chunk in model['trailing']),
            'Y saved model hides an unsupported animation or transform')
    faces = []
    for mesh in model['meshes']:
        require(len(mesh['frames']) == 1, 'Y physical mesh must be static')
        vi, ii, pi, mi = mesh['frames'][0]
        block = model['vertices'][vi]
        require(block['stride'] == 20 and block['format'] == 0x80004001,
                'Y authored mesh must use the actual XYZ/one-UV runtime descriptor')
        vertices = [struct.unpack_from('<5f', block['data'], at) for at in range(0, len(block['data']), 20)]
        require(all(all(math.isfinite(v) for v in p) for p in vertices), 'Nonfinite Y model position or texture coordinate')
        name = mesh['name'].rstrip(b'\0').decode('ascii')
        prefixes = [prefix for prefix in ('SCP DD Y ', 'SCP NAM ') if name.startswith(prefix)]
        require(len(prefixes) == 1, 'Y physical mesh lacks a reviewed role label')
        role = name[len(prefixes[0]):]
        kind = _kind(role, variant=variant)
        material = model['materials'][mi]
        material_key = 'native-pavement' if role.startswith('pavement-native-') else (
            'body' if kind == 'support' else kind)
        require(hashlib.sha256(material['raw']).hexdigest() == MATERIALS[material_key],
                'Y physical material differs from its pinned native source')
        require(len(material['textures']) == 1, 'Y physical material must reference one native texture')
        indices = model['indices'][ii]['values']
        for primitive, first, count in model['primitives'][pi]:
            require(primitive == 0 and count % 3 == 0, 'Y saved mesh must use indexed triangle lists')
            for at in range(first, first+count, 3):
                source = [vertices[index] for index in indices[at:at+3]]
                for p in source:
                    retained_corner = variant == 'original' and tuple(world_cell) == (3, 0) and role in (
                        'pavement-native-C-upper-retained-contact', 'pavement-native-C-lower-retained-contact',
                        'body-native-C-upper-retained-contact', 'body-native-C-lower-retained-contact',
                        'barrier-native-C-upper-retained-contact', 'barrier-native-C-lower-retained-contact',
                        'pavement-native-C-upper-retained-core-collar', 'pavement-native-C-lower-retained-core-collar',
                        'body-native-C-upper-retained-core-collar', 'body-native-C-lower-retained-core-collar',
                        'barrier-native-C-upper-retained-core-collar', 'barrier-native-C-lower-retained-core-collar')
                    east_bound = 8.00101 if retained_corner else 8.
                    north_bound = 8.00101 if retained_corner else 8.
                    bounds = (-8., east_bound, -north_bound, 8.)
                    if native_cell_bounds is not None:
                        bounds = native_cell_bounds.get((tuple(world_cell), role), bounds)
                    require(bounds[0]-POSITION_EPS <= p[0] <= bounds[1]+POSITION_EPS
                            and bounds[2]-POSITION_EPS <= p[2] <= bounds[3]+POSITION_EPS,
                            'Y physical model projects outside its actual city owner')
                points = tuple((p[0]+16.*world_cell[0], -p[2]-16.*world_cell[1], p[1]) for p in source)
                normal = _normal(points)
                if np.linalg.norm(normal) < 1e-13:
                    continue
                faces.append({'points': points, 'uv': tuple((p[3], p[4]) for p in source),
                              'role': role, 'kind': kind, 'material': material,
                              'upward': normal[2] > 1e-12, 'downward': normal[2] < -1e-12,
                              'owner_cell': tuple(world_cell)})
    require(faces, 'Y owned model has no actual indexed faces')
    return faces


def _context(donors):
    require(donors, 'Y complete model verification requires the pinned original native model references')
    return {'dd_rhw': donors} if any(isinstance(key, tuple) for key in donors) else donors


def native_faces(donors, *, native_source=None):
    if native_source is None:
        from . import y_junction_native_models as native_source
    posed_native_faces = native_source.posed_native_faces
    result = []
    context = _context(donors)
    for arm in ('A', 'B', 'C'):
        for group in posed_native_faces(context, arm):
            for triangle in group['triangles']:
                points = tuple((p[0], -p[2], p[1]) for p in triangle)
                normal = _normal(points)
                result.append({'points': points, 'uv': tuple((p[3], p[4]) for p in triangle),
                    'kind': group['role'], 'role': 'native-reference-'+group['role'],
                    'material': group['material'], 'upward': normal[2] > 1e-12,
                    'downward': normal[2] < -1e-12, 'native_reference': True})
    return result


def native_traffic(donors, *, native_source=None):
    if native_source is None:
        from . import y_junction_native_models as native_source
    SOCKETS = native_source.SOCKETS
    context = _context(donors)['dd_rhw']
    routes = []
    for socket in SOCKETS.values():
        for target, turns, cell in (socket['helper'], socket['peer']):
            parsed = parse_paths(decompress(context[*PATH, target]))
            for row in parsed['routes']:
                if row['transport'] != 1 or row['points'][0][2] not in (7.5, 15.):
                    continue  # Explicitly exclude native invalid ground capacity routes.
                points = [contract._rotate(point, turns) for point in row['points']]
                routes.append({**row, 'points': [(p[0]+16.*cell[0], p[1]-16.*cell[1], p[2]) for p in points]})
    return routes


class FaceIndex:
    def __init__(self, faces, size=2.):
        self.faces = faces
        self.size = size
        self.grid = defaultdict(list)
        for index, face in enumerate(faces):
            points = np.array(face['points'])
            lo, hi = points[:, :2].min(axis=0), points[:, :2].max(axis=0)
            for x in range(math.floor(lo[0]/size), math.floor(hi[0]/size)+1):
                for y in range(math.floor(lo[1]/size), math.floor(hi[1]/size)+1):
                    self.grid[x, y].append(index)

    def near(self, first, last, radius=0.):
        lo = [min(first[k], last[k])-radius for k in (0, 1)]
        hi = [max(first[k], last[k])+radius for k in (0, 1)]
        selected = set()
        for x in range(math.floor(lo[0]/self.size), math.floor(hi[0]/self.size)+1):
            for y in range(math.floor(lo[1]/self.size), math.floor(hi[1]/self.size)+1):
                selected.update(self.grid[x, y])
        return [self.faces[index] for index in selected]


def _support_interval(first, last, triangle):
    start, end = _barycentric(first, triangle), _barycentric(last, triangle)
    if start is None:
        return None
    lo, hi = 0., 1.
    for a, b in zip(start, end):
        delta = b-a
        if abs(delta) < 1e-14:
            if a < -1e-7:
                return None
        elif delta > 0.:
            lo = max(lo, (-1e-7-a)/delta)
        else:
            hi = min(hi, (-1e-7-a)/delta)
    if lo > hi or hi < 0. or lo > 1.:
        return None
    lo, hi = max(0., lo), min(1., hi)
    for fraction in (lo, hi):
        weights = [a+fraction*(b-a) for a, b in zip(start, end)]
        roof = sum(w*p[2] for w, p in zip(weights, triangle))
        route = first[2]+fraction*(last[2]-first[2])
        if abs(roof-route) > POSITION_EPS:
            return None
    return lo, hi


def covered(first, last, faces, underside=False, precision=None):
    selected = [face for face in faces
        if (face['downward'] and face['kind'] == 'body' if underside else face['upward'] and face['kind'] == 'pavement')
    ]
    intervals = sorted(value for face in selected
                       if (value := _support_interval(first, last, face['points'])) is not None)
    end, gaps = 0., []
    for lo, hi in intervals:
        if lo > end+1e-7:
            gaps.append((end, lo))
        end = max(end, hi)
    if end < 1.-1e-7:
        gaps.append((end, 1.))
    # A finite edge capsule proves a physical 3D distance bound. It does not
    # extrapolate a triangle or enlarge barycentric classification. Local
    # float32 vertices are bounded by 8.0011m horizontally and 17m vertically;
    # two rounded face boundaries can expose micrometre gaps at a true seam.
    for lo, hi in gaps:
        begin = np.array(first)+(np.array(last)-first)*lo
        finish = np.array(first)+(np.array(last)-first)*hi
        capsules = []
        for face in selected:
            triangle = np.array(face['points'])
            if np.any(triangle.max(axis=0) < np.minimum(begin, finish)-POSITION_EPS) or np.any(
                    triangle.min(axis=0) > np.maximum(begin, finish)+POSITION_EPS):
                continue
            normal = _normal(triangle)
            normal /= np.linalg.norm(normal)
            distance = max(abs(float((point-triangle[0])@normal)) for point in (begin, finish))
            if distance > POSITION_EPS:
                continue
            radius = math.sqrt(max(0., POSITION_EPS**2-distance**2))
            u = triangle[1]-triangle[0]
            u /= np.linalg.norm(u)
            v = np.cross(normal, u)
            def projected(point):
                offset = point-triangle[0]
                return float(offset@u), float(offset@v)
            a, b = projected(begin), projected(finish)
            vertices = [projected(point) for point in triangle]
            for p, q in zip(vertices, (*vertices[1:], vertices[0])):
                capsules.extend((lo+(hi-lo)*a0, lo+(hi-lo)*b0)
                                for a0, b0 in _edge_capsule_intervals(a, b, p, q, radius))
        reached = lo
        for start, stop in sorted(capsules):
            if start > reached+1e-12:
                break
            reached = max(reached, stop)
        if reached < hi-1e-12:
            return False
        if precision is not None:
            precision['admitted_spans'] += 1
            precision['maximum_admitted_span_m'] = max(precision['maximum_admitted_span_m'],
                                                      (hi-lo)*math.dist(first, last))
    return True


def _intrudes(first, last, face):
    dx, dy = last[0]-first[0], last[1]-first[1]
    length = math.hypot(dx, dy)
    polygon = []
    for point in face['points']:
        e, n = point[0]-first[0], point[1]-first[1]
        along = (e*dx+n*dy)/(length*length)
        polygon.append((along, (dx*n-dy*e)/length,
                        point[2]-first[2]-along*(last[2]-first[2])))
    # Paint and minute crossfall remain distinct from a solid obstacle.
    bottom = .03 if face['kind'] == 'pavement' else POSITION_EPS
    for axis, value, sign in ((0, 1e-8, 1), (0, 1.-1e-8, -1),
                              (1, -1.25+1e-5, 1), (1, 1.25-1e-5, -1),
                              (2, bottom, 1), (2, 3.8-1e-5, -1)):
        polygon = _clip(polygon, axis, value, sign)
        if not polygon:
            return False
    return True


def _width_covered(first, last, faces):
    dx, dy = last[0]-first[0], last[1]-first[1]
    length = math.hypot(dx, dy)
    normal = (-dy/length*1.25, dx/length*1.25)
    strip = Polygon([(p[0]+s*normal[0], p[1]+s*normal[1]) for p, s in ((first, 1), (last, 1), (last, -1), (first, -1))])
    roofs = []
    for face in faces:
        if face['kind'] != 'pavement' or not face['upward']:
            continue
        def height_error(p):
            along = ((p[0]-first[0])*dx+(p[1]-first[1])*dy)/(length*length)
            return abs(p[2]-first[2]-along*(last[2]-first[2]))
        if max(height_error(p) for p in face['points']) <= .03:
            roofs.append(Polygon([p[:2] for p in face['points']]))
    return bool(roofs) and strip.difference(unary_union(roofs)).area <= POSITION_EPS*strip.length*2.


def _saved_routes(resources, piece, *, path_contract=contract):
    origin, cells, tiles = path_contract._spec(piece)
    routes = []
    for cell, tile in zip(cells, tiles):
        world = cell[0]+origin[0], cell[1]+origin[1]
        for row in parse_paths(decompress(resources[*PATH, tile]))['routes']:
            routes.append({**row, 'points': [(p[0]+16.*world[0], p[1]-16.*world[1], p[2]) for p in row['points']]})
    return routes


def _corridor_segments(routes, floor_segments):
    for route in routes:
        for start, end in zip(route['points'], route['points'][1:]):
            if floor_segments is None:
                first, last = tuple((*p[:2], p[2]+datum(p[2])) for p in (start, end))
                yield start, end, first, last
            else:
                yield from floor_segments(start, end)


def check_corridors(faces, routes, *, full_width=False, floor_segments=None, allow_original_prefix=True,
                    underside_faces=None, obstacle_checker=None):
    index = FaceIndex(faces)
    underside_index = None if underside_faces is None else FaceIndex(underside_faces)
    checked = 0
    precision = {'proven_euclidean_distance_limit_m': POSITION_EPS, 'admitted_spans': 0,
                 'maximum_admitted_span_m': 0., 'method': 'Finite triangle-edge rectangles and endpoint discs in each actual face plane.'}
    borrowed_native_underside_length = 0.
    borrowed_native_prefixes = 0
    for start, end, first, last in _corridor_segments(routes, floor_segments):
            candidates = index.near(first, last, 1.25)
            require(covered(first, last, candidates, precision=precision),
                    f'Saved Y pavement does not continuously support a real car segment: {start}->{end}')
            authored_first, authored_last = first, last
            plane = -23.99899959564209
            if allow_original_prefix and min(first[0], last[0]) < plane-POSITION_EPS:
                exterior = first if first[0] < last[0] else last
                native_ends = [points[position] for points in contract._source()['routes'].values()
                               for position in (0, -1) if points[position][0] == -24.]
                require(any(math.dist(exterior, (*p[:2], p[2]+datum(p[2]))) <= POSITION_EPS for p in native_ends),
                        'An underside omission is not the exact original-native endpoint prefix')
                t = (plane-first[0])/(last[0]-first[0])
                require(0. < t < 1., 'Original-native model prefix exceeds its measured finite interface')
                contact = tuple(a+t*(b-a) for a, b in zip(first, last))
                if first[0] < last[0]:
                    authored_first = contact
                    length = math.dist(first, contact)
                else:
                    authored_last = contact
                    length = math.dist(contact, last)
                require(length <= .0015, 'Original-native borrowed prefix exceeds the pinned millimetre model phase')
                borrowed_native_underside_length += length
                borrowed_native_prefixes += 1
            below = [(*p[:2], p[2]-1.) for p in (authored_first, authored_last)]
            underside_candidates = candidates if underside_index is None else underside_index.near(*below, 1.25)
            require(covered(*below, underside_candidates, underside=True, precision=precision),
                    f'Saved Y deck has no complete one-metre underside below a car segment: {start}->{end}')
            if full_width:
                require(_width_covered(first, last, candidates), 'Saved Y pavement loses part of the complete 2.5m vehicle strip')
            for face in candidates:
                if obstacle_checker is None:
                    heights = [p[2] for p in face['points']]
                    if max(heights) <= min(first[2], last[2])+POSITION_EPS or min(heights) >= max(first[2], last[2])+3.8:
                        continue
                require(not (obstacle_checker or _intrudes)(first, last, face),
                        'Saved Y '+face['role']+' triangle enters the actual graded vehicle corridor: '
                        +str(first)+' -> '+str(last)+'; face='+str(face['points']))
            checked += 1
    return {'passed': True, 'actual_saved_car_segments': checked, 'continuous_spine_pavement_support': True,
            'continuous_authored_one_metre_underside_support': True, 'full_vehicle_strip_coverage': full_width,
            'original_native_endpoint_prefixes': borrowed_native_prefixes,
            'original_native_endpoint_prefix_total_length_m': borrowed_native_underside_length,
            'original_native_underside_scope': 'The unchanged native helper supplies the roof in its measured 1.415mm endpoint phase; its original open substructure is not claimed to be a newly closed authored underside.',
            'actual_face_vehicle_corridor_intersection_checked': True,
            'pavement_position_tolerance_m': POSITION_EPS, 'float32_support_bound': precision,
            'vehicle_width_m': 2.5, 'vehicle_height_m': 3.8}


def check_native_vehicle_clearance(faces, routes, *, floor_segments=None, obstacle_checker=None):
    """Authored overhangs and supports must also clear the real native approaches."""
    index = FaceIndex(faces)
    checked = 0
    for _start, _end, first, last in _corridor_segments(routes, floor_segments):
            for face in index.near(first, last, 1.25):
                require(not (obstacle_checker or _intrudes)(first, last, face),
                        'A saved Y physical face obstructs an unchanged native approach vehicle corridor')
            checked += 1
    return {'passed': True, 'native_real_car_segments_checked': checked,
            'native_capacity_routes_excluded': True, 'native_game_traffic_observed': False}


def _edge_key(point):
    # Local float32 coordinates are bounded by 8.0011m horizontally and native
    # elevations below 17m. A 2µm quantization step welds at most 3.465µm in 3D;
    # this affects the shell-topology check only, never coverage or intrusion.
    return tuple(round(value/2e-6) for value in point)


def _quadratic_interval(offset, delta, radius):
    a, b, c = float(delta@delta), float(2.*offset@delta), float(offset@offset-radius*radius)
    if a <= 1e-28:
        return (0., 1.) if c <= 0. else None
    discriminant = b*b-4.*a*c
    if discriminant < 0.:
        return None
    root = math.sqrt(max(0., discriminant))
    lo, hi = max(0., (-b-root)/(2.*a)), min(1., (-b+root)/(2.*a))
    return (lo, hi) if lo <= hi else None


def _native_edge_covered(first, last, segments):
    first, last = np.array(first), np.array(last)
    delta = last-first
    intervals = []
    for a, b in segments:
        a, b = np.array(a), np.array(b)
        axis = b-a
        length = float(np.linalg.norm(axis))
        axis /= length
        offset = first-a
        s, ds = float(offset@axis), float(delta@axis)
        perpendicular = _quadratic_interval(offset-s*axis, delta-ds*axis, POSITION_EPS)
        if perpendicular is not None:
            lo, hi = perpendicular
            if abs(ds) < 1e-18:
                if not 0. <= s <= length:
                    lo, hi = 1., 0.
            else:
                p, q = -s/ds, (length-s)/ds
                lo, hi = max(lo, min(p, q)), min(hi, max(p, q))
            if lo <= hi:
                intervals.append((lo, hi))
        for end in (a, b):
            if (interval := _quadratic_interval(first-end, delta, POSITION_EPS)) is not None:
                intervals.append(interval)
    reached = 0.
    for lo, hi in sorted(intervals):
        if lo > reached+1e-10:
            break
        reached = max(reached, hi)
    return reached >= 1.-1e-10


def native_open_profiles(donors, *, native_source=None):
    if native_source is None:
        from . import y_junction_native_models as native_source
    visible_native_end_sections = native_source.visible_native_end_sections
    segments = []
    for arm in ('A', 'B', 'C'):
        for deck in ('upper', 'lower'):
            for group in visible_native_end_sections(_context(donors), arm, deck):
                for row in group['segments']:
                    a, b = row['points']
                    segments.append(((a[0], -a[2], a[1]), (b[0], -b[2], b[1])))
    return segments


def check_shell(faces, *, kind, component=True, pavement_index=None, native_profiles=()):
    """Check oriented closed triangle edges, resolving collinear T junctions."""
    selected = [face for face in faces if (face['kind'] in ('body', 'pavement', 'barrier') if kind == 'road' else face['kind'] == kind)]
    edges = defaultdict(int)
    positions = {}
    members = defaultdict(set)
    for face in selected:
        for point in face['points']:
            key = _edge_key(point)
            positions.setdefault(key, point)
            members[key].add(tuple(point))
        for first, last in zip(face['points'], (*face['points'][1:], face['points'][0])):
            a, b = _edge_key(first), _edge_key(last)
            positions.setdefault(a, first)
            positions.setdefault(b, last)
            if a == b:
                continue
            key = (a, b) if a < b else (b, a)
            edges[key] += 1 if a < b else -1
    pending = [(a, b, count) for (a, b), count in edges.items() if count]
    maximum_displacement = max((math.dist(p, positions[key]) for key, points in members.items() for p in points), default=0.)
    # A quantization bin border can separate vertices less than one micrometre
    # apart. Cluster to an actual representative within the explicit 4µm
    # bound; never let a transitive chain enlarge that geometric allowance.
    if pending:
        representatives, bins, remap = {}, defaultdict(list), {}
        vertices = list({p for a, b, _n in pending for p in (a, b)})
        for vertex in vertices:
            point = positions[vertex]
            grid = tuple(math.floor(v/POSITION_EPS) for v in point)
            nearby = [candidate for shift in itertools.product((-1, 0, 1), repeat=3)
                      for candidate in bins[tuple(grid[k]+shift[k] for k in range(3))]
                      if all(math.dist(original, representatives[candidate]) <= POSITION_EPS
                             for original in members[vertex])]
            if nearby:
                target = min(nearby, key=lambda key: math.dist(point, representatives[key]))
            else:
                target = vertex
                representatives[target] = point
                bins[grid].append(target)
            remap[vertex] = target
            maximum_displacement = max(maximum_displacement,
                                       *(math.dist(p, representatives[target]) for p in members[vertex]))
        welded = defaultdict(int)
        for a, b, count in pending:
            a, b = remap[a], remap[b]
            if a != b:
                key = (a, b) if a < b else (b, a)
                welded[key] += count if a < b else -count
        pending = [(a, b, count) for (a, b), count in welded.items() if count]
    if pending:
        vertices = list({point for a, b, _n in pending for point in (a, b)})
        coordinates = np.array([positions[key] for key in vertices])
        split_edges = defaultdict(int)
        for a, b, count in pending:
            first, last = np.array(positions[a]), np.array(positions[b])
            direction = last-first
            length2 = float(direction@direction)
            lo, hi = np.minimum(first, last)-POSITION_EPS, np.maximum(first, last)+POSITION_EPS
            mask = np.all((coordinates >= lo) & (coordinates <= hi), axis=1)
            selected_indices = np.flatnonzero(mask)
            delta = coordinates[selected_indices]-first
            fraction = delta@direction/length2
            distance = np.linalg.norm(delta-fraction[:, None]*direction, axis=1)
            middle = [(float(t), vertices[int(i)]) for i, t, d in zip(selected_indices, fraction, distance)
                      if 1e-8 < t < 1.-1e-8 and d <= POSITION_EPS]
            cuts = [(0., a), *sorted(middle), (1., b)]
            for (_t, u), (_s, v) in zip(cuts, cuts[1:]):
                if u != v:
                    key = (u, v) if u < v else (v, u)
                    split_edges[key] += count if u < v else -count
        pending = [(a, b, n) for (a, b), n in split_edges.items() if n]
    allowed = 0
    for a, b, count in pending:
        first, last = positions[a], positions[b]
        native = bool(native_profiles) and _native_edge_covered(first, last, native_profiles)
        seam = component and any(max(abs(first[1]-plane), abs(last[1]-plane)) <= POSITION_EPS for plane in (-8., 8.))
        base = False
        if kind == 'barrier' and pavement_index is not None:
            base = covered(first, last, pavement_index.near(first, last))
        require(abs(count) == 1 and (native or seam or base),
                f'Saved Y {kind} shell has an open or reversed edge: {first}->{last}, count={count}')
        allowed += 1
    return {'passed': True, 'triangle_faces_checked': len(selected), 'declared_join_edges': allowed,
            'whole_assembly_shell': not component, 'topology_weld_maximum_distance_m': POSITION_EPS,
            'maximum_actual_source_vertex_displacement_m': maximum_displacement}


def _finite_edge_contact_region(region, first, second):
    """Prove a whole first-plane region lies near finite edges of both faces."""
    first, second = np.array(first), np.array(second)
    normal = _normal(first)
    normal /= np.linalg.norm(normal)
    u = first[1]-first[0]
    u /= np.linalg.norm(u)
    v = np.cross(normal, u)
    def projected(p):
        return float((p-first[0])@u), float((p-first[0])@v)
    polygon = Polygon([projected(np.array(p)) for p in region])
    for triangle in (first, second):
        masks = []
        for a, b in zip(triangle, (*triangle[1:], triangle[0])):
            phase = max(abs(float((p-first[0])@normal)) for p in (a, b))
            if phase >= POSITION_EPS:
                continue
            radius = math.sqrt(POSITION_EPS**2-phase**2)
            # GEOS uses inscribed circular chords. Coverage by this smaller
            # finite capsule proves the Euclidean bound without a false pass.
            masks.append(LineString([projected(a), projected(b)]).buffer(radius, quad_segs=32))
        if polygon.difference(unary_union(masks)).area > 1e-18:
            return False
    return True


def check_deck_overlaps(faces):
    roofs = [face for face in faces if face['kind'] == 'pavement' and face['upward']]
    polygons = [Polygon([p[:2] for p in face['points']]) for face in roofs]
    tree = STRtree(polygons)
    tested = 0
    for i, polygon in enumerate(polygons):
        for j in tree.query(polygon, predicate='intersects'):
            j = int(j)
            if j <= i:
                continue
            overlap = polygon.intersection(polygons[j])
            if overlap.area <= 1e-12:
                continue
            points = list(overlap.convex_hull.exterior.coords)[:-1]
            differences = []
            for p in points:
                heights = []
                for index in (i, j):
                    weights = _barycentric(p, roofs[index]['points'])
                    heights.append(sum(w*q[2] for w, q in zip(weights, roofs[index]['points'])))
                differences.append(heights[0]-heights[1])
            if min(differences) >= 1.-POSITION_EPS or max(differences) <= -1.+POSITION_EPS:
                continue
            rectangle = list(overlap.minimum_rotated_rectangle.exterior.coords)
            thin = min(math.dist(a, b) for a, b in zip(rectangle, rectangle[1:])) <= POSITION_EPS
            region = []
            for p in points:
                weights = _barycentric(p, roofs[i]['points'])
                region.append((*p, sum(w*q[2] for w, q in zip(weights, roofs[i]['points']))))
            require(thin and max(map(abs, differences)) <= POSITION_EPS
                    and _finite_edge_contact_region(region, roofs[i]['points'], roofs[j]['points']),
                    'Saved Y deck bodies overlap instead of meeting at an actual pavement union; '
                    f'roles={roofs[i]["role"]}/{roofs[j]["role"]}, area={overlap.area}, '
                    f'height_differences={min(differences), max(differences)}, bounds={overlap.bounds}')
            tested += 1
    return {'passed': True, 'roof_triangles_checked': len(roofs), 'bounded_float32_edge_contacts': tested,
            'float32_contact_width_limit_m': POSITION_EPS}


def _clip_linear_polygon(points, field, threshold=0.):
    """Clip finite 3D points against one affine half-space."""
    if not points:
        return []
    def value(p):
        return sum(field[k]*p[k] for k in range(3))+field[3]-threshold
    result = []
    previous, a = points[-1], value(points[-1])
    for current in points:
        b = value(current)
        if (a >= 0.) != (b >= 0.):
            fraction = a/(a-b)
            result.append(tuple(previous[k]+fraction*(current[k]-previous[k]) for k in range(len(previous))))
        if b >= 0.:
            result.append(tuple(current))
        previous, a = current, b
    return result


def check_underside_overlaps(faces):
    """Apply the same finite-face overlap proof to actual downward slabs."""
    floors = [{**face, 'kind': 'pavement', 'upward': True} for face in faces
              if face['kind'] == 'body' and face['downward']]
    report = check_deck_overlaps(floors)
    report['underside_triangles_checked'] = report.pop('roof_triangles_checked')
    return report


def _clip_xy_prism(points, polygon):
    coordinates = list(polygon.exterior.coords)[:-1]
    if sum(a[0]*b[1]-a[1]*b[0] for a, b in zip(coordinates, (*coordinates[1:], coordinates[0]))) < 0.:
        coordinates.reverse()
    for a, b in zip(coordinates, (*coordinates[1:], coordinates[0])):
        dx, dy = b[0]-a[0], b[1]-a[1]
        points = _clip_linear_polygon(points, (-dy, dx, 0., dy*a[0]-dx*a[1]))
        if not points:
            break
    return points


def check_barrier_deck_clearance(faces):
    """Clip rails in their own planes, including vertical positive-area faces."""
    roofs = [face for face in faces if face['kind'] == 'pavement' and face['upward']]
    floors = [face for face in faces if face['kind'] == 'body' and face['downward']]
    roof_polygons = [Polygon([p[:2] for p in face['points']]) for face in roofs]
    floor_polygons = [Polygon([p[:2] for p in face['points']]) for face in floors]
    def coefficients(face):
        return tuple(np.linalg.solve(np.array([[p[0], p[1], 1.] for p in face['points']]),
                                     np.array([p[2] for p in face['points']])))
    roof_fields = [coefficients(face) for face in roofs]
    floor_fields = [coefficients(face) for face in floors]
    roof_tree, floor_tree = STRtree(roof_polygons), STRtree(floor_polygons)
    bounded_floor_polygons = {}
    checked = vertical = 0
    for barrier in (face for face in faces if face['kind'] == 'barrier'):
        points = np.asarray(barrier['points'])
        normal = _normal(points)
        normal /= np.linalg.norm(normal)
        u = points[1]-points[0]
        u /= np.linalg.norm(u)
        v = np.cross(normal, u)
        def own_plane(polygon):
            if len(polygon) < 3:
                return Polygon()
            return Polygon([(float((np.asarray(p)-points[0])@u), float((np.asarray(p)-points[0])@v)) for p in polygon])
        projection = Polygon(points[:, :2])
        if projection.area <= 1e-12:
            vertical += 1
        west, south, east, north = projection.bounds
        for i in roof_tree.query(box(west, south, east, north)):
            i = int(i)
            if barrier.get('native_reference') and roofs[i].get('native_reference'):
                continue
            patch = _clip_xy_prism(list(map(tuple, points)), roof_polygons[i])
            overlap = own_plane(patch)
            if overlap.area <= 1e-12:
                continue
            rx, ry, rc = roof_fields[i]
            roof_above = (rx, ry, -1., rc)
            below = _clip_linear_polygon(patch, roof_above, POSITION_EPS)
            if own_plane(below).area <= 1e-12:
                checked += 1
                continue
            differences = [rx*p[0]+ry*p[1]+rc-p[2] for p in patch]
            # A genuine finite surface crossing cannot be hidden by the
            # absence of an underside in an unchanged native open frame.
            crosses_roof = min(differences) < -POSITION_EPS and max(differences) > POSITION_EPS
            lower_parts, higher_parts = [], []
            query = box(west-POSITION_EPS, south-POSITION_EPS, east+POSITION_EPS, north+POSITION_EPS)
            for j in floor_tree.query(query):
                j = int(j)
                fx, fy, fc = floor_fields[j]
                if j not in bounded_floor_polygons:
                    # Every admitted point remains within 4 micrometres of
                    # the actual finite triangle in its own sloped plane.
                    radius = POSITION_EPS/math.sqrt(1.+fx*fx+fy*fy)
                    bounded_floor_polygons[j] = floor_polygons[j].buffer(radius, quad_segs=8)
                fragment = _clip_xy_prism(below, bounded_floor_polygons[j])
                if not fragment:
                    continue
                lower = own_plane(_clip_linear_polygon(fragment, (-fx, -fy, 1., -fc), POSITION_EPS))
                higher = _clip_linear_polygon(fragment, (fx, fy, -1., fc), POSITION_EPS)
                higher = own_plane(_clip_linear_polygon(higher, (rx-fx, ry-fy, 0., rc-fc), POSITION_EPS))
                if lower.area > 1e-12:
                    lower_parts.append(lower)
                if higher.area > 1e-12:
                    higher_parts.append(higher)
            inside = unary_union(lower_parts).difference(unary_union(higher_parts))
            require(not crosses_roof and inside.area <= 1e-12,
                    'A saved Y barrier surface enters an actual road slab: '
                    f'roles={barrier["role"]}/{roofs[i]["role"]}, area={overlap.area}, '
                    f'roof_minus_barrier_m={min(differences), max(differences)}, '
                    f'actual_rail_plane_inside_area_m2={inside.area}, '
                    f'barrier={barrier["points"]}, roof={roofs[i]["points"]}')
            checked += 1
    return {'passed': True, 'actual_barrier_to_slab_overlaps_checked': checked,
            'vertical_barrier_triangles_checked': vertical,
            'contact_position_bound_m': POSITION_EPS, 'actual_saved_roof_and_underside_planes': True,
            'finite_underside_encoding_distance_bound_m': POSITION_EPS,
            'nominal_depth_substituted_for_saved_faces': False}


def check_barrier_intersections(faces):
    """Inspect finite saved rail triangles, including outside the car lanes."""
    rails = [face for face in faces if face['kind'] == 'barrier']
    arrays = [np.array(face['points']) for face in rails]
    normals = [_normal(p)/np.linalg.norm(_normal(p)) for p in arrays]
    bounds = [(p.min(axis=0), p.max(axis=0)) for p in arrays]
    tree = STRtree([box(lo[0], lo[1], hi[0], hi[1]) for lo, hi in bounds])
    candidates = seams = contacts = 0
    for i, (first, n1, (lo1, hi1)) in enumerate(zip(arrays, normals, bounds)):
        for j in tree.query(box(lo1[0]-POSITION_EPS, lo1[1]-POSITION_EPS,
                                hi1[0]+POSITION_EPS, hi1[1]+POSITION_EPS)):
            j = int(j)
            if j <= i:
                continue
            if rails[i].get('native_reference') and rails[j].get('native_reference'):
                continue
            second, n2 = arrays[j], normals[j]
            lo2, hi2 = bounds[j]
            if hi1[2] < lo2[2]-POSITION_EPS or hi2[2] < lo1[2]-POSITION_EPS:
                continue
            da, db = (first-second[0])@n2, (second-first[0])@n1
            if min(da) > POSITION_EPS or max(da) < -POSITION_EPS or min(db) > POSITION_EPS or max(db) < -POSITION_EPS:
                continue
            candidates += 1
            cross = np.cross(n1, n2)
            square = float(cross@cross)
            if square <= 1e-14:
                if max(abs(da)) > POSITION_EPS or max(abs(db)) > POSITION_EPS:
                    continue
                u = first[1]-first[0]
                u /= np.linalg.norm(u)
                v = np.cross(n1, u)
                def projected(points):
                    return Polygon([(float((p-first[0])@u), float((p-first[0])@v)) for p in points])
                overlap = projected(first).intersection(projected(second))
                if overlap.area <= 1e-12:
                    continue
                rectangle = list(overlap.minimum_rotated_rectangle.exterior.coords)
                width = min(math.dist(a, b) for a, b in zip(rectangle, rectangle[1:]))
                region = [first[0]+p[0]*u+p[1]*v for p in list(overlap.convex_hull.exterior.coords)[:-1]]
                require(width <= POSITION_EPS and _finite_edge_contact_region(region, first, second),
                        'Saved Y barrier faces duplicate a finite coplanar area: '
                        f'roles={rails[i]["role"]}/{rails[j]["role"]}, area={overlap.area}, '
                        f'first={rails[i]["points"]}, second={rails[j]["points"]}')
                contacts += 1
                continue
            direction = cross/math.sqrt(square)
            origin = (float(n1@first[0])*np.cross(n2, cross)+float(n2@second[0])*np.cross(cross, n1))/square
            def section(points, distances):
                # Physical 4 µm uncertainty belongs to the finite contact
                # capsules, not this exact plane section: dividing that
                # uncertainty by a shallow plane angle invents long segments
                # outside the actual finite triangle.
                values = [float(point@direction) for point, distance in zip(points, distances) if abs(distance) <= 1e-12]
                for k in range(3):
                    a, b = distances[k], distances[(k+1)%3]
                    if a*b < 0.:
                        point = points[k]+a/(a-b)*(points[(k+1)%3]-points[k])
                        values.append(float(point@direction))
                return (min(values), max(values)) if values else None
            sa, sb = section(first, da), section(second, db)
            if sa is None or sb is None:
                continue
            low, high = max(sa[0], sb[0]), min(sa[1], sb[1])
            if high-low <= POSITION_EPS:
                continue
            # direction@origin is zero analytically; retaining the finite
            # projection avoids assuming that floating-point identity.
            begin = origin+(low-float(origin@direction))*direction
            end = origin+(high-float(origin@direction))*direction
            edges_a = [(first[k], first[(k+1)%3]) for k in range(3)]
            edges_b = [(second[k], second[(k+1)%3]) for k in range(3)]
            require(_native_edge_covered(begin, end, edges_a) and _native_edge_covered(begin, end, edges_b),
                    'Saved Y barrier faces cross through a finite triangle interior: '
                    f'roles={rails[i]["role"]}/{rails[j]["role"]}, intersection={tuple(begin)}->{tuple(end)}, '
                    f'first={rails[i]["points"]}, second={rails[j]["points"]}')
            seams += 1
    return {'passed': True, 'barrier_triangles_checked': len(rails), 'finite_candidate_pairs_checked': candidates,
            'shared_finite_edge_seams': seams, 'bounded_float32_coplanar_contacts': contacts,
            'position_bound_m': POSITION_EPS, 'coplanar_contact_width_bound_m': POSITION_EPS}


def _support_records(*, path_contract=contract):
    from scp import jsonc
    value = jsonc.load(path_contract.SUBJECT/'checks/support-solids.jsonc')
    require(value.get('source_design_sha256') == hashlib.sha256(
        (path_contract.SUBJECT/'evidence/design-geometry.jsonc').read_bytes()).hexdigest(),
        'Y support-solid source is stale relative to the independently reviewed routes')
    records = value['supports']
    require(records and len({r['id'] for r in records}) == len(records), 'Y support source has empty or duplicate solids')
    return records


def _prism_planes(record, owned=None):
    corners = record['corners_en_m']
    bottom, top = record['bottom_m'], record['top_m']
    require(len(corners) == 4 and 0. <= bottom < top, 'Invalid Y support prism bounds')
    footprint = Polygon(corners)
    require(footprint.is_valid and footprint.area > 0., 'Y support footprint is invalid')
    region = footprint if owned is None else footprint.intersection(owned)
    planes = [({'kind': 'horizontal', 'height': bottom, 'normal': (0., 0., -1.)}, region),
              ({'kind': 'horizontal', 'height': top, 'normal': (0., 0., 1.)}, region)]
    clockwise = sum(a[0]*b[1]-a[1]*b[0] for a, b in zip(corners, (*corners[1:], corners[0]))) < 0.
    for a, b in zip(corners, (*corners[1:], corners[0])):
        delta = np.subtract(b, a)
        length = float(np.linalg.norm(delta))
        direction = delta/length
        normal = np.array([direction[1], -direction[0], 0.])*(-1. if clockwise else 1.)
        edge = LineString([a, b])
        clipped = edge if owned is None else edge.intersection(owned)
        parts = [clipped] if clipped.geom_type == 'LineString' else [
            part for part in getattr(clipped, 'geoms', ()) if part.geom_type == 'LineString']
        patches = []
        for line in parts:
            if line.length <= 1e-10:
                continue
            distances = [float(np.subtract(p, a)@direction) for p in line.coords]
            patches.append(box(min(distances), bottom, max(distances), top))
        planes.append(({'kind': 'vertical', 'a': np.array(a), 'direction': direction,
                        'normal': normal}, unary_union(patches)))
    return footprint, planes


def _plane_polygon(face, plane):
    points = np.array(face['points'])
    if plane['kind'] == 'horizontal':
        if max(abs(p[2]-plane['height']) for p in points) > POSITION_EPS:
            return None
        projected = Polygon(points[:, :2])
    else:
        normal = plane['normal'][:2]
        if max(abs(float((p[:2]-plane['a'])@normal)) for p in points) > POSITION_EPS:
            return None
        projected = Polygon([(float((p[:2]-plane['a'])@plane['direction']), p[2]) for p in points])
    if projected.area <= 1e-12:
        return None
    require(float(_normal(points)@plane['normal']) > 0., 'Saved Y support prism reverses a complete solid surface')
    return projected


def _cap_overlap_embedding(record, station, reference_floor, index):
    footprint = Polygon(record['corners_en_m'])
    west, south, east, north = footprint.bounds
    surfaces = []
    polygons = []
    patches = []
    for face in index.near((west, south, 0.), (east, north, 0.)):
        if face['kind'] != 'body' or not face['downward']:
            continue
        polygon = Polygon([q[:2] for q in face['points']])
        patch = polygon.intersection(footprint)
        if patch.area > 1e-12:
            surfaces.append(face)
            polygons.append(polygon)
            patches.append(patch)
    def height(i, point):
        weights = _barycentric(point, surfaces[i]['points'])
        return sum(w*p[2] for w, p in zip(weights, surfaces[i]['points']))
    selected = {i for i, polygon in enumerate(polygons)
                if polygon.buffer(POSITION_EPS).covers(Point(station[:2]))
                and abs(height(i, station)-reference_floor) <= POSITION_EPS}
    require(selected, 'A Y support cap has no finite served underside component')
    tree = STRtree(polygons)
    pending = list(selected)
    while pending:
        current = pending.pop()
        for other in tree.query(polygons[current].buffer(POSITION_EPS)):
            other = int(other)
            if other in selected:
                continue
            a, b = nearest_points(polygons[current], polygons[other])
            first = (*a.coords[0], height(current, a.coords[0]))
            last = (*b.coords[0], height(other, b.coords[0]))
            if math.dist(first, last) <= POSITION_EPS:
                selected.add(other)
                pending.append(other)
    embeds = [record['top_m']-height(i, point) for i in selected
              for point in list(patches[i].convex_hull.exterior.coords)[:-1]]
    require(max(embeds) <= .3+POSITION_EPS,
            'A saved Y support cap exceeds its bounded embed over the actual served-slab footprint')
    return {'actual_served_underside_triangles': len(selected),
            'minimum_cap_top_minus_served_underside_m': min(embeds),
            'maximum_cap_top_minus_served_underside_m': max(embeds),
            'served_surface_connectivity_bound_m': POSITION_EPS}


def _support_contact(record, faces, index, *, path_contract=contract, use_attachment=False):
    match = SUPPORT.fullmatch(record['id'])
    require(match is not None, 'Unknown expected Y support role')
    route_name, station, _side, kind = match.groups()
    if kind == 'pier':
        return None
    if use_attachment:
        attachment = record.get('attachment', {})
        require(attachment.get('source_route') in path_contract.NAMES
                and type(attachment.get('station_m')) in (int, float)
                and math.isfinite(attachment['station_m']),
                'Reversed support contact needs an explicit finite directed attachment')
        route_name, station = attachment['source_route'], attachment['station_m']
    points = np.asarray(path_contract._source()['routes'][route_name])
    stations = np.r_[0., np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1).cumsum()]
    p = points[int(np.argmin(np.abs(stations-float(station))))].copy()
    if kind == 'lower-cap':
        p[2] = 7.5
    reference = p[2]+datum(p[2])-1.
    require(Polygon(record['corners_en_m']).buffer(POSITION_EPS).covers(Point(p[:2])),
            'Saved Y support cap does not reach the declared served road station')
    floors = []
    for face in index.near(p, p, .01):
        if face['kind'] != 'body' or not face['downward']:
            continue
        polygon = Polygon([q[:2] for q in face['points']])
        if polygon.buffer(POSITION_EPS).covers(Point(p[:2])):
            weights = _barycentric(p, face['points'])
            floors.append(sum(w*q[2] for w, q in zip(weights, face['points'])))
    require(floors and min(abs(h-reference) for h in floors) <= POSITION_EPS,
            'Saved Y support cap has no actual served slab at its declared station')
    floor = min(floors, key=lambda h: abs(h-reference))
    embed = record['top_m']-floor
    require(-POSITION_EPS <= embed <= .3+POSITION_EPS and record['bottom_m'] <= floor,
            'Saved Y support cap floats below its slab or exceeds the bounded intentional body embed')
    require(record['top_m'] < floor+1.-POSITION_EPS, 'Saved Y support cap enters the actual asphalt plane')
    return {'id': record['id'], 'actual_slab_contact_height_m': floor,
            'intentional_contact_station_embed_m': embed, 'full_top_bearing_claimed': False,
            'whole_served_slab_overlap': _cap_overlap_embedding(record, p, floor, index)}


def _vehicle_strip(first, last):
    dx, dy = last[0]-first[0], last[1]-first[1]
    length = math.hypot(dx, dy)
    normal = np.array([-dy/length, dx/length])*1.25
    return Polygon([np.asarray(p[:2])+side*normal for p, side in ((first, 1), (last, 1), (last, -1), (first, -1))])


def check_support_frames(records, *, require_plan=True):
    """Verify connected declared prisms after their actual saved faces match."""
    frames = defaultdict(dict)
    for record in records:
        match = SUPPORT.fullmatch(record['id'])
        require(match is not None, 'Unknown Y frame role')
        route, station, side, kind = match.groups()
        require(kind not in frames[route, int(station), int(side)], 'Duplicate Y frame solid')
        frames[route, int(station), int(side)][kind] = record
    contacts = []
    for (route, station, side), members in frames.items():
        expected = {'pier', 'cap', 'lower-cap'} if route in ('A-B', 'A-C') else {'pier', 'cap'}
        require(set(members) == expected, 'A Y support frame omits its pier or a served-deck cap')
        pier, cap = members['pier'], members['cap']
        require(abs(pier['bottom_m']) <= POSITION_EPS, 'A Y support pier does not reach the ground datum')
        require(abs(pier['top_m']-cap['bottom_m']) <= POSITION_EPS,
                'A Y support cap floats above, or intersects beyond, its declared pier contact')
        footprint = Polygon(pier['corners_en_m'])
        area = footprint.intersection(Polygon(cap['corners_en_m'])).area
        require(area > 1e-10, 'A Y support upper cap misses its ground-reaching pier')
        if 'lower-cap' in members:
            lower = members['lower-cap']
            require(footprint.intersection(Polygon(lower['corners_en_m'])).area > 1e-10
                    and min(pier['top_m'], lower['top_m'])-max(pier['bottom_m'], lower['bottom_m']) > POSITION_EPS,
                    'A Y shared lower cap misses its ground-reaching pier')
        contacts.append({'route': route, 'station_m': station, 'side': side,
                         'upper_cap_to_pier_contact_area_m2': area})
    stations = {(route, station) for route, station, _side in frames}
    if require_plan:
        planned = {(route, station) for route, values in (
            ('A-B', (16, 36, 56)), ('A-C', (16, 36, 56, 76)),
            ('B-C', (16, 36, 56, 76)), ('C-B', (16, 36, 56, 76))) for station in values}
        require(stations == planned, 'Y supports do not retain a connected frame at every fixed planned station')
    return {'passed': True, 'connected_ground_frames': len(frames), 'planned_stations_with_a_frame': len(stations),
            'actual_prism_connections': contacts, 'structural_capacity_tested': False}


def check_support_solids(faces, routes, *, owned_cells=None, whole=False, path_contract=contract, use_attachment=False):
    records = _support_records(path_contract=path_contract)
    owned = None if owned_cells is None else unary_union([
        box(16.*c-8., -16.*r-8., 16.*c+8., -16.*r+8.) for c, r in owned_cells])
    groups = defaultdict(list)
    for face in faces:
        if face['kind'] == 'support':
            groups[face['role']].append(face)
    expected = {r['id']: r for r in records if owned is None or Polygon(r['corners_en_m']).intersection(owned).area > 1e-10}
    require(set(groups) == set(expected), 'Saved Y support solids omit, add, or rename a declared complete prism')
    footprints = []
    for identifier, record in expected.items():
        footprint, planes = _prism_planes(record, owned)
        footprints.append(footprint)
        actual = [[] for _ in planes]
        for face in groups[identifier]:
            matches = [(i, polygon) for i, (plane, _surface) in enumerate(planes)
                       if (polygon := _plane_polygon(face, plane)) is not None]
            require(len(matches) == 1, 'Saved Y support face is not on its declared closed prism')
            actual[matches[0][0]].append(matches[0][1])
        for (_plane, surface), pieces in zip(planes, actual):
            union = unary_union(pieces)
            require(surface.difference(union.buffer(POSITION_EPS)).area <= 1e-10
                    and union.difference(surface.buffer(POSITION_EPS)).area <= 1e-10,
                    'Saved Y support prism loses or adds part of a complete surface')
    # Closed prism containment is checked directly as well as by triangle-face
    # intrusion: a vehicle completely inside a bad solid cannot evade this.
    identifiers = list(expected)
    tree = STRtree(footprints)
    roofs = [face for face in faces if face['kind'] == 'pavement' and face['upward']]
    roof_polygons = [Polygon([p[:2] for p in face['points']]) for face in roofs]
    roof_index = STRtree(roof_polygons)
    asphalt_checks = 0
    for footprint, identifier in zip(footprints, identifiers):
        record = expected[identifier]
        for i in roof_index.query(footprint, predicate='intersects'):
            i = int(i)
            overlap = footprint.intersection(roof_polygons[i])
            if overlap.area <= 1e-12:
                continue
            heights = []
            for point in list(overlap.convex_hull.exterior.coords)[:-1]:
                weights = _barycentric(point, roofs[i]['points'])
                heights.append(sum(w*p[2] for w, p in zip(weights, roofs[i]['points'])))
            require(record['top_m'] <= min(heights)+POSITION_EPS
                    or record['bottom_m'] >= max(heights)-POSITION_EPS,
                    'Saved Y support solid pierces an actual pavement surface: '+identifier)
            asphalt_checks += 1
    checked = 0
    for route in routes:
        for first, last in zip(route['points'], route['points'][1:]):
            strip = _vehicle_strip(first, last)
            dx, dy = last[0]-first[0], last[1]-first[1]
            square = dx*dx+dy*dy
            for i in tree.query(strip, predicate='intersects'):
                i = int(i)
                overlap = strip.intersection(footprints[i])
                if overlap.area <= 1e-12:
                    continue
                record = expected[identifiers[i]]
                points = list(overlap.convex_hull.exterior.coords)[:-1]
                heights = []
                for p in points:
                    t = ((p[0]-first[0])*dx+(p[1]-first[1])*dy)/square
                    height = first[2]+t*(last[2]-first[2])
                    heights.append(height+datum(height))
                require(record['top_m'] <= min(heights)+POSITION_EPS
                        or record['bottom_m'] >= max(heights)+3.8-POSITION_EPS,
                        'A complete saved Y support solid contains part of the actual vehicle corridor')
                checked += 1
    contacts = []
    if whole:
        index = FaceIndex(faces)
        contacts = [value for record in records if (value := _support_contact(
            record, faces, index, path_contract=path_contract, use_attachment=use_attachment)) is not None]
    return {'passed': True, 'closed_prisms_checked': len(expected), 'complete_surface_coverage_checked': True,
            'closed_solid_vehicle_intersections_checked': checked, 'whole_assembly_slab_contacts': contacts,
            'whole_assembly_connected_frames': check_support_frames(records) if whole else None,
            'actual_asphalt_surface_intersections_checked': asphalt_checks,
            'full_top_bearing_claimed': False, 'structural_capacity_tested': False}


def _native_seams(faces, donors, arms, *, native_source=None, owned_cells=None):
    if native_source is None:
        from . import y_junction_native_models as native_source
    native_join_audit = native_source.native_join_audit
    roles = list(dict.fromkeys(face['role'] for face in faces))
    materials = {face['role']: face['material'] for face in faces}
    triangles = [tuple((p[0], p[2], -p[1], *uv, float(roles.index(face['role'])))
                       for p, uv in zip(face['points'], face['uv'])) for face in faces]
    return native_join_audit(triangles, roles, materials, _context(donors), arms=arms,
                             **({} if owned_cells is None else {'owned_cells': owned_cells}))


def external_skin(faces, donors):
    """Apply two source-certified native scopes only to hull analysis.

    Original native collars retain a pavement face beneath their original
    barrier. Native-source verification proves that inherited geometry before
    its buried footprint is removed from the analysis skin. The literal C
    source's finite outside-only 1 mm roof/skirt fringe retains its original
    open underside. Authored geometry must close inside the C owner bounds.
    Candidate DATs, previews, floor support, vehicle tests, interference tests,
    and texture checks retain every actual saved face.
    """
    from .y_junction_native_models import certify_native_collars
    roles = list(dict.fromkeys(face['role'] for face in faces))
    materials = {face['role']: face['material'] for face in faces}
    triangles = [tuple((p[0], p[2], -p[1], *uv, float(roles.index(face['role'])))
                       for p, uv in zip(face['points'], face['uv'])) for face in faces]
    certificate = certify_native_collars(triangles, roles, materials, _context(donors))
    masks = certificate['internal_pavement_masks']
    certified = set(certificate['certified_face_indices'])
    peer_rows = certificate.get('buried_peer_body_regions', [])
    peer_regions = {row['face_index']: row for row in peer_rows}
    require(len(peer_regions) == len(peer_rows), 'Duplicate certified peer-body analysis region')
    # The pinned original core300 source extends 1 mm east and north of its
    # city cell. Only those literal inherited roof/skirt portions retain the
    # original open underside; newly authored geometry must close inside the
    # owner bounds. Raw saved faces remain in every other physical check.
    initial = []
    inherited_area = inherited_roof_area = 0.
    inherited_points = []
    inherited_faces = 0
    peer_area = 0.
    peer_points = []
    peer_faces = 0
    def area(vertices):
        return sum(float(np.linalg.norm(_normal([vertices[0][:3], vertices[k][:3], vertices[k+1][:3]])))/2.
                   for k in range(1, len(vertices)-1))
    for index, face in enumerate(faces):
        if index in peer_regions:
            row = peer_regions[index]
            matched = re.fullmatch(r'body-native-([AB])-(upper|lower)-peer', face['role'])
            require(matched is not None and index in certified and row['role'] == face['role'],
                    'Buried peer-body scope requires the exact certified original face')
            nominal = 15. if matched[2] == 'upper' else 7.5
            require(row['analysis_below_height_m'] == nominal
                    and abs(row['underside_height_m']-(nominal+datum(nominal)-1.)) <= POSITION_EPS
                    and row['source_model_sha256'] in certificate['source_model_sha256']
                    and row['source_extrusion_length_m'] == 3.
                    and row['finite_source_footprint_and_height_containment_proved'] is True
                    and row['requires_independent_complete_shell_and_outer_wall_proof'] is True,
                    'Buried peer-body scope escapes its finite source floor/underside prism')
            vertices = [(*p, *uv) for p, uv in zip(face['points'], face['uv'])]
            kept = _clip_linear_polygon(vertices, (0., 0., 1., -nominal))
            hidden = _clip_linear_polygon(vertices, (0., 0., -1., nominal))
            removed_area = max(0., area(vertices)-area(kept))
            require(abs(removed_area-row['source_body_surface_area_below_floor_m2']) <= 1e-8,
                    'Peer-body skin trim differs from the independently certified finite region')
            peer_faces += 1
            peer_area += removed_area
            peer_points.extend(p[:3] for p in hidden)
            for k in range(1, len(kept)-1):
                triangle = [kept[0], kept[k], kept[k+1]]
                if np.linalg.norm(_normal([p[:3] for p in triangle])) >= 1e-13:
                    initial.append((index, {**face, 'points': tuple(p[:3] for p in triangle),
                                            'uv': tuple(p[3:] for p in triangle)}))
            continue
        literal_c = re.fullmatch(r'(pavement|body|barrier)-native-C-(upper|lower)-(retained-core-collar|retained-contact)', face['role'])
        if not literal_c:
            initial.append((index, face))
            continue
        require(index in certified and face['owner_cell'] == (3, 0),
                'C inherited-overhang scope requires the pinned original face in its exact owner')
        require('3d94bcce2ff84c9bd06d3bbbc7a089b8eaa28cfe921c3d31e87a27300cffd3dd' in certificate['source_model_sha256'],
                'C inherited-overhang scope lacks the pinned original core300 model signature')
        vertices = [(*p, *uv) for p, uv in zip(face['points'], face['uv'])]
        east_inside = _clip_linear_polygon(vertices, (-1., 0., 0., 56.))
        inside = _clip_linear_polygon(east_inside, (0., -1., 0., 8.))
        difference = max(0., area(vertices)-area(inside))
        if difference > 1e-14:
            inherited_faces += 1
            inherited_area += difference
            outside = []
            if max(p[0] for p in vertices) > 56.+1e-12:
                outside.append(_clip_linear_polygon(vertices, (1., 0., 0., -56.)))
            if east_inside and max(p[1] for p in east_inside) > 8.+1e-12:
                outside.append(_clip_linear_polygon(east_inside, (0., 1., 0., -8.)))
            inherited_points.extend(p[:3] for part in outside for p in part)
            if face['kind'] == 'pavement' and face['upward']:
                inherited_roof_area += sum(Polygon([p[:2] for p in part]).area for part in outside if len(part) >= 3)
        for k in range(1, len(inside)-1):
            triangle = [inside[0], inside[k], inside[k+1]]
            if np.linalg.norm(_normal([p[:3] for p in triangle])) < 1e-13:
                continue
            initial.append((index, {**face, 'points': tuple(p[:3] for p in triangle),
                                    'uv': tuple(p[3:] for p in triangle)}))
    result, removed = [], 0.
    for index, face in initial:
        mask = masks.get(face['role'])
        if mask is None or face['kind'] != 'pavement' or not face['upward']:
            result.append(face)
            continue
        require(index in certified, 'An unverified native-textured roof cannot receive a shell exception')
        polygon = Polygon([p[:2] for p in face['points']])
        exterior = polygon.difference(mask)
        removed += polygon.area-exterior.area
        parts = [exterior] if exterior.geom_type == 'Polygon' else [
            p for p in getattr(exterior, 'geoms', ()) if p.geom_type == 'Polygon']
        for part in parts:
            if part.area <= 1e-14:
                continue
            for triangle in shapely.constrained_delaunay_triangles(part).geoms:
                points, uvs = [], []
                for p in list(triangle.exterior.coords)[:3]:
                    weights = _barycentric(p, face['points'])
                    points.append((p[0], p[1], sum(w*q[2] for w, q in zip(weights, face['points']))))
                    uvs.append(tuple(sum(w*q[k] for w, q in zip(weights, face['uv'])) for k in (0, 1)))
                if _normal(points)[2] < 0.:
                    points[1], points[2] = points[2], points[1]
                    uvs[1], uvs[2] = uvs[2], uvs[1]
                result.append({**face, 'points': tuple(points), 'uv': tuple(uvs)})
    summary = {key: value for key, value in certificate.items()
               if key not in ('internal_pavement_masks', 'barrier_base_masks', 'certified_face_indices',
                              'generic_native_texture_face_indices_without_geometry_exception')}
    summary.update({'certified_faces': len(certified), 'removed_inherited_interior_roof_area_m2': removed,
                    'internal_roof_masks': len(masks), 'actual_saved_faces_changed': False,
                    'finite_original_peer_body_skin_scope': {
                        'source_faces_trimmed': peer_faces,
                        'removed_original_surface_area_m2': peer_area,
                        'removed_original_bounds_enh_m': None if not peer_points else [
                            [min(p[k] for p in peer_points) for k in range(3)],
                            [max(p[k] for p in peer_points) for k in range(3)]],
                        'raised_original_body_above_nominal_roof_preserved': True,
                        'requires_independent_complete_shell_and_outer_wall_proof': True,
                        'new_authored_faces_exempted': 0,
                        'actual_saved_faces_changed': False},
                    'finite_original_c_overhang_skin_scope': {
                        'source_model_sha256': '3d94bcce2ff84c9bd06d3bbbc7a089b8eaa28cfe921c3d31e87a27300cffd3dd',
                        'analysis_inside_east_max_m': 56., 'analysis_inside_north_max_m': 8.,
                        'source_faces_with_removed_portions': inherited_faces,
                        'removed_original_surface_area_m2': inherited_area,
                        'removed_original_upward_roof_plan_area_m2': inherited_roof_area,
                        'removed_original_bounds_enh_m': None if not inherited_points else [
                            [min(p[k] for p in inherited_points) for k in range(3)],
                            [max(p[k] for p in inherited_points) for k in range(3)]],
                        'new_authored_faces_exempted': 0,
                        'actual_dat_underside_corridor_and_interference_faces_changed': False},
                    'generic_native_textured_faces_without_geometry_exception': len(certificate.get(
                        'generic_native_texture_face_indices_without_geometry_exception', []))})
    return result, summary


def gather(resources, piece, *, path_contract=contract, variant='original', native_cell_bounds=None):
    origin, cells, tiles = path_contract._spec(piece)
    faces = []
    for cell, tile in zip(cells, tiles):
        require(all((*S3D, tile+zoom) in resources for zoom in range(5)), 'Y model lacks one of its five zooms')
        raw = decompress(resources[*S3D, tile])
        require(all(decompress(resources[*S3D, tile+zoom]) == raw for zoom in range(5)),
                'Y saved zoom changes its complete physical model')
        faces.extend(decode_faces(raw, (cell[0]+origin[0], cell[1]+origin[1]),
                                  variant=variant, native_cell_bounds=native_cell_bounds))
    from .modular_partition_verify import check_preview
    check_preview(resources, piece)
    return faces


def check_models(resources, piece, donors=None):
    contract.check_paths(resources, piece)
    faces = gather(resources, piece)
    references = native_faces(donors)
    corridors = check_corridors([*faces, *references], _saved_routes(resources, piece))
    native_corridors = check_native_vehicle_clearance(faces, native_traffic(donors))
    pavement = FaceIndex([*faces, *references])
    skin, native_certificate = external_skin(faces, donors)
    road = check_shell(skin, kind='road', pavement_index=pavement, native_profiles=native_open_profiles(donors))
    barriers = {'integral_raised_road_shell': True, 'actual_barrier_triangles': sum(f['kind'] == 'barrier' for f in faces)}
    supports = check_shell(faces, kind='support', pavement_index=pavement)
    origin = piece['engineering']['world_origin_cell']
    solid_supports = check_support_solids([*faces, *references], [*_saved_routes(resources, piece), *native_traffic(donors)], owned_cells=[
        (c[0]+origin[0], c[1]+origin[1]) for c in piece['cells']])
    arm = {contract.KEYS[0]: 'A', contract.KEYS[1]: 'B', contract.KEYS[2]: 'C'}[contract._key(piece)]
    seams = _native_seams(faces, donors, (arm,))
    from .y_junction_approaches import check_native_boundary_paths
    native = check_native_boundary_paths(donors, piece, resources)
    from .shadow_verify import check_resources
    shadows = check_resources(resources, piece)
    return {'passed': True, 'actual_indexed_triangles_checked': len(faces),
            'texture_ids': sorted({texture for face in faces for texture in face['material']['textures']}),
            'all_five_zooms_identical': True, 'preview_matches_all_saved_cells': True,
            'actual_saved_vehicle_corridors': corridors, 'road_shell': road,
            'unchanged_native_vehicle_corridors': native_corridors,
            'barrier_shell': barriers, 'support_shell': supports,
            'independent_native_collar_certificate': native_certificate,
            'complete_saved_support_prisms': solid_supports,
            'native_finite_physical_seams': seams, 'native_draggable_boundary_contract': native,
            'whole_assembly_width_and_seams_require_separate_check': True,
            **shadows, 'game_rendering_tested': False, 'structural_capacity_tested': False}


def check_models_assembly(pieces, resources_by_id, donors):
    faces, routes = [], []
    for piece in pieces:
        resources = resources_by_id[piece['id']]
        faces.extend(gather(resources, piece))
        routes.extend(_saved_routes(resources, piece))
    references = native_faces(donors)
    all_faces = [*faces, *references]
    pavement = FaceIndex(all_faces)
    skin, native_certificate = external_skin(faces, donors)
    return {'passed': True, 'actual_indexed_triangles_checked': len(faces),
            'texture_ids': sorted({texture for face in faces for texture in face['material']['textures']}),
            'actual_saved_vehicle_corridors': check_corridors(all_faces, routes, full_width=True),
            'unchanged_native_vehicle_corridors': check_native_vehicle_clearance(faces, native_traffic(donors)),
            'complete_road_shell': check_shell(skin, kind='road', component=False, pavement_index=pavement,
                                              native_profiles=native_open_profiles(donors)),
            'complete_barrier_shell': {'integral_raised_road_shell': True, 'actual_barrier_triangles': sum(f['kind'] == 'barrier' for f in faces)},
            'complete_support_shell': check_shell(faces, kind='support', component=False, pavement_index=pavement),
            'complete_saved_support_prisms': check_support_solids(all_faces, [*routes, *native_traffic(donors)], whole=True),
            'deck_body_clearance': check_deck_overlaps(faces),
            'underside_surface_clearance': check_underside_overlaps(skin),
            'barrier_to_deck_solid_clearance': check_barrier_deck_clearance(all_faces),
            'barrier_to_barrier_surface_clearance': check_barrier_intersections(all_faces),
            'native_finite_physical_seams': _native_seams(faces, donors, ('A', 'B', 'C')),
            'independent_native_collar_certificate': native_certificate,
            'game_rendering_tested': False, 'structural_capacity_tested': False}
