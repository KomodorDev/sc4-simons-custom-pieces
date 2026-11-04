"""Reproduce portable native-channel and empty-PATH measurements.

Original NAM archives remain private inputs. Only resource identities,
hashes, measurements, and the short empty-PATH format are written out.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path

from scp.dbpf import decompress, entries, read_index, require, tgi_string
from scp.models import parse_s3d, positions
from scp.track_paths import S3D, PATH
from . import native, recipes, verify

ARCHIVES = {
    'dd_rhw': ('RealHighway_DD_RHW-4.dat', 'ccf8dabd3930fce92d0baa872ff974e3a536ddcc40762505a2e70eafcf9c0dfb'),
    'rhw_core': ('RealHighway_Core.dat', '8a172e4d7f628e09af3e153ef2effb34a2bcf876ff3c8f76210cb48d660aa191'),
    'mis': ('RealHighway_MIS.dat', 'dec1873a357cca39a5a06de3b0722757b52b72c47c33a24d269d846779dba1a8'),
    'avenue_mis': ('RealHighway_Avenue_MIS_Ramp_PuzzlePieces.dat', 'e0eb1f2b47327f2a65e16a099df3ea7de2ff5af0f4ef723ae8fe74cba380657a'),
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _source_record(key, raw):
    return {'tgi': tgi_string(key), 'decoded_bytes': len(raw), 'sha256': sha(raw)}


def _zero_scan(label, resources):
    matches, total = [], 0
    for key, raw in sorted(resources.items()):
        if key[0] != PATH[0]:
            continue
        total += 1
        lines = [line.strip() for line in raw.decode('ascii').splitlines()
                 if line.strip() and not line.lstrip().startswith('--')]
        if len(lines) >= 5 and lines[2] == '0':
            require(lines[:2] == ['SC4PATHS', '1.2'] and len(lines) == 5,
                    'Unexpected native zero-route PATH structure')
            matches.append(key)
    samples = []
    if label == 'mis':
        key = (*PATH, 0x5792A449)
        require(key in matches, 'Missing audited zero-route shoulder PATH')
        raw = resources[key]
        model_key = (*S3D, key[2]); model = parse_s3d(resources[model_key])
        meshes = []
        for mesh in model['meshes']:
            points = positions(model['vertices'][mesh['frames'][0][0]])
            meshes.append({'vertices': len(points),
                           'bounds_s3d_xyz_m': [[min(p[a] for p in points), max(p[a] for p in points)]
                                                for a in range(3)]})
        samples.append({**_source_record(key, raw), 'decoded_text': raw.decode('ascii'),
                        'model': {**_source_record(model_key, resources[model_key]), 'meshes': meshes},
                        'interpretation': ('The model has an elevated partial road surface, raised barrier, '
                                           'and underside, while the saved PATH contains no traffic routes.')})
    return {'archive_filename': ARCHIVES[label][0], 'path_resources_scanned': total,
            'zero_route_path_resources': len(matches), 'samples': samples,
            'scope': 'Every PATH in this exact archive; no claim about other versions or in-game behaviour.'}


def _game_flags(path):
    key = (0x0A5BCF4B, 0xAA5BCF57, 0x0000000D)
    rows = [row for row in read_index(path) if row[:3] == key]
    require(len(rows) == 1, 'Expected one native Avenue RUL1 resource')
    with Path(path).open('rb') as stream:
        stream.seek(rows[0][3]); raw = decompress(stream.read(rows[0][4]))
    lines = [line.strip() for line in raw.decode('ascii').splitlines() if line.strip()]
    for seq in (['1,0,1,3,0', '2,4,3,0,0,1', '3,0,0x04000200,0,0'],
                ['1,3,1,3,1', '2,1,0,1,3,0', '2,3,3,0,0,1', '2,5,3,0,0,1',
                 '2,7,0,1,3,0', '3,0,0x04003800,0,0']):
        require(any(lines[i:i + len(seq)] == seq for i in range(len(lines))),
                'Native Avenue RUL1 flags differ from the measured mapping')
    return {'archive_filename': Path(path).name, **_source_record(key, raw),
            'measured_records': [{'native_instance': '04000200', 'rul1_flags_in_source_order': [0, 1, 3, 0],
                                  'rul0_little_endian_flags': '00030100', 'proper_rotation': 0},
                                 {'native_instance': '04003800', 'rul1_flags_in_source_order': [3, 1, 3, 1],
                                  'rul0_little_endian_flags': '01030103', 'proper_rotation': 0}],
            'avenue_half_A300': {'derivation': '04000200 rotated by 180 degrees', 'rul0_flags': '01000003'}}


def audit(plugins, game_dat=None):
    plugins = Path(plugins)
    context, archive_records = {}, []
    for label, (filename, fingerprint) in ARCHIVES.items():
        matches = [path for path in plugins.rglob(filename) if path.is_file()]
        require(len(matches) == 1, f'Expected exactly one {filename}')
        raw = matches[0].read_bytes()
        require(sha(raw) == fingerprint, f'{filename} changed; re-audit before using it')
        context[label] = {key: decompress(value) for key, value in entries(raw).items()}
        archive_records.append({'filename': filename, 'sha256': fingerprint, 'bytes': len(raw)})
    compiled = native.build_crossing_channels(context)
    parsed = [{'routes': native.parse_paths(path)} for cell, model, path in compiled]
    starts, ends = Counter(), Counter()
    for (cell, _, _), item in zip(compiled, parsed):
        for route in item['routes']:
            for point, target in ((route['points'][0], starts), (route['points'][-1], ends)):
                target[(route['transport'], verify._global(point, cell))] += 1
    boundary = []
    for direction, values, counterpart in [('entry', starts, ends), ('exit', ends, starts)]:
        for (transport, point), multiplicity in sorted(values.items()):
            if (transport, point) not in counterpart:
                require(multiplicity == 1, 'Ambiguous complete native boundary channel')
                boundary.append({'direction': direction, 'transport': transport,
                                 'world_east_north_height_m': list(point)})
    model_records = []
    for cell, raw, path in compiled:
        model_records.append({'cell': list(cell), 's3d_sha256': sha(raw), 'path_sha256': sha(path),
                              'path_fragments': len(native.parse_paths(path))})
    source_records = []
    for iid in [0x5753A300, 0x5753A305, 0x5753A380]:
        for prefix in (PATH, S3D):
            key = (*prefix, iid)
            source_records.append(_source_record(key, context['dd_rhw'][key]))
    result = {
        'schema_version': 1, 'measurement_date': '2026-10-30',
        'purpose': 'Native DD RHW-4 and Avenue channel composition and zero-route PATH measurements.',
        'status': 'Saved-resource evidence only; no game observation, installation, or publication is asserted.',
        'privacy': 'Original archives stay private; absolute workstation paths and binary archive payloads are omitted.',
        'generator': {'module': 'scp_highway.native_audit', 'sha256': sha(Path(__file__).read_bytes())},
        'archives': archive_records, 'native_channel_resources': source_records,
        'coordinates': {'path': '(east, north, height), metres', 's3d': '(east, height, -north), metres',
                        'construction_cells': '(column east, row south), 16 metres per cell',
                        'normalized_core_cell': [1, 1], 'highway_axis': 'east - north = 40 metres',
                        'avenue_axis': 'east + north = 0 metres'},
        'placements': [{'cell': list(cell), 'dd_source': f'{dd:08X}' if dd else None,
                        'dd_rotation_quarter_turns': dd_rotation, 'avenue_source': f'{avenue:08X}',
                        'avenue_rotation_quarter_turns': avenue_rotation}
                       for cell, dd, dd_rotation, avenue, avenue_rotation in native.PARTS],
        'saved_channel_models': model_records, 'complete_boundary_channels': boundary,
        'route_graph': [verify._journeys(parsed, native.CELLS, rotation) for rotation in range(4)],
        'measured_profiles': {
            'dd_paired_paved_deck_width_m': 16., 'dd_lane_offsets_from_axis_m': [-3.2 / math.sqrt(2), 3.2 / math.sqrt(2)],
            'dd_deck_surface_heights_m': [7.5, 15.], 'dd_substructure_thickness_m': 1.,
            'dd_barrier_profile_relative_to_deck_m': [[-8., 0.], [-7.78125, .328125],
                [-7.734375, 1.390625], [-7.4375, 1.390625], [-7.375, .328125], [-7.171875, 0.]],
            'dd_barrier_opposite_side': 'Reflect transverse offsets through zero; retain heights.',
            'avenue_lane_offsets_from_axis_m': [value / math.sqrt(2) for value in [-11.2, -4.8, 4.8, 11.2]],
            'avenue_outer_pedestrian_offsets_from_axis_m': [-15.3 / math.sqrt(2), 15.3 / math.sqrt(2)],
            'avenue_paved_width': 'Not measured: native triangle bounds include texture-controlled coverage.',
        },
        'zero_route_scan': [_zero_scan(label, context[label]) for label in ARCHIVES],
        'inspection_render_filenames': ['core-top.png', 'core-ne.png', 'core-sw.png'],
        'limits': ['The complete five-cell crossing composes highway and Avenue channels independently; it is not a renamed RUL2 neighbourhood.',
                   'Native DD models retain their approximately 1.657-metre tile overhangs and contain no new support pillars.',
                   'Generated shadows clip opaque projected triangles to each tile and do not sample texture alpha.',
                   'Software renders and saved-resource graphs do not establish game placement, driving, walking, shadows, or neighbour overrides.'],
    }
    if game_dat is not None:
        result['native_avenue_construction_flags'] = _game_flags(game_dat)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugins', required=True, type=Path)
    parser.add_argument('--game-dat', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args(argv)
    plugins = args.plugins.expanduser().resolve(); output = args.output.expanduser().resolve()
    require(not output.is_relative_to(plugins), 'Evidence output must stay outside Plugins')
    data = audit(plugins, args.game_dat.expanduser().resolve() if args.game_dat else None)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + '\n', encoding='utf8')
    print(json.dumps({'filename': output.name, 'bytes': output.stat().st_size, 'sha256': sha(output.read_bytes())}))


if __name__ == '__main__':
    main()
