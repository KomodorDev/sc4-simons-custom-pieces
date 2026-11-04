"""Measured physical owners for the separately reviewed reversed-traffic Y.

Actual saved city-cell ownership justifies these three local reservations.
Complete physical acceptance, packaging, installation, and game observations
remain separate checks. Original owners and their allocated identities stay exact.
"""
from copy import deepcopy

from . import y_junction_layout as original
from .y_junction_variants import REVERSED, records_for, variant_of

PHYSICAL_LAYOUT_REVIEWED = True
PATH_CELLS = frozenset(original.PATH_CELLS)


def module_catalog():
    identities = {row['role']: row for row in records_for(REVERSED)}
    source = original.module_catalog()
    rows = []
    for previous in source['types']:
        row = deepcopy(previous)
        identity = identities[row['key']]
        row.update({key: identity[key] for key in ('id', 'recipe', 'geometry_key')})
        row['name'] += ' — Reversed Traffic'
        row['y_junction_variant'] = REVERSED
        row['function'] = row['function'].replace('lower-to-upper', 'upper-to-lower')
        row['function'] += '; all directed journeys and their driver-left markings are reversed'
        row['engineering']['physical_model_function'] = row['function']
        row['engineering']['native_phase'] = 'Opposite directed native phase, retaining the common axis intersection (8,0) m'
        row['engineering']['native_pavement_datums_m'] = [0., .0009999275207519531, .0010004043579101562]
        row['engineering'].pop('pavement_path_offset_m', None)
        row['engineering'].pop('native_peer_shoulder_body_depth_m', None)
        row['engineering']['surface_datum_policy'] = 'Nominal-height diagonal 57530200 collars and source-measured 57530000 pose 1 roofs; finite transitions retain exact source datums'
        row['engineering'].update({
            'native_helper_pavement_datums_by_arm_m': {
                'A': {'lower': 0., 'upper': 0.},
                'B': {'lower': 0., 'upper': 0.},
                'C': {'lower': .0009999275207519531, 'upper': .0010004043579101562}},
            'native_C_full_width_station_m': 3.00100040435791,
            'graded_top_plane_policy': 'Pavement and raised barrier tops share the actual unchanged full-width supporting body planes; measured barrier rise is retained',
            'graded_construction_station_frame': 'Original canonical physical route IDs and ascending construction order; reverse travel uses the opposite directed ID and length minus station',
            'graded_top_plan_boundary_crop_bound_m': 1e-9,
            'underside_owner_mask_input_grid_m': 1e-9,
            'native_C_owned_interface_analysis': {
                'source_model': '57530000', 'pose_quarter_turns_clockwise': 1,
                'outside_native_city_cell': [4, 0],
                'east_interval_m': [55.99899959564209, 56.],
                'north_interval_m': [-8., 8.],
                'reference_roles': ['pavement', 'barrier'],
                'body_reference_faces': 0, 'copied_into_custom_DAT': False,
                'authored_underside_required_through_owned_east_boundary': True},
            'native_C_source_only_south_fringe_bounds_enh_m': [
                [52.99899959564209, -8.00100040435791, 6.500999927520752],
                [55.99900007247925, -8., 15.002500534057617]],
        })
        row['engineering']['physical_layout_reviewed'] = PHYSICAL_LAYOUT_REVIEWED
        rows.append(row)
    return {'types': rows, 'occupied_cells': deepcopy(source['occupied_cells']), 'placement_count': 3,
            'physical_layout_reviewed': PHYSICAL_LAYOUT_REVIEWED}


def declaration(spec):
    if variant_of(spec) != REVERSED:
        raise ValueError('This layout owns only the explicit reversed Y variant')
    rows = [row for row in module_catalog()['types'] if row['id'] == spec['id']]
    if len(rows) != 1:
        raise ValueError('Unknown reversed Y owner')
    row = rows[0]
    if spec.get('cells') != row['cells'] or spec.get('footprint') != row['footprint']:
        raise ValueError('Reversed Y allocated cells disagree with its measured owner')
    return row
