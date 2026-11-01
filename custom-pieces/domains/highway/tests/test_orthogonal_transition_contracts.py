"""Bound accepted connector facts without claiming a native model/build pass.

Loader fixtures contain synthetic PATH hashes in a disposable root. Freezer
fixtures mock the full-build gate and graph extraction explicitly; they test
trust-boundary rejection and publication order, not native resource quality.
"""
from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))

from scp import jsonc
from scp.dbpf import pack_dbpf
from scp_highway import connections
from scp_highway import orthogonal_transition_contracts as contracts
from scp_highway import orthogonal_transition_verify as independent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def source_piece(*, mirrored=False):
    identity = independent.MIRRORED_PIECE_ID if mirrored else independent.PIECE_ID
    return jsonc.load(ROOT / 'domains/highway/00_pieces' / identity / 'piece.jsonc')


def fixture_evidence(piece):
    facts = independent.reviewed_facts(piece)
    facts['path_hashes_by_cell'] = [[cell, sha(f'synthetic PATH cell {cell}'.encode())] for cell in piece['cells']]
    facts['raw_path_fingerprint_status'] = 'accepted-checked-saved-build'
    return {'schema_version': 1, 'state': 'accepted-independently-checked-saved-resources',
            'game_operation': 'unverified', 'source': {'build': 'dist/synthetic-fixture-only',
            'manifest_sha256': sha(b'synthetic manifest'), 'verification_passed': True}, 'contract': facts}


def connection_record(piece, facts):
    tiles = dict(zip(map(tuple, piece['cells']), piece['tile_ids']))
    ports = deepcopy(facts['ports'])
    for port in ports:
        port['boundary_sources'] = [{'cell': port['source_cell'], 'edge': port['edge'],
                                    'tile_id': tiles[tuple(port['source_cell'])]}]
    return {'subject_id': piece['id'], 'subject_kind': 'piece', 'ports': ports,
            'journeys': [{'entry_port': a, 'exit_port': b} for a, b in facts['movements']],
            'forbidden_transfers': [{'from_port': a, 'to_port': b} for a, b in facts['forbidden_transfers']],
            'source': {'resource_fingerprints': {
                f'path:{piece["id"]}:296678f7-a966883f-{tiles[tuple(cell)]}': digest
                for cell, digest in facts['path_hashes_by_cell']}}}


