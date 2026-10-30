"""Check native texture identity, marking scale, UV seams, and material flags."""
import hashlib
import math
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]

from scp import jsonc
from scp.dbpf import decompress, entries
from scp.models import parse_s3d, pack_s3d
from scp.render_meshes import assert_render_budget
from scp.paths import local_settings
from scp_highway import ramp_geometry as geometry
from scp_highway import ramp_materials as materials
from scp_highway import ramp_paths as paths
from scp_highway import ramp_verify


def portable_painter(points):
    templates = {role: geometry.road_material(iid) for role,iid in materials.TEXTURES.items()}
    with patch.object(materials, 'native_materials', return_value=templates):
        return materials.NativeRoadPainter({}, [{'points':points}])


class NativeRampUVTests(unittest.TestCase):
    def test_coalesced_ground_face_preserves_surface_and_resolves_a_turning_wheel_track(self):
        points = [(4*math.cos(index*math.pi/180),4*math.sin(index*math.pi/180),0.)
                  for index in range(91)]
        painter = portable_painter(points)
        polygon = [(-1.,0.,1.,.125,.5),(5.,0.,1.,.125,.5),
                   (5.,0.,-5.,.125,.5),(-1.,0.,-5.,.125,.5)]
        source = geometry._triangulate(polygon,(0.,1.,0.))
        subdivided = list(painter.texture_triangles(source))
        self.assertGreater(len(subdivided),2)
        self.assertAlmostEqual(sum(abs(geometry._normal(face)[1])/2 for face in subdivided),36.,places=12)
        for face in subdivided:
            self.assertGreater(geometry._normal(face)[1],0.)
            self.assertTrue(all(p[1] == 0. and -1. <= p[0] <= 5. and -5. <= p[2] <= 1. for p in face))
            self.assertTrue(all(math.dist(first[:3],last[:3]) <= 1.+1e-12
                                for first,last in zip(face,face[1:]+face[:1])))
        raw = geometry.pack_road_model(source,0x5F900000,native_painter=painter)
        model = parse_s3d(raw)
        assert_render_budget(model)
        saved = ramp_verify._triangles(raw,(0,0))
        for angle in range(5,90,5):
            point = 4*math.cos(angle*math.pi/180),4*math.sin(angle*math.pi/180),0.
            samples = []
            for face in saved:
                weights = ramp_verify._barycentric(point,face['points'])
                if weights and min(weights) >= -1e-7:
                    samples.append(sum(weight*uv[0] for weight,uv in zip(weights,face['uv'])))
            self.assertTrue(samples)
            self.assertTrue(all(abs(u-.484375) < .03 for u in samples),
                            'Saved apron corners miss the curved wheel track inside a long original face')

    def test_ground_turn_texture_has_no_phase_jump_or_fan_across_an_apron_triangle(self):
        ramps,tiles,_routes = paths._procedural_geometry()
        roads = list(ramps)+[{'points':movement['surface_points']}
                             for movement in paths.compact_access_routes(ramps)]
        templates = {role:geometry.road_material(iid) for role,iid in materials.TEXTURES.items()}
        with patch.object(materials,'native_materials',return_value=templates):
            painter = materials.NativeRoadPainter({},roads)
        checked,maximum = 0,0.0
        for cell,faces in tiles.items():
            for face in painter.texture_triangles(faces):
                if abs(face[0][3]-.125) > 1e-7 or max(p[1] for p in face) > 1e-7:
                    continue
                painted = painter.paint(face,cell)[1]
                self.assertTrue(all(.375-1e-7 <= point[3] <= .59375+1e-7 for point in painted),
                                'A ground apron must not sample native yellow or white edge paint')
                for first,last in zip(painted,painted[1:]+painted[:1]):
                    length = ((last[0]-first[0])**2+(last[2]-first[2])**2)**.5
                    if length <= 1e-7:
                        continue
                    density = ((last[3]-first[3])**2+(last[4]-first[4])**2)**.5/length
                    maximum = max(maximum,density)
                    self.assertLessEqual(density,.5,'Ground pavement UVs jump between disconnected texture phases')
                    checked += 1
        self.assertGreater(checked,1000)
        self.assertGreater(maximum,0.)

    def test_native_edge_paint_ends_continuously_before_the_ground_apron(self):
        painter = portable_painter([(0.,4.,7.5),(0.,-12.,0.)])
        observed = []
        for height in (1.5,.75,0.):
            face = ((-3.,height,3.,.125,.5),(3.,height,3.,.125,.5),(3.,height,4.,.125,.5))
            painted = painter.paint(face)[1]
            observed.append((painted[0][3],painted[1][3]))
        self.assertEqual(observed[0],(.3125,.6875))
        self.assertEqual(observed[-1],(.375,.59375))
        self.assertAlmostEqual(observed[1][0],sum((observed[0][0],observed[-1][0]))/2)
        self.assertAlmostEqual(observed[1][1],sum((observed[0][1],observed[-1][1]))/2)

    def test_the_authored_high_collar_keeps_the_same_native_pavement_as_its_ramp(self):
        painter = portable_painter([(0.,4.,7.5),(0.,-12.,7.5)])
        face = ((-1.,7.5,-4.,.125,.5),(1.,7.5,-4.,.125,.5),(1.,7.5,-3.,.125,.5))
        self.assertEqual(painter.paint(face)[0],'ramp')

    def test_missing_or_changed_native_input_cannot_fall_back_to_authored_colour(self):
        with self.assertRaisesRegex(ValueError, 'audited MIS dependency'):
            materials.native_materials({})
        with self.assertRaisesRegex(ValueError, 'slope donor changed'):
            materials.native_materials({'mis':{(0x5AD0E817,0xBADB57F1,materials.MIS_DONOR):b'changed'}})

    def test_narrow_road_preserves_native_one_lane_marking_scale(self):
        painter = portable_painter([(0.,0.,7.5),(0.,-32.,0.)])
        face = ((-3.,5.,8.,.125,.5),(3.,5.,8.,.125,.5),(3.,4.,12.,.125,.5))
        role, painted = painter.paint(face)
        self.assertEqual(role, 'ramp')
        self.assertAlmostEqual(painted[0][3], .3125)
        self.assertAlmostEqual(painted[1][3], .6875)
        self.assertAlmostEqual(painted[0][4], .5)
        self.assertAlmostEqual(painted[2][4], .75)

    def test_adjacent_saved_cells_keep_exact_same_texture_phase(self):
        painter = portable_painter([(0.,0.,7.5),(0.,-32.,0.)])
        first = ((-3.,5.625,8.,.125,.5),(3.,5.625,8.,.125,.5),(3.,6.,6.,.125,.5))
        second = ((-3.,5.625,-8.,.125,.5),(3.,5.625,-8.,.125,.5),(3.,5.,-6.,.125,.5))
        a, b = painter.paint(first,(0,0))[1], painter.paint(second,(0,1))[1]
        self.assertEqual(a[0][3:], b[0][3:])
        self.assertEqual(a[1][3:], b[1][3:])

    def test_native_edge_markings_replace_old_white_and_yellow_overlays(self):
        painter = portable_painter([(0.,0.,7.5),(0.,-32.,0.)])
        for semantic in (.625,.875):
            with self.subTest(semantic=semantic):
                self.assertIsNone(painter.paint(((0.,5.,8.,semantic,.5),(1.,5.,8.,semantic,.5),
                                                 (1.,4.,12.,semantic,.5))))

    def test_barrier_and_underside_use_their_own_native_materials(self):
        painter = portable_painter([(0.,0.,7.5),(0.,-32.,7.5)])
        barrier = ((-3.,7.5,0.,.375,.5),(-2.75,8.89,0.,.375,.5),(-2.75,8.89,4.,.375,.5))
        underside = ((-3.,6.5,0.,.375,.5),(3.,6.5,0.,.375,.5),(3.,6.5,4.,.375,.5))
        column = ((-.4,0.,0.,.375,.5),(-.4,15.,0.,.375,.5),(.4,15.,0.,.375,.5))
        self.assertEqual(painter.paint(barrier)[0], 'barrier')
        self.assertEqual(painter.paint(underside)[0], 'concrete')
        self.assertEqual(painter.paint(column)[0], 'concrete')

    def test_barrier_top_keeps_the_measured_native_texture_strip(self):
        painter = portable_painter([(0.,0.,7.5),(0.,-32.,7.5)])
        top = ((-2.734375,8.890625,0.,.375,.5),(-2.4375,8.890625,0.,.375,.5),
               (-2.4375,8.890625,4.,.375,.5))
        role, painted = painter.paint(top)
        self.assertEqual(role,'barrier')
        self.assertAlmostEqual(painted[0][4],.325)
        self.assertAlmostEqual(painted[1][4],.625)

    def test_actual_packing_retains_multiple_native_materials_and_spatial_uvs(self):
        points = [(0.,0.,7.5),(0.,-16.,3.75),(0.,-32.,0.)]
        painter = portable_painter(points)
        faces = geometry.road_triangles(points, barrier_profile=geometry.NATIVE_BARRIER_PROFILE)
        model = parse_s3d(geometry.pack_road_model(faces,0x5F900000,native_painter=painter))
        used = {m['textures'][0] for m in model['materials']}
        self.assertTrue({materials.TEXTURES['ramp'],materials.TEXTURES['barrier'],
                         materials.TEXTURES['concrete']} <= used)
        self.assertNotIn(0x5F900000, used)
        self.assertTrue(all(mesh['name'].startswith(b'SCP NAM ') for mesh in model['meshes']))


class NativeRampMaterialPrivateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings = local_settings(ROOT)
        if not settings.is_file():
            raise unittest.SkipTest('Private NAM settings are unavailable')
        folder = Path(jsonc.load(settings)['plugins'])
        cls.context = {}
        for label, filename, digest in (
            ('dd_rhw','RealHighway_DD_RHW-4.dat','ccf8dabd3930fce92d0baa872ff974e3a536ddcc40762505a2e70eafcf9c0dfb'),
            ('mis','RealHighway_MIS.dat','dec1873a357cca39a5a06de3b0722757b52b72c47c33a24d269d846779dba1a8')):
            matches = list(folder.rglob(filename)) if folder.is_dir() else []
            if not matches:
                raise unittest.SkipTest('Audited native NAM ramp archives are unavailable')
            if len(matches) != 1:
                raise ValueError('Ambiguous native NAM ramp archive')
            raw = matches[0].read_bytes()
            if hashlib.sha256(raw).hexdigest() != digest:
                raise ValueError('Native NAM ramp archive changed; re-audit rather than skip')
            cls.context[label] = {key:decompress(value) for key,value in entries(raw).items()}

    def model(self):
        points = [(0.,6.,7.5),(0.,0.,3.75),(0.,-6.,0.)]
        painter = materials.NativeRoadPainter(self.context,[{'points':points}])
        faces = geometry.road_triangles(points,barrier_profile=geometry.NATIVE_BARRIER_PROFILE)
        return parse_s3d(geometry.pack_road_model(faces,0x5F900000,native_painter=painter))

    def test_saved_native_flags_and_uvs_pass_independent_material_fingerprints(self):
        model = self.model()
        faces = ramp_verify._triangles(pack_s3d(model),(0,0))
        report = ramp_verify._native_appearance(faces)
        self.assertTrue(report['spatial_uvs_checked'])
        self.assertEqual(report['owned_texture_resources'],0)

    def test_changed_native_flags_fail_even_with_correct_texture_identity(self):
        model = self.model()
        material = model['materials'][0]
        raw = bytearray(material['raw']); raw[5] ^= 1; material['raw'] = bytes(raw)
        with self.assertRaisesRegex(ValueError,'measured native NAM surface'):
            ramp_verify._native_appearance(ramp_verify._triangles(pack_s3d(model),(0,0)))

    def test_collapsed_uvs_fail_even_with_correct_native_material(self):
        model = self.model()
        for block in model['vertices']:
            raw = bytearray(block['data'])
            for offset in range(0,len(raw),block['stride']):
                struct.pack_into('<2f',raw,offset+12,.5,.5)
            block['data'] = bytes(raw)
        with self.assertRaisesRegex(ValueError,'flat colour sample'):
            ramp_verify._native_appearance(ramp_verify._triangles(pack_s3d(model),(0,0)))


if __name__ == '__main__':
    unittest.main()
