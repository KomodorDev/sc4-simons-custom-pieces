"""Check corrected owners against accepted input PATHs, without native inputs."""
from copy import deepcopy
import hashlib
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]

from scp import jsonc
from scp.connectivity import PATH,piece_connectivity
from scp.connector_metadata import validate_piece
from scp_highway.connections import (connector_groups_value,reviewed_contract,reviewed_path_ports,
                                     service_classifier,validate_connection_record)
from scp_highway.modular_connector_contracts import (ACCEPTED_COMPACT_MANIFEST_SHA256,
    ACCEPTED_MANIFEST_SHA256,CONTRACTS,PATH_OWNERSHIP_REFERENCE,PATH_OWNERSHIP_REFERENCE_SHA256)


def encoded_cell(cell):
    """Recover accepted bytes using numeric evidence, not a resource writer."""
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
        raw = (ROOT/PATH_OWNERSHIP_REFERENCE).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == PATH_OWNERSHIP_REFERENCE_SHA256
        cls.evidence = jsonc.loads(raw.decode('utf-8'))
        assert cls.evidence['accepted_r40_manifest_sha256'] == ACCEPTED_MANIFEST_SHA256
        assert cls.evidence['accepted_compact_manifest_sha256'] == ACCEPTED_COMPACT_MANIFEST_SHA256
        cls.pieces,cls.resources,cls.records,cls.measurements = {},{},{},{}
        for saved in cls.evidence['pieces']:
            piece = jsonc.load(ROOT/saved['piece_source'])
            resources = {}
            for cell in saved['cells']:
                encoded = encoded_cell(cell)
                assert hashlib.sha256(encoded).hexdigest() == cell['path_sha256']
                resources[*PATH,int(cell['target_tile_id'],16)] = encoded
            record = piece_connectivity(piece,resources,contract=reviewed_contract(piece),
                                        service_classifier=service_classifier)
            cls.pieces[piece['recipe']],cls.resources[piece['recipe']] = piece,resources
            cls.records[piece['recipe']],cls.measurements[piece['recipe']] = record,saved

    def groups(self,recipe):
        return connector_groups_value(self.pieces[recipe],self.records[recipe],
                                      piece_sha256='1'*64,connections_sha256='2'*64)

    def test_pre_candidate_reference_has_complete_eleven_owner_services(self):
        self.assertFalse(self.evidence['scope']['candidate_resources_used'])
        self.assertFalse(self.evidence['scope']['corrected_build_pass_claimed'])
        self.assertFalse(self.evidence['scope']['physical_seam_or_game_pass_claimed'])
        totals = [0]*3
        for recipe,record in self.records.items():
            with self.subTest(recipe=recipe):
                validate_connection_record(self.pieces[recipe],record)
                groups = self.groups(recipe)
                totals = [a+b for a,b in zip(totals,(len(record['ports']),len(groups['channels']),
                                                    len(record['journeys'])))]
                self.assertEqual(record['software_status']['in_game'],'unverified')
                self.assertEqual(record['software_status']['physical_seams'],'unverified')
        self.assertEqual(len(self.records),11)
        self.assertEqual(totals,[80,38,44])
        self.assertEqual(sum(len(p['cells']) for p in self.measurements.values()),80)

    def test_current_definitions_preserve_literal_source_ownership_and_tile_ids(self):
        for recipe,saved in self.measurements.items():
            piece = self.pieces[recipe]
            with self.subTest(recipe=recipe):
                self.assertEqual(piece['footprint'],saved['footprint'])
                actual = {tuple(cell):tile for cell,tile in zip(piece['cells'],piece['tile_ids'])}
                self.assertEqual(actual,{tuple(c['cell']):c['target_tile_id'] for c in saved['cells']})
                for cell in saved['cells']:
                    self.assertEqual(cell['source_world_cell'],
                                     [a+b for a,b in zip(cell['cell'],saved['world_origin_cell'])])

    def test_all_boundaries_match_complete_independent_input_composition(self):
        for recipe,saved in self.measurements.items():
            record = self.records[recipe]
            for expected in saved['ports']:
                with self.subTest(recipe=recipe,port=expected['id']):
                    port = next(p for p in record['ports'] if p['id']==expected['id'])
                    for key in ('sampled_tangent','tangent'):
                        self.assertLessEqual(math.dist(port[key],expected[key]),1e-9)
                    for key in ('endpoint_m','grade','direction','engine_transport','edge',
                                'service_network','traffic_modes'):
                        self.assertEqual(port[key],expected[key])
                    self.assertEqual(port['boundary_sources'][0]['cell'],expected['source_cell'])
            self.assertEqual({(j['entry_port'],j['exit_port']) for j in record['journeys']},
                             {tuple(pair) for pair in saved['movements']})

    def test_straight_stamp_keeps_all_twenty_eight_traffic_cuts_and_native_services(self):
        recipe = 'highway_ddrhw_modular_stamp'
        record = self.records[recipe]
        self.assertEqual((len(self.pieces[recipe]['cells']),len(record['ports']),
                          len(record['journeys']),len(record['forbidden_transfers'])),(21,28,16,180))
        self.assertEqual(sum(p['engine_transport']==2 for p in record['ports']),4)
        self.assertEqual(sorted(p['grade'] for p in record['ports'] if p['grade']),
                         [-.226756787,.226756787])
        saved = self.measurements[recipe]
        # These six visual wing cells belong to separate ramp owners, not the stamp.
        wings = {(2,-3),(-3,2),(-2,4),(-3,5),(4,-2),(5,-3)}
        self.assertTrue(wings.isdisjoint(tuple(c['source_world_cell']) for c in saved['cells']))
        groups = self.groups(recipe)
        self.assertEqual(len(groups['channels']),14)
        self.assertEqual(sum(len(c['ports'])==3 for c in CONTRACTS[recipe]['channels']),2)

    def test_lower_full_visual_ramps_have_four_cuts_but_only_two_intrinsic_fragments(self):
        for recipe in CONTRACTS:
            if not any(f'lower_{flow}_' in recipe for flow in ('exit','entry')):
                continue
            record = self.records[recipe]
            groups = self.groups(recipe)
            with self.subTest(recipe=recipe):
                self.assertEqual((len(record['ports']),len(record['journeys']),
                                  len(record['forbidden_transfers'])),(4,2,2))
                self.assertEqual(len(groups['channels']),1)
                self.assertEqual(sum(len(g['members']) for g in groups['groups']),4)
                self.assertEqual({m['channel_id'] for g in groups['groups'] for m in g['members']},
                                 {'access-ramp-01'})
                forbidden = record['forbidden_transfers'][0]
                wrong = deepcopy(record)
                wrong['journeys'].append({'entry_port':forbidden['from_port'],
                                           'exit_port':forbidden['to_port']})
                with self.assertRaisesRegex(ValueError,'journeys'):
                    validate_connection_record(self.pieces[recipe],wrong)

    def test_path_validator_adapter_uses_measured_chords_and_returns_detached_lists(self):
        for recipe,piece in self.pieces.items():
            ports = reviewed_path_ports(piece)
            self.assertEqual(len(ports),len(CONTRACTS[recipe]['ports']))
            for actual,expected in zip(ports,CONTRACTS[recipe]['ports']):
                with self.subTest(recipe=recipe,port=expected['id']):
                    self.assertEqual(actual,{'direction':expected['direction'],
                        'transport':expected['engine_transport'],'point_m':expected['endpoint_m'],
                        'tangent':expected['sampled_tangent'],'grade':expected['grade'],
                        'source_cell':expected['source_cell'],'edge':expected['edge']})
            ports[0]['point_m'][0] += 1
            ports[0]['tangent'][0] += 1
            ports[0]['source_cell'][0] += 1
            self.assertEqual(reviewed_path_ports(piece)[0]['point_m'],CONTRACTS[recipe]['ports'][0]['endpoint_m'])
        with self.assertRaisesRegex(ValueError,'no complete reviewed'):
            reviewed_path_ports({'id':'unknown','recipe':'unreviewed'})

    def test_terminal_card_tangent_and_actual_circle_chord_remain_distinct(self):
        for recipe in CONTRACTS:
            if 'terminal' not in recipe:
                continue
            record = self.records[recipe]
            curves = [p for p in record['ports'] if math.dist(p['tangent'],p['sampled_tangent'])>.003]
            self.assertEqual(len(curves),2)
            for port in curves:
                angle = math.acos(max(-1.,min(1.,sum(a*b for a,b in zip(port['tangent'],port['sampled_tangent'])))))
                self.assertLessEqual(angle,.25/(2*40)+math.sqrt(2)*1e-6/.2+1e-8)
                self.assertEqual(port['grade'],0)
                wrong = deepcopy(record)
                next(p for p in wrong['ports'] if p['id']==port['id'])['sampled_tangent'] = port['tangent']
                with self.subTest(recipe=recipe,port=port['id']),self.assertRaisesRegex(ValueError,'tangent'):
                    validate_connection_record(self.pieces[recipe],wrong)

    def test_terminal_right_turns_cannot_move_to_the_other_carriageway(self):
        for recipe in CONTRACTS:
            if 'terminal' not in recipe:
                continue
            record = deepcopy(self.records[recipe])
            channel = next(c for c in CONTRACTS[recipe]['channels'] if c['id'].startswith('avenue-ramp'))
            movement = next(j for j in record['journeys'] if j['entry_port'] in channel['ports']
                            or j['exit_port'] in channel['ports'])
            old_exit = movement['exit_port']
            movement['exit_port'] = next(p['id'] for p in record['ports'] if p['direction']=='out'
                                         and p['engine_transport']==1 and p['id']!=old_exit)
            with self.subTest(recipe=recipe),self.assertRaisesRegex(ValueError,'journeys'):
                validate_connection_record(self.pieces[recipe],record)

    def test_canonical_input_bytes_reject_changed_wing_or_missing_bridge(self):
        for recipe,selector in (('highway_ddrhw_modular_lower_exit_r40',lambda c:c['source_world_cell']==[2,-3]),
                                ('highway_ddrhw_modular_stamp',lambda c:c['source_world_cell']==[2,-2])):
            saved = self.measurements[recipe]
            cell = next(c for c in saved['cells'] if selector(c))
            key = (*PATH,int(cell['target_tile_id'],16))
            for mutation in ('remove','foreign-wing'):
                resources = dict(self.resources[recipe])
                if mutation == 'remove':del resources[key]
                else:resources[key] = next(v for k,v in resources.items() if k!=key and v!=resources[key])
                with self.subTest(recipe=recipe,mutation=mutation),self.assertRaises((ValueError,KeyError)):
                    record = piece_connectivity(self.pieces[recipe],resources,contract=reviewed_contract(self.pieces[recipe]),
                                                service_classifier=service_classifier)
                    validate_connection_record(self.pieces[recipe],record)

    def test_serialized_height_transport_and_first_chord_mutations_are_rejected(self):
        recipe = 'highway_ddrhw_modular_lower_exit_r40'
        piece = self.pieces[recipe]
        key = next(k for k,v in self.resources[recipe].items() if b'-- SCP' in v)
        original = self.resources[recipe][key]
        for mutation in ('height','transport','sample'):
            resources = dict(self.resources[recipe]);lines = original.decode('ascii').splitlines()
            start = next(i for i,line in enumerate(lines) if line.startswith('-- SCP'))
            if mutation == 'transport':lines[start+1] = '2'
            else:
                point = lines[start+8].split(',');axis = 2 if mutation=='height' else 0
                point[axis] = str(float(point[axis])+.01);lines[start+8] = ','.join(point)
            resources[key] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
            with self.subTest(mutation=mutation),self.assertRaises((ValueError,KeyError)):
                record = piece_connectivity(piece,resources,contract=reviewed_contract(piece),
                                            service_classifier=service_classifier)
                validate_connection_record(piece,record)

    def test_signed_lower_stamp_bridge_grade_cannot_be_flattened_or_reversed(self):
        recipe = 'highway_ddrhw_modular_stamp'
        for mutation in (0.,-.226756787):
            record = deepcopy(self.records[recipe])
            next(p for p in record['ports'] if p['grade']>0)['grade'] = mutation
            with self.subTest(grade=mutation),self.assertRaisesRegex(ValueError,'grade'):
                validate_connection_record(self.pieces[recipe],record)

    def test_pedestrian_channel_ownership_and_owned_shape_are_explicit(self):
        recipe = 'highway_ddrhw_modular_northwest_terminal_r40'
        groups = self.groups(recipe)
        self.assertEqual(sum(c['kind']=='walkway' for c in groups['channels']),2)
        pedestrian = next(c for c in groups['channels'] if c['kind']=='walkway')
        pedestrian['component_id'] = 'avenue-mainline'
        with self.assertRaisesRegex(ValueError,'component'):
            validate_piece(self.pieces[recipe],self.records[recipe],groups,{})
        piece = deepcopy(self.pieces['highway_ddrhw_modular_lower_exit_compact'])
        piece['cells'][0] = [5,5]
        with self.assertRaisesRegex(ValueError,'owned cells'):
            reviewed_path_ports(piece)


if __name__ == '__main__':
    unittest.main()
