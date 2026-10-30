"""Inspect the actual Avenue texture, PATH, and T21 layers independently.

The canonical saved models remain the approved geometric reference. This
module never imports their generator or the runtime-layer writer. It proves
that the resources selected by the game retain that reference's traffic and
all surfaces except the explicitly identified native Avenue ground meshes.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import re

from scp.adaptive_network import bindings, fixed_cells, validate_active_resources
from scp.dbpf import exemplar, require
from scp.models import parse_s3d, positions, validate_s3d
from scp.track_paths import PATH, S3D
from scp.verify import parse_paths

AVENUE_PATH = (0x296678F7, 0x69668828)
TEXTURE = (0x7AB50E44, 0x1ABE787D)
PROP = (0x6534284A, 0xC977C536)
GROUND_NAMES = {b'Avenue', b'SCP opened Avenue'}
GROUND_MATERIALS = {0x0400020E, 0x0400380E}
# Independently reviewed world construction origins, not layout generation.
ORIGINS = {'access-core': (-1, -1), 'northwest-junction': (-2, -2),
           'southeast-junction': (1, 1)}
CAPTURE_SHA256 = '6ed51e2a9188826f188516fc0be7004069b2eb11f02ad0a62d271672194af839'


@lru_cache(maxsize=1)
def _texture_hashes():
    path = (Path(__file__).resolve().parents[2] / '01_assemblies' /
            'ddrhw-l1-and-l2-diagonal-avenue-diamond/evidence/adaptive-avenue-capture-audit.json')
    audit = json.loads(path.read_text(encoding='utf-8'))
    require(audit.get('schema_version') == 1 and audit.get('capture_kind') == 'resource-bundle'
            and audit.get('capture', {}).get('sha256') == CAPTURE_SHA256,
            'Adaptive Avenue input audit differs from the reviewed capture')
    result = {}
    for source in audit['sources']:
        for row in source['resources']:
            key = tuple(int(value, 16) for value in row['tgi'].split('-'))
            if key[:2] == TEXTURE:
                require(key not in result, 'Duplicate audited Avenue texture')
                result[key] = row['decompressed_resource_sha256']
    expected = {(*TEXTURE, donor + offset + zoom)
                for donor in (0x04000200, 0x04003800)
                for offset in (0, 0x10, 0x20, 0x30) for zoom in range(5)}
    require(result.keys() == expected, 'Adaptive Avenue audit must contain all forty native textures')
    return result


def _mesh_signature(model, mesh):
    frames = []
    for frame in mesh['frames']:
        frames.append(tuple(model[array][index] for array, index in
                            zip(('vertices', 'indices', 'primitives', 'materials'), frame)))
    return mesh['name'], mesh['flags'], frames


def _retained_meshes(model):
    retained, removed = [], []
    for mesh in model['meshes']:
        if mesh['name'].rstrip(b'\0') not in GROUND_NAMES:
            retained.append(mesh)
            continue
        for vi, _ii, _pi, mi in mesh['frames']:
            require(all(point[1] == 0.0 for point in positions(model['vertices'][vi])),
                    'Adaptive removal includes an elevated native Avenue mesh')
            textures = model['materials'][mi]['textures']
            require(textures and set(textures) <= GROUND_MATERIALS,
                    'Adaptive removal includes a non-native Avenue material')
        removed.append(mesh)
    require(removed, 'Adaptive canonical cell has no measured native Avenue ground mesh')
    return retained, removed


def _route_signature(route, turns=0):
    points = []
    for east, north, height in route['points']:
        for _ in range(turns % 4):
            east, north = north, -east
        points.append((round(east, 9), round(north, 9), round(height, 9)))
    return (route['transport'], route['lane'], (route['entry'] + turns) % 4,
            (route['exit'] + turns) % 4, route['compatibility'], tuple(points))


def check_resources(resources, piece):
    """Prove the saved runtime layers preserve geometry and all actual routes."""
    rows = bindings(piece)
    if not rows:
        return {'adaptive_cells_checked': 0, 'game_behavior_tested': False}
    validate_active_resources(resources, piece)
    key = piece.get('geometry_key')
    require(key in ORIGINS, 'Adaptive highway cells need a reviewed module origin')
    origin = ORIGINS[key]
    required_cells = {tuple(cell) for cell in piece['cells']
                      if cell[0] + origin[0] - cell[1] - origin[1] in (-1, 0, 1)}
    require({tuple(row['cell']) for row in rows} == required_cells,
            'Adaptive metadata must cover every and only the module Avenue cells')
    texture_hashes = _texture_hashes()
    route_count = retained_count = removed_count = props = 0
    for row in rows:
        cell = row['cell']
        difference = cell[0] + origin[0] - cell[1] - origin[1]
        donor = 0x04003800 if difference == 0 else 0x04000200
        rotation = 2 if difference == 1 else 0
        avenue = {0: 0x01030103, 1: 0x01000003, -1: 0x00030100}[difference]
        require(int(row['texture_donor_id'], 16) == donor and row['rotation'] == rotation
                and int(row['avenue_flags'], 16) == avenue,
                'Adaptive texture donor, pose, or Avenue flags differ from measured native channels')
        tile, resolved = int(row['canonical_tile_id'], 16), int(row['resolved_tile_id'], 16)
        for offset in (0, 0x10, 0x20, 0x30):
            for zoom in range(5):
                actual = resources[*TEXTURE, resolved + offset + zoom]
                require(hashlib.sha256(actual).hexdigest() == texture_hashes[*TEXTURE, donor + offset + zoom],
                        'Adaptive ground texture differs from its audited appearance and zoom donor')
        canonical = parse_paths(resources[*PATH, tile])
        active = parse_paths(resources[*AVENUE_PATH, resolved])
        require(canonical['version'] == active['version'] and canonical['terrain'] == active['terrain']
                and Counter(_route_signature(route) for route in canonical['routes']) ==
                Counter(_route_signature(route, rotation) for route in active['routes']),
                'Resolved Avenue PATH does not preserve every posed ground, highway, and ramp route')
        # Applying a whole-piece turn must preserve the same equality, rather
        # than checking only an unrotated first lane or dropping junction bits.
        for turns in range(1, 4):
            require(Counter(_route_signature(route, turns) for route in canonical['routes']) ==
                    Counter(_route_signature(route, turns + rotation) for route in active['routes']),
                    'Adaptive PATH pose fails a proper whole-piece rotation')
        route_count += len(canonical['routes'])
        model = parse_s3d(resources[*S3D, tile])
        retained, removed = _retained_meshes(model)
        require(row['prop'] == bool(retained), 'Adaptive prop declaration omits or invents retained road geometry')
        removed_count += len(removed)
        if not retained:
            continue
        overlay = parse_s3d(resources[*S3D, tile + 5])
        validate_s3d(overlay)
        require(all(overlay[name] == model[name] for name in ('version', 'anim_header', 'trailing'))
                and len(overlay['meshes']) == len(retained)
                and [_mesh_signature(overlay, mesh) for mesh in overlay['meshes']] ==
                [_mesh_signature(model, mesh) for mesh in retained],
                'Adaptive prop changes retained deck, ramp-mouth, slip-lane, or support geometry')
        properties = {int(prop['id'], 16): prop for prop in exemplar(resources[*PROP, tile])['properties']}
        size = properties.get(0x27812810, {}).get('values', [])
        points = [point for mesh in overlay['meshes'] for frame in mesh['frames']
                  for point in positions(overlay['vertices'][frame[0]])]
        require(len(size) == 3 and all(math.isfinite(value) and value > 0 for value in size)
                and size[0] + 1e-5 >= 2 * max(abs(point[0]) for point in points)
                and size[2] + 1e-5 >= 2 * max(abs(point[2]) for point in points)
                and size[1] + 1e-5 >= max(point[1] for point in points),
                'Adaptive prop occupied size clips its retained roadway or supports')
        retained_count += len(retained)
        props += 1
    return {'active_layer_verified': True,
            'adaptive_cells_checked': len(rows), 'texture_resources_checked': 20 * len(rows),
            'posed_merged_path_routes_checked': route_count, 'proper_rotations_checked': 4,
            'props_checked': props, 'retained_meshes_checked': retained_count,
            'native_ground_meshes_removed': removed_count,
            'canonical_geometry_and_traffic_preserved': True,
            'coverage_limit': 'Saved binding, texture, PATH, and exact retained-buffer checks; no game placement, network joins, sidewalk selection, or traffic observation.',
            'game_behavior_tested': False}


def check_construction_fields(fields, piece, resources):
    """Check the hybrid FLEX/fixed ownership without calling its author."""
    rows = bindings(piece)
    require(rows, 'Adaptive construction verification needs explicit bindings')
    key = piece.get('geometry_key')
    require(key in ORIGINS, 'Adaptive construction has no reviewed module origin')
    by_cell = {tuple(row['cell']): row for row in rows}
    width, depth = piece['footprint']
    expected = [['.'] * (width + 2) for _ in range(depth + 1)]
    expected[0][-1], expected[-1][0] = '<', '^'
    cons = [list(row) for row in expected]
    checks = []
    from .ramp_verify import _road_word
    origin = ORIGINS[key]
    for index, (cell, identifier) in enumerate(zip(piece['cells'], piece['tile_ids'])):
        letter = chr(ord('a') + index)
        expected[cell[1]][cell[0]] = letter
        if tuple(cell) in by_cell:
            row = by_cell[tuple(cell)]
            checks.append(f"{letter} - street: 0x{row['street_flags'].upper()} "
                          f"avenue: 0x{row['avenue_flags'].upper()}, 0xFFFFFFFF optional")
            continue
        saved = parse_paths(resources[*PATH, int(identifier, 16)])['routes']
        world = cell[0] + origin[0], cell[1] + origin[1]
        road = [route for route in saved if route['points'][0][2] != 0.0 or route['points'][-1][2] != 0.0]
        road += [route for route in saved if route['transport'] == 1 and route['compatibility']]
        if sum(world) not in (0, 1) and not road:
            road = saved
        checks.append(f'{letter} - dirtroad: 0x{_road_word(road):08X}')
        cons[cell[1]][cell[0]] = '+'
    if not fixed_cells(piece):
        expected[0][width] = 'Z'
        cons[0][width] = '+'
        checks.append('Z - road: 0x02000200')
    # Hex case is immaterial, but symbol case and every field remain exact.
    normalize = lambda line: re.sub(r'0x[0-9a-fA-F]+', lambda match: match[0].upper(), line)
    require(fields.get('CellLayout') == [''.join(row) for row in expected]
            and fields.get('ConsLayout') == [''.join(row) for row in cons]
            and [normalize(line) for line in fields.get('CheckType', [])] ==
            [normalize(line) for line in checks],
            'Adaptive construction changes tile ownership, optional Avenue flags, or real static cells')
    require(fields.get('Costs') == ['1000'], 'Unexpected adaptive highway construction cost')
    return {'adaptive_cells_checked': len(rows), 'static_cells_checked': len(fixed_cells(piece)),
            'temporary_handle_required': not bool(fixed_cells(piece)),
            'hybrid_construction_checked': True, 'game_behavior_tested': False}
