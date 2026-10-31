"""Bounded texture-network cells beneath independently checked model props.

Canonical models and paths remain authoring and measurement resources. The
explicit bindings identify the different resources selected by the game.
Absent metadata retains the existing fixed-model network contract.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import re

from .dbpf import exemplar, require

RUL1 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000001)
S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0x69668828)
TEXTURE = (0x7AB50E44, 0x1ABE787D)
PROP = (0x6534284A, 0xC977C536)
T21 = (0x6534284A, 0x89AC5643)
NETWORK_EXEMPLAR = (0x6534284A, 0xA8434037)
CURSOR_BASE = 0x55387000
SECTION = 'StreetAvenueIntersectionSolutions'
BEGIN = ';BEGIN SIMONS CUSTOM PIECES ADAPTIVE NETWORKS'
END = ';END SIMONS CUSTOM PIECES ADAPTIVE NETWORKS'


def _hex(value, label):
    require(isinstance(value, str) and re.fullmatch(r'[0-9a-fA-F]{8}', value),
            f'{label} must contain exactly eight hexadecimal digits')
    return int(value, 16)


def bindings(piece):
    """Validate declared cells and return independent, enriched copies."""
    if 'adaptive_ground' not in piece:
        return []
    metadata = piece['adaptive_ground']
    require(isinstance(metadata, dict) and {'schema_version', 'cells'} <= set(metadata)
            and set(metadata) <= {'schema_version', 'cells', 'construction_helper', 'use_path_elevation'}
            and type(metadata['schema_version']) is int and metadata['schema_version'] == 1,
            'Unsupported adaptive-ground metadata')
    require(type(metadata.get('use_path_elevation', False)) is bool,
            'Adaptive PATH elevation setting must be a boolean')
    rows = metadata['cells']
    require(isinstance(rows, list) and rows, 'Adaptive-ground cells must be a nonempty list')
    width, depth = piece['footprint']
    cells = piece.get('cells', [[x, y] for y in range(depth) for x in range(width)])
    canonical = {tuple(cell): tile for cell, tile in zip(cells, piece['tile_ids'])}
    seen_cells, seen_tiles, result = set(), set(), []
    fields = {'cell', 'resolved_tile_id', 'rotation', 'texture_donor_id',
              'street_flags', 'avenue_flags', 'prop'}
    for row in rows:
        require(isinstance(row, dict) and set(row) == fields, 'Invalid adaptive-ground cell fields')
        cell = row['cell']
        require(isinstance(cell, list) and len(cell) == 2 and all(type(v) is int for v in cell),
                'Adaptive-ground cell must contain two integer coordinates')
        cell = tuple(cell)
        require(cell in canonical and cell not in seen_cells,
                'Adaptive-ground cells must be unique occupied cells')
        seen_cells.add(cell)
        resolved = _hex(row['resolved_tile_id'], 'Resolved tile ID')
        require(resolved & 0xff == 0 and resolved not in seen_tiles,
                'Adaptive tile families must be distinct and end in hexadecimal 00')
        seen_tiles.add(resolved)
        require(type(row['rotation']) is int and row['rotation'] in range(4),
                'Adaptive tile rotation must be 0, 1, 2, or 3')
        require(type(row['prop']) is bool, 'Adaptive prop setting must be a boolean')
        _hex(row['texture_donor_id'], 'Texture donor ID')
        _hex(row['street_flags'], 'Street flags'); _hex(row['avenue_flags'], 'Avenue flags')
        tile = _hex(canonical[cell], 'Canonical tile ID')
        item = deepcopy(row)
        item.update(canonical_tile_id=f'{tile:08x}', prop_id=f'{tile:08x}',
                    prop_model_id=f'{tile + 5:08x}', t21_id=f'{resolved:08x}')
        result.append(item)
    if 'construction_helper' in metadata:
        helper = metadata['construction_helper']
        require(isinstance(helper, list) and len(helper) == 2
                and all(type(value) is int for value in helper),
                'Adaptive construction helper must contain two integer coordinates')
        require(len(result) == len(canonical),
                'An explicit adaptive construction helper requires an entirely adaptive piece')
        require(0 <= helper[0] <= width and 0 <= helper[1] < depth,
                'Adaptive construction helper must fit the non-anchor construction grid')
        require(tuple(helper) not in canonical,
                'Adaptive construction helper must not overlap an owned cell')
    return result


def construction_helper(piece):
    """Return the sole removable Road cell, separately from permanent ownership.

    Existing definitions retain the external right-edge handle. A smaller
    entirely adaptive piece may explicitly select a vacant internal corner or
    another available cell in its existing construction grid. Native FLEX
    removes every check at the handle coordinate, so overlap is forbidden.
    This declaration does not prove the game's placement or collision bounds.
    """
    rows = bindings(piece)
    width, depth = piece['footprint']
    cells = piece.get('cells', [[x, y] for y in range(depth) for x in range(width)])
    if not rows or len(rows) != len(cells):
        return None
    helper = tuple(piece['adaptive_ground'].get('construction_helper', [width, 0]))
    require(helper not in {tuple(cell) for cell in cells},
            'Adaptive construction helper must not overlap an owned cell')
    return helper


def fixed_cells(piece):
    width, depth = piece['footprint']
    adaptive = {tuple(row['cell']) for row in bindings(piece)}
    return [cell for cell in piece.get('cells', [[x, y] for y in range(depth) for x in range(width)])
            if tuple(cell) not in adaptive]


def resource_keys(piece):
    """Exact extra DAT resources; canonical models, paths, and labels remain."""
    result = set()
    for row in bindings(piece):
        resolved, tile = int(row['resolved_tile_id'], 16), int(row['canonical_tile_id'], 16)
        result.add((*PATH, resolved))
        result.update((*TEXTURE, resolved + appearance + zoom)
                      for appearance in (0, 0x10, 0x20, 0x30) for zoom in range(5))
        if row['prop']:
            result.update({(*S3D, tile + 5), (*PROP, tile), (*T21, resolved)})
    return result


def reservation_ids(record):
    """Reserve complete 256-ID appearance families and declared prop models."""
    result = []
    adaptive = record.get('adaptive_tile_ids', [])
    extra = record.get('extra_model_ids', [])
    require(isinstance(adaptive, list) and isinstance(extra, list),
            'Adaptive and extra-model allocations must be lists')
    for value in adaptive:
        tile = _hex(value, 'Adaptive allocation')
        require(tile & 0xff == 0, 'Adaptive allocation must reserve a complete 256-ID family')
        result.extend(range(tile, tile + 0x100))
    result.extend(_hex(value, 'Extra model allocation') for value in extra)
    require(len(result) == len(set(result)), 'Adaptive resource allocation overlap')
    return result


def allocation_fields(piece):
    rows = bindings(piece)
    return {'adaptive_tile_ids': [row['resolved_tile_id'] for row in rows],
            'extra_model_ids': [row['prop_model_id'] for row in rows if row['prop']]}


def allocation_blocks(record):
    """Return every 4096-ID block unavailable to a future piece allocator."""
    values = [record['preview_id'], *record['tile_ids'], *record.get('resource_blocks', []),
              *record.get('adaptive_tile_ids', []), *record.get('extra_model_ids', [])]
    return {int(value, 16) & 0xfffff000 for value in values}


def _properties(raw, kind):
    record = exemplar(raw)
    props = {int(prop['id'], 16): prop for prop in record['properties']}
    require(len(props) == len(record['properties']) and record['parent'] == [0, 0, 0]
            and props.get(0x10, {}).get('values') == [kind],
            'Invalid or inherited adaptive exemplar')
    return props


def validate_active_resources(resources, piece):
    """Check encoded bindings; domain checks establish geometry and PATH poses."""
    from .verify import parse_paths

    rows = bindings(piece)
    require(resource_keys(piece) <= resources.keys(),
            'Adaptive cell is missing a texture, PATH, prop, or T21 resource')
    for row in rows:
        resolved, tile = int(row['resolved_tile_id'], 16), int(row['canonical_tile_id'], 16)
        require(parse_paths(resources[*PATH, resolved])['terrain'] ==
                int(piece['adaptive_ground'].get('use_path_elevation', False)),
                'Adaptive active PATH elevation flag differs from its declaration')
        require((*NETWORK_EXEMPLAR, tile) not in resources and
                (*NETWORK_EXEMPLAR, resolved) not in resources,
                'Adaptive cells must not select a fixed network model exemplar')
        if not row['prop']:
            continue
        prop = _properties(resources[*PROP, tile], 0x1E)
        reference = prop.get(0x27812820, {})
        rotation = prop.get(0xE83A081D, {})
        require(prop.get(0x21, {}).get('values') == [tile] and
                reference.get('type') == '0x0300' and reference.get('key_type') == '0x0080'
                and reference.get('values') == [*S3D, tile + 5], 'Adaptive prop points to the wrong model')
        require(rotation.get('type') == '0x0b00' and rotation.get('key_type') == '0x0000'
                and rotation.get('values') == [1], 'Adaptive prop lacks native full-geometry rotation encoding')
        t21 = _properties(resources[*T21, resolved], 0x21)
        expected = {0x21: [resolved], 0xC9A5A1BE: [resolved], 0xEC3BD470: [15], 0xCA81B8D4: [4],
                    0xCC3E4755: [2], 0x88EDC789: [2], 0x88EDC793: list(range(16)),
                    0x88EDC795: [0, 1, 2, 3], 0x49D55951: [15, 15, 15, 15]}
        require(all(t21.get(pid, {}).get('values') == values for pid, values in expected.items()),
                'Adaptive T21 has incorrect network, rotation, mirror, zone, or wealth settings')
        lot = t21.get(0x88EDC900, {}).get('values')
        require(lot == [1, 0, (-row['rotation']) % 4, 0x80000, 0, 0x80000,
                        0, 0, 0xFFFFF, 0xFFFFF, 0, resolved, tile],
                'Adaptive T21 prop pose or reference differs from its declared tile pose')
    return {'adaptive_cells_checked': len(rows), 'active_bindings_checked': True,
            'game_behavior_tested': False}


def rotate_flags(value, turns):
    shift = 8 * (turns % 4)
    return ((value << shift) | (value >> ((32 - shift) % 32))) & 0xffffffff


def expected_solutions(pieces):
    result = {}
    for piece in pieces:
        for row in bindings(piece):
            street, avenue, target = (int(row[key], 16) for key in
                                      ('street_flags', 'avenue_flags', 'resolved_tile_id'))
            for turns in range(4):
                key = rotate_flags(street, turns), rotate_flags(avenue, turns)
                value = target, (row['rotation'] + turns) % 4, 0
                require(key not in result or result[key] == value, 'Conflicting adaptive RUL1 solutions')
                result[key] = value
    return result


def section_span(raw):
    headers, offset = [], 0
    for line in raw.splitlines(keepends=True):
        match = re.fullmatch(rb'\[([^\]]+)\]', line.split(b';', 1)[0].strip())
        if match:
            headers.append((offset, offset + len(line), match[1].decode('ascii').lower()))
        offset += len(line)
    found = [i for i, item in enumerate(headers) if item[2] == SECTION.lower()]
    require(len(found) == 1, f'RUL1 requires exactly one [{SECTION}] section')
    index = found[0]
    return headers[index][1], headers[index + 1][0] if index + 1 < len(headers) else len(raw)


def solution_rows(raw):
    result = []
    for line in raw.decode('ascii').splitlines():
        active = line.split(';', 1)[0].strip()
        if not active:
            continue
        match = re.fullmatch(r'TYPE\w*\s*=\s*(0x[0-9a-f]{1,8})\s*,\s*'
            r'(0x[0-9a-f]{1,8})\s*,\s*(0x[0-9a-f]{1,8})\s*,\s*([0-3])\s*,\s*([01])', active, re.I)
        require(match is not None, 'Unsupported adaptive Street/Avenue solution row')
        result.append(tuple(int(value, 16) if i < 3 else int(value)
                            for i, value in enumerate(match.groups())))
    return result


def compose_rul1(native, deltas, pieces):
    require(deltas and BEGIN.encode() not in native and END.encode() not in native,
            'RUL1 baseline already contains adaptive additions, or no delta was supplied')
    rows = [row for delta in deltas for row in solution_rows(delta.encode('ascii'))]
    expected = expected_solutions(pieces)
    require(len(rows) == len(expected) and {(a, b): (c, d, e) for a, b, c, d, e in rows} == expected,
            'Adaptive RUL1 deltas do not exactly implement the declared cell poses')
    start, end = section_span(native)
    existing = solution_rows(native[start:end])
    require(not {(a, b) for a, b, *_ in existing} & expected.keys(),
            'Adaptive Street/Avenue markers conflict with native RUL1')
    targets = {value[0] for value in expected.values()}
    all_targets = {int(match[1], 16) for match in re.finditer(
        rb'^\s*TYPE\w*\s*=\s*0x[0-9a-f]+\s*,\s*0x[0-9a-f]+\s*,\s*0x([0-9a-f]+)', native, re.I | re.M)}
    require(not targets & all_targets, 'Adaptive tile ID is already selected by native RUL1')
    lines = [BEGIN, *[f'TYPE{index}=0x{a:08X},0x{b:08X},0x{c:08X},{d},{e}'
                      for index, (a, b, c, d, e) in enumerate(rows, 1)], END, '']
    prefix = '' if not end or native[end - 1:end] in (b'\r', b'\n') else '\r\n'
    insertion = prefix + '\r\n'.join(lines)
    raw = native[:end] + insertion.encode('ascii') + native[end:]
    return raw, {'base_sha256': hashlib.sha256(native).hexdigest(),
                 'insertion_offset': end, 'insertion': insertion}


def verify_rul1(resources, pieces, overlay, donors):
    expected = expected_solutions(pieces)
    if not expected:
        require('rul1' not in overlay and RUL1 not in resources,
                'Fixed-model builds must not contain an adaptive RUL1 overlay')
        return {'adaptive_rul1_solutions_checked': 0}
    require('rul1' in overlay and RUL1 in resources, 'Adaptive construction is missing its RUL1 overlay')
    record = overlay['rul1']; insertion = record['insertion'].encode('ascii')
    raw, offset = resources[RUL1], record['insertion_offset']
    require(type(offset) is int and offset >= 0 and insertion and
            raw[offset:offset + len(insertion)] == insertion and raw.count(insertion) == 1,
            'Adaptive RUL1 insertion is missing, changed, or nonunique')
    native = raw[:offset] + raw[offset + len(insertion):]
    require(hashlib.sha256(native).hexdigest() == record['base_sha256'],
            'Native RUL1 bytes changed outside the adaptive insertion')
    if donors:
        require(donors.get(RUL1) == native, 'Restored RUL1 differs from the pinned native controller')
    start, end = section_span(native)
    require(offset == end and BEGIN.encode() in insertion and END.encode() in insertion,
            'Adaptive RUL1 insertion is outside its declared solution section')
    rows = solution_rows(insertion)
    require(len(rows) == len(expected) and {(a, b): (c, d, e) for a, b, c, d, e in rows} == expected,
            'Saved adaptive RUL1 does not exactly match declared cell poses')
    require(not {(a, b) for a, b, *_ in solution_rows(native[start:end])} & expected.keys(),
            'Saved adaptive solutions override native Street/Avenue markers')
    return {'adaptive_rul1_solutions_checked': len(rows), 'native_rul1_bytes_preserved': True}
