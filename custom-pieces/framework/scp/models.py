"""Generic S3D model parsing, packing and structural validation.

The parser retains raw vertex attributes, materials and animation metadata.
Rail-specific donor composition and profile checks belong to scp_hsr.
"""

from __future__ import annotations

import math
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
