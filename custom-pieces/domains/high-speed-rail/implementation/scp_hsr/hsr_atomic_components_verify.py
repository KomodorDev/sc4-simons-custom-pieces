"""Independently verify shortened native-profile HSR modules from saved resources.

These literal contracts do not import the geometry writer. The audits inspect
encoded routes, native joining sections, complete model ownership, supports,
clearance and render budgets; they do not establish operation in the game.
"""
from __future__ import annotations

from functools import lru_cache
import hashlib
import json
import math

from scp.dbpf import require
from scp.models import parse_s3d
from scp.render_meshes import assert_render_budget
from .directional_t_verify import _journeys, _world_triangles, _TURN_LIMITS, _resample, audit_visible_rails
from .hsr_mesh_verify import audit_bed_overlaps, audit_crossings, audit_supports, measure_journey_quality, _coalesce_grid_cuts
from .hsr_compact_fan_verify import audit_bed_corridors, audit_visible_rails_at_custom_cuts, _clip_attribute_polygon
from .interchange_verify import S3D, PATH, EXEMPLAR, _number, _encoded_routes, _graph, _native_port_headings, _models

COMMON = {
    'kind': 'partition_component', 'min_height': 15.5, 'max_height': 15.5,
    'max_grade': 0., 'clearance_width_m': 5., 'minimum_clearance': 5.,
    'foundation_width_m': 1.3, 'minimum_support_spacing_m': 16.,
    'allow_same_edge': False, 'required_grade_separated_crossings': 0,
    'custom_curved_interfaces': True,
}

CONTRACTS = {
    'hsr_component_l2_short_mainline_diverge_core': {
        **COMMON, 'footprint': (4, 1), 'cost': 400,
        'cells': [(0, 0), (1, 0), (2, 0), (3, 0)], 'structural_cells': [],
        'ports': {'Win': (-8., -2., 15.5), 'Wout': (-8., 2., 15.5),
                  'Eout': (56., -2., 15.5), 'Ein': (56., 2., 15.5),
                  'Sout': (38.398519, -8., 15.5)},
        'port_vectors': {'Win': (1., 0.), 'Wout': (-1., 0.),
                         'Eout': (1., 0.), 'Ein': (-1., 0.),
                         'Sout': (.927254808965, -.374430927211)},
        'movements': [('Win', 'Eout'), ('Ein', 'Wout'), ('Win', 'Sout')],
        'support_centres_xz': [(0., 0.), (16., 0.), (32., 0.), (48., 0.)],
        'custom_curve_ports': ('Sout',),
        'native_sections': [('east', -8., 1., 0., 15.)],
    },
    'hsr_component_l2_short_opposed_merge_core': {
        **COMMON, 'footprint': (5, 1), 'cost': 500,
        'cells': [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], 'structural_cells': [],
        'ports': {'Win': (-8., -2., 15.5), 'Wout': (-8., 2., 15.5),
                  'Eout': (72., -2., 15.5), 'Ein': (72., 2., 15.5),
                  'Nin': (48.562689, 8., 15.5), 'Sin': (25.601481, -8., 15.5)},
        'port_vectors': {'Win': (1., 0.), 'Wout': (-1., 0.),
                         'Eout': (1., 0.), 'Ein': (-1., 0.),
                         'Nin': (-.912177123445, -.409796163310),
                         'Sin': (.927254808965, .374430927211)},
        'movements': [('Win', 'Eout'), ('Ein', 'Wout'), ('Nin', 'Wout'), ('Sin', 'Eout')],
        'support_centres_xz': [(0., 0.), (16., 0.), (32., 0.), (48., 0.), (64., 0.)],
        'custom_curve_ports': ('Nin', 'Sin'),
        'native_sections': [('east', 72., -1., 0., 15.)],
    },
    'hsr_component_l2_shortened_departure_curve': {
        **COMMON, 'footprint': (5, 6), 'cost': 1200,
        'cells': [(0, 0), (1, 0), (2, 0), (3, 0), (2, 1), (3, 1), (4, 1),
                  (3, 2), (4, 2), (4, 3), (4, 4), (4, 5)],
        'structural_cells': [(0, 0), (2, 1), (4, 1)],
        'ports': {'Win': (22.398519, 8., 15.5), 'Sout': (64., -88., 15.5)},
        'port_vectors': {'Win': (.927254808965, -.374430927211), 'Sout': (0., -1.)},
        'movements': [('Win', 'Sout')],
        'support_centres_xz': [(32., 0.), (48., 16.), (64., 48.), (64., 64.),
                               (64., 80.), (57.377596412, 29.524559409)],
        'custom_curve_ports': ('Win',),
        'native_sections': [('north', -88., 1., 64., 8.)],
        'inherited_custom_cap': {'label': 'Win', 'depth_m': 2.65, 'width_m': 5.2,
            'cell': (1, 0), 'model_sha256': '3b82826d7416b68cb3d60372f6717da1b6b0851c2d0e5e1d8ccd58d8edf4f536'},
    },
    'hsr_component_l2_shortened_return_curve': {
        **COMMON, 'footprint': (5, 6), 'cost': 1200,
        'cells': [(1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1),
                  (0, 2), (1, 2), (0, 3), (0, 4), (0, 5)],
        'structural_cells': [(4, 0), (0, 1), (2, 1)],
        'ports': {'Sin': (0., -88., 15.5), 'Eout': (41.601481, 8., 15.5)},
        'port_vectors': {'Sin': (0., 1.), 'Eout': (.927254808965, .374430927211)},
        'movements': [('Sin', 'Eout')],
        'support_centres_xz': [(32., 0.), (16., 16.), (0., 48.), (0., 64.),
                               (0., 80.), (6.622403588, 29.524559409)],
        'custom_curve_ports': ('Eout',),
        'native_sections': [('north', -88., 1., 0., 8.)],
        'inherited_custom_cap': {'label': 'Eout', 'depth_m': 2.65, 'width_m': 5.2,
            'cell': (3, 0), 'model_sha256': '3275fe82e2361444a6dbc373f1384a40c67cbced6599a1e388b55613ef21d430'},
    },
}


