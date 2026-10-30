"""Check saved shoulder asphalt independently of the repainting writer.

Literal native DD measurements supply the transverse texture field. Indexed
S3D faces, rather than preview colours or authoring labels, supply evidence.
"""
from __future__ import annotations

import math
import struct

from scp.models import parse_s3d
from scp.track_paths import S3D

ROOT_TWO = math.sqrt(2.)
ERASE_LOW, ERASE_HIGH = 4.3125, 4.8125
INNER_ASPHALT_U = 29.5 / 128.
SHOULDER_LOW, SHOULDER_HIGH = 3.9, 7.15
UV_TOLERANCE = 3e-6
# Stations measured on the retained native highway axis, midway along each
# branch's repaint footprint; the two independent decks have opposite sides.
MOUTHS = (("lower-off", 65.7028492597523, 1, 7.5),
          ("lower-on", -65.7028492597523, 1, 7.5),
          ("upper-off", -94.271538625313, -1, 15.),
          ("upper-on", 94.271538625313, -1, 15.))


def _need(value, message):
    if not value:
        raise ValueError(message)


def _pose(point, owner):
    east = point[0] + 16. * owner['local_cell'][0]
    north = -point[2] - 16. * owner['local_cell'][1]
    for _ in range(owner['angle'] // 90):
        east, north = -north, east
    return east + owner['origin'][0], north + owner['origin'][1], point[1], *point[3:]


def _clip(polygon, distance):
    output = []
    if not polygon:
        return output
    before, previous = polygon[-1], distance(polygon[-1])
    for point in polygon:
        current = distance(point)
        if (previous >= 0.) != (current >= 0.):
            t = previous / (previous - current)
            output.append(tuple(a + t * (b - a) for a, b in zip(before, point)))
        if current >= 0.:
            output.append(point)
        before, previous = point, current
    return output


def _area(polygon):
    return abs(sum(a[0] * b[1] - b[0] * a[1]
                   for a, b in zip(polygon, polygon[1:] + polygon[:1]))) / 2.


def _lateral(point):
    # Registered assembly origin is shifted by (64, -64) from the measured
    # native donor frame, whose diagonal centre is (4, -4).
    return (point[1] - point[0] + 136.) / ROOT_TWO


def check_faces(faces):
    """Check the surrounding affine U field and twelve erased-line samples.

    Within the 3.9–7.15 m shoulder window, outside the half-metre erase band,
    every clipped polygon vertex must retain the native affine U field. That establishes the whole clipped
    triangle's U field, rather than only a sparse set of surface samples.
    The old line itself has three explicit samples at each of four mouths.
    V preservation is established separately by before/after resource audit;
    this check does not claim a complete texture-colour or game assessment.
    """
    selected, polygons, maximum = [], 0, 0.
    for face in faces:
        if face['texture'] != 0x5713000E:
            continue
        points = face['points']
        height = points[0][2]
        if (min(abs(height - 7.5), abs(height - 15.)) > 1e-5
                or any(abs(p[2] - height) > 1e-6 for p in points)):
            continue
        signed = sum(a[0] * b[1] - b[0] * a[1]
                     for a, b in zip(points, points[1:] + points[:1]))
        if signed <= 1e-10:
            continue
        side = 1 if abs(height - 7.5) < 1e-5 else -1
        polygon = [(*point, *uv) for point, uv in zip(points, face['uv'])]
        q = lambda p: side * _lateral(p)
        shoulder = _clip(_clip(polygon, lambda p: q(p) - SHOULDER_LOW),
                         lambda p: SHOULDER_HIGH - q(p))
        if len(shoulder) < 3 or _area(shoulder) < 1e-9:
            continue
        selected.append(face)
        # The guard excludes the intentional two-UV seam at the erased line's
        # outer boundary, plus the saved format's sub-millimetre rounding.
        for region in (_clip(shoulder, lambda p: ERASE_LOW - .0002 - q(p)),
                       _clip(shoulder, lambda p: q(p) - ERASE_HIGH - .0002)):
            if len(region) < 3 or _area(region) < 1e-9:
                continue
            polygons += 1
            for point in region:
                error = abs(point[3] - (.5 - q(point) / 16.))
                maximum = max(maximum, error)
                _need(error <= UV_TOLERANCE,
                      'Saved shoulder asphalt differs from the native UV field outside the erased edge')
    _need(polygons > 0, 'Saved shoulder asphalt check found no surrounding native pavement')
    samples = 0
    for name, station, side, height in MOUTHS:
        for q in (4.4, 4.5, 4.7):
            lateral = side * q
            point = (68. + (station - lateral) / ROOT_TWO,
                     -68. + (station + lateral) / ROOT_TWO)
            matches = []
            for face in selected:
                a, b, c = face['points']
                if abs(a[2] - height) > 1e-5:
                    continue
                den = ((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]))
                u = ((point[0]-a[0])*(c[1]-a[1]) - (point[1]-a[1])*(c[0]-a[0])) / den
                v = ((b[0]-a[0])*(point[1]-a[1]) - (b[1]-a[1])*(point[0]-a[0])) / den
                if min(u, v, 1.-u-v) >= -1e-7:
                    matches.append((1.-u-v)*face['uv'][0][0] + u*face['uv'][1][0] + v*face['uv'][2][0])
            _need(matches and all(abs(value-INNER_ASPHALT_U) <= UV_TOLERANCE for value in matches),
                  f'Saved old highway edge is not erased with adjacent native asphalt at {name}')
            samples += 1
    return {'passed': True, 'surrounding_native_uv_polygons_checked': polygons,
            'maximum_native_u_error': maximum, 'erased_edge_samples_checked': samples,
            'ramp_mouths_checked': len(MOUTHS), 'erase_band_m': [ERASE_LOW, ERASE_HIGH],
            'shoulder_window_m': [SHOULDER_LOW, SHOULDER_HIGH],
            'game_rendering_tested': False,
            'coverage_limit': 'Affine native U in the 3.9–7.15 m shoulder window outside the half-metre band, plus three erased-line samples per mouth; V preservation is a separate before/after audit, and game appearance is unverified.'}


def check_saved_shoulder_uvs(owners, piece_resources):
    faces = []
    for owner in owners.values():
        model = parse_s3d(piece_resources[owner['piece_id']][*S3D, owner['tile'] + 4])
        for mesh in model['meshes']:
            _need(len(mesh['frames']) == 1, 'Shoulder UV check requires a static indexed model')
            vi, ii, pi, mi = mesh['frames'][0]
            textures = model['materials'][mi]['textures']
            if textures != [0x5713000E]:
                continue
            block = model['vertices'][vi]
            points = [struct.unpack_from('<5f', block['data'], offset)
                      for offset in range(0, len(block['data']), block['stride'])]
            indices = model['indices'][ii]['values']
            for kind, first, count in model['primitives'][pi]:
                _need(kind == 0 and count % 3 == 0, 'Shoulder UV check requires triangle-list primitives')
                for offset in range(first, first + count, 3):
                    triangle = [_pose(points[index], owner) for index in indices[offset:offset+3]]
                    faces.append({'texture': textures[0], 'points': tuple(p[:3] for p in triangle),
                                  'uv': tuple(p[3:] for p in triangle)})
    return check_faces(faces)
