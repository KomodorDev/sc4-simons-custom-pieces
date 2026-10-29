"""New compact paired HSR corners for a continuously graded northern loop.

Existing component geometry is deliberately untouched. Each new corner has
56 m cardinal displacement, native 15 m slab, two directed tracks at +/-2 m,
and exact 8 m flat collars. The intermediate 23 m connection is custom: only
components carrying that same physical height may connect there.
"""
from __future__ import annotations

from functools import lru_cache
import math

SPAN_M = 56.
COLLAR_M = 8.
BODY_M = 48.
MID_HEIGHT_M = 23.

DEFINITIONS = {
    'hsr_component_tight_paired_curve90_l4_to_mid': {
        'kind': 'tight_paired_curved_grade', 'height': 30.5,
        'from_height': 30.5, 'to_height': MID_HEIGHT_M,
        'hand': 'right', 'angle': 90,
        'name': 'HSR Custom (23 m) \u2194 Level 4 (30.5 m) \u2014 Two-Track Curve 90\u00b0 Ramp \u2014 Tight',
        'description': 'A 56 m right-angle paired corner descends from 30.5 m to the custom 23 m matching connection. The reverse-direction track climbs; both ends have 8 m flat native collars.',
    },
    'hsr_component_tight_paired_curve90_mid_to_l2': {
        'kind': 'tight_paired_curved_grade', 'height': MID_HEIGHT_M,
        'from_height': MID_HEIGHT_M, 'to_height': 15.5,
        'hand': 'right', 'angle': 90,
        'name': 'HSR Level 2 (15.5 m) \u2194 Custom (23 m) \u2014 Two-Track Curve 90\u00b0 Ramp \u2014 Tight',
        'description': 'A 56 m right-angle paired corner descends from the custom 23 m connection to lower 15.5 m HSR. The reverse-direction track climbs; both ends have 8 m flat native collars.',
    },
}


def _progress(t):
    # This new polynomial keeps heading, curvature and its first derivative
    # continuous at the two straight collars. The reviewed extra term
    # spreads the peak curvature change enough for the smaller inner track;
    # the original 24 components retain their original polynomials.
    return (10.*t**3-15.*t**4+6.*t**5
            -4.5*t**3*(1.-t)**3*(2.*t-1.))


@lru_cache(maxsize=1)
def quarter_states():
    count = 512
    headings = [math.pi/2.*(1.-_progress(i/count)) for i in range(count+1)]
    xy = [(0., 0.)]
    for before, after in zip(headings, headings[1:]):
        x, north = xy[-1]
        xy.append((x+(math.cos(before)+math.cos(after))/2.,
                   north+(math.sin(before)+math.sin(after))/2.))
    scale = BODY_M/xy[-1][0]
    if abs(xy[-1][0]-xy[-1][1]) > 1e-9:
        raise ValueError('Tight paired HSR corner lost its diagonal symmetry')
    samples = [(0., -SPAN_M, math.pi/2.)]
    samples.extend((x*scale, north*scale-BODY_M, heading)
                   for (x, north), heading in zip(xy, headings))
    samples[1] = (0., -BODY_M, math.pi/2.)
    samples[-1] = (BODY_M, 0., 0.)
    samples.append((SPAN_M, 0., 0.))
    states, station = [], 0.
    for index, (x, north, heading) in enumerate(samples):
        if index:
            station += math.dist(samples[index-1][:2], (x, north))
        states.append((x, north, heading, station))
    return tuple(states)


def _height(station, total, first, last):
    inside, travel, edge = total-2.*COLLAR_M, station-COLLAR_M, 16.
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
    definition = DEFINITIONS[recipe]
    states = quarter_states()
    total = states[-1][3]
    first, last = definition['from_height'], definition['to_height']
    center, inner, outer = [], [], []
    for x, north, heading, station in states:
        height = _height(station, total, first, last)
        center.append((x, north, height))
        nx, nnorth = math.sin(heading), -math.cos(heading)
        inner.append((x+2.*nx, north+2.*nnorth, height))
        outer.append((x-2.*nx, north-2.*nnorth, height))
    inner[0], inner[-1] = (2., -SPAN_M, first), (SPAN_M, -2., last)
    outer[0], outer[-1] = (-2., -SPAN_M, first), (SPAN_M, 2., last)
    sheet = {
        'name': recipe, 'points': center, 'width': 15.,
        'geometry_id': recipe, 'profile': 'hsr',
        'start_tangent': (0., 1.), 'end_tangent': (1., 0.),
        'precise_union': True, 'simplify_collinear': True,
        'extend_endpoints': 'ports', 'clearance_half_width': 2.6,
        'support': False,
    }
    return {'S>E': inner, 'E>S': list(reversed(outer))}, [sheet]
