"""Static integration checks for the built crossing. These do not run SimCity 4."""
from pathlib import Path
import hashlib
import json
import re
import struct
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'setup/cam-install/runtime-audit'))
from read_dbpf import entries, decompress, exemplar
from model_tools import parse_s3d, validate_s3d

TILE = 0x5DD0F100
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)


def parse_paths(raw):
    lines = [line.strip() for line in raw.decode('ascii').splitlines()
             if line.strip() and not line.startswith('--')]
    assert lines[:2] == ['SC4PATHS', '1.1']
    count, stops, terrain = map(int, lines[2:5])
    assert stops == 0 and terrain == 1
    result, pos = [], 5
    for _ in range(count):
        transport, lane, entry, exit_, nodes = map(int, lines[pos:pos + 5])
        pos += 5
        points = [tuple(map(float, line.split(','))) for line in lines[pos:pos + nodes]]
        assert len(points) == nodes
        result.append({'transport': transport, 'lane': lane, 'entry': entry,
                       'exit': exit_, 'points': points})
        pos += nodes
    assert pos == len(lines)
    return result


def endpoints(paths, transport):
    return {(p['points'][0], p['points'][-1]) for p in paths if p['transport'] == transport}


def rotate(point, turns):
    x, y, z = point
    for _ in range(turns):
        x, y = y, -x
    return x, y, z


def edge(point):
    x, y, _ = point
    edges = [abs(x + 8) < 1e-6, abs(y - 8) < 1e-6,
             abs(x - 8) < 1e-6, abs(y + 8) < 1e-6]
    assert sum(edges) == 1
    return edges.index(True)  # SC4PATH: west, north, east, south


def main():
    manifest = json.loads((HERE / 'dist/build-manifest.json').read_text())
    path = Path(manifest['output'])
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == manifest['sha256']
    assert raw[:4] == b'DBPF'
    assert struct.unpack_from('<II', raw, 4) == (1, 0)
    assert struct.unpack_from('<I', raw, 32) == (7,)
    count, index, size = struct.unpack_from('<III', raw, 36)
    assert count == 16 and size == count * 20 and index + size == len(raw)
    ranges, tgiset = [], set()
    for n in range(count):
        kind, group, instance, offset, length = struct.unpack_from('<5I', raw, index + n * 20)
        assert 96 <= offset < index and offset + length <= index
        assert (kind, group, instance) not in tgiset
        tgiset.add((kind, group, instance))
        ranges.append((offset, offset + length))
    ranges.sort()
    assert ranges[0][0] == 96 and ranges[-1][1] == index
    assert all(a[1] == b[0] for a, b in zip(ranges, ranges[1:]))
    output = entries(raw)
    donors = []
    for item in manifest['donors']:
        donor_raw = Path(item['path']).read_bytes()
        assert hashlib.sha256(donor_raw).hexdigest() == item['sha256'], 'An installed donor changed'
        donors.append({k: decompress(v) for k, v in entries(donor_raw).items()})
    controller, glr, hsr = donors
    patched = output[RUL0].decode('ascii')
    marker = '\r\n;BEGIN CUSTOM HSR TRAM CROSSING - NAM 50 exact-controller overlay\r\n'
    assert patched.count(marker) == 1
    body, addition = patched.split(marker)
    ordering = manifest['controller_audit']['ordering_line'] + '\r\n'
    assert body.count(ordering) == 1
    assert body.replace(ordering, '', 1).encode('ascii') == controller[RUL0]
    sections = re.findall(r'^\[HighwayIntersectionInfo_0x([0-9A-Fa-f]+)\]', addition, re.M)
    assert [int(x, 16) for x in sections] == [0xF7A0 + n * 0x10000 for n in range(8)]
    assert '0x5dd0f105' in addition and '0x5dd0f100' in addition
    assert 'preview_hsr_tram_cross00001' in addition
    assert '580e070' not in addition.lower() and 'B12F' not in addition
    assert sum(k in set(controller) | set(glr) | set(hsr) for k in output) == 1
    model_checks = []
    for zoom in range(6):
        key = (0x5AD0E817, 0xBADB57F1, TILE + zoom)
        model_checks.append(validate_s3d(parse_s3d(output[key])))
    network = exemplar(output[0x6534284A, 0xA8434037, TILE])
    properties = {int(p['id'], 16): p['values'] for p in network['properties']}
    assert properties[0x10] == [11]
    assert properties[0x27812823] == [0x5AD0E817, 0xBADB57F1, *range(TILE, TILE + 5)]
    effect = output[0xEA5118B0, 0xEA5118B1, TILE]
    oldeffect = glr[0xEA5118B0, 0xEA5118B1, 0x580E0700]
    assert len(effect) == len(oldeffect)
    assert effect.count(b'preview_hsr_tram_cross00001') == 4
    assert effect.count(struct.pack('<I', TILE + 5)) == 2
    assert effect.replace(b'preview_hsr_tram_cross00001', b'preview_rail_dualnetwork029').replace(
        struct.pack('<I', TILE + 5), struct.pack('<I', 0x580E0705)) == oldeffect
    label = output[0x2026960B, 0x2A592FD1, TILE]
    chars, control = struct.unpack_from('<HH', label)
    assert control == 0x1000 and len(label) == 4 + chars * 2
    assert label[4:].decode('utf-16-le') == manifest['name']
    paths = parse_paths(output[0x296678F7, 0xA966883F, TILE])
    hsrpaths = parse_paths(hsr[0x296678F7, 0xA966883F, 0x5DD31500])
    assert len(paths) == 6
    ground = endpoints(paths, 6)
    assert ground == endpoints(paths, 3)
    assert ground == {((2., -8., 0.), (2., 8., 0.)), ((-2., 8., 0.), (-2., -8., 0.))}
    upper = endpoints(paths, 7)
    expected = {(rotate(a, 1), rotate(b, 1)) for a, b in endpoints(hsrpaths, 7)}
    assert upper == expected
    # Both routes have exact compatible endpoints under all four rotations.
    for angle in range(4):
        assert {(rotate(a, angle), rotate(b, angle)) for a, b in upper} == {
            (rotate(a, angle + 1), rotate(b, angle + 1)) for a, b in endpoints(hsrpaths, 7)}
        for a, b in {(rotate(a, angle), rotate(b, angle)) for a, b in ground}:
            assert a[2] == b[2] == 0 and sum(abs(v) == 8 for v in a[:2]) == 1
        for route in paths:
            assert edge(rotate(route['points'][0], angle)) == (route['entry'] + angle) % 4
            assert edge(rotate(route['points'][-1], angle)) == (route['exit'] + angle) % 4
    result = {'static_checks_passed': True, 'dbpf_resources': count,
              'checks': ['Header, index, resource bounds and duplicate TGIs',
                         'All original RUL0 rules and menu entries preserved byte-for-byte',
                         'Eight new puzzle rotations and unique preview/model/query IDs',
                         'Five zoom models plus preview: meshes, indices, primitives and materials',
                         'Exemplar model references and preview EffDir clone integrity',
                         'Ground tram and driving-mode paths in both directions',
                         'Exact HSR path endpoint matches under all four rotations',
                         'All six model texture dependencies exist in installed Plugins',
                         'Original donor files unchanged; prototype remains outside Plugins'],
              'in_game_placement_tested': False, 'in_game_rendering_tested': False,
              'in_game_traffic_tested': False, 'in_game_bulldozing_tested': False,
              'sha256': manifest['sha256']}
    (HERE / 'dist/verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
