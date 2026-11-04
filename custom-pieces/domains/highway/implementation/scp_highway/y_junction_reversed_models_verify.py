"""Read actual reversed S3D faces against fresh finite native source geometry.

The original physical reader supplies generic triangle, shell, vehicle, and
support tests. Every native phase, surface datum, ownership allowance, and
analysis-only source scope is selected explicitly here. No writer is imported.
"""
from __future__ import annotations

import hashlib
import math
import re
from copy import deepcopy
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import numpy as np
import shapely
from shapely.geometry import LineString, Point, Polygon, MultiPoint, box
from shapely.strtree import STRtree
from shapely.ops import unary_union

from scp import jsonc
from scp.dbpf import require
from . import y_junction_models_verify as physical
from . import y_junction_reversed_verify as contract
from . import y_junction_reversed_native_models as native
from .ramp_verify import _barycentric

POSITION_EPS = physical.POSITION_EPS
C_JOIN_EAST = 55.99899959564209
C_SOUTH_NORTH = -8.00100040435791
C_MODEL_SHA256 = '3d94bcce2ff84c9bd06d3bbbc7a089b8eaa28cfe921c3d31e87a27300cffd3dd'
C_ROLE = re.compile(r'^(pavement|body|barrier)-native-C-(upper|lower)-(retained-core-collar|retained-contact)$')


def _context(donors):
    context = physical._context(donors)
    from .y_junction_approaches import NATIVE_DEPENDENCY_SHA256
    flat = {key: raw for group in context.values() for key, raw in group.items()}
    require(all(key in flat and hashlib.sha256(flat[key]).hexdigest() == digest
                for key, digest in NATIVE_DEPENDENCY_SHA256.items()),
            'Reversed physical verification requires all exact pinned native source resources')
    return context


def _face(points, uv, role, material, *, owner=None):
    points = tuple(tuple(p) for p in points)
    normal = physical._normal(points)
    reference = {'native-reference-C-owned-roof': 'pavement', 'native-reference-C-owned-body': 'body',
                 'native-reference-C-owned-barrier': 'barrier'}
    return {'points': points, 'uv': tuple(tuple(p) for p in uv), 'role': role,
            'kind': reference[role] if role in reference else physical._kind(role, variant='reversed'),
            'material': material, 'upward': normal[2] > 1e-12,
            'downward': normal[2] < -1e-12, 'owner_cell': owner}


def _coded(faces):
    roles = list(dict.fromkeys(face['role'] for face in faces))
    materials = {face['role']: face['material'] for face in faces}
    triangles = [tuple((p[0], p[2], -p[1], *uv, float(roles.index(face['role'])))
                       for p, uv in zip(face['points'], face['uv'])) for face in faces]
    return triangles, roles, materials


def _clip(vertices, *planes):
    for plane in planes:
        vertices = physical._clip_linear_polygon(vertices, plane)
    return vertices


def _triangulated(face, vertices):
    for k in range(1, len(vertices)-1):
        triangle = [vertices[0], vertices[k], vertices[k+1]]
        if np.linalg.norm(physical._normal([p[:3] for p in triangle])) > 1e-13:
            yield {**face, 'points': tuple(p[:3] for p in triangle), 'uv': tuple(p[3:] for p in triangle)}


def _area(vertices):
    return sum(float(np.linalg.norm(physical._normal([vertices[0][:3], vertices[k][:3], vertices[k+1][:3]])))/2.
               for k in range(1, len(vertices)-1))


def _bounds(points):
    return None if not points else [[min(p[k] for p in points) for k in range(3)],
                                    [max(p[k] for p in points) for k in range(3)]]


def native_cell_bounds(donors):
    """Only literal C core source faces may occupy their exact south fringe."""
    context = _context(donors)
    result = {}
    for group in native.retained_core_collar_faces(context):
        role = f"{group['role']}-native-C-{group['deck']}-retained-core-collar"
        points = [p for row in group['fragments'] for p in row['triangle']]
        require(group['pose'] == 1 and group['source_sha256'] == C_MODEL_SHA256
                and min(-p[2] for p in points) >= C_SOUTH_NORTH-1e-12
                and max(p[0] for p in points) <= 56.,
                'Reversed C literal native fringe exceeds its independently measured source')
        # S3D local coordinates are east, height, south. The owner is (3,0).
        result[((3, 0), role)] = (-8., 8., -8., max(8., max(p[2] for p in points)))
    return result


def _roof_regions(context):
    """Derive source finite roofs directly, without calling the collar writer."""
    regions = {'upper': [], 'lower': []}
    for arm in ('A', 'B', 'C'):
        inward = native.SOCKETS[arm]['inward_en']
        for group in native.posed_native_faces(context, arm):
            if group['role'] != 'pavement':
                continue
            for triangle in group['triangles']:
                polygon = Polygon([(p[0], -p[2]) for p in triangle])
                if polygon.area > 1e-14:
                    regions[group['deck']].append((polygon, triangle[0][1]))
        if arm == 'C':
            continue
        for deck in ('upper', 'lower'):
            for group in native.native_forward_sections(context, arm, deck):
                if group['role'] != 'pavement':
                    continue
                for row in group['segments']:
                    a, b = row['points']
                    require(abs(a[1]-b[1]) < 1e-12, 'Native flat source roof is not horizontal')
                    polygon = Polygon([(a[0], -a[2]), (b[0], -b[2]),
                                       (b[0]+3.*inward[0], -b[2]+3.*inward[1]),
                                       (a[0]+3.*inward[0], -a[2]+3.*inward[1])])
                    if polygon.area > 1e-14:
                        regions[deck].append((polygon, a[1]))
    # A source302 nominal roof must not claim the measured raised309 region.
    result = {}
    for deck, rows in regions.items():
        nominal = 15. if deck == 'upper' else 7.5
        low = unary_union([p for p, h in rows if abs(h-nominal) < 1e-12])
        high = unary_union([p for p, h in rows if abs(h-nominal-physical.datum(nominal)) < 1e-10])
        require(all(abs(h-nominal) < 1e-12 or abs(h-nominal-physical.datum(nominal)) < 1e-10
                    for _p, h in rows), 'Unexpected reversed native source roof height')
        result[deck] = low.difference(high)
    return result


