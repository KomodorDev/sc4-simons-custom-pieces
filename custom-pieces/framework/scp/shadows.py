"""Create new, geometry-derived shadow artwork for SCP network tiles.

This is a deliberately explicit artwork convention, not a reproduction of the
native NAM shadow author's projection. A network tile is 16 x 16 metres, with
model coordinates X/Z in [-8, 8]. We project referenced, opaque triangles
vertically onto that square: +X goes right and +Z goes down. Height does not
shift the silhouette. No light direction, rotation, or mirror is baked in;
NetworkINI/the game applies the selected tile orientation separately.

Each image is new code-authored artwork. Native pixel calibration and actual
in-game shadow selection have NOT been tested. Native HSR shadows have a
different width from a literal 16 m projection of their S3D deck, so byte/pixel
equivalence to those hand-authored masks would be an incorrect claim.

The container *is* based on the installed NAM 50 shadow resources: SHPI/GIMX,
one ``0000`` image, format 0x7D (uncompressed 32-bit BGRA), no palette/mipmaps,
and five square zoom sizes 8, 16, 32, 64, 128. The bitmap block length occupies
the upper 24 bits of its little-endian first word. See the native FSH codec in
setup/plop-and-paint-native/source/vendor/DBPFKit/src/FSHStructures.h and the
audited 7AB50E44-2BC2759A-5DD31500..04 resources in High Speed Rail.dat.

The rasterizer intentionally supports static opaque geometry only. Empty
PROP/REGP chunks are accepted; unknown model transforms are rejected rather
than silently ignored. Material textures are not sampled for alpha cut-outs.
"""

from __future__ import annotations

import hashlib
import math
import struct
import zlib
from functools import lru_cache

from PIL import Image, ImageDraw

from .models import parse_s3d, positions, validate_s3d


SHADOW = (0x7AB50E44, 0x2BC2759A)
S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
ZOOM_SIZES = (8, 16, 32, 64, 128)
TILE_METRES = 16.0
SUPERSAMPLE = 8
PROJECTION = 'vertical; X/Z [-8,8] metres; +X right; +Z down; no height offset'


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _number(value: str | int) -> int:
    return int(value, 16) if isinstance(value, str) else value


def encode_shadow_fsh(alpha: Image.Image) -> bytes:
    """Encode one square coverage mask in the audited native BGRA container.

    Zero coverage uses transparent white, as in the native shadow. Any covered
    pixel is black with its coverage stored in alpha. No palette is present.
    """
    _require(alpha.mode == 'L', 'Shadow coverage must be a Pillow L image')
    width, height = alpha.size
    _require(width == height and width in ZOOM_SIZES, 'Unsupported shadow dimensions')
    pixels = bytearray()
    for coverage in alpha.tobytes():
        pixels.extend((0, 0, 0, coverage) if coverage else (255, 255, 255, 0))
    block_size = 16 + len(pixels)
    header = struct.pack('<4sII4s4sI', b'SHPI', 24 + block_size, 1,
                         b'GIMX', b'0000', 24)
    bitmap = struct.pack('<I6H', (block_size << 8) | 0x7D,
                         width, height, 0, 0, 0, 0)
    return header + bitmap + pixels


def decode_shadow_fsh(raw: bytes) -> Image.Image:
    """Strictly decode the one-image native shadow layout to an RGBA image.

    This accepts native RGB edge noise; semantic validation of newly generated
    artwork additionally requires the canonical black/transparent-white pixels.
    """
    _require(len(raw) >= 40, 'Truncated shadow FSH')
    magic, total, count, directory, name, offset = struct.unpack_from('<4sII4s4sI', raw)
    _require(magic == b'SHPI', 'Missing shadow SHPI signature')
    _require(total == len(raw), 'Shadow FSH total length mismatch')
    _require(count == 1 and directory == b'GIMX' and name == b'0000',
             'Unsupported shadow directory')
    _require(offset == 24, 'Shadow bitmap offset must be 24')
    code_size, width, height, cx, cy, ox, oy = struct.unpack_from('<I6H', raw, offset)
    _require(code_size & 255 == 0x7D, 'Shadow FSH must use 32-bit BGRA format 0x7D')
    _require(width == height and width in ZOOM_SIZES, 'Unsupported shadow dimensions')
    _require((cx, cy, ox, oy) == (0, 0, 0, 0), 'Unexpected shadow offsets or mipmaps')
    expected_size = 16 + width * height * 4
    _require(code_size >> 8 == expected_size, 'Shadow bitmap block length mismatch')
    _require(offset + expected_size == len(raw), 'Shadow bitmap pixels or attachments mismatch')
    return Image.frombytes('RGBA', (width, height), raw[40:], 'raw', 'BGRA')


