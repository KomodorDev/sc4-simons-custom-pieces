"""Actual-DAT preview selection, renderer equivalence and portable coverage."""
from copy import deepcopy
import hashlib
import json
import struct
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

from PIL import Image, ImageDraw

ROOT=next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp.dbpf import pack_dbpf
from scp.models import parse_s3d, pack_s3d
from scp.shadows import encode_shadow_fsh
from scp_hsr.test_support import donor
try:
    import numpy as np
    from scp import preview
except ModuleNotFoundError:
    preview=None


@unittest.skipIf(preview is None, 'NumPy preview dependency is unavailable')
class PreviewTitleBindingTests(unittest.TestCase):
    def test_commented_shared_sources_keep_titles_and_invalidate_exact_title_fingerprints(self):
        from scp.catalog import load_catalog
        catalog = load_catalog(ROOT)
        identifier = 'hsr-component-modular-crossing-core'
        piece = next(piece for piece in catalog['pieces'] if piece['id'] == identifier)
        domain = Path(catalog['domains'][piece['domain']]['path'])
        names = [domain/'domain.jsonc', domain/'connector-profiles.jsonc']
        names.extend(domain/'00_pieces'/identifier/name
                     for name in ('piece.json', 'connections.json', 'connector-groups.jsonc'))
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for relative in names:
                target = root/relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT/relative).read_bytes())
            first_title, first_inputs = preview._canonical_title(root, catalog, piece)
            registry = root/domain/'domain.jsonc'
            registry.write_text(registry.read_text()+'\n// A new authoring explanation.\n')
            second_title, second_inputs = preview._canonical_title(root, catalog, piece)
            self.assertEqual(first_title, second_title)
            key = (domain/'domain.jsonc').as_posix()
            self.assertNotEqual(first_inputs[key], second_inputs[key])
            self.assertEqual(second_inputs[key], hashlib.sha256(registry.read_bytes()).hexdigest())
            self.assertEqual(set(first_inputs), {name.as_posix() for name in names})
            for name in names[1:]:
                self.assertEqual(first_inputs[name.as_posix()], second_inputs[name.as_posix()])


