"""Build a private experimental NAM 50 HSR-over-diagonal-GHSR puzzle piece.

Reads the installed NAM; writes only this directory's dist/. Never installs or
changes a donor. The two-cell construction is adapted from native AAC1, which
already handles two heights of the same underlying network. Ground models and
paths come from the equivalent native GHSR/URail crossing C219; the upper deck
and its paths come directly from straight HSR. No track is stretched or lowered.
"""
from __future__ import annotations

from copy import deepcopy
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import struct
import sys

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
sys.dont_write_bytecode = True
sys.path[:0] = [str(HERE.parent / 'tram-under-hsr'),
                str(HERE.parent / 'cam-install/runtime-audit')]
from read_dbpf import entries, decompress, exemplar, tgi_string
from model_tools import parse_s3d, pack_s3d, valid_frame, validate_s3d, bounds

spec = importlib.util.spec_from_file_location('tram_build_helpers', HERE.parent / 'tram-under-hsr/build.py')
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)

TILES = (0x5DD0F200, 0x5DD0F210)
PREVIEW = 0x5DD0F225
PUZZLE = 0xF7A1
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
NETWORK_INI = (0x00000000, 0x8A5971C5, 0x8A5993B9)
S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
EXEMPLAR = (0x6534284A, 0xA8434037)
EFFECT = (0xEA5118B0, 0xEA5118B1)
LTEXT = (0x2026960B, 0x2A592FD1)
CONTROLLER_SHA256 = 'd903540cdf772b4ed6a072c504e006e1cac384f8027ce58a288a5a9654f94161'
OLD_EFFECT_NAME = b'preview_hsrp_subrail____001'
NEW_EFFECT_NAME = b'preview_hsr_diag_ghsr___001'
TITLE = 'HSR over Diagonal GHSR - Straight Upper Track (Experimental)'
MARKER = '\r\n;BEGIN CUSTOM HSR OVER DIAGONAL GHSR - NAM 50 exact-controller overlay\r\n'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def combine_meshes(sources: list[tuple[dict, list[dict], tuple[float, float, float]]]) -> dict:
    """Copy complete referenced buffers; only explicitly requested offsets change."""
    first = sources[0][0]
    output = {'version': first['version'], 'vertices': [], 'indices': [],
              'primitives': [], 'materials': [], 'anim_header': first['anim_header'],
              'meshes': [], 'trailing': deepcopy(first['trailing'])}
    for model, meshes, offset in sources:
        assert model['version'] == first['version'] and model['anim_header'] == first['anim_header']
        assert model['trailing'] == first['trailing']
        maps = [{}, {}, {}, {}]
        for mesh in meshes:
            assert all(valid_frame(model, frame) for frame in mesh['frames'])
            out_mesh = {'name': mesh['name'], 'flags': mesh['flags'], 'frames': []}
            for frame in mesh['frames']:
                out_frame = []
                for col, array in enumerate(('vertices', 'indices', 'primitives', 'materials')):
                    src = frame[col]
                    if src not in maps[col]:
                        item = deepcopy(model[array][src])
                        if array == 'vertices' and offset != (0., 0., 0.):
                            raw = bytearray(item['data'])
                            for pos in range(0, len(raw), item['stride']):
                                xyz = struct.unpack_from('<3f', raw, pos)
                                struct.pack_into('<3f', raw, pos, *(a + b for a, b in zip(xyz, offset)))
                            item['data'] = bytes(raw)
                        maps[col][src] = len(output[array])
                        output[array].append(item)
                    out_frame.append(maps[col][src])
                out_mesh['frames'].append(tuple(out_frame))
            output['meshes'].append(out_mesh)
    validate_s3d(output)
    return output


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


