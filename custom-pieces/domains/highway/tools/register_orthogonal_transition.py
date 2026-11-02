#!/usr/bin/env python3
"""Register the six-tile coupled DD-to-ground adapter with new local identities."""
from __future__ import annotations

from copy import deepcopy
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation'),
                str(Path(__file__).parent)]

from scp.catalog import load_catalog
from scp.registration import apply_registration
from scp.model_shadows import allocation_fields
from scp_highway.menu import make_icon
from scp_highway.orthogonal_approaches import PIECE_ID, MIRRORED_PIECE_ID, RECIPE, MIRRORED_RECIPE, CORE_CELLS, variant
from scp_highway.orthogonal_transition import engineering_metadata
from register_highway_pieces import _allocation, GAME_KEYS


def register(root=ROOT):
    root = Path(root).resolve()
    catalog = load_catalog(root)
    existing = next((piece for piece in catalog['pieces'] if piece['id'] == PIECE_ID), None)
    cells = [list(cell) for cell in CORE_CELLS]
    if existing:
        if existing['recipe'] != RECIPE or existing['cells'] != cells or existing['footprint'] != [2, 6]:
            raise ValueError('The retained transition identity has a different reviewed function or footprint')
        return {'registered': False, 'piece_id': PIECE_ID, 'reason': 'already registered; identifiers preserved'}
    ledger = deepcopy(catalog['_allocations'])
    puzzle, block, tiles = _allocation(ledger, cells)
    piece = {
        'schema_version': 1, 'id': PIECE_ID, 'domain': 'highway',
        'name': 'DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Orthogonal Combined Transition — 6 Tiles',
        'description': 'One six-tile adapter lowers both stacked highway directions while moving the upper carriageway into the neighbouring ground tile. It preserves two lanes per direction and uses native DD and ground RHW-4 approach sockets.',
        'recipe': RECIPE, 'enabled_by_default': False, 'status': 'experimental',
        'puzzle_id': f'{puzzle:04x}', 'tile_ids': tiles, 'preview_id': f'{block + 0xff5:08x}',
        'effect_name': f'preview_scp_hw_{puzzle:04x}'.ljust(24, '_') + '001',
        'footprint': [2, 6], 'cells': cells, 'orientation_count': 8,
        'dependencies': ['controller', 'dd_rhw', 'rhw_core', 'rhw4', 'rhw4_textures'],
        'native_orthogonal_approaches': True,
        'menu': {'id': f'{0x6a470000 | puzzle:08x}', 'order': f'{0xffffff00 | (puzzle & 0xff):08x}',
                 'style': 'ddrhw-transition'},
        'authored_texture_ids': tiles[:1],
        'engineering': {**engineering_metadata(), 'max_grade_percent': 20.0,
                        'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
                        'pavement_path_offset_m': 0.0},
        'shadow_mode': 'model-carrier', 'shadow_mappings': [],
        'model_shadows': {'schema_version': 1, 'sun_profile': 'sc4-default-67p5-45', 'enabled': False,
                          'cells': [{'cell': cell, 'cast_shadow': False} for cell in cells]},
        'provenance': {
            'geometry': 'Measured orthogonal native DD and RHW-4 sockets; coordinated six-tile height and width transition with flat native collars and curve-aware lane grades.',
            'construction': 'Twelve physical road-envelope owners, three unowned native starter sockets, and four proper rotations repeated across eight cursor states.',
            'granularity': 'One reusable coupled adapter. Its vertical profile depends on the lateral curve; arbitrary internal cuts do not supply standard interchangeable slope or curvature sockets.',
            'redistribution': 'permission-pending'},
        'game_tests': {name: 'unverified' for name in GAME_KEYS}}
    ledger['pieces'][PIECE_ID] = {
        'puzzle_id': piece['puzzle_id'], 'tile_ids': tiles, 'preview_id': piece['preview_id'],
        'menu_id': piece['menu']['id'], 'state': 'reserved-locally', 'cells': cells,
        'tile_base': f'{block:08x}', 'resource_blocks': [f'{block:08x}'], **allocation_fields(piece)}
    apply_registration(root, [piece], ledger, {'ddrhw-orthogonal-ground-transition': [PIECE_ID]},
                       icons={PIECE_ID: make_icon(piece['menu']['style'])}, domain='highway')
    return {'registered': True, 'piece_id': PIECE_ID, 'puzzle_id': piece['puzzle_id'],
            'footprint': piece['footprint'], 'occupied_cells': len(cells),
            'source': f'domains/highway/00_pieces/{PIECE_ID}/piece.jsonc'}


