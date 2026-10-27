"""Independent, portable audits for HSR/GHSR switches, shifts and adapters.

The expectations here describe external ports and permitted train movements;
they do not ask the path or model writer to generate its own expected answer.
Native transition geometry is also pinned by canonical visible-triangle hashes.
All coordinates below are SC4PATH metres, with a cell centre at (16*x,-16*y).
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
import hashlib
import json
import math
import struct

from scp.dbpf import exemplar, require
from scp.models import parse_s3d, positions, valid_frame, validate_s3d

S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
EXEMPLAR = (0x6534284A, 0xA8434037)
EPS = 2e-6

RECIPES = {
    'rail_hsr_diagonal_s_left', 'rail_hsr_diagonal_s_right',
    'rail_ghsr_diagonal_s_left', 'rail_ghsr_diagonal_s_right',
    'rail_hsr_adjacent_crossover_right', 'rail_hsr_adjacent_crossover_left',
    'rail_ghsr_adjacent_crossover_right', 'rail_ghsr_adjacent_crossover_left',
    'rail_hsr_ghsr_transition',
}

# Rows 0..7 of native PATH 5DCF1700..5DCF1770, sampled at the seven
# literal Y coordinates below. These also pin all intermediate grade changes.
RAMP_Y = (-8., -5.345, -2.679, -.012, 2.655, 5.321, 8.)
RAMP_HEIGHTS = (
    (15.354, 15.5, 15.5, 15.5, 15.5, 15.5, 15.5),
    (13.663, 14.008, 14.317, 14.613, 14.909, 15.132, 15.354),
    (11.121, 11.618, 12.093, 12.533, 12.915, 13.308, 13.663),
    (7.678, 8.306, 8.892, 9.499, 10.058, 10.61, 11.121),
    (4.569, 5.03, 5.501, 6.017, 6.523, 7.119, 7.678),
    (2.308, 2.631, 2.971, 3.342, 3.715, 4.129, 4.569),
    (1., 1.044, 1.247, 1.492, 1.742, 2.012, 2.308),
    (1., 1., 1., 1., 1., 1., 1.),
)
RAMP_GEOMETRY = (
    '1d5c11bbc79c79208ae246f9c2e1e22957f249a3fb0047703a4ba05f15ae2017',
    'ae52657c97dcc1d4a85d0652bbd1a6a6fd0d4a662f62228a97062de7c080f56e',
    'b65cbdecd81d53c5bf1b591d79efd7bb8cc9deb8c52b5765e471a88054f8ed20',
    '95d6aaa5b80ac56b08dad479cd9ae97af41411ef573b877f1cd1d561905cf7a7',
    'ac12593a0cb71efd837ae6257eacb91a9043889b7af8d0e0c72eaf9112f879a7',
    '9a50b86db9843ddd4dbd80b866ce07b323d2d25d5bd759facb8f85a61b89d51f',
    '080dd8ff2a079e02bec38a9f90135f630fd14e09dbf4e67a6f1243997470ff3e',
    '1f77c527553f8182fc10fe0a596128eac89013f7728a3921250f2cca3c1bdce9',
)
MATERIAL_HASHES = {
    'procedural': 'dfa087a7554486e8dc3a86e0135ed181a76e59cffcf0ac05ca312dbea72ad591',
    'native_deck': 'd0be2a15514fd471dc0ee7bc3e2bf98091b2ff2d5cb5031dc2098eba636d4824',
    'native_pillar': 'e780abe2b0d8d225cbf79e77df941f053de9f27272f5a26d7ef46f648a22dd81',
}


def _recipe(spec):
    recipe = spec['recipe']
    require(recipe in RECIPES, 'Unknown rail feature recipe requires an independent verifier')
    return recipe


def _number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def _key(point):
    return tuple(round(value, 6) for value in point)


def _level(recipe):
    return 1. if recipe.startswith('rail_ghsr_') else 15.5


def _ports(recipe):
    """Literal external train ports and the permitted directed port pairs."""
    level = _level(recipe)
    if recipe == 'rail_hsr_ghsr_transition':
        ports = {'Nin': (-2., 8., 15.5), 'Nout': (2., 8., 15.5),
                 'Sin': (2., -120., 1.), 'Sout': (-2., -120., 1.)}
        return ports, {('Sin', 'Nout'), ('Nin', 'Sout')}
    if '_diagonal_s_' in recipe:
        left = recipe.endswith('_left')
        ports = ({'Sin': (18.9, -40., level), 'Sout': (13.1, -40., level),
                  'Ein': (40., 2.9, level), 'Eout': (40., -2.8, level)} if left else
                 {'Sin': (2.9, -40., level), 'Sout': (-2.9, -40., level),
                  'Ein': (40., -13.1, level), 'Eout': (40., -18.8, level)})
        return ports, {('Sin', 'Eout'), ('Ein', 'Sout')}
    ports = {'Nin': (-2., 8., level), 'Nout': (2., 8., level),
             'Sin': (2., -40., level), 'Sout': (-2., -40., level)}
    if '_adjacent_' in recipe:
        ports.update({'BNin': (14., 8., level), 'BNout': (18., 8., level),
                      'BSin': (18., -40., level), 'BSout': (14., -40., level)})
        allowed = {('Sin', 'Nout'), ('Nin', 'Sout'), ('BSin', 'BNout'), ('BNin', 'BSout')}
        if recipe.endswith('_right'):
            allowed.update({('Sin', 'BNout'), ('BNin', 'Sout')})
        if recipe.endswith('_left'):
            allowed.update({('BSin', 'Nout'), ('Nin', 'BSout')})
        return ports, allowed
    raise ValueError(f'Unknown rail feature port contract: {recipe}')


def _adapter(recipe, cell):
    """Return native source row and the PATH counterclockwise quarter-turns."""
    if recipe == 'rail_hsr_ghsr_transition':
        return cell[1], 0
    return None


def _turn(point, quarters):
    x, y, height = point
    for _ in range(quarters % 4):
        x, y = -y, x
    return x, y, height


def _native_ramp_routes(row, turns):
    forward = [(2., y, height) for y, height in zip(RAMP_Y, RAMP_HEIGHTS[row])]
    reverse = [(-2., y, height) for y, height in reversed(list(zip(RAMP_Y, RAMP_HEIGHTS[row])))]
    return [tuple(_key(_turn(point, turns)) for point in route) for route in (forward, reverse)]


def _cells(spec):
    width, depth = spec['footprint']
    cells = [tuple(cell) for cell in spec.get('cells', [(x, y) for y in range(depth) for x in range(width)])]
    require(len(cells) == len(spec['tile_ids']) and len(cells) == len(set(cells)),
            'Rail piece repeats a cell or has the wrong number of allocated tile IDs')
    require(all(0 <= x < width and 0 <= y < depth for x, y in cells), 'Rail cell outside its declared footprint')
    recipe = _recipe(spec)
    if recipe in CONSTRUCTION:
        _, construction, _, _ = CONSTRUCTION[recipe]
        expected = [(x-1, y-1) for y, row in enumerate(construction)
                    for x, symbol in enumerate(row) if symbol == '+']
        require((width, depth) == (len(construction[0])-3, len(construction)-2) and cells == expected,
                'Rail footprint/cells differ from the independently audited construction layout')
    tiles = [_number(raw) for raw in spec['tile_ids']]
    base = tiles[0] - 0x100*cells[0][0] - 0x10*cells[0][1]
    require(tiles == [base+0x100*x+0x10*y for x, y in cells],
            'Rail tile allocation does not follow its audited AutoTileBase grid')
    return cells


def check_paths(resources, spec, donors=None):
    if spec['recipe'] == 'rail_hsr_road_stack':
        from .road_stack_verify import check_paths as verify_stack
        return verify_stack(resources, spec, donors)
    from scp.verify import edge, parse_paths
    recipe = _recipe(spec)
    cells = _cells(spec)
    ports, allowed = _ports(recipe)
    external = {_key(point): label for label, point in ports.items()}
    require(len(external) == len(ports), 'Rail verifier has ambiguous external ports')
    graph, incoming, outgoing = defaultdict(set), defaultdict(list), defaultdict(list)
    checked, slope_samples, highest_grade = 0, 0, 0.
    for cell, raw_tile in zip(cells, spec['tile_ids']):
        parsed = parse_paths(resources[*PATH, _number(raw_tile)])
        routes = parsed['routes']
        require(parsed['version'] == '1.2' and routes, 'Rail routes must use SC4PATH 1.2 with explicit junction flags')
        signatures = set()
        starts = defaultdict(list)
        for route in routes:
            require(route['transport'] == 7 and route['lane'] >= 0 and route['compatibility'] in (0, 1),
                    'Rail path has the wrong transport, path class, or junction flag')
            points = route['points']
            require(edge(points[0]) == route['entry'] and edge(points[-1]) == route['exit'],
                    'Rail path edge directions disagree with its actual endpoints')
            for turns in range(1, 4):
                require(edge(_turn(points[0], turns)) == (route['entry']-turns) % 4 and
                        edge(_turn(points[-1], turns)) == (route['exit']-turns) % 4,
                        'Rail path has inconsistent edge directions after a proper rotation')
            require(route['entry'] != route['exit'], 'Rail path contains an unwanted U-turn')
            require(all(abs(point[0]) <= 8. + EPS and abs(point[1]) <= 8. + EPS for point in points),
                    'Rail train route leaves its assigned tile')
            signature = tuple(map(_key, points))
            require(signature not in signatures, 'Rail piece repeats an identical train route')
            signatures.add(signature)
            starts[_key(points[0])].append(route)
            for a, b in zip(points, points[1:]):
                run = math.hypot(b[0] - a[0], b[1] - a[1])
                require(run > EPS, 'Rail route has a zero-length segment or a vertical height jump')
                grade = abs(b[2]-a[2]) / run
                require(grade <= .25 + EPS, 'Rail route exceeds the audited native transition grade')
                highest_grade = max(highest_grade, grade)
                slope_samples += int(grade > EPS)
            adapter = _adapter(recipe, cell)
            if not adapter:
                require(all(abs(point[2] - _level(recipe)) < EPS for point in points),
                        'Level rail route has an illegal height change or a cross-level shortcut')
            world = [(_key((x + 16.*cell[0], y - 16.*cell[1], height))) for x, y, height in points]
            start, end = world[0], world[-1]
            graph[start].add(end)
            outgoing[start].append(cell)
            incoming[end].append(cell)
            checked += 1
        if _adapter(recipe, cell):
            row, turns = _adapter(recipe, cell)
            require(signatures == set(_native_ramp_routes(row, turns)),
                    'HSR/GHSR transition differs from the exact audited native slope paths')
        for duplicated in starts.values():
            if len(duplicated) > 1:
                require(any(route['compatibility'] == 1 for route in duplicated),
                        'Rail branch choice lacks its explicit junction flag')
    endpoints = set(incoming) | set(outgoing)
    require(set(external) <= endpoints, 'Rail piece is missing a native external connection port')
    for point in endpoints - set(external):
        require(incoming[point] and outgoing[point] and
                any(a != b for a in incoming[point] for b in outgoing[point]),
                'Rail path has a disconnected cell seam or a height jump between adjacent tiles')
    for point, label in external.items():
        require(bool(outgoing[point]) == label.endswith('in') and bool(incoming[point]) == label.endswith('out'),
                'Rail external port has the wrong direction or permits reverse running')
    for turns in range(4):
        rotated_graph = {_key(_turn(start, turns)): {_key(_turn(end, turns)) for end in ends}
                         for start, ends in graph.items()}
        rotated_ports = {_key(_turn(point, turns)): label for label, point in ports.items()}
        actual = set()
        for label, point in ports.items():
            if not label.endswith('in'):
                continue
            external_point = _key(_turn(point, turns))
            pending, visited = [external_point], set()
            while pending:
                node = pending.pop()
                if node in visited:
                    continue
                visited.add(node)
                if node != external_point and node in rotated_ports:
                    actual.add((label, rotated_ports[node]))
                pending.extend(rotated_graph.get(node, ()))
        require(actual == allowed, 'Rail port graph contains a missing movement, unwanted U-turn, or incorrect direction')
    require(slope_samples > 0 if 'transition' in recipe else slope_samples == 0,
            'Rail height transition is missing or an unintended slope has been added')
    return {'tile_count': len(cells), 'routes_checked': checked, 'connected_external_ports': len(ports),
            'permitted_movements_checked': len(allowed), 'unwanted_u_turns': False,
            'cell_seams_match_exactly': True, 'native_transition_paths_preserved': bool(slope_samples),
            'maximum_path_grade': highest_grade, 'rotations_checked': 4}


def _triangles(model):
    for mesh in model['meshes']:
        require(all(valid_frame(model, frame) for frame in mesh['frames']), 'Rail model has a dangling mesh reference')
        vi, ii, pi, _ = mesh['frames'][0]
        vb = model['vertices'][vi]
        require(vb['stride'] == 20, 'Rail geometry requires the audited native XYZ/UV format')
        vertices = [struct.unpack_from('<5f', vb['data'], offset)
                    for offset in range(0, len(vb['data']), vb['stride'])]
        indices = model['indices'][ii]['values']
        for kind, start, count in model['primitives'][pi]:
            require(kind == 0 and count % 3 == 0, 'Rail model must contain triangle lists')
            for offset in range(start, start + count, 3):
                yield tuple(vertices[index] for index in indices[offset:offset + 3])


def _native_fingerprint(model, turns=0):
    triangles = []
    for triangle in _triangles(model):
        result = []
        for x, height, z, u, v in triangle:
            # Undo the PATH turn in S3D coordinates, where Z=-PATH_Y.
            for _ in range(turns % 4):
                x, z = -z, x
            result.append(tuple(round(value, 5) if abs(value) >= .000005 else 0.
                                for value in (x, height, z, u, v)))
        triangles.append(sorted(result))
    return hashlib.sha256(json.dumps(sorted(triangles), separators=(',', ':')).encode()).hexdigest()


def _weights(x, z, triangle):
    a, b, c = triangle
    determinant = (b[2]-c[2])*(a[0]-c[0]) + (c[0]-b[0])*(a[2]-c[2])
    if abs(determinant) < 1e-8:
        return None
    u = ((b[2]-c[2])*(x-c[0]) + (c[0]-b[0])*(z-c[2])) / determinant
    v = ((c[2]-a[2])*(x-c[0]) + (a[0]-c[0])*(z-c[2])) / determinant
    weights = u, v, 1-u-v
    return weights if min(weights) >= -2e-5 else None


def _rail_u(x):
    return 1.0040634870529175 + (x + 5.9922380447387695) * (
        .21594023704528809 - 1.0040634870529175) / (5.996547698974609 + 5.9922380447387695)


def _distance(point, a, b):
    dx, dy = b[0]-a[0], b[1]-a[1]
    length2 = dx*dx+dy*dy
    if length2 < EPS*EPS:
        return math.inf
    t = max(0., min(1., ((point[0]-a[0])*dx+(point[1]-a[1])*dy)/length2))
    return math.hypot(point[0]-a[0]-t*dx, point[1]-a[1]-t*dy)


def _cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def _intersects(a, b, c, d):
    values = (_cross(a, b, c), _cross(a, b, d), _cross(c, d, a), _cross(c, d, b))
    if values[0]*values[1] < -1e-10 and values[2]*values[3] < -1e-10:
        return True
    return any(abs(value) < 1e-6 and _distance(point, first, last) < 1e-5
               for value, point, first, last in ((values[0], c, a, b), (values[1], d, a, b),
                                                 (values[2], a, c, d), (values[3], b, c, d)))


def _wall_projection(triangle, floor):
    """Project only the triangle portion more than 20 cm above the bed."""
    polygon = []
    previous = triangle[-1]
    for current in triangle:
        prev_in, curr_in = previous[1] >= floor, current[1] >= floor
        if prev_in != curr_in:
            fraction = (floor-previous[1])/(current[1]-previous[1])
            polygon.append(tuple(previous[i]+fraction*(current[i]-previous[i]) for i in range(3)))
        if curr_in:
            polygon.append(current[:3])
        previous = current
    return [(point[0], point[2]) for point in polygon] if len(polygon) >= 3 else []


def _check_wall_clearance(polygons, routes):
    buckets = defaultdict(set)
    for index, polygon in enumerate(polygons):
        for x in range(math.floor(min(p[0] for p in polygon)/4.), math.floor(max(p[0] for p in polygon)/4.)+1):
            for y in range(math.floor(min(p[1] for p in polygon)/4.), math.floor(max(p[1] for p in polygon)/4.)+1):
                buckets[x, y].add(index)
    checked = 0
    for route in routes:
        for first, last in zip(route, route[1:]):
            a, b = (first[0], -first[1]), (last[0], -last[1])
            candidates = set()
            for x in range(math.floor(min(a[0], b[0])/4.), math.floor(max(a[0], b[0])/4.)+1):
                for y in range(math.floor(min(a[1], b[1])/4.), math.floor(max(a[1], b[1])/4.)+1):
                    candidates.update(buckets[x, y])
            for index in candidates:
                polygon = polygons[index]
                require(not any(_intersects(a, b, c, d) for c, d in zip(polygon, polygon[1:]+polygon[:1])),
                        'An above-bed wall blocks the actual rail train route')
            checked += 1
    return checked


def check_models(resources, spec, donors=None):
    """Memoize only complete immutable inputs, returning a fresh report.

    A full portable build is intentionally reverified after many independent
    mutations in the test suite. Reusing an audit for identical input bytes
    avoids repeating the geometric intersection work for unaffected pieces.
    No result survives this process or a change to any model/path/exemplar.
    """
    if spec['recipe'] == 'rail_hsr_road_stack':
        from .road_stack_verify import check_models as verify_stack
        return verify_stack(resources, spec, donors)
    _recipe(spec)
    _cells(spec)
    keys = {(*S3D, _number(spec['preview_id']))}
    for raw_tile in spec['tile_ids']:
        tile = _number(raw_tile)
        keys.update({(*S3D, tile+zoom) for zoom in range(5)})
        keys.update({(*PATH, tile), (*EXEMPLAR, tile)})
    inputs = tuple((key, resources[key]) for key in sorted(keys))
    spec_json = json.dumps(spec, sort_keys=True, separators=(',', ':'))
    return json.loads(_check_models_cached(spec_json, inputs))


@lru_cache(maxsize=64)
def _check_models_cached(spec_json, inputs):
    report = _check_models_uncached(dict(inputs), json.loads(spec_json))
    return json.dumps(report, sort_keys=True, separators=(',', ':'))


def _check_models_uncached(resources, spec):
    from scp.verify import mesh_data, parse_paths, translated
    recipe = _recipe(spec)
    expected_preview, textures, checked, covered, native_tiles = [], set(), 0, 0, 0
    world_bed, world_routes, procedural_heights, world_walls = [], [], [], []
    for cell, raw_tile in zip(_cells(spec), spec['tile_ids']):
        tile = _number(raw_tile)
        raw = resources[*S3D, tile]
        model = parse_s3d(raw)
        validate_s3d(model)
        for zoom in range(5):
            require(resources[*S3D, tile + zoom] == raw, 'Rail zoom model differs from its checked base model')
            checked += 1
        texture_ids = {texture for material in model['materials'] for texture in material['textures']}
        adapter = _adapter(recipe, cell)
        expected_textures = {0x0BF6E09B, 0xEBF6E069} if adapter and adapter[0] in (0, 2, 4) else {0x0BF6E09B}
        require(texture_ids == expected_textures, 'Rail model references an unexpected texture atlas')
        expected_materials = ({MATERIAL_HASHES['native_deck'], MATERIAL_HASHES['native_pillar']}
                              if adapter and adapter[0] in (0, 2, 4) else
                              {MATERIAL_HASHES['native_deck' if adapter else 'procedural']})
        require({hashlib.sha256(material['raw']).hexdigest() for material in model['materials']} == expected_materials,
                'Rail model rendering material differs from the audited native material')
        textures.update(texture_ids)
        if adapter:
            require(_native_fingerprint(model, adapter[1]) == RAMP_GEOMETRY[adapter[0]],
                    'HSR/GHSR transition visible geometry or native texture coordinates were changed')
            native_tiles += 1
        else:
            vertices = [point for vb in model['vertices'] for point in positions(vb)]
            low, high = min(p[1] for p in vertices), max(p[1] for p in vertices)
            ground = _level(recipe) == 1.
            procedural_heights.extend(point[1] for point in vertices)
            require((low >= -.990 and high < 2.01) if ground else (low >= -EPS and high < 17.01),
                    'Rail deck has the wrong elevation or extends below its ground support')
            bed_height = 1.189326 if ground else 16.189326
            triangles = list(_triangles(model))
            bed = [tri for tri in triangles
                   if max(v[1] for v in tri) - min(v[1] for v in tri) < .001
                   and all(abs(v[1]-bed_height) < .06 for v in tri)]
            require(bed, 'Rail model lacks its visible native rail bed')
            for tri in triangles:
                wall = _wall_projection(tri, bed_height+.20)
                if wall:
                    world_walls.append([(x+16.*cell[0], z+16.*cell[1]) for x, z in wall])
            for tri in bed:
                world_bed.append(tuple((vertex[0]+16.*cell[0], vertex[1], vertex[2]+16.*cell[1], *vertex[3:])
                                       for vertex in tri))
            for route in parse_paths(resources[*PATH, tile])['routes']:
                world_routes.append([(x+16.*cell[0], y-16.*cell[1], height) for x, y, height in route['points']])
        props = {int(prop['id'], 16): prop['values'] for prop in exemplar(resources[*EXEMPLAR, tile])['properties']}
        require(props[0x10] == [11] and props[0x27812823] == [*S3D, *range(tile, tile+5)],
                'Rail exemplar references the wrong set of zoom models')
        expected_preview.extend((mesh_data(model, mesh), (16.*cell[0], 0., 16.*cell[1])) for mesh in model['meshes'])
    # NAM diagonal slabs overhang their owning cell. Audit the placed union,
    # rather than incorrectly requiring each PATH to sit on its own cell's
    # mesh alone. The preview check below separately pins every cell offset.
    buckets = defaultdict(list)
    if procedural_heights:
        low, high = min(procedural_heights), max(procedural_heights)
        require((-.990 < low < -.988 and 1.98 < high < 2.01) if _level(recipe) == 1. else
                (abs(low) < EPS and 16.98 < high < 17.01),
                'Rail assembly has the wrong deck profile height or lacks its elevated supports')
    for tri in world_bed:
        for x in range(math.floor(min(v[0] for v in tri)/4.), math.floor(max(v[0] for v in tri)/4.)+1):
            for z in range(math.floor(min(v[2] for v in tri)/4.), math.floor(max(v[2] for v in tri)/4.)+1):
                buckets[x, z].append(tri)
    junction_nodes = 0
    for route_index, points in enumerate(world_routes):
        for x, y, height in points:
            candidates = [(tri, _weights(x, -y, tri)) for tri in buckets[math.floor(x/4.), math.floor(-y/4.)]]
            candidates = [(tri, weights) for tri, weights in candidates if weights]
            require(candidates, 'Rail train route is not covered by its actual visible deck')
            error = min(min(abs(sum(v[3]*w for v, w in zip(tri, weights))-_rail_u(lane))
                            for lane in (-2., 2.)) for tri, weights in candidates)
            if error >= .014:
                # Two actual rails can cross inside a switch. A 2 m-wide
                # ribbon may cover its neighbour there; its atlas UV must
                # still belong to that rail ribbon, never a concrete edge.
                crossing = any(.20 < _distance((x, y), a, b) < 1.05
                               for other_index, other in enumerate(world_routes) if other_index != route_index
                               for a, b in zip(other, other[1:]))
                require(crossing and error < .070, 'Visible rail texture band does not line up with its train path')
                junction_nodes += 1
            covered += 1
    clearance_segments = _check_wall_clearance(world_walls, world_routes)
    preview = parse_s3d(resources[*S3D, _number(spec['preview_id'])])
    validate_s3d(preview)
    actual = [mesh_data(preview, mesh) for mesh in preview['meshes']]
    require(len(actual) == len(expected_preview) and all(translated(item, source, offset)
            for item, (source, offset) in zip(actual, expected_preview)),
            'Rail cursor preview differs from its placed models or exact cell spacing')
    return {'models_checked': checked + 1, 'preview_matches_tiles': True,
            'path_nodes_covered_by_visible_bed': covered, 'native_transition_models_preserved': native_tiles,
            'native_texture_bands_checked': True, 'rail_crossing_ribbon_nodes': junction_nodes,
            'above_bed_wall_clearance_segments': clearance_segments,
            'texture_ids': sorted(textures)}


def construction_expectations(spec):
    """Literal construction tables are added alongside the finalized layouts."""
    if spec['recipe'] == 'rail_hsr_road_stack':
        from .road_stack_verify import construction_expectations as stack_expectations
        return stack_expectations(spec)
    _recipe(spec)
    require(spec['recipe'] in CONSTRUCTION, 'Rail construction layout is not independently audited')
    cells, cons, flags, cost = CONSTRUCTION[spec['recipe']]
    return cells, cons, {f'{chr(97+n)}-monorail:0x{flag}' for n, flag in enumerate(flags)}, cost


def _construction(cells, size, flags, cost):
    """Serialize independently audited occupied cells into the RUL0 grid."""
    width, depth = size
    symbols = {cell: chr(97+n) for n, cell in enumerate(cells)}
    layouts = []
    for build in (False, True):
        rows = ['.' * (width+3)]
        for row in range(depth):
            rows.append('.' + ''.join(('+' if build else symbols[x, row])
                        if (x, row) in symbols else '.' for x in range(width)) +
                        ('.<' if row == 0 else '..'))
        rows.append('.^' + '.' * (width+1))
        layouts.append(rows)
    return *layouts, flags.split(), cost


_CROSSOVER_CELLS = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)]
CONSTRUCTION = {}
for _mode in ('hsr', 'ghsr'):
    CONSTRUCTION[f'rail_{_mode}_diagonal_s_left'] = _construction(
        [(2, 0), (2, 1), (1, 2), (2, 2)], (3, 3), '03010000 03000300 03010000 00000301', 400)
    CONSTRUCTION[f'rail_{_mode}_diagonal_s_right'] = _construction(
        [(2, 1), (0, 2), (1, 2), (2, 2)], (3, 3), '03010000 03010000 00010001 00000301', 400)
    for _hand, _flags in (
            ('crossover_right', '02000200 02000200 02010200 02000201 02000200 02000200'),
            ('crossover_left', '02000200 02000200 02030200 02000203 02000200 02000200')):
        CONSTRUCTION[f'rail_{_mode}_adjacent_{_hand}'] = _construction(_CROSSOVER_CELLS, (2, 3), _flags, 600)
CONSTRUCTION['rail_hsr_ghsr_transition'] = _construction(
    [(0, row) for row in range(8)], (1, 8), ' '.join(['02000200']*8), 800)
