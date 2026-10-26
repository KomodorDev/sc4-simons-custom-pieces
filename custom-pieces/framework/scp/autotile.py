"""Check the executable's puzzle-model lookup without importing the catalog.

The Windows 1.1.641 executable creates a byte key for each modeled cell:
``((row << 4) + column + 1) & 0xff``.  It maps that key to the additive offset
``column * 256 + row * 16``.  Repeated keys overwrite earlier offsets in
row-major order.  Changing AutoTileBase cannot repair these collisions.

In that executable, the lookup builder is at 0x609fc0; key creation is at
0x60a3e6, offset storage at 0x60a4b6,
and the final base-plus-offset ADD at 0x62c45d.  Model zoom variants use offsets
0–4 in the otherwise clear low nibble.
"""
from __future__ import annotations

from collections.abc import Mapping
import re


UINT32_MAX = 0xffffffff


class AutoTileAddressError(ValueError):
    """An unsafe allocation, with its JSON-serializable diagnostic report."""

    def __init__(self, report):
        self.report = report
        details = '; '.join(report['errors'])
        super().__init__(f"{report['piece']}: unsafe auto-tile addresses: {details}")


def _integer(value, label):
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f'{label} must be an integer')
    if not 0 <= value <= UINT32_MAX:
        raise ValueError(f'{label} must fit an unsigned 32-bit integer')
    return value


def _identifier(value, label):
    if isinstance(value, str):
        if re.fullmatch(r'[0-9a-fA-F]{1,8}', value) is None:
            raise ValueError(f'{label} must be 1–8 hexadecimal digits')
        value = int(value, 16)
    return _integer(value, label)


def game_tile_id(base, column, row):
    """Return the intended additive ID, before full-grid lookup collisions.

    ``column`` and ``row`` are offsets from the modeled bounding-box origin.
    The actual runtime selection depends on every modeled cell; use
    :func:`resolve_game_tile_ids` when simulating a complete placement.
    """
    base = _integer(base, 'base')
    column = _integer(column, 'column')
    row = _integer(row, 'row')
    address = base + (column << 8) + (row << 4)
    if address > UINT32_MAX:
        raise ValueError('base plus coordinate offset must fit an unsigned 32-bit integer')
    return address


def engine_grid_key(column, row):
    """Return the executable's byte key, including column carry and wrapping."""
    column = _integer(column, 'column')
    row = _integer(row, 'row')
    return ((row << 4) + column + 1) & 0xff


def _resolve_cells(cells):
    if not isinstance(cells, (list, tuple)) or not cells:
        raise ValueError('cells must be a nonempty sequence of coordinate pairs')
    placements = []
    for index, cell in enumerate(cells):
        if not isinstance(cell, (list, tuple)) or len(cell) != 2:
            raise ValueError(f'cell {index} must be a coordinate pair')
        placements.append(tuple(_integer(value, f'cell {index} coordinate') for value in cell))
    if len(set(placements)) != len(placements):
        raise ValueError('occupied cells contain duplicate placements')
    origin = min(x for x, y in placements), min(y for x, y in placements)
    keys, winners = {}, {}
    for cell in sorted(placements, key=lambda cell: (cell[1], cell[0])):
        key = engine_grid_key(cell[0] - origin[0], cell[1] - origin[1])
        keys[cell] = key
        winners[key] = cell
    return placements, origin, keys, winners


def resolve_game_tile_ids(base, cells):
    """Return actual selected IDs for a complete physical-cell placement.

    ``cells`` contains modeled cells only; check-only and optional network
    cells are excluded.  Coordinates may arrive in any order.  The engine
    subtracts the modeled bounding-box minimum, then builds its byte-key map
    in row-major order, so later cells with a repeated key win.  Dictionary
    keys retain the supplied physical coordinates.
    """
    base = _integer(base, 'base')
    placements, origin, keys, winners = _resolve_cells(cells)
    return {cell: game_tile_id(base, winners[keys[cell]][0] - origin[0],
                              winners[keys[cell]][1] - origin[1])
            for cell in placements}


