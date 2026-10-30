"""Highway service roles and intrinsic extraction through the shared engine.

Car and pedestrian engine classes are explicit. Heights annotate the audited
DD RHW-4 and Avenue variants; they do not change engine transport or establish
neighbour compatibility. Only the pure crossing currently has an independently
reviewed complete literal port/movement contract.
"""
from __future__ import annotations

from collections import Counter,defaultdict
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

from scp import jsonc
from scp.catalog import load_catalog,safe_relative
from scp.connectivity import piece_connectivity,orientation_states_from_rules
from scp.content import fingerprint,refresh_catalog_content
from scp.dbpf import require
from scp.subject_sources import source_path
from scp.verify import parse_rules,strict_dbpf,verify_build

CORE = 'highway_ddrhw_diagonal_avenue_crossing'


@lru_cache(maxsize=1)
def _core_contract():
    # These independently transcribed route measurements belong to the native
    # verifier. The resource writer and its native donor parser are not used.
    from .verify import expected_paths,CELLS
    routes = []
    for cell,records in zip(CELLS,expected_paths()):
        for route in records:
            points = [tuple(round(value,6) for value in
                      (p[0]+16*cell[0],p[1]-16*cell[1],p[2])) for p in route['points']]
            routes.append({**route,'points':points})
    starts,ends = defaultdict(list),defaultdict(list)
    for index,route in enumerate(routes):
        starts[route['transport'],route['points'][0]].append(index)
        ends[route['transport'],route['points'][-1]].append(index)
    incoming = sorted(starts.keys()-ends.keys())
    require(len(incoming) == 10,'Independent native crossing contract needs ten incoming lanes')
    result = {'ports':{},'port_vectors':{},'port_transports':{},'port_directions':{},
              'movements':[],'_channels':[]}
    counters = Counter()
    for engine,point in incoming:
        family = ('avenue-walkway' if engine == 2 else 'upper-lane' if point[2] == 15.0
                  else 'lower-lane' if point[2] == 7.5 else 'avenue-lane')
        counters[family] += 1
        channel = f'{family}-{counters[family]:02d}'
        index,seen = starts[engine,point][0],set()
        first = routes[index]
        while True:
            require(index not in seen,'Independent crossing contract contains a route loop')
            seen.add(index)
            last = routes[index]
            end = engine,last['points'][-1]
            if end not in starts:
                break
            require(len(starts[end]) == 1,'Independent native crossing boundary is ambiguous')
            index = starts[end][0]
        require(len(seen) == 3,'Independent crossing channel must traverse three source cells')
        entry,exit_ = channel+'-a',channel+'-b'
        for name,direction,route,position in ((entry,'in',first,0),(exit_,'out',last,-1)):
            result['ports'][name] = list(route['points'][position])
            delta = [b-a for a,b in zip(route['points'][0],route['points'][-1])]
            length = math.hypot(*delta[:2])
            result['port_vectors'][name] = [value/length for value in delta[:2]]
            result['port_transports'][name] = engine
            result['port_directions'][name] = direction
        result['movements'].append([entry,exit_])
        component = ('avenue-walkways' if engine == 2 else 'upper-mainline' if point[2] == 15.0
                     else 'lower-mainline' if point[2] == 7.5 else 'avenue-mainline')
        result['_channels'].append({'id':channel,'component_id':component,
            'kind':'walkway' if engine == 2 else 'road-lane',
            'traffic_modes':['pedestrian'] if engine == 2 else ['car'],
            'entry_port':entry,'exit_port':exit_})
    return result


def reviewed_contract(piece):
    """Return independent literal crossing facts, never generated ramp poses."""
    if piece['recipe'] == CORE:
        from copy import deepcopy
        return deepcopy(_core_contract())
    # Sampled ramp endpoints are measured by extraction. Their complete native
    # boundary/channel contract remains explicitly unreviewed at this stage.
    return None


