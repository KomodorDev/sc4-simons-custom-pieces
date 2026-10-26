"""Encoded menu experiments preserve all non-presentation build resources."""
from __future__ import annotations

from copy import deepcopy
from io import BytesIO
from pathlib import Path
import struct
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.dbpf import encode_exemplar, exemplar
from scp.menu import DESCRIPTION, ICON, MENU_EXEMPLAR, TITLE
from scp.menu_experiment_resources import (
    ITEM_BUTTON_CLASS, ITEM_SUBMENU_PARENT_ID, build_menu_experiment_resources,
    validate_menu_experiment_resources)


def property_record(prop_id, values, *, kind=0x300, array=False):
    return {'id': f'0x{prop_id:08x}', 'type': f'0x{kind:04x}',
            'key_type': '0x0080' if array or kind == 0xC00 else '0x0000',
            'values': values, 'repetitions': len(values) if array or kind == 0xC00 else None}


def properties(raw):
    return {int(p['id'], 16): p for p in exemplar(raw)['properties']}


class MenuExperimentResourceTests(unittest.TestCase):
    def setUp(self):
        self.pieces, self.source = [], {}
        for number in range(14):
            button_id, order = 0x6A47F000 + number, 0x72000000 + number
            self.pieces.append({'id': f'piece-{number}',
                                'menu': {'id': f'{button_id:08x}', 'order': f'{order:08x}'}})
            props = [property_record(0x10, [40]),
                     property_record(0x20, f'Original piece {number}', kind=0xC00),
                     property_record(0x4001, [1]),
                     property_record(0x49CAC341, [1234], kind=0x700),
                     property_record(0x8A2602B8, [button_id]),
                     property_record(0x8A2602B9, [order]),
                     property_record(0x8A2602BB, [button_id]),
                     property_record(0x8A416A99, [*TITLE, button_id], array=True),
                     property_record(0x8A94EEE0, [4321]),
                     property_record(0xCA416AB5, [*DESCRIPTION, button_id], array=True)]
            self.source[*MENU_EXEMPLAR, button_id] = encode_exemplar(
                {'parent': [0x6534284A, 0x12345678, 0x87654321], 'properties': props})
            for prefix, text in ((TITLE, f'Original title {number}'),
                                 (DESCRIPTION, f'Original description {number}')):
                self.source[*prefix, button_id] = struct.pack('<HH', len(text), 0x1000) + text.encode('utf-16-le')
            self.source[*ICON, button_id] = b'opaque original PNG bytes ' + bytes([number])
        self.source[0, 0, 0] = b'Native combined controller stays byte-identical'
        self.source[0x296678F7, 0x69668828, 0x7F5F0000] = b'Native PATH stays byte-identical'
        self.cycle = {'id': '6a47f700', 'target_id': '6a47f000', 'order': '72010000',
                      'title': 'SCP | Trumpet parts: TAB cycle',
                      'description': 'Select individual pieces with TAB; place each separately.'}
        self.submenu = {'id': '7f5ff701', 'order': '72010001',
                        'title': 'SCP | Trumpet parts: individual buttons',
                        'description': 'Open all fourteen reusable types as individual buttons.'}

    def build(self):
        return build_menu_experiment_resources(self.source, self.pieces,
                                               cycle_button=self.cycle, submenu=self.submenu)

    def test_moves_fourteen_original_buttons_without_changing_identity_or_assets(self):
        before = deepcopy(self.source)
        output, report = self.build()
        self.assertEqual(self.source, before)
        self.assertEqual(len(output), len(self.source) + 8)
        self.assertEqual(len(report['individual_buttons']), 14)
        for piece in self.pieces:
            button_id = int(piece['menu']['id'], 16)
            original = properties(self.source[*MENU_EXEMPLAR, button_id])
            actual = properties(output[*MENU_EXEMPLAR, button_id])
            self.assertEqual({key: actual[key] for key in original}, original)
            self.assertEqual(actual[ITEM_SUBMENU_PARENT_ID]['values'], [0x7F5FF701])
            self.assertEqual(actual[ITEM_BUTTON_CLASS]['values'], [2])
        changed = {(*MENU_EXEMPLAR, int(p['menu']['id'], 16)) for p in self.pieces}
        for key in self.source.keys() - changed:
            self.assertEqual(output[key], before[key])
        self.assertFalse(report['in_game_menu_tested'])
        self.assertFalse(report['cycle_button']['construction_alias_verified_in_game'])

    def test_cycle_alias_uses_unique_icon_and_text_but_shared_first_piece_target(self):
        output, _ = self.build()
        props = properties(output[*MENU_EXEMPLAR, 0x6A47F700])
        self.assertEqual(props[0x8A2602BB]['values'], [0x6A47F000])
        self.assertEqual(props[0x8A2602B8]['values'], [0x6A47F700])
        self.assertEqual(props[0x8A416A99]['values'], [*TITLE, 0x6A47F700])
        self.assertEqual(props[0xCA416AB5]['values'], [*DESCRIPTION, 0x6A47F700])
        self.assertNotIn(ITEM_SUBMENU_PARENT_ID, props)
        self.assertNotIn(ITEM_BUTTON_CLASS, props)
        original = properties(self.source[*MENU_EXEMPLAR, 0x6A47F000])
        self.assertEqual(props[0x49CAC341], original[0x49CAC341])
        self.assertEqual(props[0x8A94EEE0], original[0x8A94EEE0])

    def test_submenu_is_class_one_under_rail_and_icons_have_four_distinct_states(self):
        from PIL import Image

        output, _ = self.build()
        props = properties(output[*MENU_EXEMPLAR, 0x7F5FF701])
        self.assertEqual(props[0x10]['values'], [40])
        self.assertEqual(props[0x8A2602BB]['values'], [0x7F5FF701])
        self.assertEqual(props[ITEM_SUBMENU_PARENT_ID]['values'], [0x29])
        self.assertEqual(props[ITEM_BUTTON_CLASS]['values'], [1])
        for button_id in (0x6A47F700, 0x7F5FF701):
            with Image.open(BytesIO(output[*ICON, button_id])) as icon:
                self.assertEqual(icon.size, (176, 44))
                self.assertEqual(icon.mode, 'RGBA')
                frames = {icon.crop((44*n, 0, 44*(n+1), 44)).tobytes() for n in range(4)}
                self.assertEqual(len(frames), 4)

    def test_empty_and_duplicate_piece_inputs_reject_without_mutation(self):
        for pieces in ([], [self.pieces[0], self.pieces[0]], 'piece-0'):
            with self.subTest(pieces=pieces):
                before = deepcopy(self.source)
                with self.assertRaisesRegex(ValueError, 'At least one|Duplicate|ordered sequence'):
                    build_menu_experiment_resources(self.source, pieces,
                                                   cycle_button=self.cycle, submenu=self.submenu)
                self.assertEqual(before, self.source)

    def test_original_menu_identity_collision_rejects(self):
        self.pieces[1]['menu']['id'] = self.pieces[0]['menu']['id']
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            self.build()

    def test_new_id_rejects_collision_even_if_only_a_text_resource_exists(self):
        self.source[*DESCRIPTION, 0x6A47F700] = b'Pre-existing independent text'
        with self.assertRaisesRegex(ValueError, 'collides'):
            self.build()

    def test_distinct_new_ids_and_valid_rail_orders_are_required(self):
        for field, value in (('id', self.submenu['id']), ('order', '1234'), ('order', -1),
                             ('id', True)):
            with self.subTest(field=field, value=value):
                definition = deepcopy(self.cycle)
                definition[field] = value
                with self.assertRaises(ValueError):
                    build_menu_experiment_resources(self.source, self.pieces,
                                                   cycle_button=definition, submenu=self.submenu)

    def test_alias_target_must_be_the_first_selected_original_root(self):
        for target in ('6a47f001', '6a47f700'):
            with self.subTest(target=target):
                definition = {**self.cycle, 'target_id': target}
                with self.assertRaisesRegex(ValueError, 'first selected'):
                    build_menu_experiment_resources(self.source, self.pieces,
                                                   cycle_button=definition, submenu=self.submenu)

    def test_missing_and_already_modified_sources_reject(self):
        modified, _ = self.build()
        with self.assertRaisesRegex(ValueError, 'collides|already contains'):
            build_menu_experiment_resources(modified, self.pieces,
                                           cycle_button=self.cycle, submenu=self.submenu)
        self.source.pop((*ICON, 0x6A47F000))
        with self.assertRaisesRegex(ValueError, 'Missing original menu resources'):
            self.build()

    def test_validator_rejects_unrelated_asset_changes_extra_resources_and_bad_targets(self):
        output, _ = self.build()
        changed_path = dict(output)
        changed_path[0x296678F7, 0x69668828, 0x7F5F0000] = b'Changed path'
        extra = dict(output)
        extra[1, 2, 3] = b'Unexpected resource'
        wrong_target = dict(output)
        record = exemplar(wrong_target[*MENU_EXEMPLAR, 0x6A47F700])
        next(p for p in record['properties'] if p['id'] == '0x8a2602bb')['values'] = [0x6A47F001]
        wrong_target[*MENU_EXEMPLAR, 0x6A47F700] = encode_exemplar(record)
        for damaged in (changed_path, extra, wrong_target):
            with self.assertRaisesRegex(ValueError, 'non-target|unexpected resource|construction target'):
                validate_menu_experiment_resources(damaged, self.source, self.pieces,
                                                  cycle_button=self.cycle, submenu=self.submenu)


if __name__ == '__main__':
    unittest.main()
