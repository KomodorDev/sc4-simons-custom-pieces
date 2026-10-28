"""Manual observations remain distinct, scoped, and invalidated by resources."""
from copy import deepcopy
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file()) / 'framework'))
from scp.content import (case_state, fingerprint, new_manual_record, record_software_result,
    record_user_result, refresh_manual_record, render_manual_checklist,
    resource_fingerprints, summarize_manual_record, validate_manual_record, write_subject_content,
    _new_case, compact_manual_record, declare_not_applicable, retire_connection_cases,
    retire_connection_cases_in_catalog)


class ChecklistHTML(HTMLParser):
    """Inspect disclosure visibility and actual link targets in generated Markdown."""
    def __init__(self, text):
        super().__init__()
        self.depth = 0
        self.anchors = []
        self.expanded_anchors = []
        self.open_details = []
        self.links = []
        self.visible = []
        self.group_summaries = []
        self.in_group_summary = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'details':
            self.depth += 1
            self.open_details.append('open' in attrs)
        elif tag == 'summary' and self.depth == 1:
            self.in_group_summary = True
            self.group_summaries.append('')
        elif tag == 'a':
            if 'id' in attrs:
                self.anchors.append(attrs['id'])
                if all(self.open_details):
                    self.expanded_anchors.append(attrs['id'])
            if 'href' in attrs:
                self.links.append((attrs['href'], self.depth))

    def handle_endtag(self, tag):
        if tag == 'details':
            self.depth -= 1
            self.open_details.pop()
        elif tag == 'summary':
            self.in_group_summary = False

    def handle_data(self, data):
        if self.depth == 0:
            self.visible.append(data)
        if self.in_group_summary:
            self.group_summaries[-1] += data


