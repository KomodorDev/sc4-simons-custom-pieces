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
    ROOT, SCENE, QUALITY_PATH, RESOURCES_PATH, NEW_IDS, CURRENT_IDS, STRAIGHT_ID,
    ONEWAY_ID, REPLACEMENTS, audit_quality_contract, audit_approved_layout,
    load_build, world_tiles, audit_current_world_tiles, encoded_records,
    _journeys, CONTRACT, audit_current_journeys, verify, audit_candidate_ledger,
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
        changes = {'candidate_eligibility_strictly_below_m': .01, 'encoded_fragments': 168,
                   'minimum_clearance': 4., 'minimum_pier_spacing_m': 15., 'actual_tile_triangles': 659272}
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

    def test_all_109_current_tile_resource_sets_are_frozen_exactly(self):
        report=audit_current_world_tiles(self.tiles,self.descriptor)
        self.assertEqual(report['strict_byte_identity_cells'],109)
        self.assertEqual(report['tile_resource_fingerprints_checked'],1199)

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


class ActualTrumpetBuildIntegration(unittest.TestCase):
    def test_complete_saved_candidate(self):
        path=os.environ.get('SCP_TRUMPET_BUILD')
        if not path:self.skipTest('Set SCP_TRUMPET_BUILD to audit an actual staged current build')
        report=verify(Path(path))
        self.assertEqual(report['status'],'passed')
        self.assertEqual(report['geometry']['strict_byte_identity_cells'],109)
        self.assertEqual(len(report['encoded_paths']['proper_rotations']),4)
        self.assertEqual(report['supports']['total_column_positions_preserved'],75)
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
