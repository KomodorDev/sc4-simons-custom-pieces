"""Temporary connector fixtures preserve geometry without refreshing real evidence.

Renamed live definitions intentionally fail their historical source bindings.
Portable channel/profile tests need internally consistent synthetic identities,
so this helper copies selected inputs outside the library and binds only those
temporary bytes. It performs no extraction, native verification, or export of
current production evidence, and never changes a checked-in file.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil

from scp import jsonc


def _synthetic_identity(value, previous, current):
    """Rename only this fixture's logical owner labels, never measured values."""
    if isinstance(value, dict):
        return {_synthetic_identity(key, previous, current): _synthetic_identity(item, previous, current)
                for key, item in value.items()}
    if isinstance(value, list):
        return [_synthetic_identity(item, previous, current) for item in value]
    if isinstance(value, str):
        if value == previous:
            return current
        value = value.replace(':'+previous+':', ':'+current+':')
        if value.endswith(':'+previous):
            value = value[:-len(previous)]+current
    return value


def write_connector_source_fixture(destination, identifiers, *, source_root):
    """Copy named source records and bind explicitly synthetic temporary bytes."""
    root, source = Path(destination).resolve(), Path(source_root).resolve()
    if root == source or root.is_relative_to(source):
        raise ValueError('Synthetic connector fixtures must be outside the source library')
    domain = Path('domains/high-speed-rail')
    for relative in (Path('project.jsonc'), domain/'domain.jsonc', domain/'connector-profiles.jsonc'):
        target = root/relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source/relative, target)
    for identifier in identifiers:
        relative = domain/'00_pieces'/identifier
        directory = root/relative
        directory.mkdir(parents=True, exist_ok=True)
        piece = jsonc.load(source/relative/'piece.json')
        connections = jsonc.load(source/relative/'connections.json')
        groups = jsonc.load(source/relative/'connector-groups.jsonc')
        # PATH resource keys also carry the logical owner. Their unchanged
        # numeric TGIs and resource digests still drive all boundary checks.
        previous = connections['subject_id']
        connections = _synthetic_identity(connections, previous, identifier)
        groups = _synthetic_identity(groups, previous, identifier)
        piece['id'] = identifier
        connections['subject_id'] = identifier
        groups['piece_id'] = identifier
        piece['purpose'] = 'Synthetic connector regression fixture; no current native verification is claimed.'
        for name, value in (('piece.json', piece), ('connections.json', connections)):
            (directory/name).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
        groups['source_binding'] = {
            'piece_sha256': hashlib.sha256((directory/'piece.json').read_bytes()).hexdigest(),
            'connections_sha256': hashlib.sha256((directory/'connections.json').read_bytes()).hexdigest(),
        }
        (directory/'connector-groups.jsonc').write_text(
            '// Synthetic test-only bindings; no extraction or native verification was performed.\n'
            + json.dumps(groups, indent=2, allow_nan=False)+'\n')
        manual = source/relative/'checks/manual-tests.json'
        if manual.is_file():
            (directory/'checks').mkdir(exist_ok=True)
            shutil.copyfile(manual, directory/'checks/manual-tests.json')
    return root


def synthetic_export_identity(snapshot, identifier):
    """Relabel a copied export only for synthetic strict-format rejection tests."""
    value = _synthetic_identity(deepcopy(snapshot), snapshot['piece_id'], identifier)
    value['piece_id'] = identifier
    value['resolved_piece']['id'] = identifier
    value['resolved_piece']['piece']['id'] = identifier
    value['resolved_piece']['connections']['subject_id'] = identifier
    value['resolved_piece']['metadata']['piece_id'] = identifier
    # Callers that exercise content validation must recalculate this checksum
    # after their other synthetic mutations, never write it to live evidence.
    return value
