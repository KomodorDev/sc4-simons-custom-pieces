"""Keep newly subdivided native shoulder edges watertight after float32 save."""
import math
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]

from scp_highway import ramp_verify
from scp_highway.slip_lanes import canonical_seam_vertex, canonical_native_seam_vertex


class SlipLaneEncodingTests(unittest.TestCase):
    def test_exact_failed_saved_segment_has_one_common_encoded_diagonal_edge(self):
        # Literal failing v1 saved triangles and PATH segment. Separately
        # encoded native vertices straddle a shared diagonal by one ULP.
        first = (6.798609651,-6.76597993,7.5)
        last = (6.644203695,-6.786187562,7.5)
        triangles = [((8.,-5.8574371337890625,7.5),
                      (6.343145370483398,-6.34314489364624,7.5),
                      (6.928718566894531,-6.928718566894531,7.5)),
                     ((6.34314489364624,-6.343145370483398,7.5),
                      (6.635721206665039,-8.,7.5),(8.,-8.,7.5))]
        before = [{'points':points,'upward':True} for points in triangles]
        self.assertFalse(ramp_verify._covered(first,last,before))
        repaired,max_movement = [],0.
        for triangle in triangles:
            points = []
            for east,north,height in triangle:
                encoded = canonical_seam_vertex((east,height,-north,.4,.5),(2,-3))
                x,h,z,_u,_v = struct.unpack('<5f',struct.pack('<5f',*encoded))
                point = x,-z,h
                max_movement = max(max_movement,math.dist(point,(east,north,height)))
                points.append(point)
            repaired.append({'points':points,'upward':True})
        self.assertGreater(max_movement,0.)
        self.assertLess(max_movement,2.5e-6)
        for turns in range(4):
            with self.subTest(turns=turns):
                faces = [{'points':[ramp_verify._rotate(point,turns) for point in face['points']],
                          'upward':True} for face in repaired]
                self.assertTrue(ramp_verify._covered(ramp_verify._rotate(first,turns),
                                                     ramp_verify._rotate(last,turns),faces))

    def test_vertices_outside_the_deck_seam_and_ground_vertices_stay_exact(self):
        for point in ((1.,7.5,2.,.3,.4),(6.34314537,0.,6.34314537,.3,.4)):
            self.assertEqual(canonical_seam_vertex(point,(2,-3)),point)

    def test_native_repair_requires_the_requested_deck_side_and_service_interval(self):
        point = (6.343145370483398,7.5,6.34314489364624,.4,.5)
        cell = (2,-3)
        service = (7.5,1,50.,60.)
        self.assertNotEqual(canonical_native_seam_vertex(point,cell,[service]),point)
        for services in ([],[(15.,1,50.,60.)],[(7.5,-1,50.,60.)],[(7.5,1,0.,1.)]):
            with self.subTest(services=services):
                self.assertEqual(canonical_native_seam_vertex(point,cell,services),point)

    def test_no_ramps_preserves_the_complete_native_model_bytes(self):
        from scp_highway import ramp_geometry as geometry
        road = {'points': [geometry.world_coordinates(48.,0.,7.5),
                           geometry.world_coordinates(64.,0.,7.5)],
                'width':16., 'thickness':1.,
                'barrier_profile':geometry.NATIVE_BARRIER_PROFILE,'edge_markings':False}
        for cell,raw in geometry.compile_road_tiles([road],0x5F900000).items():
            with self.subTest(cell=cell):
                result,report = geometry.cut_native_branch_openings(raw,cell,[])
                self.assertEqual(result,raw)
                self.assertFalse(report['changed'])


if __name__ == '__main__':
    unittest.main()
