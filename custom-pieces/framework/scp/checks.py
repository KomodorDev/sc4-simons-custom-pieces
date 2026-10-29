"""Run shared, domain and assembly tests from their declared ownership folders."""
from pathlib import Path
import os
import subprocess
import sys
from .catalog import load_catalog


def run_checks(root, scope='all', verbose=False):
    root = Path(root).resolve()
    catalog = load_catalog(root)
    directories = [('framework', root/'tests')]
    for slug, domain in catalog['domains'].items():
        directory = root/domain['path']
        if (directory/'tests').is_dir():
            directories.append((slug, directory/'tests'))
    for assembly in catalog['_assemblies']:
        path = root/assembly['path']/'tests'
        if path.is_dir():
            directories.append((assembly['id'], path))
    if scope != 'all':
        directories = [item for item in directories if item[0] == scope]
        if not directories:
            raise ValueError('Unknown check scope; choose framework, a domain ID, an assembly ID or all')
    environment = dict(os.environ)
    paths = [root/'framework']
    paths.extend(root/domain['path']/'implementation' for domain in catalog['domains'].values())
    environment['PYTHONPATH'] = os.pathsep.join(str(path) for path in paths)
    from .documentation_check import check_documentation
    documentation = check_documentation(root)
    results = [{'scope': 'documentation', 'passed': documentation['all_passed']}]
    for error in documentation['errors']:
        print('Documentation: '+str(error), file=sys.stderr, flush=True)
    for name, directory in directories:
        print(f'Checking {name}: {directory.relative_to(root)}', file=sys.stderr, flush=True)
        result = subprocess.run([sys.executable, '-B', str(root/'framework/scp/check_bootstrap.py'),
                                 str(root), 'discover',
                                 '-s', str(directory), '-v' if verbose else '-q'],
                                cwd=root.parent, env=environment, stdout=sys.stderr, stderr=sys.stderr, text=True)
        results.append({'scope': name, 'passed': result.returncode == 0,
                        'directory': directory.relative_to(root).as_posix()})
    return {'all_passed': all(item['passed'] for item in results), 'scopes': results,
            'documentation': documentation,
            'manual_game_results_changed': False, 'installed': False}
