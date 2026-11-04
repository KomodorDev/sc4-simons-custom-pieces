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
from types import MappingProxyType
from typing import NamedTuple

from scp.dbpf import require
from scp.track_paths import PATH
from scp.verify import parse_paths

PIECE_ID = 'ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile'
MIRRORED_PIECE_ID = PIECE_ID + '-mirrored'
RECIPE = 'highway_ddrhw_orthogonal_l0_transition'
MIRRORED_RECIPE = RECIPE + '_mirrored'
OPPOSITE_SIDE_PIECE_ID = 'ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile'
OPPOSITE_SIDE_MIRRORED_PIECE_ID = OPPOSITE_SIDE_PIECE_ID + '-mirrored'
LOWER_BEND_RIGHT = 'lower-bend-right'
LOWER_BEND_RIGHT_PIECE_ID = 'ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile'


class TransitionPhase(NamedTuple):
    key: str
    piece_id: str
    recipe: str
    physical_reflection: bool
    traffic_reversed: bool
    native_cross_section_reflection: bool


# Independently reviewed expectations, rather than the writer's variant table.
PHASES = MappingProxyType({
    'original': TransitionPhase('original', PIECE_ID, RECIPE, False, False, False),
    'mirrored': TransitionPhase('mirrored', MIRRORED_PIECE_ID, MIRRORED_RECIPE, True, True, False),
    'opposite-side': TransitionPhase('opposite-side', OPPOSITE_SIDE_PIECE_ID,
        RECIPE+'_opposite_side', True, False, True),
    'opposite-side-mirrored': TransitionPhase('opposite-side-mirrored', OPPOSITE_SIDE_MIRRORED_PIECE_ID,
        RECIPE+'_opposite_side_mirrored', False, True, True),
    LOWER_BEND_RIGHT: TransitionPhase(LOWER_BEND_RIGHT, LOWER_BEND_RIGHT_PIECE_ID,
        RECIPE+'_lower_bend_right', False, True, True),
})
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
MIRRORED_CORE_ROAD_WORDS = (0x02000200, 0x00000000, 0x02030200, 0x01000003,
                           0x02030200, 0x01000103, 0x02000200, 0x01000100,
                           0x02000200, 0x02000100, 0x02000200, 0x02000200)


def _number(value):
    return int(value, 16) if isinstance(value, str) else value


def phase_for_piece(piece):
    """Bind exact identities to independently declared shape and traffic phases."""
    key = piece.get('transition_variant', 'original')
    require(isinstance(key, str) and key in PHASES
            and piece.get('id') == PHASES[key].piece_id,
            'Transition identity and explicit mirrored variant do not agree')
    return PHASES[key]


def phase_for_options(*, mirrored=False, variant=None):
    """Retain the old bool API while selecting new phases explicitly."""
    require(type(mirrored) is bool, 'Transition mirrored option must be an exact boolean')
    if variant is None:
        return PHASES['mirrored' if mirrored else 'original']
    require(mirrored is False and isinstance(variant, str) and variant in PHASES,
            'An explicit transition variant cannot mix legacy mirrored options')
    return PHASES[variant]


def _mirrored(piece):
    """Legacy shape accessor; native traffic phase is independently declared."""
    return phase_for_piece(piece).physical_reflection


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


def straight_upper_height(s):
    """Integrate the straight deck's cubic grade easing over its 90 m run."""
    def eased_distance(distance):
        t = distance / 12.0
        return 12.0 * t**3 * (1.0 - .5*t)

    if s <= 3.0:
        return 15.0
    if s >= 93.0:
        return 0.0
    if s < 15.0:
        distance = eased_distance(s - 3.0)
    elif s > 81.0:
        distance = 78.0 - eased_distance(93.0 - s)
    else:
        distance = s - 9.0
    return 15.0 * (1.0 - distance / 78.0)


def lower_bend_frame(component, s):
    """Return the new deck centre and unit cross-section normal in east/north."""
    displacement, derivative, _ = lateral(s) if component == 'lower' else (0., 0., 0.)
    normal = 1.0 / math.hypot(1.0, derivative)
    return (16.0 - displacement, 8.0 - s), (normal, -derivative * normal)


