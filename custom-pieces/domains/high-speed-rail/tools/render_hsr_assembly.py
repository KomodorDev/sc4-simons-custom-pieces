#!/usr/bin/env python3
"""Render complete, compiled HSR geometry without inventing track geometry.

Inputs are either a raw compiled S3D model, or a JSON scene containing actual
registered DAT previews and/or raw S3D models. Scene placements use metres:
``origin_m=[east,north]`` and ``rotation_ccw_degrees`` measured in the map
plane. Texture coordinates, topology, heights and material references remain
unchanged. This is a software model renderer, never an in-game placement test.

Example scene:
  {"title":"HSR assembly", "instances":[
    {"id":"crossing", "build":"../dist/current",
     "piece_id":"hsr-component-modular-crossing-core", "origin_m":[0,0],
     "rotation_ccw_degrees":0}]}

Paths inside a scene are relative to the scene file. No model files, donor
archives or live Plugins are modified. No geometry is hidden or simplified.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import struct
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
sys.dont_write_bytecode = True

from PIL import Image, ImageDraw

from scp.models import pack_s3d, parse_s3d, validate_s3d, positions
from scp.preview import (TextureLibrary, font, read_piece_preview,
                         render_fast_view, renderer_settings)
from scp.recipes import combine_meshes
from scp.render_meshes import assert_render_budget
from scp.city_grid import make_camera, make_city_grid
from scp_hsr_tools.assembly_annotations import (
    draw_piece_callouts, colour_assignment_for_sources, ownership_boundary_segments,
    INTERNAL_GRID_WIDTH, OWNER_BOUNDARY_WIDTH, OWNER_BOUNDARY_HALO_WIDTH,
)


VIEWS = (
    ('southeast', 45., 31., 'Southeast view | looking northwest'),
    ('northwest', 225., 31., 'Northwest view | looking southeast'),
    ('top', 0., 90., 'Top view | north up'),
)


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def _finite(value, label):
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f'{label} must be finite')
    return result


def transform_model(model, origin_m=(0., 0.), rotation_ccw_degrees=0.):
    """Rotate about the model origin, then translate east/north; keep height.

    S3D z increases south, opposite the map's north axis. Consequently a
    counterclockwise map rotation has x'=cos(a)*x+sin(a)*z and
    z'=-sin(a)*x+cos(a)*z. Positive north translation subtracts from S3D z.
    """
    if len(origin_m) != 2:
        raise ValueError('origin_m must contain exactly east and north metres')
    east = _finite(origin_m[0], 'east origin')
    north = _finite(origin_m[1], 'north origin')
    angle = math.radians(_finite(rotation_ccw_degrees, 'rotation'))
    cosine, sine = math.cos(angle), math.sin(angle)
    transformed = deepcopy(model)
    for block in transformed['vertices']:
        raw = bytearray(block['data'])
        for offset in range(0, len(raw), block['stride']):
            x, height, z = struct.unpack_from('<3f', raw, offset)
            struct.pack_into('<3f', raw, offset,
                             cosine*x+sine*z+east,
                             height, -sine*x+cosine*z-north)
        block['data'] = bytes(raw)
    validate_s3d(transformed)
    return transformed


def load_scene(path, *, default_build=None):
    path = Path(path).resolve()
    raw_scene = path.read_bytes()
    scene = json.loads(raw_scene)
    instances = scene.get('instances', scene.get('placements'))
    if not isinstance(instances, list) or not instances:
        raise ValueError('Scene needs a nonempty instances list')
    coordinate_system = scene.get('coordinate_system', {
        'origin_name': 'scene origin', 'origin_world_m': [0., 0.],
        'tile_size_m': 16., 'axes': 'east,north,height',
        'tile_boundaries_offset_m': 8.,
    })
    display_origin = coordinate_system.get('origin_world_m', [0., 0.])
    if len(display_origin) != 2:
        raise ValueError('Display origin needs east and north metres')
    display_origin = [_finite(value, 'display origin') for value in display_origin]
    sources, evidence, identifiers, builds = [], [], set(), {}
    labels = set()
    for number, instance in enumerate(instances, 1):
        identifier = instance.get('id', instance.get('instance_id', instance.get('name')))
        if not isinstance(identifier, str) or not identifier or identifier in identifiers:
            raise ValueError('Every scene instance needs a unique, nonempty id')
        identifiers.add(identifier)
        if ('model_file' in instance) == ('piece_id' in instance):
            raise ValueError('Each instance needs exactly one model_file or piece_id')
        if 'model_file' in instance:
            model_path = (path.parent/instance['model_file']).resolve()
            raw = model_path.read_bytes()
            source = {'model_file': instance['model_file']}
            menu_name = instance.get('menu_name', identifier)
            piece = None
        else:
            build_name = instance.get('build', default_build or scene.get('default_build'))
            if not build_name:
                raise ValueError('Built-piece placements need build, default_build or --build')
            build = (path.parent/build_name).resolve()
            if build not in builds:
                manifest_raw = (build/'manifest.json').read_bytes()
                manifest = json.loads(manifest_raw)
                builds[build] = manifest, sha256(manifest_raw)
            manifest, manifest_hash = builds[build]
            matches = [piece for piece in manifest['pieces']
                       if piece['id'] == instance['piece_id']]
            if len(matches) != 1:
                raise ValueError(f'Expected exactly one built piece {instance["piece_id"]}')
            piece = matches[0]
            menu_name = piece['name']
            if instance.get('menu_name', menu_name) != menu_name:
                raise ValueError(f'Scene menu name differs from the compiled piece: {identifier}')
            raw = read_piece_preview(build, piece)
            source = {'piece_id': piece['id'], 'build': build.name,
                      'manifest_sha256_at_render_time': manifest_hash,
                      'source_dat_sha256': sha256((build/piece['asset_file']).read_bytes()),
                      'asset_file': piece['asset_file'],
                      'preview_id': piece['preview_id']}
        model = parse_s3d(raw)
        budget = assert_render_budget(model)
        placement = {'origin_m': list(instance.get('origin_m', [0., 0.])),
                     'rotation_ccw_degrees': instance.get('rotation_ccw_degrees',
                         instance.get('rotation_degrees_ccw', 0.))}
        transformed = transform_model(model, **placement)
        sources.append((transformed, transformed['meshes'], (0., 0., 0.)))
        label = instance.get('label', f'P{number:02}')
        if not isinstance(label, str) or not label or label in labels:
            raise ValueError('Every scene label must be unique and nonempty')
        labels.add(label)
        points = [point for block in transformed['vertices'] for point in positions(block)]
        # Attach the badge to a real upper-deck vertex of this exact instance.
        # Using a bounding-box centre alone can point into the empty inside of a curve.
        top = max(point[1] for point in points)
        deck = [point for point in points if point[1] >= top-3.]
        centre = [(min(point[axis] for point in deck)+max(point[axis] for point in deck))/2.
                  for axis in (0, 2)]
        anchor = min(deck, key=lambda point: (point[0]-centre[0])**2+(point[2]-centre[1])**2)
        cells = []
        for column, row in (piece.get('cells', []) if piece else []):
            angle = math.radians(placement['rotation_ccw_degrees'])
            x, north = 16.*column, -16.*row
            cells.append([round(x*math.cos(angle)-north*math.sin(angle)+placement['origin_m'][0], 6),
                          round(x*math.sin(angle)+north*math.cos(angle)+placement['origin_m'][1], 6)])
        display_metres = [placement['origin_m'][axis]-display_origin[axis] for axis in range(2)]
        display_tiles = [value/16. for value in display_metres]
        for key, expected in (('display_origin_tiles_en', display_tiles),
                              ('display_origin_m', display_metres)):
            if key in instance and instance[key] != expected:
                raise ValueError(f'Stale display origin in {identifier}: {key}')
        evidence.append({'id': identifier, **source, **placement,
                         'label': label, 'menu_name': menu_name,
                         'display_origin_tiles_en': display_tiles,
                         'display_origin_m': display_metres,
                         'label_anchor_world_m': [anchor[0], -anchor[2], anchor[1]],
                         'occupied_world_cells': cells,
                         'model_sha256': sha256(raw), 'render_budget': budget})
    combined = combine_meshes(sources)
    provenance = {'scene_file': path.name, 'scene_sha256': sha256(raw_scene),
                  'title': scene.get('title', 'HSR interchange'),
                  'sources': evidence,
                  'geometry_status': scene.get('geometry_status',
                      'assembled actual compiled model resources'),
                  'validation': scene.get('validation', {})}
    provenance['coordinate_system'] = coordinate_system
    if 'placement_plan_title' in scene:
        provenance['placement_plan_title'] = scene['placement_plan_title']
    if all('source_dat_sha256' in item for item in evidence):
        provenance['compiled_source_verification'] = {
            'instances_checked': len(evidence),
            'unique_pieces_checked': len({item['piece_id'] for item in evidence}),
            'every_source_preview_sha256_matches_current_dat': True,
            'manifest_hash_scope': 'Captured at render time; DAT hashes identify the unchanged compiled assets independently of documentation updates.',
        }
    return combined, provenance


def _caption(draw, text, y, size, width, *, bold=False, color='#172b42'):
    """Fit the caption without clipping a long assembly title."""
    while size > 14:
        face = font(size, bold)
        if draw.textbbox((0, 0), text, font=face)[2] <= width-64:
            break
        size -= 1
    draw.text((32, y), text, font=font(size, bold), fill=color)


def assembly_caption_rows(name, view_class, camera):
    """Keep the assembly identity in row one and the view class in row two."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError('Assembly captions require a nonempty semantic name')
    if view_class not in ('Clean view', 'Component guide', 'Construction view'):
        raise ValueError('Unknown assembly view class')
    if not isinstance(camera, str) or not camera.strip():
        raise ValueError('Assembly captions require a camera description')
    name = name.strip()
    prefix = 'Assembly - '
    while name.startswith(prefix):
        name = name[len(prefix):].strip()
    if not name or name == prefix.rstrip():
        raise ValueError('Assembly captions require a nonempty semantic name')
    return prefix+name, view_class+' | '+camera.strip()


