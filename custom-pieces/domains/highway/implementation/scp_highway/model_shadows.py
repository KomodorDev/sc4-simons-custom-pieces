"""Keep each highway module's native shadow independent of tile ownership.

Visible models and traffic resources are never rewritten here. The shadow
source contains only the module's own indexed faces above the ground plane;
faces crossing that plane are clipped before camera-relative projection.
"""
from __future__ import annotations

import hashlib
import math
import struct

from scp.dbpf import require
from scp import model_shadows
from scp.models import parse_s3d, positions
from scp.model_shadow_geometry import referenced_model_triangles, generate_shadow_carriers


def elevated_triangles(raw):
    """Clip actual referenced faces at y=0, without a 16-metre tile clip."""
    model = parse_s3d(raw)
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        points = positions(model['vertices'][vi])
        indices = model['indices'][ii]['values']
        used = {index for _kind, first, count in model['primitives'][pi]
                for index in indices[first:first + count]}
        if any(points[index][1] > 0 for index in used):
            flags = struct.unpack_from('<I', model['materials'][mi]['raw'])[0]
            require(flags & 0x11 == 0,
                    'Opaque highway shadow projection cannot ignore source alpha testing or blending')
    result = []
    for triangle in referenced_model_triangles(raw):
        if max(point[1] for point in triangle) <= 0:
            continue
        polygon = list(triangle)
        clipped = []
        for first, last in zip(polygon, polygon[1:] + polygon[:1]):
            inside_first, inside_last = first[1] >= 0, last[1] >= 0
            if inside_first:
                clipped.append(first)
            if inside_first != inside_last:
                fraction = -first[1] / (last[1] - first[1])
                clipped.append((first[0] + fraction * (last[0] - first[0]), 0.,
                                first[2] + fraction * (last[2] - first[2])))
        for index in range(1, len(clipped) - 1):
            face = clipped[0], clipped[index], clipped[index + 1]
            a, b, c = face
            u = [b[i] - a[i] for i in range(3)]
            v = [c[i] - a[i] for i in range(3)]
            cross = [u[(i + 1) % 3] * v[(i + 2) % 3]
                     - u[(i + 2) % 3] * v[(i + 1) % 3] for i in range(3)]
            if math.sqrt(sum(value * value for value in cross)) > 2e-12:
                result.append(face)
    return result


def add_shadows(spec, context, compiled, resources):
    """Append invisible native carriers after ordinary adaptive T21 creation."""
    rows = model_shadows.bindings(spec)
    if not rows:
        return resources
    if not model_shadows.enabled(spec):
        model_shadows.validate_resources(resources, spec)
        return resources
    capture = context.get('model_shadow_lighting', {})
    raw = capture.get(model_shadows.LIGHTING_EXEMPLAR)
    require(raw is not None and hashlib.sha256(raw).hexdigest() == model_shadows.LIGHTING_SHA256,
            'Highway model shadows require the audited native sunlight capture')
    canonical = {tuple(cell): model for cell, model, _path in compiled}
    carriers = {}
    for row in rows:
        cell = tuple(row['cell'])
        require(cell in canonical, 'Model-shadow source cell is missing')
        triangles = elevated_triangles(canonical[cell])
        require(bool(triangles) == row['cast_shadow'],
                'Declared highway caster differs from actual above-ground geometry')
        if triangles:
            carriers[cell] = generate_shadow_carriers(
                triangles, row['texture_ids'], metres_per_pixel=.125,
                maximum_texture_size=512, supersample=4, card_height_m=64.)
    return model_shadows.add_resources(resources, spec, carriers)
