"""Minimum whole-city-cell owners for the complementary parallel diamond."""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache

from .parallel_b_geometry import AVENUE_PHASE_OFFSET, required_traffic_cells, procedural_geometry

RECIPE_PREFIX = 'highway_ddrhw_parallel_b_'
GEOMETRY_PREFIX = 'parallel-b-'
GROUPS = {
    'crossing': ('DD RHW / Avenue Crossing', ((0, 0), (1, 0), (1, -1)), 'crossing'),
    'northwest-terminal': ('Northwest Avenue Right-Turn Terminal', ((-1, -1), (0, -1), (0, -2)), 'terminal'),
    'southeast-terminal': ('Southeast Avenue Right-Turn Terminal', ((1, 1), (2, 0)), 'terminal'),
    'lower-exit-slip': ('L1 Exit Slip Lanes', ((4, -4), (3, -3)), 'slip'),
    'lower-entry-slip': ('L1 Entry Slip Lanes', ((-2, 2), (-3, 3)), 'slip'),
    'upper-exit-slip': ('L2 Exit Slip Lanes', ((-3, 4), (-2, 3), (-1, 2)), 'slip'),
    'upper-entry-slip': ('L2 Entry Slip Lanes', ((5, -4), (4, -3), (3, -2)), 'slip'),
    'lower-exit-departure': ('L1 Exit Lateral Departure', ((3, -4),), 'departure'),
    'lower-entry-departure': ('L1 Entry Lateral Departure', ((-3, 2),), 'departure'),
    'upper-exit-departure': ('L2 Exit Lateral Departure', ((-2, 4),), 'departure'),
    'upper-entry-departure': ('L2 Entry Lateral Departure', ((5, -3),), 'departure'),
    'lower-exit-grade': ('L1 Exit Parallel Grade', ((2, -3), (2, -2), (1, -2)), 'grade'),
    'lower-entry-grade': ('L1 Entry Parallel Grade', ((-2, 1), (-1, 1), (-1, 0)), 'grade'),
    'upper-exit-grade': ('L2 Exit Parallel Grade', ((-1, 3), (0, 2), (0, 1)), 'grade'),
    'upper-entry-grade': ('L2 Entry Parallel Grade', ((4, -2), (3, -1), (2, -1)), 'grade'),
}
STRAIGHT_MODEL_HOSTS = {(2, -2): (3, -3), (-1, 1): (-2, 2),
                        (0, 1): (-1, 2), (2, -1): (3, -2)}


def owner(cell):
    return next(key for key, (_name, cells, _role) in GROUPS.items() if tuple(cell) in cells)


@lru_cache(maxsize=1)
def _catalog():
    seen, records = set(), []
    for key, (name, cells, function) in GROUPS.items():
        cells = sorted(cells, key=lambda cell: (cell[1], cell[0]))
        if seen.intersection(cells):
            raise ValueError('Alignment B functional owners overlap a whole-city PATH cell')
        seen.update(cells)
        origin = min(c[0] for c in cells), min(c[1] for c in cells)
        local = [[c[0] - origin[0], c[1] - origin[1]] for c in cells]
        records.append({'key': key, 'geometry_key': GEOMETRY_PREFIX + key, 'name': name,
                        'function': function, 'recipe': RECIPE_PREFIX + key.replace('-', '_'),
                        'world_origin_cell': list(origin), 'world_cells': [list(c) for c in cells],
                        'cells': local, 'footprint': [max(c[0] for c in local) + 1,
                                                     max(c[1] for c in local) + 1],
                        'authors_surface_atlas': False,
                        'engineering': {
                            'grid_alignment': 'B', 'alignment_a_translation_en_m': [8.0, 8.0],
                            'avenue_phase_offset': AVENUE_PHASE_OFFSET,
                            'highway_slip_profile': 'shoulder-auxiliary-lower-8m-4m-upper-5m-1m',
                            'max_grade_percent': 30.0, 'car_corridor_half_width_m': 1.25,
                            'car_corridor_height_m': 3.8, 'pavement_path_offset_m': 0.0,
                            'model_only_cells': [],
                            'path_ownership': 'Every full native and ramp fragment in each owned city cell',
                            'physical_model_function': function,
                            **({'ground_mouth_profile': 'taper-6m-to-3p5m-over-3m'}
                               if function == 'terminal' else {}),
                            'model_overhang': True, 'authored_model_overhang': function != 'crossing',
                            'pure_ramp_model': function in ('departure', 'grade'),
                            'native_model_transfers': [
                                {'source_city_cell': list(source), 'model_host_city_cell': list(host),
                                 'native_path_owner': owner(source), 'native_model_owner': owner(host)}
                                for source, host in STRAIGHT_MODEL_HOSTS.items()
                                if key in (owner(source), owner(host))],
                            'native_avenue_cells': [list(c) for c in cells
                                                    if c[0] - c[1] - AVENUE_PHASE_OFFSET in (-1, 0, 1)],
                            'native_highway_cells': [list(c) for c in cells if sum(c) in (0, 1)],
                            'reuse_limit': 'Half-grid recutting changes complete native and ramp PATH ownership; no Alignment A whole type is substituted'}})
    if seen != required_traffic_cells() or len(seen) != 34:
        raise ValueError('Alignment B owners must be exactly the 34 required traffic cells')
    from .ramp_geometry import partition_triangles
    _ramps, models = procedural_geometry()
    if any(not set(partition_triangles(faces)) <= seen for faces in models.values()):
        raise ValueError('An Alignment B physical model projects outside its declared traffic union')
    bounds = {'minimum_cell': [-3, -4], 'maximum_cell': [5, 4],
              'tiles': [9, 9], 'metres': [144.0, 144.0]}
    return {'types': records,
            'occupied_cells': [list(c) for c in sorted(seen, key=lambda cell: (cell[1], cell[0]))],
            'bounds': bounds, 'layout_id': 'parallel-inward-upper-alignment-b',
            'placement_count': len(records), 'grid_alignment': 'B'}


def module_catalog():
    """Return fresh declarations without allocating or changing Alignment A."""
    return deepcopy(_catalog())
