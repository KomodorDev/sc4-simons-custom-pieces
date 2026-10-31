"""Preserve compact-highway geometry above native texture-backed Avenue cells.

Canonical models, PATHs, and previews remain unchanged. Resolved Avenue tiles
select exact native textures, inverse-posed PATH aliases, and filtered model
props. The opposing half-tile pose is compensated without re-encoding images.
"""
from __future__ import annotations

from copy import deepcopy
import math
import re

from scp import adaptive_network
from scp.dbpf import encode_exemplar, exemplar, require
from scp.models import pack_s3d, parse_s3d, positions, validate_s3d
from scp.recipes import combine_meshes

from .native import parse_paths, rotate_route

S3D = adaptive_network.S3D
AVENUE_PATH = adaptive_network.PATH
TEXTURE = adaptive_network.TEXTURE
PROP = adaptive_network.PROP
T21 = adaptive_network.T21
NATIVE_PROP = (*PROP, 0x5EB4BEE9)
GROUND_MESH_NAMES = {b'Avenue', b'SCP opened Avenue'}
GROUND_MODEL_TEXTURES = {0x0400020E, 0x0400380E}
APPEARANCES = (0, 0x10, 0x20, 0x30)
ZOOMS = range(5)
MIN_PROP_DIMENSION_M = 0.01


def bindings(spec):
    """Validate the shared declaration against the measured Avenue corridor."""
    rows = adaptive_network.bindings(spec)
    if not rows:
        return []
    if spec.get('recipe', '').startswith('highway_ddrhw_parallel_'):
        from .parallel_modules import declaration as module_declaration
    else:
        from .ramp_paths import module_declaration
    declaration = module_declaration(spec)
    require(declaration is not None, 'Adaptive ground requires a known compact highway module')
    origin = declaration['world_origin_cell']
    expected = {}
    for local in map(tuple, spec['cells']):
        world = local[0] + origin[0], local[1] + origin[1]
        difference = world[0] - world[1]
        if difference in (-1, 0, 1):
            expected[local] = (world, difference)
    require({tuple(row['cell']) for row in rows} == set(expected),
            'Adaptive cells must cover the complete native Avenue corridor')
    for row in rows:
        world, difference = expected[tuple(row['cell'])]
        flags = 0x01030103 if difference == 0 else 0x01000003 if difference == 1 else 0x00030100
        donor = 0x04003800 if difference == 0 else 0x04000200
        rotation = 2 if difference == 1 else 0
        require(int(row['avenue_flags'], 16) == flags
                and int(row['texture_donor_id'], 16) == donor and row['rotation'] == rotation,
                'Adaptive Avenue flags, donor, or half-tile pose differs from native measurements')
        if spec.get('recipe', '').startswith('highway_ddrhw_parallel_'):
            # All nine frozen adaptive cells retain an actual deck or terminal overlay.
            expected_prop = True
        elif spec.get('geometry_key') == 'modular-stamp':
            expected_prop = sum(world) in (0, 1)
        elif spec.get('recipe', '').startswith('highway_ddrhw_modular_'):
            from .modular_ramps import procedural_geometry
            expected_prop = bool(procedural_geometry()[1].get(world))
        else:
            expected_prop = world != (1, 1)
        require(row['prop'] == expected_prop,
                'Adaptive prop declaration differs from the retained road geometry')
    return rows


def filter_overlay_model(raw):
    """Remove only audited native Avenue ground meshes; retain all apron faces.

    Opened Avenue fragments carry a prefix added by the existing branch-cut
    compiler. Ground-level MIS apron groups are independent retained geometry.
    Return None for the single Avenue-only cell instead of an empty prop.
    """
    model = parse_s3d(raw)
    keep, removed = [], 0
    for mesh in model['meshes']:
        if mesh['name'].rstrip(b'\0') not in GROUND_MESH_NAMES:
            keep.append(mesh)
            continue
        removed += 1
        for vi, _ii, _pi, mi in mesh['frames']:
            require(all(point[1] == 0.0 for point in positions(model['vertices'][vi])),
                    'Refusing to remove an elevated native Avenue mesh')
            require(set(model['materials'][mi]['textures']) <= GROUND_MODEL_TEXTURES
                    and model['materials'][mi]['textures'],
                    'Native Avenue mesh references an unaudited ground material')
    require(removed > 0, 'Adaptive canonical model has no audited Avenue ground mesh')
    if not keep:
        return None
    filtered = combine_meshes([(model, keep, (0.0, 0.0, 0.0))])
    validate_s3d(filtered)
    return pack_s3d(filtered)


