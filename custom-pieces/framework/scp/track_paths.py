"""SC4PATH encoding/parsing and generic resource type/group constants.

Rail shape samples, profile heights and construction flags are defined by the
high-speed rail domain. This module preserves the existing byte encoding.
"""
from __future__ import annotations

from collections import Counter
from .dbpf import require

S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
EXEMPLAR = (0x6534284A, 0xA8434037)
EFFECT = (0xEA5118B0, 0xEA5118B1)
LTEXT = (0x2026960B, 0x2A592FD1)
def encode_paths(routes):
    counts = Counter((route['entry'], route['exit']) for route in routes)
    next_class = Counter()
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for route in routes:
        pair = route['entry'], route['exit']
        next_class[pair] += 1
        lane = next_class[pair] if counts[pair] > 1 else 0
        lines += [f"-- SCP_{route['role']}_{pair[0]}_{pair[1]}", '7', str(lane),
                  str(pair[0]), str(pair[1]), str(int(route['junction'])), str(len(route['points']))]
        lines += [','.join(f'{value:.9f}'.rstrip('0').rstrip('.') if value else '0'
                           for value in point) for point in route['points']]
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


def _parse_paths(raw):
    lines = [line.strip() for line in raw.decode('ascii').splitlines()
             if line.strip() and not line.lstrip().startswith('--')]
    require(lines[:2] == ['SC4PATHS', '1.2'] and lines[3:5] == ['0', '0'],
            'Traffic paths must use SC4PATHS 1.2, zero stops and flat terrain')
    count, cursor, result = int(lines[2]), 5, []
    require(count > 0, 'Empty traffic path file')
    for _ in range(count):
        transport, lane, entry, exit_, junction, size = map(int, lines[cursor:cursor + 6])
        cursor += 6
        require(size >= 2, 'Traffic path needs at least two points')
        points = [tuple(map(float, line.split(','))) for line in lines[cursor:cursor + size]]
        cursor += size
        require(len(points) == size and all(len(point) == 3 for point in points), 'Truncated traffic path')
        result.append({'transport': transport, 'class': lane, 'entry': entry, 'exit': exit_,
                       'junction': junction, 'points': points})
    require(cursor == len(lines), 'Unexpected trailing traffic paths')
    return result


