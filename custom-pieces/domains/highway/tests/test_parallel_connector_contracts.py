"""Replay accepted numeric connector facts without private builds or inputs."""
from copy import deepcopy
import json
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.connectivity import assembly_connectivity
from scp.connector_metadata import load_library
from scp_highway.connections import reviewed_contract, reviewed_path_ports, validate_connection_record
from scp_highway.parallel_connector_contracts import CONTRACTS, REFERENCE, load_contracts
from scp_highway.parallel_verify import expected_ports, reviewed_contract as independent_contract


class ParallelConnectorContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evidence = jsonc.load(ROOT / REFERENCE)
        cls.pieces, cls.records = {}, {}
        for recipe, facts in CONTRACTS.items():
            directory = ROOT / 'domains/highway/00_pieces' / facts['reference_piece_id']
            cls.pieces[recipe] = jsonc.load(directory / 'piece.jsonc')
            cls.records[recipe] = jsonc.load(directory / 'connections.json')

    def test_all_fifteen_accepted_sources_remain_numeric_and_unverified_in_game(self):
        self.assertEqual(len(CONTRACTS), 15)
        self.assertEqual(self.evidence['state'], 'accepted-independently-checked-saved-resources')
        self.assertEqual(self.evidence['game_operation'], 'unverified')
        self.assertFalse(self.evidence['counterpart_matching_performed'])
        verification = self.evidence['verification']
        self.assertEqual(verification['package_construction_checks'], 'passed-by-separate-fresh-verify_build')
        self.assertEqual(verification['assembly_resources_only_package_construction_status'], 'not-run')
        self.assertTrue(verification['native_wheeltrack_seam_uv']['passed'])
        self.assertEqual(verification['native_wheeltrack_seam_uv']['actual_saved_dd_mis_seam_pairs_checked'], 20)
        self.assertEqual(sum(len(facts['cells']) for facts in CONTRACTS.values()), 31)
        self.assertEqual(load_contracts(), CONTRACTS)
        # Resource identities and hashes are public numeric evidence; native
        # binary/text payloads remain in ignored local inputs and saved builds.
        encoded = json.dumps(self.evidence, sort_keys=True)
        self.assertNotIn('SC4PATHS', encoded)
        self.assertNotIn('base64', encoded)

    def test_actual_extracted_records_replay_every_owned_path_hash_and_boundary(self):
        totals = [0, 0, 0]
        for recipe, piece in self.pieces.items():
            record = self.records[recipe]
            with self.subTest(piece=piece['id']):
                facts = validate_connection_record(piece, record)
                totals = [a + b for a, b in zip(totals,
                    (len(record['ports']), len(record['journeys']), len(facts['channels'])))]
                self.assertEqual(record['software_status']['in_game'], 'unverified')
                self.assertEqual(len(reviewed_path_ports(piece)), len(facts['ports']))
                self.assertEqual(facts['physical_ownership']['model_owner'], piece['geometry_key'])
        self.assertEqual(totals[:2], [176, 92])
        self.assertGreater(totals[2], 15)

    def test_complete_boundary_graph_agrees_with_independent_approved_source(self):
        for recipe, piece in self.pieces.items():
            accepted = reviewed_contract(piece)
            independent = independent_contract(piece)
            self.assertEqual(set(accepted['ports']), set(independent['ports']))
            self.assertEqual(set(map(tuple, accepted['movements'])), set(map(tuple, independent['movements'])))
            for name, point in accepted['ports'].items():
                with self.subTest(piece=piece['id'], port=name):
                    self.assertLessEqual(math.dist(point, independent['ports'][name]), 1.1e-6)
                    self.assertEqual(accepted['port_transports'][name], independent['port_transports'][name])
                    self.assertEqual(accepted['port_directions'][name], independent['port_directions'][name])
                    self.assertGreater(sum(a * b for a, b in zip(accepted['port_vectors'][name],
                                                                independent['port_vectors'][name])), .99999)
            # The independent route verifier supplies signed actual travel
            # grades and source cells, rather than physical render cuts.
            for port in CONTRACTS[recipe]['ports']:
                matches = [p for p in expected_ports(piece)
                    if p['direction'] == port['direction'] and p['transport'] == port['engine_transport']
                    and math.dist(p['point_m'], port['endpoint_m']) <= 1.1e-6]
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]['source_cell'], port['source_cell'])
                self.assertEqual(matches[0]['edge'], port['edge'])
                self.assertLessEqual(abs(matches[0]['grade'] - port['grade']), 1e-4)

    def test_boundary_groups_cover_all_car_and_pedestrian_channels(self):
        identifiers = [piece['id'] for piece in self.pieces.values()]
        library = load_library(ROOT, identifiers, domain_id='highway')['pieces']
        for recipe, piece in self.pieces.items():
            resolved = library[piece['id']]
            facts = CONTRACTS[recipe]
            with self.subTest(piece=piece['id']):
                self.assertEqual({member['source_port_id'] for group in resolved['groups']
                                  for member in group['members']}, {p['id'] for p in facts['ports']})
                self.assertEqual({channel['id'] for channel in resolved['channels']},
                                 {channel['id'] for channel in facts['channels']})
                self.assertEqual({s['channel_id'] for s in facts['channel_sources']},
                                 {channel['id'] for channel in facts['channels']})
                self.assertEqual(len(resolved['journeys']), len(facts['movements']))
                expected = independent_contract(piece)['port_vectors']
                self.assertTrue(all(math.dist(port['tangent'], expected[port['id']]) <= 1e-12
                                    for port in facts['ports']))
                controls = facts['full_saved_chord_direction_check']
                self.assertTrue(controls['passed'])
                self.assertTrue(all(control['reviewed_vector_error'] <= control['quantization_error_bound']
                                    for control in controls['controls']))

    def test_shared_assembly_has_only_twenty_real_outer_ports_and_fourteen_complete_journeys(self):
        identifier = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond'
        directory = ROOT / 'domains/highway/01_assemblies' / identifier
        scene = jsonc.load(directory / 'assembly.jsonc')
        pieces = {piece['id']: piece for piece in self.pieces.values()}
        records = {record['subject_id']: record for record in self.records.values()}
        measured = assembly_connectivity(identifier, scene, records, pieces)
        saved = jsonc.load(directory / 'connections.json')
        for record in (measured, saved):
            self.assertEqual((len(record['ports']), len(record['journeys']),
                              len(record['encoded_route_joins'])), (20, 14, 78))
            self.assertEqual({port['variant'] for port in record['ports']},
                             {'dd-rhw-l1', 'dd-rhw-l2', 'avenue-ground', 'avenue-sidewalk'})
        self.assertTrue(any(math.dist(port['tangent'], port['sampled_tangent']) > 2e-5
                            for facts in CONTRACTS.values() for port in facts['ports']))
        self.assertEqual(self.evidence['verification']['shared_assembly_graph']['internal_access_cut_ports_exposed'], 0)

    def test_actual_upper_grade_model_and_outlying_native_ports_have_an_unclipped_card_frame(self):
        try:
            from scp.city_grid import make_camera
            from scp.connector_overview import (PAGE_MARGIN, PAGE_WIDTH, build_records,
                make_boundary_cards, make_overview_camera, viewport_marker)
            from scp.piece_previews import local_piece_grid
        except ModuleNotFoundError:
            self.skipTest('Pillow/NumPy overview dependencies unavailable')
        identifier = 'ddrhw-parallel-upper-exit-grade'
        resolved = load_library(ROOT, [identifier], domain_id='highway')['pieces'][identifier]
        records = build_records(resolved)
        local = local_piece_grid(resolved['piece'])
        # Exact actual saved preview vertices at the four camera-axis extrema.
        # These reproduce its old model/grid camera without retaining a native
        # model payload. Source: accepted parts-01 manifest e111dc91..., whose
        # raw model fingerprints remain in this type's connections.json.
        vertices = [(-18.965721130371094, 15.0, 32.178924560546875),
                    (16.530088424682617, 0.0, -11.802167892456055),
                    (19.774259567260742, 0.0, -6.5610551834106445),
                    (-23.020137786865234, 16.390625, 28.12371063232422)]
        self.assertEqual(self.evidence['source']['manifest_sha256'],
                         'e111dc910bc3bcfc913ed5f99bfa1b9521f4e0ad8511dfcf1eb37bc8727ff9ef')
        old = make_camera(vertices, 45., 31., PAGE_WIDTH - 2 * PAGE_MARGIN, 1000,
                          bounds_world_m=local['bounds_world_m'], padding=90)
        def badges(camera):
            return [viewport_marker(camera.project_world(*record.get('marker_enh_m', record['anchor_enh_m'])),
                                    index, camera.width)
                    for card in make_boundary_cards(deepcopy(records))
                    for index, record in enumerate(card['groups'])]
        self.assertTrue(any(badge[1] < 24 for badge in badges(old)))
        before = deepcopy(records), deepcopy(local), deepcopy(vertices)
        camera, frame = make_overview_camera(vertices, records, local)
        self.assertEqual((records, local, vertices), before)
        self.assertTrue(frame['additional_stack_reserve_applied'])
        for badge in badges(camera):
            self.assertGreaterEqual(badge[0] + PAGE_MARGIN, 24)
            self.assertLessEqual(badge[0] + PAGE_MARGIN, PAGE_WIDTH - 24)
            self.assertGreaterEqual(badge[1], 24)
            self.assertLessEqual(badge[1], camera.height + 4)
        for record in records:
            for member in record['members']:
                point = camera.project_world(*member['endpoint_m'])
                self.assertTrue(0 <= point[0] <= camera.width and 0 <= point[1] <= camera.height)

    def test_nonzero_grades_and_wrong_native_hashes_are_rejected(self):
        recipe = next(recipe for recipe, facts in CONTRACTS.items() if any(p['grade'] for p in facts['ports']))
        piece = self.pieces[recipe]
        for mutation in ('height', 'grade', 'path-hash'):
            record = deepcopy(self.records[recipe])
            port = next(p for p in record['ports'] if p['grade'])
            if mutation == 'height':
                port['endpoint_m'][2] += .01
            elif mutation == 'grade':
                port['grade'] = -port['grade']
            else:
                key = next(key for key in record['source']['resource_fingerprints']
                           if key.startswith('path:') and '-a966883f-' in key)
                record['source']['resource_fingerprints'][key] = '0' * 64
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                validate_connection_record(piece, record)

    def test_forbidden_movement_cannot_be_added_to_accepted_journeys(self):
        recipe = next(recipe for recipe, facts in CONTRACTS.items() if facts['forbidden_transfers'])
        record = deepcopy(self.records[recipe])
        first, last = CONTRACTS[recipe]['forbidden_transfers'][0]
        record['journeys'].append({'entry_port': first, 'exit_port': last})
        with self.assertRaisesRegex(ValueError, 'journeys'):
            validate_connection_record(self.pieces[recipe], record)


if __name__ == '__main__':
    unittest.main()
