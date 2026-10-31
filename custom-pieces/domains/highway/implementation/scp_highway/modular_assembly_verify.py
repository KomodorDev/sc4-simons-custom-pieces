"""Independent seven-placement modular DD diamond audit on saved resources.

Only stateless decoders and geometric helpers are reused from the original
diamond verifier. Its 53-cell ownership, junction set, and verification globals
are never changed. The new literal layout owns 62 cells at seven placements.
"""
from __future__ import annotations

from collections import defaultdict, deque
import hashlib
import json
import math
from pathlib import Path

from scp.dbpf import require
from scp.models import parse_s3d, positions, validate_s3d
from scp.verify import S3D, strict_dbpf
from . import assembly_verify as shared
from .modular_verify import (STAMP, WORLD_CELLS, ORIGINS, reference, validate_specification,
                             custom_ports, _distance_to_segment)

TOLERANCE = 4e-5
SUBJECT = 'ddrhw-modular-ramp-kit'
REQUIRED = frozenset({('HW_NE', 'HW_SW'), ('HW_SW', 'HW_NE'), ('AVE_NW', 'AVE_SE'),
    ('AVE_SE', 'AVE_NW'), ('HW_NE', 'AVE_NW'), ('AVE_NW', 'HW_SW'),
    ('HW_SW', 'AVE_SE'), ('AVE_SE', 'HW_NE')})
FORBIDDEN = frozenset({('HW_NE', 'AVE_SE'), ('AVE_SE', 'HW_SW'),
                      ('HW_SW', 'AVE_NW'), ('AVE_NW', 'HW_NE')})
# These are render projections of the independently frozen DD stamp models.
# The compact grades owned these cells; the R40 plan deliberately leaves them
# unowned. They do not become construction cells or attachment sockets.
STAMP_INTERIOR_OVERHANG_CELLS = frozenset({(4, 6), (6, 4)})
PIERS = ((6., 35.76854249492381, 1.2888283156742073, .2543142572971316, 0.),
         (-35.76854249492381, -6., 1.2888283156742073, 0., -.2543142572971316),
         (10., -51.76854249492381, 1.504409662843726, -.2782677403159753, 0.),
         (51.76854249492381, -10., 1.504409662843726, 0., .2782677403159753))
COMPACT_CELLS = {
    'lower-exit-grade': ((1, -3), (1, -2)),
    'lower-entry-grade': ((-3, 1), (-2, 1)),
    'upper-exit-grade': ((0, 2), (-1, 3), (0, 3), (-1, 4)),
    'upper-entry-grade': ((4, -1), (3, -1), (2, 0), (3, 0)),
    'northwest-junction': ((-2, -2), (-1, -2), (0, -2), (-2, -1), (-1, -1), (-2, 0)),
    'southeast-junction': ((1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3)),
}


def construction_cells():
    source = {tuple(row['source_world_cell']) for row in reference()['cells']}
    source.update(cell for cells in WORLD_CELLS.values() for cell in cells)
    require(len(source) == 62, 'The independent modular partition must own exactly 62 cells')
    return frozenset((x+4, y+4) for x, y in source)


def check_owned_cells(pieces, scene):
    placements = scene.get('placements', scene.get('instances'))
    require(isinstance(placements, list) and len(placements) == 7,
            'The modular reference assembly requires seven separately placed components')
    owners, poses, used = {}, [], set()
    for index, placement in enumerate(placements):
        identifier = placement['piece_id']
        require(identifier in pieces and pieces[identifier].get('domain') == 'highway',
                'Modular assembly references a missing or foreign-domain piece')
        piece = pieces[identifier]
        key = validate_specification(piece)
        require(key not in used, 'The reference assembly repeats a modular component')
        used.add(key)
        angle = placement.get('rotation_degrees_ccw', placement.get('rotation_ccw_degrees', 0))
        origin = placement['origin_m']
        expected_origin = (16.*(ORIGINS[key][0]+4), -16.*(ORIGINS[key][1]+4))
        require(type(angle) is int and angle == 0 and len(origin) == 2 and
                all(type(v) in (int, float) and math.isfinite(v) for v in origin) and
                math.dist(origin, expected_origin) < TOLERANCE,
                'A modular reference component left its independently reviewed tile pose')
        for local, identifier_raw in zip(piece['cells'], piece['tile_ids']):
            cell = local[0]+ORIGINS[key][0]+4, local[1]+ORIGINS[key][1]+4
            require(cell not in owners, 'A modular construction cell has more than one independent owner')
            owners[cell] = {'placement': index, 'piece_id': identifier, 'tile': int(identifier_raw, 16),
                           'local_cell': tuple(local), 'geometry_key': key,
                           'angle': 0, 'origin': tuple(origin)}
        poses.append({'piece_id': identifier, 'geometry_key': key, 'origin': tuple(origin), 'angle': 0})
    require(used == {STAMP, *WORLD_CELLS} and set(owners) == construction_cells(),
            'The modular assembly differs from its literal seven-type, 62-cell partition')
    return owners, poses


