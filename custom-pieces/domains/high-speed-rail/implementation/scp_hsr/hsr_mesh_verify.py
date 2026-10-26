"""Independent geometry audits shared by upper HSR components and assemblies.

These checks inspect supplied encoded paths and actual mesh triangles without
importing any layout or model generator. Contract literals stay with each
component family.
"""
from __future__ import annotations

from collections import defaultdict
import math

from scp.dbpf import require
from .interchange_verify import _intersection, _bed
from .directional_t_verify import (
    _resample, measure_route_quality, _TURN_LIMITS,
    _area, _intersection_polygon, _polygon_union_area, _minimum_strip_width,
)
from .rail_feature_verify import _weights
from .rail_repair_verify import _overlap, _inside

EPS = 2e-6


def _shared_prefix(first, second):
    """Find the actual common directed tail, even with different sampling.

    Common incoming/outgoing labels alone are insufficient: two connectors
    from the same arm must not cross again after separating. This walks the
    coincident 3D polyline until the first geometric divergence.
    """
    if math.dist(first[0], second[0]) > EPS:
        return []
    i = j = 0
    a = b = first[0]
    shared = [a]
    while i < len(first)-1 and j < len(second)-1:
        end_a, end_b = first[i+1], second[j+1]
        da, db = math.dist(a[:2], end_a[:2]), math.dist(b[:2], end_b[:2])
        if da <= EPS:
            i += 1
            a = end_a
            continue
        if db <= EPS:
            j += 1
            b = end_b
            continue
        ua = tuple((end_a[k]-a[k])/da for k in range(3))
        ub = tuple((end_b[k]-b[k])/db for k in range(3))
        if max(abs(ua[k]-ub[k]) for k in range(3)) > 1e-5:
            break
        distance = min(da, db)
        a = tuple(a[k]+distance*ua[k] for k in range(3))
        b = tuple(b[k]+distance*ub[k] for k in range(3))
        if math.dist(a, b) > 3e-5:
            break
        shared.append(a)
        if da <= distance+EPS:
            i += 1
            a = end_a
        if db <= distance+EPS:
            j += 1
            b = end_b
    return list(zip(shared, shared[1:]))



def _on_shared(point, segments):
    for a, b in segments:
        length2 = sum((b[k]-a[k])**2 for k in (0, 1))
        if length2 <= EPS**2:
            continue
        t = sum((point[k]-a[k])*(b[k]-a[k]) for k in (0, 1))/length2
        if -EPS <= t <= 1.+EPS and math.dist(point, tuple(a[k]+t*(b[k]-a[k]) for k in range(3))) < .0001:
            return True
    return False



def _crossing_parameters(a, b, c, d):
    """Include positive collinear overlaps; opposite coincident rails collide."""
    crossing = _intersection(a, b, c, d)
    if crossing is not None:
        return [(crossing[0], crossing[1], False)]
    dx, dy, ex, ey = b[0]-a[0], b[1]-a[1], d[0]-c[0], d[1]-c[1]
    length2, other2 = dx*dx+dy*dy, ex*ex+ey*ey
    if abs(dx*ey-dy*ex) > 1e-10 or abs((c[0]-a[0])*dy-(c[1]-a[1])*dx)/math.sqrt(length2) > EPS:
        return []
    first = ((c[0]-a[0])*dx+(c[1]-a[1])*dy)/length2
    last = ((d[0]-a[0])*dx+(d[1]-a[1])*dy)/length2
    low, high = max(0., min(first, last)), min(1., max(first, last))
    if (high-low)*math.sqrt(length2) <= EPS:
        return []
    result = []
    for t in (low, (low+high)/2., high):
        x, y = a[0]+t*dx, a[1]+t*dy
        u = ((x-c[0])*ex+(y-c[1])*ey)/other2
        result.append((t, max(0., min(1., u)), True))
    return result



