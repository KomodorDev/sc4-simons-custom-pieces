"""Reopen the independently frozen saved PATH evidence without native inputs."""
from copy import deepcopy
import hashlib
import json
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
from scp_highway.connector_contracts import (ACCEPTED_MANIFEST_SHA256,CONTRACTS,
                                            SAVED_PATH_EVIDENCE_SHA256)

ASSEMBLY = ROOT/'domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond'


def saved_cells():
    """Recover exact saved bytes from the frozen public decoder's numeric rows.

    This test-local serialization neither calls a geometry writer nor evaluates
    its route formula. Every resulting byte string must match the independently
    captured original SHA before it is supplied to the extraction engine.
    """
    raw = (ASSEMBLY/'evidence/ramp-atomization-saved-paths.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SAVED_PATH_EVIDENCE_SHA256
    evidence = json.loads(raw)
    assert evidence['build_manifest_sha256'] == ACCEPTED_MANIFEST_SHA256
    routes = {row['id']:row for row in evidence['routes']}
    cells = {}
    for cell in evidence['cells']:
        lines = ['SC4PATHS','1.2',str(len(cell['route_ids'])),'0','0']
        east,north = cell['centre_assembly_world_m_EN']
        for route_id in cell['route_ids']:
            route = routes[route_id]
            points = [(x-east,y-north,h) for x,y,h in route['points_assembly_world_m_ENH']]
            lines += [route['saved_comment'],str(route['transport']),str(route['encoded_lane_class']),
                      str(route['entry_local_WNES']),str(route['exit_local_WNES']),
                      str(route['encoded_junction_flag']),str(len(points))]
            lines += [','.join(format(float(v),'.9f').rstrip('0').rstrip('.') if v else '0'
                               for v in point) for point in points]
        encoded = ('\r\n'.join(lines)+'\r\n').encode('ascii')
        assert hashlib.sha256(encoded).hexdigest() == cell['path_sha256']
        cells[cell['piece_id'],cell['path_tgi'].split('-')[-1]] = encoded
    return cells


class CompactConnectorContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = saved_cells()
        cls.pieces,cls.records = {},{}
        for recipe,facts in CONTRACTS.items():
            piece = jsonc.load(ROOT/'domains/highway/00_pieces'/facts['reference_piece_id']/'piece.jsonc')
            resources = {(*PATH,int(tile,16)):cls.saved[piece['id'],tile] for tile in piece['tile_ids']}
            record = piece_connectivity(piece,resources,contract=reviewed_contract(piece),
                                        service_classifier=service_classifier)
            cls.pieces[recipe],cls.records[recipe] = piece,record

    def groups(self,recipe,record=None):
        piece = self.pieces[recipe]
        return connector_groups_value(piece,record or self.records[recipe],
                                      piece_sha256='1'*64,connections_sha256='2'*64)

    def test_every_retained_boundary_is_extracted_from_exact_saved_bytes(self):
        totals = [0,0,0,0]
        for recipe,facts in CONTRACTS.items():
            with self.subTest(recipe=recipe):
                record = self.records[recipe]
                validate_connection_record(self.pieces[recipe],record)
                groups = self.groups(recipe)
                self.assertTrue(record['source']['reviewed_contract_available'])
                self.assertEqual(record['software_status']['physical_seams'],'unverified')
                self.assertEqual(record['software_status']['in_game'],'unverified')
                self.assertEqual({p['id'] for p in record['ports']},
                                 {m['source_port_id'] for g in groups['groups'] for m in g['members']})
                totals = [a+b for a,b in zip(totals,(len(record['ports']),len(groups['channels']),
                                                   len(groups['groups']),len(groups['boundary_bundles'])))]
        self.assertEqual(totals,[140,74,84,50])

    def test_signed_grades_and_actual_tangents_are_affirmative_contracts(self):
        recipe = 'highway_ddrhw_compact_lower_exit_grade'
        for field,value in (('grade',0.0),('grade',.226761428),('sampled_tangent',[0.,-1.]),
                            ('tangent',[0.,-1.])):
            record = deepcopy(self.records[recipe]);record['ports'][0][field] = value
            with self.subTest(field=field,value=value),self.assertRaisesRegex(ValueError,'grade|tangent'):
                validate_connection_record(self.pieces[recipe],record)

    def test_service_boundary_and_raw_path_identity_cannot_be_inferred(self):
        recipe = 'highway_ddrhw_compact_access_core'
        original = self.records[recipe]
        for mutation in ('missing-port','wrong-engine','wrong-service','wrong-cell','moved-point','changed-path'):
            record = deepcopy(original);port = record['ports'][0]
            if mutation == 'missing-port':record['ports'].pop()
            elif mutation == 'wrong-engine':port['engine_transport'] = 2
            elif mutation == 'wrong-service':port['service_network'] = 'pedestrian'
            elif mutation == 'wrong-cell':port['boundary_sources'][0]['cell'] = [1,1]
            elif mutation == 'moved-point':port['endpoint_m'][0] += .001
            else:
                key = next(k for k in record['source']['resource_fingerprints'] if k.startswith('path:'))
                record['source']['resource_fingerprints'][key] = '0'*64
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):
                validate_connection_record(self.pieces[recipe],record)

    def test_journey_and_forbidden_transfer_sets_are_both_complete(self):
        recipe = 'highway_ddrhw_compact_lower_exit_branch'
        for mutation in ('missing-journey','invented-journey','missing-forbidden'):
            record = deepcopy(self.records[recipe])
            if mutation == 'missing-journey':record['journeys'].pop()
            elif mutation == 'invented-journey':
                record['journeys'][0]['exit_port'] = record['forbidden_transfers'][0]['to_port']
                record['journeys'][0]['entry_port'] = record['forbidden_transfers'][0]['from_port']
            else:record['forbidden_transfers'].pop()
            with self.subTest(mutation=mutation),self.assertRaisesRegex(ValueError,'journeys|forbidden'):
                validate_connection_record(self.pieces[recipe],record)

    def test_serialized_saved_path_endpoint_flow_and_grade_mutations_fail(self):
        recipe = 'highway_ddrhw_compact_lower_exit_grade'
        piece = self.pieces[recipe]
        original = {(*PATH,int(tile,16)):self.saved[piece['id'],tile] for tile in piece['tile_ids']}
        key = next(k for k,v in original.items() if b'-- SCP' in v)
        for mutation in ('height','transport','flow'):
            resources = dict(original);lines = original[key].decode('ascii').splitlines()
            start = next(i for i,line in enumerate(lines) if line.startswith('-- SCP'))
            if mutation == 'height':
                point = lines[start+8].split(',');point[2] = str(float(point[2])+.01)
                lines[start+8] = ','.join(point)
            elif mutation == 'transport':lines[start+1] = '2'
            else:lines[start+3],lines[start+4] = lines[start+4],lines[start+3]
            resources[key] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):
                record = piece_connectivity(piece,resources,contract=reviewed_contract(piece),
                                            service_classifier=service_classifier)
                validate_connection_record(piece,record)

    def test_known_recipe_with_different_owned_shape_cannot_fall_back_to_unreviewed(self):
        piece = deepcopy(self.pieces['highway_ddrhw_compact_lower_exit_grade'])
        piece['cells'][0] = [5,5]
        with self.assertRaisesRegex(ValueError,'owned cells'):
            reviewed_contract(piece)

    def test_two_native_fragments_and_branch_channel_are_not_collapsed(self):
        recipe = 'highway_ddrhw_compact_lower_exit_branch'
        groups = self.groups(recipe)
        self.assertEqual(sum(c['id'].startswith(('lower-lane','upper-lane')) for c in groups['channels']),8)
        self.assertEqual(sum(c['id'].startswith('lower-ramp') for c in groups['channels']),1)
        member = next(m for g in groups['groups'] for m in g['members'] if m['source_port_id']=='1-W-out-1')
        self.assertEqual(member['channel_id'],'lower-ramp-01')
        groups['channels'][-1]['component_id'] = 'upper-mainline'
        with self.assertRaisesRegex(ValueError,'component'):
            validate_piece(self.pieces[recipe],self.records[recipe],groups,{})


if __name__ == '__main__':
    unittest.main()