@unittest.skipIf(preview is None,'NumPy preview dependency is unavailable')
class PreviewTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.output=self.root/'build';self.output.mkdir()
        self.plugins=self.root/'plugins';self.plugins.mkdir()
        self.images=self.root/'00_pieces';self.index=self.images/'preview-index.json'
        self.guide=self.root/'PREVIEWS.md';self.raw=donor()
        self.piece={'id':'test-piece','name':'Actual Test Piece','recipe':'interchange_oneway_hsr_straight',
            'footprint':[1,1],'tile_ids':['7f500000'],'preview_id':'7f500ff5',
            'asset_file':'pieces/test.dat'}
        self.catalog={'pieces':[preview.piece_spec(self.piece)]}
        atlas=encode_shadow_fsh(Image.new('L',(8,8),255))
        (self.plugins/'original-fixture.dat').write_bytes(pack_dbpf({(*preview.TEXTURE,0x0bf6e09b):atlas}))
        self.write_build(self.raw)

    def write_build(self,raw):
        path=self.output/self.piece['asset_file'];path.parent.mkdir(exist_ok=True)
        dat=pack_dbpf({(*preview.S3D,int(self.piece['preview_id'],16)):raw})
        path.write_bytes(dat)
        # This unrelated archive is intentionally invalid. A selected-model
        # preview must never open it, even though it is in the package manifest.
        (self.output/'unrelated.dat').write_bytes(b'not a DAT')
        manifest={'version':'test','pieces':[self.piece],
            'files':[{'path':self.piece['asset_file'],'sha256':hashlib.sha256(dat).hexdigest()},
                     {'path':'unrelated.dat','sha256':'unused'}]}
        (self.output/'manifest.json').write_text(json.dumps(manifest))

    def render(self,**kwargs):
        with patch('scp.catalog.load_catalog',return_value=self.catalog):
            return preview.render_catalog([self.output],self.plugins,self.images,root=self.root,
                index_path=self.index,**kwargs)

    def test_vectorized_raster_matches_reference_pixels_with_wrapping_and_alpha(self):
        rng=np.random.default_rng(514)
        atlas=rng.random((8,8,4));atlas[:,:,3]=(atlas[:,:,3]>.25).astype(float)
        model=parse_s3d(self.raw);textures={0x0bf6e09b:atlas}
        for azimuth,elevation in ((0,90),(45,36),(130,24)):
            slow=preview.render_view(model,textures,azimuth,elevation,320,240)
            fast=preview.render_fast_view(model,textures,azimuth,elevation,320,240)
            with self.subTest(azimuth=azimuth,elevation=elevation):
                self.assertEqual(slow.tobytes(),fast.tobytes())

    def test_contact_selection_reads_only_the_selected_piece_preview_resource(self):
        with patch.object(preview,'render_contact_sheet',return_value={'models':1}) as contact:
            with patch.object(preview,'read_resource',wraps=preview.read_resource) as read:
                result=preview.render_package(self.output,self.plugins,self.root/'contact.png',piece_ids=['test-piece'])
        self.assertEqual(result,{'models':1})
        items=contact.call_args.args[0]
        self.assertEqual(items[0][0],self.piece['name'])
        self.assertEqual(len(items[0][1]['meshes']),len(parse_s3d(self.raw)['meshes']))
        self.assertNotIn('unrelated.dat',[call.args[0].name for call in read.call_args_list])
        self.assertEqual(read.call_args_list[0].args[1],(*preview.S3D,0x7f500ff5))

    def test_contact_panels_fit_source_names_and_view_purposes_above_complete_models(self):
        names = ['A source-backed reusable piece with a deliberately long descriptive name',
                 'Piece - Already prefixed reusable piece']
        items = [(name, {'source-model': number}) for number, name in enumerate(names)]
        untouched = deepcopy(items)
        model_view = Image.new('RGB', (1200, 1000), '#00ff00')
        with patch.object(preview, 'render_view', return_value=model_view) as render:
            result = preview.render_contact_sheet(items, {}, self.root/'contact.png', title='Component collection')
        self.assertEqual(items, untouched)
        self.assertEqual(len(result['panel_headers']), 2)
        self.assertEqual([call.args[2:] for call in render.call_args_list], [(45,36,1200,1000)]*2)
        with Image.open(self.root/'contact.png') as image:
            for number, header in enumerate(result['panel_headers']):
                self.assertEqual(header['source_name'], names[number])
                self.assertTrue(header['captions'][0].startswith('Piece - '))
                self.assertNotIn('Piece - Piece - ', header['captions'][0])
                self.assertEqual(header['captions'][1],
                                 'Clean view | Southeast view | Authored orientation: 0°')
                left, top, right, bottom = header['viewport_box']
                self.assertEqual(image.crop((left,top,right,bottom)).tobytes(),
                                 Image.new('RGB', (600,500), '#00ff00').tobytes())
                for row in header['rows']:
                    self.assertGreaterEqual(row['bounds'][0], number*640)
                    self.assertLessEqual(row['bounds'][2], (number+1)*640)
                    self.assertLess(row['bounds'][3], top)

    def test_runtime_address_alias_is_rejected_before_reading_a_pretty_preview(self):
        self.piece.update(footprint=[17,2], cells=[[0,0],[16,0],[0,1]],
                          tile_ids=['7f503000','7f504000','7f503010'])
        with patch.object(preview, 'read_resource') as read:
            with self.assertRaisesRegex(ValueError, 'unsafe auto-tile addresses'):
                preview.read_piece_preview(self.output, self.piece)
            read.assert_not_called()

    def test_canonical_evidence_is_local_and_does_not_claim_a_game_test(self):
        self.render()
        evidence=json.loads((self.images/'test-piece/evidence/preview.json').read_text())
        self.assertEqual(evidence['size'],[1600,1200])
        self.assertFalse(evidence['assembly_labels_visible'])
        self.assertFalse(evidence['grid']['origin_marker_visible'])
        self.assertEqual(evidence['renderer']['views'],[{'azimuth':45.,'elevation':31.}])
        self.assertEqual(evidence['renderer']['view_size'],[1600,970])
        self.assertTrue(all(item['tile_index']>=0 for item in evidence['grid']['tile_labels']))
        self.assertEqual(evidence['captions'][-1], 'Software model preview.')
        self.assertNotRegex(' '.join(evidence['captions']).lower(), r'\bunverified\b|\bpassed\b|\bfailed\b')
        self.assertEqual(evidence['header']['rows'][1]['colour'], '#176eaf')
        self.assertEqual(evidence['header']['rows'][0]['text'],'Piece - Actual Test Piece')
        self.assertEqual(evidence['display_title'],evidence['header']['rows'][0]['text'])
        self.assertEqual(evidence['piece_id'],self.piece['id'])
        self.assertEqual(evidence['menu_name'],self.piece['name'])
        self.assertEqual(evidence['file'],'previews/preview.png')
        self.assertEqual(evidence['canonical_filename'],'preview.png')
        self.assertEqual(evidence['thumbnail']['file'],'previews/preview-thumb.png')
        self.assertEqual(evidence['header']['rows'][1]['text'],
                         'Clean view | Southeast view | Authored orientation: 0°')
        index=json.loads(self.index.read_text())
        self.assertEqual(index['pieces'][self.piece['id']]['views']['angled']['display_title'],evidence['display_title'])
        self.assertEqual(index['pieces'][self.piece['id']]['image'],'test-piece/previews/preview.png')
        self.assertEqual(index['pieces'][self.piece['id']]['thumbnail'],'test-piece/previews/preview-thumb.png')
        self.assertFalse(evidence['grid']['tile_scale']['caption_visible'])
        self.assertEqual(sum('1 tile = 16 m' in caption for caption in evidence['captions']), 1)
        self.assertFalse(self.guide.exists(),'No giant legacy preview guide is generated')
        self.assertFalse((self.images/'test-piece/preview.png').exists())
        self.assertFalse((self.images/'test-piece/previews/evidence').exists())

    def test_standalone_top_view_preserves_angle_and_uses_same_complete_saved_model(self):
        self.render()
        directory=self.images/'test-piece'
        preserved={name:(directory/name).read_bytes() for name in
                   ('previews/preview.png','previews/preview-thumb.png','evidence/preview.json')}
        from scp import piece_previews
        with patch.object(piece_previews,'render_piece',wraps=piece_previews.render_piece) as render:
            result=self.render(view_roles=['top'])
        self.assertEqual(result['rendered_views'],1)
        self.assertEqual([call.kwargs['view_role'] for call in render.call_args_list],['top'])
        for name,raw in preserved.items():
            self.assertEqual((directory/name).read_bytes(),raw)
        angle=json.loads(preserved['evidence/preview.json'])
        top=json.loads((directory/'evidence/preview-top.json').read_text())
        self.assertEqual(top['source'],angle['source'])
        self.assertEqual(top['render_model_sha256'],angle['render_model_sha256'])
        self.assertEqual(top['coordinate_system'],angle['coordinate_system'])
        self.assertEqual(top['display_title'],angle['display_title'])
        self.assertEqual(top['view_role'],'top-down')
        self.assertEqual(top['file'],'previews/preview-top.png')
        self.assertEqual(top['camera']['right_s3d'],[1.,0.,-0.])
        self.assertAlmostEqual(top['camera']['up_s3d'][2],-1.)
        self.assertEqual(top['displayed_rotation_ccw_degrees'],0.)
        self.assertIn('Top view, north up',top['captions'][1])
        self.assertEqual(top['captions'][1],'Clean view | Top view, north up | Authored orientation: 0°')
        self.assertEqual(top['header']['rows'][1]['colour'],angle['header']['rows'][1]['colour'])
        self.assertTrue(result['coverage']['complete'])

    def test_standalone_top_tile_edges_remain_green_over_opaque_geometry(self):
        from scp import piece_previews
        # Extend the synthetic deck across interior tile edges, so a background
        # colour change alone cannot satisfy the visible-grid requirement.
        model=parse_s3d(self.raw)
        for block in model['vertices']:
            data=bytearray(block['data'])
            for offset in range(0,len(data),block['stride']):
                for axis_offset in (0,8):
                    value=struct.unpack_from('<f',data,offset+axis_offset)[0]
                    struct.pack_into('<f',data,offset+axis_offset,3*value)
            block['data']=bytes(data)
        raw=pack_s3d(model)
        piece={**self.piece,'cells':[[x,y] for x in range(-1,2) for y in range(-1,2)]}
        library=Mock()
        library.for_model.return_value=({0x0bf6e09b:np.ones((8,8,4))},[])
        captured={}
        def raster(*args,**kwargs):
            image,depth=preview.render_fast_view(*args,**kwargs,return_depth=True)
            captured.update(image=np.asarray(image).copy(),opaque=np.isfinite(depth))
            return image
        for role in ('top','angled'):
            with self.subTest(role=role), patch.object(piece_previews,'render_fast_view',side_effect=raster):
                evidence=piece_previews.render_piece(piece,raw,library,self.images/'grid-test',
                    dat_hash='synthetic-fixture',width=800,height=800,view_role=role)
            x,y=evidence['viewport_offset_xy']
            width,height=evidence['camera']['image_size']
            with Image.open(self.images/'grid-test'/evidence['file']) as bitmap:
                actual=np.asarray(bitmap.crop((x,y,x+width,y+height)))
            if role=='angled':
                np.testing.assert_array_equal(actual,captured['image'])
                self.assertNotIn('line_overlay',evidence['grid'])
                self.assertIsNone(evidence['renderer']['top_grid_overlay'])
                continue
            style=evidence['grid']['line_overlay']
            self.assertEqual(style,{'colour':'#00ff00','line_width_pixels':2,
                                    'major_line_width_pixels':3,'drawn_above_model':True})
            self.assertEqual(evidence['renderer']['top_grid_overlay'],style)
            mask=Image.new('L',(width,height))
            draw=ImageDraw.Draw(mask)
            for line in evidence['grid']['grid_lines']:
                draw.line([tuple(point) for point in line['pixels']],fill=255,
                          width=3 if line['major'] else 2)
            grid_pixels=np.asarray(mask)>0
            self.assertTrue((grid_pixels & captured['opaque']).any())
            self.assertTrue((grid_pixels & ~captured['opaque']).any())
            self.assertTrue(np.all(actual[grid_pixels]==[0,255,0]))
            np.testing.assert_array_equal(actual[~grid_pixels],captured['image'][~grid_pixels])
            self.assertEqual(evidence['source']['model_sha256'],hashlib.sha256(raw).hexdigest())
        self.assertEqual(pack_s3d(model),raw)

    def test_each_requested_view_has_an_independent_freshness_cache(self):
        first=self.render(view_roles=['angled','top'])
        self.assertEqual(first['rendered_views'],2)
        directory=self.images/'test-piece'
        from scp import piece_previews
        with patch.object(piece_previews,'render_piece',wraps=piece_previews.render_piece) as render:
            second=self.render(view_roles=['angled','top'])
        self.assertEqual(second['skipped_unchanged_views'],2)
        render.assert_not_called()
        (directory/'previews/preview-top.png').write_bytes((directory/'previews/preview-top.png').read_bytes()+b'changed artwork')
        index=json.loads(self.index.read_text())
        report=preview.validate_preview_coverage(index,self.catalog['pieces'],self.images,view_roles=['angled','top'])
        self.assertEqual(report['views']['top']['stale'],['test-piece'])
        self.assertEqual(report['views']['angled']['stale'],[])
        with patch.object(piece_previews,'render_piece',wraps=piece_previews.render_piece) as render:
            fixed=self.render(view_roles=['angled','top'])
        self.assertEqual(fixed['rendered_views'],1)
        self.assertEqual([call.kwargs['view_role'] for call in render.call_args_list],['top'])
        self.assertTrue(fixed['coverage']['complete'])

    def test_top_policy_is_explicit_and_invalid_roles_do_not_create_outputs(self):
        self.render()
        self.assertFalse((self.images/'test-piece/previews/preview-top.png').exists())
        index=json.loads(self.index.read_text())
        report=preview.validate_preview_coverage(index,self.catalog['pieces'],self.images,view_roles=['top'])
        self.assertFalse(report['complete'])
        self.assertEqual(report['views']['top']['missing'],['test-piece'])
        for roles in ('top',[],['top','top'],['unsupported']):
            with self.subTest(roles=roles), self.assertRaisesRegex(ValueError,'unique angled/top roles'):
                self.render(view_roles=roles)

    def test_top_only_refresh_cannot_make_an_old_angled_model_appear_current(self):
        self.render(view_roles=['angled','top'])
        image=self.images/'test-piece/previews/preview.png'; original=image.read_bytes()
        model=parse_s3d(self.raw); block=model['vertices'][0]; data=bytearray(block['data'])
        struct.pack_into('<f',data,4,17.25); block['data']=bytes(data)
        self.write_build(pack_s3d(model))
        result=self.render(view_roles=['top'])
        self.assertTrue(result['coverage']['complete'])
        self.assertEqual(image.read_bytes(),original)
        report=preview.validate_preview_coverage(json.loads(self.index.read_text()),self.catalog['pieces'],self.images)
        self.assertEqual(report['stale'],['test-piece'])

    def test_catalog_proves_actual_model_and_resumes_only_unchanged_input_and_image_hashes(self):
        first=self.render();self.assertEqual(first['rendered'],1)
        index=json.loads(self.index.read_text());entry=index['pieces']['test-piece']
        self.assertTrue(index['coverage']['complete'])
        self.assertEqual(entry['preview_sha256'],hashlib.sha256(self.raw).hexdigest())
        self.assertGreater(entry['actual_model_triangles'],0)
        image=self.images/entry['image']
        with Image.open(image) as rendered_image:
            self.assertEqual(rendered_image.size,(1600,1200))
        self.assertNotIn(str(self.plugins),self.index.read_text())
        from scp import piece_previews
        with patch.object(piece_previews,'render_piece',wraps=piece_previews.render_piece) as render:
            second=self.render();self.assertEqual(second['skipped_unchanged'],1);render.assert_not_called()
        changed_model=parse_s3d(self.raw)
        block=changed_model['vertices'][0]
        vertex_data=bytearray(block['data'])
        struct.pack_into('<f',vertex_data,4,16.25)
        block['data']=bytes(vertex_data)
        changed=pack_s3d(changed_model)
        self.write_build(changed)
        self.assertEqual(self.render()['rendered'],1)
        updated=json.loads(self.index.read_text())['pieces']['test-piece']
        self.assertNotEqual(updated['preview_sha256'],entry['preview_sha256'])
        atlas=encode_shadow_fsh(Image.new('L',(8,8),200))
        (self.plugins/'original-fixture.dat').write_bytes(pack_dbpf({(*preview.TEXTURE,0x0bf6e09b):atlas}))
        self.assertEqual(self.render()['rendered'],1)
        atlas_changed=json.loads(self.index.read_text())['pieces']['test-piece']
        self.assertNotEqual(atlas_changed['textures'],updated['textures'])
        # The input is unchanged, but an edited PNG is still regenerated.
        image.write_bytes(image.read_bytes()+b'changed artwork')
        self.assertEqual(self.render()['rendered'],1)
        thumb=self.images/'test-piece/previews/preview-thumb.png'
        thumb.write_bytes(thumb.read_bytes()+b'edited thumbnail')
        self.assertEqual(self.render()['rendered'],1)

    def test_coverage_rejects_changed_catalog_and_missing_or_misassigned_artwork(self):
        self.render();index=json.loads(self.index.read_text())
        changed=deepcopy(self.catalog['pieces']);changed[0]['name']='A different registered name'
        self.assertEqual(preview.validate_preview_coverage(index,changed,self.images)['stale'],['test-piece'])
        tampered=deepcopy(index);tampered['pieces']['test-piece']['actual_model_triangles']=0
        self.assertFalse(preview.validate_preview_coverage(tampered,self.catalog['pieces'],self.images)['complete'])
        tampered=deepcopy(index);tampered['pieces']['test-piece']['image']='menu-icon.png'
        self.assertFalse(preview.validate_preview_coverage(tampered,self.catalog['pieces'],self.images)['complete'])
        (self.images/index['pieces']['test-piece']['image']).unlink()
        self.assertFalse(preview.validate_preview_coverage(index,self.catalog['pieces'],self.images)['complete'])

    def test_coverage_requires_canonical_piece_previews_and_piece_local_evidence(self):
        self.render();index=json.loads(self.index.read_text())
        entry=index['pieces']['test-piece'];record=entry['views']['angled']
        image=self.images/record['image'];thumbnail=self.images/record['thumbnail']
        for image_name,thumbnail_name in (
                ('test-piece/preview.png','test-piece/preview-thumb.png'),
                ('other-piece/previews/preview.png','other-piece/previews/preview-thumb.png'),
                ('test-piece/../test-piece/previews/preview.png','test-piece/previews/preview-thumb.png'),
                (str(image.resolve()),str(thumbnail.resolve())),
                (record['image'],'test-piece/previews/../previews/preview-thumb.png')):
            tampered=deepcopy(index);modified=tampered['pieces']['test-piece']
            modified.update(image=image_name,thumbnail=thumbnail_name)
            modified['views']['angled'].update(image=image_name,thumbnail=thumbnail_name)
            with self.subTest(image=image_name,thumbnail=thumbnail_name):
                self.assertEqual(preview.validate_preview_coverage(tampered,self.catalog['pieces'],self.images)['stale'],['test-piece'])
        evidence=self.images/'test-piece/evidence/preview.json'
        outside=self.root/'outside-evidence.json';outside.write_bytes(evidence.read_bytes())
        evidence.unlink();evidence.symlink_to(outside)
        self.assertEqual(preview.validate_preview_coverage(index,self.catalog['pieces'],self.images)['stale'],['test-piece'])

    def test_review_flag_updates_provenance_and_guide_without_redrawing_unchanged_geometry(self):
        self.render()
        image=self.images/'test-piece/previews/preview.png'
        original=image.read_bytes()
        self.catalog['pieces'][0]['design_review']={
            'status':'needs-redesign','summary':'Rectangular detours need a new layout.',
            'reasons':['The turning route takes an avoidable loop.']}
        from scp import piece_previews
        with patch.object(piece_previews,'render_piece',wraps=piece_previews.render_piece) as render:
            result=self.render()
        self.assertEqual(result['skipped_unchanged'],1)
        render.assert_not_called()
        self.assertEqual(image.read_bytes(),original)
        self.assertFalse(self.guide.exists())
        self.assertTrue(result['coverage']['complete'])
        entry=json.loads(self.index.read_text())['pieces']['test-piece']
        self.assertIn('design_review',entry['catalog_spec'])
        self.assertNotIn('design_review',entry['built_spec'])

    def test_unbuilt_piece_is_explicitly_pending_and_selection_rejects_duplicates(self):
        missing=deepcopy(self.catalog['pieces'][0]);missing.update(id='unbuilt-piece',name='Not Built Yet')
        self.catalog['pieces'].append(missing)
        report=self.render()
        self.assertTrue(report['coverage']['complete'])
        self.assertEqual(report['selected_piece_ids'],['test-piece'])
        self.assertEqual(report['selected_count'],1)
        self.assertEqual(report['coverage']['scope'],'selected_piece_ids_and_requested_views')
        self.assertEqual(report['coverage']['selected_piece_ids'],['test-piece'])
        self.assertEqual(report['catalogue_coverage']['missing'],['unbuilt-piece'])
        self.assertEqual(report['catalogue_coverage']['scope'],'all_registered_piece_ids_and_requested_views')
        self.assertFalse(self.guide.exists())
        self.assertFalse((self.images/'unbuilt-piece/previews/preview.png').exists())
        for ids in (['test-piece','test-piece'],['unknown'],['unbuilt-piece']):
            with self.subTest(ids=ids),self.assertRaisesRegex(ValueError,'duplicate, unknown or unbuilt'):
                self.render(piece_ids=ids)

    def test_explicit_piece_selection_reports_its_own_requested_view_coverage(self):
        outside=deepcopy(self.catalog['pieces'][0]);outside.update(id='outside-selection',name='Outside Selection')
        self.catalog['pieces'].append(outside)
        report=self.render(piece_ids=['test-piece'],view_roles=['angled','top'])
        coverage=report['coverage']
        self.assertTrue(coverage['complete'])
        self.assertEqual(coverage['registered'],1)
        self.assertEqual(coverage['covered'],1)
        self.assertEqual(coverage['missing'],[])
        self.assertEqual(coverage['stale'],[])
        self.assertEqual(coverage['selected_count'],1)
        self.assertEqual(coverage['selected_piece_ids'],['test-piece'])
        self.assertEqual(coverage['requested_views'],['angled','top'])
        self.assertEqual(report['catalogue_coverage']['registered'],2)
        self.assertEqual(report['catalogue_coverage']['missing'],['outside-selection'])
        self.assertFalse((self.images/'outside-selection').exists())

    def test_asset_path_must_remain_inside_the_selected_build(self):
        for asset in ('../outside.dat',str((self.root/'outside.dat').resolve())):
            piece={**self.piece,'asset_file':asset}
            with self.subTest(asset=asset),self.assertRaisesRegex(ValueError,'inside the selected build'):
                preview.read_piece_preview(self.output,piece)


if __name__=='__main__':unittest.main()
