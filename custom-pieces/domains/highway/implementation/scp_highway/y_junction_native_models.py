"""Exact finite native geometry surrounding the first Y junction's sockets.

The diagonal native staircase supplies only part of its physical shoulder
from each PATH owner. These helpers retain indexed faces, actual model
datums, independent material UVs, and the outward peer's overhang. They do
not turn a native half into an infinite rectangular road cross-section.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import math
import struct

from scp.dbpf import require
from scp.models import parse_s3d
from scp.track_paths import S3D
from .native import rotate_model
from .y_junction_approaches import NATIVE_DEPENDENCY_SHA256

# World source cells: east columns and south rows. Poses are proper clockwise
# quarter-turns, identical to the PATH and native-helper contracts.
SOCKETS = {
    'A': {'helper': (0x57530900, 0, (-2, 2)), 'peer': (0x57530200, 2, (-2, 3)), 'plane_e': -24., 'core_sign': 1, 'inward_en': (math.sqrt(.5), math.sqrt(.5))},
    'B': {'helper': (0x57530900, 3, (-2, -2)), 'peer': (0x57530200, 1, (-2, -3)), 'plane_e': -24., 'core_sign': 1, 'inward_en': (math.sqrt(.5), -math.sqrt(.5))},
    'C': {'helper': (0x57530000, 3, (4, 0)), 'peer': (0x57530000, 3, (5, 0)), 'plane_e': 56., 'core_sign': -1, 'inward_en': (-1., 0.)},
}


def _variant_sockets(variant):
    """Select one explicit finite native phase without changing globals."""
    require(type(variant) is str and variant in ('original', 'reversed'),
            'Unknown native Y physical variant')
    if variant == 'original':
        return SOCKETS
    from .y_junction_reversed_native_models import SOCKETS as reversed_sockets
    return reversed_sockets


def _core_maximum_east(context, variant):
    if variant == 'original':
        return 56.00100040435791
    return max(point[0]-16. for group in posed_native_faces(context, 'C', False, variant=variant)
               for triangle in group['triangles'] for point in triangle)


def _mesh_role(name):
    return {'Top Deck': 'pavement', 'Bottom Deck': 'pavement',
            'Substructure': 'body', 'Barriers': 'barrier'}[name]


def posed_native_faces(context, arm, include_outward_peer=True, *, variant='original'):
    """Return measured indexed XYZUV triangles, grouped by original mesh.

    World XYZ means east, height, and south. Every output retains its
    original face index, native cell, pose, material bytes, and model hash.
    An outward peer is a native traffic owner, never a custom shoulder owner.
    """
    sockets = _variant_sockets(variant)
    require(arm in sockets, 'Unknown Y native socket arm')
    if 'dd_rhw' not in context and any(isinstance(key, tuple) for key in context):
        context = {'dd_rhw': context}
    result = []
    kinds = ('helper', 'peer') if include_outward_peer else ('helper',)
    for kind in kinds:
        donor, pose, cell = sockets[arm][kind]
        key = (*S3D, donor)
        require(key in context.get('dd_rhw', {})
                and hashlib.sha256(context['dd_rhw'][key]).hexdigest() == NATIVE_DEPENDENCY_SHA256[key],
                'Y native physical donor identity changed')
        model = rotate_model(parse_s3d(context['dd_rhw'][key]), pose)
        for mesh_index, mesh in enumerate(model['meshes']):
            name = mesh['name'].rstrip(b'\0').decode('ascii')
            vi, ii, _pi, mi = mesh['frames'][0]
            buffer = model['vertices'][vi]
            require(buffer['stride'] >= 20, 'Native Y profile omits position or UV')
            vertices = [struct.unpack_from('<5f', buffer['data'], offset)
                        for offset in range(0, len(buffer['data']), buffer['stride'])]
            vertices = [(p[0] + 16 * cell[0], p[1], p[2] + 16 * cell[1], p[3], p[4]) for p in vertices]
            indices = model['indices'][ii]['values']
            require(len(indices) % 3 == 0, 'Native Y indexed face list is not triangular')
            triangles = [tuple(vertices[index] for index in indices[i:i + 3]) for i in range(0, len(indices), 3)]
            # Names repeat once per deck; actual height distinguishes them.
            deck = 'upper' if min(p[1] for p in vertices) > 10. else 'lower'
            result.append({'arm': arm, 'kind': kind, 'donor': f'{donor:08x}', 'pose': pose,
                           'cell': list(cell), 'mesh_index': mesh_index, 'mesh_name': name,
                           'deck': deck, 'role': _mesh_role(name), 'triangles': triangles,
                           'material': deepcopy(model['materials'][mi]),
                           'source_sha256': NATIVE_DEPENDENCY_SHA256[key]})
    return result


def _plane_segments(triangle, east, tolerance=1e-10):
    """Intersect one finite triangle with an east-coordinate plane."""
    on_plane = [abs(p[0] - east) <= tolerance for p in triangle]
    if all(on_plane):
        return [(triangle[i], triangle[(i + 1) % 3]) for i in range(3)]
    points = []
    for first, last in zip(triangle, (*triangle[1:], triangle[0])):
        a, b = first[0] - east, last[0] - east
        a = 0. if abs(a) <= tolerance else a
        b = 0. if abs(b) <= tolerance else b
        if a == 0.:
            points.append(first)
        if a * b < 0:
            t = -a / (b - a)
            require(0. <= t <= 1., 'Native profile plane intersection escaped its original edge')
            points.append(tuple(first[i] + t * (last[i] - first[i]) for i in range(len(first))))
    unique = []
    for point in points:
        if not any(math.dist(point[:3], value[:3]) <= tolerance for value in unique):
            unique.append(point)
    if len(unique) < 2:
        return []
    require(len(unique) == 2, 'Native finite section has an ambiguous triangle intersection')
    return [(unique[0], unique[1])]


def native_join_plane(context, arm, *, variant='original'):
    """Use the physical native end, retaining its measured millimetre phase."""
    sockets = _variant_sockets(variant)
    pavement = [point[0] for group in posed_native_faces(context, arm, False, variant=variant)
                if group['role'] == 'pavement' for triangle in group['triangles'] for point in triangle]
    return max(pavement) if sockets[arm]['core_sign'] == 1 else min(pavement)


def native_join_sections(context, arm, deck, include_outward_peer=True, plane_e=None, *, variant='original'):
    """Finite XYZUV section segments at the actual selected city-edge plane.

    Segments retain separate UVs where a native barrier intentionally has
    duplicated crest vertices. They therefore must not be collapsed into a
    single UV value for each physical cross-section vertex.
    """
    require(deck in ('upper', 'lower'), 'Unknown Y native deck')
    east = native_join_plane(context, arm, variant=variant) if plane_e is None else float(plane_e)
    records = []
    for group in posed_native_faces(context, arm, include_outward_peer, variant=variant):
        if group['deck'] != deck:
            continue
        segments = []
        for face_index, triangle in enumerate(group['triangles']):
            segments.extend({'face_index': face_index, 'points': segment}
                            for segment in _plane_segments(triangle, east)
                            if math.dist(*[point[:3] for point in segment]) > 1e-10)
        if segments:
            records.append({**{key: group[key] for key in ('arm', 'kind', 'donor', 'pose', 'cell',
                              'mesh_index', 'mesh_name', 'deck', 'role', 'material', 'source_sha256')},
                            'plane_e_m': east, 'segments': segments})
    return records


def _clip_coreward(triangle, plane, sign):
    polygon = list(triangle)
    output = []
    for first, last in zip(polygon, (*polygon[1:], polygon[0])):
        a, b = sign * (first[0] - plane), sign * (last[0] - plane)
        inside_a, inside_b = a >= 0., b >= 0.
        if inside_a:
            output.append(first)
        if inside_a != inside_b:
            t = a / (a - b)
            output.append(tuple(first[i] + t * (last[i] - first[i]) for i in range(len(first))))
    return [tuple((output[0], output[i], output[i + 1])) for i in range(1, len(output) - 1)]


def native_coreward_faces(context, arm, deck=None, *, variant='original'):
    """Original native fragments extending across the nominal custom boundary.

    These faces are already rendered by their unchanged native owners. Use
    their physical projection to exclude authored overlap; copying them into
    the custom model would produce duplicate visible geometry.
    """
    sockets = _variant_sockets(variant)
    socket = sockets[arm]
    result = []
    for group in posed_native_faces(context, arm, variant=variant):
        if deck is not None and group['deck'] != deck:
            continue
        fragments = []
        for face_index, triangle in enumerate(group['triangles']):
            fragments.extend({'face_index': face_index, 'triangle': fragment}
                             for fragment in _clip_coreward(triangle, socket['plane_e'], socket['core_sign']))
        if fragments:
            result.append({**{key: value for key, value in group.items() if key != 'triangles'}, 'fragments': fragments})
    return result


def retained_core_contact_faces(context, arm='C', *, variant='original'):
    """Literal original core DD faces in the measured C contact sliver.

    Only the selected donor-300 phase at world cell (3,0) is admitted. Each output
    fragment stays on its indexed parent face and retains its affine UVs.
    This is not permission for arbitrary authored geometry beyond east 56 m.
    """
    require(arm == 'C', 'Only the measured C native core contact is reviewed')
    result = []
    for group in posed_native_faces(context, 'C', False, variant=variant):
        fragments = []
        for face_index, triangle in enumerate(group['triangles']):
            original = tuple((point[0] - 16., *point[1:]) for point in triangle)
            for fragment in _clip_coreward(original, 56., 1):
                fragments.append({'face_index': face_index, 'parent_triangle': original, 'triangle': fragment})
        if fragments:
            result.append({**{key: value for key, value in group.items() if key != 'triangles'},
                           'kind': 'retained-core-contact', 'cell': [3, 0], 'fragments': fragments,
                           'bounded_east_interval_m': [56., _core_maximum_east(context, variant)]})
    return result


def retained_core_collar_faces(context, arm='C', length_m=3., *, variant='original'):
    """Literal core-300 collar, retaining only original parent-face geometry.

    The complete strip belongs to the selected literal model at core (3,0).
    Hosting its measured north and east millimetre edges there requires no
    extra shoulder PATH owner and permits no authored extrapolation beyond
    the source faces. The original longitudinal texture phase is preserved.
    """
    require(arm == 'C' and type(length_m) in (int, float) and length_m == 3.,
            'Only the reviewed three-metre C native core collar is admitted')
    minimum_east = native_join_plane(context, 'C', variant=variant) - 3.
    result = []
    for group in posed_native_faces(context, 'C', False, variant=variant):
        fragments = []
        for face_index, triangle in enumerate(group['triangles']):
            original = tuple((point[0]-16., *point[1:]) for point in triangle)
            fragments.extend({'face_index': face_index, 'parent_triangle': original, 'triangle': fragment}
                             for fragment in _clip_coreward(original, minimum_east, 1))
        if fragments:
            result.append({**{key: value for key, value in group.items() if key != 'triangles'},
                           'kind': 'retained-core-collar', 'cell': [3, 0], 'fragments': fragments,
                           'bounded_east_interval_m': [minimum_east, _core_maximum_east(context, variant)],
                           'native_longitudinal_texture_phase': 'Original core donor phase; one native repeat relative to the outside neighbour'})
    return result


def _uv_derivative(triangle, direction):
    first, second, third = triangle
    a = tuple(second[i] - first[i] for i in range(3))
    b = tuple(third[i] - first[i] for i in range(3))
    aa, ab, bb = sum(x*x for x in a), sum(a[i]*b[i] for i in range(3)), sum(x*x for x in b)
    determinant = aa*bb-ab*ab
    require(determinant > 1e-20, 'Native collar UV derivative has a degenerate parent face')
    da, db = sum(direction[i]*a[i] for i in range(3)), sum(direction[i]*b[i] for i in range(3))
    alpha, beta = (da*bb-db*ab)/determinant, (db*aa-da*ab)/determinant
    projected = tuple(alpha*a[i]+beta*b[i] for i in range(3))
    require(math.dist(projected, direction) < 3e-6, 'Native collar direction leaves its actual source face plane')
    return tuple(alpha*(second[i]-first[i])+beta*(third[i]-first[i]) for i in (3, 4))


def extrude_native_collars(context, length_m=3., arms=None, *, variant='original'):
    """Loft every exposed finite forward profile along its native direction.

    The output preserves each source face's longitudinal affine UV derivative
    and exact height. Returned projected overlaps are explicit unresolved
    partition inputs; they are not silently accepted as duplicate pavement.
    """
    sockets = _variant_sockets(variant)
    from collections import Counter
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    require(type(length_m) in (int, float) and math.isfinite(length_m) and length_m > 0,
            'Native collar length must be positive and finite')
    selected = tuple(sockets) if arms is None else tuple(arms)
    require(selected and len(set(selected)) == len(selected) and set(selected) <= sockets.keys(),
            'Native collar extrusion requires unique reviewed arms')
    output, roofs, end_profiles = [], [], []
    for arm in selected:
        inward = sockets[arm]['inward_en']
        direction = (inward[0], 0., -inward[1])
        for deck in ('upper', 'lower'):
            profiles = native_end_sections(context, arm, deck, variant=variant)
            end_profiles.extend(profiles)
            first_station = min(group['plane_station_m'] for group in profiles if group['role'] == 'pavement')
            for group in posed_native_faces(context, arm, arm != 'C', variant=variant):
                if group['deck'] != deck:
                    continue
                boundary = Counter()
                for triangle in group['triangles']:
                    for a, b in zip(triangle, (*triangle[1:], triangle[0])):
                        boundary[tuple(sorted((a[:3], b[:3])))] += 1
                extruded, parent_records = [], []
                for face_index, triangle in enumerate(group['triangles']):
                    for a, b in zip(triangle, (*triangle[1:], triangle[0])):
                        if boundary[tuple(sorted((a[:3], b[:3])))] != 1:
                            continue
                        stations = [sum(point[i]*direction[i] for i in range(3)) for point in (a, b)]
                        if min(stations) < first_station - 2e-6:
                            continue
                        edge = tuple(b[i]-a[i] for i in range(3))
                        cross = (edge[1]*direction[2]-edge[2]*direction[1],
                                 edge[2]*direction[0]-edge[0]*direction[2],
                                 edge[0]*direction[1]-edge[1]*direction[0])
                        if sum(value*value for value in cross) < 1e-16:
                            continue
                        derivative = _uv_derivative(triangle, direction)
                        shifted = [tuple(point[i]+length_m*direction[i] for i in range(3))
                                   + tuple(point[i+3]+length_m*derivative[i] for i in range(2)) for point in (a, b)]
                        quad = (a, b, shifted[1], shifted[0])
                        normal = _cross(tuple(triangle[1][i]-triangle[0][i] for i in range(3)),
                                        tuple(triangle[2][i]-triangle[0][i] for i in range(3)))
                        candidate_normal = _cross(tuple(quad[1][i]-quad[0][i] for i in range(3)),
                                                  tuple(quad[2][i]-quad[0][i] for i in range(3)))
                        faces = [(quad[0], quad[1], quad[2]), (quad[0], quad[2], quad[3])]
                        if sum(normal[i]*candidate_normal[i] for i in range(3)) < 0:
                            faces = [(face[0], face[2], face[1]) for face in faces]
                        extruded.extend(faces)
                        parent_records.append({'face_index': face_index, 'source_edge': (a, b),
                                               'uv_derivative_per_m': derivative})
                if not extruded:
                    continue
                record = {**{key: value for key, value in group.items() if key != 'triangles'},
                          'triangles': extruded, 'parent_edges': parent_records, 'extrusion_length_m': float(length_m)}
                output.append(record)
                if group['role'] == 'pavement':
                    polygons = [Polygon([(p[0], -p[2]) for p in face]) for face in extruded]
                    geometry = unary_union([polygon for polygon in polygons if polygon.area > 1e-15])
                    roofs.append({'arm': arm, 'deck': deck, 'kind': group['kind'], 'geometry': geometry,
                                  'height_m': extruded[0][0][1], 'material': group['material']})
    overlaps = []
    for index, first in enumerate(roofs):
        for last in roofs[index+1:]:
            if (first['arm'], first['deck']) != (last['arm'], last['deck']):
                continue
            intersection = first['geometry'].intersection(last['geometry'])
            if intersection.area > 1e-12:
                overlaps.append({'arm': first['arm'], 'deck': first['deck'],
                                 'first_kind': first['kind'], 'second_kind': last['kind'],
                                 'area_m2': intersection.area, 'geometry': intersection,
                                 'height_difference_m': abs(first['height_m']-last['height_m'])})
    return {'groups': output, 'pavement_polygons': roofs, 'end_profiles': end_profiles,
            'projected_overlaps_requiring_partition': overlaps,
            'scope': 'Exact native boundary-edge lofts; caller must partition measured phase overlaps and close authored solids'}


def _cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def certify_native_model_faces(world_faces, roles, materials, context, position_tolerance_m=4e-6, uv_tolerance=5e-6, *, variant='original'):
    """Certify decoded native-role faces against measured source envelopes.

    This reader does not call the collar writer. It solves each decoded
    vertex directly in a finite source-edge/direction coordinate system.
    Literal C contacts are checked on their original posed parent triangles.
    Generic authored pavement merely using a native texture gets no native
    geometry exception. Returned exact barrier projections let a separate
    external-hull check remove only certified pavement under native barriers.
    """
    sockets = _variant_sockets(variant)
    from collections import defaultdict
    from shapely.geometry import Polygon, box
    from shapely.ops import unary_union
    references = defaultdict(list)
    barrier_masks = defaultdict(list)
    for arm in sockets:
        inward = sockets[arm]['inward_en']
        direction = (inward[0], 0., -inward[1])
        for deck in ('upper', 'lower'):
            for source in native_forward_sections(context, arm, deck, variant=variant):
                for segment in source['segments']:
                    a, b = segment['points']
                    derivative = _uv_derivative(segment['parent_triangle'], direction)
                    span = tuple(b[i]-a[i] for i in range(3))
                    ref = {'origin': a, 'first_axis': span, 'second_axis': direction,
                           'first_limit': 1., 'second_limit': 3., 'uv_first': tuple(b[i]-a[i] for i in (3, 4)),
                           'uv_second': derivative, 'parent_triangle': segment['parent_triangle'],
                           'source_sha256': source['source_sha256'], 'kind': source['kind']}
                    key = (source['role'], arm, deck, source['kind'])
                    references[key].append((ref, source['material']['raw']))
                    if source['role'] == 'barrier':
                        ends = [a, b, tuple(b[i]+3.*direction[i] for i in range(3)),
                                tuple(a[i]+3.*direction[i] for i in range(3))]
                        polygon = Polygon([(p[0], -p[2]) for p in ends])
                        if polygon.area > 1e-15:
                            barrier_masks[arm, deck, source['kind']].append(polygon)
    # C's extra contact is admitted only on complete original source faces,
    # translated into the literal core (3,0), with exact source UVs.
    core_collar_minimum = native_join_plane(context, 'C', variant=variant) - 3.
    core_maximum_east = _core_maximum_east(context, variant)
    for source in posed_native_faces(context, 'C', False, variant=variant):
        for triangle in source['triangles']:
            triangle = tuple((p[0]-16., *p[1:]) for p in triangle)
            a, b, c = triangle
            for kind, minimum_east in (('retained-contact', 56.),
                                       ('retained-core-collar', core_collar_minimum)):
                ref = {'origin': a, 'first_axis': tuple(b[i]-a[i] for i in range(3)),
                       'second_axis': tuple(c[i]-a[i] for i in range(3)),
                       'first_limit': 1., 'second_limit': 1.,
                       'uv_first': tuple(b[i]-a[i] for i in (3, 4)),
                       'uv_second': tuple(c[i]-a[i] for i in (3, 4)),
                       'parent_triangle': triangle, 'source_sha256': source['source_sha256'],
                       'kind': kind, 'minimum_east_m': minimum_east}
                references[source['role'], 'C', source['deck'], kind].append((ref, source['material']['raw']))
                if source['role'] == 'barrier':
                    polygon = Polygon([(p[0], -p[2]) for p in triangle]).intersection(box(minimum_east, -100., core_maximum_east, 100.))
                    if polygon.area > 1e-15:
                        barrier_masks['C', source['deck'], kind].append(polygon)
    certified, generic_native_texture, counts, sources = [], [], defaultdict(int), set()
    import re
    pattern = re.compile(r'^(pavement|body|barrier)-native-([ABC])-(upper|lower)-(helper|peer|retained-contact|retained-core-collar)$')
    for face_index, face in enumerate(world_faces):
        codes = {round(p[5]) for p in face}
        require(len(codes) == 1, 'Decoded native face mixes material roles')
        role = roles[codes.pop()]
        matched = pattern.fullmatch(role)
        if not matched:
            if '-native-' in role:
                generic_native_texture.append(face_index)
            continue
        key = matched.groups()
        actual_normal = _cross(tuple(face[1][i]-face[0][i] for i in range(3)),
                               tuple(face[2][i]-face[0][i] for i in range(3)))
        accepted = False
        for reference, material in references[key]:
            if materials[role]['raw'] != material:
                continue
            a, b = reference['first_axis'], reference['second_axis']
            aa, ab, bb = sum(x*x for x in a), sum(a[i]*b[i] for i in range(3)), sum(x*x for x in b)
            determinant = aa*bb-ab*ab
            if determinant <= 1e-20:
                continue
            original = reference['parent_triangle']
            source_normal = _cross(tuple(original[1][i]-original[0][i] for i in range(3)),
                                   tuple(original[2][i]-original[0][i] for i in range(3)))
            if sum(source_normal[i]*actual_normal[i] for i in range(3)) <= 0.:
                continue
            valid = True
            for point in face:
                delta = tuple(point[i]-reference['origin'][i] for i in range(3))
                da, db = sum(delta[i]*a[i] for i in range(3)), sum(delta[i]*b[i] for i in range(3))
                first, second = (da*bb-db*ab)/determinant, (db*aa-da*ab)/determinant
                projection = tuple(first*a[i]+second*b[i] for i in range(3))
                if math.dist(delta, projection) > position_tolerance_m:
                    valid = False
                    break
                # Convert the physical bound to each independent coordinate;
                # no millimetre-level phase allowance is introduced here.
                first_slack = position_tolerance_m*math.sqrt(bb/determinant)
                second_slack = position_tolerance_m*math.sqrt(aa/determinant)
                if not (-first_slack <= first <= reference['first_limit']+first_slack
                        and -second_slack <= second <= reference['second_limit']+second_slack):
                    valid = False
                    break
                if key[3] in ('retained-contact', 'retained-core-collar') and (first+second > 1.+first_slack+second_slack
                        or not reference['minimum_east_m']-position_tolerance_m <= point[0] <= core_maximum_east+position_tolerance_m):
                    valid = False
                    break
                expected_uv = [reference['origin'][i+3]+first*reference['uv_first'][i]
                               +second*reference['uv_second'][i] for i in range(2)]
                if max(abs(point[i+3]-expected_uv[i]) for i in range(2)) > uv_tolerance:
                    valid = False
                    break
            if valid:
                accepted = True
                sources.add(reference['source_sha256'])
                break
        require(accepted, f'Decoded {role} face escapes its pinned finite native geometry, winding, material, or UV envelope')
        certified.append(face_index)
        counts[key] += 1
    masks = {key: unary_union(polygons) for key, polygons in barrier_masks.items()}
    return {'native_faces_checked': len(certified), 'certified_face_indices': certified,
            'generic_native_texture_face_indices_without_geometry_exception': generic_native_texture,
            'counts_by_source': [{'role': key[0], 'arm': key[1], 'deck': key[2], 'kind': key[3], 'faces': value}
                                 for key, value in sorted(counts.items())],
            'barrier_base_masks': masks, 'source_model_sha256': sorted(sources),
            'position_tolerance_m': position_tolerance_m, 'uv_tolerance': uv_tolerance,
            'scope': 'Decoded faces contained on actual pinned finite source-profile lofts or literal C parent faces; no authored geometry exception'}


def _buried_peer_body_regions(world_faces, roles, context, certified_indices, position_tolerance_m, *, variant='original'):
    """Bound the approved 302 wall portions inside the peer floor prisms.

    The actual native body is about 1.415 mm inside its actual pavement's
    outer edge. Once an authored wall closes that pavement edge, the lower
    native wall is internal. This source-only certificate does not prove
    that the authored wall exists: the independent complete-shell check
    must still reject a missing outer wall. The raised native millimetre
    above the nominal peer floor is never part of these regions.
    """
    sockets = _variant_sockets(variant)
    if variant != 'original':
        # The original permission names peer302 and its reviewed body
        # phase. Reverse helper302/peer309 requires separate proof.
        return []
    from collections import defaultdict
    import re
    from shapely.geometry import MultiPoint, Polygon
    from shapely.ops import unary_union

    floor_parts = defaultdict(list)
    lower_bounds = {}
    source_hashes = {}
    for arm in ('A', 'B'):
        inward = sockets[arm]['inward_en']
        direction = (inward[0], 0., -inward[1])
        for deck in ('upper', 'lower'):
            nominal = 15. if deck == 'upper' else 7.5
            helper = [group for group in posed_native_faces(context, arm, False, variant=variant)
                      if group['role'] == 'pavement' and group['deck'] == deck]
            require(len(helper) == 1, 'Peer body burial requires one pinned helper floor datum')
            heights = {p[1] for triangle in helper[0]['triangles'] for p in triangle}
            require(len(heights) == 1, 'Peer body burial requires the literal flat helper floor')
            lower_bounds[arm, deck] = heights.pop() - 1.
            for group in native_forward_sections(context, arm, deck, variant=variant):
                if group['kind'] != 'peer' or group['role'] != 'pavement':
                    continue
                source_hashes[arm, deck] = group['source_sha256']
                for segment in group['segments']:
                    a, b = segment['points']
                    require(a[1] == nominal and b[1] == nominal,
                            'Peer body burial floor differs from its pinned nominal height')
                    points = (a, b, tuple(b[i] + 3. * direction[i] for i in range(3)),
                              tuple(a[i] + 3. * direction[i] for i in range(3)))
                    polygon = Polygon([(p[0], -p[2]) for p in points])
                    if polygon.area > 1e-15:
                        floor_parts[arm, deck].append(polygon)
    footprints = {key: unary_union(parts) for key, parts in floor_parts.items()}
    result = []
    for index in certified_indices:
        face = world_faces[index]
        role = roles[round(face[0][5])]
        matched = re.fullmatch(r'body-native-([AB])-(upper|lower)-peer', role)
        if not matched:
            continue
        arm, deck = matched.groups()
        nominal = 15. if deck == 'upper' else 7.5
        polygon = []
        for first, last in zip(face, (*face[1:], face[0])):
            a, b = nominal - first[1], nominal - last[1]
            if a >= 0.:
                polygon.append(first)
            if (a >= 0.) != (b >= 0.):
                fraction = a / (a - b)
                polygon.append(tuple(first[i] + fraction * (last[i] - first[i])
                                     for i in range(len(first))))
        if len(polygon) < 3:
            continue
        area = sum(math.sqrt(sum(value * value for value in _cross(
            tuple(polygon[k][i] - polygon[0][i] for i in range(3)),
            tuple(polygon[k + 1][i] - polygon[0][i] for i in range(3))))) / 2.
                   for k in range(1, len(polygon) - 1))
        if area <= 1e-14:
            continue
        footprint = footprints[arm, deck]
        projection = MultiPoint([(p[0], -p[2]) for p in polygon]).convex_hull
        require(footprint.buffer(position_tolerance_m).covers(projection),
                'Certified peer body below the floor escapes the finite original pavement footprint')
        bottom = lower_bounds[arm, deck]
        require(min(p[1] for p in polygon) >= bottom - position_tolerance_m
                and max(p[1] for p in polygon) <= nominal,
                'Certified peer body escapes the finite authorized floor-to-underside prism')
        result.append({'face_index': index, 'role': role, 'arm': arm, 'deck': deck,
                       'source_model_sha256': source_hashes[arm, deck],
                       'analysis_below_height_m': nominal, 'underside_height_m': bottom,
                       'source_extrusion_length_m': 3.,
                       'source_pavement_plan_area_m2': footprint.area,
                       'source_pavement_bounds_en_m': list(footprint.bounds),
                       'finite_source_footprint_and_height_containment_proved': True,
                       'source_body_surface_area_below_floor_m2': area,
                       'requires_independent_complete_shell_and_outer_wall_proof': True,
                       'raised_native_strip_and_actual_saved_faces_changed': False})
    return result


def certify_native_collars(world_faces, roles, materials, context, position_tolerance_m=4e-6, uv_tolerance=5e-6, *, variant='original'):
    """Reader certificate plus exact source masks for the external-skin check."""
    report = certify_native_model_faces(world_faces, roles, materials, context, position_tolerance_m, uv_tolerance, variant=variant)
    actual_pavement_roles = {f"pavement-native-{row['arm']}-{row['deck']}-{row['kind']}"
                            for row in report['counts_by_source'] if row['role'] == 'pavement'}
    report['internal_pavement_masks'] = {f'pavement-native-{arm}-{deck}-{kind}': geometry
                                         for (arm, deck, kind), geometry in report['barrier_base_masks'].items()
                                         if f'pavement-native-{arm}-{deck}-{kind}' in actual_pavement_roles}
    report['buried_peer_body_regions'] = _buried_peer_body_regions(
        world_faces, roles, context, report['certified_face_indices'], position_tolerance_m, variant=variant)
    return report


def reserved_native_cells(steps=16):
    """Draw a bounded prefix of the three infinite native continuation runs."""
    require(type(steps) is int and steps > 0, 'Native continuation prefix must be a positive integer')
    return {'A': sorted({(-2 - i, 2 + i) for i in range(steps)} | {(-2 - i, 3 + i) for i in range(steps)}),
            'B': sorted({(-2 - i, -2 - i) for i in range(steps)} | {(-2 - i, -3 - i) for i in range(steps)}),
            'C': [(4 + i, 0) for i in range(steps)]}


def check_reserved_native_corridor(owned_cells):
    """Reject custom PATH ownership anywhere on any complete outward run."""
    cells = {tuple(cell) for cell in owned_cells}
    require(all(len(cell) == 2 and all(type(value) is int for value in cell) for cell in cells),
            'Native corridor audit requires integer world city cells')
    conflicts = []
    for column, row in sorted(cells):
        if column <= -2 and row in (-column, 1 - column):
            conflicts.append(('A', [column, row]))
        if column <= -2 and row in (column, column - 1):
            conflicts.append(('B', [column, row]))
        if column >= 4 and row == 0:
            conflicts.append(('C', [column, row]))
    require(not conflicts, 'Custom Y ownership blocks a native outward continuation: ' + repr(conflicts))
    return {'custom_world_cells_checked': len(cells), 'native_outward_runs_checked': 3,
            'native_run_extent': 'unbounded analytic staircase and orthogonal rows',
            'owned_native_cells': [], 'in_game_dragging_tested': False}


def barrier_profile(context, arm, deck, side=None, *, variant='original'):
    """Return exact finite barrier panels and section UVs, including absence.

    ``side`` filters signed north relative to the socket axis point. An empty
    helper section is meaningful: native 309's one finite barrier does not
    reach its east PATH boundary; the outward peer owns the other segment.
    """
    require(side in (None, -1, 1), 'Native barrier side must be -1, +1, or absent')
    centre_n = {'A': -32., 'B': 32., 'C': 0.}[arm]
    records = []
    for group in native_end_sections(context, arm, deck, variant=variant):
        if group['role'] != 'barrier':
            continue
        segments = [segment for segment in group['segments'] if side is None or
                    side * (sum(-p[2] for p in segment['points']) / 2 - centre_n) >= 0]
        if segments:
            records.append({**group, 'segments': segments})
    return records


def native_end_sections(context, arm, deck, *, variant='original'):
    """Exact finite coreward end rings of each contributing native half.

    A diagonal helper and its outward peer terminate their two opposite
    shoulders at different stations. Both are physical joining interfaces;
    a single city-edge section cannot replace their staggered end profiles.
    """
    sockets = _variant_sockets(variant)
    require(arm in sockets and deck in ('upper', 'lower'), 'Unknown Y native end profile')
    inward = sockets[arm]['inward_en']
    normal = (inward[0], 0., -inward[1])
    records = []
    for group in posed_native_faces(context, arm, arm != 'C', variant=variant):
        if group['deck'] != deck:
            continue
        station = max(sum(p[i] * normal[i] for i in range(3))
                      for triangle in group['triangles'] for p in triangle)
        segments, seen = [], set()
        for face_index, triangle in enumerate(group['triangles']):
            for first, last in zip(triangle, (*triangle[1:], triangle[0])):
                if max(abs(sum(p[i] * normal[i] for i in range(3)) - station) for p in (first, last)) > 2e-6:
                    continue
                if math.dist(first[:3], last[:3]) <= 1e-10:
                    continue
                key = tuple(sorted((first, last)))
                if key in seen:
                    continue
                seen.add(key)
                segments.append({'face_index': face_index, 'parent_triangle': triangle, 'points': (first, last)})
        require(segments, 'Native finite mesh has no resolved coreward end ring')
        records.append({**{key: value for key, value in group.items() if key != 'triangles'},
                        'plane_normal_xyz': normal, 'plane_station_m': station, 'segments': segments})
    return records


def native_forward_sections(context, arm, deck, *, variant='original'):
    """All exposed forward boundary edges, including the diagonal PATH edge.

    The finite outer shoulder caps alone would omit the diagonal helper's
    long east edge across both actual traffic lanes. Each edge keeps its own
    physical comparison plane and original parent face's affine UV field.
    """
    sockets = _variant_sockets(variant)
    from collections import Counter
    inward = sockets[arm]['inward_en']
    direction = (inward[0], 0., -inward[1])
    first_station = min(group['plane_station_m'] for group in native_end_sections(context, arm, deck, variant=variant)
                        if group['role'] == 'pavement')
    result = []
    for group in posed_native_faces(context, arm, arm != 'C', variant=variant):
        if group['deck'] != deck:
            continue
        boundary = Counter(tuple(sorted((a[:3], b[:3]))) for triangle in group['triangles']
                           for a, b in zip(triangle, (*triangle[1:], triangle[0])))
        for face_index, triangle in enumerate(group['triangles']):
            surface_normal = _cross(tuple(triangle[1][i]-triangle[0][i] for i in range(3)),
                                    tuple(triangle[2][i]-triangle[0][i] for i in range(3)))
            for a, b in zip(triangle, (*triangle[1:], triangle[0])):
                if boundary[tuple(sorted((a[:3], b[:3])))] != 1:
                    continue
                if min(sum(p[i]*direction[i] for i in range(3)) for p in (a, b)) < first_station - 2e-6:
                    continue
                normal = _cross(tuple(b[i]-a[i] for i in range(3)), surface_normal)
                length = math.sqrt(sum(value*value for value in normal))
                if length < 1e-12:
                    continue
                normal = tuple(value/length for value in normal)
                alignment = sum(normal[i]*direction[i] for i in range(3))
                if abs(alignment) < 1e-7:
                    continue
                if alignment < 0:
                    normal = tuple(-value for value in normal)
                result.append({**{key: value for key, value in group.items() if key != 'triangles'},
                               'plane_normal_xyz': normal,
                               'plane_station_m': sum(a[i]*normal[i] for i in range(3)),
                               'segments': [{'face_index': face_index, 'parent_triangle': triangle, 'points': (a, b)}]})
    return result


def visible_native_end_sections(context, arm, deck, *, variant='original'):
    """Exclude only peer-roof cap spans already hidden by original native roof.

    The 309 pavement's measured horizontal millimetre phase overlaps the
    lower 302 pavement by a narrow strip. This exception is reconstructed
    from both pinned original surfaces; it does not excuse authored overlap.
    """
    from shapely.geometry import LineString, Polygon
    from shapely.ops import unary_union
    groups = native_forward_sections(context, arm, deck, variant=variant)
    sources = posed_native_faces(context, arm, variant != 'original', variant=variant)
    hidden_kind = 'peer' if variant == 'original' else 'helper'
    occluding_kind = 'helper' if variant == 'original' else 'peer'
    helper_roofs = [group for group in sources if group['deck'] == deck and group['role'] == 'pavement'
                   and group['kind'] == occluding_kind]
    result = []
    for group in groups:
        if group['kind'] != hidden_kind or group['role'] != 'pavement':
            result.append({**group, 'original_native_occluded_length_m': 0.})
            continue
        height = group['segments'][0]['points'][0][1]
        occluders = [Polygon([(p[0], -p[2]) for p in triangle]) for roof in helper_roofs
                     for triangle in roof['triangles'] if min(p[1] for p in triangle) > height + 1e-7]
        occlusion = unary_union(occluders)
        segments, hidden = [], 0.
        for segment in group['segments']:
            first, last = segment['points']
            line = LineString([(first[0], -first[2]), (last[0], -last[2])])
            visible = line.difference(occlusion)
            parts = [visible] if visible.geom_type == 'LineString' else list(getattr(visible, 'geoms', []))
            hidden += line.length - sum(part.length for part in parts if part.geom_type == 'LineString')
            delta = (last[0]-first[0], -last[2]+first[2])
            length2 = sum(value*value for value in delta)
            for part in parts:
                if part.geom_type != 'LineString' or part.length <= 1e-12:
                    continue
                points = []
                for east, north in (part.coords[0], part.coords[-1]):
                    t = ((east-first[0])*delta[0]+(north+first[2])*delta[1])/length2
                    require(-1e-8 <= t <= 1.+1e-8, 'Visible native cap escaped its original indexed edge')
                    points.append(tuple(first[i]+t*(last[i]-first[i]) for i in range(5)))
                segments.append({**segment, 'points': tuple(points)})
        result.append({**group, 'segments': segments, 'original_native_occluded_length_m': hidden})
    return result


def _oblique_segments(triangle, normal, station, tolerance):
    values = [sum(p[i] * normal[i] for i in range(3)) - station for p in triangle]
    # Classification and intersection must use the same signed distances.
    # Otherwise a vertex admitted as on-plane can also produce a second,
    # exact-sign crossing far along an extremely thin native contact face.
    values = [0. if abs(value) <= tolerance else value for value in values]
    if all(value == 0. for value in values):
        return [(triangle[i], triangle[(i + 1) % 3]) for i in range(3)]
    points = []
    for index in range(3):
        first, last = triangle[index], triangle[(index + 1) % 3]
        a, b = values[index], values[(index + 1) % 3]
        if a == 0.:
            points.append(first)
        if a * b < 0:
            fraction = a / (a - b)
            points.append(tuple(first[i] + fraction * (last[i] - first[i]) for i in range(len(first))))
    unique = []
    for point in points:
        if not any(math.dist(point[:3], value[:3]) <= tolerance for value in unique):
            unique.append(point)
    return [(unique[0], unique[1])] if len(unique) == 2 else []


def native_join_audit(world_faces, roles, materials, context, position_tolerance_m=2e-6, uv_tolerance=5e-6, arms=None, *, variant='original', owned_cells=None):
    """Check authored finite section coverage against native source segments.

    Only exact finite native coreward end profiles are required, including
    both staggered diagonal shoulders. Each authored triangle retains its
    material role code at vertex index 5. This does not certify an entire
    native collar or the authored road away from these joining profiles.
    """
    sockets = _variant_sockets(variant)
    require(owned_cells is None or variant == 'reversed',
            'Owned native join traces are reviewed only for the reversed Y')
    from shapely.geometry import LineString
    from shapely.ops import unary_union
    measured, checked, original_occlusion = [], 0, 0.
    periodic_offsets = set()
    selected = tuple(sockets) if arms is None else tuple(arms)
    require(selected and len(set(selected)) == len(selected) and set(selected) <= sockets.keys(),
            'Native Y seam audit requires unique reviewed arms')
    for arm in selected:
        for deck in ('upper', 'lower'):
            if owned_cells is None:
                groups = visible_native_end_sections(context, arm, deck, variant=variant)
            else:
                from .y_junction_reversed_native_models import owned_native_join_sections
                groups = owned_native_join_sections(context, arm, deck, owned_cells)
            for native_group in groups:
                original_occlusion += native_group['original_native_occluded_length_m']
                expected_role = native_group['role']
                candidates = []
                for face in world_faces:
                    codes = {round(point[5]) for point in face}
                    require(len(codes) == 1, 'Y authored native seam crosses material codes')
                    role = roles[codes.pop()]
                    if expected_role == 'pavement' and not role.startswith('pavement'):
                        continue
                    if expected_role != 'pavement' and not role.startswith(expected_role):
                        continue
                    if materials[role]['raw'] != native_group['material']['raw']:
                        continue
                    candidates.extend(segment for segment in _oblique_segments(face, native_group['plane_normal_xyz'],
                                      native_group['plane_station_m'], position_tolerance_m)
                                      if math.dist(segment[0][:3], segment[1][:3]) > position_tolerance_m)
                for segment in native_group['segments']:
                    first, last = segment['points']
                    vector = tuple(last[i] - first[i] for i in range(3))
                    length2 = sum(value * value for value in vector)
                    require(length2 > 0, 'Native seam segment is degenerate')
                    intervals = []
                    direction = (sockets[arm]['inward_en'][0], 0., -sockets[arm]['inward_en'][1])
                    derivative = _uv_derivative(segment['parent_triangle'], direction)
                    # The literal C core-contact donor repeats its texture
                    # once relative to the adjacent original native tile.
                    # Only its measured longitudinal UV axis may repeat.
                    repeat_axes = [arm == 'C' and abs(value) > 1e-8 for value in derivative]
                    for a, b in candidates:
                        fractions = []
                        valid = True
                        repeat = None
                        for point in (a, b):
                            t = sum((point[i] - first[i]) * vector[i] for i in range(3)) / length2
                            projection = tuple(first[i] + t * vector[i] for i in range(3))
                            if math.dist(point[:3], projection) > position_tolerance_m:
                                valid = False
                                break
                            uv = tuple(first[i] + t * (last[i] - first[i]) for i in (3, 4))
                            delta_uv = [point[i]-uv[i-3] for i in (3, 4)]
                            offset = tuple(round(value) if repeat_axes[i] else 0 for i, value in enumerate(delta_uv))
                            if any(abs(value) > 1 for value in offset) or max(abs(delta_uv[i]-offset[i]) for i in range(2)) > uv_tolerance:
                                valid = False
                                break
                            if repeat is not None and repeat != offset:
                                valid = False
                                break
                            repeat = offset
                            fractions.append(t)
                        if valid:
                            low, high = max(0., min(fractions)), min(1., max(fractions))
                            if high >= low:
                                intervals.append((low, high))
                                if any(repeat):
                                    periodic_offsets.add((arm, expected_role, *repeat))
                    coverage = unary_union([LineString([(a, 0.), (b, 0.)]) for a, b in intervals])
                    missing = LineString([(0., 0.), (1., 0.)]).difference(coverage)
                    require(missing.length * math.sqrt(length2) <= 2 * position_tolerance_m,
                            f'Y {arm} {deck} native {expected_role} seam loses finite geometry, material, or UV')
                    checked += 1
                measured.append({'arm': arm, 'deck': deck, 'native_owner': native_group['kind'],
                                 'role': expected_role, 'finite_segments_checked': len(native_group['segments'])})
    report = {'native_finite_segments_checked': checked, 'section_groups': measured,
            'position_tolerance_m': position_tolerance_m, 'uv_tolerance': uv_tolerance,
            'original_native_occluded_profile_length_m': original_occlusion,
            'native_C_longitudinal_texture_repeat_offsets': [list(value) for value in sorted(periodic_offsets)],
            'scope': 'Finite geometry, material, and affine UV at exact coreward native end profiles, including staggered diagonal shoulders',
            'in_game_rendering_tested': False}
    if owned_cells is not None:
        from .y_junction_reversed_native_models import ownership_join_trace_report
        report['source_interface_ownership'] = ownership_join_trace_report(context, owned_cells)
    return report
