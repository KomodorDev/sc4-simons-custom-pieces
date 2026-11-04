"""Road extraction keeps shared-engine channels and reviewed directions exact."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]

from scp.connectivity import piece_connectivity
from scp import jsonc,piece_menu_families
from scp.build import RUL0
from scp.dbpf import pack_dbpf
from scp.rul0 import compose_rul0
from scp.track_paths import PATH
from scp_highway import connections
from scp_highway.connections import CORE,reviewed_contract,service_classifier
from scp_highway.verify import CELLS,expected_paths
import test_ghsr_crossing_verify as alignment_a
import test_ghsr_crossing_phase_b_verify as alignment_b


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


class HighwayMenuFamilyExtractionTests(unittest.TestCase):
    def saved_pair(self,root):
        """Save two literal PATH fixtures behind an actual reversible menu family."""
        pieces = [jsonc.load(ROOT/'domains/highway/00_pieces'/identifier/'piece.jsonc') for identifier in
            ('ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg',
             'ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b')]
        fragments = []
        for piece in pieces:
            puzzle = int(piece['puzzle_id'],16)
            states = [puzzle+slot*0x10000 for slot in range(8)]
            lines = ['RotationRing = '+', '.join(f'{state:X}' for state in states),
                     f'[HighwayIntersectionInfo_0x{puzzle:08X}]','Costs = 1000']
            for slot,state in enumerate(states[1:],1):
                lines += [f'[HighwayIntersectionInfo_0x{state:08X}]',f'CopyFrom = 0x{puzzle:08X}',
                          f'Rotate = {slot%4}']
            fragments.append('\r\n'.join(lines)+'\r\n')
        native = b'[Ordering]\r\nRotationRing = 100, 10100\r\nAddTypes = 101, 10101\r\n'
        controller,composition = compose_rul0(native,fragments)
        menus = {(*prefix,int(piece['menu']['id'],16)): b'fixture presentation'
                 for piece in pieces for prefix in piece_menu_families.PREFIXES}
        controller,composition,_menus,record = piece_menu_families.apply(controller,composition,menus,pieces)
        folder = 'zzz_Simons_Custom_Pieces'
        build = root/'dist/family-pair'
        (build/folder/'20_Pieces').mkdir(parents=True)
        (build/folder/'00_SCP_Controller_NAM50.dat').write_bytes(pack_dbpf({RUL0:controller}))
        built = []
        for piece,fixture in zip(pieces,(alignment_a,alignment_b)):
            asset = folder+'/20_Pieces/SCP_'+piece['id']+'.dat'
            routes = fixture.fixture_routes()
            payload = {(*PATH,int(tile,16)):fixture.encode(records)
                       for tile,records in zip(piece['tile_ids'],routes)}
            (build/asset).write_bytes(pack_dbpf(payload))
            built.append({**piece,'asset_file':asset})
        manifest = {'plugin_folder':folder,'pieces':built,'overlay':{'rul0':composition},
                    piece_menu_families.KEY:record}
        (build/'manifest.json').write_text(json.dumps(manifest))
        return pieces,build,manifest,controller

    def extract(self,root,pieces,build):
        # The fixture isolates extraction after the normal build's independent
        # verification gate; the reversible menu and actual PATH readers run.
        with patch.object(connections,'load_catalog',return_value={'pieces':pieces}), \
             patch.object(connections,'verify_build',return_value={'status':'passed'}), \
             patch.object(connections,'reviewed_contract',return_value=None), \
             patch.object(connections,'_reviewed_facts',return_value=None), \
             patch.object(connections,'refresh_catalog_content',return_value={}) as refresh:
            result = connections.materialize(root,build=build,piece_ids=[piece['id'] for piece in pieces])
        return result,refresh.call_args.kwargs['records']

    def test_both_alignments_extract_their_own_paths_and_eight_construction_states_from_one_button(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            pieces,build,manifest,_controller = self.saved_pair(root)
            self.assertIn('AddTypes = F86F',manifest['overlay']['rul0']['ordering_insertion'])
            result,records = self.extract(root,pieces,build)
            self.assertEqual(result['extracted_piece_ids'],[piece['id'] for piece in pieces])
            for piece in pieces:
                record = records[piece['id']]
                self.assertEqual(len(record['journeys']),6)
                self.assertEqual(len(record['ports']),12)
                self.assertEqual([state['rotation_ccw_degrees'] for state in record['supported_orientations']],
                                 [0,90,180,270])
                actual = [section for state in record['supported_orientations']
                          for section in state['construction_section_ids']]
                expected = [f'{int(piece["puzzle_id"],16)+slot*0x10000:08x}' for slot in range(8)]
                self.assertEqual(sorted(actual),sorted(expected))
                self.assertIn('construction:'+piece['id'],record['source']['resource_fingerprints'])

    def test_a_foreign_addtypes_row_cannot_supply_extraction_orientation_evidence(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            pieces,build,manifest,controller = self.saved_pair(root)
            overlay = manifest['overlay']['rul0']
            original = overlay['ordering_insertion']
            forged = original.replace('AddTypes = F86F','AddTypes = FFFF')
            self.assertNotEqual(original,forged)
            overlay['ordering_insertion'] = forged
            (build/'manifest.json').write_text(json.dumps(manifest))
            path = build/manifest['plugin_folder']/'00_SCP_Controller_NAM50.dat'
            path.write_bytes(pack_dbpf({RUL0:controller.replace(original.encode(),forged.encode(),1)}))
            with self.assertRaisesRegex(ValueError,'unrelated rows, order, states, or keywords'):
                self.extract(root,pieces,build)


if __name__ == '__main__':
    unittest.main()
