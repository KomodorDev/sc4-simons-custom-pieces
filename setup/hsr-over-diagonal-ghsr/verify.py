"""Independently audit the experimental NAM 50 crossing without running the game.

This reads the generated DAT and original installed donors.  A successful audit
establishes binary structure and path/model consistency, not in-game placement,
traffic, shadows, rendering, or demolition behavior.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import difflib
import hashlib
import json
import math
from pathlib import Path
import re
import struct
import sys

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
sys.path[:0] = [str(PROJECT / 'setup/cam-install/runtime-audit'),
               str(PROJECT / 'setup/tram-under-hsr')]
from read_dbpf import entries, decompress, exemplar
from model_tools import parse_s3d, validate_s3d, valid_frame, positions

TILES = (0x5DD0F200, 0x5DD0F210)
PREVIEW = 0x5DD0F225
PUZZLE = 0xF7A1
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
NETWORK_INI = (0x00000000, 0x8A5971C5, 0x8A5993B9)
MODEL = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
EXEMPLAR = (0x6534284A, 0xA8434037)
EFFECT = (0xEA5118B0, 0xEA5118B1)
SHADOW = (0x7AB50E44, 0x2BC2759A)
EPS = 1e-6


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dbpf(raw):
    """Check archive layout before using the shared decompression reader."""
    require(len(raw) >= 96 and raw[:4] == b'DBPF', 'Invalid DBPF header')
    require(struct.unpack_from('<II', raw, 4) == (1, 0), 'Expected DBPF 1.0')
    require(struct.unpack_from('<I', raw, 32)[0] == 7, 'Expected index version 7')
    count, index, size = struct.unpack_from('<III', raw, 36)
    require(count > 0 and size == count * 20, 'Invalid index size')
    require(index >= 96 and index + size == len(raw), 'Index does not end at EOF')
    keys, spans = set(), []
    for n in range(count):
        kind, group, instance, offset, length = struct.unpack_from('<5I', raw, index + n * 20)
        key = kind, group, instance
        require(key not in keys, f'Duplicate resource {key}')
        require(length > 0 and 96 <= offset < index and offset + length <= index,
                f'Invalid resource bounds for {key}')
        keys.add(key)
        spans.append((offset, offset + length))
    spans.sort()
    require(spans[0][0] == 96 and spans[-1][1] == index, 'Unaccounted body bytes')
    require(all(a[1] == b[0] for a, b in zip(spans, spans[1:])), 'Resource overlap or gap')
    result = {k: decompress(v) for k, v in entries(raw).items()}
    require(set(result) == keys and len(result) == count, 'Reader/index mismatch')
    return result


def parse_paths(raw):
    """Read both relevant SC4PATH versions without discarding a route field."""
    lines = [line.strip() for line in raw.decode('ascii').splitlines()
             if line.strip() and not line.lstrip().startswith('--')]
    require(lines[0] == 'SC4PATHS' and lines[1] in {'1.1', '1.2'}, 'Unsupported path format')
    count, stops, terrain = map(int, lines[2:5])
    require(count > 0 and stops == 0 and terrain in {0, 1}, 'Unexpected path header')
    version, cursor, paths = lines[1], 5, []
    for _ in range(count):
        fields = 5 if version == '1.1' else 6
        header = list(map(int, lines[cursor:cursor + fields]))
        require(len(header) == fields, 'Truncated route header')
        cursor += fields
        if version == '1.1':
            transport, lane, entry, exit_, nodes = header
            compatibility = None
        else:
            transport, lane, entry, exit_, compatibility, nodes = header
        require(nodes >= 2 and entry in range(4) and exit_ in range(4), 'Invalid route header')
        points = [tuple(map(float, line.split(','))) for line in lines[cursor:cursor + nodes]]
        cursor += nodes
        require(len(points) == nodes and all(len(p) == 3 for p in points), 'Truncated route')
        require(all(math.isfinite(x) for p in points for x in p), 'Nonfinite path coordinate')
        paths.append({'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
                      'compatibility': compatibility, 'points': points})
    require(cursor == len(lines), 'Unexpected trailing path data')
    return {'version': version, 'terrain': terrain, 'paths': paths}


def rounded(point):
    return tuple(round(v, 6) for v in point)


def signature(route):
    return route['transport'], route['entry'], route['exit'], tuple(map(rounded, route['points']))


def edge(point):
    x, y, _ = point
    candidates = [abs(x + 8) <= EPS, abs(y - 8) <= EPS,
                  abs(x - 8) <= EPS, abs(y + 8) <= EPS]
    require(sum(candidates) == 1, f'Route endpoint is not on exactly one tile edge: {point}')
    return candidates.index(True)  # West, North, East, South in SC4PATH.


def transform(point, angle, mirror):
    x, y, height = point
    if mirror:
        x = -x
    for _ in range(angle % 4):
        x, y = y, -x
    return x, y, height


def transformed_edge(original, angle, mirror):
    samples = ((-8., 0., 0.), (0., 8., 0.), (8., 0., 0.), (0., -8., 0.))
    return edge(transform(samples[original], angle, mirror))


def check_paths(output, donors):
    hsr = parse_paths(donors[(*PATH, 0x5DD31500)])['paths']
    require(len(hsr) == 2 and all(p['transport'] == 7 for p in hsr), 'Unexpected HSR donor')
    all_paths = []
    for tile, donor_id in zip(TILES, (0x59F3D110, 0x59F3D120)):
        parsed = parse_paths(output[(*PATH, tile)])
        routes = parsed['paths']
        require(parsed['version'] == '1.2' and parsed['terrain'] == 0 and
                all(p['lane'] == 1 and p['compatibility'] == 0 for p in routes),
                'Paths do not preserve native C20A same-network crossing conventions')
        require(len(routes) == 4 and all(p['transport'] == 7 for p in routes),
                'Each tile must contain exactly four Monorail routes')
        source = parse_paths(donors[(*PATH, donor_id)])['paths']
        lower = [p for p in source if p['transport'] == 7]
        require(len(lower) == 2, 'Unexpected native diagonal GHSR donor paths')
        expected = Counter(signature(p) for p in lower + hsr)
        require(Counter(signature(p) for p in routes) == expected,
                f'Custom paths differ from exact installed lower/upper routes for {tile:08x}')
        for route in routes:
            heights = {round(p[2], 6) for p in route['points']}
            require(len(heights) == 1 and next(iter(heights)) in {1., 15.5},
                    'Path crosses between upper and lower railway levels')
            require(edge(route['points'][0]) == route['entry'] and
                    edge(route['points'][-1]) == route['exit'], 'Entry/exit flags disagree with coordinates')
        all_paths.append(routes)

    # Both native donor tiles lie along the same straight line.  Tile 1 is
    # immediately south of tile 0 in path coordinates, exactly as C219/AAC1.
    centers = ((0., 0., 0.), (0., -16., 0.))
    checked = 0
    for mirror in (False, True):
        for angle in range(4):
            starts, ends = [], []
            for tile_no, routes in enumerate(all_paths):
                cx, cy, _ = centers[tile_no]
                for route in routes:
                    points = [transform(p, angle, mirror) for p in route['points']]
                    require(edge(points[0]) == transformed_edge(route['entry'], angle, mirror),
                            'Transformed entry edge mismatch')
                    require(edge(points[-1]) == transformed_edge(route['exit'], angle, mirror),
                            'Transformed exit edge mismatch')
                    for end_no, destination in ((0, starts), (-1, ends)):
                        p = route['points'][end_no]
                        global_point = transform((p[0] + cx, p[1] + cy, p[2]), angle, mirror)
                        is_internal = abs(p[1] - (-8. if tile_no == 0 else 8.)) <= EPS
                        destination.append((tile_no, rounded(global_point), is_internal))
            internal_starts = [item for item in starts if item[2]]
            internal_ends = [item for item in ends if item[2]]
            require(len(internal_starts) == len(internal_ends) == 4,
                    'Expected both directions of both levels on shared boundary')
            require(Counter(point for _, point, _ in internal_starts) ==
                    Counter(point for _, point, _ in internal_ends), 'Disconnected internal railway endpoint')
            for tile_no, point, _ in internal_starts:
                matches = [(other, p) for other, p, inside in internal_ends if inside and p == point]
                require(len(matches) == 1 and matches[0][0] != tile_no,
                        'Ambiguous or same-tile shortcut at shared boundary')
            require(len([item for item in starts if not item[2]]) == 4 and
                    len([item for item in ends if not item[2]]) == 4, 'Unexpected external port count')
            checked += 1
    return {'routes_per_tile': 4, 'checked_rotations_and_mirrors': checked,
            'ground_height_m': 1., 'elevated_height_m': 15.5,
            'exact_installed_path_endpoints': True, 'internal_connections_continuous': True,
            'no_crosslevel_routes': True}


def section_rules(text):
    result, current = {}, None
    for raw in text.splitlines():
        line = raw.split(';', 1)[0].strip()
        if not line:
            continue
        match = re.fullmatch(r'\[HighwayIntersectionInfo_0x([0-9a-fA-F]+)\]', line)
        if match:
            current = int(match[1], 16)
            require(current not in result, 'Duplicate appended puzzle section')
            result[current] = []
        else:
            require(current is not None and '=' in line, f'Unexpected appended rule: {line}')
            key, value = line.split('=', 1)
            result[current].append((key.strip(), value.strip()))
    return result


def compact(value):
    return re.sub(r'\s+', '', value).lower()


def check_controller(output, donors, manifest):
    original, patched = donors[RUL0], output[RUL0]
    audit = manifest['controller_audit']
    ordering = audit['ordering_line'].encode('ascii').rstrip(b'\r\n') + b'\r\n'
    require(patched.count(ordering) == 1 and ordering not in original, 'Invalid new menu entry')
    # The marker locates the appended rules; its text is not accepted as proof
    # that the preceding bytes are the original controller.
    marker = audit.get('marker')
    if marker is None:
        matches = re.findall(rb'\r\n;BEGIN CUSTOM[^\r\n]*\r\n', patched)
        require(len(matches) == 1, 'Could not independently locate controller appendix')
        marker = matches[0]
    elif isinstance(marker, str):
        marker = marker.encode('ascii')
    require(patched.count(marker) == 1, 'Nonunique controller appendix marker')
    body, addition = patched.split(marker)
    require(body.replace(ordering, b'', 1) == original,
            'Original RUL0 rules were changed or removed')
    preceding_line = body[:body.index(ordering)].splitlines()[-1]
    require(preceding_line.startswith(b'AddTypes') and b';Orth HSR x Orth GHSR' in preceding_line,
            'Custom menu entry is not immediately after native GHSR x HSR')
    ids = [int(value, 16) for value in re.findall(rb'\b[0-9A-Fa-f]+\b', ordering.split(b'=', 1)[1].split(b';', 1)[0])]
    require(ids == [PUZZLE + n * 0x10000 for n in range(16)],
            'Wrong GHSR-ring rotation-slot count or puzzle IDs')
    rules = section_rules(addition.decode('ascii'))
    require(set(rules) == set(ids), 'Unexpected appended puzzle sections')
    base = rules[PUZZLE]
    fields = {}
    for key, value in base:
        fields.setdefault(key, []).append(value)
    require(set(fields) == {'Piece', 'PreviewEffect', 'CellLayout', 'CheckType', 'ConsLayout',
                            'AutoTileBase', 'ReplacementIntersection', 'PlaceQueryID', 'Costs'},
            'Unexpected base puzzle rule fields')
    require([compact(v) for v in fields['CellLayout']] == ['.....', '..ys.<', '.rz..', '..^..'],
            'Changed native two-tile construction layout')
    require([compact(v) for v in fields['ConsLayout']] == ['...', '.+.<', '.+.', '.^.'],
            'Puzzle is not the intended two-tile assembly')
    require(set(map(compact, fields['CheckType'])) == {
        'r-monorail:0x00010000,0x00ff0000optional',
        's-monorail:0x00000001,0x000000ffoptional',
        'y-monorail:0x02010200', 'z-monorail:0x02000201'},
        'Construction flags differ from the native same-network AAC1 donor')
    require(int(fields['AutoTileBase'][0], 0) == TILES[0] and
            int(fields['PlaceQueryID'][0], 0) == TILES[0], 'Wrong tile or query IDs')
    require(compact(fields['ReplacementIntersection'][0]) == '0,0', 'Unexpected replacement intersection')
    require(len(fields['PreviewEffect']) == 1, 'Multiple preview effects')
    piece = fields['Piece'][0].split(',')
    require(len(piece) == 5 and all(float(value) == 0 for value in piece[:4]) and
            int(piece[4], 0) == PREVIEW, 'Wrong combined placement-preview model')
    require(int(fields['Costs'][0], 0) == 150, 'Unexpected puzzle construction cost')
    for n in range(1, 8):
        values = dict(rules[PUZZLE + n * 0x10000])
        require(len(values) == len(rules[PUZZLE + n * 0x10000]), 'Duplicate rotation-clone fields')
        expected = {'CopyFrom': hex(PUZZLE if n <= 4 else PUZZLE + 0x40000)}
        if n == 4:
            expected['Transpose'] = '1'
        else:
            expected['Rotate'] = str(n if n < 4 else n - 4)
        require(set(values) == set(expected), 'Unexpected rotation-clone fields')
        for key, value in expected.items():
            require(int(values[key], 0) == int(value, 0), 'Incorrect rotation/transpose clone')
    for n in range(8, 16):
        clone = rules[PUZZLE + n * 0x10000]
        require(len(clone) == 1 and clone[0][0] == 'CopyFrom' and
                int(clone[0][1], 0) == PUZZLE + (n - 8) * 0x10000,
                'GHSR rotation slots 8-15 must repeat the eight unique transformed variants')
    # Cross-check the native same-network precedent itself, rather than only
    # accepting this verifier's literal flags.
    native_text = original.decode('ascii')
    native = native_text.split('[HighwayIntersectionInfo_0x0000AAC1]', 1)[1].split(
        '[HighwayIntersectionInfo_', 1)[0]
    require('CheckType = Y - rail: 0x02010200' in native and
            'CheckType = Z - rail: 0x02000201' in native, 'Installed AAC1 precedent changed')
    return fields['PreviewEffect'][0]


def check_network_ini(output, donors):
    original, patched = donors[NETWORK_INI], output[NETWORK_INI]
    old_lines, new_lines = original.splitlines(keepends=True), patched.splitlines(keepends=True)
    matcher = difflib.SequenceMatcher(a=old_lines, b=new_lines, autojunk=False)
    restored, additions = [], []
    for kind, a0, a1, b0, b1 in matcher.get_opcodes():
        require(kind in {'equal', 'insert'}, 'Original NetworkINI entries changed or removed')
        if kind == 'equal':
            restored.extend(new_lines[b0:b1])
        else:
            additions.extend(new_lines[b0:b1])
    require(b''.join(restored) == original, 'NetworkINI restoration failed')
    inserted = b''.join(additions).decode('ascii')
    mapping_lines = [line.split(';', 1)[0].strip() for line in inserted.splitlines()
                     if line.split(';', 1)[0].strip()]
    require(len(mapping_lines) == 2, 'Expected exactly two explicit new shadow remappings')
    matched = set()
    for line in mapping_lines:
        require('=' in line, 'Invalid inserted INI entry')
        _, value = line.split('=', 1)
        numbers = [int(n.strip(), 0) for n in value.split(',')]
        require(len(numbers) in {4, 6} and numbers[0] in TILES and
                numbers[1:4] == [0xFFFFFFF0, 0x5DD31500, 0x0000000F] and
                (len(numbers) == 4 or numbers[4:] == [0, 0]), 'Unexpected shadow remapping')
        require(numbers[0] not in matched, 'Repeated shadow remapping')
        matched.add(numbers[0])
    require(matched == set(TILES), 'Missing tile shadow mapping')
    section = None
    found = set()
    for raw in patched.decode('latin1').splitlines():
        line = raw.split(';', 1)[0].strip()
        if line.startswith('['):
            section = line.lower()
        if line in mapping_lines:
            require(section == '[shadow remapping]', 'Mapping is outside the shadow section')
            found.add(line)
    require(found == set(mapping_lines), 'Shadow mappings were not found in the active INI')
    return {'original_bytes_preserved': True, 'explicit_upper_deck_shadow_mappings': 2,
            'game_shadow_selection_tested': False}


def referenced_mesh(model, mesh):
    frame = mesh['frames'][0]
    require(all(f == frame for f in mesh['frames']) and valid_frame(model, frame),
            'Expected static single-geometry mesh')
    return tuple(deepcopy(model[name][index]) for name, index in
                 zip(('vertices', 'indices', 'primitives', 'materials'), frame))


def exact_translated_mesh(actual, source, offset):
    if actual[1:] != source[1:]:
        return False
    a, b = actual[0], source[0]
    if (a['format'], a['flags'], a['stride'], len(a['data'])) != (
            b['format'], b['flags'], b['stride'], len(b['data'])):
        return False
    pa, pb = positions(a), positions(b)
    return all(a['data'][o + 12:o + a['stride']] == b['data'][o + 12:o + b['stride']]
               for o in range(0, len(a['data']), a['stride'])) and all(
        abs(pa[i][n] - pb[i][n] - offset[n]) < 2e-6
        for i in range(len(pa)) for n in range(3))


def check_models(output, donors):
    checks = []
    models = {}
    for key, raw in output.items():
        if key[0] == MODEL[0]:
            require(key[:2] == MODEL, 'Unexpected model group')
            model = parse_s3d(raw)
            checks.append(validate_s3d(model))
            models[key[2]] = model
    expected = {tile + zoom for tile in TILES for zoom in range(5)} | {PREVIEW}
    require(set(models) == expected, 'Unexpected/missing zoom or preview models')
    hsr = parse_s3d(donors[(*MODEL, 0x5DD31500)])
    valid_hsr = [referenced_mesh(hsr, mesh) for mesh in hsr['meshes']
                 if all(valid_frame(hsr, f) for f in mesh['frames'])]
    require(len(valid_hsr) == 1, 'HSR donor valid topology changed')
    expected_preview = []
    for number, (tile, donor_id) in enumerate(zip(TILES, (0x59F3D114, 0x59F3D124))):
        donor_model = parse_s3d(donors[(*MODEL, donor_id)])
        source_lower = [referenced_mesh(donor_model, mesh) for mesh in donor_model['meshes']
                        if mesh['name'].rstrip(b'\0') == b'HSR']
        require(len(source_lower) == 1, 'Unexpected native diagonal GHSR tile topology')
        reference = output[(*MODEL, tile)]
        require(all(output[(*MODEL, tile + zoom)] == reference for zoom in range(5)),
                'Zoom models unexpectedly differ')
        model = models[tile]
        mesh_items = [referenced_mesh(model, mesh) for mesh in model['meshes']]
        lower = [item for item in mesh_items if max(p[1] for p in positions(item[0])) < 3]
        upper = [item for item in mesh_items if min(p[1] for p in positions(item[0])) > 13]
        require(len(mesh_items) == len(lower) + len(upper) == 2 and len(lower) == len(upper) == 1,
                'Each tile must contain exactly one GHSR mesh and one elevated HSR deck')
        require(upper[0] == valid_hsr[0], 'Upper deck buffers differ from the native straight HSR')
        require(lower[0] == source_lower[0], 'Lower mesh buffers differ from the native GHSR half')
        expected_preview.extend((item, (0., 0., number * 16.)) for item in mesh_items)
    preview_model = models[PREVIEW]
    preview_meshes = [referenced_mesh(preview_model, mesh) for mesh in preview_model['meshes']]
    require(len(preview_meshes) == len(expected_preview) == 4, 'Preview must contain both complete tiles')
    for actual, (source, offset) in zip(preview_meshes, expected_preview):
        require(exact_translated_mesh(actual, source, offset),
                'Combined preview does not match its two tiles and native tile spacing')
    for tile in TILES:
        record = exemplar(output[(*EXEMPLAR, tile)])
        props = {int(p['id'], 16): p['values'] for p in record['properties']}
        require(props[0x10] == [11] and props[0x27812823] == [*MODEL, *range(tile, tile + 5)],
                'Incorrect network exemplar/model references')
    return checks


def check_effect(output, donors, preview_name):
    old = donors[(*EFFECT, 0x59F3D115)]
    candidates = [(key, value) for key, value in output.items() if key[:2] == EFFECT]
    require(len(candidates) == 1, 'Expected one cloned preview effect')
    key, effect = candidates[0]
    require(key[2] in {TILES[0], PREVIEW}, 'Unexpected preview effect resource ID')
    original_name = b'preview_hsrp_subrail____001'
    name = preview_name.encode('ascii')
    require(len(name) == len(original_name) and effect.count(name) == old.count(original_name) > 0,
            'Wrong preview effect name or length')
    require(old.count(struct.pack('<I', 0x59F3D115)) > 0, 'Preview model donor reference missing')
    restored = effect.replace(name, original_name).replace(struct.pack('<I', PREVIEW),
                                                         struct.pack('<I', 0x59F3D115))
    require(restored == old, 'Effect differs beyond expected name/model substitutions')
    return {'exact_native_effect_clone': True, 'preview_model_reference': f'{PREVIEW:08x}'}


def check_resource_closure(output, manifest):
    expected = {RUL0, NETWORK_INI, (*MODEL, PREVIEW), (*EFFECT, PREVIEW)}
    for tile in TILES:
        expected.update({(*MODEL, tile + zoom) for zoom in range(5)})
        expected.update({(*PATH, tile), (*EXEMPLAR, tile), (0x2026960B, 0x2A592FD1, tile)})
        text = output[0x2026960B, 0x2A592FD1, tile]
        chars, control = struct.unpack_from('<HH', text)
        require(control == 0x1000 and len(text) == 4 + chars * 2 and
                text[4:].decode('utf-16-le') == manifest['name'], 'Invalid English puzzle description')
    require(set(output) == expected, 'Unexpected or missing output resource')
    controller_path = next(Path(item['path']) for item in manifest['donors']
                           if Path(item['path']).name == 'NetworkAddonMod_Controller.dat')
    plugins = next((p for p in controller_path.parents if p.name == 'Plugins'), None)
    require(plugins is not None, 'Cannot identify original Plugins tree for dependency audit')
    require(not Path(manifest['output']).resolve().is_relative_to(plugins.resolve()),
            'Prototype was installed into Plugins during static-only verification')
    textures = {texture for key, raw in output.items() if key[0] == MODEL[0]
                for material in parse_s3d(raw)['materials'] for texture in material['textures']}
    missing_textures = set(textures)
    missing_shadows = {(*SHADOW, 0x5DD31500 + zoom) for zoom in range(5)}
    collisions = []
    for path in plugins.rglob('*'):
        if not path.is_file() or path.suffix.lower() not in {'.dat', '.sc4lot', '.sc4model', '.sc4desc'}:
            continue
        with path.open('rb') as handle:
            header = handle.read(96)
            if len(header) < 96 or header[:4] != b'DBPF':
                continue
            count, index, size = struct.unpack_from('<III', header, 36)
            require(size == count * 20, f'Unsupported installed index: {path.name}')
            handle.seek(index)
            records = handle.read(size)
        require(len(records) == size, f'Truncated installed archive index: {path.name}')
        for offset in range(0, size, 20):
            key = struct.unpack_from('<III', records, offset)
            if key[0] == 0x7AB50E44:
                missing_textures.discard(key[2])
            missing_shadows.discard(key)
            if key in expected and key not in {RUL0, NETWORK_INI}:
                collisions.append((str(path), key))
    require(not missing_textures, f'Missing material textures: {missing_textures}')
    require(not missing_shadows, f'Missing native HSR shadow textures: {missing_shadows}')
    require(not collisions, f'Custom IDs are already present in installed Plugins: {collisions}')
    return {'all_twenty_resources_accounted_for': True, 'english_descriptions_valid': True,
            'material_texture_dependencies_found': sorted(f'{tid:08x}' for tid in textures),
            'native_hsr_shadow_dependencies_found': 5, 'installed_custom_resource_collisions': 0,
            'prototype_remains_outside_plugins': True}


def main():
    manifest = json.loads((HERE / 'dist/build-manifest.json').read_text())
    output_path = Path(manifest['output']).resolve()
    require(output_path.is_relative_to((HERE / 'dist').resolve()), 'Prototype output must stay in project dist')
    raw = output_path.read_bytes()
    require(sha(raw) == manifest['sha256'], 'Output archive hash mismatch')
    require([int(value, 16) if isinstance(value, str) else value for value in manifest['tile_ids']] == list(TILES),
            'Manifest tile IDs differ from intended prototype')
    preview = manifest['preview_id']
    require((int(preview, 16) if isinstance(preview, str) else preview) == PREVIEW,
            'Manifest preview ID differs from intended prototype')
    output = dbpf(raw)
    donors = {}
    donor_checks = []
    for item in manifest['donors']:
        path = Path(item['path'])
        content = path.read_bytes()
        require(sha(content) == item['sha256'], f'Installed donor changed: {path.name}')
        donor_checks.append({'name': path.name, 'sha256': sha(content)})
        for key, value in entries(content).items():
            # The compression directory is archive-specific metadata and has
            # the same TGI in otherwise unrelated donor archives.
            if key[0] == 0xE86B1EEF:
                continue
            data = decompress(value)
            require(key not in donors or donors[key] == data, f'Conflicting donor resource {key}')
            donors[key] = data
    overlaps = set(output) & set(donors)
    require(overlaps == {RUL0, NETWORK_INI}, f'Unexpected existing resources overlaid: {overlaps}')
    preview_name = check_controller(output, donors, manifest)
    ini_checks = check_network_ini(output, donors)
    path_checks = check_paths(output, donors)
    model_checks = check_models(output, donors)
    effect_checks = check_effect(output, donors, preview_name)
    closure_checks = check_resource_closure(output, manifest)
    result = {'static_checks_passed': True, 'dbpf_resources': len(output),
              'sha256': sha(raw), 'donors': donor_checks,
              'controller_original_bytes_preserved': True, 'network_ini': ini_checks,
              'paths': path_checks, 'models': model_checks, 'preview_effect': effect_checks,
              'resources_and_dependencies': closure_checks,
              'in_game_placement_tested': False, 'in_game_rendering_tested': False,
              'in_game_traffic_tested': False, 'in_game_shadow_selection_tested': False,
              'in_game_bulldozing_tested': False,
              'verification_limit': 'Static binary and connectivity audit; SimCity 4 has not executed this prototype.'}
    (HERE / 'dist/verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'static_checks_passed': True, 'resources': len(output), 'sha256': sha(raw),
                      'path_variants_checked': 8, 'in_game_tested': False,
                      'report': str(HERE / 'dist/verification.json')}, indent=2))


if __name__ == '__main__':
    main()
