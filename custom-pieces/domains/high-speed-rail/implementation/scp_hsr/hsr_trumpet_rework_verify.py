"""Independent scope and fixed-seam controls for the authorized trumpet redesign.

Only hashes and reviewed geometric facts from baseline086d33b are retained.
No obsolete piece definition, DAT, or predecessor source folder is loaded.
"""
from __future__ import annotations

import hashlib
import heapq
import json
import math
from pathlib import Path

from scp.dbpf import require

BASELINE_COMMIT = '086d33bc276a21fe31693456d490f7a5b44725d9'
BASELINE_ATOMIZATION_HISTORY = '616e7daadab6a141e84a615f64bfcf8bc3e7fee06f7129d41e57c5b09f3eaa73'
BASELINE_LAYOUT = '7d230df3d8697640ed5b197f448e041abd75cab62be2a9886562e4fc52909ee6'
CURRENT_LAYOUT = '46ae93230a5fc56f8471780cdd9aff94c8ebdb697ab299b9c0dffbbf106d9411'
UNCHANGED_WORLD_SHA256 = '868188775970987d31234974a833e9c1e0135db33d5fa202c521cfe86d8ab898'
UNCHANGED_SUPPORTS_SHA256 = 'b798566058c682faf5dde311a34be33226984f61af761409bce6c6f79023ac91'
PRESERVED_JOURNEYS_SHA256 = '38e8b11748b6a85c8647fe6cf34a0c0c82bd728155f0c5f73856e738c81e6ec1'
UNCHANGED_ARCHIVES_SHA256 = '44070ac64c2d3167ca9cb118e38e8ca683ff9440817bf82490dc6e0932c89f46'
REWORKED_BASELINE_JOURNEYS_SHA256 = '8d0132bdbd7553795bfcc24c5e23def0bce94a3185f38be15c08e6cb243fa266'
ROUTE_MOVEMENT_POLICY = {
    'movements': [['E_in', 'S_out'], ['S_in', 'W_out']],
    'maximum_symmetric_continuous_distance_m': 6.,
    'independent_bound_basis': 'The independently fixed socket translation is 5.835829856 m; the authorized envelope was rounded upward to 6.0 m before measuring the redesigned routes.',
    'fixed_socket_translation_m': 5.835829856,
    'fixed_socket_translation_facts': [
        {'historical_join': ['P03C', 'P03A'],
         'historical_source_geometry_sha256': 'a84008816db7f0b100446608c6bde8d5bc1440c075ca99948edc84e81c51ee52',
         'before_world_east_north_height_m': [143.43731130358895, 8., 15.5],
         'after_world_east_north_height_m': [137.60148144778314, 8., 15.5]},
        {'historical_join': ['P03A', 'P03B'],
         'historical_source_geometry_sha256': '42ce9230a30a536d358db4a6b5f3137ab38e19b3c33836293c074836b17ff833',
         'before_world_east_north_height_m': [80.56268869641104, 8., 15.5],
         'after_world_east_north_height_m': [86.39851855221686, 8., 15.5]},
    ],
    'enclosure_tolerance_m': .0001,
    'floating_point_guard_m': 1e-8,
    'method': 'Continuous symmetric Hausdorff distance between complete decoded 3D PATH polylines; adaptive segment subdivision uses the 1-Lipschitz point-to-polyline distance bound, with a 1e-8 m floating-point guard.',
    'additional_controls': 'The 24-cell authorization, fixed outside ports and branch sockets, unchanged 85 cells and four journeys, and existing radius, curvature, clearance, and support controls all remain mandatory.',
}
REWORKED_SOURCES = {
    'hsr-component-l2-paired-fan-compact-join': 'aee65b48c132692063d6bd2845772403a078850d1cdc2cbca11762d5a6ca7696',
    'hsr-component-l2-short-opposed-merge-core': '42ce9230a30a536d358db4a6b5f3137ab38e19b3c33836293c074836b17ff833',
}
ALLOWED_CELLS = frozenset({
    (32., 0.), (48., 0.), (64., 0.), (64., 16.), (80., 0.), (80., 16.),
    (96., 0.), (96., 16.), (96., 32.), (96., 48.), (112., 16.), (112., 32.),
    (112., 48.), (112., 64.), (112., 80.), (128., 0.), (128., 16.),
    (128., 32.), (128., 48.), (144., 0.), (144., 16.), (160., 0.),
    (160., 16.), (176., 0.),
})
CURRENT_REGION_SUPPORTS = [[32., 0.], [48., 0.], [64., 0.], [80., 0.], [96., 0.], [96., 16.],
                           [112., 32.], [112., 48.], [112., 64.], [112., 80.], [128., 0.],
                           [128., 16.], [144., 0.], [160., 0.], [176., 0.]]
