"""Reusable two-level HSR parts, separate from existing interchange recipes.

Coordinates are SC4PATH metres: east, north, rail-path height.  The routes
returned by :func:`component_routes` are complete, directed journeys.  The
physical sheets returned by :func:`physical_decks` are independent of traffic
cell slicing.  In particular, a wide curved slab reserves every cell its
actual swept footprint occupies, including cells without a train path.

These are authored software prototypes.  No geometry or PATH check in this
module establishes SimCity 4 placement or traffic operation.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import math

from scp.dbpf import require
from .interchange_layouts import _add_route, _normalize
from .interchange_models import EFFECT_DONOR
from .rail_features import _construction_flags
from .rail_geometry import _route
from .hsr_reusable_components import EXTRA_DEFINITIONS, canonical_extra
from .hsr_partition_components import (
    RECIPES as PARTITION_RECIPES,
    partition_info, partition_layout, partition_routes,
)
from .hsr_compact_fan import (
    RECIPES as COMPACT_FAN_RECIPES,
    compact_info, compact_layout, compact_routes,
)

from .hsr_atomic_junctions import (
    RECIPES as ATOMIC_JUNCTION_RECIPES,
    atomic_info as junction_info, atomic_layout as junction_layout, atomic_routes as junction_routes,
)
from .hsr_atomic_curves import (
    RECIPES as ATOMIC_CURVE_RECIPES,
    atomic_info as curve_info, atomic_layout as curve_layout, atomic_routes as curve_routes,
)

LOWER = 15.5
UPPER = 30.5
COLLAR = 8.
CURVE_DISPLACEMENT = 96.
_HALF_TRACK_SPACING = 2.

_DEFINITIONS = {
    'hsr_component_upper_paired_straight': {
        'kind': 'upper_paired_straight',
        'name': 'HSR Level 4 (30.5 m) \u2014 Two-Track Straight',
        'description': 'Native-width opposite-direction two-track HSR at 30.5 m; connect only matching upper two-track ports.',
    },
    'hsr_component_upper_paired_to_single_adapter': {
        'kind': 'paired_to_separated_adapter',
        'name': 'HSR Level 4 (30.5 m) \u2014 Two-Track to Separate Single-Track Adapter',
        'description': 'Full native two-track HSR at the south end opens into separate centred one-way tracks one tile apart at the north end; all paths stay at 30.5 m.',
    },
}
for _hand in ('right', 'left'):
    _DEFINITIONS[f'hsr_component_upper_paired_curve90_{_hand}'] = {
        'kind': 'upper_paired_curve', 'hand': _hand, 'angle': 90,
        'name': f'HSR L4 Two-Track 90 Degree Curve {_hand.title()}',
        'description': 'Close opposite-direction tracks on one native-width upper 90 degree slab, with flat cardinal connection collars.',
    }
    for _start, _finish in (('l2', 'l4'), ('l4', 'l2')):
        _DEFINITIONS[f'hsr_component_oneway_curve90_{_hand}_{_start}_to_{_finish}'] = {
            'kind': 'oneway_curved_grade', 'hand': _hand, 'angle': 90,
            'from_height': LOWER if _start == 'l2' else UPPER,
            'to_height': UPPER if _finish == 'l4' else LOWER,
            'name': f'One-Way HSR 90 Degree {_hand.title()} {_start.upper()} to {_finish.upper()} Ramp',
            'description': 'One centred track turns 90 degrees while changing height, with flat matching-level cardinal ends.',
        }
_DEFINITIONS.update(EXTRA_DEFINITIONS)
RECIPES = tuple(_DEFINITIONS) + PARTITION_RECIPES + COMPACT_FAN_RECIPES + ATOMIC_JUNCTION_RECIPES + ATOMIC_CURVE_RECIPES


def _height(distance, length, first, last, edge=16.):
    """Integrated trapezoidal grade, including exact flat connection collars.

    The interior grade rises linearly from zero, stays constant, and falls
    linearly to zero.  Both height and grade are continuous at every join.
    The endpoint collars themselves are exactly flat, rather than almost
    flat samples of an easing function.
    """
    distance -= COLLAR
    length -= 2.*COLLAR
    require(length > 2.*edge, 'HSR component grade has no eased interior')
    if distance <= 0.:
        fraction = 0.
    elif distance >= length:
        fraction = 1.
    elif distance < edge:
        fraction = distance*distance/(2.*edge*(length-edge))
    elif distance > length-edge:
        fraction = 1.-(length-distance)**2/(2.*edge*(length-edge))
    else:
        fraction = (distance-edge/2.)/(length-edge)
    return first+(last-first)*fraction


@lru_cache(maxsize=1)
def _quarter_states():
    """North-to-east centreline with smooth zero-curvature ends.

    Each state is east, north, analytic heading, travelled distance.  A
    quintic heading transition makes curvature and its first derivative
    vanish where the curve meets each 8 m straight collar.  Equal integration
    weights make the two displacement components exactly equal.
    """
    count = 384
    headings = []
    for index in range(count+1):
        t = index/count
        headings.append(math.pi/2.-math.pi/2.*(10.*t**3-15.*t**4+6.*t**5))
    xy = [(0., 0.)]
    for first, last in zip(headings, headings[1:]):
        x, y = xy[-1]
        xy.append((x+(math.cos(first)+math.cos(last))/2.,
                   y+(math.sin(first)+math.sin(last))/2.))
    scale = CURVE_DISPLACEMENT/xy[-1][0]
    require(abs(xy[-1][0]-xy[-1][1]) < 1e-9,
            'HSR component curve lost symmetric cardinal displacement')
    span = CURVE_DISPLACEMENT+COLLAR
    states = [(0., -span, math.pi/2., 0.)]
    states.extend((x*scale, y*scale-CURVE_DISPLACEMENT, angle, COLLAR+index*scale)
                  for index, ((x, y), angle) in enumerate(zip(xy, headings)))
    states[1] = (0., -CURVE_DISPLACEMENT, math.pi/2., COLLAR)
    states[-1] = (CURVE_DISPLACEMENT, 0., 0., COLLAR+count*scale)
    states.append((span, 0., 0., 2.*COLLAR+count*scale))
    return tuple(states)


def _deck(name, points, width, start, end):
    return {'name': name, 'points': points, 'width': width,
            'geometry_id': 'hsr_component_'+name, 'profile': 'hsr',
            'start_tangent': start, 'end_tangent': end,
            'precise_union': True, 'simplify_collinear': True,
            'extend_endpoints': 'ports', 'clearance_half_width': 2.6,
            'support': False}


def _canonical(recipe):
    if recipe in EXTRA_DEFINITIONS:
        return canonical_extra(recipe)
    definition = _DEFINITIONS[recipe]
    kind = definition['kind']
    if kind == 'upper_paired_straight':
        routes = {'S>N': [(2., -8., UPPER), (2., 8., UPPER)],
                  'N>S': [(-2., 8., UPPER), (-2., -8., UPPER)]}
        decks = [_deck('upper_straight', [(0., -8., UPPER), (0., 8., UPPER)],
                       15., (0., 1.), (0., 1.))]
    elif kind == 'paired_to_separated_adapter':
        # Both physical sheets are ordered south-to-north.  The western
        # train route runs in the reverse direction.  The exact paired end
        # must span15m even though each independent filler is only8m wide.
        # Each sheet therefore starts11m wide and tapers smoothly to8m.
        distances = [0., COLLAR, *(COLLAR+.5*i for i in range(1, 225)), 128.]
        left, right = [], []
        for distance in distances:
            t = min(1., max(0., (distance-COLLAR)/(128.-2.*COLLAR)))
            ease = 10.*t**3-15.*t**4+6.*t**5
            left.append((-2.+2.*ease, -120.+distance, UPPER))
            right.append((2.+14.*ease, -120.+distance, UPPER))
        routes = {'S>N': right, 'N>S': list(reversed(left))}
        decks = []
        for name, points in (('adapter_west', left), ('adapter_east', right)):
            length = sum(math.dist(a[:2], b[:2]) for a, b in zip(points, points[1:]))
            decks.append({**_deck(name, points, 8., (0., 1.), (0., 1.)),
                          'taper_extra_half_width': 1.5,
                          'taper_start_distance': COLLAR,
                          'taper_end_distance': length-COLLAR})
    else:
        left = definition['hand'] == 'left'
        states = _quarter_states()
        total = states[-1][3]
        center, forward, backward = [], [], []
        for x, y, angle, distance in states:
            if left:
                x, angle = -x, math.pi-angle
            z = (UPPER if kind == 'upper_paired_curve' else
                 _height(distance, total, definition['from_height'], definition['to_height']))
            center.append((x, y, z))
            right = math.sin(angle), -math.cos(angle)
            forward.append((x+_HALF_TRACK_SPACING*right[0],
                            y+_HALF_TRACK_SPACING*right[1], z))
            backward.append((x-_HALF_TRACK_SPACING*right[0],
                             y-_HALF_TRACK_SPACING*right[1], z))
        target = 'W' if left else 'E'
        routes = ({'S>'+target: forward, target+'>S': list(reversed(backward))}
                  if kind == 'upper_paired_curve' else {'S>'+target: center})
        # Avoid near-zero sine/cosine noise at literal cardinal connection
        # planes. Interior samples retain the analytic offset normals.
        span = CURVE_DISPLACEMENT+COLLAR
        if kind == 'upper_paired_curve':
            first, second = routes['S>'+target], routes[target+'>S']
            first[0] = (2., -span, UPPER)
            second[-1] = (-2., -span, UPPER)
            first[-1] = (-span if left else span, 2. if left else -2., UPPER)
            second[0] = (-span if left else span, -2. if left else 2., UPPER)
        decks = [_deck('paired_curve_'+definition['hand'] if kind == 'upper_paired_curve'
                       else 'curved_ramp_'+definition['hand'], center,
                       15. if kind == 'upper_paired_curve' else 8.,
                       (0., 1.), (-1., 0.) if left else (1., 0.))]
    return routes, decks


def _clip_polygon(polygon, axis, bound, sign):
    """Clip against one exact rectangle half-plane; no occupancy sampling."""
    result = []
    for first, last in zip(polygon, polygon[1:]+polygon[:1]):
        before, after = sign*(first[axis]-bound), sign*(last[axis]-bound)
        first_inside, last_inside = before >= 0., after >= 0.
        if first_inside:
            result.append(first)
        if first_inside != last_inside:
            fraction = before/(before-after)
            require(0. <= fraction <= 1., 'HSR component cell clip escaped its segment')
            result.append(tuple(a+fraction*(b-a) for a, b in zip(first, last)))
    return result


def _area(polygon):
    return abs(sum(a[0]*b[1]-b[0]*a[1]
                   for a, b in zip(polygon, polygon[1:]+polygon[:1])))/2.


def deck_half_widths(deck):
    """Actual transverse slab half-width at every authored centre sample.

    Only the new paired-to-separated adapter supplies taper metadata.  Its
    rails stay centred on each individual sheet while the shoulder and outer
    wall move1.5m inward.  The writer must use these same widths for its
    explicit tapered native profile; a constant-width sweep is insufficient.
    """
    extra = float(deck.get('taper_extra_half_width', 0.))
    half = float(deck['width'])/2.
    if not extra:
        return [half]*len(deck['points'])
    start = float(deck['taper_start_distance'])
    end = float(deck['taper_end_distance'])
    require(0. <= start < end, 'HSR component tapered slab has invalid distance bounds')
    result, distance = [], 0.
    for index, point in enumerate(deck['points']):
        if index:
            distance += math.dist(deck['points'][index-1][:2], point[:2])
        t = min(1., max(0., (distance-start)/(end-start)))
        ease = 10.*t**3-15.*t**4+6.*t**5
        result.append(half+extra*(1.-ease))
    return result


def _physical_cells(decks):
    """Exact cell intersection of the same mitered sheets the writer sweeps."""
    cells = set()
    for deck in decks:
        points, _, miters = _route(deck['points'], deck['start_tangent'], deck['end_tangent'])
        halves = deck_half_widths(deck)
        require(len(points) == len(halves), 'HSR component tapered sheet lost a centre sample')
        for index, (first, last) in enumerate(zip(points, points[1:])):
            before, after = miters[index:index+2]
            polygon = [(point[0]+cross*normal[0], point[2]+cross*normal[1])
                       for point, normal, cross in ((first, before, -halves[index]),
                                                    (first, before, halves[index]),
                                                    (last, after, halves[index+1]),
                                                    (last, after, -halves[index+1]))]
            xmin, xmax = min(p[0] for p in polygon), max(p[0] for p in polygon)
            zmin, zmax = min(p[1] for p in polygon), max(p[1] for p in polygon)
            for column in range(math.floor((xmin+8.)/16.), math.floor((xmax+8.)/16.)+1):
                for row in range(math.floor((zmin+8.)/16.), math.floor((zmax+8.)/16.)+1):
                    clipped = polygon
                    for axis, bound, sign in ((0, 16.*column-8., 1.), (0, 16.*column+8., -1.),
                                              (1, 16.*row-8., 1.), (1, 16.*row+8., -1.)):
                        if not clipped:
                            break
                        clipped = _clip_polygon(clipped, axis, bound, sign)
                    if len(clipped) >= 3 and _area(clipped) > 1e-9:
                        cells.add((column, row))
    return cells


@lru_cache(maxsize=len(RECIPES))
def _normalized(recipe):
    require(recipe in _DEFINITIONS, f'Unknown HSR component recipe: {recipe}')
    routes, decks = _canonical(recipe)
    layout = {}
    for movement, points in routes.items():
        # Only the new parallel turnout components contain a choice between
        # the through line and a branch. The branch needs the explicit PATH
        # junction flag when both encoded fragments share a start point.
        definition = _DEFINITIONS[recipe]
        branch = ((definition['kind'].startswith('zero_turn_')
                   and movement not in ('S>N', 'N>S'))
                  or movement in definition.get('branch_movements', ()))
        _add_route(layout, points, movement,
                   role='branch' if branch else 'main', deck=False)
    for cell in _physical_cells(decks):
        layout.setdefault(cell, {'routes': [], 'decks': []})
    _, shift = _normalize(deepcopy(layout))
    # Local route fragments are unchanged by moving their cell indices;
    # complete routes and sheets must receive the corresponding world shift.
    routes = {movement: [(x+shift[0], y+shift[1], z) for x, y, z in points]
              for movement, points in routes.items()}
    decks = [{**deck, 'points': [(x+shift[0], y+shift[1], z) for x, y, z in deck['points']]}
             for deck in decks]
    layout, _ = _normalize(layout)
    anchor = min(layout, key=lambda cell: (cell[1], cell[0]))
    for deck in decks:
        local = deepcopy(deck)
        local['points'] = [(x-16.*anchor[0], y+16.*anchor[1], z) for x, y, z in deck['points']]
        layout[anchor]['decks'].append(local)
    return routes, decks, layout, shift


def component_routes(recipe):
    """Return fresh complete directed paths in normalized city coordinates."""
    if recipe in ATOMIC_JUNCTION_RECIPES:
        return junction_routes(recipe)
    if recipe in ATOMIC_CURVE_RECIPES:
        return curve_routes(recipe)
    if recipe in COMPACT_FAN_RECIPES:
        return compact_routes(recipe)
    if recipe in PARTITION_RECIPES:
        return partition_routes(recipe)
    return deepcopy(_normalized(recipe)[0])


def physical_decks(recipe):
    """Return fresh complete native-width physical sheets in world coordinates."""
    if recipe in ATOMIC_JUNCTION_RECIPES or recipe in ATOMIC_CURVE_RECIPES:
        return []
    if recipe in COMPACT_FAN_RECIPES:
        return []
    if recipe in PARTITION_RECIPES:
        # These modules own explicit surface context and selected cells.
        # Re-sweeping a clipped sheet changes walls and tangents at its cut.
        return []
    return deepcopy(_normalized(recipe)[1])


def component_layout(recipe):
    """Return fresh sparse cells with local PATH fragments and physical sheets."""
    if recipe in ATOMIC_JUNCTION_RECIPES:
        return junction_layout(recipe)
    if recipe in ATOMIC_CURVE_RECIPES:
        return curve_layout(recipe)
    if recipe in COMPACT_FAN_RECIPES:
        return compact_layout(recipe)
    if recipe in PARTITION_RECIPES:
        return partition_layout(recipe)
    return deepcopy(_normalized(recipe)[2])


INFO = {}
for _recipe, _definition in _DEFINITIONS.items():
    _routes, _decks, _layout, _shift = _normalized(_recipe)
    _cells = list(_layout)
    _ports = {}
    for _movement, _points in _routes.items():
        _source, _target = _movement.split('>')
        _ports.setdefault(_source, {})['in'] = _points[0]
        _ports.setdefault(_target, {})['out'] = _points[-1]
    INFO[_recipe] = {
        **deepcopy(_definition), 'recipe': _recipe, 'category': 'hsr-components',
        'height': _definition.get('height', LOWER if _definition['kind'] == 'oneway_curved_grade' else UPPER),
        'upper_height': UPPER, 'footprint': (max(x for x, _ in _cells)+1, max(y for _, y in _cells)+1),
        'cells': _cells, 'cost': 100*len(_cells), 'origin_shift': _shift,
        'ports': _ports, 'movements': [tuple(movement.split('>')) for movement in _routes],
        'construction_flags': {cell: _construction_flags(data['routes']) if data['routes'] else 0
                               for cell, data in _layout.items()},
        'structural_cells': [cell for cell, data in _layout.items() if not data['routes']],
        'effect_donor': EFFECT_DONOR, 'effect_tag': 'hsrcomp',
        'support_foundation_width': 1.3, 'support_min_spacing': 16.,
        'clearance_width': 5., 'clearance_height': 5.,
        'maximum_grade': .25, 'minimum_radius_m': 24., 'at_grade_conflicts': False,
        'orientation_policy': 'rotate-only-preserve-direction',
        'provenance': 'New reusable HSR native-profile sheets and directed SC4PATH; software prototype; game tests unverified',
    }

for _recipe in PARTITION_RECIPES:
    INFO[_recipe] = partition_info(_recipe)

for _recipe in COMPACT_FAN_RECIPES:
    INFO[_recipe] = compact_info(_recipe)

for _recipe in ATOMIC_JUNCTION_RECIPES:
    INFO[_recipe] = junction_info(_recipe)

for _recipe in ATOMIC_CURVE_RECIPES:
    INFO[_recipe] = curve_info(_recipe)
