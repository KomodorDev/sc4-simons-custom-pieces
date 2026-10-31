"""Independent tapered-mouth contracts and mutations of actual saved models."""
from copy import deepcopy
import json
import math
import os
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.models import pack_s3d, parse_s3d, positions
from scp.track_paths import S3D
from scp.verify import strict_dbpf
from scp_highway import parallel_verify as verify
from scp_highway.modular_assembly_verify import _triangle_distance


class GroundMouthContractTests(unittest.TestCase):
    def test_literal_cubic_widths_and_reversed_entry_station(self):
        points = [(-1., 0., 0.), (0., 0., 0.), (.75, 0., 0.), (1.5, 0., 0.),
                  (2.25, 0., 0.), (3., 0., 0.), (4., 0., 0.)]
        off = {'points': points, 'direction': 'off',
               'segments': [{'kind': 'ground-right-quarter-turn', 'start_index': 1, 'end_index': 5}]}
        expected = [6., 6., 5.609375, 4.75, 3.890625, 3.5, 3.5]
        self.assertEqual(verify._ground_widths(off, verify.GROUND_MOUTH_PROFILE), expected)
        on = {'points': list(reversed(points)), 'direction': 'on',
              'segments': [{'kind': 'ground-right-quarter-turn', 'start_index': 1, 'end_index': 5}]}
        self.assertEqual(verify._ground_widths(on, verify.GROUND_MOUTH_PROFILE), list(reversed(expected)))
        self.assertEqual(verify._ground_widths(off, None), [6.] * 7)
        with self.assertRaisesRegex(ValueError, 'Unknown'):
            verify._ground_widths(off, 'unknown-profile')

    def test_frozen_real_grade_cut_and_every_elevated_point_stay_six_metres(self):
        for ramp in verify.approved_candidate()['routes']:
            widths = verify._ground_widths(ramp, verify.GROUND_MOUTH_PROFILE)
            turn = next(row for row in ramp['segments'] if row['kind'] == 'ground-right-quarter-turn')
            cut = turn['start_index'] if ramp['direction'] == 'off' else turn['end_index']
            with self.subTest(ramp=ramp['id']):
                self.assertEqual(widths[cut], 6.)
                self.assertTrue(all(width == 6. for point, width in zip(ramp['points'], widths) if point[2] > 0.))
                self.assertEqual(widths[-1 if ramp['direction'] == 'off' else 0], 3.5)
                self.assertEqual(verify._ground_widths(ramp, None), [6.] * len(widths))

    def test_two_terminal_markers_are_explicit_consistent_and_not_inferred(self):
        pieces = {key: {'geometry_key': 'parallel-' + key, 'engineering': {}}
                  for key in ('northwest-terminal', 'southeast-terminal')}
        scene = {'placements': [{'piece_id': key} for key in pieces]}
        self.assertIsNone(verify._assembly_ground_mouth_profile(pieces, scene))
        pieces['northwest-terminal']['engineering']['ground_mouth_profile'] = verify.GROUND_MOUTH_PROFILE
        with self.assertRaisesRegex(ValueError, 'consistent'):
            verify._assembly_ground_mouth_profile(pieces, scene)
        pieces['southeast-terminal']['engineering']['ground_mouth_profile'] = verify.GROUND_MOUTH_PROFILE
        self.assertEqual(verify._assembly_ground_mouth_profile(pieces, scene), verify.GROUND_MOUTH_PROFILE)
        pieces['southeast-terminal']['engineering']['ground_mouth_profile'] = 'unknown-profile'
        with self.assertRaisesRegex(ValueError, 'consistent'):
            verify._assembly_ground_mouth_profile(pieces, scene)

    def test_unknown_or_nonterminal_profile_is_rejected_by_individual_contract(self):
        directory = ROOT / 'domains/highway/00_pieces'
        terminal = jsonc.load(directory / 'ddrhw-parallel-northwest-terminal/piece.jsonc')
        bad = deepcopy(terminal)
        bad['engineering']['ground_mouth_profile'] = 'unknown-profile'
        with self.assertRaisesRegex(ValueError, 'unknown or misplaced'):
            verify._source_origin(bad)
        crossing = jsonc.load(directory / 'ddrhw-parallel-crossing/piece.jsonc')
        crossing['engineering']['ground_mouth_profile'] = verify.GROUND_MOUTH_PROFILE
        with self.assertRaisesRegex(ValueError, 'unknown or misplaced'):
            verify._source_origin(crossing)


class SavedNativeGroundMouthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        supplied = os.environ.get('SCP_TEST_PARALLEL_GROUND_MOUTHS_BUILD')
        cls.build = (Path(supplied).expanduser() if supplied else
                     ROOT / 'dist/ddrhw-parallel-diamond-pedestrian-mouths-01')
        if not cls.build.is_absolute():
            cls.build = ROOT / cls.build
        if not (cls.build / 'manifest.json').is_file():
            raise unittest.SkipTest('Saved revised parallel ground-mouth build is absent; set SCP_TEST_PARALLEL_GROUND_MOUTHS_BUILD to its exact directory.')
        cls.manifest = json.loads((cls.build / 'manifest.json').read_text())
        cls.pieces = {piece['id']: piece for piece in cls.manifest['pieces']}
        scene = jsonc.load(ROOT / 'domains/highway/01_assemblies' / verify.SUBJECT / 'assembly.jsonc')
        if verify._assembly_ground_mouth_profile(cls.pieces, scene) != verify.GROUND_MOUTH_PROFILE:
            raise ValueError('The saved candidate is an old broad-mouth build, not the explicit revised ground-mouth profile')
        cls.resources, cls.faces_by_cell = {}, {}
        for piece in cls.pieces.values():
            resources = strict_dbpf((cls.build / piece['asset_file']).read_bytes())
            cls.resources[piece['id']] = resources
            origin = verify._source_origin(piece)
            for cell, tile in zip(piece['cells'], piece['tile_ids']):
                cls.faces_by_cell[piece['id'], tuple(cell)] = verify._decode_faces(
                    resources[*S3D, int(tile, 16)], cell, origin=(16. * origin[0], -16. * origin[1]))
        cls.faces = [face for faces in cls.faces_by_cell.values() for face in faces]

    def mutated_faces(self, *, widening=False, removal_point=None):
        """Change indexed actual S3D buffers, then independently decode them."""
        piece = self.pieces['ddrhw-parallel-northwest-terminal']
        origin = verify._source_origin(piece)
        changed, count = {}, 0
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            world = cell[0] + origin[0], cell[1] + origin[1]
            model = parse_s3d(self.resources[piece['id']][*S3D, int(tile, 16)])
            frames = [frame for mesh in model['meshes'] for frame in mesh['frames']
                      if model['materials'][frame[3]]['textures'] == [0x5712000E]]
            if widening:
                for vi in {frame[0] for frame in frames}:
                    block = model['vertices'][vi]
                    data = bytearray(block['data'])
                    for at in range(0, len(data), block['stride']):
                        x, height, south = struct.unpack_from('<3f', data, at)
                        u = (x + 16. * world[0] - south - 16. * world[1]) / math.sqrt(2.)
                        if abs(height) > 1e-8 or abs(u) < 9.2:
                            continue
                        delta = math.copysign(.4 / math.sqrt(2.), u)
                        struct.pack_into('<f', data, at, x + delta)
                        struct.pack_into('<f', data, at + 8, south - delta)
                        count += 1
                    block['data'] = bytes(data)
            else:
                for vi, ii, pi, _mi in frames:
                    vertices = positions(model['vertices'][vi])
                    indices, retained = model['indices'][ii]['values'], []
                    for kind, first, size in model['primitives'][pi]:
                        self.assertEqual(kind, 0)
                        for at in range(first, first + size, 3):
                            selected = indices[at:at + 3]
                            tri = tuple((vertices[k][0] + 16. * world[0],
                                         -vertices[k][2] - 16. * world[1], vertices[k][1]) for k in selected)
                            if (all(abs(point[2]) < 1e-8 for point in tri)
                                    and _triangle_distance(removal_point, tri) < .15):
                                count += 1
                            else:
                                retained.extend(selected)
                    model['indices'][ii]['values'] = tuple(retained)
                    model['primitives'][pi] = [(0, 0, len(retained))]
            raw = pack_s3d(model)
            changed[piece['id'], tuple(cell)] = verify._decode_faces(
                raw, cell, origin=(16. * origin[0], -16. * origin[1]))
        self.assertGreater(count, 0, 'The negative control must alter real encoded pavement')
        return [face for key, faces in self.faces_by_cell.items() for face in changed.get(key, faces)]

    def test_actual_saved_profile_retains_the_cut_and_exposes_four_parallel_pedestrian_collars(self):
        report = verify.check_ground_mouths(self.faces)
        self.assertTrue(report['passed'])
        self.assertEqual((report['grade_cut_width_m'], report['Avenue_mouth_width_m'], report['taper_plan_length_m']),
                         (6., 3.5, 3.))
        self.assertGreater(report['continuous_flat_pavement_width_witnesses'], 3000)
        self.assertGreater(report['exact_width_edge_samples'], 900)
        self.assertEqual(len(report['pedestrian_parallel_collars']), 4)
        self.assertTrue(all(row['static_asphalt_overlap_m'] == 0. for row in report['pedestrian_parallel_collars']))
        self.assertFalse(report['unavoidable_driveway_crossings_removed'])

    def test_actual_saved_rounding_spans_use_the_revised_triangle_provenance(self):
        # Frozen lower-off and upper-off width witnesses end 0.107 and
        # 0.074 micrometres beyond their encoded triangles. Narrowed faces
        # can cross an old six-metre ribbon diagonal; both ribbon halves
        # need their actual ordered source triangle to pin the unchanged
        # two-micrometre finite-edge capsule certificate.
        witnesses = [((-7.345199078566459, 19.57639646779684, 0.),
                      (-7.4844013053848055, 19.71559869461519, 0.), 1e-7, 1.1e-7),
                     ((2.8195940396719057, -23.918735661771603, 0.),
                      (2.960980064458022, -23.777349636985488, 0.), 7e-8, 8e-8)]
        ground = [face for face in self.faces if face['texture'] == 0x5712000E and face['upward']
                  and all(abs(point[2]) <= 1e-8 for point in face['points'])]
        index = verify._FaceIndex(ground)
        for first, last, low, high in witnesses:
            with self.subTest(first=first):
                nearby = index.nearby(first, last)
                precision = {'admitted_road_encoding_spans': 0, 'maximum_admitted_along_route_span_m': 0.,
                             'maximum_sampled_actual_face_distance_m': 0.}
                if low == 1e-7:
                    self.assertFalse(verify._continuous_support(first, last, nearby, deepcopy(precision)))
                self.assertTrue(verify._continuous_support(first, last, nearby, precision,
                                                          ground_mouth_profile=verify.GROUND_MOUTH_PROFILE))
                self.assertGreater(precision['admitted_road_encoding_spans'], 0)
                self.assertGreater(precision['maximum_sampled_actual_face_distance_m'], low)
                self.assertLess(precision['maximum_sampled_actual_face_distance_m'], high)

    def test_a_real_saved_asphalt_widening_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'exceeds its independently approved tapered mouth'):
            verify.check_ground_mouths(self.mutated_faces(widening=True))

    def test_removing_actual_saved_ground_pavement_cannot_be_hidden_by_native_avenue(self):
        ramp = next(row for row in verify.approved_candidate()['routes'] if row['id'] == 'lower-off')
        turn = next(row for row in ramp['segments'] if row['kind'] == 'ground-right-quarter-turn')
        target = ramp['points'][turn['start_index'] + 15]
        with self.assertRaisesRegex(ValueError, 'lacks continuous authored pavement|lacks its exact width edge'):
            verify.check_ground_mouths(self.mutated_faces(removal_point=target))


if __name__ == '__main__':
    unittest.main()
