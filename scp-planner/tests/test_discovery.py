"""Discovery eligibility and complete-boundary search using synthetic exports.

Library loading is mocked: these fixtures exercise the consumer, not compiled
game networks, source schemas, or game operation. The real matcher is retained.
"""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

PLANNER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLANNER / 'src'))
from scp_planner import discovery


def resolved_piece(identifier, services=('rail', 'road', 'walk')):
    """Two whole stacked boundaries with distinct synthetic service channels."""
    config = {'rail': (2., 15.5, 7001, 'rail', 'synthetic-train', 'synthetic-rail'),
              'road': (2.5, 0., 7002, 'road-lane', 'synthetic-car', 'synthetic-road'),
              'walk': (6.39, 0., 7003, 'walkway', 'synthetic-walk', 'synthetic-road')}
    groups, bundles = [], []
    for edge, name, north in ((1, 'north', 8.), (3, 'south', -8.)):
        ids = []
        for service in services:
            offset, height, engine, kind, mode, construction = config[service]
            group_id = service + '-' + name
            ids.append(group_id)
            members, channels = [], []
            for sign, lane in ((1, 'right'), (-1, 'left')):
                member = group_id + '-' + lane
                channel, cut = service + '-' + lane, member + '-cut'
                direction = 'out' if (edge == 1) == (sign == 1) else 'in'
                members.append({'id': member, 'source_port_id': 'source-' + member,
                                'direction': direction, 'channel_id': channel, 'cut_id': cut,
                                'endpoint_m': [sign * offset, north, height],
                                'tangent': [0., float(sign)], 'grade': 0.,
                                'service_network': 'synthetic-' + service,
                                'engine_transport': engine, 'role': 'primary',
                                'traffic_modes': [mode]})
                channels.append({'id': channel, 'kind': kind, 'traffic_modes': [mode],
                                 'cuts': [{'id': cut, 'member_ids': [member]}]})
            groups.append({'id': group_id, 'boundary_bundle_id': 'boundary-' + name,
                           'outward_normal': [0., 1. if edge == 1 else -1.],
                           'tile_seam_center_m': [0., north, 0.],
                           'construction_network': construction,
                           'channels': channels, 'members': members})
        bundles.append({'id': 'boundary-' + name, 'source_cell': [0, 0],
                        'edge': name, 'connector_ids': ids})
    return {'id': identifier, 'cells': [[0, 0]], 'groups': groups,
            'boundary_bundles': bundles,
            'supported_orientations': [{'rotation_ccw_degrees': angle,
                                        'construction_transposed': False}
                                       for angle in (0, 90, 180, 270)]}


