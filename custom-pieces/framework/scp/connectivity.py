"""Extract portable connection facts from actual saved PATH resources.

A matching encoded route endpoint is a candidate physical connection, not a
claim that visible deck/wall seams or game behavior have been reviewed.
Domain adapters provide independently reviewed port names and service roles;
the generic engine never guesses a transport domain from a piece filename.
"""
from __future__ import annotations
from collections import defaultdict
from copy import deepcopy
import math

from .content import fingerprint, resource_fingerprints
from .dbpf import require
from .verify import parse_paths

PATH = (0x296678f7, 0xa966883f)
S3D = (0x5ad0e817, 0xbadb57f1)
EPS = 2e-5
ROTATIONS = (0, 90, 180, 270)


def orientation_states_from_rules(construction, puzzle_id):
    """Resolve emitted clone rules, distinguishing real Transpose variants.

    Repeated CopyFrom sections are aliases, not additional test directions.
    The rule's Rotate count is clockwise; public manual scopes use degrees
    counterclockwise. Transpose is recorded as its construction operation,
    without assuming a player can reflect another, unrelated piece.
    """
    sections = construction.get('sections', {})
    root = int(puzzle_id, 16) if isinstance(puzzle_id, str) else puzzle_id
    resolved = {}
    def resolve(identifier, pending=()):
        require(identifier not in pending, 'Cyclic orientation CopyFrom rule')
        if identifier in resolved:return resolved[identifier]
        key = f'{identifier:08x}'
        require(key in sections, 'Missing orientation construction section '+key)
        fields = dict(sections[key])
        if identifier == root:
            state = (0, False)
        else:
            require('CopyFrom' in fields, 'Orientation clone needs an actual CopyFrom rule')
            rotation, transposed = resolve(int(fields['CopyFrom'], 0), pending+(identifier,))
            if int(fields.get('Transpose', '0'), 0):
                require(int(fields['Transpose'], 0) == 1, 'Unsupported construction Transpose value')
                rotation, transposed = (-rotation) % 360, not transposed
            state = ((rotation-90*int(fields.get('Rotate', '0'), 0)) % 360, transposed)
        resolved[identifier] = state
        return state
    grouped = defaultdict(list)
    for slot in range(8):
        identifier = root+slot*0x10000
        grouped[resolve(identifier)].append(f'{identifier:08x}')
    return [{'rotation_ccw_degrees': angle, 'construction_transposed': transposed,
             'construction_section_ids': grouped[angle, transposed],
             'basis': 'actual emitted CopyFrom/Rotate/Transpose rules'}
            for angle, transposed in sorted(grouped, key=lambda state:(state[1], state[0]))]


def _point(point):
    return tuple(round(float(value), 6) for value in point)


