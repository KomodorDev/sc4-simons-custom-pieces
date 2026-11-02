"""Compose two native diagonal DD halves above ordinary diagonal GHSR.

The crossing owns its two central tiles only. Native continuation helpers,
resource allocation, finishing resources, and independent checks belong to
their existing owners. Each rail boundary retains a three-metre collar along
the complementary native helper's chord, then meets its internal seam through
a one-metre collar at exactly 45 degrees.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import math

from scp.dbpf import require
from scp.models import pack_s3d, parse_s3d, valid_frame, validate_s3d
from scp.recipes import combine_meshes
from scp.track_paths import PATH, S3D

from .native import parse_paths, rotate_model, rotate_route


RECIPE = 'highway_ddrhw_diagonal_ghsr_crossing'
CELLS = ((0, 0), (0, 1))
FOOTPRINT = (1, 2)
ALIGNMENT_B_RECIPE = 'highway_ddrhw_diagonal_ghsr_crossing_alignment_b'
ALIGNMENT_B_CELLS = ((0, 0), (1, 0))
ALIGNMENT_B_FOOTPRINT = (2, 1)
ALIGNMENT_B_PARTS = (((0, 0), 0x5753A905, 0, 1),
                     ((1, 0), 0x5753A985, 2, 3))
EXTERIOR_COLLAR_M = 3.
INTERIOR_COLLAR_M = 1.
PACKED_VERTEX_FORMAT = 0x80004001
GHSR_DONOR = 0x5DC01A00
PARTS = (((0, 0), 0x5753A905, 0, 3),
         ((0, 1), 0x5753A985, 2, 1))

# Pins name the original unmodified native resources, not an authored output.
SOURCE_SHA256 = {
    ('dd_rhw', (*S3D, 0x5753A905)): '341aa73b6fc75596511883715d3edb3de91e988c3f7d1201bd02867313ee25f0',
    ('dd_rhw', (*PATH, 0x5753A905)): '830513d3274d30eb9934b42ef63e4b5324584af4056331fa61f5a636fe692857',
    ('dd_rhw', (*S3D, 0x5753A985)): '1937f3d3e5e0c42995fa309d37bffb32a7a30640681b2bfa2920a67d1eb339a8',
    ('dd_rhw', (*PATH, 0x5753A985)): '2d262758f1f1c22cacae2ef76847de3d995f0fa4a8d82244487501e0eccbd676',
    ('hsr', (*S3D, GHSR_DONOR)): '58e54d5d212e26564e5454c57b6fd3269067a7f48df81eec45925590c1a59fa6',
    ('hsr', (*PATH, GHSR_DONOR)): '978a2a8c8f8e5de89e80bd6841d0b91666407efe2e77c32c312c0ff2c6353e4a',
}

TRANSITION_METADATA = {
    'kind': 'authored-internal-ghsr-path-seam',
    'external_native_chord_collar_m': EXTERIOR_COLLAR_M,
    'external_chord_reference': 'complementary ordinary native GHSR helper',
    'internal_diagonal_collar_m': INTERIOR_COLLAR_M,
    'internal_collar_absolute_east_north_components_equal': True,
    'external_native_path_coordinates_preserved': True,
    'external_native_helper_path_tangents_preserved': True,
    'visible_native_mesh_attributes_preserved': True,
    'changes': [
        {'cell': [0, 0], 'source_route_index': 0, 'endpoint': 'exit',
         'axis': 'east', 'original_m': -2.8, 'authored_m': -2.9},
        {'cell': [0, 1], 'source_route_index': 0, 'endpoint': 'exit',
         'axis': 'east', 'original_m': 2.8, 'authored_m': 2.9},
    ],
    'game_operation_verified': False,
}


def _guard_sources(context):
    for (label, key), fingerprint in SOURCE_SHA256.items():
        require(key in context.get(label, {}), 'Missing audited DD/GHSR crossing source')
        require(hashlib.sha256(context[label][key]).hexdigest() == fingerprint,
                'Native DD/GHSR crossing source changed; re-audit its exact resource')


def _ground_paths(raw):
    """Read the pinned ordinary two-route, height-enabled native GHSR PATH."""
    lines = [line.strip() for line in raw.decode('ascii').splitlines()
             if line.strip() and not line.lstrip().startswith('--')]
    require(lines[:5] == ['SC4PATHS', '1.1', '2', '0', '1'],
            'Ordinary diagonal GHSR PATH header changed')
    cursor, routes = 5, []
    for _ in range(2):
        transport, lane, entry, exit_, count = map(int, lines[cursor:cursor + 5])
        cursor += 5
        require(transport == 7 and lane == 0 and count == 2,
                'Ordinary diagonal GHSR route metadata changed')
        points = [tuple(map(float, line.split(','))) for line in lines[cursor:cursor + count]]
        cursor += count
        require(all(len(point) == 3 and point[2] == 1. for point in points),
                'Ordinary diagonal GHSR route height changed')
        routes.append({'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
                       'compatibility': 0, 'points': points})
    require(cursor == len(lines), 'Unexpected ordinary diagonal GHSR PATH data')
    return routes


def _rail_collar(route, row, native_routes):
    """Match the actual native neighbour's chord at the complete rail boundary."""
    result = deepcopy(route)
    original = result['points']
    exterior_edge = 0 if row == 0 else 2
    require((result['entry'] == exterior_edge) != (result['exit'] == exterior_edge),
            'A ground crossing fragment must have exactly one exterior end')
    exterior_index = 0 if result['entry'] == exterior_edge else 1
    exterior, internal = original[exterior_index], original[1 - exterior_index]
    helper_turns, helper_east = (1, -16.) if row == 0 else (3, 16.)
    matches = []
    for native in native_routes:
        helper = rotate_route(native, helper_turns)
        points = [(east + helper_east, north, height) for east, north, height in helper['points']]
        seam = points[-1] if exterior_index == 0 else points[0]
        if math.dist(seam, exterior) < 1e-9:
            matches.append(points)
    require(len(matches) == 1, 'Ground crossing exterior lacks its exact directed native helper')
    first, last = matches[0]
    length = math.hypot(last[0] - first[0], last[1] - first[1])
    require(length > EXTERIOR_COLLAR_M, 'Native GHSR helper cannot contain the exterior collar')
    sign = 1. if exterior_index == 0 else -1.
    collar = (exterior[0] + sign * EXTERIOR_COLLAR_M * (last[0] - first[0]) / length,
              exterior[1] + sign * EXTERIOR_COLLAR_M * (last[1] - first[1]) / length,
              exterior[2])
    authored = list(internal)
    if abs(abs(authored[0]) - 2.8) < 1e-9:
        authored[0] = math.copysign(2.9, authored[0])
    require(abs(abs(authored[0]) - 2.9) < 1e-9
            and authored[1] == (-8. if row == 0 else 8.) and authored[2] == 1.,
            'Ground crossing internal seam differs from its reviewed corridor')
    internal_dx, internal_dy = exterior[0] - authored[0], exterior[1] - authored[1]
    require(abs(abs(internal_dx) - abs(internal_dy)) < 1e-9,
            'Ground crossing internal collar must follow the exact diagonal axis')
    component = INTERIOR_COLLAR_M / math.sqrt(2.)
    internal_collar = (authored[0] + math.copysign(component, internal_dx),
                       authored[1] + math.copysign(component, internal_dy), authored[2])
    require(math.dist(collar, internal_collar) > INTERIOR_COLLAR_M,
            'Ground crossing collars leave no interior blending segment')
    result['points'] = ([exterior, collar, internal_collar, tuple(authored)] if exterior_index == 0
                        else [tuple(authored), internal_collar, collar, exterior])
    return result


