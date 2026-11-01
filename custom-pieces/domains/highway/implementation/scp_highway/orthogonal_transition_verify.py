"""Independent traffic contract for the six-tile orthogonal DD transition.

The resource writer and its curve helpers are deliberately not imported.
These expectations reconstruct the reviewed curves, native lane measurements,
and city-cell cuts independently, then inspect the actual saved resources.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
from functools import lru_cache
import hashlib
import math
import re

from scp.dbpf import require
from scp.track_paths import PATH
from scp.verify import parse_paths

PIECE_ID = 'ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile'
RECIPE = 'highway_ddrhw_orthogonal_l0_transition'
CELLS = tuple((column, row) for row in range(6) for column in range(2))
LENGTH = 96.0
STATION_STEP = 0.25
POSITION_TOLERANCE = 2e-6
NATIVE_PATH_PINS = {
    0x57530000: 'e5f4c27133d0b03bae145380e151eacd0a32ac42ee7dc5f8f3a51e04ff539853',
    0x57030000: '8d663b22e6762fddd0a55389f23f58636f43d2582435c78a36e4933b89cc294c',
}
NEIGHBOURS = ((-1, 0), (0, -1), (1, 0), (0, 1))
# Independently measured endpoint-tangent flags, including the owned shoulder
# cell with no routes. The native-helper adapter must restore this core view.
CORE_ROAD_WORDS = (0x00000000, 0x02000200, 0x03010000, 0x02000201,
                   0x03010300, 0x02000201, 0x03000300, 0x02000200,
                   0x02000300, 0x02000200, 0x02000200, 0x02000200)


def _number(value):
    return int(value, 16) if isinstance(value, str) else value


def _point(point):
    return tuple(round(value, 6) for value in point)


def _rotate(point, turns):
    east, north, height = point
    for _ in range(turns % 4):
        east, north = north, -east
    return east, north, height


def _cubic(t):
    return t * t * (3.0 - 2.0 * t)


def lateral(s):
    """Return westward displacement, its derivative, and its curvature."""
    if s <= 3.0:
        return 0.0, 0.0, 0.0
    if s >= 69.0:
        return 16.0, 0.0, 0.0
    t = (s - 3.0) / 66.0
    displacement = 16.0 * (10.0 * t**3 - 15.0 * t**4 + 6.0 * t**5)
    derivative = 16.0 * 30.0 * t * t * (1.0 - t)**2 / 66.0
    second = 16.0 * (60.0 * t - 180.0 * t * t + 120.0 * t**3) / 66.0**2
    return displacement, derivative, second / (1.0 + derivative**2)**1.5


def _ease(s):
    if s <= 3.0 or s >= 93.0:
        return 0.0
    if s < 15.0:
        return _cubic((s - 3.0) / 12.0)
    if s <= 81.0:
        return 1.0
    return 1.0 - _cubic((s - 81.0) / 12.0)


def _weight(s):
    _displacement, derivative, curvature = lateral(s)
    # A conservative smooth replacement for |curvature| keeps the profile
    # differentiable through the S-curve's inflection. Both lane offsets are
    # bounded, rather than treating the centerline's grade as a lane bound.
    metric = math.sqrt(1.0 + derivative**2) * (
        1.0 - 2.5 * math.sqrt(curvature**2 + 0.001**2))
    require(metric > 0.0, 'Reviewed transition lane metric became singular')
    return _ease(s) * metric


@lru_cache(maxsize=1)
def _integrals():
    """Independent composite-Simpson antiderivative at 1/64 metre."""
    step = 1.0 / 64.0
    prefix = [0.0]
    first = _weight(0.0)
    for index in range(round(LENGTH / step)):
        start = index * step
        last = _weight(start + step)
        prefix.append(prefix[-1] + step * (first + 4.0 * _weight(start + step / 2.0) + last) / 6.0)
        first = last
    require(prefix[-1] > 75.0, 'Reviewed transition has insufficient graded route length')
    return tuple(prefix), 15.0 / prefix[-1]


def upper_height(s):
    if s <= 3.0:
        return 15.0
    if s >= 93.0:
        return 0.0
    prefix, factor = _integrals()
    index = min(math.floor(s * 64.0), len(prefix) - 2)
    start = index / 64.0
    delta = s - start
    tail = delta * (_weight(start) + 4.0 * _weight(start + delta / 2.0) + _weight(s)) / 6.0
    return 15.0 - factor * (prefix[index] + tail)


def lower_height(s):
    if s <= 3.0:
        return 7.5
    if s >= 69.0:
        return 0.0
    return 7.5 * (1.0 - _cubic((s - 3.0) / 66.0))


def lane_point(component, source_class, s):
    """Return one measured native lane in world east/north/height metres."""
    require(component in ('upper', 'lower') and source_class in (0, 1), 'Unknown transition lane')
    if component == 'lower':
        return (18.5 if source_class == 0 else 13.5), 8.0 - s, lower_height(s)
    displacement, derivative, _curvature = lateral(s)
    normal = 1.0 / math.sqrt(1.0 + derivative**2)
    offset = -2.5 if source_class == 0 else 2.5
    return (16.0 - displacement + offset * normal,
            8.0 - s - offset * derivative * normal, upper_height(s))


def _edge(point):
    east, north, _height = point
    candidates = [abs(east + 8.0) <= POSITION_TOLERANCE,
                  abs(north - 8.0) <= POSITION_TOLERANCE,
                  abs(east - 8.0) <= POSITION_TOLERANCE,
                  abs(north + 8.0) <= POSITION_TOLERANCE]
    require(sum(candidates) == 1, 'Transition endpoint is not on one unambiguous city-cell side')
    return candidates.index(True)


def _slice(points, component, source_class):
    """Independently cut the reviewed polyline, without a writer helper."""
    fragments = []
    for first, last in zip(points, points[1:]):
        cuts = [0.0, 1.0]
        for axis, boundaries in ((0, (8.0,)), (1, tuple(8.0 - 16.0 * row for row in range(1, 6)))):
            delta = last[axis] - first[axis]
            if abs(delta) <= 1e-14:
                continue
            cuts.extend((boundary - first[axis]) / delta for boundary in boundaries
                        if 1e-12 < (boundary - first[axis]) / delta < 1.0 - 1e-12)
        cuts = sorted(set(cuts))
        for begin, end in zip(cuts, cuts[1:]):
            a = tuple(first[axis] + begin * (last[axis] - first[axis]) for axis in range(3))
            b = tuple(first[axis] + end * (last[axis] - first[axis]) for axis in range(3))
            middle = tuple((x + y) / 2.0 for x, y in zip(a, b))
            cell = math.floor((middle[0] + 8.0) / 16.0), math.floor((8.0 - middle[1]) / 16.0)
            require(cell in CELLS, 'Reviewed transition lane leaves its two-by-six city-cell ownership')
            if fragments and fragments[-1]['cell'] == cell:
                require(math.dist(fragments[-1]['points'][-1], a) < 1e-8, 'Independent transition slice is discontinuous')
                fragments[-1]['points'].append(b)
            else:
                fragments.append({'cell': cell, 'points': [a, b]})
    result = []
    for fragment in fragments:
        column, row = fragment['cell']
        local = [(p[0] - 16.0 * column, p[1] + 16.0 * row, p[2]) for p in fragment['points']]
        result.append({'cell': fragment['cell'], 'component': component, 'source_class': source_class,
            'transport': 1, 'lane': source_class + (1 if row == 5 else 0),
            'entry': _edge(local[0]), 'exit': _edge(local[-1]), 'compatibility': 0, 'points': local})
    return result


@lru_cache(maxsize=1)
def _expected_routes():
    result = {cell: [] for cell in CELLS}
    stations = [index * STATION_STEP for index in range(round(LENGTH / STATION_STEP) + 1)]
    for component in ('upper', 'lower'):
        for source_class in (0, 1):
            points = [lane_point(component, source_class, s) for s in stations]
            if component == 'lower':
                points.reverse()
            for fragment in _slice(points, component, source_class):
                result[fragment['cell']].append(fragment)
    return result


def expected_cell_routes():
    return deepcopy(_expected_routes())


def _spec(piece):
    require(piece.get('id') == PIECE_ID and piece.get('recipe') == RECIPE and piece.get('domain') == 'highway',
            'Wrong registered orthogonal DD transition owner or recipe')
    require(piece.get('footprint') == [2, 6] and tuple(map(tuple, piece.get('cells', ()))) == CELLS,
            'Orthogonal DD transition must retain all twelve row-major owned cells')
    tiles = tuple(map(_number, piece.get('tile_ids', ())))
    require(len(tiles) == len(set(tiles)) == 12, 'Orthogonal transition needs twelve distinct canonical cells')
    engineering = piece.get('engineering', {})
    empty = {cell for cell, records in _expected_routes().items() if not records}
    require(set(map(tuple, engineering.get('model_only_cells', ()))) == empty,
            'Transition model-only cells differ from the independently reconstructed lanes')
    require(type(engineering.get('max_grade_percent')) in (float, int)
            and 0.0 < engineering['max_grade_percent'] <= 30.0,
            'Transition must retain an explicit lane-grade ceiling no greater than thirty percent')
    require(engineering.get('car_corridor_half_width_m') == 1.25
            and engineering.get('car_corridor_height_m') == 3.8,
            'Transition corridor must retain its declared 2.5m-by-3.8m vehicle envelope')
    require(piece.get('shadow_mappings') == [] and not piece.get('model_shadows', {}).get('enabled', True),
            'Orthogonal transition must explicitly disable custom shadows')
    return tiles


def external_ports():
    result = []
    for component in ('upper', 'lower'):
        for source_class in (0, 1):
            lane = f'{component}-lane-{source_class + 1:02d}'
            for direction in ('in', 'out'):
                s = (0.0 if direction == 'in' else LENGTH) if component == 'upper' else (
                    LENGTH if direction == 'in' else 0.0)
                cell = (1, 0) if s == 0.0 else ((0, 5) if component == 'upper' else (1, 5))
                result.append({'id': lane + '-' + direction, 'channel_id': lane, 'component': component,
                    'source_class': source_class, 'direction': direction, 'transport': 1,
                    'point_m': lane_point(component, source_class, s), 'source_cell': list(cell),
                    'edge': 1 if s == 0.0 else 3,
                    'tangent': (0.0, -1.0 if component == 'upper' else 1.0), 'grade': 0.0})
    return result


def reviewed_contract(piece):
    _spec(piece)
    ports = external_ports()
    return {'boundary_measurement_precision': 'saved-path',
        'ports': {p['id']: list(p['point_m']) for p in ports},
        'port_vectors': {p['id']: list(p['tangent']) for p in ports},
        'port_transports': {p['id']: 1 for p in ports},
        'port_directions': {p['id']: p['direction'] for p in ports},
        'movements': [[f'{component}-lane-{lane:02d}-in', f'{component}-lane-{lane:02d}-out']
                      for component in ('upper', 'lower') for lane in (1, 2)]}


def reviewed_facts(piece):
    """Independent intrinsic semantics; actual byte hashes need a later freeze."""
    contract = reviewed_contract(piece)
    ports = []
    channels = []
    for p in external_ports():
        height = p['point_m'][2]
        ports.append({'id': p['id'], 'direction': p['direction'], 'engine_transport': 1,
            'edge': p['edge'], 'endpoint_m': list(p['point_m']),
            'sampled_tangent': list(p['tangent']), 'tangent': list(p['tangent']), 'grade': 0.0,
            'service_network': 'road', 'service_family': 'road',
            'variant': 'rhw-4-l0' if height == 0.0 else 'dd-rhw-l2' if height == 15.0 else 'dd-rhw-l1',
            'role': 'primary', 'channel_kind': 'road-lane', 'traffic_modes': ['car'],
            'source_cell': p['source_cell'], 'channel_id': p['channel_id']})
    for component in ('upper', 'lower'):
        for lane in (1, 2):
            name = f'{component}-lane-{lane:02d}'
            channels.append({'id': name, 'component_id': component + '-carriageway', 'kind': 'road-lane',
                             'traffic_modes': ['car'], 'ports': [name + '-in', name + '-out']})
    movements = list(map(tuple, contract['movements']))
    forbidden = [(a['id'], b['id']) for a in ports for b in ports
                 if a['direction'] == 'in' and b['direction'] == 'out'
                 and (a['id'], b['id']) not in movements]
    return {'reference_piece_id': PIECE_ID, 'footprint': [2, 6], 'cells': [list(cell) for cell in CELLS],
            'path_hashes_by_cell': [], 'raw_path_fingerprint_status': 'requires-checked-saved-build-freeze',
            'ports': ports, 'movements': movements, 'forbidden_transfers': forbidden,
            'components': [{'id': c + '-carriageway', 'network': 'road', 'construction_network': 'dirtroad'}
                           for c in ('upper', 'lower')], 'channels': channels}


def _same_route(actual, expected):
    if any(actual[key] != expected[key] for key in ('transport', 'lane', 'entry', 'exit', 'compatibility')):
        return False
    return len(actual['points']) == len(expected['points']) and all(
        math.dist(a, b) <= POSITION_TOLERANCE for a, b in zip(actual['points'], expected['points']))


def _journeys(routes, turns):
    starts, ends = defaultdict(list), defaultdict(list)
    for index, route in enumerate(routes):
        starts[_point(_rotate(route['points'][0], turns))].append(index)
        ends[_point(_rotate(route['points'][-1], turns))].append(index)
    require(all(len(indices) == 1 for indices in (*starts.values(), *ends.values())),
            'Transition has an ambiguous lane/deck connection')
    incoming, outgoing = starts.keys() - ends.keys(), ends.keys() - starts.keys()
    literal = external_ports()
    expected_in = {_point(_rotate(p['point_m'], turns)) for p in literal if p['direction'] == 'in'}
    expected_out = {_point(_rotate(p['point_m'], turns)) for p in literal if p['direction'] == 'out'}
    require(incoming == expected_in and outgoing == expected_out,
            'Transition lost or displaced a complete native directional boundary member')
    consumed, movements = set(), []
    for port in (p for p in literal if p['direction'] == 'in'):
        start = _point(_rotate(port['point_m'], turns))
        index = starts[start][0]
        sequence = []
        while True:
            require(index not in consumed, 'Transition contains a loop or a lane/deck transfer')
            consumed.add(index)
            sequence.append(index)
            end = _point(_rotate(routes[index]['points'][-1], turns))
            if end in outgoing:
                break
            require(end in starts, 'Transition lane ends inside its owned cells')
            index = starts[end][0]
        target = next(p for p in literal if p['channel_id'] == port['channel_id'] and p['direction'] == 'out')
        require(end == _point(_rotate(target['point_m'], turns)),
                'Transition transfers a car to the wrong lane or carriageway')
        movements.append({'entry_port': port['id'], 'exit_port': target['id'], 'route_fragments': len(sequence)})
    require(len(consumed) == len(routes), 'Transition has an unconsumed capacity-only route')
    return {'quarter_turns': turns, 'complete_directed_journeys': 4, 'external_directional_members': 8,
            'route_fragments_consumed': len(consumed), 'no_lane_or_carriageway_transfers': True,
            'journeys': movements}


def check_paths(resources, piece):
    tiles = _spec(piece)
    expected = _expected_routes()
    routes, maximum = [], 0.0
    maximum_coordinate_error = 0.0
    for cell, tile in zip(CELLS, tiles):
        require((*PATH, tile) in resources, 'Missing canonical transition PATH cell')
        parsed = parse_paths(resources[*PATH, tile])
        require(parsed['version'] == '1.2' and parsed['terrain'] == 1,
                'Transition PATH must explicitly retain every authored traffic height')
        remaining = list(expected[cell])
        for actual in parsed['routes']:
            matches = [index for index, wanted in enumerate(remaining) if _same_route(actual, wanted)]
            require(len(matches) == 1, 'Saved transition PATH differs from independent native/curve/city-cut measurements')
            wanted = remaining.pop(matches[0])
            maximum_coordinate_error = max(maximum_coordinate_error,
                max(math.dist(a, b) for a, b in zip(actual['points'], wanted['points'])))
            require(_edge(actual['points'][0]) == actual['entry'] and _edge(actual['points'][-1]) == actual['exit'],
                    'Transition PATH entry/exit side differs from its actual position')
            require(all(abs(p[0]) <= 8.0 + POSITION_TOLERANCE and abs(p[1]) <= 8.0 + POSITION_TOLERANCE
                        for p in actual['points']), 'Transition PATH escapes its owning city cell')
            world = [(p[0] + 16.0 * cell[0], p[1] - 16.0 * cell[1], p[2]) for p in actual['points']]
            for first, last in zip(world, world[1:]):
                distance = math.dist(first[:2], last[:2])
                require(distance > 1e-10, 'Stationary or vertical transition PATH segment')
                grade = 100.0 * abs(last[2] - first[2]) / distance
                maximum = max(maximum, grade)
                require(grade <= piece['engineering']['max_grade_percent'] + 1e-5,
                        'Saved transition PATH exceeds its declared lane-grade ceiling')
            routes.append({**actual, 'cell': cell, 'points': world})
        require(not remaining, 'Saved transition PATH omits a lane fragment')
    rotations = [_journeys(routes, turns) for turns in range(4)]
    return {'passed': True, 'tile_count': 12, 'model_only_cells': [list(cell) for cell, records in expected.items() if not records],
            'complete_directed_journeys': 4, 'complete_native_boundary_members_checked': 8,
            'route_fragments_checked': len(routes), 'maximum_grade_percent': maximum,
            'maximum_coordinate_error_m': maximum_coordinate_error, 'use_path_elevation': True,
            'proper_rotations_checked': 4, 'proper_rotations': rotations,
            'no_capacity_only_paths': True, 'no_lane_or_carriageway_transfers': True,
            'native_ground_classes_preserved': True, 'game_operation_tested': False}


def _construction_word(records):
    sides = [0, 0, 0, 0]
    for record in records:
        for side, first, last in ((record['entry'], *record['points'][:2]),
                                  (record['exit'], *record['points'][-2:])):
            dx, dy = last[0] - first[0], last[1] - first[1]
            if abs(dx) < 1e-9 or abs(dy) < 1e-9:
                value = 2
            elif side in (1, 3):
                value = 3 if dx * dy > 0.0 else 1
            else:
                value = 1 if dx * dy > 0.0 else 3
            sides[side] = 2 if value == 2 or sides[side] == 2 else value
    return sum(value << (8 * side) for side, value in enumerate(sides))


def check_construction_fields(fields, piece, resources):
    """Inspect the restored twelve-cell core separately from native helpers."""
    tiles = _spec(piece)
    expected = _expected_routes()
    require(tuple(_construction_word(expected[cell]) for cell in CELLS) == CORE_ROAD_WORDS,
            'Independent transition tangent flags disagree with the reviewed native construction words')
    layouts = ['ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', '^...']
    constraints = ['++.<', '++..', '++..', '++..', '++..', '++..', '^...']
    require(fields.get('CellLayout') == layouts and fields.get('ConsLayout') == constraints,
            'Transition construction changes twelve-cell ownership, the model-only shoulder, or core anchors')
    require(fields.get('Costs') == ['1000'], 'Unexpected orthogonal transition construction cost')
    checks = fields.get('CheckType', [])
    require(len(checks) == 12, 'Transition construction needs exactly twelve core palette entries')
    for index, (cell, tile, word) in enumerate(zip(CELLS, tiles, CORE_ROAD_WORDS)):
        match = re.fullmatch(chr(ord('a') + index) + r'\s*-\s*dirtroad:\s*0x([0-9a-fA-F]{8})', checks[index])
        require(match is not None and int(match[1], 16) == word,
                'Transition core construction network or endpoint-tangent flags differ')
        actual = parse_paths(resources[*PATH, tile])
        require(_construction_word(actual['routes']) == word,
                'Actual saved transition PATH directions disagree with construction flags')
    return {'occupied_cells_checked': 12, 'model_only_owned_cells_checked': 1,
            'native_core_tangent_flag_words_checked': 12, 'core_anchor_and_cost_checked': True,
            'native_helpers_in_scope': False, 'game_construction_tested': False}


def check_models(resources, piece, donors=None):
    from .orthogonal_transition_models_verify import check_models as check_saved_models
    _spec(piece)
    return check_saved_models(resources, piece, donors)
