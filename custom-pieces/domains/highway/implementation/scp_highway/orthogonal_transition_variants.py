"""Finite identities and independent side/traffic choices for DD transitions.

These records allocate no resources. Reflection of the physical plan, reversal
of travel, and reflection of the native cross-section are separate choices;
the two legacy records retain their existing meanings and defaults.
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType

ORIGINAL = "original"
MIRRORED = "mirrored"
OPPOSITE_SIDE = "opposite-side"
OPPOSITE_SIDE_MIRRORED = "opposite-side-mirrored"
LOWER_BEND_RIGHT = "lower-bend-right"
VARIANTS = (ORIGINAL, MIRRORED, OPPOSITE_SIDE, OPPOSITE_SIDE_MIRRORED)
VARIANT_FIELD = "transition_variant"

PIECE_ID = "ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile"
MIRRORED_PIECE_ID = PIECE_ID + "-mirrored"
OPPOSITE_SIDE_PIECE_ID = "ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile"
OPPOSITE_SIDE_MIRRORED_PIECE_ID = OPPOSITE_SIDE_PIECE_ID + "-mirrored"
PIECE_IDS = (PIECE_ID, MIRRORED_PIECE_ID, OPPOSITE_SIDE_PIECE_ID,
             OPPOSITE_SIDE_MIRRORED_PIECE_ID)
LOWER_BEND_RIGHT_PIECE_ID = "ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile"
SUPPORTED_PIECE_IDS = (*PIECE_IDS, LOWER_BEND_RIGHT_PIECE_ID)

RECIPE = "highway_ddrhw_orthogonal_l0_transition"
MIRRORED_RECIPE = RECIPE + "_mirrored"
OPPOSITE_SIDE_RECIPE = RECIPE + "_opposite_side"
OPPOSITE_SIDE_MIRRORED_RECIPE = RECIPE + "_opposite_side_mirrored"
RECIPES = (RECIPE, MIRRORED_RECIPE, OPPOSITE_SIDE_RECIPE,
           OPPOSITE_SIDE_MIRRORED_RECIPE)
LOWER_BEND_RIGHT_RECIPE = "highway_ddrhw_orthogonal_l0_transition_lower_bend_right"
SUPPORTED_RECIPES = (*RECIPES, LOWER_BEND_RIGHT_RECIPE)


@dataclass(frozen=True)
class TransitionVariant:
    key: str
    piece_id: str
    recipe: str
    physical_reflection: bool
    traffic_reversed: bool
    native_cross_section_reflection: bool
    opposite_side: bool
    shifted_deck: str = "upper"


_RECORDS = MappingProxyType({
    **{
        key: TransitionVariant(key, piece_id, recipe, reflected, reversed_traffic,
                               reflected != reversed_traffic, index >= 2)
        for index, (key, piece_id, recipe, reflected, reversed_traffic) in enumerate(zip(
            VARIANTS, PIECE_IDS, RECIPES, (False, True, True, False),
            (False, True, False, True)))
    },
    LOWER_BEND_RIGHT: TransitionVariant(LOWER_BEND_RIGHT, LOWER_BEND_RIGHT_PIECE_ID,
        LOWER_BEND_RIGHT_RECIPE, physical_reflection=False, traffic_reversed=True,
        native_cross_section_reflection=True, opposite_side=False, shifted_deck="lower"),
})


def record_for(variant=ORIGINAL):
    """Return an immutable reviewed choice, rejecting implicit new aliases."""
    if not isinstance(variant, str) or variant not in _RECORDS:
        raise ValueError("Unknown orthogonal transition variant; expected one of " + ", ".join(_RECORDS))
    return _RECORDS[variant]


def variant_of(piece):
    """Require the exact domain, identity, recipe, and explicit variant pairing."""
    if not isinstance(piece, Mapping):
        raise ValueError("Unreviewed orthogonal transition identity or variant")
    record = record_for(piece.get(VARIANT_FIELD, ORIGINAL))
    if (piece.get("id") != record.piece_id or piece.get("recipe") != record.recipe
            or piece.get("domain") != "highway"):
        raise ValueError("Unreviewed orthogonal transition identity or variant")
    return record.key
