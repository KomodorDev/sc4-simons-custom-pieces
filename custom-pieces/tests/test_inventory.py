"""Draft artwork must not produce a broken linked inventory image."""
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch
from scp import jsonc
from scp.inventory import write_inventories
from scp.content import (fingerprint, new_manual_record, record_software_result,
                         record_user_result, split_markdown_metadata)
from scp.assembly_matrix import MARKER
from scp.markdown_navigation import (NAVIGATION_BEGIN, format_markdown_navigation,
                                     markdown_headings)


class InventoryArtworkTests(unittest.TestCase):
    def test_regeneration_numbers_shared_views_and_leaves_subject_sources_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            domain = root/'domains/fixture'
            domain.mkdir(parents=True)
            (domain/'README.md').write_text(
                '# Fixture\n\nAn authored introduction.\n\n## Reference\n\n'
                '### Values\n\nKeep these exact values.\n\n'
                '<!-- BEGIN COLLECTIONS -->\nOld counts\n<!-- END COLLECTIONS -->\n'
                '\n## Further reading\n\nKeep this exact final paragraph.\n')
            sources = {}
            for kind, identifier, filename in (('00_pieces', 'piece', 'piece.json'),
                                                ('01_assemblies', 'assembly', 'assembly.json')):
                local = domain/kind/identifier
                local.mkdir(parents=True)
                for name, text in (('README.md', '# Subject\n\n## Unnumbered subject heading\n'),
                                   ('TESTING.md', '# Subject checks\n'), (filename, '{"unchanged": true}\n'),
                                   ('connections.json', '{}\n')):
                    file = local/name
                    file.write_text(text)
                    sources[file] = file.read_bytes()
            catalog = {'version': 'fixture', 'domains': {'fixture': {'path': 'domains/fixture', 'name': 'Fixture'}},
                       'pieces': [{'id': 'piece', 'name': 'Piece', 'domain': 'fixture', 'footprint': [1, 1]}],
                       'piece_sets': {}, '_assemblies': [{'id': 'assembly', 'domain': 'fixture',
                           'path': 'domains/fixture/01_assemblies/assembly', 'scene': {'placements': []}}]}
            machine_paths = [domain/'inventory.jsonc', domain/'00_pieces/inventory.jsonc',
                             domain/'01_assemblies/inventory.jsonc']
            prefix = '// title: "Authored inventory"\n// summary: "Keep this explanation."\n/* Retain this note. */\n'
            for path in machine_paths:
                path.write_text(prefix+'{}\n', encoding='utf-8')
            with patch('scp.inventory.load_catalog', return_value=catalog):
                write_inventories(root)
            machine_before = {path: path.read_bytes() for path in machine_paths}
            for path in machine_paths:
                self.assertTrue(path.read_text(encoding='utf-8').startswith(prefix))
                self.assertFalse(path.with_suffix('.json').exists())
            paths = [domain/'README.md', domain/'00_pieces/INVENTORY.md', domain/'01_assemblies/INVENTORY.md']
            first = {path: path.read_text() for path in paths}
            self.assertIn('[1. Reference](#1-reference) · [2. Inventories and collections](#2-inventories-and-collections)'
                          ' · [3. Further reading](#3-further-reading)', first[paths[0]])
            self.assertIn('### 1.1 Values\n', first[paths[0]])
            self.assertIn('<a id="reference"></a>', first[paths[0]])
            self.assertEqual([heading.title for heading in markdown_headings(first[paths[1]]) if heading.level == 2],
                             ['1. Individual pieces'])
            self.assertEqual([heading.title for heading in markdown_headings(first[paths[2]]) if heading.level > 1],
                             ['1. Legend', '1.1 Where the results come from', '1.2 How to read the results',
                              '2. Assembly blueprints'])
            for text in first.values():
                self.assertEqual(text.count(NAVIGATION_BEGIN), 1)
                self.assertEqual(format_markdown_navigation(text), text)
            with patch('scp.inventory.load_catalog', return_value=catalog):
                write_inventories(root)
            self.assertEqual(first, {path: path.read_text() for path in paths})
            self.assertEqual(machine_before, {path: path.read_bytes() for path in machine_paths})
            self.assertEqual(sources, {file: file.read_bytes() for file in sources})

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
            machine=jsonc.loads((domain/'01_assemblies/inventory.jsonc').read_text())['assemblies']
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
            self.assertTrue((domain/'inventory.jsonc').is_file())
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


class AssemblyInventoryEvidenceTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.domain = self.root/'domains/fixture'
        self.local = self.domain/'01_assemblies/fixture'
        (self.local/'checks').mkdir(parents=True)
        self.readme = self.local/'README.md'
        self.readme.write_text(f'# Fixture\n\n<!-- BEGIN {MARKER} -->\nAll tests passed: ✅\n<!-- END {MARKER} -->\n')
        (self.local/'TESTING.md').write_text('Every preview and game check passed: [x].\n')
        self.connections = {
            'subject_id': 'fixture', 'software_status': {'path_extraction': 'passed'},
            'ports': [{'id': identifier, 'direction': direction, 'service_network': 'hsr'}
                      for identifier, direction in (('W.in', 'in'), ('E.out', 'out'), ('W.out', 'out'))],
            'journeys': [{'id': 'west-east', 'entry_port': 'W.in', 'exit_port': 'E.out',
                          'service_network': 'hsr', 'role': 'primary'}],
            'forbidden_transfers': [{'from_port': 'W.in', 'to_port': 'W.out',
                                     'from_service': 'hsr', 'to_service': 'hsr'}],
        }
        self.record = new_manual_record('fixture', 'assembly', self.connections,
            {'path:fixture:one': fingerprint(b'fixture path'), 'model:fixture:one': fingerprint(b'fixture model')},
            {'preview.png': fingerprint(b'fixture image')}, split_journey_observations=True,
            manual_check_orientations=[{'rotation_ccw_degrees': 0}])
        case = next(case for case in self.record['cases'] if case['kind'] == 'software_connectivity')
        self.record = record_software_result(self.record, case['id'], 'passed', verifier='Fixture verifier',
            checked_at='2026-10-27T10:00:00Z', evidence=['Fixture-only software result.'])
        self.catalog = {'version': 'fixture', 'domains': {'fixture': {'path': 'domains/fixture', 'name': 'Fixture'}},
                        'pieces': [], 'piece_sets': {}, '_assemblies': [
                            {'id': 'fixture', 'domain': 'fixture', 'path': 'domains/fixture/01_assemblies/fixture',
                             'scene': {'placements': []}}]}

    def generate(self):
        (self.local/'connections.json').write_text(json.dumps(self.connections))
        (self.local/'checks/manual-tests.json').write_text(json.dumps(self.record))
        with patch('scp.inventory.load_catalog', return_value=self.catalog):
            write_inventories(self.root)
        return (self.domain/'01_assemblies/INVENTORY.md').read_text()

    def observe(self, kind, result='passed'):
        case = next(case for case in self.record['cases'] if case['kind'] == kind)
        self.record = record_user_result(self.record, case['id'], result, explicit_user_confirmation=True,
            reviewer='Fixture reviewer', confirmed_at='2026-10-27T10:01:00Z',
            evidence=['Fixture-only explicit observation.'],
            environment={'platform': 'fixture OS', 'game_version': 'fixture version', 'nam_profile': 'fixture profile'})

    def test_matrix_summary_uses_current_evidence_and_does_not_parse_markdown(self):
        text = self.generate()
        self.assertIn('| Connection matrix summary |', text)
        self.assertNotIn('| Directed journey cases |', text)
        self.assertIn('[Open matrix](fixture/README.md#4-connection-matrix)', text)
        self.assertIn('Saved PATH: 2/2 confirmed', text)
        self.assertIn('Route Query: 0/1 confirmed; 1 not established', text)
        self.assertIn('Visible travel: 0/1 confirmed; 1 not established', text)
        self.assertIn('Forbidden in game: 0/1 confirmed; 1 not established', text)
        row = text.splitlines()[-1]
        self.assertEqual(row.count('[ ] 0/1 passed; 1 unverified'), 2)
        self.observe('in_game_route_query', 'failed')
        self.assertIn('Route Query: 0/1 confirmed; 1 failed', self.generate())
        self.connections['journeys'][0]['id'] = 'changed-graph'
        self.assertIn('Saved PATH: 0/2 confirmed; 2 not established', self.generate())
        machine = jsonc.loads((self.domain/'01_assemblies/inventory.jsonc').read_text())['assemblies']['fixture']
        self.assertEqual(machine['connection_matrix']['metrics']['saved_path'],
                         {'confirmed': 0, 'failed': 0, 'not_established': 2})

    def test_image_and_game_appearance_read_named_cases_from_json(self):
        self.observe('preview_review')
        self.assertEqual(self.generate().splitlines()[-1].count('[x] 1/1 passed'), 1)
        self.observe('in_game_render')
        text = self.generate()
        self.assertEqual(text.splitlines()[-1].count('[x] 1/1 passed'), 2)
        self.assertIn('Route Query: 0/1 confirmed; 1 not established', text)
        self.assertEqual((self.local/'TESTING.md').read_text(), 'Every preview and game check passed: [x].\n')

    def test_missing_matrix_or_inputs_never_fall_back_to_journey_case_totals(self):
        self.generate()
        for name in ('connections.json', 'checks/manual-tests.json'):
            with self.subTest(missing=name):
                self.generate()
                (self.local/name).unlink()
                with patch('scp.inventory.load_catalog', return_value=self.catalog):
                    write_inventories(self.root)
                text = (self.domain/'01_assemblies/INVENTORY.md').read_text()
                self.assertIn(f'Unverified; {name} missing', text)
                self.assertNotIn('Saved PATH: 2/2 confirmed', text)
        self.readme.write_text('# No matrix opted in\n')
        self.assertIn('No connection matrix declared', self.generate())


if __name__=='__main__':unittest.main()
