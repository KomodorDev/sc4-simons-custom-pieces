"""Independently verify the directed counterpart of the original frozen Y.

Expected routes are reconstructed from the immutable original source, without
importing reversed source or geometry writers. Physical ownership is accepted
only after an explicit independent review of the new native-phase model mask.
"""
from copy import deepcopy
import hashlib
import math
from pathlib import Path

from scp import jsonc
from scp.dbpf import decompress, require
from scp.track_paths import PATH
from scp.verify import parse_paths
from . import y_junction_verify as shared

ROOT = Path(__file__).resolve().parents[4]
ORIGINAL = ROOT/'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction'
SUBJECT = ROOT/'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction-reversed'
ORIGINAL_GEOMETRY_SHA256 = '8857eae50b01d3f5c15c5b47b43319de0e72c733d5cf331bb29e14f27af6d9b3'
ORIGINAL_REVIEW_SHA256 = 'ee77cc626e5fff20950fa86e477e2cef4eb412cb5aa01650a800b65cfacd5557'
NAMES = shared.NAMES
KEYS = ('y-reversed-diagonal-stem-split', 'y-reversed-diagonal-branch', 'y-reversed-orthogonal-core')
PIECE_IDS = tuple('ddrhw-'+key for key in KEYS)
RECIPES = tuple('highway_ddrhw_'+key.replace('-', '_') for key in KEYS)
POSITION_EPS = shared.POSITION_EPS
# Independently decoded all 21 nonempty new-phase S3D owners, including the
# source-only C south fringe, before freezing this explicit expected mask.
# Mask acceptance supplies no native-seam or complete physical acceptance.
REVIEWED_OWNED_WORLD_CELLS = (
    ((-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (-1, 2), (0, 2), (-1, 3)),
    ((-1, -3), (-1, -2), (0, -2), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1)),
    ((-1, 0), (0, 0), (1, 0), (2, 0), (3, 0)),
)
ORIGINAL_DAT_SHA256 = {
    'ddrhw-y-diagonal-stem-split': '6892d4ce98c569738fa186f902619eb34732f34f5be2c5f90acce3747a7c4a1f',
    'ddrhw-y-diagonal-branch': 'f245e4701d3959b2ab39a426e9bccef23ceafd1a0fa28f7a0373674ab3561e8d',
    'ddrhw-y-orthogonal-core': '584ebb51dd1c199968a1a349ef928813ecf8bc039e9463ca091fa7e290a573fc',
}


def independent_source():
    """Reconstruct only the expected directed routes and endpoint metadata."""
    raw = (ORIGINAL/'evidence/design-geometry.jsonc').read_bytes()
    review_raw = (ORIGINAL/'evidence/source-verification.jsonc').read_bytes()
    require(hashlib.sha256(raw).hexdigest() == ORIGINAL_GEOMETRY_SHA256
            and hashlib.sha256(review_raw).hexdigest() == ORIGINAL_REVIEW_SHA256,
            'Reversed Y original source or independent review changed')
    original, review = jsonc.loads(raw.decode()), jsonc.loads(review_raw.decode())
    require(review.get('passed') is True
            and review['source']['design_geometry_sha256'] == ORIGINAL_GEOMETRY_SHA256,
            'Reversed Y original source lacks its frozen independent review')
    routes, metadata = {}, {}
    for name in NAMES:
        opposite = name[2]+'-'+name[0]
        routes[name] = deepcopy(original['routes'][opposite][::-1])
        old = original['route_metadata'][opposite]
        metadata[name] = {'from_arm': name[0], 'to_arm': name[2],
                         'from_deck': old['to_deck'], 'to_deck': old['from_deck'],
                         'from_lane': 1-old['to_lane'], 'to_lane': 1-old['from_lane'],
                         'engine_transport': 1, 'compatibility': 0}
    return {'routes': routes, 'route_metadata': metadata}