def lane_point(component, source_class, s, *, mirrored=False, variant=None):
    """Return one measured native lane in world east/north/height metres."""
    require(component in ('upper', 'lower') and source_class in (0, 1), 'Unknown transition lane')
    phase = phase_for_options(mirrored=mirrored, variant=variant)
    if phase.native_cross_section_reflection:
        source_class = 1-source_class
    if phase.key == LOWER_BEND_RIGHT:
        center, normal = lower_bend_frame(component, s)
        offset = (-2.5, 2.5)[source_class] if component == 'upper' else (2.5, -2.5)[source_class]
        height = straight_upper_height(s) if component == 'upper' else lower_height(s)
        return center[0] + offset*normal[0], center[1] + offset*normal[1], height
    if phase.physical_reflection:
        east, north, height = lane_point(component, source_class, s)
        return 16.0-east, north, height
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


@lru_cache(maxsize=8)
def _expected_routes(mirrored=False, *, variant=None):
    phase = phase_for_options(mirrored=mirrored, variant=variant)
    result = {cell: [] for cell in CELLS}
    stations = [index * STATION_STEP for index in range(round(LENGTH / STATION_STEP) + 1)]
    for component in ('upper', 'lower'):
        for source_class in (0, 1):
            points = [lane_point(component, source_class, s, variant=phase.key) for s in stations]
            if (component == 'lower') != phase.traffic_reversed:
                points.reverse()
            for fragment in _slice(points, component, source_class):
                result[fragment['cell']].append(fragment)
    return result


def expected_cell_routes(*, mirrored=False, variant=None):
    return deepcopy(_expected_routes(mirrored, variant=variant))


def _spec(piece):
    phase = phase_for_piece(piece)
    expected_recipe = phase.recipe
    require(piece.get('recipe') == expected_recipe and piece.get('domain') == 'highway',
            'Wrong registered orthogonal DD transition owner or recipe')
    require(piece.get('footprint') == [2, 6] and tuple(map(tuple, piece.get('cells', ()))) == CELLS,
            'Orthogonal DD transition must retain all twelve row-major owned cells')
    tiles = tuple(map(_number, piece.get('tile_ids', ())))
    require(len(tiles) == len(set(tiles)) == 12, 'Orthogonal transition needs twelve distinct canonical cells')
    engineering = piece.get('engineering', {})
    empty = {cell for cell, records in _expected_routes(variant=phase.key).items() if not records}
    require(set(map(tuple, engineering.get('model_only_cells', ()))) == empty,
            'Transition model-only cells differ from the independently reconstructed lanes')
    require(type(engineering.get('max_grade_percent')) in (float, int)
            and 0.0 < engineering['max_grade_percent'] <= 30.0,
            'Transition must retain an explicit lane-grade ceiling no greater than thirty percent')
    if phase.native_cross_section_reflection:
        require(engineering['max_grade_percent'] <= 20.,
                'Opposite-side transition must retain the reviewed twenty-percent lane-grade ceiling')
    require(engineering.get('car_corridor_half_width_m') == 1.25
            and engineering.get('car_corridor_height_m') == 3.8,
            'Transition corridor must retain its declared 2.5m-by-3.8m vehicle envelope')
    require(piece.get('shadow_mappings') == [] and not piece.get('model_shadows', {}).get('enabled', True),
            'Orthogonal transition must explicitly disable custom shadows')
    return tiles


def external_ports(*, mirrored=False, variant=None):
    phase = phase_for_options(mirrored=mirrored, variant=variant)
    result = []
    for component in ('upper', 'lower'):
        for source_class in (0, 1):
            lane = f'{component}-lane-{source_class + 1:02d}'
            for direction in ('in', 'out'):
                s = (0.0 if direction == 'in' else LENGTH) if component == 'upper' else (
                    LENGTH if direction == 'in' else 0.0)
                if phase.traffic_reversed:
                    s = LENGTH-s
                if phase.key == LOWER_BEND_RIGHT:
                    cell = (1, 0) if s == 0.0 else ((1, 5) if component == 'upper' else (0, 5))
                else:
                    cell = (1, 0) if s == 0.0 else ((0, 5) if component == 'upper' else (1, 5))
                if phase.physical_reflection:
                    cell = 1-cell[0], cell[1]
                tangent = -1.0 if component == 'upper' else 1.0
                if phase.traffic_reversed:
                    tangent = -tangent
                result.append({'id': lane + '-' + direction, 'channel_id': lane, 'component': component,
                    'source_class': source_class, 'direction': direction, 'transport': 1,
                    'point_m': lane_point(component, source_class, s, variant=phase.key), 'source_cell': list(cell),
                    'edge': 1 if s == 0.0 else 3,
                    'tangent': (0.0, tangent), 'grade': 0.0})
    return result


