"""Current saved-resource, connection, physical-safety and mutation controls.

These tests never open predecessor folders or copied baseline DATs. Integration
uses the current staged build; explicitly absent builds may skip that scope,
while stale or malformed present resources must fail. Game checks stay human.
"""
from copy import deepcopy
from functools import lru_cache
import json
import os
from pathlib import Path
import struct
import tempfile
import unittest

from scp.models import parse_s3d, pack_s3d
from scp.track_paths import encode_paths, _parse_paths
from scp.verification_fixtures import resource_descriptor, verification_resources
from scp_hsr.rail_feature_verify import _triangles
from scp_hsr.hsr_atomic_components_verify import (
    CONTRACTS, check_paths, audit_native_sections, audit_inherited_cap_model, audit_trumpet_visible_rails,
)
from scp_hsr_tools.verify_hsr_trumpet import (
    ROOT, SCENE, QUALITY_PATH, RESOURCES_PATH, REWORK_PATH, NEW_IDS, CURRENT_IDS, STRAIGHT_ID,
    ONEWAY_ID, REPLACEMENTS, audit_quality_contract, audit_approved_layout,
    load_build, world_tiles, audit_current_world_tiles, encoded_records,
    _journeys, CONTRACT, audit_current_journeys, verify, audit_candidate_ledger, audit_whole_route_quality,
)

from scp_hsr.hsr_trumpet_rework_verify import (
    read_rework_record, audit_redesign_scope, audit_target_joins, audit_preserved_journeys,
    prove_removed_structural_cells, _projected_tile_intersection_area, _tile_intersection_surface_area,
    ROUTE_MOVEMENT_POLICY, audit_route_movement, audit_recorded_route_movement,
    continuous_symmetric_distance, _directed_continuous_distance, audit_matching_route_movement,
)


@lru_cache(maxsize=1)
def saved_current():
    path = Path(os.environ.get('SCP_TRUMPET_BUILD', ROOT/'dist/straight-stem-trumpet'))
    checked = verification_resources(RESOURCES_PATH, path, selected_piece_ids=CURRENT_IDS,
                                     assembly_id='straight-stem-trumpet', required=False)
    if checked is None:
        raise unittest.SkipTest('Current actual staged build absent; no saved-resource claim made')
    build = load_build(checked)
    tiles, _ = world_tiles(json.loads(SCENE.read_text()), build)
    return build, tiles, resource_descriptor(RESOURCES_PATH)


class TrumpetLiteralContractTests(unittest.TestCase):
    def test_current_acceptance_has_no_predecessor_resource_dependency(self):
        self.assertFalse(audit_quality_contract()['predecessor_resource_inputs_required'])

    def test_relaxing_a_physical_limit_or_threshold_is_rejected(self):
        literal = json.loads(QUALITY_PATH.read_text())
        changes = {'candidate_eligibility_strictly_below_m': .01, 'encoded_fragments': literal['encoded_fragments']+1,
                   'minimum_clearance': 4., 'minimum_pier_spacing_m': 15.,
                   'actual_tile_triangles': literal['actual_tile_triangles']+1}
        for field, value in changes.items():
            candidate = deepcopy(literal); candidate[field] = value
            with tempfile.TemporaryDirectory() as temporary:
                path = Path(temporary)/'contract.json';path.write_text(json.dumps(candidate))
                with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'independent quality contract'):
                    audit_quality_contract(path)

    def test_outside_ports_are_independent_literals(self):
        literal = json.loads(QUALITY_PATH.read_text());literal['ports']['W_in'][0] += .01
        with tempfile.TemporaryDirectory() as temporary:
            path=Path(temporary)/'contract.json';path.write_text(json.dumps(literal))
            with self.assertRaisesRegex(ValueError, 'outside connections'):
                audit_quality_contract(path)

    def test_current_plan_preserves_approved_rectangle_grid_and_outside_ports(self):
        report=audit_approved_layout(json.loads(SCENE.read_text()))
        self.assertTrue(report['approved_external_ports_rectangle_and_grid'])
        self.assertEqual(report['reviewed_placements'],26)

    def test_a_moved_module_is_rejected(self):
        scene=json.loads(SCENE.read_text());scene['placements'][0]['origin_m'][0]+=16.
        with self.assertRaisesRegex(ValueError,'approved positions'):
            audit_approved_layout(scene)

    def test_a_reflection_cannot_replace_a_proper_rotation(self):
        scene=json.loads(SCENE.read_text());scene['placements'][0]['rotation_degrees_ccw']=45
        with self.assertRaisesRegex(ValueError,'proper cardinal rotation'):
            audit_approved_layout(scene)


