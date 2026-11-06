"""Controller aliases preserve canonical geometry and placement definitions."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from scp import jsonc, multi_assembly_menu
from scp import piece_menu_families
from scp.assembly_aliases import add_aliases, verify_aliases
from scp.build import NETWORK_INI, RUL0
from scp.catalog import load_catalog
from scp.dbpf import pack_dbpf
from scp.rul0 import compose_rul0, with_feature_sequence
from scp.verify import strict_dbpf

from test_menu_experiment import menu_resource


NATIVE = (
    b'; retained original comment\r\n'
    b'[Ordering]\r\n'
    b'RotationRing = 1234, 11234\r\n'
    b'AddTypes = 3333, 13333\r\n'
    b'[HighwayIntersectionInfo_0x00003456]\r\n'
    b'AutoTileBase = 0x57030000\r\n'
)
STAMP = 0xF83C
TERMINAL = 0xF82B
STAMP_ALIAS = 0xF890
TERMINAL_ALIAS = 0xF891


def fragment(root, tile):
    states = [root + turn * 0x10000 for turn in range(8)]
    lines = [
        'RotationRing = ' + ', '.join(f'{state:X}' for state in states),
        '',
        f'[HighwayIntersectionInfo_0x{root:08X}]',
        f'Piece = 0.0, 0.0, 0, 0, 0x{tile + 0xFF5:08X}',
        'PreviewEffect = preview_scp_hw_test',
        'CellLayout = a<',
        'CheckType = a - avenue: 0x01000003',
        'ConsLayout = #<',
        f'AutoTileBase = 0x{tile:08X}',
        'ReplacementIntersection = 0, 0',
        f'PlaceQueryID = 0x{tile:08X}',
        'HandleOffset = 0, 1',
        'Costs = 1000',
    ]
    for turn, state in enumerate(states[1:], 1):
        source = states[0 if turn < 4 else turn - 4]
        lines.extend(('', f'[HighwayIntersectionInfo_0x{state:08X}]', f'CopyFrom = 0x{source:X}'))
        if turn < 4:
            lines.append(f'Rotate = {turn}')
    return '\r\n'.join(lines) + '\r\n'


class AssemblyAliasTests(unittest.TestCase):
    def setUp(self):
        self.original, self.composition = compose_rul0(
            NATIVE, [fragment(STAMP, 0x7F59D000), fragment(TERMINAL, 0x7F587000)])
        self.aliases = [(STAMP, STAMP_ALIAS), (TERMINAL, TERMINAL_ALIAS)]
        self.expanded, self.expanded_composition = add_aliases(self.original, self.composition, self.aliases)

    def verify(self, saved=None, composition=None):
        verify_aliases(
            self.original, self.composition, self.expanded if saved is None else saved,
            self.expanded_composition if composition is None else composition, self.aliases)

    def test_aliases_restore_original_bytes_and_can_join_an_independent_tab_cycle(self):
        changed, composition = with_feature_sequence(
            self.expanded, self.expanded_composition, [STAMP_ALIAS, TERMINAL_ALIAS])
        self.assertIn(b'AddTypes = F891, 1F891', changed)
        self.assertIn(b'RotationRing = F83C, 1F83C', changed)
        self.assertTrue(composition['suffix'].startswith(self.composition['suffix']))
        self.assertEqual(changed[:changed.index(b';BEGIN SIMONS CUSTOM PIECES ROTATIONS')],
                         self.original[:self.original.index(b';BEGIN SIMONS CUSTOM PIECES ROTATIONS')])
        self.verify(changed, composition)

    def test_aliases_keep_preview_adaptive_checks_and_tile_addresses_exact(self):
        added = self.expanded_composition['suffix'][len(self.composition['suffix']):]
        self.assertIn('''[HighwayIntersectionInfo_0x0000F890]
Piece = 0.0, 0.0, 0, 0, 0x7F59DFF5
PreviewEffect = preview_scp_hw_test
CellLayout = a<
CheckType = a - avenue: 0x01000003
ConsLayout = #<
AutoTileBase = 0x7F59D000
ReplacementIntersection = 0, 0
PlaceQueryID = 0x7F59D000
HandleOffset = 0, 1
Costs = 1000'''.replace('\n', '\r\n'), added)
        self.assertIn('[HighwayIntersectionInfo_0x0005F890]\r\nCopyFrom = 0x1F890', added)
        self.assertLess(added.index('0x0000F890'), added.index('0x0000F891'))
        self.verify()

    def test_aliases_can_be_grouped_without_disturbing_an_existing_piece_family(self):
        anchor, alternative = 0xF840, 0xF841
        selected = [
            {'id': 'fixture-anchor', 'puzzle_id': f'{anchor:x}', 'domain': 'highway',
             'menu': {'id': '6a47f840'}},
            {'id': 'fixture-alternative', 'puzzle_id': f'{alternative:x}', 'domain': 'highway',
             'menu': {'id': '6a47f841', 'family_anchor': 'fixture-anchor'}},
        ]
        raw, composition = compose_rul0(NATIVE, [
            fragment(STAMP, 0x7F59D000), fragment(TERMINAL, 0x7F587000),
            fragment(anchor, 0x7F590000), fragment(alternative, 0x7F591000),
        ])
        menus = {(*prefix, 0x6A47F841): b'fixture' for prefix in piece_menu_families.PREFIXES}
        grouped, family_composition, _, _ = piece_menu_families.apply(raw, composition, menus, selected)
        expanded, expanded_metadata = add_aliases(grouped, family_composition, self.aliases)
        changed, final_composition = piece_menu_families.with_feature_sequence_preserving_families(
            expanded, expanded_metadata, [STAMP_ALIAS, TERMINAL_ALIAS])
        original_family = [line for line in grouped.splitlines()
                           if line.startswith((b'RotationRing = F840,', b'AddTypes = F841,'))]
        final_family = [line for line in changed.splitlines()
                        if line.startswith((b'RotationRing = F840,', b'AddTypes = F841,'))]
        self.assertEqual(final_family, original_family)
        self.assertEqual(len(final_family), 2)
        self.assertEqual(family_composition[piece_menu_families.KEY]['previous_ordering_insertion'],
                         composition['ordering_insertion'])
        verify_aliases(grouped, family_composition, changed, final_composition, self.aliases)

    def test_aliases_reject_native_or_existing_roots_and_duplicate_aliases(self):
        for aliases in (
                [(STAMP, 0x1234)], [(STAMP, 0x3333)], [(STAMP, 0x3456)],
                [(STAMP, TERMINAL)], [(STAMP, STAMP_ALIAS), (TERMINAL, STAMP_ALIAS)]):
            with self.subTest(aliases=aliases), self.assertRaisesRegex(ValueError, 'state already exists'):
                add_aliases(self.original, self.composition, aliases)

    def test_aliases_reject_missing_canonical_sources_and_outside_copy_references(self):
        with self.assertRaisesRegex(ValueError, 'complete canonical construction ring'):
            add_aliases(self.original, self.composition, [(0x1234, STAMP_ALIAS)])
        for invalid in ('0x1234', 'invalid'):
            raw, composition = compose_rul0(NATIVE, [
                fragment(STAMP, 0x7F59D000).replace('CopyFrom = 0xF83C', f'CopyFrom = {invalid}', 1)])
            with self.subTest(invalid=invalid), self.assertRaisesRegex(ValueError, 'noncanonical construction reference'):
                add_aliases(raw, composition, [(STAMP, STAMP_ALIAS)])

    def test_alias_verifier_rejects_changed_resources_references_and_canonical_body(self):
        old_suffix = self.composition['suffix']
        extra = self.expanded_composition['suffix'][len(old_suffix):]
        changes = (
            old_suffix + extra.replace('AutoTileBase = 0x7F59D000', 'AutoTileBase = 0x7F59E000', 1),
            old_suffix + extra.replace('CopyFrom = 0xF890', 'CopyFrom = 0xF83C', 1),
            old_suffix.replace('Costs = 1000', 'Costs = 1001', 1) + extra,
        )
        for suffix in changes:
            with self.subTest(suffix=suffix), self.assertRaisesRegex(ValueError, 'changed .*construction'):
                saved = self.expanded[:-len(self.expanded_composition['suffix'])] + suffix.encode('ascii')
                self.verify(saved, {**self.expanded_composition, 'suffix': suffix})

    def test_alias_verifier_rejects_wrong_rotation_row_even_with_current_metadata(self):
        old = self.expanded_composition['ordering_insertion']
        order = old.replace('F890, 1F890, 2F890', 'F890, 2F890, 1F890', 1)
        self.assertNotEqual(order, old)
        saved = self.expanded.replace(old.encode('ascii'), order.encode('ascii'), 1)
        with self.assertRaisesRegex(ValueError, 'exact eight-state Ordering row'):
            self.verify(saved, {**self.expanded_composition, 'ordering_insertion': order})

    def test_no_aliases_preserve_the_original_format(self):
        self.assertEqual(add_aliases(self.original, self.composition, []), (self.original, self.composition))
        verify_aliases(self.original, self.composition, self.original, self.composition, [])


class TrumpetTerminalCycleTests(unittest.TestCase):
    def test_terminal_states_follow_the_ordinary_cycle_and_preserve_canonical_rules(self):
        from scp_hsr.hsr_components import build_rules

        root = Path(__file__).resolve().parents[1]
        catalog = load_catalog(root)
        scene = next(row['scene'] for row in catalog['_assemblies'] if row['id'] == 'hsr-trumpet-straight-stem')
        pieces = {piece['id']: piece for piece in catalog['pieces']}
        selected = [pieces[piece_id] for piece_id in dict.fromkeys(row['piece_id'] for row in scene['placements'])]
        layout = jsonc.load(root / 'domains/high-speed-rail/menu-layout.jsonc')['layouts']['trumpet']
        ledger = catalog['_allocations']['assembly_aliases']
        group = {'layout_id': 'trumpet', 'domain_id': 'high-speed-rail', 'layout': layout,
                 'scene': scene, 'alias_reservations': {key: ledger[key] for key in layout['terminal_components'].values()}}
        bundle = {'schema_version': 2, 'groups': [group]}
        # Re-read the frozen bundle's serialization order during saved verification.
        saved_bundle = json.loads(json.dumps(bundle, sort_keys=True))
        canonical_roots = [int(piece['puzzle_id'], 16) for piece in selected]
        fragments = ['RotationRing = ' + ', '.join(f'{puzzle + turn * 0x10000:X}' for turn in range(8))
                     + '\r\n\r\n' + build_rules(piece) for puzzle, piece in zip(canonical_roots, selected)]
        original, composition = compose_rul0(NATIVE, fragments)
        old_controller = pack_dbpf({RUL0: original, NETWORK_INI: b'Native Network INI'})
        old_menu = pack_dbpf({key: value for piece in selected for key, value in menu_resource(piece).items()})
        base = {'pieces': selected, 'overlay': {'rul0': composition}}
        controller, menu, saved, _ = multi_assembly_menu._transform(base, old_controller, old_menu, bundle, [None])
        multi_assembly_menu._actual(base, saved_bundle, old_controller, old_menu, controller, menu, saved)
        self.assertEqual(saved['feature_sequences']['groups'], [canonical_roots + [0xF891, 0xF892, 0xF893]])
        self.assertTrue(saved['suffix'].startswith(composition['suffix']))
        self.assertEqual(len(strict_dbpf(menu)), 4)
        self.assertEqual(saved['suffix'].count('monorail: 0x02000200 road: 0x00010100 optional'), 1)
        self.assertEqual(saved['suffix'].count('monorail: 0x00020002 road: 0x01010000 optional'), 2)
        saved_groups = multi_assembly_menu._groups(base, saved_bundle)
        terminals = saved_groups[0][0]['_terminals']
        self.assertEqual([(row['placement_id'], row['cycle_position'], row['rotation_degrees_ccw'], row['helper_cell_xy'])
                          for row in terminals], [('P04', 15, 0, [7, -1]), ('P08', 16, 180, [19, 13]),
                                                  ('P01', 17, 0, [0, 13])])

        original_suffix = saved['suffix'].encode('ascii')
        bad_suffix = original_suffix.replace(b'road: 0x00010100 optional', b'road: 0x00010000 optional', 1)
        resources = strict_dbpf(controller)
        resources[RUL0] = resources[RUL0][:-len(original_suffix)] + bad_suffix
        with self.assertRaisesRegex(ValueError, 'Saved HSR terminal marker'):
            multi_assembly_menu._actual(base, saved_bundle, old_controller, old_menu,
                                        pack_dbpf(resources), menu, {**saved, 'suffix': bad_suffix.decode('ascii')})

        altered = deepcopy(saved_bundle)
        altered['groups'][0]['alias_reservations']['trumpet-west-native-hsr-terminal']['placement_id'] = 'P08'
        with self.assertRaisesRegex(ValueError, 'reservation differs from the selected placement'):
            multi_assembly_menu._groups(base, altered)

        altered = deepcopy(saved_bundle)
        altered['groups'][0]['scene']['terminal_approaches']['P01']['helper_cell_xy'] = [1, 13]
        with self.assertRaisesRegex(ValueError, 'reviewed native HSR approaches'):
            multi_assembly_menu._groups(base, altered)

        # Earlier package proofs carry their old layout, reservations, and scene together.
        previous_bundle = deepcopy(saved_bundle)
        previous = previous_bundle['groups'][0]
        straight = 'hsr-l2-two-track-straight'
        for direction, current_label, old_label, edge, x, helper_x in (
                ('E', 'P08', 'P09', 'north', 19, 20), ('W', 'P01', 'P22', 'south', 0, -1)):
            alias = previous['layout']['terminal_components'].pop(current_label)
            previous['layout']['terminal_components'][old_label] = alias
            previous['alias_reservations'][alias].update(placement_id=old_label, piece_id=straight)
            previous_scene = previous['scene']
            previous_scene['terminal_approaches'].pop(current_label)
            previous_scene['terminal_approaches'][old_label] = {
                'helper_edge': edge, 'arm': direction, 'helper_cell_xy': [helper_x, 13]}
            previous_scene['placements'].append({'instance_id': old_label, 'piece_id': straight,
                                                 'display_origin_tiles_en': [x, 13], 'rotation_degrees_ccw': 270})
        previous_controller, previous_menu, previous_rules, _ = multi_assembly_menu._transform(
            base, old_controller, old_menu, previous_bundle, [None])
        multi_assembly_menu._actual(base, previous_bundle, old_controller, old_menu,
                                    previous_controller, previous_menu, previous_rules)
        self.assertEqual(previous_rules['feature_sequences']['groups'], saved['feature_sequences']['groups'])
        self.assertEqual(previous_rules['suffix'].count('monorail: 0x02000200 road: 0x00010100 optional'), 3)
