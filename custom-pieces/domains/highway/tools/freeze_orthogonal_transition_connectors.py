#!/usr/bin/env python3
"""Freeze numeric lane facts only after a complete saved adapter verifies."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.catalog import load_catalog, safe_relative
from scp.connectivity import piece_connectivity
from scp.dbpf import require
from scp.verify import strict_dbpf, verify_build
from scp_highway.connections import service_classifier
from scp_highway.orthogonal_approaches import PIECE_ID
from scp_highway.orthogonal_transition_contracts import REFERENCE
from scp_highway.orthogonal_transition_verify import reviewed_contract, reviewed_facts

HEADER = '''// title: "Accepted six-tile DD-to-ground connector measurements"
// summary: "Bind independent lane measurements to a checked native package without storing proprietary resource payloads."
//
// Used when: The six-tile adapter is extracted, validated, exported, or shown with connection cards.
// Read by: scp_highway.orthogonal_transition_contracts and the shared connector workflow.
// Updated by: domains/highway/tools/freeze_orthogonal_transition_connectors.py after saved native verification passes.
// Affects: Eight directional ports, four lane journeys, twelve forbidden transfers, and all twelve canonical PATH identities.
'''


def freeze(build, root=ROOT):
    root, build = Path(root).resolve(), Path(build).resolve()
    require(build.is_relative_to(root), 'Connector freeze build must be inside the library')
    manifest_raw = (build / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_raw)
    piece = next(p for p in load_catalog(root)['pieces'] if p['id'] == PIECE_ID)
    built = next(p for p in manifest['pieces'] if p['id'] == PIECE_ID)
    require(all(piece[k] == built[k] for k in piece if k not in {'asset_file', 'purpose', 'design_review'}),
            'Saved transition definition differs from current authoritative source')
    verify_build(build, write_report=False)
    resources = strict_dbpf(safe_relative(build, built['asset_file']).read_bytes())
    facts = reviewed_facts(piece)
    record = piece_connectivity(piece, resources, contract=reviewed_contract(piece),
                                service_classifier=service_classifier)
    actual = {p['id']: p for p in record['ports']}
    require(len(record['ports']) == len(actual) == 8
            and len(record['journeys']) == 4 and len(record['forbidden_transfers']) == 12,
            'Saved transition extraction has an incomplete directional boundary')
    for expected in facts['ports']:
        measured = actual[expected['id']]
        for key in ('direction', 'engine_transport', 'edge', 'endpoint_m', 'sampled_tangent',
                    'tangent', 'grade', 'service_network', 'service_family', 'variant', 'role',
                    'channel_kind', 'traffic_modes'):
            require(json.dumps(measured[key]) == json.dumps(expected[key]),
                    'Saved transition boundary disagrees with independent ' + key)
    require({(j['entry_port'], j['exit_port']) for j in record['journeys']} == set(facts['movements']),
            'Saved transition journey changes lane or carriageway')
    require({(p['from_port'], p['to_port']) for p in record['forbidden_transfers']}
            == set(facts['forbidden_transfers']), 'Saved transition permits an unreviewed transfer')
    facts['path_hashes_by_cell'] = [[cell, hashlib.sha256(resources[
        0x296678F7, 0xA966883F, int(tile, 16)]).hexdigest()]
        for cell, tile in zip(piece['cells'], piece['tile_ids'])]
    facts['raw_path_fingerprint_status'] = 'accepted-checked-saved-build'
    evidence = {'schema_version': 1, 'state': 'accepted-independently-checked-saved-resources',
        'game_operation': 'unverified',
        'source': {'build': build.relative_to(root).as_posix(),
                   'manifest_sha256': hashlib.sha256(manifest_raw).hexdigest(),
                   'verification_passed': True}, 'contract': facts}
    destination = root / REFERENCE
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(HEADER + json.dumps(evidence, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return {'piece_id': PIECE_ID, 'source': REFERENCE, 'ports': 8, 'journeys': 4,
            'forbidden_transfers': 12, 'canonical_path_hashes': 12, 'game_operation': 'unverified'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('build', type=Path)
    print(json.dumps(freeze(parser.parse_args().build), indent=2))
