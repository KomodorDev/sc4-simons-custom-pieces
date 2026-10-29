"""Pinned resource, source-revision, connection, and mutation controls.

The exact audited assembly fixture retains its historical resource contract.
Later standalone repairs are source-only revisions, with their own preserved
snapshots. Explicit integration uses a current staged build; absent builds may
skip that scope, while stale or malformed resources fail. Game checks stay human.
"""
from copy import deepcopy
from contextlib import contextmanager
from functools import lru_cache
import hashlib
import json
import os
import shutil
from pathlib import Path
import struct
import tempfile
import unittest
from unittest.mock import patch

from scp import jsonc
from scp.models import parse_s3d, pack_s3d
from scp.track_paths import encode_paths, _parse_paths
from scp.verification_fixtures import resource_descriptor, verification_resources
from scp.subject_sources import piece_directory
from scp_hsr.rail_feature_verify import _triangles
from scp_hsr.hsr_atomic_components_verify import (
    CONTRACTS, check_paths, audit_native_sections, audit_inherited_cap_model, audit_trumpet_visible_rails,
)
from scp_hsr_tools.verify_hsr_trumpet import (
    ROOT, SCENE, QUALITY_PATH, RESOURCES_PATH, REWORK_PATH, HISTORICAL_RESOURCES_PATH, NEW_IDS, CURRENT_IDS, STRAIGHT_ID,
    ONEWAY_ID, REPLACEMENTS, audit_quality_contract as _audit_quality_contract,
    audit_approved_layout as _audit_approved_layout,
    load_build, world_tiles, audit_current_world_tiles, encoded_records,
    _journeys, CONTRACT, audit_current_journeys, verify,
    audit_candidate_ledger as _audit_candidate_ledger, audit_whole_route_quality,
    audit_subsequent_piece_revisions as _audit_subsequent_piece_revisions, read_frozen_rework_record,
)

from scp_hsr.hsr_trumpet_rework_verify import (
    read_rework_record, audit_redesign_scope, audit_target_joins, audit_preserved_journeys,
    prove_removed_structural_cells, _projected_tile_intersection_area, _tile_intersection_surface_area,
    ROUTE_MOVEMENT_POLICY, audit_route_movement, audit_recorded_route_movement,
    continuous_symmetric_distance, _directed_continuous_distance, audit_matching_route_movement,
)


@lru_cache(maxsize=1)
def historical_recipes():
    """Use this proof's own pinned manifest, never a subject-ID crosswalk."""
    from scp_hsr.hsr_trumpet_border_verify import frozen_inputs, CORE_IDENTITY, STRAIGHT_IDENTITY
    pieces = frozen_inputs()['manifest']['pieces'] + [CORE_IDENTITY, STRAIGHT_IDENTITY]
    return {piece['id']: piece['recipe'] for piece in pieces}


def piece_folder(identifier, root=ROOT):
    historical = Path(root)/'domains/high-speed-rail/00_pieces'/identifier
    if Path(root) != ROOT or historical.is_dir():
        return historical
    return piece_directory(historical_recipes()[identifier], ROOT)


def current_piece_source(relative, root=ROOT):
    """Copy retained source bytes into tests of their original historical paths.

    Only this test fixture locates surviving source by the recipe in its own
    immutable manifest. Production selection never accepts the archived ID.
    Temporary roots deliberately reconstruct the original proof's layout.
    """
    parts = Path(relative).parts
    if len(parts) >= 5 and parts[0] == 'domains' and parts[2] == '00_pieces':
        return piece_folder(parts[3], root).joinpath(*parts[4:])
    return Path(root)/relative


def historical_scene():
    from scp_hsr.hsr_trumpet_border_verify import frozen_inputs, expected_current_placements
    scene = json.loads(SCENE.read_text())
    scene['placements'] = expected_current_placements(frozen_inputs())
    return scene


def audit_quality_contract(*args, **kwargs):
    """Exercise the unchanged historical physical policy under its original ID."""
    with patch('scp_hsr_tools.verify_hsr_trumpet.CURRENT_ASSEMBLY_ID', 'straight-stem-trumpet'):
        return _audit_quality_contract(*args, **kwargs)


def audit_approved_layout(*args, **kwargs):
    """Exercise the exact historical layout; current callers remain strict."""
    with patch('scp_hsr_tools.verify_hsr_trumpet.CURRENT_ASSEMBLY_ID', 'straight-stem-trumpet'):
        return _audit_approved_layout(*args, **kwargs)


def copy_historical_revisions(root, ledger):
    """Reconstruct only the byte-pinned historical source-chain test inputs."""
    for revision in ledger['subsequent_piece_revisions']:
        if revision['piece_id'] == 'hsr-component-l2-paired-fan-compact-join':
            continue
        original = current_piece_source(revision['source_file'])
        source = current_piece_source(revision['source_file'], root)
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_bytes(original.read_bytes())
        for relative in revision['standalone_evidence']:
            target = source.parent/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((original.parent/relative).read_bytes())
        prior = revision.get('superseded_attempt', revision.get('before_piece_snapshot'))
        original_snapshot = original.parent/prior['snapshot_directory']
        snapshot = source.parent/prior['snapshot_directory']
        files = json.loads((original_snapshot/'index.json').read_text())['files']
        relatives = list(files) if isinstance(files, dict) else [
            item.get('snapshot_file', item.get('path')) for item in files]
        for relative in ['index.json', *relatives]:
            target = snapshot/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((original_snapshot/relative).read_bytes())


@lru_cache(maxsize=1)
def historical_source_fixture():
    temporary = tempfile.TemporaryDirectory()
    root = Path(temporary.name)
    ledger = json.loads((SCENE.parent/'checks/atomization.json').read_text())
    copy_historical_revisions(root, ledger)
    # Two unchanged atomization sources have no later standalone revision.
    for candidate in ledger['candidates']:
        if candidate['decision'] != 'atomized':
            continue
        identifier = candidate['replacement']['new_core_piece_id']
        target = piece_folder(identifier, root)/'geometry.json'
        if not target.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((piece_folder(identifier)/'geometry.json').read_bytes())
    return temporary


@contextmanager
def independent_retirement_fixture():
    """Isolate geometry/ledger unit controls from separately tested stale names.

    The production retirement reader correctly rejects renamed manifest bytes.
    These unit controls use the unchanged historical decision as their supplied
    dependency; all geometry, source-chain, evidence, and hash checks still run.
    No file or source pin is rebound by this fixture.
    """
    record = json.loads((SCENE.parent/'checks/fan-parent-retirement.json').read_text())
    with patch('scp_hsr_tools.verify_hsr_trumpet.audit_parent_retirement', return_value=record):
        yield


def audit_candidate_ledger(*args, **kwargs):
    root = Path(historical_source_fixture().name)
    with independent_retirement_fixture(), patch('scp_hsr_tools.verify_hsr_trumpet.ROOT', root), patch(
            'scp_hsr_tools.verify_hsr_trumpet.audit_subsequent_piece_revisions',
            lambda ledger: _audit_subsequent_piece_revisions(ledger, root=root)):
        return _audit_candidate_ledger(*args, **kwargs)


def audit_subsequent_piece_revisions(*args, **kwargs):
    if kwargs.get('root', ROOT) == ROOT:
        kwargs['root'] = Path(historical_source_fixture().name)
    with independent_retirement_fixture():
        return _audit_subsequent_piece_revisions(*args, **kwargs)


@lru_cache(maxsize=1)
def saved_current():
    if not (SCENE.parent/'checks/border-piece-integration.json').is_file():
        raise unittest.SkipTest('Current fan integration has no completed capture; historical fixture is audited separately')
    path = Path(os.environ.get('SCP_TRUMPET_BUILD', ROOT/'dist/trumpet-fan-core-parts-audit-01'))
    descriptor = resource_descriptor(RESOURCES_PATH)
    if descriptor['assembly_id'] == 'straight-stem-trumpet':
        from scp_hsr.hsr_trumpet_border_verify import PRESERVED_INTEGRATION_FILES
        if hashlib.sha256(RESOURCES_PATH.read_bytes()).hexdigest() != PRESERVED_INTEGRATION_FILES['checks/resources.json']:
            raise ValueError('Historical assembly resource descriptor bytes changed')
        raise unittest.SkipTest('Renamed assembly has no current-ID resource capture; unchanged historical proof is preserved separately')
    checked = verification_resources(RESOURCES_PATH, path, selected_piece_ids=CURRENT_IDS,
                                     assembly_id='hsr-trumpet-straight-stem', required=False)
    if checked is None:
        raise unittest.SkipTest('Current actual staged build absent; no saved-resource claim made')
    build = load_build(checked)
    tiles, _ = world_tiles(json.loads(SCENE.read_text()), build)
    return build, tiles, resource_descriptor(RESOURCES_PATH)


@lru_cache(maxsize=1)
def saved_historical():
    path = Path(os.environ.get('SCP_TRUMPET_HISTORICAL_BUILD', ROOT/'dist/straight-stem-trumpet'))
    descriptor = resource_descriptor(HISTORICAL_RESOURCES_PATH)
    identifiers = {item['id'] for item in descriptor['pieces']}
    checked = verification_resources(HISTORICAL_RESOURCES_PATH, path, selected_piece_ids=identifiers,
                                     assembly_id='straight-stem-trumpet', required=False)
    if checked is None:
        raise unittest.SkipTest('Historical actual staged build absent; no saved-resource claim made')
    build = load_build(checked)
    scene = json.loads((HISTORICAL_RESOURCES_PATH.parent.parent/'assembly.json').read_text())
    tiles, _ = world_tiles(scene, build)
    return build, tiles, descriptor


