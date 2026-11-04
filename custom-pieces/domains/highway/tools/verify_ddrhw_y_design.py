#!/usr/bin/env python3
"""Independently check the unregistered DD RHW Y source-route experiment.

The geometry writer is never imported. Native donor rows, their proper poses,
the agreed traffic brief, and exported finite polylines supply the inputs.
Passing this review establishes neither game resources nor physical models.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import itertools
import math
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp import jsonc

SUBJECT = ROOT / 'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction'
NAMES = ('A-B', 'B-A', 'A-C', 'C-A', 'B-C', 'C-B')
POSITION_TOLERANCE = 1e-9
HEADER = '''// title: "Independent compact DD RHW Y source verification"
// summary: "Verify native lane contacts, flat joins, grades, sampled radii, and continuous polyline clearance without importing the geometry writer."
//
// Used when: Reviewing the first unregistered DD RHW Y source-design candidate.
// Read by: Contributors and the assembly-design workflow; not a game-resource verifier.
// Updated by: domains/highway/tools/verify_ddrhw_y_design.py from the identified source report, brief, and native audit.
// Affects: Bounded source-feasibility evidence only; no saved resources, physical model approval, installation, or game observations.
'''


def require(condition, message):
    if not condition:
        raise ValueError(message)


def cross(a, b):
    return a[..., 0]*b[..., 1] - a[..., 1]*b[..., 0]


def _point_to_segment_squared(point, start, vector):
    delta = point-start
    fraction = np.sum(delta*vector, axis=-1)/np.sum(vector*vector, axis=-1)
    fraction = np.clip(fraction, 0., 1.)
    return np.sum((delta-fraction[..., None]*vector)**2, axis=-1)


def segment_distances(a0, a1, b0, b1):
    """Pairwise finite planar segment distance, to float64 arithmetic precision."""
    p, p1 = a0[:, None, :], a1[:, None, :]
    q, q1 = b0[None, :, :], b1[None, :, :]
    u, v = p1-p, q1-q
    d2 = np.minimum.reduce([
        _point_to_segment_squared(p, q, v),
        _point_to_segment_squared(p1, q, v),
        _point_to_segment_squared(q, p, u),
        _point_to_segment_squared(q1, p, u),
    ])
    determinant = cross(u, v)
    nonparallel = np.abs(determinant) > 1e-15
    denominator = np.where(nonparallel, determinant, 1.)
    along_a = cross(q-p, v)/denominator
    along_b = cross(q-p, u)/denominator
    intersection = nonparallel & (along_a >= 0.) & (along_a <= 1.) & (along_b >= 0.) & (along_b <= 1.)
    return np.sqrt(np.where(intersection, 0., d2))


def pair_clearance(a, b, parameters):
    """Conservatively gate exact planar distances by segment height intervals.

    Completely coplanar ribbons may require one unioned pavement surface.
    Their traffic corridors still need separation. This exception establishes
    no safe barriers, individual ribbon edges, or pavement union geometry.
    """
    vehicle_min, physical_min = math.inf, math.inf
    vehicle_witness = physical_witness = None
    coplanar_pairs = near_pairs = 0
    vehicle_width = parameters['vehicle_width_m']
    vehicle_height = parameters['vehicle_height_m']
    pavement_width = parameters['provisional_pavement_width_m']
    depth = parameters['provisional_deck_depth_m']
    bmin = np.minimum(b[:-1, 2], b[1:, 2])
    bmax = np.maximum(b[:-1, 2], b[1:, 2])
    for offset in range(0, len(a)-1, 80):
        stop = min(offset+80, len(a)-1)
        a0, a1 = a[offset:stop], a[offset+1:stop+1]
        amin = np.minimum(a0[:, 2], a1[:, 2])[:, None]
        amax = np.maximum(a0[:, 2], a1[:, 2])[:, None]
        gap = np.maximum(0., np.maximum(amin-bmax, bmin-amax))
        distances = segment_distances(a0[:, :2], a1[:, :2], b[:-1, :2], b[1:, :2])
        coplanar = (amax == amin) & (bmin == bmax) & (amin == bmin)
        coplanar_pairs += int(coplanar.sum())
        physical_near = (gap < vehicle_height+depth) & ~coplanar
        near_pairs += int(physical_near.sum())
        for selected, physical in ((gap < vehicle_height, False), (physical_near, True)):
            gated = np.where(selected, distances, np.inf)
            index = np.unravel_index(np.argmin(gated), gated.shape)
            value = float(gated[index])
            witness = [offset+int(index[0]), int(index[1])]
            if physical and value < physical_min:
                physical_min, physical_witness = value, witness
            elif not physical and value < vehicle_min:
                vehicle_min, vehicle_witness = value, witness
    physical_required = (pavement_width+vehicle_width)/2.
    return {
        'continuous_vehicle_plan_lower_bound_m': None if math.isinf(vehicle_min) else vehicle_min,
        'continuous_noncoplanar_road_vehicle_plan_lower_bound_m': None if math.isinf(physical_min) else physical_min,
        'vehicle_required_separation_m': vehicle_width,
        'noncoplanar_road_vehicle_required_separation_m': physical_required,
        'vehicle_corridor_pass': vehicle_min > vehicle_width,
        'noncoplanar_road_vehicle_corridor_pass': physical_min > physical_required,
        'vehicle_limiting_segment_indices': vehicle_witness,
        'road_vehicle_limiting_segment_indices': physical_witness,
        'exactly_coplanar_segment_pairs': coplanar_pairs,
        'noncoplanar_height_near_segment_pairs': near_pairs,
    }


def _rotate(point, turns):
    east, north, height = point
    for _ in range(turns % 4):
        east, north = north, -east
    return np.array([east, north, height], dtype=float)


def native_members(native, parameters):
    """Reconstruct socket contacts independently from measured native routes."""
    donors = {row['native_tile_id']: row for row in native['native_donors']}
    diagonal, orthogonal = parameters['diagonal_cell'], parameters['orthogonal_cell']
    require(type(diagonal) is int and type(orthogonal) is int and diagonal > 0 and orthogonal > 0,
            'Native socket placement requires positive whole city cells')
    cells = {'A': (-diagonal, diagonal), 'B': (-diagonal, -diagonal), 'C': (orthogonal, 0)}
    sockets = {row['arm']: row for row in native['first_alignment_socket_example']}
    require(set(sockets) == set(cells), 'Native audit must contain the three complete arm sockets')
    result = {}
    for arm, socket in sockets.items():
        old_cell = socket['outside_cell_col_row']
        old_origin = np.array([16.*old_cell[0], -16.*old_cell[1], 0.])
        origin = np.array([16.*cells[arm][0], -16.*cells[arm][1], 0.])
        require(math.dist(socket['outside_world_centre_en_m'], old_origin[:2]) < POSITION_TOLERANCE,
                'Native audit cell and world origin disagree')
        turns, edge = socket['native_clockwise_quarter_turns'], socket['native_shared_edge']
        reconstructed = []
        for route in donors[socket['native_tile_id']]['real_car_routes']:
            require(route['transport'] == 1 and route['compatibility'] == 0,
                    'Only measured real native car routes may supply this design')
            entry, exit_ = (route['entry']+turns) % 4, (route['exit']+turns) % 4
            if edge not in (entry, exit_):
                continue
            points = [_rotate(point, turns) for point in route['points']]
            require(all(point[2] == points[0][2] for point in points), 'Native joining deck must be level')
            height = points[0][2]
            require(height in (7.5, 15.), 'Capacity-only or unsupported-height native route')
            direction = 'native-to-core' if exit_ == edge else 'core-to-native'
            contact = points[-1] if direction == 'native-to-core' else points[0]
            tangent = points[-1]-points[0]
            tangent /= np.linalg.norm(tangent[:2])
            level = 'L2' if height == 15. else 'L1'
            key = (arm, level, route['lane'], direction)
            require(key not in result, 'Duplicate native lane member')
            matches = [row for row in socket['members'] if row['lane'] == route['lane']
                       and row['direction'] == direction and row['level'] == level]
            require(len(matches) == 1, 'Native posed contact is absent or ambiguous in its audit')
            measured = matches[0]
            require(measured['transport'] == 1 and measured['compatibility'] == 0
                    and math.dist(measured['endpoint_enh_m'], contact+old_origin) < POSITION_TOLERANCE
                    and math.dist(measured['unit_travel_tangent_enh'], tangent) < POSITION_TOLERANCE,
                    'Native audit posed member differs from its actual donor route')
            result[key] = {'point': contact+origin, 'tangent': tangent,
                           'transport': route['transport'], 'compatibility': route['compatibility'],
                           'native_tile_id': socket['native_tile_id'], 'native_rotation': turns,
                           'outside_cell': list(cells[arm])}
            reconstructed.append(key)
        require(len(reconstructed) == len(socket['members']) == 4, 'Each DD socket needs four real lane members')
    require(len(result) == 12, 'Expected twelve native joining members')
    return result


def _collar(points, tangent, length, end=False):
    points = points[::-1] if end else points
    tangent = -tangent if end else tangent
    distance = np.r_[0., np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1).cumsum()]
    require(distance[-1] >= length, 'Lane is shorter than its required native collar')
    boundary = np.array([np.interp(length, distance, points[:, axis]) for axis in range(3)])
    sample = np.vstack([points[distance < length], boundary])
    lateral = float(np.abs(cross(sample[:, :2]-points[0, :2], tangent[:2])).max())
    vertical = float(np.abs(sample[:, 2]-points[0, 2]).max())
    require(lateral < POSITION_TOLERANCE and vertical < POSITION_TOLERANCE,
            'Native three-metre collar changes tangent or height')
    first = points[1]-points[0]
    first /= np.linalg.norm(first[:2])
    require(math.dist(first, tangent) < POSITION_TOLERANCE, 'Native endpoint travel tangent changed')
    return {'length_checked_m': length, 'maximum_lateral_error_m': lateral,
            'maximum_height_error_m': vertical}


def _sampled_radius(points):
    """Minimum circumradius through adjacent source-polyline triples."""
    first, last = np.diff(points[:, :2], axis=0)[:-1], np.diff(points[:, :2], axis=0)[1:]
    area_twice = np.abs(cross(first, last))
    turning = area_twice > 1e-14
    if not turning.any():
        return None
    numerator = (np.linalg.norm(first, axis=1)*np.linalg.norm(last, axis=1)
                 *np.linalg.norm(first+last, axis=1))
    return float(np.min(numerator[turning]/(2.*area_twice[turning])))


def _route_checks(report, brief, native):
    require(report.get('schema_version') == 1 and brief.get('registered') is False,
            'This verifier accepts only the unregistered source-design stage')
    p = brief['geometry_parameters']
    require(report['parameters'] == p, 'Source geometry parameters differ from the agreed brief')
    for key in ('native_collar_m', 'sampling_step_m', 'vehicle_width_m', 'vehicle_height_m',
                'provisional_pavement_width_m', 'provisional_deck_depth_m'):
        require(type(p[key]) in (int, float) and math.isfinite(p[key]) and p[key] > 0,
                'Invalid positive source bound: '+key)
    require(p['native_collar_m'] >= 3., 'The native collar must retain at least three metres')
    require(p['provisional_deck_depth_m'] >= 1., 'Source review must include the measured one-metre native skirt depth')
    require(p['vehicle_width_m'] >= 2.5 and p['vehicle_height_m'] >= 3.8,
            'The declared source vehicle envelope is smaller than the selected contract')
    require(brief['native_decks']['upper_m'] == 15. and brief['native_decks']['lower_m'] == 7.5
            and brief['native_decks']['lanes_per_deck'] == 2, 'Native DD deck service changed')
    limit = brief['requirements']['maximum_grade_percent']
    require(type(limit) in (float, int) and 0 < limit <= 30., 'Experimental grade bound must not exceed thirty percent')
    require(set(report['routes']) == set(NAMES) and set(report['route_metadata']) == set(NAMES),
            'Source design must contain exactly the six agreed directed journeys')
    allocations = native['proposed_single_lane_allocation']['routes']
    require(len(allocations) == 6, 'Native lane allocation must cover six journeys')
    allocation = {row['from_arm']+'-'+row['to_arm']: row for row in allocations}
    require(set(allocation) == set(NAMES), 'Native lane allocation omits or duplicates a journey')
    expected_brief = {row['id']: row for row in brief['journeys']}
    require(set(expected_brief) == set(NAMES), 'Brief journey identities changed')
    members = native_members(native, p)
    used, arrays, checks = set(), {}, {}
    for name in NAMES:
        meta = report['route_metadata'][name]
        expected = allocation[name]
        require(meta == {**expected, 'engine_transport': 1, 'compatibility': 0},
                'Native lane metadata changed for '+name)
        source = (meta['from_arm'], meta['from_deck'], meta['from_lane'], 'native-to-core')
        target = (meta['to_arm'], meta['to_deck'], meta['to_lane'], 'core-to-native')
        require(source in members and target in members and source not in used and target not in used,
                'Native lane contact is missing or reused by another journey')
        used.update((source, target))
        points = np.asarray(report['routes'][name], dtype=np.float64)
        require(points.ndim == 2 and points.shape[1] == 3 and len(points) >= 4
                and np.isfinite(points).all(), 'Invalid finite source polyline for '+name)
        steps = np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1)
        require(np.all(steps > 1e-10), 'Stationary or vertical source segment in '+name)
        require(steps.max() <= p['sampling_step_m']+1e-8, 'Source sampling bound exceeded for '+name)
        start, end = members[source], members[target]
        error = max(math.dist(points[0], start['point']), math.dist(points[-1], end['point']))
        require(error < POSITION_TOLERANCE, 'Native endpoint moved or lane contacts swapped for '+name)
        journey = expected_brief[name]
        require(journey['lanes'] == 1 and journey['from'] == meta['from_arm'] and journey['to'] == meta['to_arm']
                and journey['start_height_m'] == start['point'][2] and journey['end_height_m'] == end['point'][2],
                'Brief lane service disagrees with measured native ends')
        grade = np.diff(points[:, 2])/steps
        maximum = float(np.abs(grade).max()*100.)
        require(maximum <= limit+1e-7, 'Source grade exceeds its experimental bound for '+name)
        if name in ('B-C', 'C-B'):
            require(np.all(grade >= -1e-10), 'Branch link must climb monotonically between the selected decks')
        else:
            require(np.max(np.abs(points[:, 2]-start['point'][2])) < POSITION_TOLERANCE,
                    'An agreed flat stem journey changes height')
        start_collar = _collar(points, start['tangent'], p['native_collar_m'])
        end_collar = _collar(points, end['tangent'], p['native_collar_m'], end=True)
        radius = _sampled_radius(points)
        require(radius is None or radius >= 24.-1e-6, 'Sampled source radius is below the selected twenty-four-metre family')
        arrays[name] = points
        checks[name] = {'native_start_member': list(source), 'native_end_member': list(target),
                        'endpoint_maximum_error_m': error, 'horizontal_length_m': float(steps.sum()),
                        'maximum_grade_percent': maximum, 'sampled_minimum_radius_m': radius,
                        'start_native_collar': start_collar, 'end_native_collar': end_collar}
    require(used == set(members), 'Source routes do not consume all twelve native members exactly once')
    return arrays, checks


def _negative_controls(report, brief, native, arrays):
    controls = {}
    displaced = deepcopy(report)
    displaced['routes']['A-B'][0][0] += .05
    try:
        _route_checks(displaced, brief, native)
    except ValueError as error:
        controls['displaced_native_endpoint'] = {'rejected': True, 'reason': str(error)}
    else:
        controls['displaced_native_endpoint'] = {'rejected': False}
    steep = deepcopy(report)
    middle = len(steep['routes']['B-C'])//2
    steep['routes']['B-C'][middle][2] += .5
    try:
        _route_checks(steep, brief, native)
    except ValueError as error:
        controls['interior_grade_spike'] = {'rejected': True, 'reason': str(error)}
    else:
        controls['interior_grade_spike'] = {'rejected': False}
    # The two opposing ramp routes share the same XY corridor, retaining all
    # endpoint positions, collar tangents, grades, and native lane metadata.
    coincident = arrays['B-C'][::-1].copy()
    coincident[:, 2] = 22.5-coincident[:, 2]
    collision = pair_clearance(arrays['B-C'], coincident, brief['geometry_parameters'])
    controls['coincident_climbing_route_corridors'] = {
        'rejected': not collision['vehicle_corridor_pass'],
        'continuous_vehicle_plan_lower_bound_m': collision['continuous_vehicle_plan_lower_bound_m'],
        'reason': 'Opposing ramps on an identical plan corridor meet while their deck ordering reverses.'}
    require(all(row['rejected'] for row in controls.values()), 'A required source negative control was not rejected')
    return controls


def verify(report, brief, native, *, negative_controls=False):
    """Verify parsed source objects, raising ValueError on a measured defect."""
    arrays, route_checks = _route_checks(report, brief, native)
    pairs = []
    for a, b in itertools.combinations(NAMES, 2):
        check = pair_clearance(arrays[a], arrays[b], brief['geometry_parameters'])
        require(check['vehicle_corridor_pass'], 'Continuous source vehicle corridors overlap: '+a+' / '+b)
        require(check['noncoplanar_road_vehicle_corridor_pass'],
                'Continuous noncoplanar source road/vehicle clearance fails: '+a+' / '+b)
        pairs.append({'pair': [a, b], **check})
    return {
        'schema_version': 1, 'passed': True,
        'scope': 'Independent source-polyline checks only; first measured grid alignment.',
        'geometry_writer_imported': False, 'native_members_checked': 12,
        'route_checks': route_checks, 'continuous_pair_checks': pairs,
        'envelope_parameters': {key: brief['geometry_parameters'][key] for key in (
            'vehicle_width_m', 'vehicle_height_m', 'provisional_pavement_width_m', 'provisional_deck_depth_m')},
        'coplanar_policy': 'Separate traffic corridors may share one coordinated pavement union. Barriers and individual ribbon edges remain unverified.',
        'negative_controls': _negative_controls(report, brief, native, arrays) if negative_controls else {},
        'limits': [
            'Finite planar segment distances and conservative height intervals bound the supplied piecewise-linear source routes, within float64 arithmetic.',
            'Native contacts are reconstructed from the exported measured donor routes and proper poses; this command does not reread proprietary native archives.',
            'The radius bound is sampled through adjacent polyline triples; no continuous analytic-curve radius is claimed.',
            'Actual pavement unions, mesh datums, markings, barriers, deck solids, supports, overhangs, full moving vehicle bodies, and structural capacity remain unverified.',
            'Construction ownership, safe reusable module cuts, identifiers, saved PATH/S3D resources, native dragging, game placement, installation, and human traffic observations remain unverified.',
            'This candidate does not prove a smallest footprint or establish a second grid alignment.',
        ],
        'game_operation_tested': False,
    }


def verify_files(report_path, brief_path, native_path, *, negative_controls=True):
    report, brief, native = (jsonc.load(path) for path in (report_path, brief_path, native_path))
    inputs = {key: hashlib.sha256(path.read_bytes()).hexdigest() for key, path in (
        ('design_brief_sha256', brief_path), ('native_design_inputs_sha256', native_path),
        ('geometry_tool_sha256', Path(__file__).with_name('ddrhw_y_geometry.py')))}
    require(report.get('input_fingerprints') == inputs, 'Source geometry input fingerprints are stale or missing')
    result = verify(report, brief, native, negative_controls=negative_controls)
    result['source'] = {'design_geometry_sha256': hashlib.sha256(report_path.read_bytes()).hexdigest(),
                        **inputs, 'independent_verifier_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geometry', type=Path, default=SUBJECT/'evidence/design-geometry.jsonc')
    parser.add_argument('--brief', type=Path, default=SUBJECT/'checks/design-brief.jsonc')
    parser.add_argument('--native-audit', type=Path, default=SUBJECT/'evidence/native-design-inputs.jsonc')
    parser.add_argument('--output', type=Path, default=SUBJECT/'evidence/source-verification.jsonc')
    args = parser.parse_args(argv)
    result = verify_files(args.geometry, args.brief, args.native_audit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if not args.output.exists():
        args.output.write_text(HEADER, encoding='utf-8')
    jsonc.dump(args.output, result)
    print('Source checks passed: twelve native members, six journeys, fifteen continuous pair checks, and three rejected negative controls.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
