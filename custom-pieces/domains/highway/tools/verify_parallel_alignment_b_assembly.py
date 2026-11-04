#!/usr/bin/env python3
"""Verify actual saved Alignment B assembly resources without installation."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp_highway.parallel_alignment_b_verify import verify_assembly

ASSEMBLY = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b'
HEADER = '''// title: "Saved Alignment B parallel-diamond assembly checks"
// summary: "Record actual allocated model, traffic, native boundary, construction, and adaptive-layer checks separately from game observations."
//
// Used when: Reviewing a checked Alignment B source build and its complete placed assembly.
// Read by: The assembly TESTING document and contributors assessing the current resource evidence.
// Updated by: domains/highway/tools/verify_parallel_alignment_b_assembly.py after actual saved-resource verification.
// Affects: The measured software scope of this saved assembly; supplies no game placement or visible-traffic pass.
'''


def write_evidence(path, report):
    path = Path(path)
    if path.suffix != '.jsonc':
        raise ValueError('New maintained assembly evidence must use a .jsonc filename')
    path.parent.mkdir(parents=True, exist_ok=True)
    source = path.read_text() if path.is_file() else HEADER + '{}\n'
    path.write_text(jsonc.document(report, source=source), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', required=True, type=Path)
    parser.add_argument('--evidence', '--output', dest='evidence', type=Path)
    args = parser.parse_args()
    scene = jsonc.load(ROOT / 'domains/highway/01_assemblies' / ASSEMBLY / 'assembly.jsonc')
    report = verify_assembly(args.build, scene)
    if args.evidence is not None:
        if args.evidence.resolve().is_relative_to(args.build.resolve()):
            parser.error('--evidence must stay outside the verified build')
        write_evidence(args.evidence, report)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
