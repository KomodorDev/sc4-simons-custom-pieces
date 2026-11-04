"""Native endpoints and encoded texture pixels for the two new side choices."""
from collections import defaultdict
import math
from pathlib import Path
import re
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.dbpf import entries, decompress
from scp.models import parse_s3d, pack_s3d
from scp.paths import local_settings
from scp.preview import decode_fsh
from scp.verify import parse_paths
from scp_highway import orthogonal_approaches as helpers
from scp_highway import orthogonal_transition as writer
from scp_highway import orthogonal_transition_geometry as geometry
from scp_highway import orthogonal_transition_variants as variants
from scp_highway import orthogonal_transition_models_verify as reader

import numpy as np
from shapely.geometry import LineString, Point, Polygon
from shapely.strtree import STRtree


def spec(key):
    row = variants.record_for(key)
    return {'id': row.piece_id, 'recipe': row.recipe, 'domain': 'highway', 'transition_variant': key,
            'footprint': [2, 6], 'cells': [list(c) for c in geometry.CELLS],
            'tile_ids': [f'{0x7f700000+0x100*x+0x10*y:08x}' for x, y in geometry.CELLS],
            'native_orthogonal_approaches': True}


class OppositeSideAuthoringTests(unittest.TestCase):
    def test_exact_native_helper_ends_keep_the_parent_traffic_phase(self):
        expected = {
            'opposite-side': [([0, -1], 0x57530000, 0), ([0, 6], 0x57030000, 2), ([1, 6], 0x57030000, 0)],
            'opposite-side-mirrored': [([1, -1], 0x57530000, 2), ([0, 6], 0x57030000, 2), ([1, 6], 0x57030000, 0)]}
        for key, wanted in expected.items():
            with self.subTest(key=key):
                rows = helpers.approaches(spec(key))
                self.assertEqual([(r['cell'], int(r['native_tile_id'], 16), r['native_rotation']) for r in rows], wanted)
                self.assertEqual(helpers.existing_rul1_sections(spec(key)), helpers.existing_rul1_sections(spec('original')))

    def test_asymmetric_native_width_follows_traffic_pose_after_both_reflections(self):
        for key in variants.VARIANTS:
            record = variants.record_for(key)
            low, high = writer.pavement_bounds('upper', 0., variant=key)
            if record.physical_reflection: low, high = -high, -low
            expected = (-8.00100040435791, 7.999000072479248) if record.traffic_reversed else (-7.999000072479248, 8.00100040435791)
            self.assertEqual((low, high), expected)
            self.assertEqual(writer.pavement_bounds('upper', 96., variant=key), (-8., 8.))

    def test_native_phase_is_not_inferred_from_the_physical_shape(self):
        self.assertEqual(writer._native_station(3., 'opposite-side'), 3.)
        self.assertEqual(writer._native_station(3., 'opposite-side-mirrored'), 13.)
        u, v = writer._source_uv('upper', 0., 2.5, native_dd=True, variant='opposite-side')
        self.assertAlmostEqual(u, (-2.5+7.999000072479248)/16.000000476837158, places=14)
        self.assertAlmostEqual(v, -.0009999275207519531/16.000000476837158, places=14)


def decoded_routes(compiled):
    fragments = defaultdict(list)
    for (x, y), _model, raw in compiled:
        names = re.findall(rb'-- SCP ([a-z]+-lane-[01]) source_lane=', raw)
        actual = parse_paths(raw)['routes']
        if len(names) != len(actual): raise ValueError('Saved route labels are incomplete')
        for name, row in zip(names, actual):
            fragments[name.decode()].append(np.array([(p[0]+16*x, p[1]-16*y, p[2]) for p in row['points']]))
    result = {}
    for name, rows in fragments.items():
        starts = [r for r in rows if not any(r is not q and np.linalg.norm(r[0]-q[-1]) < 1e-6 for q in rows)]
        if len(starts) != 1: raise ValueError('Saved route has no unique start')
        path = list(starts[0]); pending = [r for r in rows if r is not starts[0]]
        while pending:
            found = [r for r in pending if np.linalg.norm(path[-1]-r[0]) < 1e-6]
            if len(found) != 1: raise ValueError('Saved route has an unmatched seam')
            path.extend(found[0][1:]); pending = [r for r in pending if r is not found[0]]
        result[name] = np.array(path)
    return result