def native_external_contract():
    cells, result = construction_cells(), []
    for x, y in sorted(cells):
        for route in shared._native_routes(x-4, y-4):
            for direction, point, side in (('in', route['points'][0], route['entry']),
                                            ('out', route['points'][-1], route['exit'])):
                dx, dy = shared.NEIGHBOURS[side]
                if (x+dx, y+dy) not in cells:
                    tangent, grade = shared._direction(route['points'], direction == 'in')
                    world = point[0]+16*x, point[1]-16*y, point[2]
                    result.append({'transport': route['transport'], 'direction': direction,
                        'point': shared._key(world), 'tangent': tangent, 'grade': grade,
                        'arm': shared._arm(world)})
    require(len(result) == 20, 'Independent modular native boundary does not have twenty channels')
    return result


def _search(start, goals, graph, routes, *, avoid_ground=False):
    queue, seen = deque([(start, [])]), set()
    while queue:
        key, witness = queue.popleft()
        if key in seen:
            continue
        seen.add(key)
        if avoid_ground and any(abs(p[2]) < TOLERANCE for p in routes[key]['points']):
            continue
        witness = witness+[key]
        if key in goals:
            return witness
        queue.extend((next_key, witness) for next_key in graph[key] if next_key not in seen)
    return None


def _rotate_routes(routes, turns):
    result = []
    for route in routes:
        x, y = route['cell']
        for _ in range(turns):
            x, y = y, -x
        result.append({**route, 'cell': (x, y),
                       'points': [shared._pose(p, 90*turns, (0., 0.)) for p in route['points']],
                       'entry': (route['entry']-turns) % 4, 'exit': (route['exit']-turns) % 4})
    return result


