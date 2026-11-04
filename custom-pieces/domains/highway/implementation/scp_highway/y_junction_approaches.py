"""Reviewed native DD sockets for the first compact three-arm Y layout.

Each independently placeable owner requests one optional, unowned native
cell. Diagonal owners share four new RUL1 rows; the orthogonal owner reuses
four original rows. Original RUL2 remains unchanged. Native continuation
checks describe saved rules and PATHs, rather than a game observation.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import math
import re

from scp.dbpf import require

OPT_IN = 'native_y_junction_approaches'
SECTION = 'MonoRailDirtRoadIntersectionSolutions'
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
RUL1 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000001)
RUL2 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000002)
PATH = (0x296678F7, 0xA966883F)
NATIVE_RUL1_SHA256 = '4e44ec44283de6fccc3cd40492fc24154d13fb16a5150e13c201c6e615bba998'
NATIVE_CONTROLLER_SHA256 = {
    RUL0: 'd2a63a6c9070857c5360343cfa07f0be13ef0559fd659e9545c57c15dda672b9',
    RUL2: 'c427c7872743ca4cd9f583adf33c93a320babe37c42061fbd33c905696e7a3b1',
}
NATIVE_DEPENDENCY_SHA256 = {
    (0x5AD0E817, 0xBADB57F1, 0x57530200): '4eb082b8329ddf70be7333f3343c4f1a621985d3992b17ca624eef79dc0ee4a8',
    (*PATH, 0x57530200): 'e888625d239fe19f546f36f58bed998359440e889904fa4976c3aec355640eb1',
    (0x6534284A, 0x6BE08658, 0x57530200): '394c783a8fedf150c93d21701e1450a520d5c31ff59245e2d1e40ebf12889b70',
    (0x5AD0E817, 0xBADB57F1, 0x57530000): '3d94bcce2ff84c9bd06d3bbbc7a089b8eaa28cfe921c3d31e87a27300cffd3dd',
    (*PATH, 0x57530000): 'e5f4c27133d0b03bae145380e151eacd0a32ac42ee7dc5f8f3a51e04ff539853',
    (0x6534284A, 0x6BE08658, 0x57530000): 'a6625188affe6851b7c10797eef0170d9762e54d3f997aa6b39b7afae2fd2d67',
    (0x5AD0E817, 0xBADB57F1, 0x57530900): 'd319f9bb39e21e319f5ce566c5093ba9e955c4c0ed5a5dcbb703c6afe127c93a',
    (*PATH, 0x57530900): 'bd5435abd7e1f8360b3b8704eab474112330d8b7719333863e5bd264216415ce',
    (0x6534284A, 0x6BE08658, 0x57530900): 'd8c35e3673dee409fcc007c6adafcd193d50f551bffe473b70ef11c753cb63a9',
}
CONTINUATION_PATH_SHA256 = 'e888625d239fe19f546f36f58bed998359440e889904fa4976c3aec355640eb1'

# id: recipe, native outside world cell, owning world cell, core edge,
# native target, clockwise pose, native outer continuation edge and cell.
OWNERS = {
    'ddrhw-y-diagonal-stem-split': ('highway_ddrhw_y_diagonal_stem_split',
        (-2, 2), (-1, 2), 0, 0x57530900, 0, 3, (0, 1), 0x57530200, 2),
    'ddrhw-y-diagonal-branch': ('highway_ddrhw_y_diagonal_branch',
        (-2, -2), (-1, -2), 0, 0x57530900, 3, 1, (0, -1), 0x57530200, 1),
    'ddrhw-y-orthogonal-core': ('highway_ddrhw_y_orthogonal_core',
        (4, 0), (3, 0), 2, 0x57530000, 3, 2, (1, 0), 0x57530000, 3),
}


def _owner_record(piece):
    if piece.get('y_junction_variant') == 'reversed':
        from .y_junction_reversed_approaches import OWNERS as reversed_owners
        require(piece.get('id') in reversed_owners, 'Unknown reversed Y native owner')
        return reversed_owners[piece['id']]
    require(piece.get('y_junction_variant', 'original') == 'original'
            and piece.get('id') in OWNERS, 'Unknown original Y native owner or variant')
    return OWNERS[piece['id']]


def _rotate_flags(value, turns):
    shift = 8 * (turns % 4)
    return ((value << shift) | (value >> ((32 - shift) % 32))) & 0xFFFFFFFF


def _point(point, turns):
    east, north, height = point
    for _ in range(turns % 4):
        east, north = north, -east
    return east, north, height


def _reviewed(piece):
    from .y_junction_layout import module_catalog
    slug = piece.get('id')
    require(piece.get('y_junction_variant', 'original') == 'original'
            and slug in OWNERS and piece.get('domain') == 'highway'
            and piece.get('recipe') == OWNERS[slug][0], 'Unreviewed Y native approach owner')
    types = module_catalog()['types']
    values = types.values() if isinstance(types, dict) else types
    matching = [record for record in values if record['id'] == slug]
    require(len(matching) == 1, 'Y approach owner lacks a unique layout definition')
    record = matching[0]
    cells, tiles = piece.get('cells'), piece.get('tile_ids')
    require(isinstance(cells, list) and cells == [list(cell) for cell in record['cells']]
            and all(isinstance(cell, list) and len(cell) == 2
                    and all(type(value) is int for value in cell) for cell in cells)
            and piece.get('footprint') == list(record['footprint']),
            'Y native approach changes the reviewed owner cells or footprint')
    require(isinstance(tiles, list) and len(tiles) == len(cells)
            and all(isinstance(tile, str) and re.fullmatch('[0-9a-fA-F]{8}', tile) for tile in tiles)
            and len({tile.lower() for tile in tiles}) == len(tiles), 'Invalid Y native owner tile identities')
    require(not any(piece.get(name) for name in ('native_dd_approaches', 'native_ghsr_approaches',
            'native_orthogonal_approaches', 'adaptive_ground')), 'Y native approaches cannot mix approach or adaptive modes')
    return record


def approaches(piece):
    if piece.get('y_junction_variant') == 'reversed':
        from .y_junction_reversed_approaches import approaches as reversed_approaches
        return reversed_approaches(piece)
    if OPT_IN not in piece:
        return []
    require(type(piece[OPT_IN]) is bool, OPT_IN + ' must be an exact boolean')
    if not piece[OPT_IN]:
        return []
    record = _reviewed(piece)
    _recipe, outside, end, edge, target, pose, *_ = OWNERS[piece['id']]
    origin = record['world_origin_cell']
    outside = [outside[i] - origin[i] for i in range(2)]
    end = [end[i] - origin[i] for i in range(2)]
    require(outside not in piece['cells'] and end in piece['cells'],
            'Y native helper is owned, or its joining owner is absent')
    marker = _rotate_flags(0x01000400, pose)
    road = _rotate_flags(0x03010000 if target == 0x57530900 else 0x02000200, pose)
    return [{'cell': outside, 'end_cell': end,
             'end_tile_id': piece['tile_ids'][piece['cells'].index(end)].lower(),
             'outward_edge': edge, 'native_tile_id': f'{target:08x}', 'native_rotation': pose,
             'section': SECTION, 'networks': [{'name': 'monorail', 'flags': f'{marker:08x}'},
                                             {'name': 'dirtroad', 'flags': f'{road:08x}'}],
             'native_exemplar_group': '6be08658', 'native_model_reference': 'rkt0',
             'optional': True, 'experimental': True}]


def dependency_sha256(piece):
    rows = approaches(piece)
    targets = {int(rows[0]['native_tile_id'], 16)} if rows else set()
    if targets & {0x57530900, 0x57530200}:
        targets.update({0x57530900, 0x57530200})
    return {key: value for key, value in NATIVE_DEPENDENCY_SHA256.items()
            if key[2] in targets}


def additional_dependency_keys(piece):
    rows = approaches(piece)
    peer = {'57530900': 0x57530200, '57530200': 0x57530900}
    return {key for key in NATIVE_DEPENDENCY_SHA256 if rows and rows[0]['native_tile_id'] in peer
            and key[2] == peer[rows[0]['native_tile_id']]}


def dependency_model_references(piece):
    return {key: 'rkt0' for key in additional_dependency_keys(piece) if key[0] == 0x6534284A}


def rul1_sections(piece):
    if piece.get('y_junction_variant') == 'reversed':
        from .y_junction_reversed_approaches import rul1_sections as reversed_sections
        return reversed_sections(piece)
    rows = approaches(piece)
    if not rows:
        return {}
    target = int(rows[0]['native_tile_id'], 16)
    road = 0x03010000 if target == 0x57530900 else 0x02000200
    return {SECTION: tuple((_rotate_flags(0x01000400, turns), _rotate_flags(road, turns),
                            target, turns, 0) for turns in range(4))}


def existing_rul1_sections(piece):
    rows = approaches(piece)
    return rul1_sections(piece) if rows and rows[0]['native_tile_id'] == '57530000' else {}


def _palette(symbol, row):
    flags = ' '.join(f"{item['name']}: 0x{item['flags'].upper()}" for item in row['networks'])
    return f'{symbol} - {flags}, 0xFFFFFFFF optional'


def _extent(piece, row):
    width, depth = piece['footprint']
    x, y = row['cell']
    left, top = max(0, -x), max(0, -y)
    return left, top, max(width + 2 + left, x + left + 1), max(depth + 1 + top, y + top + 1)


def add_approaches(piece, layout, checks, constraints):
    declared = approaches(piece)
    if not declared:
        return list(layout), list(checks), list(constraints)
    row = declared[0]
    width, depth = piece['footprint']
    require(len(layout) == len(constraints) == depth + 1
            and all(len(line) == width + 2 for line in [*layout, *constraints]),
            'Y helpers require the reviewed core construction extent')
    for grid in (layout, constraints):
        require([(x, y) for y, line in enumerate(grid) for x, value in enumerate(line) if value == '^'] == [(0, depth)]
                and [(x, y) for y, line in enumerate(grid) for x, value in enumerate(line) if value == '<'] == [(width + 1, 0)],
                'Y helpers cannot move core coordinate anchors')
    left, top, columns, rows = _extent(piece, row)
    def padded(source):
        result = [['.'] * columns for _ in range(rows)]
        for y, line in enumerate(source):
            result[y + top][left:left + len(line)] = line
        return result
    layout, constraints = padded(layout), padded(constraints)
    x, y = row['cell'][0] + left, row['cell'][1] + top
    require(layout[y][x] == constraints[y][x] == '.', 'Y helper collides with an owned cell or anchor')
    used = {value for line in layout for value in line if value.isalpha()}
    symbol = next((value for value in reversed('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') if value not in used), None)
    require(symbol is not None, 'No Y native helper symbol remains')
    layout[y][x] = symbol
    return [''.join(line) for line in layout], [*checks, _palette(symbol, row)], [''.join(line) for line in constraints]


def check_construction_approaches(fields, piece):
    result = deepcopy(fields)
    declared = approaches(piece)
    if not declared:
        return result
    row = declared[0]
    left, top, columns, rows = _extent(piece, row)
    layout, constraints = [list(line) for line in fields['CellLayout']], [list(line) for line in fields['ConsLayout']]
    require(len(layout) == len(constraints) == rows
            and all(len(line) == columns for line in [*layout, *constraints]), 'Y native helper changes the padded extent')
    width, depth = piece['footprint']
    for grid in (layout, constraints):
        require([(x, y) for y, line in enumerate(grid) for x, value in enumerate(line) if value == '^'] == [(left, top + depth)]
                and [(x, y) for y, line in enumerate(grid) for x, value in enumerate(line) if value == '<'] == [(left + width + 1, top)],
                'Y native helper changes the modeled coordinate frame')
    x, y = row['cell'][0] + left, row['cell'][1] + top
    symbol = layout[y][x]
    require(symbol.isascii() and symbol.isalpha() and constraints[y][x] == '.'
            and sum(line.count(symbol) for line in layout) == 1, 'Y native helper is missing, repeated, or owned')
    palette = list(fields['CheckType'])
    matches = [line for line in palette if re.match(r'^\s*' + re.escape(symbol) + r'\s*-', line)]
    normalized = lambda value: re.sub(r'\s+', '', value).lower()
    require(len(matches) == 1 and normalized(matches[0]) == normalized(_palette(symbol, row)),
            'Y native helper changes its exact optional network flags or full mask')
    palette.remove(matches[0])
    layout[y][x] = '.'
    for grid in (layout, constraints):
        require(all(value == '.' for cy, line in enumerate(grid) for cx, value in enumerate(line)
                    if not (left <= cx < left + width + 2 and top <= cy < top + depth + 1)),
                'Y native helper padding contains an undeclared cell')
    result['CellLayout'] = [''.join(line[left:left + width + 2]) for line in layout[top:top + depth + 1]]
    result['ConsLayout'] = [''.join(line[left:left + width + 2]) for line in constraints[top:top + depth + 1]]
    result['CheckType'] = palette
    return result


def _continuation_templates():
    result = [
        '0x57530200,0,0,0x57000200,2,0=0x57530200,0,0,0x57530900,2,0',
        '0x57530200,3,0,0x57000200,1,0=0x57530200,3,0,0x57530900,1,0',
        '0x57530900,0,0,0x57000200,2,0=0x57530900,0,0,0x57530200,2,0',
        '0x57530900,3,0,0x57000200,1,0=0x57530900,3,0,0x57530200,1,0',
    ]
    result.extend(f'0x57530000,{pose},0,0x57000000,{base},0=0x57530000,{pose},0,0x57530000,{pose},0'
                  for pose in (1, 3) for base in (1, 3))
    return result


def check_native_continuation(controller):
    pins = {**NATIVE_CONTROLLER_SHA256, RUL1: NATIVE_RUL1_SHA256}
    require(all(key in controller and hashlib.sha256(controller[key]).hexdigest() == value for key, value in pins.items()),
            'Y approaches require pinned original NAM 50 RUL0, RUL1, and RUL2')
    rul0 = controller[RUL0].decode('ascii')
    starter = re.findall(r'^\[HighwayIntersectionInfo_0x0*5022\]([^\[]+)', rul0, re.I | re.M)
    require(len(starter) == 1 and 'checktype=a-dirtroad:0x02000200monorail:0x01000400,0xffffffffoptional'
            in re.sub(r'\s+', '', starter[0]).lower(), 'Original DD starter changed')
    from scp.native_approaches import _section_span, _solution_rows
    start, end = _section_span(controller[RUL1], SECTION)
    actual = _solution_rows(controller[RUL1][start:end])
    reused = 0
    for turns in range(4):
        pair = _rotate_flags(0x01000400, turns), _rotate_flags(0x02000200, turns)
        require([row for row in actual if row[:2] == pair] == [(*pair, 0x57530000, turns, 0)],
                'Original orthogonal DD starter solution is missing, changed, or ambiguous')
        require(not any(row[:2] == (_rotate_flags(0x01000400, turns), _rotate_flags(0x03010000, turns)) for row in actual),
                'Y diagonal markers collide with original native RUL1')
        reused += 1
    rows = [re.sub(r'\s+', '', line.split(';', 1)[0]).lower() for line in controller[RUL2].decode('ascii').splitlines()]
    require(all(rows.count(row) == 1 for row in _continuation_templates()), 'Y native continuation template changed')
    return {'native_starters_checked': 1, 'existing_native_rul1_solutions_checked': reused,
            'new_diagonal_marker_pairs_absent_from_native': 4, 'native_continuation_rows_checked': 8,
            'native_rul1_unchanged': True, 'native_rul2_unchanged': True, 'game_behavior_tested': False}


def _native_routes(target, donors=None):
    from .orthogonal_approaches import _NATIVE_BOUNDARY_MEASUREMENTS
    from scp.verify import parse_paths
    if target == 0x57530000:
        rows = _NATIVE_BOUNDARY_MEASUREMENTS[target]
        expected = [dict(zip(('transport', 'lane', 'entry', 'exit', 'compatibility', 'points'), row)) for row in rows]
    else:
        upper = [((3.2, -8., 15.), (8., -3.2, 15.)), ((-3.2, -8., 15.), (8., 3.2, 15.))]
        lower = [((8., 3.2, 7.5), (-3.2, -8., 7.5)), ((8., -3.2, 7.5), (3.2, -8., 7.5))]
        expected = [{'transport': 1, 'lane': lane, 'entry': entry, 'exit': exit_,
                     'compatibility': 0, 'points': points}
                    for entry, exit_, items in ((3, 2, upper), (2, 3, lower)) for lane, points in enumerate(items)]
        if target == 0x57530200:
            for route in expected:
                route['points'] = tuple(reversed(route['points']))
                route['entry'], route['exit'] = route['exit'], route['entry']
                route['lane'] = 1 - route['lane']
            expected.sort(key=lambda route: (-route['points'][0][2], route['lane']))
    if donors is not None:
        key = (*PATH, target)
        fingerprint = CONTINUATION_PATH_SHA256 if target == 0x57530200 else NATIVE_DEPENDENCY_SHA256[key]
        require(key in donors and hashlib.sha256(donors[key]).hexdigest() == fingerprint, 'Y native boundary PATH identity changed')
        actual = [route for route in parse_paths(donors[key])['routes']
                  if route['transport'] == 1 and all(point[2] > 0 for point in route['points'])]
        require(actual == [{**route, 'points': list(route['points'])} for route in expected], 'Y native lane measurements changed')
    return expected


def _members(routes, cell, edge, collar=False):
    result = {}
    for route in routes:
        for name, index, order in (('in', 0, route['points']), ('out', -1, list(reversed(route['points'])))):
            if route['entry' if name == 'in' else 'exit'] != edge:
                continue
            require(len(order) >= 2, 'Y native boundary PATH has no tangent')
            point = order[0]
            delta = tuple(order[1][i] - point[i] for i in range(3))
            length = math.sqrt(sum(value * value for value in delta))
            require(length > 0, 'Y native boundary PATH has a zero tangent')
            inward = tuple(value / length for value in delta)
            tangent = inward if name == 'in' else tuple(-value for value in inward)
            if collar:
                reached = 0.
                for value in order[1:]:
                    offset = tuple(value[i] - point[i] for i in range(3))
                    station = sum(offset[i] * inward[i] for i in range(3))
                    require(station >= reached - 2e-6 and math.dist(offset, tuple(station * value for value in inward)) <= 2e-6,
                            'Y saved native end loses its straight flat collar')
                    reached = station
                    if reached >= 3. - 2e-6:
                        break
                require(reached >= 3. - 2e-6, 'Y saved native end lacks a three-metre collar')
            key = route['transport'], route['lane'], route.get('compatibility', 0), name
            require(key not in result, 'Y native boundary repeats a directed lane class')
            result[key] = {'point': (point[0] + 16 * cell[0], point[1] - 16 * cell[1], point[2]), 'tangent': tangent}
    return result


def _compare(first, second, turns):
    require(len(first) == len(second) == 4, 'Y native boundary is incomplete or has extra routes')
    for key, value in first.items():
        opposite = (*key[:3], 'out' if key[3] == 'in' else 'in')
        require(opposite in second, 'Y native boundary lane class, permission, or direction changed')
        other = second[opposite]
        require(math.dist(_point(value['point'], turns), _point(other['point'], turns)) <= 2e-6
                and math.dist(_point(value['tangent'], turns), _point(other['tangent'], turns)) <= 2e-6,
                'Y native boundary position, height, or travel tangent changed')


def _oriented_propagation(piece):
    """Apply original templates in both build directions, without reflection.

    The forward neighbour and its four lane members are checked separately
    from this discrete controller proof. RUL2 rows have two source tiles and
    two resulting tiles; only their poses rotate, and their flip bits stay 0.
    """
    if piece.get('y_junction_variant') == 'reversed':
        from .y_junction_reversed_approaches import oriented_propagation
        return oriented_propagation(piece)
    _recipe, _outside, _end, _edge, target, pose, _outer, step, next_target, next_pose = _owner_record(piece)
    if pose == 0:
        cases = [('outward', 2, 0), ('inward', 0, 2)]
    elif target == 0x57530900:
        cases = [('outward', 3, 0), ('inward', 1, 2)]
    else:
        cases = [('outward', 6, 0), ('outward', 7, 0), ('inward', 4, 2), ('inward', 5, 2)]
    templates, result = _continuation_templates(), []
    seed_rows = rul1_sections(piece)[SECTION]
    for turns in range(4):
        for order, index, alignment in cases:
            source, output = [part.split(',') for part in templates[index].split('=')]
            source = [int(value, 16) if i % 3 == 0 else int(value) for i, value in enumerate(source)]
            output = [int(value, 16) if i % 3 == 0 else int(value) for i, value in enumerate(output)]
            for values in (source, output):
                for i in (1, 4):
                    values[i] = (values[i] + alignment + turns) % 4
            first = (target, (pose + turns) % 4) if order == 'outward' else (next_target, (next_pose + turns) % 4)
            second = (next_target, (next_pose + turns) % 4) if order == 'outward' else (target, (pose + turns) % 4)
            require(tuple(source[:2]) == first and tuple(output[:2]) == first
                    and tuple(output[3:5]) == second and source[2] == source[5] == output[2] == output[5] == 0,
                    'Original Y native propagation template does not produce the directed socket phase')
            seed = seed_rows[(pose + turns) % 4]
            require(seed[2:] == (target, (pose + turns) % 4, 0),
                    'Y marker seeding does not select the native propagation pose')
            vector = _point((step[0], -step[1], 0), turns)
            result.append({'piece_rotation': turns, 'construction_order': order,
                           'original_native_template': templates[index],
                           'template_clockwise_quarter_turns': (alignment + turns) % 4,
                           'seeded_helper_tile': f'{target:08x}', 'seeded_helper_pose': (pose + turns) % 4,
                           'further_native_tile': f'{next_target:08x}', 'further_native_pose': (next_pose + turns) % 4,
                           'further_native_step_en': list(vector[:2]),
                           'basic_rhw_tile': f'{source[3]:08x}', 'basic_rhw_pose': source[4]})
    return result


def check_native_boundary_paths(context, piece, resources):
    from .native import rotate_route
    from scp.verify import parse_paths
    declared = approaches(piece)
    require(declared, 'Y saved boundary check requires its explicit reviewed native socket')
    if context is None:
        donors, continuation = None, None
    else:
        donors = context if any(isinstance(key, tuple) for key in context) else {
            key: value for label in ('controller', 'dd_rhw') for key, value in context.get(label, {}).items()}
        if piece.get('y_junction_variant') == 'reversed':
            from .y_junction_reversed_approaches import check_native_continuation as reversed_continuation
            continuation = reversed_continuation(donors)
        else:
            continuation = check_native_continuation(donors)
    row = declared[0]
    target, pose = int(row['native_tile_id'], 16), row['native_rotation']
    key = (*PATH, int(row['end_tile_id'], 16))
    require(key in resources, 'Y saved native socket owner PATH is missing')
    core = _members(parse_paths(resources[key])['routes'], row['end_cell'], row['outward_edge'], collar=True)
    native = [rotate_route(route, pose) for route in _native_routes(target, donors)]
    helper = _members(native, row['cell'], (row['outward_edge'] + 2) % 4)
    _recipe, _outside, _end, _edge, _target, _pose, outer_edge, step, next_target, next_pose = _owner_record(piece)
    next_routes = [rotate_route(route, next_pose) for route in _native_routes(next_target, donors)]
    outer = _members(native, (0, 0), outer_edge)
    next_members = _members(next_routes, step, (outer_edge + 2) % 4)
    for turns in range(4):
        _compare(core, helper, turns)
        _compare(outer, next_members, turns)
    propagation = _oriented_propagation(piece)
    return {'sockets_checked': 1, 'boundary_members_checked': 4, 'proper_rotations_checked': 4,
            'rotated_boundary_member_checks': 16, 'native_continuation_member_checks': 16,
            'saved_flat_collar_minimum_m': 3., 'native_input_scope': 'pinned-public-numeric-measurements' if donors is None else 'reread-pinned-native-resources',
            'native_controller_reread': donors is not None, 'native_continuation': continuation,
            'native_helper_tile': f'{target:08x}', 'native_helper_pose': pose,
            'outward_continuation_tile': f'{next_target:08x}', 'outward_continuation_pose': next_pose,
            'native_rul2_oriented_propagation_checks': len(propagation), 'oriented_propagation': propagation,
            'in_game_dragging_tested': False, 'in_game_travel_tested': False}
