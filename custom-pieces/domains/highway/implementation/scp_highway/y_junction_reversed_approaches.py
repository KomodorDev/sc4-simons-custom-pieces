"""Exact reversed Y helper identities, marker flags, and propagation phases."""
from copy import deepcopy
import re

from scp.dbpf import require
from . import y_junction_approaches as shared

OPT_IN = shared.OPT_IN
SECTION = shared.SECTION
NATIVE_DEPENDENCY_SHA256 = shared.NATIVE_DEPENDENCY_SHA256
NATIVE_CONTROLLER_SHA256 = shared.NATIVE_CONTROLLER_SHA256

OWNERS = {
    'ddrhw-y-reversed-diagonal-stem-split': ('highway_ddrhw_y_reversed_diagonal_stem_split',
        (-2, 2), (-1, 2), 0, 0x57530200, 0, 3, (0, 1), 0x57530900, 2),
    'ddrhw-y-reversed-diagonal-branch': ('highway_ddrhw_y_reversed_diagonal_branch',
        (-2, -2), (-1, -2), 0, 0x57530200, 3, 1, (0, -1), 0x57530900, 1),
    'ddrhw-y-reversed-orthogonal-core': ('highway_ddrhw_y_reversed_orthogonal_core',
        (4, 0), (3, 0), 2, 0x57530000, 1, 2, (1, 0), 0x57530000, 1),
}


def _reviewed(piece):
    require(piece.get('y_junction_variant') == 'reversed' and piece.get('domain') == 'highway'
            and piece.get('id') in OWNERS and piece.get('recipe') == OWNERS[piece['id']][0],
            'Unreviewed reversed Y native approach owner')
    from .y_junction_reversed_layout import module_catalog
    records = module_catalog()['types']
    matches = [row for row in records if row['id'] == piece['id']]
    require(len(matches) == 1, 'Reversed Y native owner lacks a unique physical declaration')
    row = matches[0]
    require(piece.get('cells') == row['cells'] and piece.get('footprint') == row['footprint'],
            'Reversed Y native owner changes its declared physical cells')
    tiles = piece.get('tile_ids')
    require(isinstance(tiles, list) and len(tiles) == len(row['cells'])
            and all(isinstance(value, str) and re.fullmatch('[0-9a-fA-F]{8}', value) for value in tiles)
            and len({value.lower() for value in tiles}) == len(tiles),
            'Reversed Y native owner has invalid canonical addresses')
    require(not any(piece.get(name) for name in ('native_dd_approaches', 'native_ghsr_approaches',
            'native_orthogonal_approaches', 'adaptive_ground')),
            'Reversed Y native helpers cannot mix approach modes')
    return row


def approaches(piece):
    if shared.OPT_IN not in piece:
        return []
    require(type(piece[shared.OPT_IN]) is bool, shared.OPT_IN+' must be an exact boolean')
    if not piece[shared.OPT_IN]:
        return []
    record = _reviewed(piece)
    _recipe, outside, end, edge, target, pose, *_ = OWNERS[piece['id']]
    origin = record['world_origin_cell']
    outside, end = ([point[i]-origin[i] for i in range(2)] for point in (outside, end))
    require(outside not in piece['cells'] and end in piece['cells'],
            'Reversed Y helper becomes owned, or its actual joining cell is absent')
    # 302's native marker direction is opposite 309's. Retaining 01000400
    # here would collide with the installed original Y at the same road key.
    marker = 0x04000100 if target == 0x57530200 else 0x01000400
    road = 0x03010000 if target == 0x57530200 else 0x02000200
    return [{'cell': outside, 'end_cell': end,
             'end_tile_id': piece['tile_ids'][piece['cells'].index(end)].lower(),
             'outward_edge': edge, 'native_tile_id': f'{target:08x}', 'native_rotation': pose,
             'section': shared.SECTION,
             'networks': [{'name': 'monorail', 'flags': f'{shared._rotate_flags(marker, pose):08x}'},
                          {'name': 'dirtroad', 'flags': f'{shared._rotate_flags(road, pose):08x}'}],
             'native_exemplar_group': '6be08658', 'native_model_reference': 'rkt0',
             'optional': True, 'experimental': True}]


