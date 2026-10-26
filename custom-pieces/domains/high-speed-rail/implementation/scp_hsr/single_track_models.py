"""Native rail mesh primitives shared by the current rail generators.

Routes use SC4PATH coordinates (east, north, height); models use
(east, height, -north). Preserve donor profiles, UV coordinates and mesh
packing exactly when clipping, joining or supporting current rail decks.
"""
from __future__ import annotations

from copy import deepcopy
import math
import struct

from scp.models import parse_s3d, pack_s3d, valid_frame, validate_s3d

EPS = 1e-7


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _lerp(a, b, fraction):
    return tuple(x + (y - x) * fraction for x, y in zip(a, b))


def _clip(polygon, distance, keep_positive=True):
    """Clip position/UV vertices against a plane, preserving interpolation."""
    if not polygon:
        return []
    result = []
    previous = polygon[-1]
    dp = distance(previous) * (1 if keep_positive else -1)
    for current in polygon:
        dc = distance(current) * (1 if keep_positive else -1)
        if (dc >= -EPS) != (dp >= -EPS):
            fraction = dp / (dp - dc)
            result.append(_lerp(previous, current, fraction))
        if dc >= -EPS:
            result.append(current)
        previous, dp = current, dc
    return result


def _normal(triangle):
    a, b, c = triangle
    u = tuple(b[n] - a[n] for n in range(3))
    v = tuple(c[n] - a[n] for n in range(3))
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def _triangulate(polygon):
    for index in range(1, len(polygon) - 1):
        triangle = polygon[0], polygon[index], polygon[index + 1]
        if sum(value * value for value in _normal(triangle)) > EPS * EPS:
            yield triangle


def _oriented(triangle, desired):
    if sum(a * b for a, b in zip(_normal(triangle), desired)) < 0:
        return triangle[0], triangle[2], triangle[1]
    return triangle


def _quad(vertices, desired=None):
    result = list(_triangulate(vertices))
    return [_oriented(t, desired) for t in result] if desired else result


def _convex(points):
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(points, points[1:] + points[:1]))
    return points if area > 0 else list(reversed(points))


def _subtract_polygons(polygon, footprint):
    """Keep convex face fragments as polygons until all cuts are complete."""
    if (max(v[0] for v in polygon) < min(p[0] for p in footprint) - EPS
            or min(v[0] for v in polygon) > max(p[0] for p in footprint) + EPS
            or max(v[2] for v in polygon) < min(p[1] for p in footprint) - EPS
            or min(v[2] for v in polygon) > max(p[1] for p in footprint) + EPS):
        return [polygon]
    footprint = _convex(footprint)
    pending, outside = polygon, []
    for a, b in zip(footprint, footprint[1:] + footprint[:1]):
        def side(vertex, a=a, b=b):
            return (b[0] - a[0]) * (vertex[2] - a[1]) - (b[1] - a[1]) * (vertex[0] - a[0])
        # A vertical face exactly on a clip boundary has nonzero 3D area but
        # zero plan area. Treat it as inside instead of duplicating it through
        # both inclusive half-planes.
        if any(side(vertex) < -EPS for vertex in pending):
            clipped = _clip(pending, side, False)
            if len(clipped) >= 3:
                outside.append(clipped)
        pending = _clip(pending, side, True)
        if len(pending) < 3:
            break
    return outside


def _subtract(polygon, footprint):
    """Subtract a convex X/Z footprint; retain every new vertex's UVs."""
    return [tri for piece in _subtract_polygons(polygon, footprint) for tri in _triangulate(piece)]


def _native(raw):
    model = parse_s3d(raw)
    meshes = [mesh for mesh in model['meshes']
              if all(valid_frame(model, frame) for frame in mesh['frames'])]
    _require(len(meshes) == 1, 'Expected one valid native straight HSR mesh')
    mesh = meshes[0]
    _require(len(mesh['frames']) == 1, 'Animated HSR donors are unsupported')
    vi, ii, pi, mi = mesh['frames'][0]
    vb = model['vertices'][vi]
    _require(vb['stride'] == 20 and len(model['materials'][mi]['textures']) == 1,
             'Expected native XYZ/UV vertices and one HSR atlas')
    vertices = [struct.unpack_from('<5f', vb['data'], offset)
                for offset in range(0, len(vb['data']), vb['stride'])]
    indices = model['indices'][ii]['values']
    triangles = []
    for kind, start, count in model['primitives'][pi]:
        _require(kind == 0 and count % 3 == 0, 'Expected triangle-list HSR primitives')
        triangles.extend(tuple(vertices[i] for i in indices[pos:pos + 3])
                         for pos in range(start, start + count, 3))
    bed = [tri for tri in triangles
           if max(v[1] for v in tri) - min(v[1] for v in tri) < 1e-4
           and max(v[0] for v in tri) - min(v[0] for v in tri) > 10]
    _require(len(bed) == 2, 'Native HSR flat two-track bed topology changed')
    bed_y = sum(v[1] for tri in bed for v in tri) / 6
    outer = max(abs(v[0]) for tri in triangles for v in tri)
    inner = max(abs(v[0]) for tri in bed for v in tri)
    _require(abs(outer - 7.5) < 1e-3 and 5.9 < inner < 6.1,
             'Native HSR width/profile changed')
    return {'model': model, 'mesh': mesh, 'vb': vb, 'material': model['materials'][mi],
            'triangles': triangles, 'bed': bed, 'bed_y': bed_y,
            'outer': outer, 'inner': inner,
            'bottom': min(v[1] for tri in triangles for v in tri),
            'top': max(v[1] for tri in triangles for v in tri)}


