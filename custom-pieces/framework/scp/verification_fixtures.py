"""Verify current built archives against a maintained resource descriptor.

The descriptor pins selected archive identities, complete bytes and resource
counts. It does not contain or copy game resources. Optional integration tests
may skip an absent build; missing source definitions and stale or malformed
present builds always fail. Physical model and traffic audits remain separate.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath, PureWindowsPath
import re

from .dbpf import decompress, entries, tgi_string
from .subject_identity import canonical_subject_id


_SHA256 = re.compile(r'[0-9a-f]{64}')
_TGI = re.compile(r'[0-9a-f]{8}-[0-9a-f]{8}-[0-9a-f]{8}')


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _identifier(value):
    return isinstance(value, str) and bool(value) and value == value.strip()


def _relative_asset(value):
    """Accept a canonical portable path, without traversal or drive aliases."""
    _require(isinstance(value, str) and value and '\\' not in value and '\0' not in value,
             'Resource asset paths must be nonempty portable relative paths')
    path = PurePosixPath(value)
    _require(not path.is_absolute() and not PureWindowsPath(value).drive
             and all(part not in ('', '.', '..') for part in value.split('/')),
             'Resource asset path escapes its root or is not canonical')
    return path


def _inside(root, relative):
    resolved = (root / _relative_asset(relative)).resolve()
    _require(resolved.is_relative_to(root), 'Resource asset path escapes its build root')
    return resolved


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        _require(key not in result, f'Duplicate JSON property: {key}')
        result[key] = value
    return result


def _read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf8'), object_pairs_hook=_unique_object)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ValueError(f'Malformed current resource JSON: {path.name}') from error


def _piece_identities(pieces, label):
    _require(isinstance(pieces, list) and pieces, f'{label} must select at least one piece')
    result, assets = {}, set()
    for piece in pieces:
        _require(isinstance(piece, dict), f'{label} piece must be an object')
        identifier, recipe = piece.get('id'), piece.get('recipe')
        _require(_identifier(identifier) and _identifier(recipe),
                 f'{label} piece requires an id and recipe')
        asset = _relative_asset(piece.get('asset_file')).as_posix()
        _require(identifier not in result, f'{label} has duplicate piece identities')
        _require(asset.casefold() not in assets, f'{label} has duplicate asset paths')
        result[identifier] = (recipe, asset)
        assets.add(asset.casefold())
    return result


def _current_piece_identities(pieces, label, root):
    """Compare declared aliases without rewriting a descriptor or its assets."""
    identities = {}
    for identifier, value in _piece_identities(pieces, label).items():
        current = canonical_subject_id(identifier, root=root)
        _require(current not in identities, f'{label} has duplicate piece identities after declared aliases')
        identities[current] = value
    return identities


def resource_descriptor(descriptor_path):
    """Read an explicit maintained schema-3 descriptor; source errors never skip.

    Required top-level fields are schema_version, id, assembly_id and pieces.
    Each piece records id, recipe, asset_file, bytes, sha256 and resource_count.
    Optional resource_sha256 maps every lowercase TGI to the SHA-256 of its
    decompressed bytes. Other top-level audit metadata is left to its owner.
    """
    path = Path(descriptor_path)
    if not path.exists():
        raise FileNotFoundError(f'Current resource descriptor is unavailable: {path}')
    _require(path.is_file(), 'Current resource descriptor is not a file')
    descriptor = _read_json(path)
    _require(isinstance(descriptor, dict) and type(descriptor.get('schema_version')) is int
             and descriptor['schema_version'] == 3,
             'Current resource descriptor has the wrong schema')
    _require(_identifier(descriptor.get('id')) and _identifier(descriptor.get('assembly_id')),
             'Current resource descriptor requires an id and assembly_id')
    _piece_identities(descriptor.get('pieces'), 'Current resource descriptor')
    for piece in descriptor['pieces']:
        _require(type(piece.get('bytes')) is int and piece['bytes'] > 0,
                 'Current resource descriptor requires a positive archive byte count')
        _require(isinstance(piece.get('sha256'), str) and _SHA256.fullmatch(piece['sha256']),
                 'Current resource descriptor requires an archive SHA-256')
        _require(type(piece.get('resource_count')) is int and piece['resource_count'] > 0,
                 'Current resource descriptor requires a positive resource count')
        if 'resource_sha256' in piece:
            resources = piece['resource_sha256']
            _require(isinstance(resources, dict) and len(resources) == piece['resource_count']
                     and all(isinstance(key, str) and _TGI.fullmatch(key)
                             and isinstance(digest, str) and _SHA256.fullmatch(digest)
                             for key, digest in resources.items()),
                     'Current resource descriptor requires exact TGI resource hashes')
    return descriptor


def verification_resources(descriptor_path, build_root, *, selected_piece_ids=None,
                           assembly_id=None, required=True, root=None):
    """Return the verified current build, or None only for an optional absent build.

    The actual manifest must select exactly the descriptor's identities, recipes
    and asset paths. Callers may independently supply the expected selected IDs
    and assembly ID so a valid descriptor for a different selection cannot pass.
    Only declared subject aliases are normalized, using the selected source
    project's migration ledger. Recipes, asset paths, archive bytes, resource
    identities, and hashes stay exact. The descriptor itself remains unchanged.
    Documentation, controller, and menu files are outside this focused contract.
    """
    descriptor = resource_descriptor(descriptor_path)
    identities = _current_piece_identities(descriptor['pieces'], 'Current resource descriptor', root)
    if assembly_id is not None:
        _require(_identifier(assembly_id)
                 and canonical_subject_id(descriptor['assembly_id'], 'assembly', root)
                 == canonical_subject_id(assembly_id, 'assembly', root),
                 'Current resource descriptor assembly identity differs')
    if selected_piece_ids is not None:
        _require(not isinstance(selected_piece_ids, (str, bytes)),
                 'Expected selected piece identities must be a collection')
        try:
            selected = list(selected_piece_ids)
        except TypeError as error:
            raise ValueError('Expected selected piece identities must be a collection') from error
        _require(all(_identifier(value) for value in selected)
                 and len(selected) == len(set(selected)),
                 'Expected selected piece identities must be unique identifiers')
        selected = [canonical_subject_id(value, root=root) for value in selected]
        _require(len(selected) == len(set(selected)),
                 'Expected selected piece identities must be unique after declared aliases')
        _require(set(selected) == set(identities), 'Current resource descriptor selected identities differ')
    requested = Path(build_root)
    _require(not (requested.is_symlink() and not requested.exists()),
             'Current verification build is a broken symbolic link')
    directory = requested.resolve()
    if not directory.exists():
        if not required:
            return None
        raise FileNotFoundError(f'Current verification build is unavailable: {directory}')
    _require(directory.is_dir(), 'Current verification build is not a directory')
    manifest_path = _inside(directory, 'manifest.json')
    _require(manifest_path.is_file(), 'Present current build is incomplete: manifest.json')
    manifest = _read_json(manifest_path)
    _require(isinstance(manifest, dict), 'Current build manifest must be an object')
    actual_identities = _current_piece_identities(manifest.get('pieces'), 'Current build manifest', root)
    _require(actual_identities == identities,
             'Current build manifest selected identity, recipe or asset path differs')
    resolved_assets = set()
    for piece in descriptor['pieces']:
        path = _inside(directory, piece['asset_file'])
        _require(path not in resolved_assets, 'Current build has duplicate resolved asset paths')
        resolved_assets.add(path)
        _require(path.is_file(), f'Present current build is incomplete: {piece["asset_file"]}')
        raw = path.read_bytes()
        _require(len(raw) == piece['bytes'] and hashlib.sha256(raw).hexdigest() == piece['sha256'],
                 f'Current resource archive bytes changed: {piece["id"]}')
        resources = entries(raw)
        indexed_count = int.from_bytes(raw[36:40], 'little')
        _require(len(resources) == indexed_count,
                 f'Current resource archive has duplicate resource identities: {piece["id"]}')
        _require(indexed_count == piece['resource_count'],
                 f'Current resource archive count differs: {piece["id"]}')
        if 'resource_sha256' in piece:
            hashes = {tgi_string(tgi): hashlib.sha256(decompress(value)).hexdigest()
                      for tgi, value in resources.items()}
            _require(hashes == piece['resource_sha256'],
                     f'Current decompressed resource hashes differ: {piece["id"]}')
    return directory
