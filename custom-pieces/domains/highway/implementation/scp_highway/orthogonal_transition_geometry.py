"""Approved six-tile orthogonal DD-to-ground geometry, without allocation.

Model coordinates are east, height, and south. PATH coordinates are east,
north, and height. Station s runs south from the entry at model z=-8 m.
The upper deck moves west while both directions descend; no lane changes
or transfers between the two carriageways are introduced.
"""
from __future__ import annotations

from functools import lru_cache
import math

LENGTH = 96.0
COLLAR = 3.0
ACTIVE_END = 69.0
EASE = 12.0
STEP = 0.25
CELLS = tuple((column, row) for row in range(6) for column in range(2))
MODEL_ONLY_CELLS = ((0, 0),)
STATIONS = tuple(index * STEP for index in range(int(LENGTH / STEP) + 1))
BREAKS = (0.0, 3.0, 15.0, 36.0, 69.0, 81.0, 93.0, 96.0)


def is_mirrored(variant):
    """Require an explicit supported source variant; rotations are separate."""
    if variant not in ("original", "mirrored") or not isinstance(variant, str):
        raise ValueError("Orthogonal transition variant must be 'original' or 'mirrored'")
    return variant == "mirrored"


def model_only_cells(*, variant="original"):
    return ((1, 0),) if is_mirrored(variant) else MODEL_ONLY_CELLS


def _unit(value):
    return min(1.0, max(0.0, value))


def cubic(value):
    t = _unit(value)
    return t * t * (3.0 - 2.0 * t)


def upper_plan(station, *, variant="original"):
    """Return centre x, dx/ds, and d²x/ds² in the approved fixed frame."""
    t = _unit((station - COLLAR) / (ACTIVE_END - COLLAR))
    x = 16.0 * (1.0 - t ** 3 * (10.0 - 15.0 * t + 6.0 * t * t))
    if station <= COLLAR or station >= ACTIVE_END:
        return (16.0 - x, 0.0, 0.0) if is_mirrored(variant) else (x, 0.0, 0.0)
    run = ACTIVE_END - COLLAR
    first = -16.0 * 30.0 * t * t * (1.0 - t) ** 2 / run
    second = -16.0 * 60.0 * t * (1.0 - t) * (1.0 - 2.0 * t) / run ** 2
    return (16.0 - x, -first, -second) if is_mirrored(variant) else (x, first, second)


def upper_weight(station):
    """Conservative actual-lane speed times the approved flat-end easing."""
    _x, first, second = upper_plan(station)
    speed = math.hypot(1.0, first)
    curvature = second / speed ** 3
    easing = cubic((station - COLLAR) / EASE) * cubic((LENGTH - COLLAR - station) / EASE)
    return easing * speed * (1.0 - 2.5 * math.sqrt(curvature ** 2 + 0.001 ** 2))


def _simpson(function, left, right, tolerance=2e-12):
    """Deterministic adaptive Simpson integration on one smooth interval."""
    if right <= left:
        return 0.0
    middle = (left + right) / 2.0
    a, b, c = function(left), function(middle), function(right)
    whole = (right - left) * (a + 4.0 * b + c) / 6.0

    def refine(lo, hi, fa, fm, fb, estimate, error, depth):
        mid = (lo + hi) / 2.0
        fl, fr = function((lo + mid) / 2.0), function((mid + hi) / 2.0)
        first = (mid - lo) * (fa + 4.0 * fl + fm) / 6.0
        last = (hi - mid) * (fm + 4.0 * fr + fb) / 6.0
        difference = first + last - estimate
        if depth == 0 or abs(difference) <= 15.0 * error:
            return first + last + difference / 15.0
        return (refine(lo, mid, fa, fl, fm, first, error / 2.0, depth - 1)
                + refine(mid, hi, fm, fr, fb, last, error / 2.0, depth - 1))

    return refine(left, right, a, b, c, whole, tolerance, 20)


@lru_cache(maxsize=None)
def weight_integral(station):
    finish = min(LENGTH - COLLAR, max(COLLAR, float(station)))
    cuts = [COLLAR] + [v for v in BREAKS if COLLAR < v < finish] + [finish]
    return sum(_simpson(upper_weight, first, last) for first, last in zip(cuts, cuts[1:]))


