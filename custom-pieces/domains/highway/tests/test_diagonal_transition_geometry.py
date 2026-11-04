"""Portable first-cut analytical/native-boundary and ownership controls."""
import math
from pathlib import Path
import sys
import unittest

from shapely.geometry import Polygon, box

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "framework"))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp_highway import diagonal_transition_geometry as geometry
from scp_highway import diagonal_transition_layout as layout
from scp_highway import diagonal_transition_variants as variants
from scp_highway import diagonal_transition_collars as collars


class FirstCutDiagonalGeometry(unittest.TestCase):
    def assertPoint(self, actual, expected):
        self.assertLess(math.dist(actual, expected), 2e-12)

    def test_finite_native_forward_projection_gets_a_full_three_metre_collar(self):
        measured_extent = 5.656854586667169
        self.assertGreaterEqual(geometry.COLLAR - measured_extent, 3.0)
        self.assertGreater(geometry.COLLAR, 3.0 + 4.0 * math.sqrt(2.0))
        for deck, altitude in (("upper", 15.0), ("lower", 7.5)):
            self.assertEqual(geometry.height(deck, measured_extent + 3.0), altitude)

    def test_every_side_and_direction_has_the_measured_native_DD_endpoints(self):
        for key in variants.VARIANTS:
            reverse = variants.record_for(key).traffic_reversed
            paths = {p["id"]: p for p in geometry.traffic_routes(variant=key)}
            for deck, altitude in (("upper", 15.0), ("lower", 7.5)):
                for lane in (0, 1):
                    at_DD = 0 if (deck == "upper") != reverse else -1
                    north = (3.2 if lane == 0 else -3.2) * (-1 if reverse else 1)
                    if deck == "lower":
                        north = -north
                    self.assertPoint(paths[f"{deck}-lane-{lane}"]["points"][at_DD],
                                     (8.0, north, altitude))

    def test_ground_boundaries_keep_source_lane_order_and_height(self):
        for key in variants.VARIANTS:
            record = variants.record_for(key)
            rows = {p["id"]: p for p in geometry.traffic_routes(variant=key)}
            upper_axis = (-48., -88.) if record.physical_reflection else (-80., -56.)
            for deck, axis in (("upper", upper_axis), ("lower", (-64., -72.))):
                for lane in (0, 1):
                    at_ground = -1 if (deck == "upper") != record.traffic_reversed else 0
                    offset = (-3.2 if lane == 0 else 3.2) * (-1 if record.traffic_reversed else 1)
                    if deck == "lower":
                        offset = -offset
                    self.assertPoint(rows[f"{deck}-lane-{lane}"]["points"][at_ground],
                                     (axis[0] + offset, axis[1], 0.0))

    def test_all_four_actual_lane_profiles_stay_below_twenty_percent(self):
        for key in variants.VARIANTS:
            for path in geometry.traffic_routes(variant=key):
                for first, last in zip(path["points"], path["points"][1:]):
                    distance = math.dist(first[:2], last[:2])
                    self.assertGreater(distance, 0.0)
                    self.assertLessEqual(abs(last[2] - first[2]) / distance, .2)
        self.assertLess(geometry.normalized_upper_grade(), .19)

    def test_lane_cuts_and_exact_profile_breaks_survive_station_sampling(self):
        for key in variants.VARIANTS:
            for deck in ("upper", "lower"):
                for lane in (0, 1):
                    stations = geometry.lane_stations(deck, lane, variant=key)
                    self.assertEqual(len(stations), len(set(stations)))
                    self.assertTrue(set(geometry.BREAKS) - {0.0, geometry.LENGTH} <= set(stations))
                    self.assertLessEqual(max(b-a for a,b in zip(stations, stations[1:])), geometry.STEP + 1e-12)

    def test_section_normal_is_perpendicular_for_both_curve_hands(self):
        for key in variants.VARIANTS:
            for station in (0., 20., 40., 65., geometry.LENGTH):
                _centre, normal = geometry.frame("upper", station, variant=key)
                _p, derivative, _second = geometry.upper_plan(station, variant=key)
                tangent = tuple(derivative * u + d for u,d in
                                zip(geometry.TRANSVERSE_EN, geometry.LONGITUDINAL_EN))
                self.assertAlmostEqual(sum(a*b for a,b in zip(normal,tangent)), 0., places=13)
                self.assertAlmostEqual(math.hypot(*normal), 1., places=13)

    def test_unknown_or_orthogonal_variants_are_never_silently_selected(self):
        for bad in (None, True, {}, "alignment-b", "original-mirrored", "orthogonal"):
            with self.subTest(variant=bad), self.assertRaises(ValueError):
                geometry.traffic_routes(variant=bad)

    def test_complete_proposed_supports_have_positive_closed_volume_bounds(self):
        for key in variants.VARIANTS:
            supports = geometry.support_specifications(variant=key)
            self.assertEqual(len(supports), 14)
            self.assertEqual(len({s["id"] for s in supports}), 14)
            for row in supports:
                self.assertGreater(row["top_m"], row["bottom_m"])
                self.assertEqual(len(row["corners_EN_m"]), 4)
                self.assertLess(row["lateral_range_m"][0], row["lateral_range_m"][1])


