"""Find current piece sources by their explicit recipe registrations.

Recipe keys select implementation code; registered IDs, display names, and
folders come directly from the maintained project and domain manifests.
"""
from __future__ import annotations

from functools import lru_cache
import json
from pathlib import Path
import re

from . import jsonc
from .paths import project_root

_SLUG = re.compile(r'[a-z](?:[a-z0-9]|-[a-z0-9])+\Z')
_RECIPE = re.compile(r'[a-z][a-z0-9_]*\Z')
_DEFAULT_DOMAIN = 'high-speed-rail'


def source_path(directory, kind, *, required=True):
    """Find one maintained subject source, refusing ambiguous parallel copies.

    Existing strict-JSON subjects keep their original filename. New subjects
    use JSONC, and a registry must explicitly list the chosen extension.
    """
    if kind not in {'piece', 'assembly'}:
        raise ValueError('Subject kind must be piece or assembly')
    directory = Path(directory)
    candidates = [directory / (kind + suffix) for suffix in ('.jsonc', '.json')]
    present = [path for path in candidates if path.exists() or path.is_symlink()]
    if len(present) > 1:
        raise ValueError(f'Only one maintained {kind}.jsonc or {kind}.json source is allowed')
    if not present:
        if required:
            raise FileNotFoundError(f'Missing {kind}.jsonc or {kind}.json source: {directory}')
        return None
    path = present[0]
    if path.is_symlink() or not path.is_file():
        raise ValueError(f'Subject source must be a regular file: {path}')
    return path


def registered_source_path(directory, relative, kind, *, identifier=None):
    """Validate an explicitly registered filename and its canonical folder."""
    directory = Path(directory).resolve()
    if not isinstance(relative, str) or '\\' in relative or Path(relative).is_absolute():
        raise ValueError('Expected a relative registered subject path')
    parts = Path(relative).parts
    folder = '00_pieces' if kind == 'piece' else '01_assemblies' if kind == 'assembly' else None
    if folder is None or len(parts) != 3 or parts[0] != folder or parts[2] not in {kind+'.json', kind+'.jsonc'}:
        raise ValueError(f'{kind.capitalize()} source must be {folder}/<id>/{kind}.jsonc or {kind}.json')
    if not _SLUG.fullmatch(parts[1]) or not 2 <= len(parts[1]) <= 64:
        raise ValueError('Subject source requires a safe lowercase folder identifier')
    if identifier is not None and parts[1] != identifier:
        raise ValueError('Registered subject identity disagrees with its source folder')
    path = directory.joinpath(*parts)
    if path.resolve() != path or not path.is_relative_to(directory):
        raise ValueError('A registered subject path escapes or redirects its owning domain')
    if source_path(path.parent, kind) != path:
        raise ValueError('Registered subject filename differs from its maintained source')
    return path


def load_subject(directory, kind):
    """Read the sole maintained JSON or JSONC definition in a subject folder."""
    return jsonc.load(source_path(directory, kind))


def new_subject_document(value, kind):
    """Create a JSONC definition with the complete human-readable usage header."""
    if kind not in {'piece', 'assembly'}:
        raise ValueError('Subject kind must be piece or assembly')
    name = value.get('name') or value.get('title') or value.get('id')
    title = f'{kind.capitalize()} definition: {name}'
    summary = ('Define permanent game-resource identity and reusable construction metadata.' if kind == 'piece'
               else 'Define the placed reusable components and construction plan for this assembly.')
    writer = ('custom-pieces/scp.py scaffold and scp.registration.apply_registration() create this definition; contributors use scp.subject_sources.write_subject() for later edits.'
              if kind == 'piece' else
              'Contributors following custom-pieces/docs/WORKFLOW_ASSEMBLY_CREATION.md; scp.subject_sources.write_subject() preserves later edits.')
    affects = ('Permanent construction, model, preview, and menu identifiers, generated documentation, and derived game resources.'
               if kind == 'piece' else
               'Placed component positions and rotations, generated documentation, and the assembly’s component-cycle menu.')
    header = (f'// title: {json.dumps(title, ensure_ascii=False)}\n'
              f'// summary: {json.dumps(summary)}\n//\n'
              f'// Used when: Contributors author this {kind}, and the catalogue loads its registered definition.\n'
              '// Read by: scp.catalog.load_catalog(), documentation generators, and build or assembly-menu workflows.\n'
              f'// Updated by: {writer}\n'
              f'// Affects: {affects}\n')
    return jsonc.document(value, source=header+'{}\n')


def write_subject(directory, kind, value):
    """Update the original source path, retaining JSONC introductory comments."""
    path = source_path(directory, kind)
    if path.suffix == '.jsonc':
        jsonc.dump(path, value)
    else:
        text = json.dumps(value, indent=2, allow_nan=False)+'\n'
        if path.read_text(encoding='utf-8') != text:
            path.write_text(text, encoding='utf-8')
    return path


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
            identifier = _identifier(piece.get('id'))
            registered_source_path(directory, relative, 'piece', identifier=identifier)
            if piece.get('recipe') != recipe:
                continue
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