def posed_path_alias(raw, rotation):
    """Cancel the resolved tile pose while preserving every merged route."""
    require(type(rotation) is int and rotation in range(4), 'Invalid resolved PATH pose')
    if rotation == 0:
        return raw
    routes = [rotate_route(route, (-rotation) % 4) for route in parse_paths(raw)]
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for index, route in enumerate(routes):
        lines += [f'-- SCP inverse-posed adaptive channel {index + 1}',
                  str(route['transport']), str(route['lane']), str(route['entry']),
                  str(route['exit']), str(route['compatibility']), str(len(route['points']))]
        # The canonical ramp encoder keeps nine decimal places, rather than
        # nine significant digits. Reusing the native donor encoder's .9g
        # would round those authored points. repr(float) round-trips every
        # parsed value exactly, including small offsets and high-deck points.
        lines += [','.join(repr(value) for value in point) for point in route['points']]
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


def _property(pid, kind, values, *, array=False):
    return {'id': f'0x{pid:08x}', 'type': f'0x{kind:04x}',
            'key_type': '0x0080' if array else '0x0000', 'values': values,
            'repetitions': len(values) if array else None}


def _name(value):
    return _property(0x20, 0xC00, value, array=True)


def _prop(raw_template, row, model_raw, title):
    native = exemplar(raw_template)
    props = {int(prop['id'], 16): prop for prop in native['properties']}
    flag = props.get(0xE83A081D, {})
    require(native['parent'] == [0, 0, 0] and props.get(0x10, {}).get('values') == [30]
            and flag.get('type') == '0x0b00' and flag.get('key_type') == '0x0000'
            and flag.get('values') == [1], 'Native prop donor lacks full-geometry rotation encoding')
    model = parse_s3d(model_raw)
    points = [point for block in model['vertices'] for point in positions(block)]
    require(points and all(math.isfinite(value) for point in points for value in point),
            'Adaptive prop needs finite nonempty model geometry')
    # A flat apron remains at height zero. Positive conservative occupant
    # dimensions avoid a degenerate prop without moving any model vertex.
    size = [max(MIN_PROP_DIMENSION_M, 2 * max(abs(point[0]) for point in points)),
            max(MIN_PROP_DIMENSION_M, max(0.0, max(point[1] for point in points))
                - min(0.0, min(point[1] for point in points))),
            max(MIN_PROP_DIMENSION_M, 2 * max(abs(point[2]) for point in points))]
    iid, model_iid = int(row['prop_id'], 16), int(row['prop_model_id'], 16)
    output = [_property(0x10, 0x300, [30]), _name(title), _property(0x21, 0x300, [iid]),
              _property(0x0ABFC024, 0x300, [31]),
              _property(0x27812810, 0x900, size, array=True),
              _property(0x27812820, 0x300, [*S3D, model_iid], array=True),
              _property(0x49A1E05A, 0x300, [0x49A1E995]),
              _property(0x4A89FCF3, 0xB00, [1]), _property(0x69F14D33, 0xB00, [0]),
              _property(0x8A5E5DB8, 0xB00, [0]), deepcopy(flag),
              _property(0xE9A316EB, 0x100, [0])]
    return encode_exemplar({'parent': [0, 0, 0], 'properties': output})


def _t21(row, title):
    resolved, prop = int(row['resolved_tile_id'], 16), int(row['prop_id'], 16)
    lot = [1, 0, (-row['rotation']) % 4, 0x80000, 0, 0x80000,
           0, 0, 0xFFFFF, 0xFFFFF, 0, resolved, prop]
    props = [_property(0x10, 0x300, [0x21]), _name(title),
             _property(0x21, 0x300, [int(row['t21_id'], 16)]),
             _property(0x49D55951, 0x100, [15] * 4, array=True),
             _property(0x88EDC789, 0x100, [2]),
             _property(0x88EDC793, 0x100, list(range(16)), array=True),
             _property(0x88EDC795, 0x100, list(range(4)), array=True),
             _property(0x88EDC900, 0x300, lot, array=True),
             _property(0xAA120972, 0x900, [0.0]), _property(0xAA120973, 0x900, [64.0]),
             _property(0xC9A5A1BE, 0x300, [resolved]),
             _property(0xCA81B8D4, 0x100, [4]), _property(0xCC3E4755, 0x100, [2]),
             _property(0xEC3BD470, 0x100, [15])]
    return encode_exemplar({'parent': [0, 0, 0], 'properties': props})


