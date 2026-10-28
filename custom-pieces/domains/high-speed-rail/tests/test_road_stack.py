"""Native-resource and mutation tests for the independently authored parallel tile."""
from copy import deepcopy
import json,os,struct,unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from scp import jsonc
from scp.paths import local_settings
from scp.dbpf import entries,decompress,pack_dbpf
from scp.models import parse_s3d,pack_s3d
from scp.track_paths import S3D,PATH
from scp.verify import parse_paths,parse_rules
from scp_hsr.road_stack import build
from scp_hsr.road_stack_verify import check_paths,check_models
from scp_hsr.hsr_connections import materialize,service_classifier

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'project.jsonc').is_file())


class RoadStackClassificationTests(unittest.TestCase):
    def test_reviewed_road_and_sidewalk_classes_keep_distinct_services(self):
        piece={'recipe':'rail_hsr_road_stack'}
        for engine,service in ((1,'road'),(2,'pedestrian')):
            with self.subTest(engine=engine):
                classified=service_classifier(piece,engine,0.)
                self.assertEqual(classified['service_network'],service)
                self.assertEqual(classified['role'],'primary')

    def test_other_piece_families_do_not_inherit_road_classification(self):
        for recipe in ('rail_hsr_diagonal_s_left','hsr_component_modular_crossing_core'):
            for engine in (1,2):
                with self.subTest(recipe=recipe,engine=engine):
                    classified=service_classifier({'recipe':recipe},engine,0.)
                    self.assertEqual(classified['service_network'],f'unresolved-engine-{engine}')
                    self.assertEqual(classified['role'],'unresolved')


class NativeRoadStackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec=json.loads((ROOT/'domains/high-speed-rail/00_pieces/blind-hsr-road-stack/piece.json').read_text())
        settings=jsonc.load(local_settings(ROOT)) if local_settings(ROOT).is_file() else {}
        fixture=Path(os.environ.get('SCP_TEST_NAM_PLUGINS',
                                    settings.get('plugins',ROOT/'local/validation-inputs/Plugins'))).expanduser()
        profile=jsonc.load(ROOT/'config/profiles/nam50-rhd.jsonc')['files']
        names={key:profile[key]['filename'] for key in
               ('hsr','ordinary_road','ordinary_sidewalk_texture')}
        if not all((fixture/name).is_file() for name in names.values()):
            raise unittest.SkipTest('Exact native HSR, ordinary Road PATH, and opaque sidewalk capture are unavailable; supply SCP_TEST_NAM_PLUGINS, local/settings.jsonc, legacy local/settings.json, or local/validation-inputs/Plugins.')
        cls.context={label:{k:decompress(v) for k,v in entries((fixture/name).read_bytes()).items()} for label,name in names.items()}
        generated,cls.rules=build(cls.spec,cls.context)
        # Read the serialized archive, rather than trusting only the in-memory result.
        cls.resources={k:decompress(v) for k,v in entries(pack_dbpf(generated)).items()}
        cls.tile=int(cls.spec['tile_ids'][0],16)

    def path_mutation(self,old,new):
        out=dict(self.resources);out[*PATH,self.tile]=out[*PATH,self.tile].replace(old,new,1);return out

    def model_mutation(self,change):
        out=dict(self.resources);m=parse_s3d(out[*S3D,self.tile]);change(m);raw=pack_s3d(m)
        for z in range(5):out[*S3D,self.tile+z]=raw
        out[*S3D,int(self.spec['preview_id'],16)]=raw
        return out

    def test_saved_resources_match_independent_native_contracts(self):
        self.assertEqual(check_paths(self.resources,self.spec)['native_pedestrian_routes'],6)
        self.assertTrue(check_models(self.resources,self.spec)['exact_native_visible_hsr_mesh'])

    def test_shared_builder_and_verifiers_dispatch_to_the_native_contract(self):
        from scp_hsr.rail_features import build_feature,INFO
        from scp_hsr import rail_feature_verify
        generated,rules=build_feature(self.spec,self.context)
        self.assertEqual(generated,self.resources)
        self.assertEqual(rules,self.rules)
        self.assertIn(self.spec['recipe'],INFO)
        self.assertEqual(rail_feature_verify.check_paths(generated,self.spec),check_paths(generated,self.spec))
        self.assertEqual(rail_feature_verify.check_models(generated,self.spec),check_models(generated,self.spec))
        self.assertEqual(rail_feature_verify.construction_expectations(self.spec)[2],
                         {'a-monorail:0x02000200road:0x02000200'})

    def test_selected_extraction_classifies_each_saved_service(self):
        with TemporaryDirectory() as temporary:
            root=Path(temporary);capture=root/'capture';capture.mkdir()
            (capture/'road.dat').write_bytes(pack_dbpf(self.resources))
            (capture/'manifest.json').write_text(json.dumps({'pieces':[{**self.spec,'asset_file':'road.dat'}]}))
            with patch('scp.catalog.load_catalog',return_value={'pieces':[self.spec]}), \
                    patch('scp.content.refresh_catalog_content',return_value={}) as refresh:
                result=materialize(root,build=capture,piece_ids=[self.spec['id']])
            self.assertEqual(result['extracted_piece_ids'],[self.spec['id']])
            record=refresh.call_args.kwargs['records'][self.spec['id']]
            self.assertEqual({port['service_network'] for port in record['ports']},
                             {'hsr','road','pedestrian'})
            self.assertTrue(all(port['role']=='primary' for port in record['ports']))

    def test_sidewalk_endpoint_substitution_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'route contract'):
            check_paths(self.path_mutation(b'6.39,-8,0',b'6.35,-8,0'),self.spec)

    def test_lower_route_raised_into_hsr_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'route contract'):
            check_paths(self.path_mutation(b'2.5,-8,0',b'2.5,-8,15.5'),self.spec)

    def test_missing_native_pedestrian_access_is_rejected(self):
        out=dict(self.resources);raw=out[*PATH,self.tile]
        start=raw.index(b'-- Native_2_3_2');out[*PATH,self.tile]=raw[:start].replace(b'\r\n10\r\n',b'\r\n9\r\n',1)
        with self.assertRaisesRegex(ValueError,'route contract'):check_paths(out,self.spec)

    def test_narrowed_native_hsr_is_rejected(self):
        def change(m):
            b=m['vertices'][0];raw=bytearray(b['data'])
            for o in range(0,len(raw),b['stride']):
                x=struct.unpack_from('<f',raw,o)[0];struct.pack_into('<f',raw,o,x*.8)
            b['data']=bytes(raw)
        with self.assertRaisesRegex(ValueError,'Native HSR'):check_models(self.model_mutation(change),self.spec)

    def test_shifted_column_into_vehicle_corridor_is_rejected(self):
        def change(m):
            i=m['meshes'][4]['frames'][0][0];b=m['vertices'][i];raw=bytearray(b['data'])
            for o in range(0,len(raw),b['stride']):
                x=struct.unpack_from('<f',raw,o)[0];struct.pack_into('<f',raw,o,x+2.5)
            b['data']=bytes(raw)
        with self.assertRaisesRegex(ValueError,'Support bounds'):check_models(self.model_mutation(change),self.spec)

    def test_missing_support_face_is_rejected(self):
        def change(m):
            pi=m['meshes'][4]['frames'][0][2]
            kind,start,count=m['primitives'][pi][0]
            m['primitives'][pi]=[(kind,start,count-3)]
        with self.assertRaisesRegex(ValueError,'entire closed box'):
            check_models(self.model_mutation(change),self.spec)

    def test_full_saved_support_clearance_is_quantified(self):
        report=check_models(self.resources,self.spec)
        self.assertEqual(report['support_closed_solid_faces_checked'],36)
        self.assertEqual(report['side_pillars'],2)
        self.assertTrue(report['pillar_road_faces_align_pavement_seams'])
        self.assertAlmostEqual(report['clearance_margins_m']['minimum_vehicle_horizontal'],1.,places=6)
        self.assertAlmostEqual(report['clearance_margins_m']['minimum_pedestrian_horizontal'],.04,places=6)
        self.assertAlmostEqual(report['clearance_margins_m']['minimum_lateral_pedestrian_horizontal'],1.1751144546747296,places=6)
        self.assertEqual(report['clearance_margins_m']['minimum_cap_vertical'],9.)

    def test_actual_native_pavement_is_opaque_and_covers_every_pedestrian_route(self):
        from scp.preview import decode_fsh
        from scp.verify import mesh_data
        from scp.models import positions
        atlas=decode_fsh(self.context['ordinary_sidewalk_texture'][0x7ab50e44,0x1abe787d,0x08200004])
        self.assertEqual(atlas.getchannel('A').getextrema(),(255,255))
        model=parse_s3d(self.resources[*S3D,self.tile])
        bands=[mesh_data(model,model['meshes'][index]) for index in (2,3)]
        routes=parse_paths(self.resources[*PATH,self.tile])['routes']
        for route in routes:
            if route['transport']!=2:continue
            for first,second in zip(route['points'],route['points'][1:]):
                samples=[first,second,tuple((a+b)/2 for a,b in zip(first,second))]
                for east,north,height in samples:
                    covering=[]
                    for vertices,_,_,material in bands:
                        points=positions(vertices)
                        if min(p[0] for p in points)<=east<=max(p[0] for p in points):
                            covering.append(material['textures'])
                    self.assertEqual(covering,[[0x08200004]])

    def test_stretching_road_texture_across_its_clipped_band_is_rejected(self):
        def change(m):
            index=m['meshes'][1]['frames'][0][0];block=m['vertices'][index];raw=bytearray(block['data'])
            for offset in range(0,len(raw),block['stride']):
                east=struct.unpack_from('<f',raw,offset)[0]
                struct.pack_into('<f',raw,offset+12,(east+5.)/10.)
            block['data']=bytes(raw)
        with self.assertRaisesRegex(ValueError,'native lane scale'):
            check_models(self.model_mutation(change),self.spec)

    def test_missing_sidewalk_face_is_rejected(self):
        def change(m):
            index=m['meshes'][2]['frames'][0][2];kind,start,count=m['primitives'][index][0]
            m['primitives'][index]=[(kind,start,count-3)]
        with self.assertRaisesRegex(ValueError,'pavement face'):
            check_models(self.model_mutation(change),self.spec)

    def test_replacing_pavement_with_transparent_road_overlay_is_rejected(self):
        def change(m):
            index=m['meshes'][2]['frames'][0][3];material=m['materials'][index]
            material['raw']=material['raw'].replace(struct.pack('<I',0x08200004),struct.pack('<I',0x4b0e))
            material['textures']=[0x4b0e]
        with self.assertRaisesRegex(ValueError,'unaudited material'):
            check_models(self.model_mutation(change),self.spec)

    def test_widening_side_pillars_into_pedestrian_corridors_is_rejected(self):
        def change(m):
            index=m['meshes'][4]['frames'][0][0];block=m['vertices'][index];raw=bytearray(block['data'])
            for offset in range(0,len(raw),block['stride']):
                east=struct.unpack_from('<f',raw,offset)[0]
                struct.pack_into('<f',raw,offset,-5.225+2*(east+5.225))
            block['data']=bytes(raw)
        with self.assertRaisesRegex(ValueError,'Support bounds'):
            check_models(self.model_mutation(change),self.spec)

    def test_wrong_road_texture_is_rejected(self):
        def change(m):
            i=m['meshes'][1]['frames'][0][3];mat=m['materials'][i]
            mat['raw']=mat['raw'].replace(struct.pack('<I',0x4b0e),struct.pack('<I',0x4c0e));mat['textures']=[0x4c0e]
        with self.assertRaisesRegex(ValueError,'unaudited material'):check_models(self.model_mutation(change),self.spec)

    def test_partial_cursor_preview_is_rejected(self):
        out=dict(self.resources);m=parse_s3d(out[*S3D,self.tile]);m['meshes']=m['meshes'][:1]
        out[*S3D,int(self.spec['preview_id'],16)]=pack_s3d(m)
        with self.assertRaisesRegex(ValueError,'Cursor preview'):check_models(out,self.spec)

    def test_saved_rule_clones_have_four_proper_rotations_without_transpose(self):
        rings,sections=parse_rules(self.rules);root=int(self.spec['puzzle_id'],16)
        self.assertEqual(len(sections),8)
        for n in range(1,8):
            fields=dict(sections[root+n*0x10000])
            self.assertNotIn('Transpose',fields)
            self.assertEqual(int(fields['CopyFrom'],0),root if n<4 else root+(n%4)*0x10000)
            if n<4:self.assertEqual(fields['Rotate'],str(n))
        checks=[v for k,v in sections[root] if k=='CheckType']
        self.assertEqual(checks,['a - monorail: 0x02000200 road: 0x02000200'])

    def test_serial_copies_match_all_native_north_south_services_in_four_rotations(self):
        routes=parse_paths(self.resources[*PATH,self.tile])['routes']
        def turn(p,n):
            x,y,z=p
            for _ in range(n):x,y=-y,x
            return tuple(round(v,6) for v in (x,y,z))
        for n in range(4):
            # The second copy is one whole tile north, so occupied plots are disjoint.
            south_ends={(r['transport'],turn(r['points'][-1],n)) for r in routes if r['exit']==1}
            north_starts={(r['transport'],turn((r['points'][0][0],r['points'][0][1]+16,r['points'][0][2]),n)) for r in routes if r['entry']==3}
            north_ends={(r['transport'],turn((r['points'][-1][0],r['points'][-1][1]+16,r['points'][-1][2]),n)) for r in routes if r['exit']==3}
            south_starts={(r['transport'],turn(r['points'][0],n)) for r in routes if r['entry']==1}
            self.assertEqual(south_ends,north_starts);self.assertEqual(north_ends,south_starts)
            self.assertEqual({t for t,p in south_ends},{1,2,7})

if __name__=='__main__':unittest.main()
