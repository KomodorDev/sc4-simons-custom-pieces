"""Corrected junctions preserve ports and clear wider trains and foundations."""
from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))

from scp_hsr.rail_repairs import INFO, build_models, build_rules, repair_layout
from scp.models import parse_s3d
from scp_hsr.rail_feature_verify import _triangles, _weights
from scp_hsr.interchange_verify import _clearance_segments
from scp_hsr.test_support import donor


def world_triangles(models, support=None):
    for (x, row), raw in models.items():
        model = parse_s3d(raw)
        for mesh in model['meshes']:
            is_support = mesh['name'].rstrip(b'\0') == b'SCP consolidated junction support'
            if support is not None and support != is_support:
                continue
            for triangle in _triangles({**model, 'meshes': [mesh]}):
                yield tuple((v[0] + 16*x, v[1], v[2] + 16*row, *v[3:]) for v in triangle)


class RailRepairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.native = donor()
        cls.models = {recipe: build_models(cls.native, recipe) for recipe in INFO}

    def test_layout_calls_return_fresh_current_switch_data(self):
        before = {recipe: deepcopy((INFO[recipe], repair_layout(recipe))) for recipe in INFO}
        for recipe in INFO:
            layout = repair_layout(recipe)
            self.assertEqual(list(layout), INFO[recipe]['cells'])
            layout[next(iter(layout))]['decks'][0]['points'][0] = (123., 456., 789.)
        after = {recipe: (INFO[recipe], repair_layout(recipe)) for recipe in INFO}
        self.assertEqual(before, after)

    def test_exact_external_ports_and_native_cardinal_chords(self):
        for recipe in INFO:
            height = 1. if '_ghsr_' in recipe else 15.5
            incoming = {(x-2., 8., height) for x in (0., 16.)} | {(x+2., -40., height) for x in (0., 16.)}
            outgoing = {(x+2., 8., height) for x in (0., 16.)} | {(x-2., -40., height) for x in (0., 16.)}
            starts, ends = Counter(), Counter()
            records = []
            for (x, row), data in repair_layout(recipe).items():
                for route in data['routes']:
                    points = [(p[0] + 16*x, p[1] - 16*row, p[2]) for p in route['points']]
                    starts[points[0]] += 1
                    ends[points[-1]] += 1
                    records.append(points)
            self.assertEqual(starts.keys() - ends.keys(), incoming)
            self.assertEqual(ends.keys() - starts.keys(), outgoing)
            for points in records:
                for point, a, b in ((points[0], points[0], points[1]),
                                    (points[-1], points[-2], points[-1])):
                    if point not in incoming | outgoing:
                        continue
                    dx, dy = b[0] - a[0], b[1] - a[1]
                    self.assertGreater(math.hypot(dx, dy), 0)
                    self.assertLess(min(abs(dx), abs(dy)), 1e-10)

    def test_exact_one_pier_per_upper_cell_and_no_ground_piers(self):
        for recipe, models in self.models.items():
            support_triangles = list(world_triangles(models, support=True))
            if '_ghsr_' in recipe:
                self.assertFalse(support_triangles)
                continue
            centers = []
            for (x, row), raw in models.items():
                model = parse_s3d(raw)
                supports = [mesh for mesh in model['meshes']
                            if mesh['name'].rstrip(b'\0') == b'SCP consolidated junction support']
                self.assertEqual(len(supports), 1)
                points = [p for triangle in _triangles({**model, 'meshes': supports}) for p in triangle]
                self.assertAlmostEqual(min(p[0] for p in points), -.65, places=6)
                self.assertAlmostEqual(max(p[0] for p in points), .65, places=6)
                self.assertAlmostEqual(min(p[2] for p in points), -.65, places=6)
                self.assertAlmostEqual(max(p[2] for p in points), .65, places=6)
                self.assertEqual(min(p[1] for p in points), 0.)
                self.assertEqual(max(p[1] for p in points), 14.)
                centers.append((16.*x, -16.*row))
            self.assertEqual(centers, INFO[recipe]['support_centers'])
            self.assertGreaterEqual(min(math.dist(a, b) for n, a in enumerate(centers) for b in centers[n+1:]), 16.)

    def test_each_entire_pier_top_contacts_the_deck_underside(self):
        for recipe, models in self.models.items():
            if '_ghsr_' in recipe:
                continue
            undersides = [triangle for triangle in world_triangles(models, support=False)
                          if all(abs(v[1] - 14.) < 1e-5 for v in triangle)]
            for x, north in INFO[recipe]['support_centers']:
                for dx in (-.65, 0., .65):
                    for dz in (-.65, 0., .65):
                        self.assertTrue(any(_weights(x + dx, -north + dz, triangle)
                                            for triangle in undersides), (recipe, x, north, dx, dz))

    def test_every_deck_triangle_is_within_sixteen_metres_of_its_cell_pier(self):
        for recipe, models in self.models.items():
            if '_ghsr_' in recipe:
                continue
            for raw in models.values():
                for triangle in _triangles(parse_s3d(raw)):
                    # Distance to this cell's own pier is a convex function:
                    # the vertex bound consequently covers the entire face.
                    self.assertLessEqual(max(math.hypot(v[0], v[2]) for v in triangle), 16.)

    def test_all_actual_routes_have_five_metre_width_and_height_clearance(self):
        for recipe, models in self.models.items():
            buckets = defaultdict(list)
            for triangle in world_triangles(models):
                for x in range(math.floor((min(v[0] for v in triangle)-1e-4)/4.),
                               math.floor((max(v[0] for v in triangle)+1e-4)/4.)+1):
                    for z in range(math.floor((min(v[2] for v in triangle)-1e-4)/4.),
                                   math.floor((max(v[2] for v in triangle)+1e-4)/4.)+1):
                        buckets[x, z].append(triangle)
            records = [(x, row, [(p[0]+16*x, p[1]-16*row, p[2]) for p in route['points']])
                       for (x, row), data in repair_layout(recipe).items() for route in data['routes']]
            checked = _clearance_segments(records, buckets, half_width=2.5)
            self.assertEqual(checked, sum(len(points)-1 for _, _, points in records))

    def test_construction_uses_only_new_allocation_and_proper_rotations(self):
        recipe = 'rail_hsr_adjacent_scissors_revised'
        cells = INFO[recipe]['cells']
        spec = {'recipe': recipe, 'cells': cells, 'footprint': [2, 3],
                'tile_ids': [0x7F590000 + 0x100*x + 0x10*row for x, row in cells],
                'puzzle_id': 'f9f0', 'preview_id': '7f590ff5', 'effect_name': 'fixture'}
        rules = build_rules(spec)
        self.assertIn('AutoTileBase = 0x7F590000', rules)
        self.assertIn('[HighwayIntersectionInfo_0x0000F9F0]', rules)
        self.assertEqual(rules.count('Rotate = '), 3)
        self.assertNotIn('Transpose', rules)


if __name__ == '__main__':
    unittest.main()
