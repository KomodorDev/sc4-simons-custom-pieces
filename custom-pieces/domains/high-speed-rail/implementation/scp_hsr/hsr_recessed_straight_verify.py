"""Independently pin the fan-family straight's actual recessed-web profile.

The expected raw resources come from interior cell [3,1] of the approved
full-fan DAT, independently of the new one-cell writer. The standard paired
straight remains a separate unchanged profile.
"""
from __future__ import annotations

import hashlib
from scp.dbpf import require
from scp.track_paths import PATH, S3D

RECIPE = 'hsr_component_l2_paired_straight_recessed_web'
SOURCE_DAT_SHA256 = '54086c7a5423f0d121d732d1b8081c1984e0663afb3d3c8a4604cdcc5b43c797'
MODEL_SHA256 = 'c1cf559567913402dc89899514427af3a8af7db6c3ef1e4db6c1103f7d8abff0'
PATH_SHA256 = '41dfafc4ef2c1cf41cf838382b088cafe3bbe704b88dc4ee3e220d6cd7c748ef'
SHADOW_SHA256 = ('e2ace4d7f48bd1046e7c619a20550d4da2f5f949fd8d9c9b69332aec2243869a', 'f334b53c5daf3e0a5ca0900ea72a3defb3cde7843fa255d87741348fd14b6a40', 'f7fb212677ad7841a6dbbf3022b136e11b497ae86f94fa7d83b9c51763b48b0c', '2024b2b7a9f2a100f9beaf66672ed4cc8a74bf1128ffe4dcf82d4f6eddc90b15', 'c9af156b08417a82dd5a66617b9019582df277598760186a044d6df4f0f6ef6d')


def audit_retained_straight_paths(resources, spec):
    require(spec['recipe'] == RECIPE and spec['cells'] == [[0, 0]]
            and spec['footprint'] == [1, 1] and len(spec['tile_ids']) == 1,
            'Recessed-web straight must be its exact one-cell piece')
    tile = int(spec['tile_ids'][0], 16)
    require(hashlib.sha256(resources[*PATH, tile]).hexdigest() == PATH_SHA256,
            'Recessed-web straight changed its approved directed local PATHs')
    return {'exact_recessed_web_path_cells_checked': 1}


def audit_retained_straight_resources(resources, spec):
    report = audit_retained_straight_paths(resources, spec)
    tile = int(spec['tile_ids'][0], 16)
    for zoom in range(5):
        require(hashlib.sha256(resources[*S3D, tile+zoom]).hexdigest() == MODEL_SHA256,
                f'Recessed-web straight changed its approved body, rails, support, or UV: zoom={zoom}')
        require(hashlib.sha256(resources[0x7ab50e44, 0x2bc2759a, tile+zoom]).hexdigest() == SHADOW_SHA256[zoom],
                f'Recessed-web straight changed its approved shadow: zoom={zoom}')
    return {**report, 'exact_recessed_web_model_zoom_resources_checked': 5,
            'exact_recessed_web_shadow_zoom_resources_checked': 5,
            'canonical_full_fan_local_cell': [3, 1],
            'recessed_web_body_rails_support_and_uv_unchanged': True,
            'retained_fan_source_dat_sha256': SOURCE_DAT_SHA256,
            'full_profile_equivalence_to_standard_straight_claimed': False}
