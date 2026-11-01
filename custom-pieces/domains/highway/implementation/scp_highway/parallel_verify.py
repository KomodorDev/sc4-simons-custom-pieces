"""Independently inspect encoded resources for the approved parallel diamond.

Expected driving geometry comes from the immutable, human-approved review,
not the implementation's layout, mesh, or PATH author.  Actual saved indexed
triangles, rather than construction ownership or a preview, establish road
support and the full assembled physical joins.  Game behavior is unverified.
"""
from __future__ import annotations

from bisect import bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from functools import lru_cache
import hashlib
import importlib
import json
import math
from pathlib import Path
import re
import struct

from scp.dbpf import decompress, require
from scp.models import parse_s3d, positions, validate_s3d
from scp.track_paths import PATH, S3D

PREFIX = 'highway_ddrhw_parallel_'
SUBJECT = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond'
GROUND_MOUTH_PROFILE = 'taper-6m-to-3p5m-over-3m'
HIGHWAY_SLIP_PROFILE = 'shoulder-auxiliary-lower-8m-4m-upper-5m-1m'
ROOT = Path(__file__).resolve().parents[4]
APPROVAL = ('domains/highway/01_assemblies/'
            'ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/'
            'evidence/parallel-ramp-review.json')
APPROVAL_SHA256 = 'fed3668c9c13654ca3775637c558cd85976269d4cb3f39634c8d5a1a7ff9e23e'
SOURCE_SHA256 = '6259e4364ba6447204c85bc35229196ce0151b40a496bfa53680ec7908ec51a9'
TOLERANCE = 4e-5
NEIGHBOURS = ((-1, 0), (0, -1), (1, 0), (0, 1))
OWNED_CELLS = frozenset(((2, -3), (3, -3), (4, -3), (1, -2), (2, -2), (3, -2),
    (4, -2), (-1, -1), (0, -1), (1, -1), (2, -1), (3, -1), (-1, 0), (0, 0),
    (1, 0), (2, 0), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (-3, 2),
    (-2, 2), (-1, 2), (0, 2), (1, 2), (-3, 3), (-2, 3), (-1, 3), (-3, 4), (-2, 4)))


@lru_cache(maxsize=1)
def approved_candidate():
    raw = (ROOT / APPROVAL).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == APPROVAL_SHA256,
            'Approved parallel-ramp evidence fingerprint changed')
    report = json.loads(raw)
    require(report['source_geometry_review_sha256'] == SOURCE_SHA256,
            'Approved parallel-ramp source fingerprint changed')
    candidate = next(c for c in report['source_geometry_review']['candidates']
                     if c['id'] == 'parallel-inward-upper')
    require(set(map(tuple, candidate['owned_cells'])) == OWNED_CELLS
            and candidate['bounds']['tiles'] == [8, 8]
            and candidate['parallel_offset_m'] == 12.
            and candidate['ground_turn_radius_m'] == 6.,
            'Approved parallel-ramp extent, alignment, or radius changed')
    return candidate


def _point_key(point):
    return tuple(round(value, 5) for value in point)


def _uv(point):
    return ((point[0] + point[1]) / math.sqrt(2),
            (point[1] - point[0] + 8.) / math.sqrt(2))


def _rotate(point, turns):
    x, y, h = point
    for _ in range(turns % 4):
        x, y = -y, x
    return x, y, h


def _split_points(points):
    """Independently split each approved chord at the actual 16 m lattice."""
    result = defaultdict(list)
    previous_cell = None
    for first, last in zip(points, points[1:]):
        cuts = [0., 1.]
        for axis in (0, 1):
            delta = last[axis] - first[axis]
            if abs(delta) < 1e-12:
                continue
            low, high = sorted((first[axis], last[axis]))
            for index in range(math.floor((low + 8.) / 16.),
                               math.ceil((high + 8.) / 16.) + 1):
                at = (16. * index - 8. - first[axis]) / delta
                if 1e-10 < at < 1. - 1e-10:
                    cuts.append(at)
        cuts = sorted(set(cuts))
        for a, b in zip(cuts, cuts[1:]):
            middle = tuple(x + (a + b) / 2. * (y - x) for x, y in zip(first, last))
            cell = math.floor((middle[0] + 8.) / 16.), math.floor((8. - middle[1]) / 16.)
            ends = [tuple(x + t * (y - x) for x, y in zip(first, last)) for t in (a, b)]
            if previous_cell == cell:
                result[cell][-1].append(ends[-1])
            else:
                result[cell].append(ends)
            previous_cell = cell
    return result


@lru_cache(maxsize=2)
def revised_routes(profile=None):
    """Independently reconstruct the explicit PATH-only shoulder revision.

    The immutable approval still owns every physical mesh point and cut.
    These literal taper/parallel dimensions alter only traffic before the
    first retained sample at or beyond the actual eight-metre deck edge.
    """
    require(profile in (None, HIGHWAY_SLIP_PROFILE), 'Unknown parallel highway-slip profile')
    original = approved_candidate()['routes']
    if profile is None:
        return deepcopy(original)
    result = []
    for ramp in original:
        outward = ramp['points'] if ramp['direction'] == 'off' else list(reversed(ramp['points']))
        old_u, _old_v = _uv(outward[0])
        direction = 1. if _uv(outward[1])[0] > old_u else -1.
        first = tuple(outward[0])
        if ramp['deck'] == 'lower':
            first = (60.8, 56., 7.5) if ramp['direction'] == 'off' else (-56., -60.8, 7.5)
        u0, v0 = _uv(first)
        side, height = ramp['side'], ramp['height_m']
        taper, parallel = (8., 4.) if ramp['deck'] == 'lower' else (5., 1.)
        join = next(at for at, point in enumerate(outward) if side * _uv(point)[1] >= 8.)
        endpoint, following = _uv(outward[join]), _uv(outward[join + 1])
        joining_station = direction * (endpoint[0] - u0)
        joining_q = side * endpoint[1]
        slope = side * (following[1] - endpoint[1]) / (direction * (following[0] - endpoint[0]))
        span = joining_station - taper - parallel
        require(span > 0., 'Parallel highway shoulder lacks a finite retained joining span')

        def world(station, lateral):
            u, v = u0 + direction * station, side * lateral
            return (4. + (u - v) / math.sqrt(2.), -4. + (u + v) / math.sqrt(2.), height)

        prefix = [first, (first[0] + direction * .01 / math.sqrt(2.),
                          first[1] + direction * .01 / math.sqrt(2.), height)]
        for at in range(1, int(taper * 8.) + 1):
            station = at / 8.
            t = station / taper
            ease = 10. * t ** 3 - 15. * t ** 4 + 6. * t ** 5
            prefix.append(world(station, abs(v0) + (5.5 - abs(v0)) * ease))
        prefix.extend(world(taper + at / 8., 5.5) for at in range(1, int(parallel * 8.) + 1))
        steps = max(8, math.ceil(span * 8.))
        for at in range(1, steps):
            t = at / steps
            lateral = (5.5 * (2. * t ** 3 - 3. * t ** 2 + 1.)
                       + joining_q * (-2. * t ** 3 + 3. * t ** 2)
                       + span * slope * (t ** 3 - t ** 2))
            prefix.append(world(taper + parallel + t * span, lateral))
        require(all(side * _uv(point)[1] < 8. for point in prefix),
                'A revised shoulder sample alters the retained outside-deck route')
        revised = prefix + [tuple(point) for point in outward[join:]]
        points = revised if ramp['direction'] == 'off' else list(reversed(revised))
        delta, old_last = len(points) - len(ramp['points']), len(ramp['points']) - 1
        segments = deepcopy(ramp['segments'])
        for segment in segments:
            for key in ('start_index', 'end_index'):
                if (segment[key] >= join if ramp['direction'] == 'off' else segment[key] > old_last - join):
                    segment[key] += delta
        record = {**deepcopy(ramp), 'mesh_points': deepcopy(ramp['points']),
                       'points': points, 'segments': segments,
                       'points_uvh': [[*_uv(point), point[2]] for point in points],
                       'native_high_port': list(first),
                       'path_cells': [list(cell) for cell in sorted(_split_points(points), key=lambda c: (c[1], c[0]))],
                       'highway_slip_profile': profile,
                       'independent_auxiliary_lane': {'taper_m': taper, 'parallel_m': parallel,
                           'auxiliary_q_m': 5.5, 'joining_station_m': joining_station,
                           'bridge_axis_length_m': span, 'retained_first_outside_sample': list(outward[join]),
                           'retained_outward_joining_slope': slope}}
        record['profile']['length_total_plan_m'] = sum(math.dist(a[:2], b[:2]) for a, b in zip(points, points[1:]))
        result.append(record)
    return result


@lru_cache(maxsize=2)
def expected_cell_routes(profile=None):
    """All unchanged native channels plus the exact four approved transfers."""
    from .assembly_verify import _native_routes
    result = {cell: [{**route, 'points': [(p[0] + 16. * cell[0], p[1] - 16. * cell[1], p[2])
                                        for p in route['points']]}
                     for route in _native_routes(*cell)] for cell in OWNED_CELLS}
    for ramp in revised_routes(profile):
        for cell, fragments in _split_points(ramp['points']).items():
            require(cell in result, 'An approved ramp leaves the literal 31-cell union')
            result[cell].extend({'transport': 1, 'points': points, 'approved_ramp': ramp['id']}
                                for points in fragments)
    return result


def _route_key(route):
    return route['transport'], tuple(_point_key(p) for p in route['points'])


def _same_routes(actual, expected):
    remaining = list(expected)
    for route in actual:
        match = next((other for other in remaining if route['transport'] == other['transport']
                      and len(route['points']) == len(other['points'])
                      and all(math.dist(a, b) <= 1.1e-6 for a, b in zip(route['points'], other['points']))), None)
        if match is None:
            return False
        remaining.remove(match)
    return not remaining


def _source_origin(piece):
    """Read the reviewed literal partition, never the mesh or route writer."""
    key = piece.get('geometry_key', '').removeprefix('parallel-')
    require(piece.get('recipe', '').startswith(PREFIX), 'Not a parallel highway recipe')
    require(key in PARTITIONS, 'No independent parallel module ownership contract')
    require(piece['recipe'] == PREFIX + key.replace('-', '_'),
            'Parallel recipe disagrees with its independent geometry key')
    cells = PARTITIONS[key]
    origin = min(c[0] for c in cells), min(c[1] for c in cells)
    expected = sorted(([x - origin[0], y - origin[1]] for x, y in cells),
                      key=lambda c: (c[1], c[0]))
    require(piece['cells'] == expected
            and piece['footprint'] == [max(c[a] for c in expected) + 1 for a in (0, 1)]
            and len(piece['tile_ids']) == len(expected)
            and len(set(piece['tile_ids'])) == len(expected),
            'Parallel module ownership or sparse footprint differs from the reviewed partition')
    engineering = piece.get('engineering', {})
    require(engineering.get('highway_slip_profile') in (None, HIGHWAY_SLIP_PROFILE),
            'Parallel piece declares an unknown highway-slip profile')
    if 'ground_mouth_profile' in engineering:
        require(key in ('northwest-terminal', 'southeast-terminal')
                and engineering['ground_mouth_profile'] == GROUND_MOUTH_PROFILE,
                'Parallel terminal declares an unknown or misplaced ground-mouth profile')
    require(engineering.get('max_grade_percent') == 30.
            and engineering.get('pavement_path_offset_m') == 0.
            and engineering.get('car_corridor_half_width_m') == 1.25
            and engineering.get('car_corridor_height_m') == 3.8,
            'Parallel module grade, pavement datum, or traffic corridor changed')
    return origin


