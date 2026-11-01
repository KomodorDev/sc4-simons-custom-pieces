"""Highway assembly artwork from complete component source routes."""
from scp.dbpf import require
from .menu import make_icon


def assembly_icon_network(assembly_id):
    require(assembly_id in ('ddrhw-l1-and-l2-diagonal-avenue-diamond',
                           'ddrhw-l1-and-l2-diagonal-avenue-modular-diamond',
                           'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond',
                           'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b'),
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
            from .straight_stamp_geometry import stamp_cells
            from .ramp_geometry import world_coordinates
            source = []
            stamp_origin = reference()['source_layout_origin_cell']
            # Slice the retained traffic sources to the21 actual owners.
            # Replaying an old branch type would reintroduce its wing cells.
            lines = [route['points'] for route in ramp_paths.compact_access_routes()]
            import math
            for lateral in (-3.2 / math.sqrt(2), 3.2 / math.sqrt(2)):
                lines.extend(([world_coordinates(-200., lateral, 15.), world_coordinates(200., lateral, 15.)],
                              [world_coordinates(200., lateral, 7.5), world_coordinates(-200., lateral, 7.5)]))
            for lateral in (4.8 / math.sqrt(2), 11.2 / math.sqrt(2)):
                lines.extend(([world_coordinates(lateral, -200.), world_coordinates(lateral, 200.)],
                              [world_coordinates(-lateral, 200.), world_coordinates(-lateral, -200.)]))
            for line in lines:
                for cell, points in ramp_paths.polyline_fragments(line):
                    if cell in stamp_cells():
                        source.append([(p[0] + 16 * (cell[0] - stamp_origin[0]),
                                        p[1] - 16 * (cell[1] - stamp_origin[1]), p[2]) for p in points])
        elif piece.get('recipe', '').startswith('highway_ddrhw_modular_'):
            from .modular_ramps import component_routes
            source = component_routes(piece)
        elif piece.get('recipe', '').startswith('highway_ddrhw_parallel_b_'):
            from .parallel_alignment_b_verify import expected_cell_routes, _source_origin, PARTITIONS
            ox, oy = _source_origin(piece)
            cell_routes = expected_cell_routes()
            source = [[(x - 16. * ox, y + 16. * oy, h) for x, y, h in route['points']]
                      for cell in PARTITIONS[piece['geometry_key'].removeprefix('parallel-b-')]
                      for route in cell_routes[cell]]
        elif piece.get('recipe', '').startswith('highway_ddrhw_parallel_'):
            # The frozen approved lines include native through services and
            # every ramp cut. Transform their complete whole-cell partition
            # into this component's local frame before applying its placement.
            from .parallel_verify import expected_cell_routes, _source_origin, PARTITIONS
            ox, oy = _source_origin(piece)
            cell_routes = expected_cell_routes(piece.get('engineering', {}).get('highway_slip_profile'))
            source = [[(x - 16. * ox, y + 16. * oy, h) for x, y, h in route['points']]
                      for cell in PARTITIONS[piece['geometry_key'].removeprefix('parallel-')]
                      for route in cell_routes[cell]]
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
