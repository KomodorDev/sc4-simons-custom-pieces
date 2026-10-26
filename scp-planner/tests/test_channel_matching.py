"""Check the application contract independently of profiles and authoring groups.

Resolved fixtures altered here are artificial boundary data, not compiled Street
pieces, construction clearance, or evidence of traffic inside SimCity 4.
"""
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scp-planner/src'))
from scp_planner import metadata, jsonc

CROSSING = 'hsr-component-modular-crossing-core'
CURVE = 'hsr-component-tight-paired-curve90-l4-to-mid'


def one_boundary(pilot, slug, endpoint):
    result = deepcopy(pilot['pieces'][slug])
    result['groups'] = [g for g in result['groups'] if g['id'] == endpoint]
    result['boundary_bundles'] = [b for b in result['boundary_bundles'] if endpoint in b['connector_ids']]
    return result


def one_cut(piece, direction):
    group = piece['groups'][0]
    group['members'] = [m for m in group['members'] if m['direction'] == direction]
    used = {m['channel_id'] for m in group['members']}
    group['channels'] = [c for c in group['channels'] if c['id'] in used]
    return group


class ChannelMatchingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pilot = metadata.load_library(ROOT / 'custom-pieces', [CROSSING, CURVE])

    def setUp(self):
        self.a = one_boundary(self.pilot, CROSSING, 'upper-end-b')
        self.b = one_boundary(self.pilot, CURVE, 'curve-end-a')

    def test_application_loads_exports_without_falling_back_to_authored_sidecars(self):
        sentinel = {'source_format': 'connector-data-v1'}
        with patch.object(metadata._library, 'load_exports', return_value=sentinel) as loader:
            self.assertIs(metadata.load_pilot(ROOT / 'custom-pieces', [CROSSING]), sentinel)
        loader.assert_called_once_with(ROOT / 'custom-pieces', [CROSSING], domain_id='high-speed-rail')

    def test_parser_and_validator_are_the_source_owned_functions(self):
        self.assertIs(metadata.validate_piece, metadata._library.validate_piece)
        self.assertEqual(jsonc.loads.__module__, 'scp.jsonc')

    def test_profile_names_and_descriptive_fields_do_not_decide_matches(self):
        self.b['groups'][0]['profile_id'] = 'an-unrelated-authoring-label'
        self.b['groups'][0]['profile'] = {'section_id': 'different', 'expected_deck_width_m': 999.}
        self.assertEqual(len(metadata.find_matches(self.a, self.b)), 1)

    def test_equivalent_edge_contents_can_use_different_group_partitions(self):
        original = self.b['groups'][0]
        parts = []
        for index, channel in enumerate(original['channels']):
            part = deepcopy(original)
            part['id'] = 'partition-'+str(index)
            part['channels'] = [deepcopy(channel)]
            part['members'] = [m for m in part['members'] if m['channel_id'] == channel['id']]
            parts.append(part)
        self.b['groups'] = parts
        self.b['boundary_bundles'][0]['connector_ids'] = [p['id'] for p in parts]
        matches = metadata.find_matches(self.a, self.b)
        self.assertEqual(len(matches), 2)
        for match in matches:
            self.assertEqual(match['relative_position_m'], [0., 64.])
            self.assertEqual(len(match['bundle_group_pairs']), 2)
            self.assertEqual(sum(len(g['member_pairs']) for g in match['bundle_group_pairs']), 2)

    def test_channel_ids_are_local_identities_instead_of_compatibility_keys(self):
        group = self.b['groups'][0]
        for index, channel in enumerate(group['channels']):
            old, new = channel['id'], 'new-channel-'+str(index)
            channel['id'] = new
            for member in group['members']:
                if member['channel_id'] == old:
                    member['channel_id'] = new
        self.assertEqual(len(metadata.find_matches(self.a, self.b)), 1)

    def test_channel_kind_cannot_be_replaced_by_matching_mode_and_geometry(self):
        self.b['groups'][0]['channels'][0]['kind'] = 'walkway'
        self.assertEqual(metadata.find_matches(self.a, self.b), [])

    def test_construction_network_is_explicit_and_not_inferred_from_engine(self):
        self.a['groups'][0]['construction_network'] = 'monorail'
        for other in (None, 'street'):
            self.b['groups'][0]['construction_network'] = other
            self.assertEqual(metadata.find_matches(self.a, self.b), [])
        self.b['groups'][0]['construction_network'] = 'monorail'
        self.assertEqual(len(metadata.find_matches(self.a, self.b)), 1)

    def test_mode_coverage_can_match_one_record_to_two_source_records(self):
        first, second = one_cut(self.a, 'in'), one_cut(self.b, 'out')
        for group in (first, second):
            group['channels'][0]['traffic_modes'] = ['synthetic-car', 'synthetic-bus']
            group['members'][0]['traffic_modes'] = ['synthetic-car', 'synthetic-bus']
        car = second['members'][0]
        bus = deepcopy(car)
        car['traffic_modes'], bus['traffic_modes'] = ['synthetic-car'], ['synthetic-bus']
        bus['id'], bus['source_port_id'] = 'synthetic-bus', 'synthetic-source-bus'
        second['members'].append(bus)
        second['channels'][0]['cuts'][0]['member_ids'].append(bus['id'])
        matches = metadata.find_matches(self.a, self.b)
        self.assertEqual(len(matches), 1)
        self.assertEqual(len(matches[0]['member_pairs']), 2)
        self.assertEqual({p['b_port_id'] for p in matches[0]['member_pairs']}, {car['id'], bus['id']})
        second['members'].remove(bus)
        second['channels'][0]['cuts'][0]['member_ids'].remove(bus['id'])
        self.assertEqual(metadata.find_matches(self.a, self.b), [])

    def test_travel_grade_agrees_while_outward_grades_have_opposite_signs(self):
        first, second = one_cut(self.a, 'in'), one_cut(self.b, 'out')
        first['members'][0]['grade'] = second['members'][0]['grade'] = .1
        self.assertEqual(len(metadata.find_matches(self.a, self.b)), 1)
        second['members'][0]['grade'] = -.1
        self.assertEqual(metadata.find_matches(self.a, self.b), [])

    def test_actual_endpoint_heading_is_compared_without_profile_tokens(self):
        first, second = one_cut(self.a, 'in'), one_cut(self.b, 'out')
        first['members'][0]['tangent'] = second['members'][0]['tangent'] = [.6, -.8]
        self.assertEqual(len(metadata.find_matches(self.a, self.b)), 1)
        second['members'][0]['tangent'] = [0., -1.]
        self.assertEqual(metadata.find_matches(self.a, self.b), [])

    def test_identical_overlapping_channels_require_unambiguous_mapping(self):
        first, second = one_cut(self.a, 'in'), one_cut(self.b, 'out')
        for group in (first, second):
            original = group['channels'][0]
            channel, member = deepcopy(original), deepcopy(group['members'][0])
            channel['id'] += '-duplicate'
            member['id'] += '-duplicate'
            member['channel_id'] = channel['id']
            channel['cuts'][0]['id'] += '-duplicate'
            channel['cuts'][0]['member_ids'] = [member['id']]
            group['channels'].append(channel)
            group['members'].append(member)
        self.assertEqual(metadata.find_matches(self.a, self.b), [])

    def test_one_bidirectional_channel_is_not_two_physical_channels(self):
        for group in (self.a['groups'][0], self.b['groups'][0]):
            for member in group['members']:
                member['endpoint_m'][:2] = group['anchor_m'][:2]
        group = self.a['groups'][0]
        channel = group['channels'][0]
        channel['cuts'][0]['member_ids'] = [m['id'] for m in group['members']]
        for member in group['members']:
            member['channel_id'] = channel['id']
        group['channels'] = [channel]
        self.assertEqual(metadata.find_matches(self.a, self.b), [])

    def test_bidirectional_channel_requires_both_permitted_flows(self):
        for group in (self.a['groups'][0], self.b['groups'][0]):
            channel = group['channels'][0]
            channel['cuts'][0]['member_ids'] = [m['id'] for m in group['members']]
            for member in group['members']:
                member['endpoint_m'][:2] = group['anchor_m'][:2]
                member['channel_id'] = channel['id']
            group['channels'] = [channel]
        self.assertEqual(len(metadata.find_matches(self.a, self.b)), 1)
        group = self.b['groups'][0]
        removed = group['members'].pop()
        group['channels'][0]['cuts'][0]['member_ids'].remove(removed['id'])
        self.assertEqual(metadata.find_matches(self.a, self.b), [])


if __name__ == '__main__':
    unittest.main()
