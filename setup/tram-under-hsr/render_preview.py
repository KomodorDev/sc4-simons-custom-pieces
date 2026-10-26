"""Render the staged S3D triangles with their installed NAM material textures.

This is an orthographic software rendering of the actual DAT model, not a
SimCity 4 screenshot. No geometry is invented and no AI image generation is
used. Only the final PNG is written. Requires Pillow and NumPy.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import struct
import sys

sys.dont_write_bytecode = True
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'cam-install/runtime-audit'))
import read_dbpf
from model_tools import parse_s3d


def decode_fsh(blob: bytes) -> Image.Image:
    """Decode the first image of the NAM FSH texture resource."""
    data = read_dbpf.decompress(blob)
    if data[:4] != b'SHPI':
        raise ValueError('Texture is not an FSH resource')
    count, = struct.unpack_from('<I', data, 8)
    if count < 1:
        raise ValueError('FSH resource has no images')
    offset, = struct.unpack_from('<I', data, 20)
    code, width, height = struct.unpack_from('<IHH', data, offset)
    kind = code & 0xff
    pixels = data[offset + 16:]
    if kind == 0x60:
        length = ((width + 3) // 4) * ((height + 3) // 4) * 8
        return Image.frombytes('RGBA', (width, height), pixels[:length], 'bcn', (1, 'DXT1'))
    if kind == 0x61:
        length = ((width + 3) // 4) * ((height + 3) // 4) * 16
        return Image.frombytes('RGBA', (width, height), pixels[:length], 'bcn', (2, 'DXT3'))
    if kind == 0x7d:
        return Image.frombytes('RGBA', (width, height), pixels[:width * height * 4], 'raw', 'BGRA')
    if kind == 0x7f:
        return Image.frombytes('RGB', (width, height), pixels[:width * height * 3], 'raw', 'BGR').convert('RGBA')
    raise ValueError(f'Unsupported FSH image encoding {kind:02x}')


def textures_from_manifest(manifest: dict) -> dict:
    result = {}
    # Prefer the HSR texture archive to the earlier common Monorail atlas.
    for instance in ('580cc704', '0bf6e09b'):
        record = next(item for item in manifest['texture_dependencies'][instance]
                      if item['tgi'].split('-')[1] == '1abe787d')
        archive = Path(record['files'][-1])
        resources = read_dbpf.entries(archive.read_bytes())
        tgi = tuple(int(value, 16) for value in record['tgi'].split('-'))
        result[int(instance, 16)] = np.asarray(decode_fsh(resources[tgi]), dtype=float) / 255
    return result


def model_triangles(model: dict):
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        vb = model['vertices'][vi]
        vertices = np.array([struct.unpack_from('<5f', vb['data'], offset)
                             for offset in range(0, len(vb['data']), vb['stride'])])
        indices = np.array(model['indices'][ii]['values'])
        texture = model['materials'][mi]['textures'][0]
        for kind, first, length in model['primitives'][pi]:
            if kind != 0:
                raise ValueError('Preview supports triangle lists only')
            for tri in indices[first:first + length].reshape(-1, 3):
                yield vertices[tri, :3], vertices[tri, 3:], texture


def render_view(model: dict, textures: dict, azimuth: float, elevation: float,
                width: int, height: int) -> Image.Image:
    az, el = map(math.radians, (azimuth, elevation))
    right = np.array([math.cos(az), 0, -math.sin(az)])
    up = np.array([-math.sin(az) * math.sin(el), math.cos(el), -math.cos(az) * math.sin(el)])
    towards = np.array([math.sin(az) * math.cos(el), math.sin(el), math.cos(az) * math.cos(el)])
    triangles = list(model_triangles(model))
    all_positions = np.concatenate([position for position, uv, tex in triangles])
    projected = np.column_stack((all_positions @ right, all_positions @ up))
    low, high = projected.min(axis=0), projected.max(axis=0)
    scale = min((width - 80) / (high[0] - low[0]), (height - 80) / (high[1] - low[1]))
    center = (low + high) / 2
    background = np.array([247, 249, 251], float) / 255
    rgb = np.broadcast_to(background, (height, width, 3)).copy()
    depth = np.full((height, width), -np.inf)
    light = np.array([-0.4, 0.9, 0.2]); light /= np.linalg.norm(light)

    for position, uv, texture_id in triangles:
        projected = np.column_stack((position @ right, position @ up))
        screen = (projected - center) * [scale, -scale] + [width / 2, height / 2]
        z = position @ towards
        x0, y0 = np.maximum(np.floor(screen.min(axis=0)).astype(int), [0, 0])
        x1, y1 = np.minimum(np.ceil(screen.max(axis=0)).astype(int), [width - 1, height - 1])
        if x1 < x0 or y1 < y0:
            continue
        yy, xx = np.mgrid[y0:y1 + 1, x0:x1 + 1]
        xx, yy = xx + .5, yy + .5
        a, b, c = screen
        denominator = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
        if abs(denominator) < 1e-8:
            continue
        w0 = ((b[1] - c[1]) * (xx - c[0]) + (c[0] - b[0]) * (yy - c[1])) / denominator
        w1 = ((c[1] - a[1]) * (xx - c[0]) + (a[0] - c[0]) * (yy - c[1])) / denominator
        w2 = 1 - w0 - w1
        inside = (w0 >= -1e-8) & (w1 >= -1e-8) & (w2 >= -1e-8)
        pixel_depth = w0 * z[0] + w1 * z[1] + w2 * z[2]
        local_depth = depth[y0:y1 + 1, x0:x1 + 1]
        visible = inside & (pixel_depth > local_depth)
        coords = w0[..., None] * uv[0] + w1[..., None] * uv[1] + w2[..., None] * uv[2]
        texture = textures[texture_id]
        # S3D's repeat wrapping handles the HSR donor's V range of -1 to 0.
        tu = np.mod(coords[..., 0], 1) * texture.shape[1] - .5
        tv = np.mod(coords[..., 1], 1) * texture.shape[0] - .5
        u0, v0 = np.floor(tu).astype(int), np.floor(tv).astype(int)
        fu, fv = (tu - u0)[..., None], (tv - v0)[..., None]
        t00 = texture[v0 % texture.shape[0], u0 % texture.shape[1]]
        t10 = texture[v0 % texture.shape[0], (u0 + 1) % texture.shape[1]]
        t01 = texture[(v0 + 1) % texture.shape[0], u0 % texture.shape[1]]
        t11 = texture[(v0 + 1) % texture.shape[0], (u0 + 1) % texture.shape[1]]
        sampled = (t00 * (1 - fu) + t10 * fu) * (1 - fv) + (t01 * (1 - fu) + t11 * fu) * fv
        visible &= sampled[..., 3] > .5
        normal = np.cross(position[1] - position[0], position[2] - position[0])
        normal /= np.linalg.norm(normal)
        shade = .78 + .22 * abs(normal @ light)
        color = np.clip(sampled[..., :3] * shade, 0, 1)
        local_rgb = rgb[y0:y1 + 1, x0:x1 + 1]
        local_rgb[visible] = color[visible]
        local_depth[visible] = pixel_depth[visible]
    return Image.fromarray(np.uint8(np.clip(rgb * 255, 0, 255)), 'RGB')


def font(size: int, bold: bool = False):
    candidates = ([Path('/System/Library/Fonts/Supplemental/Arial Bold.ttf')] if bold else
                  [Path('/System/Library/Fonts/Supplemental/Arial.ttf')])
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def main():
    manifest = json.loads((HERE / 'dist/build-manifest.json').read_text())
    archive = read_dbpf.entries(Path(manifest['output']).read_bytes())
    model = parse_s3d(read_dbpf.decompress(archive[0x5ad0e817, 0xbadb57f1, 0x5dd0f104]))
    textures = textures_from_manifest(manifest)
    # Supersampling makes the real low-resolution NAM textures readable without
    # changing the model. There is no composited or generated scenery.
    supersample = 2
    views = [render_view(model, textures, 45, math.degrees(math.atan(1 / math.sqrt(2))),
                         720 * supersample, 610 * supersample),
             render_view(model, textures, 138, 17, 720 * supersample, 610 * supersample)]
    views = [view.resize((720, 610), Image.Resampling.LANCZOS) for view in views]
    canvas = Image.new('RGB', (1560, 900), '#f7f9fb')
    draw = ImageDraw.Draw(canvas)
    dark, muted, blue = '#172b42', '#586a7e', '#176eaf'
    draw.text((62, 42), 'Tram beneath High Speed Rail', fill=dark, font=font(38, True))
    draw.text((64, 96), 'Actual staged model and NAM textures · one 16 × 16 metre crossing tile',
              fill=muted, font=font(20))
    for x, view in ((30, views[0]), (810, views[1])):
        canvas.paste(view, (x, 162))
    draw.text((64, 151), 'ISOMETRIC VIEW', fill=blue, font=font(16, True))
    draw.text((844, 151), 'LOW VIEW FROM THE OTHER SIDE', fill=blue, font=font(16, True))
    draw.line((780, 185, 780, 765), fill='#dce3eb', width=1)
    draw.text((64, 777), 'Upper: HSR deck at its original height', fill=dark, font=font(22, True))
    draw.text((64, 813), 'Lower: ground tram crosses at 90° · no pillar in the crossing tile',
              fill=muted, font=font(20))
    draw.text((64, 858), 'Model preview, not a game screenshot. Placement, lighting and traffic still require an in-game test.',
              fill=muted, font=font(17))
    destination = HERE / 'dist/model-preview.png'
    canvas.save(destination)
    print(destination)


if __name__ == '__main__':
    main()