@dataclass(frozen=True)
class SourceFloorField:
    """Immutable finite nominal302 domains; no author mesh supplies this field."""
    domains: tuple
    interior_domains: tuple = field(init=False, repr=False)

    def __post_init__(self):
        require(type(self.domains) is tuple and len(self.domains) == 2,
                'Source floor domains must be an immutable two-deck configuration')
        object.__setattr__(self, 'interior_domains', tuple(region.buffer(-POSITION_EPS) for region in self.domains))

    def _domain(self, nominal):
        return self.domains[0 if nominal == 15. else 1]

    @lru_cache(maxsize=256)
    def _partitions(self, first, last, nominal):
        strip = _vehicle_polygon(first, last, inset=True)
        interior = self.interior_domains[0 if nominal == 15. else 1]
        if interior.covers(strip):
            return 'low', ()
        if not interior.intersects(strip):
            return 'high', ()
        inside = strip.intersection(interior)
        return 'split', tuple((region, tuple(triangle for part in _polygons(geometry)
            for triangle in shapely.constrained_delaunay_triangles(part).geoms))
            for region, geometry in ((0, inside), (1, strip.difference(inside))))

    def __call__(self, start, end):
        nominal = start[2]
        if abs(end[2]-nominal) > 1e-10 or nominal not in (7.5, 15.):
            yield start, end, (*start[:2], start[2]+physical.datum(start[2])), (*end[:2], end[2]+physical.datum(end[2]))
            return
        region = self._domain(nominal)
        line = LineString([start[:2], end[:2]])
        cuts = [0., 1.]
        crossing = line.intersection(region.boundary)
        members = list(getattr(crossing, 'geoms', (crossing,)))
        for member in members:
            for p in getattr(member, 'coords', ()):
                cuts.append(line.project(Point(p))/line.length)
        cuts = sorted(set(max(0., min(1., t)) for t in cuts))
        for low, high in zip(cuts, cuts[1:]):
            if high-low <= 1e-13:
                continue
            a, b = (tuple(start[k]+t*(end[k]-start[k]) for k in range(3)) for t in (low, high))
            middle = line.interpolate((low+high)*.5, normalized=True)
            offset = 0. if region.covers(middle) else physical.datum(nominal)
            yield a, b, (*a[:2], nominal+offset), (*b[:2], nominal+offset)

    def intrudes(self, first, last, face):
        if abs(first[2]-last[2]) > 1e-10:
            return physical._intrudes(first, last, face)
        nominal = min((7.5, 15.), key=lambda h: abs(first[2]-h))
        if abs(first[2]-nominal) > .002:
            return physical._intrudes(first, last, face)
        raised = nominal+physical.datum(nominal)
        heights = [p[2] for p in face['points']]
        if max(heights) <= nominal+POSITION_EPS or min(heights) >= raised+3.8:
            return False
        # A saved vertical riser can move only within the existing Euclidean
        # float32 bound. Its upper adjacent source floor owns that finite
        # boundary capsule; this is no vertical-height tolerance increase.
        kind, partitions = self._partitions(tuple(first), tuple(last), nominal)
        if kind == 'low':
            return physical._intrudes((*first[:2], nominal), (*last[:2], nominal), face)
        if kind == 'high':
            return physical._intrudes((*first[:2], raised), (*last[:2], raised), face)
        bottom = .03 if face['kind'] == 'pavement' else POSITION_EPS
        for region, triangles in partitions:
            floor = nominal if region == 0 else raised
            for triangle in triangles:
                clipped = physical._clip_xy_prism(face['points'], triangle)
                clipped = _clip(clipped, (0., 0., 1., -floor-bottom),
                                (0., 0., -1., floor+3.8-1e-5))
                if _area(clipped) > 1e-12:
                    return True
        return False


def _polygons(geometry, *, minimum_area=1e-15):
    if geometry.geom_type == 'Polygon':
        return [geometry] if geometry.area > minimum_area else []
    return [part for child in getattr(geometry, 'geoms', ())
            for part in _polygons(child, minimum_area=minimum_area)]


def _vehicle_polygon(first, last, *, inset=False):
    dx, dy = last[0]-first[0], last[1]-first[1]
    length = math.hypot(dx, dy)
    width = 1.25-(1e-5 if inset else 0.)
    normal = (-dy/length*width, dx/length*width)
    a, b = first, last
    if inset:
        a = tuple(first[k]+1e-8*(last[k]-first[k]) for k in range(3))
        b = tuple(first[k]+(1.-1e-8)*(last[k]-first[k]) for k in range(3))
    return Polygon([(p[0]+s*normal[0], p[1]+s*normal[1]) for p, s in ((a, 1), (b, 1), (b, -1), (a, -1))])


def source_floor_segments(donors):
    """Measure piecewise source302 floor heights across the entire road width."""
    domains = _roof_regions(_context(donors))
    return SourceFloorField((domains['upper'], domains['lower']))


def _plane_field(face):
    return np.linalg.solve(np.array([[p[0], p[1], 1.] for p in face['points']]),
                           np.array([p[2] for p in face['points']]))


def _distance_to_finite_triangle(point, triangle):
    """True3D distance; an outside projection must use a finite edge."""
    point = np.asarray(point)
    a, b, c = np.asarray(triangle)
    ab, ac = b-a, c-a
    normal = np.cross(ab, ac)
    square = float(normal@normal)
    if square > 0.:
        projection = point-normal*float(normal@(point-a))/square
        uv = np.linalg.lstsq(np.column_stack((ab, ac)), projection-a, rcond=None)[0]
        if min(uv) >= 0. and sum(uv) <= 1.:
            return float(np.linalg.norm(point-projection))
    distances = []
    for first, last in ((a, b), (b, c), (c, a)):
        direction = last-first
        length2 = float(direction@direction)
        fraction = 0. if length2 == 0. else min(1., max(0., float((point-first)@direction)/length2))
        distances.append(float(np.linalg.norm(point-first-fraction*direction)))
    return min(distances)


