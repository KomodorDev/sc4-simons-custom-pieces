"""Small negative controls for independently placeable parallel HSR branches.

Inputs are actual registered manifests and encoded generator output. Expected
ports, directions, cells and heights come from the independent literal
contracts, never from the route writer's complete-route declarations.
"""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp_hsr.hsr_assembly_components_verify import CONTRACTS
from scp_hsr.hsr_components_layout import component_layout
from scp_hsr.hsr_components_verify import check_paths
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
from scp_hsr.interchange_verify import PATH, _encoded_routes, _graph
from scp.track_paths import encode_paths
from scp.subject_sources import piece_directory
from scp.verify import parse_paths


def fixture(recipe):
    spec = json.loads((piece_directory(recipe, ROOT)/'piece.json').read_text())
    layout = component_layout(recipe)
    resources = {(*PATH, int(tile, 16)):
        encode_paths(layout[tuple(cell)]['routes'])
        if layout[tuple(cell)]['routes'] else EMPTY_STRUCTURAL_PATH
        for cell, tile in zip(spec['cells'], spec['tile_ids'])}
    return spec, layout, resources


def reencode(routes):
    """Encode inspected records without recalculating their junction fields."""
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for route in routes:
        lines.extend(str(route[field]) for field in
                     ('transport', 'lane', 'entry', 'exit', 'compatibility'))
        lines.append(str(len(route['points'])))
        lines.extend(','.join(format(value, '.12g') for value in point)
                     for point in route['points'])
    return ('\r\n'.join(lines)+'\r\n').encode('ascii')


class ParallelHsrBranchNegativeTests(unittest.TestCase):
    def test_split_branch_role_produces_one_flag_in_its_literal_departure_cell(self):
        recipe = 'hsr_component_lower_zero_turn_split'
        spec, layout, resources = fixture(recipe)
        flagged = [(cell, route) for cell, data in layout.items()
                   for route in data['routes'] if route['junction']]
        self.assertEqual(len(flagged), 1)
        cell, route = flagged[0]
        self.assertEqual(cell, (0, 7))
        self.assertEqual(route['role'], 'branch')
        self.assertEqual(route['movement'], 'S>B')
        self.assertEqual(route['points'][0], (2., -8., 15.5))
        self.assertEqual(check_paths(resources, spec)['permitted_movements_checked'], 3)

    def test_removing_the_split_flag_fails_even_when_geometry_remains_connected(self):
        recipe = 'hsr_component_lower_zero_turn_split'
        spec, _, resources = fixture(recipe)
        contract = CONTRACTS[recipe]
        records = deepcopy(_encoded_routes(resources, spec, contract))
        for _, metadata, _ in records:
            metadata['compatibility'] = 0
        self.assertEqual(_graph(records, contract), (5, 3))
        key = (*PATH, int(spec['tile_ids'][spec['cells'].index([0, 7])], 16))
        parsed = parse_paths(resources[key])['routes']
        self.assertTrue(any(route['compatibility'] == 1 for route in parsed))
        for route in parsed:
            route['compatibility'] = 0
        with self.assertRaisesRegex(ValueError, 'explicit junction flag'):
            check_paths({**resources, key: reencode(parsed)}, spec)

    def test_oneway_lower_straight_cannot_be_reversed_without_a_new_contract(self):
        recipe = 'hsr_component_lower_oneway_straight'
        spec, _, resources = fixture(recipe)
        key = (*PATH, int(spec['tile_ids'][0], 16))
        parsed = parse_paths(resources[key])['routes']
        self.assertEqual(parsed[0]['points'], [(0., -8., 15.5), (0., 8., 15.5)])
        parsed[0]['points'].reverse()
        parsed[0]['entry'], parsed[0]['exit'] = parsed[0]['exit'], parsed[0]['entry']
        with self.assertRaisesRegex(ValueError, 'wrong direction'):
            check_paths({**resources, key: reencode(parsed)}, spec)

    def test_reversing_only_the_opposing_merge_cannot_turn_it_into_a_split(self):
        recipe = 'hsr_component_lower_zero_turn_double_merge'
        spec, layout, resources = fixture(recipe)
        changed, reversed_count = dict(resources), 0
        for cell, tile in zip(spec['cells'], spec['tile_ids']):
            data = layout[tuple(cell)]
            for route in data['routes']:
                if route['movement'] == 'L>S':
                    route['points'].reverse()
                    route['entry'], route['exit'] = route['exit'], route['entry']
                    reversed_count += 1
            if data['routes']:
                changed[*PATH, int(tile, 16)] = encode_paths(data['routes'])
        self.assertGreater(reversed_count, 0)
        self.assertEqual(check_paths(resources, spec)['permitted_movements_checked'], 4)
        with self.assertRaisesRegex(ValueError, 'wrong direction'):
            check_paths(changed, spec)

    def test_each_additional_flat_component_rejects_an_undeclared_height(self):
        for recipe in CONTRACTS:
            with self.subTest(recipe=recipe):
                spec, layout, resources = fixture(recipe)
                tile = next(tile for cell, tile in zip(spec['cells'], spec['tile_ids'])
                            if layout[tuple(cell)]['routes'])
                key = (*PATH, int(tile, 16))
                parsed = parse_paths(resources[key])['routes']
                x, north, height = parsed[0]['points'][0]
                parsed[0]['points'][0] = (x, north, height+1.)
                with self.assertRaisesRegex(ValueError, 'grade|height range'):
                    check_paths({**resources, key: reencode(parsed)}, spec)


if __name__ == '__main__':
    unittest.main()
