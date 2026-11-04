"""Register both missing side/traffic choices and guard their real dispatch."""
from copy import deepcopy
import importlib.util
from pathlib import Path
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
from scp.verify import check_emitted_runtime_addresses, parse_rules
from scp_highway import recipes, verify
from scp_highway import orthogonal_transition_variants as variants
from scp_highway import orthogonal_transition_verify as independent
from scp_highway import orthogonal_transition_contracts as contracts
from scp_installer import service


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encoded(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '1']
    for route in routes:
        lines.extend(str(route[key]) for key in ('transport', 'lane', 'entry', 'exit', 'compatibility'))
        lines.append(str(len(route['points'])))
        lines.extend(','.join(f'{value:.9f}' for value in point) for point in route['points'])
    return ('\n'.join(lines)+'\n').encode('ascii')


class OppositeTransitionIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog(ROOT)
        cls.pieces = [next(p for p in cls.catalog['pieces'] if p['id'] == identity)
                      for identity in variants.PIECE_IDS]

    def test_pair_registration_preserves_every_prior_allocation_and_old_definition(self):
        tool = module_at('opposite_transition_registration', ROOT / 'domains/highway/tools/register_orthogonal_transition.py')
        helper = module_at('opposite_registration_fixture', Path(__file__).with_name('test_ghsr_crossing_integration.py'))
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            helper.copy_registration_inputs(root, variants.PIECE_IDS[2:])
            before = deepcopy(load_catalog(root)['_allocations']['pieces'])
            protected = {root / 'domains/highway/00_pieces' / identity / 'piece.jsonc': None
                         for identity in variants.PIECE_IDS[:2]}
            protected = {path: path.read_bytes() for path in protected}
            result = tool.register_opposite_side_pair(root)
            self.assertTrue(result['registered'])
            self.assertEqual(result['new_piece_ids'], list(variants.PIECE_IDS[2:]))
            current = load_catalog(root)
            for identity, allocation in before.items():
                self.assertEqual(current['_allocations']['pieces'][identity], allocation)
            for path, raw in protected.items():
                self.assertEqual(path.read_bytes(), raw)
            for piece in self.pieces[2:]:
                generated = next(p for p in current['pieces'] if p['id'] == piece['id'])
                for key in ('puzzle_id', 'tile_ids', 'preview_id', 'menu', 'engineering', 'transition_variant'):
                    self.assertEqual(generated[key], piece[key], key)
            self.assertFalse(tool.register_opposite_side_pair(root)['registered'])

    def test_all_four_alternatives_share_one_cycle_and_each_new_type_works_alone(self):
        self.assertEqual(self.catalog['piece_sets']['ddrhw-orthogonal-ground-transition'], list(variants.PIECE_IDS))
        self.assertEqual(piece_menu_families.hidden_members(self.pieces), set(variants.PIECE_IDS[1:]))
        self.assertEqual(piece_menu_families.manifest_record(self.pieces)['families'],
                         [{'anchor_id': variants.PIECE_ID, 'member_ids': list(variants.PIECE_IDS)}])
        for piece in self.pieces[2:]:
            self.assertEqual(piece_menu_families.hidden_members([piece]), set())
            self.assertIsNone(piece_menu_families.manifest_record([piece]))

    def test_new_recipes_resolve_unique_owners_and_distinct_contract_paths(self):
        self.assertEqual(len(set(variants.RECIPES)), 4)
        self.assertEqual(len({contracts.reference(piece) for piece in self.pieces}), 4)
        for piece in self.pieces[2:]:
            with self.subTest(piece=piece['id']):
                self.assertEqual(piece_id_for_recipe(piece['recipe'], ROOT), piece['id'])
                self.assertEqual(piece_name_for_recipe(piece['recipe'], ROOT), piece['name'])
                self.assertEqual(piece_directory(piece['recipe'], ROOT).name, piece['id'])
                self.assertIn(piece['recipe'], service.implemented_recipes_by_domain()['highway'])
                self.assertIn(piece['id'], service.all_implemented_ids(ROOT))
                self.assertIn('/'+piece['id']+'/', contracts.reference(piece))

    def test_actual_provider_dispatch_preserves_native_sockets_and_flat_owned_core(self):
        for piece in self.pieces[2:]:
            with self.subTest(variant=piece['transition_variant']):
                key = variants.variant_of(piece)
                expected = independent.expected_cell_routes(variant=key)
                compiled = [(cell, b'model', encoded(routes)) for cell, routes in expected.items()]
                paths = {(0x296678f7, 0xa966883f, int(tile, 16)): raw
                         for tile, (_cell, _model, raw) in zip(piece['tile_ids'], compiled)}
                texture = int(piece['authored_texture_ids'][0], 16)
                extra = {(0x7ab50e44, 0x1abe787d, texture): b'texture'}
                context = {'controller': {}}
                with patch('scp_highway.orthogonal_transition.build_channels', return_value=compiled) as channels, \
                     patch('scp_highway.orthogonal_transition.build_textures', return_value=extra), \
                     patch('scp_highway.orthogonal_approaches.check_native_continuation'), \
                     patch('scp_highway.recipes.finish_piece', return_value=deepcopy(paths)), \
                     patch('scp_highway.model_shadows.add_shadows', side_effect=lambda p, c, m, a: a):
                    resources, raw = recipes.build_piece(piece, context)
                channels.assert_called_once_with(context, texture_id=texture, variant=key)
                self.assertEqual(resources, {**paths, **extra})
                rings, sections = parse_rules(raw)
                self.assertEqual(len(rings[0]), 8)
                self.assertNotIn('Transpose', raw)
                fields = {}
                for name, value in sections[int(piece['puzzle_id'], 16)]:
                    fields.setdefault(name, []).append(value)
                addresses = check_emitted_runtime_addresses(fields, piece)
                self.assertEqual((addresses['cells_checked'], addresses['wrong_model_selections']), (12, 0))
                self.assertEqual(sum(line.count('#') for line in fields['ConsLayout']), 12)
                report = verify.check_construction_fields(fields, piece, resources)
                self.assertEqual(report['native_orthogonal_outside_approaches_checked'], 3)
                for invalid in (0, 1, None, 'flat'):
                    from scp_highway.orthogonal_transition_construction import core_construction_data
                    with self.assertRaises(ValueError):
                        core_construction_data(compiled, flat_terrain=invalid)


if __name__ == '__main__':
    unittest.main()
