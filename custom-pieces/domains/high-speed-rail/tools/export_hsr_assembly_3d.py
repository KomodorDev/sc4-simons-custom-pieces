#!/usr/bin/env python3
"""Export exact compiled geometry and native textures as an orbitable preview.

The HTML fragment embeds gzip-compressed, indexed XYZ/UV vertices and exact
triangle indices. No triangles are reduced or discarded. There are no remote
libraries, API requests or dependencies beyond the browser's WebGL2 and gzip
decompression support. Inline output is refused above the 1 MB size limit.
"""
from __future__ import annotations

import argparse
import base64
from collections import defaultdict
import gzip
import hashlib
import io
import json
from pathlib import Path
import struct
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
sys.dont_write_bytecode = True

import numpy as np
from PIL import Image

from scp.models import parse_s3d, positions, validate_s3d
from scp.preview import TextureLibrary, model_triangles
from scp.render_meshes import assert_render_budget


def embedded_geometry(model, plugins):
    validate_s3d(model)
    budget = assert_render_budget(model)
    vertices_by_texture = defaultdict(dict)
    indices_by_texture = defaultdict(list)
    for xyz, uv, texture in model_triangles(model):
        vertices, indices = vertices_by_texture[texture], indices_by_texture[texture]
        for point, coords in zip(xyz, uv):
            encoded = struct.pack('<5f', *point, *coords)
            if encoded not in vertices:
                vertices[encoded] = len(vertices)
            indices.append(vertices[encoded])
    binary, groups = bytearray(), []
    for texture in sorted(vertices_by_texture):
        vertices, indices = vertices_by_texture[texture], indices_by_texture[texture]
        vertex_offset = len(binary)
        binary.extend(b''.join(vertices))
        index_offset = len(binary)
        binary.extend(struct.pack('<'+'I'*len(indices), *indices))
        groups.append({'texture': texture, 'vertex_offset': vertex_offset,
                       'vertex_count': len(vertices), 'index_offset': index_offset,
                       'index_count': len(indices)})
    library = TextureLibrary(plugins)
    textures, provenance = library.for_model(model)
    atlases = []
    for texture, pixels in sorted(textures.items()):
        image = Image.fromarray(np.uint8(np.rint(np.clip(pixels*255., 0., 255.))), 'RGBA')
        out = io.BytesIO()
        image.save(out, format='PNG', optimize=True)
        atlases.append({'id': texture,
                        'png': base64.b64encode(out.getvalue()).decode('ascii')})
    points = np.asarray([point for block in model['vertices'] for point in positions(block)])
    low, high = points.min(axis=0), points.max(axis=0)
    # Group corresponding bytes of each 32-bit word before compression. This
    # is reversible byte rearrangement, retaining the precise IEEE floats
    # and triangle indices while compressing recurring coordinate exponents.
    shuffled = np.frombuffer(binary, dtype=np.uint8).reshape(-1, 4).T.copy().tobytes()
    return {
        'groups': groups, 'atlases': atlases,
        'geometry': base64.b64encode(gzip.compress(shuffled, mtime=0)).decode('ascii'),
        'byte_plane_shuffle': 4,
        'center': ((low+high)/2.).tolist(),
        'radius': float(np.linalg.norm(high-low)/2.),
        'triangle_count': sum(group['index_count']//3 for group in groups),
        'geometry_hidden': False, 'geometry_simplified': False,
        'textures': provenance, 'render_budget': budget,
    }


def export(model_file, plugins, destination):
    raw = Path(model_file).read_bytes()
    data = embedded_geometry(parse_s3d(raw), plugins)
    data['model_sha256'] = hashlib.sha256(raw).hexdigest()
    template = Path(__file__).with_name('assembly-3d-fragment.txt').read_text()
    output = template.replace('ASSEMBLY_DATA_PLACEHOLDER',
                               json.dumps(data, separators=(',', ':'), allow_nan=False))
    if 'ASSEMBLY_DATA_PLACEHOLDER' in output:
        raise ValueError('Assembly data was not inserted')
    if len(output.encode('utf-8')) >= 1_000_000:
        raise ValueError('Exact geometry exceeds the 1 MB inline preview limit; use the PNG views')
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output)
    return {'output': str(destination.resolve()), 'size_bytes': destination.stat().st_size,
            'model_sha256': data['model_sha256'], 'triangle_count': data['triangle_count'],
            'geometry_hidden': False, 'geometry_simplified': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', required=True, type=Path)
    parser.add_argument('--plugins', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(export(args.model, args.plugins, args.output), indent=2))


if __name__ == '__main__':
    main()