def rotate(point, degrees):
    require(degrees in ROTATIONS, 'Connections use four proper cardinal rotations')
    values = list(point)
    for _ in range(degrees//90):
        values[0], values[1] = -values[1], values[0]
    return values


def _unit(vector):
    length = math.hypot(*vector[:2])
    require(length > 1e-12, 'External route has no horizontal travel tangent')
    return [value/length for value in vector[:2]]


def _cells(piece):
    width, depth = piece['footprint']
    return piece.get('cells', [[x, row] for row in range(depth) for x in range(width)])


def _routes(piece, resources):
    result = []
    cells = _cells(piece)
    require(len(cells) == len(piece['tile_ids']), 'Piece cell/tile counts differ')
    for cell, tile_id in zip(cells, piece['tile_ids']):
        tile = int(tile_id, 16) if isinstance(tile_id, str) else tile_id
        raw = resources[*PATH, tile]
        lines = [line.strip() for line in raw.decode('ascii').splitlines() if line.strip() and not line.lstrip().startswith('--')]
        if len(lines) >= 5 and lines[:2] == ['SC4PATHS', '1.2'] and lines[2:5] == ['0', '0', '0']:
            continue
        parsed = parse_paths(raw)
        for index, route in enumerate(parsed['routes']):
            world = [_point((x+16.*cell[0], north-16.*cell[1], height))
                     for x, north, height in route['points']]
            result.append({'id': f'path-{tile:08x}-route-{index:03d}',
                           'source_route_index': index, 'source_class': route['lane'],
                           'compatibility': route['compatibility'],
                           'engine_transport': route['transport'], 'cell': list(cell),
                           'tile_id': f'{tile:08x}', 'points': world,
                           'entry_edge': route['entry'], 'exit_edge': route['exit']})
    require(result, 'A registered piece has no actual transport routes')
    return result


def _default_service(piece, engine_transport, height):
    return {'service_network': f'unresolved-engine-{engine_transport}', 'variant': None,
            'role': 'unresolved', 'classification_status': 'requires_domain_review'}


def piece_connectivity(piece, resources, *, contract=None, service_classifier=None):
    """Read one actual piece; expose ports and all directed external journeys.

    Port locations are from saved PATH bytes. A reviewed contract supplies
    labels and analytic tangents, and is checked against those actual bytes.
    Uncontracted native-family endpoints remain measured, explicitly named
    facts; their physical profile and compatibility remain unreviewed.
    """
    classify = service_classifier or _default_service
    routes = _routes(piece, resources)
    by_engine = defaultdict(list)
    for route in routes:
        by_engine[route['engine_transport']].append(route)
    ports, journeys, forbidden = [], [], []
    hashes = resource_fingerprints(piece['id'], resources)
    declared = (contract or {}).get('ports', {})
    used_declared = set()
    for engine, records in sorted(by_engine.items()):
        incoming, outgoing = defaultdict(list), defaultdict(list)
        for route in records:
            a, b = route['points'][0], route['points'][-1]
            outgoing[a].append(route); incoming[b].append(route)
        # A boundary can carry both directions at exactly the same XYZ. Keep
        # distinct endpoint geometries instead of reducing its graph degree.
        owned = {tuple(cell) for cell in _cells(piece)}
        # Source-cell rows increase south, unlike north-positive PATH positions.
        cell_steps = ((-1, 0), (0, -1), (1, 0), (0, 1))
        external, route_ends = defaultdict(list), {}
        for route in records:
            for direction, endpoint, edge, segment in (
                ('in', route['points'][0], route['entry_edge'], route['points'][:2]),
                ('out', route['points'][-1], route['exit_edge'], route['points'][-2:]),
            ):
                cell, normal = route['cell'], cell_steps[edge]
                exposed = (cell[0]+normal[0], cell[1]+normal[1]) not in owned
                legacy_end = bool(incoming[endpoint]) != bool(outgoing[endpoint])
                if not exposed and not legacy_end:
                    continue
                delta = [b-a for a, b in zip(*segment)]
                sampled = _unit(delta)
                grade = round(delta[2]/math.hypot(*delta[:2]), 9)
                key = (endpoint, direction, tuple(round(v, 9) for v in sampled), grade)
                external[key].append(route)
                route_ends[route['id'], direction] = key
        require(external, 'Actual route graph has no external connection endpoints')
        local_ports = {}
        for index, key in enumerate(sorted(external), 1):
            point, direction, _, _ = key
            incident = external[key]
            route = incident[0]
            segment = (route['points'][0], route['points'][1]) if direction == 'in' else (route['points'][-2], route['points'][-1])
            delta = [b-a for a, b in zip(*segment)]
            sampled = _unit(delta)
            matches = [name for name, wanted in declared.items() if engine == 7 and math.dist(point, wanted) <= EPS]
            if len(matches) > 1:
                vectors = (contract or {}).get('port_vectors', {})
                matches = [name for name in matches if name in vectors and
                           sum(a*b for a, b in zip(_unit(vectors[name]), sampled)) > .998]
            require(len(matches) <= 1, 'Reviewed contract gives ambiguous external port labels')
            if matches:
                identifier = matches[0]
                require(identifier not in used_declared, 'Reviewed port label merges distinct directional endpoint geometries')
                used_declared.add(identifier)
            else:
                edge = route['entry_edge'] if direction == 'in' else route['exit_edge']
                identifier = f'{engine}-'+('W', 'N', 'E', 'S')[edge]+'-'+direction+'-'+str(index)
            tangent = list((contract or {}).get('port_vectors', {}).get(identifier, sampled))
            service = classify(piece, engine, point[2])
            relevant = []
            for item in incident:
                tile = int(item['tile_id'], 16)
                relevant.extend(key for key in hashes if key.startswith(('model:', 'path:')) and (key.endswith('-'+f'{tile:08x}') or
                                any(key.endswith('-'+f'{tile+zoom:08x}') for zoom in range(5))))
            port = {'id': identifier, 'direction': direction, **service,
                    'engine_transport': engine, 'edge': route['entry_edge'] if direction == 'in' else route['exit_edge'], 'endpoint_m': list(point),
                    'tangent': _unit(tangent), 'sampled_tangent': sampled,
                    'grade': round(delta[2]/math.hypot(*delta[:2]), 9),
                    'lane_spacing_m': None, 'profile': 'unreviewed-physical-profile',
                    'physical_profile_status': 'unreviewed; actual PATH alignment alone does not prove deck/wall fit',
                    'endpoint_basis': 'actual_saved_PATH',
                    'tangent_basis': 'reviewed_contract' if identifier in (contract or {}).get('port_vectors', {}) else 'actual_saved_PATH_sample',
                    'resource_keys': sorted(set(relevant)),
                    'source_route_ids': sorted(item['id'] for item in incident),
                    'boundary_sources': [
                        {'cell': list(cell), 'edge': edge, 'tile_id': tile}
                        for cell, edge, tile in sorted({
                            (tuple(item['cell']), item['entry_edge'] if direction == 'in' else item['exit_edge'], item['tile_id'])
                            for item in incident})]}
            ports.append(port); local_ports[key] = port
        for key, port in local_ports.items():
            point = key[0]
            opposites = [other for other in local_ports.values() if other['direction'] != port['direction']
                         and abs(other['endpoint_m'][2]-point[2]) <= EPS
                         and abs(sum(a*b for a,b in zip(other['tangent'], port['tangent']))+1) < .002]
            normal = [-port['tangent'][1], port['tangent'][0]]
            candidates = []
            for other in opposites:
                delta = [other['endpoint_m'][axis]-point[axis] for axis in (0,1)]
                axis = 0 if port['edge'] in (0, 2) else 1
                same_edge_plane = other['edge'] == port['edge'] and abs(other['endpoint_m'][axis]-point[axis]) < EPS
                spacing = abs(sum(a*b for a,b in zip(delta, normal)))
                if same_edge_plane and .1 < spacing < 8.:
                    candidates.append(spacing)
            if candidates:
                port['lane_spacing_m'] = round(min(candidates), 6)
                port['profile'] = 'paired-directed-route-interface; physical-deck-profile-unreviewed'
            else:
                port['profile'] = 'single-directed-route-interface; physical-deck-profile-unreviewed'
            port['connection_class'] = _connection_class(port)
        actual_movements = set()
        for key, start in local_ports.items():
            if start['direction'] != 'in':
                continue
            pending, seen, reached = list(external[key]), set(), set()
            while pending:
                route = pending.pop()
                if route['id'] in seen:continue
                seen.add(route['id'])
                terminal = route_ends.get((route['id'], 'out'))
                if terminal is not None:
                    finish = local_ports[terminal]
                    if finish['id'] not in reached:
                        reached.add(finish['id'])
                        networks = sorted({start['service_network'], finish['service_network']})
                        service = networks[0] if len(networks) == 1 else '+'.join(networks)
                        role = 'primary' if start['role'] == finish['role'] == 'primary' else start['role']
                        journeys.append({'id': f'{engine}:{start["id"]}>{finish["id"]}',
                            'entry_port': start['id'], 'exit_port': finish['id'],
                            'service_network': service, 'role': role, 'engine_transport_classes': [engine],
                            'endpoint_variants': [start.get('variant'), finish.get('variant')],
                            'basis': 'reachability_in_actual_saved_PATH_graph'})
                        actual_movements.add((start['id'], finish['id']))
                    continue
                endpoint = route['points'][-1]
                following = outgoing[endpoint]
                if len(incoming[endpoint]) > 1 or len(following) > 1:
                    normal = cell_steps[route['exit_edge']]
                    neighbour = (route['cell'][0]+normal[0], route['cell'][1]+normal[1])
                    # Coincident reverse records belong to the opposite flow,
                    # not an inferred U-turn at this internal tile seam.
                    following = [item for item in following if tuple(item['cell']) == neighbour
                                 and item['entry_edge'] == (route['exit_edge']+2) % 4]
                pending.extend(following)
        if engine == 7 and contract and contract.get('movements'):
            require(actual_movements == set(map(tuple, contract['movements'])),
                    f'{piece["id"]}: actual movements differ from reviewed contract')
    if declared:
        require(used_declared == set(declared), f'{piece["id"]}: actual PATH does not expose every reviewed port')
    allowed = {(journey['entry_port'],journey['exit_port']) for journey in journeys}
    forbidden = [{'from_port':a['id'],'to_port':b['id'],'from_service':a['service_network'],
                  'to_service':b['service_network'],'basis':'not reachable in actual saved PATH graph'}
                 for a in ports for b in ports if a['direction']=='in' and b['direction']=='out'
                 and (a['id'],b['id']) not in allowed]
    return {'schema_version': 1, 'purpose': 'Intrinsic ports, service roles, and directed journeys measured from this piece’s saved resources.', 'subject_id': piece['id'], 'subject_kind': 'piece',
            'source': {'basis': 'actual decompressed saved resources',
                       'resource_fingerprints': hashes,
                       'reviewed_contract_available': bool(contract),
                       'scope': 'one piece only; no counterpart catalogue is consulted'},
            'coordinate_units': 'metres east,north,height; canonical orientation 0 degrees',
            'ports': ports, 'journeys': journeys, 'forbidden_transfers': forbidden,
            'compatibility_policy': 'Intrinsic encoded-route facts only; complete shared-boundary agreement, physical seams, and game operation are not evaluated.',
            'software_status': {'path_extraction': 'passed', 'contract_consistency': 'passed' if contract else 'unverified',
                                'physical_seams': 'unverified', 'in_game': 'unverified'}}


def _connection_class(port):
    canonical = []
    for angle in ROTATIONS:
        point, tangent = rotate(port['endpoint_m'], angle), rotate(port['tangent'], angle)
        phase = [round(value % 16., 5) % 16. for value in point[:2]]
        canonical.append({'phase_m': phase, 'travel_tangent': [round(value, 5) for value in tangent]})
    meaning = {'service_network': port['service_network'], 'role': port['role'],
               'engine_transport': port['engine_transport'], 'height_m': port['endpoint_m'][2],
               'lane_spacing_m': port['lane_spacing_m'],
               'canonical_interface': min(canonical, key=lambda item: str(item))}
    return 'path-interface-'+fingerprint(meaning)[:20]


def link_counterparts(records, pieces, *, max_candidates=3):
    """Deprecated, non-authoritative catalogue test-pose suggestions.

    This legacy helper is opt-in and is never part of intrinsic extraction.
    Its selected poses are not complete-boundary compatibility decisions.

    All proposed links match actual direction, service, engine, height and
    heading. They are candidates until independent physical seam review and
    exact in-game observations have been recorded. Sparse occupied masks are
    checked, so a proposed counterpart never occupies an already owned tile.
    """
    require(type(max_candidates) is int and max_candidates > 0, 'Need a positive concrete counterpart limit')
    output = deepcopy(records)
    cells = {identifier: _cells(piece) for identifier,piece in pieces.items()}
    all_ports = [(identifier,port) for identifier,record in records.items() for port in record['ports']]
    for identifier, record in output.items():
        own_cells = {(16.*column, -16.*row) for column,row in cells[identifier]}
        for port in record['ports']:
            matches = []
            for other_id, other in all_ports:
                if (other['direction'] == port['direction'] or other['engine_transport'] != port['engine_transport']
                        or other['service_network'] != port['service_network'] or other['role'] != port['role']
                        or abs(other['endpoint_m'][2]-port['endpoint_m'][2]) > EPS):continue
                if (port['lane_spacing_m'] is None) != (other['lane_spacing_m'] is None):continue
                if port['lane_spacing_m'] is not None and abs(port['lane_spacing_m']-other['lane_spacing_m']) > .02:continue
                for angle in ROTATIONS:
                    tangent = rotate(other['tangent'], angle)
                    if math.dist(tangent, port['tangent']) > .002:continue
                    point = rotate(other['endpoint_m'], angle)
                    offset = [port['endpoint_m'][axis]-point[axis] for axis in (0,1)]
                    if any(abs(value/16.-round(value/16.)) > EPS for value in offset):continue
                    offset = [16.*round(value/16.) for value in offset]
                    posed = {(round(rotate((16.*column,-16.*row),angle)[0]+offset[0],6),
                              round(rotate((16.*column,-16.*row),angle)[1]+offset[1],6))
                             for column,row in cells[other_id]}
                    if own_cells & posed:continue
                    companion_keys = other.get('resource_keys', [])
                    matches.append({'piece_id': other_id, 'port_id': other['id'],
                        'relative_rotation_ccw': angle, 'relative_position_m': offset,
                        'resource_keys': companion_keys,
                        'status': 'candidate; actual PATH endpoints/headings align; physical seam and in-game operation unverified',
                        'endpoint_error_m': math.dist(port['endpoint_m'],[point[0]+offset[0],point[1]+offset[1],point[2]]),
                        'tangent_error': math.dist(tangent,port['tangent'])})
            matches.sort(key=lambda item:(len(cells[item['piece_id']]),item['piece_id'],item['port_id'],item['relative_rotation_ccw']))
            port['candidate_counterpart_count'] = len(matches)
            port['compatible_counterparts'] = matches[:max_candidates]
            port['counterpart_list_scope'] = 'Deprecated, non-authoritative selected test poses; not a complete-boundary compatibility decision.'
    return output


def catalog_connectivity(pieces, resource_loader, *, contract_provider=None, service_classifier=None, max_candidates=None):
    """Extract non-draft subjects independently, without catalogue matching.

    ``max_candidates`` is accepted only for source compatibility with old
    callers; it no longer changes extraction. Call the explicitly deprecated
    ``link_counterparts`` helper separately when inspecting legacy test poses.
    """
    if max_candidates is not None:
        import warnings
        warnings.warn('catalog_connectivity no longer suggests counterpart poses; '
                      'max_candidates is ignored. Use explicit link_counterparts only for legacy inspection.',
                      DeprecationWarning, stacklevel=2)
    pieces = list(pieces)
    require(len({piece['id'] for piece in pieces}) == len(pieces), 'Duplicate piece in connectivity input')
    records = {}
    for piece in pieces:
        if piece.get('status') == 'draft':
            continue
        resources = resource_loader(piece)
        records[piece['id']] = piece_connectivity(piece, resources,
            contract=contract_provider(piece) if contract_provider else None,
            service_classifier=service_classifier)
    return records


_EDGE_NORMALS = ((-1., 0.), (0., 1.), (1., 0.), (0., -1.))
_LEGACY_COUNTERPART_FIELDS = ('compatible_counterparts', 'transposed_compatible_counterparts',
                              'candidate_counterpart_count', 'counterpart_list_scope')


def _port_boundary_sources(port, piece):
    """Resolve a measured port to its actual source cells and encoded edges.

    Fresh intrinsic records carry these facts explicitly. Cached legacy
    records retain their original bytes; their PATH resource references and
    the unchanged tile allocation supply the same source-cell association.
    No suggested counterpart or interface-class membership is consulted.
    """
    cells = _cells(piece)
    tiles = {int(tile, 16) if isinstance(tile, str) else tile: tuple(cell)
             for tile, cell in zip(piece['tile_ids'], cells)}
    sources = port.get('boundary_sources')
    if sources is None:
        sources = []
        prefix = 'path:'+piece['id']+':'
        for key in port.get('resource_keys', []):
            if not key.startswith(prefix):
                continue
            tile = int(key.rsplit('-', 1)[-1], 16)
            require(tile in tiles, 'Assembly port references a PATH tile outside its piece')
            sources.append({'cell': tiles[tile], 'edge': port['edge']})
    owned = {tuple(cell) for cell in cells}
    result = set()
    point = port['endpoint_m']
    for source in sources:
        cell, edge = tuple(source['cell']), source['edge']
        require(cell in owned and type(edge) is int and 0 <= edge < 4,
                'Assembly port has an invalid source cell or edge')
        require(port['edge'] in {item['edge'] for item in sources},
                'Assembly port edge differs from its actual PATH boundary sources')
        normal = _EDGE_NORMALS[edge]
        centre = (16.*cell[0], -16.*cell[1])
        delta = (point[0]-centre[0], point[1]-centre[1])
        require(abs(sum(a*b for a, b in zip(delta, normal))-8.) <= EPS and
                max(map(abs, delta)) <= 8.+EPS,
                'Assembly port is not on its actual source tile edge')
        # An unmatched internal fragment is an intrinsic graph terminal, but
        # cannot attach another piece through an already owned neighbour.
        neighbour = (cell[0]+int(normal[0]), cell[1]-int(normal[1]))
        if neighbour not in owned:
            result.add((cell, edge))
    return sorted(result)


def _same_route_service(first, second):
    """Match measured route classification, plus channel facts when supplied."""
    if not first.get('service_network') or first.get('role') in (None, 'unresolved'):
        return False
    if first['service_network'].startswith('unresolved-'):
        return False
    for key in ('engine_transport', 'service_network', 'service_family', 'role', 'channel_kind'):
        if first.get(key) != second.get(key):
            return False
    modes_a, modes_b = first.get('traffic_modes'), second.get('traffic_modes')
    if (modes_a is None) != (modes_b is None):
        return False
    return modes_a is None or set(modes_a) == set(modes_b)


def _placed_route_join(first, second):
    """Check one directed encoded-route seam at the two saved placements.

    This is deliberately a route-member graph check. It does not infer a
    complete multi-channel boundary, a physical mesh seam, or game operation.
    """
    if first['instance'] == second['instance']:
        return False
    a, b = first['port'], second['port']
    if a['direction'] != 'out' or b['direction'] != 'in' or not _same_route_service(a, b):
        return False
    if _point(a['endpoint_m']) != _point(b['endpoint_m']):
        return False
    if math.dist(_unit(a['tangent']), _unit(b['tangent'])) > EPS or abs(a['grade']-b['grade']) > EPS:
        return False
    for centre_a, edge_a in first['boundaries']:
        normal = _EDGE_NORMALS[edge_a]
        if sum(x*y for x, y in zip(a['tangent'], normal)) <= EPS:
            continue
        neighbour = _point((centre_a[0]+16.*normal[0], centre_a[1]+16.*normal[1]))
        for centre_b, edge_b in second['boundaries']:
            if edge_b != (edge_a+2) % 4 or centre_b != neighbour:
                continue
            if sum(x*y for x, y in zip(b['tangent'], _EDGE_NORMALS[edge_b])) < -EPS:
                return True
    return False


def assembly_connectivity(subject_id, scene, piece_records, pieces):
    """Compose saved intrinsic graphs using directly checked placed seams.

    Distinct instance/port nodes prevent coincident endpoints from inventing
    transfers. Inter-piece edges use only actual placed measurements, never
    a catalogue shortlist, a candidate count, or registration order. Legacy
    inputs need no rewrite and the resulting evidence is explicitly limited
    to the encoded-route graph; complete boundary compatibility is separate.
    """
    placements = scene.get('placements', scene.get('instances', []))
    require(placements, 'An assembly needs actual registered placements')
    graph, nodes, positions = defaultdict(set), {}, defaultdict(list)
    resource_hashes, poses, occupied = {}, [], {}
    lattice_origin = None
    for index, placement in enumerate(placements):
        identifier = placement['piece_id']
        require(identifier in piece_records and identifier in pieces, 'Assembly placement has no measured piece record')
        record, spec = piece_records[identifier], pieces[identifier]
        require(record.get('subject_id') == identifier, 'Assembly measurement belongs to another piece')
        angle = placement.get('rotation_degrees_ccw', placement.get('rotation_ccw_degrees', 0))
        origin = placement.get('origin_m', [0., 0.])
        require(not isinstance(angle, bool) and angle in ROTATIONS and len(origin) == 2 and
                all(isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
                    for value in origin), 'Assembly pose must be a finite proper cardinal rotation')
        angle = int(angle)
        if lattice_origin is None:
            lattice_origin = origin
        require(all(abs((origin[axis]-lattice_origin[axis])/16.-round((origin[axis]-lattice_origin[axis])/16.)) <= EPS
                    for axis in (0, 1)), 'Assembly placements do not share the same city-tile lattice')
        for column, row in _cells(spec):
            local = rotate((16.*column, -16.*row), angle)
            cell = _point((local[0]+origin[0], local[1]+origin[1]))
            require(cell not in occupied, 'Assembly placements overlap owned city cells')
            occupied[cell] = index
        local_ports = {}
        for original in record['ports']:
            port = deepcopy(original)
            require(port['id'] not in local_ports, 'Assembly piece repeats a measured port ID')
            require(port['direction'] in ('in', 'out') and len(port['endpoint_m']) == 3 and
                    all(math.isfinite(value) for value in port['endpoint_m']) and
                    len(port['tangent']) == 2 and all(math.isfinite(value) for value in port['tangent']) and
                    math.isfinite(port['grade']), 'Assembly port has invalid measured direction or geometry')
            boundaries = []
            for cell, edge in _port_boundary_sources(original, spec):
                local = rotate((16.*cell[0], -16.*cell[1]), angle)
                centre = _point((local[0]+origin[0], local[1]+origin[1]))
                boundaries.append((centre, (edge-angle//90) % 4))
            point = rotate(port['endpoint_m'], angle)
            port['endpoint_m'] = [point[0]+origin[0], point[1]+origin[1], point[2]]
            port['tangent'] = rotate(port['tangent'], angle)
            if 'sampled_tangent' in port:
                port['sampled_tangent'] = rotate(port['sampled_tangent'], angle)
            port['edge'] = (port['edge']-angle//90) % 4
            for key in _LEGACY_COUNTERPART_FIELDS:
                port.pop(key, None)
            port['source_piece_id'] = identifier
            port['source_port_id'] = original['id']
            port['source_placement'] = placement.get('label', placement.get('name', identifier))
            port['source_origin_m'] = list(origin)
            port['source_rotation_ccw_degrees'] = angle
            key = (index, original['id'])
            local_ports[original['id']] = key
            nodes[key] = {'instance': index, 'port': port, 'boundaries': boundaries}
            positions[(port['engine_transport'], *_point(port['endpoint_m']))].append(key)
        for journey in record['journeys']:
            a, b = local_ports[journey['entry_port']], local_ports[journey['exit_port']]
            require(nodes[a]['port']['direction'] == 'in' and nodes[b]['port']['direction'] == 'out',
                    'Assembly source journey has reversed port directions')
            graph[a].add(b)
        for key, digest in record['source']['resource_fingerprints'].items():
            require(key not in resource_hashes or resource_hashes[key] == digest,
                    'Assembly sources disagree about one saved resource fingerprint')
            resource_hashes[key] = digest
        poses.append({'piece_id': identifier, 'origin_m': list(origin), 'rotation_ccw_degrees': angle})
    candidates, reverse = defaultdict(list), defaultdict(list)
    for colocated in positions.values():
        for first in colocated:
            for second in colocated:
                if _placed_route_join(nodes[first], nodes[second]):
                    candidates[first].append(second)
                    reverse[second].append(first)
    require(all(len(values) == 1 for values in candidates.values()) and
            all(len(values) == 1 for values in reverse.values()),
            'Assembly has an ambiguous placed encoded-route join')
    joined = set()
    joins = []
    for first, values in candidates.items():
        second = values[0]
        graph[first].add(second)
        joined.update((first, second))
        joins.append({'from_piece': nodes[first]['port']['source_piece_id'],
                      'from_placement': nodes[first]['port']['source_placement'],
                      'from_port': first[1],
                      'to_piece': nodes[second]['port']['source_piece_id'],
                      'to_placement': nodes[second]['port']['source_placement'],
                      'to_port': second[1],
                      'endpoint_m': list(nodes[first]['port']['endpoint_m'])})
    declared = {f'{leg}.{direction}': (point, direction)
                for leg, values in scene.get('external_ports', {}).items() for direction, point in values.items()}
    external_nodes = sorted(set(nodes)-joined, key=lambda key: (
        nodes[key]['port']['engine_transport'], *_point(nodes[key]['port']['endpoint_m']),
        nodes[key]['port']['direction'], nodes[key]['port']['service_network'],
        nodes[key]['port']['source_piece_id'], str(nodes[key]['port']['source_origin_m'])))
    ports, external_by_node, used_names = [], {}, set()
    for index, key in enumerate(external_nodes, 1):
        source = deepcopy(nodes[key]['port'])
        matches = [name for name, (point, direction) in declared.items()
                   if direction == source['direction'] and _point(source['endpoint_m']) == _point(point)]
        require(len(matches) <= 1, 'Assembly has ambiguous declared external ports')
        source['id'] = matches[0] if matches else f'external-{index}'
        require(source['id'] not in used_names, 'Assembly has ambiguous coincident external port declarations')
        used_names.add(source['id'])
        ports.append(source)
        external_by_node[key] = source
    require(not declared or used_names == set(declared), 'Actual assembly external ports differ from declared scene')
    journeys = []
    for key, port in external_by_node.items():
        if port['direction'] != 'in':
            continue
        queue, seen = [key], set()
        while queue:
            current = queue.pop()
            if current in seen:
                continue
            seen.add(current)
            if current != key and current in external_by_node:
                finish = external_by_node[current]
                if finish['direction'] == 'out':
                    networks = sorted({port['service_network'], finish['service_network']})
                    journeys.append({'id': f'{port["id"]}>{finish["id"]}', 'entry_port': port['id'],
                                     'exit_port': finish['id'], 'service_network': '+'.join(networks),
                                     'role': port['role'], 'engine_transport_classes': [port['engine_transport']],
                                     'basis': 'actual intrinsic saved-PATH graphs and checked directed seams at saved poses'})
                continue
            queue.extend(graph[current]-seen)
    journeys.sort(key=lambda journey: journey['id'])
    allowed = {(journey['entry_port'], journey['exit_port']) for journey in journeys}
    forbidden = [{'from_port': a['id'], 'to_port': b['id'], 'from_service': a['service_network'],
                  'to_service': b['service_network'], 'basis': 'not reachable in the saved placed encoded-route graph'}
                 for a in ports for b in ports if a['direction'] == 'in' and b['direction'] == 'out'
                 and (a['id'], b['id']) not in allowed]
    resource_hashes[f'assembly_pose:{subject_id}'] = fingerprint(sorted(poses, key=lambda item: str(item)))
    return {'schema_version': 1,
            'purpose': 'Encoded-route reachability at saved assembly poses; complete boundary compatibility is not evaluated.',
            'subject_id': subject_id, 'subject_kind': 'assembly',
            'coordinate_units': 'metres east,north,height; saved assembly poses',
            'ports': ports, 'journeys': journeys, 'forbidden_transfers': forbidden,
            'encoded_route_joins': sorted(joins, key=lambda item: str(item)),
            'source': {'basis': 'intrinsic graphs measured from saved PATH resources and explicit saved assembly poses',
                       'scope': 'encoded_route_graph_only', 'resource_fingerprints': resource_hashes},
            'software_status': {'path_extraction': 'passed', 'placed_encoded_route_joins': 'passed',
                                'complete_boundary_compatibility': 'not_evaluated',
                                'physical_seams': 'unverified', 'in_game': 'unverified'},
            'compatibility_policy': 'Individual encoded-route seams only. Complete physical-channel boundary agreement, '
                                    'model seams, construction operation, and in-game behaviour require separate evidence.'}
