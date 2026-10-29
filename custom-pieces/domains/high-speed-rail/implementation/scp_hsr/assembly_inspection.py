"""Inspect actual compiled network archives and placed geometry independently.

These helpers read saved DAT models, paths, shadows and triangle inventories.
They have no dependency on a particular assembly version or geometry writer.
The only exceptional owned-cell support vertices are gated by exact current
model fingerprints and the same piece owning both neighboring cells.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import struct

from scp.dbpf import decompress, entries, require
from scp.models import parse_s3d
from scp.render_meshes import _triangles
from scp.track_paths import _parse_paths
from .hsr_trumpet_verify import key, rotate

S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
SHADOW = (0x7AB50E44, 0x2BC2759A)
FAN_ID = 'hsr-component-l2-paired-fan-compact-join'
FAN_CORE_ID = 'hsr-l2-mixed-fan-compact-recessed-web'
CORE_INHERITED_EDGE_SUPPORTS = {
    (112., 32.): ((2, 1), '02b6aaaaffa6c07ad253e2c45efbb6b6709dbd64cce12672f3ce80556f29549a'),
    (128., 32.): ((3, 1), '8d7a29768be30c12b9325315608b46c26ab01c3b2b0af46d8ca20913315beb91'),
}
INHERITED_EDGE_SUPPORTS = {
    (112., 32.): ((3, 3), 'e565971d06cf636dce72ed7473d1cf354ef38573021ca56e50f7adf019866f1a'),
    (128., 32.): ((4, 3), '216257d7ed1183f7965eceac3d894ef8b95afb863ea770b8d527906e31f9a195'),
}


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def rotation(instance):
    degrees = instance.get('rotation_ccw_degrees', instance.get(
        'rotation_degrees_ccw', instance.get('rotation_degrees', 0)))
    require(degrees in (0, 90, 180, 270), 'Only proper cardinal rotations are permitted')
    return degrees//90


def placements(scene):
    result = scene.get('instances', scene.get('placements'))
    require(isinstance(result, list) and result, 'Assembly scene needs placements')
    return result


def load_build(path):
    path = Path(path).resolve()
    raw = (path/'manifest.json').read_bytes()
    manifest = json.loads(raw)
    pieces = {}
    for piece in manifest['pieces']:
        require(piece['id'] not in pieces, 'Duplicate compiled piece ID')
        pieces[piece['id']] = piece
    cache = {}

    def resources(piece):
        if piece['id'] not in cache:
            dat = (path/piece['asset_file']).read_bytes()
            cache[piece['id']] = {
                'sha256': sha256(dat),
                'resources': {tgi: decompress(value) for tgi, value in entries(dat).items()},
            }
        return cache[piece['id']]

    return {'path': path, 'manifest_sha256': sha256(raw), 'pieces': pieces,
            'resources': resources}


def triangle_count(raw):
    model = parse_s3d(raw)
    return sum(length//3 for mesh in model['meshes']
               for kind, _, length in model['primitives'][mesh['frames'][0][2]]
               if kind == 0)


def _triangle_inventory(raw, east=0., south=0.):
    """Read saved XYZ/UV triangles; preserve winding, materials and repeats."""
    model = parse_s3d(raw)
    inventory = Counter()
    for mesh in model['meshes']:
        require(len(mesh['frames']) == 1, 'The reviewed parts must remain static single-frame models')
        frame = mesh['frames'][0]
        material = hashlib.sha256(model['materials'][frame[3]]['raw']).digest()
        for triangle in _triangles(model, frame):
            vertices = []
            for vertex in triangle:
                x, height, z = struct.unpack_from('<3f', vertex)
                # Combining saved tile models writes these translated floats
                # to the preview's float32 buffer. No new surface is made.
                vertices.append(struct.pack('<3f', x+east, height, z+south)+vertex[12:])
            canonical = min(tuple(vertices), tuple(vertices[1:]+vertices[:1]),
                            tuple(vertices[2:]+vertices[:2]))
            inventory[hashlib.sha256(material+b''.join(canonical)).digest()] += 1
    return inventory


def audit_preview_tile_identity(piece, resources):
    """Check actual preview faces against actual saved placed-tile faces."""
    expected = Counter()
    for (column, row), tile in zip(piece['cells'], piece['tile_ids']):
        expected.update(_triangle_inventory(resources[*S3D, number(tile)],
                                             16.*column, 16.*row))
    actual = _triangle_inventory(resources[*S3D, number(piece['preview_id'])])
    require(actual == expected,
            f'Compiled preview changes saved tile geometry, materials or UVs: {piece["id"]}')
    return {'preview_triangles': sum(actual.values()),
            'preview_matches_actual_saved_tile_faces_materials_and_uvs': True}


def world_tiles(scene, build):
    result, source_records, preview_audits = {}, [], {}
    for index, instance in enumerate(placements(scene), 1):
        piece = build['pieces'][instance['piece_id']]
        origin = instance['origin_m']
        require(len(origin) == 2 and all(abs(v/16.-round(v/16.)) < 1e-9 for v in origin),
                'Every module must use the original 16 m city grid')
        turns = rotation(instance)
        identifier = instance.get('label', instance.get('id', str(index)))
        require(len(piece['cells']) == len(piece['tile_ids']), 'Incomplete compiled tile mapping')
        saved = build['resources'](piece)
        resources = saved['resources']
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            column, row = cell
            east, north, _ = rotate((16.*column, -16.*row, 0.), turns)
            position = key((east+origin[0], north+origin[1], 0.))[:2]
            require(position not in result, f'Two modules own city tile {position}')
            iid = number(tile)
            tile_resources = {'path': resources[*PATH, iid]}
            for zoom in range(5):
                tile_resources[f'model_{zoom}'] = resources[*S3D, iid+zoom]
                tile_resources[f'shadow_{zoom}'] = resources[*SHADOW, iid+zoom]
            result[position] = {'piece_id': piece['id'], 'recipe': piece['recipe'],
                                'instance_id': identifier, 'cell': tuple(cell),
                                'rotation': turns, 'resources': tile_resources}
        if piece['id'] not in preview_audits:
            preview_audits[piece['id']] = audit_preview_tile_identity(piece, resources)
        source_records.append({'instance': identifier, 'piece_id': piece['id'],
            'dat_sha256': saved['sha256'], 'cells': len(piece['cells']),
            **preview_audits[piece['id']]})
    return result, source_records


def encoded_records(tiles):
    records = []
    for position, tile in tiles.items():
        raw = tile['resources']['path']
        lines = [line.strip() for line in raw.decode('ascii').splitlines()
                 if line.strip() and not line.lstrip().startswith('--')]
        if len(lines) >= 3 and lines[2] == '0':
            continue
        for parsed in _parse_paths(raw):
            points = []
            for point in parsed['points']:
                x, north, height = rotate(point, tile['rotation'])
                points.append(key((x+position[0], north+position[1], height)))
            metadata = {**parsed, 'instance_id': tile['instance_id']}
            records.append(((tile['instance_id'], *tile['cell']), metadata, points))
    return records


def _preserved_edge_support_vertex(point, position, tile, tiles):
    """Admit only exact inherited pier bytes inside adjacent owned cells."""
    if position not in INHERITED_EDGE_SUPPORTS:
        return False
    cell, digest = INHERITED_EDGE_SUPPORTS[position]
    west = tiles.get((position[0]-16., position[1]))
    x, height, south, u, _ = point
    if tile['piece_id'] == FAN_CORE_ID:
        core_cell, core_digest = CORE_INHERITED_EDGE_SUPPORTS[position]
        return (tile['cell'] == core_cell and tile['rotation'] == 0
                and sha256(tile['resources']['model_0']) == core_digest
                and west is not None and west['instance_id'] == tile['instance_id']
                and west['piece_id'] == FAN_CORE_ID and west['cell'] == (core_cell[0]-1, core_cell[1])
                and -8.650001 <= x < -8.00005
                and -2.650001 <= south <= -1.349999
                and 0. <= height <= 14.010672 and abs(u-.035) <= 1e-8)
    return (tile['piece_id'] == FAN_ID and tile['cell'] == cell and tile['rotation'] == 0
            and sha256(tile['resources']['model_0']) == digest
            and west is not None and west['instance_id'] == tile['instance_id']
            and west['piece_id'] == FAN_ID and west['cell'] == (cell[0]-1, cell[1])
            and -8.650001 <= x < -8.00005
            and -2.650001 <= south <= -1.349999
            and 0. <= height <= 14.010672 and abs(u-.035) <= 1e-8)


def _world_triangles(tiles, positions=None):
    from scp.models import parse_s3d
    from scp_hsr.rail_feature_verify import _triangles
    for (east, north), tile in tiles.items():
        if positions is not None and (east, north) not in positions:
            continue
        for triangle in _triangles(parse_s3d(tile['resources']['model_0'])):
            converted = []
            for x, height, south, u, v in triangle:
                require((abs(x) <= 8.00005 and abs(south) <= 8.00005)
                        or _preserved_edge_support_vertex((x, height, south, u, v),
                                                         (east, north), tile, tiles),
                        'An actual tile mesh extends beyond its independently owned city cell')
                px, py, _ = rotate((x, -south, 0.), tile['rotation'])
                converted.append((px+east, height, -py-north, u, v))
            yield tuple(converted)
