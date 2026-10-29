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
import hashlib
import json
from scp.subject_sources import piece_name_for_recipe, piece_directory
import struct

from scp.dbpf import require

RECIPES = (
    'hsr_component_l2_short_mainline_diverge_core',
    'hsr_component_l2_short_opposed_merge_core',
)


@lru_cache(maxsize=2)
def _source(recipe):
    require(recipe in RECIPES, 'Unknown shortened HSR junction recipe')
    path = piece_directory(recipe)/'geometry.json'
    data = json.loads(path.read_text())
    require(data.get('schema_version') == 1 and data['metadata']['recipe'] == recipe,
            'Shortened HSR junction source identity or schema is invalid')
    return data


def atomic_info(recipe):
    """Return literal ports, construction cells and the retained support plan."""
    info = deepcopy(_source(recipe)['metadata'])
    info['name'] = piece_name_for_recipe(recipe, info['name'])
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
    result = {}
    for mapping, config in compilation_parts(recipe):
        signature = json.dumps(config, sort_keys=True, separators=(',', ':'), allow_nan=False)
        models = dict(_cached_junction_models(native_hsr, signature))
        for local, source in mapping.items():
            require(local not in result, 'Two analytic contexts own one junction tile')
            result[local] = models[source]
    require(set(result) == set(atomic_info(recipe)['cells']),
            'Analytic junction contexts leave an unowned tile')
    collar = _source(recipe).get('west_straight_extraction', {}).get('native_west_parapet_collar')
    if collar is not None:
        alignment = _source(recipe).get('opposed_parapet_alignment')
        if alignment is not None and 'raw_west_cell_sha256' in alignment:
            collar = deepcopy(collar)
            collar['baseline_cell_model_sha256'] = alignment['raw_west_cell_sha256']
            collar['preserve_native_upper_concrete'] = True
        cell = tuple(collar['cell'])
        require(cell in result, 'West parapet collar has no retained owner')
        result[cell] = normalize_west_parapet(result[cell], native_hsr, collar)
    return result


@lru_cache(maxsize=4)
def _cached_junction_models(native_hsr, signature):
    from .hsr_mesh import _compile_models
    config = json.loads(signature)
    layout = {tuple(cell): data for cell, data in config['layout']}
    return tuple(_compile_models(native_hsr, layout, config,
                                sweep_function=_sweep_junction_profile).items())


