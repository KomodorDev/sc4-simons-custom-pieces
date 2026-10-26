"""Independent literal contracts for symmetric, shorter HSR junction parts.

No layout, INFO table or model writer is imported to make expected geometry.
Ports and cells are reviewed city coordinates; support coordinates are S3D
east/south. Curvature, grade, native widths and 5 x 5 m clearances keep the
established limits. The graded Y has a deliberately mirrored support plan.
"""
import math

from scp.dbpf import require
from .directional_t_verify import _TURN_LIMITS

LOWER, UPPER = 15.5, 30.5
COMMON = {
    'clearance_width_m': 5., 'minimum_clearance': 5.,
    'foundation_width_m': 1.3, 'minimum_support_spacing_m': 16.,
    'allow_same_edge': False, 'required_grade_separated_crossings': 0,
    'flat_collar_m': 8.,
}
STRAIGHT = {
    **_TURN_LIMITS, 'max_length_ratio': 1.00001,
    'max_total_turn_degrees': .01, 'max_raw_turn_degrees': .01,
    'max_sample_turn_degrees': .01, 'signed_turn_degrees': 0.,
    'max_grade_change_per_m': .011,
}
OFFSET = {
    **_TURN_LIMITS, 'max_length_ratio': 1.02,
    'min_length_m': 96., 'max_length_m': 99.,
    'max_total_turn_degrees': 40., 'signed_turn_degrees': 0.,
    'min_radius_m': 80., 'max_grade_change_per_m': .011,
}
QUARTER = {
    **_TURN_LIMITS, 'min_total_turn_degrees': 89.,
    'max_total_turn_degrees': 91., 'signed_turn_degrees': -90.,
    'min_radius_m': 50., 'max_grade_change_per_m': .011,
}

