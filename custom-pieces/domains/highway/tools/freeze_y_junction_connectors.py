#!/usr/bin/env python3
"""Freeze Y component boundary facts after the complete native build verifies."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.catalog import load_catalog, safe_relative
from scp.connectivity import piece_connectivity
from scp.dbpf import require
from scp.verify import strict_dbpf, verify_build, load_local_donors
from scp_highway.connections import service_classifier
from scp_highway.y_junction_contracts import IDENTITIES, reference
from scp_highway.y_junction_verify import reviewed_contract, reviewed_facts, check_assembly
from scp_highway.y_junction_models_verify import check_models_assembly
from scp_highway.y_junction_variants import ORIGINAL, REVERSED, VARIANTS, identities_for, assembly_for

HEADER = '''// title: "Checked DD RHW Y component connector measurements"
// summary: "Bind complete intrinsic lane boundaries to independently verified saved component and assembly resources."
//
// Used when: Extracting, validating, exporting, or drawing connector cards for this Y component.
// Read by: scp_highway.y_junction_contracts and the shared connector workflow.
// Updated by: domains/highway/tools/freeze_y_junction_connectors.py after the complete native build verifies.
// Affects: This component's directional ports, permitted journeys, forbidden transfers, and complete canonical PATH identities; game observations remain unverified.
'''


def freeze(build, root=ROOT, *, variant=ORIGINAL):
    root, build = Path(root).resolve(), Path(build).resolve()
    require(build.is_relative_to(root), 'Y connector freeze requires a build inside the library')
    raw = (build/'manifest.json').read_bytes()
    manifest = json.loads(raw)
    catalog = load_catalog(root)
    identifiers = tuple(identities_for(variant))
    if variant == REVERSED:
        from scp_highway.y_junction_reversed_verify import reviewed_contract as selected_contract
        from scp_highway.y_junction_reversed_verify import reviewed_facts as selected_facts
        from scp_highway.y_junction_reversed_verify import check_assembly as selected_assembly
        from scp_highway.y_junction_reversed_models_verify import check_models_assembly as selected_models
    else:
        selected_contract, selected_facts = reviewed_contract, reviewed_facts
        selected_assembly, selected_models = check_assembly, check_models_assembly
    known = {p['id']: p for p in catalog['pieces']}
    built = {p['id']: p for p in manifest['pieces']}
    require(set(identifiers) <= built.keys(), 'The complete selected three-component Y variant is required')
    verify_build(build, write_report=False)
    pieces = [known[identifier] for identifier in identifiers]
    archives = {}
    for piece in pieces:
        actual = built[piece['id']]
        require(all(piece[key] == actual[key] for key in piece if key not in {'purpose', 'asset_file', 'design_review'}),
                'Saved Y component differs from current source')
        archives[piece['id']] = strict_dbpf(safe_relative(build, actual['asset_file']).read_bytes())
    scene = jsonc.load(root/'domains/highway/01_assemblies'/assembly_for(variant)/'assembly.jsonc')
    donors, _donor_report = load_local_donors(build, manifest)
    require(donors, 'Y connector acceptance requires the pinned native input archives')
    assembly = selected_assembly(pieces, archives, scene, donors)
    physical = selected_models(pieces, archives, donors)
    results = []
    for piece in pieces:
        resources = archives[piece['id']]
        facts = selected_facts(piece)
        record = piece_connectivity(piece, resources, contract=selected_contract(piece),
                                    service_classifier=service_classifier)
        require({(j['entry_port'], j['exit_port']) for j in record['journeys']} == set(map(tuple, facts['movements']))
                and {(p['from_port'], p['to_port']) for p in record['forbidden_transfers']}
                    == set(map(tuple, facts['forbidden_transfers'])),
                'Saved Y component has an unreviewed intrinsic transfer')
        actual = {p['id']: p for p in record['ports']}
        require(set(actual) == {p['id'] for p in facts['ports']}, 'Saved Y boundary omits a directed lane cut')
        for expected in facts['ports']:
            measured = actual[expected['id']]
            for key in ('direction', 'engine_transport', 'edge', 'endpoint_m', 'sampled_tangent',
                        'tangent', 'grade', 'service_network', 'service_family', 'variant', 'role',
                        'channel_kind', 'traffic_modes'):
                if key in ('endpoint_m', 'sampled_tangent', 'tangent'):
                    # Match the existing highway public-record validation:
                    # endpoints use the micrometre graph representation,
                    # while unit-vector normalization has floating-point rounding.
                    tolerance = 1e-6 if key == 'endpoint_m' else 1e-9
                    agrees = (len(measured[key]) == len(expected[key]) and
                              all(math.isfinite(value) for value in (*measured[key], *expected[key])) and
                              math.dist(measured[key], expected[key]) <= tolerance)
                elif key == 'grade':
                    agrees = (math.isfinite(measured[key]) and math.isfinite(expected[key]) and
                              abs(measured[key]-expected[key]) <= 1e-9)
                else:
                    agrees = json.dumps(measured[key]) == json.dumps(expected[key])
                require(agrees,
                        'Saved Y boundary differs from independent '+key)
        facts['path_hashes_by_cell'] = [[cell, hashlib.sha256(resources[
            0x296678F7, 0xA966883F, int(tile, 16)]).hexdigest()]
            for cell, tile in zip(piece['cells'], piece['tile_ids'])]
        facts['raw_path_fingerprint_status'] = 'accepted-checked-saved-build'
        evidence = {'schema_version': 1, 'state': 'accepted-independently-checked-saved-resources',
                    'game_operation': 'unverified', 'source': {
                        'build': build.relative_to(root).as_posix(),
                        'manifest_sha256': hashlib.sha256(raw).hexdigest(),
                        'verification_passed': True, 'whole_assembly_checked': True,
                        'whole_assembly_physical_models_checked': True}, 'contract': facts}
        destination = root/reference(piece)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            destination.write_text(HEADER, encoding='utf-8')
        jsonc.dump(destination, evidence)
        results.append({'piece_id': piece['id'], 'ports': len(facts['ports']),
                        'journeys': len(facts['movements']), 'path_hashes': len(piece['cells'])})
    return {'variant': variant, 'components': results, 'assembly': assembly, 'physical_models': physical,
            'game_operation': 'unverified'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('build', type=Path)
    parser.add_argument('--variant', choices=VARIANTS, default=ORIGINAL)
    args = parser.parse_args()
    print(json.dumps(freeze(args.build, variant=args.variant), indent=2))