def _triangles(modelraw: bytes) -> tuple[list[tuple], dict]:
    model = parse_s3d(modelraw)
    audit = validate_s3d(model)
    _require(struct.unpack_from('<H', model['anim_header'])[0] == 1,
             'Shadow artwork requires a static, single-frame S3D')
    for name, raw in model['trailing']:
        _require(name in (b'PROP', b'REGP') and len(raw) == 12 and raw[8:] == b'\0' * 4,
                 'Shadow artwork cannot ignore nonempty/unknown model transforms')
    triangles, seen = [], set()
    for mesh in model['meshes']:
        vi, ii, pi, _ = mesh['frames'][0]
        if (vi, ii, pi) in seen:
            continue
        seen.add((vi, ii, pi))
        vertices = positions(model['vertices'][vi])
        indices = model['indices'][ii]['values']
        for kind, first, count in model['primitives'][pi]:
            for start in range(first, first + count, 3):
                triangle = tuple(vertices[index] for index in indices[start:start + 3])
                # A vertical side projects to a line, which has zero coverage.
                a, b, c = triangle
                area = ((b[0] - a[0]) * (c[2] - a[2]) -
                        (b[2] - a[2]) * (c[0] - a[0]))
                if abs(area) > 1e-12:
                    triangles.append(triangle)
    _require(triangles, 'S3D has no nonzero-area horizontal shadow silhouette')
    return triangles, audit


