"""Own and compile compact native HSR fan modules with ordinary straight ends.

The independent JSON sources contain literal local traffic paths, complete
physical sweep samples and explicit support centres. The only profile warp
is an authored outer corner, outside every rail and train-clearance corridor.
It frees a neighbouring mainline tile for an ordinary native-width straight.
The new compact core also completes tiny union-clipping holes at its native
east end using only missing native floor, underside and parapet-cap facets;
every original encoded triangle and the matching fan remain unchanged.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
import json
from pathlib import Path
import struct

from scp.dbpf import require

RECIPES = (
    'hsr_component_l2_compact_fan_diverge',
    'hsr_component_l2_paired_fan_compact_join',
)


@lru_cache(maxsize=2)
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


def _compact_corner(x, z, contract):
    """Ease only the outer-profile corner onto the following module's edge."""
    boundary = float(contract['east_boundary'])
    start, end = float(contract['north_start_s3d']), float(contract['north_end_s3d'])
    if x > boundary+1e-10 or z <= start:
        return x, z
    if abs(x-boundary) <= 1e-10:
        x = boundary
    t = min(1., (z-start)/(end-start))
    blend = t*t*t*(10.+t*(-15.+6.*t))
    # Strict partitioning assigns exactly-on-boundary vertical faces west.
    # One micrometre places this new face inside its actual eastern owner.
    target = boundary+float(contract['ownership_epsilon'])
    return x+(target-x)*blend, z


def _split_corner_levels(polygon, contract):
    """Cut both sides of the ownership edge at the two easing breakpoints."""
    from .single_track_models import _clip
    start, end = float(contract['north_start_s3d']), float(contract['north_end_s3d'])
    if max(p[2] for p in polygon) <= start or min(p[2] for p in polygon) >= end:
        return [polygon]
    low = _clip(list(polygon), lambda p: start-p[2])
    middle = _clip(_clip(list(polygon), lambda p: p[2]-start), lambda p: end-p[2])
    high = _clip(list(polygon), lambda p: p[2]-end)
    return [piece for piece in (low,middle,high) if len(piece) >= 3]


def _split_corner_polygon(polygon, contract):
    """Separate unchanged XYZUV faces before moving a bounded outer corner.

    Moving a vertex of an unsplit face changes its affine texture field on
    both sides of the edit boundary. Exact plane cuts retain the outside
    field; only the part inside x<boundary and z>start can then move.
    """
    from .single_track_models import _clip
    east = float(contract['east_boundary'])
    north = float(contract['north_start_s3d'])
    if min(vertex[0] for vertex in polygon) >= east or max(vertex[2] for vertex in polygon) <= north:
        if any(abs(vertex[0]-east) < 1e-10 and vertex[2] > north for vertex in polygon):
            return [(piece, False) for piece in _split_corner_levels(polygon, contract)]
        return [(polygon, False)]
    outside_east = _clip(list(polygon), lambda vertex: vertex[0]-east)
    west = _clip(list(polygon), lambda vertex: east-vertex[0])
    outside_north = _clip(west, lambda vertex: north-vertex[2])
    inside = _clip(west, lambda vertex: vertex[2]-north)
    if len(inside) < 3 or not any(abs(_compact_corner(vertex[0], vertex[2], contract)[0]-vertex[0]) > 1e-10
                                  for vertex in inside):
        return [(polygon, False)]
    end = float(contract['north_end_s3d'])
    transition = _clip(inside, lambda vertex: end-vertex[2])
    clamped = _clip(inside, lambda vertex: vertex[2]-end)
    result = [(piece, False) for piece in _split_corner_levels(outside_east, contract)] if len(outside_east) >= 3 else []
    return result+[(piece, edit) for piece, edit in ((outside_north, False),
                                                   (transition, True), (clamped, True))
                   if len(piece) >= 3]


def _sweep_compact_profile(source, deck):
    """Shape the scoped outer edge while preserving outside XYZUV fields."""
    from .hsr_components import _sweep_component_profile
    from .single_track_models import _triangulate
    from .rail_geometry import _convex_parts
    surfaces, corridors, points, lengths = _sweep_component_profile(source, deck)
    contract = deck.get('compact_native_corner')
    if contract is None:
        return surfaces, corridors, points, lengths
    changed = []
    for kind, triangle in surfaces:
        pieces = _split_corner_polygon(triangle, contract)
        touches_boundary = any(abs(vertex[0]-float(contract['east_boundary'])) < 1e-10
                               and vertex[2] > float(contract['north_start_s3d']) for vertex in triangle)
        if len(pieces) == 1 and not pieces[0][1] and not touches_boundary:
            changed.append((kind, triangle))
            continue
        for polygon, edit in pieces:
            vertices = []
            for x, height, z, u, v in polygon:
                boundary_vertex = abs(x-float(contract['east_boundary'])) < 1e-10
                xx, zz = _compact_corner(x, z, contract) if edit or boundary_vertex else (x, z)
                require(kind != 'rail' or abs(xx-x) < 1e-10,
                        'Compact outer-corner adjustment touches a rail ribbon')
                vertices.append((xx, height, zz, u, v))
            changed.extend((kind, piece) for piece in _triangulate(vertices))
    adjusted = []
    for corridor in corridors:
        # Keep true train clearance and rail ribbons entirely unchanged.
        for polygon in corridor.get('clearance_polygons', []):
            require(all(abs(_compact_corner(x, z, contract)[0]-x) < 1e-10 for x, z in polygon),
                    'Compact outer-corner adjustment touches train clearance')
        polygon = [(x, 0., z, 0., 0.) for x, z in corridor['polygon']]
        pieces = _split_corner_polygon(polygon, contract)
        touches_boundary = any(abs(vertex[0]-float(contract['east_boundary'])) < 1e-10
                               and vertex[2] > float(contract['north_start_s3d']) for vertex in polygon)
        if len(pieces) == 1 and not pieces[0][1] and not touches_boundary:
            adjusted.append(corridor)
            continue
        first = True
        for piece, edit in pieces:
            footprint = [_compact_corner(x, z, contract)
                         if edit or abs(x-float(contract['east_boundary'])) < 1e-10 else (x, z)
                         for x, height, z, u, v in piece]
            for convex in _convex_parts(footprint):
                area = abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(convex,convex[1:]+convex[:1])))/2.
                if area <= 1e-12:
                    continue
                adjusted.append({**corridor, 'polygon': convex,
                    'rail_polygons': corridor['rail_polygons'] if first else [],
                    'clearance_polygons': corridor.get('clearance_polygons', []) if first else []})
                first = False
    return changed, adjusted, points, lengths