def service_classifier(piece,engine_transport,height):
    if engine_transport == 1:
        if abs(height) <= 2e-5:
            variant = 'avenue-ground'
        elif abs(height-7.5) <= 2e-5:
            variant = 'dd-rhw-l1'
        elif abs(height-15.0) <= 2e-5:
            variant = 'dd-rhw-l2'
        else:
            variant = 'access-ramp'
        return {'service_network':'road','service_family':'road','variant':variant,'role':'primary',
                'channel_kind':'road-lane','traffic_modes':['car'],
                'classification_status':'Registered highway domain: actual car engine 1; audited ground/DD heights annotate the variant, and intermediate heights are access-ramp.'}
    if engine_transport == 2:
        return {'service_network':'pedestrian','service_family':'pedestrian',
                'variant':'avenue-sidewalk' if abs(height) <= 2e-5 else 'unreviewed-elevated-walkway',
                'role':'primary','channel_kind':'walkway','traffic_modes':['pedestrian'],
                'classification_status':'Actual pedestrian engine 2; no car channel is inferred from coincident coordinates.'}
    return {'service_network':f'unresolved-engine-{engine_transport}','service_family':None,
            'variant':None,'role':'unresolved','classification_status':'requires_explicit_highway_domain_review'}


def materialize(root,*,build,piece_ids=None,include_assemblies=False):
    """Verify one saved build, extract intrinsically, and refresh exact subjects."""
    root,build = Path(root).resolve(),Path(build).resolve()
    require(build.is_relative_to(root),'Highway extraction build must be inside the selected library')
    catalog = load_catalog(root)
    known = {p['id']:p for p in catalog['pieces'] if p['domain'] == 'highway' and p['status'] != 'draft'}
    manifest = jsonc.load(build/'manifest.json')
    built = {p['id']:p for p in manifest['pieces']}
    if piece_ids is None:
        selected = sorted(known.keys() & built.keys())
    else:
        require(not isinstance(piece_ids,(str,bytes)),'Highway extraction IDs must be an iterable of exact identifiers')
        selected = list(piece_ids)
        require(selected and len(selected) == len(set(selected)) and set(selected) <= known.keys() & built.keys(),
                'Highway extraction contains empty, duplicate, draft, unknown, or unbuilt piece IDs')
    require(selected,'Saved build contains no selected implemented highway pieces')
    verify_build(build,write_report=False)
    overlay = manifest.get('overlay',{}).get('rul0',{})
    require(overlay.get('suffix'),'Highway extraction requires actual saved construction rules')
    rings,sections = parse_rules(overlay.get('ordering_insertion','')+overlay['suffix'])
    records = {}
    for identifier in selected:
        piece,item = known[identifier],built[identifier]
        comparable = lambda p:{key:value for key,value in p.items() if key not in {'asset_file','purpose','design_review'}}
        require(comparable(piece) == comparable(item),identifier+': saved highway definition differs from current source')
        archive = safe_relative(build,item['asset_file'])
        resources = strict_dbpf(archive.read_bytes())
        record = piece_connectivity(piece,resources,contract=reviewed_contract(piece),service_classifier=service_classifier)
        puzzle = int(piece['puzzle_id'],16)
        construction = {'rotation_ring':next((ring for ring in rings if ring[0] == puzzle),[]),
                        'rotation_ring_section':'Ordering',
                        'sections':{f'{key:08x}':sections[key] for key in
                            (puzzle+slot*0x10000 for slot in range(8)) if key in sections}}
        record['supported_orientations'] = orientation_states_from_rules(construction,piece['puzzle_id'])
        key = 'construction:'+identifier
        record['source']['resource_fingerprints'][key] = fingerprint(construction)
        record['source']['construction_basis'] = 'Actual emitted per-piece rule sections from the independently verified saved build'
        for port in record['ports']:
            port['resource_keys'].append(key)
        records[identifier] = record
    result = refresh_catalog_content(root,records=records,changed_piece_ids=frozenset(records),
                                     scope_to_changed=not include_assemblies)
    return {**result,'extracted_piece_ids':selected,'saved_build_verified':True,
            'counterpart_matching_performed':False,'manual_game_results_changed':False}


