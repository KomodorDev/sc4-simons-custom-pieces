"""Explicit reversed native phase of the shared finite-profile reader.

The bound functions pass an immutable variant argument through the engine.
They never mutate its original sockets, caches, or source measurements.
"""
from functools import wraps
from copy import deepcopy
import hashlib
import math
from pathlib import Path
import re
from types import MappingProxyType

from scp.dbpf import require
from . import y_junction_native_models as shared

SOCKETS = MappingProxyType({
    'A': MappingProxyType({'helper': (0x57530200, 0, (-2, 2)), 'peer': (0x57530900, 2, (-2, 3)),
        'plane_e': -24., 'core_sign': 1, 'inward_en': (math.sqrt(.5), math.sqrt(.5))}),
    'B': MappingProxyType({'helper': (0x57530200, 3, (-2, -2)), 'peer': (0x57530900, 1, (-2, -3)),
        'plane_e': -24., 'core_sign': 1, 'inward_en': (math.sqrt(.5), -math.sqrt(.5))}),
    'C': MappingProxyType({'helper': (0x57530000, 1, (4, 0)), 'peer': (0x57530000, 1, (5, 0)),
        'plane_e': 56., 'core_sign': -1, 'inward_en': (-1., 0.)}),
})

# Only this measured physical mask and these four pavement caps have an
# approved ownership-trace interpretation. Changing the mask needs review.
APPROVED_INTERFACE_CELLS = frozenset({
    (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (-1, 2), (0, 2), (-1, 3),
    (-1, -3), (-1, -2), (0, -2), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
    (-1, 0), (0, 0), (1, 0), (2, 0), (3, 0),
})

def _bind(function):
    @wraps(function)
    def bound(*args, **kwargs):
        require('variant' not in kwargs, 'A reversed native API cannot select another variant')
        return function(*args, **kwargs, variant='reversed')
    return bound


posed_native_faces = _bind(shared.posed_native_faces)
native_join_plane = _bind(shared.native_join_plane)
native_join_sections = _bind(shared.native_join_sections)
native_coreward_faces = _bind(shared.native_coreward_faces)
retained_core_contact_faces = _bind(shared.retained_core_contact_faces)
retained_core_collar_faces = _bind(shared.retained_core_collar_faces)
extrude_native_collars = _bind(shared.extrude_native_collars)
certify_native_model_faces = _bind(shared.certify_native_model_faces)
_certify_native_collars = _bind(shared.certify_native_collars)
barrier_profile = _bind(shared.barrier_profile)
native_end_sections = _bind(shared.native_end_sections)
native_forward_sections = _bind(shared.native_forward_sections)
visible_native_end_sections = _bind(shared.visible_native_end_sections)
native_join_audit = _bind(shared.native_join_audit)
reserved_native_cells = shared.reserved_native_cells
check_reserved_native_corridor = shared.check_reserved_native_corridor
_oblique_segments = shared._oblique_segments


def _buried_helper_body_regions(world_faces, roles, context, certified_indices, tolerance):
    """Fresh302-helper source containment; actual slab closure stays separate.

    Only previously source-certified helper302 body portions below the exact
    nominal floor qualify. The high millimetre strip remains exposed, and
    a separate saved-solid reader must still prove the real outer wall,
    complete slab, and absence of interference with every raw saved face.
    """
    from collections import defaultdict
    from shapely.geometry import MultiPoint, Polygon
    from shapely.ops import unary_union
    require(type(tolerance) in (float, int) and 0. < tolerance <= 4e-6,
            'Reversed helper-body containment requires its unchanged 4 micrometre bound')
    floor_parts, hashes = defaultdict(list), {}
    for arm in ('A', 'B'):
        inward = SOCKETS[arm]['inward_en']
        direction = (inward[0], 0., -inward[1])
        for deck in ('upper', 'lower'):
            nominal = 15. if deck == 'upper' else 7.5
            for group in native_forward_sections(context, arm, deck):
                if group['kind'] != 'helper' or group['role'] != 'pavement':
                    continue
                require(group['donor'] == '57530200' and group['pose'] == (0 if arm == 'A' else 3),
                        'Helper-body containment changes its exact 302 source pose')
                hashes[arm, deck] = group['source_sha256']
                for segment in group['segments']:
                    a, b = segment['points']
                    require(a[1] == nominal and b[1] == nominal,
                            'Helper-body containment requires the actual nominal 302 floor')
                    points = (a, b, tuple(b[i]+3.*direction[i] for i in range(3)),
                              tuple(a[i]+3.*direction[i] for i in range(3)))
                    polygon = Polygon([(p[0], -p[2]) for p in points])
                    if polygon.area > 1e-15:
                        floor_parts[arm, deck].append(polygon)
    footprints = {key: unary_union(parts) for key, parts in floor_parts.items()}
    result = []
    for index in certified_indices:
        face = world_faces[index]
        role = roles[round(face[0][5])]
        matched = re.fullmatch(r'body-native-([AB])-(upper|lower)-helper', role)
        if not matched:
            continue
        arm, deck = matched.groups()
        nominal = 15. if deck == 'upper' else 7.5
        polygon = []
        for first, last in zip(face, (*face[1:], face[0])):
            a, b = nominal-first[1], nominal-last[1]
            if a >= 0.:
                polygon.append(first)
            if (a >= 0.) != (b >= 0.):
                fraction = a/(a-b)
                polygon.append(tuple(first[i]+fraction*(last[i]-first[i]) for i in range(len(first))))
        if len(polygon) < 3:
            continue
        area = sum(math.sqrt(sum(v*v for v in shared._cross(
            tuple(polygon[k][i]-polygon[0][i] for i in range(3)),
            tuple(polygon[k+1][i]-polygon[0][i] for i in range(3)))))/2.
                   for k in range(1, len(polygon)-1))
        if area <= 1e-14:
            continue
        footprint = footprints[arm, deck]
        projection = MultiPoint([(p[0], -p[2]) for p in polygon]).convex_hull
        require(footprint.buffer(tolerance).covers(projection)
                and min(p[1] for p in polygon) >= nominal-1.-tolerance
                and max(p[1] for p in polygon) <= nominal,
                'Source-certified helper body escapes its finite nominal-floor-to-underside prism')
        result.append({'face_index': index, 'role': role, 'arm': arm, 'deck': deck,
            'source_model_sha256': hashes[arm, deck], 'source_native_tile_id': '57530200',
            'source_native_kind': 'helper',
            'source_native_pose': 0 if arm == 'A' else 3,
            'analysis_below_height_m': nominal, 'underside_height_m': nominal-1.,
            'source_extrusion_length_m': 3., 'source_pavement_plan_area_m2': footprint.area,
            'source_pavement_bounds_en_m': list(footprint.bounds),
            'finite_source_footprint_and_height_containment_proved': True,
            'source_body_surface_area_below_floor_m2': area,
            'requires_independent_complete_shell_and_outer_wall_proof': True,
            'requires_independent_actual_slab_containment_proof': True,
            'raised_native_strip_and_actual_saved_faces_changed': False,
            'generic_authored_phase_wall_covered': False})
    return result


def certify_native_collars(world_faces, roles, materials, context, position_tolerance_m=4e-6, uv_tolerance=5e-6):
    report = _certify_native_collars(world_faces, roles, materials, context, position_tolerance_m, uv_tolerance)
    report['buried_helper_body_regions'] = _buried_helper_body_regions(
        world_faces, roles, context, report['certified_face_indices'], position_tolerance_m)
    return report


def _owned_mask(owned_cells):
    from shapely.geometry import box
    from shapely.ops import unary_union
    cells = [tuple(cell) for cell in owned_cells]
    require(cells and len(cells) == len(set(cells))
            and all(len(cell) == 2 and all(type(value) is int for value in cell) for cell in cells)
            and frozenset(cells) == APPROVED_INTERFACE_CELLS,
            'Native interface ownership differs from the exact approved 21-cell mask')
    return unary_union([box(16*x-8., -16*y-8., 16*x+8., -16*y+8.) for x, y in cells])


def _line_parts(geometry):
    if geometry.geom_type == 'LineString':
        return [geometry] if geometry.length > 0. else []
    return [part for child in getattr(geometry, 'geoms', ()) for part in _line_parts(child)]


def owned_native_join_sections(context, arm, deck, owned_cells):
    """Clip exactly four approved peer309 roof caps to actual owned cells.

    All other full finite source interfaces remain unchanged. The omitted
    cap tails are outside the custom construction, within the unchanged
    native helper cells. This is ownership accounting, not occlusion, a
    numerical tolerance, or a car-floor or underside waiver.
    """
    from shapely.geometry import LineString, box
    owned = _owned_mask(owned_cells)
    groups = visible_native_end_sections(context, arm, deck)
    if arm == 'C':
        return groups
    result, clipped = [], 0
    for group in groups:
        if not (group['kind'] == 'peer' and group['donor'] == '57530900'
                and group['role'] == 'pavement'):
            result.append(group)
            continue
        # The pinned native phase has exactly one pavement cap per deck.
        require(len(group['segments']) == 1, 'Approved peer309 pavement cap changed its finite segmentation')
        segment = group['segments'][0]
        first, last = segment['points']
        line = LineString([(first[0], -first[2]), (last[0], -last[2])])
        inside, outside = line.intersection(owned), line.difference(owned)
        require(abs(line.length-2.343146625118034) <= 1e-10
                and abs(inside.length-2.3417325134463294) <= 1e-10
                and abs(outside.length-0.0014141116717046691) <= 1e-10,
                'Peer309 cap ownership is outside the four exactly measured source traces')
        helper_cell = SOCKETS[arm]['helper'][2]
        helper = box(16*helper_cell[0]-8., -16*helper_cell[1]-8.,
                     16*helper_cell[0]+8., -16*helper_cell[1]+8.)
        require(outside.intersection(owned).length == 0. and outside.difference(helper).length == 0.
                and all(x <= -24. for part in _line_parts(outside) for x, _n in part.coords),
                'Excluded native cap has a positive-length custom-owner interface')
        delta = (last[0]-first[0], -last[2]+first[2])
        denominator = sum(value*value for value in delta)
        def interpolate(east, north):
            fraction = ((east-first[0])*delta[0]+(north+first[2])*delta[1])/denominator
            require(0. <= fraction <= 1., 'Owned cap trace escaped its finite original parent edge')
            return tuple(first[i]+fraction*(last[i]-first[i]) for i in range(5))
        def records(geometry):
            return [{**deepcopy(segment), 'points': tuple(interpolate(*xy) for xy in (part.coords[0], part.coords[-1]))}
                    for part in _line_parts(geometry)]
        inside_segments, outside_segments = records(inside), records(outside)
        points = [point for row in outside_segments for point in row['points']]
        trace = {'arm': arm, 'deck': deck, 'native_owner': 'peer', 'native_tile_id': '57530900',
            'source_model_sha256': group['source_sha256'],
            'full_source_length_m': line.length, 'inside_owned_length_m': inside.length,
            'outside_owned_length_m': outside.length,
            'outside_native_helper_cell_col_row': list(helper_cell),
            'outside_bounds_east_height_south_m': [[min(p[k] for p in points) for k in range(3)],
                                                   [max(p[k] for p in points) for k in range(3)]],
            'raw_source_segments': deepcopy(group['segments']),
            'inside_owned_segments': inside_segments, 'outside_owned_segments': outside_segments,
            'positive_length_outside_intersection_with_custom_mask_m': outside.intersection(owned).length,
            'interpretation': 'Exact source cap outside custom ownership; not occlusion or a numerical or floor waiver'}
        result.append({**group, 'segments': inside_segments, 'source_interface_ownership_trace': trace})
        clipped += 1
    require(clipped == 1, 'Reversed diagonal deck lacks its single approved peer309 cap ownership trace')
    return result


def ownership_join_trace_report(context, owned_cells):
    owned = _owned_mask(owned_cells)
    traces = [group['source_interface_ownership_trace'] for arm in ('A', 'B')
              for deck in ('upper', 'lower') for group in owned_native_join_sections(context, arm, deck, owned_cells)
              if 'source_interface_ownership_trace' in group]
    require(len(traces) == 4, 'Owned native profile report must retain exactly four approved pavement caps')
    return {'schema_version': 1, 'review_scope': 'Four A/B peer309 pavement cap traces only',
        'owned_cells_col_row': [list(cell) for cell in sorted(APPROVED_INTERFACE_CELLS)],
        'owned_mask_bounds_en_m': list(owned.bounds),
        'intersection_method': 'Exact finite LineString intersection with the union of complete 16 m city-cell boxes; no epsilon buffer',
        'traces': traces, 'excluded_outside_length_m': sum(row['outside_owned_length_m'] for row in traces),
        'all_other_native_profiles_unchanged': True,
        'occlusion_floor_or_underside_waiver': False}


def _clip_axis(triangle, axis, boundary, sign):
    polygon = list(triangle)
    result = []
    for first, last in zip(polygon, (*polygon[1:], polygon[0])):
        a, b = sign*(first[axis]-boundary), sign*(last[axis]-boundary)
        if a >= 0.:
            result.append(first)
        if (a >= 0.) != (b >= 0.):
            fraction = a/(a-b)
            result.append(tuple(first[i]+fraction*(last[i]-first[i]) for i in range(5)))
    return [tuple((result[0], result[i], result[i+1])) for i in range(1, len(result)-1)]


def native_owned_interface_faces(context):
    """Source-only C contact already rendered by the unchanged outside NAM cell.

    These finite fragments may complete the physical analysis of the custom
    owner's E56 boundary. They must not be copied into its actual DAT, and
    they do not supply or waive any authored underside or car corridor.
    """
    result = []
    for group in posed_native_faces(context, 'C', False):
        fragments = []
        for face_index, parent in enumerate(group['triangles']):
            clipped = shared._clip_coreward(parent, 56., -1)
            for axis, boundary, sign in ((2, -8., 1), (2, 8., -1)):
                clipped = [part for triangle in clipped for part in _clip_axis(triangle, axis, boundary, sign)]
            fragments.extend({'face_index': face_index, 'parent_triangle': parent, 'triangle': triangle}
                             for triangle in clipped)
        if fragments:
            result.append({**{key: value for key, value in group.items() if key != 'triangles'},
                'fragments': fragments, 'reference_only_already_rendered_native': True,
                'copy_into_custom_DAT_permitted': False,
                'owned_analysis_bounds_en_m': [[55.99899959564209, -8.], [56., 8.]],
                'underside_or_car_corridor_waiver': False})
    return result


def native_profiles_report(context):
    """Decode pinned native profiles afresh; do not accept authored geometry."""
    from . import native
    from . import y_junction_approaches as approaches
    from . import y_junction_reversed_approaches as reversed_approaches
    flat = context if any(isinstance(key, tuple) for key in context) else {
        key: raw for group in context.values() for key, raw in group.items()}
    for key, digest in approaches.NATIVE_DEPENDENCY_SHA256.items():
        require(key in flat and hashlib.sha256(flat[key]).hexdigest() == digest,
                'Reversed native input dependency differs from its pinned original bytes')
    controller = {key: flat[key] for key in (*approaches.NATIVE_CONTROLLER_SHA256, approaches.RUL1)}
    continuation = reversed_approaches.check_native_continuation(controller)
    arms = []
    for arm, socket in SOCKETS.items():
        donor, pose, cell = socket['helper']
        routes = [native.rotate_route(route, pose) for route in approaches._native_routes(donor, flat)]
        edge = 0 if arm == 'C' else 2
        members = approaches._members(routes, cell, edge)
        interfaces, source_faces = [], []
        for deck in ('upper', 'lower'):
            for group in native_forward_sections(context, arm, deck):
                interfaces.append({**{key: group[key] for key in ('kind', 'donor', 'pose', 'cell',
                    'mesh_index', 'mesh_name', 'deck', 'role', 'source_sha256', 'plane_normal_xyz', 'plane_station_m')},
                    'material_sha256': hashlib.sha256(group['material']['raw']).hexdigest(),
                    'segments': group['segments']})
        for group in posed_native_faces(context, arm, arm != 'C'):
            points = [point for triangle in group['triangles'] for point in triangle]
            source_faces.append({**{key: group[key] for key in ('kind', 'donor', 'pose', 'cell',
                'mesh_index', 'mesh_name', 'deck', 'role', 'source_sha256')},
                'material_raw_hex': group['material']['raw'].hex(),
                'material_sha256': hashlib.sha256(group['material']['raw']).hexdigest(),
                'texture_ids': list(group['material']['textures']),
                'bounds_east_height_south_m': [[min(p[k] for p in points) for k in range(3)],
                                               [max(p[k] for p in points) for k in range(3)]],
                'indexed_triangles_xyzuv': group['triangles']})
        arms.append({'arm': arm, 'helper': [donor, pose, list(cell)],
            'peer': [socket['peer'][0], socket['peer'][1], list(socket['peer'][2])],
            'actual_helper_pavement_join_east_m': native_join_plane(context, arm),
            'nominal_path_join_east_m': socket['plane_e'],
            'members': [{'transport': key[0], 'lane': key[1], 'compatibility': key[2],
                'direction': 'core-to-native' if key[3] == 'in' else 'native-to-core',
                'point_enh_m': value['point'], 'travel_tangent_enh': value['tangent']}
                for key, value in sorted(members.items())],
            'finite_forward_interfaces': interfaces, 'posed_original_indexed_faces': source_faces})
    return {'schema_version': 1, 'variant': 'reversed', 'state': 'fresh-pinned-native-measurement',
        'generator': 'scp_highway.y_junction_reversed_native_models.native_profiles_report',
        'source_module_sha256': {
            'y_junction_reversed_native_models.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'y_junction_native_models.py': hashlib.sha256(Path(shared.__file__).read_bytes()).hexdigest(),
            'y_junction_reversed_approaches.py': hashlib.sha256(Path(reversed_approaches.__file__).read_bytes()).hexdigest(),
            'y_junction_approaches.py': hashlib.sha256(Path(approaches.__file__).read_bytes()).hexdigest()},
        'scope': 'Actual native helper and peer PATHs, indexed source triangles, finite forward interfaces, material bytes, UVs, and unchanged continuation templates; no authored source or saved-model acceptance.',
        'model_vertex_coordinates': 'east, height, south, U, V; metres for the first three coordinates',
        'path_coordinates': 'east, north, height in metres',
        'native_model_and_path_sha256': [{'tgi': '-'.join(f'{v:08x}' for v in key), 'sha256': digest}
            for key, digest in sorted(approaches.NATIVE_DEPENDENCY_SHA256.items())],
        'native_controller_resource_sha256': [{'tgi': '-'.join(f'{v:08x}' for v in key),
            'sha256': hashlib.sha256(controller[key]).hexdigest()} for key in sorted(controller)],
        'arms': arms, 'native_continuation': continuation,
        'approved_source_interface_ownership': ownership_join_trace_report(context, APPROVED_INTERFACE_CELLS),
        'diagonal_rul1_declarations': {'section': approaches.SECTION,
            'rows': [[approaches._rotate_flags(0x04000100, turn), approaches._rotate_flags(0x03010000, turn),
                      0x57530200, turn, 0] for turn in range(4)],
            'original_diagonal_marker_base': '01000400', 'reversed_diagonal_marker_base': '04000100',
            'original_and_reversed_key_pairs_overlap': False,
            'declaration_scope': 'Four reversed marker solutions; the complete installed selection may already supply them.'},
        'native_continuation_templates': approaches._continuation_templates(),
        'skin_exception_scope': 'No original peer302 buried-body authorization transfers to the reversed phase. The distinct helper302 source containment below nominal15/7.5 requires actual saved slab and real outer-wall proof; raised strips and all raw faces stay unchanged.',
        'helper_body_analysis_contract': {'source_tile_id': '57530200', 'source_helper_poses': {'A': 0, 'B': 3},
            'below_nominal_floor_m': {'upper': 15., 'lower': 7.5},
            'actual_authored_underside_m': {'upper': 14., 'lower': 6.5},
            'source_forward_length_m': 3., 'source_position_bound_m': 4e-6,
            'requires_independent_actual_slab_and_outer_wall_proof': True,
            'generic_phase_walls_or_above_nominal_body_covered': False},
        'game_operation_tested': False}
