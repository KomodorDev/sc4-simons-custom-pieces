"""Release evidence is checked in temporary project fixtures, never Plugins."""
from copy import deepcopy
import json
from pathlib import Path, PureWindowsPath
import sys
import tempfile
import unittest
from unittest.mock import patch

FRAMEWORK = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(FRAMEWORK / 'framework'))

from scp import jsonc
from scp.release import _portable_error, assess_build


class ReleaseEvidenceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='scp-release-test-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        gates = jsonc.loads((FRAMEWORK / 'config/release.jsonc').read_text())
        for record in gates.values():
            if isinstance(record, dict) and 'status' in record:
                record['status'], record['evidence'] = 'passed', 'fixture-human-record'
        self._write_json('config/release.jsonc', gates)
        cases = dict.fromkeys(('placement', 'traffic_both_directions', 'no_unwanted_transfers',
                               'rotations_and_mirrors', 'shadows', 'demolition', 'save_reload'), 'passed')
        self.manifest = {
            'pieces': [{'id': 'example-crossing', 'status': 'tested', 'game_tests': cases,
                        'asset_file': 'zzz_Simons_Custom_Pieces/20_Pieces/SCP_example-crossing.dat',
                        'game_evidence': 'evidence/example-crossing.json',
                        'provenance': {'redistribution': 'permission-recorded'}}],
            'files': [{'path': 'zzz_Simons_Custom_Pieces/20_Pieces/SCP_example-crossing.dat',
                       'sha256': 'a' * 64},
                      {'path': 'zzz_Simons_Custom_Pieces/00_SCP_Controller_NAM50.dat',
                       'sha256': 'e' * 64},
                      {'path': 'zzz_Simons_Custom_Pieces/10_SCP_Menu.dat', 'sha256': 'f' * 64}],
            'profile': {'donors': [{'filename': 'NetworkAddonMod_Controller.dat', 'sha256': 'b' * 64},
                                   {'filename': 'High Speed Rail.dat', 'sha256': 'c' * 64}]},
        }
        self.evidence = {
            'piece_id': 'example-crossing', 'asset_sha256': 'a' * 64,
            'package_fingerprints': {record['path']: record['sha256']
                                      for record in self.manifest['files']},
            'donor_fingerprints': {'NetworkAddonMod_Controller.dat': 'b' * 64,
                                   'High Speed Rail.dat': 'c' * 64},
            'case_results': deepcopy(cases), 'tester': 'Fixture Tester',
            'date': '2026-10-18', 'screenshots': ['evidence/screenshots/crossing.png'],
        }
        screenshot = self.root / 'evidence/screenshots/crossing.png'
        screenshot.parent.mkdir(parents=True)
        screenshot.write_bytes(b'fixture screenshot; existence is the checked property')
        self._write_evidence()

    def _write_json(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + '\n')

    def _write_evidence(self):
        self._write_json('evidence/example-crossing.json', self.evidence)

    def _assert_blocked(self, manifest=None):
        result = assess_build(self.root, self.manifest if manifest is None else manifest)
        self.assertFalse(result['public_release_ready'])
        self.assertTrue(result['blocked'])
        return result

    def test_matching_evidence_and_human_gates_pass(self):
        self.assertEqual(assess_build(self.root, self.manifest),
                         {'public_release_ready': True, 'blocked': []})

    def test_layout_objection_blocks_release_even_when_all_file_and_game_evidence_pass(self):
        self.manifest['pieces'][0]['design_review']={
            'status':'needs-redesign','summary':'A route takes an unnecessary rectangular detour.',
            'reasons':['The track layout has not been accepted.']}
        result=self._assert_blocked()
        self.assertTrue(any('NEEDS REDESIGN' in reason for reason in result['blocked']))

    def test_older_manifest_cannot_hide_a_current_layout_objection(self):
        current=deepcopy(self.manifest['pieces'][0])
        current['design_review']={'status':'needs-redesign','summary':'Current review rejected this layout.',
                                  'reasons':['The historical build did not include the new flag.']}
        self._write_json('project.jsonc',{'fixture':'catalog access is mocked below'})
        with patch('scp.catalog.load_catalog',return_value={'pieces':[current]}):
            result=self._assert_blocked()
        self.assertTrue(any('NEEDS REDESIGN' in reason for reason in result['blocked']))

    def test_missing_reference_or_file_is_blocked(self):
        manifest = deepcopy(self.manifest)
        del manifest['pieces'][0]['game_evidence']
        self._assert_blocked(manifest)
        (self.root / 'evidence/example-crossing.json').unlink()
        self._assert_blocked()

    def test_missing_manual_coverage_keeps_relative_filename_without_private_root(self):
        source = {**deepcopy(self.manifest['pieces'][0]), 'domain': 'fixture-network'}
        catalog = {'pieces': [source], 'domains': {'fixture-network': {'path': 'domains/fixture-network'}}}
        self._write_json('project.jsonc', {'fixture': 'catalog access is mocked below'})
        with patch('scp.catalog.load_catalog', return_value=catalog):
            result = self._assert_blocked()
        reason = next(reason for reason in result['blocked'] if 'authoritative manual coverage' in reason)
        self.assertNotIn(str(self.root.resolve()), reason)
        self.assertNotIn(repr(str(self.root.resolve()))[1:-1], reason)
        self.assertIn('manual-tests.json', reason)
        self.assertIn('fixture-network', reason)
        self.assertIn('[Errno 2]', reason)

    def test_game_evidence_read_error_keeps_failure_without_private_root(self):
        path = self.root.resolve()/'evidence/example-crossing.json'
        error = PermissionError(13, 'Permission denied', str(path))
        with patch('scp.release._project_file', side_effect=error):
            result = self._assert_blocked()
        reason = next(reason for reason in result['blocked'] if 'game evidence invalid' in reason)
        self.assertNotIn(str(self.root.resolve()), reason)
        self.assertNotIn(repr(str(self.root.resolve()))[1:-1], reason)
        self.assertIn('example-crossing.json', reason)
        self.assertIn('Permission denied', reason)
        self.assertIn('[Errno 13]', reason)

    def test_portable_error_removes_raw_and_repr_escaped_windows_roots(self):
        root = PureWindowsPath('C:/') / 'temporary-fixtures' / self.root.name / 'custom-pieces'
        missing = root/'evidence/missing.json'
        for message in (f'Cannot read {missing}', str(FileNotFoundError(2, 'Missing evidence', str(missing)))):
            with self.subTest(message=message):
                portable = _portable_error(root, ValueError(message))
                self.assertNotIn(str(root), portable)
                self.assertNotIn(repr(str(root))[1:-1], portable)
                self.assertIn('missing.json', portable)
                self.assertIn('.', portable)

    def test_changed_asset_controller_or_menu_cannot_reuse_the_old_evidence(self):
        for index in range(3):
            with self.subTest(changed_file=self.manifest['files'][index]['path']):
                manifest = deepcopy(self.manifest)
                manifest['files'][index]['sha256'] = 'd' * 64
                self._assert_blocked(manifest)

    def test_donor_fingerprint_set_and_values_must_match_exactly(self):
        for donors in ({'High Speed Rail.dat': 'c' * 64},
                       {**self.evidence['donor_fingerprints'], 'Extra.dat': 'd' * 64},
                       {**self.evidence['donor_fingerprints'], 'High Speed Rail.dat': 'd' * 64}):
            with self.subTest(donors=donors):
                self.evidence['donor_fingerprints'] = donors
                self._write_evidence()
                self._assert_blocked()

    def test_case_results_must_be_complete_exact_and_passing(self):
        baseline = deepcopy(self.evidence['case_results'])
        incomplete = deepcopy(baseline)
        incomplete.pop('demolition')
        for cases in (incomplete, {**baseline, 'demolition': 'failed'},
                      {**baseline, 'unrelated_case': 'passed'}):
            with self.subTest(cases=cases):
                self.evidence['case_results'] = cases
                self._write_evidence()
                self._assert_blocked()

    def test_screenshots_must_be_nonempty_and_exist(self):
        for screenshots in ([], ['evidence/screenshots/missing.png']):
            with self.subTest(screenshots=screenshots):
                self.evidence['screenshots'] = screenshots
                self._write_evidence()
                self._assert_blocked()

    def test_relative_paths_cannot_escape_or_use_symlinks(self):
        original = deepcopy(self.evidence)
        for reference in ('../outside.json', '/tmp/outside.json', 'evidence\\outside.json'):
            with self.subTest(reference=reference):
                manifest = deepcopy(self.manifest)
                manifest['pieces'][0]['game_evidence'] = reference
                self._assert_blocked(manifest)
        for screenshot in ('../outside.png', '/tmp/outside.png', 'evidence\\outside.png'):
            with self.subTest(screenshot=screenshot):
                self.evidence['screenshots'] = [screenshot]
                self._write_evidence()
                self._assert_blocked()
        with tempfile.TemporaryDirectory(prefix='scp-outside-evidence-') as directory:
            external = Path(directory) / 'evidence.json'
            external.write_text(json.dumps(original))
            link = self.root / 'evidence/linked.json'
            link.symlink_to(external)
            manifest = deepcopy(self.manifest)
            manifest['pieces'][0]['game_evidence'] = 'evidence/linked.json'
            self._assert_blocked(manifest)
            screenshot = Path(directory) / 'screenshot.png'
            screenshot.write_bytes(b'external fixture screenshot')
            (self.root / 'evidence/screenshots/linked.png').symlink_to(screenshot)
            self.evidence = {**original, 'screenshots': ['evidence/screenshots/linked.png']}
            self._write_evidence()
            self._assert_blocked()

    def test_wrong_piece_tester_and_invalid_calendar_dates_are_blocked(self):
        original = deepcopy(self.evidence)
        for field, value in (('piece_id', 'another-piece'), ('tester', '  '),
                             ('date', '2026-2-1'), ('date', '2026-02-30')):
            with self.subTest(field=field, value=value):
                self.evidence = {**deepcopy(original), field: value}
                self._write_evidence()
                self._assert_blocked()

    def test_game_evidence_does_not_override_pending_human_permission_gates(self):
        path = self.root / 'config/release.jsonc'
        gates = jsonc.loads(path.read_text())
        gates['nam_derivatives_permission']['status'] = 'pending'
        path.write_text(json.dumps(gates))
        self._assert_blocked()

    def test_malformed_json_and_ambiguous_build_records_fail_closed(self):
        (self.root / 'evidence/example-crossing.json').write_text('{not JSON')
        self._assert_blocked()
        self._write_evidence()
        manifest = deepcopy(self.manifest)
        manifest['files'].append(deepcopy(manifest['files'][0]))
        self._assert_blocked(manifest)
        manifest = deepcopy(self.manifest)
        manifest['profile']['donors'].append(deepcopy(manifest['profile']['donors'][0]))
        self._assert_blocked(manifest)


if __name__ == '__main__':
    unittest.main()