def body_depth_coverage(roof, patch, floors, *, precision=None):
    """Finite actual same-slab coverage at least1m below an actual roof patch."""
    floors = [face for face in floors if face['kind'] == 'body' and face['downward']
              and face['role'] == 'body' and not face.get('native_reference')]
    rx, ry, rc = _plane_field(roof)
    coverage = []
    for floor in floors:
        overlap = patch.intersection(Polygon([p[:2] for p in floor['points']]))
        if overlap.area <= 1e-14:
            continue
        fx, fy, fc = _plane_field(floor)
        for part in _polygons(overlap):
            vertices = [(p[0], p[1], 0.) for p in list(part.exterior.coords)[:-1]]
            # Select this served1m slab's source-height envelope; a lower
            # unrelated travel deck cannot replace an absent upper floor.
            clipped = _clip(vertices, (rx-fx, ry-fy, 0., rc-fc-1.+POSITION_EPS),
                             (fx-rx, fy-ry, 0., fc-rc+1.+physical.DATUM_UPPER+POSITION_EPS))
            if len(clipped) >= 3:
                # Interior XY coverage already spends any vertical error.
                # Edge/vertex admissions below use a SINGLE true3D budget.
                coverage.append(Polygon([p[:2] for p in clipped]))
    covered = unary_union(coverage)
    # A valid adjacent floor triangle can have only edge contact in XY.
    # Its finite3D capsule still supports nearby encoded roof corners. Never
    # discard that evidence merely because the planar overlap has zero area.
    remaining = _polygons(patch.difference(covered), minimum_area=0.)
    proved = 0
    def certify(region, floor):
        hull = region.convex_hull
        points = list(hull.exterior.coords)[:-1] if hull.geom_type == 'Polygon' else list(hull.coords)
        targets = [(x, y, float(rx*x+ry*y+rc-1.)) for x, y in points]
        maximum = max(_distance_to_finite_triangle(point, floor['points']) for point in targets)
        if maximum > POSITION_EPS:
            return False
        if precision is not None:
            precision['exact_convex_patch_admissions'] += 1
            precision['maximum_admitted_euclidean_distance_m'] = max(
                precision['maximum_admitted_euclidean_distance_m'], maximum)
        return True
    for region in remaining:
        for floor in floors:
            if certify(region, floor):
                # Distance to one convex finite triangle is convex. Bounding
                # every lifted hull vertex bounds its entire planar hull,
                # including its interior, under ONE combined3D budget.
                coverage.append(region)
                proved += 1
                break
        else:
            # A seam can span several actual floor triangles. Partition its
            # target polygon into candidate neighbourhoods, then prove EACH
            # convex part against ONE finite triangle using true3D distance.
            # The XY search buffer supplies no admission or extra tolerance.
            hull = region.convex_hull
            xy = list(hull.exterior.coords)[:-1] if hull.geom_type == 'Polygon' else list(hull.coords)
            pending = [[(x, y, float(rx*x+ry*y+rc-1.)) for x, y in xy]]
            for floor in floors:
                search = Polygon([p[:2] for p in floor['points']]).buffer(POSITION_EPS/2., quad_segs=8)
                ring = list(search.exterior.coords)[:-1]
                if sum(a[0]*b[1]-a[1]*b[0] for a, b in zip(ring, (*ring[1:], ring[0]))) < 0.:
                    ring.reverse()
                fields = [(-b[1]+a[1], b[0]-a[0], 0., (b[1]-a[1])*a[0]-(b[0]-a[0])*a[1])
                          for a, b in zip(ring, (*ring[1:], ring[0]))]
                left = []
                for target in pending:
                    intersection = _clip(target, *fields)
                    maximum = max((_distance_to_finite_triangle(p, floor['points']) for p in intersection), default=math.inf)
                    if not intersection or maximum > POSITION_EPS:
                        left.append(target)
                        continue
                    # Split with actual half-spaces instead of a polygon
                    # overlay: even a positive femtometre-width seam keeps
                    # its vertices and receives a real finite-distance proof.
                    inside = target
                    for equation in fields:
                        values = [sum(equation[k]*p[k] for k in range(3))+equation[3] for p in inside]
                        if values and min(values) < 0.:
                            outside = _clip(inside, tuple(-v for v in equation))
                            if outside:
                                left.append(outside)
                        inside = _clip(inside, equation)
                        if not inside:
                            break
                    if precision is not None:
                        precision['exact_convex_patch_admissions'] += 1
                        precision['maximum_admitted_euclidean_distance_m'] = max(
                            precision['maximum_admitted_euclidean_distance_m'], maximum)
                pending = left
                if not pending:
                    break
            if not pending:
                coverage.append(region)
                proved += 1
    if remaining and proved == len(remaining):
        return patch
    return unary_union(coverage)


