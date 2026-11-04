"""Pinned finite native sources for the first-cut diagonal DD transition.

Coordinates returned here are east, north, height, U, and V. A socket is a
complete directed traffic boundary plus its native outward peer; its source
faces remain finite indexed triangles, rather than an infinite road ribbon.
This module does not import or execute the geometry or resource writer.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
import hashlib
import math
from pathlib import Path
import struct

from scp import jsonc
from scp.dbpf import require
from scp.models import parse_s3d
from .diagonal_transition_variants import record_for
from .native import parse_paths

PATH = (0x296678F7, 0xA966883F)
S3D = (0x5AD0E817, 0xBADB57F1)
EXEMPLAR = (0x6534284A, 0x6BE08658)
TEXTURE = (0x7AB50E44, 0x1ABE787D)
DATUM = {'upper': .0010004043579101562, 'lower': .0009999275207519531}
MEASURED_CONTRACT_FILE = 'diagonal-transition-native-inputs.jsonc'
MEASURED_CONTRACT_SHA256 = 'd76c1441dc66c87b3f8c316c5f809908fd10fc9bbc0aa01a7a1eda1383037225'
RESOURCE_SHA256 = {
    (*S3D, 0x57530200): '4eb082b8329ddf70be7333f3343c4f1a621985d3992b17ca624eef79dc0ee4a8',
    (*S3D, 0x57530900): 'd319f9bb39e21e319f5ce566c5093ba9e955c4c0ed5a5dcbb703c6afe127c93a',
    (*S3D, 0x57030200): 'd413898ebd882827b8af169bc7df1eb67d1319d3a0f5fa5fea4f4ab1927673c9',
    (*S3D, 0x57030900): '5067e45f39469addc8326c1ad1a0677d0e16e3b028985acc976696586126536f',
    (*PATH, 0x57530200): 'e888625d239fe19f546f36f58bed998359440e889904fa4976c3aec355640eb1',
    (*PATH, 0x57530900): 'bd5435abd7e1f8360b3b8704eab474112330d8b7719333863e5bd264216415ce',
    (*PATH, 0x57030200): '4797ee5b6184c8e04bae9052efbdf4a5dd83f244618106770266c1a9ad2ff3c9',
    (*PATH, 0x57030900): '5bd140e491186605c518da6e16db7b01dc241adec329b0051dd750bf0b3728d5',
    (*EXEMPLAR, 0x57530200): '394c783a8fedf150c93d21701e1450a520d5c31ff59245e2d1e40ebf12889b70',
    (*EXEMPLAR, 0x57530900): 'd8c35e3673dee409fcc007c6adafcd193d50f551bffe473b70ef11c753cb63a9',
    (*EXEMPLAR, 0x57030200): '66bb78899e5d7fe22224aaf119cdcfe6959682e305771b25172dda074e641f56',
    (*EXEMPLAR, 0x57030900): '9e62e84be75389b0713b07a7dc3e350b064b0f8079ed06fff1713c293c98105d',
}
TEXTURE_SHA256 = {
    0x5703000E: 'c2b9ac53cc080ca8146f1345e13d43e91c883d9559ec3ec3293e7ff88a259e88',
    0x5713000E: '25a91179a26a82ba6307777b1957c5862bee61daf55c7638c4487d64b275c7b8',
}


@dataclass(frozen=True)
class NativeSocket:
    arm: str
    helper: tuple
    outward_peer: tuple
    coreward_source: tuple
    mouth_en: tuple
    inward_en: tuple
    joining_axis: int
    joining_coordinate: float
    outward_edge: int
    core_end_cell: tuple


def measured_contract():
    """Read fresh reviewed portable measurements, without a mutable cache."""
    path = Path(__file__).with_name(MEASURED_CONTRACT_FILE)
    raw = path.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == MEASURED_CONTRACT_SHA256,
            'Reviewed diagonal native contract changed')
    value = jsonc.loads(raw.decode('utf-8'))
    require(value.get('schema_version') == 1 and value.get('stage') == 'frozen-measured-native-inputs',
            'Unreviewed diagonal native contract stage')
    for target in (0x57530200,0x57530900,0x57030200,0x57030900):
        row = value['resources'][f'{target:08x}']
        require(row['PATH']['sha256'] == RESOURCE_SHA256[*PATH,target]
                and row['S3D']['sha256'] == RESOURCE_SHA256[*S3D,target],
                'Portable diagonal source facts disagree with native resource pins')
    return value


def socket_specs(variant='original'):
    """Select one exact first-cut socket layout, without allocating resources."""
    record = record_for(variant)
    side = 1 if record.physical_reflection else -1
    reverse = record.traffic_reversed
    dd, dd_peer = ((0x57530200, 0x57530900) if reverse else (0x57530900, 0x57530200))
    upper, upper_peer = ((0x57030200, 0x57030900) if reverse else (0x57030900, 0x57030200))
    lower, lower_peer = ((0x57030900, 0x57030200) if reverse else (0x57030200, 0x57030900))
    q = math.sqrt(.5)
    column, row = -4 + side, 5 + side
    return (
        NativeSocket('dd', (dd, 2, (1, 0)), (dd_peer, 0, (1, -1)),
                     (dd_peer, 0, (0, 0)), (8., 0.), (-q, -q), 0, 8., 2, (0, 0)),
        NativeSocket('upper', (upper, 2, (column, row)), (upper_peer, 0, (column-1, row)),
                     (upper_peer, 0, (column, row-1)),
                     (-64.+16.*side, -72.-16.*side), (q, q), 1, -72.-16.*side, 3, (column, row-1)),
        NativeSocket('lower', (lower, 2, (-4, 5)), (lower_peer, 0, (-5, 5)),
                     (lower_peer, 0, (-4, 4)), (-64., -72.), (q, q), 1, -72., 3, (-4, 4)),
    )


def resource(context, key):
    """Read one exact original resource from nested or flat audited inputs."""
    require(key in RESOURCE_SHA256, 'Unreviewed diagonal transition native resource')
    if key in context:
        raw = context[key]
    else:
        label = 'dd_rhw' if key[2] >> 16 == 0x5753 else 'rhw4'
        require(key in context.get(label, {}), 'Missing diagonal transition native input')
        raw = context[label][key]
    require(hashlib.sha256(raw).hexdigest() == RESOURCE_SHA256[key],
            'Diagonal transition native input differs from its measured source')
    return raw


def rotate_en(point, pose):
    require(type(pose) is int and pose in range(4), 'Native pose must be a proper quarter-turn')
    east, north, height = point
    for _ in range(pose):
        east, north = north, -east
    return east, north, height


def _placement(tile_id,pose,world_cell):
    require(type(tile_id) is int and (*S3D,tile_id) in RESOURCE_SHA256
            and type(pose) is int and pose in range(4)
            and isinstance(world_cell,(tuple,list)) and len(world_cell)==2
            and all(type(value) is int for value in world_cell),
            'Native diagonal placement must use one pinned tile, proper pose, and integer city cell')


def source_paths(context, tile_id, pose=0, world_cell=(0, 0)):
    """Return all real native car members, excluding pinned capacity dummies."""
    _placement(tile_id,pose,world_cell)
    if context is None:
        rows = measured_contract()['resources'].get(f'{tile_id:08x}')
        require(rows is not None, 'Unknown measured native diagonal PATH')
        decoded = [{key: row[key] for key in ('transport','lane','entry','exit','points')}
                   | {'compatibility': row['compatibility'] if row['compatibility'] is not None else 0}
                   for row in rows['PATH']['routes']]
    else:
        decoded = parse_paths(resource(context, (*PATH, tile_id)))
    dd = tile_id >> 16 == 0x5753
    routes = [row for row in decoded if not dd or row['points'][0][2] in (7.5, 15.)]
    require(len(decoded) == (6 if dd and context is not None else 4 if dd else 2) and len(routes) == (4 if dd else 2)
            and all(row['transport'] == 1 and row['compatibility'] == 0 for row in routes),
            'Native diagonal lane inventory changed')
    result = []
    for row in routes:
        value = deepcopy(row)
        value['entry'], value['exit'] = (row['entry']+pose)%4, (row['exit']+pose)%4
        value['points'] = []
        for point in row['points']:
            east, north, height = rotate_en(point, pose)
            value['points'].append((east+16.*world_cell[0], north-16.*world_cell[1], height))
        result.append(value)
    return result


def measured_profiles(arm, variant='original', *, deck):
    """Return only reviewed finite joining lines and hashed parent identities.

    Full original indexed meshes and material payloads are not distributed.
    Complete donor-parent matching requires audited original native inputs.
    """
    record_for(variant)
    key = f'{variant}:{arm}:{deck}'
    rows = measured_contract()['finite_joining_profiles'].get(key)
    require(rows is not None, 'Unknown measured finite native interface')
    return deepcopy(rows)


def source_faces(context, tile_id, pose=0, world_cell=(0, 0)):
    """Decode complete indexed original faces with their exact source UVs."""
    _placement(tile_id,pose,world_cell)
    raw = resource(context, (*S3D, tile_id))
    model = parse_s3d(raw)
    result = []
    for mesh_index, mesh in enumerate(model['meshes']):
        require(len(mesh['frames']) == 1, 'Native diagonal source must remain static')
        vi, ii, pi, mi = mesh['frames'][0]
        block = model['vertices'][vi]
        require(block['stride'] >= 20, 'Native diagonal source omits XYZUV')
        vertices = []
        for offset in range(0, len(block['data']), block['stride']):
            east, height, south, u, v = struct.unpack_from('<5f', block['data'], offset)
            east, north, height = rotate_en((east, -south, height), pose)
            vertices.append((east+16.*world_cell[0], north-16.*world_cell[1], height, u, v))
        name = mesh['name'].rstrip(b'\0').decode('ascii')
        role = 'pavement' if tile_id >> 16 == 0x5703 else {
            'Top Deck': 'pavement', 'Bottom Deck': 'pavement', 'Substructure': 'body', 'Barriers': 'barrier'}[name]
        deck = 'ground' if tile_id >> 16 == 0x5703 else ('upper' if min(p[2] for p in vertices) > 10. else 'lower')
        faces = []
        indices = model['indices'][ii]['values']
        for kind, start, count in model['primitives'][pi]:
            require(kind == 0 and count % 3 == 0, 'Native diagonal source is not a triangle list')
            faces.extend(tuple(vertices[k] for k in indices[at:at+3]) for at in range(start, start+count, 3))
        result.append({'native_tile_id': f'{tile_id:08x}', 'pose': pose, 'world_cell': tuple(world_cell),
                       'mesh_index': mesh_index, 'mesh_name': name, 'role': role, 'deck': deck,
                       'triangles': faces, 'material': deepcopy(model['materials'][mi]),
                       'source_model_sha256': hashlib.sha256(raw).hexdigest()})
    return result


def socket_faces(context, arm, variant='original', *, include_peer=True, include_coreward=False):
    sockets = [row for row in socket_specs(variant) if row.arm == arm]
    require(len(sockets) == 1, 'Unknown first-cut native socket arm')
    socket = sockets[0]
    placements = [('helper', socket.helper)]
    if include_peer:
        placements.append(('outward-peer', socket.outward_peer))
    if include_coreward:
        placements.append(('coreward-source', socket.coreward_source))
    return [{**group, 'socket_arm': arm, 'native_owner_kind': kind}
            for kind, (tile, pose, cell) in placements for group in source_faces(context, tile, pose, cell)]


def surface_fields(parent):
    """Measure a source plane and its minimal-norm in-plane affine UV fields."""
    a,b,c=parent
    first=tuple(b[i]-a[i]for i in range(3));second=tuple(c[i]-a[i]for i in range(3))
    dot=lambda x,y:sum(p*q for p,q in zip(x,y))
    aa,ab,bb=dot(first,first),dot(first,second),dot(second,second)
    determinant=aa*bb-ab*ab
    normal=(first[1]*second[2]-first[2]*second[1],first[2]*second[0]-first[0]*second[2],first[0]*second[1]-first[1]*second[0])
    length=math.sqrt(dot(normal,normal))
    require(determinant>0. and length>0.,'Native attribute parent must have a finite surface plane')
    normal=tuple(value/length for value in normal)
    fields={}
    for name,index in(('U',3),('V',4)):
        x,y=b[index]-a[index],c[index]-a[index]
        alpha,beta=(x*bb-y*ab)/determinant,(y*aa-x*ab)/determinant
        gradient=tuple(alpha*first[i]+beta*second[i]for i in range(3))
        fields[name]={'gradient_ENH':gradient,'offset':a[index]-dot(gradient,a[:3])}
    return {'source_surface_plane_ENH':{'normal':normal,'constant':dot(normal,a[:3])},'source_affine_UV_ENH':fields}


def forward_profiles(context, arm, variant='original', *, deck=None):
    """Read finite forward source edges, retaining each original XYZUV field.

    The native staircase has staggered shoulder caps. The complete forward
    boundary includes their end rings and the longer city-edge pavement
    interface, rather than replacing them with one rectangular section.
    """
    from collections import Counter
    socket = next((row for row in socket_specs(variant) if row.arm == arm), None)
    require(socket is not None, 'Unknown first-cut native profile socket')
    groups = [group for group in socket_faces(context, arm, variant)
              if deck is None or group['deck'] == deck]
    direction = (*socket.inward_en, 0.)
    dot = lambda p: sum(p[i]*direction[i] for i in range(3))
    ends = [max(dot(p) for triangle in group['triangles'] for p in triangle)
            for group in groups if group['role'] == 'pavement']
    require(ends, 'Native socket has no pavement in the requested deck')
    first_station = min(ends)
    cross = lambda a, b: (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
    result = []
    for group in groups:
        boundary = Counter(tuple(sorted((a[:3], b[:3]))) for triangle in group['triangles']
                           for a, b in zip(triangle, (*triangle[1:], triangle[0])))
        for face_index, triangle in enumerate(group['triangles']):
            normal = cross(tuple(triangle[1][i]-triangle[0][i] for i in range(3)),
                           tuple(triangle[2][i]-triangle[0][i] for i in range(3)))
            for a, b in zip(triangle, (*triangle[1:], triangle[0])):
                if boundary[tuple(sorted((a[:3], b[:3])))] != 1 or min(dot(a), dot(b)) < first_station-2e-6:
                    continue
                outward = cross(tuple(b[i]-a[i] for i in range(3)), normal)
                length = math.sqrt(sum(value*value for value in outward))
                if length < 1e-12:
                    continue
                outward = tuple(value/length for value in outward)
                alignment = sum(outward[i]*direction[i] for i in range(3))
                if abs(alignment) < 1e-7:
                    continue
                if alignment < 0.:
                    outward = tuple(-value for value in outward)
                result.append({**{key: value for key, value in group.items() if key != 'triangles'},
                               'face_index': face_index, 'parent_triangle': triangle, 'points': (a, b),
                               'plane_normal_ENH': outward,
                               'plane_station_m': sum(a[i]*outward[i] for i in range(3))})
    return result
