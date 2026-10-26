"""Prove continuous surface and UV preservation outside one literal fan corner.

The seventh changed fan tile may contain retessellated faces beside the
one-micrometre ownership edge. This verifier compares saved oriented surfaces
in both directions, integrates exact polygon coverage and compares the full
affine XYZUV fields at every intersection vertex. It never samples a grid or
imports the mesh writer. Literal bounds admit only the corner ownership strip;
the existing100µm native meshing precision bounds projected boundary changes,
while the4µm affine-plane and3e-6 UV tolerances remain strict. Other audits establish
no substantive duplicate coplanar surfaces and complete assembled rail beds.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
import math
import struct

from scp.dbpf import require
from scp.models import parse_s3d, validate_s3d
from .directional_t_verify import _area, _intersection_polygon
from .hsr_mesh_verify import _component_union_area

# Tile-local XYZ for fan local cell(5,4), global assembly display(X16,Y14).
# The actual corner edge isx=-7.999999; the second micrometre bounds packing.
ALLOWED_CORNER_XYZ = ((-8., -7.999998), (13.5, 17.5), (7., 8.))
POSITION_TOLERANCE_M = 4e-6
UV_TOLERANCE = 3e-6
MESH_PRECISION_M = 1e-4
PROJECTION_EXPANSION_M = MESH_PRECISION_M-POSITION_TOLERANCE_M
AREA_TOLERANCE_M2 = 1e-9


def _clip(polygon, value, positive=True):
    if not polygon:
        return []
    result, a = [], polygon[-1]
    va = value(a)*(1 if positive else -1)
    for b in polygon:
        vb = value(b)*(1 if positive else -1)
        if (va >= 0.) != (vb >= 0.):
            t = va/(va-vb)
            result.append(tuple(x+t*(y-x) for x, y in zip(a, b)))
        if vb >= 0.:
            result.append(b)
        a, va = b, vb
    return result


def _outside_corner(triangle):
    inside, outside = list(triangle), []
    for axis, (low, high) in enumerate(ALLOWED_CORNER_XYZ):
        for boundary, sign in ((low, 1.), (high, -1.)):
            plane = lambda point, axis=axis, boundary=boundary, sign=sign: sign*(point[axis]-boundary)
            part = _clip(inside, plane, False)
            if len(part) >= 3 and any(plane(point) < -1e-12 for point in part):
                outside.append(part)
            inside = _clip(inside, plane)
            if len(inside) < 3:
                return outside
    return outside


def _normal(triangle):
    a, b, c = triangle
    u = [b[i]-a[i] for i in range(3)]
    v = [c[i]-a[i] for i in range(3)]
    n = u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]
    length = math.sqrt(sum(value*value for value in n))
    return tuple(value/length for value in n) if length > 1e-14 else None


def _hull(points):
    points = sorted(set(points))
    def cross(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def side(values):
        result = []
        for point in values:
            while len(result) >= 2 and cross(result[-2], result[-1], point) <= 0.:
                result.pop()
            result.append(point)
        return result
    return side(points)[:-1]+side(reversed(points))[:-1]


def _expanded(points, radius=PROJECTION_EXPANSION_M):
    # A diamond bounds Euclidean projection distance by radius. Scaling it
    # by the dropped-axis normal component bounds the lifted3D movement by
    # radius/abs(normal[axis]). With the remaining4µm plane allowance this
    # is at most the existing100µm native mesh precision, in every direction.
    return _hull([(x+dx, y+dy) for x, y in points
                  for dx, dy in ((-radius,0.),(radius,0.),(0.,-radius),(0.,radius))])


def _at(triangle, axis, point):
    indices = [index for index in range(3) if index != axis]
    a, b, c = triangle
    u = [b[i]-a[i] for i in indices]
    v = [c[i]-a[i] for i in indices]
    r = [point[j]-a[i] for j, i in enumerate(indices)]
    determinant = u[0]*v[1]-u[1]*v[0]
    if abs(determinant) <= 1e-16:
        return None
    s = (r[0]*v[1]-r[1]*v[0])/determinant
    t = (u[0]*r[1]-u[1]*r[0])/determinant
    return tuple(a[i]+s*(b[i]-a[i])+t*(c[i]-a[i]) for i in (axis, 3, 4))


def _key(state, triangle):
    return state, min(triangle, triangle[1:]+triangle[:1], triangle[2:]+triangle[:2])


def _faces(raw):
    model = parse_s3d(raw)
    validate_s3d(model)
    frames = struct.unpack_from('<H', model['anim_header'])[0]
    require(frames == 1, 'Corner proof requires exactly one static animation frame')
    result = []
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        vb, ib = model['vertices'][vi], model['indices'][ii]
        require(vb['format'] in (2, 0x80004001) and vb['stride'] == 20,
                'Corner proof requires the existing native XYZUV vertex format')
        state = (mesh['flags'], vb['flags'], vb['format'], vb['stride'],
                 ib['flags'], ib['stride'], model['materials'][mi]['raw'])
        vertices = [struct.unpack_from('<5f', vb['data'], offset)
                    for offset in range(0, len(vb['data']), vb['stride'])]
        for kind, start, count in model['primitives'][pi]:
            require(kind == 0 and count % 3 == 0, 'Corner proof requires independent triangles')
            for offset in range(start, start+count, 3):
                tri = tuple(vertices[i] for i in ib['values'][offset:offset+3])
                if _normal(tri) is not None:
                    result.append((state, tri))
    metadata = (model['version'], model['anim_header'],
                tuple(material['raw'] for material in model['materials']), tuple(model['trailing']))
    return metadata, result


def _buckets(polygon):
    return [(x, y) for x in range(math.floor(min(p[0] for p in polygon)),
                                  math.floor(max(p[0] for p in polygon))+1)
                   for y in range(math.floor(min(p[1] for p in polygon)),
                                  math.floor(max(p[1] for p in polygon))+1)]


def _index(faces):
    buckets = defaultdict(set)
    cached = []
    for index, (state, triangle) in enumerate(faces):
        normal = _normal(triangle)
        projections = []
        for axis in range(3):
            projected = [tuple(point[i] for i in range(3) if i != axis) for point in triangle]
            projections.append(projected)
            if _area(projected) > 1e-14:
                for cell in _buckets(_expanded(projected)):
                    buckets[state, axis, cell].add(index)
        cached.append((triangle, normal, projections))
    return buckets, cached


def _one_way(source, target, exact, label):
    index, cached = _index(target)
    checked, intersections, worst_uv, worst_xyz, worst_hole = 0, 0, 0., 0., 0.
    for state, triangle in source:
        key = _key(state, triangle)
        if exact[key]:
            exact[key] -= 1
            continue
        normal = _normal(triangle)
        axis = max(range(3), key=lambda i: abs(normal[i]))
        for polygon in _outside_corner(triangle):
            projected = [tuple(point[i] for i in range(3) if i != axis) for point in polygon]
            area = _area(projected)
            if area <= 1e-14:
                continue
            candidates = set()
            for cell in _buckets(projected):
                candidates.update(index[state, axis, cell])
            coverage, best_bad_uv = [], math.inf
            for number in candidates:
                other, other_normal, projections = cached[number]
                if sum(a*b for a,b in zip(normal, other_normal)) <= 0.:
                    continue
                other_projected = projections[axis]
                if _area(other_projected) <= 1e-14:
                    continue
                radius = PROJECTION_EXPANSION_M*abs(other_normal[axis])
                overlap = _intersection_polygon(projected, _expanded(other_projected, radius))
                if len(overlap) < 3 or _area(overlap) <= 1e-14:
                    continue
                one = [_at(triangle, axis, p) for p in overlap]
                two = [_at(other, axis, p) for p in overlap]
                if any(p is None for p in one+two):
                    continue
                # Every difference is affine on this overlap. Exact
                # half-plane cuts retain precisely the continuously matching
                # physical/texture region; no vertex sampling can hide an
                # interior edit or waive a UV seam crossed by expansion.
                uv = max(abs(a[i]-b[i]) for a,b in zip(one,two) for i in (1,2))
                best_bad_uv = min(best_bad_uv, uv)
                for component, tolerance in ((0, POSITION_TOLERANCE_M),
                                              (1, UV_TOLERANCE), (2, UV_TOLERANCE)):
                    def difference(point, component=component):
                        return _at(triangle, axis, point)[component]-_at(other, axis, point)[component]
                    overlap = _clip(overlap, lambda point, tolerance=tolerance:
                                    tolerance-difference(point))
                    overlap = _clip(overlap, lambda point, tolerance=tolerance:
                                    tolerance+difference(point))
                    if len(overlap) < 3:
                        break
                if len(overlap) < 3 or _area(overlap) <= 1e-14:
                    continue
                one = [_at(triangle, axis, p) for p in overlap]
                two = [_at(other, axis, p) for p in overlap]
                position = max(abs(a[0]-b[0]) for a,b in zip(one,two))
                uv = max(abs(a[i]-b[i]) for a,b in zip(one,two) for i in (1,2))
                coverage.append(overlap)
                intersections += 1
                worst_uv, worst_xyz = max(worst_uv, uv), max(worst_xyz, position)
            missing = max(0., area-_component_union_area(coverage))
            worst_hole = max(worst_hole, missing)
            require(missing <= AREA_TOLERANCE_M2,
                    f'Corner equivalence {label} changed physical/UV surface outside the literal strip: '
                    f'unmatched projected area {missing:.12g} m²; best candidate UV error '
                    f'{best_bad_uv:.12g}; face {triangle}')
            checked += 1
    return {'outside_polygons_checked': checked, 'affine_intersections_checked': intersections,
            'maximum_accepted_uv_error': worst_uv, 'maximum_accepted_position_error_m': worst_xyz,
            'maximum_unmatched_projected_area_m2': worst_hole}


@lru_cache(maxsize=8)
def _audit(before_raw, after_raw):
    before_metadata, before = _faces(before_raw)
    after_metadata, after = _faces(after_raw)
    require(before_metadata == after_metadata, 'Corner equivalence changed material or animation state')
    old, new = Counter(_key(s,t) for s,t in before), Counter(_key(s,t) for s,t in after)
    common = old & new
    forward = _one_way(before, after, common.copy(), 'before-to-after')
    backward = _one_way(after, before, common.copy(), 'after-to-before')
    return {'continuous_oriented_surface_and_affine_uv_equivalence': True,
            'literal_allowed_tile_local_xyz': [list(bounds) for bounds in ALLOWED_CORNER_XYZ],
            'position_tolerance_m': POSITION_TOLERANCE_M, 'uv_tolerance': UV_TOLERANCE,
            'projection_expansion_m': PROJECTION_EXPANSION_M,
            'projection_expansion_shape': 'L1 diamond scaled by target plane normal',
            'full_3d_surface_distance_bound_m': MESH_PRECISION_M,
            'unmatched_area_tolerance_m2': AREA_TOLERANCE_M2,
            'before_triangles': len(before), 'after_triangles': len(after),
            'exact_common_oriented_xyzuv_triangles': sum(common.values()),
            'before_to_after': forward, 'after_to_before': backward}


def audit_corner_equivalence(before_raw, after_raw):
    """Prove the seventh tile's bounded edit from actual saved S3D resources."""
    from copy import deepcopy
    return deepcopy(_audit(before_raw, after_raw))
