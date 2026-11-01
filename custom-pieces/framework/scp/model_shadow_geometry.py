"""Build four camera-relative, invisible single-mesh shadow carriers.

The caller supplies the actual opaque triangles of one physical model, with
any deliberate ground-only filtering already applied. Nothing is clipped to
a network tile, or borrowed from neighbouring components. The native default
sun is fixed to the screen, so each object/camera relative pose needs its own
projected silhouette. Native RKT2 selection chooses (object-camera-1) modulo
four, while the shadow pass rotates the selected model by camera+1 turns.

Each silhouette is carried by one slanted, affine-UV quadrilateral. Its four
vertices have a real height range, but its primitive list draws no geometry.
The native shadow pass uses vertex positions and UVs rather than the draw
indices. This module implements the geometric/container contract; a successful
build does not establish native loading, lifecycle, or in-game shadow output.
"""
from __future__ import annotations

import hashlib
import math
import struct
from collections.abc import Sequence

from PIL import Image, ImageDraw

from .models import pack_s3d, parse_s3d, positions, validate_s3d


# The native lighting reader stores these values as Float32 after applying
# its Float32 degrees-to-radians factor to azimuth 67.5 and elevation 45.
DEFAULT_SUN = (0.6532814502716064, -0.7071067690849304,
               -0.27059805393218994)
LOCAL_SUN = (-0.27059805393218994, -0.7071067690849304,
             -0.6532814502716064)
SUPPORTED_TEXTURE_SIZES = (8, 16, 32, 64, 128, 256, 512)
PACKED_POSITION_UV = 0x80004001


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def rotate_y(point, quarter_turns):
    """Rotate by R1(x,y,z)=(-z,y,x), using exact quarter turns."""
    x, y, z = point
    for _ in range(quarter_turns % 4):
        x, z = -z, x
    return x, y, z


def project_to_ground(point, sun=LOCAL_SUN):
    """Intersect the sun ray through a point with the local y=0 plane."""
    x, y, z = point
    _require(len(sun) == 3 and all(math.isfinite(v) for v in sun)
             and sun[1] < 0, 'Shadow sun must be a finite downward vector')
    return x - y * sun[0] / sun[1], z - y * sun[2] / sun[1]


def referenced_model_triangles(model_raw):
    """Return all referenced, nondegenerate, static S3D triangles.

    Materials are not sampled for texture alpha. The caller must establish
    that treating the selected geometry as opaque is appropriate. Ground and
    vertical triangles are both retained; ground filtering belongs to the
    caller. Unreferenced vertices and unused index ranges do not contribute.
    """
    model = parse_s3d(model_raw)
    validate_s3d(model)
    _require(struct.unpack_from('<H', model['anim_header'])[0] == 1,
             'Shadow carriers require a static, single-frame source model')
    for name, raw in model['trailing']:
        _require(name in (b'PROP', b'REGP') and len(raw) == 12
                 and raw[8:] == b'\0' * 4,
                 'Shadow carriers cannot ignore source model transforms')
    result, seen = [], set()
    for mesh in model['meshes']:
        vi, ii, pi, _ = mesh['frames'][0]
        if (vi, ii, pi) in seen:
            continue
        seen.add((vi, ii, pi))
        points = positions(model['vertices'][vi])
        indices = model['indices'][ii]['values']
        for kind, first, count in model['primitives'][pi]:
            _require(kind == 0 and count % 3 == 0,
                     'Shadow source requires triangular primitives')
            for start in range(first, first + count, 3):
                triangle = tuple(points[i] for i in indices[start:start + 3])
                if _triangle_area_3d(triangle) > 1e-12:
                    result.append(triangle)
    return result


def _triangle_area_3d(triangle):
    a, b, c = triangle
    u = tuple(b[i] - a[i] for i in range(3))
    v = tuple(c[i] - a[i] for i in range(3))
    cross = tuple(u[(i + 1) % 3] * v[(i + 2) % 3]
                  - u[(i + 2) % 3] * v[(i + 1) % 3]
                  for i in range(3))
    return math.sqrt(sum(value * value for value in cross)) / 2


def _source_triangles(triangles):
    result = []
    for triangle in triangles:
        _require(len(triangle) == 3 and all(len(p) == 3 for p in triangle),
                 'A shadow triangle must contain three 3D points')
        points = tuple(tuple(float(value) for value in p) for p in triangle)
        _require(all(math.isfinite(v) for p in points for v in p),
                 'Shadow triangle coordinates must be finite')
        _require(_triangle_area_3d(points) > 1e-12,
                 'Shadow triangle has zero 3D area')
        result.append(points)
    _require(result, 'Shadow carriers require nonempty opaque geometry')
    return result


