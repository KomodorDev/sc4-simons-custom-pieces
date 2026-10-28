#!/usr/bin/env python3
"""Register current adjacent-line scissors switches."""
import json
from pathlib import Path
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp import jsonc
from scp.catalog import load_catalog, number
from scp.dbpf import require
from scp_hsr.icons import make_icon
from scp.inventory import write_inventories
from scp.subject_sources import piece_id_for_recipe, piece_name_for_recipe


def main():
    from scp_hsr.rail_repairs import INFO, RECIPES
    catalog = load_catalog(ROOT)
    project = jsonc.load(ROOT/'project.jsonc')
    ledger = jsonc.load(ROOT/'config/allocations.jsonc')
    current = {piece['id']:piece for piece in catalog['pieces']}
    used_puzzles = {number(p['puzzle_id']) for p in ledger['pieces'].values()}
    used_blocks = {number(value)&0xfffff000 for p in ledger['pieces'].values()
                   for value in [p['preview_id'], *p['tile_ids'], *p.get('resource_blocks', [])]}
    additions, identifiers = [], []
    for recipe in RECIPES:
        info = INFO[recipe]
        owners = [piece for piece in catalog['pieces'] if piece['recipe'] == recipe]
        require(len(owners) <= 1, f'Ambiguous scissors recipe owner: {recipe}')
        require(not owners or owners[0]['domain'] == 'high-speed-rail',
                'A rail scissors recipe must belong to the high-speed-rail domain')
        slug = owners[0]['id'] if owners else piece_id_for_recipe(recipe, ROOT)
        identifiers.append(slug)
        cells = [list(cell) for cell in info['cells']]
        if slug in current:
            require(current[slug]['recipe']==recipe and current[slug]['cells']==cells and current[slug]['footprint']==list(info['footprint']),
                    f'{slug}: reserved geometry grid cannot be changed')
            continue
        require(slug not in ledger['pieces'], 'Existing allocation cannot be reused for a new piece')
        puzzle = next((n for n in range(0xf7a0,0xf900) if n not in used_puzzles),None)
        block = next((n for n in range(0x7f500000,0x7f600000,0x1000) if n not in used_blocks),None)
        require(puzzle is not None and block is not None, 'Reviewed local identifier namespace exhausted')
        used_puzzles.add(puzzle); used_blocks.add(block)
        level = 'ghsr' if recipe.startswith('rail_ghsr_') else 'hsr'
        style = f'rail-{level}-scissors-revised'
        tiles = [f'{block+x*0x100+row*0x10:08x}' for x,row in cells]
        name = piece_name_for_recipe(recipe, f'{level.upper()} Adjacent Scissors Revised', ROOT)
        description = (f'{name}. Corrected rail deck union and branch openings; '
                       'one shared support per occupied elevated tile, no ground-track pillars. '
                       'Authored 5 m wide by 5 m high route clearance check. '
                       'Experimental; actual game placement and train operation remain unverified.')
        piece = {'schema_version':1,'id':slug,'name':name,'description':description,
                 'recipe':recipe,'domain':'high-speed-rail','status':'experimental',
                 'enabled_by_default':True,'puzzle_id':f'{puzzle:04x}',
                 'tile_ids':tiles,'preview_id':f'{block+0xff5:08x}',
                 'effect_name':f'preview_scp_railfix_{puzzle:04x}_00',
                 'footprint':list(info['footprint']),'cells':cells,'orientation_count':8,
                 'orientation_policy':'rotate-only-preserve-direction',
                 'dependencies':['controller','hsr'],
                 'menu':{'id':f'{0x6a470000|puzzle:08x}','order':f'{0x70110000|puzzle:08x}','style':style},
                 'shadow_mappings':[{'tile':tile,'source':tile,'rotation':0} for tile in tiles],
                 'provenance':{'geometry':'NAM HSR/GHSR profile and texture; authored union decks and consolidated supports.',
                               'construction':'Reviewed Monorail ports and directed movements; independent construction audit.',
                               'redistribution':'permission-pending'},
                 'game_tests':{key:'unverified' for key in catalog['pieces'][0]['game_tests']},
                 'category':'revised-rail-junctions',
                 'ports':info['ports'],'movements':info['movements']}
        require(len(piece['effect_name'])==27,'Preview effect name must match native donor length')
        require(name.casefold() not in {p['name'].casefold() for p in catalog['pieces']+additions},'Duplicate menu name')
        allocation={key:piece[key] for key in ('puzzle_id','tile_ids','preview_id','cells')}
        allocation.update({'menu_id':piece['menu']['id'],'tile_base':f'{block:08x}',
                           'state':'reserved-locally','resource_blocks':[f'{block:08x}']})
        ledger['pieces'][slug]=allocation
        additions.append(piece)
    from scp.registration import apply_registration
    icons = {p['id']: make_icon(p['menu']['style']) for p in [*catalog['pieces'], *additions]
             if p['id'] in identifiers}
    apply_registration(ROOT, additions, ledger, {'revised-rail-junctions': identifiers}, icons,
                       domain='high-speed-rail')
    write_inventories(ROOT)
    print(json.dumps({'added':len(additions),'revised_pieces':identifiers,'installed':False},indent=2))


if __name__=='__main__':main()
