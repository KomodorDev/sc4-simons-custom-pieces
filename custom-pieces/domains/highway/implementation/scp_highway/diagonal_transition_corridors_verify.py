"""Finite full-width support and clearance from certified saved roof fields.

The complete surface/source checker must run before this reader. Coordinates
are world east, north, and height; native cells are an explicit independently
reviewed input, never inferred from a route or from a missing owned surface.
"""
from __future__ import annotations

import math

from shapely.geometry import Polygon, Point, box
from shapely.ops import unary_union
from shapely.strtree import STRtree

from scp.dbpf import require

POSITION_EPS = 4e-6
HALF_WIDTH = 1.25
VEHICLE_HEIGHT = 3.8
COMPONENTS = ('upper', 'lower')


def _normal(points):
    a, b, c = points
    u = tuple(y-x for x, y in zip(a, b))
    v = tuple(y-x for x, y in zip(a, c))
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])


def _plane(points):
    nx, ny, nz = _normal(points)
    require(nz > 0., 'Certified corridor pavement must point upward')
    x, y, h = points[0]
    gx, gy = -nx/nz, -ny/nz
    return gx, gy, h-gx*x-gy*y


def _clip(points, field, *, strict=False):
    if not points:
        return []
    values = [sum(field[i]*point[i] for i in range(3))+field[3] for point in points]
    if strict and max(values) <= 0.:
        return []
    result = []
    previous, a = points[-1], values[-1]
    for current, b in zip(points, values):
        if (a >= 0.) != (b >= 0.):
            t = a/(a-b)
            result.append(tuple(x+t*(y-x) for x, y in zip(previous, current)))
        if b >= 0.:
            result.append(current)
        previous, a = current, b
    return result


def _clip_xy(points, polygon):
    ring = list(polygon.exterior.coords)[:-1]
    if sum(a[0]*b[1]-a[1]*b[0] for a, b in zip(ring, (*ring[1:], ring[0]))) < 0.:
        ring.reverse()
    for a, b in zip(ring, (*ring[1:], ring[0])):
        dx, dy = b[0]-a[0], b[1]-a[1]
        points = _clip(points, (-dy, dx, 0., dy*a[0]-dx*a[1]))
        if not points:
            break
    return points


def _intrinsic_polygon(points, axes):
    if len(points) < 3:
        return Polygon()
    result = Polygon([(point[axes[0]], point[axes[1]]) for point in points])
    require(result.is_valid or result.area == 0.,
            'Finite corridor clipping produced an invalid obstacle polygon')
    return result


def _cells(value, description):
    result = set()
    for cell in value:
        require(len(cell) == 2 and all(type(n) is int for n in cell), description+' must use integer world cells')
        require(tuple(cell) not in result, description+' repeats a world cell')
        result.add(tuple(cell))
    return result


def _cell_mask(cells):
    return unary_union([box(16*c-8, -16*r-8, 16*c+8, -16*r+8) for c, r in cells])


def _strip(first, last):
    dx, dy = last[0]-first[0], last[1]-first[1]
    length = math.hypot(dx, dy)
    require(length > 0., 'Saved corridor chord has zero horizontal length')
    nx, ny = -dy/length*HALF_WIDTH, dx/length*HALF_WIDTH
    return Polygon([(first[0]-nx, first[1]-ny), (last[0]-nx, last[1]-ny),
                    (last[0]+nx, last[1]+ny), (first[0]+nx, first[1]+ny)])


