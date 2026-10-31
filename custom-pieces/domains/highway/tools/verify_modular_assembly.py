#!/usr/bin/env python3
"""Verify the saved seven-part modular highway, without installing it."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp_highway.modular_assembly_verify import verify_assembly, verify_compact_alternative


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--compact-alternative', action='store_true',
                        help='Check the same stamp with the six retained compact attachments')
    args = parser.parse_args()
    scene = jsonc.load(ROOT/'domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/assembly.jsonc')
    verify = verify_compact_alternative if args.compact_alternative else verify_assembly
    print(json.dumps(verify(args.build, scene, evidence_path=args.output), indent=2))


if __name__ == '__main__':
    main()