def _clip_polygon(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Clip in world metres first, so off-tile coordinates cannot overflow PIL."""
    for axis, edge, keep_greater in ((0, -8., True), (0, 8., False),
                                     (1, -8., True), (1, 8., False)):
        if not points:
            break
        clipped = []
        prior = points[-1]
        prior_inside = prior[axis] >= edge if keep_greater else prior[axis] <= edge
        for current in points:
            current_inside = current[axis] >= edge if keep_greater else current[axis] <= edge
            if current_inside != prior_inside:
                fraction = (edge - prior[axis]) / (current[axis] - prior[axis])
                crossing = tuple(prior[n] + fraction * (current[n] - prior[n]) for n in (0, 1))
                clipped.append(crossing)
            if current_inside:
                clipped.append(current)
            prior, prior_inside = current, current_inside
        points = clipped
    return points


def _rasterize(triangles: list[tuple], size: int) -> Image.Image:
    _require(size in ZOOM_SIZES, 'Unsupported shadow zoom size')
    side = size * SUPERSAMPLE
    canvas = Image.new('L', (side, side), 0)
    draw = ImageDraw.Draw(canvas)
    for triangle in triangles:
        polygon = _clip_polygon([(point[0], point[2]) for point in triangle])
        if len(polygon) < 3:
            continue
        pixels = [((x + 8.) * side / TILE_METRES,
                   (z + 8.) * side / TILE_METRES) for x, z in polygon]
        # Draw centre-sampled scanline spans ourselves. ImageDraw.polygon
        # includes both endpoints of an integer edge, which widens an exact
        # four-metre rectangle by one high-resolution pixel. Half-open spans
        # keep a centred, grid-aligned deck at its actual world width.
        first_y = max(0, math.ceil(min(y for x, y in pixels) - .5))
        stop_y = min(side, math.ceil(max(y for x, y in pixels) - .5))
        for row in range(first_y, stop_y):
            sample_y, crossings = row + .5, []
            prior = pixels[-1]
            for current in pixels:
                if ((prior[1] <= sample_y < current[1]) or
                        (current[1] <= sample_y < prior[1])):
                    fraction = (sample_y - prior[1]) / (current[1] - prior[1])
                    crossings.append(prior[0] + fraction * (current[0] - prior[0]))
                prior = current
            if len(crossings) >= 2:
                left = max(0, math.ceil(min(crossings) - .5))
                right = min(side, math.ceil(max(crossings) - .5)) - 1
                if left <= right:
                    draw.line((left, row, right, row), fill=255)
    # BOX area reduction gives bounded coverage with no ringing outside the
    # silhouette. Eight samples per axis provide 1/64-pixel coverage steps.
    return canvas.resize((size, size), Image.Resampling.BOX)


def rasterize_shadow(modelraw: bytes, size: int) -> Image.Image:
    """Return a coverage mask for actual referenced geometry, clipped to one tile."""
    return _rasterize(_triangles(modelraw)[0], size)


@lru_cache(maxsize=12288)
def _compressed_shadow_set(modelraw: bytes) -> tuple[bytes, ...]:
    """Retain exact FSH results compressed, keyed by complete model bytes.

    Builds and repeated verification inspect the same models many times.
    Changed model bytes get a different key; shadow bytes are still compared
    independently on every verification. Mutable Pillow images are not cached.
    The bounded compressed cache fits the full catalog without retaining its
    approximately 0.8 GB of uncompressed five-zoom shadow images.
    """
    triangles, _ = _triangles(modelraw)
    return tuple(zlib.compress(encode_shadow_fsh(_rasterize(triangles, size)))
                 for size in ZOOM_SIZES)


@lru_cache(maxsize=256)
def _shadow_set(modelraw: bytes) -> tuple[bytes, ...]:
    """Restore exact bytes, retaining only a small hot uncompressed set.

    The five zoom checks commonly reuse one model. This small cache avoids
    repeated decompression within that check; eviction never rerasterizes a
    model still present in the larger immutable compressed cache.
    """
    return tuple(zlib.decompress(raw) for raw in _compressed_shadow_set(modelraw))


def build_shadows(modelraw: bytes, tile: str | int) -> dict[tuple[int, int, int], bytes]:
    """Return the five new SHADOW FSH resources for one model's tile ID.

    ``tile`` is the unrotated S3D base instance ID and must reserve low nibble
    zero. The function does not create a NetworkINI remapping entry; the caller
    registers this same tile as shadow source with rotation=0 and flip=0.
    """
    tile = _number(tile)
    _require(0 <= tile <= 0xFFFFFFF0 and tile & 15 == 0,
             'Shadow tile ID must be a 32-bit instance with a zero low nibble')
    return {(*SHADOW, tile + zoom): raw for zoom, raw in enumerate(_shadow_set(modelraw))}


def validate_piece_shadows(resources: dict, piece: dict) -> dict:
    """Validate actual FSH closure and compare each image to its actual S3D.

    This verifies our documented artwork recipe, not the game's projection or
    renderer. All five S3D zoom resources must be supplied; silently falling
    back to another zoom could hide a stale shadow on a simplified model.
    """
    tiles = list(map(_number, piece['tile_ids']))
    _require(len(tiles) == len(set(tiles)) and tiles, 'Duplicate or missing shadow tile IDs')
    expected = {(*SHADOW, tile + zoom) for tile in tiles for zoom in range(5)}
    actual = {key for key in resources if key[:2] == SHADOW}
    _require(actual == expected, 'Custom shadow resource closure differs from piece tiles')
    images, subpixel_structural = [], []
    for tile_index, tile in enumerate(tiles):
        tile_images, model_bytes, empty_zooms = [], [], []
        for zoom, size in enumerate(ZOOM_SIZES):
            key, modelkey = (*SHADOW, tile + zoom), (*S3D, tile + zoom)
            _require(modelkey in resources, f'Missing shadow source S3D {tile + zoom:08x}')
            raw = resources[key]
            decoded = decode_shadow_fsh(raw)
            _require(decoded.size == (size, size), f'Wrong shadow zoom dimensions {tile + zoom:08x}')
            expected_raw = _shadow_set(resources[modelkey])[zoom]
            _require(raw == expected_raw, f'Shadow silhouette differs from actual S3D {tile + zoom:08x}')
            mask = decoded.getchannel('A')
            bbox = mask.getbbox()
            if bbox is None:
                empty_zooms.append(zoom)
            model_bytes.append(resources[modelkey])
            tile_images.append({'instance': f'{tile + zoom:08x}', 'width': size, 'height': size,
                                'alpha_bbox': list(bbox) if bbox is not None else None,
                                'coverage_pixels': sum(mask.tobytes()) / 255.,
                                'sha256': hashlib.sha256(raw).hexdigest()})
        if empty_zooms:
            # A genuine, very small structural sliver can miss the coarse
            # centre-sampling lattice. Do not invent shadow pixels or accept
            # an empty traffic tile. This exception is verified from the
            # saved PATH/model/FSH resources, not just a manifest assertion.
            cells, structural = piece.get('cells'), piece.get('structural_cells')
            _require(isinstance(cells, list) and len(cells) == len(tiles) and
                     all(isinstance(cell, (list, tuple)) and len(cell) == 2 and
                         all(type(value) is int for value in cell) for cell in cells) and
                     isinstance(structural, list) and
                     all(isinstance(cell, (list, tuple)) and len(cell) == 2 and
                         all(type(value) is int for value in cell) for cell in structural) and
                     tuple(cells[tile_index]) in {tuple(cell) for cell in structural},
                     f'Empty custom shadow {tile:08x} is not a declared structural cell')
            path_key = (*PATH, tile)
            _require(path_key in resources,
                     f'Empty custom shadow {tile:08x} lacks its structural PATH resource')
            lines = tuple(line.strip() for line in resources[path_key].decode('ascii').splitlines()
                          if line.strip())
            _require(lines == ('SC4PATHS', '1.2', '0', '0', '0'),
                     f'Empty custom shadow {tile:08x} does not have the exact empty structural PATH header')
            _require(all(raw == model_bytes[0] for raw in model_bytes[1:]),
                     f'Empty structural shadow {tile:08x} requires identical S3D geometry at all five zooms')
            _require(tile_images[-1]['alpha_bbox'] is not None,
                     f'Empty structural shadow {tile:08x} is still empty at the highest zoom')
            first_visible = next(zoom for zoom, item in enumerate(tile_images)
                                 if item['alpha_bbox'] is not None)
            _require(empty_zooms == list(range(first_visible)),
                     f'Empty structural shadow {tile:08x} must occur only at leading coarser zooms')
            subpixel_structural.append({
                'tile': f'{tile:08x}', 'cell': list(cells[tile_index]),
                'empty_zoom_indices': empty_zooms,
                'first_visible_zoom_index': first_visible,
                'first_visible_width': ZOOM_SIZES[first_visible],
                'identical_source_model_sha256': hashlib.sha256(model_bytes[0]).hexdigest(),
                'reason': 'Actual structural geometry has zero quantized coverage at leading coarse zooms',
            })
            for zoom in empty_zooms:
                tile_images[zoom]['subpixel_structural_coverage'] = True
        images.extend(tile_images)
    return {'artwork': 'new code-authored vertical triangle silhouettes',
            'projection': PROJECTION, 'tile_metres': TILE_METRES,
            'supersample_per_axis': SUPERSAMPLE,
            'all_five_zoom_resources_valid': True,
            'silhouettes_match_actual_s3d_geometry': True,
            'native_projection_calibrated': False,
            'texture_alpha_cutouts_sampled': False,
            'in_game_shadow_selection_tested': False,
            'subpixel_structural_zooms': subpixel_structural,
            'images': images}
