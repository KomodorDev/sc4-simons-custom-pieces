#!/usr/bin/env python3
"""Compare saved adaptive-diamond resources with their fixed-model baseline.

This auditor decodes both saved builds. It does not call a resource writer,
rebuild geometry, or treat software evidence as a game observation.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.dbpf import exemplar, require, tgi_string
from scp.verify import safe_file, strict_dbpf, verify_build
from scp_highway.assembly_verify import check_owned_cells

SUBJECT = 'ddrhw-l1-and-l2-diagonal-avenue-diamond'
SCENE = f'docs/domains/highway/01_assemblies/{SUBJECT}/assembly.jsonc'
S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
AVENUE_PATH = (0x296678F7, 0x69668828)
NETWORK = (0x6534284A, 0xA8434037)
PROP = (0x6534284A, 0xC977C536)
T21 = (0x6534284A, 0x89AC5643)
TEXTURE = (0x7AB50E44, 0x1ABE787D)
SHADOW = (0x7AB50E44, 0x2BC2759A)
EFFECT = (0xEA5118B0, 0xEA5118B1)
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
RUL1 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000001)
NETWORK_INI = (0, 0x8A5971C5, 0x8A5993B9)
IDENTITY_FIELDS = ('id', 'domain', 'recipe', 'puzzle_id', 'tile_ids', 'preview_id',
                   'footprint', 'cells', 'orientation_count', 'effect_name', 'asset_file')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def compare_piece_archive(reference_piece, candidate_piece, reference_raw, candidate_raw):
    """Compare actual decoded resources, including unchanged source buffers."""
    identifier = reference_piece['id']
    require(all(reference_piece.get(key) == candidate_piece.get(key) for key in IDENTITY_FIELDS)
            and reference_piece['menu']['id'] == candidate_piece['menu']['id'],
            f'{identifier}: canonical piece, menu, or construction identity changed')
    reference, candidate = strict_dbpf(reference_raw), strict_dbpf(candidate_raw)
    require('adaptive_ground' not in reference_piece, 'Reference piece is already adaptive')
    rows = candidate_piece.get('adaptive_ground', {}).get('cells', [])
    if not rows:
        require(reference_raw == candidate_raw, f'{identifier}: unconverted asset DAT changed')
    cells = {tuple(cell): int(tile, 16) for cell, tile in
             zip(candidate_piece['cells'], candidate_piece['tile_ids'])}
    removed, additions = set(), set()
    for row in rows:
        tile, resolved = cells[tuple(row['cell'])], int(row['resolved_tile_id'], 16)
        removed.add((*NETWORK, tile))
        additions.add((*AVENUE_PATH, resolved))
        additions.update((*TEXTURE, resolved + appearance + zoom)
                         for appearance in (0, 0x10, 0x20, 0x30) for zoom in range(5))
        if row['prop']:
            additions.update({(*S3D, tile + 5), (*PROP, tile), (*T21, resolved)})
    require(set(reference) - set(candidate) == removed,
            f'{identifier}: resources removed beyond the declared fixed network exemplars')
    require(set(candidate) - set(reference) == additions,
            f'{identifier}: runtime resource additions differ from the exact declared layers')
    for key in removed:
        props = {int(prop['id'], 16): prop['values'] for prop in exemplar(reference[key])['properties']}
        require(props.get(0x10) == [11], f'{identifier}: omitted resource was not a type-11 network exemplar')
    retained = set(reference) & set(candidate)
    for key in sorted(retained):
        require(reference[key] == candidate[key],
                f'{identifier}: retained resource bytes changed: {tgi_string(key)}')
    canonical = {(*S3D, int(candidate_piece['preview_id'], 16)),
                 (*EFFECT, int(candidate_piece['preview_id'], 16))}
    for tile in cells.values():
        canonical.add((*PATH, tile))
        canonical.update((*S3D, tile + zoom) for zoom in range(5))
        canonical.update((*SHADOW, tile + zoom) for zoom in range(5))
    require(canonical <= retained,
            f'{identifier}: canonical models, paths, preview, effect, or shadows are missing')
    report = {'piece_id': identifier, 'asset_file': candidate_piece['asset_file'],
              'reference_dat_sha256': sha(reference_raw), 'candidate_dat_sha256': sha(candidate_raw),
              'dat_byte_identical': reference_raw == candidate_raw,
              'reference_resources': len(reference), 'candidate_resources': len(candidate),
              'unchanged_resources': len(retained), 'removed_network_exemplars': len(removed),
              'added_runtime_resources': len(additions), 'canonical_resources_preserved': len(canonical),
              'added_resource_counts': {'ground_textures': sum(key[:2] == TEXTURE for key in additions),
                  'posed_path_aliases': sum(key[:2] == AVENUE_PATH for key in additions),
                  'filtered_models': sum(key[:2] == S3D for key in additions),
                  'props': sum(key[:2] == PROP for key in additions),
                  't21_bindings': sum(key[:2] == T21 for key in additions)},
              'canonical_model_zooms_preserved': 5 * len(cells), 'canonical_paths_preserved': len(cells),
              'canonical_shadows_preserved': 5 * len(cells), 'adaptive_cells': len(rows),
              'resources': [{'tgi': tgi_string(key),
                  'reference_sha256': sha(reference[key]) if key in reference else None,
                  'candidate_sha256': sha(candidate[key]) if key in candidate else None,
                  'status': 'unchanged' if key in retained else 'removed-network-exemplar' if key in removed else 'added-runtime-layer'}
                  for key in sorted(reference.keys() | candidate.keys())]}
    return report


def _payload(build, manifest):
    records = manifest['files']
    require(len(records) == len({record['path'] for record in records}), 'Repeated build payload path')
    result = {}
    for record in records:
        raw = safe_file(build, record['path']).read_bytes()
        require(len(raw) == record['bytes'] and sha(raw) == record['sha256'],
                'Saved DAT differs from its manifest: ' + record['path'])
        result[record['path']] = raw
    return result


def _restore_rul0(raw, overlay):
    record = overlay['rul0']
    suffix, insertion = record['suffix'].encode('latin1'), record['ordering_insertion'].encode('ascii')
    require(suffix and raw.endswith(suffix), 'Saved RUL0 does not retain its exact declared suffix')
    body = raw[:-len(suffix)]
    require(insertion and body.count(insertion) == 1, 'Saved RUL0 Ordering insertion is not unique')
    restored = body.replace(insertion, b'', 1)
    require(sha(restored) == record['base_sha256'], 'Saved RUL0 does not restore its native baseline')
    return restored


def _document(build, manifest, relative):
    records = [item for item in manifest.get('documentation', []) if item['path'] == relative]
    require(len(records) == 1, 'Saved build omits or repeats the documented assembly plan')
    raw = safe_file(build, relative).read_bytes(); record = records[0]
    require(len(raw) == record['bytes'] and sha(raw) == record['sha256'],
            'Saved assembly plan differs from its manifest documentation fingerprint')
    return raw


def _restore_ini(raw, overlay):
    record = overlay['network_ini']; insertion = record['insertion'].encode('latin1')
    require(insertion and raw.count(insertion) == 1, 'Saved NetworkINI insertion is not unique')
    restored = raw.replace(insertion, b'', 1)
    require(sha(restored) == record['base_sha256'], 'Saved NetworkINI does not restore its native baseline')
    return restored


def _plan(scene):
    return {'coordinate_system': scene['coordinate_system'],
            'construction_rectangle_tiles': scene['construction_rectangle_tiles'],
            'traffic_policy': scene['traffic_policy'],
            'placements': [{'piece_id': placement['piece_id'], 'origin_m': placement['origin_m'],
                            'rotation_degrees_ccw': placement.get('rotation_degrees_ccw', placement.get('rotation_ccw_degrees', 0))}
                           for placement in scene['placements']]}


def compare_builds(build, reference, *, verify_candidate=True):
    """Audit the complete thirteen-type diamond against a frozen saved build."""
    build, reference = Path(build).resolve(), Path(reference).resolve()
    candidate_manifest_raw, reference_manifest_raw = (build / 'manifest.json').read_bytes(), (reference / 'manifest.json').read_bytes()
    candidate_manifest, reference_manifest = json.loads(candidate_manifest_raw), json.loads(reference_manifest_raw)
    verification = verify_build(build, write_report=False) if verify_candidate else None
    candidate_pieces = {piece['id']: piece for piece in candidate_manifest['pieces']}
    reference_pieces = {piece['id']: piece for piece in reference_manifest['pieces']}
    require(len(candidate_pieces) == len(reference_pieces) == 13
            and candidate_pieces.keys() == reference_pieces.keys(),
            'Adaptive diamond and reference must contain the same thirteen piece types')
    require(candidate_manifest['profile']['id'] == reference_manifest['profile']['id'],
            'Adaptive build changed the supported native profile identity')
    require(candidate_manifest['profile'] == reference_manifest['profile'] or
            {record['filename']: record['sha256'] for record in reference_manifest['profile']['donors']}.items() <=
            {record['filename']: record['sha256'] for record in candidate_manifest['profile']['donors']}.items(),
            'Adaptive build changed a previously pinned native donor')
    candidate_files, reference_files = _payload(build, candidate_manifest), _payload(reference, reference_manifest)
    require(candidate_files.keys() == reference_files.keys(), 'Adaptive migration changed the payload DAT file set')
    reports = [compare_piece_archive(reference_pieces[identifier], candidate_pieces[identifier],
                reference_files[reference_pieces[identifier]['asset_file']],
                candidate_files[candidate_pieces[identifier]['asset_file']]) for identifier in sorted(candidate_pieces)]
    changed = [report for report in reports if report['adaptive_cells']]
    require(len(changed) == 3 and sum(report['adaptive_cells'] for report in changed) == 15,
            'Diamond migration must affect exactly three member types and fifteen Avenue cells')
    require(sum(report['added_runtime_resources'] for report in reports) == 357
            and sum(report['removed_network_exemplars'] for report in reports) == 15,
            'Diamond runtime resource difference must be exactly 357 additions and 15 omissions')
    require(sum(report['dat_byte_identical'] for report in reports) == 10,
            'All ten unconverted component DATs must remain byte-identical')
    folder = candidate_manifest['plugin_folder']
    require(folder == reference_manifest['plugin_folder'], 'Managed plugin identity changed')
    menu_path, controller_path = f'{folder}/10_SCP_Menu.dat', f'{folder}/00_SCP_Controller_NAM50.dat'
    require(candidate_files[menu_path] == reference_files[menu_path], 'The original thirteen-button menu DAT changed')
    menu_resources = strict_dbpf(reference_files[menu_path])
    candidate_controller, reference_controller = strict_dbpf(candidate_files[controller_path]), strict_dbpf(reference_files[controller_path])
    require(set(reference_controller) == {RUL0, NETWORK_INI}
            and set(candidate_controller) == {RUL0, NETWORK_INI, RUL1},
            'Controller migration must add only the declared RUL1 resource')
    native_rul0 = _restore_rul0(reference_controller[RUL0], reference_manifest['overlay'])
    require(_restore_rul0(candidate_controller[RUL0], candidate_manifest['overlay']) == native_rul0,
            'Adaptive RUL0 changed native construction bytes')
    native_ini = _restore_ini(reference_controller[NETWORK_INI], reference_manifest['overlay'])
    require(_restore_ini(candidate_controller[NETWORK_INI], candidate_manifest['overlay']) == native_ini
            and candidate_controller[NETWORK_INI] == reference_controller[NETWORK_INI],
            'Adaptive migration changed original NetworkINI or shadow mappings')
    rul1 = candidate_manifest['overlay']['rul1']; insertion = rul1['insertion'].encode('ascii'); offset = rul1['insertion_offset']
    require(candidate_controller[RUL1][offset:offset + len(insertion)] == insertion,
            'Adaptive RUL1 does not contain its exact declared insertion')
    native_rul1 = candidate_controller[RUL1][:offset] + candidate_controller[RUL1][offset + len(insertion):]
    require(sha(native_rul1) == rul1['base_sha256'], 'Adaptive RUL1 does not restore its declared native baseline')
    candidate_scene_raw = _document(build, candidate_manifest, SCENE)
    reference_scene_raw = _document(reference, reference_manifest, SCENE)
    candidate_scene, reference_scene = jsonc.loads(candidate_scene_raw.decode()), jsonc.loads(reference_scene_raw.decode())
    require(_plan(candidate_scene) == _plan(reference_scene), 'Assembly placements, traffic policy, or coordinate plan changed')
    candidate_owners, candidate_poses = check_owned_cells(candidate_pieces, candidate_scene)
    reference_owners, reference_poses = check_owned_cells(reference_pieces, reference_scene)
    require(candidate_owners == reference_owners and candidate_poses == reference_poses
            and len(candidate_owners) == 53 and len(candidate_poses) == 15,
            'Assembly no longer preserves its exact 53-cell, fifteen-placement ownership')
    counts, added_counts = Counter(), Counter()
    for report in reports:
        for key in ('unchanged_resources', 'canonical_resources_preserved', 'canonical_model_zooms_preserved',
                    'canonical_paths_preserved', 'canonical_shadows_preserved', 'added_runtime_resources',
                    'removed_network_exemplars'):
            counts[key] += report[key]
        added_counts.update(report['added_resource_counts'])
    reference_count = sum(report['reference_resources'] for report in reports) + 2 + len(menu_resources)
    candidate_count = sum(report['candidate_resources'] for report in reports) + 3 + len(menu_resources)
    require(candidate_count - reference_count == 343, 'Complete package resource difference is not 343')
    return {'schema_version': 1, 'subject_id': SUBJECT, 'preservation_checks_passed': True,
            'candidate_saved_verification_passed': verification is not None and verification['static_checks_passed'],
            'source': {'candidate_build': build.name, 'reference_build': reference.name,
                       'candidate_manifest_sha256': sha(candidate_manifest_raw), 'reference_manifest_sha256': sha(reference_manifest_raw),
                       'candidate_scene_sha256': sha(candidate_scene_raw), 'reference_scene_sha256': sha(reference_scene_raw)},
            'piece_types': 13, 'unchanged_asset_dats': 10, 'adaptive_asset_dats': 3,
            'assembly_owned_cells': 53, 'assembly_placements': 15, 'preserved': dict(counts),
            'added_runtime_layers': dict(added_counts),
            'controller': {'reference_resources': 2, 'candidate_resources': 3,
                           'native_rul0_sha256': sha(native_rul0), 'native_network_ini_sha256': sha(native_ini),
                           'native_rul1_restored_to_declared_sha256': sha(native_rul1),
                           'original_menu_dat_sha256': sha(reference_files[menu_path]),
                           'original_menu_dat_preserved': True,
                           'resources': [{'tgi': tgi_string(key),
                               'reference_sha256': sha(reference_controller[key]) if key in reference_controller else None,
                               'candidate_sha256': sha(candidate_controller[key])}
                               for key in sorted(candidate_controller)]},
            'menu': {'unchanged_resources': len(menu_resources),
                     'resource_hashes': {tgi_string(key): sha(raw) for key, raw in sorted(menu_resources.items())}},
            'resource_counts': {'reference': reference_count, 'candidate': candidate_count,
                                'net_change': candidate_count - reference_count},
            'files': [{'path': name, 'reference_sha256': sha(reference_files[name]),
                       'candidate_sha256': sha(candidate_files[name]),
                       'byte_identical': reference_files[name] == candidate_files[name]} for name in sorted(candidate_files)],
            'pieces': reports, 'game_behavior_tested': False,
            'coverage_limit': 'Direct saved-byte preservation against the named fixed-model baseline; candidate resource verification runs separately from game placement, Avenue redraw, sidewalk selection, traffic, and save/reload. Assembly route reachability and pavement/support checks belong to verify_compact_assembly.py.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--reference', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = compare_builds(args.build, args.reference)
    raw = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(raw)
        print(json.dumps({key: report[key] for key in
            ('subject_id', 'preservation_checks_passed', 'candidate_saved_verification_passed',
             'piece_types', 'unchanged_asset_dats', 'adaptive_asset_dats', 'assembly_owned_cells',
             'assembly_placements', 'preserved', 'added_runtime_layers', 'resource_counts', 'game_behavior_tested')}, indent=2))
    else:
        print(raw, end='')


if __name__ == '__main__':
    main()
