"""Independent literal contracts for the seven complete-trumpet additions.

These expectations do not import the layout or model generator. Coordinates
are east, north, height in metres; support coordinates use S3D east/south.
"""
from .directional_t_verify import _TURN_LIMITS

LOWER, UPPER = 15.5, 30.5
COMMON = {'clearance_width_m': 5., 'minimum_clearance': 5.,
          'foundation_width_m': 1.3, 'minimum_support_spacing_m': 16.,
          'allow_same_edge': False, 'required_grade_separated_crossings': 0,
          'max_grade': 0., 'flat_collar_m': 8.}
STRAIGHT = {**_TURN_LIMITS, 'max_length_ratio': 1.00001,
            'max_total_turn_degrees': .01, 'max_raw_turn_degrees': .01,
            'max_sample_turn_degrees': .01, 'signed_turn_degrees': 0.,
            'max_grade_change_per_m': .011}
OFFSET = {**_TURN_LIMITS, 'max_length_ratio': 1.02,
          'max_total_turn_degrees': 30., 'signed_turn_degrees': 0.,
          'min_length_m': 128., 'max_length_m': 130.,
          'max_grade_change_per_m': .011}
QUARTER = {**_TURN_LIMITS, 'min_total_turn_degrees': 89.,
           'max_total_turn_degrees': 91., 'signed_turn_degrees': -90.,
           'max_grade_change_per_m': .011}


def cells(rows):
    return [(x, row) for row, mask in enumerate(rows)
            for x, value in enumerate(mask) if value == '#']


def paired_ports(x=0., south=-120., north=8., height=LOWER):
    return {'Sin': (x+2., south, height), 'Nout': (x+2., north, height),
            'Nin': (x-2., north, height), 'Sout': (x-2., south, height)}


VECTORS = {'Sin': (0., 1.), 'Nout': (0., 1.),
           'Nin': (0., -1.), 'Sout': (0., -1.)}
