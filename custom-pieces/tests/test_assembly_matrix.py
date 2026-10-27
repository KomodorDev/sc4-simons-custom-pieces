"""Assembly summaries preserve directional services and exact evidence limits."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'framework'))

from scp.assembly_matrix import ASSEMBLY_CONNECTION_MATRIX, render_assembly_connection_matrix
from scp.content import (compact_manual_record, declare_not_applicable, fingerprint,
                         new_manual_record, record_software_result, record_user_result)


class AssemblyMatrixTests(unittest.TestCase):
    def setUp(self):
        self.connections = {
            'subject_id': 'fixture', 'software_status': {'path_extraction': 'passed'},
            'ports': [self.port('W.in', 'in'), self.port('S.in', 'in'),
                      self.port('E.out', 'out'), self.port('W.out', 'out'), self.port('S.out', 'out')],
            'journeys': [self.journey('west-east', 'W.in', 'E.out'),
                         self.journey('south-west', 'S.in', 'W.out')],
            'forbidden_transfers': [{'from_port': 'W.in', 'to_port': 'W.out',
                                     'from_service': 'hsr', 'to_service': 'hsr'}],
        }
        self.fingerprints = {'path:fixture:one': fingerprint(b'actual fixture PATH'),
                             'model:fixture:one': fingerprint(b'actual fixture model')}
        self.record = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints,
                                        split_journey_observations=True)
        case = next(case for case in self.record['cases'] if case['kind'] == 'software_connectivity')
        self.record = record_software_result(self.record, case['id'], 'passed', verifier='Fixture verifier',
                                            checked_at='2026-10-27T10:00:00Z', evidence=['Actual fixture check.'])

    @staticmethod
    def port(identifier, direction, service='hsr', variant='hsr', role='primary'):
        return {'id': identifier, 'direction': direction, 'service_network': service,
                'variant': variant, 'role': role, 'engine_transport': 7}

    @staticmethod
    def journey(identifier, entry, exit_port, service='hsr', role='primary'):
        return {'id': identifier, 'entry_port': entry, 'exit_port': exit_port,
                'service_network': service, 'role': role}

    def observe(self, kind, *, journey='west-east', angle=0, result='passed', transposed=False):
        case = next(case for case in self.record['cases']
                    if case['kind'] == kind and case['scope'].get('rotation_ccw_degrees') == angle
                    and bool(case['scope'].get('construction_transposed', False)) == transposed
                    and (kind == 'in_game_render' or case['scope'].get('journey_id') == journey))
        self.record = record_user_result(self.record, case['id'], result, explicit_user_confirmation=True,
                                        reviewer='Fixture reviewer', confirmed_at='2026-10-27T10:01:00Z',
                                        evidence=['Explicit fixture observation.'],
                                        environment={'platform': 'fixture OS', 'game_version': 'fixture version',
                                                     'nam_profile': 'fixture profile'})
        return case['id']

    def render(self):
        return render_assembly_connection_matrix(self.connections, self.record)

    def cell(self, entry='W.in', exit_port='E.out'):
        rows = [line.split(' | ') for line in self.render().splitlines() if line.startswith('| ') ]
        column = next(index for index, value in enumerate(rows[0]) if f'`{exit_port}`' in value)
        row = next(row for row in rows[2:] if f'`{entry}`' in row[0])
        return row[column]

    def metric(self, label, **pair):
        cell = self.cell(**pair)
        return cell.split(f'**{label}:** ', 1)[1].split('<br>', 1)[0]

    def test_entry_rows_exit_columns_and_all_four_distinct_metrics(self):
        text = self.render()
        header = next(line for line in text.splitlines() if line.startswith('| Entrance'))
        self.assertIn('`E.out`', header)
        self.assertNotIn('`W.in`', header)
        self.assertFalse(any(line.startswith('| `E.out`') for line in text.splitlines()))
        for label in ('Saved PATH', 'Game appearance†', 'Route Query', 'Visible travel'):
            self.assertIn(f'**{label}:**', self.cell())
        self.assertEqual(ASSEMBLY_CONNECTION_MATRIX, 'ASSEMBLY CONNECTION MATRIX')
        self.assertIn('**HSR · West entrance**', text)
        self.assertIn('**HSR · East exit**', header)

    def test_explicit_port_names_and_unrecognised_ids_are_not_guessed(self):
        self.connections['ports'][0]['display_label'] = 'Valley approach'
        self.connections['ports'][1]['id'] = 'branch-17'
        text = self.render()
        self.assertIn('**HSR · Valley approach**<br>`W.in`', text)
        self.assertIn('**HSR · branch-17**<br>`branch-17`', text)
        self.assertNotIn('South entrance', text)

    def test_saved_path_needs_both_extraction_and_current_graph_check(self):
        self.assertTrue(self.metric('Saved PATH').startswith('[✓]'))
        self.connections['software_status']['path_extraction'] = 'unverified'
        self.assertIn('extraction: unverified', self.metric('Saved PATH'))
        self.assertNotIn('✓', self.metric('Saved PATH'))
        self.connections['software_status']['path_extraction'] = 'passed'
        self.connections['journeys'][0]['role'] = 'changed'
        # The unaffected movement still cannot borrow the old whole-graph check.
        self.assertIn('stale', self.metric('Saved PATH', entry='S.in', exit_port='W.out'))

    def test_missing_software_check_and_missing_graph_scope_do_not_pass(self):
        self.record['cases'] = [case for case in self.record['cases'] if case['kind'] != 'software_connectivity']
        self.assertIn('missing software check', self.metric('Saved PATH'))
        self.setUp()
        case = next(case for case in self.record['cases'] if case['kind'] == 'software_connectivity')
        case['dependencies'].pop('graph:fixture')
        self.assertIn('missing graph scope', self.metric('Saved PATH'))

    def test_forbidden_and_undeclared_are_distinct_from_failed_tests(self):
        forbidden = self.cell(exit_port='W.out')
        self.assertIn('Forbidden (saved PATH)', forbidden)
        self.assertNotIn('✗', forbidden)
        unknown = self.cell(exit_port='S.out')
        self.assertIn('? not declared', unknown)
        self.assertNotIn('Forbidden', unknown)
        self.assertNotIn('N/A', unknown)

    def test_forbidden_negative_check_failures_staleness_and_missing_cases_stay_visible(self):
        cases = [case for case in self.record['cases'] if case['kind'] == 'in_game_forbidden_transfer']
        self.record = record_user_result(self.record, cases[0]['id'], 'failed', explicit_user_confirmation=True,
                                        reviewer='Fixture reviewer', confirmed_at='2026-10-27T10:01:00Z',
                                        evidence=['Observed the forbidden transfer.'],
                                        environment={'platform': 'fixture OS', 'game_version': 'fixture version',
                                                     'nam_profile': 'fixture profile'})
        self.record = record_user_result(self.record, cases[1]['id'], 'passed', explicit_user_confirmation=True,
                                        reviewer='Fixture reviewer', confirmed_at='2026-10-27T10:01:00Z',
                                        evidence=['Observed the transfer remained unavailable.'],
                                        environment={'platform': 'fixture OS', 'game_version': 'fixture version',
                                                     'nam_profile': 'fixture profile'})
        stale = next(case for case in self.record['cases'] if case['id'] == cases[1]['id'])
        stale['observations'][-1]['dependency_fingerprint'] = '0' * 64
        self.record['cases'] = [case for case in self.record['cases'] if case['id'] != cases[3]['id']]
        cell = self.cell(exit_port='W.out')
        self.assertIn('negative game check: [✗ 0/4 passed; failed: 1; stale: 1; unverified: 1; missing: 1]', cell)
        self.assertIn('TESTING.md#case-' + cases[0]['id'], cell)
        self.assertEqual('— forbidden movement', self.metric('Route Query', exit_port='W.out'))
        self.assertEqual('— forbidden movement', self.metric('Visible travel', exit_port='W.out'))

    def test_saved_path_gate_does_not_hide_failed_software_when_extraction_is_missing(self):
        case = next(case for case in self.record['cases'] if case['kind'] == 'software_connectivity')
        self.record = record_software_result(self.record, case['id'], 'failed', verifier='Fixture verifier',
                                            checked_at='2026-10-27T10:02:00Z', evidence=['Actual fixture failure.'])
        self.connections['software_status']['path_extraction'] = 'unverified'
        self.assertIn('✗ failed; extraction: unverified', self.metric('Saved PATH'))
        self.assertIn('✗ failed; extraction: unverified', self.cell(exit_port='W.out'))

    def test_generic_journey_pass_never_becomes_query_or_visible_travel_pass(self):
        self.record = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints)
        for angle in (0, 90, 180, 270):
            self.observe('in_game_journey', angle=angle)
        for label in ('Route Query', 'Visible travel'):
            self.assertIn('0/4 passed', self.metric(label))
            self.assertNotIn('✓', self.metric(label))

    def test_partial_rotations_and_unverified_counts_remain_explicit(self):
        identifier = self.observe('in_game_route_query')
        query = self.metric('Route Query')
        self.assertIn('Partial: 1/4 passed; unverified: 3', query)
        self.assertIn('TESTING.md#case-in_game_route_query-', query)
        self.assertNotIn('✓', query)
        self.assertIn('0/4 passed', self.metric('Visible travel'))
        self.assertNotIn(identifier, self.metric('Visible travel'))

    def test_missing_case_is_different_from_unverified_case(self):
        self.record['cases'] = [case for case in self.record['cases']
                                if not (case['kind'] == 'in_game_route_query'
                                        and case['scope'].get('rotation_ccw_degrees') == 270)]
        self.assertIn('unverified: 3; missing: 1', self.metric('Route Query'))
        self.record['cases'] = [case for case in self.record['cases'] if case['kind'] != 'in_game_route_query']
        self.assertIn('missing: 4', self.metric('Route Query'))
        self.assertNotIn('TESTING.md#case-', self.metric('Route Query'))

    def test_failure_and_stale_observations_are_not_hidden_by_partial_passes(self):
        self.observe('in_game_route_query', angle=0)
        self.observe('in_game_route_query', angle=90, result='failed')
        stale_id = self.observe('in_game_route_query', angle=180)
        case = next(case for case in self.record['cases'] if case['id'] == stale_id)
        case['observations'][-1]['dependency_fingerprint'] = '0' * 64
        query = self.metric('Route Query')
        self.assertIn('✗ 1/4 passed; failed: 1; stale: 1; unverified: 1', query)
        self.assertNotIn('✓', query)

    def test_stale_only_and_explicit_inapplicability_have_different_states(self):
        identifier = self.observe('in_game_visible_travel')
        case = next(case for case in self.record['cases'] if case['id'] == identifier)
        case['observations'][-1]['dependency_fingerprint'] = '0' * 64
        self.assertIn('↻ 0/4 passed; stale: 1; unverified: 3', self.metric('Visible travel'))
        self.setUp()
        case = next(case for case in self.record['cases'] if case['kind'] == 'in_game_visible_travel')
        self.record = declare_not_applicable(self.record, case['id'], explicit_user_confirmation=True,
                                            reviewer='Fixture reviewer', confirmed_at='2026-10-27T10:01:00Z',
                                            reason='Explicit fixture-only inapplicability.')
        self.assertIn('N/A: 1/4; passed: 0/4; unverified: 3', self.metric('Visible travel'))

    def test_complete_query_and_travel_have_separate_exact_case_links(self):
        for kind in ('in_game_route_query', 'in_game_visible_travel'):
            for angle in (0, 90, 180, 270):
                self.observe(kind, angle=angle)
        self.assertIn('[✓ 4/4](TESTING.md#case-in_game_route_query-', self.metric('Route Query'))
        self.assertIn('[✓ 4/4](TESTING.md#case-in_game_visible_travel-', self.metric('Visible travel'))
        self.assertNotIn('✓', self.metric('Game appearance†'))

    def test_appearance_is_shared_whole_assembly_evidence_not_journey_evidence(self):
        for angle in (0, 90, 180, 270):
            self.observe('in_game_render', angle=angle)
        appearance = self.metric('Game appearance†')
        self.assertIn('✓ 4/4', appearance)
        self.assertEqual(appearance, self.metric('Game appearance†', entry='S.in', exit_port='W.out'))
        self.assertEqual(appearance, self.metric('Game appearance†', exit_port='W.out'))
        self.assertIn('not a separate inspection of each journey', self.render())
        self.assertIn('recorded environment', self.render())

    def test_declared_transposed_states_and_missing_pose_do_not_borrow_proper_passes(self):
        self.connections['supported_orientations'] = [
            {'rotation_ccw_degrees': 0, 'construction_transposed': False},
            {'rotation_ccw_degrees': 0, 'construction_transposed': True},
        ]
        self.record = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints,
                                        split_journey_observations=True)
        self.observe('in_game_route_query', angle=0)
        self.assertIn('Partial: 1/2 passed; unverified: 1', self.metric('Route Query'))
        self.observe('in_game_route_query', angle=0, transposed=True)
        self.assertIn('✓ 2/2', self.metric('Route Query'))

    def test_nondefault_declared_rotation_is_the_required_scope(self):
        self.connections['supported_orientations'] = [
            {'rotation_ccw_degrees': 90, 'construction_transposed': False},
        ]
        self.record = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints,
                                        split_journey_observations=True)
        self.assertIn('0/1 passed; unverified: 1', self.metric('Route Query'))
        self.observe('in_game_route_query', angle=90)
        self.assertIn('✓ 1/1', self.metric('Route Query'))

    def test_mixed_service_variant_and_role_labels_do_not_collapse_shared_engine(self):
        self.connections['ports'] += [self.port('M.in', 'in', 'monorail', 'monorail', 'passengers'),
                                       self.port('M.out', 'out', 'monorail', 'monorail', 'passengers'),
                                       self.port('G.in', 'in', 'hsr', 'ghsr'), self.port('G.out', 'out', 'hsr', 'ghsr')]
        self.connections['journeys'] += [self.journey('monorail', 'M.in', 'M.out', 'monorail', 'passengers'),
                                          self.journey('ground', 'G.in', 'G.out')]
        self.record = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints,
                                        split_journey_observations=True)
        for angle in (0, 90, 180, 270):
            self.observe('in_game_route_query', angle=angle)
        text = self.render()
        for label in ('Network: **hsr**', 'Network: **monorail**', 'Variant: ghsr', 'Role: passengers'):
            self.assertIn(label, text)
        self.assertIn('0/4 passed', self.metric('Route Query', entry='M.in', exit_port='M.out'))
        self.assertIn('0/4 passed', self.metric('Route Query', entry='G.in', exit_port='G.out'))
        self.assertIn('not declared', self.metric('Saved PATH', entry='M.in', exit_port='E.out'))

    def test_same_journey_id_with_a_different_service_or_role_cannot_supply_manual_passes(self):
        for angle in (0, 90, 180, 270):
            self.observe('in_game_route_query', angle=angle)
        for field, value in (('service_network', 'monorail'), ('role', 'passengers')):
            with self.subTest(field=field):
                altered = deepcopy(self.connections)
                altered['journeys'][0][field] = value
                for port in altered['ports']:
                    if port['id'] in ('W.in', 'E.out'):
                        port[field] = value
                text = render_assembly_connection_matrix(altered, self.record)
                row = next(line for line in text.splitlines() if line.startswith('| ') and '`W.in`' in line)
                cell = next(value for value in row.split(' | ') if '**Route Query:**' in value
                            and 'Forbidden' not in value and 'not declared' not in value)
                self.assertIn('**Route Query:** ? 0/4 passed; missing: 4', cell)
                self.assertNotIn('✓ 4/4', cell)

    def test_repeat_render_and_compacted_records_preserve_every_input_byte(self):
        before_connections, before_record = deepcopy(self.connections), deepcopy(self.record)
        first = self.render()
        self.assertEqual(first, self.render())
        self.assertEqual(first, render_assembly_connection_matrix(self.connections, compact_manual_record(self.record)))
        self.assertEqual(before_connections, self.connections)
        self.assertEqual(before_record, self.record)


if __name__ == '__main__':
    unittest.main()
