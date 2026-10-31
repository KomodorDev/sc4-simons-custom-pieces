"""Check the complete modular kit against frozen decoded saved PATH evidence."""
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]

from scp import jsonc
from scp.connectivity import PATH,piece_connectivity
from scp.connector_metadata import validate_piece
from scp_highway.connections import (connector_groups_value,reviewed_contract,
                                     service_classifier,validate_connection_record)
from scp_highway.connector_contracts import CONTRACTS as RETAINED
from scp_highway.modular_connector_contracts import (ACCEPTED_MANIFEST_SHA256,CONTRACTS,
                                                    SAVED_PATH_EVIDENCE,SAVED_PATH_EVIDENCE_SHA256)


def encoded_cell(cell):
    """Reproduce the captured resource format without calling a resource writer."""
    lines = list(cell['header'])
    for route in cell['routes']:
        lines += route['comments']
        lines += [str(route[key]) for key in ('transport','lane','entry','exit','junction')]
        lines += [str(len(route['points_m_east_north_height']))]
        lines += [','.join(format(float(v),'.9f').rstrip('0').rstrip('.') if v else '0'
                           for v in point) for point in route['points_m_east_north_height']]
    return ('\r\n'.join(lines)+'\r\n').encode('ascii')


class ModularConnectorContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = (ROOT/SAVED_PATH_EVIDENCE).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == SAVED_PATH_EVIDENCE_SHA256
        cls.evidence = json.loads(raw)
        assert cls.evidence['build_manifest_sha256'] == ACCEPTED_MANIFEST_SHA256
        cls.pieces,cls.resources,cls.records,cls.measurements = {},{},{},{}
        for saved in cls.evidence['pieces']:
            piece = jsonc.load(ROOT/saved['piece_source'])
            resources = {}
            for cell in saved['cells']:
                encoded = encoded_cell(cell)
                assert hashlib.sha256(encoded).hexdigest() == cell['saved_path_sha256']
                resources[*PATH,int(cell['tile_id'],16)] = encoded
            record = piece_connectivity(piece,resources,contract=reviewed_contract(piece),
                                        service_classifier=service_classifier)
            cls.pieces[piece['recipe']],cls.resources[piece['recipe']] = piece,resources
            cls.records[piece['recipe']],cls.measurements[piece['recipe']] = record,saved

    def groups(self,recipe):
        return connector_groups_value(self.pieces[recipe],self.records[recipe],
                                      piece_sha256='1'*64,connections_sha256='2'*64)

    def test_actual_seven_owner_resources_have_complete_services_and_boundaries(self):
        totals = [0]*5
        for recipe,record in self.records.items():
            with self.subTest(recipe=recipe):
                validate_connection_record(self.pieces[recipe],record)
                groups = self.groups(recipe)
                totals = [a+b for a,b in zip(totals,(len(record['ports']),len(groups['channels']),
                    len(record['journeys']),len(groups['groups']),len(groups['boundary_bundles'])))]
                self.assertEqual(record['software_status']['in_game'],'unverified')
                self.assertEqual(record['software_status']['physical_seams'],'unverified')
        self.assertEqual(totals,[60,34,34,44,30])
        self.assertEqual(sum(len(p['cells']) for p in self.measurements.values()),62)

    def test_all_new_endpoints_match_preexisting_literal_cell_and_service_criteria(self):
        for recipe in CONTRACTS:
            ports = self.records[recipe]['ports']
            for expected in self.measurements[recipe]['independent_literal_endpoint_criteria']:
                with self.subTest(recipe=recipe,point=expected['point_m']):
                    matches = [port for port in ports if port['direction']==expected['direction']
                               and port['engine_transport']==expected['transport']
                               and math.dist(port['endpoint_m'],expected['point_m'])<2e-6]
                    self.assertEqual(len(matches),1)
                    self.assertEqual(matches[0]['boundary_sources'][0]['cell'],expected['source_cell'])
                    self.assertEqual(matches[0]['edge'],expected['edge'])

    def test_new_high_sockets_preserve_accepted_saved_grade_owner_first_chords(self):
        for recipe in CONTRACTS:
            if 'terminal' in recipe:
                continue
            old = RETAINED[recipe.replace('_modular_','_compact_').replace('_r40','_grade')]
            high = next(p for p in self.records[recipe]['ports'] if p['endpoint_m'][2]>0)
            expected = next(p for p in old['ports'] if p['direction']==high['direction'])
            with self.subTest(recipe=recipe):
                self.assertEqual(high['grade'],expected['grade'])
                self.assertLess(math.dist(high['sampled_tangent'],expected['sampled_tangent']),1e-9)
                ground = next(p for p in self.records[recipe]['ports'] if p['endpoint_m'][2]==0)
                self.assertEqual(ground['grade'],0)

    def test_terminal_card_tangent_and_measured_circle_chord_remain_distinct(self):
        for recipe in CONTRACTS:
            if 'terminal' not in recipe:
                continue
            record = self.records[recipe]
            for measure in self.measurements[recipe]['terminal_chord_heading_measurements']:
                port = next(p for p in record['ports'] if p['id']==measure['port_id'])
                with self.subTest(recipe=recipe,port=port['id']):
                    self.assertEqual(port['tangent'],measure['card_tangent'])
                    self.assertGreater(math.dist(port['tangent'],port['sampled_tangent']),.003)
                    self.assertLessEqual(measure['sampled_heading_deviation_radians'],
                                         measure['maximum_deviation_radians'])
                    wrong = deepcopy(record)
                    next(p for p in wrong['ports'] if p['id']==port['id'])['sampled_tangent'] = port['tangent']
                    with self.assertRaisesRegex(ValueError,'tangent'):
                        validate_connection_record(self.pieces[recipe],wrong)

    def test_terminal_right_turns_cannot_move_to_the_other_carriageway_or_lane(self):
        for recipe in CONTRACTS:
            if 'terminal' not in recipe:
                continue
            record = deepcopy(self.records[recipe])
            channels = CONTRACTS[recipe]['channels']
            ramp_in = next(c['ports'][0] for c in channels if c['id'].startswith('avenue-ramp')
                           and next(p for p in record['ports'] if p['id']==c['ports'][0])['direction']=='in')
            movement = next(j for j in record['journeys'] if j['entry_port']==ramp_in)
            old_exit = movement['exit_port']
            movement['exit_port'] = next(p['id'] for p in record['ports'] if p['direction']=='out'
                                         and p['engine_transport']==1 and p['id']!=old_exit)
            with self.subTest(recipe=recipe),self.assertRaisesRegex(ValueError,'journeys'):
                validate_connection_record(self.pieces[recipe],record)

    def test_serialized_height_transport_and_first_chord_mutations_are_rejected(self):
        recipe = 'highway_ddrhw_modular_lower_exit_r40'
        piece = self.pieces[recipe]
        key = next(k for k,v in self.resources[recipe].items() if b'-- SCP' in v)
        original = self.resources[recipe][key]
        for mutation in ('height','transport','sample','remove-canonical-cell'):
            resources = dict(self.resources[recipe])
            if mutation == 'remove-canonical-cell':
                del resources[key]
            else:
                lines = original.decode('ascii').splitlines()
                start = next(i for i,line in enumerate(lines) if line.startswith('-- SCP'))
                if mutation == 'transport':
                    lines[start+1] = '2'
                else:
                    point = lines[start+8].split(',')
                    axis = 2 if mutation=='height' else 0
                    point[axis] = str(float(point[axis])+.01)
                    lines[start+8] = ','.join(point)
                resources[key] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
            with self.subTest(mutation=mutation),self.assertRaises((ValueError,KeyError)):
                record = piece_connectivity(piece,resources,contract=reviewed_contract(piece),
                                            service_classifier=service_classifier)
                validate_connection_record(piece,record)

    def test_curve_declared_heading_or_signed_grade_cannot_be_relabelled(self):
        recipe = 'highway_ddrhw_modular_southeast_terminal_r40'
        measure = self.measurements[recipe]['terminal_chord_heading_measurements'][0]
        record = deepcopy(self.records[recipe])
        port = next(p for p in record['ports'] if p['id']==measure['port_id'])
        port['tangent'] = port['sampled_tangent']
        with self.assertRaisesRegex(ValueError,'tangent'):
            validate_connection_record(self.pieces[recipe],record)
        recipe = 'highway_ddrhw_modular_upper_entry_r40'
        record = deepcopy(self.records[recipe])
        next(p for p in record['ports'] if p['grade'])['grade'] *= -1
        with self.assertRaisesRegex(ValueError,'grade'):
            validate_connection_record(self.pieces[recipe],record)

    def test_pedestrian_permissions_and_channel_ownership_remain_explicit(self):
        recipe = 'highway_ddrhw_modular_northwest_terminal_r40'
        groups = self.groups(recipe)
        self.assertEqual(sum(c['kind']=='walkway' for c in groups['channels']),2)
        self.assertEqual(sum(c['id'].startswith('avenue-ramp') for c in groups['channels']),2)
        pedestrian = next(c for c in groups['channels'] if c['kind']=='walkway')
        pedestrian['component_id'] = 'avenue-mainline'
        with self.assertRaisesRegex(ValueError,'component'):
            validate_piece(self.pieces[recipe],self.records[recipe],groups,{})


if __name__ == '__main__':
    unittest.main()
