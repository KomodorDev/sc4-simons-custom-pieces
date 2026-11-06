"""Saved-resource recipes for measured DD RHW-4 network components."""
from __future__ import annotations

from copy import deepcopy
import hashlib
import struct

from scp.catalog import auto_tile_base
from scp.dbpf import require, exemplar, encode_exemplar
from scp.models import parse_s3d, pack_s3d
from scp.recipes import combine_meshes, effect_clone, label
from scp.shadows import build_shadows
from scp.track_paths import S3D, PATH, EXEMPLAR, EFFECT, LTEXT
from .native import CELLS, RECIPE, build_crossing_channels
from .orthogonal_transition_variants import LOWER_BEND_RIGHT, SUPPORTED_RECIPES as ORTHOGONAL_TRANSITION_RECIPES
from .diagonal_transition_variants import RECIPES as DIAGONAL_TRANSITION_RECIPES

EFFECT_DONOR = ((*EFFECT, 0x57F53600), 'preview_filler__ddrhw4__001', 0x57F53605)
EFFECT_DONOR_SHA256 = '0ecbae8d051d62d8f42a583b584d167a1e976a8e21942b4b56e554e7ad1cdb9a'


def effect_donor(spec):
    return EFFECT_DONOR


def validate_effect(spec, effect):
    """Verify all effect bytes portably after undoing only our two edits."""
    _key, name, native_model = EFFECT_DONOR
    authored_name, donor_name = spec['effect_name'].encode('ascii'), name.encode('ascii')
    authored_model = struct.pack('<I', int(spec['preview_id'], 16))
    donor_model = struct.pack('<I', native_model)
    require(len(authored_name) == len(donor_name) and effect.count(authored_name) == 4 and
            effect.count(authored_model) == 2, 'Invalid native highway preview effect references')
    restored = effect.replace(authored_name, donor_name).replace(authored_model, donor_model)
    require(hashlib.sha256(restored).hexdigest() == EFFECT_DONOR_SHA256,
            'Highway preview effect differs from the pinned native effect bytes')
    return {'native_effect_fingerprint_verified': True, 'native_donor_tgi': 'EA5118B0-EA5118B1-57F53600',
            'portable_verification': True}


def tile_exemplar(context, tile, title):
    record = deepcopy(exemplar(context['rhw_core'][*EXEMPLAR, 0x57F53600]))
    for prop in record['properties']:
        if int(prop['id'], 16) == 0x20:
            prop['values'] = title
        elif int(prop['id'], 16) == 0x27812820:
            prop['id'] = '0x27812823'
            prop['values'] = [*S3D, *range(tile, tile + 5)]
    return encode_exemplar(record)


def construction(spec, cells=None, checks=None, cons=None):
    """Emit explicit dirtroad construction, with four rotations repeated once."""
    puzzle, preview, base = int(spec['puzzle_id'], 16), int(spec['preview_id'], 16), auto_tile_base(spec)
    cell_rows = cells or ['.a..<', 'bcd..', '.e...', '^....']
    cons_rows = cons or ['.\\..<', '\\++..', '.+...', '^....']
    palette = checks or ['a - avenue: 0x01000003', 'b - avenue: 0x00030100',
                         'c - dirtroad: 0x03010000 avenue: 0x01030103',
                         'd - dirtroad: 0x00000301 avenue: 0x01000003',
                         'e - dirtroad: 0x00000301 avenue: 0x00030100']
    from .ddrhw_connections import add_approaches
    cell_rows, palette, cons_rows = add_approaches(spec, cell_rows, palette, cons_rows)
    lines = ['RotationRing = ' + ', '.join(f'{puzzle + n * 0x10000:X}' for n in range(8)) + f' ;SCP {spec["id"]}',
             '', f'[HighwayIntersectionInfo_0x{puzzle:08X}]', f'Piece = 0.0, 0.0, 0, 0, 0x{preview:08X}',
             f'PreviewEffect = {spec["effect_name"]}']
    lines += ['CellLayout = ' + line for line in cell_rows]
    lines += ['CheckType = ' + line for line in palette]
    lines += ['ConsLayout = ' + line for line in cons_rows]
    lines += [f'AutoTileBase = 0x{base:08X}', 'ReplacementIntersection = 0, 0',
              f'PlaceQueryID = 0x{int(spec["tile_ids"][0], 16):08X}']
    if spec.get('recipe') in DIAGONAL_TRANSITION_RECIPES:
        from .diagonal_transition_layout import declaration
        from .diagonal_transition_native import socket_specs
        layout = declaration(spec)
        socket = next(row for row in socket_specs(layout['key']) if row.arm == 'dd')
        x, y = [end - origin for end, origin in zip(socket.core_end_cell, layout['world_origin_cell'])]
        require([x, y] in spec['cells'], 'Diagonal transition handle must be on the owned DD end')
        lines.append(f'HandleOffset = {x}, {y}')
    lines.append('Costs = 1000')
    for n in range(1, 8):
        lines += ['', f'[HighwayIntersectionInfo_0x{puzzle + n * 0x10000:08X}]',
                  f'CopyFrom = 0x{puzzle if n < 4 else puzzle + (n - 4) * 0x10000:X}']
        if n < 4:
            lines += [f'Rotate = {n}']
    return '\r\n'.join(lines) + '\r\n'


