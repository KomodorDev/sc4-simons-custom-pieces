"""Highway service roles and intrinsic extraction through the shared engine.

Car, pedestrian, and reviewed GHSR engine classes are explicit. Heights
annotate the audited variants; they do not change engine transport or establish
neighbour compatibility. Frozen accepted-resource contracts cover native
crossings, compact components, and separately placed highway modules.
"""
from __future__ import annotations

from collections import Counter,defaultdict
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

from scp import jsonc,piece_menu_families
from scp.build import RUL0
from scp.catalog import load_catalog,safe_relative
from scp.connectivity import piece_connectivity,orientation_states_from_rules
from scp.content import fingerprint,refresh_catalog_content
from scp.dbpf import require
from scp.subject_sources import source_path
from scp.verify import parse_rules,strict_dbpf,verify_build

CORE = 'highway_ddrhw_diagonal_avenue_crossing'
GHSR_RECIPES = ('highway_ddrhw_diagonal_ghsr_crossing',
                'highway_ddrhw_diagonal_ghsr_crossing_alignment_b')
ORTHOGONAL_TRANSITION = 'highway_ddrhw_orthogonal_l0_transition'


def connector_source_files(piece_id):
    """Bind accepted numeric measurement sources used by this piece's adapter."""
    if piece_id == 'ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile':
        from .orthogonal_transition_contracts import REFERENCE
        return [REFERENCE] if (Path(__file__).resolve().parents[4] / REFERENCE).is_file() else []
    if piece_id in ('ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg',
                    'ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b'):
        from .ghsr_crossing_verify import connector_source_files as sources
        return sources(piece_id)
    if piece_id.startswith('ddrhw-parallel-b-'):
        from .parallel_b_connector_contracts import REFERENCE
        return [REFERENCE] if (Path(__file__).resolve().parents[4] / REFERENCE).is_file() else []
    if piece_id.startswith('ddrhw-parallel-'):
        from .parallel_connector_contracts import REFERENCE
        return [REFERENCE]
    return []


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
    """Return reviewed intrinsic facts, never candidate-generated ramp poses."""
    if piece['recipe'] == ORTHOGONAL_TRANSITION:
        from .orthogonal_transition_verify import reviewed_contract as transition_contract
        return transition_contract(piece)
    if piece['recipe'] in GHSR_RECIPES:
        from .ghsr_crossing_verify import reviewed_contract as crossing_contract
        return crossing_contract(piece)
    if piece['recipe'] == CORE:
        from copy import deepcopy
        return deepcopy(_core_contract())
    facts = _reviewed_facts(piece)
    if facts is None:
        return None
    return {**({'boundary_measurement_precision': 'saved-path'}
               if piece['recipe'].startswith('highway_ddrhw_parallel_b_') else {}),
            'ports':{p['id']:list(p['endpoint_m']) for p in facts['ports']},
            'port_vectors':{p['id']:list(p.get('tangent',p['sampled_tangent'])) for p in facts['ports']},
            'port_transports':{p['id']:p['engine_transport'] for p in facts['ports']},
            'port_directions':{p['id']:p['direction'] for p in facts['ports']},
            'movements':[list(pair) for pair in facts['movements']]}


def reviewed_path_ports(piece):
    """Return the complete reviewed saved-PATH boundary for model/path checks.

    These are traffic cuts at owned city-tile edges, rather than physical
    pavement sockets. In particular, a lower full visual ramp has four cuts
    and two intrinsic route fragments. Use the measured first/last chord here;
    an independently declared analytic card tangent remains a separate fact.
    """
    facts = _reviewed_facts(piece)
    require(facts is not None,piece['id']+': no complete reviewed highway boundary contract')
    return [{'direction':p['direction'],'transport':p['engine_transport'],
             'point_m':list(p['endpoint_m']),'tangent':list(p['sampled_tangent']),
             'grade':p['grade'],'source_cell':list(p['source_cell']),'edge':p['edge']}
            for p in facts['ports']]