def _sweep_junction_profile(source, deck):
    """Continue both concrete borders along the branch into their old wings.

    Exact mitered inner-wall footprints cut the mainline top, and the matching
    inside faces close that curved cut. The original outside face and wing,
    rail floors, undersides, supports, and original curved wings are retained.
    """
    from .hsr_components import _sweep_component_profile
    from .single_track_models import _clip, _triangulate
    surfaces, corridors, points, lengths = _sweep_component_profile(source, deck)
    if deck.get('opposed_parapet_alignment') is not None:
        from .hsr_opposed_parapet import sweep_opposed_parapet
        return sweep_opposed_parapet(source, deck, (surfaces, corridors, points, lengths))
    alignment = deck.get('south_parapet_alignment')
    if alignment is None:
        return surfaces, corridors, points, lengths
    offset = alignment['source_east_offset_m']
    right = offset+alignment['right_inner_join_local_east_m']
    require(alignment['right_join'] == 'continuous_branch_inside_outline'
            and alignment['right_inner_half_width_m'] == 2.6,
            'Right parapet requires its measured branch inside outline')
    split = offset+alignment['left_selection_limit_local_east_m']
    if deck['name'] == alignment['left_branch']:
        from .rail_geometry import _route, _convex_parts
        route, _, miters = _route(deck['points'], deck.get('start_tangent'), deck.get('end_tangent'))
        half = alignment['left_inner_half_width_m']
        polygons = []
        for a, b, na, nb in zip(route, route[1:], miters, miters[1:]):
            polygons.extend(_convex_parts([
                (p[0]+cross*n[0], p[2]+cross*n[1])
                for p, n, cross in ((a, na, -half), (a, na, half),
                                    (b, nb, half), (b, nb, -half))]))
        require(corridors and half == 2.6 and deck['width'] == 8.
                and all(abs(point[1]-15.5) < 1e-8 for point in points),
                'Following parapet requires its flat native single branch')
        corridors[0]['parapet_opening_polygons'] = polygons
        changed = list(surfaces)
        for kind, triangle in surfaces:
            if kind != 'inner_wall':
                continue
            for region in (lambda v: split-v[0], lambda v: v[0]-split):
                polygon = list(triangle)
                for plane in (lambda v: v[2]-source['inner'],
                              # Retain the exact old nominal mainline mask.
                              lambda v: 7.5-v[2], region):
                    polygon = _clip(polygon, plane)
                # Both native branch inside faces now close their matching
                # raised mainline-to-wing continuations. Existing wing faces
                # beyond the old mainline mask retain their original bytes.
                changed.extend(('aligned_inner_wall', part) for part in _triangulate(polygon))
        return changed, corridors, points, lengths
    require(deck['name'] == 'native_east_west_main' and deck['width'] == 15.
            and len(points) == 2 and points[0][0] < split < right < points[-1][0]
            and all(abs(point[1]-15.5) < 1e-8 and abs(point[2]) < 1e-8 for point in points),
            'South parapet alignment requires its flat native mainline')
    changed = []
    for kind, triangle in surfaces:
        if (kind != 'wall' or min(v[2] for v in triangle) < source['inner']-1e-5
                or max(v[1] for v in triangle) <= source['bed_y']+1e-5):
            changed.append((kind, triangle))
            continue
        # Keep structural side faces below the ballast plane untouched.
        if min(v[1] for v in triangle) < source['bed_y']-1e-5:
            lower = _clip(list(triangle), lambda v: source['bed_y']-v[1])
            changed.extend((kind, part) for part in _triangulate(lower))
        upper = _clip(list(triangle), lambda v: v[1]-source['bed_y'])
        left_polygon = _clip(upper, lambda v: split-v[0])
        # The outside wall ends where the original curved outside face takes
        # over. Only the top and inside face follow the inner ballast line.
        left_kind = (kind if all(abs(v[2]-source['outer']) < 1e-5 for v in triangle)
                     else 'following_parapet')
        changed.extend((left_kind, part) for part in _triangulate(left_polygon))
        right_polygon = _clip(upper, lambda v: v[0]-split)
        # Continue the right top to the same inside outline as its wing.
        # Its outer side remains clipped by the original full branch deck;
        # no internal wall or obsolete perpendicular cap closes the join.
        right_kind = (kind if all(abs(v[2]-source['outer']) < 1e-5 for v in triangle)
                      else 'following_parapet')
        changed.extend((right_kind, part) for part in _triangulate(right_polygon))
    return changed, corridors, points, lengths


