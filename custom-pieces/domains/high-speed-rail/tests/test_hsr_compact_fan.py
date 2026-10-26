"""Protect current compact fan geometry, physical safety and native profiles.

These tests inspect literal source paths and isolated native-profile sweeps.
They do not compile full models, load installed plugins or claim game results.
Frozen current geometry and compiled-PATH fingerprints preserve the approved
types without loading predecessor modules or historical assembly folders.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

from scp.track_paths import encode_paths
from scp_hsr.hsr_compact_fan import (
    RECIPES, compact_info, compact_layout, compact_routes, model_inputs,
    _sweep_compact_profile, _split_corner_polygon,
    _complete_core_native_end, build_models,
)
from scp_hsr.hsr_components import _sweep_component_profile
from scp_hsr.directional_t_verify import measure_route_quality, _TURN_LIMITS
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
from scp_hsr.single_track_models import _native, _clip, _triangulate, _pack
from scp_hsr.hsr_surface_equivalence import audit_corner_equivalence
from scp_hsr.hsr_mesh import _surface_triangles
from scp_hsr.test_support import donor, triangles as encoded_triangles
from scp_hsr.directional_t import _floor_subtract

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.json').is_file())
PIECES = ROOT/'domains/high-speed-rail/00_pieces'
CORE = 'hsr_component_l2_compact_fan_diverge'
FAN = 'hsr_component_l2_paired_fan_compact_join'

# Current geometry fingerprints remain independent of production loaders.
RETAINED_GEOMETRY = {
    'hsr-component-l2-compact-fan-diverge': 'a84008816db7f0b100446608c6bde8d5bc1440c075ca99948edc84e81c51ee52',
    'hsr-component-l2-paired-fan-compact-join': 'aee65b48c132692063d6bd2845772403a078850d1cdc2cbca11762d5a6ca7696',
}


def _point(point):
    return tuple(round(value, 6) for value in point)


class CompactFanSourceTests(unittest.TestCase):
    def test_current_compact_fan_geometry_keeps_its_frozen_source_bytes(self):
        for slug, digest in RETAINED_GEOMETRY.items():
            with self.subTest(piece=slug):
                self.assertEqual(hashlib.sha256((PIECES/slug/'geometry.json').read_bytes()).hexdigest(), digest)

    def test_native_mainline_ports_and_single_branch_start_are_literal(self):
        self.assertEqual(set(RECIPES), {CORE, FAN})
        self.assertEqual(set(compact_layout(CORE)), {(0, 0), (1, 0), (2, 0)})
        routes = compact_routes(CORE)
        self.assertEqual((routes['W>E'][0], routes['W>E'][-1]),
                         ((-8., -2., 15.5), (40., -2., 15.5)))
        self.assertEqual((routes['E>W'][0], routes['E>W'][-1]),
                         ((40., 2., 15.5), (-8., 2., 15.5)))
        self.assertEqual(routes['E>N'][0], (40., 2., 15.5))
        self.assertEqual(routes['E>N'][-1], (-.562688696411044, 8., 15.5))
        branches = [(cell, route) for cell, data in compact_layout(CORE).items()
                    for route in data['routes'] if route['movement'] == 'E>N']
        self.assertEqual([cell for cell, route in branches if route['junction']], [(2, 0)])
        start = next(route for cell, route in branches if cell == (2, 0))
        self.assertEqual(start['points'][:2], [(8., 2., 15.5), (7.875, 2., 15.5)])
        self.assertEqual(start['tangent_in'], [-1., 0.])

    def test_local_fragments_form_only_the_three_permitted_directed_journeys(self):
        graph = defaultdict(set)
        for (column, row), data in compact_layout(CORE).items():
            for route in data['routes']:
                first, last = (_point((x+16*column, north-16*row, height))
                               for x, north, height in (route['points'][0], route['points'][-1]))
                graph[first].add(last)
        exits = {(-8., 2., 15.5): 'W', (40., -2., 15.5): 'E',
                 (-.562689, 8., 15.5): 'N'}
        for start, expected in {(-8., -2., 15.5): {'E'}, (40., 2., 15.5): {'W', 'N'}}.items():
            reached, pending = set(), [start]
            while pending:
                point = pending.pop()
                if point not in reached:
                    reached.add(point); pending.extend(graph[point]-reached)
            self.assertEqual({exits[point] for point in reached if point in exits}, expected)

    def test_current_branch_keeps_native_heading_height_and_strict_curve_limits(self):
        points = compact_routes(CORE)['E>N']
        self.assertEqual(points[:2], [(40., 2., 15.5), (39.875, 2., 15.5)])
        self.assertTrue(all(point[2] == 15.5 for point in points))
        # The opposite custom curved cut intentionally has nonzero curvature.
        result = measure_route_quality(points, {**_TURN_LIMITS, 'max_endpoint_curvature_per_m': .02})
        self.assertGreater(result['minimum_sampled_radius_m'], 50.)
        self.assertLess(result['maximum_curvature_change_per_m2'], .0015)

    def test_all_encoded_paths_and_supports_match_the_approved_current_types(self):
        # PATH fingerprints were captured from the approved current DATs.
        expected = {
            CORE: 'd6ead22a10b51d6c3845cb14c92f5a8a4534203f1ceed592933fa5ea941547e5',
            FAN: '85e31bb024cd8d37262ce5d2a59be39ff718bce806ba664543e64663444d45c2',
        }
        for recipe, digest in expected.items():
            fingerprints = [[list(cell), hashlib.sha256(
                encode_paths(data['routes']) if data['routes'] else EMPTY_STRUCTURAL_PATH
            ).hexdigest()] for cell, data in compact_layout(recipe).items()]
            self.assertEqual(hashlib.sha256(json.dumps(fingerprints, separators=(',', ':')).encode()).hexdigest(), digest)
        self.assertEqual(compact_info(FAN)['support_centers'],
                         [(48., 0.), (48., -16.), (48., -32.), (40., -46.),
                          (56., -46.), (32., -64.), (64., -64.)])
        self.assertEqual(compact_info(CORE)['support_centers'], [(0., 0.), (16., 0.), (32., 0.)])

    def test_owned_contexts_agree_and_branch_collar_ends_at_the_new_native_seam(self):
        core_map, core = model_inputs(CORE)
        fan_map, fan = model_inputs(FAN)
        self.assertEqual(core['surface_decks'], fan['surface_decks'])
        self.assertEqual(core_map, {(0, 0): (8, 5), (1, 0): (9, 5), (2, 0): (10, 5)})
        self.assertTrue(set(core_map.values()).isdisjoint(fan_map.values()))
        branch = next(deck for deck in core['surface_decks'] if deck['name'] == 'native_y_right')
        self.assertEqual(branch['points'][-1], [168., -78., 15.5])
        self.assertEqual(branch['end_tangent'], [1., 0.])
        self.assertEqual(branch['shared_mainline_collar'], 'end')
        self.assertIn([0, 168., -1, -1], branch['scoped_clip_planes'])
        for config in (core, fan):
            cells = {tuple(cell) for cell, data in config['layout']}
            for x, north in config['support_centers']:
                self.assertIn((math.floor((x+8)/16), math.floor((-north+8)/16)), cells)


class CompactFanSweepSafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = _native(donor())
        _, config = model_inputs(CORE)
        cls.deck = next(deck for deck in config['surface_decks'] if deck['name'] == 'native_y_right')
        cls.before = _sweep_component_profile(cls.source, cls.deck)
        cls.after = _sweep_compact_profile(cls.source, cls.deck)

    def test_outer_corner_cannot_change_rails_clearance_or_other_surface_kinds(self):
        before_rails = [tri for kind, tri in self.before[0] if kind == 'rail']
        after_rails = [tri for kind, tri in self.after[0] if kind == 'rail']
        self.assertEqual(before_rails, after_rails)
        for kind in {kind for kind, tri in self.before[0]}-{'bed', 'underside', 'wall'}:
            self.assertEqual([tri for actual, tri in self.before[0] if actual == kind],
                             [tri for actual, tri in self.after[0] if actual == kind])
        for key in ('rail_polygons', 'clearance_polygons'):
            before = Counter(tuple(tuple(point) for point in polygon)
                             for corridor in self.before[1] for polygon in corridor.get(key, []))
            after = Counter(tuple(tuple(point) for point in polygon)
                            for corridor in self.after[1] for polygon in corridor.get(key, []))
            self.assertEqual(before, after)
        self.assertEqual(self.before[2:], self.after[2:])
        self.assertGreater(len(self.after[0]), len(self.before[0]))

    def test_triangles_crossing_the_corner_keep_the_original_outside_affine_uv(self):
        def vertex(x, z):
            return x, 16., z, .2*x+.1*z, .3*x-.1*z
        triangle = [vertex(119., 70.), vertex(122., 70.), vertex(119., 74.)]
        contract = self.deck['compact_native_corner']
        pieces = _split_corner_polygon(triangle, contract)
        self.assertTrue(any(edit for piece, edit in pieces))
        self.assertTrue(any(not edit for piece, edit in pieces))
        for piece, edit in pieces:
            for x, height, z, u, v in piece:
                self.assertAlmostEqual(u, .2*x+.1*z, places=12)
                self.assertAlmostEqual(v, .3*x-.1*z, places=12)
                if edit:
                    self.assertLessEqual(x, 120.+1e-7)
                    self.assertGreaterEqual(z, 71.-1e-7)
                else:
                    self.assertTrue(all(p[0] >= 120.-1e-7 for p in piece)
                                    or all(p[2] <= 71.+1e-7 for p in piece))

    def test_isolated_saved_sweep_preserves_continuous_uv_outside_the_ownership_strip(self):
        def cropped_model(surfaces):
            triangles = []
            for kind, triangle in surfaces:
                polygon = list(triangle)
                for axis, boundary, sign in ((0,120.,1.), (0,136.,-1.),
                                              (2,56.,1.), (2,72.,-1.)):
                    polygon = _clip(polygon, lambda p, axis=axis, boundary=boundary, sign=sign:
                                    sign*(p[axis]-boundary))
                for tri in _triangulate(polygon):
                    triangles.append(tuple((x-128.,height,z-64.,u,v) for x,height,z,u,v in tri))
            return _pack(self.source, triangles)
        report = audit_corner_equivalence(cropped_model(self.before[0]),cropped_model(self.after[0]))
        self.assertTrue(report['continuous_oriented_surface_and_affine_uv_equivalence'])
        self.assertLessEqual(report['before_to_after']['maximum_unmatched_projected_area_m2'],1e-9)
        self.assertLessEqual(report['after_to_before']['maximum_unmatched_projected_area_m2'],1e-9)

    def test_complete_native_seams_remain_clear_through_the_ownership_micrometre(self):
        # Compute only two8µm slices, not a complete module. Exact floor,
        # underside and both parapet intervals catch partial-width corner
        # leaks that one rail-centre sample would miss.
        def sliced(source,deck):
            surfaces,corridors,points,lengths = _sweep_compact_profile(source,deck)
            output=[]
            for kind,triangle in surfaces:
                for center in (120.,168.):
                    polygon=list(triangle)
                    for axis,boundary,sign in ((0,center-4e-6,1.),(0,center+4e-6,-1.),
                                               (2,72.,1.),(2,88.,-1.)):
                        polygon=_clip(polygon,lambda p,axis=axis,boundary=boundary,sign=sign:
                                      sign*(p[axis]-boundary))
                    output.extend((kind,tri) for tri in _triangulate(polygon))
            return output,corridors,points,lengths
        _,config=model_inputs(CORE)
        triangles,_=_surface_triangles(self.source,config['surface_decks'],sliced)
        def intervals(station,height):
            values=[]
            for tri in triangles:
                if any(abs(v[1]-height)>1e-7 for v in tri):
                    continue
                coordinates=[]
                for a,b in zip(tri,tri[1:]+tri[:1]):
                    if abs(a[0]-station)<1e-8:
                        coordinates.append(a[2])
                    if (a[0]-station)*(b[0]-station)<0.:
                        t=(station-a[0])/(b[0]-a[0])
                        coordinates.append(a[2]+t*(b[2]-a[2]))
                if coordinates and max(coordinates)-min(coordinates)>1e-8:
                    values.append((min(coordinates),max(coordinates)))
            result=[]
            for low,high in sorted(values):
                # Synthetic8µm slices can leave sub0.1mm clipped seams;
                # use the existing native meshing precision when joining
                # intervals, while keeping their full outside edges strict.
                if result and low<=result[-1][1]+1e-4:
                    result[-1]=(result[-1][0],max(high,result[-1][1]))
                else:result.append((low,high))
            return result
        for station in (120.,120.00000025,120.0000005,120.00000075,167.99999925,168.):
            for height,expected in ((self.source['bed_y'],[(72.5,87.5)]),
                                    (self.source['bottom'],[(72.5,87.5)]),
                                    (self.source['top'],[(72.5,74.),(86.,87.5)])):
                with self.subTest(station=station,height=height):
                    actual=intervals(station,height)
                    self.assertEqual(len(actual),len(expected),actual)
                    for got,wanted in zip(actual,expected):
                        self.assertAlmostEqual(got[0],wanted[0],places=5)
                        self.assertAlmostEqual(got[1],wanted[1],places=5)

    def test_warp_moved_into_the_train_clearance_is_rejected(self):
        unsafe = deepcopy(self.deck)
        unsafe['compact_native_corner']['north_start_s3d'] = 70.
        with self.assertRaisesRegex(ValueError, 'touches train clearance'):
            _sweep_compact_profile(self.source, unsafe)

    def test_warp_moved_onto_the_rails_is_rejected(self):
        unsafe = deepcopy(self.deck)
        unsafe['compact_native_corner']['north_start_s3d'] = 68.
        with self.assertRaisesRegex(ValueError, 'touches a rail ribbon'):
            _sweep_compact_profile(self.source, unsafe)

    def test_unmarked_profiles_use_the_existing_unmodified_sweep(self):
        ordinary = deepcopy(self.deck)
        ordinary.pop('compact_native_corner')
        self.assertEqual(_sweep_compact_profile(self.source, ordinary),
                         _sweep_component_profile(self.source, ordinary))


class CompactNativeEndCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.native = donor()
        cls.source = _native(cls.native)
        _, config = model_inputs(CORE)
        cls.deck = config['surface_decks'][0]
        faces = []
        for kind, triangle in _sweep_component_profile(cls.source, cls.deck)[0]:
            polygon = _clip(list(triangle), lambda p: p[0]-152.)
            polygon = _clip(polygon, lambda p: 168.-p[0])
            faces.extend(tuple((x-160., h, z-80., u, v) for x, h, z, u, v in tri)
                         for tri in _triangulate(polygon))
        cls.clean = _pack(cls.source, faces, preserve_encoded_triangles=True)

    def damaged(self, start=7.9999, half_width=.00005):
        # Distinct positions on three planes ensure a floor-only repair
        # cannot accidentally satisfy the underside or parapet-cap cases.
        planes = ((self.source['bed_y'], 2.), (self.source['bottom'], .5),
                  (self.source['top'], 6.5))
        faces = encoded_triangles(self.clean)
        for height, center in planes:
            rectangle = [(start, height, center-half_width, 0., 0.),
                         (8., height, center-half_width, 0., 0.),
                         (8., height, center+half_width, 0., 0.),
                         (start, height, center+half_width, 0., 0.)]
            result = []
            for face in faces:
                pieces = [list(face)]
                if all(abs(p[1]-height) < .0001 for p in face):
                    for mask in ((rectangle[0],rectangle[1],rectangle[2]),
                                 (rectangle[0],rectangle[2],rectangle[3])):
                        pieces = [part for piece in pieces
                                  for part in _floor_subtract(piece,list(mask))]
                result.extend((p[0],p[n],p[n+1]) for p in pieces for n in range(1,len(p)-1))
            faces = result
        return _pack(self.source, faces, preserve_encoded_triangles=True)

    def test_packed_completion_preserves_every_existing_face_and_is_idempotent(self):
        raw = self.damaged()
        repaired = _complete_core_native_end(self.native, raw, self.deck)
        original = Counter(encoded_triangles(raw))
        final = Counter(encoded_triangles(repaired))
        self.assertFalse(original-final)
        added = list((final-original).elements())
        self.assertTrue(added)
        for triangle in added:
            self.assertTrue(all(7.99-1e-6 <= p[0] <= 8. for p in triangle))
        self.assertEqual(_complete_core_native_end(self.native,repaired,self.deck),repaired)

    def test_three_planes_restore_continuous_native_geometry_and_their_own_uv(self):
        damaged = self.damaged()
        repaired = _complete_core_native_end(self.native,damaged,self.deck)
        added = list((Counter(encoded_triangles(repaired))-
                      Counter(encoded_triangles(damaged))).elements())
        for height in (self.source['bed_y'],self.source['bottom'],self.source['top']):
            self.assertTrue(any(all(abs(v[1]-height)<1e-4 for v in tri) for tri in added))
        # This independent continuous proof checks the original native atlas
        # field, surface orientation and full planar coverage on every plane.
        report = audit_corner_equivalence(self.clean,repaired)
        self.assertTrue(report['continuous_oriented_surface_and_affine_uv_equivalence'])

    def test_larger_missing_end_is_rejected_instead_of_hidden(self):
        with self.assertRaisesRegex(ValueError,'defect exceeds its bounded'):
            _complete_core_native_end(self.native,self.damaged(7.995,.1),self.deck)

    def test_matching_fan_never_runs_the_core_end_completion(self):
        mapping, _ = model_inputs(FAN)
        fake = tuple((cell,b'unchanged saved fan') for cell in mapping.values())
        with patch('scp_hsr.hsr_compact_fan._cached_models',return_value=fake), \
                patch('scp_hsr.hsr_compact_fan._complete_core_native_end') as completion:
            self.assertEqual(build_models(b'unused',FAN),
                             {cell:b'unchanged saved fan' for cell in mapping})
            completion.assert_not_called()


if __name__ == '__main__':
    unittest.main()
