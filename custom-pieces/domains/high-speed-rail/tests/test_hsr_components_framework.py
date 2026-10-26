"""Optional registration, preflight failure isolation and family dispatch."""
from __future__ import annotations

from contextlib import redirect_stdout
from copy import deepcopy
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import Mock, patch

FRAMEWORK = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(FRAMEWORK / 'framework'))

from scp.catalog import load_catalog, select_pieces
from scp.build import preflight_allocations
from scp.recipes import build_piece
from scp.verify import check_piece_paths, _check_piece_geometry


def registration_module():
    spec = importlib.util.spec_from_file_location('scp_test_register_hsr_components',
                FRAMEWORK / 'domains/high-speed-rail/tools/register_hsr_components.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class HSRComponentRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='scp-component-registration-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        project = json.loads((FRAMEWORK / 'project.json').read_text())
        paths = ['project.json', project['profile'], project['allocations']]
        for domain in project['domains'].values():
            directory = Path(domain['path'])
            paths.extend(str(directory/name) for name in ('AGENTS.md', 'README.md'))
            paths.append(domain['registry'])
            registry = json.loads((FRAMEWORK/domain['registry']).read_text())
            paths.append(str(directory/registry['collections']))
            paths.extend(str(directory/relative) for relative in registry['assemblies'])
            for relative in registry['pieces']:
                manifest = directory/relative
                paths.append(str(manifest))
                icon = manifest.parent/'icon.png'
                if (FRAMEWORK/icon).is_file():
                    paths.append(str(icon))
        for relative in paths:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((FRAMEWORK / relative).read_bytes())
        self.module = registration_module()
        self.recipe = 'hsr_component_registration_probe'
        self.info = {self.recipe: {'cells': [(0, 0), (1, 0)], 'footprint': (2, 1),
                     'name': 'Registration Probe', 'description': 'Fixture matching paired ports.',
                     'effect_tag': 'hsrtest', 'kind': 'paired_straight'}}

    def manifest_path(self, piece):
        return self.root/'domains'/piece['domain']/'00_pieces'/piece['id']/'piece.json'

    def snapshot(self):
        return {str(path.relative_to(self.root)): path.read_bytes()
                for path in self.root.rglob('*') if path.is_file()}

    def register(self, info=None, recipes=None):
        with patch.object(self.module, 'make_icon', side_effect=lambda style: style.encode()), \
             patch.object(self.module, 'write_inventories'), redirect_stdout(io.StringIO()):
            return self.module.register_components(info or self.info,
                recipes or tuple(info or self.info), root=self.root)

    def test_registration_adds_only_optional_family_and_preserves_all_existing_allocations(self):
        before = load_catalog(self.root)
        manifests = {piece['id']: self.manifest_path(piece).read_bytes()
                     for piece in before['pieces']}
        project_bytes = (self.root/'project.json').read_bytes()
        report = self.register()
        after = load_catalog(self.root)
        slug = self.recipe.replace('_', '-')
        piece = next(piece for piece in after['pieces'] if piece['id'] == slug)
        self.assertEqual(report['added'], 1)
        self.assertFalse(report['installed'])
        self.assertEqual((self.root/'project.json').read_bytes(), project_bytes,
                         'Domain registration must not edit shared project routing')
        self.assertIn('Authoritative build definition', piece['purpose'])
        self.assertTrue((self.manifest_path(piece).parent/'icon.png').is_file())
        self.assertEqual(after['piece_sets']['hsr-all-components'], [slug])
        self.assertEqual([p['id'] for p in select_pieces(before)],
                         [p['id'] for p in select_pieces(after)])
        self.assertFalse(piece['enabled_by_default'])
        self.assertEqual(piece['status'], 'experimental')
        self.assertEqual(set(piece['game_tests'].values()), {'unverified'})
        self.assertEqual(piece['component']['kind'], 'paired_straight')
        self.assertEqual(piece['menu']['style'], slug)
        for name, members in before['piece_sets'].items():
            if name != 'hsr-all-components':
                self.assertEqual(after['piece_sets'][name], members)
        for old in before['pieces']:
            self.assertEqual(old, next(p for p in after['pieces'] if p['id'] == old['id']))
            self.assertEqual(after['_allocations']['pieces'][old['id']],
                             before['_allocations']['pieces'][old['id']])
            self.assertEqual(self.manifest_path(old).read_bytes(), manifests[old['id']])

    def test_rerun_is_idempotent(self):
        self.register()
        before = self.snapshot()
        self.assertEqual(self.register()['added'], 0)
        self.assertEqual(self.snapshot(), before)

    def test_existing_recipe_owner_keeps_independently_allocated_piece_id(self):
        self.register()
        old_id = self.recipe.replace('_', '-')
        new_id = 'independently-scaffolded-component'
        old_directory = self.root/'domains/high-speed-rail/00_pieces'/old_id
        new_directory = old_directory.with_name(new_id)
        old_directory.rename(new_directory)
        path = new_directory/'piece.json'
        piece = json.loads(path.read_text())
        piece['id'] = new_id
        path.write_text(json.dumps(piece, indent=2)+'\n')
        registry = self.root/'domains/high-speed-rail/domain.json'
        registry.write_text(registry.read_text().replace(old_id, new_id))
        collections = registry.parent/'collections.json'
        collections.write_text(collections.read_text().replace(old_id, new_id))
        ledger = self.root/'config/allocations.json'
        data = json.loads(ledger.read_text())
        data['pieces'][new_id] = data['pieces'].pop(old_id)
        ledger.write_text(json.dumps(data, indent=2)+'\n')
        before = self.snapshot()
        report = self.register()
        self.assertEqual(report['added'], 0)
        self.assertEqual(report['pieces'], [new_id])
        self.assertEqual(before, self.snapshot())

    def test_ambiguous_recipe_owner_fails_before_writing_any_subject(self):
        second = 'hsr_component_second_registration_probe'
        info = deepcopy(self.info)
        info[second] = deepcopy(info[self.recipe])
        info[second]['name'] = 'Second Registration Probe'
        self.register(info)
        piece = next(p for p in load_catalog(self.root)['pieces'] if p['recipe'] == second)
        path = self.manifest_path(piece)
        data = json.loads(path.read_text())
        data['recipe'] = self.recipe
        path.write_text(json.dumps(data, indent=2)+'\n')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'Ambiguous component recipe owner'):
            self.register()
        self.assertEqual(before, self.snapshot())

    def test_actual_family_registration_exposes_structural_cells_to_independent_verifier(self):
        from scp_hsr.hsr_components import INFO, RECIPES
        from scp_hsr.hsr_components_verify import _contract
        with patch.object(self.module, 'write_inventories'), redirect_stdout(io.StringIO()):
            self.module.register_components(root=self.root)
        catalog = load_catalog(self.root)
        for piece in catalog['pieces']:
            if piece['recipe'] in RECIPES:
                _contract(piece)
                self.assertEqual(piece['structural_cells'],
                                 [list(cell) for cell in INFO[piece['recipe']]['structural_cells']])

    def test_adapter_registration_preserves_existing_components_and_other_selections(self):
        from scp_hsr.hsr_components import INFO, RECIPES
        adapter = 'hsr_component_upper_paired_to_single_adapter'
        slug = adapter.replace('_', '-')
        registry_path = self.root/'domains/high-speed-rail/domain.json'
        ledger_path = self.root/'config/allocations.json'
        registry = json.loads(registry_path.read_text())
        collection_path = registry_path.parent/registry['collections']
        selections = json.loads(collection_path.read_text())
        ledger = json.loads(ledger_path.read_text())
        # Remove only the adapter in this private fixture. Its shared project
        # routing remains intact; domain registry and collections own membership.
        registry['pieces'] = [relative for relative in registry['pieces']
                              if Path(relative).parent.name != slug]
        for members in selections['collections'].values():
            if slug in members:
                members.remove(slug)
        ledger['pieces'].pop(slug, None)
        piece_directory = self.root/'domains/high-speed-rail/00_pieces'/slug
        (piece_directory/'piece.json').unlink(missing_ok=True)
        (piece_directory/'icon.png').unlink(missing_ok=True)
        registry_path.write_text(json.dumps(registry, indent=2)+'\n')
        collection_path.write_text(json.dumps(selections, indent=2)+'\n')
        ledger_path.write_text(json.dumps(ledger, indent=2)+'\n')
        with patch.object(self.module, 'write_inventories'), redirect_stdout(io.StringIO()):
            self.module.register_components(INFO, [recipe for recipe in RECIPES if recipe != adapter],
                                            root=self.root)
        before, files = load_catalog(self.root), self.snapshot()
        with patch.object(self.module, 'write_inventories'), redirect_stdout(io.StringIO()):
            report = self.module.register_components(root=self.root)
        after = load_catalog(self.root)
        self.assertEqual(report['added'], 1)
        self.assertEqual({piece['id'] for piece in after['pieces']} -
                         {piece['id'] for piece in before['pieces']}, {slug})
        self.assertEqual(len(after['piece_sets']['hsr-all-components']), len(RECIPES))
        for piece in before['pieces']:
            relative = f'domains/{piece["domain"]}/00_pieces/{piece["id"]}/piece.json'
            self.assertEqual((self.root/relative).read_bytes(), files[relative])
            self.assertEqual(after['_allocations']['pieces'][piece['id']],
                             before['_allocations']['pieces'][piece['id']])
        for name, members in before['piece_sets'].items():
            if name != 'hsr-all-components':
                self.assertEqual(after['piece_sets'][name], members)

    def test_later_invalid_grid_cannot_partly_register_earlier_valid_component(self):
        second = 'hsr_component_unsafe_probe'
        info = deepcopy(self.info)
        info[second] = {'cells': [(0, 0), (16, 0), (0, 1)], 'footprint': (17, 2),
                        'name': 'Unsafe Probe', 'description': 'Colliding engine keys.'}
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'unsafe auto-tile addresses'):
            self.register(info)
        self.assertEqual(self.snapshot(), before)

    def test_existing_component_coordinates_cannot_be_changed_on_rerun(self):
        self.register()
        before = self.snapshot()
        changed = deepcopy(self.info)
        changed[self.recipe]['cells'] = [(1, 0)]
        with self.assertRaisesRegex(ValueError, 'coordinates are frozen'):
            self.register(changed)
        self.assertEqual(self.snapshot(), before)

    def test_icon_failure_is_detected_before_registry_writes(self):
        before = self.snapshot()
        with patch.object(self.module, 'make_icon', side_effect=ValueError('invalid icon')):
            with self.assertRaisesRegex(ValueError, 'invalid icon'):
                self.module.register_components(self.info, tuple(self.info), root=self.root)
        self.assertEqual(self.snapshot(), before)

    def test_unserializable_metadata_cannot_partly_write_registration(self):
        self.info[self.recipe]['support_centers'] = {(0., 0.)}
        before = self.snapshot()
        with self.assertRaisesRegex(TypeError, 'not JSON serializable'):
            self.register()
        self.assertEqual(self.snapshot(), before)

    def test_sparse_wide_layout_reserves_multiple_families_without_false_dimension_cap(self):
        self.info[self.recipe].update(cells=[(0, 0), (16, 0), (32, 0)], footprint=(37, 1))
        self.register()
        catalog = load_catalog(self.root)
        piece = next(piece for piece in catalog['pieces'] if piece['recipe'] == self.recipe)
        reservation = catalog['_allocations']['pieces'][piece['id']]
        self.assertEqual(len(reservation['resource_blocks']), 3)
        base = int(reservation['tile_base'], 16)
        self.assertEqual(piece['tile_ids'], [f'{base + column*0x100:08x}'
                                            for column in (0, 16, 32)])


