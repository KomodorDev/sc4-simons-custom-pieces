"""Rail track shapes, directed route geometry and construction flags.

Cell (x,row) has PATH centre (16*x,-16*row). The 15.5 m reference
height and Monorail route semantics belong to the high-speed rail domain.
"""
from __future__ import annotations

import math
from scp.dbpf import require

HEIGHT = 15.5
EPS = 1e-6

_SHAPES = {'straight': {'cells': [(0, 0)], 'footprint': (1, 1), 'start': (0.0, -8.0), 'end': (0.0, 8.0)},
 'diagonal': {'cells': [(0, 0), (0, 1)],
              'footprint': (1, 2),
              'start': (-8.0, -16.0),
              'end': (8.0, 0.0)},
 'diagonal_north_half': {'cells': [(0, 0)],
                         'footprint': (1, 1),
                         'start': (-8.0, 0.0),
                         'end': (0.0, 8.0)},
 'diagonal_east_half': {'cells': [(0, 0)],
                        'footprint': (1, 1),
                        'start': (0.0, -8.0),
                        'end': (8.0, 0.0)},
 'curve_out_right': {'cells': [(0, 0), (0, 1)],
                     'footprint': (1, 2),
                     'control': [(0.0, -24.0), (0.0, -12.0), (0.0, -8.0), (8.0, 0.0)],
                     'start': (0.0, -24.0),
                     'end': (8.0, 0.0)},
 'curve_out_left': {'cells': [(0, 0), (0, 1)],
                    'footprint': (1, 2),
                    'control': [(0.0, -24.0), (0.0, -12.0), (0.0, -8.0), (-8.0, 0.0)],
                    'start': (0.0, -24.0),
                    'end': (-8.0, 0.0)},
 'curve_in_left': {'cells': [(0, 0), (0, 1)],
                   'footprint': (1, 2),
                   'control': [(-8.0, -16.0), (0.0, -8.0), (0.0, -4.0), (0.0, 8.0)],
                   'start': (-8.0, -16.0),
                   'end': (0.0, 8.0)},
 'curve_in_right': {'cells': [(0, 0), (0, 1)],
                    'footprint': (1, 2),
                    'control': [(8.0, -16.0), (0.0, -8.0), (0.0, -4.0), (0.0, 8.0)],
                    'start': (8.0, -16.0),
                    'end': (0.0, 8.0)}}

def _bezier(control, t):
    u = 1. - t
    return tuple(u**3 * control[0][a] + 3*u*u*t * control[1][a] +
                 3*u*t*t * control[2][a] + t**3 * control[3][a] for a in (0, 1))


def _tangent(control, t):
    u = 1. - t
    return tuple(3*u*u*(control[1][a]-control[0][a]) +
                 6*u*t*(control[2][a]-control[1][a]) +
                 3*t*t*(control[3][a]-control[2][a]) for a in (0, 1))


def _root(control, axis, boundary):
    first, last = control[0][axis], control[-1][axis]
    if not min(first, last) + 1e-12 < boundary < max(first, last) - 1e-12:
        return None
    low, high = 0., 1.
    increasing = last > first
    for _ in range(64):
        middle = (low + high) / 2
        if (_bezier(control, middle)[axis] < boundary) == increasing:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def _snap(value):
    nearest = round((value + 8.) / 16.) * 16. - 8.
    return nearest if abs(value - nearest) < 1e-9 else value


def _edge(point):
    x, y = point[:2]
    edges = [abs(x + 8.) < EPS, abs(y - 8.) < EPS,
             abs(x - 8.) < EPS, abs(y + 8.) < EPS]
    require(sum(edges) == 1, f'Endpoint must be on one tile edge: {point}')
    return edges.index(True)


def _route(points, role, tangent_in, tangent_out, junction=False):
    return {'transport': 7, 'entry': _edge(points[0]), 'exit': _edge(points[-1]),
            'points': points, 'role': role, 'junction': bool(junction),
            'tangent_in': tangent_in, 'tangent_out': tangent_out}


def _branch_segments(key, info):
    """Cut a monotonic cubic at exact grid intersections before sampling it."""
    if 'control' not in info:
        if key == 'straight':
            points = [(0., -8., HEIGHT), (0., 8., HEIGHT)]
            return {(0, 0): _route(points, 'branch', (0., 1.), (0., 1.))}
        if key in ('diagonal_north_half', 'diagonal_east_half'):
            points = [(*info['start'], HEIGHT), (*info['end'], HEIGHT)]
            return {(0, 0): _route(points, 'branch', (1., 1.), (1., 1.))}
        require(key == 'diagonal', 'Linear recipe has no implemented geometry')
        return {(0, 0): _route([(0., -8., HEIGHT), (8., 0., HEIGHT)],
                                'branch', (1., 1.), (1., 1.)),
                (0, 1): _route([(-8., 0., HEIGHT), (0., 8., HEIGHT)],
                                'branch', (1., 1.), (1., 1.))}
    control = info['control']
    cuts = [0., 1.]
    width, depth = info['footprint']
    for axis, boundaries in ((0, [16*x - 8. for x in range(width + 1)]),
                             (1, [8. - 16*y for y in range(depth + 1)])):
        for boundary in boundaries:
            value = _root(control, axis, boundary)
            if value is not None:
                cuts.append(value)
    cuts.sort()
    unique = [cuts[0]]
    for value in cuts[1:]:
        if value - unique[-1] > 1e-10:
            unique.append(value)
    result = {}
    for a, b in zip(unique, unique[1:]):
        x, y = _bezier(control, (a + b) / 2.)
        cell = (math.floor((x + 8.) / 16.), math.floor((8. - y) / 16.))
        require(cell in info['cells'], f'Curve occupies undeclared cell: {cell}')
        require(cell not in result, 'Curve re-enters a cell; unsupported shape')
        cx, cy = 16.*cell[0], -16.*cell[1]
        points = []
        for n in range(17):
            px, py = _bezier(control, a + (b - a) * n / 16.)
            points.append((_snap(px - cx), _snap(py - cy), HEIGHT))
        result[cell] = _route(points, 'branch', _tangent(control, a), _tangent(control, b))
    require(set(result) == set(info['cells']), 'Curve does not fill every declared cell')
    return result


def single_track_layout(shape):
    """Return the local tile routes and endpoint tangents for a modular shape."""
    require(shape in _SHAPES, f'Unknown single-track shape: {shape}')
    segments = _branch_segments(shape, _SHAPES[shape])
    return {cell: {'routes': [branch], 'branch': branch['points'], 'mainline': False,
                   'tangent_in': branch['tangent_in'], 'tangent_out': branch['tangent_out']}
            for cell, branch in segments.items()}


def _flag(edge, tangent):
    dx, dy = tangent
    if abs(dx) < 1e-8 or abs(dy) < 1e-8:
        return 2
    positive = dx * dy > 0.
    return (3 if positive else 1) if edge in (1, 3) else (1 if positive else 3)


def _construction_flags(routes):
    sides = [0, 0, 0, 0]
    for route in routes:
        for edge, tangent in ((route['entry'], route['tangent_in']),
                              (route['exit'], route['tangent_out'])):
            value = _flag(edge, tangent)
            # Native same-network AAC1 uses the straight category where its
            # diagonal and straight paths share an edge at different offsets.
            sides[edge] = 2 if value == 2 or sides[edge] == 2 else value
    return sides[3] << 24 | sides[2] << 16 | sides[1] << 8 | sides[0]


