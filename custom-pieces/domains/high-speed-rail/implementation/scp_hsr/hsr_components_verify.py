"""Independent encoded-resource contracts for the reusable upper HSR kit.

The dimensions, native ports and support plans below are reviewed literals.
No component layout or model writer is imported to construct expectations.
Software geometry checks deliberately do not establish game operation.
"""
from __future__ import annotations

from functools import lru_cache
import json
import math

from scp.dbpf import require
from scp.models import parse_s3d
from .interchange_verify import (
    S3D, PATH, EXEMPLAR, _number, _encoded_routes, _graph,
    _native_port_headings, _models, check_construction_fields as _construction,
)
from .directional_t_verify import _journeys, _world_triangles, _TURN_LIMITS, audit_visible_rails
from .hsr_mesh_verify import (
    audit_bed_union, audit_crossings, audit_supports, measure_journey_quality,
)
from scp.render_meshes import assert_render_budget

EPS = 2e-6
_STRAIGHT = {**_TURN_LIMITS, 'max_length_ratio': 1.00001,
             'max_total_turn_degrees': .01, 'max_raw_turn_degrees': .01,
             'max_sample_turn_degrees': .01, 'signed_turn_degrees': 0.,
             'max_grade_change_per_m': .011}
_COMMON = {'clearance_width_m': 5., 'minimum_clearance': 5.,
           'foundation_width_m': 1.3, 'minimum_support_spacing_m': 16.,
           'allow_same_edge': False, 'required_grade_separated_crossings': 0}

CONTRACTS = {
    'hsr_component_upper_paired_straight': {
        **_COMMON, 'kind': 'paired_straight', 'cells': [(0, 0)],
        'footprint': (1, 1), 'cost': 100,
        'ports': {'Sin': (2., -8., 30.5), 'Nout': (2., 8., 30.5),
                  'Nin': (-2., 8., 30.5), 'Sout': (-2., -8., 30.5)},
        'port_vectors': {'Sin': (0., 1.), 'Nout': (0., 1.),
                         'Nin': (0., -1.), 'Sout': (0., -1.)},
        'movements': [('Sin', 'Nout'), ('Nin', 'Sout')],
        'min_height': 30.5, 'max_height': 30.5, 'max_grade': 0.,
        'support_centres_xz': [(0., 0.)],
    },
    'hsr_component_paired_ramp_l2_to_l4': {
        **_COMMON, 'kind': 'paired_ramp', 'cells': [(0, row) for row in range(8)],
        'footprint': (1, 8), 'cost': 800,
        'ports': {'Sin': (2., -120., 15.5), 'Nout': (2., 8., 30.5),
                  'Nin': (-2., 8., 30.5), 'Sout': (-2., -120., 15.5)},
        'port_vectors': {'Sin': (0., 1.), 'Nout': (0., 1.),
                         'Nin': (0., -1.), 'Sout': (0., -1.)},
        'movements': [('Sin', 'Nout'), ('Nin', 'Sout')],
        'min_height': 15.5, 'max_height': 30.5, 'max_grade': .156251,
        'flat_collar_m': 8., 'support_centres_xz': [(0., 16.*row) for row in range(8)],
    },
}


