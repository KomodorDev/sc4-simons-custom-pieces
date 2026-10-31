"""Functional, nonoverlapping whole-cell owners for the approved tight diamond.

A city cell owns every native and authored PATH fragment crossing it. Physical
models may overhang that owner, so a straight grade and its curved departure
can meet at their real functional boundary without pretending PATHs stop there.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache

from .parallel_ramp_review import review

RECIPE_PREFIX = 'highway_ddrhw_parallel_'

# Exact world city cells. Each retained native cell is emitted once only.
GROUPS = {
    'crossing': ('DD RHW / Avenue Crossing', ((0, 0), (1, 0), (0, 1)), 'crossing'),
    'northwest-terminal': ('Northwest Avenue Right-Turn Terminal', ((-1, -1), (0, -1), (-1, 0)), 'terminal'),
    'southeast-terminal': ('Southeast Avenue Right-Turn Terminal', ((1, 1), (2, 1), (1, 2)), 'terminal'),
    'lower-exit-slip': ('L1 Exit Slip Lanes', ((3, -3), (2, -2)), 'slip'),
    'lower-entry-slip': ('L1 Entry Slip Lanes', ((-2, 2), (-3, 3)), 'slip'),
    'upper-exit-slip': ('L2 Exit Slip Lanes', ((-2, 3), (-3, 4)), 'slip'),
    'upper-entry-slip': ('L2 Entry Slip Lanes', ((4, -3), (3, -2)), 'slip'),
    'lower-exit-departure': ('L1 Exit Lateral Departure', ((2, -3),), 'departure'),
    'lower-entry-departure': ('L1 Entry Lateral Departure', ((-3, 2),), 'departure'),
    'upper-exit-departure': ('L2 Exit Lateral Departure', ((-2, 4),), 'departure'),
    'upper-entry-departure': ('L2 Entry Lateral Departure', ((4, -2),), 'departure'),
    'lower-exit-grade': ('L1 Exit Parallel Grade', ((1, -2), (1, -1)), 'grade'),
    'lower-entry-grade': ('L1 Entry Parallel Grade', ((-2, 1), (-1, 1)), 'grade'),
    'upper-exit-grade': ('L2 Exit Parallel Grade', ((-1, 2), (0, 2), (-1, 3)), 'grade'),
    'upper-entry-grade': ('L2 Entry Parallel Grade', ((2, -1), (3, -1), (2, 0)), 'grade'),
}

# The straight stem visually owns these intact native halves and their piers.
# Their whole-city-cell PATHs remain with the adjacent grade traffic owners.
STRAIGHT_MODEL_HOSTS = {(1, -1): (2, -2), (-1, 1): (-2, 2),
                        (-1, 2): (-2, 3), (2, -1): (3, -2)}



@lru_cache(maxsize=1)
def _catalog():
    candidate = next(row for row in review()['candidates'] if row['id'] == 'parallel-inward-upper')
    expected = set(map(tuple, candidate['owned_cells']))
    seen, records = set(), []
    for key, (name, cells, function) in GROUPS.items():
        cells = sorted(cells, key=lambda c: (c[1], c[0]))
        if seen.intersection(cells):
            raise ValueError('Parallel functional modules overlap whole-cell traffic ownership')
        seen.update(cells)
        origin = min(c[0] for c in cells), min(c[1] for c in cells)
        local = [[c[0] - origin[0], c[1] - origin[1]] for c in cells]
        records.append({'key': key, 'geometry_key': 'parallel-' + key, 'name': name, 'function': function,
                        'recipe': RECIPE_PREFIX + key.replace('-', '_'),
                        'world_origin_cell': list(origin), 'world_cells': [list(c) for c in cells],
                        'cells': local, 'footprint': [max(c[0] for c in local) + 1,
                                                     max(c[1] for c in local) + 1],
                        'authors_surface_atlas': False,
                        'engineering': {
                            'max_grade_percent': 30.0, 'car_corridor_half_width_m': 1.25,
                            'car_corridor_height_m': 3.8, 'pavement_path_offset_m': 0.0,
                            'model_only_cells': [], 'path_ownership': 'Every full native and ramp fragment in each owned city cell',
                            'physical_model_function': function,
                            **({'ground_mouth_profile': 'taper-6m-to-3p5m-over-3m'}
                               if function == 'terminal' else {}),
                            'model_overhang': True,
                            'authored_model_overhang': function != 'crossing',
                            'pure_ramp_model': function in ('departure', 'grade'),
                            'native_model_transfers': [
                                {'source_city_cell': list(source), 'model_host_city_cell': list(host),
                                 'native_path_owner': owner(source), 'native_model_owner': owner(host)}
                                for source, host in STRAIGHT_MODEL_HOSTS.items()
                                if key in (owner(source), owner(host))],
                            'native_avenue_cells': [list(c) for c in cells if c[0] - c[1] in (-1, 0, 1)],
                            'native_highway_cells': [list(c) for c in cells if sum(c) in (0, 1)],
                            'reuse_limit': 'Outside-deck access PATHs change all four ordinary highway continuation cells; no whole existing native half is substituted'}})
    if seen != expected or len(seen) != 31:
        raise ValueError('Parallel modules must preserve the approved exact 31-cell union')
    return {'types': records, 'occupied_cells': [list(c) for c in sorted(seen, key=lambda c: (c[1], c[0]))],
            'bounds': deepcopy(candidate['bounds']), 'layout_id': 'parallel-inward-upper',
            'placement_count': len(records)}


def module_catalog():
    """Return fresh declarations for root allocation and saved-resource checks."""
    return deepcopy(_catalog())


def owner(cell):
    return next(key for key, (_name, cells, _function) in GROUPS.items() if tuple(cell) in cells)
