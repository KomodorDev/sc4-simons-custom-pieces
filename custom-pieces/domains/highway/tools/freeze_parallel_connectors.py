#!/usr/bin/env python3
"""Accept checked saved parallel-diamond connector facts through SCP extraction.

Run before ordinary highway materialization. The command verifies the saved
package and complete assembly, then uses the shared extractor with independent
approved-source port labels. It never copies game-resource payloads into Git.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]
_bootstrap_spec = importlib.util.spec_from_file_location(
    '_parallel_connector_source_packages', ROOT / 'framework/scp/check_bootstrap.py')
_bootstrap = importlib.util.module_from_spec(_bootstrap_spec)
_bootstrap_spec.loader.exec_module(_bootstrap)
sys.meta_path.insert(0, _bootstrap.SourcePackages(ROOT))

from scp import jsonc
from scp.catalog import load_catalog, safe_relative
from scp.connectivity import PATH, _routes, assembly_connectivity, piece_connectivity
from scp.dbpf import require
from scp.subject_sources import source_path
from scp.verify import parse_paths, strict_dbpf, verify_build
from scp_highway.connections import service_classifier
from scp_highway.parallel_connector_contracts import PREFIX, REFERENCE
from scp_highway.parallel_verify import (APPROVAL_SHA256, HIGHWAY_SLIP_PROFILE, PARTITIONS, _source_origin,
    expected_cell_routes, reviewed_contract, verify_assembly)

ASSEMBLY = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond'
# Literal reviewed counts: the lower access now crosses one extra existing
# owner on either end. Those two joins add four intrinsic boundary ports,
# without changing any external native channel or complete assembly journey.
REVIEWED_COUNTS = {None: (176, 92, 20, 14, 78),
                   HIGHWAY_SLIP_PROFILE: (180, 94, 20, 14, 80)}
PORT_FIELDS = ('id', 'direction', 'engine_transport', 'edge', 'endpoint_m',
               'sampled_tangent', 'tangent', 'grade', 'service_network',
               'service_family', 'variant', 'role', 'channel_kind', 'traffic_modes')
HEADER = ('// title: "Accepted parallel diamond connector measurements"\n'
          '// summary: "Freeze complete service boundaries and physical channel associations after independent saved-resource checks."\n//\n'
          '// Used when: The parallel diamond components are extracted, validated, exported, or shown with connection cards.\n'
          '// Read by: scp_highway.parallel_connector_contracts and the existing shared highway connector pipeline.\n'
          '// Updated by: domains/highway/tools/freeze_parallel_connectors.py after package, PATH, model, and assembly checks pass.\n'
          '// Affects: All fifteen parallel diamond types, every exposed service boundary, signed travel grade, intrinsic journey, forbidden transfer, and derived connector output.\n')


def _hash(raw):
    return hashlib.sha256(raw).hexdigest()


def _reuse_accepted_checks(root, build, manifest_raw, manifest, scene_path):
    """Reuse native proofs only for an unchanged, already accepted resource set.

    A connector-label or tangent metadata correction must still re-extract the
    actual resources. It need not repeat unchanged native model proofs. Every
    payload, the complete manifest, the scene, and the independent measurement
    and verification sources must retain their accepted exact fingerprints.
    """
    prior_raw = (root / REFERENCE).read_bytes()
    prior = jsonc.loads(prior_raw.decode('utf-8'))
    from scp_highway.parallel_connector_contracts import load_contracts
    accepted = load_contracts(root)
    require(prior['source']['manifest_sha256'] == _hash(manifest_raw)
            and prior['source']['assembly_source_sha256'] == _hash(scene_path.read_bytes())
            and prior['source']['approval_sha256'] == APPROVAL_SHA256,
            'Accepted resource checks cannot be reused for a changed manifest, scene, or approval')
    for name in ('framework/scp/connectivity.py', 'domains/highway/implementation/scp_highway/parallel_verify.py'):
        require(prior['source']['source_sha256'][name] == _hash((root / name).read_bytes()),
                'Accepted resource checks cannot be reused after measurement or verifier code changes')
    for record in manifest['files']:
        raw = safe_relative(build, record['path']).read_bytes()
        require(len(raw) == record['bytes'] and _hash(raw) == record['sha256'],
                'Accepted resource checks cannot be reused for changed package bytes')
    verification = prior['verification']
    require(verification['package'] == 'passed'
            and verification['all_fifteen_saved_path_and_model_checks'] == 'passed'
            and verification['assembly'] == 'passed'
            and verification['native_wheeltrack_seam_uv']['passed'],
            'Prior native resource checks did not pass completely')
    piece_reports = {facts['reference_piece_id']: deepcopy(facts['saved_checks']) for facts in accepted.values()}
    assembly_report = {'saved_resource_checks_passed': True, 'saved_path_checks_passed': True,
        'saved_ownership_checks_passed': True,
        'package_construction_checks': verification['assembly_resources_only_package_construction_status'],
        'native_wheeltrack_seam_uv': deepcopy(verification['native_wheeltrack_seam_uv'])}
    return piece_reports, assembly_report, _hash(prior_raw)


def _full_saved_chord_check(piece, resources, measured):
    """Bound reviewed source-chord directions against every actual 9-digit cut.

    Each encoded coordinate is rounded to 1e-9 m. Subtracting two rounded
    endpoints gives at most 1e-9 m error per horizontal axis. The extra 1e-12 m
    covers floating-point subtraction. Unit-vector perturbation is bounded by
    2e/(L-e), where e is that two-axis error norm and L is the saved chord length.
    """
    routes = {route['id']: route for route in _routes(piece, resources)}
    parsed = {tile: parse_paths(resources[*PATH, int(tile, 16)])['routes'] for tile in piece['tile_ids']}
    controls = []
    error_norm = math.sqrt(2.) * (1e-9 + 1e-12)
    for port in measured['ports']:
        for name in port['source_route_ids']:
            route = routes[name]
            points = parsed[route['tile_id']][route['source_route_index']]['points']
            first, last = points[:2] if port['direction'] == 'in' else points[-2:]
            delta = [last[axis] - first[axis] for axis in (0, 1)]
            length = math.hypot(*delta)
            require(length > error_norm, 'A saved boundary chord is too short for its encoding precision')
            saved = [value / length for value in delta]
            difference = math.dist(saved, port['tangent'])
            bound = 2. * error_norm / (length - error_norm)
            require(difference <= bound, 'Reviewed source tangent exceeds the actual saved chord quantization bound')
            controls.append({'port_id': port['id'], 'source_route_id': name,
                'full_saved_chord_length_m': length, 'reviewed_vector_error': difference,
                'quantization_error_bound': bound,
                'shared_six_decimal_sample_error': math.dist(port['sampled_tangent'], port['tangent'])})
    return {'passed': True, 'incident_saved_chords_checked': len(controls),
        'saved_coordinate_decimal_places': 9, 'shared_graph_coordinate_decimal_places': 6,
        'maximum_reviewed_vector_error': max(c['reviewed_vector_error'] for c in controls),
        'maximum_shared_sample_error': max(c['shared_six_decimal_sample_error'] for c in controls),
        'controls': controls}


def _native_channel(route):
    """Name independently measured native lanes in their fixed world frame."""
    points, transport = route['points'], route['transport']
    first, last = points[0], points[-1]
    highway = first[2] > 1.
    if highway:
        value = (first[1] - first[0] + 8.) / math.sqrt(2.)
        direction = 'positive' if last[0] + last[1] > first[0] + first[1] else 'negative'
        family = 'upper-mainline' if first[2] > 10. else 'lower-mainline'
    else:
        value = (first[0] + first[1]) / math.sqrt(2.)
        direction = 'positive' if last[1] - last[0] > first[1] - first[0] else 'negative'
        family = 'avenue-walkways' if transport == 2 else 'avenue-mainline'
    signed = ('minus-' if value < -1e-6 else 'plus-') + format(abs(value), '.5f').replace('.', '-')
    identifier = family + '-axis-' + signed + '-' + direction
    return identifier, family, {'kind': 'independent-native-lane',
        'axis': 'highway-v' if highway else 'avenue-u', 'axis_offset_m': round(value, 6),
        'travel_axis_direction': direction, 'engine_transport': transport,
        'path_height_m': first[2]}


def _channel_associations(piece, resources, measured):
    """Associate actual saved route indices with independent physical channels.

    An approved ramp may leave and re-enter several traffic owners while its
    physical model belongs to a separate functional component. The association
    therefore uses the full accepted source route, not the type's name or a
    one-route-per-piece assumption.
    """
    origin = _source_origin(piece)
    expected = expected_cell_routes(piece.get('engineering', {}).get('highway_slip_profile'))
    route_channels, descriptions = {}, {}
    for route in _routes(piece, resources):
        source = route['cell'][0] + origin[0], route['cell'][1] + origin[1]
        points = [(p[0] + 16. * origin[0], p[1] - 16. * origin[1], p[2]) for p in route['points']]
        matches = [wanted for wanted in expected[source]
            if wanted['transport'] == route['engine_transport'] and len(wanted['points']) == len(points)
            and all(math.dist(a, b) <= 1.1e-6 for a, b in zip(points, wanted['points']))]
        require(len(matches) == 1, 'A saved route lacks one independently approved channel association')
        wanted = matches[0]
        if 'approved_ramp' in wanted:
            identifier = 'access-' + wanted['approved_ramp']
            family = 'access-network-' + wanted['approved_ramp']
            description = {'kind': 'approved-access-ramp', 'approved_ramp_id': wanted['approved_ramp'],
                'physical_model_and_traffic_ownership_are_separate': True,
                'complete_approved_route_sections': ['flat-high-departure', 'straight-parallel-descent', 'ground-right-quarter-turn'],
                'source': 'Independent approved-source ramp polyline, checked against actual saved PATH fragments'}
        else:
            identifier, family, description = _native_channel(wanted)
        route_channels[route['id']] = identifier, family
        descriptions[identifier] = description
    port_channels, families = {}, {}
    for port in measured['ports']:
        candidates = {route_channels[name] for name in port['source_route_ids']}
        # At a ramp transfer's shared native-lane endpoint, the physical cut is
        # still the original native lane. The distinct ramp cut stays separate.
        native = [pair for pair in candidates if descriptions[pair[0]]['kind'] == 'independent-native-lane']
        chosen = native if native else list(candidates)
        require(len(chosen) == 1, 'A boundary port has ambiguous physical-channel ownership')
        port_channels[port['id']], families[chosen[0][0]] = chosen[0][0], chosen[0][1]
    # Components retain independent networks except where an actual permitted
    # intrinsic journey joins the mainline and its access channel.
    parents = {family: family for family in families.values()}
    def find(family):
        while parents[family] != family:
            family = parents[family]
        return family
    for journey in measured['journeys']:
        first, last = (families[port_channels[journey[key]]] for key in ('entry_port', 'exit_port'))
        a, b = find(first), find(last)
        if a != b:
            parents[b] = a
    members = defaultdict(list)
    for family in parents:
        members[find(family)].append(family)
    component_ids = {}
    priority = ('avenue-mainline', 'lower-mainline', 'upper-mainline', 'avenue-walkways')
    for root, names in members.items():
        component_ids[root] = next((name for name in priority if name in names), sorted(names)[0])
    components, channels, sources = {}, [], []
    for identifier in sorted(families):
        family = families[identifier]
        component = component_ids[find(family)]
        ports = sorted(name for name, channel in port_channels.items() if channel == identifier)
        first = next(p for p in measured['ports'] if p['id'] == ports[0])
        pedestrian = first['engine_transport'] == 2
        components[component] = {'id': component, 'network': 'pedestrian' if pedestrian else 'road',
            'construction_network': 'avenue' if component.startswith('avenue') else 'dirtroad'}
        channels.append({'id': identifier, 'component_id': component,
            'kind': 'walkway' if pedestrian else 'road-lane',
            'traffic_modes': ['pedestrian'] if pedestrian else ['car'], 'ports': ports})
        sources.append({'channel_id': identifier, **descriptions[identifier]})
    return port_channels, list(components.values()), channels, sources


def freeze(root, build, *, reuse_accepted_resource_checks=False):
    root, build = Path(root).resolve(), Path(build).resolve()
    require(build.is_relative_to(root), 'The saved build must be inside the selected library')
    catalog = load_catalog(root)
    pieces = {p['id']: p for p in catalog['pieces'] if p['recipe'].startswith(PREFIX)}
    require(len(pieces) == len(PARTITIONS) == 15, 'Freeze requires all fifteen registered parallel types')
    profiles = {piece.get('engineering', {}).get('highway_slip_profile') for piece in pieces.values()}
    require(len(profiles) == 1, 'Freeze requires one coordinated highway slip profile')
    highway_slip_profile = next(iter(profiles))
    require(highway_slip_profile in REVIEWED_COUNTS, 'Freeze requires a reviewed highway slip profile')
    intrinsic_ports, intrinsic_journeys, outer_ports, complete_journeys, piece_joins = REVIEWED_COUNTS[highway_slip_profile]
    manifest_raw = (build / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_raw)
    built = {p['id']: p for p in manifest['pieces']}
    require(pieces.keys() <= built.keys(), 'The saved build does not contain every parallel component')
    scene_path = source_path(root / 'domains/highway/01_assemblies' / ASSEMBLY, 'assembly')
    scene = jsonc.load(scene_path)
    prior_acceptance_sha256 = None
    if reuse_accepted_resource_checks:
        piece_reports, assembly_report, prior_acceptance_sha256 = _reuse_accepted_checks(
            root, build, manifest_raw, manifest, scene_path)
    else:
        package_report = verify_build(build, write_report=False)
        require(package_report['static_checks_passed'], 'Independent saved package verification did not pass')
        piece_reports = {row['id']: row for row in package_report['pieces']}
        assembly_report = verify_assembly(build, scene, verify_package=False)
    require(assembly_report['saved_resource_checks_passed']
            and assembly_report['saved_path_checks_passed']
            and assembly_report['saved_ownership_checks_passed']
            and assembly_report['native_wheeltrack_seam_uv']['passed'],
            'Independent saved assembly model and PATH verification did not pass')
    contracts, asset_hashes, summary, measured_records = {}, {}, [], {}
    for identifier, piece in sorted(pieces.items()):
        comparable = lambda p: {key: value for key, value in p.items()
            if key not in {'asset_file', 'purpose', 'design_review'}}
        require(comparable(piece) == comparable(built[identifier]),
                identifier + ': saved type definition differs from current authoring source')
        asset = built[identifier]['asset_file']
        raw = safe_relative(build, asset).read_bytes()
        resources = strict_dbpf(raw)
        # The fresh package audit has already called the owning independent
        # PATH/model checks on these exact hash-verified saved DAT resources.
        path_report = piece_reports[identifier]['paths']
        model_report = piece_reports[identifier]['models']
        require(path_report['passed'] and model_report['passed'], 'Independent saved-resource checks failed')
        independent = reviewed_contract(piece)
        measured = piece_connectivity(piece, resources, contract=independent, service_classifier=service_classifier)
        # Preserve the common independently reviewed source-chord direction.
        # The separate sampled tangent retains the shared engine's deliberate
        # six-decimal graph sampling; a tiny cut chord can magnify that loss.
        full_chords = _full_saved_chord_check(piece, resources, measured)
        measured_records[identifier] = measured
        port_channels, components, channels, sources = _channel_associations(piece, resources, measured)
        ports = []
        for port in measured['ports']:
            require(len(port['boundary_sources']) == 1, 'Accepted port needs one real source boundary')
            ports.append({**{key: deepcopy(port[key]) for key in PORT_FIELDS},
                          'source_cell': port['boundary_sources'][0]['cell'],
                          'channel_id': port_channels[port['id']]})
        hashes = measured['source']['resource_fingerprints']
        facts = {'reference_piece_id': identifier, 'footprint': piece['footprint'], 'cells': piece['cells'],
            'path_hashes_by_cell': [[cell, hashes[f'path:{identifier}:296678f7-a966883f-{tile}']]
                                   for cell, tile in zip(piece['cells'], piece['tile_ids'])],
            'ports': ports,
            'movements': [[j['entry_port'], j['exit_port']] for j in measured['journeys']],
            'forbidden_transfers': [[j['from_port'], j['to_port']] for j in measured['forbidden_transfers']],
            'components': components, 'channels': channels, 'channel_sources': sources,
            'physical_ownership': {'model_owner': piece['geometry_key'],
                'physical_model_function': piece['engineering']['physical_model_function'],
                'authored_function_overhang_declared': piece['engineering']['model_overhang'],
                'native_overhang_convention': 'Retained native donor edges may also overhang occupied cells; the authored-function declaration is not the full model projection.',
                'traffic_owner': 'Every complete PATH fragment in the listed owned source cells',
                'traffic_boundary_is_not_a_physical_model_cut': True},
            'saved_checks': {'paths': path_report, 'models': model_report},
            'full_saved_chord_direction_check': full_chords}
        contracts[piece['recipe']] = facts
        asset_hashes[asset] = _hash(raw)
        summary.append({'piece_id': identifier, 'ports': len(ports), 'channels': len(channels),
                        'journeys': len(facts['movements'])})
    composed = assembly_connectivity(ASSEMBLY, scene, measured_records, pieces)
    outer_variants = {port['variant'] for port in composed['ports']}
    require((sum(len(record['ports']) for record in measured_records.values()),
             sum(len(record['journeys']) for record in measured_records.values()))
            == (intrinsic_ports, intrinsic_journeys),
            'Parallel intrinsic graph differs from the independently reviewed profile counts')
    require((len(composed['ports']), len(composed['journeys']), len(composed['encoded_route_joins']))
            == (outer_ports, complete_journeys, piece_joins) and outer_variants == {
                'dd-rhw-l1', 'dd-rhw-l2', 'avenue-ground', 'avenue-sidewalk'},
            'Shared parallel assembly graph differs from its independently reviewed profile counts')
    evidence = {'schema_version': 1, 'subject_id': ASSEMBLY,
        'state': 'accepted-independently-checked-saved-resources',
        'purpose': 'Authoritative reviewed numeric connector measurements for the exact compiled parallel diamond; no game-resource payload is retained.',
        'source': {'manifest_sha256': _hash(manifest_raw), 'asset_sha256': asset_hashes,
            'highway_slip_profile': highway_slip_profile,
            'approval_sha256': APPROVAL_SHA256, 'assembly_source_sha256': _hash(scene_path.read_bytes()),
            'measurement_engine': 'scp.connectivity.piece_connectivity',
            'independent_contract': 'scp_highway.parallel_verify.reviewed_contract',
            'source_sha256': {name: _hash((root / name).read_bytes()) for name in (
                'framework/scp/connectivity.py', 'domains/highway/implementation/scp_highway/parallel_verify.py',
                'domains/highway/tools/freeze_parallel_connectors.py')}},
        'verification': {'package': 'passed', 'all_fifteen_saved_path_and_model_checks': 'passed',
            'assembly': 'passed', 'proper_path_rotations': 4,
            'package_construction_checks': 'passed-by-separate-fresh-verify_build',
            'assembly_resource_checks': 'passed',
            'assembly_resource_invocation': 'verify_assembly(..., verify_package=False), after a separate fresh verify_build() checked actual saved controller rules.',
            'assembly_resources_only_package_construction_status': assembly_report['package_construction_checks'],
            'native_wheeltrack_seam_uv': deepcopy(assembly_report['native_wheeltrack_seam_uv']),
            'shared_assembly_graph': {'passed': True, 'external_ports': outer_ports,
                'complete_journeys': complete_journeys, 'directed_piece_joins': piece_joins,
                'external_service_variants': sorted(outer_variants),
                'internal_access_cut_ports_exposed': 0,
                'basis': 'Unchanged scp.connectivity.assembly_connectivity with independently reviewed chord tangents and actual sampled tangents retained separately'},
            'unchanged_native_resource_checks_reused': bool(reuse_accepted_resource_checks),
            'prior_accepted_resource_measurements_sha256': prior_acceptance_sha256,
            'resource_extraction': 'actual saved DAT resources through the existing shared engine'},
        'game_operation': 'unverified', 'counterpart_matching_performed': False,
        'tangent_convention': 'tangent retains the independently reviewed approved-source polyline chord; sampled_tangent retains the actual saved first/last chord after shared six-decimal graph sampling, and grade retains that sampled signed rise/run. Every reviewed tangent is separately checked against the full nine-decimal saved PATH chord with its own coordinate-quantization bound; no ideal perpendicular or new route geometry is invented.',
        'ownership_convention': 'Physical model functions and whole-cell traffic ownership differ; each source cell retains all native, pedestrian, and access PATH fragments.',
        'contracts': contracts}
    target = root / REFERENCE
    target.parent.mkdir(parents=True, exist_ok=True)
    original = target.read_text() if target.is_file() else HEADER + '{}\n'
    target.write_text(jsonc.document(evidence, source=original), encoding='utf-8')
    return {'accepted_measurements': REFERENCE, 'manifest_sha256': _hash(manifest_raw),
            'pieces': summary, 'manual_observations_changed': False, 'resource_payloads_published': False}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--reuse-accepted-resource-checks', action='store_true',
        help='Reuse prior native proofs only when all accepted package bytes and verification inputs remain exactly unchanged; re-extract connector facts.')
    args = parser.parse_args()
    print(json.dumps(freeze(args.root, args.build,
                           reuse_accepted_resource_checks=args.reuse_accepted_resource_checks), indent=2))
