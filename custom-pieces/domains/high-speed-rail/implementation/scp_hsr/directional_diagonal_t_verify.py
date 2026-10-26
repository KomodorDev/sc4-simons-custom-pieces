"""Independent resource contract for the new all-diagonal smooth HSR T.

The literal native ports below were checked against decoded NAM diagonal
PATH resources, not against the route writer.  This authored model assigns
its external joins to city-cell edge planes; native meshes can themselves
overhang those cells.  The outward part of the corridor belongs to adjoining
native track.  Only the first or last encoded corridor segment at an exact
declared port receives that boundary clipping.  Every interior segment
retains its complete five-metre-wide bed check.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
import json
import math

from scp.dbpf import require
from .directional_t_verify import (
    EPS, _TURN_LIMITS, _journeys, _at_grade_conflicts, measure_route_quality,
    _world_triangles, _area, _clip_polygon, _intersection_polygon,
    _polygon_union_area, _minimum_strip_width,
)
from .interchange_verify import (
    S3D, PATH, EXEMPLAR, _point, _number, _encoded_routes, _graph,
    _native_port_headings, _bed, _models,
    check_construction_fields as _construction,
)
from .rail_repair_verify import audit_supports
from .rail_feature_verify import _rail_u

# Native external points were independently decoded from PATH5dd01a00 and
# its proper quarter rotations.  The reviewed mask and consolidated support
# plan below are literals: this module never imports their writer.
_ROWS = ('..........##.', '.........##..', '........##...', '.......##....',
         '......###....', '.....###.....', '....##.#.....', '...######....',
         '..#######....', '.##.....##...', '##.......##..', '#.........##.',
         '...........#.', '.............')
_MOVES = [(a+'in', b+'out') for a in 'NSE' for b in 'NSE' if a != b]
CONTRACTS = {'directional_hsr_t_smooth_diagonal_at_grade': {
    'cells': [(x, row) for row, mask in enumerate(_ROWS) for x, flag in enumerate(mask) if flag == '#'],
    'footprint': (13, 14), 'cost': 4200, 'kind': 'smooth_diagonal_at_grade_t',
    'ports': {'Nin': (173.1, 8., 15.5), 'Nout': (178.9, 8., 15.5),
              'Sin': (-8., -178.9, 15.5), 'Sout': (-8., -173.2, 15.5),
              'Ein': (184., -189.1, 15.5), 'Eout': (184., -194.9, 15.5)},
    'port_vectors': {'Nin': (-1., -1.), 'Nout': (1., 1.),
                     'Sin': (1., 1.), 'Sout': (-1., -1.),
                     'Ein': (-1., 1.), 'Eout': (1., -1.)},
    # (model plan axis, plane coordinate, inward signed distance)
    'port_planes_xz': {'Nin': (1, -8., 1.), 'Nout': (1, -8., 1.),
                       'Sin': (0, -8., 1.), 'Sout': (0, -8., 1.),
                       'Ein': (0, 184., -1.), 'Eout': (0, 184., -1.)},
    'movements': _MOVES, 'min_height': 15.5, 'max_height': 15.5, 'max_grade': 0.,
    'clearance_width_m': 5., 'foundation_width_m': 1.3,
    'support_centres_xz': [
        (160., 0.), (176., 0.), (144., 16.), (160., 16.), (128., 32.), (144., 32.),
        (112., 48.), (128., 48.), (96., 64.), (112., 64.), (80., 80.),
        (96., 80.), (112., 80.), (64., 96.), (80., 96.), (112., 96.),
        (48., 112.), (64., 112.), (112., 112.), (32., 128.), (48., 128.),
        (64., 128.), (96., 128.), (112., 128.), (128., 128.), (16., 144.),
        (32., 144.), (128., 144.), (144., 144.), (0., 160.), (16., 160.),
        (144., 160.), (160., 160.), (0., 176.), (160., 176.), (176., 176.),
        (176., 192.)],
    'minimum_support_spacing_m': 16.,
    'at_grade_conflict_pairs': [(('Sin', 'Nout'), ('Nin', 'Eout')),
                                (('Sin', 'Nout'), ('Ein', 'Sout')),
                                (('Nin', 'Eout'), ('Ein', 'Sout'))],
    'quality_limits': {(a, b): {**_TURN_LIMITS,
                                **({'max_length_ratio': 1.02, 'max_total_turn_degrees': 1.}
                                   if {a[0], b[0]} == {'N', 'S'} else {})}
                       for a, b in _MOVES},
}}


def _contract(spec):
    require(spec['recipe'] in CONTRACTS,
            'Unknown diagonal smooth T requires a literal independent contract')
    contract = CONTRACTS[spec['recipe']]
    require([tuple(cell) for cell in spec['cells']] == contract['cells'] and
            tuple(spec['footprint']) == contract['footprint'],
            'Diagonal smooth T footprint differs from its independent reserved cells')
    require([tuple(cell) for cell in spec.get('structural_cells', [])] ==
            contract.get('structural_cells', []),
            'Diagonal smooth T contains an undeclared structural-only cell')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(contract['cells']) and tiles,
            'Diagonal smooth T allocation count differs from its reserved cells')
    x, row = contract['cells'][0]
    base = tiles[0]-0x100*x-0x10*row
    require(tiles == [base+0x100*x+0x10*row for x, row in contract['cells']],
            'Diagonal smooth T allocation differs from its AutoTileBase grid')
    return contract


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
            'native_diagonal_offsets_m': [2.8, 2.9],
            'grade_separated_crossings_checked': 0,
            'declared_at_grade_conflicts_checked': len(conflicts),
            'at_grade_conflicts': conflicts, 'collision_free_operation_claimed': False,
            'all_encoded_tracks_used_by_intended_journeys': True,
            'unique_complete_journeys_checked': len(journeys), 'journey_quality': quality}


def check_construction_fields(fields, spec, resources):
    return _construction(fields, spec, resources, contract=_contract(spec))


def _native_corridor_rectangle(first, last, contract, half_width, native_ends=()):
    """Return one actual corridor cross-section, clipped only at native ends.

    SC4PATH north is negated to obtain the model's south-positive Z axis.
    The literal port plane contains ``axis``, ``boundary`` and an inward sign;
    positive signed distance lies on the piece side of that native join.
    """
    a, b = (first[0], -first[1]), (last[0], -last[1])
    length = math.dist(a, b)
    require(length > EPS, 'Diagonal smooth T has a zero-length bed corridor')
    normal = (b[1]-a[1])/length, (a[0]-b[0])/length
    rectangle = [(p[0]+cross*normal[0], p[1]+cross*normal[1])
                 for p, cross in ((a, -half_width), (a, half_width),
                                  (b, half_width), (b, -half_width))]
    ports = {_point(point): label for label, point in contract['ports'].items()}
    clipped = 0
    for endpoint in native_ends:
        label = ports.get(_point(endpoint))
        if label is None:
            continue
        axis, boundary, inward = contract['port_planes_xz'][label]
        rectangle = _clip_polygon(rectangle,
                                  lambda p: inward*(p[axis]-boundary), True)
        clipped += 1
    require(len(rectangle) >= 3 and _area(rectangle) > EPS,
            'A diagonal native port leaves no interior corridor area')
    return rectangle, clipped


def audit_bed_union(triangles, records, contract, *, half_width=2.5):
    """Measure every interior floor area and reject coplanar duplicates.

    This preserves the first smooth T's exact floor-union audit and explicit
    0.1 mm numerical meshing tolerance.  Its only boundary addition is the
    native external-cell-edge clipping described by the literal contract.
    A hole even beside a clipped external join must still be rejected.
    """
    buckets, floors = defaultdict(set), []
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
                require(thickness <= .0001,
                        f'Diagonal smooth T has substantive coplanar rail-bed overlap: area {area:.8f} square metres, '
                        f'thickness {thickness:.8f} metres')
                overlap_count += 1
                parents[find(index)] = find(other)
    checked, worst, native_clips = 0, 0., 0
    for _, _, points in records:
        for index, (first, last) in enumerate(zip(points, points[1:])):
            native_ends = ([first] if index == 0 else [])+([last] if index == len(points)-2 else [])
            rectangle, clips = _native_corridor_rectangle(first, last, contract, half_width, native_ends)
            native_clips += clips
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
                    f'Diagonal smooth T train corridor has a hole in the actual placed rail bed: {missing:.8f} square metres')
            checked += 1
    require(checked > 0, 'Diagonal smooth T has no train corridor to check for bed coverage')
    return {'full_width_bed_union_segments_checked': checked,
            'maximum_uncovered_bed_area_m2': worst, 'bed_union_width_m': 2.*half_width,
            'coplanar_bed_triangle_pairs_checked': pair_checks,
            'positive_area_coplanar_bed_pairs': overlap_count,
            'maximum_coplanar_bed_overlap_area_m2': maximum_overlap,
            'maximum_coplanar_bed_overlap_thickness_m': maximum_thickness,
            'coplanar_overlap_meshing_tolerance_m': .0001,
            'native_external_port_corridor_segments_clipped': native_clips,
            'external_native_continuation_geometry_included': False}


def audit_visible_rails(triangles, records, contract):
    """Require every actual rail stripe and centre line to own a used PATH.

    At an axis-cut diagonal native face, a rail ribbon's outer corner can
    extend forward of the PATH endpoint while remaining inside the model's
    authored halfspace.  Only stripe centroids receive that exact cap test:
    their existing1.10m perpendicular allowance also bounds the outward
    projection.  The0.25m rail-centre check remains clamped to actual PATH.
    A nearby undeclared or missing external port gets no cap extension.
    """
    segments, buckets = [], defaultdict(set)
    encoded_inputs = {_point(points[0]) for _, _, points in records}
    encoded_outputs = {_point(points[-1]) for _, _, points in records}
    caps = []
    for label, point in contract['ports'].items():
        encoded_ends = encoded_inputs if label.endswith('in') else encoded_outputs
        if _point(point) not in encoded_ends:
            continue
        dx, dy = contract['port_vectors'][label]
        direction = 1. if label.endswith('out') else -1.
        length = math.hypot(dx, dy)
        caps.append((point, (direction*dx/length, direction*dy/length),
                     contract['port_planes_xz'][label]))
    for _, _, points in records:
        for a, b in zip(points, points[1:]):
            index = len(segments)
            segments.append((a, b))
            for x in range(math.floor((min(a[0], b[0])-1.1)/4.), math.floor((max(a[0], b[0])+1.1)/4.)+1):
                for y in range(math.floor((min(a[1], b[1])-1.1)/4.), math.floor((max(a[1], b[1])+1.1)/4.)+1):
                    buckets[x, y].add(index)
    cap_matches = 0
    def matching(point, maximum_distance, *, stripe_cap=False):
        nonlocal cap_matches
        x, h, z = point[:3]
        for index in buckets[math.floor(x/4.), math.floor(-z/4.)]:
            a, b = segments[index]
            dx, dy = b[0]-a[0], b[1]-a[1]
            t = max(0., min(1., ((x-a[0])*dx+(-z-a[1])*dy)/(dx*dx+dy*dy)))
            if (math.hypot(x-a[0]-t*dx, -z-a[1]-t*dy) <= maximum_distance and
                abs(h-_bed(a[2]+t*(b[2]-a[2]))) < .10):
                return True
        if stripe_cap:
            for port, (dx, dy), (axis, boundary, inward) in caps:
                if inward*((x, z)[axis]-boundary) < -EPS or abs(h-_bed(port[2])) >= .10:
                    continue
                px, py = x-port[0], -z-port[1]
                outward = px*dx+py*dy
                perpendicular = abs(px*dy-py*dx)
                if EPS < outward <= maximum_distance+EPS and perpendicular <= maximum_distance+EPS:
                    cap_matches += 1
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
        require(matching(centre, 1.10, stripe_cap=True),
                f'Diagonal smooth T contains a visible native rail stripe with no used train PATH: {centre}')
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
                    f'Diagonal smooth T visible native rail centre has no matching used train PATH: {midpoint}')
            centre_count += 1
    require(triangle_count > 0 and centre_count > 0, 'Diagonal smooth T model has no audited native rail stripes')
    return {'visible_native_rail_triangles_matched_to_paths': triangle_count,
            'visible_native_rail_centre_segments_matched_to_paths': centre_count,
            'unused_visible_native_rails': False,
            'native_external_cap_stripe_matches': cap_matches,
            'native_external_cap_rail_centre_matches': 0,
            'native_external_cap_maximum_stripe_projection_m': 1.10,
            'native_external_rail_centres_clamped_to_actual_paths': True}


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
    report.update(audit_bed_union(triangles, records, contract))
    report.update(audit_visible_rails(triangles, records, contract))
    report.update(audit_supports(triangles, contract))
    return json.dumps(report, sort_keys=True, separators=(',', ':'))