def _contract(spec):
    require(spec['recipe'] in CONTRACTS, 'Unknown Trumpet shortened module contract')
    contract = CONTRACTS[spec['recipe']]
    require([tuple(cell) for cell in spec['cells']] == contract['cells']
            and tuple(spec['footprint']) == contract['footprint'],
            'Trumpet shortened module footprint differs from its independent literal contract')
    require([tuple(cell) for cell in spec.get('structural_cells', [])] == contract['structural_cells'],
            'Trumpet shortened module structural ownership differs')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(contract['cells']), 'Trumpet shortened module allocation is incomplete')
    col, row = contract['cells'][0]
    base = tiles[0]-0x100*col-0x10*row
    require(tiles == [base+0x100*x+0x10*y for x, y in contract['cells']],
            'Trumpet shortened module AutoTileBase allocation differs')
    return contract


def _section_intervals(triangles, axis, station, height, centre):
    """Intersect all saved horizontal faces; clip to this port's own tile."""
    along, lateral = (0, 2) if axis == 'east' else (2, 0)
    # S3D south is the opposite of north. East sections use north laterally.
    station = station if axis == 'east' else -station
    sign = -1. if axis == 'east' else 1.
    found = []
    for tri in triangles:
        if not all(abs(p[1]-height) <= .0001 for p in tri):
            continue
        values = []
        for a, b in zip(tri, tri[1:]+tri[:1]):
            if abs(a[along]-station) <= 1e-8:
                values.append(sign*a[lateral]-centre)
            if min(a[along], b[along]) < station < max(a[along], b[along]):
                t = (station-a[along])/(b[along]-a[along])
                values.append(sign*(a[lateral]+t*(b[lateral]-a[lateral]))-centre)
        if len(values) >= 2:
            first, last = max(-8., min(values)), min(8., max(values))
            if last-first > 1e-7:
                found.append((first, last))
    merged = []
    for first, last in sorted(found):
        if merged and first <= merged[-1][1]+.00005:
            merged[-1] = merged[-1][0], max(last, merged[-1][1])
        else:
            merged.append((first, last))
    return merged


