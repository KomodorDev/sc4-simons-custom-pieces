"""Finite first-cut diagonal DD transition identities, without allocation.

Physical side and travel direction are independent choices. Native profiles,
tile halves, and socket poses must be measured for each choice; these records
do not assert that reflecting an orthogonal or native model is sufficient.
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType

ORIGINAL = "original"
MIRRORED = "mirrored"
OPPOSITE_SIDE = "opposite-side"
OPPOSITE_SIDE_MIRRORED = "opposite-side-mirrored"
VARIANTS = (ORIGINAL, MIRRORED, OPPOSITE_SIDE, OPPOSITE_SIDE_MIRRORED)
VARIANT_FIELD = "diagonal_transition_variant"
ALIGNMENT_FIELD = "diagonal_transition_alignment"
ALIGNMENT = "a"

_BASE = "ddrhw-l1-l2-rhw-l0-ramp-diagonal"
PIECE_IDS = tuple(_BASE + suffix + "-alignment-a" for suffix in
                  ("", "-mirrored", "-opposite", "-opposite-mirrored"))
PIECE_ID, MIRRORED_PIECE_ID, OPPOSITE_SIDE_PIECE_ID, OPPOSITE_SIDE_MIRRORED_PIECE_ID = PIECE_IDS
RECIPES = tuple("highway_ddrhw_diagonal_l0_transition" + suffix + "_a" for suffix in
                ("", "_mirrored", "_opposite", "_opposite_mirrored"))
RECIPE, MIRRORED_RECIPE, OPPOSITE_SIDE_RECIPE, OPPOSITE_SIDE_MIRRORED_RECIPE = RECIPES


@dataclass(frozen=True)
class TransitionVariant:
    key: str
    piece_id: str
    recipe: str
    physical_reflection: bool
    traffic_reversed: bool
    opposite_side: bool


_RECORDS = MappingProxyType({
    key: TransitionVariant(key, identifier, recipe, reflected, reversed_traffic,
                           index >= 2)
    for index, (key, identifier, recipe, reflected, reversed_traffic) in enumerate(zip(
        VARIANTS, PIECE_IDS, RECIPES, (False, True, True, False),
        (False, True, False, True)))
})


def record_for(variant=ORIGINAL):
    """Select only one reviewed side/travel combination of the first cut."""
    if not isinstance(variant, str) or variant not in _RECORDS:
        raise ValueError("Unknown first-cut diagonal transition variant")
    return _RECORDS[variant]


def variant_of(piece):
    """Reject implicit aliases, old identities, mixed recipes, and other cuts."""
    if not isinstance(piece, Mapping):
        raise ValueError("Unreviewed diagonal transition identity")
    record = record_for(piece.get(VARIANT_FIELD))
    if (piece.get("domain") != "highway" or piece.get("id") != record.piece_id
            or piece.get("recipe") != record.recipe
            or piece.get(ALIGNMENT_FIELD) != ALIGNMENT):
        raise ValueError("Unreviewed diagonal transition identity, recipe, or alignment")
    return record.key