def encode_mask_fsh(mask):
    """Encode an ordinary texture-group BGRA mask, without tile projection."""
    _require(mask.mode == 'L' and mask.width == mask.height
             and mask.width in SUPPORTED_TEXTURE_SIZES,
             'Shadow mask must be a supported square power-of-two L image')
    # Transparent white matches the native shadow convention. Covered pixels
    # are black, with fractional geometric coverage in alpha.
    pixels = bytearray()
    for coverage in mask.tobytes():
        pixels.extend((0, 0, 0, coverage) if coverage else (255, 255, 255, 0))
    block_size = 16 + len(pixels)
    return (struct.pack('<4sII4s4sI', b'SHPI', 24 + block_size, 1,
                        b'GIMX', b'0000', 24)
            + struct.pack('<I6H', (block_size << 8) | 0x7D,
                          mask.width, mask.height, 0, 0, 0, 0) + pixels)


def _mask(projected, *, metres_per_pixel, maximum_texture_size, supersample):
    points = [point for triangle in projected for point in triangle]
    low = [min(p[axis] for p in points) for axis in range(2)]
    high = [max(p[axis] for p in points) for axis in range(2)]
    extent = max(high[axis] - low[axis] for axis in range(2))
    _require(extent > 1e-9, 'Projected shadow has zero extent')
    # A two-pixel transparent border prevents the actual footprint from
    # touching a clamped texture edge. One metric pitch is shared by both
    # axes; a narrow shadow retains its real width inside a square bitmap.
    size = next((size for size in SUPPORTED_TEXTURE_SIZES
                 if size <= maximum_texture_size
                 and extent / metres_per_pixel + 4 <= size), None)
    _require(size is not None,
             'Projected shadow exceeds the texture budget at requested resolution')
    pitch = metres_per_pixel
    span = size * pitch
    center = [(low[i] + high[i]) / 2 for i in range(2)]
    bounds = [(center[i] - span / 2, center[i] + span / 2) for i in range(2)]
    image = Image.new('L', (size * supersample, size * supersample))
    draw = ImageDraw.Draw(image)
    represented, edge_on = [], []
    for index, triangle in enumerate(projected):
        a, b, c = triangle
        twice_area = ((b[0] - a[0]) * (c[1] - a[1])
                      - (b[1] - a[1]) * (c[0] - a[0]))
        if abs(twice_area) <= 1e-12:
            edge_on.append(index)
            continue
        represented.append(index)
        draw.polygon([((p[0] - bounds[0][0]) / pitch * supersample,
                       (p[1] - bounds[1][0]) / pitch * supersample)
                      for p in triangle], fill=255)
    _require(represented, 'All source triangles are edge-on to this shadow pose')
    mask = image.resize((size, size), Image.Resampling.BOX)
    _require(mask.getbbox() is not None, 'Opaque source shadow rasterized empty')
    return mask, bounds, represented, edge_on


def _carrier_model(bounds, texture_id, height, draw_mode):
    x0, x1 = bounds[0]
    z0, z1 = bounds[1]
    targets = ((x0, z0), (x1, z0), (x1, z1), (x0, z1))
    uv = ((0., 0.), (1., 0.), (1., 1.), (0., 1.))
    points = []
    for (x, z), y in zip(targets, (0., height, height, 0.)):
        points.append((x + y * LOCAL_SUN[0] / LOCAL_SUN[1], y,
                       z + y * LOCAL_SUN[2] / LOCAL_SUN[1]))
    data = b''.join(struct.pack('<5f', *point, *pair)
                    for point, pair in zip(points, uv))
    name = b'SCP opaque shadow mask\0'
    material = (struct.pack('<IBBBBHIBB', 0xA3, 4, 3, 1, 0, 0, 0, 0, 1)
                + struct.pack('<IBBBBHHB', texture_id, 2, 2, 1, 1,
                              0, 0, len(name)) + name)
    primitives = [] if draw_mode == 'empty-primitives' else [(0, 0, 3)]
    model = {'version': (1, 5),
             'vertices': [{'flags': 0, 'format': PACKED_POSITION_UV,
                           'stride': 20, 'data': data}],
             'indices': [{'flags': 0, 'stride': 2, 'values': (0, 0, 0)}],
             'primitives': [primitives],
             'materials': [{'raw': material, 'textures': [texture_id]}],
             'anim_header': struct.pack('<H', 1) + b'\0' * 12,
             'meshes': [{'name': b'SCP invisible shadow carrier\0',
                         'flags': 0, 'frames': [(0, 0, 0, 0)]}],
             'trailing': [(tag, tag + struct.pack('<II', 12, 0))
                          for tag in (b'PROP', b'REGP')]}
    raw = pack_s3d(model)
    parsed = parse_s3d(raw)
    audit = validate_s3d(parsed)
    stored = positions(parsed['vertices'][0])
    projected = [project_to_ground(p) for p in stored]
    residual = max(abs(actual[i] - target[i])
                   for actual, target in zip(projected, targets)
                   for i in range(2))
    _require(residual <= 1e-4,
             'Float32 shadow card loses the required geometric precision')
    return raw, {'quad_xyz_m': stored, 'quad_uv': list(uv),
                 'target_quad_xz_m': list(targets),
                 'maximum_float32_projection_error_m': residual,
                 'draw_area_m2': 0.0, 'model_validation': audit}


