"""First-cut diagonal DD-to-ground analytical geometry, without allocation.

The fixed source frame is east/north/height. Its longitudinal direction is
southwest, its positive transverse direction is southeast, and its DD axis
is E-N=8. Each traffic/side combination is cut afresh on the city grid.
"""
from __future__ import annotations

from functools import lru_cache
import math

from . import diagonal_transition_variants as variants

SQRT2 = math.sqrt(2.0)
LENGTH = 72.0 * SQRT2
SPREAD = 16.0 * SQRT2
LANE_OFFSET = 3.2 / SQRT2
NATIVE_FORWARD_EXTENT = 5.656854586667169
NATIVE_COLLAR = 3.0
COLLAR = NATIVE_FORWARD_EXTENT + NATIVE_COLLAR
CURVE_RUN = 66.0
ACTIVE_END = COLLAR + CURVE_RUN
EASE = 8.0
STEP = 0.125
J = (8.0, 0.0)
LONGITUDINAL_EN = (-1.0 / SQRT2, -1.0 / SQRT2)
TRANSVERSE_EN = (1.0 / SQRT2, -1.0 / SQRT2)
BREAKS = tuple(sorted({0.0, COLLAR, COLLAR + EASE, ACTIVE_END,
                       LENGTH - COLLAR - EASE, LENGTH - COLLAR, LENGTH}))
STATIONS = tuple(sorted({index * STEP for index in range(int(LENGTH / STEP) + 1)} | set(BREAKS)))


def is_mirrored(variant="original"):
    return variants.record_for(variant).physical_reflection


def traffic_reversed(variant="original"):
    return variants.record_for(variant).traffic_reversed


def native_cross_section_reflected(variant="original"):
    """Local normal convention only; this does not transform native resources."""
    record = variants.record_for(variant)
    return record.physical_reflection != record.traffic_reversed


def _unit(value):
    return min(1.0, max(0.0, value))


def cubic(value):
    t = _unit(value)
    return t * t * (3.0 - 2.0 * t)


def upper_plan(station, *, variant="original"):
    """Return transverse p, dp/ds, and d2p/ds2, from the fixed DD axis."""
    record = variants.record_for(variant)
    t = _unit((station - COLLAR) / CURVE_RUN)
    sign = 1.0 if record.physical_reflection else -1.0
    p = sign * SPREAD * t ** 3 * (10.0 - 15.0 * t + 6.0 * t * t)
    first = sign * SPREAD * 30.0 * t * t * (1.0 - t) ** 2 / CURVE_RUN
    second = sign * SPREAD * 60.0 * t * (1.0 - t) * (1.0 - 2.0 * t) / CURVE_RUN ** 2
    return p, first, second


def upper_weight(station):
    _p, derivative, second = upper_plan(station)
    speed = math.hypot(1.0, derivative)
    curvature = second / speed ** 3
    easing = cubic((station - COLLAR) / EASE) * cubic((LENGTH - COLLAR - station) / EASE)
    return easing * speed * (1.0 - LANE_OFFSET * math.sqrt(curvature ** 2 + .001 ** 2))


def _simpson(function, left, right, tolerance=2e-12):
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


@lru_cache(maxsize=4096)
def weight_integral(station):
    finish = min(LENGTH - COLLAR, max(COLLAR, float(station)))
    cuts = [COLLAR] + [v for v in BREAKS if COLLAR < v < finish] + [finish]
    return sum(_simpson(upper_weight, first, last) for first, last in zip(cuts, cuts[1:]))


@lru_cache(maxsize=1)
def normalized_upper_grade():
    return 15.0 / weight_integral(LENGTH)


def height(deck, station):
    if not math.isfinite(station):
        raise ValueError("Diagonal transition station must be finite")
    if deck == "lower":
        return 7.5 * (1.0 - cubic((station - COLLAR) / CURVE_RUN))
    if deck != "upper":
        raise ValueError("Diagonal transition has only upper and lower decks")
    if station <= COLLAR:
        return 15.0
    if station >= LENGTH - COLLAR:
        return 0.0
    return 15.0 - normalized_upper_grade() * weight_integral(float(station))


