"""Native resource compiler for the complementary parallel-diamond phase."""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import hashlib
from pathlib import Path

from scp.models import pack_s3d, parse_s3d
from scp.recipes import combine_meshes

from . import ramp_geometry as geometry
from . import ramp_paths as paths
from .native import channels, material_template, parse_paths
from .parallel_b_geometry import AVENUE_PHASE_OFFSET, procedural_geometry, traffic_routes
from .parallel_b_layout import GEOMETRY_PREFIX, GROUPS, STRAIGHT_MODEL_HOSTS, module_catalog
from .parallel_geometry import ParallelRoadPainter
from .wheeltracks import NativeWheeltrackField


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def declaration(spec):
    key = spec['geometry_key'].removeprefix(GEOMETRY_PREFIX)
    _require(spec['geometry_key'] == GEOMETRY_PREFIX + key,
             'Alignment B compiler requires its explicit geometry prefix')
    return next(row for row in module_catalog()['types'] if row['key'] == key)


def _closest(cell, candidates):
    return min(candidates, key=lambda c: ((c[0] - cell[0]) ** 2 + (c[1] - cell[1]) ** 2,
                                          c[1], c[0]))


def _native_cell(context, cell):
    """Keep the original DD phase and select the adjacent Avenue lattice."""
    models, highway, avenue = [], [], []
    total, difference = sum(cell), cell[0] - cell[1] - AVENUE_PHASE_OFFSET
    if total in (0, 1):
        donor, turns = (0x5753A380, 0) if total == 0 else (0x5753A300, 2)
        model, highway = channels(context['dd_rhw'], donor, False, turns)
        models.append((model, model['meshes'], (0.0, 0.0, 0.0)))
    if difference in (-1, 0, 1):
        donor, turns = ((0x5753A305, 0) if difference == 0
                        else (0x5753A300, 0 if difference == 1 else 2))
        model, avenue = channels(context['dd_rhw'], donor, True, turns)
        models.append((model, model['meshes'], (0.0, 0.0, 0.0)))
    return models, highway, avenue


def _build_world(context):
    """Compile a fresh half-grid partition before selecting a functional owner."""
    names = ('parallel_b_geometry', 'parallel_b_layout', 'parallel_b_modules',
             'parallel_geometry', 'parallel_slip_lanes', 'parallel_layout',
             'parallel_ramp_review', 'ramp_geometry', 'ramp_materials', 'wheeltracks', 'slip_lanes')
    revision = hashlib.sha256(b''.join(Path(__file__).with_name(name + '.py').read_bytes()
                                      for name in names)).hexdigest()
    cached = context.get('_parallel_b_compiled_world')
    if cached is not None and context.get('_parallel_b_compiler_sha256') == revision:
        return cached
    physical, model_faces = procedural_geometry()
    painter = ParallelRoadPainter(context, physical)
    wheeltracks = NativeWheeltrackField(physical, painter, retain_nonzero_top_fragments=True)
    base, _routes = channels(context['dd_rhw'], 0x5753A380, False, 0)
    material = material_template(context)
    cells = set(map(tuple, module_catalog()['occupied_cells']))
    parts, ground = defaultdict(list), defaultdict(list)
    for key, faces in model_faces.items():
        candidates = GROUPS[key][1]
        for cell, triangles in geometry.partition_triangles(faces).items():
            host = cell if cell in candidates else _closest(cell, candidates)
            raw = geometry.pack_road_model(triangles, 0, material_template=material,
                                          model_template=base, native_painter=painter, cell=cell)
            model = parse_s3d(raw)
            parts[host].append((model, model['meshes'],
                               (16.0 * (cell[0] - host[0]), 0.0,
                                16.0 * (cell[1] - host[1]))))
            for triangle in triangles:
                if all(abs(point[1]) < 1e-8
                       and abs(point[3] - geometry.ATLAS_UV['asphalt'][0]) < 1e-8
                       for point in triangle):
                    ground[cell].append(tuple((p[0] + 16.0 * cell[0], p[1],
                                               p[2] + 16.0 * cell[1], *p[3:]) for p in triangle))
    additional = paths.slice_routes(traffic_routes())
    result, native_changes, encoded_paths = {}, {}, {}
    for cell in sorted(cells, key=lambda c: (c[1], c[0])):
        native_models, highway, avenue = _native_cell(context, cell)
        if native_models:
            native_raw = pack_s3d(combine_meshes(native_models))
            opened, report = geometry.cut_native_branch_openings(
                native_raw, cell, physical, ground_pavement=ground[cell], wheeltracks=wheeltracks)
            model = parse_s3d(opened)
            host = STRAIGHT_MODEL_HOSTS.get(cell, cell)
            delta = (16.0 * (cell[0] - host[0]), 0.0, 16.0 * (cell[1] - host[1]))
            parts[host].insert(0, (model, model['meshes'], delta))
            native_changes[cell] = report
        routes = [paths._route_metadata(route, 'native-highway') for route in highway]
        routes += [paths._route_metadata(route, 'native-avenue') for route in avenue]
        routes += deepcopy(additional.get(cell, []))
        routes = paths.mark_junctions(paths.deduplicate_routes({cell: routes}))[cell]
        _require(routes, f'Alignment B cell {cell} has no complete traffic')
        encoded_paths[cell] = paths.encode_paths(routes)
    for cell in sorted(cells, key=lambda c: (c[1], c[0])):
        _require(parts[cell], f'Alignment B cell {cell} has no actual visible model')
        result[cell] = pack_s3d(combine_meshes(parts[cell])), encoded_paths[cell]
    context['_parallel_b_compiler_sha256'] = revision
    context['_parallel_b_compiled_world'] = result
    context['_parallel_b_native_changes'] = native_changes
    return result


