"""Reusable paired HSR bridges, ramps and curves with independent placement.

Each physical paired deck is supplied once, retaining the native +/-2 m
traffic lanes.  The reviewed height-aware compiler keeps both bridge floors
and uses one globally spaced, slope-seated support plan per module. Existing
pieces are never rebuilt here.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import json
import math

from scp.autotile import validate_auto_tile_addresses
from scp.catalog import auto_tile_base
from scp.dbpf import require
from .hsr_mesh import _compile_models, _sweep_native_profile, support_centers
from .interchange_models import construction_symbols, EMPTY_STRUCTURAL_PATH, EFFECT_DONOR
from scp.track_paths import S3D, PATH, EXEMPLAR, EFFECT, LTEXT, encode_paths
from .hsr_components_layout import INFO as LAYOUT_INFO, RECIPES, component_layout


INFO = deepcopy(LAYOUT_INFO)
for _recipe in RECIPES:
    INFO[_recipe]['support_centers'] = (deepcopy(INFO[_recipe]['authored_support_centers'])
        if 'authored_support_centers' in INFO[_recipe] else support_centers(component_layout(_recipe)))
    INFO[_recipe]['support_foundation_width'] = 1.3
    INFO[_recipe]['support_min_spacing'] = 16.


def _number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def _spec(spec):
    recipe = spec['recipe']
    require(recipe in INFO, 'Unknown reusable HSR component')
    info = INFO[recipe]
    cells = [tuple(cell) for cell in spec.get('cells', info['cells'])]
    require(cells == list(info['cells']) and tuple(spec['footprint']) == tuple(info['footprint']),
            'HSR component footprint/cells differ from the implemented layout')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(cells) and tiles, 'HSR component allocation count differs')
    base = tiles[0]-0x100*cells[0][0]-0x10*cells[0][1]
    require(tiles == [base+0x100*x+0x10*row for x, row in cells],
            'HSR component allocation differs from its additive grid')
    validate_auto_tile_addresses(spec)
    return info, dict(zip(cells, tiles)), auto_tile_base(spec)


def build_rules(spec):
    info, tiles, base = _spec(spec)
    letters, by_flag = construction_symbols(list(tiles), info['construction_flags'])
    width, depth = info['footprint']

    def grid(construct=False):
        rows = ['.'*(width+3)]
        for row in range(depth):
            rows.append('.'+''.join(('+' if construct else letters[x, row])
                if (x, row) in letters else '.' for x in range(width))
                +'.'+('<' if row == 0 else '.'))
        return rows+['.^'+'.'*(width+1)]

    puzzle, preview = _number(spec['puzzle_id']), _number(spec['preview_id'])
    lines = [f'[HighwayIntersectionInfo_0x{puzzle:08X}]',
             f'Piece = 0.0, 0.0, 0, 0, 0x{preview:08X}',
             f"PreviewEffect = {spec['effect_name']}", '']
    lines += ['CellLayout = '+row for row in grid()]
    lines += ['']+[f'CheckType = {symbol} - monorail: 0x{flag:08X}' for flag, symbol in by_flag.items()]
    lines += ['']+['ConsLayout = '+row for row in grid(True)]
    lines += ['', f'AutoTileBase = 0x{base:08X}', 'ReplacementIntersection = 0, 0',
              f'PlaceQueryID = 0x{next(iter(tiles.values())):08X}', f'Costs = {info["cost"]}']
    for slot in range(1, 8):
        lines += ['', f'[HighwayIntersectionInfo_0x{puzzle+slot*0x10000:08X}]',
                  f'CopyFrom = 0x{puzzle+(slot%4)*0x10000 if slot >= 4 else puzzle:X}']
        if slot < 4:
            lines.append(f'Rotate = {slot}')
    return '\r\n'.join(lines)+'\r\n'


def build_models(native_hsr, recipe):
    require(recipe in INFO, 'Unknown reusable HSR component')
    from .hsr_atomic_junctions import RECIPES as JUNCTION_RECIPES, build_models as junction_models
    from .hsr_atomic_curves import RECIPES as CURVE_RECIPES, build_models as curve_models
    if recipe in JUNCTION_RECIPES:
        return junction_models(native_hsr, recipe)
    if recipe in CURVE_RECIPES:
        return curve_models(native_hsr, recipe)
    from .hsr_compact_fan import RECIPES as COMPACT_FAN_RECIPES, build_models as compact_models
    if recipe in COMPACT_FAN_RECIPES:
        return compact_models(native_hsr, recipe)
    from .hsr_partition_components import RECIPES as PARTITION_RECIPES, build_models as partition_models
    if recipe in PARTITION_RECIPES:
        # Each module owns the exact surface context for its selected cells.
        return partition_models(native_hsr, recipe)
    config = {'layout': [[list(cell), data] for cell, data in component_layout(recipe).items()],
              'support_centers': INFO[recipe]['support_centers'],
              'support_foundation_width': 1.3, 'support_min_spacing': 16.}
    signature = json.dumps(config, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return dict(_cached_models(native_hsr, signature))


def _sweep_component_profile(source, deck):
    """Taper an adapter's shoulders while preserving its actual rail ribbons.

    At its paired end, the two single sheets have 11 m outside widths and
    centres +/-2 m. Their union is exactly the native 15 m deck. Each sheet
    narrows smoothly to the 8 m single-track profile at its other end. The
    inside and outside wall faces interpolate separately, so the native
    parapet thickness also matches the paired end rather than being scaled.
    This transformation is confined to this family's explicit flat adapter.
    """
    swept = _sweep_native_profile(source, deck)
    taper = float(deck.get('taper_extra_half_width', 0.))
    shared_collar = deck.get('shared_mainline_collar')
    if not taper and not shared_collar:
        return swept
    surfaces, corridors, points, lengths = swept
    start = float(deck.get('taper_start_distance', 8.))
    end = float(deck.get('taper_end_distance', 16.))
    require(not taper or end > start, 'Tapered HSR adapter has no narrowing span')
    cumulative = [0.]
    for length in lengths:
        cumulative.append(cumulative[-1]+length)
    if shared_collar:
        require(shared_collar in ('start', 'end') and deck['width'] == 8.
                and all(abs(point[1]-15.5) < 1e-8 for point in points),
                'Shared native collar requires a flat lower eight-metre branch')
        require(3.9 < source['inner']-2. <= 4.,
                'Shared native collar lacks its audited paired parapet profile')
    if not taper:
        pass
    elif deck.get('graded_taper_upper_collar'):
        require(all(abs(point[1]-30.5) < 1e-8
                    for point, distance in zip(points, cumulative) if distance <= end+1e-8),
                'Graded HSR fork must stay flat until its tapered decks have separated')
        require(all(15.5-1e-8 <= point[1] <= 30.5+1e-8 for point in points),
                'Graded HSR fork leaves its explicit lower/upper height range')
    elif 'flat_paired_collar_height' in deck:
        # Only the new lower native junction uses a tapered paired collar
        # at15.5 m. Older upper adapters retain their exact30.5 m contract.
        collar_height = float(deck['flat_paired_collar_height'])
        require(collar_height == 15.5 and
                all(abs(point[1]-collar_height) < 1e-8 for point in points),
                'Lower paired HSR collar must remain exactly flat at15.5 m')
    else:
        require(all(abs(point[1]-30.5) < 1e-8 for point in points),
                'Tapered HSR adapter must remain at its reviewed upper height')
    # Each original sweep vertex is close to its originating centre segment.
    # A spatial index avoids a full route search for every textured corner.
    buckets = {}
    for number, (a, b) in enumerate(zip(points, points[1:])):
        for x in range(math.floor((min(a[0], b[0])-6.)/8.),
                       math.floor((max(a[0], b[0])+6.)/8.)+1):
            for z in range(math.floor((min(a[2], b[2])-6.)/8.),
                           math.floor((max(a[2], b[2])+6.)/8.)+1):
                buckets.setdefault((x, z), []).append(number)
    cache = {}

    def warp(x, z):
        identity = x, z
        if identity in cache:
            return cache[identity]
        best = None
        for number in buckets.get((math.floor(x/8.), math.floor(z/8.)), []):
            a, b = points[number:number+2]
            dx, dz = b[0]-a[0], b[2]-a[2]
            length = lengths[number]
            fraction = max(0., min(1., ((x-a[0])*dx+(z-a[2])*dz)/(length*length)))
            cx, cz = a[0]+fraction*dx, a[2]+fraction*dz
            distance = (x-cx)**2+(z-cz)**2
            if best is None or distance < best[0]:
                best = distance, number, fraction, cx, cz, dz/length, -dx/length
        require(best is not None, 'Taper vertex lacks its physical centreline')
        _, number, fraction, cx, cz, nx, nz = best
        cross = (x-cx)*nx+(z-cz)*nz
        offset = abs(cross)
        station = cumulative[number]+fraction*lengths[number]
        t = max(0., min(1., (station-start)/(end-start))) if taper else 1.
        quintic = t*t*t*(10.+t*(-15.+6.*t))
        q = 1.-quintic
        inner = 2.6+q*(source['inner']-2.-2.6)
        outer = 4.+q*taper
        if shared_collar:
            # The paired native parapet begins3.9965477 m from its
            # +/-2 m track. An ordinary4 m single-track shoulder would
            # shave3.4523 mm from that parapet at a shared connection.
            # Fit only that coincident branch shoulder inside the native
            # parapet; the complete15 m main slab remains untouched.
            distance = station if shared_collar == 'start' else cumulative[-1]-station
            blend = max(0., min(1., (distance-8.)/8.))
            keep = 1.-blend*blend*blend*(10.+blend*(-15.+6.*blend))
            outer -= keep*(4.-(source['inner']-2.))
        # Rail ribbons and their immediate ballast retain their exact lines.
        if offset <= 1.1:
            changed = offset
        elif offset <= 2.6:
            changed = 1.1+(offset-1.1)*(inner-1.1)/1.5
        else:
            changed = inner+(offset-2.6)*(outer-inner)/1.4
        delta = ((changed-offset)*math.copysign(1., cross) if shared_collar
                 else math.copysign(changed-offset, cross))
        result = x+delta*nx, z+delta*nz
        cache[identity] = result
        return result

    changed_surfaces = []
    for kind, triangle in surfaces:
        if kind == 'rail':
            changed_surfaces.append((kind, triangle))
            continue
        vertices = []
        for x, height, z, u, v in triangle:
            xx, zz = warp(x, z)
            vertices.append((xx, height, zz, u, v))
        changed_surfaces.append((kind, tuple(vertices)))
    changed_corridors = []
    for corridor in corridors:
        changed_corridors.append({**corridor,
            'polygon': [warp(x, z) for x, z in corridor['polygon']],
            'clearance_polygons': [[warp(x, z) for x, z in polygon]
                                   for polygon in corridor.get('clearance_polygons', [])]})
    return changed_surfaces, changed_corridors, points, lengths


@lru_cache(maxsize=16)
def _cached_models(native_hsr, signature):
    config = json.loads(signature)
    layout = {tuple(cell): data for cell, data in config['layout']}
    result = _compile_models(native_hsr, layout, config,
                             sweep_function=_sweep_component_profile)
    return tuple(result.items())


def build_hsr_component(spec, context):
    from scp.models import parse_s3d, pack_s3d
    from scp.recipes import combine_meshes, effect_clone, label, tile_exemplar
    from scp.shadows import build_shadows
    info, tiles, _ = _spec(spec)
    layout = component_layout(spec['recipe'])
    structural = set(map(tuple, info.get('structural_cells', [])))
    hsr = context['hsr']
    models = build_models(hsr[*S3D, 0x5DD31500], spec['recipe'])
    assets, parts = {}, []
    for cell, tile in tiles.items():
        raw = models[cell]
        routes = layout[cell]['routes']
        require(routes or cell in structural, 'HSR component has an undeclared empty traffic cell')
        for zoom in range(5):
            assets[*S3D, tile+zoom] = raw
        assets.update(build_shadows(raw, tile))
        assets[*PATH, tile] = encode_paths(routes) if routes else EMPTY_STRUCTURAL_PATH
        assets[*EXEMPLAR, tile] = tile_exemplar(hsr[*EXEMPLAR, 0x5DCF0A00], tile, 'SCP | '+spec['name'])
        assets[*LTEXT, tile] = label('SCP | '+spec['name']+' (Experimental)')
        model = parse_s3d(raw)
        parts.append((model, model['meshes'], (16.*cell[0], 0., 16.*cell[1])))
    preview = _number(spec['preview_id'])
    assets[*S3D, preview] = pack_s3d(combine_meshes(parts))
    donor, name, source_model = info.get('effect_donor', EFFECT_DONOR)
    assets[*EFFECT, preview] = effect_clone(hsr[donor], name, spec['effect_name'], source_model, preview)
    return assets, build_rules(spec)
