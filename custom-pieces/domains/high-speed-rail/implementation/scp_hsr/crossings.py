"""Remaining double-track HSR/GHSR crossing combinations and their audits.

The native AAC0/AAC2/AAC3 rules describe same-network, two-height crossings.
Only the HSR and GHSR meshes are retained from their native model donors;
underground rail surfaces and pedestrian/rail traffic are omitted.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import math
import re
import struct

from scp.dbpf import require
from scp.models import parse_s3d, pack_s3d, valid_frame, validate_s3d, positions

S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
EXEMPLAR = (0x6534284A, 0xA8434037)
EFFECT = (0xEA5118B0, 0xEA5118B1)
LTEXT = (0x2026960B, 0x2A592FD1)
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
RECIPES = ('hsr_straight_ghsr', 'diagonal_hsr_straight_ghsr', 'diagonal_hsr_diagonal_ghsr')
INFO = {
    'hsr_straight_ghsr': {'family': 'AAC0', 'native_base': 0x59F33000,
                         'native_preview': 0x59F33005, 'effect': 0x59F3D105,
                         'effect_name': 'preview_hsrp_subrail____000', 'cost': 100,
                         'tile_count': 1},
    'diagonal_hsr_straight_ghsr': {'family': 'AAC2', 'native_base': 0x59F33030,
                                  'native_preview': 0x59F33035, 'effect': 0x59F3D135,
                                  'effect_name': 'preview_hsrp_subrail____002', 'cost': 150,
                                  'lower_models': (0x59F3D134, 0x59F3D144),
                                  'lower_paths': (0x59F3D130, 0x59F3D140), 'tile_count': 2},
    'diagonal_hsr_diagonal_ghsr': {'family': 'AAC3', 'native_base': 0x59F33050,
                                  'native_preview': 0x59F33055, 'effect': 0x59F3D155,
                                  'effect_name': 'preview_hsrp_subrail____003', 'cost': 150,
                                  'lower_models': (0x59F3D154, 0x59F3D164),
                                  'lower_paths': (0x59F3D150, 0x59F3D160), 'tile_count': 2},
}


def number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def _read_paths(raw):
    lines = [line.strip() for line in raw.decode('ascii').splitlines()
             if line.strip() and not line.lstrip().startswith('--')]
    require(lines[:2] in (['SC4PATHS', '1.1'], ['SC4PATHS', '1.2']), 'Unexpected crossing path format')
    count, stops, terrain = map(int, lines[2:5])
    require(count > 0 and stops == 0 and terrain in (0, 1), 'Unexpected crossing path header')
    cursor, result = 5, []
    for _ in range(count):
        fields = 5 if lines[1] == '1.1' else 6
        header = list(map(int, lines[cursor:cursor + fields])); cursor += fields
        require(len(header) == fields, 'Truncated crossing path header')
        if fields == 5:
            transport, lane, entry, exit_, count_nodes = header
            compat = None
        else:
            transport, lane, entry, exit_, compat, count_nodes = header
        require(count_nodes >= 2 and entry in range(4) and exit_ in range(4), 'Invalid crossing path direction')
        points = [tuple(map(float, line.split(','))) for line in lines[cursor:cursor + count_nodes]]
        cursor += count_nodes
        require(len(points) == count_nodes and all(len(p) == 3 and all(math.isfinite(v) for v in p) for p in points),
                'Invalid crossing path coordinates')
        result.append({'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
                       'compatibility': compat, 'points': points})
    require(cursor == len(lines), 'Trailing crossing path data')
    return lines[1], terrain, result


def _monorail(raw):
    return [route for route in _read_paths(raw)[2] if route['transport'] == 7]


def _write_paths(routes):
    require(len(routes) == 4 and all(r['transport'] == 7 for r in routes), 'Expected two routes at each railway level')
    lines = ['SC4PATHS', '1.2', '4', '0', '0']
    for route in routes:
        lines.extend([f"-- Mono_{route['entry']}_{route['exit']}", '7', '1',
                      str(route['entry']), str(route['exit']), '0', str(len(route['points']))])
        lines.extend(','.join(f'{v:g}' for v in point) for point in route['points'])
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


def canonicalize_shared_ports(routes, tile_no):
    """Correct two native C21B internal coordinates by 0.1 m, never externals.

    C21B's first lower tile ends at x=-2.8 on its south edge, while its partner
    starts at -2.9; the reverse path ends at +2.8 on the second tile's north
    edge. Both shared ports are made exactly +/-2.9, as in the other native
    crossing pairs. Meshes and all external path endpoints stay unchanged.
    """
    routes = deepcopy(routes)
    shared_y = -8. if tile_no == 0 else 8.
    for route in routes:
        for n, (x, y, z) in enumerate(route['points']):
            if z == 1. and y == shared_y and abs(abs(x) - 2.8) < 1e-6:
                route['points'][n] = (math.copysign(2.9, x), y, z)
    return routes


def _hsr_mesh(model):
    meshes = [mesh for mesh in model['meshes'] if mesh['name'].rstrip(b'\0') == b'HSR']
    require(len(meshes) == 1 and all(valid_frame(model, frame) for frame in meshes[0]['frames']),
            'Native crossing HSR mesh changed')
    return meshes


def build_crossing(spec, context):
    """Return piece assets and eight native construction rules, without a ring."""
    from scp.recipes import combine_meshes, tile_exemplar, effect_clone, family, label
    info = INFO[spec['recipe']]
    tiles = list(map(number, spec['tile_ids']))
    preview, puzzle = number(spec['preview_id']), spec['puzzle_id'].upper()
    require(len(tiles) == info['tile_count'], 'Crossing tile allocation does not match native footprint')
    hsr, urail = context['hsr'], context['urail']
    title, assets = 'SCP | ' + spec['name'] + ' (Experimental)', {}
    if spec['recipe'] == 'hsr_straight_ghsr':
        model = parse_s3d(hsr[*S3D, 0x5DCF0A00])
        meshes = [mesh for mesh in model['meshes'] if all(valid_frame(model, f) for f in mesh['frames'])]
        require(len(meshes) == 2, 'Native HSR x GHSR valid topology changed')
        raw = pack_s3d(combine_meshes([(model, meshes, (0., 0., 0.))]))
        models = [raw]
        paths = [hsr[*PATH, 0x5DCF0A00]]
    else:
        models, paths = [], []
        for n, (lower_id, path_id, upper_id, upper_path_id) in enumerate(zip(
                info['lower_models'], info['lower_paths'], (0x59F3D214, 0x59F3D224), (0x59F3D210, 0x59F3D220))):
            lower, upper = parse_s3d(urail[*S3D, lower_id]), parse_s3d(urail[*S3D, upper_id])
            assembled = combine_meshes([(lower, _hsr_mesh(lower), (0., 0., 0.)),
                                       (upper, _hsr_mesh(upper), (0., 0., 0.))])
            models.append(pack_s3d(assembled))
            ground_routes = _monorail(urail[*PATH, path_id])
            if spec['recipe'] == 'diagonal_hsr_diagonal_ghsr':
                ground_routes = canonicalize_shared_ports(ground_routes, n)
            paths.append(_write_paths(ground_routes + _monorail(urail[*PATH, upper_path_id])))
    for n, tile in enumerate(tiles):
        for zoom in range(5):
            assets[*S3D, tile + zoom] = models[n]
        assets[*PATH, tile] = paths[n]
        assets[*EXEMPLAR, tile] = tile_exemplar(hsr[*EXEMPLAR, 0x5DCF0A00], tile, title)
        assets[*LTEXT, tile] = label(title)
    parts = []
    for n, raw in enumerate(models):
        model = parse_s3d(raw)
        parts.append((model, model['meshes'], (0., 0., n * 16.)))
    assets[*S3D, preview] = pack_s3d(combine_meshes(parts))
    assets[*EFFECT, preview] = effect_clone(urail[*EFFECT, info['effect']], info['effect_name'],
                                          spec['effect_name'], info['effect'], preview)
    rules = family(context['controller'][RUL0].decode('ascii'), info['family'])
    rules = rules.replace(info['family'], puzzle).replace('rail:', 'monorail:')
    rules = rules.replace(f"0x{info['native_preview']:08X}", f'0x{preview:08X}')
    rules = rules.replace(f"0x{info['native_base']:08X}", f'0x{tiles[0]:08X}')
    old_effect = 'preview_rail_subrail____' + info['effect_name'][-3:]
    rules = rules.replace(old_effect, spec['effect_name'])
    rules = re.sub(r'(?m)^Costs\s*=\s*\d+', f"Costs = {info['cost']}", rules)
    require('rail:' not in rules.replace('monorail:', '') and info['family'] not in rules,
            'Native crossing references were not fully rewritten')
    return assets, rules


def _route(entry, exit_, start, end, height):
    return {'transport': 7, 'entry': entry, 'exit': exit_,
            'points': [(start[0], start[1], height), (end[0], end[1], height)]}


STRAIGHT = [_route(3, 1, (2, -8), (2, 8), 1), _route(1, 3, (-2, 8), (-2, -8), 1)]
DIAGONAL_UPPER = [
    [_route(3, 2, (2.9, -8), (8, -2.8), 15.5), _route(2, 3, (8, 2.9), (-2.9, -8), 15.5)],
    [_route(1, 0, (-2.9, 8), (-8, 2.8), 15.5), _route(0, 1, (-8, -2.9), (2.9, 8), 15.5)],
]
DIAGONAL_LOWER = [
    [_route(0, 3, (-8, -2.9), (-2.9, -8), 1), _route(3, 0, (2.9, -8), (-8, 2.9), 1)],
    [_route(2, 1, (8, 2.9), (2.9, 8), 1), _route(1, 2, (-2.9, 8), (8, -2.9), 1)],
]


def _signature(route):
    return (route['transport'], route['entry'], route['exit'],
            tuple(tuple(round(v, 6) for v in point) for point in route['points']))


def _transform(point, angle, mirror):
    x, y, height = point
    if mirror:
        x = -x
    for _ in range(angle):
        x, y = y, -x
    return x, y, height


def _edge(point):
    x, y, _ = point
    options = [abs(x + 8) < 1e-6, abs(y - 8) < 1e-6, abs(x - 8) < 1e-6, abs(y + 8) < 1e-6]
    require(sum(options) == 1, 'Crossing path endpoint is not on exactly one edge')
    return options.index(True)


def check_paths(resources, spec, donors=None):
    """Compare to independently stated endpoint values and every transformed port."""
    recipe, tiles = spec['recipe'], list(map(number, spec['tile_ids']))
    require(recipe in RECIPES and len(tiles) == INFO[recipe]['tile_count'], 'Unsupported crossing footprint')
    if recipe == 'hsr_straight_ghsr':
        expected = [STRAIGHT + [_route(2, 0, (8, 2), (-8, 2), 15.5),
                                _route(0, 2, (-8, -2), (8, -2), 15.5)]]
    else:
        expected = [(STRAIGHT if recipe == 'diagonal_hsr_straight_ghsr' else DIAGONAL_LOWER[n]) +
                    DIAGONAL_UPPER[n] for n in range(2)]
    routes_by_tile = []
    for tile, wanted in zip(tiles, expected):
        version, terrain, routes = _read_paths(resources[*PATH, tile])
        require(version == '1.2' and terrain == 0 and len(routes) == 4 and
                all(r['lane'] == 1 and r['compatibility'] == 0 for r in routes),
                'Crossing path header or native same-network class changed')
        require(Counter(map(_signature, routes)) == Counter(map(_signature, wanted)),
                'Crossing traffic endpoints, heights, or directions differ from independent reference')
        for route in routes:
            require(len({p[2] for p in route['points']}) == 1, 'Cross-level crossing shortcut')
            require(_edge(route['points'][0]) == route['entry'] and _edge(route['points'][-1]) == route['exit'],
                    'Crossing path direction differs from endpoint edge')
        routes_by_tile.append(routes)
    edge_samples = [(-8, 0, 0), (0, 8, 0), (8, 0, 0), (0, -8, 0)]
    for mirror in (False, True):
        for angle in range(4):
            starts, ends = [], []
            for n, routes in enumerate(routes_by_tile):
                for route in routes:
                    for point, port, target in ((route['points'][0], route['entry'], starts),
                                                 (route['points'][-1], route['exit'], ends)):
                        require(_edge(_transform(point, angle, mirror)) == _edge(_transform(edge_samples[port], angle, mirror)),
                                'Rotated or mirrored crossing port has wrong direction')
                        if len(tiles) == 2 and point[1] == (-8 if n == 0 else 8):
                            global_point = _transform((point[0], point[1] - n * 16, point[2]), angle, mirror)
                            target.append((n, tuple(round(v, 6) for v in global_point)))
            if len(tiles) == 2:
                require(len(starts) == len(ends) == 4 and Counter(p for _, p in starts) == Counter(p for _, p in ends),
                        'Crossing halves do not connect exactly at both levels')
                for n, point in starts:
                    matches = [other for other, p in ends if p == point]
                    require(len(matches) == 1 and matches[0] != n, 'Crossing port has ambiguous or same-tile connection')
    return {'tile_count': len(tiles), 'rotations_and_mirrors_checked': 8, 'exact_audited_paths': True,
            'no_crosslevel_routes': True, 'internal_port_correction_m': .1 if recipe == 'diagonal_hsr_diagonal_ghsr' else 0.}


def _mesh(model, mesh):
    frame = mesh['frames'][0]
    require(all(f == frame for f in mesh['frames']) and valid_frame(model, frame), 'Invalid static crossing model mesh')
    return tuple(deepcopy(model[name][index]) for name, index in
                 zip(('vertices', 'indices', 'primitives', 'materials'), frame))


def _translated(actual, source, delta):
    if actual[1:] != source[1:]:
        return False
    a, b = actual[0], source[0]
    if (a['flags'], a['format'], a['stride'], len(a['data'])) != (b['flags'], b['format'], b['stride'], len(b['data'])):
        return False
    pa, pb = positions(a), positions(b)
    return all(a['data'][o + 12:o + a['stride']] == b['data'][o + 12:o + b['stride']]
               for o in range(0, len(a['data']), a['stride'])) and all(
        abs(pa[i][n] - pb[i][n] - delta[n]) < 2e-6 for i in range(len(pa)) for n in range(3))


def check_models(resources, spec, donors=None):
    """Validate buffers, heights, zoom references, native copies and preview spacing."""
    from scp.dbpf import exemplar
    tiles = list(map(number, spec['tile_ids']))
    expected_preview, textures, count = [], set(), 0
    for n, tile in enumerate(tiles):
        raw = resources[*S3D, tile]
        require(all(resources[*S3D, tile + zoom] == raw for zoom in range(5)), 'Crossing zoom models unexpectedly differ')
        model = parse_s3d(raw)
        for zoom in range(5):
            validate_s3d(parse_s3d(resources[*S3D, tile + zoom])); count += 1
        actual = [_mesh(model, mesh) for mesh in model['meshes']]
        lower = [item for item in actual if max(p[1] for p in positions(item[0])) < 2.]
        upper = [item for item in actual if min(p[1] for p in positions(item[0])) > 14.]
        require(len(actual) == 2 and len(lower) == len(upper) == 1, 'Crossing must have one low deck and one clear elevated deck')
        if donors:
            if spec['recipe'] == 'hsr_straight_ghsr':
                source = parse_s3d(donors[*S3D, 0x5DCF0A00])
                expected = [_mesh(source, mesh) for mesh in source['meshes']
                            if all(valid_frame(source, f) for f in mesh['frames'])]
            else:
                source_lower = parse_s3d(donors[*S3D, INFO[spec['recipe']]['lower_models'][n]])
                source_upper = parse_s3d(donors[*S3D, (0x59F3D214, 0x59F3D224)[n]])
                expected = [_mesh(source_lower, _hsr_mesh(source_lower)[0]),
                            _mesh(source_upper, _hsr_mesh(source_upper)[0])]
            require(actual == expected, 'Crossing model buffers differ from native geometry, UVs or materials')
        properties = {number(p['id']): p['values'] for p in exemplar(resources[*EXEMPLAR, tile])['properties']}
        require(properties[0x10] == [11] and properties[0x27812823] == [*S3D, *range(tile, tile + 5)],
                'Crossing exemplar has wrong zoom-model references')
        expected_preview.extend((item, (0., 0., n * 16.)) for item in actual)
        textures.update(texture for material in model['materials'] for texture in material['textures'])
    preview = parse_s3d(resources[*S3D, number(spec['preview_id'])])
    validate_s3d(preview); count += 1
    meshes = [_mesh(preview, mesh) for mesh in preview['meshes']]
    require(len(meshes) == len(expected_preview) and
            all(_translated(item, source, offset) for item, (source, offset) in zip(meshes, expected_preview)),
            'Crossing preview does not match its exact playable models')
    return {'models_checked': count, 'native_buffer_comparison': bool(donors),
            'preview_matches_tiles': True, 'texture_ids': sorted(textures)}


def verify_crossing(resources, spec, donors=None):
    return {'paths': check_paths(resources, spec, donors), 'models': check_models(resources, spec, donors)}