def audit_crossings(journeys, contract):
    """Allow only connected tangent forks/merges or real clear flyovers."""
    items = list(journeys.items())
    separated, joined, actual_crossings = {}, set(), set()
    for index, (first, points) in enumerate(items):
        for other_index in range(index+1):
            second, other = items[other_index]
            same = index == other_index
            shared = []
            if not same and first[0] == second[0]:
                shared.extend(_shared_prefix(points, other))
            if not same and first[1] == second[1]:
                shared.extend(_shared_prefix(list(reversed(points)), list(reversed(other))))
            buckets = defaultdict(list)
            for node, (a, b) in enumerate(zip(other, other[1:])):
                for x in range(math.floor(min(a[0], b[0])/8.), math.floor(max(a[0], b[0])/8.)+1):
                    for y in range(math.floor(min(a[1], b[1])/8.), math.floor(max(a[1], b[1])/8.)+1):
                        buckets[x, y].append((node, a, b))
            checked = set()
            for node_a, (a, b) in enumerate(zip(points, points[1:])):
                candidates = {}
                for x in range(math.floor(min(a[0], b[0])/8.), math.floor(max(a[0], b[0])/8.)+1):
                    for y in range(math.floor(min(a[1], b[1])/8.), math.floor(max(a[1], b[1])/8.)+1):
                        for node_b, c, d in buckets[x, y]:
                            candidates[node_b] = (c, d)
                for node_b, (c, d) in candidates.items():
                    if same and abs(node_a-node_b) <= 1:
                        continue
                    pair = (min(node_a, node_b), max(node_a, node_b)) if same else (node_a, node_b)
                    if pair in checked:
                        continue
                    checked.add(pair)
                    for t, u, collinear in _crossing_parameters(a, b, c, d):
                        ha, hb = a[2]+t*(b[2]-a[2]), c[2]+u*(d[2]-c[2])
                        point = (a[0]+t*(b[0]-a[0]), a[1]+t*(b[1]-a[1]), ha)
                        dot = sum((b[k]-a[k])*(d[k]-c[k]) for k in (0, 1))/(math.dist(a[:2], b[:2])*math.dist(c[:2], d[:2]))
                        if abs(ha-hb) < .0001 and dot > .95 and _on_shared(point, shared):
                            joined.add(tuple(round(v, 3) for v in point))
                            continue
                        clearance = abs(ha-hb)-(16.98933-14.01067)
                        require(clearance >= contract.get('minimum_clearance', 5.)-EPS,
                                f'HSR has an independent same-level crossing or insufficient deck clearance: '
                                f'{first} versus {second}, XY {point[:2]}, heights {(ha, hb)}, clearance {clearance:.6f}m')
                        key = tuple(round(v, 3) for v in (*point[:2], max(ha, hb), min(ha, hb)))
                        separated[key] = {'xy': list(point[:2]), 'path_heights_m': [ha, hb],
                                          'structural_clearance_m': clearance, 'collinear_projection': collinear}
                        if not collinear and abs(dot) < .9999:
                            actual_crossings.add(key)
    require(len(actual_crossings) >= contract['required_grade_separated_crossings'],
            'HSR lacks its required real over/under train crossings')
    expected = contract.get('expected_crossings_xyz')
    if expected is not None:
        require(len(actual_crossings) == len(expected) and
                all(any(math.dist(point, actual) < .02 for actual in actual_crossings) for point in expected),
                'HSR real crossing positions or heights differ from its reviewed independent contract')
    return {'grade_separated_crossings_checked': len(actual_crossings),
            'grade_separated_projected_contacts_checked': len(separated),
            'grade_separated_crossings': [separated[key] for key in sorted(separated)],
            'same_direction_shared_tail_contacts_checked': len(joined),
            'independent_at_grade_conflicts_checked': 0}



def _coalesce_grid_cuts(points):
    """Remove only straight chord subdivisions within the2µm graph guard.

    Tile boundaries may split a0.5m authored chord into0.08m and0.42m pieces.
    Treating the0.08m fragment as a whole new curve sample would spuriously
    halve its measured radius. The independent graph normalizes XYZ to1µm; preserve real bends,
    zigzags and grade changes beyond that explicit coordinate guard.
    """
    result = []
    for point in points:
        result.append(point)
        while len(result) >= 3:
            a, b, c = result[-3:]
            ab, bc, ac = math.dist(a[:2], b[:2]), math.dist(b[:2], c[:2]), math.dist(a[:2], c[:2])
            if ac <= EPS or ab <= EPS or bc <= EPS:
                break
            deviation = abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/ac
            t = ((b[0]-a[0])*(c[0]-a[0])+(b[1]-a[1])*(c[1]-a[1]))/(ac*ac)
            if not (0. < t < 1.) or deviation > 2e-6 or ab+bc-ac > 4e-6 or abs(b[2]-(a[2]+t*(c[2]-a[2]))) > 2e-6:
                break
            result.pop(-2)
    return result