class AuthorizedJunctionReworkControls(unittest.TestCase):
    def altered_record(self, change):
        record = json.loads(REWORK_PATH.read_text()); change(record)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary)/'junction-rework.json';path.write_text(json.dumps(record))
            return read_rework_record(path, root=ROOT, require_completed=False)

    def test_baseline_scope_needs_no_deleted_definition_or_dat(self):
        record = read_rework_record(REWORK_PATH, root=ROOT, require_completed=False)
        self.assertEqual(len(record['unchanged_world_cells']),85)
        self.assertEqual(len(record['unchanged_piece_archives']),11)
        self.assertEqual(len(record['allowed_world_cells_east_north_m']),24)
        self.assertFalse((ROOT/'domains/high-speed-rail/00_pieces/hsr-component-l2-compact-fan-diverge').exists())

    def test_expanding_the_change_region_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'authorized 24-cell'):
            self.altered_record(lambda record:record['allowed_world_cells_east_north_m'].append([192.,0.]))

    def test_rehashing_an_unchanged_baseline_cell_is_rejected(self):
        def change(record):record['unchanged_world_cells'][0]['resources_sha256']['path']='0'*64
        with self.assertRaisesRegex(ValueError,'unchanged 85-cell baseline'):self.altered_record(change)

    def test_changing_an_unchanged_type_hash_is_rejected(self):
        def change(record):record['unchanged_piece_archives'][0]['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'unchanged 11-type baseline'):self.altered_record(change)

    def test_socket_positions_and_headings_cannot_follow_a_changed_writer(self):
        for key in ('endpoint_m','travel_tangent'):
            with self.subTest(field=key),self.assertRaisesRegex(ValueError,'fixed target joins'):
                self.altered_record(lambda record:record['fixed_target_joins'][0][key].__setitem__(0,0.))

    def test_historical_replacement_geometry_binding_cannot_be_relabelled(self):
        def change(record):record['source_geometry']['hsr-component-l2-short-opposed-merge-core']['before_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'historical source binding'):self.altered_record(change)

    def test_unchanged_support_positions_cannot_move(self):
        def change(record):record['unchanged_support_positions_east_north_m'][0][0]+=.01
        with self.assertRaisesRegex(ValueError,'support plan'):self.altered_record(change)

    def test_a_different_structural_cell_cannot_be_removed(self):
        def change(record):record['removed_world_cells_east_north_m']=[[64.,16.],[144.,0.]]
        with self.assertRaisesRegex(ValueError,'unauthorized structural cell'):self.altered_record(change)

    def test_frozen_complete_northern_route_facts_cannot_be_rehashed(self):
        def change(record):
            record['baseline_reworked_journeys'][0]['points_east_north_height_m'][0][0]+=.001
        with self.assertRaisesRegex(ValueError,'frozen affected-route baseline'):self.altered_record(change)

    def test_independent_movement_envelope_cannot_be_relaxed(self):
        def change(record):record['route_movement_policy']['maximum_symmetric_continuous_distance_m']=6.01
        with self.assertRaisesRegex(ValueError,'independent route-movement envelope'):self.altered_record(change)

    def test_relaxing_any_whole_route_curvature_limit_is_rejected(self):
        for field,value in (('min_radius_m',23.),('max_curvature_change_per_m2',.002),
                            ('max_endpoint_curvature_per_m',.001)):
            literal=json.loads(QUALITY_PATH.read_text())
            literal['whole_route_quality']['per_movement']['E_in>S_out'][field]=value
            with tempfile.TemporaryDirectory() as temporary:
                path=Path(temporary)/'contract.json';path.write_text(json.dumps(literal))
                with self.subTest(field=field),self.assertRaisesRegex(ValueError,'complete route quality'):
                    audit_quality_contract(path)


class ContinuousRouteMovementControls(unittest.TestCase):
    def test_sub_guard_tolerance_cannot_create_nonterminating_subdivision(self):
        before=[(0.,0.,8.),(2.,0.,8.)];after=[(0.,1.,8.),(2.,1.,8.)]
        with self.assertRaisesRegex(ValueError,'guarded numerical range'):
            continuous_symmetric_distance(before,after,tolerance=1e-9)

    def test_segment_interior_is_measured_when_all_source_vertices_are_on_target(self):
        before=[(-1.,0.,0.),(1.,0.,0.)]
        after=[(-1.,0.,0.),(-1.,1.,0.),(1.,1.,0.),(1.,0.,0.)]
        measured=_directed_continuous_distance(before,after,tolerance=.0001)
        self.assertLessEqual(measured['lower_bound_m'],1.)
        self.assertGreaterEqual(measured['upper_bound_m'],1.)
        self.assertGreater(measured['lower_bound_m'],.9999)
        self.assertLessEqual(measured['upper_bound_m']-measured['lower_bound_m'],.0001)

    def test_identical_continuous_polylines_have_zero_movement(self):
        points=[(0.,0.,8.),(12.,5.,8.),(30.,0.,8.)]
        measured=continuous_symmetric_distance(points,points)
        self.assertEqual(measured['lower_bound_m'],0.)
        self.assertLessEqual(measured['upper_bound_m'],1e-8)

    def test_full_three_dimensional_separation_is_measured(self):
        before=[(0.,0.,8.),(2.,0.,8.)];after=[(0.,0.,14.01),(2.,0.,14.01)]
        measured=continuous_symmetric_distance(before,after)
        self.assertGreater(measured['lower_bound_m'],6.)
        routes=[{'movement':movement,**measured} for movement in ROUTE_MOVEMENT_POLICY['movements']]
        with self.assertRaisesRegex(ValueError,'independent 6.0 m'):
            audit_recorded_route_movement({'policy':ROUTE_MOVEMENT_POLICY,'journeys':routes})

    def test_rounding_differences_are_allowed_only_for_identical_encoded_geometry(self):
        original=json.loads(REWORK_PATH.read_text())['source_path_movement_preflight']['measurement']
        rounded=deepcopy(original)
        for item in rounded['journeys']:
            item['lower_bound_m']+=1e-12;item['upper_bound_m']+=1e-12
        rounded['maximum_lower_bound_m']+=1e-12;rounded['maximum_upper_bound_m']+=1e-12
        self.assertEqual(audit_matching_route_movement(rounded,original),rounded)
        rounded['journeys'][0]['current_points_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'compiled redesign proof'):
            audit_matching_route_movement(rounded,original)


class RemovedStructuralCellProjectionControls(unittest.TestCase):
    def setUp(self):
        from scp_hsr.test_support import donor
        self.record=json.loads(REWORK_PATH.read_text())
        self.spec={'id':'hsr-component-l2-paired-fan-compact-join','cells':[[3,0]],
                   'tile_ids':['7f580300'],'preview_id':'7f580ff5',
                   'component':{'support_centers':[[48.,0.]]}}
        self.model=donor()
        self.resources={(0x5ad0e817,0xbadb57f1,0x7f580300+zoom):self.model for zoom in range(5)}
        self.resources[0x5ad0e817,0xbadb57f1,0x7f580ff5]=self.shift(self.model,48.,0.)
        self.build={'pieces':{self.spec['id']:self.spec},'manifest_sha256':'1'*64,
                    'resources':lambda spec:{'sha256':'2'*64,'resources':self.resources}}

    @staticmethod
    def shift(raw,east,south):
        model=parse_s3d(raw)
        for block in model['vertices']:
            data=bytearray(block['data'])
            for offset in range(0,len(data),block['stride']):
                x,h,z=struct.unpack_from('<3f',data,offset)
                struct.pack_into('<3f',data,offset,x+east,h,z+south)
            block['data']=bytes(data)
        return pack_s3d(model)

    def prove(self):
        return prove_removed_structural_cells(self.build,self.record,root=ROOT)

    def test_exact_tile_borders_have_no_positive_open_area(self):
        self.assertEqual(_projected_tile_intersection_area([(-9.,0.),(-8.,0.),(-8.,1.)],(-8.,-8.,8.,8.)),0.)
        self.assertGreater(_projected_tile_intersection_area([(-9.,0.),(-7.,0.),(-7.,1.)],(-8.,-8.,8.,8.)),0.)

    def test_valid_saved_models_are_checked_in_all_five_zooms_and_preview(self):
        proof=self.prove()
        self.assertEqual(len(proof['cells']),4)
        self.assertEqual(len(proof['checked_model_resources']),6)
        self.assertEqual({x['zoom'] for x in proof['checked_model_resources']},{0,1,2,3,4})
        self.assertTrue(all(x['positive_area_intersections_by_zoom']==[0]*5 for x in proof['cells']))

    def test_any_saved_zoom_projection_inside_a_removed_cell_is_rejected(self):
        for zoom in range(5):
            with self.subTest(zoom=zoom):
                key=(0x5ad0e817,0xbadb57f1,0x7f580300+zoom)
                self.resources[key]=self.shift(self.model,-16.,32.)
                with self.assertRaisesRegex(ValueError,'projects.*removed structural cell'):self.prove()
                self.resources[key]=self.model

    def test_vertical_surface_inside_an_omitted_tile_cannot_hide_in_zero_plan_area(self):
        triangle=[(32.,14.,30.),(32.,17.,30.),(32.,14.,34.)]
        bounds=(24.,24.,40.,40.)
        self.assertEqual(_projected_tile_intersection_area([(x,z) for x,h,z in triangle],bounds),0.)
        self.assertGreater(_tile_intersection_surface_area(triangle,bounds),0.)
        self.assertEqual(_tile_intersection_surface_area([(24.,14.,30.),(24.,17.,30.),(24.,14.,34.)],bounds),0.)
        model=parse_s3d(self.model)
        for block in model['vertices']:
            data=bytearray(block['data'])
            for index,offset in enumerate(range(0,len(data),block['stride'])):
                x,h,z=triangle[index%3]
                struct.pack_into('<3f',data,offset,x-48.,h,z)
            block['data']=bytes(data)
        self.resources[0x5ad0e817,0xbadb57f1,0x7f580300]=pack_s3d(model)
        with self.assertRaisesRegex(ValueError,'surface inside removed structural cell'):self.prove()

    def test_complete_preview_projection_is_checked_separately(self):
        self.resources[0x5ad0e817,0xbadb57f1,0x7f580ff5]=self.shift(self.model,32.,32.)
        with self.assertRaisesRegex(ValueError,'projects.*removed structural cell'):self.prove()

    def test_hidden_path_resource_for_an_omitted_source_cell_is_rejected(self):
        self.resources[0x296678f7,0xa966883f,0x7f580220]=b'SC4PATHS\n1.2\n0\n0\n0\n'
        with self.assertRaisesRegex(ValueError,'retains an actual PATH resource'):self.prove()

    def test_an_owned_support_cannot_hide_in_an_omitted_cell(self):
        self.spec['component']['support_centers'].append([32.,-32.])
        with self.assertRaisesRegex(ValueError,'still owns a support'):self.prove()

    def test_unexpected_unmapped_saved_model_is_rejected(self):
        self.resources[0x5ad0e817,0xbadb57f1,0x7f580220]=self.model
        with self.assertRaisesRegex(ValueError,'unexpected model'):self.prove()


class EncodedWholeAssemblySourceControls(unittest.TestCase):
    """Clean clones can check encoded route geometry without native model inputs."""
    @classmethod
    def setUpClass(cls):
        from scp_hsr.hsr_components_layout import component_layout
        from scp_hsr.hsr_trumpet_verify import rotate,key
        scene=json.loads(SCENE.read_text());tiles={}
        for placement in scene['placements']:
            path=ROOT/'domains/high-speed-rail/00_pieces'/placement['piece_id']/'piece.json'
            spec=json.loads(path.read_text());layout=component_layout(spec['recipe'])
            turns=placement['rotation_degrees_ccw']//90
            for cell in spec['cells']:
                column,row=cell;x,north,_=rotate((column*16.,-row*16.,0.),turns)
                position=key((x+placement['origin_m'][0],north+placement['origin_m'][1],0.))[:2]
                if position in tiles:raise ValueError('Source assembly overlaps owned cells')
                routes=layout[tuple(cell)]['routes']
                raw=encode_paths(routes) if routes else b'SC4PATHS\n1.2\n0\n0\n0\n'
                tiles[position]={'resources':{'path':raw},'cell':tuple(cell),
                    'rotation':turns,'instance_id':placement['label']}
        cls.records=encoded_records(tiles);cls.journeys=_journeys(cls.records,CONTRACT)
        cls.rework=read_rework_record(REWORK_PATH,root=ROOT,require_completed=False)

    def test_all_six_complete_encoded_source_journeys_meet_global_limits(self):
        self.assertEqual(audit_whole_route_quality(self.journeys)['complete_journeys_checked'],6)

    def test_actual_encoded_source_sockets_use_independent_targets(self):
        self.assertEqual(len(audit_target_joins(self.records)['fixed_branch_joins_checked']),2)

    def test_mainlines_and_direct_slips_preserve_accepted_baseline_geometry(self):
        self.assertEqual(audit_preserved_journeys(self.journeys,self.rework)['unchanged_complete_journeys'],4)

    def test_complete_changed_northern_routes_stay_within_independent_six_metre_envelope(self):
        measured=audit_route_movement(self.journeys,self.rework)
        self.assertEqual(len(measured['journeys']),2)
        self.assertLessEqual(measured['maximum_upper_bound_m'],6.)


class AtomizationHistoryControls(unittest.TestCase):
    def changed_ledger(self,change):
        ledger=json.loads((SCENE.parent/'checks/atomization.json').read_text());change(ledger)
        with tempfile.TemporaryDirectory() as temporary:
            path=Path(temporary)/'atomization.json';path.write_text(json.dumps(ledger))
            return audit_candidate_ledger(path)

    def test_decisions_and_all_original_cell_reviews_remain_recorded(self):
        report=audit_candidate_ledger()
        self.assertEqual(report['original_owned_cells_reviewed'],51)
        self.assertEqual(len(report['eligible_atomized_candidates']),4)
        self.assertEqual(report['retained_candidates'],13)
        self.assertFalse(report['deleted_predecessor_resources_required'])

    def test_exactly_five_millimetres_is_ineligible(self):
        def change(ledger):ledger['candidates'][0]['original_path_deviation_m']=.005
        with self.assertRaisesRegex(ValueError,'strictly below'):self.changed_ledger(change)

    def test_an_extra_accepted_candidate_is_rejected(self):
        def change(ledger):next(c for c in ledger['candidates'] if c['id']=='p03b-west-tail')['decision']='atomized'
        with self.assertRaisesRegex(ValueError,'unauthorized candidate'):self.changed_ledger(change)

    def test_wrong_oneway_direction_is_rejected(self):
        def change(ledger):next(c for c in ledger['candidates'] if c['id']=='p01b-south-tail')['replacement']['straight_rotation_degrees']=0
        with self.assertRaisesRegex(ValueError,'native type or direction'):self.changed_ledger(change)

    def test_omitting_a_retained_owned_cell_is_rejected(self):
        def change(ledger):ledger['source_cell_inventory'].pop()
        with self.assertRaisesRegex(ValueError,'omits or repeats'):self.changed_ledger(change)

    def test_swapping_local_and_assembly_coordinates_is_rejected(self):
        def change(ledger):ledger['source_cell_inventory'][0]['assembly_xy']=[0,0]
        with self.assertRaisesRegex(ValueError,'local and assembly coordinates'):self.changed_ledger(change)

    def test_historical_measurements_cannot_silently_drift(self):
        def change(ledger):ledger['candidates'][0]['original_path_deviation_m']-=.000000001
        with self.assertRaisesRegex(ValueError,'frozen atomization measurements'):self.changed_ledger(change)

    def test_changed_replacement_geometry_stales_its_prior_decision(self):
        def change(ledger):ledger['candidates'][0]['replacement_geometry_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'stale for its changed replacement geometry'):self.changed_ledger(change)


class CurrentSavedResourceMutationControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build,cls.tiles,cls.descriptor=saved_current()
        cls.journeys=_journeys(encoded_records(cls.tiles),CONTRACT)

    def test_all_current_tile_resource_sets_are_frozen_exactly(self):
        report=audit_current_world_tiles(self.tiles,self.descriptor)
        self.assertEqual(report['strict_byte_identity_cells'],len(self.descriptor['world_cells']))
        self.assertEqual(report['tile_resource_fingerprints_checked'],len(self.descriptor['world_cells'])*11)

    def test_every_complete_current_journey_is_frozen(self):
        self.assertEqual(audit_current_journeys(self.journeys,self.descriptor)['complete_directed_journeys_frozen'],6)

    def test_any_unapproved_track_bend_change_is_rejected(self):
        changed=deepcopy(self.journeys);points=changed['E_in','S_out']
        index=next(i for i,p in enumerate(points) if p[2]==30.5);x,y,h=points[index]
        points[index]=(x+.000001,y,h)
        with self.assertRaisesRegex(ValueError,'complete encoded journey geometry changed'):
            audit_current_journeys(changed,self.descriptor)

    def test_previously_reworked_tiles_have_no_current_edit_exemption(self):
        changed=deepcopy(self.tiles);changed[-16.,-112.]['resources']['model_0']+=b'\0'
        with self.assertRaisesRegex(ValueError,'current saved tile resources changed'):
            audit_current_world_tiles(changed,self.descriptor)

    def test_even_a_shadow_only_change_is_rejected(self):
        changed=deepcopy(self.tiles);next(iter(changed.values()))['resources']['shadow_4']+=b'\0'
        with self.assertRaisesRegex(ValueError,'current saved tile resources changed'):
            audit_current_world_tiles(changed,self.descriptor)

    def test_orientation_change_cannot_pass_on_identical_saved_model_bytes(self):
        changed=deepcopy(self.tiles);next(iter(changed.values()))['rotation']=1
        with self.assertRaisesRegex(ValueError,'orientation changed'):
            audit_current_world_tiles(changed,self.descriptor)

    def test_actual_existing_paired_straight_passes_native_sections_but_widening_fails(self):
        tile=next(t for t in self.tiles.values() if t['piece_id']==STRAIGHT_ID)
        source=list(_triangles(parse_s3d(tile['resources']['model_0'])))
        triangles=[tuple((-south+16.*column,height,x,u,v) for x,height,south,u,v in tri)
                   for column in range(4) for tri in source]
        contract=CONTRACTS['hsr_component_l2_short_mainline_diverge_core']
        self.assertEqual(audit_native_sections(triangles,contract)['complete_native_join_sections_checked'],3)
        widened=[tuple((x,h,z*1.01,u,v) for x,h,z,u,v in tri) for tri in triangles]
        with self.assertRaisesRegex(ValueError,'native joining section differs'):
            audit_native_sections(widened,contract)


class CurrentRedesignSavedResourceControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build,cls.tiles,cls.descriptor=saved_current()
        cls.record=read_rework_record(REWORK_PATH,root=ROOT)
        cls.records=encoded_records(cls.tiles)
        cls.journeys=_journeys(cls.records,CONTRACT)

    def test_actual_candidate_preserves_all_unaffected_cells_and_types(self):
        report=audit_redesign_scope(self.tiles,self.build,self.record)
        self.assertEqual(report['unchanged_world_cells_preserved_byte_for_byte'],85)
        self.assertEqual(report['unchanged_type_archives_preserved_byte_for_byte'],11)

    def test_changed_resource_outside_redesign_scope_is_rejected(self):
        changed=deepcopy(self.tiles)
        position=tuple(self.record['unchanged_world_cells'][0]['world_east_north_m'])
        changed[position]['resources']['path']+=b'\n'
        with self.assertRaisesRegex(ValueError,'outside its authorized region'):
            audit_redesign_scope(changed,self.build,self.record)

    def test_both_independently_fixed_sockets_match_actual_saved_paths(self):
        self.assertEqual(len(audit_target_joins(self.records)['fixed_branch_joins_checked']),2)

    def test_a_shifted_actual_socket_is_rejected(self):
        changed=deepcopy(self.records)
        target=tuple(round(x,6) for x in self.record['fixed_target_joins'][0]['endpoint_m'])
        route=next(points for _,meta,points in changed if meta['instance_id']=='P06' and points[0]==target)
        route[0]=(route[0][0]+.001,route[0][1],route[0][2])
        with self.assertRaisesRegex(ValueError,'fixed directed target join'):audit_target_joins(changed)

    def test_both_mainlines_and_direct_slips_preserve_baseline_geometry(self):
        self.assertEqual(audit_preserved_journeys(self.journeys,self.record)['unchanged_complete_journeys'],4)

    def test_changed_direct_slip_bend_cannot_hide_behind_straight_normalization(self):
        changed=deepcopy(self.journeys)
        points=changed['W_in','S_out'];index=len(points)//2;x,north,height=points[index]
        points[index]=(x+.01,north,height)
        with self.assertRaisesRegex(ValueError,'preserved mainline or direct-slip'):
            audit_preserved_journeys(changed,self.record)

    def test_all_six_complete_journeys_meet_their_global_physical_limits(self):
        report=audit_whole_route_quality(self.journeys)
        self.assertEqual(report['complete_journeys_checked'],6)
        self.assertEqual(set(report['complete_journeys']),{'>'.join(x) for x in CONTRACT['movements']})

    def test_a_sharp_loop_bend_is_rejected_by_global_quality(self):
        changed=deepcopy(self.journeys)
        points=changed['E_in','S_out'];index=len(points)//2;x,north,height=points[index]
        points[index]=(x+1.,north,height)
        with self.assertRaisesRegex(ValueError,'kink|curve|curvature|turn|winding'):
            audit_whole_route_quality(changed)


class ActualTrumpetBuildIntegration(unittest.TestCase):
    def test_complete_saved_candidate(self):
        path=os.environ.get('SCP_TRUMPET_BUILD')
        if not path:self.skipTest('Set SCP_TRUMPET_BUILD to audit an actual staged current build')
        report=verify(Path(path))
        self.assertEqual(report['status'],'passed')
        self.assertEqual(report['geometry']['strict_byte_identity_cells'],len(resource_descriptor(RESOURCES_PATH)['world_cells']))
        self.assertEqual(len(report['encoded_paths']['proper_rotations']),4)
        self.assertEqual(report['supports']['total_column_positions'],74)
        self.assertEqual(report['supports']['unchanged_support_positions'],59)
        self.assertEqual(report['encoded_paths']['whole_route_quality']['complete_journeys_checked'],6)
        self.assertFalse(report['deleted_predecessor_resource_inputs_required'])


class EncodedTrumpetModuleTests(unittest.TestCase):
    def encoded(self, identifier):
        folder = ROOT/'domains/high-speed-rail/00_pieces'/identifier
        geometry = json.loads((folder/'geometry.json').read_text())
        info = geometry['metadata']
        spec = {k: info[k] for k in ('recipe', 'cells', 'footprint', 'structural_cells')}
        spec['tile_ids'] = [f'{0x7f000000+0x100*x+0x10*y:08x}' for x, y in spec['cells']]
        spec['preview_id'] = '7f000ff5'
        layout = {tuple(cell): data for cell, data in geometry['layout']}
        resources = {(0x296678F7, 0xA966883F, int(tile, 16)):
                     (encode_paths(layout[tuple(cell)]['routes']) if layout[tuple(cell)]['routes']
                      else b'SC4PATHS\n1.2\n0\n0\n0\n')
                     for cell, tile in zip(spec['cells'], spec['tile_ids'])}
        return spec, resources

    def test_all_four_sources_satisfy_literal_routing_and_curve_quality(self):
        for identifier in sorted(NEW_IDS):
            with self.subTest(identifier=identifier):
                spec, resources = self.encoded(identifier)
                report = check_paths(resources, spec)
                self.assertEqual(report['unique_complete_journeys_checked'], len(CONTRACTS[spec['recipe']]['movements']))

    def test_one_way_reversal_is_rejected(self):
        spec, resources = self.encoded('hsr-component-l2-shortened-return-curve')
        for key, raw in resources.items():
            if raw.splitlines()[2] == b'0':
                continue
            routes = _parse_paths(raw)
            for route in routes:
                route.update(role='branch', entry=route['exit'], exit=route['entry'],
                             points=list(reversed(route['points'])))
            resources[key] = encode_paths(routes)
        with self.assertRaisesRegex(ValueError, 'port|route|graph|movement|missing'):
            check_paths(resources, spec)

    def test_foreign_transport_is_rejected(self):
        spec, resources = self.encoded('hsr-component-l2-shortened-return-curve')
        key = next(k for k, raw in resources.items() if raw.splitlines()[2] != b'0')
        lines = resources[key].decode().splitlines()
        index = next(i+1 for i, line in enumerate(lines) if line.startswith('-- SCP_'))
        lines[index] = '6'
        resources[key] = ('\r\n'.join(lines)+'\r\n').encode()
        with self.assertRaisesRegex(ValueError, 'foreign transport'):
            check_paths(resources, spec)

    def test_extra_owned_tile_is_rejected(self):
        spec, resources = self.encoded('hsr-component-l2-shortened-return-curve')
        spec['cells'].append([0, 6])
        with self.assertRaisesRegex(ValueError, 'footprint differs'):
            check_paths(resources, spec)

    def test_one_way_height_change_is_rejected(self):
        spec, resources = self.encoded('hsr-component-l2-shortened-return-curve')
        key = next(k for k, raw in resources.items() if raw.splitlines()[2] != b'0')
        routes = _parse_paths(resources[key])
        for route in routes:
            route.update(role='branch', points=[(x, y, h+.01) for x, y, h in route['points']])
        resources[key] = encode_paths(routes)
        with self.assertRaisesRegex(ValueError, 'height range'):
            check_paths(resources, spec)



class InheritedCustomCutRailControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from scp_hsr.directional_t_verify import _world_triangles
        from scp_hsr.interchange_verify import _encoded_routes
        build, _, _ = saved_current()
        cls.inputs = []
        for identifier in ('hsr-component-l2-shortened-departure-curve',
                           'hsr-component-l2-shortened-return-curve'):
            spec = build['pieces'][identifier]
            resources = build['resources'](spec)['resources']
            contract = CONTRACTS[spec['recipe']]
            cls.inputs.append((spec, resources, list(_world_triangles(resources, spec, contract)),
                               _encoded_routes(resources, spec, contract), contract))
        neighbour = build['pieces']['hsr-component-l2-short-mainline-diverge-core']
        paths = _encoded_routes(build['resources'](neighbour)['resources'], neighbour,
                                CONTRACTS[neighbour['recipe']])
        cls.neighbour_paths = [(cell, meta, [(x-16., north+16., h) for x, north, h in points])
                              for cell, meta, points in paths]

    def rail_triangle(self, outward=1., transverse=-1.5):
        from scp_hsr.rail_feature_verify import _rail_u
        contract = self.inputs[0][-1]
        x, north, _ = contract['ports']['Win']
        vx, vy = contract['port_vectors']['Win']
        dx, dz = -vx, vy
        x, z = x+outward*dx-transverse*dz, -north+outward*dz+transverse*dx
        return tuple((x+a, 16.189326, z+b, _rail_u(-2.), .5)
                     for a, b in ((-.02, -.02), (.02, -.02), (0., .02)))

    def test_current_custom_cuts_require_the_literal_2_65m_mask(self):
        from scp_hsr.hsr_compact_fan_verify import audit_visible_rails_at_custom_cuts
        for _, _, triangles, records, contract in self.inputs:
            with self.subTest(port=contract['custom_curve_ports']), self.assertRaisesRegex(ValueError, 'stripe with no used train PATH'):
                audit_visible_rails_at_custom_cuts(triangles, records, contract)

    def test_both_frozen_current_models_pass_the_literal_mask(self):
        for spec, resources, triangles, records, contract in self.inputs:
            evidence = audit_inherited_cap_model(resources, spec, contract)
            report = audit_trumpet_visible_rails(triangles, records, contract)
            self.assertEqual(evidence['inherited_custom_cap_model_zooms_checked'], 5)
            self.assertEqual(report['inherited_custom_cap_depth_m'], 2.65)
            self.assertEqual(report['inherited_custom_cap_width_m'], 5.2)

    def test_even_one_changed_model_zoom_loses_the_inherited_exception(self):
        spec, resources, _, _, contract = self.inputs[0]
        resources = dict(resources)
        index = contract['cells'].index(contract['inherited_custom_cap']['cell'])
        key = (0x5AD0E817, 0xBADB57F1, int(spec['tile_ids'][index], 16)+4)
        resources[key] += b'\0'
        with self.assertRaisesRegex(ValueError, 'exact original port-tile model bytes'):
            audit_inherited_cap_model(resources, spec, contract)

    def test_actual_current_neighbour_paths_satisfy_the_strict_unclipped_audit(self):
        from scp_hsr.directional_t_verify import audit_visible_rails
        _, _, triangles, records, _ = self.inputs[0]
        report = audit_visible_rails(triangles, records+self.neighbour_paths)
        self.assertFalse(report['unused_visible_native_rails'])

    def test_interior_extra_rail_cannot_hide_in_the_outward_mask(self):
        _, _, triangles, records, contract = self.inputs[0]
        with self.assertRaisesRegex(ValueError, 'stripe with no used train PATH'):
            audit_trumpet_visible_rails([*triangles, self.rail_triangle(outward=-1.)], records, contract)

    def test_rail_beyond_the_literal_cap_depth_is_rejected(self):
        _, _, triangles, records, contract = self.inputs[0]
        with self.assertRaisesRegex(ValueError, 'stripe with no used train PATH'):
            audit_trumpet_visible_rails([*triangles, self.rail_triangle(outward=2.8)], records, contract)

    def test_rail_outside_the_existing_width_is_rejected(self):
        _, _, triangles, records, contract = self.inputs[0]
        with self.assertRaisesRegex(ValueError, 'stripe with no used train PATH'):
            audit_trumpet_visible_rails([*triangles, self.rail_triangle(transverse=-3.)], records, contract)

    def test_complete_actual_neighbour_check_still_rejects_an_unused_rail_inside_the_cap(self):
        from scp_hsr.directional_t_verify import audit_visible_rails
        _, _, triangles, records, contract = self.inputs[0]
        changed = [*triangles, self.rail_triangle()]
        audit_trumpet_visible_rails(changed, records, contract)
        with self.assertRaisesRegex(ValueError, 'stripe with no used train PATH'):
            audit_visible_rails(changed, records+self.neighbour_paths)



if __name__ == "__main__":
    unittest.main()