CONTRACTS['hsr_component_upper_paired_to_single_adapter'] = {
    **_COMMON, 'kind': 'paired_to_single_adapter', 'footprint': (2, 8), 'cost': 1500,
    'cells': [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3), (1, 3),
              (0, 4), (1, 4), (0, 5), (1, 5), (0, 6), (1, 6), (0, 7)],
    'structural_cells': [(1, 5), (1, 6)],
    'ports': {'Sin': (2., -120., 30.5), 'Sout': (-2., -120., 30.5),
              'Nout': (16., 8., 30.5), 'Nin': (0., 8., 30.5)},
    'port_vectors': {'Sin': (0., 1.), 'Sout': (0., -1.),
                     'Nout': (0., 1.), 'Nin': (0., -1.)},
    'movements': [('Sin', 'Nout'), ('Nin', 'Sout')],
    'min_height': 30.5, 'max_height': 30.5, 'max_grade': 0., 'flat_collar_m': 8.,
    'support_centres_xz': [(0., 0.), (16., 0.), (0., 16.), (16., 16.), (0., 32.),
                            (16., 32.), (0., 48.), (0., 64.), (0., 80.), (0., 96.), (0., 112.)],
    'quality_limits': {
        ('Sin', 'Nout'): {**_TURN_LIMITS, 'max_total_turn_degrees': 30.,
                          'min_length_m': 129., 'max_length_m': 130., 'signed_turn_degrees': 0.},
        ('Nin', 'Sout'): {**_TURN_LIMITS, 'max_total_turn_degrees': 8.,
                          'min_length_m': 128., 'max_length_m': 128.1, 'signed_turn_degrees': 0.},
    },
}


# Reviewed full swept-width masks: route-free slab cells remain structural.
_PAIRED_RIGHT = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                 (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2), (2, 2),
                 (0, 3), (1, 3), (0, 4), (1, 4), (0, 5), (0, 6)]
