"""Exercise portable entry points in an isolated copy, never the live project."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

SOURCE = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())


class PortableCLITests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve() / 'framework'
        shutil.copytree(SOURCE, self.root, ignore=shutil.ignore_patterns(
            'dist', 'local', 'backups', '__pycache__', '.pytest_cache', '*.egg-info', '.venv'))

    def tearDown(self):
        self.temp.cleanup()

    def call(self, *args):
        return subprocess.run([sys.executable, '-B', str(self.root / 'scp.py'), *args],
                              cwd=self.root.parent, capture_output=True, text=True)

    def test_self_contained_list_needs_no_previous_prototype_directory(self):
        result = self.call('list')
        self.assertEqual(result.returncode, 0, result.stderr)
        project = json.loads((self.root / 'project.json').read_text())
        registered = [path for domain in project['domains'].values()
                      for path in json.loads((self.root / domain['registry']).read_text())['pieces']]
        self.assertEqual(len(json.loads(result.stdout)['pieces']), len(registered))

    def test_invalid_display_names_do_not_reserve_ids_or_break_the_registry(self):
        files = [self.root/'config/allocations.json',
                 self.root/'domains/high-speed-rail/domain.json']
        before = {str(path): path.read_bytes() for path in files}
        for identifier, name in [('duplicate-display-name', 'HSR over Diagonal GHSR'),
                                 ('blank-display-name', '   ')]:
            result = self.call('scaffold', '--id', identifier, '--name', name)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((self.root/'domains/high-speed-rail/00_pieces'/identifier/'piece.json').exists())
            self.assertEqual(before, {str(path): path.read_bytes() for path in files})
            self.assertEqual(self.call('list').returncode, 0)

    def test_new_piece_symlink_escape_is_rejected_before_reserving_ids(self):
        outside = self.root.parent/'outside'
        outside.mkdir()
        piece_dir = self.root/'domains/high-speed-rail/00_pieces/symlink-draft'
        piece_dir.symlink_to(outside, target_is_directory=True)
        paths = [self.root/'config/allocations.json', self.root/'domains/high-speed-rail/domain.json']
        before = {str(path): path.read_bytes() for path in paths}
        result = self.call('scaffold', '--id', 'symlink-draft', '--name', 'Symlink Draft')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(outside.iterdir()), [])
        self.assertEqual(before, {str(path): path.read_bytes() for path in paths})
        self.assertEqual(self.call('list').returncode, 0)

    def test_scaffold_grid_and_reservations_do_not_collide(self):
        result = self.call('scaffold', '--id', 'future-crossing', '--name', 'Future Crossing', '--width', '2', '--depth', '2')
        self.assertEqual(result.returncode, 0, result.stderr)
        piece = json.loads((self.root / 'domains/high-speed-rail/00_pieces/future-crossing/piece.json').read_text())
        ids = [int(x, 16) for x in piece['tile_ids']]
        self.assertEqual(ids, [ids[0], ids[0] + 0x100, ids[0] + 0x10, ids[0] + 0x110])
        self.assertFalse(piece['enabled_by_default'])
        self.assertEqual(piece['status'], 'draft')
        self.assertNotEqual(self.call('scaffold', '--id', 'future-crossing', '--name', 'Again').returncode, 0)

    def test_scaffold_routes_a_draft_into_the_selected_domain(self):
        result = self.call('scaffold', '--domain', 'highway', '--id', 'highway-draft', '--name', 'Highway Draft')
        self.assertEqual(result.returncode, 0, result.stderr)
        piece = json.loads((self.root / 'domains/highway/00_pieces/highway-draft/piece.json').read_text())
        self.assertEqual(piece['domain'], 'highway')
        self.assertFalse(piece['enabled_by_default'])

    def test_unknown_domain_does_not_reserve_identifiers(self):
        ledger = (self.root / 'config/allocations.json').read_bytes()
        result = self.call('scaffold', '--domain', 'unknown', '--id', 'bad-domain', '--name', 'Bad Domain')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.root / 'config/allocations.json').read_bytes(), ledger)

    def test_invalid_scaffold_leaves_all_registry_bytes_unchanged(self):
        before = {p.name: p.read_bytes() for p in (self.root / 'project.json', self.root / 'config/allocations.json')}
        result = self.call('scaffold', '--id', '../escape', '--name', 'Bad', '--width', '0')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(before, {p.name: p.read_bytes() for p in (self.root / 'project.json', self.root / 'config/allocations.json')})

    def test_scaffold_does_not_inherit_sparse_cells_from_the_first_piece(self):
        path = self.root / 'domains/high-speed-rail/domain.json'
        registry = json.loads(path.read_text())
        first = '00_pieces/rail-hsr-diagonal-s-left/piece.json'
        registry['pieces'].remove(first)
        registry['pieces'].insert(0, first)
        path.write_text(json.dumps(registry))
        result = self.call('scaffold', '--id', 'new-small-piece', '--name', 'New Small Piece')
        self.assertEqual(result.returncode, 0, result.stderr)
        piece = json.loads((self.root / 'domains/high-speed-rail/00_pieces/new-small-piece/piece.json').read_text())
        self.assertEqual(piece['footprint'], [1, 1])
        self.assertNotIn('cells', piece)
        self.assertNotIn('category', piece)

    def test_source_zip_has_no_installed_assets_settings_or_personal_paths(self):
        private = self.root / 'local'
        (private / 'fixtures').mkdir(parents=True)
        sentinel = (str(self.root) + ':private-resource').encode()
        (private / 'settings.json').write_text(json.dumps({'secret': sentinel.decode()}))
        (private / 'fixtures' / 'resource.DAT').write_bytes(sentinel)
        target = self.root.parent / 'source.zip'
        result = self.call('source-package', '--destination', str(target))
        self.assertEqual(result.returncode, 0, result.stderr)
        with zipfile.ZipFile(target) as archive:
            self.assertIsNone(archive.testzip())
            for identifier in ('hsr-component-modular-crossing-core', 'hsr-component-tight-paired-curve90-l4-to-mid'):
                relative = Path('domains/high-speed-rail/00_pieces') / identifier / 'connector-groups.jsonc'
                matches = [name for name in archive.namelist() if name.endswith('/' + relative.as_posix())]
                self.assertEqual(len(matches), 1, f'Commented connector source missing from export: {relative}')
                self.assertEqual(archive.read(matches[0]), (self.root / relative).read_bytes())
            for name in archive.namelist():
                self.assertNotIn('/dist/', name)
                self.assertNotIn('/local/', name)
                self.assertNotIn('.egg-info/', name)
                self.assertFalse(name.lower().endswith(('.dat', '.sc4model')))
                self.assertNotIn(sentinel, archive.read(name))
                if name.endswith('.md'):
                    self.assertNotIn(str(Path.home()).encode(), archive.read(name))

    def test_source_zip_is_deterministic(self):
        a, b = self.root.parent / 'a.zip', self.root.parent / 'b.zip'
        self.assertEqual(self.call('source-package', '--destination', str(a)).returncode, 0)
        self.assertEqual(self.call('source-package', '--destination', str(b)).returncode, 0)
        self.assertEqual(a.read_bytes(), b.read_bytes())

    def test_release_check_does_not_treat_static_status_as_game_evidence(self):
        result = self.call('release-check', '--all')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(json.loads(result.stdout)['public_release_ready'])

    def test_failed_piece_can_be_inspected_but_not_selected_for_build(self):
        slug = 'tram-under-hsr'
        path = self.root / 'domains/high-speed-rail/00_pieces' / slug / 'piece.json'
        piece = json.loads(path.read_text())
        piece['game_tests']['placement'] = 'failed'
        path.write_text(json.dumps(piece))
        report = self.call('release-check', '--include', slug)
        self.assertEqual(report.returncode, 0, report.stderr)
        self.assertFalse(json.loads(report.stdout)['public_release_ready'])
        self.assertIn(slug+': in-game test matrix', json.loads(report.stdout)['blocked'])
        # Selection must reject this piece before reading any NAM donor assets.
        plugins = self.root.parent / 'Plugins'
        plugins.mkdir()
        built = self.call('build', '--plugins', str(plugins), '--include', slug)
        self.assertNotEqual(built.returncode, 0)
        self.assertIn('failed placement tests', built.stderr)

    def test_named_piece_sets_combine_without_duplicate_pieces(self):
        result = self.call('release-check', '--set', 'smooth-t-junctions', '--set', 'diagonal-s-curves')
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertFalse(report['public_release_ready'])
        matrices = [value for value in report['blocked'] if value.endswith(': in-game test matrix')]
        self.assertEqual(len(matrices), 6)

    def test_unknown_piece_set_cannot_silently_build_the_default_set(self):
        result = self.call('release-check', '--set', 'misspelled-set')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Unknown piece set', result.stderr)


if __name__ == '__main__':
    unittest.main()
