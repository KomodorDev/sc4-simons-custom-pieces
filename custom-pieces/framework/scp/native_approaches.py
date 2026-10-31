"""Reversible RUL1 solutions for explicitly declared native DD approaches.

The helper cells belong to the native network. They add no owned resources,
and do not change the independent adaptive Street/Avenue insertion contract.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import re

from . import adaptive_network
from .dbpf import exemplar, require, tgi_string
from .providers import domain_module

RUL1 = adaptive_network.RUL1
S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
NETWORK_EXEMPLAR = (0x6534284A, 0x6BE08658)
SECTION = 'MonoRailDirtRoadIntersectionSolutions'
BEGIN = ';BEGIN SIMONS CUSTOM PIECES NATIVE DD APPROACHES'
END = ';END SIMONS CUSTOM PIECES NATIVE DD APPROACHES'
OVERLAY = 'native_dd_approaches'


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def approaches(piece):
    """Absent declarations never load a new domain implementation or schema."""
    if OVERLAY not in piece:
        return []
    require(type(piece[OVERLAY]) is bool, 'native_dd_approaches must be a boolean')
    if not piece[OVERLAY]:
        return []
    result = domain_module(piece, 'ddrhw_connections').approaches(piece)
    require(isinstance(result, list) and result and all(isinstance(row, dict) for row in result),
            'Declared native DD approaches require nonempty domain bindings')
    return deepcopy(result)


def declarations(pieces):
    return [{'piece_id': piece['id'], 'approaches': rows} for piece in pieces
            if (rows := approaches(piece))]


def needs_rul1(overlay):
    """The adaptive and native-helper proofs independently require RUL1."""
    return 'rul1' in overlay or OVERLAY in overlay


def expected_solutions(pieces):
    expected, supplied = {}, {}
    for piece in pieces:
        rows = approaches(piece)
        if not rows:
            continue
        for row in rows:
            for turns in range(4):
                first, second = (adaptive_network.rotate_flags(int(row[key], 16), turns)
                                 for key in ('monorail_flags', 'dirtroad_flags'))
                value = (int(row['native_tile_id'], 16), (row['native_rotation'] + turns) % 4, 0)
                require((first, second) not in expected or expected[first, second] == value,
                        'Conflicting declared native DD marker solutions')
                expected[first, second] = value
        domain_rows = domain_module(piece, 'ddrhw_connections').rul1_rows(piece)
        require(isinstance(domain_rows, (list, tuple)) and domain_rows,
                'Native DD approaches require domain RUL1 solutions')
        local = {}
        for row in domain_rows:
            require(isinstance(row, (list, tuple)) and len(row) == 5 and
                    all(type(value) is int for value in row) and
                    all(0 <= value <= 0xffffffff for value in row[:3]) and
                    row[3] in range(4) and row[4] == 0,
                    'Invalid native DD RUL1 solution row')
            a, b, c, d, e = row
            require((a, b) not in local, 'Duplicate per-piece native DD marker pair')
            local[a, b] = c, d, e
            require((a, b) not in supplied or supplied[a, b] == (c, d, e),
                    'Conflicting native DD RUL1 marker pairs')
            supplied[a, b] = c, d, e
        local_expected = {}
        for row in rows:
            for turns in range(4):
                key = tuple(adaptive_network.rotate_flags(int(row[name], 16), turns)
                            for name in ('monorail_flags', 'dirtroad_flags'))
                local_expected[key] = (int(row['native_tile_id'], 16),
                                       (row['native_rotation'] + turns) % 4, 0)
        require(local == local_expected, 'Domain native DD solutions differ from declared helper poses')
    require(supplied == expected, 'Native DD solutions do not cover the selected declarations')
    return expected


def dependency_keys(pieces):
    targets = {int(row['native_tile_id'], 16) for piece in pieces for row in approaches(piece)}
    return {(*prefix, target) for target in targets for prefix in (S3D, PATH, NETWORK_EXEMPLAR)}


def expected_dependencies(pieces):
    result = {}
    for piece in pieces:
        if not approaches(piece):
            continue
        pins = domain_module(piece, 'ddrhw_connections').NATIVE_DEPENDENCY_SHA256
        require(isinstance(pins, dict) and set(pins) == dependency_keys([piece]),
                'Native DD domain pins do not exactly cover its target resources')
        for key, value in pins.items():
            require(isinstance(value, str) and re.fullmatch('[0-9a-f]{64}', value) and
                    (key not in result or result[key] == value), 'Conflicting native DD dependency pins')
            result[key] = value
    return [{'tgi': tgi_string(key), 'sha256': value} for key, value in sorted(result.items())]


def dependency_records(pieces, resources):
    keys = dependency_keys(pieces)
    if not keys:
        return []
    require(keys <= resources.keys(), 'Missing audited native DD approach model or PATH dependency')
    from .models import parse_s3d, validate_s3d, valid_frame
    from .verify import parse_paths
    for key in keys:
        if key[:2] == S3D:
            model = parse_s3d(resources[key])
            frames = [frame for mesh in model['meshes'] for frame in mesh['frames']]
            require(frames and all(valid_frame(model, frame) for frame in frames),
                    'Native DD approach model has invalid render references')
            # Native donors may retain unused source buffers. Validate every
            # rendered buffer through a remapped validation view; the actual
            # resource remains untouched and its complete bytes stay pinned.
            names = ('vertices', 'indices', 'primitives', 'materials')
            used = [sorted({frame[index] for frame in frames}) for index in range(4)]
            lookup = [{old: new for new, old in enumerate(values)} for values in used]
            view = {**model, **{name: [model[name][index] for index in values]
                               for name, values in zip(names, used)}}
            view['meshes'] = [{**mesh, 'frames': [tuple(lookup[index][value]
                for index, value in enumerate(frame)) for frame in mesh['frames']]}
                for mesh in model['meshes']]
            validate_s3d(view)
        elif key[:2] == PATH:
            require(parse_paths(resources[key])['routes'], 'Native DD approach PATH contains no routes')
        else:
            props = {int(prop['id'], 16): prop['values'] for prop in exemplar(resources[key])['properties']}
            require(props.get(0x10) == [11] and props.get(0x27812820) == [*S3D, key[2]],
                    'Native DD approach exemplar does not select its single native model')
    result = [{'tgi': tgi_string(key), 'sha256': _sha(resources[key])} for key in sorted(keys)]
    require(result == expected_dependencies(pieces), 'Native DD approach resources differ from frozen domain pins')
    return result


def audit_dependencies(pieces, context, installed, paths):
    """Reject foreign overrides of native targets, including helper-only builds."""
    resources = {}
    for key in dependency_keys(pieces):
        labels = [label for label in paths if key in context[label]]
        require(labels, 'Native DD approach dependency is absent from audited donors')
        values = [context[label][key] for label in labels]
        require(all(value == values[0] for value in values), 'Conflicting audited native DD dependencies')
        require(set(installed.get(key, [])) == {paths[label] for label in labels},
                'Foreign or missing native DD approach dependency: ' + tgi_string(key))
        resources[key] = values[0]
    return dependency_records(pieces, resources)


def _section_span(raw):
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


def _solution_rows(raw):
    result = []
    for line in raw.decode('ascii').splitlines():
        active = line.split(';', 1)[0].strip()
        if not active:
            continue
        match = re.fullmatch(r'(?:TYPE\w*|[0-9]+)\s*=\s*(0x[0-9a-f]{1,8})\s*,\s*'
            r'(0x[0-9a-f]{1,8})\s*,\s*(0x[0-9a-f]{1,8})\s*,\s*([0-3])\s*,\s*([01])', active, re.I)
        require(match is not None, 'Unsupported native Monorail/DirtRoad solution row')
        result.append(tuple(int(value, 16) if index < 3 else int(value)
                            for index, value in enumerate(match.groups())))
    return result


def _compose(raw, pieces, dependencies):
    rows = expected_solutions(pieces)
    require(rows and BEGIN.encode() not in raw and END.encode() not in raw,
            'Native DD RUL1 baseline is empty or already contains helper additions')
    start, end = _section_span(raw)
    existing = _solution_rows(raw[start:end])
    require(not {(a, b) for a, b, *_ in existing} & rows.keys(),
            'Native DD approach markers conflict with native RUL1')
    ordered = [(*key, *value) for key, value in sorted(rows.items())]
    lines = [BEGIN, *[f'TYPE{index}=0x{a:08X},0x{b:08X},0x{c:08X},{d},{e}'
                     for index, (a, b, c, d, e) in enumerate(ordered, 1)], END, '']
    prefix = '' if not end or raw[end - 1:end] in (b'\r', b'\n') else '\r\n'
    insertion = prefix + '\r\n'.join(lines)
    record = {'schema_version': 1, 'section': SECTION, 'base_sha256': _sha(raw),
              'selected_declarations': declarations(pieces),
              'native_dependencies': dependencies, 'native_solutions': [list(row) for row in ordered],
              'insertion_offset': end, 'insertion': insertion, 'game_behavior_tested': False}
    return raw[:end] + insertion.encode('ascii') + raw[end:], record


def compose_rul1(raw, pieces, donors):
    if not declarations(pieces):
        return raw, None
    return _compose(raw, pieces, dependency_records(pieces, donors))


def verify_rul1(resources, pieces, overlay, donors):
    """Remove helper bytes first, then run the unchanged adaptive verifier."""
    selected = declarations(pieces)
    if not selected:
        require(OVERLAY not in overlay, 'Undeclared native DD approach overlay')
        return adaptive_network.verify_rul1(resources, pieces, overlay, donors)
    require(OVERLAY in overlay and RUL1 in resources, 'Missing native DD approach RUL1 overlay')
    record = overlay[OVERLAY]
    require(isinstance(record, dict) and isinstance(record.get('insertion'), str),
            'Invalid native DD approach proof')
    insertion, offset = record['insertion'].encode('ascii'), record.get('insertion_offset')
    raw = resources[RUL1]
    require(type(offset) is int and offset >= 0 and insertion and
            raw[offset:offset + len(insertion)] == insertion and raw.count(insertion) == 1,
            'Native DD approach insertion is missing, changed, or nonunique')
    restored = raw[:offset] + raw[offset + len(insertion):]
    dependencies = record.get('native_dependencies')
    keys = [tgi_string(key) for key in sorted(dependency_keys(pieces))]
    require(isinstance(dependencies, list) and len(dependencies) == len(keys) and
            all(isinstance(item, dict) and set(item) == {'tgi', 'sha256'} and
                item['tgi'] == key and isinstance(item['sha256'], str) and
                re.fullmatch('[0-9a-f]{64}', item['sha256'])
                for item, key in zip(dependencies, keys)),
            'Native DD approach dependency proof differs from the declared targets')
    require(dependencies == expected_dependencies(pieces),
            'Native DD approach dependency hashes differ from frozen domain pins')
    if donors:
        require(dependencies == dependency_records(pieces, donors),
                'Native DD approach dependencies differ from audited donors')
    expected_raw, expected_record = _compose(restored, pieces, dependencies)
    require(raw == expected_raw and json.dumps(record, sort_keys=True) ==
            json.dumps(expected_record, sort_keys=True),
            'Native DD approach insertion or declaration proof differs')
    view = {**resources, RUL1: restored}
    if not adaptive_network.expected_solutions(pieces):
        del view[RUL1]
    report = adaptive_network.verify_rul1(view, pieces, overlay, donors)
    native = restored
    if 'rul1' in overlay:
        adaptive = overlay['rul1']
        at, added = adaptive['insertion_offset'], adaptive['insertion'].encode('ascii')
        native = restored[:at] + restored[at + len(added):]
    pins = {domain_module(piece, 'ddrhw_connections').NATIVE_RUL1_SHA256
            for piece in pieces if approaches(piece)}
    require(pins == {_sha(native)}, 'Native DD approach baseline differs from the pinned native RUL1')
    if donors:
        require(donors.get(RUL1) == native, 'Restored native DD RUL1 differs from audited donors')
    return {**report, 'native_dd_approach_cells_checked': sum(len(item['approaches']) for item in selected),
            'native_dd_rul1_solutions_checked': len(expected_solutions(pieces)),
            'native_dd_dependencies_checked': len(dependencies), 'native_rul1_bytes_preserved': True,
            'native_dd_game_behavior_tested': False}
