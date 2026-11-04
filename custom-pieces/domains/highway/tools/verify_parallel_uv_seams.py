#!/usr/bin/env python3
"""Measure final saved DD/MIS seam UVs and reject a real encoded phase reset."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import struct
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.models import pack_s3d, parse_s3d
from scp_highway.parallel_verify import _decode_faces, check_highway_ramp_uv_seams, world_resources_from_build


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    world, source = world_resources_from_build(args.build)
    faces, mutants = [], []
    for cell, (raw, _path) in world.items():
        origin = 16. * cell[0], -16. * cell[1]
        faces.extend(_decode_faces(raw, origin=origin))
        model = parse_s3d(raw)
        indices = {frame[0] for mesh in model['meshes'] for frame in mesh['frames']
                   if model['materials'][frame[3]]['textures'] == [0x5712000E]}
        for index in indices:
            block = model['vertices'][index]
            data = bytearray(block['data'])
            for at in range(16, len(data), block['stride']):
                value = struct.unpack_from('<f', data, at)[0]
                struct.pack_into('<f', data, at, value + .01)
            block['data'] = bytes(data)
        mutants.extend(_decode_faces(pack_s3d(model), origin=origin))
    report = check_highway_ramp_uv_seams(faces)
    report['schema_version'] = 1
    report['source'] = source
    try:
        check_highway_ramp_uv_seams(mutants)
    except ValueError as error:
        report['negative_control'] = {'mutation': 'Every actual saved MIS V coordinate shifted by 0.01 repeats',
                                      'rejected': True, 'reason': str(error)}
    else:
        raise ValueError('Native seam checker accepted its actual encoded MIS phase-reset control')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key not in ('source', 'controls')}, indent=2))


if __name__ == '__main__':
    main()
