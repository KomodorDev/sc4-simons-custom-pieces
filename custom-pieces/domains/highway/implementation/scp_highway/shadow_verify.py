"""Independently compare saved highway geometry with saved shadow masks.

This reader does not import the carrier writer or its triangle filtering.
It reconstructs referenced faces, clips them at ground height, projects them
through the native light, and compares the resulting footprint with actual
texture coverage through the saved card's inverse affine UV transform.
"""
from __future__ import annotations

from functools import lru_cache
import hashlib
import math
import struct

from PIL import Image, ImageChops, ImageDraw, ImageFilter

from scp.dbpf import require
from scp.model_shadows import bindings
from scp.models import parse_s3d, positions, validate_s3d
from scp.preview import decode_fsh

S3D = (0x5AD0E817, 0xBADB57F1)
TEXTURE = (0x7AB50E44, 0x1ABE787D)
# Independently transcribed native Float32 light stores; not writer imports.
SUN = (0.6532814502716064, -0.7071067690849304, -0.27059805393218994)
LOCAL_LIGHT = (-0.27059805393218994, -0.7071067690849304, -0.6532814502716064)
METRES_PER_PIXEL = .125
POSITION_TOLERANCE_M = 1e-4


def _turn(point, quarter):
    x, y, z = point
    return ((x, y, z), (-z, y, x), (-x, y, -z), (z, y, -x))[quarter % 4]


def _ground(point, light):
    return (point[0] - point[1] * light[0] / light[1],
            point[2] - point[1] * light[2] / light[1])


def _area3(points):
    a, b, c = points
    ab = tuple(b[i] - a[i] for i in range(3))
    ac = tuple(c[i] - a[i] for i in range(3))
    return math.sqrt(sum((ab[(i + 1) % 3] * ac[(i + 2) % 3]
                          - ab[(i + 2) % 3] * ac[(i + 1) % 3]) ** 2
                         for i in range(3))) / 2


def _clip_face(face):
    """Clip with a previous/current edge walk, then triangulate the polygon."""
    if max(p[1] for p in face) <= 0:
        return []
    polygon = []
    previous = face[-1]
    previous_inside = previous[1] >= 0
    for current in face:
        current_inside = current[1] >= 0
        if current_inside != previous_inside:
            ratio = previous[1] / (previous[1] - current[1])
            polygon.append((previous[0] + ratio * (current[0] - previous[0]), 0.,
                            previous[2] + ratio * (current[2] - previous[2])))
        if current_inside:
            polygon.append(current)
        previous, previous_inside = current, current_inside
    return [triangle for i in range(1, len(polygon) - 1)
            if _area3(triangle := (polygon[0], polygon[i], polygon[i + 1])) > 1e-12]


@lru_cache(maxsize=96)
def _read_source(raw):
    model = parse_s3d(raw)
    validate_s3d(model)
    require(struct.unpack_from('<H', model['anim_header'])[0] == 1,
            'Highway shadow geometry requires a static saved source')
    for _name, chunk in model['trailing']:
        require(len(chunk) == 12 and chunk[8:] == b'\0' * 4,
                'Highway shadow geometry cannot ignore source transforms')
    faces, seen = [], set()
    original_count = ground_count = clipped_count = vertical_count = 0
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        if (vi, ii, pi, mi) in seen:
            continue
        seen.add((vi, ii, pi, mi))
        vertices = positions(model['vertices'][vi])
        indices = model['indices'][ii]['values']
        material_flags, = struct.unpack_from('<I', model['materials'][mi]['raw'])
        for kind, first, count in model['primitives'][pi]:
            require(kind == 0 and count % 3 == 0,
                    'Highway shadow geometry requires referenced triangle lists')
            for at in range(first, first + count, 3):
                face = tuple(vertices[index] for index in indices[at:at + 3])
                if _area3(face) <= 1e-12:
                    continue
                original_count += 1
                if max(point[1] for point in face) <= 0:
                    ground_count += 1
                    continue
                require(not material_flags & 0x11,
                        'Highway shadow source has alpha-test or blending enabled')
                if min(point[1] for point in face) < 0:
                    clipped_count += 1
                if abs((face[1][0] - face[0][0]) * (face[2][2] - face[0][2])
                       - (face[1][2] - face[0][2]) * (face[2][0] - face[0][0])) <= 1e-12:
                    vertical_count += 1
                faces.extend(_clip_face(face))
    return tuple(faces), {'referenced_faces': original_count,
                         'ground_or_below_faces_excluded': ground_count,
                         'ground_crossing_faces_clipped': clipped_count,
                         'vertical_faces_retained': vertical_count}


