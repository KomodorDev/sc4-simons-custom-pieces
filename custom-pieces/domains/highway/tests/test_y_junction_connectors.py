"""Public connector precision reconstructed from independently encoded PATHs."""
from copy import deepcopy
import hashlib
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]
from scp import jsonc
from scp.connectivity import PLACED_ROUTE_GRADE_TOLERANCE, assembly_connectivity, piece_connectivity
from scp_highway import connections
from scp_highway import ramp_paths
from scp_highway import y_junction_verify as independent


def encoded_path_fixtures():
    """Serialize generic cuts of the maintained source, without the Y writer."""
    source = jsonc.load(ROOT/'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/design-geometry.jsonc')
    cut = ramp_paths.slice_routes([{'id': name, 'points': points,
                                   'lane': source['route_metadata'][name]['from_lane']}
                                  for name, points in source['routes'].items()])
    result = []
    for slug in ('ddrhw-y-diagonal-stem-split', 'ddrhw-y-diagonal-branch', 'ddrhw-y-orthogonal-core'):
        piece = jsonc.load(ROOT/f'domains/highway/00_pieces/{slug}/piece.jsonc')
        origin = piece['engineering']['world_origin_cell']
        resources = {}
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            world = cell[0]+origin[0], cell[1]+origin[1]
            raw = ramp_paths.encode_paths(cut.get(world, []), allow_empty=True)
            lines = raw.decode('ascii').splitlines()
            lines[4] = '1'
            resources[0x296678F7, 0xA966883F, int(tile, 16)] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
        result.append((piece, resources))
    return result


def fixture_facts(piece, resources):
    """Bind only test-fixture PATH hashes; this creates no accepted source file."""
    facts = independent.reviewed_facts(piece)
    facts['path_hashes_by_cell'] = [[cell, hashlib.sha256(resources[
        0x296678F7, 0xA966883F, int(tile, 16)]).hexdigest()]
        for cell, tile in zip(piece['cells'], piece['tile_ids'])]
    return facts


def shared_assembly(fixtures, mutate=None):
    """Exercise the real shared consumer at the maintained scene placements."""
    scene = jsonc.load(ROOT/'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction/assembly.jsonc')
    pieces = {piece['id']: piece for piece, _resources in fixtures}
    records = {piece['id']: piece_connectivity(piece, resources, contract=independent.reviewed_contract(piece),
                                               service_classifier=connections.service_classifier)
               for piece, resources in fixtures}
    if mutate:
        mutate(records)
    return assembly_connectivity('ddrhw-compact-diagonal-y-junction', scene, records, pieces), records


class YJunctionConnectorPrecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = encoded_path_fixtures()

    def test_all_three_public_records_match_source_precision_and_strict_validator(self):
        for piece, resources in self.fixtures:
            contract = independent.reviewed_contract(piece)
            record = piece_connectivity(piece, resources, contract=contract,
                                        service_classifier=connections.service_classifier)
            facts = fixture_facts(piece, resources)
            actual = {port['id']: port for port in record['ports']}
            self.assertEqual(set(actual), {port['id'] for port in facts['ports']})
            for expected in facts['ports']:
                measured = actual[expected['id']]
                with self.subTest(piece=piece['id'], port=expected['id']):
                    for field in ('endpoint_m', 'sampled_tangent', 'tangent'):
                        self.assertLessEqual(math.dist(measured[field], expected[field]), 1e-12, field)
                    self.assertEqual(measured['grade'], expected['grade'])
                    for field in ('direction', 'engine_transport', 'edge', 'service_network',
                                  'service_family', 'variant', 'role', 'channel_kind', 'traffic_modes'):
                        self.assertEqual(measured[field], expected[field], field)
            with patch('scp_highway.connections._reviewed_facts', return_value=facts):
                self.assertIs(connections.validate_connection_record(piece, record), facts)

    def test_precise_contract_does_not_become_the_graph_rounded_measurement(self):
        piece, _resources = self.fixtures[0]
        contract = independent.reviewed_contract(piece)
        facts = independent.reviewed_facts(piece)
        endpoint_differences = [math.dist(contract['ports'][p['id']], p['endpoint_m']) for p in facts['ports']]
        sampled_differences = [math.dist(contract['port_vectors'][p['id']], p['sampled_tangent']) for p in facts['ports']]
        self.assertGreater(max(endpoint_differences), 1e-8)
        self.assertGreater(max(sampled_differences), 1e-6)
        self.assertTrue(all(all(value == round(value, 6) for value in port['endpoint_m']) for port in facts['ports']))

    def test_old_saved_tangent_used_as_graph_sample_and_wrong_grade_are_rejected(self):
        observed_grade = False
        for piece, resources in self.fixtures:
            contract = independent.reviewed_contract(piece)
            record = piece_connectivity(piece, resources, contract=contract,
                                        service_classifier=connections.service_classifier)
            facts = fixture_facts(piece, resources)
            differing = next((p for p in facts['ports'] if math.dist(p['sampled_tangent'], p['tangent']) > 1e-6), None)
            if differing:
                bad = deepcopy(facts)
                item = next(p for p in bad['ports'] if p['id'] == differing['id'])
                item['sampled_tangent'] = item['tangent']
                with patch('scp_highway.connections._reviewed_facts', return_value=bad), self.assertRaisesRegex(ValueError, 'travel tangent'):
                    connections.validate_connection_record(piece, record)
            graded = next((p for p in facts['ports'] if abs(p['grade']) > 1e-4), None)
            if graded:
                observed_grade = True
                bad = deepcopy(facts)
                next(p for p in bad['ports'] if p['id'] == graded['id'])['grade'] += .001
                with patch('scp_highway.connections._reviewed_facts', return_value=bad), self.assertRaisesRegex(ValueError, 'signed travel grade'):
                    connections.validate_connection_record(piece, record)
        self.assertTrue(observed_grade, 'The fixture must exercise real sloped module cuts')

    def test_shared_assembly_keeps_six_journeys_twelve_native_ports_and_precise_sloped_joins(self):
        result, records = shared_assembly(self.fixtures)
        ports = {port['id']: port for port in result['ports']}
        self.assertEqual(len(ports), 12)
        self.assertEqual(len(result['journeys']), 6)
        self.assertEqual(len(result['encoded_route_joins']), 8)
        self.assertEqual(sum(len(record['ports']) for record in records.values()), 28)
        expected = {('in', (-24., n, 15.)) for n in (-35.2, -28.8)}
        expected |= {('out', (-24., n, 7.5)) for n in (-35.2, -28.8)}
        expected |= {('out', (-24., n, 15.)) for n in (28.8, 35.2)}
        expected |= {('in', (-24., n, 7.5)) for n in (28.8, 35.2)}
        expected |= {('out', (56., n, 15.)) for n in (-2.5, 2.5)}
        expected |= {('in', (56., n, 7.5)) for n in (-2.5, 2.5)}
        measured = {(port['direction'], tuple(round(value, 6) for value in port['endpoint_m']))
                    for port in ports.values()}
        self.assertEqual(measured, expected)

        def arm(port):
            east, north, _height = port['endpoint_m']
            return 'C' if abs(east - 56.) < 1e-6 else ('A' if north < 0. else 'B')
        movements = {(arm(ports[journey['entry_port']]), arm(ports[journey['exit_port']]))
                     for journey in result['journeys']}
        self.assertEqual(movements, {('A', 'B'), ('B', 'A'), ('A', 'C'), ('C', 'A'), ('B', 'C'), ('C', 'B')})
        graded = 0
        differing_graph_witness = False
        for join in result['encoded_route_joins']:
            first = next(port for port in records[join['from_piece']]['ports'] if port['id'] == join['from_port'])
            second = next(port for port in records[join['to_piece']]['ports'] if port['id'] == join['to_port'])
            for port in (first, second):
                self.assertEqual(port['grade_basis'], 'actual_saved_PATH_before_graph_rounding')
                self.assertEqual(port['tangent_basis'], 'reviewed_contract')
                self.assertEqual(port['grade'], port['actual_saved_grade'])
                differing_graph_witness |= math.dist(port['actual_saved_tangent'], port['sampled_tangent']) > 1e-6
            if abs(first['grade']) > 1e-4:
                graded += 1
                self.assertLess(abs(first['actual_saved_grade'] - second['actual_saved_grade']),
                                PLACED_ROUTE_GRADE_TOLERANCE)
        self.assertEqual(graded, 2)
        self.assertTrue(differing_graph_witness, 'Exercise precise saved witnesses beyond six-decimal graph sampling')

    def test_shared_assembly_rejects_join_with_changed_saved_grade_or_declared_heading(self):
        for field in ('actual_saved_grade', 'tangent'):
            def mutate(records):
                record = records['ddrhw-y-diagonal-branch']
                port = next(port for port in record['ports'] if port['id'] == 'b-c-out')
                if field == 'actual_saved_grade':
                    port[field] += .01
                else:
                    x, y = port[field]
                    port[field] = [-y, x]
            with self.subTest(field=field):
                result, _records = shared_assembly(self.fixtures, mutate)
                self.assertEqual(len(result['encoded_route_joins']), 7)
                self.assertEqual(len(result['ports']), 14)
                self.assertFalse(any(join['from_port'] == 'b-c-out' and join['to_port'] == 'b-c-in'
                                     for join in result['encoded_route_joins']))


if __name__ == '__main__':
    unittest.main()
