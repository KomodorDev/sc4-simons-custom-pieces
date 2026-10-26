"""Build useful multi-piece ramp corridors from their encoded train paths.

This checks GHSR/HSR split -> height ramp -> L4 overpass -> height ramp ->
GHSR/HSR merge, with both lower networks and every proper rotation. It proves
connections without overlapping the pieces' occupied construction cells.
"""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))
from scp_hsr.interchange_layouts import INFO, interchange_layout
from scp.track_paths import encode_paths, _parse_paths


def key(point):
    return tuple(round(value, 6) for value in point)


def rotate(point, turns):
    x, y, height = point
    for _ in range(turns):
        x, y = y, -x
    return x, y, height


def placed(recipe, turns, offset):
    paths, cells = [], set()
    for (x, row), data in interchange_layout(recipe).items():
        center = rotate((16*x, -16*row, 0), turns)
        cells.add((round((center[0]+offset[0])/16), round((center[1]+offset[1])/16)))
        for route in _parse_paths(encode_paths(data['routes'])):
            points = []
            for px, py, height in route['points']:
                a, b, h = rotate((px+16*x, py-16*row, height), turns)
                points.append(key((a+offset[0], b+offset[1], h)))
            paths.append(points)
    return paths, cells


def reachable(paths, start):
    graph = {}
    for path in paths:
        graph.setdefault(key(path[0]), set()).add(key(path[-1]))
    seen, pending = set(), [key(start)]
    while pending:
        point = pending.pop()
        if point not in seen:
            seen.add(point)
            pending.extend(graph.get(point, set())-seen)
    return seen


class InterchangeAssemblyTests(unittest.TestCase):
    def test_all_thirty_two_mixed_network_flyover_corridors_join_and_stay_one_way(self):
        cases = 0
        for origin in ('ground', 'hsr'):
            for destination in ('ground', 'hsr'):
                for lower in ('ground', 'hsr'):
                    paths, occupied = [], set()
                    def add(recipe, turns, offset):
                        new_paths, new_cells = placed(recipe, turns, offset)
                        self.assertFalse(occupied & new_cells, (recipe, occupied & new_cells))
                        occupied.update(new_cells)
                        paths.extend(new_paths)
                        return new_paths
                    height = 1. if origin == 'ground' else 15.5
                    start = (2., -24., height)
                    add(f'interchange_{origin}_split_90_compact', 0, (0., 0.))
                    cursor = (24., 0., height)
                    def attach_grade(first, last):
                        nonlocal cursor
                        recipe = f'interchange_oneway_grade_{first}_to_{last}'
                        inlet, outlet = INFO[recipe]['ports']['in'][0], INFO[recipe]['ports']['out'][0]
                        inlet = rotate(inlet, 1)
                        outlet = rotate(outlet, 1)
                        offset = cursor[0]-inlet[0], cursor[1]-inlet[1]
                        self.assertEqual(cursor[2], inlet[2])
                        self.assertTrue(all(abs(value/16-round(value/16)) < 1e-8 for value in offset))
                        add(recipe, 1, offset)
                        cursor = outlet[0]+offset[0], outlet[1]+offset[1], outlet[2]
                    if origin == 'ground':
                        attach_grade('ground', 'hsr')
                    attach_grade('hsr', 'l4')
                    overpass_offset = cursor[0]+8., cursor[1]
                    cross_paths = add(f'interchange_l4_oneway_over_{lower}', 0, overpass_offset)
                    lower_routes = [path for path in cross_paths if path[0][2] < 30.5]
                    cursor = cursor[0]+48., cursor[1], 30.5
                    attach_grade('l4', 'hsr')
                    if destination == 'ground':
                        attach_grade('hsr', 'ground')
                    merge_offset = cursor[0]+24., -16.
                    add(f'interchange_{destination}_merge_90_compact', 2, merge_offset)
                    finish = merge_offset[0]-2., -24., 1. if destination == 'ground' else 15.5
                    for turns in range(4):
                        transformed = [[rotate(point, turns) for point in path] for path in paths]
                        source, target = rotate(start, turns), rotate(finish, turns)
                        with self.subTest(origin=origin, destination=destination, lower=lower, turns=turns):
                            self.assertIn(key(target), reachable(transformed, source))
                            self.assertNotIn(key(source), reachable(transformed, target))
                            for path in lower_routes:
                                self.assertNotIn(key(target), reachable(transformed, rotate(path[0], turns)))
                        cases += 1
        self.assertEqual(cases, 32)


if __name__ == '__main__':
    unittest.main()
