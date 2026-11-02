"""Inspect bounded saved barrier joints independently of the road writer.

Literal native profiles and the retained continuous cubic define transverse
sections through the former gaps. These checks establish oriented coverage
of those sections, not manifold closure of every native road model.
"""
from __future__ import annotations

import math

from scp.dbpf import require
from scp.models import parse_s3d, positions, validate_s3d

S3D = (0x5AD0E817, 0xBADB57F1)
BARRIER_TEXTURES = {0x5EB4BEE9, 0x5EB4BEEE}
# Independent transcription of the measured native Jersey cross-section.
PROFILE = ((0., 0.), (.21875, .328125), (.265625, 1.390625),
           (.5625, 1.390625), (.625, .328125), (.828125, 0.))
MOUTHS = (
    ('lower-off', 75.80184694319789, -1, 1, 7.5, 63.80184694319789),
    ('lower-on', -75.80184694319789, 1, 1, 7.5, 63.80184694319789),
    ('upper-off', -109.74297244015216, 1, -1, 15., 97.74297244015216),
    ('upper-on', 109.74297244015216, -1, -1, 15., 97.74297244015216),
)
SECTION_FRACTIONS = (.125, .375, .625, .875)
END_GUARD_M = .003
PLANE_TOLERANCE_M = .001
POSITION_TOLERANCE_M = .00002


def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def _sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def _curve(t, length):
    """Continuous reference in outward highway distance and native-side v.

    The two retained cubic families have longitudinal control fractions
    0, .38, .62, 1, and lateral controls lane, lane, junction, junction.
    Analytic derivative normals deliberately differ from the writer's
    sampled-polyline miter implementation.
    """
    lane, spread = 3.2 / math.sqrt(2.), (20. * math.sqrt(2.) - 3.2 / math.sqrt(2.))
    station = length * (3. * .38 * t * (1. - t) ** 2 + 3. * .62 * t * t * (1. - t) + t ** 3)
    lateral = lane + spread * (3. * t * t - 2. * t ** 3)
    ds = 3. * length * (.38 * (1. - t) ** 2 + .48 * (1. - t) * t + .38 * t * t)
    dv = spread * 6. * t * (1. - t)
    speed = math.hypot(ds, dv)
    return station, lateral, -dv / speed, ds / speed


def _anchor(length, barrier_side, inset, offset):
    """Intersect an analytic offset curve with native v=8-inset."""
    lo, hi = 0., 1.
    for _ in range(64):
        t = (lo + hi) / 2.
        station, lateral, ns, nv = _curve(t, length)
        if lateral + barrier_side * offset * nv < 8. - inset:
            lo = t
        else:
            hi = t
    station, _lateral, ns, _nv = _curve((lo + hi) / 2., length)
    return station + barrier_side * offset * ns


def _world(u, v, height):
    # The registered assembly shifts the original construction frame by
    # +64 m east and -64 m north. Heights retain the zero-pavement datum.
    root = math.sqrt(2.)
    return ((u - v) / root + 68., (u + v) / root - 68., height)


def section_contracts():
    """Return 160 independently derived unrotated bridge-section witnesses."""
    result = []
    for name, u0, direction, native_side, deck, length in MOUTHS:
        for barrier_side in (1, -1):
            for band, ((ia, ha), (ib, hb)) in enumerate(zip(PROFILE, PROFILE[1:])):
                for fraction in SECTION_FRACTIONS:
                    inset = ia + fraction * (ib - ia)
                    height = ha + fraction * (hb - ha)
                    old_end = _anchor(length, barrier_side, inset, 3.)
                    miter = _anchor(length, barrier_side, inset, 3. - inset)
                    first, last = sorted((old_end, miter))
                    require(last - first > 2. * END_GUARD_M,
                            'Independent barrier section is shorter than its encoding guard')
                    first += END_GUARD_M; last -= END_GUARD_M
                    normal = (-native_side * (hb - ha) / math.sqrt(2.),
                              native_side * (hb - ha) / math.sqrt(2.), ib - ia)
                    result.append({'ramp_id': name, 'barrier_side': barrier_side, 'profile_band': band,
                        'fraction': fraction, 'deck_height_m': deck,
                        'first': _world(u0 + direction * first, native_side * (8. - inset), deck + height),
                        'last': _world(u0 + direction * last, native_side * (8. - inset), deck + height),
                        'outward_normal': normal, 'reference_gap_length_m': last - first})
    return result


def _turn(point, quarters):
    x, y, z = point
    for _ in range(quarters % 4):
        x, y = -y, x
    return x, y, z


def _face(points):
    a, b, c = points
    normal = _cross(_sub(b, a), _sub(c, a))
    return {'points': tuple(points), 'normal': normal,
            'bounds': tuple((min(p[axis] for p in points), max(p[axis] for p in points)) for axis in range(3))}


