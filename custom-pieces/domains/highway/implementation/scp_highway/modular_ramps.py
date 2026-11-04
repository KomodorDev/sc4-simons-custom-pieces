"""Independently placed full ramps for the straight DD slip-lane stamp.

Each ramp includes its complete curved high throat, including model-only
overhang above highway-owned cells. R40 grades end at flat orthogonal tile
edges; compact full ramps retain the original grades. Neither family owns
highway cells, and their downstream terminals remain separately placed.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import math

from . import ramp_geometry as geometry
from . import ramp_paths as paths

RECIPE_PREFIX = 'highway_ddrhw_modular_'
RADIUS_M = 40.0
RETAINED_COLLAR_M = 2.0
GRADE_TRANSITION_M = 8.0
FLAT_END_M = 1.0
MAX_STEP_M = 0.25
MAX_GRADE = 0.30
ROOT_TWO = math.sqrt(2.0)

MODULES = {
    'lower-exit-r40': ('Lower Exit Ramp — R40', ((0, -2), (1, -3), (1, -2), (2, -3))),
    'lower-entry-r40': ('Lower Entry Ramp — R40', ((-3, 1), (-2, 0), (-2, 1), (-3, 2))),
    'upper-exit-r40': ('Upper Exit Ramp — R40', ((-1, 3), (-1, 4), (0, 3), (1, 3), (-2, 4), (-3, 5))),
    'upper-entry-r40': ('Upper Entry Ramp — R40', ((3, -1), (4, -1), (3, 0), (3, 1), (4, -2), (5, -3))),
    'northwest-terminal-r40': ('Northwest Avenue Ramp Terminal — R40', (
        (-3, -3), (-3, -2), (-3, -1), (-2, -3), (-2, -2), (-2, -1), (-1, -3), (-1, -2), (-1, -1))),
    'southeast-terminal-r40': ('Southeast Avenue Ramp Terminal — R40', (
        (1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4))),
    'lower-exit-compact': ('Lower Exit Ramp — Compact', ((1, -3), (1, -2), (2, -3))),
    'lower-entry-compact': ('Lower Entry Ramp — Compact', ((-3, 1), (-2, 1), (-3, 2))),
    'upper-exit-compact': ('Upper Exit Ramp — Compact', ((0, 2), (-1, 3), (0, 3), (-1, 4), (-2, 4), (-3, 5))),
    'upper-entry-compact': ('Upper Entry Ramp — Compact', ((4, -1), (3, -1), (2, 0), (3, 0), (4, -2), (5, -3))),
}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def stamp_cells():
    from .straight_stamp_geometry import stamp_cells as retained
    return retained()


def _lengths(points):
    result = [0.0]
    for first, last in zip(points, points[1:]):
        distance = math.dist(first[:2], last[:2])
        _require(distance > 1e-10, 'A modular ramp contains a stationary planar segment')
        result.append(result[-1] + distance)
    return result


def _line(first, direction, length):
    _require(length >= -1e-8, 'The selected standard anchors need a negative straight section')
    if length <= 1e-8:
        return [tuple(first)]
    count = max(1, math.ceil(length / MAX_STEP_M))
    return [(first[0] + direction[0] * length * index / count,
             first[1] + direction[1] * length * index / count, first[2])
            for index in range(count + 1)]


def _clockwise_arc(first, heading_start, heading_end):
    _require(heading_end < heading_start, 'An R40 turn must have a clockwise angular interval')
    count = max(2, math.ceil((heading_start - heading_end) * RADIUS_M / MAX_STEP_M))
    centre = (first[0] + RADIUS_M * math.sin(heading_start),
              first[1] - RADIUS_M * math.cos(heading_start))
    result = [tuple(first)]
    for index in range(1, count + 1):
        angle = heading_start + (heading_end - heading_start) * index / count
        result.append((centre[0] - RADIUS_M * math.sin(angle),
                       centre[1] + RADIUS_M * math.cos(angle), first[2]))
    return result


def _retained_prefix(ramp):
    """Retain original samples, rather than inserting a different mesh miter."""
    original = ramp['mesh_points']
    boundary_x = 24.0 if ramp['deck'] == 'lower' else -24.0
    crossing = next(index for index, (a, b) in enumerate(zip(original, original[1:]))
                    if min(a[0], b[0]) <= boundary_x <= max(a[0], b[0]))
    first, last = original[crossing:crossing + 2]
    fraction = (boundary_x - first[0]) / (last[0] - first[0])
    boundary = tuple(first[axis] + fraction * (last[axis] - first[axis]) for axis in range(3))
    index = crossing + 1
    retained = math.dist(boundary[:2], original[index][:2])
    while retained < RETAINED_COLLAR_M:
        retained += math.dist(original[index][:2], original[index + 1][:2])
        index += 1
    prefix = original[:index + 1]
    tangent = tuple(prefix[-1][axis] - prefix[-2][axis] for axis in range(3))
    length = math.hypot(*tangent[:2])
    return prefix, boundary, retained, tuple(value / length for value in tangent)


def _vertical_profile(points, start_height, entry_grade):
    """Solve exact height with two linear grade changes and a flat end collar."""
    distances = _lengths(points)
    graded_length = distances[-1] - FLAT_END_M
    taper = GRADE_TRANSITION_M
    _require(graded_length > 2.0 * taper, 'An R40 grade has no constant-grade middle')
    middle_grade = (-start_height - taper * entry_grade / 2.0) / (graded_length - taper)
    _require(max(abs(entry_grade), abs(middle_grade)) <= MAX_GRADE + 1e-10,
             'The fixed R40 anchors exceed the 30% experimental grade bound')

    def height(distance):
        if distance >= graded_length:
            return 0.0
        if distance <= taper:
            value = start_height + entry_grade * distance
            value += (middle_grade - entry_grade) * distance * distance / (2.0 * taper)
        elif distance <= graded_length - taper:
            value = start_height + (entry_grade + middle_grade) * taper / 2.0
            value += middle_grade * (distance - taper)
        else:
            # Integrate backwards from the exact zero-height landing.
            remaining = graded_length - distance
            value = -middle_grade * remaining * remaining / (2.0 * taper)
        _require(value >= -1e-8, 'The R40 vertical profile crossed below ground')
        return max(0.0, value)

    result = [(point[0], point[1], height(distance)) for point, distance in zip(points, distances)]
    result[0] = (*result[0][:2], start_height)
    result[-1] = (*result[-1][:2], 0.0)
    return result, {'length_plan_m': distances[-1], 'graded_length_m': graded_length,
                    'entry_travel_grade': entry_grade, 'middle_travel_grade': middle_grade,
                    'exit_travel_grade': 0.0, 'grade_transition_m': taper,
                    'flat_end_m': FLAT_END_M,
                    'maximum_grade_percent': 100.0 * max(abs(entry_grade), abs(middle_grade))}


def _off_variant(source):
    mesh_prefix, boundary, retained, tangent = _retained_prefix(source)
    start = mesh_prefix[-1]
    heading = math.atan2(tangent[1], tangent[0])
    lower = source['deck'] == 'lower'
    if lower and heading < 0.0:
        heading += 2.0 * math.pi
    end_heading = math.pi if lower else 0.0
    end_east = -8.0 if lower else 24.0
    sign = 1.0 if lower else -1.0
    end_u = sign * (11.2 / ROOT_TWO + RADIUS_M * (1.0 - 1.0 / ROOT_TWO))
    end_north = ROOT_TWO * end_u - end_east
    arc_delta = (RADIUS_M * (math.sin(heading) - math.sin(end_heading)),
                 RADIUS_M * (math.cos(end_heading) - math.cos(heading)))
    first_straight = (end_north - start[1] - arc_delta[1]) / tangent[1]
    final_direction = -1.0 if lower else 1.0
    last_straight = (end_east - start[0] - arc_delta[0] - tangent[0] * first_straight) / final_direction
    plan = _line(start, tangent[:2], first_straight)
    arc_start = plan[-1]
    arc_centre = (arc_start[0] + RADIUS_M * math.sin(heading),
                  arc_start[1] - RADIUS_M * math.cos(heading))
    plan += _clockwise_arc(plan[-1], heading, end_heading)[1:]
    arc_end = plan[-1]
    plan += _line(plan[-1], (final_direction, 0.0), last_straight)[1:]
    plan[-1] = (end_east, end_north, start[2])
    continuation, vertical = _vertical_profile(plan, start[2], tangent[2])
    ground_turn = _clockwise_arc(continuation[-1], end_heading, end_heading - math.pi / 4.0)
    mouth_u, mouth_v = geometry.highway_coordinates(ground_turn[-1])
    _require(abs(mouth_u - sign * 11.2 / ROOT_TWO) < 1e-10,
             'The R40 ground turn missed the adjacent outer Avenue lane')
    port_v = paths._avenue_boundary(mouth_u, mouth_v, int(sign), beyond=True)
    port = geometry.world_coordinates(mouth_u, port_v)
    delta = tuple(port[axis] - ground_turn[-1][axis] for axis in (0, 1))
    port_length = math.hypot(*delta)
    ground_turn += _line(ground_turn[-1], tuple(value / port_length for value in delta), port_length)[1:]
    ground_turn[-1] = tuple(port)
    tail = continuation[1:] + ground_turn[1:]
    source_path_index = next(index for index, point in enumerate(source['points'])
                             if math.dist(point, start) < 1e-12)
    result = deepcopy(source)
    result['points'] = source['points'][:source_path_index + 1] + tail
    result['mesh_points'] = mesh_prefix + tail
    result['ground_points'] = ground_turn
    result['avenue_port'] = tuple(port)
    result['standard_ground_port'] = continuation[-1]
    result['length_plan_m'] = _lengths(result['points'])[-1]
    result['legacy_controls'] = result.pop('controls')
    result['grade_max_percent'] = vertical['maximum_grade_percent']
    result['modular_profile'] = {
        **vertical, 'minimum_new_curve_radius_m': RADIUS_M,
        'retained_boundary_m': boundary, 'retained_high_collar_m': retained,
        'retained_collar_end_m': tuple(start), 'retained_collar_end_tangent': tangent,
        'new_arc_centre_EN_m': arc_centre, 'new_arc_start_EN_m': arc_start[:2],
        'new_arc_end_EN_m': arc_end[:2],
        'new_arc_start_heading_radians_E_counterclockwise': heading,
        'new_arc_end_heading_radians_E_counterclockwise': end_heading,
        'new_arc_reference_turn': 'clockwise outward from the highway',
        'first_straight_m': first_straight, 'last_straight_m': last_straight,
        'ground_curve_turn_degrees': 45.0,
        'grade_length_with_retained_collar_m': retained + vertical['length_plan_m'],
    }
    return result


def _opposite_entry(off, source):
    """Reflect the physical side and reverse flow, preserving right-hand traffic."""
    result = deepcopy(source)
    for key in ('points', 'mesh_points', 'ground_points'):
        result[key] = [(-north, -east, height) for east, north, height in reversed(off[key])]
    # Independently generated on/off native samples have harmless floating
    # asymmetries. Preserve the actual retained on-ramp bytes at its high end,
    # rather than replacing them with the mathematically reflected off end.
    collar = _retained_prefix(off)[0][-1]
    reflected_collar = (-collar[1], -collar[0], collar[2])
    for key in ('points', 'mesh_points'):
        new_index = next(index for index, point in enumerate(result[key])
                         if math.dist(point, reflected_collar) < 1e-10)
        old_index = next(index for index, point in enumerate(source[key])
                         if math.dist(point, reflected_collar) < 1e-10)
        result[key] = result[key][:new_index] + deepcopy(source[key][old_index:])
    for key in ('avenue_port', 'standard_ground_port'):
        east, north, height = off[key]
        result[key] = (-north, -east, height)
    result['length_plan_m'] = off['length_plan_m']
    result['legacy_controls'] = result.pop('controls')
    result['grade_max_percent'] = off['grade_max_percent']
    result['modular_profile'] = deepcopy(off['modular_profile'])
    east, north, height = result['modular_profile']['retained_boundary_m']
    result['modular_profile']['retained_boundary_m'] = (-north, -east, height)
    result['modular_profile']['entry_travel_grade'] = 0.0
    result['modular_profile']['exit_travel_grade'] = -off['modular_profile']['entry_travel_grade']
    result['modular_profile']['middle_travel_grade'] *= -1.0
    for key in ('retained_collar_end_m', 'new_arc_centre_EN_m',
                'new_arc_start_EN_m', 'new_arc_end_EN_m'):
        point = result['modular_profile'][key]
        result['modular_profile'][key] = (-point[1], -point[0], *point[2:])
    east, north, grade = result['modular_profile']['retained_collar_end_tangent']
    result['modular_profile']['retained_collar_end_tangent'] = (-north, -east, grade)
    for key in ('new_arc_start_heading_radians_E_counterclockwise',
                'new_arc_end_heading_radians_E_counterclockwise'):
        result['modular_profile'][key] = (-math.pi / 2.0 - result['modular_profile'][key]) % (2.0 * math.pi)
    result['modular_profile']['new_arc_reference_turn'] = 'counterclockwise outward from the highway'
    result['modular_profile']['planar_reference_direction'] = 'Outward from the highway; traffic reverses this reference for an entrance.'
    return result


@lru_cache(maxsize=1)
def _variant_ramps():
    originals = {row['id']: row for row in geometry.compact_ramps()}
    result = []
    for deck in ('lower', 'upper'):
        off = _off_variant(originals[deck + '-off'])
        result.extend((off, _opposite_entry(off, originals[deck + '-on'])))
    return result


def variant_ramps():
    """Return four fresh complete highway-to-Avenue route/mesh sources."""
    return deepcopy(_variant_ramps())


def access_routes():
    result = []
    for ramp in _variant_ramps():
        arm = 'NW' if ramp['deck'] == 'lower' else 'SE'
        name = (f'{ramp["deck"]}-highway->{arm}' if ramp['direction'] == 'off'
                else f'{arm}->{ramp["deck"]}-highway')
        result.append({'id': name, 'ramp_id': ramp['id'], 'points': deepcopy(ramp['points']),
                       'transport': paths.CAR, 'lane': 1, 'junction': True,
                       'avenue_port': ramp['avenue_port'],
                       'native_high_port': ramp['native_high_port']})
    return result


def module_catalog():
    """Describe six default R40 parts and four alternative full compact ramps."""
    routes = paths.slice_routes(access_routes())
    compact_routes = paths.slice_routes(paths.compact_access_routes())
    from .straight_stamp_geometry import WING_CELLS
    types, placements, compact_placements, owners, compact_owners = [], [], [], {}, {}
    for key, (name, world_cells) in MODULES.items():
        origin = min(c[0] for c in world_cells), min(c[1] for c in world_cells)
        cells = sorted(((c[0] - origin[0], c[1] - origin[1]) for c in world_cells),
                       key=lambda c: (c[1], c[0]))
        compact = key.endswith('-compact')
        selected_routes = compact_routes if compact else routes
        model_only = [list((c[0] - origin[0], c[1] - origin[1])) for c in world_cells
                      if c not in selected_routes and c[0] - c[1] not in (-1, 0, 1)]
        row = {'key': key, 'name': name, 'recipe': RECIPE_PREFIX + key.replace('-', '_'),
               'geometry_key': key, 'cells': [list(c) for c in cells],
               'footprint': [max(c[0] for c in cells) + 1, max(c[1] for c in cells) + 1],
               'world_origin_cell': list(origin), 'world_cells': [list(c) for c in world_cells],
               'authors_surface_atlas': False,
               'engineering': {'max_grade_percent': 30.0, 'pavement_path_offset_m': 0.0,
                               'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
                               'model_only_cells': model_only}}
        if not compact:
            row['engineering'].update({'minimum_new_curve_radius_m': RADIUS_M,
                                       'retained_high_collar_m': RETAINED_COLLAR_M})
        if '-terminal-' not in key:
            ramp_id = key.split('-')[0] + ('-off' if '-exit-' in key else '-on')
            branch = key.split('-')[0] + ('-exit-branch' if '-exit-' in key else '-entry-branch')
            row['model_overhang_source_cells'] = [list(c) for c in paths.MODULES[branch][1]
                                                  if c not in WING_CELLS[ramp_id]]
            row['model_overhang_contract'] = 'Retained indexed high-throat faces; construction and PATH ownership do not overlap.'
        types.append(row)
        (compact_placements if compact else placements).append({
            'key': key, 'geometry_key': key,
            'origin': [origin[axis] - paths.WORLD_GRID_ORIGIN[axis] for axis in (0, 1)], 'rotation': 0})
        selected_owners = compact_owners if compact else owners
        for cell in world_cells:
            _require(cell not in selected_owners and cell not in stamp_cells(),
                     f'A separately placed ramp or terminal overlaps another owner at {cell}')
            selected_owners[cell] = key
    return {'types': types, 'placements': placements, 'compact_placements': compact_placements,
            'world_grid_origin': list(paths.WORLD_GRID_ORIGIN), 'footprint': [10, 10],
            'occupied_cells': [list(c) for c in sorted(owners, key=lambda c: (c[1], c[0]))],
            'cell_owners': [{'cell': list(c), 'key': owners[c]}
                            for c in sorted(owners, key=lambda c: (c[1], c[0]))],
            'compact_occupied_cells': [list(c) for c in sorted(compact_owners, key=lambda c: (c[1], c[0]))],
            'compact_cell_owners': [{'cell': list(c), 'key': compact_owners[c]}
                                    for c in sorted(compact_owners, key=lambda c: (c[1], c[0]))],
            'excluded_highway_stamp_cells': [list(c) for c in sorted(stamp_cells())]}


def _pier_faces(ramp):
    """Seat a narrow, sloping pier beneath the constant-grade final straight."""
    from .ramp_geometry import _triangulate, ATLAS_UV
    outward = ramp['points'] if ramp['direction'] == 'off' else list(reversed(ramp['points']))
    end = ramp['standard_ground_port']
    at = next(index for index, point in enumerate(outward) if math.dist(point, end) < 1e-10)
    distances = _lengths(outward[:at + 1])
    station = distances[-1] - 14.0
    index = next(index for index, distance in enumerate(distances) if distance >= station)
    a, b = outward[index - 1:index + 1]
    length = distances[index] - distances[index - 1]
    fraction = (station - distances[index - 1]) / length
    centre = tuple(a[axis] + fraction * (b[axis] - a[axis]) for axis in range(3))
    dx, dy, grade = tuple((b[axis] - a[axis]) / length for axis in range(3))
    top = centre[2] - 1.0
    _require(top > 0.5, 'The selected ramp support must meet an elevated real underside')
    corners = [(a * .4, b * .4) for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    vertices = [(centre[0] + east, (top + grade * (dx * east + dy * north)) if upper else 0.0,
                 -(centre[1] + north), *ATLAS_UV['concrete'])
                for upper in (False, True) for east, north in corners]
    result = []
    for indices in ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4),
                    (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)):
        result.extend(_triangulate([vertices[index] for index in indices]))
    return result


@lru_cache(maxsize=1)
def procedural_geometry():
    """Partition complete physical sheets before selecting the six owners."""
    from .slip_lanes import WHITE, surfaces
    ramps = _variant_ramps()
    faces = [face for ramp in ramps for face in geometry.compact_ramp_triangles(ramp)]
    faces += [face for face in surfaces(ramps) if abs(face[0][3] - WHITE) < 1e-8]
    faces += [face for ramp in ramps for face in _pier_faces(ramp)]
    tiles = geometry.partition_triangles(geometry.union_ground_pavement(faces))
    routes = paths.deduplicate_routes(paths.slice_routes(access_routes()))
    owners = {cell for key, (_name, cells) in MODULES.items() if not key.endswith('-compact') for cell in cells}
    _require(set(tiles) <= owners | stamp_cells(),
             f'Actual R40 pavement/barrier/support faces exceed declared cells: {set(tiles) - owners - stamp_cells()}')
    _require(owners <= set(tiles) | {c for c in owners if c[0] - c[1] in (-1, 0, 1)},
             'An R40 structural cell has neither authored geometry nor a native Avenue surface')
    return ramps, tiles, routes


def component_routes(piece):
    key = piece.get('geometry_key')
    _require(key in MODULES, f'Unknown modular highway component {key}')
    declaration = next(row for row in module_catalog()['types'] if row['key'] == key)
    origin, owned = declaration['world_origin_cell'], set(MODULES[key][1])
    result = []
    for route in paths.compact_access_routes() if key.endswith('-compact') else access_routes():
        for cell, points in paths.polyline_fragments(route['points']):
            if cell in owned:
                result.append([(p[0] + 16 * (cell[0] - origin[0]),
                                p[1] - 16 * (cell[1] - origin[1]), p[2]) for p in points])
    # Native Avenue routes are visible in standalone terminal icons as well.
    if key.endswith('terminal-r40'):
        for lateral in (4.8 / ROOT_TWO, 11.2 / ROOT_TWO):
            for sign in (-1, 1):
                route = [geometry.world_coordinates(sign * lateral, -200.0),
                         geometry.world_coordinates(sign * lateral, 200.0)]
                for cell, points in paths.polyline_fragments(route):
                    if cell in owned:
                        result.append([(p[0] + 16 * (cell[0] - origin[0]),
                                        p[1] - 16 * (cell[1] - origin[1]), p[2]) for p in points])
    return result


def _phase_matched_painter(context, ramps):
    """Keep the accepted stamp's exact longitudinal texture phase at all joins.

    An entrance's texture station starts at its Avenue end. Moving that end
    changes every later station even when the high geometry is unchanged.
    One constant offset per physical road aligns its original native high end,
    preserving phase across the retained high collar and every new tile cut.
    """
    from .ramp_materials import NativeRoadPainter
    old_ramps = geometry.compact_ramps()
    old_turns = [{'points': row['surface_points']} for row in paths.compact_access_routes(old_ramps)]
    old = NativeRoadPainter(context, list(old_ramps) + old_turns)
    current = NativeRoadPainter(context, ramps)
    offsets = {}
    for ramp in ramps:
        reference = ramp['native_high_port']
        previous = old._frame(reference)
        measured = current._frame(reference)
        offsets[measured[3]] = previous[0] - measured[0]
    current.segments = [(first, last, distance + offsets[owner], length, dx, dy, owner)
                        for first, last, distance, length, dx, dy, owner in current.segments]
    current.cache.clear()
    return current


def compile_module(spec, context):
    """Compile only one ramp/terminal owner, retaining every Avenue service."""
    from scp.models import parse_s3d, pack_s3d
    from scp.recipes import combine_meshes
    from .native import channels, material_template
    declaration = next((row for row in module_catalog()['types']
                        if row['key'] == spec.get('geometry_key')), None)
    _require(declaration is not None, 'Unknown modular highway recipe or geometry key')
    _require(spec['cells'] == declaration['cells'] and spec['footprint'] == declaration['footprint'],
             'Allocated modular cells differ from the full physical ownership declaration')
    if spec['geometry_key'].endswith('-compact'):
        return _compile_compact(spec, context, declaration)
    origin = declaration['world_origin_cell']
    ramps, procedural_tiles, additional_paths = procedural_geometry()
    painter = _phase_matched_painter(context, ramps)
    base, _ = channels(context['dd_rhw'], 0x5753A380, False, 0)
    material = material_template(context)
    texture = int(spec['tile_ids'][0], 16)
    from .straight_stamp_geometry import partition, WING_CELLS
    key = spec['geometry_key']
    ramp_id = None if '-terminal-' in key else key.split('-')[0] + ('-off' if '-exit-' in key else '-on')
    transferred = partition(context) if ramp_id else None
    compiled = []
    for local in map(tuple, spec['cells']):
        cell = local[0] + origin[0], local[1] + origin[1]
        _require(cell not in stamp_cells(), 'A modular ramp may not compile a highway-stamp cell')
        if ramp_id and cell in WING_CELLS[ramp_id]:
            model = transferred['ramp_models'][ramp_id][cell]
            raw_path = transferred['wing_paths'][cell]
            from .native import parse_paths
            expected_empty = list(local) in declaration['engineering']['model_only_cells']
            _require(bool(parse_paths(raw_path)) != expected_empty,
                     f'Transferred high-wing PATH declaration differs in {cell}')
            compiled.append((local, model, raw_path))
            continue
        native_models, highway_routes, avenue_routes = paths._native_cell(context, cell)
        _require(not highway_routes, 'A separately placed ramp unexpectedly owns a highway through service')
        parts = []
        if native_models:
            native_raw = pack_s3d(combine_meshes(native_models))
            ground = [tuple((p[0] + 16 * cell[0], p[1], p[2] + 16 * cell[1], *p[3:]) for p in face)
                      for face in procedural_tiles.get(cell, ())
                      if all(abs(p[1]) < 1e-8 and abs(p[3] - geometry.ATLAS_UV['asphalt'][0]) < 1e-8
                             for p in face)]
            opened, _ = geometry.cut_native_branch_openings(native_raw, cell, ramps, ground_pavement=ground)
            model = parse_s3d(opened)
            parts.append((model, model['meshes'], (0.0, 0.0, 0.0)))
        if cell in procedural_tiles:
            raw = geometry.pack_road_model(procedural_tiles[cell], texture, material_template=material,
                                           model_template=base, native_painter=painter, cell=cell)
            model = parse_s3d(raw)
            parts.append((model, model['meshes'], (0.0, 0.0, 0.0)))
        _require(parts, f'R40 cell {cell} has no actual visible model')
        routes = [paths._route_metadata(route, 'native-avenue') for route in avenue_routes]
        routes += deepcopy(additional_paths.get(cell, []))
        routes = paths.mark_junctions(paths.deduplicate_routes({cell: routes}))[cell]
        empty = list(local) in declaration['engineering']['model_only_cells']
        _require(bool(routes) != empty, f'R40 model-only PATH declaration differs in {cell}')
        compiled.append((local, pack_s3d(combine_meshes(parts)), paths.encode_paths(routes, allow_empty=empty)))
    return compiled


def _compile_compact(spec, context, declaration):
    """Attach retained high throats to unchanged original compact grade models."""
    from scp import jsonc
    from .modular_stamp import ROOT
    from .straight_stamp_geometry import partition, WING_CELLS
    key = spec['geometry_key']
    stem = key.removesuffix('-compact')
    ramp_id = stem.split('-')[0] + ('-off' if '-exit' in stem else '-on')
    source = jsonc.load(ROOT / 'domains/highway/00_pieces' / f'ddrhw-diagonal-{stem}-grade' / 'piece.jsonc')
    grade_record = next(row for row in paths.module_catalog()['types'] if row['key'] == stem + '-grade')
    grade_origin = grade_record['world_origin_cell']
    original = {(cell[0] + grade_origin[0], cell[1] + grade_origin[1]): (model, path)
                for cell, model, path in paths.compile_module(source, context)}
    transferred = partition(context)
    origin = declaration['world_origin_cell']
    result = []
    for local in map(tuple, spec['cells']):
        world = local[0] + origin[0], local[1] + origin[1]
        if world in WING_CELLS[ramp_id]:
            model, path = transferred['ramp_models'][ramp_id][world], transferred['wing_paths'][world]
        else:
            model, path = original[world]
        result.append((local, model, path))
    return result


def construction_fields(spec, compiled):
    """Derive each owner and construction flag from its actual encoded paths."""
    from .native import parse_paths
    declaration = next(row for row in module_catalog()['types'] if row['key'] == spec['geometry_key'])
    origin = declaration['world_origin_cell']
    width, depth = spec['footprint']
    rows = [['.'] * (width + 2) for _ in range(depth + 1)]
    cons = deepcopy(rows)
    rows[0][-1] = cons[0][-1] = '<'
    rows[-1][0] = cons[-1][0] = '^'
    palette = []
    for index, (local, _model, raw) in enumerate(compiled):
        symbol = chr(ord('a') + index)
        rows[local[1]][local[0]] = symbol
        cell = local[0] + origin[0], local[1] + origin[1]
        native_avenue = cell[0] - cell[1] in (-1, 0, 1)
        routes = [paths._route_metadata(route, 'saved') for route in parse_paths(raw)]
        custom = [route for route in routes if route['junction'] and route['transport'] == paths.CAR]
        if not native_avenue:
            custom = routes
        fields = []
        if custom or not native_avenue:
            fields.append(f'dirtroad: 0x{paths.construction_flags(custom):08X}')
        if native_avenue:
            difference = cell[0] - cell[1]
            word = 0x01030103 if difference == 0 else 0x01000003 if difference == 1 else 0x00030100
            fields.append(f'avenue: 0x{word:08X}')
        palette.append(symbol + ' - ' + ' '.join(fields))
        cons[local[1]][local[0]] = '+' if custom or not native_avenue else '\\'
    return [''.join(row) for row in rows], palette, [''.join(row) for row in cons]


def build_piece(spec, context):
    """Package one separately placed part, with optional adaptive Avenue ground."""
    from .recipes import finish_piece, construction
    declaration = next((row for row in module_catalog()['types']
                        if row['key'] == spec.get('geometry_key')), None)
    _require(declaration is not None and not declaration['authors_surface_atlas']
             and not spec.get('authored_texture_ids'),
             'Native-textured modular ramps must not reserve an authored surface atlas')
    compiled = compile_module(spec, context)
    assets = finish_piece(spec, context, compiled)
    if spec.get('adaptive_ground'):
        from .adaptive_ground import build_resources, build_construction
        from scp.adaptive_network import RUL1
        from scp.build import RUL0
        extra = build_resources(spec, context, compiled)
        _require(not assets.keys() & extra.keys(), 'Adaptive modular runtime resources overlap canonical assets')
        assets.update(extra)
        return assets, build_construction(spec, compiled, context['controller'][RUL0],
                                          context['controller'][RUL1])
    rows, fields, cons = construction_fields(spec, compiled)
    return assets, construction(spec, rows, fields, cons)