def validate_auto_tile_addresses(piece):
    """Return an address report, or raise ``AutoTileAddressError`` with it.

    ``footprint`` is [columns, rows].  Optional ``cells`` lists occupied
    [column, row] pairs; otherwise the footprint is filled in row-major order.
    ``tile_ids`` contains their allocated IDs, as integers or hexadecimal
    strings.  The required AutoTileBase is inferred from the first allocation
    using coordinates relative to the modeled bounding-box minimum.  Empty
    borders do not consume runtime offsets.  The emitted-rule verifier must
    separately check that the actual AutoTileBase matches this required base.
    Actual selection is resolved through the executable's byte-key map.
    Legacy mask report fields are descriptive
    arithmetic diagnostics only; overlapping base or coordinate bits are not
    themselves errors because the executable adds offsets.
    """
    report = {'piece': str(piece.get('id', '<unnamed>')) if isinstance(piece, Mapping)
              else '<unnamed>', 'valid': False, 'errors': [], 'base': None,
              'footprint': None, 'cell_count': 0, 'column_mask': None,
              'row_mask': None, 'base_coordinate_overlap': None,
              'coordinate_field_overlap': None, 'mismatches': [],
              'runtime_collisions': [], 'duplicate_cells': [], 'zoom_collisions': [],
              'allocation_collisions': [], 'engine_origin': None,
              'engine_grid_keys': [], 'engine_key_collisions': [],
              'engine_key_formula': '((row << 4) + column + 1) & 0xff',
              'engine_collision_resolution': 'last cell in row-major order wins'}

    def fail(message):
        report['errors'].append(message)

    def finish():
        if report['errors']:
            raise AutoTileAddressError(report)
        report['valid'] = True
        return report

    if not isinstance(piece, Mapping):
        fail('piece must be a mapping')
        return finish()
    footprint = piece.get('footprint')
    if not isinstance(footprint, (list, tuple)) or len(footprint) != 2:
        fail('footprint must contain a positive integer width and depth')
        return finish()
    try:
        width, depth = (_integer(value, 'footprint dimension') for value in footprint)
        if not width or not depth:
            raise ValueError('footprint dimensions must be positive')
    except ValueError as error:
        fail(str(error))
        return finish()
    report['footprint'] = [width, depth]
    column_mask = ((1 << (width - 1).bit_length()) - 1) << 8
    row_mask = ((1 << (depth - 1).bit_length()) - 1) << 4
    report['column_mask'] = f'{column_mask:08x}'
    report['row_mask'] = f'{row_mask:08x}'
    report['coordinate_field_overlap'] = f'{column_mask & row_mask:08x}'

    tiles = piece.get('tile_ids')
    explicit_cells = piece.get('cells')
    if not isinstance(tiles, (list, tuple)):
        fail('tile_ids must be a nonempty sequence')
        return finish()
    if explicit_cells is None:
        expected_count = width * depth
        cells = ((column, row) for row in range(depth) for column in range(width))
    elif isinstance(explicit_cells, (list, tuple)):
        expected_count = len(explicit_cells)
        cells = iter(explicit_cells)
    else:
        fail('cells must be a nonempty sequence of coordinate pairs')
        return finish()
    report['cell_count'] = expected_count
    if not expected_count or len(tiles) != expected_count:
        fail('tile_ids must contain exactly one ID for every occupied cell')
        return finish()

    placements, allocated, seen_cells = [], [], set()
    for index, (cell, tile) in enumerate(zip(cells, tiles)):
        try:
            if not isinstance(cell, (list, tuple)) or len(cell) != 2:
                raise ValueError(f'cell {index} must be a coordinate pair')
            column, row = (_integer(value, f'cell {index} coordinate') for value in cell)
            if column >= width or row >= depth:
                raise ValueError(f'cell {index} lies outside the declared footprint')
            address = _identifier(tile, f'tile_ids[{index}]')
        except ValueError as error:
            fail(str(error))
            continue
        if (column, row) in seen_cells:
            report['duplicate_cells'].append([column, row])
        seen_cells.add((column, row))
        placements.append((column, row))
        allocated.append(address)
    if report['duplicate_cells']:
        fail('occupied cells contain duplicate placements')
    # A malformed first cell cannot provide an unambiguous allocation base.
    if len(placements) != expected_count or report['duplicate_cells']:
        return finish()
    _, origin, keys, winners = _resolve_cells(placements)
    report['engine_origin'] = list(origin)
    first_column, first_row = placements[0]
    base = allocated[0] - ((first_column - origin[0]) << 8) - ((first_row - origin[1]) << 4)
    if not 0 <= base <= UINT32_MAX:
        fail('inferred base must fit an unsigned 32-bit integer')
        return finish()
    report['base'] = f'{base:08x}'
    report['base_coordinate_overlap'] = f'{base & (column_mask | row_mask):08x}'
    if base & 0xf or any(address & 0xf for address in allocated):
        fail('base and tile IDs must leave the low four zoom bits clear')

    key_owners = {}
    for cell, key in keys.items():
        key_owners.setdefault(key, []).append(cell)
    report['engine_key_collisions'] = [
        {'key': f'{key:02x}', 'cells': [list(cell) for cell in cells],
         'selected_cell': list(winners[key])}
        for key, cells in key_owners.items() if len(cells) > 1]
    runtime_owners, zoom_owners, allocation_owners = {}, {}, {}
    for cell, address in zip(placements, allocated):
        column, row = cell
        selected = winners[keys[cell]]
        try:
            runtime = game_tile_id(base, selected[0] - origin[0], selected[1] - origin[1])
        except ValueError as error:
            fail(f'tile {column},{row}: {error}')
            continue
        report['engine_grid_keys'].append({'cell': list(cell), 'key': f'{keys[cell]:02x}',
            'selected_cell': list(selected), 'runtime': f'{runtime:08x}'})
        if runtime != address:
            report['mismatches'].append({'cell': list(cell), 'allocated': f'{address:08x}',
                                         'runtime': f'{runtime:08x}'})
        if runtime in runtime_owners:
            report['runtime_collisions'].append({'id': f'{runtime:08x}',
                'cells': [list(runtime_owners[runtime]), list(cell)]})
        else:
            runtime_owners[runtime] = cell
        if address in allocation_owners:
            report['allocation_collisions'].append({'id': f'{address:08x}',
                'cells': [list(allocation_owners[address]), list(cell)]})
        else:
            allocation_owners[address] = cell
        # Inspect all allocated zoom resources independently of runtime IDs.
        if address + 4 > UINT32_MAX:
            fail(f'tile {column},{row} zoom IDs exceed unsigned 32-bit range')
            continue
        for zoom in range(5):
            zoom_id = address + zoom
            if zoom_id in zoom_owners:
                old_cell, old_zoom = zoom_owners[zoom_id]
                report['zoom_collisions'].append({'id': f'{zoom_id:08x}',
                    'first': {'cell': list(old_cell), 'zoom': old_zoom},
                    'second': {'cell': list(cell), 'zoom': zoom}})
            else:
                zoom_owners[zoom_id] = (cell, zoom)
    if report['mismatches']:
        fail(f"{len(report['mismatches'])} allocated tile IDs differ from runtime addresses")
    if report['runtime_collisions']:
        fail('runtime addresses alias different placements')
    if report['engine_key_collisions']:
        fail('engine byte keys alias different placements')
    if report['allocation_collisions']:
        fail('allocated tile IDs collide')
    if report['zoom_collisions']:
        fail('allocated zoom resources collide')
    return finish()