class HSRComponentDispatchTests(unittest.TestCase):
    def test_new_component_shadow_collision_is_checked_before_generation(self):
        piece = {'id': 'hsr-component-preflight-probe', 'recipe': 'hsr_component_preflight_probe',
                 'domain': 'high-speed-rail',
                 'puzzle_id': 'f8f0', 'tile_ids': ['7f5f0000'], 'preview_id': '7f5f0ff5',
                 'effect_name': 'preview_component_preflight', 'menu': {'id': '6a47f8f0'}}
        context = {'controller': {(0x0a5bcf4b, 0xaa5bcf57, 0x10000000): b'fixture'}}
        shadow = (0x7ab50e44, 0x2bc2759a, 0x7f5f0004)
        with self.assertRaisesRegex(ValueError, 'collide'):
            preflight_allocations(context, {shadow: ['other.dat']}, [piece])

    def test_actual_component_menu_icons_are_valid_and_all_distinct(self):
        from scp_hsr.hsr_components_layout import RECIPES
        from scp_hsr.icons import make_icon, validate_icon
        icons = [make_icon(recipe.replace('_', '-')) for recipe in RECIPES]
        self.assertEqual(len(set(icons)), len(RECIPES))
        for icon in icons:
            validate_icon(icon)
        with self.assertRaisesRegex(ValueError, 'Unknown SCP icon style'):
            make_icon('hsr-component-unknown-probe')

    def test_builder_dispatch_passes_original_context_and_keeps_framework_query_and_rotation_ring(self):
        module = types.ModuleType('scp_hsr.hsr_components')
        module.build_hsr_component = Mock(return_value=({}, 'component rules'))
        piece = {'recipe': 'hsr_component_dispatch_probe', 'id': 'hsr-component-dispatch-probe',
                 'domain': 'high-speed-rail',
                 'name': 'Dispatch Probe', 'puzzle_id': 'f8ff',
                 'tile_ids': ['7f5ff000'], 'preview_id': '7f5ffff5'}
        context = {'controller': {(0x0a5bcf4b, 0xaa5bcf57, 0x10000000): b'fixture'}, 'hsr': {}}
        with patch.dict(sys.modules, {'scp_hsr.hsr_components': module}):
            assets, rules = build_piece(piece, context)
        module.build_hsr_component.assert_called_once_with(piece, context)
        self.assertIn((0x2026960b, 0x2a592fd1, 0x7f5ff000), assets)
        self.assertIn('RotationRing = F8FF, 1F8FF, 2F8FF, 3F8FF, 4F8FF, 5F8FF, 6F8FF, 7F8FF', rules)
        self.assertTrue(rules.endswith('component rules'))

    def test_path_and_geometry_dispatch_use_independent_component_verifier(self):
        module = types.ModuleType('scp_hsr.hsr_components_verify')
        module.check_paths = Mock(return_value={'checked': 'paths'})
        module.check_models = Mock(return_value={'checked': 'models'})
        resources, piece, donors = {}, {'recipe': 'hsr_component_dispatch_probe',
                                       'domain': 'high-speed-rail'}, {'donor': b'bytes'}
        with patch.dict(sys.modules, {'scp_hsr.hsr_components_verify': module}):
            self.assertEqual(check_piece_paths(resources, piece), {'checked': 'paths'})
            self.assertEqual(_check_piece_geometry(resources, piece, donors), {'checked': 'models'})
        module.check_paths.assert_called_once_with(resources, piece)
        module.check_models.assert_called_once_with(resources, piece, donors)


if __name__ == '__main__':
    unittest.main()
