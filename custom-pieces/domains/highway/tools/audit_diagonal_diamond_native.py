#!/usr/bin/env python3
"""Reproduce the bounded native-donor audit without private workstation settings.

Reads original archives and writes portable measured evidence only. This does
not register a piece, build game resources, install files, or test the game.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import re
import sys

ROOT = next(parent for parent in Path(__file__).resolve().parents
            if (parent / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.dbpf import decompress, entries, read_index, require
from scp.models import parse_s3d, positions

GENERATOR_VERSION = 1
DONORS = {
    'NetworkAddonMod_Controller.dat': 'd903540cdf772b4ed6a072c504e006e1cac384f8027ce58a288a5a9654f94161',
    'RealHighway_DD_RHW-4.dat': 'ccf8dabd3930fce92d0baa872ff974e3a536ddcc40762505a2e70eafcf9c0dfb',
    'RealHighway_Core.dat': '8a172e4d7f628e09af3e153ef2effb34a2bcf876ff3c8f76210cb48d660aa191',
    'RealHighway_Avenue_MIS_Ramp_PuzzlePieces.dat': 'e0eb1f2b47327f2a65e16a099df3ea7de2ff5af0f4ef723ae8fe74cba380657a',
    'RealHighway_MIS.dat': 'dec1873a357cca39a5a06de3b0722757b52b72c47c33a24d269d846779dba1a8',
}
PATH = (0x296678F7, 0xA966883F)
S3D = (0x5AD0E817, 0xBADB57F1)
RUL = (0x0A5BCF4B, 0xAA5BCF57)
AVENUE = (0x296678F7, 0x69668828, 0x04000200)
AVENUE_SHA256 = 'e724937d0055bd680e50c5c59066a5ca9fc45d402ae75fb877c9e10fd3f3d746'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def tgi(key):
    return '-'.join(f'{number:08X}' for number in key)


def parse_native_paths(raw):
    """Read the two measured SC4PATHS versions, retaining native capacity labels.

    Native comment labels identify deliberate invalid capacity paths. Interior
    coordinates alone do not identify them: an interior endpoint can instead
    belong to a legitimate route ending inside a tile.
    """
    tokens = []
    capacity_section, label = False, None
    for source_line in raw.decode('ascii').splitlines():
        line = source_line.strip()
        if not line:
            continue
        if line.startswith('--'):
            comment = line[2:].strip('- ')
            if 'invalid paths for capacity increase' in comment.casefold():
                capacity_section = True
            else:
                label = comment
            continue
        tokens.append((line, capacity_section, label))
    require(len(tokens) >= 5, 'Truncated native SC4PATHS header')
    values = [token[0] for token in tokens]
    require(values[0] == 'SC4PATHS' and values[1] in {'1.1', '1.2'},
            'Unsupported native SC4PATHS format; expected 1.1 or 1.2')
    count, stops, terrain = map(int, values[2:5])
    require(count >= 0 and stops == 0 and terrain in {0, 1},
            'Unsupported native SC4PATHS counts or terrain flag')
    cursor, routes = 5, []
    fields = 5 if values[1] == '1.1' else 6
    for _ in range(count):
        require(cursor + fields <= len(tokens), 'Truncated native PATH route header')
        metadata = list(map(int, values[cursor:cursor + fields]))
        excluded, route_label = tokens[cursor][1:]
        transport, lane, entry, exit_ = metadata[:4]
        compatibility = metadata[4] if fields == 6 else None
        nodes = metadata[-1]
        cursor += fields
        require(nodes >= 2 and entry in {*range(4), 255} and exit_ in {*range(4), 255},
                'Invalid native PATH route directions or node count')
        require(cursor + nodes <= len(tokens), 'Truncated native PATH route points')
        points = [tuple(map(float, point.split(',')))
                  for point in values[cursor:cursor + nodes]]
        require(all(len(point) == 3 and all(math.isfinite(value) for value in point)
                    for point in points), 'Invalid native PATH coordinates')
        routes.append({
            'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
            'compatibility': compatibility, 'points': points,
            'native_comment': route_label,
            'classification': ('native_invalid_capacity_path' if excluded
                               else 'native_saved_route'),
            'included_as_connectable_route': not excluded,
        })
        cursor += nodes
    require(cursor == len(tokens), 'Unexpected trailing native PATH data')
    return {'format': values[1], 'terrain': terrain, 'routes': routes}


def path_record(key, raw):
    decoded = parse_native_paths(raw)
    routes = decoded['routes']
    return {
        'tgi': tgi(key), 'decoded_bytes': len(raw), 'sha256': sha(raw),
        **decoded, 'total_routes': len(routes),
        'connectable_routes': sum(route['included_as_connectable_route'] for route in routes),
        'invalid_capacity_routes_excluded': sum(
            not route['included_as_connectable_route'] for route in routes),
    }


def model_record(key, raw):
    model = parse_s3d(raw)
    meshes = []
    for mesh in model['meshes']:
        points = positions(model['vertices'][mesh['frames'][0][0]])
        name = mesh['name'].rstrip(b'\0').decode('ascii')
        record = {
            'name': name,
            'stored_coordinate_bounds_m': {
                axis: [min(point[index] for point in points), max(point[index] for point in points)]
                for index, axis in enumerate(['x', 'y_vertical', 'z'])
            },
            'x_plus_z_projection_m': [
                min(point[0] + point[2] for point in points) / math.sqrt(2),
                max(point[0] + point[2] for point in points) / math.sqrt(2),
            ],
        }
        if name in {'Top Deck', 'Bottom Deck', 'Avenue'}:
            record['first_frame_vertices'] = points
        meshes.append(record)
    return {
        'tgi': tgi(key), 'decoded_bytes': len(raw), 'sha256': sha(raw),
        'mesh_count': len(meshes), 'meshes': meshes,
        'limits': ('These are stored vertices and geometric bounds. Transparent or textured triangle '
                   'coverage is not a measured paved-road width, a vehicle envelope, or a physical '
                   'collision result.'),
    }


def required_resource(resources, key, archive_name):
    require(key in resources, f'{archive_name}: missing required native resource {tgi(key)}')
    return resources[key]


def load_archives(plugins):
    require(plugins.is_dir(), '--plugins must name an existing Plugins directory')
    archives = {}
    for name, expected in DONORS.items():
        matches = sorted(path for path in plugins.rglob(name) if path.is_file())
        require(len(matches) == 1,
                f'Expected exactly one {name} below --plugins; found {len(matches)}')
        raw = matches[0].read_bytes()
        require(sha(raw) == expected,
                f'{name}: SHA-256 differs from the audited baseline; re-audit this donor version')
        archives[name] = {
            'raw': raw,
            'resources': {key: decompress(value) for key, value in entries(raw).items()},
        }
    return archives


def ramp_scan(resources):
    records = []
    for key, raw in sorted(resources.items()):
        if key[0] != PATH[0] or key[2] & 0xFFFF0000 != 0x57830000:
            continue
        parsed = path_record(key, raw)
        routes = [route for route in parsed['routes'] if route['included_as_connectable_route']]
        records.append({
            'tgi': tgi(key), 'sha256': sha(raw), 'routes': len(parsed['routes']),
            'connectable_routes': len(routes),
            'heights_m': sorted({point[2] for route in routes for point in route['points']}),
            'has_route_changing_height': any(
                len({point[2] for point in route['points']}) > 1 for route in routes),
            'external_direction_pairs': sorted({(route['entry'], route['exit']) for route in routes}),
        })
    samples = {'57830059', '57830259', '5783005A', '5783025A', '57830A59', '57830A5A'}
    return {
        'instance_prefix': '5783',
        'scope': ('Every PATH resource with a 5783 instance prefix in this archive; this is a bounded '
                  'candidate scan, not proof that no suitable donor exists elsewhere.'),
        'candidates': len(records),
        'candidates_with_changing_height_route': sum(record['has_route_changing_height'] for record in records),
        'resource_instances': [record['tgi'].rsplit('-', 1)[1] for record in records],
        'height_sets_m': [list(values) for values in sorted({tuple(record['heights_m']) for record in records})],
        'sampled_records': [record for record in records if record['tgi'].rsplit('-', 1)[1] in samples],
        'all_candidates_have_constant_height_routes': not any(record['has_route_changing_height'] for record in records),
    }


def archive_records(archives):
    records = []
    for name, archive in archives.items():
        resources = archive['resources']
        record = {
            'filename': name, 'sha256': sha(archive['raw']), 'archive_bytes': len(archive['raw']),
            'resource_count': len(resources),
            'resource_types': dict(sorted(Counter(f'{key[0]:08X}' for key in resources).items())),
        }
        if name == 'RealHighway_DD_RHW-4.dat':
            instances = [0x57530200, 0x57530900, 0x5753A300, 0x5753A305, 0x5753A380, 0x5753A385]
            record['measured_paths'] = [path_record((*PATH, iid), required_resource(resources, (*PATH, iid), name))
                                        for iid in instances]
            record['measured_models'] = [model_record((*S3D, iid), required_resource(resources, (*S3D, iid), name))
                                         for iid in [0x57530200, 0x5753A300, 0x5753A305]]
            record['ramp_candidate_scan'] = ramp_scan(resources)
        if name == 'RealHighway_Core.dat':
            record['measured_paths'] = [path_record((*PATH, iid), required_resource(resources, (*PATH, iid), name))
                                        for iid in [0x57F53600, 0x57F53900]]
        records.append(record)
    return records


def construction_record(controller):
    raw_rul0 = required_resource(controller, (*RUL, 0x10000000), 'NetworkAddonMod_Controller.dat')
    raw_rul2 = required_resource(controller, (*RUL, 0x10000002), 'NetworkAddonMod_Controller.dat')
    rul0 = raw_rul0.decode('ascii')
    records = []
    for block in re.split(r'(?=^\[HighwayIntersectionInfo_)', rul0, flags=re.M):
        match = re.match(r'\[HighwayIntersectionInfo_0x([0-9a-fA-F]+)\]', block)
        if not match:
            continue
        puzzle = int(match[1], 16)
        if puzzle & 0xFFFF != 0x5072 and puzzle not in {0x5136, 0x45136}:
            continue
        fields = defaultdict(list)
        for source_line in block.splitlines()[1:]:
            body = source_line.split(';', 1)[0].strip()
            if '=' in body:
                key, value = body.split('=', 1)
                fields[key.strip()].append(value.strip())
        records.append({'puzzle_id': f'0x{puzzle:08X}', 'native_block_sha256': sha(block.encode('ascii')),
                        'fields': dict(fields)})
    rules = [{'line': index + 1, 'rule': line}
             for index, line in enumerate(raw_rul2.decode('ascii').splitlines())
             if any(term in line.lower() for term in ['0x5753a300', '0x5753a305'])]
    return {
        'rul0_tgi': tgi((*RUL, 0x10000000)), 'native_rul0_sha256': sha(raw_rul0),
        'selected_families': records, 'crossing_rul0_reference_matches': rul0.lower().count('5753a3'),
        'rul2_tgi': tgi((*RUL, 0x10000002)), 'native_rul2_sha256': sha(raw_rul2),
        'selected_crossing_rules': rules,
    }


def avenue_record(game_dat):
    require(game_dat.is_file(), '--game-dat must name an existing original SimCity_1.dat archive')
    rows = [row for row in read_index(game_dat) if row[:3] == AVENUE]
    require(len(rows) == 1, f'SimCity_1.dat: expected one native avenue resource {tgi(AVENUE)}')
    row = rows[0]
    with game_dat.open('rb') as stream:
        stream.seek(row[3])
        raw = decompress(stream.read(row[4]))
    require(sha(raw) == AVENUE_SHA256,
            'Native diagonal avenue PATH differs from the measured baseline; re-audit this game version')
    return {
        'archive_filename': 'SimCity_1.dat',
        'scope': 'Only this indexed resource was read; the complete game archive is not a registered build dependency.',
        **path_record(AVENUE, raw),
    }


def audit(plugins, game_dat):
    archives = load_archives(plugins)
    return {
        'schema_version': 1,
        'purpose': 'Frozen native-donor measurements for the experimental diagonal double-decker highway and avenue design.',
        'status': ('donor-only; no highway implementation adapter, compiled candidate, installed candidate, '
                   'or game operation is established by this audit'),
        'baseline_measurement_date': '2026-10-30',
        'generator': {
            'path': Path(__file__).resolve().relative_to(ROOT).as_posix(),
            'version': GENERATOR_VERSION, 'sha256': sha(Path(__file__).read_bytes()),
            'shared_parsers': {name: sha((ROOT / 'framework' / name).read_bytes())
                               for name in ['scp/dbpf.py', 'scp/models.py']},
        },
        'source_privacy': ('Archive filenames and resource identifiers are portable; private absolute source paths '
                           'are intentionally omitted. Native archives remain private and are not copied into this evidence.'),
        'coordinate_notes': {
            'path': ('Saved PATH points use x, y_ground_plane, and z_vertical in meters. '
                     'Direction indices are native 0=west, 1=north, 2=east, and 3=south.'),
            'model': ('Saved S3D vertices use x, y_vertical, and z in meters. '
                      'No automatic PATH-to-model alignment or texture-alpha interpretation is asserted.'),
        },
        'facts': {
            'traffic_profile': ('NAM 50, right-hand traffic, identified by the pinned audited controller hash. '
                                'Individual donor semantics still require comparison with the placed geometry.'),
            'dd_real_deck_heights_m': [7.5, 15.0], 'avenue_height_m': 0.0, 'dd_lanes_per_deck': 2,
            'main_diagonal_route_directions': {
                '57530200': {'upper': '2 to 3', 'lower': '3 to 2'},
                '57530900': {'upper': '3 to 2', 'lower': '2 to 3'},
            },
            'capacity_paths': ('The native 57530200, 57530900, 57F53600, and 57F53900 resources contain two routes '
                               'explicitly labelled Invalid Paths for Capacity Increase. They are recorded and excluded '
                               'from connectable-route claims using the native comment section, not a coordinate heuristic.'),
            'crossing': ('5753A300, 5753A305, 5753A380, and 5753A385 contain actual diagonal DD road and perpendicular '
                         'diagonal ground-avenue paths plus models. Their complete multi-cell arrangement has not been '
                         'solved or verified here.'),
            'construction': ('The native DD diagonal filler has RUL0 puzzle roots 00085072 and 00095072 and references '
                             'Core.dat models 57F53600 and 57F53900. The 5753A3 crossing is created through native RUL2 '
                             'rewrites; no RUL0 family containing 5753A3 references was found in the controller.'),
            'ramps': ('The native named DDRHW-4/MIS-1 entrance and exit puzzle roots 00045136 and 00005136 explicitly '
                      'describe Orthogonal ramps. This audit does not establish a diagonal DD to avenue on/off-ramp '
                      'seam or a complete donor-clone solution.'),
        },
        'archives': archive_records(archives),
        'native_avenue_diagonal_path': avenue_record(game_dat),
        'native_construction': construction_record(archives['NetworkAddonMod_Controller.dat']['resources']),
        'remaining_work': [
            'Choose and independently verify the complete diagonal crossing placement, including the paired DD and avenue cells.',
            'Establish measured native joining seams for all intended on- and off-ramps; do not infer highway compatibility from rail ramps.',
            'Implement and register a highway recipe, menu, connector adapter, extraction workflow, and independent saved-resource verifier before changing the domain to implemented.',
            'Audit and register exact dependencies before a native highway build.',
            'Build, verify, and inspect the saved game resources, then obtain separate human game observations.',
        ],
        'game_observations': 'unverified',
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugins', required=True, type=Path,
                        help='Plugins directory containing the original audited NAM archives')
    parser.add_argument('--game-dat', required=True, type=Path,
                        help='Original SimCity_1.dat containing the measured native avenue PATH')
    parser.add_argument('--output', required=True, type=Path,
                        help='JSON evidence file to write outside the native Plugins directory')
    args = parser.parse_args(argv)
    try:
        plugins, game_dat, output = (path.expanduser().resolve()
                                     for path in [args.plugins, args.game_dat, args.output])
        require(not output.is_relative_to(plugins) and output != game_dat,
                'Audit output must be outside the native Plugins directory and distinct from the game archive')
        result = audit(plugins, game_dat)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    except (OSError, ValueError, UnicodeError) as error:
        parser.exit(1, f'Native donor audit failed: {error}\n')
    print(json.dumps({'output_file': output.name, 'bytes': output.stat().st_size,
                      'sha256': sha(output.read_bytes()), 'status': result['status']}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
