#!/usr/bin/env python3
"""Register independently implemented highway types with permanent local IDs."""
from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.catalog import load_catalog, number, validate_catalog
from scp.registration import apply_registration
from scp.subject_sources import new_subject_document, write_subject
from scp_highway.menu import make_icon
from scp_highway.native import CELLS, RECIPE


CORE_ID = 'ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg'
GAME_KEYS = ('placement', 'traffic_both_directions', 'no_unwanted_transfers',
             'rotations_and_mirrors', 'shadows', 'demolition', 'save_reload')
ASSEMBLY_ID = 'ddrhw-l1-and-l2-diagonal-avenue-diamond'


def register_compact_modules(root=ROOT, *, review_partition=False):
    """Reserve the reviewed disjoint modules, then register their placement plan."""
    from scp_highway.ramp_paths import module_catalog
    root = Path(root).resolve()
    catalog = load_catalog(root)
    modules = module_catalog()
    existing = {piece['id']: piece for piece in catalog['pieces']}
    ledger = deepcopy(catalog['_allocations'])
    reviewed = {}
    for module in modules['types']:
        identifier = 'ddrhw-diagonal-' + module['key']
        if identifier not in existing or existing[identifier]['cells'] == module['cells']:
            continue
        piece = deepcopy(existing[identifier])
        reviewed_ids = {'ddrhw-diagonal-upper-entry-branch', 'ddrhw-diagonal-upper-exit-branch'}
        if (not review_partition or identifier not in reviewed_ids or
                ledger['pieces'][identifier]['state'] != 'reserved-locally' or
                piece['footprint'] != module['footprint'] or
                piece['cells'] != [[0, 0], [1, 0], [0, 1], [1, 1]] or
                module['cells'] != [[1, 0], [0, 1], [1, 1]]):
            raise ValueError('Changed registered cells must match the two independently reviewed upper-branch cuts')
        original = {tuple(cell): tile for cell, tile in zip(piece['cells'], piece['tile_ids'])}
        piece['cells'] = module['cells']
        piece['tile_ids'] = [original[tuple(cell)] for cell in piece['cells']]
        if piece.get('authored_texture_ids'):
            piece['authored_texture_ids'] = piece['tile_ids'][:1]
        piece['shadow_mappings'] = [{'tile': tile, 'source': tile, 'rotation': 0} for tile in piece['tile_ids']]
        piece['engineering']['model_only_cells'] = module['engineering']['model_only_cells']
        piece['provenance']['partition_review'] = ('Detached unchanged native continuation A; all remaining tile IDs, '
            'puzzle, preview, menu, and reserved resource-block identities are preserved.')
        ledger['pieces'][identifier].update(cells=piece['cells'], tile_ids=piece['tile_ids'])
        reviewed[identifier] = piece
    if reviewed:
        candidate = deepcopy(catalog)
        candidate['pieces'] = [reviewed.get(piece['id'], piece) for piece in catalog['pieces']]
        candidate['_allocations'] = ledger
        validate_catalog(candidate)
        for identifier, piece in reviewed.items():
            write_subject(root / 'domains/highway/00_pieces' / identifier, 'piece', piece)
            existing[identifier] = piece
        allocation_path = root / catalog['allocations']
        allocation_path.write_text(jsonc.document(ledger, source=allocation_path.read_text()), encoding='utf-8')
    additions, identities = [], {}
    for module in modules['types']:
        key = module['key']
        identifier = 'ddrhw-diagonal-' + key
        recipe = 'highway_ddrhw_compact_' + key.replace('-', '_')
        name = 'DD RHW-4 — ' + module['name'].removeprefix('DD RHW-4 ')
        identities[key] = identifier
        if identifier in existing:
            piece = existing[identifier]
            if piece['recipe'] != recipe or piece['cells'] != module['cells']:
                raise ValueError('Existing compact module identity differs from the reviewed partition')
            continue
        puzzle, block, tiles = _allocation(ledger, module['cells'])
        piece = {
            'schema_version': 1, 'id': identifier, 'domain': 'highway', 'name': name,
            'description': ('Reusable ' + key.replace('-', ' ') + ' component of the compact diagonal '
                            'double-decker highway and Avenue interchange. Place its owned tiles exactly '
                            'as shown in the assembly guide; traffic uses actual car and pedestrian PATHs.'),
            'recipe': recipe, 'geometry_key': key, 'enabled_by_default': False,
            'status': 'experimental', 'puzzle_id': f'{puzzle:04x}', 'tile_ids': tiles,
            'preview_id': f'{block + 0xFF5:08x}',
            'effect_name': f'preview_scp_hw_{puzzle:04x}'.ljust(24, '_') + '001',
            'footprint': module['footprint'], 'cells': module['cells'], 'orientation_count': 8,
            'dependencies': ['controller', 'dd_rhw', 'rhw_core'],
            'menu': {'id': f'{0x6A470000 | puzzle:08x}',
                     'order': f'{0xFFFFFF00 | (puzzle & 0xFF):08x}', 'style': 'ddrhw-ramp'},
            'engineering': {'max_grade_percent': 40.0, 'car_corridor_half_width_m': 1.25,
                            'car_corridor_height_m': 3.8, 'pavement_path_offset_m': 0.0,
                            'model_only_cells': module['engineering']['model_only_cells']},
            'shadow_mode': 'generated',
            'shadow_mappings': [{'tile': tile, 'source': tile, 'rotation': 0} for tile in tiles],
            'provenance': {'geometry': 'Measured native DD RHW-4 and Avenue channels with authored compact ramps.',
                           'construction': 'Reviewed exclusive tile partition; four proper rotations repeated.',
                           'redistribution': 'permission-pending'},
            'game_tests': {key: 'unverified' for key in GAME_KEYS},
        }
        if module['authors_surface_atlas']:
            piece['authored_texture_ids'] = tiles[:1]
        ledger['pieces'][identifier] = {'puzzle_id': piece['puzzle_id'], 'tile_ids': tiles,
            'preview_id': piece['preview_id'], 'menu_id': piece['menu']['id'], 'state': 'reserved-locally',
            'cells': piece['cells'], 'tile_base': f'{block:08x}', 'resource_blocks': [f'{block:08x}']}
        additions.append(piece)
    members = [identities[module['key']] for module in modules['types']]
    if additions:
        apply_registration(root, additions, ledger, {'ddrhw-compact-diagonal-diamond': members},
                           icons={piece['id']: make_icon('ddrhw-ramp') for piece in additions}, domain='highway')
    current = {piece['id']: piece for piece in load_catalog(root)['pieces']}
    placements = []
    for index, item in enumerate(modules['placements'], 1):
        piece = current[identities[item['geometry_key']]]
        column, row = item['origin']
        placements.append({'instance_id': f'P{index:02}', 'label': f'P{index:02}',
                           'name': piece['name'] + f' at P{index:02}', 'menu_name': piece['name'],
                           'piece_id': piece['id'], 'recipe': piece['recipe'],
                           'origin_m': [16.0 * column, -16.0 * row],
                           'rotation_degrees_ccw': 0, 'rotation_degrees': 0,
                           'display_origin_tiles_en': [column, modules['footprint'][1] - 1 - row]})
    scene = {'purpose': 'Build the compact diagonal DD RHW-4 and Avenue diamond from individually placeable modules.',
             'id': ASSEMBLY_ID, 'title': 'DD RHW-4 — Compact Diagonal Avenue Diamond',
             'geometry_status': 'Experimental compiled modules; see TESTING.md for current software and game evidence.',
             'coordinate_units': 'metres east,north,height; rotations counterclockwise',
             'construction_rectangle_tiles': modules['footprint'], 'occupied_tiles': len(modules['occupied_cells']),
             'module_placements': len(placements), 'component_types_used': len(members),
             'separately_available_component_types': len(members), 'placements': placements,
             'game_tests': {key: 'unverified' for key in GAME_KEYS}}
    domain = root / 'domains/highway'
    directory = domain / '01_assemblies' / ASSEMBLY_ID
    target = directory / 'assembly.jsonc'
    if target.exists():
        write_subject(directory, 'assembly', scene)
    else:
        target.write_text(new_subject_document(scene, 'assembly'), encoding='utf-8')
    if not (directory / 'icon.png').is_file():
        (directory / 'icon.png').write_bytes(make_icon('ddrhw-ramp'))
    registry_path = domain / 'domain.jsonc'
    registry = jsonc.load(registry_path)
    relative = target.relative_to(domain).as_posix()
    if relative not in registry['assemblies']:
        registry['assemblies'].append(relative)
        registry_path.write_text(jsonc.document(registry, source=registry_path.read_text()), encoding='utf-8')
    layout = {'schema_version': 1, 'purpose': 'One Roads button cycles through the compact diamond component types.',
              'layouts': {'compact-diagonal-diamond': {'assembly_id': ASSEMBLY_ID,
              'member_order': 'first-use-in-assembly',
              'cycle_button': {'id': '6a47fee0', 'order': 'fffffee0',
              'title': 'SCP | ASSEMBLY | ' + scene['title'],
              'description': 'Tab and Shift+Tab select one reusable component; Home and End rotate it. Each click places one component. Follow the assembly placement table.'}}}}
    header = ('// title: "Highway assembly menu layouts"\n'
              '// summary: "Define the compact diamond component cycle and its locally reserved Roads button."\n//\n'
              '// Used when: scp.py assembly-menu prepares this assembly from a verified normal build.\n'
              '// Read by: scp.menu_experiment.build_assembly_menu().\n'
              '// Updated by: domains/highway/tools/register_highway_pieces.py after reviewing module membership.\n'
              '// Affects: The component cycling order and one assembly menu button; geometry and game observations are separate.\n')
    (domain / 'menu-layout.jsonc').write_text(header + json.dumps(layout, indent=2) + '\n', encoding='utf-8')
    load_catalog(root)
    return {'registered_modules': len(additions), 'assembly': ASSEMBLY_ID, 'types': len(members), 'placements': len(placements)}