def rul1_sections(piece):
    rows = approaches(piece)
    if not rows:
        return {}
    target = int(rows[0]['native_tile_id'], 16)
    marker = 0x04000100 if target == 0x57530200 else 0x01000400
    road = 0x03010000 if target == 0x57530200 else 0x02000200
    return {shared.SECTION: tuple((shared._rotate_flags(marker, turn), shared._rotate_flags(road, turn),
                                  target, turn, 0) for turn in range(4))}


def check_native_continuation(controller):
    result = deepcopy(shared.check_native_continuation(controller))
    from scp.native_approaches import _section_span, _solution_rows
    start, end = _section_span(controller[shared.RUL1], shared.SECTION)
    actual = _solution_rows(controller[shared.RUL1][start:end])
    for turn in range(4):
        pair = shared._rotate_flags(0x04000100, turn), shared._rotate_flags(0x03010000, turn)
        require(not any(row[:2] == pair for row in actual),
                'Reversed Y diagonal markers collide with pinned original NAM RUL1')
    result.update(reversed_diagonal_marker_pairs_absent_from_native=4,
                  reversed_helper_target='57530200', original_helper_target='57530900')
    return result


def oriented_propagation(piece):
    """Check exact original RUL2 templates in both construction directions."""
    _recipe, _outside, _end, _edge, target, pose, _outer, step, next_target, next_pose = OWNERS[piece['id']]
    if target == 0x57530200:
        index = 0 if pose == 0 else 1
        cases = [('outward', index, 0), ('inward', index+2, 2)]
    else:
        cases = [('outward', 4, 0), ('outward', 5, 0), ('inward', 6, 2), ('inward', 7, 2)]
    templates, result = shared._continuation_templates(), []
    seeds = rul1_sections(piece)[shared.SECTION]
    for turns in range(4):
        for order, index, alignment in cases:
            source, output = [part.split(',') for part in templates[index].split('=')]
            source = [int(value, 16) if i % 3 == 0 else int(value) for i, value in enumerate(source)]
            output = [int(value, 16) if i % 3 == 0 else int(value) for i, value in enumerate(output)]
            for values in (source, output):
                for i in (1, 4):
                    values[i] = (values[i]+alignment+turns) % 4
            first = (target, (pose+turns) % 4) if order == 'outward' else (next_target, (next_pose+turns) % 4)
            last = (next_target, (next_pose+turns) % 4) if order == 'outward' else (target, (pose+turns) % 4)
            require(tuple(source[:2]) == first and tuple(output[:2]) == first
                    and tuple(output[3:5]) == last and source[2] == source[5] == output[2] == output[5] == 0,
                    'Reversed Y continuation does not follow an unchanged original propagation template')
            require(seeds[(pose+turns) % 4][2:] == (target, (pose+turns) % 4, 0),
                    'Reversed Y marker selects the wrong original native propagation pose')
            vector = shared._point((step[0], -step[1], 0), turns)
            result.append({'piece_rotation': turns, 'construction_order': order,
                'original_native_template': templates[index],
                'template_clockwise_quarter_turns': (alignment+turns) % 4,
                'seeded_helper_tile': f'{target:08x}', 'seeded_helper_pose': (pose+turns) % 4,
                'further_native_tile': f'{next_target:08x}', 'further_native_pose': (next_pose+turns) % 4,
                'further_native_step_en': list(vector[:2]), 'basic_rhw_tile': f'{source[3]:08x}',
                'basic_rhw_pose': source[4]})
    return result


# Shared construction and saved-PATH readers dispatch through the exact
# explicit variant. Keeping them in one engine avoids divergent grid logic.
add_approaches = shared.add_approaches
check_construction_approaches = shared.check_construction_approaches
check_native_boundary_paths = shared.check_native_boundary_paths
dependency_sha256 = shared.dependency_sha256
additional_dependency_keys = shared.additional_dependency_keys
dependency_model_references = shared.dependency_model_references
existing_rul1_sections = shared.existing_rul1_sections