def decode_faces(owners, piece_resources):
    """Read all indexed barrier faces, including downward/back-facing ones."""
    result = []
    for owner in owners.values():
        model = parse_s3d(piece_resources[owner['piece_id']][*S3D, owner['tile'] + 4])
        validate_s3d(model)
        for mesh in model['meshes']:
            require(len(mesh['frames']) == 1, 'Saved barrier verification requires static models')
            vi, ii, pi, mi = mesh['frames'][0]
            if not BARRIER_TEXTURES.intersection(model['materials'][mi]['textures']):
                continue
            vertices = positions(model['vertices'][vi]); indices = model['indices'][ii]['values']
            for kind, start, count in model['primitives'][pi]:
                require(kind == 0 and count % 3 == 0, 'Saved barrier model has non-triangle primitives')
                for offset in range(start, start + count, 3):
                    points = []
                    for index in indices[offset:offset + 3]:
                        east, height, south = vertices[index]
                        point = (east + 16. * owner['local_cell'][0],
                                 -south - 16. * owner['local_cell'][1], height)
                        x, y, h = _turn(point, owner['angle'] // 90)
                        points.append((x + owner['origin'][0], y + owner['origin'][1], h))
                    if max(p[2] for p in points) > 7.5:
                        result.append(_face(points))
    return result


def _interval(first, last, face, outward):
    """Exact interval on a triangle after bounded plane and winding checks."""
    a, b, c = face['points']; normal = face['normal']
    normal_length = math.sqrt(_dot(normal, normal)); desired_length = math.sqrt(_dot(outward, outward))
    if normal_length < 1e-12 or _dot(normal, outward) < .99 * normal_length * desired_length:
        return None
    if max(abs(_dot(normal, _sub(point, a))) / normal_length for point in (first, last)) > PLANE_TOLERANCE_M:
        return None
    u, v = _sub(b, a), _sub(c, a)
    uu, uv, vv = _dot(u, u), _dot(u, v), _dot(v, v)
    determinant = uu * vv - uv * uv
    if determinant <= 1e-20:
        return None
    weights = []
    for point in (first, last):
        w = _sub(point, a); wu, wv = _dot(w, u), _dot(w, v)
        one, two = (vv * wu - uv * wv) / determinant, (uu * wv - uv * wu) / determinant
        weights.append((1. - one - two, one, two))
    low, high = 0., 1.
    tolerance = POSITION_TOLERANCE_M / max(math.sqrt(uu), math.sqrt(vv), 1e-12)
    for before, after in zip(*weights):
        delta = after - before
        if abs(delta) < 1e-15:
            if before < -tolerance:
                return None
        elif delta > 0.:
            low = max(low, (-tolerance - before) / delta)
        else:
            high = min(high, (-tolerance - before) / delta)
        if high < low:
            return None
    return max(0., low), min(1., high)


def check_faces(faces, *, rotations=(0, 1, 2, 3)):
    """Require continuous oriented coverage across all declared bridge strips."""
    contracts = section_contracts(); counts = []
    for quarter in rotations:
        rotated = [_face([_turn(point, quarter) for point in face['points']]) for face in faces]
        for section in contracts:
            first, last = _turn(section['first'], quarter), _turn(section['last'], quarter)
            outward = _turn(section['outward_normal'], quarter)
            low = tuple(min(a, b) - PLANE_TOLERANCE_M for a, b in zip(first, last))
            high = tuple(max(a, b) + PLANE_TOLERANCE_M for a, b in zip(first, last))
            candidates = [face for face in rotated if all(face['bounds'][axis][1] >= low[axis]
                          and face['bounds'][axis][0] <= high[axis] for axis in range(3))]
            intervals = sorted(interval for face in candidates
                               for interval in [_interval(first, last, face, outward)] if interval is not None)
            cursor = 0.
            for start, end in intervals:
                if start > cursor + 1e-7:
                    break
                cursor = max(cursor, end)
            require(cursor >= 1. - 1e-7,
                    f'Saved barrier mouth has an open or inward-facing profile strip: '
                    f'ramp={section["ramp_id"]}, barrier={section["barrier_side"]}, '
                    f'band={section["profile_band"]}, section={section["fraction"]}, rotation={quarter * 90}')
        counts.append({'rotation_ccw_degrees': quarter * 90, 'continuous_profile_sections_checked': len(contracts)})
    return {'passed': True, 'ramp_mouths_checked': 4, 'barriers_per_mouth': 2,
            'profile_bands_per_barrier': 5, 'sections_per_profile_band': len(SECTION_FRACTIONS),
            'continuous_profile_sections_checked': sum(row['continuous_profile_sections_checked'] for row in counts),
            'proper_rotations_checked': len(counts), 'rotations': counts,
            'reference_sampling_guard_m': END_GUARD_M, 'plane_tolerance_m': PLANE_TOLERANCE_M,
            'outward_winding_checked': True, 'game_rendering_tested': False,
            'coverage_limit': 'Continuous indexed-triangle coverage of 160 independent barrier-joint cross-sections in each proper rotation; this is not all-model manifold closure, every possible intervening surface point, or an in-game observation.'}


def check_saved_barrier_mouths(owners, piece_resources):
    return check_faces(decode_faces(owners, piece_resources))