def measure_journey_quality(points, limits):
    points = _coalesce_grid_cuts(points)
    measured = measure_route_quality(points, limits)
    require(measured['total_turn_degrees'] >= limits.get('min_total_turn_degrees', 0.)-EPS,
            'HSR intentional loop is missing its independently required cumulative turn')
    require(limits.get('min_length_m', 0.)-EPS <= measured['length_m'] <= limits.get('max_length_m', math.inf)+EPS,
            'HSR journey leaves its independently bounded length range')
    sampled, _, _ = _resample(points)
    directions = [(b[0]-a[0], b[1]-a[1]) for a, b in zip(sampled, sampled[1:])]
    signed = math.degrees(sum(math.atan2(a[0]*b[1]-a[1]*b[0], a[0]*b[0]+a[1]*b[1])
                              for a, b in zip(directions, directions[1:])))
    if 'signed_turn_degrees' in limits:
        require(abs(signed-limits['signed_turn_degrees']) <= limits.get('max_signed_turn_error_degrees', 1.)+EPS,
                'HSR journey has the wrong signed winding for its deliberate loop or direct turn')
    changes = []
    for a, b, c in zip(points, points[1:], points[2:]):
        first, second = math.dist(a[:2], b[:2]), math.dist(b[:2], c[:2])
        ga, gb = (b[2]-a[2])/first, (c[2]-b[2])/second
        rounding = 4e-6*(1./first+1./second)
        changes.append(max(0., abs(gb-ga)-rounding)/(.5*(first+second)))
    raw_change = max(changes, default=0.)
    require(raw_change <= limits['max_grade_change_per_m']+EPS,
            f'HSR raw encoded vertical grade changes abruptly between quality samples: {raw_change:.8f} per metre')
    measured.update(signed_turn_degrees=signed, maximum_raw_grade_change_per_m=raw_change)
    return measured



def _plane(triangle):
    a, b, c = triangle
    determinant = (b[0]-a[0])*(c[2]-a[2])-(b[2]-a[2])*(c[0]-a[0])
    if abs(determinant) < 1e-10:
        return None
    gx = ((b[1]-a[1])*(c[2]-a[2])-(c[1]-a[1])*(b[2]-a[2]))/determinant
    gz = ((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1]))/determinant
    return gx, gz, a[1]-gx*a[0]-gz*a[2]



def _height(plane, point):
    return plane[0]*point[0]+plane[1]*point[1]+plane[2]



def _clip_height(polygon, plane, expected, bound, positive):
    """Clip in plan against the same exact affine height comparison plane."""
    result = []
    for a, b in zip(polygon, polygon[1:]+polygon[:1]):
        va = _height(plane, a)-_height(expected, a)-bound
        vb = _height(plane, b)-_height(expected, b)-bound
        ia, ib = (va >= 0., vb >= 0.) if positive else (va <= 0., vb <= 0.)
        if ia:
            result.append(a)
        if ia != ib:
            fraction = va/(va-vb)
            require(0. <= fraction <= 1., 'HSR height clipping extrapolated outside a real edge')
            result.append(tuple(a[k]+fraction*(b[k]-a[k]) for k in (0, 1)))
    return result



def _component_union_area(polygons):
    """Integrate overlapping components; disjoint triangles need no slab scan."""
    if len(polygons) < 2:
        return sum(_area(poly) for poly in polygons)
    parents = list(range(len(polygons)))
    def find(index):
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index
    buckets = defaultdict(set)
    bounds = []
    for index, polygon in enumerate(polygons):
        xmin, xmax = min(p[0] for p in polygon), max(p[0] for p in polygon)
        zmin, zmax = min(p[1] for p in polygon), max(p[1] for p in polygon)
        bounds.append((xmin, xmax, zmin, zmax))
        candidates = set()
        keys = [(x, z) for x in range(math.floor(xmin), math.floor(xmax)+1)
                for z in range(math.floor(zmin), math.floor(zmax)+1)]
        for key in keys:
            candidates.update(buckets[key])
        for other in candidates:
            oxmin, oxmax, ozmin, ozmax = bounds[other]
            if min(xmax, oxmax)-max(xmin, oxmin) <= 1e-10 or min(zmax, ozmax)-max(zmin, ozmin) <= 1e-10:
                continue
            overlap = _intersection_polygon(polygon, polygons[other])
            if len(overlap) >= 3 and _area(overlap) > 1e-10:
                parents[find(index)] = find(other)
        for key in keys:
            buckets[key].add(index)
    groups = defaultdict(list)
    for index, polygon in enumerate(polygons):
        groups[find(index)].append(polygon)
    return sum(_polygon_union_area(group) for group in groups.values())



