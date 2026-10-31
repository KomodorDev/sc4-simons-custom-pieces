"""Compare the straight-stamp repartition with an immutable saved checkpoint.

Expected geometry comes from the preceding saved DATs, never from the new
partition writer. A transferred triangle must retain every material and UV
byte, its winding, and the exact float32 representation of its old vertices
in its new city-cell frame. The resulting public model hashes are frozen
only after both complete layout comparisons pass.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import hashlib
import itertools
import json
import math
from pathlib import Path
import struct

from scp import jsonc
from scp.dbpf import require
from scp.models import parse_s3d, positions, validate_s3d
from scp.verify import S3D, strict_dbpf

STAMP = 'modular-stamp'
WINGS = {'lower-exit': ((2, -3),), 'lower-entry': ((-3, 2),),
         'upper-exit': ((-2, 4), (-3, 5)), 'upper-entry': ((4, -2), (5, -3))}
POSTS = ((-1, 1), (-1, 2), (1, -1), (2, -1), (-4, 4), (4, -4))
ROOT = Path(__file__).resolve().parents[4]
CONTRACT = ('domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/'
            'checks/straight-partition-models.jsonc')
PATH = (0x296678F7, 0xA966883F)
BUCKET_M = .001
INHERITED_DD_BRANCHES = {
    **{c: 'lower-exit-branch' for c in ((2, -3), (3, -3), (2, -2))},
    **{c: 'lower-entry-branch' for c in ((-3, 2), (-2, 2), (-3, 3))},
    **{c: 'upper-exit-branch' for c in ((-2, 3), (-4, 4), (-3, 4), (-2, 4), (-4, 5), (-3, 5))},
    **{c: 'upper-entry-branch' for c in ((4, -4), (5, -4), (4, -3), (5, -3), (3, -2), (4, -2))},
}


def reviewed_models():
    value = jsonc.load(ROOT/CONTRACT)
    require(value.get('schema_version') == 1 and value.get('independent_partition_audit_passed') is True
            and value.get('proof', {}).get('default_union_passed') is True
            and value.get('proof', {}).get('compact_union_passed') is True,
            'Straight modular models need a reviewed independent two-layout output contract')
    return value


def validate_reviewed_models(resources, piece):
    """Portable exact output identity, independent of ignored checkpoint DATs."""
    contract = reviewed_models()
    expected = contract['pieces'].get(piece['id'])
    require(expected is not None and expected['recipe'] == piece['recipe']
            and expected['geometry_key'] == piece['geometry_key']
            and expected['cells'] == piece['cells'] and expected['footprint'] == piece['footprint'],
            'The modular model contract has no exact matching piece and ownership declaration')
    require(len(expected['cell_resources']) == len(piece['cells']), 'Incomplete reviewed model cell contract')
    textures = set()
    for cell, tile, row in zip(piece['cells'], piece['tile_ids'], expected['cell_resources']):
        require(row['cell'] == cell, 'Reviewed modular resource cells changed order')
        for zoom in range(5):
            raw = resources[*S3D, int(tile, 16)+zoom]
            require(hashlib.sha256(raw).hexdigest() == row['model_sha256'],
                    'Saved modular model differs from the independently audited straight partition')
            model = parse_s3d(raw)
            validate_s3d(model)
            textures.update(t for material in model['materials'] for t in material['textures'])
        require(hashlib.sha256(resources[*PATH, int(tile, 16)]).hexdigest() == row['path_sha256'],
                'Saved modular PATH differs from the independently audited ownership partition')
    raw = resources[*S3D, int(piece['preview_id'], 16)]
    require(hashlib.sha256(raw).hexdigest() == expected['preview_sha256'],
            'Saved modular preview differs from the independently audited complete model')
    preview = parse_s3d(raw)
    validate_s3d(preview)
    textures.update(t for material in preview['materials'] for t in material['textures'])
    check_preview(resources, piece)
    return {'passed': True, 'independent_partition_model_hashes_checked': True,
            'model_resources_checked': 5*len(piece['cells'])+1,
            'cell_paths_checked': len(piece['cells']),
            'texture_ids': sorted(textures),
            'contract_sha256': hashlib.sha256((ROOT/CONTRACT).read_bytes()).hexdigest(),
            'game_rendering_tested': False,
            'scope': 'Frozen outputs after independent checkpoint triangle/UV/material/winding and ownership comparison. Whole-assembly pavement support remains a separate required check.'}


def check_preview(resources, piece):
    from scp.verify import mesh_data, translated
    expected = []
    for cell, tile in zip(piece['cells'], piece['tile_ids']):
        model = parse_s3d(resources[*S3D, int(tile, 16)])
        expected.extend((mesh_data(model, mesh), (16.*cell[0], 0., 16.*cell[1]))
                        for mesh in model['meshes'])
    model = parse_s3d(resources[*S3D, int(piece['preview_id'], 16)])
    require(len(model['meshes']) == len(expected), 'A repartition preview omits or adds an owned model mesh')
    for mesh, (source, offset) in zip(model['meshes'], expected):
        require(translated(mesh_data(model, mesh), source, offset),
                'A repartition preview changes its complete translated cell models')
    return True


@dataclass(frozen=True)
class Triangle:
    owner: str
    piece_id: str
    source_cell: tuple
    mesh_name: str
    material: bytes
    texture: int
    format: int
    vertex_flags: int
    mesh_flags: int
    world: tuple
    local: tuple
    tails: tuple
    anchor: tuple


def _scene_rows(build, scene):
    build = Path(build)
    raw = (build/'manifest.json').read_bytes()
    manifest = json.loads(raw)
    pieces = {piece['id']: piece for piece in manifest['pieces']}
    files = {row['path']: row for row in manifest['files']}
    result = []
    used = set()
    for placement in scene['placements']:
        piece = pieces[placement['piece_id']]
        require(piece['id'] not in used, 'A repartition scene repeats a piece type')
        used.add(piece['id'])
        require(placement.get('rotation_degrees_ccw', 0) == 0,
                'The independently reviewed repartition checkpoint uses canonical proper poses')
        archive = (build/piece['asset_file']).read_bytes()
        row = files[piece['asset_file']]
        require(len(archive) == row['bytes'] and hashlib.sha256(archive).hexdigest() == row['sha256'],
                'A repartition DAT differs from its exact saved manifest')
        result.append((piece, placement, strict_dbpf(archive)))
    return result, hashlib.sha256(raw).hexdigest()


def triangles(rows):
    for piece, placement, resources in rows:
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            anchor = (placement['origin_m'][0]+16*cell[0], placement['origin_m'][1]-16*cell[1])
            source_cell = (round(anchor[0]/16)-4, round(-anchor[1]/16)-4)
            model = parse_s3d(resources[*S3D, int(tile, 16)+4])
            validate_s3d(model)
            for mesh in model['meshes']:
                require(len(mesh['frames']) == 1, 'Repartition comparison requires static complete S3D meshes')
                vi, ii, pi, mi = mesh['frames'][0]
                block = model['vertices'][vi]
                points, indices = positions(block), model['indices'][ii]['values']
                for kind, first, count in model['primitives'][pi]:
                    require(kind == 0 and count % 3 == 0, 'Repartition comparison requires indexed triangles')
                    for at in range(first, first+count, 3):
                        ids = indices[at:at+3]
                        local = tuple(points[i] for i in ids)
                        world = tuple((p[0]+anchor[0], -p[2]+anchor[1], p[1]) for p in local)
                        tails = tuple(block['data'][i*block['stride']+12:(i+1)*block['stride']] for i in ids)
                        require(len(model['materials'][mi]['textures']) == 1,
                                'Repartition triangles require one audited material texture')
                        yield Triangle(piece['geometry_key'], piece['id'], source_cell,
                            mesh['name'].decode('ascii').rstrip('\0'), model['materials'][mi]['raw'],
                            model['materials'][mi]['textures'][0],
                            block['format'], block['flags'], mesh['flags'], world, local, tails, anchor)


def _post(triangle):
    # Only the six actual central 0.8 m square shafts stay with the stamp.
    return any(all(abs(p[0]-(16*x+64)) <= .400002 and
                       abs(p[1]-(-16*y-64)) <= .400002 for p in triangle.world) for x, y in POSTS)


def assigned_owner(triangle, alternative):
    """Determine the new owner from old saved geometry and literal service side."""
    key = triangle.owner
    if key != STAMP:
        if alternative == 'compact' and key.endswith('-grade'):
            return key.removesuffix('-grade')+'-compact'
        return key
    name = triangle.mesh_name
    if name in ('SCP NAM ramp', 'SCP NAM barrier', 'SCP NAM concrete'):
        if name == 'SCP NAM concrete' and _post(triangle):
            return STAMP
        centre = tuple(sum(p[a] for p in triangle.world)/3 for a in range(3))
        east, north = centre[0]-64, centre[1]+64
        u, v = (east+north)/math.sqrt(2), (north-east+8)/math.sqrt(2)
        require(abs(v) > 6., 'An unclassified authored stamp face lies inside the core highway')
        deck = 'lower' if v > 0 else 'upper'
        entry = u < 0 if deck == 'lower' else u > 0
        return deck+('-entry-' if entry else '-exit-')+('compact' if alternative == 'compact' else 'r40')
    require(not name.startswith('SCP NAM ') or name == 'SCP NAM highway',
            'An unknown authored mesh cannot silently remain in the straight stamp')
    return STAMP


def _tails(triangle):
    return min(triangle.tails[i:]+triangle.tails[:i] for i in range(3))


def _signature(triangle, owner):
    return owner, triangle.material, triangle.format, triangle.vertex_flags, triangle.mesh_flags, _tails(triangle)


def _bucket(triangle):
    return tuple(math.floor(sum(p[a] for p in triangle.world)/3/BUCKET_M) for a in range(3))


def _f32(value):
    return struct.unpack('<f', struct.pack('<f', value))[0]


def translated_match(old, new):
    """Return max world residual if exactly one target-frame encoding matches."""
    for turn in range(3):
        tails = old.tails[turn:]+old.tails[:turn]
        if tails != new.tails:
            continue
        world = old.world[turn:]+old.world[:turn]
        expected = tuple((_f32(p[0]-new.anchor[0]), p[2], _f32(-(p[1]-new.anchor[1]))) for p in world)
        if expected == new.local:
            return max(math.dist(a, b) for a, b in zip(world, new.world))
    return None


def compare_union(old_rows, new_rows, *, alternative):
    """Require an exact one-to-one attributed triangle/owner partition."""
    require(alternative in ('default', 'compact'), 'Unknown checkpoint layout')
    buckets = defaultdict(lambda: defaultdict(list))
    counts = Counter()
    for triangle in triangles(old_rows):
        owner = assigned_owner(triangle, alternative)
        buckets[_signature(triangle, owner)][_bucket(triangle)].append(triangle)
        counts[owner] += 1
    maximum, moved, total = 0., 0, 0
    for triangle in triangles(new_rows):
        possible = buckets.get(_signature(triangle, triangle.owner))
        require(possible is not None, f'A {triangle.owner} triangle changes its owner, material, vertex attributes, or winding')
        center, found = _bucket(triangle), None
        for delta in itertools.product((-1, 0, 1), repeat=3):
            cell = tuple(a+b for a, b in zip(center, delta))
            candidates = possible.get(cell, ())
            for index, old in enumerate(candidates):
                residual = translated_match(old, triangle)
                if residual is not None:
                    found = cell, index, residual, old
                    break
            if found is not None:
                break
        require(found is not None,
                f'A {triangle.owner} triangle is not the exact float32 translation of a checkpoint face')
        cell, index, residual, old = found
        possible[cell].pop(index)
        maximum, moved, total = max(maximum, residual), moved+(old.owner != triangle.owner), total+1
    remaining = sum(len(rows) for group in buckets.values() for rows in group.values())
    require(remaining == 0, 'The straight partition omits a checkpoint pavement, barrier, bridge, paint, or support triangle')
    return {'passed': True, 'attributed_triangles': total, 'triangles_assigned_to_a_different_owner': moved,
            'expected_triangles_by_geometry_key': dict(sorted(counts.items())),
            'material_and_non_xyz_vertex_bytes_exact': True, 'cyclic_winding_preserved': True,
            'target_frame_float32_encoding_exact': True, 'maximum_world_vertex_translation_residual_m': maximum,
            'scope': 'One-to-one saved indexed triangles; only one exact float32 translation into the actual target host frame is accepted. Mesh regrouping and names are not geometry.'}


def compare_paths(old_rows, new_rows):
    def cells(rows):
        result = {}
        for piece, placement, resources in rows:
            for cell, tile in zip(piece['cells'], piece['tile_ids']):
                at = (round(placement['origin_m'][0]/16)+cell[0],
                      round(-placement['origin_m'][1]/16)+cell[1])
                require(at not in result, 'The repartition gives two independent pieces one traffic tile')
                result[at] = resources[*PATH, int(tile, 16)]
        return result
    old, new = cells(old_rows), cells(new_rows)
    require(old == new, 'The repartition changes a complete owned-city-cell PATH or construction footprint')
    return {'passed': True, 'unique_owned_cells': len(new), 'every_owned_cell_path_byte_exact': True}


def straight_envelope(rows):
    checked, maximum, materials = 0, 0., set()
    for triangle in triangles(rows):
        if triangle.owner != STAMP:
            continue
        materials.add(hashlib.sha256(triangle.material).hexdigest())
        if max(p[2] for p in triangle.world) <= 1e-6:
            continue  # Independently unchanged native Avenue pavement at ground.
        for east, north, _height in triangle.world:
            lateral = (north-east+136.)/math.sqrt(2.)
            maximum = max(maximum, abs(lateral))
            require(abs(lateral) <= 8.000002,
                    'The corrected highway stamp still contains an elevated curved wing outside its straight native envelope')
            checked += 1
        require(triangle.mesh_name not in ('SCP NAM ramp', 'SCP NAM barrier'),
                'A curved authored ramp or its barriers remain part of the highway stamp')
    require(checked > 0, 'No elevated straight-stamp vertices were checked')
    return {'passed': True, 'elevated_indexed_vertex_uses': checked,
            'maximum_abs_native_lateral_m': maximum, 'native_half_width_m': 8.,
            'native_encoded_boundary_tolerance_m': .000002,
            'material_sha256': sorted(materials),
            'scope': 'Every elevated indexed stamp vertex stays in the straight native DD envelope; unchanged native ground Avenue triangles remain separate.'}


def output_contract(rows, *, proof):
    pieces = {}
    for piece, _placement, resources in rows:
        if not piece['recipe'].startswith('highway_ddrhw_modular_'):
            continue
        check_preview(resources, piece)
        cells = []
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            raw = resources[*S3D, int(tile, 16)]
            require(all(resources[*S3D, int(tile, 16)+q] == raw for q in range(5)),
                    'A repartition output zoom differs from its canonical saved model')
            cells.append({'cell': cell, 'model_sha256': hashlib.sha256(raw).hexdigest(),
                          'path_sha256': hashlib.sha256(resources[*PATH, int(tile, 16)]).hexdigest()})
        pieces[piece['id']] = {'recipe': piece['recipe'], 'geometry_key': piece['geometry_key'],
            'cells': piece['cells'], 'footprint': piece['footprint'], 'cell_resources': cells,
            'preview_sha256': hashlib.sha256(resources[*S3D, int(piece['preview_id'], 16)]).hexdigest()}
    return {'schema_version': 1, 'independent_partition_audit_passed': True, 'proof': proof, 'pieces': pieces}


def check_union_traffic(rows, routes):
    """Run continuous pavement and solid-prism tests on the actual model union.

    Frozen per-piece outputs authorize only the exact reviewed overhangs.
    Geometry decoding below deliberately has no generic overhang exemption:
    provenance is checked first, and every traffic segment must then have
    actual support in the assembled indexed faces.
    """
    from .ramp_verify import _intrudes, _rotate
    for piece, _pose, resources in rows:
        if piece['recipe'].startswith('highway_ddrhw_modular_'):
            validate_reviewed_models(resources, piece)
    faces, grid = [], defaultdict(list)
    for tri in triangles(rows):
        a, b, c = tri.world
        area = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        low = tuple(min(p[i] for p in tri.world) for i in range(3))
        high = tuple(max(p[i] for p in tri.world) for i in range(3))
        face = {'points': tri.world, 'upward': area > 1e-12, 'texture': tri.texture,
                'material_sha256': hashlib.sha256(tri.material).hexdigest(), 'low': low, 'high': high}
        index = len(faces)
        faces.append(face)
        for x in range(math.floor(low[0]), math.floor(high[0])+1):
            for y in range(math.floor(low[1]), math.floor(high[1])+1):
                grid[x, y].append(index)
    segments, admitted = 0, []
    for route in routes:
        if route['transport'] != 1:
            continue
        for first, last in zip(route['points'], route['points'][1:]):
            low = (min(first[0], last[0])-1.25, min(first[1], last[1])-1.25,
                   min(first[2], last[2])-.0002)
            high = (max(first[0], last[0])+1.25, max(first[1], last[1])+1.25,
                    max(first[2], last[2])+3.8)
            ids = {i for x in range(math.floor(low[0]), math.floor(high[0])+1)
                   for y in range(math.floor(low[1]), math.floor(high[1])+1) for i in grid.get((x, y), ())}
            candidates = [faces[i] for i in ids if all(faces[i]['high'][a] >= low[a] and
                          faces[i]['low'][a] <= high[a] for a in range(3))]
            for quarter in range(4):
                begin, end = _rotate(first, quarter), _rotate(last, quarter)
                rotated = [{**face, 'points': tuple(_rotate(p, quarter) for p in face['points'])}
                           for face in candidates]
                source_cell = route['cell'][0]-4, route['cell'][1]-4
                require(_union_covered(begin, end, rotated, source_cell, quarter, admitted),
                        f'Assembled modular pavement does not continuously support saved route {route["id"]}, '
                        f'rotation={quarter}, points={begin}->{end}')
                require(all(not _intrudes(begin, end, face['points'], 1.25, 3.8) for face in rotated),
                        f'An assembled modular solid enters saved car route {route["id"]}, rotation={quarter}')
            segments += 1
    require(segments > 0, 'No actual saved assembled car segments were checked')
    return {'passed': True, 'continuous_saved_car_segments': segments,
            'proper_rotations_checked': 4, 'indexed_triangles': len(faces),
            'pavement_path_offset_m': 0., 'car_corridor_half_width_m': 1.25,
            'car_corridor_height_m': 3.8, 'continuous_support_with_reported_encoding_precision': True,
            'strict_barycentric_and_height_tests_unchanged': True,
            'inherited_dd_encoding_precision': {'euclidean_limit_m': .000002,
                'admitted_spans': len(admitted), 'spans': admitted,
                'maximum_sampled_distance_m': max((r['maximum_sampled_distance_m'] for r in admitted), default=0.),
                'scope': 'The unchanged finite-edge rectangle/endpoint-disc proof applies only to exact frozen inherited branch cells and affirmative flat DD faces. Every admitted interval is recorded; outside those cells strict support is mandatory.'},
            'scope': 'Actual complete indexed-model union supports every saved car PATH segment and clears its declared narrow solid prism. This is not game operation or a complete swept vehicle body.'}


def _union_covered(first, last, faces, source_cell, quarter, admitted):
    """Inherit the existing native encoding proof after exact output checks."""
    from . import ramp_verify as v
    if v._covered(first, last, faces):
        return True
    key = INHERITED_DD_BRANCHES.get(tuple(source_cell))
    if key is None:
        return False
    require(v.SUPPORT_ENCODING_DISTANCE_M == .000002, 'The inherited native encoding cap changed')
    encoding = {'geometry_key': key, 'field_controls': {'passed': True,
        'provenance': 'Exact independently frozen one-to-one checkpoint geometry and native UV/material union.'}}
    precision = {'admitted_spans': 0, 'admitted_endpoint_spans': 0,
                 'maximum_admitted_along_path_span_m': 0., 'distance_samples_checked': 0,
                 'maximum_sampled_distance_m': 0.}
    if not v._covered(first, last, faces, encoding=encoding, precision_report=precision):
        return False
    intervals = sorted(interval for face in faces if face['upward']
                       if (interval := v._interval(first, last, face['points'])) is not None)
    end, gaps = 0., []
    for low, high in intervals:
        if low > end+1e-7:
            gaps.append((end, low))
        end = max(end, high)
    if end < 1.-1e-7:
        gaps.append((end, 1.))
    deck = 7.5 if key.startswith('lower') else 15.
    native = [f for f in faces if f['upward'] and f['texture'] == 0x5713000E
              and f.get('material_sha256') == v.DD_MATERIAL_SHA256
              and all(abs(p[2]-deck) <= 1e-5 and p[2] == f['points'][0][2] for p in f['points'])]
    for low, high in gaps:
        samples = [tuple(a+t*(b-a) for a, b in zip(first, last)) for t in (low, (low+high)/2., high)]
        distances = [min(v._point_triangle_distance(p, f['points']) for f in native) for p in samples]
        admitted.append({'source_world_cell': list(source_cell), 'inherited_source_region': key,
            'proper_rotation_clockwise_quarters': quarter, 'path_segment_m': [list(first), list(last)],
            'uncovered_fraction_interval': [low, high],
            'along_path_span_m': (high-low)*math.dist(first, last),
            'distance_sample_points_m': [list(p) for p in samples], 'distance_samples_m': distances,
            'maximum_sampled_distance_m': max(distances), 'complete_interval_capsule_proof_passed': True})
    require(len(gaps) == precision['admitted_spans'], 'Inherited precision reporting omitted an admitted interval')
    return True


def audit_layouts(baseline, baseline_scene, candidate, candidate_scene):
    """Return proof and a proposed frozen contract only after both layouts pass."""
    reports, all_new = {}, {}
    for name in ('default', 'compact'):
        old_scene = baseline_scene if name == 'default' else {**baseline_scene, **baseline_scene['alternatives']['compact']}
        new_scene = candidate_scene if name == 'default' else {**candidate_scene, **candidate_scene['alternatives']['compact']}
        old, old_manifest = _scene_rows(baseline, old_scene)
        new, new_manifest = _scene_rows(candidate, new_scene)
        reports[name] = {'union': compare_union(old, new, alternative=name),
                         'owned_paths': compare_paths(old, new), 'straight_stamp': straight_envelope(new)}
        all_new.update({p['id']: (p, pose, resources) for p, pose, resources in new})
    proof = {'baseline_manifest_sha256': old_manifest, 'candidate_manifest_sha256': new_manifest,
             'baseline_scene_sha256': hashlib.sha256(json.dumps(baseline_scene, sort_keys=True).encode()).hexdigest(),
             'candidate_scene_sha256': hashlib.sha256(json.dumps(candidate_scene, sort_keys=True).encode()).hexdigest(),
             'default_union_passed': True, 'compact_union_passed': True,
             'expected_source': 'Immutable independently reviewed saved checkpoint; no writer-derived expected geometry.'}
    report = {'schema_version': 1, 'independent_partition_audit_passed': True, 'proof': proof,
              'layouts': reports, 'game_operation': 'unverified'}
    return report, output_contract(list(all_new.values()), proof=proof)