# Frozen after independent inspection of the actual minimum whole-cell split.
# The compiler imports neither this dictionary nor any verifier helper.
PARTITIONS = {
    'crossing': ((0, 0), (1, 0), (0, 1)),
    'northwest-terminal': ((-1, -1), (0, -1), (-1, 0)),
    'southeast-terminal': ((1, 1), (2, 1), (1, 2)),
    'lower-exit-slip': ((3, -3), (2, -2)),
    'lower-entry-slip': ((-2, 2), (-3, 3)),
    'upper-exit-slip': ((-2, 3), (-3, 4)),
    'upper-entry-slip': ((4, -3), (3, -2)),
    'lower-exit-departure': ((2, -3),),
    'lower-entry-departure': ((-3, 2),),
    'upper-exit-departure': ((-2, 4),),
    'upper-entry-departure': ((4, -2),),
    'lower-exit-grade': ((1, -2), (1, -1)),
    'lower-entry-grade': ((-2, 1), (-1, 1)),
    'upper-exit-grade': ((-1, 2), (0, 2), (-1, 3)),
    'upper-entry-grade': ((2, -1), (3, -1), (2, 0)),
}


def check_paths(resources, piece):
    from .ramp_verify import _paths
    origin = _source_origin(piece)
    profile = piece.get('engineering', {}).get('highway_slip_profile')
    expected = expected_cell_routes(profile)
    routes = []
    maximum = 0.
    for cell, tile in zip(piece['cells'], piece['tile_ids']):
        source_cell = cell[0] + origin[0], cell[1] + origin[1]
        actual = _paths(resources[*PATH, int(tile, 16)])
        translated = [{**route, 'points': [(p[0] + 16. * source_cell[0],
                       p[1] - 16. * source_cell[1], p[2]) for p in route['points']]}
                      for route in actual]
        require(_same_routes(translated, expected[source_cell]),
                f'Saved parallel PATH differs from approved/native routes in source cell {source_cell}')
        for route in translated:
            for a, b in zip(route['points'], route['points'][1:]):
                maximum = max(maximum, abs(b[2] - a[2]) / math.dist(a[:2], b[:2]))
        routes.extend(translated)
    require(maximum <= .30001, 'Saved parallel ramp exceeds 30 percent grade')
    return {'passed': True, 'approved_route_points_and_native_channels_checked': True,
            'route_fragments_checked': len(routes), 'maximum_grade_percent': maximum * 100.,
            'highway_slip_profile': profile or 'retained-approved-departure',
            'approval_sha256': APPROVAL_SHA256, 'game_operation_tested': False}


def _endpoint_edge(point, other):
    matches = [side for side, (axis, value) in enumerate(((0, -8.), (1, 8.), (0, 8.), (1, -8.)))
               if abs(point[axis] - value) <= TOLERANCE
               and (other[axis] - point[axis]) * (-1. if value > 0. else 1.) > 1e-10]
    require(len(matches) == 1, 'Approved path has no unique directed tile-edge cut')
    return matches[0]


def expected_ports(piece):
    """Complete intrinsic traffic cuts, independent of physical render cuts."""
    from .ramp_verify import _endpoints
    origin = _source_origin(piece)
    routes = {}
    for local in map(tuple, piece['cells']):
        source = local[0] + origin[0], local[1] + origin[1]
        records = []
        for expected in expected_cell_routes(piece.get('engineering', {}).get('highway_slip_profile'))[source]:
            city_local = [(p[0] - 16. * source[0], p[1] + 16. * source[1], p[2])
                          for p in expected['points']]
            records.append({'transport': expected['transport'],
                'entry': _endpoint_edge(city_local[0], city_local[1]),
                'exit': _endpoint_edge(city_local[-1], city_local[-2]),
                'points': [(p[0] - 16. * origin[0], p[1] + 16. * origin[1], p[2])
                           for p in expected['points']]})
        routes[local] = records
    ends = _endpoints(routes)
    result = []
    for endpoint in ends:
        dx, dy = NEIGHBOURS[endpoint['side']]
        neighbour = endpoint['cell'][0] + dx, endpoint['cell'][1] + dy
        if any(other['direction'] != endpoint['direction']
               and other['transport'] == endpoint['transport']
               and other['cell'] == neighbour and other['side'] == (endpoint['side'] + 2) % 4
               and math.dist(other['point_m'], endpoint['point_m']) < TOLERANCE for other in ends):
            continue
        if any(other['transport'] == endpoint['transport'] and other['direction'] == endpoint['direction']
               and math.dist(other['point_m'], endpoint['point_m']) < TOLERANCE for other in result):
            continue
        result.append({**endpoint, 'source_cell': list(endpoint['cell']), 'edge': endpoint['side']})
    return result


def reviewed_contract(piece):
    """Name the independently sampled complete port graph for extraction."""
    origin = _source_origin(piece)
    ports = expected_ports(piece)
    result = {'ports': {}, 'port_vectors': {}, 'port_transports': {}, 'port_directions': {}, 'movements': []}
    for index, port in enumerate(sorted(ports, key=lambda p: (p['transport'], p['direction'], p['point_m']))):
        name = f'channel-{index + 1:02d}-{port["direction"]}'
        port['id'] = name
        result['ports'][name] = list(port['point_m'])
        result['port_vectors'][name] = list(port['tangent'])
        result['port_transports'][name] = port['transport']
        result['port_directions'][name] = port['direction']
    graph = defaultdict(set)
    for cell in PARTITIONS[piece['geometry_key'].removeprefix('parallel-')]:
        for route in expected_cell_routes(piece.get('engineering', {}).get('highway_slip_profile'))[cell]:
            graph[route['transport'], _point_key(route['points'][0])].add(
                (route['transport'], _point_key(route['points'][-1])))
    for first in ports:
        if first['direction'] != 'in':
            continue
        start = first['transport'], _point_key((first['point_m'][0] + 16. * origin[0],
                                               first['point_m'][1] - 16. * origin[1], first['point_m'][2]))
        pending, seen = [start], set()
        while pending:
            point = pending.pop()
            if point not in seen:
                seen.add(point)
                pending.extend(graph[point] - seen)
        for last in ports:
            finish = last['transport'], _point_key((last['point_m'][0] + 16. * origin[0],
                                                   last['point_m'][1] - 16. * origin[1], last['point_m'][2]))
            if last['direction'] == 'out' and finish in seen:
                result['movements'].append([first['id'], last['id']])
    return result


def _decode_faces(raw, local_cell=(0, 0), *, origin=(0., 0.), turns=0):
    """Decode every referenced triangle and UV, including deliberate overhang."""
    model = parse_s3d(decompress(raw))
    validate_s3d(model)
    result = []
    for mesh in model['meshes']:
        require(len(mesh['frames']) == 1, 'Parallel road needs static complete meshes')
        vi, ii, pi, mi = mesh['frames'][0]
        block = model['vertices'][vi]
        require(block['stride'] >= 20, 'Parallel mesh needs encoded XYZ and UV attributes')
        require(len(block['data']) // block['stride'] <= 512,
                'Parallel S3D render group exceeds the conservative 512-vertex budget')
        vertices = [struct.unpack_from('<5f', block['data'], at)
                    for at in range(0, len(block['data']), block['stride'])]
        require(all(all(math.isfinite(v) for v in p) for p in vertices),
                'Parallel model contains a nonfinite position or UV')
        require(all(max(abs(p[0]), abs(p[2])) <= 32. for p in vertices),
                'Parallel local model exceeds the measured 32m encoding envelope')
        material = model['materials'][mi]
        require(len(material['textures']) == 1, 'Parallel mesh needs exactly one native material texture')
        indices = model['indices'][ii]['values']
        require(len(indices) <= 1536, 'Parallel S3D render group exceeds its 1,536-index budget')
        for kind, first, size in model['primitives'][pi]:
            require(kind == 0 and size % 3 == 0, 'Parallel models need indexed triangles')
            for at in range(first, first + size, 3):
                source = tuple(vertices[i] for i in indices[at:at + 3])
                points = []
                for p in source:
                    posed = _rotate((p[0] + 16. * local_cell[0],
                                     -p[2] - 16. * local_cell[1], p[1]), turns)
                    points.append((posed[0] + origin[0], posed[1] + origin[1], posed[2]))
                area = ((points[1][0] - points[0][0]) * (points[2][1] - points[0][1])
                        - (points[1][1] - points[0][1]) * (points[2][0] - points[0][0]))
                result.append({'points': tuple(points), 'upward': area > 1e-12,
                    'texture': material['textures'][0], 'uv': tuple((p[3], p[4]) for p in source),
                    'material_sha256': hashlib.sha256(material['raw']).hexdigest(),
                    'material': material, 'source_vertices': source,
                    'mesh_name': mesh['name'].rstrip(b'\0').decode('ascii', errors='replace')})
    require(result, 'Parallel model contains no referenced triangles')
    return result


_MODEL_CACHE = OrderedDict()


def check_models(resources, piece, donors=None):
    """Cache only exact inputs and live independent validator identities."""
    from .ramp_verify import _model_audit_context
    modules = ('scp_highway.parallel_verify', 'scp_highway.modular_partition_verify',
               'scp_highway.modular_assembly_verify', 'scp_highway.adaptive_verify', 'scp.shadows',
               'scp.model_shadows', 'scp.model_shadow_geometry', 'scp_highway.shadow_verify')
    context = []
    for name in modules:
        module = importlib.import_module(name)
        context.append((name, hashlib.sha256(Path(module.__file__).read_bytes()).digest(),
                        tuple((key, id(value)) for key, value in sorted(vars(module).items()) if callable(value)),
                        hashlib.sha256(repr([(key, value) for key, value in sorted(vars(module).items())
                                             if key.isupper() and key != '_MODEL_CACHE']).encode()).digest()))
    identity = (json.dumps(piece, sort_keys=True, separators=(',', ':')),
                tuple((key, hashlib.sha256(value).digest()) for key, value in sorted(resources.items())),
                _model_audit_context(), tuple(context))
    if identity in _MODEL_CACHE:
        _MODEL_CACHE.move_to_end(identity)
        return deepcopy(_MODEL_CACHE[identity])
    result = _check_models_uncached(resources, piece, donors)
    _MODEL_CACHE[identity] = deepcopy(result)
    while len(_MODEL_CACHE) > 24:
        _MODEL_CACHE.popitem(last=False)
    return result


def _check_models_uncached(resources, piece, donors=None):
    from .modular_partition_verify import check_preview
    from .ramp_verify import _native_appearance
    origin = _source_origin(piece)
    faces, triangles = [], 0
    for cell, tile in zip(piece['cells'], piece['tile_ids']):
        identifier = int(tile, 16)
        raw = decompress(resources[*S3D, identifier])
        for zoom in range(5):
            require(decompress(resources[*S3D, identifier + zoom]) == raw,
                    'Parallel saved zoom differs from the independently inspected base model')
        decoded = _decode_faces(raw, cell)
        faces.extend(decoded)
        triangles += len(decoded)
    # Native UVs may contain legitimately constant neutral samples only if
    # their complete independent field check authorizes that exception.
    world_faces = [{**face, 'points': tuple((p[0] + 16. * origin[0], p[1] - 16. * origin[1], p[2])
                                          for p in face['points'])} for face in faces]
    field = check_wheeltrack_vertices(world_faces,
                                     highway_slip_profile=piece.get('engineering', {}).get('highway_slip_profile'))
    appearance = _native_appearance(faces, neutral_field_controls=field)
    check_preview(resources, piece)
    report = {'passed': True, 'model_resources_checked': 5 * len(piece['cells']) + 1,
              'indexed_triangles_checked': triangles, 'all_five_zooms_exact': True,
              'texture_ids': sorted({face['texture'] for face in faces}),
              'preview_matches_all_saved_cells': True, 'native_appearance': appearance,
              'independent_wheeltrack_field': field,
              'game_rendering_tested': False}
    if piece.get('adaptive_ground'):
        from .adaptive_verify import check_resources
        report['adaptive_ground'] = check_resources(resources, piece)
    if piece.get('shadow_mode') == 'generated':
        from scp.shadows import validate_piece_shadows
        report['shadows'] = validate_piece_shadows(resources, piece)
    if piece.get('shadow_mode') == 'model-carrier':
        from .shadow_verify import check_resources
        report.update(check_resources(resources, piece))
    return report