def _allocation(ledger, cells):
    puzzles = {number(record['puzzle_id']) for record in ledger['pieces'].values()}
    puzzle = next((value for value in range(0xF7A0, 0xF900) if value not in puzzles), None)
    if puzzle is None:
        raise ValueError('Reviewed local puzzle namespace is exhausted')
    blocks = {number(iid) & 0xFFFFF000 for record in ledger['pieces'].values()
              for iid in [record['preview_id'], *record['tile_ids'], *record.get('resource_blocks', [])]}
    block = next((value for value in range(0x7F500000, 0x7F600000, 0x1000) if value not in blocks), None)
    if block is None:
        raise ValueError('Reviewed local model namespace is exhausted')
    tile_ids = [f'{block + x * 0x100 + y * 0x10:08x}' for x, y in cells]
    return puzzle, block, tile_ids


def register_native_crossing(root=ROOT):
    root = Path(root).resolve()
    catalog = load_catalog(root)
    existing = next((piece for piece in catalog['pieces'] if piece['id'] == CORE_ID), None)
    if existing:
        if existing['recipe'] != RECIPE or existing['cells'] != [list(cell) for cell in CELLS]:
            raise ValueError('Existing highway identity has a different recipe or footprint')
        return {'registered': False, 'reason': 'already registered; identities preserved', 'piece': CORE_ID}
    ledger = deepcopy(catalog['_allocations'])
    puzzle, block, tiles = _allocation(ledger, CELLS)
    name = ('DD RHW-4 Level 1 (7.5 m) and Level 2 (15 m) over Avenue Ground (0 m)'
            ' — Diagonal Crossing 90°')
    piece = {
        'schema_version': 1, 'id': CORE_ID, 'domain': 'highway', 'name': name,
        'description': ('Five coordinated construction tiles preserve the native stacked DD RHW-4 lanes '
                        'above both directions of a diagonal avenue, including avenue pedestrians. '
                        'This crossing supplies through routes; connecting access ramps are separate components.'),
        'recipe': RECIPE, 'enabled_by_default': False, 'status': 'experimental',
        'puzzle_id': f'{puzzle:04x}', 'tile_ids': tiles, 'preview_id': f'{block + 0xFF5:08x}',
        'effect_name': f'preview_scp_hw_{puzzle:04x}'.ljust(24, '_') + '001',
        'footprint': [3, 3], 'cells': [list(cell) for cell in CELLS], 'orientation_count': 8,
        'dependencies': ['controller', 'dd_rhw', 'rhw_core'],
        'menu': {'id': f'{0x6A470000 | puzzle:08x}', 'order': f'{0xFFFFFF00 | (puzzle & 0xFF):08x}',
                 'style': 'ddrhw-crossing'},
        'shadow_mode': 'generated',
        'shadow_mappings': [{'tile': tile, 'source': tile, 'rotation': 0} for tile in tiles],
        'provenance': {'geometry': 'Independently measured native NAM DD RHW-4 and Avenue channels.',
                       'construction': 'Explicit five-cell RUL0 construction; measured native network flags; four proper rotations repeated.',
                       'redistribution': 'permission-pending'},
        'game_tests': {key: 'unverified' for key in GAME_KEYS},
    }
    ledger['pieces'][CORE_ID] = {'puzzle_id': piece['puzzle_id'], 'tile_ids': tiles,
        'preview_id': piece['preview_id'], 'menu_id': piece['menu']['id'], 'state': 'reserved-locally',
        'cells': piece['cells'], 'tile_base': f'{block:08x}', 'resource_blocks': [f'{block:08x}']}
    apply_registration(root, [piece], ledger, {'ddrhw-diagonal-avenue-crossing': [CORE_ID]},
                       icons={CORE_ID: make_icon(piece['menu']['style'])}, domain='highway')
    return {'registered': True, 'piece': CORE_ID, 'puzzle_id': piece['puzzle_id'],
            'source': f'domains/highway/00_pieces/{CORE_ID}/piece.jsonc'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--compact-modules', action='store_true')
    parser.add_argument('--review-partition', action='store_true',
                        help='Apply the independently reviewed subset cut while preserving remaining resource identities')
    args = parser.parse_args()
    print(register_native_crossing(args.root))
    if args.compact_modules:
        print(register_compact_modules(args.root, review_partition=args.review_partition))


if __name__ == '__main__':
    main()
