"""Oblique end wedges exclude no interior, unrelated, or unowned rail defect."""
from copy import deepcopy
import math
import unittest

from scp_hsr.directional_t_verify import audit_visible_rails
from scp_hsr.hsr_compact_fan_verify import (
    _custom_port_rail_wedges, clip_custom_port_rail_caps, audit_visible_rails_at_custom_cuts,
)
from scp_hsr.interchange_verify import _bed
from scp_hsr.rail_feature_verify import _rail_u


class ObliqueRailCutTests(unittest.TestCase):
    def setUp(self):
        self.direction = (-.927254808965, .374430927211)  # East/south model frame.
        norm = math.hypot(*self.direction)
        self.direction = tuple(value/norm for value in self.direction)
        self.origin = (0., 8.)
        self.contract = {'cells': [(0, 0)], 'ports': {'Sout': (0., -8., 15.5)},
                         'port_vectors': {'Sout': (self.direction[0], -self.direction[1])},
                         'custom_curve_ports': ('Sout',), 'geometric_custom_rail_wedges': True}
        first = self.vertex(-6., 0., _rail_u(2.))
        self.records = [((0, 0), {}, [(first[0], -first[2], 15.5), (0., -8., 15.5)])]
        a, b, c, d = (self.vertex(t, s, _rail_u(2.+s))
                       for t, s in ((-6., -1.), (-6., 1.), (0., 1.), (0., -1.)))
        self.base = [(a, b, c), (a, c, d)]

    def vertex(self, distance, transverse, u):
        dx, dz = self.direction
        return (self.origin[0]+distance*dx-transverse*dz, _bed(15.5),
                self.origin[1]+distance*dz+transverse*dx, u, 0.)

    def patch(self, distance, transverse):
        # A recovered native rail center at this exact position. A small
        # patch avoids relying on one centroid or a zero-area boundary face.
        r = .0005
        a, b, c, d = (self.vertex(t, s, _rail_u(2.)) for t, s in (
            (distance-r, transverse-r), (distance-r, transverse+r),
            (distance+r, transverse+r), (distance+r, transverse-r)))
        return [(a, b, c), (a, c, d)]

    def test_correct_oblique_termination_derives_its_depth_from_the_actual_boundary(self):
        wedge = _custom_port_rail_wedges(self.contract)[0]
        expected = 1.10*abs(self.direction[0])/self.direction[1]
        self.assertAlmostEqual(wedge['maximum_depth_m'], expected, places=12)
        self.assertGreater(wedge['maximum_depth_m'], 2.6)
        self.assertEqual(wedge['source_cell'], [0, 0])
        self.assertEqual(wedge['edge'], 'south')
        extension = self.patch(2.60, 1.055)
        with self.assertRaisesRegex(ValueError, 'visible native rail'):
            audit_visible_rails(self.base+extension, self.records)
        result = audit_visible_rails_at_custom_cuts(self.base+extension, self.records, self.contract)
        self.assertFalse(result['unused_visible_rails_outside_declared_custom_caps'])
        self.assertTrue(result['custom_cap_extensions_require_strict_actual_assembled_path_audit'])

    def test_same_strict_interior_rail_center_rule_still_rejects_a_half_metre_offset(self):
        inward = self.patch(-1., .5)
        with self.assertRaisesRegex(ValueError, 'rail centre has no matching'):
            audit_visible_rails_at_custom_cuts(self.base+inward, self.records, self.contract)
        preserved, affected = clip_custom_port_rail_caps(inward, self.contract)
        self.assertEqual(preserved, inward)
        self.assertEqual(affected, 0)

    def test_stripes_beyond_the_tile_edge_or_lateral_envelope_remain_rejected(self):
        for distance, transverse in ((2.80, 1.055), (2.20, 1.20), (-3., 3.)):
            patch = self.patch(distance, transverse)
            with self.subTest(distance=distance, transverse=transverse):
                preserved, affected = clip_custom_port_rail_caps(patch, self.contract)
                self.assertEqual(preserved, patch)
                self.assertEqual(affected, 0)
                with self.assertRaisesRegex(ValueError, 'visible native rail'):
                    audit_visible_rails_at_custom_cuts(self.base+patch, self.records, self.contract)

    def test_a_wedge_cannot_hide_model_geometry_in_an_unowned_cell(self):
        self.origin = (-7., 8.)
        contract = deepcopy(self.contract)
        contract['ports']['Sout'] = (-7., -8., 15.5)
        outside = self.patch(2.60, 1.055)
        self.assertTrue(all(point[0] < -8. for triangle in outside for point in triangle))
        preserved, affected = clip_custom_port_rail_caps(outside, contract)
        self.assertEqual(preserved, outside)
        self.assertEqual(affected, 0)

    def test_all_cardinal_poses_use_their_actual_exposed_edge(self):
        def rotated(point, count):
            east, north, *rest = point
            for _ in range(count):
                east, north = -north, east
            return (east, north, *rest)

        def model_point(point, count):
            east, height, south, u, v = point
            east, north = rotated((east, -south), count)
            return east, height, -north, u, v

        for turns, edge in enumerate(('south', 'east', 'north', 'west')):
            with self.subTest(edge=edge):
                contract = deepcopy(self.contract)
                contract['ports']['Sout'] = rotated(contract['ports']['Sout'], turns)
                contract['port_vectors']['Sout'] = rotated(contract['port_vectors']['Sout'], turns)
                records = [(key, data, [rotated(point, turns) for point in points])
                           for key, data, points in self.records]
                triangles = [tuple(model_point(point, turns) for point in triangle)
                             for triangle in self.base+self.patch(2.60, 1.055)]
                result = audit_visible_rails_at_custom_cuts(triangles, records, contract)
                self.assertEqual(result['custom_port_boundary_wedges'][0]['edge'], edge)

    def test_an_inward_facing_declared_cut_is_invalid(self):
        contract = deepcopy(self.contract)
        contract['port_vectors']['Sout'] = tuple(-value for value in contract['port_vectors']['Sout'])
        with self.assertRaisesRegex(ValueError, 'must leave'):
            clip_custom_port_rail_caps(self.base, contract)

    def test_geometric_wedges_cannot_bypass_an_inherited_model_exception(self):
        contract = deepcopy(self.contract)
        contract['inherited_custom_cap'] = {'label': 'Sout', 'depth_m': 2.65}
        with self.assertRaisesRegex(ValueError, 'Inherited custom-cut model exceptions'):
            audit_visible_rails_at_custom_cuts(self.base, self.records, contract)

    def test_exact_redesigned_contracts_and_extracted_core_opt_in(self):
        from scp_hsr.hsr_compact_fan_verify import CONTRACTS as fans
        from scp_hsr.hsr_atomic_components_verify import CONTRACTS as atomic
        selected = {name for name, contract in {**fans, **atomic}.items()
                    if contract.get('geometric_custom_rail_wedges', False)}
        self.assertEqual(selected, {'hsr_component_l2_paired_fan_compact_join',
                                    'hsr_component_l2_paired_fan_compact_core',
                                    'hsr_component_l2_short_opposed_merge_core'})
        self.assertEqual(fans['hsr_component_l2_paired_fan_compact_core']['custom_curve_ports'],
                         ('Wout', 'Ein'))
        straight = fans['hsr_component_l2_paired_straight_recessed_web']
        self.assertFalse(straight.get('geometric_custom_rail_wedges', False))
        self.assertEqual(straight['custom_curve_ports'], ())
        self.assertFalse(straight['custom_curved_interfaces'])

    def test_unselected_contracts_retain_the_original_literal_mask(self):
        contract = deepcopy(self.contract)
        del contract['geometric_custom_rail_wedges']
        report = audit_visible_rails_at_custom_cuts(self.base+self.patch(2.59, 1.055), self.records, contract)
        self.assertEqual(report['custom_port_cap_depth_m'], 2.6)
        self.assertEqual(report['custom_port_cap_width_m'], 5.2)
        self.assertNotIn('custom_port_boundary_wedges', report)

        # The geometric extension is valid only for an opted-in contract.
        beyond_original = self.patch(2.62, 1.065)
        with self.assertRaisesRegex(ValueError, 'visible native rail'):
            audit_visible_rails_at_custom_cuts(self.base+beyond_original, self.records, contract)
        audit_visible_rails_at_custom_cuts(self.base+beyond_original, self.records, self.contract)


if __name__ == '__main__':
    unittest.main()