def check_full_underfloor(faces, roof_faces, routes, *, donors=None):
    """Prove1m authored body at every owned vehicle-strip roof point q.

    Exact city ownership clips only outside lateral endpoint wedges. Those
    wedges must remain inside the pinned native helper cell and its actual
    source roof; no spine, owned width, or C source prefix is omitted.
    """
    owned = unary_union([box(16*x-8., -16*y-8., 16*x+8., -16*y+8.)
                         for cells in contract.REVIEWED_OWNED_WORLD_CELLS for x, y in cells])
    segments = [(a, b) for route in routes for a, b in zip(route['points'], route['points'][1:])]
    strips = [_vehicle_polygon(a, b) for a, b in segments]
    strip_tree = STRtree(strips)
    inside = [strip.intersection(owned) for strip in strips]
    outside_by_helper = {}
    source_roofs = []
    for index, (strip, (first, last)) in enumerate(zip(strips, segments)):
        outside = strip.difference(owned)
        if outside.is_empty:
            continue
        require(donors is not None and abs(first[2]-last[2]) <= 1e-10,
                'An outside vehicle-width wedge lacks a pinned native helper or level endpoint')
        if not source_roofs:
            context = _context(donors)
            for arm in ('A', 'B', 'C'):
                for group in native.posed_native_faces(context, arm, False):
                    if group['role'] != 'pavement':
                        continue
                    cell = group['cell']
                    source_roofs.append((arm, group, box(16*cell[0]-8., -16*cell[1]-8.,
                                                       16*cell[0]+8., -16*cell[1]+8.),
                        unary_union([Polygon([(p[0], -p[2]) for p in triangle]) for triangle in group['triangles']])))
        candidates = [(arm, group) for arm, group, cell, roof in source_roofs
                      if abs((15. if group['deck'] == 'upper' else 7.5)-first[2]) <= 1e-10
                      and cell.covers(outside)
                      and roof.buffer(POSITION_EPS).covers(outside)]
        require(len(candidates) == 1,
                'An outside vehicle-width wedge escapes its exact required native helper cell or pinned roof')
        arm, group = candidates[0]
        key = arm, group['deck']
        entry = outside_by_helper.setdefault(key, {'source': group, 'parts': []})
        entry['parts'].append(outside)
    floors = [face for face in faces if face['kind'] == 'body' and face['downward']
              and face['role'] == 'body' and not face.get('native_reference')]
    floor_polygons = [Polygon([p[:2] for p in f['points']]) for f in floors]
    floor_tree = STRtree(floor_polygons)
    supported = [[] for _strip in strips]
    precision = {'finite_euclidean_position_bound_m': POSITION_EPS, 'exact_convex_patch_admissions': 0,
                 'maximum_admitted_euclidean_distance_m': 0.,
                 'method': 'Every lifted convex target-patch vertex lies within4µm of ONE actual finite authored floor triangle; convexity bounds the whole patch.'}
    checked = 0
    for roof in (f for f in roof_faces if f['kind'] == 'pavement' and f['upward']):
        polygon = Polygon([p[:2] for p in roof['points']])
        patches = []
        for index in strip_tree.query(polygon, predicate='intersects'):
            index = int(index)
            first, last = segments[index]
            dx, dy = last[0]-first[0], last[1]-first[1]
            square = dx*dx+dy*dy
            def error(p):
                fraction = ((p[0]-first[0])*dx+(p[1]-first[1])*dy)/square
                h = first[2]+fraction*(last[2]-first[2])
                return abs(p[2]-h-physical.datum(h))
            if max(error(p) for p in roof['points']) > .03:
                continue
            patch = polygon.intersection(inside[index])
            if patch.area > 1e-12:
                patches.append(patch)
                supported[index].append(patch)
        if not patches:
            continue
        patch = unary_union(patches)
        candidates = [floors[int(index)] for index in floor_tree.query(patch.buffer(POSITION_EPS), predicate='intersects')]
        uncovered = patch.difference(body_depth_coverage(roof, patch, candidates, precision=precision))
        require(uncovered.area <= 1e-18,
                'Reversed saved vehicle strip loses its full authored one-metre body below an actual roof: '
                +str({'roof_role': roof['role'], 'roof': roof['points'],
                      'uncovered_area_m2': uncovered.area, 'uncovered_bounds_en_m': list(uncovered.bounds)}))
        checked += 1
    require(all(region.is_empty or parts and region.difference(unary_union(parts).buffer(POSITION_EPS)).area <= 1e-18
                for region, parts in zip(inside, supported)),
            'Reversed full underside proof has no complete actual inside-owned vehicle-strip roof')
    outside_records = []
    for (arm, deck), entry in sorted(outside_by_helper.items()):
        region, source = unary_union(entry['parts']), entry['source']
        outside_records.append({'arm': arm, 'deck': deck, 'plan_area_m2': region.area,
            'bounds_en_m': list(region.bounds), 'native_helper_city_cell': source['cell'],
            'source_tile_id': source['donor'], 'source_pose': source['pose'],
            'source_model_sha256': source['source_sha256'], 'exact_helper_cell_containment': True,
            'actual_pinned_source_roof_coverage': True, 'numeric_position_bound_m': POSITION_EPS})
    return {'passed': True, 'actual_finite_roof_vehicle_strip_patches_checked': checked,
            'minimum_authored_body_depth_m': 1., 'full_vehicle_width_m': 2.5,
            'external_native_undersides_used': 0, 'finite_position_bound_m': POSITION_EPS,
            'finite_authored_floor_triangle_contact_proof': precision,
            'owned_mask_city_cells': 21, 'owned_mask_has_epsilon_buffer': False,
            'outside_lateral_wedges_by_helper_and_deck': outside_records,
            'outside_lateral_plan_area_sum_by_deck_m2': sum(row['plan_area_m2'] for row in outside_records),
            'no_spine_endpoint_or_inside_owned_width_waiver': True}


def owned_native_roof_references(donors, *, kinds=('pavement',)):
    """Independently reclip pinned C helper parents to the approved finite ROI."""
    context = _context(donors)
    require(type(kinds) is tuple and kinds and len(set(kinds)) == len(kinds)
            and set(kinds) <= {'pavement', 'body', 'barrier'},
            'C source interface requires explicit finite native role selection')
    actual = native.native_owned_interface_faces(context)
    sources = {g['mesh_index']: g for g in native.posed_native_faces(context, 'C', False)}
    expected, observed, records = {}, {}, []
    for mesh_index, group in sources.items():
        require(group['donor'] == '57530000' and group['pose'] == 1
                and group['source_sha256'] == C_MODEL_SHA256,
                'C owned roof reference requires its exact native donor, pose, and source hash')
        for index, parent in enumerate(group['triangles']):
            vertices = [(p[0], -p[2], p[1], p[3], p[4]) for p in parent]
            clipped = _clip(vertices, (1., 0., 0., -C_JOIN_EAST), (-1., 0., 0., 56.),
                            (0., 1., 0., 8.), (0., -1., 0., 8.))
            if _area(clipped) > 1e-13:
                expected[mesh_index, index] = clipped
    for group in actual:
        source = sources.get(group['mesh_index'])
        require(source is not None and group['donor'] == '57530000' and group['pose'] == 1
                and group['cell'] == [4, 0] and group['source_sha256'] == C_MODEL_SHA256
                and group['material']['raw'] == source['material']['raw']
                and group['role'] == source['role'] and group['deck'] == source['deck']
                and group['owned_analysis_bounds_en_m'] == [[C_JOIN_EAST, -8.], [56., 8.]]
                and group['reference_only_already_rendered_native'] is True
                and group['copy_into_custom_DAT_permitted'] is False
                and group['underside_or_car_corridor_waiver'] is False,
                'C native interface reference escapes its exact source or analysis-only bounds')
        for fragment in group['fragments']:
            index = fragment['face_index']
            parent = source['triangles'][index]
            triangle = fragment['triangle']
            require(tuple(map(tuple, fragment['parent_triangle'])) == tuple(map(tuple, parent)),
                    'C native interface provenance differs from the actual indexed source parent')
            a, b, c = np.asarray(parent)
            axes = np.column_stack((b[:3]-a[:3], c[:3]-a[:3]))
            normal = np.cross(axes[:, 0], axes[:, 1])
            actual_normal = np.cross(np.subtract(triangle[1][:3], triangle[0][:3]),
                                     np.subtract(triangle[2][:3], triangle[0][:3]))
            require(float(normal@actual_normal) > 0., 'C native reference reverses its source winding')
            for p in triangle:
                weights = np.linalg.lstsq(axes, np.subtract(p[:3], a[:3]), rcond=None)[0]
                require(min(weights) >= -1e-9 and sum(weights) <= 1.+1e-9
                        and np.linalg.norm(a[:3]+axes@weights-p[:3]) <= 1e-10
                        and np.max(np.abs(a[3:]+weights[0]*(b[3:]-a[3:])+weights[1]*(c[3:]-a[3:])-p[3:])) <= 1e-8
                        and C_JOIN_EAST-1e-12 <= p[0] <= 56.+1e-12
                        and -8.-1e-12 <= p[2] <= 8.+1e-12,
                        'C native reference escapes its finite parent XYZUV or exact approved ROI')
            points = tuple((p[0], -p[2], p[1]) for p in triangle)
            observed.setdefault((group['mesh_index'], index), []).append(points)
            if group['role'] in kinds:
                role = 'native-reference-C-owned-'+('roof' if group['role'] == 'pavement' else group['role'])
                face = _face(points, [p[3:] for p in triangle],
                             role, group['material'])
                require(group['role'] != 'pavement' or face['upward'], 'C required native roof reference points down')
                face['native_reference'] = True
                face['native_deck'] = group['deck']
                face['native_source'] = {'model_sha256': C_MODEL_SHA256, 'tile_id': '57530000',
                    'pose': 1, 'deck': group['deck'], 'mesh_index': group['mesh_index'], 'parent_face_index': index}
                records.append(face)
    require(set(expected) == set(observed), 'The required C native helper interface is absent or incomplete')
    for key, polygon in expected.items():
        source = sources[key[0]]['triangles'][key[1]]
        origin = np.asarray((source[0][0], -source[0][2], source[0][1]))
        first = np.asarray((source[1][0], -source[1][2], source[1][1]))-origin
        first /= np.linalg.norm(first)
        normal = np.cross(first, np.asarray((source[2][0], -source[2][2], source[2][1]))-origin)
        normal /= np.linalg.norm(normal)
        second = np.cross(normal, first)
        def projected(points):
            return Polygon([(float((np.asarray(p[:3])-origin)@first),
                             float((np.asarray(p[:3])-origin)@second)) for p in points])
        wanted = projected(polygon)
        found = unary_union([projected(points) for points in observed[key]])
        require(wanted.symmetric_difference(found).area <= 1e-10
                and abs(sum(projected(points).area for points in observed[key])-found.area) <= 1e-10,
                'C native reference loses part of its independently clipped finite source parent')
    require(records, 'The required real C native helper supplies no finite owned roof interface')
    return records