def _encode_paths(routes):
    """Use explicit authored heights for rail and both native highway decks."""
    require(len(routes) == 6 and [route['transport'] for route in routes] == [1] * 4 + [7] * 2,
            'The crossing needs four DD car and two GHSR rail fragments per tile')
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '1']
    for index, route in enumerate(routes, 1):
        lines += [f'-- SCP diagonal DD/GHSR channel {index}', str(route['transport']),
                  str(route['lane']), str(route['entry']), str(route['exit']),
                  str(route['compatibility']), str(len(route['points']))]
        lines += [','.join(format(value, '.12g') for value in point) for point in route['points']]
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


def _retained_models(context, highway_id, highway_turns, rail_turns):
    dd = parse_s3d(context['dd_rhw'][*S3D, highway_id])
    road_meshes = [mesh for mesh in dd['meshes'] if mesh['name'].rstrip(b'\0') != b'HSR']
    require([mesh['name'].rstrip(b'\0') for mesh in road_meshes] ==
            [b'Top Deck', b'Substructure', b'Barriers', b'Bottom Deck', b'Substructure', b'Barriers'],
            'Native DD/GHSR donor changed its six highway meshes')
    rail = parse_s3d(context['hsr'][*S3D, GHSR_DONOR])
    rail_meshes = [mesh for mesh in rail['meshes'] if all(valid_frame(rail, frame) for frame in mesh['frames'])]
    require(len(rail_meshes) == 1 and rail_meshes[0]['name'].rstrip(b'\0') == b'support',
            'Ordinary diagonal GHSR changed its one valid rendered mesh')
    dd = rotate_model(combine_meshes([(dd, road_meshes, (0., 0., 0.))]), highway_turns)
    rail = rotate_model(combine_meshes([(rail, rail_meshes, (0., 0., 0.))]), rail_turns)
    model = combine_meshes([(dd, dd['meshes'], (0., 0., 0.)),
                            (rail, rail['meshes'], (0., 0., 0.))])
    for vertices in model['vertices']:
        require(vertices['stride'] == 20 and vertices['format'] in (2, PACKED_VERTEX_FORMAT),
                'Native DD/GHSR requires position-and-UV vertices')
        vertices['format'] = PACKED_VERTEX_FORMAT
    validate_s3d(model)
    return pack_s3d(model)


