"""Compose a visible surface-tram crossing beneath NAM's elevated HSR deck.

Only the Python standard library is required. Inputs and outputs are unpacked
S3D (3DMD) resource bytes, not complete DAT archives. The caller supplies the
installed NAM 50 donor resources and owns DBPF archive packaging.

The S3D layout follows DBPFKit/src/S3DReader.cpp, with an important detail:
the installed donors' PRIM length fields overstate their real lengths by four
bytes per primitive block. Parse their counted contents, as DBPFKit does, and
emit actual chunk lengths. Raw vertex attributes, materials and animation
metadata are retained; only the HSR vertex positions and resource-array
references change.
"""

from __future__ import annotations

from copy import deepcopy
import argparse
import hashlib
import json
import math
from pathlib import Path
import struct


class ModelError(ValueError):
    """An S3D donor has an unsupported layout or an unsafe reference."""


class Reader:
    def __init__(self, data: bytes):
        self.data, self.pos = data, 0

    def take(self, length: int) -> bytes:
        if length < 0 or self.pos + length > len(self.data):
            raise ModelError(f"S3D read past end at byte {self.pos}")
        result = self.data[self.pos:self.pos + length]
        self.pos += length
        return result

    def unpack(self, fmt: str):
        return struct.unpack('<' + fmt, self.take(struct.calcsize('<' + fmt)))

    def chunk(self, name: bytes) -> tuple[int, int]:
        start = self.pos
        actual = self.take(4)
        if actual != name:
            raise ModelError(f"Expected {name!r}, found {actual!r} at {start}")
        return start, self.unpack('I')[0]


def vertex_stride(fmt: int) -> int:
    if fmt & 0x80000000:
        coordinates, colors, textures = fmt & 3, (fmt >> 8) & 3, (fmt >> 14) & 3
    else:
        coordinates, colors, textures = {
            1: (1, 1, 0), 2: (1, 0, 1), 3: (1, 0, 2),
            10: (1, 1, 1), 11: (1, 1, 2),
        }.get(fmt, (0, 0, 0))
    if coordinates != 1:
        raise ModelError(f"Unsupported vertex format 0x{fmt:08x}")
    return coordinates * 12 + colors * 4 + textures * 8


def parse_s3d(data: bytes) -> dict:
    """Read NAM donor S3Ds without losing raw material/vertex attributes."""
    r = Reader(data)
    if r.take(4) != b'3DMD':
        raise ModelError("Missing 3DMD signature")
    total, = r.unpack('I')
    if total != len(data):
        raise ModelError(f"S3D total length {total} != actual {len(data)}")
    lengths = []

    def begin(name: bytes):
        start, declared = r.chunk(name)
        return name, start, declared

    def end(chunk):
        name, start, declared = chunk
        lengths.append({'chunk': name.decode(), 'declared': declared,
                        'actual': r.pos - start})
        if declared != r.pos - start and name != b'PRIM':
            raise ModelError(f"Unexpected {name.decode()} chunk length")

    c = begin(b'HEAD')
    version = r.unpack('HH')
    if version != (1, 5):
        raise ModelError(f"Only donor version 1.5 is supported, found {version}")
    end(c)

    c = begin(b'VERT')
    vertices = []
    for _ in range(r.unpack('I')[0]):
        flags, count, fmt = r.unpack('HHI')
        stride = vertex_stride(fmt)
        vertices.append({'flags': flags, 'format': fmt, 'stride': stride,
                         'data': r.take(count * stride)})
    end(c)

    c = begin(b'INDX')
    indices = []
    for _ in range(r.unpack('I')[0]):
        flags, stride, count = r.unpack('HHH')
        if stride != 2:
            raise ModelError(f"Unsupported index stride {stride}")
        indices.append({'flags': flags, 'stride': stride,
                        'values': r.unpack('H' * count)})
    end(c)

    c = begin(b'PRIM')
    primitives = []
    for _ in range(r.unpack('I')[0]):
        primitives.append([r.unpack('III') for _ in range(r.unpack('H')[0])])
    end(c)

    c = begin(b'MATS')
    materials = []
    for _ in range(r.unpack('I')[0]):
        start = r.pos
        flags, alpha, depth, src, dst, threshold, material_class, reserved, count = r.unpack('IBBBB H I BB')
        textures = []
        for _ in range(count):
            texture, wrap_s, wrap_t, mag, min_filter, rate, mode, length = r.unpack('IBBBBHHB')
            name = r.take(length)
            textures.append(texture)
        materials.append({'raw': data[start:r.pos], 'textures': textures})
    end(c)

    c = begin(b'ANIM')
    header = r.take(14)  # frames, rate, mode, flags, displacement
    frame_count, = struct.unpack_from('<H', header)
    meshes = []
    for _ in range(r.unpack('H')[0]):
        length, flags = r.unpack('BB')
        name = r.take(length)
        meshes.append({'name': name, 'flags': flags,
                       'frames': [r.unpack('HHHH') for _ in range(frame_count)]})
    end(c)

    trailing = []
    while r.pos < len(data):
        start = r.pos
        name = r.take(4)
        length, = r.unpack('I')
        r.take(length - 8)
        trailing.append((name, data[start:r.pos]))
    return {'version': version, 'vertices': vertices, 'indices': indices,
            'primitives': primitives, 'materials': materials,
            'anim_header': header, 'meshes': meshes, 'trailing': trailing,
            'source_chunk_lengths': lengths}