@lru_cache(maxsize=2)
def _approved_texture_segments(profile=None):
    result = []
    for route in revised_routes(profile):
        distance = 0.
        segments = []
        for a, b in zip(route['points'], route['points'][1:]):
            length = math.dist(a[:2], b[:2])
            segments.append((a, b, distance, length, (b[0] - a[0]) / length, (b[1] - a[1]) / length))
            distance += length
        buckets = defaultdict(list)
        for segment in segments:
            a, b = segment[:2]
            for x in range(math.floor((min(a[0], b[0]) - 4.) / 2.), math.floor((max(a[0], b[0]) + 4.) / 2.) + 1):
                for y in range(math.floor((min(a[1], b[1]) - 4.) / 2.), math.floor((max(a[1], b[1]) + 4.) / 2.) + 1):
                    buckets[x, y].append(segment)
        result.append((route, {'segments': segments, 'buckets': buckets,
                               'stations': [segment[2] for segment in segments]}))
    return result


def _nearest_texture_frame(point, segments):
    return _texture_frames(point, segments)[0]


def _texture_frames(point, segments, *, encoding_ties=False):
    best = None
    frames = []
    candidates = segments['buckets'].get((math.floor(point[0] / 2.), math.floor(point[1] / 2.)), segments['segments'])
    for a, b, station, length, tx, ty in candidates:
        at = min(length, max(0., (point[0] - a[0]) * tx + (point[1] - a[1]) * ty))
        x, y, h = a[0] + at * tx, a[1] + at * ty, a[2] + at / length * (b[2] - a[2])
        score = (point[0] - x) ** 2 + (point[1] - y) ** 2 + 4. * (point[2] - h) ** 2
        frame = score, station + at, -(point[0] - x) * ty + (point[1] - y) * tx, tx, ty
        frames.append(frame)
        if best is None or score < best[0]:
            best = frame
    if not encoding_ties:
        return [best]
    # Two actual float32 packing stages bound each planar coordinate by
    # 4 micrometres here. The distance to any finite segment is 1-Lipschitz.
    # Only a nearest-segment order that can reverse within that position
    # envelope may supply an alternative phase; arbitrary stations cannot.
    position_radius = math.sqrt(2.) * 4e-6
    distance = math.sqrt(best[0])
    return [frame for frame in frames if math.sqrt(frame[0]) - distance <= 2. * position_radius + 1e-12]


def _phase_tangent(distance, segments, profile):
    """The revised field uses the following chord at an exact phase vertex.

    Lateral distance still belongs to the nearest finite chord. At its
    clamped end that chord and the phase-selected chord need not be the
    same. This literal field rule preserves the existing UV and position
    bounds; it does not admit an arbitrary alternative tangent.
    """
    require(profile == HIGHWAY_SLIP_PROFILE, 'Following phase tangents need the revised slip profile')
    at = max(0, bisect_right(segments['stations'], distance) - 1)
    return segments['segments'][at][4:6]


def check_wheeltrack_vertices(faces, *, highway_slip_profile=None):
    """Bound the neutral exception by the complete independent saved UV field.

    Every newly mapped DD field vertex must follow the approved route's
    unmarked native asphalt band and longitudinal metre station. A broad
    neutral patch subdivided into small faces therefore cannot pass.
    """
    count, maximum_u, maximum_v = 0, 0., 0.
    for face in faces:
        if face['texture'] != 0x5713000E or not face['upward']:
            continue
        if not all(65.5 / 128. - 3e-6 <= uv[0] <= 95.5 / 128. + 3e-6 for uv in face['uv']):
            continue
        heights = [p[2] for p in face['points']]
        if max(heights) - min(heights) > 1e-5 or min(abs(heights[0] - 7.5), abs(heights[0] - 15.)) > 1e-5:
            continue
        centre = tuple(sum(p[a] for p in face['points']) / 3. for a in range(3))
        candidates = [(route, segments) for route, segments in _approved_texture_segments(highway_slip_profile)
                      if abs(route['height_m'] - centre[2]) <= 1e-5]
        route, segments = min(candidates, key=lambda pair: _nearest_texture_frame(centre, pair[1])[0])
        side = route['side']
        require(all(4.5 - .001 <= side * _uv(p)[1] <= 8. + .001 for p in face['points']),
                'Parallel wheeltrack mapping leaves the approved native shoulder band')
        error_by_flank = []
        for flank in (-1, 1):
            errors_u, errors_v = [], []
            for point, actual in zip(face['points'], face['uv']):
                variants = []
                for _score, distance, lateral, tx, ty in _texture_frames(point, segments, encoding_ties=True):
                    if highway_slip_profile == HIGHWAY_SLIP_PROFILE:
                        tx, ty = _phase_tangent(distance, segments, highway_slip_profile)
                    q = side * _uv(point)[1]
                    centre_q = q - lateral * side * (tx + ty) / math.sqrt(2.)
                    ease = lambda value: (lambda t: t * t * (3. - 2. * t))(min(1., max(0., value)))
                    amplitude = ease(centre_q - 4.5) * ease(q - 4.5)
                    column = 63.5 + 8. * lateral
                    target = min(95., max(65., column + 16. + min(1., max(0., (column - 68.) / 6.))))
                    edge = 65. if flank < 0 else 95.
                    expected_u = (edge + (target - edge) * amplitude + .5) / 128.
                    variants.append((abs(actual[0] - expected_u), abs(actual[1] - distance / 16.)))
                u_error, v_error = min(variants, key=lambda row: max(row))
                errors_u.append(u_error)
                errors_v.append(v_error)
            error_by_flank.append((max(errors_u), max(errors_v)))
        error_u, error_v = min(error_by_flank)
        require(error_u <= 5e-6 and error_v <= 5e-6,
                f'Parallel saved wheeltrack UV does not follow its approved native wear field: U={error_u}, V={error_v}')
        maximum_u, maximum_v = max(maximum_u, error_u), max(maximum_v, error_v)
        count += 1
    return {'passed': True, 'mapped_native_dd_triangles_checked': count,
            'highway_slip_profile': highway_slip_profile or 'retained-approved-departure',
            'maximum_vertex_u_error': maximum_u, 'maximum_vertex_v_error': maximum_v,
            'vertex_uv_tolerance': 5e-6, 'source': 'Pinned approved routes and independently reconstructed native asphalt field',
            'nearest_finite_segment_position_tie_radius_m': math.sqrt(2.) * 4e-6,
            'game_filtering_or_colour_observed': False}


def check_highway_slip_lanes(faces, *, profile):
    """Affirmatively sample saved tyre-wear phase on every real parallel run."""
    require(profile == HIGHWAY_SLIP_PROFILE, 'Revised slip checks need the explicit highway-slip profile')
    from .ramp_verify import _barycentric
    index = _FaceIndex(faces)
    controls = []
    for route, segments in _approved_texture_segments(profile):
        data = route['independent_auxiliary_lane']
        outward = route['points'] if route['direction'] == 'off' else list(reversed(route['points']))
        u0, _v0 = _uv(outward[0])
        direction = 1. if _uv(outward[1])[0] > u0 else -1.
        samples = math.ceil(data['parallel_m'] / .5)
        for at in range(samples):
            station = data['taper_m'] + data['parallel_m'] * (at + .5) / samples
            u, q = u0 + direction * station, route['side'] * 5.5
            point = 4. + (u - q) / math.sqrt(2.), -4. + (u + q) / math.sqrt(2.), route['height_m']
            _score, distance, lateral, _tx, _ty = _nearest_texture_frame(point, segments)
            require(abs(lateral) < 1e-8, 'Independent auxiliary control leaves its literal parallel centreline')
            expected = 80. / 128., distance / 16.
            found = []
            for face in index.nearby(point, margin=2e-5):
                if face['texture'] != 0x5713000E or not face['upward']:
                    continue
                weights = _barycentric(point, face['points'])
                if weights is None or min(weights) < -1e-7:
                    continue
                height = sum(w * p[2] for w, p in zip(weights, face['points']))
                if abs(height - point[2]) > 2e-6:
                    continue
                actual = tuple(sum(w * uv[axis] for w, uv in zip(weights, face['uv'])) for axis in (0, 1))
                found.append(max(abs(a - b) for a, b in zip(actual, expected)))
            require(found and min(found) <= 5e-6,
                    f'Parallel auxiliary lane lacks its actual saved native wear field: {route["id"]} {station}')
        controls.append({'ramp_id': route['id'], 'taper_axis_m': data['taper_m'],
                         'parallel_axis_m': data['parallel_m'], 'auxiliary_axis_q_m': 5.5,
                         'continuous_sampled_parallel_chords': int(data['parallel_m'] * 8.),
                         'saved_wear_controls': samples,
                         'outside_mesh_and_route_reference': 'immutable approved candidate'})
    return {'passed': True, 'profile': profile, 'ramps': controls,
            'actual_saved_parallel_wear_controls': sum(row['saved_wear_controls'] for row in controls),
            'vertex_and_sample_uv_tolerance': 5e-6,
            'scope': 'Exact independently reconstructed saved PATHs establish real taper and parallel lengths; actual indexed DD UV controls affirm native tyre wear on all four parallel runs. Physical road-width checks remain on the immutable original mesh, and actual car-corridor checks remain separate. No game observation.'}


def check_construction_fields(fields, piece, resources):
    from scp.verify import check_emitted_runtime_addresses
    from .ramp_verify import _paths, _road_word
    from .ddrhw_connections import approaches, check_construction_approaches
    native_approaches = approaches(piece)
    if native_approaches:
        fields = check_construction_approaches(fields, piece)
        piece = {key: value for key, value in piece.items() if key != 'native_dd_approaches'}
    _source_origin(piece)
    if piece.get('adaptive_ground'):
        from .adaptive_verify import check_construction_fields as inspect
        result = inspect(fields, piece, resources)
    else:
        width, depth = piece['footprint']
        rows = [['.'] * (width + 2) for _ in range(depth + 1)]
        rows[0][-1], rows[-1][0] = '<', '^'
        cons, checks = deepcopy(rows), []
        for index, (cell, tile) in enumerate(zip(piece['cells'], piece['tile_ids'])):
            symbol = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[index]
            rows[cell[1]][cell[0]], cons[cell[1]][cell[0]] = symbol, '+'
            checks.append(f'{symbol} - dirtroad: 0x{_road_word(_paths(resources[*PATH, int(tile, 16)])):08X}')
        normalize = lambda line: re.sub(r'0x[0-9a-fA-F]+', lambda m: m[0].upper(), line)
        require(fields.get('CellLayout') == [''.join(row) for row in rows]
                and fields.get('ConsLayout') == [''.join(row) for row in cons]
                and list(map(normalize, fields.get('CheckType', []))) == list(map(normalize, checks))
                and fields.get('Costs') == ['1000'],
                'Parallel construction changes sparse ownership or saved-route flags')
        result = {'passed': True, 'occupied_cells_checked': len(piece['cells'])}
    check_emitted_runtime_addresses(fields, piece)
    result = {**result, 'emitted_runtime_addresses_checked': True, 'game_behavior_tested': False}
    return ({**result, 'native_dd_outside_approaches_checked': len(native_approaches)}
            if native_approaches else result)


