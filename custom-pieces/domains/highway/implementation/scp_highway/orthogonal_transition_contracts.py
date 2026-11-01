"""Load accepted numeric connector measurements for the six-tile adapter."""
from copy import deepcopy
from pathlib import Path
import re

from scp import jsonc
from scp.dbpf import require
from .orthogonal_approaches import PIECE_ID

ROOT = Path(__file__).resolve().parents[4]
REFERENCE = f'domains/highway/00_pieces/{PIECE_ID}/checks/accepted-connector-contract.jsonc'


def load_contract(piece, root=ROOT):
    path = Path(root) / REFERENCE
    if not path.is_file():
        return None
    evidence = jsonc.load(path)
    source = evidence.get('source')
    require(isinstance(source, dict) and source.get('verification_passed') is True
            and isinstance(source.get('manifest_sha256'), str),
            'Transition connector evidence lacks a passed saved-resource verification source')
    require(type(evidence.get('schema_version')) is int and evidence['schema_version'] == 1
            and evidence.get('state') == 'accepted-independently-checked-saved-resources'
            and evidence.get('game_operation') == 'unverified'
            and re.fullmatch('[0-9a-f]{64}', source['manifest_sha256']),
            'Transition connector evidence lacks an accepted saved-resource identity')
    facts = deepcopy(evidence['contract'])
    from .orthogonal_transition_verify import reviewed_facts
    expected = reviewed_facts(piece)
    hashes = facts.pop('path_hashes_by_cell', None)
    facts.pop('raw_path_fingerprint_status', None)
    expected.pop('path_hashes_by_cell')
    expected.pop('raw_path_fingerprint_status', None)
    # JSON arrays represent the same numeric tuples used by the verifier.
    import json
    require(json.dumps(facts, sort_keys=True) == json.dumps(expected, sort_keys=True),
            'Accepted transition connector semantics differ from the independent review')
    require(isinstance(hashes, list) and len(hashes) == len(piece['cells'])
            and all(isinstance(row, list) and len(row) == 2
                    and isinstance(row[0], list) and len(row[0]) == 2
                    and all(type(value) is int for value in row[0])
                    and isinstance(row[1], str) and re.fullmatch('[0-9a-f]{64}', row[1])
                    for row in hashes),
            'Accepted transition PATH hashes require exact integer cells and lowercase SHA256 strings')
    require(len({tuple(cell) for cell, _digest in hashes}) == len(hashes)
            and {tuple(cell) for cell, _digest in hashes} == set(map(tuple, piece['cells'])),
            'Accepted transition PATH hashes must cover every owned cell exactly once')
    for key in ('movements', 'forbidden_transfers'):
        facts[key] = [tuple(pair) for pair in facts[key]]
    return {**facts, 'path_hashes_by_cell': hashes,
            'raw_path_fingerprint_status': 'accepted-checked-saved-build'}