def _grid_bounds(vertices, sources):
    """Enclose real cells and model at tile edges, without extra negative-index cells."""
    cells = [cell for source in sources for cell in source.get('occupied_world_cells', [])]
    east = [point[0] for point in vertices] + [point[0] for point in cells]
    north = [-point[2] for point in vertices] + [point[1] for point in cells]
    # Bounds are tile edges, not a lattice through the tile centres.
    return (16.*math.floor((min(east)+8.)/16.)-8.,
            16.*math.floor((min(north)+8.)/16.)-8.,
            16.*math.ceil((max(east)-8.)/16.)+8.,
            16.*math.ceil((max(north)-8.)/16.)+8.)


def _placement_plan(vertices, sources, bounds, origin, width, height, panel, top, *, title=None,
                    colour_assignment=None):
    """Draw exact occupied city cells. This is explicitly a plan, not model geometry."""
    canvas = Image.new('RGB', (width, height), '#f7f9fb')
    draw = ImageDraw.Draw(canvas)
    header_rows = assembly_caption_rows(title or 'HSR interchange', 'Construction view', 'Top view | north up')
    _caption(draw, header_rows[0], 22, 34, width, bold=True)
    _caption(draw, header_rows[1], 72, 23, width, color='#176eaf')
    label_prefix = 'Piece labels'
    _caption(draw, f'{label_prefix} match the model views and guide | diamonds mark piece reference positions, not cursor anchors',
             108, 21, width, color='#586a7e')
    view_width, view_height = width-2*panel, height-top-115
    camera = make_camera(vertices, 0., 90., view_width, view_height,
                         bounds_world_m=bounds, padding=85)
    view, grid = make_city_grid(camera, bounds, origin_world_m=origin,
                                font=font(18), bold_font=font(19, True))
    vd = ImageDraw.Draw(view)
    colours = colour_assignment or colour_assignment_for_sources(sources)
    owners = {}
    plan_sources = []
    for source in sources:
        label = source['label']
        colour = colours['palette'][label]
        fill = colours['ownership_fill_palette'][label]
        for east, north in source.get('occupied_world_cells', []):
            key = (east, north)
            if key in owners:
                raise ValueError(f'Placement-plan cell has more than one owner: {key}')
            owners[key] = label
            polygon = camera.project_world([east-8, east+8, east+8, east-8],
                                            [north-8, north-8, north+8, north+8])
            vd.polygon([tuple(p) for p in polygon], fill=fill)
        copy = deepcopy(source)
        cells = source.get('occupied_world_cells', [])
        if cells:
            average = [sum(cell[i] for cell in cells)/len(cells) for i in range(2)]
            centre = min(cells, key=lambda cell: sum((cell[i]-average[i])**2 for i in range(2)))
            copy['label_anchor_world_m'] = [*centre, 0.]
        plan_sources.append(copy)
    boundaries = ownership_boundary_segments(sources)
    # Paint all halos before all dark boundaries: later strokes must not
    # erase a previous edge at a three-way junction or shared tile corner.
    for segment in boundaries:
        if segment['kind'] == 'internal-grid':
            first, last = segment['world_endpoints_m']
            vd.line([tuple(camera.project_world(*first)), tuple(camera.project_world(*last))],
                    fill='#687784', width=INTERNAL_GRID_WIDTH)
    for colour, stroke in (('#ffffff', OWNER_BOUNDARY_HALO_WIDTH), ('#10212d', OWNER_BOUNDARY_WIDTH)):
        for segment in boundaries:
            if segment['kind'] != 'internal-grid':
                first, last = segment['world_endpoints_m']
                vd.line([tuple(camera.project_world(*first)), tuple(camera.project_world(*last))],
                        fill=colour, width=stroke)
    for source in sources:
        label = source['label']
        for east, north in source.get('occupied_world_cells', []):
            centre = camera.project_world(east, north)
            vd.text(tuple(centre), label, font=font(17, True),
                    fill=colours['ownership_text_colour'], anchor='mm')
        east, north = source['origin_m']
        x, y = camera.project_world(east, north)
        vd.polygon([(x,y-8),(x+8,y),(x,y+8),(x-8,y)], fill='white',
                   outline=colours['palette'][label], width=3)
    canvas.paste(view, (panel, top))
    labels = draw_piece_callouts(canvas, camera, plan_sources,
                                 view_offset=(panel, top), panel_width=panel,
                                 header_y=top+30, footer_y=height-140,
                                 colour_assignment=colours)
    draw = ImageDraw.Draw(canvas)
    _caption(draw, f'{len(owners)} occupied tiles | blank squares remain empty | same P-labels in every view',
             height-77, 21, width, color='#586a7e')
    _caption(draw, 'Match the shown positions and rotations; reference diamonds mark model origins.',
             height-42, 20, width, color='#586a7e')
    return canvas, {'kind': 'construction tile-ownership plan', 'camera': camera.metadata(),
                    'header_rows': list(header_rows), 'label': header_rows[1],
                    'grid': grid, 'piece_labels': labels,
                    'colour_assignment': colours,
                    'ownership_boundaries': {
                        'internal_grid_width_pixels': INTERNAL_GRID_WIDTH,
                        'outer_and_inter_owner_width_pixels': OWNER_BOUNDARY_WIDTH,
                        'boundary_halo_width_pixels': OWNER_BOUNDARY_HALO_WIDTH,
                        'halos_drawn_before_all_dark_boundaries': True, 'segments': boundaries},
                    'occupied_tiles': len(owners),
                    'owners': [{'east_m': key[0], 'north_m': key[1], 'label': label}
                               for key, label in sorted(owners.items())]}


