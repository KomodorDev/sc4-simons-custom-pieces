"""Inspect grouped assembly presentation bytes without native game fixtures."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.assembly_submenus import build_resources, validate_resources
from scp.dbpf import encode_exemplar, exemplar
from scp.menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
from scp.menu_experiment import _layout
from scp.menu_experiment_resources import build_menu_experiment_resources
from scp_highway import menu


class AssemblySubmenuTests(unittest.TestCase):
    def setUp(self):
        self.source = {(1, 2, 3): b'Unrelated immutable menu resource'}
        self.pieces = []
        for index in range(2):
            piece = {'id': f'fixture-highway-{index}', 'domain': 'highway',
                     'name': f'Highway component {index}', 'description': 'Synthetic menu source.',
                     'puzzle_id': f'{0xF610 + index:04x}',
                     'menu': {'id': f'{0x6A47F610 + index:08x}',
                              'order': f'{0xFFFFFF10 + index:08x}', 'style': 'ddrhw-crossing'}}
            resources, _ = menu.build_menu_resources(menu.portable_baseline(), piece)
            self.source.update(resources); self.pieces.append(piece)
        self.cycle_ids = ['6a47fee2', '6a47fee3']
        for piece, iid in zip(self.pieces, self.cycle_ids):
            self.source, _ = build_menu_experiment_resources(self.source, [piece],
                cycle_button={'id': iid, 'target_id': piece['menu']['id'], 'order': 'fffffee2',
                              'title': 'Fixture assembly ' + iid, 'description': 'Cycle this assembly.'})
        self.groups = [{'definition': {'id': '6a47fee4', 'order': 'fffffee2',
                                       'title': 'Fixture parallel diamond', 'description': 'Choose one alignment.'},
                        'cycle_ids': self.cycle_ids}]

    def build(self, groups=None):
        return build_resources(self.source, self.groups if groups is None else groups, domain='highway')

    def corrupt(self, resources, iid, prop_id, values):
        result = dict(resources); key = (*MENU_EXEMPLAR, iid)
        record = exemplar(result[key])
        next(prop for prop in record['properties'] if int(prop['id'], 16) == prop_id)['values'] = values
        result[key] = encode_exemplar(record)
        return result

    def test_encoded_parent_and_children_keep_targets_icons_text_and_all_source_bytes(self):
        before = deepcopy(self.source)
        output, report = self.build()
        self.assertEqual(self.source, before)
        self.assertEqual(set(output) - set(before), {(*prefix, 0x6A47FEE4)
                         for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)})
        for iid in map(lambda value: int(value, 16), self.cycle_ids):
            original = exemplar(before[*MENU_EXEMPLAR, iid]); current = exemplar(output[*MENU_EXEMPLAR, iid])
            self.assertEqual(current['parent'], original['parent'])
            self.assertEqual(current['properties'][:-2], original['properties'])
            self.assertEqual([prop['values'] for prop in current['properties'][-2:]], [[0x6A47FEE4], [2]])
            for prefix in (ICON, TITLE, DESCRIPTION):
                self.assertEqual(output[*prefix, iid], before[*prefix, iid])
        self.assertEqual(output[1, 2, 3], before[1, 2, 3])
        self.assertTrue(report['submenus_dll_required'])
        self.assertFalse(report['in_game_menu_tested'])

    def test_independent_validator_rejects_wrong_highway_parent_child_class_and_targets(self):
        output, _ = self.build()
        for iid, propid, values in ((0x6A47FEE4, 0x8A2602CA, [0x29]),
                                   (0x6A47FEE2, 0x8A2602CC, [1]),
                                   (0x6A47FEE3, 0x8A2602CA, [0x31]),
                                   (0x6A47FEE2, 0x8A2602BB, [0x6A47F611]),
                                   (0x6A47FEE4, 0x8A2602BB, [0x6A47FEE2])):
            with self.subTest(iid=iid, propid=propid):
                with self.assertRaises(ValueError):
                    validate_resources(self.corrupt(output, iid, propid, values), self.source,
                                       self.groups, domain='highway')

    def test_independent_validator_rejects_unrelated_bytes_missing_resource_and_extra_resource(self):
        output, _ = self.build()
        changed = dict(output); changed[1, 2, 3] = b'Mutated source'
        missing = dict(output); missing.pop((*ICON, 0x6A47FEE4))
        extra = {**output, (3, 2, 1): b'Unexpected resource'}
        for damaged in (changed, missing, extra):
            with self.subTest(keys=len(damaged)):
                with self.assertRaises(ValueError):
                    validate_resources(damaged, self.source, self.groups, domain='highway')

    def test_invalid_duplicate_and_overlapping_members_and_parent_collisions_reject(self):
        for groups in ([{**self.groups[0], 'cycle_ids': []}],
                       [{**self.groups[0], 'cycle_ids': [self.cycle_ids[0]] * 2}],
                       self.groups * 2,
                       [{**self.groups[0], 'cycle_ids': ['6a47fee4']}],
                       [{**self.groups[0], 'definition': {**self.groups[0]['definition'], 'id': '6a47fee2'}}],
                       [{**self.groups[0], 'cycle_ids': [True]}]):
            with self.subTest(groups=groups):
                with self.assertRaises(ValueError):
                    self.build(groups)

    def test_subset_with_one_cycle_is_supported_and_cannot_reparent_existing_cycle(self):
        groups = [{**self.groups[0], 'cycle_ids': self.cycle_ids[:1]}]
        output, report = self.build(groups)
        self.assertEqual(report['submenus'][0]['assembly_cycle_ids'], self.cycle_ids[:1])
        self.assertEqual(output[*MENU_EXEMPLAR, 0x6A47FEE3], self.source[*MENU_EXEMPLAR, 0x6A47FEE3])
        with self.assertRaisesRegex(ValueError, 'collides|already belongs'):
            build_resources(output, groups, domain='highway')

    def test_layout_keeps_shared_submenu_separate_from_legacy_individual_component_submenu(self):
        layout = {'assembly_id': 'fixture-assembly', 'member_order': 'first-use-in-assembly',
                  'cycle_button': {'id': '6a47fee2', 'order': 'fffffee2',
                                   'title': 'Alignment A', 'description': 'Cycle components.'},
                  'cycle_submenu': self.groups[0]['definition']}
        self.assertEqual(_layout(layout, 'highway'), layout)
        with self.assertRaisesRegex(ValueError, 'Unsupported menu layout fields'):
            _layout({**layout, 'submenu': self.groups[0]['definition']}, 'highway')


if __name__ == '__main__':
    unittest.main()
