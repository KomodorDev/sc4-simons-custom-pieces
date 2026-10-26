"""Repack compiled SCP meshes without changing their encoded triangles.

The budgets are conservative authoring choices, not asserted engine limits.
Native meshes and already-small SCP meshes retain their buffers exactly.
Only static, XYZ/UV, triangle-list SCP meshes can be split.  In particular,
this is not a geometric simplifier: even encoded degenerate triangles remain.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import struct

from .models import ModelError, pack_s3d, parse_s3d, valid_frame
from scp_hsr.single_track_models import _pack

MAX_VERTICES = 512
MAX_TRIANGLES = 512
_ARRAYS = ('vertices', 'indices', 'primitives')


def _authored(mesh):
    return mesh['name'].rstrip(b'\0').startswith(b'SCP ')


def _triangles(model, frame):
    """Yield original vertex bytes, in primitive and index order."""
    if not valid_frame(model, frame):
        raise ModelError('Render mesh has a dangling animation reference')
    vi, ii, pi, _ = frame
    vb, ib = model['vertices'][vi], model['indices'][ii]
    stride = vb['stride']
    if stride <= 0 or len(vb['data']) % stride:
        raise ModelError('Render mesh has a malformed vertex buffer')
    count = len(vb['data']) // stride
    for kind, first, length in model['primitives'][pi]:
        if kind != 0 or length % 3 or first + length > len(ib['values']):
            raise ModelError('Render repacking requires bounded triangle-list primitives')
        for position in range(first, first + length, 3):
            indices = ib['values'][position:position + 3]
            if any(index < 0 or index >= count for index in indices):
                raise ModelError('Render mesh has an out-of-range vertex index')
            yield tuple(vb['data'][index * stride:(index + 1) * stride] for index in indices)


def _metrics(model, mesh, frame=None):
    frames = mesh['frames']
    if not frames:
        raise ModelError('Authored render mesh has an invalid frame table')
    frame = frames[0] if frame is None else frame
    if not valid_frame(model, frame):
        raise ModelError('Authored render mesh has a dangling frame reference')
    vi, _, pi, _ = frame
    vb = model['vertices'][vi]
    return (len(vb['data']) // vb['stride'],
            sum(length // 3 for _, _, length in model['primitives'][pi]))


def assert_render_budget(model: dict) -> dict:
    """Check every authored mesh frame; leave donor meshes outside this policy."""
    count, = struct.unpack_from('<H', model['anim_header'])
    checked, maximum_vertices, maximum_triangles = 0, 0, 0
    for mesh in model['meshes']:
        if not _authored(mesh):
            continue
        if len(mesh['frames']) != count or count == 0:
            raise ModelError('Authored render mesh has an invalid animation frame count')
        for frame in mesh['frames']:
            vertices, triangles = _metrics(model, mesh, frame)
            checked += 1
            maximum_vertices = max(maximum_vertices, vertices)
            maximum_triangles = max(maximum_triangles, triangles)
            if vertices > MAX_VERTICES or triangles > MAX_TRIANGLES:
                raise ModelError(f'Authored SCP render mesh exceeds conservative render budget: '
                                 f'{vertices} vertices/{triangles} triangles '
                                 f'(budgets {MAX_VERTICES}/{MAX_TRIANGLES})')
    return {'authored_frames_checked': checked,
            'max_authored_vertices': maximum_vertices,
            'max_authored_triangles': maximum_triangles,
            'vertex_budget': MAX_VERTICES, 'triangle_budget': MAX_TRIANGLES}


def _fingerprints(model):
    """Ignore grouping, but retain every frame's ordered geometry/materials."""
    count, = struct.unpack_from('<H', model['anim_header'])
    hashes = []
    for frame_number in range(count):
        digest = hashlib.sha256()
        for mesh in model['meshes']:
            frame = mesh['frames'][frame_number]
            material = model['materials'][frame[3]]['raw']
            for triangle in _triangles(model, frame):
                digest.update(struct.pack('<I', len(material)))
                digest.update(material)
                for vertex in triangle:
                    digest.update(struct.pack('<I', len(vertex)))
                    digest.update(vertex)
        hashes.append(digest.hexdigest())
    return hashes


