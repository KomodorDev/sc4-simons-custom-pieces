"""Reversible RUL1 solutions for explicitly declared native approaches.

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
GHSR_OVERLAY = 'native_ghsr_approaches'
ORTHOGONAL_OVERLAY = 'native_orthogonal_approaches'
Y_JUNCTION_OVERLAY = 'native_y_junction_approaches'
DIAGONAL_TRANSITION_OVERLAY = 'native_diagonal_transition_approaches'


def _provider(piece):
    name = ('diagonal_transition_approaches' if piece.get(DIAGONAL_TRANSITION_OVERLAY) else
            'y_junction_approaches' if piece.get(Y_JUNCTION_OVERLAY) else
            'orthogonal_approaches' if piece.get(ORTHOGONAL_OVERLAY) else
            'ghsr_approaches' if piece.get(GHSR_OVERLAY) else 'ddrhw_connections')
    return domain_module(piece, name)


def _pair(row):
    """Keep legacy DD records unchanged; new helpers name both networks."""
    if 'networks' not in row:
        return SECTION, int(row['monorail_flags'], 16), int(row['dirtroad_flags'], 16)
    names = {'MonoRailDirtRoadIntersectionSolutions': ('monorail', 'dirtroad'),
             'RailMonoRailIntersectionSolutions': ('rail', 'monorail'),
             'RoadDirtRoadIntersectionSolutions': ('road', 'dirtroad')}
    section, networks = row.get('section'), row['networks']
    require(section in names and isinstance(networks, list) and len(networks) == 2
            and all(isinstance(item, dict) and set(item) == {'name', 'flags'} for item in networks)
            and tuple(item['name'] for item in networks) == names[section]
            and all(isinstance(item['flags'], str) and re.fullmatch('[0-9a-fA-F]{8}', item['flags'])
                    for item in networks), 'Invalid section-specific native approach network pair')
    return section, *(int(item['flags'], 16) for item in networks)


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def approaches(piece):
    """Absent declarations never load a new domain implementation or schema."""
    modes = (OVERLAY, GHSR_OVERLAY, ORTHOGONAL_OVERLAY, Y_JUNCTION_OVERLAY, DIAGONAL_TRANSITION_OVERLAY)
    if not any(name in piece for name in modes):
        return []
    for name in modes:
        if name in piece:
            require(type(piece[name]) is bool, name + ' must be a boolean')
    if not any(piece.get(name) for name in modes):
        return []
    require(sum(bool(piece.get(name)) for name in modes) == 1,
            'Mixed native approaches must not also request legacy DD helpers or another approach mode')
    result = _provider(piece).approaches(piece)
    require(isinstance(result, list) and result and all(isinstance(row, dict) for row in result),
            'Declared native DD approaches require nonempty domain bindings')
    for row in result:
        _pair(row)
    return deepcopy(result)


def declarations(pieces):
    return [{'piece_id': piece['id'], 'approaches': rows} for piece in pieces
            if (rows := approaches(piece))]


def needs_rul1(overlay):
    """The adaptive and native-helper proofs independently require RUL1."""
    return 'rul1' in overlay or OVERLAY in overlay


def required_controller_resources(pieces):
    """Extra native rule inputs required by an explicitly selected provider."""
    result = {}
    for piece in pieces:
        if not approaches(piece):
            continue
        pins = getattr(_provider(piece), 'NATIVE_CONTROLLER_SHA256', {})
        require(isinstance(pins, dict), 'Invalid native approach controller dependency pins')
        for key, fingerprint in pins.items():
            require(isinstance(key, tuple) and len(key) == 3
                    and all(type(value) is int and 0 <= value <= 0xFFFFFFFF for value in key)
                    and key[:2] == RUL1[:2] and isinstance(fingerprint, str)
                    and re.fullmatch('[0-9a-f]{64}', fingerprint)
                    and (key not in result or result[key] == fingerprint),
                    'Conflicting or invalid native approach controller dependency')
            result[key] = fingerprint
    return result


def expected_solution_sections(pieces):
    """Validate each complete network-pair table independently."""
    expected, supplied = {}, {}
    for piece in pieces:
        rows = approaches(piece)
        if not rows:
            continue
        for row in rows:
            section, a, b = _pair(row)
            for turns in range(4):
                first, second = (adaptive_network.rotate_flags(value, turns) for value in (a, b))
                value = (int(row['native_tile_id'], 16), (row['native_rotation'] + turns) % 4, 0)
                key = section, first, second
                require(key not in expected or expected[key] == value,
                        'Conflicting declared native DD marker solutions')
                expected[key] = value
        provider = _provider(piece)
        sections = (provider.rul1_sections(piece) if piece.get(GHSR_OVERLAY) or piece.get(ORTHOGONAL_OVERLAY)
                    or piece.get(Y_JUNCTION_OVERLAY) or piece.get(DIAGONAL_TRANSITION_OVERLAY)
                    else {SECTION: provider.rul1_rows(piece)})
        require(isinstance(sections, dict) and sections and all(isinstance(section, str)
                and isinstance(values, (list, tuple)) and values for section, values in sections.items()),
                'Native approaches require domain RUL1 solutions')
        local = {}
        for section, domain_rows in sections.items():
            for row in domain_rows:
                require(isinstance(row, (list, tuple)) and len(row) == 5 and
                        all(type(value) is int for value in row) and
                        all(0 <= value <= 0xffffffff for value in row[:3]) and
                        row[3] in range(4) and row[4] == 0,
                        'Invalid native DD RUL1 solution row')
                a, b, c, d, e = row
                key = section, a, b
                require(key not in local, 'Duplicate per-piece native DD marker pair')
                local[key] = c, d, e
                require(key not in supplied or supplied[key] == (c, d, e),
                        'Conflicting native DD RUL1 marker pairs')
                supplied[key] = c, d, e
        local_expected = {}
        for row in rows:
            section, a, b = _pair(row)
            for turns in range(4):
                key = section, *(adaptive_network.rotate_flags(value, turns) for value in (a, b))
                local_expected[key] = (int(row['native_tile_id'], 16),
                                       (row['native_rotation'] + turns) % 4, 0)
        require(local == local_expected, 'Domain native DD solutions differ from declared helper poses')
    require(supplied == expected, 'Native DD solutions do not cover the selected declarations')
    result = {}
    for (section, a, b), value in expected.items():
        result.setdefault(section, {})[a, b] = value
    return result


def _existing_solution_sections(pieces):
    """Reuse only rows declared by explicitly reviewed native socket owners."""
    result = {}
    for piece in pieces:
        if not (piece.get(ORTHOGONAL_OVERLAY) or piece.get(Y_JUNCTION_OVERLAY) or piece.get(DIAGONAL_TRANSITION_OVERLAY)):
            continue
        provider = _provider(piece)
        declared = provider.existing_rul1_sections(piece)
        # Each Y module owns one socket: only its orthogonal owner reuses
        # original rows. The two diagonal owners require inserted solutions.
        if piece.get(Y_JUNCTION_OVERLAY) and declared == {}:
            continue
        expected = expected_solution_sections([piece])
        require(isinstance(declared, dict) and declared,
                'Orthogonal native approaches require exact existing solutions')
        actual = {}
        for section, rows in declared.items():
            require(isinstance(rows, (tuple, list)) and rows,
                    'Invalid existing native approach solution table')
            table = {}
            for row in rows:
                require(isinstance(row, (tuple, list)) and len(row) == 5
                        and all(type(value) is int for value in row)
                        and all(0 <= value <= 0xffffffff for value in row[:3])
                        and row[3] in range(4) and row[4] == 0,
                        'Invalid existing native approach solution row')
                a, b, c, d, e = row
                require((a, b) not in table, 'Duplicate existing native approach marker pair')
                table[a, b] = c, d, e
            actual[section] = table
        if piece.get(DIAGONAL_TRANSITION_OVERLAY):
            # This reviewed provider combines native ground rows with stacked
            # DD rows inserted under distinct markers. Legacy modes retain
            # their complete-table equality requirement below.
            require(actual and all(section in expected and all(expected[section].get(key) == value
                    for key,value in table.items()) for section,table in actual.items()),
                    'Reused diagonal transition rows differ from reviewed declarations')
        else:
            require(actual == expected, 'Existing native solutions differ from the reviewed socket declarations')
        for section, table in actual.items():
            target = result.setdefault(section, {})
            for key, value in table.items():
                require(key not in target or target[key] == value,
                        'Conflicting reused native approach solutions')
                target[key] = value
    return result


def expected_solutions(pieces):
    """Retain the legacy public DD-only table view."""
    return expected_solution_sections(pieces).get(SECTION, {})


def dependency_keys(pieces):
    result = set()
    for piece in pieces:
        for row in approaches(piece):
            target = int(row['native_tile_id'], 16)
            group = int(row.get('native_exemplar_group', f'{NETWORK_EXEMPLAR[1]:08x}'), 16)
            require(group in (NETWORK_EXEMPLAR[1], 0xEBE084C2), 'Unsupported native approach exemplar group')
            reference = row.get('native_model_reference', 'rkt0')
            require(reference in ('rkt0', 'rkt1', 'direct'), 'Unsupported native approach model reference')
            require(reference != 'direct' or piece.get(ORTHOGONAL_OVERLAY),
                    'Direct native lookup requires an explicit reviewed orthogonal approach')
            result.update({(*S3D, target), (*PATH, target)})
            if reference != 'direct':
                result.add((NETWORK_EXEMPLAR[0], group, target))
        if (piece.get(Y_JUNCTION_OVERLAY) or piece.get(DIAGONAL_TRANSITION_OVERLAY)) and approaches(piece):
            additional = _provider(piece).additional_dependency_keys(piece)
            require(isinstance(additional, set) and all(isinstance(key, tuple) and len(key) == 3
                    and all(type(value) is int and 0 <= value <= 0xffffffff for value in key)
                    for key in additional), 'Invalid Y native continuation dependencies')
            result.update(additional)
    return result


def expected_dependencies(pieces):
    result = {}
    for piece in pieces:
        if not approaches(piece):
            continue
        provider = _provider(piece)
        pins = (provider.dependency_sha256(piece) if piece.get(Y_JUNCTION_OVERLAY) or piece.get(DIAGONAL_TRANSITION_OVERLAY)
                else provider.NATIVE_DEPENDENCY_SHA256)
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
    references, ignored_frames = {}, {}
    for piece in pieces:
        if approaches(piece):
            ignored = getattr(_provider(piece), 'NATIVE_IGNORED_MODEL_FRAMES', {})
            require(isinstance(ignored, dict) and set(ignored) <= dependency_keys([piece])
                    and all(key[:2] == S3D for key in ignored),
                    'Invalid reviewed native model frame inventory')
            for key, frames in ignored.items():
                require(key not in ignored_frames or ignored_frames[key] == frames,
                        'Conflicting reviewed native model frame inventories')
                ignored_frames[key] = frames
            if piece.get(Y_JUNCTION_OVERLAY) or piece.get(DIAGONAL_TRANSITION_OVERLAY):
                additional = _provider(piece).dependency_model_references(piece)
                require(isinstance(additional, dict) and set(additional) <= dependency_keys([piece])
                        and all(key[:2] == NETWORK_EXEMPLAR and reference == 'rkt0'
                                for key, reference in additional.items()),
                        'Invalid Y native continuation model references')
                for key, reference in additional.items():
                    require(key not in references or references[key] == reference,
                            'Conflicting native continuation model references')
                    references[key] = reference
        for row in approaches(piece):
            target = int(row['native_tile_id'], 16)
            group = int(row.get('native_exemplar_group', f'{NETWORK_EXEMPLAR[1]:08x}'), 16)
            reference = row.get('native_model_reference', 'rkt0')
            require(reference in ('rkt0', 'rkt1', 'direct'), 'Unsupported native approach model reference')
            if reference == 'direct':
                continue
            key = NETWORK_EXEMPLAR[0], group, target
            require(key not in references or references[key] == reference,
                    'Conflicting native approach model references')
            references[key] = reference
    for key in keys:
        if key[:2] == S3D:
            model = parse_s3d(resources[key])
            invalid = tuple((mesh_no, frame_no, tuple(frame))
                            for mesh_no, mesh in enumerate(model['meshes'])
                            for frame_no, frame in enumerate(mesh['frames']) if not valid_frame(model, frame))
            frames = [frame for mesh in model['meshes'] for frame in mesh['frames'] if valid_frame(model, frame)]
            require(frames and invalid == ignored_frames.get(key, ()),
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
                for index, value in enumerate(frame)) for frame in mesh['frames'] if valid_frame(model, frame)]}
                for mesh in model['meshes'] if any(valid_frame(model, frame) for frame in mesh['frames'])]
            validate_s3d(view)
        elif key[:2] == PATH:
            require(parse_paths(resources[key])['routes'], 'Native DD approach PATH contains no routes')
        else:
            props = {int(prop['id'], 16): prop['values'] for prop in exemplar(resources[key])['properties']}
            reference = references[key]
            property_id, values = ((0x27812820, [*S3D, key[2]]) if reference == 'rkt0'
                                   else (0x27812823, [*S3D, *([key[2]] * 5)]))
            require(props.get(0x10) == [11] and props.get(property_id) == values,
                    'Native DD approach exemplar does not select its audited native model')
    result = [{'tgi': tgi_string(key), 'sha256': _sha(resources[key])} for key in sorted(keys)]
    require(result == expected_dependencies(pieces), 'Native DD approach resources differ from frozen domain pins')
    return result


def audit_dependencies(pieces, context, installed, paths):
    """Reject foreign overrides of native targets, including helper-only builds."""
    direct_targets = {int(row['native_tile_id'], 16) for piece in pieces
                      if piece.get(ORTHOGONAL_OVERLAY) for row in approaches(piece)
                      if row.get('native_model_reference') == 'direct'}
    # An absent exemplar is part of a direct lookup's measured identity.
    # Reject every exemplar group for that IID without fabricating a donor
    # dependency or changing any legacy model-reference admission behavior.
    direct_exemplars = sorted(key for key, providers in installed.items()
                              if providers and key[0] == NETWORK_EXEMPLAR[0] and key[2] in direct_targets)
    require(not direct_exemplars, 'Direct native lookup must not have a network exemplar: '
            + ', '.join(tgi_string(key) for key in direct_exemplars))
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


def _section_span(raw, section=SECTION):
    headers, offset = [], 0
    for line in raw.splitlines(keepends=True):
        match = re.fullmatch(rb'\[([^\]]+)\]', line.split(b';', 1)[0].strip())
        if match:
            headers.append((offset, offset + len(line), match[1].decode('ascii').lower()))
        offset += len(line)
    found = [i for i, item in enumerate(headers) if item[2] == section.lower()]
    require(len(found) == 1, f'RUL1 requires exactly one [{section}] section')
    index = found[0]
    return headers[index][1], headers[index + 1][0] if index + 1 < len(headers) else len(raw)


def _solution_rows(raw):
    result = []
    for line in raw.decode('ascii').splitlines():
        active = line.split(';', 1)[0].strip()
        if not active:
            continue
        match = re.fullmatch(r'[A-Za-z0-9_]+\s*=\s*(0x[0-9a-f]{1,8})\s*,\s*'
            r'(0x[0-9a-f]{1,8})\s*,\s*(0x[0-9a-f]{1,8})\s*,\s*([0-3])\s*,\s*([01])', active, re.I)
        require(match is not None, 'Unsupported native Monorail/DirtRoad solution row')
        result.append(tuple(int(value, 16) if index < 3 else int(value)
                            for index, value in enumerate(match.groups())))
    return result


def _compose(raw, pieces, dependencies):
    sections = expected_solution_sections(pieces)
    reused = _existing_solution_sections(pieces)
    require(sections and BEGIN.encode() not in raw and END.encode() not in raw,
            'Native DD RUL1 baseline is empty or already contains helper additions')
    reuse_records = []
    for section, table in sorted(reused.items()):
        start, end = _section_span(raw, section)
        actual = _solution_rows(raw[start:end])
        ordered = [(*key, *value) for key, value in sorted(table.items())]
        for row in ordered:
            require([value for value in actual if value[:2] == row[:2]] == [row],
                    'Reviewed existing native approach solution is missing, changed, or ambiguous')
        reuse_records.append({'section': section, 'native_solutions': [list(row) for row in ordered]})
    sections = {section: {key: value for key, value in table.items()
                          if key not in reused.get(section, {})}
                for section, table in sections.items()}
    sections = {section: table for section, table in sections.items() if table}
    current, entries = raw, []
    for section, rows in sorted(sections.items()):
        start, end = _section_span(current, section)
        existing = _solution_rows(current[start:end])
        require(not {(a, b) for a, b, *_ in existing} & rows.keys(),
                'Native DD approach markers conflict with native RUL1')
        ordered = [(*key, *value) for key, value in sorted(rows.items())]
        # Historical one-section proof bytes remain unchanged. Distinct
        # markers make each new insertion independently removable.
        first = BEGIN if len(sections) == 1 else BEGIN + ' ' + section
        last = END if len(sections) == 1 else END + ' ' + section
        lines = [first, *[f'TYPE{index}=0x{a:08X},0x{b:08X},0x{c:08X},{d},{e}'
                         for index, (a, b, c, d, e) in enumerate(ordered, 1)], last, '']
        prefix = '' if not end or current[end - 1:end] in (b'\r', b'\n') else '\r\n'
        insertion = prefix + '\r\n'.join(lines)
        entries.append({'section': section, 'native_solutions': [list(row) for row in ordered],
                        'insertion_offset': end, 'insertion': insertion})
        current = current[:end] + insertion.encode('ascii') + current[end:]
    if reuse_records:
        record = {'schema_version': 3, 'sections': entries, 'base_sha256': _sha(raw),
                  'selected_declarations': declarations(pieces),
                  'native_dependencies': dependencies, 'existing_native_solutions': reuse_records,
                  'game_behavior_tested': False}
    elif len(entries) == 1:
        item = entries[0]
        record = {'schema_version': 1, 'section': item['section'], 'base_sha256': _sha(raw),
                  'selected_declarations': declarations(pieces),
                  'native_dependencies': dependencies, 'native_solutions': item['native_solutions'],
                  'insertion_offset': item['insertion_offset'], 'insertion': item['insertion'],
                  'game_behavior_tested': False}
    else:
        record = {'schema_version': 2, 'sections': entries, 'base_sha256': _sha(raw),
                  'selected_declarations': declarations(pieces),
                  'native_dependencies': dependencies, 'game_behavior_tested': False}
    return current, record


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
    require(isinstance(record, dict) and type(record.get('schema_version')) is int and
            record['schema_version'] in (1, 2, 3),
            'Invalid native DD approach proof')
    raw = resources[RUL1]
    edits = [record] if record['schema_version'] == 1 else record.get('sections')
    require(isinstance(edits, list) and (edits or record['schema_version'] == 3)
            and all(isinstance(edit, dict) for edit in edits),
            'Invalid native approach section proofs')
    restored = raw
    for edit in reversed(edits):
        require(isinstance(edit.get('insertion'), str), 'Invalid native DD approach insertion')
        insertion, offset = edit['insertion'].encode('ascii'), edit.get('insertion_offset')
        require(type(offset) is int and offset >= 0 and insertion and
                restored[offset:offset + len(insertion)] == insertion and restored.count(insertion) == 1,
                'Native DD approach insertion is missing, changed, or nonunique')
        restored = restored[:offset] + restored[offset + len(insertion):]
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
    pins = {_provider(piece).NATIVE_RUL1_SHA256
            for piece in pieces if approaches(piece)}
    require(pins == {_sha(native)}, 'Native DD approach baseline differs from the pinned native RUL1')
    if donors:
        require(donors.get(RUL1) == native, 'Restored native DD RUL1 differs from audited donors')
    result = {**report, 'native_dd_approach_cells_checked': sum(len(item['approaches']) for item in selected),
            'native_dd_rul1_solutions_checked': len(expected_solutions(pieces)),
            'native_dd_dependencies_checked': len(dependencies), 'native_rul1_bytes_preserved': True,
            'native_dd_game_behavior_tested': False}
    if any(piece.get(GHSR_OVERLAY) or piece.get(ORTHOGONAL_OVERLAY)
           or piece.get(Y_JUNCTION_OVERLAY) or piece.get(DIAGONAL_TRANSITION_OVERLAY) for piece in pieces):
        sections = expected_solution_sections(pieces)
        rows = [row for item in selected for row in item['approaches']]
        dd_rows = [row for row in rows if _pair(row)[0] == SECTION and int(row['native_tile_id'],16) >> 16 != 0x5703]
        rail_rows = [row for row in rows if _pair(row)[0] == 'RailMonoRailIntersectionSolutions']
        ground_rows = [row for row in rows if _pair(row)[0] == 'RoadDirtRoadIntersectionSolutions'
                       or int(row['native_tile_id'],16) >> 16 == 0x5703]
        result.update(native_approach_cells_checked=len(rows),
                      native_dd_approach_cells_checked=len(dd_rows),
                      native_ghsr_approach_cells_checked=len(rail_rows),
                      native_approach_sections_checked=len(sections),
                      native_approach_dependencies_checked=len(dependencies),
                      native_dd_dependencies_checked=3 * len({row['native_tile_id'] for row in dd_rows}),
                      native_ghsr_dependencies_checked=3 * len({row['native_tile_id'] for row in rail_rows}),
                      native_rul1_solutions_checked=sum(len(table) for table in sections.values()),
                      native_ghsr_rul1_solutions_checked=len(sections.get('RailMonoRailIntersectionSolutions', {})))
        if any(piece.get(ORTHOGONAL_OVERLAY) or piece.get(Y_JUNCTION_OVERLAY)
               or piece.get(DIAGONAL_TRANSITION_OVERLAY) for piece in pieces):
            result.update(native_ground_rhw_approach_cells_checked=len(ground_rows),
                          existing_native_rul1_solutions_reused=sum(len(table) for table in
                              _existing_solution_sections(pieces).values()),
                          native_ground_rhw_dependencies_checked=2 * len({row['native_tile_id'] for row in ground_rows}))
        if any(piece.get(Y_JUNCTION_OVERLAY) for piece in pieces):
            dd_targets = {int(row['native_tile_id'], 16) for row in dd_rows}
            dd_targets.update(key[2] for piece in pieces if piece.get(Y_JUNCTION_OVERLAY)
                              for key in _provider(piece).additional_dependency_keys(piece))
            result['native_dd_dependencies_checked'] = sum(key[2] in dd_targets for key in dependency_keys(pieces))
        if any(piece.get(DIAGONAL_TRANSITION_OVERLAY) for piece in pieces):
            keys = dependency_keys(pieces)
            result.update(native_diagonal_transition_approach_cells_checked=sum(len(approaches(piece)) for piece in pieces
                          if piece.get(DIAGONAL_TRANSITION_OVERLAY)),
                          native_ground_rhw_dependencies_checked=sum(key[2] >> 16 == 0x5703 for key in keys),
                          native_dd_dependencies_checked=sum(key[2] >> 16 == 0x5753 for key in keys),
                          native_dd_rul1_solutions_checked=sum(value[0] >> 16 == 0x5753
                              for table in sections.values() for value in table.values()))
    return result
