"""Independently inspect saved compact-diamond resources at registered poses.

The literal construction and native lane contract below is separate from
the module builder. Geometry comes from indexed saved S3D triangles, and
traffic comes from saved PATH bytes. No preview or authoring sample array
is accepted as compiled-resource evidence.
"""
from __future__ import annotations

from collections import Counter, defaultdict, deque
import hashlib
import json
import math
from pathlib import Path

from scp.dbpf import require
from scp.models import parse_s3d, positions, validate_s3d
from scp.verify import parse_paths, strict_dbpf, S3D, PATH

SUBJECT = 'ddrhw-l1-and-l2-diagonal-avenue-diamond'
POSITION_TOLERANCE = 4e-5
MESH_TOLERANCE = 0.04
ROWS = ((8, 9), (5, 6, 7, 8, 9), (2, 3, 4, 5, 6, 7, 8),
        (2, 3, 4, 5, 6, 7, 8), (2, 3, 4, 5, 6, 7),
        (1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7),
        (1, 2, 3, 4, 5, 6), (0, 1, 2, 3), (0, 1))
CONSTRUCTION_CELLS = frozenset((column, row) for row, columns in enumerate(ROWS) for column in columns)
GROUND_JUNCTION_CELLS = frozenset({(2, 2), (3, 2), (4, 2), (2, 3), (3, 3), (2, 4),
    (5, 5), (6, 5), (7, 5), (5, 6), (6, 6), (7, 6), (5, 7), (6, 7),
    (4, 3), (3, 4), (4, 4), (5, 4), (4, 5)})
NATIVE_OVERHANG_CELLS = frozenset({(-1, 8), (0, 7), (0, 10), (7, 0), (8, -1), (10, 0)})
SUPPORT_CELLS = frozenset({(3, 5), (5, 3), (0, 8), (8, 0), (3, 6), (6, 3)})
NEIGHBOURS = ((-1, 0), (0, -1), (1, 0), (0, 1))


def _key(point):
    return tuple(round(value, 6) for value in point)


