"""HSR/GHSR recipe dispatch and native crossing composition policy."""
from copy import deepcopy
import re
import struct
from scp.dbpf import exemplar, encode_exemplar, require
from scp.models import parse_s3d, pack_s3d, valid_frame, validate_s3d, bounds
from .crossing_models import build_crossing_model
from scp.recipes import family, label, tile_exemplar, effect_clone, combine_meshes, parse_donor_paths
from scp.track_paths import S3D, PATH, EXEMPLAR, EFFECT, LTEXT


def build_piece(spec, context):
    """The recipe contract: assets + an independent eight-slot rule ring."""
    tiles = [int(x, 16) for x in spec['tile_ids']]
    preview = int(spec['preview_id'], 16)
    puzzle = spec['puzzle_id'].upper()
    title = 'SCP | ' + spec['name'] + ' (Experimental)'
    text = context['controller'][(0x0A5BCF4B, 0xAA5BCF57, 0x10000000)].decode('ascii')
    hsr, assets = context['hsr'], {}
    from scp_hsr.crossings import RECIPES as CROSSING_RECIPES, build_crossing
    if spec['recipe'] in CROSSING_RECIPES:
        assets, rules = build_crossing(spec, context)
    elif spec['recipe'].startswith('hsr_component_'):
        from scp_hsr.hsr_components import build_hsr_component
        assets, rules = build_hsr_component(spec, context)
    elif spec['recipe'] == 'directional_hsr_t_smooth_diagonal_at_grade':
        from scp_hsr.directional_diagonal_t import build_directional
        assets, rules = build_directional(spec, context)
    elif spec['recipe'].startswith('directional_'):
        from scp_hsr.directional_t import build_directional
        assets, rules = build_directional(spec, context)
    elif spec['recipe'].startswith('interchange_'):
        from scp_hsr.interchange_models import build_interchange
        assets, rules = build_interchange(spec, context)
    elif spec['recipe'].startswith('rail_') and spec['recipe'].endswith('_revised'):
        from scp_hsr.rail_repairs import build_repair
        assets, rules = build_repair(spec, context)
    elif spec['recipe'].startswith('rail_'):
        from scp_hsr.rail_features import build_feature
        assets, rules = build_feature(spec, context)
    elif spec['recipe'] == 'hsr_diagonal_ghsr':
        urail = context['urail']
        for number, (tile, native) in enumerate(zip(tiles, (0x59F3D110, 0x59F3D120))):
            raw, audit = crossing_model(urail[*S3D, native + 4], hsr[*S3D, 0x5DD31500])
            for zoom in range(5):
                assets[*S3D, tile + zoom] = raw
            assets[*PATH, tile] = make_paths(urail[*PATH, native], hsr[*PATH, 0x5DD31500])
            assets[*EXEMPLAR, tile] = tile_exemplar(hsr[*EXEMPLAR, 0x5DCF0A00], tile, title)
        parts = []
        for n, tile in enumerate(tiles):
            model = parse_s3d(assets[*S3D, tile + 4])
            parts.append((model, model['meshes'], (0., 0., 16. * n)))
        assets[*S3D, preview] = pack_s3d(combine_meshes(parts))
        assets[*EFFECT, preview] = effect_clone(urail[*EFFECT, 0x59F3D115],
            'preview_hsrp_subrail____001', spec['effect_name'], 0x59F3D115, preview)
        rules = family(text, 'AAC1').replace('AAC1', puzzle).replace('rail:', 'monorail:')
        rules = rules.replace('0x59F33015', f'0x{preview:08X}').replace('0x59F33010', f'0x{tiles[0]:08X}')
        rules = rules.replace('preview_rail_subrail____001', spec['effect_name']).replace('Costs = 60', 'Costs = 150')
    elif spec['recipe'] == 'tram_under_hsr':
        glr = context['glr']; tile = tiles[0]
        model = build_crossing_model(glr[*S3D, 0x580E0700], hsr[*S3D, 0x5DD31500])
        for zoom in range(5):
            assets[*S3D, tile + zoom] = model
        assets[*S3D, preview] = model
        assets[*PATH, tile] = glr[*PATH, 0x580E0700]
        assets[*EXEMPLAR, tile] = tile_exemplar(glr[*EXEMPLAR, 0x580E0700], tile, title)
        assets[*EFFECT, preview] = effect_clone(glr[*EFFECT, 0x580E0700],
            'preview_rail_dualnetwork029', spec['effect_name'], 0x580E0705, preview)
        rules = family(text, 'B12F').replace('B12F', puzzle)
        rules = rules.replace('580e070', f'{tile:08x}'[:-1]).replace('0x580E0705', f'0x{preview:08X}')
        rules = rules.replace('preview_rail_dualnetwork029', spec['effect_name'])
    else:
        raise ValueError(f"Recipe {spec['recipe']!r} has no builder; draft pieces cannot be built")
    for tile in tiles:
        assets[*LTEXT, tile] = label(title)
    ring = 'RotationRing = ' + ', '.join(f'{n * 0x10000 + int(puzzle, 16):X}' for n in range(8))
    rules = ring + f" ;SCP {spec['id']}\r\n\r\n" + rules
    return assets, rules