def repack_s3d(raw: bytes) -> tuple[bytes, dict]:
    """Split oversized authored groups and prove their triangle bytes unchanged.

    Returns ``(s3d_bytes, diagnostics)``.  No changes means the original byte
    object is returned, including its original chunk-length conventions.
    Shared buffers needed by an unchanged mesh are retained, with references
    remapped only if removal of an obsolete authored buffer shifts the table.
    """
    model = parse_s3d(raw)
    replacements = {}
    before = []
    for number, mesh in enumerate(model['meshes']):
        if not _authored(mesh):
            continue
        per_frame = [_metrics(model, mesh, frame) for frame in mesh['frames']]
        if not per_frame:
            raise ModelError('Authored render mesh has no animation frames')
        vertices = max(v for v, _ in per_frame)
        triangles = max(t for _, t in per_frame)
        before.append((vertices, triangles))
        if vertices <= MAX_VERTICES and triangles <= MAX_TRIANGLES:
            continue
        if any(frame != mesh['frames'][0] for frame in mesh['frames']):
            raise ModelError('Animated authored SCP meshes cannot be repacked')
        vi, ii, _, mi = mesh['frames'][0]
        vb = model['vertices'][vi]
        if vb['stride'] != 20:
            raise ModelError('Authored render repacking requires XYZ/UV vertices')
        expanded = [tuple(struct.unpack('<5f', vertex) for vertex in triangle)
                    for triangle in _triangles(model, mesh['frames'][0])]
        native = {'model': model, 'mesh': mesh, 'vb': vb,
                  'material': model['materials'][mi]}
        packed = parse_s3d(_pack(native, expanded, preserve_encoded_triangles=True))
        for chunk in packed['meshes']:
            chunk['name'] = mesh['name']
            chunk['flags'] = mesh['flags']
        replacements[number] = packed
    diagnostics = {'changed': bool(replacements), 'split_source_meshes': len(replacements),
                   'meshes_before': len(model['meshes']),
                   'authored_meshes_before': len(before),
                   'max_authored_vertices_before': max((v for v, _ in before), default=0),
                   'max_authored_triangles_before': max((t for _, t in before), default=0),
                   'vertex_budget': MAX_VERTICES, 'triangle_budget': MAX_TRIANGLES}
    if not replacements:
        return raw, {**diagnostics, 'meshes_after': len(model['meshes']),
                     **assert_render_budget(model),
                     'ordered_triangle_material_bytes_unchanged': True}

    retained = [set() for _ in _ARRAYS]
    for number, mesh in enumerate(model['meshes']):
        if number not in replacements:
            for frame in mesh['frames']:
                for used, index in zip(retained, frame):
                    used.add(index)
    output = deepcopy(model)
    maps = []
    for array, used in zip(_ARRAYS, retained):
        maps.append({old: new for new, old in enumerate(sorted(used))})
        output[array] = [deepcopy(model[array][old]) for old in sorted(used)]
    output['meshes'] = []
    for number, mesh in enumerate(model['meshes']):
        if number not in replacements:
            copy = deepcopy(mesh)
            copy['frames'] = [tuple(mapping[old] for mapping, old in zip(maps, frame)) + (frame[3],)
                              for frame in mesh['frames']]
            output['meshes'].append(copy)
            continue
        packed = replacements[number]
        material = mesh['frames'][0][3]
        offsets = tuple(len(output[array]) for array in _ARRAYS)
        for array in _ARRAYS:
            output[array].extend(deepcopy(packed[array]))
        for chunk in packed['meshes']:
            copy = deepcopy(chunk)
            copy['frames'] = [tuple(offset + index for offset, index in zip(offsets, frame)) + (material,)
                              for frame in chunk['frames']]
            output['meshes'].append(copy)
    if len(output['meshes']) > 65535 or any(len(output[array]) > 65535 for array in _ARRAYS):
        raise ModelError('Repacked model exceeds the conservative S3D group/reference budget')
    result = pack_s3d(output)
    reparsed = parse_s3d(result)
    fingerprints = _fingerprints(model)
    if _fingerprints(reparsed) != fingerprints:
        raise ModelError('Render repacking changed ordered triangle/material bytes')
    after = [_metrics(reparsed, mesh) for mesh in reparsed['meshes'] if _authored(mesh)]
    diagnostics.update(assert_render_budget(reparsed))
    diagnostics.update(meshes_after=len(reparsed['meshes']), authored_meshes_after=len(after),
                       max_authored_vertices_after=max((v for v, _ in after), default=0),
                       max_authored_triangles_after=max((t for _, t in after), default=0),
                       ordered_triangle_material_bytes_unchanged=True,
                       frame_triangle_material_sha256=fingerprints)
    return result, diagnostics