def _unoccluded_intrusion(face, clipped, roofs, strip):
    """Subtract only finite portions at/below the actual local roof maximum.

    All clipping is performed in 3D, and area is measured in the obstacle's
    own plane, so a vertical wall cannot disappear in a zero-area XY view.
    """
    normal = _normal(face['points'])
    dropped = max(range(3), key=lambda i: abs(normal[i]))
    axes = tuple(i for i in range(3) if i != dropped)
    whole = _intrinsic_polygon(clipped, axes)
    if whole.area == 0.:
        return 0.
    middle = tuple(sum(point[i] for point in clipped)/len(clipped) for i in range(3))
    if (not any(strip.contains(Point(*point[:2])) for point in clipped)
            and not strip.contains(Point(*middle[:2]))):
        return 0.
    assigned = [_intrinsic_polygon(_clip_xy(clipped, roof['polygon']), axes) for roof in roofs]
    unassigned = whole.difference(unary_union(assigned))
    # The 4um plan coverage admission must not make an obstacle disappear
    # between exact roof patches. With no exact local height assignment,
    # fail closed instead of extrapolating a roof plane into that gap.
    if unassigned.area > 0.:
        return unassigned.area
    for index, roof in enumerate(roofs):
        gx, gy, c = roof['field']
        candidate = _clip_xy(clipped, roof['polygon'])
        candidate = _clip(candidate, (-gx, -gy, 1., -c-POSITION_EPS), strict=True)
        candidate = _clip(candidate, (gx, gy, -1., c+VEHICLE_HEIGHT-POSITION_EPS), strict=True)
        region = _intrinsic_polygon(candidate, axes)
        if region.area == 0.:
            continue
        # A finite triangle on the corridor's side/end curtain merely touches
        # the strip. Its interior must enter the actual open XY footprint.
        if not any(strip.contains(Point(*point[:2])) for point in candidate):
            middle = tuple(sum(point[i] for point in candidate)/len(candidate) for i in range(3))
            if not strip.contains(Point(*middle[:2])):
                continue
        obscured = []
        for other_index, other in enumerate(roofs):
            if other_index == index:
                continue
            qx, qy, qc = other['field']
            below = _clip_xy(candidate, other['polygon'])
            below = _clip(below, (qx, qy, -1., qc+POSITION_EPS))
            patch = _intrinsic_polygon(below, axes)
            if patch.area > 0.:
                obscured.append(patch)
        uncovered = region.difference(unary_union(obscured)) if obscured else region
        if uncovered.area > 0.:
            return uncovered.area
    return 0.


