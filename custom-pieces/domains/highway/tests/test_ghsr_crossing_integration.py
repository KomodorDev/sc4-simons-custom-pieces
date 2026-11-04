"""Register, select, dispatch, and independently verify the new crossing."""
from copy import deepcopy
import hashlib
import importlib.util
import io
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'installer'),
               str(ROOT / 'domains/highway/implementation'),
               str(ROOT / 'domains/high-speed-rail/implementation')]

from scp import jsonc, model_shadows, native_approaches
from scp.catalog import load_catalog, number
from scp.dbpf import entries, decompress, exemplar, pack_dbpf
from scp.menu import ICON, MENU_EXEMPLAR
from scp.paths import local_settings
from scp.verify import check_emitted_runtime_addresses, parse_rules
from scp_highway import ghsr_approaches, ghsr_crossing, menu, piece_icons, recipes, verify
from scp_installer import service

IDENTIFIER = ghsr_approaches.PIECE_ID
DIRECTORY = ROOT / 'domains/highway/00_pieces' / IDENTIFIER


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def registration_tool():
    source = ROOT / 'domains/highway/tools/register_highway_pieces.py'
    spec = importlib.util.spec_from_file_location('scp_highway_registration_integration', source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def copy_registration_inputs(target, identifier=IDENTIFIER):
    """Copy catalogue inputs and icons, removing selected exact subjects everywhere."""
    identifiers = {identifier} if isinstance(identifier, str) else set(identifier)
    project = jsonc.load(ROOT / 'project.jsonc')
    selected = {'project.jsonc', project['profile'], project['allocations']}
    for domain in project['domains'].values():
        directory = Path(domain['path'])
        selected.update(str(directory / filename) for filename in ('AGENTS.md', 'README.md'))
        selected.add(domain['registry'])
        registry = jsonc.load(ROOT / domain['registry'])
        selected.add(str(directory / registry['collections']))
        for relative in [*registry['pieces'], *registry.get('assemblies', [])]:
            if any(item in Path(relative).parts for item in identifiers):
                continue
            selected.add(str(directory / relative))
            icon = directory / Path(relative).parent / 'icon.png'
            if (ROOT / icon).is_file():
                selected.add(str(icon))
    for relative in selected:
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, destination)
    ledger_path = target / project['allocations']
    ledger = jsonc.load(ledger_path)
    for item in identifiers:
        ledger['pieces'].pop(item, None)
    ledger_path.write_text(jsonc.document(ledger, source=ledger_path.read_text()), encoding='utf-8')
    domain = project['domains']['highway']
    registry_path = target / domain['registry']
    registry = jsonc.load(registry_path)
    registry['pieces'] = [relative for relative in registry['pieces']
                          if not any(item in Path(relative).parts for item in identifiers)]
    registry_path.write_text(jsonc.document(registry, source=registry_path.read_text()), encoding='utf-8')
    collections_path = target / domain['path'] / registry['collections']
    collections = jsonc.load(collections_path)
    collections['collections'] = {key: retained for key, value in collections['collections'].items()
                                  if (retained := [item for item in value if item not in identifiers])}
    collections_path.write_text(jsonc.document(collections, source=collections_path.read_text()), encoding='utf-8')


class GHSRCrossingRegistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog(ROOT)
        cls.piece = next(piece for piece in cls.catalog['pieces'] if piece['id'] == IDENTIFIER)

    def test_registration_preserves_every_previous_file_identity_and_is_idempotent(self):
        tool = registration_tool()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            copy_registration_inputs(root)
            before = {path.relative_to(root).as_posix(): path.read_bytes()
                      for path in root.rglob('*') if path.is_file()}
            prior = load_catalog(root)
            old_allocations = deepcopy(prior['_allocations']['pieces'])
            result = tool.register_ghsr_crossing(root)
            self.assertTrue(result['registered'])
            current = load_catalog(root)
            for identifier, allocation in old_allocations.items():
                self.assertEqual(current['_allocations']['pieces'][identifier], allocation)
            mutable = {'config/allocations.jsonc', 'domains/highway/domain.jsonc',
                       'domains/highway/collections.jsonc'}
            for relative, raw in before.items():
                if relative not in mutable:
                    self.assertEqual((root / relative).read_bytes(), raw, relative)
            crossing = next(piece for piece in current['pieces'] if piece['id'] == IDENTIFIER)
            for field in ('puzzle_id', 'tile_ids', 'preview_id', 'menu', 'model_shadows'):
                self.assertEqual(crossing[field], self.piece[field])
            once = {path.relative_to(root).as_posix(): path.read_bytes()
                    for path in root.rglob('*') if path.is_file()}
            again = tool.register_ghsr_crossing(root)
            self.assertFalse(again['registered'])
            self.assertEqual(once, {path.relative_to(root).as_posix(): path.read_bytes()
                                    for path in root.rglob('*') if path.is_file()})

    def test_two_owned_cells_and_two_shadow_families_stay_in_one_reserved_block(self):
        piece = self.piece
        allocation = self.catalog['_allocations']['pieces'][IDENTIFIER]
        self.assertEqual(piece['recipe'], ghsr_crossing.RECIPE)
        self.assertEqual(piece['footprint'], [1, 2])
        self.assertEqual(piece['cells'], [[0, 0], [0, 1]])
        base = number(piece['tile_ids'][0])
        self.assertEqual(piece['tile_ids'], [f'{base:08x}', f'{base + 0x10:08x}'])
        self.assertEqual(allocation['resource_blocks'], [f'{base:08x}'])
        self.assertEqual(model_shadows.allocation_fields(piece),
                         {'shadow_resource_families': [f'{base + 0x800:08x}', f'{base + 0x900:08x}']})
        self.assertEqual(allocation['shadow_resource_families'],
                         model_shadows.allocation_fields(piece)['shadow_resource_families'])
        reserved = set(model_shadows.reservation_ids(allocation))
        self.assertEqual(len(reserved), 512)
        self.assertTrue(all((value & 0xFFFFF000) == base for value in reserved))
        self.assertTrue(all(row['cast_shadow'] for row in model_shadows.bindings(piece)))
        self.assertEqual(piece['model_shadows']['sun_profile'], 'sc4-default-67p5-45')
        self.assertFalse(model_shadows.enabled(piece))
        self.assertEqual(model_shadows.resource_keys(piece), set())
        self.assertEqual(len(native_approaches.approaches(piece)), 4)
        self.assertNotIn('native_dd_approaches', piece)

    def test_new_highways_menu_icon_is_distinct_and_legacy_icon_pixels_are_preserved(self):
        resources, report = menu.build_menu_resources(menu.portable_baseline(), self.piece)
        identifier = number(self.piece['menu']['id'])
        props = {int(prop['id'], 16): prop['values']
                 for prop in exemplar(resources[*MENU_EXEMPLAR, identifier])['properties']}
        self.assertEqual(props[0x4005], [0])
        self.assertNotIn(0x4001, props)
        self.assertEqual(report['menu'], 'Highways')
        icon = resources[*ICON, identifier]
        piece_icons.validate_piece_icon(icon, expected=(DIRECTORY / 'icon.png').read_bytes())
        icon_pixels = Image.open(io.BytesIO(icon)).tobytes()
        for style, fingerprint in {
            'ddrhw-crossing': 'f324aed1e8375db5164892ed611ff2f8032b575772f5bbade5b3e4dbb7104f64',
            'ddrhw-ramp': '07711d39e5cc6c7252d1b949151cd81b9e830d444d7b0d74111d09b6bc963581',
        }.items():
            legacy_pixels = Image.open(io.BytesIO(menu.make_icon(style))).tobytes()
            self.assertEqual(sha(legacy_pixels), fingerprint)
            self.assertNotEqual(icon_pixels, legacy_pixels)

    def test_installer_finite_recipe_selection_includes_the_crossing_and_actual_dependencies(self):
        self.assertIn(self.piece['recipe'], service.implemented_recipes_by_domain()['highway'])
        self.assertIn(IDENTIFIER, service.all_implemented_ids(ROOT))
        self.assertEqual(set(self.piece['dependencies']),
                         {'controller', 'dd_rhw', 'rhw_core', 'hsr'})
        self.assertTrue(set(self.piece['dependencies']) <= self.catalog['_profile']['files'].keys())
        self.assertEqual(self.catalog['piece_sets']['ddrhw-diagonal-ghsr-crossing'], [IDENTIFIER])

    def test_recipe_dispatch_runs_native_continuation_then_compiles_the_exact_core_and_helpers(self):
        compiled = [((0, 0), b'first model', b'first paths'),
                    ((0, 1), b'second model', b'second paths')]
        context = {'controller': {'fixture': b'native controller'}}
        assets = {(1, 2, 3): b'finished source'}
        with patch('scp_highway.ghsr_crossing.build_channels', return_value=compiled) as build, \
             patch('scp_highway.ghsr_approaches.check_native_continuation') as continuation, \
             patch('scp_highway.recipes.finish_piece', return_value=assets) as finish, \
             patch('scp_highway.model_shadows.add_shadows', return_value=assets) as shadows:
            saved, construction = recipes.build_piece(self.piece, context)
        build.assert_called_once_with(context)
        continuation.assert_called_once_with(context['controller'])
        finish.assert_called_once_with(self.piece, context, compiled)
        shadows.assert_called_once_with(self.piece, context, compiled, assets)
        self.assertIs(saved, assets)
        rings, rules = parse_rules(construction)
        self.assertEqual(len(rings[0]), 8)
        fields = {}
        for name, value in rules[number(self.piece['puzzle_id'])]:
            fields.setdefault(name, []).append(value)
        report = check_emitted_runtime_addresses(fields, self.piece)
        self.assertEqual((report['cells_checked'], report['wrong_model_selections']), (2, 0))
        self.assertEqual(sum(' optional' in row for row in fields['CheckType']), 4)
        self.assertNotIn('Transpose', construction)


class GHSRCrossingPrivateNativeIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings_path = local_settings(ROOT)
        if not settings_path.is_file():
            raise unittest.SkipTest('Private NAM settings are unavailable')
        settings = jsonc.load(settings_path)
        roots = list(dict.fromkeys(Path(value).expanduser().resolve()
                                  for value in [settings['plugins'], *settings.get('extra_plugins', [])]))
        if not any(path.is_dir() for path in roots):
            raise unittest.SkipTest('Audited native NAM DD/GHSR input folders are unavailable')
        catalog = load_catalog(ROOT)
        cls.piece = next(piece for piece in catalog['pieces'] if piece['id'] == IDENTIFIER)
        cls.context = {}
        for label in cls.piece['dependencies']:
            record = catalog['_profile']['files'][label]
            found = sorted({path.resolve() for folder in roots if folder.is_dir()
                            for path in folder.rglob(record['filename'])})
            if not found:
                raise unittest.SkipTest('Audited native DD/GHSR dependency is unavailable: ' + record['filename'])
            if len(found) != 1:
                raise ValueError('Ambiguous native DD/GHSR dependency: ' + record['filename'])
            raw = found[0].read_bytes()
            if sha(raw) != record['sha256']:
                raise ValueError('Native DD/GHSR input changed; re-audit rather than skip: ' + record['filename'])
            cls.context[label] = {key: decompress(value) for key, value in entries(raw).items()}

    def test_actual_native_recipe_saves_verified_routes_shadows_helpers_and_continuation(self):
        controller_before = dict(self.context['controller'])
        assets, construction = recipes.build_piece(self.piece, self.context)
        saved = {key: decompress(value) for key, value in entries(pack_dbpf(assets)).items()}
        paths = verify.check_paths(saved, self.piece)
        models = verify.check_models(saved, self.piece, None)
        self.assertEqual(paths['complete_directed_journeys'], 6)
        self.assertEqual(paths['complete_native_boundary_members_checked'], 12)
        self.assertTrue(paths['use_path_elevation'])
        self.assertTrue(paths['native_helper_boundary_tangents_verified'])
        self.assertFalse(paths['game_operation_tested'])
        self.assertTrue(models)
        _rings, rules = parse_rules(construction)
        fields = {}
        for name, value in rules[number(self.piece['puzzle_id'])]:
            fields.setdefault(name, []).append(value)
        verify.check_construction_fields(fields, self.piece, saved)
        self.assertEqual(check_emitted_runtime_addresses(fields, self.piece)['wrong_model_selections'], 0)
        donors = {key: raw for resources in self.context.values() for key, raw in resources.items()}
        rul1, record = native_approaches.compose_rul1(donors[native_approaches.RUL1], [self.piece], donors)
        report = native_approaches.verify_rul1({native_approaches.RUL1: rul1}, [self.piece],
                                               {native_approaches.OVERLAY: record}, donors)
        self.assertEqual(report['native_rul1_solutions_checked'], 12)
        self.assertFalse(native_approaches.dependency_keys([self.piece]) & saved.keys())
        self.assertEqual(self.context['controller'], controller_before)
        continuation = ghsr_approaches.check_native_continuation(self.context['controller'])
        self.assertEqual(continuation['native_continuation_rows_checked'], 6)
        self.assertTrue(continuation['native_rul2_unchanged'])


if __name__ == '__main__':
    unittest.main()