_PAIRED_STRUCTURAL = [(1, 0), (0, 1), (3, 1), (4, 1), (2, 2), (1, 3), (1, 4)]
_SINGLE_RIGHT = [(2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (1, 1), (2, 1), (3, 1),
                 (0, 2), (1, 2), (0, 3), (1, 3), (0, 4), (0, 5), (0, 6)]
_SINGLE_STRUCTURAL = [(3, 1), (1, 3)]
_CURVE_SUPPORTS = {
    ('paired', 'right'): [(48., 0.), (64., 0.), (80., 0.), (96., 0.), (16., 16.), (32., 16.),
                           (16., 32.), (0., 48.), (0., 64.), (0., 80.), (0., 96.)],
    ('paired', 'left'): [(0., 0.), (16., 0.), (32., 0.), (48., 0.), (64., 16.), (80., 16.),
                          (80., 32.), (96., 48.), (96., 64.), (96., 80.), (96., 96.)],
    ('single', 'right'): [(64., 0.), (80., 0.), (96., 0.), (0., 64.), (0., 80.), (0., 96.),
                           (3.258463782, 48.235071478), (10.774672182, 29.783006147),
                           (23.916395723, 14.848064312), (41.392040409, 5.310173253)],
    ('single', 'left'): [(0., 0.), (16., 0.), (32., 0.), (96., 64.), (96., 80.), (96., 96.),
                          (92.741536218, 48.235071478), (85.225327818, 29.783006147),
                          (72.083604277, 14.848064312), (54.607959591, 5.310173253)],
}
# The inner and outer paired routes measure 176.005 m and 182.288 m;
# their difference is the expected 4 m track spacing times a 90 degree turn.
_CURVE_QUALITY = {**_TURN_LIMITS, 'min_radius_m': 50.,
                  'max_grade_change_per_m': .011, 'min_total_turn_degrees': 89.,
                  'max_total_turn_degrees': 91., 'min_length_m': 175., 'max_length_m': 184.}
for _hand in ('right', 'left'):
    _left = _hand == 'left'
    _target, _x, _end, _vector = ('W', 96., -8., (-1., 0.)) if _left else ('E', 0., 104., (1., 0.))
    _mirror = lambda cells: sorted(((6-x if _left else x, row) for x, row in cells), key=lambda p: (p[1], p[0]))
    _signed = 90. if _left else -90.
    _moves = [('Sin', _target+'out'), (_target+'in', 'Sout')]
    CONTRACTS['hsr_component_upper_paired_curve90_'+_hand] = {
        **_COMMON, 'kind': 'paired_curve', 'cells': _mirror(_PAIRED_RIGHT),
        'structural_cells': _mirror(_PAIRED_STRUCTURAL), 'footprint': (7, 7), 'cost': 2000,
        'ports': {'Sin': (_x+2., -104., 30.5), 'Sout': (_x-2., -104., 30.5),
                  _target+'in': (_end, -2. if _left else 2., 30.5),
                  _target+'out': (_end, 2. if _left else -2., 30.5)},
        'port_vectors': {'Sin': (0., 1.), 'Sout': (0., -1.),
                         _target+'out': _vector, _target+'in': tuple(-v for v in _vector)},
        'movements': _moves, 'min_height': 30.5, 'max_height': 30.5, 'max_grade': 0.,
        'flat_collar_m': 8., 'support_centres_xz': _CURVE_SUPPORTS['paired', _hand],
        'quality_limits': {_moves[0]: {**_CURVE_QUALITY, 'signed_turn_degrees': _signed},
                           _moves[1]: {**_CURVE_QUALITY, 'signed_turn_degrees': -_signed}},
    }
    for _levels, _first, _last in (('l2_to_l4', 15.5, 30.5), ('l4_to_l2', 30.5, 15.5)):
        CONTRACTS['hsr_component_oneway_curve90_'+_hand+'_'+_levels] = {
            **_COMMON, 'kind': 'single_curved_grade', 'cells': _mirror(_SINGLE_RIGHT),
            'structural_cells': _mirror(_SINGLE_STRUCTURAL), 'footprint': (7, 7), 'cost': 1500,
            'ports': {'Sin': (_x, -104., _first), _target+'out': (_end, 0., _last)},
            'port_vectors': {'Sin': (0., 1.), _target+'out': _vector},
            'movements': [('Sin', _target+'out')],
            'min_height': 15.5, 'max_height': 30.5, 'max_grade': .156251,
            'flat_collar_m': 8., 'support_centres_xz': _CURVE_SUPPORTS['single', _hand],
            'quality_limits': {('Sin', _target+'out'): {**_CURVE_QUALITY, 'min_length_m': 178., 'max_length_m': 181.,
                                                           'signed_turn_degrees': _signed}},
        }


from .hsr_assembly_components_verify import CONTRACTS as _ASSEMBLY_COMPONENT_CONTRACTS
CONTRACTS.update(_ASSEMBLY_COMPONENT_CONTRACTS)
from .hsr_compact_components_verify import CONTRACTS as _COMPACT_COMPONENT_CONTRACTS
CONTRACTS.update(_COMPACT_COMPONENT_CONTRACTS)
from .hsr_refined_components_verify import (
    CONTRACTS as _REFINED_COMPONENT_CONTRACTS, audit_refined_journeys, audit_y_native_profiles,
)
CONTRACTS.update(_REFINED_COMPONENT_CONTRACTS)
from .hsr_tight_loop_components_verify import (
    CONTRACTS as _TIGHT_LOOP_CONTRACTS, audit_tight_journeys, audit_tight_native_profiles,
)
CONTRACTS.update(_TIGHT_LOOP_CONTRACTS)
from .hsr_partition_components_verify import (
    CONTRACTS as _PARTITION_CONTRACTS,
    check_partition_paths, check_partition_models,
)
CONTRACTS.update(_PARTITION_CONTRACTS)
from .hsr_compact_fan_verify import (
    CONTRACTS as _COMPACT_FAN_CONTRACTS,
    check_paths as check_compact_fan_paths, check_models as check_compact_fan_models,
)
CONTRACTS.update(_COMPACT_FAN_CONTRACTS)
from .hsr_atomic_components_verify import (
    CONTRACTS as _ATOMIC_COMPONENT_CONTRACTS,
    check_paths as check_atomic_paths, check_models as check_atomic_models,
)
CONTRACTS.update(_ATOMIC_COMPONENT_CONTRACTS)


def _contract(spec):
    require(spec['recipe'] in CONTRACTS, 'Unknown HSR component requires an independent literal contract')
    contract = CONTRACTS[spec['recipe']]
    cells = [tuple(cell) for cell in spec['cells']]
    require(cells == contract['cells'] and tuple(spec['footprint']) == contract['footprint'],
            'HSR component footprint differs from its independent reserved cells')
    require([tuple(cell) for cell in spec.get('structural_cells', [])] == contract.get('structural_cells', []),
            'HSR component contains an undeclared structural-only cell')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(cells) and tiles,
            'HSR component allocation count differs from its reserved cells')
    base = tiles[0]-0x100*cells[0][0]-0x10*cells[0][1]
    require(tiles == [base+0x100*x+0x10*row for x, row in cells],
            'HSR component tile allocation differs from its AutoTileBase grid')
    return contract