def pack_s3d(model: dict) -> bytes:
    def chunk(name: bytes, payload: bytes) -> bytes:
        return name + struct.pack('<I', len(payload) + 8) + payload

    chunks = [chunk(b'HEAD', struct.pack('<HH', *model['version']))]
    data = bytearray(struct.pack('<I', len(model['vertices'])))
    for vb in model['vertices']:
        data.extend(struct.pack('<HHI', vb['flags'], len(vb['data']) // vb['stride'], vb['format']))
        data.extend(vb['data'])
    chunks.append(chunk(b'VERT', data))
    data = bytearray(struct.pack('<I', len(model['indices'])))
    for ib in model['indices']:
        data.extend(struct.pack('<HHH', ib['flags'], ib['stride'], len(ib['values'])))
        data.extend(struct.pack('<' + 'H' * len(ib['values']), *ib['values']))
    chunks.append(chunk(b'INDX', data))
    data = bytearray(struct.pack('<I', len(model['primitives'])))
    for block in model['primitives']:
        data.extend(struct.pack('<H', len(block)))
        for primitive in block:
            data.extend(struct.pack('<III', *primitive))
    chunks.append(chunk(b'PRIM', data))
    chunks.append(chunk(b'MATS', struct.pack('<I', len(model['materials'])) +
                        b''.join(mat['raw'] for mat in model['materials'])))
    data = bytearray(model['anim_header'] + struct.pack('<H', len(model['meshes'])))
    for mesh in model['meshes']:
        data.extend(struct.pack('<BB', len(mesh['name']), mesh['flags']))
        data.extend(mesh['name'])
        for frame in mesh['frames']:
            data.extend(struct.pack('<HHHH', *frame))
    chunks.append(chunk(b'ANIM', data))
    chunks.extend(raw for name, raw in model['trailing'])
    payload = b''.join(chunks)
    return b'3DMD' + struct.pack('<I', len(payload) + 8) + payload


def positions(vertex_block: dict) -> list[tuple[float, float, float]]:
    return [struct.unpack_from('<3f', vertex_block['data'], offset)
            for offset in range(0, len(vertex_block['data']), vertex_block['stride'])]


def bounds(vertex_block: dict) -> list[list[float]]:
    points = positions(vertex_block)
    return [[min(point[axis] for point in points), max(point[axis] for point in points)]
            for axis in range(3)]


def valid_frame(model: dict, frame: tuple) -> bool:
    return all(0 <= value < len(model[array]) for value, array in
               zip(frame, ('vertices', 'indices', 'primitives', 'materials')))


def validate_s3d(model: dict) -> dict:
    """Validate every render reference, index and primitive, and finite coordinates."""
    used_vertices, used_indices, used_primitives, used_materials = [set() for _ in range(4)]
    triangles = 0
    for mesh in model['meshes']:
        if len(mesh['frames']) != struct.unpack_from('<H', model['anim_header'])[0]:
            raise ModelError('Animation frame count mismatch')
        for frame in mesh['frames']:
            if not valid_frame(model, frame):
                raise ModelError(f"Dangling animation reference {frame}")
            vi, ii, pi, mi = frame
            for used, index in zip((used_vertices, used_indices, used_primitives, used_materials), frame):
                used.add(index)
            vertex_count = len(positions(model['vertices'][vi]))
            for index in model['indices'][ii]['values']:
                if index >= vertex_count:
                    raise ModelError(f'Vertex index {index} >= vertex count {vertex_count}')
            for kind, first, length in model['primitives'][pi]:
                if kind != 0 or length % 3:
                    raise ModelError(f'Unsupported/non-triangular primitive {(kind, first, length)}')
                if first + length > len(model['indices'][ii]['values']):
                    raise ModelError('Primitive exceeds index buffer')
                triangles += length // 3
    for vb in model['vertices']:
        if not all(math.isfinite(value) for point in positions(vb) for value in point):
            raise ModelError('Non-finite vertex coordinate')
    for array, used in zip(('vertices', 'indices', 'primitives', 'materials'),
                           (used_vertices, used_indices, used_primitives, used_materials)):
        if used != set(range(len(model[array]))):
            raise ModelError(f'Unreferenced output {array}: {set(range(len(model[array]))) - used}')
    return {'all_animation_references_valid': True, 'all_vertex_indices_valid': True,
            'all_primitive_ranges_valid': True, 'all_output_buffers_used': True,
            'all_vertex_positions_finite': True, 'triangles': triangles,
            'mesh_count': len(model['meshes']),
            'bounds_xyz_m': [bounds(vb) for vb in model['vertices']],
            'textures': [f'{texture:08x}' for mat in model['materials'] for texture in mat['textures']]}


def build_crossing_model(glr_donor: bytes, hsr_donor: bytes) -> bytes:
    """Return a model with GLR along Z, elevated HSR along X, in donor coordinates.

    Expected inputs are NAM50 S3Ds 580e0700 (GLR x Monorail) and 5dd31500
    (HSR straight), group badb57f1. GLR mesh zero is the ground textured quad;
    its material and UVs are copied exactly. All original elevated Monorail
    meshes are omitted. The HSR's complete valid deck geometry is rotated
    clockwise 90 degrees around Y: (x, y, z) -> (z, y, -x). This is a proper
    rotation, so triangle winding is unchanged. No height or rail-spacing
    adjustment is made. The HSR donor has no ground-reaching support pillar.

    Five stale HSR animation meshes point outside its one-buffer arrays. They
    are discarded; the valid mesh remains byte-identical except for remapped
    references. Both donors use identical single-frame animation settings.
    """
    glr, hsr = parse_s3d(glr_donor), parse_s3d(hsr_donor)
    if glr['anim_header'] != hsr['anim_header']:
        raise ModelError('Donor animation headers differ')
    if struct.unpack_from('<H', glr['anim_header'])[0] != 1:
        raise ModelError('Only these static, one-frame donors are supported')
    # The original donors contain no matrix transforms: PROP and REGP are empty.
    if glr['trailing'] != hsr['trailing']:
        raise ModelError('Trailing donor chunks differ; transforms cannot be silently discarded')
    if any(len(raw) != 12 or raw[8:] != b'\0' * 4 for name, raw in glr['trailing']):
        raise ModelError('Unexpected non-empty donor matrix/property chunks')
    ground_meshes = [mesh for mesh in glr['meshes'] if
                     all(valid_frame(glr, frame) and
                         max(abs(value) for value in bounds(glr['vertices'][frame[0]])[1]) < 0.001
                         for frame in mesh['frames'])]
    deck_meshes = [mesh for mesh in hsr['meshes'] if all(valid_frame(hsr, frame) for frame in mesh['frames'])]
    if len(ground_meshes) != 1 or len(deck_meshes) != 1:
        raise ModelError('Unexpected donor ground/deck mesh topology')
    if bounds(hsr['vertices'][deck_meshes[0]['frames'][0][0]])[1][0] < 13:
        raise ModelError('HSR donor has ground-reaching geometry; a pillar would obstruct the tram')

    output = {'version': glr['version'], 'vertices': [], 'indices': [],
              'primitives': [], 'materials': [], 'anim_header': glr['anim_header'],
              'meshes': [], 'trailing': deepcopy(glr['trailing'])}
    for donor, meshes, rotate in ((glr, ground_meshes, False), (hsr, deck_meshes, True)):
        maps = [{}, {}, {}, {}]
        for mesh in meshes:
            out_mesh = {'name': mesh['name'], 'flags': mesh['flags'], 'frames': []}
            for frame in mesh['frames']:
                out_frame = []
                for column, array in enumerate(('vertices', 'indices', 'primitives', 'materials')):
                    source_index = frame[column]
                    if source_index not in maps[column]:
                        item = deepcopy(donor[array][source_index])
                        if array == 'vertices' and rotate:
                            raw = bytearray(item['data'])
                            for offset in range(0, len(raw), item['stride']):
                                x, y, z = struct.unpack_from('<3f', raw, offset)
                                struct.pack_into('<3f', raw, offset, z, y, -x)
                            item['data'] = bytes(raw)
                        maps[column][source_index] = len(output[array])
                        output[array].append(item)
                    out_frame.append(maps[column][source_index])
                out_mesh['frames'].append(tuple(out_frame))
            output['meshes'].append(out_mesh)
    validate_s3d(output)
    result = pack_s3d(output)
    validate_s3d(parse_s3d(result))
    return result


def audit_crossing_model(glr_donor: bytes, hsr_donor: bytes, output: bytes) -> dict:
    glr, hsr, model = map(parse_s3d, (glr_donor, hsr_donor, output))
    glr_original = glr['meshes'][0]
    ground_frame = glr_original['frames'][0]
    out_ground, out_deck = model['meshes'][0]['frames'][0], model['meshes'][1]['frames'][0]
    expected_hsr_points = [(z, y, -x) for x, y, z in positions(hsr['vertices'][0])]
    if positions(model['vertices'][out_deck[0]]) != expected_hsr_points:
        raise ModelError('HSR rotation failed to reproduce exact source coordinates')
    source_deck, result_deck = hsr['vertices'][0], model['vertices'][out_deck[0]]
    if source_deck['format'] != result_deck['format'] or source_deck['flags'] != result_deck['flags']:
        raise ModelError('HSR vertex format or flags were altered')
    for offset in range(0, len(source_deck['data']), source_deck['stride']):
        end = offset + source_deck['stride']
        if source_deck['data'][offset + 12:end] != result_deck['data'][offset + 12:end]:
            raise ModelError('HSR UVs or additional vertex attributes were altered')
    for column, array in enumerate(('vertices', 'indices', 'primitives', 'materials')):
        if model[array][out_ground[column]] != glr[array][ground_frame[column]]:
            raise ModelError(f'Ground {array} was altered')
        if array != 'vertices' and model[array][out_deck[column]] != hsr[array][0]:
            raise ModelError(f'HSR {array} was altered')
    return {
        'donors': {'ground': '5ad0e817-badb57f1-580e0700',
                   'hsr': '5ad0e817-badb57f1-5dd31500'},
        'sha256': {'ground_donor': hashlib.sha256(glr_donor).hexdigest(),
                   'hsr_donor': hashlib.sha256(hsr_donor).hexdigest(),
                   'crossing': hashlib.sha256(output).hexdigest()},
        'output_bytes': len(output),
        'geometry': {
            'ground': 'Original ground quad, UVs, material and texture preserved exactly.',
            'hsr': 'Entire valid straight HSR deck rotated (x,y,z) -> (z,y,-x). Height/UVs unchanged.',
            'removed': 'All elevated Monorail meshes; five dangling HSR animation mesh records.',
            'support_clearance_m': bounds(model['vertices'][out_deck[0]])[1][0],
            'pillar': 'No ground-reaching pillar exists in the selected HSR donor.',
            'alignment': 'GLR runs north/south (Z); HSR east/west (X), matching unrotated 580e0700 paths.',
        },
        'retained_exactly': ['Ground vertices and UVs', 'Ground index and primitive buffers',
                             'HSR index and primitive buffers', 'Both used raw material records',
                             'UV coordinates of HSR vertices', 'Animation header, mesh names and flags',
                             'Empty PROP and REGP chunks (no donor matrix transforms exist)'],
        'discarded_invalid_hsr_meshes': [
            {'name': mesh['name'].rstrip(b'\0').decode('ascii', 'replace'),
             'frames': mesh['frames']}
            for mesh in hsr['meshes'] if not all(valid_frame(hsr, frame) for frame in mesh['frames'])],
        'donor_chunk_length_anomalies': {
            'ground': [item for item in glr['source_chunk_lengths'] if item['declared'] != item['actual']],
            'hsr': [item for item in hsr['source_chunk_lengths'] if item['declared'] != item['actual']]},
        'checks': validate_s3d(model),
        'verification_limit': 'Binary geometry/reference audit only; no in-game rendering or traffic test.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('glr_s3d', type=Path)
    parser.add_argument('hsr_s3d', type=Path)
    parser.add_argument('output_s3d', type=Path)
    parser.add_argument('--audit', type=Path)
    args = parser.parse_args()
    glr, hsr = args.glr_s3d.read_bytes(), args.hsr_s3d.read_bytes()
    output = build_crossing_model(glr, hsr)
    args.output_s3d.write_bytes(output)
    audit = audit_crossing_model(glr, hsr, output)
    if args.audit:
        args.audit.write_text(json.dumps(audit, indent=2) + '\n')
    print(json.dumps(audit, indent=2))


if __name__ == '__main__':
    main()
