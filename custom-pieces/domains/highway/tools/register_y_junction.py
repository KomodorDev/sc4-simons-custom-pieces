#!/usr/bin/env python3
"""Allocate the measured Y owners and register their modular assembly."""
from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation'), str(Path(__file__).parent)]
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.catalog import load_catalog
from scp.model_shadows import allocation_fields
from scp.registration import apply_registration
from scp.subject_sources import new_subject_document
from scp_highway.menu import make_icon
from scp_highway.y_junction_layout import module_catalog
from scp_highway.y_junction_contracts import IDENTITIES
from scp_highway.y_junction_variants import ORIGINAL, REVERSED, VARIANTS, identities_for, assembly_for
from register_highway_pieces import _allocation, GAME_KEYS

ASSEMBLY = 'ddrhw-compact-diagonal-y-junction'
TITLE = 'DD RHW-4 — Compact Y-Junction — Diagonal Stem'
STYLES = {'diagonal-stem-split': 'ddrhw-y-stem', 'diagonal-branch': 'ddrhw-y-branch',
          'orthogonal-core': 'ddrhw-y-core'}


def register(root=ROOT, *, variant=ORIGINAL):
    root = Path(root).resolve()
    catalog = load_catalog(root)
    identifiers = tuple(identities_for(variant))
    assembly_id = assembly_for(variant)
    title = TITLE if variant == ORIGINAL else TITLE + ' — Reversed Traffic'
    if variant == REVERSED:
        from scp_highway.y_junction_reversed_layout import module_catalog as selected_catalog
        if selected_catalog().get('physical_layout_reviewed') is not True:
            raise ValueError('Review the actual reversed physical layout before allocating any permanent type')
    else:
        selected_catalog = module_catalog
    declarations = selected_catalog()['types']
    if {row['id'] for row in declarations} != set(identifiers):
        raise ValueError('The Y layout must declare exactly its three reviewed functional owners')
    cells = [tuple(c) for row in declarations for c in row['world_cells']]
    if len(cells) != len(set(cells)):
        raise ValueError('Y component construction owners overlap')
    ledger, additions = deepcopy(catalog['_allocations']), []
    existing = {p['id']: p for p in catalog['pieces']}
    for row in declarations:
        if row['id'] in existing:
            piece = existing[row['id']]
            if any(piece[key] != row[key] for key in ('recipe', 'cells', 'footprint', 'geometry_key', 'engineering')):
                raise ValueError('An existing Y identity has different construction coordinates or engineering bounds')
            continue
        puzzle, block, tiles = _allocation(ledger, row['cells'])
        piece = {
            'schema_version': 1, 'id': row['id'], 'domain': 'highway', 'name': row['name'],
            'description': row['function']+'. Place its owned cells at the matching assembly reference; every native deck retains its measured real car lanes.',
            'recipe': row['recipe'], 'geometry_key': row['geometry_key'],
            'enabled_by_default': False, 'status': 'experimental', 'puzzle_id': f'{puzzle:04x}',
            'tile_ids': tiles, 'preview_id': f'{block+0xff5:08x}',
            'effect_name': f'preview_scp_hw_{puzzle:04x}'.ljust(24, '_')+'001',
            'footprint': row['footprint'], 'cells': row['cells'], 'orientation_count': 8,
            'dependencies': ['controller', 'dd_rhw', 'rhw_core', 'mis'],
            'native_y_junction_approaches': True,
            'menu': {'id': f'{0x6a470000|puzzle:08x}', 'order': f'{0xffffff00|(puzzle&0xff):08x}',
                     'style': STYLES[row['key']]},
            'engineering': deepcopy(row['engineering']),
            'shadow_mode': 'model-carrier', 'shadow_mappings': [],
            'model_shadows': {'schema_version': 1, 'sun_profile': 'sc4-default-67p5-45', 'enabled': False,
                              'cells': [{'cell': cell, 'cast_shadow': False} for cell in row['cells']]},
            'provenance': {
                'geometry': 'Native-profile DD ends and six source-bound single-lane journeys; physical pavement, closed bodies, barriers, and supporting solids are compiled together before whole-cell ownership.',
                'construction': 'Three disjoint functional owners, one native outside socket per owner, and four proper rotations repeated across eight cursor states.',
                'granularity': row['function']+'. Shared decks and route fragments in a city tile retain one coordinated owner; full custom joining boundaries are supplied by checked connector exports.',
                'redistribution': 'permission-pending'},
            'game_tests': {key: 'unverified' for key in GAME_KEYS}}
        if variant == REVERSED:
            piece['y_junction_variant'] = REVERSED
        if row.get('authors_surface_atlas'):
            piece['authored_texture_ids'] = tiles[:1]
        ledger['pieces'][piece['id']] = {
            'puzzle_id': piece['puzzle_id'], 'tile_ids': tiles, 'preview_id': piece['preview_id'],
            'menu_id': piece['menu']['id'], 'state': 'reserved-locally', 'cells': piece['cells'],
            'tile_base': f'{block:08x}', 'resource_blocks': [f'{block:08x}'], **allocation_fields(piece)}
        additions.append(piece)
    if additions:
        apply_registration(root, additions, ledger, {assembly_id: list(identifiers)},
                           icons={piece['id']: make_icon(piece['menu']['style']) for piece in additions},
                           domain='highway')
    current = {p['id']: p for p in load_catalog(root)['pieces']}
    low_col, high_col = min(c[0] for c in cells), max(c[0] for c in cells)
    low_row, high_row = min(c[1] for c in cells), max(c[1] for c in cells)
    placements = []
    for index, row in enumerate(declarations, 1):
        piece = current[row['id']]
        col, tile_row = row['world_origin_cell']
        placements.append({'instance_id': f'P{index:02d}', 'label': f'P{index:02d}',
            'piece_id': piece['id'], 'name': piece['name']+f' at P{index:02d}',
            'menu_name': piece['name'], 'recipe': piece['recipe'],
            'origin_m': [16.*col, -16.*tile_row], 'rotation_degrees_ccw': 0, 'rotation_degrees': 0,
            'display_origin_tiles_en': [col-low_col, high_row-tile_row]})
    scene = {'title': title,
        'purpose': 'A southwest native DD stem splits its two lanes between a northwest diagonal branch and an east orthogonal branch; two separated one-lane graded connections complete all six journeys.',
        'geometry_status': 'Implementation candidate; actual software and human game evidence are recorded in TESTING.md.',
        'coordinate_units': 'metres east, north, and height; rotations counterclockwise',
        'coordinate_system': {'origin_world_m': [16.*low_col, -16.*high_row],
            'origin_name': 'southwest tile-centre reference', 'tile_size_m': 16,
            'tile_boundaries_offset_m': 8, 'axes': ['east', 'north', 'height']},
        'construction_rectangle_tiles': [high_col-low_col+1, high_row-low_row+1],
        'occupied_tiles': len(cells), 'module_placements': 3, 'component_types_used': 3,
        'traffic_policy': {'required_movements': ['A->B', 'B->A', 'A->C', 'C->A', 'B->C', 'C->B'],
                           'lanes_per_journey': 1, 'forbidden_movements': ['A->A', 'B->B', 'C->C'],
                           'native_upper_directions': {'A': 'incoming', 'B': 'outgoing', 'C': 'outgoing'},
                           'native_lower_directions': {'A': 'outgoing', 'B': 'incoming', 'C': 'incoming'}},
        'native_socket_cells_col_row': {'A': [-2, 2], 'B': [-2, -2], 'C': [4, 0]},
        'placements': placements, 'game_tests': {key: 'unverified' for key in GAME_KEYS}}
    if variant == REVERSED:
        scene['purpose'] = 'The same southwest, northwest, and east arms with every directed journey reversed and driver-left yellow markings on the opposite physical edges; both separate branch-to-branch links descend.'
        scene['y_junction_variant'] = REVERSED
        scene['traffic_policy']['native_upper_directions'] = {'A': 'outgoing', 'B': 'incoming', 'C': 'incoming'}
        scene['traffic_policy']['native_lower_directions'] = {'A': 'incoming', 'B': 'outgoing', 'C': 'outgoing'}
    target = root/'domains/highway/01_assemblies'/assembly_id
    path = target/'assembly.jsonc'
    if not path.exists():
        path.write_text(new_subject_document(scene, 'assembly'), encoding='utf-8')
    elif jsonc.load(path) != scene:
        raise ValueError('Existing Y assembly placements differ; review the changed physical allocation explicitly')
    registry_path = root/'domains/highway/domain.jsonc'
    registry = jsonc.load(registry_path)
    relative = f'01_assemblies/{assembly_id}/assembly.jsonc'
    if relative not in registry['assemblies']:
        registry['assemblies'].append(relative)
        jsonc.dump(registry_path, registry)
    menu_path = root/'domains/highway/menu-layout.jsonc'
    menus = jsonc.load(menu_path)
    button = '6a47fee5' if variant == ORIGINAL else '6a47fee6'
    order = 'fffffee5' if variant == ORIGINAL else 'fffffee6'
    if any(key != assembly_id and value.get('cycle_button', {}).get('id') == button
           for key, value in menus['layouts'].items()):
        raise ValueError('The selected new assembly button ID is already reserved by another layout')
    layout = {'assembly_id': assembly_id, 'member_order': 'first-use-in-assembly',
        'cycle_button': {'id': button, 'order': order, 'title': 'SCP | ASSEMBLY | '+title,
            'description': 'Tab and Shift+Tab select the diagonal stem, diagonal branch, and orthogonal core. Home and End rotate each component. Each click places one component; follow the three-placement table.'}}
    if assembly_id in menus['layouts'] and menus['layouts'][assembly_id] != layout:
        raise ValueError('Existing Y menu declaration differs from its reviewed single-button cycle')
    menus['layouts'][assembly_id] = layout
    jsonc.dump(menu_path, menus)
    return {'new_types': len(additions), 'assembly': assembly_id, 'piece_ids': list(identifiers),
            'owned_cells': len(cells), 'construction_rectangle_tiles': scene['construction_rectangle_tiles']}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--variant', choices=VARIANTS, default=ORIGINAL)
    args = parser.parse_args()
    print(json.dumps(register(variant=args.variant), indent=2))
