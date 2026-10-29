"""Render a complete canonical piece preview on its independent city grid.

This shared renderer accepts encoded models, textures and a registered piece;
it never alters game geometry or uses an assembly-specific caption.
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
from PIL import Image, ImageDraw
from .catalog import piece_cells
from .city_grid import make_camera, make_city_grid
from .models import pack_s3d, parse_s3d, positions, validate_s3d
from .preview import font, render_fast_view, renderer_settings as raster_settings
from .render_headers import draw_header, grid_caption, header_settings, piece_heading, view_caption


TOP_GRID_OVERLAY = {'colour': '#00ff00', 'line_width_pixels': 2,
                    'major_line_width_pixels': 3, 'drawn_above_model': True}


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def _caption(draw, text, y, size, width, *, bold=False, color='#172b42'):
    chosen = font(size, bold)
    while draw.textlength(text, font=chosen) > width - 60 and size > 12:
        size -= 1
        chosen = font(size, bold)
    draw.text((30, y), text, font=chosen, fill=color)


def _overlay_top_grid(image, grid):
    """Keep true tile edges visible across opaque surfaces in a piece plan.

    Reuse the ground grid's projected boundary endpoints, so this overlay
    changes only documentation pixels, never the camera or model geometry.
    """
    draw = ImageDraw.Draw(image)
    for line in grid['grid_lines']:
        width = TOP_GRID_OVERLAY['major_line_width_pixels' if line['major'] else 'line_width_pixels']
        draw.line([tuple(point) for point in line['pixels']],
                  fill=TOP_GRID_OVERLAY['colour'], width=width)
    grid['line_overlay'] = dict(TOP_GRID_OVERLAY)


def local_piece_grid(piece):
    """Describe canonical tile centres without moving or rotating the model.

    Registered cell columns increase east; rows increase south. Display X/Y
    instead increase east/north from the southwest bounding-rectangle centre.
    This reference need not be an occupied cell of a sparse, curved piece.
    """
    cells = piece['cells'] if 'cells' in piece else piece_cells(piece)
    if not isinstance(cells, list) or not cells:
        raise ValueError('A reusable type preview needs nonempty registered cells')
    checked = []
    for cell in cells:
        if (not isinstance(cell, (list, tuple)) or len(cell) != 2
                or any(isinstance(value, bool) or not isinstance(value, (int, float))
                       or not math.isfinite(value) or int(value) != value for value in cell)):
            raise ValueError('Registered cells must be finite integer column/row pairs')
        checked.append(tuple(map(int, cell)))
    if len(set(checked)) != len(checked):
        raise ValueError('Registered cells must not repeat')
    min_column = min(column for column, row in checked)
    max_column = max(column for column, row in checked)
    min_row = min(row for column, row in checked)
    max_row = max(row for column, row in checked)
    southwest = [16.*min_column, -16.*max_row]
    bounds = [southwest[0]-8., southwest[1]-8.,
              16.*max_column+8., -16.*min_row+8.]
    reference = [-min_column, max_row]
    reference_in_grid = (0 <= reference[0] <= max_column-min_column
                         and 0 <= reference[1] <= max_row-min_row)
    return {
        'scope': 'Independent local grid for this reusable type at its default orientation',
        'tile_metres': 16., 'displayed_rotation_ccw_degrees': 0.,
        'origin_world_m': southwest, 'bounds_world_m': bounds,
        'display_axis_labels': {'east': 'X', 'north': 'Y'},
        'display_index_ranges': {'X': [0, max_column-min_column],
                                 'Y': [0, max_row-min_row]},
        'southwest_reference': 'Tile centre at the southwest corner of the occupied-cell bounding rectangle',
        'southwest_corner_occupied': (min_column, max_row) in checked,
        'occupied_local_tiles_en': sorted([[column-min_column, max_row-row]
                                           for column, row in checked]),
        'construction_reference': {
            'world_m': [0., 0.],
            'local_tiles_en': reference,
            'inside_displayed_grid': reference_in_grid,
            'caption_visible': reference_in_grid,
            'meaning': 'The compiled piece reference position, expressed in this local grid; not a cursor anchor',
            'reference_cell_occupied': (0, 0) in checked,
        },
        'model_coordinates_changed': False,
        'origin_marker_visible': False,
    }

def render_piece(piece, raw, library, destination, *, dat_hash, width=1600, height=1200,
                 thumbnail_width=360, view_role='angled', title=None):
    """Write one exact-model canonical view and portable per-view evidence.

    Top-only generation never reads or rewrites the angled view or thumbnail.
    Both roles use untranslated, unrotated geometry and the same local grid.
    """
    if view_role not in ('angled', 'top'):
        raise ValueError('Canonical view role must be angled or top')
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    azimuth, elevation = (0., 90.) if view_role == 'top' else (45., 31.)
    model = parse_s3d(raw)
    model_check = validate_s3d(model)
    before_model = sha256(pack_s3d(model))
    vertices = [point for block in model['vertices'] for point in positions(block)]
    local = local_piece_grid(piece)
    bounds, origin = local['bounds_world_m'], local['origin_world_m']
    canvas = Image.new('RGB', (width, height), '#f7f9fb')
    draw = ImageDraw.Draw(canvas)
    captions = [piece_heading(title or piece['name']), view_caption(view_role, azimuth, elevation), grid_caption(local)]
    header = draw_header(draw, captions, width, font, margin=30, top=20)
    view_height, top = height-230, max(145, header['bottom'])
    if top + view_height > height - 80:
        raise ValueError('Canonical preview dimensions leave no room for the complete scene and evidence footer')
    camera = make_camera(vertices, azimuth, elevation, width, view_height,
                         bounds_world_m=bounds, padding=90)
    background, grid = make_city_grid(camera, bounds, origin_world_m=origin,
                                     font=font(21), bold_font=font(23, True), scale_caption_visible=False)
    textures, texture_sources = library.for_model(model)
    view = render_fast_view(model, textures, azimuth, elevation, width, view_height,
                           camera=camera, background_image=background)
    if view_role == 'top':
        _overlay_top_grid(view, grid)
    canvas.paste(view, (0, top))
    footer = ['Complete reusable piece shown at its authored orientation.',
              'Software model preview.']
    for caption, y_position, size in zip(footer, (height-68, height-35), (22, 21)):
        _caption(draw, caption, y_position, size, width, color='#586a7e')
    captions.extend(footer)
    filename = 'preview-top.png' if view_role == 'top' else 'preview.png'
    target = destination/'previews'/filename
    target.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(target)
    thumbnail = None
    if view_role == 'angled':
        bitmap = canvas.resize((thumbnail_width, round(height*thumbnail_width/width)), Image.Resampling.LANCZOS)
        thumb = target.with_name('preview-thumb.png')
        bitmap.save(thumb)
        thumbnail = {'file': thumb.relative_to(destination).as_posix(), 'sha256': sha256(thumb.read_bytes()), 'size': list(bitmap.size)}
    if sha256(pack_s3d(model)) != before_model:
        raise ValueError('Canonical preview rendering modified the parsed source model')
    image = {
        'purpose': 'Provenance of this standalone compiled-model preview; not game-test evidence.',
        'piece_id': piece['id'], 'menu_name': piece['name'], 'display_title': captions[0],
        'view_role': 'top-down' if view_role == 'top' else 'angled', 'canonical_filename': filename,
        'source': {'asset_file': piece.get('asset_file', piece['id']+'.dat'), 'preview_id': piece['preview_id'],
                   'source_dat_sha256': dat_hash, 'model_sha256': sha256(raw)},
        'file': target.relative_to(destination).as_posix(), 'sha256': sha256(target.read_bytes()), 'size': [width, height],
        'azimuth_degrees': azimuth, 'elevation_degrees': elevation,
        'displayed_rotation_ccw_degrees': 0., 'coordinate_system': local,
        'camera': camera.metadata(), 'grid': grid, 'header': header, 'viewport_offset_xy': [0, top],
        'model': model_check, 'render_model_sha256': before_model,
        'textures': texture_sources, 'captions': captions,
        'annotation_mode': 'Shared source-backed piece title and independent local X/Y grid; no assembly labels',
        'assembly_labels_visible': False, 'other_piece_types_drawn': False,
        'selected_piece_geometry_hidden_or_simplified': False, 'in_game_evidence': False,
        'renderer': preview_settings(width=width, height=height, view_role=view_role),
    }
    if thumbnail is not None:
        image['thumbnail'] = thumbnail
    evidence = destination/('evidence/preview-top.json' if view_role == 'top' else 'evidence/preview.json')
    evidence.parent.mkdir(parents=True, exist_ok=True)
    evidence.write_text(json.dumps(image, indent=2)+'\n')
    return image


_LAYOUT_HELPERS=(local_piece_grid,_caption,_overlay_top_grid,render_piece,make_camera,make_city_grid)


def preview_settings(*, width=1600, height=1200, view_role='angled'):
    """Fingerprint the actual view, shared three-row caption, and city grid."""
    import inspect
    if view_role not in ('angled', 'top'):
        raise ValueError('Canonical view role must be angled or top')
    source='\n'.join(inspect.getsource(function) for function in _LAYOUT_HELPERS)
    azimuth, elevation = (0., 90.) if view_role == 'top' else (45., 31.)
    return {**raster_settings(), 'layout':'one canonical view with independent local city grid',
            'layout_sha256':sha256(source.encode()), 'header':header_settings(),
            'city_grid_source_sha256':sha256((Path(__file__).parent/'city_grid.py').read_bytes()),
            'image_size':[width,height], 'view_size':[width,height-230],
            'views':[{'azimuth':azimuth,'elevation':elevation}], 'view_role':view_role,
            'tile_metres':16., 'origin_marker_visible':False, 'geometry_simplified':False,
            'top_grid_overlay':dict(TOP_GRID_OVERLAY) if view_role == 'top' else None,
            'duplicate_grid_footer_visible':False}


def normalize_preview_evidence(directory):
    """Correct view metadata from saved camera facts without redrawing pixels.

    The raster engine functions are unchanged. The formerly shared settings
    incorrectly described an unused two-panel catalogue layout; this corrects
    that description while retaining the original PNGs and their provenance.
    A missing layout source hash is not invented, so a future strict cache
    still requires a fresh canonical render before claiming that source hash.
    """
    directory=Path(directory);path=directory/'evidence/preview.json'
    entry=json.loads(path.read_text())
    if sha256((directory/'previews/preview.png').read_bytes())!=entry['sha256']:
        raise ValueError('Actual preview PNG differs from its saved evidence')
    if sha256((directory/'previews/preview-thumb.png').read_bytes())!=entry['thumbnail']['sha256']:
        raise ValueError('Actual thumbnail differs from its saved evidence')
    actual={**raster_settings(),'layout':'one canonical view with independent local city grid',
            'image_size':entry['size'],'view_size':entry['camera']['image_size'],
            'views':[{'azimuth':entry['azimuth_degrees'],'elevation':entry['elevation_degrees']}],
            'tile_metres':entry['grid']['tile_metres'],
            'origin_marker_visible':entry['grid']['origin_marker_visible']}
    if entry.get('renderer',{}).get('layout_sha256'):
        actual['layout_sha256']=entry['renderer']['layout_sha256']
    entry['renderer']=actual
    entry['renderer_metadata_note']='View settings normalized from saved camera/grid facts; original image bytes retained. No new render or manual review is claimed.'
    entry={'purpose':entry.get('purpose','Portable provenance for this canonical compiled-model preview; not game evidence.'),
           **{key:value for key,value in entry.items() if key!='purpose'}}
    path.write_text(json.dumps(entry,indent=2)+'\n')
    return entry
