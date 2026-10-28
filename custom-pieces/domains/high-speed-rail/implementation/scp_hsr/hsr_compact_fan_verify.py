"""Independently audit the compact fan connection pieces from saved resources.

Literal cells, ports, directions, native cross sections and foundations are
defined here, separately from the geometry writer. These checks establish
software geometry only; they never record observations inside SimCity 4.
"""
from __future__ import annotations

from functools import lru_cache
import json
import math

from scp.dbpf import require
from scp.models import parse_s3d
from scp.render_meshes import assert_render_budget
from .directional_t_verify import _journeys, _world_triangles, audit_visible_rails, _TURN_LIMITS, _resample
from .hsr_mesh_verify import (
    audit_bed_overlaps, audit_crossings, audit_supports, measure_journey_quality,
    _bed_index, _height, _clip_height, _component_union_area, _coalesce_grid_cuts,
)
from .directional_t_verify import _area, _intersection_polygon
from .interchange_verify import (
    S3D, PATH, EXEMPLAR, _number, _encoded_routes, _graph,
    _native_port_headings, _models, _bed,
)

_COMMON = {
    'kind': 'partition_component', 'min_height': 15.5, 'max_height': 15.5,
    'max_grade': 0., 'clearance_width_m': 5., 'minimum_clearance': 5.,
    'foundation_width_m': 1.3, 'minimum_support_spacing_m': 16.,
    'allow_same_edge': False, 'required_grade_separated_crossings': 0,
    'custom_curved_interfaces': True,
}

