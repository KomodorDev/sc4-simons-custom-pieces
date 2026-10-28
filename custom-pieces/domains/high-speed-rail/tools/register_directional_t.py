#!/usr/bin/env python3
"""Reserve a separate identifier for each deliberately designed T example."""
import json
from pathlib import Path
import sys

ROOT=next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp import jsonc
from scp.catalog import load_catalog,number
from scp.dbpf import require
from scp_hsr.icons import make_icon
from scp.inventory import write_inventories
from scp.autotile import validate_auto_tile_addresses


def register_examples(info_by_recipe,recipes,selection_name):
    catalog=load_catalog(ROOT)
    project=jsonc.load(ROOT/'project.jsonc')
    ledger=jsonc.load(ROOT/'config/allocations.jsonc')
    current={p['id']:p for p in catalog['pieces']}
    used_puzzles={number(p['puzzle_id']) for p in ledger['pieces'].values()}
    used_blocks={number(value)&0xfffff000 for p in ledger['pieces'].values()
                 for value in [p['preview_id'],*p['tile_ids'],*p.get('resource_blocks',[])]}
    selected=[];added=[]
    for recipe in recipes:
        info=info_by_recipe[recipe];slug=recipe.replace('_','-');selected.append(slug)
        cells=[list(cell) for cell in info['cells']]
        footprint=list(info['footprint'])
        validate_auto_tile_addresses({'id':slug,'footprint':footprint,'cells':cells,
            'tile_ids':[f'{0x100*x+0x10*y:08x}' for x,y in cells]})
        if slug in current:
            require(current[slug]['cells']==cells and current[slug]['footprint']==footprint,
                    'Existing example coordinates are frozen; add a new recipe for a redesign')
            continue
        require(slug not in ledger['pieces'],'An existing allocation must not be reused')
        puzzle=next((n for n in range(0xf7a0,0xf900) if n not in used_puzzles),None)
        span=(footprint[0]+15)//16
        block=next((n for n in range(0x7f500000,0x7f600000-span*0x1000+1,0x1000)
                    if all(n+part*0x1000 not in used_blocks for part in range(span))),None)
        require(puzzle is not None and block is not None,'Local identifier namespace exhausted')
        blocks=[block+part*0x1000 for part in range(span)]
        used_puzzles.add(puzzle);used_blocks.update(blocks)
        tiles=[f'{block+0x100*x+0x10*row:08x}' for x,row in cells]
        name=info.get('name','HSR Smooth T-Junction — At Grade')
        orientation='Diagonal' if 'diagonal' in recipe else 'Straight'
        description=info.get('description') or (f'{name}. {orientation} HSR mainline with four direct smooth turning connections. '
            'All routes stay at the native HSR path height of 15.5 m. '
            'This is an at-grade junction: turning routes cross other routes at the same height. '
            'It is not a flyover and adds no train signalling or conflict simulation. '
            'New visual-review example; experimental, with actual game operation unverified.')
        piece={'schema_version':1,'id':slug,'name':name,'description':description,
            'domain':'high-speed-rail','recipe':recipe,'status':'experimental','enabled_by_default':False,
            'puzzle_id':f'{puzzle:04x}','tile_ids':tiles,'preview_id':f'{blocks[-1]+0xff5:08x}',
            'effect_name':f'preview_scp_{info.get("effect_tag", "smoothT")}_{puzzle:04x}_00'.lower(),
            'footprint':footprint,'cells':cells,'orientation_count':8,
            'orientation_policy':'rotate-only-preserve-direction','dependencies':['controller','hsr'],
            'menu':{'id':f'{0x6a470000|puzzle:08x}','order':f'{0x70110000|puzzle:08x}','style':slug},
            'shadow_mappings':[{'tile':tile,'source':tile,'rotation':0} for tile in tiles],
            'provenance':info.get('provenance_record') or {'geometry':'Deliberately authored direct HSR curves and native NAM profile/texture.',
                'construction':'Explicit full-T port contract; intended same-height conflicts remain declared.',
                'redistribution':'permission-pending'},
            'game_tests':{key:'unverified' for key in catalog['pieces'][0]['game_tests']},
            'category':info.get('category','redesigned-junction-examples'),'ports':info.get('ports',{}),
            'movements':info.get('movements',[]),'at_grade_conflicts':info.get('at_grade_conflicts',True),
            'design_assessment':info.get('design_assessment') or {'stage':'single visual-review example','scope':'same-height full T; not a replacement flyover'}}
        require(len(piece['effect_name'])==27,'Preview effect must retain native donor name length')
        allocation={k:piece[k] for k in ('puzzle_id','tile_ids','preview_id','cells')}
        allocation.update(menu_id=piece['menu']['id'],tile_base=f'{block:08x}',
                          state='reserved-locally',resource_blocks=[f'{value:08x}' for value in blocks])
        ledger['pieces'][slug]=allocation
        added.append(piece)
    from scp.registration import apply_registration
    collections = {selection_name: selected,
        'smooth-t-junctions': [p['id'] for p in [*catalog['pieces'], *added]
                              if p['recipe'].startswith('directional_hsr_t_smooth')]}
    icons = {p['id']: make_icon(p['menu']['style']) for p in [*catalog['pieces'], *added]
             if p['id'] in selected}
    apply_registration(ROOT, added, ledger, collections, icons, domain='high-speed-rail')
    write_inventories(ROOT)
    print(json.dumps({'added':len(added),'pieces':selected,'installed':False},indent=2))


def main():
    from scp_hsr.directional_t import INFO,RECIPES
    register_examples(INFO,RECIPES,'redesigned-junction-example')


if __name__=='__main__':main()