def write_native_interface_source_review(donors):
    """Freeze literal finite source witnesses, separately from physical acceptance."""
    context = _context(donors)
    checked = owned_native_roof_references(donors, kinds=('pavement', 'body', 'barrier'))
    groups, summary = [], []
    for source in native.native_owned_interface_faces(context):
        triangles = [row['triangle'] for row in source['fragments']]
        points = [(p[0], -p[2], p[1]) for triangle in triangles for p in triangle]
        summary.append({'role': source['role'], 'deck': source['deck'], 'source_faces': len(triangles),
                        'source_surface_area_m2': sum(_area(triangle) for triangle in triangles),
                        'finite_bounds_enh_m': _bounds(points)})
        groups.append({**{key: value for key, value in source.items() if key != 'material'},
            'material_raw_hex': source['material']['raw'].hex(),
            'material_sha256': hashlib.sha256(source['material']['raw']).hexdigest(),
            'material_texture_ids': list(source['material']['textures'])})
    report = {'schema_version': 1, 'passed': True,
        'scope': 'Literal already-rendered C helper source, exact finite clipping, XYZUV, material, and winding only; complete composed physical acceptance remains separate.',
        'source_model_tgi': '5ad0e817-badb57f1-57530000', 'source_model_sha256': C_MODEL_SHA256,
        'source_pose': 1, 'source_native_city_cell': [4, 0],
        'native_measurements_sha256': hashlib.sha256((contract.SUBJECT/'evidence/native-design-inputs.jsonc').read_bytes()).hexdigest(),
        'verifier_module_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'approved_finite_candidate_roi_en_m': [[C_JOIN_EAST, -8.], [56., 8.]],
        'approved_analysis_reference_roles': ['pavement', 'barrier'],
        'body_fragments_are_source_witnesses_only': True,
        'checked_source_fragments': len(checked), 'measurements': summary, 'source_groups': groups,
        'actual_analysis_source_usage': native_interface_skin(donors)[1],
        'actual_saved_faces_changed': False, 'copy_into_custom_DAT_permitted': False,
        'authored_body_or_floor_waiver': False, 'complete_physical_acceptance': False,
        'negative_controls': 'test_y_junction_reversed_verify checks missing helper, source pose, changed UV, enlarged ROI, deleted barrier fragment, absent authored floor, and absent boundary cap.'}
    target = contract.SUBJECT/'evidence/native-owned-interface-verification.jsonc'
    header = ('// title: "Exact reversed C native helper interface source review"\n'
              '// summary: "Pin the existing native helper profile fragments inside the finite owned boundary strip, without accepting composed physical geometry."\n'
              '// Used when: Reviewing the precise source contribution to the C owned-interface analysis.\n'
              '// Read by: The physical verification coordinator and native-interface reviewers.\n'
              '// Updated by: y_junction_reversed_models_verify.write_native_interface_source_review() after source controls pass.\n'
              '// Affects: Native source provenance only; actual authored floor, body, interference, and complete shell checks remain required.\n')
    target.write_text(jsonc.document(report, source=target.read_text() if target.exists() else header))
    return report


def _clip_roof_mask(face, mask):
    polygon = Polygon([p[:2] for p in face['points']])
    exterior = polygon.difference(mask)
    parts = [exterior] if exterior.geom_type == 'Polygon' else [
        p for p in getattr(exterior, 'geoms', ()) if p.geom_type == 'Polygon']
    result = []
    for part in parts:
        if part.area <= 1e-14:
            continue
        for triangle in shapely.constrained_delaunay_triangles(part).geoms:
            vertices = []
            for p in list(triangle.exterior.coords)[:3]:
                weights = _barycentric(p, face['points'])
                vertices.append((*p, sum(w*q[2] for w, q in zip(weights, face['points'])),
                                 *(sum(w*q[k] for w, q in zip(weights, face['uv'])) for k in (0, 1))))
            if physical._normal([p[:3] for p in vertices])[2] < 0.:
                vertices[1], vertices[2] = vertices[2], vertices[1]
            result.extend(_triangulated(face, vertices))
    return result, polygon.area-exterior.area