def _quad(raw):
    model = parse_s3d(raw)
    block = model['vertices'][model['meshes'][0]['frames'][0][0]]
    require(block['stride'] == 20 and block['format'] == 0x80004001,
            'Saved shadow card has an unsupported vertex format')
    data = [struct.unpack_from('<5f', block['data'], n * block['stride'])
            for n in range(len(block['data']) // block['stride'])]
    require(len(data) == 4 and all(math.isfinite(v) for p in data for v in p),
            'Saved shadow card must have four finite XYZ/UV corners')
    require(tuple(p[3:] for p in data) == ((0., 0.), (1., 0.), (1., 1.), (0., 1.)),
            'Saved shadow card has the wrong corner UV order')
    q = [_ground(p, LOCAL_LIGHT) for p in data]
    a, b, c, d = q
    u, v = (b[0] - a[0], b[1] - a[1]), (d[0] - a[0], d[1] - a[1])
    determinant = u[0] * v[1] - u[1] * v[0]
    require(determinant > 1e-9, 'Saved shadow card has a singular or reversed projection')
    error = max(abs(c[i] - (b[i] + d[i] - a[i])) for i in range(2))
    require(error <= POSITION_TOLERANCE_M,
            'Saved shadow card exceeds Float32 affine projection tolerance')

    def uv(point):
        dx, dz = point[0] - a[0], point[1] - a[1]
        return ((dx * v[1] - dz * v[0]) / determinant,
                (u[0] * dz - u[1] * dx) / determinant)

    return q, uv, error


def _world_projection_check(faces):
    # Exercise the explicit native selector for every original referenced
    # point, rather than relying on an image or the writer's pose report.
    points = set(point for face in faces for point in face)
    maximum = 0.
    for object_rotation in range(4):
        for camera_rotation in range(4):
            selected = (3 * ((camera_rotation + 1) % 4) + object_rotation) % 4
            light = _turn(SUN, camera_rotation)
            for point in points:
                expected = _ground(_turn(point, object_rotation), light)
                source = _ground(_turn(point, selected), LOCAL_LIGHT)
                actual = _turn((source[0], 0., source[1]), camera_rotation + 1)
                maximum = max(maximum, abs(actual[0] - expected[0]), abs(actual[2] - expected[1]))
    require(maximum <= 1e-9, 'Native RKT2 selection does not preserve the saved source footprint')
    return maximum


def _check_host(source_raw, model_raws, texture_raws):
    faces, counts = _read_source(source_raw)
    require(faces, 'Declared shadow caster has no above-ground referenced faces')
    variants = []
    for pose, (model_raw, texture_raw) in enumerate(zip(model_raws, texture_raws)):
        quad, inverse, affine_error = _quad(model_raw)
        image = decode_fsh(texture_raw)
        alpha = image.getchannel('A')
        width, height = image.size
        require(width == height and width > 4, 'Saved shadow mask has invalid dimensions')
        # Verify the actual saved rectangle and metric texture resolution.
        projected = [tuple(_ground(_turn(p, pose), LOCAL_LIGHT) for p in face) for face in faces]
        points = [point for face in projected for point in face]
        low = tuple(min(p[axis] for p in points) for axis in range(2))
        high = tuple(max(p[axis] for p in points) for axis in range(2))
        span = width * METRES_PER_PIXEL
        expected_corners = ((low[0] + high[0] - span) / 2, (low[1] + high[1] - span) / 2)
        extent_error = max(abs(quad[0][axis] - expected_corners[axis]) for axis in range(2))
        extent_error = max(extent_error, abs(quad[1][0] - quad[0][0] - span),
                           abs(quad[3][1] - quad[0][1] - span))
        require(extent_error <= POSITION_TOLERANCE_M,
                'Saved shadow card is translated, scaled, or centred on the wrong source geometry')
        expected = Image.new('L', image.size)
        draw = ImageDraw.Draw(expected)
        edge_on = 0
        for triangle in projected:
            a, b, c = triangle
            twice_area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
            if abs(twice_area) < 1e-12:
                edge_on += 1
                continue
            corners = [inverse(point) for point in triangle]
            require(all(-1e-5 <= value <= 1 + 1e-5 for pair in corners for value in pair),
                    'Saved shadow card clips an above-ground source face or model overhang')
            # This independent one-pixel raster deliberately differs from the
            # writer's supersampled coverage. One texture pixel of boundary
            # tolerance preserves subpixel walls without hiding missing areas.
            draw.polygon([(u * width, v * height) for u, v in corners], fill=255)
        actual = alpha.point(lambda value: 255 if value else 0)
        require(actual.getbbox() is not None, 'Saved shadow mask is empty')
        missing = ImageChops.subtract(expected, actual.filter(ImageFilter.MaxFilter(3)))
        phantom = ImageChops.subtract(actual, expected.filter(ImageFilter.MaxFilter(3)))
        require(missing.getbbox() is None,
                'Saved shadow mask omits source geometry beyond one texture pixel')
        require(phantom.getbbox() is None,
                'Saved shadow mask contains phantom or neighbouring geometry beyond one texture pixel')
        variants.append({'relative_pose': pose, 'mask_size': width,
                         'actual_covered_pixels': sum(actual.histogram()[1:]),
                         'ground_shadow_area_m2': sum(alpha.tobytes()) / 255 * METRES_PER_PIXEL ** 2,
                         'edge_on_projected_faces': edge_on,
                         'maximum_card_ground_error_m': extent_error,
                         'maximum_affine_corner_error_m': affine_error})
    return {**counts, 'clipped_elevated_triangles': len(faces), 'variants': variants,
            'proper_object_camera_poses_checked': 16,
            'maximum_native_pose_error_m': _world_projection_check(faces),
            'source_sha256': hashlib.sha256(source_raw).hexdigest()}


def check_resources(resources, piece):
    """Check actual saved canonical geometry and four saved model/texture pairs."""
    from scp import model_shadows
    if not model_shadows.enabled(piece):
        return {'model_shadow_geometry': model_shadows.validate_resources(resources, piece)}
    # Reuse repeated canonical zoom bytes only within this verification call.
    # The enclosing model audit tracks live validator identities and constants;
    # an older inner cache must not bypass a changed clipping or light check.
    _read_source.cache_clear()
    rows = bindings(piece)
    reports, ground_only = [], 0
    for row in rows:
        tile = int(row['canonical_tile_id'], 16)
        require((*S3D, tile) in resources, 'Saved canonical shadow source is missing')
        source = resources[*S3D, tile]
        # One native carrier serves all zooms. A changed canonical geometry
        # therefore needs a deliberately revised shadow contract.
        for zoom in range(1, 5):
            if (*S3D, tile + zoom) in resources:
                require(_read_source(resources[*S3D, tile + zoom])[0] == _read_source(source)[0],
                        'Canonical zoom geometry differs from its common saved shadow source')
        if not row['cast_shadow']:
            require(not _read_source(source)[0],
                    'Ground-only shadow declaration hides above-ground referenced geometry')
            ground_only += 1
            continue
        needed = {(*S3D, iid) for iid in row['model_ids']} | {
            (*TEXTURE, iid) for iid in row['texture_ids']}
        require(needed <= resources.keys(), 'Saved shadow geometry is missing a card model or alpha mask')
        models = tuple(resources[*S3D, iid] for iid in row['model_ids'])
        textures = tuple(resources[*TEXTURE, iid] for iid in row['texture_ids'])
        reports.append({'cell': row['cell'], **_check_host(source, models, textures)})
    return {'model_shadow_geometry': {'hosts_checked': len(reports),
            'ground_only_hosts_checked': ground_only, 'hosts': reports,
            'binary_mask_edge_tolerance_texture_pixels': 1,
            'metres_per_texture_pixel': METRES_PER_PIXEL,
            'proper_rotations_checked': 4, 'camera_rotations_checked': 4,
            'ground_clipping_checked': True, 'tile_clipping': False,
            'material_texture_alpha_sampled': False,
            'limits': ['Opaque selected source materials only; original atlas coverage is a separate dependency audit.',
                       'Four proper object rotations and four camera rotations; mirrored placements are outside this contract.',
                       'Instruction-derived native projection and saved resources; no live game, lifecycle, or terrain-render pass.'],
            'in_game_tested': False}}
