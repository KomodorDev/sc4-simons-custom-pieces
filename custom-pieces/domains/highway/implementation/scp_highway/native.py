"""Measured DD RHW-4 and Avenue channels, composed without RUL2 rewrites.

The draggable A300/A305 crossing resources contain separate highway and
avenue channels. Their native RUL2 neighbourhood is not a placeable RUL0
family. We reuse those channels independently in an explicit five-cell
cross, rather than relabelling an unresolved RUL2 neighbourhood.
"""
from __future__ import annotations

from copy import deepcopy
import struct

from scp.dbpf import require
from scp.models import parse_s3d, pack_s3d, validate_s3d
from scp.recipes import combine_meshes
from scp.track_paths import PATH, S3D

RECIPE = 'highway_ddrhw_diagonal_avenue_crossing'
CELLS = ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2))
# (cell, DD donor, DD proper rotation, Avenue donor, Avenue proper rotation)
PARTS = (
    ((1, 0), None, 0, 0x5753A300, 0),
    ((0, 1), None, 0, 0x5753A300, 2),
    ((1, 1), 0x5753A380, 0, 0x5753A305, 0),
    ((2, 1), 0x5753A300, 2, 0x5753A300, 0),
    ((1, 2), 0x5753A300, 2, 0x5753A300, 2),
)


def parse_paths(raw):
    """Read native 1.1/1.2 traffic without inventing transport metadata."""
    lines = [line.strip() for line in raw.decode('ascii').splitlines()
             if line.strip() and not line.lstrip().startswith('--')]
    require(len(lines) >= 5 and lines[:2] in (['SC4PATHS', '1.1'], ['SC4PATHS', '1.2']),
            'Unsupported native highway PATH header')
    require(lines[3:5] == ['0', '0'], 'Native crossing requires flat zero-stop PATH data')
    fields, cursor, routes = (6 if lines[1] == '1.2' else 5), 5, []
    for _ in range(int(lines[2])):
        metadata = list(map(int, lines[cursor:cursor + fields])); cursor += fields
        require(len(metadata) == fields and metadata[-1] >= 2, 'Truncated native PATH metadata')
        points = [tuple(map(float, line.split(','))) for line in lines[cursor:cursor + metadata[-1]]]
        cursor += metadata[-1]
        require(len(points) == metadata[-1] and all(len(point) == 3 for point in points), 'Truncated native PATH')
        routes.append({'transport': metadata[0], 'lane': metadata[1], 'entry': metadata[2],
                       'exit': metadata[3], 'compatibility': metadata[4] if fields == 6 else 0,
                       'points': points})
    require(cursor == len(lines), 'Unexpected trailing native PATH data')
    return routes


def rotate_route(route, turns):
    out = deepcopy(route)
    for field in ('entry', 'exit'):
        out[field] = (out[field] + turns) % 4
    points = []
    for x, y, z in route['points']:
        for _ in range(turns % 4):
            x, y = y, -x
        points.append((x, y, z))
    out['points'] = points
    return out


def encode_paths(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for n, route in enumerate(routes):
        lines += [f'-- SCP native highway channel {n + 1}', str(route['transport']), str(route['lane']),
                  str(route['entry']), str(route['exit']), str(route['compatibility']), str(len(route['points']))]
        lines += [','.join(format(v, '.9g') for v in point) for point in route['points']]
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


def rotate_model(model, turns):
    """Rotate complete native vertex buffers; UVs and triangle order remain exact."""
    result = deepcopy(model)
    for vb in result['vertices']:
        raw = bytearray(vb['data'])
        for offset in range(0, len(raw), vb['stride']):
            x, height, z = struct.unpack_from('<3f', raw, offset)
            for _ in range(turns % 4):
                x, z = -z, x
            struct.pack_into('<3f', raw, offset, x, height, z)
        vb['data'] = bytes(raw)
    return result


def channels(dd_resources, donor, avenue, turns):
    model = parse_s3d(dd_resources[*S3D, donor])
    meshes = [mesh for mesh in model['meshes']
              if (mesh['name'].rstrip(b'\0') == b'Avenue') == avenue]
    require(len(meshes) == (1 if avenue else 6), 'Native crossing channel mesh inventory changed')
    selected = combine_meshes([(model, meshes, (0., 0., 0.))])
    paths = [route for route in parse_paths(dd_resources[*PATH, donor])
             if (route['points'][0][2] == 0) == avenue]
    require(len(paths) == ((6 if donor == 0x5753A305 else 3) if avenue else 4),
            'Native crossing channel PATH inventory changed')
    return rotate_model(selected, turns), [rotate_route(route, turns) for route in paths]


def build_crossing_channels(context):
    dd, result = context['dd_rhw'], []
    for cell, highway, highway_turns, avenue, avenue_turns in PARTS:
        models, routes = [], []
        if highway is not None:
            model, paths = channels(dd, highway, False, highway_turns)
            models.append((model, model['meshes'], (0., 0., 0.))); routes.extend(paths)
        model, paths = channels(dd, avenue, True, avenue_turns)
        models.append((model, model['meshes'], (0., 0., 0.))); routes.extend(paths)
        model = combine_meshes(models)
        validate_s3d(model)
        result.append((cell, pack_s3d(model), encode_paths(routes)))
    return result


def material_template(context):
    """Return the audited opaque native deck material for authored road ribbons."""
    model = parse_s3d(context['dd_rhw'][*S3D, 0x5753A380])
    mesh = next(mesh for mesh in model['meshes'] if mesh['name'].rstrip(b'\0') == b'Top Deck')
    return deepcopy(model['materials'][mesh['frames'][0][3]])
