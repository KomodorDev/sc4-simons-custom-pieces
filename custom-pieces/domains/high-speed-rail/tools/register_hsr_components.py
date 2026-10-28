#!/usr/bin/env python3
"""Reserve optional reusable HSR components without changing existing pieces.

Registration is not installation. Every source layout and the complete proposed
catalogue are checked before any manifest or allocation is written.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import jsonc
from scp.autotile import validate_auto_tile_addresses
from scp.catalog import load_catalog, number, piece_cells, validate_catalog
from scp.dbpf import require
from scp_hsr.icons import make_icon
from scp.inventory import write_inventories
from scp.subject_sources import piece_id_for_recipe, piece_name_for_recipe

SELECTION = 'hsr-all-components'


def register_components(info_by_recipe=None, recipes=None, *, root=None, selection=SELECTION):
    """Add missing components, preserving all existing manifests and IDs.

    The optional arguments allow the exact same allocator to be tested using a
    temporary catalogue. Normal invocation reads the model writer's INFO, which
    includes its final global support plan.
    """
    if info_by_recipe is None or recipes is None:
        from scp_hsr.hsr_components import INFO, RECIPES
        info_by_recipe = INFO if info_by_recipe is None else info_by_recipe
        recipes = RECIPES if recipes is None else recipes
    root = Path(ROOT if root is None else root)
    require(isinstance(selection, str) and selection.strip(), 'A named component selection is required')
    recipes = tuple(recipes)
    require(recipes and len(set(recipes)) == len(recipes),
            'Component recipes must be nonempty and unique')
    require(all(recipe.startswith('hsr_component_') for recipe in recipes),
            'Only reusable HSR component recipes belong in this selection')

    # Check the complete family before reserving even the first new identifier.
    # A later unsafe layout must not leave earlier entries partly registered.
    for recipe in recipes:
        info = info_by_recipe[recipe]
        cells = [list(cell) for cell in info['cells']]
        validate_auto_tile_addresses({
            'id': piece_id_for_recipe(recipe, root), 'footprint': list(info['footprint']),
            'cells': cells,
            'tile_ids': [f'{column*0x100 + row*0x10:08x}' for column, row in cells],
        })
        require(info.get('name') and info.get('description'),
                'Every component requires its own name and joining description')

    catalog = load_catalog(root)
    project = jsonc.load(root / 'project.jsonc')
    ledger = jsonc.load(root / 'config/allocations.jsonc')
    current = {piece['id']: piece for piece in catalog['pieces']}
    used_puzzles = {number(piece['puzzle_id']) for piece in ledger['pieces'].values()}
    used_blocks = {number(value) & 0xfffff000
                   for piece in ledger['pieces'].values()
                   for value in [piece['preview_id'], *piece['tile_ids'],
                                 *piece.get('resource_blocks', [])]}
    added, selected = [], []
    for recipe in recipes:
        info = info_by_recipe[recipe]
        owners = [piece for piece in catalog['pieces'] if piece['recipe'] == recipe]
        require(len(owners) <= 1,
                f'Ambiguous component recipe owner for {recipe}: '
                + ', '.join(piece['id'] for piece in owners))
        require(not owners or owners[0]['domain'] == 'high-speed-rail',
                'An HSR component recipe must belong to the high-speed-rail domain')
        # A scaffold allocates a permanent type ID independently of its later
        # recipe name. Resolve that existing owner before deriving a new slug.
        slug = owners[0]['id'] if owners else piece_id_for_recipe(recipe, root)
        selected.append(slug)
        cells = [list(cell) for cell in info['cells']]
        footprint = list(info['footprint'])
        if slug in current:
            piece = current[slug]
            require(piece['recipe'] == recipe and piece_cells(piece) == cells
                    and piece['footprint'] == footprint,
                    'Existing component coordinates are frozen; use a new recipe for a redesign')
            require(piece.get('structural_cells', []) ==
                    [list(cell) for cell in info.get('structural_cells', [])],
                    'Existing component structural-cell declarations differ from the implemented layout')
            require(not piece['enabled_by_default'],
                    'Reusable experimental components must remain optional')
            continue
        require(slug not in ledger['pieces'], 'An existing allocation must not be reused')
        puzzle = next((value for value in range(0xf7a0, 0xf900)
                       if value not in used_puzzles), None)
        span = (footprint[0] + 15) // 16
        block = next((value for value in range(0x7f500000,
                        0x7f600000 - span*0x1000 + 1, 0x1000)
                      if all(value + offset*0x1000 not in used_blocks
                             for offset in range(span))), None)
        require(puzzle is not None and block is not None,
                'Local identifier namespace exhausted')
        blocks = [block + offset*0x1000 for offset in range(span)]
        used_puzzles.add(puzzle)
        used_blocks.update(blocks)
        tiles = [f'{block + column*0x100 + row*0x10:08x}' for column, row in cells]
        component = deepcopy(info.get('component', {}))
        for key in ('kind', 'support_centers',
                    'support_foundation_width', 'support_min_spacing',
                    'custom_curved_interfaces'):
            if key in info:
                component[key] = deepcopy(info[key])
        effect_tag = info.get('effect_tag', 'hsrcomp')
        piece = {
            'schema_version': 1, 'id': slug, 'name': piece_name_for_recipe(recipe, info['name'], root),
            'description': info['description'], 'domain': 'high-speed-rail',
            'recipe': recipe, 'status': 'experimental', 'enabled_by_default': False,
            'puzzle_id': f'{puzzle:04x}', 'tile_ids': tiles,
            'preview_id': f'{blocks[-1] + 0xff5:08x}',
            'effect_name': f'preview_scp_{effect_tag}_{puzzle:04x}_00'.lower(),
            'footprint': footprint, 'cells': cells, 'orientation_count': 8,
            'structural_cells': deepcopy(info.get('structural_cells', [])),
            'orientation_policy': 'rotate-only-preserve-direction',
            'dependencies': ['controller', 'hsr'],
            'menu': {'id': f'{0x6a470000 | puzzle:08x}',
                     'order': f'{0x70120000 | puzzle:08x}', 'style': recipe.replace('_', '-')},
            'shadow_mappings': [{'tile': tile, 'source': tile, 'rotation': 0}
                                for tile in tiles],
            'provenance': deepcopy(info.get('provenance_record') or {
                'geometry': 'Authored modular HSR geometry using the audited NAM HSR profile and texture.',
                'construction': 'Separate component port contract; additive auto-tile addresses checked before allocation.',
                'redistribution': 'permission-pending',
            }),
            'game_tests': {key: 'unverified' for key in catalog['pieces'][0]['game_tests']},
            'category': 'hsr-components', 'component': component,
            'ports': deepcopy(info.get('ports', {})),
            'movements': deepcopy(info.get('movements', [])),
            'at_grade_conflicts': deepcopy(info.get('at_grade_conflicts', False)),
            'design_assessment': deepcopy(info.get('design_assessment') or {
                'stage': 'reusable component prototype',
                'scope': 'Individual component; assembly and game operation unverified',
            }),
        }
        require(len(piece['effect_name']) == 27,
                'Preview effect must retain native donor name length')
        validate_auto_tile_addresses(piece)
        allocation = {key: piece[key] for key in ('puzzle_id', 'tile_ids', 'preview_id', 'cells')}
        allocation.update(menu_id=piece['menu']['id'], tile_base=f'{block:08x}',
                          state='reserved-locally',
                          resource_blocks=[f'{value:08x}' for value in blocks])
        ledger['pieces'][slug] = allocation
        added.append(piece)

    candidate = deepcopy(catalog)
    candidate['pieces'].extend(added)
    candidate['_allocations'] = ledger
    candidate['piece_sets'][selection] = selected
    validate_catalog(candidate)
    # Fail an unavailable/invalid icon before changing any on-disk registry.
    icons = {piece['id']: make_icon(piece['menu']['style'])
             for piece in candidate['pieces'] if piece['id'] in selected}
    from scp.registration import apply_registration
    apply_registration(root, added, ledger, {selection: selected}, icons, domain='high-speed-rail')
    write_inventories(root)
    report = {'added': len(added), 'pieces': selected, 'selection': selection,
              'installed': False}
    print(json.dumps(report, indent=2))
    return report


if __name__ == '__main__':
    register_components()