def check_owned_cells(pieces, scene):
    placements = scene.get('placements', [])
    require(len(placements) == 15, 'Parallel assembly needs fifteen functional placements')
    owners, keys, shifts = {}, set(), set()
    for index, pose in enumerate(placements):
        piece = pieces[pose['piece_id']]
        source = _source_origin(piece)
        key = piece['geometry_key'].removeprefix('parallel-')
        require(key not in keys and pose.get('rotation_degrees_ccw', 0) == 0,
                'Parallel assembly repeats a module or changes an approved relative pose')
        keys.add(key)
        origin = pose['origin_m']
        require(len(origin) == 2 and all(type(v) in (int, float) and math.isfinite(v) for v in origin),
                'Parallel assembly has an invalid placement origin')
        shift = origin[0] - source[0] * 16., origin[1] + source[1] * 16.
        require(all(abs(v / 16. - round(v / 16.)) < 1e-9 for v in shift),
                'Parallel assembly translation leaves the city-tile lattice')
        shifts.add(shift)
        for local, tile in zip(piece['cells'], piece['tile_ids']):
            cell = source[0] + local[0], source[1] + local[1]
            require(cell not in owners, 'Parallel assembly duplicates whole-cell ownership')
            owners[cell] = {'placement': index, 'piece_id': piece['id'], 'tile': int(tile, 16),
                           'local_cell': tuple(local), 'geometry_key': key, 'angle': 0,
                           'origin': (16. * source[0], -16. * source[1])}
    require(keys == set(PARTITIONS) and set(owners) == OWNED_CELLS and len(shifts) == 1,
            'Parallel assembly changes its exact fifteen-owner, 31-cell approved union')
    return owners, next(iter(shifts))


def _native_external_contract():
    from .assembly_verify import _native_routes, _direction
    result = {}
    for cell in OWNED_CELLS:
        for route in _native_routes(*cell):
            for direction, at, edge in (('in', 0, route['entry']), ('out', -1, route['exit'])):
                dx, dy = NEIGHBOURS[edge]
                if (cell[0] + dx, cell[1] + dy) in OWNED_CELLS:
                    continue
                p = route['points'][at]
                point = p[0] + 16. * cell[0], p[1] - 16. * cell[1], p[2]
                u, v = _uv(point)
                arm = ('HW_NE' if u > 0 else 'HW_SW') if point[2] > 1. else ('AVE_NW' if v > 0 else 'AVE_SE')
                tangent, grade = _direction(route['points'], direction == 'in')
                port = {'transport': route['transport'], 'direction': direction,
                        'point': _point_key(point), 'tangent': tangent, 'grade': grade, 'arm': arm}
                result[route['transport'], direction, _point_key(point)] = port
    require(len(result) == 20, 'Parallel native boundary must retain twenty directed ports')
    return result


def _search(starts, goals, graph):
    pending = deque((start, [start]) for start in starts)
    seen = set()
    while pending:
        node, path = pending.popleft()
        if node in seen:
            continue
        seen.add(node)
        if node in goals:
            return path
        pending.extend((next_, path + [next_]) for next_ in graph[node] if next_ not in seen)
    return None


def check_saved_routes(routes, *, turns=0):
    """Prove actual whole-cell graph reaches exactly the required arm pairs."""
    from .assembly_verify import _direction
    ends, graph, external = defaultdict(list), defaultdict(set), {'in': defaultdict(set), 'out': defaultdict(set)}
    expected = {}
    for port in _native_external_contract().values():
        point = _point_key(_rotate(port['point'], turns))
        tangent = _rotate((*port['tangent'], 0.), turns)[:2]
        rotated = {**port, 'point': point, 'tangent': tangent}
        expected[port['transport'], port['direction'], point] = rotated
    seen_external, seams = set(), []
    for route in routes:
        for direction, at, edge in (('in', 0, route['entry']), ('out', -1, route['exit'])):
            tangent, grade = _direction(route['points'], at == 0)
            ends[route['transport'], _point_key(route['points'][at])].append(
                {'direction': direction, 'route': route['id'], 'edge': edge,
                 'cell': tuple(route['cell']), 'tangent': tangent, 'grade': grade})
    for (transport, point), endpoints in ends.items():
        for endpoint in endpoints:
            dx, dy = NEIGHBOURS[endpoint['edge']]
            neighbour = endpoint['cell'][0] + dx, endpoint['cell'][1] + dy
            matches = [other for other in endpoints if other['direction'] != endpoint['direction']
                       and other['cell'] == neighbour and other['edge'] == (endpoint['edge'] + 2) % 4]
            if matches:
                for other in matches:
                    require(sum(a * b for a, b in zip(endpoint['tangent'], other['tangent'])) > .998
                            and abs(endpoint['grade'] - other['grade']) < .005,
                            'Parallel saved tile seam changes travel tangent or grade')
                    if endpoint['direction'] == 'out':
                        graph[endpoint['route']].add(other['route'])
                        seams.append((endpoint['route'], other['route'], point))
            else:
                key = transport, endpoint['direction'], point
                require(key in expected, 'Parallel saved graph has an unexpected or disconnected native boundary')
                contract = expected[key]
                require(sum(a * b for a, b in zip(endpoint['tangent'], contract['tangent'])) > .998
                        and abs(endpoint['grade']) < .005,
                        'Parallel saved native boundary tangent or grade changed')
                seen_external.add(key)
                external[endpoint['direction']][key].add(endpoint['route'])
    require(seen_external == set(expected), 'Parallel saved graph lost a native lane or sidewalk port')
    required = {('HW_NE', 'HW_SW'), ('HW_SW', 'HW_NE'), ('AVE_NW', 'AVE_SE'), ('AVE_SE', 'AVE_NW'),
                ('HW_NE', 'AVE_NW'), ('AVE_NW', 'HW_SW'), ('HW_SW', 'AVE_SE'), ('AVE_SE', 'HW_NE')}
    forbidden = {('HW_NE', 'AVE_SE'), ('AVE_SE', 'HW_SW'), ('HW_SW', 'AVE_NW'), ('AVE_NW', 'HW_NE')}
    reachable, witnesses, through = set(), {}, 0
    for first, starts in external['in'].items():
        same_lane = 0
        for last, goals in external['out'].items():
            if first[0] != last[0]:
                continue
            witness = _search(starts, goals, graph)
            if witness is None:
                continue
            pair = expected[first]['arm'], expected[last]['arm']
            if first[0] == 1:
                reachable.add(pair)
                witnesses.setdefault(pair, witness)
            p, q = _rotate(first[2], -turns), _rotate(last[2], -turns)
            axis_p, axis_q = (p[0] - p[1], q[0] - q[1]) if p[2] > 1 else (p[0] + p[1], q[0] + q[1])
            if abs(p[2] - q[2]) < TOLERANCE and abs(axis_p - axis_q) < TOLERANCE and pair[0] != pair[1]:
                same_lane += 1
        require(same_lane == 1, 'Parallel saved graph loses or ambiguously duplicates a native through lane')
        through += 1
    require(required <= reachable, 'Parallel saved graph loses a required right turn or through movement')
    require(not forbidden & reachable, 'Parallel saved graph permits a forbidden cross-Avenue turn')
    return {'passed': True, 'external_native_channels': len(seen_external),
            'pedestrian_external_channels': sum(p['transport'] == 2 for p in expected.values()),
            'native_through_lane_and_sidewalk_journeys': through,
            'matched_directed_lane_seams': len(seams), 'right_turn_transfers': 4,
            'no_cross_avenue_transfers': True,
            'reachable_arm_pairs': [list(pair) for pair in sorted(reachable)],
            'movement_witnesses': [{'from_arm': pair[0], 'to_arm': pair[1], 'saved_route_ids': witnesses[pair]}
                                   for pair in sorted(required)]}, seams


class _FaceIndex:
    """Use actual face bounds, so another piece's model overhang is visible."""
    def __init__(self, faces, size=2.):
        self.size = size
        self.bins = defaultdict(list)
        for face in faces:
            points = face['points']
            low = [min(p[a] for p in points) for a in (0, 1)]
            high = [max(p[a] for p in points) for a in (0, 1)]
            for x in range(math.floor(low[0] / size), math.floor(high[0] / size) + 1):
                for y in range(math.floor(low[1] / size), math.floor(high[1] / size) + 1):
                    self.bins[x, y].append(face)

    def nearby(self, first, last=None, margin=.01):
        last = first if last is None else last
        low = [min(first[a], last[a]) - margin for a in (0, 1)]
        high = [max(first[a], last[a]) + margin for a in (0, 1)]
        faces = {}
        for x in range(math.floor(low[0] / self.size), math.floor(high[0] / self.size) + 1):
            for y in range(math.floor(low[1] / self.size), math.floor(high[1] / self.size) + 1):
                for face in self.bins[x, y]:
                    if all(max(p[a] for p in face['points']) >= low[a]
                           and min(p[a] for p in face['points']) <= high[a] for a in (0, 1)):
                        faces[id(face)] = face
        return list(faces.values())


def _frames(points):
    """Intersect adjacent offset lines to recover the physical miter."""
    tangents = []
    for a, b in zip(points, points[1:]):
        length = math.dist(a[:2], b[:2])
        tangents.append(((b[0] - a[0]) / length, (b[1] - a[1]) / length))
    result = []
    for index in range(len(points)):
        before, after = tangents[max(0, index - 1)], tangents[min(index, len(tangents) - 1)]
        one, two = (-before[1], before[0]), (-after[1], after[0])
        determinant = before[0] * after[1] - before[1] * after[0]
        if abs(determinant) < 1e-10:
            result.append(two)
        else:
            delta = two[0] - one[0], two[1] - one[1]
            run = (delta[0] * after[1] - delta[1] * after[0]) / determinant
            result.append((one[0] + run * before[0], one[1] + run * before[1]))
    return result


def _near_surface(point, index, *, concrete=False, tolerance=.002, desired_normal=None):
    from .modular_assembly_verify import _triangle_distance
    def oriented(face):
        if desired_normal is None:
            return True
        a, b, c = face['points']
        one, two = [y - x for x, y in zip(a, b)], [y - x for x, y in zip(a, c)]
        normal = (one[1] * two[2] - one[2] * two[1],
                  one[2] * two[0] - one[0] * two[2], one[0] * two[1] - one[1] * two[0])
        return sum(x * y for x, y in zip(normal, desired_normal)) > 0.
    return any((not concrete or face['texture'] in (0x5EB4BEE9, 0x5EB4BEEE))
               and oriented(face)
               and _triangle_distance(point, face['points']) <= tolerance
               for face in index.nearby(point, margin=tolerance))


