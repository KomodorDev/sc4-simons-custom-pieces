"""Compact assembly summaries preserve exact directional evidence limits."""
from copy import deepcopy
import json
from pathlib import Path
import re
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'framework'))

from scp.assembly_matrix import (ASSEMBLY_CONNECTION_MATRIX, render_assembly_connection_matrix,
                                 summarize_assembly_connection_matrix)
from scp.content import (compact_manual_record, declare_not_applicable, fingerprint,
                         new_manual_record, record_software_result, record_user_result, refresh_manual_record)


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

    @staticmethod
    def cell_from_text(text, entry='W.in', exit_port='E.out'):
        rows = [line.split(' | ') for line in text.splitlines() if line.startswith('| ')]
        column = next(index for index, value in enumerate(rows[0]) if f'`{exit_port}`' in value)
        row = next(row for row in rows[2:] if f'`{entry}`' in row[0])
        return row[column]

    def cell(self, **pair):
        return self.cell_from_text(self.render(), **pair)

    def metric(self, label, **pair):
        return self.cell(**pair).split(f'**{label}:** ', 1)[1].split('<br>', 1)[0]

    def status(self, label, **pair):
        text = self.metric(label, **pair)
        return text.split(']', 1)[0][1:] if text.startswith('[') else text

    def assert_summary_matches_render(self):
        summary = summarize_assembly_connection_matrix(self.connections, self.record)
        # Independently count the displayed results, excluding the appearance line.
        table = '\n'.join(line for line in self.render().splitlines() if line.startswith('| '))
        labels = {'saved_path': r'\*\*Saved PATH:\*\*',
                  'route_query': r'\*\*Route Query:\*\*',
                  'visible_travel': r'\*\*Visible (?:train )?travel:\*\*',
                  'forbidden': r'In-game check:'}
        self.assertEqual(set(summary), {'metrics'})
        self.assertEqual(set(summary['metrics']), set(labels))
        for key, label in labels.items():
            symbols = re.findall(label + r' \[?([✅❌?])', table)
            self.assertEqual(summary['metrics'][key], {
                'confirmed': symbols.count('✅'), 'failed': symbols.count('❌'),
                'not_established': symbols.count('?')}, key)
        self.assertEqual(json.loads(json.dumps(summary)), summary)
        return summary['metrics']

    def test_directional_axes_three_cell_metrics_and_one_separate_appearance(self):
        text = self.render()
        self.assertTrue(text.startswith('## 4. Connection matrix\n\n'))
        self.assertNotIn('\n## Connection matrix\n', text)
        header = next(line for line in text.splitlines() if line.startswith('| Entrance'))
        self.assertIn('**HSR · East exit**<br>`E.out`', header)
        self.assertNotIn('`W.in`', header)
        self.assertIn('**HSR · West entrance**<br>`W.in`', text)
        for label in ('Saved PATH', 'Route Query', 'Visible train travel'):
            self.assertIn(f'**{label}:**', self.cell())
        self.assertEqual(text.count('**Game appearance:**'), 1)
        self.assertNotIn('appearance', self.cell())
        for duplicate in ('Network:', 'Variant: hsr', 'Role: primary'):
            self.assertNotIn(duplicate, text)
        self.assertEqual(ASSEMBLY_CONNECTION_MATRIX, 'ASSEMBLY CONNECTION MATRIX')

    def test_explicit_port_names_and_unrecognised_ids_are_not_guessed(self):
        self.connections['ports'][0]['display_label'] = 'Valley approach'
        self.connections['ports'][1]['id'] = 'branch-17'
        text = self.render()
        self.assertIn('**HSR · Valley approach**<br>`W.in`', text)
        self.assertIn('**HSR · branch-17**<br>`branch-17`', text)
        self.assertNotIn('South entrance', text)

    def test_saved_path_needs_extraction_and_a_current_graph_check(self):
        self.assertEqual(self.status('Saved PATH'), '✅')
        self.connections['software_status']['path_extraction'] = 'unverified'
        self.assertEqual(self.status('Saved PATH'), '?')
        self.connections['software_status']['path_extraction'] = 'passed'
        self.connections['journeys'][0]['role'] = 'changed'
        self.assertEqual(self.status('Saved PATH', entry='S.in', exit_port='W.out'), '?')

    def test_missing_software_check_or_missing_graph_scope_never_passes(self):
        self.record['cases'] = [case for case in self.record['cases'] if case['kind'] != 'software_connectivity']
        self.assertEqual(self.status('Saved PATH'), '?')
        self.setUp()
        case = next(case for case in self.record['cases'] if case['kind'] == 'software_connectivity')
        case['dependencies'].pop('graph:fixture')
        self.assertEqual(self.status('Saved PATH'), '?')

    def test_forbidden_and_unknown_movements_are_not_failed_tests(self):
        forbidden = self.cell(exit_port='W.out')
        self.assertIn('**Forbidden**', forbidden)
        self.assertIn('In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-', forbidden)
        self.assertNotIn('❌', forbidden)
        self.assertNotIn('Route Query', forbidden)
        unknown = self.cell(exit_port='S.out')
        self.assertNotIn('Forbidden', unknown)
        for label in ('Saved PATH', 'Route Query', 'Visible travel'):
            self.assertIn(f'**{label}:** ?', unknown)

    def test_forbidden_current_failure_is_visible_despite_stale_or_missing_other_cases(self):
        cases = [case for case in self.record['cases'] if case['kind'] == 'in_game_forbidden_transfer']
        common = dict(explicit_user_confirmation=True, reviewer='Fixture reviewer',
                      confirmed_at='2026-10-27T10:01:00Z', evidence=['Explicit negative fixture observation.'],
                      environment={'platform': 'fixture OS', 'game_version': 'fixture version', 'nam_profile': 'fixture profile'})
        self.record = record_user_result(self.record, cases[0]['id'], 'failed', **common)
        self.record = record_user_result(self.record, cases[1]['id'], 'passed', **common)
        stale = next(case for case in self.record['cases'] if case['id'] == cases[1]['id'])
        stale['observations'][-1]['dependency_fingerprint'] = '0' * 64
        self.record['cases'] = [case for case in self.record['cases'] if case['id'] != cases[3]['id']]
        cell = self.cell(exit_port='W.out')
        self.assertIn('In-game check: [❌](TESTING.md#case-' + cases[0]['id'] + ')', cell)
        self.assertNotIn('Route Query', cell)
        self.assertNotIn('Visible train travel', cell)

    def test_current_software_failure_is_red_even_when_extraction_is_missing(self):
        case = next(case for case in self.record['cases'] if case['kind'] == 'software_connectivity')
        self.record = record_software_result(self.record, case['id'], 'failed', verifier='Fixture verifier',
                                            checked_at='2026-10-27T10:02:00Z', evidence=['Actual fixture failure.'])
        self.connections['software_status']['path_extraction'] = 'unverified'
        self.assertEqual(self.status('Saved PATH'), '❌')
        self.assertEqual(self.status('Saved PATH', exit_port='W.out'), '❌')

    def test_old_generic_journey_pass_never_becomes_query_or_visible_travel_pass(self):
        self.record = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints)
        for angle in (0, 90, 180, 270):
            self.observe('in_game_journey', angle=angle)
        self.assertEqual(self.status('Route Query'), '?')
        self.assertEqual(self.status('Visible train travel'), '?')

    def test_partial_coverage_is_unknown_with_exact_links_and_no_detail_counts(self):
        self.observe('in_game_route_query')
        self.assertEqual(self.status('Route Query'), '?')
        self.assertIn('TESTING.md#case-in_game_route_query-', self.metric('Route Query'))
        self.assertEqual(self.status('Visible train travel'), '?')
        for detail in ('1/4', 'Partial:', 'stale:', 'unverified:', 'missing:', 'N/A:'):
            self.assertNotIn(detail, self.render())

    def test_missing_cases_are_unknown_without_invented_exact_case_links(self):
        self.record['cases'] = [case for case in self.record['cases']
                                if not (case['kind'] == 'in_game_route_query'
                                        and case['scope'].get('rotation_ccw_degrees') == 270)]
        self.assertEqual(self.status('Route Query'), '?')
        self.record['cases'] = [case for case in self.record['cases'] if case['kind'] != 'in_game_route_query']
        self.assertEqual(self.metric('Route Query'), '?')

    def test_current_failure_outranks_partial_and_stale_observations(self):
        self.observe('in_game_route_query', angle=0)
        failure_id = self.observe('in_game_route_query', angle=90, result='failed')
        stale_id = self.observe('in_game_route_query', angle=180)
        case = next(case for case in self.record['cases'] if case['id'] == stale_id)
        case['observations'][-1]['dependency_fingerprint'] = '0' * 64
        self.assertEqual(self.status('Route Query'), '❌')
        self.assertIn('TESTING.md#case-' + failure_id, self.metric('Route Query'))

    def test_stale_evidence_and_explicit_inapplicability_are_question_marks(self):
        identifier = self.observe('in_game_visible_travel')
        case = next(case for case in self.record['cases'] if case['id'] == identifier)
        case['observations'][-1]['dependency_fingerprint'] = '0' * 64
        self.assertEqual(self.status('Visible train travel'), '?')
        self.assertIn('TESTING.md#case-' + identifier, self.metric('Visible train travel'))
        self.setUp()
        case = next(case for case in self.record['cases'] if case['kind'] == 'in_game_visible_travel')
        self.record = declare_not_applicable(self.record, case['id'], explicit_user_confirmation=True,
                                            reviewer='Fixture reviewer', confirmed_at='2026-10-27T10:01:00Z',
                                            reason='Explicit fixture-only inapplicability.')
        self.assertEqual(self.status('Visible train travel'), '?')

    def test_complete_query_and_travel_have_separate_green_statuses_and_exact_links(self):
        for kind in ('in_game_route_query', 'in_game_visible_travel'):
            for angle in (0, 90, 180, 270):
                self.observe(kind, angle=angle)
        self.assertEqual(self.status('Route Query'), '✅')
        self.assertEqual(self.status('Visible train travel'), '✅')
        self.assertIn('TESTING.md#case-in_game_route_query-', self.metric('Route Query'))
        self.assertIn('TESTING.md#case-in_game_visible_travel-', self.metric('Visible train travel'))

    def test_game_appearance_is_one_whole_assembly_status_outside_the_matrix(self):
        for angle in (0, 90, 180, 270):
            self.observe('in_game_render', angle=angle)
        text = self.render()
        appearance = next(line for line in text.splitlines() if line.startswith('**Game appearance:**'))
        self.assertIn('[✅](TESTING.md#case-in_game_render-', appearance)
        self.assertIn('complete assembly', appearance)
        self.assertLess(text.index('**Game appearance:**'), text.index('| Entrance'))
        self.assertEqual(text.count('**Game appearance:**'), 1)
        self.assertNotIn('appearance', self.cell())
        self.assertNotIn('appearance', self.cell(exit_port='W.out'))

    def test_default_records_still_require_their_declared_supported_manual_states(self):
        self.connections['supported_orientations'] = [
            {'rotation_ccw_degrees': 0, 'construction_transposed': False},
            {'rotation_ccw_degrees': 0, 'construction_transposed': True},
        ]
        self.record = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints,
                                        split_journey_observations=True)
        self.observe('in_game_route_query', angle=0)
        self.assertEqual(self.status('Route Query'), '?')
        self.observe('in_game_route_query', angle=0, transposed=True)
        self.assertEqual(self.status('Route Query'), '✅')

    def test_explicit_manual_scope_does_not_change_saved_software_coverage(self):
        self.observe('in_game_route_query', angle=0)
        self.assertEqual(self.status('Route Query'), '?')
        generated = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints,
                                      split_journey_observations=True,
                                      manual_check_orientations=[{'rotation_ccw_degrees': 0}])
        self.record = refresh_manual_record(self.record, generated)
        self.assertEqual(self.status('Route Query'), '✅')
        self.assertEqual(self.status('Visible train travel'), '?')
        self.assertEqual(self.status('Saved PATH'), '✅')
        self.assertEqual(len(self.record['supported_orientations']), 4)
        self.assertEqual(sum(case['kind'] == 'software_connectivity' for case in self.record['cases']), 1)

    def test_nondefault_manual_scope_uses_the_correct_exact_case(self):
        self.observe('in_game_route_query', angle=0)
        generated = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints,
                                      split_journey_observations=True,
                                      manual_check_orientations=[{'rotation_ccw_degrees': 90}])
        self.record = refresh_manual_record(self.record, generated)
        self.assertEqual(self.status('Route Query'), '?')
        identifier = self.observe('in_game_route_query', angle=90)
        self.assertEqual(self.status('Route Query'), '✅')
        self.assertIn('TESTING.md#case-' + identifier, self.metric('Route Query'))

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
        for label in ('**HSR ·', '**Monorail ·', 'Variant: ghsr', 'Role: passengers'):
            self.assertIn(label, self.render())
        self.assertEqual(self.status('Route Query', entry='M.in', exit_port='M.out'), '?')
        self.assertEqual(self.status('Route Query', entry='G.in', exit_port='G.out'), '?')
        self.assertEqual(self.status('Saved PATH', entry='M.in', exit_port='E.out'), '?')

    def test_changed_service_or_role_with_same_journey_id_cannot_borrow_passes(self):
        for angle in (0, 90, 180, 270):
            self.observe('in_game_route_query', angle=angle)
        for field, value in (('service_network', 'monorail'), ('role', 'passengers')):
            with self.subTest(field=field):
                altered = deepcopy(self.connections)
                altered['journeys'][0][field] = value
                for port in altered['ports']:
                    if port['id'] in ('W.in', 'E.out'):
                        port[field] = value
                cell = self.cell_from_text(render_assembly_connection_matrix(altered, self.record))
                self.assertIn('**Route Query:** ?', cell)
                self.assertNotIn('✅', cell)

    def test_repeat_render_and_compacted_records_preserve_every_input_byte(self):
        before_connections, before_record = deepcopy(self.connections), deepcopy(self.record)
        first = self.render()
        self.assertEqual(first, self.render())
        self.assertEqual(first, render_assembly_connection_matrix(self.connections, compact_manual_record(self.record)))
        self.assertEqual(before_connections, self.connections)
        self.assertEqual(before_record, self.record)

    def test_summary_counts_displayed_layers_including_undefined_movements(self):
        metrics = self.assert_summary_matches_render()
        self.assertEqual(metrics, {
            'saved_path': {'confirmed': 3, 'failed': 0, 'not_established': 3},
            'route_query': {'confirmed': 0, 'failed': 0, 'not_established': 5},
            'visible_travel': {'confirmed': 0, 'failed': 0, 'not_established': 5},
            'forbidden': {'confirmed': 0, 'failed': 0, 'not_established': 1},
        })
        # Three Saved PATH entries reference one software case, not three passes.
        self.assertEqual(sum(case['kind'] == 'software_connectivity' for case in self.record['cases']), 1)
        self.assertEqual(self.render().count('**Saved PATH:** [✅](TESTING.md#case-software_connectivity-'), 3)
        for angle in (0, 90, 180, 270):
            self.observe('in_game_render', angle=angle)
        self.assertEqual(self.assert_summary_matches_render(), metrics)

    def test_summary_requires_all_manual_orientations_but_respects_explicit_zero_degree_scope(self):
        self.observe('in_game_route_query', angle=0)
        self.observe('in_game_visible_travel', angle=0)
        self.assertEqual(self.assert_summary_matches_render()['route_query']['confirmed'], 0)
        generated = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints,
                                      split_journey_observations=True,
                                      manual_check_orientations=[{'rotation_ccw_degrees': 0}])
        self.record = refresh_manual_record(self.record, generated)
        metrics = self.assert_summary_matches_render()
        self.assertEqual(metrics['route_query'], {'confirmed': 1, 'failed': 0, 'not_established': 4})
        self.assertEqual(metrics['visible_travel'], {'confirmed': 1, 'failed': 0, 'not_established': 4})
        self.assertEqual(metrics['saved_path'], {'confirmed': 3, 'failed': 0, 'not_established': 3})
        self.assertEqual(len(self.record['supported_orientations']), 4)

    def test_summary_counts_each_journey_displayed_in_one_pair_without_inventing_software_cases(self):
        self.connections['journeys'].append(self.journey('second-west-east', 'W.in', 'E.out'))
        self.record = new_manual_record('fixture', 'assembly', self.connections, self.fingerprints,
                                        split_journey_observations=True)
        software = next(case for case in self.record['cases'] if case['kind'] == 'software_connectivity')
        self.record = record_software_result(self.record, software['id'], 'passed', verifier='Fixture verifier',
                                            checked_at='2026-10-27T10:00:00Z', evidence=['Actual fixture check.'])
        metrics = self.assert_summary_matches_render()
        self.assertEqual(metrics['saved_path'], {'confirmed': 4, 'failed': 0, 'not_established': 3})
        self.assertEqual(metrics['route_query'], {'confirmed': 0, 'failed': 0, 'not_established': 6})
        self.assertEqual(metrics['visible_travel'], {'confirmed': 0, 'failed': 0, 'not_established': 6})
        self.assertEqual(sum(case['kind'] == 'software_connectivity' for case in self.record['cases']), 1)
        self.assertIn('Journey: `second-west-east`', self.cell())

    def test_summary_forbidden_check_confirms_unavailability_and_keeps_failures(self):
        cases = [case for case in self.record['cases'] if case['kind'] == 'in_game_forbidden_transfer']
        common = dict(explicit_user_confirmation=True, reviewer='Fixture reviewer',
                      confirmed_at='2026-10-27T10:01:00Z', evidence=['Explicit negative fixture observation.'],
                      environment={'platform': 'fixture OS', 'game_version': 'fixture version', 'nam_profile': 'fixture profile'})
        for case in cases:
            self.record = record_user_result(self.record, case['id'], 'passed', **common)
        self.assertEqual(self.assert_summary_matches_render()['forbidden'],
                         {'confirmed': 1, 'failed': 0, 'not_established': 0})
        self.record = record_user_result(self.record, cases[0]['id'], 'failed', **common)
        self.record['cases'] = [case for case in self.record['cases'] if case['id'] != cases[-1]['id']]
        self.assertEqual(self.assert_summary_matches_render()['forbidden'],
                         {'confirmed': 0, 'failed': 1, 'not_established': 0})

    def test_summary_does_not_confirm_stale_missing_duplicate_or_inapplicable_cases(self):
        for defect in ('stale', 'missing', 'duplicate', 'not_applicable'):
            with self.subTest(defect=defect):
                self.setUp()
                for angle in (0, 90, 180, 270):
                    self.observe('in_game_route_query', angle=angle)
                self.assertEqual(self.assert_summary_matches_render()['route_query']['confirmed'], 1)
                case = next(case for case in self.record['cases'] if case['kind'] == 'in_game_route_query')
                if defect == 'stale':
                    case['observations'][-1]['dependency_fingerprint'] = '0' * 64
                elif defect == 'missing':
                    self.record['cases'].remove(case)
                elif defect == 'duplicate':
                    self.record['cases'].append(deepcopy(case))
                else:
                    self.record = declare_not_applicable(
                        self.record, case['id'], explicit_user_confirmation=True,
                        reviewer='Fixture reviewer', confirmed_at='2026-10-27T10:02:00Z',
                        reason='Explicit fixture-only inapplicability.')
                self.assertEqual(self.assert_summary_matches_render()['route_query'],
                                 {'confirmed': 0, 'failed': 0, 'not_established': 5})

    def test_summary_keeps_current_failures_despite_incomplete_and_stale_coverage(self):
        self.observe('in_game_route_query', angle=0, result='failed')
        stale_id = self.observe('in_game_route_query', angle=90)
        next(case for case in self.record['cases'] if case['id'] == stale_id)['observations'][-1]['dependency_fingerprint'] = '0' * 64
        self.record['cases'] = [case for case in self.record['cases']
                                if not (case['kind'] == 'in_game_route_query'
                                        and case['scope'].get('rotation_ccw_degrees') == 270)]
        metrics = self.assert_summary_matches_render()
        self.assertEqual(metrics['route_query'], {'confirmed': 0, 'failed': 1, 'not_established': 4})
        software = next(case for case in self.record['cases'] if case['kind'] == 'software_connectivity')
        self.record = record_software_result(self.record, software['id'], 'failed', verifier='Fixture verifier',
                                            checked_at='2026-10-27T10:02:00Z', evidence=['Actual fixture failure.'])
        self.connections['software_status']['path_extraction'] = 'unverified'
        self.assertEqual(self.assert_summary_matches_render()['saved_path'],
                         {'confirmed': 0, 'failed': 3, 'not_established': 3})

    def test_summary_rejects_stale_resource_and_graph_evidence(self):
        for dependency in ('resource', 'graph'):
            with self.subTest(dependency=dependency):
                self.setUp()
                for angle in (0, 90, 180, 270):
                    self.observe('in_game_route_query', angle=angle)
                if dependency == 'resource':
                    self.connections['source'] = {'resource_fingerprints': {
                        'path:fixture:one': fingerprint(b'changed fixture PATH')}}
                else:
                    # Reordering declarations preserves displayed pairs, but changes the graph proof.
                    self.connections['journeys'].reverse()
                metrics = self.assert_summary_matches_render()
                self.assertEqual(metrics['saved_path'], {'confirmed': 0, 'failed': 0, 'not_established': 6})
                if dependency == 'resource':
                    self.assertEqual(metrics['route_query']['confirmed'], 0)

    def test_summary_does_not_borrow_query_passes_for_changed_pair_semantics(self):
        for field, value in (('service_network', 'monorail'), ('role', 'passengers'), ('variant', 'ghsr')):
            with self.subTest(field=field):
                self.setUp()
                self.connections['journeys'][0]['variant'] = 'hsr'
                for angle in (0, 90, 180, 270):
                    self.observe('in_game_route_query', angle=angle)
                self.assertEqual(self.assert_summary_matches_render()['route_query']['confirmed'], 1)
                if field != 'variant':
                    self.connections['journeys'][0][field] = value
                for port in self.connections['ports']:
                    if port['id'] in ('W.in', 'E.out'):
                        port[field] = value
                self.assertEqual(self.assert_summary_matches_render()['route_query']['confirmed'], 0)

    def test_summary_and_render_accept_compacted_records_without_mutation(self):
        for angle in (0, 90, 180, 270):
            self.observe('in_game_route_query', angle=angle)
        summary = self.assert_summary_matches_render()
        self.record = compact_manual_record(self.record)
        before_connections, before_record = deepcopy(self.connections), deepcopy(self.record)
        self.assertEqual(self.assert_summary_matches_render(), summary)
        self.assertEqual(self.assert_summary_matches_render(), summary)
        self.assertEqual(self.connections, before_connections)
        self.assertEqual(self.record, before_record)

    def test_current_trumpet_summary_counts_matrix_entries_and_its_selected_manual_scope(self):
        base = Path(__file__).resolve().parents[1] / 'domains/high-speed-rail/01_assemblies/hsr-trumpet-straight-stem'
        self.connections = json.loads((base / 'connections.json').read_text())
        self.record = json.loads((base / 'checks/manual-tests.json').read_text())
        self.assertEqual(self.record['manual_check_orientations'], [{'rotation_ccw_degrees': 0}])
        self.assertEqual(self.assert_summary_matches_render(), {
            'saved_path': {'confirmed': 9, 'failed': 0, 'not_established': 0},
            'route_query': {'confirmed': 0, 'failed': 0, 'not_established': 6},
            'visible_travel': {'confirmed': 0, 'failed': 0, 'not_established': 6},
            'forbidden': {'confirmed': 0, 'failed': 0, 'not_established': 3},
        })


if __name__ == '__main__':
    unittest.main()
