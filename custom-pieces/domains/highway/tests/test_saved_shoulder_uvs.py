"""Reject the former broad shoulder crop in actual indexed saved models."""
from copy import deepcopy
import math
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.models import pack_s3d, parse_s3d
from scp_highway import ramp_geometry as fixture_writer
from scp_highway import shoulder_uv_verify as check


def fixtures():
    owners, resources = {}, {}
    for index, (name, station, side, height) in enumerate(check.MOUTHS):
        faces = []
        for low, high, erased in ((3.8, 4.3125, False), (4.3125, 4.8125, True),
                                  (4.8125, 7.171875, False)):
            points = []
            for along, q in ((station-1., low), (station+1., low),
                             (station+1., high), (station-1., high)):
                lateral = side*q
                east = 4. + (along-lateral)/math.sqrt(2.)
                north = -4. + (along+lateral)/math.sqrt(2.)
                u = 29.5/128. if erased else .5-q/16.
                points.append((east, height, -north, u, along/16.))
            faces.extend(fixture_writer._triangulate(points, (0., 1., 0.)))
        tile = 0x7F720000 + index*0x100
        raw = fixture_writer.pack_road_model(faces, 0x5713000E)
        owners[index, 0] = {'piece_id': name, 'tile': tile, 'local_cell': (0, 0),
                            'angle': 0, 'origin': (64., -64.)}
        resources[name] = {(*check.S3D, tile+4): raw}
    return owners, resources


def mutate(raw, callback):
    model = parse_s3d(raw)
    for block in model['vertices']:
        data = bytearray(block['data'])
        for offset in range(0, len(data), block['stride']):
            point = struct.unpack_from('<5f', data, offset)
            revised = callback(point)
            struct.pack_into('<5f', data, offset, *revised)
        block['data'] = bytes(data)
    return pack_s3d(model)


class SavedShoulderUVTests(unittest.TestCase):
    def test_saved_native_asphalt_and_erased_edge_pass_at_all_four_mouths(self):
        owners, resources = fixtures()
        report = check.check_saved_shoulder_uvs(owners, resources)
        self.assertTrue(report['passed'])
        self.assertEqual(report['ramp_mouths_checked'], 4)
        self.assertEqual(report['erased_edge_samples_checked'], 12)
        self.assertGreater(report['surrounding_native_uv_polygons_checked'], 0)
        self.assertFalse(report['game_rendering_tested'])

    def test_broad_dark_crop_is_rejected_at_each_saved_mouth(self):
        owners, baseline = fixtures()
        for name in baseline:
            with self.subTest(mouth=name):
                resources = deepcopy(baseline)
                key = next(iter(resources[name]))
                resources[name][key] = mutate(resources[name][key], lambda p: (*p[:3], .36, p[4]))
                with self.assertRaisesRegex(ValueError, 'outside the erased edge'):
                    check.check_saved_shoulder_uvs(owners, resources)

    def test_original_white_edge_cannot_reappear_at_any_mouth(self):
        owners, baseline = fixtures()
        for name in baseline:
            with self.subTest(mouth=name):
                resources = deepcopy(baseline)
                key = next(iter(resources[name]))
                side = 1 if name.startswith('lower') else -1
                def original(point):
                    q = side*(-point[2]-point[0]+8.)/math.sqrt(2.)
                    return *point[:3], .5-q/16., point[4]
                resources[name][key] = mutate(resources[name][key], original)
                with self.assertRaisesRegex(ValueError, 'not erased'):
                    check.check_saved_shoulder_uvs(owners, resources)

    def test_missing_saved_shoulder_faces_cannot_pass(self):
        with self.assertRaisesRegex(ValueError, 'no surrounding native pavement'):
            check.check_faces([])


if __name__ == '__main__':
    unittest.main()
