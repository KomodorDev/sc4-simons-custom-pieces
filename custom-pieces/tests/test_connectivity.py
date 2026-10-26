"""Saved-path metadata must preserve direction, service roles and exact joins."""
from copy import deepcopy
import json
import math
from pathlib import Path
import unittest
from unittest.mock import Mock, patch
from scp.connectivity import PATH, assembly_connectivity, catalog_connectivity, link_counterparts, piece_connectivity, rotate, orientation_states_from_rules
from scp_hsr.hsr_connections import service_classifier


def paths(routes):
    lines=['SC4PATHS','1.2',str(len(routes)),'0','0']
    for engine,entry,exit_,points in routes:
        lines += [str(engine),'0',str(entry),str(exit_),'0',str(len(points))]
        lines += [','.join(str(v) for v in point) for point in points]
    return ('\n'.join(lines)+'\n').encode()


def piece(identifier,recipe='fixture'):
    return {'id':identifier,'recipe':recipe,'footprint':[1,1],'cells':[[0,0]],'tile_ids':['7f500000']}


def paired(identifier='straight',height=15.5):
    spec=piece(identifier)
    resources={(*PATH,0x7f500000):paths([
        (7,3,1,[(2.,-8.,height),(2.,8.,height)]),
        (7,1,3,[(-2.,8.,height),(-2.,-8.,height)])])}
    contract={'ports':{'Sin':(2.,-8.,height),'Nout':(2.,8.,height),'Nin':(-2.,8.,height),'Sout':(-2.,-8.,height)},
              'port_vectors':{'Sin':(0.,1.),'Nout':(0.,1.),'Nin':(0.,-1.),'Sout':(0.,-1.)},
              'movements':[('Sin','Nout'),('Nin','Sout')]}
    return spec,piece_connectivity(spec,resources,contract=contract,service_classifier=service_classifier)


