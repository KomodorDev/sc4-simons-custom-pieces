"""Source-only close, parallel DD RHW ramp candidates.

This module deliberately does not register types, allocate resources, or alter
the accepted assembly.  Its sampled proposals reauthor the high departure,
hold its full width at deck height, descend beside the highway, and reach the
perpendicular Avenue on a straight approach before a finite right turn.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import math

from . import ramp_geometry as geometry
from . import ramp_paths as paths

ROOT_TWO = math.sqrt(2.0)
RAMP_WIDTH_M = 6.0
MAX_GRADE = 0.30
AVENUE_OUTER_CAR_U = 11.2 / ROOT_TWO
NATIVE_HIGH_PORTS = {'lower': (56.0, 51.2, 7.5),
                     'upper': (-72.0, -83.2, 15.0)}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _cells(values):
    return [list(cell) for cell in sorted(set(map(tuple, values)), key=lambda c: (c[1], c[0]))]


def _bounds(cells):
    west, east = min(c[0] for c in cells), max(c[0] for c in cells)
    north, south = min(c[1] for c in cells), max(c[1] for c in cells)
    return {'minimum_cell': [west, north], 'maximum_cell': [east, south],
            'tiles': [east - west + 1, south - north + 1],
            'metres': [16.0 * (east - west + 1), 16.0 * (south - north + 1)]}


def _smooth(t):
    return t ** 3 * (10.0 + t * (-15.0 + 6.0 * t))


def _line(first, last, step=0.20):
    count = max(1, math.ceil(math.dist(first[:2], last[:2]) / step))
    return [tuple(a + (b - a) * index / count for a, b in zip(first, last))
            for index in range(count + 1)]


def _radius(points):
    radii = []
    for a, b, c in zip(points, points[1:], points[2:]):
        cross = abs((b[0] - a[0]) * (c[1] - a[1])
                    - (b[1] - a[1]) * (c[0] - a[0]))
        if cross > 1e-11:
            radii.append(math.dist(a[:2], b[:2]) * math.dist(b[:2], c[:2])
                         * math.dist(a[:2], c[:2]) / (2.0 * cross))
    return min(radii) if radii else None


def _grade(points):
    return max(abs(b[2] - a[2]) / math.dist(a[:2], b[:2])
               for a, b in zip(points, points[1:]))


def _vertical(points, start_height, taper=2.0, flat_end=1.0):
    lengths, _normals = geometry.route_frames(points)
    graded = lengths[-1] - flat_end
    _require(graded > 2.0 * taper, 'Parallel descent has no constant-grade middle')
    middle = start_height / (graded - taper)
    _require(middle <= MAX_GRADE, 'Parallel descent exceeds its 30% source bound')

    def height(distance):
        if distance >= graded:
            return 0.0
        if distance < taper:
            return start_height - middle * distance * distance / (2.0 * taper)
        if distance <= graded - taper:
            return start_height - middle * (distance - taper / 2.0)
        return middle * (graded - distance) ** 2 / (2.0 * taper)

    result = [(*point[:2], height(distance)) for point, distance in zip(points, lengths)]
    return result, {'reference': 'Physical profile measured outward from the highway, independent of traffic direction',
                    'length_plan_m': lengths[-1], 'graded_length_m': graded,
                    'grade_taper_m': taper, 'flat_end_m': flat_end,
                    'constant_grade_percent': middle * 100.0,
                    'maximum_sampled_grade_percent': _grade(result) * 100.0,
                    'high_height_m': start_height, 'ground_height_m': 0.0}


def _ribbon(points, half_width=3.0, *, side):
    _lengths, normals = geometry.route_frames(points)
    left = [(p[0] + half_width * n[0], p[1] + half_width * n[1])
            for p, n in zip(points, normals)]
    right = [(p[0] - half_width * n[0], p[1] - half_width * n[1])
             for p, n in zip(points, normals)]
    polygon = left + list(reversed(right))
    # The native highway owns every road face inside its straight eight-metre
    # half-width. A separate ramp starts physically at that actual deck edge.
    clipped = geometry._clip(polygon, lambda p: side * geometry.highway_coordinates(p)[1] - 8.0)
    return clipped + [clipped[0]]


def _projection_cells(points, *, side):
    # The actual indexed ribbon sweep includes the miter at every sample.
    # Barrier and underside footprints stay within this same six-metre sweep.
    _lengths, normals = geometry.route_frames(points)
    faces = geometry._ribbon(points, normals, -3.0, 3.0, 'asphalt')
    faces = geometry.outside_highway_corridor(faces, side)
    return _cells(geometry.partition_triangles(faces))


def _support(parallel_points):
    """One explicit 0.8 m square pier, wholly below the parallel road."""
    lengths, _normals = geometry.route_frames(parallel_points)
    at = lengths[-1] * 0.46
    index = next(i for i, distance in enumerate(lengths) if distance >= at)
    a, b = parallel_points[index - 1:index + 1]
    t = (at - lengths[index - 1]) / (lengths[index] - lengths[index - 1])
    centre = tuple(x + (y - x) * t for x, y in zip(a, b))
    grade = (b[2] - a[2]) / math.dist(a[:2], b[:2])
    run = math.dist(a[:2], b[:2])
    tangent = ((b[0] - a[0]) / run, (b[1] - a[1]) / run)
    footprint = [(centre[0] + dx, centre[1] + dy)
                 for dx, dy in ((-.4, -.4), (.4, -.4), (.4, .4), (-.4, .4))]
    tops = [centre[2] - 1.0 + grade * ((p[0] - centre[0]) * tangent[0]
                                     + (p[1] - centre[1]) * tangent[1]) for p in footprint]
    _require(min(tops) > 0.0, 'A proposed ramp pier misses the real underside')
    return {'centre_enh': list(centre), 'half_width_m': .4,
            'footprint_en': [list(p) for p in footprint],
            'top_corner_heights_m': tops, 'bottom_height_m': 0.0,
            'status': 'Source-designed sloping support; not compiled or load-checked'}


def _off(deck, *, offset, departure, radius, inward_upper):
    side = 1 if deck == 'lower' else -1
    direction = -side
    high = NATIVE_HIGH_PORTS[deck]
    if deck == 'upper' and inward_upper:
        high = (high[0] + 16.0, high[1] + 16.0, high[2])
    u0, v0 = geometry.highway_coordinates(high)
    collar = .01
    collar_end = (u0 + direction * collar, v0, high[2])
    start = [(u0, v0, high[2]), collar_end]
    count = max(80, math.ceil(departure / .10))
    for index in range(1, count + 1):
        t = index / count
        start.append((collar_end[0] + direction * departure * t,
                      v0 + (side * offset - v0) * _smooth(t), high[2]))
    approach_u = side * (AVENUE_OUTER_CAR_U + radius)
    approach = (approach_u, side * offset, 0.0)
    parallel_plan = _line(start[-1], (*approach[:2], high[2]))
    parallel, profile = _vertical(parallel_plan, high[2])
    start_index = len(start) - 1
    points_uvh = start + parallel[1:]
    approach_index = len(points_uvh) - 1
    # A clockwise right turn in the oriented u/v plane, for either side.
    arc = []
    count = max(48, math.ceil(radius * math.pi / 2.0 / .10))
    for index in range(1, count + 1):
        angle = index / count * math.pi / 2.0
        arc.append((side * (AVENUE_OUTER_CAR_U + radius * (1.0 - math.sin(angle))),
                    side * (offset + radius * (1.0 - math.cos(angle))), 0.0))
    points_uvh += arc
    turn_end = len(points_uvh) - 1
    port_v = paths._avenue_boundary(side * AVENUE_OUTER_CAR_U,
                                   side * (offset + radius), side, beyond=True)
    points_uvh += _line(points_uvh[-1], (side * AVENUE_OUTER_CAR_U, port_v, 0.0))[1:]
    points = [geometry.world_coordinates(u, v, h) for u, v, h in points_uvh]
    # Preserve the actual native decimal endpoint, not an equivalent float.
    points[0] = high
    departure_points = points[:start_index + 1]
    parallel_points = points[start_index:approach_index + 1]
    _lengths, normals = geometry.route_frames(points)
    # Full mitered edge is checked from the first wholly parallel section.
    edge_vs = []
    for p, n in zip(points[start_index:approach_index + 1], normals[start_index:approach_index + 1]):
        edge_vs.extend(side * geometry.highway_coordinates((p[0] + sign * 3.0 * n[0],
                                                            p[1] + sign * 3.0 * n[1]))[1]
                       for sign in (-1, 1))
    profile.update({'departure_station_u_m': u0, 'departure_plan_run_u_m': departure,
                    'departure_length_plan_m': geometry.route_frames(departure_points)[0][-1],
                    'departure_minimum_sampled_radius_m': _radius(departure_points),
                    'turn_radius_m': radius, 'parallel_offset_m': offset,
                    'full_width_parallel_inner_v_m': min(edge_vs),
                    'minimum_parallel_gap_to_native_deck_m': min(edge_vs) - 8.0,
                    'high_throat_remains_at_deck_height': True,
                    'maximum_route_grade_percent': _grade(points) * 100.0,
                    'length_total_plan_m': geometry.route_frames(points)[0][-1]})
    return {'id': deck + '-off', 'deck': deck, 'direction': 'off', 'side': side,
            'transport': 1, 'lane': 1, 'width_m': 6.0, 'height_m': high[2],
            'points': [list(p) for p in points],
            'points_uvh': [list(p) for p in points_uvh],
            'segments': [{'kind': 'flat-native-direction-collar', 'start_index': 0, 'end_index': 1},
                         {'kind': 'flat-high-departure', 'start_index': 1, 'end_index': start_index},
                         {'kind': 'straight-parallel-descent', 'start_index': start_index,
                          'end_index': approach_index},
                         {'kind': 'ground-right-quarter-turn', 'start_index': approach_index,
                          'end_index': turn_end},
                         {'kind': 'native-avenue-lane-collar', 'start_index': turn_end,
                          'end_index': len(points) - 1}],
            'native_high_port': list(high), 'avenue_port': list(points[-1]),
            'approach': {'point_enh': list(points[approach_index]),
                         'unit_tangent_en': [direction / ROOT_TWO, direction / ROOT_TWO],
                         'angle_to_avenue_degrees': 90.0,
                         'description': 'Straight ramp reaches a separate right-turn ground terminal'},
            'profile': profile,
            'path_cells': _cells(cell for cell, _part in paths.polyline_fragments(points)),
            'model_cells': _projection_cells(points, side=side),
            'ribbon_outlines_en': [[list(p) for p in _ribbon(points, side=side)]],
            'supports': [_support(parallel_points)],
            'status': 'New source geometry; original slip paint, seam, and barriers need reauthoring'}


def _entry(off):
    result = deepcopy(off)
    result['id'] = off['deck'] + '-on'
    result['direction'] = 'on'
    # Reflect u -> -u while retaining v, then reverse the travel sequence.
    reflect = lambda p: [-p[1], -p[0], *p[2:]]
    result['points'] = [reflect(p) for p in reversed(off['points'])]
    result['points_uvh'] = [[-u, v, h] for u, v, h in reversed(off['points_uvh'])]
    last = len(off['points']) - 1
    result['segments'] = [{**segment, 'start_index': last - segment['end_index'],
                           'end_index': last - segment['start_index']}
                          for segment in reversed(off['segments'])]
    result['native_high_port'] = reflect(off['native_high_port'])
    result['avenue_port'] = reflect(off['avenue_port'])
    result['profile']['departure_station_u_m'] *= -1.0
    result['path_cells'] = _cells(cell for cell, _part in paths.polyline_fragments(result['points']))
    result['model_cells'] = _projection_cells(result['points'], side=result['side'])
    result['ribbon_outlines_en'] = [[list(p) for p in _ribbon(result['points'], side=result['side'])]]
    result['approach']['point_enh'] = reflect(off['approach']['point_enh'])
    result['approach']['unit_tangent_en'] = [
        off['approach']['unit_tangent_en'][1], off['approach']['unit_tangent_en'][0]]
    result['approach']['description'] = 'Entry traffic leaves separate right-turn terminal on straight ramp'
    for support in result['supports']:
        support['centre_enh'] = reflect(support['centre_enh'])
        support['footprint_en'] = [reflect(p) for p in support['footprint_en']]
    return result


def _avenue_cells(routes):
    """Native Avenue checkerboard cells through both nearest ground collars.

    Both measured car carriageways establish the crossed city cells. This
    is a proposed service-cell union, not a new native-model extraction.
    """
    all_points = [p for route in routes for p in route['points']
                  if abs(p[2]) < 1e-9]
    extent = max(abs(geometry.highway_coordinates(p)[1]) for p in all_points)
    cells = set()
    for u in (-11.2 / ROOT_TWO, -4.8 / ROOT_TWO, 4.8 / ROOT_TWO, 11.2 / ROOT_TWO):
        points = [geometry.world_coordinates(u, -extent), geometry.world_coordinates(u, extent)]
        cells.update(cell for cell, _part in paths.polyline_fragments(points))
    return _cells(cells), extent


def _candidate(identifier, *, offset, departure, radius, inward_upper):
    from .straight_stamp_geometry import stamp_cells
    ramps = []
    for deck in ('lower', 'upper'):
        off = _off(deck, offset=offset, departure=departure, radius=radius,
                   inward_upper=inward_upper)
        ramps.extend((off, _entry(off)))
    stamp = set(stamp_cells())
    if inward_upper:
        stamp -= {(-4, 4), (-4, 5), (4, -4), (5, -4)}
    avenue, extent = _avenue_cells(ramps)
    traffic = stamp | set(map(tuple, avenue))
    model = set()
    for ramp in ramps:
        traffic.update(map(tuple, ramp['path_cells']))
        model.update(map(tuple, ramp['model_cells']))
    owned = traffic | model
    # Projected ribbon cells include the invisible half inside the mainline:
    # stamp ownership takes precedence there. No native shape is overwritten.
    return {'id': identifier, 'routes': ramps, 'stamp_cells': _cells(stamp),
            'avenue_cells': avenue, 'avenue_extent_v_m': extent,
            'path_and_native_cells': _cells(traffic), 'model_projection_cells': _cells(model),
            'owned_cells': _cells(owned), 'bounds': _bounds(owned),
            'ownership_status': 'Conservative service/ribbon union; separate piece owners are not allocated',
            'ramp_model_over_native_cells': _cells(model & stamp),
            'model_only_cells': _cells(owned - traffic),
            'parallel_offset_m': offset, 'parallel_nominal_gap_m': offset - 11.0,
            'ground_turn_radius_m': radius, 'high_departure_run_m': departure,
            'changed_native_high_sockets': ['upper-off', 'upper-on'] if inward_upper else [],
            'upper_socket_shift_along_highway_m': 16.0 * ROOT_TWO if inward_upper else 0.0,
            'constraints': [
                'All four transfers use only the adjacent Avenue carriageway; no transfer crosses the Avenue centre.',
                'Each ramp stays at full deck height until its complete six-metre width is outside the native deck.',
                'Both approaches are diagonal and perpendicular to the Avenue; actual vehicle turns use finite quarter-circles.',
                'The 30% bound is experimental game geometry, not a real-world highway standard.',
                'R6/R8 terminals and short high departures are new custom geometry, not measured NAM ramps.',
                'Native slip-lane paint, high-edge barrier seams, and whole-tile traffic ownership require coordinated reauthoring.',
                'Adaptive sidewalks must be retained in the eventual Avenue/crossing owners.',
                'Support shells are explicit source footprints; structural capacity and native encoded meshes are unverified.',
                'The conservative union reserves every swept-ribbon cell; model overhang may reduce construction ownership after review.',
                'No resource allocation, compiled-game build, installation, or human game observation is supplied by this review.']}


@lru_cache(maxsize=1)
def _review():
    from . import modular_ramps
    from .straight_stamp_geometry import stamp_cells
    catalog = modular_ramps.module_catalog()
    compact_junctions = {cell for key in ('northwest-junction', 'southeast-junction')
                         for cell in paths.MODULES[key][1]}
    r40 = set(map(tuple, catalog['occupied_cells'])) | stamp_cells()
    compact = set(map(tuple, catalog['compact_occupied_cells'])) | compact_junctions | stamp_cells()
    return {'schema_version': 1, 'status': 'Source-only geometric proposal',
            'axes': {'u': 'Highway axis, northeast positive',
                     'v': 'Perpendicular Avenue axis, northwest positive',
                     'world': 'East, north, and pavement height in metres',
                     'cells': 'City columns east and rows south; centre=(16c,-16r)'},
            'baselines': {'r40': {'occupied_cells': _cells(r40), 'cell_count': len(r40), 'bounds': _bounds(r40)},
                          'compact': {'occupied_cells': _cells(compact), 'cell_count': len(compact),
                                      'bounds': _bounds(compact)}},
            'candidates': [
                _candidate('parallel-retained-ports', offset=13.0, departure=28.0,
                           radius=8.0, inward_upper=False),
                _candidate('parallel-inward-upper', offset=12.0, departure=17.0,
                           radius=6.0, inward_upper=True)]}


def review():
    """Return independent mutable, JSON-serializable measured source candidates."""
    return deepcopy(_review())
