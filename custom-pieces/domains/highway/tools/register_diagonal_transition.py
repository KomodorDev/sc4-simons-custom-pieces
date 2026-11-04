#!/usr/bin/env python3
"""Register only the independently reviewed first diagonal transition cut."""
from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation'),
                str(Path(__file__).parent)]

from scp.catalog import load_catalog
from scp.dbpf import require
from scp.model_shadows import allocation_fields
from scp.registration import apply_registration
from scp_highway import diagonal_transition_layout as layout
from scp_highway import diagonal_transition_variants as variants
from scp_highway.menu import make_icon
from register_highway_pieces import _allocation, GAME_KEYS

COLLECTION = 'ddrhw-diagonal-ground-transition-alignment-a'
SELECTOR_SUFFIXES = ('original', 'mirrored', 'opposite', 'opposite-mirrored')


def register(root=ROOT):
    root = Path(root).resolve()
    modules = layout.module_catalog()
    require(modules.get('alignment') == 'a'
            and modules.get('physical_layout_reviewed') is True
            and modules.get('native_shoulder_ownership_reviewed') is True,
            'Diagonal registration requires reviewed physical layout and finite native shoulder ownership')
    from scp_highway.diagonal_transition_verify import validate_layout_metadata
    rows = modules['types']
    require([row['id'] for row in rows] == list(variants.PIECE_IDS)
            and [row['recipe'] for row in rows] == list(variants.RECIPES),
            'Diagonal registration requires the exact four first-cut types')
    for row in rows:
        validate_layout_metadata(row, row['key'])
    catalog = load_catalog(root)
    existing = {piece['id']: piece for piece in catalog['pieces']}
    ledger = deepcopy(catalog['_allocations'])
    additions, icons = [], {}
    for row in rows:
        key, identifier = row['key'], row['id']
        cells = deepcopy(row['cells'])
        anchor = {} if identifier == variants.PIECE_ID else {'family_anchor': variants.PIECE_ID}
        expected_engineering = {**deepcopy(row['engineering']), 'max_grade_percent': 20.0,
            'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
            'pavement_path_offset_m': 0.0}
        if identifier in existing:
            piece = existing[identifier]
            variants.variant_of(piece)
            require(piece['cells'] == cells and piece['footprint'] == row['footprint']
                    and piece['engineering'] == expected_engineering
                    and piece.get('native_diagonal_transition_approaches') is True
                    and piece['menu'].get('family_anchor') == anchor.get('family_anchor'),
                    'Existing diagonal type differs from its reviewed first-cut function or footprint')
            continue
        puzzle, block, tiles = _allocation(ledger, cells)
        piece = {'schema_version': 1, 'domain': 'highway', 'id': identifier,
            'name': row['name'],
            'description': 'A diagonal paired ramp converts the stacked L1/L2 DD RHW-4 into two ground RHW-4 carriageways. It preserves two lanes per direction, the selected upper-road side and traffic phase, driver-left yellow markings, and explicitly measured first-cut native sockets.',
            'recipe': row['recipe'], 'diagonal_transition_variant': key,
            'diagonal_transition_alignment': 'a', 'status': 'experimental',
            'enabled_by_default': False, 'puzzle_id': f'{puzzle:04x}',
            'tile_ids': tiles, 'preview_id': f'{block + 0xff5:08x}',
            'effect_name': f'preview_scp_hw_{puzzle:04x}'.ljust(24, '_') + '001',
            'footprint': deepcopy(row['footprint']), 'cells': cells, 'orientation_count': 8,
            'dependencies': ['controller', 'dd_rhw', 'rhw_core', 'rhw4', 'rhw4_textures'],
            'native_diagonal_transition_approaches': True,
            'menu': {'id': f'{0x6a470000 | puzzle:08x}',
                     'order': f'{0xffffff00 | (puzzle & 0xff):08x}',
                     'style': 'ddrhw-diagonal-transition', **anchor},
            'authored_texture_ids': tiles[:1], 'engineering': expected_engineering,
            'shadow_mode': 'model-carrier', 'shadow_mappings': [],
            'model_shadows': {'schema_version': 1, 'sun_profile': 'sc4-default-67p5-45',
                'enabled': False, 'cells': [{'cell': cell, 'cast_shadow': False} for cell in cells]},
            'provenance': {
                'geometry': 'Measured diagonal DD and ground RHW-4 native interfaces, an independently reviewed sparse mask, four same-lane journeys, and curve-aware height profiles. No orthogonal profile or reflected cell mask substitutes for actual diagonal measurements.',
                'construction': 'Explicit flat constraints on every reviewed owned cell; three unowned native sockets with their separately audited finite peers; four proper rotations repeated across eight cursor states.',
                'granularity': 'One independently useful coordinated DD-to-ground conversion per side/traffic choice. Interior slope and curve sections do not expose a proven standard native connection for an arbitrary split.',
                'alignment': 'First explicit longitudinal native mouth cut only. The adjacent 302/309 cut is not supplied by four rotations or inferred from the parallel transverse spacing.',
                'redistribution': 'permission-pending'},
            'game_tests': {name: 'unverified' for name in GAME_KEYS}}
        ledger['pieces'][identifier] = {'puzzle_id': piece['puzzle_id'], 'tile_ids': tiles,
            'preview_id': piece['preview_id'], 'menu_id': piece['menu']['id'],
            'state': 'reserved-locally', 'cells': cells, 'tile_base': f'{block:08x}',
            'resource_blocks': [f'{block:08x}'], **allocation_fields(piece)}
        additions.append(piece)
        icons[identifier] = make_icon(piece['menu']['style'])
    if not additions:
        return {'registered': False, 'piece_ids': list(variants.PIECE_IDS),
                'reason': 'All reviewed first-cut types already exist; retained sources preserved'}
    collections = {COLLECTION: list(variants.PIECE_IDS)}
    collections.update({COLLECTION+'-'+suffix: [row['id']]
                        for row, suffix in zip(rows, SELECTOR_SUFFIXES, strict=True)})
    apply_registration(root, additions, ledger, collections, icons=icons, domain='highway')
    return {'registered': True, 'new_piece_ids': [piece['id'] for piece in additions],
            'menu_family_anchor': variants.PIECE_ID, 'alignment': 'a',
            'resources': [{'id': piece['id'], 'puzzle_id': piece['puzzle_id'],
                           'tile_base': ledger['pieces'][piece['id']]['tile_base'],
                           'owned_cells': len(piece['cells']), 'footprint': piece['footprint']}
                          for piece in additions]}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(register(args.root), indent=2))
