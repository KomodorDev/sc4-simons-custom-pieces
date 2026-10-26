"""Independent encoded-resource checks for authored rail interchanges.

Contracts describe native-facing external ports and permitted movements. They
are separate from the layout and geometry writers. A resource must satisfy its
contract; the writer's own route output is never used as the expected answer.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
import hashlib
import json
import math
import re

from scp.dbpf import exemplar, require
from scp.models import parse_s3d, validate_s3d
from .rail_feature_verify import _triangles, _weights, _rail_u, _intersects, _distance

S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
EXEMPLAR = (0x6534284A, 0xA8434037)
EPS = 2e-6
TRAIN_HALF_WIDTH = 1.5
TRAIN_CLEARANCE_HEIGHT = 5.
EMPTY_PATH = ('SC4PATHS', '1.2', '0', '0', '0')
HSR_MATERIAL = 'dfa087a7554486e8dc3a86e0135ed181a76e59cffcf0ac05ca312dbea72ad591'

# Populated only with independently reviewed concrete layouts. An unknown
# interchange recipe must fail closed, rather than inherit a generic T shape.
CONTRACTS = {}

LEVEL_HEIGHTS = {'ground': 1., 'hsr': 15.5, 'l3': 23., 'l4': 30.5}
BRANCH_CONTROLS = {
    (45, 'compact'): ((2., -56.), (2., -24.), (16., -24.), (40., 0.)),
    (45, 'wide'): ((2., -104.), (2., -40.), (40., -16.), (88., 32.)),
    (90, 'compact'): ((2., -24.), (2., -8.), (8., 0.), (24., 0.)),
    (90, 'wide'): ((2., -88.), (2., -32.), (32., 0.), (88., 0.)),
    (135, 'compact'): ((2., -88.), (2., -8.), (40., 32.), (88., -16.)),
    (135, 'wide'): ((2., -184.), (2., -16.), (80., 64.), (184., -32.)),
}


def _cubic(control):
    # Independently sample the reviewed design at 4096 intervals, rather than
    # borrowing the writer's 64-interval route arrays or grid slicing code.
    result = []
    for n in range(4097):
        t, s = n/4096., 1.-n/4096.
        result.append(tuple(s*s*s*control[0][axis] + 3*s*s*t*control[1][axis] +
                            3*s*t*t*control[2][axis] + t*t*t*control[3][axis] for axis in (0, 1)))
    return result


def _occupied(lines):
    """Compute reviewed design cells without using the route writer."""
    cells = set()
    for line in lines:
        for a, b in zip(line, line[1:]):
            cuts = {0., 1.}
            for axis in (0, 1):
                if abs(b[axis]-a[axis]) < 1e-12:
                    continue
                lo, hi = sorted((a[axis], b[axis]))
                for n in range(math.floor((lo+8.)/16.), math.ceil((hi+8.)/16.)+1):
                    t = (16.*n-8.-a[axis])/(b[axis]-a[axis])
                    if 1e-9 < t < 1.-1e-9:
                        cuts.add(t)
            cuts = sorted(cuts)
            for lo, hi in zip(cuts, cuts[1:]):
                t = (lo+hi)/2.
                x, y = (a[axis]+t*(b[axis]-a[axis]) for axis in (0, 1))
                cells.add((math.floor((x+8.)/16.), math.floor((8.-y)/16.)))
    minimum_x, minimum_row = min(x for x, _ in cells), min(row for _, row in cells)
    return sorted(((x-minimum_x, row-minimum_row) for x, row in cells), key=lambda p: (p[1], p[0])), (-16.*minimum_x, 16.*minimum_row)


def _register(recipe, lines, ports, movements, *, min_height, max_height, kind, **extra):
    cells, shift = _occupied(lines)
    CONTRACTS[recipe] = {
        'cells': cells, 'footprint': (max(x for x, _ in cells)+1, max(y for _, y in cells)+1),
        'ports': {label: (point[0]+shift[0], point[1]+shift[1], point[2]) for label, point in ports.items()},
        'movements': movements, 'min_height': min_height, 'max_height': max_height,
        'max_grade': .25, 'cost': 100*len(cells), 'kind': kind, **extra,
    }


_SINGLE_SHAPES = {
    'straight': (((0., -8.), (0., 8.)), False),
    'diagonal': (((-8., -16.), (8., 0.)), False),
    'diagonal_north_half': (((-8., 0.), (0., 8.)), False),
    'diagonal_east_half': (((0., -8.), (8., 0.)), False),
    'curve_out_right': (((0., -24.), (0., -12.), (0., -8.), (8., 0.)), True),
    'curve_out_left': (((0., -24.), (0., -12.), (0., -8.), (-8., 0.)), True),
    'curve_in_left': (((-8., -16.), (0., -8.), (0., -4.), (0., 8.)), True),
    'curve_in_right': (((8., -16.), (0., -8.), (0., -4.), (0., 8.)), True),
}
for _level, _height in LEVEL_HEIGHTS.items():
    for _shape, (_control, _curved) in _SINGLE_SHAPES.items():
        _register(f'interchange_oneway_{_level}_{_shape}', [_cubic(_control) if _curved else _control],
                  {'in': (*_control[0], _height), 'out': (*_control[-1], _height)}, [('in', 'out')],
                  min_height=_height, max_height=_height, kind='single')
    for _radius, _size in (('compact', 40.), ('wide', 88.)):
        for _hand, _sign in (('left', -1.), ('right', 1.)):
            _control = ((0., -_size), (0., -.4*_size), (.4*_size*_sign, 0.), (_size*_sign, 0.))
            _suffix = '_wide' if _radius == 'wide' else ''
            _register(f'interchange_oneway_{_level}_turn90_{_hand}{_suffix}', [_cubic(_control)],
                      {'in': (*_control[0], _height), 'out': (*_control[-1], _height)}, [('in', 'out')],
                      min_height=_height, max_height=_height, kind='single')

for _level in ('ground', 'hsr', 'l4'):
    _height = LEVEL_HEIGHTS[_level]
    for (_angle, _radius), _reviewed_control in BRANCH_CONTROLS.items():
        _control = list(_reviewed_control)
        if _level == 'l4':
            _control[:2] = [(0., point[1]) for point in _control[:2]]
        _south = _control[0][1]
        for _mode in ('split', 'merge'):
            _branch = _cubic(_control)
            _branch_port = _control[-1]
            if _mode == 'merge':
                _branch = [(x, _south+8.-y) for x, y in reversed(_branch)]
                _branch_port = (_branch_port[0], _south+8.-_branch_port[1])
            if _level == 'l4':
                _lines = [[(0., _south), (0., 8.)], _branch]
                _ports = {'Sin': (0., _south, _height), 'Nout': (0., 8., _height)}
                _movements = [('Sin', 'Nout')]
            else:
                _lines = [[(2., _south), (2., 8.)], [(-2., 8.), (-2., _south)], _branch]
                _ports = {'Sin': (2., _south, _height), 'Nout': (2., 8., _height),
                          'Nin': (-2., 8., _height), 'Sout': (-2., _south, _height)}
                _movements = [('Sin', 'Nout'), ('Nin', 'Sout')]
            _ports['Bout' if _mode == 'split' else 'Bin'] = (*_branch_port, _height)
            _movements = [*_movements, ('Sin', 'Bout') if _mode == 'split' else ('Bin', 'Nout')]
            _register(f'interchange_{_level}_{_mode}_{_angle}_{_radius}', _lines, _ports, _movements,
                      min_height=_height, max_height=_height, kind='directed_branch')
            if _level == 'l4':
                _register(f'interchange_l4_{_mode}_{_angle}_{_radius}_left',
                          [[(-x, y) for x, y in line] for line in _lines],
                          {label: (-x, y, z) for label, (x, y, z) in _ports.items()}, _movements,
                          min_height=_height, max_height=_height, kind='directed_branch')

for _start, _finish in (('ground', 'hsr'), ('hsr', 'ground'), ('hsr', 'l3'), ('l3', 'hsr'),
                        ('l3', 'l4'), ('l4', 'l3'), ('hsr', 'l4'), ('l4', 'hsr')):
    _first, _last = LEVEL_HEIGHTS[_start], LEVEL_HEIGHTS[_finish]
    _depth = 8 if abs(_last-_first) >= 14.5 else 6
    _south = 8.-16.*_depth
    _register(f'interchange_oneway_grade_{_start}_to_{_finish}', [[(0., _south), (0., 8.)]],
              {'in': (0., _south, _first), 'out': (0., 8., _last)}, [('in', 'out')],
              min_height=min(_first, _last), max_height=max(_first, _last), kind='grade',
              endpoint_flat_length=16.)

for _lower in ('ground', 'hsr'):
    _height = LEVEL_HEIGHTS[_lower]
    _register(f'interchange_l4_oneway_over_{_lower}',
              [[(-24., 0.), (24., 0.)], [(2., -8.), (2., 8.)], [(-2., 8.), (-2., -8.)]],
              {'Win': (-24., 0., 30.5), 'Eout': (24., 0., 30.5),
               'Sin': (2., -8., _height), 'Nout': (2., 8., _height),
               'Nin': (-2., 8., _height), 'Sout': (-2., -8., _height)},
              [('Win', 'Eout'), ('Sin', 'Nout'), ('Nin', 'Sout')],
              min_height=_height, max_height=30.5, kind='crossing', required_grade_separated_crossings=2)

# Each mixed-heading crossing declares both actual networks. These literals
# preserve the native diagonal 2.8/2.9 m asymmetry at the external tile edges.
for _lower in ('ground', 'hsr'):
    _h = LEVEL_HEIGHTS[_lower]
    for _variant in ('upper_grid_lower_diag', 'upper_diag_lower_grid', 'upper_diag_lower_diag'):
        _diagonal_lower = 'lower_diag' in _variant
        _upper = [(-24., -16.), (16., 24.)] if _variant.startswith('upper_diag') else [(-24., 0.), (24., 0.)]
        if _diagonal_lower:
            _lower_forward, _lower_reverse = [(24., -13.1), (-13.2, 24.)], [(-18.9, 24.), (24., -18.9)]
        else:
            _lower_forward, _lower_reverse = [(2., -24.), (2., 24.)], [(-2., 24.), (-2., -24.)]
        _register(f'interchange_l4_{_variant}_over_{_lower}', [_upper, _lower_forward, _lower_reverse],
                  {'upper_in': (*_upper[0], 30.5), 'upper_out': (*_upper[-1], 30.5),
                   'lower_a_in': (*_lower_forward[0], _h), 'lower_a_out': (*_lower_forward[-1], _h),
                   'lower_b_in': (*_lower_reverse[0], _h), 'lower_b_out': (*_lower_reverse[-1], _h)},
                  [('upper_in', 'upper_out'), ('lower_a_in', 'lower_a_out'), ('lower_b_in', 'lower_b_out')],
                  min_height=_h, max_height=30.5, kind='crossing', required_grade_separated_crossings=2)
_register('interchange_ground_oneway_under_hsr',
          [[(-8., 0.), (8., 0.)], [(2., -24.), (2., 24.)], [(-2., 24.), (-2., -24.)]],
          {'Win': (-8., 0., 1.), 'Eout': (8., 0., 1.), 'Sin': (2., -24., 15.5),
           'Nout': (2., 24., 15.5), 'Nin': (-2., 24., 15.5), 'Sout': (-2., -24., 15.5)},
          [('Win', 'Eout'), ('Sin', 'Nout'), ('Nin', 'Sout')],
          min_height=1., max_height=15.5, kind='crossing', required_grade_separated_crossings=2)
_register('interchange_hsr_oneway_over_ground',
          [[(-24., 0.), (24., 0.)], [(2., -8.), (2., 8.)], [(-2., 8.), (-2., -8.)]],
          {'Win': (-24., 0., 15.5), 'Eout': (24., 0., 15.5), 'Sin': (2., -8., 1.),
           'Nout': (2., 8., 1.), 'Nin': (-2., 8., 1.), 'Sout': (-2., -8., 1.)},
          [('Win', 'Eout'), ('Sin', 'Nout'), ('Nin', 'Sout')],
          min_height=1., max_height=15.5, kind='crossing', required_grade_separated_crossings=2)

def _native_vectors():
    """Literal native-facing travel directions, independent of route sampling."""
    for recipe, contract in CONTRACTS.items():
        if contract['kind'] == 'directed_branch':
            match = re.fullmatch(r'interchange_(ground|hsr|l4)_(split|merge)_(45|90|135)_(compact|wide)(_left)?', recipe)
            require(match, 'Unknown native branch heading family')
            angle, merge, left = int(match[3]), match[2] == 'merge', bool(match[5])
            dx, dy = {45: (1., 1.), 90: (1., 0.), 135: (1., -1.)}[angle]
            if merge: dx = -dx
            if left: dx = -dx
            vectors = {'Sin': (0., 1.), 'Nout': (0., 1.)}
            if match[1] != 'l4': vectors.update({'Nin': (0., -1.), 'Sout': (0., -1.)})
            vectors['Bin' if merge else 'Bout'] = dx, dy
        elif contract['kind'] == 'grade':
            vectors = {'in': (0., 1.), 'out': (0., 1.)}
        elif contract['kind'] == 'single':
            shape = re.sub(r'^interchange_oneway_(ground|hsr|l3|l4)_', '', recipe)
            if shape.startswith('turn90_'):
                vectors = {'in': (0., 1.), 'out': (-1., 0.) if '_left' in shape else (1., 0.)}
            else:
                vectors = {'in': (0., 1.), 'out': (0., 1.)}
                if shape in ('diagonal', 'diagonal_north_half', 'diagonal_east_half'):
                    vectors = {'in': (1., 1.), 'out': (1., 1.)}
                elif shape.startswith('curve_out_'):
                    vectors['out'] = (-1., 1.) if shape.endswith('left') else (1., 1.)
                elif shape.startswith('curve_in_'):
                    vectors['in'] = (1., 1.) if shape.endswith('left') else (-1., 1.)
        elif 'lower_a_in' in contract['ports']:
            upper = (1., 1.) if '_upper_diag_' in recipe else (1., 0.)
            lower = (-1., 1.) if '_lower_diag_' in recipe else (0., 1.)
            vectors = {'upper_in': upper, 'upper_out': upper, 'lower_a_in': lower,
                       'lower_a_out': lower, 'lower_b_in': tuple(-v for v in lower),
                       'lower_b_out': tuple(-v for v in lower)}
        else:
            vectors = {'Win': (1., 0.), 'Eout': (1., 0.), 'Sin': (0., 1.),
                       'Nout': (0., 1.), 'Nin': (0., -1.), 'Sout': (0., -1.)}
        require(set(vectors) == set(contract['ports']), 'Native heading contract omits a port')
        contract['port_vectors'] = vectors


_native_vectors()


def _native_port_headings(records, contract):
    ports = {_point(point): label for label, point in contract['ports'].items()}
    expected = contract['port_vectors']
    checked = {}
    for cell, route, points in records:
        for point, a, b, edge, incoming in ((points[0], points[0], points[1], route['entry'], True),
                                           (points[-1], points[-2], points[-1], route['exit'], False)):
            label = ports.get(_point(point))
            if label is None: continue
            require(label.endswith('in') == incoming, 'Native-facing port has an incorrect travel direction')
            dx, dy = b[0]-a[0], b[1]-a[1]
            ex, ey = expected[label]
            norm = math.hypot(dx, dy)*math.hypot(ex, ey)
            require(norm > EPS and abs(dx*ey-dy*ex)/norm <= 2e-5 and
                    (dx*ex+dy*ey)/norm > .999999,
                    f'Interchange external port does not have its literal native-facing tangent: {label}, {(dx, dy)}, expected {(ex, ey)}')
            checked[label] = cell, edge, _edge_category(edge, (ex, ey))
    require(set(checked) == set(expected), 'Native-facing tangent check omitted a declared port')
    return checked


def _number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def _point(point):
    return tuple(round(value, 6) for value in point)


def _contract(spec):
    recipe = spec['recipe']
    require(recipe in CONTRACTS, 'Unknown interchange recipe requires an independently audited port contract')
    contract = CONTRACTS[recipe]
    cells = [tuple(cell) for cell in spec['cells']]
    require(cells == contract['cells'] and tuple(spec['footprint']) == contract['footprint'],
            'Interchange footprint differs from its independent port contract')
    structural = [tuple(cell) for cell in spec.get('structural_cells', [])]
    require(structural == contract.get('structural_cells', []), 'Interchange structural cells are not independently declared')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(cells), 'Interchange tile count differs from its occupied footprint')
    base = tiles[0] - 0x100*cells[0][0] - 0x10*cells[0][1]
    require(tiles == [base+0x100*x+0x10*y for x, y in cells], 'Interchange AutoTileBase allocation is inconsistent')
    return contract


def _paths(raw, structural=False):
    from scp.verify import parse_paths
    lines = tuple(line.strip() for line in raw.decode('ascii').splitlines() if line.strip())
    if structural:
        require(lines == EMPTY_PATH, 'Structural interchange cell must have exactly the native empty PATH header')
        return []
    require(lines != EMPTY_PATH, 'A train-carrying interchange cell has no train route')
    parsed = parse_paths(raw)
    require(parsed['version'] == '1.2' and parsed['terrain'] == 0, 'Authored interchange PATH must use explicit 1.2 junction fields')
    return parsed['routes']


def _encoded_routes(resources, spec, contract):
    from scp.verify import edge
    records = []
    structural = set(contract.get('structural_cells', []))
    for cell, raw_tile in zip(contract['cells'], spec['tile_ids']):
        routes = _paths(resources[*PATH, _number(raw_tile)], cell in structural)
        signatures, starts = set(), defaultdict(list)
        for route in routes:
            points = route['points']
            require(route['transport'] == 7 and route['lane'] >= 0 and route['compatibility'] in (0, 1),
                    'Interchange route has a foreign transport, negative path class, or invalid junction flag')
            require(edge(points[0]) == route['entry'] and edge(points[-1]) == route['exit'],
                    'Interchange route edge fields disagree with its actual endpoint')
            require(route['entry'] != route['exit'] or contract.get('allow_same_edge', False),
                    'Interchange route makes an undeclared same-edge curve')
            require(all(abs(x) <= 8.+EPS and abs(y) <= 8.+EPS for x, y, _ in points),
                    'Interchange PATH leaves its assigned tile')
            signature = tuple(map(_point, points))
            require(signature not in signatures, 'Interchange repeats an identical encoded train route')
            signatures.add(signature)
            starts[_point(points[0])].append(route)
            for a, b in zip(points, points[1:]):
                run = math.hypot(b[0]-a[0], b[1]-a[1])
                require(run > EPS, 'Interchange route contains a zero-length segment or vertical teleport')
                require(abs(b[2]-a[2])/run <= contract.get('max_grade', .25)+EPS,
                        'Interchange route exceeds its bounded rise/run grade')
            require(all(contract['min_height']-EPS <= point[2] <= contract['max_height']+EPS for point in points),
                    'Interchange route leaves its independently declared height range')
            world = [_point((x+16.*cell[0], y-16.*cell[1], height)) for x, y, height in points]
            records.append((cell, route, world))
        for choices in starts.values():
            require(len(choices) == 1 or any(route['compatibility'] == 1 for route in choices),
                    'Interchange branch choice has no explicit junction flag')
        classes = defaultdict(list)
        for route in routes:
            classes[route['entry'], route['exit']].append(route['lane'])
        require(all(sorted(values) == ([0] if len(values) == 1 else list(range(1, len(values)+1)))
                    for values in classes.values()), 'Interchange path classes are missing, repeated, or out of range')
    return records


def _turn(point, quarters):
    x, y, height = point
    for _ in range(quarters % 4):
        x, y = -y, x
    return _point((x, y, height))


def _graph(records, contract):
    graph, incoming, outgoing = defaultdict(set), defaultdict(list), defaultdict(list)
    for cell, _, points in records:
        graph[points[0]].add(points[-1])
        outgoing[points[0]].append(cell)
        incoming[points[-1]].append(cell)
    ports = {label: _point(point) for label, point in contract['ports'].items()}
    external = {point: label for label, point in ports.items()}
    require(len(external) == len(ports), 'Interchange has duplicate independent external port coordinates')
    endpoints = set(incoming) | set(outgoing)
    require(set(external) <= endpoints, 'Interchange is missing a native-facing external port')
    for point in endpoints - set(external):
        require(incoming[point] and outgoing[point] and
                any(a != b for a in incoming[point] for b in outgoing[point]),
                'Interchange has a disconnected internal port or cross-level seam jump')
    for label, point in ports.items():
        require(bool(outgoing[point]) == label.endswith('in') and bool(incoming[point]) == label.endswith('out'),
                'Interchange external port permits travel in the wrong direction')
    degree = {point: 0 for point in endpoints}
    for ends in graph.values():
        for point in ends:
            degree[point] += 1
    pending = [point for point, count in degree.items() if count == 0]
    acyclic = set()
    while pending:
        point = pending.pop()
        acyclic.add(point)
        for end in graph.get(point, ()):
            degree[end] -= 1
            if degree[end] == 0:
                pending.append(end)
    require(acyclic == endpoints, 'Interchange contains an unintended directed route cycle')
    allowed = set(map(tuple, contract['movements']))
    for turns in range(4):
        rotated = {_turn(start, turns): {_turn(end, turns) for end in ends} for start, ends in graph.items()}
        boundary = {_turn(point, turns): label for label, point in ports.items()}
        actual, all_reachable = set(), set()
        for label, point in ports.items():
            if not label.endswith('in'):
                continue
            source = _turn(point, turns)
            pending, visited = [source], set()
            while pending:
                node = pending.pop()
                if node in visited:
                    continue
                visited.add(node)
                if node != source and node in boundary:
                    actual.add((label, boundary[node]))
                pending.extend(rotated.get(node, ()))
            all_reachable.update(visited)
        require(actual == allowed, 'Interchange permits a missing movement, reverse movement, or unwanted U-turn')
        require(set(rotated) | {end for ends in rotated.values() for end in ends} <= all_reachable,
                'Interchange contains an isolated internal route loop')
    return len(ports), len(allowed)


def _intersection(a, b, c, d):
    """Parameters of one horizontal crossing; parallel tracks return None."""
    dx, dy, ex, ey = b[0]-a[0], b[1]-a[1], d[0]-c[0], d[1]-c[1]
    determinant = dx*ey-dy*ex
    if abs(determinant) < 1e-10:
        return None
    cx, cy = c[0]-a[0], c[1]-a[1]
    first, second = (cx*ey-cy*ex)/determinant, (cx*dy-cy*dx)/determinant
    if -1e-7 <= first <= 1.+1e-7 and -1e-7 <= second <= 1.+1e-7:
        return max(0., min(1., first)), max(0., min(1., second))
    return None


def _crossing_audit(records, contract):
    """Check real opposite/crossing train movements and vertical deck space."""
    segments, buckets = [], defaultdict(list)
    for route_index, (_, _, points) in enumerate(records):
        for node_index, (a, b) in enumerate(zip(points, points[1:])):
            index = len(segments)
            segments.append((route_index, node_index, a, b))
            for x in range(math.floor(min(a[0], b[0])/8.), math.floor(max(a[0], b[0])/8.)+1):
                for y in range(math.floor(min(a[1], b[1])/8.), math.floor(max(a[1], b[1])/8.)+1):
                    buckets[x, y].append(index)
    compared, separated = set(), set()
    for candidates in buckets.values():
        for offset, first in enumerate(candidates):
            for second in candidates[offset+1:]:
                pair = tuple(sorted((first, second)))
                if first == second or pair in compared:
                    continue
                compared.add(pair)
                route_a, node_a, a, b = segments[first]
                route_b, node_b, c, d = segments[second]
                if route_a == route_b and abs(node_a-node_b) <= 1:
                    continue
                crossing = _intersection(a, b, c, d)
                if crossing is None:
                    continue
                t, u = crossing
                ha, hb = a[2]+t*(b[2]-a[2]), c[2]+u*(d[2]-c[2])
                dot = ((b[0]-a[0])*(d[0]-c[0])+(b[1]-a[1])*(d[1]-c[1])) / (
                    math.hypot(b[0]-a[0], b[1]-a[1])*math.hypot(d[0]-c[0], d[1]-c[1]))
                if abs(ha-hb) < 1e-5 and dot > .25:
                    continue  # Same-direction joining/diverging track.
                upper, lower = max(ha, hb), min(ha, hb)
                clearance = (14.01067+_offset(upper))-(16.98933+_offset(lower))
                require(clearance >= contract.get('minimum_clearance', 5.)-EPS,
                        f'Interchange crossing lacks actual vertical deck clearance or crosses opposing traffic at grade; '
                        f'XY {(a[0]+t*(b[0]-a[0]), a[1]+t*(b[1]-a[1]))}, heights {(ha, hb)}, direction dot {dot:.6f}, clearance {clearance:.6f}; '
                        f'routes {(route_a, route_b)} segments {(a, b)} / {(c, d)}')
                separated.add(_point((a[0]+t*(b[0]-a[0]), a[1]+t*(b[1]-a[1]), upper)))
    require(len(separated) >= contract.get('required_grade_separated_crossings', 0),
            'Interchange claims a flyover without the required real grade-separated train crossings')
    return len(separated)


def check_paths(resources, spec, donors=None):
    contract = _contract(spec)
    records = _encoded_routes(resources, spec, contract)
    ports, movements = _graph(records, contract)
    if contract['kind'] == 'grade':
        first, last = contract['ports']['in'], contract['ports']['out']
        flat = contract['endpoint_flat_length']
        require(all(abs(point[2]-first[2]) < EPS for _, _, points in records for point in points
                    if point[1] <= first[1]+flat+EPS) and
                all(abs(point[2]-last[2]) < EPS for _, _, points in records for point in points
                    if point[1] >= last[1]-flat-EPS),
                'Interchange height connector lacks its declared flat endpoint sections')
    _native_port_headings(records, contract)
    separated = _crossing_audit(records, contract)
    return {'tile_count': len(contract['cells']), 'encoded_routes_checked': len(records),
            'external_ports_checked': ports, 'permitted_movements_checked': movements,
            'rotations_checked': 4, 'exact_3d_cell_seams': True, 'unwanted_u_turns': False,
            'grade_separated_crossings_checked': separated, 'native_facing_port_tangents_checked': ports}


def _edge_category(edge, vector):
    dx, dy = vector
    if min(abs(dx), abs(dy)) < 1e-7:
        return 2
    return (3 if dx*dy > 0 else 1) if edge in (1, 3) else (1 if dx*dy > 0 else 3)


def check_construction_fields(fields, spec, resources, contract=None):
    """Compare actual encoded port headings with the RUL0 cell palette."""
    contract = _contract(spec) if contract is None else contract
    records = _encoded_routes(resources, spec, contract)
    width, depth = contract['footprint']
    grids = []
    for field in ('CellLayout', 'ConsLayout'):
        rows = [re.sub(r'\s+', '', value) for value in fields[field]]
        require(len(rows) == depth+2 and all(len(row) == width+3 for row in rows),
                'Interchange construction grid dimensions are wrong')
        require(rows[0] == '.'*(width+3) and rows[-1] == '.^'+'.'*(width+1),
                'Interchange construction anchor row is wrong')
        require(all(row[0] == '.' and row[-2:] == ('.<' if y == 0 else '..')
                    for y, row in enumerate(rows[1:-1])), 'Interchange grid has an inconsistent construction anchor')
        grids.append({(x, y): rows[y+1][x+1] for y in range(depth) for x in range(width)})
    cells, construction = grids
    require({cell for cell, symbol in construction.items() if symbol == '+'} == set(contract['cells']) and
            all(symbol in '.+' for symbol in construction.values()), 'Interchange occupied construction cells differ')
    require({cell for cell, symbol in cells.items() if symbol != '.'} == set(contract['cells']),
            'Interchange cell-check grid differs from its independently reserved cells')
    palette = {}
    for value in fields['CheckType']:
        match = re.fullmatch(r'([A-Za-z])-monorail:0x([0-9a-fA-F]{8})', re.sub(r'\s+', '', value))
        require(match and match[1] not in palette, 'Interchange has a duplicate or unsupported cell-check type')
        palette[match[1]] = int(match[2], 16)
    require(set(palette) == {symbol for symbol in cells.values() if symbol != '.'},
            'Interchange cell palette has unused or undefined symbols')
    native_headings = _native_port_headings(records, contract)
    native_points = {_point(point): native_headings[label][2] for label, point in contract['ports'].items()}
    headings = defaultdict(lambda: defaultdict(set))
    for cell, route, points in records:
        for edge, endpoint, a, b in ((route['entry'], points[0], points[0], points[1]),
                                      (route['exit'], points[-1], points[-2], points[-1])):
            category = native_points.get(_point(endpoint), _edge_category(edge, (b[0]-a[0], b[1]-a[1])))
            headings[cell][edge].add(category)
    for cell in contract['cells']:
        value = palette[cells[cell]]
        sides = [(value >> (8*edge)) & 255 for edge in range(4)]
        for edge, actual in enumerate(sides):
            expected = headings[cell][edge]
            require((actual == 0) == (not expected), 'Interchange construction edge presence disagrees with encoded PATH')
            if expected:
                desired = 2 if 2 in expected or {1, 3} <= expected else next(iter(expected))
                require(actual == desired, 'Interchange construction edge heading disagrees with encoded PATH')
    require(fields['Costs'] == [str(contract['cost'])], 'Interchange construction cost differs from its independent contract')
    return {'occupied_cells_checked': len(contract['cells']), 'check_types_checked': len(palette),
            'encoded_path_edge_headings_checked': True,
            'native_external_edge_categories_checked': len(native_headings)}


def _offset(height):
    return (height-15.5)*15./14.5 if height < 15.5 else height-15.5


def _bed(height):
    return 16.189326+_offset(height)


def _clip_band(polygon, value, inside_positive):
    result = []
    previous = polygon[-1]
    prev = value(previous)
    for current in polygon:
        curr = value(current)
        a, b = prev >= 0. if inside_positive else prev <= 0., curr >= 0. if inside_positive else curr <= 0.
        if a != b:
            t = prev/(prev-curr)
            result.append(tuple(previous[axis]+t*(current[axis]-previous[axis]) for axis in range(3)))
        if b:
            result.append(current[:3])
        previous, prev = current, curr
    return result


def _inside_convex(point, polygon):
    signs = [(b[0]-a[0])*(point[1]-a[1])-(b[1]-a[1])*(point[0]-a[0])
             for a, b in zip(polygon, polygon[1:]+polygon[:1])]
    return all(value >= -1e-6 for value in signs) or all(value <= 1e-6 for value in signs)


def _clearance_segments(records, buckets, *, half_width=TRAIN_HALF_WIDTH):
    """Reject walls, posts and beams in an authored 3 m-wide, 5 m-high envelope.

    Clip each candidate 3D triangle against planes following the actual grade.
    This detects a vertical post between PATH samples while allowing a clear
    bridge deck many metres overhead. The 5 m rule is authored conservatism,
    not a claim about an undocumented game collision threshold.
    """
    require(math.isfinite(half_width) and half_width >= TRAIN_HALF_WIDTH, 'Authored clearance cannot be narrower than the3m baseline')
    checked = 0
    for _, _, points in records:
        for first, last in zip(points, points[1:]):
            a, b = (first[0], -first[1]), (last[0], -last[1])
            dx, dz = b[0]-a[0], b[1]-a[1]
            length2 = dx*dx+dz*dz
            length = math.sqrt(length2)
            nx, nz = -dz/length, dx/length
            corridor = [(a[0]+half_width*nx, a[1]+half_width*nz),
                        (b[0]+half_width*nx, b[1]+half_width*nz),
                        (b[0]-half_width*nx, b[1]-half_width*nz),
                        (a[0]-half_width*nx, a[1]-half_width*nz)]
            corridor_bounds = [(min(p[axis] for p in corridor), max(p[axis] for p in corridor))
                               for axis in (0, 1)]
            floor_a, floor_b = _bed(first[2]), _bed(last[2])
            def relative(point):
                t = ((point[0]-a[0])*dx+(point[2]-a[1])*dz)/length2
                return point[1]-(floor_a+t*(floor_b-floor_a))
            candidates = {}
            for x in range(math.floor((min(a[0], b[0])-half_width)/4.), math.floor((max(a[0], b[0])+half_width)/4.)+1):
                for z in range(math.floor((min(a[1], b[1])-half_width)/4.), math.floor((max(a[1], b[1])+half_width)/4.)+1):
                    for triangle in buckets[x, z]:
                        candidates[id(triangle)] = triangle
            for triangle in candidates.values():
                if max(v[1] for v in triangle) < min(floor_a, floor_b)+.20 or min(v[1] for v in triangle) > max(floor_a, floor_b)+TRAIN_CLEARANCE_HEIGHT:
                    continue
                polygon = _clip_band(triangle, lambda p: relative(p)-.20, True)
                if len(polygon) < 3:
                    continue
                polygon = _clip_band(polygon, lambda p: relative(p)-TRAIN_CLEARANCE_HEIGHT, False)
                if len(polygon) < 3:
                    continue
                projected = [(p[0], p[2]) for p in polygon]
                # Intersection requires overlapping axis-aligned bounds.
                # Test this necessary condition before orientation predicates:
                # a submicrometre cap edge otherwise looks collinear with a
                # distant corridor edge under their absolute area guard.
                # The unchanged coordinate guard keeps this rejection
                # conservative; triangles inside the corridor still undergo
                # all original height, polygon and segment checks.
                if any(max(p[axis] for p in projected) < lower-EPS
                       or min(p[axis] for p in projected) > upper+EPS
                       for axis, (lower, upper) in enumerate(corridor_bounds)):
                    continue
                area = abs(sum(a[0]*b[1]-b[0]*a[1]
                               for a, b in zip(projected, projected[1:]+projected[:1])))
                blocked = (any(_inside_convex(point, corridor) for point in projected) or
                    (area > 1e-8 and any(_inside_convex(point, projected) for point in corridor)) or
                    any(_intersects(c, d, e, f) for c, d in zip(projected, projected[1:]+projected[:1])
                        for e, f in zip(corridor, corridor[1:]+corridor[:1])))
                require(not blocked,
                        f'Interchange wall, pillar, beam, or lower deck blocks an actual train-clearance envelope; '
                        f'PATH {first} to {last}; triangle {[p[:3] for p in triangle]}')
            checked += 1
    return checked


def _neighbour_rail_ribbon(point, candidates, route_segments, route_index):
    """Prove an overlapping stripe belongs to another actual nearby track.

    Merely finding a neighbour is insufficient: the *same covering triangle*
    must continue its affine UV field to a native rail-band UV at the nearest
    point on that neighbour (at most 1.05 m away). Clipping can split a stripe
    into tiny triangles that do not each contain both points. A shifted atlas
    or concrete floor cannot obtain an exception this way.
    """
    x, y, height = point
    for other_index, a, b in route_segments:
        distance = _distance((x, y), a, b)
        if other_index == route_index or not EPS < distance < 1.05:
            continue
        dx, dy = b[0]-a[0], b[1]-a[1]
        t = max(0., min(1., ((x-a[0])*dx+(y-a[1])*dy)/(dx*dx+dy*dy)))
        px, py, ph = (a[axis]+t*(b[axis]-a[axis]) for axis in range(3))
        if abs(height-ph) >= .05:
            continue
        for triangle, weights in candidates:
            own_u = sum(v[3]*w for v, w in zip(triangle, weights))
            if min(abs(own_u-_rail_u(lane)) for lane in (-2., 2.)) >= .070:
                continue
            va, vb, vc = triangle
            determinant = (vb[2]-vc[2])*(va[0]-vc[0])+(vc[0]-vb[0])*(va[2]-vc[2])
            if abs(determinant) < 1e-8:
                continue
            wa = ((vb[2]-vc[2])*(px-vc[0])+(vc[0]-vb[0])*(-py-vc[2]))/determinant
            wb = ((vc[2]-va[2])*(px-vc[0])+(va[0]-vc[0])*(-py-vc[2]))/determinant
            nearest = wa, wb, 1.-wa-wb
            if abs(sum(v[1]*w for v, w in zip(triangle, nearest))-_bed(ph)) >= .10:
                continue
            neighbour_u = sum(v[3]*w for v, w in zip(triangle, nearest))
            if min(abs(neighbour_u-_rail_u(lane)) for lane in (-2., 2.)) < .014:
                return True
    return False


def check_models(resources, spec, donors=None):
    _contract(spec)
    keys = {(*S3D, _number(spec['preview_id']))}
    for raw_tile in spec['tile_ids']:
        tile = _number(raw_tile)
        keys.update({(*S3D, tile+zoom) for zoom in range(5)})
        keys.update({(*PATH, tile), (*EXEMPLAR, tile)})
    immutable = tuple((key, resources[key]) for key in sorted(keys))
    return json.loads(_models_cached(json.dumps(spec, sort_keys=True, separators=(',', ':')), immutable))


@lru_cache(maxsize=256)
def _models_cached(spec_json, immutable):
    return json.dumps(_models(dict(immutable), json.loads(spec_json)), sort_keys=True, separators=(',', ':'))


def _models(resources, spec, contract=None):
    from scp.verify import mesh_data, translated
    contract = _contract(spec) if contract is None else contract
    records = _encoded_routes(resources, spec, contract)
    expected_preview, triangles, textures = [], [], set()
    width, depth = contract['footprint']
    minimum, maximum = math.inf, -math.inf
    occupied = set(contract['cells'])
    def reserved_foundation(point):
        fx, fy = (point[0]+8.)/16., (point[2]+8.)/16.
        columns, rows = {math.floor(fx)}, {math.floor(fy)}
        if abs(fx-round(fx)) < 1e-5:
            columns.add(round(fx)-1)
        if abs(fy-round(fy)) < 1e-5:
            rows.add(round(fy)-1)
        return any((x, y) in occupied for x in columns for y in rows)
    for cell, raw_tile in zip(contract['cells'], spec['tile_ids']):
        tile = _number(raw_tile)
        raw = resources[*S3D, tile]
        model = parse_s3d(raw)
        validate_s3d(model)
        require(all(resources[*S3D, tile+zoom] == raw for zoom in range(5)), 'Interchange zoom models differ')
        require(all(hashlib.sha256(material['raw']).hexdigest() == HSR_MATERIAL for material in model['materials']),
                'Interchange model uses an unaudited rendering material')
        textures.update(texture for material in model['materials'] for texture in material['textures'])
        for triangle in _triangles(model):
            world = tuple((x+16.*cell[0], height, z+16.*cell[1], u, v) for x, height, z, u, v in triangle)
            require(all(-8.-EPS <= p[0] <= 16.*width-8.+EPS and -8.-EPS <= p[2] <= 16.*depth-8.+EPS
                        for p in world), 'Interchange geometry occupies land outside its declared footprint')
            minimum = min(minimum, min(v[1] for v in world))
            maximum = max(maximum, max(v[1] for v in world))
            if max(v[1] for v in world) >= 3.:
                base = [point for point in world if abs(point[1]) < 1e-5]
                samples = base + [tuple((a[axis]+b[axis])/2. for axis in range(3))
                                  for n, a in enumerate(base) for b in base[n+1:]]
                require(all(reserved_foundation(point) for point in samples),
                        'Interchange support foundation occupies an unreserved construction cell')
            triangles.append(world)
        props = {int(p['id'], 16): p['values'] for p in exemplar(resources[*EXEMPLAR, tile])['properties']}
        require(props[0x10] == [11] and props[0x27812823] == [*S3D, *range(tile, tile+5)],
                'Interchange exemplar references the wrong zoom models')
        expected_preview.extend((mesh_data(model, mesh), (16.*cell[0], 0., 16.*cell[1])) for mesh in model['meshes'])
    require(minimum >= -.991 and maximum <= 16.990+_offset(contract['max_height'])+.05,
            'Interchange model exceeds its declared native profile height range')
    require(contract['max_height'] <= 1. or abs(minimum) < EPS or minimum < -.98,
            'Elevated interchange has no foundation at ground level')
    buckets = defaultdict(list)
    for triangle in triangles:
        # Include float32 edge rounding on exact 4 m bucket boundaries. The
        # barycentric predicate already permits this small boundary tolerance.
        for x in range(math.floor((min(v[0] for v in triangle)-1e-4)/4.), math.floor((max(v[0] for v in triangle)+1e-4)/4.)+1):
            for z in range(math.floor((min(v[2] for v in triangle)-1e-4)/4.), math.floor((max(v[2] for v in triangle)+1e-4)/4.)+1):
                buckets[x, z].append(triangle)
    route_buckets = defaultdict(list)
    for index, (_, _, points) in enumerate(records):
        for a, b in zip(points, points[1:]):
            for x in range(math.floor((min(a[0], b[0])-1.05)/4.), math.floor((max(a[0], b[0])+1.05)/4.)+1):
                for y in range(math.floor((min(a[1], b[1])-1.05)/4.), math.floor((max(a[1], b[1])+1.05)/4.)+1):
                    route_buckets[x, y].append((index, a, b))
    covered, junction_nodes = 0, 0
    for route_index, (_, _, points) in enumerate(records):
        for x, y, height in points:
            candidates = []
            for triangle in buckets[math.floor(x/4.), math.floor(-y/4.)]:
                weights = _weights(x, -y, triangle)
                if weights and abs(sum(v[1]*w for v, w in zip(triangle, weights))-_bed(height)) < .10:
                    candidates.append((triangle, weights))
            require(candidates, f'Interchange PATH has no matching visible rail bed at its actual height: {(x, y, height)}')
            error = min(min(abs(sum(v[3]*w for v, w in zip(triangle, weights))-_rail_u(lane))
                            for lane in (-2., 2.)) for triangle, weights in candidates)
            if error >= .014:
                require(_neighbour_rail_ribbon((x, y, height), candidates,
                            route_buckets[math.floor(x/4.), math.floor(y/4.)], route_index),
                        f'Interchange visible native rail band does not follow the train PATH: {(x, y, height)}, U error {error:.6f}')
                junction_nodes += 1
            covered += 1
    clearance_width = contract.get('clearance_width_m', 2.*TRAIN_HALF_WIDTH)
    clearance_segments = _clearance_segments(records, buckets, half_width=clearance_width/2.)
    preview = parse_s3d(resources[*S3D, _number(spec['preview_id'])])
    validate_s3d(preview)
    actual = [mesh_data(preview, mesh) for mesh in preview['meshes']]
    require(len(actual) == len(expected_preview) and all(translated(item, source, offset)
            for item, (source, offset) in zip(actual, expected_preview)),
            'Interchange preview differs from its actual placed models or cell spacing')
    return {'models_checked': 5*len(contract['cells'])+1, 'path_nodes_covered_by_visible_bed': covered,
            'preview_matches_tiles': True, 'native_material_preserved': True,
            'train_clearance_segments_checked': clearance_segments,
            'authored_clearance_width_m': clearance_width,
            'authored_clearance_height_m': TRAIN_CLEARANCE_HEIGHT,
            'support_foundations_within_reserved_cells': True,
            'rail_crossing_ribbon_nodes': junction_nodes, 'texture_ids': sorted(textures)}