REMOVABLE_STRUCTURAL_CELLS = frozenset({(96., 48.), (128., 48.), (64., 16.), (160., 16.)})
# These targets follow the retained core's measured branch, not the fan writer.
TARGET_JOINS = [
    {'from_placement': 'P08', 'to_placement': 'P06',
     'endpoint_m': [137.60148144778314, 8., 15.5],
     'travel_tangent': [-.9272548089645606, .37443092721100973]},
    {'from_placement': 'P06', 'to_placement': 'P07',
     'endpoint_m': [86.39851855221686, 8., 15.5],
     'travel_tangent': [-.9272548089645606, -.37443092721100973]},
]


def canonical_sha256(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def read_rework_record(path, *, root, require_completed=True):
    """Validate immutable baseline evidence and exact authorized change scope."""
    record = json.loads(Path(path).read_text())
    require(record.get('schema_version') == 1 and record.get('assembly_id') == 'straight-stem-trumpet'
            and record.get('baseline_commit') == BASELINE_COMMIT
            and record.get('baseline_layout_sha256') == BASELINE_LAYOUT
            and record.get('baseline_atomization_history_sha256') == BASELINE_ATOMIZATION_HISTORY,
            'Trumpet redesign baseline identity differs')
    allowed = record.get('allowed_world_cells_east_north_m', [])
    require(len(allowed) == 24 and set(map(tuple, allowed)) == ALLOWED_CELLS,
            'Trumpet redesign expands or changes its authorized 24-cell region')
    cells, archives = record['unchanged_world_cells'], record['unchanged_piece_archives']
    require(len(cells) == 85 and canonical_sha256(cells) == UNCHANGED_WORLD_SHA256,
            'Trumpet redesign unchanged 85-cell baseline was altered')
    require(len(archives) == 11 and canonical_sha256(archives) == UNCHANGED_ARCHIVES_SHA256,
            'Trumpet redesign unchanged 11-type baseline was altered')
    require(canonical_sha256(record.get('unchanged_support_positions_east_north_m')) == UNCHANGED_SUPPORTS_SHA256
            and record.get('current_reworked_support_positions_east_north_m') == CURRENT_REGION_SUPPORTS,
            'Trumpet redesign support plan or unchanged support baseline differs')
    require(canonical_sha256(record.get('preserved_journeys')) == PRESERVED_JOURNEYS_SHA256,
            'Trumpet redesign preserved mainline/direct-slip baseline differs')
    require(canonical_sha256(record.get('baseline_reworked_journeys')) == REWORKED_BASELINE_JOURNEYS_SHA256,
            'Trumpet redesign frozen affected-route baseline differs')
    require(record.get('route_movement_policy') == ROUTE_MOVEMENT_POLICY,
            'Trumpet redesign independent route-movement envelope differs')
    removed = record.get('removed_world_cells_east_north_m', [])
    require(len(removed) == len(set(map(tuple, removed)))
            and set(map(tuple, removed)) <= REMOVABLE_STRUCTURAL_CELLS,
            'Trumpet redesign removes an unauthorized structural cell')
    require(record.get('fixed_target_joins') == TARGET_JOINS,
            'Trumpet redesign fixed target joins or branch angles differ')
    sources = record.get('source_geometry', {})
    require(set(sources) == set(REWORKED_SOURCES), 'Trumpet redesign changes an unauthorized source type')
    for identifier, before in REWORKED_SOURCES.items():
        binding = sources[identifier]
        require(binding.get('before_sha256') == before,
                'Trumpet redesign historical source binding differs')
        if require_completed:
            actual = hashlib.sha256((Path(root)/'domains/high-speed-rail/00_pieces'/identifier/'geometry.json').read_bytes()).hexdigest()
            require(binding.get('after_sha256') == actual,
                    'Trumpet redesign current geometry differs from its independently audited source')
    if require_completed:
        audit_removed_cell_evidence(record)
        require(record.get('status') == 'passed' and record.get('compiled_audit'),
                'Trumpet redesign requires an actual completed compiled-resource audit')
        audit_recorded_route_movement(record.get('compiled_route_movement'))
    return record


def audit_redesign_scope(tiles, build, record):
    """Preserve all85 unmodified world cells and all11 unmodified type DATs."""
    expected = {tuple(item['world_east_north_m']): item for item in record['unchanged_world_cells']}
    removed = set(map(tuple, record.get('removed_world_cells_east_north_m', [])))
    current_region = ALLOWED_CELLS - removed
    require(set(tiles) == set(expected) | current_region,
            'Trumpet redesign occupied world cells differ from the approved change scope')
    region = {position for position, tile in tiles.items() if tile['instance_id'] in ('P06', 'P07', 'P08', 'P26')}
    require(region == current_region, 'Trumpet redesigned placements leave their authorized 24-cell region')
    for position, baseline in expected.items():
        tile = tiles[position]
        require(tile['piece_id'] == baseline['piece_id'] and list(tile['cell']) == baseline['cell']
                and tile['rotation'] == baseline['rotation_quarter_turns_ccw'],
                f'Trumpet redesign changed an unaffected tile owner or pose at {position}')
        hashes = {name: hashlib.sha256(raw).hexdigest() for name, raw in tile['resources'].items()}
        require(hashes == baseline['resources_sha256'],
                f'Trumpet redesign changed resources outside its authorized region at {position}')
    for baseline in record['unchanged_piece_archives']:
        spec = build['pieces'].get(baseline['id'])
        require(spec is not None and spec['recipe'] == baseline['recipe'] and spec['asset_file'] == baseline['asset_file'],
                'Trumpet redesign changed an unaffected type identity')
        raw = (build['path']/spec['asset_file']).read_bytes()
        require(len(raw) == baseline['bytes'] and hashlib.sha256(raw).hexdigest() == baseline['sha256'],
                'Trumpet redesign changed an unaffected type archive: '+baseline['id'])
    return {'allowed_changed_world_cells': 24, 'current_reworked_world_cells': len(current_region),
            'removed_structural_world_cells': sorted(map(list, removed)), 'unchanged_world_cells_preserved_byte_for_byte': 85,
            'unchanged_type_archives_preserved_byte_for_byte': 11,
            'baseline_commit': BASELINE_COMMIT, 'obsolete_resources_required': False}


def audit_target_joins(records):
    """Inspect actual encoded neighbours at both independently fixed sockets."""
    checked = []
    for target in TARGET_JOINS:
        endpoint = tuple(round(value, 6) for value in target['endpoint_m'])
        outgoing = [points for _, metadata, points in records
                    if metadata['instance_id'] == target['from_placement'] and points[-1] == endpoint]
        incoming = [points for _, metadata, points in records
                    if metadata['instance_id'] == target['to_placement'] and points[0] == endpoint]
        require(len(outgoing) == len(incoming) == 1,
                'Trumpet redesigned socket misses its fixed directed target join')
        for a, b in ((outgoing[0][-2], outgoing[0][-1]), (incoming[0][0], incoming[0][1])):
            run = math.dist(a[:2], b[:2])
            require(run > 0. and abs(b[2]-a[2]) <= 2e-6,
                    'Trumpet redesigned socket has a missing or nonflat endpoint chord')
            tangent = ((b[0]-a[0])/run, (b[1]-a[1])/run)
            require(math.dist(tangent, target['travel_tangent']) <= 2e-5,
                    'Trumpet redesigned socket heading differs from the retained core branch angle')
        checked.append(dict(target))
    return {'fixed_branch_joins_checked': checked, 'endpoint_tolerance_m': 2e-6,
            'unit_travel_tangent_tolerance': 2e-5, 'expected_targets_from_unchanged_reusable_core': True}


def audit_preserved_journeys(journeys, record):
    """Normalize straight subdivisions only; preserve every actual direct-slip bend."""
    from .hsr_mesh_verify import _coalesce_grid_cuts

    for baseline in record['preserved_journeys']:
        movement = tuple(baseline['movement'])
        require(movement in journeys, 'Trumpet redesign omits an unchanged directed journey')
        points = _coalesce_grid_cuts(journeys[movement])
        require(len(points) == baseline['coalesced_encoded_points']
                and canonical_sha256(points) == baseline['coalesced_points_sha256'],
                'Trumpet redesign changes preserved mainline or direct-slip geometry: '+str(movement))
    return {'unchanged_complete_journeys': 4, 'unchanged_direct_slips': 2,
            'normalization': record['journey_normalization']}


def _segment_tree(points):
    """Spatial bounds accelerate nearest-segment queries without sampling curves."""
    segments = [(a, b) for a, b in zip(points, points[1:]) if a != b]
    require(segments, 'Route displacement needs a nondegenerate target polyline')

    def node(items):
        lower = tuple(min(min(a[k], b[k]) for a, b in items) for k in range(3))
        upper = tuple(max(max(a[k], b[k]) for a, b in items) for k in range(3))
        if len(items) <= 8:
            return lower, upper, items, None
        axis = max(range(3), key=lambda k: upper[k]-lower[k])
        items.sort(key=lambda item: item[0][axis]+item[1][axis])
        middle = len(items)//2
        return lower, upper, None, (node(items[:middle]), node(items[middle:]))
    return node(segments)


def _distance_to_polyline(point, tree):
    """Return the actual closest point on continuous target segments."""
    guard = ROUTE_MOVEMENT_POLICY['floating_point_guard_m']
    best, closest = float('inf'), None

    def box_distance(node):
        return math.sqrt(sum(max(lo-value, 0., value-hi)**2
                             for value, lo, hi in zip(point, node[0], node[1])))

    def search(node):
        nonlocal best, closest
        if box_distance(node) > best+guard:
            return
        if node[2] is not None:
            for a, b in node[2]:
                delta = tuple(y-x for x, y in zip(a, b))
                length2 = sum(value*value for value in delta)
                fraction = min(1., max(0., sum((value-origin)*step for value, origin, step
                                              in zip(point, a, delta))/length2))
                candidate = tuple(origin+fraction*step for origin, step in zip(a, delta))
                distance = math.dist(point, candidate)
                if distance < best:
                    best, closest = distance, candidate
        else:
            children = sorted(node[3], key=box_distance)
            search(children[0]); search(children[1])
    search(tree)
    return best, closest


def _directed_continuous_distance(source, target, *, tolerance):
    """Enclose the maximum over every source segment, including its interior.

    Distance to a fixed closed set is 1-Lipschitz. If an interval has length L
    and endpoint distances d0 and d1, its distance is at most (d0+d1+L)/2.
    Subdivision tightens this analytic bound. Double precision is used, with
    a conservative 1e-8 m guard and coordinates restricted to 10,000 m; this
    is a numerical enclosure, not a claim of exact symbolic arithmetic.
    """
    guard = ROUTE_MOVEMENT_POLICY['floating_point_guard_m']
    require(4.*guard <= tolerance <= ROUTE_MOVEMENT_POLICY['enclosure_tolerance_m'],
            'Route displacement enclosure tolerance is outside its guarded numerical range')
    require(all(len(p) == 3 and all(math.isfinite(v) and abs(v) <= 10000. for v in p)
                for p in [*source, *target]), 'Route displacement coordinates exceed the numerical guard scope')
    require(len(source) >= 2 and len(target) >= 2, 'Route displacement needs complete polylines')
    if list(map(tuple, source)) == list(map(tuple, target)):
        return {'lower_bound_m': 0., 'upper_bound_m': guard, 'sampled_points': 0,
                'adaptive_subdivisions': 0, 'lower_bound_witness': None,
                'exact_identical_polyline': True}
    tree = _segment_tree(target)
    samples = {}
    lower, witness = 0., None

    def sample(point):
        nonlocal lower, witness
        point = tuple(point)
        if point not in samples:
            distance, closest = _distance_to_polyline(point, tree)
            samples[point] = distance
            if witness is None or distance-guard > lower:
                lower = max(0., distance-guard)
                witness = {'source_point_east_north_height_m': list(point),
                           'closest_target_point_east_north_height_m': list(closest),
                           'sampled_distance_m': distance}
        return samples[point]

    queue, serial = [], 0
    def interval(a, b, da, db):
        nonlocal serial
        upper = (da+db+math.dist(a, b))/2.+2.*guard
        if upper > lower:
            heapq.heappush(queue, (-upper, serial, a, b, da, db)); serial += 1
    distances = [sample(point) for point in source]
    for a, b, da, db in zip(source, source[1:], distances, distances[1:]):
        interval(tuple(a), tuple(b), da, db)
    subdivisions = 0
    while queue and -queue[0][0] > lower+tolerance:
        _, _, a, b, da, db = heapq.heappop(queue)
        middle = tuple((x+y)/2. for x, y in zip(a, b))
        require(middle != a and middle != b,
                'Route displacement subdivision exhausted floating-point resolution')
        dm = sample(middle); subdivisions += 1
        interval(a, middle, da, dm); interval(middle, b, dm, db)
    return {'lower_bound_m': lower, 'upper_bound_m': max(lower, -queue[0][0] if queue else lower),
            'sampled_points': len(samples), 'adaptive_subdivisions': subdivisions, 'lower_bound_witness': witness}


def continuous_symmetric_distance(before, after, *, tolerance=.0001):
    """Bound the continuous symmetric Hausdorff distance, not just vertices."""
    forward = _directed_continuous_distance(before, after, tolerance=tolerance)
    reverse = _directed_continuous_distance(after, before, tolerance=tolerance)
    return {'lower_bound_m': max(forward['lower_bound_m'], reverse['lower_bound_m']),
            'upper_bound_m': max(forward['upper_bound_m'], reverse['upper_bound_m']),
            'before_to_after': forward, 'after_to_before': reverse}


def audit_recorded_route_movement(report):
    require(isinstance(report, dict) and report.get('policy') == ROUTE_MOVEMENT_POLICY,
            'Trumpet redesign lacks its independent route-movement measurement')
    routes = report.get('journeys', [])
    require([item.get('movement') for item in routes] == ROUTE_MOVEMENT_POLICY['movements'],
            'Trumpet redesign route-movement measurement omits an affected northern journey')
    for item in routes:
        lower, upper = item.get('lower_bound_m', -1.), item.get('upper_bound_m', float('inf'))
        require(0. <= lower <= upper <= ROUTE_MOVEMENT_POLICY['maximum_symmetric_continuous_distance_m']
                and upper-lower <= ROUTE_MOVEMENT_POLICY['enclosure_tolerance_m']+1e-10,
                'Trumpet redesign exceeds its independent 6.0 m continuous route-movement envelope')
    require(report.get('maximum_lower_bound_m') == max(item['lower_bound_m'] for item in routes)
            and report.get('maximum_upper_bound_m') == max(item['upper_bound_m'] for item in routes),
            'Trumpet redesign route-movement summary differs from its measured bounds')
    return report


def audit_matching_route_movement(current, accepted):
    """Require identical encoded routes and overlapping numerical enclosures.

    Exact raw PATH hashes preserve the geometry. Independently valid bounds
    may differ in their last floating-point bits on another contributor's
    platform; comparison therefore uses their intervals, not float equality.
    """
    audit_recorded_route_movement(current); audit_recorded_route_movement(accepted)
    guard = ROUTE_MOVEMENT_POLICY['floating_point_guard_m']
    for actual, baseline in zip(current['journeys'], accepted['journeys']):
        require(all(actual.get(key) == baseline.get(key) for key in
                    ('movement', 'baseline_points_sha256', 'current_points_sha256'))
                and max(actual['lower_bound_m'], baseline['lower_bound_m'])
                    <= min(actual['upper_bound_m'], baseline['upper_bound_m'])+2.*guard,
                'Trumpet saved route movement differs from its compiled redesign proof')
    return current


def audit_route_movement(journeys, record):
    """Compare both complete changed northern journeys with frozen saved PATHs."""
    require(canonical_sha256(record.get('baseline_reworked_journeys')) == REWORKED_BASELINE_JOURNEYS_SHA256,
            'Trumpet redesign frozen affected-route baseline differs')
    routes = []
    for baseline in record['baseline_reworked_journeys']:
        movement = tuple(baseline['movement'])
        require(movement in journeys, 'Trumpet redesign omits an affected northern journey')
        before, after = baseline['points_east_north_height_m'], journeys[movement]
        require(canonical_sha256(before) == baseline['points_sha256'] and len(before) == baseline['encoded_points'],
                'Trumpet frozen baseline route facts differ')
        routes.append({'movement': list(movement), 'baseline_points_sha256': baseline['points_sha256'],
                       'current_points_sha256': canonical_sha256(after),
                       **continuous_symmetric_distance(before, after)})
    report = {'policy': ROUTE_MOVEMENT_POLICY, 'journeys': routes,
              'maximum_lower_bound_m': max(item['lower_bound_m'] for item in routes),
              'maximum_upper_bound_m': max(item['upper_bound_m'] for item in routes),
              'baseline_source': 'Frozen decoded saved PATH facts from the accepted baseline; no predecessor files are read.'}
    return audit_recorded_route_movement(report)


def audit_redesign_supports(supports, record):
    expected = record['unchanged_support_positions_east_north_m'] + CURRENT_REGION_SUPPORTS
    require(len(supports) == len(set(supports)) == len(expected) == 74
            and set(supports) == set(map(tuple, expected)),
            'Trumpet redesign support positions differ from the explicit 74-pier plan')
    minimum = min(math.dist(a, b) for i, a in enumerate(supports) for b in supports[:i])
    require(minimum >= 16.-2e-6, 'Trumpet global pier spacing is below 16 m')
    return {'total_column_positions': 74, 'unchanged_support_positions': 59,
            'reworked_region_support_positions': 15, 'minimum_global_centre_spacing_m': minimum}


def audit_removed_cell_evidence(record):
    """Validate recorded proof from a valid DAT, never nonexistent empty S3Ds."""
    removed = set(map(tuple, record.get('removed_world_cells_east_north_m', [])))
    if not removed:
        return {'removed_cells_proved_empty': 0}
    proof = record.get('removed_cell_proof', {})
    def valid_hash(value):
        return isinstance(value, str) and len(value) == 64 and all(c in '0123456789abcdef' for c in value)
    require(all(valid_hash(proof.get(key)) for key in ('source_fan_geometry_sha256',
            'source_build_manifest_sha256', 'source_dat_sha256')),
            'Trumpet removed cells need exact actual-native build/source fingerprints')
    cells = proof.get('cells', [])
    require(len(cells) == len(removed) and {tuple(item['world_east_north_m']) for item in cells} == removed,
            'Trumpet removed structural cells lack their exact actual-native proof')
    require(proof.get('projection_rule') == 'No positive 3D surface area or X/Z projection inside the open removed tile; exact tile borders are allowed.',
            'Trumpet removed-cell projection rule differs')
    require(isinstance(proof.get('checked_model_resources'), list) and proof['checked_model_resources']
            and all(valid_hash(item.get('sha256')) for item in proof['checked_model_resources']),
            'Trumpet empty-cell proof omits the actual saved model fingerprints')
    for item in cells:
        column, row = item['local_cell']
        require([64.+16.*column, 80.-16.*row] == item['world_east_north_m']
                and item.get('positive_area_intersections_by_zoom') == [0]*5
                and item.get('preview_positive_area_intersections') == 0
                and item.get('positive_surface_intersections_by_zoom') == [0]*5
                and item.get('preview_positive_surface_intersections') == 0
                and item.get('path_source_cell_absent') is True
                and item.get('owned_support_absent') is True,
                'Trumpet removed structural cell contains saved geometry, a PATH source cell, or a support')
    return {'removed_cells_proved_empty': len(removed), 'all_five_actual_native_model_zooms_checked': True}


def _clip_to_open_tile(triangle, bounds, axes):
    """Clip actual vertices; a polygon lying on a tile border has no interior."""
    west, south, east, north = bounds
    x_axis, z_axis = axes
    if (max(p[x_axis] for p in triangle) <= west or min(p[x_axis] for p in triangle) >= east
            or max(p[z_axis] for p in triangle) <= south or min(p[z_axis] for p in triangle) >= north):
        return []
    polygon = list(triangle)
    for axis, boundary, sign in ((x_axis, west, 1), (x_axis, east, -1),
                                  (z_axis, south, 1), (z_axis, north, -1)):
        output = []
        if not polygon:
            return []
        previous = polygon[-1]
        before = sign*(previous[axis]-boundary)
        for current in polygon:
            after = sign*(current[axis]-boundary)
            if (before >= 0.) != (after >= 0.):
                fraction = before/(before-after)
                point = [previous[k]+fraction*(current[k]-previous[k]) for k in range(len(previous))]
                point[axis] = boundary
                output.append(tuple(point))
            if after >= 0.:
                output.append(current)
            previous, before = current, after
        polygon = output
    if len(set(polygon)) < 3:
        return []
    if any(all(point[axis] == boundary for point in polygon)
           for axis, boundary in ((x_axis, west), (x_axis, east), (z_axis, south), (z_axis, north))):
        return []
    return polygon


def _projected_tile_intersection_area(triangle, bounds):
    """Measure positive X/Z projection inside an open tile."""
    polygon = _clip_to_open_tile(triangle, bounds, (0, 1))
    if not polygon:
        return 0.
    west, south, _, _ = bounds
    polygon = [(x-west, z-south) for x, z in polygon]
    return abs(math.fsum(a[0]*b[1]-b[0]*a[1]
                        for a, b in zip(polygon, polygon[1:]+polygon[:1])))/2.


def _tile_intersection_surface_area(triangle, bounds):
    """Retain vertical faces: zero X/Z area does not mean an empty saved tile."""
    polygon = _clip_to_open_tile(triangle, bounds, (0, 2))
    if not polygon:
        return 0.
    first = polygon[0]
    areas = []
    for a, b in zip(polygon[1:], polygon[2:]):
        u = tuple(a[k]-first[k] for k in range(3))
        v = tuple(b[k]-first[k] for k in range(3))
        cross = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
        areas.append(math.sqrt(sum(value*value for value in cross))/2.)
    return math.fsum(areas)


def prove_removed_structural_cells(build, record, *, root):
    """Inspect every actual saved fan model zoom and its complete preview.

    Source-cell omission alone is insufficient. This reads only a valid final
    DAT and checks the saved geometry against each independently named tile.
    It never fabricates empty S3D resources or treats a packing error as proof.
    """
    import struct
    from scp.models import parse_s3d
    from scp.render_meshes import _triangles

    removed = sorted(map(tuple, record.get('removed_world_cells_east_north_m', [])))
    if not removed:
        return None
    identifier = 'hsr-component-l2-paired-fan-compact-join'
    spec = build['pieces'][identifier]
    saved = build['resources'](spec)
    resources = saved['resources']
    cells = []
    for east, north in removed:
        local = (int((east-64.)/16.), int((80.-north)/16.))
        require([east, north] == [64.+16.*local[0], 80.-16.*local[1]]
                and list(local) not in spec['cells'],
                'Trumpet removed structural cell is still owned by the compiled fan')
        iid = 0x7f580000+0x100*local[0]+0x10*local[1]
        require((0x296678f7, 0xa966883f, iid) not in resources,
                'Trumpet removed structural cell retains an actual PATH resource')
        for support_east, support_north in spec['component']['support_centers']:
            owner = (math.floor((support_east+8.)/16.), math.floor((-support_north+8.)/16.))
            require(owner != local, 'Trumpet removed structural cell still owns a support')
        cells.append({'local_cell': list(local), 'world_east_north_m': [east, north],
            'positive_area_intersections_by_zoom': [0]*5, 'preview_positive_area_intersections': 0,
            'positive_surface_intersections_by_zoom': [0]*5, 'preview_positive_surface_intersections': 0,
            'path_source_cell_absent': True, 'owned_support_absent': True})
    models = []
    for cell, tile in zip(spec['cells'], spec['tile_ids']):
        for zoom in range(5):
            models.append((int(tile, 16)+zoom, zoom, 16.*cell[0], 16.*cell[1], False))
    models.append((int(spec['preview_id'], 16), 0, 0., 0., True))
    require({key for key in resources if key[0] == 0x5ad0e817}
            == {(0x5ad0e817, 0xbadb57f1, iid) for iid, *_ in models},
            'Trumpet fan DAT includes an unexpected model outside its exact saved-cell inventory')
    checked_models = []
    for iid, zoom, east, south, preview in models:
        raw = resources[0x5ad0e817, 0xbadb57f1, iid]
        model = parse_s3d(raw)
        count = 0
        for mesh in model['meshes']:
            for frame in set(tuple(item) for item in mesh['frames']):
                for raw_triangle in _triangles(model, frame):
                    points = [struct.unpack_from('<3f', vertex) for vertex in raw_triangle]
                    world = [(p[0]+east, p[1], p[2]+south) for p in points]
                    projected = [(p[0], p[2]) for p in world]
                    count += 1
                    for cell in cells:
                        column, row = cell['local_cell']
                        bounds = (16.*column-8., 16.*row-8., 16.*column+8., 16.*row+8.)
                        area = _projected_tile_intersection_area(projected, bounds)
                        require(area == 0.,
                                f'Trumpet saved fan model {iid:08x} zoom {zoom} projects {area:.12g} m2 into removed structural cell {cell["local_cell"]}')
                        surface_area = _tile_intersection_surface_area(world, bounds)
                        require(surface_area == 0.,
                                f'Trumpet saved fan model {iid:08x} zoom {zoom} has {surface_area:.12g} m2 of surface inside removed structural cell {cell["local_cell"]}')
        checked_models.append({'resource_id': f'5ad0e817-badb57f1-{iid:08x}', 'zoom': zoom,
            'preview': preview, 'triangles_checked': count, 'sha256': hashlib.sha256(raw).hexdigest()})
    geometry_path = Path(root)/'domains/high-speed-rail/00_pieces'/identifier/'geometry.json'
    return {'source_fan_geometry_sha256': hashlib.sha256(geometry_path.read_bytes()).hexdigest(),
            'source_build_manifest_sha256': build['manifest_sha256'], 'source_dat_sha256': saved['sha256'],
            'manifest_scope': 'Exact manifest of the original projection audit; later documentation-only manifest changes do not change these DAT/model hashes.',
            'projection_rule': 'No positive 3D surface area or X/Z projection inside the open removed tile; exact tile borders are allowed.',
            'checked_model_resources': checked_models, 'cells': cells}
