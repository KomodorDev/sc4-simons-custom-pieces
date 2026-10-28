"""Find current piece sources by their explicit recipe registrations.

Recipe keys select implementation code; registered IDs, display names, and
folders come directly from the maintained project and domain manifests.
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


def _identifier(value):
    if not isinstance(value, str) or not 2 <= len(value) <= 64 or not _SLUG.fullmatch(value):
        raise ValueError('Piece identifier must be a 2–64-character lowercase hyphenated identifier')
    return value


def _recipe(value):
    if not isinstance(value, str) or not _RECIPE.fullmatch(value):
        raise ValueError('Recipe must be a lowercase Python-style identifier')
    return value


def _root(root):
    return Path(project_root() if root is None else root).resolve()


@lru_cache(maxsize=512)
def _manifest(path, modified_ns, size):
    # A source edit changes the signature, so names and recipe owners stay current.
    return jsonc.load(Path(path))


def _registered_owner(recipe, root):
    """Find the unique registered owner without importing recipe implementations."""
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
            stat = path.stat()
            piece = _manifest(str(path), stat.st_mtime_ns, stat.st_size)
            if piece.get('recipe') != recipe:
                continue
            identifier = _identifier(piece.get('id'))
            if piece.get('domain') != domain_id or identifier != path.parent.name:
                raise ValueError(f'Registered piece identity disagrees with its path or domain: {recipe}')
            owners.append((path, piece))
    if len(owners) > 1:
        raise ValueError(f'Ambiguous registered recipe owner: {recipe}')
    return owners[0] if owners else None


def piece_id_for_recipe(recipe, root=None):
    """Read the registered ID, or propose a slug for an unregistered recipe."""
    recipe, root = _recipe(recipe), _root(root)
    owner = _registered_owner(recipe, root)
    return owner[1]['id'] if owner is not None else _identifier(recipe.replace('_', '-'))


def piece_name_for_recipe(recipe, fallback, root=None):
    """Read the registered display name; new recipes use their supplied name."""
    recipe, root = _recipe(recipe), _root(root)
    owner = _registered_owner(recipe, root)
    if owner is None:
        return fallback
    name = owner[1].get('name')
    if not isinstance(name, str) or not name.strip():
        raise ValueError(f'Registered piece requires a nonempty current name: {recipe}')
    return name


def piece_directory(recipe, root=None):
    """Locate the registered source folder, or the prospective scaffold folder."""
    recipe, root = _recipe(recipe), _root(root)
    owner = _registered_owner(recipe, root)
    if owner is not None:
        return owner[0].parent
    return root / 'domains' / _DEFAULT_DOMAIN / '00_pieces' / _identifier(recipe.replace('_', '-'))