def native_interface_skin(donors):
    """Compose only exact source ROOF/BARRIER exterior within the finite C ROI."""
    source = owned_native_roof_references(donors, kinds=('pavement', 'barrier'))
    masks = {deck: unary_union([Polygon([p[:2] for p in face['points']])
        for face in source if face['kind'] == 'barrier' and face['native_deck'] == deck])
        for deck in ('upper', 'lower')}
    result, removed, hidden_points, trimmed = [], 0., [], []
    for face in source:
        require(face['native_source']['model_sha256'] == C_MODEL_SHA256
                and face['native_source']['tile_id'] == '57530000'
                and face['native_source']['pose'] == 1
                and face['native_deck'] == face['native_source']['deck'],
                'C intrinsic source union requires the same actual pinned model and pose')
        if face['kind'] != 'pavement':
            result.append(face)
            continue
        hidden = Polygon([p[:2] for p in face['points']]).intersection(masks[face['native_deck']])
        kept, area = _clip_roof_mask(face, masks[face['native_deck']])
        require(abs(area-hidden.area) <= 1e-12, 'C source union mask exceeds its actual finite source overlap')
        result.extend(kept)
        removed += area
        if hidden.area > 0.:
            fx, fy, fc = _plane_field(face)
            points = [(x, y, float(fx*x+fy*y+fc)) for part in _polygons(hidden)
                      for x, y in list(part.exterior.coords)[:-1]]
            hidden_points.extend(points)
            trimmed.append({'deck': face['native_deck'], **face['native_source'],
                            'removed_source_roof_plan_area_m2': hidden.area,
                            'removed_source_roof_bounds_enh_m': _bounds(points)})
    evidence = {'source_model_sha256': C_MODEL_SHA256, 'source_native_tile_id': '57530000', 'source_pose': 1,
        'source_roles': ['pavement', 'barrier'], 'source_body_reference_faces_used': 0,
        'reference_source_fragments': len(source), 'analysis_reference_faces': len(result),
        'reference_source_counts': {kind: sum(f['kind'] == kind for f in source) for kind in ('pavement', 'barrier')},
        'finite_bounds_enh_m': _bounds([p for f in source for p in f['points']]),
        'roof_plan_area_m2': sum(Polygon([p[:2] for p in f['points']]).area for f in result if f['kind'] == 'pavement'),
        'intrinsic_source_roof_union': {
            'same_pinned_model_pose_and_deck_only': True, 'source_roof_fragments_trimmed': len(trimmed),
            'removed_source_roof_plan_area_m2': removed, 'removed_source_roof_bounds_enh_m': _bounds(hidden_points),
            'actual_finite_source_overlap_by_parent': trimmed, 'new_authored_faces_trimmed': 0,
            'actual_DAT_interference_and_floor_faces_changed': False},
        'copy_into_custom_DAT_permitted': False, 'full_authored_one_metre_underside_required': True,
        'closure_scope': 'Actual authored skin plus exact already-rendered native helper roof/barrier exterior; source BODY fragments are not added.'}
    return result, evidence


def external_skin(faces, donors):
    """Fresh source-only intrinsic roof masks and literal south C fringe.

    The actual saved mesh stays unchanged. No original peer302 body or
    endpoint-prefix allowance is inherited. The source-only C helper roof
    composes a finite hybrid interface over the required full authored floor.
    """
    context = _context(donors)
    certificate = native.certify_native_collars(*_coded(faces), context)
    require(not certificate.get('buried_peer_body_regions'),
            'The reversed variant has no approved buried native body scope')
    certified = set(certificate['certified_face_indices'])
    masks = certificate['internal_pavement_masks']
    helper_rows = certificate.get('buried_helper_body_regions', [])
    helper_regions = {row['face_index']: row for row in helper_rows}
    require(len(helper_regions) == len(helper_rows), 'Duplicate certified helper-body analysis region')
    result, removed_roof = [], 0.
    fringe_area = fringe_roof_area = 0.
    fringe_points, fringe_count = [], 0
    helper_area, helper_points, helper_counts = 0., [], {}
    for index, face in enumerate(faces):
        current = [face]
        if index in helper_regions:
            row = helper_regions[index]
            matched = re.fullmatch(r'body-native-([AB])-(upper|lower)-helper', face['role'])
            require(matched is not None and index in certified and row['role'] == face['role'],
                    'Reversed helper-body scope requires its exact certified source face')
            nominal = 15. if matched[2] == 'upper' else 7.5
            from .y_junction_approaches import NATIVE_DEPENDENCY_SHA256
            require(row['source_native_tile_id'] == '57530200'
                    and row['source_native_pose'] == (0 if matched[1] == 'A' else 3)
                    and row['source_model_sha256'] == NATIVE_DEPENDENCY_SHA256[0x5ad0e817, 0xbadb57f1, 0x57530200]
                    and row['analysis_below_height_m'] == nominal and row['underside_height_m'] == nominal-1.
                    and row['source_extrusion_length_m'] == 3.
                    and row['finite_source_footprint_and_height_containment_proved'] is True
                    and row['requires_independent_complete_shell_and_outer_wall_proof'] is True
                    and row['requires_independent_actual_slab_containment_proof'] is True
                    and row['raised_native_strip_and_actual_saved_faces_changed'] is False
                    and row['generic_authored_phase_wall_covered'] is False,
                    'Reversed helper-body scope escapes its exact source pose, finite body prism, or mandatory physical proof')
            vertices = [(*p, *uv) for p, uv in zip(face['points'], face['uv'])]
            inside = _clip(vertices, (0., 0., 1., -nominal))
            hidden = _clip(vertices, (0., 0., -1., nominal))
            removed = max(0., _area(vertices)-_area(inside))
            require(abs(removed-row['source_body_surface_area_below_floor_m2']) <= 1e-8,
                    'Reversed helper-body skin trim differs from the independently certified finite source region')
            helper_counts[face['role']] = helper_counts.get(face['role'], 0)+1
            helper_area += removed
            helper_points.extend(p[:3] for p in hidden)
            current = list(_triangulated(face, inside))
        elif C_ROLE.fullmatch(face['role']):
            require(index in certified and face['owner_cell'] == (3, 0)
                    and C_MODEL_SHA256 in certificate['source_model_sha256'],
                    'Reversed C south fringe requires a certified literal source face in its exact owner')
            vertices = [(*p, *uv) for p, uv in zip(face['points'], face['uv'])]
            require(all(p[0] <= 56.+POSITION_EPS and p[1] >= C_SOUTH_NORTH-POSITION_EPS
                        and p[1] <= 8.+POSITION_EPS for p in vertices),
                    'Reversed C source fringe exceeds its fresh measured south bounds')
            inside = _clip(vertices, (0., 1., 0., 8.))
            outside = _clip(vertices, (0., -1., 0., -8.))
            difference = max(0., _area(vertices)-_area(inside))
            if difference > 1e-14:
                fringe_count += 1
                fringe_area += difference
                fringe_points.extend(p[:3] for p in outside)
                if face['kind'] == 'pavement' and face['upward'] and len(outside) >= 3:
                    fringe_roof_area += Polygon([p[:2] for p in outside]).area
            current = list(_triangulated(face, inside))
        mask = masks.get(face['role'])
        if mask is not None and face['kind'] == 'pavement' and face['upward']:
            require(index in certified, 'Uncertified reversed native roof cannot receive an intrinsic barrier mask')
            for part in current:
                kept, area = _clip_roof_mask(part, mask)
                result.extend(kept)
                removed_roof += area
        else:
            result.extend(current)
    if any(face['owner_cell'] == (3, 0) for face in faces):
        references, interface = native_interface_skin(donors)
    else:
        references, interface = [], {'source_body_reference_faces_used': 0, 'reference_source_fragments': 0}
    result.extend(references)
    require(all(count == 6 for count in helper_counts.values()),
            'Reversed saved helper-body partition differs from its six reviewed source faces per arm/deck')
    summary = {key: value for key, value in certificate.items() if key not in (
        'internal_pavement_masks', 'barrier_base_masks', 'certified_face_indices',
        'generic_native_texture_face_indices_without_geometry_exception')}
    summary.update({'certified_faces': len(certified), 'removed_inherited_interior_roof_area_m2': removed_roof,
        'actual_saved_faces_changed': False, 'original_borrowed_underside_prefixes': 0,
        'original_peer_body_faces_exempted': 0,
        'finite_source302_helper_body_skin_scope': {
            'source_faces_trimmed': len(helper_regions), 'counts_by_exact_role': helper_counts,
            'removed_original_surface_area_m2': helper_area, 'removed_original_bounds_enh_m': _bounds(helper_points),
            'required_upper_authored_floor_m': 14., 'required_lower_authored_floor_m': 6.5,
            'raised_original_body_above_nominal_roof_preserved': True,
            'actual_saved_faces_changed': False, 'new_authored_faces_exempted': 0,
            'requires_independent_complete_shell_outer_wall_and_full_slab_proof': True},
        'finite_literal_c_south_fringe_skin_scope': {
            'source_model_sha256': C_MODEL_SHA256, 'source_pose': 1,
            'analysis_inside_north_min_m': -8., 'source_faces_with_removed_portions': fringe_count,
            'removed_original_surface_area_m2': fringe_area,
            'removed_original_upward_roof_plan_area_m2': fringe_roof_area,
            'removed_original_bounds_enh_m': _bounds(fringe_points), 'new_authored_faces_exempted': 0,
            'actual_dat_underside_corridor_and_interference_faces_changed': False},
        'required_native_c_owned_roof_interface': interface})
    return result, summary


