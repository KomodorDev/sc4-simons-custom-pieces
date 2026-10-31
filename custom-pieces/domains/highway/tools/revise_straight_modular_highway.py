#!/usr/bin/env python3
"""Apply the reviewed straight stamp and full ramp ownership to local reservations."""
from copy import deepcopy
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'framework'),str(ROOT/'domains/highway/implementation'),str(Path(__file__).parent)]
from scp import jsonc
from scp.catalog import load_catalog,number,tile_base,validate_catalog
from scp.registration import apply_registration
from scp.subject_sources import write_subject
from scp_highway.modular_stamp import declaration
from scp_highway.modular_ramps import module_catalog
from scp_highway.menu import make_icon
from register_highway_pieces import _allocation,GAME_KEYS
from register_modular_highway import _free_block

STAMP='ddrhw-modular-highway-stamp'
ASSEMBLY='ddrhw-l1-and-l2-diagonal-avenue-modular-diamond'


def revise(root=ROOT):
    root=Path(root).resolve();catalog=load_catalog(root);ledger=deepcopy(catalog['_allocations'])
    by_id={p['id']:deepcopy(p) for p in catalog['pieces']}
    declarations=[declaration(),*module_catalog()['types']]
    additions=[];changed=[]
    for d in declarations:
        identifier=STAMP if d['key']=='modular-stamp' else 'ddrhw-modular-'+d['key']
        if identifier in by_id:
            p=by_id[identifier];allocation=ledger['pieces'][identifier]
            if allocation['state']!='reserved-locally':raise ValueError('Only unpublished local reservations may change')
            base=tile_base(p)
        else:
            puzzle,_old,_ids=_allocation(ledger,d['cells']);base=_free_block(ledger)
            p={'schema_version':1,'id':identifier,'domain':'highway','recipe':d['recipe'],'geometry_key':d['key'],
               'enabled_by_default':False,'status':'experimental','puzzle_id':f'{puzzle:04x}',
               'preview_id':f'{base+0xff5:08x}','effect_name':f'preview_scp_hw_{puzzle:04x}'.ljust(24,'_')+'001',
               'orientation_count':8,'dependencies':['controller','dd_rhw','rhw_core','mis'],
               'menu':{'id':f'{0x6a470000|puzzle:08x}','order':f'{0xffffff00|(puzzle&0xff):08x}','style':'ddrhw-ramp'},
               'shadow_mode':'generated','provenance':{'geometry':'Complete compact ramp body, including the separately rendered high throat.',
               'construction':'Disjoint ramp-owned cells plus explicit model overhang into highway-owned cells.','redistribution':'permission-pending'},
               'game_tests':{key:'unverified' for key in GAME_KEYS}}
            allocation={'puzzle_id':p['puzzle_id'],'preview_id':p['preview_id'],'menu_id':p['menu']['id'],
                        'state':'reserved-locally','tile_base':f'{base:08x}','resource_blocks':[f'{base:08x}']}
            ledger['pieces'][identifier]=allocation;additions.append(p)
        p['name']=('DD RHW-4 — Straight Diagonal Highway Stamp' if identifier==STAMP else
                   'RHW Ramp — '+d['name'].replace('Exit Ramp','Full Exit Ramp').replace('Entry Ramp','Full Entry Ramp'))
        p['description']=('Straight double-decker highway with slip lanes and barrier cutouts only. All curved ramp pavement, undersides, and barriers are separately placed attachments.' if identifier==STAMP else
            'Separately placed '+d['name']+'. Includes its entire curved high throat at the highway cutout, including explicit model overhang. Construction and traffic-path ownership remain disjoint.')
        p.update(cells=deepcopy(d['cells']),footprint=deepcopy(d['footprint']),engineering=deepcopy(d['engineering']))
        p['tile_ids']=[f'{base+x*0x100+y*0x10:08x}' for x,y in p['cells']]
        blocks={number(x) for x in allocation['resource_blocks']}
        if any(number(t)&0xfffff000 not in blocks for t in p['tile_ids']):raise ValueError('Repartition exceeds reserved blocks')
        p['shadow_mappings']=[{'tile':t,'source':t,'rotation':0} for t in p['tile_ids']]
        if 'model_overhang_source_cells' in d:
            p['model_overhang_source_cells']=deepcopy(d['model_overhang_source_cells'])
            p['model_overhang_contract']=d['model_overhang_contract']
        p['provenance']['partition_review']='Corrected straight21-cell highway stamp; all four complete curved high throats belong to separate ramps. Retains puzzle, menu, preview, and reserved block identities. Uninstalled prototype local tile slots follow the reviewed new AutoTileBase grid.'
        allocation.update(cells=deepcopy(p['cells']),tile_ids=p['tile_ids'],tile_base=f'{base:08x}')
        by_id[identifier]=p;changed.append(p)
    candidate=deepcopy(catalog);candidate['pieces']=list(by_id.values());candidate['_allocations']=ledger
    # New types are registered together with their current finite recipe declarations.
    new_ids={p['id'] for p in additions}
    for p in changed:
        if p['id'] not in new_ids:write_subject(root/'domains/highway/00_pieces'/p['id'],'piece',p)
    jsonc.dump(root/'config/allocations.jsonc',dict(ledger,pieces={k:v for k,v in ledger['pieces'].items() if k not in new_ids}))
    if additions:
        apply_registration(root,additions,ledger,{},icons={p['id']:make_icon('ddrhw-ramp') for p in additions},domain='highway')
    default=[STAMP]+['ddrhw-modular-'+d['key'] for d in module_catalog()['types'] if not d['key'].endswith('-compact')]
    compact=['ddrhw-modular-'+d['key'] for d in module_catalog()['types'] if d['key'].endswith('-compact')]
    junctions=['ddrhw-diagonal-northwest-junction','ddrhw-diagonal-southeast-junction']
    sets=jsonc.load(root/'domains/highway/collections.jsonc');sets['collections']['ddrhw-modular-ramp-kit']=default+compact+junctions
    jsonc.dump(root/'domains/highway/collections.jsonc',sets)
    scene_path=root/'domains/highway/01_assemblies'/ASSEMBLY/'assembly.jsonc';scene=jsonc.load(scene_path)
    def pose(identifier,index,prefix='P'):
        p=by_id[identifier]
        if identifier==STAMP:origin=(-4,-4)
        elif identifier.startswith('ddrhw-modular-'):origin=next(d['world_origin_cell'] for d in declarations if d['recipe']==p['recipe'])
        else:
            from scp_highway.ramp_paths import module_catalog as old_catalog
            origin=next(d['world_origin_cell'] for d in old_catalog()['types'] if d['recipe']==p['recipe'])
        x,y=(origin[0]+4,origin[1]+4)
        return {'instance_id':f'{prefix}{index:02d}','label':f'{prefix}{index:02d}','piece_id':identifier,
                'origin_m':[16.*x,-16.*y],'rotation_degrees_ccw':0,'rotation_degrees':0,
                'display_origin_tiles_en':[x,9-y],'name':p['name']+f' at {prefix}{index:02d}',
                'menu_name':p['name'],'recipe':p['recipe']}
    scene['placements']=[pose(key,i) for i,key in enumerate(default,1)]
    scene['purpose']='One completely straight highway stamp with barrier cutouts. All four complete curved ramps and both Avenue terminals are placed separately.'
    scene['separately_available_component_types']=13
    scene['alternatives']['compact'].update(purpose='The same completely straight stamp with four separately placed full compact ramps and the two retained Avenue junctions.',placements=[pose(key,i,'C') for i,key in enumerate([STAMP,*compact,*junctions],1)],menu='Four full compact ramps and two compact Avenue junctions retain separate icons outside the seven-component R40 cycle.')
    jsonc.dump(scene_path,scene)
    load_catalog(root)
    print({'new_full_compact_types':len(additions),'straight_stamp_cells':21,'default_component_cells':[len(by_id[k]['cells']) for k in default],'kit_types':13})


if __name__=='__main__':revise()
