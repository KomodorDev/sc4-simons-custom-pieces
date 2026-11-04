"""Portable texture-partition controls, independent of the Y model writer."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

import numpy as np
from shapely.geometry import Point, Polygon, box
from shapely.ops import unary_union

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp_highway.y_junction_surface_uv import NativePaintJoin, RibbonMarkings, flat_surface_domains


def road(owner, points, normals, stations):
    points, normals = np.array(points, dtype=float), np.array(normals, dtype=float)
    return {'id': owner, 'points': points, 'normals': normals, 'station': np.array(stations, dtype=float),
            'rail_low': points[:, :2] - 3. * normals, 'rail_high': points[:, :2] + 3. * normals}


def ribbon(route):
    return unary_union([Polygon([route['rail_low'][i], route['rail_low'][i + 1],
                                 route['rail_high'][i + 1], route['rail_high'][i]])
                        for i in range(len(route['points']) - 1)])


def at(domains, point):
    return [domain for domain in domains if domain['geometry'].distance(Point(point)) < 1e-9]


class FlatSurfaceUVTests(unittest.TestCase):
    def assert_partition(self, domains, original):
        total = unary_union([domain['geometry'] for domain in domains])
        self.assertLess(total.symmetric_difference(original).area, 1e-9)
        self.assertAlmostEqual(sum(domain['geometry'].area for domain in domains), original.area, places=8)

    def test_full_native_mouth_and_taper_keep_one_exact_affine_field_beyond_three_metres(self):
        routes = [road('left', [(0, -2.5, 15), (20, -2.5, 15)], [(0, 1)] * 2, [0, 20]),
                  road('right', [(0, 2.5, 15), (20, 2.5, 15)], [(0, 1)] * 2, [0, 20])]
        mouth = box(0, -8, 11, 8).union(Polygon([(11, -8), (13, -5), (13, 5), (11, 8)]))
        asphalt = unary_union([mouth, *map(ribbon, routes)]).difference(box(1, -1, 3, 1))
        coefficients = np.array([[0., 1. / 16.], [1. / 16., 0.], [.5, 0.]])
        profiles = {('A', 'upper'): {'coefficients': coefficients}}
        domains = flat_surface_domains(asphalt, routes, 'upper', profiles,
                                       [{'arm': 'A', 'deck': 'upper', 'geometry': mouth}])
        self.assert_partition(domains, asphalt)
        for point in ((8, 0), (11.5, 0), (12.5, 1)):
            selected = at(domains, point)
            self.assertTrue(selected)
            for domain in selected:
                self.assertEqual(domain['owner'], 'native-A')
                self.assertEqual(domain['material_role'], 'pavement-native-A-upper')
                self.assertEqual(domain['uv'](point), (.5 + point[1] / 16., point[0] / 16.))

    def test_route_ownership_is_fixed_before_vertex_mapping_and_input_order_does_not_change_it(self):
        routes = [road('south', [(0, -2, 15), (20, -2, 15)], [(0, 1)] * 2, [0, 20]),
                  road('north', [(0, 2, 15), (20, 2, 15)], [(0, 1)] * 2, [0, 20])]
        asphalt = unary_union(list(map(ribbon, routes)))
        first = flat_surface_domains(asphalt, routes, 'upper', {}, [])
        second = flat_surface_domains(asphalt, list(reversed(routes)), 'upper', {}, [])
        self.assert_partition(first, asphalt)
        self.assertTrue(all(domain['maximum_edge_m'] is None for domain in first))
        for owner in ('south', 'north'):
            a = unary_union([domain['geometry'] for domain in first if domain['owner'] == owner])
            b = unary_union([domain['geometry'] for domain in second if domain['owner'] == owner])
            self.assertLess(a.symmetric_difference(b).area, 1e-12)
        self.assertTrue(all(domain['owner'] == 'south' for domain in at(first, (10, -1))))
        self.assertTrue(all(domain['owner'] == 'north' for domain in at(first, (10, 1))))
        for domain in first:
            owner_y = -2. if domain['owner'] == 'south' else 2.
            # Calling one domain at either side of the owner boundary keeps
            # its own affine field; it never picks another route per vertex.
            for point in ((4, -1), (4.25, 1)):
                np.testing.assert_allclose(domain['uv'](point),
                                           (.5 + (point[1] - owner_y) / 16., point[0] / 16.), atol=1e-12)

    def test_curved_chord_domains_share_exact_endpoint_phase_and_do_not_step_to_nearest_vertex(self):
        route = road('turn', [(0, 0, 7.5), (10, 0, 7.5), (10, 10, 7.5)],
                     [(0, 1), (-1, 1), (-1, 0)], [20, 30, 40])
        original = deepcopy(route)
        asphalt = ribbon(route)
        domains = flat_surface_domains(asphalt, [route], 'lower', {}, [])
        self.assert_partition(domains, asphalt)
        for point, expected in (((10, 0), (.5, 30 / 16.)), ((7, 3), (.5 + 3 / 16., 30 / 16.)),
                                ((13, -3), (.5 - 3 / 16., 30 / 16.)), ((2.1, 0), (.5, 22.1 / 16.))):
            self.assertTrue(at(domains, point))
            for domain in at(domains, point):
                np.testing.assert_allclose(domain['uv'](point), expected, atol=1e-12)
        for key in ('points', 'normals', 'station', 'rail_low', 'rail_high'):
            np.testing.assert_array_equal(route[key], original[key])

    def test_wrong_deck_and_unexplained_asphalt_fail_instead_of_borrowing_another_route(self):
        route = road('lower', [(0, 0, 7.5), (10, 0, 7.5)], [(0, 1)] * 2, [0, 10])
        with self.assertRaisesRegex(ValueError, 'same-deck'):
            flat_surface_domains(ribbon(route), [route], 'upper', {}, [])
        with self.assertRaisesRegex(ValueError, 'outside the supplied'):
            flat_surface_domains(box(0, -3, 10, 4), [route], 'lower', {}, [])


    def test_native_edge_positions_match_and_both_ribbon_stripes_fit_narrow_asphalt(self):
        stations = np.array([0.0, 32.0])
        left = np.array([1.95, 1.95])
        right = np.array([1.2, 1.2])
        for reverse_traffic, native_u, ribbon_u in (
            (False, 97.5 / 128.0, 80.5 / 128.0),
            (True, 28.0 / 128.0, 45.0 / 128.0),
        ):
            with self.subTest(reverse_traffic=reverse_traffic):
                join = NativePaintJoin((0.0, 0.0), (1.0, 0.0), (0.0, 1.0 / 16.0, 0.5),
                                       ribbon_u, native_u)
                paint = RibbonMarkings(stations, left, right, (join,), reverse_traffic)
                native_offset = 16.0 * (native_u - 0.5)
                self.assertAlmostEqual(paint((13.0, native_offset), (0.55, 0.75))[0], ribbon_u)
                for offset, stripe_u in ((-1.2, 45.0 / 128.0), (1.95, 80.5 / 128.0)):
                    original_uv = (0.5 + offset / 16.0, 1.5)
                    actual_u, actual_v = paint((20.0, offset), original_uv)
                    self.assertAlmostEqual(actual_u, stripe_u)
                    self.assertEqual(actual_v, original_uv[1])


if __name__ == '__main__':
    unittest.main()
