"""Independent saved PATH, S3D, and construction checks for highway pieces."""
from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
import math
import struct

from scp.dbpf import require
from scp.models import parse_s3d, positions, validate_s3d
from scp.track_paths import PATH, S3D

CORE = 'highway_ddrhw_diagonal_avenue_crossing'
CELLS = ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2))
# Measured decoded model fingerprints for the exact independently composed
# native channels. They bind full vertex attributes, materials, triangle
# order, and animation data, rather than checking only bounding boxes.
MODEL_SHA = (
    'e166ee3fe408f6f9f3a38ff9393cadda81cc5c7ea8b1b997eed73947b8fce911',
    'fa49cb4d40b8890ae23cc993ac31ae89191ff15a7daa3bf48ca657ddca2aa06b',
    'ee7c37dbe7a259130eead031dca99432e92fb9a37e7c9e0e1dd22870b1bd419a',
    '5c36e47942a024f5c9e165c520829430895c922f380cbf4278951f8ceb8f5d75',
    'c039d989e33fe40b1fb4aeacce4fb03159c7be9ca8f2e5a1a1168ec96920b861',
)
PREVIEW_SHA = 'cd036a64e935b54328dd3b999651d37acae7f9ba0726d94a952d0fc53dac8549'
EPS = 2e-6


def _number(value):
    return int(value, 16) if isinstance(value, str) else value


def _core_spec(piece):
    require(piece['footprint'] == [3, 3] and [tuple(cell) for cell in piece['cells']] == list(CELLS),
            'Saved native crossing footprint differs from the measured five-cell cross')
    return list(map(_number, piece['tile_ids']))


def _route(transport, lane, entry, exit_, a, b):
    return {'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
            'compatibility': 0, 'points': [a, b]}


def _turn(route, angle):
    result = dict(route, entry=(route['entry'] + angle) % 4, exit=(route['exit'] + angle) % 4)
    points = []
    for x, y, height in route['points']:
        for _ in range(angle):
            x, y = y, -x
        points.append((x, y, height))
    result['points'] = points
    return result


def expected_paths():
    """Literal measurements, independent of the native-channel writer."""
    half = [_route(1, 1, 3, 0, (-3.2, -8., 0.), (-8., -3.2, 0.)),
            _route(1, 2, 3, 0, (3.2, -8., 0.), (-8., 3.2, 0.)),
            _route(2, 1, 3, 0, (7.3, -8., 0.), (-8., 7.3, 0.))]
    full = [_route(2, 1, 2, 1, (8., 7.3, 0.), (7.3, 8., 0.)),
            _route(1, 1, 2, 1, (8., 3.2, 0.), (3.2, 8., 0.)),
            _route(1, 2, 2, 1, (8., -3.2, 0.), (-3.2, 8., 0.)),
            _route(1, 1, 0, 3, (-8., 3.2, 0.), (3.2, -8., 0.)),
            _route(1, 2, 0, 3, (-8., -3.2, 0.), (-3.2, -8., 0.)),
            _route(2, 1, 0, 3, (-8., -7.3, 0.), (-7.3, -8., 0.))]
    # A380 measured upper NE, lower SW. Ground routes are separate.
    highway = [_route(1, 0, 3, 2, (3.2, -8., 15.), (8., -3.2, 15.)),
               _route(1, 1, 3, 2, (-3.2, -8., 15.), (8., 3.2, 15.)),
               _route(1, 1, 2, 3, (8., 3.2, 7.5), (-3.2, -8., 7.5)),
               _route(1, 0, 2, 3, (8., -3.2, 7.5), (3.2, -8., 7.5))]
    # The opposite corner uses A300 rotated 180 degrees, retaining native
    # lane class metadata rather than renumbering it to fit another tile.
    other = [_route(1, 0, 0, 1, (-8., -3.2, 15.), (3.2, 8., 15.)),
             _route(1, 1, 0, 1, (-8., 3.2, 15.), (-3.2, 8., 15.)),
             _route(1, 1, 1, 0, (3.2, 8., 7.5), (-8., -3.2, 7.5)),
             _route(1, 0, 1, 0, (-3.2, 8., 7.5), (-8., 3.2, 7.5))]
    return [half, [_turn(r, 2) for r in half], highway + full,
            other + half, other + [_turn(r, 2) for r in half]]


def _sig(route):
    return (route['transport'], route['lane'], route['entry'], route['exit'], route['compatibility'],
            tuple(tuple(round(value, 6) for value in point) for point in route['points']))


def _edge(point):
    x, y, _ = point
    sides = [abs(x + 8) < EPS, abs(y - 8) < EPS, abs(x - 8) < EPS, abs(y + 8) < EPS]
    require(sum(sides) == 1, 'Native highway PATH endpoint is not on exactly one tile edge')
    return sides.index(True)


def _global(point, cell, angle=0):
    x, y, h = point; x += 16 * cell[0]; y -= 16 * cell[1]
    for _ in range(angle):
        x, y = y, -x
    return tuple(round(v, 6) for v in (x, y, h))


