#!/usr/bin/env python3
"""Audit sampled driver-left yellow in saved reversed Y S3D/PATH files.

No geometry or UV writer is imported. Road directions come from actual saved
PATH points, and texture positions come from the encoded triangle attributes.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import re
import struct
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.dbpf import require
from scp.models import parse_s3d, pack_s3d
from scp.paths import local_settings
from scp.preview import TextureLibrary, decode_fsh, read_resource
from scp.verify import parse_paths

import numpy as np
from shapely.geometry import Point, Polygon, box
from shapely.strtree import STRtree

MIS, DD = 0x5712000E, 0x5713000E
FSH_SHA = {
    MIS: {'050264fbfd4aa3dbc9da4989c602b926abaab58cd18bc4747a6e19fb78a2bc8a',
          '676fd00d3e3d608917274ed742ecf75e8253b4d6be20586a1eb19db5c3222105'},
    DD: {'25a91179a26a82ba6307777b1957c5862bee61daf55c7638c4487d64b275c7b8',
         '6539c7d6d5a33e157c842724799a326f9f392a8282b0bbe27f74a2fe96ec6e7d'},
}
RGBA_SHA = {MIS: '4356005bdc0f7ed5e5b96f9bb1274acb7afbf502266360dbbad0744ef51a5210',
            DD: '3ff0c1dcdd4e987dd50c51f240055cccad5c0531619ce626f96447b5d33d1d11'}
ORIGINS = {'ddrhw-y-reversed-diagonal-stem-split': (-2, 1),
           'ddrhw-y-reversed-diagonal-branch': (-2, -3),
           'ddrhw-y-reversed-orthogonal-core': (-1, 0)}
NAMES = ('A-B', 'B-A', 'A-C', 'C-A', 'B-C', 'C-B')
ARM_POINTS = {'A': (-24., -32.), 'B': (-24., 32.), 'C': (56., 0.)}
INWARD = {'A': (math.sqrt(.5), math.sqrt(.5)),
          'B': (math.sqrt(.5), -math.sqrt(.5)), 'C': (-1., 0.)}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def is_yellow(rgb):
    red, green, blue = rgb[:3]
    # The pinned stripe-core pixels include weathered RGB137/118/25.
    # Chroma separates their yellow paint from grey asphalt and white lines.
    return red > 125 and green > 105 and blue < 80 and red-blue > 80 and green-blue > 60


def textures(cache, plugins=None):
    cache = Path(cache)
    if not all((cache/f'{iid:08x}.fsh').is_file() for iid in (MIS, DD)):
        if plugins is None:
            plugins = Path(jsonc.load(local_settings(ROOT))['plugins']).expanduser()
        library = TextureLibrary(Path(plugins).expanduser())
        dummy = {'materials': [{'textures': [iid]} for iid in (MIS, DD)],
                 'meshes': [{'frames': [(0, 0, 0, i)]} for i in range(2)]}
        library.for_model(dummy)
        cache.mkdir(parents=True, exist_ok=True)
        for iid in (MIS, DD):
            key = (0x7AB50E44, 0x1ABE787D, iid)
            providers = sorted(library.index[key], key=lambda path: (path.name == 'High Speed Rail_Textures.dat', str(path)))
            raw = read_resource(providers[-1], key)
            require(sha(raw) == library.provenance[iid]['fsh_sha256'], 'Texture loader changed its selected source')
            (cache/f'{iid:08x}.fsh').write_bytes(raw)
    images, provenance = {}, {}
    for iid in (MIS, DD):
        raw = (cache/f'{iid:08x}.fsh').read_bytes()
        image = np.asarray(decode_fsh(raw).convert('RGBA'), dtype=np.uint8)
        require(sha(raw) in FSH_SHA[iid] and image.shape == (128, 128, 4)
                and sha(image.tobytes()) == RGBA_SHA[iid], 'Pinned native marking pixels changed')
        yellow = np.array([[is_yellow(pixel) and pixel[3] > 200 for pixel in row] for row in image])
        columns = [int(i) for i, count in enumerate(yellow.sum(axis=0)) if count >= 96]
        require(columns and min(columns) > 64, 'Pinned yellow stripe is not in the measured high-U half')
        images[iid] = image.astype(float)
        provenance[iid] = {'texture_id': f'{iid:08x}', 'fsh_sha256': sha(raw),
            'decoded_rgba_sha256': sha(image.tobytes()), 'size_px': [128, 128],
            'yellow_threshold_rgb': 'R>125,G>105,B<80,R-B>80,G-B>60;alpha>200',
            'yellow_columns_with_at_least_96_of_128_rows': columns,
            'yellow_uv_pixel_centres': [(column+.5)/128. for column in columns]}
    return images, provenance


def decode_model(raw, cell, model_id, native_reference=False, pose=0):
    model = parse_s3d(raw)
    result = []
    for mesh_index, mesh in enumerate(model['meshes']):
        for vi, ii, pi, mi in mesh['frames']:
            buffer = model['vertices'][vi]
            require(buffer['stride'] >= 20, 'Saved pavement omits XYZUV vertices')
            vertices = [struct.unpack_from('<5f', buffer['data'], at)
                        for at in range(0, len(buffer['data']), buffer['stride'])]
            if pose:
                rotated = []
                for x, height, south, u, v in vertices:
                    for _ in range(pose):
                        x, south = -south, x
                    rotated.append((x, height, south, u, v))
                vertices = rotated
            material = model['materials'][mi]
            require(len(material['textures']) == 1, 'Saved face does not have one actual material texture')
            texture = material['textures'][0]
            name = mesh['name'].rstrip(b'\0').decode('ascii')
            for primitive, start, count in model['primitives'][pi]:
                require(primitive == 0 and count % 3 == 0, 'Saved marking mesh is not a triangle list')
                for at in range(start, start+count, 3):
                    points = [vertices[i] for i in model['indices'][ii]['values'][at:at+3]]
                    world = np.array([(p[0]+16*cell[0], -p[2]-16*cell[1], p[1]) for p in points])
                    normal = np.cross(world[1]-world[0], world[2]-world[0])
                    if normal[2] <= 1e-12:
                        continue
                    matrix = np.array([[p[0], p[1], 1.] for p in world])
                    if abs(np.linalg.det(matrix)) <= 1e-14:
                        continue
                    fields = np.linalg.solve(matrix, np.array([[p[2], q[3], q[4]] for p, q in zip(world, points)]))
                    result.append({'points': world, 'uv': np.array([(p[3], p[4]) for p in points]),
                        'geometry': Polygon(world[:, :2]), 'fields': fields, 'texture': texture,
                        'mesh': name, 'model': model_id, 'mesh_index': mesh_index,
                        'material_sha256': sha(material['raw']),
                        'rendered_by': 'unchanged-native-socket' if native_reference else 'new-encoded-component',
                        'pavement': texture in (MIS, DD) and ('pavement' in name or
                            native_reference and name in ('Top Deck', 'Bottom Deck'))})
    return result


def load_saved(folder, reverse_texture=None):
    faces, fragments, signatures = [], defaultdict(list), []
    cells = set()
    for piece_id, origin in ORIGINS.items():
        directory = folder/piece_id
        require(directory.is_dir(), 'Saved candidate lacks an expected reversed component')
        paths = sorted(directory.glob('*.s3d'))
        for path in paths:
            match = re.fullmatch(r'(-?\d+)-(-?\d+)\.s3d', path.name)
            require(match, 'Unexpected saved model filename')
            local = tuple(map(int, match.groups()))
            cell = local[0]+origin[0], local[1]+origin[1]
            require(cell not in cells, 'Saved marking candidate repeats a model owner')
            cells.add(cell)
            raw = path.read_bytes()
            original_size = len(raw)
            original_hash = sha(raw)
            if reverse_texture is not None:
                model = parse_s3d(raw)
                selected = {frame[0] for mesh in model['meshes'] for frame in mesh['frames']
                            if model['materials'][frame[3]]['textures'] == [reverse_texture]}
                for vi in selected:
                    block = model['vertices'][vi]
                    data = bytearray(block['data'])
                    for offset in range(0, len(data), block['stride']):
                        u, = struct.unpack_from('<f', data, offset+12)
                        struct.pack_into('<f', data, offset+12, 1.-u)
                    block['data'] = bytes(data)
                raw = pack_s3d(model)
            label = path.relative_to(folder).as_posix()
            faces.extend(decode_model(raw, cell, label))
            signatures.append({'path': label, 'sha256': original_hash, 'bytes': original_size})
            path_file = path.with_suffix('.path')
            path_raw = path_file.read_bytes()
            parsed = parse_paths(path_raw)
            require(parsed['terrain'] == 1, 'Saved marking PATH does not retain its actual elevated coordinates')
            names = re.findall(rb'-- SCP Y ([ABC]-[ABC]) source_lane=', path_raw)
            require(len(names) == len(parsed['routes']), 'Saved PATH labels do not bind all actual routes')
            for name, route in zip(names, parsed['routes']):
                require(route['transport'] == 1, 'Marking direction is not an actual car path')
                fragments[name.decode()].append(np.array([(p[0]+16*cell[0], p[1]-16*cell[1], p[2])
                                                           for p in route['points']]))
            signatures.append({'path': path_file.relative_to(folder).as_posix(), 'sha256': sha(path_raw), 'bytes': len(path_raw)})
    require(len(cells) == 21 and set(fragments) == set(NAMES), 'Saved candidate does not cover all21 owners and six journeys')
    routes = {}
    for name, rows in fragments.items():
        starts = [row for row in rows if not any(np.linalg.norm(row[0]-other[-1]) <= 2e-7 for other in rows if other is not row)]
        require(len(starts) == 1, 'Saved journey has no unique directed start')
        pending = [row for row in rows if row is not starts[0]]
        points = list(starts[0])
        while pending:
            following = [row for row in pending if np.linalg.norm(points[-1]-row[0]) <= 2e-7]
            require(len(following) == 1, 'Saved directed journey does not connect uniquely through its actual seams')
            row = following[0]
            points.extend(row[1:]); pending = [other for other in pending if other is not row]
        routes[name] = np.array(points)
    return faces, routes, signatures


def native_socket_contributions(native_build):
    """Decode actual unchanged native models that already render at the joins.

    Early diagonal cross-sections straddle a custom-owned city cell and its
    native helper. Sampling only the custom DAT would omit a real native
    yellow edge across E=-24; no new geometry is added by this reader.
    """
    from scp.dbpf import entries, decompress
    audit_raw = (native_build/'input-audit.json').read_bytes()
    rows = json.loads(audit_raw)['donors']
    archives = [row for row in rows if row['filename'] == 'RealHighway_DD_RHW-4.dat']
    require(len(archives) == 1, 'Native input audit must name exactly one DD RHW archive')
    archive = archives[0]
    archive_path = Path(archive['path']).expanduser()
    if not archive_path.is_absolute():
        archive_path = ROOT/archive_path
    archive_bytes = archive_path.read_bytes()
    require(sha(archive_bytes) == archive['sha256'], 'Actual native socket archive changed')
    resources = entries(archive_bytes)
    pins = {0x57530200: '4eb082b8329ddf70be7333f3343c4f1a621985d3992b17ca624eef79dc0ee4a8',
            0x57530900: 'd319f9bb39e21e319f5ce566c5093ba9e955c4c0ed5a5dcbb703c6afe127c93a',
            0x57530000: '3d94bcce2ff84c9bd06d3bbbc7a089b8eaa28cfe921c3d31e87a27300cffd3dd'}
    placed = ((0x57530200, 0, (-2, 2)), (0x57530900, 2, (-2, 3)),
              (0x57530200, 3, (-2, -2)), (0x57530900, 1, (-2, -3)),
              (0x57530000, 1, (4, 0)), (0x57530000, 1, (5, 0)))
    faces, signatures = [], []
    for donor, pose, cell in placed:
        raw = decompress(resources[0x5AD0E817, 0xBADB57F1, donor])
        require(sha(raw) == pins[donor], 'Pinned native marking model changed')
        label = f'native:{donor:08x}/pose{pose}/cell{cell[0]},{cell[1]}'
        faces.extend(decode_model(raw, cell, label, native_reference=True, pose=pose))
        signatures.append({'model': f'{donor:08x}', 'pose': pose, 'world_cell': list(cell),
                           'decompressed_s3d_sha256': sha(raw), 'rendered_by': 'unchanged-native-socket'})
    provenance = {'build': portable_path(native_build, 'external-native-build'),
        'input_audit_sha256': sha(audit_raw), 'donor_filename': archive['filename'],
        'donor_archive_sha256': sha(archive_bytes), 'private_native_archive_path_omitted': True}
    return faces, signatures, provenance


class SurfaceIndex:
    def __init__(self, faces):
        self.faces = faces
        self.tree = STRtree([face['geometry'] for face in faces])

    def at(self, point, height, texture=None):
        records = []
        xy = Point(*point)
        for i in self.tree.query(box(point[0]-2e-6, point[1]-2e-6, point[0]+2e-6, point[1]+2e-6)):
            face = self.faces[int(i)]
            if (texture is not None and face['texture'] != texture) or face['geometry'].distance(xy) > 2e-6:
                continue
            actual = np.array([*point, 1.]) @ face['fields']
            if abs(actual[0]-height) <= .02:
                records.append((face, actual))
        return records

    def visible(self, point, height):
        return not self.occluders(point, height)

    def occluders(self, point, height):
        xy = Point(*point)
        result = []
        for i in self.tree.query(xy):
            face = self.faces[int(i)]
            if not face['geometry'].covers(xy):
                continue
            actual_height = float(np.array([*point, 1.]) @ face['fields'][:, 0])
            if height+2e-5 < actual_height < height+2.:
                result.append({'model': face['model'], 'mesh': face['mesh'], 'height_m': actual_height})
        return result


def sample_rgb(image, uv):
    x, y = 128.*uv[0]-.5, 128.*uv[1]-.5
    ix, iy = math.floor(x), math.floor(y)
    a, b = x-ix, y-iy
    return ((1-a)*(1-b)*image[iy % 128, ix % 128] + a*(1-b)*image[iy % 128, (ix+1) % 128]
            + (1-a)*b*image[(iy+1) % 128, ix % 128] + a*b*image[(iy+1) % 128, (ix+1) % 128])


def cross_section(index, images, provenance, point, tangent, texture, reach):
    tangent = np.asarray(tangent, dtype=float)
    tangent /= np.linalg.norm(tangent)
    left = np.array([-tangent[1], tangent[0]])
    base = {'point_enh_m': [float(v) for v in point], 'travel_tangent_en': list(map(float, tangent)),
            'driver_left_normal_en': list(map(float, left))}
    centre_faces = [(face, values) for face, values in index.at(point[:2], point[2], texture) if face['pavement']]
    if not centre_faces:
        return {**base, 'scored': False, 'reason': 'No matching actual saved pavement under this PATH sample'}
    derivatives = [float(left @ face['fields'][:2, 1]) for face, _values in centre_faces]
    # The actual pinned yellow pixels are high-U. Their direction must agree
    # with the left normal computed from actual directed saved PATH points.
    require(all(value > 1e-5 for value in derivatives),
            f'Saved pavement places high-U yellow driver-right at {base["point_enh_m"]}; derivatives={derivatives}')
    hits, probes = [], []
    search = LineStringForQuery(point[:2], left, reach)
    for number in index.tree.query(search):
        face = index.faces[int(number)]
        if not face['pavement'] or face['texture'] != texture:
            continue
        matrix = face['fields']
        u0 = float(np.array([*point[:2], 1.]) @ matrix[:, 1])
        du = float(left @ matrix[:2, 1])
        if abs(du) < 1e-10:
            continue
        lo, hi = sorted((u0-reach*du, u0+reach*du))
        for yellow_u in provenance[texture]['yellow_uv_pixel_centres']:
            for repeat in range(math.floor(lo)-1, math.ceil(hi)+1):
                offset = (yellow_u+repeat-u0)/du
                if abs(offset) > reach:
                    continue
                xy = point[:2]+offset*left
                if not face['geometry'].covers(Point(*xy)):
                    continue
                actual = np.array([*xy, 1.]) @ matrix
                rgba = sample_rgb(images[texture], actual[1:])
                blockers = index.occluders(xy, float(actual[0])) if abs(actual[0]-point[2]) <= .02 else []
                probes.append({'driver_left_offset_m': float(offset), 'height_m': float(actual[0]),
                    'uv': list(map(float, actual[1:])), 'rgb': list(map(float, rgba[:3])),
                    'model': face['model'], 'mesh': face['mesh'], 'occluders': blockers,
                    'rendered_by': face['rendered_by'],
                    'matches_requested_deck': bool(abs(actual[0]-point[2]) <= .02)})
                if abs(actual[0]-point[2]) > .02 or blockers:
                    continue
                if is_yellow(rgba) and rgba[3] > 200:
                    hits.append({'driver_left_offset_m': float(offset), 'point_enh_m': [float(xy[0]), float(xy[1]), float(actual[0])],
                        'uv': [float(v) for v in actual[1:]], 'sampled_rgb': [float(v) for v in rgba[:3]],
                        'model': face['model'], 'mesh': face['mesh'], 'material_sha256': face['material_sha256']})
                    hits[-1]['rendered_by'] = face['rendered_by']
    if not hits:
        return {**base, 'scored': False, 'reason': 'No visible pinned yellow texel inside actual saved pavement at this cross-section',
                'left_u_derivatives': derivatives, 'yellow_texel_surface_probes': probes}
    require(all(hit['driver_left_offset_m'] > .05 for hit in hits), 'Actual saved yellow paint is visible on driver-right')
    return {**base, 'scored': True, 'left_u_derivatives': derivatives,
            'yellow_samples': hits}


def LineStringForQuery(point, left, reach):
    from shapely.geometry import LineString
    return LineString([point-reach*left, point+reach*left])


def station_sample(points, fraction):
    lengths = np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1)
    stations = np.r_[0., np.cumsum(lengths)]
    station = fraction*stations[-1]
    index = min(len(lengths)-1, int(np.searchsorted(stations, station, side='right')-1))
    ratio = (station-stations[index])/lengths[index]
    point = points[index]+ratio*(points[index+1]-points[index])
    tangent = points[index+1, :2]-points[index, :2]
    return point, tangent/np.linalg.norm(tangent), float(station)


def nearest_other(point, routes, name):
    distances = []
    for other_name, points in routes.items():
        if other_name == name:
            continue
        start, delta = points[:-1], np.diff(points, axis=0)
        lengths2 = np.sum(delta[:, :2]**2, axis=1)
        fraction = np.clip(np.sum((point[:2]-start[:, :2])*delta[:, :2], axis=1)/lengths2, 0., 1.)
        nearest = start+fraction[:, None]*delta
        selected = np.abs(nearest[:, 2]-point[2]) < .2
        if selected.any():
            distances.append(float(np.linalg.norm(nearest[selected, :2]-point[:2], axis=1).min()))
    return min(distances, default=1000.)


def audit_surfaces(faces, routes, images, provenance, allow_incomplete=False):
    index = SurfaceIndex(faces)
    journeys, native_ends = [], []
    for name in NAMES:
        scored, excluded = [], []
        for fraction in np.linspace(.2, .8, 13):
            point, tangent, station = station_sample(routes[name], float(fraction))
            separation = nearest_other(point, routes, name)
            if separation < 6.25:
                excluded.append({'station_m': station, 'reason': 'Another saved journey at the same deck is within6.25m; fork/merge ownership is ambiguous'})
                continue
            result = cross_section(index, images, provenance, point, tangent, MIS, 3.25)
            result.update(station_m=station, source_fraction=float(fraction), nearest_other_same_height_route_m=separation)
            (scored if result['scored'] else excluded).append(result)
        require(allow_incomplete or len(scored) >= 3, f'{name}: fewer than three unambiguous actual saved MIS yellow cross-sections')
        journeys.append({'journey': name, 'coverage_satisfied': len(scored) >= 3,
                         'scored_cross_sections': scored, 'excluded_candidate_cross_sections': excluded})
    for arm in 'ABC':
        members = defaultdict(list)
        for name, points in routes.items():
            for endpoint, tangent in ((points[0], points[1, :2]-points[0, :2]),
                                      (points[-1], points[-1, :2]-points[-2, :2])):
                if np.linalg.norm(endpoint[:2]-ARM_POINTS[arm]) < 6.:
                    members[round(float(endpoint[2]), 3)].append((endpoint, tangent/np.linalg.norm(tangent)))
        require(set(members) == {7.5, 15.}, 'Native marking coverage lacks a real saved deck')
        for height, rows in sorted(members.items()):
            require(len(rows) == 2 and float(rows[0][1] @ rows[1][1]) > .999999,
                    'Native marking cross-section is not a complete same-direction two-lane deck')
            centre = (rows[0][0]+rows[1][0])/2.
            tangent = rows[0][1]+rows[1][1]
            unit = tangent/np.linalg.norm(tangent)
            left = np.array([-unit[1], unit[0]])
            lane_offsets = [float((row[0][:2]-centre[:2]) @ left) for row in rows]
            scored, excluded = [], []
            for station in (.75, 1.5, 2.25):
                point = centre+np.array([*INWARD[arm], 0.])*station
                result = cross_section(index, images, provenance, point, tangent, DD, 9.)
                if result['scored']:
                    clearance = min(hit['driver_left_offset_m'] for hit in result['yellow_samples'])-max(lane_offsets)
                    require(clearance > .05, f'{arm}/{height}: native yellow is not left of BOTH actual saved lanes')
                    result['yellow_left_of_leftmost_saved_lane_m'] = clearance
                result.update(coreward_station_m=station)
                (scored if result['scored'] else excluded).append(result)
            require(allow_incomplete or len(scored) >= 2, f'{arm}/{height}: native DD end lacks two actual yellow-marking cross-sections')
            native_ends.append({'arm': arm, 'height_m': height, 'saved_lane_members': 2,
                               'saved_lane_offsets_from_carriageway_centre_m': lane_offsets,
                               'coverage_satisfied': len(scored) >= 2,
                               'scored_cross_sections': scored, 'excluded_candidate_cross_sections': excluded})
    return {'passed': all(row['coverage_satisfied'] for row in [*journeys, *native_ends]),
        'directed_journeys_checked': len(journeys), 'native_arm_deck_ends_checked': len(native_ends),
        'journeys': journeys, 'native_ends': native_ends}


def portable_path(path, external_label):
    """Keep report paths portable; never export a personal absolute location."""
    path = Path(path).resolve()
    return path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else external_label


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--saved', type=Path, required=True,
                        help='Frozen folder with the three reversed component S3D/PATH subfolders')
    parser.add_argument('--native-build', type=Path, required=True,
                        help='Build whose actual input-audit.json identifies the unchanged native DD archive')
    parser.add_argument('--output', type=Path, required=True, help='New JSONC audit report')
    parser.add_argument('--texture-cache', type=Path, default=ROOT/'local/cache/y-junction-markings',
                        help='Ignored cache for the two exact native FSH textures')
    parser.add_argument('--plugins', type=Path,
                        help='Read-only texture source; defaults to local settings if cache inputs are absent')
    args = parser.parse_args()
    folder, native_build = args.saved.resolve(), args.native_build.resolve()
    require(folder.is_dir() and native_build.is_dir(), 'Saved candidate and native build must be existing directories')
    require(not args.output.exists(), 'Choose an unused output report to preserve earlier evidence')
    images, provenance = textures(args.texture_cache, args.plugins)
    faces, routes, signatures = load_saved(folder)
    require(len(signatures) == 42 and len({row['path'] for row in signatures}) == 42,
            'The complete saved candidate must bind exactly 21 model and 21 PATH inputs')
    native_faces, native_signatures, native_input = native_socket_contributions(native_build)
    result = audit_surfaces([*faces, *native_faces], routes, images, provenance)
    controls = []
    for texture, label in ((MIS, 'Reverse actual encoded MIS U while retaining saved PATHs'),
                           (DD, 'Reverse actual encoded DD U while retaining saved PATHs')):
        changed, same_routes, current_signatures = load_saved(folder, reverse_texture=texture)
        require(current_signatures == signatures, 'Saved model or PATH inputs changed during the marking audit')
        try:
            audit_surfaces([*changed, *native_faces], same_routes, images, provenance)
        except ValueError as error:
            controls.append({'control': label, 'rejected': True, 'reason': str(error), 'saved_files_modified': False})
        else:
            raise ValueError('Wrong-side encoded UV control unexpectedly passed')
    require(all(sha((folder/row['path']).read_bytes()) == row['sha256'] for row in signatures),
            'Saved model or PATH inputs changed before the marking report was completed')
    result.update({'schema_version': 1, 'audit_helper_sha256': sha(Path(__file__).read_bytes()),
        'input_kind': 'saved-s3d-path-candidate', 'saved_candidate_files_checked': True,
        'saved_folder': portable_path(folder, 'external-saved-candidate'),
        'native_build_input': native_input,
        'path_redaction': 'Personal native archive paths are omitted; inputs outside the library use explicit external labels. Source and measured bytes are unchanged.',
        'encoded_model_and_path_inputs': signatures,
        'unchanged_native_socket_model_inputs': native_signatures,
        'native_texture_inputs': list(provenance.values()), 'negative_controls': controls,
        'method': 'Actual saved indexed S3D triangle planes/UV/materials, actual unchanged native socket S3Ds in their measured poses, saved directed PATHs, finite cross-section texel positions, and repeat/bilinear sampling of pinned native RGB pixels; no geometry or UV writer callbacks.',
        'scope': 'At least three unambiguous interior MIS cross-sections per journey and two native DD cross-sections per arm/deck; this is sampled orientation evidence, not complete paint continuity or game rendering.',
        'unsampled_scope': ['Forks and merges with another same-height route within 6.25 m',
                            'Route portions outside the 20–80 percent station range',
                            'Cross-sections with no visible yellow stripe, recorded as excluded',
                            'Complete pixel continuity over junction fans, shoulder tapers, and native-to-MIS transitions'],
        'game_appearance_tested': False, 'installed': False})
    header = ('// title: "Reversed Y actual saved driver-left yellow audit"\n'
              '// summary: "Bind sampled yellow stripe positions to actual encoded models, saved car directions, and pinned native texture pixels."\n'
              '// Used when: Reviewing the reversed candidate before installation.\n'
              '// Read by: Contributors and independent saved-resource reviewers.\n'
              '// Updated by: domains/highway/tools/verify_y_junction_markings.py against a frozen saved candidate.\n'
              '// Affects: Sampled driver-left marking evidence only; no game result is asserted.\n')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(header+json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'passed': result['passed'], 'journeys': len(result['journeys']),
                      'native_ends': len(result['native_ends']), 'controls_rejected': len(controls),
                      'report': portable_path(args.output, 'external-audit-report')}))


if __name__ == '__main__':
    main()