class FirstCutDiagonalLayout(unittest.TestCase):
    def test_actual_staggered_DD_profile_keeps_its_free_shoulder_host(self):
        for key in variants.VARIANTS:
            self.assertIn((1,1),layout.world_cells(variant=key))
            self.assertFalse(layout.is_reserved_native_cell((1,1),variant=key))
            self.assertNotIn((1,1),layout.path_cells(variant=key))
            self.assertEqual(len(layout.world_cells(variant=key)),24)
            self.assertEqual(len(layout.model_only_cells(variant=key)),9)
            vertices=set(layout.flat_base_vertices(variant=key))
            self.assertEqual(len(vertices),39)
            parent={v:v for v in vertices}
            def find(v):
                while parent[v]!=v:v=parent[v]
                return v
            for c,r in layout.cells(variant=key):
                corners=((c,r),(c+1,r),(c,r+1),(c+1,r+1))
                for other in corners[1:]:parent[find(other)]=find(corners[0])
            self.assertEqual(len({find(v) for v in vertices}),1)

    def test_no_custom_cell_owns_any_of_the_three_native_strings(self):
        for key in variants.VARIANTS:
            owned = layout.world_cells(variant=key)
            self.assertTrue(set(layout.path_cells(variant=key)) <= set(owned))
            self.assertFalse(any(layout.is_reserved_native_cell(c, variant=key) for c in owned))
            for socket in geometry.native_socket_plan(variant=key).values():
                self.assertIn(tuple(socket["end_cell"]), owned)
                self.assertNotIn(tuple(socket["outside_cell"]), owned)

    def test_local_cells_map_back_to_real_world_centres_without_half_grid_shifts(self):
        for key in variants.VARIANTS:
            origin = layout.world_origin_cell(variant=key)
            translated = {(c+origin[0],r+origin[1]) for c,r in layout.cells(variant=key)}
            self.assertEqual(translated, set(layout.world_cells(variant=key)))
            self.assertTrue(all(type(v) is int for c in translated for v in c))
            path_world = set(layout.path_cells(variant=key))
            model_only = {(c+origin[0],r+origin[1]) for c,r in layout.model_only_cells(variant=key)}
            self.assertFalse(model_only & path_world)
            self.assertEqual(model_only | path_world, translated)

    def test_a_wrong_owned_mask_cannot_match_a_valid_diagonal_identity(self):
        for row in layout.module_catalog()["types"]:
            spec = {k: row[k] for k in ("id", "recipe", "diagonal_transition_variant",
                                       "diagonal_transition_alignment", "cells", "footprint")}
            spec["domain"] = "highway"
            self.assertEqual(layout.declaration(spec)["id"], row["id"])
            spec["cells"] = spec["cells"][:-1]
            with self.assertRaisesRegex(ValueError, "allocation"):
                layout.declaration(spec)