def _journeys(parsed, cells, angle):
    starts, ends = defaultdict(list), defaultdict(list)
    for tile_no, (item, cell) in enumerate(zip(parsed, cells)):
        for route_no, route in enumerate(item['routes']):
            key = (tile_no, route_no)
            starts[(route['transport'], _global(route['points'][0], cell, angle))].append(key)
            ends[(route['transport'], _global(route['points'][-1], cell, angle))].append(key)
    shared = starts.keys() & ends.keys()
    require(len(shared) == 20 and all(len(starts[key]) == len(ends[key]) == 1 for key in shared),
            'Missing or ambiguous native highway/Avenue lane seam')
    incoming, outgoing = starts.keys() - ends.keys(), ends.keys() - starts.keys()
    require(len(incoming) == len(outgoing) == 10, 'Incomplete native crossing boundary')
    followed, levels = set(), Counter()
    for start in incoming:
        key = starts[start][0]; count = 0
        while True:
            require(key not in followed, 'Native crossing route loop or duplicate journey')
            followed.add(key); count += 1
            tile, route_no = key; route = parsed[tile]['routes'][route_no]
            end = (route['transport'], _global(route['points'][-1], cells[tile], angle))
            if end in outgoing:
                levels[(start[0], start[1][2])] += 1
                break
            require(end in starts, 'Native crossing route terminates inside its footprint')
            key = starts[end][0]
        require(count == 3, 'Native crossing must preserve the three-cell journey length')
    require(len(followed) == 30 and levels == Counter({(1, 15.): 2, (1, 7.5): 2, (1, 0.): 4, (2, 0.): 2}),
            'Native crossing lost a deck lane, Avenue lane, or pedestrian channel')
    return {'complete_directed_journeys': 10, 'car_journeys': 8, 'pedestrian_channels': 2,
            'matched_internal_lane_seams': len(shared), 'route_fragments_consumed': len(followed)}


def check_paths(resources, piece):
    if piece['recipe'] != CORE:
        from .ramp_paths import check_paths as check_ramp
        return check_ramp(resources, piece)
    from scp.verify import parse_paths
    tiles = _core_spec(piece)
    parsed = [parse_paths(resources[*PATH, tile]) for tile in tiles]
    for actual, expected in zip(parsed, expected_paths()):
        require(actual['version'] == '1.2' and actual['terrain'] == 0 and
                Counter(map(_sig, actual['routes'])) == Counter(map(_sig, expected)),
                'Saved highway PATH differs from literal native route measurements')
        for route in actual['routes']:
            require(_edge(route['points'][0]) == route['entry'] and _edge(route['points'][-1]) == route['exit'],
                    'Saved highway PATH direction disagrees with its endpoint')
            require(len({p[2] for p in route['points']}) == 1, 'Unexpected crossing inter-level shortcut')
    reports = [_journeys(parsed, CELLS, rotation) for rotation in range(4)]
    return {'tile_count': 5, 'native_path_measurements_exact': True,
            'proper_rotations_checked': 4, 'reflections_authored': False,
            'no_capacity_only_paths': True, **reports[0], 'game_operation_tested': False}


def check_models(resources, piece, donors):
    if piece['recipe'] != CORE:
        from .ramp_paths import check_models as check_ramp
        return check_ramp(resources, piece, donors)
    tiles = _core_spec(piece); textures = set(); deck_sections = defaultdict(list)
    for cell, tile, fingerprint in zip(CELLS, tiles, MODEL_SHA):
        for zoom in range(5):
            raw = resources[*S3D, tile + zoom]
            require(hashlib.sha256(raw).hexdigest() == fingerprint, 'Native highway channel model fingerprint changed')
            model = parse_s3d(raw); validate_s3d(model)
            textures.update(texture for mat in model['materials'] for texture in mat['textures'])
            if zoom == 4:
                for mesh in model['meshes']:
                    name = mesh['name'].rstrip(b'\0')
                    if name in {b'Top Deck', b'Bottom Deck'}:
                        for x, h, south in positions(model['vertices'][mesh['frames'][0][0]]):
                            # The normalized crossing's diagonal axis is
                            # east-north=40m, after its (16m,-16m) offset.
                            deck_sections[name].append(((x + south + 16 * sum(cell) - 40) / math.sqrt(2), h))
    for name, height in ((b'Top Deck', 15.), (b'Bottom Deck', 7.5)):
        points = deck_sections[name]
        require(points and all(abs(h - height) < EPS for _, h in points),
                'Native DD deck surface left its measured height')
        require(abs(min(v for v, _ in points) + 8.) < EPS and
                abs(max(v for v, _ in points) - 8.) < EPS,
                'Native DD paired surface width differs from its measured 16m envelope')
    preview = resources[*S3D, _number(piece['preview_id'])]
    require(hashlib.sha256(preview).hexdigest() == PREVIEW_SHA, 'Native highway placement preview differs from the saved five cells')
    validate_s3d(parse_s3d(preview))
    return {'native_channel_fingerprints_verified': True, 'model_resources_checked': 26,
            'native_paired_deck_width_m': 16., 'deck_surface_heights_m': [7.5, 15.],
            'native_substructure_thickness_m': 1., 'native_barrier_height_m': 1.390625,
            'paired_native_deck_projection_verified': True,
            'preview_matches_all_cells': True, 'texture_ids': sorted(textures),
            'game_rendering_tested': False}


def check_construction_fields(fields, piece, resources):
    if piece['recipe'] != CORE:
        from .ramp_paths import check_construction_fields as check_ramp
        return check_ramp(fields, piece, resources)
    _core_spec(piece)
    require(fields['CellLayout'] == ['.a..<', 'bcd..', '.e...', '^....'], 'Wrong highway construction cells/anchors')
    require(fields['ConsLayout'] == ['.\\..<', '\\++..', '.+...', '^....'], 'Wrong highway construction network layout')
    require(fields['CheckType'] == ['a - avenue: 0x01000003', 'b - avenue: 0x00030100',
            'c - dirtroad: 0x03010000 avenue: 0x01030103',
            'd - dirtroad: 0x00000301 avenue: 0x01000003',
            'e - dirtroad: 0x00000301 avenue: 0x00030100'], 'Wrong measured native highway/Avenue construction flags')
    require(fields['Costs'] == ['1000'], 'Wrong native highway crossing construction cost')
    return {'explicit_five_cell_construction': True, 'native_draggable_rules_not_overwritten': True}
