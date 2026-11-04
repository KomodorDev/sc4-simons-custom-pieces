"""Read independently checked saved connector contracts for the DD RHW Y."""
from copy import deepcopy
import json
from pathlib import Path
import re

from scp import jsonc
from scp.dbpf import require
from .y_junction_variants import ORIGINAL, REVERSED, identities_for, variant_for_id, variant_of

ROOT = Path(__file__).resolve().parents[4]
IDENTITIES = ('ddrhw-y-diagonal-stem-split', 'ddrhw-y-diagonal-branch', 'ddrhw-y-orthogonal-core')
REVERSED_IDENTITIES = tuple(identities_for(REVERSED))


def reference(piece):
    variant_for_id(piece['id'])
    return f'domains/highway/00_pieces/{piece["id"]}/checks/accepted-connector-contract.jsonc'


def load_contract(piece, root=ROOT):
    path = Path(root)/reference(piece)
    if not path.is_file():
        return None
    value = jsonc.load(path)
    source = value.get('source', {})
    require(value.get('schema_version') == 1
            and value.get('state') == 'accepted-independently-checked-saved-resources'
            and value.get('game_operation') == 'unverified'
            and source.get('verification_passed') is True
            and source.get('whole_assembly_checked') is True
            and source.get('whole_assembly_physical_models_checked') is True
            and re.fullmatch('[0-9a-f]{64}', source.get('manifest_sha256', '')),
            'Y connector evidence requires a checked saved-build identity')
    facts = deepcopy(value['contract'])
    if variant_of(piece) == REVERSED:
        from .y_junction_reversed_verify import reviewed_facts
    else:
        from .y_junction_verify import reviewed_facts
    expected = reviewed_facts(piece)
    hashes = facts.pop('path_hashes_by_cell', None)
    facts.pop('raw_path_fingerprint_status', None)
    expected.pop('path_hashes_by_cell', None)
    expected.pop('raw_path_fingerprint_status', None)
    require(json.dumps(facts, sort_keys=True) == json.dumps(expected, sort_keys=True),
            'Saved Y connector semantics differ from independent source expectations')
    require(isinstance(hashes, list) and len(hashes) == len(piece['cells'])
            and all(isinstance(row, list) and len(row) == 2 and isinstance(row[0], list)
                    and len(row[0]) == 2 and all(type(v) is int for v in row[0])
                    and isinstance(row[1], str) and re.fullmatch('[0-9a-f]{64}', row[1])
                    for row in hashes)
            and len({tuple(cell) for cell, _ in hashes}) == len(hashes)
            and {tuple(cell) for cell, _ in hashes} == set(map(tuple, piece['cells'])),
            'Y saved PATH fingerprints must cover all owned cells exactly once')
    for key in ('movements', 'forbidden_transfers'):
        facts[key] = [tuple(pair) for pair in facts[key]]
    return {**facts, 'path_hashes_by_cell': hashes,
            'raw_path_fingerprint_status': 'accepted-checked-saved-build'}
