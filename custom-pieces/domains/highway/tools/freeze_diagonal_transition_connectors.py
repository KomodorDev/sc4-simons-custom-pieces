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
from scp_highway.diagonal_transition_variants import PIECE_ID, PIECE_IDS, variant_of
from scp_highway.diagonal_transition_verify import reviewed_contract, reviewed_facts

HEADER = '''// title: "Accepted first-cut diagonal DD-to-ground connector measurements"
// summary: "Bind independent lane measurements to a checked native package without storing proprietary resource payloads."
//
// Used when: The selected first-cut diagonal adapter is extracted, validated, exported, or shown with connection cards.
// Read by: scp_highway.diagonal_transition_contracts and the shared connector workflow.
// Updated by: domains/highway/tools/freeze_diagonal_transition_connectors.py after saved native verification passes.
// Affects: Eight directional ports, four lane journeys, twelve forbidden transfers, and every owned canonical PATH identity.
'''


def _prepare(root, build, manifest, manifest_raw, piece):
    piece_id = piece['id']
    built = next(p for p in manifest['pieces'] if p['id'] == piece_id)
    variant_of(piece)
    require(all(piece[k] == built[k] for k in piece if k not in {'asset_file', 'purpose', 'design_review'}),
            'Saved diagonal definition differs from current authoritative source')
    raw = safe_relative(build, built['asset_file']).read_bytes()
    file_record = next(item for item in manifest['files'] if item['path'] == built['asset_file'])
    require(hashlib.sha256(raw).hexdigest() == file_record['sha256'],
            'Saved diagonal DAT changed after native verification')
    resources = strict_dbpf(raw)
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
        'game_operation': 'unverified', 'subject_id': piece_id, 'alignment': 'a',
        'source': {'build': build.relative_to(root).as_posix(),
                   'manifest_sha256': hashlib.sha256(manifest_raw).hexdigest(),
                   'verification_passed': True}, 'contract': facts}
    reference = f'domains/highway/00_pieces/{piece_id}/checks/accepted-connector-contract.jsonc'
    destination = root / reference
    summary = {'piece_id': piece_id, 'source': reference, 'ports': 8, 'journeys': 4,
               'forbidden_transfers': 12, 'canonical_path_hashes': len(piece['cells']),
               'game_operation': 'unverified'}
    return destination, HEADER + json.dumps(evidence, indent=2, ensure_ascii=False) + '\n', summary


def freeze_many(build, root=ROOT, *, piece_ids=None):
    """Verify the complete saved selection once, then prepare all selected facts."""
    root, build = Path(root).resolve(), Path(build).resolve()
    selected = list(PIECE_IDS) if piece_ids is None else list(piece_ids)
    require(selected and len(set(selected)) == len(selected)
            and all(identifier in PIECE_IDS for identifier in selected),
            'Connector freeze requires unique exact first-cut diagonal identities')
    require(build.is_relative_to(root), 'Connector freeze build must be inside the library')
    manifest_raw = (build / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_raw)
    catalog = {piece['id']: piece for piece in load_catalog(root)['pieces']}
    require(all(identifier in catalog and any(row['id'] == identifier for row in manifest['pieces'])
                for identifier in selected), 'Every selected diagonal type must be registered and saved')
    verify_build(build, write_report=False)
    require((build / 'manifest.json').read_bytes() == manifest_raw,
            'Saved manifest changed during native verification')
    prepared = [_prepare(root, build, manifest, manifest_raw, catalog[identifier])
                for identifier in selected]
    for destination, raw, _summary in prepared:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(raw, encoding='utf-8')
    return [summary for _destination, _raw, summary in prepared]


def freeze(build, root=ROOT, *, piece_id=PIECE_ID):
    return freeze_many(build, root=root, piece_ids=[piece_id])[0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('build', type=Path)
    parser.add_argument('--piece', choices=PIECE_IDS, action='append', dest='piece_ids',
                        help='Repeat for selected first-cut owners; the default is all four')
    args = parser.parse_args()
    print(json.dumps(freeze_many(args.build, piece_ids=args.piece_ids), indent=2))