class FiniteDiagonalCollarInterfaces(unittest.TestCase):
    def test_common_station_section_keeps_the_complete_finite_shoulder(self):
        # A separately evaluated exact C end can be a few arithmetic ULPs
        # behind a GEOS cutting line. The actual finite shoulder is 2.34 m
        # wide; losing it must not shorten the bridge's native start ring.
        shoulder=Polygon(((0.,-8.000000874610194),
                          (1.-5e-15,-8.000000874610194),
                          (1.-5e-15,-5.65685424949238),
                          (0.,-5.65685424949238)))
        middle=box(0.,-5.65685424949238,1.,7.998586426374169)
        phases=[{'deck':'upper','geometry':shoulder,'height_m':15.},
                {'deck':'upper','geometry':middle,'height_m':15.00100040435791}]
        result=collars._phase_floor_sections(phases,'upper',(1.,0.),(0.,1.),(1.,0.,0.),1.)
        self.assertAlmostEqual(min(row[0] for row in result),-8.000000874610194,places=12)
        self.assertAlmostEqual(max(row[1] for row in result),7.998586426374169,places=12)
        self.assertEqual({row[2] for row in result},{15.,15.00100040435791})
        # A genuinely different finite end is not enlarged to reach C.
        outside=[{'deck':'upper','geometry':box(0.,-8.,1.-1e-7,8.),'height_m':15.}]
        self.assertEqual(collars._phase_floor_sections(outside,'upper',(1.,0.),(0.,1.),
                                                       (1.,0.,0.),1.),[])

    def test_nominal_roof_gets_only_its_exact_inner_rail_foot_closure(self):
        for variant in variants.VARIANTS:
            for deck,nominal in (('upper',15.),('lower',7.5)):
                with self.subTest(variant=variant,deck=deck):
                    foot=nominal+geometry.pavement_datum(deck,0.)
                    def point(s,u,h):
                        centre,normal=geometry.frame(deck,s,variant=variant)
                        return (*[centre[i]+u*normal[i] for i in range(2)],h,0.,0.)
                    def rail(u,raised_u):
                        a=point(geometry.COLLAR-2.,u,foot)
                        b=point(geometry.COLLAR,u,foot)
                        c=point(geometry.COLLAR,raised_u,foot+.328125)
                        d=point(geometry.COLLAR-2.,raised_u,foot+.328125)
                        return {'role':'barrier','deck':deck,'triangles_ENHUV':
                                [(a,b,c),(a,c,d)]}
                    patch={'deck':deck,'geometry':box(-50.,-50.,50.,50.),'height_m':nominal}
                    inner=rail(-7.170460195897805,-7.373586426533876)
                    shim=collars._inner_rail_foot_shims([inner],[patch],deck,{},variant)
                    faces=shim['triangles_ENHUV']
                    self.assertEqual(len(faces),2)
                    area=sum(math.sqrt(sum(v*v for v in collars._normal(face)))/2. for face in faces)
                    self.assertAlmostEqual(area,2.*(foot-nominal),places=12)
                    self.assertEqual(min(p[2] for face in faces for p in face),nominal)
                    self.assertEqual(max(p[2] for face in faces for p in face),foot)
                    # Already level 309 pavement and the existing outer body
                    # strip must not acquire coincident new closing panels.
                    level={**patch,'height_m':foot}
                    self.assertEqual(collars._inner_rail_foot_shims([inner],[level],deck,{},variant)
                                     ['triangles_ENHUV'],[])
                    outer=rail(-7.998585077675017,-7.779836190407716)
                    self.assertEqual(collars._inner_rail_foot_shims([outer],[patch],deck,{},variant)
                                     ['triangles_ENHUV'],[])


if __name__ == "__main__":
    unittest.main()
