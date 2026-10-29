"""Resolve transport implementations from explicit domain registry metadata."""
from functools import lru_cache
import importlib
from . import jsonc
from .paths import project_root


@lru_cache(maxsize=None)
def implementation(domain):
    root = project_root()
    project = jsonc.load(root/'project.jsonc')
    from .catalog import safe_relative
    registry = safe_relative(root, project['domains'][domain]['registry'])
    name = jsonc.load(registry).get('implementation')
    if not name:
        raise ValueError(f'{domain}: no implementation is registered')
    if not all(part.isidentifier() for part in name.split('.')):
        raise ValueError('Invalid domain implementation module')
    return name


def domain_module(piece, feature):
    return importlib.import_module(implementation(piece['domain']) + '.' + feature)