def generate_shadow_carriers(triangles, texture_ids, *, metres_per_pixel=.125,
                             maximum_texture_size=512, supersample=4,
                             card_height_m=64., draw_mode='empty-primitives'):
    """Return four S3Ds, four ordinary FSHs, and source/geometry evidence.

    ``models[j]`` binds to ``textures[texture_ids[j]]``. Register those four
    model IDs in the four RKT2 rotation slots, repeated for all five zooms.
    The prop must omit the full-geometry rotation property E83A081D. Resource
    allocation, prop/T21 construction, material opacity, native height culling,
    and actual game validation remain the caller's explicit responsibilities.
    The 64-metre proxy height keeps the invisible carrier above the native
    Medium and High shadow height gates at all five zooms; it is not a change
    to the source deck height, and the compensating slant preserves the exact
    projected footprint.
    """
    _require(isinstance(texture_ids, Sequence) and len(texture_ids) == 4
             and len(set(texture_ids)) == 4
             and all(type(iid) is int and 0 < iid <= 0xFFFFFFFF
                     for iid in texture_ids),
             'Exactly four distinct allocated texture IDs are required')
    _require(math.isfinite(metres_per_pixel) and metres_per_pixel > 0,
             'Shadow metres per pixel must be positive and finite')
    _require(maximum_texture_size in SUPPORTED_TEXTURE_SIZES,
             'Unsupported maximum shadow texture size')
    _require(type(supersample) is int and 1 <= supersample <= 8,
             'Shadow supersampling must be an integer from 1 through 8')
    _require(math.isfinite(card_height_m) and 0 < card_height_m <= 512,
             'Shadow card height must be positive and at most 512 metres')
    _require(draw_mode in ('empty-primitives', 'degenerate-triangle'),
             'Shadow carrier draw mode must remain invisible')
    source = _source_triangles(triangles)
    models, textures, variants = [], {}, []
    for pose, texture_id in enumerate(texture_ids):
        projected = [tuple(project_to_ground(rotate_y(p, pose)) for p in tri)
                     for tri in source]
        mask, bounds, represented, edge_on = _mask(
            projected, metres_per_pixel=metres_per_pixel,
            maximum_texture_size=maximum_texture_size, supersample=supersample)
        model, witness = _carrier_model(bounds, texture_id, card_height_m, draw_mode)
        texture = encode_mask_fsh(mask)
        models.append(model)
        textures[texture_id] = texture
        variants.append({'relative_pose': pose, 'texture_id': f'{texture_id:08x}',
                         'mask_size': mask.width, 'pixel_pitch_m': metres_per_pixel,
                         'projected_bounds_xz_m': bounds,
                         'source_triangle_indices': represented,
                         'edge_on_triangle_indices': edge_on,
                         'mask_sha256': hashlib.sha256(mask.tobytes()).hexdigest(),
                         'texture_sha256': hashlib.sha256(texture).hexdigest(),
                         'model_sha256': hashlib.sha256(model).hexdigest(),
                         **witness})
    source_bounds = [[min(p[i] for tri in source for p in tri),
                      max(p[i] for tri in source for p in tri)] for i in range(3)]
    return {'models': tuple(models), 'textures': textures,
            'report': {'source_triangle_count': len(source),
                       'source_bounds_xyz_m': source_bounds,
                       'default_sun': list(DEFAULT_SUN), 'local_sun': list(LOCAL_SUN),
                       'variant_selection': '(object_rotation-camera_rotation-1)%4',
                       'native_model_rotation': '(camera_rotation+1)%4',
                       'card_height_m': card_height_m, 'draw_mode': draw_mode,
                       'card_height_is_shadow_proxy_only': True,
                       'tile_clipping': False, 'opaque_geometry_assumption': True,
                       'texture_alpha_sampled': False, 'supersample': supersample,
                       'variants': variants, 'in_game_tested': False}}
