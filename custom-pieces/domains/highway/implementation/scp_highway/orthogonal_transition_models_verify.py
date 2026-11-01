"""Inspect the actual indexed six-tile transition, independently of its writer.

The reviewed curves, native cross-sections, materials, and support dimensions
define a piecewise-linear surface contract. Saved triangles must partition
that complete surface, with its winding and affine UV field intact. This is
stronger than checking that a named mesh exists or that PATH nodes touch it.
No authoring module is imported, and no game result is inferred.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
import hashlib
import math
import struct

from scp.dbpf import decompress, require
from scp.models import parse_s3d, validate_s3d
from scp.track_paths import PATH, S3D
from scp.verify import parse_paths
from . import orthogonal_transition_verify as contract

TEXTURE = (0x7AB50E44, 0x1ABE787D)
PREFIX = 'SCP DD transition '
POSITION_EPS = 6e-6  # Local Float32 vertices, including a world translation.
UV_EPS = 3e-6
MIN_AREA = 2e-9
DD_MIN, DD_MAX = -7.999000072479248, 8.00100040435791
DD_WIDTH, DD_OFFSET = DD_MAX - DD_MIN, DD_MIN + 8.0
DATUM = {'upper': .0010004043579101562, 'lower': .0009999275207519531}
MATERIAL_PINS = {
    'native-dd': '307aba7786d4b4f11dbc499eb54f7d05d01a114001919b8a5f7d55970fbb64ca',
    'native-ground': '6222075ddc668c03c58ce8c66cbd82c633bf82d4b9eacb78d5da0a05e7589219',
    'body': 'cf4e393b8ca3a2b3d0edba0f86bb197ddf82b65e85cf73cfa13ebd4d2a8c6f6e',
    'barrier': 'd81e8d70e3ab9182adb393f2bc6a61608c70f8129cdb06631409a4b19c73e306',
}
NATIVE_TEXTURE_PINS = {
    0x5713000E: '25a91179a26a82ba6307777b1957c5862bee61daf55c7638c4487d64b275c7b8',
    0x5703000E: 'c2b9ac53cc080ca8146f1345e13d43e91c883d9559ec3ec3293e7ff88a259e88',
}
# Filled from a separate, repeat-wrapped bilinear reconstruction of the two
# pinned native images; this is a portable expected pixel identity, not a
# fingerprint copied from the writer's output. The reconstruction remains
# executable below whenever the native input map is supplied.
ATLAS_RGBA_SHA256 = '78b31c0de9afdff8563a5b3b21c4d4ebb80b7d222f56dea45b0de72e1bb9b816'
MIRRORED_ATLAS_RGBA_SHA256 = '7561c84312f940a53296ba5fbc3e7eb15883ac42ace8b704ad3c43d2152068b0'


def _sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def _cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def _dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def _normal(points):
    return _cross(_sub(points[1], points[0]), _sub(points[2], points[0]))


def _area(points):
    return math.sqrt(_dot(n := _normal(points), n)) / 2.0


def _height(deck, s):
    return contract.upper_height(s) if deck == 'upper' else contract.lower_height(s)


def _fade(deck, s):
    return _height(deck, s) / (15.0 if deck == 'upper' else 7.5)


def _bounds(deck, s):
    fade = _fade(deck, s)
    return -8.0 + fade*(DD_MIN+8.0), 8.0 + fade*(DD_MAX-8.0)


def _frame(deck, s):
    displacement, derivative, _ = contract.lateral(s) if deck == 'upper' else (0., 0., 0.)
    q = 1.0 / math.sqrt(1.0 + derivative*derivative)
    return (16.0-displacement, 8.0-s), (q, -derivative*q)


def _position(deck, s, u, absolute_height):
    center, normal = _frame(deck, s)
    return center[0] + u*normal[0], center[1] + u*normal[1], absolute_height


def _uv(deck, s, u, role, *, mirrored=False):
    if role == 'atlas':
        low, high = _bounds(deck, s)
        lateral = (u-low)/(high-low)
        if deck == 'lower':
            lateral = 1.0-lateral
        return ((8.0 if deck == 'upper' else 264.0)+128.0*lateral)/512.0, (128.0+8.0*s)/1024.0
    if role == 'native-dd':
        result = (u-DD_MIN)/DD_WIDTH, ((16.-s if mirrored else s)-DD_OFFSET)/DD_WIDTH
    else:
        result = (u+8.0)/16.0, (16.-s if mirrored else s)/16.0
    return result if deck == 'upper' else tuple(1.0-x for x in result)


def support_contract():
    """Four upper pier/cap pairs and six lower piers, in exact metres."""
    rows = []
    for s in (12., 32., 52., 72.):
        underside = _height('upper', s) + DATUM['upper']*_fade('upper', s)-1.0
        west = -9.2 if s == 12. else -6.4
        rows.extend(((f'upper-pier-{int(s)}', 'upper', s, west-.4, west+.4, .4, 0., underside-.3),
                     (f'upper-cap-{int(s)}', 'upper', s, min(-7., west-.4), 7., .45, underside-.3, underside)))
    for s in (12., 32., 48.):
        top = _height('lower', s)+DATUM['lower']*_fade('lower', s)-1.0
        rows.extend((f'lower-pier-{int(s)}-{name}', 'lower', s, u-.4, u+.4, .4, 0., top)
                    for name, u in (('west', -6.4), ('east', 6.4)))
    return tuple(rows)


def _barrier_strips(deck):
    """Literal measured cross-section, including distinct native upper/lower crown heights."""
    rise = (0., .328125, 1.3906240463256836 if deck == 'upper' else 1.3906254768371582)
    vs = (1., .7119640111923218, 0.)
    result = []
    for side, outer, inner in ((1, (8.00100040435791, 7.782249927520752, 7.735374927520752),
                                  (7.172874927520752, 7.375999927520752, 7.438499927520752)),
                                (-1, (-7.999000072479248, -7.780250072479248, -7.733375072479248),
                                   (-7.170875072479248, -7.374000072479248, -7.436500072479248))):
        for xs, first_u in ((outer, 1. if side == 1 else 0.), (inner, 0. if side == 1 else 1.)):
            for i in (0, 1):
                result.append(tuple((xs[j], rise[j], first_u, vs[j], 1.-first_u) for j in (i, i+1)))
        first_u = 1. if side == 1 else 0.
        result.append(((inner[2], rise[2], first_u, .625, 1.-first_u),
                       (outer[2], rise[2], first_u, .32499998807907104, 1.-first_u)))
    return result


@lru_cache(maxsize=2)
def _surface_contract(mirrored=False):
    """Triangulated reviewed ruled surfaces; no city clipping or writer imports."""
    faces = []

    def quad(role, vertices, outward=None):
        for indices in ((0, 1, 2), (0, 2, 3)):
            points = tuple(vertices[i][:3] for i in indices)
            uvs = tuple(vertices[i][3:] for i in indices)
            if _area(points) <= MIN_AREA:
                continue
            if outward is not None and _dot(_normal(points), outward) < 0.:
                points, uvs = (points[0], points[2], points[1]), (uvs[0], uvs[2], uvs[1])
            faces.append({'role': role, 'points': points, 'uv': uvs, 'area': _area(points)})

    for deck in ('upper', 'lower'):
        for index in range(384):
            a, b = index/4., (index+1)/4.
            role = 'native-dd' if b <= 3. else 'native-ground' if a >= (69. if deck == 'lower' else 93.) else 'atlas'
            rings, bottoms = [], []
            for s in (a, b):
                low, high = _bounds(deck, s)
                surface = _height(deck, s)+DATUM[deck]*_fade(deck, s)
                rings.append([(*_position(deck, s, u, surface), *_uv(deck, s, u, role, mirrored=mirrored))
                              for u in (low, -3.75, -2.5, -1.25, 0., 1.25, 2.5, 3.75, high)])
                bottoms.append([(*_position(deck, s, u, max(0., surface-1.)), u/8., s/8.) for u in (low, high)])
            for strip in range(8):
                quad(f'{deck}-pavement-{role}', (rings[0][strip], rings[1][strip], rings[1][strip+1], rings[0][strip+1]), (0., 0., 1.))
            if max(_height(deck, a), _height(deck, b)) > 0.:
                quad(f'{deck}-body', (bottoms[0][0], bottoms[0][1], bottoms[1][1], bottoms[1][0]), (0., 0., -1.))
                for side, top_index, bottom_index in ((-1, 0, 0), (1, -1, 1)):
                    top_a, top_b = rings[0][top_index], rings[1][top_index]
                    # UVs are not needed for concrete appearance, but their
                    # continuity is still bound to the reviewed affine field.
                    vertices = []
                    for p in (top_a, bottoms[0][bottom_index], bottoms[1][bottom_index], top_b):
                        south = -p[1]
                        vertices.append((*p[:3], south/16., (p[2]-min(top_a[2], top_b[2]))/8.))
                    normal = _frame(deck, (a+b)/2.)[1]
                    quad(f'{deck}-body', vertices, (side*normal[0], side*normal[1], 0.))
        low, high = _bounds(deck, 0.)
        surface = _height(deck, 0.)+DATUM[deck]
        quad(f'{deck}-body', [(*_position(deck, 0., u, surface+vertical), u/8., (DATUM[deck]+vertical)/8.)
                             for u, vertical in ((low, 0.), (low, -1.), (high, -1.), (high, 0.))], (0., 1., 0.))
        for strip in _barrier_strips(deck):
            for index in range(384):
                a, b = index/4., (index+1)/4.
                if _height(deck, a) == _height(deck, b) == 0.:
                    continue
                points = []
                for s, at in ((a, 0), (a, 1), (b, 1), (b, 0)):
                    source_x, rise, uv_a, v, uv_b = strip[at]
                    canonical = (source_x-(DD_MIN+DD_MAX)/2.)*16./DD_WIDTH
                    u = canonical+_fade(deck, s)*(source_x-canonical)
                    t = min(1., max(0., _height(deck, s)/2.))
                    height = _height(deck, s)+DATUM[deck]*_fade(deck, s)+rise*t*t*(3.-2.*t)
                    phase = ((16.-s if mirrored else s)-DD_OFFSET)/DD_WIDTH
                    points.append((*_position(deck, s, u, height), uv_a+phase*(uv_b-uv_a), v))
                quad(f'{deck}-barrier', points)
    for name, deck, s, low, high, half, bottom, top in support_contract():
        center, normal = _frame(deck, s)
        tangent = normal[1], -normal[0]
        vertices = [((center[0]+u*normal[0]+t*tangent[0]),
                     (center[1]+u*normal[1]+t*tangent[1]), height)
                    for height in (bottom, top)
                    for u, t in ((low, -half), (high, -half), (high, half), (low, half))]
        middle = tuple(sum(p[k] for p in vertices)/8. for k in range(3))
        for indices in ((0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)):
            polygon = [(*vertices[i], vertices[i][0]/8., (-vertices[i][1]+vertices[i][2])/8.) for i in indices]
            outward = tuple(sum(p[k] for p in polygon)/4.-middle[k] for k in range(3))
            quad(name, polygon, outward)
    return tuple(faces)


def decode_faces(raw, cell=(0, 0), *, mirrored=False):
    """Decode only referenced saved faces, retaining material and UV evidence."""
    model = parse_s3d(decompress(raw))
    validate_s3d(model)
    require(struct.unpack_from('<H', model['anim_header'])[0] == 1,
            'Transition must retain a single static animation frame')
    require(all(len(chunk) == 12 and chunk[8:] == b'\0'*4 for _name, chunk in model['trailing']),
            'Transition cannot hide a transform in its saved model')
    result = []
    for mesh in model['meshes']:
        require(len(mesh['frames']) == 1, 'Transition mesh must be static')
        vi, ii, pi, mi = mesh['frames'][0]
        block = model['vertices'][vi]
        require(block['stride'] >= 20 and len(block['data'])//block['stride'] <= 512,
                'Transition render group exceeds its 512-vertex budget')
        vertices = [struct.unpack_from('<5f', block['data'], at) for at in range(0, len(block['data']), block['stride'])]
        require(all(all(math.isfinite(v) for v in p) for p in vertices), 'Transition contains nonfinite XYZ/UV')
        material = model['materials'][mi]
        require(len(material['textures']) == 1, 'Transition material must reference one texture')
        indices = model['indices'][ii]['values']
        require(len(indices) <= 1536, 'Transition render group exceeds its 1,536-index budget')
        name = mesh['name'].rstrip(b'\0').decode('ascii')
        require(name.startswith(PREFIX), 'Transition contains an unreviewed mesh role')
        role = name[len(PREFIX):]
        for kind, first, size in model['primitives'][pi]:
            require(kind == 0 and size % 3 == 0, 'Transition requires indexed triangles')
            for at in range(first, first+size, 3):
                source = tuple(vertices[i] for i in indices[at:at+3])
                points = tuple((p[0]+16.*cell[0], -p[2]-16.*cell[1], p[1]) for p in source)
                west = -8.-(DD_MAX-8.) if mirrored else -8.
                east = 24. if mirrored else 24.+(DD_MAX-8.)
                require(all(west-POSITION_EPS <= p[0] <= east+POSITION_EPS
                            and -88.-POSITION_EPS <= p[1] <= 8.+POSITION_EPS for p in points),
                        'Transition physical model leaves its reviewed 2 by 6 envelope')
                local_west = -8.-(DD_MAX-8.) if mirrored else -8.
                local_east = 8. if mirrored else 8.+(DD_MAX-8.)
                require(all(local_west-POSITION_EPS <= p[0] <= local_east+POSITION_EPS
                            and abs(p[2]) <= 8.+POSITION_EPS for p in source),
                        'Transition cell has unowned geometry beyond its measured native overhang')
                result.append({'points': points, 'uv': tuple((p[3], p[4]) for p in source),
                               'role': role, 'texture': material['textures'][0], 'material': material,
                               'upward': _normal(points)[2] > 1e-12})
    require(result, 'Transition owned model cell is empty')
    return result


def _keys(points, size=1.):
    low = [math.floor((min(p[i] for p in points)-POSITION_EPS)/size) for i in (0, 1)]
    high = [math.floor((max(p[i] for p in points)+POSITION_EPS)/size) for i in (0, 1)]
    return ((x, y) for x in range(low[0], high[0]+1) for y in range(low[1], high[1]+1))


def _weights(point, triangle):
    a, b, c = triangle
    u, v, w = _sub(b, a), _sub(c, a), _sub(point, a)
    uu, uv, vv, wu, wv = _dot(u, u), _dot(u, v), _dot(v, v), _dot(w, u), _dot(w, v)
    denominator = uu*vv-uv*uv
    if denominator <= 1e-24:
        return None
    second, third = (vv*wu-uv*wv)/denominator, (uu*wv-uv*wu)/denominator
    weights = 1.-second-third, second, third
    reconstructed = tuple(sum(weights[k]*p[i] for k, p in enumerate(triangle)) for i in range(3))
    if math.dist(point, reconstructed) > POSITION_EPS:
        return None
    # A metric distance to each edge is the useful tolerance for short end
    # slivers; a dimensionless barycentric allowance would silently scale it.
    area_twice = math.sqrt(_dot(n := _normal(triangle), n))
    for weight, edge in zip(weights, ((b, c), (c, a), (a, b))):
        altitude = area_twice/math.dist(*edge)
        if weight*altitude < -POSITION_EPS:
            return None
    return weights


def _field_weights(point, uv, parent):
    """One barycentric witness must satisfy both saved XYZ and saved UV.

    Near a barrier's ground taper the XYZ triangle becomes very thin, but its
    UV triangle remains well conditioned. Solving XYZ alone amplifies harmless
    Float32 rounding into an incorrect UV error. Select the best conditioned
    pair from all five attributes, then check every attribute at its original
    explicit tolerance; this does not increase either tolerance.
    """
    scales = (POSITION_EPS,)*3+(UV_EPS,)*2
    rows = [tuple(v/s for v, s in zip((*p, *t), scales))
            for p, t in zip(parent['points'], parent['uv'])]
    target = tuple(v/s for v, s in zip((*point, *uv), scales))
    a, b, c = rows
    u, v, w = _sub(b, a), _sub(c, a), _sub(target, a)
    determinant, first, second = max((abs(u[i]*v[j]-u[j]*v[i]), i, j)
                                      for i in range(5) for j in range(i+1, 5))
    if determinant < 1e-10:
        return None
    denominator = u[first]*v[second]-u[second]*v[first]
    q = (w[first]*v[second]-w[second]*v[first])/denominator
    r = (u[first]*w[second]-u[second]*w[first])/denominator
    weights = (1.-q-r, q, r)
    if any(abs(target[i]-sum(weights[k]*rows[k][i] for k in range(3))) > 1. for i in range(5)):
        return None
    # Bound edge excursions in both fields, rather than a free dimensionless
    # barycentric tolerance on arbitrarily thin triangles.
    for k in range(3):
        if weights[k] >= 0.:
            continue
        opposite = [i for i in range(3) if i != k]
        edge = _sub(rows[opposite[1]], rows[opposite[0]])
        delta = _sub(rows[k], rows[opposite[0]])
        projection = _dot(delta, edge)/_dot(edge, edge)
        altitude = math.sqrt(sum((delta[i]-projection*edge[i])**2 for i in range(5)))
        if -weights[k]*altitude > 1.5:
            return None
    return weights


def _material(face, atlas_id):
    role, material = face['role'], face['material']
    if '-pavement-' in role:
        family = role.rsplit('-pavement-', 1)[1]
        texture = {'native-dd': 0x5713000E, 'native-ground': 0x5703000E, 'atlas': atlas_id}[family]
    else:
        family = 'barrier' if role.endswith('-barrier') else 'body'
        texture = 0x5EB4BEE9 if family == 'barrier' else 0x5EB4BEEE
    require(face['texture'] == texture, 'Transition face uses the wrong native or authored texture')
    raw = material['raw']
    if family == 'atlas':
        # The sole texture word is deliberately variable; every other native
        # material setting, including alpha and wrapping, remains fixed.
        first = struct.pack('<I', atlas_id)
        require(raw.count(first) == 1, 'Transition atlas material texture address is ambiguous')
        raw = raw.replace(first, struct.pack('<I', 0x5703000E), 1)
        family = 'native-ground'
    require(hashlib.sha256(raw).hexdigest() == MATERIAL_PINS[family],
            'Transition changes its pinned native material/alpha/wrapping settings')


def check_complete_surfaces(faces, atlas_id, *, mirrored=False):
    """Prove saved clipped faces partition all reviewed body, barrier, and support faces."""
    expected = _surface_contract(mirrored)
    index = defaultdict(set)
    for i, face in enumerate(expected):
        for key in _keys(face['points']):
            index[face['role'], key].add(i)
    areas = [0.]*len(expected)
    children = defaultdict(list)
    ignored = 0
    max_uv_error = 0.
    for face in faces:
        _material(face, atlas_id)
        area = _area(face['points'])
        if area <= MIN_AREA:
            ignored += 1
            continue
        candidates = set()
        for key in _keys(face['points']):
            candidates.update(index.get((face['role'], key), ()))
        matches = []
        for i in candidates:
            parent = expected[i]
            if any(max(p[k] for p in face['points']) < min(p[k] for p in parent['points'])-POSITION_EPS
                   or min(p[k] for p in face['points']) > max(p[k] for p in parent['points'])+POSITION_EPS
                   for k in range(3)):
                continue
            weights = [_field_weights(p, uv, parent) for p, uv in zip(face['points'], face['uv'])]
            if any(w is None for w in weights):
                continue
            error = max(abs(actual[axis]-sum(w[k]*parent['uv'][k][axis] for k in range(3)))
                        for actual, w in zip(face['uv'], weights) for axis in range(2))
            if error <= UV_EPS and _dot(_normal(face['points']), _normal(parent['points'])) > 0.:
                matches.append((error, i, weights))
        require(matches, f"Saved transition {face['role']} face leaves its independent surface, winding, or UV field: {face['points']}")
        error, chosen, weights = min(matches)
        max_uv_error = max(max_uv_error, error)
        areas[chosen] += area
        children[chosen].append(tuple((w[1], w[2], 0.) for w in weights))
    # Equal total area alone does not prove a partition: a duplicated half
    # could conceal a missing half. Reject positive-area overlap between
    # children in the parent's barycentric plane before accepting its total.
    overlap_pairs = 0
    for parent, triangles in children.items():
        for index, first in enumerate(triangles):
            for second in triangles[index+1:]:
                overlap_pairs += 1
                polygon = _plan_overlap(first, second)
                overlap = (abs(sum(a[0]*b[1]-a[1]*b[0] for a, b in zip(polygon, (*polygon[1:], polygon[0]))))
                           * expected[parent]['area']) if polygon else 0.
                require(overlap <= max(2e-5, expected[parent]['area']*4e-5),
                        'Transition saved children overlap within a reviewed source face; a duplicate cannot conceal a hole')
    incomplete = [(expected[i]['role'], i, area, face['area']) for i, (area, face) in enumerate(zip(areas, expected))
                  if abs(area-face['area']) > max(2e-5, face['area']*4e-5)]
    require(not incomplete, f'Transition has missing or duplicate pavement, underside, barrier, or support surface: {incomplete[:3]}')
    return {'passed': True, 'reviewed_source_faces_checked': len(expected),
            'saved_indexed_faces_checked': len(faces), 'maximum_affine_uv_error': max_uv_error,
            'source_face_child_overlap_pairs_checked': overlap_pairs,
            'absolute_area_and_overlap_tolerance_m2': 2e-5,
            'relative_area_and_overlap_tolerance': 4e-5,
            'zero_or_sub_float32_area_faces_ignored': ignored,
            'surface_distance_tolerance_m': POSITION_EPS,
            'complete_closed_support_solids': len(support_contract()),
            'complete_native_barrier_sections_per_deck': 10,
            'complete_pavement_and_closed_elevated_deck_bodies': True,
            'measured_native_outer_overhang_m': DD_MAX-8.0}


def _sample_pixels(image, u, v):
    x, y = (u % 1.)*128.-.5, (v % 1.)*128.-.5
    ix, iy = math.floor(x), math.floor(y)
    fx, fy = x-ix, y-iy
    return tuple(sum(image[(ix+a) % 128, (iy+b) % 128][c]
                     * (fx if a else 1.-fx) * (fy if b else 1.-fy)
                     for a, b in ((0, 0), (1, 0), (0, 1), (1, 1))) for c in range(4))


def reconstruct_atlas(native_images, *, mirrored=False):
    """Independent pixel calculation from fingerprinted native asphalt images."""
    result = bytearray(512*1024*4)
    dd, ground = native_images[0x5713000E].load(), native_images[0x5703000E].load()
    for deck, base in (('upper', 8), ('lower', 264)):
        for row in range(1024):
            s = (row-128+.5)/8.
            native_station = 16.-s if mirrored else s
            phase, ground_phase = (native_station-DD_OFFSET)/DD_WIDTH, native_station/16.
            if deck == 'lower':
                phase, ground_phase = 1.-phase, 1.-ground_phase
            rgb = 1.-_fade(deck, s)
            t = min(1., max(0., _height(deck, s)/.25))
            alpha = 1.-t*t*(3.-2.*t)
            for column in range(-2, 130):
                u = ((column % 128)+.5)/128.
                a, b = _sample_pixels(dd, u, phase), _sample_pixels(ground, u, ground_phase)
                offset = (row*512+base+column)*4
                result[offset:offset+4] = bytes(max(0, min(255, round(x+(alpha if c == 3 else rgb)*(y-x))))
                                               for c, (x, y) in enumerate(zip(a, b)))
    return bytes(result)


def check_atlas(resources, piece, donors=None):
    from scp.preview import decode_fsh
    ids = piece.get('authored_texture_ids')
    require(ids == [piece['tile_ids'][0]], 'Transition needs its one allocated atlas at its first tile ID')
    atlas_id = contract._number(ids[0])
    mirrored = contract._mirrored(piece)
    require((*TEXTURE, atlas_id) in resources, 'Transition atlas is missing')
    image = decode_fsh(decompress(resources[*TEXTURE, atlas_id])).convert('RGBA')
    require(image.size == (512, 1024), 'Transition atlas dimensions changed')
    digest = hashlib.sha256(image.tobytes()).hexdigest()
    reconstructed = False
    capture = donors.get('rhw4_textures') if donors else None
    if capture is None and donors and all((*TEXTURE, iid) in donors for iid in NATIVE_TEXTURE_PINS):
        capture = donors
    if capture is not None:
        native = {}
        for iid, pin in NATIVE_TEXTURE_PINS.items():
            raw = decompress(capture[*TEXTURE, iid])
            require(hashlib.sha256(raw).hexdigest() == pin, 'Transition native texture input changed')
            native[iid] = decode_fsh(raw).convert('RGBA')
            require(native[iid].size == (128, 128), 'Transition native texture dimensions changed')
        require(hashlib.sha256(reconstruct_atlas(native, mirrored=mirrored)).hexdigest() == digest,
                'Saved transition atlas differs from independent native colour/alpha reconstruction')
        reconstructed = True
    expected_digest = MIRRORED_ATLAS_RGBA_SHA256 if mirrored else ATLAS_RGBA_SHA256
    require(expected_digest is not None and digest == expected_digest,
            'Saved transition atlas colour, alpha, wear, lane markings, or repeat gutters changed')
    return {'passed': True, 'rgba_sha256': digest, 'pixels_checked': 512*1024,
            'independently_reconstructed_from_native_inputs_this_run': reconstructed,
            'alpha_transition_height_m': .25, 'native_external_collars_unchanged': True}


def check_corridors(faces, resources, piece):
    """Continuous triangle/prism collision and continuous pavement coverage."""
    from .ramp_verify import _covered, _intrudes
    mirrored = piece.get('transition_variant') == 'mirrored'
    buckets = defaultdict(set)
    for i, face in enumerate(faces):
        for key in _keys(face['points'], size=4.):
            buckets[key].add(i)
    segments, intersections = 0, 0
    for cell, tile in zip(contract.CELLS, piece['tile_ids']):
        for route in parse_paths(decompress(resources[*PATH, contract._number(tile)]))['routes']:
            points = [(p[0]+16.*cell[0], p[1]-16.*cell[1], p[2]) for p in route['points']]
            if mirrored:
                points = [(16.-p[0], p[1], p[2]) for p in points]
            source_column = 1-cell[0] if mirrored else cell[0]
            deck = 'lower' if source_column == 1 and all(abs(p[0]-points[0][0]) < 1e-7 for p in points) else 'upper'
            # At the initial collar both decks have the same plan alignment.
            if min(p[2] for p in points) > 14.9:
                deck = 'upper'
            ratio = 1.+DATUM[deck]/(15. if deck == 'upper' else 7.5)
            for first, last in zip(points, points[1:]):
                candidates = set()
                box = ((min(first[0], last[0])-1.26, min(first[1], last[1])-1.26, 0.),
                       (max(first[0], last[0])+1.26, max(first[1], last[1])+1.26, 0.))
                for key in _keys(box, size=4.):
                    candidates.update(buckets.get(key, ()))
                relevant = [faces[i] for i in candidates]
                supported_a, supported_b = (*first[:2], first[2]*ratio), (*last[:2], last[2]*ratio)
                pavement = [face for face in relevant if face['role'].startswith(deck+'-pavement-')]
                require(_covered(supported_a, supported_b, pavement),
                        f'Transition pavement does not continuously support actual saved {deck} PATH segment: {first}, {last}')
                for face in relevant:
                    if max(p[2] for p in face['points']) < min(first[2], last[2])+.03 or min(p[2] for p in face['points']) > max(first[2], last[2])+3.8:
                        continue
                    intersections += 1
                    require(not _intrudes(first, last, face['points'], 1.25, 3.8),
                            f"Transition vehicle corridor intersects {face['role']} at {first}, {last}")
                segments += 1
    return {'passed': True, 'continuous_saved_segments_checked': segments,
            'actual_face_prism_intersections_checked': intersections,
            'half_width_m': 1.25, 'height_m': 3.8,
            'scope': 'Continuous straight graded prisms for every saved lane chord, including complete support faces; vehicle shapes, structural capacity, and game rendering remain unverified.'}


def _clip_in_box(polygon, axis, bound, sign):
    """Clip an actual face against one strict interior plane of a support."""
    if not polygon:
        return []
    result = []
    previous = polygon[-1]
    before = sign*(previous[axis]-bound)
    for current in polygon:
        after = sign*(current[axis]-bound)
        if (before >= 0.) != (after >= 0.):
            t = before/(before-after)
            result.append(tuple(a+t*(b-a) for a, b in zip(previous, current)))
        if after >= 0.:
            result.append(current)
        previous, before = current, after
    return result


def check_support_clearance(faces):
    """No reviewed closed support may pierce the opposite deck or barrier."""
    checked = 0
    for name, deck, s, low, high, half, bottom, top in support_contract():
        center, normal = _frame(deck, s)
        tangent = normal[1], -normal[0]
        opposite = 'lower' if deck == 'upper' else 'upper'
        for face in faces:
            role = face['role']
            if not (role.startswith(opposite+'-pavement-') or role == opposite+'-body' or role == opposite+'-barrier'):
                continue
            if max(p[2] for p in face['points']) < bottom or min(p[2] for p in face['points']) > top:
                continue
            polygon = [((p[0]-center[0])*normal[0]+(p[1]-center[1])*normal[1],
                        (p[0]-center[0])*tangent[0]+(p[1]-center[1])*tangent[1], p[2])
                       for p in face['points']]
            if (max(p[0] for p in polygon) < low or min(p[0] for p in polygon) > high
                    or max(p[1] for p in polygon) < -half or min(p[1] for p in polygon) > half):
                continue
            checked += 1
            for axis, bound, sign in ((0, low+POSITION_EPS, 1), (0, high-POSITION_EPS, -1),
                                       (1, -half+POSITION_EPS, 1), (1, half-POSITION_EPS, -1),
                                       (2, bottom+POSITION_EPS, 1), (2, top-POSITION_EPS, -1)):
                polygon = _clip_in_box(polygon, axis, bound, sign)
            require(not polygon, f'Transition closed support {name} intersects opposite {role}')
    return {'passed': True, 'closed_support_solids_checked': len(support_contract()),
            'opposite_surface_box_intersections_checked': checked,
            'interior_distance_tolerance_m': POSITION_EPS,
            'structural_capacity_tested': False}


def _plan_overlap(first, second):
    """Intersect two projected triangles, retaining world east/north only."""
    polygon = [p[:2] for p in first]
    winding = 1. if _normal(second)[2] > 0. else -1.
    for a, b in zip(second, (*second[1:], second[0])):
        if not polygon:
            break
        def distance(p):
            return winding*((b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0]))
        result = []
        previous = polygon[-1]
        before = distance(previous)
        for current in polygon:
            after = distance(current)
            if (before >= 0.) != (after >= 0.):
                t = before/(before-after)
                result.append(tuple(x+t*(y-x) for x, y in zip(previous, current)))
            if after >= 0.:
                result.append(current)
            previous, before = current, after
        polygon = result
    if len(polygon) < 3:
        return []
    area = abs(sum(a[0]*b[1]-a[1]*b[0] for a, b in zip(polygon, (*polygon[1:], polygon[0]))))/2.
    return polygon if area > MIN_AREA else []


def _plane_height(face, point):
    normal = _normal(face)
    a = face[0]
    return a[2]-(normal[0]*(point[0]-a[0])+normal[1]*(point[1]-a[1]))/normal[2]


def check_deck_clearance(faces):
    """Compare both complete deck/barrier surfaces wherever their plans overlap."""
    upper, lower = [], []
    for face in faces:
        role = face['role']
        if not ('-pavement-' in role or role in ('upper-body', 'lower-body', 'upper-barrier', 'lower-barrier')):
            continue
        if abs(_normal(face['points'])[2]) <= 1e-12:
            continue
        (upper if role.startswith('upper-') else lower).append(face)
    bins = defaultdict(set)
    for index, face in enumerate(lower):
        for key in _keys(face['points'], size=4.):
            bins[key].add(index)
    pairs, exact, ground_edge_contacts = 0, 0, 0
    for face in upper:
        candidates = set()
        for key in _keys(face['points'], size=4.):
            candidates.update(bins.get(key, ()))
        for index in candidates:
            other = lower[index]
            pairs += 1
            if min(p[2] for p in face['points']) > max(p[2] for p in other['points'])+POSITION_EPS:
                continue
            overlap = _plan_overlap(face['points'], other['points'])
            if not overlap:
                continue
            exact += 1
            gap = min(_plane_height(face['points'], p)-_plane_height(other['points'], p) for p in overlap)
            # The declared native +1 mm outside edge fades with height. Once
            # the upper slab's underside reaches ground, its last <=0.067 mm
            # of shoulder can touch the adjacent ground shoulder. Bind that
            # exact measured ground-only boundary contact, not a free general
            # mesh-intersection tolerance or a vehicle-lane exception.
            ground_edge = (face['role'] == 'upper-body'
                           and other['role'] == 'lower-pavement-native-ground'
                           and all(abs(p[2]) <= POSITION_EPS for p in other['points'])
                           and all(8.-POSITION_EPS <= p[0] <= 8.+(DD_MAX-8.)/15.+POSITION_EPS for p in overlap)
                           and gap >= -POSITION_EPS)
            ground_edge_contacts += bool(ground_edge and gap <= POSITION_EPS)
            require(gap > POSITION_EPS or ground_edge,
                    f"Transition upper {face['role']} intersects or drops below lower {other['role']}; gap={gap}")
    return {'passed': True, 'indexed_upper_lower_surface_pairs_checked': pairs,
            'overlapping_plan_pairs_requiring_exact_height_comparison': exact,
            'interior_distance_tolerance_m': POSITION_EPS,
            'measured_native_ground_shoulder_edge_contacts': ground_edge_contacts,
            'maximum_declared_ground_shoulder_contact_width_m': (DD_MAX-8.)/15.,
            'native_ground_edge_contact_is_outside_vehicle_lanes': True}


def canonical_surface_frame(faces, *, mirrored=False):
    """Put actual B triangles in the independent original geometry frame.

    Reflection changes handedness. Reverse each saved index winding as well
    as reflecting its position, keeping the same saved UV attached to each
    vertex. This exact isometry preserves distances, widths, heights,
    collision prisms, and support solids. Native UV expectations separately
    select the measured original or mirrored longitudinal phase.
    """
    if not mirrored:
        return faces
    result = []
    for face in faces:
        points = tuple((16.-face['points'][i][0], *face['points'][i][1:]) for i in (0, 2, 1))
        result.append({**face, 'points': points, 'uv': tuple(face['uv'][i] for i in (0, 2, 1)),
                       'upward': _normal(points)[2] > 1e-12})
    return result


def check_models(resources, piece, donors=None):
    contract._spec(piece)
    mirrored = contract._mirrored(piece)
    atlas = check_atlas(resources, piece, donors)
    faces = []
    for cell, tile in zip(contract.CELLS, piece['tile_ids']):
        tile = contract._number(tile)
        require(all((*S3D, tile+zoom) in resources for zoom in range(5)), 'Transition model zoom is missing')
        raw = decompress(resources[*S3D, tile])
        require(all(decompress(resources[*S3D, tile+zoom]) == raw for zoom in range(5)),
                'Transition saved zoom changes the complete physical geometry')
        faces.extend(decode_faces(raw, cell, mirrored=mirrored))
    faces = canonical_surface_frame(faces, mirrored=mirrored)
    surfaces = check_complete_surfaces(faces, contract._number(piece['authored_texture_ids'][0]), mirrored=mirrored)
    corridors = check_corridors(faces, resources, piece)
    supports = check_support_clearance(faces)
    deck_clearance = check_deck_clearance(faces)
    from .modular_partition_verify import check_preview
    check_preview(resources, piece)
    from .shadow_verify import check_resources
    shadows = check_resources(resources, piece)
    from .orthogonal_approaches import check_native_boundary_paths
    native_boundaries = check_native_boundary_paths(donors, piece, resources)
    return {'passed': True, 'indexed_triangles_checked': len(faces),
            'texture_ids': sorted({face['texture'] for face in faces}),
            'all_five_zooms_exact': True, 'preview_matches_all_saved_cells': True,
            'independent_complete_surfaces': surfaces, 'continuous_saved_vehicle_corridors': corridors,
            'closed_support_clearance': supports,
            'complete_deck_and_barrier_clearance': deck_clearance,
            'native_draggable_boundary_contract': native_boundaries,
            'independent_native_atlas': atlas, 'proper_rotation_geometry_invariant': True,
            **shadows, 'game_rendering_tested': False, 'structural_capacity_tested': False}