def copy_retirement_inputs(root):
    """Copy retained proofs for mutation tests, never retired parent sources."""
    from scp_hsr import hsr_trumpet_border_verify as current
    paths = []
    paths.extend(ROOT/'domains/high-speed-rail'/relative for relative in ('domain.jsonc','collections.jsonc'))
    paths.extend(SCENE.parent/relative for relative in (
        current.PARENT_RETIREMENT_RELATIVE, 'checks/atomization.json', *current.PRESERVED_INTEGRATION_FILES))
    for source in paths:
        target=root/source.relative_to(ROOT)
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
    for identifier, inputs in ((current.CORE_ID,current.CORE_SOURCE_INPUTS),
                               (current.STRAIGHT_ID,current.STRAIGHT_SOURCE_INPUTS)):
        for relative in {**inputs, **current.EXTRACTED_STANDALONE_EVIDENCE[identifier]}:
            target = piece_folder(identifier, root)/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(piece_folder(identifier)/relative, target)


def synthetic_retirement_manifests(case, root):
    """Supply fictional manifests for isolated byte-mutation controls only.

    The tiny temporary files are deliberately not current authoring sources.
    Their fixture-only pins and retirement decision exist only inside this
    test. Real renamed source bytes remain stale under the original pins.
    """
    from scp_hsr import hsr_trumpet_border_verify as current
    for field, identifier in (('CORE_SOURCE_INPUTS', current.CORE_ID),
                              ('STRAIGHT_SOURCE_INPUTS', current.STRAIGHT_ID)):
        path = piece_folder(identifier, root)/'piece.json'
        raw = (json.dumps({'fixture': 'Synthetic retirement manifest', 'id': identifier})+'\n').encode()
        path.write_bytes(raw)
        pins = deepcopy(getattr(current, field))
        pins['piece.json'] = hashlib.sha256(raw).hexdigest()
        case.enterContext(patch.object(current, field, pins))
    raw = (json.dumps(current.parent_retirement_record(), indent=2)+'\n').encode()
    (root/SCENE.parent.relative_to(ROOT)/current.PARENT_RETIREMENT_RELATIVE).write_bytes(raw)
    case.enterContext(patch.object(current, 'PARENT_RETIREMENT_SHA256', hashlib.sha256(raw).hexdigest()))


