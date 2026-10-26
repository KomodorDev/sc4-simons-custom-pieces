"""Resolve transport implementations from explicit domain registry metadata."""
from functools import lru_cache
import importlib
import json
from .paths import project_root


@lru_cache(maxsize=None)
def implementation(domain):
    root = project_root()
    project = json.loads((root/'project.json').read_text())
    from .catalog import safe_relative
    registry = safe_relative(root, project['domains'][domain]['registry'])
    name = json.loads(registry.read_text()).get('implementation')
    if not name:
        raise ValueError(f'{domain}: no implementation is registered')
    if not all(part.isidentifier() for part in name.split('.')):
        raise ValueError('Invalid domain implementation module')
    return name


def domain_module(piece, feature):
    return importlib.import_module(implementation(piece['domain']) + '.' + feature)
