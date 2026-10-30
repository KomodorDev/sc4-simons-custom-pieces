"""A highway assembly keeps Highways selection and exact one-button ownership."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.dbpf import exemplar, encode_exemplar
from scp.menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
from scp.menu_experiment import _layout, _guide, _game_checks, _assembly_icon_network
from scp.menu_experiment_resources import (build_menu_experiment_resources,
    validate_menu_experiment_resources, make_assembly_icon)
from scp_highway import menu, icons


class HighwayAssemblyMenuTests(unittest.TestCase):
    def setUp(self):
        self.pieces, self.resources = [], {(1, 2, 3): b'Unrelated source bytes'}
        for index in range(2):
            puzzle = 0xF610 + index
            piece = {'id': f'fixture-highway-{index}', 'domain': 'highway',
                     'name': f'Highway component {index}', 'description': 'Synthetic Highways menu test.',
                     'puzzle_id': f'{puzzle:04x}', 'menu': {'id': f'{0x6A470000 | puzzle:08x}',
                     'order': f'{0xFFFFFF10 + index:08x}', 'style': 'ddrhw-crossing'}}
            resources, _report = menu.build_menu_resources(menu.portable_baseline(), piece)
            self.pieces.append(piece); self.resources.update(resources)
        self.layout = {'assembly_id': 'fixture-highway-assembly', 'member_order': 'first-use-in-assembly',
                       'cycle_button': {'id': '6a47fee0', 'order': 'fffffee0', 'title': 'SCP | Highway assembly',
                                        'description': 'Change components with Tab.'}}
        self.cycle = {**self.layout['cycle_button'], 'target_id': self.pieces[0]['menu']['id']}
        self.icon = make_assembly_icon([[(0., 0., 7.5), (32., 32., 7.5)],
                                        [(0., 32., 0.), (32., 0., 0.)]], network_label='HWY')

    def build(self, pieces=None, cycle=None):
        return build_menu_experiment_resources(self.resources, pieces or self.pieces,
            cycle_button=cycle or self.cycle, cycle_icon=self.icon, expected_cycle_icon=self.icon)

    def test_single_cycle_keeps_highways_property_and_hides_every_member_presentation(self):
        before = deepcopy(self.resources)
        output, report = self.build()
        props = {int(prop['id'], 16): prop['values'] for prop in exemplar(output[*MENU_EXEMPLAR, 0x6A47FEE0])['properties']}
        self.assertEqual(props[0x4005], [0]); self.assertNotIn(0x4001, props)
        self.assertEqual(props[0x8A2602BB], [int(self.pieces[0]['menu']['id'], 16)])
        self.assertEqual(report['cycle_button']['menu'], 'Highways')
        self.assertEqual(report['assembly_menu_buttons'], 1)
        self.assertEqual(report['member_buttons_hidden'], 2)
        self.assertEqual(output[1, 2, 3], before[1, 2, 3]); self.assertEqual(self.resources, before)
        self.assertEqual(output[*ICON, 0x6A47FEE0], self.icon)
        for piece in self.pieces:
            for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION):
                self.assertNotIn((*prefix, int(piece['menu']['id'], 16)), output)

    def test_rail_order_cannot_move_a_highway_cycle_into_rail(self):
        cycle = {**self.cycle, 'order': '72000000'}
        with self.assertRaisesRegex(ValueError, 'domain menu'):
            self.build(cycle=cycle)

    def test_mixed_domains_fail_before_any_source_changes(self):
        pieces = deepcopy(self.pieces); pieces[1]['domain'] = 'high-speed-rail'
        with self.assertRaisesRegex(ValueError, 'cannot mix member domains'):
            self.build(pieces=pieces)

    def test_highway_does_not_inherit_unmeasured_rail_submenu_parent(self):
        submenu = {**self.layout['cycle_button'], 'id': '6a47fee1'}
        with self.assertRaisesRegex(ValueError, 'no highway submenu contract'):
            build_menu_experiment_resources(self.resources, self.pieces, cycle_button=self.cycle, submenu=submenu)

    def test_changed_highways_selector_is_rejected_by_saved_cycle_validation(self):
        output, _report = self.build()
        key = (*MENU_EXEMPLAR, 0x6A47FEE0); record = exemplar(output[key])
        for prop in record['properties']:
            if int(prop['id'], 16) == 0x4005:
                prop['id'] = '0x4001'
        output[key] = encode_exemplar(record)
        with self.assertRaisesRegex(ValueError, 'property|ordering'):
            validate_menu_experiment_resources(output, self.resources, self.pieces,
                cycle_button=self.cycle, expected_cycle_icon=self.icon)

    def test_layout_uses_explicit_domain_and_guide_checks_name_highways(self):
        self.assertEqual(_layout(self.layout, 'highway'), self.layout)
        with self.assertRaisesRegex(ValueError, 'domain menu'):
            _layout(self.layout, 'high-speed-rail')
        guide = _guide(self.layout, self.pieces).decode()
        self.assertIn('Transportation → Highways', guide); self.assertNotIn('Transportation → Rail', guide)
        self.assertIn('visible vehicle operation', guide)
        self.assertIn('Transportation > Highways', _game_checks(self.pieces, single_button=True)['cases'][0]['description'])

    def test_highway_icon_adapter_poses_component_routes_without_native_inputs(self):
        pieces = [{'id': 'first', 'domain': 'highway', 'geometry_key': 'one'}]
        scene = {'placements': [{'piece_id': 'first', 'origin_m': [32., -16.], 'rotation_degrees_ccw': 90}]}
        source = {'route': [(2., -8., 7.5), (2., 8., 15.)]}
        with patch('scp_highway.ramp_paths.component_routes', return_value=source, create=True) as provider:
            result = icons.assembly_icon_routes(scene, pieces)
        self.assertEqual(result, [[(40., -14., 7.5), (24., -14., 15.)]])
        provider.assert_called_once_with(pieces[0])
        self.assertEqual(icons.assembly_icon_network('ddrhw-l1-and-l2-diagonal-avenue-diamond'), 'HWY')
        with self.assertRaises(ValueError):
            icons.assembly_icon_network('unknown-highway-assembly')


if __name__ == '__main__':
    unittest.main()