def sample(image, uv):
    width, height = image.size; x, y = uv[0]*width-.5, uv[1]*height-.5
    ix, iy = math.floor(x), math.floor(y); fx, fy = x-ix, y-iy
    return tuple(sum(image.getpixel(((ix+a) % width, (iy+b) % height))[c]
                     * (fx if a else 1-fx)*(fy if b else 1-fy) for a, b in ((0, 0), (1, 0), (0, 1), (1, 1))) for c in range(4))


def yellow(rgba):
    r, g, b, a = rgba
    return r > 125 and g > 105 and b < 80 and r-b > 80 and g-b > 60 and a > 200


def marking_samples(compiled, key, images):
    """Only actual encoded XYZUV, directed PATHs, and decoded texture pixels."""
    faces = []
    for cell, model, _raw in compiled:
        for face in reader.decode_faces(model, cell, variant=key):
            if '-pavement-' not in face['role'] or reader._normal(face['points'])[2] <= 0.: continue
            vertices = np.array(face['points']); matrix = np.c_[vertices[:, :2], np.ones(3)]
            fields = np.linalg.solve(matrix, np.c_[vertices[:, 2], np.array(face['uv'])])
            faces.append((face, fields, Polygon(vertices[:, :2])))
    tree = STRtree([f[2] for f in faces]); columns = {}
    for texture, image in images.items():
        width, height = image.size
        columns[texture] = [x for x in range(width) if sum(yellow(image.getpixel((x, y))) for y in range(height)) >= max(8, height//16)]
    checked = []
    for name, points in decoded_routes(compiled).items():
        lengths = np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1); stations = np.r_[0., np.cumsum(lengths)]
        for fraction in (.01, .5, .99):
            target = fraction*stations[-1]; segment = min(len(lengths)-1, int(np.searchsorted(stations, target, side='right')-1))
            t = (target-stations[segment])/lengths[segment]; point = points[segment]+t*(points[segment+1]-points[segment])
            direction = (points[segment+1, :2]-points[segment, :2])/lengths[segment]; left = np.array([-direction[1], direction[0]])
            hits = []
            for index in tree.query(LineString((point[:2]-9*left, point[:2]+9*left))):
                face, field, polygon = faces[int(index)]
                if not face['role'].startswith(name.split('-')[0]+'-'): continue
                u0 = np.array([*point[:2], 1.]) @ field[:, 1]; du = left @ field[:2, 1]
                if abs(du) < 1e-12: continue
                image = images[face['texture']]; width = image.size[0]
                for column in columns[face['texture']]:
                    for repeat in range(math.floor(min(u0-9*du, u0+9*du))-1, math.ceil(max(u0-9*du, u0+9*du))+1):
                        offset = ((column+.5)/width+repeat-u0)/du
                        if abs(offset) > 9.: continue
                        xy = point[:2]+offset*left
                        if not polygon.covers(Point(*xy)): continue
                        h, u, v = np.array([*xy, 1.]) @ field
                        if abs(h-point[2]) <= .03 and yellow(sample(image, (u, v))): hits.append(float(offset))
            if not hits or min(hits) <= .05: raise ValueError('Encoded yellow is missing or is not driver-left')
            checked.append({'route': name, 'fraction': fraction, 'minimum_left_m': min(hits)})
    return checked


def reversed_pavement_u(compiled, atlas, *, native):
    changed = []
    for cell, raw, path in compiled:
        model = parse_s3d(raw)
        for mesh in model['meshes']:
            name = mesh['name'].rstrip(b'\0').decode()
            if '-pavement-' not in name: continue
            for vi, _ii, _pi, mi in mesh['frames']:
                is_atlas = model['materials'][mi]['textures'] == [atlas]
                if is_atlas == native: continue
                block = model['vertices'][vi]; data = bytearray(block['data'])
                origin = (2*(8 if 'upper-' in name else 264)+128)/512 if is_atlas else 1.
                for at in range(0, len(data), block['stride']):
                    u, = struct.unpack_from('<f', data, at+12); struct.pack_into('<f', data, at+12, origin-u)
                block['data'] = bytes(data)
        changed.append((cell, pack_s3d(model), path))
    return changed


class OppositeSideNativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings_path = local_settings(ROOT)
        if not settings_path.is_file(): raise unittest.SkipTest('Original NAM 50 inputs unavailable in this source-only checkout')
        settings = jsonc.load(settings_path); cls.plugins = Path(settings['plugins']).expanduser()
        roots = [cls.plugins, *(Path(p).expanduser() for p in settings.get('extra_plugins', []))]
        cls.context = {}
        for label, filename in [('controller', 'NetworkAddonMod_Controller.dat'), ('dd_rhw', 'RealHighway_DD_RHW-4.dat'),
                                ('rhw4', 'RealHighway_RHW-4.dat'), ('rhw4_textures', 'US_Common_RHW-4_Textures.dat')]:
            found = {p for root in roots if root.is_dir() for p in root.rglob(filename)}
            if len(found) != 1: raise unittest.SkipTest('Exactly one original '+filename+' is required')
            cls.context[label] = {k: decompress(v) for k, v in entries(found.pop().read_bytes()).items()}
        cls.compiled, cls.images, cls.atlases = {}, {}, {}
        for key in ('opposite-side', 'opposite-side-mirrored'):
            piece = jsonc.load(ROOT/'domains/highway/00_pieces'/variants.record_for(key).piece_id/'piece.jsonc')
            atlas = int(piece['authored_texture_ids'][0], 16); cls.atlases[key] = atlas
            cls.compiled[key] = writer.build_channels(cls.context, texture_id=atlas, variant=key)
            owned = writer.build_textures(cls.context, atlas, variant=key)
            cls.images[key] = {iid: decode_fsh(cls.context['rhw4_textures'][*writer.TEXTURE, iid]).convert('RGBA') for iid in writer.TEXTURE_SHA256}
            cls.images[key][atlas] = decode_fsh(owned[*writer.TEXTURE, atlas]).convert('RGBA')

    def test_actual_native_endpoints_classes_and_markers_in_all_four_rotations(self):
        for key, compiled in self.compiled.items():
            piece = spec(key)
            resources = {(0x296678f7, 0xa966883f, int(tile, 16)): raw for tile, (_cell, _model, raw) in zip(piece['tile_ids'], compiled)}
            result = helpers.check_native_boundary_paths(self.context, piece, resources)
            self.assertEqual(result['rotated_boundary_member_checks'], 32)
            self.assertEqual(result['boundary_members_checked'], 8)
            self.assertEqual([r['lane_classes'] for r in result['sockets']], [[0, 1], [1, 2], [1, 2]])

    def test_decoded_saved_pavement_pixels_are_driver_left_at_both_native_ends_and_middle(self):
        for key, compiled in self.compiled.items():
            with self.subTest(key=key): self.assertEqual(len(marking_samples(compiled, key, self.images[key])), 12)

    def test_wrong_side_encoded_native_uv_control_rejects(self):
        for key, compiled in self.compiled.items():
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, 'driver-left'):
                marking_samples(reversed_pavement_u(compiled, self.atlases[key], native=True), key, self.images[key])

    def test_wrong_side_encoded_atlas_uv_control_rejects(self):
        for key, compiled in self.compiled.items():
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, 'driver-left'):
                marking_samples(reversed_pavement_u(compiled, self.atlases[key], native=False), key, self.images[key])

    def test_both_legacy_cell_models_paths_and_atlas_match_actual_installed_dat(self):
        for key in ('original', 'mirrored'):
            identifier = variants.record_for(key).piece_id
            piece = jsonc.load(ROOT/'domains/highway/00_pieces'/identifier/'piece.jsonc')
            dat = self.plugins/'zzz_Simons_Custom_Pieces/20_Pieces'/('SCP_'+identifier+'.dat')
            if not dat.is_file(): self.skipTest('Retained installed legacy DAT unavailable for byte comparison')
            actual = {k: decompress(v) for k, v in entries(dat.read_bytes()).items()}
            atlas = int(piece['authored_texture_ids'][0], 16)
            for tile, (cell, model, raw) in zip(piece['tile_ids'], writer.build_channels(self.context, texture_id=atlas, variant=key)):
                iid = int(tile, 16)
                self.assertEqual(actual[0x296678f7, 0xa966883f, iid], raw)
                for zoom in range(5): self.assertEqual(actual[0x5ad0e817, 0xbadb57f1, iid+zoom], model)
            self.assertEqual(actual[*writer.TEXTURE, atlas], writer.build_textures(self.context, atlas, variant=key)[*writer.TEXTURE, atlas])


if __name__ == '__main__': unittest.main()
