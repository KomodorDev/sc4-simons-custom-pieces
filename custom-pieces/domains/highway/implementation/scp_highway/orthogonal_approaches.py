"""Three outside native sockets for the reviewed orthogonal DD-to-L0 ramp.

The optional cells reproduce NAM 50's original DD and RHW-4 starter
markers. They are unowned native cells, and reuse existing RUL1 solutions
and RUL2 propagators without establishing live-game success.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import math
import re

from scp.dbpf import require

PIECE_ID = 'ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile'
MIRRORED_PIECE_ID = PIECE_ID + '-mirrored'
VARIANT_FIELD = 'transition_variant'
RECIPE = 'highway_ddrhw_orthogonal_l0_transition'
MIRRORED_RECIPE = RECIPE + '_mirrored'
OPT_IN = 'native_orthogonal_approaches'
CORE_CELLS = tuple((column, row) for row in range(6) for column in range(2))
DD_SECTION = 'MonoRailDirtRoadIntersectionSolutions'
GROUND_SECTION = 'RoadDirtRoadIntersectionSolutions'
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
RUL1 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000001)
RUL2 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000002)
NATIVE_RUL0_SHA256 = 'd2a63a6c9070857c5360343cfa07f0be13ef0559fd659e9545c57c15dda672b9'
NATIVE_RUL1_SHA256 = '4e44ec44283de6fccc3cd40492fc24154d13fb16a5150e13c201c6e615bba998'
NATIVE_RUL2_SHA256 = 'c427c7872743ca4cd9f583adf33c93a320babe37c42061fbd33c905696e7a3b1'
NATIVE_CONTROLLER_SHA256 = {RUL0: NATIVE_RUL0_SHA256, RUL2: NATIVE_RUL2_SHA256}
NATIVE_ARCHIVE_SHA256 = {
    'dd_rhw': 'ccf8dabd3930fce92d0baa872ff974e3a536ddcc40762505a2e70eafcf9c0dfb',
    'rhw4': 'e4433c0b5aea609c7b438d6451325dfa9b76bdc45f103e5a93f75d25b4ad6a96',
}

# Decompressed native bytes. Ground RHW-4 uses the direct model/PATH lookup;
# there is no native network exemplar with IID 57030000 in the audited input.
NATIVE_DEPENDENCY_SHA256 = {
    (0x5AD0E817, 0xBADB57F1, 0x57530000): '3d94bcce2ff84c9bd06d3bbbc7a089b8eaa28cfe921c3d31e87a27300cffd3dd',
    (0x296678F7, 0xA966883F, 0x57530000): 'e5f4c27133d0b03bae145380e151eacd0a32ac42ee7dc5f8f3a51e04ff539853',
    (0x6534284A, 0x6BE08658, 0x57530000): 'a6625188affe6851b7c10797eef0170d9762e54d3f997aa6b39b7afae2fd2d67',
    (0x5AD0E817, 0xBADB57F1, 0x57030000): '81bf6080e261e2a902d8836ce480e970af8428d9f4a9b36d2290b3a8522f21dc',
    (0x296678F7, 0xA966883F, 0x57030000): '8d663b22e6762fddd0a55389f23f58636f43d2582435c78a36e4933b89cc294c',
}


def _rotate(value, turns):
    shift = 8 * (turns % 4)
    return ((value << shift) | (value >> ((32 - shift) % 32))) & 0xFFFFFFFF


def variant(piece):
    """Identify only a finite reviewed owner; absence preserves the original."""
    from .orthogonal_transition_variants import variant_of
    try:
        return variant_of(piece)
    except ValueError as error:
        raise ValueError('Unreviewed orthogonal approach owner or variant') from error


def approaches(piece):
    """Bind three reviewed sockets to the actual allocated owning cells."""
    if OPT_IN not in piece:
        return []
    require(type(piece[OPT_IN]) is bool, OPT_IN + ' must be an exact boolean')
    if not piece[OPT_IN]:
        return []
    reviewed_variant = variant(piece)
    cells = piece.get('cells', [])
    require(isinstance(cells, list) and all(isinstance(cell, list) and len(cell) == 2
            and all(type(value) is int for value in cell) for cell in cells)
            and [tuple(cell) for cell in cells] == list(CORE_CELLS)
            and piece.get('footprint') == [2, 6], 'Orthogonal approaches require the reviewed two-by-six core')
    require(not piece.get('native_dd_approaches') and not piece.get('native_ghsr_approaches')
            and not piece.get('adaptive_ground'), 'Orthogonal approaches cannot mix native or adaptive modes')
    tiles = piece.get('tile_ids', [])
    require(isinstance(tiles, list) and len(tiles) == len(cells)
            and all(isinstance(tile, str) and re.fullmatch('[0-9a-fA-F]{8}', tile) for tile in tiles)
            and len({tile.lower() for tile in tiles}) == len(tiles), 'Invalid orthogonal owning cell identifiers')
    by_cell = {tuple(cell): tile.lower() for cell, tile in zip(cells, tiles)}
    bindings = (
        ((1, -1), (1, 0), 1, 0x57530000, 0, DD_SECTION, 'monorail', 0x01000400, 'rkt0'),
        ((0, 6), (0, 5), 3, 0x57030000, 0, GROUND_SECTION, 'road', 0x01000001, 'direct'),
        ((1, 6), (1, 5), 3, 0x57030000, 2, GROUND_SECTION, 'road', 0x00010100, 'direct'),
    ) if reviewed_variant == 'original' else (
        ((0, -1), (0, 0), 1, 0x57530000, 2, DD_SECTION, 'monorail', 0x04000100, 'rkt0'),
        ((0, 6), (0, 5), 3, 0x57030000, 0, GROUND_SECTION, 'road', 0x01000001, 'direct'),
        ((1, 6), (1, 5), 3, 0x57030000, 2, GROUND_SECTION, 'road', 0x00010100, 'direct'),
    )
    if reviewed_variant not in ('original', 'mirrored'):
        from .orthogonal_transition_variants import LOWER_BEND_RIGHT, record_for
        record = record_for(reviewed_variant)
        reflected, reversed_traffic = record.physical_reflection, record.traffic_reversed
        dd_column = 0 if reflected else 1
        upper_column, lower_column = ((1, 0) if reflected else (0, 1))
        if reviewed_variant == LOWER_BEND_RIGHT:
            upper_column, lower_column = dd_column, 1 - dd_column
        upper_pose, lower_pose = ((2, 0) if reversed_traffic else (0, 2))
        ground_poses = {upper_column: upper_pose, lower_column: lower_pose}
        dd_pose = 2 if reversed_traffic else 0
        bindings = (
            ((dd_column, -1), (dd_column, 0), 1, 0x57530000, dd_pose,
             DD_SECTION, 'monorail', _rotate(0x01000400, dd_pose), 'rkt0'),
            *(((column, 6), (column, 5), 3, 0x57030000, ground_poses[column],
               GROUND_SECTION, 'road', _rotate(0x01000001, ground_poses[column]), 'direct')
              for column in (0, 1)),
        )
    result = []
    for outside, end, edge, target, pose, section, marker, flags, reference in bindings:
        result.append({'cell': list(outside), 'end_cell': list(end), 'end_tile_id': by_cell[end],
                       'outward_edge': edge, 'native_tile_id': f'{target:08x}', 'native_rotation': pose,
                       'section': section, 'networks': [{'name': marker, 'flags': f'{flags:08x}'},
                                                      {'name': 'dirtroad', 'flags': '02000200'}],
                       'native_exemplar_group': '6be08658', 'native_model_reference': reference,
                       'optional': True, 'experimental': True})
    return result


def rul1_sections(piece):
    """Return the eight exact solutions already present in native NAM 50."""
    if not approaches(piece):
        return {}
    return {
        section: tuple((_rotate(marker, turns), _rotate(0x02000200, turns), target, turns, 0)
                       for turns in range(4))
        for section, marker, target in ((DD_SECTION, 0x01000400, 0x57530000),
                                        (GROUND_SECTION, 0x01000001, 0x57030000))
    }


def existing_rul1_sections(piece):
    """Declare exact existing rows; the framework must verify and reuse them."""
    return rul1_sections(piece)


def _palette_row(symbol, declaration):
    flags = ' '.join(f"{item['name']}: 0x{item['flags'].upper()}" for item in declaration['networks'])
    return f'{symbol} - {flags}, 0xFFFFFFFF optional'


def add_approaches(piece, layout, checks, constraints):
    """Add check-only cells, retaining the modeled coordinate frame exactly."""
    declared = approaches(piece)
    if not declared:
        return list(layout), list(checks), list(constraints)
    rows, cons = [list(row) for row in layout], [list(row) for row in constraints]
    require(len(rows) == len(cons) == 7 and all(len(row) == 4 for row in rows + cons),
            'Orthogonal approach construction requires the exact two-by-six core grid')
    for grid in (rows, cons):
        require([(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == '^'] == [(0, 6)]
                and [(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == '<'] == [(3, 0)]
                and all(char == '.' for char in grid[6][1:]),
                'Orthogonal approach construction changes its coordinate anchors')
    # The ground socket at (0, 6) needs the old caret cell. A caret fixes
    # only the x origin, so moving it one row down preserves the full frame.
    rows[6][0] = cons[6][0] = '.'
    rows, cons = [list('....'), *rows, list('^...')], [list('....'), *cons, list('^...')]
    palette, used = list(checks), {char for row in rows for char in row if char.isalpha()}
    for declaration in declared:
        symbol = next((char for char in reversed('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                       if char not in used), None)
        require(symbol is not None, 'No unused orthogonal approach symbol remains')
        x, y = declaration['cell'][0], declaration['cell'][1] + 1
        require(rows[y][x] == cons[y][x] == '.', 'A native orthogonal helper collides with a construction cell')
        rows[y][x] = symbol
        palette.append(_palette_row(symbol, declaration))
        used.add(symbol)
    return [''.join(row) for row in rows], palette, [''.join(row) for row in cons]


def check_construction_approaches(fields, piece):
    """Check emitted helpers independently, restoring the original core view.

    The caller must verify all restored owned cells, flags, tile addresses,
    preview settings, and other construction fields independently.
    """
    declared = approaches(piece)
    result = deepcopy(fields)
    if not declared:
        return result
    rows, cons = [list(row) for row in fields['CellLayout']], [list(row) for row in fields['ConsLayout']]
    require(len(rows) == len(cons) == 9 and all(len(row) == 4 for row in rows + cons),
            'Orthogonal helpers change the exact padded construction extent')
    for grid in (rows, cons):
        require([(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == '^'] == [(0, 8)]
                and [(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == '<'] == [(3, 1)],
                'Orthogonal helpers move the modeled coordinate frame')
    palette, removed = list(fields['CheckType']), set()
    normalized = lambda value: re.sub(r'\s+', '', value).lower()
    for declaration in declared:
        x, y = declaration['cell'][0], declaration['cell'][1] + 1
        symbol = rows[y][x]
        require(symbol.isascii() and symbol.isalpha() and symbol not in removed and cons[y][x] == '.'
                and sum(line.count(symbol) for line in rows) == 1,
                'A native orthogonal helper is missing, repeated, or statically owned')
        matches = [line for line in palette if re.match(r'^\s*' + re.escape(symbol) + r'\s*-', line)]
        require(len(matches) == 1 and normalized(matches[0]) == normalized(_palette_row(symbol, declaration)),
                'A native orthogonal helper changes the exact optional marker or full mask')
        rows[y][x] = '.'
        palette.remove(matches[0])
        removed.add(symbol)
    require(rows[0] == cons[0] == list('....') and rows[7] == cons[7] == list('....')
            and rows[8] == cons[8] == list('^...'), 'Undeclared cell outside the orthogonal core')
    rows, cons = rows[1:8], cons[1:8]
    rows[6][0] = cons[6][0] = '^'
    result['CellLayout'], result['ConsLayout'] = [''.join(row) for row in rows], [''.join(row) for row in cons]
    result['CheckType'] = palette
    return result


def check_native_continuation(controller):
    """Check original starters, eight existing solutions, and eight propagators."""
    for key, expected in ((RUL0, NATIVE_RUL0_SHA256), (RUL1, NATIVE_RUL1_SHA256), (RUL2, NATIVE_RUL2_SHA256)):
        require(key in controller and hashlib.sha256(controller[key]).hexdigest() == expected,
                'Orthogonal approaches require the pinned native NAM 50 RUL0, RUL1, and RUL2')
    rul0 = controller[RUL0].decode('ascii')
    for puzzle, marker in ((0x5000, 'road:0x01000001'), (0x5022, 'monorail:0x01000400')):
        matches = re.findall(r'^\[HighwayIntersectionInfo_0x0*' + f'{puzzle:x}' + r'\]([^\[]+)', rul0, re.I | re.M)
        require(len(matches) == 1 and 'checktype=a-dirtroad:0x02000200' + marker + ',0xffffffffoptional'
                in re.sub(r'\s+', '', matches[0]).lower(), 'Native orthogonal starter marker changed')
    native_sections, section = {}, None
    for line in controller[RUL1].decode('ascii').splitlines():
        active = re.sub(r'\s+', '', line.split(';', 1)[0]).lower()
        if active.startswith('['):
            section = active[1:-1]
        elif active and section in (DD_SECTION.lower(), GROUND_SECTION.lower()):
            native_sections.setdefault(section, []).append(active.split('=', 1)[-1])
    count = 0
    for section, marker, target in ((DD_SECTION, 0x01000400, 0x57530000),
                                     (GROUND_SECTION, 0x01000001, 0x57030000)):
        for turns in range(4):
            row = f'0x{_rotate(marker, turns):08x},0x{_rotate(0x02000200, turns):08x},0x{target:08x},{turns},0'
            require(native_sections.get(section.lower(), []).count(row) == 1,
                    'Existing native orthogonal RUL1 solution changed')
            count += 1
    rows = [re.sub(r'\s+', '', line.split(';', 1)[0]).lower()
            for line in controller[RUL2].decode('ascii').splitlines()]
    for target in (0x57530000, 0x57030000):
        for pose in (1, 3):
            for base_pose in (1, 3):
                row = (f'0x{target:08x},{pose},0,0x57000000,{base_pose},0='
                       f'0x{target:08x},{pose},0,0x{target:08x},{pose},0')
                require(rows.count(row) == 1, 'Native orthogonal continuation row changed')
    return {'native_rul0_sha256': NATIVE_RUL0_SHA256, 'native_starters_checked': 2,
            'native_rul1_sha256': NATIVE_RUL1_SHA256, 'existing_native_rul1_solutions_checked': count,
            'native_rul2_sha256': NATIVE_RUL2_SHA256, 'native_continuation_rows_checked': 8,
            'native_rul1_unchanged': True, 'native_rul2_unchanged': True, 'game_behavior_tested': False}


# Public numeric boundary measurements, rather than proprietary PATH bytes.
# The two native DD corner stubs at ground level do not reach tile edges and
# are not part of the orthogonal elevated carriageway boundary.
_NATIVE_BOUNDARY_MEASUREMENTS = {
    0x57530000: (
        (1, 0, 1, 3, 0, ((-2.5, 8.0, 15.0), (-2.5, -8.0, 15.0))),
        (1, 1, 1, 3, 0, ((2.5, 8.0, 15.0), (2.5, -8.0, 15.0))),
        (1, 0, 3, 1, 0, ((2.5, -8.0, 7.5), (2.5, 8.0, 7.5))),
        (1, 1, 3, 1, 0, ((-2.5, -8.0, 7.5), (-2.5, 8.0, 7.5))),
    ),
    0x57030000: (
        (1, 1, 1, 3, 0, ((-2.5, 8.0, 0.0), (-2.5, -8.0, 0.0))),
        (1, 2, 1, 3, 0, ((2.5, 8.0, 0.0), (2.5, -8.0, 0.0))),
    ),
}


def _rotate_point(point, turns):
    east, north, height = point
    for _ in range(turns % 4):
        east, north = north, -east
    return east, north, height


def _native_boundary_routes(target, donors):
    from scp.verify import parse_paths
    expected = [dict(zip(('transport', 'lane', 'entry', 'exit', 'compatibility', 'points'), row))
                for row in _NATIVE_BOUNDARY_MEASUREMENTS[target]]
    if donors is None:
        return expected
    key = (0x296678F7, 0xA966883F, target)
    require(key in donors and hashlib.sha256(donors[key]).hexdigest()
            == NATIVE_DEPENDENCY_SHA256[key], 'Native boundary PATH identity changed or is missing')
    actual = [route for route in parse_paths(donors[key])['routes']
              if route['transport'] == 1 and {route['entry'], route['exit']} == {1, 3}]
    require(actual == [{**route, 'points': list(route['points'])} for route in expected],
            'Native boundary lane, compatibility, direction, or numeric measurement changed')
    return actual


def _boundary_members(routes, cell, edge):
    result = {}
    for route in routes:
        if route['transport'] != 1:
            continue
        for field, direction, index, other in (('entry', 'in', 0, 1), ('exit', 'out', -1, -2)):
            if route[field] != edge:
                continue
            point = route['points'][index]
            adjacent = route['points'][other]
            tangent = tuple((adjacent[axis] - point[axis]) if direction == 'in'
                            else (point[axis] - adjacent[axis]) for axis in range(3))
            length = math.sqrt(sum(value * value for value in tangent))
            require(length > 0.0 and all(math.isfinite(value) for value in (*point, *tangent)),
                    'Native boundary contains a degenerate or non-finite tangent')
            key = (route['transport'], route['lane'], route['compatibility'], direction)
            require(key not in result, 'Native socket repeats a boundary lane class')
            result[key] = {'point': (point[0] + 16.0 * cell[0], point[1] - 16.0 * cell[1], point[2]),
                           'tangent': tuple(value / length for value in tangent)}
    return result


def check_native_boundary_paths(context, piece, resources):
    """Match saved outer lanes to native sockets, all rotations, and RUL2.

    ``context`` accepts the writer's nested donor maps, the verifier's flat
    donor map, or ``None``. Portable verification without native inputs uses
    the pinned public measurements above, and explicitly reports that scope.
    It still checks every actual saved custom endpoint, lane class, direction,
    compatibility value, tangent, and native propagation/phase expectation.
    """
    from scp.verify import parse_paths
    from .native import rotate_route

    declared = approaches(piece)
    require(declared, 'Native boundary verification requires an opted-in reviewed transition')
    reviewed_variant = variant(piece)
    if context is None:
        donors = None
    elif any(isinstance(key, tuple) for key in context):
        donors = context
    else:
        donors = {}
        for label in ('controller', 'dd_rhw', 'rhw4'):
            require(isinstance(context.get(label), dict), 'Native boundary donor context is incomplete')
            donors.update(context[label])
    continuation = check_native_continuation(donors) if donors is not None else None
    native = {target: _native_boundary_routes(target, donors) for target in _NATIVE_BOUNDARY_MEASUREMENTS}
    endpoint_checks, propagation, sockets = 0, [], []
    # NAM stores the propagation templates on a horizontal pair. Its four
    # proper rotations cover both ends of a vertical or horizontal native
    # line, and both orientations of the undifferentiated RHW drag tool.
    rule_templates = {(target, pose, base_pose)
                      for target in (0x57530000, 0x57030000)
                      for pose in (1, 3) for base_pose in (1, 3)}
    vectors = ((1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 1, 0))
    outward_vectors = ((-1, 0, 0), (0, 1, 0), (1, 0, 0), (0, -1, 0))
    for declaration in declared:
        target, pose = int(declaration['native_tile_id'], 16), declaration['native_rotation']
        core_key = (0x296678F7, 0xA966883F, int(declaration['end_tile_id'], 16))
        require(core_key in resources, 'Saved transition omits a native socket owner PATH')
        core_routes = parse_paths(resources[core_key])['routes']
        core = _boundary_members(core_routes, declaration['end_cell'], declaration['outward_edge'])
        helper_routes = [rotate_route(route, pose) for route in native[target]]
        helper = _boundary_members(helper_routes, declaration['cell'], (declaration['outward_edge'] + 2) % 4)
        require(len(core) == len(helper) == (4 if target == 0x57530000 else 2),
                'Saved native socket has an incomplete or extra car boundary')
        marker = 0x01000400 if target == 0x57530000 else 0x01000001
        require(int(declaration['networks'][0]['flags'], 16) == _rotate(marker, pose),
                'Native socket marker disagrees with its directed donor pose')
        for turns in range(4):
            actual_pose = (pose + turns) % 4
            require(_rotate(int(declaration['networks'][0]['flags'], 16), turns)
                    == _rotate(marker, actual_pose), 'Rotated native socket changes lane phase')
            for key, actual in core.items():
                opposite = (*key[:3], 'out' if key[3] == 'in' else 'in')
                require(opposite in helper, 'Native socket has an incompatible lane class or travel direction')
                expected = helper[opposite]
                require(math.dist(_rotate_point(actual['point'], turns), _rotate_point(expected['point'], turns)) <= 2e-6
                        and math.dist(_rotate_point(actual['tangent'], turns), _rotate_point(expected['tangent'], turns)) <= 2e-6,
                        'Native socket endpoint or travel tangent does not meet the saved custom boundary')
                endpoint_checks += 1
            outward = _rotate_point(outward_vectors[declaration['outward_edge']], turns)
            quarter = vectors.index(outward)
            for base_pose in ((quarter + 1) % 2, (quarter + 1) % 2 + 2):
                original_pose = (actual_pose - quarter) % 4
                original_base = (base_pose - quarter) % 4
                require((target, original_pose, original_base) in rule_templates,
                        'Native RUL2 does not cover this socket end or RHW drag orientation')
                propagation.append({'native_tile_id': f'{target:08x}', 'piece_rotation': turns,
                                    'outside_cell': declaration['cell'], 'outward_step_en': list(outward[:2]),
                                    'native_pose': actual_pose, 'basic_rhw_pose': base_pose,
                                    'template_native_pose': original_pose, 'template_basic_rhw_pose': original_base})
        sockets.append({'cell': declaration['cell'], 'end_cell': declaration['end_cell'],
                        'native_tile_id': f'{target:08x}', 'native_pose': pose,
                        'boundary_members': len(core), 'lane_classes': sorted({key[1] for key in core}),
                        'members': [{'transport': key[0], 'lane': key[1], 'compatibility': key[2],
                                     'direction': key[3], 'endpoint_m': list(value['point']),
                                     'travel_tangent': list(value['tangent'])} for key, value in sorted(core.items())]})
    paired = []
    for original_turns in range(4):
        mirrored_turns = (original_turns + 2) % 4
        first = [rotate_route(route, original_turns) for route in native[0x57530000]]
        second = [rotate_route(route, (2 + mirrored_turns) % 4) for route in native[0x57530000]]
        require(first == second, 'Facing transition variants disagree on the directed native DD line')
        paired.append({'original_rotation': original_turns, 'mirrored_rotation': mirrored_turns,
                       'shared_native_dd_pose': original_turns, 'directed_lane_members': 4})
    return {'transition_variant': reviewed_variant, 'sockets_checked': len(sockets),
            'boundary_members_checked': sum(row['boundary_members'] for row in sockets),
            'proper_rotations_checked': 4, 'rotated_boundary_member_checks': endpoint_checks,
            'native_rul2_oriented_propagation_checks': len(propagation),
            'native_input_scope': 'reread-pinned-native-resources' if donors is not None else 'pinned-public-numeric-measurements',
            'native_controller_reread': donors is not None, 'native_continuation': continuation,
            'sockets': sockets, 'oriented_propagation': propagation, 'paired_facing_dd_phases': paired,
            'in_game_dragging_tested': False, 'in_game_travel_tested': False}
