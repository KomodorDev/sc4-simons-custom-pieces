#!/usr/bin/env python3
"""Verify actual saved parallel-diamond resources without installing anything."""
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
from scp_highway.parallel_verify import verify_assembly

DEFAULT_ASSEMBLY = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', required=True, type=Path,
                        help='Existing verified normal or assembly-menu build directory')
    parser.add_argument('--assembly', default=DEFAULT_ASSEMBLY,
                        help='Registered parallel assembly folder identifier')
    parser.add_argument('--output', type=Path,
                        help='Optional saved-resource evidence destination')
    args = parser.parse_args()
    subject = ROOT / 'domains/highway/01_assemblies' / args.assembly
    if args.assembly != Path(args.assembly).name or not subject.is_dir():
        parser.error('--assembly must name an existing highway assembly folder')
    scene = jsonc.load(subject / 'assembly.jsonc')
    print(json.dumps(verify_assembly(args.build, scene, evidence_path=args.output), indent=2))


if __name__ == '__main__':
    main()
