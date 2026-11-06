"""One-sided native HSR starter cells for the three trumpet approaches."""
from __future__ import annotations

from collections import defaultdict
import hashlib
from pathlib import Path
import re

from scp.dbpf import require


STRAIGHT = 'hsr-l2-two-track-straight'
SOUTH_JUNCTION = 'hsr-l2-two-track-mainline-split-merge-parallel-recessed-end'
DIVERGE = 'hsr-l2-two-track-mainline-split-oblique-cut'

# Column and southward row, relative to the custom piece's reference cell.
HELPERS = {
    (STRAIGHT, 'north'): (0, -1),
    (STRAIGHT, 'south'): (0, 1),
    (SOUTH_JUNCTION, 'south'): (1, 6),
    (DIVERGE, 'west'): (-1, 0),
}
TERMINALS = {
    'P04': (SOUTH_JUNCTION, 'south', 'S', (7, -1)),
    'P08': (DIVERGE, 'west', 'E', (19, 13)),
    'P01': (DIVERGE, 'west', 'W', (0, 13)),
}
# Frozen menus from the first terminal build still verify their original proof.
PREVIOUS_TERMINALS = {
    'P04': (SOUTH_JUNCTION, 'south', 'S', (7, -1)),
    'P09': (STRAIGHT, 'north', 'E', (20, 13)),
    'P22': (STRAIGHT, 'south', 'W', (-1, 13)),
}

# Installed NAM C215 supplies the north–south pair. The west-facing check
# uses its quarter-turn pose, also resolved to ordinary HSR by stock RUL1.
STARTER_CHECKS = {
    'north': b'CheckType = Z - monorail: 0x02000200 road: 0x00010100 optional\r\n',
    'south': b'CheckType = Z - monorail: 0x02000200 road: 0x00010100 optional\r\n',
    'west': b'CheckType = Z - monorail: 0x00020002 road: 0x01010000 optional\r\n',
}
INWARD_STEP = {'north': (0, 1), 'south': (0, -1), 'west': (1, 0)}
GRID = {field: re.compile(rb'(?m)^' + field + rb' = ([A-Za-z.+^<]+)\r\n')
        for field in (b'CellLayout', b'ConsLayout')}
CONTROLLER = (0x0A5BCF4B, 0xAA5BCF57)
NATIVE_TILE = 0x5DD31500
DEPENDENCIES = {
    'controller': ('NetworkAddonMod_Controller.dat', {
        (*CONTROLLER, 0x10000000): 'd2a63a6c9070857c5360343cfa07f0be13ef0559fd659e9545c57c15dda672b9',
        (*CONTROLLER, 0x10000001): '4e44ec44283de6fccc3cd40492fc24154d13fb16a5150e13c201c6e615bba998',
        (*CONTROLLER, 0x10000002): 'c427c7872743ca4cd9f583adf33c93a320babe37c42061fbd33c905696e7a3b1',
    }),
    'hsr': ('High Speed Rail.dat', {
        (0x5AD0E817, 0xBADB57F1, NATIVE_TILE): '00647b6415b099944955815ac5f32b6890acb4dc09e6b3082c3887e833082b25',
        (0x296678F7, 0xA966883F, NATIVE_TILE): '14ede4aca7915368d6cfbeb88e5af3e801243eb9e4becbd4a5cf9b1e1fe7a9b8',
        (0x6534284A, 0xEBE084C2, NATIVE_TILE): 'a280683a000029d779f33544950fde4ff0043e54e2368b94b60a323a98459175',
        (0x6534284A, 0x89AC5643, NATIVE_TILE): 'f7a179b4a7d32eeefd22f4571712549e93de62c450c93efb75764680ed0c9504',
    }),
}


def verify_native_inputs(context, installed, donors):
    """Require the audited native starter rules and a single provider for its tile."""
    from scp.dbpf import tgi_string

    for label, (filename, resources) in DEPENDENCIES.items():
        paths = [Path(row['path']) for row in donors if row['filename'] == filename]
        require(len(paths) == 1, f'Expected one audited HSR terminal donor {filename}')
        for key, digest in resources.items():
            require(installed.get(key) == paths, 'HSR terminal has a missing or conflicting native resource: '
                    + tgi_string(key))
            require(key in context[label] and hashlib.sha256(context[label][key]).hexdigest() == digest,
                    'HSR terminal native resource changed: ' + tgi_string(key))