def check_support_source():
    """Check every numeric prism and probe against the retained original source."""
    raw = (contract.ORIGINAL/'checks/support-solids.jsonc').read_bytes()
    require(hashlib.sha256(raw).hexdigest() == 'c2f5da458026f7380bf88b048e6bca5aa6019764484ce53735df104dc7e88e1d',
            'Reversed support baseline differs from its reviewed original physical prisms')
    original = jsonc.loads(raw.decode())['supports']
    actual = physical._support_records(path_contract=contract)
    require(len(original) == len(actual) == 66, 'Reversed support source changes the sixty-six physical solids')
    expected = {}
    points_by_name = contract.independent_source()['routes']
    for row in original:
        copied = deepcopy(row)
        if 'attachment' in copied:
            old = copied['attachment']
            name = old['source_route'][2]+'-'+old['source_route'][0]
            points = points_by_name[name]
            length = sum(math.dist(a[:2], b[:2]) for a, b in zip(points, points[1:]))
            old['source_route'], old['station_m'] = name, length-old['station_m']
        expected[copied['id']] = copied
    normalized = deepcopy(actual)
    for row in normalized:
        if 'attachment' in row and row['id'] in expected:
            wanted = expected[row['id']]['attachment']['station_m']
            require(abs(row['attachment']['station_m']-wanted) <= 1e-9,
                    'Reversed support attachment station differs from the reversed finite route')
            row['attachment']['station_m'] = wanted
    require({row['id']: row for row in normalized} == expected,
            'Reversed support source changes a physical prism, probe, or exact remapped attachment')
    return {'passed': True, 'unchanged_physical_prisms': 66,
            'remapped_directed_attachments': sum('attachment' in row for row in actual),
            'physical_support_identifiers_retain_original_station_labels': True}


def check_actual_helper_slab_containment(faces, regions):
    """Cover every removed helper wall projection with real new slab faces.

    This supplements source-prism membership. A floor hole outside every
    vehicle strip cannot inherit the source-only body analysis scope.
    """
    def horizontal_coverage(projection, height, candidates):
        polygons = []
        for face in candidates:
            error = max(abs(p[2]-height) for p in face['points'])
            if error > POSITION_EPS:
                continue
            # Horizontal nominal surfaces are exact in these native collars.
            # Reserve the actual vertical error from the same4µm Euclidean
            # distance bound before admitting finite XY edge capsules.
            radius = math.sqrt(max(0., POSITION_EPS**2-error**2))
            polygons.append(Polygon([p[:2] for p in face['points']]).buffer(radius, quad_segs=8))
        missing = projection.difference(unary_union(polygons))
        return missing.area <= 1e-18 if projection.geom_type == 'Polygon' else missing.length <= 1e-12 and (
            missing.is_empty or projection.geom_type != 'Point')

    roofs = [face for face in faces if face['kind'] == 'pavement' and face['upward']
             and not face.get('native_reference')]
    floors = [face for face in faces if face['kind'] == 'body' and face['downward'] and face['role'] == 'body'
              and not face.get('native_reference')]
    roof_index, floor_index = physical.FaceIndex(roofs), physical.FaceIndex(floors)
    checked, footprints = [], []
    for row in regions:
        face = faces[row['face_index']]
        match = re.fullmatch(r'body-native-([AB])-(upper|lower)-helper', face['role'])
        require(match is not None and row['role'] == face['role'], 'Actual helper burial refers to an unrelated saved face')
        nominal = 15. if match[2] == 'upper' else 7.5
        require(row['analysis_below_height_m'] == nominal and row['underside_height_m'] == nominal-1.,
                'Actual helper burial changed its exact required slab heights')
        removed = _clip([tuple(p) for p in face['points']], (0., 0., -1., nominal))
        require(_area(removed) > 1e-14 and min(p[2] for p in removed) >= nominal-1.-POSITION_EPS,
                'Actual helper burial exceeds the finite source wall or required floor')
        projection = MultiPoint([p[:2] for p in removed]).convex_hull
        xmin, ymin, xmax, ymax = projection.bounds
        a, b = (xmin, ymin, nominal), (xmax, ymax, nominal)
        require(horizontal_coverage(projection, nominal, roof_index.near(a, b, POSITION_EPS)),
                'Source helper wall lacks complete actual saved nominal-roof coverage over its entire removed footprint')
        require(horizontal_coverage(projection, nominal-1., floor_index.near(a, b, POSITION_EPS)),
                'Source helper wall lacks complete actual authored-floor coverage over its entire removed footprint')
        checked.append({'source_face_index': row['face_index'], 'source_role': face['role'],
                        'projection_geometry': projection.geom_type, 'projection_bounds_en_m': list(projection.bounds),
                        'actual_roof_height_m': nominal, 'actual_authored_floor_height_m': nominal-1.})
        footprints.extend(removed)
    return {'passed': True, 'removed_source_wall_faces_checked': len(checked),
            'entire_removed_wall_footprints_including_outside_vehicle_strips': True,
            'actual_authored_floor_faces_only': True, 'external_native_floor_faces_used': 0,
            'source_wall_bounds_enh_m': _bounds(footprints), 'finite_euclidean_position_bound_m': POSITION_EPS,
            'requires_separate_complete_saved_shell_and_outer_wall_proof': True, 'source_face_proofs': checked}