def check_saved_routes(routes, *, turns=0, external_ports=None):
    expected = []
    for port in native_external_contract() if external_ports is None else external_ports:
        expected.append({**port, 'point': shared._key(shared._pose(port['point'], 90*turns, (0., 0.))),
                         'tangent': shared._pose((*port['tangent'], 0.), 90*turns, (0., 0.))[:2]})
    contract = {(p['transport'], p['direction'], p['point']): p for p in expected}
    endpoints, graph, observed = defaultdict(list), defaultdict(set), {}
    for route in routes:
        for direction, point, side in (('in', route['points'][0], route['entry']),
                                        ('out', route['points'][-1], route['exit'])):
            tangent, grade = shared._direction(route['points'], direction == 'in')
            endpoints[route['transport'], shared._key(point)].append(
                {'route': route['id'], 'cell': route['cell'], 'direction': direction,
                 'side': side, 'tangent': tangent, 'grade': grade})
    boundaries, seams = {'in': defaultdict(set), 'out': defaultdict(set)}, []
    for (transport, point), ends in endpoints.items():
        for end in ends:
            dx, dy = shared.NEIGHBOURS[end['side']]
            neighbour = end['cell'][0]+dx, end['cell'][1]+dy
            matches = [e for e in ends if e['direction'] != end['direction'] and
                       e['cell'] == neighbour and e['side'] == (end['side']+2) % 4]
            if matches:
                for other in matches:
                    require(sum(a*b for a, b in zip(end['tangent'], other['tangent'])) > .998 and
                            abs(end['grade']-other['grade']) < .005,
                            'A modular saved-route join changes tangent or grade')
                    if end['direction'] == 'out':
                        graph[end['route']].add(other['route'])
                        seams.append((end['route'], other['route'], point))
            else:
                key = transport, end['direction'], point
                require(key in contract, 'A modular route terminates at a disconnected or unexpected boundary')
                port = contract[key]
                require(sum(a*b for a, b in zip(end['tangent'], port['tangent'])) > .998 and
                        abs(end['grade']) < .005, 'A modular native boundary changed its tangent or grade')
                observed[key] = port
                boundaries[end['direction']][key].add(end['route'])
    require(set(observed) == set(contract), 'A modular native lane or sidewalk boundary is missing')
    witnesses, reachable, through = {}, set(), 0
    inverse = lambda p: shared._pose(p, (360-90*turns) % 360, (0., 0.))
    for first, starts in boundaries['in'].items():
        p = inverse(first[2])
        axis = p[0]-p[1] if p[2] > 1. else p[0]+p[1]
        through_goals = []
        for last, goals in boundaries['out'].items():
            q = inverse(last[2])
            other_axis = q[0]-q[1] if q[2] > 1. else q[0]+q[1]
            if first[0] == last[0] and abs(p[2]-q[2]) < TOLERANCE and abs(axis-other_axis) < TOLERANCE:
                through_goals.append(goals)
            if first[0] != last[0]:
                continue
            pair = observed[first]['arm'], observed[last]['arm']
            witness = next((_search(start, goals, graph, routes) for start in starts
                            if _search(start, goals, graph, routes) is not None), None)
            if witness and first[0] == 1:
                reachable.add(pair)
                witnesses.setdefault(pair, witness)
            if first[0] == 1 and p[2] > 1. and q[2] > 1. and abs(p[2]-q[2]) > 1.:
                require(not any(_search(start, goals, graph, routes, avoid_ground=True) for start in starts),
                        'A modular journey transfers decks without reaching ground')
        require(len(through_goals) == 1 and any(_search(start, through_goals[0], graph, routes) for start in starts),
                'A modular highway, Avenue lane, or sidewalk through journey is missing')
        through += 1
    require(REQUIRED <= reachable, 'A modular assembly is missing required movements: '+repr(sorted(REQUIRED-reachable)))
    require(not FORBIDDEN & reachable, 'A modular assembly permits forbidden Avenue-crossing turns')
    maximum = 0.
    for route in routes:
        if route['transport'] != 1:
            continue
        for a, b in zip(route['points'], route['points'][1:]):
            length = math.dist(a[:2], b[:2])
            require(length > 1e-9, 'A modular car route contains a stationary planar segment')
            maximum = max(maximum, abs(b[2]-a[2])/length)
    require(maximum <= .30001, 'A modular car route exceeds the 30 percent experimental grade ceiling')
    intercomponent = [s for s in seams if routes[s[0]]['placement'] != routes[s[1]]['placement']]
    return {'passed': True, 'route_fragments': len(routes), 'proper_rotation_ccw_degrees': turns*90,
            'matched_directed_lane_seams': len(seams), 'external_native_channels': len(observed),
            'native_through_lane_and_sidewalk_journeys': through, 'required_arm_movements': 8,
            'forbidden_avenue_crossing_movements': 4, 'maximum_saved_car_grade_percent': maximum*100.,
            'reachable_arm_pairs': [list(pair) for pair in sorted(reachable)],
            'movement_witnesses': [{'from_arm': a, 'to_arm': b, 'saved_route_ids': witnesses[a, b]}
                                   for a, b in sorted(REQUIRED)],
            'game_operation_tested': False}, intercomponent


def _triangle_distance(point, triangle):
    a, b, c = triangle
    ab, ac = [b[i]-a[i] for i in range(3)], [c[i]-a[i] for i in range(3)]
    n = (ab[1]*ac[2]-ab[2]*ac[1], ab[2]*ac[0]-ab[0]*ac[2], ab[0]*ac[1]-ab[1]*ac[0])
    n2 = sum(v*v for v in n)
    if n2 > 1e-24:
        signed = sum((point[i]-a[i])*n[i] for i in range(3))/n2
        projected = [point[i]-signed*n[i]-a[i] for i in range(3)]
        aa, bb, cc = sum(v*v for v in ab), sum(v*w for v, w in zip(ab, ac)), sum(v*v for v in ac)
        d, e = sum(v*w for v, w in zip(projected, ab)), sum(v*w for v, w in zip(projected, ac))
        denominator = aa*cc-bb*bb
        if denominator > 1e-24:
            u, v = (d*cc-e*bb)/denominator, (e*aa-d*bb)/denominator
            if min(u, v, 1-u-v) >= -1e-8:
                return abs(signed)*math.sqrt(n2)
    return min(_distance_to_segment(point, x, y) for x, y in ((a, b), (b, c), (c, a)))


