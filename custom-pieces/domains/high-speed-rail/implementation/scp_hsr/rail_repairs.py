"""Current adjacent-line scissors switches with consolidated supports.

Each switch compiles its complete deck union with the current clearance
algorithm. Elevated models use one deliberate support per occupied cell.
"""
from __future__ import annotations

from scp.dbpf import require
from .rail_features import _adjacent_layout, _adjacent_ports, _layout_info, _construction_rules
from scp.track_paths import S3D, PATH, EXEMPLAR, EFFECT, LTEXT, encode_paths

RECIPES = ('rail_hsr_adjacent_scissors_revised', 'rail_ghsr_adjacent_scissors_revised')
INFO = {}
for _recipe in RECIPES:
    _height = 1. if '_ghsr_' in _recipe else 15.5
    _info = _layout_info(_adjacent_layout(_height, 'both'), _height)
    _info['ports'], _info['movements'] = _adjacent_ports(_height, 'both')
    _info.update(recipe=_recipe,
                 support_centers=[(16. * x, -16. * row) for x, row in _info['cells']]
                 if _height > 1 else [],
                 support_foundation_width=1.3, support_min_spacing=16.,
                 clearance_width=5., clearance_height=5.,
                 provenance='Retained native ports and movements; current global union, widened clearance and consolidated supports')
    INFO[_recipe] = _info


def repair_layout(recipe):
    """Return a fresh layout for the current adjacent-line scissors switch."""
    require(recipe in INFO, f'Unknown scissors-switch recipe: {recipe}')
    layout = _adjacent_layout(INFO[recipe]['height'], 'both')
    from .interchange_layouts import _native_collars
    layout = _native_collars(layout, {'kind': 'rail_repair'})
    height = INFO[recipe]['height']
    for data in layout.values():
        for deck in data['decks']:
            deck.update(profile='ghsr' if height == 1. else 'hsr',
                        precise_union=True, simplify_collinear=True,
                        extend_endpoints='ports', clearance_half_width=2.6,
                        support=False)
    return layout


def _number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def _spec(spec):
    recipe = spec['recipe']
    require(recipe in INFO, 'Unknown repaired rail recipe')
    info = INFO[recipe]
    cells = [tuple(cell) for cell in spec.get('cells', info['cells'])]
    require(cells == info['cells'] and tuple(spec['footprint']) == info['footprint'],
            'Repaired rail footprint/cells differ from the implemented layout')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(cells) and bool(tiles), 'Repaired rail tile count differs from its occupied cells')
    base = tiles[0] - 0x100 * cells[0][0] - 0x10 * cells[0][1]
    require(tiles == [base + 0x100 * x + 0x10 * row for x, row in cells],
            'Repaired rail allocation differs from the native AutoTileBase grid')
    return recipe, info, dict(zip(cells, tiles))


def build_rules(spec):
    """Use the reviewed construction headings for the current switch."""
    _, info, tiles = _spec(spec)
    return _construction_rules(spec, info, tiles)


def build_models(native_hsr, recipe):
    """Compile each tile with a single reserved, widely spaced foundation."""
    from scp.models import parse_s3d, pack_s3d
    from .rail_geometry import build_tiled_geometry
    from .single_track_models import _native, _pack, _pillar
    from scp.recipes import combine_meshes
    require(recipe in INFO, 'Unknown repaired rail recipe')
    info = INFO[recipe]
    result = build_tiled_geometry(native_hsr, repair_layout(recipe), supports=False,
                                  ground=info['height'] == 1.)
    if info['height'] == 1.:
        return result
    source = _native(native_hsr)
    support = parse_s3d(_pack(source, _pillar((0., 0.), source['bottom'])))
    support['meshes'][0]['name'] = b'SCP consolidated junction support\0'
    for cell, raw in result.items():
        model = parse_s3d(raw)
        result[cell] = pack_s3d(combine_meshes([
            (model, model['meshes'], (0., 0., 0.)),
            (support, support['meshes'], (0., 0., 0.)),
        ]))
    return result


def build_repair(spec, context):
    """Build the current switch assets and construction rules."""
    from scp.models import parse_s3d, pack_s3d
    from scp.recipes import combine_meshes, effect_clone, label, tile_exemplar
    from scp.shadows import build_shadows
    recipe, info, tiles = _spec(spec)
    layout = repair_layout(recipe)
    hsr = context['hsr']
    models = build_models(hsr[*S3D, 0x5DD31500], recipe)
    assets, parts = {}, []
    for cell, tile in tiles.items():
        raw = models[cell]
        for zoom in range(5):
            assets[*S3D, tile + zoom] = raw
        assets.update(build_shadows(raw, tile))
        assets[*PATH, tile] = encode_paths(layout[cell]['routes'])
        assets[*EXEMPLAR, tile] = tile_exemplar(hsr[*EXEMPLAR, 0x5DCF0A00], tile, 'SCP | ' + spec['name'])
        assets[*LTEXT, tile] = label('SCP | ' + spec['name'] + ' (Experimental)')
        model = parse_s3d(raw)
        parts.append((model, model['meshes'], (16. * cell[0], 0., 16. * cell[1])))
    preview = _number(spec['preview_id'])
    assets[*S3D, preview] = pack_s3d(combine_meshes(parts))
    donor, donor_name, donor_model = info['effect_donor']
    assets[*EFFECT, preview] = effect_clone(hsr[donor], donor_name, spec['effect_name'], donor_model, preview)
    return assets, build_rules(spec)
