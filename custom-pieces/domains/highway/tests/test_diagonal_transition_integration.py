"""Exercise finite registration, retained allocations, and connector services."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'installer'),
               str(ROOT / 'domains/highway/implementation'),
               str(ROOT / 'domains/high-speed-rail/implementation')]

from scp.catalog import load_catalog
from scp import piece_menu_families
from scp.subject_sources import piece_id_for_recipe, piece_name_for_recipe, piece_directory
from scp_highway import connections
from scp_highway import diagonal_transition_layout as layout
from scp_highway import diagonal_transition_variants as variants
from scp_highway import diagonal_transition_contracts as contracts
from scp_highway import orthogonal_transition_variants as orthogonal
from scp_installer import service


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tree_bytes(root):
    return {path.relative_to(root).as_posix(): path.read_bytes()
            for path in root.rglob('*') if path.is_file()}


class DiagonalProviderServiceTests(unittest.TestCase):
    def test_four_standalone_selectors_fit_the_shared_catalogue_namespace(self):
        tool = module_at('diagonal_collection_names_test', ROOT / 'domains/highway/tools/register_diagonal_transition.py')
        names = [tool.COLLECTION, *(tool.COLLECTION+'-'+suffix for suffix in tool.SELECTOR_SUFFIXES)]
        self.assertEqual(len(set(names)), 5)
        self.assertTrue(all(re.fullmatch('[a-z][a-z0-9-]{1,63}', name) for name in names))

    def test_ground_service_is_rhw4_in_each_phase_and_legacy_avenue_is_preserved(self):
        for key in variants.VARIANTS:
            record = variants.record_for(key)
            piece = {'id': record.piece_id, 'recipe': record.recipe, 'domain': 'highway',
                     'diagonal_transition_variant': key, 'diagonal_transition_alignment': 'a'}
            for height, expected in ((0., 'rhw-4-l0'), (7.5, 'dd-rhw-l1'),
                                     (15., 'dd-rhw-l2'), (4., 'dd-rhw-ground-transition')):
                with self.subTest(variant=key, height=height):
                    actual = connections.service_classifier(piece, 1, height)
                    self.assertEqual(actual['variant'], expected)
                    self.assertEqual(actual['service_network'], 'road')
                    self.assertEqual(actual['traffic_modes'], ['car'])
            self.assertEqual(connections.service_classifier(piece, 2, 0.)['variant'], 'avenue-sidewalk')
        legacy = {'recipe': connections.CORE}
        self.assertEqual(connections.service_classifier(legacy, 1, 0.)['variant'], 'avenue-ground')
        self.assertEqual(connections.service_classifier(legacy, 1, 4.)['variant'], 'access-ramp')

    def test_registration_rejects_closed_review_and_corrupt_mask_before_any_write(self):
        tool = module_at('diagonal_registration_gate_test', ROOT / 'domains/highway/tools/register_diagonal_transition.py')
        for field in ('physical_layout_reviewed', 'native_shoulder_ownership_reviewed'):
            candidate = deepcopy(layout.module_catalog())
            candidate['physical_layout_reviewed'] = True
            candidate['native_shoulder_ownership_reviewed'] = True
            candidate[field] = False
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                with patch.object(tool.layout, 'module_catalog', return_value=candidate), \
                     self.assertRaisesRegex(ValueError, 'requires reviewed physical layout'):
                    tool.register(root)
                self.assertEqual(tree_bytes(root), {})


class DiagonalRegistrationIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog(ROOT)
        cls.pieces = [next(piece for piece in cls.catalog['pieces'] if piece['id'] == identifier)
                      for identifier in variants.PIECE_IDS]

    def test_registration_preserves_every_prior_allocation_and_definition_and_is_idempotent(self):
        tool = module_at('diagonal_registration_integration', ROOT / 'domains/highway/tools/register_diagonal_transition.py')
        helper = module_at('diagonal_registration_fixture', Path(__file__).with_name('test_ghsr_crossing_integration.py'))
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            helper.copy_registration_inputs(root, variants.PIECE_IDS)
            before = tree_bytes(root)
            allocations = deepcopy(load_catalog(root)['_allocations']['pieces'])
            result = tool.register(root)
            self.assertTrue(result['registered'])
            self.assertEqual(result['new_piece_ids'], list(variants.PIECE_IDS))
            current = load_catalog(root)
            for identifier, allocation in allocations.items():
                self.assertEqual(current['_allocations']['pieces'][identifier], allocation)
            mutable = {'config/allocations.jsonc', 'domains/highway/domain.jsonc',
                       'domains/highway/collections.jsonc'}
            for relative, raw in before.items():
                if relative not in mutable:
                    self.assertEqual((root / relative).read_bytes(), raw, relative)
            for piece in self.pieces:
                generated = next(row for row in current['pieces'] if row['id'] == piece['id'])
                for field in ('puzzle_id', 'tile_ids', 'preview_id', 'menu', 'engineering',
                              'cells', 'footprint', 'model_shadows'):
                    self.assertEqual(generated[field], piece[field], field)
                self.assertEqual(len(generated['cells']), 24)
                self.assertEqual(set(generated['game_tests'].values()), {'unverified'})
            once = tree_bytes(root)
            self.assertFalse(tool.register(root)['registered'])
            self.assertEqual(tree_bytes(root), once)
            candidate = deepcopy(layout.module_catalog())
            candidate['types'][0]['cells'] = candidate['types'][0]['cells'][:-1]
            with patch.object(tool.layout, 'module_catalog', return_value=candidate), \
                 self.assertRaises(ValueError):
                tool.register(root)
            self.assertEqual(tree_bytes(root), once)

    def test_four_choice_diagonal_family_preserves_the_separate_orthogonal_family(self):
        self.assertEqual(self.catalog['piece_sets']['ddrhw-diagonal-ground-transition-alignment-a'], list(variants.PIECE_IDS))
        self.assertEqual(self.catalog['piece_sets']['ddrhw-orthogonal-ground-transition'], list(orthogonal.PIECE_IDS))
        self.assertEqual(piece_menu_families.hidden_members(self.pieces), set(variants.PIECE_IDS[1:]))
        self.assertEqual(piece_menu_families.manifest_record(self.pieces)['families'],
                         [{'anchor_id': variants.PIECE_ID, 'member_ids': list(variants.PIECE_IDS)}])
        for piece in self.pieces:
            self.assertEqual(piece_menu_families.hidden_members([piece]), set())
            self.assertIsNone(piece_menu_families.manifest_record([piece]))

    def test_each_recipe_and_contract_has_one_distinct_registered_owner(self):
        self.assertEqual(len({contracts.reference(piece) for piece in self.pieces}), 4)
        for piece in self.pieces:
            with self.subTest(piece=piece['id']):
                self.assertEqual(piece_id_for_recipe(piece['recipe'], ROOT), piece['id'])
                self.assertEqual(piece_name_for_recipe(piece['recipe'], ROOT), piece['name'])
                self.assertEqual(piece_directory(piece['recipe'], ROOT).name, piece['id'])
                self.assertIn(piece['recipe'], service.implemented_recipes_by_domain()['highway'])
                self.assertIn(piece['id'], service.all_implemented_ids(ROOT))
                sources = connections.connector_source_files(piece['id'])
                self.assertIn('domains/highway/implementation/scp_highway/diagonal-transition-native-inputs.jsonc', sources)
                self.assertIn('domains/highway/implementation/scp_highway/diagonal-transition-collar-inputs.jsonc', sources)
                self.assertIn('domains/highway/implementation/scp_highway/diagonal-transition-native-obstacle-inputs.jsonc', sources)


if __name__ == '__main__':
    unittest.main()