def _indexed_faces(owners, resources):
    """Decode all windings, including vertical profiles, without builder calls."""
    for cell, owner in owners.items():
        model = parse_s3d(resources[owner['piece_id']][*S3D, owner['tile']+4])
        validate_s3d(model)
        for mesh in model['meshes']:
            require(len(mesh['frames']) == 1, 'Modular physical joins require static saved meshes')
            vi, ii, pi, mi = mesh['frames'][0]
            vertices, indices = positions(model['vertices'][vi]), model['indices'][ii]['values']
            for kind, first, count in model['primitives'][pi]:
                require(kind == 0 and count % 3 == 0, 'Modular physical joins require indexed triangles')
                for at in range(first, first+count, 3):
                    points = [shared._pose((vertices[i][0]+16*owner['local_cell'][0],
                              -vertices[i][2]-16*owner['local_cell'][1], vertices[i][1]),
                              owner['angle'], owner['origin']) for i in indices[at:at+3]]
                    yield cell, points, model['materials'][mi]['textures']


def _frozen_stamp_provenance(owners, resources):
    expected = {tuple(row['cell']): row['model_sha256'] for row in reference()['cells']}
    records = []
    for cell, owner in owners.items():
        if owner.get('geometry_key') != STAMP:
            continue
        raw = resources[owner['piece_id']][*S3D, owner['tile']+4]
        digest = hashlib.sha256(raw).hexdigest()
        require(digest == expected.get(owner['local_cell']),
                'A stamp projection no longer has its independently frozen native model provenance')
        records.append({'cell': list(cell), 'model_tgi': [f'{v:08x}' for v in (*S3D, owner['tile']+4)],
                        'model_sha256': digest})
    return records


def _new_component_projection(owners, resources):
    records = []
    for identifier in sorted({o['piece_id'] for o in owners.values() if o.get('geometry_key') in WORLD_CELLS}):
        subset = {cell: o for cell, o in owners.items() if o['piece_id'] == identifier}
        _faces, physical, _points = shared._model_faces(subset, resources)
        require(physical <= set(subset), 'An authored modular attachment projects beyond its own construction cells')
        records.append({'piece_id': identifier, 'owned_cells': [list(c) for c in sorted(subset)],
                        'physical_projection_cells': [list(c) for c in sorted(physical)]})
    return records


def check_projection(owners, resources, physical, allowed):
    require(physical <= allowed | shared.NATIVE_OVERHANG_CELLS | STAMP_INTERIOR_OVERHANG_CELLS,
            'A modular saved model projects beyond its cells and measured native overhangs')
    provenance = _frozen_stamp_provenance(owners, resources)
    attachments = _new_component_projection(owners, resources)
    unowned = STAMP_INTERIOR_OVERHANG_CELLS-set(owners)
    require(not unowned or unowned == STAMP_INTERIOR_OVERHANG_CELLS,
            'Only the reviewed pair of empty interior stamp-overhang cells may be unowned')
    projection = []
    if unowned:
        stamp = {cell: o for cell, o in owners.items() if o.get('geometry_key') == STAMP}
        totals = {cell: {'triangles': 0, 'summed_projected_triangle_area_m2': 0., 'materials': set(),
                         'source_owner_cells': set()} for cell in unowned}
        for source, triangle, textures in _indexed_faces(stamp, resources):
            for cell, record in totals.items():
                area = shared._projected_area_in_cell(triangle, cell)
                if area > 1e-7:
                    record['triangles'] += 1
                    record['summed_projected_triangle_area_m2'] += area
                    record['materials'].update(textures)
                    record['source_owner_cells'].add(source)
        for cell, record in sorted(totals.items()):
            require(record['triangles'] > 0, 'A declared stamp overhang has no actual frozen face projection')
            projection.append({'unowned_cell': list(cell), 'triangles': record['triangles'],
                'summed_projected_triangle_area_m2': record['summed_projected_triangle_area_m2'],
                'materials': [f'{v:08x}' for v in sorted(record['materials'])],
                'source_owner_cells': [list(c) for c in sorted(record['source_owner_cells'])]})
    return {'passed': True, 'frozen_stamp_models': provenance, 'new_attachment_projections': attachments,
            'interior_native_overhangs_without_construction_ownership': projection,
            'scope': 'Projection is rendering geometry, not construction ownership. Areas sum indexed projected triangles, including overlapping decks and barrier bands; they are not a planar union area.'}