class OrthogonalContractLoaderTests(unittest.TestCase):
    mirrored = False

    def setUp(self):
        self.piece = source_piece(mirrored=self.mirrored)
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.destination = self.root / contracts.reference(self.piece)
        self.evidence = fixture_evidence(self.piece)

    def write(self, evidence=None):
        self.destination.parent.mkdir(parents=True, exist_ok=True)
        self.destination.write_text('// Synthetic numeric test fixture; not native acceptance evidence.\n'
                                    + json.dumps(self.evidence if evidence is None else evidence) + '\n')

    def test_missing_evidence_returns_no_accepted_hashes_and_strict_extraction_refuses_fallback(self):
        self.assertIsNone(contracts.load_contract(self.piece, self.root))
        facts = independent.reviewed_facts(self.piece)
        self.assertEqual(facts['path_hashes_by_cell'], [])
        self.assertEqual(facts['raw_path_fingerprint_status'], 'requires-checked-saved-build-freeze')
        with patch.object(contracts, 'load_contract', return_value=None):
            with self.assertRaisesRegex(ValueError, 'independently checked saved PATH fingerprints'):
                connections.validate_connection_record(self.piece, connection_record(self.piece, facts))

    def test_independent_semantics_cover_eight_ports_four_journeys_and_twelve_forbidden_transfers(self):
        facts = independent.reviewed_facts(self.piece)
        self.assertEqual(len(facts['ports']), 8)
        self.assertEqual(len({port['id'] for port in facts['ports']}), 8)
        self.assertEqual(len(facts['movements']), 4)
        self.assertEqual(len(facts['forbidden_transfers']), 12)
        self.assertEqual({tuple(pair) for pair in facts['movements']}, {
            ('upper-lane-01-in', 'upper-lane-01-out'), ('upper-lane-02-in', 'upper-lane-02-out'),
            ('lower-lane-01-in', 'lower-lane-01-out'), ('lower-lane-02-in', 'lower-lane-02-out')})
        incoming = {port['id'] for port in facts['ports'] if port['direction'] == 'in'}
        outgoing = {port['id'] for port in facts['ports'] if port['direction'] == 'out'}
        self.assertEqual(set(facts['movements']) | set(facts['forbidden_transfers']),
                         {(a, b) for a in incoming for b in outgoing})

    def test_valid_synthetic_freeze_loads_all_twelve_hashes_without_mutating_source_or_returns(self):
        self.write()
        before = deepcopy(self.piece)
        loaded = contracts.load_contract(self.piece, self.root)
        self.assertEqual(loaded['raw_path_fingerprint_status'], 'accepted-checked-saved-build')
        self.assertEqual(len(loaded['path_hashes_by_cell']), 12)
        self.assertEqual(loaded['path_hashes_by_cell'][0][0], [0, 0])
        loaded['ports'][0]['endpoint_m'][0] = 999
        loaded['path_hashes_by_cell'][0][1] = '0' * 64
        reread = contracts.load_contract(self.piece, self.root)
        self.assertNotEqual(reread['ports'][0]['endpoint_m'][0], 999)
        self.assertNotEqual(reread['path_hashes_by_cell'][0][1], '0' * 64)
        self.assertEqual(self.piece, before)

    def test_hash_table_rejects_empty_missing_duplicate_or_unowned_cells_including_model_only_cell(self):
        original = self.evidence['contract']['path_hashes_by_cell']
        for rows in ([], original[1:], [*original[:-1], original[0]],
                     [[[99, 99], original[0][1]], *original[1:]]):
            changed = deepcopy(self.evidence); changed['contract']['path_hashes_by_cell'] = rows
            self.write(changed)
            with self.subTest(rows=rows), self.assertRaisesRegex(ValueError, 'PATH hashes'):
                contracts.load_contract(self.piece, self.root)
        changed = deepcopy(self.evidence); del changed['contract']['path_hashes_by_cell']; self.write(changed)
        with self.assertRaisesRegex(ValueError, 'PATH hashes'):
            contracts.load_contract(self.piece, self.root)

    def test_hash_rows_require_exact_integer_cell_coordinates_and_lowercase_sha256_strings(self):
        first = self.evidence['contract']['path_hashes_by_cell'][0]
        mutations = [None, {}, 'row', [], [first[0]], [*first, 'extra'],
                     [None, first[1]], [[0], first[1]], [[0, 0, 0], first[1]],
                     [[False, 0], first[1]], [[0.0, 0], first[1]], [['0', 0], first[1]],
                     [first[0], None], [first[0], 1], [first[0], ''], [first[0], 'f' * 63],
                     [first[0], 'F' * 64], [first[0], 'g' * 64]]
        for row in mutations:
            changed = deepcopy(self.evidence); changed['contract']['path_hashes_by_cell'][0] = row
            self.write(changed)
            with self.subTest(row=row), self.assertRaisesRegex(ValueError, 'PATH hashes'):
                contracts.load_contract(self.piece, self.root)
        for rows in (None, {}, 'all rows'):
            changed = deepcopy(self.evidence); changed['contract']['path_hashes_by_cell'] = rows
            self.write(changed)
            with self.subTest(rows=rows), self.assertRaisesRegex(ValueError, 'PATH hashes'):
                contracts.load_contract(self.piece, self.root)

    def test_frozen_evidence_cannot_redefine_independent_semantics(self):
        mutations = []
        changed = deepcopy(self.evidence); changed['contract']['ports'].pop(); mutations.append(changed)
        changed = deepcopy(self.evidence); changed['contract']['ports'][0]['endpoint_m'][0] += 0.1; mutations.append(changed)
        changed = deepcopy(self.evidence); changed['contract']['ports'][0]['variant'] = 'avenue-ground'; mutations.append(changed)
        changed = deepcopy(self.evidence); changed['contract']['ports'][0]['traffic_modes'] = ['bus']; mutations.append(changed)
        changed = deepcopy(self.evidence); changed['contract']['movements'][0] = ['upper-lane-01-in', 'lower-lane-01-out']; mutations.append(changed)
        changed = deepcopy(self.evidence); changed['contract']['forbidden_transfers'].pop(); mutations.append(changed)
        changed = deepcopy(self.evidence); changed['contract']['cells'][0] = [3, 3]; mutations.append(changed)
        changed = deepcopy(self.evidence); changed['contract']['channels'][0]['kind'] = 'rail-track'; mutations.append(changed)
        changed = deepcopy(self.evidence); changed['contract']['components'][0]['construction_network'] = 'avenue'; mutations.append(changed)
        changed = deepcopy(self.evidence); changed['contract']['extra_semantics'] = True; mutations.append(changed)
        for index, changed in enumerate(mutations):
            self.write(changed)
            with self.subTest(mutation=index), self.assertRaisesRegex(ValueError, 'independent review'):
                contracts.load_contract(self.piece, self.root)

    def test_accepted_header_requires_unverified_game_state_and_exact_software_verification_identity(self):
        mutations = []
        for key, value in [('schema_version', True), ('schema_version', 2), ('state', 'draft'),
                           ('game_operation', 'passed')]:
            changed = deepcopy(self.evidence); changed[key] = value; mutations.append(changed)
        for key, value in [('manifest_sha256', ''), ('manifest_sha256', 'A' * 64),
                           ('verification_passed', False), ('verification_passed', 1)]:
            changed = deepcopy(self.evidence); changed['source'][key] = value; mutations.append(changed)
        changed = deepcopy(self.evidence); del changed['source']['verification_passed']; mutations.append(changed)
        for index, changed in enumerate(mutations):
            self.write(changed)
            with self.subTest(mutation=index), self.assertRaisesRegex(ValueError, 'saved-resource'):
                contracts.load_contract(self.piece, self.root)
        for source in (None, [], 'not a source mapping'):
            changed = deepcopy(self.evidence); changed['source'] = source; self.write(changed)
            with self.subTest(source=source), self.assertRaisesRegex(ValueError, 'saved-resource'):
                contracts.load_contract(self.piece, self.root)

    def test_complete_hash_pins_cover_even_the_empty_model_only_path_when_record_is_validated(self):
        self.write()
        loader = contracts.load_contract
        with patch.object(contracts, 'load_contract', side_effect=lambda piece: loader(piece, self.root)):
            record = connection_record(self.piece, self.evidence['contract'])
            loaded = connections.validate_connection_record(self.piece, record)
            self.assertEqual(len(loaded['path_hashes_by_cell']), 12)
            self.assertEqual(set(loaded['movements']), set(independent.reviewed_facts(self.piece)['movements']))
            self.assertEqual(set(loaded['forbidden_transfers']),
                             set(independent.reviewed_facts(self.piece)['forbidden_transfers']))
            tile = self.piece['tile_ids'][0]
            key = f'path:{self.piece["id"]}:296678f7-a966883f-{tile}'
            changed = deepcopy(record); del changed['source']['resource_fingerprints'][key]
            with self.assertRaisesRegex(ValueError, 'canonical PATH bytes'):
                connections.validate_connection_record(self.piece, changed)
            changed = deepcopy(record); changed['source']['resource_fingerprints'][key] = sha(b'')
            with self.assertRaisesRegex(ValueError, 'canonical PATH bytes'):
                connections.validate_connection_record(self.piece, changed)

    def test_ground_rhw_and_intermediate_transition_are_explicit_and_do_not_change_avenue_classification(self):
        for height, variant in ((0.0, 'rhw-4-l0'), (7.5, 'dd-rhw-l1'), (15.0, 'dd-rhw-l2'),
                                (4.0, 'dd-rhw-ground-transition')):
            result = connections.service_classifier(self.piece, 1, height)
            self.assertEqual((result['service_network'], result['variant'], result['traffic_modes']),
                             ('road', variant, ['car']))
        self.assertEqual(connections.service_classifier({'recipe': 'highway_ddrhw_parallel_crossing'}, 1, 0.)['variant'],
                         'avenue-ground')


