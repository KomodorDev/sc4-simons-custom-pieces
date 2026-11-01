"""Experimental movable native approaches outside reviewed custom DD ends.

The existing custom end cells remain static and keep every allocated resource.
An optional, unmodelled construction cell requests a native diagonal DD tile
through the same asymmetric Monorail marker used by NAM's DD starter. This
uses RUL1, because the NAM DLL masks an immovable RUL2 neighbour's tile ID.
The new diagonal marker combinations have no match in the pinned NAM 50
controller. Placement, redraw, and actual external traffic remain untested.
"""
from __future__ import annotations

from dataclasses import dataclass
from copy import deepcopy
import hashlib
import math
import re

from scp.dbpf import require

RUL1_SECTION = 'MonoRailDirtRoadIntersectionSolutions'
NATIVE_RUL1_SHA256 = '4e44ec44283de6fccc3cd40492fc24154d13fb16a5150e13c201c6e615bba998'
NATIVE_DIAGONAL_TILE = 0x57530900
NATIVE_ARCHIVE_SHA256 = 'ccf8dabd3930fce92d0baa872ff974e3a536ddcc40762505a2e70eafcf9c0dfb'
# The native exemplar uses one 0x27812820 model reference, not five custom
# zoom-specific models. These are the three actual resources in that file.
NATIVE_DEPENDENCY_SHA256 = {
    (0x5AD0E817, 0xBADB57F1, NATIVE_DIAGONAL_TILE):
        'd319f9bb39e21e319f5ce566c5093ba9e955c4c0ed5a5dcbb703c6afe127c93a',
    (0x296678F7, 0xA966883F, NATIVE_DIAGONAL_TILE):
        'bd5435abd7e1f8360b3b8704eab474112330d8b7719333863e5bd264216415ce',
    (0x6534284A, 0x6BE08658, NATIVE_DIAGONAL_TILE):
        'd8c35e3673dee409fcc007c6adafcd193d50f551bffe473b70ef11c753cb63a9',
}

# Literal native-marker rotations, in RUL1's Monorail, DirtRoad order.
# 57530900 pose 0 carries the two opposing decks through the E/S half-cell.
# The custom end carries the complementary W/N half-cell: its 00000301
# flags must not be copied to the outside approach in the same pose.
SOLUTIONS = (
    (0x01000400, 0x03010000, NATIVE_DIAGONAL_TILE, 0, 0),
    (0x00040001, 0x01000003, NATIVE_DIAGONAL_TILE, 1, 0),
    (0x04000100, 0x00000301, NATIVE_DIAGONAL_TILE, 2, 0),
    (0x00010004, 0x00030100, NATIVE_DIAGONAL_TILE, 3, 0),
)


@dataclass(frozen=True)
class _End:
    piece_id: str
    recipe: str
    tile: int
    cell: tuple[int, int]
    edge: int
    approach: tuple[int, int]


ENDS = (
    _End('ddrhw-diagonal-upper-exit-branch', 'highway_ddrhw_compact_upper_exit_branch',
         0x7F593020, (0, 2), 0, (-1, 2)),
    _End('ddrhw-diagonal-upper-entry-branch', 'highway_ddrhw_compact_upper_entry_branch',
         0x7F594200, (2, 0), 1, (2, -1)),
    _End('ddrhw-modular-highway-stamp', 'highway_ddrhw_modular_stamp',
         0x7F59D090, (0, 9), 0, (-1, 9)),
    _End('ddrhw-modular-highway-stamp', 'highway_ddrhw_modular_stamp',
         0x7F59D900, (9, 0), 1, (9, -1)),
    _End('ddrhw-parallel-upper-exit-slip', 'highway_ddrhw_parallel_upper_exit_slip',
         0x7F5B3010, (0, 1), 0, (-1, 1)),
    _End('ddrhw-parallel-upper-entry-slip', 'highway_ddrhw_parallel_upper_entry_slip',
         0x7F5B4100, (1, 0), 1, (1, -1)),
    _End('ddrhw-parallel-b-upper-exit-slip', 'highway_ddrhw_parallel_b_upper_exit_slip',
         0x7F5C7020, (0, 2), 0, (-1, 2)),
    _End('ddrhw-parallel-b-upper-entry-slip', 'highway_ddrhw_parallel_b_upper_entry_slip',
         0x7F5C8200, (2, 0), 1, (2, -1)),
)


def _number(value):
    return int(value, 16) if isinstance(value, str) else value


