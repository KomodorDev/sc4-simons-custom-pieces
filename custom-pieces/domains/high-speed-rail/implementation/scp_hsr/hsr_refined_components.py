"""Coordinated symmetric connections for the shorter modular HSR trumpet.

Each definition is an independently selectable track component. Existing
components retain their original geometry. Coordinates are east, north and
rail-path height in metres, before construction-cell normalization.
"""
from __future__ import annotations

from functools import lru_cache
import math

LOWER, UPPER = 15.5, 30.5

DEFINITIONS = {
    'hsr_component_symmetric_graded_y': {
        'kind': 'symmetric_graded_y', 'height': LOWER,
        'name': 'HSR Symmetric Upper Stem to Lower Curved Arms',
        'description': 'Two mirrored curved level transitions connect one native two-track upper stem to opposite lower one-way arms. The paired collar stays flat until the two tapered decks separate.',
        # Coordinates are normalized SC4PATH east/north. A shared upper
        # support line continues into reflected lower curve supports;
        # the first separated pair is more than 16 m apart.
        'authored_support_centers': [
            (96., 0.), (96., -16.), (96., -32.),
            (0., -96.), (16., -96.), (32., -96.),
            (160., -96.), (176., -96.), (192., -96.),
            (104.961438816, -59.152402577), (87.038561184, -59.152402577),
            (115.757575795, -75.87085803), (76.242424205, -75.87085803),
            (131.705670536, -87.762381847), (60.294329464, -87.762381847),
        ],
    },
    'hsr_component_lower_oneway_curve90_right': {
        'kind': 'lower_oneway_curve', 'height': LOWER,
        'hand': 'right', 'angle': 90,
        'name': 'One-Way HSR L2 Standard 90 Degree Curve Right',
        'description': 'A centred lower one-way track turns right through 90 degrees with 104 m cardinal displacement, smooth curvature and eight-metre flat collars.',
        'authored_support_centers': [
            (64., 0.), (80., 0.), (96., 0.),
            (0., -64.), (0., -80.), (0., -96.),
            (3.258463782, -48.235071478), (12.964372950, -26.436553182),
            (26.436553182, -12.964372950), (48.235071478, -3.258463782),
        ],
    },
}


def _deck(name, points, width, start, end, **extra):
    return {'name': name, 'points': points, 'width': width,
            'geometry_id': name, 'profile': 'hsr',
            'start_tangent': start, 'end_tangent': end,
            'precise_union': True, 'simplify_collinear': True,
            'extend_endpoints': 'ports', 'clearance_half_width': 2.6,
            'support': False, **extra}


@lru_cache(maxsize=1)
def _quarter():
    count = 384
    headings = [math.pi/2.-math.pi/2.*(10.*(i/count)**3-15.*(i/count)**4+6.*(i/count)**5)
                for i in range(count+1)]
    xy = [(0., 0.)]
    for before, after in zip(headings, headings[1:]):
        x, y = xy[-1]
        xy.append((x+(math.cos(before)+math.cos(after))/2.,
                   y+(math.sin(before)+math.sin(after))/2.))
    scale = 96./xy[-1][0]
    points = [(0., -104.)]
    points.extend((x*scale, y*scale-96.) for x, y in xy)
    points[1], points[-1] = (0., -96.), (96., 0.)
    points.append((104., 0.))
    return tuple(points)


def _height(distance, length, first, last, *, flat_start=8., flat_end=8., edge=16.):
    """The original integrated trapezoidal grade with explicit flat collars."""
    inside = length-flat_start-flat_end
    if inside <= 2.*edge:
        raise ValueError('HSR grade has no constant-slope interior')
    travel = distance-flat_start
    if travel <= 0.:
        fraction = 0.
    elif travel >= inside:
        fraction = 1.
    elif travel < edge:
        fraction = travel*travel/(2.*edge*(inside-edge))
    elif travel > inside-edge:
        fraction = 1.-(inside-travel)**2/(2.*edge*(inside-edge))
    else:
        fraction = (travel-edge/2.)/(inside-edge)
    return first+(last-first)*fraction


def canonical(recipe):
    if recipe == 'hsr_component_lower_oneway_curve90_right':
        points = [(x, north, LOWER) for x, north in _quarter()]
        return {'S>E': points}, [_deck('lower_standard_quarter', points, 8., (0., 1.), (1., 0.))]
    if recipe != 'hsr_component_symmetric_graded_y':
        raise ValueError('Unknown refined HSR component: '+recipe)
    # Two reflected quarters start at the actual +/-2 m native tracks.
    # Their interior horizontal displacement is 94 m; the final flat collar
    # is exactly 8 m, so the lower connection planes remain +/-104 m.
    left_xy = [(-2., 104.)]
    left_xy.extend((-2.-x*94./96., -north) for x, north in _quarter()[1:-1])
    left_xy.append((-104., 0.))
    stations = [0.]
    for before, after in zip(left_xy, left_xy[1:]):
        stations.append(stations[-1]+math.dist(before, after))
    length = stations[-1]
    left = [(x, north, _height(s, length, UPPER, LOWER, flat_start=56.))
            for (x, north), s in zip(left_xy, stations)]
    right = [(-x, north, height) for x, north, height in left]
    taper = {'taper_extra_half_width': 1.5,
             'taper_start_distance': 8., 'taper_end_distance': 56.,
             'graded_taper_upper_collar': True}
    return {'N>W': left, 'E>N': list(reversed(right))}, [
        _deck('graded_y_left', left, 8., (0., -1.), (-1., 0.), **taper),
        _deck('graded_y_right', right, 8., (0., -1.), (1., 0.), **taper),
    ]