def check_source_candidate():
    """Compare the submitted source with frozen reversal and actual natives."""
    raw = (SUBJECT/'evidence/design-geometry.jsonc').read_bytes()
    actual = jsonc.loads(raw.decode())
    expected = independent_source()
    require(actual.get('variant') == 'reversed' and actual.get('routes') == expected['routes']
            and actual.get('route_metadata') == expected['route_metadata'],
            'Reversed Y candidate differs from complete frozen-route reversal or native lane-class swap')
    native_raw = (SUBJECT/'evidence/native-design-inputs.jsonc').read_bytes()
    native = jsonc.loads(native_raw.decode())
    require(native.get('variant') == 'reversed', 'Reversed Y requires its own fresh native measurement')
    expected_modules = {'y_junction_reversed_native_models.py', 'y_junction_native_models.py',
                        'y_junction_reversed_approaches.py', 'y_junction_approaches.py'}
    require(set(native.get('source_module_sha256', {})) == expected_modules
            and all(hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest() == digest
                    for name, digest in native['source_module_sha256'].items()),
            'Reversed native measurements are stale relative to their four source readers')
    arms = {row['arm']: row for row in native['arms']}
    require(set(arms) == {'A', 'B', 'C'}, 'Reversed Y native report omits an arm')
    helpers = {'A': [0x57530200, 0, [-2, 2]], 'B': [0x57530200, 3, [-2, -2]],
               'C': [0x57530000, 1, [4, 0]]}
    matched, route_reports = set(), []
    for arm, row in arms.items():
        require(row['helper'] == helpers[arm] and len(row['members']) == 4,
                'Reversed Y native helper pose or four-member boundary changed')
    for name in NAMES:
        points, meta = expected['routes'][name], expected['route_metadata'][name]
        for incoming, index, adjacent in ((True, 0, 1), (False, -1, -2)):
            arm = name[0] if incoming else name[2]
            point = points[index]
            delta = [(points[adjacent][k]-point[k]) if incoming else (point[k]-points[adjacent][k])
                     for k in range(3)]
            length = math.sqrt(sum(value*value for value in delta))
            tangent = [value/length for value in delta]
            lane = meta['from_lane' if incoming else 'to_lane']
            direction = 'native-to-core' if incoming else 'core-to-native'
            members = [(i, member) for i, member in enumerate(arms[arm]['members'])
                       if member['lane'] == lane and member['direction'] == direction
                       and member['transport'] == 1 and member['compatibility'] == 0
                       and math.dist(member['point_enh_m'], point) <= POSITION_EPS
                       and math.dist(member['travel_tangent_enh'], tangent) <= POSITION_EPS]
            require(len(members) == 1 and (arm, members[0][0]) not in matched,
                    'Reversed Y endpoint fails its fresh native position, lane class, direction, or tangent')
            matched.add((arm, members[0][0]))
        grades = [(b[2]-a[2])/math.dist(a[:2], b[:2]) for a, b in zip(points, points[1:])]
        require(max(map(abs, grades)) <= .3+1e-9 and max(grades) <= 1e-12,
                'Reversed Y must retain level or descending travel within thirty percent')
        if name in ('B-C', 'C-B'):
            require(points[0][2] == 15. and points[-1][2] == 7.5 and min(grades) < -.2,
                    'Reversed branch-to-branch route does not descend from L2 to L1')
        route_reports.append({'journey': name, 'source_points_checked': len(points),
                              'minimum_signed_grade_percent': 100.*min(grades),
                              'maximum_signed_grade_percent': 100.*max(grades)})
    require(len(matched) == 12, 'Reversed Y source does not consume all twelve fresh native members')
    return {'schema_version': 1, 'passed': True,
            'scope': 'Independent frozen-polyline reversal, descending grades, and fresh native endpoint matching only; physical model acceptance and game observations remain separate.',
            'source': {'design_geometry_sha256': hashlib.sha256(raw).hexdigest(),
                       'native_measurements_sha256': hashlib.sha256(native_raw).hexdigest(),
                       'original_geometry_sha256': ORIGINAL_GEOMETRY_SHA256,
                       'original_independent_review_sha256': ORIGINAL_REVIEW_SHA256},
            'complete_directed_journeys': 6, 'fresh_native_members_checked': 12,
            'routes': route_reports, 'original_source_bytes_changed': False,
            'physical_model_mask_accepted': False, 'game_operation_tested': False}


