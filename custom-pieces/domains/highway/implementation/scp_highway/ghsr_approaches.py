"""Four exposed native approaches for the protected diagonal DD/GHSR crossing.

The two DD half phases carry opposite deck directions. GHSR uses a distinct
Rail/Monorail false intersection. Every helper is dynamic, unowned, and
outside the two retained model cells; none establishes live-game success.
"""
from __future__ import annotations

import hashlib
import re

from scp.dbpf import require

PIECE_ID = 'ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg'
RECIPE = 'highway_ddrhw_diagonal_ghsr_crossing'
ALIGNMENT_B_PIECE_ID = 'ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b'
ALIGNMENT_B_RECIPE = 'highway_ddrhw_diagonal_ghsr_crossing_alignment_b'
OPT_IN = 'native_ghsr_approaches'
NATIVE_RUL1_SHA256 = '4e44ec44283de6fccc3cd40492fc24154d13fb16a5150e13c201c6e615bba998'
NATIVE_RUL2_SHA256 = 'c427c7872743ca4cd9f583adf33c93a320babe37c42061fbd33c905696e7a3b1'
RUL2 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000002)
NATIVE_CONTROLLER_SHA256 = {RUL2: NATIVE_RUL2_SHA256}
DD_SECTION = 'MonoRailDirtRoadIntersectionSolutions'
GHSR_SECTION = 'RailMonoRailIntersectionSolutions'

# Exact decompressed resources from the pinned NAM 50 source archives.
NATIVE_DEPENDENCY_SHA256 = {
    (0x5AD0E817, 0xBADB57F1, 0x57530900): 'd319f9bb39e21e319f5ce566c5093ba9e955c4c0ed5a5dcbb703c6afe127c93a',
    (0x296678F7, 0xA966883F, 0x57530900): 'bd5435abd7e1f8360b3b8704eab474112330d8b7719333863e5bd264216415ce',
    (0x6534284A, 0x6BE08658, 0x57530900): 'd8c35e3673dee409fcc007c6adafcd193d50f551bffe473b70ef11c753cb63a9',
    (0x5AD0E817, 0xBADB57F1, 0x57530200): '4eb082b8329ddf70be7333f3343c4f1a621985d3992b17ca624eef79dc0ee4a8',
    (0x296678F7, 0xA966883F, 0x57530200): 'e888625d239fe19f546f36f58bed998359440e889904fa4976c3aec355640eb1',
    (0x6534284A, 0x6BE08658, 0x57530200): '394c783a8fedf150c93d21701e1450a520d5c31ff59245e2d1e40ebf12889b70',
    (0x5AD0E817, 0xBADB57F1, 0x5DC01A00): '58e54d5d212e26564e5454c57b6fd3269067a7f48df81eec45925590c1a59fa6',
    (0x296678F7, 0xA966883F, 0x5DC01A00): '978a2a8c8f8e5de89e80bd6841d0b91666407efe2e77c32c312c0ff2c6353e4a',
    (0x6534284A, 0xEBE084C2, 0x5DC01A00): '3029157db99ce4334d588c4b6fb765ee3de84154b95b8d541df6d63546e8be56',
}

# The actual native diagonal GHSR model has one referenced buffer family and
# five dangling historical animation records. Preserve the donor untouched;
# do not weaken validation for any other resource or unreviewed frame.
NATIVE_IGNORED_MODEL_FRAMES = {
    (0x5AD0E817, 0xBADB57F1, 0x5DC01A00): (
        (0, 0, (0, 2, 2, 2)), (2, 0, (2, 4, 4, 4)),
        (3, 0, (0, 5, 5, 5)), (4, 0, (1, 3, 3, 3)),
        (5, 0, (0, 1, 1, 1)),
    ),
}


def _rot(value, turns):
    shift = 8 * (turns % 4)
    return ((value << shift) | (value >> ((32 - shift) % 32))) & 0xFFFFFFFF