def check_model_seams(owners, resources, routes, seams, *, allowed_cells=None):
    faces, physical, points = shared._model_faces(owners, resources)
    allowed = construction_cells() if allowed_cells is None else frozenset(allowed_cells)
    projection = check_projection(owners, resources, physical, allowed)
    checked, maximum_height, maximum_grade = 0, 0., 0.
    seen = set()
    flat_sockets = [tuple(p['point_m'][a]+(64. if a == 0 else -64. if a == 1 else 0.)
                          for a in range(3))
                    for key in ('lower-exit-r40', 'lower-entry-r40', 'upper-exit-r40', 'upper-entry-r40')
                    for p in custom_ports(key) if p['point_m'][2] == 0.]
    for before, after, endpoint in seams:
        if routes[before]['transport'] != 1:
            continue
        tangent, grade = shared._direction(routes[before]['points'], False)
        identity = shared._key(endpoint), tuple(round(v, 5) for v in tangent)
        if identity in seen:
            continue
        seen.add(identity)
        normal = -tangent[1], tangent[0]
        # The custom six-metre roadway is a complete one-lane profile.
        # Native Avenue lane seams retain their measured 1.25 m car collar;
        # widening that per-lane test to 2.9 m would reach native sidewalks.
        custom = abs(grade) > 1e-5 or any(math.dist(endpoint, p) < TOLERANCE for p in flat_sockets)
        laterals = (-2.9, -2.25, -1.25, -.625, 0., .625, 1.25, 2.25, 2.9) if custom else (-1.25, -.625, 0., .625, 1.25)
        for lateral in laterals:
            pair = []
            for step in (-.002, .002):
                point = endpoint[0]+step*tangent[0]+lateral*normal[0], endpoint[1]+step*tangent[1]+lateral*normal[1], endpoint[2]+step*grade
                cell = math.floor((point[0]+8)/16), math.floor((-point[1]+8)/16)
                support = shared._support(point, tangent, faces.get(cell, []))
                require(support is not None, 'A modular full-width pavement collar has a saved-face gap')
                pair.append(support)
            height, gradient = abs(pair[0][1]-pair[1][1]), abs(pair[0][2]-pair[1][2])
            require(height <= .04 and gradient <= .015, 'A modular pavement join changes height or longitudinal plane')
            maximum_height, maximum_grade = max(maximum_height, height), max(maximum_grade, gradient)
            checked += 1
    require(checked, 'No modular inter-component pavement collars were checked')
    profile_points = []
    profile = ((0., 0.), (.21875, .328125), (.265625, 1.390625),
               (.5625, 1.390625), (.625, .328125), (.828125, 0.))
    for key in ('lower-exit-r40', 'lower-entry-r40', 'upper-exit-r40', 'upper-entry-r40'):
        for port in custom_ports(key):
            point = port['point_m']
            if point[2] < 1.:
                continue
            t, grade = port['tangent'], port['grade']
            normal = -t[1], t[0]
            for side in (-1, 1):
                for (a, h), (b, j) in zip(profile, profile[1:]):
                    lateral, height = side*(3.-(a+b)/2.), (h+j)/2.
                    for step in (-.002, .002):
                        profile_points.append((point[0]+64+step*t[0]+lateral*normal[0],
                            point[1]-64+step*t[1]+lateral*normal[1], point[2]+step*grade+height))
    near = []
    for _cell, triangle, textures in _indexed_faces(owners, resources):
        if textures not in ([0x5EB4BEE9], [0x5EB4BEEE]):
            continue
        low, high = [min(p[a] for p in triangle) for a in range(3)], [max(p[a] for p in triangle) for a in range(3)]
        if any(all(low[a]-.04 <= q[a] <= high[a]+.04 for a in range(3)) for q in profile_points):
            near.append((triangle, low, high))
    for point in profile_points:
        require(any(all(low[a]-.04 <= point[a] <= high[a]+.04 for a in range(3)) and
                    _triangle_distance(point, triangle) <= .04 for triangle, low, high in near),
                'A modular high join is missing a concrete barrier-profile band')
    return {'passed': True, 'pavement_collar_samples': checked, 'custom_ramp_pavement_half_width_m': 2.9,
            'native_car_lane_collar_half_width_m': 1.25,
            'high_join_profile_samples': len(profile_points), 'surface_tolerance_m': .04,
            'maximum_sampled_height_difference_m': maximum_height,
            'maximum_sampled_grade_difference': maximum_grade,
            'projection_provenance': projection,
            'physical_projection_cells': [list(c) for c in sorted(physical)],
            'actual_saved_model_bounds_east_north_height_m': [[min(p[a] for p in points), max(p[a] for p in points)] for a in range(3)],
            'scope': 'Saved full-width pavement and barrier-profile samples; continuous car corridors are checked per piece. This is not structural engineering or a complete vehicle-body proof.'}


