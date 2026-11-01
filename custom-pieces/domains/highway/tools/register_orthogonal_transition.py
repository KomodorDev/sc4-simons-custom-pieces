#!/usr/bin/env python3
"""Register the six-tile coupled DD-to-ground adapter with new local identities."""
from __future__ import annotations

from copy import deepcopy
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
from scp_highway.orthogonal_approaches import PIECE_ID, RECIPE, CORE_CELLS
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


if __name__ == '__main__':
    print(json.dumps(register(), indent=2))
