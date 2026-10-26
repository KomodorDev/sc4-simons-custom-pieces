#!/usr/bin/env python3
"""Consume source-owned exports and audit the two-piece placement pilot.

Reports are generated only below SCP Planner's local directory. This command
does not build, install, alter game resources, or record manual observations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
PLANNER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLANNER / 'src'))

from scp_planner.metadata import find_matches, load_pilot


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def within(root, relative):
    root = Path(root).resolve()
    relative = Path(relative)
    target = (root / relative).resolve()
    if relative.is_absolute() or '..' in relative.parts or not target.is_relative_to(root):
        raise ValueError('Source path must stay inside its explicit root')
    return target


def verify_compiled(custom_root, build, resolved, domain_id='high-speed-rail'):
    """Delegate compiled audits to SCP; omit full polylines from this placement report."""
    from scp_planner._source import source_module
    report = source_module('connector_metadata').verify_compiled(custom_root, build, resolved, domain_id)
    return {**report, 'pieces': {identifier: {key: value for key, value in item.items()
                                           if key not in ('routes', 'endpoint_route_refs')}
                                for identifier, item in report['pieces'].items()}}


def check_preserved_inputs(custom_root, snapshot_name='source-snapshot.json'):
    snapshot = PLANNER / 'local/pilot' / snapshot_name
    if not snapshot.is_file():
        return {'status': 'not_recorded', 'reason': 'No original pilot snapshot in this checkout'}
    files = read_json(snapshot)['files']
    allowed_views = {'domains/high-speed-rail/00_pieces/'+identifier+'/README.md'
                     for identifier in read_json(PLANNER / 'pilot.json')['pieces']}
    allowed_definitions = {'domains/high-speed-rail/domain.json',
                           'domains/high-speed-rail/connector-profiles.json'}
    changed = [name for name, digest in files.items()
               if not within(custom_root, name).is_file()
               or sha256(within(custom_root, name).read_bytes()) != digest]
    unexpected = [name for name in changed if name not in allowed_views | allowed_definitions]
    if unexpected:
        raise ValueError('Retained source inputs differ from ' + snapshot_name + ': ' + ', '.join(unexpected))
    differences = {name: {'before_sha256': files[name], 'current_sha256': sha256(within(custom_root, name).read_bytes())}
                   for name in changed}
    return {'status': 'passed', 'existing_files_checked': len(files)-len((allowed_views | allowed_definitions).intersection(files)),
            'authorized_generated_readme_changes': {name: differences[name] for name in changed if name in allowed_views},
            'authorized_connector_definition_changes': {name: differences[name] for name in changed if name in allowed_definitions},
            'scope': 'Protected source resources, definitions, geometry, placements, and observations; the two generated README views are separately maintained.'}


def run(custom_root, build):
    config = read_json(PLANNER / 'pilot.json')
    pilot = load_pilot(custom_root, config['pieces'])
    resources = verify_compiled(custom_root, build, pilot['pieces'], config['domain'])
    crossing, curve = [pilot['pieces'][identifier] for identifier in config['pieces']]
    matches = find_matches(crossing, curve)
    connectors = []
    for item in pilot['pieces'].values():
        for group in item['groups']:
            connectors.append({key: group.get(key) for key in
                               ('id', 'component_id', 'profile_id', 'section_offset_m', 'source_cell',
                                'edge', 'anchor_m', 'outward_normal', 'boundary_bundle_id')}
                              | {'piece_id': item['id'],
                                 'member_port_ids': [p['id'] for p in group['members']],
                                 'members': [{key: p[key] for key in
                                              ('id', 'source_port_id', 'direction', 'endpoint_m', 'channel_id', 'cut_id', 'traffic_modes',
                                               'tangent', 'grade', 'edge')} for p in group['members']],
                                 'channels': group['channels'],
                                 'construction_network': group.get('construction_network')})
    proof = {(m['a_group_id'], m['b_group_id'], m['relative_rotation_ccw'],
              tuple(m['relative_position_m'])) for m in matches}
    expected = {('upper-end-b', 'curve-end-a', 0, (0., 64.)),
                ('upper-end-a', 'curve-end-a', 180, (0., -64.))}
    if proof != expected:
        raise ValueError('The independently specified two-piece pose contract did not pass')
    domain = custom_root / 'domains' / config['domain']
    inputs = [domain / 'domain.json', domain / 'connector-profiles.json',
              PLANNER / 'pilot.json', PLANNER / 'src/scp_planner/metadata.py',
              PLANNER / 'src/scp_planner/jsonc.py',
              PLANNER / 'src/scp_planner/_source.py',
              Path(__file__).resolve()]
    for identifier in config['pieces']:
        inputs.extend(domain / '00_pieces' / identifier / name
                      for name in ('piece.json', 'connections.json', 'connector-groups.jsonc'))
    return {
        'schema_version': 3,
        'purpose': 'Planner consumes fresh source-owned connector exports and finds pairwise occupied-tile placement candidates; not game or physical-clearance confirmation.',
        'status': 'passed', 'coverage': pilot['counts'],
        'metadata_input_sha256': {str(path): sha256(path.read_bytes()) for path in inputs},
        'metadata_validation': 'passed', 'compiled_sources': resources,
        'source_format': pilot['source_format'], 'source_exports': pilot['exports'],
        'coordinate_system': {
            'units': 'metres', 'axes': ['east', 'north', 'height'],
            'orientation': 'piece-authored 0 degrees; not a placed instance',
            'origin': 'centre of source cell [0,0]; height measured from the source datum',
            'source_cell_order': '[column east, row south], counted from zero; 16 metres per tile',
            'component_identity': 'piece_id plus component_id; a component is a route, not one coordinate',
        },
        'pieces': [{
            'id': item['id'], 'components': item['metadata']['components'],
            'footprint_tiles': item['piece']['footprint'], 'occupied_cells': item['cells'],
            'journeys': item['journeys'], 'forbidden_transfers': item['forbidden_transfers'],
        } for item in pilot['pieces'].values()],
        'connectors': connectors, 'candidate_placements': matches,
        'custom_23m_end_to_crossing': 'no matching height',
        'original_selected_piece_inputs': check_preserved_inputs(custom_root),
        'jsonc_migration_retained_sources': check_preserved_inputs(custom_root, 'jsonc-migration-source-snapshot.json'),
        'checks_not_established': pilot['checks'],
        'trial_scope': 'Separate direct pair trial. The saved V4 trumpet placements are unchanged and have five upper straight pieces between these types.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--custom-pieces-root', type=Path)
    parser.add_argument('--build', type=Path)
    parser.add_argument('--report', type=Path, default=PLANNER / 'local/pilot/report.json')
    args = parser.parse_args()
    config = read_json(PLANNER / 'pilot.json')
    custom_root = (args.custom_pieces_root or (PLANNER / config['custom_pieces_root'])).resolve()
    build = (args.build or within(custom_root, config['compiled_build'])).resolve()
    destination = args.report.resolve()
    if not destination.is_relative_to((PLANNER / 'local').resolve()):
        parser.error('Generated reports must stay below scp-planner/local')
    report = run(custom_root, build)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    print('SCP Planner: two-piece metadata pilot passed.')
    print(json.dumps({'coverage': report['coverage'],
                      'candidate_placements': len(report['candidate_placements']),
                      'existing_files': report['original_selected_piece_inputs'],
                      'jsonc_migration_retained_sources': report['jsonc_migration_retained_sources'],
                      'unverified': report['checks_not_established'],
                      'report': str(destination)}, indent=2))


if __name__ == '__main__':
    main()
