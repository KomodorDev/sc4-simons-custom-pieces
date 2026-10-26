"""Compose and independently audit the actual tram-under-HSR donor model.

Only this domain module knows the audited GLR/HSR donors and rail profile.
Generic S3D parsing, packing, references and validation remain in scp.models.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import struct

from scp.models import (ModelError, parse_s3d, pack_s3d, valid_frame,
                        bounds, positions, validate_s3d)


def build_crossing_model(glr_donor: bytes, hsr_donor: bytes) -> bytes:
    """Return a model with GLR along Z, elevated HSR along X, in donor coordinates.

    Expected inputs are NAM50 S3Ds 580e0700 (GLR x Monorail) and 5dd31500
    (HSR straight), group badb57f1. GLR mesh zero is the ground textured quad;
    its material and UVs are copied exactly. All original elevated Monorail
    meshes are omitted. The HSR's complete valid deck geometry is rotated
    clockwise 90 degrees around Y: (x, y, z) -> (z, y, -x). This is a proper
    rotation, so triangle winding is unchanged. No height or rail-spacing
    adjustment is made. The HSR donor has no ground-reaching support pillar.

    Five stale HSR animation meshes point outside its one-buffer arrays. They
    are discarded; the valid mesh remains byte-identical except for remapped
    references. Both donors use identical single-frame animation settings.
    """
    glr, hsr = parse_s3d(glr_donor), parse_s3d(hsr_donor)
    if glr['anim_header'] != hsr['anim_header']:
        raise ModelError('Donor animation headers differ')
    if struct.unpack_from('<H', glr['anim_header'])[0] != 1:
        raise ModelError('Only these static, one-frame donors are supported')
    # The original donors contain no matrix transforms: PROP and REGP are empty.
    if glr['trailing'] != hsr['trailing']:
        raise ModelError('Trailing donor chunks differ; transforms cannot be silently discarded')
    if any(len(raw) != 12 or raw[8:] != b'\0' * 4 for name, raw in glr['trailing']):
        raise ModelError('Unexpected non-empty donor matrix/property chunks')
    ground_meshes = [mesh for mesh in glr['meshes'] if
                     all(valid_frame(glr, frame) and
                         max(abs(value) for value in bounds(glr['vertices'][frame[0]])[1]) < 0.001
                         for frame in mesh['frames'])]
    deck_meshes = [mesh for mesh in hsr['meshes'] if all(valid_frame(hsr, frame) for frame in mesh['frames'])]
    if len(ground_meshes) != 1 or len(deck_meshes) != 1:
        raise ModelError('Unexpected donor ground/deck mesh topology')
    if bounds(hsr['vertices'][deck_meshes[0]['frames'][0][0]])[1][0] < 13:
        raise ModelError('HSR donor has ground-reaching geometry; a pillar would obstruct the tram')

    output = {'version': glr['version'], 'vertices': [], 'indices': [],
              'primitives': [], 'materials': [], 'anim_header': glr['anim_header'],
              'meshes': [], 'trailing': deepcopy(glr['trailing'])}
    for donor, meshes, rotate in ((glr, ground_meshes, False), (hsr, deck_meshes, True)):
        maps = [{}, {}, {}, {}]
        for mesh in meshes:
            out_mesh = {'name': mesh['name'], 'flags': mesh['flags'], 'frames': []}
            for frame in mesh['frames']:
                out_frame = []
                for column, array in enumerate(('vertices', 'indices', 'primitives', 'materials')):
                    source_index = frame[column]
                    if source_index not in maps[column]:
                        item = deepcopy(donor[array][source_index])
                        if array == 'vertices' and rotate:
                            raw = bytearray(item['data'])
                            for offset in range(0, len(raw), item['stride']):
                                x, y, z = struct.unpack_from('<3f', raw, offset)
                                struct.pack_into('<3f', raw, offset, z, y, -x)
                            item['data'] = bytes(raw)
                        maps[column][source_index] = len(output[array])
                        output[array].append(item)
                    out_frame.append(maps[column][source_index])
                out_mesh['frames'].append(tuple(out_frame))
            output['meshes'].append(out_mesh)
    validate_s3d(output)
    result = pack_s3d(output)
    validate_s3d(parse_s3d(result))
    return result


def audit_crossing_model(glr_donor: bytes, hsr_donor: bytes, output: bytes) -> dict:
    glr, hsr, model = map(parse_s3d, (glr_donor, hsr_donor, output))
    glr_original = glr['meshes'][0]
    ground_frame = glr_original['frames'][0]
    out_ground, out_deck = model['meshes'][0]['frames'][0], model['meshes'][1]['frames'][0]
    expected_hsr_points = [(z, y, -x) for x, y, z in positions(hsr['vertices'][0])]
    if positions(model['vertices'][out_deck[0]]) != expected_hsr_points:
        raise ModelError('HSR rotation failed to reproduce exact source coordinates')
    source_deck, result_deck = hsr['vertices'][0], model['vertices'][out_deck[0]]
    if source_deck['format'] != result_deck['format'] or source_deck['flags'] != result_deck['flags']:
        raise ModelError('HSR vertex format or flags were altered')
    for offset in range(0, len(source_deck['data']), source_deck['stride']):
        end = offset + source_deck['stride']
        if source_deck['data'][offset + 12:end] != result_deck['data'][offset + 12:end]:
            raise ModelError('HSR UVs or additional vertex attributes were altered')
    for column, array in enumerate(('vertices', 'indices', 'primitives', 'materials')):
        if model[array][out_ground[column]] != glr[array][ground_frame[column]]:
            raise ModelError(f'Ground {array} was altered')
        if array != 'vertices' and model[array][out_deck[column]] != hsr[array][0]:
            raise ModelError(f'HSR {array} was altered')
    return {
        'donors': {'ground': '5ad0e817-badb57f1-580e0700',
                   'hsr': '5ad0e817-badb57f1-5dd31500'},
        'sha256': {'ground_donor': hashlib.sha256(glr_donor).hexdigest(),
                   'hsr_donor': hashlib.sha256(hsr_donor).hexdigest(),
                   'crossing': hashlib.sha256(output).hexdigest()},
        'output_bytes': len(output),
        'geometry': {
            'ground': 'Original ground quad, UVs, material and texture preserved exactly.',
            'hsr': 'Entire valid straight HSR deck rotated (x,y,z) -> (z,y,-x). Height/UVs unchanged.',
            'removed': 'All elevated Monorail meshes; five dangling HSR animation mesh records.',
            'support_clearance_m': bounds(model['vertices'][out_deck[0]])[1][0],
            'pillar': 'No ground-reaching pillar exists in the selected HSR donor.',
            'alignment': 'GLR runs north/south (Z); HSR east/west (X), matching unrotated 580e0700 paths.',
        },
        'retained_exactly': ['Ground vertices and UVs', 'Ground index and primitive buffers',
                             'HSR index and primitive buffers', 'Both used raw material records',
                             'UV coordinates of HSR vertices', 'Animation header, mesh names and flags',
                             'Empty PROP and REGP chunks (no donor matrix transforms exist)'],
        'discarded_invalid_hsr_meshes': [
            {'name': mesh['name'].rstrip(b'\0').decode('ascii', 'replace'),
             'frames': mesh['frames']}
            for mesh in hsr['meshes'] if not all(valid_frame(hsr, frame) for frame in mesh['frames'])],
        'donor_chunk_length_anomalies': {
            'ground': [item for item in glr['source_chunk_lengths'] if item['declared'] != item['actual']],
            'hsr': [item for item in hsr['source_chunk_lengths'] if item['declared'] != item['actual']]},
        'checks': validate_s3d(model),
        'verification_limit': 'Binary geometry/reference audit only; no in-game rendering or traffic test.',
    }

