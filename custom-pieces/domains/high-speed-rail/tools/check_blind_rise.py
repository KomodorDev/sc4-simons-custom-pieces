#!/usr/bin/env python3
"""Inspect the saved paired-rise DAT and two saved straight approaches.

This tool reads independent contracts and emitted files only. It imports no
model or route writer. Transforming all real model vertices and PATH points
by the same proper rotation preserves their independently audited distances.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
from copy import deepcopy
from scp.dbpf import entries, decompress, require
from scp.catalog import load_catalog
from scp.models import parse_s3d, positions
from scp.track_paths import S3D, PATH
from scp.verify import parse_paths
from scp_hsr.hsr_components_verify import CONTRACTS, check_paths
from scp_hsr.interchange_verify import _encoded_routes, _graph, _turn
from scp_hsr.directional_t_verify import _journeys, _world_triangles

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'project.json').is_file())
ID = 'blind-hsr-rise-quarter-turn'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def native_hsr_path(build, manifest, explicit=None):
    """Resolve the audited donor without depending on one workstation's settings."""
    profile = load_catalog(ROOT)['_profile']
    expected = profile['files']['hsr']
    require(manifest['profile']['id'] == profile['id'],
            'Build profile differs from the current audited source profile')
    donors = [item for item in manifest['profile']['donors']
              if item['filename'] == expected['filename']]
    require(len(donors) == 1 and donors[0]['sha256'] == expected['sha256'],
            'Build does not identify the pinned native HSR donor')
    if explicit is None:
        audit = build/'input-audit.json'
        require(audit.is_file(), 'Build input audit is unavailable; pass --native-hsr with the pinned donor DAT')
        candidates = [Path(item['path']).expanduser()
                      for item in json.loads(audit.read_text())['donors']
                      if item['filename'] == expected['filename']]
        require(len(candidates) == 1, 'Build input audit does not identify one HSR donor; pass --native-hsr')
        path = candidates[0]
    else:
        path = Path(explicit).expanduser()
    require(path.is_file(), 'Native HSR donor is unavailable; pass --native-hsr with the pinned donor DAT')
    require(sha(path) == expected['sha256'], 'Native HSR donor differs from the pinned audited profile')
    return path


