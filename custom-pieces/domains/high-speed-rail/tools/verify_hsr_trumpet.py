#!/usr/bin/env python3
"""Audit the current trumpet directly against approved resource fingerprints.

Every current DAT, placed tile model/PATH/shadow, orientation and complete
journey is pinned exactly. Independent physical audits then check all ports,
travel directions, native joins, rotations, clearances, supports and budgets.
Historical atomization decisions are descriptive records; predecessor source
folders, layout files and DAT fixtures are neither retained nor required.
This tool never installs files or records observations inside the game.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from copy import deepcopy
import json
import math
from pathlib import Path
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'project.json').is_file())
sys.path.insert(0, str(ROOT/'framework'))

from scp.dbpf import require
from scp.verification_fixtures import resource_descriptor, verification_resources
from scp_hsr.directional_t_verify import _journeys, audit_visible_rails, _TURN_LIMITS
from scp_hsr.hsr_components_verify import CONTRACTS, verify_component
from scp_hsr.hsr_mesh_verify import audit_crossings, measure_journey_quality
from scp_hsr.hsr_trumpet_verify import CONTRACT, direct_slip_symmetry, key, physical_layout, rotate, split_flags
from scp_hsr.interchange_verify import _graph, _clearance_segments
from scp_hsr.assembly_inspection import encoded_records, load_build, number, placements, rotation, sha256, triangle_count, world_tiles, _world_triangles
from scp_hsr.hsr_compact_fan_verify import audit_bed_corridors

ASSEMBLY = ROOT/'domains/high-speed-rail/01_assemblies/straight-stem-trumpet'
SCENE = ASSEMBLY/'assembly.json'
QUALITY_PATH = ASSEMBLY/'checks/contract.json'
RESOURCES_PATH = ASSEMBLY/'checks/resources.json'
STRAIGHT_ID = 'hsr-component-lower-paired-straight'
ONEWAY_ID = 'hsr-component-lower-oneway-straight'
NEW_IDS = frozenset({
    'hsr-component-l2-short-mainline-diverge-core', 'hsr-component-l2-short-opposed-merge-core',
    'hsr-component-l2-shortened-departure-curve', 'hsr-component-l2-shortened-return-curve',
})
CURRENT_IDS = NEW_IDS | frozenset({
    'hsr-component-l2-compact-fan-diverge', 'hsr-component-l2-paired-fan-compact-join',
    'hsr-component-lower-paired-straight', 'hsr-component-lower-oneway-straight',
    'hsr-component-modular-south-junction', 'hsr-component-modular-paired-climb',
    'hsr-component-modular-crossing-core', 'hsr-component-upper-paired-straight',
    'hsr-component-tight-paired-curve90-l4-to-mid', 'hsr-component-tight-paired-curve90-mid-to-l2',
})
REPLACEMENTS = {
    (-112., 0.): (STRAIGHT_ID, 3), (112., 0.): (STRAIGHT_ID, 3),
    (-16., -112.): (ONEWAY_ID, 2), (16., -112.): (ONEWAY_ID, 0),
}
ELIGIBLE_CANDIDATES = {
    'p01a-west-tail': ({(-112., 0.), (-96., 0.)},
                       'hsr-component-l2-short-mainline-diverge-core', STRAIGHT_ID, 270, .0245),
    'p03b-east-tail': ({(96., 0.), (112., 0.)},
                       'hsr-component-l2-short-opposed-merge-core', STRAIGHT_ID, 270, .0245),
    'p01b-south-tail': ({(-16., -112.), (-16., -96.)},
                        'hsr-component-l2-shortened-departure-curve', ONEWAY_ID, 180, .0082),
    'p03d-south-tail': ({(16., -112.), (16., -96.)},
                        'hsr-component-l2-shortened-return-curve', ONEWAY_ID, 0, .0082),
}


def canonical_sha256(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def audit_quality_contract(path=QUALITY_PATH):
    literal = json.loads(Path(path).read_text())
    expected = {
        'schema_version': 2, 'id': 'straight-stem-trumpet', 'occupied_cells': 109,
        'encoded_fragments': 167, 'unique_piers': 75, 'placements': 26, 'unique_piece_types': 14,
        'candidate_eligibility_strictly_below_m': .005, 'minimum_pier_spacing_m': 16.,
        'minimum_clearance': 5., 'actual_tile_triangles': 659271,
        'current_resource_contract': 'resources.json',
        'required_grade_separated_crossings': 4,
        'expected_crossings_xyz': [list(p) for p in CONTRACT['expected_crossings_xyz']],
    }
    require(all(literal.get(k) == v for k, v in expected.items()),
            'Trumpet independent quality contract differs from its literal acceptance policy')
    require({k: tuple(v) for k, v in literal['ports'].items()} == CONTRACT['ports']
            and [tuple(v) for v in literal['movements']] == CONTRACT['movements'],
            'Trumpet outside connections differ from the independently authored assembly contract')
    require(literal['inherited_custom_cut_policy'] == {
        'departure_port': 'Win', 'return_port': 'Eout', 'depth_m': 2.65, 'width_m': 5.2,
        'require_exact_original_port_tile_models_all_five_zooms': True,
        'whole_assembly_uses_strict_unclipped_actual_neighbour_paths': True,
        'native_new_join_profile_tolerance_m': .00005},
        'Trumpet inherited custom-cut or native joining policy differs')
    require(literal['whole_route_quality'] == {
        'direct_slips': {'minimum_radius_m': 24., 'maximum_total_turn_degrees': 130.,
                         'maximum_curvature_change_per_m2': .0015,
                         'maximum_native_endpoint_curvature_per_m': .0005},
        'other_four_journeys': 'Exact approved current encoded geometry; all constituent modules retain their existing independent physical contracts.'},
        'Trumpet complete route quality policy differs')
    return {'contract_sha256': sha256(Path(path).read_bytes()),
            'candidate_eligibility_and_actual_edit_limits_are_separate': True,
            'independent_ports_movements_clearance_and_budgets_checked': True,
            'predecessor_resource_inputs_required': False}


def audit_approved_layout(scene):
    frozen = json.loads((ASSEMBLY/'checks/layout.json').read_text())
    normalized = canonical_sha256(frozen['layout'])
    require(frozen['schema_version'] == 1 and frozen['assembly_id'] == 'straight-stem-trumpet'
            and normalized == frozen['layout_sha256']
            == '7d230df3d8697640ed5b197f448e041abd75cab62be2a9886562e4fc52909ee6',
            'Trumpet independently reviewed layout record changed')
    require(physical_layout(scene) == frozen['layout'], 'Trumpet physical layout differs from its approved positions')
    return {'layout_sha256': frozen['layout_sha256'], 'reviewed_placements': 26,
            'approved_external_ports_rectangle_and_grid': True}


def audit_candidate_ledger(path=None, descriptor=None):
    """Validate frozen decisions and current replacements without old inputs."""
    path = ASSEMBLY/'checks/atomization.json' if path is None else Path(path)
    ledger = json.loads(path.read_text())
    descriptor = resource_descriptor(RESOURCES_PATH) if descriptor is None else descriptor
    require(ledger.get('schema_version') == 2 and ledger.get('assembly_id') == 'straight-stem-trumpet'
            and ledger.get('historical_inputs_required') is False,
            'Trumpet atomization ledger identity or historical-input policy differs')
    policy = ledger['policy']
    require(policy['candidate_eligibility_strictly_below_m'] == .005
            and policy['actual_rework_bounds_separate'] is True
            and policy['render_after_geometry_complete'] is True,
            'Trumpet atomization policy differs from the approved procedure')
    candidates = ledger['candidates']
    require(len(candidates) == len({c['id'] for c in candidates}) == 17, 'Trumpet atomization ledger omits or repeats a decision')
    approved = {c['id']: c for c in candidates if c['decision'] == 'atomized'}
    require(set(approved) == set(ELIGIBLE_CANDIDATES), 'Trumpet atomization ledger approves an unauthorized candidate')
    require(all(c['decision'] in ('atomized', 'retained') and c.get('reason') for c in candidates),
            'Trumpet candidate decisions need an explicit status and reason')
    measurements = {}
    for identifier, (cells, core_id, straight_id, angle, bound) in ELIGIBLE_CANDIDATES.items():
        candidate = approved[identifier]
        measured, visible = candidate['original_path_deviation_m'], candidate['original_visible_rail_deviation_m']
        require(all(isinstance(v, (int, float)) and math.isfinite(v) and 0. <= v < .005
                    for v in (measured, visible)), 'Trumpet candidate is not strictly below the5mm original eligibility threshold')
        require(abs(visible-measured) <= .000005,
                'Trumpet recorded original visible rail does not support its sub5mm PATH eligibility')
        replacement, work = candidate['replacement'], candidate['actual_rework']
        require(replacement['straight_piece_id'] == straight_id
                and replacement['straight_rotation_degrees'] == angle
                and replacement['new_core_piece_id'] == core_id,
                'Trumpet candidate replacement differs from its approved native type or direction')
        require(work['independent_bound_m'] == bound and 0. <= work['maximum_route_change_m'] <= bound
                and set(map(tuple, work['allowed_world_cells_en_m'])) == cells,
                'Trumpet recorded actual rework differs from its finite approved bound')
        current_source = ROOT/'domains/high-speed-rail/00_pieces'/core_id/'geometry.json'
        require(sha256(current_source.read_bytes()) == candidate['replacement_geometry_sha256'],
                'Trumpet atomization decision is stale for its changed replacement geometry')
        require(isinstance(work.get('measurement_method'), str) and bool(work['measurement_method'].strip()),
                'Trumpet recorded measured correction needs its explicit measurement method')
        measurements[identifier] = {'recorded_original_path_deviation_m': measured,
            'recorded_original_visible_rail_deviation_m': visible,
            'recorded_actual_rework_bound_m': bound,
            'current_replacement_geometry_sha256': candidate['replacement_geometry_sha256']}
    inventory = ledger['source_cell_inventory']
    identities = [(cell['source_piece_id'], *cell['standalone_xy']) for cell in inventory]
    require(len(identities) == len(set(identities)) == ledger['source_cells_reviewed'] == 51,
            'Trumpet atomization ledger omits or repeats an original reviewed cell')
    require(all(cell.get('reason') and (cell['candidate_id'] is None or cell['candidate_id'] in {c['id'] for c in candidates})
                for cell in inventory), 'Trumpet cell inventory lacks its decision or linked candidate')
    history = {'candidates': candidates, 'source_cell_inventory': inventory,
               'source_cells_reviewed': ledger['source_cells_reviewed']}
    require(canonical_sha256(history) == descriptor['atomization_history_sha256'],
            'Trumpet frozen atomization measurements or local and assembly coordinates changed')
    require(ledger['current_resource_contract'] == 'resources.json'
            and ledger['current_resource_contract_sha256'] == sha256(RESOURCES_PATH.read_bytes()),
            'Trumpet atomization ledger references a different current resource contract')
    require(ledger['observations_inside_game'] == 'unverified', 'Trumpet software atomization cannot create game observations')
    return {'ledger_sha256': sha256(path.read_bytes()), 'eligible_atomized_candidates': measurements,
            'retained_candidates': 13, 'original_owned_cells_reviewed': 51,
            'strict_original_threshold_m': .005, 'old_deviation_and_actual_work_recorded_separately': True,
            'historical_measurements_are_frozen_not_remeasured': True,
            'deleted_predecessor_resources_required': False}


def audit_current_world_tiles(candidate, descriptor):
    expected = {tuple(cell['world_east_north_m']): cell for cell in descriptor['world_cells']}
    require(len(expected) == len(descriptor['world_cells']) == 109 and set(candidate) == set(expected),
            'Trumpet occupied world tiles differ from the approved current resource contract')
    for position, tile in candidate.items():
        record = expected[position]
        require(tile['piece_id'] == record['piece_id'] and list(tile['cell']) == record['cell']
                and tile['rotation'] == record['rotation_quarter_turns_ccw'],
                f'Trumpet approved current tile owner, local cell or orientation changed at {position}')
        hashes = {family: sha256(raw) for family, raw in tile['resources'].items()}
        require(hashes == record['resources_sha256'],
                f'Trumpet approved current saved tile resources changed at {position}')
    for position, (identifier, turns) in REPLACEMENTS.items():
        require(candidate[position]['piece_id'] == identifier and candidate[position]['rotation'] == turns,
                'Trumpet extracted tile is not the correctly directed existing standard straight')
    triangles = sum(triangle_count(t['resources']['model_0']) for t in candidate.values())
    require(triangles == descriptor['actual_tile_triangles'] == 659271,
            'Trumpet approved current actual triangle inventory differs')
    return {'occupied_cells': 109, 'strict_byte_identity_cells': 109,
            'actual_tile_triangles': triangles, 'tile_resource_fingerprints_checked': 109*11,
            'exact_current_ownership_and_rotations_checked': True,
            'original_standard_straight_replacements': 4}


def audit_current_journeys(journeys, descriptor):
    expected = {tuple(record['movement']): record for record in descriptor['journeys']}
    require(len(expected) == len(descriptor['journeys']) == 6 and set(journeys) == set(expected)
            == set(CONTRACT['movements']), 'Trumpet current directed journey inventory differs')
    for movement, points in journeys.items():
        record = expected[movement]
        require(len(points) == record['encoded_points'] and canonical_sha256(points) == record['points_sha256'],
                f'Trumpet approved complete encoded journey geometry changed: {movement}')
    return {'complete_directed_journeys_frozen': 6, 'all_encoded_point_positions_and_counts_identical': True}


def audit_whole_route_quality(journeys):
    """Retain strict complete direct-slip quality and frozen loop geometry."""
    reports = {}
    for movement in (('W_in', 'S_out'), ('S_in', 'E_out')):
        reports['>'.join(movement)] = measure_journey_quality(
            journeys[movement], {**_TURN_LIMITS, 'max_total_turn_degrees': 130.})
    return {'direct_slips': reports, 'other_complete_journeys_frozen_exactly': 4,
            'radius_minimum_m': 24., 'curvature_change_limit_per_m2': .0015,
            'native_endpoint_curvature_limit_per_m': .0005,
            'constituent_module_quality_limits_remain_unchanged': True}


def audit_assembled_geometry(tiles, records):
    instances = {tile['instance_id'] for tile in tiles.values()}
    selected = [record for record in records if record[1]['instance_id'] in instances]
    points = [p for _, _, route in selected for p in route]
    east = min(p[0] for p in points)-2.5, max(p[0] for p in points)+2.5
    north = min(p[1] for p in points)-2.5, max(p[1] for p in points)+2.5
    neighbours = {pos for pos in tiles if pos[0]+8. >= east[0] and pos[0]-8. <= east[1]
                  and pos[1]+8. >= north[0] and pos[1]-8. <= north[1]}
    triangles = list(_world_triangles(tiles, neighbours))
    report = audit_bed_corridors(triangles, selected)
    report.update(audit_visible_rails(triangles, records))
    buckets = defaultdict(list)
    for tri in triangles:
        for x in range(math.floor(min(p[0] for p in tri)/4.), math.floor(max(p[0] for p in tri)/4.)+1):
            for z in range(math.floor(min(p[2] for p in tri)/4.), math.floor(max(p[2] for p in tri)/4.)+1):
                buckets[x, z].append(tri)
    report['complete_train_clearance_segments_checked'] = _clearance_segments(selected, buckets, half_width=2.5)
    return {**report, 'actual_module_instances_checked': len(instances),
            'actual_neighbour_models_used': len(neighbours), 'strict_unclipped_actual_path_audit': True}


def verify(build_path, scene_path=SCENE):
    raw = Path(scene_path).read_bytes()
    scene = json.loads(raw)
    layout, quality = audit_approved_layout(scene), audit_quality_contract()
    descriptor = resource_descriptor(RESOURCES_PATH)
    verification_resources(RESOURCES_PATH, build_path, selected_piece_ids=CURRENT_IDS,
                           assembly_id='straight-stem-trumpet')
    require(descriptor['layout_sha256'] == layout['layout_sha256'], 'Trumpet resource contract pins a different physical layout')
    build = load_build(build_path)
    candidate, sources = world_tiles(scene, build)
    decisions = audit_candidate_ledger(descriptor=descriptor)
    geometry = audit_current_world_tiles(candidate, descriptor)
    owned = sum(1 for _ in _world_triangles(candidate))
    require(owned == geometry['actual_tile_triangles'] == sum(s['preview_triangles'] for s in sources),
            'Trumpet ownership or actual preview triangle inventory differs')
    records = encoded_records(candidate)
    require(len(records) == 167, 'Trumpet must contain exactly167 encoded fragments')
    journeys = _journeys(records, CONTRACT)
    paths = {'encoded_fragments': len(records), 'approved_current_journeys': audit_current_journeys(journeys, descriptor),
             'direct_slip_symmetry': direct_slip_symmetry(journeys), 'proper_rotations': [],
             'whole_route_quality': audit_whole_route_quality(journeys)}
    for turns in range(4):
        contract = deepcopy(CONTRACT)
        contract['ports'] = {name: key(rotate(p, turns)) for name, p in CONTRACT['ports'].items()}
        contract['expected_crossings_xyz'] = [(*rotate((x, north, upper), turns)[:2], upper, lower)
                                              for x, north, upper, lower in CONTRACT['expected_crossings_xyz']]
        transformed = [(cell, meta, [key(rotate(p, turns)) for p in points]) for cell, meta, points in records]
        require(_graph(transformed, contract) == (6, 6), 'Trumpet directed travel matrix differs')
        moved = _journeys(transformed, contract)
        require(split_flags(transformed) == 3, 'Trumpet split flags differ')
        paths['proper_rotations'].append({'rotation_degrees_ccw': turns*90, 'unique_journeys': 6,
                                          **audit_crossings(moved, contract)})
    geometry['complete_actual_assembly_corridors'] = audit_assembled_geometry(candidate, records)
    checked, audits, supports = set(), [], []
    for instance in placements(scene):
        piece = build['pieces'][instance['piece_id']]
        if piece['recipe'] not in checked:
            saved = build['resources'](piece)
            audits.append({'piece_id': piece['id'], 'dat_sha256': saved['sha256'],
                           'audit': verify_component(piece, saved['resources'])})
            checked.add(piece['recipe'])
        for east, south in CONTRACTS[piece['recipe']]['support_centres_xz']:
            x, north, _ = rotate((east, -south, 0.), rotation(instance))
            supports.append(key((x+instance['origin_m'][0], north+instance['origin_m'][1], 0.))[:2])
    require(len(placements(scene)) == 26 and len(checked) == 14, 'Trumpet placement/type totals differ')
    require(len(supports) == len(set(supports)) == 75, 'Trumpet must retain75 unique piers')
    minimum = min(math.dist(a, b) for i, a in enumerate(supports) for b in supports[:i])
    require(minimum >= 16.-2e-6, 'Trumpet global pier spacing is below16m')
    return {'purpose': __doc__.split('\n\n')[0], 'schema_version': 2, 'status': 'passed',
            'scope': 'actual approved current saved compiled resources; game operation unverified',
            'scene_file': Path(scene_path).name, 'scene_sha256': sha256(raw),
            'manifest_sha256': build['manifest_sha256'], 'audited_manifest_file': 'audited-build-manifest.json',
            'manifest_hash_scope': 'Exact input manifest at audit start. Documentation-only metadata may change later; actual DAT fingerprints are independently pinned.',
            'audited_manifest_file_scope': 'Current binary payload registry with generated documentation excluded; the full input manifest hash is recorded separately as audit-start metadata.',
            'current_resource_contract_sha256': sha256(RESOURCES_PATH.read_bytes()),
            'deleted_predecessor_resource_inputs_required': False,
            'reviewed_layout': layout, 'independent_quality_contract': quality, 'atomization_decisions': decisions,
            'geometry': geometry, 'encoded_paths': paths, 'sources': sources,
            'independent_component_audits': audits,
            'supports': {'total_column_positions_preserved': 75, 'minimum_global_centre_spacing_m': minimum},
            'game_tests': 'unverified'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', required=True, type=Path)
    parser.add_argument('--scene', default=SCENE, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    report = verify(args.build, args.scene)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'occupied_cells': 109, 'preserved_piers': 75,
                      'strict_byte_identity_cells': report['geometry']['strict_byte_identity_cells'],
                      'proper_rotations_checked': 4, 'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
