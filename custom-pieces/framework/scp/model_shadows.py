"""Explicit native prop shadows that retain per-module geometric overhang.

This resource contract is opt-in. It does not select elevated triangles or
infer a shadow from a traffic PATH. The owning domain supplies independently
reviewed four-pose carrier models and their alpha textures. Fixed and adaptive
network cells select these props through ordinary network-lot configurations.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import math
import re
import struct

from .adaptive_network import bindings as adaptive_bindings
from .dbpf import encode_exemplar, exemplar, require
from .models import parse_s3d, positions, validate_s3d

MODE = 'model-carrier'
S3D = (0x5AD0E817, 0xBADB57F1)
TEXTURE = (0x7AB50E44, 0x1ABE787D)
SHADOW = (0x7AB50E44, 0x2BC2759A)
PROP = (0x6534284A, 0xC977C536)
T21 = (0x6534284A, 0x89AC5643)
SUN_PROFILE = 'sc4-default-67p5-45'
LIGHTING_EXEMPLAR = (0x6534284A, 0xA9189CF0, 0x00000001)
LIGHTING_SHA256 = '14e29418b419fd89f4f06f697f8137f4ce933157be9b63d0260a743e19098ced'


def _hex(value, label):
    require(isinstance(value, str) and re.fullmatch(r'[0-9a-fA-F]{8}', value),
            label + ' must contain exactly eight hexadecimal digits')
    return int(value, 16)


def bindings(piece):
    """Return every declared cell, with exact selected native resource keys."""
    if piece.get('shadow_mode') != MODE:
        require('model_shadows' not in piece, 'Model shadows require their explicit shadow mode')
        return []
    require(piece.get('shadow_mappings') == [], 'Model carriers must not retain clipped network shadow mappings')
    metadata = piece.get('model_shadows')
    require(isinstance(metadata, dict) and set(metadata) in (
                {'schema_version', 'sun_profile', 'cells'},
                {'schema_version', 'sun_profile', 'cells', 'enabled'})
            and type(metadata['schema_version']) is int and metadata['schema_version'] == 1,
            'Unsupported model-shadow metadata')
    require(type(metadata.get('enabled', True)) is bool,
            'Model-shadow enabled setting must be a boolean')
    require(metadata['sun_profile'] == SUN_PROFILE, 'Unsupported model-shadow sunlight profile')
    width, depth = piece['footprint']
    cells = piece.get('cells', [[x, y] for y in range(depth) for x in range(width)])
    rows = metadata['cells']
    require(isinstance(rows, list) and len(rows) == len(cells) and rows,
            'Model-shadow declarations must cover every owned cell')
    adaptive = {tuple(row['cell']): row for row in adaptive_bindings(piece)}
    base = int(piece['tile_ids'][0], 16) - cells[0][0] * 0x100 - cells[0][1] * 0x10
    result = []
    for index, (row, cell, tile_text) in enumerate(zip(rows, cells, piece['tile_ids'])):
        require(isinstance(row, dict) and type(row.get('cast_shadow')) is bool,
                'Model-shadow cast setting must be a boolean')
        fields = {'cell', 'cast_shadow'} | ({'resource_base'} if row['cast_shadow'] else set())
        require(set(row) == fields and row['cell'] == cell and
                isinstance(row['cell'], list) and len(row['cell']) == 2 and
                all(type(value) is int for value in row['cell']),
                'Model-shadow cells must retain the complete declared ownership order')
        item = deepcopy(row)
        item['canonical_tile_id'] = tile_text
        host = adaptive.get(tuple(cell))
        item['t21_id'] = host['resolved_tile_id'] if host else tile_text
        item['rotation'] = (-host['rotation']) % 4 if host else 0
        item['lot_property'] = 0x88EDC901 if host and host['prop'] else 0x88EDC900
        item['adaptive'] = host is not None
        if row['cast_shadow']:
            family = _hex(row['resource_base'], 'Model-shadow resource base')
            require(family == base + 0x800 + index * 0x100 and
                    family & 0xFF == 0 and family & 0xFFFFF000 == base & 0xFFFFF000,
                    'Model-shadow family must use its reserved canonical-block cell slot')
            item.update(model_ids=list(range(family, family + 4)),
                        texture_ids=list(range(family + 0x10, family + 0x14)),
                        prop_id=family + 4)
        result.append(item)
    return result


def enabled(piece):
    """Keep permanent carrier reservations separate from current generation."""
    return bool(bindings(piece)) and piece['model_shadows'].get('enabled', True)


def allocation_fields(piece):
    return {'shadow_resource_families': [row['resource_base'] for row in bindings(piece)
                                         if row['cast_shadow']]}


def reservation_ids(record):
    values = record.get('shadow_resource_families', [])
    require(isinstance(values, list), 'Shadow resource-family allocations must be a list')
    result = []
    for value in values:
        base = _hex(value, 'Allocated shadow resource family')
        require(base & 0xFF == 0, 'Shadow resource families must reserve aligned 256-ID ranges')
        result.extend(range(base, base + 0x100))
    require(len(result) == len(set(result)), 'Shadow resource-family allocation overlap')
    return result


def resource_keys(piece):
    keys = set()
    if not enabled(piece):
        return keys
    for row in bindings(piece):
        if row['cast_shadow']:
            keys.update((*S3D, iid) for iid in row['model_ids'])
            keys.update((*TEXTURE, iid) for iid in row['texture_ids'])
            keys.update({(*PROP, row['prop_id']), (*T21, int(row['t21_id'], 16))})
    return keys


def audit_lighting_dependency(context, installed, pieces):
    """Reject a different captured light or a competing installed override."""
    selected = [piece for piece in pieces if enabled(piece)]
    if not selected:
        return {'model_shadow_lighting_required': False}
    for piece in selected:
        bindings(piece)
        require('model_shadow_lighting' in piece.get('dependencies', []),
                'Model carriers must declare their exact lighting dependency')
    capture = context.get('model_shadow_lighting', {})
    require(LIGHTING_EXEMPLAR in capture and
            hashlib.sha256(capture[LIGHTING_EXEMPLAR]).hexdigest() == LIGHTING_SHA256,
            'Model-shadow lighting capture differs from the supported native sunlight profile')
    require(len(installed.get(LIGHTING_EXEMPLAR, [])) == 1,
            'Model-shadow sunlight has a missing or competing installed lighting override')
    return {'model_shadow_lighting_required': True, 'sun_profile': SUN_PROFILE,
            'lighting_sha256': LIGHTING_SHA256, 'competing_lighting_overrides': 0}


def _property(pid, kind, values, *, array=False):
    return {'id': f'0x{pid:08x}', 'type': f'0x{kind:04x}',
            'key_type': '0x0080' if array else '0x0000', 'values': values,
            'repetitions': len(values) if array else None}


def _properties(raw, kind):
    record = exemplar(raw)
    props = {int(prop['id'], 16): prop for prop in record['properties']}
    require(len(props) == len(record['properties']) and record['parent'] == [0, 0, 0]
            and props.get(0x10, {}).get('values') == [kind],
            'Invalid or inherited model-shadow exemplar')
    return record, props


def _size(models):
    points = [point for raw in models for block in parse_s3d(raw)['vertices'] for point in positions(block)]
    require(points and all(math.isfinite(value) for point in points for value in point),
            'Model-shadow geometry must have finite, nonempty bounds')
    return [max(0.01, 2 * max(abs(point[0]) for point in points)),
            max(0.01, max(0., max(point[1] for point in points)) - min(0., min(point[1] for point in points))),
            max(0.01, 2 * max(abs(point[2]) for point in points))]


def _check_carrier_model(model):
    require(all(tag in (b'PROP', b'REGP') and len(chunk) == 12 and chunk[8:] == b'\0' * 4
                for tag, chunk in model['trailing']),
            'Model carrier cannot ignore nonempty or unknown model transforms')
    require(len(model['meshes']) == 1 and all(len(model[name]) == 1 for name in
            ('vertices', 'indices', 'primitives', 'materials')) and
            model['meshes'][0]['frames'] == [(0, 0, 0, 0)],
            'Model carrier must retain one static four-corner mesh')
    block = model['vertices'][0]
    points = positions(block)
    require(block['format'] == 0x80004001 and block['stride'] == 20 and len(points) == 4,
            'Model carrier needs four native packed XYZ/UV vertices')
    vertices = [struct.unpack_from('<5f', block['data'], index * 20) for index in range(4)]
    require(tuple(point[3:] for point in vertices) == ((0., 0.), (1., 0.), (1., 1.), (0., 1.))
            and tuple(point[1] for point in points) == (0., 64., 64., 0.),
            'Model carrier must retain its 64-metre invisible slanted shadow quad')
    # This is the independently transcribed native local-light contract, not
    # a call back into the model writer being checked.
    local_sun = (-0.27059805393218994, -0.7071067690849304, -0.6532814502716064)
    projected = [(x - y * local_sun[0] / local_sun[1], z - y * local_sun[2] / local_sun[1])
                 for x, y, z in points]
    p0, p1, p2, p3 = projected
    require(p0[0] < p1[0] and p0[1] < p3[1] and
            max(abs(p0[1] - p1[1]), abs(p1[0] - p2[0]),
                abs(p2[1] - p3[1]), abs(p3[0] - p0[0])) <= 1e-4,
            'Model carrier projection is not its affine rectangular alpha mask')
    indices = model['indices'][0]['values']
    for _kind, first, count in model['primitives'][0]:
        for at in range(first, first + count, 3):
            a, b, c = (points[index] for index in indices[at:at + 3])
            ab, ac = [b[i] - a[i] for i in range(3)], [c[i] - a[i] for i in range(3)]
            cross = (ab[1] * ac[2] - ab[2] * ac[1], ab[2] * ac[0] - ab[0] * ac[2],
                     ab[0] * ac[1] - ab[1] * ac[0])
            require(sum(value * value for value in cross) <= 1e-16,
                    'Model carrier contains visible nondegenerate triangles')


def _prop(row, models, title):
    # Native RKT2 order is five zoom-major rows of four relative model poses.
    # The helper deliberately omits E83A081D, which would add another rotation.
    props = [_property(0x10, 0x300, [30]), _property(0x20, 0xC00, title, array=True),
             _property(0x21, 0x300, [row['prop_id']]), _property(0x0ABFC024, 0x300, [31]),
             _property(0x27812810, 0x900, _size(models), array=True),
             _property(0x27812822, 0x300, [*S3D, *(row['model_ids'] * 5)], array=True),
             _property(0x8A5E5DB8, 0xB00, [1]), _property(0x029244DB, 0xB00, [0]),
             _property(0x29F013E6, 0xB00, [1]),
             _property(0x69F14D33, 0xB00, [0]), _property(0xE9A316EB, 0x100, [0])]
    return encode_exemplar({'parent': [0, 0, 0], 'properties': props})


def _lot(row):
    host = int(row['t21_id'], 16)
    return [1, 0, row['rotation'], 0x80000, 0, 0x80000,
            0, 0, 0xFFFFF, 0xFFFFF, 0, host, row['prop_id']]


def _t21(row, title, existing=None):
    host = int(row['t21_id'], 16)
    if existing is not None:
        record, props = _properties(existing, 0x21)
        require(row['lot_property'] not in props, 'Shadow carrier would replace an existing network-lot object')
        require(props.get(0xC9A5A1BE, {}).get('values') == [host],
                'Shadow carrier T21 decorates the wrong actual network host')
    else:
        require(row['lot_property'] == 0x88EDC900, 'Shadow carrier is missing its retained adaptive T21')
        values = [(0x10, 0x300, [0x21], False), (0x20, 0xC00, title, True),
                  (0x21, 0x300, [host], False), (0x49D55951, 0x100, [15] * 4, True),
                  (0x88EDC789, 0x100, [2], False), (0x88EDC793, 0x100, list(range(16)), True),
                  (0x88EDC795, 0x100, list(range(4)), True), (0xAA120972, 0x900, [0.], False),
                  (0xAA120973, 0x900, [64.], False), (0xC9A5A1BE, 0x300, [host], False),
                  (0xCA81B8D4, 0x100, [4], False), (0xCC3E4755, 0x100, [2], False),
                  (0xEC3BD470, 0x100, [15], False)]
        record = {'parent': [0, 0, 0], 'properties': [
            _property(pid, kind, value, array=array) for pid, kind, value, array in values]}
    record['properties'].append(_property(row['lot_property'], 0x300, _lot(row), array=True))
    return encode_exemplar(record)


def add_resources(resources, piece, carriers_by_cell):
    """Add actual domain-compiled carriers after ordinary active layers exist."""
    if not enabled(piece):
        require(not carriers_by_cell, 'Disabled model shadows must not compile carriers')
        if piece.get('shadow_mode') == MODE:
            validate_resources(resources, piece)
        return resources
    rows = [row for row in bindings(piece) if row['cast_shadow']]
    require(set(carriers_by_cell) == {tuple(row['cell']) for row in rows},
            'Compiled shadow carriers must cover exactly the declared elevated hosts')
    for row in rows:
        carrier = carriers_by_cell[tuple(row['cell'])]
        models, textures = carrier['models'], carrier['textures']
        require(len(models) == 4 and all(isinstance(raw, bytes) for raw in models)
                and set(textures) == set(row['texture_ids']) and all(isinstance(raw, bytes) for raw in textures.values()),
                'Shadow carrier needs four real models and its four declared textures')
        extra = {(*S3D, iid): raw for iid, raw in zip(row['model_ids'], models)}
        extra.update({(*TEXTURE, iid): raw for iid, raw in textures.items()})
        title = 'SCP | ' + piece.get('name', piece.get('id', 'network')) + f' shadow carrier {tuple(row["cell"])}'
        extra[*PROP, row['prop_id']] = _prop(row, models, title)
        require(not extra.keys() & resources.keys(), 'Shadow resources overlap retained piece artwork or traffic')
        hostkey = (*T21, int(row['t21_id'], 16))
        resources.update(extra)
        resources[hostkey] = _t21(row, title, resources.get(hostkey))
    validate_resources(resources, piece)
    return resources


def validate_resources(resources, piece):
    """Check encoded native bindings without importing the carrier generator."""
    rows = bindings(piece)
    if not rows:
        return {'carrier_hosts_checked': 0, 'game_shadow_selection_tested': False}
    if not enabled(piece):
        reserved = set(reservation_ids(allocation_fields(piece)))
        require(not any(key[2] in reserved for key in resources),
                'Disabled model shadows retain a reserved carrier resource')
        require(not {(*SHADOW, int(tile, 16) + zoom) for tile in piece['tile_ids']
                     for zoom in range(5)} & resources.keys(),
                'Disabled model shadows retain clipped network shadow FSH resources')
        for row in rows:
            key = (*T21, int(row['t21_id'], 16))
            if key not in resources:
                continue
            lotprops = exemplar(resources[key])['properties']
            require(not any(type(value) is int and value in reserved
                            for prop in lotprops for value in prop.get('values', [])),
                    'Disabled model shadows retain a T21 carrier reference')
        return {'carrier_hosts_checked': 0, 'model_resources_checked': 0,
                'owned_alpha_textures_checked': 0, 'texture_ids': [],
                'shadow_generation_disabled': True,
                'permanent_reserved_resource_ids_checked': len(reserved),
                'retained_shadow_resources': 0, 'retained_t21_carrier_references': 0,
                'game_shadow_selection_tested': False}
    require(resource_keys(piece) <= resources.keys(), 'Model carrier has missing model, texture, prop, or T21 resources')
    require(not {(*SHADOW, int(tile, 16) + zoom) for tile in piece['tile_ids'] for zoom in range(5)} & resources.keys(),
            'Model carriers must not retain their clipped network shadow FSH resources')
    textures_checked = set()
    for row in rows:
        if not row['cast_shadow']:
            continue
        _record, props = _properties(resources[*PROP, row['prop_id']], 30)
        forbidden = {0x27812820, 0x27812821, 0x27812823, 0x27812824, 0x27812825, 0xE83A081D, 0xE9822D62}
        require(not forbidden & props.keys(), 'Model carrier has a competing model key or extra geometry rotation')
        expected = {0x21: (0x300, 0, [row['prop_id']]), 0x0ABFC024: (0x300, 0, [31]),
                    0x27812822: (0x300, 0x80, [*S3D, *(row['model_ids'] * 5)]),
                    0x8A5E5DB8: (0xB00, 0, [1]), 0x029244DB: (0xB00, 0, [0]),
                    0x29F013E6: (0xB00, 0, [1]), 0x69F14D33: (0xB00, 0, [0])}
        require(all(int(props.get(pid, {}).get('type', '0'), 16) == kind
                    and int(props.get(pid, {}).get('key_type', '0'), 16) == keytype
                    and props.get(pid, {}).get('values') == values for pid, (kind, keytype, values) in expected.items()),
                'Model carrier native model, shadow, or collision-isolation contract differs')
        models = [resources[*S3D, iid] for iid in row['model_ids']]
        size = props.get(0x27812810, {})
        expected_size = _size(models)
        require(size.get('type') == '0x0900' and size.get('key_type') == '0x0080'
                and len(size.get('values', [])) == 3 and all(math.isfinite(value) and value + 1e-5 >= minimum
                for value, minimum in zip(size['values'], expected_size)),
                'Model carrier occupied dimensions clip its shadow geometry')
        for raw, texture in zip(models, row['texture_ids']):
            model = parse_s3d(raw)
            validate_s3d(model)
            _check_carrier_model(model)
            require(len(model['meshes']) == 1 and len(model['materials']) == 1
                    and model['materials'][0]['textures'] == [texture],
                    'Model carrier must have one mesh and its exact declared alpha texture')
            from .preview import decode_fsh
            image = decode_fsh(resources[*TEXTURE, texture])
            require(image.mode == 'RGBA' and 0 < image.width <= 512 and 0 < image.height <= 512
                    and image.getchannel('A').getbbox() is not None,
                    'Model carrier needs a nonempty bounded alpha shadow texture')
            textures_checked.add(texture)
        _record, lotprops = _properties(resources[*T21, int(row['t21_id'], 16)], 0x21)
        expected_lot = {0x21: [int(row['t21_id'], 16)], 0xC9A5A1BE: [int(row['t21_id'], 16)],
                        0xEC3BD470: [15], 0xCA81B8D4: [4], 0xCC3E4755: [2],
                        0x88EDC789: [2], 0x49D55951: [15] * 4, 0x88EDC793: list(range(16)),
                        0x88EDC795: list(range(4)), row['lot_property']: _lot(row)}
        require(all(lotprops.get(pid, {}).get('values') == values for pid, values in expected_lot.items()),
                'Model carrier T21 host, pose, eligibility, or prop reference differs')
        lot_object = lotprops[row['lot_property']]
        require(lot_object.get('type') == '0x0300' and lot_object.get('key_type') == '0x0080',
                'Model carrier network-lot object must be an unsigned 32-bit array')
    return {'carrier_hosts_checked': sum(row['cast_shadow'] for row in rows),
            'ground_only_hosts_without_carriers': sum(not row['cast_shadow'] for row in rows),
            'model_resources_checked': 4 * sum(row['cast_shadow'] for row in rows),
            'owned_alpha_textures_checked': len(textures_checked),
            'native_binding_contract_checked': True, 'texture_ids': sorted(textures_checked),
            'game_shadow_selection_tested': False}
