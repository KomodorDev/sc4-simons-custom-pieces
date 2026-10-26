"""Independently compare the visible render state of two saved S3D models.

This check permits editor-label changes and different vertex/index grouping.
It preserves the ordered, oriented visible triangles in every animation frame,
including every encoded vertex attribute and the render flags/materials used
to draw them. Unsupported or invalid model structures fail explicitly.
"""

from __future__ import annotations

import hashlib
import math
import struct

from .models import ModelError, parse_s3d, validate_s3d


def _blob(digest, value: bytes) -> None:
    digest.update(struct.pack('<Q', len(value)))
    digest.update(value)


def s3d_render_fingerprint(raw: bytes) -> dict:
    """Fingerprint actual ordered draws, independent of names/buffer indices.

    Cyclically choosing another first vertex keeps a triangle's winding and
    is accepted. Reversing its winding, reordering distinct triangles, changing
    frame multiplicity or changing any encoded attribute/state is rejected by
    the resulting fingerprint. Bounds include all encoded vertex positions.
    """
    model = parse_s3d(raw)
    validate_s3d(model)
    if not model['meshes'] or not model['vertices']:
        raise ModelError('Render equivalence requires a visible model')
    frame_count = struct.unpack_from('<H', model['anim_header'])[0]
    if frame_count <= 0:
        raise ModelError('Render equivalence requires an animation frame')
    states = hashlib.sha256()
    _blob(states, struct.pack('<HH', *model['version']))
    _blob(states, model['anim_header'])
    for material in model['materials']:
        _blob(states, material['raw'])
    for tag, content in model['trailing']:
        _blob(states, tag)
        _blob(states, content)
    bounds = [[math.inf] * 3, [-math.inf] * 3]
    for vertices in model['vertices']:
        for offset in range(0, len(vertices['data']), vertices['stride']):
            position = struct.unpack_from('<3f', vertices['data'], offset)
            for axis, value in enumerate(position):
                bounds[0][axis] = min(bounds[0][axis], value)
                bounds[1][axis] = max(bounds[1][axis], value)
    for side in bounds:
        _blob(states, struct.pack('<3d', *side))

    frame_hashes, counts = [], []
    for frame in range(frame_count):
        digest, count = hashlib.sha256(), 0
        for mesh in model['meshes']:
            vi, ii, pi, mi = mesh['frames'][frame]
            vertices = model['vertices'][vi]
            indices = model['indices'][ii]
            data, stride = vertices['data'], vertices['stride']
            state = struct.pack('<BIIIII', mesh['flags'], vertices['flags'],
                                vertices['format'], stride, indices['flags'],
                                indices['stride']) + model['materials'][mi]['raw']
            visible = 0
            for kind, start, length in model['primitives'][pi]:
                # validate_s3d already rejects unsupported primitive types,
                # incomplete triangles and invalid buffer references.
                for offset in range(start, start + length, 3):
                    a, b, c = (data[index * stride:(index + 1) * stride]
                               for index in indices['values'][offset:offset + 3])
                    _blob(digest, state)
                    _blob(digest, min(a + b + c, b + c + a, c + a + b))
                    count += 1
                    visible += 1
            if not visible:
                raise ModelError('Render equivalence requires visible mesh triangles')
        frame_hashes.append(digest.hexdigest())
        counts.append(count)
    return {'version': list(model['version']), 'frame_count': frame_count,
            'visible_triangles_per_frame': counts,
            'exact_render_states_sha256': states.hexdigest(),
            'ordered_oriented_encoded_vertex_draw_sha256_per_frame': frame_hashes,
            'all_vertex_bounds_xyz': bounds}


def audit_s3d_equivalence(before: bytes, after: bytes) -> dict:
    """Require exact visible render equivalence and describe serialization.

    Mesh names are editor labels. Buffer indices/grouping may change while
    drawing precisely the same ordered vertices with the same render state.
    Raw resource identity remains a separate, stronger claim for callers.
    """
    original, current = s3d_render_fingerprint(before), s3d_render_fingerprint(after)
    if original != current:
        raise ModelError('Render-relevant S3D model semantics differ')
    a, b = parse_s3d(before), parse_s3d(after)
    for model in (a, b):
        model.pop('source_chunk_lengths')
        for mesh in model['meshes']:
            mesh.pop('name')
    difference = ('mesh_labels_only' if a == b else
                  'vertex_index_or_render_group_encoding_and_optional_mesh_labels')
    return {'semantics': original, 'serialization_difference': difference,
            'exact_visible_draw_sequence_and_render_state_preserved': True}