def write_source_review():
    report = check_source_candidate()
    path = SUBJECT/'evidence/source-verification.jsonc'
    header = ('// title: "Independent reversed DD RHW Y directed-source review"\n'
              '// summary: "Check exact reversal of frozen original polylines, signed descending grades, and all twelve freshly measured native members."\n'
              '// Used when: Accepting directed source inputs before independently checking actual reversed saved models.\n'
              '// Read by: The reversed PATH verifier and integration coordinator.\n'
              '// Updated by: y_junction_reversed_verify.write_source_review() after the exact source and native measurements pass.\n'
              '// Affects: Directed source acceptance only; no physical mask, saved DAT, installation, or human game pass.\n')
    path.write_text(jsonc.document(report, source=path.read_text() if path.exists() else header))
    return report


def _source():
    report = check_source_candidate()
    review = jsonc.load(SUBJECT/'evidence/source-verification.jsonc')
    require(review.get('passed') is True and review.get('source') == report['source'],
            'Reversed source or native measurements changed after independent review')
    return independent_source()


def _configuration():
    require(len(REVIEWED_OWNED_WORLD_CELLS) == 3,
            'Reversed physical model mask awaits independent review; original ownership is not inherited')
    return shared.RouteVariantConfig(KEYS, PIECE_IDS, RECIPES, REVIEWED_OWNED_WORLD_CELLS, _source)


def _key(piece):
    return shared._key(piece, variant=_configuration())


def _spec(piece):
    return shared._spec(piece, variant=_configuration())


def _intrinsic_runs(piece):
    return shared._intrinsic_runs(piece, variant=_configuration())


def expected_cell_routes(piece):
    return shared.expected_cell_routes(piece, variant=_configuration())


def reviewed_contract(piece):
    return shared.reviewed_contract(piece, variant=_configuration())


def reviewed_facts(piece):
    return shared.reviewed_facts(piece, variant=_configuration())


def check_paths(resources, piece):
    report = shared.check_paths(resources, piece, variant=_configuration())
    grades = []
    for tile in piece['tile_ids']:
        for row in parse_paths(decompress(resources[*PATH, int(tile, 16)]))['routes']:
            grades.extend(100.*(b[2]-a[2])/math.dist(a[:2], b[:2])
                          for a, b in zip(row['points'], row['points'][1:]))
    require(grades and max(grades) <= 1e-6, 'Reversed saved travel contains an upward car segment')
    return {**report, 'minimum_signed_grade_percent': min(grades),
            'maximum_signed_grade_percent': max(grades), 'variant': 'reversed'}


def check_construction_fields(fields, piece, resources):
    from .y_junction_reversed_approaches import check_construction_approaches
    return shared.check_construction_fields(fields, piece, resources, variant=_configuration(),
                                            native_checker=check_construction_approaches)


def check_models(resources, piece, donors=None):
    from .y_junction_reversed_models_verify import check_models as inspect_models
    return inspect_models(resources, piece, donors)


def check_assembly(pieces, resources_by_id, scene, donors=None):
    return shared.check_assembly(pieces, resources_by_id, scene, donors, variant=_configuration())


def check_dat_byte_invariance(before, after):
    require(set(before) == set(after) == set(ORIGINAL_DAT_SHA256),
            'Original Y invariance requires all three distinct original DATs')
    require(all(before[key] == after[key] for key in before), 'An original Y DAT changed while adding the reversed variant')
    return {'original_DATs_byte_identical': 3, 'compared_bytes': sum(map(len, before.values()))}


def check_original_dat_invariance(before, after):
    require(all(hashlib.sha256(before[key]).hexdigest() == digest
                for key, digest in ORIGINAL_DAT_SHA256.items() if key in before),
            'Original Y DAT baseline differs from its accepted installed bytes')
    return check_dat_byte_invariance(before, after)


_rotate = shared._rotate
