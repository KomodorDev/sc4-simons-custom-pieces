"""Road extraction keeps shared-engine channels and reviewed directions exact."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]

from scp.connectivity import piece_connectivity
from scp.track_paths import PATH
from scp_highway.connections import CORE,reviewed_contract,service_classifier
from scp_highway.verify import CELLS,expected_paths


def fixture():
    piece = {'id':'literal-native-crossing-fixture','recipe':CORE,'domain':'highway',
             'footprint':[3,3],'cells':[list(cell) for cell in CELLS],
             'tile_ids':[f'{0x5F900000+256*cell[0]+16*cell[1]:08x}' for cell in CELLS]}
    resources = {}
    for identifier,routes in zip(piece['tile_ids'],expected_paths()):
        lines = ['SC4PATHS','1.2',str(len(routes)),'0','0']
        for route in routes:
            lines += [str(route[key]) for key in ('transport','lane','entry','exit','compatibility')]
            lines += [str(len(route['points']))]
            lines += [','.join(str(value) for value in point) for point in route['points']]
        resources[*PATH,int(identifier,16)] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
    return piece,resources


class HighwayConnectionTests(unittest.TestCase):
    def setUp(self):
        self.piece,self.resources = fixture()

    def test_real_car_engine_has_consistent_seam_service_with_explicit_variants(self):
        expected = ((0.,'avenue-ground'),(7.5,'dd-rhw-l1'),(15.,'dd-rhw-l2'),(4.,'access-ramp'))
        for height,variant in expected:
            with self.subTest(height=height):
                result = service_classifier(self.piece,1,height)
                self.assertEqual((result['service_network'],result['service_family']),('road','road'))
                self.assertEqual(result['variant'],variant)
                self.assertEqual(result['traffic_modes'],['car'])
                self.assertEqual(result['channel_kind'],'road-lane')
        self.assertEqual(service_classifier(self.piece,2,0.)['service_network'],'pedestrian')
        self.assertEqual(service_classifier(self.piece,7,15.)['role'],'unresolved')

    def test_literal_crossing_extracts_all_lanes_and_both_pedestrian_channels(self):
        contract = reviewed_contract(self.piece)
        record = piece_connectivity(self.piece,self.resources,contract=contract,service_classifier=service_classifier)
        self.assertEqual(len(record['ports']),20)
        self.assertEqual(len(record['journeys']),10)
        self.assertEqual({p['id'] for p in record['ports']},set(contract['ports']))
        self.assertEqual({(j['entry_port'],j['exit_port']) for j in record['journeys']},
                         set(map(tuple,contract['movements'])))
        self.assertEqual(sum(j['engine_transport_classes'] == [2] for j in record['journeys']),2)
        self.assertEqual(record['software_status']['physical_seams'],'unverified')
        self.assertEqual(record['software_status']['in_game'],'unverified')
        self.assertNotIn('compatible_counterparts',record['ports'][0])

    def test_reviewed_port_transport_and_direction_cannot_be_guessed_from_position(self):
        original = reviewed_contract(self.piece)
        name = next(iter(original['ports']))
        for field,value in (('port_transports',2),('port_directions','out')):
            contract = deepcopy(original)
            contract[field][name] = value
            with self.subTest(field=field),self.assertRaisesRegex(ValueError,'reviewed transport and direction contract'):
                piece_connectivity(self.piece,self.resources,contract=contract,service_classifier=service_classifier)

    def test_coincident_same_direction_same_transport_labels_are_rejected_as_ambiguous(self):
        contract = reviewed_contract(self.piece)
        name = next(iter(contract['ports']))
        for field in ('ports','port_vectors','port_transports','port_directions'):
            contract[field]['duplicate-label'] = deepcopy(contract[field][name])
        with self.assertRaisesRegex(ValueError,'ambiguous external port labels'):
            piece_connectivity(self.piece,self.resources,contract=contract,service_classifier=service_classifier)

    def test_unreviewed_ramp_boundary_uses_measured_ports_without_a_native_contract_claim(self):
        piece = {**self.piece,'recipe':'highway_future_unreviewed_ramp'}
        self.assertIsNone(reviewed_contract(piece))
        record = piece_connectivity(piece,self.resources,contract=None,service_classifier=service_classifier)
        self.assertFalse(record['source']['reviewed_contract_available'])
        self.assertEqual(record['software_status']['contract_consistency'],'unverified')


if __name__ == '__main__':
    unittest.main()
