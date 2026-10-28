"""Compile the reusable paired fan from its own measured local geometry.

The fan owns literal train paths, complete native-profile sweep samples,
and explicitly placed supports. Its oblique lower cuts continue the reused
mainline diverge and opposing merge; neither lower cut is a native collar.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import json
from pathlib import Path

from scp.dbpf import require

RECIPES = (
    'hsr_component_l2_paired_fan_compact_join',
    'hsr_component_l2_paired_fan_compact_core',
    'hsr_component_l2_paired_straight_recessed_web',
)


@lru_cache(maxsize=3)
def _source(recipe):
    """Read only this module's own maintained geometry source."""
    require(recipe in RECIPES, 'Unknown compact HSR fan recipe')
    path = Path(__file__).resolve().parents[2]/'00_pieces'/recipe.replace('_', '-')/'geometry.json'
    data = json.loads(path.read_text())
    require(data.get('schema_version') == 1 and data['metadata']['recipe'] == recipe,
            'Compact HSR fan source identity or schema is invalid')
    return data


def compact_info(recipe):
    """Return the native construction, connection and support contract."""
    info = deepcopy(_source(recipe)['metadata'])
    info['construction_flags'] = {tuple(cell): flag for cell, flag in info['construction_flags']}
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


DEFINITIONS = {recipe: compact_info(recipe) for recipe in RECIPES}


def compact_layout(recipe):
    """Return literal local train paths without resampling the approved curves."""
    layout = {tuple(cell): deepcopy(data) for cell, data in _source(recipe)['layout']}
    for data in layout.values():
        for route in data['routes']:
            route['points'] = [tuple(point) for point in route['points']]
    return layout


def compact_routes(recipe):
    """Stitch every independent movement through its exact local fragments."""
    fragments = {}
    for (column, row), data in compact_layout(recipe).items():
        for route in data['routes']:
            points = [(x+16.*column, north-16.*row, height)
                      for x, north, height in route['points']]
            fragments.setdefault(route['movement'], []).append(points)

    def key(point):
        return tuple(round(value, 6) for value in point)

    all_parts = [part for parts in fragments.values() for part in parts]
    result = {}
    for movement, parts in fragments.items():
        targets = {key(points[-1]) for points in parts}
        starts = [points for points in parts if key(points[0]) not in targets]
        require(len(starts) == 1, f'Compact movement {recipe}/{movement} has no unique start')
        points = list(starts[0])
        remaining = [part for part in parts if part is not starts[0]]
        while remaining:
            matches = [part for part in remaining if key(part[0]) == key(points[-1])]
            require(len(matches) == 1, f'Compact movement {recipe}/{movement} is disconnected')
            points.extend(matches[0][1:]); remaining.remove(matches[0])
        visited = {key(point) for point in points}
        while True:
            unique = {tuple(key(point) for point in part): part for part in all_parts
                      if key(part[0]) == key(points[-1])}
            if not unique:
                break
            require(len(unique) == 1, f'Compact movement {recipe}/{movement} has an ambiguous continuation')
            following = next(iter(unique.values()))
            require(key(following[-1]) not in visited, 'Compact HSR shared-route loop')
            points.extend(following[1:]); visited.update(key(point) for point in following)
        result[movement] = points
    return result


def model_inputs(recipe):
    """Return selected native sweep cells and the exact independent context."""
    context = deepcopy(_source(recipe)['surface_context'])
    mapping = {tuple(local): tuple(source) for local, source in context['selected_cells']}
    compilation_cells = context.get('compilation_cells', list(mapping.values()))
    if 'compilation_cells' in context:
        extraction_sizes = {'hsr_component_l2_paired_fan_compact_core': 9,
                            'hsr_component_l2_paired_straight_recessed_web': 1}
        require(recipe in extraction_sizes and len(mapping) == extraction_sizes[recipe]
                and len(compilation_cells) == 11
                and len({tuple(cell) for cell in compilation_cells}) == 11
                and set(mapping.values()) <= {tuple(cell) for cell in compilation_cells},
                'Only the extracted fan pieces may retain their full eleven-cell computation context')
    config = {
        'layout': [[list(source), {'routes': [], 'decks': []}] for source in compilation_cells],
        'surface_decks': context['surface_decks'],
        'surface_partition_cells': context['partition_cells'],
        'support_centers': context['support_centers'],
        'support_foundation_width': 1.3,
        'support_min_spacing': 16.,
    }
    rule = _source(recipe).get('central_parapet_alignment')
    if rule is not None:
        config['central_parapet_alignment'] = deepcopy(rule)
    return mapping, config


def build_models(native_hsr, recipe):
    """Compile the fan's own cells and explicitly owned supports."""
    from .hsr_components import _cached_models
    mapping, config = model_inputs(recipe)
    signature = json.dumps(config, sort_keys=True, separators=(',', ':'), allow_nan=False)
    compiler = _cached_fan_models if 'central_parapet_alignment' in config else _cached_models
    models = dict(compiler(native_hsr, signature))
    return {local: models[source] for local, source in mapping.items()}


@lru_cache(maxsize=2)
def _cached_fan_models(native_hsr, signature):
    """Keep the central-border correction exclusive to this owned fan."""
    from .hsr_fan_parapet import corrected_fan_sweeps
    from .hsr_mesh import _compile_models
    from .single_track_models import _native
    config = json.loads(signature)
    layout = {tuple(cell): data for cell, data in config['layout']}
    sweeps = corrected_fan_sweeps(_native(native_hsr), config['surface_decks'],
                                  config['central_parapet_alignment'])

    def sweep(source, deck):
        return sweeps[deck['name']]

    return tuple(_compile_models(native_hsr, layout, config, sweep_function=sweep).items())