def build_channels(context):
    """Return canonical ``(cell, S3D bytes, PATH bytes)`` for both owned tiles."""
    _guard_sources(context)
    source_rail = _ground_paths(context['hsr'][*PATH, GHSR_DONOR])
    compiled = []
    for cell, highway_id, highway_turns, rail_turns in PARTS:
        highway = [rotate_route(route, highway_turns)
                   for route in parse_paths(context['dd_rhw'][*PATH, highway_id])
                   if route['transport'] == 1]
        require(len(highway) == 4, 'Native DD/GHSR donor lost a highway lane')
        rail = [_rail_collar(rotate_route(route, rail_turns), cell[1], source_rail) for route in source_rail]
        compiled.append((cell, _retained_models(context, highway_id, highway_turns, rail_turns),
                         _encode_paths(highway + rail)))
    return compiled


def path_transition_report(context):
    """Measure authored rail-node movement against the original native chords."""
    _guard_sources(context)
    source = _ground_paths(context['hsr'][*PATH, GHSR_DONOR])
    rows = []
    for cell, _highway_id, _highway_turns, rail_turns in PARTS:
        for index, native in enumerate(source):
            original = rotate_route(native, rail_turns)
            changed = _rail_collar(original, cell[1], source)
            first, last = original['points']
            dx, dy = last[0] - first[0], last[1] - first[1]
            length = math.hypot(dx, dy)
            offsets = [abs(dx * (point[1] - first[1]) - dy * (point[0] - first[0])) / length
                       for point in changed['points']]
            rows.append({'cell': list(cell), 'source_route_index': index,
                         'maximum_lateral_deviation_from_source_chord_m': max(offsets),
                         'internal_endpoint_shift_m': max(math.dist(changed['points'][0], first),
                                                          math.dist(changed['points'][-1], last)),
                         'external_collar_m': EXTERIOR_COLLAR_M,
                         'internal_collar_m': INTERIOR_COLLAR_M})
    return {'routes': rows,
            'maximum_lateral_deviation_from_source_chord_m': max(
                row['maximum_lateral_deviation_from_source_chord_m'] for row in rows),
            'maximum_internal_endpoint_shift_m': max(row['internal_endpoint_shift_m'] for row in rows),
            'game_operation_verified': False}