def audit_height_profile(points, contract):
    """Reject vertical teleports, a hidden hump and sloped native connections."""
    lengths = [math.dist(a[:2], b[:2]) for a, b in zip(points, points[1:])]
    require(lengths and min(lengths) > EPS, 'HSR component has a zero-length horizontal segment')
    heights = [point[2] for point in points]
    rises = [b-a for a, b in zip(heights, heights[1:])]
    direction = heights[-1]-heights[0]
    if abs(direction) <= EPS:
        require(max(heights)-min(heights) <= EPS,
                'HSR component flat route contains an undeclared height change')
    else:
        require(all(rise*direction >= -EPS for rise in rises),
                'HSR component grade reverses instead of making a monotonic level transition')
    require(abs(rises[0]) < EPS and abs(rises[-1]) < EPS,
            'HSR component must have flat endpoint chords at native joins')
    collar = contract.get('flat_collar_m', 0.)
    if collar:
        for samples in (points, list(reversed(points))):
            distance = 0.
            for a, b in zip(samples, samples[1:]):
                distance += math.dist(a[:2], b[:2])
                if distance <= collar+EPS:
                    require(abs(b[2]-samples[0][2]) <= EPS,
                            'HSR component native join lacks its full flat collar')
                else:
                    fraction = (collar-(distance-math.dist(a[:2], b[:2])))/math.dist(a[:2], b[:2])
                    height = a[2]+fraction*(b[2]-a[2])
                    require(abs(height-samples[0][2]) <= EPS,
                            'HSR component native join lacks its full flat collar')
                    break
    return max((abs(rise)/run for rise, run in zip(rises, lengths)), default=0.)


def check_paths(resources, spec, donors=None):
    contract = _contract(spec)
    if spec['recipe'] in _ATOMIC_COMPONENT_CONTRACTS:
        return check_atomic_paths(resources, spec, donors)
    if spec['recipe'] in _COMPACT_FAN_CONTRACTS:
        return check_compact_fan_paths(resources, spec, donors)
    if spec['recipe'] in _PARTITION_CONTRACTS:
        return check_partition_paths(resources, spec)
    records = _encoded_routes(resources, spec, contract)
    ports, movements = _graph(records, contract)
    native = _native_port_headings(records, contract)
    journeys = _journeys(records, contract)
    quality, maximum_grade = {}, 0.
    for movement, points in journeys.items():
        maximum_grade = max(maximum_grade, audit_height_profile(points, contract))
        if contract['kind'] in ('paired_straight', 'paired_ramp'):
            axis = 0 if abs(points[-1][0]-points[0][0]) < EPS else 1
            require(all(abs(point[axis]-points[0][axis]) <= EPS for point in points),
                    'HSR component straight track departs from its literal native offset')
        limits = contract.get('quality_limits', {}).get(movement, _STRAIGHT)
        quality['>'.join(movement)] = measure_journey_quality(points, limits)
    if contract['kind'] == 'paired_ramp':
        north, south = journeys['Sin', 'Nout'], list(reversed(journeys['Nin', 'Sout']))
        for first, second in ((north, south), (south, north)):
            index = 0
            for point in first:
                while index < len(second)-2 and second[index+1][1] < point[1]-EPS:
                    index += 1
                a, b = second[index:index+2]
                t = (point[1]-a[1])/(b[1]-a[1])
                require(-EPS <= t <= 1.+EPS and abs(point[2]-(a[2]+t*(b[2]-a[2]))) <= EPS,
                        'HSR component paired ramp tracks do not share the same height profile')
    report = {'tile_count': len(contract['cells']), 'encoded_routes_checked': len(records),
              'external_ports_checked': ports, 'permitted_movements_checked': movements,
              'native_facing_port_tangents_checked': len(native),
              'unique_complete_journeys_checked': len(journeys), 'rotations_checked': 4,
              'exact_3d_cell_seams': True, 'all_encoded_tracks_used_by_intended_journeys': True,
              'unwanted_u_turns': False, 'unwanted_cross_level_transfers': False,
              'maximum_encoded_grade': maximum_grade, 'journey_quality': quality,
              'native_port_heights_m': sorted(set(point[2] for point in contract['ports'].values())),
              'collision_free_operation_claimed': False}
    report.update(audit_crossings(journeys, contract))
    if spec['recipe'] in _REFINED_COMPONENT_CONTRACTS:
        report.update(audit_refined_journeys(journeys, spec['recipe']))
    if spec['recipe'] in _TIGHT_LOOP_CONTRACTS:
        report.update(audit_tight_journeys(journeys, spec['recipe']))
    return report


