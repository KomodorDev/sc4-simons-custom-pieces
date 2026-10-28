"""Physical rail deck tests use an original fixture, independent of NAM files."""
from __future__ import annotations

import math
import struct
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file()) / 'framework'))
from scp.models import parse_s3d, pack_s3d, validate_s3d
from scp_hsr.rail_geometry import build_geometry, build_tiled_geometry
from scp_hsr.single_track_models import _normal
from scp_hsr.test_support import donor, triangles


def vertices(raw):
    return [vertex for triangle in triangles(raw) for vertex in triangle]


class RailGeometryTests(unittest.TestCase):
    def setUp(self):
        self.native = donor()
        self.straight = {'points': [(0, -8, 15.5), (0, 8, 15.5)], 'width': 15}

    def test_two_track_profile_preserves_native_width_heights_and_material(self):
        result = build_geometry(self.native, [self.straight], supports=False)
        points = vertices(result)
        self.assertAlmostEqual(min(point[0] for point in points), -7.5)
        self.assertAlmostEqual(max(point[0] for point in points), 7.5)
        self.assertAlmostEqual(min(point[1] for point in points), 14)
        self.assertAlmostEqual(max(point[1] for point in points), 17)
        self.assertEqual(parse_s3d(result)['materials'], parse_s3d(self.native)['materials'])
        self.assertTrue(validate_s3d(parse_s3d(result))['all_vertex_indices_valid'])
        self.assertEqual(self.native, donor())

    def test_ground_profile_uses_audited_fifteen_metre_translation(self):
        deck = {'points': [(0, -8, 1), (0, 8, 1)], 'width': 15}
        result = build_geometry(self.native, [deck], ground=True)
        points = vertices(result)
        self.assertAlmostEqual(min(point[1] for point in points), -1)
        self.assertAlmostEqual(max(point[1] for point in points), 2)
        self.assertTrue(any(abs(point[1] - 1.2) < 1e-5 for point in points))
        # Ground pieces do not acquire pillars even when supports=True.
        self.assertFalse(any(abs(point[0]) <= .65 and point[1] == 0 for point in points))

    def test_single_track_uses_only_one_native_texture_band(self):
        deck = {'points': self.straight['points'], 'width': 7.5, 'source_lane': 2}
        result = build_geometry(self.native, [deck], supports=False)
        bed = [vertex for triangle in triangles(result) if all(abs(v[1] - 16.2) < 1e-5 for v in triangle) for vertex in triangle]
        self.assertTrue(bed)
        # Original one-track rail ribbon U=.4375..5625 remains intact;
        # non-rail floor uses the existing ballast patchU=.57..65.
        self.assertAlmostEqual(min(vertex[3] for vertex in bed), .4375, places=5)
        self.assertAlmostEqual(max(vertex[3] for vertex in bed), .65, places=5)
        self.assertTrue(any(abs(vertex[3] - .5625) < 1e-5 for vertex in bed))
        self.assertAlmostEqual(min(point[0] for point in vertices(result)), -3.75)
        self.assertAlmostEqual(max(point[0] for point in vertices(result)), 3.75)

    def test_graded_deck_matches_both_native_endpoint_profiles(self):
        deck = {'points': [(0, -8, 1), (0, 0, 8.25), (0, 8, 15.5)],
                'width': 15, 'transition': True}
        result = build_geometry(self.native, [deck], supports=False)
        points = vertices(result)
        low = [point[1] for point in points if abs(point[2] - 8) < 1e-5]
        high = [point[1] for point in points if abs(point[2] + 8) < 1e-5]
        self.assertAlmostEqual(min(low), -1)
        self.assertAlmostEqual(max(low), 2)
        self.assertAlmostEqual(min(high), 14)
        self.assertAlmostEqual(max(high), 17)
        # The slab and parapets follow the grade rather than staying flat.
        middle = [point[1] for point in points if abs(point[2]) < 1e-5]
        self.assertTrue(any(abs(height - 8.7) < 1e-5 for height in middle))

    def test_same_height_overlap_has_no_duplicate_coplanar_bed_area(self):
        east_west = {'points': [(-8, 0, 15.5), (8, 0, 15.5)], 'width': 15}
        result = build_geometry(self.native, [self.straight, east_west], supports=False)
        bed = [triangle for triangle in triangles(result) if all(abs(v[1] - 16.2) < 1e-5 for v in triangle)]
        area = sum(abs(_normal(triangle)[1]) / 2 for triangle in bed)
        # Each15x16m slab has hidden concrete fill below the parapets. Opening
        # the walls reveals a continuous floor:240+240-15x15=255m².
        self.assertAlmostEqual(area, 255, places=4)

    def test_crossing_at_separate_heights_keeps_both_beds(self):
        lower = {'points': [(-8, 0, 1), (8, 0, 1)], 'width': 15}
        # Ground calibration belongs to the complete call; assigning the low
        # deck atransition endpoint makes the mixed-height comparison explicit.
        lower['transition'] = True
        result = build_geometry(self.native, [self.straight, lower], supports=False)
        bed = [triangle for triangle in triangles(result)
               if max(v[1] for v in triangle) - min(v[1] for v in triangle) < 1e-5
               and abs(triangle[0][1] - 16.2) < 1e-5]
        self.assertAlmostEqual(sum(abs(_normal(triangle)[1]) / 2 for triangle in bed), 240, places=4)
        self.assertTrue(any(abs(point[1] - 1.2) < 1e-5 for point in vertices(result)))

    def test_junction_removes_blocking_interior_parapets(self):
        branch = {'points': [(2, -8, 15.5), (2.5, -4, 15.5), (4, -1, 15.5), (8, 0, 15.5)],
                  'width': 7.5}
        result = build_geometry(self.native, [self.straight, branch], supports=False)
        # Branch walls wholly inside the dual mainline are removed. There
        # must still be a concrete outer profile elsewhere in the model.
        wall_vertices = [point for triangle in triangles(result)
                         if max(v[1] for v in triangle) - min(v[1] for v in triangle) > .1
                         for point in triangle]
        self.assertTrue(wall_vertices)
        self.assertTrue(any(abs(point[0]) > 7 for point in wall_vertices))
        self.assertTrue(validate_s3d(parse_s3d(result))['all_vertex_indices_valid'])

    def test_analytic_tangents_match_adjacent_curve_sections(self):
        tangent = (1 / math.sqrt(2), 1 / math.sqrt(2))
        first = {'points': [(-2, -8, 15.5), (0, 0, 15.5)], 'width': 15, 'end_tangent': tangent}
        last = {'points': [(0, 0, 15.5), (8, 2, 15.5)], 'width': 15, 'start_tangent': tangent}
        def section(deck):
            return {tuple(round(point[index], 5) for index in range(3))
                    for point in vertices(build_geometry(self.native, [deck], supports=False))
                    if abs(point[0] * tangent[0] - point[2] * tangent[1]) < 1e-5}
        self.assertTrue(section(first))
        self.assertEqual(section(first), section(last))

    def test_support_reaches_ground_and_does_not_extend_above_slab(self):
        result = build_geometry(self.native, [self.straight])
        points = vertices(result)
        self.assertEqual(min(point[1] for point in points), 0)
        post = [point for point in points if abs(point[0]) < .651 and abs(point[2]) < .651]
        self.assertTrue(post)
        self.assertAlmostEqual(max(point[1] for point in post), 14)

    def test_no_degenerate_faces_are_emitted(self):
        curve = {'points': [(0, -8, 15.5), (.5, -4, 15.5), (2, 0, 15.5), (8, 4, 15.5)], 'width': 15}
        result = build_geometry(self.native, [curve], supports=False)
        for triangle in triangles(result):
            self.assertGreater(sum(value * value for value in _normal(triangle)), 1e-10)

    def test_tiled_curve_is_joined_before_grid_partition(self):
        layout = {
            (0, 0): {'decks': [{'points': [(0, -8, 15.5), (0, 8, 15.5)],
                                'width': 15, 'geometry_id': 'main',
                                'start_tangent': (0, 1), 'end_tangent': (0, 1)}]},
            (0, 1): {'decks': [{'points': [(0, -8, 15.5), (0, 8, 15.5)],
                                'width': 15, 'geometry_id': 'main',
                                'start_tangent': (0, 1), 'end_tangent': (0, 1)}]},
        }
        tiled = build_tiled_geometry(self.native, layout, supports=False)
        self.assertEqual(set(tiled), set(layout))
        area = 0
        for (x, row), raw in tiled.items():
            for triangle in triangles(raw):
                if all(abs(v[1] - 16.2) < 1e-5 for v in triangle):
                    area += abs(_normal(triangle)[1]) / 2
            self.assertTrue(validate_s3d(parse_s3d(raw))['all_vertex_indices_valid'])
        # Two contiguous15x16m floors are emitted once. The construction does
        # not retain artificial end caps or duplicate profiles at the join.
        self.assertAlmostEqual(area, 480, places=4)

    def test_diagonal_native_ports_are_covered_after_axis_clipping(self):
        tangent = (1 / math.sqrt(2), 1 / math.sqrt(2))
        layout = {(0, 0): {'decks': [{'points': [(-8, -8, 15.5), (8, 8, 15.5)],
                                     'width': 15, 'geometry_id': 'diagonal',
                                     'start_tangent': tangent, 'end_tangent': tangent}]}}
        raw = build_tiled_geometry(self.native, layout, supports=False)[(0, 0)]
        points = vertices(raw)
        self.assertGreaterEqual(min(p[0] for p in points), -8 - 1e-5)
        self.assertLessEqual(max(p[0] for p in points), 8 + 1e-5)
        self.assertGreaterEqual(min(p[2] for p in points), -8 - 1e-5)
        self.assertLessEqual(max(p[2] for p in points), 8 + 1e-5)
        # The right-hand parallel lane reaches the E boundary2.828m before
        # the centreline, rather than ending at a perpendicular end cap.
        port = (8, -(8 - 2 * math.sqrt(2)))
        bed = [triangle for triangle in triangles(raw) if all(abs(v[1] - 16.2) < 1e-5 for v in triangle)]
        def inside(triangle):
            signs = []
            for a, b in zip(triangle, triangle[1:] + triangle[:1]):
                signs.append((b[0] - a[0]) * (port[1] - a[2]) - (b[2] - a[2]) * (port[0] - a[0]))
            return min(signs) >= -1e-4 or max(signs) <= 1e-4
        self.assertTrue(any(inside(triangle) for triangle in bed))

    def test_cached_geometry_stays_independent_of_callers_and_changed_inputs(self):
        layout = {(0, 0): {'decks': [{'points': [(0, -8, 15.5), (0, 8, 15.5)],
                                     'width': 15, 'geometry_id': 'main'}]}}
        first = build_tiled_geometry(self.native, layout, supports=False)
        original = first[(0, 0)]
        first[(0, 0)] = b'caller-owned replacement'
        self.assertEqual(build_tiled_geometry(self.native, layout, supports=False)[(0, 0)], original)
        layout[(0, 0)]['decks'][0]['width'] = 7.5
        narrow = build_tiled_geometry(self.native, layout, supports=False)[(0, 0)]
        self.assertAlmostEqual(max(v[0] for v in vertices(narrow)), 3.75)
        # A different donor with the same resource identity must cause a new
        # model. Move its complete original profile upwards by one metre.
        changed = parse_s3d(self.native)
        data = bytearray(changed['vertices'][0]['data'])
        for offset in range(0, len(data), changed['vertices'][0]['stride']):
            height = struct.unpack_from('<f', data, offset + 4)[0]
            struct.pack_into('<f', data, offset + 4, height + 1)
        changed['vertices'][0]['data'] = bytes(data)
        raised = build_tiled_geometry(pack_s3d(changed), layout, supports=False)[(0, 0)]
        self.assertAlmostEqual(max(v[1] for v in vertices(raised)), 18)

    def test_invalid_decks_fail_explicitly(self):
        for decks in ([], [{'points': [(0, 0, 15.5)], 'width': 15}],
                      [{'points': [(0, 0, 1), (0, 0, 15.5)]}],
                      [{'points': [(0, 0, 15.5), (0, 8, float('nan'))]}],
                      [{'points': self.straight['points'], 'width': 10}],
                      [{'points': [(0, -8, 15.5), (0, 0, 15.5), (0, -8, 15.5)]}]):
            with self.subTest(decks=decks):
                with self.assertRaises(ValueError):
                    build_geometry(self.native, decks)


if __name__ == '__main__':
    unittest.main()