class SourceFailure(ValueError):
    def __init__(self, code, detail):
        super().__init__(detail)
        self.code = code


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='scp-planner-discovery-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.catalog = {'domains': {'rail': {'path': 'domains/rail'},
                                    'other': {'path': 'domains/other'}}, 'pieces': []}
        self.pieces, self.failures, self.calls = {}, {}, []
        self.source = SimpleNamespace(load_catalog=lambda root: self.catalog)
        self.addCleanup(patch.stopall)
        patch.object(discovery, '_check_source_root', return_value=self.root).start()
        patch.object(discovery, 'source_module', return_value=self.source).start()
        patch.object(discovery._library, 'load_exports', side_effect=self.load_exports).start()
        patch.object(discovery._library, 'load_library', side_effect=AssertionError('No authored-data fallback')).start()

    def add_piece(self, identifier, *, state='fresh', domain='rail', services=('rail', 'road', 'walk')):
        self.catalog['pieces'].append({'id': identifier, 'domain': domain})
        directory = self.root / 'domains' / domain / '00_pieces' / identifier
        directory.mkdir(parents=True)
        (directory / 'piece.json').write_text(json.dumps({'id': identifier, 'domain': domain}))
        if state != 'legacy':
            (directory / 'connector-groups.jsonc').write_text('{}')
        if state not in ('legacy', 'missing-export'):
            (directory / 'connector-data.json').write_text('{}')
        self.pieces[identifier] = resolved_piece(identifier, services)
        return directory

    def load_exports(self, root, identifiers, *, domain_id):
        self.assertEqual(root, self.root)
        self.assertEqual(len(identifiers), 1)
        identifier = identifiers[0]
        self.calls.append((identifier, domain_id))
        if identifier in self.failures:
            raise self.failures[identifier]
        return {'pieces': {identifier: deepcopy(self.pieces[identifier])},
                'exports': {identifier: {'path': f'domains/{domain_id}/00_pieces/{identifier}/connector-data.json',
                                         'sha256': 'synthetic-source-proof'}},
                'source_format': 'connector-data-v1'}

    def run_discovery(self, **kwargs):
        return discovery.discover_compatibility(self.root, domain_id='rail', **kwargs)

    def test_mixed_registry_distinguishes_legacy_missing_stale_and_invalid(self):
        self.add_piece('fresh-a')
        self.add_piece('fresh-b')
        legacy = self.add_piece('legacy', state='legacy')
        (legacy / 'connections.json').write_text(json.dumps({'compatible_counterparts': ['fresh-a']}))
        self.add_piece('missing', state='missing-export')
        self.add_piece('stale')
        self.add_piece('invalid')
        self.add_piece('stale-authoring')
        self.add_piece('different-domain', domain='other')
        stray = self.root / 'domains/rail/00_pieces/unregistered'
        stray.mkdir()
        (stray / 'connector-groups.jsonc').write_text('{}')
        (stray / 'connector-data.json').write_text('{}')
        self.failures = {'stale': SourceFailure('stale_export', 'Changed bytes'),
                         'invalid': SourceFailure('invalid_export', 'A stale word in an invalid document'),
                         'stale-authoring': SourceFailure('stale_source', 'Changed authored binding')}
        before = {path: path.read_bytes() for path in self.root.rglob('*') if path.is_file()}
        report = self.run_discovery()
        states = {row['piece_id']: row for row in report['piece_eligibility']}
        self.assertEqual(report['eligible_piece_ids'], ['fresh-a', 'fresh-b'])
        self.assertEqual(states['legacy']['status'], 'not_migrated')
        self.assertEqual(states['missing']['reason'], 'missing_export')
        self.assertEqual(states['stale']['reason'], 'stale_export')
        self.assertEqual(states['invalid']['reason'], 'invalid_export')
        self.assertEqual(states['stale-authoring']['reason'], 'stale_source')
        self.assertEqual(report['counts']['registered_pieces'], 7)
        self.assertEqual(report['counts']['not_migrated'], 1)
        self.assertEqual(report['counts']['excluded'], 4)
        self.assertEqual(set(self.calls), {(name, 'rail') for name in
                                         ('fresh-a', 'fresh-b', 'stale', 'invalid', 'stale-authoring')})
        self.assertEqual(before, {path: path.read_bytes() for path in before})
        self.assertNotIn('incompatible', json.dumps(report))

    def test_entire_eligible_set_has_no_three_candidate_cap_and_keeps_whole_maps(self):
        for number in range(6):
            self.add_piece(f'fresh-{number}')
        report = self.run_discovery(query_piece_id='fresh-0', query_boundary_id='boundary-north')
        candidates = report['candidate_placements']
        self.assertEqual({row['b_piece_id'] for row in candidates}, {f'fresh-{n}' for n in range(6)})
        self.assertEqual(len(candidates), 12)
        self.assertEqual(report['counts']['searched_type_pairs'], 6)
        self.assertEqual(report['counts']['raw_group_matches'], 36)
        keys = {(row['a_piece_id'], row['a_boundary_id'], row['b_piece_id'], row['b_boundary_id'],
                 row['relative_rotation_ccw'], tuple(row['relative_position_m'])) for row in candidates}
        self.assertEqual(len(keys), len(candidates))
        for candidate in candidates:
            self.assertEqual(candidate['a_boundary_id'], 'boundary-north')
            self.assertEqual(len(candidate['bundle_group_pairs']), 3)
            self.assertEqual(len(candidate['member_pairs']), 6)
            self.assertEqual(sum(len(pair['member_pairs']) for pair in candidate['bundle_group_pairs']), 6)
            self.assertEqual(candidate['checks']['occupied_cells'], 'passed')
            self.assertEqual(candidate['checks']['complete_boundary_metadata'], 'passed')
            for check in ('full_scene', 'physical_seams', 'construction_clearance',
                          'geometry_collisions', 'terrain_construction', 'in_game'):
                self.assertEqual(candidate['checks'][check], 'unverified')

    def test_complete_mixed_boundaries_reject_rail_only_and_road_only_candidates(self):
        self.add_piece('full')
        self.add_piece('full-counterpart')
        self.add_piece('rail-only', services=('rail',))
        self.add_piece('road-only', services=('road', 'walk'))
        report = self.run_discovery(query_piece_id='full', query_boundary_id='boundary-north')
        self.assertEqual(report['counts']['eligible_pieces'], 4)
        self.assertEqual(report['counts']['searched_type_pairs'], 4)
        self.assertEqual({row['b_piece_id'] for row in report['candidate_placements']},
                         {'full', 'full-counterpart'})

    def test_unqueried_search_includes_each_unordered_type_pair_and_self_pair(self):
        for number in range(4):
            self.add_piece(f'fresh-{number}')
        report = self.run_discovery()
        self.assertEqual(report['counts']['searched_type_pairs'], 10)
        self.assertEqual(len(report['candidate_placements']), 40)
        pairs = {(row['a_piece_id'], row['b_piece_id']) for row in report['candidate_placements']}
        self.assertTrue(all(a <= b for a, b in pairs))
        self.assertEqual({a for a, b in pairs if a == b}, set(report['eligible_piece_ids']))

    def test_result_order_is_independent_of_registry_and_group_order(self):
        self.add_piece('fresh-b')
        self.add_piece('fresh-a')
        first = self.run_discovery()['candidate_placements']
        self.catalog['pieces'].reverse()
        for piece in self.pieces.values():
            piece['groups'].reverse()
        self.assertEqual(first, self.run_discovery()['candidate_placements'])

    def test_ineligible_query_is_reported_without_falling_back_or_matching(self):
        self.add_piece('legacy', state='legacy')
        self.add_piece('fresh')
        with patch.object(discovery, 'find_matches', side_effect=AssertionError('No matching of legacy data')):
            report = self.run_discovery(query_piece_id='legacy')
        self.assertEqual(report['query']['status'], 'not_eligible')
        self.assertEqual(report['query']['eligibility']['status'], 'not_migrated')
        self.assertEqual(report['candidate_placements'], [])
        self.assertEqual(report['counts']['searched_type_pairs'], 0)

    def test_unknown_queries_and_domains_fail_explicitly(self):
        self.add_piece('fresh')
        for kwargs in ({'query_piece_id': 'unknown'},
                       {'query_piece_id': 'fresh', 'query_boundary_id': 'individual-rail-group'},
                       {'query_boundary_id': 'boundary-north'}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.run_discovery(**kwargs)
        with self.assertRaisesRegex(ValueError, 'Unknown registered transport domain'):
            discovery.discover_compatibility(self.root, domain_id='unknown')

    def test_unknown_validation_failures_are_not_guessed_from_text(self):
        self.add_piece('unknown-error')
        self.failures['unknown-error'] = ValueError('stale or invalid words are not machine codes')
        report = self.run_discovery()
        self.assertEqual(report['piece_eligibility'][0]['reason'], 'validation_failed')


class DiscoverySourceSelectionTests(unittest.TestCase):
    def test_different_code_and_data_roots_are_rejected_before_registry_loading(self):
        with tempfile.TemporaryDirectory(prefix='scp-wrong-discovery-root-') as temporary:
            with self.assertRaisesRegex(ValueError, 'code and data roots must match'):
                discovery.discover_compatibility(temporary)


def load_tool():
    spec = importlib.util.spec_from_file_location('discover_compatibility_tool', PLANNER / 'tools/discover_compatibility.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DiscoveryCommandTests(unittest.TestCase):
    def test_command_delegates_selection_and_writes_only_private_report(self):
        tool = load_tool()
        with tempfile.TemporaryDirectory(prefix='scp-discovery-command-') as temporary:
            planner = Path(temporary)
            destination = planner / 'local/compatibility/scoped.json'
            report = {'status': 'completed', 'domain_id': 'rail', 'query': {'piece_id': 'fresh'},
                      'counts': {'eligible_pieces': 4}, 'checks_not_established': {'in_game': 'unverified'}}
            with patch.object(tool, 'PLANNER', planner), patch.object(tool, 'discover_compatibility', return_value=report) as run, patch('builtins.print'):
                tool.main(['--custom-pieces-root', '/chosen/library', '--domain', 'rail', '--piece', 'fresh',
                           '--boundary', 'boundary-north', '--report', str(destination)])
            run.assert_called_once_with(Path('/chosen/library'), domain_id='rail',
                                        query_piece_id='fresh', query_boundary_id='boundary-north')
            self.assertEqual(json.loads(destination.read_text()), report)

    def test_command_rejects_reports_outside_planner_local_before_search(self):
        tool = load_tool()
        with patch.object(tool, 'discover_compatibility') as run, patch('sys.stderr'), self.assertRaises(SystemExit) as error:
            tool.main(['--report', str(PLANNER / 'README.md')])
        self.assertEqual(error.exception.code, 2)
        run.assert_not_called()


if __name__ == '__main__':
    unittest.main()