def reviewed_contract(piece):
    _spec(piece)
    ports = external_ports(variant=phase_for_piece(piece).key)
    return {'boundary_measurement_precision': 'saved-path',
        'ports': {p['id']: list(p['point_m']) for p in ports},
        'port_vectors': {p['id']: list(p['tangent']) for p in ports},
        'port_transports': {p['id']: 1 for p in ports},
        'port_directions': {p['id']: p['direction'] for p in ports},
        'movements': [[f'{component}-lane-{lane:02d}-in', f'{component}-lane-{lane:02d}-out']
                      for component in ('upper', 'lower') for lane in (1, 2)]}


def check_opposite_end_direction_pair(*, opposite_side=False):
    """A at 0 degrees and B at 180 degrees preserve the same DD flow.

    Translate the rotated B by (16,16) metres solely to compare the adjoining
    DD boundary planes. This is a lane-direction proof, not a claim that the
    two optional construction helpers permit direct touching placement.
    """
    require(type(opposite_side) is bool, 'Transition pair side must be an exact boolean')
    first, second = ('opposite-side', 'opposite-side-mirrored') if opposite_side else ('original', 'mirrored')
    original = [p for p in external_ports(variant=first) if p['point_m'][2] > 0.]
    mirrored = [p for p in external_ports(variant=second) if p['point_m'][2] > 0.]
    checked = []
    for port in original:
        target = next(p for p in mirrored if p['channel_id'] == port['channel_id'])
        posed = _rotate(target['point_m'], 2)
        posed = posed[0]+16., posed[1]+16., posed[2]
        tangent = _rotate((*target['tangent'], 0.), 2)[:2]
        require(math.dist(posed, port['point_m']) <= 1e-12 and tangent == port['tangent']
                and target['direction'] != port['direction'] and target['source_class'] == port['source_class']
                and (target['edge']+2) % 4 == (port['edge']+2) % 4,
                'Facing original/mirrored transitions do not preserve the same directed native DD lane')
        checked.append({'original_port': port['id'], 'mirrored_port': target['id'],
                        'point_m': list(posed), 'travel_tangent': list(tangent)})
    return {'passed': True, 'native_dd_lanes_checked': len(checked),
            'original_quarter_turns': 0, 'mirrored_quarter_turns': 2,
            'translation_for_boundary_comparison_m': [16., 16.], 'lanes': checked,
            'construction_or_game_connection_tested': False}


def reviewed_facts(piece):
    """Independent intrinsic semantics; actual byte hashes need a later freeze."""
    contract = reviewed_contract(piece)
    ports = []
    channels = []
    for p in external_ports(variant=phase_for_piece(piece).key):
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
    return {'reference_piece_id': piece['id'], 'footprint': [2, 6], 'cells': [list(cell) for cell in CELLS],
            'path_hashes_by_cell': [], 'raw_path_fingerprint_status': 'requires-checked-saved-build-freeze',
            'ports': ports, 'movements': movements, 'forbidden_transfers': forbidden,
            'components': [{'id': c + '-carriageway', 'network': 'road', 'construction_network': 'dirtroad'}
                           for c in ('upper', 'lower')], 'channels': channels}


def _same_route(actual, expected):
    if any(actual[key] != expected[key] for key in ('transport', 'lane', 'entry', 'exit', 'compatibility')):
        return False
    return len(actual['points']) == len(expected['points']) and all(
        math.dist(a, b) <= POSITION_TOLERANCE for a, b in zip(actual['points'], expected['points']))


def _journeys(routes, turns, *, mirrored=False, variant=None):
    starts, ends = defaultdict(list), defaultdict(list)
    for index, route in enumerate(routes):
        starts[_point(_rotate(route['points'][0], turns))].append(index)
        ends[_point(_rotate(route['points'][-1], turns))].append(index)
    require(all(len(indices) == 1 for indices in (*starts.values(), *ends.values())),
            'Transition has an ambiguous lane/deck connection')
    incoming, outgoing = starts.keys() - ends.keys(), ends.keys() - starts.keys()
    literal = external_ports(mirrored=mirrored, variant=variant)
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
    phase = phase_for_piece(piece)
    expected = _expected_routes(variant=phase.key)
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
    rotations = [_journeys(routes, turns, variant=phase.key) for turns in range(4)]
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


