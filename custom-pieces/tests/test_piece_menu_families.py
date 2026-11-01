"""Portable alternative-menu corruption and disjoint assembly integration checks."""
from __future__ import annotations

from copy import deepcopy
import hashlib
from pathlib import Path
import re
import sys
import unittest

ROOT = next(path for path in Path(__file__).resolve().parents if (path / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import piece_menu_families as families
from scp.build import NETWORK_INI, RUL0
from scp.dbpf import pack_dbpf
from scp.menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
from scp.rul0 import compose_rul0, with_feature_sequence
from scp.verify import strict_dbpf
import test_menu_experiment as menu_fixture


NATIVE = (b'; retained native rules\r\n[Ordering]\r\n'
          b'RotationRing = 100, 10100\r\nAddTypes = 101, 10101\r\n'
          b'[HighwayIntersectionInfo_0x00000100]\r\nPiece = native\r\n')


def fragment(root):
    states = [root + (turn << 16) for turn in range(8)]
    return ('RotationRing = ' + ', '.join(f'{state:X}' for state in states) + '\r\n'
            + ''.join(f'[HighwayIntersectionInfo_0x{state:08X}]\r\n'
                      f'CopyFrom = 0x{root:08X}\r\n' for state in states))


def rows(insertion):
    result = []
    for line in insertion.splitlines():
        match = re.fullmatch(r'(RotationRing|AddTypes)\s*=\s*(.+)', line, re.I)
        if match:
            result.append((match[1].lower(), [int(token, 16) for token in match[2].split(',')]))
    return result


class PieceMenuFamilyTests(unittest.TestCase):
    def setUp(self):
        self.pieces = []
        for index, name in enumerate(('first', 'anchor', 'middle', 'alternative', 'last')):
            self.pieces.append({'id': 'fixture-' + name, 'name': 'Fixture ' + name,
                'description': 'Portable menu family fixture', 'domain': 'high-speed-rail',
                'puzzle_id': f'{0xF800 + index:04x}',
                'menu': {'id': f'{0x6A47F800 + index:08x}', 'order': f'{0x7200F800 + index:08x}'}})
        self.pieces[3]['menu']['family_anchor'] = self.pieces[1]['id']
        self.raw, self.composition = compose_rul0(NATIVE, [fragment(int(piece['puzzle_id'], 16))
                                                          for piece in self.pieces])
        self.menus = {key: raw for piece in self.pieces
                      for key, raw in menu_fixture.menu_resource(piece).items()}

    def apply(self, pieces=None):
        return families.apply(self.raw, self.composition, self.menus,
                              self.pieces if pieces is None else pieces)

    def test_pair_shares_original_button_and_preserves_native_and_construction_bytes(self):
        original = deepcopy((self.composition, self.pieces, self.menus))
        raw, composition, menus, record = self.apply()
        saved = rows(composition['ordering_insertion'])
        self.assertEqual([(keyword, states[0]) for keyword, states in saved],
                         [('rotationring', 0xF800), ('rotationring', 0xF801), ('addtypes', 0xF803),
                          ('rotationring', 0xF802), ('rotationring', 0xF804)])
        hidden = {(*prefix, int(self.pieces[3]['menu']['id'], 16)) for prefix in families.PREFIXES}
        self.assertEqual(menus, {key: value for key, value in self.menus.items() if key not in hidden})
        self.assertEqual(raw[-len(self.composition['suffix']):], self.raw[-len(self.composition['suffix']):])
        plain, metadata, report = families.verify(raw, composition, self.pieces, record)
        self.assertEqual((plain, metadata), (self.raw, self.composition))
        self.assertEqual(plain[:-len(metadata['suffix'])].replace(metadata['ordering_insertion'].encode(), b'', 1), NATIVE)
        self.assertEqual(report['hidden_member_buttons'], 1)
        self.assertEqual(original, (self.composition, self.pieces, self.menus))

    def test_member_only_and_anchor_only_keep_their_standalone_presentations(self):
        for piece in (self.pieces[1], self.pieces[3]):
            with self.subTest(piece=piece['id']):
                raw, meta = compose_rul0(NATIVE, [fragment(int(piece['puzzle_id'], 16))])
                menus = menu_fixture.menu_resource(piece)
                result = families.apply(raw, meta, menus, [piece], available=self.pieces)
                self.assertEqual(result, (raw, meta, menus, None))
                self.assertEqual(families.verify(raw, meta, [piece], None), (raw, meta, None))

    def test_builder_rejects_unknown_anchor_even_when_only_member_is_selected(self):
        pieces = deepcopy(self.pieces)
        pieces[3]['menu']['family_anchor'] = 'fixture-unknown'
        with self.assertRaisesRegex(ValueError, 'Unknown menu family anchor'):
            families.declarations([pieces[3]], available=pieces)

    def test_selected_linking_fields_must_match_the_supplied_catalogue(self):
        for field in ('anchor', 'puzzle', 'menu', 'domain', 'order'):
            piece = deepcopy(self.pieces[3])
            if field == 'anchor':
                piece['menu']['family_anchor'] = 'fixture-unknown'
            elif field == 'puzzle':
                piece['puzzle_id'] = 'f8ff'
            elif field == 'menu':
                piece['menu']['id'] = '6a47ffff'
            elif field == 'domain':
                piece['domain'] = 'highway'
            else:
                piece['menu']['order'] = '7200ffff'
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'differs from its catalogue'):
                families.declarations([piece], available=self.pieces)
        saved_piece = dict(deepcopy(self.pieces[3]), asset_file='managed/20_Pieces/member.dat')
        self.assertEqual(families.declarations([saved_piece], available=self.pieces), [])

    def test_malformed_self_wrong_domain_chain_cycle_and_duplicate_anchors_fail(self):
        cases = []
        for anchor in (None, True, [], {}, '', 'Fixture-Invalid', 'fixture-alternative'):
            pieces = deepcopy(self.pieces)
            pieces[3]['menu']['family_anchor'] = anchor
            cases.append(pieces)
        pieces = deepcopy(self.pieces); pieces[1]['domain'] = 'highway'; cases.append(pieces)
        pieces = deepcopy(self.pieces); pieces[1]['menu']['family_anchor'] = 'fixture-first'; cases.append(pieces)
        pieces = deepcopy(self.pieces); pieces[1]['menu']['family_anchor'] = 'fixture-alternative'; cases.append(pieces)
        pieces = deepcopy(self.pieces); pieces.append(deepcopy(pieces[1])); cases.append(pieces)
        pieces = deepcopy(self.pieces); pieces[3]['menu']['id'] = pieces[1]['menu']['id']; cases.append(pieces)
        pieces = deepcopy(self.pieces); pieces[3]['puzzle_id'] = pieces[1]['puzzle_id']; cases.append(pieces)
        for pieces in cases:
            with self.subTest(pieces=pieces), self.assertRaises(ValueError):
                families.declarations(pieces, available=pieces)

    def test_manifest_and_evidence_must_follow_actual_piece_declarations(self):
        raw, composition, _menus, record = self.apply()
        cases = [None, {}, dict(record, schema_version=True),
                 dict(record, families=[]), dict(record, extra='unexpected')]
        wrong = deepcopy(record); wrong['families'][0]['member_ids'].reverse(); cases.append(wrong)
        for candidate in cases:
            with self.subTest(candidate=candidate), self.assertRaises(ValueError):
                families.verify(raw, composition, self.pieces, candidate)
        changed = deepcopy(self.pieces)
        changed[3]['menu'].pop('family_anchor')
        with self.assertRaisesRegex(ValueError, 'differs from selected declarations'):
            families.verify(raw, composition, changed, record)
        wrong_meta = deepcopy(composition)
        wrong_meta[families.KEY]['groups'] = [[0xF801, 0xF802]]
        with self.assertRaisesRegex(ValueError, 'roots differ'):
            families.verify(raw, wrong_meta, self.pieces, record)

    def test_missing_evidence_or_invented_family_on_plain_build_is_rejected(self):
        raw, composition, _menus, record = self.apply()
        wrong = deepcopy(composition); del wrong[families.KEY]
        with self.assertRaises(ValueError):
            families.verify(raw, wrong, self.pieces, record)
        plain = deepcopy(self.pieces)
        plain[3]['menu'].pop('family_anchor')
        with self.assertRaises(ValueError):
            families.verify(self.raw, composition, plain, None)

    def test_saved_family_root_metadata_requires_actual_integer_lists(self):
        raw, composition, _menus, record = self.apply()
        for groups in ([[float(0xF801), float(0xF803)]], ((0xF801, 0xF803),),
                       [(0xF801, 0xF803)], [[True, 0xF803]], [[0xF801, -1]],
                       [[0xF801, 0x100000000]]):
            meta = deepcopy(composition); meta[families.KEY]['groups'] = groups
            with self.subTest(groups=groups), self.assertRaisesRegex(ValueError, 'root metadata'):
                families.verify(raw, meta, self.pieces, record)
            with self.subTest(compositor=groups), self.assertRaisesRegex(ValueError, 'root metadata'):
                families.with_feature_sequence_preserving_families(raw, meta, [0xF804, 0xF800])

    def test_changed_states_unrelated_rows_and_family_keywords_are_rejected(self):
        raw, composition, _menus, record = self.apply()
        original = composition['ordering_insertion']
        changes = (original.replace('AddTypes = F803', 'RotationRing = F803'),
                   original.replace('AddTypes = F803', 'AddTypes = FFFF'),
                   original.replace('RotationRing = F800', 'AddTypes = F800'),
                   original.replace('RotationRing = F804', 'RotationRing = F805'))
        for insertion in changes:
            modified = raw.replace(original.encode(), insertion.encode(), 1)
            meta = dict(composition, ordering_insertion=insertion)
            with self.subTest(insertion=insertion), self.assertRaises(ValueError):
                families.verify(modified, meta, self.pieces, record)

    def test_native_and_definition_tampering_is_rejected_before_restoration(self):
        raw, composition, _menus, record = self.apply()
        for changed in (raw.replace(b'Piece = native', b'Piece = changed'),
                        raw.replace(b'CopyFrom = 0x0000F800', b'CopyFrom = 0x0000FFFF'), raw + b'; extra'):
            with self.subTest(changed=changed[:40]), self.assertRaises(ValueError):
                families.verify(changed, composition, self.pieces, record)

    def test_multiple_alternative_families_have_separate_roots(self):
        pieces = deepcopy(self.pieces)
        pieces[4]['menu']['family_anchor'] = pieces[0]['id']
        raw, composition, _menus, record = self.apply(pieces)
        self.assertEqual([(kind, state[0]) for kind, state in rows(composition['ordering_insertion'])],
                         [('rotationring', 0xF800), ('addtypes', 0xF804),
                          ('rotationring', 0xF801), ('addtypes', 0xF803), ('rotationring', 0xF802)])
        self.assertEqual(families.verify(raw, composition, pieces, record)[:2],
                         (self.raw, self.composition))

    def test_legacy_feature_sequence_is_unchanged_without_declared_families(self):
        expected = with_feature_sequence(self.raw, self.composition, [0xF804, 0xF800])
        self.assertEqual(families.with_feature_sequence_preserving_families(
            self.raw, self.composition, [0xF804, 0xF800]), expected)

    def test_disjoint_assembly_family_preserves_alternatives_and_exact_previous_controller(self):
        raw, composition, _menus, _record = self.apply()
        changed, metadata = families.with_feature_sequence_preserving_families(
            raw, composition, [0xF804, 0xF800])
        saved = rows(metadata['ordering_insertion'])
        self.assertEqual([(keyword, states[0]) for keyword, states in saved],
                         [('rotationring', 0xF804), ('addtypes', 0xF800),
                          ('rotationring', 0xF801), ('addtypes', 0xF803), ('rotationring', 0xF802)])
        proof = metadata['feature_sequence']
        restored = changed.replace(metadata['ordering_insertion'].encode(),
                                   proof['previous_ordering_insertion'].encode(), 1)
        self.assertEqual(restored, raw)
        self.assertEqual(hashlib.sha256(restored).hexdigest(), proof['previous_controller_sha256'])
        self.assertEqual(metadata[families.KEY], composition[families.KEY])

    def test_assembly_selection_cannot_consume_an_alternative_or_anchor(self):
        raw, composition, _menus, _record = self.apply()
        for selection in ([0xF800, 0xF801], [0xF803, 0xF804], [0xF801, 0xF803]):
            with self.subTest(selection=selection), self.assertRaisesRegex(ValueError, 'overlaps'):
                families.with_feature_sequence_preserving_families(raw, composition, selection)
        for selection in ([0xF800, 'bad'], [0xF800, []], [0xF800, True], [0xF800, 0xFFFF]):
            with self.subTest(selection=selection), self.assertRaises(ValueError):
                families.with_feature_sequence_preserving_families(raw, composition, selection)

    def test_malformed_preserved_family_or_contiguity_cannot_reach_compositor(self):
        raw, composition, _menus, _record = self.apply()
        for groups in ([], [[0xF801]], [[0xF801, 0xF803], [0xF800, 0xF803]], [[0xF801, 0xFFFF]],
                       [[0xF801, 0xF802]]):
            meta = deepcopy(composition); meta[families.KEY]['groups'] = groups
            with self.subTest(groups=groups), self.assertRaises(ValueError):
                families.with_feature_sequence_preserving_families(raw, meta, [0xF804, 0xF800])

    def test_production_three_assembly_transform_preserves_unrelated_alternative_family(self):
        from scp.multi_assembly_menu import _actual, _transform
        from scp.menu_experiment_resources import make_assembly_icon
        pieces = deepcopy(self.pieces)
        for index, name in enumerate(('extra-one', 'extra-two', 'extra-three', 'extra-four'), len(pieces)):
            pieces.append({'id': 'fixture-' + name, 'name': 'Fixture ' + name,
                'description': 'Another independent assembly component', 'domain': 'high-speed-rail',
                'puzzle_id': f'{0xF800 + index:04x}',
                'menu': {'id': f'{0x6A47F800 + index:08x}', 'order': f'{0x7200F800 + index:08x}'}})
        raw, composition = compose_rul0(NATIVE, [fragment(int(piece['puzzle_id'], 16)) for piece in pieces])
        menus = {key: raw for piece in pieces for key, raw in menu_fixture.menu_resource(piece).items()}
        raw, composition, menus, record = families.apply(raw, composition, menus, pieces)
        controller = pack_dbpf({RUL0: raw, NETWORK_INI: b'unchanged network ini'})
        menu = pack_dbpf(menus)
        base = {'pieces': pieces, 'overlay': {'rul0': composition}, families.KEY: record}
        selections = [[pieces[0], pieces[2]], [pieces[4], pieces[5]], [pieces[6], pieces[7]]]
        bundle = {'schema_version': 1, 'domain_id': 'high-speed-rail', 'groups': []}
        for index, members in enumerate(selections):
            bundle['groups'].append({'layout_id': 'fixture-layout-' + str(index),
                'layout': {'assembly_id': 'fixture-assembly-' + str(index),
                    'member_order': 'first-use-in-assembly',
                    'cycle_button': {'id': f'{0x6A47FEF0 + index:08x}', 'order': f'{0x7200FEF0 + index:08x}',
                        'title': 'Fixture assembly ' + str(index), 'description': 'Select individual components.'}},
                'scene': {'placements': [{'piece_id': piece['id']} for piece in members]}})
        icon = make_assembly_icon([[(0, 0, 15.5), (16, 16, 15.5)]], network_label='HSR')
        changed, new_menu, metadata, _audits = _transform(base, controller, menu, bundle, [icon] * 3)
        _actual(base, bundle, controller, menu, changed, new_menu, metadata)
        self.assertEqual(strict_dbpf(changed)[NETWORK_INI], b'unchanged network ini')
        kept = [row for row in rows(metadata['ordering_insertion']) if row[1][0] in (0xF801, 0xF803)]
        self.assertEqual([(keyword, states[0]) for keyword, states in kept],
                         [('rotationring', 0xF801), ('addtypes', 0xF803)])
        self.assertEqual(len(strict_dbpf(new_menu)), 4 * 5)  # Three assemblies, A/B anchor, unused last piece.
        for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION):
            key = (*prefix, int(pieces[1]['menu']['id'], 16))
            self.assertEqual(strict_dbpf(new_menu)[key], menus[key])

    def test_production_single_assembly_transform_preserves_alternative_family(self):
        from scp.menu_experiment import _check_actual_resources, _transformed
        from scp.menu_experiment_resources import make_assembly_icon
        raw, composition, menus, record = self.apply()
        controller = pack_dbpf({RUL0: raw, NETWORK_INI: b'unchanged network ini'})
        menu = pack_dbpf(menus)
        base = {'pieces': self.pieces, 'overlay': {'rul0': composition}, families.KEY: record}
        layout = {'assembly_id': 'fixture-single-assembly', 'member_order': 'first-use-in-assembly',
                  'cycle_button': {'id': '6a47fef0', 'order': '7200fef0',
                                   'title': 'Fixture assembly', 'description': 'Select individual components.'}}
        scene = {'placements': [{'piece_id': self.pieces[index]['id']} for index in (4, 0)]}
        icon = make_assembly_icon([[(0, 0, 15.5), (16, 16, 15.5)]], network_label='HSR')
        changed, new_menu, metadata, _audit, selected = _transformed(
            base, controller, menu, layout, scene, cycle_icon=icon, expected_cycle_icon=icon)
        _check_actual_resources(controller, menu, changed, new_menu, base, layout, selected)
        self.assertEqual(len(strict_dbpf(new_menu)), 12)
        self.assertEqual(metadata[families.KEY], composition[families.KEY])

    def test_single_member_assembly_cannot_consume_anchor_or_alternative(self):
        from scp.menu_experiment import _check_actual_resources, _transformed
        from scp.menu_experiment_resources import build_menu_experiment_resources, make_assembly_icon
        raw, composition, menus, record = self.apply()
        controller = pack_dbpf({RUL0: raw, NETWORK_INI: b'unchanged network ini'})
        menu = pack_dbpf(menus)
        base = {'pieces': self.pieces, 'overlay': {'rul0': composition}, families.KEY: record}
        layout = {'assembly_id': 'fixture-single-assembly', 'member_order': 'first-use-in-assembly',
                  'cycle_button': {'id': '6a47fef0', 'order': '7200fef0',
                                   'title': 'Fixture assembly', 'description': 'Select individual components.'}}
        icon = make_assembly_icon([[(0, 0, 15.5), (16, 16, 15.5)]], network_label='HSR')
        for piece in (self.pieces[1], self.pieces[3]):
            scene = {'placements': [{'piece_id': piece['id']}]}
            with self.subTest(piece=piece['id']), self.assertRaisesRegex(ValueError, 'active alternative-piece menu family'):
                _transformed(base, controller, menu, layout, scene, cycle_icon=icon, expected_cycle_icon=icon)
        # This menu-only rewrite would otherwise satisfy the old single-root
        # audit: A's rotation row and unrelated B's AddTypes row remain exact.
        anchor = self.pieces[1]
        forged_menu, _ = build_menu_experiment_resources(menus, [anchor],
            cycle_button={**layout['cycle_button'], 'target_id': anchor['menu']['id']},
            cycle_icon=icon, expected_cycle_icon=icon)
        with self.assertRaisesRegex(ValueError, 'active alternative-piece menu family'):
            _check_actual_resources(controller, menu, controller, pack_dbpf(forged_menu), base, layout, [anchor])


if __name__ == '__main__':
    unittest.main()