CONTRACTS = {
    'hsr_component_l2_paired_fan_compact_join': {
        **_COMMON, 'footprint': (7, 5), 'cost': 1500,
        'cells': [(3, 0), (3, 1), (3, 2), (2, 3), (3, 3), (4, 3),
                  (1, 4), (2, 4), (3, 4), (4, 4), (5, 4)],
        'structural_cells': [(2, 3), (4, 3)],
        'ports': {'Nin': (46., 8., 15.5), 'Nout': (50., 8., 15.5),
                  'Wout': (22.398519, -72., 15.5), 'Ein': (73.601481, -72., 15.5)},
        'port_vectors': {'Nin': (0., -1.), 'Nout': (0., 1.),
                         'Wout': (-.927254808965, -.374430927211),
                         'Ein': (-.927254808965, .374430927211)},
        'movements': [('Nin', 'Wout'), ('Ein', 'Nout')],
        'support_centres_xz': [(48., 0.), (48., 16.), (48., 32.), (48., 48.),
                               (32., 64.), (64., 64.)],
        'custom_curve_ports': ('Wout', 'Ein'),
        'geometric_custom_rail_wedges': True,
    },
    'hsr_component_l2_paired_fan_compact_core': {
        **_COMMON, 'footprint': (5, 3), 'cost': 1300,
        'cells': [(2, 0), (1, 1), (2, 1), (3, 1),
                  (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
        'structural_cells': [(1, 1), (3, 1)],
        'ports': {'Nin': (30., 8., 15.5), 'Nout': (34., 8., 15.5),
                  'Wout': (6.398519, -40., 15.5), 'Ein': (57.601481, -40., 15.5)},
        'port_vectors': {'Nin': (0., -1.), 'Nout': (0., 1.),
                         'Wout': (-.927254808965, -.374430927211),
                         'Ein': (-.927254808965, .374430927211)},
        'movements': [('Nin', 'Wout'), ('Ein', 'Nout')],
        'support_centres_xz': [(32., 0.), (32., 16.), (16., 32.), (48., 32.)],
        'custom_curve_ports': ('Wout', 'Ein'),
        'geometric_custom_rail_wedges': True,
    },
    'hsr_component_l2_paired_straight_recessed_web': {
        **_COMMON, 'footprint': (1, 1), 'cost': 100,
        'cells': [(0, 0)], 'structural_cells': [],
        'ports': {'Nin': (-2., 8., 15.5), 'Nout': (2., 8., 15.5),
                  'Sin': (2., -8., 15.5), 'Sout': (-2., -8., 15.5)},
        'port_vectors': {'Nin': (0., -1.), 'Nout': (0., 1.),
                         'Sin': (0., 1.), 'Sout': (0., -1.)},
        'movements': [('Nin', 'Sout'), ('Sin', 'Nout')],
        'support_centres_xz': [(0., 0.)],
        'custom_curve_ports': (), 'custom_curved_interfaces': False,
    },
}


def _clip_attribute_polygon(polygon, value, positive):
    """Clip XYZUV vertices, preserving the saved triangle's affine fields."""
    result = []
    for a, b in zip(polygon, polygon[1:]+polygon[:1]):
        va, vb = value(a), value(b)
        ia, ib = va >= 0., vb >= 0.
        if not positive:
            ia, ib = not ia, not ib
        if ia:
            result.append(a)
        if ia != ib:
            fraction = va/(va-vb)
            result.append(tuple(a[n]+fraction*(b[n]-a[n]) for n in range(5)))
    return result


def _custom_port_rail_wedges(contract):
    """Derive each finite-PATH termination wedge from its actual city boundary.

    The rail audit already permits stripe centroids at most 1.10 m from a
    used PATH. At an oblique cut, that same strip intersects the owner's
    side of the tile edge beyond the perpendicular PATH-end plane. Its
    maximum length follows from those half-planes; it is not a depth limit.
    """
    require('inherited_custom_cap' not in contract,
            'Inherited custom-cut model exceptions cannot use generic geometric rail wedges')
    owned = set(contract['cells'])
    edges = (('west', -1., 0.), ('east', 1., 0.),
             ('north', 0., -1.), ('south', 0., 1.))
    result = []
    for label in contract['custom_curve_ports']:
        px, north, _ = contract['ports'][label]
        pz = -north
        boundaries = []
        for col, row in owned:
            for edge, nx, nz in edges:
                if (col+int(nx), row+int(nz)) in owned:
                    continue
                cx, cz = 16.*col+8.*nx, 16.*row+8.*nz
                if (abs((px-cx)*nx+(pz-cz)*nz) <= 2e-6
                        and abs(-(px-cx)*nz+(pz-cz)*nx) <= 8.+2e-6):
                    boundaries.append(((col, row), edge, nx, nz))
        require(len(boundaries) == 1, 'Custom rail cut needs one literal exposed source edge')
        cell, edge, nx, nz = boundaries[0]
        east, direction_north = contract['port_vectors'][label]
        norm = math.hypot(east, direction_north)
        sign = -1. if label.endswith('in') else 1.
        dx, dz = sign*east/norm, -sign*direction_north/norm
        outward = dx*nx+dz*nz
        lateral = -dz*nx+dx*nz
        require(outward > 0., 'Custom rail cut tangent must leave its declared boundary')
        half = 1.10  # Exactly the unchanged visible-stripe matching envelope.
        depth = half*abs(lateral)/outward
        transverse_end = -math.copysign(half, lateral) if lateral else 0.
        corners = [(px, pz), (px-transverse_end*dz, pz+transverse_end*dx),
                   (px+depth*dx-transverse_end*dz, pz+depth*dz+transverse_end*dx)]
        result.append({'label': label, 'source_cell': list(cell), 'edge': edge,
                       'origin': (px, pz), 'tangent': (dx, dz), 'normal': (nx, nz),
                       'half_width_m': half, 'maximum_depth_m': depth,
                       'bounds': (min(p[0] for p in corners), max(p[0] for p in corners),
                                  min(p[1] for p in corners), max(p[1] for p in corners))})
    return result


def _literal_custom_port_rail_caps(contract):
    """Preserve the original 2.6 m generic mask for unchanged components."""
    caps = []
    for label in contract['custom_curve_ports']:
        px, north, _ = contract['ports'][label]
        east, direction_north = contract['port_vectors'][label]
        norm = math.hypot(east, direction_north)
        sign = -1. if label.endswith('in') else 1.
        dx, dz, pz = sign*east/norm, -sign*direction_north/norm, -north
        longitudinal = lambda p, px=px, pz=pz, dx=dx, dz=dz: (p[0]-px)*dx+(p[2]-pz)*dz
        transverse = lambda p, px=px, pz=pz, dx=dx, dz=dz: -(p[0]-px)*dz+(p[2]-pz)*dx
        corners = [(px+t*dx-s*dz, pz+t*dz+s*dx) for t in (0., 2.6) for s in (-2.6, 2.6)]
        bounds = (min(p[0] for p in corners), max(p[0] for p in corners),
                  min(p[1] for p in corners), max(p[1] for p in corners))
        planes = (longitudinal, lambda p, f=longitudinal: 2.6-f(p),
                  lambda p, f=transverse: f(p)+2.6,
                  lambda p, f=transverse: 2.6-f(p))
        caps.append((bounds, planes))
    return caps


def clip_custom_port_rail_caps(triangles, contract):
    """Use an explicitly selected geometric wedge, or the original generic cap.

    Only the redesigned fan and opposed merge opt in to the exact owned
    boundary wedges. Unchanged components retain their original 2.6 m mask;
    inherited 2.65 m exceptions remain in their exact-model-bound wrapper.
    Whole-assembly rail verification stays fully unclipped.
    """
    geometric = contract.get('geometric_custom_rail_wedges', False)
    caps = [] if geometric else _literal_custom_port_rail_caps(contract)
    for wedge in _custom_port_rail_wedges(contract) if geometric else ():
        if wedge['maximum_depth_m'] == 0.:
            continue
        px, pz = wedge['origin']
        dx, dz = wedge['tangent']
        nx, nz = wedge['normal']
        half = wedge['half_width_m']
        longitudinal = lambda p, px=px, pz=pz, dx=dx, dz=dz: (p[0]-px)*dx+(p[2]-pz)*dz
        transverse = lambda p, px=px, pz=pz, dx=dx, dz=dz: -(p[0]-px)*dz+(p[2]-pz)*dx
        inward = lambda p, px=px, pz=pz, nx=nx, nz=nz: -(p[0]-px)*nx-(p[2]-pz)*nz
        xmin, xmax, zmin, zmax = wedge['bounds']
        for column, row in contract['cells']:
            left, right, top, bottom = 16.*column-8., 16.*column+8., 16.*row-8., 16.*row+8.
            bounds = max(xmin, left), min(xmax, right), max(zmin, top), min(zmax, bottom)
            if bounds[0] >= bounds[1] or bounds[2] >= bounds[3]:
                continue
            planes = (longitudinal, inward,
                      lambda p, f=transverse, half=half: f(p)+half,
                      lambda p, f=transverse, half=half: half-f(p),
                      lambda p, left=left: p[0]-left,
                      lambda p, right=right: right-p[0],
                      lambda p, top=top: p[2]-top,
                      lambda p, bottom=bottom: bottom-p[2])
            caps.append((bounds, planes))
    result, affected = [], 0
    for triangle in triangles:
        polygons = [list(triangle)]
        for (xmin, xmax, zmin, zmax), planes in caps:
            retained = []
            for polygon in polygons:
                if (max(p[0] for p in polygon) <= xmin or min(p[0] for p in polygon) >= xmax
                        or max(p[2] for p in polygon) <= zmin or min(p[2] for p in polygon) >= zmax):
                    retained.append(polygon)
                    continue
                remaining = polygon
                for plane in planes:
                    if not remaining:
                        break
                    outside = _clip_attribute_polygon(remaining, plane, False)
                    if len(outside) >= 3:
                        retained.append(outside)
                    remaining = _clip_attribute_polygon(remaining, plane, True)
                if len(remaining) >= 3:
                    affected += 1
            polygons = retained
        for polygon in polygons:
            result.extend((polygon[0], polygon[n], polygon[n+1]) for n in range(1, len(polygon)-1))
    return result, affected


def audit_visible_rails_at_custom_cuts(triangles, records, contract):
    clipped, affected = clip_custom_port_rail_caps(triangles, contract)
    report = audit_visible_rails(clipped, records)
    report.pop('unused_visible_native_rails', None)
    report = {**report, 'unused_visible_rails_outside_declared_custom_caps': False,
            'custom_port_cap_labels': list(contract['custom_curve_ports']),
            'model_polygons_cut_at_custom_caps': affected,
            'custom_cap_extensions_require_strict_actual_assembled_path_audit': True}
    if contract.get('geometric_custom_rail_wedges', False):
        report['custom_port_boundary_wedges'] = [
            {key: wedge[key] for key in ('label', 'source_cell', 'edge', 'half_width_m', 'maximum_depth_m')}
            for wedge in _custom_port_rail_wedges(contract)]
        report['custom_port_caps_clipped_to_literal_owned_cells'] = True
    else:
        report.update(custom_port_cap_depth_m=2.6, custom_port_cap_width_m=5.2)
    return report


def audit_bed_corridors(triangles, records, *, owned_cells=None):
    """Prove exact 5 m bed corridors, optionally clipped to literal ownership.

    A curved port meets its continuation at an oblique angle to a city-tile
    boundary. Part of the train's full corridor then belongs to the adjoining
    module. Standalone checks cover every portion in their literal tile mask;
    the assembly checker calls this again with no clipping and actual adjacent
    module meshes. Interior holes retain the established allowance: the larger
    of 1e-5 square metres and one millionth of the target corridor's area.
    """
    floors, buckets = _bed_index(triangles)
    owned = None if owned_cells is None else set(map(tuple, owned_cells))
    segments, patches, worst = 0, 0, 0.
    for _, _, points in records:
        for first, last in zip(points, points[1:]):
            a, b = (first[0], -first[1]), (last[0], -last[1])
            dx, dz = b[0]-a[0], b[1]-a[1]
            length2 = dx*dx+dz*dz
            length = math.sqrt(length2)
            normal = dz/length, -dx/length
            rectangle = [(p[0]+cross*normal[0], p[1]+cross*normal[1])
                         for p, cross in ((a, -2.5), (a, 2.5), (b, 2.5), (b, -2.5))]
            targets = [rectangle]
            if owned is not None:
                targets = []
                columns = range(math.floor((min(p[0] for p in rectangle)+8.)/16.),
                                math.floor((max(p[0] for p in rectangle)+8.)/16.)+1)
                rows = range(math.floor((min(p[1] for p in rectangle)+8.)/16.),
                             math.floor((max(p[1] for p in rectangle)+8.)/16.)+1)
                for column in columns:
                    for row in rows:
                        if (column, row) not in owned:
                            continue
                        square = [(16.*column-8., 16.*row-8.), (16.*column+8., 16.*row-8.),
                                  (16.*column+8., 16.*row+8.), (16.*column-8., 16.*row+8.)]
                        patch = _intersection_polygon(rectangle, square)
                        if len(patch) >= 3 and _area(patch) > 1e-10:
                            targets.append(patch)
            require(targets, 'A declared PATH corridor has no area in its literal owned cells')
            rise = _bed(last[2])-_bed(first[2])
            expected = rise*dx/length2, rise*dz/length2, _bed(first[2])-rise*(a[0]*dx+a[1]*dz)/length2
            for target in targets:
                candidates = set()
                for x in range(math.floor(min(p[0] for p in target)/4.), math.floor(max(p[0] for p in target)/4.)+1):
                    for z in range(math.floor(min(p[1] for p in target)/4.), math.floor(max(p[1] for p in target)/4.)+1):
                        candidates.update(buckets[x, z])
                pieces = []
                for index in candidates:
                    polygon, plane = floors[index]
                    differences = [_height(plane, corner)-_height(expected, corner) for corner in target]
                    if min(differences) > .10 or max(differences) < -.10:
                        continue
                    polygon = _intersection_polygon(polygon, target)
                    if len(polygon) < 3:
                        continue
                    polygon = _clip_height(polygon, plane, expected, -.10, True)
                    if len(polygon) < 3:
                        continue
                    polygon = _clip_height(polygon, plane, expected, .10, False)
                    if len(polygon) >= 3 and _area(polygon) > 1e-10:
                        pieces.append(polygon)
                area = _area(target)
                missing = max(0., area-_component_union_area(pieces))
                worst = max(worst, missing)
                require(missing <= max(1e-5, area*1e-6),
                        f'HSR owned/assembled train corridor has a hole at its actual height: '
                        f'{missing:.8f} square metres; {first} to {last}')
                patches += 1
            segments += 1
    require(segments, 'No actual train bed corridors were checked')
    return {'full_width_bed_union_segments_checked': segments, 'bed_union_width_m': 5.,
            'maximum_uncovered_bed_area_m2': worst, 'height_aware_bed_union_checked': True,
            'owner_clipped_corridor_fragments_checked': patches,
            'corridor_clipped_to_literal_ownership': owned is not None,
            'external_custom_collar_requires_unclipped_actual_assembly_check': owned is not None}


def _contract(spec):
    require(spec['recipe'] in CONTRACTS, 'Unknown compact fan piece contract')
    contract = CONTRACTS[spec['recipe']]
    require([tuple(cell) for cell in spec['cells']] == contract['cells']
            and tuple(spec['footprint']) == contract['footprint'],
            'Compact fan footprint differs from the literal contract')
    require([tuple(cell) for cell in spec.get('structural_cells', [])]
            == contract['structural_cells'], 'Compact fan structural cells differ')
    require(len(spec['tile_ids']) == len(contract['cells']), 'Compact fan tile IDs are incomplete')
    tiles = list(map(_number, spec['tile_ids']))
    base = tiles[0]-0x100*contract['cells'][0][0]-0x10*contract['cells'][0][1]
    require(tiles == [base+0x100*x+0x10*y for x, y in contract['cells']],
            'Compact fan AutoTileBase allocation differs')
    return contract


def check_paths(resources, spec, donors=None):
    contract = _contract(spec)
    if spec['recipe'] == 'hsr_component_l2_paired_fan_compact_core':
        from .hsr_fan_core_verify import audit_retained_core_paths
        audit_retained_core_paths(resources, spec)
    if spec['recipe'] == 'hsr_component_l2_paired_straight_recessed_web':
        from .hsr_recessed_straight_verify import audit_retained_straight_paths
        audit_retained_straight_paths(resources, spec)
    records = _encoded_routes(resources, spec, contract)
    ports, movements = _graph(records, contract)
    headings = _native_port_headings(records, contract)
    journeys = _journeys(records, contract)
    quality = {}
    for movement, points in journeys.items():
        # Custom curved cuts retain the existing non-zero curvature. They
        # are matching interfaces, not native straight approaches. All other
        # established radius, tangent and curvature-change limits still apply.
        limits = {**_TURN_LIMITS, 'max_endpoint_curvature_per_m': 1./24.}
        quality['>'.join(movement)] = measure_journey_quality(points, limits)
        sampled, _, _ = _resample(_coalesce_grid_cuts(points))
        native_curvatures = {}
        for label, end in ((movement[0], sampled[:3]), (movement[1], sampled[-3:])):
            if label in contract['custom_curve_ports']:
                continue
            a, b, c = end
            product = math.dist(a[:2], b[:2])*math.dist(b[:2], c[:2])*math.dist(a[:2], c[:2])
            curvature = abs(2.*((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])))/product
            require(curvature <= .0005+2e-6,
                    f'Compact fan native endpoint does not ease into its straight: {label}, {curvature}')
            native_curvatures[label] = curvature
        quality['>'.join(movement)]['native_endpoint_curvature_per_m'] = native_curvatures
    for _, _, points in records:
        require(all(abs(point[2]-15.5) <= 2e-6 for point in points),
                'Compact fan route must remain flat at the native L2 height')
    return {'tile_count': len(contract['cells']), 'encoded_routes_checked': len(records),
            'external_ports_checked': ports, 'permitted_movements_checked': movements,
            'literal_port_tangents_checked': len(headings),
            'unique_complete_journeys_checked': len(journeys),
            'journey_quality': quality,
            'custom_curve_cuts_exempt_only_from_zero_endpoint_curvature': True,
            'exact_3d_cell_seams': True, 'maximum_encoded_grade': 0.,
            'native_port_heights_m': [15.5], 'game_operation': 'unverified',
            **audit_crossings(journeys, contract)}


def check_models(resources, spec, donors=None):
    _contract(spec)
    preservation = {}
    if spec['recipe'] == 'hsr_component_l2_paired_fan_compact_core':
        from .hsr_fan_core_verify import audit_retained_core_resources
        preservation = audit_retained_core_resources(resources, spec)
    if spec['recipe'] == 'hsr_component_l2_paired_straight_recessed_web':
        from .hsr_recessed_straight_verify import audit_retained_straight_resources
        preservation = audit_retained_straight_resources(resources, spec)
    keys = {(*S3D, _number(spec['preview_id']))}
    for tile in map(_number, spec['tile_ids']):
        keys.update((*S3D, tile+zoom) for zoom in range(5))
        keys.update({(*PATH, tile), (*EXEMPLAR, tile)})
    immutable = tuple((key, resources[key]) for key in sorted(keys))
    return {**json.loads(_cached_models(json.dumps(spec, sort_keys=True), immutable)),
            **preservation}


@lru_cache(maxsize=4)
def _cached_models(spec_json, immutable):
    spec, resources = json.loads(spec_json), dict(immutable)
    contract = _contract(spec)
    records = _encoded_routes(resources, spec, contract)
    triangles = _world_triangles(resources, spec, contract)
    report = _models(resources, spec, contract=contract)
    report.update(audit_bed_corridors(triangles, records, owned_cells=contract['cells']))
    report.update(audit_bed_overlaps(triangles))
    report.update(audit_visible_rails_at_custom_cuts(triangles, records, contract))
    report.update(audit_supports(triangles, contract))
    from .hsr_fan_parapet_verify import audit_central_parapet
    original_frame = triangles
    if spec['recipe'] == 'hsr_component_l2_paired_fan_compact_core':
        original_frame = [tuple((v[0]+16., v[1], v[2]+32., *v[3:]) for v in triangle)
                          for triangle in triangles]
    if spec['recipe'] != 'hsr_component_l2_paired_straight_recessed_web':
        report.update(audit_central_parapet(original_frame))
    budgets = [assert_render_budget(parse_s3d(raw)) for key, raw in immutable if key[:2] == S3D]
    report.update(render_budget_models_checked=len(budgets), render_group_budget_checked=True)
    return json.dumps(report, sort_keys=True)


def verify_component(spec, resources, construction_fields=None):
    return {'paths': check_paths(resources, spec), 'models': check_models(resources, spec)}
