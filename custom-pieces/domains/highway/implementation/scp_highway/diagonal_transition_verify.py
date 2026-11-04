"""Independent Alignment A traffic and construction expectations.

Native measurements and the reviewed mathematical design are reconstructed
here. Neither the resource writer nor its geometry/layout helpers are used as
an expectation oracle. An unresolved ownership contract fails closed.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from functools import lru_cache
import math
import re
from types import MappingProxyType
from typing import NamedTuple

from scp.dbpf import decompress, require
from scp.track_paths import PATH
from scp.verify import parse_paths


class TransitionPhase(NamedTuple):
    key: str
    piece_id: str
    recipe: str
    physical_reflection: bool
    traffic_reversed: bool


# These literal identities and phase choices are independently declared. In
# particular, native model/UV reflection is not inferred from an XOR flag.
_BASE = 'ddrhw-l1-l2-rhw-l0-ramp-diagonal'
PHASES = MappingProxyType({
    'original': TransitionPhase('original', _BASE+'-alignment-a',
        'highway_ddrhw_diagonal_l0_transition_a', False, False),
    'mirrored': TransitionPhase('mirrored', _BASE+'-mirrored-alignment-a',
        'highway_ddrhw_diagonal_l0_transition_mirrored_a', True, True),
    'opposite-side': TransitionPhase('opposite-side', _BASE+'-opposite-alignment-a',
        'highway_ddrhw_diagonal_l0_transition_opposite_a', True, False),
    'opposite-side-mirrored': TransitionPhase('opposite-side-mirrored',
        _BASE+'-opposite-mirrored-alignment-a',
        'highway_ddrhw_diagonal_l0_transition_opposite_mirrored_a', False, True),
})
SQRT2 = math.sqrt(2.)
LENGTH = 72.*SQRT2
SPREAD = 16.*SQRT2
LANE_OFFSET = 3.2/SQRT2
FLAT_ENVELOPE = 8.656854586667169
CURVE_RUN = 66.
EASE = 8.
STATION_STEP = .125
POSITION_TOLERANCE = 2e-6
MAXIMUM_GRADE_PERCENT = 20.
NEIGHBOURS = ((-1, 0), (0, -1), (1, 0), (0, 1))
J = (8., 0.)
TRANSVERSE = (1./SQRT2, -1./SQRT2)
LONGITUDINAL = (-1./SQRT2, -1./SQRT2)
BREAKS = (0., FLAT_ENVELOPE, FLAT_ENVELOPE+EASE,
          FLAT_ENVELOPE+CURVE_RUN, LENGTH-FLAT_ENVELOPE-EASE,
          LENGTH-FLAT_ENVELOPE, LENGTH)

# Exact independently reviewed masks. Full encoded source05 physical proof:
# cfdb0b02add5f59c7084e42d895252de26e8da076b1e79bfd94b2c10beb38f27.
# Normal DAT containers and game observations remain separate checks.
_CANDIDATE_WORLD_CELLS = MappingProxyType({
    False: ((-6, 3), (-5, 2), (-5, 3), (-4, 1), (-4, 2), (-4, 3), (-4, 4),
        (-3, 1), (-3, 2), (-3, 3), (-3, 4), (-2, 1), (-2, 2), (-2, 3), (-2, 4),
        (-1, 0), (-1, 1), (-1, 2), (-1, 3), (0, -1), (0, 0), (0, 1), (0, 2), (1, 1)),
    True: ((-5, 4), (-4, 3), (-4, 4), (-3, 2), (-3, 3), (-3, 4), (-3, 5),
        (-2, 1), (-2, 2), (-2, 3), (-2, 4), (-2, 5), (-1, 0), (-1, 1), (-1, 2),
        (-1, 3), (-1, 4), (-1, 5), (0, -1), (0, 0), (0, 1), (0, 2), (0, 3), (1, 1)),
})


def _accepted_layout_data(reflected):
    world=_CANDIDATE_WORLD_CELLS[reflected]
    origin=min(c for c,r in world),min(r for c,r in world)
    cells=tuple((c-origin[0],r-origin[1]) for c,r in world)
    width,depth=max(c for c,r in cells)+1,max(r for c,r in cells)+1
    grid=[['.']*(width+2) for _ in range(depth+1)]
    constraints=[row.copy() for row in grid]
    grid[0][-1]=constraints[0][-1]='<'
    grid[-1][0]=constraints[-1][0]='^'
    for index,(c,r) in enumerate(cells):
        grid[r][c]='abcdefghijklmnopqrstuvwxyz'[index]
        constraints[r][c]='#'
    return MappingProxyType({'world_cells':world,'world_origin_cell':origin,'cells':cells,
        'footprint':(width,depth),'cell_layout':tuple(''.join(row) for row in grid),
        'cons_layout':tuple(''.join(row) for row in constraints),'ownership_reviewed':True,
        'accepted_for_allocation':True,'accepted_encoded_source_snapshot_sha256':
            '43f0c7a936ad07b227768d21e7f1ceb183f96a728f38a50d0c9fed169cf703a6',
        'accepted_encoded_source_physical_report_sha256':
            'cfdb0b02add5f59c7084e42d895252de26e8da076b1e79bfd94b2c10beb38f27',
        'normal_DAT_container_verified_by_this_table':False,'game_tested':False})


REVIEWED_LAYOUTS=MappingProxyType({key:_accepted_layout_data(phase.physical_reflection)
    for key,phase in PHASES.items()})


def _number(value):
    return int(value, 16) if isinstance(value, str) else value


def phase_for_options(variant='original'):
    require(isinstance(variant, str) and variant in PHASES,
            'Unknown diagonal transition phase')
    return PHASES[variant]


def phase_for_piece(piece):
    phase = phase_for_options(piece.get('diagonal_transition_variant'))
    require(piece.get('diagonal_transition_alignment') == 'a'
            and piece.get('id') == phase.piece_id
            and piece.get('recipe') == phase.recipe
            and piece.get('domain') == 'highway',
            'Diagonal transition identity, recipe, phase, or alignment differs')
    return phase


def reviewed_layout(variant='original'):
    phase_for_options(variant)
    require(variant in REVIEWED_LAYOUTS,
            'Diagonal transition ownership review is pending; no layout is accepted')
    return REVIEWED_LAYOUTS[variant]


def candidate_layout_for_measurement(variant='original'):
    """Independent finite ROI for source measurements; never an allocation pass."""
    phase = phase_for_options(variant)
    world = _CANDIDATE_WORLD_CELLS[phase.physical_reflection]
    origin = min(c for c, _r in world), min(r for _c, r in world)
    cells = tuple((c-origin[0], r-origin[1]) for c, r in world)
    return {'world_cells': world, 'world_origin_cell': origin, 'cells': cells,
            'footprint': (max(c for c, _r in cells)+1, max(r for _c, r in cells)+1),
            'ownership_reviewed': False, 'accepted_for_allocation': False}


def _rotate(point, turns):
    east, north, height = point
    for _ in range(turns % 4):
        east, north = north, -east
    return east, north, height


def _point(point):
    return tuple(round(v, 6) for v in point)


def _cubic(value):
    value = min(1., max(0., value))
    return value*value*(3.-2.*value)


def lateral(station):
    """Canonical upper displacement, derivative, and signed curvature."""
    t = min(1., max(0., (station-FLAT_ENVELOPE)/CURVE_RUN))
    displacement = -SPREAD*(10.*t**3-15.*t**4+6.*t**5)
    derivative = -SPREAD*30.*t*t*(1.-t)**2/CURVE_RUN
    second = -SPREAD*60.*t*(1.-t)*(1.-2.*t)/CURVE_RUN**2
    return displacement, derivative, second/(1.+derivative*derivative)**1.5


def _weight(station):
    _offset, derivative, curvature = lateral(station)
    easing = _cubic((station-FLAT_ENVELOPE)/EASE)*_cubic(
        (LENGTH-FLAT_ENVELOPE-station)/EASE)
    metric = math.hypot(1., derivative)*(1.-LANE_OFFSET*math.hypot(curvature, .001))
    require(metric > 0., 'Diagonal transition lane metric became singular')
    return easing*metric


@lru_cache(maxsize=1)
def _integrals():
    """Independent composite Simpson integration on a 1/64 m grid."""
    step = 1./64.
    cuts = sorted({0., LENGTH, *BREAKS,
                   *(index*step for index in range(1, math.ceil(LENGTH/step)))})
    prefix = [0.]
    for a, b in zip(cuts, cuts[1:]):
        prefix.append(prefix[-1]+(b-a)*(_weight(a)+4.*_weight((a+b)/2.)+_weight(b))/6.)
    require(prefix[-1] > 75., 'Diagonal transition has insufficient reviewed grade length')
    return tuple(cuts), tuple(prefix), 15./prefix[-1]


def upper_height(station):
    if station <= FLAT_ENVELOPE:
        return 15.
    if station >= LENGTH-FLAT_ENVELOPE:
        return 0.
    from bisect import bisect_right
    cuts, prefix, factor = _integrals()
    index = bisect_right(cuts, station)-1
    a, b = cuts[index], station
    tail = (b-a)*(_weight(a)+4.*_weight((a+b)/2.)+_weight(b))/6.
    return 15.-factor*(prefix[index]+tail)


def lower_height(station):
    return 7.5*(1.-_cubic((station-FLAT_ENVELOPE)/CURVE_RUN))


def frame(component, station, *, variant='original'):
    phase = phase_for_options(variant)
    require(component in ('upper', 'lower'), 'Unknown diagonal transition carriageway')
    p, derivative, _ = lateral(station) if component == 'upper' else (0., 0., 0.)
    sign = -1. if phase.physical_reflection else 1.
    center = tuple(J[i]+sign*TRANSVERSE[i]*p+LONGITUDINAL[i]*station for i in range(2))
    speed = math.hypot(1., derivative)
    normal = tuple((sign*TRANSVERSE[i]-LONGITUDINAL[i]*derivative)/speed for i in range(2))
    return center, normal


def lane_lateral(component, source_class, *, variant='original'):
    phase = phase_for_options(variant)
    require(component in ('upper', 'lower') and type(source_class) is int
            and source_class in (0, 1), 'Unknown diagonal transition lane')
    canonical_class = source_class
    if phase.physical_reflection != phase.traffic_reversed:
        canonical_class = 1-source_class
    return LANE_OFFSET*(1. if (canonical_class == 1) == (component == 'upper') else -1.)


def lane_point(component, source_class, station, *, variant='original'):
    center, normal = frame(component, station, variant=variant)
    offset = lane_lateral(component, source_class, variant=variant)
    height = upper_height(station) if component == 'upper' else lower_height(station)
    return center[0]+offset*normal[0], center[1]+offset*normal[1], height


def _physical_lateral(component, source_class, variant):
    phase = phase_for_options(variant)
    return lane_lateral(component, source_class, variant=variant)*(-1. if phase.physical_reflection else 1.)


def lane_stations(component, source_class, *, variant='original'):
    offset = _physical_lateral(component, source_class, variant)
    first, last = offset, LENGTH-offset
    stations = {first, last, *[b for b in BREAKS if first < b < last]}
    stations.update(index*STATION_STEP for index in range(math.ceil(first/STATION_STEP),
                    math.floor(last/STATION_STEP)+1) if first < index*STATION_STEP < last)
    return tuple(sorted(stations))


def _edge(point):
    e, n, _h = point
    sides = [abs(e+8.) <= POSITION_TOLERANCE, abs(n-8.) <= POSITION_TOLERANCE,
             abs(e-8.) <= POSITION_TOLERANCE, abs(n+8.) <= POSITION_TOLERANCE]
    require(sum(sides) == 1, 'Diagonal PATH endpoint is not on one unambiguous city-cell side')
    return sides.index(True)


def _slice(points, component, source_class, *, variant='original'):
    """Cut directed chords at every crossed city plane, independently."""
    fragments = []
    for first, last in zip(points, points[1:]):
        cuts = [0., 1.]
        for axis in (0, 1):
            delta = last[axis]-first[axis]
            if abs(delta) <= 1e-14:
                continue
            low, high = sorted((first[axis], last[axis]))
            for index in range(math.ceil((low-8.)/16.), math.floor((high-8.)/16.)+1):
                t = (8.+16.*index-first[axis])/delta
                if 1e-12 < t < 1.-1e-12:
                    cuts.append(t)
        cuts = sorted(set(cuts))
        for low, high in zip(cuts, cuts[1:]):
            a = tuple(first[i]+low*(last[i]-first[i]) for i in range(3))
            b = tuple(first[i]+high*(last[i]-first[i]) for i in range(3))
            middle = tuple((x+y)/2. for x, y in zip(a, b))
            cell = math.floor((middle[0]+8.)/16.), math.floor((8.-middle[1])/16.)
            if fragments and fragments[-1]['cell'] == cell:
                require(math.dist(fragments[-1]['points'][-1], a) < 1e-8,
                        'Independent diagonal city cut is discontinuous')
                fragments[-1]['points'].append(b)
            else:
                fragments.append({'cell': cell, 'points': [a, b]})
    result = []
    ground_n = (-88. if phase_for_options(variant).physical_reflection else -56.) if component == 'upper' else -72.
    for fragment in fragments:
        c, r = fragment['cell']
        local = [(p[0]-16.*c, p[1]+16.*r, p[2]) for p in fragment['points']]
        at_ground = any(abs(p[1]-ground_n) <= POSITION_TOLERANCE and p[2] == 0.
                        for p in (fragment['points'][0], fragment['points'][-1]))
        at_dd = any(abs(p[0]-8.) <= POSITION_TOLERANCE and p[2] in (7.5, 15.)
                    for p in (fragment['points'][0], fragment['points'][-1]))
        result.append({'cell': fragment['cell'], 'component': component, 'source_class': source_class,
            'transport': 1, 'lane': source_class+int(at_ground), 'compatibility': 0,
            'entry': _edge(local[0]), 'exit': _edge(local[-1]), 'points': local,
            'source_route_id': f'{component}-lane-{source_class}',
            'native_contact': 'ground' if at_ground else 'dd' if at_dd else None})
    return result


@lru_cache(maxsize=4)
def _world_expected_routes(variant='original'):
    phase = phase_for_options(variant)
    result = defaultdict(list)
    for component in ('upper', 'lower'):
        for lane in (0, 1):
            points = [lane_point(component, lane, s, variant=variant)
                      for s in lane_stations(component, lane, variant=variant)]
            if (component == 'lower') != phase.traffic_reversed:
                points.reverse()
            for fragment in _slice(points, component, lane, variant=variant):
                result[fragment['cell']].append(fragment)
    for fragments in result.values():
        fragments.sort(key=lambda r: (r['native_contact'] is None, r['source_route_id']))
        used = defaultdict(set)
        for route in fragments:
            key = route['transport'], route['entry'], route['exit']
            if route['native_contact']:
                require(route['lane'] not in used[key],
                        'Independent diagonal native boundary lane classes collide')
            else:
                while route['lane'] in used[key]:
                    route['lane'] += 1
            used[key].add(route['lane'])
    return dict(result)


def _routes_for_layout(variant,layout):
    expected = deepcopy(_world_expected_routes(variant))
    ox, oy = layout['world_origin_cell']
    result = {tuple(cell): [] for cell in layout['cells']}
    for (x, y), routes in expected.items():
        local = x-ox, y-oy
        require(local in result, 'Reviewed diagonal lane leaves its accepted owner cells')
        for route in routes:
            route['cell'] = local
        result[local] = routes
    return result


def expected_cell_routes(*, variant='original', world=False):
    if world:
        return deepcopy(_world_expected_routes(variant))
    return _routes_for_layout(variant,reviewed_layout(variant))


def external_ports(*, variant='original', world=False,_source_layout=None):
    phase = phase_for_options(variant)
    origin = (0, 0) if world else (_source_layout or reviewed_layout(variant))['world_origin_cell']
    result = []
    for component in ('upper', 'lower'):
        for lane in (0, 1):
            offset = _physical_lateral(component, lane, variant)
            dd_in = (component == 'upper') != phase.traffic_reversed
            name = f'{component}-lane-{lane+1:02d}'
            for dd in (True, False):
                station = offset if dd else LENGTH-offset
                point = lane_point(component, lane, station, variant=variant)
                tangent_sign = 1. if dd_in else -1.
                direction = 'in' if dd == dd_in else 'out'
                tangent = tuple(tangent_sign*v for v in LONGITUDINAL)
                inward = tangent_sign if direction == 'in' else -tangent_sign
                near = tuple(point[i]+inward*LONGITUDINAL[i]*1e-3 for i in range(2))
                cell = math.floor((near[0]+8.)/16.)-origin[0], math.floor((8.-near[1])/16.)-origin[1]
                result.append({'id': name+'-'+direction, 'channel_id': name, 'component': component,
                    'source_class': lane, 'native_class': lane if dd else lane+1,
                    'direction': direction, 'transport': 1, 'edge': 2 if dd else 3,
                    'point_m': (point[0]-16.*origin[0], point[1]+16.*origin[1], point[2]),
                    'source_cell': list(cell), 'tangent': tangent, 'grade': 0.})
    return result


def _spec(piece,*,_source_only=False):
    phase = phase_for_piece(piece)
    layout = candidate_layout_for_measurement(phase.key) if _source_only else reviewed_layout(phase.key)
    cells = tuple(map(tuple, piece.get('cells', ())))
    require(cells == tuple(map(tuple, layout['cells'])) and piece.get('footprint') == list(layout['footprint']),
            'Diagonal transition changes its independently reviewed ownership')
    tiles = tuple(map(_number, piece.get('tile_ids', ())))
    require(len(tiles) == len(set(tiles)) == len(cells), 'Diagonal transition tile identities are incomplete')
    expected = _routes_for_layout(phase.key,layout)
    engineering = piece.get('engineering', {})
    empty = {cell for cell, routes in expected.items() if not routes}
    require(set(map(tuple, engineering.get('model_only_cells', ()))) == empty,
            'Diagonal transition model-only cells differ from complete measured lanes')
    require(type(engineering.get('max_grade_percent')) in (float, int)
            and 0. < engineering['max_grade_percent'] <= MAXIMUM_GRADE_PERCENT,
            'Diagonal transition must retain its reviewed twenty-percent grade ceiling')
    require(engineering.get('car_corridor_half_width_m') == 1.25
            and engineering.get('car_corridor_height_m') == 3.8,
            'Diagonal transition changes its measured vehicle envelope')
    require(piece.get('shadow_mappings') == [] and not piece.get('model_shadows', {}).get('enabled', True),
            'Diagonal transition must explicitly disable custom shadows')
    return tiles


def validate_layout_metadata(row, variant='original'):
    """Preallocation guard against the independent accepted finite mask.

    This requires no tile IDs and accepts no author-provided review flag as
    evidence. Source module rows intentionally need not have a domain field.
    """
    phase = phase_for_options(variant)
    layout = reviewed_layout(variant)
    require(row.get('id') == phase.piece_id and row.get('recipe') == phase.recipe
            and row.get('diagonal_transition_variant') == variant
            and row.get('diagonal_transition_alignment') == 'a',
            'Preallocation diagonal layout identity, recipe, phase, or cut differs')
    require(tuple(map(tuple, row.get('cells', ()))) == tuple(map(tuple, layout['cells']))
            and tuple(row.get('footprint', ())) == tuple(layout['footprint'])
            and tuple(row.get('world_origin_cell', ())) == tuple(layout['world_origin_cell']),
            'Preallocation diagonal layout differs from independently reviewed finite ownership')
    expected = expected_cell_routes(variant=variant)
    empty = {cell for cell, routes in expected.items() if not routes}
    require(set(map(tuple, row.get('engineering', {}).get('model_only_cells', ()))) == empty,
            'Preallocation diagonal model-only cells differ from independently reconstructed lanes')
    return {'accepted_for_allocation': True, 'variant': variant, 'alignment': 'a',
            'world_origin_cell': list(layout['world_origin_cell']),
            'cells': [list(c) for c in layout['cells']], 'footprint': list(layout['footprint']),
            'routed_cells': len(expected)-len(empty), 'model_only_cells': len(empty),
            'saved_resource_physical_acceptance_supplied': False, 'game_tested': False}


def _same_route(actual, expected):
    return all(actual[k] == expected[k] for k in ('transport', 'lane', 'entry', 'exit', 'compatibility')) and (
        len(actual['points']) == len(expected['points']) and all(math.dist(a, b) <= POSITION_TOLERANCE
        for a, b in zip(actual['points'], expected['points'])))


def _journeys(routes, turns, *, variant='original',ports=None):
    starts, ends = defaultdict(list), defaultdict(list)
    for index, route in enumerate(routes):
        starts[_point(_rotate(route['points'][0], turns))].append(index)
        ends[_point(_rotate(route['points'][-1], turns))].append(index)
    require(all(len(v) == 1 for v in (*starts.values(), *ends.values())),
            'Diagonal transition has ambiguous lane or deck connections')
    incoming, outgoing = starts.keys()-ends.keys(), ends.keys()-starts.keys()
    ports = ports or external_ports(variant=variant)
    require(incoming == {_point(_rotate(p['point_m'], turns)) for p in ports if p['direction'] == 'in'}
            and outgoing == {_point(_rotate(p['point_m'], turns)) for p in ports if p['direction'] == 'out'},
            'Diagonal transition changes its complete eight-member native boundary')
    consumed, movements = set(), []
    for port in (p for p in ports if p['direction'] == 'in'):
        index = starts[_point(_rotate(port['point_m'], turns))][0]
        sequence = []
        while True:
            require(index not in consumed, 'Diagonal transition contains a loop or cross-lane transfer')
            consumed.add(index)
            sequence.append(index)
            end = _point(_rotate(routes[index]['points'][-1], turns))
            if end in outgoing:
                break
            require(end in starts, 'Diagonal transition lane ends inside its owner')
            index = starts[end][0]
        target = next(p for p in ports if p['channel_id'] == port['channel_id'] and p['direction'] == 'out')
        require(end == _point(_rotate(target['point_m'], turns)),
                'Diagonal transition changes lane or carriageway')
        movements.append({'entry_port': port['id'], 'exit_port': target['id'], 'route_fragments': len(sequence)})
    require(len(consumed) == len(routes), 'Diagonal transition contains a capacity-only route')
    return {'quarter_turns': turns, 'complete_directed_journeys': 4,
            'external_directional_members': 8, 'route_fragments_consumed': len(consumed),
            'no_lane_or_carriageway_transfers': True, 'journeys': movements}


def _check_paths(resources,piece,*,_source_only=False):
    tiles = _spec(piece,_source_only=_source_only)
    phase = phase_for_piece(piece)
    layout=candidate_layout_for_measurement(phase.key) if _source_only else reviewed_layout(phase.key)
    expected = _routes_for_layout(phase.key,layout)
    routes, maximum, error = [], 0., 0.
    for cell, tile in zip(map(tuple, piece['cells']), tiles):
        require((*PATH, tile) in resources, 'Missing diagonal transition PATH cell')
        parsed = parse_paths(decompress(resources[*PATH, tile]))
        require(parsed['version'] == '1.2' and parsed['terrain'] == 1,
                'Diagonal transition PATH must explicitly retain authored elevations')
        remaining = list(expected[cell])
        for actual in parsed['routes']:
            matches = [i for i, wanted in enumerate(remaining) if _same_route(actual, wanted)]
            require(len(matches) == 1, 'Saved diagonal PATH differs from independent curves, native classes, or city cuts')
            wanted = remaining.pop(matches[0])
            error = max(error, max(math.dist(a, b) for a, b in zip(actual['points'], wanted['points'])))
            require(_edge(actual['points'][0]) == actual['entry'] and _edge(actual['points'][-1]) == actual['exit'],
                    'Diagonal PATH entry or exit does not match its actual position')
            require(all(abs(p[0]) <= 8.+POSITION_TOLERANCE and abs(p[1]) <= 8.+POSITION_TOLERANCE
                        for p in actual['points']), 'Diagonal PATH leaves its owning city cell')
            world = [(p[0]+16.*cell[0], p[1]-16.*cell[1], p[2]) for p in actual['points']]
            for first, last in zip(world, world[1:]):
                run = math.dist(first[:2], last[:2])
                require(run > 1e-10, 'Diagonal PATH has a stationary or vertical segment')
                grade = 100.*abs(last[2]-first[2])/run
                maximum = max(maximum, grade)
                require(grade <= piece['engineering']['max_grade_percent']+1e-5,
                        'Saved diagonal PATH exceeds its declared lane-grade ceiling')
            routes.append({**actual, 'cell': cell, 'points': world})
        require(not remaining, 'Saved diagonal PATH omits a measured lane fragment')
    ports=external_ports(variant=phase.key,_source_layout=layout)
    rotations = [_journeys(routes, turns, variant=phase.key,ports=ports) for turns in range(4)]
    return {'passed': True, 'tile_count': len(tiles), 'route_fragments_checked': len(routes),
            'complete_directed_journeys': 4, 'complete_native_boundary_members_checked': 8,
            'proper_rotations_checked': 4, 'proper_rotations': rotations,
            'maximum_grade_percent': maximum, 'maximum_coordinate_error_m': error,
            'model_only_cells': [list(c) for c, r in expected.items() if not r],
            'use_path_elevation': True, 'no_capacity_only_paths': True,
            'no_lane_or_carriageway_transfers': True, 'game_operation_tested': False}


def check_paths(resources,piece):
    return _check_paths(resources,piece)


def check_source_paths(resources,piece):
    """Check encoded preallocation PATHs against the independent finite candidate.

    This does not approve the unresolved model surfaces, change the reviewed
    allocation mask, or bypass the ordinary saved-resource entry point.
    """
    result=_check_paths(resources,piece,_source_only=True)
    return {**result,'stage':'encoded-source-path-check','accepted_for_allocation':False,
        'complete_physical_acceptance':False}


def decoded_journeys(resources, piece,*,_source_only=False):
    """Join checked actual saved fragments without depending on comments."""
    _check_paths(resources,piece,_source_only=_source_only)
    phase = phase_for_piece(piece)
    layout=candidate_layout_for_measurement(phase.key) if _source_only else reviewed_layout(phase.key)
    fragments = []
    for cell, tile in zip(piece['cells'], piece['tile_ids']):
        for row in parse_paths(decompress(resources[*PATH, _number(tile)]))['routes']:
            fragments.append([(p[0]+16.*cell[0], p[1]-16.*cell[1], p[2]) for p in row['points']])
    starts = {_point(points[0]): points for points in fragments}
    result = []
    ports=external_ports(variant=phase.key,_source_layout=layout)
    for port in (p for p in ports if p['direction'] == 'in'):
        target = next(p for p in ports
                      if p['channel_id'] == port['channel_id'] and p['direction'] == 'out')
        current = _point(port['point_m'])
        points, consumed = [], set()
        while current != _point(target['point_m']):
            require(current in starts and current not in consumed, 'Actual diagonal journey is broken or cyclic')
            consumed.add(current)
            row = starts[current]
            points.extend(row if not points else row[1:])
            current = _point(row[-1])
        result.append({'id': port['channel_id'], 'component': port['component'],
                       'source_class': port['source_class'], 'points': points})
    return result


def reviewed_contract(piece):
    _spec(piece)
    ports = external_ports(variant=phase_for_piece(piece).key)
    return {'boundary_measurement_precision': 'saved-path',
        'ports': {p['id']: list(p['point_m']) for p in ports},
        'port_vectors': {p['id']: list(p['tangent']) for p in ports},
        'port_transports': {p['id']: 1 for p in ports},
        'port_directions': {p['id']: p['direction'] for p in ports},
        'movements': [[f'{d}-lane-{lane:02d}-in', f'{d}-lane-{lane:02d}-out']
                      for d in ('upper', 'lower') for lane in (1, 2)]}


def native_socket_bindings(variant='original'):
    """Independent actual first-cut donor IDs, proper poses, and city cells."""
    phase = phase_for_options(variant)
    reversed_traffic = phase.traffic_reversed
    return {
        'dd': ((0x57530200 if reversed_traffic else 0x57530900), 2, (1, 0)),
        'upper': ((0x57030200 if reversed_traffic else 0x57030900), 2,
                  (-3, 6) if phase.physical_reflection else (-5, 4)),
        'lower': ((0x57030900 if reversed_traffic else 0x57030200), 2, (-4, 5)),
    }


def native_vehicle_routes(donors=None,*,variant='original'):
    """Original finite helper/peer car chords with explicit component/cell facts."""
    from . import diagonal_transition_native as native
    result=[];cells={'upper':set(),'lower':set()}
    for arm,(tile,pose,cell) in native_socket_bindings(variant).items():
        if arm=='dd':
            peer=(0x57530900 if tile==0x57530200 else 0x57530200,0,(1,-1))
        else:
            peer=(0x57030900 if tile==0x57030200 else 0x57030200,0,(cell[0]-1,cell[1]))
        for owner,placement in (('helper',(tile,pose,cell)),('outward-peer',peer)):
            for index,row in enumerate(native.source_paths(donors,*placement)):
                component=('upper' if row['points'][0][2]==15. else 'lower') if arm=='dd' else arm
                cells[component].add(tuple(placement[2]))
                if owner!='helper':
                    continue
                result.append({'id':f'native-{arm}-{owner}-{index}','component':component,
                    'arm':arm,'points':row['points'],'native_tile_id':placement[0],
                    'native_pose_clockwise':placement[1],'native_world_cell':tuple(placement[2]),
                    'native_lane_class':row['lane']})
    require(len(result)==8,'Native helper vehicle window must have exactly eight directed source lanes')
    return result,{component:tuple(sorted(values)) for component,values in cells.items()}


def check_native_boundaries(donors, piece, resources,*,_source_only=False):
    """Compare every actual saved endpoint with an original posed native lane."""
    _spec(piece,_source_only=_source_only)
    from . import diagonal_transition_native as native
    phase = phase_for_piece(piece)
    bindings = native_socket_bindings(phase.key)
    source = {arm: native.source_paths(donors, tile, pose, cell)
              for arm, (tile, pose, cell) in bindings.items()}
    layout=candidate_layout_for_measurement(phase.key) if _source_only else reviewed_layout(phase.key)
    ports = external_ports(variant=phase.key,_source_layout=layout)
    ox, oy = layout['world_origin_cell']
    by_cell = dict(zip(map(tuple, piece['cells']), map(_number, piece['tile_ids'])))
    comparisons = []
    for port in ports:
        arm = 'dd' if port['point_m'][2] > 0. else port['component']
        first = port['direction'] == 'in'
        rows = parse_paths(decompress(resources[*PATH, by_cell[tuple(port['source_cell'])]]))['routes']
        endpoint = tuple(port['point_m'])
        offset = (16.*port['source_cell'][0], -16.*port['source_cell'][1], 0.)
        candidates = [r for r in rows if r['transport'] == 1 and r['compatibility'] == 0
                      and r['lane'] == port['native_class']
                      and math.dist(tuple(p+q for p, q in zip(r['points'][0 if first else -1], offset)), endpoint)
                      <= POSITION_TOLERANCE]
        require(len(candidates) == 1, 'Actual diagonal native endpoint lacks a unique saved lane')
        actual = candidates[0]
        segment = actual['points'][:2] if first else actual['points'][-2:]
        delta = tuple(b-a for a, b in zip(*segment))
        tangent = tuple(v/math.hypot(*delta[:2]) for v in delta[:2])
        global_endpoint = endpoint[0]+16.*ox, endpoint[1]-16.*oy, endpoint[2]
        native_members = [r for r in source[arm] if r['transport'] == 1 and r['compatibility'] == 0
                          and r['lane'] == port['native_class']
                          and math.dist(r['points'][-1 if first else 0], global_endpoint) <= POSITION_TOLERANCE]
        require(len(native_members) == 1, 'Diagonal source phase/class does not meet its complete actual native boundary')
        member = native_members[0]
        native_delta = tuple(b-a for a, b in zip(member['points'][0], member['points'][-1]))
        native_tangent = tuple(v/math.hypot(*native_delta[:2]) for v in native_delta[:2])
        require(member['exit' if first else 'entry'] == (port['edge']+2)%4,
                'Diagonal native helper does not face the actual SCP boundary')
        for turns in range(4):
            require(math.dist(_rotate(global_endpoint, turns),
                              _rotate(member['points'][-1 if first else 0], turns)) <= POSITION_TOLERANCE
                    and math.dist(_rotate((*tangent, 0.), turns),
                                  _rotate((*native_tangent, 0.), turns)) <= 1e-6,
                    'Saved diagonal native position, height, or travel tangent differs in a proper rotation')
        comparisons.append({'port_id': port['id'], 'arm': arm, 'native_lane_class': port['native_class'],
            'native_tile_id': f'{bindings[arm][0]:08x}', 'pose_clockwise_quarter_turns': bindings[arm][1],
            'native_world_cell': list(bindings[arm][2]), 'native_endpoint_ENH_m': list(global_endpoint),
            'entry_exit_complementary': True})
    require(len(comparisons) == 8, 'Diagonal native audit did not cover every exterior lane')
    return {'passed': True, 'native_boundary_members_per_rotation': 8,
            'proper_rotations_checked': 4, 'directed_native_comparisons': 32,
            'native_lane_positions_classes_heights_and_tangents_checked': True,
            'native_source_pins_enforced': True, 'members': comparisons,
            'native_dragging_game_tested': False}


def reviewed_facts(piece):
    accepted = reviewed_contract(piece)
    phase = phase_for_piece(piece)
    ports = []
    routes = expected_cell_routes(variant=phase.key)
    for p in external_ports(variant=phase.key):
        height = p['point_m'][2]
        cell = tuple(p['source_cell'])
        matches = [r for r in routes[cell] if r['component'] == p['component']
                   and r['source_class'] == p['source_class']]
        require(len(matches) == 1, 'Diagonal public boundary lacks a unique independent source route')
        row = matches[0]
        segment = row['points'][:2] if p['direction'] == 'in' else row['points'][-2:]
        # Independently reproduce the specified9f PATH serialization before
        # the shared graph's six-decimal rounding. Analytic port vectors stay
        # separate; a rounded short chord is not their authority.
        saved = [(float(f'{a:.9f}')+16.*cell[0], float(f'{b:.9f}')-16.*cell[1], float(f'{h:.9f}'))
                 for a, b, h in segment]
        graph = [_point(point) for point in saved]
        delta = tuple(b-a for a, b in zip(*graph))
        norm = math.hypot(*delta[:2])
        require(norm > 0., 'Diagonal public boundary chord collapses under graph precision')
        sampled = [v/norm for v in delta[:2]]
        tangent_norm = math.hypot(*p['tangent'])
        ports.append({'id': p['id'], 'direction': p['direction'], 'engine_transport': 1,
            'edge': p['edge'], 'endpoint_m': list(_point(p['point_m'])),
            'sampled_tangent': sampled, 'tangent': [v/tangent_norm for v in p['tangent']], 'grade': 0.,
            'service_network': 'road', 'service_family': 'road',
            'variant': 'rhw-4-l0' if height == 0. else 'dd-rhw-l2' if height == 15. else 'dd-rhw-l1',
            'role': 'primary', 'channel_kind': 'road-lane', 'traffic_modes': ['car'],
            'source_cell': p['source_cell'], 'channel_id': p['channel_id']})
    channels = [{'id': f'{d}-lane-{lane:02d}', 'component_id': d+'-carriageway',
        'kind': 'road-lane', 'traffic_modes': ['car'],
        'ports': [f'{d}-lane-{lane:02d}-in', f'{d}-lane-{lane:02d}-out']}
        for d in ('upper', 'lower') for lane in (1, 2)]
    movements = list(map(tuple, accepted['movements']))
    return {'reference_piece_id': piece['id'], 'footprint': list(piece['footprint']),
        'cells': deepcopy(piece['cells']), 'path_hashes_by_cell': [],
        'raw_path_fingerprint_status': 'requires-checked-saved-build-freeze',
        'ports': ports, 'channels': channels, 'movements': movements,
        'forbidden_transfers': [(a['id'], b['id']) for a in ports for b in ports
            if a['direction'] == 'in' and b['direction'] == 'out' and (a['id'], b['id']) not in movements],
        'components': [{'id': d+'-carriageway', 'network': 'road', 'construction_network': 'dirtroad'}
                       for d in ('upper', 'lower')]}


def terrain_vertex_components(cells, constraints, turns=0):
    """Apply measured code7 corner equalities, without an altitude solver."""
    def pose(point):
        x, y = point
        for _ in range(turns % 4):
            x, y = -y, x
        return x, y
    corners = {tuple(c): tuple(pose((c[0]+x, c[1]+y)) for x, y in ((0, 0), (1, 0), (1, 1), (0, 1)))
               for c in cells}
    parents = {p: p for ring in corners.values() for p in ring}
    def root(p):
        while parents[p] != p:
            p = parents[p]
        return p
    for (x, y), ring in corners.items():
        require(0 <= y < len(constraints) and 0 <= x < len(constraints[y]),
                'Terrain grid omits an owned cell')
        require(constraints[y][x] == '#', 'Diagonal fixed-base cell lacks native all-corner constraint')
        for point in ring[1:]:
            parents[root(point)] = root(ring[0])
    groups = defaultdict(list)
    for p in parents:
        groups[root(p)].append(p)
    return sorted(sorted(v) for v in groups.values())


def _construction_word(records):
    sides = [0, 0, 0, 0]
    for route in records:
        points = route['points']
        for side, a, b in ((route['entry'], points[0], points[1]),
                           (route['exit'], points[-2], points[-1])):
            dx, dy = b[0]-a[0], b[1]-a[1]
            if abs(dx) < 1e-6 or abs(dy) < 1e-6:
                value = 2
            elif side in (1, 3):
                value = 3 if dx*dy > 0. else 1
            else:
                value = 1 if dx*dy > 0. else 3
            sides[side] = 2 if value == 2 or sides[side] == 2 else value
    return sum(v << (8*i) for i, v in enumerate(sides))


def check_construction_fields(fields, piece, resources):
    _spec(piece)
    layout = reviewed_layout(phase_for_piece(piece).key)
    # The native adapter must independently check and remove optional helper
    # padding before passing this core to the owned-cell checker.
    require(fields.get('CellLayout') == list(layout['cell_layout'])
            and fields.get('ConsLayout') == list(layout['cons_layout']),
            'Diagonal construction changes accepted owners, anchors, or flat-base constraints')
    checks = fields.get('CheckType', [])
    cells = tuple(map(tuple, piece['cells']))
    require(len(checks) == len(cells), 'Diagonal construction palette has missing or additional core owners')
    expected = expected_cell_routes(variant=phase_for_piece(piece).key)
    for cell, tile, row in zip(cells, piece['tile_ids'], checks):
        symbol = fields['CellLayout'][cell[1]][cell[0]]
        match = re.fullmatch(re.escape(symbol)+r'\s*-\s*dirtroad:\s*0x([0-9a-fA-F]{8})', row)
        require(match is not None and int(match[1], 16) == _construction_word(expected[cell]),
                'Diagonal core tangent flags differ from independent lane measurements')
        saved = parse_paths(decompress(resources[*PATH, _number(tile)]))['routes']
        require(_construction_word(saved) == int(match[1], 16),
                'Saved diagonal PATH tangents differ from emitted core flags')
    rotations = []
    for turns in range(4):
        groups = terrain_vertex_components(cells, fields['ConsLayout'], turns)
        require(len(groups) == 1, 'Diagonal fixed-base terrain vertices are not one equality group')
        rotations.append({'quarter_turns': turns, 'constrained_vertices': len(groups[0]), 'flat_height_groups': 1})
    return {'passed': True, 'occupied_cells_checked': len(cells),
            'native_core_tangent_flag_words_checked': len(cells),
            'terrain_constraint_symbol': '#', 'native_constraint_code': 7,
            'inserted_equality_pairs': 3*len(cells), 'proper_rotations': rotations,
            'proper_rotations_checked': 4, 'absolute_world_height_fixed': False,
            'native_helpers_in_scope': False, 'game_construction_tested': False}


def check_placement_handle(fields, piece):
    """Bind the cursor to the owned DD mouth in the independently measured grid."""
    layout = reviewed_layout(phase_for_piece(piece).key)
    # The DD join is on the east edge of source cell (0, 0).
    x, y = (-coordinate for coordinate in layout['world_origin_cell'])
    require((x, y) in layout['cells'] and fields.get('HandleOffset') == [f'{x}, {y}'],
            'Diagonal transition cursor must anchor on the owned DD mouth tile')
    return [x, y]


def check_models(resources, piece, donors=None):
    from .diagonal_transition_models_verify import check_models as saved_models
    return saved_models(resources, piece, donors)
