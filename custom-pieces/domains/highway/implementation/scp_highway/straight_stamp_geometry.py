"""Partition the accepted indexed faces into a straight stamp and full ramps.

Construction and PATH ownership follow whole city tiles. A separately placed
ramp may draw its exact retained high throat over highway-owned tiles; only
its model crosses that ownership boundary. Native deck faces, inside-corridor
slip-lane paint, and centre piers remain with the straight highway stamp.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import hashlib
import math
import re
import struct

from scp.models import pack_s3d, parse_s3d, validate_s3d
from scp.recipes import combine_meshes

WING_CELLS = {
    'lower-off': ((2, -3),),
    'lower-on': ((-3, 2),),
    'upper-off': ((-2, 4), (-3, 5)),
    'upper-on': ((4, -2), (5, -3)),
}
CENTRE_PIER_CELLS = frozenset(((-1, 1), (-1, 2), (1, -1), (2, -1), (-4, 4), (4, -4)))
NATIVE_HALF_WIDTH_M = 8.0
ENCODING_TOLERANCE_M = 2.0 ** -18
_AUTHORED_MESH = re.compile(
    rb'(?:SCP moved -?\d+,-?\d+ )?SCP NAM (?:highway|ramp|concrete|barrier)\x00'
    rb'|SCP highway road\x00')


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def matches_frozen_model(raw, expected_sha256):
    """Match frozen bytes, permitting only the authored VERT-word repair.

    Frozen records retain their historical SHA-256. The corrected runtime
    word 0x80004001 has the same XYZ/one-UV bytes as historical format 2.
    Reconstruct only those four-byte words in exclusively authored buffers;
    every other byte, including native-buffer descriptors, must still hash
    to the original record. The live model is never changed or repacked.
    """
    if hashlib.sha256(raw).hexdigest() == expected_sha256:
        return True
    try:
        model = parse_s3d(raw)
        validate_s3d(model)
    except (ValueError, struct.error):
        return False
    owners = defaultdict(list)
    for mesh in model['meshes']:
        for vi, _ii, _pi, _mi in mesh['frames']:
            owners[vi].append(mesh['name'])
    # parse_s3d has already validated the ordered HEAD and VERT chunks.
    vert = 8 + struct.unpack_from('<I', raw, 12)[0]
    offset = vert + 12
    restored = bytearray(raw)
    changed = False
    for vi, block in enumerate(model['vertices']):
        if (block['format'] == 0x80004001 and block['stride'] == 20
                and block['flags'] == 0 and owners[vi]
                and all(_AUTHORED_MESH.fullmatch(name) for name in owners[vi])):
            struct.pack_into('<I', restored, offset + 4, 2)
            changed = True
        offset += 8 + len(block['data'])
    return changed and hashlib.sha256(restored).hexdigest() == expected_sha256


def stamp_cells():
    from .modular_stamp import reference
    wings = {cell for cells in WING_CELLS.values() for cell in cells}
    cells = {tuple(row['source_world_cell']) for row in reference()['cells']} - wings
    _require(len(cells) == 21 and all(sum(c) in (0, 1) or c in ((0, -1), (-1, 0)) for c in cells),
             'The straight stamp must own only its 19 native DD and 2 pure Avenue cells')
    return frozenset(cells)


def _triangle_role(name, points, cell):
    """Classify complete saved faces, including the piers inside shared meshes."""
    if not name.startswith(b'SCP NAM '):
        return 'stamp'
    if name.rstrip(b'\0') == b'SCP NAM highway':
        # This role is the explicit white slip-lane paint, not the MIS ramp
        # pavement. Its strokes were already clipped at the native edge.
        lateral = [(-p[2] - 16 * cell[1] - p[0] - 16 * cell[0] + 8) / math.sqrt(2)
                   for p in points]
        _require(max(map(abs, lateral)) <= 8.00001 and
                 any(all(abs(p[1] - height) < 1e-5 for p in points) for height in (7.51, 15.01)),
                 'A retained slip-lane paint face leaves the straight native corridor')
        return 'stamp'
    if (cell in CENTRE_PIER_CELLS and name.rstrip(b'\0') == b'SCP NAM concrete'
            and all(abs(p[0]) <= .40001 and abs(p[2]) <= .40001 for p in points)
            and min(p[1] for p in points) < 1e-5 and max(p[1] for p in points) >= 14.99999):
        return 'stamp'
    _require(name.rstrip(b'\0') in (b'SCP NAM ramp', b'SCP NAM concrete', b'SCP NAM barrier'),
             f'Unexpected authored face role in straight partition: {name!r}')
    heights = [p[1] for p in points]
    if max(heights) < 10:
        _require(min(heights) >= 5.0, 'A non-pier ground face entered the retained high ramp partition')
        deck = 'lower'
    else:
        _require(min(heights) >= 10, 'A face straddles both highway decks')
        deck = 'upper'
    u = sum(p[0] + 16 * cell[0] - p[2] - 16 * cell[1] for p in points) / (3 * math.sqrt(2))
    _require(abs(u) > 1, 'A retained high throat cannot straddle the Avenue crossing')
    direction = 'off' if (u > 0) == (deck == 'lower') else 'on'
    return deck + '-' + direction


def split_model(raw, cell):
    """Return role-model subsets without changing any selected XYZ/UV bytes."""
    source = parse_s3d(raw)
    groups = defaultdict(list)
    for mesh in source['meshes']:
        _require(len(mesh['frames']) == 1, 'Straight partition supports static source meshes only')
        vi, ii, pi, mi = mesh['frames'][0]
        vertices = source['vertices'][vi]
        _require(vertices['stride'] == 20, 'Straight partition requires actual XYZ/UV source vertices')
        points = [struct.unpack_from('<5f', vertices['data'], n)
                  for n in range(0, len(vertices['data']), 20)]
        indices = source['indices'][ii]['values']
        selections = defaultdict(list)
        for kind, first, count in source['primitives'][pi]:
            _require(kind == 0 and count % 3 == 0, 'Straight partition needs indexed triangle-list primitives')
            for n in range(first, first + count, 3):
                triangle = indices[n:n + 3]
                role = _triangle_role(mesh['name'], [points[i] for i in triangle], cell)
                selections[role].extend(triangle)
        for role, selected in selections.items():
            groups[role].append((mesh, vertices, source['indices'][ii], source['materials'][mi], selected))
    result = {}
    for role, selections in groups.items():
        output = {key: deepcopy(source[key]) for key in ('version', 'anim_header', 'trailing')}
        output.update({key: [] for key in ('vertices', 'indices', 'primitives', 'materials', 'meshes')})
        for mesh, vertices, indices, material, selected in selections:
            n = len(output['meshes'])
            # Copy referenced source vertex bytes verbatim, removing unused
            # curved vertices from the straight stamp's actual model bounds.
            lookup, ordered, remapped = {}, [], []
            for index in selected:
                if index not in lookup:
                    lookup[index] = len(ordered)
                    ordered.append(index)
                remapped.append(lookup[index])
            vertex_buffer = deepcopy(vertices)
            vertex_buffer['data'] = b''.join(vertices['data'][20 * index:20 * (index + 1)] for index in ordered)
            output['vertices'].append(vertex_buffer)
            index_buffer = deepcopy(indices)
            index_buffer['values'] = tuple(remapped)
            output['indices'].append(index_buffer)
            output['primitives'].append([(0, 0, len(selected))])
            output['materials'].append(deepcopy(material))
            name = mesh['name']
            if role != 'stamp':
                name = f'SCP moved {cell[0]},{cell[1]} '.encode('ascii') + name.rstrip(b'\0') + b'\0'
            output['meshes'].append({'name': name, 'flags': mesh['flags'], 'frames': [(n, n, n, n)]})
        validate_s3d(output)
        result[role] = output
    return result


def _closest(cell, candidates):
    return min(candidates, key=lambda c: ((c[0] - cell[0]) ** 2 + (c[1] - cell[1]) ** 2, c[1], c[0]))


def partition_source_cells(source_cells):
    """Split a complete 27-cell checkpoint for direct saved-source review."""
    kept, moved = defaultdict(list), {name: defaultdict(list) for name in WING_CELLS}
    retained = stamp_cells()
    wing_paths, source_counts = {}, {}
    _require(len(source_cells) == 27, 'The straight partition requires the complete accepted 27-cell source')
    for cell, (raw, path) in source_cells.items():
        roles = split_model(raw, cell)
        source_counts[cell] = {role: sum(sum(p[2] for p in model['primitives'][mesh['frames'][0][2]]) // 3
                                       for mesh in model['meshes']) for role, model in roles.items()}
        for role, model in roles.items():
            host = cell if cell in retained else _closest(cell, retained)
            collection = kept
            if role != 'stamp':
                host = cell if cell in WING_CELLS[role] else _closest(cell, WING_CELLS[role])
                collection = moved[role]
            offset = (16.0 * (cell[0] - host[0]), 0.0, 16.0 * (cell[1] - host[1]))
            collection[host].append((model, model['meshes'], offset))
        if cell not in retained:
            wing_paths[cell] = path
    def packed(parts):
        return {cell: pack_s3d(combine_meshes(models)) for cell, models in parts.items()}
    return {'stamp_models': packed(kept), 'ramp_models': {name: packed(parts) for name, parts in moved.items()},
            'wing_paths': wing_paths, 'source_triangle_counts': source_counts}


def _source_mismatch(record, resource, expected, actual):
    return ValueError(
        f"The accepted source changed before straight-stamp face partition. "
        f"{record['source_piece_id']} {resource} at source cell "
        f"{tuple(record['source_local_cell'])}, world cell {tuple(record['source_world_cell'])}. "
        f"Expected SHA-256 {expected}, actual SHA-256 {actual}."
    )


def source_cells(context):
    """Reproduce and fingerprint the accepted 27-cell source using pinned inputs."""
    from scp import jsonc
    from .modular_stamp import ROOT, reference
    from .ramp_paths import compile_module as compile_source
    from .native import build_crossing_channels
    cached = context.get('_straight_stamp_source_cells')
    if cached is not None:
        return cached
    compiled = {}
    pristine = None
    result = {}
    for record in reference()['cells']:
        identifier = record['source_piece_id']
        if identifier not in compiled:
            spec = jsonc.load(ROOT / 'domains/highway/00_pieces' / identifier / 'piece.jsonc')
            compiled[identifier] = {tuple(cell): (model, path) for cell, model, path in compile_source(spec, context)}
        local_cell = tuple(record['source_local_cell'])
        model, path = compiled[identifier][local_cell]
        if 'inherited_model_sha256' in record:
            expected = record['inherited_model_sha256']
            if not matches_frozen_model(model, expected):
                raise _source_mismatch(record, 'inherited Avenue apron model', expected,
                                       hashlib.sha256(model).hexdigest())
            if pristine is None:
                pristine = {tuple(cell): model for cell, model, _ in build_crossing_channels(context)}
            model = pristine[local_cell]
        expected = record['model_sha256']
        if not matches_frozen_model(model, expected):
            raise _source_mismatch(record, 'model', expected, hashlib.sha256(model).hexdigest())
        expected = record['path_sha256']
        actual = hashlib.sha256(path).hexdigest()
        if actual != expected:
            raise _source_mismatch(record, 'traffic PATH', expected, actual)
        result[tuple(record['source_world_cell'])] = model, path
    context['_straight_stamp_source_cells'] = result
    return result


def partition(context):
    if '_straight_stamp_partition' not in context:
        context['_straight_stamp_partition'] = partition_source_cells(source_cells(context))
    return context['_straight_stamp_partition']