class TrumpetLiteralContractTests(unittest.TestCase):
    def test_historical_acceptance_has_no_predecessor_resource_dependency(self):
        self.assertFalse(audit_quality_contract()['predecessor_resource_inputs_required'])

    def test_current_identity_rejects_the_unchanged_historical_acceptance(self):
        with self.assertRaisesRegex(ValueError, 'independent quality contract'):
            _audit_quality_contract()
        with self.assertRaisesRegex(ValueError, 'reviewed layout record changed'):
            _audit_approved_layout(json.loads(SCENE.read_text()))
        with self.assertRaisesRegex(ValueError, 'descriptor assembly identity differs'):
            verification_resources(RESOURCES_PATH, ROOT/'dist/absent-current-fixture',
                                   selected_piece_ids=CURRENT_IDS, assembly_id='hsr-trumpet-straight-stem',
                                   required=False)

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

    def test_historical_plan_preserves_approved_rectangle_grid_and_outside_ports(self):
        report=audit_approved_layout(historical_scene())
        self.assertTrue(report['approved_external_ports_rectangle_and_grid'])
        self.assertEqual(report['reviewed_placements'],28)

    def test_a_moved_module_is_rejected(self):
        scene=historical_scene();scene['placements'][0]['origin_m'][0]+=16.
        with self.assertRaisesRegex(ValueError,'approved positions'):
            audit_approved_layout(scene)

    def test_a_reflection_cannot_replace_a_proper_rotation(self):
        scene=historical_scene();scene['placements'][0]['rotation_degrees_ccw']=45
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

    def test_frozen_completed_audit_retains_its_original_source_bindings(self):
        record=read_frozen_rework_record()
        self.assertEqual(record['source_geometry']['hsr-component-l2-paired-fan-compact-join']['after_sha256'],
                         'd034aa453bfa95fb3a537736d12a40d0be427cbe59baffebf8f73424c7f7a090')
        self.assertEqual(record['source_geometry']['hsr-component-l2-short-opposed-merge-core']['after_sha256'],
                         '8bf5a7e8439a29017cc2d556695552ae98d0be9eaf4e550e6505a9ef30c6f7f8')

    def test_relabelling_a_completed_historical_record_is_rejected(self):
        original=REWORK_PATH.read_bytes()
        with tempfile.TemporaryDirectory() as temporary:
            path=Path(temporary)/'junction-rework.json'
            path.write_bytes(original+b'\n')
            with self.assertRaisesRegex(ValueError,'frozen completed redesign record fingerprint'):
                read_frozen_rework_record(path)

    def test_standalone_repairs_do_not_satisfy_the_completed_current_source_check(self):
        with self.assertRaisesRegex(ValueError,'current geometry differs'):
            read_rework_record(REWORK_PATH,root=ROOT)

    def test_each_later_reworked_piece_fails_the_strict_completed_current_reader(self):
        from scp_hsr import hsr_trumpet_rework_verify as rework_verify
        ledger=json.loads((SCENE.parent/'checks/atomization.json').read_text())
        originals={}
        for item in ledger['subsequent_piece_revisions']:
            originals.setdefault(item['piece_id'],item)
        identifiers=('hsr-component-l2-short-opposed-merge-core',)
        for changed_identifier in identifiers:
            with self.subTest(piece=changed_identifier),tempfile.TemporaryDirectory() as temporary:
                root=Path(temporary)
                for identifier in identifiers:
                    revision=originals[identifier]
                    current=current_piece_source(revision['source_file'], ROOT)
                    previous=current.parent/revision['before_piece_snapshot']['snapshot_directory']/'geometry.json'
                    self.assertEqual(hashlib.sha256(previous.read_bytes()).hexdigest(),
                                     read_frozen_rework_record()['source_geometry'][identifier]['after_sha256'])
                    target=current_piece_source(revision['source_file'], root)
                    target.parent.mkdir(parents=True)
                    target.write_bytes((current if identifier==changed_identifier else previous).read_bytes())
                # Check the retained source first so the separate missing
                # retired parent cannot satisfy this mutation control.
                ordered={identifier:rework_verify.REWORKED_SOURCES[identifier]
                         for identifier in (changed_identifier,'hsr-component-l2-paired-fan-compact-join')}
                with patch.object(rework_verify,'REWORKED_SOURCES',ordered):
                    with self.assertRaisesRegex(ValueError,'independently audited source'):
                        read_rework_record(REWORK_PATH,root=root)
                    (current_piece_source(originals[changed_identifier]['source_file'], root)).write_bytes(previous.read_bytes())
                    with self.assertRaisesRegex(ValueError,'historical source is no longer active'):
                        read_rework_record(REWORK_PATH,root=root)

    def test_retired_parent_is_not_recreated_to_replay_historical_source(self):
        from scp_hsr.hsr_trumpet_border_verify import FULL_FAN_ID,audit_parent_retirement
        self.assertFalse((ROOT/'domains/high-speed-rail/00_pieces'/FULL_FAN_ID).exists())
        record=json.loads((SCENE.parent/'checks/fan-parent-retirement.json').read_text())
        self.assertFalse(record['historical_source_replay_available_for_retired_piece'])
        with self.assertRaisesRegex(ValueError, 'retained source or extraction proof'):
            audit_parent_retirement()
        with self.assertRaisesRegex(ValueError,'historical source is no longer active'):
            read_rework_record(REWORK_PATH,root=ROOT)

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
        self.temporary=tempfile.TemporaryDirectory();self.addCleanup(self.temporary.cleanup)
        self.root=Path(self.temporary.name)
        source=self.root/'domains/high-speed-rail/00_pieces'/self.spec['id']/'geometry.json'
        source.parent.mkdir(parents=True)
        source.write_text('{"purpose":"Synthetic saved-model projection fixture, not a retired authoring source."}')

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
        return prove_removed_structural_cells(self.build,self.record,root=self.root)

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
            path=piece_folder(placement['piece_id'])/'piece.json'
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

    def test_all_six_atomized_source_journeys_preserve_exact_continuous_geometry(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_current_journey_geometry
        self.assertEqual(audit_current_journey_geometry(self.journeys)['complete_directed_journey_geometries_preserved'],6)

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
        self.assertFalse(report['current_assembly_resource_audit_claimed_by_this_ledger_check'])
        self.assertEqual([item['piece_id'] for item in report['subsequent_piece_revisions']],
                         ['hsr-component-l2-short-mainline-diverge-core',
                          'hsr-component-modular-south-junction',
                          'hsr-component-l2-paired-fan-compact-join',
                          'hsr-component-l2-short-opposed-merge-core',
                          'hsr-component-l2-short-mainline-diverge-core',
                          'hsr-component-modular-south-junction',
                          'hsr-component-l2-short-opposed-merge-core'])
        for item in report['subsequent_piece_revisions']:
            self.assertEqual(item['status'],'standalone-verified/assembly-integration-deferred')
            self.assertFalse(item['assembly_resource_pins_refreshed'])
            self.assertFalse(item['assembly_render_refreshed'])
        revision=report['subsequent_piece_revisions'][0]
        self.assertEqual(revision['status'],'standalone-verified/assembly-integration-deferred')
        self.assertFalse(revision['assembly_resource_pins_refreshed'])
        self.assertFalse(revision['assembly_render_refreshed'])
        self.assertEqual(revision['south_parapet_alignment']['left_inner_half_width_m'],2.6)
        self.assertEqual(revision['south_parapet_alignment']['right_local_east_cap_m'],43.776078282276934)
        self.assertEqual(revision['superseded_attempt']['status'],
                         'software-checked/superseded-after-border-shape-clarification')
        candidate=report['eligible_atomized_candidates']['p01a-west-tail']
        self.assertEqual(candidate['historical_replacement_geometry_sha256'],
                         '7760cdba90db6e0b12959708faf677121a0f5913edae65ef83d524006004baa0')
        self.assertTrue(candidate['historical_source_superseded_by_standalone_piece_revision'])
        self.assertFalse(candidate['historical_source_superseded_by_explicit_redesign'])

    def test_the_four_prior_standalone_revision_dictionaries_remain_frozen(self):
        ledger=json.loads((SCENE.parent/'checks/atomization.json').read_text())
        encoded=json.dumps(ledger['subsequent_piece_revisions'][:4],sort_keys=True,separators=(',',':')).encode()
        self.assertEqual(hashlib.sha256(encoded).hexdigest(),
                         '0cf73a7aaf81eb75722ba2a2910651eca0366918da8ab34fe1fa21eccad40bec')

    def test_the_five_accepted_standalone_revision_dictionaries_remain_frozen(self):
        ledger=json.loads((SCENE.parent/'checks/atomization.json').read_text())
        encoded=json.dumps(ledger['subsequent_piece_revisions'][:5],sort_keys=True,separators=(',',':')).encode()
        self.assertEqual(hashlib.sha256(encoded).hexdigest(),
                         '678b99a35bb7c4d4f3a81362f1ae371c04898ef9a397ff2d7bbf7189e4fb88fd')

    def test_the_six_accepted_standalone_revision_dictionaries_remain_frozen(self):
        ledger=json.loads((SCENE.parent/'checks/atomization.json').read_text())
        encoded=json.dumps(ledger['subsequent_piece_revisions'][:6],sort_keys=True,separators=(',',':')).encode()
        self.assertEqual(hashlib.sha256(encoded).hexdigest(),
                         '2a9c3a5e9303bed9727a325612530affad64f6a8009463402ec65975682da1d6')

    def test_symmetric_lineage_retains_the_accepted_wedges_before_the_stem_repair(self):
        ledger=json.loads((SCENE.parent/'checks/atomization.json').read_text())
        chain=audit_subsequent_piece_revisions(ledger)['hsr-component-modular-south-junction']
        self.assertEqual(len(chain),2)
        self.assertEqual(chain[0],ledger['subsequent_piece_revisions'][1])
        self.assertEqual(chain[1],ledger['subsequent_piece_revisions'][5])
        self.assertEqual(chain[0]['after_sha256'],chain[1]['before_sha256'])
        self.assertEqual(chain[1]['before_sha256'],
                         'd0c24a85209a56f0ac3e924b3f66e9ee291fd8362e65726c975b1033eaf3066a')
        self.assertEqual(chain[1]['only_added_geometry_property'],'stem_parapet_alignment')
        self.assertEqual(chain[1]['preserved_geometry_semantic_sha256'],
                         '081cb9770cf3d44f82947db73d46dc83feb65078989168614172184c54f20b35')
        self.assertEqual(chain[1]['status'],'standalone-verified/assembly-integration-deferred')
        self.assertFalse(chain[1]['assembly_resource_pins_refreshed'])
        self.assertFalse(chain[1]['assembly_render_refreshed'])

    def test_diverge_lineage_retains_the_accepted_left_border_before_the_right_extension(self):
        report=audit_candidate_ledger()
        candidate=report['eligible_atomized_candidates']['p01a-west-tail']
        current=piece_folder('hsr-component-l2-short-mainline-diverge-core')/'geometry.json'
        self.assertEqual(candidate['standalone_geometry_revision_chain'],[
            '7760cdba90db6e0b12959708faf677121a0f5913edae65ef83d524006004baa0',
            '4ab1cb1c939a896800373840832be4dd02dc6b199a41f7831e18ee65cb3f1ca4',
            hashlib.sha256(current.read_bytes()).hexdigest()])
        self.assertFalse(candidate['historical_source_superseded_by_explicit_redesign'])
        self.assertEqual(report['subsequent_piece_revisions'][4]['before_sha256'],
                         '4ab1cb1c939a896800373840832be4dd02dc6b199a41f7831e18ee65cb3f1ca4')
        self.assertFalse(report['current_assembly_resource_audit_claimed_by_this_ledger_check'])

    def test_opposed_merge_preserves_the_redesign_and_both_standalone_repairs(self):
        report=audit_candidate_ledger()
        candidate=report['eligible_atomized_candidates']['p03b-east-tail']
        revisions=[item for item in report['subsequent_piece_revisions']
                   if item['piece_id']=='hsr-component-l2-short-opposed-merge-core']
        self.assertEqual(len(revisions),2)
        revision,successor=revisions
        self.assertEqual(successor,report['subsequent_piece_revisions'][6])
        self.assertEqual(successor['before_sha256'],revision['after_sha256'])
        self.assertEqual(successor['before_sha256'],
                         '3ad00c99b0d3eccf69c5113d426e3680f2d4a03bd9ecb27d5e79542b00e228c1')
        prior=read_frozen_rework_record()['source_geometry'][revision['piece_id']]
        self.assertEqual(candidate['historical_replacement_geometry_sha256'],prior['before_sha256'])
        self.assertEqual(revision['before_sha256'],prior['after_sha256'])
        self.assertEqual(revision['before_sha256'],
                         '8bf5a7e8439a29017cc2d556695552ae98d0be9eaf4e550e6505a9ef30c6f7f8')
        self.assertEqual(candidate['current_replacement_geometry_sha256'],successor['after_sha256'])
        self.assertEqual(candidate['standalone_geometry_revision_chain'],[
            revision['before_sha256'],revision['after_sha256'],successor['after_sha256']])
        self.assertEqual(successor['status'],'standalone-verified/assembly-integration-deferred')
        self.assertFalse(successor['assembly_resource_pins_refreshed'])
        self.assertFalse(successor['assembly_render_refreshed'])
        self.assertFalse(report['current_assembly_resource_audit_claimed_by_this_ledger_check'])
        self.assertTrue(candidate['historical_source_superseded_by_explicit_redesign'])
        self.assertTrue(candidate['historical_source_superseded_by_standalone_piece_revision'])

    def test_a_missing_or_relabelled_intermediate_opposed_source_is_rejected(self):
        identifier='hsr-component-l2-short-opposed-merge-core'
        for field in ('before_sha256','after_sha256',None):
            with self.subTest(field=field):
                redesign=read_frozen_rework_record()
                if field is None:
                    del redesign['source_geometry'][identifier]
                else:
                    redesign['source_geometry'][identifier][field]='0'*64
                with self.assertRaisesRegex(ValueError,'stale for its changed replacement geometry'):
                    audit_candidate_ledger(redesign=redesign)

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


class SubsequentStandalonePieceRevisionControls(unittest.TestCase):
    def setUp(self):
        self.ledger=json.loads((SCENE.parent/'checks/atomization.json').read_text())
        self.revision=self.ledger['subsequent_piece_revisions'][0]
        self.temporary=tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root=Path(self.temporary.name)
        self.source=current_piece_source(self.revision['source_file'], self.root)
        copy_retirement_inputs(self.root)
        for revision in self.ledger['subsequent_piece_revisions']:
            if revision['piece_id']=='hsr-component-l2-paired-fan-compact-join':
                continue
            source=current_piece_source(revision['source_file'], self.root)
            original_source=current_piece_source(revision['source_file'], ROOT)
            source.parent.mkdir(parents=True,exist_ok=True)
            source.write_bytes(original_source.read_bytes())
            for relative in revision['standalone_evidence']:
                target=source.parent/relative
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(original_source.parent.joinpath(relative).read_bytes())
            prior=revision.get('superseded_attempt',revision.get('before_piece_snapshot'))
            original=original_source.parent/prior['snapshot_directory']
            snapshot=source.parent/prior['snapshot_directory']
            index=json.loads((original/'index.json').read_text())
            files=index['files']
            relatives=list(files) if isinstance(files,dict) else [
                item.get('snapshot_file',item.get('path')) for item in files]
            for relative in ['index.json',*relatives]:
                target=snapshot/relative
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes((original/relative).read_bytes())

    def audit(self):
        return audit_subsequent_piece_revisions(self.ledger,root=self.root)

    def revision_source(self,revision):
        source=current_piece_source(revision['source_file'], self.root)
        chain=[item for item in self.ledger['subsequent_piece_revisions']
               if item['piece_id']==revision['piece_id']]
        number=chain.index(revision)
        if number+1<len(chain):
            return source.parent/chain[number+1]['before_piece_snapshot']['snapshot_directory']/source.name
        return source

    def test_exact_standalone_revision_requires_no_old_build_or_assembly_artwork(self):
        result=self.audit()
        self.assertEqual(list(result),['hsr-component-l2-short-mainline-diverge-core',
                                     'hsr-component-modular-south-junction',
                                     'hsr-component-l2-paired-fan-compact-join',
                                     'hsr-component-l2-short-opposed-merge-core'])
        self.assertEqual(len(result['hsr-component-l2-short-mainline-diverge-core']),2)
        self.assertEqual(len(result['hsr-component-modular-south-junction']),2)
        self.assertEqual(len(result['hsr-component-l2-short-opposed-merge-core']),2)
        self.assertFalse((self.root/'dist').exists())
        self.assertFalse((self.root/'domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-join').exists())

    def test_changing_either_end_of_the_source_chain_is_rejected(self):
        for field in ('before_sha256','after_sha256','preserved_geometry_semantic_sha256'):
            with self.subTest(field=field):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][0][field]='0'*64
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)

    def test_a_different_source_or_added_piece_revision_is_rejected(self):
        for field,value in (('piece_id','hsr-component-l2-short-opposed-merge-core'),
                            ('source_file','domains/high-speed-rail/00_pieces/other/geometry.json')):
            with self.subTest(field=field):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][0][field]=value
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)
        self.ledger['subsequent_piece_revisions'].append(deepcopy(self.revision))
        with self.assertRaisesRegex(ValueError,'exact standalone authorization'):self.audit()

    def test_omitting_the_revision_does_not_approve_a_changed_source(self):
        del self.ledger['subsequent_piece_revisions']
        with self.assertRaisesRegex(ValueError,'exact standalone authorization'):self.audit()

    def test_a_wider_border_rule_cannot_be_authorized_by_rehashing_the_ledger(self):
        self.revision['south_parapet_alignment']['left_inner_half_width_m']-=.01
        with self.assertRaisesRegex(ValueError,'exact standalone authorization'):self.audit()

    def test_an_undeclared_source_border_edit_is_rejected(self):
        source=json.loads(self.source.read_text())
        source['south_parapet_alignment']['minimum_train_half_width_m']=2.4
        self.source.write_text(json.dumps(source))
        with self.assertRaisesRegex(ValueError,'border rule differs'):self.audit()

    def test_ports_paths_supports_and_sweep_contexts_cannot_change_with_the_border(self):
        original=json.loads(self.source.read_text())
        def port(source):source['metadata']['ports']['W']['in'][0]+=.001
        def path(source):source['layout'][0][1]['routes'][0]['points'][0][0]+=.001
        def support(source):source['metadata']['support_centers'][0][0]+=.001
        def context(source):source['retained_surface_context']['surface_decks'][0]['width']=14.9
        for change in (port,path,support,context):
            with self.subTest(change=change.__name__):
                source=deepcopy(original);change(source)
                self.source.write_text(json.dumps(source))
                with self.assertRaisesRegex(ValueError,'changed preexisting geometry'):self.audit()

    def test_even_a_source_byte_change_with_identical_semantics_requires_a_new_pin(self):
        self.source.write_bytes(self.source.read_bytes()+b'\n')
        with self.assertRaisesRegex(ValueError,'current source fingerprint differs'):self.audit()

    def test_relabelled_standalone_evidence_hashes_are_rejected(self):
        for relative in self.revision['standalone_evidence']:
            with self.subTest(evidence=relative):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][0]['standalone_evidence'][relative]='0'*64
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)

    def test_changed_actual_standalone_evidence_is_rejected(self):
        for relative in self.revision['standalone_evidence']:
            with self.subTest(evidence=relative):
                target=self.source.parent/relative
                original=target.read_bytes();target.write_bytes(original+b'\n')
                with self.assertRaisesRegex(ValueError,'standalone evidence fingerprint differs'):self.audit()
                target.write_bytes(original)

    def test_standalone_success_cannot_be_relabelled_as_assembly_completion(self):
        for field,value in (('status','passed'),('assembly_resource_pins_refreshed',True),
                            ('assembly_render_refreshed',True)):
            with self.subTest(field=field):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][0][field]=value
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)


    def test_the_superseded_attempt_identity_and_status_cannot_be_relabelled(self):
        for field,value in (('geometry_sha256','0'*64),('index_sha256','0'*64),
                            ('snapshot_directory','evidence/design-history/other-attempt'),
                            ('status','approved')):
            with self.subTest(field=field):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][0]['superseded_attempt'][field]=value
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)

    def test_changed_superseded_snapshot_index_is_rejected(self):
        index=self.source.parent/self.revision['superseded_attempt']['snapshot_directory']/'index.json'
        index.write_bytes(index.read_bytes()+b'\n')
        with self.assertRaisesRegex(ValueError,'snapshot index fingerprint differs'):self.audit()

    def test_archived_source_observations_reports_and_images_cannot_be_overwritten(self):
        snapshot=self.source.parent/self.revision['superseded_attempt']['snapshot_directory']
        index=json.loads((snapshot/'index.json').read_text())
        for item in index['files']:
            with self.subTest(file=item['snapshot_file']):
                target=snapshot/item['snapshot_file']
                original=target.read_bytes();target.write_bytes(original+b'\n')
                with self.assertRaisesRegex(ValueError,'archived evidence fingerprint differs'):self.audit()
                target.write_bytes(original)

    def test_the_old_rectangular_cap_cannot_replace_the_active_continuous_border(self):
        snapshot=self.source.parent/self.revision['superseded_attempt']['snapshot_directory']
        self.source.write_bytes((snapshot/'geometry.json').read_bytes())
        with self.assertRaisesRegex(ValueError,'border rule differs'):self.audit()

    def test_each_new_revision_rejects_altered_source_chain_and_predecessor_pins(self):
        self.assertEqual(len(self.ledger['subsequent_piece_revisions'][1:4]),3)
        for number,revision in enumerate(self.ledger['subsequent_piece_revisions'][1:4],1):
            for field in ('before_sha256','after_sha256','preserved_geometry_semantic_sha256'):
                with self.subTest(piece=revision['piece_id'],field=field):
                    changed=deepcopy(self.ledger)
                    changed['subsequent_piece_revisions'][number][field]='0'*64
                    with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                        audit_subsequent_piece_revisions(changed,root=self.root)
            for field in ('geometry_sha256','index_sha256','snapshot_directory'):
                with self.subTest(piece=revision['piece_id'],snapshot_field=field):
                    changed=deepcopy(self.ledger)
                    changed['subsequent_piece_revisions'][number]['before_piece_snapshot'][field]='altered'
                    with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                        audit_subsequent_piece_revisions(changed,root=self.root)

    def test_new_revisions_cannot_be_omitted_or_reordered(self):
        for number in range(1,4):
            with self.subTest(omitted_record=number):
                changed=deepcopy(self.ledger)
                del changed['subsequent_piece_revisions'][number]
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)
        changed=deepcopy(self.ledger)
        changed['subsequent_piece_revisions'][1:4]=reversed(changed['subsequent_piece_revisions'][1:4])
        with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
            audit_subsequent_piece_revisions(changed,root=self.root)

    def test_each_new_source_rejects_a_wider_wall_or_changed_existing_path(self):
        for revision in self.ledger['subsequent_piece_revisions'][1:4]:
            if revision['piece_id']=='hsr-component-l2-paired-fan-compact-join':
                continue  # Its exact old row is checked through the separate retirement proof.
            target=current_piece_source(revision['source_file'], self.root)
            latest=next(item for item in reversed(self.ledger['subsequent_piece_revisions'])
                        if item['piece_id']==revision['piece_id'])
            property_name=latest.get('only_added_geometry_property',latest.get('only_changed_geometry_property'))
            original=target.read_bytes()
            for mutation in ('wall','path','height','sweep'):
                with self.subTest(piece=revision['piece_id'],mutation=mutation):
                    source=json.loads(original)
                    if mutation=='wall':
                        source[property_name]['minimum_train_half_width_m']=2.4
                    elif mutation=='path':
                        source['layout'][0][1]['routes'][0]['points'][0][0]+=.001
                    elif mutation=='height':
                        source['metadata']['height']+=.001
                    else:
                        source['surface_context']['surface_decks'][0]['width']+=.01
                    target.write_text(json.dumps(source))
                    message='border rule differs' if mutation=='wall' else 'changed preexisting geometry'
                    with self.assertRaisesRegex(ValueError,message):self.audit()
                    target.write_bytes(original)

    def test_each_new_revision_rejects_relabelled_or_changed_actual_evidence(self):
        for number,revision in enumerate(self.ledger['subsequent_piece_revisions'][1:4],1):
            for relative in revision['standalone_evidence']:
                with self.subTest(piece=revision['piece_id'],evidence=relative):
                    changed=deepcopy(self.ledger)
                    changed['subsequent_piece_revisions'][number]['standalone_evidence'][relative]='0'*64
                    with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                        audit_subsequent_piece_revisions(changed,root=self.root)
                    if revision['piece_id']=='hsr-component-l2-paired-fan-compact-join':
                        continue
                    target=self.revision_source(revision).parent/relative
                    original=target.read_bytes();target.write_bytes(original+b'\n')
                    with self.assertRaisesRegex(ValueError,'standalone evidence fingerprint differs'):self.audit()
                    target.write_bytes(original)

    def test_each_new_snapshot_rejects_changed_index_source_observations_report_and_image(self):
        for revision in self.ledger['subsequent_piece_revisions'][1:4]:
            if revision['piece_id']=='hsr-component-l2-paired-fan-compact-join':
                continue  # Removed piece-local evidence is explicitly unavailable for replay.
            snapshot=(current_piece_source(revision['source_file'], self.root)).parent/revision['before_piece_snapshot']['snapshot_directory']
            for relative in ('index.json','geometry.json','checks/manual-tests.json',
                             'evidence/saved-resource-checks.json','previews/preview.png'):
                with self.subTest(piece=revision['piece_id'],archived_file=relative):
                    target=snapshot/relative
                    original=target.read_bytes();target.write_bytes(original+b'\n')
                    message=('snapshot index fingerprint differs' if relative=='index.json'
                             else 'archived evidence fingerprint differs')
                    with self.assertRaisesRegex(ValueError,message):self.audit()
                    target.write_bytes(original)

    def test_no_new_standalone_revision_can_be_relabelled_as_completed_assembly_work(self):
        for number,revision in enumerate(self.ledger['subsequent_piece_revisions'][1:4],1):
            for field,value in (('status','passed'),('assembly_resource_pins_refreshed',True),
                                ('assembly_render_refreshed',True)):
                with self.subTest(piece=revision['piece_id'],field=field):
                    changed=deepcopy(self.ledger)
                    changed['subsequent_piece_revisions'][number][field]=value
                    with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                        audit_subsequent_piece_revisions(changed,root=self.root)

    def test_right_extension_successor_cannot_skip_or_relabel_its_accepted_predecessor(self):
        successor=self.ledger['subsequent_piece_revisions'][4]
        self.assertEqual(successor['only_changed_geometry_property'],'south_parapet_alignment')
        self.assertNotIn('only_added_geometry_property',successor)
        for before in ('0'*64,
                       '7760cdba90db6e0b12959708faf677121a0f5913edae65ef83d524006004baa0',
                       '4b0c7313fd3c7ece31aa43fca820cde4bb6ced03e95d4d1ba4604a230d800d51'):
            with self.subTest(before=before):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][4]['before_sha256']=before
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)

    def test_right_extension_successor_cannot_be_omitted_or_duplicated(self):
        for mutation in ('omit','duplicate'):
            with self.subTest(mutation=mutation):
                changed=deepcopy(self.ledger)
                if mutation=='omit':del changed['subsequent_piece_revisions'][4]
                else:changed['subsequent_piece_revisions'].append(deepcopy(changed['subsequent_piece_revisions'][4]))
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)

    def test_the_accepted_predecessor_cannot_stand_in_for_the_current_right_extension(self):
        successor=self.ledger['subsequent_piece_revisions'][4]
        snapshot=self.source.parent/successor['before_piece_snapshot']['snapshot_directory']
        self.source.write_bytes((snapshot/'geometry.json').read_bytes())
        with self.assertRaisesRegex(ValueError,'border rule differs'):self.audit()

    def test_the_accepted_predecessor_source_and_reports_remain_bound_to_their_snapshot(self):
        successor=self.ledger['subsequent_piece_revisions'][4]
        snapshot=self.source.parent/successor['before_piece_snapshot']['snapshot_directory']
        for relative in ('geometry.json',*self.revision['standalone_evidence']):
            with self.subTest(accepted_predecessor_file=relative):
                target=snapshot/relative
                original=target.read_bytes();target.write_bytes(original+b'\n')
                with self.assertRaisesRegex(ValueError,'fingerprint differs'):self.audit()
                target.write_bytes(original)

    def test_the_right_extension_does_not_authorize_altering_the_accepted_left_border(self):
        source=json.loads(self.source.read_text())
        source['south_parapet_alignment']['left_inner_half_width_m']=2.7
        self.source.write_text(json.dumps(source))
        with self.assertRaisesRegex(ValueError,'border rule differs'):self.audit()


    def test_stem_successor_cannot_skip_or_relabel_its_accepted_predecessor(self):
        successor=self.ledger['subsequent_piece_revisions'][5]
        self.assertEqual(successor['only_added_geometry_property'],'stem_parapet_alignment')
        self.assertNotIn('only_changed_geometry_property',successor)
        changes=[('before_sha256','0'*64),
                 ('before_sha256',self.ledger['subsequent_piece_revisions'][1]['before_sha256']),
                 ('after_sha256','0'*64),('preserved_geometry_semantic_sha256','0'*64),
                 ('source_file',self.revision['source_file']),('piece_id',self.revision['piece_id']),
                 ('status','passed'),('assembly_resource_pins_refreshed',True),
                 ('assembly_render_refreshed',True),
                 ('only_added_geometry_property','junction_wedge_alignment')]
        for field,value in changes:
            with self.subTest(field=field,value=value):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][5][field]=value
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)
        for field in ('geometry_sha256','index_sha256','snapshot_directory'):
            with self.subTest(snapshot_field=field):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][5]['before_piece_snapshot'][field]='altered'
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)

    def test_stem_successor_cannot_be_omitted_duplicated_or_moved_before_its_predecessor(self):
        for mutation in ('omit','duplicate','reorder'):
            with self.subTest(mutation=mutation):
                changed=deepcopy(self.ledger)
                revisions=changed['subsequent_piece_revisions']
                if mutation=='omit':del revisions[5]
                elif mutation=='duplicate':revisions.append(deepcopy(revisions[5]))
                else:revisions[1],revisions[5]=revisions[5],revisions[1]
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)

    def test_the_accepted_wedge_source_cannot_replace_the_current_stem_repair(self):
        successor=self.ledger['subsequent_piece_revisions'][5]
        source=current_piece_source(successor['source_file'], self.root)
        snapshot=source.parent/successor['before_piece_snapshot']['snapshot_directory']
        source.write_bytes((snapshot/'geometry.json').read_bytes())
        with self.assertRaisesRegex(ValueError,'border rule differs'):self.audit()

    def test_the_stem_repair_does_not_authorize_changing_the_accepted_wedge_rule(self):
        successor=self.ledger['subsequent_piece_revisions'][5]
        source=current_piece_source(successor['source_file'], self.root)
        current=json.loads(source.read_text())
        current['junction_wedge_alignment']['branch_inner_half_width_m']=2.7
        source.write_text(json.dumps(current))
        with self.assertRaisesRegex(ValueError,'changed preexisting geometry'):self.audit()

    def test_the_stem_predecessor_source_reports_observations_and_images_remain_frozen(self):
        successor=self.ledger['subsequent_piece_revisions'][5]
        source=current_piece_source(successor['source_file'], self.root)
        snapshot=source.parent/successor['before_piece_snapshot']['snapshot_directory']
        prior=self.ledger['subsequent_piece_revisions'][1]
        for relative in ('index.json','geometry.json',*prior['standalone_evidence'],
                         'checks/manual-tests.json','previews/preview.png'):
            with self.subTest(accepted_predecessor_file=relative):
                target=snapshot/relative
                original=target.read_bytes();target.write_bytes(original+b'\n')
                with self.assertRaisesRegex(ValueError,'fingerprint differs'):self.audit()
                target.write_bytes(original)

    def test_the_current_stem_evidence_and_exact_rule_cannot_be_relabelled(self):
        successor=self.ledger['subsequent_piece_revisions'][5]
        source=current_piece_source(successor['source_file'], self.root)
        for relative in successor['standalone_evidence']:
            with self.subTest(current_evidence=relative):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][5]['standalone_evidence'][relative]='0'*64
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)
                target=source.parent/relative
                original=target.read_bytes();target.write_bytes(original+b'\n')
                with self.assertRaisesRegex(ValueError,'standalone evidence fingerprint differs'):self.audit()
                target.write_bytes(original)
        changed=deepcopy(self.ledger)
        changed['subsequent_piece_revisions'][5]['stem_parapet_alignment']['branch_inner_half_width_m']=2.7
        with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
            audit_subsequent_piece_revisions(changed,root=self.root)


    def test_opposite_join_successor_cannot_skip_or_relabel_its_accepted_predecessor(self):
        successor=self.ledger['subsequent_piece_revisions'][6]
        self.assertEqual(successor['only_changed_geometry_property'],'opposed_parapet_alignment')
        self.assertNotIn('only_added_geometry_property',successor)
        rule=successor['opposed_parapet_alignment']
        self.assertEqual(rule['outer_join_mode'],'continuous_branch_inside_outline')
        self.assertNotIn('north_opposite_cap_local_east_m',rule)
        self.assertNotIn('south_opposite_cap_local_east_m',rule)
        self.assertEqual(successor['preserved_geometry_semantic_sha256'],
                         '50cace339297dad171b9b03dfc94e8dc97b9e4f19221239d4fb2462536542cea')
        changes=[('before_sha256','0'*64),
                 ('before_sha256',self.ledger['subsequent_piece_revisions'][3]['before_sha256']),
                 ('after_sha256','0'*64),('preserved_geometry_semantic_sha256','0'*64),
                 ('source_file',self.revision['source_file']),('piece_id',self.revision['piece_id']),
                 ('status','passed'),('assembly_resource_pins_refreshed',True),
                 ('assembly_render_refreshed',True),
                 ('only_changed_geometry_property','south_parapet_alignment')]
        for field,value in changes:
            with self.subTest(field=field,value=value):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][6][field]=value
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)
        for field in ('geometry_sha256','index_sha256','snapshot_directory'):
            with self.subTest(snapshot_field=field):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][6]['before_piece_snapshot'][field]='altered'
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)

    def test_opposite_join_successor_cannot_be_omitted_duplicated_or_moved_before_its_predecessor(self):
        for mutation in ('omit','duplicate','reorder'):
            with self.subTest(mutation=mutation):
                changed=deepcopy(self.ledger)
                revisions=changed['subsequent_piece_revisions']
                if mutation=='omit':del revisions[6]
                elif mutation=='duplicate':revisions.append(deepcopy(revisions[6]))
                else:revisions[3],revisions[6]=revisions[6],revisions[3]
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)

    def test_the_accepted_opposed_source_cannot_replace_the_current_opposite_joins(self):
        successor=self.ledger['subsequent_piece_revisions'][6]
        source=current_piece_source(successor['source_file'], self.root)
        snapshot=source.parent/successor['before_piece_snapshot']['snapshot_directory']
        source.write_bytes((snapshot/'geometry.json').read_bytes())
        with self.assertRaisesRegex(ValueError,'border rule differs'):self.audit()

    def test_the_opposite_joins_cannot_rebind_the_native_cell_or_widen_the_branch(self):
        successor=self.ledger['subsequent_piece_revisions'][6]
        source=current_piece_source(successor['source_file'], self.root)
        original=json.loads(source.read_text())
        for field,value in (('raw_west_cell_sha256','0'*64),('branch_inner_half_width_m',2.7)):
            with self.subTest(protected_rule_field=field):
                current=deepcopy(original)
                current['opposed_parapet_alignment'][field]=value
                source.write_text(json.dumps(current))
                with self.assertRaisesRegex(ValueError,'border rule differs'):self.audit()

    def test_the_opposed_predecessor_source_reports_observations_and_images_remain_frozen(self):
        successor=self.ledger['subsequent_piece_revisions'][6]
        source=current_piece_source(successor['source_file'], self.root)
        snapshot=source.parent/successor['before_piece_snapshot']['snapshot_directory']
        prior=self.ledger['subsequent_piece_revisions'][3]
        for relative in ('index.json','geometry.json',*prior['standalone_evidence'],
                         'checks/manual-tests.json','previews/preview.png'):
            with self.subTest(accepted_predecessor_file=relative):
                target=snapshot/relative
                original=target.read_bytes();target.write_bytes(original+b'\n')
                with self.assertRaisesRegex(ValueError,'fingerprint differs'):self.audit()
                target.write_bytes(original)

    def test_the_current_opposite_join_evidence_and_exact_rule_cannot_be_relabelled(self):
        successor=self.ledger['subsequent_piece_revisions'][6]
        source=current_piece_source(successor['source_file'], self.root)
        for relative in successor['standalone_evidence']:
            with self.subTest(current_evidence=relative):
                changed=deepcopy(self.ledger)
                changed['subsequent_piece_revisions'][6]['standalone_evidence'][relative]='0'*64
                with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
                    audit_subsequent_piece_revisions(changed,root=self.root)
                target=source.parent/relative
                original=target.read_bytes();target.write_bytes(original+b'\n')
                with self.assertRaisesRegex(ValueError,'standalone evidence fingerprint differs'):self.audit()
                target.write_bytes(original)
        changed=deepcopy(self.ledger)
        changed['subsequent_piece_revisions'][6]['opposed_parapet_alignment']['branch_inner_half_width_m']=2.7
        with self.assertRaisesRegex(ValueError,'exact standalone authorization'):
            audit_subsequent_piece_revisions(changed,root=self.root)