def _bed_index(triangles):
    floors, buckets = [], defaultdict(set)
    for triangle in triangles:
        # Audited native bed atlas strip. Undersides, parapets and support
        # caps use U below0.2158 and are independently checked elsewhere.
        if not all(.2158 <= vertex[3] <= 1.0042 for vertex in triangle):
            continue
        plane = _plane(triangle)
        if plane is None or math.hypot(plane[0], plane[1]) > .3:
            continue
        polygon = [(v[0], v[2]) for v in triangle]
        if _area(polygon) < 1e-10:
            continue
        index = len(floors)
        floors.append((polygon, plane))
        for x in range(math.floor((min(p[0] for p in polygon)-1e-4)/4.), math.floor((max(p[0] for p in polygon)+1e-4)/4.)+1):
            for z in range(math.floor((min(p[1] for p in polygon)-1e-4)/4.), math.floor((max(p[1] for p in polygon)+1e-4)/4.)+1):
                buckets[x, z].add(index)
    return floors, buckets



def _bed_overlap_index(floors, buckets):
    pairs, max_overlap, max_thickness = 0, 0., 0.
    bounds = [(min(p[0] for p in polygon), max(p[0] for p in polygon),
               min(p[1] for p in polygon), max(p[1] for p in polygon)) for polygon, _ in floors]
    for index in range(len(floors)):
        polygon, plane = floors[index]
        candidates = set()
        for x in range(math.floor((min(p[0] for p in polygon)-1e-4)/4.), math.floor((max(p[0] for p in polygon)+1e-4)/4.)+1):
            for z in range(math.floor((min(p[1] for p in polygon)-1e-4)/4.), math.floor((max(p[1] for p in polygon)+1e-4)/4.)+1):
                candidates.update(j for j in buckets[x, z] if j < index)
        # Each candidates set is unique and already restricted to other<index.
        # Consequently every unordered pair is visited exactly once, without
        # retaining a quadratic global set of previously compared pairs.
        for other in candidates:
            other_poly, other_plane = floors[other]
            xmin, xmax, zmin, zmax = bounds[index]
            oxmin, oxmax, ozmin, ozmax = bounds[other]
            # Disjoint bounds prove there is no positive intersection area.
            # Reject these before polygon clipping; no tolerance changes.
            if min(xmax, oxmax) <= max(xmin, oxmin) or min(zmax, ozmax) <= max(zmin, ozmin):
                continue
            overlap = _intersection_polygon(polygon, other_poly)
            if len(overlap) < 3 or _area(overlap) < 1e-10:
                continue
            # A stacked slab has the same X/Z area but a different actual
            # plane. Retain it. Only genuine coplanar duplicated area fails.
            if max(abs(_height(plane, p)-_height(other_plane, p)) for p in overlap) > .0001:
                continue
            pairs += 1
            area = _area(overlap)
            thickness = _minimum_strip_width(overlap)
            max_overlap, max_thickness = max(max_overlap, area), max(max_thickness, thickness)
            require(thickness <= .0001,
                    f'HSR has substantive coplanar rail-bed overlap: area {area:.8f} square metres, thickness {thickness:.8f} metres; '
                    f'triangles{index, other}, planes{plane, other_plane}, overlap{overlap}')
    return {'positive_area_coplanar_bed_pairs': pairs, 'maximum_coplanar_bed_overlap_area_m2': max_overlap,
            'maximum_coplanar_bed_overlap_thickness_m': max_thickness,
            'coplanar_overlap_meshing_tolerance_m': .0001}



def audit_bed_overlaps(triangles):
    """Fast independent audit of all native bed surfaces, including overhangs."""
    return _bed_overlap_index(*_bed_index(triangles))



