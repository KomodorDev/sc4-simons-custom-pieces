"""Locate the source project and its private workstation settings explicitly."""
from pathlib import Path


def project_root(start=None):
    """Find project.json without assuming a module's directory depth."""
    path = Path(start or __file__).resolve()
    if path.is_file():
        path = path.parent
    for candidate in (path, *path.parents):
        if (candidate / 'project.json').is_file():
            return candidate
    raise ValueError(f'Cannot locate SCP project.json above {path}')


def local_settings(root):
    """Return the one private settings path; never publish this directory."""
    return Path(root) / 'local' / 'settings.json'