def core_construction_data():
    """Return unchanged two-tile ownership before external helper padding."""
    return (['a.<', 'b..', '^..'],
            ['a - dirtroad: 0x03010000 monorail: 0x01000003',
             'b - dirtroad: 0x00000301 monorail: 0x00030100'],
            ['+.<', '+..', '^..'])


ALIGNMENT_B_TRANSITION_METADATA = {
    'kind': 'authored-native-helper-ghsr-boundary-collar',
    'external_native_chord_collar_m': EXTERIOR_COLLAR_M,
    'external_chord_reference': 'complementary ordinary native GHSR helper',
    'internal_diagonal_collar_m': INTERIOR_COLLAR_M,
    'internal_collar_absolute_east_north_components_equal': True,
    'external_native_helper_path_coordinates_preserved': True,
    'external_native_helper_path_tangents_preserved': True,
    'core_donor_external_path_coordinates_preserved': False,
    'core_donor_internal_path_coordinates_preserved': True,
    'visible_native_mesh_attributes_preserved': True,
    'changes': [
        {'cell': [0, 0], 'source_route_index': 0, 'endpoint': 'exit',
         'axis': 'east', 'original_m': 2.8, 'authored_m': 2.9},
        {'cell': [0, 0], 'source_route_index': 1, 'endpoint': 'entry',
         'axis': 'east', 'original_m': -2.9, 'authored_m': -2.8},
        {'cell': [1, 0], 'source_route_index': 0, 'endpoint': 'exit',
         'axis': 'east', 'original_m': -2.8, 'authored_m': -2.9},
        {'cell': [1, 0], 'source_route_index': 1, 'endpoint': 'entry',
         'axis': 'east', 'original_m': 2.9, 'authored_m': 2.8},
    ],
    'game_operation_verified': False,
}


def _alignment_b_rail_collar(route, column, native_routes):
    """Join unmodified north/south helpers and the common east/west rail seam.

    Native poses 1 and 3 do not put their rounded 2.8/2.9 m lane coordinates
    on identical opposite boundaries. Author the core boundary from the
    actual complementary helper, rather than moving that dynamic helper.
    The existing core east/west endpoints already coincide at +/-2.9 m.
    """
    result = deepcopy(route)
    exterior_edge = 1 if column == 0 else 3
    require((result['entry'] == exterior_edge) != (result['exit'] == exterior_edge),
            'Alignment B rail fragment must have exactly one exterior end')
    exterior_index = 0 if result['entry'] == exterior_edge else 1
    original_exterior = result['points'][exterior_index]
    internal = result['points'][1 - exterior_index]
    require(internal[0] == (8. if column == 0 else -8.)
            and abs(abs(internal[1]) - 2.9) < 1e-9 and internal[2] == 1.,
            'Alignment B rail internal seam differs from the reviewed east/west corridor')
    helper_turns, helper_north = (3, 16.) if column == 0 else (1, -16.)
    matches = []
    for native in native_routes:
        helper = rotate_route(native, helper_turns)
        points = [(east, north + helper_north, height)
                  for east, north, height in helper['points']]
        seam = points[-1] if exterior_index == 0 else points[0]
        if math.dist(seam, original_exterior) <= .100000001:
            matches.append((seam, points))
    require(len(matches) == 1,
            'Alignment B rail boundary lacks one reviewed directed native helper')
    exterior, (first, last) = matches[0]
    require(abs(math.dist(exterior, original_exterior) - .1) < 1e-9,
            'Alignment B native helper join differs from its reviewed 0.1 m correction')
    length = math.hypot(last[0] - first[0], last[1] - first[1])
    require(length > EXTERIOR_COLLAR_M,
            'Native GHSR helper cannot contain the alignment B exterior collar')
    sign = 1. if exterior_index == 0 else -1.
    collar = (exterior[0] + sign * EXTERIOR_COLLAR_M * (last[0] - first[0]) / length,
              exterior[1] + sign * EXTERIOR_COLLAR_M * (last[1] - first[1]) / length,
              exterior[2])
    component = INTERIOR_COLLAR_M / math.sqrt(2.)
    internal_collar = (internal[0] + math.copysign(component, exterior[0] - internal[0]),
                       internal[1] + math.copysign(component, exterior[1] - internal[1]),
                       internal[2])
    require(math.dist(collar, internal_collar) > INTERIOR_COLLAR_M,
            'Alignment B rail collars leave no interior blending segment')
    result['points'] = ([exterior, collar, internal_collar, internal] if exterior_index == 0
                        else [internal, internal_collar, collar, exterior])
    return result