def frame(deck, station, *, variant="original"):
    """Return world centre EN and reflected canonical section normal EN.

    Reflection defines a new analytical curve about the fixed DD axis. It
    carries no claim that city cells, helper poses, or native meshes reflect.
    """
    record = variants.record_for(variant)
    if deck == "upper":
        p, derivative, _second = upper_plan(station, variant=variant)
    elif deck == "lower":
        p, derivative = 0.0, 0.0
    else:
        raise ValueError("Unknown diagonal transition deck")
    speed = math.hypot(1.0, derivative)
    orientation = -1.0 if record.physical_reflection else 1.0
    centre = tuple(J[i] + p * TRANSVERSE_EN[i] + station * LONGITUDINAL_EN[i] for i in range(2))
    normal = tuple(orientation * (TRANSVERSE_EN[i] - derivative * LONGITUDINAL_EN[i]) / speed for i in range(2))
    return centre, normal


def model_point(deck, station, lateral, vertical=0.0, *, variant="original"):
    centre, normal = frame(deck, station, variant=variant)
    return (centre[0] + lateral * normal[0], height(deck, station) + vertical,
            -centre[1] - lateral * normal[1])


def lane_lateral(deck, lane, *, variant="original"):
    if lane not in (0, 1) or type(lane) is not int:
        raise ValueError("Each diagonal carriageway has two native DD classes, 0 and 1")
    if deck not in ("upper", "lower"):
        raise ValueError("Unknown diagonal transition deck")
    source = 1 - lane if native_cross_section_reflected(variant) else lane
    return ((-LANE_OFFSET, LANE_OFFSET) if deck == "upper" else (LANE_OFFSET, -LANE_OFFSET))[source]


def lane_point(deck, lane, station, *, variant="original"):
    e, h, south = model_point(deck, station, lane_lateral(deck, lane, variant=variant), variant=variant)
    return e, -south, h


def lane_stations(deck, lane, *, variant="original"):
    lateral = lane_lateral(deck, lane, variant=variant)
    physical_lateral = (-1.0 if is_mirrored(variant) else 1.0) * lateral
    first, last = physical_lateral, LENGTH - physical_lateral
    grid = {index * STEP for index in range(math.floor(first / STEP), math.ceil(last / STEP) + 1)
            if first < index * STEP < last}
    return tuple(sorted({first, last} | grid | {s for s in BREAKS if first < s < last}))


def traffic_routes(*, variant="original"):
    record = variants.record_for(variant)
    routes = []
    for deck in ("upper", "lower"):
        for lane in (0, 1):
            stations = lane_stations(deck, lane, variant=variant)
            if (deck == "upper") == record.traffic_reversed:
                stations = tuple(reversed(stations))
            routes.append({"id": f"{deck}-lane-{lane}", "transport": 1, "lane": lane,
                "junction": False, "points": [lane_point(deck, lane, s, variant=variant) for s in stations]})
    return routes


def native_socket_plan(*, variant="original"):
    record = variants.record_for(variant)
    side = 1 if record.physical_reflection else -1
    return {
        "dd": {"outside_cell": [1, 0], "end_cell": [0, 0], "cut": ["east", 8.0],
               "donor": "57530200" if record.traffic_reversed else "57530900", "pose": 2,
               "outward_peer_cell": [1, -1],
               "outward_peer_donor": "57530900" if record.traffic_reversed else "57530200", "outward_peer_pose": 0},
        "lower_ground": {"outside_cell": [-4, 5], "end_cell": [-4, 4], "cut": ["north", -72.0],
                         "donor": "57030900" if record.traffic_reversed else "57030200", "pose": 2},
        "upper_ground": {"outside_cell": [-3, 6] if side > 0 else [-5, 4],
                         "end_cell": [-3, 5] if side > 0 else [-5, 3],
                         "cut": ["north", -88.0 if side > 0 else -56.0],
                         "donor": "57030200" if record.traffic_reversed else "57030900", "pose": 2},
    }


def pavement_datum(deck, station):
    """Middle-body datum; literal native collar regions retain their own phase."""
    if deck not in ("upper", "lower"):
        raise ValueError("Unknown diagonal transition deck")
    native_height = 15.0 if deck == "upper" else 7.5
    datum = .0010004043579101562 if deck == "upper" else .0009999275207519531
    return datum * height(deck, station) / native_height


def underside_height(deck, station):
    roof = height(deck, station) + pavement_datum(deck, station)
    return max(0.0, roof - 1.0)


