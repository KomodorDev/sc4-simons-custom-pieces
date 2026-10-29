"""The new smooth T is direct, genuinely two-track, and deliberately at grade."""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.dont_write_bytecode=True
sys.path.insert(0,str(next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file()) / 'framework'))

from scp_hsr.directional_t import (INFO,RECIPE,build_models,build_rules,
                               directional_layout,directional_routes,
                               _flat_union,_floor_clip,_plan_area,_cached_models,_compile_models,
                               _partition_strict)
from scp.models import parse_s3d,validate_s3d
from scp_hsr.rail_feature_verify import _triangles,_weights
from scp_hsr.interchange_verify import _clearance_segments
from scp_hsr.test_support import donor


def world_triangles(models,support=None):
    for (x,row),raw in models.items():
        model=parse_s3d(raw)
        for mesh in model['meshes']:
            is_support=mesh['name'].rstrip(b'\0')==b'SCP consolidated directional support'
            if support is not None and is_support!=support:continue
            for tri in _triangles({**model,'meshes':[mesh]}):
                yield tuple((p[0]+16*x,p[1],p[2]+16*row,*p[3:]) for p in tri)


class DirectionalTTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models=build_models(donor())

    def test_exact_native_ports_six_movements_and_constant_height(self):
        paths=directional_routes()
        ports={'N':{'in':(-2.,8.,15.5),'out':(2.,8.,15.5)},
               'S':{'in':(2.,-168.,15.5),'out':(-2.,-168.,15.5)},
               'E':{'in':(104.,-78.,15.5),'out':(104.,-82.,15.5)}}
        self.assertEqual(set(paths),{'N>S','S>N','N>E','E>N','S>E','E>S'})
        for movement,points in paths.items():
            a,b=movement.split('>')
            self.assertEqual(points[0],ports[a]['in'])
            self.assertEqual(points[-1],ports[b]['out'])
            self.assertEqual({p[2] for p in points},{15.5})
            for u,v in (points[:2],points[-2:]):
                self.assertLess(min(abs(v[0]-u[0]),abs(v[1]-u[1])),1e-12)

    def test_routes_are_direct_monotone_quarter_turns(self):
        for movement,points in directional_routes().items():
            length=sum(math.dist(a,b) for a,b in zip(points,points[1:]))
            ratio=length/math.dist(points[0],points[-1])
            self.assertLessEqual(ratio,1.02 if movement in ('N>S','S>N') else 1.55)
            for axis in (0,1):
                deltas=[b[axis]-a[axis] for a,b in zip(points,points[1:])]
                self.assertTrue(all(d>=-1e-9 for d in deltas) or all(d<=1e-9 for d in deltas))
            radii=[]
            for a,b,c in zip(points,points[1:],points[2:]):
                cross=abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
                if cross>1e-8:radii.append(math.dist(a,b)*math.dist(b,c)*math.dist(a,c)/(2*cross))
            if radii:self.assertGreaterEqual(min(radii),24.)

    def test_three_physical_dual_decks_and_fresh_layouts(self):
        layout=directional_layout()
        decks=[d for data in layout.values() for d in data['decks']]
        self.assertEqual(len(decks),3)
        self.assertEqual({d['width'] for d in decks},{15.})
        self.assertTrue(all(d['precise_union'] and d['clearance_half_width']==2.6 for d in decks))
        self.assertEqual(list(layout),INFO[RECIPE]['cells'])
        self.assertEqual(INFO[RECIPE]['footprint'],(7,11))
        before=deepcopy(directional_layout())
        decks[0]['points'][0]=(123.,456.,789.)
        self.assertEqual(directional_layout(),before)

    def test_nearly_parallel_floor_clipping_never_extrapolates_or_duplicates(self):
        # Both sides are outside the same exact plane. An epsilon test
        # followed by a zero-plane intersection would fabricate a vertex
        # beyond this very short segment.
        polygon=[(0.,16.2,-5e-8,.61,0.),(1.,16.2,-2e-7,.65,0.),
                 (1.,16.2,-1.,.65,1.)]
        self.assertEqual(_floor_clip(polygon,(0.,0.,0.),(1.,0.,0.),True),[])
        triangle=[(3.,16.2,167.5,.61,0.),(3.75,16.2,167.5,.65,0.),
                  (3.,16.2,167.1514835,.61,1.)]
        result=_flat_union([tuple(triangle),tuple(reversed(triangle))])
        self.assertAlmostEqual(sum(_plan_area(list(t)) for t in result),_plan_area(triangle),places=9)
        self.assertEqual(len(result),1)

    def test_real_mesh_indices_and_donor_material_are_preserved(self):
        material=parse_s3d(donor())['materials'][0]['raw']
        for raw in self.models.values():
            model=parse_s3d(raw)
            self.assertTrue(validate_s3d(model)['all_vertex_indices_valid'])
            self.assertTrue(all(m['raw']==material for m in model['materials']))

    def test_consolidated_piers_are_reserved_well_spaced_and_touch_the_slab(self):
        centers=INFO[RECIPE]['support_centers']
        self.assertEqual(len(centers),18)
        self.assertGreaterEqual(min(math.dist(a,b) for n,a in enumerate(centers) for b in centers[n+1:]),16.)
        supports=list(world_triangles(self.models,True))
        bases=[tri for tri in supports if all(abs(p[1])<1e-7 for p in tri)]
        self.assertEqual(len(bases),2*len(centers))
        underside=[tri for tri in world_triangles(self.models,False) if all(abs(p[1]-14.)<1e-6 for p in tri)]
        for x,north in centers:
            self.assertIn((round(x/16),round(-north/16)),self.models)
            for dx in (-.65,0.,.65):
                for dz in (-.65,0.,.65):
                    self.assertTrue(any(_weights(x+dx,-north+dz,tri) for tri in underside),(x,north,dx,dz))
        self.assertEqual(max(p[1] for tri in supports for p in tri),14.)

    def test_actual_union_is_clear_for_five_metre_wide_and_high_routes(self):
        buckets=defaultdict(list)
        for tri in world_triangles(self.models):
            for x in range(math.floor((min(v[0] for v in tri)-1e-4)/4.),math.floor((max(v[0] for v in tri)+1e-4)/4.)+1):
                for z in range(math.floor((min(v[2] for v in tri)-1e-4)/4.),math.floor((max(v[2] for v in tri)+1e-4)/4.)+1):
                    buckets[x,z].append(tri)
        records=[(x,row,[(p[0]+16*x,p[1]-16*row,p[2]) for p in route['points']])
                 for (x,row),data in directional_layout().items() for route in data['routes']]
        self.assertEqual(_clearance_segments(records,buckets,half_width=2.5),sum(len(p)-1 for _,_,p in records))

    def test_construction_has_only_the_new_fixture_ids_and_four_rotations(self):
        info=INFO[RECIPE]
        rules=build_rules({'recipe':RECIPE,'cells':info['cells'],'footprint':info['footprint'],
            'tile_ids':[0x7F5FF000+0x100*x+0x10*row for x,row in info['cells']],
            'puzzle_id':'f8ff','preview_id':'7f5ffff5','effect_name':'fixture'})
        self.assertIn('AutoTileBase = 0x7F5FF000',rules)
        self.assertEqual(rules.count('Rotate = '),3)
        self.assertNotIn('Transpose',rules)
        self.assertTrue(INFO[RECIPE]['at_grade_conflicts'])