def check_saved_supports(owners, resources, routes):
    retained = shared.check_saved_supports(owners, resources, routes)
    faces, _cells, _points = shared._model_faces(owners, resources)
    indexed = [points for _cell, points, textures in _indexed_faces(owners, resources)
               if textures == [0x5EB4BEEE]]
    contacts, checked, minimum = [], 0, float('inf')
    for x, y, top, gx, gy in PIERS:
        center = x+64, y-64
        corners = [(center[0]+dx, center[1]+dy, top+gx*dx+gy*dy)
                   for dx in (-.4, .4) for dy in (-.4, .4)]
        expected_vertices = [(p[0], p[1], 0.) for p in corners]+corners
        triangles = [tri for tri in indexed if all(any(math.dist(p, q) < 2e-5 for q in expected_vertices) for p in tri)]
        check_pier_shell(triangles, corners)
        for corner in corners:
            cell = math.floor((corner[0]+8)/16), math.floor((-corner[1]+8)/16)
            hit = shared._support((corner[0], corner[1], corner[2]+1.), (1., 0.), faces.get(cell, []))
            require(hit is not None and hit[0] < 3e-5, 'A modular ramp pier does not meet the actual one-metre-thick road underside')
            contacts.append(corner)
        for route in routes:
            if route['transport'] != 1:
                continue
            for a, b in zip(route['points'], route['points'][1:]):
                if min(a[2], b[2]) >= max(p[2] for p in corners)+TOLERANCE:
                    continue
                clearance = shared._segment_square_distance(a, b, center)-1.25
                require(clearance > TOLERANCE, 'A modular ramp pier intersects another saved car corridor')
                minimum, checked = min(minimum, clearance), checked+1
    return {'passed': True, 'retained_center_columns': retained,
            'additional_ramp_piers': 4, 'pier_width_m': .8, 'additional_contact_corner_samples': len(contacts),
            'car_segments_checked': checked, 'minimum_conservative_planar_clearance_m': minimum,
            'scope': 'Saved pier shell, road contact, and conservative traffic clearance; load capacity and game collision behavior remain unverified.'}


def check_pier_shell(triangles, corners):
    """Require every complete, outward-facing side of the literal small pier."""
    vertices = [(p[0], p[1], 0.) for p in corners]+list(corners)
    # Corners are ordered (-x,-y),(-x,+y),(+x,-y),(+x,+y).
    groups = (({0, 1, 2, 3}, (0., 0., -1.)), ({4, 5, 6, 7}, None),
              ({0, 1, 4, 5}, (-1., 0., 0.)), ({2, 3, 6, 7}, (1., 0., 0.)),
              ({0, 2, 4, 6}, (0., -1., 0.)), ({1, 3, 5, 7}, (0., 1., 0.)))
    buckets = defaultdict(list)
    require(len(triangles) == 12, 'A modular ramp pier is missing one of its twelve saved shell triangles')
    for triangle in triangles:
        ids = [next((i for i, v in enumerate(vertices) if math.dist(p, v) < 2e-5), None) for p in triangle]
        require(None not in ids and len(set(ids)) == 3, 'A modular pier shell has a displaced or degenerate corner')
        matches = [i for i, (indices, _normal) in enumerate(groups) if set(ids) <= indices]
        require(len(matches) == 1, 'A modular pier triangle cuts across the shell interior')
        index = matches[0]
        normal = groups[index][1]
        if normal is None:
            normal = (0., 0., 1.)
        a, b, c = triangle
        u, v = [b[i]-a[i] for i in range(3)], [c[i]-a[i] for i in range(3)]
        cross = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
        require(sum(x*y for x, y in zip(cross, normal)) > 1e-8,
                'A modular pier shell triangle faces inward')
        buckets[index].append(set(ids))
    for index, (indices, _normal) in enumerate(groups):
        pair = buckets[index]
        require(len(pair) == 2 and pair[0] != pair[1] and pair[0] | pair[1] == indices and
                len(pair[0] & pair[1]) == 2,
                'A modular pier has a missing or duplicated shell side')
    return {'passed': True, 'complete_shell_sides': 6, 'outward_triangles': 12}