def _continuous_support(first, last, faces, precision, *, ground_mouth_profile=None):
    """Preserve strict support plus source-pinned two-micrometre certificates.

    Very thin remap triangles can leave a long parameter interval beside one
    almost parallel edge. Finite edge capsules prove the Euclidean distance
    for the complete uncovered interval; its along-route length is reported
    separately. Native DD/Avenue faces must match their actual donor planes,
    and MIS faces must lie on one independently reconstructed approved road
    triangle. Slopes use full3Dcapsules, not a horizontal height waiver.
    """
    from .ramp_verify import _covered, _interval, _edge_capsule_intervals, _point_triangle_distance, _native_fragment
    if _covered(first, last, faces):
        return True
    hashes = {0x5713000E: '307aba7786d4b4f11dbc499eb54f7d05d01a114001919b8a5f7d55970fbb64ca',
              0x5712000E: 'ed1b4a35ab986ff74a56ac79a1a33f579c31bf9630e7bb2b79ad4a4d9b6739ca',
              0x0400020E: 'b9e662590684786bfeca084538ef53fcd70c9c6beb489c2ea94f3d001ea2a6e5',
              0x0400380E: 'e481f8838ddc4e494a5fc2854007dbc319541a70d11ea3cbfd01f03c7a57bda1'}
    pinned = []
    for face in faces:
        texture = face['texture']
        if not face['upward'] or face['material_sha256'] != hashes.get(texture):
            continue
        if texture != 0x5712000E and (first[2] != last[2]
                or not all(abs(p[2] - first[2]) <= 1e-5 and p[2] == face['points'][0][2] for p in face['points'])):
            continue
        if texture == 0x5713000E and min(abs(first[2] - 7.5), abs(first[2] - 15.)) > 1e-5:
            continue
        if texture in (0x0400020E, 0x0400380E) and abs(first[2]) > 1e-5:
            continue
        # The encoded source triangle must remain within a real donor face,
        # preserving Avenue UVs. DD wear changes UVs only after the separate
        # whole-field proof above; its source geometry/material still pins.
        matched = (_native_avenue_fragment(face) if texture in (0x0400020E, 0x0400380E) else
                   _approved_ramp_encoding_fragment(face, ground_mouth_profile=ground_mouth_profile)
                   if texture == 0x5712000E else
                   _native_dd_fragment(face))
        if not matched:
            continue
        pinned.append(face)
    intervals = sorted(interval for face in faces if face['upward']
                       if (interval := _interval(first, last, face['points'])) is not None)
    gaps, reached = [], 0.
    for low, high in intervals:
        if low > reached + 1e-7:
            gaps.append((reached, low))
        reached = max(reached, high)
    if reached < 1. - 1e-7:
        gaps.append((reached, 1.))
    for low, high in gaps:
        capsules = []
        for face in pinned:
            for a, b in zip(face['points'], face['points'][1:] + face['points'][:1]):
                capsules.extend((max(low, begin), min(high, end)) for begin, end in
                                _edge_capsule_intervals_3d(first, last, a, b, 2e-6)
                                if end >= low and begin <= high)
        end = low
        for begin, finish in sorted(capsules):
            if begin > end + 1e-12:
                break
            end = max(end, finish)
        if end < high - 1e-12:
            return False
        precision['admitted_road_encoding_spans'] += 1
        precision['maximum_admitted_along_route_span_m'] = max(
            precision['maximum_admitted_along_route_span_m'], (high - low) * math.dist(first, last))
        for at in (low, (low + high) / 2., high):
            point = tuple(a + at * (b - a) for a, b in zip(first, last))
            from .modular_assembly_verify import _triangle_distance
            distance = min(_triangle_distance(point, face['points']) for face in pinned)
            precision['maximum_sampled_actual_face_distance_m'] = max(
                precision['maximum_sampled_actual_face_distance_m'], distance)
    return True


@lru_cache(maxsize=1)
def _approved_ramp_surface_index():
    faces = []
    for ramp in approved_candidate()['routes']:
        points, normals = ramp['points'], _frames(ramp['points'])
        for low, high in ((-3., 0.), (0., 3.)):
            for at, (a, b) in enumerate(zip(points, points[1:])):
                quad = [(p[0] + offset * n[0], p[1] + offset * n[1], p[2])
                        for p, n, offset in ((a, normals[at], low), (a, normals[at], high),
                                             (b, normals[at + 1], high), (b, normals[at + 1], low))]
                faces.extend({'points': tuple(triangle)} for triangle in
                             ((quad[0], quad[1], quad[2]), (quad[0], quad[2], quad[3])))
    return _FaceIndex(faces)


def _approved_ramp_encoding_fragment(face, *, ground_mouth_profile=None):
    """A saved MIS triangle must remain on one literal approved road triangle."""
    from .modular_assembly_verify import _triangle_distance
    require(ground_mouth_profile in (None, GROUND_MOUTH_PROFILE), 'Unknown parallel ground-mouth profile')
    flat_revised = ground_mouth_profile == GROUND_MOUTH_PROFILE and all(
        abs(point[2]) <= 1e-8 for point in face['points'])
    reference = _ground_reference(ground_mouth_profile) if flat_revised else _approved_ramp_surface_index()
    candidates = reference.nearby(face['points'][0], margin=4e-6)
    return any(all(_triangle_distance(point, source['points']) <= 4e-6 for point in face['points'])
               for source in candidates)


def _edge_capsule_intervals_3d(first, last, a, b, radius):
    """Exact quadratic interval intersections with one finite 3D edge capsule."""
    dot = lambda u, v: sum(x * y for x, y in zip(u, v))
    delta = tuple(y - x for x, y in zip(first, last))
    edge = tuple(y - x for x, y in zip(a, b))
    squared = dot(edge, edge)
    output = []

    def quadratic(vector, direction, low=0., high=1.):
        aa, bb = dot(direction, direction), 2. * dot(vector, direction)
        cc = dot(vector, vector) - radius ** 2
        if aa <= 1e-30:
            return (low, high) if cc <= 0. else None
        discriminant = bb * bb - 4. * aa * cc
        if discriminant < 0.:
            return None
        root = math.sqrt(max(0., discriminant))
        low, high = max(low, (-bb - root) / (2. * aa)), min(high, (-bb + root) / (2. * aa))
        return (low, high) if low <= high else None

    for endpoint in (a, b):
        interval = quadratic(tuple(x - y for x, y in zip(first, endpoint)), delta)
        if interval is not None:
            output.append(interval)
    if squared <= 1e-30:
        return output
    relative = tuple(x - y for x, y in zip(first, a))
    start, change = dot(relative, edge) / squared, dot(delta, edge) / squared
    low, high = 0., 1.
    if abs(change) < 1e-30:
        if not 0. <= start <= 1.:
            return output
    else:
        x, y = -start / change, (1. - start) / change
        low, high = max(0., min(x, y)), min(1., max(x, y))
    if low <= high:
        vector = tuple(x - start * y for x, y in zip(relative, edge))
        direction = tuple(x - change * y for x, y in zip(delta, edge))
        interval = quadratic(vector, direction, low, high)
        if interval is not None:
            output.append(interval)
    return output


def _native_avenue_fragment(face):
    """Literal native Avenue ground triangles, including all four rotations.

    Donor5753A300 SHA7509d29d6e36aa20c1b01689808ac30bf4a063fb6be8a0affd04b09a4643aef9
    supplies half triangle(-8,-8),(-8,8),(8,8). Donor5753A305
    SHA952d02ab4a523747cd4b049c56d7b7091a2d253a59530ebf96207d9691d99c40
    supplies both halves of the square. Both haveH0 and the affine UV map
    U=.5-X/16,V=.5-Z/16. These measurements precede candidate cuts.
    """
    for turns in range(4):
        matched = True
        for x, height, south, u, v in face['source_vertices']:
            for _ in range(turns):
                x, south = south, -x
            if (abs(height) > 1e-6 or max(abs(x), abs(south)) > 8. + 2e-5
                    or abs(u - (.5 - x / 16.)) > 2e-6
                    or abs(v - (.5 - south / 16.)) > 2e-6
                    or (face['texture'] == 0x0400020E and x > south + 2e-5)):
                matched = False
                break
        if matched:
            return True
    return False


def _native_dd_fragment(face):
    """Native geometry is measured in its true city cell, not its model host."""
    from .ramp_verify import _native_fragment
    for column, row in OWNED_CELLS:
        if column + row not in (0, 1):
            continue
        if not all(abs(p[0] - 16. * column) <= 10. and abs(p[1] + 16. * row) <= 10.
                   for p in face['points']):
            continue
        local = tuple((p[0] - 16. * column, p[2], -p[1] - 16. * row, *uv)
                      for p, uv in zip(face['points'], face['uv']))
        if _native_fragment(local, face['material'], preserve_uv=face['texture'] != 0x5713000E):
            return True
    return False


def check_projection(faces):
    """Actual authored faces stay in31cells; only pinned native ends overhang."""
    from .assembly_verify import _projected_area_in_cell
    outside, by_key = set(), defaultdict(set)
    certified = 0
    for face in faces:
        triangle = face['points']
        columns = range(math.floor((min(p[0] for p in triangle) + 8.) / 16.),
                        math.floor((max(p[0] for p in triangle) + 8.) / 16.) + 1)
        rows = range(math.floor((8. - max(p[1] for p in triangle)) / 16.),
                     math.floor((8. - min(p[1] for p in triangle)) / 16.) + 1)
        unowned = []
        for column in columns:
            for row in rows:
                cell = column, row
                area = _projected_area_in_cell(triangle, cell)
                if area <= 1e-7:
                    continue
                by_key[face['geometry_key']].add(cell)
                if cell not in OWNED_CELLS:
                    unowned.append(cell)
        if unowned:
            require(_native_dd_fragment(face),
                    'Parallel authored model projects outside its approved31cells without pinned native donor provenance')
            certified += 1
            outside.update(unowned)
    return {'passed': True, 'approved_owned_cells': 31,
            'unowned_native_end_projection_cells': [list(cell) for cell in sorted(outside)],
            'pinned_native_overhang_triangles_checked': certified,
            'actual_model_projection_cells_by_function': {key: [list(cell) for cell in sorted(cells)]
                                                          for key, cells in sorted(by_key.items())},
            'scope': 'Positive-area actual indexed projections distinguish model drawing from whole-cell traffic ownership. Native end overhangs retain audited donor geometry/material, and non-DD donor UVs; complete road support is checked separately.'}


def _assembly_ground_mouth_profile(pieces, scene):
    """Select the explicit revision without relabelling retained old builds."""
    terminals = [pieces[row['piece_id']] for row in scene['placements']
                 if pieces[row['piece_id']]['geometry_key'] in
                 ('parallel-northwest-terminal', 'parallel-southeast-terminal')]
    require(len(terminals) == 2, 'Parallel assembly needs its two ground terminals')
    profiles = {piece.get('engineering', {}).get('ground_mouth_profile') for piece in terminals}
    require(profiles in ({None}, {GROUND_MOUTH_PROFILE}),
            'Parallel Avenue terminals must declare one consistent ground-mouth revision')
    return next(iter(profiles))


def _assembly_highway_slip_profile(pieces, scene):
    """Every whole-cell owner must dispatch the same explicit traffic revision."""
    profiles = {pieces[row['piece_id']].get('engineering', {}).get('highway_slip_profile')
                for row in scene['placements']}
    require(profiles in ({None}, {HIGHWAY_SLIP_PROFILE}),
            'Parallel assembly must declare one consistent highway-slip revision')
    return next(iter(profiles))


def _ground_widths(ramp, profile):
    """Independent literal widths at the frozen PATH samples, in travel order.

    Outward means from the six-metre grade cut towards the Avenue. Entries
    reverse that station direction; all elevated and graded points stay six
    metres wide. Only the flat right turn and its native-lane collar taper.
    """
    require(profile in (None, GROUND_MOUTH_PROFILE), 'Unknown parallel ground-mouth profile')
    result = [6.] * len(ramp['points'])
    if profile is None:
        return result
    turn = next(row for row in ramp['segments'] if row['kind'] == 'ground-right-quarter-turn')
    cut = turn['start_index'] if ramp['direction'] == 'off' else turn['end_index']
    outward = range(cut, len(result)) if ramp['direction'] == 'off' else range(cut, -1, -1)
    previous, distance = None, 0.
    for at in outward:
        point = ramp['points'][at]
        require(abs(point[2]) <= 1e-8, 'Ground-mouth taper extends onto a graded or elevated surface')
        if previous is not None:
            distance += math.dist(ramp['points'][previous][:2], point[:2])
        fraction = min(1., distance / 3.)
        smooth = fraction * fraction * (3. - 2. * fraction)
        result[at] = 6. - 2.5 * smooth
        previous = at
    return result