class OrthogonalConnectorFreezeTests(unittest.TestCase):
    mirrored = False

    @classmethod
    def setUpClass(cls):
        path = ROOT / 'domains/highway/tools/freeze_orthogonal_transition_connectors.py'
        spec = importlib.util.spec_from_file_location('_orthogonal_freezer_contract_test', path)
        cls.freezer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.freezer)

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.build = self.root / 'dist/synthetic-fixture'
        self.build.mkdir(parents=True)
        self.piece = source_piece(mirrored=self.mirrored)
        self.asset = 'managed/synthetic.dat'
        self.manifest = {'pieces': [{**self.piece, 'asset_file': self.asset}]}
        (self.build / 'manifest.json').write_text(json.dumps(self.manifest))
        self.resources = {(0x296678F7, 0xA966883F, int(tile, 16)): f'synthetic PATH bytes {index}'.encode()
                          for index, tile in enumerate(self.piece['tile_ids'])}
        destination = self.build / self.asset
        destination.parent.mkdir()
        destination.write_bytes(pack_dbpf(self.resources))
        self.facts = independent.reviewed_facts(self.piece)
        self.record = connection_record(self.piece, self.facts)
        self.destination = self.root / contracts.reference(self.piece)
        self.catalog_patcher = patch.object(self.freezer, 'load_catalog', return_value={'pieces': [self.piece]})
        self.catalog_patcher.start(); self.addCleanup(self.catalog_patcher.stop)
        self.verify_patcher = patch.object(self.freezer, 'verify_build', return_value={'static_checks_passed': True})
        self.verify = self.verify_patcher.start(); self.addCleanup(self.verify_patcher.stop)
        self.graph_patcher = patch.object(self.freezer, 'piece_connectivity', side_effect=lambda *args, **kwargs: deepcopy(self.record))
        self.graph = self.graph_patcher.start(); self.addCleanup(self.graph_patcher.stop)

    def freeze(self):
        return self.freezer.freeze(self.build, root=self.root, piece_id=self.piece['id'])

    def test_successful_synthetic_gate_binds_all_actual_fixture_bytes_and_writes_no_game_pass(self):
        result = self.freeze()
        self.verify.assert_called_once_with(self.build, write_report=False)
        self.assertEqual((result['ports'], result['journeys'], result['forbidden_transfers'], result['canonical_path_hashes']),
                         (8, 4, 12, 12))
        evidence = jsonc.load(self.destination)
        self.assertEqual(evidence['source']['manifest_sha256'], sha((self.build / 'manifest.json').read_bytes()))
        self.assertTrue(evidence['source']['verification_passed'])
        self.assertEqual(evidence['game_operation'], 'unverified')
        self.assertEqual(evidence['contract']['path_hashes_by_cell'], [[cell, sha(self.resources[
            0x296678F7, 0xA966883F, int(tile, 16)])] for cell, tile in zip(self.piece['cells'], self.piece['tile_ids'])])
        self.assertNotIn('synthetic PATH bytes', self.destination.read_text())
        loaded = contracts.load_contract(self.piece, self.root)
        self.assertEqual(len(loaded['path_hashes_by_cell']), 12)

    def test_failed_full_build_gate_never_extracts_or_overwrites_existing_evidence(self):
        self.destination.parent.mkdir(parents=True)
        self.destination.write_bytes(b'preserved prior accepted evidence')
        self.verify.side_effect = ValueError('synthetic full-build failure')
        with self.assertRaisesRegex(ValueError, 'synthetic full-build failure'):
            self.freeze()
        self.graph.assert_not_called()
        self.assertEqual(self.destination.read_bytes(), b'preserved prior accepted evidence')

    def test_saved_definition_must_match_current_source_before_verification(self):
        changed = deepcopy(self.manifest); changed['pieces'][0]['tile_ids'][0] = '7f000000'
        (self.build / 'manifest.json').write_text(json.dumps(changed))
        with self.assertRaisesRegex(ValueError, 'authoritative source'):
            self.freeze()
        self.verify.assert_not_called(); self.graph.assert_not_called()
        self.assertFalse(self.destination.exists())

    def test_all_eight_ports_must_be_present_once_without_duplicate_id_deduplication(self):
        original = deepcopy(self.record)
        for ports in (original['ports'][:-1], [*original['ports'], original['ports'][0]],
                      [*original['ports'][:-1], original['ports'][0]]):
            self.record = {**deepcopy(original), 'ports': ports}
            with self.subTest(port_count=len(ports)), self.assertRaisesRegex(ValueError, 'directional boundary'):
                self.freeze()
            self.assertFalse(self.destination.exists())

    def test_wrong_semantics_or_transfers_never_publish_a_hash_contract(self):
        original = deepcopy(self.record)
        mutations = []
        changed = deepcopy(original); changed['ports'][0]['endpoint_m'][0] += .1; mutations.append(changed)
        changed = deepcopy(original); changed['ports'][0]['variant'] = 'avenue-ground'; mutations.append(changed)
        changed = deepcopy(original); changed['ports'][0]['engine_transport'] = 2; mutations.append(changed)
        changed = deepcopy(original); changed['journeys'][0]['exit_port'] = 'lower-lane-01-out'; mutations.append(changed)
        changed = deepcopy(original); changed['journeys'].pop(); mutations.append(changed)
        changed = deepcopy(original); changed['forbidden_transfers'].pop(); mutations.append(changed)
        changed = deepcopy(original); changed['forbidden_transfers'][0] = deepcopy(changed['forbidden_transfers'][1]); mutations.append(changed)
        for index, record in enumerate(mutations):
            self.record = record
            with self.subTest(mutation=index), self.assertRaises(ValueError):
                self.freeze()
            self.assertFalse(self.destination.exists())

    def test_every_owned_cell_requires_a_real_saved_path_resource_before_publication(self):
        del self.resources[0x296678F7, 0xA966883F, int(self.piece['tile_ids'][0], 16)]
        (self.build / self.asset).write_bytes(pack_dbpf(self.resources))
        with self.assertRaises(KeyError):
            self.freeze()
        self.assertFalse(self.destination.exists())

    def test_freeze_rejects_a_build_outside_the_selected_library_root(self):
        with tempfile.TemporaryDirectory() as outside:
            with self.assertRaisesRegex(ValueError, 'inside the library'):
                self.freezer.freeze(Path(outside), root=self.root)
        self.verify.assert_not_called(); self.graph.assert_not_called()
        self.assertFalse(self.destination.exists())