def finish_piece(spec, context, compiled):
    """Add per-cell exemplars, labels, shadows, and a complete placement preview."""
    assets, parts = {}, []
    cells = [tuple(cell) for cell in spec['cells']]
    tiles = [int(value, 16) for value in spec['tile_ids']]
    require(cells == [cell for cell, _, _ in compiled], 'Compiled cell order differs from allocated cells')
    title = 'SCP | ' + spec['name'] + ' (Experimental)'
    from scp.adaptive_network import bindings
    adaptive_tiles = {int(row['canonical_tile_id'], 16) for row in bindings(spec)}
    for (cell, model_raw, path_raw), tile in zip(compiled, tiles):
        for zoom in range(5):
            assets[*S3D, tile + zoom] = model_raw
        assets[*PATH, tile] = path_raw
        if tile not in adaptive_tiles:
            assets[*EXEMPLAR, tile] = tile_exemplar(context, tile, title)
        assets[*LTEXT, tile] = label(title)
        if spec.get('shadow_mode') != 'model-carrier':
            assets.update(build_shadows(model_raw, tile))
        model = parse_s3d(model_raw)
        parts.append((model, model['meshes'], (cell[0] * 16., 0., cell[1] * 16.)))
    preview = int(spec['preview_id'], 16)
    assets[*S3D, preview] = pack_s3d(combine_meshes(parts))
    key, name, model_id = EFFECT_DONOR
    assets[*EFFECT, preview] = effect_clone(context['rhw_core'][key], name, spec['effect_name'], model_id, preview)
    return assets


def compilation_group(spec):
    """Share each cached Highway world or straight-stamp partition in one process."""
    for family in ('highway_ddrhw_parallel_b_', 'highway_ddrhw_parallel_', 'highway_ddrhw_modular_'):
        if spec['recipe'].startswith(family):
            return family
    return None


def build_piece(spec, context):
    if spec['recipe'] in DIAGONAL_TRANSITION_RECIPES:
        from .diagonal_transition import build_piece as build_diagonal_transition
        return build_diagonal_transition(spec, context)
    if spec['recipe'].startswith('highway_ddrhw_y_'):
        from .y_junction import build_piece as build_y_junction
        return build_y_junction(spec, context)
    if spec['recipe'] in ORTHOGONAL_TRANSITION_RECIPES:
        from .orthogonal_transition import build_channels, build_textures
        from .orthogonal_approaches import add_approaches, check_native_continuation, variant
        from .orthogonal_transition_construction import core_construction_data
        from .model_shadows import add_shadows
        check_native_continuation(context['controller'])
        texture_id = int(spec['authored_texture_ids'][0], 16)
        selected_variant = variant(spec)
        variant_options = {} if selected_variant == 'original' else {'variant': selected_variant}
        compiled = build_channels(context, texture_id=texture_id, **variant_options)
        assets = finish_piece(spec, context, compiled)
        extra = build_textures(context, texture_id, **variant_options)
        require(not assets.keys() & extra.keys(), 'Transition texture allocation overlaps another resource')
        assets.update(extra)
        rows, checks, cons = add_approaches(
            spec, *core_construction_data(compiled, mirrored=selected_variant == 'mirrored',
                                          flat_terrain=selected_variant in ('opposite-side', 'opposite-side-mirrored', LOWER_BEND_RIGHT)))
        return add_shadows(spec, context, compiled, assets), construction(spec, rows, checks, cons)
    if spec['recipe'] in ('highway_ddrhw_diagonal_ghsr_crossing',
                          'highway_ddrhw_diagonal_ghsr_crossing_alignment_b'):
        from .ghsr_crossing import (build_channels, core_construction_data,
                                    build_alignment_b_channels, alignment_b_core_construction_data)
        from .ghsr_approaches import add_approaches, check_native_continuation
        from .model_shadows import add_shadows
        check_native_continuation(context['controller'])
        alignment_b = spec['recipe'].endswith('_alignment_b')
        compiled = (build_alignment_b_channels if alignment_b else build_channels)(context)
        assets = finish_piece(spec, context, compiled)
        core_data = (alignment_b_core_construction_data if alignment_b else core_construction_data)()
        rows, checks, cons = add_approaches(spec, *core_data)
        return add_shadows(spec, context, compiled, assets), construction(spec, rows, checks, cons)
    if spec['recipe'].startswith('highway_ddrhw_parallel_b_'):
        from .parallel_b_modules import build_piece as build_parallel_b
        return build_parallel_b(spec, context)
    if spec['recipe'].startswith('highway_ddrhw_parallel_'):
        from .parallel_modules import build_piece as build_parallel
        return build_parallel(spec, context)
    if spec['recipe'] == 'highway_ddrhw_modular_stamp':
        from .modular_stamp import build_piece as build_stamp
        return build_stamp(spec, context)
    if spec['recipe'].startswith('highway_ddrhw_modular_'):
        from .modular_ramps import build_piece as build_modular
        return build_modular(spec, context)
    if spec['recipe'] == RECIPE:
        require(spec['footprint'] == [3, 3] and [tuple(cell) for cell in spec['cells']] == list(CELLS),
                'Native highway crossing requires its measured five-cell cross')
        return finish_piece(spec, context, build_crossing_channels(context)), construction(spec)
    if spec['recipe'].startswith('highway_'):
        from .ramp_paths import build_piece as build_ramp
        return build_ramp(spec, context)
    raise ValueError(f'Unsupported highway recipe: {spec["recipe"]}')
