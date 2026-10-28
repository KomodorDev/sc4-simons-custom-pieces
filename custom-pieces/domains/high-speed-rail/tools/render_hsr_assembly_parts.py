#!/usr/bin/env python3
"""Render canonical compiled angled previews and optional north-up type views.

Every type is shown at its default 0-degree orientation with an independent
16 m city grid. X0,Y0 is the southwest tile centre of its occupied bounding
rectangle, even when that corner itself is empty. Model coordinates do not
change. Assembly labels, positions and rotations remain in JSON evidence;
they are not reusable piece names and do not appear in the pictures.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import tempfile

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
sys.dont_write_bytecode = True

from scp_hsr_tools.render_hsr_assembly import load_scene, sha256
from scp.piece_previews import local_piece_grid, render_piece, preview_settings
from scp.preview import TextureLibrary, read_piece_preview, renderer_settings, _canonical_title


def _type_sources(sources, pieces):
    """Deduplicate placements while rejecting conflicting compiled identities."""
    groups = {}
    for source in sources:
        identifier = source.get('piece_id')
        if identifier not in pieces:
            raise ValueError('Every standalone preview must identify a piece in --build')
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', identifier):
            raise ValueError('Piece IDs must be safe single filename components')
        if source['menu_name'] != pieces[identifier]['name']:
            raise ValueError('Part menu name differs from the audited scene build')
        previous = groups.get(identifier)
        if previous is not None and any(source[key] != previous[key] for key in
                ('source_dat_sha256', 'model_sha256', 'menu_name')):
            raise ValueError('Repeated piece type has conflicting compiled source identities')
        groups[identifier] = source
    return [groups[identifier] for identifier in sorted(groups)]


def render_parts(scene, build, plugins, destination, *, prefix,
                 width=1600, height=1200, thumbnail_width=360, top_piece_ids=()):
    scene, build, destination = map(Path, (scene, build, destination))
    if min(width, height) < 800 or not 0 < thumbnail_width < width:
        raise ValueError('Use full images at least 800px and smaller positive thumbnails')
    if not prefix or Path(prefix).name != prefix:
        raise ValueError('prefix must be one filename component')
    # Verify all assembly names, saved positions and compiled source hashes.
    assembly_model, provenance = load_scene(scene, default_build=build.resolve())
    del assembly_model
    sources = provenance['sources']
    manifest = json.loads((build/'manifest.json').read_text())
    pieces = {piece['id']: piece for piece in manifest['pieces']}
    if len(pieces) != len(manifest['pieces']):
        raise ValueError('Build manifest must contain unique piece IDs')
    type_sources = _type_sources(sources, pieces)
    if isinstance(top_piece_ids, (str, bytes)):
        raise ValueError('top_piece_ids must be a collection of exact piece IDs')
    selected_top = set(top_piece_ids)
    if selected_top-set(source['piece_id'] for source in type_sources):
        raise ValueError('Every top-view type must be used by the audited assembly')
    library = TextureLibrary(plugins)
    destination.mkdir(parents=True, exist_ok=True)
    images, top_images = [], []
    for source in type_sources:
        piece = pieces[source['piece_id']]
        dat_hash = sha256((build/piece['asset_file']).read_bytes())
        if dat_hash != source['source_dat_sha256']:
            raise ValueError('Part source differs from the audited scene build')
        raw = read_piece_preview(build, piece)
        if sha256(raw) != source['model_sha256']:
            raise ValueError('Part preview differs from the audited scene build')
        domain = piece.get('domain')
        title_catalog = {'domains': {domain: {'path': 'domains/'+domain}}} if domain else {'domains': {}}
        title, title_sources = _canonical_title(ROOT, title_catalog, piece)
        # All standalone type views now use the shared canonical renderer.
        # The assembly mapping remains solely in the report below.
        with tempfile.TemporaryDirectory(prefix='.piece-views-', dir=destination) as staging:
            for role in ('angled', 'top') if piece['id'] in selected_top else ('angled',):
                image = render_piece(piece, raw, library, staging, dat_hash=dat_hash,
                                     width=width, height=height, thumbnail_width=thumbnail_width,
                                     view_role=role, title=title)
                filename = f'{piece["id"]}-top-local-xy.png' if role == 'top' else f'{piece["id"]}-southeast-local-xy.png'
                (Path(staging)/image['file']).replace(destination/filename)
                image['file'] = filename
                image['title_source_inputs'] = title_sources
                if role == 'angled':
                    thumb_name = Path(filename).stem+'-thumb.png'
                    (Path(staging)/image['thumbnail']['file']).replace(destination/thumb_name)
                    image['thumbnail']['file'] = thumb_name
                    images.append(image)
                else:
                    top_images.append(image)
                print(json.dumps({'rendered': filename}), flush=True)
    by_type = {item['piece_id']: item for item in images}
    placement_images = [{
        'label': source['label'], 'piece_id': source['piece_id'],
        'menu_name': source['menu_name'],
        'file': by_type[source['piece_id']]['file'],
        'thumbnail': by_type[source['piece_id']]['thumbnail']['file'],
        'assembly_reference_world_m': source['origin_m'],
        'assembly_reference_tiles_en': source['display_origin_tiles_en'],
        'assembly_rotation_ccw_degrees': source['rotation_ccw_degrees'],
        'type_preview_rotation_ccw_degrees': 0.,
        'type_preview_reference_tiles_en': by_type[source['piece_id']]['coordinate_system']['construction_reference']['local_tiles_en'],
        'coordinate_mapping': 'Rotate canonical model coordinates counterclockwise by assembly_rotation_ccw_degrees, then add assembly_reference_world_m; assembly grid labels use assembly_coordinate_system.',
    } for source in sources]
    report = {
        'schema_version': 2,
        'scope': 'One complete, canonical preview per unique reusable type; independent nonnegative local grids',
        'scene_file': provenance['scene_file'], 'scene_sha256': provenance['scene_sha256'],
        'coordinate_system': {'scope': 'Independent local grid per reusable type; see each image coordinate_system',
                              'tile_metres': 16., 'display_axis_labels': {'east': 'X', 'north': 'Y'},
                              'origin_marker_visible': False},
        'assembly_coordinate_system': provenance['coordinate_system'],
        'compiled_source_verification': provenance['compiled_source_verification'],
        'renderer': renderer_settings(),
        'canonical_view_settings': {role: preview_settings(width=width, height=height, view_role=role)
                                    for role in ('angled', 'top')},
        'images': images,
        'placement_images': placement_images,
        'in_game_evidence': False,
    }
    if selected_top:
        report['schema_version'] = 3
        report['scope'] = ('One canonical angled preview per unique reusable type and selected '
                           'north-up top views; unchanged models and independent nonnegative local grids')
        report['top_images'] = top_images
    (destination/f'{prefix}s-preview-evidence.json').write_text(json.dumps(report, indent=2)+'\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scene', required=True, type=Path)
    parser.add_argument('--build', required=True, type=Path)
    parser.add_argument('--plugins', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--prefix', default='straight-stem-trumpet-part',
                        help='Evidence filename prefix; picture filenames use reusable piece IDs')
    parser.add_argument('--top-piece-id', action='append', default=[],
                        help='Also render a north-up top view of this exact type; repeat per type')
    args = parser.parse_args()
    report = render_parts(args.scene, args.build, args.plugins, args.output_dir,
                          prefix=args.prefix, top_piece_ids=args.top_piece_id)
    print(json.dumps({'placements': len(report['placement_images']),
                      'unique_pieces': len(report['images'])}))


if __name__ == '__main__':
    main()