PAIRED_MOVES = [('Sin', 'Nout'), ('Nin', 'Sout')]
CONTRACTS = {
    'hsr_component_lower_paired_straight': {
        **COMMON, 'kind': 'paired_straight', 'footprint': (1, 1),
        'cells': [(0, 0)], 'cost': 100,
        'ports': paired_ports(south=-8.), 'port_vectors': VECTORS,
        'movements': PAIRED_MOVES, 'min_height': LOWER, 'max_height': LOWER,
        'support_centres_xz': [(0., 0.)],
    },
    'hsr_component_lower_oneway_straight': {
        **COMMON, 'kind': 'single_straight', 'footprint': (1, 1),
        'cells': [(0, 0)], 'cost': 100,
        'ports': {'Sin': (0., -8., LOWER), 'Nout': (0., 8., LOWER)},
        'port_vectors': {'Sin': (0., 1.), 'Nout': (0., 1.)},
        'movements': [('Sin', 'Nout')], 'min_height': LOWER, 'max_height': LOWER,
        'support_centres_xz': [(0., 0.)],
    },
    'hsr_component_lower_zero_turn_split': {
        **COMMON, 'kind': 'parallel_split', 'footprint': (2, 8), 'cost': 1400,
        'cells': cells(['##', '##', '##', '##', '##', '##', '#.', '#.']),
        'structural_cells': [(1, 5)],
        'ports': {**paired_ports(), 'Bout': (16., 8., LOWER)},
        'port_vectors': {**VECTORS, 'Bout': (0., 1.)},
        'movements': [*PAIRED_MOVES, ('Sin', 'Bout')],
        'min_height': LOWER, 'max_height': LOWER,
        'quality_limits': {('Sin', 'Nout'): STRAIGHT,
                           ('Nin', 'Sout'): STRAIGHT, ('Sin', 'Bout'): OFFSET},
        'support_centres_xz': [(0., 0.), (16., 0.), (0., 16.), (16., 16.),
            (0., 32.), (16., 32.), (0., 48.), (0., 64.), (0., 80.),
            (0., 96.), (0., 112.)],
    },
    'hsr_component_lower_zero_turn_merge': {
        **COMMON, 'kind': 'parallel_merge', 'footprint': (2, 8), 'cost': 1400,
        'cells': cells(['#.', '#.', '##', '##', '##', '##', '##', '##']),
        'structural_cells': [(1, 2)],
        'ports': {**paired_ports(), 'Bin': (16., -120., LOWER)},
        'port_vectors': {**VECTORS, 'Bin': (0., 1.)},
        'movements': [*PAIRED_MOVES, ('Bin', 'Nout')],
        'min_height': LOWER, 'max_height': LOWER,
        'quality_limits': {('Sin', 'Nout'): STRAIGHT,
                           ('Nin', 'Sout'): STRAIGHT, ('Bin', 'Nout'): OFFSET},
        'support_centres_xz': [(0., 0.), (0., 16.), (0., 32.), (0., 48.),
            (0., 64.), (0., 80.), (16., 80.), (0., 96.), (16., 96.),
            (0., 112.), (16., 112.)],
    },
    'hsr_component_lower_zero_turn_double_merge': {
        **COMMON, 'kind': 'opposing_parallel_merges', 'footprint': (3, 8), 'cost': 2000,
        'cells': cells(['##.', '##.', '###', '###', '###', '###', '.##', '.##']),
        'structural_cells': [(2, 2), (0, 5)],
        'ports': {**paired_ports(x=16.), 'Rin': (32., -120., LOWER),
                  'Lin': (0., 8., LOWER)},
        'port_vectors': {**VECTORS, 'Rin': (0., 1.), 'Lin': (0., -1.)},
        'movements': [*PAIRED_MOVES, ('Rin', 'Nout'), ('Lin', 'Sout')],
        'min_height': LOWER, 'max_height': LOWER,
        'quality_limits': {('Sin', 'Nout'): STRAIGHT, ('Nin', 'Sout'): STRAIGHT,
                           ('Rin', 'Nout'): OFFSET, ('Lin', 'Sout'): OFFSET},
        'support_centres_xz': [(0., 0.), (16., 0.), (0., 16.), (16., 16.),
            (0., 32.), (16., 32.), (16., 48.), (16., 64.), (16., 80.),
            (32., 80.), (16., 96.), (32., 96.), (16., 112.), (32., 112.)],
    },
    'hsr_component_lower_oneway_curve90_right_wide': {
        **COMMON, 'kind': 'single_curve', 'footprint': (9, 9), 'cost': 2000,
        'cells': cells(['...######', '.####....', '.##......', '##.......',
                        '##.......', '#........', '#........', '#........', '#........']),
        'structural_cells': [(1, 1), (4, 1), (1, 4)],
        'ports': {'Sin': (0., -136., LOWER), 'Eout': (136., 0., LOWER)},
        'port_vectors': {'Sin': (0., 1.), 'Eout': (1., 0.)},
        'movements': [('Sin', 'Eout')], 'min_height': LOWER, 'max_height': LOWER,
        'quality_limits': {('Sin', 'Eout'): {**QUARTER, 'min_radius_m': 65.,
                           'min_length_m': 232., 'max_length_m': 236.}},
        'support_centres_xz': [(80., 0.), (96., 0.), (112., 0.), (128., 0.),
            (32., 16.), (16., 32.), (0., 80.), (0., 96.), (0., 112.), (0., 128.),
            (4.344663574, 64.313466811), (47.778785174, 10.087270968)],
    },
    'hsr_component_upper_paired_curve90_right_wide': {
        **COMMON, 'kind': 'paired_curve', 'footprint': (13, 13), 'cost': 3800,
        'cells': cells(['....#########', '...#######...', '..###........',
            '.###.........', '###..........', '##...........', '##...........',
            '##...........', '##...........', '##...........', '#............',
            '#............', '#............']),
        'structural_cells': [(4, 0), (7, 1), (8, 1), (9, 1), (3, 3), (0, 4),
                             (1, 7), (1, 8), (1, 9)],
        'ports': {'Sin': (2., -200., UPPER), 'Sout': (-2., -200., UPPER),
                  'Eout': (200., -2., UPPER), 'Ein': (200., 2., UPPER)},
        'port_vectors': {'Sin': (0., 1.), 'Sout': (0., -1.),
                         'Eout': (1., 0.), 'Ein': (-1., 0.)},
        'movements': [('Sin', 'Eout'), ('Ein', 'Sout')],
        'min_height': UPPER, 'max_height': UPPER,
        'quality_limits': {
            ('Sin', 'Eout'): {**QUARTER, 'min_radius_m': 95.,
                             'min_length_m': 338., 'max_length_m': 347.},
            ('Ein', 'Sout'): {**QUARTER, 'min_radius_m': 95.,
                             'min_length_m': 338., 'max_length_m': 347.,
                             'signed_turn_degrees': 90.}},
        'support_centres_xz': [(96., 0.), (112., 0.), (128., 0.), (144., 0.),
            (160., 0.), (176., 0.), (192., 0.), (64., 16.), (80., 16.),
            (48., 32.), (32., 48.), (16., 64.), (16., 80.), (0., 96.),
            (0., 112.), (0., 128.), (0., 144.), (0., 160.), (0., 176.), (0., 192.)],
    },
}