def crossing_model(ground_raw: bytes, hsr_raw: bytes) -> tuple[bytes, dict]:
    ground, upper = map(parse_s3d, (ground_raw, hsr_raw))
    ground_meshes = [m for m in ground['meshes'] if m['name'].rstrip(b'\0') == b'HSR']
    upper_meshes = [m for m in upper['meshes'] if all(valid_frame(upper, f) for f in m['frames'])]
    assert len(ground_meshes) == len(upper_meshes) == 1
    assert bounds(ground['vertices'][ground_meshes[0]['frames'][0][0]])[1][1] < 2
    assert bounds(upper['vertices'][upper_meshes[0]['frames'][0][0]])[1][0] > 14
    model = combine_meshes([(ground, ground_meshes, (0., 0., 0.)),
                            (upper, upper_meshes, (0., 0., 0.))])
    raw = pack_s3d(model)
    checks = validate_s3d(parse_s3d(raw))
    # Every retained vertex buffer is exactly native. The ground platform and
    # unrelated Rail surface of the URail preview are intentionally omitted.
    for number, donor, meshes in ((0, ground, ground_meshes), (1, upper, upper_meshes)):
        for col, array in enumerate(('vertices', 'indices', 'primitives', 'materials')):
            assert model[array][model['meshes'][number]['frames'][0][col]] == donor[array][meshes[0]['frames'][0][col]]
    return raw, {'retained_donor_buffers_exactly': True, 'checks': checks,
                 'no_ground_reaching_upper_support': True}


def make_paths(ground_raw: bytes, hsr_raw: bytes) -> bytes:
    lower = [r for r in parse_donor_paths(ground_raw) if r['transport'] == 7]
    upper = parse_donor_paths(hsr_raw)
    assert len(lower) == len(upper) == 2 and all(r['transport'] == 7 for r in upper)
    # Format/header/class/junction convention copied from native GHSR x HSR.
    lines = ['SC4PATHS', '1.2', '4', '0', '0']
    for level, routes in (('GHSR', lower), ('HSR', upper)):
        for route in routes:
            lines += [f"-- {level}_{route['entry']}_{route['exit']}", '7', '1',
                      str(route['entry']), str(route['exit']), '0', str(len(route['points']))]
            lines += [','.join(f'{v:g}' for v in point) for point in route['points']]
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


def make_exemplar(donor: bytes, tile: int, number: int) -> bytes:
    record = exemplar(donor)
    output = bytearray(b'EQZB1###' + struct.pack('<3I', *record['parent']) + struct.pack('<I', len(record['properties'])))
    for p in record['properties']:
        pid, kind, key = int(p['id'], 16), int(p['type'], 16), int(p['key_type'], 16)
        values = p['values']
        if pid == 0x20: values = f'Custom HSR Level 2 (15.5 m) over GHSR Ground (1 m) \u2014 Two-Track Crossing 45\u00b0 \u2014 Lower Diagonal - tile {number + 1}'
        if pid == 0x27812823: values = [*S3D, *range(tile, tile + 5)]
        output.extend(struct.pack('<IHHB', pid, kind, key, 0))
        if kind == 0xC00:
            data = values.encode('utf8'); assert key == 0x80
            output.extend(struct.pack('<I', len(data)) + data)
        else:
            if key == 0x80: output.extend(struct.pack('<I', len(values)))
            output.extend(struct.pack('<' + {0x300: 'I', 0x900: 'f'}[kind] * len(values), *values))
    return bytes(output)
