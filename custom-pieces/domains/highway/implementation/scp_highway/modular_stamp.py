"""One straight highway stamp with openings for independently placed ramps.

The frozen 27-cell source remains an immutable input. Its curved branch faces
and six wing construction cells move to the separately placed ramp owners;
native decks, inside-corridor slip-lane paint, and centre piers remain here.
"""
from __future__ import annotations

from pathlib import Path

from scp import jsonc
from scp.dbpf import require

RECIPE = 'highway_ddrhw_modular_stamp'
KEY = 'modular-stamp'
ROOT = Path(__file__).resolve().parents[4]
REFERENCE = 'domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/checks/stamp-reference.jsonc'


def reference():
    return jsonc.load(ROOT / REFERENCE)


def declaration():
    from .straight_stamp_geometry import stamp_cells
    data = reference()
    retained = stamp_cells()
    cells = [row['cell'] for row in data['cells'] if tuple(row['source_world_cell']) in retained]
    return {'key': KEY, 'geometry_key': KEY, 'recipe': RECIPE,
            'name': 'DD RHW-4 Highway and Slip-Lane Stamp',
            'world_origin_cell': data['source_layout_origin_cell'],
            'cells': cells, 'footprint': data['footprint'],
            'engineering': {'max_grade_percent': 30.0,
                            'car_corridor_half_width_m': 1.25,
                            'car_corridor_height_m': 3.8,
                            'pavement_path_offset_m': 0.0,
                            'model_only_cells': []},
            'authors_surface_atlas': False}


def compile_module(spec, context):
    from .straight_stamp_geometry import partition, source_cells
    declared = declaration()
    require(spec['cells'] == declared['cells'] and spec['footprint'] == declared['footprint'],
            'Highway stamp differs from its straight 21-cell declaration')
    separated = partition(context)
    original = source_cells(context)
    result = []
    for record in reference()['cells']:
        world = tuple(record['source_world_cell'])
        if world in separated['stamp_models']:
            result.append((tuple(record['cell']), separated['stamp_models'][world], original[world][1]))
    return result


def build_piece(spec, context):
    from .recipes import finish_piece
    from .adaptive_ground import build_resources, build_construction
    from scp.adaptive_network import RUL1
    from scp.build import RUL0
    compiled = compile_module(spec, context)
    assets = finish_piece(spec, context, compiled)
    active = build_resources(spec, context, compiled)
    require(not assets.keys() & active.keys(), 'Adaptive stamp resources overlap canonical resources')
    assets.update(active)
    return assets, build_construction(spec, compiled, context['controller'][RUL0], context['controller'][RUL1])