def approaches(piece):
    """Return fresh, source-bound metadata; these cells own no custom model."""
    if 'native_dd_approaches' not in piece:
        return []
    require(type(piece['native_dd_approaches']) is bool,
            'native_dd_approaches must be an exact boolean')
    if not piece['native_dd_approaches']:
        return []
    selected = [end for end in ENDS if end.piece_id == piece.get('id')]
    require(selected, 'No reviewed native DD approach exists for this piece')
    require(piece.get('domain') == 'highway', 'DD approach owner must be a highway piece')
    cells = list(map(tuple, piece['cells']))
    tiles = list(map(_number, piece['tile_ids']))
    require(len(cells) == len(tiles) and len(set(cells)) == len(cells),
            'DD approach owner has an invalid tile/cell binding')
    bindings = dict(zip(cells, tiles))
    result = []
    for end in selected:
        require(piece.get('recipe') == end.recipe and bindings.get(end.cell) == end.tile,
                'DD approach no longer names its exact reviewed exterior tile')
        require(end.approach not in bindings and
                (end.approach[0] < 0 or end.approach[1] < 0),
                'A DD approach must stay outside the retained custom footprint')
        result.append({'cell': list(end.approach), 'end_cell': list(end.cell),
                       'end_tile_id': f'{end.tile:08x}', 'outward_edge': end.edge,
                       'native_tile_id': f'{NATIVE_DIAGONAL_TILE:08x}', 'native_rotation': 0,
                       'monorail_flags': '01000400', 'dirtroad_flags': '03010000',
                       'optional': True, 'experimental': True})
    return result


def solution_rows(pieces):
    """Four proper rotations, selected once, with no reflected alternatives."""
    selected = [approaches(piece) for piece in pieces]
    return SOLUTIONS if any(selected) else ()


def rul1_rows(piece):
    """Provider hook: exact (Monorail, DirtRoad, target, rotation, flip) rows."""
    return SOLUTIONS if approaches(piece) else ()


def rul1_delta(pieces, native_rul1):
    """Bind the four new solutions to the exact native NAM 50 RHD input.

    The caller inserts these rows inside the existing named section and
    preserves the remainder of the resource. A second section is not valid.
    """
    rows = solution_rows(pieces)
    if not rows:
        return None
    require(hashlib.sha256(native_rul1).hexdigest() == NATIVE_RUL1_SHA256,
            'DD approaches require the pinned native NAM 50 RUL1')
    text = native_rul1.decode('ascii')
    header = re.search(r'^\[' + RUL1_SECTION + r'\][ \t]*\r?$', text, re.I | re.M)
    require(header is not None, 'Native RUL1 lacks its Monorail/DirtRoad section')
    next_header = text.find('[', header.end())
    section = text[header.end():next_header if next_header >= 0 else len(text)]
    existing = set()
    for match in re.finditer(r'^\s*TYPE\w*\s*=\s*0x([0-9a-f]+)\s*,\s*0x([0-9a-f]+)',
                             section, re.I | re.M):
        existing.add((int(match[1], 16), int(match[2], 16)))
    require(not existing.intersection((mono, road) for mono, road, *_ in rows),
            'DD approach marker pair conflicts with native RUL1')
    lines = [f'TYPE{index}=0x{mono:08X},0x{road:08X},0x{target:08X},{rotation},{flip}'
             for index, (mono, road, target, rotation, flip) in enumerate(rows, 1)]
    return {'section': RUL1_SECTION, 'insertion': '\r\n'.join(lines) + '\r\n',
            'base_sha256': NATIVE_RUL1_SHA256, 'solution_count': len(rows),
            'game_behavior_tested': False}


