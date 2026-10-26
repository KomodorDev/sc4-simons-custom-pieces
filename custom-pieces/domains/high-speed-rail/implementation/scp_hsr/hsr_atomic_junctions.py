"""Load and compile shortened native HSR junction cores from owned sources.

Purpose: remove two eligible sub-five-millimetre approach tails without
changing the existing types. Each new core owns its literal PATH fragments,
bounded symmetric collar correction, complete sweep context and supports.
Only selected cells compile; the extracted tile uses the existing paired
straight. Saved-resource checks remain independent of this writer.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import json
from pathlib import Path

from scp.dbpf import require

RECIPES = (
    'hsr_component_l2_short_mainline_diverge_core',
    'hsr_component_l2_short_opposed_merge_core',
)


@lru_cache(maxsize=2)
def _source(recipe):
    require(recipe in RECIPES, 'Unknown shortened HSR junction recipe')
    path = Path(__file__).resolve().parents[2]/'00_pieces'/recipe.replace('_', '-')/'geometry.json'
    data = json.loads(path.read_text())
    require(data.get('schema_version') == 1 and data['metadata']['recipe'] == recipe,
            'Shortened HSR junction source identity or schema is invalid')
    return data


def atomic_info(recipe):
    """Return literal ports, construction cells and the retained support plan."""
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


DEFINITIONS = {recipe: atomic_info(recipe) for recipe in RECIPES}


def atomic_layout(recipe):
    """Return exact authored local route fragments without re-sampling them."""
    layout = {tuple(cell): deepcopy(data) for cell, data in _source(recipe)['layout']}
    for data in layout.values():
        for route in data['routes']:
            route['points'] = [tuple(point) for point in route['points']]
    return layout


def atomic_routes(recipe):
    """Join literal fragments and their shared mainline continuations."""
    fragments = {}
    for (column, row), data in atomic_layout(recipe).items():
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
        require(len(starts) == 1, f'Short junction {recipe}/{movement} has no unique start')
        points = list(starts[0])
        remaining = [part for part in parts if part is not starts[0]]
        while remaining:
            matches = [part for part in remaining if key(part[0]) == key(points[-1])]
            require(len(matches) == 1, f'Short junction {recipe}/{movement} is disconnected')
            points.extend(matches[0][1:]); remaining.remove(matches[0])
        visited = {key(point) for point in points}
        while True:
            unique = {tuple(key(point) for point in part): part for part in all_parts
                      if key(part[0]) == key(points[-1])}
            if not unique:
                break
            require(len(unique) == 1, f'Short junction {recipe}/{movement} has ambiguous continuation')
            following = next(iter(unique.values()))
            require(key(following[-1]) not in visited, 'Short junction shared-route loop')
            points.extend(following[1:]); visited.update(key(point) for point in following)
        result[movement] = points
    return result


def model_inputs(recipe):
    """Keep the original sweep frame and compile only this core's cells."""
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
    """Compile real native-profile models, without any preview-only repair."""
    from .hsr_components import _cached_models
    result = {}
    for mapping, config in compilation_parts(recipe):
        signature = json.dumps(config, sort_keys=True, separators=(',', ':'), allow_nan=False)
        models = dict(_cached_models(native_hsr, signature))
        for local, source in mapping.items():
            require(local not in result, 'Two analytic contexts own one junction tile')
            result[local] = models[source]
    require(set(result) == set(atomic_info(recipe)['cells']),
            'Analytic junction contexts leave an unowned tile')
    return result


def compilation_parts(recipe):
    """Keep the edited collar and literal retained surfaces independently owned.

    A bounded endpoint correction can alter a remote union's triangulation
    even where the actual curve is unchanged. Compile those retained cells
    from this type's own unchanged analytic context, rather than silently
    expanding the permitted change region or importing a previous build.
    """
    data = _source(recipe)
    revised = set(map(tuple, data['revised_surface_cells']))
    require(len(revised) == 1, 'Short junction must revise exactly one collar tile')
    parts = []
    for key, changed in (('surface_context', True), ('retained_surface_context', False)):
        context = deepcopy(data[key])
        mapping = {tuple(local): tuple(source) for local, source in context['selected_cells']
                   if (tuple(local) in revised) == changed}
        require(mapping, 'Short junction analytic context emits no tiles')
        cells = set(mapping.values())
        centres = [(x, north) for x, north in context['support_centers']
                   if (round(x/16.), round(-north/16.)) in cells]
        require(len(centres) == len(mapping), 'Short junction support ownership differs')
        parts.append((mapping, {
            'layout': [[list(source), {'routes': [], 'decks': []}] for source in mapping.values()],
            'surface_decks': context['surface_decks'],
            'surface_partition_cells': context['partition_cells'],
            'support_centers': centres,
            'support_foundation_width': 1.3,
            'support_min_spacing': 16.,
        }))
    return parts
