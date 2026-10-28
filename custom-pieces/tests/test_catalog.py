"""Catalog safety checks that do not need SimCity 4 or installed NAM assets.

The fixture uses this project's real JSON manifests in a temporary directory.
Each rejection checks a practical failure case: silently selecting another
piece, writing outside the project, ambiguous identifiers, or missing evidence.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

FRAMEWORK = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(FRAMEWORK / 'framework'))
sys.path.insert(0, str(FRAMEWORK / 'domains/high-speed-rail/implementation'))

from scp import jsonc
from scp.catalog import load_catalog, release_status, select_pieces, validate_catalog


class CatalogTests(unittest.TestCase):
    def test_additive_wide_grid_that_aliases_in_game_is_rejected(self):
        catalog = self._catalog()
        piece = next(p for p in catalog['pieces'] if p['id'] == 'hsr-l2-over-tram-ground-mixed-crossing-90deg')
        piece['footprint'] = [17, 2]
        piece['cells'] = [[0, 0], [16, 0], [0, 1]]
        piece['tile_ids'] = [f'{0x7f503000+0x100*x+0x10*y:08x}' for x,y in piece['cells']]
        with self.assertRaisesRegex(ValueError, 'unsafe auto-tile addresses'):
            validate_catalog(catalog)

    def test_failed_placement_can_be_inspected_but_cannot_be_built(self):
        catalog = self._catalog()
        piece = next(p for p in catalog['pieces'] if p['id'] == 'hsr-l2-over-tram-ground-mixed-crossing-90deg')
        piece['game_tests']['placement'] = 'failed'
        with self.assertRaisesRegex(ValueError, 'failed placement tests.*hsr-l2-over-tram-ground-mixed-crossing-90deg'):
            select_pieces(catalog, [piece['id']])
        self.assertNotIn(piece['id'], {p['id'] for p in select_pieces(catalog)})

    def test_new_sparse_wide_example_allocator_preserves_unique_engine_keys(self):
        import contextlib
        import importlib.util
        import io
        from unittest.mock import patch
        spec = importlib.util.spec_from_file_location('scp_test_register_examples',
                    FRAMEWORK / 'domains/high-speed-rail/tools/register_directional_t.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        directory = self.root / 'domains/high-speed-rail/assets'
        directory.mkdir(parents=True, exist_ok=True)
        recipe = 'directional_hsr_wide_allocation_probe'
        info = {'cells': [(0,0),(16,0),(32,0)], 'footprint': (37,1),
                'effect_tag': 'testabc'}
        with patch.object(module, 'ROOT', self.root), patch.object(module, 'make_icon', return_value=b'fixture'):
            with contextlib.redirect_stdout(io.StringIO()):
                module.register_examples({recipe: info}, [recipe], 'allocation-probe')
        catalog = self._catalog()
        piece = next(p for p in catalog['pieces'] if p['recipe'] == recipe)
        allocation = catalog['_allocations']['pieces'][piece['id']]
        base = int(allocation['tile_base'],16)
        self.assertEqual(base & 0xfff, 0)
        self.assertEqual(piece['tile_ids'], [f'{base+(x<<8)+(y<<4):08x}' for x,y in piece['cells']])

    def test_registration_rejects_byte_key_collision_before_writing(self):
        import importlib.util
        from unittest.mock import patch
        spec = importlib.util.spec_from_file_location('scp_test_unsafe_registration',
                    FRAMEWORK / 'domains/high-speed-rail/tools/register_directional_t.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        before = {name:(self.root/name).read_bytes() for name in ('project.jsonc','config/allocations.jsonc')}
        recipe = 'directional_hsr_unsafe_grid_probe'
        info = {'cells':[(0,0),(16,0),(0,1)],'footprint':(17,2)}
        with patch.object(module,'ROOT',self.root):
            with self.assertRaisesRegex(ValueError,'unsafe auto-tile addresses'):
                module.register_examples({recipe:info},[recipe],'unsafe-probe')
        for name,raw in before.items():
            self.assertEqual((self.root/name).read_bytes(),raw)

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='scp-catalog-test-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.project = jsonc.loads((FRAMEWORK / 'project.jsonc').read_text())
        self.piece_paths = []
        self.registries = {}
        for domain in self.project.get('domains', {}).values():
            directory = self.root / domain['path']
            directory.mkdir(parents=True, exist_ok=True)
            for name in ('AGENTS.md', 'README.md'):
                (directory / name).write_text((FRAMEWORK / domain['path'] / name).read_text())
            registry = jsonc.loads((FRAMEWORK / domain['registry']).read_text())
            self.registries[registry['id']] = registry
            self._write(domain['registry'], registry)
            for relative in registry['pieces']:
                path = str(Path(domain['path']) / relative)
                self.piece_paths.append(path)
                self._write(path, jsonc.loads((FRAMEWORK / path).read_text()))
            for relative in [registry['collections'], *registry.get('assemblies', [])]:
                path = str(Path(domain['path']) / relative)
                self._write(path, jsonc.loads((FRAMEWORK / path).read_text()))
        profile_path = self.project['profile']
        self._write(profile_path, jsonc.loads((FRAMEWORK / profile_path).read_text()))
        if self.project.get('allocations'):
            relative = self.project['allocations']
            self._write(relative, jsonc.loads((FRAMEWORK / relative).read_text()))
        self._write('config/release.jsonc', jsonc.loads((FRAMEWORK / 'config/release.jsonc').read_text()))
        self._write('project.jsonc', self.project)
        self.default_count = sum(jsonc.loads((self.root / path).read_text())['enabled_by_default']
                                 for path in self.piece_paths)

    def _write(self, relative, value):
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.suffix == '.jsonc':
            jsonc.dump(destination, value, title=relative, summary='Isolated catalogue fixture.')
        else:
            destination.write_text(json.dumps(value, indent=2) + '\n')
        return destination

    def _catalog(self):
        return load_catalog(self.root)

    def test_domain_guides_are_required(self):
        (self.root / 'domains/high-speed-rail/AGENTS.md').unlink()
        with self.assertRaisesRegex(ValueError, 'requires agent and human guides'):
            self._catalog()

    def test_manifest_cannot_be_registered_in_another_domain(self):
        relative = self.piece_paths[0]
        piece = jsonc.loads((self.root / relative).read_text())
        piece['domain'] = 'highway'
        self._write(relative, piece)
        with self.assertRaisesRegex(ValueError, 'unknown transport domain'):
            self._catalog()

    def test_unknown_domain_is_rejected(self):
        relative = self.piece_paths[0]
        piece = jsonc.loads((self.root / relative).read_text())
        piece['domain'] = 'missing'
        self._write(relative, piece)
        with self.assertRaisesRegex(ValueError, 'unknown transport domain'):
            self._catalog()

    def test_domain_path_cannot_escape_project(self):
        self.project['domains']['highway']['path'] = '../outside'
        self._write('project.jsonc', self.project)
        with self.assertRaises(ValueError):
            self._catalog()

    def test_extra_allocation_cannot_occupy_another_pieces_reserved_empty_cell(self):
        catalog = self._catalog()
        ledger = catalog['_allocations']['pieces']
        owner = ledger['ghsr-ground-single-track-oneway-straight']
        base = int(owner['tile_base'],16)
        ledger['conflicting-allocation'] = {
            'puzzle_id':'f8ff','menu_id':'6a47f8ff',
            'tile_ids':[f'{base+0x100:08x}'],'preview_id':f'{base+0xff6:08x}',
            'state':'reserved-locally'}
        with self.assertRaisesRegex(ValueError, 'another piece'):
            validate_catalog(catalog)

    def test_large_width_uses_distinct_reserved_families_without_row_aliasing(self):
        catalog = self._catalog()
        piece = deepcopy(catalog['pieces'][0])
        piece.update(id='wide-three-families', name='Wide Three Families',
                     recipe='wide_three_families', status='draft', enabled_by_default=False,
                     puzzle_id='f8fe', footprint=[33,1], cells=[[0,0],[16,0],[32,0]],
                     tile_ids=['7f5fc000','7f5fd000','7f5fe000'],preview_id='7f5feff5',
                     effect_name='preview_wide_three_families',shadow_mappings=[])
        piece['menu'] = {'id':'6a47f8fe','order':'7011f8fe','style':'diagonal-hsr'}
        catalog['pieces'].append(piece)
        catalog['_allocations']['pieces'][piece['id']] = {
            **{key:piece[key] for key in ('puzzle_id','tile_ids','preview_id','cells')},
            'menu_id':piece['menu']['id'],'tile_base':'7f5fc000',
            'resource_blocks':['7f5fc000','7f5fd000','7f5fe000']}
        validate_catalog(catalog)
        self.assertEqual(len(set(piece['tile_ids'])),3)

    def _invalid_piece(self, field, value):
        catalog = self._catalog()
        catalog['pieces'][0][field] = value
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_loads_actual_manifests_and_resolves_profile(self):
        catalog = self._catalog()
        validate_catalog(catalog)
        self.assertEqual(catalog['_root'], self.root.resolve())
        self.assertIsInstance(catalog['_profile'], dict)
        self.assertEqual(catalog['_profile']['id'], 'nam50-rhd')
        self.assertEqual([p['id'] for p in catalog['pieces']],
                         [Path(relative).parent.name for relative in self.piece_paths])
        self.assertTrue(all(isinstance(piece, dict) for piece in catalog['pieces']))

    def test_source_package_version_matches_registered_project_version(self):
        from scp import __version__
        self.assertEqual(self._catalog()['version'], __version__)

    def test_default_selection_excludes_disabled_experiment(self):
        selected = select_pieces(self._catalog())
        self.assertEqual(len(selected), self.default_count)
        self.assertNotIn('hsr-l2-over-tram-ground-mixed-crossing-90deg', [p['id'] for p in selected])
        self.assertTrue(all(p['enabled_by_default'] for p in selected))

    def test_explicit_selection_can_select_disabled_piece(self):
        selected = select_pieces(self._catalog(), include=['hsr-l2-over-tram-ground-mixed-crossing-90deg'])
        self.assertEqual([p['id'] for p in selected], ['hsr-l2-over-tram-ground-mixed-crossing-90deg'])


    def test_explicit_selection_preserves_requested_order(self):
        selected = select_pieces(self._catalog(),
                                 include=['hsr-l2-over-tram-ground-mixed-crossing-90deg', 'hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg'])
        self.assertEqual([p['id'] for p in selected],
                         ['hsr-l2-over-tram-ground-mixed-crossing-90deg', 'hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg'])

    def test_explicit_empty_selection_does_not_fall_back_to_defaults(self):
        self.assertEqual(select_pieces(self._catalog(), include=[]), [])

    def test_unknown_explicit_selection_does_not_fall_back_to_defaults(self):
        with self.assertRaises(ValueError):
            select_pieces(self._catalog(), include=['misspelled-piece'])

    def test_duplicate_explicit_selection_is_rejected(self):
        with self.assertRaises(ValueError):
            select_pieces(self._catalog(), include=['hsr-l2-over-tram-ground-mixed-crossing-90deg', 'hsr-l2-over-tram-ground-mixed-crossing-90deg'])

    def test_registering_a_disabled_draft_does_not_break_default_selection(self):
        catalog = self._catalog()
        catalog['pieces'][1]['status'] = 'draft'
        validate_catalog(catalog)
        self.assertEqual(len(select_pieces(catalog)), self.default_count)
        self.assertNotIn('hsr-l2-over-tram-ground-mixed-crossing-90deg', [p['id'] for p in select_pieces(catalog)])

    def test_duplicate_or_outside_sparse_cells_are_rejected(self):
        for cells in ([[1, 0], [1, 0]], [[0, 0], [3, 0]], [[1, 0], [1, True]]):
            with self.subTest(cells=cells):
                catalog = self._catalog()
                piece = next(p for p in catalog['pieces'] if p['id'] == 'hsr-l2-two-track-s-curve-diagonal-left')
                piece['cells'] = cells
                with self.assertRaisesRegex(ValueError, 'cells'):
                    validate_catalog(catalog)

    def test_sparse_tile_ids_must_match_construction_cell_coordinates(self):
        catalog = self._catalog()
        piece = next(p for p in catalog['pieces'] if p['id'] == 'hsr-l2-two-track-s-curve-diagonal-left')
        piece['cells'][1], piece['cells'][2] = piece['cells'][2], piece['cells'][1]
        with self.assertRaisesRegex(ValueError, 'AutoTileBase'):
            validate_catalog(catalog)

    def test_diagonal_s_curves_keep_an_empty_construction_anchor(self):
        from scp.catalog import tile_base, piece_cells
        catalog = self._catalog()
        pieces = [p for p in catalog['pieces'] if p.get('category') == 'diagonal-s-curves']
        self.assertEqual(len(pieces), 4)
        for piece in pieces:
            self.assertNotIn([0, 0], piece_cells(piece))
            self.assertNotEqual(tile_base(piece), int(piece['tile_ids'][0], 16))
            self.assertEqual(len(piece['tile_ids']), 4)

    def test_recorded_cell_coordinates_cannot_be_shifted_under_saved_ids(self):
        catalog = self._catalog()
        piece = next(p for p in catalog['pieces'] if p['id'] == 'hsr-l2-two-track-s-curve-diagonal-left')
        piece['cells'] = [[x-1, y] for x, y in piece['cells']]
        # The shift is also an unsafe runtime bit-field allocation, which is
        # rejected before the frozen-coordinate comparison is reached.
        with self.assertRaisesRegex(ValueError, 'construction coordinates|unsafe auto-tile addresses'):
            validate_catalog(catalog)

    def test_piece_sets_reject_unknown_or_duplicate_members(self):
        for members in (['does-not-exist'], ['hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg', 'hsr-l2-over-ghsr-ground-two-track-crossing-lower-diagonal-45deg']):
            catalog = self._catalog()
            catalog['piece_sets']['broken-example'] = members
            with self.assertRaisesRegex(ValueError, 'piece set'):
                validate_catalog(catalog)

    def test_explicit_draft_selection_is_rejected_before_building(self):
        catalog = self._catalog()
        catalog['pieces'][1]['status'] = 'draft'
        with self.assertRaises(ValueError):
            select_pieces(catalog, include=['hsr-l2-over-tram-ground-mixed-crossing-90deg'])

    def test_duplicate_piece_ids_are_rejected_even_when_disabled(self):
        catalog = self._catalog()
        catalog['pieces'][1]['id'] = catalog['pieces'][0]['id']
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_duplicate_human_names_are_rejected_even_when_disabled(self):
        catalog = self._catalog()
        catalog['pieces'][1]['name'] = catalog['pieces'][0]['name']
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_duplicate_puzzle_roots_are_rejected(self):
        catalog = self._catalog()
        catalog['pieces'][1]['puzzle_id'] = catalog['pieces'][0]['puzzle_id']
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_duplicate_menu_ids_are_rejected(self):
        catalog = self._catalog()
        catalog['pieces'][1]['menu']['id'] = catalog['pieces'][0]['menu']['id']
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_duplicate_effect_names_are_rejected(self):
        catalog = self._catalog()
        catalog['pieces'][1]['effect_name'] = catalog['pieces'][0]['effect_name']
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_duplicate_tiles_are_rejected(self):
        catalog = self._catalog()
        catalog['pieces'][1]['tile_ids'] = [catalog['pieces'][0]['tile_ids'][0]]
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_tile_zoom_range_cannot_overlap_another_tile(self):
        catalog = self._catalog()
        original = int(catalog['pieces'][0]['tile_ids'][0], 16)
        catalog['pieces'][1]['tile_ids'] = [f'{original + 4:08x}']
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_preview_cannot_overlap_another_pieces_zoom_model(self):
        catalog = self._catalog()
        original = int(catalog['pieces'][0]['tile_ids'][0], 16)
        catalog['pieces'][1]['preview_id'] = f'{original + 4:08x}'
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_preview_cannot_overlap_its_own_zoom_model(self):
        catalog = self._catalog()
        original = int(catalog['pieces'][0]['tile_ids'][0], 16)
        catalog['pieces'][0]['preview_id'] = f'{original + 2:08x}'
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_duplicate_previews_are_rejected(self):
        catalog = self._catalog()
        catalog['pieces'][1]['preview_id'] = catalog['pieces'][0]['preview_id']
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_identifiers_must_fit_their_hexadecimal_width(self):
        examples = [('puzzle_id', '10000'), ('puzzle_id', '-001'),
                    ('puzzle_id', 'zzzz'), ('preview_id', '100000000'),
                    ('preview_id', '-0000001'), ('preview_id', 'not-hex')]
        for field, value in examples:
            with self.subTest(field=field, value=value):
                self._invalid_piece(field, value)

    def test_piece_id_is_a_safe_lowercase_slug(self):
        for value in ('../outside', '/absolute', 'MixedCase', 'contains space', '', 'a/b'):
            with self.subTest(value=value):
                self._invalid_piece('id', value)

    def test_recipe_must_be_a_safe_identifier(self):
        for value in ('../outside', 'contains space', 'MixedCase', '', 'a/b'):
            with self.subTest(value=value):
                self._invalid_piece('recipe', value)

    def test_unknown_piece_schema_is_rejected(self):
        self._invalid_piece('schema_version', 99)

    def test_unknown_project_schema_is_rejected(self):
        project = deepcopy(self.project)
        project['schema_version'] = 99
        self._write('project.jsonc', project)
        with self.assertRaises(ValueError):
            self._catalog()

    def test_unknown_profile_schema_is_rejected(self):
        profile_path = self.project['profile']
        profile = jsonc.loads((self.root / profile_path).read_text())
        profile['schema_version'] = 99
        self._write(profile_path, profile)
        with self.assertRaises(ValueError):
            self._catalog()

    def test_footprint_dimensions_have_finite_integer_bounds(self):
        for value in ([0, 2], [-1, 2], [65, 1], [1, 17], [1], [1, 2, 3],
                      [1.5, 2], [True, 2]):
            with self.subTest(value=value):
                self._invalid_piece('footprint', value)

    def test_declared_tile_count_matches_the_footprint(self):
        self._invalid_piece('tile_ids', ['5dd0f200'])

    def test_orientation_count_is_supported(self):
        for value in (0, 3, 32, True):
            with self.subTest(value=value):
                self._invalid_piece('orientation_count', value)

    def test_missing_game_test_evidence_is_rejected(self):
        catalog = self._catalog()
        del catalog['pieces'][0]['game_tests']
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_missing_specific_game_test_is_rejected(self):
        catalog = self._catalog()
        del catalog['pieces'][0]['game_tests']['no_unwanted_transfers']
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_existing_saved_city_identifier_cannot_be_reassigned(self):
        catalog = self._catalog()
        self.assertIn('_allocations', catalog)
        catalog['pieces'][0]['preview_id'] = '5dd0f325'
        with self.assertRaises(ValueError):
            validate_catalog(catalog)

    def test_allocation_ledger_contains_only_current_piece_ids(self):
        catalog = self._catalog()
        self.assertEqual(set(catalog['_allocations']['pieces']),
                         {piece['id'] for piece in catalog['pieces']})
        del catalog['pieces'][1]
        with self.assertRaisesRegex(ValueError, 'match current piece IDs exactly'):
            validate_catalog(catalog)

    def test_nonboolean_default_selection_is_rejected(self):
        self._invalid_piece('enabled_by_default', 'false')

    def test_piece_manifest_must_contain_a_json_object(self):
        self._write(self.piece_paths[0], ['not', 'a', 'manifest'])
        with self.assertRaises(ValueError):
            self._catalog()

    def test_duplicate_manifest_path_is_rejected(self):
        registry = deepcopy(self.registries['high-speed-rail'])
        registry['pieces'].append(registry['pieces'][0])
        self._write(self.project['domains']['high-speed-rail']['registry'], registry)
        with self.assertRaises(ValueError):
            self._catalog()

    def test_manifest_paths_cannot_escape_the_catalog(self):
        for value in ('../outside.json', '/tmp/outside.json', 'pieces\\outside.json'):
            with self.subTest(value=value):
                registry = deepcopy(self.registries['high-speed-rail'])
                registry['pieces'][0] = value
                self._write(self.project['domains']['high-speed-rail']['registry'], registry)
                with self.assertRaises(ValueError):
                    self._catalog()

    def test_profile_path_cannot_escape_the_catalog(self):
        project = deepcopy(self.project)
        project['profile'] = '../outside.json'
        self._write('project.jsonc', project)
        with self.assertRaises(ValueError):
            self._catalog()

    def test_manifest_symlink_cannot_escape_the_catalog(self):
        with tempfile.TemporaryDirectory(prefix='scp-catalog-outside-') as outside:
            source = Path(outside) / 'piece.json'
            source.write_text((self.root / self.piece_paths[0]).read_text())
            link = self.root / 'domains/high-speed-rail/00_pieces/external/piece.json'
            link.parent.mkdir(parents=True)
            link.symlink_to(source)
            registry = deepcopy(self.registries['high-speed-rail'])
            registry['pieces'][0] = '00_pieces/external/piece.json'
            self._write(self.project['domains']['high-speed-rail']['registry'], registry)
            with self.assertRaises(ValueError):
                self._catalog()

    def test_pending_release_gates_do_not_claim_public_readiness(self):
        catalog = self._catalog()
        result = release_status(self.root, catalog['pieces'])
        self.assertFalse(result['public_release_ready'])
        self.assertTrue(result['blocked'])

    def test_passing_gate_labels_without_evidence_are_not_sufficient(self):
        gates = jsonc.loads((self.root / 'config/release.jsonc').read_text())
        for value in gates.values():
            if isinstance(value, dict) and 'status' in value:
                value['status'], value['evidence'] = 'passed', None
        self._write('config/release.jsonc', gates)
        pieces = self._catalog()['pieces']
        for piece in pieces:
            piece['status'] = 'tested'
            piece['game_tests'] = dict.fromkeys(piece['game_tests'], 'passed')
            piece['provenance']['redistribution'] = 'permission-recorded'
        self.assertFalse(release_status(self.root, pieces)['public_release_ready'])

    def test_release_gate_labels_do_not_replace_piece_game_tests(self):
        gates = jsonc.loads((self.root / 'config/release.jsonc').read_text())
        for value in gates.values():
            if isinstance(value, dict) and 'status' in value:
                value['status'], value['evidence'] = 'passed', 'test-fixture-evidence'
        self._write('config/release.jsonc', gates)
        pieces = self._catalog()['pieces']
        for piece in pieces:
            piece['provenance']['redistribution'] = 'permission-recorded'
        self.assertFalse(release_status(self.root, pieces)['public_release_ready'])

    def test_complete_mock_evidence_can_pass_release_assessment(self):
        gates = jsonc.loads((self.root / 'config/release.jsonc').read_text())
        for value in gates.values():
            if isinstance(value, dict) and 'status' in value:
                value['status'], value['evidence'] = 'passed', 'test-fixture-evidence'
        self._write('config/release.jsonc', gates)
        # This positive fixture represents a catalogue after design approval.
        # Passing game labels alone must not erase real recorded objections.
        for relative in self.piece_paths:
            piece=jsonc.loads((self.root/relative).read_text())
            piece.pop('design_review',None)
            self._write(relative,piece)
        pieces = self._catalog()['pieces']
        for piece in pieces:
            piece['status'] = 'tested'
            piece['game_tests'] = dict.fromkeys(piece['game_tests'], 'passed')
            piece['provenance']['redistribution'] = 'permission-recorded'
        result = release_status(self.root, pieces)
        self.assertTrue(result['public_release_ready'])
        self.assertEqual(result['blocked'], [])


if __name__ == '__main__':
    unittest.main()