@lru_cache(maxsize=1)
def normalized_upper_grade():
    return 15.0 / weight_integral(LENGTH)


def height(deck, station):
    if deck == "lower":
        return 7.5 * (1.0 - cubic((station - COLLAR) / (ACTIVE_END - COLLAR)))
    if deck != "upper":
        raise ValueError("The orthogonal transition has only upper and lower decks")
    if station <= COLLAR:
        return 15.0
    if station >= LENGTH - COLLAR:
        return 0.0
    return 15.0 - normalized_upper_grade() * weight_integral(float(station))


def frame(deck, station, *, variant="original"):
    """Return the centre and reflected canonical normal for level sections."""
    if deck == "upper":
        east, derivative, _second = upper_plan(station)
    elif deck == "lower":
        east, derivative = 16.0, 0.0
    else:
        raise ValueError("Unknown transition deck")
    speed = math.hypot(1.0, derivative)
    if is_mirrored(variant):
        return (16.0 - east, station - 8.0), (-1.0 / speed, -derivative / speed)
    return (east, station - 8.0), (1.0 / speed, -derivative / speed)


def model_point(deck, station, lateral, vertical=0.0, *, variant="original"):
    (east, south), normal = frame(deck, station, variant=variant)
    return (east + lateral * normal[0], height(deck, station) + vertical,
            south + lateral * normal[1])


def lane_point(deck, lane, station, *, variant="original"):
    """Return the exact native-class lane centre as a PATH-space point."""
    if lane not in (0, 1):
        raise ValueError("Each transition carriageway has exactly two lanes")
    lateral = (-2.5, 2.5)[lane] if deck == "upper" else (2.5, -2.5)[lane]
    east, altitude, south = model_point(deck, station, lateral, variant=variant)
    return east, -south, altitude


def traffic_routes(*, variant="original"):
    """Four complete sampled routes, before the single city-lattice cut."""
    routes = []
    for deck in ("upper", "lower"):
        stations = STATIONS if (deck == "upper") != is_mirrored(variant) else reversed(STATIONS)
        ordered = tuple(stations)
        for lane in (0, 1):
            routes.append({"id": f"{deck}-lane-{lane}", "transport": 1, "lane": lane,
                           "junction": False,
                           "points": [lane_point(deck, lane, s, variant=variant) for s in ordered]})
    return routes


def engineering_metadata(*, variant="original"):
    """Authored parameters and calculated facts; no saved-resource or game claims."""
    result = {"length_m": LENGTH, "width_m": 32.0, "footprint_tiles": [2, 6],
            "cells": [list(c) for c in CELLS], "model_only_cells": [list(c) for c in model_only_cells(variant=variant)],
            "entry_station_model_z_m": -8.0, "exit_station_model_z_m": 88.0,
            "native_collar_m": COLLAR, "lateral_and_lower_active_m": [COLLAR, ACTIVE_END],
            "upper_grade_easing_m": EASE, "path_station_step_m": STEP,
            "upper_normalized_grade": normalized_upper_grade(),
            "upper_height_at_complete_spread_m": height("upper", ACTIVE_END),
            "lower_maximum_grade": 7.5 * 1.5 / (ACTIVE_END - COLLAR),
            "cross_section_policy": "Flat horizontal normal sections; true lane-speed curvature compensation",
            "path_runtime_use_elevation": True,
            "software_resource_verification": "not supplied by the generator",
            "in_game_status": "unverified"}
    if is_mirrored(variant):
        result.update({"transition_variant": "mirrored", "reflection_axis_east_m": 8.0,
                       "geometry_transform": "East x becomes 16 minus x; height and north coordinates unchanged",
                       "directed_path_transform": "Reflect each complete lane and reverse its directed point sequence; retain native lane classes",
                       "dd_axis_east_m": 0.0, "ground_upper_axis_east_m": 16.0,
                       "ground_lower_axis_east_m": 0.0,
                       "upper_travel_direction": "northbound", "lower_travel_direction": "southbound"})
    return result