@lru_cache(maxsize=2)
def _ground_reference(profile):
    """Independent flat-ribbon triangles; no model writer is imported."""
    faces = []
    for ramp in approved_candidate()['routes']:
        points, normals, widths = ramp['points'], _frames(ramp['points']), _ground_widths(ramp, profile)
        for at, (a, b) in enumerate(zip(points, points[1:])):
            if abs(a[2]) > 1e-8 or abs(b[2]) > 1e-8:
                continue
            for low, high in ((-1., 0.), (0., 1.)):
                quad = [(p[0] + side * half * n[0], p[1] + side * half * n[1], 0.)
                        for p, n, half, side in
                        ((a, normals[at], widths[at] / 2., low),
                         (a, normals[at], widths[at] / 2., high),
                         (b, normals[at + 1], widths[at + 1] / 2., high),
                         (b, normals[at + 1], widths[at + 1] / 2., low))]
                faces.extend({'points': tuple(triangle)} for triangle in
                             ((quad[0], quad[1], quad[2]), (quad[0], quad[2], quad[3])))
    return _FaceIndex(faces)


def check_ground_mouths(faces, *, profile=GROUND_MOUTH_PROFILE):
    """Check affirmative tapered pavement and exposed sidewalk-line collars.

    Actual flat MIS surfaces must stay within the independently reconstructed
    envelope, and seven continuous longitudinal witnesses plus both exact
    edge samples require real saved pavement. Native Avenue faces cannot
    conceal a missing authored ramp. Each driveway's unavoidable sidewalk
    crossing is retained; only its Avenue-parallel collar must leave the
    measured pedestrian centreline outside the static asphalt.
    """
    require(profile == GROUND_MOUTH_PROFILE, 'Narrow-mouth checks need the explicit revised profile')
    from .modular_assembly_verify import _triangle_distance
    from .ramp_verify import _interval
    ground = [face for face in faces if face['texture'] == 0x5712000E and face['upward']
              and all(abs(point[2]) <= 1e-8 for point in face['points'])]
    require(ground, 'Parallel ground mouths contain no actual saved MIS pavement')
    index, reference = _FaceIndex(ground), _ground_reference(profile)
    maximum, samples, edges, spans = 0., 0, 0, 0
    precision = {'admitted_road_encoding_spans': 0, 'maximum_admitted_along_route_span_m': 0.,
                 'maximum_sampled_actual_face_distance_m': 0.}
    for face in ground:
        points = face['points']
        witnesses = [*points, tuple(sum(p[a] for p in points) / 3. for a in range(3))]
        witnesses += [tuple((a[k] + b[k]) / 2. for k in range(3))
                      for a, b in zip(points, points[1:] + points[:1])]
        for point in witnesses:
            nearby = reference.nearby(point, margin=4e-6)
            distance = min((_triangle_distance(point, other['points']) for other in nearby), default=math.inf)
            require(distance <= 4e-6,
                    f'Parallel ground asphalt exceeds its independently approved tapered mouth: {point}')
            maximum, samples = max(maximum, distance), samples + 1
    collars = []
    for ramp in approved_candidate()['routes']:
        points, normals, widths = ramp['points'], _frames(ramp['points']), _ground_widths(ramp, profile)
        for fraction in (-2.9 / 3., -2.17 / 3., -1.25 / 3., 0., 1.25 / 3., 2.17 / 3., 2.9 / 3.):
            spine = [(p[0] + fraction * width / 2. * normal[0],
                      p[1] + fraction * width / 2. * normal[1], p[2])
                     for p, normal, width in zip(points, normals, widths)]
            for a, b in zip(spine, spine[1:]):
                if abs(a[2]) > 1e-8 or abs(b[2]) > 1e-8:
                    continue
                require(_continuous_support(a, b, index.nearby(a, b), precision,
                                            ground_mouth_profile=profile),
                        f'Parallel tapered ground mouth lacks continuous authored pavement: {ramp["id"]} {a}->{b}')
                spans += 1
        for point, normal, width in zip(points, normals, widths):
            if abs(point[2]) > 1e-8:
                continue
            for sign in (-1., 1.):
                edge = point[0] + sign * width / 2. * normal[0], point[1] + sign * width / 2. * normal[1], 0.
                require(_near_surface(edge, index, tolerance=.002, desired_normal=(0., 0., 1.)),
                        f'Parallel tapered ground mouth lacks its exact width edge: {ramp["id"]} {edge}')
                edges += 1
        collar = next(row for row in ramp['segments'] if row['kind'] == 'native-avenue-lane-collar')
        first, last = points[collar['start_index']], points[collar['end_index']]
        u = math.copysign(15.3 / math.sqrt(2.), _uv(first)[0])
        a, b = [(4. + (u - _uv(p)[1]) / math.sqrt(2.),
                 -4. + (u + _uv(p)[1]) / math.sqrt(2.), 0.) for p in (first, last)]
        length = math.dist(a, b)
        intervals = [interval for face in index.nearby(a, b) if
                     (interval := _interval(a, b, face['points'])) is not None]
        covered, reached = 0., 0.
        for low, high in sorted(intervals):
            covered += max(0., high - max(low, reached))
            reached = max(reached, high)
        require(covered * length <= 2e-6,
                f'Parallel static Avenue-parallel collar covers its pedestrian centreline: {ramp["id"]}')
        collars.append({'ramp_id': ramp['id'], 'pedestrian_axis_u_m': u,
                        'static_asphalt_overlap_m': covered * length,
                        'car_to_pedestrian_centre_distance_m': 4.1 / math.sqrt(2.),
                        'nominal_asphalt_edge_to_pedestrian_centre_m': 4.1 / math.sqrt(2.) - 1.75})
    return {'passed': True, 'profile': profile, 'grade_cut_width_m': 6., 'Avenue_mouth_width_m': 3.5,
            'taper_plan_length_m': 3., 'taper': 'cubic smoothstep; travel order reversed for entries',
            'continuous_flat_pavement_width_witnesses': spans, 'exact_width_edge_samples': edges,
            'actual_ground_envelope_samples': samples, 'maximum_envelope_distance_m': maximum,
            'envelope_encoding_distance_bound_m': 4e-6, 'edge_sample_distance_bound_m': .002,
            'pedestrian_parallel_collars': collars,
            'unavoidable_driveway_crossings_removed': False,
            'scope': 'Actual saved flat MIS triangles, finite continuous width lines, exact nominal-edge samples, and no static asphalt along the four Avenue-parallel pedestrian collars. Complete sidewalk surface width and game texture selection are not established.'}


def check_model_union(faces, routes, *, ground_mouth_profile=None, highway_slip_profile=None):
    """Check continuous car corridors and each explicitly declared road width."""
    from .ramp_verify import _intrudes
    index = _FaceIndex(faces)
    field = check_wheeltrack_vertices(faces, highway_slip_profile=highway_slip_profile)
    precision = {'euclidean_distance_limit_m': 2e-6, 'admitted_road_encoding_spans': 0,
                 'maximum_admitted_along_route_span_m': 0., 'maximum_sampled_actual_face_distance_m': 0.}
    segments, grade = 0, 0.
    for route in routes:
        if route['transport'] != 1:
            continue
        for first, last in zip(route['points'], route['points'][1:]):
            candidates = index.nearby(first, last, 1.25)
            require(_continuous_support(first, last, candidates, precision,
                                        ground_mouth_profile=ground_mouth_profile),
                    f'Parallel saved model union lacks continuous car pavement: {first}->{last}')
            require(not any(_intrudes(first, last, face['points'], 1.25, 3.8) for face in candidates),
                    f'Parallel saved solid face intrudes into actual car corridor: {first}->{last}')
            grade = max(grade, abs(last[2] - first[2]) / math.dist(first[:2], last[:2]))
            segments += 1
    require(grade <= .30001, 'Parallel saved car grade exceeds the experimental bound')
    ribbon_segments, underside, barrier, native_boundary_spans = 0, 0, 0, 0
    barrier_profile = ((0., 0.), (.21875, .328125), (.265625, 1.390625),
                       (.5625, 1.390625), (.625, .328125), (.828125, 0.))
    for ramp in approved_candidate()['routes']:
        points = ramp['points']
        normals = _frames(points)
        widths = _ground_widths(ramp, ground_mouth_profile)
        for lateral in (-2.9, -2.17, -1.25, 0., 1.25, 2.17, 2.9):
            spine = [(p[0] + lateral * width / 6. * n[0], p[1] + lateral * width / 6. * n[1], p[2])
                     for p, n, width in zip(points, normals, widths)]
            for first, last in zip(spine, spine[1:]):
                for cell, fragments in _split_points([first, last]).items():
                    for fragment in fragments:
                        a, b = fragment[0], fragment[-1]
                        if (cell not in OWNED_CELLS and first[2] == last[2] == ramp['height_m']
                                and all(abs(_uv(p)[1]) <= 8. + 1e-5 for p in (a, b))):
                            # A diagonal native lane port is a city-edge cut,
                            # not a perpendicular road-width cut. The ordinary
                            # highway neighbour supplies the outer half-width
                            # before that assembly boundary; no authored ramp
                            # overhang is excused here.
                            native_boundary_spans += 1
                            continue
                        require(_continuous_support(a, b, index.nearby(a, b), precision,
                                                    ground_mouth_profile=ground_mouth_profile),
                                f'Parallel saved declared-width road has a continuous width gap on {ramp["id"]}: {a}->{b}')
                        ribbon_segments += 1
        # Sample every metre, including both functional physical boundaries.
        # Continuous spine/width checks above are distinct from these bounded
        # concrete-shell samples; neither establishes structural capacity.
        next_station, distance = 0., 0.
        for position, (point, normal) in enumerate(zip(points, normals)):
            if position:
                distance += math.dist(points[position - 1][:2], point[:2])
            if distance + 1e-9 < next_station and position != len(points) - 1:
                continue
            next_station = distance + 1.
            if point[2] > 1.01 and ramp['side'] * _uv(point)[1] > 11.01:
                for lateral in (-2.9, 0., 2.9):
                    sample = point[0] + lateral * normal[0], point[1] + lateral * normal[1], point[2] - 1.
                    require(_near_surface(sample, index, concrete=True, desired_normal=(0., 0., -1.)),
                            f'Parallel ramp lacks its one-metre underside: {ramp["id"]} {sample}')
                    underside += 1
            if point[2] <= .03:
                continue
            taper = min(1., point[2] / 1.5)
            for side in (-1, 1):
                for (a, h), (b, j) in zip(barrier_profile, barrier_profile[1:]):
                    inset, height = (a + b) / 2., (h + j) / 2.
                    lateral = side * (3. - inset)
                    sample = (point[0] + lateral * normal[0], point[1] + lateral * normal[1],
                              point[2] + taper * height)
                    if ramp['side'] * _uv(sample)[1] < 8. - inset - .0001:
                        continue
                    desired = side * (j - h) * normal[0], side * (j - h) * normal[1], b - a
                    require(_near_surface(sample, index, concrete=True, desired_normal=desired),
                            f'Parallel ramp lacks a complete native barrier profile: {ramp["id"]} {sample}')
                    barrier += 1
    return {'passed': True, 'continuous_car_segments_checked': segments,
            'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
            'continuous_ramp_width_segments_checked': ribbon_segments,
            'ramp_width_m': 6. if ground_mouth_profile is None else None,
            'elevated_and_grade_ramp_width_m': 6.,
            'ground_mouth_width_profile': ground_mouth_profile or 'retained-six-metre-ground-mouth',
            'native_external_boundary_width_spans_requiring_highway_neighbour': native_boundary_spans,
            'maximum_saved_grade_percent': 100. * grade,
            'road_support_encoding_precision': precision, 'wheeltrack_field': field,
            'underside_samples_checked': underside, 'barrier_profile_samples_checked': barrier,
            'shell_sample_tolerance_m': .002,
            'scope': 'Actual indexed triangle intervals for car support, seven longitudinal width lines per ramp, exact prism/triangle car-corridor intersections, and bounded underside/barrier-profile samples. No structural capacity or game observation is established.'}


