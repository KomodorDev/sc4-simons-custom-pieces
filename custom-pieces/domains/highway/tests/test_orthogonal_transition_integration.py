"""Guard registration, actual construction addresses, and scoped recipe dispatch."""
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
from scp.verify import check_emitted_runtime_addresses, parse_rules
from scp_highway import recipes, menu, verify, orthogonal_transition_verify as independent
from scp_installer import service


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encoded(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '1']
    for route in routes:
        lines += [str(route[key]) for key in ('transport', 'lane', 'entry', 'exit', 'compatibility')]
        lines.append(str(len(route['points'])))
        lines += [','.join(f'{value:.9f}' for value in point) for point in route['points']]
    return ('\n'.join(lines) + '\n').encode('ascii')


class OrthogonalTransitionIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog(ROOT)
        cls.piece = next(p for p in cls.catalog['pieces'] if p['id'] == independent.PIECE_ID)

    def test_registration_retains_prior_allocations_and_is_idempotent(self):
        tool = module_at('transition_registration_test', ROOT / 'domains/highway/tools/register_orthogonal_transition.py')
        helpers = module_at('transition_registration_inputs', Path(__file__).with_name('test_ghsr_crossing_integration.py'))
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            helpers.copy_registration_inputs(root, independent.PIECE_ID)
            before = deepcopy(load_catalog(root)['_allocations']['pieces'])
            self.assertTrue(tool.register(root)['registered'])
            current = load_catalog(root)
            for identifier, allocation in before.items():
                self.assertEqual(current['_allocations']['pieces'][identifier], allocation)
            piece = next(p for p in current['pieces'] if p['id'] == independent.PIECE_ID)
            for key in ('puzzle_id', 'tile_ids', 'preview_id', 'menu', 'engineering', 'model_shadows'):
                self.assertEqual(piece[key], self.piece[key], key)
            self.assertFalse(tool.register(root)['registered'])

    def test_real_construction_addresses_own_twelve_cells_and_leave_three_native_cells_unowned(self):
        compiled = [(cell, b'model', encoded(routes))
                    for cell, routes in independent.expected_cell_routes().items()]
        context = {'controller': {}}
        texture = int(self.piece['authored_texture_ids'][0], 16)
        extra = {(0x7ab50e44, 0x1abe787d, texture): b'texture'}
        paths = {(0x296678f7, 0xa966883f, int(tile, 16)): raw
                 for tile, (_cell, _model, raw) in zip(self.piece['tile_ids'], compiled)}
        with patch('scp_highway.orthogonal_transition.build_channels', return_value=compiled) as channels, \
             patch('scp_highway.orthogonal_transition.build_textures', return_value=extra), \
             patch('scp_highway.orthogonal_approaches.check_native_continuation') as continuation, \
             patch('scp_highway.recipes.finish_piece', return_value=deepcopy(paths)), \
             patch('scp_highway.model_shadows.add_shadows', side_effect=lambda p, c, m, a: a):
            resources, rules = recipes.build_piece(self.piece, context)
        channels.assert_called_once_with(context, texture_id=texture)
        continuation.assert_called_once_with(context['controller'])
        self.assertEqual(resources, {**paths, **extra})
        rings, sections = parse_rules(rules)
        self.assertEqual(len(rings[0]), 8)
        fields = {}
        for key, value in sections[int(self.piece['puzzle_id'], 16)]:
            fields.setdefault(key, []).append(value)
        report = check_emitted_runtime_addresses(fields, self.piece)
        self.assertEqual((report['cells_checked'], report['wrong_model_selections']), (12, 0))
        self.assertEqual(sum('optional' in row for row in fields['CheckType']), 3)
        self.assertNotIn('Transpose', rules)
        checked = verify.check_construction_fields(fields, self.piece, resources)
        self.assertEqual(checked['native_orthogonal_outside_approaches_checked'], 3)

    def test_finite_installer_selection_and_distinct_canonical_icon(self):
        self.assertIn(independent.RECIPE, service.implemented_recipes_by_domain()['highway'])
        self.assertIn(independent.PIECE_ID, service.all_implemented_ids(ROOT))
        self.assertEqual(self.catalog['piece_sets']['ddrhw-orthogonal-ground-transition'], [independent.PIECE_ID])
        self.assertEqual(set(self.piece['dependencies']), {'controller', 'dd_rhw', 'rhw_core', 'rhw4', 'rhw4_textures'})
        icon = ROOT / 'domains/highway/00_pieces' / independent.PIECE_ID / 'icon.png'
        self.assertEqual(icon.read_bytes(), menu.make_icon('ddrhw-transition'))
        self.assertNotEqual(icon.read_bytes(), menu.make_icon('ddrhw-ramp'))


if __name__ == '__main__':
    unittest.main()