def verify_assembly_resources(manifest, scene, piece_resources, *, inspect_models=True):
    pieces = {piece['id']: piece for piece in manifest['pieces']}
    owners, poses = check_owned_cells(pieces, scene)
    routes = shared.decode_placed_routes(owners, piece_resources)
    paths, seams = check_saved_routes(routes)
    rotations = [paths]+[check_saved_routes(_rotate_routes(routes, q), turns=q)[0] for q in (1, 2, 3)]
    models = check_model_seams(owners, piece_resources, routes, seams) if inspect_models else {'passed': False, 'status': 'not-run'}
    supports = check_saved_supports(owners, piece_resources, routes) if inspect_models else {'passed': False, 'status': 'not-run'}
    return {'schema_version': 1, 'subject_id': scene.get('id', SUBJECT),
            'saved_resource_checks_passed': bool(inspect_models), 'saved_path_and_construction_checks_passed': True,
            'construction': {'unique_owned_cells': len(owners), 'placements': 7, 'distinct_component_types': 7,
                             'bounding_rectangle_tiles': [10, 10], 'physical_projection_is_separate': True},
            'paths': paths, 'proper_rotation_paths': rotations, 'model_seams': models, 'supports': supports,
            'game_operation': 'unverified',
            'limits': ['This checks the literal seven-placement R40 reference layout, not all possible custom combinations.',
                       'Saved geometry and traffic checks do not establish native MIS compatibility or game placement, traffic, shadows, demolition, or save/reload.']}


def check_compact_owned_cells(pieces, scene):
    """The same stamp with six retained compact counterparts, at seven poses."""
    placements = scene.get('placements', scene.get('instances'))
    require(isinstance(placements, list) and len(placements) == 7,
            'The compact alternative requires the stamp and six separately placed counterparts')
    owners, used = {}, set()
    for index, placement in enumerate(placements):
        identifier = placement['piece_id']
        require(identifier in pieces and pieces[identifier].get('domain') == 'highway',
                'The compact alternative contains an unbuilt or foreign component')
        piece = pieces[identifier]
        key = piece.get('geometry_key')
        require(key not in used, 'The compact alternative repeats a component')
        used.add(key)
        if key == STAMP:
            validate_specification(piece)
            origin = (-4, -4)
        else:
            require(key in COMPACT_CELLS and piece['recipe'] == 'highway_ddrhw_compact_'+key.replace('-', '_'),
                    'The compact alternative contains an unexpected counterpart')
            cells = COMPACT_CELLS[key]
            origin = min(c[0] for c in cells), min(c[1] for c in cells)
            expected = sorted(([x-origin[0], y-origin[1]] for x, y in cells), key=lambda c: (c[1], c[0]))
            require(piece['cells'] == expected and piece['footprint'] == [max(c[a] for c in expected)+1 for a in (0, 1)],
                    'A retained compact counterpart changed its literal cell ownership')
        angle = placement.get('rotation_degrees_ccw', placement.get('rotation_ccw_degrees', 0))
        pose = (16.*(origin[0]+4), -16.*(origin[1]+4))
        require(type(angle) is int and angle == 0 and tuple(placement['origin_m']) == pose,
                'The compact alternative changed its literal registered pose')
        for cell, identifier_raw in zip(piece['cells'], piece['tile_ids']):
            world = cell[0]+origin[0]+4, cell[1]+origin[1]+4
            require(world not in owners, 'The compact alternative has overlapping construction ownership')
            owners[world] = {'placement': index, 'piece_id': identifier, 'tile': int(identifier_raw, 16),
                             'local_cell': tuple(cell), 'geometry_key': key, 'angle': 0, 'origin': pose}
    expected_source = {tuple(row['source_world_cell']) for row in reference()['cells']}
    expected_source.update(c for cells in COMPACT_CELLS.values() for c in cells)
    expected_cells = {(x+4, y+4) for x, y in expected_source}
    require(used == {STAMP, *COMPACT_CELLS} and len(owners) == 53 and set(owners) == expected_cells,
            'The compact alternative differs from the independent seven-type, 53-cell partition')
    require(expected_cells == shared.CONSTRUCTION_CELLS,
            'The compact alternative no longer covers the preceding measured physical layout')
    return owners