def check_construction_fields(fields, spec, resources):
    from scp.verify import check_emitted_runtime_addresses
    report = _construction(fields, spec, resources, contract=_contract(spec))
    report['runtime_addresses'] = check_emitted_runtime_addresses(fields, spec)
    return report


def _section_intervals(triangles, z, height, *, floor=False):
    intervals = []
    for tri in triangles:
        if not all(abs(point[1]-height) < .0001 for point in tri):
            continue
        if floor and not all(.2158 <= point[3] <= 1.0042 for point in tri):
            continue
        xs = []
        for a, b in zip(tri, tri[1:]+tri[:1]):
            if abs(a[2]-z) <= EPS:
                xs.append(a[0])
            if (a[2] < z < b[2]) or (b[2] < z < a[2]):
                fraction = (z-a[2])/(b[2]-a[2])
                xs.append(a[0]+fraction*(b[0]-a[0]))
        if len(xs) >= 2 and max(xs)-min(xs) > 1e-7:
            intervals.append((min(xs), max(xs)))
    merged = []
    for first, last in sorted(intervals):
        if merged and first <= merged[-1][1]+.00005:
            merged[-1] = (merged[-1][0], max(last, merged[-1][1]))
        else:
            merged.append((first, last))
    return merged


def audit_adapter_native_profiles(triangles, *, paired_south_north_m=-120.):
    """Measure full slab widths, thickness and unobstructed paired collars.

    A narrow train corridor alone cannot prove a 15 m paired physical join.
    These literal sections inspect the actual saved mesh at all three native
    collar stations on each end, including the underneath slab surface.
    """
    triangles = list(triangles)
    checked = 0
    for z, expected, paired in [(-paired_south_north_m-d, [(-7.5, 7.5)], True)
            for d in (.5, 4., 7.5)]+[
            (-8.+d, [(-4., 4.), (12., 20.)], False) for d in (.5, 4., 7.5)]:
        for height, floor in ((31.189326, True), (29.01067, False)):
            actual = _section_intervals(triangles, z, height, floor=floor)
            require(len(actual) == len(expected) and all(
                abs(a-c) < .00005 and abs(b-d) < .00005
                for (a, b), (c, d) in zip(actual, expected)),
                f'HSR adapter native collar slab width, continuity or thickness differs: '
                f'z={z}, height={height}, intervals={actual}, expected={expected}')
            checked += 1
        expected_caps = ([(-7.5, -5.9965477), (5.9965477, 7.5)] if paired else
                         [(-4., -2.6), (2.6, 4.), (12., 13.4), (18.6, 20.)])
        caps = _section_intervals(triangles, z, 31.98933)
        require(len(caps) == len(expected_caps) and all(
            abs(a-c) < .00005 and abs(b-d) < .00005
            for (a, b), (c, d) in zip(caps, expected_caps)),
            f'HSR adapter native parapet top widths differ: z={z}, '
            f'intervals={caps}, expected={expected_caps}')
        if paired:
            # Native paired HSR has one unobstructed interior between its
            # exact inside parapet positions. Retaining two single-track
            # inside walls here would produce an apparent central barrier.
            for tri in triangles:
                if min(p[2] for p in tri)-EPS <= z <= max(p[2] for p in tri)+EPS:
                    points = []
                    for a, b in zip(tri, tri[1:]+tri[:1]):
                        if abs(a[2]-z) <= EPS:
                            points.append(a)
                        if (a[2] < z < b[2]) or (b[2] < z < a[2]):
                            t = (z-a[2])/(b[2]-a[2])
                            points.append(tuple(a[k]+t*(b[k]-a[k]) for k in range(5)))
                    require(not any(-5.9964 < p[0] < 5.9964 and 31.389326 < p[1] < 31.9894
                                    for p in points),
                            f'HSR adapter retains an internal wall in its native paired collar: '
                            f'z={z}, section={points}, triangle={tri}')
    return {'native_adapter_profile_sections_checked': checked,
            'native_paired_slab_width_m': 15., 'single_output_slab_width_m': 8.,
            'native_slab_floor_to_underside_m': 31.189326-29.01067,
            'paired_collar_internal_walls': False}