def check_supports(faces):
    """Locate each approved sloping 0.8 m square pier shell in actual faces."""
    index = _FaceIndex(faces)
    samples = 0
    for ramp in approved_candidate()['routes']:
        for support in ramp['supports']:
            corners = [(*xy, height) for xy, height in
                       zip(support['footprint_en'], support['top_corner_heights_m'])]
            for point in corners:
                outward = point[0] - support['centre_enh'][0], point[1] - support['centre_enh'][1], 0.
                require(_near_surface(point, index, concrete=True, desired_normal=outward),
                        f'Parallel support does not meet its sloping underside: {ramp["id"]}')
                samples += 1
            for a, b in zip(corners, corners[1:] + corners[:1]):
                for fraction in (.1, .5, .9):
                    for height_fraction in (0., .25, .75, 1.):
                        point = (a[0] + fraction * (b[0] - a[0]),
                                 a[1] + fraction * (b[1] - a[1]),
                                 height_fraction * (a[2] + fraction * (b[2] - a[2])))
                        outward = point[0] - support['centre_enh'][0], point[1] - support['centre_enh'][1], 0.
                        require(_near_surface(point, index, concrete=True, desired_normal=outward),
                                f'Parallel support lacks a complete grounded shell: {ramp["id"]} {point}')
                        samples += 1
    native_samples = 0
    for column, row in ((-1, 1), (-1, 2), (1, -1), (2, -1)):
        centre = 16. * column, -16. * row
        for dx, dy in ((-.4, 0.), (.4, 0.), (0., -.4), (0., .4)):
            for height in (0., 3., 6.5, 7.5, 10., 14., 15.):
                point = centre[0] + dx, centre[1] + dy, height
                require(_near_surface(point, index, concrete=True, desired_normal=(dx, dy, 0.)),
                        'A parallel native centre pier is missing its grounded outward-facing span to both decks')
                native_samples += 1
    return {'passed': True, 'authored_ramp_piers_checked': 4, 'pier_half_width_m': .4,
            'actual_face_samples_checked': samples, 'native_centre_piers_checked': 4,
            'native_pier_samples_checked': native_samples, 'outward_face_winding_checked': True,
            'structural_capacity_tested': False}


def check_straight_native_decks_and_mouths(faces):
    """Sample both16m deck surfaces and all forty real barrier handoffs."""
    from .modular_assembly_verify import _triangle_distance
    index = _FaceIndex(faces)
    decks, mouths = 0, 0
    for station in range(-90, 91, 2):
        for lateral in (-7.9, -6., -4.5, -2.2627417, 0., 2.2627417, 4.5, 6., 7.9):
            point_xy = 4. + (station - lateral) / math.sqrt(2.), -4. + (station + lateral) / math.sqrt(2.)
            cell = math.floor((point_xy[0] + 8.) / 16.), math.floor((8. - point_xy[1]) / 16.)
            if cell not in OWNED_CELLS:
                continue
            for height in (7.5, 15.):
                point = *point_xy, height
                require(any(face['texture'] == 0x5713000E and face['upward']
                            and _triangle_distance(point, face['points']) <= .002
                            for face in index.nearby(point)),
                        f'Parallel straight stem loses a native16m deck surface: {point}')
                decks += 1
    profile = ((0., 0.), (.21875, .328125), (.265625, 1.390625),
               (.5625, 1.390625), (.625, .328125), (.828125, 0.))
    for ramp in approved_candidate()['routes']:
        points = ramp['points'] if ramp['direction'] == 'off' else list(reversed(ramp['points']))
        normals = _frames(points)
        flat = [(point, normal) for point, normal in zip(points, normals)
                if abs(point[2] - ramp['height_m']) <= 1e-7]
        for road_side in (-1, 1):
            for (a, h), (b, j) in zip(profile, profile[1:]):
                inset, raised = (a + b) / 2., (h + j) / 2.
                curve = [(p[0] + road_side * (3. - inset) * n[0],
                          p[1] + road_side * (3. - inset) * n[1], p[2] + raised) for p, n in flat]
                crossing = None
                for first, last in zip(curve, curve[1:]):
                    before = ramp['side'] * _uv(first)[1] - (8. - inset)
                    after = ramp['side'] * _uv(last)[1] - (8. - inset)
                    if before <= 0. <= after and after - before > 1e-12:
                        fraction = -before / (after - before)
                        crossing = tuple(x + fraction * (y - x) for x, y in zip(first, last))
                        break
                require(crossing is not None and _near_surface(crossing, index, concrete=True),
                        'Parallel highway/ramp mouth leaves an empty native barrier-profile handoff')
                mouths += 1
    return {'passed': True, 'native_deck_surface_samples_checked': decks,
            'native_deck_heights_m': [7.5, 15.], 'native_deck_width_m': 16.,
            'native_barrier_mouth_profile_samples_checked': mouths,
            'surface_sample_tolerance_m': .002,
            'scope': 'Bounded samples of the real indexed DD surfaces and all four mouths, with five bands on both barrier sides; continuous car corridors and actual source-preservation checks remain separate.'}


def check_highway_ramp_uv_seams(faces):
    """Measure actual DD/MIS wear continuation at the four physical mouths."""
    from .ramp_verify import _barycentric
    index = _FaceIndex(faces)

    def sample(point, texture):
        for face in index.nearby(point, margin=2e-5):
            if face['texture'] != texture or not face['upward']:
                continue
            weights = _barycentric(point, face['points'])
            if weights is None or min(weights) < -1e-7:
                continue
            height = sum(w * p[2] for w, p in zip(weights, face['points']))
            if abs(height - point[2]) > 2e-6:
                continue
            return tuple(sum(w * uv[a] for w, uv in zip(weights, face['uv'])) for a in (0, 1))
        raise ValueError('A saved native wheeltrack seam lacks its actual indexed DD or MIS pavement')

    controls = []
    for ramp in approved_candidate()['routes']:
        outward = ramp['points'] if ramp['direction'] == 'off' else list(reversed(ramp['points']))
        crossing = None
        for first, last in zip(outward, outward[1:]):
            before, after = ramp['side'] * _uv(first)[1], ramp['side'] * _uv(last)[1]
            if before <= 8. <= after and after - before > 1e-12:
                fraction = (8. - before) / (after - before)
                crossing = _uv(tuple(x + fraction * (y - x) for x, y in zip(first, last)))[0]
                break
        require(crossing is not None, 'Approved ramp has no physical native deck-edge mouth')
        for delta in (-2., -1., 0., 1., 2.):
            uv = []
            for q, texture in ((8. - 2e-5, 0x5713000E), (8. + 2e-5, 0x5712000E)):
                u, v = crossing + delta, ramp['side'] * q
                point = 4. + (u - v) / math.sqrt(2.), -4. + (u + v) / math.sqrt(2.), ramp['height_m']
                uv.append(sample(point, texture))
            dd, mis = uv
            column = 128. * mis[0] - .5
            target = (min(95., max(65., column + 16. + min(1., max(0., (column - 68.) / 6.)))) + .5) / 128.
            u_error = abs(dd[0] - target)
            phase = abs((dd[1] - mis[1] + .5) % 1. - .5)
            require(u_error <= 1e-4 and phase <= .001,
                    f'Saved highway/ramp native wear seam changes transverse crop or longitudinal phase: {ramp["id"]} U={u_error}, V={phase}')
            controls.append({'ramp_id': ramp['id'], 'highway_axis_offset_m': delta,
                             'dd_uv': list(dd), 'mis_uv': list(mis),
                             'transverse_uv_error': u_error, 'phase_error_repeats': phase})
    return {'passed': True, 'actual_saved_dd_mis_seam_pairs_checked': len(controls),
            'transverse_uv_tolerance': 1e-4, 'phase_tolerance_repeats': .001,
            'maximum_transverse_uv_error': max(row['transverse_uv_error'] for row in controls),
            'maximum_phase_error_repeats': max(row['phase_error_repeats'] for row in controls),
            'controls': controls, 'native_rgb_or_game_filtering_tested': False}


def check_physical_cuts(faces):
    """Keep complete physical joins distinct from whole-cell traffic ports."""
    by_key = defaultdict(list)
    for face in faces:
        by_key[face['geometry_key']].append(face)
    indices = {key: _FaceIndex(group) for key, group in by_key.items()}
    checked, overhang = 0, set()
    profile = ((0., 0.), (.21875, .328125), (.265625, 1.390625),
               (.5625, 1.390625), (.625, .328125), (.828125, 0.))
    for ramp in approved_candidate()['routes']:
        stem = ramp['deck'] + ('-exit' if ramp['direction'] == 'off' else '-entry')
        points, normals = ramp['points'], _frames(ramp['points'])
        segments = ramp['segments']
        for before, after in zip(segments, segments[1:]):
            before_kind, after_kind = before['kind'], after['kind']
            departure_grade = {before_kind, after_kind} == {'flat-high-departure', 'straight-parallel-descent'}
            grade_terminal = {before_kind, after_kind} == {'straight-parallel-descent', 'ground-right-quarter-turn'}
            if not (departure_grade or grade_terminal):
                continue
            before_key = (stem + '-departure' if before_kind == 'flat-high-departure' else stem + '-grade'
                          if before_kind == 'straight-parallel-descent' else
                          'northwest-terminal' if ramp['deck'] == 'lower' else 'southeast-terminal')
            after_key = (stem + '-departure' if after_kind == 'flat-high-departure' else stem + '-grade'
                         if after_kind == 'straight-parallel-descent' else
                         'northwest-terminal' if ramp['deck'] == 'lower' else 'southeast-terminal')
            at = before['end_index']
            require(at == after['start_index'], 'Approved physical modules have an inconsistent source cut')
            for key, neighbour in ((before_key, at - 1), (after_key, at + 1)):
                point = points[at]
                other = points[neighbour]
                length = math.dist(point[:2], other[:2])
                fraction = .001 / length
                centre = tuple(a + fraction * (b - a) for a, b in zip(point, other))
                normal = tuple(a + fraction * (b - a) for a, b in zip(normals[at], normals[neighbour]))
                for lateral in (-2.9, -2.17, -1.25, 0., 1.25, 2.17, 2.9):
                    sample = centre[0] + lateral * normal[0], centre[1] + lateral * normal[1], centre[2]
                    require(_near_surface(sample, indices[key], desired_normal=(0., 0., 1.)),
                            f'Parallel physical seam lacks its separately owned full pavement: {key} {sample}')
                    checked += 1
                if centre[2] > 1.:
                    for lateral in (-2.9, 0., 2.9):
                        sample = centre[0] + lateral * normal[0], centre[1] + lateral * normal[1], centre[2] - 1.
                        require(_near_surface(sample, indices[key], concrete=True, desired_normal=(0., 0., -1.)),
                                f'Parallel physical seam lacks its separately owned underside: {key}')
                        checked += 1
                    for side in (-1, 1):
                        for (a, h), (b, j) in zip(profile, profile[1:]):
                            lateral, height = side * (3. - (a + b) / 2.), (h + j) / 2.
                            sample = centre[0] + lateral * normal[0], centre[1] + lateral * normal[1], centre[2] + height
                            desired = side * (j - h) * normal[0], side * (j - h) * normal[1], b - a
                            require(_near_surface(sample, indices[key], concrete=True, desired_normal=desired),
                                    f'Parallel physical seam lacks its separately owned complete barrier: {key}')
                            checked += 1
                source_cell = math.floor((centre[0] + 8.) / 16.), math.floor((8. - centre[1]) / 16.)
                if source_cell not in PARTITIONS[key]:
                    overhang.add((key, source_cell))
    return {'passed': True, 'functional_physical_interfaces_checked': 8,
            'separate_owner_pavement_underside_barrier_samples': checked,
            'checked_physical_cuts_outside_traffic_owner_cells': [
                {'geometry_key': key, 'source_cell': list(cell)} for key, cell in sorted(overhang)],
            'physical_profiles_and_city_tile_path_ports_checked_separately': True}


