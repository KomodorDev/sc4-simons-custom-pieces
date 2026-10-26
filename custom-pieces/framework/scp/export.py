"""Enumerate portable documentation and identify immutable compiled build facts."""
import hashlib
import json
from pathlib import Path


PUBLIC_SUFFIXES = {'.py', '.json', '.jsonc', '.md', '.txt', '.command', '.png', '.toml', '.yaml', '.yml', '.html'}
PRIVATE_PARTS = {'local', 'dist', '__pycache__', '.git', '.venv', '.pytest_cache', 'backups', 'build'}


def compiled_manifest_sha256(manifest):
    """Bind payloads and build contracts independently of mutable documentation.

    Only documentation and evidence/publication state are omitted. Every other
    manifest field, including unknown future fields, remains fingerprinted.
    Exact payload hashes, selected definitions, overlay metadata, dependency
    audits, and donor identities therefore cannot change during a docs handoff.
    """
    facts = {key: value for key, value in manifest.items()
             if key not in {'documentation', 'release', 'installed', 'in_game_tested'}}
    raw = json.dumps(facts, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf8')
    return hashlib.sha256(raw).hexdigest()


def documentation_members(root):
    """Return one current portable documentation snapshot for a package."""
    return {'docs/' + relative.as_posix(): portable_bytes(root, path)
            for relative, path in public_files(root)}


def public_files(root):
    """Keep relative paths intact so nested Markdown links remain portable."""
    root = Path(root).resolve()
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if (any(part in PRIVATE_PARTS or part.endswith('.egg-info') for part in relative.parts)
                or path.is_symlink() or not path.is_file()):
            continue
        if path.suffix in PUBLIC_SUFFIXES or path.name == '.gitignore':
            yield relative, path


def portable_bytes(root, path):
    """Replace workstation-specific project prefixes in prose and evidence."""
    raw = Path(path).read_bytes()
    if Path(path).suffix in {'.md', '.json', '.jsonc', '.txt', '.html'}:
        prefixes = {str(Path(root).absolute().parent), str(Path(root).resolve().parent)}
        prefixes.update(repr(prefix)[1:-1] for prefix in tuple(prefixes))
        for value in sorted(prefixes, key=len, reverse=True):
            raw = raw.replace(value.encode(), b'/path/to/sc4-simons-custom-pieces')
    return raw


def copy_documentation(root, stage, sha):
    """Bundle the maintained tree, including diagrams and connection records."""
    records = []
    for relative, path in public_files(root):
        target = Path(stage) / 'docs' / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        raw = portable_bytes(root, path)
        target.write_bytes(raw)
        records.append({'path': 'docs/' + relative.as_posix(), 'sha256': sha(raw), 'bytes': len(raw)})
    return records