def compile_module(spec, context):
    """Return normalized cells with complete canonical saved model/PATH bytes."""
    record = declaration(spec)
    _require(spec['cells'] == record['cells'] and spec['footprint'] == record['footprint'],
             'Alignment B allocation differs from the minimum whole-cell partition')
    world = _build_world(context)
    ox, oy = record['world_origin_cell']
    return [(tuple(local), *world[(local[0] + ox, local[1] + oy)]) for local in spec['cells']]


def construction_fields(spec, compiled):
    """Derive both actual native network fields from each saved traffic owner."""
    record = declaration(spec)
    ox, oy = record['world_origin_cell']
    width, depth = record['footprint']
    rows = [['.'] * (width + 2) for _ in range(depth + 1)]
    cons = deepcopy(rows)
    rows[0][-1] = cons[0][-1] = '<'
    rows[-1][0] = cons[-1][0] = '^'
    palette = []
    for index, (local, _model, raw) in enumerate(compiled):
        symbol = paths.construction_symbol(index)
        x, y = local
        rows[y][x] = symbol
        world = x + ox, y + oy
        difference = world[0] - world[1] - AVENUE_PHASE_OFFSET
        native_avenue = difference in (-1, 0, 1)
        native_highway = sum(world) in (0, 1)
        routes = [paths._route_metadata(route, 'saved') for route in parse_paths(raw)]
        custom = [route for route in routes if route['junction'] and route['transport'] == paths.CAR]
        if not native_avenue:
            custom = routes
        fields = []
        if native_highway or custom or not native_avenue:
            fields.append(f'dirtroad: 0x{paths.construction_flags(custom):08X}')
        if native_avenue:
            word = 0x01030103 if difference == 0 else 0x01000003 if difference == 1 else 0x00030100
            fields.append(f'avenue: 0x{word:08X}')
        palette.append(symbol + ' - ' + ' '.join(fields))
        cons[y][x] = '+' if native_highway or custom or not native_avenue else '\\'
    return [''.join(row) for row in rows], palette, [''.join(row) for row in cons]


def build_piece(spec, context):
    """Finish canonical models, adaptive Avenue aliases, and explicit no-shadow policy."""
    from .recipes import finish_piece, construction
    compiled = compile_module(spec, context)
    assets = finish_piece(spec, context, compiled)
    _require(not spec.get('authored_texture_ids'), 'Alignment B retains audited native materials')
    if spec.get('adaptive_ground'):
        from .adaptive_ground import build_resources, build_construction
        from scp.adaptive_network import RUL1
        from scp.build import RUL0
        extra = build_resources(spec, context, compiled)
        _require(not assets.keys() & extra.keys(), 'Alignment B adaptive and canonical resources overlap')
        assets.update(extra)
        rules = build_construction(spec, compiled, context['controller'][RUL0], context['controller'][RUL1])
    else:
        rules = construction(spec, *construction_fields(spec, compiled))
    _require(spec.get('shadow_mode') == 'model-carrier'
             and spec.get('model_shadows', {}).get('enabled') is False,
             'Alignment B must retain the explicit no-shadow policy')
    from .model_shadows import add_shadows
    add_shadows(spec, context, compiled, assets)
    return assets, rules