def build_resources(spec, context, compiled):
    """Return only the extra active-layer resources; never mutate canonical data."""
    rows = bindings(spec)
    if not rows:
        return {}
    require('adaptive_avenue' in context, 'Adaptive Avenue capture is required')
    capture = context['adaptive_avenue']
    canonical = {tuple(cell): (model, path) for cell, model, path in compiled}
    require(len(canonical) == len(compiled), 'Compiled adaptive cells must be unique')
    resources = {}
    for row in rows:
        cell = tuple(row['cell'])
        require(cell in canonical, 'Missing compiled adaptive cell')
        model, path = canonical[cell]
        resolved, donor = int(row['resolved_tile_id'], 16), int(row['texture_donor_id'], 16)
        resources[*AVENUE_PATH, resolved] = posed_path_alias(path, row['rotation'])
        for appearance in APPEARANCES:
            for zoom in ZOOMS:
                key = (*TEXTURE, donor + appearance + zoom)
                require(key in capture, 'Adaptive Avenue capture lacks a native appearance or zoom')
                resources[*TEXTURE, resolved + appearance + zoom] = capture[key]
        filtered = filter_overlay_model(model)
        require(bool(filtered) == row['prop'], 'Adaptive prop declaration differs from compiled geometry')
        if filtered is not None:
            require(NATIVE_PROP in capture, 'Adaptive Avenue capture lacks the native RKT0 prop donor')
            title = 'SCP | ' + spec['name'] + f' adaptive cell {cell}'
            resources[*S3D, int(row['prop_model_id'], 16)] = filtered
            resources[*PROP, int(row['prop_id'], 16)] = _prop(capture[NATIVE_PROP], row, filtered, title)
            resources[*T21, int(row['t21_id'], 16)] = _t21(row, title)
    require(set(resources) == adaptive_network.resource_keys(spec),
            'Adaptive resource closure differs from the declared cells')
    return resources


def _native_states(raw):
    result = set()
    for line in raw.decode('ascii').splitlines():
        active = line.split(';', 1)[0].strip()
        match = re.fullmatch(r'\[HighwayIntersectionInfo_0x([0-9a-f]+)\]', active, re.I)
        if match:
            result.add(int(match[1], 16))
        match = re.fullmatch(r'(?:RotationRing|AddTypes)\s*=\s*(.*)', active, re.I)
        if match:
            result.update(int(value.strip(), 16) for value in match[1].split(','))
    return result


def build_construction(spec, compiled, native_rul0, native_rul1):
    """Return RUL0/RUL1 deltas for a measured mixed static/FLEX component."""
    from .recipes import construction
    from .ramp_paths import construction_symbol
    if spec.get('recipe', '').startswith('highway_ddrhw_parallel_'):
        from .parallel_modules import construction_fields
    else:
        from .ramp_paths import construction_fields
    rows = bindings(spec)
    require(rows, 'Adaptive construction requires adaptive cell declarations')
    solutions = adaptive_network.expected_solutions([spec])
    require(len(solutions) == 4 * len(rows), 'Adaptive markers need four distinct paired rotations')
    start, end = adaptive_network.section_span(native_rul1)
    native = adaptive_network.solution_rows(native_rul1[start:end])
    require(not set(solutions) & {(a, b) for a, b, *_ in native},
            'Adaptive marker pair conflicts with native Street/Avenue construction')
    targets = {value[0] for value in solutions.values()}
    existing_targets = {int(match[1], 16) for match in re.finditer(
        rb'^\s*TYPE\w*\s*=\s*0x[0-9a-f]+\s*,\s*0x[0-9a-f]+\s*,\s*0x([0-9a-f]+)',
        native_rul1, re.I | re.M)}
    require(not targets & existing_targets, 'Adaptive resolved tile conflicts with native RUL1')
    puzzle = int(spec['puzzle_id'], 16)
    require(not {puzzle + turn * 0x10000 for turn in range(8)} & _native_states(native_rul0),
            'Adaptive construction state conflicts with native RUL0')
    layout, checks, constraints = construction_fields(spec, compiled)
    layout, constraints = list(map(list, layout)), list(map(list, constraints))
    by_cell = {tuple(row['cell']): row for row in rows}
    for index, (cell, _model, _path) in enumerate(compiled):
        row = by_cell.get(tuple(cell))
        if row is None:
            continue
        symbol = construction_symbol(index)
        checks[index] = (f'{symbol} - street: 0x{row["street_flags"]} '
                         f'avenue: 0x{row["avenue_flags"]}, 0xFFFFFFFF optional')
        constraints[cell[1]][cell[0]] = '.'
    helper = adaptive_network.construction_helper(spec)
    if helper is not None:
        x, y = helper
        require(layout[y][x] == '.', 'The temporary FLEX handle overlaps an owned cell')
        require(all(not line.startswith('Z - ') for line in checks),
                'The temporary FLEX handle symbol overlaps an owned-cell symbol')
        layout[y][x], constraints[y][x] = 'Z', '+'
        checks.append('Z - road: 0x02000200')
    rul0 = construction(spec, [''.join(row) for row in layout], checks,
                        [''.join(row) for row in constraints])
    rul1 = '\r\n'.join(f'TYPE{index}=0x{street:08X},0x{avenue:08X},0x{target:08X},{rotation},{flip}'
                       for index, ((street, avenue), (target, rotation, flip))
                       in enumerate(solutions.items(), 1)) + '\r\n'
    return {'rul0': rul0, 'rul1': rul1}
