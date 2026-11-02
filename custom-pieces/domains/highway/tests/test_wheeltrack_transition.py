"""Check the bounded native shoulder wear field without private image assets."""
from pathlib import Path
import math
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp_highway import ramp_geometry as geometry
from scp_highway import ramp_materials
from scp_highway import ramp_paths
from scp_highway import slip_lanes
from scp_highway.wheeltracks import NativeWheeltrackField, SAFE_DD_COLUMNS, _split_crossing_sweep
from scp.models import parse_s3d


class NativeWheeltrackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ramps = ramp_paths._procedural_geometry()[0]
        roads = list(cls.ramps) + [{'points': item['surface_points']}
                                  for item in ramp_paths.compact_access_routes(cls.ramps)]
        with patch.object(ramp_materials, 'native_materials', return_value={}):
            cls.painter = ramp_materials.NativeRoadPainter({}, roads)
        cls.field = NativeWheeltrackField(cls.ramps, cls.painter)

    def region(self, ramp, flank):
        return next(row for row in self.field.regions
                    if row['ramp_id'] == ramp['id'] and row['flank'] == flank)

    def point(self, ramp, station, q):
        data = slip_lanes.profile(ramp)
        east, north, height = geometry.world_coordinates(
            data['u0'] + data['direction'] * station, data['side'] * q, data['height'])
        return east, height, -north, 0.125, 0.25

    def centre_at_q(self, ramp, target):
        side = ramp['side']
        for first, last in zip(ramp['points'], ramp['points'][1:]):
            q0 = side * (first[1] - first[0] + 8.0) / math.sqrt(2.0)
            q1 = side * (last[1] - last[0] + 8.0) / math.sqrt(2.0)
            if (max(abs(first[2] - ramp['height_m']), abs(last[2] - ramp['height_m'])) < 1e-5
                    and min(q0, q1) - 1e-8 <= target <= max(q0, q1) + 1e-8 and abs(q1 - q0) > 1e-9):
                t = min(1.0, max(0.0, (target - q0) / (q1 - q0)))
                p = tuple(a + t * (b - a) for a, b in zip(first, last))
                return p[0], p[2], -p[1], 0.125, 0.25
        self.fail('Missing actual auxiliary PATH centre at requested q')

    def test_all_four_fields_have_explicit_ramp_deck_and_two_flank_owners(self):
        for ramp in self.ramps:
            rows = [row for row in self.field.regions if row['ramp_id'] == ramp['id']]
            self.assertEqual({row['height'] for row in rows}, {ramp['height_m']})
            self.assertEqual({row['side'] for row in rows}, {ramp['side']})
            self.assertEqual({row['flank'] for row in rows}, {-1, 1})
            self.assertEqual(len({row['owner'] for row in rows}), 1)

    def test_inner_boundary_is_neutral_across_taper_parallel_and_split(self):
        for ramp in self.ramps:
            for station in (6.0, 8.0, 12.0, 16.0, 24.0, 30.0):
                point = self.point(ramp, station, 4.5)
                for flank in (-1, 1):
                    painted = self.field.map_point(point, self.region(ramp, flank))
                    edge = SAFE_DD_COLUMNS[0 if flank < 0 else 1]
                    self.assertAlmostEqual(painted[3], (edge + 0.5) / 128.0, places=12)

    def test_q8_handoff_keeps_actual_connected_mis_phase_and_asphalt_correspondence(self):
        for ramp in self.ramps:
            point = self.centre_at_q(ramp, 8.0)
            region = self.region(ramp, 1)
            distance, lateral, _height, _owner = self.painter._frame(
                (point[0], -point[2], point[1]), region['owner'])
            column = 63.5 + 8.0 * lateral
            expected = column + 16.0 + min(1.0, max(0.0, (column - 68.0) / 6.0))
            expected = min(95.0, max(65.0, expected))
            painted = self.field.map_point(point, region)
            self.assertAlmostEqual(painted[3], (expected + 0.5) / 128.0, places=10)
            self.assertAlmostEqual(painted[4], distance / 16.0, places=12)

    def test_onset_centre_eases_each_safe_flank_without_width_singularity(self):
        for ramp in self.ramps:
            samples = []
            for index in range(21):
                point = self.centre_at_q(ramp, 4.5 + index / 20.0)
                samples.append([self.field.map_point(point, self.region(ramp, flank))[3]
                                for flank in (-1, 1)])
            self.assertAlmostEqual(samples[0][0], 65.5 / 128.0, places=10)
            self.assertAlmostEqual(samples[0][1], 95.5 / 128.0, places=10)
            self.assertLess(max(abs(a[0] - b[0]) for a, b in zip(samples, samples[1:])), 0.02)
            self.assertLess(max(abs(a[1] - b[1]) for a, b in zip(samples, samples[1:])), 0.02)
            self.assertTrue(all(b[0] >= a[0] - 1e-9 for a, b in zip(samples, samples[1:])))
            self.assertTrue(all(b[1] <= a[1] + 1e-9 for a, b in zip(samples, samples[1:])))

    def test_remap_retains_plane_area_winding_and_never_interpolates_across_opposite_edges(self):
        ramp = next(ramp for ramp in self.ramps if ramp['id'] == 'upper-off')
        polygon = [self.point(ramp, station, q)
                   for station, q in ((16.0, 4.5), (18.0, 4.5), (18.0, 8.0), (16.0, 8.0))]
        polygon = list(geometry._triangulate(polygon, (0.0, 1.0, 0.0))[0])
        source_area = geometry._normal(polygon)[1] / 2.0
        faces = [face for part in self.field.remap_polygon(polygon)
                 for face in geometry._triangulate(part)]
        self.assertAlmostEqual(sum(geometry._normal(face)[1] / 2.0 for face in faces), source_area, places=8)
        self.assertTrue(all(geometry._normal(face)[1] > 0.0 for face in faces))
        self.assertTrue(all(point[1] == ramp['height_m'] for face in faces for point in face))
        mapped = [face for face in faces if all(point[3] >= 65.5 / 128.0 for point in face)]
        self.assertGreater(len(mapped), 100)
        self.assertTrue(all(65.5 / 128.0 - 1e-10 <= point[3] <= 95.5 / 128.0 + 1e-10
                            for face in mapped for point in face))
        self.assertTrue(all(not (min(p[3] for p in face) < 79.4 / 128.0
                                 and max(p[3] for p in face) > 80.6 / 128.0) for face in mapped))

    def test_nonpavement_and_outside_corridor_keep_every_original_vertex_attribute(self):
        ramp = self.ramps[0]
        outside = [self.point(ramp, station, q)
                   for station, q in ((8.0, 2.0), (10.0, 2.0), (9.0, 3.0))]
        self.assertEqual(self.field.remap_polygon(outside), [outside])
        tilted = [self.point(ramp, station, q)
                  for station, q in ((8.0, 5.0), (10.0, 5.0), (9.0, 6.0))]
        tilted[0] = (tilted[0][0], tilted[0][1] + 0.25, *tilted[0][2:])
        self.assertEqual(self.field.remap_polygon(tilted), [tilted])
        # The lower-off native road extends past source cell (2,-2).
        # Its physical top must carry the same field through that join.
        polygon = [self.point(ramp, station, q)
                   for station, q in ((19.9, 7.8), (20.3, 7.8), (20.3, 7.99), (19.9, 7.99))]
        polygon = list(geometry._triangulate(polygon, (0.0, 1.0, 0.0))[0])
        self.assertTrue(any(abs(p[2] + 32.0) > 8.0 for p in polygon))
        faces = self.field.remap_polygon(polygon)
        self.assertTrue(any(point[3] >= 65.5 / 128.0 for face in faces for point in face),
                        'Construction-cell clipping must not restore plain UVs on a physical native overhang')
        self.assertAlmostEqual(sum(geometry._normal(face)[1] / 2.0
                                   for part in faces for face in geometry._triangulate(part)),
                               geometry._normal(polygon)[1] / 2.0, places=9)

    def test_new_fragments_that_collapse_only_in_float32_are_omitted(self):
        original = ((0.0, 7.5, 0.0, 0.2, 0.0), (0.0, 7.5, 2.0, 0.2, 0.1),
                    (2.0, 7.5, 2.0, 0.2, 0.2))
        raw = geometry.pack_road_model([original], 0x5713000E)

        class ClippedSliver:
            def remap_polygon(self, polygon):
                return [polygon, [(7.25, 7.5, 0.0, 0.6, 0.0),
                                  (7.25, 7.5, 1.0, 0.6, 0.1),
                                  (7.2500001, 7.5, 1.0, 0.6, 0.2)]]

        saved, _report = geometry.cut_native_branch_openings(raw, (0, 0), (), wheeltracks=ClippedSliver())
        model = parse_s3d(saved)
        triangles = []
        for mesh in model['meshes']:
            vi, ii, pi, _mi = mesh['frames'][0]
            block = model['vertices'][vi]
            vertices = [struct.unpack_from('<5f', block['data'], offset)
                        for offset in range(0, len(block['data']), block['stride'])]
            indices = model['indices'][ii]['values']
            for _kind, first, count in model['primitives'][pi]:
                triangles.extend(tuple(vertices[index] for index in indices[offset:offset + 3])
                                 for offset in range(first, first + count, 3))
        self.assertEqual(len(triangles), 1)
        self.assertGreater(geometry._normal(triangles[0])[1], 0.0)

    def test_actual_clipped_polygon_with_collinear_leading_vertices_keeps_its_field(self):
        from scp_highway.ramp_verify import _barycentric

        # Actual lower-on input after native edge erasure: its first two
        # points differ only by arithmetic noise, while the complete upward
        # polygon has 5.008 square metres of pavement. First-three orientation
        # incorrectly skipped the field at the six-metre boundary control.
        polygon = [
            (-52.64939799386698, 7.5, 54.550602006133005, 0.23046875, 1.994974198412261),
            (-52.649397993866984, 7.5, 54.55060200613301, 0.23046875, 1.9949741984122618),
            (-40.0, 7.5, 41.25903724563513, 0.23046875, 0.8485351211900226),
            (-40.0, 7.5, 41.19409723107948, 0.23046875, 0.8456651499800428),
            (-53.00295138446025, 7.5, 54.19704861553973, 0.23046875, 1.9949741786559256),
        ]
        self.assertLess(abs(geometry._normal(polygon[:3])[1]), 1e-12)
        output = self.field.remap_polygon(polygon)
        self.assertNotEqual(output, [polygon])
        point = (-48.53941053889829, 50.17530808686311)
        samples = []
        for part in output:
            for triangle in geometry._triangulate(part):
                weights = _barycentric(point, [(p[0], p[2], p[1]) for p in triangle])
                if weights is not None and min(weights) >= -1e-7:
                    samples.append(sum(weight * p[3] for weight, p in zip(weights, triangle)))
        self.assertTrue(samples)
        self.assertTrue(all(abs(u - 65.5 / 128.0) < 3e-5 for u in samples))
        downward = list(reversed(polygon))
        self.assertEqual(self.field.remap_polygon(downward), [downward])
        vertical = [(0.0, 7.5, 0.0, 0.2, 0.3), (0.0, 8.5, 0.0, 0.2, 0.3),
                    (0.0, 8.5, 2.0, 0.2, 0.3)]
        self.assertEqual(self.field.remap_polygon(vertical), [vertical])

    def test_folded_sweeps_keep_two_exact_lobes_without_filling_their_hull(self):
        polygon = [(x, 7.5, z, 0.0, 0.0) for x, z in ((0.0, 0.0), (2.0, 2.0),
                                                      (0.0, 2.0), (2.0, 0.0))]
        parts = _split_crossing_sweep(polygon)
        self.assertEqual(len(parts), 2)
        self.assertTrue(all(len(part) == 3 for part in parts))
        self.assertTrue(all(part[0] == (1.0, 7.5, 1.0, 0.0, 0.0) for part in parts))
        self.assertAlmostEqual(sum(abs(geometry._normal(part)[1]) / 2.0 for part in parts), 2.0)
        from scp_highway.ramp_verify import _barycentric
        for point, expected in (((1.0, 0.25), True), ((1.0, 1.75), True), ((0.25, 1.0), False)):
            contained = any(min(_barycentric(point, [(p[0], p[2], p[1]) for p in part])) >= -1e-10
                            for part in parts)
            self.assertEqual(contained, expected)
        for region in self.field.regions:
            boundary = region['boundary']
            for index, point in enumerate(boundary):
                a, b = boundary[index - 1], boundary[(index + 1) % len(boundary)]
                cross = ((point[0] - a[0]) * (b[1] - point[1])
                         - (point[1] - a[1]) * (b[0] - point[0]))
                self.assertGreaterEqual(cross, -1e-9, 'Every field clip kernel must actually be convex')

    def test_actual_lower_grey_triangle_witnesses_receive_the_route_field(self):
        from scp_highway.ramp_verify import _barycentric
        cases = [
            ((-42.745589920237094, 41.68518587909168),
             [(-43.67544603347778, 7.5, 40.95171546936035, 0.026073725894093513, 0.9973865151405334),
              (-42.28834676742554, 7.5, 42.288347244262695, 0.14644700288772583, 0.9951561093330383),
              (-41.86140584945679, 7.5, 41.861406326293945, 0.14644700288772583, 0.9574195146560669)]),
            ((-42.404761012596424, 41.8982039463671),
             [(-43.67544603347778, 7.5, 40.95171546936035, 0.026073725894093513, 0.9973865151405334),
              (-42.28834676742554, 7.5, 42.288347244262695, 0.14644700288772583, 0.9951561093330383),
              (-41.86140584945679, 7.5, 41.861406326293945, 0.14644700288772583, 0.9574195146560669)]),
            ((41.77039310600184, -42.57517546641676),
             [(41.728065490722656, 7.5, -42.12730264663696, 0.12880302965641022, 2.0367212295532227),
              (42.05532455444336, 7.5, -42.53016757965088, 0.1254616379737854, 2.0044541358947754),
              (40.95171546936035, 7.5, -43.67544603347778, 0.026073725894093513, 2.002612590789795)]),
        ]
        for point, polygon in cases:
            samples = []
            for part in self.field.remap_polygon(polygon):
                for triangle in geometry._triangulate(part):
                    weights = _barycentric(point, [(p[0], p[2], p[1]) for p in triangle])
                    if weights is not None and min(weights) >= -1e-7:
                        samples.append(sum(weight * p[3] for weight, p in zip(weights, triangle)))
            self.assertTrue(samples)
            self.assertTrue(all(65.5 / 128.0 <= u <= 95.5 / 128.0 for u in samples),
                            'The captured grey wedge lies in a folded ribbon lobe, not outside the route field')

    def test_original_shared_diagonal_encodes_continuous_path_support_in_all_rotations(self):
        from scp_highway.ramp_verify import _covered, _rotate

        # Actual failed parts-03 saved top faces around its 0.842 micrometre
        # crack. The two source tiles rounded the same original x=z boundary
        # to opposite sides. The encoded PATH is independently fixed.
        first = (6.798609651, -6.76597993, 7.5)
        last = (6.644203695, -6.786187562, 7.5)
        captured = [
            ((1, 0), ((6.798609733581543, -6.765979766845703), (6.865012168884277, -6.757944107055664), (6.7985076904296875, -6.765170097351074))),
            ((1, 0), ((6.799261093139648, -6.771150588989258), (6.865012168884277, -6.757944107055664), (6.798609733581543, -6.765979766845703))),
            ((1, 0), ((6.798609733581543, -6.765979766845703), (6.769502639770508, -6.769502639770508), (6.769756317138672, -6.769755840301514))),
            ((1, 0), ((6.798609733581543, -6.765979766845703), (6.7985076904296875, -6.765170097351074), (6.768437385559082, -6.768437385559082))),
            ((1, 0), ((6.798609733581543, -6.765979766845703), (6.768437385559082, -6.768437385559082), (6.769502639770508, -6.769502639770508))),
            ((1, 0), ((6.799261093139648, -6.771150588989258), (6.798609733581543, -6.765979766845703), (6.769756317138672, -6.769755840301514))),
            ((1, 0), ((6.799261093139648, -6.771150588989258), (6.769756317138672, -6.769755840301514), (6.774031639099121, -6.774030685424805))),
            ((0, 1), ((6.632931709289551, -6.703924179077148), (6.6442036628723145, -6.786187171936035), (6.69570779800415, -6.695708274841309))),
            ((0, 1), ((6.706979751586914, -6.777972221374512), (6.769755840301514, -6.769756317138672), (6.69570779800415, -6.695708274841309))),
            ((0, 1), ((6.6442036628723145, -6.786187171936035), (6.706979751586914, -6.777972221374512), (6.69570779800415, -6.695708274841309))),
            ((0, 1), ((6.723757743835449, -6.7947492599487305), (6.803311347961426, -6.803311347961426), (6.769755840301514, -6.769756317138672))),
            ((0, 1), ((6.706979751586914, -6.777972221374512), (6.6442036628723145, -6.786187171936035), (6.723757743835449, -6.7947492599487305))),
            ((0, 1), ((6.769755840301514, -6.769756317138672), (6.706979751586914, -6.777972221374512), (6.723757743835449, -6.7947492599487305))),
            ((0, 1), ((6.723757743835449, -6.7947492599487305), (6.6442036628723145, -6.786187171936035), (6.693657398223877, -6.861091613769531))),
            ((0, 1), ((6.6442036628723145, -6.786187171936035), (6.653880596160889, -6.856810569763184), (6.693657398223877, -6.861091613769531))),
            ((0, 1), ((6.567831993103027, -6.797122955322266), (6.6442036628723145, -6.786187171936035), (6.56769323348999, -6.796200752258301))),
            ((0, 1), ((6.56769323348999, -6.796200752258301), (6.6442036628723145, -6.786187171936035), (6.556421279907227, -6.713936805725098))),
            ((0, 1), ((6.6442036628723145, -6.786187171936035), (6.632931709289551, -6.703924179077148), (6.556421279907227, -6.713936805725098))),
            ((0, 1), ((6.650478363037109, -6.860213279724121), (6.6442036628723145, -6.786187171936035), (6.640931606292725, -6.861579895019531))),
            ((0, 1), ((6.640931606292725, -6.861579895019531), (6.6442036628723145, -6.786187171936035), (6.602745532989502, -6.867047309875488))),
            ((0, 1), ((6.6442036628723145, -6.786187171936035), (6.567831993103027, -6.797122955322266), (6.602745532989502, -6.867047309875488))),
            ((0, 1), ((6.653880596160889, -6.856810569763184), (6.6442036628723145, -6.786187171936035), (6.650478363037109, -6.860213279724121))),
        ]
        # Original donor triangles translated into the piece's frame. Their
        # shared endpoints have opposite exact 2**-21 m residuals before any
        # new clipping or subdivision, converging at the exact (8,8) corner.
        originals = {
            (1, 0): ((22.34314489364624, 7.5, -9.656854629516602, 0.0, 0.0),
                     (6.343145370483398, 7.5, 6.34314489364624, 0.0, 0.0),
                     (8.0, 7.5, 8.0, 0.0, 0.0)),
            (0, 1): ((6.34314489364624, 7.5, 6.343145370483398, 0.0, 0.0),
                     (-8.0, 7.5, 24.0, 0.0, 0.0), (8.0, 7.5, 8.0, 0.0, 0.0)),
        }
        before, after = [], []
        for cell, points in captured:
            revised = []
            before.append({'points': [(x, north, 7.5) for x, north in points], 'upward': True})
            for x, north in points:
                point = (x, 7.5, -north, 0.625, 1.2756905555725098)
                if abs(x + north) < 1.5e-6:
                    # Recover a point on its actual inherited skewed edge,
                    # before source-local float32 packing. No ideal edge is
                    # substituted until the authoring encoder runs.
                    original = originals[cell]
                    a = original[1] if cell == (1, 0) else original[0]
                    b = original[2]
                    mean = (x - north) / 2.0
                    fraction = (mean - a[0]) / (b[0] - a[0])
                    point = (mean, 7.5, a[2] + fraction * (b[2] - a[2]), *point[3:])
                result = geometry._canonical_native_diagonal_vertex(point, cell, originals[cell])
                self.assertEqual(result[1], point[1])
                self.assertEqual(result[3:], point[3:])
                self.assertLessEqual(math.dist(result[:3], point[:3]), 1e-6)
                local = struct.unpack('<5f', struct.pack('<5f', result[0] - 16.0 * cell[0],
                                      result[1], result[2] - 16.0 * cell[1], *result[3:]))
                revised.append((local[0] + 16.0 * cell[0], -local[2] - 16.0 * cell[1], local[1]))
            after.append({'points': revised, 'upward': True})
        for quarter in range(4):
            rotate_faces = lambda faces: [{**face, 'points': [_rotate(p, quarter) for p in face['points']]}
                                          for face in faces]
            self.assertFalse(_covered(_rotate(first, quarter), _rotate(last, quarter), rotate_faces(before)))
            self.assertTrue(_covered(_rotate(first, quarter), _rotate(last, quarter), rotate_faces(after)))

        outside = (6.7, 7.5, 6.6, 0.2, 0.3)
        self.assertEqual(geometry._canonical_native_diagonal_vertex(outside, (1, 0), originals[1, 0]), outside)
        no_diagonal = ((0.0, 7.5, 1.0, 0.0, 0.0), (16.0, 7.5, 17.0, 0.0, 0.0),
                       (16.0, 7.5, 1.0, 0.0, 0.0))
        self.assertEqual(geometry._canonical_native_diagonal_vertex(
            (6.7, 7.5, 6.7, 0.2, 0.3), (1, 0), no_diagonal), (6.7, 7.5, 6.7, 0.2, 0.3))


if __name__ == '__main__':
    unittest.main()