def verify_assembly_resources(manifest, scene, piece_resources, *, inspect_models=True):
    from .assembly_verify import decode_placed_routes
    require(scene.get('id', SUBJECT) == SUBJECT, 'Parallel verification received another assembly identity')
    pieces = {piece['id']: piece for piece in manifest['pieces']}
    from .ddrhw_connections import check_selected_helper_collisions
    helper_report = check_selected_helper_collisions(pieces, scene)
    owners, shift = check_owned_cells(pieces, scene)
    ground_profile = _assembly_ground_mouth_profile(pieces, scene)
    slip_profile = _assembly_highway_slip_profile(pieces, scene)
    for identifier in {owner['piece_id'] for owner in owners.values()}:
        check_paths(piece_resources[identifier], pieces[identifier])
    routes = decode_placed_routes(owners, piece_resources)
    paths, seams = check_saved_routes(routes)
    rotations = [{'quarter_turns_ccw': 0, **paths}]
    # Rotate actual decoded resources, tile edges, city cells, and the
    # separately measured native port contract together. Controller rule
    # inspection remains part of verify_build rather than a geometry claim.
    for turns in (1, 2, 3):
        rotated = []
        for route in routes:
            centre = _rotate((route['cell'][0], -route['cell'][1], 0.), turns)
            rotated.append({**route, 'points': [_rotate(p, turns) for p in route['points']],
                            'entry': (route['entry'] - turns) % 4,
                            'exit': (route['exit'] - turns) % 4,
                            'cell': (round(centre[0]), round(-centre[1]))})
        rotations.append({'quarter_turns_ccw': turns, **check_saved_routes(rotated, turns=turns)[0]})
    if inspect_models:
        faces = []
        for owner in owners.values():
            raw = piece_resources[owner['piece_id']][*S3D, owner['tile'] + 4]
            faces.extend({**face, 'geometry_key': owner['geometry_key']} for face in
                         _decode_faces(raw, owner['local_cell'], origin=owner['origin']))
        models = check_model_union(faces, routes, ground_mouth_profile=ground_profile,
                                   highway_slip_profile=slip_profile)
        supports, cuts = check_supports(faces), check_physical_cuts(faces)
        ground_mouths = (check_ground_mouths(faces, profile=ground_profile) if ground_profile else
                        {'passed': True, 'profile': 'retained-six-metre-ground-mouth',
                         'narrowed_sidewalk_collar_claimed': False})
        native = check_straight_native_decks_and_mouths(faces)
        projection = check_projection(faces)
        uv_seams = check_highway_ramp_uv_seams(faces)
        slip_lanes = (check_highway_slip_lanes(faces, profile=slip_profile) if slip_profile else
                      {'passed': True, 'profile': 'retained-approved-departure',
                       'revised_auxiliary_lane_claimed': False})
    else:
        models = supports = cuts = native = projection = uv_seams = ground_mouths = slip_lanes = {'passed': False, 'status': 'not-run'}
    return {'schema_version': 1, 'subject_id': SUBJECT,
            **({'native_dd_outside_approaches': helper_report} if helper_report else {}),
            'saved_resource_checks_passed': bool(inspect_models),
            'saved_path_checks_passed': True,
            'saved_ownership_checks_passed': True,
            'saved_path_and_construction_checks_passed': False,
            'package_construction_checks': 'not-run',
            'construction': {'unique_owned_cells': 31, 'placements': 15,
                             'bounding_rectangle_tiles': [8, 8], 'translation_east_north_m': list(shift)},
            'paths': paths, 'proper_rotation_paths': rotations, 'model_union': models, 'supports': supports,
            'highway_slip_profile': slip_profile or 'retained-approved-departure',
            'highway_slip_lanes': slip_lanes,
            'physical_functional_cuts': cuts,
            'ground_mouths': ground_mouths,
            'straight_native_decks_and_mouths': native,
            'actual_model_projection': projection,
            'native_wheeltrack_seam_uv': uv_seams,
            'approval_sha256': APPROVAL_SHA256, 'game_operation': 'unverified',
            'limits': ['Software does not establish native placement, adaptive sidewalk appearance, visible traffic, or game shadows.',
                       'Barrier, underside, and pier shells receive bounded samples, not structural-load proof.']}


def verify_assembly(output, scene, *, evidence_path=None, verify_package=True):
    from scp.verify import strict_dbpf
    output = Path(output).resolve()
    if evidence_path is not None:
        require(not Path(evidence_path).resolve().is_relative_to(output),
                'Parallel assembly evidence must remain outside its saved build')
    if verify_package:
        from scp.verify import verify_build
        verify_build(output, write_report=False)
    raw = (output / 'manifest.json').read_bytes()
    manifest = json.loads(raw)
    files, resources, fingerprints = {r['path']: r for r in manifest['files']}, {}, {}
    for piece in manifest['pieces']:
        path = piece['asset_file']
        data = (output / path).read_bytes()
        require(len(data) == files[path]['bytes'] and hashlib.sha256(data).hexdigest() == files[path]['sha256'],
                'A parallel source DAT differs from its saved manifest')
        resources[piece['id']], fingerprints[path] = strict_dbpf(data), files[path]['sha256']
    report = verify_assembly_resources(manifest, scene, resources)
    if verify_package:
        report['saved_path_and_construction_checks_passed'] = True
        report['package_construction_checks'] = 'passed-actual-saved-controller-rules'
    report['source'] = {'manifest_sha256': hashlib.sha256(raw).hexdigest(), 'asset_files': fingerprints,
                        'actual_saved_dat_resources': True,
                        'scene_sha256': hashlib.sha256(json.dumps(scene, sort_keys=True, separators=(',', ':')).encode()).hexdigest()}
    if evidence_path is not None:
        target = Path(evidence_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(report, indent=2) + '\n')
    return report


def verify_native_visual_transfer(reference_world, candidate_world):
    """Compare actual independently saved resources before and after host moves.

    Native DD pavement, slip paint, and the four native centre piers retain
    complete triangle winding, UVs, and raw native materials. City-frame
    float32 fingerprints are reported separately from the bounded additional
    local-coordinate rounding caused by a16m host-origin translation.
    """
    require(set(reference_world) == set(candidate_world) == OWNED_CELLS,
            'Visual transfer inputs must contain the exact approved31cell world')

    def selected(world):
        triangles, hashes = [], {}
        for cell, (model, _path) in sorted(world.items()):
            hashes[str(cell)] = hashlib.sha256(model).hexdigest()
            for face in _decode_faces(model, origin=(16. * cell[0], -16. * cell[1])):
                pier = face['texture'] == 0x5EB4BEEE and any(all(
                    abs(p[0] - 16. * column) <= .40001 and abs(p[1] + 16. * row) <= .40001
                    and -.00001 <= p[2] <= 15.00001 for p in face['points'])
                    for column, row in ((-1, 1), (-1, 2), (1, -1), (2, -1)))
                if face['texture'] != 0x5713000E and not pier:
                    continue
                vertices = tuple((*point, *uv) for point, uv in zip(face['points'], face['uv']))
                vertices = min(vertices[index:] + vertices[:index] for index in range(3))
                triangles.append((face['material_sha256'], vertices))
        return triangles, hashes

    before, reference_hashes = selected(reference_world)
    after, candidate_hashes = selected(candidate_world)
    require(len(before) == len(after), 'Native visual transfer adds or removes an actual DD, paint, or pier triangle')
    exact_key = lambda triangle: (triangle[0], tuple(struct.pack('<5f', *vertex) for vertex in triangle[1]))
    exact = Counter(map(exact_key, before)) == Counter(map(exact_key, after))
    buckets = defaultdict(list)
    for material, vertices in before:
        buckets[material, tuple(p[3:] for p in vertices)].append(vertices)
    maximum, changed = 0., 0
    for material, vertices in after:
        candidates = buckets[material, tuple(p[3:] for p in vertices)]
        match = next((expected for expected in candidates if all(
            math.dist(a[:3], b[:3]) <= 2e-6 for a, b in zip(vertices, expected))), None)
        require(match is not None, 'Native visual transfer changes a complete material, UV, winding, or physical face beyond its measured float32 envelope')
        candidates.remove(match)
        for actual, expected in zip(vertices, match):
            distance = math.dist(actual[:3], expected[:3])
            maximum = max(maximum, distance)
            changed += actual[:3] != expected[:3]
    require(not any(buckets.values()), 'Native visual transfer leaves unmatched original triangles')
    return {'passed': True, 'triangles_checked': len(before),
            'common_city_frame_float32_triangle_multiset_exact': exact,
            'raw_material_uv_and_winding_multiset_exact': True,
            'local_origin_translation_position_limit_m': 2e-6,
            'maximum_measured_city_frame_vertex_difference_m': maximum,
            'vertex_positions_with_additional_local_float32_rounding': changed,
            'reference_model_sha256_by_source_cell': reference_hashes,
            'candidate_model_sha256_by_source_cell': candidate_hashes,
            'scope': 'Actual native DD and slip-paint triangles, plus four explicitly bounded centre piers. Intentionally repaired MIS ground and barrier-bevel UVs are outside this preservation mask.'}


def world_resources_from_build(output):
    """Read all31actual canonical DAT cells and bind their saved manifest."""
    from scp.verify import strict_dbpf
    output = Path(output)
    raw = (output / 'manifest.json').read_bytes()
    manifest = json.loads(raw)
    files, result, assets = {row['path']: row for row in manifest['files']}, {}, {}
    for piece in manifest['pieces']:
        origin = _source_origin(piece)
        path = piece['asset_file']
        archive = (output / path).read_bytes()
        require(len(archive) == files[path]['bytes']
                and hashlib.sha256(archive).hexdigest() == files[path]['sha256'],
                'A preservation DAT differs from its actual saved manifest')
        resources = strict_dbpf(archive)
        check_paths(resources, piece)
        assets[path] = files[path]['sha256']
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            world = cell[0] + origin[0], cell[1] + origin[1]
            require(world not in result, 'Preservation input repeats a city cell')
            result[world] = resources[*S3D, int(tile, 16)], resources[*PATH, int(tile, 16)]
    require(set(result) == OWNED_CELLS, 'Preservation build lacks the exact31city cells')
    return result, {'manifest_sha256': hashlib.sha256(raw).hexdigest(), 'asset_files': assets,
                    'actual_saved_dat_resources': True}