def model_inputs(recipe):
    """Return selected native sweep cells and the exact independent context."""
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


@lru_cache(maxsize=2)
def _cached_models(native_hsr, signature):
    from .hsr_mesh import _compile_models
    config = json.loads(signature)
    layout = {tuple(cell): data for cell, data in config['layout']}
    return tuple(_compile_models(native_hsr, layout, config,
                                sweep_function=_sweep_compact_profile).items())


def _missing_native_facets(triangles, donors, height):
    """Subtract actual coverage from native XYZUV facets without refitting UVs."""
    from .directional_t import _floor_subtract, _plan_area
    blockers = [triangle for triangle in triangles
                if all(abs(vertex[1]-height) < .0001 for vertex in triangle)
                and max(vertex[0] for vertex in triangle) >= 7.99]
    result = []
    for triangle in donors:
        pieces = [list(triangle)]
        for other in blockers:
            remaining = []
            for polygon in pieces:
                if (max(p[2] for p in polygon) < min(p[2] for p in other)
                        or min(p[2] for p in polygon) > max(p[2] for p in other)):
                    remaining.append(polygon)
                else:
                    remaining.extend(_floor_subtract(polygon, list(other)))
            pieces = [polygon for polygon in remaining if _plan_area(polygon) > 1e-17]
            if not pieces:
                break
        result.extend(pieces)
    return result


def _native_end_patches(source, triangles, surfaces):
    """Complete only sub-square-millimetre native holes in the final 10 mm.

    Global union clipping can leave tiny holes after float32 vertex packing.
    Subtracting the actual faces from the original native horizontal facets
    retains each plane's own affine texture mapping and winding. Rail ribbons
    have their usual priority over ballast. The area guard rejects a missing
    end or a larger defect instead of hiding it with a replacement surface.
    """
    from .directional_t import _plan_area
    from .hsr_mesh import _height_aware_union
    from .single_track_models import _clip, _triangulate
    planes = ((source['bed_y'], ('rail', 'bed')),
              (source['bottom'], ('underside',)),
              (source['top'], ('wall',)))
    patches = []
    for height, kinds in planes:
        cropped = []
        for kind in kinds:
            for actual, triangle in surfaces:
                if actual != kind or not all(abs(v[1]-height) < .0001 for v in triangle):
                    continue
                polygon = list(triangle)
                polygon = _clip(polygon, lambda p: p[0]-167.99)
                polygon = _clip(polygon, lambda p: 168.-p[0])
                cropped.extend((kind, tuple((x-160., y, z-80., u, v)
                                            for x, y, z, u, v in part))
                               for part in _triangulate(polygon))
        donors = [triangle for kind, triangle in
                  _height_aware_union(cropped, single_sheet=True, tagged=True)]
        require(donors, 'Compact native end lacks its original horizontal profile')
        missing = _missing_native_facets(triangles, donors, height)
        require(sum(_plan_area(polygon) for polygon in missing) <= 1e-6,
                'Compact native end defect exceeds its bounded native-surface completion')
        for polygon in missing:
            for number in range(1, len(polygon)-1):
                # Quantize now: a sub-float32 edge sliver is already the
                # native precision, rather than a distinct renderable face.
                triangle = tuple(struct.unpack('<5f', struct.pack('<5f', *vertex))
                                 for vertex in (polygon[0], polygon[number], polygon[number+1]))
                if _plan_area(list(triangle)) > 1e-17:
                    require(all(7.99-1e-6 <= p[0] <= 8. for p in triangle),
                            'Compact native end patch leaves its final 10 mm collar')
                    patches.append(triangle)
    return patches


def _complete_core_native_end(native_hsr, raw, deck):
    """Append missing end facets; keep every existing encoded face unchanged."""
    from scp.models import parse_s3d
    from .hsr_components import _sweep_component_profile
    from .interchange_verify import _triangles
    from .single_track_models import _native, _pack
    source = _native(native_hsr)
    require(deck['name'] == 'native_east_west_main' and deck['width'] == 15.,
            'Compact native end completion requires its ordinary paired mainline')
    triangles = list(_triangles(parse_s3d(raw)))
    surfaces = _sweep_component_profile(source, deck)[0]
    patches = _native_end_patches(source, triangles, surfaces)
    return _pack(source, triangles+patches, preserve_encoded_triangles=True) if patches else raw


def build_models(native_hsr, recipe):
    """Emit only the module's own cells and explicit slope-seated supports."""
    mapping, config = model_inputs(recipe)
    signature = json.dumps(config, sort_keys=True, separators=(',', ':'), allow_nan=False)
    models = dict(_cached_models(native_hsr, signature))
    result = {local: models[source] for local, source in mapping.items()}
    if recipe == 'hsr_component_l2_compact_fan_diverge':
        result[2, 0] = _complete_core_native_end(native_hsr, result[2, 0], config['surface_decks'][0])
    return result