def make_controller(original: bytes) -> tuple[bytes, dict]:
    text = original.decode('ascii')
    assert not re.search(r'HighwayIntersectionInfo_0x[0-9a-f]{4}F7A1\]', text, re.I)
    assert not re.search(r'0x5dd0f2[0-9a-f]{2}\b', text, re.I)
    ordering = next(line for line in text.splitlines(keepends=True)
                    if line.startswith('AddTypes') and ';Orth HSR x Orth GHSR' in line)
    # The GHSR button has sixteen rotation slots. Repeat the eight distinct
    # orientations in the second half so TAB works from every tool state.
    added = ('AddTypes     = ' + ', '.join(f'{n * 0x10000 + PUZZLE:X}' for n in range(16)) +
             ' ;Custom HSR over Diagonal GHSR - experimental\r\n')
    start = text.index('[HighwayIntersectionInfo_0x0000AAC1]')
    end = text.index('[HighwayIntersectionInfo_0x0000AAC2]', start)
    donor = text[start:end]
    new = donor.replace('AAC1', f'{PUZZLE:X}').replace('rail:', 'monorail:')
    new = new.replace('0x59F33015', f'0x{PREVIEW:08X}').replace('0x59F33010', f'0x{TILES[0]:08X}')
    new = new.replace('preview_rail_subrail____001', NEW_EFFECT_NAME.decode('ascii'))
    new = new.replace(';railUrail Dual - DTR Diagonal, Rail Straight Piece',
                      ';Custom straight HSR over diagonal GHSR; two heights of Monorail')
    new = new.replace('Costs = 60', 'Costs = 150')
    assert new.count('monorail:') == 4 and ' rail:' not in new
    assert '02010200' in new and '02000201' in new
    for n in range(8, 16):
        new += (f'[HighwayIntersectionInfo_0x{n * 0x10000 + PUZZLE:08X}]\r\n'
                f'CopyFrom = 0x{(n - 8) * 0x10000 + PUZZLE:X}\r\n')
    patched = text.replace(ordering, ordering + added, 1) + MARKER + new
    assert patched.split(MARKER)[0].replace(added, '', 1).encode('ascii') == original
    return patched.encode('ascii'), {'ordering_line': added.strip(), 'marker': MARKER,
                                    'new_rule_sections': 16, 'unique_orientations': 8,
                                    'donor_puzzle': 'AAC1',
                                    'original_rules_preserved_byte_for_byte': True,
                                    'new_rules_text': new}


def make_network_ini(original: bytes) -> tuple[bytes, dict]:
    # Latin-1 is a reversible byte mapping; NAM comments contain UTF-8 names.
    # Do not transcode or normalize any of the existing INI bytes.
    text = original.decode('latin1')
    header = '[Shadow remapping]\r\n'
    assert text.count(header) == 1
    added = (';BEGIN CUSTOM HSR OVER DIAGONAL GHSR SHADOWS\r\n' +
             ''.join(f'custom_hsr_diag_ghsr_{n} = 0x{tile:08X},0xFFFFFFF0,0x5DD31500,0x0000000F,0,0\r\n'
                     for n, tile in enumerate(TILES)) +
             ';END CUSTOM HSR OVER DIAGONAL GHSR SHADOWS\r\n')
    patched = text.replace(header, header + added, 1)
    assert patched.replace(added, '', 1).encode('latin1') == original
    return patched.encode('latin1'), {'insertion': added, 'resource': tgi_string(NETWORK_INI),
                                    'upper_shadow_source': '5dd31500',
                                    'original_ini_preserved_byte_for_byte': True}


