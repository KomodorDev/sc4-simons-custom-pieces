#!/usr/bin/env python3
"""Register the approved close parallel diamond without changing older types."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation'),
                str(Path(__file__).parent)]
from scp import jsonc
from scp.adaptive_network import allocation_fields, expected_solutions
from scp.catalog import load_catalog
from scp.registration import apply_registration
from scp.subject_sources import new_subject_document
from scp_highway.menu import make_icon
from scp_highway.parallel_layout import module_catalog
from register_highway_pieces import _allocation, GAME_KEYS
from register_modular_highway import _free_block, _marker

ASSEMBLY = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond'
COLLECTION = 'ddrhw-parallel-diamond'


def _name(declaration):
    key, name = declaration['key'], declaration['name']
    if key == 'crossing':
        return 'DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel'
    if declaration['function'] == 'terminal':
        return 'Avenue — ' + name + ' — Parallel DD RHW'
    return ('DD RHW-4 — ' if declaration['function'] == 'slip' else 'RHW Ramp — ') + name + ' — Parallel'


def register(root=ROOT):
    root = Path(root).resolve()
    catalog = load_catalog(root)
    ledger = deepcopy(catalog['_allocations'])
    existing = {piece['id']: piece for piece in catalog['pieces']}
    occupied = set(expected_solutions(catalog['pieces']))
    declarations = module_catalog()['types']
    additions, members = [], []
    for declaration in declarations:
        key = declaration['key']
        identifier = 'ddrhw-parallel-' + key
        members.append(identifier)
        if identifier in existing:
            piece = existing[identifier]
            if piece['cells'] != declaration['cells'] or piece['recipe'] != declaration['recipe']:
                raise ValueError('An existing parallel type differs from the frozen partition')
            continue
        puzzle, _block, _tiles = _allocation(ledger, declaration['cells'])
        adaptive_cells = declaration['engineering']['native_avenue_cells']
        block = _free_block(ledger, 2 if adaptive_cells else 1)
        tile_ids = [f'{block + x * 0x100 + y * 0x10:08x}' for x, y in declaration['cells']]
        engineering = {**deepcopy(declaration['engineering']), 'max_grade_percent': 30.0,
                       'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
                       'pavement_path_offset_m': 0.0}
        piece = {'schema_version': 1, 'id': identifier, 'domain': 'highway',
                 'name': _name(declaration),
                 'description': 'Place one ' + declaration['name'].lower() +
                     ' for the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.',
                 'recipe': declaration['recipe'], 'geometry_key': 'parallel-' + key,
                 'enabled_by_default': False, 'status': 'experimental',
                 'puzzle_id': f'{puzzle:04x}', 'tile_ids': tile_ids,
                 'preview_id': f'{block + 0xff5:08x}',
                 'effect_name': f'preview_scp_hw_{puzzle:04x}'.ljust(24, '_') + '001',
                 'footprint': declaration['footprint'], 'cells': declaration['cells'],
                 'orientation_count': 8, 'dependencies': ['controller', 'dd_rhw', 'rhw_core', 'mis'],
                 'menu': {'id': f'{0x6a470000 | puzzle:08x}',
                          'order': f'{0xffffff00 | (puzzle & 0xff):08x}', 'style': 'ddrhw-ramp'},
                 'engineering': engineering, 'shadow_mode': 'generated',
                 'shadow_mappings': [{'tile': tile, 'source': tile, 'rotation': 0} for tile in tile_ids],
                 'provenance': {'geometry': 'Approved parallel inward-upper layout with exact source coordinates, finite right turns, and fixed levels.',
                                'construction': 'Disjoint whole-cell traffic owners; separate physical models may overhang neighbouring cells.',
                                'redistribution': 'permission-pending'},
                 'game_tests': {name: 'unverified' for name in GAME_KEYS}}
        record = {'puzzle_id': piece['puzzle_id'], 'tile_ids': tile_ids,
                  'preview_id': piece['preview_id'], 'menu_id': piece['menu']['id'],
                  'state': 'reserved-locally', 'cells': piece['cells'],
                  'tile_base': f'{block:08x}', 'resource_blocks': [f'{block:08x}']}
        ledger['pieces'][identifier] = record
        if adaptive_cells:
            origin = declaration['world_origin_cell']
            rows = []
            for index, cell in enumerate(declaration['cells']):
                world = [cell[0] + origin[0], cell[1] + origin[1]]
                if world not in adaptive_cells:
                    continue
                difference = world[0] - world[1]
                avenue = {0: 0x01030103, 1: 0x01000003, -1: 0x00030100}[difference]
                rows.append({'cell': cell, 'rotation': 2 if difference == 1 else 0,
                             'texture_donor_id': f'{0x04003800 if difference == 0 else 0x04000200:08x}',
                             'street_flags': _marker(avenue, occupied), 'avenue_flags': f'{avenue:08x}',
                             'prop': True, 'resolved_tile_id': f'{block + 0x1000 + index * 0x100:08x}'})
            if len(rows) != len(declaration['cells']):
                raise ValueError('Parallel adaptive declarations must be entirely adaptive')
            piece['adaptive_ground'] = {'schema_version': 1, 'construction_helper': [1, 1], 'cells': rows}
            piece['dependencies'].append('adaptive_avenue')
            record['resource_blocks'].append(f'{block + 0x1000:08x}')
            record.update(allocation_fields(piece))
        additions.append(piece)
    if additions:
        apply_registration(root, additions, ledger, {COLLECTION: members},
                           icons={p['id']: make_icon('ddrhw-ramp') for p in additions}, domain='highway')
    all_pieces = {piece['id']: piece for piece in load_catalog(root)['pieces']}
    placements = []
    for index, declaration in enumerate(declarations, 1):
        identifier = 'ddrhw-parallel-' + declaration['key']
        piece = all_pieces[identifier]
        x, y = [value + 4 for value in declaration['world_origin_cell']]
        label = f'P{index:02d}'
        placements.append({'instance_id': label, 'label': label, 'piece_id': identifier,
                           'origin_m': [16.0 * x, -16.0 * y],
                           'rotation_degrees_ccw': 0, 'rotation_degrees': 0,
                           'display_origin_tiles_en': [x, 9 - y],
                           'name': piece['name'] + ' at ' + label, 'menu_name': piece['name'],
                           'recipe': piece['recipe']})
    scene = {'title': 'DD RHW-4 — Parallel Diagonal Avenue Diamond',
             'purpose': 'Close parallel graded ramps beside a straight double-decker highway, with perpendicular right-turn-only Avenue approaches and independently placed functional components.',
             'geometry_status': 'Experimental native resource implementation; software and human observations retain separate scope.',
             'coordinate_units': 'metres east,north,height; rotations counterclockwise',
             'coordinate_system': {'origin_world_m': [0.0, -144.0],
                                   'origin_name': 'retained southwest tile-centre reference',
                                   'tile_size_m': 16, 'tile_boundaries_offset_m': 8,
                                   'axes': ['east', 'north', 'height']},
             'construction_rectangle_tiles': [8, 8], 'reference_grid_rectangle_tiles': [10, 10],
             'occupied_tiles': 31, 'module_placements': len(placements),
             'component_types_used': len(members), 'separately_available_component_types': len(members),
             'traffic_policy': {'ramp_access': 'adjacent-carriageway right turns only',
                                'required_movements': ['SW->NE', 'NE->SW', 'NW->SE', 'SE->NW', 'NE->NW', 'NW->SW', 'SW->SE', 'SE->NE'],
                                'forbidden_cross_avenue_turns': ['NE->SE', 'SE->SW', 'SW->NW', 'NW->NE']},
             'placements': placements, 'game_tests': {key: 'unverified' for key in GAME_KEYS}}
    directory = root / 'domains/highway/01_assemblies' / ASSEMBLY
    directory.mkdir(parents=True, exist_ok=True)
    definition = directory / 'assembly.jsonc'
    if not definition.exists():
        definition.write_text(new_subject_document(scene, 'assembly'))
    from scp.content import assembly_document_scaffold
    for name, source in assembly_document_scaffold({**scene, 'id': ASSEMBLY, 'name': scene['title']}).items():
        if not (directory / name).exists():
            (directory / name).write_text(source)
    registry_path = root / 'domains/highway/domain.jsonc'
    registry = jsonc.load(registry_path)
    relative = f'01_assemblies/{ASSEMBLY}/assembly.jsonc'
    if relative not in registry['assemblies']:
        registry['assemblies'].append(relative)
        jsonc.dump(registry_path, registry)
    return {'new_types': len(additions), 'members': members, 'assembly': ASSEMBLY,
            'placements': len(placements), 'occupied_tiles': 31}


if __name__ == '__main__':
    print(json.dumps(register(), indent=2))
