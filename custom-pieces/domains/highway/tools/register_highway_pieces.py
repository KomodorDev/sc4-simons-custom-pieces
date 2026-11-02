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
from scp.catalog import load_catalog, number, tile_base, validate_catalog
from scp.registration import apply_registration
from scp.subject_sources import new_subject_document, write_subject
from scp_highway.menu import make_icon
from scp_highway.native import CELLS, RECIPE


CORE_ID = 'ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg'
GAME_KEYS = ('placement', 'traffic_both_directions', 'no_unwanted_transfers',
             'rotations_and_mirrors', 'shadows', 'demolition', 'save_reload')
ASSEMBLY_ID = 'ddrhw-l1-and-l2-diagonal-avenue-diamond'


EXTENSION_REVIEW = {
    'lower-exit-branch': ([1, 1], [[0, 0]], [2, 2], [[0, 0], [1, 0], [0, 1]]),
    'lower-entry-branch': ([1, 1], [[0, 0]], [2, 2], [[0, 0], [1, 0], [0, 1]]),
    'lower-exit-grade': ([1, 1], [[0, 0]], [1, 2], [[0, 0], [0, 1]]),
    'lower-entry-grade': ([1, 1], [[0, 0]], [2, 1], [[0, 0], [1, 0]]),
    'upper-exit-branch': ([2, 2], [[1, 0], [0, 1], [1, 1]], [3, 3], [[2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2]]),
    'upper-entry-branch': ([2, 2], [[1, 0], [0, 1], [1, 1]], [3, 3], [[1, 0], [2, 0], [1, 1], [2, 1], [0, 2], [1, 2]]),
    'upper-exit-grade': ([2, 2], [[1, 0], [0, 1], [1, 1]], [2, 3], [[1, 0], [0, 1], [1, 1], [0, 2]]),
    'upper-entry-grade': ([2, 2], [[1, 0], [0, 1], [1, 1]], [3, 2], [[1, 0], [2, 0], [0, 1], [1, 1]]),
}


def reviewed_extension(catalog, modules):
    """Prepare the exact unpublished extension, preserving reserved identity blocks.

    A changed local origin changes its AutoTileBase offsets. Retain each
    existing local resource slot rather than attaching IDs to world cells;
    new cells may use only the same piece's already reserved resource block.
    No installed or published allocation is eligible for this review.
    """
    candidate = deepcopy(catalog)
    pieces = {piece['id']: piece for piece in candidate['pieces']}
    ledger = candidate['_allocations']
    for module in modules['types']:
        identifier = 'ddrhw-diagonal-' + module['key']
        if identifier not in pieces or ledger['pieces'][identifier]['state'] != 'reserved-locally':
            raise ValueError('Ramp extension review requires an existing locally reserved component')
        piece = pieces[identifier]
        if module['key'] in EXTENSION_REVIEW:
            before_size, before_cells, after_size, after_cells = EXTENSION_REVIEW[module['key']]
            if (module['footprint'], module['cells']) != (after_size, after_cells):
                raise ValueError('Ramp extension differs from its independently reviewed partition')
            if (piece['footprint'], piece['cells']) not in ((before_size, before_cells), (after_size, after_cells)):
                raise ValueError('Ramp extension source is neither the reviewed original nor its current revision')
        elif (piece['footprint'], piece['cells']) != (module['footprint'], module['cells']):
            raise ValueError('Ramp extension cannot change an unreviewed component footprint')
        base = tile_base(piece)
        tiles = [f'{base + x * 0x100 + y * 0x10:08x}' for x, y in module['cells']]
        blocks = {number(value) for value in ledger['pieces'][identifier]['resource_blocks']}
        if any(number(tile) & 0xfffff000 not in blocks for tile in tiles):
            raise ValueError('Ramp extension exceeds the component reserved resource blocks')
        piece.update(cells=deepcopy(module['cells']), footprint=deepcopy(module['footprint']), tile_ids=tiles)
        piece['engineering'].update(deepcopy(module['engineering']))
        piece['dependencies'] = ['controller', 'dd_rhw', 'rhw_core', 'mis']
        if piece.get('adaptive_ground'):
            piece['dependencies'].append('adaptive_avenue')
        piece.pop('authored_texture_ids', None)
        piece['shadow_mappings'] = [{'tile': tile, 'source': tile, 'rotation': 0} for tile in tiles]
        piece['provenance']['partition_review'] = (
            'Reviewed one-diagonal-tile ramp extension and right-turn-only access. '
            'Retains piece, puzzle, menu, preview, and reserved resource-block identities; '
            'local model slots follow the revised AutoTileBase grid. Native MIS materials replace the flat atlas.')
        ledger['pieces'][identifier].update(cells=deepcopy(piece['cells']), tile_ids=tiles)
    validate_catalog(candidate)
    return candidate