class ConnectivityTests(unittest.TestCase):
    def test_actual_clone_rules_distinguish_aliases_from_transposed_shapes(self):
        root=0xf700;sections={f'{root:08x}':[('CellLayout','0,0,0,0')]}
        for slot in range(1,8):
            fields=[('CopyFrom',hex(root+(slot-4)*65536 if slot>=4 else root))]
            if slot<4:fields.append(('Rotate',str(slot)))
            sections[f'{root+slot*65536:08x}']=fields
        normal=orientation_states_from_rules({'sections':sections},root)
        self.assertEqual(len(normal),4)
        self.assertFalse(any(state['construction_transposed'] for state in normal))
        self.assertTrue(all(len(state['construction_section_ids'])==2 for state in normal))
        sections[f'{root+4*65536:08x}']=[('CopyFrom',hex(root)),('Transpose','1')]
        for slot in range(5,8):
            sections[f'{root+slot*65536:08x}']=[('CopyFrom',hex(root+4*65536)),('Rotate',str(slot-4))]
        mirrored=orientation_states_from_rules({'sections':sections},root)
        self.assertEqual(len(mirrored),8)
        self.assertEqual([state['rotation_ccw_degrees'] for state in mirrored if state['construction_transposed']],[0,90,180,270])
        sections[f'{root+7*65536:08x}']=[('CopyFrom',hex(root+7*65536))]
        with self.assertRaisesRegex(ValueError,'Cyclic'):orientation_states_from_rules({'sections':sections},root)

    def test_actual_saved_paths_determine_direction_height_spacing_and_journeys(self):
        spec,record=paired()
        ports={port['id']:port for port in record['ports']}
        self.assertEqual(ports['Sin']['endpoint_m'],[2.,-8.,15.5])
        self.assertEqual(ports['Sin']['direction'],'in')
        self.assertEqual(ports['Sin']['lane_spacing_m'],4.)
        self.assertEqual(ports['Sin']['grade'],0.)
        self.assertEqual({(j['entry_port'],j['exit_port']) for j in record['journeys']},{('Sin','Nout'),('Nin','Sout')})
        self.assertEqual(len(record['forbidden_transfers']),2)
        self.assertEqual(record['software_status']['physical_seams'],'unverified')
        self.assertNotIn('/Users/',str(record))
        broken={**spec,'id':'changed'}
        contract={'ports':{'Sin':(2.,-8.,15.5),'Nout':(2.,8.,15.5)},'movements':[('Sin','Nout')]}
        with self.assertRaisesRegex(ValueError,'movements'):
            piece_connectivity(broken,{(*PATH,0x7f500000):paths([(7,3,1,[(2.,-8.,15.5),(2.,8.,15.5)]),(7,1,3,[(-2.,8.,15.5),(-2.,-8.,15.5)])])},contract=contract,service_classifier=service_classifier)

    def test_candidate_joins_preserve_directed_native_poses_and_disjoint_tile_ownership(self):
        spec,record=paired()
        linked=link_counterparts({'straight':record},{'straight':spec})['straight']
        north=next(port for port in linked['ports'] if port['id']=='Nout')
        self.assertTrue(north['compatible_counterparts'])
        for target in north['compatible_counterparts']:
            other=next(p for p in record['ports'] if p['id']==target['port_id'])
            endpoint=rotate(other['endpoint_m'],target['relative_rotation_ccw'])
            endpoint=[endpoint[0]+target['relative_position_m'][0],endpoint[1]+target['relative_position_m'][1],endpoint[2]]
            self.assertEqual(endpoint,north['endpoint_m'])
            self.assertNotEqual(target['relative_position_m'],[0.,0.])
            self.assertIn('unverified',target['status'])

    def test_custom_offcentre_curve_only_links_to_its_exact_matching_cut(self):
        first=piece('core');second=piece('curve');plain=piece('plain')
        vectors={'in':(1.,0.),'out':(.927254808965,-.374430927211)}
        a=piece_connectivity(first,{(*PATH,0x7f500000):paths([(7,0,3,[(-8.,-2.,15.5),(4.471264, -7.625569,15.5),(5.398519,-8.,15.5)])])},
            contract={'ports':{'in':(-8.,-2.,15.5),'out':(5.398519,-8.,15.5)},'port_vectors':vectors,'movements':[('in','out')]},service_classifier=service_classifier)
        b=piece_connectivity(second,{(*PATH,0x7f500000):paths([(7,1,3,[(5.398519,8.,15.5),(6.325774,7.625569,15.5),(0.,-8.,15.5)])])},
            contract={'ports':{'in':(5.398519,8.,15.5),'out':(0.,-8.,15.5)},'port_vectors':{'in':vectors['out'],'out':(0.,-1.)},'movements':[('in','out')]},service_classifier=service_classifier)
        _,c=paired('plain')
        linked=link_counterparts({'core':a,'curve':b,'plain':c},{'core':first,'curve':second,'plain':plain})
        out=next(port for port in linked['core']['ports'] if port['id']=='out')
        self.assertEqual([(x['piece_id'],x['port_id'],x['relative_rotation_ccw'],x['relative_position_m']) for x in out['compatible_counterparts']],
                         [('curve','in',0,[0.,-16.])])

    def test_tram_primary_and_udi_auxiliary_are_separate_from_hsr_and_heavy_rail(self):
        spec=piece('tram','tram_under_hsr');routes=[]
        for engine,height in ((3,0.),(6,0.),(7,15.5)):
            routes += [(engine,3,1,[(2.,-8.,height),(2.,8.,height)]),(engine,1,3,[(-2.,8.,height),(-2.,-8.,height)])]
        record=piece_connectivity(spec,{(*PATH,0x7f500000):paths(routes)},service_classifier=service_classifier)
        self.assertEqual(len(record['ports']),12);self.assertEqual(len(record['journeys']),6)
        self.assertEqual({(port['engine_transport'],port['service_network'],port['role']) for port in record['ports']},
                         {(3,'tram-udi','auxiliary'),(6,'tram','primary'),(7,'hsr','primary')})
        self.assertFalse(any('heavy-rail'==port['service_network'] for port in record['ports']))
        self.assertTrue(any(item['from_service']=='hsr' and item['to_service']=='tram' for item in record['forbidden_transfers']))

    def test_composed_assembly_keeps_two_way_graph_without_inventing_uturns(self):
        spec,record=paired()
        linked=link_counterparts({'straight':record},{'straight':spec})
        scene={'placements':[{'piece_id':'straight','origin_m':[0.,0.],'rotation_degrees_ccw':0},
                             {'piece_id':'straight','origin_m':[0.,16.],'rotation_degrees_ccw':0}],
               'external_ports':{'S':{'in':[2.,-8.,15.5],'out':[-2.,-8.,15.5]},'N':{'in':[-2.,24.,15.5],'out':[2.,24.,15.5]}}}
        assembly=assembly_connectivity('assembly',scene,linked,{'straight':spec})
        self.assertEqual(len(assembly['ports']),4)
        self.assertEqual({(j['entry_port'],j['exit_port']) for j in assembly['journeys']},{('S.in','N.out'),('N.in','S.out')})
        self.assertEqual(len(assembly['forbidden_transfers']),2)
        self.assertTrue(any(key.startswith('assembly_pose:') for key in assembly['source']['resource_fingerprints']))
        changed=deepcopy(scene);changed['placements'][1]['origin_m']=[0.,32.]
        with self.assertRaisesRegex(ValueError,'external ports'):
            assembly_connectivity('assembly',changed,linked,{'straight':spec})


