"""One paired L2→L4 quarter-turn; existing reusable pieces stay unchanged.

Coordinates are PATH east, north, and height in metres. The new recipe uses
one native 15 m paired sheet, two opposite routes, and exact flat collars.
The normalized construction origin is deliberately allowed to remain empty.
"""
from functools import lru_cache
import math

RECIPE = 'hsr_component_blind_rise_quarter_turn'
DEFINITIONS = {RECIPE: {
    'kind': 'paired_curved_grade', 'height': 15.5,
    'from_height': 15.5, 'to_height': 30.5, 'hand': 'right', 'angle': 90,
    'name': 'HSR Paired Quarter-Turn Level 2 to Level 4',
    'description': 'A native-width paired right quarter-turn rises from L2 (15.5 m) at its south end to L4 (30.5 m) at its east end. The return track descends. Both ends retain 8 m straight, flat native collars.',
}}

@lru_cache(maxsize=1)
def _states():
    # Integrate a quintic heading law. Its curvature and curvature derivative
    # vanish at both ends, so the body meets the 8 m straight collars smoothly.
    count = 384
    headings = [math.pi/2.*(1.-(10.*(i/count)**3-15.*(i/count)**4+6.*(i/count)**5))
                for i in range(count+1)]
    xy = [(0., 0.)]
    for a, b in zip(headings, headings[1:]):
        x, north = xy[-1]
        xy.append((x+(math.cos(a)+math.cos(b))/2.,
                   north+(math.sin(a)+math.sin(b))/2.))
    scale = 96./xy[-1][0]
    samples = [(0., -104., math.pi/2.)]
    samples += [(x*scale, n*scale-96., heading)
                for (x, n), heading in zip(xy, headings)]
    samples[1], samples[-1] = (0., -96., math.pi/2.), (96., 0., 0.)
    samples.append((104., 0., 0.))
    states, station = [], 0.
    for i, sample in enumerate(samples):
        if i:
            station += math.dist(samples[i-1][:2], sample[:2])
        states.append((*sample, station))
    return tuple(states)


def _height(station, total):
    # Integrate a trapezoidal grade: 8 m flat, 16 m eased grade increase,
    # constant interior grade, 16 m eased decrease, and 8 m flat. The height
    # is monotonic, and its first derivative is continuous everywhere.
    travel, inside, edge = station-8., total-16., 16.
    if travel <= 0.:
        fraction = 0.
    elif travel >= inside:
        fraction = 1.
    elif travel < edge:
        fraction = travel**2/(2.*edge*(inside-edge))
    elif travel > inside-edge:
        fraction = 1.-(inside-travel)**2/(2.*edge*(inside-edge))
    else:
        fraction = (travel-edge/2.)/(inside-edge)
    return 15.5+15.*fraction


def canonical(recipe):
    if recipe != RECIPE:
        raise ValueError('Unknown paired-rise quarter-turn')
    states = _states()
    center, inner, outer = [], [], []
    for east, north, heading, station in states:
        height = _height(station, states[-1][3])
        nx, nn = math.sin(heading), -math.cos(heading)
        center.append((east, north, height))
        inner.append((east+2.*nx, north+2.*nn, height))
        outer.append((east-2.*nx, north-2.*nn, height))
    # Literal cardinal ports eliminate sine/cosine round-off in saved joins.
    inner[0], inner[-1] = (2., -104., 15.5), (104., -2., 30.5)
    outer[0], outer[-1] = (-2., -104., 15.5), (104., 2., 30.5)
    sheet = {'name': 'paired_l2_l4_quarter_turn', 'points': center, 'width': 15.,
             'geometry_id': RECIPE, 'profile': 'hsr',
             'start_tangent': (0., 1.), 'end_tangent': (1., 0.),
             'precise_union': True, 'simplify_collinear': True,
             'extend_endpoints': 'ports', 'clearance_half_width': 2.6,
             'support': False}
    return {'S>E': inner, 'E>S': list(reversed(outer))}, [sheet]
