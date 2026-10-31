"""Highway assembly artwork from complete component source routes."""
from scp.dbpf import require
from .menu import make_icon


def assembly_icon_network(assembly_id):
    require(assembly_id in ('ddrhw-l1-and-l2-diagonal-avenue-diamond',
                           'ddrhw-l1-and-l2-diagonal-avenue-modular-diamond'),
            'No declared highway assembly icon network')
    return 'HWY'


def assembly_icon_routes(scene, pieces):
    """Transform local component channels into the declared assembly pose."""
    from . import ramp_paths
    require(hasattr(ramp_paths, 'component_routes'),
            'Highway assembly artwork needs complete local component source routes')
    by_id = {piece['id']: piece for piece in pieces}
    placements = scene.get('placements', scene.get('instances'))
    require(isinstance(placements, list) and placements, 'Highway assembly icon needs placements')
    result = []
    for placement in placements:
        require(placement['piece_id'] in by_id, 'Highway icon placement refers to an unknown component')
        piece = by_id[placement['piece_id']]
        require(piece.get('domain') == 'highway', 'Highway assembly icon cannot mix network domains')
        turns = placement.get('rotation_ccw_degrees', placement.get(
            'rotation_degrees_ccw', placement.get('rotation_degrees', 0)))
        require(turns in (0, 90, 180, 270), 'Highway assembly icon needs proper cardinal rotations')
        east, north = placement['origin_m']
        if piece.get('recipe') == 'highway_ddrhw_modular_stamp':
            from .modular_stamp import reference
            source = []
            groups = {}
            stamp = reference()
            stamp_origin = stamp['source_layout_origin_cell']
            for row in stamp['cells']:
                origin = tuple(row['source_world_cell'][axis] - row['source_local_cell'][axis]
                               for axis in (0, 1))
                groups[row['source_piece_id'], origin] = by_id[row['source_piece_id']]
            for (_identifier, origin), inherited in groups.items():
                offset = (16 * (origin[0] - stamp_origin[0]), -16 * (origin[1] - stamp_origin[1]))
                source.extend([[(point[0] + offset[0], point[1] + offset[1], point[2]) for point in route]
                               for route in ramp_paths.component_routes(inherited)])
        elif piece.get('recipe', '').startswith('highway_ddrhw_modular_'):
            from .modular_ramps import component_routes
            source = component_routes(piece)
        else:
            source = ramp_paths.component_routes(piece)
        channels = source.values() if isinstance(source, dict) else source
        for points in channels:
            posed = []
            for x, y, height in points:
                for _ in range(turns // 90):
                    x, y = -y, x
                posed.append((x + east, y + north, height))
            result.append(posed)
    require(result, 'Highway assembly icon has no source routes')
    return result
