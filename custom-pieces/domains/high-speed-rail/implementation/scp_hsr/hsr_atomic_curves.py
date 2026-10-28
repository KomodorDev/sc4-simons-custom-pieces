"""Compile independently owned twelve-tile HSR curves with a native straight end.

Literal local PATH samples, the bounded mirrored tail correction, complete
physical sweep context and retained supports live in each new geometry.json.
Existing curve types and their immutable resources are never rewritten here.
The selected twelve cells exclude the separate ordinary eight-metre straight.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import json
from scp.subject_identity import canonical_piece_name, piece_directory

from scp.dbpf import require

RECIPES = (
    'hsr_component_l2_shortened_departure_curve',
    'hsr_component_l2_shortened_return_curve',
)


@lru_cache(maxsize=2)
def _source(recipe):
    require(recipe in RECIPES, 'Unknown shortened HSR curve recipe')
    path = piece_directory(recipe)/'geometry.json'
    data = json.loads(path.read_text())
    require(data.get('schema_version') == 1 and data['metadata']['recipe'] == recipe,
            'Shortened HSR curve source identity or schema is invalid')
    return data


def atomic_info(recipe):
    """Return a fresh local connection, construction and support definition."""
    info = deepcopy(_source(recipe)['metadata'])
    info['name'] = canonical_piece_name(recipe, info['name'])
    info['construction_flags'] = {tuple(cell): value for cell, value in info['construction_flags']}
    for key in ('cells', 'structural_cells', 'support_centers', 'authored_support_centers'):
        info[key] = [tuple(value) for value in info[key]]
    for key in ('footprint', 'origin_shift'):
        info[key] = tuple(info[key])
    info['movements'] = [tuple(value) for value in info['movements']]
    for ports in info['ports'].values():
        for direction, point in ports.items():
            ports[direction] = tuple(point)
    info['port_vectors'] = {key: tuple(value) for key, value in info['port_vectors'].items()}
    donor, name, model = info['effect_donor']
    info['effect_donor'] = (tuple(donor), name, model)
    return info


DEFINITIONS = {recipe: atomic_info(recipe) for recipe in RECIPES}


def atomic_layout(recipe):
    """Return literal local route fragments without re-sampling the old curve."""
    layout = {tuple(cell): deepcopy(data) for cell, data in _source(recipe)['layout']}
    for data in layout.values():
        for route in data['routes']:
            route['points'] = [tuple(point) for point in route['points']]
    return layout


def atomic_routes(recipe):
    """Stitch the single directional curve through its actual local cells."""
    fragments = []
    for (column, row), data in atomic_layout(recipe).items():
        for route in data['routes']:
            fragments.append([(x+16.*column, north-16.*row, height)
                              for x, north, height in route['points']])
    key = lambda point: tuple(round(value, 6) for value in point)
    targets = {key(points[-1]) for points in fragments}
    starts = [points for points in fragments if key(points[0]) not in targets]
    require(len(starts) == 1, 'Shortened HSR curve lacks a unique directional start')
    points = list(starts[0])
    remaining = [part for part in fragments if part is not starts[0]]
    while remaining:
        following = [part for part in remaining if key(part[0]) == key(points[-1])]
        require(len(following) == 1, 'Shortened HSR curve contains a disconnected or ambiguous route')
        points.extend(following[0][1:]); remaining.remove(following[0])
    source, target = atomic_info(recipe)['movements'][0]
    return {source+'>'+target: points}


def model_inputs(recipe):
    """Retain the original sweep frame while emitting only the twelve owned cells."""
    context = deepcopy(_source(recipe)['surface_context'])
    mapping = {tuple(local): tuple(source) for local, source in context['selected_cells']}
    return mapping, {
        'layout': [[list(source), {'routes': [], 'decks': []}] for source in mapping.values()],
        'surface_decks': context['surface_decks'],
        'surface_partition_cells': context['partition_cells'],
        'support_centers': context['support_centers'],
        'support_foundation_width': 1.3,
        'support_min_spacing': 16.,
    }


def build_models(native_hsr, recipe):
    """Compile only this curve's cells using the established native-profile sweep."""
    from .hsr_components import _cached_models
    mapping, config = model_inputs(recipe)
    signature = json.dumps(config, sort_keys=True, separators=(',', ':'), allow_nan=False)
    models = dict(_cached_models(native_hsr, signature))
    return {local: models[source] for local, source in mapping.items()}
