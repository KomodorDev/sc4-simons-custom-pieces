"""Authoring controls for native-width, joined, and curve-anchored slip paint."""
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]

from scp_highway.ramp_geometry import compact_ramps, highway_coordinates
from scp_highway import slip_lanes as paint


def squared_distance(point, first, last):
    dx,dy = last[0]-first[0],last[1]-first[1]
    fraction = min(1.,max(0.,((point[0]-first[0])*dx+(point[1]-first[1])*dy)/(dx*dx+dy*dy)))
    return (point[0]-first[0]-fraction*dx)**2+(point[1]-first[1]-fraction*dy)**2


def local_point(vertex, ramp):
    data = paint.profile(ramp)
    u,v = highway_coordinates((vertex[0],-vertex[2],vertex[1]))
    return ((u-data['u0'])*data['direction'],v*data['side'])


class SlipLaneMarkingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ramps = compact_ramps()

    def test_all_straight_strokes_have_the_native_quarter_metre_core(self):
        for ramp in self.ramps:
            for a,b in (((0.,1.),(3.,5.)),((2.,4.5),(4.,4.5))):
                with self.subTest(ramp=ramp['id'],a=a,b=b):
                    points = [local_point(p,ramp) for f in paint._stripe(ramp,a,b) for p in f]
                    length = math.dist(a,b); normal = (-(b[1]-a[1])/length,(b[0]-a[0])/length)
                    offsets = [(p[0]-a[0])*normal[0]+(p[1]-a[1])*normal[1] for p in points]
                    self.assertAlmostEqual(max(offsets)-min(offsets),.25,places=10)

    def test_native_edge_and_gore_share_one_axis_after_lane_change(self):
        for ramp in self.ramps:
            with self.subTest(ramp=ramp['id']):
                layout = paint.marking_layout(ramp); data = paint.profile(ramp)
                self.assertEqual(layout['dashes'][0][0][0],8. if ramp['deck']=='lower' else 12.)
                self.assertEqual(layout['dashes'][-1][1][0],18. if ramp['deck']=='lower' else 26.)
                for first,last in layout['dashes']:
                    self.assertGreaterEqual(first[0],.65*data['taper_m'])
                    self.assertEqual((first[1],last[1]),(4.5,4.5))
                self.assertEqual(layout['gore_outline'][0],(data['join_s'],4.5))

    def test_gore_nose_follows_the_accepted_auxiliary_curve(self):
        for ramp in self.ramps:
            with self.subTest(ramp=ramp['id']):
                nose = paint.marking_layout(ramp)['gore_nose']
                self.assertAlmostEqual(nose[0],18.8766204161424 if ramp['deck']=='lower' else 28.1274721841987,places=9)
                self.assertEqual(nose[1],4.5)
                self.assertGreater(nose[0],paint.profile(ramp)['departure_s'])

    def test_outer_connector_is_monotone_and_joins_the_saved_native_tangent(self):
        for ramp in self.ramps:
            with self.subTest(ramp=ramp['id']):
                layout = paint.marking_layout(ramp); controls = layout['outer_controls']
                points = paint._bezier_paint(controls)
                self.assertTrue(all(a[0]<b[0] and a[1]<=b[1] for a,b in zip(points,points[1:])))
                self.assertEqual(controls[0][1],7.); self.assertEqual(controls[-1][1],8.)
                self.assertAlmostEqual(controls[-1][0]-controls[0][0],4.)
                self.assertEqual(controls[0][1],controls[1][1])
                self.assertGreaterEqual(controls[0][0],paint.profile(ramp)['taper_m'])
                expected = paint.MIS_PAINT_HANDOFFS[ramp['id']][0]
                actual = tuple((points[-1][axis]-points[-2][axis])/.25 for axis in (0,1))
                for value,target in zip(actual,expected[1:]): self.assertAlmostEqual(value,target,places=10)

    def test_inner_handoff_has_measured_clearance_and_preserves_native_tangent(self):
        for ramp in self.ramps:
            with self.subTest(ramp=ramp['id']):
                controls = paint.marking_layout(ramp)['inner_controls']
                station,tx,ty = paint.MIS_PAINT_HANDOFFS[ramp['id']][1]
                self.assertEqual(controls[0][1],7.); self.assertEqual(controls[-1][1],8.)
                self.assertAlmostEqual((station-controls[-1][0])*ty,.03125,places=10)
                dx,dy = controls[-1][0]-controls[-2][0],controls[-1][1]-controls[-2][1]
                self.assertAlmostEqual(dy/dx,ty/tx,places=10)

    def test_hatches_are_parallel_and_the_full_core_keeps_clear_of_borders(self):
        for ramp in self.ramps:
            with self.subTest(ramp=ramp['id']):
                layout = paint.marking_layout(ramp)
                self.assertEqual(len(layout['hatches']),2 if ramp['deck']=='lower' else 4)
                for first,last in layout['hatches']:
                    self.assertAlmostEqual(first[0]-last[0],last[1]-first[1],places=10)
                    self.assertGreaterEqual(math.dist(first,last),.5)
                    corners = [local_point(p,ramp) for f in paint._stripe(ramp,first,last) for p in f]
                    for corner in corners:
                        self.assertGreaterEqual(corner[1]-4.5-.125,.125-1e-8)
                        distance = min(squared_distance(corner,a,b) for a,b in zip(layout['gore_inner'],layout['gore_inner'][1:]))
                        self.assertGreaterEqual(math.sqrt(distance)-.125,.125-1e-5)

    def test_paint_stays_on_the_native_plane_and_does_not_mutate_the_ramps(self):
        before = deepcopy(self.ramps)
        for ramp in self.ramps:
            data = paint.profile(ramp)
            for triangle in paint.surfaces([ramp]):
                if abs(triangle[0][3]-paint.WHITE)>1e-8: continue
                for vertex in triangle:
                    self.assertAlmostEqual(vertex[1],ramp['height_m']+.01,places=10)
                    self.assertLessEqual(local_point(vertex,ramp)[1],8.+1e-8)
            asphalt = [f for f in paint.surfaces([ramp]) if abs(f[0][3]-paint.ASPHALT)<1e-8]
            expected = paint._polygon(ramp,((0.,paint.SEPARATOR_V),(data['join_s'],paint.SEPARATOR_V),
                                            (data['join_s'],paint.SHOULDER_OUTER_V),(0.,paint.SHOULDER_OUTER_V)))
            self.assertEqual(asphalt,expected)
        self.assertEqual(before,self.ramps)


if __name__ == '__main__':
    unittest.main()
