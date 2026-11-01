"""Register and dispatch the alternate alignment while retaining existing types."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'installer'),
               str(ROOT / 'domains/highway/implementation'),
               str(ROOT / 'domains/high-speed-rail/implementation')]

from scp import jsonc, model_shadows, native_approaches
from scp.catalog import load_catalog, number
from scp.dbpf import decompress, entries, pack_dbpf
from scp.verify import check_emitted_runtime_addresses, parse_rules
from scp_highway import ghsr_approaches, ghsr_crossing, recipes, verify
from scp_installer import service
import test_ghsr_crossing_integration as baseline

IDENTIFIER = ghsr_approaches.ALIGNMENT_B_PIECE_ID
ANCHOR = ghsr_approaches.PIECE_ID


def file_snapshot(root):
    return {path.relative_to(root).as_posix(): path.read_bytes()
            for path in root.rglob('*') if path.is_file()}


def previous_installation_pieces(catalog):
    """The three retained diamond assemblies and original reusable GHSR crossing."""
    registry = jsonc.load(ROOT / 'domains/highway/domain.jsonc')
    identifiers = {ANCHOR}
    for relative in registry['assemblies']:
        assembly = jsonc.load(ROOT / 'domains/highway' / relative)
        identifiers.update(row['piece_id'] for row in assembly['placements'])
    return [piece for piece in catalog['pieces'] if piece['id'] in identifiers]


class GHSRCrossingAlignmentRegistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog(ROOT)
        cls.pieces = {piece['id']: piece for piece in cls.catalog['pieces']}
        cls.piece = cls.pieces[IDENTIFIER]
        cls.anchor = cls.pieces[ANCHOR]

    def test_registration_b_preserves_every_previous_definition_and_allocation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            baseline.copy_registration_inputs(root, IDENTIFIER)
            before = file_snapshot(root)
            prior = load_catalog(root)
            allocations = deepcopy(prior['_allocations']['pieces'])
            old_pieces = {piece['id']: piece for piece in prior['pieces']}
            tool = baseline.registration_tool()
            result = tool.register_ghsr_crossing(root, alignment='b')
            self.assertTrue(result['registered'])
            current = load_catalog(root)
            for identifier, allocation in allocations.items():
                self.assertEqual(current['_allocations']['pieces'][identifier], allocation, identifier)
            current_pieces = {piece['id']: piece for piece in current['pieces']}
            for identifier, piece in old_pieces.items():
                self.assertEqual(current_pieces[identifier], piece, identifier)
            for field in ('puzzle_id', 'tile_ids', 'preview_id', 'menu', 'model_shadows', 'engineering'):
                self.assertEqual(current_pieces[IDENTIFIER][field], self.piece[field], field)
            mutable = {'config/allocations.jsonc', 'domains/highway/domain.jsonc',
                       'domains/highway/collections.jsonc'}
            for relative, raw in before.items():
                if relative not in mutable:
                    self.assertEqual((root / relative).read_bytes(), raw, relative)
            once = file_snapshot(root)
            again = tool.register_ghsr_crossing(root, alignment='b')
            self.assertFalse(again['registered'])
            self.assertEqual(file_snapshot(root), once)

    def test_b_links_to_a_button_without_rewriting_a_identity(self):
        self.assertEqual(self.piece['menu']['family_anchor'], ANCHOR)
        self.assertNotIn('family_anchor', self.anchor['menu'])
        self.assertEqual(self.anchor['puzzle_id'], 'f86e')
        self.assertEqual(self.anchor['menu']['id'], '6a47f86e')
        self.assertNotEqual(self.piece['puzzle_id'], self.anchor['puzzle_id'])
        self.assertNotEqual(self.piece['menu']['id'], self.anchor['menu']['id'])
        self.assertEqual(self.catalog['piece_sets']['ddrhw-diagonal-ghsr-crossing'], [ANCHOR])
        self.assertEqual(self.catalog['piece_sets']['ddrhw-diagonal-ghsr-crossing-alignment-b'], [IDENTIFIER])
        self.assertEqual(self.catalog['piece_sets']['ddrhw-diagonal-ghsr-crossing-alignments'], [ANCHOR, IDENTIFIER])

    def test_b_reserves_two_horizontal_hosts_and_independent_shadow_families(self):
        piece = self.piece
        self.assertEqual(piece['cells'], [[0, 0], [1, 0]])
        self.assertEqual(piece['footprint'], [2, 1])
        base = number(piece['tile_ids'][0])
        self.assertEqual(piece['tile_ids'], [f'{base:08x}', f'{base + 0x100:08x}'])
        allocations = self.catalog['_allocations']['pieces'][IDENTIFIER]
        self.assertEqual(allocations['resource_blocks'], [f'{base:08x}'])
        self.assertEqual(allocations['shadow_resource_families'], [f'{base + 0x800:08x}', f'{base + 0x900:08x}'])
        shadow_hosts = model_shadows.bindings(piece)
        self.assertEqual([row['cell'] for row in shadow_hosts], [[0, 0], [1, 0]])
        self.assertTrue(all(row['cast_shadow'] for row in shadow_hosts))
        self.assertFalse(model_shadows.enabled(piece))
        self.assertEqual(model_shadows.resource_keys(piece), set())
        self.assertEqual(len(set(model_shadows.reservation_ids(allocations))), 512)
        self.assertTrue(set(model_shadows.reservation_ids(allocations)).isdisjoint(
            model_shadows.reservation_ids(self.catalog['_allocations']['pieces'][ANCHOR])))

    def test_installer_finite_selection_includes_b_and_preserves_all_previous_36(self):
        selected = service.all_implemented_ids(ROOT)
        self.assertIn(ghsr_crossing.ALIGNMENT_B_RECIPE,
                      service.implemented_recipes_by_domain()['highway'])
        self.assertIn(IDENTIFIER, selected)
        previous = previous_installation_pieces(self.catalog)
        self.assertEqual(len(previous), 36)
        self.assertTrue({piece['id'] for piece in previous} <= set(selected))
        self.assertEqual(self.piece['dependencies'], self.anchor['dependencies'])
        self.assertEqual(self.piece['game_tests'], {key: 'unverified' for key in self.anchor['game_tests']})

    def test_native_helpers_of_previous_36_are_frozen_and_b_reuses_the_same_rule_table(self):
        previous = previous_installation_pieces(self.catalog)
        declarations = native_approaches.declarations(previous)
        self.assertEqual(len(previous), 36)
        self.assertEqual(len(declarations), 6)
        self.assertEqual(sum(len(row['approaches']) for row in declarations), 10)
        fingerprint = hashlib.sha256(json.dumps(declarations, sort_keys=True,
                                                 separators=(',', ':')).encode()).hexdigest()
        self.assertEqual(fingerprint, '865e0b8645663408e7011e4467a6d1c74d5bc8c19b5902bfed97cb9edc1d4b79')
        self.assertEqual(native_approaches.declarations([*previous, self.piece])[:-1], declarations)
        self.assertEqual(native_approaches.expected_solution_sections([*previous, self.piece]),
                         native_approaches.expected_solution_sections(previous))
        self.assertEqual(native_approaches.required_controller_resources([*previous, self.piece]),
                         native_approaches.required_controller_resources(previous))

    def test_dispatcher_builds_b_only_and_preserves_normal_finishing_and_shadow_owners(self):
        compiled = [((0, 0), b'first model', b'first paths'),
                    ((1, 0), b'second model', b'second paths')]
        context = {'controller': {'fixture': b'native controller'}}
        assets = {(1, 2, 3): b'finished source'}
        with patch('scp_highway.ghsr_crossing.build_alignment_b_channels', return_value=compiled) as build_b, \
             patch('scp_highway.ghsr_crossing.build_channels') as build_a, \
             patch('scp_highway.ghsr_approaches.check_native_continuation') as continuation, \
             patch('scp_highway.recipes.finish_piece', return_value=assets) as finish, \
             patch('scp_highway.model_shadows.add_shadows', return_value=assets) as shadows:
            saved, construction = recipes.build_piece(self.piece, context)
        build_b.assert_called_once_with(context)
        build_a.assert_not_called()
        continuation.assert_called_once_with(context['controller'])
        finish.assert_called_once_with(self.piece, context, compiled)
        shadows.assert_called_once_with(self.piece, context, compiled, assets)
        self.assertIs(saved, assets)
        rings, rules = parse_rules(construction)
        self.assertEqual(len(rings[0]), 8)
        fields = {}
        for name, value in rules[number(self.piece['puzzle_id'])]:
            fields.setdefault(name, []).append(value)
        self.assertEqual(fields['CellLayout'], ['ji.', 'ab<', 'hk.', '^..'])
        self.assertEqual(fields['ConsLayout'], ['...', '++<', '...', '^..'])
        report = check_emitted_runtime_addresses(fields, self.piece)
        self.assertEqual((report['cells_checked'], report['wrong_model_selections']), (2, 0))
        self.assertEqual(sum(' optional' in row for row in fields['CheckType']), 4)
        self.assertNotIn('Transpose', construction)


class GHSRCrossingAlignmentBPrivateNativeIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseline.GHSRCrossingPrivateNativeIntegrationTests.setUpClass.__func__(cls)
        cls.anchor = cls.piece
        cls.piece = next(piece for piece in load_catalog(ROOT)['pieces'] if piece['id'] == IDENTIFIER)

    def test_native_b_resources_have_all_six_journeys_and_share_actual_rules_with_a(self):
        controller_before = dict(self.context['controller'])
        assets, construction = recipes.build_piece(self.piece, self.context)
        saved = {key: decompress(value) for key, value in entries(pack_dbpf(assets)).items()}
        report = verify.check_paths(saved, self.piece)
        self.assertEqual(report['complete_directed_journeys'], 6)
        self.assertEqual(report['complete_native_boundary_members_checked'], 12)
        self.assertTrue(report['use_path_elevation'])
        self.assertTrue(report['native_helper_boundary_tangents_verified'])
        self.assertFalse(report['game_operation_tested'])
        self.assertTrue(verify.check_models(saved, self.piece, None))
        _rings, rules = parse_rules(construction)
        fields = {}
        for name, value in rules[number(self.piece['puzzle_id'])]:
            fields.setdefault(name, []).append(value)
        verify.check_construction_fields(fields, self.piece, saved)
        donors = {key: raw for resources in self.context.values() for key, raw in resources.items()}
        pair = [self.anchor, self.piece]
        rul1, record = native_approaches.compose_rul1(donors[native_approaches.RUL1], pair, donors)
        result = native_approaches.verify_rul1({native_approaches.RUL1: rul1}, pair,
                                               {native_approaches.OVERLAY: record}, donors)
        self.assertEqual(result['native_rul1_solutions_checked'], 12)
        self.assertFalse(native_approaches.dependency_keys(pair) & saved.keys())
        self.assertEqual(self.context['controller'], controller_before)


if __name__ == '__main__':
    unittest.main()