def audit_bed_union(triangles, records, *, half_width=2.5):
    """Check exact full corridor areas on each actual grade, keeping both levels.

    The0.1m vertical matching bound is the existing native PATH-to-bed bound;
    planar areas still retain the reviewed1e-5m² hole tolerance and0.1mm
    coplanar-overlap thickness tolerance. Different heights never fill a hole.
    """
    floors, buckets = _bed_index(triangles)
    overlaps = _bed_overlap_index(floors, buckets)
    checked, worst = 0, 0.
    for _, _, points in records:
        for first, last in zip(points, points[1:]):
            a, b = (first[0], -first[1]), (last[0], -last[1])
            dx, dz = b[0]-a[0], b[1]-a[1]
            length2 = dx*dx+dz*dz
            length = math.sqrt(length2)
            normal = dz/length, -dx/length
            rectangle = [(p[0]+cross*normal[0], p[1]+cross*normal[1])
                         for p, cross in ((a, -half_width), (a, half_width), (b, half_width), (b, -half_width))]
            rise = _bed(last[2])-_bed(first[2])
            expected = rise*dx/length2, rise*dz/length2, _bed(first[2])-rise*(a[0]*dx+a[1]*dz)/length2
            candidates = set()
            for x in range(math.floor(min(p[0] for p in rectangle)/4.), math.floor(max(p[0] for p in rectangle)/4.)+1):
                for z in range(math.floor(min(p[1] for p in rectangle)/4.), math.floor(max(p[1] for p in rectangle)/4.)+1):
                    candidates.update(buckets[x, z])
            pieces = []
            for index in candidates:
                polygon, plane = floors[index]
                differences = [_height(plane, corner)-_height(expected, corner) for corner in rectangle]
                if min(differences) > .10 or max(differences) < -.10:
                    continue
                polygon = _intersection_polygon(polygon, rectangle)
                if len(polygon) < 3:
                    continue
                polygon = _clip_height(polygon, plane, expected, -.10, True)
                if len(polygon) < 3:
                    continue
                polygon = _clip_height(polygon, plane, expected, .10, False)
                if len(polygon) >= 3 and _area(polygon) > 1e-10:
                    pieces.append(polygon)
            # Planar slabs are integrated exactly, including triple overlaps;
            # adding triangle areas could hide a hole beneath duplicate faces.
            covered = _component_union_area(pieces)
            missing = max(0., _area(rectangle)-covered)
            worst = max(worst, missing)
            require(missing <= max(1e-5, _area(rectangle)*1e-6),
                    f'HSR train corridor has a hole in the actual placed rail bed at its height: {missing:.8f} square metres; {first} to {last}')
            checked += 1
    require(checked, 'HSR has no actual full-width bed corridor')
    return {'full_width_bed_union_segments_checked': checked, 'bed_union_width_m': 2.*half_width,
            'maximum_uncovered_bed_area_m2': worst, 'height_aware_bed_union_checked': True,
            **overlaps}



