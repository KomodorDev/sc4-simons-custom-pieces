"""Load self-contained reusable HSR modules and compile their selected cells.

Each registered module owns geometry.json beside its manifest. Local traffic
paths and support metadata are explicit. Complete analytic sweep samples
retain exact shared-boundary miters and height-aware unions; the compiler
emits only this module's cells, never another selectable piece or assembly.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import json
from scp.subject_sources import piece_name_for_recipe, piece_directory

RECIPES = (
    'hsr_component_modular_south_junction',
    'hsr_component_modular_paired_climb',
    'hsr_component_modular_crossing_core',
)


@lru_cache(maxsize=len(RECIPES))
def _source(recipe):
    if recipe not in RECIPES:
        raise ValueError('Unknown reusable HSR module: '+recipe)
    directory = piece_directory(recipe)
    data = json.loads((directory/'geometry.json').read_text())
    if data.get('schema_version') != 1 or data['metadata']['recipe'] != recipe:
        raise ValueError('Reusable HSR module geometry has an invalid identity or schema')
    return data


def partition_info(recipe):
    """Return local module metadata, independent of any other piece recipe."""
    info = deepcopy(_source(recipe)['metadata'])
    info['name'] = piece_name_for_recipe(recipe, info['name'])
    info['construction_flags'] = {tuple(cell): flag for cell, flag in info['construction_flags']}
    for key in ('cells', 'structural_cells', 'support_centers', 'authored_support_centers'):
        info[key] = [tuple(value) for value in info[key]]
    info['footprint'] = tuple(info['footprint'])
    info['origin_shift'] = tuple(info['origin_shift'])
    info['movements'] = [tuple(value) for value in info['movements']]
    for ports in info['ports'].values():
        for direction, point in ports.items():
            ports[direction] = tuple(point)
    info['port_vectors'] = {key: tuple(value) for key, value in info['port_vectors'].items()}
    donor, name, model = info['effect_donor']
    info['effect_donor'] = (tuple(donor), name, model)
    return info


DEFINITIONS = {recipe: partition_info(recipe) for recipe in RECIPES}


def partition_layout(recipe):
    """Return the authored local PATH cells without re-sampling a curve."""
    layout = {tuple(cell): deepcopy(data) for cell, data in _source(recipe)['layout']}
    for data in layout.values():
        for route in data['routes']:
            route['points'] = [tuple(point) for point in route['points']]
    return layout


def partition_routes(recipe):
    """Stitch authored local fragments into directed writer-facing journeys."""
    fragments = {}
    for (column, row), data in partition_layout(recipe).items():
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
        if len(starts) != 1:
            raise ValueError(f'Module movement {recipe}/{movement} has no unique start')
        points = list(starts[0])
        remaining = [part for part in parts if part is not starts[0]]
        while remaining:
            matches = [part for part in remaining if key(part[0]) == key(points[-1])]
            if len(matches) != 1:
                raise ValueError(f'Module movement {recipe}/{movement} is disconnected or ambiguous')
            points.extend(matches[0][1:])
            remaining.remove(matches[0])
        visited = {key(point) for point in points}
        while True:
            matches = [part for part in all_parts if key(part[0]) == key(points[-1])]
            unique = {tuple(key(point) for point in part): part for part in matches}
            if not unique:
                break
            if len(unique) != 1:
                raise ValueError(f'Module movement {recipe}/{movement} has ambiguous shared continuation')
            following = next(iter(unique.values()))
            if key(following[-1]) in visited:
                raise ValueError(f'Module movement {recipe}/{movement} has a shared-route loop')
            points.extend(following[1:])
            visited.update(key(point) for point in following)
        result[movement] = points
    return result


def model_inputs(recipe):
    """Return exact sweep context and the module's local-to-sweep cell map.

    Sweep coordinates are a private numerical frame. Keeping that frame
    prevents floating-point changes in existing curve cuts. It does not
    expose or build a larger piece. Only listed cells and supports compile.
    """
    context = deepcopy(_source(recipe)['surface_context'])
    mapping = {tuple(local): tuple(source) for local, source in context['selected_cells']}
    layout = {source: {'routes': [], 'decks': []} for source in mapping.values()}
    return mapping, {
        'layout': [[list(cell), data] for cell, data in layout.items()],
        'surface_decks': context['surface_decks'],
        'surface_partition_cells': context['partition_cells'],
        'support_centers': context['support_centers'],
        'support_foundation_width': 1.3, 'support_min_spacing': 16.,
    }


def build_models(native_hsr, recipe):
    """Compile only this reusable module's cells from its own surface input."""
    from .hsr_components import _cached_models
    mapping, config = model_inputs(recipe)
    signature = json.dumps(config, sort_keys=True, separators=(',', ':'), allow_nan=False)
    models = dict(_cached_models(native_hsr, signature))
    result = {local: models[source] for local, source in mapping.items()}
    alignment = _source(recipe).get('junction_wedge_alignment')
    if alignment is not None:
        if recipe != 'hsr_component_modular_south_junction':
            raise ValueError('Junction wedge repair belongs only to the symmetric split and return')
        from .hsr_symmetric_parapet import repair_models
        result = repair_models(native_hsr, result, mapping, alignment)
    stem_alignment = _source(recipe).get('stem_parapet_alignment')
    if stem_alignment is not None:
        if recipe != 'hsr_component_modular_south_junction':
            raise ValueError('Stem parapet repair belongs only to the symmetric split and return')
        from .hsr_symmetric_stem import repair_stem_models
        result = repair_stem_models(native_hsr, result, mapping, stem_alignment)
    return result
