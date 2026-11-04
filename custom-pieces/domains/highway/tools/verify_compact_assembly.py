#!/usr/bin/env python3
"""Verify the saved compact highway assembly, including all six pier contacts."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp_highway.assembly_verify import verify_assembly


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    scene = jsonc.load(args.root / 'domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/assembly.jsonc')
    print(json.dumps(verify_assembly(args.build, scene, evidence_path=args.output), indent=2))


if __name__ == '__main__':
    main()
