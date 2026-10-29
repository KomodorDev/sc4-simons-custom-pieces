"""Locate the source project and its private workstation settings explicitly."""
from pathlib import Path


def project_root(start=None):
    """Find project.jsonc without assuming a module's directory depth."""
    path = Path(start or __file__).resolve()
    if path.is_file():
        path = path.parent
    for candidate in (path, *path.parents):
        if (candidate / 'project.jsonc').is_file():
            return candidate
    raise ValueError(f'Cannot locate SCP project.jsonc above {path}')


def local_settings(root):
    """Prefer the new private JSONC path while retaining existing JSON settings."""
    directory = Path(root) / 'local'
    current, legacy = directory / 'settings.jsonc', directory / 'settings.json'
    if current.exists() and legacy.exists():
        raise ValueError('Both local/settings.jsonc and local/settings.json exist; keep only one private settings file')
    return legacy if legacy.exists() else current
