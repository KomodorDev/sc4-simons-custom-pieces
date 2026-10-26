#!/usr/bin/env python3
"""Compatibility launcher for source-owned connection overview rendering.

Canonical images, evidence, and README sections belong to the piece library.
An explicit private output directory creates a working export instead; this
launcher contains no renderer, annotations, or metadata parser of its own.
"""
import argparse
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
PLANNER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLANNER / 'src'))
from scp_planner._source import configured_root, source_module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--custom-pieces-root', type=Path)
    parser.add_argument('--build', type=Path)
    parser.add_argument('--plugins', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    config = json.loads((PLANNER / 'pilot.json').read_text())
    root = (args.custom_pieces_root or configured_root()).resolve()
    output = (PLANNER.parent / args.output).resolve() if args.output else None
    if output is not None and output.is_relative_to(PLANNER / 'docs'):
        parser.error('Maintained overviews now belong to each custom piece. Omit --output for canonical images, or choose a private working folder such as scp-planner/local/overviews.')
    build = args.build.resolve() if args.build else root / config['compiled_build']
    renderer = source_module('connector_overview')
    report = renderer.render_overviews(root, config['pieces'], output_root=output,
                                      build=build, plugins=args.plugins, domain_id=config['domain'])
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