def render_assembly(model, plugins, destination, *, provenance=None,
                    width=2800, height=2100, prefix='hsr-trumpet'):
    if width < 640 or height < 480:
        raise ValueError('Assembly previews require at least 640 x 480 pixels')
    if not prefix or Path(prefix).name != prefix:
        raise ValueError('prefix must be one filename component')
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    provenance = deepcopy(provenance or {})
    check = validate_s3d(model)
    budget = assert_render_budget(model)
    library = TextureLibrary(plugins)
    textures, texture_provenance = library.for_model(model)
    vertices = [point for block in model['vertices'] for point in positions(block)]
    bounds = [[min(point[axis] for point in vertices),
               max(point[axis] for point in vertices)] for axis in range(3)]
    title = provenance.get('title', 'HSR interchange')
    sources = provenance.get('sources', [])
    labelled = bool(sources) and all('label_anchor_world_m' in item and 'piece_id' in item
                                    for item in sources)
    colours = colour_assignment_for_sources(sources) if labelled else None
    if labelled and (width < 2000 or height < 1400):
        raise ValueError('Named piece callouts require at least 2000 x 1400 pixels')
    panel = min(570, width//5) if labelled else 0
    top = 190 if labelled else 147
    view_width, view_height = width-2*panel, height-top-115
    origin = provenance.get('coordinate_system', {}).get('origin_world_m', [0., 0.])
    grid_bounds = _grid_bounds(vertices, sources)
    images = []
    for name, azimuth, elevation, label in VIEWS:
        canvas = Image.new('RGB', (width, height), '#f7f9fb')
        draw = ImageDraw.Draw(canvas)
        header_rows = assembly_caption_rows(title, 'Component guide' if labelled else 'Clean view', label)
        _caption(draw, header_rows[0], 22, 34, width, bold=True)
        _caption(draw, header_rows[1], 72, 23, width, color='#176eaf')
        _caption(draw, 'Actual compiled S3D track, decks, and supports | software preview',
                 108, 21, width, color='#586a7e')
        if labelled:
            labels_caption = f'{len(sources)} named placements | positions in side panels'
            _caption(draw, f'X/Y tile coordinates | 1 tile = 16 m | {labels_caption}',
                     143, 20, width, color='#586a7e')
            if provenance.get('coordinate_system', {}).get('layout') == 'straight-stem-trumpet':
                _caption(draw, 'Rail-path heights: mainline and outside arms 15.5 m | upper bridge 30.5 m | northern corner joint 23 m',
                         170, 18, width, color='#586a7e')
        camera = make_camera(vertices, azimuth, elevation, view_width, view_height,
                             bounds_world_m=grid_bounds,
                             padding=85 if labelled else 35)
        background, grid = make_city_grid(camera, grid_bounds, origin_world_m=origin,
                                          font=font(18 if labelled else 11),
                                          bold_font=font(19 if labelled else 12, True))
        view = render_fast_view(model, textures, azimuth, elevation,
                                view_width, view_height, camera=camera,
                                background_image=background)
        canvas.paste(view, (panel, top))
        labels = draw_piece_callouts(canvas, camera, sources,
                                    view_offset=(panel, top), panel_width=panel,
                                    header_y=top+30, footer_y=height-140,
                                    colour_assignment=colours) if labelled else None
        _caption(draw,
                 'All model geometry shown; no simulated trains, terrain, or game lighting.',
                 height-65, 20, width, color='#586a7e')
        target = destination/f'{prefix}-{name}-xy.png'
        canvas.save(target)
        image = {'file': target.name, 'sha256': sha256(target.read_bytes()),
                 'size': [width, height], 'azimuth_degrees': azimuth,
                 'elevation_degrees': elevation, 'label': header_rows[1],
                 'header_rows': list(header_rows),
                 'variant': 'named' if labelled else 'overview',
                 'camera': camera.metadata(), 'grid': grid,
                 'piece_labels': labels}
        images.append(image)
        print(json.dumps({'rendered': target.name}), flush=True)
        if labelled and name in ('top', 'southeast'):
            # Clean companions use the same complete model and world coordinates,
            # with the whole width available for inspecting its shape.
            clean = Image.new('RGB', (width, height), '#f7f9fb')
            cd = ImageDraw.Draw(clean)
            clean_header_rows = assembly_caption_rows(title, 'Clean view', label)
            _caption(cd, clean_header_rows[0], 22, 34, width, bold=True)
            _caption(cd, clean_header_rows[1], 72, 23, width, color='#176eaf')
            _caption(cd, 'Actual compiled S3D track, decks, and supports | software preview',
                     108, 21, width, color='#586a7e')
            _caption(cd, 'X/Y tile coordinates | 1 tile = 16 m',
                     143, 20, width, color='#586a7e')
            clean_camera = make_camera(vertices, azimuth, elevation, width, view_height,
                                       bounds_world_m=grid_bounds, padding=100)
            clean_background, clean_grid = make_city_grid(clean_camera, grid_bounds,
                origin_world_m=origin, font=font(20), bold_font=font(21, True))
            clean_view = render_fast_view(model, textures, azimuth, elevation,
                width, view_height, camera=clean_camera, background_image=clean_background)
            clean.paste(clean_view, (0, top))
            _caption(cd, 'All model geometry shown; no simulated trains, terrain, or game lighting.',
                     height-65, 20, width, color='#586a7e')
            clean_target = destination/f'{prefix}-{name}-clean-xy.png'
            clean.save(clean_target)
            images.append({'file': clean_target.name, 'sha256': sha256(clean_target.read_bytes()),
                'size': [width, height], 'azimuth_degrees': azimuth,
                'elevation_degrees': elevation, 'label': clean_header_rows[1],
                'header_rows': list(clean_header_rows),
                'variant': 'clean', 'piece_labels': None,
                'camera': clean_camera.metadata(), 'grid': clean_grid})
            print(json.dumps({'rendered': clean_target.name}), flush=True)
    if labelled and any(item.get('occupied_world_cells') for item in sources):
        plan, metadata = _placement_plan(vertices, sources, grid_bounds, origin,
                                         width, height, panel, top,
                                         title=title,
                                         colour_assignment=colours)
        target = destination/f'{prefix}-placement-plan-xy.png'
        plan.save(target)
        images.append({'file': target.name, 'sha256': sha256(target.read_bytes()),
                       'size': [width, height], 'variant': 'construction-plan', **metadata})
        print(json.dumps({'rendered': target.name}), flush=True)
    settings = renderer_settings()
    # The shared settings describe catalogue panels; record these larger
    # assembly dimensions and each camera explicitly instead of inheriting
    # unrelated catalogue views.
    settings.pop('view_size', None)
    settings['image_size'] = [width, height]
    settings['views'] = [{'azimuth': item[1], 'elevation': item[2]}
                         for item in VIEWS]
    settings['assembly_renderer_sha256'] = sha256(Path(__file__).read_bytes())
    settings['city_grid_renderer_sha256'] = sha256((ROOT/'framework/scp/city_grid.py').read_bytes())
    settings['piece_annotations_renderer_sha256'] = sha256((ROOT/'domains/high-speed-rail/tools/assembly_annotations.py').read_bytes())
    report = {
        'schema_version': 1, **provenance,
        'source_kind': 'actual compiled S3D geometry',
        'render_model_sha256': sha256(pack_s3d(model)),
        'geometry_invented_by_renderer': False, 'geometry_simplified': False,
        'geometry_hidden': False, 'in_game_evidence': False,
        'model': {'triangles': check['triangles'], 'mesh_count': check['mesh_count'],
                  'bounds_s3d_xyz_m': bounds, 'render_budget': budget},
        'textures': texture_provenance, 'renderer': settings, 'images': images,
        'colour_assignment': colours,
    }
    report_path = destination/f'{prefix}-preview-evidence.json'
    report_path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--scene', type=Path)
    source.add_argument('--model', type=Path)
    parser.add_argument('--provenance', type=Path,
                        help='Optional metadata for a complete raw S3D model')
    parser.add_argument('--build', type=Path,
                        help='Default actual DAT build for --scene placements')
    parser.add_argument('--build-label',
                        help='Portable logical name for a build currently in an atomic staging folder')
    parser.add_argument('--save-model', type=Path,
                        help='Write the exact combined S3D used for rendering')
    parser.add_argument('--plugins', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--prefix', default='hsr-trumpet')
    parser.add_argument('--width', type=int, default=2800)
    parser.add_argument('--height', type=int, default=2100)
    args = parser.parse_args()
    if args.scene:
        if args.provenance:
            parser.error('--provenance belongs with --model; scenes carry their metadata')
        model, provenance = load_scene(args.scene, default_build=args.build.resolve() if args.build else None)
        if args.build_label:
            if not args.build_label or Path(args.build_label).name != args.build_label:
                parser.error('--build-label must be one portable filename component')
            for source in provenance['sources']:
                if 'build' in source:
                    source['build'] = args.build_label
    else:
        raw = args.model.read_bytes()
        model = parse_s3d(raw)
        provenance = json.loads(args.provenance.read_text()) if args.provenance else {}
        provenance['model_file'] = args.model.name
        provenance['model_sha256'] = sha256(raw)
    if args.save_model:
        args.save_model.parent.mkdir(parents=True, exist_ok=True)
        args.save_model.write_bytes(pack_s3d(model))
    report = render_assembly(model, args.plugins, args.output_dir,
                             provenance=provenance, width=args.width,
                             height=args.height, prefix=args.prefix)
    print(json.dumps({'images': [item['file'] for item in report['images']],
                      'triangles': report['model']['triangles'],
                      'in_game_evidence': False}, indent=2))


if __name__ == '__main__':
    main()
