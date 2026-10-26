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
from .directional_t_verify import _journeys, _world_triangles, audit_visible_rails, _TURN_LIMITS
from .hsr_mesh_verify import (
    audit_bed_overlaps, audit_crossings, audit_supports, measure_journey_quality,
    _bed_index, _height, _clip_height, _component_union_area,
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
    'hsr_component_l2_compact_fan_diverge': {
        **_COMMON, 'footprint': (3, 1), 'cost': 300,
        'cells': [(0, 0), (1, 0), (2, 0)], 'structural_cells': [],
        'ports': {'Win': (-8., -2., 15.5), 'Wout': (-8., 2., 15.5),
                  'Eout': (40., -2., 15.5), 'Ein': (40., 2., 15.5),
                  'Nout': (-.562689, 8., 15.5)},
        'port_vectors': {'Win': (1., 0.), 'Wout': (-1., 0.),
                         'Eout': (1., 0.), 'Ein': (-1., 0.),
                         'Nout': (-.912177123445, .409796163310)},
        'movements': [('Win', 'Eout'), ('Ein', 'Wout'), ('Ein', 'Nout')],
        'support_centres_xz': [(0., 0.), (16., 0.), (32., 0.)],
        'custom_curve_ports': ('Nout',),
    },
    'hsr_component_l2_paired_fan_compact_join': {
        **_COMMON, 'footprint': (7, 5), 'cost': 1500,
        'cells': [(3, 0), (3, 1), (2, 2), (3, 2), (4, 2), (2, 3), (3, 3),
                  (4, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4)],
        'structural_cells': [(2, 2), (4, 2), (0, 4), (3, 4), (6, 4)],
        'ports': {'Nin': (46., 8., 15.5), 'Nout': (50., 8., 15.5),
                  'Wout': (16.562689, -72., 15.5), 'Ein': (79.437311, -72., 15.5)},
        'port_vectors': {'Nin': (0., -1.), 'Nout': (0., 1.),
                         'Wout': (-.912177123445, -.409796163310),
                         'Ein': (-.912177123445, .409796163310)},
        'movements': [('Nin', 'Wout'), ('Ein', 'Nout')],
        'support_centres_xz': [(48., 0.), (48., 16.), (48., 32.), (40., 46.),
                               (56., 46.), (32., 64.), (64., 64.)],
        'custom_curve_ports': ('Wout', 'Ein'),
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


def clip_custom_port_rail_caps(triangles, contract):
    """Exclude only finite, literally declared custom-cut rail extensions.

    A tile boundary cuts a curved track obliquely. Its textured rail ribbon
    extends beyond the perpendicular plane through the last owned PATH point.
    Remove that extension only inside a 2.6 m deep, 5.2 m wide oriented cap.
    This does not alter the saved model, PATH, native matching distances or
    the strict complete-assembly rail audit.
    """
    caps = []
    for label in contract['custom_curve_ports']:
        x, north, _ = contract['ports'][label]
        east, direction_north = contract['port_vectors'][label]
        norm = math.hypot(east, direction_north)
        sign = -1. if label.endswith('in') else 1.
        dx, dz = sign*east/norm, -sign*direction_north/norm
        px, pz = x, -north
        def longitudinal(point, px=px, pz=pz, dx=dx, dz=dz):
            return (point[0]-px)*dx+(point[2]-pz)*dz
        def transverse(point, px=px, pz=pz, dx=dx, dz=dz):
            return -(point[0]-px)*dz+(point[2]-pz)*dx
        corners = [(px+t*dx-s*dz, pz+t*dz+s*dx) for t in (0., 2.6) for s in (-2.6, 2.6)]
        bounds = (min(p[0] for p in corners), max(p[0] for p in corners),
                  min(p[1] for p in corners), max(p[1] for p in corners))
        planes = (longitudinal, lambda point, f=longitudinal: 2.6-f(point),
                  lambda point, f=transverse: f(point)+2.6,
                  lambda point, f=transverse: 2.6-f(point))
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
    return {**report, 'unused_visible_rails_outside_declared_custom_caps': False,
            'custom_port_cap_labels': list(contract['custom_curve_ports']),
            'custom_port_cap_depth_m': 2.6, 'custom_port_cap_width_m': 5.2,
            'model_polygons_cut_at_custom_caps': affected,
            'custom_cap_extensions_require_strict_actual_assembled_path_audit': True}


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


def audit_native_mainline_sections(triangles):
    """Measure both compact core interfaces against the complete native profile.

    At the exact replacement seam the native slab is 15 m wide, with one
    unobstructed interior between its two outside parapets. The branch wing
    starts one micrometre inside its owner. Saved native cap ends round inward
    by 0.48 micrometres, so sample 0.75 micrometres inside the seam with a 0.01
    micrometre intersection tolerance. This includes native float32 rounding
    while excluding the intentional branch wing farther inside its owner.
    """
    sections = [(tuple((z, height, x, u, v) for x, height, z, u, v in tri))
                for tri in triangles]
    def intervals(station, height, floor):
        found = []
        for triangle in sections:
            if not all(abs(point[1]-height) < .0001 for point in triangle):
                continue
            if floor and not all(.2158 <= point[3] <= 1.0042 for point in triangle):
                continue
            xs = []
            for a, b in zip(triangle, triangle[1:]+triangle[:1]):
                if abs(a[2]-station) <= 1e-8:
                    xs.append(a[0])
                if min(a[2], b[2]) < station < max(a[2], b[2]):
                    t = (station-a[2])/(b[2]-a[2])
                    xs.append(a[0]+t*(b[0]-a[0]))
            if len(xs) >= 2 and max(xs)-min(xs) > 1e-7:
                found.append((min(xs), max(xs)))
        merged = []
        for first, last in sorted(found):
            if merged and first <= merged[-1][1]+.00005:
                merged[-1] = merged[-1][0], max(last, merged[-1][1])
            else:
                merged.append((first, last))
        return merged
    checked = 0
    for station in (-8.+.00000075, 40.-.00000075):
        for height, floor, expected in (
            (16.189326, True, [(-7.5, 7.5)]),
            (14.01067, False, [(-7.5, 7.5)]),
            (16.98933, False, [(-7.5, -5.9965477), (5.9965477, 7.5)]),
        ):
            actual = intervals(station, height, floor)
            require(len(actual) == len(expected) and all(
                abs(a-c) <= .0001 and abs(b-d) <= .0001
                for (a, b), (c, d) in zip(actual, expected)),
                f'Compact fan native mainline section differs: x={station}, height={height}, '
                f'actual={actual}, expected={expected}')
            checked += 1
    return {'native_mainline_sections_checked': checked,
            'native_slab_width_m': 15., 'native_parapet_inner_offsets_m': [-5.9965477, 5.9965477]}


def check_paths(resources, spec, donors=None):
    contract = _contract(spec)
    records = _encoded_routes(resources, spec, contract)
    ports, movements = _graph(records, contract)
    headings = _native_port_headings(records, contract)
    journeys = _journeys(records, contract)
    quality = {}
    for movement, points in journeys.items():
        # Custom curved cuts retain the existing non-zero curvature. They
        # are matching interfaces, not native straight approaches. All other
        # established radius, tangent and curvature-change limits still apply.
        custom = (spec['recipe'] == 'hsr_component_l2_paired_fan_compact_join'
                  or movement == ('Ein', 'Nout'))
        limits = {**_TURN_LIMITS,
                  'max_endpoint_curvature_per_m': 1./24. if custom else .0005}
        quality['>'.join(movement)] = measure_journey_quality(points, limits)
    for _, _, points in records:
        require(all(abs(point[2]-15.5) <= 2e-6 for point in points),
                'Compact fan route must remain flat at the native L2 height')
    if spec['recipe'] == 'hsr_component_l2_compact_fan_diverge':
        for movement, offset in ((('Win', 'Eout'), -2.), (('Ein', 'Wout'), 2.)):
            require(all(abs(point[1]-offset) <= 2e-6 for point in journeys[movement]),
                    'Compact fan mainline departs from its literal native straight')
        branch = journeys['Ein', 'Nout']
        require(branch[0] == (40., 2., 15.5) and branch[-1] == (-.562689, 8., 15.5),
                'Compact fan branch endpoints differ')
        require(all(b[0] <= a[0]+2e-6 and b[1] >= a[1]-2e-6
                    for a, b in zip(branch, branch[1:])),
                'Compact fan branch reverses or loops inside the compact core')
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
    keys = {(*S3D, _number(spec['preview_id']))}
    for tile in map(_number, spec['tile_ids']):
        keys.update((*S3D, tile+zoom) for zoom in range(5))
        keys.update({(*PATH, tile), (*EXEMPLAR, tile)})
    immutable = tuple((key, resources[key]) for key in sorted(keys))
    return json.loads(_cached_models(json.dumps(spec, sort_keys=True), immutable))


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
    if spec['recipe'] == 'hsr_component_l2_compact_fan_diverge':
        report.update(audit_native_mainline_sections(triangles))
    budgets = [assert_render_budget(parse_s3d(raw)) for key, raw in immutable if key[:2] == S3D]
    report.update(render_budget_models_checked=len(budgets), render_group_budget_checked=True)
    return json.dumps(report, sort_keys=True)


def verify_component(spec, resources, construction_fields=None):
    return {'paths': check_paths(resources, spec), 'models': check_models(resources, spec)}
