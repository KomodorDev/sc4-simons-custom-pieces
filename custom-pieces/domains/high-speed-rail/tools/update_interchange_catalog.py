#!/usr/bin/env python3
"""Register current modular interchange definitions with collision-free identifiers.

Run from the project parent with Python 3.11+: 
python3 custom-pieces/domains/high-speed-rail/tools/update_interchange_catalog.py
Generation is a development action; it does not install or publish anything.
Existing piece coordinates are frozen. A changed layout needs a new recipe ID.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp import jsonc
from scp.catalog import load_catalog, number
from scp.dbpf import require
from scp_hsr.icons import make_icon
from scp_hsr.interchange_layouts import RECIPES, INFO
from scp.inventory import write_inventories
from scp.subject_identity import canonical_piece_id, canonical_piece_name

LEVEL_NAMES = {'ground': 'GHSR', 'hsr': 'HSR L2', 'l3': 'Rail L3', 'l4': 'Rail L4'}


def presentation(recipe, info, root=None):
    level = LEVEL_NAMES.get(info.get('level'), info.get('level', 'Rail'))
    kind = info['kind']
    if kind == 'oneway_filler':
        name = f'One-Way {level} {info["shape"].replace("_", " ").title()}'
    elif kind == 'oneway_turn':
        name = f'One-Way {level} {info["angle"]} Degree {info["hand"].title()} {info["radius"].title()} Curve'
    elif kind == 'directed_branch':
        name = f'{level} {info["mode"].title()} {info["angle"]} Degree {info["radius"].title()}'
    elif kind == 'oneway_grade':
        name = f'One-Way {LEVEL_NAMES[info["from_level"]]} to {LEVEL_NAMES[info["to_level"]]} Ramp'
    elif kind == 'flyover_crossing':
        name = f'One-Way L4 over {LEVEL_NAMES[info["lower_level"]]} Crossing'
    else:
        name = info.get('name', recipe.removeprefix('interchange_').replace('_', ' ').title())
    name = canonical_piece_name(recipe, info.get('name', name), ROOT if root is None else root)
    width, depth = info['footprint']
    description = info.get('description') or (
        f'{name}. Fixed click-to-place piece in a {width} by {depth} tile area. '
        'Follow the arrows and join only matching track widths, directions, and height labels. '
        'Four proper rotations; the second four states repeat them. Experimental; game testing pending.')
    if kind == 'directed_branch':
        description += (' The L4 mainline and branch are both one-way single tracks.' if info['level'] == 'l4'
                        else ' The mainline retains both directions; only the branch is one-way.')
    if kind == 'flyover_crossing' and info.get('one_way_position') == 'lower':
        description += ' The lower track is one-way and the upper track is two-way; there is no transfer.'
    elif kind == 'flyover_crossing':
        description += ' The upper route crosses without transferring to the lower two-way route.'
    return name, description


def main():
    catalog = load_catalog(ROOT)
    project_path, ledger_path = ROOT/'project.jsonc', ROOT/'config/allocations.jsonc'
    project, ledger = jsonc.load(project_path), jsonc.load(ledger_path)
    current = {piece['id']: piece for piece in catalog['pieces']}
    used_names = {piece['name'].casefold() for piece in catalog['pieces']}
    used_puzzles = {number(record['puzzle_id']) for record in ledger['pieces'].values()}
    used_blocks = {number(value)&0xfffff000 for record in ledger['pieces'].values()
                   for value in [record['preview_id'], *record['tile_ids'], *record.get('resource_blocks', [])]}
    additions, registered = [], []
    game_keys = catalog['pieces'][0]['game_tests']
    groups = {}
    for recipe in RECIPES:
        info = INFO[recipe]
        owners = [piece for piece in catalog['pieces'] if piece['recipe'] == recipe]
        require(len(owners) <= 1, f'Ambiguous interchange recipe owner: {recipe}')
        require(not owners or owners[0]['domain'] == 'high-speed-rail',
                'An interchange recipe must belong to the high-speed-rail domain')
        slug = owners[0]['id'] if owners else canonical_piece_id(recipe, ROOT)
        require(len(slug) <= 64, 'Recipe identifier exceeds the catalog limit')
        cells = [list(cell) for cell in info['cells']]
        footprint = list(info['footprint'])
        registered.append(slug)
        groups.setdefault(info['category'], []).append(slug)
        if slug in current:
            require(current[slug]['recipe'] == recipe and current[slug].get('cells') == cells and current[slug]['footprint'] == footprint,
                    f'{slug}: layout changed after reservation; create a new recipe ID')
            continue
        require(slug not in ledger['pieces'], f'{slug}: identifier already reserved')
        puzzle = next((n for n in range(0xf7a0, 0xf900) if n not in used_puzzles), None)
        require(puzzle is not None, 'Local puzzle namespace exhausted')
        span = (footprint[0]+15)//16
        block = next((n for n in range(0x7f500000, 0x7f600000-span*0x1000+1, 0x1000)
                      if all(n+part*0x1000 not in used_blocks for part in range(span))), None)
        require(block is not None, 'Local contiguous model namespace exhausted')
        blocks = [block+part*0x1000 for part in range(span)]
        used_puzzles.add(puzzle); used_blocks.update(blocks)
        tiles = [f'{block+0x100*x+0x10*y:08x}' for x,y in cells]
        preview = f'{block+span*0x1000-11:08x}'
        name, description = presentation(recipe, info, ROOT)
        require(name.casefold() not in used_names, f'Duplicate menu name before reservation: {name}')
        used_names.add(name.casefold())
        piece = {'schema_version':1,'id':slug,'name':name,'description':description,
                 'domain':'high-speed-rail','recipe':recipe,'enabled_by_default':True,
                 'status':'experimental','puzzle_id':f'{puzzle:04x}','tile_ids':tiles,
                 'preview_id':preview,'effect_name':f'preview_scp_interchg_{puzzle:04x}_0',
                 'footprint':footprint,'cells':cells,'orientation_count':8,
                 'orientation_policy':'rotate-only-preserve-direction',
                 'dependencies':['controller','hsr'],
                 'menu':{'id':f'{0x6a470000|puzzle:08x}','order':f'{0x70110000|puzzle:08x}','style':slug},
                 'shadow_mappings':[{'tile':tile,'source':tile,'rotation':0} for tile in tiles],
                 'provenance':{'geometry':'NAM HSR/GHSR native texture and profile with SCP authored geometry.',
                               'construction':'SCP directed Monorail PATHs and independent fixed-piece rules.',
                               'redistribution':'permission-pending'},
                 'game_tests':{key:'unverified' for key in game_keys},
                 'category':info['category'],'structural_cells':[list(cell) for cell in info.get('structural_cells',[])],
                 'ports':info['ports'],
                 'interchange':{key:info[key] for key in ('kind','level','height','angle','radius',
                                  'mode','from_level','to_level','lower_level','heading','trunk_level',
                                  'branch_level','movements','hand','upper_heading','lower_heading',
                                  'one_way_position') if key in info}}
        require(len(piece['effect_name']) == 27, 'Preview effect name length must match donor')
        allocation = {key:piece[key] for key in ('puzzle_id','tile_ids','preview_id','cells')}
        allocation.update({'menu_id':piece['menu']['id'],'tile_base':f'{block:08x}',
                           'state':'reserved-locally','resource_blocks':[f'{value:08x}' for value in blocks]})
        ledger['pieces'][slug] = allocation
        additions.append(piece)
    from scp.registration import apply_registration
    icons = {p['id']: make_icon(p['menu']['style']) for p in [*catalog['pieces'], *additions]
             if p['id'] in registered}
    apply_registration(ROOT, additions, ledger, {'rail-interchanges': registered, **groups}, icons,
                       domain='high-speed-rail')
    write_inventories(ROOT)
    print(json.dumps({'added':len(additions),'interchange_pieces':len(registered),
                      'installed':False,'published':False},indent=2))


if __name__ == '__main__':
    main()
