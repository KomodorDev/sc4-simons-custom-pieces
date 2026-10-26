"""Load SCP's shared library API from the Planner's explicit source configuration."""
import importlib
import json
import os
from pathlib import Path
import sys


PLANNER = Path(__file__).resolve().parents[2]


def configured_root():
    """Use an explicit environment override or pilot.json's registered root."""
    override = os.environ.get('SCP_CUSTOM_PIECES_ROOT')
    if override:
        return Path(override).expanduser().resolve()
    config = json.loads((PLANNER / 'pilot.json').read_text())
    return (PLANNER / config['custom_pieces_root']).resolve()


def source_module(name):
    """Import source code once; reject an already imported unrelated SCP package."""
    framework = configured_root() / 'framework'
    expected = (framework / 'scp').resolve()
    if not (expected / (name+'.py')).is_file():
        raise ImportError(f'Configured SCP library lacks {name}: {expected}')
    package = sys.modules.get('scp')
    if package is not None and not Path(package.__file__).resolve().is_relative_to(expected):
        raise ImportError('An unrelated SCP package is already imported; restart with the configured library')
    if str(framework) not in sys.path:
        sys.path.insert(0, str(framework))
    return importlib.import_module('scp.'+name)