def _reviewed_facts(piece):
    if piece['recipe'] == ORTHOGONAL_TRANSITION:
        from .orthogonal_transition_contracts import load_contract
        from .orthogonal_transition_verify import reviewed_facts
        return load_contract(piece) or reviewed_facts(piece)
    if piece['recipe'].startswith('highway_ddrhw_parallel_b_'):
        from .parallel_b_connector_contracts import load_contracts
        from .parallel_alignment_b_verify import reviewed_facts
        facts = load_contracts().get(piece['recipe']) or reviewed_facts(piece)
        require(piece['footprint'] == facts['footprint']
                and sorted(map(tuple, piece['cells'])) == sorted(map(tuple, facts['cells'])),
                piece['id'] + ': owned cells differ from the reviewed Alignment B contract')
        return facts
    if piece['recipe'] in GHSR_RECIPES:
        from .ghsr_crossing_verify import reviewed_facts
        return reviewed_facts(piece)
    from .connector_contracts import CONTRACTS
    from .modular_connector_contracts import CONTRACTS as MODULAR_CONTRACTS
    facts = CONTRACTS.get(piece['recipe']) or MODULAR_CONTRACTS.get(piece['recipe'])
    if facts is None and piece['recipe'].startswith('highway_ddrhw_parallel_'):
        from .parallel_connector_contracts import CONTRACTS as PARALLEL_CONTRACTS
        facts = PARALLEL_CONTRACTS.get(piece['recipe'])
    if facts is not None:
        require(piece['footprint'] == facts['footprint']
                and sorted(map(tuple,piece['cells'])) == sorted(map(tuple,facts['cells'])),
                piece['id']+': owned cells differ from the reviewed highway contract')
    return facts


def validate_connection_record(piece,record):
    """Check saved routing, service, boundary, and nonzero travel-grade facts.

    Endpoint contracts intentionally do not establish physical seam fit. Raw
    canonical PATH hashes bind the complete reviewed source graph, including
    model-only cells, while runtime Avenue aliases remain separate dependencies.
    """
    facts = _reviewed_facts(piece)
    require(facts is not None,piece['id']+': no complete reviewed highway boundary contract')
    if (piece['recipe'].startswith('highway_ddrhw_parallel_b_')
            or piece['recipe'] == ORTHOGONAL_TRANSITION):
        require(len(facts.get('path_hashes_by_cell', [])) == len(piece['cells'])
                and {tuple(cell) for cell, _digest in facts['path_hashes_by_cell']}
                    == set(map(tuple, piece['cells'])),
                ('Alignment B strict extraction requires independently checked saved PATH fingerprints; run freeze_parallel_b_connectors.py after native package and assembly verification'
                 if piece['recipe'].startswith('highway_ddrhw_parallel_b_') else
                 'Orthogonal transition strict extraction requires independently checked saved PATH fingerprints; run freeze_orthogonal_transition_connectors.py after native verification'))
    require(record['subject_id'] == piece['id'] and record['subject_kind'] == 'piece',
            'Highway connector record belongs to another subject')
    actual = {p['id']:p for p in record['ports']}
    require(len(actual) == len(record['ports']) and set(actual) == {p['id'] for p in facts['ports']},
            'Highway measured ports differ from the complete reviewed contract')
    tiles = {tuple(cell):tile for cell,tile in zip(piece['cells'],piece['tile_ids'])}
    fingerprints = record['source']['resource_fingerprints']
    for cell,expected in facts['path_hashes_by_cell']:
        key = f'path:{piece["id"]}:296678f7-a966883f-{tiles[tuple(cell)]}'
        require(fingerprints.get(key) == expected,'Highway canonical PATH bytes differ from reviewed saved evidence')
    for expected in facts['ports']:
        port = actual[expected['id']]
        for key in ('direction','engine_transport','edge','service_network','service_family',
                    'variant','role','channel_kind','traffic_modes'):
            require(port.get(key) == expected[key],'Highway measured '+key+' differs from reviewed boundary')
        require(math.dist(port['endpoint_m'],expected['endpoint_m']) <= 1e-6,
                'Highway endpoint differs from reviewed saved evidence')
        require(math.dist(port['sampled_tangent'],expected['sampled_tangent']) <= 1e-9
                and math.dist(port['tangent'],expected.get('tangent',expected['sampled_tangent'])) <= 1e-9,
                'Highway travel tangent differs from reviewed saved evidence')
        require(abs(port['grade']-expected['grade']) <= 1e-9,
                'Highway signed travel grade differs from reviewed saved evidence')
        require(port['boundary_sources'] == [{'cell':expected['source_cell'],
                    'edge':expected['edge'],'tile_id':tiles[tuple(expected['source_cell'])]}],
                'Highway source boundary differs from reviewed saved evidence')
    require(len(record['journeys']) == len(facts['movements'])
            and {(j['entry_port'],j['exit_port']) for j in record['journeys']} == set(facts['movements']),
            'Highway directed journeys differ from reviewed saved evidence')
    require(len(record['forbidden_transfers']) == len(facts['forbidden_transfers'])
            and {(p['from_port'],p['to_port']) for p in record['forbidden_transfers']}
                == set(facts['forbidden_transfers']),
            'Highway forbidden transfers differ from reviewed saved evidence')
    return facts


