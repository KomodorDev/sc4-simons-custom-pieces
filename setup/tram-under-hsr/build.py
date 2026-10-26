"""Build a separate NAM 50 surface-tram-under-HSR puzzle piece, without installing it.

Run: python3 build.py
Inputs are the user's installed NAM assets. Output is an uncompressed DBPF 1.0
archive. Only RUL0 is overlaid; all existing rules remain byte-for-byte intact.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import sys

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
sys.path.insert(0, str(PROJECT / 'setup/cam-install/runtime-audit'))
from read_dbpf import entries, decompress, exemplar, tgi_string
from model_tools import build_crossing_model, audit_crossing_model, parse_s3d

TILE = 0x5DD0F100
PUZZLE = 0xF7A0
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
EXEMPLAR = (0x6534284A, 0xA8434037)
EFFECT = (0xEA5118B0, 0xEA5118B1)
SHADOW_TEXTURE = (0x7AB50E44, 0x2BC2759A)
LTEXT = (0x2026960B, 0x2A592FD1)
CONTROLLER_SHA256 = 'd903540cdf772b4ed6a072c504e006e1cac384f8027ce58a288a5a9654f94161'
OLD_EFFECT_NAME = b'preview_rail_dualnetwork029'
NEW_EFFECT_NAME = b'preview_hsr_tram_cross00001'
TITLE = 'HSR over Ground Tram - Right-Angle Crossing (Experimental)'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_index(path: Path) -> list[tuple[int, int, int]]:
    """Read only a DBPF header/index, without loading large donor archives."""
    with path.open('rb') as f:
        header = f.read(96)
        if len(header) != 96 or header[:4] != b'DBPF':
            return []
        count, offset, size = struct.unpack_from('<3I', header, 36)
        if size != count * 20:
            raise ValueError(f'Unsupported DBPF index in {path}')
        f.seek(offset)
        raw = f.read(size)
    if len(raw) != size:
        raise ValueError(f'Truncated DBPF index in {path}')
    return [struct.unpack_from('<3I', raw, i * 20) for i in range(count)]


def inventory(plugins: Path) -> tuple[dict, dict]:
    locations, stats = {}, {'files': 0, 'resources': 0}
    for path in sorted(plugins.rglob('*')):
        if not path.is_file() or path.suffix.lower() not in {'.dat', '.sc4model', '.sc4lot', '.sc4desc'}:
            continue
        keys = read_index(path)
        if keys:
            stats['files'] += 1
            stats['resources'] += len(keys)
        for key in keys:
            locations.setdefault(key, []).append(path)
    return locations, stats


def pack_dbpf(resources: dict) -> bytes:
    header = bytearray(96)
    header[:4] = b'DBPF'
    struct.pack_into('<2I', header, 4, 1, 0)
    struct.pack_into('<I', header, 32, 7)
    body, index = bytearray(), bytearray()
    for key, data in sorted(resources.items()):
        index.extend(struct.pack('<5I', *key, 96 + len(body), len(data)))
        body.extend(data)
    struct.pack_into('<3I', header, 36, len(resources), 96 + len(body), len(index))
    return bytes(header + body + index)


def encode_exemplar(original: bytes) -> bytes:
    record = exemplar(original)
    output = bytearray(b'EQZB1###' + struct.pack('<3I', *record['parent']) +
                       struct.pack('<I', len(record['properties'])))
    for p in record['properties']:
        pid, kind, key = int(p['id'], 16), int(p['type'], 16), int(p['key_type'], 16)
        values = p['values']
        if pid == 0x20:
            values = 'Custom HSR over Ground Tram - orthogonal'
        elif pid == 0x27812823:
            values = [*S3D, *range(TILE, TILE + 5)]
        output.extend(struct.pack('<IHHB', pid, kind, key, 0))
        if kind == 0xC00:
            data = values.encode('utf8')
            assert key == 0x80
            output.extend(struct.pack('<I', len(data)) + data)
        else:
            if key == 0x80:
                output.extend(struct.pack('<I', len(values)))
            output.extend(struct.pack('<' + {0x300: 'I', 0x900: 'f'}[kind] * len(values), *values))
    return bytes(output)


def make_controller(original: bytes) -> tuple[bytes, dict]:
    text = original.decode('ascii')
    for i in range(8):
        assert not re.search(rf'^\[HighwayIntersectionInfo_0x{i * 0x10000 + PUZZLE:08X}\]', text, re.M | re.I)
    assert not re.search(r'\b0x5dd0f10[0-5]\b', text, re.I)
    ordering = next(line for line in text.splitlines(keepends=True)
                    if line.startswith('AddTypes') and ';Ground Light RailxMonorail Puzzle Piece' in line)
    added = ('AddTypes     = ' + ', '.join(f'{i * 0x10000 + PUZZLE:X}' for i in range(8)) +
             ' ;Custom HSR over Ground Tram - experimental\r\n')
    assert text.count(ordering) == 1
    patched = text.replace(ordering, ordering + added, 1)
    start = text.index('[HighwayIntersectionInfo_0x0000B12F]')
    last = text.index('[HighwayIntersectionInfo_0x0007B12F]', start)
    finish = text.index('[HighwayIntersectionInfo_', last + 1)
    donor = text[start:finish]
    new = donor.replace('B12F', f'{PUZZLE:X}').replace('580e070', '5dd0f10')
    new = new.replace(OLD_EFFECT_NAME.decode(), NEW_EFFECT_NAME.decode())
    new = new.replace('Ground Light RailxMonorail Puzzle Piece', 'Custom HSR over Ground Tram')
    suffix = '\r\n;BEGIN CUSTOM HSR TRAM CROSSING - NAM 50 exact-controller overlay\r\n' + new
    patched += suffix
    # Reversing only the additions must recover every byte of the original.
    assert patched[:-len(suffix)].replace(added, '', 1).encode('ascii') == original
    return patched.encode('ascii'), {'ordering_line': added.strip(), 'new_rule_sections': 8,
                                    'original_rules_preserved_byte_for_byte': True,
                                    'new_rules_text': new}


def make_effect(original: bytes) -> bytes:
    assert len(OLD_EFFECT_NAME) == len(NEW_EFFECT_NAME)
    assert original.count(OLD_EFFECT_NAME) == 4
    old, new = struct.pack('<I', 0x580E0705), struct.pack('<I', TILE + 5)
    assert original.count(old) == 2
    output = original.replace(OLD_EFFECT_NAME, NEW_EFFECT_NAME).replace(old, new)
    assert len(output) == len(original)
    assert output.replace(NEW_EFFECT_NAME, OLD_EFFECT_NAME).replace(new, old) == original
    return output


def load_named(root: Path, filename: str) -> tuple[Path, bytes, dict]:
    paths = list(root.rglob(filename))
    if len(paths) != 1:
        raise ValueError(f'Expected exactly one {filename}, found {len(paths)}')
    path = paths[0]
    raw = path.read_bytes()
    return path, raw, {k: decompress(v) for k, v in entries(raw).items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugins', type=Path, default=Path.home() / 'Documents/SimCity 4 Windows/Plugins')
    args = parser.parse_args()
    controller_path, controller_raw, controller = load_named(args.plugins, 'NetworkAddonMod_Controller.dat')
    if sha(controller_raw) != CONTROLLER_SHA256:
        raise ValueError('Installed NAM controller differs from the audited NAM 50 build. Re-audit before rebuilding.')
    glr_path, glr_raw, glr = load_named(args.plugins, 'NetworkAddonMod_GroundLightRail_Plugin.dat')
    hsr_path, hsr_raw, hsr = load_named(args.plugins, 'High Speed Rail.dat')
    installed, stats = inventory(args.plugins)
    collisions = [(k, v) for k, v in installed.items() if TILE <= k[2] <= TILE + 5]
    if collisions:
        raise ValueError(f'Custom resource IDs already installed: {collisions}')
    output = {}
    patched, controller_audit = make_controller(controller[RUL0])
    output[RUL0] = patched
    models = []
    for zoom in range(5):
        old = glr[*S3D, 0x580E0700 + zoom]
        model = build_crossing_model(old, hsr[*S3D, 0x5DD31500])
        output[*S3D, TILE + zoom] = model
        models.append(audit_crossing_model(old, hsr[*S3D, 0x5DD31500], model))
        # Placeholder: native Monorail-crossing shadows do not match the wider
        # HSR deck. Custom shadow images AND NetworkINI selection need work.
        output[*SHADOW_TEXTURE, TILE + zoom] = glr[*SHADOW_TEXTURE, 0x580E0700 + zoom]
    output[*S3D, TILE + 5] = output[*S3D, TILE + 4]
    output[*PATH, TILE] = glr[*PATH, 0x580E0700]
    output[*EXEMPLAR, TILE] = encode_exemplar(glr[*EXEMPLAR, 0x580E0700])
    output[*EFFECT, TILE] = make_effect(glr[*EFFECT, 0x580E0700])
    label = TITLE.encode('utf-16-le')
    output[*LTEXT, TILE] = struct.pack('<HH', len(label) // 2, 0x1000) + label
    texture_ids = sorted({int(tid, 16) for m in models for tid in m['checks']['textures']})
    texture_sources = {}
    for tid in texture_ids:
        matches = [(k, paths) for k, paths in installed.items() if k[0] == 0x7AB50E44 and k[2] == tid]
        if not matches:
            raise ValueError(f'Missing model texture {tid:08x}')
        texture_sources[f'{tid:08x}'] = [{'tgi': tgi_string(k), 'files': [str(p) for p in paths]}
                                                for k, paths in matches]
    dat = pack_dbpf(output)
    assert entries(dat) == output
    outdir = HERE / 'dist/zzz_Custom_Tram_Under_HSR'
    outdir.mkdir(parents=True, exist_ok=True)
    outfile = outdir / 'zzz_Custom_Tram_Under_HSR_NAM50.dat'
    outfile.write_bytes(dat)
    (HERE / 'dist/custom-rules.txt').write_text(controller_audit.pop('new_rules_text'), newline='')
    (HERE / 'dist/traffic-paths.sc4path').write_bytes(output[*PATH, TILE])
    manifest = {
        'name': TITLE, 'built_for_date': '2026-10-18', 'status': 'experimental; not installed or tested in game',
        'output': str(outfile), 'bytes': len(dat), 'sha256': sha(dat),
        'tile_id': f'{TILE:08x}', 'puzzle_id': f'{PUZZLE:04x}', 'resources': len(output),
        'donors': [{'path': str(p), 'sha256': sha(raw)} for p, raw in
                   [(controller_path, controller_raw), (glr_path, glr_raw), (hsr_path, hsr_raw)]],
        'controller_audit': controller_audit,
        'texture_dependencies': texture_sources, 'installed_resource_inventory': stats,
        'new_resource_id_collisions': 0, 'models': models,
        'resource_list': [{'tgi': tgi_string(k), 'bytes': len(v), 'sha256': sha(v)} for k, v in sorted(output.items())],
        'limitations': ['One-tile orthogonal static puzzle piece; no draggable crossing rules.',
                        'Build HSR approaches independently on both sides; the piece does not propagate the HSR override.',
                        'Shadow images are unchanged Monorail-crossing placeholders; HSR-width shadows and shadow selection are unverified.',
                        'RUL0 overlay pinned to the exact installed NAM 50 controller. Remove before updating NAM.',
                        'In-game placement, preview, rotations, traffic, and bulldozing still require testing.'],
        'credits': 'NAM Team original HSR and GLR assets/rules; private local derivative prototype.',
    }
    (HERE / 'dist/build-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'output': str(outfile), 'bytes': len(dat), 'resources': len(output), 'sha256': sha(dat)}, indent=2))


if __name__ == '__main__':
    main()