def check_corridors(faces, routes, *, owned_cells, native_routes=(), native_cells=None):
    """Prove complete 2.5m strips and 3.8m clearance above finite saved roofs.

    Only previously certified upward pavement for the same component may
    support a route. Every obstacle face, including complete supports and
    original native references, is considered. Native approach strips use
    the same checks; their unowned wedges must fit explicit native cells.
    """
    faces, routes, native_routes = list(faces), list(routes), list(native_routes)
    owned = _cells(owned_cells, 'Owned mask')
    require(owned, 'Corridor check needs the reviewed owned mask')
    native_cells = {} if native_cells is None else dict(native_cells)
    require(set(native_cells) <= set(COMPONENTS), 'Native corridor cell scope has an unknown component')
    native = {key: _cells(native_cells.get(key, ()), 'Pinned native mask') for key in COMPONENTS}
    require(all(not owned.intersection(value) for value in native.values()),
            'Native corridor allowance must not relabel an owned cell')
    owned_mask = _cell_mask(owned)
    native_masks = {key: _cell_mask(value) for key, value in native.items()}
    indexed, roofs_by_component = [], {key: [] for key in COMPONENTS}
    for face in faces:
        points = tuple(tuple(float(value) for value in point) for point in face['points'])
        require(len(points) == 3 and all(len(p) == 3 and all(math.isfinite(v) for v in p) for p in points),
                'Corridor obstacle needs a finite decoded triangle')
        normal = _normal(points)
        require(any(normal), 'Corridor input contains a zero-area saved triangle')
        row = {**face, 'points': points, 'polygon': Polygon([p[:2] for p in points]),
               'minimum_h': min(p[2] for p in points), 'maximum_h': max(p[2] for p in points)}
        indexed.append(row)
        if face['kind'] == 'pavement' and normal[2] > 0.:
            require(face['deck'] in COMPONENTS, 'Certified pavement has no reviewed component')
            row['field'] = _plane(points)
            roofs_by_component[face['deck']].append(row)
    require(indexed and routes, 'Corridor check requires actual obstacles and saved journeys')
    obstacle_tree = STRtree([face['polygon'] for face in indexed])
    roof_trees = {key: STRtree([face['polygon'] for face in rows]) for key, rows in roofs_by_component.items()}
    segments = native_segments = tested = roof_patches = wedges = 0
    outside_sum = 0.
    for is_native, selected in ((False, routes), (True, native_routes)):
        for route in selected:
            component = route.get('component', route.get('deck'))
            require(component in COMPONENTS, 'Saved corridor journey lacks its reviewed component')
            points = [tuple(float(v) for v in point) for point in route['points']]
            require(len(points) >= 2 and all(len(p) == 3 and all(math.isfinite(v) for v in p) for p in points),
                    'Saved corridor journey needs finite world ENH points')
            for first, last in zip(points, points[1:]):
                strip = _strip(first, last)
                outside = strip.difference(owned_mask)
                require(outside.difference(native_masks[component]).area == 0.,
                        f'Saved {component} full-width strip enters an unowned non-native cell: {first}, {last}')
                if outside.area > 0.:
                    wedges += 1
                    outside_sum += outside.area
                local = []
                for at in roof_trees[component].query(strip):
                    roof = roofs_by_component[component][int(at)]
                    if roof['polygon'].intersects(strip):
                        local.append(roof)
                require(local, 'Saved diagonal full-width corridor has no certified finite pavement')
                plan = unary_union([roof['polygon'] for roof in local])
                # The inscribed round buffer is conservative: every admitted
                # XY point is within the single declared 4um finite bound.
                missing = strip.difference(plan.buffer(POSITION_EPS, quad_segs=32))
                require(missing.area == 0.,
                        f'Saved {component} full-width corridor lacks inside-owned/native pavement: {first}, {last}; area={missing.area}; inside_owned={missing.intersection(owned_mask).area}; outside_owned={missing.difference(owned_mask).area}')
                roof_patches += len(local)
                low = min(roof['minimum_h'] for roof in local)
                high = max(roof['maximum_h'] for roof in local)
                for at in obstacle_tree.query(strip):
                    face = indexed[int(at)]
                    if face['maximum_h'] <= low or face['minimum_h'] >= high+VEHICLE_HEIGHT:
                        continue
                    if (face['kind'] == 'pavement' and face.get('deck') == component
                            and _normal(face['points'])[2] > 0.):
                        # Its own finite plane is one member of the maximum;
                        # it is mathematically at/below that local envelope.
                        continue
                    clipped = _clip_xy(list(face['points']), strip)
                    # Discard only heights known to be below EVERY local
                    # finite roof, or above EVERY possible vehicle ceiling.
                    # No position tolerance is spent by these exact bounds.
                    clipped = _clip(clipped, (0., 0., 1., -low), strict=True)
                    clipped = _clip(clipped, (0., 0., -1., high+VEHICLE_HEIGHT), strict=True)
                    if len(clipped) < 3:
                        continue
                    tested += 1
                    intrusion = _unoccluded_intrusion(face, clipped, local, strip)
                    require(intrusion == 0.,
                            f'Saved diagonal obstacle enters finite vehicle clearance above the local roof: {face["role"]}; component={component}; area={intrusion}; chord={first},{last}')
                segments += 1
                native_segments += int(is_native)
    return {'passed': True, 'continuous_saved_segments_checked': segments-native_segments,
            'native_approach_segments_checked': native_segments,
            'actual_face_prism_intersections_checked': tested, 'finite_roof_patches_checked': roof_patches,
            'outside_owned_segment_wedges_checked': wedges,
            'sum_segment_outside_owned_plan_area_m2': outside_sum,
            'half_width_m': HALF_WIDTH, 'height_m': VEHICLE_HEIGHT,
            'finite_position_bound_m': POSITION_EPS,
            'local_finite_roof_envelope_used': True, 'centreline_datum_broadcast': False,
            'scope': 'Continuous full-width saved/native strips and finite local-roof obstacle clearance, after complete source-surface certification; no game or structural-capacity result.'}