def verify_compact_alternative_resources(manifest, scene, piece_resources, *, inspect_models=True):
    pieces = {piece['id']: piece for piece in manifest['pieces']}
    owners = check_compact_owned_cells(pieces, scene)
    routes = shared.decode_placed_routes(owners, piece_resources)
    expected = shared.native_external_contract()
    paths, seams = check_saved_routes(routes, external_ports=expected)
    rotations = [paths]+[check_saved_routes(_rotate_routes(routes, q), turns=q, external_ports=expected)[0]
                         for q in (1, 2, 3)]
    models = check_model_seams(owners, piece_resources, routes, seams,
                              allowed_cells=set(owners)) if inspect_models else {'passed': False, 'status': 'not-run'}
    supports = shared.check_saved_supports(owners, piece_resources, routes) if inspect_models else {'passed': False, 'status': 'not-run'}
    return {'schema_version': 1, 'subject_id': scene.get('id', SUBJECT), 'alternative': 'compact',
            'saved_resource_checks_passed': bool(inspect_models), 'saved_path_and_construction_checks_passed': True,
            'construction': {'unique_owned_cells': 53, 'placements': 7, 'distinct_component_types': 7,
                             'bounding_rectangle_tiles': [10, 10]},
            'paths': paths, 'proper_rotation_paths': rotations, 'model_seams': models, 'supports': supports,
            'same_stamp_combined_with_retained_compact_counterparts': True,
            'game_operation': 'unverified',
            'limits': ['This is the literal compact alternative, not a promise about arbitrary module combinations.',
                       'Saved geometry and traffic checks do not establish native MIS compatibility or game behavior.']}


def verify_assembly(output, scene, *, evidence_path=None, verify_package=True, alternative=None):
    output = Path(output).resolve()
    if evidence_path is not None:
        require(not Path(evidence_path).resolve().is_relative_to(output), 'Assembly evidence must remain outside the saved build')
    if verify_package:
        from scp.verify import verify_build
        verify_build(output, write_report=False)
    raw = (output/'manifest.json').read_bytes()
    manifest = json.loads(raw)
    files, resources, fingerprints = {r['path']: r for r in manifest['files']}, {}, {}
    for piece in manifest['pieces']:
        path = piece['asset_file']
        data = (output/path).read_bytes()
        require(len(data) == files[path]['bytes'] and hashlib.sha256(data).hexdigest() == files[path]['sha256'],
                'A modular source DAT differs from its saved manifest')
        resources[piece['id']], fingerprints[path] = strict_dbpf(data), files[path]['sha256']
    require(alternative in (None, 'compact'), 'Unknown independently reviewed modular alternative')
    inspect = verify_compact_alternative_resources if alternative == 'compact' else verify_assembly_resources
    report = inspect(manifest, scene, resources)
    report['source'] = {'manifest_sha256': hashlib.sha256(raw).hexdigest(), 'asset_files': fingerprints,
                        'actual_saved_dat_resources': True,
                        'scene_sha256': hashlib.sha256(json.dumps(scene, sort_keys=True, separators=(',', ':')).encode()).hexdigest()}
    if evidence_path is not None:
        target = Path(evidence_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(report, indent=2)+'\n')
    return report


def verify_compact_alternative(output, scene, *, evidence_path=None, verify_package=True):
    return verify_assembly(output, scene, evidence_path=evidence_path,
                           verify_package=verify_package, alternative='compact')