def _terrain_vertex_components(constraints, turns):
    """Expand measured native code7 equalities; this is not a height solver.

    Windows641 parses '#' as7 and inserts equality(0,1), equality(0,2),
    equality(0,3) for each such cell. Shared city vertices identify adjacent
    cells. Rotation changes coordinates, without selecting an absolute height.
    """
    def rotated(point):
        x, y = point
        for _ in range(turns):
            x, y = -y, x
        return x, y

    corners = {cell: tuple(rotated((cell[0]+dx, cell[1]+dy))
                           for dx, dy in ((0, 0), (1, 0), (1, 1), (0, 1))) for cell in CELLS}
    parents = {point: point for points in corners.values() for point in points}

    def root(point):
        while parents[point] != point:
            point = parents[point]
        return point

    for (x, y), points in corners.items():
        if constraints[y][x] == '#':
            for point in points[1:]:
                parents[root(point)] = root(points[0])
    groups = defaultdict(list)
    for point in parents:
        groups[root(point)].append(point)
    return sorted(sorted(points) for points in groups.values())


def check_mirrored_terrain_constraints(fields, piece):
    """Require the selected flat-base policy; retain the original's old rules."""
    require(phase_for_piece(piece).key != 'original',
            'Flat-base terrain policy is restricted to the mirrored transition and new opposite-side types')
    constraints = ['##.<', '##..', '##..', '##..', '##..', '##..', '^...']
    require(fields.get('ConsLayout') == constraints,
            'Mirrored transition terrain constraints require native # on all twelve owned cells')
    rotations = []
    for turns in range(4):
        groups = _terrain_vertex_components(fields['ConsLayout'], turns)
        require(len(groups) == 1 and len(groups[0]) == 21,
                'Mirrored transition terrain constraints do not join all twenty-one ground vertices')
        rotations.append({'quarter_turns': turns, 'constrained_vertices': 21, 'flat_height_groups': 1})
    return {'constraint_symbol': '#', 'native_constraint_code': 7, 'owned_cells_checked': 12,
            'inserted_equality_pairs': 36, 'proper_rotations_checked': 4, 'proper_rotations': rotations,
            'absolute_world_height_fixed': False, 'authored_path_heights_changed': False,
            'game_terrain_behavior_tested': False}


def check_construction_fields(fields, piece, resources):
    """Inspect the restored twelve-cell core separately from native helpers."""
    tiles = _spec(piece)
    phase = phase_for_piece(piece)
    expected = _expected_routes(variant=phase.key)
    words = MIRRORED_CORE_ROAD_WORDS if phase.physical_reflection else CORE_ROAD_WORDS
    require(tuple(_construction_word(expected[cell]) for cell in CELLS) == words,
            'Independent transition tangent flags disagree with the reviewed native construction words')
    layouts = ['ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', '^...']
    symbol = '+' if phase.key == 'original' else '#'
    constraints = [symbol*2+'.<', *[symbol*2+'..']*5, '^...']
    require(fields.get('CellLayout') == layouts and fields.get('ConsLayout') == constraints,
            'Transition construction changes twelve-cell ownership, the model-only shoulder, or core anchors')
    require(fields.get('Costs') == ['1000'], 'Unexpected orthogonal transition construction cost')
    checks = fields.get('CheckType', [])
    require(len(checks) == 12, 'Transition construction needs exactly twelve core palette entries')
    for index, (cell, tile, word) in enumerate(zip(CELLS, tiles, words)):
        match = re.fullmatch(chr(ord('a') + index) + r'\s*-\s*dirtroad:\s*0x([0-9a-fA-F]{8})', checks[index])
        require(match is not None and int(match[1], 16) == word,
                'Transition core construction network or endpoint-tangent flags differ')
        actual = parse_paths(resources[*PATH, tile])
        require(_construction_word(actual['routes']) == word,
                'Actual saved transition PATH directions disagree with construction flags')
    report = {'occupied_cells_checked': 12, 'model_only_owned_cells_checked': 1,
            'native_core_tangent_flag_words_checked': 12, 'core_anchor_and_cost_checked': True,
            'native_helpers_in_scope': False, 'game_construction_tested': False}
    if phase.key != 'original':
        report['terrain_constraints'] = check_mirrored_terrain_constraints(fields, piece)
    return report


def check_models(resources, piece, donors=None):
    from .orthogonal_transition_models_verify import check_models as check_saved_models
    _spec(piece)
    return check_saved_models(resources, piece, donors)
