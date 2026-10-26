"""Build globally joined one-way branches and modular rail crossings.

Layouts and train movement permissions live in ``interchange_layouts``. This
module compiles their physical decks, models at all five zooms, paths, shadows,
menu-preview assets and fixed construction rules. Construction rules use
a separate SCP rotation sequence.
"""
from __future__ import annotations

from copy import deepcopy
import string

from scp.dbpf import require
from scp.track_paths import S3D, PATH, EXEMPLAR, EFFECT, LTEXT, encode_paths
from scp_hsr.track_shapes import _construction_flags

SAFE_CELL_SYMBOLS = string.ascii_uppercase + string.ascii_lowercase
EMPTY_STRUCTURAL_PATH = b'SC4PATHS\r\n1.2\r\n0\r\n0\r\n0\r\n'
EFFECT_DONOR = ((*EFFECT, 0x5DDF0100), 'preview_hsr_ofillerpiece000', 0x5DD31500)


def _layout_data(recipe):
    from .interchange_layouts import INFO, interchange_layout
    require(recipe in INFO, f'Unknown interchange recipe: {recipe}')
    return INFO[recipe], interchange_layout(recipe)


def _number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def _spec(spec):
    recipe = spec['recipe']
    info, layout = _layout_data(recipe)
    cells = [tuple(cell) for cell in spec.get('cells', info['cells'])]
    require(cells == list(info['cells']) and tuple(spec['footprint']) == tuple(info['footprint']),
            'Interchange footprint/cells differ from the implemented layout')
    width, depth = info['footprint']
    require(1 <= width <= 64 and 1 <= depth <= 16, 'Interchange exceeds the native construction grid allocation')
    require(set(cells) == set(layout), 'Interchange layout and allocated cells differ')
    require(len(cells) == len(set(cells)) and all(0 <= x < width and 0 <= row < depth for x, row in cells),
            'Interchange has duplicate or out-of-bounds cells')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(cells) and tiles, 'Interchange tile allocation count differs from the layout')
    base = tiles[0] - 0x100 * cells[0][0] - 0x10 * cells[0][1]
    require(tiles == [base + 0x100 * x + 0x10 * row for x, row in cells],
            'Interchange tile IDs do not follow the native AutoTileBase grid')
    return recipe, info, layout, dict(zip(cells, tiles)), base


def construction_symbols(cells, flags):
    """Reuse a safe ASCII symbol for every cell sharing a construction type.

    Native NAM interchange E8A3 repeats its c/d/W/Z labels over many cells and
    supplies one CheckType per label. Grouping by flag avoids the non-ASCII
    characters produced by assigning a new character to each occupied cell.
    """
    unique = sorted({flags[cell] for cell in cells})
    require(len(unique) <= len(SAFE_CELL_SYMBOLS), 'Too many distinct interchange construction flags')
    symbols = dict(zip(unique, SAFE_CELL_SYMBOLS))
    return {cell: symbols[flags[cell]] for cell in cells}, symbols


def build_rules(spec):
    _, info, layout, tiles, base = _spec(spec)
    cells = list(tiles)
    flags = info.get('construction_flags') or {cell: _construction_flags(layout[cell]['routes']) for cell in cells}
    require(set(flags) == set(cells), 'Interchange construction flags differ from allocated cells')
    letters, by_flag = construction_symbols(cells, flags)
    width, depth = info['footprint']
    def grid(construct=False):
        rows = ['.' * (width + 3)]
        for row in range(depth):
            rows.append('.' + ''.join(('+' if construct else letters[(x, row)])
                                     if (x, row) in letters else '.' for x in range(width))
                        + '.' + ('<' if row == 0 else '.'))
        rows.append('.^' + '.' * (width + 1))
        return rows
    puzzle, preview = _number(spec['puzzle_id']), _number(spec['preview_id'])
    lines = [f'[HighwayIntersectionInfo_0x{puzzle:08X}]',
             f'Piece = 0.0, 0.0, 0, 0, 0x{preview:08X}', f"PreviewEffect = {spec['effect_name']}", '']
    lines += ['CellLayout = ' + row for row in grid()]
    lines += [''] + [f'CheckType = {symbol} - monorail: 0x{flag:08X}' for flag, symbol in by_flag.items()]
    lines += [''] + ['ConsLayout = ' + row for row in grid(True)]
    lines += ['', f'AutoTileBase = 0x{base:08X}', 'ReplacementIntersection = 0, 0',
              f'PlaceQueryID = 0x{next(iter(tiles.values())):08X}', f'Costs = {info["cost"]}']
    # Proper rotations retain the declared one-way running. Mirroring is
    # deliberately represented by a separately designed recipe where needed.
    for slot in range(1, 8):
        lines += ['', f'[HighwayIntersectionInfo_0x{puzzle + slot * 0x10000:08X}]',
                  f'CopyFrom = 0x{puzzle + (slot % 4) * 0x10000 if slot >= 4 else puzzle:X}']
        if slot < 4:
            lines.append(f'Rotate = {slot}')
    return '\r\n'.join(lines) + '\r\n'


def _physical_layout(layout):
    result = deepcopy(layout)
    for data in result.values():
        for deck in data['decks']:
            deck.setdefault('profile', 'blend')
            deck.setdefault('safe_supports', True)
            deck.setdefault('extend_endpoints', 'ports')
            deck.setdefault('precise_union', True)
            deck.setdefault('simplify_collinear', True)
    return result


def build_interchange(spec, context):
    """Compile assets and one construction family; the caller adds its ring."""
    from scp.models import parse_s3d, pack_s3d
    from .rail_geometry import build_tiled_geometry
    from scp.recipes import combine_meshes, effect_clone, label, tile_exemplar
    from scp.shadows import build_shadows
    _, info, layout, tiles, _ = _spec(spec)
    structural = {tuple(cell) for cell in info.get('structural_cells', [])}
    require(structural <= set(tiles), 'Interchange structural cells are not allocated')
    hsr = context['hsr']
    models = build_tiled_geometry(hsr[*S3D, 0x5DD31500], _physical_layout(layout), supports=True, ground=False)
    assets, preview_parts = {}, []
    for cell, tile in tiles.items():
        routes = layout[cell]['routes']
        require(routes or cell in structural, 'An interchange traffic cell has no train paths')
        raw = models[cell]
        for zoom in range(5):
            assets[*S3D, tile + zoom] = raw
        assets.update(build_shadows(raw, tile))
        assets[*PATH, tile] = encode_paths(routes) if routes else EMPTY_STRUCTURAL_PATH
        assets[*EXEMPLAR, tile] = tile_exemplar(hsr[*EXEMPLAR, 0x5DCF0A00], tile, 'SCP | ' + spec['name'])
        assets[*LTEXT, tile] = label('SCP | ' + spec['name'] + ' (Experimental)')
        model = parse_s3d(raw)
        preview_parts.append((model, model['meshes'], (16. * cell[0], 0., 16. * cell[1])))
    preview = _number(spec['preview_id'])
    assets[*S3D, preview] = pack_s3d(combine_meshes(preview_parts))
    donor_tgi, donor_name, donor_model = info.get('effect_donor', EFFECT_DONOR)
    assets[*EFFECT, preview] = effect_clone(hsr[donor_tgi], donor_name, spec['effect_name'], donor_model, preview)
    return assets, build_rules(spec)
