#!/usr/bin/env python3
"""Bound a shoulder revision against actual saved preceding assembly models.

The existing SCP decoder and source-pinned support checker remain authoritative.
This audit adds no resource parser, route author, or consumer interchange format.
Its DD-top witnesses are explicitly finite, rather than a Boolean union proof.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import struct
import sys

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location('_slip_preservation_source_packages',
                                             ROOT / 'framework/scp/check_bootstrap.py')
_bootstrap = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bootstrap)
sys.meta_path.insert(0, _bootstrap.SourcePackages(ROOT))

from scp.dbpf import require
from scp.models import pack_s3d, parse_s3d
from scp_highway.parallel_verify import (HIGHWAY_SLIP_PROFILE, OWNED_CELLS,
    _FaceIndex, _continuous_support, _decode_faces, _uv, approved_candidate,
    check_projection, revised_routes, world_resources_from_build)
from scp_highway.native_overhangs import NATIVE_OVERHANG_SURFACES
from scp_highway.ramp_verify import _barycentric, _point_triangle_distance
from scp_highway.modular_assembly_verify import _triangle_distance

DD = 0x5713000E
AVENUE = frozenset((0x0400020E, 0x0400380E))
POSITION_BOUND_M = 2e-6  # The existing saved-face support certificate.


def _cycle(values):
    values = tuple(values)
    return min(values[index:] + values[:index] for index in range(3))


def _geometry_key(face):
    return face['material_sha256'], _cycle(face['points'])


def _attributed_key(face):
    return face['material_sha256'], _cycle(tuple((*point, *uv)
        for point, uv in zip(face['points'], face['uv'])))


def _kind(face):
    if face['texture'] != DD:
        return 'body'
    heights = [point[2] for point in face['points']]
    require(max(heights) - min(heights) <= POSITION_BOUND_M,
            'Shoulder revision adds a nonhorizontal DD-material surface')
    # The shared decoder's `upward` flag uses a 1e-12 area threshold for
    # surface indexing. Winding here is its exact sign, including an actual
    # positive 2.27e-13 m² encoded sliver; no negative-area waiver applies.
    require(_area(face) > 0., 'Shoulder revision reverses a DD pavement or paint face')
    if min(abs(heights[0] - height) for height in (7.5, 15.)) <= POSITION_BOUND_M:
        return 'deck'
    require(min(abs(heights[0] - height) for height in (7.51, 15.01)) <= POSITION_BOUND_M,
            'Shoulder revision moves DD pavement or white paint off its actual plane')
    return 'paint'


def compare_bodies(before, after):
    """Require exact physical faces; only trusted authored UV fields may change."""
    require(Counter(map(_geometry_key, before)) == Counter(map(_geometry_key, after)),
            'Shoulder revision changes a body pavement, barrier, underside, pier, raw material, or winding')
    # The preceding saved mesh identifies authored faces; a new candidate's
    # name cannot grant itself permission to alter a retained native UV.
    fixed = {key for face in before if face['texture'] in AVENUE
             or not face['mesh_name'].startswith('SCP NAM ')
             for key in (_geometry_key(face),)}
    old_fixed = Counter(_attributed_key(face) for face in before if _geometry_key(face) in fixed)
    new_fixed = Counter(_attributed_key(face) for face in after if _geometry_key(face) in fixed)
    require(old_fixed == new_fixed,
            'Shoulder revision changes retained native Avenue, barrier, or support UVs')
    return {'exact_geometry_material_winding_triangles': len(before),
            'exact_retained_native_uv_triangles': sum(old_fixed.values()),
            'authored_route_field_uv_triangles': len(before) - sum(old_fixed.values())}


def _masks():
    result = []
    # These are independent approved/reconstructed traffic sources. A bound
    # is the served shoulder only, including the measured half-metre erasure
    # band and a three-metre end allowance for the physical half-ribbon.
    for route in [*approved_candidate()['routes'], *revised_routes(HIGHWAY_SLIP_PROFILE)]:
        stations = [_uv(point)[0] for point in route['points']
                    if abs(point[2] - route['height_m']) < 1e-8]
        result.append((route['height_m'], route['side'], min(stations) - 3., max(stations) + 3.))
    return tuple(result)


def _masked(point, masks, *, paint=False):
    u, v = _uv(point)
    return any(abs(point[2] - height - (.01 if paint else 0.)) <= POSITION_BOUND_M
               and 4.3125 - POSITION_BOUND_M <= side * v <= 8. + POSITION_BOUND_M
               and low - POSITION_BOUND_M <= u <= high + POSITION_BOUND_M
               for height, side, low, high in masks)


def _native_vertex(point, uv, material_sha256, reference):
    """Retain the actual preceding native frame, including mirrored halves."""
    for face in reference.nearby(point, margin=POSITION_BOUND_M):
        if face['material_sha256'] != material_sha256:
            continue
        if _triangle_distance(point, face['points']) > POSITION_BOUND_M:
            continue
        weights = _barycentric(point, face['points'])
        if weights is None:
            continue
        expected = tuple(sum(weight * old[axis] for weight, old in zip(weights, face['uv']))
                         for axis in (0, 1))
        if max(abs(actual - old) for actual, old in zip(uv, expected)) <= 2e-6:
            return True
    return False


def _area(face):
    a, b, c = face['points']
    return ((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])) / 2.


@lru_cache(maxsize=1)
def _native_donor_faces():
    """Place existing frozen native DD triangles in their actual source cells."""
    result = []
    for column, row in sorted(OWNED_CELLS):
        if column + row not in (0, 1):
            continue
        for index, (material, vertices) in enumerate(NATIVE_OVERHANG_SURFACES):
            points = tuple((p[0] + 16. * column, -p[2] - 16. * row, p[1]) for p in vertices)
            if (material != '307aba7786d4b4f11dbc499eb54f7d05d01a114001919b8a5f7d55970fbb64ca'
                    or len({p[2] for p in points}) != 1 or points[0][2] not in (7.5, 15.)
                    or _area({'points': points}) <= 0.):
                continue
            result.append({'points': points, 'material_sha256': material,
                           'native_city_cell': [column, row], 'frozen_native_face_index': index})
    return _FaceIndex(result, size=2.)


def _native_fill_certificate(face):
    """Bound a complete new triangle by one convex, frozen native donor face.

    Each saved vertex must lie within the unchanged two-micrometre distance
    of the same closed source triangle. A triangle plus a Euclidean ball is
    convex, so the bound covers every convex combination of those vertices,
    rather than merely a finite set of line witnesses. UV permission is not
    granted here; the independent unmasked-UV and current-field checks remain.
    """
    points = face['points']
    if (face['texture'] != DD or _area(face) <= 0.
            or max(p[2] for p in points) - min(p[2] for p in points) > POSITION_BOUND_M
            or min(abs(points[0][2] - height) for height in (7.5, 15.)) > POSITION_BOUND_M):
        return None
    first = tuple(min(p[a] for p in points) for a in range(3))
    last = tuple(max(p[a] for p in points) for a in range(3))
    for donor in _native_donor_faces().nearby(first, last, margin=POSITION_BOUND_M):
        if donor['material_sha256'] != face['material_sha256']:
            continue
        distances = [_point_triangle_distance(point, donor['points']) for point in points]
        if max(distances) <= POSITION_BOUND_M:
            return {'native_triangle_enh_m': donor['points'],
                    'native_city_cell': donor['native_city_cell'],
                    'frozen_native_face_index': donor['frozen_native_face_index'],
                    'material_sha256': donor['material_sha256'],
                    'maximum_saved_vertex_distance_m': max(distances),
                    'saved_vertex_distances_m': distances, 'position_certificate_m': POSITION_BOUND_M,
                    'whole_face_bounded_by_convexity': True}
    return None


def _coverage(sources, targets, *, permit_source_native_fill=False):
    """Keep all historical coverage; separately certify repaired native holes."""
    common = Counter(map(_geometry_key, sources)) & Counter(map(_geometry_key, targets))
    index = _FaceIndex(targets, size=.25)
    controls = {'admitted_road_encoding_spans': 0,
                'maximum_admitted_along_route_span_m': 0.,
                'maximum_sampled_actual_face_distance_m': 0.}
    segments, native_fills = 0, {}
    for face in sources:
        key = _geometry_key(face)
        if common[key]:
            common[key] -= 1
            continue
        points = face['points']
        centre = tuple(sum(point[axis] for point in points) / 3. for axis in range(3))
        witnesses = [*zip(points, points[1:] + points[:1]),
                     *((centre, point) for point in points)]
        for first, last in witnesses:
            nearby = index.nearby(first, last, margin=POSITION_BOUND_M)
            supported = _continuous_support(first, last, nearby, controls)
            if not supported:
                certificate = _native_fill_certificate(face) if permit_source_native_fill else None
                require(certificate is not None,
                        f'Shoulder revision removes or moves native DD coverage at an actual face witness: {first} -> {last}')
                if key not in native_fills:
                    native_fills[key] = {'actual_saved_triangle_enh_m': points, 'donor_certificate': certificate,
                                         'historical_reference_gap_witnesses': []}
                native_fills[key]['historical_reference_gap_witnesses'].append({'first_enh_m': first, 'last_enh_m': last,
                    'historical_reference_two_micrometre_support_passed': False})
            segments += 1
    projection = check_projection([{**face, 'geometry_key': 'source-native-hole-fill'}
        for face in sources if _geometry_key(face) in native_fills]) if native_fills else None
    return {'line_segments_checked': segments, **controls,
            'historical_saved_reference_support_passed': not native_fills,
            'source_native_hole_fill_triangles': len(native_fills),
            'source_native_hole_fill_projection': projection,
            'historical_reference_holes_repaired': list(native_fills.values())}


def compare_decks(before, after, masks):
    require(before and after, 'Shoulder preservation needs actual native DD surfaces')
    require({face['material_sha256'] for face in before} == {face['material_sha256'] for face in after},
            'Shoulder revision changes a native DD raw material')
    checked, cache = 0, {}
    reference = _FaceIndex(before, size=.25)
    for face in after:
        for point, uv in zip(face['points'], face['uv']):
            if _masked(point, masks):
                continue
            key = face['material_sha256'], point, uv
            if key not in cache:
                cache[key] = _native_vertex(point, uv, face['material_sha256'], reference)
            require(cache[key], 'Shoulder revision changes an unmasked native DD vertex or UV')
            checked += 1
    coverage = {'reference_to_candidate': _coverage(before, after),
                'candidate_to_reference_or_frozen_native_donor': _coverage(after, before, permit_source_native_fill=True)}
    areas = []
    for height in (7.5, 15.):
        old = [face for face in before if abs(face['points'][0][2] - height) < POSITION_BOUND_M]
        new = [face for face in after if abs(face['points'][0][2] - height) < POSITION_BOUND_M]
        first, last = math.fsum(map(_area, old)), math.fsum(map(_area, new))
        perimeter = math.fsum(math.dist(a, b) for face in [*old, *new]
                              for a, b in zip(face['points'], face['points'][1:] + face['points'][:1]))
        # A conservative area envelope induced by the unchanged position
        # certificate. This is reported as a bound, not exact union equality.
        bound = POSITION_BOUND_M * perimeter + len(old + new) * math.pi * POSITION_BOUND_M ** 2
        require(abs(first - last) <= bound,
                'Shoulder revision changes native DD area beyond the saved-coordinate envelope')
        areas.append({'height_m': height, 'reference_area_m2': first, 'candidate_area_m2': last,
                      'absolute_area_difference_m2': abs(first - last),
                      'coordinate_induced_area_bound_m2': bound})
    return {'reference_triangles': len(before), 'candidate_triangles': len(after),
            'unmasked_native_vertex_uv_checks': checked,
            'unmasked_uv_basis': 'Affine interpolation on actual preceding saved native DD triangles, preserving their proper or mirrored frame',
            'unmasked_uv_tolerance': 2e-6, 'areas': areas,
            'finite_face_witnesses': coverage,
            'position_certificate_m': POSITION_BOUND_M,
            'all_historical_native_face_witnesses_preserved': True,
            'candidate_face_witnesses_are_historical_or_frozen_native_donor': True,
            'exact_boolean_union_equivalence_claimed': False}


def verify_slip_preservation(reference_world, candidate_world):
    require(set(reference_world) == set(candidate_world) == OWNED_CELLS,
            'Shoulder preservation requires the complete unchanged 31-cell world')
    decoded = []
    hashes = []
    for world in (reference_world, candidate_world):
        groups = {'body': [], 'deck': [], 'paint': []}
        model_hashes = {}
        for cell, (raw, _path) in sorted(world.items()):
            model_hashes[str(cell)] = hashlib.sha256(raw).hexdigest()
            for face in _decode_faces(raw, origin=(16. * cell[0], -16. * cell[1])):
                groups[_kind(face)].append(face)
        decoded.append(groups)
        hashes.append(model_hashes)
    before, after = decoded
    bodies = compare_bodies(before['body'], after['body'])
    masks = _masks()
    allowed = {face['material_sha256'] for face in before['deck']}
    for face in [*before['paint'], *after['paint']]:
        require(face['material_sha256'] in allowed and all(_masked(point, masks, paint=True) for point in face['points']),
                'Shoulder paint leaves its served deck, source station range, or measured shoulder band')
    decks = compare_decks(before['deck'], after['deck'], masks)
    return {'schema_version': 1, 'passed': True, 'highway_slip_profile': HIGHWAY_SLIP_PROFILE,
            'physical_body_comparison': bodies, 'native_dd_top_comparison': decks,
            'reference_white_paint_triangles': len(before['paint']),
            'candidate_white_paint_triangles': len(after['paint']),
            'intentional_uv_mask': {'minimum_served_q_m': 4.3125, 'maximum_served_q_m': 8.,
                'physical_half_ribbon_end_allowance_m': 3., 'native_deck_heights_m': [7.5, 15.],
                'paint_height_offset_m': .01,
                'source': 'Union of bounded original-approved and independently reconstructed revised served-shoulder stations; through lanes are excluded'},
            'reference_model_sha256_by_city_cell': hashes[0],
            'candidate_model_sha256_by_city_cell': hashes[1],
            'native_hole_fill_source': {'reference': 'domains/highway/implementation/scp_highway/native_overhangs.py',
                'reference_sha256': hashlib.sha256((ROOT / 'domains/highway/implementation/scp_highway/native_overhangs.py').read_bytes()).hexdigest(),
                'source_archive_sha256': 'ccf8dabd3930fce92d0baa872ff974e3a536ddcc40762505a2e70eafcf9c0dfb',
                'scope': 'Frozen native DD top triangles, in their true approved city cells; each admitted complete new triangle is within two micrometres of one convex donor triangle and keeps the same raw native material.'},
            'game_operation': 'unverified',
            'scope': 'Exact actual body XYZ/material/winding and retained native-body UVs; actual-baseline affine unmasked DD vertex UVs; complete historical-to-candidate finite DD face-edge and centroid-fan support witnesses with the existing two-micrometre encoding certificate; candidate witnesses supported by history or a separately reported whole-face convex frozen-native-donor certificate; and coordinate-bounded oriented area. Historical remap holes repaired by new native coverage are explicitly reported. Changed paint and route-field UVs need their separate current saved-resource checks. No exact historical Boolean-union, structural-load, or game-appearance claim.'}


def _mutant_world(world, mutation):
    """Change a referenced attribute or face in one actual saved S3D model."""
    masks = _masks()
    for cell, (raw, paths) in sorted(world.items()):
        model = parse_s3d(raw)
        for mesh in model['meshes']:
            vi, ii, pi, mi = mesh['frames'][0]
            block = model['vertices'][vi]
            material = model['materials'][mi]
            texture = material['textures'][0]
            indices = model['indices'][ii]['values']
            source = [struct.unpack_from('<5f', block['data'], at)
                      for at in range(0, len(block['data']), block['stride'])]
            posed = [(p[0] + 16. * cell[0], -p[2] - 16. * cell[1], p[1]) for p in source]
            referenced = [index for _kind, start, count in model['primitives'][pi]
                          for index in indices[start:start + count]]
            authored_barrier = texture == 0x5EB4BEE9 and mesh['name'].rstrip(b'\0') == b'SCP NAM barrier'
            if mutation in ('changed-authored-barrier-vertex', 'changed-raw-material') and authored_barrier:
                if mutation == 'changed-raw-material':
                    data = bytearray(material['raw'])
                    data[0] ^= 1
                    material['raw'] = bytes(data)
                else:
                    data = bytearray(block['data'])
                    at = referenced[0] * block['stride']
                    struct.pack_into('<f', data, at, source[referenced[0]][0] + .05)
                    block['data'] = bytes(data)
            elif mutation == 'changed-unmasked-native-uv' and texture == DD:
                chosen = next((index for index in referenced if not _masked(posed[index], masks)
                    and min(abs(posed[index][2] - height) for height in (7.5, 15.)) < POSITION_BOUND_M), None)
                if chosen is None:
                    continue
                data = bytearray(block['data'])
                struct.pack_into('<f', data, chosen * block['stride'] + 12, source[chosen][3] + .01)
                block['data'] = bytes(data)
            elif mutation == 'removed-through-lane-face' and texture == DD:
                chosen = None
                for _kind, start, count in model['primitives'][pi]:
                    if count < 6:
                        continue
                    for at in range(start, start + count, 3):
                        points = tuple(posed[index] for index in indices[at:at + 3])
                        centre = tuple(sum(point[axis] for point in points) / 3. for axis in range(3))
                        if (min(abs(centre[2] - height) for height in (7.5, 15.)) < POSITION_BOUND_M
                                and max(point[2] for point in points) == min(point[2] for point in points)
                                and abs(_uv(centre)[1]) < 4. and abs(_area({'points': points})) > .05):
                            chosen = at
                            break
                    if chosen is not None:
                        break
                if chosen is None:
                    continue
                model['indices'][ii]['values'] = indices[:chosen] + indices[chosen + 3:]
                primitive_ids = {frame[2] for part in model['meshes'] for frame in part['frames'] if frame[1] == ii}
                for primitive_id in primitive_ids:
                    model['primitives'][primitive_id] = [
                        (kind, start - (3 if start > chosen else 0),
                         count - (3 if start <= chosen < start + count else 0))
                        for kind, start, count in model['primitives'][primitive_id]]
            else:
                continue
            result = dict(world)
            result[cell] = pack_s3d(model), paths
            return result
    raise ValueError('No actual saved S3D witness is available for mutation: ' + mutation)


def mutation_controls(reference, candidate):
    controls = []
    for mutation in ('removed-through-lane-face', 'changed-unmasked-native-uv',
                     'changed-authored-barrier-vertex', 'changed-raw-material'):
        mutant = _mutant_world(candidate, mutation)
        try:
            verify_slip_preservation(reference, mutant)
        except ValueError as error:
            controls.append({'mutation': mutation, 'rejected': True, 'reason': str(error)})
        else:
            raise ValueError('Shoulder preservation accepted an actual saved-S3D negative control: ' + mutation)
    return controls


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference-build', type=Path, required=True)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    reference, reference_source = world_resources_from_build(args.reference_build)
    candidate, candidate_source = world_resources_from_build(args.build)
    report = verify_slip_preservation(reference, candidate)
    report['negative_controls'] = mutation_controls(reference, candidate)
    report['negative_controls_passed'] = True
    report['reference_source'] = reference_source
    report['source'] = candidate_source
    report['generator_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if 'sha256_by_city_cell' not in key
                      and key not in ('source', 'reference_source')}, indent=2))


if __name__ == '__main__':
    main()