class DirectionalGeometryCacheTests(unittest.TestCase):
    def test_cache_keys_complete_layout_supports_and_native_bytes_and_returns_fresh_dict(self):
        _cached_models.cache_clear()
        native=donor()
        try:
            with patch('scp_hsr.directional_t._compile_models',return_value={(0,0):b'original'}) as compile:
                first=build_models(native)
                first[0,0]=b'changed by caller'
                self.assertEqual(build_models(native),{(0,0):b'original'})
                self.assertEqual(compile.call_count,1)
                layout=deepcopy(directional_layout())
                layout[0,0]['decks'][0]['points'][0]=(0.,-167.,15.5)
                with patch('scp_hsr.directional_t.directional_layout',return_value=layout):build_models(native)
                self.assertEqual(compile.call_count,2)
                build_models(native+b'different donor bytes')
                self.assertEqual(compile.call_count,3)
                with patch.dict(INFO[RECIPE],support_centers=[(0.,0.)]):build_models(native)
                self.assertEqual(compile.call_count,4)
                self.assertEqual(_cached_models.cache_info().maxsize,2)
                self.assertLessEqual(_cached_models.cache_info().currsize,2)
        finally:_cached_models.cache_clear()


class DirectionalNativeFloorReplacementTests(unittest.TestCase):
    def test_strict_partition_preserves_area_uv_and_unoccupied_cell_overhangs(self):
        triangle=((7.,16.2,0.,7./16,0.),(10.,16.2,0.,10./16,0.),
                  (7.,16.2,2.,7./16,2.))
        for cells in ([(0,0)],[(0,0),(1,0)]):
            pieces=_partition_strict([triangle],cells)
            self.assertAlmostEqual(sum(_plan_area(list(face)) for faces in pieces.values() for face in faces),3.)
            self.assertEqual(max(p[0]+16*cell[0] for cell,faces in pieces.items() for f in faces for p in f),10.)
            for cell,faces in pieces.items():
                for face in faces:
                    for p in face:
                        self.assertAlmostEqual(p[3],(p[0]+16*cell[0])/16)
                        self.assertAlmostEqual(p[4],p[2]+16*cell[1])
        wall=((8.,14.,0.,0.,0.),(8.,17.,0.,1.,0.),(8.,14.,2.,0.,1.))
        pieces=_partition_strict([wall],[(0,0),(1,0)])
        self.assertEqual(sum(map(len,pieces.values())),1)

    def test_native_micrometre_height_variation_does_not_retain_original_floor(self):
        # These native-sized height differences are below the donor's
        # coplanarity bound but above the erroneous one-micrometre filter.
        native=donor()
        from scp_hsr.single_track_models import _native
        height=_native(native)['bed_y']
        triangle=((1.,height,1.,.47,0.),(3.,height+1.90735e-6,1.,.53,0.),
                  (1.,height-1.90735e-6,2.,.47,1.))
        layout={(0,0):{'routes':[],'decks':[{'points':[(-8.,0.,15.5),(8.,0.,15.5)],
                   'width':15.,'geometry_id':'native-floor-test','extend_endpoints':'ports'}]}}
        with patch('scp_hsr.rail_geometry._build_triangles',return_value=[triangle]), \
             patch('scp_hsr.rail_geometry._sweep',return_value=([('rail',triangle)],[],[],[])):
            models=_compile_models(native,layout,{'support_foundation_width':1.3,'support_centers':[]})
        self.assertEqual(len(list(_triangles(parse_s3d(models[0,0])))),1)


if __name__=='__main__':unittest.main()
