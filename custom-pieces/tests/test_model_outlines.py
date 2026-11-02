"""Actual component silhouettes remain distinct from owned city tiles."""
from copy import deepcopy
import struct
import unittest
from PIL import Image
from scp.city_grid import make_camera
from scp.model_outlines import projected_component_masks,draw_component_outlines
from scp.models import pack_s3d
from test_render_meshes import fixture


def example():
    model=fixture(2)
    points=[(-4.,15.,4.),(20.,15.,4.),(-4.,15.,-4.),
            (-22.,15.,-22.),(-18.,15.,-22.),(-22.,15.,-18.)]
    model['vertices'][0]['data']=b''.join(struct.pack('<5f',*p,0.,0.) for p in points)
    model['indices'][0]['values']=(3,4,5,0,1,2)
    model['primitives']=[[(0,3,3)]]
    source={'label':'P01','render_mesh_indices':[0],'occupied_world_cells':[[0.,0.]]}
    camera=make_camera(points,0.,90.,500,500,bounds_world_m=(-32.,-32.,32.,32.),padding=20)
    return model,source,camera


class ActualModelOutlineTests(unittest.TestCase):
    def pixel(self,camera,east,north):
        return tuple(round(v) for v in camera.project_world(east,north))

    def test_actual_indexed_projection_extends_past_ownership_without_filling_its_rectangle(self):
        model,source,camera=example();before=pack_s3d(model)
        (_source,mask,report),=projected_component_masks(model,[source],camera,(500,500))
        self.assertEqual(mask.getpixel(self.pixel(camera,14.,-3.)),255)
        self.assertEqual(mask.getpixel(self.pixel(camera,16.,3.)),0)
        self.assertEqual(mask.getpixel(self.pixel(camera,-21.,21.)),0)
        self.assertEqual(report['indexed_triangles_projected'],1)
        self.assertGreater(report['projection_pixels_outside_owned_tiles'],0)
        self.assertEqual(pack_s3d(model),before)

    def test_coloured_model_edge_is_drawn_in_the_unowned_tile(self):
        model,source,camera=example();view=Image.new('RGB',(500,500),(31,47,63))
        result,report=draw_component_outlines(view,model,[source],camera,{'palette':{'P01':'#d5205a'}})
        self.assertEqual(result.getpixel(self.pixel(camera,14.,-4.)),(213,32,90))
        self.assertEqual(view.getpixel(self.pixel(camera,14.,-4.)),(31,47,63))
        self.assertEqual(result.getpixel(self.pixel(camera,16.,3.)),(31,47,63))
        self.assertTrue(report['shared_ownership_camera'])
        self.assertTrue(report['drawn_above_ownership_fills_and_boundaries'])

    def test_missing_duplicate_or_shared_mesh_assignments_cannot_mislabel_a_piece(self):
        model,source,camera=example()
        for sources in ([dict(source,render_mesh_indices=[])],[dict(source,render_mesh_indices=[0,0])],
                        [source,dict(source,label='P02')],[dict(source,render_mesh_indices=[1])]):
            with self.subTest(sources=sources),self.assertRaises(ValueError):
                projected_component_masks(model,sources,camera,(500,500))
