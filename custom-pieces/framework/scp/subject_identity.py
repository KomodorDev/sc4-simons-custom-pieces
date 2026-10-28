"""Resolve deliberately migrated subject IDs without changing recipe identities.

The migration ledger declares aliases; it never supplies current display names.
Read those names from registered manifests, and keep recipe dispatch independent
of folder spelling. This module deliberately does not import the catalogue.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import re

from . import jsonc
from .paths import project_root

_SLUG = re.compile(r'[a-z](?:[a-z0-9]|-[a-z0-9])+\Z')
_RECIPE = re.compile(r'[a-z][a-z0-9_]*\Z')
_DEFAULT_DOMAIN = 'high-speed-rail'


def _identifier(value, label='Subject identifier'):
    if not isinstance(value, str) or not 2 <= len(value) <= 64 or not _SLUG.fullmatch(value):
        raise ValueError(f'{label} must be a 2–64-character lowercase hyphenated identifier')
    return value


def _recipe(value):
    if not isinstance(value, str) or not _RECIPE.fullmatch(value):
        raise ValueError('Recipe must be a lowercase Python-style identifier')
    return value


def _root(root):
    return Path(project_root() if root is None else root).resolve()


@lru_cache(maxsize=16)
def _read_indexes(path, modified_ns, size):
    # The file signature invalidates this small cache after a real source edit.
    # Current manifest names are deliberately never cached here.
    data = jsonc.load(Path(path))
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise ValueError('Subject ID migration ledger has an unsupported schema')
    indexes = {}
    for kind, plural in (('piece', 'pieces'), ('assembly', 'assemblies')):
        records = data.get(plural, [])
        if not isinstance(records, list):
            raise ValueError(f'Subject ID migration {plural} must be a list')
        old, new, recipes = {}, {}, {}
        for record in records:
            if not isinstance(record, dict):
                raise ValueError(f'Subject ID migration {kind} must be an object')
            previous = _identifier(record.get('old_id'), 'Previous subject identifier')
            current = _identifier(record.get('new_id'), 'Current subject identifier')
            _identifier(record.get('domain'), 'Subject domain')
            if previous in old or current in new:
                raise ValueError(f'Ambiguous {kind} identity in subject ID migration ledger')
            old[previous], new[current] = record, record
            if kind == 'piece':
                recipe = _recipe(record.get('recipe'))
                if recipe in recipes:
                    raise ValueError(f'Ambiguous recipe owner in subject ID migration ledger: {recipe}')
                recipes[recipe] = record
        if any(identifier in old and old[identifier]['new_id'] != identifier for identifier in new):
            raise ValueError(f'Ambiguous current/previous {kind} alias in subject ID migration ledger')
        indexes[kind] = old, new, recipes
    return indexes


def _indexes(root):
    path = root / 'config/subject-id-migration.jsonc'
    if not path.is_file():
        return {'piece': ({}, {}, {}), 'assembly': ({}, {}, {})}
    stat = path.stat()
    return _read_indexes(str(path), stat.st_mtime_ns, stat.st_size)


def canonical_subject_id(identifier, kind='piece', root=None):
    """Translate a declared old ID; leave current and unknown IDs unchanged."""
    identifier = _identifier(identifier)
    if kind not in ('piece', 'assembly'):
        raise ValueError('Subject kind must be piece or assembly')
    old, _, _ = _indexes(_root(root))[kind]
    return old[identifier]['new_id'] if identifier in old else identifier


def legacy_piece_id(identifier, root=None):
    """Return a declared previous piece ID for procedural styles and evidence."""
    identifier = _identifier(identifier)
    _, new, _ = _indexes(_root(root))['piece']
    return new[identifier]['old_id'] if identifier in new else identifier


def canonical_piece_id(recipe, root=None):
    """Resolve a migrated recipe owner, or retain ordinary recipe-to-slug form."""
    recipe = _recipe(recipe)
    _, _, recipes = _indexes(_root(root))['piece']
    return recipes[recipe]['new_id'] if recipe in recipes else _identifier(recipe.replace('_', '-'))


def _registered_owner(recipe, root):
    """Find the unique registered manifest using only explicit source registries."""
    project = jsonc.load(root / 'project.jsonc')
    owners = []
    for domain_id, domain in project.get('domains', {}).items():
        directory = (root / domain['path']).resolve()
        registry_path = (root / domain['registry']).resolve()
        if not directory.is_relative_to(root) or not registry_path.is_relative_to(root):
            raise ValueError('A registered domain path escapes the source project')
        registry = jsonc.load(registry_path)
        for relative in registry.get('pieces', []):
            path = (directory / relative).resolve()
            if not path.is_relative_to(directory):
                raise ValueError('A registered piece path escapes its owning domain')
            piece = jsonc.load(path)
            if piece.get('recipe') != recipe:
                continue
            if piece.get('domain') != domain_id or piece.get('id') != path.parent.name:
                raise ValueError(f'Registered piece identity disagrees with its path or domain: {recipe}')
            owners.append((path, piece))
    if len(owners) > 1:
        raise ValueError(f'Ambiguous registered recipe owner: {recipe}')
    return owners[0] if owners else None


def canonical_piece_name(recipe, fallback, root=None):
    """Read the current registered name; ledger names remain historical records."""
    recipe, root = _recipe(recipe), _root(root)
    owner = _registered_owner(recipe, root)
    if owner is None:
        return fallback
    name = owner[1].get('name')
    if not isinstance(name, str) or not name.strip():
        raise ValueError(f'Registered piece requires a nonempty current name: {recipe}')
    return name


def piece_directory(recipe, root=None):
    """Locate maintained geometry beside its recipe's registered piece manifest."""
    recipe, root = _recipe(recipe), _root(root)
    _, _, recipes = _indexes(root)['piece']
    if recipe in recipes:
        record = recipes[recipe]
        return root / 'domains' / record['domain'] / '00_pieces' / record['new_id']
    owner = _registered_owner(recipe, root)
    if owner is not None:
        return owner[0].parent
    return root / 'domains' / _DEFAULT_DOMAIN / '00_pieces' / canonical_piece_id(recipe, root)
