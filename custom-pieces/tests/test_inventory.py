"""Draft artwork must not produce a broken linked inventory image."""
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch
from scp.inventory import write_inventories
from scp.content import split_markdown_metadata


class InventoryArtworkTests(unittest.TestCase):
    def test_assembly_human_titles_preserve_ids_paths_and_missing_title_fallback(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);domain=root/'domains/fixture';domain.mkdir(parents=True)
            assemblies=[]
            for identifier,title in (('trumpet-stable-id','Straight-stem HSR trumpet'),
                                     ('missing',None),('blank','  '),('invalid',7)):
                local=domain/'01_assemblies'/identifier
                (local/'previews').mkdir(parents=True)
                (local/'previews/preview.png').write_bytes(b'fixture')
                scene={'placements':[]}
                if title is not None:scene['title']=title
                assemblies.append({'id':identifier,'domain':'fixture',
                    'path':f'domains/fixture/01_assemblies/{identifier}','scene':scene})
            catalog={'version':'fixture','domains':{'fixture':{'path':'domains/fixture','name':'Fixture'}},
                     'pieces':[],'piece_sets':{},'_assemblies':assemblies}
            with patch('scp.inventory.load_catalog',return_value=catalog):write_inventories(root)
            text=(domain/'01_assemblies/INVENTORY.md').read_text()
            self.assertIn('[Straight-stem HSR trumpet](trumpet-stable-id/README.md)',text)
            self.assertIn('[![Straight-stem HSR trumpet](trumpet-stable-id/previews/preview.png)](trumpet-stable-id/previews/preview.png)',text)
            self.assertNotIn('[trumpet-stable-id](trumpet-stable-id/README.md)',text)
            for identifier in ('missing','blank','invalid'):
                self.assertIn(f'[{identifier}]({identifier}/README.md)',text)
                self.assertIn(f'[![{identifier}]({identifier}/previews/preview.png)]',text)
            machine=json.loads((domain/'01_assemblies/inventory.json').read_text())['assemblies']
            self.assertEqual(set(machine),{'trumpet-stable-id','missing','blank','invalid'})
            for identifier,status in machine.items():
                self.assertEqual(status['path'],identifier+'/README.md')
                self.assertEqual(status['preview'],identifier+'/previews/preview.png')
                self.assertEqual(status['manual_record'],identifier+'/checks/manual-tests.json')

    def test_linked_thumbnail_requires_both_image_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);domain=root/'domains/fixture';domain.mkdir(parents=True)
            pieces=[]
            for identifier,files in (
                    ('none',()),('only-thumb',('preview-thumb.png',)),
                    ('only-full',('preview.png',)),('complete',('preview.png','preview-thumb.png'))):
                local=domain/'00_pieces'/identifier;(local/'previews').mkdir(parents=True)
                for name in files:(local/'previews'/name).write_bytes(b'fixture')
                pieces.append({'id':identifier,'name':identifier,'domain':'fixture','footprint':[1,1]})
            catalog={'version':'fixture','domains':{'fixture':{'path':'domains/fixture','name':'Fixture'}},
                     'pieces':pieces,'piece_sets':{},'_assemblies':[]}
            with patch('scp.inventory.load_catalog',return_value=catalog):write_inventories(root)
            text=(domain/'00_pieces/INVENTORY.md').read_text()
            header,body=split_markdown_metadata((domain/'README.md').read_text())
            fields={key:json.loads(value) for key,value in (line.split(': ',1) for line in header.splitlines()[1:5])}
            self.assertEqual(fields['title'],'Fixture')
            self.assertEqual(fields['audience'],'players')
            self.assertEqual(fields['document_type'],'guide')
            self.assertTrue(body.startswith('# Fixture\n'))
            self.assertNotIn('Purpose:',body)
            self.assertNotIn('Connection cases',text)
            self.assertNotIn('0/0',text)
            self.assertIn('Legacy endpoint observations remain historical evidence',text)
            self.assertNotIn('Connection cases',(domain/'01_assemblies/INVENTORY.md').read_text())
            self.assertEqual(text.count('Preview pending'),3)
            self.assertIn('[![complete](complete/previews/preview-thumb.png)](complete/previews/preview.png)',text)
            for identifier in ('none','only-thumb','only-full'):
                self.assertNotIn(f'![{identifier}]',text)

    def test_domain_overview_merges_into_authored_readme_and_design_flags_stay_visible(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);domain=root/'domains/fixture';domain.mkdir(parents=True)
            (domain/'README.md').write_text('# My domain\n\nAn authored player guide.\n\n<!-- BEGIN COLLECTIONS -->\nOld counts\n<!-- END COLLECTIONS -->\n\nKeep this exact final paragraph.\n')
            (domain/'INVENTORY.md').write_text('Obsolete overview')
            review={'status':'needs-redesign','summary':'The branch clips its neighbour.',
                    'reasons':['An observed collision needs a layout correction.']}
            piece={'id':'flagged','name':'Flagged example','domain':'fixture','footprint':[1,1],'design_review':review}
            catalog={'version':'fixture','domains':{'fixture':{'path':'domains/fixture','name':'Fixture'}},
                     'pieces':[piece],'piece_sets':{'test-collection':['flagged']},'_assemblies':[]}
            with patch('scp.inventory.load_catalog',return_value=catalog):result=write_inventories(root)
            text=(domain/'README.md').read_text()
            self.assertIn('An authored player guide.',text)
            self.assertTrue(text.endswith('Keep this exact final paragraph.\n'))
            self.assertNotIn('Old counts',text)
            self.assertIn('Individual pieces: 1 menu types',text)
            self.assertIn('`test-collection`: 1 piece types.',text)
            self.assertFalse((domain/'INVENTORY.md').exists())
            self.assertTrue((domain/'inventory.json').is_file())
            self.assertEqual(set(result['written']),{'domains/fixture/00_pieces/INVENTORY.md','domains/fixture/01_assemblies/INVENTORY.md'})
            inventory=(domain/'00_pieces/INVENTORY.md').read_text()
            header,body=inventory.split('---\n',2)[1:]
            metadata={key:json.loads(value) for key,value in (line.split(': ',1) for line in header.strip().splitlines())}
            self.assertEqual(metadata,{'title':'Fixture — individual pieces',
                'summary':'Find each separate menu button, one reusable type image, its connections, and current test coverage.',
                'audience':'players','document_type':'catalogue'})
            self.assertTrue(body.startswith('\n# Fixture — individual pieces\n'))
            self.assertNotIn('Purpose:',body)
            self.assertIn('[NEEDS REDESIGN](flagged/README.md#design-review): The branch clips its neighbour.',inventory)
            with patch('scp.inventory.load_catalog',return_value=catalog):write_inventories(root)
            self.assertEqual(text,(domain/'README.md').read_text())
            self.assertEqual(inventory,(domain/'00_pieces/INVENTORY.md').read_text())


if __name__=='__main__':unittest.main()