def terminal_placements(scene):
    """Bind terminal selections to the exact outward cells in the saved plan."""
    for terminals in (TERMINALS, PREVIOUS_TERMINALS):
        if scene.get('terminal_approaches') == {
                label: {'helper_edge': edge, 'arm': arm, 'helper_cell_xy': list(cell)}
                for label, (_, edge, arm, cell) in terminals.items()}:
            break
    else:
        raise ValueError('Trumpet must declare its three reviewed native HSR approaches')
    placements = {row['instance_id']: row for row in scene['placements']}
    require(len(placements) == len(scene['placements']), 'Trumpet repeats a placement identifier')
    for label, (piece_id, edge, _, cell) in terminals.items():
        row = placements.get(label)
        require(row is not None and row['piece_id'] == piece_id,
                'Trumpet terminal is attached to the wrong piece')
        east, south = HELPERS[piece_id, edge]
        north = -south
        angle = row['rotation_degrees_ccw']
        require(angle in (0, 90, 180, 270), 'Unsupported trumpet terminal rotation')
        dx, dy = ((east, north), (-north, east), (-east, -north), (north, -east))[angle // 90]
        x, y = row['display_origin_tiles_en']
        require((x + dx, y + dy) == cell, 'Trumpet terminal no longer points to its outward cell')
    return {label: placements[label] for label in terminals}


def _grids(body):
    grids = {field: list(pattern.finditer(body)) for field, pattern in GRID.items()}
    count = len(grids[b'CellLayout'])
    require(count >= 3 and count == len(grids[b'ConsLayout']), 'Invalid HSR terminal layout rows')
    for rows in grids.values():
        require(all(left.end() == right.start() for left, right in zip(rows, rows[1:])),
                'HSR terminal layout rows are not contiguous')
    cell, cons = grids.values()
    width = len(cell[0][1])
    require(all(len(row[1]) == width for row in cell + cons)
            and cell[1][1].endswith(b'<') and cons[1][1].endswith(b'<')
            and cell[-1][1] == cons[-1][1] == b'.^' + b'.' * (width - 2),
            'Unexpected HSR construction anchors')
    return grids


def _helper_index(piece_id, helper_edge):
    require((piece_id, helper_edge) in HELPERS, 'Unreviewed HSR terminal piece or edge')
    column, row = HELPERS[piece_id, helper_edge]
    return column + 1, row + 1  # HSR generated layouts start with one padding row and column.


def terminal_body(piece_id, helper_edge, body: bytes) -> bytes:
    """Add the optional seed while keeping the same static cells and addresses."""
    x, y = _helper_index(piece_id, helper_edge)
    grids = _grids(body)
    cell, cons = grids.values()
    require(not re.search(rb'(?m)^CheckType = Z\b', body) and all(b'Z' not in row[1] for row in cell),
            'HSR terminal marker is already in use')
    dx, dy = INWARD_STEP[helper_edge]
    require(y < len(cell) and cell[y][1][x:x + 1] == cons[y][1][x:x + 1] in (b'.', b'^')
            and cell[y + dy][1][x + dx:x + dx + 1].isalpha(),
            'HSR helper must border its own unoccupied terminal cell')
    move_caret = y == len(cell) - 1
    for field, rows in reversed(list(grids.items())):
        row = rows[y]
        value = b'.' * len(row[1]) if move_caret else row[1]
        if field == b'CellLayout':
            value = value[:x] + b'Z' + value[x + 1:]
        line = field + b' = ' + value + b'\r\n'
        if move_caret:
            line += row[0]
        body = body[:row.start()] + line + body[row.end():]
    checks = list(re.finditer(rb'(?m)^CheckType = [^\r\n]+\r\n', body))
    require(checks, 'HSR terminal source has no owned network flags')
    end = checks[-1].end()
    return body[:end] + STARTER_CHECKS[helper_edge] + body[end:]


def verify_terminal_body(piece_id, helper_edge, original: bytes, actual: bytes, *, piece):
    """Read the saved marker and recover every byte of the original body."""
    from scp.verify import check_emitted_runtime_addresses, parse_rules

    x, y = _helper_index(piece_id, helper_edge)
    old_cell = _grids(original)[b'CellLayout']
    cell, cons = _grids(actual).values()
    require(y < len(old_cell), 'Canonical HSR terminal has no outward row')
    moved = y == len(old_cell) - 1
    starter = STARTER_CHECKS[helper_edge]
    require(len(cell) == len(old_cell) + moved and actual.count(starter) == 1
            and sum(row[1].count(b'Z') for row in cell) == 1 and cell[y][1][x:x + 1] == b'Z'
            and cons[y][1][x:x + 1] == b'.',
            'Saved HSR terminal marker, optional flags, or ownership changed')
    require(piece['id'] == piece_id, 'Saved HSR terminal is bound to the wrong allocation')
    _, sections = parse_rules('[HighwayIntersectionInfo_0x00000001]' + actual.decode('ascii'))
    fields = defaultdict(list)
    for key, value in sections[1]:
        fields[key].append(value)
    check_emitted_runtime_addresses(fields, piece)
    if moved:
        padding = b'.' * len(cell[y][1])
        require(cons[y][1] == padding and cell[y][1] == padding[:x] + b'Z' + padding[x + 1:],
                'Saved HSR terminal adds another cell in its padding row')
        actual = actual[:cons[y].start()] + actual[cons[y].end():]
        actual = actual[:cell[y].start()] + actual[cell[y].end():]
    else:
        marker = cell[y].start(1) + x
        actual = actual[:marker] + b'.' + actual[marker + 1:]
    require(actual.replace(starter, b'', 1) == original,
            'Saved HSR terminal changes canonical construction or asset references')