def normalize_west_parapet(raw_model, native_hsr, collar):
    """Join the reviewed northern parapet to a native straight in a2.5m collar.

    This explicit source rule acts only on the hash-pinned retained west cell.
    Every face is split at the continuous warp's affine region boundaries,
    so existing collinear edges and T junctions remain aligned. Exact clipping
    and retained tiny triangle fans avoid opening gaps at those boundaries.
    The original vertex UV attributes are retained, and new cut attributes
    are interpolated; the UV field inside the deformed collar can change.
    """
    from scp.models import parse_s3d, pack_s3d
    from scp.render_meshes import _triangles
    from .single_track_models import _native, _pack
    require(hashlib.sha256(raw_model).hexdigest() == collar['baseline_cell_model_sha256'],
            'West parapet normalization requires its exact reviewed retained model')
    start, end = collar['west_boundary_east_m'], collar['blend_end_east_m']
    inner, target, outer = (collar[key] for key in
                            ('inner_north_before_m', 'native_inner_north_m', 'outer_north_m'))
    lower = collar['lower_north_m']
    delta = inner-target
    require(start == -8. and end == -5.5 and 0. < delta <= collar['maximum_displacement_m'] <= .0034524
            and lower == 5. and inner == 6. and outer == 7.5
            and collar['minimum_height_m'] == 16.1892
            and collar['falloff'] == 'piecewise-affine-hat',
            'West parapet normalization exceeds its explicitly approved collar')

    def along(vertex):
        return (end-vertex[0])/(end-start)

    def low(vertex):
        return (-vertex[2]-lower)/(inner-lower)

    def high(vertex):
        return (outer+vertex[2])/(outer-inner)

    planes = (lambda vertex: end-vertex[0],
              lambda vertex: -vertex[2]-lower,
              lambda vertex: outer+vertex[2],
              lambda vertex: along(vertex)-low(vertex),
              lambda vertex: along(vertex)-high(vertex))

    def clip_exact(polygon, plane, positive):
        # An expanded epsilon half-plane can produce a hairline opening when
        # its neighbour retains a tiny real face. Keep exact signed cuts and
        # every resulting fan, including encoded degenerate triangles.
        result = []
        previous = polygon[-1]
        previous_value = plane(previous)
        previous_inside = previous_value >= 0. if positive else previous_value <= 0.
        for current in polygon:
            current_value = plane(current)
            current_inside = current_value >= 0. if positive else current_value <= 0.
            if current_inside != previous_inside:
                fraction = previous_value/(previous_value-current_value)
                result.append(tuple(a+fraction*(b-a) for a, b in zip(previous, current)))
            if current_inside:
                result.append(current)
            previous, previous_value, previous_inside = current, current_value, current_inside
        return result

    model, triangles, changed = parse_s3d(raw_model), [], 0
    bed_height = _native(native_hsr)['bed_y']
    for mesh in model['meshes']:
        require(mesh['frames'] and all(frame == mesh['frames'][0] for frame in mesh['frames']),
                'West parapet normalization requires static model frames')
        for encoded in _triangles(model, mesh['frames'][0]):
            require(all(len(vertex) == 20 for vertex in encoded), 'West parapet requires native XYZUV vertices')
            triangle = tuple(struct.unpack('<5f', vertex) for vertex in encoded)
            if (collar.get('preserve_native_upper_concrete')
                    and min(v[1] for v in triangle) >= bed_height-1e-5
                    and max(v[1] for v in triangle) > bed_height+1e-5):
                # The new border already supplies the native concrete face;
                # retain the historical warp only for its original bed faces.
                triangles.append(triangle)
                continue
            if (min(v[0] for v in triangle) >= end or max(-v[2] for v in triangle) <= lower
                    or min(-v[2] for v in triangle) >= outer
                    or min(v[1] for v in triangle) < collar['minimum_height_m']):
                triangles.append(triangle)
                continue
            polygons = [list(triangle)]
            for plane in planes:
                parts = []
                for polygon in polygons:
                    values = [plane(vertex) for vertex in polygon]
                    if min(values) < 0. and max(values) > 0.:
                        parts.extend(part for part in (clip_exact(polygon, plane, True),
                                                        clip_exact(polygon, plane, False))
                                     if len(part) >= 3)
                    else:
                        parts.append(polygon)
                polygons = parts
            for polygon in polygons:
                vertices = []
                for vertex in polygon:
                    amount = delta*max(0., min(along(vertex), low(vertex), high(vertex)))
                    require(0. <= amount <= collar['maximum_displacement_m'],
                            'West parapet vertex exceeds its displacement bound')
                    x, height, south, u, v = vertex
                    vertices.append((x, height, south+amount, u, v))
                    changed += amount > 0.
                triangles.extend((vertices[0], vertices[index], vertices[index+1])
                                 for index in range(1, len(vertices)-1))
    require(changed, 'West parapet normalization changed no reviewed vertices')
    normalized = parse_s3d(_pack(_native(native_hsr), triangles, preserve_encoded_triangles=True))
    for mesh in normalized['meshes']:
        mesh['name'] = b'SCP HSR junction native west parapet collar\0'
    return pack_s3d(normalized)


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
        alignment = data.get('south_parapet_alignment')
        if alignment is not None:
            for deck in parts[-1][1]['surface_decks']:
                if deck['name'] in ('native_east_west_main', alignment['left_branch']):
                    deck['south_parapet_alignment'] = deepcopy(alignment)
        opposed = data.get('opposed_parapet_alignment')
        if opposed is not None:
            for deck in parts[-1][1]['surface_decks']:
                deck['opposed_parapet_alignment'] = deepcopy(opposed)
                # The normalizer checks this saved-cell proof independently;
                # it does not change the sweep or its geometry cache key.
                deck['opposed_parapet_alignment'].pop('raw_west_cell_sha256', None)
    return parts
