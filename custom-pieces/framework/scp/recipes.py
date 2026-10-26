"""Piece recipes: return asset resources and author deltas, never whole NAM overlays."""
from copy import deepcopy
import re
import struct
from .dbpf import exemplar, encode_exemplar, require
from .models import parse_s3d, pack_s3d, valid_frame, validate_s3d, bounds
S3D=(0x5AD0E817,0xBADB57F1)
PATH=(0x296678F7,0xA966883F)
EXEMPLAR=(0x6534284A,0xA8434037)
EFFECT=(0xEA5118B0,0xEA5118B1)
LTEXT=(0x2026960B,0x2A592FD1)


def family(text, source_id):
    start = text.index(f'[HighwayIntersectionInfo_0x0000{source_id}]')
    following = list(re.finditer(r'^\[HighwayIntersectionInfo_0x([0-9a-fA-F]{8})\]', text[start:], re.M))
    for match in following[1:]:
        if int(match[1], 16) & 0xffff != int(source_id, 16):
            return text[start:start + match.start()]
    raise ValueError(f'Missing end of native construction family {source_id}')


def label(text):
    raw = text.encode('utf-16-le')
    return struct.pack('<HH', len(raw) // 2, 0x1000) + raw


def tile_exemplar(donor, tile, title):
    record = exemplar(donor)
    for prop in record['properties']:
        if int(prop['id'], 16) == 0x20:
            prop['values'] = title
        elif int(prop['id'], 16) == 0x27812823:
            prop['values'] = [*S3D, *range(tile, tile + 5)]
    return encode_exemplar(record)


def effect_clone(donor, old_name, new_name, old_iid, new_iid):
    old, new = old_name.encode('ascii'), new_name.encode('ascii')
    require(len(old) == len(new) and donor.count(old) == 4, 'Preview effect name length/topology mismatch')
    before, after = struct.pack('<I', old_iid), struct.pack('<I', new_iid)
    require(donor.count(before) == 2, 'Native effect model reference mismatch')
    result = donor.replace(old, new).replace(before, after)
    require(result.replace(new, old).replace(after, before) == donor, 'Effect clone is not reversible')
    return result



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









def build_piece(spec, context):
    """Dispatch to the explicitly registered transport-domain implementation."""
    from .providers import domain_module
    return domain_module(spec, 'recipes').build_piece(spec, context)
