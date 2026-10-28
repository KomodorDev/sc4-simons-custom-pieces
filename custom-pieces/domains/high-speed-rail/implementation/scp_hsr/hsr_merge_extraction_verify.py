"""Independent saved-resource guard for the approved one-plus-four merge split.

Frozen public fingerprints describe the accepted pre-extraction build. The
guard runs before current-resource capture and never reads an old DAT or a
geometry writer. Only the replacement straight and its western merge seam
may change models; every train route and support remains fixed in the city.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath

from scp.dbpf import require
from scp.track_paths import _parse_paths
from scp.subject_identity import canonical_subject_id
from .hsr_trumpet_verify import rotate

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.jsonc').is_file())
HISTORY = ROOT/'domains/high-speed-rail/01_assemblies/hsr-trumpet-straight-stem/evidence/design-history'
FROZEN_FILES = {
    'checks-resources-before-merge-west-tail-extraction.json': '3becf81758cceaf522820038640e73127ac3180291a5e38f592b83c5c439bf8c',
    'checks-layout-before-merge-west-tail-extraction.json': '2b149a52ed2c04c0bf3628f4c91189a48d906da7ae295d0878d3aa05db5d9976',
    'assembly-before-merge-west-tail-extraction.json': '57e520ee5e54e5e46a72a696d4d657afd4b53ea564a580f9140bcd1741ff5ace',
}
MERGE_ID = 'hsr-l2-two-track-mainline-opposed-merges-oblique-cuts'
STRAIGHT_ID = 'hsr-l2-two-track-straight'
REPLACEMENT = (32., 0.)
SEAM = (48., 0.)
SUPPORTS_SHA256 = '76d116a6f8cb5d6e48ab681dd679eb8d67bb137c2badb72943290d0860b82d1d'
# Frozen from the independent transformation of saved cell 7f585100 before
# the candidate build; accepting a candidate cannot supply this expected hash.
SEAM_MODEL_SHA256 = '59e736b92ef86c5cd6d0e69e94b5e93bc84bb09b832d906353ae685346e391c0'


def canonical_sha256(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def _piece_id(identifier):
    """Translate only a declared piece identity, never a recipe or resource hash."""
    return canonical_subject_id(identifier, kind='piece', root=ROOT)


def _archive_identity(filename, identifier):
    """Translate an exact owned DAT basename without changing its parent path."""
    path = PurePosixPath(filename)
    current = _piece_id(identifier)
    for prefix in ('', 'SCP_'):
        if path.name == prefix + identifier + '.dat':
            return path.with_name(prefix + current + '.dat').as_posix()
    return filename


def frozen_baseline(directory=HISTORY):
    """Reject edited historical facts even if current resources are recaptured."""
    values = {}
    for name, digest in FROZEN_FILES.items():
        raw = (Path(directory)/name).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == digest,
                'Merge extraction frozen baseline differs: '+name)
        values[name] = json.loads(raw)
    return values['checks-resources-before-merge-west-tail-extraction.json']


def _resource_hashes(tile):
    return {name: hashlib.sha256(raw).hexdigest() for name, raw in tile['resources'].items()}


def audit_world_resources(tiles, baseline):
    """Allow reindexed retained cells, never changed resources outside two cells."""
    expected = {tuple(cell['world_east_north_m']): cell for cell in baseline['world_cells']}
    require(len(expected) == len(baseline['world_cells']) == 105 and set(tiles) == set(expected),
            'Merge extraction changes the 105 occupied world cells')
    for position, record in expected.items():
        tile = tiles[position]
        hashes = _resource_hashes(tile)
        require(set(hashes) == set(record['resources_sha256']),
                'Merge extraction changes a world-cell resource inventory')
        if position == REPLACEMENT:
            require(_piece_id(tile['piece_id']) == STRAIGHT_ID and tuple(tile['cell']) == (0, 0)
                    and tile['rotation'] == 3 and tile['instance_id'] == 'P26',
                    'Merge extraction replacement must be the existing rotated P26 straight')
            standard = expected[(-112., 0.)]
            require(hashes == standard['resources_sha256'],
                    'Merge extraction replacement differs from the existing standard straight')
            continue
        require(_piece_id(tile['piece_id']) == _piece_id(record['piece_id'])
                and tile['rotation'] == record['rotation_quarter_turns_ccw'],
                'Merge extraction changes an unchanged world owner or rotation')
        cell = tuple(record['cell'])
        if _piece_id(record['piece_id']) == MERGE_ID:
            cell = (cell[0]-1, cell[1])
        require(tuple(tile['cell']) == cell,
                'Merge extraction changes the retained world-cell mapping')
        require(hashes['path'] == record['resources_sha256']['path'],
                'Merge extraction changes a retained saved PATH')
        if position != SEAM:
            require(hashes == record['resources_sha256'],
                    'Merge extraction changes resources outside the replacement and seam')
        else:
            require(all(hashes[f'shadow_{zoom}'] == record['resources_sha256'][f'shadow_{zoom}']
                        for zoom in range(5)), 'Merge extraction changes a retained seam shadow')
    return {'occupied_world_cells_preserved': 105, 'unchanged_world_cells_all_resources_exact': 103,
            'retained_world_path_bytes_identical': 104,
            'model_shadow_change_world_cells_en_m': [list(REPLACEMENT), list(SEAM)]}


def audit_replacement_paths(tile):
    """Compare decoded flow and every saved coordinate, independent of comments."""
    signatures = []
    for route in _parse_paths(tile['resources']['path']):
        points = []
        for point in route['points']:
            east, north, height = rotate(point, tile['rotation'])
            points.append((east+32., north, height))
        signatures.append((route['transport'], route['class'], (route['entry']-tile['rotation']) % 4,
                           (route['exit']-tile['rotation']) % 4, route['junction'], tuple(points)))
    expected = [
        (7, 0, 0, 2, 0, ((24., -2., 15.5), (40., -2., 15.5))),
        (7, 0, 2, 0, 0, ((40., 2., 15.5), (24., 2., 15.5))),
    ]
    require(sorted(signatures) == expected,
            'Merge extraction changes the replacement world PATH geometry or direction')
    return {'replacement_decoded_routes_identical': 2, 'every_world_path_geometry_preserved': True}


def audit_unchanged_archives(build, baseline):
    """Changing the merge must not silently rebuild the twelve other archives."""
    old = {_piece_id(piece['id']): piece for piece in baseline['pieces']}
    current = {_piece_id(identifier): piece for identifier, piece in build['pieces'].items()}
    require(len(old) == len(baseline['pieces']) and len(current) == len(build['pieces'])
            and set(current) == set(old), 'Merge extraction changes the thirteen retained types')
    for identifier, record in old.items():
        piece = current[identifier]
        require(_piece_id(piece['id']) == identifier and piece['recipe'] == record['recipe']
                and _archive_identity(piece['asset_file'], piece['id'])
                == _archive_identity(record['asset_file'], record['id']),
                'Merge extraction changes a retained archive identity')
        if identifier == MERGE_ID:
            require(piece['cells'] == [[column, 0] for column in range(4)]
                    and piece['tile_ids'] == [f'7f585{column}00' for column in range(1, 5)],
                    'Merge extraction reassigns retained active cell resource IDs')
            continue
        raw = (Path(build['path'])/piece['asset_file']).read_bytes()
        require(len(raw) == record['bytes'] and hashlib.sha256(raw).hexdigest() == record['sha256'],
                'Merge extraction changes an unaffected archive: '+identifier)
    return {'unchanged_complete_archives_exact': 12, 'retained_merge_tile_resource_ids_unchanged': 4}


def audit_journeys_and_supports(journeys, supports, baseline):
    expected = {tuple(row['movement']): row for row in baseline['journeys']}
    require(len(expected) == len(baseline['journeys']) == 6 and set(journeys) == set(expected),
            'Merge extraction changes the six complete assembly journeys')
    for movement, points in journeys.items():
        record = expected[movement]
        require(len(points) == record['encoded_points'] and canonical_sha256(points) == record['points_sha256'],
                'Merge extraction changes a complete assembly journey: '+str(movement))
    normalized = sorted([round(float(east), 6), round(float(north), 6)] for east, north in supports)
    require(len(normalized) == len({tuple(point) for point in normalized}) == 74
            and canonical_sha256(normalized) == SUPPORTS_SHA256,
            'Merge extraction changes the seventy-four support positions')
    return {'complete_journey_counts_and_point_hashes_identical': 6,
            'support_positions_preserved': 74, 'support_positions_sha256': SUPPORTS_SHA256}


def audit_collar_sections(triangles):
    """Reject new slab or parapet cracks at fixed stations across the collar.

    A two-micrometre interval gap tolerance detects cracks independently of
    the looser fifty-micrometre native profile position tolerance. This is a
    finite section check; the separately frozen model hash binds the complete
    independently inspected saved model, including surfaces between stations.
    """
    from .hsr_atomic_components_verify import _section_intervals

    triangles = list(triangles)
    stations = sorted({40.+index*.1 for index in range(26)}
                      | {40.+.00000075, 42.5-.000001, 42.5+.000001})
    for station in stations:
        for height in (14.01067, 16.189326, 16.98933):
            actual = _section_intervals(triangles, 'east', station, height, 0., merge_gap_m=.000002)
            if height < 16.5:
                valid = (len(actual) == 1 and abs(actual[0][0]+7.5) <= .00005
                         and abs(actual[0][1]-7.5) <= .00005)
            else:
                valid = (len(actual) == 2
                         and abs(actual[0][0]+7.5) <= .00005
                         and abs(actual[0][1]+5.9965477) <= .00005
                         and 5.9965477-.00005 <= actual[1][0] <= 6.+.00005
                         and abs(actual[1][1]-7.5) <= .00005)
            require(valid, f'Merge extraction collar has a gap or invalid profile at east {station}, height {height}')
    return {'collar_section_stations_checked': len(stations),
            'collar_horizontal_sections_checked': len(stations)*3,
            'collar_gap_tolerance_m': .000002,
            'collar_profile_position_tolerance_m': .00005}


def audit_native_seam(tiles):
    """Measure both actual saved sides of the new join and pin its bounded edit."""
    from .assembly_inspection import _world_triangles
    from .hsr_atomic_components_verify import _section_intervals

    require(isinstance(SEAM_MODEL_SHA256, str) and len(SEAM_MODEL_SHA256) == 64,
            'Merge extraction needs independently frozen normalized seam geometry')
    for zoom in range(5):
        require(hashlib.sha256(tiles[SEAM]['resources'][f'model_{zoom}']).hexdigest() == SEAM_MODEL_SHA256,
                'Merge extraction seam differs from its independently bounded normalization')
    for position, station in ((REPLACEMENT, 40.-.00000075), (SEAM, 40.+.00000075)):
        triangles = list(_world_triangles(tiles, {position}))
        for height, expected in ((16.189326, [(-7.5, 7.5)]), (14.01067, [(-7.5, 7.5)]),
                                 (16.98933, [(-7.5, -5.9965477), (5.9965477, 7.5)])):
            actual = _section_intervals(triangles, 'east', station, height, 0.)
            require(len(actual) == len(expected) and all(
                abs(a-c) <= .00005 and abs(b-d) <= .00005
                for (a, b), (c, d) in zip(actual, expected)),
                'Merge extraction native joining profile differs')
    collar = audit_collar_sections(_world_triangles(tiles, {SEAM}))
    return {'actual_native_joining_sections_checked': 6, 'native_profile_tolerance_m': .00005,
            'seam_model_zooms_pinned_to_bounded_edit': 5, 'seam_model_sha256': SEAM_MODEL_SHA256,
            'normalization_collar_world_east_m': [40., 42.5],
            'maximum_authorized_parapet_change_m': .0034524, **collar}


def audit_merge_extraction(tiles, build, journeys, supports):
    """Check accepted old facts before any new resource hashes can be captured."""
    baseline = frozen_baseline()
    report = audit_world_resources(tiles, baseline)
    report.update(audit_replacement_paths(tiles[REPLACEMENT]))
    report.update(audit_unchanged_archives(build, baseline))
    report.update(audit_journeys_and_supports(journeys, supports, baseline))
    report.update(audit_native_seam(tiles))
    return {'status': 'passed', 'baseline_resource_archives_required': False,
            'manual_or_game_observations_added': 0, **report}
