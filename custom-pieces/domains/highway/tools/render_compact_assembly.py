#!/usr/bin/env python3
"""Stage six views of the actual saved highway modules at registered poses."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from PIL import Image, ImageDraw
from scp import jsonc
from scp.city_grid import make_camera, make_city_grid
from scp.dbpf import entries, decompress
from scp.models import parse_s3d, positions, pack_s3d, validate_s3d
from scp.paths import local_settings
from scp.preview import TextureLibrary, font, render_fast_view
from scp.recipes import combine_meshes
from scp.render_headers import _fit_font, TITLE_INK, SUBTITLE_INK, FACTS_INK
from scp.verify import verify_build


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def assembly_header(draw, captions, width):
    """Use the shared typography with the assembly-specific title contract."""
    if len(captions) != 3 or not captions[0].startswith('Assembly - '):
        raise ValueError('Assembly views require one assembly title and three caption rows')
    if not captions[1].startswith(('Clean view | ', 'Component guide | ', 'Construction view | ')):
        raise ValueError('Assembly view purpose must lead the second caption row')
    rows, y = [], 20
    for text, size, bold, colour in zip(captions, (42, 27, 25), (True, False, False),
                                      (TITLE_INK, SUBTITLE_INK, FACTS_INK)):
        face, pixels = _fit_font(draw, text, font, size, width - 60, bold)
        draw.text((30, y), text, font=face, fill=colour)
        rows.append({'text': text, 'colour': colour, 'font_pixels': pixels,
                     'position': [30, y], 'bounds': list(draw.textbbox((30, y), text, font=face))})
        y += 52 if bold else 42
    return {'captions': captions, 'rows': rows, 'bottom': y + 12, 'title_occurrences': 1}


def render(build, destination, *, root=ROOT, plugins=None):
    root, build, destination = map(lambda value: Path(value).resolve(), (root, build, destination))
    if destination.is_relative_to(build):
        raise ValueError('Render staging must stay outside the verified build')
    verify_build(build, write_report=False)
    scene_path = root / 'domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/assembly.jsonc'
    scene = jsonc.load(scene_path)
    manifest_raw = (build / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_raw)
    pieces = {piece['id']: piece for piece in manifest['pieces']}
    plugins = plugins or jsonc.load(local_settings(root))['plugins']
    library, parts, sources, placed = TextureLibrary(plugins), [], {}, []
    for placement in scene['placements']:
        piece = pieces[placement['piece_id']]
        if placement['rotation_degrees_ccw'] != 0:
            raise ValueError('This renderer requires the currently authored zero-rotation highway poses')
        dat = (build / piece['asset_file']).read_bytes()
        resources = {key: decompress(raw) for key, raw in entries(dat).items()}
        raw = resources[0x5AD0E817, 0xBADB57F1, int(piece['preview_id'], 16)]
        model = parse_s3d(raw)
        owned = {int(iid, 16): resources[0x7AB50E44, 0x1ABE787D, int(iid, 16)]
                 for iid in piece.get('authored_texture_ids', [])}
        library.for_model(model, owned_resources=owned)
        east, north = placement['origin_m']
        parts.append((model, model['meshes'], (east, 0., -north)))
        sources[piece['id']] = {'dat_sha256': sha(dat), 'preview_sha256': sha(raw)}
        cells = [[east + 16 * column, north - 16 * row] for column, row in piece['cells']]
        placed.append((placement['label'], cells))
    model = combine_meshes(parts)
    model_check = validate_s3d(model)
    model_hash = sha(pack_s3d(model))
    vertices = [point for block in model['vertices'] for point in positions(block)]
    width_tiles, height_tiles = scene['construction_rectangle_tiles']
    bounds = (-8., -16. * (height_tiles - 1) - 8., 16. * (width_tiles - 1) + 8., 8.)
    reference = (0., -16. * (height_tiles - 1))
    destination.mkdir(parents=True, exist_ok=True)
    output, palette = [], ['#d25a43', '#3e8eae', '#5c9e55', '#aa77b5', '#ca9a31', '#507fc0']
    views = [('overview-top', 0., 90., False, False), ('preview', 45., 31., False, False),
             ('named-top', 0., 90., True, False), ('named-southeast', 45., 31., True, False),
             ('named-northwest', 225., 31., True, False), ('tile-ownership', 0., 90., True, True)]
    for basename, azimuth, elevation, labels, construction in views:
        purpose = 'Construction view' if construction else 'Component guide' if labels else 'Clean view'
        direction = 'North-up' if elevation == 90 else 'Southeast' if azimuth == 45 else 'Northwest'
        canvas = Image.new('RGB', (1900, 1500), '#f7f9fb')
        draw = ImageDraw.Draw(canvas)
        captions = ['Assembly - ' + scene['title'], f'{purpose} | {direction} view',
                    f'Fixed X/Y city grid | {width_tiles} × {height_tiles} construction tiles | 1 tile = 16 m']
        header = assembly_header(draw, captions, 1900)
        camera = make_camera(vertices, azimuth, elevation, 1900, 1180, bounds_world_m=bounds, padding=100)
        background, grid = make_city_grid(camera, bounds, origin_world_m=reference, font=font(23),
                                         bold_font=font(25, True), scale_caption_visible=False)
        view = render_fast_view(model, library.textures, azimuth, elevation, 1900, 1180,
                                camera=camera, background_image=background)
        overlay = ImageDraw.Draw(view)
        if labels:
            for index, (label, cells) in enumerate(placed):
                if construction:
                    for east, north in cells:
                        polygon = [tuple(camera.project_world(east + x, north + y))
                                   for x, y in ((-8, -8), (-8, 8), (8, 8), (8, -8))]
                        overlay.line(polygon + polygon[:1], fill=palette[index % len(palette)], width=4)
                        point = camera.project_world(east, north)
                        overlay.text(tuple(point), label, fill='#142b42', font=font(17, True), anchor='mm', stroke_width=2, stroke_fill='white')
                else:
                    east = sum(cell[0] for cell in cells) / len(cells)
                    north = sum(cell[1] for cell in cells) / len(cells)
                    point = camera.project_world(east, north, 17.)
                    overlay.text(tuple(point), label, fill='#142b42', font=font(23, True), anchor='mm', stroke_width=3, stroke_fill='white')
        top = max(145, header['bottom'] + 8)
        canvas.paste(view, (0, top))
        draw.text((30, 1430), 'Actual saved S3D models and FSH textures at the registered component positions.', fill='#586a7e', font=font(23))
        footer = (f'P01–P{len(placed):02} refer to the numbered placement table. Software model preview.'
                  if labels else '41 owned construction tiles; retained native model overhangs remain visible. Software model preview.')
        draw.text((30, 1465), footer, fill='#586a7e', font=font(22))
        file = destination / (basename + '.png')
        canvas.save(file)
        output.append({'file': file.name, 'sha256': sha(file.read_bytes()), 'size': list(canvas.size),
                       'captions': captions, 'header': header, 'camera': camera.metadata(), 'grid': grid})
    if sha(pack_s3d(model)) != model_hash:
        raise ValueError('Rendering changed compiled model geometry')
    evidence = {'purpose': 'Six views rendered from the saved compiled module models; no in-game observation.',
                'assembly_id': scene['id'], 'assembly_sha256': sha(scene_path.read_bytes()),
                'source_manifest_sha256': sha(manifest_raw), 'piece_sources': sources,
                'combined_model_sha256': model_hash, 'model': model_check,
                'renderer_sha256': sha(Path(__file__).read_bytes()), 'images': output,
                'textures': list(library.provenance.values()), 'in_game_evidence': False}
    (destination / 'render.json').write_text(json.dumps(evidence, indent=2) + '\n')
    return {'images': len(output), 'destination': str(destination), 'source_pieces': len(sources)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--plugins', type=Path)
    args = parser.parse_args()
    print(json.dumps(render(args.build, args.output_dir, root=args.root, plugins=args.plugins), indent=2))


if __name__ == '__main__':
    main()
