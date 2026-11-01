"""Independent saved-resource proof for the complementary parallel diamond.

The B compiler and layout writer are deliberately not imported. The accepted
reference routes, literal native lane measurements, and the measured (8, 8)
metre shift establish expectations before any candidate is decoded.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import re

from scp.dbpf import decompress, require
from scp.track_paths import PATH, S3D

from . import parallel_verify as reference

PREFIX = 'highway_ddrhw_parallel_b_'
SUBJECT = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b'
TRANSLATION_M = (8., 8.)
TOLERANCE = 4e-5
NEIGHBOURS = ((-1, 0), (0, -1), (1, 0), (0, 1))
# Reviewed against independently sliced accepted routes and their real cuts.
# This literal contract is separate from, and not imported by, the writer.
PARTITIONS = {
    'crossing': ((0, 0), (1, 0), (1, -1)),
    'northwest-terminal': ((-1, -1), (0, -1), (0, -2)),
    'southeast-terminal': ((1, 1), (2, 0)),
    'lower-exit-slip': ((4, -4), (3, -3)),
    'lower-entry-slip': ((-2, 2), (-3, 3)),
    'upper-exit-slip': ((-3, 4), (-2, 3), (-1, 2)),
    'upper-entry-slip': ((5, -4), (4, -3), (3, -2)),
    'lower-exit-departure': ((3, -4),),
    'lower-entry-departure': ((-3, 2),),
    'upper-exit-departure': ((-2, 4),),
    'upper-entry-departure': ((5, -3),),
    'lower-exit-grade': ((2, -3), (2, -2), (1, -2)),
    'lower-entry-grade': ((-2, 1), (-1, 1), (-1, 0)),
    'upper-exit-grade': ((-1, 3), (0, 2), (0, 1)),
    'upper-entry-grade': ((4, -2), (3, -1), (2, -1)),
}
OWNED_CELLS = frozenset(cell for cells in PARTITIONS.values() for cell in cells)


def _point(point):
    return tuple(round(value, 5) for value in point)


def _translate(point, sign=1.):
    return (point[0] + sign * TRANSLATION_M[0],
            point[1] + sign * TRANSLATION_M[1], point[2])


def _edge_extension(endpoint, neighbour):
    """Follow the terminal chord outward to the first positive lattice cut."""
    vector = tuple(endpoint[axis] - neighbour[axis] for axis in (0, 1))
    require(math.hypot(*vector) > 1e-12 and abs(endpoint[2] - neighbour[2]) < 1e-8,
            'B native collar must extend one nonzero flat directed chord')
    candidates = []
    for axis, delta in enumerate(vector):
        if abs(delta) < 1e-12:
            continue
        index = math.floor((endpoint[axis] + 8.) / 16.) if delta > 0. else math.ceil((endpoint[axis] + 8.) / 16.) - 1
        boundary = 16. * index + (8. if delta > 0. else -8.)
        at = (boundary - endpoint[axis]) / delta
        if at > 1e-9:
            candidates.append((at, axis, boundary))
    require(candidates, 'B native collar has no next tile-side intersection')
    at, axis, boundary = min(candidates)
    result = [endpoint[i] + at * vector[i] for i in (0, 1)] + [endpoint[2]]
    result[axis] = boundary
    return tuple(result)


@lru_cache(maxsize=1)
def physical_routes():
    """Keep the accepted shape, width, radius, grade, and texture station."""
    result = deepcopy(reference.revised_routes(reference.HIGHWAY_SLIP_PROFILE))
    for ramp in result:
        ramp['points'] = [_translate(point) for point in ramp['points']]
    return result


@lru_cache(maxsize=1)
def traffic_routes():
    result = deepcopy(physical_routes())
    for ramp in result:
        points = ramp['points']
        ramp['points'] = [_edge_extension(points[0], points[1]), *points,
                          _edge_extension(points[-1], points[-2])]
    return result


def native_routes(column, row):
    """Literal unchanged DD phase, with the Avenue advanced one half-step."""
    from .assembly_verify import _native_routes
    highway = [route for route in _native_routes(column, row) if route['points'][0][2] > 1.]
    avenue = [route for route in _native_routes(column - 1, row) if route['points'][0][2] == 0.]
    return highway + avenue


@lru_cache(maxsize=1)
def expected_cell_routes():
    owned = {cell for cells in PARTITIONS.values() for cell in cells}
    result = {cell: [{**route, 'points': [(p[0] + 16. * cell[0], p[1] - 16. * cell[1], p[2])
                                        for p in route['points']]}
                     for route in native_routes(*cell)] for cell in owned}
    for ramp in traffic_routes():
        for cell, fragments in reference._split_points(ramp['points']).items():
            require(cell in result, 'B ramp PATH leaves its independently reviewed whole-cell ownership')
            result[cell].extend({'transport': 1, 'points': points, 'approved_ramp': ramp['id']}
                                for points in fragments)
    return result


def _source_origin(piece):
    key = piece.get('geometry_key', '').removeprefix('parallel-b-')
    require(piece.get('domain') == 'highway' and key in PARTITIONS
            and piece.get('recipe') == PREFIX + key.replace('-', '_'),
            'No independent B recipe and sparse-ownership contract')
    cells = PARTITIONS[key]
    origin = min(c[0] for c in cells), min(c[1] for c in cells)
    expected = sorted(([x - origin[0], y - origin[1]] for x, y in cells), key=lambda c: (c[1], c[0]))
    require(piece.get('cells') == expected
            and piece.get('footprint') == [max(c[a] for c in expected) + 1 for a in (0, 1)]
            and len(piece.get('tile_ids', ())) == len(expected)
            and len(set(piece['tile_ids'])) == len(expected),
            'B sparse ownership or footprint differs from the independent partition')
    engineering = piece.get('engineering', {})
    require(engineering.get('grid_alignment') == 'B'
            and engineering.get('alignment_a_translation_en_m') == [8., 8.]
            and engineering.get('avenue_phase_offset') == 1,
            'B must explicitly declare the measured translation and distinct Avenue grid phase')
    require(engineering.get('highway_slip_profile') == reference.HIGHWAY_SLIP_PROFILE
            and engineering.get('max_grade_percent') == 30.
            and engineering.get('pavement_path_offset_m') == 0.
            and engineering.get('car_corridor_half_width_m') == 1.25
            and engineering.get('car_corridor_height_m') == 3.8,
            'B changes the retained shoulder, grade, pavement datum, or traffic corridor')
    require(piece.get('shadow_mode') == 'model-carrier'
            and piece.get('model_shadows', {}).get('enabled') is False,
            'B must preserve the declared no-shadow policy and reserved carrier namespace')
    if key.endswith('terminal'):
        require(engineering.get('ground_mouth_profile') == reference.GROUND_MOUTH_PROFILE,
                'B terminal must retain its narrowed adaptive-sidewalk mouth')
    return origin


def check_paths(resources, piece):
    from .ramp_verify import _paths
    origin = _source_origin(piece)
    expected, fragments, maximum = expected_cell_routes(), 0, 0.
    for cell, tile in zip(piece['cells'], piece['tile_ids']):
        source = cell[0] + origin[0], cell[1] + origin[1]
        actual = _paths(resources[*PATH, int(tile, 16)])
        translated = [{**route, 'points': [(p[0] + 16. * source[0], p[1] - 16. * source[1], p[2])
                                          for p in route['points']]} for route in actual]
        require(reference._same_routes(translated, expected[source]),
                f'B saved PATH differs from the independently shifted ramps or native phase in {source}')
        for route in translated:
            for a, b in zip(route['points'], route['points'][1:]):
                maximum = max(maximum, abs(b[2] - a[2]) / math.dist(a[:2], b[:2]))
        fragments += len(actual)
    require(maximum <= .30001, 'B saved ramp exceeds the retained 30 percent bound')
    return {'passed': True, 'route_fragments_checked': fragments, 'maximum_grade_percent': maximum * 100.,
            'native_dd_phase_retained': True, 'native_avenue_phase': 1,
            'authored_shape_translation_east_north_m': list(TRANSLATION_M),
            'flat_native_endpoint_collars_checked': True, 'game_operation_tested': False}


def expected_ports(piece):
    from .ramp_verify import _endpoints
    origin = _source_origin(piece)
    routes = {}
    for local in map(tuple, piece['cells']):
        source = local[0] + origin[0], local[1] + origin[1]
        records = []
        for route in expected_cell_routes()[source]:
            city = [(p[0] - 16. * source[0], p[1] + 16. * source[1], p[2]) for p in route['points']]
            records.append({'transport': route['transport'],
                'entry': reference._endpoint_edge(city[0], city[1]),
                'exit': reference._endpoint_edge(city[-1], city[-2]),
                'points': [(p[0] - 16. * origin[0], p[1] + 16. * origin[1], p[2]) for p in route['points']]})
        routes[local] = records
    ends, result = _endpoints(routes), []
    for endpoint in ends:
        dx, dy = NEIGHBOURS[endpoint['side']]
        neighbour = endpoint['cell'][0] + dx, endpoint['cell'][1] + dy
        if any(other['direction'] != endpoint['direction'] and other['transport'] == endpoint['transport']
               and other['cell'] == neighbour and other['side'] == (endpoint['side'] + 2) % 4
               and math.dist(other['point_m'], endpoint['point_m']) < TOLERANCE for other in ends):
            continue
        if any(other['transport'] == endpoint['transport'] and other['direction'] == endpoint['direction']
               and math.dist(other['point_m'], endpoint['point_m']) < TOLERANCE for other in result):
            continue
        result.append({**endpoint, 'source_cell': list(endpoint['cell']), 'edge': endpoint['side']})
    return result


def reviewed_contract(piece):
    origin, ports = _source_origin(piece), expected_ports(piece)
    result = {'ports': {}, 'port_vectors': {}, 'port_transports': {}, 'port_directions': {}, 'movements': [],
              'boundary_measurement_precision': 'saved-path'}
    for index, port in enumerate(sorted(ports, key=lambda p: (p['transport'], p['direction'], p['point_m']))):
        port['id'] = f'channel-{index + 1:02d}-{port["direction"]}'
        for field, value in (('ports', port['point_m']), ('port_vectors', port['tangent']),
                             ('port_transports', port['transport']), ('port_directions', port['direction'])):
            result[field][port['id']] = list(value) if isinstance(value, tuple) else value
    graph = defaultdict(set)
    for cell in PARTITIONS[piece['geometry_key'].removeprefix('parallel-b-')]:
        for route in expected_cell_routes()[cell]:
            graph[route['transport'], _point(route['points'][0])].add((route['transport'], _point(route['points'][-1])))
    world = lambda p: (p['transport'], _point((p['point_m'][0] + 16. * origin[0],
                                             p['point_m'][1] - 16. * origin[1], p['point_m'][2])))
    for first in ports:
        if first['direction'] != 'in':
            continue
        pending, seen = [world(first)], set()
        while pending:
            point = pending.pop()
            if point not in seen:
                seen.add(point)
                pending.extend(graph[point] - seen)
        for last in ports:
            if last['direction'] == 'out' and world(last) in seen:
                result['movements'].append([first['id'], last['id']])
    return result


def reviewed_facts(piece):
    """Semantic expectations; exact saved byte pins require the later freeze.

    A byte hash cannot be inferred from a geometric contract: comments,
    record ordering, and decimal formatting are also part of its input.
    Strict extraction must therefore combine these independent expectations
    with the actual independently checked saved PATH fingerprints.
    """
    from .connections import service_classifier
    origin, contract = _source_origin(piece), reviewed_contract(piece)
    endpoints = expected_ports(piece)
    ports, channels, components = [], [], {}
    for name, position in contract['ports'].items():
        direction, engine = contract['port_directions'][name], contract['port_transports'][name]
        matches = [port for port in endpoints if port['direction'] == direction and port['transport'] == engine
                   and math.dist(port['point_m'], position) <= 1e-6]
        require(len(matches) == 1, 'B semantic connector does not name one complete directed boundary')
        measurement = matches[0]
        local = tuple(measurement['source_cell'])
        source = local[0] + origin[0], local[1] + origin[1]
        incidents = []
        for route in expected_cell_routes()[source]:
            if route['transport'] != engine:
                continue
            points = [(p[0] - 16. * origin[0], p[1] + 16. * origin[1], p[2]) for p in route['points']]
            at = 0 if direction == 'in' else -1
            if math.dist(points[at], position) <= 1e-6:
                incidents.append(points[:2] if direction == 'in' else points[-2:])
        require(incidents, 'B boundary has no independently sampled source chord')
        # Match the common connector engine's documented six-decimal point
        # sampling without treating it as an analytic travel direction.
        first, last = (tuple(round(v, 6) for v in p) for p in incidents[0])
        delta = tuple(b - a for a, b in zip(first, last))
        length = math.hypot(*delta[:2])
        sampled = [delta[0] / length, delta[1] / length]
        saved_first, saved_last = (tuple(round(v, 9) for v in p) for p in incidents[0])
        saved_delta = tuple(b - a for a, b in zip(saved_first, saved_last))
        saved_grade = saved_delta[2] / math.hypot(*saved_delta[:2])
        service = service_classifier(piece, engine, position[2])
        component = ('avenue-walkways' if engine == 2 else 'upper-mainline' if position[2] == 15.
                     else 'lower-mainline' if position[2] == 7.5 else 'avenue-mainline' if position[2] == 0.
                     else 'access-network')
        channel = name + '-boundary'
        components[component] = {'id': component, 'network': service['service_network'],
                                 'construction_network': 'avenue' if component.startswith('avenue') else 'dirtroad'}
        channels.append({'id': channel, 'component_id': component, 'kind': service['channel_kind'],
                         'traffic_modes': service['traffic_modes'], 'ports': [name]})
        ports.append({'id': name, 'direction': direction, 'engine_transport': engine,
            'edge': measurement['edge'], 'endpoint_m': [round(v, 6) for v in position],
            'sampled_tangent': sampled, 'tangent': list(contract['port_vectors'][name]),
            'grade': round(saved_grade, 9),
            'sampled_grade': round(delta[2] / length, 9),
            **{key: service[key] for key in ('service_network', 'service_family', 'variant',
                                            'role', 'channel_kind', 'traffic_modes')},
            'source_cell': list(local), 'channel_id': channel})
    movements = list(map(tuple, contract['movements']))
    forbidden = [(first['id'], last['id']) for first in ports for last in ports
                 if first['direction'] == 'in' and last['direction'] == 'out'
                 and (first['id'], last['id']) not in movements]
    return {'reference_piece_id': piece['id'], 'footprint': piece['footprint'], 'cells': piece['cells'],
            'path_hashes_by_cell': [], 'raw_path_fingerprint_status': 'requires-independent-saved-build-freeze',
            'ports': ports, 'movements': movements, 'forbidden_transfers': forbidden,
            'components': list(components.values()), 'channels': channels,
            'channel_scope': 'Independent boundary semantics; the later saved-resource freeze must associate physical native and access channels.'}


def check_construction_fields(fields, piece, resources):
    from scp.verify import check_emitted_runtime_addresses
    from .ddrhw_connections import approaches, check_construction_approaches
    from .ramp_verify import _paths, _road_word
    _source_origin(piece)
    helpers = approaches(piece)
    if helpers:
        fields = check_construction_approaches(fields, piece)
        piece = {key: value for key, value in piece.items() if key != 'native_dd_approaches'}
    if piece.get('adaptive_ground'):
        from .adaptive_verify import check_construction_fields as check
        result = check(fields, piece, resources)
    else:
        width, depth = piece['footprint']
        rows = [['.'] * (width + 2) for _ in range(depth + 1)]
        rows[0][-1], rows[-1][0] = '<', '^'
        cons, checks = deepcopy(rows), []
        for index, (cell, tile) in enumerate(zip(piece['cells'], piece['tile_ids'])):
            symbol = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[index]
            rows[cell[1]][cell[0]], cons[cell[1]][cell[0]] = symbol, '+'
            checks.append(f'{symbol} - dirtroad: 0x{_road_word(_paths(resources[*PATH, int(tile, 16)])):08X}')
        normalize = lambda row: re.sub(r'0x[0-9a-fA-F]+', lambda match: match[0].upper(), row)
        require(fields.get('CellLayout') == [''.join(row) for row in rows]
                and fields.get('ConsLayout') == [''.join(row) for row in cons]
                and list(map(normalize, fields.get('CheckType', []))) == list(map(normalize, checks))
                and fields.get('Costs') == ['1000'], 'B construction changes sparse ownership or saved-route flags')
        result = {'passed': True, 'occupied_cells_checked': len(piece['cells'])}
    check_emitted_runtime_addresses(fields, piece)
    return {**result, 'native_dd_outside_approaches_checked': len(helpers),
            'emitted_runtime_addresses_checked': True, 'game_behavior_tested': False}


def check_models(resources, piece, donors=None):
    from .modular_partition_verify import check_preview
    from .ramp_verify import _native_appearance
    origin, faces = _source_origin(piece), []
    for cell, tile in zip(piece['cells'], piece['tile_ids']):
        tile = int(tile, 16)
        raw = decompress(resources[*S3D, tile])
        require(all(decompress(resources[*S3D, tile + zoom]) == raw for zoom in range(5)),
                'B saved zoom changes its complete native or authored model')
        faces.extend(reference._decode_faces(raw, cell, origin=(16. * origin[0], -16. * origin[1])))
    canonical = [{**face, 'points': tuple(_translate(p, -1.) for p in face['points'])} for face in faces]
    if piece['geometry_key'].endswith(('-departure', '-grade')):
        require(all(face['texture'] not in (0x5713000E, 0x0400020E, 0x0400380E) for face in faces),
                'B departure and grade models must remain separately reusable pure ramp geometry')
    field = reference.check_wheeltrack_vertices(canonical, highway_slip_profile=reference.HIGHWAY_SLIP_PROFILE)
    appearance = _native_appearance(faces, neutral_field_controls=field)
    check_preview(resources, piece)
    result = {'passed': True, 'indexed_triangles_checked': len(faces),
              'all_five_zooms_exact': True, 'preview_matches_all_saved_cells': True,
              'texture_ids': sorted({face['texture'] for face in faces}),
              'native_appearance': appearance, 'independent_wheeltrack_field': field,
              'game_rendering_tested': False}
    if piece.get('adaptive_ground'):
        from .adaptive_verify import check_resources
        result['adaptive_ground'] = check_resources(resources, piece)
    from .shadow_verify import check_resources
    result.update(check_resources(resources, piece))
    return result


def check_owned_cells(pieces, scene):
    placements, owners, keys, shifts = scene.get('placements', []), {}, set(), set()
    require(len(placements) == 15, 'B assembly needs fifteen reusable functional placements')
    for index, pose in enumerate(placements):
        piece = pieces[pose['piece_id']]
        source = _source_origin(piece)
        key = piece['geometry_key'].removeprefix('parallel-b-')
        require(key not in keys and pose.get('rotation_degrees_ccw', 0) == 0,
                'B assembly repeats a module or changes its relative proper rotation')
        keys.add(key)
        origin = pose['origin_m']
        require(len(origin) == 2 and all(type(v) in (int, float) and math.isfinite(v) for v in origin),
                'B assembly has an invalid placement origin')
        shift = origin[0] - source[0] * 16., origin[1] + source[1] * 16.
        require(all(abs(v / 16. - round(v / 16.)) < 1e-9 for v in shift),
                'B construction anchor leaves the actual city-tile lattice')
        shifts.add(shift)
        for local, tile in zip(piece['cells'], piece['tile_ids']):
            cell = source[0] + local[0], source[1] + local[1]
            require(cell not in owners, 'B assembly duplicates whole-cell traffic ownership')
            owners[cell] = {'placement': index, 'piece_id': piece['id'], 'tile': int(tile, 16),
                           'local_cell': tuple(local), 'geometry_key': key, 'angle': 0,
                           'origin': (16. * source[0], -16. * source[1])}
    require(keys == set(PARTITIONS) and set(owners) == OWNED_CELLS and len(shifts) == 1,
            'B assembly changes its independently reviewed fifteen-owner, 34-cell union')
    return owners, next(iter(shifts))


def _native_external_contract():
    from .assembly_verify import _direction
    result = {}
    for cell in OWNED_CELLS:
        for route in native_routes(*cell):
            for direction, at, edge in (('in', 0, route['entry']), ('out', -1, route['exit'])):
                dx, dy = NEIGHBOURS[edge]
                if (cell[0] + dx, cell[1] + dy) in OWNED_CELLS:
                    continue
                p = route['points'][at]
                point = p[0] + 16. * cell[0], p[1] - 16. * cell[1], p[2]
                u, v = reference._uv(_translate(point, -1.))
                arm = ('HW_NE' if u > 0. else 'HW_SW') if point[2] > 1. else ('AVE_NW' if v > 0. else 'AVE_SE')
                tangent, grade = _direction(route['points'], direction == 'in')
                result[route['transport'], direction, _point(point)] = {
                    'transport': route['transport'], 'direction': direction, 'point': _point(point),
                    'tangent': tangent, 'grade': grade, 'arm': arm}
    require(len(result) == 20, 'B native boundary must retain all twenty directed car and pedestrian ports')
    return result


def check_native_boundary_neighbours():
    """Measure the complete complement on every actual outside city tile."""
    from .assembly_verify import _direction
    checked = []
    for cell in sorted(OWNED_CELLS):
        for route in native_routes(*cell):
            for direction, at, edge in (('in', 0, route['entry']), ('out', -1, route['exit'])):
                dx, dy = NEIGHBOURS[edge]
                neighbour = cell[0] + dx, cell[1] + dy
                if neighbour in OWNED_CELLS:
                    continue
                endpoint = route['points'][at]
                world = (endpoint[0] + 16. * cell[0], endpoint[1] - 16. * cell[1], endpoint[2])
                counterpart_at = -1 if direction == 'in' else 0
                matches = [other for other in native_routes(*neighbour)
                           if other['transport'] == route['transport']
                           and math.dist((other['points'][counterpart_at][0] + 16. * neighbour[0],
                                          other['points'][counterpart_at][1] - 16. * neighbour[1],
                                          other['points'][counterpart_at][2]), world) <= TOLERANCE]
                require(len(matches) == 1, 'B exterior lacks one complete directed native neighbour counterpart')
                tangent, grade = _direction(route['points'], direction == 'in')
                native_tangent, native_grade = _direction(matches[0]['points'], direction != 'in')
                require(math.dist(tangent, native_tangent) < 1e-6 and abs(grade - native_grade) < 1e-8,
                        'B exterior and native neighbour disagree on heading or traffic height')
                checked.append({'cell': list(cell), 'outside_cell': list(neighbour),
                                'direction': direction, 'transport': route['transport'], 'point_m': list(world)})
    require(len(checked) == 20, 'B external native-neighbour proof lost a lane or pedestrian channel')
    return {'passed': True, 'complete_directed_native_counterparts_checked': len(checked),
            'native_dd_phase_retained': True, 'native_avenue_phase': 1,
            'boundaries': checked, 'native_dragging_observed': False}


def _straight_witness(first, last, graph, routes, turns):
    """Require actual constant-height native travel instead of a ramp detour."""
    p = reference._rotate(first[2], -turns)
    axis = p[0] - p[1] if p[2] > 1. else p[0] + p[1]
    allowed = set()
    for route in routes:
        if route['transport'] != first[0]:
            continue
        points = [reference._rotate(point, -turns) for point in route['points']]
        if all(abs(point[2] - p[2]) < TOLERANCE
               and abs((point[0] - point[1] if p[2] > 1. else point[0] + point[1]) - axis) < TOLERANCE
               for point in points):
            allowed.add(route['id'])
    restricted = {node: set(next_ for next_ in graph[node] if next_ in allowed) for node in allowed}
    return restricted, allowed


def check_saved_routes(routes, *, turns=0):
    """Inspect complete decoded journeys, their level, and their native spine."""
    from .assembly_verify import _direction
    ends, graph = defaultdict(list), defaultdict(set)
    external = {'in': defaultdict(set), 'out': defaultdict(set)}
    expected = {}
    for port in _native_external_contract().values():
        point = _point(reference._rotate(port['point'], turns))
        tangent = reference._rotate((*port['tangent'], 0.), turns)[:2]
        expected[port['transport'], port['direction'], point] = {**port, 'point': point, 'tangent': tangent}
    for route in routes:
        for direction, at, edge in (('in', 0, route['entry']), ('out', -1, route['exit'])):
            tangent, grade = _direction(route['points'], at == 0)
            ends[route['transport'], _point(route['points'][at])].append(
                {'direction': direction, 'route': route['id'], 'edge': edge,
                 'cell': tuple(route['cell']), 'tangent': tangent, 'grade': grade})
    observed, seams = set(), []
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
                            'B saved seam changes its directed native/ramp tangent or grade')
                    if endpoint['direction'] == 'out':
                        graph[endpoint['route']].add(other['route'])
                        seams.append((endpoint['route'], other['route'], point))
            else:
                key = transport, endpoint['direction'], point
                require(key in expected, 'B saved graph has an unexpected or disconnected native boundary')
                contract = expected[key]
                require(sum(a * b for a, b in zip(endpoint['tangent'], contract['tangent'])) > .998
                        and abs(endpoint['grade']) < .005,
                        'B saved native boundary changes its complete directed heading or height')
                observed.add(key)
                external[endpoint['direction']][key].add(endpoint['route'])
    require(observed == set(expected), 'B saved graph lost a native car lane or pedestrian channel')
    required = {('HW_NE', 'HW_SW'), ('HW_SW', 'HW_NE'), ('AVE_NW', 'AVE_SE'), ('AVE_SE', 'AVE_NW'),
                ('HW_NE', 'AVE_NW'), ('AVE_NW', 'HW_SW'), ('HW_SW', 'AVE_SE'), ('AVE_SE', 'HW_NE')}
    forbidden = {('HW_NE', 'AVE_SE'), ('AVE_SE', 'HW_SW'), ('HW_SW', 'AVE_NW'), ('AVE_NW', 'HW_NE')}
    reachable, witnesses, through = set(), {}, []
    for first, starts in external['in'].items():
        same_lane = []
        for last, goals in external['out'].items():
            if first[0] != last[0]:
                continue
            witness = reference._search(starts, goals, graph)
            if witness is None:
                continue
            pair = expected[first]['arm'], expected[last]['arm']
            if first[0] == 1:
                reachable.add(pair)
                witnesses.setdefault(pair, witness)
            p, q = reference._rotate(first[2], -turns), reference._rotate(last[2], -turns)
            axis_p, axis_q = (p[0] - p[1], q[0] - q[1]) if p[2] > 1. else (p[0] + p[1], q[0] + q[1])
            if abs(p[2] - q[2]) < TOLERANCE and abs(axis_p - axis_q) < TOLERANCE and pair[0] != pair[1]:
                straight, allowed = _straight_witness(first, last, graph, routes, turns)
                direct = reference._search(starts & allowed, goals & allowed, defaultdict(set, straight))
                require(direct is not None, 'B native through lane takes a ramp, changes height, or leaves its straight spine')
                same_lane.append(direct)
        require(len(same_lane) == 1, 'B saved graph loses or ambiguously duplicates a native through lane')
        through.extend(same_lane)
    require(required <= reachable, 'B saved graph loses a required right turn or through movement')
    require(not forbidden & reachable, 'B saved graph permits a forbidden cross-Avenue turn')
    return {'passed': True, 'external_native_channels': len(observed),
            'pedestrian_external_channels': sum(port['transport'] == 2 for port in expected.values()),
            'native_through_lane_and_sidewalk_journeys': len(through),
            'constant_height_straight_native_journeys': len(through),
            'straight_through_witnesses': through, 'matched_directed_lane_seams': len(seams),
            'right_turn_transfers': 4, 'no_cross_avenue_transfers': True,
            'movement_witnesses': [{'from_arm': pair[0], 'to_arm': pair[1], 'saved_route_ids': witnesses[pair]}
                                   for pair in sorted(required)],
            'reachable_arm_pairs': [list(pair) for pair in sorted(reachable)]}, seams


def _native_dd_fragment(face):
    """Certify original DD geometry in its unchanged source lattice."""
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
    from .assembly_verify import _projected_area_in_cell
    outside, projection, certified = set(), defaultdict(set), 0
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
                if _projected_area_in_cell(triangle, cell) <= 1e-7:
                    continue
                projection[face['geometry_key']].add(cell)
                if cell not in OWNED_CELLS:
                    unowned.append(cell)
        if unowned:
            require(_native_dd_fragment(face), 'B authored model projects into an unowned tile without native DD provenance')
            outside.update(unowned)
            certified += 1
    return {'passed': True, 'reviewed_owned_cells': len(OWNED_CELLS),
            'unowned_native_end_projection_cells': [list(cell) for cell in sorted(outside)],
            'pinned_native_overhang_triangles_checked': certified,
            'actual_model_projection_cells_by_function': {
                key: [list(cell) for cell in sorted(cells)] for key, cells in sorted(projection.items())}}


def check_straight_native_decks(faces):
    """Sample both complete sixteen-metre decks on the fixed DD axis."""
    from .modular_assembly_verify import _triangle_distance
    index = reference._FaceIndex(faces)
    checked = 0
    # These bounds enclose all 34 literal B cells; each candidate is then
    # clipped to the actual owned union, rather than a rectangular footprint.
    for station in range(-128, 145, 2):
        for lateral in (-7.9, -6., -4.5, -2.2627417, 0., 2.2627417, 4.5, 6., 7.9):
            point = (4. + (station - lateral) / math.sqrt(2.),
                     -4. + (station + lateral) / math.sqrt(2.))
            cell = math.floor((point[0] + 8.) / 16.), math.floor((8. - point[1]) / 16.)
            if cell not in OWNED_CELLS:
                continue
            for height in (7.5, 15.):
                sample = *point, height
                require(any(face['texture'] == 0x5713000E and face['upward']
                            and _triangle_distance(sample, face['points']) <= .002
                            for face in index.nearby(sample)),
                        f'B straight stem loses its complete native sixteen-metre deck: {sample}')
                checked += 1
    return {'passed': True, 'native_deck_surface_samples_checked': checked,
            'native_deck_heights_m': [7.5, 15.], 'native_deck_width_m': 16.,
            'directed_highway_axis_north_minus_east_m': -8., 'surface_sample_tolerance_m': .002,
            'scope': 'Fixed-world indexed-surface samples on both unchanged native DD decks throughout the B owned union.'}


def _continuous_support(first, last, faces, precision):
    """Keep the existing two-micrometre, source-qualified encoding bound."""
    from .ramp_verify import _covered, _interval
    from .modular_assembly_verify import _triangle_distance
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
        canonical = {**face, 'points': tuple(_translate(point, -1.) for point in face['points'])}
        matched = (reference._native_avenue_fragment(face) if texture in (0x0400020E, 0x0400380E) else
                   reference._approved_ramp_encoding_fragment(canonical, ground_mouth_profile=reference.GROUND_MOUTH_PROFILE)
                   if texture == 0x5712000E else _native_dd_fragment(face))
        if matched:
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
                                reference._edge_capsule_intervals_3d(first, last, a, b, 2e-6)
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
            distance = min(_triangle_distance(point, face['points']) for face in pinned)
            precision['maximum_sampled_actual_face_distance_m'] = max(
                precision['maximum_sampled_actual_face_distance_m'], distance)
    return True


def check_model_union(faces, routes):
    """Check real B traffic on indexed pavement before reference samples."""
    from .ramp_verify import _intrudes
    index = reference._FaceIndex(faces)
    precision = {'euclidean_distance_limit_m': 2e-6, 'admitted_road_encoding_spans': 0,
                 'maximum_admitted_along_route_span_m': 0., 'maximum_sampled_actual_face_distance_m': 0.}
    checked = 0
    for route in routes:
        if route['transport'] != 1:
            continue
        for first, last in zip(route['points'], route['points'][1:]):
            candidates = index.nearby(first, last, 1.25)
            require(_continuous_support(first, last, candidates, precision),
                    f'B model union lacks continuous actual car pavement: {first}->{last}')
            require(not any(_intrudes(first, last, face['points'], 1.25, 3.8) for face in candidates),
                    f'B saved face intrudes into the actual car corridor: {first}->{last}')
            checked += 1
    canonical = [{**face, 'points': tuple(_translate(point, -1.) for point in face['points'])} for face in faces]
    # These approved samples constrain the translated authored shape. The
    # fixed native lattice and new PATH-only collars were checked above in
    # B world coordinates, so they are not inferred from a translated A.
    canonical_routes = []
    for ramp in reference.revised_routes(reference.HIGHWAY_SLIP_PROFILE):
        canonical_routes.append({'transport': 1, 'points': ramp['points']})
    shape = reference.check_model_union(canonical, canonical_routes,
        ground_mouth_profile=reference.GROUND_MOUTH_PROFILE,
        highway_slip_profile=reference.HIGHWAY_SLIP_PROFILE)
    return {'passed': True, 'continuous_actual_b_car_segments_checked': checked,
            'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
            'road_support_encoding_precision': precision, 'translated_approved_shape_checks': shape,
            'scope': 'B-world continuous pavement and car corridors, including new flat native collars; translated approved width, underside, barrier, and wheeltrack samples. No game traffic is established.'}


def verify_assembly_resources(manifest, scene, piece_resources, *, inspect_models=True):
    from .assembly_verify import decode_placed_routes
    from .ddrhw_connections import check_selected_helper_collisions
    require(scene.get('id', SUBJECT) == SUBJECT, 'B verification received another assembly identity')
    pieces = {piece['id']: piece for piece in manifest['pieces']}
    owners, shift = check_owned_cells(pieces, scene)
    helpers = check_selected_helper_collisions(pieces, scene)
    for identifier in {owner['piece_id'] for owner in owners.values()}:
        check_paths(piece_resources[identifier], pieces[identifier])
    routes = decode_placed_routes(owners, piece_resources)
    paths, _seams = check_saved_routes(routes)
    rotations = [{'quarter_turns_ccw': 0, **paths}]
    for turns in (1, 2, 3):
        rotated = []
        for route in routes:
            centre = reference._rotate((route['cell'][0], -route['cell'][1], 0.), turns)
            rotated.append({**route, 'points': [reference._rotate(p, turns) for p in route['points']],
                            'entry': (route['entry'] - turns) % 4, 'exit': (route['exit'] - turns) % 4,
                            'cell': (round(centre[0]), round(-centre[1]))})
        rotations.append({'quarter_turns_ccw': turns, **check_saved_routes(rotated, turns=turns)[0]})
    not_run = {'passed': False, 'status': 'not-run'}
    models = projection = supports = cuts = mouths = uv = slip = decks = not_run
    if inspect_models:
        faces = []
        for owner in owners.values():
            faces.extend({**face, 'geometry_key': owner['geometry_key']} for face in
                         reference._decode_faces(piece_resources[owner['piece_id']][*S3D, owner['tile'] + 4],
                                                 owner['local_cell'], origin=owner['origin']))
        models, projection = check_model_union(faces, routes), check_projection(faces)
        decks = check_straight_native_decks(faces)
        canonical = [{**face, 'points': tuple(_translate(point, -1.) for point in face['points'])} for face in faces]
        supports = reference.check_supports(canonical)
        cuts = reference.check_physical_cuts(canonical)
        # The A-frame overhang inventory is not a B ownership measurement.
        cuts.pop('checked_physical_cuts_outside_traffic_owner_cells', None)
        cuts['reference_frame'] = 'Actual B faces inverse-translated by the measured eight metres east and north.'
        mouths = reference.check_ground_mouths(canonical, profile=reference.GROUND_MOUTH_PROFILE)
        uv = reference.check_highway_ramp_uv_seams(canonical)
        slip = reference.check_highway_slip_lanes(canonical, profile=reference.HIGHWAY_SLIP_PROFILE)
    return {'schema_version': 1, 'subject_id': SUBJECT, 'saved_resource_checks_passed': bool(inspect_models),
            'saved_path_checks_passed': True, 'saved_ownership_checks_passed': True,
            'saved_path_and_construction_checks_passed': False, 'package_construction_checks': 'not-run',
            'construction': {'unique_owned_cells': 34, 'placements': 15, 'bounding_rectangle_tiles': [9, 9],
                             'translation_east_north_m': list(shift)},
            'paths': paths, 'proper_rotation_paths': rotations,
            'native_neighbour_boundaries': check_native_boundary_neighbours(),
            **({'native_dd_outside_approaches': helpers} if helpers else {}),
            'model_union': models, 'actual_model_projection': projection, 'supports': supports,
            'straight_native_decks': decks,
            'physical_functional_cuts': cuts, 'ground_mouths': mouths,
            'native_wheeltrack_seam_uv': uv, 'highway_slip_lanes': slip,
            'authored_shape_translation_east_north_m': list(TRANSLATION_M),
            'directed_highway_axis_north_minus_east_m': -8., 'ground_avenue_axis_north_plus_east_m': 16.,
            'approval_sha256': reference.APPROVAL_SHA256, 'game_operation': 'unverified',
            'limits': ['Native dragging, adaptive sidewalk selection, visible traffic, shadows, and save/reload require human game observations.',
                       'Width, underside, barrier, and pier samples do not establish structural load capacity.']}


def verify_assembly(output, scene, *, evidence_path=None, verify_package=True):
    from scp.verify import strict_dbpf
    output = Path(output).resolve()
    if evidence_path is not None:
        require(not Path(evidence_path).resolve().is_relative_to(output), 'B evidence must remain outside its saved build')
    if verify_package:
        from scp.verify import verify_build
        verify_build(output, write_report=False)
    raw = (output / 'manifest.json').read_bytes()
    manifest = json.loads(raw)
    files, resources, fingerprints = {row['path']: row for row in manifest['files']}, {}, {}
    for piece in manifest['pieces']:
        path = piece['asset_file']
        data = (output / path).read_bytes()
        require(len(data) == files[path]['bytes'] and hashlib.sha256(data).hexdigest() == files[path]['sha256'],
                'B source DAT differs from its saved manifest')
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