def check_models(resources, spec, donors=None):
    _contract(spec)
    if spec['recipe'] in _ATOMIC_COMPONENT_CONTRACTS:
        return check_atomic_models(resources, spec, donors)
    if spec['recipe'] in _COMPACT_FAN_CONTRACTS:
        return check_compact_fan_models(resources, spec, donors)
    if spec['recipe'] in _PARTITION_CONTRACTS:
        return check_partition_models(resources, spec)
    keys = {(*S3D, _number(spec['preview_id']))}
    for tile in map(_number, spec['tile_ids']):
        keys.update({(*S3D, tile+zoom) for zoom in range(5)})
        keys.update({(*PATH, tile), (*EXEMPLAR, tile)})
    immutable = tuple((key, resources[key]) for key in sorted(keys))
    return json.loads(_cached_models(json.dumps(spec, sort_keys=True, separators=(',', ':')), immutable))


# Keep one complete component build through its saved-resource audit.
# The immutable key still contains every inspected model, PATH and exemplar.
@lru_cache(maxsize=32)
def _cached_models(spec_json, immutable):
    spec, resources = json.loads(spec_json), dict(immutable)
    contract = _contract(spec)
    records = _encoded_routes(resources, spec, contract)
    triangles = _world_triangles(resources, spec, contract)
    report = _models(resources, spec, contract=contract)
    report.update(audit_bed_union(triangles, records))
    report.update(audit_visible_rails(triangles, records))
    report.update(audit_supports(triangles, contract))
    if contract['kind'] == 'paired_to_single_adapter':
        report.update(audit_adapter_native_profiles(triangles,
            paired_south_north_m=contract.get('native_paired_south_north_m', -120.)))
    if contract['kind'] == 'symmetric_graded_y':
        report.update(audit_y_native_profiles(triangles))
    if spec['recipe'] in _TIGHT_LOOP_CONTRACTS:
        report.update(audit_tight_native_profiles(triangles, spec['recipe']))
    reports = [assert_render_budget(parse_s3d(raw)) for key, raw in immutable if key[:2] == S3D]
    report['render_budget_models_checked'] = len(reports)
    report['render_group_budget_checked'] = True
    return json.dumps(report, sort_keys=True, separators=(',', ':'))


def verify_component(spec, resources, construction_fields=None):
    """Run the same audits used by portable saved-DAT verification."""
    report = {'paths': check_paths(resources, spec), 'models': check_models(resources, spec)}
    if construction_fields is not None:
        report['construction'] = check_construction_fields(construction_fields, spec, resources)
    return report
