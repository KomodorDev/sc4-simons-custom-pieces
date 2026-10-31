#!/usr/bin/env python3
"""Register a highway stamp and separately attached, reviewed R40 components."""
from __future__ import annotations
from copy import deepcopy
import itertools
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation'), str(Path(__file__).parent)]
from scp import jsonc
from scp.adaptive_network import allocation_fields, expected_solutions, rotate_flags
from scp.catalog import load_catalog, number
from scp.registration import apply_registration
from scp.subject_sources import new_subject_document
from scp_highway.menu import make_icon
from scp_highway.modular_stamp import declaration as stamp_declaration
from scp_highway.modular_ramps import module_catalog, procedural_geometry
from register_highway_pieces import _allocation, GAME_KEYS

STAMP = 'ddrhw-modular-highway-stamp'
ASSEMBLY = 'ddrhw-l1-and-l2-diagonal-avenue-modular-diamond'


def _free_block(ledger, count=1):
    used = {number(value) & 0xfffff000 for row in ledger['pieces'].values()
            for value in [row['preview_id'], *row['tile_ids'], *row.get('resource_blocks', []),
                          *row.get('adaptive_tile_ids', []), *row.get('extra_model_ids', [])]}
    return next(value for value in range(0x7f500000, 0x7f600000-count*0x1000+1, 0x1000)
                if all(value+n*0x1000 not in used for n in range(count)))


def _marker(avenue, occupied):
    # Use actual Street marker edge vocabulary (0, 2, 4), not invented byte
    # values. All rotated Street/Avenue pairs are distinct and retained.
    for values in itertools.chain(itertools.product((2,4),repeat=4), itertools.product((0,2,4),repeat=4)):
        if 4 not in values or 2 not in values:
            continue
        street = sum(value << (8*axis) for axis,value in enumerate(values))
        pairs = {(rotate_flags(street,t),rotate_flags(avenue,t)) for t in range(4)}
        if len(pairs) == 4 and not pairs & occupied:
            occupied.update(pairs)
            return f'{street:08x}'
    raise ValueError('No independent Street/Avenue marker pattern remains')