def write_core_groups(root,piece_id):
    """Author the pure crossing's ten measured physical channel associations."""
    root = Path(root).resolve()
    catalog = load_catalog(root)
    pieces = {p['id']:p for p in catalog['pieces']}
    require(piece_id in pieces and pieces[piece_id]['recipe'] == CORE,'Connector declarations are supported only for the independently verified pure native crossing')
    piece = pieces[piece_id]
    directory = root/catalog['domains']['highway']['path']/'00_pieces'/piece_id
    connections = jsonc.load(directory/'connections.json')
    contract = _core_contract()
    ports = {p['id']:p for p in connections['ports']}
    require(set(ports) == set(contract['ports']),'Pure crossing measured ports differ from the independent literal contract')
    for name,port in ports.items():
        require(port['engine_transport'] == contract['port_transports'][name]
                and port['direction'] == contract['port_directions'][name]
                and math.dist(port['endpoint_m'],contract['ports'][name]) <= 2e-5,
                'Pure crossing measured endpoint differs from literal native evidence')
    require({(j['entry_port'],j['exit_port']) for j in connections['journeys']}
            == set(map(tuple,contract['movements'])),'Pure crossing channel journeys differ from independent literal evidence')
    components = [{'id':name,'network':'pedestrian' if name == 'avenue-walkways' else 'road',
                   'construction_network':'avenue' if name.startswith('avenue') else 'dirtroad'}
                  for name in ('upper-mainline','lower-mainline','avenue-mainline','avenue-walkways')]
    channels,port_channel = [],{}
    for channel in contract['_channels']:
        channels.append({key:value for key,value in channel.items() if key not in {'entry_port','exit_port'}})
        for name in (channel['entry_port'],channel['exit_port']):
            port_channel[name] = channel
    boundaries = defaultdict(lambda:defaultdict(list))
    for name,port in sorted(ports.items()):
        require(len(port['boundary_sources']) == 1,'Crossing port has an ambiguous physical source boundary')
        source = port['boundary_sources'][0]
        boundaries[tuple(source['cell']),source['edge']][port_channel[name]['component_id']].append(name)
    groups,bundles = [],[]
    for number,((cell,edge),parts) in enumerate(sorted(boundaries.items()),1):
        bundle = {'id':f'boundary-{number:02d}','source_cell':list(cell),
                  'edge':('west','north','east','south')[edge],'connector_ids':[]}
        for component,names in sorted(parts.items()):
            group = {'id':f'boundary-{number:02d}-{component}','component_id':component,'members':[]}
            for name in names:
                port,channel = ports[name],port_channel[name]
                group['members'].append({'id':name+'-member','source_port_id':name,
                    'direction':port['direction'],'channel_id':channel['id'],'cut_id':name+'-cut'})
            groups.append(group)
            bundle['connector_ids'].append(group['id'])
        bundles.append(bundle)
    value = {'schema_version':3,'purpose':'Explicit native highway, Avenue car, and Avenue pedestrian channels with complete exposed source-cell boundary bundles; no neighbouring compatibility or game result is implied.',
             'piece_id':piece_id,'source_binding':{
                 'piece_sha256':hashlib.sha256(source_path(directory,'piece').read_bytes()).hexdigest(),
                 'connections_sha256':hashlib.sha256((directory/'connections.json').read_bytes()).hexdigest()},
             'components':components,'channels':channels,'groups':groups,'boundary_bundles':bundles}
    from scp.connector_metadata import validate_piece
    validate_piece(piece,connections,value,{})
    path = directory/'connector-groups.jsonc'
    header = ('// title: "Native diagonal highway crossing connector channels"\n'
              '// summary: "Bind twenty measured directional endpoints to ten independently reviewed native physical channels."\n//\n'
              '// Used when: Contributors export or inspect this pure native crossing’s complete physical boundaries.\n'
              '// Read by: scp.connector_metadata.load_library(), connector exports, and source-owned overview rendering.\n'
              '// Updated by: scp_highway.connections.write_core_groups() after independent saved-resource extraction and literal-port checks.\n'
              '// Affects: Explicit upper/lower highway lanes, Avenue lanes, pedestrian channels, complete boundary bundles, and derived connector exports.\n'
              '// Reference: custom-pieces/docs/CONNECTOR_METADATA.md.\n')
    source = path.read_text(encoding='utf-8') if path.is_file() else header+'{}\n'
    path.write_text(jsonc.document(value,source=source),encoding='utf-8')
    return {'piece_id':piece_id,'physical_channels':len(channels),'directional_members':len(ports),
            'boundary_bundles':len(bundles),'path':path.relative_to(root).as_posix()}


def main():
    import argparse
    from scp.paths import project_root
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=project_root())
    parser.add_argument('--build',type=Path,required=True)
    parser.add_argument('--piece',action='append',dest='piece_ids')
    parser.add_argument('--include-assemblies',action='store_true')
    args = parser.parse_args()
    print(json.dumps(materialize(args.root,build=args.build,piece_ids=args.piece_ids,
                                include_assemblies=args.include_assemblies),indent=2))


if __name__ == '__main__':
    main()