def audit_native_sections(triangles, contract):
    """Require native slab, underside and parapet at each newly created join.

    Other interfaces retain exact approved bytes in the whole-assembly guard.
    In particular, the existing opposed merge's west parapet end is inherited;
    this atomization does not silently replace it with different geometry.
    """
    triangles = list(triangles)
    checked = 0
    for axis, boundary, inside, centre, width in contract['native_sections']:
        station = boundary+inside*.00000075
        half, inner = (7.5, 5.9965477) if width == 15. else (4., 2.6)
        for height, expected in ((16.189326, [(-half, half)]),
                                 (14.01067, [(-half, half)]),
                                 (16.98933, [(-half, -inner), (inner, half)])):
            actual = _section_intervals(triangles, axis, station, height, centre)
            require(len(actual) == len(expected) and all(
                abs(a-c) <= .00005 and abs(b-d) <= .00005
                for (a, b), (c, d) in zip(actual, expected)),
                f'Trumpet native joining section differs: {axis}={station}, height={height}, '
                f'actual={actual}, expected={expected}')
            checked += 1
    return {'complete_native_join_sections_checked': checked,
            'native_join_widths_m': sorted({s[4] for s in contract['native_sections']}),
            'native_join_profile_tolerance_m': .00005}


def audit_inherited_cap_model(resources, spec, contract):
    """Allow the shallow existing cut only for its exact inherited model bytes."""
    cap = contract.get('inherited_custom_cap')
    if cap is None:
        return {}
    index = contract['cells'].index(cap['cell'])
    tile = _number(spec['tile_ids'][index])
    require(all(hashlib.sha256(resources[*S3D, tile+zoom]).hexdigest() == cap['model_sha256']
                for zoom in range(5)), 'Trumpet inherited custom-cut exception requires exact original port-tile model bytes')
    return {'inherited_custom_cap_exact_model_cell': list(cap['cell']),
            'inherited_custom_cap_exact_model_sha256': cap['model_sha256'],
            'inherited_custom_cap_model_zooms_checked': 5}


def clip_inherited_curve_cap(triangles, contract):
    """Clip one literal2.65×5.2m outward mask; interior geometry stays checked.

    Both current curves need a wider mask than the2.6m fan-specific mask at their
    shallow diagonal cut. Their unchanged saved meshes pass the strict audit
    when their actual opposed merge/diverge neighbour's PATHs are included.
    The full Trumpet assembly must repeat that unclipped actual-neighbour proof.
    """
    cap = contract['inherited_custom_cap']
    label, depth, half = cap['label'], cap['depth_m'], cap['width_m']/2.
    x, north, _ = contract['ports'][label]
    east, direction_north = contract['port_vectors'][label]
    norm, sign = math.hypot(east, direction_north), -1. if label.endswith('in') else 1.
    dx, dz, z = sign*east/norm, -sign*direction_north/norm, -north
    longitudinal = lambda p: (p[0]-x)*dx+(p[2]-z)*dz
    transverse = lambda p: -(p[0]-x)*dz+(p[2]-z)*dx
    planes = (longitudinal, lambda p: depth-longitudinal(p),
              lambda p: transverse(p)+half, lambda p: half-transverse(p))
    corners = [(x+t*dx-s*dz, z+t*dz+s*dx) for t in (0., depth) for s in (-half, half)]
    xmin, xmax = min(p[0] for p in corners), max(p[0] for p in corners)
    zmin, zmax = min(p[1] for p in corners), max(p[1] for p in corners)
    result, affected = [], 0
    for tri in triangles:
        if max(p[0] for p in tri) <= xmin or min(p[0] for p in tri) >= xmax or max(p[2] for p in tri) <= zmin or min(p[2] for p in tri) >= zmax:
            result.append(tri)
            continue
        remaining, retained = list(tri), []
        for plane in planes:
            if not remaining:
                break
            outside = _clip_attribute_polygon(remaining, plane, False)
            if len(outside) >= 3:
                retained.append(outside)
            remaining = _clip_attribute_polygon(remaining, plane, True)
        if len(remaining) >= 3:
            affected += 1
        for polygon in retained:
            result.extend((polygon[0], polygon[i], polygon[i+1]) for i in range(1, len(polygon)-1))
    return result, affected