def _template(native, source_lane, deck_width):
    _require(math.isfinite(source_lane) and abs(abs(source_lane) - 2) < EPS,
             'Select exactly one native HSR lane: source_lane must be +2 or -2')
    _require(math.isfinite(deck_width) and 6.0 <= deck_width <= 8.0,
             'Single-track deck width must be between 6 and 8 metres')
    outer, inner = native['outer'], native['inner']
    inset = outer - inner
    inner_half = deck_width / 2 - inset
    low, high = source_lane - inner_half, source_lane + inner_half
    _require(-inner <= low < high <= inner, 'One-track bed extends outside the native atlas band')
    result = []
    for triangle in native['triangles']:
        if triangle in native['bed']:
            polygon = _clip(list(triangle), lambda v: v[0] - low)
            polygon = _clip(polygon, lambda v: high - v[0])
            for tri in _triangulate(polygon):
                result.append(('bed', tuple((v[0] - source_lane, *v[1:]) for v in tri)))
        else:
            positive = all(v[0] > 0 for v in triangle)
            negative = all(v[0] < 0 for v in triangle)
            _require(positive or negative, 'Unrecognized native HSR side-profile face')
            shift = (deck_width / 2 - outer) if positive else (outer - deck_width / 2)
            # Source lane cancels here: both unchanged parapets bound a deck
            # centered on the supplied route, while bed UVs retain lane choice.
            result.append(('wall', tuple((v[0] + shift, *v[1:]) for v in triangle)))
    return result, inner_half


def _pillar(center, top):
    x, z = center
    half = .65
    points = [(x + a * half, y, z + b * half, .07 + .035 * a, y / 16)
              for y in (0., top) for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    triangles = []
    for face, normal in (((0, 1, 2, 3), (0, -1, 0)), ((4, 5, 6, 7), (0, 1, 0)),
                         ((0, 1, 5, 4), (0, 0, -1)), ((1, 2, 6, 5), (1, 0, 0)),
                         ((2, 3, 7, 6), (0, 0, 1)), ((3, 0, 4, 7), (-1, 0, 0))):
        triangles.extend(_quad([points[i] for i in face], normal))
    return triangles


def _pack(native, triangles, *, preserve_encoded_triangles=False):
    """Pack exact authored faces into conservatively sized render groups.

    The 512-vertex and 512-triangle budgets are authoring choices, rather
    than asserted engine limits. Vertex reuse compares the exact encoded
    XYZUV bytes, preserving UV seams, float32 rounding and signed zero.
    Already encoded resources can retain their zero-area faces explicitly;
    ordinary authored geometry keeps its existing degenerate-face filter.
    """
    triangles = (list(triangles) if preserve_encoded_triangles else
                 [tri for tri in triangles if sum(v * v for v in _normal(tri)) > EPS * EPS])
    _require(triangles, 'Generated model has no encoded triangles' if preserve_encoded_triangles
             else 'Generated model has no nondegenerate triangles')
    model = {'version': native['model']['version'], 'vertices': [], 'indices': [],
             'primitives': [], 'materials': [deepcopy(native['material'])],
             'anim_header': native['model']['anim_header'],
             'meshes': [],
             'trailing': deepcopy(native['model']['trailing'])}
    frame_count = struct.unpack_from('<H', model['anim_header'])[0]
    _require(frame_count > 0, 'Generated model needs a nonempty animation frame table')
    source_indices = native['model']['indices'][native['mesh']['frames'][0][1]]
    vertex_data, lookup, indices = bytearray(), {}, []

    def finish():
        group = len(model['meshes'])
        _require(group < 65535, 'Generated model exceeds the 16-bit mesh reference limit')
        vb, ib = deepcopy(native['vb']), deepcopy(source_indices)
        vb['data'] = bytes(vertex_data)
        ib['values'] = tuple(indices)
        model['vertices'].append(vb)
        model['indices'].append(ib)
        model['primitives'].append([(0, 0, len(indices))])
        model['meshes'].append({
            'name': b'SCP one-way HSR\0', 'flags': native['mesh']['flags'],
            'frames': [(group, group, group, 0)] * frame_count})

    for triangle in triangles:
        packed = tuple(struct.pack('<5f', *vertex) for vertex in triangle)
        new_vertices = len(set(packed).difference(lookup))
        if indices and (len(lookup) + new_vertices > 512 or len(indices) // 3 >= 512):
            finish()
            vertex_data, lookup, indices = bytearray(), {}, []
        for vertex in packed:
            index = lookup.get(vertex)
            if index is None:
                index = len(lookup)
                lookup[vertex] = index
                vertex_data.extend(vertex)
            indices.append(index)
    finish()
    validate_s3d(model)
    raw = pack_s3d(model)
    validate_s3d(parse_s3d(raw))
    return raw