def _gather(resources, piece, donors):
    return physical.gather(resources, piece, path_contract=contract, variant='reversed',
                           native_cell_bounds=native_cell_bounds(donors))


def check_models(resources, piece, donors=None):
    contract.check_paths(resources, piece)
    check_support_source()
    faces = _gather(resources, piece, donors)
    return _check([piece], {piece['id']: resources}, faces, donors, whole=False)


def check_models_assembly(pieces, resources_by_id, donors):
    check_support_source()
    faces = []
    for piece in pieces:
        contract.check_paths(resources_by_id[piece['id']], piece)
        faces.extend(_gather(resources_by_id[piece['id']], piece, donors))
    return _check(pieces, resources_by_id, faces, donors, whole=True)


def _check(pieces, resources_by_id, faces, donors, *, whole):
    _context(donors)
    routes = [row for piece in pieces for row in physical._saved_routes(
        resources_by_id[piece['id']], piece, path_contract=contract)]
    references = physical.native_faces(donors, native_source=native)
    native_routes = physical.native_traffic(donors, native_source=native)
    all_faces = [*faces, *references]
    pavement = physical.FaceIndex(all_faces)
    floors = source_floor_segments(donors)
    corridors = physical.check_corridors(all_faces, routes, full_width=whole,
                                         floor_segments=floors, allow_original_prefix=False,
                                         underside_faces=[face for face in faces if face['role'] == 'body'],
                                         obstacle_checker=floors.intrudes)
    corridors['original_native_underside_scope'] = None
    skin, certificate = external_skin(faces, donors)
    actual_helper_burial = check_actual_helper_slab_containment(faces, certificate.get('buried_helper_body_regions', []))
    expected_helper_walls = 24 if whole else (0 if contract._key(pieces[0]) == contract.KEYS[2] else 12)
    require(actual_helper_burial['removed_source_wall_faces_checked'] == expected_helper_walls,
            'Reversed actual helper slab proof omits one of this component or assembly source-wall footprints')
    arms = ('A', 'B', 'C') if whole else (dict(zip(contract.KEYS, ('A', 'B', 'C')))[contract._key(pieces[0])],)
    owned = None if whole else [
        (c[0]+pieces[0]['engineering']['world_origin_cell'][0], c[1]+pieces[0]['engineering']['world_origin_cell'][1])
        for c in pieces[0]['cells']]
    result = {'passed': True, 'variant': 'reversed', 'actual_indexed_triangles_checked': len(faces),
        'saved_triangle_metric': 'Actual indexed finite S3D triangles after city-cell clipping; the author world count is a distinct pre-partition metric.',
        'numeric_bounds': {'saved_position_and_finite_contact_m': POSITION_EPS,
            'native_finite_join_position_m': 2e-6, 'native_source_uv': 5e-6,
            'saved_path_position_m': contract.POSITION_EPS},
        'texture_ids': sorted({texture for face in faces for texture in face['material']['textures']}),
        'actual_saved_vehicle_corridors': corridors,
        'unchanged_native_vehicle_corridors': physical.check_native_vehicle_clearance(faces, native_routes, floor_segments=floors, obstacle_checker=floors.intrudes),
        'complete_road_shell' if whole else 'road_shell': physical.check_shell(
            skin, kind='road', component=not whole, pavement_index=pavement,
            native_profiles=physical.native_open_profiles(donors, native_source=native)),
        'complete_support_shell' if whole else 'support_shell': physical.check_shell(
            faces, kind='support', component=not whole, pavement_index=pavement),
        'complete_saved_support_prisms': physical.check_support_solids(
            all_faces, [*routes, *native_routes], owned_cells=owned, whole=whole,
            path_contract=contract, use_attachment=True),
        'native_finite_physical_seams': physical._native_seams(faces, donors, arms, native_source=native,
            owned_cells=[cell for group in contract.REVIEWED_OWNED_WORLD_CELLS for cell in group]),
        'independent_native_collar_certificate': certificate,
        'actual_saved_helper_slab_containment': actual_helper_burial,
        'game_rendering_tested': False, 'structural_capacity_tested': False}
    if whole:
        result.update({'full_vehicle_width_authored_body_depth': check_full_underfloor(faces, all_faces, routes, donors=donors),
            'deck_body_clearance': physical.check_deck_overlaps(faces),
            'underside_surface_clearance': physical.check_underside_overlaps(skin),
            'barrier_to_deck_solid_clearance': physical.check_barrier_deck_clearance(all_faces),
            'barrier_to_barrier_surface_clearance': physical.check_barrier_intersections(all_faces)})
    else:
        from .y_junction_reversed_approaches import check_native_boundary_paths
        from .shadow_verify import check_resources
        result.update({'native_draggable_boundary_contract': check_native_boundary_paths(donors, pieces[0], resources_by_id[pieces[0]['id']]),
            'all_five_zooms_identical': True, 'preview_matches_all_saved_cells': True,
            'whole_assembly_width_and_seams_require_separate_check': True,
            **check_resources(resources_by_id[pieces[0]['id']], pieces[0])})
    result['complete_physical_acceptance'] = bool(whole)
    return result
