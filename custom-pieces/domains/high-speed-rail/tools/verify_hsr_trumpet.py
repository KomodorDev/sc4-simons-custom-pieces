#!/usr/bin/env python3
"""Audit the current trumpet directly against approved resource fingerprints.

Every current DAT, placed tile model/PATH/shadow, orientation and complete
journey is pinned exactly. Independent physical audits then check all ports,
travel directions, native joins, rotations, clearances, supports and budgets.
Historical atomization decisions retain their original frozen evidence. The
current integration binds its separate pre-integration source snapshot; actual
predecessor DAT archives are not required for current physical acceptance.
This tool never installs files or records observations inside the game.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from copy import deepcopy
import json
import math
import os
import tempfile
from pathlib import Path
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'project.json').is_file())
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/high-speed-rail/implementation')]

from scp.dbpf import require, entries
from scp.verification_fixtures import resource_descriptor, verification_resources
from scp_hsr.directional_t_verify import _journeys, audit_visible_rails, _TURN_LIMITS
from scp_hsr.hsr_components_verify import CONTRACTS, verify_component
from scp_hsr.hsr_mesh_verify import audit_crossings, measure_journey_quality
from scp_hsr.hsr_trumpet_verify import CONTRACT, direct_slip_symmetry, key, physical_layout, rotate, split_flags
from scp_hsr.interchange_verify import _graph, _clearance_segments
from scp_hsr.assembly_inspection import encoded_records, load_build, number, placements, rotation, sha256, triangle_count, world_tiles, _world_triangles
from scp_hsr.hsr_compact_fan_verify import audit_bed_corridors
from scp_hsr.hsr_merge_extraction_verify import audit_merge_extraction
from scp_hsr.hsr_trumpet_border_verify import (
    SNAPSHOT_RELATIVE, SNAPSHOT_INDEX_SHA256, STANDALONE_REVISIONS_SHA256, CURRENT_TILE_TRIANGLES,
    frozen_inputs as frozen_border_inputs, audit_source_inputs, expected_archives,
    integration_policy, audit_border_scope, audit_current_native_seam,
    audit_preserved_current_journeys, read_border_integration_record, CURRENT_INTEGRATION_LAYOUT,
    CORE_ID, STRAIGHT_ID as RECESSED_STRAIGHT_ID, expected_current_placements,
    FULL_FAN_ID, audit_parent_retirement,
    prove_current_removed_structural_cells, audit_current_removed_cell_evidence, audit_current_route_movement,
)
from scp_hsr.hsr_trumpet_rework_verify import (CURRENT_LAYOUT, ALLOWED_CELLS, REWORKED_SOURCES,
    read_rework_record, audit_redesign_scope, audit_target_joins, audit_preserved_journeys, audit_redesign_supports, audit_removed_cell_evidence, prove_removed_structural_cells, audit_route_movement, audit_matching_route_movement)

ASSEMBLY = ROOT/'domains/high-speed-rail/01_assemblies/straight-stem-trumpet'
SCENE = ASSEMBLY/'assembly.json'
QUALITY_PATH = ASSEMBLY/'checks/contract.json'
RESOURCES_PATH = ASSEMBLY/'checks/resources.json'
REWORK_PATH = ASSEMBLY/'checks/junction-rework.json'
INTEGRATION_PATH = ASSEMBLY/'checks/border-piece-integration.json'
HISTORICAL_RESOURCES_PATH = ASSEMBLY/SNAPSHOT_RELATIVE/'checks/resources.json'
FROZEN_REWORK_SHA256 = 'fd260acf137b4d690ec111aef4edf747cc0eb0b7f75155bf61c81fd4843d85dc'
STRAIGHT_ID = 'hsr-component-lower-paired-straight'
ONEWAY_ID = 'hsr-component-lower-oneway-straight'
NEW_IDS = frozenset({
    'hsr-component-l2-short-mainline-diverge-core', 'hsr-component-l2-short-opposed-merge-core',
    'hsr-component-l2-shortened-departure-curve', 'hsr-component-l2-shortened-return-curve',
})
CURRENT_IDS = NEW_IDS | frozenset({
    CORE_ID, RECESSED_STRAIGHT_ID,
    'hsr-component-lower-paired-straight', 'hsr-component-lower-oneway-straight',
    'hsr-component-modular-south-junction', 'hsr-component-modular-paired-climb',
    'hsr-component-modular-crossing-core', 'hsr-component-upper-paired-straight',
    'hsr-component-tight-paired-curve90-l4-to-mid', 'hsr-component-tight-paired-curve90-mid-to-l2',
})
REPLACEMENTS = {
    (-112., 0.): (STRAIGHT_ID, 3), (112., 0.): (STRAIGHT_ID, 3),
    (-16., -112.): (ONEWAY_ID, 2), (16., -112.): (ONEWAY_ID, 0),
}
ELIGIBLE_CANDIDATES = {
    'p01a-west-tail': ({(-112., 0.), (-96., 0.)},
                       'hsr-component-l2-short-mainline-diverge-core', STRAIGHT_ID, 270, .0245),
    'p03b-east-tail': ({(96., 0.), (112., 0.)},
                       'hsr-component-l2-short-opposed-merge-core', STRAIGHT_ID, 270, .0245),
    'p01b-south-tail': ({(-16., -112.), (-16., -96.)},
                        'hsr-component-l2-shortened-departure-curve', ONEWAY_ID, 180, .0082),
    'p03d-south-tail': ({(16., -112.), (16., -96.)},
                        'hsr-component-l2-shortened-return-curve', ONEWAY_ID, 0, .0082),
}


# Preserve the original meaning of all seven standalone source decisions.
# Current whole-assembly integration is a separate completed record; it never
# rewrites their historical deferred statuses or earlier redesign authorization.
DIVERGE_PARAPET_REVISION = {
    'piece_id': 'hsr-component-l2-short-mainline-diverge-core',
    'source_file': 'domains/high-speed-rail/00_pieces/hsr-component-l2-short-mainline-diverge-core/geometry.json',
    'before_sha256': '7760cdba90db6e0b12959708faf677121a0f5913edae65ef83d524006004baa0',
    'after_sha256': '4ab1cb1c939a896800373840832be4dd02dc6b199a41f7831e18ee65cb3f1ca4',
    'preserved_geometry_semantic_sha256': '871c42775ee4315b47cfb7f97059a8fd3c35623f1b7525f1e0c0c5d338bed5b5',
    'only_added_geometry_property': 'south_parapet_alignment',
    'south_parapet_alignment': {
        'purpose': "Continue the raised left mainline border along the branch's dark ballast outline into the existing curved grey wing at the bottom of X2; retain the separate straight right end, rails, PATHs, supports, and original outer faces.",
        'left_branch': 'direct_west_south_curve',
        'left_inner_half_width_m': 2.6,
        'left_selection_limit_local_east_m': 32.,
        'right_local_east_cap_m': 43.776078282276934,
        'source_east_offset_m': 16.,
        'left_reference': 'Follow the southern branch inside parapet at 2.6 m from its centreline, from its intersection with the mainline inside face through the retained curved wing.',
        'right_reference': 'Northern branch outside edge (+4 m cross offset) at the mainline inside edge (5.996547698974609 m south).',
        'minimum_train_half_width_m': 2.5,
    },
    'standalone_evidence': {
        'evidence/parapet-alignment.json': '3f796a97d5ff2d317fdc0ffae6a184f695ee9e37a418d10cb2e24db505936eb2',
        'evidence/saved-resource-checks.json': '5eb889298f79e441e76c3390afe9c99102dfffebf63449ae55d6a8b7c5f556d0',
    },
    'superseded_attempt': {
        'status': 'software-checked/superseded-after-border-shape-clarification',
        'geometry_sha256': '4b0c7313fd3c7ece31aa43fca820cde4bb6ced03e95d4d1ba4604a230d800d51',
        'snapshot_directory': 'evidence/design-history/straight-cap-attempt',
        'index_sha256': '981c7c5aaf35f7d00e3ed3b5cd6f7f5b741f46bd8836ee5a791af5806325bdcb',
    },
    'status': 'standalone-verified/assembly-integration-deferred',
    'assembly_resource_pins_refreshed': False,
    'assembly_render_refreshed': False,
}
LATER_PARAPET_REVISIONS = ({'piece_id': 'hsr-component-modular-south-junction',
  'source_file': 'domains/high-speed-rail/00_pieces/hsr-component-modular-south-junction/geometry.json',
  'before_sha256': '72005262cfa843a3c380da08e5cab2f03106e3dce7b350b126b70ca5df595fdd',
  'after_sha256': 'd0c24a85209a56f0ac3e924b3f66e9ee291fd8362e65726c975b1033eaf3066a',
  'preserved_geometry_semantic_sha256': '01764d043bcf43d4b6630748e9a132ebed4ebc568f77a704fdd5da3fe7f0a6bb',
  'only_added_geometry_property': 'junction_wedge_alignment',
  'junction_wedge_alignment': {'purpose': 'Close the two visible triangular concrete gaps beside the '
                                          'recessed northern paired end, following the original branch '
                                          'ballast boundaries; preserve existing models, tracks, routes, '
                                          'supports, and identities.',
                               'left_branch': 'symmetric_fan_left',
                               'right_branch': 'symmetric_fan_right',
                               'branch_inner_half_width_m': 2.6,
                               'paired_centre_east_m': 16.0,
                               'recessed_end_local_south_m': 24.0,
                               'minimum_train_half_width_m': 2.5},
  'standalone_evidence': {'evidence/junction-wedge-alignment.json': 'a946a2856ff8fab56987eb1c2644979ae6385bfa6d59c07c8faaf0feb17d9511',
                          'evidence/saved-resource-checks.json': 'da4237702a6c65347939a91bd98ceb248750b8bc7bd40cf335e2c010189c31fd'},
  'before_piece_snapshot': {'geometry_sha256': '72005262cfa843a3c380da08e5cab2f03106e3dce7b350b126b70ca5df595fdd',
                            'snapshot_directory': 'evidence/design-history/missing-junction-wedges',
                            'index_sha256': '38a1af1432bdb54e78095d9d1227738b757662863475f4e2a6b0f207166823a5'},
  'status': 'standalone-verified/assembly-integration-deferred',
  'assembly_resource_pins_refreshed': False,
  'assembly_render_refreshed': False},
 {'piece_id': 'hsr-component-l2-paired-fan-compact-join',
  'source_file': 'domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-join/geometry.json',
  'before_sha256': 'd034aa453bfa95fb3a537736d12a40d0be427cbe59baffebf8f73424c7f7a090',
  'after_sha256': 'd5366120c1f9c38b8b1eccc7fc8927dabb6e28d8ba1dd08427ed4e0b1c74aa0b',
  'preserved_geometry_semantic_sha256': 'a021fb24b76304ca70e28478323e822913b15b9bc12f462947b1ffc0a874df2e',
  'only_added_geometry_property': 'central_parapet_alignment',
  'central_parapet_alignment': {'purpose': 'Close the missing central raised grey triangle between the '
                                           'existing tapered ballast outlines, continuing both inside '
                                           'faces into the retained separate fork walls.',
                                'reflection_axis_source_east_m': 96.0,
                                'inside_sides': {'native_y_left': 1, 'native_y_right': -1},
                                'minimum_train_half_width_m': 2.5,
                                'preservation': 'Keep all source route samples, taper settings, rails, '
                                                'ballast floor, undersides, supports, tile ownership, and '
                                                'resource identities unchanged.'},
  'standalone_evidence': {'evidence/central-parapet-alignment.json': '80638f599c9dc3ef5ba0ee5df75029d147a5615088acb1431938000e7e02f606',
                          'evidence/saved-resource-checks.json': 'e69c8a6a2fb71d9fedb483d31927b2b9ebe6a1d6c7055861504aedad333c20cb'},
  'before_piece_snapshot': {'geometry_sha256': 'd034aa453bfa95fb3a537736d12a40d0be427cbe59baffebf8f73424c7f7a090',
                            'snapshot_directory': 'evidence/design-history/before-central-parapet-repair',
                            'index_sha256': '49b3578b3c1a041eaf1a6ebcacf0b771380312fac263b2d4bafc1af4f4d2cdbb'},
  'status': 'standalone-verified/assembly-integration-deferred',
  'assembly_resource_pins_refreshed': False,
  'assembly_render_refreshed': False},
 {'piece_id': 'hsr-component-l2-short-opposed-merge-core',
  'source_file': 'domains/high-speed-rail/00_pieces/hsr-component-l2-short-opposed-merge-core/geometry.json',
  'before_sha256': '8bf5a7e8439a29017cc2d556695552ae98d0be9eaf4e550e6505a9ef30c6f7f8',
  'after_sha256': '3ad00c99b0d3eccf69c5113d426e3680f2d4a03bd9ecb27d5e79542b00e228c1',
  'preserved_geometry_semantic_sha256': '50cace339297dad171b9b03dfc94e8dc97b9e4f19221239d4fb2462536542cea',
  'only_added_geometry_property': 'opposed_parapet_alignment',
  'opposed_parapet_alignment': {'purpose': 'Continue both raised mainline borders along the existing '
                                           'branch ballast outlines into their retained curved wings, and '
                                           'close the separate opposite strips without changing tracks, '
                                           'supports, PATHs, or prior source contexts.',
                                'mainline': 'native_east_west_main',
                                'north_branch': 'native_y_left',
                                'south_branch': 'direct_south_east_merge',
                                'source_east_offset_m': 32.0,
                                'source_south_offset_m': 80.0,
                                'branch_inner_half_width_m': 2.6,
                                'mainline_half_width_m': 7.5,
                                'north_selection_limit_local_east_m': 32.0,
                                'south_selection_limit_local_east_m': 16.0,
                                'north_opposite_cap_local_east_m': 43.76798391999034,
                                'south_opposite_cap_local_east_m': 4.223921717723081,
                                'minimum_train_half_width_m': 2.5,
                                'raw_west_cell_sha256': 'eab267409283bcb38d6cd9adff9ad364100e2e06fdde8764fa2ea42695412605'},
  'standalone_evidence': {'evidence/parapet-alignment.json': '12fbe3436f8aa129d791e91adb0ca5b6830287f465e15e7d90744cb512dc51f1',
                          'evidence/saved-resource-checks.json': '1bffd0fc02b6d8a64b19f0b35aacb71e4e6e09903d1631c109341510d7056718'},
  'before_piece_snapshot': {'geometry_sha256': '8bf5a7e8439a29017cc2d556695552ae98d0be9eaf4e550e6505a9ef30c6f7f8',
                            'snapshot_directory': 'evidence/design-history/before-ballast-border-repair',
                            'index_sha256': '0ab9571c36279cce131e14f567202296e3dc79d6277cfccbaecf6116b3b27a76'},
  'status': 'standalone-verified/assembly-integration-deferred',
  'assembly_resource_pins_refreshed': False,
  'assembly_render_refreshed': False})


DIVERGE_SUCCESSOR_REVISIONS = ({'piece_id': 'hsr-component-l2-short-mainline-diverge-core',
  'source_file': 'domains/high-speed-rail/00_pieces/hsr-component-l2-short-mainline-diverge-core/geometry.json',
  'before_sha256': '4ab1cb1c939a896800373840832be4dd02dc6b199a41f7831e18ee65cb3f1ca4',
  'after_sha256': 'cba97aca000381fee6d99dce0e63cf35d6be467b57b4e4b0b2db82ef4001cd9c',
  'preserved_geometry_semantic_sha256': '871c42775ee4315b47cfb7f97059a8fd3c35623f1b7525f1e0c0c5d338bed5b5',
  'only_changed_geometry_property': 'south_parapet_alignment',
  'south_parapet_alignment': {'purpose': 'Preserve the accepted left ballast-following border and continue '
                                         'the right raised border into its existing curved wing along the '
                                         'branch inside outline; retain rails, PATHs, supports, and '
                                         'original outside contours.',
                              'left_branch': 'direct_west_south_curve',
                              'left_inner_half_width_m': 2.6,
                              'left_selection_limit_local_east_m': 32.0,
                              'source_east_offset_m': 16.0,
                              'left_reference': 'Follow the southern branch inside parapet at 2.6 m from '
                                                'its centreline, from its intersection with the mainline '
                                                'inside face through the retained curved wing.',
                              'right_reference': 'Continue the right concrete top and inside face along '
                                                 'the branch inside outline (+2.6 m cross offset), joining '
                                                 'its existing curved grey wing at the mainline outside '
                                                 'edge.',
                              'minimum_train_half_width_m': 2.5,
                              'right_inner_join_local_east_m': 40.361872522872716,
                              'right_outer_join_local_east_m': 43.669002829692054,
                              'right_inner_half_width_m': 2.6,
                              'right_join': 'continuous_branch_inside_outline'},
  'standalone_evidence': {'evidence/parapet-alignment.json': '334d9a98246e19ed9678716a8992343a9a466b5331a560141665689843de3ccd',
                          'evidence/saved-resource-checks.json': 'e4ba0e67558e74340272361a34fb8185fbdc76dd961514baa1bb238c793aaf18'},
  'before_piece_snapshot': {'geometry_sha256': '4ab1cb1c939a896800373840832be4dd02dc6b199a41f7831e18ee65cb3f1ca4',
                            'snapshot_directory': 'evidence/design-history/before-right-border-extension',
                            'index_sha256': 'c00d46028afafa7ba2cc5f4b1a1a0042f729aee6ddaf8a7c6708ed1bae1607f7'},
  'status': 'standalone-verified/assembly-integration-deferred',
  'assembly_resource_pins_refreshed': False,
  'assembly_render_refreshed': False},)


SYMMETRIC_STEM_SUCCESSOR_REVISIONS = ({'piece_id': 'hsr-component-modular-south-junction',
 'source_file': 'domains/high-speed-rail/00_pieces/hsr-component-modular-south-junction/geometry.json',
 'before_sha256': 'd0c24a85209a56f0ac3e924b3f66e9ee291fd8362e65726c975b1033eaf3066a',
 'after_sha256': 'fda2275ea4013c2e9333e3904fc8e5f96de483ce12982c7d45e2fc4d3485ef5e',
 'preserved_geometry_semantic_sha256': '081cb9770cf3d44f82947db73d46dc83feb65078989168614172184c54f20b35',
 'only_added_geometry_property': 'stem_parapet_alignment',
 'stem_parapet_alignment': {'purpose': 'Keep both southern paired borders straight until the first branch '
                                       'ballast outline, then follow that outline through the adjacent '
                                       'northern row; preserve the accepted recessed wedges and every '
                                       'original face, rail, route, support, and identity.',
                            'left_branch': 'symmetric_fan_left',
                            'right_branch': 'symmetric_fan_right',
                            'branch_inner_half_width_m': 2.6,
                            'paired_centre_east_m': 16.0,
                            'stem_scope_local_south_m': [48.0, 88.0],
                            'minimum_train_half_width_m': 2.5},
 'standalone_evidence': {'evidence/stem-parapet-alignment.json': '9cb68594306b1dee86bfc534562a7a390c9c06fdbc0f72cb9f1d51f9228fdf5e',
                         'evidence/saved-resource-checks.json': '2540c36e65f98f10f876a266abf3c8ba85e5f21c8e081bd8a560b7ea335e989f'},
 'before_piece_snapshot': {'geometry_sha256': 'd0c24a85209a56f0ac3e924b3f66e9ee291fd8362e65726c975b1033eaf3066a',
                           'snapshot_directory': 'evidence/design-history/before-stem-border-repair',
                           'index_sha256': 'cf8393df1f0aa2f5a4b9d8f4c3f8030607788b7cc97ad8828248371e0c1395f7'},
 'status': 'standalone-verified/assembly-integration-deferred',
 'assembly_resource_pins_refreshed': False,
 'assembly_render_refreshed': False},)

OPPOSED_SUCCESSOR_REVISIONS = ({'piece_id': 'hsr-component-l2-short-opposed-merge-core',
 'source_file': 'domains/high-speed-rail/00_pieces/hsr-component-l2-short-opposed-merge-core/geometry.json',
 'before_sha256': '3ad00c99b0d3eccf69c5113d426e3680f2d4a03bd9ecb27d5e79542b00e228c1',
 'after_sha256': '61083be80c1a6d067e4bd05e6434d5eb110b4485bd77452cfa671cad0cb9f6e9',
 'preserved_geometry_semantic_sha256': '50cace339297dad171b9b03dfc94e8dc97b9e4f19221239d4fb2462536542cea',
 'only_changed_geometry_property': 'opposed_parapet_alignment',
 'opposed_parapet_alignment': {'purpose': 'Preserve both accepted continuous inner banks and join the '
                                          'separate outer strips in X0 and X3 along their own native branch '
                                          'inside outlines into the retained curved wings; retain all '
                                          'tracks, floors, supports, PATHs, and prior collar behavior.',
                               'mainline': 'native_east_west_main',
                               'north_branch': 'native_y_left',
                               'south_branch': 'direct_south_east_merge',
                               'source_east_offset_m': 32.0,
                               'source_south_offset_m': 80.0,
                               'branch_inner_half_width_m': 2.6,
                               'mainline_half_width_m': 7.5,
                               'north_selection_limit_local_east_m': 32.0,
                               'south_selection_limit_local_east_m': 16.0,
                               'minimum_train_half_width_m': 2.5,
                               'raw_west_cell_sha256': '6449b8842ae2d90d39235960aa1b8a59e13fa6c7883f68a34f6e17888845d4e0',
                               'outer_join_mode': 'continuous_branch_inside_outline',
                               'north_opposite_inner_join_local_east_m': 40.361872522872716,
                               'north_opposite_outer_join_local_east_m': 43.65474068840744,
                               'south_opposite_inner_join_local_east_m': 7.638127477127277,
                               'south_opposite_outer_join_local_east_m': 4.330997170307948},
 'standalone_evidence': {'evidence/parapet-alignment.json': '7267688f247384e1b6e6d6f0b61f585895886a760af30686a812d7ada20f97fa',
                         'evidence/saved-resource-checks.json': 'db9ea281fce0c39c22c3e9cd3bcfd20b43ae2d7fb03b5411438013f65419db1e'},
 'before_piece_snapshot': {'geometry_sha256': '3ad00c99b0d3eccf69c5113d426e3680f2d4a03bd9ecb27d5e79542b00e228c1',
                           'snapshot_directory': 'evidence/design-history/before-outer-border-joins',
                           'index_sha256': 'f9aeaf66ef064e8e3f5d2e32fc84904002ca71649b3ca44a270e508930abe0d1'},
 'status': 'standalone-verified/assembly-integration-deferred',
 'assembly_resource_pins_refreshed': False,
 'assembly_render_refreshed': False},)

def canonical_sha256(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def read_frozen_rework_record(path=None):
    """Read the completed historical audit without certifying later models.

    The exact saved record retains its original source and compiled-resource
    bindings. Later standalone repairs have their own strict source chain;
    the ordinary current-build verifier still requires current geometry.
    """
    path = REWORK_PATH if path is None else Path(path)
    require(sha256(path.read_bytes()) == FROZEN_REWORK_SHA256,
            'Trumpet frozen completed redesign record fingerprint differs')
    record = read_rework_record(path, root=ROOT, require_completed=False)
    require(record.get('status') == 'passed' and record.get('compiled_audit'),
            'Trumpet frozen redesign record lacks its completed historical audit')
    return record


def audit_subsequent_piece_revisions(ledger, *, root=ROOT):
    """Check the exact later piece repair without accepting assembly resources.

    Hash the complete preexisting semantic payload independently, including
    routes, ports, supports, both sweep contexts, and all other source fields.
    The superseded standalone attempt retains its exact snapshot. Obsolete
    atomization predecessors, old builds, and assembly renders are not inputs.
    """
    revisions = ledger.get('subsequent_piece_revisions')
    require(revisions == [DIVERGE_PARAPET_REVISION, *LATER_PARAPET_REVISIONS,
                          *DIVERGE_SUCCESSOR_REVISIONS, *SYMMETRIC_STEM_SUCCESSOR_REVISIONS,
                          *OPPOSED_SUCCESSOR_REVISIONS],
            'Trumpet subsequent piece revision differs from its exact standalone authorization')
    chains = {}
    for revision in revisions:
        chains.setdefault(revision['piece_id'], []).append(revision)
    for chain in chains.values():
        for previous, successor in zip(chain, chain[1:]):
            require(previous['source_file'] == successor['source_file']
                    and previous['after_sha256'] == successor['before_sha256']
                    == successor['before_piece_snapshot']['geometry_sha256'],
                    'Trumpet standalone piece revision source chain is disconnected')
        if chain[0]['piece_id'] == FULL_FAN_ID:
            # Its exact original row remains evidence of the old execution.
            # Retirement explicitly removes source replay rather than making
            # an invisible exception to current retained-piece acceptance.
            audit_parent_retirement(root=root, ledger=ledger)
            continue
        for number, revision in enumerate(chain):
            directory = None
            if number+1 < len(chain):
                successor = chain[number+1]
                directory = (Path(root)/revision['source_file']).parent/successor[
                    'before_piece_snapshot']['snapshot_directory']
            _audit_standalone_piece_revision(revision, root=root, source_directory=directory)
    return chains


def _audit_standalone_piece_revision(revision, *, root, source_directory=None):
    """Bind each accepted repair to its own source, evidence, and archive.

    A later revision supplies the snapshot of its accepted predecessor. Older
    archive references remain relative to the original owning piece folder.
    """
    original_source = Path(root)/revision['source_file']
    source = original_source if source_directory is None else source_directory/original_source.name
    raw = source.read_bytes()
    existing = json.loads(raw)
    properties = [revision.get(key) for key in
                  ('only_added_geometry_property', 'only_changed_geometry_property')]
    require(sum(value is not None for value in properties) == 1,
            'Trumpet standalone repair needs exactly one bounded geometry property')
    property_name = next(value for value in properties if value is not None)
    require(existing.pop(property_name, None) == revision[property_name],
            'Trumpet subsequent piece revision border rule differs')
    require(canonical_sha256(existing) == revision['preserved_geometry_semantic_sha256'],
            'Trumpet subsequent piece revision changed preexisting geometry outside its border rule')
    require(sha256(raw) == revision['after_sha256'],
            'Trumpet subsequent piece revision current source fingerprint differs')
    for relative, digest in revision['standalone_evidence'].items():
        require(sha256((source.parent/relative).read_bytes()) == digest,
                'Trumpet subsequent piece revision standalone evidence fingerprint differs')
    superseded = revision.get('superseded_attempt', revision.get('before_piece_snapshot'))
    snapshot = original_source.parent/superseded['snapshot_directory']
    index_raw = (snapshot/'index.json').read_bytes()
    require(sha256(index_raw) == superseded['index_sha256'],
            'Trumpet superseded piece attempt snapshot index fingerprint differs')
    files = json.loads(index_raw)['files']
    archived = ([(relative, item['sha256']) for relative, item in files.items()]
                if isinstance(files, dict) else
                [(item.get('snapshot_file', item.get('path')), item['sha256']) for item in files])
    for relative, digest in archived:
        require(sha256((snapshot/relative).read_bytes()) == digest,
                'Trumpet superseded piece attempt archived evidence fingerprint differs')
    require(sha256((snapshot/'geometry.json').read_bytes()) == superseded['geometry_sha256'],
            'Trumpet superseded piece attempt source fingerprint differs')
    if 'before_piece_snapshot' in revision:
        previous = json.loads((snapshot/'geometry.json').read_bytes())
        if 'only_changed_geometry_property' in revision:
            require(property_name in previous,
                    'Trumpet standalone repair predecessor lacks its changed geometry property')
            previous.pop(property_name)
        require(superseded['geometry_sha256'] == revision['before_sha256']
                and canonical_sha256(previous) == revision['preserved_geometry_semantic_sha256'],
                'Trumpet standalone repair predecessor does not match its preserved source')


# Signed winding distinguishes the deliberate loops from the direct slips.
# Direct slips retain their existing130-degree absolute-turn allowance for
# unchanged reverse curvature; their net heading change is exactly-90degrees.
# East-to-south has270degrees of absolute turning but a+90degree net heading
# after its initial reverse bend; south-to-west winds consistently-270degrees.
WHOLE_ROUTE_LIMITS = {
    ('W_in', 'E_out'): {**_TURN_LIMITS, 'max_length_ratio': 1.00001,
        'max_total_turn_degrees': .01, 'signed_turn_degrees': 0., 'max_signed_turn_error_degrees': .01},
    ('E_in', 'W_out'): {**_TURN_LIMITS, 'max_length_ratio': 1.00001,
        'max_total_turn_degrees': .01, 'signed_turn_degrees': 0., 'max_signed_turn_error_degrees': .01},
    ('W_in', 'S_out'): {**_TURN_LIMITS, 'max_total_turn_degrees': 130.,
        'signed_turn_degrees': -90., 'max_signed_turn_error_degrees': .01},
    ('S_in', 'E_out'): {**_TURN_LIMITS, 'max_total_turn_degrees': 130.,
        'signed_turn_degrees': -90., 'max_signed_turn_error_degrees': .01},
    ('E_in', 'S_out'): {**_TURN_LIMITS, 'max_length_ratio': 3.5,
        'min_total_turn_degrees': 269., 'max_total_turn_degrees': 271.,
        'signed_turn_degrees': 90., 'max_signed_turn_error_degrees': .01},
    ('S_in', 'W_out'): {**_TURN_LIMITS, 'max_length_ratio': 3.5,
        'min_total_turn_degrees': 269., 'max_total_turn_degrees': 271.,
        'signed_turn_degrees': -270., 'max_signed_turn_error_degrees': .01},
}


def whole_route_policy():
    return {'per_movement': {'>'.join(movement): limits for movement, limits in WHOLE_ROUTE_LIMITS.items()},
            'preserved_baseline_journeys': 'Both mainlines and both direct slips; only collinear grid-cut subdivisions may differ.',
            'constituent_module_limits_retained': True}


def expected_occupied_cells():
    record = read_rework_record(REWORK_PATH, root=ROOT, require_completed=False)
    return 85+len(ALLOWED_CELLS)-len(record.get('removed_world_cells_east_north_m', []))


def audit_quality_contract(path=QUALITY_PATH):
    literal = json.loads(Path(path).read_text())
    integrated = 'border_piece_integration_sha256' in resource_descriptor(RESOURCES_PATH)
    expected = {
        'schema_version': 2, 'id': 'straight-stem-trumpet', 'occupied_cells': expected_occupied_cells(),
        'encoded_fragments': resource_descriptor(RESOURCES_PATH).get('encoded_fragments', 167),
        'unique_piers': 74, 'placements': 28 if integrated else 26,
        'unique_piece_types': 14 if integrated else 13,
        'candidate_eligibility_strictly_below_m': .005, 'minimum_pier_spacing_m': 16.,
        'minimum_clearance': 5., 'actual_tile_triangles': resource_descriptor(RESOURCES_PATH)['actual_tile_triangles'],
        'current_resource_contract': 'resources.json',
        'required_grade_separated_crossings': 4,
        'expected_crossings_xyz': [list(p) for p in CONTRACT['expected_crossings_xyz']],
    }
    require(all(literal.get(k) == v for k, v in expected.items()),
            'Trumpet independent quality contract differs from its literal acceptance policy')
    require({k: tuple(v) for k, v in literal['ports'].items()} == CONTRACT['ports']
            and [tuple(v) for v in literal['movements']] == CONTRACT['movements'],
            'Trumpet outside connections differ from the independently authored assembly contract')
    require(literal['inherited_custom_cut_policy'] == {
        'departure_port': 'Win', 'return_port': 'Eout', 'depth_m': 2.65, 'width_m': 5.2,
        'require_exact_original_port_tile_models_all_five_zooms': True,
        'whole_assembly_uses_strict_unclipped_actual_neighbour_paths': True,
        'native_new_join_profile_tolerance_m': .00005},
        'Trumpet inherited custom-cut or native joining policy differs')
    require(literal['whole_route_quality'] == whole_route_policy()
            and literal.get('junction_rework_contract') == 'junction-rework.json',
            'Trumpet complete route quality policy differs')
    if 'border_piece_integration_sha256' in resource_descriptor(RESOURCES_PATH):
        require(literal.get('border_piece_integration_contract') == 'border-piece-integration.json',
                'Trumpet quality contract omits its current border integration')
    return {'contract_sha256': sha256(Path(path).read_bytes()),
            'candidate_eligibility_and_actual_edit_limits_are_separate': True,
            'independent_ports_movements_clearance_and_budgets_checked': True,
            'predecessor_resource_inputs_required': False}


def audit_approved_layout(scene, *, current_border_integration=True):
    path = (ASSEMBLY/'checks/layout.json' if current_border_integration else
            ASSEMBLY/SNAPSHOT_RELATIVE/'checks/layout.json')
    frozen = json.loads(path.read_text())
    normalized = canonical_sha256(frozen['layout'])
    require(frozen['schema_version'] == 1 and frozen['assembly_id'] == 'straight-stem-trumpet'
            and normalized == frozen['layout_sha256']
            == (CURRENT_INTEGRATION_LAYOUT if current_border_integration else CURRENT_LAYOUT),
            'Trumpet independently reviewed layout record changed')
    require(physical_layout(scene) == frozen['layout'], 'Trumpet physical layout differs from its approved positions')
    return {'layout_sha256': frozen['layout_sha256'], 'reviewed_placements': 28 if current_border_integration else 26,
            'approved_external_ports_rectangle_and_grid': True}


def audit_candidate_ledger(path=None, descriptor=None, *, redesign=None):
    """Validate frozen decisions and source revisions, not current assembly models."""
    path = ASSEMBLY/'checks/atomization.json' if path is None else Path(path)
    ledger = json.loads(path.read_text())
    descriptor = resource_descriptor(RESOURCES_PATH) if descriptor is None else descriptor
    require(ledger.get('schema_version') == 2 and ledger.get('assembly_id') == 'straight-stem-trumpet'
            and ledger.get('historical_inputs_required') is False,
            'Trumpet atomization ledger identity or historical-input policy differs')
    policy = ledger['policy']
    require(policy['candidate_eligibility_strictly_below_m'] == .005
            and policy['actual_rework_bounds_separate'] is True
            and policy['render_after_geometry_complete'] is True,
            'Trumpet atomization policy differs from the approved procedure')
    candidates = ledger['candidates']
    require(len(candidates) == len({c['id'] for c in candidates}) == 17, 'Trumpet atomization ledger omits or repeats a decision')
    approved = {c['id']: c for c in candidates if c['decision'] == 'atomized'}
    require(set(approved) == set(ELIGIBLE_CANDIDATES), 'Trumpet atomization ledger approves an unauthorized candidate')
    require(all(c['decision'] in ('atomized', 'retained') and c.get('reason') for c in candidates),
            'Trumpet candidate decisions need an explicit status and reason')
    subsequent = audit_subsequent_piece_revisions(ledger)
    measurements = {}
    for identifier, (cells, core_id, straight_id, angle, bound) in ELIGIBLE_CANDIDATES.items():
        candidate = approved[identifier]
        measured, visible = candidate['original_path_deviation_m'], candidate['original_visible_rail_deviation_m']
        require(all(isinstance(v, (int, float)) and math.isfinite(v) and 0. <= v < .005
                    for v in (measured, visible)), 'Trumpet candidate is not strictly below the5mm original eligibility threshold')
        require(abs(visible-measured) <= .000005,
                'Trumpet recorded original visible rail does not support its sub5mm PATH eligibility')
        replacement, work = candidate['replacement'], candidate['actual_rework']
        require(replacement['straight_piece_id'] == straight_id
                and replacement['straight_rotation_degrees'] == angle
                and replacement['new_core_piece_id'] == core_id,
                'Trumpet candidate replacement differs from its approved native type or direction')
        require(work['independent_bound_m'] == bound and 0. <= work['maximum_route_change_m'] <= bound
                and set(map(tuple, work['allowed_world_cells_en_m'])) == cells,
                'Trumpet recorded actual rework differs from its finite approved bound')
        current_source = ROOT/'domains/high-speed-rail/00_pieces'/core_id/'geometry.json'
        actual_source = sha256(current_source.read_bytes())
        historical_source = candidate['replacement_geometry_sha256']
        prior_redesign_used = False
        chain = subsequent.get(core_id, [])
        if actual_source != historical_source:
            predecessor = chain[0]['before_sha256'] if chain else actual_source
            if predecessor != historical_source:
                prior_redesign_used = True
                approved_redesign = read_frozen_rework_record() if redesign is None else redesign
                prior = approved_redesign['source_geometry'].get(core_id, {})
                require(prior.get('before_sha256') == historical_source
                        and prior.get('after_sha256') == predecessor,
                        'Trumpet atomization decision is stale for its changed replacement geometry')
            require(not chain or chain[-1]['after_sha256'] == actual_source,
                    'Trumpet atomization decision is stale for its changed replacement geometry')
        require(isinstance(work.get('measurement_method'), str) and bool(work['measurement_method'].strip()),
                'Trumpet recorded measured correction needs its explicit measurement method')
        measurements[identifier] = {'recorded_original_path_deviation_m': measured,
            'recorded_original_visible_rail_deviation_m': visible,
            'recorded_actual_rework_bound_m': bound,
            'historical_replacement_geometry_sha256': historical_source,
            'current_replacement_geometry_sha256': actual_source,
            'historical_source_superseded_by_explicit_redesign': prior_redesign_used,
            'historical_source_superseded_by_standalone_piece_revision': core_id in subsequent,
            'standalone_geometry_revision_chain':
                [chain[0]['before_sha256'], *(item['after_sha256'] for item in chain)] if chain else []}
    inventory = ledger['source_cell_inventory']
    identities = [(cell['source_piece_id'], *cell['standalone_xy']) for cell in inventory]
    require(len(identities) == len(set(identities)) == ledger['source_cells_reviewed'] == 51,
            'Trumpet atomization ledger omits or repeats an original reviewed cell')
    require(all(cell.get('reason') and (cell['candidate_id'] is None or cell['candidate_id'] in {c['id'] for c in candidates})
                for cell in inventory), 'Trumpet cell inventory lacks its decision or linked candidate')
    history = {'candidates': candidates, 'source_cell_inventory': inventory,
               'source_cells_reviewed': ledger['source_cells_reviewed']}
    require(canonical_sha256(history) == descriptor['atomization_history_sha256'],
            'Trumpet frozen atomization measurements or local and assembly coordinates changed')
    require(ledger['current_resource_contract'] == 'resources.json'
            and ledger['current_resource_contract_sha256'] == sha256(RESOURCES_PATH.read_bytes()),
            'Trumpet atomization ledger references a different current resource contract')
    if 'border_piece_integration_sha256' in descriptor:
        require(ledger.get('current_border_piece_integration') == 'border-piece-integration.json'
                and ledger.get('current_border_piece_integration_sha256') == descriptor['border_piece_integration_sha256'],
                'Trumpet atomization ledger omits its separate current integration binding')
    require(ledger['observations_inside_game'] == 'unverified', 'Trumpet software atomization cannot create game observations')
    return {'ledger_sha256': sha256(path.read_bytes()), 'eligible_atomized_candidates': measurements,
            'retained_candidates': 13, 'original_owned_cells_reviewed': 51,
            'strict_original_threshold_m': .005, 'old_deviation_and_actual_work_recorded_separately': True,
            'historical_measurements_are_frozen_not_remeasured': True,
            'subsequent_piece_revisions': ledger['subsequent_piece_revisions'],
            'retired_parent_source_replay': 'unavailable; exact historical row and immutable integration proof retained',
            'current_assembly_resource_audit_claimed_by_this_ledger_check': False,
            'deleted_predecessor_resources_required': False}


def audit_current_world_tiles(candidate, descriptor):
    expected = {tuple(cell['world_east_north_m']): cell for cell in descriptor['world_cells']}
    require(len(expected) == len(descriptor['world_cells']) == expected_occupied_cells() and set(candidate) == set(expected),
            'Trumpet occupied world tiles differ from the approved current resource contract')
    for position, tile in candidate.items():
        record = expected[position]
        require(tile['piece_id'] == record['piece_id'] and list(tile['cell']) == record['cell']
                and tile['rotation'] == record['rotation_quarter_turns_ccw'],
                f'Trumpet approved current tile owner, local cell or orientation changed at {position}')
        hashes = {family: sha256(raw) for family, raw in tile['resources'].items()}
        require(hashes == record['resources_sha256'],
                f'Trumpet approved current saved tile resources changed at {position}')
    for position, (identifier, turns) in REPLACEMENTS.items():
        require(candidate[position]['piece_id'] == identifier and candidate[position]['rotation'] == turns,
                'Trumpet extracted tile is not the correctly directed existing standard straight')
    triangles = sum(triangle_count(t['resources']['model_0']) for t in candidate.values())
    require(triangles == descriptor['actual_tile_triangles'],
            'Trumpet approved current actual triangle inventory differs')
    return {'occupied_cells': len(candidate), 'strict_byte_identity_cells': len(candidate),
            'actual_tile_triangles': triangles, 'tile_resource_fingerprints_checked': len(candidate)*11,
            'exact_current_ownership_and_rotations_checked': True,
            'original_standard_straight_replacements': 4}


def audit_current_journeys(journeys, descriptor):
    expected = {tuple(record['movement']): record for record in descriptor['journeys']}
    require(len(expected) == len(descriptor['journeys']) == 6 and set(journeys) == set(expected)
            == set(CONTRACT['movements']), 'Trumpet current directed journey inventory differs')
    for movement, points in journeys.items():
        record = expected[movement]
        require(len(points) == record['encoded_points'] and canonical_sha256(points) == record['points_sha256'],
                f'Trumpet approved complete encoded journey geometry changed: {movement}')
    return {'complete_directed_journeys_frozen': 6, 'all_encoded_point_positions_and_counts_identical': True}


def audit_whole_route_quality(journeys):
    """Measure all six actual journeys under independent movement-specific bounds."""
    require(set(journeys) == set(WHOLE_ROUTE_LIMITS), 'Trumpet complete route-quality movement inventory differs')
    reports = {'>'.join(movement): measure_journey_quality(journeys[movement], limits)
               for movement, limits in WHOLE_ROUTE_LIMITS.items()}
    return {'complete_journeys': reports, 'complete_journeys_checked': 6,
            'radius_minimum_m': 24., 'curvature_change_limit_per_m2': .0015,
            'native_endpoint_curvature_limit_per_m': .0005,
            'constituent_module_quality_limits_remain_unchanged': True}


def audit_assembled_geometry(tiles, records):
    instances = {tile['instance_id'] for tile in tiles.values()}
    selected = [record for record in records if record[1]['instance_id'] in instances]
    points = [p for _, _, route in selected for p in route]
    east = min(p[0] for p in points)-2.5, max(p[0] for p in points)+2.5
    north = min(p[1] for p in points)-2.5, max(p[1] for p in points)+2.5
    neighbours = {pos for pos in tiles if pos[0]+8. >= east[0] and pos[0]-8. <= east[1]
                  and pos[1]+8. >= north[0] and pos[1]-8. <= north[1]}
    triangles = list(_world_triangles(tiles, neighbours))
    report = audit_bed_corridors(triangles, selected)
    report.update(audit_visible_rails(triangles, records))
    buckets = defaultdict(list)
    for tri in triangles:
        for x in range(math.floor(min(p[0] for p in tri)/4.), math.floor(max(p[0] for p in tri)/4.)+1):
            for z in range(math.floor(min(p[2] for p in tri)/4.), math.floor(max(p[2] for p in tri)/4.)+1):
                buckets[x, z].append(tri)
    report['complete_train_clearance_segments_checked'] = _clearance_segments(selected, buckets, half_width=2.5)
    return {**report, 'actual_module_instances_checked': len(instances),
            'actual_neighbour_models_used': len(neighbours), 'strict_unclipped_actual_path_audit': True}


def audit_candidate_without_current_pins(build_path, scene, *, completed_rework, current_border_integration=False):
    """Prove the authorized redesign independently before capturing its new hashes."""
    layout = audit_approved_layout(scene, current_border_integration=current_border_integration)
    rework = (read_frozen_rework_record() if current_border_integration else
              read_rework_record(REWORK_PATH, root=ROOT, require_completed=completed_rework))
    build = load_build(build_path)
    if current_border_integration:
        empty_proof = prove_current_removed_structural_cells(build, root=ROOT)
        empty_cells = audit_current_removed_cell_evidence(empty_proof)
        rework['current_core_removed_cell_proof'] = empty_proof
        expected_ids = CURRENT_IDS
        expected_labels = [item['label'] for item in expected_current_placements(frozen_border_inputs())]
    else:
        empty_proof = prove_removed_structural_cells(build, rework, root=ROOT)
        if completed_rework and empty_proof is not None:
            original = dict(rework['removed_cell_proof']); current = dict(empty_proof)
            original.pop('source_build_manifest_sha256', None); current.pop('source_build_manifest_sha256', None)
            require(original == current, 'Trumpet removed-cell proof differs from the actual saved fan resources')
        if empty_proof is not None:
            rework['removed_cell_proof'] = empty_proof
        empty_cells = audit_removed_cell_evidence(rework)
        expected_ids = frozenset(piece['id'] for piece in frozen_border_inputs()['descriptor']['pieces'])
        expected_labels = [f'P{i:02}' for i in range(1, 27)]
    require(set(build['pieces']) == set(expected_ids), 'Trumpet candidate selected piece types differ')
    require([item.get('label') for item in placements(scene)] == expected_labels,
            'Trumpet placements differ from their exact approved instance labels')
    for instance in placements(scene):
        require(instance.get('instance_id') == instance['label']
                and instance['recipe'] == build['pieces'][instance['piece_id']]['recipe'],
                'Trumpet placement identity or retained recipe differs')
    candidate, sources = world_tiles(scene, build)
    preservation = (audit_border_scope(candidate, build, scene) if current_border_integration else
                    audit_redesign_scope(candidate, build, rework))
    records = encoded_records(candidate)
    journeys = _journeys(records, CONTRACT)
    paths = {'encoded_fragments': len(records), 'direct_slip_symmetry': direct_slip_symmetry(journeys),
             'fixed_redesigned_joins': audit_target_joins(records),
             'unchanged_journeys': audit_preserved_journeys(journeys, rework),
             'affected_northern_route_movement': audit_route_movement(journeys, rework),
             'whole_route_quality': audit_whole_route_quality(journeys), 'proper_rotations': []}
    if current_border_integration:
        paths['atomized_route_movement_preservation'] = audit_current_route_movement(
            paths['affected_northern_route_movement'], rework['compiled_route_movement'], journeys)
    elif completed_rework:
        audit_matching_route_movement(paths['affected_northern_route_movement'], rework['compiled_route_movement'])
    for turns in range(4):
        contract = deepcopy(CONTRACT)
        contract['ports'] = {name: key(rotate(p, turns)) for name, p in CONTRACT['ports'].items()}
        contract['expected_crossings_xyz'] = [(*rotate((x, north, upper), turns)[:2], upper, lower)
                                              for x, north, upper, lower in CONTRACT['expected_crossings_xyz']]
        transformed = [(cell, meta, [key(rotate(p, turns)) for p in points]) for cell, meta, points in records]
        require(_graph(transformed, contract) == (6, 6), 'Trumpet directed travel matrix differs')
        moved = _journeys(transformed, contract)
        require(split_flags(transformed) == 3, 'Trumpet split flags differ')
        paths['proper_rotations'].append({'rotation_degrees_ccw': turns*90, 'unique_journeys': 6,
                                          **audit_crossings(moved, contract)})
    geometry = {'redesign_preservation': preservation,
                'complete_actual_assembly_corridors': audit_assembled_geometry(candidate, records)}
    checked, audits, supports = set(), [], []
    for instance in placements(scene):
        piece = build['pieces'][instance['piece_id']]
        if piece['recipe'] not in checked:
            saved = build['resources'](piece)
            audits.append({'piece_id': piece['id'], 'dat_sha256': saved['sha256'],
                           'audit': verify_component(piece, saved['resources'])})
            checked.add(piece['recipe'])
        for east, south in CONTRACTS[piece['recipe']]['support_centres_xz']:
            x, north, _ = rotate((east, -south, 0.), rotation(instance))
            supports.append(key((x+instance['origin_m'][0], north+instance['origin_m'][1], 0.))[:2])
    require(len(placements(scene)) == (28 if current_border_integration else 26)
            and len(checked) == (14 if current_border_integration else 13),
            'Trumpet placement/type totals differ')
    support_report = audit_redesign_supports(supports, rework)
    if current_border_integration:
        geometry['current_merge_join_and_preserved_routes'] = {
            **audit_current_native_seam(candidate),
            **audit_preserved_current_journeys(journeys, supports),
            'historical_extraction_record_rewritten': False}
    else:
        geometry['merge_west_tail_extraction'] = audit_merge_extraction(candidate, build, journeys, supports)
    triangles = sum(triangle_count(t['resources']['model_0']) for t in candidate.values())
    require(triangles == sum(s['preview_triangles'] for s in sources),
            'Trumpet ownership or actual preview triangle inventory differs')
    return {'build': build, 'candidate': candidate, 'journeys': journeys, 'layout': layout,
            'geometry': {**geometry, 'empty_structural_cells': empty_cells}, 'paths': paths, 'audits': audits, 'sources': sources,
            'supports': support_report, 'triangles': triangles, 'rework': rework}


def _candidate_report(audited, scene_path, quality):
    build = audited['build']
    return {'purpose': __doc__.split('\n\n')[0], 'schema_version': 3, 'status': 'passed',
            'scope': 'actual approved current saved compiled resources; game operation unverified',
            'scene_file': Path(scene_path).name, 'scene_sha256': sha256(Path(scene_path).read_bytes()),
            'manifest_sha256': build['manifest_sha256'], 'audited_manifest_file': 'audited-build-manifest.json',
            'manifest_hash_scope': 'Exact input manifest at audit start; documentation metadata may change later. DAT fingerprints are independently pinned.',
            'current_resource_contract_sha256': sha256(RESOURCES_PATH.read_bytes()),
            'deleted_predecessor_resource_inputs_required': False,
            'reviewed_layout': audited['layout'], 'independent_quality_contract': quality,
            'atomization_decisions': audit_candidate_ledger(),
            'geometry': audited['geometry'], 'encoded_paths': audited['paths'],
            'sources': audited['sources'], 'independent_component_audits': audited['audits'],
            'supports': audited['supports'], 'game_tests': 'unverified'}


def verify(build_path, scene_path=SCENE):
    scene = json.loads(Path(scene_path).read_text())
    quality = audit_quality_contract()
    descriptor = resource_descriptor(RESOURCES_PATH)
    verification_resources(RESOURCES_PATH, build_path, selected_piece_ids=CURRENT_IDS,
                           assembly_id='straight-stem-trumpet')
    integration = read_border_integration_record(descriptor=descriptor)
    audited = audit_candidate_without_current_pins(build_path, scene, completed_rework=False,
                                                    current_border_integration=True)
    audited['geometry']['current_border_piece_integration'] = {
        'record_file': INTEGRATION_PATH.name, 'record_sha256': sha256(INTEGRATION_PATH.read_bytes()),
        'status': integration['status'], 'historical_standalone_rows_rewritten': False}
    require(descriptor['layout_sha256'] == audited['layout']['layout_sha256'],
            'Trumpet resource contract pins a different physical layout')
    require(descriptor['junction_rework_sha256'] == sha256(REWORK_PATH.read_bytes()),
            'Trumpet resource contract pins a different authorized redesign proof')
    audited['geometry'].update(audit_current_world_tiles(audited['candidate'], descriptor))
    audited['paths']['approved_current_journeys'] = audit_current_journeys(audited['journeys'], descriptor)
    require(audited['paths']['encoded_fragments'] == descriptor['encoded_fragments'],
            'Trumpet current encoded fragment count differs')
    return _candidate_report(audited, scene_path, quality)


def _commit_current_contracts(payloads):
    """Stage every file, then restore the previous complete set on write failure."""
    previous = {path: path.read_bytes() if path.exists() else None for path in payloads}
    staged = {}
    try:
        for path, raw in payloads.items():
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.border-integration-', delete=False) as stream:
                staged[path] = Path(stream.name)
                stream.write(raw)
        for path, temporary in staged.items():
            os.replace(temporary, path)
    except BaseException:
        for path, raw in previous.items():
            if raw is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(raw)
        raise
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)


def _commit_and_validate_current_contracts(payloads, validate):
    """Restore the complete previous state if any post-commit validation fails."""
    previous = {path: path.read_bytes() if path.exists() else None for path in payloads}
    try:
        _commit_current_contracts(payloads)
        return validate()
    except BaseException:
        for path, raw in previous.items():
            if raw is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(raw)
        raise


def capture_current_resources(build_path, scene_path=SCENE):
    """Capture approved border repairs and fan atomization without rewriting history."""
    if INTEGRATION_PATH.exists():
        return verify(build_path, scene_path)
    audit_quality_contract()
    audit_candidate_ledger()
    scene = json.loads(Path(scene_path).read_text())
    audited = audit_candidate_without_current_pins(build_path, scene, completed_rework=False,
                                                    current_border_integration=True)
    build, tiles, journeys = audited['build'], audited['candidate'], audited['journeys']
    require(audited['triangles'] == CURRENT_TILE_TRIANGLES,
            'Trumpet current triangle total differs from the independently counted approved standalone archives')
    ledger_path = ASSEMBLY/'checks/atomization.json'
    ledger = json.loads(ledger_path.read_text())
    history = {name: ledger[name] for name in ('candidates', 'source_cell_inventory', 'source_cells_reviewed')}
    frozen = frozen_border_inputs()
    require(canonical_sha256(history) == frozen['descriptor']['atomization_history_sha256'],
            'Trumpet integration capture cannot rewrite historical atomization measurements')
    archives = []
    for identifier in sorted(CURRENT_IDS):
        spec = build['pieces'][identifier]
        raw = (build['path']/spec['asset_file']).read_bytes()
        saved = build['resources'](spec)['resources']
        require(len(entries(raw)) == len(saved) == int.from_bytes(raw[36:40], 'little'),
                'Trumpet capture archive repeats or omits a resource identity')
        archives.append({'id': identifier, 'recipe': spec['recipe'], 'asset_file': spec['asset_file'],
                         'bytes': len(raw), 'sha256': sha256(raw), 'resource_count': len(saved),
                         'resource_sha256': {'-'.join(f'{v:08x}' for v in key): sha256(value)
                                             for key, value in saved.items()}})
    descriptor = {'purpose': 'Current border-repair and three-piece fan integration pins, captured after independent standalone archive identity and complete physical assembly audits.',
        'schema_version': 3, 'id': 'straight-stem-trumpet-current-resources', 'assembly_id': 'straight-stem-trumpet',
        'pieces': archives, 'layout_sha256': audited['layout']['layout_sha256'],
        'junction_rework_sha256': sha256(REWORK_PATH.read_bytes()),
        'atomization_history_sha256': canonical_sha256(history),
        'world_cells': [{'world_east_north_m': list(position), 'piece_id': tile['piece_id'],
                         'cell': list(tile['cell']), 'rotation_quarter_turns_ccw': tile['rotation'],
                         'resources_sha256': {name: sha256(raw) for name, raw in tile['resources'].items()}}
                        for position, tile in sorted(tiles.items())],
        'journeys': [{'movement': list(movement), 'encoded_points': len(points), 'points_sha256': canonical_sha256(points)}
                     for movement, points in sorted(journeys.items())],
        'encoded_fragments': audited['paths']['encoded_fragments'], 'actual_tile_triangles': audited['triangles']}
    integration = {'schema_version': 1, 'assembly_id': 'straight-stem-trumpet', 'status': 'passed',
        'purpose': 'Integrate the approved border repairs and atomized three-piece fan into the complete trumpet; preserve all seven earlier source-only decisions and historical redesign proofs.',
        'baseline_snapshot': {'directory': SNAPSHOT_RELATIVE.as_posix(), 'index_sha256': SNAPSHOT_INDEX_SHA256},
        'layout_sha256': audited['layout']['layout_sha256'], 'scene_sha256': sha256(Path(scene_path).read_bytes()),
        'policy': integration_policy(frozen), 'source_inputs': audit_source_inputs(),
        'standalone_revisions_sha256': STANDALONE_REVISIONS_SHA256,
        'compiled_audit': {'manifest_sha256': build['manifest_sha256'],
            'manifest_scope': 'Exact manifest at the integration audit; later documentation-only changes may be checked against the same independently approved DATs and permanent piece identities.',
            'archive_sha256': expected_archives(frozen),
            'world_cells_sha256': canonical_sha256(descriptor['world_cells']),
            'journeys_sha256': canonical_sha256(descriptor['journeys']),
            'encoded_fragments': audited['paths']['encoded_fragments'], 'actual_tile_triangles': audited['triangles'],
            'occupied_cells': len(tiles), 'placements': len(placements(scene)),
            'component_types_checked': len(audited['audits']), 'support_positions': audited['supports']['total_column_positions'],
            'proper_rotations_checked': len(audited['paths']['proper_rotations']), 'complete_journeys_checked': 6,
            'all_independent_physical_checks_passed': True},
        'current_empty_structural_cell_proof': audited['rework']['current_core_removed_cell_proof'],
        'current_model_scope_audit': audited['geometry']['redesign_preservation'],
        'current_merge_join_and_preserved_routes': audited['geometry']['current_merge_join_and_preserved_routes'],
        'historical_standalone_rows_rewritten': False, 'manual_or_game_observations_added': False,
        'rendering_checked_by_this_record': False, 'installed': False}
    integration_raw = json.dumps(integration, indent=2)+'\n'
    descriptor['border_piece_integration_sha256'] = sha256(integration_raw.encode())
    quality = json.loads(QUALITY_PATH.read_text())
    quality.update(actual_tile_triangles=audited['triangles'], placements=28, unique_piece_types=14,
                   encoded_fragments=audited['paths']['encoded_fragments'],
                   border_piece_integration_contract='border-piece-integration.json')
    # All model identities, source bindings, preservation rules, and physical
    # checks above must pass before any current contract is renewed.
    descriptor_raw = json.dumps(descriptor, indent=2)+'\n'
    ledger['current_resource_contract_sha256'] = sha256(descriptor_raw.encode())
    ledger['current_border_piece_integration'] = 'border-piece-integration.json'
    ledger['current_border_piece_integration_sha256'] = sha256(integration_raw.encode())
    # Validate the proposed completed record against actual current sources
    # before renewing any file. Its descriptor points at this exact temporary
    # record; no active path needs to be overwritten to perform the check.
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf8') as stream:
        stream.write(integration_raw); stream.flush()
        read_border_integration_record(Path(stream.name), descriptor=descriptor,
                                       initial_manifest_raw=(build['path']/'manifest.json').read_bytes())
    payloads = {
        INTEGRATION_PATH: integration_raw.encode(), RESOURCES_PATH: descriptor_raw.encode(),
        QUALITY_PATH: (json.dumps(quality, indent=2)+'\n').encode(),
        ledger_path: (json.dumps(ledger, indent=2)+'\n').encode(),
        ASSEMBLY/'evidence/border-piece-integration-initial-build-manifest.json': (build['path']/'manifest.json').read_bytes()}
    def validate_committed():
        read_border_integration_record(descriptor=descriptor)
        audited['geometry'].update(audit_current_world_tiles(tiles, descriptor))
        audited['geometry']['current_border_piece_integration'] = {
            'record_file': INTEGRATION_PATH.name, 'record_sha256': sha256(integration_raw.encode()),
            'status': 'passed', 'historical_standalone_rows_rewritten': False}
        audited['paths']['approved_current_journeys'] = audit_current_journeys(journeys, descriptor)
        report = _candidate_report(audited, scene_path, audit_quality_contract())
        report['audited_manifest_file'] = 'border-piece-integration-initial-build-manifest.json'
        return report
    return _commit_and_validate_current_contracts(payloads, validate_committed)



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', required=True, type=Path)
    parser.add_argument('--scene', default=SCENE, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--capture-current', action='store_true',
                        help='Capture current integration pins only after all independently approved standalone DATs and full assembly physical audits pass')
    args = parser.parse_args()
    preserve_initial_output = args.capture_current and args.output.exists()
    require(not preserve_initial_output or INTEGRATION_PATH.exists(),
            'Initial integration capture cannot overwrite an existing report before its contract exists')
    report = (capture_current_resources if args.capture_current else verify)(args.build, args.scene)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if not preserve_initial_output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'occupied_cells': report['geometry']['occupied_cells'], 'current_piers': report['supports']['total_column_positions'],
                      'strict_byte_identity_cells': report['geometry']['strict_byte_identity_cells'],
                      'proper_rotations_checked': 4, 'initial_output_preserved': preserve_initial_output, 'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