class CurrentFanAtomizationSourceControls(unittest.TestCase):
    def test_exact_new_poses_preserve_every_other_placement_dictionary(self):
        from scp_hsr.hsr_trumpet_border_verify import frozen_inputs, expected_current_placements
        frozen=frozen_inputs()
        actual=historical_scene()['placements']
        def physical(item):
            result={key:deepcopy(value) for key,value in item.items() if key not in ('name','menu_name')}
            return result
        self.assertEqual([physical(item) for item in actual],
                         [physical(item) for item in expected_current_placements(frozen)])
        old={item['label']:physical(item) for item in frozen['scene']['placements'] if item['label']!='P06'}
        retained={item['label']:physical(item) for item in actual if item['label'] not in ('P06','P06A','P06B')}
        self.assertEqual(old,retained)
        self.assertEqual(len(retained),25)
        self.assertEqual(len(actual),28)
        self.assertEqual(len({item['piece_id'] for item in actual}),14)

    def test_seven_source_history_dictionaries_remain_the_exact_frozen_list(self):
        from scp_hsr.hsr_trumpet_border_verify import frozen_inputs,canonical_sha256,STANDALONE_REVISIONS_SHA256
        current=json.loads((SCENE.parent/'checks/atomization.json').read_text())
        self.assertEqual(current['subsequent_piece_revisions'],frozen_inputs()['ledger']['subsequent_piece_revisions'])
        self.assertEqual(canonical_sha256(current['subsequent_piece_revisions']),STANDALONE_REVISIONS_SHA256)

    def test_frozen_layout_retains_its_distinct_historical_identity(self):
        from scp_hsr.hsr_trumpet_border_verify import CURRENT_INTEGRATION_LAYOUT,frozen_inputs
        from scp_hsr.hsr_trumpet_rework_verify import CURRENT_LAYOUT
        self.assertNotEqual(CURRENT_INTEGRATION_LAYOUT,CURRENT_LAYOUT)
        self.assertEqual(frozen_inputs()['descriptor']['layout_sha256'],CURRENT_LAYOUT)
        self.assertEqual(audit_approved_layout(historical_scene())['layout_sha256'],CURRENT_INTEGRATION_LAYOUT)

    def straight_routes(self):
        return [{'role':'branch','transport':7,'class':0,'entry':1,'exit':3,'junction':0,
                 'points':[(-2.,8.,15.5),(-2.,-8.,15.5)]},
                {'role':'branch','transport':7,'class':0,'entry':3,'exit':1,'junction':0,
                 'points':[(2.,-8.,15.5),(2.,8.,15.5)]}]

    def test_exact_collinear_path_subdivision_preserves_directed_straight_geometry(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_straight_path_geometry
        routes=self.straight_routes()
        for route in routes:
            first,last=route['points'];route['points'].insert(1,tuple((a+b)/2 for a,b in zip(first,last)))
        self.assertEqual(audit_straight_path_geometry(encode_paths(routes))['exact_directed_straight_routes'],2)

    def test_every_semantic_straight_flag_and_direction_is_independently_fixed(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_straight_path_geometry
        for field,value in (('transport',6),('class',1),('entry',3),('exit',1),('junction',1)):
            lines=encode_paths(self.straight_routes()).decode().splitlines()
            start=next(i+1 for i,line in enumerate(lines) if line.startswith('-- SCP_'))
            lines[start+('transport','class','entry','exit','junction').index(field)]=str(value)
            with self.subTest(field=field),self.assertRaisesRegex(ValueError,'directed PATH geometry or route flags'):
                audit_straight_path_geometry(('\r\n'.join(lines)+'\r\n').encode())
        routes=self.straight_routes();routes[0]['points'].reverse()
        with self.assertRaisesRegex(ValueError,'directed PATH geometry or route flags'):
            audit_straight_path_geometry(encode_paths(routes))

    def test_straight_path_normalization_cannot_hide_a_one_micrometre_bend(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_straight_path_geometry
        routes=self.straight_routes();routes[0]['points'].insert(1,(-1.999999,0.,15.5))
        with self.assertRaisesRegex(ValueError,'directed PATH geometry or route flags'):
            audit_straight_path_geometry(encode_paths(routes))

    def test_collinear_normalization_does_not_remove_a_reversal(self):
        from scp_hsr.hsr_trumpet_border_verify import strictly_coalesced_points
        points=[(0.,0.,0.),(1.,0.,0.),(.5,0.,0.)]
        self.assertEqual(strictly_coalesced_points(points),points)

    def test_capture_requires_independent_final_archive_pins(self):
        from scp_hsr import hsr_trumpet_border_verify as current
        frozen=current.frozen_inputs()
        for name in ('CORE_ARCHIVE_SHA256','STRAIGHT_ARCHIVE_SHA256'):
            with self.subTest(pin=name),patch.object(current,name,None),self.assertRaisesRegex(ValueError,'awaits'):
                current.expected_archives(frozen)

    def test_capture_write_failure_restores_every_previous_contract(self):
        from scp_hsr_tools.verify_hsr_trumpet import _commit_current_contracts
        with tempfile.TemporaryDirectory() as temporary:
            first=Path(temporary)/'first.json';second=Path(temporary)/'second.json';new=Path(temporary)/'new.json'
            first.write_bytes(b'old first');second.write_bytes(b'old second')
            replace=os.replace;calls=[]
            def fail_second(source,target):
                calls.append(target)
                if len(calls)==2:raise OSError('injected second-file replacement failure')
                return replace(source,target)
            with patch('scp_hsr_tools.verify_hsr_trumpet.os.replace',side_effect=fail_second),self.assertRaisesRegex(OSError,'injected'):
                _commit_current_contracts({first:b'new first',second:b'new second',new:b'new third'})
            self.assertEqual(first.read_bytes(),b'old first')
            self.assertEqual(second.read_bytes(),b'old second')
            self.assertFalse(new.exists())
            self.assertEqual({path.name for path in Path(temporary).iterdir()},{'first.json','second.json'})


    def test_post_commit_validation_failure_restores_all_contracts(self):
        from scp_hsr_tools.verify_hsr_trumpet import _commit_and_validate_current_contracts
        with tempfile.TemporaryDirectory() as temporary:
            old=Path(temporary)/'old.json';new=Path(temporary)/'new.json'
            old.write_bytes(b'exact original')
            def reject():
                self.assertEqual(old.read_bytes(),b'candidate')
                self.assertTrue(new.exists())
                raise ValueError('injected completed-record rejection')
            with self.assertRaisesRegex(ValueError,'injected completed-record rejection'):
                _commit_and_validate_current_contracts({old:b'candidate',new:b'candidate record'},reject)
            self.assertEqual(old.read_bytes(),b'exact original')
            self.assertFalse(new.exists())

    def test_selected_types_keep_ordinary_straight_and_retained_full_fan_registration(self):
        from scp_hsr.hsr_trumpet_border_verify import FULL_FAN_ID
        from scp.subject_sources import piece_id_for_recipe
        collections=jsonc.load(ROOT/'domains/high-speed-rail/collections.jsonc')['collections']
        selected=collections['hsr-straight-stem-trumpet']
        self.assertEqual(set(selected),set(CURRENT_IDS))
        self.assertEqual(len(selected),14)
        for recipe in ('hsr_component_l2_paired_fan_compact_core',
                       'hsr_component_l2_paired_straight_recessed_web',
                       'hsr_component_lower_paired_straight'):
            self.assertIn(piece_id_for_recipe(recipe, ROOT), selected)
        self.assertNotIn(FULL_FAN_ID,selected)
        self.assertFalse((ROOT/'domains/high-speed-rail/00_pieces'/FULL_FAN_ID).exists())


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

    def test_existing_paired_straight_passes_declared_reference_sections_but_widening_fails(self):
        tile=next(t for t in self.tiles.values() if t['piece_id']==STRAIGHT_ID)
        source=list(_triangles(parse_s3d(tile['resources']['model_0'])))
        triangles=[tuple((-south+16.*column,height,x,u,v) for x,height,south,u,v in tri)
                   for column in range(4) for tri in source]
        contract=CONTRACTS['hsr_component_l2_short_mainline_diverge_core']
        self.assertEqual(audit_native_sections(triangles,contract)['complete_native_join_sections_checked'],3)
        widened=[tuple((x,h,z*1.01,u,v) for x,h,z,u,v in tri) for tri in triangles]
        with self.assertRaisesRegex(ValueError,'native joining section differs'):
            audit_native_sections(widened,contract)


class SupersededFanParentRetirementControls(unittest.TestCase):
    def setUp(self):
        self.temporary=tempfile.TemporaryDirectory();self.addCleanup(self.temporary.cleanup)
        self.root=Path(self.temporary.name)
        copy_retirement_inputs(self.root)
        synthetic_retirement_manifests(self, self.root)

    def audit(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_parent_retirement
        return audit_parent_retirement(root=self.root)

    def test_retirement_preserves_original_audit_without_claiming_a_new_execution(self):
        from scp_hsr.hsr_trumpet_border_verify import FULL_FAN_ID
        record=self.audit()
        self.assertFalse((self.root/'domains/high-speed-rail/00_pieces'/FULL_FAN_ID).exists())
        self.assertFalse(record['historical_source_replay_available_for_retired_piece'])
        for field in ('new_physical_audit_executed','assembly_geometry_changed','assembly_render_regenerated',
                      'historical_decisions_rewritten','manual_or_game_observations_added','installed'):
            self.assertFalse(record[field])
        initial=json.loads((self.root/SCENE.parent.relative_to(ROOT)/'checks/border-piece-integration.json').read_text())
        self.assertTrue(initial['policy']['full_fan_retained_in_library_unchanged'])
        self.assertFalse(record['retired_piece']['active_piece_directory_present'])

    def test_recreating_any_retired_source_directory_is_rejected(self):
        from scp_hsr.hsr_trumpet_border_verify import FULL_FAN_ID
        (self.root/'domains/high-speed-rail/00_pieces'/FULL_FAN_ID).mkdir()
        with self.assertRaisesRegex(ValueError,'active or compatibility source'):
            self.audit()

    def test_reintroducing_the_retired_identity_in_a_registry_or_collection_is_rejected(self):
        from scp_hsr.hsr_trumpet_border_verify import FULL_FAN_ID
        domain=self.root/'domains/high-speed-rail'
        for relative in ('domain.jsonc','collections.jsonc'):
            target=domain/relative;raw=target.read_bytes();record=jsonc.loads(raw.decode())
            if relative=='domain.jsonc':record['pieces'].append('00_pieces/'+FULL_FAN_ID+'/piece.json')
            else:record['collections']['retired-copy']=[FULL_FAN_ID]
            jsonc.dump(target, record)
            with self.subTest(registry=relative),self.assertRaisesRegex(ValueError,'active piece selection'):
                self.audit()
            target.write_bytes(raw)

    def test_coordinated_retirement_rehash_cannot_change_identity_pins_or_verification_scope(self):
        from scp_hsr import hsr_trumpet_border_verify as current
        target=self.root/SCENE.parent.relative_to(ROOT)/current.PARENT_RETIREMENT_RELATIVE
        original=target.read_bytes()
        changes=[lambda r:r['retired_piece'].__setitem__('id',current.CORE_ID),
                 lambda r:r['retired_piece']['historical_source_inputs'].__setitem__('geometry.json','0'*64),
                 lambda r:r['current_replacements'][0].__setitem__('archive_sha256','0'*64),
                 lambda r:r.__setitem__('status','passed-new-physical-audit'),
                 lambda r:r.__setitem__('historical_source_replay_available_for_retired_piece',True),
                 lambda r:r.__setitem__('new_physical_audit_executed',True),
                 lambda r:r.__setitem__('standalone_revisions_sha256','0'*64)]
        for number,change in enumerate(changes):
            record=json.loads(original);change(record);raw=(json.dumps(record)+'\n').encode();target.write_bytes(raw)
            with self.subTest(mutation=number),patch.object(current,'PARENT_RETIREMENT_SHA256',hashlib.sha256(raw).hexdigest()),self.assertRaisesRegex(ValueError,'exact successor scope'):
                self.audit()
        target.write_bytes(original)

    def test_changed_historical_gate_or_retained_extraction_source_cannot_inherit_acceptance(self):
        from scp_hsr import hsr_trumpet_border_verify as current
        targets=[self.root/SCENE.parent.relative_to(ROOT)/relative for relative in current.PRESERVED_INTEGRATION_FILES]
        for identifier,inputs in ((current.CORE_ID,current.CORE_SOURCE_INPUTS),
                                  (current.STRAIGHT_ID,current.STRAIGHT_SOURCE_INPUTS)):
            targets.extend(self.root/'domains/high-speed-rail/00_pieces'/identifier/relative
                           for relative in {**inputs,**current.EXTRACTED_STANDALONE_EVIDENCE[identifier]})
        for target in targets:
            raw=target.read_bytes();target.write_bytes(raw+b'\n')
            with self.subTest(file=target.relative_to(self.root)),self.assertRaisesRegex(ValueError,'changes its preserved integration proof|changes a retained source or extraction proof'):
                self.audit()
            target.write_bytes(raw)


class CurrentFanIntegrationSavedControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build,cls.tiles,cls.descriptor=saved_current()
        cls.scene=json.loads(SCENE.read_text())
        cls.journeys=_journeys(encoded_records(cls.tiles),CONTRACT)

    def altered_record(self,change):
        from scp_hsr.hsr_trumpet_border_verify import read_border_integration_record
        record=json.loads((SCENE.parent/'checks/border-piece-integration.json').read_text())
        descriptor=deepcopy(self.descriptor);change(record)
        raw=(json.dumps(record,indent=2)+'\n').encode()
        descriptor['border_piece_integration_sha256']=hashlib.sha256(raw).hexdigest()
        with tempfile.TemporaryDirectory() as temporary:
            target=Path(temporary)/'integration.json';target.write_bytes(raw)
            return read_border_integration_record(target,descriptor=descriptor)

    def test_current_record_is_separate_from_all_seven_original_deferred_decisions(self):
        from scp_hsr.hsr_trumpet_border_verify import read_border_integration_record
        record=read_border_integration_record()
        self.assertEqual(record['status'],'passed')
        self.assertEqual(record['compiled_audit']['placements'],28)
        self.assertEqual(record['compiled_audit']['component_types_checked'],14)
        self.assertFalse(record['historical_standalone_rows_rewritten'])
        ledger=json.loads((SCENE.parent/'checks/atomization.json').read_text())
        self.assertEqual(len(ledger['subsequent_piece_revisions']),7)
        self.assertTrue(all(row['status']=='standalone-verified/assembly-integration-deferred'
                            and row['assembly_resource_pins_refreshed'] is False
                            and row['assembly_render_refreshed'] is False
                            for row in ledger['subsequent_piece_revisions']))

    def test_coordinated_policy_record_relabeling_cannot_expand_edit_scope(self):
        mutations=[lambda r:r['policy']['allowed_model_world_cells_east_north_m'].append([0.,0.]),
                   lambda r:r['policy'].__setitem__('unchanged_world_path_sets',102),
                   lambda r:r['policy'].__setitem__('unchanged_complete_archives',8),
                   lambda r:r['policy']['accepted_wedge_shadow_transition']['resources'][0].__setitem__('after_sha256','0'*64),
                   lambda r:r['policy']['new_core_identity'].__setitem__('preview_id','7f505ff4'),
                   lambda r:r['policy']['new_recessed_web_straight_identity'].__setitem__('puzzle_id','f830'),
                   lambda r:r['policy'].__setitem__('fan_core_atomization_decision_sha256','0'*64)]
        for index,mutation in enumerate(mutations):
            with self.subTest(mutation=index),self.assertRaisesRegex(ValueError,'approved scope'):
                self.altered_record(mutation)

    def test_coordinated_compiled_record_relabeling_cannot_change_measured_counts_or_hashes(self):
        changes={'actual_tile_triangles':self.descriptor['actual_tile_triangles']+1,'encoded_fragments':167,
                 'placements':26,'component_types_checked':13,'occupied_cells':104,'support_positions':73,
                 'proper_rotations_checked':3,'complete_journeys_checked':5,
                 'world_cells_sha256':'0'*64,'journeys_sha256':'0'*64,'all_independent_physical_checks_passed':False}
        for field,value in changes.items():
            with self.subTest(field=field),self.assertRaisesRegex(ValueError,'compiled audit differs'):
                self.altered_record(lambda r:r['compiled_audit'].__setitem__(field,value))

    def test_current_integration_cannot_claim_installation_rendering_or_game_observations(self):
        for field in ('historical_standalone_rows_rewritten','manual_or_game_observations_added',
                      'rendering_checked_by_this_record','installed'):
            with self.subTest(field=field),self.assertRaisesRegex(ValueError,'overstates'):
                self.altered_record(lambda r:r.__setitem__(field,True))

    def test_actual_source_and_all_scoped_atomization_and_native_artifacts_reject_changed_bytes(self):
        from scp_hsr import hsr_trumpet_border_verify as current
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)
            copy_retirement_inputs(root)
            all_inputs={**current.SOURCE_INPUTS,current.CORE_ID:current.CORE_SOURCE_INPUTS,
                        current.STRAIGHT_ID:current.STRAIGHT_SOURCE_INPUTS}
            all_inputs={identifier:{**files,**current.EXTRACTED_STANDALONE_EVIDENCE.get(identifier,{})}
                        for identifier,files in all_inputs.items() if identifier!=current.FULL_FAN_ID}
            targets=[]
            for identifier,files in all_inputs.items():
                for relative in files:
                    source=piece_folder(identifier)/relative
                    target=root/source.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copyfile(source,target);targets.append(target)
            for relative in ('checks/atomization.json',*current.FAN_ATOMIZATION_INPUTS):
                source=SCENE.parent/relative;target=root/source.relative_to(ROOT)
                target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
                if relative!='checks/atomization.json':targets.append(target)
            current.audit_source_inputs(root)
            for target in targets:
                raw=target.read_bytes();target.write_bytes(raw+b'\n')
                with self.subTest(file=target.relative_to(root)),self.assertRaisesRegex(ValueError,'differs|changes|seven standalone history rows'):
                    current.audit_source_inputs(root)
                target.write_bytes(raw)

    def test_current_initial_manifest_and_source_pins_are_independent(self):
        from scp_hsr.hsr_trumpet_border_verify import CORE_ID
        for mutation,message in ((lambda r:r['compiled_audit'].__setitem__('manifest_sha256','0'*64),'initial audit manifest differs'),
                (lambda r:r['source_inputs'][CORE_ID].__setitem__('geometry.json','0'*64),'source or standalone history binding'),
                (lambda r:r.__setitem__('standalone_revisions_sha256','0'*64),'source or standalone history binding')):
            with self.subTest(message=message),self.assertRaisesRegex(ValueError,message):
                self.altered_record(mutation)

    def test_recorded_empty_cell_and_join_proofs_cannot_be_rewritten_with_a_new_descriptor_hash(self):
        changes=[lambda r:r['current_empty_structural_cell_proof']['cells'][0].__setitem__('positive_surface_intersections_by_zoom',[1,0,0,0,0]),
                 lambda r:r['current_empty_structural_cell_proof']['checked_model_resources'][0].__setitem__('sha256','0'*64),
                 lambda r:r['current_model_scope_audit'].__setitem__('all_fourteen_archives_match_independent_prior_approval',False),
                 lambda r:r['current_merge_join_and_preserved_routes'].__setitem__('actual_native_joining_sections_checked',5)]
        for index,change in enumerate(changes):
            with self.subTest(mutation=index),self.assertRaisesRegex(ValueError,'removed cell contains|preservation proofs'):
                self.altered_record(change)

    def test_actual_current_scope_preserves_exact_approved_archives_and_103_path_sets(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_border_scope
        report=audit_border_scope(self.tiles,self.build,self.scene)
        self.assertEqual(len(report['independently_approved_current_archives']),14)
        self.assertEqual(report['unchanged_world_path_sets'],103)
        self.assertEqual(report['exact_recessed_web_straight_path_substitutions'],2)
        self.assertEqual(report['unchanged_world_shadow_sets'],102)
        self.assertTrue(report['retained_nine_core_tiles_exact_at_all_five_zooms'])
        self.assertIn('Historical initial-integration policy',report['policy_scope'])
        self.assertFalse(report['current_source_retirement']['parent_active_in_current_library'])
        self.assertFalse(report['current_source_retirement']['historical_policy_rewritten'])

    def test_no_placed_model_or_path_or_shadow_can_change_even_inside_the_allowed_piece_region(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_border_scope
        for position,name in (((112.,80.),'model_0'),((112.,64.),'path'),((112.,48.),'shadow_4'),((-112.,0.),'model_0')):
            changed=deepcopy(self.tiles);changed[position]['resources'][name]+=b'\0'
            with self.subTest(position=position,resource=name),self.assertRaisesRegex(ValueError,'placed resources differ'):
                audit_border_scope(changed,self.build,self.scene)

    def test_current_core_local_mapping_and_straight_owner_are_exact(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_border_scope
        for position,field,value in (((112.,48.),'cell',(3,2)),((112.,80.),'instance_id','P06B')):
            changed=deepcopy(self.tiles);changed[position][field]=value
            with self.subTest(position=position),self.assertRaisesRegex(ValueError,'world owner, local cell, or rotation'):
                audit_border_scope(changed,self.build,self.scene)

    def test_all_six_continuous_journeys_reject_any_small_bend(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_current_journey_geometry
        for movement in self.journeys:
            changed=deepcopy(self.journeys);points=changed[movement];index=len(points)//2
            x,n,h=points[index]
            before,after=points[index-1],points[index+1]
            east,north=after[0]-before[0],after[1]-before[1]
            length=(east*east+north*north)**.5
            self.assertGreater(length,0.)
            # A perpendicular displacement changes the line itself. Moving
            # along a straight line only changes its redundant subdivision.
            points[index]=(x-.000001*north/length,n+.000001*east/length,h)
            with self.subTest(movement=movement),self.assertRaisesRegex(ValueError,'complete directed journey geometry'):
                audit_current_journey_geometry(changed)

    def test_collinear_resampling_of_both_mainlines_preserves_continuous_geometry(self):
        from scp_hsr.hsr_trumpet_border_verify import audit_current_journey_geometry
        for movement in (('W_in','E_out'),('E_in','W_out')):
            changed=deepcopy(self.journeys);points=changed[movement];index=len(points)//2
            x,n,h=points[index];points[index]=(x+.000001,n,h)
            with self.subTest(movement=movement):
                report=audit_current_journey_geometry(changed)
                self.assertEqual(report['complete_directed_journey_geometries_preserved'],6)

    def test_current_core_pier_overhang_requires_exact_native_bytes_and_same_instance_neighbor(self):
        from scp_hsr.assembly_inspection import _preserved_edge_support_vertex
        point=(-8.25,10.,-2.,.035,.5);position=(112.,32.)
        tile=self.tiles[position]
        self.assertTrue(_preserved_edge_support_vertex(point,position,tile,self.tiles))
        for field,value in (('instance_id','different core'),('piece_id','hsr-component-lower-paired-straight')):
            changed=deepcopy(self.tiles);changed[96.,32.][field]=value
            self.assertFalse(_preserved_edge_support_vertex(point,position,changed[position],changed))
        changed=deepcopy(self.tiles);changed[position]['resources']['model_0']+=b'\0'
        self.assertFalse(_preserved_edge_support_vertex(point,position,changed[position],changed))
        self.assertFalse(_preserved_edge_support_vertex((-8.7,10.,-2.,.035,.5),position,tile,self.tiles))



class HistoricalRedesignSavedResourceControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build,cls.tiles,cls.descriptor=saved_historical()
        cls.record=read_frozen_rework_record()
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
        build, _, _ = saved_current()
        report=verify(build['path'])
        self.assertEqual(report['status'],'passed')
        self.assertEqual(report['geometry']['strict_byte_identity_cells'],len(resource_descriptor(RESOURCES_PATH)['world_cells']))
        self.assertEqual(len(report['encoded_paths']['proper_rotations']),4)
        self.assertEqual(report['supports']['total_column_positions'],74)
        self.assertEqual(report['supports']['unchanged_support_positions'],59)
        self.assertEqual(report['encoded_paths']['whole_route_quality']['complete_journeys_checked'],6)
        self.assertFalse(report['deleted_predecessor_resource_inputs_required'])


class EncodedTrumpetModuleTests(unittest.TestCase):
    def encoded(self, identifier):
        folder = piece_folder(identifier)
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
        build, _, _ = saved_historical()
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
