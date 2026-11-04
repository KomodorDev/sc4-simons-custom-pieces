"""Verify the lower-deck bend's native sockets and coherent authored floor."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.dbpf import decompress, entries
from scp.paths import local_settings
from scp.preview import decode_fsh
from scp.verify import parse_paths
from scp_highway import orthogonal_approaches as approaches
from scp_highway import orthogonal_transition as writer
from scp_highway import orthogonal_transition_geometry as geometry
from scp_highway import orthogonal_transition_variants as variants
from scp_highway import ramp_paths


ATLAS = 0x7F5F7000
VARIANT = 'lower-bend-right'


def piece_spec():
    record = variants.record_for(VARIANT)
    return {'id': record.piece_id, 'recipe': record.recipe, 'domain': 'highway',
            'transition_variant': VARIANT, 'footprint': [2, 6],
            'cells': [list(cell) for cell in geometry.CELLS],
            'tile_ids': [f'{ATLAS + 0x100*x + 0x10*y:08x}' for x, y in geometry.CELLS],
            'native_orthogonal_approaches': True}


def path_resources(piece, raws):
    return {(0x296678F7, 0xA966883F, int(tile, 16)): raw
            for tile, raw in zip(piece['tile_ids'], raws, strict=True)}


def floor_height_at(point, face):
    """Interpolate height at a world X/Z point, if inside the actual triangle."""
    (ax, ah, az), (bx, bh, bz), (cx, ch, cz) = [p[:3] for p in face]
    dx, dz = point[0] - ax, point[2] - az
    ux, uz = bx - ax, bz - az
    vx, vz = cx - ax, cz - az
    det = ux * vz - vx * uz
    if abs(det) < 1e-10:
        return None
    u, v = (dx * vz - vx * dz) / det, (ux * dz - dx * uz) / det
    if min(u, v, 1.0 - u - v) < -1e-9:
        return None
    return ah + u * (bh - ah) + v * (ch - ah)


class LowerBendAuthoringTests(unittest.TestCase):
    def test_native_sockets_have_directed_deck_specific_ground_poses(self):
        piece = piece_spec()
        rows = approaches.approaches(piece)
        self.assertEqual([(row['cell'], row['end_cell'], row['native_tile_id'],
                           row['native_rotation'], row['networks'][0]['flags']) for row in rows],
                         [([1, -1], [1, 0], '57530000', 2, '04000100'),
                          ([0, 6], [0, 5], '57030000', 0, '01000001'),
                          ([1, 6], [1, 5], '57030000', 2, '00010100')])
        self.assertEqual(sum(map(len, approaches.existing_rul1_sections(piece).values())), 8)
        self.assertTrue(all(row['optional'] and tuple(row['cell']) not in geometry.CELLS for row in rows))

    def test_encoded_native_lane_phase_rejects_swapping_ground_classes(self):
        piece = piece_spec()
        routed = ramp_paths.slice_routes(geometry.traffic_routes(variant=VARIANT))
        paths = []
        for cell in geometry.CELLS:
            fragments = deepcopy(routed.get(cell, []))
            if cell[1] == 5:
                for fragment in fragments:
                    fragment['lane'] += 1
            paths.append(writer._encode_paths(fragments))
        resources = path_resources(piece, paths)
        result = approaches.check_native_boundary_paths(None, piece, resources)
        self.assertEqual(result['rotated_boundary_member_checks'], 32)
        self.assertEqual(result['native_rul2_oriented_propagation_checks'], 24)
        west = deepcopy(routed[0, 5])
        for row in west:
            row['lane'] = 2 - row['lane']
        paths[geometry.CELLS.index((0, 5))] = writer._encode_paths(west)
        with self.assertRaisesRegex(ValueError, 'socket endpoint|incompatible lane'):
            approaches.check_native_boundary_paths(None, piece, path_resources(piece, paths))

    def test_floor_clips_same_nonplanar_roof_split_at_ground_contact(self):
        # Opposite triangulation of this skewed quad gives a different plane.
        before = [(0., 1.4, 0., 0., 0., 0.), (8., 1.4, 0., 0., 0., 0.)]
        after = [(1., .6, 7., 0., 0., 0.), (7., .6, 9., 0., 0., 0.)]
        floor = writer._paired_body_strip([before, after], [(0., 8.), (0., 8.)],
                                          0., 8., (1., 0.), 1)
        roof = [(before[0], after[0], after[1]), (before[0], after[1], before[1])]
        for face in roof:
            for weights in ((.8, .1, .1), (.15, .75, .1), (.1, .15, .75)):
                point = tuple(sum(weight * vertex[axis] for weight, vertex in zip(weights, face))
                              for axis in range(3))
                contacts = [floor_height_at(point, triangle) for triangle in floor]
                contacts = [height for height in contacts if height is not None]
                self.assertTrue(contacts)
                for height in contacts:
                    self.assertAlmostEqual(height, max(0., point[1] - 1.), places=12)


class LowerBendNativeAuthoringTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = local_settings(ROOT)
        if not source.is_file():
            raise unittest.SkipTest('Original NAM 50 inputs unavailable in this source-only checkout')
        settings = jsonc.load(source)
        roots = [Path(path).expanduser() for path in (settings['plugins'], *settings.get('extra_plugins', []))]
        cls.context = {}
        for key, filename in (('controller', 'NetworkAddonMod_Controller.dat'),
                              ('dd_rhw', 'RealHighway_DD_RHW-4.dat'),
                              ('rhw4', 'RealHighway_RHW-4.dat'),
                              ('rhw4_textures', 'US_Common_RHW-4_Textures.dat')):
            inputs = {path for root in roots if root.is_dir() for path in root.rglob(filename)}
            if len(inputs) != 1:
                raise unittest.SkipTest('Exactly one original ' + filename + ' is required')
            cls.context[key] = {key: decompress(raw) for key, raw in entries(inputs.pop().read_bytes()).items()}
        cls.compiled = writer.build_channels(cls.context, texture_id=ATLAS, variant=VARIANT)

    def test_saved_native_donor_matches_all_rotations(self):
        resources = path_resources(piece_spec(), [raw for _cell, _model, raw in self.compiled])
        result = approaches.check_native_boundary_paths(self.context, piece_spec(), resources)
        self.assertEqual(result['boundary_members_checked'], 8)
        self.assertEqual(result['rotated_boundary_member_checks'], 32)
        self.assertTrue(result['native_controller_reread'])
        self.assertEqual(len(self.compiled), 12)
        self.assertTrue(all(parse_paths(raw)['terrain'] == 1 for _cell, _model, raw in self.compiled))

    def test_saved_yellow_is_driver_left_on_each_lane_with_two_uv_controls(self):
        from test_orthogonal_transition_opposite_native import marking_samples, reversed_pavement_u

        images = {iid: decode_fsh(self.context['rhw4_textures'][*writer.TEXTURE, iid]).convert('RGBA')
                  for iid in writer.TEXTURE_SHA256}
        textures = writer.build_textures(self.context, ATLAS, variant=VARIANT)
        images[ATLAS] = decode_fsh(textures[*writer.TEXTURE, ATLAS]).convert('RGBA')
        self.assertEqual(len(marking_samples(self.compiled, VARIANT, images)), 12)
        for native in (True, False):
            with self.subTest(native=native), self.assertRaisesRegex(ValueError, 'driver-left'):
                marking_samples(reversed_pavement_u(self.compiled, ATLAS, native=native), VARIANT, images)


if __name__ == '__main__':
    unittest.main()