def approaches(piece):
    if OPT_IN not in piece:
        return []
    require(type(piece[OPT_IN]) is bool, OPT_IN + ' must be an exact boolean')
    if not piece[OPT_IN]:
        return []
    alignment_b = piece.get('id') == ALIGNMENT_B_PIECE_ID and piece.get('recipe') == ALIGNMENT_B_RECIPE
    require(((piece.get('id') == PIECE_ID and piece.get('recipe') == RECIPE) or alignment_b)
            and piece.get('domain') == 'highway', 'Unreviewed native DD/GHSR approach owner')
    expected_cells = [[0, 0], [1, 0]] if alignment_b else [[0, 0], [0, 1]]
    expected_footprint = [2, 1] if alignment_b else [1, 2]
    require(piece.get('footprint') == expected_footprint and piece.get('cells') == expected_cells,
            'Native DD/GHSR approaches require the reviewed two-cell crossing')
    require(not piece.get('native_dd_approaches'), 'DD/GHSR helpers must not duplicate legacy DD helpers')
    tiles = piece.get('tile_ids', [])
    require(len(tiles) == 2 and all(isinstance(tile, str) and re.fullmatch('[0-9a-fA-F]{8}', tile)
                                  for tile in tiles), 'Invalid crossing cell identifiers')
    bindings = (
        # cell, owning end, outward edge, native target, native pose, section,
        # first name/flags, second name/flags, exemplar group, model reference.
        ((1, 0), 0, 2, 0x57530900, 2, DD_SECTION,
         'monorail', 0x04000100, 'dirtroad', 0x00000301, 0x6BE08658, 'rkt0'),
        ((-1, 1), 1, 0, 0x57530200, 0, DD_SECTION,
         'monorail', 0x04000100, 'dirtroad', 0x03010000, 0x6BE08658, 'rkt0'),
        ((-1, 0), 0, 0, 0x5DC01A00, 1, GHSR_SECTION,
         'rail', 0x01010000, 'monorail', 0x00030100, 0xEBE084C2, 'rkt1'),
        ((1, 1), 1, 2, 0x5DC01A00, 3, GHSR_SECTION,
         'rail', 0x00000101, 'monorail', 0x01000003, 0xEBE084C2, 'rkt1'),
    )
    if alignment_b:
        bindings = (
            ((0, 1), 0, 3, 0x57530900, 2, DD_SECTION,
             'monorail', 0x04000100, 'dirtroad', 0x00000301, 0x6BE08658, 'rkt0'),
            ((1, -1), 1, 1, 0x57530200, 0, DD_SECTION,
             'monorail', 0x04000100, 'dirtroad', 0x03010000, 0x6BE08658, 'rkt0'),
            ((0, -1), 0, 1, 0x5DC01A00, 3, GHSR_SECTION,
             'rail', 0x00000101, 'monorail', 0x01000003, 0xEBE084C2, 'rkt1'),
            ((1, 1), 1, 3, 0x5DC01A00, 1, GHSR_SECTION,
             'rail', 0x01010000, 'monorail', 0x00030100, 0xEBE084C2, 'rkt1'),
        )
    result = []
    for cell, end, edge, target, pose, section, first, a, second, b, group, reference in bindings:
        result.append({'cell': list(cell), 'end_cell': expected_cells[end], 'end_tile_id': tiles[end].lower(),
                       'outward_edge': edge, 'native_tile_id': f'{target:08x}', 'native_rotation': pose,
                       'section': section, 'networks': [{'name': first, 'flags': f'{a:08x}'},
                                                      {'name': second, 'flags': f'{b:08x}'}],
                       'native_exemplar_group': f'{group:08x}', 'native_model_reference': reference,
                       'optional': True, 'experimental': True})
    return result


def rul1_sections(piece):
    if not approaches(piece):
        return {}
    return {
        DD_SECTION: tuple((_rot(marker, turns), _rot(0x03010000, turns), target, turns, 0)
                          for marker, target in ((0x01000400, 0x57530900),
                                                 (0x04000100, 0x57530200)) for turns in range(4)),
        GHSR_SECTION: tuple((_rot(0x00010100, turns), _rot(0x00000301, turns),
                             0x5DC01A00, turns, 0) for turns in range(4)),
    }


def add_approaches(piece, layout, checks, constraints):
    """Pad only the helper side; preserve the modeled origin and both IDs."""
    declared = approaches(piece)
    if not declared:
        return list(layout), list(checks), list(constraints)
    alignment_b = piece.get('id') == ALIGNMENT_B_PIECE_ID
    expected_layout = ['ab<', '...', '^..'] if alignment_b else ['a.<', 'b..', '^..']
    expected_constraints = ['++<', '...', '^..'] if alignment_b else ['+.<', '+..', '^..']
    require(list(layout) == expected_layout and list(constraints) == expected_constraints,
            'DD/GHSR helpers require the exact two-cell construction grid')
    if alignment_b:
        rows = [list('...'), *map(list, layout)]
        cons = [list('...'), *map(list, constraints)]
    else:
        rows, cons = [list('.' + row) for row in layout], [list('.' + row) for row in constraints]
    palette, used = list(checks), {char for row in rows for char in row if char.isalpha()}
    for row in declared:
        symbol = next(char for char in 'hijk' if char not in used)
        used.add(symbol)
        x, y = ((row['cell'][0], row['cell'][1] + 1) if alignment_b
                else (row['cell'][0] + 1, row['cell'][1]))
        require(rows[y][x] == cons[y][x] == '.', 'A native helper collides with an owned construction cell')
        rows[y][x] = symbol
        flags = ' '.join(f"{item['name']}: 0x{item['flags'].upper()}" for item in row['networks'])
        # A full mask on the second entry mirrors NAM's DD starter and makes
        # each exact pair explicit without accepting a broad fallback.
        palette.append(f'{symbol} - {flags}, 0xFFFFFFFF optional')
    return [''.join(row) for row in rows], palette, [''.join(row) for row in cons]


def check_native_continuation(controller):
    """Audit actual native RUL2 continuation beyond each seeded helper family."""
    require(RUL2 in controller and hashlib.sha256(controller[RUL2]).hexdigest() == NATIVE_RUL2_SHA256,
            'DD/GHSR approaches require the pinned native NAM 50 RUL2')
    rows = [line.split(';', 1)[0].strip().lower() for line in controller[RUL2].decode('ascii').splitlines()]
    expected = (
        '0x5dc01a00,1,0,0x0d001a00,1,0=0x5dc01a00,1,0,0x5dc01a00,3,0',
        '0x5dc01a00,2,0,0x0d001a00,2,0=0x5dc01a00,2,0,0x5dc01a00,0,0',
        '0x57530200,0,0,0x57000200,2,0=0x57530200,0,0,0x57530900,2,0',
        '0x57530200,3,0,0x57000200,1,0=0x57530200,3,0,0x57530900,1,0',
        '0x57530900,0,0,0x57000200,2,0=0x57530900,0,0,0x57530200,2,0',
        '0x57530900,3,0,0x57000200,1,0=0x57530900,3,0,0x57530200,1,0',
    )
    require(all(rows.count(row) == 1 for row in expected), 'Native DD/GHSR continuation rows changed')
    return {'native_rul2_sha256': NATIVE_RUL2_SHA256, 'native_continuation_rows_checked': 6,
            'native_rul2_unchanged': True, 'game_behavior_tested': False}
