"""Owned construction cells derived from the saved transition PATH channels."""
from __future__ import annotations

from scp.dbpf import require
from scp.verify import parse_paths
from .orthogonal_approaches import CORE_CELLS
from .ramp_paths import _route_metadata, construction_flags


def core_construction_data(compiled):
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
        rows[y][x], cons[y][x] = symbol, '+'
        routes = [_route_metadata(route, 'saved') for route in parse_paths(raw)['routes']]
        checks.append(f'{symbol} - dirtroad: 0x{construction_flags(routes):08X}')
    return [''.join(row) for row in rows], checks, [''.join(row) for row in cons]
