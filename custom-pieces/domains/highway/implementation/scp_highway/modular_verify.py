"""Independent traffic ownership and reviewed straight-partition outputs.

Rendering may deliberately overhang another component's traffic cells. Exact
audited output hashes bind that split; complete pavement and solid-corridor
checks therefore run on the assembled model union. Old compact verification
is unchanged. No function imports either modular builder.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import re

from scp import jsonc
from scp.dbpf import require
from scp.models import parse_s3d, validate_s3d
from scp.track_paths import PATH, S3D

REFERENCE = ('domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/'
             'checks/stamp-reference.jsonc')
STAMP = 'modular-stamp'
WORLD_CELLS = {
    'lower-exit-r40': ((0, -2), (1, -3), (1, -2), (2, -3)),
    'lower-entry-r40': ((-3, 1), (-2, 0), (-2, 1), (-3, 2)),
    'upper-exit-r40': ((-1, 3), (-1, 4), (0, 3), (1, 3), (-2, 4), (-3, 5)),
    'upper-entry-r40': ((3, -1), (4, -1), (3, 0), (3, 1), (4, -2), (5, -3)),
    'northwest-terminal-r40': tuple((x, y) for x in (-3, -2, -1) for y in (-3, -2, -1)),
    'southeast-terminal-r40': ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (2, 4),
                               (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4)),
    'lower-exit-compact': ((1, -3), (1, -2), (2, -3)),
    'lower-entry-compact': ((-3, 1), (-2, 1), (-3, 2)),
    'upper-exit-compact': ((0, 2), (-1, 3), (0, 3), (-1, 4), (-2, 4), (-3, 5)),
    'upper-entry-compact': ((4, -1), (3, -1), (2, 0), (3, 0), (4, -2), (5, -3)),
}
EMPTY = {'lower-exit-r40': ((1, 0),), 'lower-entry-r40': ((0, 1),),
         'upper-exit-r40': ((0, 2),), 'upper-entry-r40': ((2, 0),),
         'northwest-terminal-r40': ((0, 2), (2, 0)),
         'southeast-terminal-r40': ((1, 3), (3, 1)),
         'lower-exit-compact': ((0, 0),), 'lower-entry-compact': ((0, 0),),
         'upper-exit-compact': ((0, 3),), 'upper-entry-compact': ((3, 0),)}
ORIGINS = {key: (min(c[0] for c in cells), min(c[1] for c in cells))
           for key, cells in WORLD_CELLS.items()}
ORIGINS[STAMP] = (-4, -4)
# Literal source-layout endpoints, travel tangents, and signed grades. These
# belong to the reviewed interface; they are not read from authoring arrays.
LOW_HIGH = (24., 37.792555790382046, 6.745131503884605)
UP_HIGH = (-24., -56.142764726126174, 12.258240084515554)
LOW_FLAT = (-8., 35.76854249492381, 0.)
UP_FLAT = (24., -51.76854249492381, 0.)
LOW_TANGENT = (-.97934963172818, -.20217393213239)
UP_TANGENT = (.92731797329645, .37427446667033)
LOW_GRADE = -.22675579053998945
UP_GRADE = -.2960959566966601
PROFILES = {
    'lower': {'collar': (21.982877954619557, 37.37435140461956, 6.278010267023249),
              'length': 30.119488785042925, 'middle_grade': -.2543142572971316,
              'first_straight': 3.7306953600401243, 'last_straight': 18.15899625736688,
              'arc_centre': (10.158996257366885, 75.7685424949238),
              'arc_heading': 3.3473379160153747, 'arc_finish': math.pi},
    'upper': {'collar': (-22.046330265982746, -55.34969481598275, 11.633920359366007),
              'length': 46.55209468662746, 'middle_grade': -.2782677403159753,
              'first_straight': 1.6237823977932182, 'last_straight': 29.423929626680593,
              'arc_centre': (-5.423929626680591, -91.7685424949238),
              'arc_heading': .38761017790813923, 'arc_finish': 0.},
}


def reference():
    return jsonc.load(Path(__file__).resolve().parents[4] / REFERENCE)


def stamp_reference_cells():
    """Retain only the 19 native DD and two pure Avenue traffic cells."""
    rows = [r for r in reference()['cells'] if sum(r['source_world_cell']) in (0, 1)
            or r['source_world_cell'][0]-r['source_world_cell'][1] in (-1, 0, 1)]
    require(len(rows) == 21, 'The straight stamp must retain exactly twenty-one native traffic cells')
    return rows


def geometry_key(piece):
    key = piece.get('geometry_key')
    require(key == STAMP or key in WORLD_CELLS, 'Unknown independent modular highway contract')
    recipe = ('highway_ddrhw_modular_stamp' if key == STAMP else
              'highway_ddrhw_modular_' + key.replace('-', '_'))
    require(piece.get('recipe') == recipe, 'Modular recipe and geometry contract disagree')
    return key


def validate_specification(piece):
    key = geometry_key(piece)
    if key == STAMP:
        data = reference()
        cells, footprint = stamp_reference_cells(), data['footprint']
        expected = [row['cell'] for row in cells]
        empty = []
        require(len(expected) == 21 and data['source_layout_origin_cell'] == [-4, -4],
                'Frozen stamp reference has the wrong measured scope')
    else:
        origin = ORIGINS[key]
        expected = sorted(([x-origin[0], y-origin[1]] for x, y in WORLD_CELLS[key]),
                          key=lambda c: (c[1], c[0]))
        footprint = [max(c[a] for c in expected)+1 for a in (0, 1)]
        empty = [list(c) for c in EMPTY[key]]
    require(piece['cells'] == expected and piece['footprint'] == footprint,
            'Modular component differs from its independent physical cell partition')
    require(len(piece['tile_ids']) == len(expected) and len(set(piece['tile_ids'])) == len(expected),
            'Modular cell resources have missing or repeated tile identities')
    engineering = piece.get('engineering', {})
    require(engineering.get('max_grade_percent') == 30.0 and
            engineering.get('pavement_path_offset_m') == 0.0 and
            engineering.get('car_corridor_half_width_m') == 1.25 and
            engineering.get('car_corridor_height_m') == 3.8 and
            {tuple(c) for c in engineering.get('model_only_cells', [])} == {tuple(c) for c in empty},
            'Modular grade, pavement datum, car corridor, or model-only declaration changed')
    return key


def _reflect(point):
    return -point[1], -point[0], point[2]


def custom_ports(key):
    """Return the literal source-layout ramp/terminal boundaries."""
    low = [('in', LOW_HIGH, LOW_TANGENT, LOW_GRADE),
           ('out', LOW_FLAT, (-1., 0.), 0.)]
    upper = [('in', UP_HIGH, UP_TANGENT, UP_GRADE),
             ('out', UP_FLAT, (1., 0.), 0.)]
    def entry(rows):
        return [('out' if direction == 'in' else 'in', _reflect(point),
                 (tangent[1], tangent[0]), -grade)
                for direction, point, tangent, grade in rows]
    lookup = {'lower-exit-r40': low, 'lower-entry-r40': entry(low),
              'upper-exit-r40': upper, 'upper-entry-r40': entry(upper),
              'northwest-terminal-r40': [('in', LOW_FLAT, (-1., 0.), 0.),
                    ('out', _reflect(LOW_FLAT), (0., -1.), 0.)],
              'southeast-terminal-r40': [('in', UP_FLAT, (1., 0.), 0.),
                    ('out', _reflect(UP_FLAT), (0., 1.), 0.)]}
    return [{'direction': direction, 'point_m': point, 'tangent': tangent, 'grade': grade,
             'transport': 1} for direction, point, tangent, grade in lookup[key]]


def expected_ports(piece):
    """Use complete independent checkpoint ports, including split fragments."""
    from .connections import reviewed_path_ports
    return reviewed_path_ports(piece)


def _stamp_paths(resources, piece):
    for identifier, row in zip(piece['tile_ids'], stamp_reference_cells()):
        require(hashlib.sha256(resources[*PATH, int(identifier, 16)]).hexdigest() == row['path_sha256'],
                'Saved stamp PATH differs from the frozen retained native/slip-lane contract')


def _audited_piece(piece):
    result = deepcopy(piece)
    result['engineering']['external_ports'] = expected_ports(piece)
    return result


def _distance_to_segment(point, a, b):
    delta = tuple(b[i]-a[i] for i in range(3))
    squared = sum(v*v for v in delta)
    fraction = 0. if squared == 0. else min(1., max(0., sum(
        (point[i]-a[i])*delta[i] for i in range(3))/squared))
    return math.dist(point, tuple(a[i]+fraction*delta[i] for i in range(3)))


def _source_routes(resources, piece):
    from .ramp_verify import _paths
    origin = ORIGINS[geometry_key(piece)]
    return [{**route, 'points': [(p[0]+16*(cell[0]+origin[0]),
                                p[1]-16*(cell[1]+origin[1]), p[2]) for p in route['points']]}
            for cell, identifier in zip(piece['cells'], piece['tile_ids'])
            for route in _paths(resources[*PATH, int(identifier, 16)])]


def check_profile_routes(routes, key):
    """Measure the saved R40 plan and vertical profile against literal anchors.

    Tile cuts can fall inside a sampled circular chord, so the 0.3 mm radial
    guard includes its independently bounded 0.25 m chord sagitta. Heights
    allow 0.5 mm for interpolation within the sampled grade-easing chords.
    """
    cars = [route for route in routes if route['transport'] == 1]
    if key.endswith('terminal-r40'):
        lower = key.startswith('northwest')
        start, first_heading = (LOW_FLAT, math.pi) if lower else (UP_FLAT, 0.)
        centres = [(start[0]+40*math.sin(first_heading), start[1]-40*math.cos(first_heading))]
        controls = [(centres[0][0]-40*math.sin(first_heading-math.pi/4*t/12),
                     centres[0][1]+40*math.cos(first_heading-math.pi/4*t/12), 0.)
                    for t in range(13)]
        controls += [_reflect(p) for p in controls]
        segments = [(a, b) for route in cars for a, b in zip(route['points'], route['points'][1:])]
        require(segments and all(min(_distance_to_segment(p, a, b) for a, b in segments) < .0003
                                 for p in controls),
                'Saved terminal does not follow both literal R40 ground-turn curves')
        require(all(abs(p[2]) < 2e-6 for route in routes for p in route['points']),
                'A ground Avenue terminal contains an elevated or sloped traffic route')
        return {'passed': True, 'literal_r40_ground_controls': len(controls),
                'new_radius_m': 40., 'ground_height_m': 0.}
    lower, entry = key.startswith('lower'), '-entry-' in key
    profile = PROFILES['lower' if lower else 'upper']
    ground = _reflect(LOW_FLAT if lower else UP_FLAT) if entry else (LOW_FLAT if lower else UP_FLAT)
    high = _reflect(LOW_HIGH if lower else UP_HIGH) if entry else (LOW_HIGH if lower else UP_HIGH)
    start = ground if entry else high
    remaining, points = list(cars), []
    finish = high if entry else ground
    # The complete attachment now also owns the old wing fragments. Measure
    # the independently fixed R40 continuation between its retained internal
    # datum and flat end; the complete ownership graph is checked separately.
    while math.dist(start, finish) >= 4e-5:
        choices = [r for r in remaining if math.dist(r['points'][0], start) < 4e-5]
        require(len(choices) == 1, 'Saved R40 ramp has a missing, reversed, or ambiguous directed continuation')
        route = choices[0]
        points.extend(route['points'] if not points else route['points'][1:])
        start = route['points'][-1]
        remaining.remove(route)
    require(points and math.dist(points[-1], high if entry else ground) < 4e-5,
            'Saved R40 ramp does not join its two literal sockets')
    if entry:
        points = [_reflect(p) for p in reversed(points)]
    collar_index = next((i for i, p in enumerate(points) if math.dist(p, profile['collar']) < 4e-5), None)
    require(collar_index is not None, 'Saved ramp lost its retained high collar end')
    points = points[collar_index:]
    distances = [0.]
    for a, b in zip(points, points[1:]):
        distances.append(distances[-1]+math.dist(a[:2], b[:2]))
    require(abs(distances[-1]-profile['length']) < .0002,
            'Saved R40 continuation changed its independently measured length')
    grade, middle = LOW_GRADE if lower else UP_GRADE, profile['middle_grade']
    graded = profile['length']-1.
    height = profile['collar'][2]
    maximum_height_error, maximum_radius_error, arc_count = 0., 0., 0
    for point, station in zip(points, distances):
        if station >= graded:
            expected_height = 0.
        elif station <= 8.:
            expected_height = height+grade*station+(middle-grade)*station*station/16.
        elif station <= graded-8.:
            expected_height = height+(grade+middle)*4.+middle*(station-8.)
        else:
            expected_height = -middle*(graded-station)**2/16.
        error = abs(point[2]-expected_height)
        require(error < .0005, 'Saved ramp differs from its literal continuous grade-easing profile')
        maximum_height_error = max(maximum_height_error, error)
        if profile['first_straight']+.0001 < station < profile['length']-profile['last_straight']-.0001:
            radial_error = abs(math.dist(point[:2], profile['arc_centre'])-40.)
            require(radial_error < .0003, 'Saved new ramp curve differs from its literal 40-metre circle')
            maximum_radius_error = max(maximum_radius_error, radial_error)
            arc_count += 1
    require(arc_count >= 10, 'Saved ramp has no adequately sampled R40 circular section')
    return {'passed': True, 'new_radius_m': 40., 'saved_arc_points_checked': arc_count,
            'maximum_radius_error_m': maximum_radius_error,
            'maximum_profile_height_error_m': maximum_height_error,
            'flat_end_length_m': 1., 'grade_easing_length_m': 8.,
            'retained_high_collar_excluded_from_r40_claim': True}


def check_paths(resources, piece):
    from .ramp_verify import check_paths as inspect
    key = validate_specification(piece)
    if key == STAMP:
        _stamp_paths(resources, piece)
    result = inspect(resources, _audited_piece(piece))
    if key.endswith('-r40'):
        result['r40_profile'] = check_profile_routes(_source_routes(resources, piece), key)
    return {**result, 'independent_modular_partition_checked': True,
            'frozen_stamp_paths_checked': 21 if key == STAMP else 0,
            'literal_modular_ports_checked': True}


def _stamp_models(resources, piece):
    """Retained checkpoint-model helper; current outputs use the split contract."""
    from scp.verify import mesh_data, translated
    from .straight_stamp_geometry import matches_frozen_model
    for identifier, row in zip(piece['tile_ids'], reference()['cells']):
        require(hashlib.sha256(resources[*PATH, int(identifier, 16)]).hexdigest() == row['path_sha256'],
                'Saved stamp PATH differs from the frozen checkpoint contract')
    expected, textures = [], set()
    for cell, identifier, row in zip(piece['cells'], piece['tile_ids'], reference()['cells']):
        for zoom in range(5):
            raw = resources[*S3D, int(identifier, 16)+zoom]
            require(matches_frozen_model(raw, row['model_sha256']),
                    'Saved stamp model differs from its independently frozen cell contract')
            model = parse_s3d(raw)
            validate_s3d(model)
            textures.update(t for material in model['materials'] for t in material['textures'])
            if zoom == 0:
                expected.extend((mesh_data(model, mesh), (16.*cell[0], 0., 16.*cell[1]))
                                for mesh in model['meshes'])
    preview = parse_s3d(resources[*S3D, int(piece['preview_id'], 16)])
    validate_s3d(preview)
    require(len(preview['meshes']) == len(expected), 'Stamp preview omits or adds a source mesh')
    for mesh, (source, delta) in zip(preview['meshes'], expected):
        require(translated(mesh_data(preview, mesh), source, delta),
                'Stamp preview differs from its translated cells, UVs, indices, or materials')
    restored = sum(row.get('model_sha256') != row.get('inherited_model_sha256', row['model_sha256'])
                   for row in reference()['cells'])
    return {'passed': True, 'frozen_cell_models_checked': 27, 'frozen_cell_paths_checked': 27,
            'model_resources_checked': 136, 'preview_matches_all_cells': True,
            'pristine_native_avenue_cells_restored': restored,
            'texture_ids': sorted(textures), 'game_rendering_tested': False,
            'scope': 'Frozen canonical byte identity after restoring only the authored VERT descriptor for historical hash comparison, plus exact preview composition; retained cells reuse preceding geometry evidence, and adaptive active resources are checked separately.'}


def check_models(resources, piece, donors=None):
    from .modular_partition_verify import validate_reviewed_models
    validate_specification(piece)
    result = validate_reviewed_models(resources, piece)
    if piece.get('adaptive_ground'):
        from .adaptive_verify import check_resources
        result['adaptive_ground'] = check_resources(resources, piece)
    return result


def check_construction_fields(fields, piece, resources):
    key = validate_specification(piece)
    if piece.get('adaptive_ground'):
        from .adaptive_verify import check_construction_fields as inspect
        return inspect(fields, piece, resources)
    from .ramp_verify import _paths, _road_word
    width, depth = piece['footprint']
    rows = [['.']*(width+2) for _ in range(depth+1)]
    rows[0][-1], rows[-1][0] = '<', '^'
    cons, palette = deepcopy(rows), []
    for index, (cell, identifier) in enumerate(zip(piece['cells'], piece['tile_ids'])):
        symbol = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[index]
        rows[cell[1]][cell[0]], cons[cell[1]][cell[0]] = symbol, '+'
        routes = _paths(resources[*PATH, int(identifier, 16)])
        palette.append(f'{symbol} - dirtroad: 0x{_road_word(routes):08X}')
    normalize = lambda text: re.sub(r'0x[0-9a-fA-F]+', lambda m: m[0].upper(), text)
    require(fields.get('CellLayout') == [''.join(row) for row in rows] and
            fields.get('ConsLayout') == [''.join(row) for row in cons] and
            list(map(normalize, fields.get('CheckType', []))) == list(map(normalize, palette)) and
            fields.get('Costs') == ['1000'],
            'Modular construction changes cell ownership, anchors, or actual saved-route flags')
    return {'independent_modular_partition_checked': True, 'occupied_cells_checked': len(piece['cells']),
            'actual_saved_route_flags_checked': True, 'game_behavior_tested': False}


def saved_path_evidence(output):
    """Decode current modular canonical PATHs, without claiming a game test."""
    from scp.verify import strict_dbpf
    from .ramp_verify import _paths
    output = Path(output)
    raw = (output/'manifest.json').read_bytes()
    manifest = json.loads(raw)
    files = {r['path']: r for r in manifest['files']}
    pieces = []
    for piece in manifest['pieces']:
        if not piece['recipe'].startswith('highway_ddrhw_modular_'):
            continue
        archive = (output/piece['asset_file']).read_bytes()
        require(len(archive) == files[piece['asset_file']]['bytes'] and
                hashlib.sha256(archive).hexdigest() == files[piece['asset_file']]['sha256'],
                'Saved modular PATH evidence DAT differs from its native manifest')
        resources = strict_dbpf(archive)
        measured = check_paths(resources, piece)
        cells = []
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            data = resources[*PATH, int(tile, 16)]
            cells.append({'cell': cell, 'path_tgi': [f'{v:08x}' for v in (*PATH, int(tile, 16))],
                          'path_sha256': hashlib.sha256(data).hexdigest(), 'routes': _paths(data)})
        pieces.append({'piece_id': piece['id'], 'geometry_key': piece['geometry_key'],
            'source_world_origin_cell': list(ORIGINS[piece['geometry_key']]),
            'cells': cells, 'independent_path_checks': measured})
    return {'schema_version': 1, 'build_manifest_sha256': hashlib.sha256(raw).hexdigest(),
            'modular_types': len(pieces), 'canonical_cells': sum(len(p['cells']) for p in pieces),
            'straight_stamp_owned_cells': 21, 'pieces': pieces, 'game_operation': 'unverified',
            'scope': 'Canonical PATHs from eleven separately selectable modular types. R40 and compact alternatives reuse world positions and must not all be placed together. Render projection and physical q=8 mouths do not allocate PATH ownership.'}
