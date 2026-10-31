#!/usr/bin/env python3
"""Bind the reviewed native visual transfer to final actual saved DATs.

The reference is a trusted private compiler checkpoint from before host
reassignment. Its mandatory SHA-256 is checked before loading the local
pickle. Native input bytes and private filesystem paths are never exported.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import pickle
import struct
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.models import pack_s3d, parse_s3d
from scp_highway.parallel_verify import verify_native_visual_transfer, world_resources_from_build


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--reference-context', type=Path, required=True)
    parser.add_argument('--reference-sha256', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    raw = args.reference_context.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != args.reference_sha256:
        raise ValueError('Trusted reference context does not match the supplied checked fingerprint')
    reference = pickle.loads(raw)['_parallel_compiled_world']
    candidate, saved_source = world_resources_from_build(args.build)
    report = verify_native_visual_transfer(reference, candidate)
    report['schema_version'] = 1
    report['reference_context_sha256'] = digest
    report['source'] = saved_source
    report['negative_controls'] = []
    host = (2, -2)
    original = parse_s3d(candidate[host][0])
    mesh = next(mesh for mesh in original['meshes'] if any(
        original['materials'][frame[3]]['textures'] == [0x5713000E] for frame in mesh['frames'])
        and original['primitives'][mesh['frames'][0][2]][0][2] >= 6)
    for control in ('changed-native-uv', 'missing-native-triangle'):
        model = deepcopy(original)
        vi, _ii, pi, _mi = mesh['frames'][0]
        if control == 'changed-native-uv':
            block = model['vertices'][vi]
            data = bytearray(block['data'])
            u = struct.unpack_from('<f', data, 12)[0]
            struct.pack_into('<f', data, 12, u + .01)
            block['data'] = bytes(data)
        else:
            kind, first, count = model['primitives'][pi][0]
            model['primitives'][pi][0] = kind, first, count - 3
        mutant = dict(candidate)
        mutant[host] = pack_s3d(model), candidate[host][1]
        try:
            verify_native_visual_transfer(reference, mutant)
        except ValueError as error:
            report['negative_controls'].append({'mutation': control, 'rejected': True, 'reason': str(error)})
        else:
            raise ValueError('Native visual preservation accepted its required negative control: ' + control)
    report['negative_controls_passed'] = True
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ('reference_model_sha256_by_source_cell',
                                     'candidate_model_sha256_by_source_cell', 'source')}, indent=2))


if __name__ == '__main__':
    main()
