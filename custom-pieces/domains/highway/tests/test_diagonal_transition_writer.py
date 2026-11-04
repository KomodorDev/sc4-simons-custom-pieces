"""Finite slab and deterministic PATH controls for the new middle writer."""
from pathlib import Path
import math
import sys
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0,SourcePackages(ROOT))
from scp.verify import parse_paths
from scp_highway import diagonal_transition as writer
from scp_highway import diagonal_transition_geometry as geometry
from scp_highway import ramp_paths


def section(variant='original'):
    # Geometry-only fixture; it supplies no native or saved-asset acceptance.
    with patch.object(writer,'_materials',return_value={name:{'textures':[1]} for name in('body','barrier','pavement-atlas')}):
        return writer.section_factory({},1,variant=variant)


def plane_height(triangle,point):
    a,b,c=triangle
    denominator=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
    if not denominator:return None
    u=((b[1]-c[1])*(point[0]-c[0])+(c[0]-b[0])*(point[1]-c[1]))/denominator
    v=((c[1]-a[1])*(point[0]-c[0])+(a[0]-c[0])*(point[1]-c[1]))/denominator
    if min(u,v,1-u-v)<-1e-9:return None
    return u*a[2]+v*b[2]+(1-u-v)*c[2]


def at(groups,role,point):
    heights=[height for group in groups if group['role']==role for tri in group['triangles_ENHUV']
             if (height:=plane_height(tri,point)) is not None]
    if not heights:raise ValueError('No actual face covers the test point')
    return heights


class DiagonalMiddleTests(unittest.TestCase):
    def test_encoder_omits_only_exact_zero3D_float32_faces_and_preserves_tiny_or_vertical_faces(self):
        # This real double-precision triangle loses its area at the actual
        # encoded coordinate1.0; the saved vertices become identical.
        collapsed=((1.,0.,0.),(1.+2.**-30,0.,0.),(1.,2.**-30,0.))
        self.assertFalse(writer._encoded_triangle_has_area(collapsed))
        self.assertFalse(writer._encoded_triangle_has_area(((0.,0.,0.),(1.,1.,1.),(2.,2.,2.))))
        # A projected-plan-area filter would wrongly delete this finite wall.
        self.assertTrue(writer._encoded_triangle_has_area(((0.,0.,0.),(0.,0.,1.),(0.,1.,0.))))
        # Every positive encoded area remains, however small; there is no
        # numerical area threshold masquerading as a float32 cleanup.
        tiny=((0.,0.,0.),(2.**-50,0.,0.),(0.,2.**-50,0.))
        self.assertTrue(writer._encoded_triangle_has_area(tiny))

    def test_float32_inverted_native_sliver_keeps_all_vertices_and_restores_pinned_parent_winding(self):
        # Actual source03 pinned302 parent witness, expressed in local model
        # coordinates. Its positive source child becomes downward after F32.
        source=((6.619419867379989,15.,6.619419470101734,.1,.2,0.),
                (6.619429811331046,15.,6.619429414007616,.3,.4,0.),
                (6.425321755575498,15.,6.425321302388426,.5,.6,0.))
        parent=(0.,53.01935419382585,0.)
        original=writer._cross(writer._sub(source[1][:3],source[0][:3]),writer._sub(source[2][:3],source[0][:3]))
        self.assertGreater(original[1],0.)
        self.assertLess(writer._encoded_triangle_normal(source)[1],0.)
        repaired=writer._triangle_for_packing(source,parent)
        self.assertEqual(repaired,(source[0],source[2],source[1]))
        self.assertEqual(set(repaired),set(source))
        self.assertGreater(writer._encoded_triangle_normal(repaired)[1],0.)
        with self.assertRaisesRegex(ValueError,'ambiguous'):
            writer._triangle_for_packing(source,(1.,0.,0.))

    def test_curved_graded_slab_keeps_same_base_diagonal_at_the_independent_373um_witness(self):
        point=(-52.025349166247764,-27.380719315179597)
        groups=writer.middle_groups({},1,section=section(),start=62.125,end=62.25)
        roof=at(groups,'upper-pavement-atlas',point);floor=at(groups,'upper-body',point)
        self.assertTrue(all(abs(top-bottom-1.)<2e-12 for top in roof for bottom in floor))
        # Reproduce the actual former opposite-diagonal floor using independent
        # ring coordinates; this must exhibit a material thickness shortfall.
        q=[]
        for s,u in((62.125,-1.012741699796952),(62.125,-2.262741699796952),
                   (62.25,-2.262741699796952),(62.25,-1.012741699796952)):
            e,h,south=geometry.model_point('upper',s,u)
            q.append((e,-south,h+geometry.pavement_datum('upper',s)-1.))
        wrong=[value for indices in((0,1,2),(0,2,3)) if
               (value:=plane_height([q[i]for i in indices],point)) is not None]
        self.assertTrue(wrong)
        self.assertLess(min(roof)-max(wrong),.9997)

    def test_ground_clamp_has_its_own_complete_lateral_ring_and_no_zero_depth_concrete_copy(self):
        root=writer._clamp_station('lower')
        groups=writer.middle_groups({},1,section=section(),start=root-.5,end=geometry.LENGTH-geometry.COLLAR-1.)
        self.assertAlmostEqual(writer._base('lower',root),1.,places=12)
        # Just after the clamp, a real positive-depth road still has its H0 floor.
        centre,_=geometry.frame('lower',root+.25)
        floors=at(groups,'lower-body',centre)
        self.assertTrue(any(abs(value)<1e-12 for value in floors))
        ground=writer.middle_groups({},1,section=section(),start=80.,end=81.)
        lower_body=[tri for group in ground if group['role']=='lower-body' for tri in group['triangles_ENHUV']]
        self.assertEqual(lower_body,[])
        self.assertTrue([tri for group in ground if group['role']=='lower-pavement-atlas' for tri in group['triangles_ENHUV']])

    def test_each_native_endpoint_is_encoded_at_fixed9f_with_DD_or_ground_class_and_elevation(self):
        for variant in('original','mirrored','opposite-side','opposite-side-mirrored'):
            source=geometry.traffic_routes(variant=variant)
            sliced=ramp_paths.slice_routes(source)
            actual={}
            for cell,fragments in sliced.items():
                raw=writer.encode_paths(fragments,cell,variant=variant);decoded=parse_paths(raw)
                self.assertEqual(decoded['terrain'],1)
                for row in decoded['routes']:
                    for point in(row['points'][0],row['points'][-1]):
                        world=(point[0]+16*cell[0],point[1]-16*cell[1],point[2])
                        actual.setdefault(tuple(round(v,8)for v in world),[]).append(row['lane'])
            for route in source:
                for point in(route['points'][0],route['points'][-1]):
                    expected=route['lane']+(1 if point[2]==0. else 0)
                    self.assertIn(expected,actual[tuple(round(v,8)for v in point)])


if __name__=='__main__':unittest.main()
