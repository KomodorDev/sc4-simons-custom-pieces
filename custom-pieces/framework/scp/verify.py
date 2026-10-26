"""Independent package, construction, model and traffic-path verification.

Portable verification needs only the output folder. When its optional local
input-audit.json is available, this also compares against unchanged NAM donors.
Neither mode executes SimCity 4 or treats file checks as an in-game test.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import struct

from .catalog import validate_catalog, auto_tile_base
from .dbpf import entries, decompress, exemplar, encode_exemplar, tgi_string, require
from .menu import validate_menu_resources, MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
from .models import parse_s3d, validate_s3d, valid_frame, positions

RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
NETWORK_INI = (0, 0x8A5971C5, 0x8A5993B9)
S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
EXEMPLAR = (0x6534284A, 0xA8434037)
EFFECT = (0xEA5118B0, 0xEA5118B1)
LTEXT = (0x2026960B, 0x2A592FD1)
SHADOW = (0x7AB50E44, 0x2BC2759A)
EPS = 2e-6


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def safe_file(root, name):
    require(isinstance(name, str) and name and '\\' not in name and ':' not in name,
            'Invalid output-relative path')
    parts = PurePosixPath(name)
    require(not parts.is_absolute() and '..' not in parts.parts and str(parts) == name,
            'Noncanonical or escaping output-relative path')
    target = root.joinpath(*parts.parts)
    require(not any(p.is_symlink() for p in (target, *target.parents) if p != root.parent),
            'Symlinks are not allowed in a build output path')
    require(target.resolve().is_relative_to(root.resolve()), 'Output path escapes build root')
    return target


def strict_dbpf(raw):
    require(len(raw) >= 96 and raw[:4] == b'DBPF', 'Invalid DBPF header')
    require(struct.unpack_from('<II', raw, 4) == (1, 0), 'Expected DBPF 1.0')
    require(struct.unpack_from('<I', raw, 32)[0] == 7, 'Expected DBPF index version 7')
    count, index, size = struct.unpack_from('<III', raw, 36)
    require(count > 0 and size == count * 20 and index >= 96 and index + size == len(raw),
            'Invalid DBPF index location or size')
    keys, spans = set(), []
    for n in range(count):
        kind, group, iid, start, length = struct.unpack_from('<5I', raw, index + n * 20)
        require((kind, group, iid) not in keys, 'Duplicate TGI inside DBPF')
        require(length > 0 and 96 <= start < index and start + length <= index,
                'DBPF body extends outside body area')
        keys.add((kind, group, iid)); spans.append((start, start + length))
    spans.sort()
    require(spans[0][0] == 96 and spans[-1][1] == index and
            all(a[1] == b[0] for a, b in zip(spans, spans[1:])), 'DBPF gaps or overlapping resources')
    parsed = {key: decompress(value) for key, value in entries(raw).items()}
    require(set(parsed) == keys, 'DBPF parser/index mismatch')
    return parsed


def parse_paths(raw):
    lines = [line.strip() for line in raw.decode('ascii').splitlines()
             if line.strip() and not line.lstrip().startswith('--')]
    require(len(lines) >= 5 and lines[0] == 'SC4PATHS' and lines[1] in {'1.1', '1.2'},
            'Unsupported SC4PATH format')
    count, stops, terrain = map(int, lines[2:5])
    require(count > 0 and stops == 0 and terrain in {0, 1}, 'Invalid SC4PATH header')
    cursor, routes = 5, []
    for _ in range(count):
        fields = 5 if lines[1] == '1.1' else 6
        values = list(map(int, lines[cursor:cursor + fields])); cursor += fields
        require(len(values) == fields, 'Truncated SC4PATH route')
        if fields == 5:
            transport, lane, entry, exit_, nodes = values
            compatibility = None
        else:
            transport, lane, entry, exit_, compatibility, nodes = values
        require(nodes >= 2 and entry in range(4) and exit_ in range(4), 'Invalid path directions')
        points = [tuple(map(float, line.split(','))) for line in lines[cursor:cursor + nodes]]
        cursor += nodes
        require(len(points) == nodes and all(len(p) == 3 and all(math.isfinite(v) for v in p) for p in points),
                'Invalid path coordinates')
        routes.append({'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
                       'compatibility': compatibility, 'points': points})
    require(cursor == len(lines), 'Unexpected trailing SC4PATH data')
    return {'version': lines[1], 'terrain': terrain, 'routes': routes}


def point_key(point):
    return tuple(round(v, 6) for v in point)


def signature(route):
    return route['transport'], route['entry'], route['exit'], tuple(map(point_key, route['points']))


def transform(point, angle, mirror=False):
    x, y, z = point
    if mirror:
        x = -x
    for _ in range(angle % 4):
        x, y = y, -x
    return x, y, z


def edge(point):
    x, y, _ = point
    edges = [abs(x + 8) <= EPS, abs(y - 8) <= EPS, abs(x - 8) <= EPS, abs(y + 8) <= EPS]
    require(sum(edges) == 1, 'Path endpoint is not on exactly one tile edge')
    return edges.index(True)


def route(transport, entry, exit_, *points):
    return {'transport': transport, 'entry': entry, 'exit': exit_, 'points': list(points)}


HSR_ROUTES = [route(7, 3, 1, (2., -8., 15.5), (2., 8., 15.5)),
              route(7, 1, 3, (-2., 8., 15.5), (-2., -8., 15.5))]
GHSR_ROUTES = [
    [route(7, 3, 2, (2.9, -8., 1.), (8., -2.8, 1.)),
     route(7, 2, 3, (8., 2.9, 1.), (-2.9, -8., 1.))],
    [route(7, 1, 0, (-2.9, 8., 1.), (-8., 2.8, 1.)),
     route(7, 0, 1, (-8., -2.9, 1.), (2.9, 8., 1.))],
]


def check_piece_paths(resources, piece):
    if piece['recipe'].startswith('hsr_component_'):
        from scp_hsr.hsr_components_verify import check_paths
        return check_paths(resources, piece)
    if piece['recipe'] == 'directional_hsr_t_smooth_diagonal_at_grade':
        from scp_hsr.directional_diagonal_t_verify import check_paths
        return check_paths(resources, piece)
    if piece['recipe'].startswith('directional_'):
        from scp_hsr.directional_t_verify import check_paths
        return check_paths(resources, piece)
    if piece['recipe'].startswith('interchange_'):
        from scp_hsr.interchange_verify import check_paths
        return check_paths(resources, piece)
    if piece['recipe'].startswith('rail_') and piece['recipe'].endswith('_revised'):
        from scp_hsr.rail_repair_verify import check_paths
        return check_paths(resources, piece)
    if piece['recipe'].startswith('rail_'):
        from scp_hsr.rail_feature_verify import check_paths
        return check_paths(resources, piece)
    from scp_hsr.crossings import RECIPES, check_paths
    if piece['recipe'] in RECIPES:
        return check_paths(resources, piece)
    tiles = list(map(number, piece['tile_ids']))
    recipe = piece['recipe']
    require(recipe in {'hsr_diagonal_ghsr', 'tram_under_hsr'}, 'Recipe requires an independent verifier')
    parsed = [parse_paths(resources[*PATH, tile]) for tile in tiles]
    if recipe == 'hsr_diagonal_ghsr':
        require(len(tiles) == 2, 'Diagonal GHSR crossing requires two tiles')
        expected = [HSR_ROUTES + lower for lower in GHSR_ROUTES]
        for item in parsed:
            require(item['version'] == '1.2' and item['terrain'] == 0 and
                    len(item['routes']) == 4 and all(p['lane'] == 1 and p['compatibility'] == 0
                                                   for p in item['routes']),
                    'Changed native same-network crossing path conventions')
    else:
        require(len(tiles) == 1, 'Ground tram crossing requires one tile')
        expected = [[route(t, 3, 1, (2., -8., 0.), (2., 8., 0.)) for t in (6, 3)] +
                    [route(t, 1, 3, (-2., 8., 0.), (-2., -8., 0.)) for t in (6, 3)] +
                    [route(7, 0, 2, (-8., -2., 15.5), (8., -2., 15.5)),
                     route(7, 2, 0, (8., 2., 15.5), (-8., 2., 15.5))]]
        require(parsed[0]['version'] == '1.1' and parsed[0]['terrain'] == 1 and
                len(parsed[0]['routes']) == 6 and all(p['lane'] == 0 for p in parsed[0]['routes']),
                'Changed native tram crossing path conventions')
    for item, wanted in zip(parsed, expected):
        require(Counter(map(signature, item['routes'])) == Counter(map(signature, wanted)),
                'Traffic paths differ from audited installed endpoint, height, or direction values')
        for path in item['routes']:
            require(len({round(p[2], 6) for p in path['points']}) == 1, 'Cross-level shortcut route')
            require(edge(path['points'][0]) == path['entry'] and edge(path['points'][-1]) == path['exit'],
                    'Path entry/exit direction disagrees with endpoint')
    samples = ((-8., 0., 0.), (0., 8., 0.), (8., 0., 0.), (0., -8., 0.))
    for mirror in (False, True):
        for angle in range(4):
            starts, ends = [], []
            for tile_no, item in enumerate(parsed):
                for path in item['routes']:
                    for endpoint, port, target in ((path['points'][0], path['entry'], starts),
                                                   (path['points'][-1], path['exit'], ends)):
                        require(edge(transform(endpoint, angle, mirror)) == edge(transform(samples[port], angle, mirror)),
                                'Rotated/mirrored endpoint has the wrong edge')
                        global_point = (endpoint[0], endpoint[1] - 16. * tile_no, endpoint[2])
                        internal = recipe == 'hsr_diagonal_ghsr' and abs(endpoint[1] - (-8. if tile_no == 0 else 8.)) < EPS
                        target.append((tile_no, point_key(transform(global_point, angle, mirror)), internal))
            if recipe == 'hsr_diagonal_ghsr':
                ins, outs = [p for p in starts if p[2]], [p for p in ends if p[2]]
                require(len(ins) == len(outs) == 4 and Counter(p for _, p, _ in ins) == Counter(p for _, p, _ in outs),
                        'Disconnected traffic paths between the two crossing tiles')
                for tile_no, point, _ in ins:
                    matches = [other for other, p, _ in outs if p == point]
                    require(len(matches) == 1 and matches[0] != tile_no, 'Ambiguous crossing connection')
    return {'tile_count': len(tiles), 'rotations_and_mirrors_checked': 8,
            'exact_audited_paths': True, 'no_crosslevel_routes': True}


def mesh_data(model, mesh):
    frame = mesh['frames'][0]
    require(all(f == frame for f in mesh['frames']) and valid_frame(model, frame), 'Expected valid static mesh')
    return tuple(deepcopy(model[name][index]) for name, index in
                 zip(('vertices', 'indices', 'primitives', 'materials'), frame))


def translated(actual, source, delta):
    # S3D stores float32 coordinates. Long footprints need the expected offset
    # rounded to that same representation, rather than widening every check.
    if actual[1:] != source[1:]:
        return False
    a, b = actual[0], source[0]
    if (a['flags'], a['format'], a['stride'], len(a['data'])) != (b['flags'], b['format'], b['stride'], len(b['data'])):
        return False
    pa, pb = positions(a), positions(b)
    return all(a['data'][i + 12:i + a['stride']] == b['data'][i + 12:i + b['stride']]
               for i in range(0, len(a['data']), a['stride'])) and all(
        abs(pa[i][n] - struct.unpack('<f', struct.pack('<f', pb[i][n] + delta[n]))[0]) <= EPS
        for i in range(len(pa)) for n in range(3))


def rotated_mesh(source, angle):
    item = deepcopy(source)
    raw = bytearray(item[0]['data'])
    for pos in range(0, len(raw), item[0]['stride']):
        x, y, z = struct.unpack_from('<3f', raw, pos)
        for _ in range(angle % 4):
            x, z = z, -x
        struct.pack_into('<3f', raw, pos, x, y, z)
    item[0]['data'] = bytes(raw)
    return item


def check_piece_models(resources, piece, donors):
    render_report = check_piece_render_budget(resources, piece)
    result = _check_piece_geometry(resources, piece, donors)
    result['render_groups'] = render_report
    return result


def check_piece_render_budget(resources, piece):
    """Check actual exported models, including every zoom and placement preview.

    Equal zoom payloads need decoding only once. Native donor groups are not
    subject to the stricter SCP authoring budget.
    """
    from .render_meshes import assert_render_budget
    keys = {(*S3D, number(piece['preview_id']))}
    keys.update((*S3D, number(tile) + zoom)
                for tile in piece['tile_ids'] for zoom in range(5))
    payloads = dict.fromkeys(resources[key] for key in sorted(keys))
    reports = [assert_render_budget(parse_s3d(raw)) for raw in payloads]
    return {'all_authored_groups_within_budget': True,
            'model_resources_checked': len(keys),
            'distinct_model_payloads_checked': len(payloads),
            'details': reports}


def _check_piece_geometry(resources, piece, donors):
    if piece['recipe'].startswith('hsr_component_'):
        from scp_hsr.hsr_components_verify import check_models
        return check_models(resources, piece, donors)
    if piece['recipe'] == 'directional_hsr_t_smooth_diagonal_at_grade':
        from scp_hsr.directional_diagonal_t_verify import check_models
        return check_models(resources, piece, donors)
    if piece['recipe'].startswith('directional_'):
        from scp_hsr.directional_t_verify import check_models
        return check_models(resources, piece, donors)
    if piece['recipe'].startswith('interchange_'):
        from scp_hsr.interchange_verify import check_models
        return check_models(resources, piece, donors)
    if piece['recipe'].startswith('rail_') and piece['recipe'].endswith('_revised'):
        from scp_hsr.rail_repair_verify import check_models
        return check_models(resources, piece, donors)
    if piece['recipe'].startswith('rail_'):
        from scp_hsr.rail_feature_verify import check_models
        return check_models(resources, piece, donors)
    from scp_hsr.crossings import RECIPES, check_models
    if piece['recipe'] in RECIPES:
        return check_models(resources, piece, donors)
    tiles, preview_id = list(map(number, piece['tile_ids'])), number(piece['preview_id'])
    texture_ids, preview_expected, models_checked = set(), [], 0
    for n, tile in enumerate(tiles):
        raw = resources[*S3D, tile]
        require(all(resources[*S3D, tile + zoom] == raw for zoom in range(5)), 'Unexpected differing zoom model')
        model = parse_s3d(raw)
        for zoom in range(5):
            validate_s3d(parse_s3d(resources[*S3D, tile + zoom])); models_checked += 1
        items = [mesh_data(model, mesh) for mesh in model['meshes']]
        lower = [item for item in items if max(p[1] for p in positions(item[0])) < 3.]
        upper = [item for item in items if min(p[1] for p in positions(item[0])) > 14.]
        require(len(items) == 2 and len(lower) == len(upper) == 1, 'Expected ground track and clear elevated deck only')
        if donors:
            hsr = parse_s3d(donors[*S3D, 0x5DD31500])
            hsr_items = [mesh_data(hsr, mesh) for mesh in hsr['meshes']
                         if all(valid_frame(hsr, f) for f in mesh['frames'])]
            require(len(hsr_items) == 1, 'Unexpected HSR donor topology')
            expected_upper = hsr_items[0]
            if piece['recipe'] == 'tram_under_hsr':
                expected_upper = rotated_mesh(expected_upper, 1)
                donor = parse_s3d(donors[*S3D, 0x580E0700])
                expected_lower = [mesh_data(donor, mesh) for mesh in donor['meshes']
                                  if all(valid_frame(donor, f) for f in mesh['frames']) and
                                  max(abs(p[1]) for p in positions(donor['vertices'][mesh['frames'][0][0]])) < .001]
            else:
                donor = parse_s3d(donors[*S3D, (0x59F3D114, 0x59F3D124)[n]])
                expected_lower = [mesh_data(donor, mesh) for mesh in donor['meshes'] if mesh['name'].rstrip(b'\0') == b'HSR']
            require(upper[0] == expected_upper and len(expected_lower) == 1 and lower[0] == expected_lower[0],
                    'Crossing model geometry, UVs, or material differs from unchanged native donors')
        record = exemplar(resources[*EXEMPLAR, tile])
        props = {number(p['id']): p['values'] for p in record['properties']}
        require(props[0x10] == [11] and props[0x27812823] == [*S3D, *range(tile, tile + 5)],
                'Network exemplar points to wrong zoom models')
        preview_expected.extend((item, (0., 0., n * 16.)) for item in items)
        texture_ids.update(tid for material in model['materials'] for tid in material['textures'])
    preview = parse_s3d(resources[*S3D, preview_id])
    validate_s3d(preview); models_checked += 1
    actual = [mesh_data(preview, mesh) for mesh in preview['meshes']]
    require(len(actual) == len(preview_expected) and
            all(translated(item, source, delta) for item, (source, delta) in zip(actual, preview_expected)),
            'Combined placement preview differs from the actual tile models or spacing')
    return {'models_checked': models_checked, 'native_buffer_comparison': bool(donors),
            'preview_matches_tiles': True, 'texture_ids': sorted(texture_ids)}


def read_ltext(raw):
    require(len(raw) >= 4, 'Truncated LTEXT')
    chars, control = struct.unpack_from('<HH', raw)
    require(control == 0x1000 and len(raw) == 4 + chars * 2, 'Invalid LTEXT header')
    return raw[4:].decode('utf-16-le')


def menu_baseline():
    """Audited native NAM50 GHSR button fields, for portable verification."""
    values = [(0x10, 0x300, 0, [40]), (0x20, 0xC00, 0x80, 'Ground High Speed Rail'),
              (0x4001, 0x300, 0, [0]), (0x49CAC341, 0x800, 0, [0]),
              (0x8A2602B8, 0x300, 0, [0x6A47C200]), (0x8A2602B9, 0x300, 0, [0x7011111F]),
              (0x8A2602BB, 0x300, 0, [0x6A47C200]),
              (0x8A416A99, 0x300, 0x80, [*TITLE, 0x6A47C200]),
              (0x8A94EEE0, 0x900, 0x80, [0.]),
              (0xCA416AB5, 0x300, 0x80, [*DESCRIPTION, 0x6A47C200])]
    return encode_exemplar({'parent': [0, 0, 0], 'properties': [
        {'id': hex(pid), 'type': hex(kind), 'key_type': hex(key), 'values': value}
        for pid, kind, key, value in values]})


def parse_rules(text):
    """Parse generator fragments; check_construction verifies full RUL0 scope."""
    rings, sections, current = [], {}, None
    for raw in text.splitlines():
        line = raw.split(';', 1)[0].strip()
        if not line:
            continue
        require('=' in line or line.startswith('['), 'Invalid appended RUL0 syntax')
        if line.startswith('RotationRing'):
            rings.append([int(n.strip(), 16) for n in line.split('=', 1)[1].split(',')])
            continue
        require(not line.startswith('AddTypes'), 'Custom pieces must not extend an existing NAM menu ring')
        match = re.fullmatch(r'\[HighwayIntersectionInfo_0x([0-9a-fA-F]+)\]', line)
        if match:
            current = int(match[1], 16)
            require(current not in sections, 'Duplicate custom puzzle section')
            sections[current] = []
        else:
            require(current is not None, 'Rule property outside puzzle section')
            key, value = line.split('=', 1)
            sections[current].append((key.strip(), value.strip()))
    return rings, sections


def check_rotation_ordering(raw, expected_rings):
    """Independently inspect active sections in the actual saved controller."""
    section, ordering_count, rings = None, 0, []
    all_states = set()
    for raw_line in raw.decode('ascii').splitlines():
        line = raw_line.split(';', 1)[0].strip()
        if not line:
            continue
        header = re.fullmatch(r'\[([^\]]+)\]', line)
        if header:
            section = header[1].strip().lower()
            ordering_count += section == 'ordering'
            continue
        if line.lower().startswith('rotationring'):
            require(section == 'ordering', 'RotationRing is outside the active [Ordering] section')
            match = re.fullmatch(r'RotationRing\s*=\s*(.+)', line, re.I)
            require(match is not None, 'Malformed RotationRing property in controller')
            tokens = [token.strip() for token in match[1].split(',')]
            require(tokens and all(re.fullmatch(r'(?:0x)?[0-9a-f]{1,8}', token, re.I)
                                   for token in tokens), 'Malformed RotationRing state identifier')
            ring = [int(token, 16) for token in tokens]
            require(len(set(ring)) == len(ring) and not all_states.intersection(ring),
                    'A rule belongs to more than one RotationRing or is repeated')
            all_states.update(ring)
            rings.append(ring)
    require(ordering_count == 1, 'Controller requires exactly one active [Ordering] section')
    custom_states = {state for ring in expected_rings for state in ring}
    custom_rings = [ring for ring in rings if custom_states.intersection(ring)]
    require(custom_rings == expected_rings,
            'Custom RotationRing entries in [Ordering] differ from the selected pieces')
    return {'ordering_sections_checked': ordering_count,
            'custom_rotation_rings_in_ordering': len(custom_rings),
            'native_rotation_rings_preserved': len(rings) - len(custom_rings)}


def compact(value):
    return re.sub(r'\s+', '', value).lower()


def check_emitted_runtime_addresses(fields, piece):
    """Decode actual CellLayout cells and the executable's byte-key map.

    This intentionally does not call a writer or the catalogue's address
    simulator. Check-only/optional cells do not enter the modeled bounding
    box. Physical placement uses a one-byte key whose later row-major entry
    overwrites the earlier model offset, followed by ADD of AutoTileBase.
    """
    palette = {}
    for value in fields['CheckType']:
        match = re.fullmatch(r'\s*([A-Za-z])\s*-\s*(.+)', value)
        require(match and match[1] not in palette,
                'Emitted cell-check palette has an invalid or duplicate symbol')
        palette[match[1]] = not bool(re.search(r'\b(?:check|optional)\b', match[2], re.I))
    rows = [re.sub(r'\s+', '', value) for value in fields['CellLayout']]
    column_anchors = [x for line in rows for x, symbol in enumerate(line) if symbol == '^']
    row_anchors = [y for y, line in enumerate(rows) for symbol in line if symbol == '<']
    require(len(column_anchors) == len(row_anchors) == 1,
            'Emitted CellLayout requires one column anchor and one row anchor')
    built = []
    for y, line in enumerate(rows):
        for x, symbol in enumerate(line):
            if symbol in '.^<':
                continue
            require(symbol == '+' or symbol in palette,
                    'Emitted CellLayout uses an undefined construction symbol')
            if symbol == '+' or palette[symbol]:
                built.append((x, y))
    require(built, 'Emitted CellLayout contains no modeled cells')
    width, depth = piece['footprint']
    declared_cells = [tuple(cell) for cell in piece.get('cells',
                      [[x, y] for y in range(depth) for x in range(width)])]
    intended_ids = list(map(number, piece['tile_ids']))
    require(len(declared_cells) == len(intended_ids) and
            len(set(declared_cells)) == len(declared_cells),
            'Declared modeled cells do not uniquely identify the allocated models')
    intended = dict(zip(declared_cells, intended_ids))
    actual_cells = [(x-column_anchors[0], y-row_anchors[0]) for x, y in built]
    require(set(actual_cells) == set(declared_cells),
            f'{piece["id"]}: emitted modeled cells differ from the allocated physical cells')
    origin_x, origin_y = min(x for x, _ in built), min(y for _, y in built)
    relative = [(x-origin_x, y-origin_y) for x, y in built]
    keys = [((row << 4)+column+1) & 0xff for column, row in relative]
    offsets = {}
    for key, (column, row) in zip(keys, relative):
        offsets[key] = column*256+row*16
    base_values = fields['AutoTileBase']
    require(len(base_values) == 1, 'Emitted rules require exactly one AutoTileBase')
    base = int(base_values[0], 0)
    selected = [(base+offsets[key]) & 0xffffffff for key in keys]
    wrong = sum(iid != intended[cell] for iid, cell in zip(selected, actual_cells))
    require(len(offsets) == len(built),
            f'{piece["id"]}: emitted auto-tile byte-key collision: '
            f'{wrong} cells select the wrong cell models')
    require(not wrong,
            f'{piece["id"]}: emitted AutoTileBase selects the wrong cell models '
            f'after modeled-origin normalization ({wrong} cells)')
    return {'cells_checked': len(built), 'unique_byte_keys': len(offsets),
            'modeled_origin': [origin_x-column_anchors[0], origin_y-row_anchors[0]],
            'wrong_model_selections': wrong}


def check_construction(resources, pieces, manifest, donors):
    overlay = manifest['overlay']
    rul = overlay['rul0']
    suffix = rul['suffix'].encode('latin1')
    require(suffix and resources[RUL0].endswith(suffix), 'RUL0 appendix differs from manifest')
    ordering = rul.get('ordering_insertion', '').encode('ascii')
    require(ordering, 'RUL0 is missing its [Ordering] rotation insertion; rebuild the controller')
    body = resources[RUL0][:-len(suffix)]
    require(body.count(ordering) == 1, 'Missing or nonunique RUL0 Ordering insertion')
    restored = body.replace(ordering, b'', 1)
    require(sha(restored) == rul['base_sha256'], 'Original RUL0 rules were changed, removed, or had menu insertions')
    if donors:
        require(restored == donors[RUL0], 'Restored RUL0 differs from local native controller')
    rings, ordering_rules = parse_rules(ordering.decode('ascii'))
    require(not ordering_rules, 'Ordering insertion must contain rotation lists only')
    appended_rings, rules = parse_rules(suffix.decode('ascii'))
    require(not appended_rings, 'RotationRing entries must not appear in the puzzle definition appendix')
    expected_rings = [[number(piece['puzzle_id']) + n * 0x10000 for n in range(8)] for piece in pieces]
    require(rings == expected_rings and set(rules) == {value for ring in expected_rings for value in ring},
            'Custom root rings must contain exactly eight states per enabled piece')
    ordering_report = check_rotation_ordering(resources[RUL0], expected_rings)
    for piece in pieces:
        independently_verified_construction = False
        root, tile, preview = number(piece['puzzle_id']), number(piece['tile_ids'][0]), number(piece['preview_id'])
        fields = {}
        for key, value in rules[root]:
            fields.setdefault(key, []).append(value)
        require(set(fields) == {'Piece', 'PreviewEffect', 'CellLayout', 'CheckType', 'ConsLayout',
                                'AutoTileBase', 'ReplacementIntersection', 'PlaceQueryID', 'Costs'},
                'Unexpected custom puzzle fields')
        require(fields['PreviewEffect'] == [piece['effect_name']] and int(fields['AutoTileBase'][0], 0) == auto_tile_base(piece) and
                int(fields['PlaceQueryID'][0], 0) == tile, 'Wrong piece asset or preview-effect reference')
        check_emitted_runtime_addresses(fields, piece)
        placement = fields['Piece'][0].split(',')
        require(len(placement) == 5 and all(float(n) == 0 for n in placement[:4]) and
                int(placement[4], 0) == preview, 'Wrong placement preview')
        require(compact(fields['ReplacementIntersection'][0]) == '0,0', 'Unexpected intersection replacement')
        if piece['recipe'] == 'hsr_diagonal_ghsr':
            cells, cons = ['.....', '..ys.<', '.rz..', '..^..'], ['...', '.+.<', '.+.', '.^.']
            checks = {'r-monorail:0x00010000,0x00ff0000optional', 's-monorail:0x00000001,0x000000ffoptional',
                      'y-monorail:0x02010200', 'z-monorail:0x02000201'}
            expected_cost = 150
        elif piece['recipe'] == 'tram_under_hsr':
            cells, cons = ['.........', '...bzc...<', '....^....'], ['.........', '....+...<', '....^....']
            checks = {'b-monorail:0x00020000,0x00000000optional', 'c-monorail:0x00000002,0x00000000optional',
                      'z-lightrail:0x02000200monorail:0x00020002'}
            expected_cost = 8
        elif piece['recipe'] == 'hsr_straight_ghsr':
            cells, cons = ['.........', '...bzc..<', '....^....'], ['.........', '....+...<', '....^....']
            checks = {'b-monorail:0x00020000,0x00ff0000optional', 'c-monorail:0x00000002,0x000000ffoptional',
                      'z-monorail:0x02020202'}
            expected_cost = 100
        elif piece['recipe'] == 'diagonal_hsr_straight_ghsr':
            cells, cons = ['.r.', '.y.<', '.z.', '.s.', '.^.'], ['...', '.+.<', '.+.', '.^.']
            checks = {'r-monorail:0x02000000,0xff000000optional', 's-monorail:0x00000200,0x0000ff00optional',
                      'y-monorail:0x02010200', 'z-monorail:0x02000201'}
            expected_cost = 150
        elif piece['recipe'] == 'diagonal_hsr_diagonal_ghsr':
            cells, cons = ['.....', '.ry..<', '..zs.', '..^..'], ['...', '.+.<', '.+.', '.^.']
            checks = {'r-monorail:0x00030000,0x00ff0000optional', 's-monorail:0x00000003,0x000000ffoptional',
                      'y-monorail:0x02010003', 'z-monorail:0x00030201'}
            expected_cost = 150
        elif piece['recipe'].startswith('hsr_component_'):
            from scp_hsr.hsr_components_verify import check_construction_fields
            check_construction_fields(fields, piece, resources)
            independently_verified_construction = True
        elif piece['recipe'] == 'directional_hsr_t_smooth_diagonal_at_grade':
            from scp_hsr.directional_diagonal_t_verify import check_construction_fields
            check_construction_fields(fields, piece, resources)
            independently_verified_construction = True
        elif piece['recipe'].startswith('directional_'):
            from scp_hsr.directional_t_verify import check_construction_fields
            check_construction_fields(fields, piece, resources)
            independently_verified_construction = True
        elif piece['recipe'].startswith('interchange_'):
            from scp_hsr.interchange_verify import check_construction_fields
            check_construction_fields(fields, piece, resources)
            independently_verified_construction = True
        elif piece['recipe'].startswith('rail_') and piece['recipe'].endswith('_revised'):
            from scp_hsr.rail_repair_verify import check_construction_fields
            check_construction_fields(fields, piece, resources)
            independently_verified_construction = True
        elif piece['recipe'].startswith('rail_'):
            from scp_hsr.rail_feature_verify import construction_expectations
            cells, cons, checks, expected_cost = construction_expectations(piece)
        else:
            raise ValueError('Recipe requires an independent construction verifier')
        if not independently_verified_construction:
            require(list(map(compact, fields['CellLayout'])) == cells and
                    list(map(compact, fields['ConsLayout'])) == cons and
                    set(map(compact, fields['CheckType'])) == checks, 'Construction topology differs from native audited donor')
            require(fields['Costs'] == [str(expected_cost)], 'Unexpected piece construction cost')
        for n in range(1, 8):
            items = rules[root + n * 0x10000]
            values = dict(items)
            require(len(values) == len(items), 'Duplicate clone property')
            if piece['recipe'] in {'hsr_diagonal_ghsr', 'diagonal_hsr_straight_ghsr', 'diagonal_hsr_diagonal_ghsr'}:
                expected = {'CopyFrom': root if n <= 4 else root + 0x40000}
                expected['Transpose' if n == 4 else 'Rotate'] = 1 if n == 4 else (n if n < 4 else n - 4)
            else:
                expected = {'CopyFrom': root if n < 4 else root + (n - 4) * 0x10000}
                if n < 4:
                    expected['Rotate'] = n
            require(set(values) == set(expected) and all(int(values[k], 0) == v for k, v in expected.items()),
                    'Wrong custom clone rotation or reflection')
    ini = overlay['network_ini']
    insertion = ini['insertion'].encode('latin1')
    require(insertion and resources[NETWORK_INI].count(insertion) == 1, 'Nonunique custom INI insertion')
    restored_ini = resources[NETWORK_INI].replace(insertion, b'', 1)
    require(sha(restored_ini) == ini['base_sha256'], 'Original NetworkINI bytes changed or were removed')
    if donors:
        require(restored_ini == donors[NETWORK_INI], 'Restored NetworkINI differs from native controller')
    expected = {(number(s['tile']), 0xFFFFFFF0, number(s['source']), 15, s['rotation'], 0)
                for piece in pieces for s in piece['shadow_mappings']}
    required = set()
    for piece in pieces:
        for index, tile in enumerate(map(number, piece['tile_ids'])):
            if piece['recipe'].startswith(('rail_', 'interchange_', 'directional_', 'hsr_component_')):
                source, rotation = tile, 0
            elif piece['recipe'].startswith('diagonal_hsr_'):
                source, rotation = 0x5DD01A00, index * 2
            else:
                source, rotation = 0x5DD31500, 0 if piece['recipe'] == 'hsr_diagonal_ghsr' else 1
            required.add((tile, 0xFFFFFFF0, source, 15, rotation, 0))
    require(expected == required, 'Shadow sources or orientation do not match the elevated deck geometry')
    actual = []
    for raw in insertion.decode('ascii').splitlines():
        line = raw.split(';', 1)[0].strip()
        if line:
            require('=' in line, 'Invalid shadow insertion')
            actual.append(tuple(int(n.strip(), 0) for n in line.split('=', 1)[1].split(',')))
    require(len(actual) == len(expected) and set(actual) == expected, 'Missing, extra, or wrong custom shadow mapping')
    prefix = resources[NETWORK_INI].split(insertion)[0].decode('latin1')
    require(re.findall(r'^\[([^]]+)\]', prefix, re.M)[-1].lower() == 'shadow remapping',
            'Custom shadow entries are outside their active INI section')
    return {'original_rul0_restored': True, 'original_network_ini_restored': True,
            'separate_piece_menu_roots': len(rings), 'states_per_root': 8,
            'runtime_tile_addresses_checked': sum(len(piece['tile_ids']) for piece in pieces),
            **ordering_report}


def _tgi(value):
    require(isinstance(value, str) and re.fullmatch(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{8}-[0-9a-fA-F]{8}', value),
            'Invalid dependency TGI')
    return tuple(int(n, 16) for n in value.split('-'))


def load_local_donors(output, manifest):
    audit_path = output / 'input-audit.json'
    if not audit_path.exists():
        return {}, {'local_donor_comparison': False}
    require(not audit_path.is_symlink(), 'Local donor audit must not be a symlink')
    audit = json.loads(audit_path.read_text())
    profile = {item['filename']: item['sha256'] for item in manifest['profile']['donors']}
    require(len(profile) == len(manifest['profile']['donors']) and
            len({item['filename'] for item in audit['donors']}) == len(audit['donors']),
            'Duplicate donor filename in profile or local audit')
    require(set(profile) == {item['filename'] for item in audit['donors']},
            'Local donor audit does not match the declared profile files')
    donors = {}
    for entry in audit['donors']:
        path = Path(entry['path'])
        require(path.is_file() and not path.is_symlink(), 'Local NAM donor is missing or symlinked')
        require(path.name == entry['filename'] and entry['sha256'] == profile[path.name],
                'Local donor audit differs from the declared compatibility profile')
        raw = path.read_bytes()
        require(sha(raw) == entry['sha256'], f'Local NAM donor changed: {path.name}')
        for key, value in entries(raw).items():
            if key[0] == 0xE86B1EEF:
                continue
            value = decompress(value)
            require(key not in donors or donors[key] == value, 'Conflicting local donor resources')
            donors[key] = value
    require(RUL0 in donors and NETWORK_INI in donors, 'Local donor audit has no native controller')
    return donors, {'local_donor_comparison': True, 'unchanged_donor_files': len(audit['donors'])}


def verify_build(output, write_report=True):
    output = Path(output)
    require(output.is_dir() and not output.is_symlink(), 'Build output must be a real directory')
    output = output.resolve()
    require(not any(path.is_symlink() for path in output.rglob('*')), 'Build output contains a symlink')
    manifest = json.loads((output / 'manifest.json').read_text())
    if 'menu_experiment' in manifest:
        from .menu_experiment import verify_menu_experiment
        return verify_menu_experiment(output, write_report=write_report)
    require(manifest.get('schema_version') == 1, 'Unsupported build manifest schema')
    require(manifest.get('plugin_folder') == 'zzz_Simons_Custom_Pieces', 'Wrong managed plugin folder')
    pieces = manifest['pieces']
    validate_catalog({'schema_version': 1, 'plugin_folder': manifest['plugin_folder'], 'pieces': pieces,
                      '_profile': {'schema_version': 1}})
    file_records = manifest['files']
    require(file_records and len({item['path'] for item in file_records}) == len(file_records), 'Duplicate or missing package files')
    expected_paths = {item['path'] for item in file_records}
    require(all(name.startswith(manifest['plugin_folder'] + '/') for name in expected_paths), 'Package payload outside managed folder')
    folder = manifest['plugin_folder']
    expected_payload = {f'{folder}/00_SCP_Controller_NAM50.dat', f'{folder}/10_SCP_Menu.dat'}
    for piece in pieces:
        asset_path = f"{folder}/20_Pieces/SCP_{piece['id']}.dat"
        require(piece['asset_file'] == asset_path, 'Piece assets must use their own managed DAT path')
        expected_payload.add(asset_path)
    require(expected_paths == expected_payload, 'Unexpected, missing, or non-DAT package payload')
    documentation = manifest.get('documentation', [])
    doc_paths = {item['path'] for item in documentation}
    require(len(doc_paths) == len(documentation) and not (doc_paths & expected_paths),
            'Repeated or overlapping documentation paths')
    require(all(name == 'README.txt' or name.startswith('docs/') for name in doc_paths),
            'Unexpected documentation location')
    metadata = {'manifest.json', 'input-audit.json', 'verification.json'}
    actual_paths = {p.relative_to(output).as_posix() for p in output.rglob('*') if p.is_file()}
    require(actual_paths - metadata == expected_paths | doc_paths and
            expected_paths | doc_paths <= actual_paths, 'Output file closure mismatch')
    for item in documentation:
        raw = safe_file(output, item['path']).read_bytes()
        require(len(raw) == item['bytes'] and sha(raw) == item['sha256'], 'Documentation hash/size mismatch')
    resources, owners, by_file = {}, {}, {}
    for item in file_records:
        path = safe_file(output, item['path'])
        raw = path.read_bytes()
        require(len(raw) == item['bytes'] and sha(raw) == item['sha256'], f'Package file hash/size mismatch: {item["path"]}')
        if path.suffix.lower() == '.dat':
            parsed = strict_dbpf(raw)
            require(not (set(resources) & set(parsed)), 'A resource TGI appears in more than one package DAT')
            resources.update(parsed); owners.update({key: item['path'] for key in parsed}); by_file[item['path']] = parsed
    donors, donor_report = load_local_donors(output, manifest)
    construction = check_construction(resources, pieces, manifest, donors)
    base_menu = donors.get((*MENU_EXEMPLAR, 0x6A47C200), menu_baseline())
    expected_resources = {RUL0, NETWORK_INI}
    model_textures, piece_reports = set(), []
    for piece in pieces:
        tiles, preview = list(map(number, piece['tile_ids'])), number(piece['preview_id'])
        shadow_report = {'artwork': 'native NAM shadow remapping', 'in_game_shadow_selection_tested': False}
        asset_keys = {(*S3D, preview)}
        for tile in tiles:
            asset_keys.update({(*S3D, tile + zoom) for zoom in range(5)})
            asset_keys.update({(*PATH, tile), (*EXEMPLAR, tile), (*LTEXT, tile)})
            require(piece['name'] in read_ltext(resources[*LTEXT, tile]), 'Piece query description mismatch')
        if piece['recipe'].startswith(('rail_', 'interchange_', 'directional_', 'hsr_component_')):
            asset_keys.update({(*SHADOW, tile + zoom) for tile in tiles for zoom in range(5)})
            from .shadows import validate_piece_shadows
            shadow_report = validate_piece_shadows({key: resources[key] for key in asset_keys}, piece)
        effect_keys = {key for key in resources if key[:2] == EFFECT and key[2] in {tiles[0], preview}}
        require(len(effect_keys) == 1, 'Missing or repeated per-piece preview effect')
        asset_keys.update(effect_keys)
        require(piece['asset_file'] in by_file and set(by_file[piece['asset_file']]) == asset_keys,
                'Piece asset DAT contains missing, unexpected, or another piece resources')
        expected_resources.update(asset_keys)
        menu_id = number(piece['menu']['id'])
        expected_resources.update({(*prefix, menu_id) for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)})
        menu_report = validate_menu_resources(resources, base_menu, piece)
        try:
            paths_report = check_piece_paths(resources, piece)
            models_report = check_piece_models(resources, piece, donors)
        except ValueError as error:
            raise ValueError(f'{piece["id"]}: {error}') from error
        model_textures.update(models_report.pop('texture_ids'))
        effect = resources[next(iter(effect_keys))]
        effect_name = piece['effect_name'].encode('ascii')
        require(effect.count(effect_name) == 4 and effect.count(struct.pack('<I', preview)) == 2,
                'Preview effect name/model references do not match the piece')
        if donors:
            from scp_hsr.crossings import INFO as CROSSINGS
            if piece['recipe'] in CROSSINGS:
                info = CROSSINGS[piece['recipe']]
                native_id, native_name, native_model = info['effect'], info['effect_name'].encode('ascii'), info['effect']
            elif piece['recipe'].startswith('hsr_component_'):
                from scp_hsr.hsr_components import INFO as COMPONENTS
                key, name, native_model = COMPONENTS[piece['recipe']]['effect_donor']
                native_id, native_name = key[2], name.encode('ascii')
            elif piece['recipe'] == 'directional_hsr_t_smooth_diagonal_at_grade':
                from scp_hsr.directional_diagonal_t import INFO as DIAGONAL
                key, name, native_model = DIAGONAL[piece['recipe']]['effect_donor']
                native_id, native_name = key[2], name.encode('ascii')
            elif piece['recipe'].startswith('directional_'):
                from scp_hsr.directional_t import INFO as DIRECTIONAL
                key, name, native_model = DIRECTIONAL[piece['recipe']]['effect_donor']
                native_id, native_name = key[2], name.encode('ascii')
            elif piece['recipe'].startswith('interchange_'):
                from scp_hsr.interchange_layouts import INFO as INTERCHANGES
                key, name, native_model = INTERCHANGES[piece['recipe']]['effect_donor']
                native_id, native_name = key[2], name.encode('ascii')
            elif piece['recipe'].startswith('rail_') and piece['recipe'].endswith('_revised'):
                from scp_hsr.rail_repairs import INFO as RAIL_REPAIRS
                key, name, native_model = RAIL_REPAIRS[piece['recipe']]['effect_donor']
                native_id, native_name = key[2], name.encode('ascii')
            elif piece['recipe'].startswith('rail_'):
                from scp_hsr.rail_features import INFO as RAIL_FEATURES
                key, name, native_model = RAIL_FEATURES[piece['recipe']]['effect_donor']
                native_id, native_name = key[2], name.encode('ascii')
            else:
                native_id = 0x59F3D115 if piece['recipe'] == 'hsr_diagonal_ghsr' else 0x580E0700
                native_name = (b'preview_hsrp_subrail____001' if piece['recipe'] == 'hsr_diagonal_ghsr'
                               else b'preview_rail_dualnetwork029')
                native_model = native_id if piece['recipe'] == 'hsr_diagonal_ghsr' else native_id + 5
            require(effect.replace(effect_name, native_name).replace(struct.pack('<I', preview),
                    struct.pack('<I', native_model)) == donors[*EFFECT, native_id], 'Preview effect differs from native clone')
        piece_reports.append({'id': piece['id'], 'menu': menu_report, 'paths': paths_report,
                              'models': models_report, 'shadows': shadow_report})
    require(set(resources) == expected_resources, 'Unexpected or missing package resource')
    require(owners[RUL0] == owners[NETWORK_INI] and set(by_file[owners[RUL0]]) == {RUL0, NETWORK_INI},
            'Shared controller DAT must contain exactly one RUL0 and NetworkINI overlay')
    menu_keys = {(*prefix, number(piece['menu']['id'])) for piece in pieces
                 for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)}
    require(set(by_file[f'{folder}/10_SCP_Menu.dat']) == menu_keys and
            owners[RUL0] == f'{folder}/00_SCP_Controller_NAM50.dat',
            'Shared controller and menu resources are not separated into their own DATs')
    deps = manifest['dependency_audit']
    textures, shadows = {_tgi(v) for v in deps['textures']}, {_tgi(v) for v in deps['shadows']}
    require(all(key[:2] == (0x7AB50E44, 0x1ABE787D) for key in textures) and
            {key[2] for key in textures} == model_textures,
            'Declared texture dependencies do not exactly cover model material references')
    expected_shadows = {(*SHADOW, number(s['source']) + zoom) for piece in pieces
                        for s in piece['shadow_mappings'] for zoom in range(5)
                        if (*SHADOW, number(s['source']) + zoom) not in resources}
    require(shadows == expected_shadows, 'Declared shadow dependencies do not cover actual mappings')
    report = {'schema_version': 1, 'static_checks_passed': True, 'files_checked': len(file_records),
              'documentation_files_checked': len(documentation),
              'resources_checked': len(resources), 'construction': construction, 'pieces': piece_reports,
              'dependency_records_cover_all_references': True, 'external_textures': len(textures),
              'external_shadows': len(shadows), **donor_report,
              'in_game_placement_tested': False, 'in_game_menu_tested': False, 'in_game_rendering_tested': False,
              'in_game_traffic_tested': False, 'in_game_shadow_selection_tested': False,
              'in_game_bulldozing_tested': False, 'in_game_save_reload_tested': False,
              'verification_limit': 'Static archive and content audit. External NAM dependencies are declared; this does not execute SimCity 4.'}
    if write_report:
        (output / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    return report
