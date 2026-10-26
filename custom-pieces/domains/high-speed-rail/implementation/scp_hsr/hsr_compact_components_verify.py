"""Independent literal contracts for the compact modular trumpet additions.

These dimensions were reviewed from the intended port geometry, not copied
at runtime from INFO, the route generator, or a compiled model. Coordinates
are east/north/height; support coordinates are S3D east/south. The 96 m
variants retain eight metres of flat track at each end and an 80 m eased
offset. A rejected 64 m offset failed the existing curvature-change limit;
these contracts retain that limit rather than relaxing it.
"""
from .directional_t_verify import _TURN_LIMITS

LOWER, UPPER = 15.5, 30.5
COMMON = {
    'clearance_width_m': 5., 'minimum_clearance': 5.,
    'foundation_width_m': 1.3, 'minimum_support_spacing_m': 16.,
    'allow_same_edge': False, 'required_grade_separated_crossings': 0,
    'max_grade': 0., 'flat_collar_m': 8.,
}
STRAIGHT = {
    **_TURN_LIMITS, 'max_length_ratio': 1.00001,
    'max_total_turn_degrees': .01, 'max_raw_turn_degrees': .01,
    'max_sample_turn_degrees': .01, 'signed_turn_degrees': 0.,
    'max_grade_change_per_m': .011,
}
OFFSET_96 = {
    **_TURN_LIMITS, 'max_length_ratio': 1.02,
    'min_length_m': 96., 'max_length_m': 99.,
    'max_total_turn_degrees': 40., 'signed_turn_degrees': 0.,
    'min_radius_m': 80., 'max_grade_change_per_m': .011,
}
OFFSET_128 = {
    **_TURN_LIMITS, 'max_length_ratio': 1.02,
    'min_length_m': 128., 'max_length_m': 130.,
    'max_total_turn_degrees': 30., 'signed_turn_degrees': 0.,
    'min_radius_m': 150., 'max_grade_change_per_m': .011,
}
VECTORS = {
    'Sin': (0., 1.), 'Nout': (0., 1.),
    'Nin': (0., -1.), 'Sout': (0., -1.),
}
PAIRED_MOVES = [('Sin', 'Nout'), ('Nin', 'Sout')]
CELLS_96_SPLIT = [
    (0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2),
    (0, 3), (1, 3), (0, 4), (1, 4), (0, 5),
]
CELLS_96_MERGE = [
    (0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3),
    (1, 3), (0, 4), (1, 4), (0, 5), (1, 5),
]
SUPPORTS_96_SPLIT = [
    (0., 0.), (16., 0.), (0., 16.), (16., 16.),
    (0., 32.), (0., 48.), (0., 64.), (0., 80.),
]
SUPPORTS_96_MERGE = [
    (0., 0.), (0., 16.), (0., 32.), (0., 48.),
    (0., 64.), (16., 64.), (0., 80.), (16., 80.),
]
PORTS_96 = {
    'Sin': (2., -88., LOWER), 'Nout': (2., 8., LOWER),
    'Nin': (-2., 8., LOWER), 'Sout': (-2., -88., LOWER),
}

CONTRACTS = {
    'hsr_component_upper_paired_to_single_adapter_compact': {
        **COMMON, 'kind': 'paired_to_single_adapter',
        'footprint': (2, 6), 'cells': CELLS_96_SPLIT, 'cost': 1100,
        'structural_cells': [(1, 4)],
        'ports': {
            'Sin': (2., -88., UPPER), 'Sout': (-2., -88., UPPER),
            'Nout': (16., 8., UPPER), 'Nin': (0., 8., UPPER),
        },
        'port_vectors': VECTORS, 'movements': PAIRED_MOVES,
        'min_height': UPPER, 'max_height': UPPER,
        'native_paired_south_north_m': -88.,
        'support_centres_xz': SUPPORTS_96_SPLIT,
        'quality_limits': {
            ('Sin', 'Nout'): OFFSET_96,
            ('Nin', 'Sout'): {
                **OFFSET_96, 'max_length_m': 96.1,
                'max_total_turn_degrees': 10., 'min_radius_m': 500.,
            },
        },
    },
    'hsr_component_lower_zero_turn_split_compact': {
        **COMMON, 'kind': 'parallel_split',
        'footprint': (2, 6), 'cells': CELLS_96_SPLIT, 'cost': 1100,
        'structural_cells': [(1, 4)],
        'ports': {**PORTS_96, 'Bout': (16., 8., LOWER)},
        'port_vectors': {**VECTORS, 'Bout': (0., 1.)},
        'movements': [*PAIRED_MOVES, ('Sin', 'Bout')],
        'min_height': LOWER, 'max_height': LOWER,
        'support_centres_xz': SUPPORTS_96_SPLIT,
        'quality_limits': {
            ('Sin', 'Nout'): STRAIGHT, ('Nin', 'Sout'): STRAIGHT,
            ('Sin', 'Bout'): OFFSET_96,
        },
    },
    'hsr_component_lower_zero_turn_merge_compact': {
        **COMMON, 'kind': 'parallel_merge',
        'footprint': (2, 6), 'cells': CELLS_96_MERGE, 'cost': 1100,
        'structural_cells': [(1, 1)],
        'ports': {**PORTS_96, 'Bin': (16., -88., LOWER)},
        'port_vectors': {**VECTORS, 'Bin': (0., 1.)},
        'movements': [*PAIRED_MOVES, ('Bin', 'Nout')],
        'min_height': LOWER, 'max_height': LOWER,
        'support_centres_xz': SUPPORTS_96_MERGE,
        'quality_limits': {
            ('Sin', 'Nout'): STRAIGHT, ('Nin', 'Sout'): STRAIGHT,
            ('Bin', 'Nout'): OFFSET_96,
        },
    },
    'hsr_component_lower_zero_turn_split_merge': {
        **COMMON, 'kind': 'opposing_parallel_split_merge',
        'footprint': (3, 8), 'cost': 2000,
        'cells': [
            (0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1),
            (0, 2), (1, 2), (2, 2), (0, 3), (1, 3), (2, 3),
            (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5),
            (1, 6), (1, 7),
        ],
        'structural_cells': [(0, 5), (2, 5)],
        'ports': {
            'Sin': (18., -120., LOWER), 'Nout': (18., 8., LOWER),
            'Nin': (14., 8., LOWER), 'Sout': (14., -120., LOWER),
            'Rout': (32., 8., LOWER), 'Lin': (0., 8., LOWER),
        },
        'port_vectors': {**VECTORS, 'Rout': (0., 1.), 'Lin': (0., -1.)},
        'movements': [*PAIRED_MOVES, ('Sin', 'Rout'), ('Lin', 'Sout')],
        'min_height': LOWER, 'max_height': LOWER,
        'support_centres_xz': [
            (0., 0.), (16., 0.), (32., 0.),
            (0., 16.), (16., 16.), (32., 16.),
            (0., 32.), (16., 32.), (32., 32.),
            (16., 48.), (16., 64.), (16., 80.), (16., 96.), (16., 112.),
        ],
        'quality_limits': {
            ('Sin', 'Nout'): STRAIGHT, ('Nin', 'Sout'): STRAIGHT,
            ('Sin', 'Rout'): OFFSET_128, ('Lin', 'Sout'): OFFSET_128,
        },
    },
}