def service_classifier(piece,engine_transport,height):
    if piece['recipe'] in GHSR_RECIPES and engine_transport == 7:
        require(abs(height - 1.) <= 2e-5, 'Reviewed crossing GHSR service must remain at 1 m')
        return {'service_network':'ghsr','service_family':'high-speed-rail','variant':'ghsr',
                'role':'primary','channel_kind':'rail-track','traffic_modes':['monorail'],
                'classification_status':'Explicitly reviewed native ground HSR engine 7 at 1 m; ordinary railway service is separate.'}
    if engine_transport == 1:
        if abs(height) <= 2e-5:
            variant = 'rhw-4-l0' if piece['recipe'] == ORTHOGONAL_TRANSITION else 'avenue-ground'
        elif abs(height-7.5) <= 2e-5:
            variant = 'dd-rhw-l1'
        elif abs(height-15.0) <= 2e-5:
            variant = 'dd-rhw-l2'
        else:
            variant = 'dd-rhw-ground-transition' if piece['recipe'] == ORTHOGONAL_TRANSITION else 'access-ramp'
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
    controller = strict_dbpf(safe_relative(build,
        manifest['plugin_folder']+'/00_SCP_Controller_NAM50.dat').read_bytes())
    _plain,overlay,_family_report = piece_menu_families.verify(
        controller[RUL0],overlay,manifest['pieces'],manifest.get(piece_menu_families.KEY))
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
        runtime_keys = []
        if piece.get('adaptive_ground'):
            from scp.adaptive_network import bindings, resource_keys, solution_rows, BEGIN, END
            from scp.content import resource_fingerprints
            targets = {int(row['resolved_tile_id'],16) for row in bindings(piece)}
            insertion = manifest['overlay']['rul1']['insertion']
            active = '\n'.join(line for line in insertion.splitlines()
                               if line.strip() not in {BEGIN,END} and line.strip())
            construction['adaptive_rul1_solutions'] = [list(row) for row in solution_rows(active.encode('ascii'))
                                                      if row[2] in targets]
            construction['adaptive_bindings'] = piece['adaptive_ground']
            runtime_keys = list(resource_fingerprints(identifier,{
                key:resources[key] for key in resource_keys(piece) if key[0] != 0x7AB50E44}))
        record['supported_orientations'] = orientation_states_from_rules(construction,piece['puzzle_id'])
        key = 'construction:'+identifier
        record['source']['resource_fingerprints'][key] = fingerprint(construction)
        record['source']['construction_basis'] = 'Actual emitted per-piece rule sections from the independently verified saved build'
        for port in record['ports']:
            port['resource_keys'].append(key)
            port['resource_keys'].extend(name for name in runtime_keys if name not in port['resource_keys'])
        if _reviewed_facts(piece) is not None:
            validate_connection_record(piece,record)
        records[identifier] = record
    result = refresh_catalog_content(root,records=records,changed_piece_ids=frozenset(records),
                                     scope_to_changed=not include_assemblies)
    return {**result,'extracted_piece_ids':selected,'saved_build_verified':True,
            'counterpart_matching_performed':False,'manual_game_results_changed':False}


