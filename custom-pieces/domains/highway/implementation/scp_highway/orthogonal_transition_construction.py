"""Owned construction cells derived from the saved transition PATH channels."""
from __future__ import annotations

from scp.dbpf import require
from scp.verify import parse_paths
from .orthogonal_approaches import CORE_CELLS
from .ramp_paths import _route_metadata, construction_flags


def core_construction_data(compiled, *, mirrored=False, flat_terrain=False):
    require(type(mirrored) is bool, 'Transition construction variant must be an exact boolean')
    require(type(flat_terrain) is bool, 'Transition flat-terrain policy must be an exact boolean')
    require(tuple(cell for cell, _model, _path in compiled) == CORE_CELLS,
            'Transition construction must retain the twelve row-major cells')
    rows = [list('....') for _ in range(7)]
    cons = [list('....') for _ in range(7)]
    rows[0][3] = cons[0][3] = '<'
    rows[6][0] = cons[6][0] = '^'
    checks = []
    for index, (cell, _model, raw) in enumerate(compiled):
        x, y = cell
        symbol = chr(ord('a') + index)
        # This fixed model has one common ground datum beneath its graded
        # carriageways. In ConsLayout, '#' ties all four terrain corners;
        # '+' is ignored by the game's constraint parser. Keep the original
        # transition's legacy output, and opt the mirrored correction and
        # new opposite-side counterparts into this explicit flat-base policy.
        rows[y][x], cons[y][x] = symbol, '#' if mirrored or flat_terrain else '+'
        routes = [_route_metadata(route, 'saved') for route in parse_paths(raw)['routes']]
        checks.append(f'{symbol} - dirtroad: 0x{construction_flags(routes):08X}')
    return [''.join(row) for row in rows], checks, [''.join(row) for row in cons]
