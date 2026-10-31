"""One placeable highway/slip-lane stamp with independently attached ramps.

Twenty-five inherited models and all 27 PATHs are retained byte for byte.
Two Avenue-only cells restore the independently pinned pristine pavement.
No grade or Avenue terminal is included. The frozen independent reference is
also used by the saved-resource verifier, rather than regenerated expectations.
"""
from __future__ import annotations

import hashlib
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
    data = reference()
    cells = [row['cell'] for row in data['cells']]
    return {'key': KEY, 'geometry_key': KEY, 'recipe': RECIPE,
            'name': 'DD RHW-4 Highway and Slip-Lane Stamp',
            'world_origin_cell': data['source_layout_origin_cell'],
            'cells': cells, 'footprint': data['footprint'],
            'engineering': {'max_grade_percent': 30.0,
                            'car_corridor_half_width_m': 1.25,
                            'car_corridor_height_m': 3.8,
                            'pavement_path_offset_m': 0.0,
                            'model_only_cells': [row['cell'] for row in data['cells']
                              if row['source_world_cell'] in ([-3,5], [5,-3])]},
            'authors_surface_atlas': False}


def compile_module(spec, context):
    from .ramp_paths import compile_module as compile_source
    declared = declaration()
    require(spec['cells'] == declared['cells'] and spec['footprint'] == declared['footprint'],
            'Highway stamp differs from its independent 27-cell reference')
    compiled = {}
    for record in reference()['cells']:
        identifier = record['source_piece_id']
        if identifier not in compiled:
            source = jsonc.load(ROOT / 'domains/highway/00_pieces' / identifier / 'piece.jsonc')
            compiled[identifier] = {tuple(cell): (model, path)
                                   for cell, model, path in compile_source(source, context)}
    from .native import build_crossing_channels
    pristine = {tuple(cell): model for cell, model, _path in build_crossing_channels(context)}
    result = []
    for record in reference()['cells']:
        model, path = compiled[record['source_piece_id']][tuple(record['source_local_cell'])]
        if 'inherited_model_sha256' in record:
            require(hashlib.sha256(model).hexdigest() == record['inherited_model_sha256'],
                    'The scoped old Avenue apron reference changed')
            model = pristine[tuple(record['source_local_cell'])]
        require(hashlib.sha256(model).hexdigest() == record['model_sha256'] and
                hashlib.sha256(path).hexdigest() == record['path_sha256'],
                'Retained highway/slip-lane source geometry differs from the accepted reference')
        result.append((tuple(record['cell']), model, path))
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
