"""Reviewed Alignment A diagonal transition source ownership.

Each choice owns 24 cells: 15 routed and nine model-only, with 39 terrain corners.
All four source05 encoded models, finite native collars, supports, and
ownership passed independent physical review. Normal DAT verification,
installation, and game observations remain separate gates.
"""
from __future__ import annotations

from functools import lru_cache
import math

from shapely.geometry import Polygon, box
from shapely.ops import unary_union

from . import diagonal_transition_geometry as geometry
from . import diagonal_transition_variants as variants
from .ramp_paths import slice_routes

PHYSICAL_LAYOUT_REVIEWED = True
NATIVE_SHOULDER_OWNERSHIP_REVIEWED = True


def is_reserved_native_cell(cell, *, variant="original"):
    """Protect complete infinite native strings, including each outside peer."""
    c, r = cell
    if c >= 1 and r in (1 - c, -c):
        return True
    sockets = geometry.native_socket_plan(variant=variant)
    for key in ("upper_ground", "lower_ground"):
        a, b = sockets[key]["outside_cell"]
        k = r - b
        if k >= 0 and c in (a - k, a - k - 1):
            return True
    return False


@lru_cache(maxsize=4)
def path_cells(*, variant="original"):
    variants.record_for(variant)
    return tuple(sorted(slice_routes(geometry.traffic_routes(variant=variant))))


def _road_outline(deck, variant):
    stations = (-12.0, *geometry.STATIONS, geometry.LENGTH + 12.0)
    edges = []
    for lateral, order in ((-8.0, stations), (8.0, reversed(stations))):
        for s in order:
            e, _h, south = geometry.model_point(deck, s, lateral, variant=variant)
            edges.append((e, -south))
    north_cut = geometry.native_socket_plan(variant=variant)[deck + "_ground"]["cut"][1]
    return Polygon(edges).intersection(box(-200.0, north_cut, 8.0, 100.0))


@lru_cache(maxsize=4)
def nominal_physical_world_cells(*, variant="original"):
    """Conservative nominal 16 m roads plus complete reviewed support footprints."""
    variants.record_for(variant)
    footprint = unary_union([_road_outline(deck, variant) for deck in ("upper", "lower")]
        + [Polygon(row["corners_EN_m"]) for row in geometry.support_specifications(variant=variant)])
    min_e, min_n, max_e, max_n = footprint.bounds
    result = []
    for c in range(math.floor((min_e + 8) / 16), math.floor((max_e + 8) / 16) + 1):
        for r in range(math.floor((8 - max_n) / 16), math.floor((8 - min_n) / 16) + 1):
            # A line-only cell touch owns no model area. Finite native collar
            # ownership is separately proved from the actual source models.
            if footprint.intersection(box(16*c-8, -16*r-8, 16*c+8, -16*r+8)).area > 1e-10:
                result.append((c, r))
    return tuple(sorted(result))


@lru_cache(maxsize=4)
def world_cells(*, variant="original"):
    """Reviewed 24 custom hosts; every native outside/helper cell stays unowned."""
    result = tuple(sorted({cell for cell in nominal_physical_world_cells(variant=variant)
                          if not is_reserved_native_cell(cell, variant=variant)} | {(1, 1)}))
    if not set(path_cells(variant=variant)) <= set(result):
        raise ValueError("A first-cut source PATH enters a reserved native corridor")
    return result


def world_origin_cell(*, variant="original"):
    owned = world_cells(variant=variant)
    return min(c for c, _ in owned), min(r for _, r in owned)


def cells(*, variant="original"):
    origin = world_origin_cell(variant=variant)
    return tuple((c-origin[0], r-origin[1]) for c,r in world_cells(variant=variant))


def footprint(*, variant="original"):
    owned = cells(variant=variant)
    return max(c for c,_ in owned)+1, max(r for _,r in owned)+1


def model_only_cells(*, variant="original"):
    paths = set(path_cells(variant=variant)); origin = world_origin_cell(variant=variant)
    return tuple((c-origin[0],r-origin[1]) for c,r in world_cells(variant=variant) if (c,r) not in paths)


def flat_base_vertices(*, variant="original"):
    """Actual terrain-corner graph of the selected city-cell mask."""
    return tuple(sorted({(c+dc,r+dr) for c,r in cells(variant=variant)
                         for dc,dr in ((0,0),(1,0),(0,1),(1,1))}))


def module_catalog():
    rows = []
    for key in variants.VARIANTS:
        record = variants.record_for(key)
        name = "DD RHW-4 — L1/L2 ↔ RHW-4 L0 — "
        name += "Mirrored Diagonal Ramp" if record.traffic_reversed else "Diagonal Ramp"
        if record.opposite_side:
            name += " — Opposite Upper Descent"
        name += " — Alignment A"
        rows.append({"key": key, "id": record.piece_id, "recipe": record.recipe,
            "name": name,
            "diagonal_transition_variant": key, "diagonal_transition_alignment": "a",
            "cells": [list(c) for c in cells(variant=key)], "footprint": list(footprint(variant=key)),
            "world_origin_cell": list(world_origin_cell(variant=key)),
            "engineering": {**geometry.engineering_metadata(variant=key),
                "source_scope": "Reviewed Alignment A source05 encoded physical geometry and ownership; normal DAT verification, installation, and game observations are separate gates",
                "physical_layout_reviewed": PHYSICAL_LAYOUT_REVIEWED,
                "native_shoulder_ownership_reviewed": NATIVE_SHOULDER_OWNERSHIP_REVIEWED,
                "physical_source_review": {
                    "snapshot_sha256": "43f0c7a936ad07b227768d21e7f1ceb183f96a728f38a50d0c9fed169cf703a6",
                    "verification_sha256": "cfdb0b02add5f59c7084e42d895252de26e8da076b1e79bfd94b2c10beb38f27",
                    "scope": "Independent ordered physical checks of all four choices and 196 actual encoded source payloads; no game acceptance"},
                "support_plan": {**geometry.engineering_metadata(variant=key)["support_plan"],
                    "scope": "Fourteen complete diagonal support solids independently checked in source05 for closed faces, contact, and full clearance; normal DAT and game checks are separate"},
                "native_shoulder_depth_policy": "Reviewed first-A finite 302/309 profiles and source-only original native union; every authored floor and wall is retained, and no old exception is inherited",
                "model_only_cells": [list(c) for c in model_only_cells(variant=key)],
                "native_DD_authored_shoulder_host_world_cells": [[1,1]],
                "flat_base_corner_vertices": len(flat_base_vertices(variant=key)),
                "ownership_scope": "Reviewed source05 mask: 24 owned cells, 15 routed and nine model-only, with 39 terrain corners; actual native collars, source-parent shoulder hosting, and complete supports checked while all native approach corridors remain unowned",
                "excluded_native_corridor_cells": [list(c) for c in nominal_physical_world_cells(variant=key)
                    if is_reserved_native_cell(c, variant=key)]}})
    return {"alignment": "a", "physical_layout_reviewed": PHYSICAL_LAYOUT_REVIEWED,
            "native_shoulder_ownership_reviewed": NATIVE_SHOULDER_OWNERSHIP_REVIEWED, "types": rows}


def declaration(spec):
    key = variants.variant_of(spec)
    row = next(row for row in module_catalog()["types"] if row["key"] == key)
    if spec.get("cells") != row["cells"] or spec.get("footprint") != row["footprint"]:
        raise ValueError("Diagonal transition allocation disagrees with the first-cut layout")
    return row