def connector_groups_value(piece,connections,*,piece_sha256,connections_sha256):
    """Author existing shared-schema groups from independently frozen channels.

    A boundary bundle is one occupied tile side. Multiple services or endpoint
    heights on that side remain separate cards; a shared component establishes
    intrinsic journey membership, never a new traffic movement.
    """
    from copy import deepcopy
    from scp.connector_metadata import validate_piece
    facts = validate_connection_record(piece,connections)
    channels = {c['id']:c for c in facts['channels']}
    boundaries = defaultdict(lambda:defaultdict(list))
    for port in facts['ports']:
        channel = channels[port['channel_id']]
        boundaries[tuple(port['source_cell']),port['edge']][
            channel['component_id'],port['endpoint_m'][2]].append(port)
    groups,bundles = [],[]
    for number,((cell,edge),services) in enumerate(sorted(boundaries.items()),1):
        bundle = {'id':f'boundary-{number:02d}','source_cell':list(cell),
                  'edge':('west','north','east','south')[edge],'connector_ids':[]}
        for service_number,((component,_height),ports) in enumerate(sorted(services.items()),1):
            group = {'id':f'boundary-{number:02d}-{component}-{service_number:02d}',
                     'component_id':component,'members':[]}
            for port in sorted(ports,key=lambda p:p['id']):
                identifier = port['id'].lower()
                group['members'].append({'id':'member-'+identifier,'source_port_id':port['id'],
                    'direction':port['direction'],'channel_id':port['channel_id'],
                    'cut_id':'cut-'+identifier})
            groups.append(group)
            bundle['connector_ids'].append(group['id'])
        bundles.append(bundle)
    value = {'schema_version':3,
             'purpose':'Complete reviewed saved-PATH service boundaries, signed endpoint grades, and physical channel associations. Physical deck fit, neighbouring compatibility, and game operation remain unverified.',
             'piece_id':piece['id'],'source_binding':{'piece_sha256':piece_sha256,
                'connections_sha256':connections_sha256},
             'components':deepcopy(facts['components']),
             'channels':[{key:deepcopy(value) for key,value in channel.items() if key != 'ports'}
                         for channel in facts['channels']],
             'groups':groups,'boundary_bundles':bundles}
    validate_piece(piece,connections,value,{})
    return value


def write_connector_groups(root,piece_ids):
    """Write only selected source-owned connector declarations after extraction.

    This does not re-extract resources, refresh prose, render cards, build DATs,
    discover compatible neighbours, or change human observations. Run it again
    after an extraction changes a selected connections.json fingerprint.
    """
    root = Path(root).resolve()
    require(not isinstance(piece_ids,(str,bytes)),'Connector IDs must be an iterable of exact identifiers')
    identifiers = list(piece_ids)
    require(identifiers and len(identifiers) == len(set(identifiers)),
            'Connector IDs must be nonempty and unique')
    catalog = load_catalog(root)
    known = {p['id']:p for p in catalog['pieces'] if p['domain'] == 'highway'}
    require(set(identifiers) <= known.keys(),'Unknown selected highway connector subject')
    pending,results = [],[]
    for identifier in identifiers:
        piece = known[identifier]
        require(_reviewed_facts(piece) is not None,'No complete reviewed highway connector contract')
        directory = root/catalog['domains']['highway']['path']/'00_pieces'/identifier
        connections_path = directory/'connections.json'
        connections_bytes = connections_path.read_bytes()
        value = connector_groups_value(piece,jsonc.loads(connections_bytes.decode('utf-8')),
            piece_sha256=hashlib.sha256(source_path(directory,'piece').read_bytes()).hexdigest(),
            connections_sha256=hashlib.sha256(connections_bytes).hexdigest())
        path = directory/'connector-groups.jsonc'
        header = ('// title: "Reviewed highway connector channels"\n'
                  '// summary: "Bind every measured service endpoint to its independently reviewed channel and exposed tile boundary."\n//\n'
                  '// Used when: Contributors export this highway component or inspect its complete boundary cards.\n'
                  '// Read by: scp.connector_metadata.load_library(), connector exports, and source-owned overview rendering.\n'
                  '// Updated by: scp_highway.connections.write_connector_groups() after reviewed saved-resource extraction.\n'
                  '// Affects: Highway, Avenue, ramp, and pedestrian service boundaries, signed slopes, and derived connector exports.\n')
        source = path.read_text(encoding='utf-8') if path.is_file() else header+'{}\n'
        pending.append((path,jsonc.document(value,source=source)))
        results.append({'piece_id':identifier,'physical_channels':len(value['channels']),
                        'directional_members':sum(len(group['members']) for group in value['groups']),
                        'service_groups':len(value['groups']),
                        'boundary_bundles':len(value['boundary_bundles']),
                        'path':path.relative_to(root).as_posix()})
    for path,text in pending:
        path.write_text(text,encoding='utf-8')
    return {'pieces':results,'resource_extraction':False,'manual_game_results_changed':False}


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
