"""Independent saved-resource contract for the diagonal DD/GHSR crossing.

The writer is deliberately not imported. Literal native traffic measurements,
complete directed boundaries, source-fingerprinted mesh streams, and actual
indexed rail-bed coverage are checked independently of the source recipe.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
import json
import math
import re
import struct

from scp.dbpf import require
from scp.models import parse_s3d, positions, valid_frame, validate_s3d
from scp.track_paths import S3D, PATH

RECIPE = 'highway_ddrhw_diagonal_ghsr_crossing'
RECIPE_B = 'highway_ddrhw_diagonal_ghsr_crossing_alignment_b'
CELLS = ((0, 0), (0, 1))
CELLS_B = ((0, 0), (1, 0))
PIECE_ID = 'ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg'
PIECE_ID_B = 'ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b'
TOLERANCE = 2e-6
COLLAR_LENGTH_M = 3.0
INTERNAL_COLLAR_LENGTH_M = 1.0
# These pins identify independently inspected original NAM 50 resources.
DONOR_PINS = {
    ('dd_rhw', (*S3D, 0x5753A905)): '341aa73b6fc75596511883715d3edb3de91e988c3f7d1201bd02867313ee25f0',
    ('dd_rhw', (*S3D, 0x5753A985)): '1937f3d3e5e0c42995fa309d37bffb32a7a30640681b2bfa2920a67d1eb339a8',
    ('hsr', (*S3D, 0x5DC01A00)): '58e54d5d212e26564e5454c57b6fd3269067a7f48df81eec45925590c1a59fa6',
}
# Independent per-mesh semantic measurements are filled from the pinned native
# resources, never from a generated candidate. References may be renumbered;
# every position, extra attribute, index, primitive, and material remains bound.
EXPECTED_MESHES = (('8aa5a40fae1a20f98af68c8d8ee87ba9b153a70880baed037ecaa6040d5aee1e',
  '6f14f3f112f8cb6e2f1186e5891aad9c36a4810dd573b7366be84b77d73590dd',
  '3a4c515dc63fbd9717bb7533610baf89404ee1ef0abafd416bf7a274f1fa8099',
  'c1ca480c6cb635033713fe564a2a4e84aea476601a10128af6d7f9365e8ae744',
  'ec93dd2d0b7a49d59caebd87bc34bf5f5bfdc70dc9f8c5ff7006bdc8ebd56f10',
  '938f75fff25d17c926b22985ee5553fa9942da3836078dc62a0ab7cbeaabed86',
  'a7464910bc13f1ac9954bb354482ce1073783f010a811bbb9bfc7ecaad2702c0'),
 ('2f907f29bd75c30707516ae2f0967ad490463efa4878045f9ab43359ae997bc6',
  '89393e93f0bb31b26a6a99c44383f2dcdc573961e852884b3f6db8a4805e6422',
  'fd14f8311a5e159a814da3c0234baff8aa67a6bc577609be238bc85954c73f6c',
  '341998a8daf93b606cf4520272d4c38d8079da9de82c7189fb4edb9f1ffb2238',
  'ee640953757a3f36aea84a1888fb62ad078ac9b5d018393fc9e2ff1c90a911b2',
  '4f6c575c4af398202986c178279fb44e28b990360d2da947645db36b23e1b474',
  '8ed80b6c2f1766c3c47de51662cc6182cfbfbb27b8c956b7b5b2a56b116e97cd'))  # NATIVE_MESH_PINS
# Directly measured from the same pinned original NAM streams: the six DD
# meshes retain their poses, while ordinary GHSR support poses are 1 and 3.
# No generated alignment-B model participates in these expectations.
EXPECTED_MESHES_B = (EXPECTED_MESHES[0][:6] + (EXPECTED_MESHES[1][6],),
                     EXPECTED_MESHES[1][:6] + (EXPECTED_MESHES[0][6],))
EXPECTED_ANIMATION = '0100000003000000000000000000'  # NATIVE_ANIMATION_PIN
EXPECTED_TRAILING = "[(b'PROP', b'PROP\\x0c\\x00\\x00\\x00\\x00\\x00\\x00\\x00'), (b'REGP', b'REGP\\x0c\\x00\\x00\\x00\\x00\\x00\\x00\\x00')]"  # NATIVE_TRAILING_PIN
DD_NAMES = (b'Top Deck', b'Substructure', b'Barriers', b'Bottom Deck', b'Substructure', b'Barriers')


def _number(value):
    return int(value, 16) if isinstance(value, str) else value


def _alignment_b(piece):
    return piece is not None and piece.get('recipe') == RECIPE_B


def _cells(piece):
    return CELLS_B if _alignment_b(piece) else CELLS


def _spec(piece):
    require(piece.get('recipe') in (RECIPE, RECIPE_B) and piece.get('domain') == 'highway',
            'Wrong owner or recipe for the measured DD/GHSR crossing')
    footprint = [2, 1] if _alignment_b(piece) else [1, 2]
    require(piece.get('footprint') == footprint and tuple(map(tuple, piece.get('cells', ()))) == _cells(piece),
            'DD/GHSR alignment B must retain its two horizontally adjacent owned cells'
            if _alignment_b(piece) else 'DD/GHSR crossing must retain its two vertically adjacent owned cells')
    tiles = tuple(map(_number, piece.get('tile_ids', ())))
    require(len(tiles) == 2 and len(set(tiles)) == 2, 'DD/GHSR crossing needs two unique tile IDs')
    return tiles


def _route(transport, lane, entry, exit_, *points):
    return {'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
            'compatibility': 0, 'points': list(points)}


def _collar(endpoint, vector, *, entering):
    length = math.hypot(vector[0], vector[1])
    sign = 1.0 if entering else -1.0
    return (endpoint[0] + sign * COLLAR_LENGTH_M * vector[0] / length,
            endpoint[1] + sign * COLLAR_LENGTH_M * vector[1] / length, endpoint[2])


def expected_paths(piece=None):
    """Literal core paths; exterior vectors come from complementary helpers."""
    top = [_route(1, 0, 2, 3, (8., 3.2, 15.), (-3.2, -8., 15.)),
           _route(1, 1, 2, 3, (8., -3.2, 15.), (3.2, -8., 15.)),
           _route(1, 1, 3, 2, (-3.2, -8., 7.5), (8., 3.2, 7.5)),
           _route(1, 0, 3, 2, (3.2, -8., 7.5), (8., -3.2, 7.5))]
    bottom = [_route(1, 0, 1, 0, (-3.2, 8., 15.), (-8., 3.2, 15.)),
              _route(1, 1, 1, 0, (3.2, 8., 15.), (-8., -3.2, 15.)),
              _route(1, 1, 0, 1, (-8., -3.2, 7.5), (3.2, 8., 7.5)),
              _route(1, 0, 0, 1, (-8., 3.2, 7.5), (-3.2, 8., 7.5))]
    if _alignment_b(piece):
        # Transcribed from the independent native helper PATHs, not the core
        # writer. Pose-3 helper at (0,-1) exposes north x=-2.8/+2.9;
        # pose-1 helper at (1,1) exposes south x=+2.8/-2.9. Native core
        # exteriors would miss these by 0.1 m, so that correction is explicit.
        unit = INTERNAL_COLLAR_LENGTH_M / math.sqrt(2.)
        north_out, north_in = (2.9, 8., 1.), (-2.8, 8., 1.)
        south_out, south_in = (-2.9, -8., 1.), (2.8, -8., 1.)
        top += [_route(7, 0, 2, 1, (8., 2.9, 1.), (8. - unit, 2.9 + unit, 1.),
                       _collar(north_out, (-1., 1.), entering=False), north_out),
                _route(7, 0, 1, 2, north_in, _collar(north_in, (5.2, -5.1), entering=True),
                       (8. - unit, -2.9 + unit, 1.), (8., -2.9, 1.))]
        bottom += [_route(7, 0, 0, 3, (-8., -2.9, 1.), (-8. + unit, -2.9 - unit, 1.),
                          _collar(south_out, (1., -1.), entering=False), south_out),
                   _route(7, 0, 3, 0, south_in, _collar(south_in, (-5.2, 5.1), entering=True),
                          (-8. + unit, 2.9 - unit, 1.), (-8., 2.9, 1.))]
        return top, bottom
    a, b = (-8., -2.9, 1.), (-8., 2.9, 1.)
    c, d = (8., 2.9, 1.), (8., -2.9, 1.)
    unit = INTERNAL_COLLAR_LENGTH_M / math.sqrt(2.)
    top += [_route(7, 0, 0, 3, a, _collar(a, (1., -1.), entering=True),
                   (-2.9 - unit, -8. + unit, 1.), (-2.9, -8., 1.)),
            _route(7, 0, 3, 0, (2.9, -8., 1.), (2.9 - unit, -8. + unit, 1.),
                   _collar(b, (-5.2, 5.1), entering=False), b)]
    bottom += [_route(7, 0, 2, 1, c, _collar(c, (-1., 1.), entering=True),
                      (2.9 + unit, 8. - unit, 1.), (2.9, 8., 1.)),
               _route(7, 0, 1, 2, (-2.9, 8., 1.), (-2.9 + unit, 8. - unit, 1.),
                      _collar(d, (5.2, -5.1), entering=False), d)]
    return top, bottom


def _point(point, cell=(0, 0), rotation=0):
    x, north, height = point
    x += 16 * cell[0]
    north -= 16 * cell[1]
    for _ in range(rotation):
        x, north = north, -x
    return tuple(round(v, 6) for v in (x, north, height))


def _signature(route):
    return (route['transport'], route['lane'], route['entry'], route['exit'], route['compatibility'],
            tuple(_point(point) for point in route['points']))


def _edge(point):
    x, north, _ = point
    matches = [abs(x + 8) <= TOLERANCE, abs(north - 8) <= TOLERANCE,
               abs(x - 8) <= TOLERANCE, abs(north + 8) <= TOLERANCE]
    require(sum(matches) == 1, 'DD/GHSR PATH endpoint is not on one unambiguous tile edge')
    return matches.index(True)


def _graph(routes_by_cell, rotation=0, *, cells=CELLS):
    starts, ends = defaultdict(list), defaultdict(list)
    require(len(routes_by_cell) == len(cells) == 2, 'DD/GHSR graph needs both owned cells')
    for tile_no, (cell, routes) in enumerate(zip(cells, routes_by_cell)):
        for route_no, route in enumerate(routes):
            starts[(route['transport'], _point(route['points'][0], cell, rotation))].append((tile_no, route_no))
            ends[(route['transport'], _point(route['points'][-1], cell, rotation))].append((tile_no, route_no))
    require(all(len(value) == 1 for value in (*starts.values(), *ends.values())),
            'Ambiguous DD/GHSR lane endpoint')
    shared = starts.keys() & ends.keys()
    incoming, outgoing = starts.keys() - ends.keys(), ends.keys() - starts.keys()
    for seam in shared:
        before_tile, before_no = ends[seam][0]
        after_tile, after_no = starts[seam][0]
        before = _tangent(routes_by_cell[before_tile][before_no]['points'], 'out')
        after = _tangent(routes_by_cell[after_tile][after_no]['points'], 'in')
        require(max(abs(a - b) for a, b in zip(before, after)) <= TOLERANCE,
                'DD/GHSR internal seam has a discontinuous travel heading')
    require(len(shared) == len(incoming) == len(outgoing) == 6,
            'DD/GHSR crossing lost a complete internal lane or external boundary')
    visited, journeys = set(), []
    for key in sorted(incoming):
        first = starts[key][0]
        cursor, chain = first, []
        while True:
            require(cursor not in visited, 'DD/GHSR crossing contains a loop or shared directed route')
            visited.add(cursor)
            chain.append(cursor)
            tile, route_no = cursor
            route = routes_by_cell[tile][route_no]
            endpoint = (route['transport'], _point(route['points'][-1], cells[tile], rotation))
            if endpoint in outgoing:
                break
            require(endpoint in starts, 'DD/GHSR route stops inside the crossing')
            cursor = starts[endpoint][0]
        require(len(chain) == 2 and endpoint[0] == key[0] and endpoint[1][2] == key[1][2],
                'DD/GHSR crossing added a network transfer, height transfer, or shortened journey')
        journeys.append((key, endpoint, first, cursor))
    require(len(visited) == 12, 'DD/GHSR graph leaves an unconsumed traffic fragment')
    require(Counter((first[0], first[1][2]) for first, *_ in journeys) ==
            Counter({(1, 15.): 2, (1, 7.5): 2, (7, 1.): 2}),
            'DD/GHSR crossing lost a deck lane or ground railway direction')
    return journeys


def _native_helpers(piece=None):
    """Literal native adjacent halves, including the distinct west DD phase."""
    result = [
        ((1, 0), [
            _route(1, 0, 1, 0, (-3.2, 8., 15.), (-8., 3.2, 15.)),
            _route(1, 1, 1, 0, (3.2, 8., 15.), (-8., -3.2, 15.)),
            _route(1, 0, 0, 1, (-8., -3.2, 7.5), (3.2, 8., 7.5)),
            _route(1, 1, 0, 1, (-8., 3.2, 7.5), (-3.2, 8., 7.5))]),
        ((-1, 1), [
            _route(1, 0, 2, 3, (8., 3.2, 15.), (-3.2, -8., 15.)),
            _route(1, 1, 2, 3, (8., -3.2, 15.), (3.2, -8., 15.)),
            _route(1, 0, 3, 2, (3.2, -8., 7.5), (8., -3.2, 7.5)),
            _route(1, 1, 3, 2, (-3.2, -8., 7.5), (8., 3.2, 7.5))]),
        ((-1, 0), [
            _route(7, 0, 2, 1, (8., 2.9, 1.), (2.8, 8., 1.)),
            _route(7, 0, 1, 2, (-2.9, 8., 1.), (8., -2.9, 1.))]),
        ((1, 1), [
            _route(7, 0, 0, 3, (-8., -2.9, 1.), (-2.8, -8., 1.)),
            _route(7, 0, 3, 0, (2.9, -8., 1.), (-8., 2.9, 1.))]),
    ]
    if _alignment_b(piece):
        # DD source halves keep the same poses and deck directions. Only
        # their grid cells move. Rail helpers likewise retain literal native
        # route records, but exchange which side of the core they border.
        return [((0, 1), result[0][1]), ((1, -1), result[1][1]),
                ((0, -1), result[3][1]), ((1, 1), result[2][1])]
    return result


def _tangent(points, direction):
    a, b = points[:2] if direction == 'in' else points[-2:]
    vector = tuple(b[i] - a[i] for i in range(3))
    length = math.hypot(*vector[:2])
    require(length > 0 and abs(vector[2]) <= TOLERANCE, 'Invalid DD/GHSR boundary grade')
    return tuple(value / length for value in vector)


def _check_helpers(routes_by_cell, piece=None):
    cells = _cells(piece)
    journeys = _graph(routes_by_cell, cells=cells)
    boundary = []
    for start, finish, first, last in journeys:
        for direction, key, location in [('in', start, first), ('out', finish, last)]:
            tile, index = location
            route = routes_by_cell[tile][index]
            candidates = []
            for helper_cell, helper_routes in (_native_helpers(piece) if piece is not None else _native_helpers()):
                for helper in helper_routes:
                    end = helper['points'][-1 if direction == 'in' else 0]
                    if helper['transport'] == key[0] and _point(end, helper_cell) == key[1]:
                        candidates.append(helper)
            require(len(candidates) == 1, 'No unique complete directed native DD/GHSR helper counterpart')
            actual = _tangent(route['points'], direction)
            counterpart = _tangent(candidates[0]['points'], 'out' if direction == 'in' else 'in')
            require(max(abs(a - b) for a, b in zip(actual, counterpart)) <= TOLERANCE,
                    'DD/GHSR exterior collar tangent differs from its native helper')
            boundary.append({'transport': key[0], 'direction': direction, 'endpoint_m': list(key[1]),
                             'tangent': list(actual), 'source_cell': list(cells[tile]),
                             'edge': route['entry' if direction == 'in' else 'exit']})
    return boundary


def check_paths(resources, piece):
    from scp.verify import parse_paths
    tiles = _spec(piece)
    parsed = [parse_paths(resources[*PATH, tile]) for tile in tiles]
    expected = expected_paths(piece)
    for index, item in enumerate(parsed):
        require(item['version'] == '1.2' and item['terrain'] == 1,
                'DD/GHSR active PATH must explicitly retain elevation with UseElevation=1')
        require(Counter(map(_signature, item['routes'])) == Counter(map(_signature, expected[index])),
                'DD/GHSR saved routes differ from the independent lane, height, and collar contract')
        for route in item['routes']:
            require(_edge(route['points'][0]) == route['entry'] and
                    _edge(route['points'][-1]) == route['exit'],
                    'DD/GHSR PATH edge numbers disagree with its saved endpoints')
    routes = [item['routes'] for item in parsed]
    for rotation in range(4):
        _graph(routes, rotation, cells=_cells(piece))
    ports = _check_helpers(routes, piece)
    report = {'tile_count': 2, 'complete_directed_journeys': 6, 'car_journeys': 4,
            'ghsr_journeys': 2, 'matched_internal_lane_seams': 6,
            'route_fragments_consumed': 12, 'complete_native_boundary_members_checked': len(ports),
            'proper_rotations_checked': 4, 'external_ghsr_collar_length_m': COLLAR_LENGTH_M,
            'internal_ghsr_collar_length_m': INTERNAL_COLLAR_LENGTH_M,
            'native_helper_boundary_tangents_verified': True, 'internal_seam_tangents_verified': True,
            'use_path_elevation': True,
            'no_capacity_only_paths': True, 'no_network_or_height_transfers': True,
            'game_operation_tested': False}
    if _alignment_b(piece):
        report.update({'alignment': 'B', 'fixed_directed_highway_centerline_north_minus_east_m': -8.,
                       'railway_centerline_north_plus_east_m': 8.,
                       'native_core_rail_exterior_endpoint_correction_m': .1,
                       'railway_internal_endpoint_correction_m': 0.})
    return report


def reviewed_contract(piece):
    _spec(piece)
    routes = expected_paths(piece)
    journeys = _graph(routes, cells=_cells(piece))
    result = {'ports': {}, 'port_vectors': {}, 'port_transports': {}, 'port_directions': {},
              'movements': [], '_channels': []}
    counters = Counter()
    for start, finish, first, last in journeys:
        family = 'ghsr-track' if start[0] == 7 else 'upper-lane' if start[1][2] == 15 else 'lower-lane'
        counters[family] += 1
        name = f'{family}-{counters[family]:02d}'
        for suffix, key, location in [('in', start, first), ('out', finish, last)]:
            tile, index = location
            port = name + '-' + suffix
            result['ports'][port] = list(key[1])
            result['port_vectors'][port] = list(_tangent(routes[tile][index]['points'], suffix))
            result['port_transports'][port] = key[0]
            result['port_directions'][port] = suffix
        result['movements'].append([name + '-in', name + '-out'])
        result['_channels'].append({'id': name, 'component_id': family,
            'kind': 'rail-track' if start[0] == 7 else 'road-lane',
            'traffic_modes': ['monorail'] if start[0] == 7 else ['car'],
            'entry_port': name + '-in', 'exit_port': name + '-out'})
    return result


def reviewed_facts(piece):
    """Source-bound intrinsic facts; no neighbour compatibility is inferred."""
    _spec(piece)
    cells = _cells(piece)
    routes = expected_paths(piece)
    contract = reviewed_contract(piece)
    locations = {tuple(port['endpoint_m']): port for port in _check_helpers(routes, piece)}
    ports, channels = [], []
    for channel in contract['_channels']:
        rail = channel['kind'] == 'rail-track'
        component = ('ghsr-mainline' if rail else 'upper-mainline'
                     if channel['component_id'] == 'upper-lane' else 'lower-mainline')
        ends = []
        for name in (channel['entry_port'], channel['exit_port']):
            direction = contract['port_directions'][name]
            position = contract['ports'][name]
            measurement = locations[tuple(position)]
            tile_no = cells.index(tuple(measurement['source_cell']))
            route = next(route for route in routes[tile_no]
                         if route['transport'] == contract['port_transports'][name] and
                         list(_point(route['points'][0 if direction == 'in' else -1], cells[tile_no])) == position)
            sampled = _tangent([_point(point, cells[tile_no]) for point in route['points']], direction)[:2]
            ports.append({'id': name, 'direction': direction,
                'engine_transport': contract['port_transports'][name], 'edge': measurement['edge'],
                'endpoint_m': position, 'sampled_tangent': list(sampled),
                'tangent': contract['port_vectors'][name][:2], 'grade': 0.,
                'service_network': 'ghsr' if rail else 'road',
                'service_family': 'high-speed-rail' if rail else 'road',
                'variant': 'ghsr' if rail else 'dd-rhw-l2' if position[2] == 15. else 'dd-rhw-l1',
                'role': 'primary', 'channel_kind': 'rail-track' if rail else 'road-lane',
                'traffic_modes': ['monorail'] if rail else ['car'],
                'source_cell': measurement['source_cell'], 'channel_id': channel['id']})
            ends.append(name)
        channels.append({'id': channel['id'], 'component_id': component,
                         'kind': 'rail-track' if rail else 'road-lane',
                         'traffic_modes': ['monorail'] if rail else ['car'], 'ports': ends})
    movements = list(map(tuple, contract['movements']))
    forbidden = [(a['id'], b['id']) for a in ports for b in ports
                 if a['direction'] == 'in' and b['direction'] == 'out' and
                 (a['id'], b['id']) not in movements]
    return {'reference_piece_id': PIECE_ID_B if _alignment_b(piece) else PIECE_ID,
        'footprint': [2, 1] if _alignment_b(piece) else [1, 2], 'cells': [list(cell) for cell in cells],
        'path_hashes_by_cell': _path_hashes(piece),
        'ports': ports, 'movements': movements, 'forbidden_transfers': forbidden,
        'components': [{'id': 'upper-mainline', 'network': 'road', 'construction_network': 'dirtroad'},
                       {'id': 'lower-mainline', 'network': 'road', 'construction_network': 'dirtroad'},
                       {'id': 'ghsr-mainline', 'network': 'ghsr', 'construction_network': 'monorail'}],
        'channels': channels}


def connector_source_files(_piece_id=None):
    return ['domains/highway/implementation/scp_highway/ghsr_crossing_verify.py',
            'domains/highway/00_pieces/' + (PIECE_ID_B if _piece_id == PIECE_ID_B else PIECE_ID) +
            '/evidence/native-contract.jsonc']


def _path_hashes(piece):
    if _alignment_b(piece):
        return [([0, 0], '0317b165f05ef91efb4bd535d1b04f08e709ed3959c296516733fd8e3e210ff8'),
                ([1, 0], '88bfddb92442071231b47a7118286da59c8b3413fe8cf6d672ae37a3222a607a')]
    return [([0, 0], 'c0647202666bf828612a49fd1576276379d848a4fa3a0fb5028cf1bb995f6db3'),
            ([0, 1], 'c053ea61baa8481a327223a057bddfb94f2fee25ed2b5137ee21d9851876422a')]


def _f32(value):
    return struct.unpack('<f', struct.pack('<f', value))[0]


def _mesh_signature(model, mesh, *, turns=0, offset=(0., 0., 0.), source=False):
    frames = []
    for vi, ii, pi, mi in mesh['frames']:
        block = model['vertices'][vi]
        require(block['stride'] == 20 and (source or block['format'] == 0x80004001),
                'DD/GHSR saved VERT must use packed XYZ/UV format 80004001')
        vertices = []
        for at in range(0, len(block['data']), block['stride']):
            x, height, south = struct.unpack_from('<3f', block['data'], at)
            for _ in range(turns):
                x, south = -south, x
            xyz = [_f32(value + delta) for value, delta in zip((x, height, south), offset)]
            xyz = [0. if value == 0 else value for value in xyz]
            vertices.append([xyz, block['data'][at + 12:at + block['stride']].hex()])
        frames.append({'vertex_flags': block['flags'], 'format': 0x80004001,
            'vertices': vertices, 'indices': model['indices'][ii],
            'primitives': model['primitives'][pi], 'material': model['materials'][mi]['raw'].hex()})
    payload = {'name': mesh['name'].hex(), 'flags': mesh['flags'], 'frames': frames}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def native_mesh_measurements(donors, piece=None):
    """Independently derive semantic pins from the original fingerprinted inputs."""
    sources = {}
    for (label, key), expected in DONOR_PINS.items():
        require(label in donors and key in donors[label], 'Missing audited native DD/GHSR source')
        raw = donors[label][key]
        require(hashlib.sha256(raw).hexdigest() == expected, 'Native DD/GHSR source fingerprint changed')
        sources[key[2]] = parse_s3d(raw)
    rail = sources[0x5DC01A00]
    rail_meshes = [m for m in rail['meshes'] if all(valid_frame(rail, f) for f in m['frames'])]
    require(len(rail_meshes) == 1 and rail_meshes[0]['name'].rstrip(b'\0') == b'support',
            'Native GHSR valid support-mesh inventory changed')
    result = []
    parts = [(0x5753A905, 0, 1), (0x5753A985, 2, 3)] if _alignment_b(piece) else [
        (0x5753A905, 0, 3), (0x5753A985, 2, 1)]
    for iid, turns, rail_turns in parts:
        source = sources[iid]
        meshes = [m for m in source['meshes'] if m['name'].rstrip(b'\0') != b'HSR']
        require(tuple(m['name'].rstrip(b'\0') for m in meshes) == DD_NAMES,
                'Native DD/GHSR six-mesh deck inventory changed')
        result.append(tuple([_mesh_signature(source, m, turns=turns, source=True) for m in meshes] +
                            [_mesh_signature(rail, rail_meshes[0], turns=rail_turns, source=True)]))
    return tuple(result), sources[0x5753A905]['anim_header'].hex(), repr(sources[0x5753A905]['trailing'])


def _triangles(model, mesh):
    vi, ii, pi, _mi = mesh['frames'][0]
    points, indices = positions(model['vertices'][vi]), model['indices'][ii]['values']
    faces = []
    for kind, first, count in model['primitives'][pi]:
        require(kind == 0 and count % 3 == 0, 'DD/GHSR geometry requires indexed triangle lists')
        faces += [tuple(points[i] for i in indices[at:at + 3]) for at in range(first, first + count, 3)]
    return faces


def _inside_surface(x, south, face):
    a, b, c = face
    denominator = (b[2] - c[2]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[2] - c[2])
    if abs(denominator) < 1e-10:
        return False
    first = ((b[2] - c[2]) * (x - c[0]) + (c[0] - b[0]) * (south - c[2])) / denominator
    second = ((c[2] - a[2]) * (x - c[0]) + (a[0] - c[0]) * (south - c[2])) / denominator
    weights = (first, second, 1 - first - second)
    if min(weights) < -2e-5:
        return False
    height = sum(weight * point[1] for weight, point in zip(weights, face))
    # Native GHSR rail-bearing faces reach about 1.18933 m; the 1 m
    # PATH datum is a native vehicle reference, rather than the bed top.
    # Exclude the outboard parapet tops at about 1.98933 m. Exact source
    # fingerprints separately bind every face, so this is not a geometry waiver.
    return -1.1 <= height <= 1.2 + TOLERANCE


def _rail_bed_coverage(models, piece=None):
    # A train body straddles the owned-cell boundary. Include the actual native
    # helper half there instead of demanding that one clipped half cover it.
    # West helper pose 1 is the same native stream as the lower core; east
    # helper pose 3 is the same stream as the upper core. All streams have
    # already passed the independent original-donor semantic fingerprints.
    faces = []
    placements = ((0, (0., 0.)), (1, (16., 0.)),
                  (1, (0., -16.)), (0, (16., 16.))) if _alignment_b(piece) else (
                      (0, (0., 0.)), (1, (0., 16.)), (1, (-16., 0.)), (0, (16., 16.)))
    for model_no, offset in placements:
        for face in _triangles(models[model_no], models[model_no]['meshes'][6]):
            faces.append(tuple((p[0] + offset[0], p[1], p[2] + offset[1]) for p in face))
    samples = 0
    for cell, routes in zip(_cells(piece), expected_paths(piece)):
        for route in routes[4:]:
            for first, last in zip(route['points'], route['points'][1:]):
                dx, dn = last[0] - first[0], last[1] - first[1]
                length = math.hypot(dx, dn)
                for step in range(math.ceil(length) + 1):
                    fraction = min(1., step / max(1, math.ceil(length)))
                    x, north = first[0] + fraction * dx, first[1] + fraction * dn
                    for lateral in (-2.5, 0., 2.5):
                        east = x - lateral * dn / length + cell[0] * 16.
                        south = -(north + lateral * dx / length) + cell[1] * 16.
                        require(any(_inside_surface(east, south, face) for face in faces),
                                f'Saved GHSR rail bed does not cover its five-metre train corridor at {(east, south)}')
                        samples += 1
    return samples


def check_models(resources, piece, donors=None):
    tiles = _spec(piece)
    expected_meshes = EXPECTED_MESHES_B if _alignment_b(piece) else EXPECTED_MESHES
    if donors is not None and all(label in donors for label in ('dd_rhw', 'hsr')):
        measured = native_mesh_measurements(donors, piece)
        require(measured == (expected_meshes, EXPECTED_ANIMATION, EXPECTED_TRAILING),
                'Independent native DD/GHSR semantic measurement pins changed')
    canonical, textures = [], set()
    for tile_no, tile in enumerate(tiles):
        for zoom in range(5):
            key = (*S3D, tile + zoom)
            require(key in resources, 'Missing DD/GHSR canonical model zoom')
            model = parse_s3d(resources[key])
            validate_s3d(model)
            require(len(model['meshes']) == 7, 'DD/GHSR model lost a deck, barrier, or ground railway mesh')
            require(model['anim_header'].hex() == EXPECTED_ANIMATION and repr(model['trailing']) == EXPECTED_TRAILING,
                    'DD/GHSR saved animation or transform data differs from its native source')
            actual = tuple(_mesh_signature(model, mesh) for mesh in model['meshes'])
            require(actual == expected_meshes[tile_no],
                    'DD/GHSR saved native mesh positions, attributes, indices, or materials changed')
            textures.update(texture for material in model['materials'] for texture in material['textures'])
            if zoom == 0:
                canonical.append(model)
    minimum = min(point[1] for model in canonical for mesh in model['meshes'][:6]
                  for point in positions(model['vertices'][mesh['frames'][0][0]]))
    require(abs(minimum - 6.5) <= TOLERANCE, 'DD/GHSR crossing has a new low support or changed underside')
    require(minimum - (1. + 5.) >= .5 - TOLERANCE,
            'DD/GHSR crossing obstructs the five-metre train-height corridor')
    preview = parse_s3d(resources[*S3D, _number(piece['preview_id'])])
    validate_s3d(preview)
    require(preview['anim_header'].hex() == EXPECTED_ANIMATION and repr(preview['trailing']) == EXPECTED_TRAILING,
            'DD/GHSR preview animation or transforms differ from the placed models')
    expected_preview = Counter(_mesh_signature(model, mesh, offset=(16. * cell[0], 0., 16. * cell[1]))
                               for cell, model in zip(_cells(piece), canonical) for mesh in model['meshes'])
    actual_preview = Counter(_mesh_signature(preview, mesh) for mesh in preview['meshes'])
    require(actual_preview == expected_preview, 'DD/GHSR preview does not contain the complete placed geometry')
    report = {'native_channel_fingerprints_verified': True, 'model_resources_checked': 11,
              'native_paired_deck_width_m': 16., 'deck_surface_heights_m': [7.5, 15.],
              'ghsr_path_height_m': 1., 'lower_underside_height_m': minimum,
              'train_envelope_width_m': 5., 'train_envelope_height_m': 5.,
              'minimum_train_roof_clearance_m': minimum - 6.,
              'rail_bed_corridor_samples': _rail_bed_coverage(canonical, piece),
              'rail_bed_coverage_includes_native_helper_collars': True,
              'native_overhang_preserved': True, 'preview_matches_all_cells': True,
              'texture_ids': sorted(textures), 'game_rendering_tested': False}
    if piece.get('shadow_mode') == 'model-carrier':
        from .shadow_verify import check_resources
        report.update(check_resources(resources, piece))
    return report


def check_construction_fields(piece, fields):
    """Check exact static core flags; helper fields have their own verifier."""
    _spec(piece)
    rows = fields.get('CellLayout', [])
    cons = fields.get('ConsLayout', [])
    checks = fields.get('CheckType', [])
    core_checks = (['a - dirtroad: 0x03010000 monorail: 0x00030100',
                    'b - dirtroad: 0x00000301 monorail: 0x01000003'] if _alignment_b(piece) else [
                        'a - dirtroad: 0x03010000 monorail: 0x01000003',
                        'b - dirtroad: 0x00000301 monorail: 0x00030100'])
    require(all(row in checks for row in core_checks) and
            all(sum(row.startswith(symbol + ' - ') for row in checks) == 1 for symbol in 'ab'),
            'Wrong measured DD/GHSR static network flags')
    require(len(rows) == len(cons) and rows and len({len(row) for row in rows + cons}) == 1,
            'DD/GHSR construction and ownership grids differ')
    coordinates = {}
    for y, row in enumerate(rows):
        for x, symbol in enumerate(row):
            if symbol in 'ab':
                require(symbol not in coordinates, 'DD/GHSR construction repeats an owned cell')
                coordinates[symbol] = x, y
    offset = (1, 0) if _alignment_b(piece) else (0, 1)
    require(set(coordinates) == {'a', 'b'} and
            coordinates['b'] == tuple(a + b for a, b in zip(coordinates['a'], offset)),
            'DD/GHSR construction does not own exactly the horizontal two-cell alignment-B core'
            if _alignment_b(piece) else 'DD/GHSR construction does not own exactly the vertical two-cell core')
    for x, y in coordinates.values():
        require(cons[y][x] == '+', 'DD/GHSR core is missing its fixed-network placement token')
    require(sum(row.count('+') for row in cons) == 2 and
            all(symbol in '.^<+' for row in cons for symbol in row),
            'DD/GHSR helpers must not become owned fixed models')
    for token, axis in [('^', 0), ('<', 1)]:
        locations = [(x, y) for y, row in enumerate(rows) for x, symbol in enumerate(row) if symbol == token]
        cons_locations = [(x, y) for y, row in enumerate(cons) for x, symbol in enumerate(row) if symbol == token]
        require(len(locations) == 1 and locations == cons_locations and
                coordinates['a'][axis] == locations[0][axis],
                'DD/GHSR construction anchors move the measured owned-cell origin')
    helper_count = 0
    if piece.get('native_ghsr_approaches'):
        # Independently transcribed construction pairs. A valid RUL1 table
        # cannot compensate for a RUL0 cell requesting a different marker.
        helpers = (
            ((0, 1), 'monorail:0x04000100dirtroad:0x00000301,0xffffffffoptional'),
            ((1, -1), 'monorail:0x04000100dirtroad:0x03010000,0xffffffffoptional'),
            ((0, -1), 'rail:0x00000101monorail:0x01000003,0xffffffffoptional'),
            ((1, 1), 'rail:0x01010000monorail:0x00030100,0xffffffffoptional'),
        ) if _alignment_b(piece) else (
            ((1, 0), 'monorail:0x04000100dirtroad:0x00000301,0xffffffffoptional'),
            ((-1, 1), 'monorail:0x04000100dirtroad:0x03010000,0xffffffffoptional'),
            ((-1, 0), 'rail:0x01010000monorail:0x00030100,0xffffffffoptional'),
            ((1, 1), 'rail:0x00000101monorail:0x01000003,0xffffffffoptional'),
        )
        palette = {}
        for check in checks:
            match = re.fullmatch(r'\s*([A-Za-z])\s*-\s*(.+)', check)
            require(match and match[1] not in palette, 'Invalid or duplicate DD/GHSR helper palette symbol')
            palette[match[1]] = re.sub(r'\s+', '', match[2]).lower()
        symbols = set()
        origin_x, origin_y = coordinates['a']
        for (east, south), expected in helpers:
            x, y = origin_x + east, origin_y + south
            require(0 <= y < len(rows) and 0 <= x < len(rows[y]),
                    'DD/GHSR construction omits a required native helper cell')
            symbol = rows[y][x]
            require(symbol in palette and symbol not in 'ab' and symbol not in symbols and
                    palette[symbol] == expected and cons[y][x] == '.',
                    'DD/GHSR native helper flags, mask, optional state, or ownership changed')
            symbols.add(symbol)
        require(set(palette) == symbols | {'a', 'b'} and
                {symbol for row in rows for symbol in row} <= symbols | set('ab.^<'),
                'DD/GHSR construction has an undeclared native helper')
        helper_count = len(helpers)
    require(fields.get('Costs') == ['1000'], 'Wrong DD/GHSR crossing construction cost')
    return {'explicit_two_cell_construction': True, 'native_core_flags_verified': True,
            'owned_tiles': 2, 'native_helper_check_flags_verified': helper_count,
            'game_construction_tested': False}


def check_alignment_coverage(resources_a, piece_a, resources_b, piece_b):
    """Prove both adjacent rail-grid phases without reversing either DD deck.

    The native 16 m city grid admits parallel rail centreline intercepts
    separated by 16 m. Translating the crossing along its fixed directed DD
    axis by a full grid cell adds 32 m to that intercept. Consequently two
    residue classes are required; four proper rotations of A do not supply B
    while retaining the same upper-deck and lower-deck travel directions.
    """
    require(piece_a.get('recipe') == RECIPE and piece_b.get('recipe') == RECIPE_B,
            'Both distinct alignment A and alignment B are required for grid coverage')
    check_paths(resources_a, piece_a)
    check_paths(resources_b, piece_b)
    from scp.verify import parse_paths
    for piece, resources in ((piece_a, resources_a), (piece_b, resources_b)):
        for cell, tile in zip(_cells(piece), _spec(piece)):
            routes = parse_paths(resources[*PATH, tile])['routes']
            # Opposing lane offsets are symmetric around the same DD axis.
            for height, sign in ((15., -1.), (7.5, 1.)):
                lanes = [route for route in routes if route['transport'] == 1 and
                         all(abs(point[2] - height) <= TOLERANCE for point in route['points'])]
                require(len(lanes) == 2, 'Alignment coverage lost one fixed-direction DD lane')
                for route in lanes:
                    first, last = [_point(route['points'][index], cell) for index in (0, -1)]
                    require(sign * (last[0] - first[0]) > 0 and sign * (last[1] - first[1]) > 0,
                            'Alignment coverage reverses an existing highway deck direction')
                for end in (0, -1):
                    ends = [_point(route['points'][end], cell) for route in lanes]
                    center = tuple(sum(point[axis] for point in ends) / 2 for axis in range(2))
                    require(abs(center[1] - center[0] + 8.) <= TOLERANCE,
                            'Alignment coverage moves the fixed highway centreline')
    # The explicit verified rail endpoints put the symmetric native track
    # pairs about these design axes. Native 0.1 m chord asymmetries are bound
    # above; they are not rounded away to manufacture neighbour compatibility.
    intercepts = (-8., 8.)
    require({int(value) % 32 for value in intercepts} == {8, 24},
            'Crossing alignment variants fail the two rail-grid residue classes')
    return {'alignment_classes_checked': 2, 'fixed_highway_centerline_north_minus_east_m': -8.,
            'railway_centerline_north_plus_east_m': list(intercepts),
            'crossing_centres_east_north_m': [[0., -8.], [8., 0.]],
            'adjacent_diagonal_railway_spacing_m': 16. / math.sqrt(2.),
            'full_grid_translation_along_highway_east_north_m': [16., 16.],
            'railway_intercept_repeat_m': 32., 'both_highway_deck_directions_preserved': True,
            'proper_rotations_per_alignment': 4, 'game_alignment_tested': False}