def audit_trumpet_visible_rails(triangles, records, contract):
    if 'inherited_custom_cap' not in contract:
        return audit_visible_rails_at_custom_cuts(triangles, records, contract)
    clipped, affected = clip_inherited_curve_cap(triangles, contract)
    report = audit_visible_rails(clipped, records)
    report.pop('unused_visible_native_rails', None)
    cap = contract['inherited_custom_cap']
    return {**report, 'unused_visible_rails_outside_declared_custom_caps': False,
            'inherited_custom_cap_labels': [cap['label']], 'inherited_custom_cap_depth_m': cap['depth_m'],
            'inherited_custom_cap_width_m': cap['width_m'], 'model_polygons_cut_at_custom_caps': affected,
            'custom_cap_scope': 'Only the exact approved saved northern port-tile model may use this literal outward mask. Both current curves need the2.65m mask when checked alone and pass with actual neighbouring PATHs; whole assembly checks remain fully unclipped.',
            'custom_cap_extensions_require_strict_actual_assembled_path_audit': True}


def check_paths(resources, spec, donors=None):
    contract = _contract(spec)
    records = _encoded_routes(resources, spec, contract)
    ports, movements = _graph(records, contract)
    headings = _native_port_headings(records, contract)
    journeys = _journeys(records, contract)
    quality = {}
    for movement, points in journeys.items():
        custom = any(label in contract['custom_curve_ports'] for label in movement)
        limits = {**_TURN_LIMITS, 'max_endpoint_curvature_per_m': 1./24. if custom else .0005}
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
                    f'Trumpet native endpoint does not ease into its straight: {label}, {curvature}')
            native_curvatures[label] = curvature
        quality['>'.join(movement)]['native_endpoint_curvature_per_m'] = native_curvatures
        require(all(abs(p[2]-15.5) <= 2e-6 for p in points), 'Trumpet shortened route changes its native L2 height')
    for movement, offset in ((('Win', 'Eout'), -2.), (('Ein', 'Wout'), 2.)):
        if movement in journeys:
            require(all(abs(p[1]-offset) <= 2e-6 for p in journeys[movement]),
                    'Trumpet shortened mainline leaves its literal native straight')
    return {'tile_count': len(contract['cells']), 'encoded_routes_checked': len(records),
            'external_ports_checked': ports, 'permitted_movements_checked': movements,
            'unique_complete_journeys_checked': len(journeys), 'literal_port_tangents_checked': len(headings),
            'journey_quality': quality, 'maximum_encoded_grade': 0.,
            'custom_curve_cuts_exempt_only_from_zero_endpoint_curvature': True,
            'game_operation': 'unverified', **audit_crossings(journeys, contract)}


def check_models(resources, spec, donors=None):
    _contract(spec)
    keys = {(*S3D, _number(spec['preview_id']))}
    for tile in map(_number, spec['tile_ids']):
        keys.update((*S3D, tile+zoom) for zoom in range(5))
        keys.update({(*PATH, tile), (*EXEMPLAR, tile)})
    immutable = tuple((key, resources[key]) for key in sorted(keys))
    return json.loads(_cached_models(json.dumps(spec, sort_keys=True), immutable))


@lru_cache(maxsize=8)
def _cached_models(spec_json, immutable):
    spec, resources = json.loads(spec_json), dict(immutable)
    contract = _contract(spec)
    records = _encoded_routes(resources, spec, contract)
    triangles = _world_triangles(resources, spec, contract)
    cap_evidence = audit_inherited_cap_model(resources, spec, contract)
    report = _models(resources, spec, contract=contract)
    report.update(audit_bed_corridors(triangles, records, owned_cells=contract['cells']))
    report.update(audit_bed_overlaps(triangles))
    report.update(audit_trumpet_visible_rails(triangles, records, contract))
    report.update(cap_evidence)
    report.update(audit_supports(triangles, contract))
    report.update(audit_native_sections(triangles, contract))
    budgets = [assert_render_budget(parse_s3d(raw)) for key, raw in immutable if key[:2] == S3D]
    report.update(render_budget_models_checked=len(budgets), render_group_budget_checked=True)
    return json.dumps(report, sort_keys=True)


def verify_component(spec, resources, construction_fields=None):
    return {'paths': check_paths(resources, spec), 'models': check_models(resources, spec)}