def _pose(point, angle, origin):
    x, y, h = point
    for _ in range(angle // 90):
        x, y = -y, x
    return x + origin[0], y + origin[1], h


def _direction(points, start):
    a, b = points[:2] if start else points[-2:]
    delta = tuple(b[n] - a[n] for n in range(3)); length = math.hypot(*delta[:2])
    require(length > 1e-9, 'Saved assembly PATH has a zero-length endpoint tangent')
    return (delta[0] / length, delta[1] / length), delta[2] / length


def check_owned_cells(pieces, scene):
    placements = scene.get('placements', scene.get('instances'))
    require(isinstance(placements, list) and len(placements) == 15,
            'Gentler compact diamond requires fifteen registered placements')
    owners, poses = {}, []
    used = set()
    for index, placement in enumerate(placements):
        identifier = placement['piece_id']; require(identifier in pieces, 'Assembly references a missing built component')
        piece = pieces[identifier]; require(piece.get('domain') == 'highway', 'Compact diamond contains a non-highway component')
        angle = placement.get('rotation_degrees_ccw', placement.get('rotation_ccw_degrees', 0))
        origin = placement['origin_m']
        require(angle in (0, 90, 180, 270) and type(angle) is int and len(origin) == 2
                and all(type(v) in (int, float) and math.isfinite(v) for v in origin), 'Invalid saved assembly pose')
        used.add(identifier)
        for local_cell, raw_tile in zip(piece['cells'], piece['tile_ids']):
            centre = _pose((local_cell[0] * 16., -local_cell[1] * 16., 0.), angle, origin)
            cell = round(centre[0] / 16.), round(-centre[1] / 16.)
            require(abs(centre[0] - cell[0] * 16.) < POSITION_TOLERANCE and
                    abs(centre[1] + cell[1] * 16.) < POSITION_TOLERANCE, 'Assembly poses leave the measured city-tile lattice')
            require(cell not in owners, 'Assembly construction cell has more than one owner')
            owners[cell] = {'placement': index, 'piece_id': identifier, 'tile': int(raw_tile, 16),
                            'local_cell': tuple(local_cell), 'angle': angle, 'origin': tuple(origin)}
        poses.append({'piece_id': identifier, 'angle': angle, 'origin': tuple(origin)})
    require(set(owners) == CONSTRUCTION_CELLS, 'Assembly differs from the independent 53-cell construction contract')
    require(len(used) == 13, 'Compact diamond must use thirteen distinct reusable types')
    return owners, poses


def _native_routes(column, row):
    """Native measurements on the unshifted DD and Avenue diagonal lattice."""
    routes = []
    def add(transport, entry, exit_, a, b):
        routes.append({'transport': transport, 'entry': entry, 'exit': exit_, 'points': [a, b]})
    if column + row == 0:
        for x, y in ((3.2, -3.2), (-3.2, 3.2)):
            add(1, 3, 2, (x, -8., 15.), (8., y, 15.))
            add(1, 2, 3, (8., y, 7.5), (x, -8., 7.5))
    elif column + row == 1:
        for y, x in ((-3.2, 3.2), (3.2, -3.2)):
            add(1, 0, 1, (-8., y, 15.), (x, 8., 15.))
            add(1, 1, 0, (x, 8., 7.5), (-8., y, 7.5))
    if column - row in (0, 1):
        if column - row == 0:
            for y, x in ((3.2, 3.2), (-3.2, -3.2)):
                add(1, 2, 1, (8., y, 0.), (x, 8., 0.))
            add(2, 2, 1, (8., 7.3, 0.), (7.3, 8., 0.))
        else:
            for x, y in ((-3.2, -3.2), (3.2, 3.2)):
                add(1, 3, 0, (x, -8., 0.), (-8., y, 0.))
            add(2, 3, 0, (7.3, -8., 0.), (-8., 7.3, 0.))
    if column - row in (0, -1):
        if column - row == 0:
            for y, x in ((3.2, 3.2), (-3.2, -3.2)):
                add(1, 0, 3, (-8., y, 0.), (x, -8., 0.))
            add(2, 0, 3, (-8., -7.3, 0.), (-7.3, -8., 0.))
        else:
            for x, y in ((3.2, 3.2), (-3.2, -3.2)):
                add(1, 1, 2, (x, 8., 0.), (8., y, 0.))
            add(2, 1, 2, (-7.3, 8., 0.), (8., -7.3, 0.))
    return routes


def _arm(point):
    if point[2] > 1.:
        return 'HW_NE' if point[0] + point[1] > 0 else 'HW_SW'
    return 'AVE_NW' if point[0] - point[1] < 136. else 'AVE_SE'


def native_external_contract():
    """Twenty independently measured channels, including both native sidewalks."""
    result = []
    for column, row in sorted(CONSTRUCTION_CELLS):
        for route in _native_routes(column - 4, row - 4):
            for direction, point, edge in (('in', route['points'][0], route['entry']),
                                            ('out', route['points'][-1], route['exit'])):
                step = NEIGHBOURS[edge]
                if (column + step[0], row + step[1]) in CONSTRUCTION_CELLS:
                    continue
                world = (point[0] + 16 * column, point[1] - 16 * row, point[2])
                tangent, grade = _direction(route['points'], direction == 'in')
                result.append({'transport': route['transport'], 'direction': direction, 'point': _key(world),
                               'tangent': tangent, 'grade': grade, 'arm': _arm(world)})
    require(len(result) == 20, 'Independent native external channel contract is inconsistent')
    return sorted(result, key=lambda p: (p['transport'], p['direction'], p['point']))


def decode_placed_routes(owners, piece_resources):
    result = []
    for cell, owner in sorted(owners.items()):
        resources = piece_resources[owner['piece_id']]
        parsed = parse_paths(resources[*PATH, owner['tile']])
        require(parsed['version'] == '1.2' and parsed['terrain'] == 0, 'Compact assembly requires its audited flat PATH encoding')
        for index, route in enumerate(parsed['routes']):
            points = [_pose((p[0] + 16 * owner['local_cell'][0], p[1] - 16 * owner['local_cell'][1], p[2]),
                            owner['angle'], owner['origin']) for p in route['points']]
            result.append({**route, 'points': points, 'cell': cell, 'placement': owner['placement'],
                           'piece_id': owner['piece_id'], 'id': len(result),
                           'entry': (route['entry'] - owner['angle'] // 90) % 4,
                           'exit': (route['exit'] - owner['angle'] // 90) % 4,
                           'source_route_index': index})
    require(result, 'Assembly has no saved traffic routes')
    return result


def _search(start, exits, graph, routes, *, avoid_junctions=False):
    pending, seen = deque([(start, [])]), set()
    while pending:
        key, path = pending.popleft()
        if key in seen:
            continue
        seen.add(key); route = routes[key]
        if avoid_junctions and route['cell'] in GROUND_JUNCTION_CELLS and any(abs(p[2]) < POSITION_TOLERANCE for p in route['points']):
            continue
        path = path + [key]
        if key in exits:
            return path
        pending.extend((next_key, path) for next_key in graph[key] if next_key not in seen)
    return None


def _witness_points(witness, routes):
    """Join decoded saved PATH fragments, retaining their actual sample order."""
    points = []
    for identifier in witness:
        incoming = routes[identifier]['points']
        if points:
            require(math.dist(points[-1], incoming[0]) < POSITION_TOLERANCE,
                    'Saved auxiliary-lane witness has a disconnected route seam')
            points.extend(incoming[1:])
        else:
            points.extend(incoming)
    return points


def _axis_window(points, low, high):
    """Clip actual (longitudinal distance, lateral offset, height) segments."""
    result = []
    cursor = low
    for first, last in zip(points, points[1:]):
        start, finish = first[0], last[0]
        if max(start, finish) <= low + 1e-9 or min(start, finish) >= high - 1e-9:
            continue
        require(finish > start + 1e-9,
                'Saved auxiliary-lane PATH reverses within its flat joining section')
        a, b = max(low, start), min(high, finish)
        if b <= a + 1e-9:
            continue
        require(abs(a - cursor) < POSITION_TOLERANCE,
                'Saved auxiliary-lane PATH skips part of its required joining section')
        pair = [tuple(first[axis] + (distance - start) / (finish - start)
                      * (last[axis] - first[axis]) for axis in range(3))
                for distance in (a, b)]
        result.append(pair)
        cursor = b
    require(result and abs(cursor - high) < POSITION_TOLERANCE,
            'Saved auxiliary-lane PATH misses its complete required joining section')
    return result


def _covers_interval(intervals, low, high):
    cursor = low
    for first, last in sorted(intervals):
        if last < cursor - POSITION_TOLERANCE:
            continue
        if first > cursor + POSITION_TOLERANCE:
            return False
        cursor = max(cursor, last)
        if cursor >= high - POSITION_TOLERANCE:
            return True
    return False


def check_saved_auxiliary_lanes(routes, witnesses):
    """Prove four real flat slip lanes using saved PATHs and literal contracts.

    The high ports, 5.5 m auxiliary offset, taper lengths, and parallel runs
    are independently reviewed expectations. No ramp, mesh, or slip-lane
    authoring helper supplies the expected geometry to this check.
    """
    root = math.sqrt(2.)
    native_offset = 3.2 / root
    contracts = (
        ('lower-off', ('HW_NE', 'AVE_NW'), 1, -1, (56., 51.2), 7.5, 12., 4.),
        ('lower-on', ('AVE_NW', 'HW_SW'), 1, -1, (56., 51.2), 7.5, 12., 4.),
        ('upper-off', ('HW_SW', 'AVE_SE'), -1, 1, (-72., -83.2), 15., 16., 8.),
        ('upper-on', ('AVE_SE', 'HW_NE'), -1, 1, (-72., -83.2), 15., 16., 8.),
    )
    reports = []
    for name, pair, side, direction, native_port, height, taper_length, parallel_length in contracts:
        require(pair in witnesses, 'Saved assembly is missing its required auxiliary-lane transfer')
        witness = witnesses[pair]
        saved = _witness_points(witness, routes)
        on = name.endswith('-on')
        if on:
            saved = list(reversed(saved))
        original_u = sum(native_port) / root

        def coordinates(point):
            # Registered placements translate the native (4,-4) centre to
            # (68,-68). This is a literal saved-layout frame, not generator data.
            x, y, z = point
            u, v = (x + y) / root, (y - x + 136.) / root
            if on:
                u = -u
            return direction * (u - original_u), side * v, z

        local = [coordinates(point) for point in saved]
        end = taper_length + parallel_length
        taper = _axis_window(local, 0., taper_length)
        auxiliary = _axis_window(local, taper_length, end)
        require(all(abs(point[2] - height) < POSITION_TOLERANCE
                    for segment in taper + auxiliary for point in segment),
                'Saved auxiliary lane or lateral taper changes height before the graded ramp')
        require(abs(taper[0][0][1] - native_offset) < POSITION_TOLERANCE
                and abs(taper[-1][-1][1] - 5.5) < POSITION_TOLERANCE,
                'Saved auxiliary taper does not connect the actual native lane to its slip lane')
        maximum_lateral_slope = 0.
        for first, last in taper:
            require(native_offset - POSITION_TOLERANCE <= first[1] <= last[1] + POSITION_TOLERANCE
                    and last[1] <= 5.5 + POSITION_TOLERANCE,
                    'Saved auxiliary taper changes side, reverses, or leaves its lane-change envelope')
            slope = abs(last[1] - first[1]) / (last[0] - first[0])
            require(slope <= .55,
                    'Saved auxiliary taper makes an abrupt lateral jump instead of a progressive lane change')
            maximum_lateral_slope = max(maximum_lateral_slope, slope)
        for fraction, low, high in ((.25, .05, .30), (.5, .35, .65), (.75, .70, .95)):
            sample = _axis_window(local, fraction * taper_length, fraction * taper_length + .001)[0][0]
            progress = (sample[1] - native_offset) / (5.5 - native_offset)
            require(low <= progress <= high,
                    'Saved auxiliary taper skips the independently required progressive lateral movement')
        require(all(abs(point[1] - 5.5) < POSITION_TOLERANCE
                    for segment in auxiliary for point in segment),
                'Saved auxiliary PATH lacks its full contiguous parallel lane at 5.5 metres')

        # The auxiliary lane supplements the two actual native through lanes.
        # Check both saved spines beside the complete parallel interval.
        # Native diagonal half-tile boundaries start the two through lanes at
        # different u positions, so the outermost taper collar cannot require
        # a lane outside its own measured external port.
        for lateral in (-native_offset, native_offset):
            intervals = []
            for route in routes:
                if route['transport'] != 1:
                    continue
                for first, last in zip(route['points'], route['points'][1:]):
                    first_v, last_v = ((point[1] - point[0] + 136.) / root for point in (first, last))
                    first_u, last_u = (sum(point[:2]) / root for point in (first, last))
                    if (abs(first[2] - height) < POSITION_TOLERANCE
                            and abs(last[2] - height) < POSITION_TOLERANCE
                            and abs(first_v - lateral) < POSITION_TOLERANCE
                            and abs(last_v - lateral) < POSITION_TOLERANCE
                            and direction * (last_u - first_u) > 1e-9):
                        intervals.append(tuple(sorted((coordinates(first)[0], coordinates(last)[0]))))
            require(_covers_interval(intervals, taper_length, end),
                    'Saved auxiliary lane replaced or displaced an original native through lane')
        reports.append({'ramp_id': name, 'from_arm': pair[0], 'to_arm': pair[1],
                        'saved_route_ids': witness, 'deck_height_m': height,
                        'native_lane_abs_v_m': native_offset, 'auxiliary_lane_abs_v_m': 5.5,
                        'flat_taper_axis_length_m': taper_length,
                        'contiguous_parallel_axis_length_m': sum(b[0] - a[0] for a, b in auxiliary),
                        'maximum_saved_lateral_taper_slope': maximum_lateral_slope,
                        'retained_native_through_lanes_beside_auxiliary': 2})
    return {'passed': True, 'verified_ramps': len(reports), 'ramps': reports,
            'scope': 'Decoded saved PATH transfer witnesses, flat progressive lane changes, contiguous parallel auxiliary lanes, and both unchanged native through spines beside each parallel section.'}


def check_saved_routes(routes, owners):
    expected = native_external_contract(); expected_by_key = {
        (port['transport'], port['direction'], port['point']): port for port in expected}
    endpoints = defaultdict(list); graph = defaultdict(set); observed = {}
    for route in routes:
        for direction, point, edge in (('in', route['points'][0], route['entry']),
                                       ('out', route['points'][-1], route['exit'])):
            tangent, grade = _direction(route['points'], direction == 'in')
            endpoints[(route['transport'], _key(point))].append({'route': route['id'], 'direction': direction,
                'edge': edge, 'cell': route['cell'], 'tangent': tangent, 'grade': grade})
    seam_pairs, external_routes = [], {'in': defaultdict(set), 'out': defaultdict(set)}
    for (transport, point), ends in endpoints.items():
        for end in ends:
            step = NEIGHBOURS[end['edge']]; neighbour = end['cell'][0] + step[0], end['cell'][1] + step[1]
            matches = [other for other in ends if other['direction'] != end['direction'] and
                       other['cell'] == neighbour and other['edge'] == (end['edge'] + 2) % 4]
            if matches:
                for other in matches:
                    require(sum(a * b for a, b in zip(end['tangent'], other['tangent'])) > .998 and
                            abs(end['grade'] - other['grade']) < .005,
                            'Saved assembly lane seam changes travel tangent or grade')
                    if end['direction'] == 'out':
                        graph[end['route']].add(other['route'])
                        seam_pairs.append((end['route'], other['route'], point))
            else:
                key = (transport, end['direction'], point)
                require(key in expected_by_key, 'Saved assembly has an unexpected or disconnected native boundary channel')
                contract = expected_by_key[key]
                require(sum(a * b for a, b in zip(end['tangent'], contract['tangent'])) > .998
                        and abs(end['grade']) < .005, 'Saved assembly native boundary tangent or grade changed')
                observed[key] = contract
                external_routes[end['direction']][key].add(end['route'])
    require(set(observed) == set(expected_by_key), 'Saved assembly is missing a measured native boundary lane or pedestrian channel')
    through_channels = 0
    for first, starts in external_routes['in'].items():
        height = first[2][2]
        lane_axis = first[2][0] - first[2][1] if height > 1. else first[2][0] + first[2][1]
        finishes = []
        for last in external_routes['out']:
            other_axis = last[2][0] - last[2][1] if height > 1. else last[2][0] + last[2][1]
            if (last[0] == first[0] and abs(last[2][2] - height) < POSITION_TOLERANCE and
                    abs(other_axis - lane_axis) < POSITION_TOLERANCE and observed[first]['arm'] != observed[last]['arm']):
                finishes.append(last)
        require(len(finishes) == 1, 'Native boundary through-lane contract is ambiguous')
        goals = external_routes['out'][finishes[0]]
        require(any(_search(start, goals, graph, routes) is not None for start in starts),
                'Saved assembly lost a measured native through lane or sidewalk channel')
        through_channels += 1
    # Independent height-routing proof: a cross-deck journey must traverse
    # the explicitly located ground junctions, rather than a hidden shortcut.
    for first, starts in external_routes['in'].items():
        if first[0] != 1 or first[2][2] < 1.:
            continue
        for last, finishes in external_routes['out'].items():
            if last[0] == 1 and last[2][2] > 1. and abs(first[2][2] - last[2][2]) > 1.:
                require(not any(_search(start, finishes, graph, routes, avoid_junctions=True) for start in starts),
                        'Saved assembly permits a deck transfer that bypasses the intentional ground junctions')
    required = {('HW_NE', 'HW_SW'), ('HW_SW', 'HW_NE'), ('AVE_NW', 'AVE_SE'), ('AVE_SE', 'AVE_NW')}
    transfers = {('HW_NE', 'AVE_NW'), ('AVE_NW', 'HW_SW'),
                 ('HW_SW', 'AVE_SE'), ('AVE_SE', 'HW_NE')}
    forbidden = {('HW_NE', 'AVE_SE'), ('AVE_SE', 'HW_SW'),
                 ('HW_SW', 'AVE_NW'), ('AVE_NW', 'HW_NE')}
    required |= transfers
    witnesses, reachable = {}, set()
    for first, starts in external_routes['in'].items():
        for last, finishes in external_routes['out'].items():
            if first[0] != last[0]:
                continue
            pair = observed[first]['arm'], observed[last]['arm']
            for start in starts:
                witness = _search(start, finishes, graph, routes)
                if witness is not None:
                    if first[0] == 1:
                        reachable.add(pair); witnesses.setdefault(pair, witness)
                    break
    require(required <= reachable, 'Saved assembly is missing required highway/Avenue transfer or through movements: ' +
            repr(sorted(required - reachable)))
    require(not forbidden & reachable, 'Saved assembly permits a forbidden Avenue-crossing transfer: ' +
            repr(sorted(forbidden & reachable)))
    maximum_grade = 0.0
    for route in routes:
        if route['transport'] != 1:
            continue
        for first, last in zip(route['points'], route['points'][1:]):
            horizontal = math.dist(first[:2], last[:2])
            require(horizontal > 1e-9, 'Saved assembly car PATH has a vertical or stationary segment')
            grade = abs(last[2] - first[2]) / horizontal
            require(grade <= .3 + 1e-5, 'Saved assembly exceeds the gentler 30 percent grade ceiling')
            maximum_grade = max(maximum_grade, grade)
    intercomponent = [pair for pair in seam_pairs if routes[pair[0]]['placement'] != routes[pair[1]]['placement']]
    auxiliary_lanes = check_saved_auxiliary_lanes(routes, witnesses)
    return {'passed': True, 'route_fragments': len(routes), 'matched_directed_lane_seams': len(seam_pairs),
            'inter_component_directed_lane_seams': len(intercomponent), 'external_native_channels': len(observed),
            'pedestrian_external_channels': sum(port['transport'] == 2 for port in observed.values()),
            'native_through_lane_and_sidewalk_journeys': through_channels,
            'required_arm_movements': len(required), 'highway_avenue_transfers': len(transfers), 'through_arm_movements': 4,
            'forbidden_avenue_crossing_movements': len(forbidden), 'no_avenue_crossing_transfers': True,
            'grade_ceiling_percent': 30.0, 'maximum_saved_car_grade_percent': 100.0 * maximum_grade,
            'reachable_arm_pairs': [list(pair) for pair in sorted(reachable)],
            'movement_witnesses': [{'from_arm': pair[0], 'to_arm': pair[1], 'saved_route_ids': witnesses[pair]}
                                   for pair in sorted(required)],
            'all_cross_deck_journeys_require_intentional_ground_junctions': True,
            'auxiliary_lanes': auxiliary_lanes,
            'external_ports': list(observed.values())}, intercomponent


def _projected_area_in_cell(points, cell):
    polygon = [(point[0], point[1]) for point in points]
    for axis, boundary, sign in ((0, cell[0] * 16. - 8., 1), (0, cell[0] * 16. + 8., -1),
                                  (1, -cell[1] * 16. - 8., 1), (1, -cell[1] * 16. + 8., -1)):
        if not polygon:
            return 0.
        clipped = []; previous = polygon[-1]; before = sign * (previous[axis] - boundary) >= 0.
        for point in polygon:
            inside = sign * (point[axis] - boundary) >= 0.
            if inside != before:
                fraction = (boundary - previous[axis]) / (point[axis] - previous[axis])
                clipped.append(tuple(previous[n] + fraction * (point[n] - previous[n]) for n in (0, 1)))
            if inside:
                clipped.append(point)
            previous, before = point, inside
        polygon = clipped
    return abs(sum(a[0] * b[1] - a[1] * b[0] for a, b in zip(polygon, polygon[1:] + polygon[:1]))) / 2.


def _model_faces(owners, piece_resources):
    faces = defaultdict(list); physical_cells = set(); all_points = []
    for cell, owner in owners.items():
        raw = piece_resources[owner['piece_id']][*S3D, owner['tile'] + 4]
        model = parse_s3d(raw); validate_s3d(model)
        for mesh in model['meshes']:
            require(len(mesh['frames']) == 1, 'Assembly model seam audit requires static S3D meshes')
            vi, ii, pi, mi = mesh['frames'][0]
            vertices = positions(model['vertices'][vi]); indices = model['indices'][ii]['values']
            for kind, first, count in model['primitives'][pi]:
                require(kind == 0 and count % 3 == 0, 'Assembly model contains a non-triangular primitive')
                for offset in range(first, first + count, 3):
                    points = [_pose((vertices[index][0] + 16 * owner['local_cell'][0],
                        -vertices[index][2] - 16 * owner['local_cell'][1], vertices[index][1]),
                        owner['angle'], owner['origin']) for index in indices[offset:offset + 3]]
                    all_points.extend(points)
                    a, b, c = points; area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
                    low = min(p[0] for p in points), min(p[1] for p in points)
                    high = max(p[0] for p in points), max(p[1] for p in points)
                    for column in range(math.floor((low[0] + 8. + 1e-6) / 16.), math.floor((high[0] + 8. - 1e-6) / 16.) + 1):
                        for row in range(math.floor((-high[1] + 8. + 1e-6) / 16.), math.floor((-low[1] + 8. - 1e-6) / 16.) + 1):
                            if _projected_area_in_cell(points, (column, row)) > 1e-7:
                                physical_cells.add((column, row))
                    if area <= 1e-9:
                        continue
                    face = {'points': points, 'bounds': (low, high), 'area': area}
                    for column in range(cell[0] - 1, cell[0] + 2):
                        for row in range(cell[1] - 1, cell[1] + 2):
                            faces[column, row].append(face)
    return faces, physical_cells, all_points


def _support(point, tangent, candidates):
    matches = []
    for face in candidates:
        low, high = face['bounds']
        if not (low[0] - 2e-5 <= point[0] <= high[0] + 2e-5 and low[1] - 2e-5 <= point[1] <= high[1] + 2e-5):
            continue
        a, b, c = face['points']; den = face['area']
        u = ((point[0] - a[0]) * (c[1] - a[1]) - (point[1] - a[1]) * (c[0] - a[0])) / den
        v = ((b[0] - a[0]) * (point[1] - a[1]) - (b[1] - a[1]) * (point[0] - a[0])) / den
        if min(u, v, 1. - u - v) < -2e-5:
            continue
        height = a[2] + u * (b[2] - a[2]) + v * (c[2] - a[2])
        if abs(height - point[2]) > MESH_TOLERANCE:
            continue
        gx = ((b[2] - a[2]) * (c[1] - a[1]) - (c[2] - a[2]) * (b[1] - a[1])) / den
        gy = ((b[0] - a[0]) * (c[2] - a[2]) - (c[0] - a[0]) * (b[2] - a[2])) / den
        matches.append((abs(height - point[2]), height, gx * tangent[0] + gy * tangent[1]))
    return min(matches) if matches else None


def check_model_seams(owners, piece_resources, routes, seams):
    faces, physical_cells, points = _model_faces(owners, piece_resources)
    require(physical_cells <= CONSTRUCTION_CELLS | NATIVE_OVERHANG_CELLS,
            'Saved model projection extends beyond construction and the six measured native overhang cells')
    checked, maximum_height_difference, maximum_grade_difference = 0, 0., 0.
    seen = set()
    for before, after, endpoint in seams:
        if routes[before]['transport'] != 1:
            continue
        tangent, grade = _direction(routes[before]['points'], False)
        key = (_key(endpoint), tuple(round(v, 5) for v in tangent))
        if key in seen:
            continue
        seen.add(key); normal = -tangent[1], tangent[0]
        for lateral in (-1.25, -.625, 0., .625, 1.25):
            supports = []
            for step in (-.002, .002):
                point = (endpoint[0] + step * tangent[0] + lateral * normal[0],
                         endpoint[1] + step * tangent[1] + lateral * normal[1], endpoint[2] + step * grade)
                cell = math.floor((point[0] + 8.) / 16.), math.floor((-point[1] + 8.) / 16.)
                support = _support(point, tangent, faces.get(cell, []))
                require(support is not None, 'Saved inter-component pavement seam has a gap within the measured car lane collar')
                supports.append(support)
            difference = abs(supports[0][1] - supports[1][1])
            grade_difference = abs(supports[0][2] - supports[1][2])
            require(difference <= MESH_TOLERANCE and grade_difference <= .015,
                    'Saved inter-component pavement seam changes surface height or longitudinal plane')
            maximum_height_difference = max(maximum_height_difference, difference)
            maximum_grade_difference = max(maximum_grade_difference, grade_difference); checked += 1
    require(checked > 0, 'No inter-component car pavement collars were inspected')
    return {'passed': True, 'car_lane_collar_samples': checked, 'collar_half_width_m': 1.25,
            'surface_height_tolerance_m': MESH_TOLERANCE, 'longitudinal_grade_difference_tolerance': .015,
            'maximum_sampled_height_difference_m': maximum_height_difference,
            'maximum_sampled_longitudinal_grade_difference': maximum_grade_difference,
            'physical_projection_cells': [list(cell) for cell in sorted(physical_cells)],
            'native_overhang_cells_beyond_construction': [list(cell) for cell in sorted(physical_cells - CONSTRUCTION_CELLS)],
            'actual_saved_model_bounds_east_north_height_m': [[min(p[a] for p in points), max(p[a] for p in points)] for a in range(3)],
            'scope': 'Car-lane pavement collars at inter-component joins; full barriers, supports, texture alpha, and game rendering remain separate.'}


def _point_segment_distance(point, first, last):
    dx, dy = last[0] - first[0], last[1] - first[1]
    length = dx * dx + dy * dy
    t = max(0., min(1., ((point[0] - first[0]) * dx + (point[1] - first[1]) * dy) / length))
    return math.hypot(point[0] - first[0] - t * dx, point[1] - first[1] - t * dy)


def _segment_square_distance(first, last, center, half=.4):
    low, high = (center[0] - half, center[1] - half), (center[0] + half, center[1] + half)
    if any(low[0] <= p[0] <= high[0] and low[1] <= p[1] <= high[1] for p in (first, last)):
        return 0.
    corners = [(low[0], low[1]), (high[0], low[1]), (high[0], high[1]), (low[0], high[1])]
    distances = []
    def cross(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    for a, b in zip(corners, corners[1:] + corners[:1]):
        if (max(min(first[0], last[0]), min(a[0], b[0])) <= min(max(first[0], last[0]), max(a[0], b[0])) and
            max(min(first[1], last[1]), min(a[1], b[1])) <= min(max(first[1], last[1]), max(a[1], b[1])) and
            cross(first, last, a) * cross(first, last, b) <= 0. and cross(a, b, first) * cross(a, b, last) <= 0.):
            return 0.
        distances.extend((_point_segment_distance(a, first, last), _point_segment_distance(b, first, last),
                          _point_segment_distance(first, a, b), _point_segment_distance(last, a, b)))
    return min(distances)


def check_saved_supports(owners, piece_resources, routes):
    """Check six actual centre posts against all saved car paths and deck planes."""
    faces, _physical_cells, _points = _model_faces(owners, piece_resources)
    posts = {}
    for cell, owner in owners.items():
        model = parse_s3d(piece_resources[owner['piece_id']][*S3D, owner['tile'] + 4])
        triangles, side_corners = [], defaultdict(list)
        for mesh in model['meshes']:
            vi, ii, pi, mi = mesh['frames'][0]
            vertices = positions(model['vertices'][vi]); indices = model['indices'][ii]['values']
            for kind, first, count in model['primitives'][pi]:
                for offset in range(first, first + count, 3):
                    local = [vertices[index] for index in indices[offset:offset + 3]]
                    if (abs(min(p[1] for p in local)) < 1e-6 and abs(max(p[1] for p in local) - 15.) < 1e-6
                            and all(abs(abs(p[0]) - .4) < 2e-6 and abs(abs(p[2]) - .4) < 2e-6 for p in local)):
                        sides = [(axis, sign) for axis in (0, 2) for sign in (-1, 1)
                                 if all(abs(p[axis] - sign * .4) < 2e-6 for p in local)]
                        require(len(sides) == 1, 'Saved support triangle does not belong to one vertical column side')
                        axis, sign = sides[0]; across = 2 if axis == 0 else 0
                        corners = frozenset((1 if p[across] > 0. else -1, 1 if p[1] > 7.5 else -1) for p in local)
                        require(len(corners) == 3, 'Saved support contains a degenerate vertical triangle')
                        side_corners[axis, sign].append(corners)
                        triangles.append(tuple(_pose((p[0] + 16 * owner['local_cell'][0],
                            -p[2] - 16 * owner['local_cell'][1], p[1]), owner['angle'], owner['origin']) for p in local))
        if triangles:
            require(cell in SUPPORT_CELLS and len(triangles) == 8, 'Unexpected support position or vertical-face inventory')
            require(len(side_corners) == 4, 'Saved support is missing one of its four vertical sides')
            for pair in side_corners.values():
                shared = pair[0] & pair[1] if len(pair) == 2 else frozenset()
                require(len(pair) == 2 and len(shared) == 2 and
                        len({p[0] for p in shared}) == 2 and len({p[1] for p in shared}) == 2,
                        'Saved support side triangles do not cover the entire rectangular face')
            posts[cell] = triangles
    require(set(posts) == SUPPORT_CELLS, 'Saved assembly is missing a measured centre support column')
    checked_segments, minimum_clearance, contacts = 0, float('inf'), []
    for cell, triangles in sorted(posts.items()):
        center = cell[0] * 16., -cell[1] * 16.
        for height in (7.5, 15.):
            for east in (center[0] - .4, center[0] + .4):
                for north in (center[1] - .4, center[1] + .4):
                    contact = _support((east, north, height), (1., 0.), faces.get(cell, []))
                    require(contact is not None and contact[0] <= POSITION_TOLERANCE,
                            'Saved centre support does not intersect the actual lower or upper road plane at every corner')
                    contacts.append({'cell': list(cell), 'point_m': [east, north, height],
                                     'measured_plane_height_m': contact[1], 'height_difference_m': contact[0]})
        for route in routes:
            if route['transport'] != 1:
                continue
            for first, last in zip(route['points'], route['points'][1:]):
                # Exclude contact with the road plane on which an upper
                # vehicle begins; the column ends at that plane.
                if min(first[2], last[2]) >= 15. - 1e-6 or max(first[2], last[2]) + 3.8 <= 0.:
                    continue
                distance = _segment_square_distance(first, last, center)
                clearance = distance - 1.25
                minimum_clearance = min(minimum_clearance, clearance); checked_segments += 1
                require(clearance > POSITION_TOLERANCE,
                        'Saved centre support intersects the declared 1.25-metre car corridor')
    return {'passed': True, 'actual_columns': len(posts), 'actual_vertical_triangles': sum(map(len, posts.values())),
            'column_width_m': .8, 'height_interval_m': [0., 15.],
            'actual_deck_contact_corner_samples': len(contacts), 'deck_contact_samples': contacts,
            'car_segments_checked_against_columns': checked_segments,
            'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
            'minimum_conservative_planar_clearance_m': minimum_clearance,
            'column_cells': [list(cell) for cell in sorted(posts)],
            'saved_model_instances': [{'cell': list(cell), 'piece_id': owners[cell]['piece_id'],
                                       'model_tgi': [f'{S3D[0]:08x}', f'{S3D[1]:08x}', f'{owners[cell]["tile"] + 4:08x}']}
                                      for cell in sorted(posts)],
            'scope': 'Saved vertical faces, indexed road-plane contacts, and conservative saved-PATH car corridors; structural load capacity and in-game collision behaviour are unverified.'}


def verify_assembly_resources(manifest, scene, piece_resources, *, inspect_models=True):
    pieces = {piece['id']: piece for piece in manifest['pieces']}
    from .ddrhw_connections import check_selected_helper_collisions
    helper_report = check_selected_helper_collisions(pieces, scene)
    owners, poses = check_owned_cells(pieces, scene)
    rectangle = [max(cell[axis] for cell in owners) - min(cell[axis] for cell in owners) + 1 for axis in (0, 1)]
    require(scene.get('construction_rectangle_tiles', rectangle) == rectangle,
            'Declared assembly rectangle differs from its actual owned construction cells')
    routes = decode_placed_routes(owners, piece_resources)
    graph, seams = check_saved_routes(routes, owners)
    model_report = check_model_seams(owners, piece_resources, routes, seams) if inspect_models else {'passed': False, 'status': 'not-run'}
    support_report = check_saved_supports(owners, piece_resources, routes) if inspect_models else {'passed': False, 'status': 'not-run'}
    from .barrier_mouth_verify import check_saved_barrier_mouths
    barrier_report = check_saved_barrier_mouths(owners, piece_resources) if inspect_models else {'passed': False, 'status': 'not-run'}
    from .wheeltrack_verify import check_saved_wheeltracks
    wheeltrack_report, wheeltrack_corridors = check_saved_wheeltracks(owners, piece_resources, routes, graph) if inspect_models else ({'passed': False, 'status': 'not-run'}, [])
    from .shoulder_uv_verify import check_saved_shoulder_uvs
    shoulder_report = check_saved_shoulder_uvs(owners, piece_resources, permitted_corridors=wheeltrack_corridors) if inspect_models else {'passed': False, 'status': 'not-run'}
    from .marking_verify import check_saved_markings
    marking_report = check_saved_markings(owners, piece_resources) if inspect_models else {'passed': False, 'status': 'not-run'}
    return {'schema_version': 1, 'subject_id': SUBJECT, 'saved_resource_checks_passed': bool(inspect_models),
            **({'native_dd_outside_approaches': helper_report} if helper_report else {}),
            'saved_path_and_construction_checks_passed': True, 'assembly_orientation_checked_ccw_degrees': 0,
            'construction': {'unique_owned_cells': len(owners), 'bounding_rectangle_tiles': rectangle,
                             'placements': len(poses), 'distinct_component_types': len({p['piece_id'] for p in poses}),
                             'physical_projection_is_separate': True},
            'paths': graph, 'model_seams': model_report, 'supports': support_report,
            'barrier_mouths': barrier_report, 'shoulder_uvs': shoulder_report, 'markings': marking_report, 'wheeltracks': wheeltrack_report, 'game_operation': 'unverified',
            'limits': ['Arm reachability does not establish every possible lane-to-lane transfer or game lane choice.',
                       'Pavement seam samples do not certify complete barrier profiles, complete collision envelopes, or texture-alpha coverage.',
                       'Ground junction priority and traffic conflicts, construction overrides, shadows, bulldozing, and save/reload require separate game observations.']}


def verify_assembly(output, scene, *, evidence_path=None, verify_package=True):
    output = Path(output).resolve()
    if evidence_path is not None:
        require(not Path(evidence_path).resolve().is_relative_to(output),
                'Assembly evidence must stay outside the verified build directory')
    if verify_package:
        from scp.verify import verify_build
        verify_build(output, write_report=False)
    manifest_raw = (output / 'manifest.json').read_bytes(); manifest = json.loads(manifest_raw)
    piece_resources, fingerprints = {}, {}
    file_records = {item['path']: item for item in manifest['files']}
    for piece in manifest['pieces']:
        relative = piece['asset_file']; raw = (output / relative).read_bytes()
        record = file_records[relative]
        require(len(raw) == record['bytes'] and hashlib.sha256(raw).hexdigest() == record['sha256'],
                'Assembly source DAT fingerprint differs from its verified manifest')
        piece_resources[piece['id']] = strict_dbpf(raw); fingerprints[relative] = record['sha256']
    report = verify_assembly_resources(manifest, scene, piece_resources)
    report['source'] = {'manifest_sha256': hashlib.sha256(manifest_raw).hexdigest(),
                        'asset_files': fingerprints, 'actual_saved_dat_resources': True,
                        'scene_sha256': hashlib.sha256(json.dumps(scene, sort_keys=True, separators=(',', ':')).encode()).hexdigest()}
    if evidence_path is not None:
        path = Path(evidence_path); path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, indent=2) + '\n', encoding='utf8')
    return report
