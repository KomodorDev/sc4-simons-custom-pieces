"""Three outside native sockets for the reviewed orthogonal DD-to-L0 ramp.

The optional cells reproduce NAM 50's original DD and RHW-4 starter
markers. They are unowned native cells, and reuse existing RUL1 solutions
and RUL2 propagators without establishing live-game success.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import re

from scp.dbpf import require

PIECE_ID = 'ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile'
RECIPE = 'highway_ddrhw_orthogonal_l0_transition'
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


def approaches(piece):
    """Bind three reviewed sockets to the actual allocated owning cells."""
    if OPT_IN not in piece:
        return []
    require(type(piece[OPT_IN]) is bool, OPT_IN + ' must be an exact boolean')
    if not piece[OPT_IN]:
        return []
    require(piece.get('id') == PIECE_ID and piece.get('recipe') == RECIPE
            and piece.get('domain') == 'highway', 'Unreviewed orthogonal approach owner')
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
