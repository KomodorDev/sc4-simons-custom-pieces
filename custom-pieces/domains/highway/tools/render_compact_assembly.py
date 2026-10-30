#!/usr/bin/env python3
"""Stage six compiled highway assembly views with the trumpet presentation.

The current assembly definition and verified build own all names, poses,
occupied cells, models, and textures. This wrapper reuses the HSR renderer's
presentation, without importing its rail heights or traffic assumptions.
Canonical artwork remains untouched until the staged pictures are reviewed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
sys.dont_write_bytecode = True

from scp import jsonc
from scp.check_bootstrap import SourcePackages

# Resolve tool packages from this checkout, including direct script calls.
sys.meta_path.insert(0, SourcePackages(ROOT))

from scp.dbpf import entries, decompress
from scp.models import pack_s3d
from scp.paths import local_settings
from scp.verify import verify_build
from scp_highway.native import parse_paths
from scp_hsr_tools.render_hsr_assembly import load_scene, render_assembly


ASSEMBLY_ID = 'ddrhw-l1-and-l2-diagonal-avenue-diamond'
TRUMPET = Path('domains/high-speed-rail/01_assemblies/hsr-trumpet-straight-stem')
CANONICAL_VIEWS = (
    ('overview-top.png', 'top-clean-xy.png'),
    ('preview.png', 'southeast-clean-xy.png'),
    ('named-top.png', 'top-xy.png'),
    ('named-southeast.png', 'southeast-xy.png'),
    ('named-northwest.png', 'northwest-xy.png'),
    ('tile-ownership.png', 'placement-plan-xy.png'),
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def saved_resources(build, manifest, piece_ids):
    """Collect exact DAT-owned textures and the saved flat car-path heights."""
    pieces = {piece['id']: piece for piece in manifest['pieces']}
    owned, sources, levels = {}, {}, set()
    for piece_id in sorted(piece_ids):
        piece = pieces[piece_id]
        dat = (build / piece['asset_file']).read_bytes()
        resources = {key: decompress(raw) for key, raw in entries(dat).items()}
        preview = resources[0x5AD0E817, 0xBADB57F1, int(piece['preview_id'], 16)]
        texture_sources = []
        for identifier in piece.get('authored_texture_ids', []):
            iid = int(identifier, 16)
            raw = resources[0x7AB50E44, 0x1ABE787D, iid]
            if iid in owned and owned[iid] != raw:
                raise ValueError(f'Saved texture {iid:08x} differs between component DATs')
            owned[iid] = raw
            texture_sources.append({'instance': f'{iid:08x}', 'fsh_sha256': sha(raw)})
        for key, raw in resources.items():
            if key[:2] != (0x296678F7, 0xA966883F):
                continue
            for route in parse_paths(raw):
                heights = [point[2] for point in route['points']]
                if route['transport'] == 1 and max(heights) - min(heights) <= 1e-7:
                    levels.add(round(heights[0], 7))
        sources[piece_id] = {
            'asset_file': piece['asset_file'], 'dat_sha256': sha(dat),
            'preview_sha256': sha(preview), 'owned_textures': texture_sources,
        }
    return owned, sources, sorted(levels)


def canonical_images(report, destination, prefix):
    """Copy unchanged staged bytes into the exact six README roles and order."""
    staged = {item['file']: item for item in report['images']}
    images, mapping = [], []
    for canonical, suffix in CANONICAL_VIEWS:
        name = f'{prefix}-{suffix}'
        item = staged[name]
        source, target = destination / name, destination / canonical
        shutil.copyfile(source, target)
        if sha(target.read_bytes()) != item['sha256']:
            raise ValueError(f'Canonical staging copy changed the rendered bytes: {canonical}')
        images.append({**item, 'file': canonical, 'staged_file': name})
        mapping.append({'staged_file': name, 'canonical_file': canonical,
                        'sha256': item['sha256']})
    return images, mapping


def render(build, destination, *, root=ROOT, plugins=None,
           width=2800, height=2600, prefix='reviewed-compact-assembly'):
    root, build, destination = map(lambda value: Path(value).resolve(), (root, build, destination))
    if destination.is_relative_to(build):
        raise ValueError('Render staging must stay outside the verified build')
    verify_build(build, write_report=False)
    scene_path = root / 'domains/highway/01_assemblies' / ASSEMBLY_ID / 'assembly.jsonc'
    scene = jsonc.load(scene_path)
    manifest_raw = (build / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_raw)
    model, provenance = load_scene(scene_path, default_build=str(build))
    model_hash = sha(pack_s3d(model))
    piece_ids = {source['piece_id'] for source in provenance['sources']}
    owned, sources, levels = saved_resources(build, manifest, piece_ids)
    expected_levels = [0., 7.5, 15.]
    if levels != expected_levels:
        raise ValueError(f'Unexpected saved flat car-path heights for the highway caption: {levels}')
    plugins = plugins or jsonc.load(local_settings(root))['plugins']
    provenance.update({
        'assembly_id': scene['id'], 'assembly_sha256': sha(scene_path.read_bytes()),
        'source_manifest_sha256': sha(manifest_raw), 'piece_sources': sources,
        'saved_flat_car_path_heights_m': levels,
        'combined_model_sha256': model_hash,
        'renderer_sha256': sha(Path(__file__).read_bytes()),
        'presentation_reference': {
            'assembly_id': 'hsr-trumpet-straight-stem',
            'workflow': 'docs/WORKFLOW_DOCUMENTATION_GENERATION.md#trumpet-presentation-reference',
            'images': [{'file': (TRUMPET / 'previews' / name).as_posix(),
                        'sha256': sha((root / TRUMPET / 'previews' / name).read_bytes()),
                        'corresponding_canonical_file': name}
                       for name, _suffix in CANONICAL_VIEWS],
            'comparison_scope': 'Headers, cameras, grid, compass, full-name cards, placement badges, '
                                'leaders, consistent ownership colours, filled tiles, boundaries, and reference diamonds.',
            'visual_comparison': 'Inspect every staged PNG beside its corresponding reference before promotion.',
        },
    })
    report = render_assembly(
        model, plugins, destination, provenance=provenance,
        width=width, height=height, prefix=prefix,
        owned_texture_resources=owned,
        source_caption='Actual compiled S3D pavement, decks, barriers, and supports | software preview',
        height_caption='Car-path pavement heights: avenue 0 m | lower deck 7.5 m | upper deck 15 m',
        footer_caption='All model geometry shown; no simulated traffic, terrain, or game lighting.',
    )
    if sha(pack_s3d(model)) != model_hash or report['render_model_sha256'] != model_hash:
        raise ValueError('Rendering changed compiled model geometry')
    images, mapping = canonical_images(report, destination, prefix)
    report.update({'images': images, 'staged_to_canonical': mapping,
                   'raw_staging_report': f'{prefix}-preview-evidence.json'})
    (destination / 'render.json').write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    return {'images': len(images), 'destination': str(destination),
            'source_pieces': len(sources), 'placements': len(provenance['sources']),
            'occupied_tiles': sum(len(source['occupied_world_cells']) for source in provenance['sources']),
            'image_size': [width, height], 'canonical_files': [image['file'] for image in images]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--plugins', type=Path)
    parser.add_argument('--width', type=int, default=2800)
    parser.add_argument('--height', type=int, default=2600)
    parser.add_argument('--prefix', default='reviewed-compact-assembly')
    args = parser.parse_args()
    print(json.dumps(render(args.build, args.output_dir, root=args.root, plugins=args.plugins,
                            width=args.width, height=args.height, prefix=args.prefix), indent=2))


if __name__ == '__main__':
    main()
