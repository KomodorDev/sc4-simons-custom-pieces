"""Render the packaged HSR / diagonal GHSR crossing with real NAM textures.

This is a software rendering of the S3D resource in the output DAT, not a
SimCity 4 screenshot.  Geometry, UV coordinates and triangle ordering come
directly from that resource.  The existing tram-crossing preview module
provides the FSH decoder and orthographic, alpha-tested triangle renderer.
Only dist/model-preview.png is written.  Requires Pillow and NumPy.
"""
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import numpy as np
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
HELPERS = HERE.parent / 'tram-under-hsr'
sys.path.insert(0, str(HELPERS))
spec = importlib.util.spec_from_file_location('tram_crossing_preview', HELPERS / 'render_preview.py')
if spec is None or spec.loader is None:
    raise ImportError('Cannot load the existing NAM software-rendering helpers')
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)


def textures_from_manifest(manifest: dict, required: set[int]) -> dict:
    """Load the exact referenced FSH images, preferring NAM's model group.

    A texture ID may also occur in a lot texture group.  Network S3D textures
    use group 1abe787d, so select that record whenever it is available.  Within
    each record, the last existing file has the installed override precedence.
    """
    result, archives = {}, {}
    dependencies = manifest['texture_dependencies']
    for instance in sorted(required):
        key = f'{instance:08x}'
        if key not in dependencies:
            raise ValueError(f'Texture {key} is absent from the build manifest')
        candidates = dependencies[key]
        preferred = [item for item in candidates
                     if item['tgi'].split('-')[1].lower() == '1abe787d']
        records = preferred or candidates
        found = False
        for record in reversed(records):
            tgi = tuple(int(value, 16) for value in record['tgi'].split('-'))
            for filename in reversed(record['files']):
                path = Path(filename)
                if not path.is_file():
                    continue
                if path not in archives:
                    archives[path] = preview.read_dbpf.entries(path.read_bytes())
                if tgi not in archives[path]:
                    continue
                image = preview.decode_fsh(archives[path][tgi])
                result[instance] = np.asarray(image, dtype=float) / 255
                found = True
                break
            if found:
                break
        if not found:
            raise FileNotFoundError(f'No installed source contains required texture {key}')
    return result


def main():
    manifest = json.loads((HERE / 'dist/build-manifest.json').read_text())
    archive_path = Path(manifest['output'])
    archive = preview.read_dbpf.entries(archive_path.read_bytes())
    instance = int(manifest.get('preview_id', '5dd0f225'), 16)
    resource = archive[0x5ad0e817, 0xbadb57f1, instance]
    model = preview.parse_s3d(preview.read_dbpf.decompress(resource))
    required = {texture for _, _, texture in preview.model_triangles(model)}
    textures = textures_from_manifest(manifest, required)

    # Render both cameras directly from the combined preview model, whose two
    # tiles share their exact in-game 16 m offset.  Supersampling improves edge
    # readability; it does not alter or replace any source textures.
    view_size, supersample = (760, 635), 2
    cameras = [(45, math.degrees(math.atan(1 / math.sqrt(2)))), (0, 71)]
    views = []
    for azimuth, elevation in cameras:
        view = preview.render_view(model, textures, azimuth, elevation,
                                   view_size[0] * supersample,
                                   view_size[1] * supersample)
        views.append(view.resize(view_size, Image.Resampling.LANCZOS))

    canvas = Image.new('RGB', (1640, 960), '#f7f9fb')
    draw = ImageDraw.Draw(canvas)
    dark, muted, blue = '#172b42', '#586a7e', '#176eaf'
    draw.text((60, 38), 'HSR over diagonal GHSR', fill=dark, font=preview.font(40, True))
    draw.text((62, 94), 'Actual packaged model and installed NAM textures',
              fill=muted, font=preview.font(22))
    draw.rounded_rectangle((1350, 43, 1580, 84), radius=9, fill='#e6edf5')
    draw.text((1371, 53), 'EXPERIMENTAL', fill=muted, font=preview.font(19, True))

    for x, view in zip((30, 850), views):
        canvas.paste(view, (x, 169))
    draw.text((62, 151), 'ISOMETRIC VIEW', fill=blue, font=preview.font(17, True))
    draw.text((882, 151), 'VIEW FROM ABOVE', fill=blue, font=preview.font(17, True))
    draw.line((820, 192, 820, 785), fill='#dce3eb', width=1)

    draw.text((62, 806), 'Straight elevated HSR crosses diagonal ground HSR at 45°',
              fill=dark, font=preview.font(25, True))
    draw.text((62, 848), 'Footprint: 2 tiles (16 × 32 metres) · upper route: HSR · lower route: GHSR',
              fill=muted, font=preview.font(22))
    draw.text((62, 910), 'Software model preview. Placement, shadows and train routing require an in-game test.',
              fill=muted, font=preview.font(18))
    destination = HERE / 'dist/model-preview.png'
    canvas.save(destination)
    print(destination)


if __name__ == '__main__':
    main()