def build_alignment_b_channels(context):
    """Return the other grid alignment without changing the retained A builder."""
    _guard_sources(context)
    source_rail = _ground_paths(context['hsr'][*PATH, GHSR_DONOR])
    compiled = []
    for cell, highway_id, highway_turns, rail_turns in ALIGNMENT_B_PARTS:
        highway = [rotate_route(route, highway_turns)
                   for route in parse_paths(context['dd_rhw'][*PATH, highway_id])
                   if route['transport'] == 1]
        require(len(highway) == 4, 'Native alignment B donor lost a highway lane')
        rail = [_alignment_b_rail_collar(rotate_route(route, rail_turns), cell[0], source_rail)
                for route in source_rail]
        compiled.append((cell, _retained_models(context, highway_id, highway_turns, rail_turns),
                         _encode_paths(highway + rail)))
    return compiled


def alignment_b_path_transition_report(context):
    """Measure helper-driven exterior corrections against the original core."""
    _guard_sources(context)
    source = _ground_paths(context['hsr'][*PATH, GHSR_DONOR])
    rows = []
    for cell, _highway_id, _highway_turns, rail_turns in ALIGNMENT_B_PARTS:
        for index, native in enumerate(source):
            original = rotate_route(native, rail_turns)
            changed = _alignment_b_rail_collar(original, cell[0], source)
            first, last = original['points']
            dx, dy = last[0] - first[0], last[1] - first[1]
            length = math.hypot(dx, dy)
            offsets = [abs(dx * (point[1] - first[1]) - dy * (point[0] - first[0])) / length
                       for point in changed['points']]
            exterior_index = 0 if original['entry'] == (1 if cell[0] == 0 else 3) else -1
            rows.append({'cell': list(cell), 'source_route_index': index,
                         'maximum_lateral_deviation_from_source_chord_m': max(offsets),
                         'external_endpoint_shift_m': math.dist(changed['points'][exterior_index],
                                                               original['points'][exterior_index]),
                         'internal_endpoint_shift_m': math.dist(changed['points'][0 if exterior_index == -1 else -1],
                                                               original['points'][0 if exterior_index == -1 else -1]),
                         'external_collar_m': EXTERIOR_COLLAR_M,
                         'internal_collar_m': INTERIOR_COLLAR_M})
    return {'routes': rows,
            'maximum_lateral_deviation_from_source_chord_m': max(
                row['maximum_lateral_deviation_from_source_chord_m'] for row in rows),
            'maximum_external_endpoint_shift_m': max(row['external_endpoint_shift_m'] for row in rows),
            'maximum_internal_endpoint_shift_m': max(row['internal_endpoint_shift_m'] for row in rows),
            'external_native_helper_coordinates_preserved': True,
            'game_operation_verified': False}


def alignment_b_core_construction_data():
    """Return the horizontal two-cell core before unowned helper row padding."""
    return (['ab<', '...', '^..'],
            ['a - dirtroad: 0x03010000 monorail: 0x00030100',
             'b - dirtroad: 0x00000301 monorail: 0x01000003'],
            ['++<', '...', '^..'])