def add_approaches(piece, layout, checks, constraints):
    """Pad check-only cells around unchanged anchors and static ownership.

    ``^`` fixes the original column, and ``<`` fixes the original row. Moving
    both anchors with their existing rows preserves all original coordinates
    when a new negative-coordinate approach needs top or left padding.
    """
    declared = approaches(piece)
    if not declared:
        return list(layout), list(checks), list(constraints)
    rows, cons = [list(row) for row in layout], [list(row) for row in constraints]
    require(rows and len(rows) == len(cons) and
            len({len(row) for row in rows + cons}) == 1,
            'DD approaches require equally sized construction grids')
    origins_x = [x for row in rows for x, symbol in enumerate(row) if symbol == '^']
    origins_y = [y for y, row in enumerate(rows) for symbol in row if symbol == '<']
    require(len(origins_x) == len(origins_y) == 1,
            'DD approaches require the original unique construction anchors')
    ox, oy = origins_x[0], origins_y[0]
    require(cons[oy].count('<') == 1 and
            any(len(row) > ox and row[ox] == '^' for row in cons),
            'DD approaches cannot move inconsistent construction anchors')
    left = max(0, -min(ox + row['cell'][0] for row in declared))
    top = max(0, -min(oy + row['cell'][1] for row in declared))
    width, depth = len(rows[0]) + left, len(rows) + top
    width = max(width, max(ox + left + row['cell'][0] + 1 for row in declared))
    depth = max(depth, max(oy + top + row['cell'][1] + 1 for row in declared))
    def padded(source):
        target = [['.'] * width for _ in range(depth)]
        for y, row in enumerate(source):
            target[y + top][left:left + len(row)] = row
        return target
    rows, cons = padded(rows), padded(cons)
    used = {symbol for row in rows for symbol in row if symbol.isalpha()}
    palette = list(checks)
    for declaration in declared:
        available = next((symbol for symbol in reversed('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                          if symbol not in used), None)
        require(available is not None, 'No unused DD approach construction symbol remains')
        x, y = declaration['cell']
        x, y = ox + left + x, oy + top + y
        require(rows[y][x] == cons[y][x] == '.',
                'A DD outside approach collides with an existing construction cell or anchor')
        rows[y][x] = available
        used.add(available)
        palette.append(f'{available} - dirtroad: 0x03010000 monorail: 0x01000400, 0xFFFFFFFF optional')
    return [''.join(row) for row in rows], palette, [''.join(row) for row in cons]


def check_construction_approaches(fields, piece):
    """Check actual helper fields, then restore only the legacy check grids.

    This verifier does not regenerate the construction. The caller must run
    its existing exact static/adaptive construction verifier on the returned
    fields, using a piece copy without ``native_dd_approaches``. All other
    fields, including AutoTileBase and preview, pass through unchanged.
    """
    declared = approaches(piece)
    result = deepcopy(fields)
    if not declared:
        return result
    rows = [list(row) for row in fields['CellLayout']]
    cons = [list(row) for row in fields['ConsLayout']]
    left = max(0, -min(row['cell'][0] for row in declared))
    top = max(0, -min(row['cell'][1] for row in declared))
    width, depth = piece['footprint']
    require(len(rows) == len(cons) == depth + 1 + top and
            all(len(row) == width + 2 + left for row in rows + cons),
            'DD approach construction changes the exact padded grid extent')
    for grid in (rows, cons):
        require([(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == '^']
                == [(left, depth + top)] and
                [(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == '<']
                == [(width + 1 + left, top)],
                'DD approach construction moves the original coordinate anchors')
    palette = list(fields['CheckType'])
    removed = set()
    normalized = lambda text: re.sub(r'\s+', '', text).lower()
    for declaration in declared:
        x, y = declaration['cell']
        x, y = x + left, y + top
        symbol = rows[y][x]
        require(symbol.isascii() and symbol.isalpha() and symbol not in removed and cons[y][x] == '.',
                'DD outside approach is missing, repeated, or statically modelled')
        matching = [line for line in palette if re.match(r'^\s*' + re.escape(symbol) + r'\s*-', line)]
        require(len(matching) == 1 and normalized(matching[0]) == normalized(
            f'{symbol} - dirtroad: 0x03010000 monorail: 0x01000400, 0xFFFFFFFF optional'),
            'DD outside approach changes its exact optional native flags')
        require(sum(line.count(symbol) for line in rows) == 1,
                'A DD optional approach symbol is also used on another cell')
        rows[y][x] = '.'
        removed.add(symbol)
        palette.remove(matching[0])
    require(all(char == '.' for y, line in enumerate(rows) for x, char in enumerate(line)
                if x < left or y < top) and
            all(char == '.' for y, line in enumerate(cons) for x, char in enumerate(line)
                if x < left or y < top),
            'DD approach padding contains an undeclared construction cell')
    result['CellLayout'] = [''.join(line[left:]) for line in rows[top:]]
    result['ConsLayout'] = [''.join(line[left:]) for line in cons[top:]]
    result['CheckType'] = palette
    return result


def check_helper_collisions(pieces, scene):
    """Reject an approach over any retained component in each actual pose."""
    def world(cell, pose):
        angle = pose.get('rotation_degrees_ccw', pose.get('rotation_degrees', 0))
        require(type(angle) is int and angle % 90 == 0, 'DD approach pose is not a proper quarter turn')
        origin = pose['origin_m']
        require(len(origin) == 2 and all(type(v) in (int, float) and math.isfinite(v)
                and abs(v / 16. - round(v / 16.)) < 1e-9 for v in origin),
                'DD approach pose must lie on the city-cell lattice')
        x, north = cell[0], -cell[1]
        for _ in range((angle // 90) % 4):
            x, north = -north, x
        return round(origin[0] / 16.) + x, round(origin[1] / 16.) + north
    occupied, helpers = {}, []
    for index, pose in enumerate(scene['placements']):
        piece = pieces[pose['piece_id']]
        for cell in piece['cells']:
            at = world(cell, pose)
            require(at not in occupied, 'DD approach scene duplicates custom ownership')
            occupied[at] = index
        helpers.extend((index, world(row['cell'], pose)) for row in approaches(piece))
    require(len({cell for _, cell in helpers}) == len(helpers),
            'Two DD outside approaches occupy the same construction cell')
    require(not any(cell in occupied for _, cell in helpers),
            'A DD outside approach overlaps another retained custom component')
    return {'passed': True, 'outside_approaches_checked': len(helpers),
            'custom_cells_checked': len(occupied), 'game_behavior_tested': False}


def check_selected_helper_collisions(pieces, scene):
    """Keep historical assembly reports unchanged without the explicit opt-in."""
    return (check_helper_collisions(pieces, scene)
            if any(approaches(pieces[pose['piece_id']]) for pose in scene['placements']) else None)