def parse_donor_paths(raw: bytes) -> list[dict]:
    lines = [s.strip() for s in raw.decode('ascii').splitlines() if s.strip() and not s.startswith('--')]
    assert lines[:2] == ['SC4PATHS', '1.1'] and lines[3] == '0'
    routes, pos = [], 5
    for _ in range(int(lines[2])):
        transport, lane, entry, exit_, count = map(int, lines[pos:pos + 5]); pos += 5
        points = [tuple(map(float, s.split(','))) for s in lines[pos:pos + count]]; pos += count
        routes.append({'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_, 'points': points})
    assert pos == len(lines)
    return routes


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
        if pid == 0x20: values = f'Custom HSR over Diagonal GHSR - tile {number + 1}'
        if pid == 0x27812823: values = [*S3D, *range(tile, tile + 5)]
        output.extend(struct.pack('<IHHB', pid, kind, key, 0))
        if kind == 0xC00:
            data = values.encode('utf8'); assert key == 0x80
            output.extend(struct.pack('<I', len(data)) + data)
        else:
            if key == 0x80: output.extend(struct.pack('<I', len(values)))
            output.extend(struct.pack('<' + {0x300: 'I', 0x900: 'f'}[kind] * len(values), *values))
    return bytes(output)


def make_effect(donor: bytes) -> bytes:
    assert len(OLD_EFFECT_NAME) == len(NEW_EFFECT_NAME) == 27
    assert donor.count(OLD_EFFECT_NAME) == 4
    old, new = struct.pack('<I', 0x59F3D115), struct.pack('<I', PREVIEW)
    assert donor.count(old) == 2
    output = donor.replace(OLD_EFFECT_NAME, NEW_EFFECT_NAME).replace(old, new)
    assert output.replace(NEW_EFFECT_NAME, OLD_EFFECT_NAME).replace(new, old) == donor
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugins', type=Path, default=Path.home() / 'Documents/SimCity 4 Windows/Plugins')
    args = parser.parse_args()
    loaded = [helpers.load_named(args.plugins, name) for name in
              ('NetworkAddonMod_Controller.dat', 'High Speed Rail.dat', 'NetworkAddonMod_URail_Puzzle_Plugin.dat')]
    (controller_path, controller_raw, controller), (_, _, hsr), (_, _, urail) = loaded
    assert sha(controller_raw) == CONTROLLER_SHA256, 'NAM controller differs; re-audit before rebuilding.'
    installed, stats = helpers.inventory(args.plugins)
    assert not [(k, p) for k, p in installed.items() if 0x5DD0F200 <= k[2] <= 0x5DD0F2FF], 'Custom IDs already installed.'
    assert installed[RUL0] == [controller_path], 'Another RUL0 overlay is installed; merge it before building.'
    assert installed[NETWORK_INI] == [controller_path], 'Another NetworkINI overlay is installed; merge it before building.'
    output = {}
    output[RUL0], controller_audit = make_controller(controller[RUL0])
    output[NETWORK_INI], shadow_audit = make_network_ini(controller[NETWORK_INI])
    model_audits = []
    for number, (tile, ground_id) in enumerate(zip(TILES, (0x59F3D110, 0x59F3D120))):
        for zoom in range(5):
            # Native HSR supplies one model for every zoom, via its exemplar.
            model, audit = crossing_model(urail[*S3D, ground_id + 4], hsr[*S3D, 0x5DD31500])
            output[*S3D, tile + zoom] = model
            model_audits.append({'tile': f'{tile:08x}', 'zoom': zoom, **audit})
        output[*PATH, tile] = make_paths(urail[*PATH, ground_id], hsr[*PATH, 0x5DD31500])
        output[*EXEMPLAR, tile] = make_exemplar(hsr[*EXEMPLAR, 0x5DCF0A00], tile, number)
        label = TITLE.encode('utf-16-le')
        output[*LTEXT, tile] = struct.pack('<HH', len(label) // 2, 0x1000) + label
    preview_sources = []
    for number, tile in enumerate(TILES):
        model = parse_s3d(output[*S3D, tile + 4])
        preview_sources.append((model, model['meshes'], (0., 0., 16. * number)))
    output[*S3D, PREVIEW] = pack_s3d(combine_meshes(preview_sources))
    output[*EFFECT, PREVIEW] = make_effect(urail[*EFFECT, 0x59F3D115])
    texture_ids = sorted({t for tile in TILES for mat in parse_s3d(output[*S3D, tile + 4])['materials'] for t in mat['textures']})
    textures = {}
    for tid in texture_ids:
        matches = [(k, paths) for k, paths in installed.items() if k[0] == 0x7AB50E44 and k[2] == tid]
        assert matches, f'Texture {tid:08x} is missing'
        textures[f'{tid:08x}'] = [{'tgi': tgi_string(k), 'files': [str(p) for p in paths]} for k, paths in matches]
    for zoom in range(5):
        assert (0x7AB50E44, 0x2BC2759A, 0x5DD31500 + zoom) in installed, 'Native upper HSR shadow missing'
    dat = helpers.pack_dbpf(output)
    assert entries(dat) == output
    dist = HERE / 'dist'; folder = dist / 'zzz_Custom_HSR_Over_Diagonal_GHSR'
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / 'zzz_Custom_HSR_Over_Diagonal_GHSR_NAM50.dat'
    destination.write_bytes(dat)
    (dist / 'custom-rules.txt').write_text(controller_audit.pop('new_rules_text'), newline='')
    for tile in TILES: (dist / f'{tile:08x}.sc4path').write_bytes(output[*PATH, tile])
    manifest = {'name': TITLE, 'built_for_date': '2026-10-18',
                'status': 'experimental; staged outside Plugins; in-game testing required',
                'output': str(destination), 'bytes': len(dat), 'sha256': sha(dat),
                'tile_ids': [f'{tile:08x}' for tile in TILES], 'preview_id': f'{PREVIEW:08x}',
                'puzzle_id': f'{PUZZLE:04x}', 'footprint_tiles': [1, 2], 'resources': len(output),
                'donors': [{'path': str(p), 'sha256': sha(raw)} for p, raw, resources in loaded],
                'controller_audit': controller_audit, 'shadow_audit': shadow_audit,
                'texture_dependencies': textures, 'models': model_audits,
                'installed_resource_inventory': stats, 'new_resource_id_collisions': 0,
                'resource_list': [{'tgi': tgi_string(k), 'bytes': len(v), 'sha256': sha(v)} for k, v in sorted(output.items())],
                'limitations': ['Straight elevated HSR over diagonal GHSR; eight rotated/mirrored variants.',
                    'Static puzzle piece; does not propagate the HSR/GHSR overrides into approaches.',
                    'Exact NAM 50 RUL0 and NetworkINI overlays; remove before a NAM update.',
                    'Other custom overlays of those same resources must be merged before use.',
                    'Placement, previews, shadows, traffic and bulldozing require an in-game test.'],
                'credits': 'NAM Team original geometry, textures, paths, previews and construction rules. Private local derivative.'}
    (dist / 'build-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'output': str(destination), 'bytes': len(dat), 'resources': len(output), 'sha256': sha(dat)}, indent=2))


if __name__ == '__main__':
    main()