CONTRACTS = {
    'hsr_component_symmetric_graded_y': {
        **COMMON, 'kind': 'symmetric_graded_y', 'footprint': (13, 7),
        'cost': 2500, 'min_height': LOWER, 'max_height': UPPER,
        'max_grade': .156251,
        'cells': [
            (6, 0), (6, 1), (6, 2),
            (5, 3), (6, 3), (7, 3), (5, 4), (6, 4), (7, 4),
            (3, 5), (4, 5), (5, 5), (7, 5), (8, 5), (9, 5),
            (0, 6), (1, 6), (2, 6), (3, 6), (4, 6),
            (8, 6), (9, 6), (10, 6), (11, 6), (12, 6),
        ],
        'structural_cells': [(5, 3), (7, 3), (3, 5), (9, 5)],
        'ports': {
            'Nin': (94., 8., UPPER), 'Nout': (98., 8., UPPER),
            'Wout': (-8., -96., LOWER), 'Ein': (200., -96., LOWER),
        },
        'port_vectors': {
            'Nin': (0., -1.), 'Nout': (0., 1.),
            'Wout': (-1., 0.), 'Ein': (-1., 0.),
        },
        'movements': [('Nin', 'Wout'), ('Ein', 'Nout')],
        'quality_limits': {
            ('Nin', 'Wout'): {**QUARTER, 'min_length_m': 176., 'max_length_m': 179.},
            ('Ein', 'Nout'): {**QUARTER, 'min_length_m': 176., 'max_length_m': 179.},
        },
        'upper_flat_distance_m': 56., 'reflection_axis_east_m': 96.,
        'support_centres_xz': [
            (96., 0.), (96., 16.), (96., 32.),
            (0., 96.), (16., 96.), (32., 96.),
            (160., 96.), (176., 96.), (192., 96.),
            (87.038561184, 59.152402577),
            (76.242424205, 75.87085803),
            (60.294329464, 87.762381847),
            (104.961438816, 59.152402577),
            (115.757575795, 75.87085803),
            (131.705670536, 87.762381847),
        ],
    },
    'hsr_component_lower_oneway_curve90_right': {
        **COMMON, 'kind': 'single_curve', 'footprint': (7, 7),
        'cost': 1500, 'min_height': LOWER, 'max_height': LOWER,
        'max_grade': 0.,
        'cells': [
            (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
            (1, 1), (2, 1), (3, 1), (0, 2), (1, 2),
            (0, 3), (1, 3), (0, 4), (0, 5), (0, 6),
        ],
        'structural_cells': [(3, 1), (1, 3)],
        'ports': {'Sin': (0., -104., LOWER), 'Eout': (104., 0., LOWER)},
        'port_vectors': {'Sin': (0., 1.), 'Eout': (1., 0.)},
        'movements': [('Sin', 'Eout')],
        'quality_limits': {('Sin', 'Eout'): {**QUARTER, 'min_length_m': 178., 'max_length_m': 181.}},
        'support_centres_xz': [
            (64., 0.), (80., 0.), (96., 0.), (0., 64.), (0., 80.), (0., 96.),
            (3.258463782, 48.235071478), (12.964372950, 26.436553182),
            (26.436553182, 12.964372950), (48.235071478, 3.258463782),
        ],
    },
}


def _flat_for_distance(points, distance, expected_height):
    travelled = 0.
    for first, last in zip(points, points[1:]):
        length = math.dist(first[:2], last[:2])
        if travelled >= distance-2e-6:
            break
        fraction = min(1., (distance-travelled)/length)
        height = first[2]+fraction*(last[2]-first[2])
        require(abs(first[2]-expected_height) <= 2e-6 and
                abs(height-expected_height) <= 2e-6,
                'Symmetric graded Y rises before its full 56 m upper separation distance')
        travelled += length
    require(travelled >= distance-2e-6, 'Symmetric graded Y is shorter than its upper flat collar')


def _mirror(first, second, axis):
    require(len(first) == len(second), 'Symmetric component paths have unequal encoded sampling')
    error = max(math.dist((2.*axis-a[0], a[1], a[2]), b)
                for a, b in zip(first, reversed(second)))
    require(error <= 3e-6, 'Symmetric component paths are not exact mirrored reverse journeys')
    return len(first), error


def audit_refined_journeys(journeys, recipe):
    """Check reviewed symmetry and the phase of each physical level change."""
    if recipe == 'hsr_component_symmetric_graded_y':
        left, right = journeys['Nin', 'Wout'], journeys['Ein', 'Nout']
        _flat_for_distance(left, 56., UPPER)
        _flat_for_distance(list(reversed(right)), 56., UPPER)
        count, error = _mirror(left, right, 96.)
        return {'upper_flat_before_deck_separation_m': 56.,
                'mirrored_encoded_points_checked': count,
                'maximum_3d_reflection_error_m': error}
    return {}


def audit_y_native_profiles(triangles):
    """Measure real paired and single-arm slabs, caps and the paired interior."""
    from .hsr_components_verify import _section_intervals
    triangles = list(triangles)
    swapped = [tuple((p[2], p[1], p[0], p[3], p[4]) for p in triangle)
               for triangle in triangles]
    checked = 0
    for station in (.5, 4., 7.5):
        checks = [
            (triangles, -8.+station, [(88.5, 103.5)], UPPER,
             [(88.5, 90.0034523), (101.9965477, 103.5)], True),
            (swapped, -8.+station, [(92., 100.)], LOWER,
             [(92., 93.4), (98.6, 100.)], False),
            (swapped, 200.-station, [(92., 100.)], LOWER,
             [(92., 93.4), (98.6, 100.)], False),
        ]
        for surfaces, plane, expected, height, caps_expected, paired in checks:
            for actual_height, floor in ((height+.689326, True), (height-1.48933, False)):
                actual = _section_intervals(surfaces, plane, actual_height, floor=floor)
                require(len(actual) == len(expected) and all(
                    abs(a-c) < .00005 and abs(b-d) < .00005
                    for (a, b), (c, d) in zip(actual, expected)),
                    f'Symmetric graded Y native slab width, continuity or thickness differs: '
                    f'plane={plane}, height={actual_height}, intervals={actual}, expected={expected}')
                checked += 1
            caps = _section_intervals(surfaces, plane, height+1.48933)
            require(len(caps) == len(caps_expected) and all(
                abs(a-c) < .00005 and abs(b-d) < .00005
                for (a, b), (c, d) in zip(caps, caps_expected)),
                'Symmetric graded Y native parapet widths differ')
            if paired:
                for triangle in surfaces:
                    points = []
                    for a, b in zip(triangle, triangle[1:]+triangle[:1]):
                        if abs(a[2]-plane) <= 2e-6:
                            points.append(a)
                        if (a[2] < plane < b[2]) or (b[2] < plane < a[2]):
                            t = (plane-a[2])/(b[2]-a[2])
                            points.append(tuple(a[k]+t*(b[k]-a[k]) for k in range(5)))
                    require(not any(90.0036 < p[0] < 101.9964 and
                                    31.389326 < p[1] < 31.9894 for p in points),
                            'Symmetric graded Y retains an internal wall in its native paired collar')
    return {'native_y_profile_sections_checked': checked,
            'native_y_paired_slab_width_m': 15., 'native_y_arm_slab_width_m': 8.,
            'paired_collar_internal_walls': False}