def register_compact_modules(root=ROOT, *, review_partition=False, review_ramp_extension=False):
    """Reserve the reviewed disjoint modules, then register their placement plan."""
    from scp_highway.ramp_paths import module_catalog
    root = Path(root).resolve()
    catalog = load_catalog(root)
    modules = module_catalog()
    if review_ramp_extension:
        candidate = reviewed_extension(catalog, modules)
        for piece in candidate['pieces']:
            if piece['id'].startswith('ddrhw-diagonal-'):
                write_subject(root / 'domains/highway/00_pieces' / piece['id'], 'piece', piece)
        allocation_path = root / catalog['allocations']
        allocation_path.write_text(jsonc.document(candidate['_allocations'], source=allocation_path.read_text()), encoding='utf-8')
        catalog = load_catalog(root)
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
            'dependencies': ['controller', 'dd_rhw', 'rhw_core', 'mis'],
            'menu': {'id': f'{0x6A470000 | puzzle:08x}',
                     'order': f'{0xFFFFFF00 | (puzzle & 0xFF):08x}', 'style': 'ddrhw-ramp'},
            'engineering': {'max_grade_percent': module['engineering']['max_grade_percent'], 'car_corridor_half_width_m': 1.25,
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
             'coordinate_system': {'origin_world_m': [0.0, -16.0 * (modules['footprint'][1] - 1)],
                                   'origin_name': 'southwest tile-centre reference', 'tile_size_m': 16,
                                   'tile_boundaries_offset_m': 8, 'axes': ['east', 'north', 'height']},
             'traffic_policy': {'ramp_access': 'adjacent-carriageway right turns only',
                                'required_movements': ['SW->NE', 'NE->SW', 'NW->SE', 'SE->NW',
                                                       'NE->NW', 'NW->SW', 'SW->SE', 'SE->NE'],
                                'forbidden_cross_avenue_turns': ['NE->SE', 'SE->SW', 'SW->NW', 'NW->NE'],
                                'ramp_extension': 'One diagonal city-grid step: 16 m east/north components and 22.627416998 m along the highway.'},
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
    layout = {'schema_version': 1, 'purpose': 'One Highways button cycles through the compact diamond component types.',
              'layouts': {'compact-diagonal-diamond': {'assembly_id': ASSEMBLY_ID,
              'member_order': 'first-use-in-assembly',
              'cycle_button': {'id': '6a47fee0', 'order': 'fffffee0',
              'title': 'SCP | ASSEMBLY | ' + scene['title'],
              'description': 'Tab and Shift+Tab select one reusable component; Home and End rotate it. Each click places one component. Follow the assembly placement table.'}}}}
    header = ('// title: "Highway assembly menu layouts"\n'
              '// summary: "Define the compact diamond component cycle and its locally reserved Highways button."\n//\n'
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
              for iid in [record['preview_id'], *record['tile_ids'], *record.get('resource_blocks', []),
                          *record.get('adaptive_tile_ids', []), *record.get('extra_model_ids', [])]}
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


def register_ghsr_crossing(root=ROOT, *, alignment='a'):
    """Allocate one reusable crossing; preserve every existing game identity."""
    from scp.model_shadows import allocation_fields
    from scp_highway.ghsr_approaches import PIECE_ID
    from scp_highway import ghsr_crossing
    if alignment not in ('a', 'b'):
        raise ValueError('DD/GHSR alignment must be a or b')
    anchor_id = PIECE_ID
    if alignment == 'b':
        PIECE_ID = 'ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b'
        recipe, cells = ghsr_crossing.ALIGNMENT_B_RECIPE, ghsr_crossing.ALIGNMENT_B_CELLS
        footprint = list(ghsr_crossing.ALIGNMENT_B_FOOTPRINT)
        transition = ghsr_crossing.ALIGNMENT_B_TRANSITION_METADATA
    else:
        recipe, cells = ghsr_crossing.RECIPE, ghsr_crossing.CELLS
        footprint = list(ghsr_crossing.FOOTPRINT)
        transition = ghsr_crossing.TRANSITION_METADATA
    root = Path(root).resolve()
    catalog = load_catalog(root)
    existing = next((piece for piece in catalog['pieces'] if piece['id'] == PIECE_ID), None)
    if existing:
        if existing['recipe'] != recipe or existing['cells'] != [list(cell) for cell in cells]:
            raise ValueError('Existing DD/GHSR crossing identity has different geometry')
        return {'registered': False, 'reason': 'already registered; identities preserved', 'piece': PIECE_ID}
    ledger = deepcopy(catalog['_allocations'])
    puzzle, block, tiles = _allocation(ledger, cells)
    name = ('DD RHW-4 Level 1 (7.5 m) and Level 2 (15 m) over GHSR Ground (1 m)'
            ' — Mixed Crossing — Both Diagonal 90°')
    if alignment == 'b':
        name += ' — Alignment B'
    piece = {
        'schema_version': 1, 'id': PIECE_ID, 'domain': 'highway', 'name': name,
        'description': ('Two fixed tiles carry both directions of diagonal ground high-speed rail beneath '
                        'the two diagonal DD RHW-4 decks. Four unowned native approach tiles seed actual '
                        'NAM draggable continuation. Rail and highway have independent through routes.'),
        'recipe': recipe, 'enabled_by_default': False, 'status': 'experimental',
        'puzzle_id': f'{puzzle:04x}', 'tile_ids': tiles, 'preview_id': f'{block + 0xFF5:08x}',
        'effect_name': f'preview_scp_hw_{puzzle:04x}'.ljust(24, '_') + '001',
        'footprint': footprint, 'cells': [list(cell) for cell in cells], 'orientation_count': 8,
        'dependencies': ['controller', 'dd_rhw', 'rhw_core', 'hsr'],
        'menu': {'id': f'{0x6A470000 | puzzle:08x}', 'order': f'{0xFFFFFF00 | (puzzle & 0xFF):08x}',
                 'style': 'ddrhw-ghsr-crossing'},
        'native_ghsr_approaches': True,
        'shadow_mode': 'model-carrier', 'shadow_mappings': [],
        'model_shadows': {'schema_version': 1, 'sun_profile': 'sc4-default-67p5-45', 'enabled': False,
                          'cells': [{'cell': list(cell), 'cast_shadow': True,
                                     'resource_base': f'{block + 0x800 + index * 0x100:08x}'}
                                    for index, cell in enumerate(cells)]},
        'engineering': {'ghsr_path_height_m': 1., 'ddrhw_path_heights_m': [7.5, 15.],
                        'minimum_ddrhw_underside_m': 6.5,
                        'reviewed_train_envelope_height_m': 5.,
                        'reviewed_train_envelope_width_m': 5.,
                        'minimum_train_roof_clearance_m': .5,
                        'rail_path_transition': deepcopy(transition)},
        'provenance': {'geometry': 'Pinned NAM 50 native six-mesh DD halves and ordinary GHSR valid track mesh.',
                       'construction': 'Two protected DirtRoad/Monorail cells; four disjoint dynamic native helpers; four proper rotations repeated.',
                       'redistribution': 'permission-pending'},
        'game_tests': {key: 'unverified' for key in GAME_KEYS},
    }
    if alignment == 'b':
        piece['description'] = ('Alignment B fits the alternate diagonal railway position beneath the same directed '
                                'double-decker highway. Two horizontal fixed tiles and four native approaches '
                                'provide independent rail and highway through routes. When both alignments are '
                                'selected, Tab changes between A and B from the original crossing button.')
        piece['menu']['family_anchor'] = anchor_id
        piece['engineering']['diagonal_alignment'] = 'b'
    ledger['pieces'][PIECE_ID] = {'puzzle_id': piece['puzzle_id'], 'tile_ids': tiles,
        'preview_id': piece['preview_id'], 'menu_id': piece['menu']['id'], 'state': 'reserved-locally',
        'cells': piece['cells'], 'tile_base': f'{block:08x}', 'resource_blocks': [f'{block:08x}'],
        **allocation_fields(piece)}
    collections = ({'ddrhw-diagonal-ghsr-crossing-alignment-b': [PIECE_ID],
                    'ddrhw-diagonal-ghsr-crossing-alignments': [anchor_id, PIECE_ID]}
                   if alignment == 'b' else {'ddrhw-diagonal-ghsr-crossing': [PIECE_ID]})
    apply_registration(root, [piece], ledger, collections,
                       icons={PIECE_ID: make_icon(piece['menu']['style'])}, domain='highway')
    return {'registered': True, 'piece': PIECE_ID, 'puzzle_id': piece['puzzle_id']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--compact-modules', action='store_true')
    parser.add_argument('--ghsr-crossing', action='store_true',
                        help='Register the independently checked two-cell diagonal DD/GHSR crossing')
    parser.add_argument('--ghsr-alignment', choices=('a', 'b'), default='a',
                        help='Select the original or alternate diagonal DD/GHSR grid alignment')
    parser.add_argument('--review-partition', action='store_true',
                        help='Apply the independently reviewed subset cut while preserving remaining resource identities')
    parser.add_argument('--review-ramp-extension', action='store_true',
                        help='Apply the reviewed locally reserved 53-cell ramp extension and native MIS materials')
    args = parser.parse_args()
    if args.ghsr_crossing:
        print(register_ghsr_crossing(args.root, alignment=args.ghsr_alignment))
    else:
        print(register_native_crossing(args.root))
    if args.compact_modules:
        print(register_compact_modules(args.root, review_partition=args.review_partition,
                                       review_ramp_extension=args.review_ramp_extension))


if __name__ == '__main__':
    main()
