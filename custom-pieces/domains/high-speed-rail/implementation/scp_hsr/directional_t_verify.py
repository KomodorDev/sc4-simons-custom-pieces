"""Independent resource and design checks for the new smooth at-grade HSR T.

The old interchange contracts deliberately remain unchanged.  This module's
new contract must describe actual native ports and reserved cells before a
recipe can pass.  Design measurements use the encoded PATH polylines, rather
than the generator's control points, labels, or claimed radii.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
import json
import math

from scp.dbpf import require
from .interchange_verify import (
    S3D, PATH, EXEMPLAR, _point, _number, _encoded_routes, _graph,
    _native_port_headings, _intersection, _bed, _models,
    check_construction_fields as _construction,
)
from scp.models import parse_s3d
from .rail_feature_verify import _triangles, _rail_u
from .rail_repair_verify import audit_supports

# Reviewed city-cell masks and native ports.  No layout writer is imported.
_ROWS = ('#......', '#......', '#......', '##.....', '###....', '#.#####',
         '###....', '##.....', '#......', '#......', '#......')
_MOVES = [(a+'in', b+'out') for a in 'NSE' for b in 'NSE' if a != b]
_TURN_LIMITS = {'max_length_ratio': 1.55, 'max_total_turn_degrees': 100.,
                'max_sample_turn_degrees': 8., 'max_raw_turn_degrees': 3., 'min_radius_m': 24.,
                'max_curvature_change_per_m2': .0015,
                'max_endpoint_curvature_per_m': .0005,
                'max_grade_change_per_m': .025}
CONTRACTS = {'directional_hsr_t_smooth_at_grade': {
    'cells': [(x, row) for row, mask in enumerate(_ROWS) for x, flag in enumerate(mask) if flag == '#'],
    'footprint': (7, 11), 'cost': 2200, 'kind': 'smooth_at_grade_t',
    'ports': {'Nin': (-2., 8., 15.5), 'Nout': (2., 8., 15.5),
              'Sin': (2., -168., 15.5), 'Sout': (-2., -168., 15.5),
              'Ein': (104., -78., 15.5), 'Eout': (104., -82., 15.5)},
    'port_vectors': {'Nin': (0., -1.), 'Nout': (0., 1.),
                     'Sin': (0., 1.), 'Sout': (0., -1.),
                     'Ein': (-1., 0.), 'Eout': (1., 0.)},
    'movements': _MOVES, 'min_height': 15.5, 'max_height': 15.5, 'max_grade': 0.,
    'clearance_width_m': 5., 'foundation_width_m': 1.3,
    'support_centres_xz': [(0., 16.*row) for row in range(11)]+
                          [(16., 64.), (32., 80.), (48., 80.), (64., 80.),
                           (80., 80.), (96., 80.), (16., 96.)],
    'minimum_support_spacing_m': 16.,
    'at_grade_conflict_pairs': [(('Sin', 'Nout'), ('Nin', 'Eout')),
                                (('Sin', 'Nout'), ('Ein', 'Sout')),
                                (('Nin', 'Eout'), ('Ein', 'Sout'))],
    'quality_limits': {(a, b): {**_TURN_LIMITS,
                                **({'max_length_ratio': 1.02, 'max_total_turn_degrees': 1.}
                                   if {a[0], b[0]} == {'N', 'S'} else {})}
                       for a, b in _MOVES},
}}
EPS = 2e-6


def _contract(spec):
    require(spec['recipe'] in CONTRACTS,
            'Unknown directional T recipe requires a literal independent contract')
    contract = CONTRACTS[spec['recipe']]
    require([tuple(cell) for cell in spec['cells']] == contract['cells'] and
            tuple(spec['footprint']) == contract['footprint'],
            'Directional T footprint differs from its independent reserved cells')
    require([tuple(cell) for cell in spec.get('structural_cells', [])] ==
            contract.get('structural_cells', []),
            'Directional T contains an undeclared structural-only cell')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(contract['cells']) and tiles,
            'Directional T allocation count differs from its reserved cells')
    x, row = contract['cells'][0]
    base = tiles[0]-0x100*x-0x10*row
    require(tiles == [base+0x100*x+0x10*row for x, row in contract['cells']],
            'Directional T tile allocation differs from its AutoTileBase grid')
    return contract


def _journeys(records, contract):
    """Reconstruct each *unique* complete journey across actual encoded seams.

    A permitted endpoint matrix alone can hide an unnecessary alternative
    loop which reaches the same destination.  Here every cell route must be
    used by one of the six unambiguous external journeys.
    """
    starts, parents = defaultdict(list), defaultdict(set)
    for index, (_, _, points) in enumerate(records):
        starts[points[0]].append(index)
        parents[points[-1]].add(points[0])
    ports = {label: _point(point) for label, point in contract['ports'].items()}
    used, result = set(), {}
    for movement in contract['movements']:
        source, target = (ports[label] for label in movement)
        reverse, pending = set(), [target]
        while pending:
            node = pending.pop()
            if node not in reverse:
                reverse.add(node)
                pending.extend(parents[node])
        require(source in reverse, 'Directional T is missing a complete intended journey')
        path, visited, node = [source], set(), source
        while node != target:
            require(node not in visited, 'Directional T journey contains a directed loop')
            visited.add(node)
            choices = [index for index in starts[node] if records[index][2][-1] in reverse]
            require(len(choices) == 1,
                    'Directional T has ambiguous alternative routes for one intended journey')
            index = choices[0]
            used.add(index)
            points = records[index][2]
            path.extend(points[1:])
            node = points[-1]
        result[tuple(movement)] = path
    require(used == set(range(len(records))),
            'Directional T includes an unused encoded track or redundant alternative')
    return result


def _resample(points, spacing=2.):
    """Sample by horizontal arclength so tiny grid cuts cannot skew curvature."""
    lengths = [math.dist(a[:2], b[:2]) for a, b in zip(points, points[1:])]
    total = sum(lengths)
    require(total > EPS, 'Directional T journey has no horizontal length')
    # Equal spacing includes both exact endpoints without a tiny last sample.
    count = max(2, math.ceil(total/spacing))
    samples, segment, start_distance = [], 0, 0.
    for index in range(count+1):
        distance = total*index/count
        while segment < len(lengths)-1 and distance > start_distance+lengths[segment]:
            start_distance += lengths[segment]
            segment += 1
        require(lengths[segment] > EPS, 'Directional T journey has a vertical or zero-length segment')
        t = max(0., min(1., (distance-start_distance)/lengths[segment]))
        samples.append(tuple(points[segment][axis]+t*(points[segment+1][axis]-points[segment][axis])
                             for axis in range(3)))
    return samples, total/count, total


def measure_route_quality(points, limits):
    """Measure one encoded journey against explicit, authored design limits.

    Radius and change in curvature describe only the horizontal PATH line.
    These project thresholds are not railway design standards or a measured
    game vehicle collision box.
    """
    # Grid intersections can create a chord shorter than1mm whose printed
    # coordinates have micro-metre rounding. Remove such a point only if it
    # lies within0.01mm of its neighbours' straight chord. A short but real
    # zigzag is retained and cannot disappear between2m quality samples.
    raw = [points[0]]
    for point in points[1:]:
        raw.append(point)
        while len(raw) >= 3:
            a, b, c = raw[-3:]
            ab, bc, ac = math.dist(a[:2], b[:2]), math.dist(b[:2], c[:2]), math.dist(a[:2], c[:2])
            if min(ab, bc) >= .001 or ac <= EPS:
                break
            deviation = abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/ac
            if deviation > .00001 or ab+bc-ac > .00001:
                break
            raw.pop(-2)
    raw_turns, resolved_raw_curvatures = [], []
    for a, b, c in zip(raw, raw[1:], raw[2:]):
        ab, bc = math.dist(a[:2], b[:2]), math.dist(b[:2], c[:2])
        require(ab > EPS and bc > EPS, 'Directional T has a zero-length raw curve segment')
        angle = abs(math.atan2((b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0]),
                               (b[0]-a[0])*(c[0]-b[0])+(b[1]-a[1])*(c[1]-b[1])))
        # Account only for the known1e-6m coordinate rounding, not for a
        # designer's sharp turn or short side excursion.
        rounding_angle = 2.*math.asin(min(1., 2e-6/min(ab, bc)))
        raw_turns.append(max(0., math.degrees(angle-rounding_angle)))
        ac = math.dist(a[:2], c[:2])
        require(ac > EPS, 'Directional T raw curve reverses directly into itself')
        cross = abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
        # An upper bound on cross-product error from1e-6m printed points.
        # Subtract it before testing curvature, so a very short straight grid
        # cut is not mistaken for a tight bend. A densely sampled real bend
        # still fails even if each separate heading change is below3 degrees.
        cross_error = 8e-6*(ab+bc+ac)+1e-10
        resolved_raw_curvatures.append(2.*max(0., cross-cross_error)/(ab*bc*ac))
    maximum_raw_turn = max(raw_turns, default=0.)
    require(maximum_raw_turn <= limits['max_raw_turn_degrees']+EPS,
            f'Directional T contains a sharp raw encoded tangent kink between quality samples: {maximum_raw_turn:.6f} degrees')
    maximum_raw_curvature = max(resolved_raw_curvatures, default=0.)
    resolved_radius = 1./maximum_raw_curvature if maximum_raw_curvature > 1e-10 else None
    require(resolved_radius is None or resolved_radius >= limits['min_radius_m']-EPS,
            f'Directional T has a tight raw encoded curve hidden between quality samples: resolved radius {resolved_radius!r} m')
    sampled, step, length = _resample(points)
    direct = math.dist(points[0][:2], points[-1][:2])
    require(direct > EPS, 'Directional T journey returns to its own endpoint')
    ratio = length/direct
    require(ratio <= limits['max_length_ratio']+EPS,
            f'Directional T journey takes an excessive detour: length/direct distance {ratio:.6f}')
    directions, grades = [], []
    for a, b in zip(sampled, sampled[1:]):
        dx, dy = b[0]-a[0], b[1]-a[1]
        run = math.hypot(dx, dy)
        require(run > EPS, 'Directional T journey doubles back within a quality sample')
        directions.append((dx/run, dy/run))
        grades.append((b[2]-a[2])/run)
    angles = [math.atan2(a[0]*b[1]-a[1]*b[0], a[0]*b[0]+a[1]*b[1])
              for a, b in zip(directions, directions[1:])]
    total_turn = math.degrees(sum(abs(angle) for angle in angles))
    require(total_turn <= limits['max_total_turn_degrees']+EPS,
            f'Directional T journey has excessive cumulative turning: {total_turn:.6f} degrees')
    maximum_angle = math.degrees(max(map(abs, angles), default=0.))
    require(maximum_angle <= limits['max_sample_turn_degrees']+EPS,
            f'Directional T has an abrupt tangent kink: {maximum_angle:.6f} degrees per sample')
    curvatures = []
    for a, b, c in zip(sampled, sampled[1:], sampled[2:]):
        first, second, chord = math.dist(a[:2], b[:2]), math.dist(b[:2], c[:2]), math.dist(a[:2], c[:2])
        cross = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        require(first*second*chord > EPS**3, 'Directional T curve reverses into its preceding sample')
        curvatures.append(2.*cross/(first*second*chord))
    maximum_curvature = max(map(abs, curvatures), default=0.)
    radius = 1./maximum_curvature if maximum_curvature > 1e-10 else None
    require(radius is None or radius >= limits['min_radius_m']-EPS,
            f'Directional T has an undersized horizontal curve radius: {radius!r} m')
    endpoint_curvature = max(abs(curvatures[0]), abs(curvatures[-1])) if curvatures else 0.
    require(endpoint_curvature <= limits['max_endpoint_curvature_per_m']+EPS,
            f'Directional T does not ease curvature continuously into its native straight approach: {endpoint_curvature:.8f} per metre')
    curvature_change = max((abs(b-a)/step for a, b in zip(curvatures, curvatures[1:])), default=0.)
    require(curvature_change <= limits['max_curvature_change_per_m2']+EPS,
            f'Directional T curvature changes abruptly: {curvature_change:.8f} per square metre')
    grade_change = max((abs(b-a)/step for a, b in zip(grades, grades[1:])), default=0.)
    require(grade_change <= limits['max_grade_change_per_m']+EPS,
            f'Directional T vertical grade changes abruptly: {grade_change:.8f} per metre')
    return {'length_m': length, 'direct_distance_m': direct, 'length_ratio': ratio,
            'total_turn_degrees': total_turn, 'minimum_sampled_radius_m': radius,
            'maximum_sample_turn_degrees': maximum_angle,
            'maximum_raw_encoded_turn_degrees': maximum_raw_turn,
            'minimum_resolved_raw_radius_m': resolved_radius,
            'maximum_endpoint_curvature_per_m': endpoint_curvature,
            'maximum_curvature_change_per_m2': curvature_change,
            'maximum_grade_change_per_m': grade_change, 'quality_sample_spacing_m': step}


def check_paths(resources, spec, donors=None):
    contract = _contract(spec)
    records = _encoded_routes(resources, spec, contract)
    ports, movements = _graph(records, contract)
    native = _native_port_headings(records, contract)
    journeys = _journeys(records, contract)
    conflicts = _at_grade_conflicts(journeys, contract)
    quality = {f'{a}>{b}': measure_route_quality(points, contract['quality_limits'][a, b])
               for (a, b), points in journeys.items()}
    return {'tile_count': len(contract['cells']), 'encoded_routes_checked': len(records),
            'external_ports_checked': ports, 'permitted_movements_checked': movements,
            'rotations_checked': 4, 'exact_3d_cell_seams': True, 'unwanted_u_turns': False,
            'native_facing_port_tangents_checked': len(native),
            'grade_separated_crossings_checked': 0,
            'declared_at_grade_conflicts_checked': len(conflicts),
            'at_grade_conflicts': conflicts, 'collision_free_operation_claimed': False,
            'all_encoded_tracks_used_by_intended_journeys': True,
            'unique_complete_journeys_checked': len(journeys), 'journey_quality': quality}


def check_construction_fields(fields, spec, resources):
    return _construction(fields, spec, resources, contract=_contract(spec))


def _at_grade_conflicts(journeys, contract):
    """Declare the flat prototype's actual conflicts, without hiding them.

    Shared-input forks and shared-output merges may join in the same travel
    direction.  Every other crossing must match one explicit conflict pair.
    The target is an at-grade rail junction, never a claimed flying junction.
    """
    expected = {frozenset(map(tuple, pair)) for pair in contract['at_grade_conflict_pairs']}
    actual = defaultdict(dict)
    items = list(journeys.items())
    for index, (first, points) in enumerate(items):
        for second, other in items[:index]:
            common_arm = first[0] == second[0] or first[1] == second[1]
            for a, b in zip(points, points[1:]):
                for c, d in zip(other, other[1:]):
                    if (min(a[0], b[0]) > max(c[0], d[0])+EPS or
                        min(c[0], d[0]) > max(a[0], b[0])+EPS or
                        min(a[1], b[1]) > max(c[1], d[1])+EPS or
                        min(c[1], d[1]) > max(a[1], b[1])+EPS):
                        continue
                    crossing = _intersection(a, b, c, d)
                    if crossing is None:
                        continue
                    t, u = crossing
                    dot = ((b[0]-a[0])*(d[0]-c[0])+(b[1]-a[1])*(d[1]-c[1]))/(
                        math.dist(a[:2], b[:2])*math.dist(c[:2], d[:2]))
                    if common_arm and dot > .25:
                        continue
                    pair = frozenset((first, second))
                    require(pair in expected,
                            f'Directional T contains an undeclared crossing conflict between {first} and {second}')
                    ha, hb = a[2]+t*(b[2]-a[2]), c[2]+u*(d[2]-c[2])
                    require(abs(ha-15.5) < EPS and abs(hb-15.5) < EPS,
                            'The explicitly at-grade T must retain both actual crossing PATH heights')
                    point = a[0]+t*(b[0]-a[0]), a[1]+t*(b[1]-a[1])
                    # Adjacent polyline fragments can describe the same
                    # crossing twice; millimetre rounding merges those copies.
                    actual[pair][tuple(round(v, 3) for v in point)] = (point, dot)
    require(set(actual) == expected and all(len(points) == 1 for points in actual.values()),
            'Directional T is missing a declared conflict or crosses the same opposing route repeatedly')
    return [{'movements': sorted('>'.join(move) for move in pair),
             'xy': list(next(iter(points.values()))[0]),
             'direction_dot': next(iter(points.values()))[1], 'height_m': 15.5}
            for pair, points in sorted(actual.items(), key=lambda item: sorted(item[0]))]


def _world_triangles(resources, spec, contract):
    return [tuple((x+16.*col, h, z+16.*row, u, v) for x, h, z, u, v in triangle)
            for (col, row), tile in zip(contract['cells'], spec['tile_ids'])
            for triangle in _triangles(parse_s3d(resources[*S3D, _number(tile)]))]


def _area(polygon):
    return abs(sum(a[0]*b[1]-b[0]*a[1]
                   for a, b in zip(polygon, polygon[1:]+polygon[:1])))/2.


def _clip_polygon(polygon, value, positive):
    result = []
    for a, b in zip(polygon, polygon[1:]+polygon[:1]):
        va, vb = value(a), value(b)
        if (va >= 0.) == positive:
            result.append(a)
        if (va < 0. < vb) or (vb < 0. < va):
            t = va/(va-vb)
            result.append(tuple(a[axis]+t*(b[axis]-a[axis]) for axis in (0, 1)))
    return result


def _intersection_polygon(polygon, clip):
    signed = sum(a[0]*b[1]-b[0]*a[1] for a, b in zip(clip, clip[1:]+clip[:1]))
    orientation = 1. if signed > 0. else -1.
    for a, b in zip(clip, clip[1:]+clip[:1]):
        if not polygon:
            break
        polygon = _clip_polygon(polygon, lambda p: orientation*((b[0]-a[0])*(p[1]-a[1])-
                                                               (b[1]-a[1])*(p[0]-a[0])), True)
    return polygon


def _polygon_union_area(polygons):
    """Exact area of a small overlap component by vertical arrangement slabs.

    Between polygon vertices and boundary intersections, interval endpoints
    vary linearly and their order is fixed.  The union's vertical length is
    therefore linear too: one midpoint times slab width integrates it exactly.
    This handles triple overlaps without a conservative false-hole result.
    """
    if not polygons:
        return 0.
    if len(polygons) == 1:
        return _area(polygons[0])
    events = {p[0] for polygon in polygons for p in polygon}
    for index, polygon in enumerate(polygons):
        for other in polygons[:index]:
            for a, b in zip(polygon, polygon[1:]+polygon[:1]):
                for c, d in zip(other, other[1:]+other[:1]):
                    crossing = _intersection(a, b, c, d)
                    if crossing is not None:
                        events.add(a[0]+crossing[0]*(b[0]-a[0]))
    events = sorted(events)
    area = 0.
    for left, right in zip(events, events[1:]):
        if right-left < 1e-12:
            continue
        x, intervals = (left+right)/2., []
        for polygon in polygons:
            ys = [a[1]+(x-a[0])*(b[1]-a[1])/(b[0]-a[0])
                  for a, b in zip(polygon, polygon[1:]+polygon[:1])
                  if min(a[0], b[0]) <= x <= max(a[0], b[0]) and abs(b[0]-a[0]) > 1e-12]
            if ys:
                intervals.append((min(ys), max(ys)))
        intervals.sort()
        length, start, end = 0., None, None
        for low, high in intervals:
            if start is None:
                start, end = low, high
            elif low <= end:
                end = max(end, high)
            else:
                length += end-start
                start, end = low, high
        if start is not None:
            length += end-start
        area += length*(right-left)
    return area


def _minimum_strip_width(polygon):
    widths = []
    for a, b in zip(polygon, polygon[1:]+polygon[:1]):
        length = math.dist(a, b)
        if length > 1e-10:
            projected = [((b[1]-a[1])*p[0]-(b[0]-a[0])*p[1])/length for p in polygon]
            widths.append(max(projected)-min(projected))
    return min(widths, default=0.)


def audit_bed_union(triangles, records, *, half_width=2.5):
    """Prove each complete rectangular train corridor has actual bed beneath.

    Measure actual placed floor overlaps, rejecting substantive duplicates.
    Then sum disjoint triangles and integrate overlap components exactly;
    checking centre points would miss holes between samples. Even a triple
    overlap cannot conceal a gap or cause a conservative false-hole result.
    The reviewed prototype is flat, so its bed plane is unambiguous.
    """
    buckets = defaultdict(set)
    floors = []
    for triangle in triangles:
        if not all(abs(p[1]-_bed(15.5)) < .001 for p in triangle):
            continue
        polygon = [(p[0], p[2]) for p in triangle]
        if _area(polygon) <= 1e-10:
            continue
        index = len(floors)
        floors.append(polygon)
        for x in range(math.floor((min(p[0] for p in polygon)-1e-4)/4.),
                       math.floor((max(p[0] for p in polygon)+1e-4)/4.)+1):
            for z in range(math.floor((min(p[1] for p in polygon)-1e-4)/4.),
                           math.floor((max(p[1] for p in polygon)+1e-4)/4.)+1):
                buckets[x, z].add(index)
    bounds = [(min(p[0] for p in polygon), max(p[0] for p in polygon),
               min(p[1] for p in polygon), max(p[1] for p in polygon)) for polygon in floors]
    parents = list(range(len(floors)))
    def find(index):
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index
    pair_checks, maximum_overlap, maximum_thickness, overlap_count = 0, 0., 0., 0
    for index, polygon in enumerate(floors):
        xmin, xmax, zmin, zmax = bounds[index]
        candidates = set()
        for x in range(math.floor((xmin-1e-4)/4.), math.floor((xmax+1e-4)/4.)+1):
            for z in range(math.floor((zmin-1e-4)/4.), math.floor((zmax+1e-4)/4.)+1):
                candidates.update(j for j in buckets[x, z] if j < index)
        for other in candidates:
            oxmin, oxmax, ozmin, ozmax = bounds[other]
            if min(xmax, oxmax)-max(xmin, oxmin) <= 1e-9 or min(zmax, ozmax)-max(zmin, ozmin) <= 1e-9:
                continue
            pair_checks += 1
            intersection = _intersection_polygon(polygon, floors[other])
            area = _area(intersection) if len(intersection) >= 3 else 0.
            maximum_overlap = max(maximum_overlap, area)
            if area > 1e-10:
                thickness = _minimum_strip_width(intersection)
                maximum_thickness = max(maximum_thickness, thickness)
                # Near-parallel clipping edges can leave sub0.1mm slivers.
                # This is an explicit numerical meshing tolerance, not a
                # claim that every sliver comes from float32 quantization.
                require(thickness <= .0001,
                        f'Directional T has substantive coplanar rail-bed overlap: area {area:.8f} square metres, '
                        f'thickness {thickness:.8f} metres; triangles {index, other}: {polygon}, {floors[other]}')
                overlap_count += 1
                parents[find(index)] = find(other)
    checked, worst = 0, 0.
    for _, _, points in records:
        for first, last in zip(points, points[1:]):
            a, b = (first[0], -first[1]), (last[0], -last[1])
            length = math.dist(a, b)
            normal = (b[1]-a[1])/length, (a[0]-b[0])/length
            rectangle = [(p[0]+cross*normal[0], p[1]+cross*normal[1])
                         for p, cross in ((a, -half_width), (a, half_width),
                                          (b, half_width), (b, -half_width))]
            candidates = set()
            for x in range(math.floor(min(p[0] for p in rectangle)/4.), math.floor(max(p[0] for p in rectangle)/4.)+1):
                for z in range(math.floor(min(p[1] for p in rectangle)/4.), math.floor(max(p[1] for p in rectangle)/4.)+1):
                    candidates.update(buckets[x, z])
            components = defaultdict(list)
            for index in candidates:
                polygon = _intersection_polygon(floors[index], rectangle)
                if len(polygon) >= 3 and _area(polygon) > 1e-10:
                    components[find(index)].append(polygon)
            covered = sum(_polygon_union_area(polygons) for polygons in components.values())
            missing = max(0., _area(rectangle)-covered)
            worst = max(worst, missing)
            require(missing <= max(1e-5, _area(rectangle)*1e-6),
                    f'Directional T train corridor has a hole in the actual placed rail bed: {missing:.8f} square metres')
            checked += 1
    require(checked > 0, 'Directional T has no train corridor to check for bed coverage')
    return {'full_width_bed_union_segments_checked': checked,
            'maximum_uncovered_bed_area_m2': worst, 'bed_union_width_m': 2.*half_width,
            'coplanar_bed_triangle_pairs_checked': pair_checks,
            'positive_area_coplanar_bed_pairs': overlap_count,
            'maximum_coplanar_bed_overlap_area_m2': maximum_overlap,
            'maximum_coplanar_bed_overlap_thickness_m': maximum_thickness,
            'coplanar_overlap_meshing_tolerance_m': .0001}


def audit_visible_rails(triangles, records):
    """Reverse the usual PATH→model audit: every native rail stripe needs PATH.

    Concrete floor UVs occupy the native central ballast patch.  The two
    rail-bearing atlas strips are disjoint, so actual rail-centre lines can
    be recovered by intersecting each textured triangle with its U value.
    """
    segments, buckets = [], defaultdict(set)
    for _, _, points in records:
        for a, b in zip(points, points[1:]):
            index = len(segments)
            segments.append((a, b))
            for x in range(math.floor((min(a[0], b[0])-1.1)/4.), math.floor((max(a[0], b[0])+1.1)/4.)+1):
                for y in range(math.floor((min(a[1], b[1])-1.1)/4.), math.floor((max(a[1], b[1])+1.1)/4.)+1):
                    buckets[x, y].add(index)
    def matching(point, maximum_distance):
        x, h, z = point[:3]
        for index in buckets[math.floor(x/4.), math.floor(-z/4.)]:
            a, b = segments[index]
            dx, dy = b[0]-a[0], b[1]-a[1]
            t = max(0., min(1., ((x-a[0])*dx+(-z-a[1])*dy)/(dx*dx+dy*dy)))
            if (math.hypot(x-a[0]-t*dx, -z-a[1]-t*dy) <= maximum_distance and
                abs(h-_bed(a[2]+t*(b[2]-a[2]))) < .10):
                return True
        return False
    bands = [(min(_rail_u(lane-1.), _rail_u(lane+1.))-.0001,
              max(_rail_u(lane-1.), _rail_u(lane+1.))+.0001, _rail_u(lane)) for lane in (-2., 2.)]
    triangle_count, centre_count = 0, 0
    for triangle in triangles:
        a, b, c = triangle
        ab, ac = [b[i]-a[i] for i in range(3)], [c[i]-a[i] for i in range(3)]
        normal = (ab[1]*ac[2]-ab[2]*ac[1], ab[2]*ac[0]-ab[0]*ac[2], ab[0]*ac[1]-ab[1]*ac[0])
        magnitude = math.sqrt(sum(value*value for value in normal))
        if magnitude < 1e-10 or abs(normal[1])/magnitude < .96:
            continue
        band = next((band for band in bands if all(band[0] <= p[3] <= band[1] for p in triangle)), None)
        if band is None:
            continue
        centre = tuple(sum(p[axis] for p in triangle)/3. for axis in range(3))
        require(matching(centre, 1.10),
                f'Directional T contains a visible native rail stripe with no used train PATH: {centre}')
        triangle_count += 1
        crossings = []
        for a, b in zip(triangle, triangle[1:]+triangle[:1]):
            if abs(a[3]-band[2]) < 1e-7:
                crossings.append(a[:3])
            if (a[3] < band[2] < b[3]) or (b[3] < band[2] < a[3]):
                t = (band[2]-a[3])/(b[3]-a[3])
                crossings.append(tuple(a[axis]+t*(b[axis]-a[axis]) for axis in range(3)))
        if len(crossings) >= 2:
            midpoint = tuple(sum(p[axis] for p in crossings)/len(crossings) for axis in range(3))
            require(matching(midpoint, .25),
                    f'Directional T visible native rail centre has no matching used train PATH: {midpoint}')
            centre_count += 1
    require(triangle_count > 0 and centre_count > 0, 'Directional T model has no audited native rail stripes')
    return {'visible_native_rail_triangles_matched_to_paths': triangle_count,
            'visible_native_rail_centre_segments_matched_to_paths': centre_count,
            'unused_visible_native_rails': False}


def check_models(resources, spec, donors=None):
    _contract(spec)
    keys = {(*S3D, _number(spec['preview_id']))}
    for tile in map(_number, spec['tile_ids']):
        keys.update({(*S3D, tile+zoom) for zoom in range(5)})
        keys.update({(*PATH, tile), (*EXEMPLAR, tile)})
    immutable = tuple((key, resources[key]) for key in sorted(keys))
    return json.loads(_cached_models(json.dumps(spec, sort_keys=True, separators=(',', ':')), immutable))


@lru_cache(maxsize=8)
def _cached_models(spec_json, immutable):
    spec, resources = json.loads(spec_json), dict(immutable)
    contract = _contract(spec)
    records = _encoded_routes(resources, spec, contract)
    triangles = _world_triangles(resources, spec, contract)
    report = _models(resources, spec, contract=contract)
    report.update(audit_bed_union(triangles, records))
    report.update(audit_visible_rails(triangles, records))
    report.update(audit_supports(triangles, contract))
    return json.dumps(report, sort_keys=True, separators=(',', ':'))