class MirroredOrthogonalContractLoaderTests(OrthogonalContractLoaderTests):
    mirrored = True

    def test_missing_mirrored_evidence_cannot_fall_back_to_the_original_contract(self):
        original = self.root / contracts.REFERENCE
        original.parent.mkdir(parents=True)
        original.write_text(json.dumps(fixture_evidence(source_piece())))
        self.assertIsNone(contracts.load_contract(self.piece, self.root))
        self.assertNotEqual(contracts.REFERENCE, contracts.MIRRORED_REFERENCE)
        self.assertEqual(contracts.reference(self.piece), contracts.MIRRORED_REFERENCE)

    def test_original_frozen_semantics_cannot_be_copied_into_the_mirrored_reference(self):
        self.write(fixture_evidence(source_piece()))
        with self.assertRaisesRegex(ValueError, 'independent review'):
            contracts.load_contract(self.piece, self.root)

    def test_reference_selection_rejects_an_identity_variant_mismatch(self):
        changed = deepcopy(self.piece)
        changed.pop('transition_variant')
        with self.assertRaisesRegex(ValueError, 'identity.*variant'):
            contracts.reference(changed)


class MirroredOrthogonalConnectorFreezeTests(OrthogonalConnectorFreezeTests):
    mirrored = True


if __name__ == '__main__':
    unittest.main()