def check(build, native_hsr=None):
    manifest=json.loads((build/'manifest.json').read_text())
    by_id={p['id']:p for p in manifest['pieces']}
    loaded={}
    for slug in (ID,'hsr-component-lower-paired-straight','hsr-component-upper-paired-straight'):
        spec=by_id[slug];path=build/spec['asset_file']
        loaded[slug]=(spec,{k:decompress(v) for k,v in entries(path.read_bytes()).items()})
    piece,resources=loaded[ID]
    paths=check_paths(resources,piece)
    negative_controls=[]
    key=(*PATH,int(piece['tile_ids'][-1],16))
    original=parse_paths(resources[key])['routes']
    for mutation in ('interior-height','reverse-channel','remove-travel-cell'):
        routes=deepcopy(original)
        if mutation=='interior-height':
            point=list(routes[0]['points'][len(routes[0]['points'])//2]);point[2]+=.25
            routes[0]['points'][len(routes[0]['points'])//2]=tuple(point)
        elif mutation=='reverse-channel':
            routes[0]['points'].reverse()
            routes[0]['entry'],routes[0]['exit']=routes[0]['exit'],routes[0]['entry']
        else:
            routes=[]
        lines=['SC4PATHS','1.2',str(len(routes)),'0','0']
        for route in routes:
            lines += [str(route[field]) for field in ('transport','lane','entry','exit','compatibility')]
            lines += [str(len(route['points']))]
            lines += [','.join(format(v,'.12g') for v in p) for p in route['points']]
        raw=('\r\n'.join(lines)+'\r\n').encode('ascii')
        try:
            check_paths({**resources,key:raw},piece)
        except ValueError as error:
            negative_controls.append({'mutation':mutation,'rejected':True,'reason':str(error)})
        else:
            raise ValueError('Actual saved PATH mutation was not rejected: '+mutation)
    records=_encoded_routes(resources,piece,CONTRACTS[piece['recipe']])
    journeys=_journeys(records,CONTRACTS[piece['recipe']])
    # Independent locations in source east/north metres. The upper straight
    # turns clockwise to extend east. All placements own disjoint city cells.
    placements=[(ID,0,(0.,0.)),('hsr-component-lower-paired-straight',0,(0.,-112.)),
                ('hsr-component-upper-paired-straight',3,(112.,0.))]
    occupied=set();combined=[];model_vertices=[];sources=[]
    for slug,turns,anchor in placements:
        spec,data=loaded[slug]
        sources.append({'piece_id':slug,'dat_sha256':sha(build/spec['asset_file']),
                        'rotation_ccw_degrees':90*turns,'anchor_en_m':anchor})
        def place(p):
            q=_turn(p,turns)
            return (q[0]+anchor[0],q[1]+anchor[1],q[2])
        for cell in spec['cells']:
            q=place((16.*cell[0],-16.*cell[1],0.))
            city=(round(q[0]/16.),round(-q[1]/16.))
            if city in occupied:
                raise ValueError('Combined approaches overlap city-cell ownership')
            occupied.add(city)
        for cell,metadata,points in _encoded_routes(data,spec,CONTRACTS[spec['recipe']]):
            q=place((16.*cell[0],-16.*cell[1],0.))
            combined.append(((round(q[0]/16.),round(-q[1]/16.)),metadata,[place(p) for p in points]))
        for tile in spec['tile_ids']:
            raw=data[*S3D,int(tile,16)+4]
            cell=spec['cells'][spec['tile_ids'].index(tile)]
            for block in parse_s3d(raw)['vertices']:
                for east,height,south in positions(block):
                    model_vertices.append(place((east+16.*cell[0],-south-16.*cell[1],height)))
    contract={'ports':{'Lowin':(2.,-120.,15.5),'Lowout':(-2.,-120.,15.5),
                       'Highin':(120.,2.,30.5),'Highout':(120.,-2.,30.5)},
              'movements':[('Lowin','Highout'),('Highin','Lowout')]}
    ports,movements=_graph(combined,contract)
    connected=_journeys(combined,contract)
    rotations=[]
    for turns in range(4):
        rotated_records=[(cell,metadata,[_turn(p,turns) for p in points])
                         for cell,metadata,points in combined]
        rotated_contract={**contract,'ports':{k:_turn(v,turns) for k,v in contract['ports'].items()}}
        _graph(rotated_records,rotated_contract)
        actual=_journeys(rotated_records,rotated_contract)
        transformed_vertices=[_turn(p,turns) for p in model_vertices]
        if any(a[2]!=b[2] for a,b in zip(model_vertices,transformed_vertices)):
            raise ValueError('Proper rotation changed actual model height')
        for move,line in actual.items():
            original=connected[move]
            if line != [_turn(p,turns) for p in original]:
                raise ValueError('Rotation changed saved route continuity')
        rotations.append({'rotation_ccw_degrees':90*turns,'proper_rotation_determinant':1,
                          'complete_journeys':2,'all_saved_model_vertices_transformed':len(transformed_vertices),
                          'model_heights_preserved':True,'exact_route_points_and_heights_preserved':True,
                          'shared_endpoint_and_travel_tangent_checks_passed':True})
    # Tangents across all four joined directed routes are equal in the saved
    # canonical points, including exact 3D height and flat endpoint chords.
    joins=[((2.,-104.,15.5),(0.,1.,0.)),((-2.,-104.,15.5),(0.,-1.,0.)),
           ((104.,-2.,30.5),(1.,0.,0.)),((104.,2.,30.5),(-1.,0.,0.))]
    for point,expected in joins:
        before=[line for _,_,line in combined if line[-1]==point]
        after=[line for _,_,line in combined if line[0]==point]
        if len(before)!=1 or len(after)!=1:
            raise ValueError('Combined paired join is incomplete or ambiguous')
        for a,b in ((before[0][-2],point),(point,after[0][1])):
            delta=[b[k]-a[k] for k in range(3)];norm=math.sqrt(sum(v*v for v in delta))
            if max(abs(delta[k]/norm-expected[k]) for k in range(3))>2e-6:
                raise ValueError('Combined approach tangent or flat grade differs')
    # Confirm measured native L2 offsets from the pinned real donor, rather
    # than deriving them from the new curve writer or its declared profiles.
    donor_path=native_hsr_path(build,manifest,native_hsr)
    donor={k:decompress(v) for k,v in entries(donor_path.read_bytes()).items()}
    native=parse_paths(donor[*PATH,0x5dd31500])['routes']
    donor_endpoints=sorted({tuple(p) for r in native for p in (r['points'][0],r['points'][-1])})
    if donor_endpoints != [(-2.,-8.,15.5),(-2.,8.,15.5),(2.,-8.,15.5),(2.,8.,15.5)]:
        raise ValueError('Pinned native paired HSR offsets or heights changed')
    return {'schema_version':1,'piece_id':ID,'build_manifest_sha256':sha(build/'manifest.json'),
            'sources':sources,'paths':paths,'actual_saved_path_negative_controls':negative_controls,'combined_approach_cells':len(occupied),
            'combined_ports':ports,'combined_movements':movements,'four_directed_joins_checked':len(joins),
            'proper_rotations':rotations,'native_l2_donor_archive_sha256':sha(donor_path),
            'native_l2_donor_path_sha256':hashlib.sha256(donor[*PATH,0x5dd31500]).hexdigest(),
            'native_l2_donor_endpoints_enh_m':donor_endpoints,
            'geometry_scope':'Canonical actual-model rail/bed, wall clearance, collars, and support contact proof is in build verification.json. Proper rigid rotations preserve its distances and heights; no game collision claim.',
            'human_preview_approved':False,'game_operation_verified':False,
            'compatibility_discovery_performed':False}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--native-hsr',type=Path,
                        help='Pinned High Speed Rail.dat; default: the verified build input audit')
    args=parser.parse_args();report=check(args.build,args.native_hsr)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'piece_id':ID,'proper_rotations':4,'complete_journeys':2,
                      'directed_joins':4,'output':str(args.output),'passed':True},indent=2))
if __name__=='__main__':
    main()
