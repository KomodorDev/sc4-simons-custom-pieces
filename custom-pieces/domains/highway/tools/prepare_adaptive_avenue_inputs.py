#!/usr/bin/env python3
"""Capture the pinned native Avenue inputs privately, without installing anything."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))

from scp.catalog import load_catalog, safe_relative
from scp.dbpf import require
from scp.resource_audit import capture_resource_bundle


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugins', type=Path, required=True,
                        help='Original NAM Plugins root, read only')
    parser.add_argument('--extra-plugins', type=Path, action='append', default=[],
                        help='Additional original Plugins root; repeat as needed')
    parser.add_argument('--game-dir', type=Path, required=True,
                        help='Original game folder containing SimCity_4.dat')
    parser.add_argument('--output', type=Path, required=True,
                        help='New capture directory under the selected library local/ folder')
    parser.add_argument('--root', type=Path, default=ROOT,
                        help='Library root containing project.jsonc')
    args = parser.parse_args(argv)
    try:
        root = args.root.expanduser().resolve()
        roots = [path.expanduser().resolve() for path in (args.plugins, *args.extra_plugins)]
        game = args.game_dir.expanduser().resolve()
        require(all(path.is_dir() for path in (*roots, game)), 'Every input root must be an existing directory')
        require(len(set(roots)) == len(roots)
                and not any(a != b and a.is_relative_to(b) for a in roots for b in roots),
                'Plugins scan roots must be distinct and must not be nested')
        output = args.output.expanduser().resolve()
        require(not any(output.is_relative_to(folder) for folder in (*roots, game)),
                'Capture output must stay outside every supplied game and Plugins input root')
        record = load_catalog(root)['_profile']['files']['adaptive_avenue']
        audit = json.loads(safe_relative(root, record['audit']).read_text(encoding='utf-8'))
        require(record.get('capture_kind') == audit.get('capture_kind') == 'resource-bundle'
                and audit.get('capture', {}).get('file') == record['filename']
                and audit['capture'].get('sha256') == record['sha256'],
                'Adaptive Avenue capture evidence differs from the selected profile')
        sources = []
        for descriptor in audit['sources']:
            filename = descriptor['filename']
            require(isinstance(filename, str) and filename and Path(filename).name == filename
                    and '\\' not in filename and ':' not in filename,
                    'Capture source must declare one plain archive filename')
            if descriptor['location'] == 'game':
                candidates = game.iterdir()
            elif descriptor['location'] == 'plugins':
                candidates = (path for folder in roots for path in folder.rglob('*'))
            else:
                raise ValueError('Capture source location must be game or plugins')
            matches = [path for path in candidates
                       if path.is_file() and path.name.casefold() == filename.casefold()]
            require(len(matches) == 1, f'Expected one original {filename}; found {len(matches)}')
            sources.append({**descriptor, 'archive': matches[0]})
        report = capture_resource_bundle(sources, args.output, filename=record['filename'],
                                         expected_sha256=record['sha256'], root=root, plugins=roots[0])
    except (OSError, ValueError) as error:
        print(json.dumps({'status': 'error', 'error': str(error)}), file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