class ManualContentTests(unittest.TestCase):
    def setUp(self):
        self.connections = {'subject_id':'fixture','ports':[
            {'id':'Sin','direction':'in','service_network':'hsr','engine_transport':7,'role':'primary',
             'endpoint_m':[2.,-8.,15.5],'tangent':[0.,1.],'grade':0.,'profile':'native-paired',
             'connection_class':'paired-native-l2-rhd','compatible_counterparts':[
                 {'piece_id':'neighbour','port_id':'Nout','relative_rotation_ccw':90,'relative_position_m':[16.,-16.]}]},
            {'id':'Nout','direction':'out','service_network':'hsr','engine_transport':7,'role':'primary',
             'endpoint_m':[2.,8.,15.5],'tangent':[0.,1.],'grade':0.,'connection_class':'paired-native-l2-rhd'}],
            'journeys':[{'id':'hsr-south-north','service_network':'hsr','role':'primary','entry_port':'Sin','exit_port':'Nout'}],
            'forbidden_transfers':[]}
        self.resources={(0x5ad0e817,0xbadb57f1,1):b'mesh',(0x296678f7,0xa966883f,2):b'path',
                        (0x7ab50e44,0x2bc2759a,3):b'shadow',(0x2026960b,0x123007bb,4):b'name'}
        self.hashes=resource_fingerprints('fixture',self.resources,b'emitted rules')
        self.images={'southeast':fingerprint(b'exact image')}
        self.record=new_manual_record('fixture','piece',self.connections,self.hashes,self.images)
        self.environment={'platform':'macos','game_version':'1.2.1','nam_profile':'NAM 50 RHD'}
    def case(self,kind,**scope):
        return next(c for c in self.record['cases'] if c['kind']==kind and all(c['scope'].get(k)==v for k,v in scope.items()))
    def user_result(self,record,case,**overrides):
        args={'explicit_user_confirmation':True,'reviewer':'User Simon','confirmed_at':'2026-10-19T12:00:00+02:00',
              'evidence':['User explicitly observed this exact test.'],'environment':self.environment}
        args.update(overrides)
        return record_user_result(record,case['id'],'passed',**args)
    def legacy_record(self):
        """Literal old endpoint scopes exercise reading without regenerating them."""
        record=deepcopy(self.record)
        neighbour=resource_fingerprints('neighbour',self.resources,b'neighbour rules')
        record['fingerprints'].update(neighbour)
        for angle,offset in ((0,[16.,-16.]),(270,[-16.,-16.])):
            scope={'subject_id':'fixture','port_id':'Sin','service_network':'hsr','role':'primary',
                'direction':'in','rotation_ccw_degrees':angle,
                'counterpart':deepcopy(self.connections['ports'][0]['compatible_counterparts'][0]),
                'counterpart_rotation_ccw_degrees':(angle+90)%360,
                'counterpart_reference_offset_m':offset,
                'counterpart_reference_offset_tiles_en':[value/16 for value in offset]}
            record['cases'].append(_new_case('in_game_connection','Observe this exact legacy endpoint scope.',scope,
                {**self.hashes,**neighbour}))
        record['cases'].append(_new_case('in_game_connection','No concrete counterpart was established.',
            {'subject_id':'fixture','port_id':'Nout','rotation_ccw_degrees':0,'counterpart':None},self.hashes))
        return record
    def legacy_case(self,record,port='Sin',angle=0):
        return next(case for case in record['cases'] if case['kind']=='in_game_connection'
            and case['scope']['port_id']==port and case['scope']['rotation_ccw_degrees']==angle)
    def large_record(self):
        """Reproduce the blind run's scale without reading or altering its frozen files."""
        connections = deepcopy(self.connections)
        connections['journeys'] = [{'id':f'{service}-journey-{index}', 'service_network':service,
            'entry_port':f'{service}-in-{index}', 'exit_port':f'{service}-out-{index}'}
            for service in ('hsr', 'road') for index in range(5)]
        connections['forbidden_transfers'] = [{'from_service':source, 'to_service':target,
            'from_port':f'{source}-in-{index}', 'to_port':f'{target}-out-{index}',
            'reason':'No directed route exists in the saved PATH graph.'}
            for source,target in (('hsr','road'), ('road','hsr'), ('pedestrian','road'))
            for index in range(18)]
        return new_manual_record('fixture','piece',connections,self.hashes,
            {name:fingerprint(name.encode()) for name in ('southeast','top','connection-overview')})
    def test_defaults_never_infer_manual_or_software_pass(self):
        self.assertTrue(validate_manual_record(self.record))
        summary=summarize_manual_record(self.record)
        self.assertEqual(summary['states']['unverified'],len(self.record['cases']))
        self.assertEqual(summary['states']['passed'],0)
        self.assertEqual({c['scope']['rotation_ccw_degrees'] for c in self.record['cases'] if c['kind']=='in_game_journey'},{0,90,180,270})
        self.assertFalse(any('[x]' in line for line in render_manual_checklist(self.record).splitlines() if line.startswith('| ')))

    def test_final_images_attach_without_regenerating_game_cases_or_restoring_endpoint_matrices(self):
        from scp.content import refresh_image_reviews
        record = self.user_result(self.record, self.case('in_game_journey', rotation_ccw_degrees=0))
        record = self.user_result(record, self.case('preview_review'))
        record = compact_manual_record(record)
        original = deepcopy(record)
        updated = refresh_image_reviews(record, {**self.images, 'canonical-top': fingerprint(b'top'),
                                                 'connection-overview': fingerprint(b'cards')})
        self.assertEqual(record, original)
        self.assertEqual([case for case in updated['cases'] if case['kind'] != 'preview_review'],
                         [case for case in record['cases'] if case['kind'] != 'preview_review'])
        self.assertTrue(record['dependency_sets'].items() <= updated['dependency_sets'].items())
        self.assertFalse(any(case['kind'] == 'in_game_connection' for case in updated['cases']))
        summary = summarize_manual_record(updated)
        self.assertEqual({key: value for key, value in summary['by_kind']['preview_review'].items() if value}, {'passed': 1, 'unverified': 2})
        self.assertEqual(refresh_image_reviews(updated, {**self.images, 'canonical-top': fingerprint(b'top'),
                                                         'connection-overview': fingerprint(b'cards')}), updated)
        changed = refresh_image_reviews(updated, {**self.images, 'canonical-top': fingerprint(b'top'),
                                                  'connection-overview': fingerprint(b'new cards')})
        self.assertEqual([case for case in changed['cases'] if case['kind'] != 'preview_review'],
                         [case for case in record['cases'] if case['kind'] != 'preview_review'])

    def test_changed_and_removed_image_reviews_preserve_observation_history(self):
        from scp.content import refresh_image_reviews
        observed = self.user_result(self.record, self.case('preview_review'))
        changed = refresh_image_reviews(compact_manual_record(observed), {'southeast': fingerprint(b'new image')})
        self.assertEqual(summarize_manual_record(changed)['by_kind']['preview_review']['stale'], 1)
        self.assertEqual(next(c for c in changed['cases'] if c['kind'] == 'preview_review')['observations'],
                         next(c for c in observed['cases'] if c['kind'] == 'preview_review')['observations'])
        missing = refresh_image_reviews(changed, {})
        self.assertEqual(summarize_manual_record(missing)['by_kind']['preview_review']['unverified'], 1)
        self.assertEqual(len(missing['removed_cases']), 1)
        self.assertEqual(missing['removed_cases'][0]['observations'],
                         next(c for c in observed['cases'] if c['kind'] == 'preview_review')['observations'])
        restored = refresh_image_reviews(missing, {'southeast': self.images['southeast']})
        self.assertEqual(summarize_manual_record(restored)['by_kind']['preview_review']['passed'], 1)
        self.assertFalse(restored.get('removed_cases'))

    def test_scoped_final_image_handoff_preserves_raw_measurements_and_other_subjects(self):
        from scp.content import refresh_image_reviews_in_catalog, piece_preview_hashes
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            pieces = [{'id': key, 'domain': 'hsr', 'name': key} for key in ('fixture', 'other')]
            directories = {}
            for piece in pieces:
                directory = root/'domains/hsr/00_pieces'/piece['id']
                directories[piece['id']] = directory
                connections = deepcopy(self.connections)
                connections['subject_id'] = piece['id']
                write_subject_content(directory, {**piece, 'kind': 'piece'}, connections, self.hashes)
            directory = directories['fixture']
            before = (directory/'connections.json').read_bytes()
            (directory/'previews').mkdir(exist_ok=True)
            for name in ('previews/preview.png', 'previews/preview-top.png', 'previews/connection-overview.png', 'previews/preview-thumb.png'):
                (directory/name).write_bytes(name.encode())
            self.assertEqual(set(piece_preview_hashes(directory)),
                             {'canonical-southeast', 'canonical-top', 'connection-overview'})
            untouched = {path: path.read_bytes() for path in directories['other'].rglob('*') if path.is_file()}
            catalog = {'pieces': pieces, 'domains': {'hsr': {'path': 'domains/hsr'}}, '_assemblies': []}
            with patch('scp.catalog.load_catalog', return_value=catalog):
                result = refresh_image_reviews_in_catalog(root, piece_ids=['fixture'])
                self.assertEqual(result['manual_observations_added'], 0)
                self.assertEqual(len(result['subjects'][0]['image_roles']), 3)
                snapshot = {path: path.read_bytes() for path in directory.rglob('*') if path.is_file()}
                repeat = refresh_image_reviews_in_catalog(root, piece_ids=['fixture'])
                self.assertFalse(repeat['subjects'][0]['record_changed'])
                self.assertEqual(snapshot, {path: path.read_bytes() for path in snapshot})
                with self.assertRaisesRegex(ValueError, 'Unknown piece selection'):
                    refresh_image_reviews_in_catalog(root, piece_ids=['fixture', 'missing'])
                self.assertEqual(snapshot, {path: path.read_bytes() for path in snapshot})
            self.assertEqual((directory/'connections.json').read_bytes(), before)
            self.assertEqual(untouched, {path: path.read_bytes() for path in untouched})
    def test_endpoint_candidate_growth_does_not_create_cases_or_dependencies(self):
        changed=deepcopy(self.connections)
        changed['ports'][0]['compatible_counterparts'] *= 12
        for target in changed['ports'][0]['compatible_counterparts']:
            target['resource_keys']=['path:neighbour:legacy']
        fresh=new_manual_record('fixture','piece',changed,self.hashes,self.images)
        self.assertEqual(fresh,self.record)
        self.assertFalse(any(case['kind']=='in_game_connection' for case in fresh['cases']))

    def test_retirement_preserves_raw_cases_dependencies_all_observations_and_na_idempotently(self):
        record=self.legacy_record();passed=self.legacy_case(record)
        record=self.user_result(record,passed)
        record=record_user_result(record,passed['id'],'failed',explicit_user_confirmation=True,
            reviewer='Simon',confirmed_at='2026-10-20',evidence=['The exact legacy join failed.'],environment=self.environment)
        na=self.legacy_case(record,angle=270)
        record=declare_not_applicable(record,na['id'],explicit_user_confirmation=True,
            reviewer='Simon',confirmed_at='2026-10-20',reason='This historical pose was explicitly excluded.')
        # Retain a stale observation and its original dependency fingerprint too.
        key=next(key for key in record['fingerprints'] if key.startswith('path:neighbour:'))
        record['fingerprints'][key]=fingerprint(b'revised legacy path')
        for case in record['cases']:
            if key in case['dependencies']:case['dependencies'][key]=record['fingerprints'][key]
        compact=compact_manual_record(record);before=deepcopy(compact)
        output=retire_connection_cases(compact)
        self.assertEqual(compact,before)
        self.assertEqual(output['cases'],[case for case in compact['cases'] if case['kind']!='in_game_connection'])
        self.assertEqual(output['fingerprints'],compact['fingerprints'])
        self.assertEqual(output['dependency_sets'],compact['dependency_sets'])
        meaningful=[case for case in compact['cases'] if case['id'] in (passed['id'],na['id'])]
        self.assertEqual(output['removed_cases'],meaningful)
        self.assertEqual(retire_connection_cases(output),output)
        self.assertEqual(len(output['removed_cases'][0]['observations']),2)
        self.assertFalse(output['removed_cases'][1]['observations'])
        self.assertEqual(summarize_manual_record(output),summarize_manual_record(self.record))
        text=render_manual_checklist(output)
        self.assertIn('Legacy connection history',text)
        self.assertIn('This historical pose was explicitly excluded.',text)
        self.assertIn('The exact legacy join failed.',text)
        self.assertEqual(text.count('id="case-'+passed['id']+'"'),1)
        # A later explicit observation can still name the exact historical ID.
        recorded=self.user_result(output,passed)
        self.assertEqual(len(recorded['removed_cases'][0]['observations']),3)
        self.assertEqual(recorded['cases'],self.record['cases'])

    def test_refresh_archives_explicit_na_with_no_observations(self):
        record=self.legacy_record();case=self.legacy_case(record)
        record=declare_not_applicable(record,case['id'],explicit_user_confirmation=True,
            reviewer='Simon',confirmed_at='2026-10-20',reason='Explicit legacy N/A.')
        output=refresh_manual_record(compact_manual_record(record),self.record)
        self.assertEqual([item['id'] for item in output['removed_cases']],[case['id']])
        self.assertEqual(output['removed_cases'][0]['not_applicable_declaration'],
            next(item for item in record['cases'] if item['id']==case['id'])['not_applicable_declaration'])

    def test_connection_only_retirement_has_no_fake_cases_or_zero_over_zero_status(self):
        record=self.legacy_record();case=self.legacy_case(record)
        record=self.user_result(record,case)
        record['cases']=[item for item in record['cases'] if item['kind']=='in_game_connection']
        output=retire_connection_cases(record)
        self.assertEqual(output['cases'],[])
        self.assertEqual(summarize_manual_record(output)['total'],0)
        with tempfile.TemporaryDirectory() as directory:
            from scp.content import update_manual_summary
            readme=Path(directory)/'README.md';readme.write_text('# Fixture\n')
            update_manual_summary(readme,output)
            text=render_manual_checklist(output,directory=directory)
            self.assertNotIn('0/0',readme.read_text()+text)
            self.assertIn('Legacy connection history',text)
            self.assertFalse((Path(directory)/'checks/observation.example.json').exists())

    def test_selected_retirement_preflights_and_preserves_unselected_records_and_measurements(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);pieces=[];paths={}
            for identifier in ('fixture','other','draft'):
                pieces.append({'id':identifier,'domain':'hsr','name':identifier})
                paths[identifier]=root/'domains/hsr/00_pieces'/identifier
                if identifier=='draft':continue
                local=paths[identifier];(local/'checks').mkdir(parents=True)
                record=self.legacy_record()
                if identifier=='fixture':record=self.user_result(record,self.legacy_case(record))
                record['subject']['id']=identifier
                (local/'checks/manual-tests.json').write_text(json.dumps(compact_manual_record(record),separators=(',',':')))
                (local/'connections.json').write_text(json.dumps(self.connections,separators=(',',':')))
            catalog={'pieces':pieces,'domains':{'hsr':{'path':'domains/hsr','name':'HSR'}},'_assemblies':[]}
            protected=[paths['other']/'checks/manual-tests.json',*(paths[key]/'connections.json' for key in ('fixture','other'))]
            original={path:path.read_bytes() for path in protected}
            with patch('scp.catalog.load_catalog',return_value=catalog),patch('scp.inventory.write_inventories') as inventory:
                with self.assertRaisesRegex(ValueError,'Unknown piece'):
                    retire_connection_cases_in_catalog(root,piece_ids=['fixture','typo'])
                result=retire_connection_cases_in_catalog(root,piece_ids=['fixture','draft'])
                first={path:path.read_bytes() for path in paths['fixture'].rglob('*') if path.is_file()}
                second=retire_connection_cases_in_catalog(root,piece_ids=['fixture','draft'])
                self.assertEqual(first,{path:path.read_bytes() for path in first})
                inventory.assert_not_called()
            self.assertEqual(original,{path:path.read_bytes() for path in protected})
            self.assertEqual(result['subjects'][0]['retired'],3)
            self.assertEqual(result['subjects'][0]['archived'],1)
            self.assertEqual(result['skipped_missing_records'],['draft'])
            self.assertFalse(second['subjects'][0]['record_changed'])
            saved=json.loads((paths['fixture']/'checks/manual-tests.json').read_text())
            self.assertEqual(saved['cases'],[case for case in compact_manual_record(self.legacy_record())['cases'] if case['kind']!='in_game_connection'])
    def test_transposed_states_add_cases_without_mirroring_one_way_counterparts_or_losing_observations(self):
        connections=deepcopy(self.connections)
        connections['supported_orientations']=[{'rotation_ccw_degrees':angle,'construction_transposed':transposed,
            'construction_section_ids':[str(index)]} for transposed in (False,True) for index,angle in enumerate((0,90,180,270))]
        observed=self.user_result(self.record,self.case('in_game_journey',rotation_ccw_degrees=0))
        fresh=refresh_manual_record(observed,new_manual_record('fixture','piece',connections,self.hashes,self.images))
        old={case['id'] for case in self.record['cases']}
        self.assertTrue(old.issubset({case['id'] for case in fresh['cases']}))
        self.assertEqual(summarize_manual_record(fresh)['states']['passed'],1)
        for kind in ('in_game_render','in_game_journey'):
            cases=[case for case in fresh['cases'] if case['kind']==kind]
            self.assertEqual(len(cases),8)
            self.assertEqual(sum(bool(case['scope'].get('construction_transposed')) for case in cases),4)
        self.assertFalse(any(case['kind']=='in_game_connection' for case in fresh['cases']))
        self.assertIn('construction-transposed',fresh['rotation_policy'])
        self.assertEqual(summarize_manual_record(self.record)['by_kind']['in_game_journey']['unverified'],4)
    def test_pass_requires_explicit_identity_date_evidence_and_environment(self):
        case=self.case('in_game_journey',rotation_ccw_degrees=0)
        for overrides in ({'explicit_user_confirmation':False},{'reviewer':''},{'confirmed_at':'today'},{'evidence':[]},{'environment':{'platform':'macos'}}):
            with self.subTest(overrides=overrides),self.assertRaises(ValueError):self.user_result(self.record,case,**overrides)
        output=self.user_result(self.record,case)
        observed=next(c for c in output['cases'] if c['id']==case['id'])
        self.assertEqual(case_state(observed,environment=self.environment),'passed')
        self.assertEqual(case_state(observed,environment={**self.environment,'platform':'windows'}),'unverified')
        self.assertEqual(case_state(self.case('in_game_journey',rotation_ccw_degrees=90)),'unverified')
        self.assertFalse(case['observations'])
    def test_software_cannot_pass_human_cases_and_user_cannot_pass_software(self):
        case=self.case('software_resources')
        output=record_software_result(self.record,case['id'],'passed',verifier='Verifier',checked_at='2026-10-19',evidence=['Actual audit report'])
        summary=summarize_manual_record(output)
        self.assertEqual(summary['by_kind']['software_resources']['passed'],1)
        self.assertEqual(summary['by_kind']['preview_review']['passed'],0)
        self.assertEqual(summary['by_kind']['in_game_journey']['passed'],0)
        with self.assertRaisesRegex(ValueError,'manual'):
            record_software_result(self.record,self.case('preview_review')['id'],'passed',verifier='Renderer',checked_at='2026-10-19',evidence=['PNG exists'])
        with self.assertRaisesRegex(ValueError,'software'):self.user_result(self.record,case)
    def test_invalidation_is_granular_and_excludes_prose_and_paths(self):
        journey=self.case('in_game_journey',rotation_ccw_degrees=0)
        render=self.case('in_game_render',rotation_ccw_degrees=0)
        image=self.case('preview_review')
        output=self.user_result(self.record,journey)
        output=self.user_result(output,render)
        output=self.user_result(output,image)
        prose=deepcopy(self.connections);prose['description']='Moved README path; changed wording'
        fresh=refresh_manual_record(output,new_manual_record('fixture','piece',prose,self.hashes,self.images))
        self.assertEqual(summarize_manual_record(fresh)['states']['passed'],3)
        changed=dict(self.resources);changed[(0x5ad0e817,0xbadb57f1,1)]=b'new mesh'
        fresh=refresh_manual_record(output,new_manual_record('fixture','piece',self.connections,resource_fingerprints('fixture',changed,b'emitted rules'),self.images))
        states={c['id']:case_state(c) for c in fresh['cases']}
        self.assertEqual(states[journey['id']],'passed');self.assertEqual(states[render['id']],'stale');self.assertEqual(states[image['id']],'passed')
        changed[(0x296678f7,0xa966883f,2)]=b'new path'
        fresh=refresh_manual_record(output,new_manual_record('fixture','piece',self.connections,resource_fingerprints('fixture',changed,b'emitted rules'),self.images))
        self.assertEqual(next(case_state(c) for c in fresh['cases'] if c['id']==journey['id']),'stale')
    def test_changed_image_only_stales_that_image_review(self):
        case=self.case('preview_review');output=self.user_result(self.record,case)
        fresh=refresh_manual_record(output,new_manual_record('fixture','piece',self.connections,self.hashes,{'southeast':fingerprint(b'new image')}))
        self.assertEqual(next(case_state(c) for c in fresh['cases'] if c['id']==case['id']),'stale')
        self.assertEqual(summarize_manual_record(fresh)['by_kind']['in_game_render']['unverified'],4)
    def test_assembly_pose_changes_stale_actual_game_checks_without_using_doc_paths(self):
        hashes={**self.hashes,'assembly_pose:fixture':fingerprint([{'piece_id':'fixture','origin_m':[0.,0.]}])}
        record=new_manual_record('fixture','assembly',self.connections,hashes,self.images)
        observed=record
        cases=[next(case for case in record['cases'] if case['kind']==kind) for kind in
               ('in_game_render','in_game_placement','in_game_journey','preview_review')]
        for case in cases:observed=self.user_result(observed,case)
        hashes['assembly_pose:fixture']=fingerprint([{'piece_id':'fixture','origin_m':[16.,0.]}])
        fresh=refresh_manual_record(observed,new_manual_record('fixture','assembly',self.connections,hashes,self.images))
        states={case['id']:case_state(case) for case in fresh['cases']}
        for case in cases:
            self.assertEqual(states[case['id']],'passed' if case['kind']=='preview_review' else 'stale')
    def test_connection_cases_keep_exact_pose_and_require_a_counterpart(self):
        record=self.legacy_record();case=self.legacy_case(record,angle=270)
        self.assertEqual(case['scope']['counterpart_rotation_ccw_degrees'],0)
        self.assertEqual(case['scope']['counterpart']['relative_position_m'],[16.,-16.])
        self.assertEqual(case['scope']['counterpart_reference_offset_m'],[-16.,-16.])
        self.assertEqual(case['scope']['counterpart_reference_offset_tiles_en'],[-1.,-1.])
        with self.assertRaisesRegex(ValueError,'counterpart'):self.user_result(record,self.legacy_case(record,port='Nout'))
    def test_failure_and_explicit_not_applicable_are_not_passes(self):
        case=self.case('in_game_journey',rotation_ccw_degrees=0)
        output=record_user_result(self.record,case['id'],'failed',explicit_user_confirmation=True,reviewer='Simon',confirmed_at='2026-10-19',evidence=['Observed train stop'],environment=self.environment)
        self.assertEqual(summarize_manual_record(output)['states']['failed'],1)
        manual=deepcopy(self.record);manual['cases'][0]['applicability']='not_applicable'
        with self.assertRaisesRegex(ValueError,'reason'):validate_manual_record(manual)
        manual['cases'][0]['not_applicable_reason']='Explicitly outside this platform scope.'
        self.assertEqual(summarize_manual_record(manual)['states']['not_applicable'],1)
        self.assertEqual(summarize_manual_record(manual)['states']['passed'],0)
    def test_dependency_maps_are_compact_without_changing_observation_semantics(self):
        from scp.content import compact_manual_record, record_observation_file
        case=self.case('preview_review');observed=self.user_result(self.record,case)
        compact=compact_manual_record(observed)
        self.assertTrue(compact['dependency_sets'])
        self.assertNotIn('dependencies',compact['cases'][0])
        self.assertEqual(summarize_manual_record(compact),summarize_manual_record(observed))
        self.assertEqual(next(case_state(c) for c in compact['cases'] if c['id']==case['id']),'passed')
        broken=deepcopy(compact);broken['cases'][0]['dependency_snapshot']='0'*64
        with self.assertRaisesRegex(ValueError,'snapshot'):validate_manual_record(broken)
        fresh=refresh_manual_record(compact,self.record)
        self.assertEqual(summarize_manual_record(fresh)['states']['passed'],1)

    def test_counterpart_resource_changes_stale_only_the_exact_connection_scope(self):
        initial=self.legacy_record();connection=self.legacy_case(initial)
        observed=self.user_result(initial,connection)
        changed=dict(initial['fingerprints']);key=next(key for key in changed if key.startswith('path:neighbour:'))
        changed[key]=fingerprint(b'changed neighbour route')
        case=self.legacy_case(observed)
        self.assertEqual(case_state(case,changed),'stale')
        self.assertEqual(case_state(case,initial['fingerprints']),'passed')
        fresh=refresh_manual_record(observed,self.record)
        self.assertEqual(fresh['removed_cases'],[case])
        self.assertNotIn('in_game_connection',summarize_manual_record(fresh)['by_kind'])

    def test_observation_file_requires_confirmation_and_records_only_its_case(self):
        from scp.content import record_observation_file
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            write_subject_content(root,{'id':'fixture','kind':'piece'},self.connections,self.hashes,preview_hashes=self.images)
            record_path=root/'checks/manual-tests.json'
            request=json.loads((root/'checks/observation.example.json').read_text())
            request.update(reviewer='Simon',confirmed_at='2026-10-19',evidence=['The user observed this exact journey'],environment=self.environment)
            request_path=root/'observation.json';request_path.write_text(json.dumps(request))
            original=record_path.read_bytes()
            with self.assertRaisesRegex(ValueError,'Explicit user'):
                record_observation_file(record_path,request_path)
            self.assertEqual(record_path.read_bytes(),original)
            request['explicit_user_confirmation']=True;request_path.write_text(json.dumps(request))
            result=record_observation_file(record_path,request_path)
            self.assertEqual(result['state'],'passed')
            saved=json.loads(record_path.read_text())
            self.assertIn('dependency_sets',saved)
            self.assertEqual(summarize_manual_record(saved)['states']['passed'],1)
            self.assertIn('[x] passed</a>',(root/'TESTING.md').read_text())
            self.assertIn(request['case_id'],(root/'TESTING.md').read_text())

    def test_written_views_preserve_authoritative_observations(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);subject={'id':'fixture','kind':'piece','name':'Fixture menu name','description':'Fixture only.'}
            write_subject_content(root,subject,self.connections,self.hashes,preview_hashes=self.images,write_readme=True)
            path=root/'checks/manual-tests.json';record=json.loads(path.read_text());case=next(c for c in record['cases'] if c['kind']=='preview_review')
            record=self.user_result(record,case);path.write_text(json.dumps(record))
            result=write_subject_content(root,subject,self.connections,self.hashes,preview_hashes=self.images,write_readme=True)
            self.assertEqual(result['summary']['states']['passed'],1)
            self.assertIn('[x] passed</a>',(root/'TESTING.md').read_text())
            self.assertIn('Exact reusable identifier: `fixture`',(root/'README.md').read_text())
            self.assertTrue((root/'connections.json').is_file())

    def test_catalog_refresh_does_not_present_endpoint_candidates_as_compatibility(self):
        from scp.content import refresh_catalog_content
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            domains={key:{'path':'domains/'+key,'name':key} for key in ('hsr','tram')}
            pieces=[{'id':'fixture','domain':'hsr','name':'Fixture'},
                    {'id':'neighbour','domain':'tram','name':'Neighbour'}]
            records={}
            for piece in pieces:
                local=root/domains[piece['domain']]['path']/'00_pieces'/piece['id'];local.mkdir(parents=True)
                record=deepcopy(self.connections);record['subject_id']=piece['id']
                record['source']={'resource_fingerprints':self.hashes}
                record['ports'][0]['compatible_counterparts'].append(
                    {'piece_id':'fixture','port_id':'Nout','relative_rotation_ccw':0,'relative_position_m':[0.,16.]})
                records[piece['id']]=record
            assembly_path='domains/hsr/01_assemblies/fixture-assembly'
            (root/assembly_path).mkdir(parents=True)
            assembly=deepcopy(records['fixture']);assembly['subject_id']='fixture-assembly'
            catalog={'pieces':pieces,'domains':domains,'_assemblies':[
                {'id':'fixture-assembly','domain':'hsr','path':assembly_path,'scene':{}}]}
            with patch('scp.catalog.load_catalog',return_value=catalog), \
                    patch('scp.connectivity.assembly_connectivity',return_value=assembly), \
                    patch('scp.inventory.write_inventories',return_value={}):
                refresh_catalog_content(root,records=records)
            text=(root/'domains/hsr/00_pieces/fixture/TESTING.md').read_text()
            self.assertNotIn('Concrete compatible counterparts',text)
            self.assertNotIn('[neighbour]',text)
            self.assertIn('| `Sin` | hsr / 7 / primary | in |',text)
            self.assertIn('complete joining boundaries',text)
            text=(root/assembly_path/'README.md').read_text()
            self.assertNotIn('[neighbour]',text)
            self.assertNotIn('Concrete compatible counterparts',text)

    def test_scoped_catalog_refresh_uses_read_only_cached_context_and_only_affected_assemblies(self):
        from scp.content import refresh_catalog_content
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);pieces=[];records={};paths={}
            for identifier in ('fixture','cached','draft'):
                piece={'id':identifier,'domain':'hsr','name':identifier}
                pieces.append(piece);paths[identifier]=root/'domains/hsr/00_pieces'/identifier
                if identifier=='draft':continue
                record=deepcopy(self.connections);record['subject_id']=identifier
                hashes=resource_fingerprints(identifier,self.resources,b'fixture rules')
                record['source']={'resource_fingerprints':hashes}
                records[identifier]=record
                write_subject_content(paths[identifier],{**piece,'kind':'piece'},record,hashes)
            # A legacy candidate points to cached resources; it must not make
            # those resources dependencies of a fresh intrinsic piece record.
            records['fixture']['ports'][0]['compatible_counterparts'][0]['resource_keys']=list(records['cached']['source']['resource_fingerprints'])
            assemblies=[]
            for identifier,piece_id in (('affected','fixture'),('untouched','cached')):
                local=root/'domains/hsr/01_assemblies'/identifier
                scene={'placements':[{'piece_id':piece_id,'id':'one'}]}
                assemblies.append({'id':identifier,'domain':'hsr','path':str(local.relative_to(root)),'scene':scene})
                record=deepcopy(records[piece_id]);record['subject_id']=identifier
                write_subject_content(local,{'id':identifier,'kind':'assembly'},record,record['source']['resource_fingerprints'])
                paths[identifier]=local
            catalog={'pieces':pieces,'domains':{'hsr':{'path':'domains/hsr','name':'HSR'}},'_assemblies':assemblies}
            protected=[path for identifier in ('cached','untouched') for path in paths[identifier].rglob('*') if path.is_file()]
            original={path:path.read_bytes() for path in protected}
            def compose(identifier,scene,known,definitions):
                self.assertEqual(set(known),{'fixture','cached'})
                self.assertEqual(known['cached'],records['cached'])
                record=deepcopy(records['fixture']);record['subject_id']=identifier
                return record
            with patch('scp.catalog.load_catalog',return_value=catalog), \
                    patch('scp.connectivity.assembly_connectivity',side_effect=compose) as assembly_call, \
                    patch('scp.inventory.write_inventories',return_value={}):
                result=refresh_catalog_content(root,records={'fixture':records['fixture']},changed_piece_ids={'fixture'})
                assembly_call.assert_called_once()
                self.assertEqual(assembly_call.call_args.args[0],'affected')
                self.assertEqual((result['pieces'],result['assemblies']),(1,1))
                self.assertEqual(result['skipped_missing_records'],['draft'])
                manual=json.loads((paths['fixture']/'checks/manual-tests.json').read_text())
                self.assertFalse(any(':cached' in key for key in manual['fingerprints']))
                self.assertFalse(any(case['kind']=='in_game_connection' for case in manual['cases']))
                snapshot={path:path.read_bytes() for identifier in ('fixture','affected') for path in paths[identifier].rglob('*') if path.is_file()}
                empty=refresh_catalog_content(root,records={},changed_piece_ids=set())
                self.assertEqual((empty['pieces'],empty['assemblies']),(0,0))
                self.assertEqual(snapshot,{path:path.read_bytes() for path in snapshot})
            self.assertEqual(original,{path:path.read_bytes() for path in original})

    def test_top_view_has_its_own_review_and_only_its_changed_image_goes_stale(self):
        from scp.content import piece_preview_hashes
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            (root/'previews').mkdir()
            (root/'previews/preview.png').write_bytes(b'unchanged angled image')
            (root/'previews/preview-top.png').write_bytes(b'first top image')
            images=piece_preview_hashes(root)
            record=new_manual_record('fixture','piece',self.connections,self.hashes,images)
            cases=[case for case in record['cases'] if case['kind']=='preview_review']
            self.assertEqual(len(cases),2)
            for case in cases:
                record=self.user_result(record,case)
            (root/'previews/preview-top.png').write_bytes(b'revised top image')
            fresh=new_manual_record('fixture','piece',self.connections,self.hashes,piece_preview_hashes(root))
            refreshed=refresh_manual_record(record,fresh)
            summary=summarize_manual_record(refreshed)
            self.assertEqual(summary['by_kind']['preview_review']['passed'],1)
            self.assertEqual(summary['by_kind']['preview_review']['stale'],1)
            write_subject_content(root,{'id':'fixture','kind':'piece','name':'Fixture'},
                                  self.connections,self.hashes,preview_hashes=piece_preview_hashes(root))
            self.assertIn('](previews/preview-top.png)',(root/'README.md').read_text())

    def test_forbidden_transfer_view_uses_readable_known_and_unknown_rows(self):
        from scp.content import render_connections
        connections=deepcopy(self.connections)
        connections['forbidden_transfers']=[{'from_port':'Sin','to_port':'Nout',
            'basis':'not reachable in actual saved PATH graph'},{}]
        text=render_connections(connections)
        self.assertIn('| From service / port | To service / port | Reason |',text)
        self.assertIn('| hsr / `Sin` | hsr / `Nout` | No directed route exists',text)
        self.assertIn('In-game confirmation remains unverified.',text)
        self.assertIn('Unresolved service / Unspecified port',text)
        self.assertIn('No reason has been established',text)
        self.assertNotIn("{'from_port':",text)

    def test_manual_workflow_uses_exact_portable_subject_command(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)/'custom-pieces';root.mkdir();(root/'project.jsonc').write_text('{}')
            subject=root/'domains/hsr/00_pieces/fixture'
            write_subject_content(subject,{'id':'fixture','kind':'piece'},self.connections,self.hashes)
            text=(subject/'TESTING.md').read_text()
            relative='custom-pieces/domains/hsr/00_pieces/fixture/checks/'
            self.assertIn('python3 -m scp.content record --record '+relative+'manual-tests.json --observation '+relative+'observation.json',text)
            self.assertIn('../../../../docs/TESTING.md',text)
            self.assertFalse((subject/'checks/README.md').exists())
            self.assertNotIn('/absolute/path',text)
            self.assertNotIn(str(Path(directory)),text)

    def test_piece_consolidation_preserves_authored_sections_and_removes_old_views(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'checks').mkdir()
            subject={'id':'fixture','kind':'piece','name':'Fixture menu name','description':'Fixture only.','footprint':[1,1]}
            legacy='\n'.join(['# Fixture menu name','','Purpose: explain this reusable type, show its exact preview and expose its connection and manual-test coverage.','','Fixture only.','','Exact reusable identifier: `fixture`.','','- [Connections and directed journeys](CONNECTIONS.md)','- [Authoritative manual checks](checks/MANUAL_TESTS.md)','','<!-- BEGIN MANUAL SUMMARY -->','<!-- END MANUAL SUMMARY -->','','## A useful authored example','','Keep this precise authored text.',''])
            (root/'README.md').write_text(legacy)
            for file in ('CONNECTIONS.md','checks/README.md','checks/MANUAL_TESTS.md'):
                (root/file).write_text('Obsolete generated view')
            write_subject_content(root,subject,self.connections,self.hashes,preview_hashes=self.images)
            text=(root/'README.md').read_text()
            self.assertEqual(list(root.rglob('*.md')),[root/'README.md'])
            self.assertIn('## A useful authored example\n\nKeep this precise authored text.',text)
            self.assertNotIn('(CONNECTIONS.md)',text)
            self.assertLess(text.index('BEGIN PIECE OVERVIEW'),text.index('BEGIN MANUAL SUMMARY'))
            self.assertEqual(text.count('Exact reusable identifier:'),1)
            write_subject_content(root,subject,self.connections,self.hashes,preview_hashes=self.images)
            self.assertEqual((root/'README.md').read_text(),text)

    def test_assembly_consolidation_routes_cases_to_testing_and_preserves_authored_text(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            (root/'README.md').write_text('# Assembly\n\nAn exact authored layout.\n')
            (root/'TESTING.md').write_text('# Assembly tests\n\nAn exact authored procedure.\n')
            write_subject_content(root,{'id':'fixture','kind':'assembly'},self.connections,self.hashes,preview_hashes=self.images)
            readme=(root/'README.md').read_text();tests=(root/'TESTING.md').read_text()
            self.assertEqual({path.name for path in root.rglob('*.md')},{'README.md','TESTING.md'})
            self.assertIn('An exact authored layout.',readme)
            self.assertIn('An exact authored procedure.',tests)
            self.assertIn('TESTING.md#test-checklist',readme)
            self.assertNotIn('BEGIN MANUAL CHECKS',readme)
            self.assertIn('BEGIN MANUAL CHECKS',tests)
            self.assertIn(self.case('in_game_journey',rotation_ccw_degrees=0)['id'],tests)

    def test_compact_matrix_keeps_every_case_pose_environment_and_failed_state(self):
        initial=self.legacy_record()
        observed=self.user_result(initial,self.legacy_case(initial))
        observed=self.user_result(observed,self.legacy_case(initial,angle=270))
        bad=self.case('in_game_journey',rotation_ccw_degrees=90)
        observed=record_user_result(observed,bad['id'],'failed',explicit_user_confirmation=True,
            reviewer='User Simon',confirmed_at='2026-10-20',evidence=['Train stopped at this exact merge'],environment=self.environment)
        text=render_manual_checklist(observed)
        self.assertIn('| General | 0° | 90° | 180° | 270° |',text)
        self.assertNotIn('`{"',text)
        self.assertIn('**0° CCW: passed**',text)
        self.assertIn('[ ] failed</a>',text)
        self.assertIn('Train stopped at this exact merge',text)
        self.assertIn('platform: macos',text)
        self.assertIn('game version: 1.2.1',text)
        self.assertIn('nam profile: NAM 50 RHD',text)
        self.assertIn('counterpart reference offset m: [16.0, -16.0]',text)
        self.assertIn('counterpart reference offset m: [-16.0, -16.0]',text)
        for case in observed['cases']:
            if case['kind']=='in_game_connection' and not case['observations']:
                continue
            self.assertIn('`'+case['id']+'`',text)
            self.assertEqual(text.count('id="case-'+case['id']+'"'),1)
        matrix=[line for line in text.splitlines() if line.startswith('| **')]
        self.assertEqual(sum('**Connection**' in line for line in matrix),0)
        self.assertEqual(sum('**Journey**' in line for line in matrix),1)
        self.assertIn('### Legacy connection history',text)
        self.assertNotIn('in_game_connection',summarize_manual_record(observed)['by_kind'])

    def test_large_checklist_collapses_by_kind_and_service_without_losing_exact_cases(self):
        record = compact_manual_record(self.large_record())
        original = deepcopy(record)
        text = render_manual_checklist(record)
        parsed = ChecklistHTML(text)
        self.assertEqual(len(record['cases']), 277)
        self.assertEqual(sum(case['kind']=='in_game_forbidden_transfer' for case in record['cases']), 216)
        self.assertEqual(record, original)
        self.assertEqual(parsed.depth, 0)
        expected = {'case-'+case['id'] for case in record['cases']}
        self.assertEqual(set(parsed.anchors), expected)
        self.assertEqual(len(parsed.anchors), len(expected))
        self.assertEqual(parsed.expanded_anchors, [])
        self.assertEqual({target[1:] for target,depth in parsed.links}, expected)
        self.assertTrue(all(depth == 1 for _,depth in parsed.links))
        self.assertEqual(len(parsed.group_summaries), 12)
        for pair in ('hsr → road', 'road → hsr', 'pedestrian → road'):
            self.assertIn('Forbidden transfer — '+pair+' — 72 cases; unverified: 72',parsed.group_summaries)
        self.assertNotIn('from port:', ''.join(parsed.visible))
        self.assertNotIn('| Check / exact scope |', ''.join(parsed.visible))
        self.assertIn('Current totals: unverified: 277, passed: 0, failed: 0, stale: 0, not_applicable: 0.', ''.join(parsed.visible))
        for case in record['cases']:
            self.assertIn('`'+case['id']+'`', text)
            transfer = case['scope'].get('forbidden_transfer')
            if transfer:
                self.assertIn('from port: '+transfer['from_port'], text)
                self.assertIn('to port: '+transfer['to_port'], text)
        self.assertNotIn('[x] passed</a>', text)

    def test_failed_and_stale_current_and_historical_scopes_stay_visible_and_linked(self):
        record = self.legacy_record()
        failed = self.case('in_game_journey',rotation_ccw_degrees=90)
        stale = self.case('preview_review')
        old_failed = self.legacy_case(record)
        old_stale = self.legacy_case(record,angle=270)
        for case in (failed,old_failed):
            record = record_user_result(record,case['id'],'failed',explicit_user_confirmation=True,
                reviewer='Precise tester',confirmed_at='2026-10-22',
                evidence=['Failed evidence '+case['id']],environment=self.environment)
        for case in (stale,old_stale):
            record = self.user_result(record,case,evidence=['Original evidence '+case['id']])
        # A newly relevant path dependency leaves this historical observation stale.
        key = 'path:neighbour:additional-member'
        record['fingerprints'][key] = fingerprint(b'additional relevant saved route')
        self.legacy_case(record,angle=270)['dependencies'][key] = record['fingerprints'][key]
        record = retire_connection_cases(record)
        current = dict(record['fingerprints'])
        current['image:fixture:southeast'] = fingerprint(b'changed preview')
        original = deepcopy(record)
        text = render_manual_checklist(record,current)
        parsed = ChecklistHTML(text)
        visible_links = [target for target,depth in parsed.links if depth == 0]
        self.assertEqual(set(visible_links), {'#case-'+case['id'] for case in (failed,stale,old_failed,old_stale)})
        self.assertEqual(len(visible_links), 4)
        self.assertIn('| failed | Current | Journey — Service: hsr;', ''.join(parsed.visible))
        self.assertIn('| stale | Current | Preview review — Image: image:fixture:southeast', ''.join(parsed.visible))
        self.assertEqual(''.join(parsed.visible).count('| Historical |'), 2)
        self.assertIn('| 90° |', ''.join(parsed.visible))
        self.assertIn('| 270° |', ''.join(parsed.visible))
        self.assertIn('counterpart: neighbour / Nout', ''.join(parsed.visible))
        for case in (failed,stale,old_failed,old_stale):
            self.assertEqual(parsed.anchors.count('case-'+case['id']),1)
            self.assertIn('case-'+case['id'],parsed.expanded_anchors)
            self.assertIn(('Failed' if case in (failed,old_failed) else 'Original')+' evidence '+case['id'],text)
        self.assertIn('Precise tester',text)
        self.assertIn('platform: macos',text)
        self.assertIn('game version: 1.2.1',text)
        self.assertIn('nam profile: NAM 50 RHD',text)
        self.assertEqual(record,original)

    def test_grouped_refresh_preserves_frontmatter_authored_blocks_and_record_bytes(self):
        from scp.content import markdown_metadata
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'checks').mkdir()
            record_path = root/'checks/manual-tests.json'
            record_path.write_text(json.dumps(compact_manual_record(self.large_record()),separators=(',',':')))
            connection_path = root/'connections.json'
            connection_path.write_text(json.dumps(self.connections,separators=(',',':')))
            header = markdown_metadata('Exact fixture','Preserved header.','Testers','reference')
            outside = '# Exact fixture\n\nAuthored text stays on one physical line.\n\n<!-- BEGIN CONNECTOR OVERVIEW -->\n\nPreserve this separate generated block.\n\n<!-- END CONNECTOR OVERVIEW -->\n'
            subject = {'id':'fixture','kind':'piece'}
            (root/'README.md').write_text(header+outside)
            records = {path:path.read_bytes() for path in (record_path,connection_path)}
            write_subject_content(root,subject,self.connections,{},refresh_metadata=False)
            first = (root/'README.md').read_bytes()
            write_subject_content(root,subject,self.connections,{},refresh_metadata=False)
            self.assertEqual((root/'README.md').read_bytes(),first)
            self.assertTrue(first.decode().startswith(header+outside))
            self.assertEqual({path:path.read_bytes() for path in records},records)
            text = first.decode()
            self.assertEqual(text.count('<!-- BEGIN MANUAL CHECKS -->'),1)
            self.assertEqual(text.count('<!-- END MANUAL CHECKS -->'),1)
            block = text.split('<!-- BEGIN MANUAL CHECKS -->',1)[1].split('<!-- END MANUAL CHECKS -->',1)[0]
            parsed = ChecklistHTML(block)
            self.assertEqual(len(parsed.anchors),277)
            self.assertEqual(len(parsed.group_summaries),12)

    def test_matrix_keeps_transposed_states_separate_and_exposes_stale_observations(self):
        connections=deepcopy(self.connections)
        connections['supported_orientations']=[{'rotation_ccw_degrees':angle,'construction_transposed':transpose}
            for transpose in (False,True) for angle in (0,90,180,270)]
        record=new_manual_record('fixture','piece',connections,self.hashes,self.images)
        render=next(case for case in record['cases'] if case['kind']=='in_game_render' and
            case['scope']['rotation_ccw_degrees']==90 and case['scope'].get('construction_transposed'))
        observed=self.user_result(record,render)
        changed={**self.hashes}
        model=next(key for key in changed if key.startswith('model:'))
        changed[model]=fingerprint(b'changed native surface')
        fresh=refresh_manual_record(observed,new_manual_record('fixture','piece',connections,changed,self.images))
        text=render_manual_checklist(fresh)
        self.assertIn('| 0° T | 90° T | 180° T | 270° T |',text)
        self.assertIn('[ ] stale</a>',text)
        self.assertIn('**90° CCW with construction Transpose: stale** — `'+render['id']+'`.',text)
        self.assertNotIn('[x] passed</a>',text)
        self.assertNotIn('counterpart pose status:',text)
        for case in fresh['cases']:
            self.assertEqual(text.count('id="case-'+case['id']+'"'),1)

    def test_view_only_refresh_preserves_authoritative_bytes_and_current_observations(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            subject={'id':'fixture','kind':'piece'}
            write_subject_content(root,subject,self.connections,self.hashes,preview_hashes=self.images)
            path=root/'checks/manual-tests.json'
            record=json.loads(path.read_text())
            case=next(c for c in record['cases'] if c['kind']=='preview_review')
            observed=self.user_result(record,case)
            # Non-default JSON formatting makes accidental metadata rewrites visible.
            path.write_text(json.dumps(observed,separators=(',',':')))
            connection_path=root/'connections.json'
            connection_path.write_text(json.dumps(self.connections,separators=(',',':')))
            original={file:file.read_bytes() for file in (path,connection_path)}
            result=write_subject_content(root,subject,self.connections,{},refresh_metadata=False)
            self.assertEqual(result['summary']['states']['passed'],1)
            self.assertEqual({file:file.read_bytes() for file in original},original)
            self.assertIn('[x] passed</a>',(root/'TESTING.md').read_text())

    def test_refresh_manual_unverified_flag_ignores_supported_software_passes(self):
        from scp.content import compact_manual_record,refresh_catalog_content
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);subject=root/'domains/fixture/00_pieces/fixture';subject.mkdir(parents=True)
            # This regression retains a legacy combined journey observation.
            (subject/'README.md').write_text('# Legacy fixture\n\nKeep combined journey coverage.\n')
            connections=deepcopy(self.connections)
            for port in connections['ports']:port['compatible_counterparts']=[]
            connections['source']={'resource_fingerprints':self.hashes}
            catalog={'pieces':[{'id':'fixture','name':'Fixture','domain':'fixture'}],
                'domains':{'fixture':{'path':'domains/fixture','name':'Fixture'}},'_assemblies':[]}
            with patch('scp.catalog.load_catalog',return_value=catalog), \
                    patch('scp.inventory.write_inventories',return_value={}):
                refresh_catalog_content(root,records={'fixture':connections})
                path=subject/'checks/manual-tests.json';record=json.loads(path.read_text())
                case=next(case for case in record['cases'] if case['kind']=='software_resources')
                record=record_software_result(record,case['id'],'passed',verifier='Fixture verifier',
                    checked_at='2026-10-19',evidence=['Explicit fixture resource audit'])
                path.write_text(json.dumps(compact_manual_record(record)))
                self.assertTrue(refresh_catalog_content(root,records={'fixture':connections})['all_new_manual_cases_unverified'])
                record=json.loads(path.read_text());case=next(case for case in record['cases'] if case['kind']=='in_game_journey')
                record=record_user_result(record,case['id'],'failed',explicit_user_confirmation=True,
                    reviewer='Fixture user',confirmed_at='2026-10-19',evidence=['Observed fixture failure'],environment=self.environment)
                path.write_text(json.dumps(compact_manual_record(record)))
                self.assertFalse(refresh_catalog_content(root,records={'fixture':connections})['all_new_manual_cases_unverified'])

if __name__=='__main__':unittest.main()