def audit_supports(triangles, contract):
    """Measure global foundations and all nine actual sloping head contacts."""
    triangles = list(triangles)
    bases = [[(v[0], v[2]) for v in tri] for tri in triangles if all(abs(v[1]) < 5e-5 for v in tri)]
    bases = [tri for tri in bases if _area(tri) > 1e-8]
    expected = contract['support_centres_xz']
    require(bool(bases) == bool(expected), 'HSR foundations differ from its literal support plan')
    parents = list(range(len(bases)))
    def find(index):
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index
    for i, a in enumerate(bases):
        for j, b in enumerate(bases[:i]):
            if (min(p[0] for p in a) > max(p[0] for p in b)+5e-5 or
                min(p[0] for p in b) > max(p[0] for p in a)+5e-5 or
                min(p[1] for p in a) > max(p[1] for p in b)+5e-5 or
                min(p[1] for p in b) > max(p[1] for p in a)+5e-5):
                continue
            require(_overlap(a, b) < 1e-7, 'HSR has overlapping or duplicate support foundations')
            if any(_inside(p, b) for p in a) or any(_inside(p, a) for p in b):
                parents[find(i)] = find(j)
    groups = defaultdict(list)
    for index, triangle in enumerate(bases):
        groups[find(index)].append(triangle)
    buckets = defaultdict(list)
    for triangle in triangles:
        for x in range(math.floor((min(p[0] for p in triangle)-1e-4)/4.), math.floor((max(p[0] for p in triangle)+1e-4)/4.)+1):
            for z in range(math.floor((min(p[2] for p in triangle)-1e-4)/4.), math.floor((max(p[2] for p in triangle)+1e-4)/4.)+1):
                buckets[x, z].append(triangle)
    centres, contacts, sloped = [], 0, 0
    width = contract['foundation_width_m']
    for group in groups.values():
        xs, zs = [p[0] for tri in group for p in tri], [p[1] for tri in group for p in tri]
        xmin, xmax, zmin, zmax = min(xs), max(xs), min(zs), max(zs)
        require(abs(xmax-xmin-width) < 5e-5 and abs(zmax-zmin-width) < 5e-5 and
                abs(sum(_area(tri) for tri in group)-width*width) < .0002,
                'HSR support foundation is incomplete, merged with a near duplicate, or not1.3m square')
        centre = ((xmin+xmax)/2., (zmin+zmax)/2.)
        centres.append(centre)
        candidates = {}
        for x in range(math.floor((xmin-1e-4)/4.), math.floor((xmax+1e-4)/4.)+1):
            for z in range(math.floor((zmin-1e-4)/4.), math.floor((zmax+1e-4)/4.)+1):
                for tri in buckets[x, z]:
                    candidates[id(tri)] = tri
        def column(tri):
            return all(xmin-5e-5 <= p[0] <= xmax+5e-5 and zmin-5e-5 <= p[2] <= zmax+5e-5 for p in tri)
        sides = [tri for tri in candidates.values() if column(tri) and min(p[1] for p in tri) <= 5e-5 and max(p[1] for p in tri) > 3.]
        require(sides, 'HSR foundation has no continuous elevated column')
        top_min = min(max(p[1] for p in tri) for tri in sides)
        top_max = max(max(p[1] for p in tri) for tri in sides)
        def head_grid(tri):
            return all(min(abs(p[0]-x) for x in (xmin, centre[0], xmax)) < 5e-5 and
                       min(abs(p[2]-z) for z in (zmin, centre[1], zmax)) < 5e-5 for p in tri)
        tops = [tri for tri in candidates.values() if column(tri) and head_grid(tri)
                and min(p[1] for p in tri) >= top_min-.4
                and max(p[1] for p in tri) <= top_max+5e-5 and _plane(tri) is not None]
        column_faces = {id(tri) for tri in sides+tops}
        head_polygons = [[(p[0], p[2]) for p in tri] for tri in tops]
        union_area, sum_area = _polygon_union_area(head_polygons), sum(_area(poly) for poly in head_polygons)
        require(abs(union_area-width*width) <= .0002 and abs(sum_area-width*width) <= .0002,
                f'HSR support head has an incomplete or duplicated cap surface at{xmin, xmax, zmin, zmax}: '
                f'cap union{union_area:.9f}m², summed area{sum_area:.9f}m², faces{len(tops)}, wall tops{top_min, top_max}')
        measured = []
        for x in (xmin, centre[0], xmax):
            for z in (zmin, centre[1], zmax):
                head = [sum(p[1]*w for p, w in zip(tri, weights)) for tri in tops if (weights := _weights(x, z, tri))]
                require(head, 'HSR support head has a hole at a required contact point')
                top = max(head)
                roofs = []
                for tri in candidates.values():
                    if id(tri) in column_faces or max(p[1] for p in tri) < top-.001 or _plane(tri) is None:
                        continue
                    weights = _weights(x, z, tri)
                    if weights:
                        roof = sum(p[1]*w for p, w in zip(tri, weights))
                        if roof >= top-.001:
                            roofs.append(roof)
                require(roofs and -.001 <= min(roofs)-top <= .021,
                        'HSR support head floats below or cuts through its actual sloped deck underside')
                measured.append(top)
                contacts += 1
        if max(measured)-min(measured) > .001:
            sloped += 1
    minimum = min((math.dist(a, b) for i, a in enumerate(centres) for b in centres[:i]), default=None)
    require(minimum is None or minimum >= contract['minimum_support_spacing_m']-5e-5,
            'HSR near-duplicate support columns are too close across placed meshes')
    require(len(centres) == len(expected) and all(any(math.dist(a, b) < 5e-5 for b in centres) for a in expected),
            'HSR support centres differ from the independent consolidated plan')
    return {'support_columns_checked': len(centres), 'support_contact_points_checked': contacts,
            'sloped_support_heads_checked': sloped, 'global_support_spacing_checked': True,
            'minimum_support_centre_distance_m': minimum, 'support_tops_touch_deck': True,
            'support_centres_sc4path_xy': sorted((round(x, 6), round(-z, 6)) for x, z in centres)}