class IntrinsicConnectivityTests(unittest.TestCase):
    def test_catalogue_extraction_is_independent_of_other_subjects_and_drafts(self):
        first, other, draft = piece('first'), piece('other'), {**piece('unfinished'), 'status': 'draft'}
        raw = {(*PATH, 0x7f500000): paths([
            (7, 3, 1, [(2., -8., 15.5), (2., 8., 15.5)]),
            (7, 1, 3, [(-2., 8., 15.5), (-2., -8., 15.5)])])}
        loader = Mock(return_value=raw)
        with patch('scp.connectivity.link_counterparts', side_effect=AssertionError('Intrinsic extraction must not match a catalogue')):
            alone = catalog_connectivity([first], loader, service_classifier=service_classifier)
            expanded = catalog_connectivity([other, draft, first], loader, service_classifier=service_classifier)
            reordered = catalog_connectivity([first, other], loader, service_classifier=service_classifier)
        self.assertEqual(alone['first'], expanded['first'])
        self.assertEqual(alone['first'], reordered['first'])
        self.assertNotIn('unfinished', expanded)
        self.assertNotIn(draft, [call.args[0] for call in loader.call_args_list])
        for port in alone['first']['ports']:
            self.assertTrue(port['connection_class'].startswith('path-interface-'))
            self.assertTrue(port['boundary_sources'])
            self.assertFalse({'compatible_counterparts', 'candidate_counterpart_count', 'counterpart_list_scope'} & port.keys())

    def test_old_candidate_limit_cannot_change_intrinsic_records(self):
        spec, _ = paired()
        resources = {(*PATH, 0x7f500000): paths([(7, 3, 1, [(0., -8., 15.5), (0., 8., 15.5)])])}
        with self.assertWarnsRegex(DeprecationWarning, 'ignored'):
            limited = catalog_connectivity([spec], lambda _: resources, max_candidates=1)
        self.assertEqual(limited, catalog_connectivity([spec], lambda _: resources))

    def test_saved_assembly_ignores_missing_truncated_and_poisoned_shortlists(self):
        first, a = paired('first')
        last, b = paired('z-required')
        scene = {'placements': [{'piece_id': first['id'], 'origin_m': [0., 0.]},
                                {'piece_id': last['id'], 'origin_m': [0., 16.]}]}
        plain = assembly_connectivity('line', scene, {'first': a, 'z-required': b}, {'first': first, 'z-required': last})
        specs, records = {'first': first, 'z-required': last}, {'first': a, 'z-required': b}
        for index in range(6):
            spec, record = paired('a-decoy-'+str(index))
            specs[spec['id']], records[spec['id']] = spec, record
        linked = link_counterparts(records, specs, max_candidates=1)
        north = next(port for port in linked['first']['ports'] if port['id'] == 'Nout')
        self.assertFalse(any(item['piece_id'] == 'z-required' for item in north['compatible_counterparts']))
        for record in linked.values():
            for port in record['ports']:
                port.pop('boundary_sources')  # Exercise cached legacy PATH-resource provenance.
                port['transposed_compatible_counterparts'] = [{'piece_id': 'not-registered', 'nonsense': object()}]
        original = deepcopy(linked)
        result = assembly_connectivity('line', scene, linked, specs)
        # Old caches lack this optional source provenance; their measured
        # geometry, journeys, and checked seams must still be identical.
        for port in plain['ports']:
            port.pop('boundary_sources')
        self.assertEqual(result, plain)
        # Deep equality cannot compare deepcopy(object()), so compare the
        # actual legacy suggestion lists and geometry separately.
        for identifier in linked:
            for before, after in zip(original[identifier]['ports'], linked[identifier]['ports']):
                self.assertEqual(before['endpoint_m'], after['endpoint_m'])
                self.assertEqual(before['compatible_counterparts'], after['compatible_counterparts'])
        self.assertEqual(len(result['journeys']), 2)
        self.assertEqual(len(result['encoded_route_joins']), 2)
        self.assertEqual(result['source']['scope'], 'encoded_route_graph_only')
        self.assertEqual(result['software_status']['complete_boundary_compatibility'], 'not_evaluated')

    def test_colocated_opposite_flows_do_not_disappear_or_create_a_uturn(self):
        spec = piece('bidirectional-channel')
        resources = {(*PATH, 0x7f500000): paths([
            (7, 3, 1, [(0., -8., 15.5), (0., 8., 15.5)]),
            (7, 1, 3, [(0., 8., 15.5), (0., -8., 15.5)])])}
        contract = {'ports': {'Sin': (0., -8., 15.5), 'Sout': (0., -8., 15.5),
                              'Nin': (0., 8., 15.5), 'Nout': (0., 8., 15.5)},
                    'port_vectors': {'Sin': (0., 1.), 'Sout': (0., -1.), 'Nin': (0., -1.), 'Nout': (0., 1.)},
                    'movements': [('Sin', 'Nout'), ('Nin', 'Sout')]}
        record = piece_connectivity(spec, resources, contract=contract, service_classifier=service_classifier)
        scene = {'placements': [{'piece_id': spec['id'], 'origin_m': [0., 0.]}],
                 'external_ports': {'S': {'in': [0., -8., 15.5], 'out': [0., -8., 15.5]},
                                    'N': {'in': [0., 8., 15.5], 'out': [0., 8., 15.5]}}}
        result = assembly_connectivity('bidirectional', scene, {spec['id']: record}, {spec['id']: spec})
        self.assertEqual(len(result['ports']), 4)
        self.assertEqual({(j['entry_port'], j['exit_port']) for j in result['journeys']},
                         {('S.in', 'N.out'), ('N.in', 'S.out')})
        self.assertEqual(len(result['forbidden_transfers']), 2)

    def test_matching_xyz_and_engine_cannot_join_different_services_or_channel_modes(self):
        first, a = paired('first')
        last, b = paired('last')
        scene = {'placements': [{'piece_id': 'first', 'origin_m': [0., 0.]},
                                {'piece_id': 'last', 'origin_m': [0., 16.]}]}
        for field, value in [('service_network', 'tram'), ('service_family', 'another-family'),
                             ('role', 'auxiliary'), ('channel_kind', 'road'), ('traffic_modes', ['pedestrian'])]:
            with self.subTest(field=field):
                altered = deepcopy(b)
                for port in altered['ports']:
                    port[field] = value
                result = assembly_connectivity('separate', scene, {'first': a, 'last': altered}, {'first': first, 'last': last})
                self.assertEqual(result['encoded_route_joins'], [])
                self.assertEqual(len(result['ports']), 8)
                self.assertEqual(len(result['journeys']), 4)
        # Local channel identities may differ across two pieces; actual kind
        # and mode agreement, rather than the spelling of the IDs, matters.
        records = {'first': deepcopy(a), 'last': deepcopy(b)}
        for identifier, record in records.items():
            for port in record['ports']:
                port.update(channel_kind='rail', traffic_modes=['monorail'], channel_id=identifier+'-track')
        joined = assembly_connectivity('line', scene, records, {'first': first, 'last': last})
        self.assertEqual(len(joined['encoded_route_joins']), 2)

    def test_tangent_grade_and_exact_height_are_checked_at_the_saved_seam(self):
        first, a = paired('first')
        last, b = paired('last')
        scene = {'placements': [{'piece_id': 'first', 'origin_m': [0., 0.]},
                                {'piece_id': 'last', 'origin_m': [0., 16.]}]}
        for alteration in ('heading', 'grade', 'height'):
            with self.subTest(alteration=alteration):
                changed = deepcopy(b)
                for port in changed['ports']:
                    if alteration == 'heading':
                        x, y = port['tangent'];theta = .01
                        port['tangent'] = [x*math.cos(theta)-y*math.sin(theta), x*math.sin(theta)+y*math.cos(theta)]
                    elif alteration == 'grade':port['grade'] += .01
                    else:port['endpoint_m'][2] += .00001
                result = assembly_connectivity('separate', scene, {'first': a, 'last': changed}, {'first': first, 'last': last})
                self.assertEqual(result['encoded_route_joins'], [])
                self.assertEqual(len(result['ports']), 8)
        # Positive slopes are compared in the recorded travel direction,
        # rather than negated merely because the tile edges face each other.
        records = {}
        for identifier, start, finish in [('first', 15., 16.), ('last', 16., 17.)]:
            resources = {(*PATH, 0x7f500000): paths([
                (7, 3, 1, [(2., -8., start), (2., 8., finish)]),
                (7, 1, 3, [(-2., 8., finish), (-2., -8., start)])])}
            records[identifier] = piece_connectivity(piece(identifier), resources, service_classifier=service_classifier)
        result = assembly_connectivity('graded', scene, records, {'first': first, 'last': last})
        self.assertEqual(len(result['encoded_route_joins']), 2)

    def test_owned_cells_source_edges_and_lattice_poses_are_checked(self):
        spec, record = paired()
        overlapping = {'placements': [{'piece_id': 'straight', 'origin_m': [0., 0.]},
                                      {'piece_id': 'straight', 'origin_m': [0., 0.]}]}
        with self.assertRaisesRegex(ValueError, 'overlap owned'):
            assembly_connectivity('bad', overlapping, {'straight': record}, {'straight': spec})
        shifted = deepcopy(overlapping);shifted['placements'][1]['origin_m'] = [0., 16.25]
        with self.assertRaisesRegex(ValueError, 'lattice'):
            assembly_connectivity('bad', shifted, {'straight': record}, {'straight': spec})
        corrupt = deepcopy(record)
        next(port for port in corrupt['ports'] if port['id'] == 'Sin')['edge'] = 1
        with self.assertRaisesRegex(ValueError, 'boundary sources'):
            assembly_connectivity('bad', {'placements': [overlapping['placements'][0]]}, {'straight': corrupt}, {'straight': spec})

    def test_rotated_port_edge_and_sampled_tangent_use_the_saved_world_pose(self):
        spec, record = paired()
        scene = {'placements': [{'piece_id': 'straight', 'origin_m': [0., 0.], 'rotation_degrees_ccw': 270}]}
        result = assembly_connectivity('turned', scene, {'straight': record}, {'straight': spec})
        port = next(port for port in result['ports'] if port['source_port_id'] == 'Sin')
        self.assertEqual(port['edge'], 0)
        self.assertEqual(port['tangent'], [1., -0.])
        self.assertEqual(port['sampled_tangent'], port['tangent'])

    def test_saved_trumpet_preserves_six_journeys_without_modifying_frozen_records(self):
        from scp.catalog import load_catalog
        root = Path(__file__).resolve().parents[1]
        directory = root/'domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4'
        scene_path = directory/'assembly.json'
        scene = json.loads(scene_path.read_text())
        specs = {spec['id']: spec for spec in load_catalog(root)['pieces']}
        identifiers = {item['piece_id'] for item in scene['placements']}
        files = {identifier: root/'domains/high-speed-rail/00_pieces'/identifier/'connections.json' for identifier in identifiers}
        before = {identifier: path.read_bytes() for identifier, path in files.items()}
        original = (directory/'connections.json').read_bytes()
        records = {identifier: json.loads(raw) for identifier, raw in before.items()}
        output = assembly_connectivity('straight-stem-trumpet-v4', scene, records, specs)
        self.assertEqual({(j['entry_port'], j['exit_port']) for j in output['journeys']},
                         {(a+'.in', b+'.out') for a in 'WES' for b in 'WES' if a != b})
        self.assertEqual(len(output['encoded_route_joins']), 50)
        self.assertEqual(original, (directory/'connections.json').read_bytes())
        self.assertEqual(before, {identifier: path.read_bytes() for identifier, path in files.items()})


if __name__=='__main__':unittest.main()