def register_mirrored(root=ROOT):
    """Reserve only the reviewed counterpart; retain every original source."""
    root = Path(root).resolve()
    catalog = load_catalog(root)
    original = next((piece for piece in catalog['pieces'] if piece['id'] == PIECE_ID), None)
    if original is None:
        raise ValueError('Register and review the original six-tile transition before its mirrored counterpart')
    if variant(original) != 'original' or original['cells'] != [list(cell) for cell in CORE_CELLS]:
        raise ValueError('Original transition has an unreviewed identity or owned footprint')
    existing = next((piece for piece in catalog['pieces'] if piece['id'] == MIRRORED_PIECE_ID), None)
    if existing is not None:
        if (variant(existing) != 'mirrored' or existing['cells'] != original['cells']
                or existing['footprint'] != [2, 6]
                or existing.get('menu', {}).get('family_anchor') != PIECE_ID):
            raise ValueError('Retained mirrored transition differs from the reviewed variant or Tab family')
        return {'registered': False, 'piece_id': MIRRORED_PIECE_ID,
                'reason': 'already registered; all identifiers and original source preserved'}
    ledger = deepcopy(catalog['_allocations'])
    cells = [list(cell) for cell in CORE_CELLS]
    puzzle, block, tiles = _allocation(ledger, cells)
    piece = {key: deepcopy(value) for key, value in original.items()
             if key not in {'purpose', 'asset_file', 'design_review'}}
    piece.update({
        'id': MIRRORED_PIECE_ID,
        'name': 'DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Mirrored Orthogonal Transition — 6 Tiles',
        'description': 'The mirrored six-tile coupled adapter has the stacked highway at its north-west end. Its lower deck travels south into the west ground carriageway, and its upper deck rises north from the east ground carriageway. Each direction retains two lanes and native DD and ground RHW-4 sockets.',
        'recipe': MIRRORED_RECIPE, 'transition_variant': 'mirrored',
        'puzzle_id': f'{puzzle:04x}', 'tile_ids': tiles,
        'preview_id': f'{block + 0xff5:08x}',
        'effect_name': f'preview_scp_hw_{puzzle:04x}'.ljust(24, '_') + '001',
        'menu': {'id': f'{0x6a470000 | puzzle:08x}',
                 'order': f'{0xffffff00 | (puzzle & 0xff):08x}',
                 'style': 'ddrhw-transition', 'family_anchor': PIECE_ID},
        'authored_texture_ids': tiles[:1],
        'engineering': {**engineering_metadata(variant='mirrored'), 'max_grade_percent': 20.0,
                        'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
                        'pavement_path_offset_m': 0.0},
        'provenance': {
            'geometry': 'Reviewed counterpart of the original six-tile adapter: reflect the complete road envelopes, supports, and lane geometry about east = 8 m, reverse directed travel, and align native DD pose 2 and native ground poses 0 and 2.',
            'construction': 'Twelve row-major owners, three unowned native sockets, and four proper rotations repeated across eight cursor states. Native RUL1 solutions are reused without insertion or a RUL2 override.',
            'granularity': original['provenance']['granularity'],
            'redistribution': 'permission-pending'},
        'game_tests': {name: 'unverified' for name in GAME_KEYS}})
    ledger['pieces'][MIRRORED_PIECE_ID] = {
        'puzzle_id': piece['puzzle_id'], 'tile_ids': tiles, 'preview_id': piece['preview_id'],
        'menu_id': piece['menu']['id'], 'state': 'reserved-locally', 'cells': cells,
        'tile_base': f'{block:08x}', 'resource_blocks': [f'{block:08x}'], **allocation_fields(piece)}
    collections = {
        'ddrhw-orthogonal-ground-transition': [PIECE_ID, MIRRORED_PIECE_ID],
        'ddrhw-orthogonal-ground-transition-original': [PIECE_ID],
        'ddrhw-orthogonal-ground-transition-mirrored': [MIRRORED_PIECE_ID]}
    apply_registration(root, [piece], ledger, collections,
                       icons={MIRRORED_PIECE_ID: make_icon(piece['menu']['style'])}, domain='highway')
    return {'registered': True, 'piece_id': MIRRORED_PIECE_ID, 'puzzle_id': piece['puzzle_id'],
            'footprint': piece['footprint'], 'occupied_cells': len(cells),
            'menu_family_anchor': PIECE_ID,
            'source': f'domains/highway/00_pieces/{MIRRORED_PIECE_ID}/piece.jsonc'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mirrored', action='store_true', help='Register only the mirrored counterpart and paired Tab selection')
    args = parser.parse_args()
    print(json.dumps(register_mirrored() if args.mirrored else register(), indent=2))
