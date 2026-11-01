"""The complementary city-grid phase of the accepted parallel diamond.

Only the authored physical layout moves by eight metres on each world axis.
The native highway remains on its original directed diagonal. Texture station
zero follows the physical layout; the flat endpoint collars belong only to
the separately sliced traffic alignment.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import math

from . import ramp_geometry as geometry
from . import ramp_paths as paths
from .parallel_geometry import procedural_geometry as alignment_a_geometry

TRANSLATION_EN_M = (8.0, 8.0)
AVENUE_PHASE_OFFSET = 1


def _point(point):
    return [point[0] + 8.0, point[1] + 8.0, *point[2:]]


def _translate_route(route):
    result = deepcopy(route)
    for field in ('points', 'mesh_points', 'shoulder_points'):
        if field in result:
            result[field] = [_point(point) for point in result[field]]
    for field in ('native_high_port', 'avenue_port'):
        result[field] = _point(result[field])
    result['points_uvh'] = [[*geometry.highway_coordinates(point), point[2]]
                            for point in result['points']]
    result['approach']['point_enh'] = _point(result['approach']['point_enh'])
    for support in result['supports']:
        support['centre_enh'] = _point(support['centre_enh'])
        support['footprint_en'] = [[p[0] + 8.0, p[1] + 8.0]
                                   for p in support['footprint_en']]
    result['ribbon_outlines_en'] = [[[p[0] + 8.0, p[1] + 8.0] for p in outline]
                                    for outline in result['ribbon_outlines_en']]
    for field in ('profile', 'physical_profile'):
        if field in result:
            result[field]['departure_station_u_m'] += 8.0 * math.sqrt(2.0)
    result['path_cells'] = [list(cell) for cell in sorted(
        {cell for cell, _ in paths.polyline_fragments(result['points'])},
        key=lambda cell: (cell[1], cell[0]))]
    from .parallel_ramp_review import _projection_cells
    result['model_cells'] = _projection_cells(result.get('mesh_points', result['points']),
                                              side=result['side'])
    result['grid_alignment'] = 'B'
    return result


@lru_cache(maxsize=1)
def _physical():
    routes, models = alignment_a_geometry()
    translated = {key: [tuple((p[0] + 8.0, p[1], p[2] - 8.0, *p[3:])
                              for p in triangle) for triangle in faces]
                  for key, faces in models.items()}
    return [_translate_route(route) for route in routes], translated


def physical_routes():
    """Return the rigidly moved ramp/marking routes with their original cuts."""
    return deepcopy(_physical()[0])


def procedural_geometry():
    """Return complete physical models, retaining the accepted functional cuts."""
    return deepcopy(_physical())


def _collar(point, neighbour):
    """Extend away from neighbour to the first strictly outward city side."""
    tangent = [point[axis] - neighbour[axis] for axis in (0, 1)]
    length = math.hypot(*tangent)
    if length <= 1e-12 or abs(point[2] - neighbour[2]) > 1e-8:
        raise ValueError('An Alignment B native collar must extend a flat, nonzero tangent')
    tangent = [value / length for value in tangent]
    candidates = []
    for axis, direction in enumerate(tangent):
        if abs(direction) < 1e-12:
            continue
        tile = math.floor((point[axis] + 8.0) / 16.0)
        for index in range(tile - 2, tile + 3):
            boundary = 16.0 * index - 8.0
            distance = (boundary - point[axis]) / direction
            if distance > 1e-7:
                candidates.append((distance, axis, boundary))
    distance, axis, boundary = min(candidates)
    output = [point[0] + distance * tangent[0], point[1] + distance * tangent[1], point[2]]
    output[axis] = boundary
    # Exact native lane offsets survive cancellation of the tiny source collar.
    # Nine decimal metres is also the owning canonical PATH encoding precision.
    return [round(value, 9) for value in output]


@lru_cache(maxsize=1)
def _traffic():
    result = physical_routes()
    for route in result:
        original = route['points']
        first, last = _collar(*original[:2]), _collar(original[-1], original[-2])
        route['points'] = [first, *original, last]
        for segment in route['segments']:
            segment['start_index'] += 1
            segment['end_index'] += 1
        route['points_uvh'] = [[*geometry.highway_coordinates(point), point[2]]
                                for point in route['points']]
        route['native_high_port'] = list(first if route['direction'] == 'off' else last)
        route['avenue_port'] = list(last if route['direction'] == 'off' else first)
        route['path_cells'] = [list(cell) for cell in sorted(
            {cell for cell, _ in paths.polyline_fragments(route['points'])},
            key=lambda cell: (cell[1], cell[0]))]
        route['native_endpoint_collars'] = {
            'policy': 'Nearest strictly outward city edge on each retained flat native lane',
            'original_first_enh': list(original[0]), 'original_last_enh': list(original[-1]),
            'first_extension_m': math.dist(first[:2], original[0][:2]),
            'last_extension_m': math.dist(last[:2], original[-1][:2]),
            'physical_models_and_texture_stations_unchanged': True}
    return result


def traffic_routes():
    """Return native-edge-complete transfers for actual whole-cell PATH slicing."""
    return deepcopy(_traffic())


def required_traffic_cells():
    """Fill both native strips only between the actual ramp endpoint owners."""
    cells = {cell for route in _traffic() for cell, _ in paths.polyline_fragments(route['points'])}
    highway = [cell for cell in cells if sum(cell) in (0, 1)]
    avenue = [cell for cell in cells if cell[0] - cell[1] in (0, 1, 2)]
    low, high = min(c[0] - c[1] for c in highway), max(c[0] - c[1] for c in highway)
    near, far = min(sum(c) for c in avenue), max(sum(c) for c in avenue)
    for column in range(min(c[0] for c in cells), max(c[0] for c in cells) + 1):
        for row in range(min(c[1] for c in cells), max(c[1] for c in cells) + 1):
            if ((column + row in (0, 1) and low <= column - row <= high)
                    or (column - row in (0, 1, 2) and near <= column + row <= far)):
                cells.add((column, row))
    return cells
