"""Generic reusable HSR straights, forks, adapters and curves.

Each definition describes one reusable standalone type. No assembly layout
or interchangeable collection of placements is defined here.
East/north/height coordinates are metres; proper rotations are anticlockwise.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import math
from .hsr_refined_components import DEFINITIONS as REFINED_DEFINITIONS, canonical as canonical_refined
from .hsr_tight_loop_components import DEFINITIONS as TIGHT_LOOP_DEFINITIONS, canonical as canonical_tight_loop

LOWER = 15.5
UPPER = 30.5

EXTRA_DEFINITIONS = {
    'hsr_component_lower_paired_straight': {
        'kind': 'lower_paired_straight', 'height': LOWER,
        'name': 'HSR L2 Two-Track Straight',
        'description': 'Native-width two-track HSR at 15.5 m with opposite-direction paths; an individually selectable lower straight.',
    },
    'hsr_component_lower_oneway_straight': {
        'kind': 'lower_oneway_straight', 'height': LOWER,
        'name': 'One-Way HSR L2 Eight-Metre Straight',
        'description': 'One centred northbound track on an eight-metre slab at 15.5 m; matches the new single-track curved ramps.',
    },
    'hsr_component_lower_zero_turn_split': {
        'kind': 'zero_turn_split', 'height': LOWER,
        'name': 'HSR L2 Parallel One-Way Split',
        'description': 'Keep the two-track mainline straight while its right-hand forward track separates into a parallel one-way track one tile away.',
    },
    'hsr_component_lower_zero_turn_merge': {
        'kind': 'zero_turn_merge', 'height': LOWER,
        'name': 'HSR L2 Parallel One-Way Merge',
        'description': 'A parallel one-way track one tile to the right merges into the forward track of the straight two-track mainline.',
    },
    'hsr_component_lower_zero_turn_double_merge': {
        'kind': 'zero_turn_double_merge', 'height': LOWER,
        'name': 'HSR L2 Opposite-Direction Parallel Merges',
        'description': 'Two outside one-way tracks merge into their matching directions of one straight two-track mainline, without crossing either track.',
    },
    'hsr_component_lower_oneway_curve90_right_wide': {
        'kind': 'lower_oneway_curve_wide', 'height': LOWER,
        'hand': 'right', 'angle': 90,
        'name': 'One-Way HSR L2 Wide 90 Degree Curve Right',
        'description': 'A centred one-way track turns right through 90 degrees at 15.5 m; 136 m displacement in each cardinal direction and flat connection collars.',
    },
    'hsr_component_upper_paired_curve90_right_wide': {
        'kind': 'upper_paired_curve_wide', 'height': UPPER,
        'hand': 'right', 'angle': 90,
        'name': 'HSR L4 Wide Two-Track 90 Degree Curve Right',
        'description': 'Two close opposite-direction tracks turn on one upper slab at 30.5 m; two copies form the large northern half-circle of the straight-stem trumpet.',
    },
    'hsr_component_upper_paired_to_single_adapter_compact': {
        'kind': 'paired_to_single_adapter_compact', 'height': UPPER,
        'name': 'HSR L4 Compact Two-Track to Separate Tracks',
        'description': 'A 96 m long upper adapter spreads native opposite-direction tracks into two eight-metre single-track decks, with centres one tile apart and matching flat collars.',
    },
    'hsr_component_lower_zero_turn_split_compact': {
        'kind': 'zero_turn_split_compact', 'height': LOWER,
        'name': 'HSR L2 Compact Parallel One-Way Split',
        'description': 'A 96 m long turnout separates the forward track into a parallel one-way track one tile to the right; the opposite mainline track remains straight.',
    },
    'hsr_component_lower_zero_turn_merge_compact': {
        'kind': 'zero_turn_merge_compact', 'height': LOWER,
        'name': 'HSR L2 Compact Parallel One-Way Merge',
        'description': 'A 96 m long turnout merges a parallel one-way track one tile to the right into the forward mainline track, while preserving the opposite straight track.',
    },
    'hsr_component_lower_zero_turn_split_merge': {
        'kind': 'zero_turn_split_merge', 'height': LOWER,
        'name': 'HSR L2 Symmetric Parallel Split and Return Merge',
        'description': 'A shared 128 m two-track stem splits a northbound track to the right and merges its mirrored southbound return from the left, with both branch ends at the north side.',
    },
}
EXTRA_DEFINITIONS.update(REFINED_DEFINITIONS)
EXTRA_DEFINITIONS.update(TIGHT_LOOP_DEFINITIONS)


def _sheet(name, points, width, start=(0., 1.), end=(0., 1.)):
    return {'name': name, 'points': points, 'width': width,
            'geometry_id': name, 'profile': 'hsr',
            'start_tangent': start, 'end_tangent': end,
            'precise_union': True, 'simplify_collinear': True,
            'extend_endpoints': 'ports', 'clearance_half_width': 2.6,
            'support': False}


@lru_cache(maxsize=2)
def _wide_quarter(displacement):
    count = 512
    headings = [math.pi/2.-math.pi/2.*(10.*(i/count)**3-15.*(i/count)**4+6.*(i/count)**5)
                for i in range(count+1)]
    xy = [(0., 0.)]
    for before, after in zip(headings, headings[1:]):
        x, y = xy[-1]
        xy.append((x+(math.cos(before)+math.cos(after))/2.,
                   y+(math.sin(before)+math.sin(after))/2.))
    scale = displacement/xy[-1][0]
    span = displacement+8.
    states = [(0., -span, math.pi/2.)]
    states.extend((x*scale, y*scale-displacement, angle)
                  for (x, y), angle in zip(xy, headings))
    states[1] = (0., -displacement, math.pi/2.)
    states[-1] = (displacement, 0., 0.)
    states.append((span, 0., 0.))
    return states


def canonical_extra(recipe):
    """Return one additional component before catalogue normalization."""
    if recipe in TIGHT_LOOP_DEFINITIONS:
        return canonical_tight_loop(recipe)
    if recipe in REFINED_DEFINITIONS:
        return canonical_refined(recipe)
    definition = EXTRA_DEFINITIONS[recipe]
    kind = definition['kind']
    if kind in ('lower_paired_straight', 'lower_oneway_straight'):
        routes = ({'S>N': [(2., -8., LOWER), (2., 8., LOWER)],
                   'N>S': [(-2., 8., LOWER), (-2., -8., LOWER)]}
                  if kind == 'lower_paired_straight' else
                  {'S>N': [(0., -8., LOWER), (0., 8., LOWER)]})
        return routes, [_sheet(kind, [(0., -8., LOWER), (0., 8., LOWER)],
                               15. if kind == 'lower_paired_straight' else 8.)]
    if kind == 'paired_to_single_adapter_compact':
        left, right = [], []
        for distance in [0., 8., *[8.+.5*i for i in range(1, 161)], 96.]:
            t = min(1., max(0., (distance-8.)/80.))
            ease = 10.*t**3-15.*t**4+6.*t**5
            left.append((-2.+2.*ease, -88.+distance, UPPER))
            right.append((2.+14.*ease, -88.+distance, UPPER))
        decks = []
        for name, points in (('compact_adapter_west', left), ('compact_adapter_east', right)):
            length = sum(math.dist(a[:2], b[:2]) for a, b in zip(points, points[1:]))
            decks.append({**_sheet(name, points, 8.),
                          'taper_extra_half_width': 1.5,
                          'taper_start_distance': 8.,
                          'taper_end_distance': length-8.})
        return {'S>N': right, 'N>S': list(reversed(left))}, decks
    if kind.startswith('zero_turn_'):
        length = 96. if kind.endswith('_compact') else 128.
        south, interior = 8.-length, length-16.
        routes = {'S>N': [(2., south, LOWER), (2., 8., LOWER)],
                  'N>S': [(-2., 8., LOWER), (-2., south, LOWER)]}
        decks = [_sheet('lower_native_main', [(0., south, LOWER), (0., 8., LOWER)], 15.)]
        def branch(first, last, reverse=False):
            points = []
            for distance in [0., 8., *[8.+.5*i for i in range(1, int(2.*interior)+1)], length]:
                t = min(1., max(0., (distance-8.)/interior))
                ease = 10.*t**3-15.*t**4+6.*t**5
                points.append((first+(last-first)*ease, south+distance, LOWER))
            return list(reversed(points)) if reverse else points
        if kind in ('zero_turn_split', 'zero_turn_split_compact', 'zero_turn_split_merge'):
            movement = 'S>R' if kind == 'zero_turn_split_merge' else 'S>B'
            routes[movement] = branch(2., 16.)
            decks.append(_sheet('parallel_split_branch', routes[movement], 8.))
            if kind == 'zero_turn_split_merge':
                routes['L>S'] = branch(-2., -16., reverse=True)
                decks.append(_sheet('parallel_return_merge', list(reversed(routes['L>S'])), 8.))
        else:
            routes['R>N' if kind == 'zero_turn_double_merge' else 'B>N'] = branch(16., 2.)
            decks.append(_sheet('parallel_merge_right', branch(16., 2.), 8.))
            if kind == 'zero_turn_double_merge':
                routes['L>S'] = branch(-2., -16., reverse=True)
                decks.append(_sheet('parallel_merge_left', branch(-2., -16.), 8.))
        return routes, decks
    paired = kind == 'upper_paired_curve_wide'
    height = UPPER if paired else LOWER
    states = _wide_quarter(192. if paired else 128.)
    center = [(x, y, height) for x, y, _ in states]
    if paired:
        routes = {
            'S>E': [(x+2.*math.sin(angle), y-2.*math.cos(angle), height) for x, y, angle in states],
            'E>S': list(reversed([(x-2.*math.sin(angle), y+2.*math.cos(angle), height) for x, y, angle in states])),
        }
        routes['S>E'][0], routes['S>E'][-1] = (2., -200., height), (200., -2., height)
        routes['E>S'][0], routes['E>S'][-1] = (200., 2., height), (-2., -200., height)
    else:
        routes = {'S>E': center}
    return routes, [_sheet(kind, center, 15. if paired else 8., (0., 1.), (1., 0.))]


