"""An assembly's explicit matrix opt-in separates two human journey observations."""
from copy import deepcopy
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents
                          if (p/'project.jsonc').is_file())/'framework'))
from scp.content import (case_state, compact_manual_record, fingerprint,
                         new_manual_record, record_observation_file,
                         record_software_result, record_user_result,
                         refresh_manual_record, summarize_manual_record,
                         validate_manual_record, write_subject_content)
from scp.inventory import _coverage


class AssemblyObservationSplitTests(unittest.TestCase):
    def setUp(self):
        self.subject = {'id': 'fixture-assembly', 'kind': 'assembly'}
        self.hashes = {'path:fixture:route': fingerprint(b'actual route'),
                       'model:fixture:model': fingerprint(b'actual model'),
                       'construction:fixture': fingerprint(b'actual construction')}
        self.connections = {
            'subject_id': self.subject['id'],
            'ports': [{'id': 'W.in', 'direction': 'in', 'service_network': 'hsr',
                       'variant': 'hsr', 'role': 'primary'},
                      {'id': 'E.out', 'direction': 'out', 'service_network': 'hsr',
                       'variant': 'hsr', 'role': 'primary'}],
            'journeys': [{'id': 'W.in>E.out', 'service_network': 'hsr', 'role': 'primary',
                          'entry_port': 'W.in', 'exit_port': 'E.out'}],
            'forbidden_transfers': [], 'software_status': {'path_extraction': 'passed'},
            'source': {'resource_fingerprints': self.hashes},
        }
        self.environment = {'platform': 'fixture platform', 'game_version': 'fixture version',
                            'nam_profile': 'fixture NAM profile'}

    def record(self, split=False, orientations=None):
        return new_manual_record(self.subject['id'], 'assembly', self.connections, self.hashes,
                                 split_journey_observations=split, manual_check_orientations=orientations)

    def case(self, record, kind, rotation=0):
        return next(case for case in record['cases'] if case['kind'] == kind
                    and case['scope'].get('rotation_ccw_degrees') == rotation)

    def observe(self, record, case, **overrides):
        request = {'explicit_user_confirmation': True, 'reviewer': 'Fixture human',
                   'confirmed_at': '2026-10-27', 'environment': self.environment,
                   'evidence': ['The human confirmed this exact fixture observation.']}
        request.update(overrides)
        return record_user_result(record, case['id'], 'passed', **request)

    def test_split_is_explicit_and_preserves_exact_direction_service_role_and_rotations(self):
        default, split = self.record(), self.record(True)
        generic = [case for case in default['cases'] if case['kind'] == 'in_game_journey']
        self.assertEqual(len(generic), 4)
        self.assertFalse(any(case['kind'] in ('in_game_route_query', 'in_game_visible_travel')
                             for case in default['cases']))
        self.assertFalse(any(case['kind'] == 'in_game_journey' for case in split['cases']))
        for kind in ('in_game_route_query', 'in_game_visible_travel'):
            cases = [case for case in split['cases'] if case['kind'] == kind]
            self.assertEqual([case['scope'] for case in cases], [case['scope'] for case in generic])
            self.assertTrue(all(case_state(case) == 'unverified' for case in cases))
        self.assertEqual(len({case['id'] for case in split['cases']}), len(split['cases']))
        self.assertEqual(self.record(True), split)
        with self.assertRaisesRegex(ValueError, 'boolean'):
            new_manual_record('fixture', 'assembly', {}, {}, split_journey_observations=1)
        # Pieces use the same explicit opt-in while preserving legacy defaults.
        piece = new_manual_record(self.subject['id'], 'piece', self.connections, self.hashes,
                                  split_journey_observations=True)
        self.assertEqual([case['scope'] for case in piece['cases']],
                         [case['scope'] for case in split['cases']])
        self.assertTrue(all(case_state(case) == 'unverified' for case in piece['cases']))

    def test_query_does_not_approve_visible_travel_other_rotations_or_environments(self):
        record = self.record(True)
        query = self.case(record, 'in_game_route_query')
        observed = self.observe(record, query)
        self.assertEqual(case_state(self.case(observed, 'in_game_route_query')), 'passed')
        self.assertEqual(case_state(self.case(observed, 'in_game_visible_travel')), 'unverified')
        self.assertEqual(case_state(self.case(observed, 'in_game_route_query', 90)), 'unverified')
        summary = summarize_manual_record(observed, environment={'platform': 'another platform'})
        self.assertEqual(summary['journey_coverage']['passed'], 0)
        for overrides in ({'explicit_user_confirmation': False}, {'environment': {}}, {'evidence': []}):
            with self.subTest(overrides=overrides), self.assertRaises(ValueError):
                self.observe(record, query, **overrides)
        with self.assertRaisesRegex(ValueError, 'cannot mark a manual check'):
            record_software_result(record, query['id'], 'passed', verifier='Fixture software',
                                   checked_at='2026-10-27', evidence=['Software checked a file.'])
        travel = self.case(observed, 'in_game_visible_travel')
        observed = self.observe(observed, travel)
        summary = summarize_manual_record(observed)
        self.assertEqual(summary['journey_coverage']['passed'], 2)
        self.assertEqual(summary['journey_coverage']['unverified'], 6)
        self.assertEqual(sum(summary['journey_coverage'].values()), 8)
        self.assertNotIn('in_game_journey', summary['by_kind'])
        self.assertEqual(sum(sum(counts.values()) for counts in summary['by_kind'].values()),
                         summary['total'])

    def test_legacy_observations_remain_historical_without_approving_either_new_kind(self):
        previous = self.record()
        previous = self.observe(previous, self.case(previous, 'in_game_journey'))
        observed_case = deepcopy(self.case(previous, 'in_game_journey'))
        snapshot = deepcopy(previous)
        migrated = refresh_manual_record(compact_manual_record(previous), self.record(True))
        self.assertEqual(previous, snapshot)
        self.assertEqual(migrated['removed_cases'], [observed_case])
        self.assertEqual(summarize_manual_record(migrated)['journey_coverage']['passed'], 0)
        self.assertEqual(summarize_manual_record(migrated)['journey_coverage']['unverified'], 8)
        self.assertEqual(refresh_manual_record(migrated, self.record(True)), migrated)
        for case in migrated['cases']:
            if case['kind'] in ('in_game_route_query', 'in_game_visible_travel'):
                self.assertFalse(case['observations'])

    def test_changed_route_stales_each_independent_observation_without_rewriting_history(self):
        previous = self.record(True)
        for kind in ('in_game_route_query', 'in_game_visible_travel'):
            previous = self.observe(previous, self.case(previous, kind))
        self.hashes['path:fixture:route'] = fingerprint(b'changed actual route')
        refreshed = refresh_manual_record(previous, self.record(True))
        for kind in ('in_game_route_query', 'in_game_visible_travel'):
            self.assertEqual(case_state(self.case(refreshed, kind)), 'stale')
            self.assertEqual(self.case(refreshed, kind)['observations'],
                             self.case(previous, kind)['observations'])

    def test_manual_orientation_subset_keeps_supported_and_software_scopes_unchanged(self):
        self.connections['ports'].append({'id': 'W.out', 'direction': 'out', 'service_network': 'hsr',
                                          'variant': 'hsr', 'role': 'primary'})
        self.connections['forbidden_transfers'] = [{'from_port': 'W.in', 'to_port': 'W.out',
                                                   'from_service': 'hsr', 'to_service': 'hsr'}]
        original = self.record(True)
        selected = self.record(True, [{'rotation_ccw_degrees': 0}])
        self.assertEqual(selected['supported_orientations'], original['supported_orientations'])
        self.assertEqual(selected['manual_check_orientations'], [{'rotation_ccw_degrees': 0}])
        self.assertNotIn('manual_check_orientations', original)
        self.assertEqual([case for case in selected['cases'] if not case['kind'].startswith('in_game_')],
                         [case for case in original['cases'] if not case['kind'].startswith('in_game_')])
        self.assertEqual({case['scope']['rotation_ccw_degrees'] for case in selected['cases']
                          if case['kind'].startswith('in_game_')}, {0})
        self.assertEqual(sum(case['kind'] == 'in_game_forbidden_transfer' for case in selected['cases']), 1)
        self.assertEqual(summarize_manual_record(selected)['journey_coverage']['unverified'], 2)
        self.assertEqual(compact_manual_record(selected)['manual_check_orientations'],
                         selected['manual_check_orientations'])
        self.assertIn('Human game checks are required only at 0° CCW', selected['rotation_policy'])
        self.assertNotIn('Four proper rotations are covered', selected['rotation_policy'])

    def test_removed_manual_orientations_keep_observed_history_without_copying_results(self):
        previous = self.record(True)
        previous = self.observe(previous, self.case(previous, 'in_game_route_query', 90))
        previous = self.observe(previous, self.case(previous, 'in_game_render', 270))
        previous = self.observe(previous, self.case(previous, 'in_game_visible_travel', 0))
        historical = [deepcopy(case) for case in previous['cases'] if case['observations']
                      and case['scope']['rotation_ccw_degrees'] != 0]
        selected = refresh_manual_record(previous, self.record(True, [{'rotation_ccw_degrees': 0}]))
        self.assertEqual(selected['removed_cases'], historical)
        self.assertEqual(case_state(self.case(selected, 'in_game_route_query')), 'unverified')
        self.assertEqual(case_state(self.case(selected, 'in_game_visible_travel')), 'passed')
        self.assertEqual(refresh_manual_record(selected, self.record(True, [{'rotation_ccw_degrees': 0}])), selected)

    def test_manual_orientation_selection_rejects_unsupported_duplicate_and_invalid_scopes(self):
        for states in ([], {}, [{'rotation_ccw_degrees': True}], [{'rotation_ccw_degrees': 45}],
                       [{'rotation_ccw_degrees': 0, 'construction_transposed': True}],
                       [{'rotation_ccw_degrees': 0}, {'rotation_ccw_degrees': 0, 'construction_transposed': False}],
                       [{'rotation_ccw_degrees': 0, 'extra': 'unreviewed'}]):
            with self.subTest(states=states), self.assertRaises(ValueError):
                self.record(True, states)
        record = self.record(True, [{'rotation_ccw_degrees': 0}])
        record['manual_check_orientations'] = [{'rotation_ccw_degrees': 90}]
        with self.assertRaisesRegex(ValueError, 'outside the selected manual'):
            validate_manual_record(record)

    def test_opt_in_refresh_and_observation_file_keep_matrix_ownership_and_metadata(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            readme, testing = directory/'README.md', directory/'TESTING.md'
            authored_readme = '# Fixture assembly\n\nKeep this authored player paragraph.\n'
            authored_testing = '# Fixture testing\n\nKeep this authored evidence paragraph.\n'
            readme.write_text(authored_readme)
            testing.write_text(authored_testing)
            write_subject_content(directory, self.subject, self.connections, self.hashes)
            self.assertIn('<!-- BEGIN MANUAL SUMMARY -->', readme.read_text())
            self.assertIn('<!-- BEGIN CONNECTIONS -->', readme.read_text())
            with readme.open('a') as stream:
                stream.write('\n<!-- BEGIN ASSEMBLY CONNECTION MATRIX -->\n\nPending matrix.\n\n<!-- END ASSEMBLY CONNECTION MATRIX -->\n')
            write_subject_content(directory, self.subject, self.connections, self.hashes)
            record_path = directory/'checks/manual-tests.json'
            connection_path = directory/'connections.json'
            record = json.loads(record_path.read_text())
            self.assertEqual(summarize_manual_record(record)['journey_coverage']['unverified'], 2)
            self.assertEqual(record['manual_check_orientations'], [{'rotation_ccw_degrees': 0}])
            self.assertEqual(len(record['supported_orientations']), 4)
            self.assertIn('## 4. Connection matrix', readme.read_text())
            self.assertNotIn('<!-- BEGIN MANUAL SUMMARY -->', readme.read_text())
            self.assertNotIn('<!-- BEGIN CONNECTIONS -->', readme.read_text())
            self.assertIn('<!-- BEGIN CONNECTIONS -->', testing.read_text())
            self.assertIn('<!-- BEGIN MANUAL CHECKS -->', testing.read_text())
            self.assertIn('Human game checks use only 0° CCW', testing.read_text())
            self.assertNotIn('Each state has its own declared manual scope', testing.read_text())
            self.assertTrue(readme.read_text().startswith(authored_readme))
            self.assertTrue(testing.read_text().startswith(authored_testing))
            # Non-default JSON formatting makes an unintended metadata rewrite observable.
            record_path.write_text(json.dumps(record, separators=(',', ':')))
            connection_path.write_text(json.dumps(self.connections, separators=(',', ':')))
            metadata = {path: path.read_bytes() for path in (record_path, connection_path)}
            write_subject_content(directory, self.subject, self.connections, {}, refresh_metadata=False)
            self.assertEqual(metadata, {path: path.read_bytes() for path in metadata})
            before_matrix = readme.read_text()
            query = self.case(record, 'in_game_route_query')
            request = {'case_id': query['id'], 'result': 'passed', 'explicit_user_confirmation': True,
                       'reviewer': 'Fixture human', 'confirmed_at': '2026-10-27',
                       'environment': self.environment, 'evidence': ['Observed exact Route Query.']}
            observation = directory/'checks/observation.json'
            observation.write_text(json.dumps(request))
            result = record_observation_file(record_path, observation)
            self.assertEqual(result['state'], 'passed')
            self.assertNotEqual(before_matrix, readme.read_text())
            self.assertNotIn('<!-- BEGIN MANUAL SUMMARY -->', readme.read_text())
            self.assertNotIn('<!-- BEGIN CONNECTIONS -->', readme.read_text())
            self.assertEqual(metadata[connection_path], connection_path.read_bytes())
            self.assertIn('Route Query — hsr', testing.read_text())
            self.assertIn('Visible travel — hsr', testing.read_text())
            write_subject_content(directory, self.subject, self.connections, self.hashes)
            refreshed = json.loads(record_path.read_text())
            self.assertEqual(case_state(self.case(refreshed, 'in_game_route_query')), 'passed')
            self.assertEqual(case_state(self.case(refreshed, 'in_game_visible_travel')), 'unverified')
            stable = {path: path.read_bytes() for path in (readme, testing, record_path, connection_path)}
            write_subject_content(directory, self.subject, self.connections, self.hashes)
            self.assertEqual(stable, {path: path.read_bytes() for path in stable})

    def test_matrix_refresh_honors_an_explicit_supported_subset_and_never_invents_zero(self):
        for supported, selected in (([90], 90), ([0, 90, 180, 270], 90)):
            with self.subTest(supported=supported), TemporaryDirectory() as temporary:
                directory = Path(temporary)
                (directory/'README.md').write_text('# Fixture\n\n<!-- BEGIN ASSEMBLY CONNECTION MATRIX -->\n\n<!-- END ASSEMBLY CONNECTION MATRIX -->\n')
                connections = deepcopy(self.connections)
                connections['supported_orientations'] = [
                    {'rotation_ccw_degrees': angle, 'construction_transposed': False} for angle in supported]
                if len(supported) > 1:
                    record = new_manual_record(self.subject['id'], 'assembly', connections, self.hashes,
                        split_journey_observations=True, manual_check_orientations=[{'rotation_ccw_degrees': selected}])
                    checks = directory/'checks'
                    checks.mkdir()
                    (checks/'manual-tests.json').write_text(json.dumps(compact_manual_record(record)))
                write_subject_content(directory, self.subject, connections, self.hashes)
                record = json.loads((directory/'checks/manual-tests.json').read_text())
                self.assertEqual(record['manual_check_orientations'], [{'rotation_ccw_degrees': selected}])
                self.assertEqual(record['supported_orientations'], connections['supported_orientations'])
                self.assertEqual({case['scope']['rotation_ccw_degrees'] for case in record['cases']
                                  if case['kind'].startswith('in_game_')}, {selected})

    def test_inventory_uses_split_coverage_without_changing_legacy_fallback(self):
        split = self.record(True)
        split = self.observe(split, self.case(split, 'in_game_route_query'))
        status = {'record_present': True, 'summary': summarize_manual_record(split)}
        self.assertIn('1/8 passed; 7 unverified', _coverage(status, 'in_game_journey'))
        legacy = {'record_present': True, 'summary': summarize_manual_record(self.record())}
        expected = _coverage(legacy, 'in_game_journey')
        self.assertIn('0/4 passed; 4 unverified', expected)
        self.assertNotIn('journey_coverage', legacy['summary'])
        legacy['summary']['journey_coverage'] = deepcopy(legacy['summary']['by_kind']['in_game_journey'])
        self.assertEqual(_coverage(legacy, 'in_game_journey'), expected)


if __name__ == '__main__':
    unittest.main()