def register(root=ROOT):
    root = Path(root).resolve(); catalog=load_catalog(root); ledger=deepcopy(catalog['_allocations'])
    existing={p['id']:p for p in catalog['pieces']}; occupied=set(expected_solutions(catalog['pieces']))
    declarations=[stamp_declaration(),*module_catalog()['types']]
    additions=[]; members=[]; identities={}
    tiles=procedural_geometry()[1]
    for d in declarations:
        key=d['key'];identifier=STAMP if key=='modular-stamp' else 'ddrhw-modular-'+key
        identities[key]=identifier;members.append(identifier)
        if identifier in existing:
            if existing[identifier]['cells'] != d['cells'] or existing[identifier]['recipe'] != d['recipe']:
                raise ValueError('Registered modular identity differs from its reviewed footprint')
            continue
        puzzle,_unused,_tiles=_allocation(ledger,d['cells'])
        origin=d['world_origin_cell']
        has_adaptive=any(c[0]+origin[0]-c[1]-origin[1] in (-1,0,1) for c in d['cells'])
        block=_free_block(ledger,2 if has_adaptive else 1)
        tile_ids=[f'{block+x*0x100+y*0x10:08x}' for x,y in d['cells']]
        name=('DD RHW-4 — Diagonal Highway and Slip-Lane Stamp' if key=='modular-stamp'
              else 'RHW Ramp — '+d['name'])
        description=('Place the complete double-decker highway and four slip-lane openings in one click. '
          'On-ramps, off-ramps, and Avenue terminals are separate pieces attached at measured sloped boundaries.'
          if key=='modular-stamp' else 'Independently placed '+d['name'].lower()+'. '
          'Use its complete connection cards; it attaches outside the highway stamp and owns no highway tiles.')
        piece={'schema_version':1,'id':identifier,'domain':'highway','name':name,'description':description,
            'recipe':d['recipe'],'geometry_key':key,'enabled_by_default':False,'status':'experimental',
            'puzzle_id':f'{puzzle:04x}','tile_ids':tile_ids,'preview_id':f'{block+0xff5:08x}',
            'effect_name':f'preview_scp_hw_{puzzle:04x}'.ljust(24,'_')+'001',
            'footprint':d['footprint'],'cells':d['cells'],'orientation_count':8,
            'dependencies':['controller','dd_rhw','rhw_core','mis'],
            'menu':{'id':f'{0x6a470000|puzzle:08x}','order':f'{0xffffff00|(puzzle&0xff):08x}','style':'ddrhw-ramp'},
            'engineering':d['engineering'],'shadow_mode':'generated',
            'shadow_mappings':[{'tile':t,'source':t,'rotation':0} for t in tile_ids],
            'provenance':{'geometry':'Retained measured highway sockets and separately attached R40 continuations.',
                          'construction':'Disjoint sparse ownership; four proper rotations repeated; no reflected traffic.',
                          'redistribution':'permission-pending'},
            'game_tests':{key:'unverified' for key in GAME_KEYS}}
        record={'puzzle_id':piece['puzzle_id'],'tile_ids':tile_ids,'preview_id':piece['preview_id'],
          'menu_id':piece['menu']['id'],'state':'reserved-locally','cells':piece['cells'],
          'tile_base':f'{block:08x}','resource_blocks':[f'{block:08x}']}
        ledger['pieces'][identifier]=record
        origin=d['world_origin_cell'];adaptive=[]
        for cell in d['cells']:
            world=(cell[0]+origin[0],cell[1]+origin[1]);diff=world[0]-world[1]
            if diff not in (-1,0,1):continue
            avenue={0:0x01030103,1:0x01000003,-1:0x00030100}[diff]
            adaptive.append({'cell':cell,'rotation':2 if diff==1 else 0,
                'texture_donor_id':f'{0x04003800 if diff==0 else 0x04000200:08x}',
                'street_flags':_marker(avenue,occupied),'avenue_flags':f'{avenue:08x}',
                'prop':sum(world) in (0,1) if key=='modular-stamp' else bool(tiles.get(world))})
        if adaptive:
            active_block=block+0x1000
            record['resource_blocks'].append(f'{active_block:08x}')
            for n,row in enumerate(adaptive):row['resolved_tile_id']=f'{active_block+n*0x100:08x}'
            piece['adaptive_ground']={'schema_version':1,'cells':adaptive}
            piece['dependencies'].append('adaptive_avenue')
            record.update(allocation_fields(piece))
        additions.append(piece)
    old=['ddrhw-diagonal-'+key for key in ['lower-exit-grade','lower-entry-grade','upper-exit-grade','upper-entry-grade','northwest-junction','southeast-junction']]
    selections={'ddrhw-modular-ramp-kit':members+old}
    if additions:
        apply_registration(root,additions,ledger,selections,
            icons={p['id']:make_icon('ddrhw-ramp') for p in additions},domain='highway')
    all_pieces={p['id']:p for p in load_catalog(root)['pieces']}
    placements=[{'instance_id':'P01','label':'P01','piece_id':STAMP,'origin_m':[0.,0.],
      'rotation_degrees_ccw':0,'rotation_degrees':0,'display_origin_tiles_en':[0,9],
      'menu_name':all_pieces[STAMP]['name'],'name':all_pieces[STAMP]['name']+' at P01','recipe':all_pieces[STAMP]['recipe']}]
    for n,d in enumerate(module_catalog()['types'],2):
        identifier=identities[d['key']];p=all_pieces[identifier];x,y=[v+4 for v in d['world_origin_cell']]
        placements.append({'instance_id':f'P{n:02d}','label':f'P{n:02d}','piece_id':identifier,
          'origin_m':[16.*x,-16.*y],'rotation_degrees_ccw':0,'rotation_degrees':0,
          'display_origin_tiles_en':[x,9-y],'name':p['name']+f' at P{n:02d}','menu_name':p['name'],'recipe':p['recipe']})
    scene={'id':ASSEMBLY,'title':'DD RHW-4 — Modular Diagonal Avenue Diamond',
      'purpose':'One highway/slip-lane stamp with four separately attached ramps and two independently placed Avenue terminals.',
      'geometry_status':'Compiled experimental modules; see TESTING.md for exact software and game evidence.',
      'coordinate_units':'metres east,north,height; rotations counterclockwise',
      'coordinate_system':{'origin_world_m':[0.,-144.],'origin_name':'southwest tile-centre reference',
        'tile_size_m':16,'tile_boundaries_offset_m':8,'axes':['east','north','height']},
      'construction_rectangle_tiles':[10,10],'occupied_tiles':62,'module_placements':7,
      'component_types_used':7,'separately_available_component_types':13,
      'traffic_policy':{'ramp_access':'adjacent-carriageway right turns only',
        'required_movements':['SW->NE','NE->SW','NW->SE','SE->NW','NE->NW','NW->SW','SW->SE','SE->NE'],
        'forbidden_cross_avenue_turns':['NE->SE','SE->SW','SW->NW','NW->NE']},
      'placements':placements,'game_tests':{key:'unverified' for key in GAME_KEYS}}
    target=root/'domains/highway/01_assemblies'/ASSEMBLY;target.mkdir(parents=True,exist_ok=True)
    if not (target/'assembly.jsonc').exists():
        (target/'assembly.jsonc').write_text(new_subject_document(scene,'assembly'))
        from scp.content import assembly_document_scaffold
        for name,text in assembly_document_scaffold(scene).items():
            (target/name).write_text(text)
    reg_path=root/'domains/highway/domain.jsonc';registry=jsonc.load(reg_path);rel=f'01_assemblies/{ASSEMBLY}/assembly.jsonc'
    if rel not in registry['assemblies']:
        registry['assemblies'].append(rel);reg_path.write_text(jsonc.document(registry,source=reg_path.read_text()))
    return {'new_types':len(additions),'default_placements':len(placements),'kit_members':members+old,'assembly':ASSEMBLY}

if __name__=='__main__':
    print(json.dumps(register(),indent=2))
