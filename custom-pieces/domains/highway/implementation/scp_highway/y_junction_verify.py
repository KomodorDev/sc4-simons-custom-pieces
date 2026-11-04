"""Independent saved-resource contracts for the first compact DD RHW Y.

Expected lane cuts are reconstructed from the reviewed source polylines,
without importing the curve writer, module writer, or construction writer.
Actual saved PATHs, indexed model faces, and construction fields supply the
candidate evidence; human game observations remain separate.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
from functools import lru_cache
import hashlib
import math
from pathlib import Path

from scp import jsonc
from scp.dbpf import decompress, require
from scp.track_paths import PATH
from scp.verify import parse_paths

ROOT = Path(__file__).resolve().parents[4]
SUBJECT = ROOT/'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction'
NAMES = ('A-B', 'B-A', 'A-C', 'C-A', 'B-C', 'C-B')
KEYS = ('y-diagonal-stem-split', 'y-diagonal-branch', 'y-orthogonal-core')
POSITION_EPS = 2e-8
# Independently reviewed physical ownership; never ask the module writer for
# the expected cells while checking its candidate definitions or resources.
OWNED_WORLD_CELLS = {
    KEYS[0]: ((-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (-1, 2), (0, 2), (-1, 3)),
    KEYS[1]: ((-1, -3), (-1, -2), (0, -2), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1)),
    KEYS[2]: ((-1, 0), (0, 0), (1, 0), (2, 0), (3, 0)),
}


@dataclass(frozen=True)
class RouteVariantConfig:
    """Immutable explicit identities, independently reviewed cells, and source."""
    keys: tuple
    piece_ids: tuple
    recipes: tuple
    owned_world_cells: tuple
    source_loader: object

    def __post_init__(self):
        require(all(type(values) is tuple and len(values) == 3 for values in (
            self.keys, self.piece_ids, self.recipes, self.owned_world_cells))
            and all(len(set(values)) == 3 for values in (self.keys, self.piece_ids, self.recipes))
            and callable(self.source_loader), 'Invalid finite Y route-variant configuration')
        cells = [cell for group in self.owned_world_cells for cell in group]
        require(all(type(group) is tuple and group for group in self.owned_world_cells)
                and all(type(cell) is tuple and len(cell) == 2 and all(type(v) is int for v in cell)
                        for cell in cells) and len(cells) == len(set(cells)),
                'Y route-variant ownership must be immutable, nonempty, and disjoint')


def _key(piece, *, variant=None):
    key = piece.get('geometry_key')
    require(key in (KEYS if variant is None else variant.keys) and piece.get('recipe', '').startswith('highway_ddrhw_y_')
            and piece.get('domain') == 'highway', 'Unknown compact DD RHW Y component')
    return key


def _owner(cell, *, variant=None):
    keys = KEYS if variant is None else variant.keys
    if cell[1] >= 1:
        return keys[0]
    if cell[1] <= -1:
        return keys[1]
    return keys[2]


def _source():
    return deepcopy(_source_for_bytes(*_source_bytes()))


def _source_bytes():
    """Read both current inputs before consulting either bounded cache."""
    return ((SUBJECT/'evidence/design-geometry.jsonc').read_bytes(),
            (SUBJECT/'evidence/source-verification.jsonc').read_bytes())


@lru_cache(maxsize=1)
def _source_for_bytes(geometry_bytes, review_bytes):
    source = jsonc.loads(geometry_bytes.decode('utf-8'))
    evidence = jsonc.loads(review_bytes.decode('utf-8'))
    require(evidence.get('passed') is True and evidence.get('source', {}).get('design_geometry_sha256')
            == hashlib.sha256(geometry_bytes).hexdigest(),
            'The Y source polylines lack a matching independent source review')
    require(set(source['routes']) == set(NAMES), 'Y source must retain all six directed lane journeys')
    return source


def _point_at(a, b, fraction):
    return tuple(a[k]+fraction*(b[k]-a[k]) for k in range(3))


def _world_cell(point):
    return math.floor((point[0]+8.)/16.), math.floor((-point[1]+8.)/16.)


def _side(point):
    candidates = [side for side, axis, value in ((0, 0, -8.), (1, 1, 8.), (2, 0, 8.), (3, 1, -8.))
                  if abs(point[axis]-value) <= POSITION_EPS]
    require(candidates, 'Expected Y lane has an interior endpoint')
    return candidates[0]


def _split(points):
    """Cut each finite source segment at exact city-grid planes."""
    fragments = []
    for a, b in zip(points, points[1:]):
        cuts = [0., 1.]
        for axis in (0, 1):
            delta = b[axis]-a[axis]
            if abs(delta) < 1e-14:
                continue
            low, high = sorted((a[axis], b[axis]))
            first, last = math.ceil((low-8.)/16.), math.floor((high-8.)/16.)
            for index in range(first, last+1):
                fraction = (16.*index+8.-a[axis])/delta
                if 1e-12 < fraction < 1.-1e-12:
                    cuts.append(fraction)
        cuts = sorted(set(cuts))
        for lo, hi in zip(cuts, cuts[1:]):
            start, end = _point_at(a, b, lo), _point_at(a, b, hi)
            if math.dist(start[:2], end[:2]) < 1e-10:
                continue
            cell = _world_cell(_point_at(a, b, (lo+hi)/2.))
            if fragments and fragments[-1]['cell'] == cell and math.dist(fragments[-1]['points'][-1], start) <= POSITION_EPS:
                fragments[-1]['points'].append(end)
            else:
                fragments.append({'cell': cell, 'points': [start, end]})
    return fragments


def _expected_world(*, variant=None):
    return deepcopy(_expected_world_for_bytes(*_source_bytes()) if variant is None
                    else _cut_source(variant.source_loader()))


@lru_cache(maxsize=1)
def _expected_world_for_bytes(geometry_bytes, review_bytes):
    source = _source_for_bytes(geometry_bytes, review_bytes)
    return _cut_source(source)


def _cut_source(source):
    result = defaultdict(list)
    for name in NAMES:
        meta = source['route_metadata'][name]
        for order, row in enumerate(_split(source['routes'][name])):
            column, tile_row = row['cell']
            local = [(p[0]-16.*column, p[1]+16.*tile_row, p[2]) for p in row['points']]
            record = {**row, 'id': name, 'order': order, 'transport': 1,
                      'lane': meta['from_lane'], 'compatibility': 0,
                      'entry': _side(local[0]), 'exit': _side(local[-1])}
            result[row['cell']].append(record)
    return dict(result)


def _spec(piece, *, variant=None):
    key = _key(piece, variant=variant)
    keys = KEYS if variant is None else variant.keys
    reviewed_cells = OWNED_WORLD_CELLS if variant is None else dict(zip(keys, variant.owned_world_cells))
    engineering = piece.get('engineering', {})
    origin = engineering.get('world_origin_cell')
    require(isinstance(origin, list) and len(origin) == 2 and all(type(x) is int for x in origin),
            'Y component needs its reviewed world-origin cell')
    cells = list(map(tuple, piece.get('cells', [])))
    tiles = [int(tile, 16) for tile in piece.get('tile_ids', [])]
    require(cells and len(cells) == len(set(cells)) == len(tiles) == len(set(tiles)),
            'Y component ownership and canonical tile identifiers disagree')
    world = {(x+origin[0], y+origin[1]): local for local, (x, y) in zip(cells, cells)}
    expected_id = 'ddrhw-'+key if variant is None else variant.piece_ids[keys.index(key)]
    expected_recipe = 'highway_ddrhw_'+key.replace('-', '_') if variant is None else variant.recipes[keys.index(key)]
    require(piece['id'] == expected_id and piece['recipe'] == expected_recipe
            and set(world) == set(reviewed_cells[key]),
            'Y component changes its independently reviewed physical ownership or identity')
    require(origin == [min(c[k] for c in reviewed_cells[key]) for k in range(2)]
            and piece['footprint'] == [max(c[k] for c in cells)+1 for k in range(2)],
            'Y component changes its normalized origin or construction footprint')
    require(all(_owner(cell, variant=variant) == key for cell in world), 'Y component crosses another component ownership band')
    expected = {cell for cell in _expected_world(variant=variant) if _owner(cell, variant=variant) == key}
    require(expected <= set(world), 'Y component omits an owned traffic cell')
    empty = {world[cell] for cell in set(world)-expected}
    require(empty == set(map(tuple, engineering.get('model_only_cells', []))),
            'Y model-only cells differ from the actual independent traffic cuts')
    require(engineering.get('max_grade_percent') == 30.
            and engineering.get('car_corridor_half_width_m') == 1.25
            and engineering.get('car_corridor_height_m') == 3.8,
            'Y component changed its reviewed grade or vehicle bounds')
    require(piece.get('shadow_mappings') == [] and piece.get('model_shadows', {}).get('enabled') is False,
            'Y component must retain the selected no-custom-shadow policy')
    return tuple(origin), cells, tiles


def expected_cell_routes(piece, *, variant=None):
    origin, cells, _tiles = _spec(piece, variant=variant)
    result = {cell: [] for cell in cells}
    expected = _expected_world(variant=variant)
    for cell in cells:
        world = cell[0]+origin[0], cell[1]+origin[1]
        for row in expected.get(world, []):
            result[cell].append({**deepcopy(row), 'cell': cell,
                'points': [(p[0]-16.*world[0], p[1]+16.*world[1], p[2]) for p in row['points']]})
    return result


def _matches(actual, expected):
    return (all(actual[key] == expected[key] for key in ('transport', 'entry', 'exit', 'compatibility'))
            and len(actual['points']) == len(expected['points'])
            and all(math.dist(a, b) <= POSITION_EPS for a, b in zip(actual['points'], expected['points'])))


def _rotate(point, turns):
    east, north, height = point
    for _ in range(turns % 4):
        east, north = north, -east
    return east, north, height


def _endpoint(point):
    return tuple(round(value, 7) for value in point)


def _intrinsic_runs(piece, *, variant=None):
    origin, _cells, _tiles = _spec(piece, variant=variant)
    key = _key(piece, variant=variant)
    result = []
    expected = _expected_world(variant=variant)
    for name in NAMES:
        full = sorted((row for group in expected.values() for row in group if row['id'] == name),
                      key=lambda row: row['order'])
        runs, current = [], []
        for row in full:
            if _owner(row['cell'], variant=variant) == key:
                current.append(row)
            elif current:
                runs.append(current)
                current = []
        if current:
            runs.append(current)
        for index, run in enumerate(runs):
            identifier = name.lower()+(f'-{index+1}' if len(runs) > 1 else '')
            ends = []
            for direction, fragment, position, other in (('in', run[0], 0, 1), ('out', run[-1], -1, -2)):
                column, row = fragment['cell']
                encoded = [(float(format(p[0]-16.*column, '.9f'))+16.*column,
                            float(format(p[1]+16.*row, '.9f'))-16.*row,
                            float(format(p[2], '.9f'))) for p in fragment['points']]
                p = encoded[position]
                delta = tuple(encoded[other][k]-p[k] for k in range(3)) if direction == 'in' else tuple(
                    p[k]-encoded[other][k] for k in range(3))
                length = math.hypot(*delta[:2])
                # The public extractor retains a six-decimal graph alongside
                # the unrounded saved PATH. Reconstruct both independently
                # from the reviewed source, in the piece's local frame, using
                # the same declared encoding precision rather than candidate
                # measurements. The precise contract below remains unchanged.
                saved_local = [(float(format(point[0]-16.*column, '.9f'))+16.*(column-origin[0]),
                                float(format(point[1]+16.*row, '.9f'))-16.*(row-origin[1]),
                                float(format(point[2], '.9f'))) for point in fragment['points']]
                graph_local = [tuple(round(value, 6) for value in point) for point in saved_local]
                saved_delta = tuple(saved_local[other][k]-saved_local[position][k] for k in range(3)) if direction == 'in' else tuple(
                    saved_local[position][k]-saved_local[other][k] for k in range(3))
                graph_delta = tuple(graph_local[other][k]-graph_local[position][k] for k in range(3)) if direction == 'in' else tuple(
                    graph_local[position][k]-graph_local[other][k] for k in range(3))
                graph_length = math.hypot(*graph_delta[:2])
                precise_tangent = tuple(value/length for value in delta[:2])
                tangent_length = math.hypot(*precise_tangent)
                ends.append({'id': identifier+'-'+direction, 'channel_id': identifier, 'direction': direction,
                             'point_m': (p[0]-16.*origin[0], p[1]+16.*origin[1], p[2]),
                             'tangent': precise_tangent, 'grade': delta[2]/length,
                             'public_endpoint_m': graph_local[position],
                             'public_sampled_tangent': tuple(value/graph_length for value in graph_delta[:2]),
                             'public_tangent': tuple(value/tangent_length for value in precise_tangent),
                             'public_grade': round(saved_delta[2]/math.hypot(*saved_delta[:2]), 9),
                             'source_cell': [fragment['cell'][0]-origin[0], fragment['cell'][1]-origin[1]],
                             'edge': fragment['entry'] if direction == 'in' else fragment['exit']})
            result.append({'id': identifier, 'route': name, 'ports': ends, 'fragments': run})
    return result


def reviewed_contract(piece, *, variant=None):
    runs = _intrinsic_runs(piece, variant=variant)
    ports = [p for run in runs for p in run['ports']]
    return {'boundary_measurement_precision': 'saved-path',
            'ports': {p['id']: list(p['point_m']) for p in ports},
            'port_vectors': {p['id']: list(p['tangent']) for p in ports},
            'port_transports': {p['id']: 1 for p in ports},
            'port_directions': {p['id']: p['direction'] for p in ports},
            'movements': [[run['ports'][0]['id'], run['ports'][1]['id']] for run in runs]}


def reviewed_facts(piece, *, variant=None):
    runs = _intrinsic_runs(piece, variant=variant)
    ports = []
    for run in runs:
        for p in run['ports']:
            height = p['public_endpoint_m'][2]
            ports.append({'id': p['id'], 'direction': p['direction'], 'engine_transport': 1,
                'edge': p['edge'], 'endpoint_m': list(p['public_endpoint_m']),
                'sampled_tangent': list(p['public_sampled_tangent']),
                'tangent': list(p['public_tangent']), 'grade': p['public_grade'], 'service_network': 'road',
                'service_family': 'road', 'variant': 'dd-rhw-l1' if abs(height-7.5) <= 2e-5 else (
                    'dd-rhw-l2' if abs(height-15.) <= 2e-5 else 'access-ramp'),
                'role': 'primary', 'channel_kind': 'road-lane', 'traffic_modes': ['car'],
                'source_cell': p['source_cell'], 'channel_id': p['channel_id']})
    movements = [(run['ports'][0]['id'], run['ports'][1]['id']) for run in runs]
    return {'reference_piece_id': piece['id'], 'footprint': deepcopy(piece['footprint']),
        'cells': deepcopy(piece['cells']), 'path_hashes_by_cell': [],
        'raw_path_fingerprint_status': 'requires-checked-saved-build-freeze', 'ports': ports,
        'movements': movements, 'forbidden_transfers': [(a['id'], b['id']) for a in ports for b in ports
            if a['direction'] == 'in' and b['direction'] == 'out' and (a['id'], b['id']) not in movements],
        'components': [{'id': 'dd-highway', 'network': 'road', 'construction_network': 'dirtroad'}],
        'channels': [{'id': run['id'], 'component_id': 'dd-highway', 'kind': 'road-lane',
            'traffic_modes': ['car'], 'ports': [run['ports'][0]['id'], run['ports'][1]['id']]} for run in runs]}


def check_paths(resources, piece, *, variant=None):
    origin, cells, tiles = _spec(piece, variant=variant)
    expected = expected_cell_routes(piece, variant=variant)
    decoded, maximum, consumed, fragments = [], 0., set(), 0
    source = _source() if variant is None else variant.source_loader()
    global_ends = {_endpoint(points[index]) for points in source['routes'].values() for index in (0, -1)}
    for cell, tile in zip(cells, tiles):
        require((*PATH, tile) in resources, 'Missing Y canonical PATH resource')
        parsed = parse_paths(decompress(resources[*PATH, tile]))
        require(parsed['version'] == '1.2' and parsed['terrain'] == 1,
                'Y PATH must explicitly retain authored elevated traffic heights')
        remaining = list(expected[cell])
        classes = set()
        for actual in parsed['routes']:
            identity = actual['transport'], actual['entry'], actual['exit'], actual['lane']
            require(identity not in classes, 'Duplicate Y car class for the same directed tile-side pair')
            classes.add(identity)
            matches = [index for index, row in enumerate(remaining) if _matches(actual, row)]
            require(len(matches) == 1, 'Saved Y PATH differs from the independently cut source route')
            row = remaining.pop(matches[0])
            points = [(p[0]+16.*(cell[0]+origin[0]), p[1]-16.*(cell[1]+origin[1]), p[2]) for p in actual['points']]
            if any(_endpoint(points[index]) in global_ends for index in (0, -1)):
                require(actual['lane'] == row['lane'], 'Saved Y native endpoint changed its measured lane class')
            require(_side(actual['points'][0]) == actual['entry'] and _side(actual['points'][-1]) == actual['exit'],
                    'Saved Y PATH side flag differs from its actual owned boundary')
            for first, last in zip(points, points[1:]):
                distance = math.dist(first[:2], last[:2])
                require(distance > 1e-10, 'Stationary or vertical saved Y car segment')
                grade = 100.*abs(last[2]-first[2])/distance
                require(grade <= 30.+1e-5, 'Saved Y car PATH exceeds the thirty-percent grade bound')
                maximum = max(maximum, grade)
            decoded.append({**actual, 'points': points, 'source_id': row['id'], 'order': row['order']})
            consumed.add((row['id'], row['order']))
            fragments += 1
        require(not remaining, 'Saved Y cell omits a required real car route')
    rotations = []
    for turns in range(4):
        for run in _intrinsic_runs(piece, variant=variant):
            chain = sorted((row for row in decoded if row['source_id'] == run['route']
                            and (row['source_id'], row['order']) in {(p['id'], p['order']) for p in run['fragments']}),
                           key=lambda row: row['order'])
            require(len(chain) == len(run['fragments']), 'Saved Y intrinsic journey is disconnected')
            for a, b in zip(chain, chain[1:]):
                require(math.dist(_rotate(a['points'][-1], turns), _rotate(b['points'][0], turns)) <= POSITION_EPS,
                        'Saved Y rotated internal lane seam is disconnected')
        rotations.append({'quarter_turns_clockwise': turns, 'intrinsic_journeys': len(_intrinsic_runs(piece, variant=variant))})
    return {'passed': True, 'actual_saved_route_fragments': fragments, 'owned_cells': len(cells),
            'intrinsic_journeys': len(_intrinsic_runs(piece, variant=variant)), 'maximum_grade_percent': maximum,
            'use_path_elevation': True, 'native_lane_classes_preserved': True,
            'model_only_cells': deepcopy(piece['engineering']['model_only_cells']),
            'proper_rotations': rotations, 'game_operation_tested': False}


def _construction_flags(records):
    sides = [0, 0, 0, 0]
    for row in records:
        for side, a, b in ((row['entry'], row['points'][0], row['points'][1]),
                           (row['exit'], row['points'][-2], row['points'][-1])):
            dx, dy = b[0]-a[0], b[1]-a[1]
            if abs(dx) < 1e-7 or abs(dy) < 1e-7:
                value = 2
            elif side in (1, 3):
                value = 3 if dx*dy > 0. else 1
            else:
                value = 1 if dx*dy > 0. else 3
            sides[side] = 2 if 2 in (value, sides[side]) else value
    return sum(value << (8*index) for index, value in enumerate(sides))


def check_construction_fields(fields, piece, resources, *, variant=None, native_checker=None):
    if native_checker is None:
        from .y_junction_approaches import check_construction_approaches
    else:
        check_construction_approaches = native_checker
    fields = check_construction_approaches(fields, piece)
    _origin, cells, tiles = _spec(piece, variant=variant)
    layout = fields['CellLayout']
    cons = fields['ConsLayout']
    require(len(layout) == len(cons) and all(len(a) == len(b) for a, b in zip(layout, cons)),
            'Y construction and owned-cell grids differ')
    palette = {}
    for line in fields['CheckType']:
        symbol, rest = line.split(' - ', 1)
        require(rest.startswith('dirtroad: 0x'), 'Y construction must use its saved real-road flags')
        palette[symbol] = int(rest.split('0x', 1)[1], 16)
    owners = {(x, y): symbol for y, row in enumerate(layout) for x, symbol in enumerate(row)
              if symbol not in '.<>^'}
    require(set(owners) == set(cells), 'Y construction writes cells outside its declared ownership')
    for cell, tile in zip(cells, tiles):
        require(cons[cell[1]][cell[0]] == '+', 'Y owned cell lost its actual construction marker')
        flags = _construction_flags(parse_paths(decompress(resources[*PATH, tile]))['routes'])
        require(palette.get(owners[cell]) == flags, 'Y construction flags disagree with actual saved traffic')
    require(len({int(tile, 16) for tile in piece['tile_ids']}) == len(cells), 'Y runtime cell addresses collide')
    return {'passed': True, 'owned_construction_cells': len(cells), 'actual_saved_flags_checked': True,
            'native_helpers_checked_separately': True, 'game_operation_tested': False}


def check_models(resources, piece, donors=None):
    from .y_junction_models_verify import check_models as inspect_models
    return inspect_models(resources, piece, donors)


def check_assembly(pieces, resources_by_id, scene, donors=None, *, variant=None):
    """Inspect the three actual placed owners and all six complete journeys."""
    by_id = {piece['id']: piece for piece in pieces}
    require(len(by_id) == len(pieces) == 3 and {_key(piece, variant=variant) for piece in pieces}
            == set(KEYS if variant is None else variant.keys),
            'Y assembly must contain exactly its three distinct reviewed components')
    placements = scene['placements']
    require(len(placements) == 3 and {p['piece_id'] for p in placements} == set(by_id),
            'Y assembly placement plan omits or repeats a component')
    owned, routes, reports = {}, [], {}
    for placed in placements:
        piece = by_id[placed['piece_id']]
        origin, cells, tiles = _spec(piece, variant=variant)
        require(placed.get('rotation_degrees_ccw', placed.get('rotation_degrees', 0)) == 0
                and placed['origin_m'] == [16.*origin[0], -16.*origin[1]],
                'Y assembly moved a component away from its reviewed source pose')
        resources = resources_by_id[piece['id']]
        reports[piece['id']] = check_paths(resources, piece, variant=variant)
        for cell, tile in zip(cells, tiles):
            world = cell[0]+origin[0], cell[1]+origin[1]
            require(world not in owned, 'Y assembly overwrites another component traffic or model cell')
            owned[world] = piece['id']
            parsed = parse_paths(decompress(resources[*PATH, tile]))
            for row in parsed['routes']:
                routes.append({**row, 'cell': world, 'points': [
                    (p[0]+16.*world[0], p[1]-16.*world[1], p[2]) for p in row['points']]})
    require(not {(-2, 2), (-2, -2), (4, 0)} & set(owned),
            'Y assembly overwrites an unowned native external helper cell')
    rotations = []
    for turns in range(4):
        graph = defaultdict(list)
        for index, route in enumerate(routes):
            graph[_endpoint(_rotate(route['points'][0], turns))].append(index)
        consumed, witnesses = set(), []
        for name in NAMES:
            expected = (_source() if variant is None else variant.source_loader())['routes'][name]
            start, end = _endpoint(_rotate(expected[0], turns)), _endpoint(_rotate(expected[-1], turns))
            node, visited = start, []
            while node != end:
                require(len(graph[node]) == 1, 'Saved Y complete journey has a missing or ambiguous continuation')
                index = graph[node][0]
                require(index not in visited, 'Saved Y complete journey contains a loop')
                visited.append(index)
                node = _endpoint(_rotate(routes[index]['points'][-1], turns))
            require(visited and not consumed.intersection(visited), 'Y complete journeys improperly share encoded lane paths')
            consumed.update(visited)
            witnesses.append({'journey': name, 'fragments': len(visited), 'native_start': list(start), 'native_end': list(end)})
        require(len(consumed) == len(routes), 'Y assembly has extra, disconnected, or forbidden traffic routes')
        rotations.append({'quarter_turns_clockwise': turns, 'complete_journeys': witnesses,
                          'all_saved_fragments_consumed': len(consumed)})
    return {'passed': True, 'component_path_reports': reports, 'occupied_cells': len(owned),
            'complete_directed_journeys': 6, 'complete_native_members': 12,
            'no_uturn_or_unintended_lane_transfer': True, 'proper_rotations': rotations,
            'game_operation_tested': False}