def support_specifications(*, variant="original"):
    """Proposed complete solids, newly positioned in this diagonal frame.

    Flat cap tops meet the middle underside and may embed finitely into that
    slab as its longitudinal height changes. This is no full-top contact or
    structural-capacity claim. Saved solids and their actual contacts remain
    independently checked before this layout can be accepted.
    """
    variants.record_for(variant)
    result = []
    for reference in (12.0, 32.0, 52.0, 72.0):
        station = reference * LENGTH / 96.0
        top = underside_height("upper", station)
        outside = -9.2 if reference == 12.0 else -6.4
        result.extend((
            {"id": f"upper-pier-{int(reference)}", "deck": "upper", "station_m": station,
             "lateral_range_m": [outside - .4, outside + .4], "station_half_length_m": .4,
             "bottom_m": 0.0, "top_m": top - .3},
            {"id": f"upper-cap-{int(reference)}", "deck": "upper", "station_m": station,
             "lateral_range_m": [min(-7.0, outside - .4), 7.0], "station_half_length_m": .45,
             "bottom_m": top - .3, "top_m": top}))
    for reference in (12.0, 32.0, 48.0):
        station = reference * LENGTH / 96.0
        for side in (-1, 1):
            result.append({"id": f"lower-pier-{int(reference)}-{side}", "deck": "lower",
                "station_m": station, "lateral_range_m": [side * 6.4 - .4, side * 6.4 + .4],
                "station_half_length_m": .4, "bottom_m": 0.0,
                "top_m": underside_height("lower", station)})
    for row in result:
        s, half = row["station_m"], row["station_half_length_m"]
        u0, u1 = row["lateral_range_m"]
        row["corners_EN_m"] = [[model_point(row["deck"], t, u, variant=variant)[0],
            -model_point(row["deck"], t, u, variant=variant)[2]]
            for t, u in ((s - half, u0), (s + half, u0), (s + half, u1), (s - half, u1))]
        if row["top_m"] <= row["bottom_m"]:
            raise ValueError("A diagonal support solid collapsed")
    return tuple(result)


def engineering_metadata(*, variant="original"):
    record = variants.record_for(variant)
    return {"diagonal_transition_variant": record.key, "diagonal_transition_alignment": "a",
        "source_scope": "Analytical first-cut source; physical mask, saved resources, and game behavior require separate acceptance",
        "frame": {"mouth_EN_m": list(J), "longitudinal_unit_EN": list(LONGITUDINAL_EN),
                  "transverse_unit_EN": list(TRANSVERSE_EN), "DD_and_lower_axis": "E-N=8",
                  "upper_ground_axis": "E-N=40" if record.physical_reflection else "E-N=-24"},
        "nominal_axis_run_m": LENGTH, "ground_axis_spacing_m": SPREAD,
        "native_lane_offset_m": LANE_OFFSET, "physical_flat_envelope_m": COLLAR,
        "source_forward_extent_m": NATIVE_FORWARD_EXTENT, "literal_native_collar_m": NATIVE_COLLAR,
        "sideways_curve_run_m": CURVE_RUN, "upper_grade_ease_m": EASE,
        "station_step_m": STEP, "station_sampling": "0.125m source grid plus exact profile breaks and lane-dependent cut endpoints",
        "height_integration": "Adaptive Simpson per smooth interval, absolute target2e-12, depth20",
        "upper_normalized_grade_bound": normalized_upper_grade(), "lower_peak_grade": 7.5 * 1.5 / CURVE_RUN,
        "native_cross_section_reflected_in_canonical_frame": native_cross_section_reflected(variant),
        "cell_transform_policy": "Fresh city-grid clipping and native reconstruction per variant; no reflected-mask equivalence",
        "middle_body_floor_policy": "Native309 datum faded with PATH height; one metre below roof, clamped to ground",
        "native_shoulder_depth_policy": "Literal native302 shoulders and body feet require their own finite measured scope; no old exception is inherited",
        "support_plan": {"solids": 14, "scope": "Proposed diagonal volumes; saved closed faces, contact, and full clearance are pending",
                         "cap_contact": "Flat cap centre meets the served underside; finite own-slab embedding is checked from actual meshes"},
        "native_sockets": native_socket_plan(variant=variant), "in_game_status": "unverified"}
