"""Portable rail-expansion package tests against the actual encoded DATs.

One temporary build contains the eleven current rail-feature and switch recipes. Mutations update
the affected DAT's declared SHA-256 and remove local donor paths, so semantic
rejections cannot be attributed to an obsolete checksum or a local source.
Nothing is installed, and these tests do not execute SimCity 4.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import sys
import tempfile
import unittest
import zipfile

ROOT=next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.build import build_project,package_build
from scp.catalog import load_catalog
from scp.dbpf import entries,decompress,pack_dbpf
from scp.models import parse_s3d,pack_s3d
from scp.verify import (verify_build,parse_paths,RUL0,NETWORK_INI,S3D,PATH,
                        SHADOW,EXEMPLAR,LTEXT,EFFECT,MENU_EXEMPLAR,ICON,TITLE,DESCRIPTION)


def _paths(parsed):
    """Write inspected fields independently of the feature recipe writer."""
    counts=Counter((r['entry'],r['exit']) for r in parsed['routes'])
    classes=Counter()
    lines=['SC4PATHS','1.2',str(len(parsed['routes'])),'0','0']
    for route in parsed['routes']:
        pair=route['entry'],route['exit']
        classes[pair]+=1
        lane=0 if counts[pair]==1 else classes[pair]
        lines += list(map(str,[route['transport'],lane,route['entry'],route['exit'],
                               route['compatibility'],len(route['points'])]))
        lines += [','.join(format(value,'.12g') for value in point) for point in route['points']]
    return ('\r\n'.join(lines)+'\r\n').encode('ascii')


def _read_dat(path):
    return {key:decompress(value) for key,value in entries(path.read_bytes()).items()}


def _key(point):
    return tuple(round(value,6) for value in point)


def _reachable(resources,piece,start):
    """Follow cell-boundary endpoints read from packaged SC4PATH bytes."""
    graph={}
    for (cx,row),tile in zip(piece['cells'],piece['tile_ids']):
        for route in parse_paths(resources[*PATH,int(tile,16)])['routes']:
            a,b=[_key((point[0]+16*cx,point[1]-16*row,point[2]))
                 for point in (route['points'][0],route['points'][-1])]
            graph.setdefault(a,set()).add(b)
    pending,visited=[_key(start)],set()
    while pending:
        node=pending.pop()
        if node not in visited:
            visited.add(node)
            pending.extend(graph.get(node,set())-visited)
    return visited


class RailPortablePackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local=ROOT/'local/settings.json'
        settings=json.loads(local.read_text()) if local.is_file() else {}
        plugins=os.environ.get('SCP_TEST_NAM_PLUGINS',settings.get('plugins'))
        if not plugins or not Path(plugins).is_dir():
            raise unittest.SkipTest('Audited NAM unavailable; set SCP_TEST_NAM_PLUGINS')
        from scp_hsr.rail_features import RECIPES as FEATURES
        from scp_hsr.rail_repairs import RECIPES as SWITCHES
        current = set(FEATURES) | set(SWITCHES)
        selected = [piece['id'] for piece in load_catalog(ROOT)['pieces'] if piece['recipe'] in current]
        priority=['rail-hsr-adjacent-crossover-right','rail-hsr-adjacent-scissors-revised',
                  'rail-hsr-ghsr-transition','rail-hsr-diagonal-s-left']
        include=priority+[slug for slug in selected if slug not in priority]
        if len(include)!=11 or set(include)!=set(selected):
            raise AssertionError('Expected exactly eleven current rail-feature and switch recipes')
        cls.sandbox=tempfile.TemporaryDirectory(prefix='scp-rail-package-')
        cls.base=Path(cls.sandbox.name).resolve()
        cls.fixture=cls.base/'fixture'
        try:
            build_project(ROOT,plugins,cls.fixture,include=include,extra_roots=settings.get('extra_plugins',[]))
            cls.manifest=json.loads((cls.fixture/'manifest.json').read_text())
            cls.pieces={piece['id']:piece for piece in cls.manifest['pieces']}
        except BaseException:
            cls.sandbox.cleanup()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.sandbox.cleanup()

    def setUp(self):
        self.case=Path(tempfile.mkdtemp(prefix='case-',dir=self.base))
        self.output=self.case/'portable'
        shutil.copytree(self.fixture,self.output)
        (self.output/'input-audit.json').unlink()

    def tearDown(self):
        shutil.rmtree(self.case)

    def mutate_dat(self,relative,mutation):
        path=self.output/relative
        resources=_read_dat(path)
        manifest=json.loads((self.output/'manifest.json').read_text())
        mutation(resources,manifest)
        raw=pack_dbpf(resources)
        path.write_bytes(raw)
        record=next(record for record in manifest['files'] if record['path']==relative)
        record.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
        (self.output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')

    def mutate_piece(self,slug,mutation):
        self.mutate_dat(self.pieces[slug]['asset_file'],mutation)

    def test_portable_archive_has_eleven_menu_roots_all_shadows_and_placement_guide(self):
        report=verify_build(self.output,write_report=False)
        self.assertTrue(report['static_checks_passed'])
        self.assertFalse(report['local_donor_comparison'])
        self.assertEqual(len(self.pieces),11)
        self.assertTrue(all(p['recipe'].startswith('rail_') for p in self.pieces.values()))
        self.assertEqual(report['construction']['separate_piece_menu_roots'],11)
        self.assertEqual(report['construction']['states_per_root'],8)
        self.assertEqual(report['external_shadows'],0)
        self.assertFalse(any(value for key,value in report.items() if key.startswith('in_game_')))
        all_resources={}
        tile_count=0
        for piece in self.pieces.values():
            resources=_read_dat(self.output/piece['asset_file'])
            expected={(*S3D,int(piece['preview_id'],16)),(*EFFECT,int(piece['preview_id'],16))}
            for tile in map(lambda value:int(value,16),piece['tile_ids']):
                expected |= {(*family,tile+zoom) for family in (S3D,SHADOW) for zoom in range(5)}
                expected |= {(*family,tile) for family in (PATH,EXEMPLAR,LTEXT)}
            self.assertEqual(set(resources),expected)
            self.assertFalse(set(all_resources)&set(resources))
            all_resources.update(resources)
            tile_count+=len(piece['tile_ids'])
        self.assertEqual(tile_count,60)
        self.assertEqual(sum(key[:2]==SHADOW for key in all_resources),300)
        folder=Path(next(iter(self.pieces.values()))['asset_file']).parents[1]
        menu=_read_dat(self.output/folder/'10_SCP_Menu.dat')
        self.assertEqual(set(menu),{(*family,int(piece['menu']['id'],16))
            for family in (MENU_EXEMPLAR,ICON,TITLE,DESCRIPTION) for piece in self.pieces.values()})
        controller=_read_dat(self.output/folder/'00_SCP_Controller_NAM50.dat')
        self.assertEqual(set(controller),{RUL0,NETWORK_INI})
        archive=self.case/'rail-expansion.zip'
        package_build(self.output,archive)
        with zipfile.ZipFile(archive) as zipped:
            self.assertNotIn('input-audit.json',zipped.namelist())
            domain='docs/domains/high-speed-rail/'
            self.assertIn(domain+'README.md',zipped.namelist())
            # Player instructions and the shared recording procedure are bundled once.
            self.assertNotIn(domain+'docs/ONE_WAY_HSR.md',zipped.namelist())
            self.assertIn('docs/docs/TESTING.md',zipped.namelist())
            self.assertIn(domain+'00_pieces/INVENTORY.md',zipped.namelist())
            self.assertIn(domain+'01_assemblies/INVENTORY.md',zipped.namelist())
            manifest=json.loads(zipped.read('manifest.json'))
            guide=next(item for item in manifest['documentation'] if item['path']==domain+'README.md')
            raw=zipped.read(guide['path'])
            self.assertEqual(hashlib.sha256(raw).hexdigest(),guide['sha256'])
            self.assertEqual(len(raw),guide['bytes'])
            self.assertIn('HSR',raw.decode('utf8'))
            self.assertIn('GHSR',raw.decode('utf8'))
            for record in manifest['files']:
                self.assertEqual(hashlib.sha256(zipped.read(record['path'])).hexdigest(),record['sha256'])


    def test_empty_origin_s_allocations_match_permanent_ledger_and_controller(self):
        ledger=json.loads((ROOT/'config/allocations.json').read_text())['pieces']
        controller_path=Path(next(iter(self.pieces.values()))['asset_file']).parents[1]/'00_SCP_Controller_NAM50.dat'
        rul=_read_dat(self.output/controller_path)[RUL0].decode('ascii')
        for piece in self.pieces.values():
            if '_diagonal_s_' not in piece['recipe']:
                continue
            reservation=ledger[piece['id']]
            self.assertEqual(piece['cells'],reservation['cells'])
            self.assertEqual(piece['tile_ids'],reservation['tile_ids'])
            x,y=piece['cells'][0]
            self.assertNotEqual((x,y),(0,0))
            first=int(piece['tile_ids'][0],16)
            base=first-x*0x100-y*0x10
            self.assertEqual(base,int(reservation['tile_base'],16))
            puzzle=int(piece['puzzle_id'],16)
            section=rul.split(f'[HighwayIntersectionInfo_0x{puzzle:08X}]',1)[1].split('[',1)[0]
            normalized_base=base+(0x100 if piece['id'].endswith('-left') else 0x10)
            self.assertIn(f'AutoTileBase = 0x{normalized_base:08X}',section)
            self.assertIn(f'PlaceQueryID = 0x{first:08X}',section)
            resources=_read_dat(self.output/piece['asset_file'])
            self.assertNotIn((*PATH,base),resources)

    def test_reversed_crossover_branch_fails_after_hash_and_classes_are_updated(self):
        slug='rail-hsr-adjacent-crossover-right'
        tile=int(self.pieces[slug]['tile_ids'][4],16)
        def mutate(resources,manifest):
            parsed=parse_paths(resources[*PATH,tile])
            route=next(r for r in parsed['routes'] if r['entry']==3 and len(r['points'])>2)
            route['entry'],route['exit']=route['exit'],route['entry']
            route['points'].reverse()
            resources[*PATH,tile]=_paths(parsed)
        self.mutate_piece(slug,mutate)
        with self.assertRaisesRegex(ValueError,'Rail|rail|route|port|path'):
            verify_build(self.output,write_report=False)

    def test_removed_scissors_movement_fails_after_valid_path_count_and_hash_update(self):
        slug='rail-hsr-adjacent-scissors-revised'
        piece=self.pieces[slug]
        tile=int(piece['tile_ids'][piece['cells'].index([0,2])],16)
        def mutate(resources,manifest):
            parsed=parse_paths(resources[*PATH,tile])
            branch=next(route for route in parsed['routes'] if route['entry']==3 and len(route['points'])>2)
            parsed['routes'].remove(branch)
            self.assertGreaterEqual(len(parsed['routes']),2)
            resources[*PATH,tile]=_paths(parsed)
        self.mutate_piece(slug,mutate)
        with self.assertRaisesRegex(ValueError,'Rail|rail|movement|seam|route|path'):
            verify_build(self.output,write_report=False)

    def test_adapter_height_teleport_fails_after_rehashing(self):
        slug='rail-hsr-ghsr-transition'
        tile=int(self.pieces[slug]['tile_ids'][3],16)
        def mutate(resources,manifest):
            parsed=parse_paths(resources[*PATH,tile])
            x,y,height=parsed['routes'][0]['points'][0]
            self.assertGreater(height,1.)
            parsed['routes'][0]['points'][0]=(x,y,1.)
            resources[*PATH,tile]=_paths(parsed)
        self.mutate_piece(slug,mutate)
        with self.assertRaisesRegex(ValueError,'grade|native slope|height|transition'):
            verify_build(self.output,write_report=False)

    def test_changed_diagonal_s_native_port_fails_after_rehashing(self):
        slug='rail-hsr-diagonal-s-left'
        tile=int(self.pieces[slug]['tile_ids'][0],16)
        def mutate(resources,manifest):
            parsed=parse_paths(resources[*PATH,tile])
            route=next(route for route in parsed['routes'] if route['exit']==2)
            x,y,height=route['points'][-1]
            self.assertEqual(x,8.)
            route['points'][-1]=(x,y+.25,height)
            resources[*PATH,tile]=_paths(parsed)
        self.mutate_piece(slug,mutate)
        with self.assertRaisesRegex(ValueError,'native external connection port|port|seam'):
            verify_build(self.output,write_report=False)

    def test_wrong_empty_origin_tile_base_fails_even_when_controller_manifest_agree(self):
        piece=self.pieces['rail-hsr-diagonal-s-left']
        puzzle=int(piece['puzzle_id'],16)
        x,y=piece['cells'][0]
        base=int(piece['tile_ids'][0],16)-x*0x100-y*0x10
        correct_base=base+0x100
        controller=Path(piece['asset_file']).parents[1]/'00_SCP_Controller_NAM50.dat'
        def mutate(resources,manifest):
            suffix=manifest['overlay']['rul0']['suffix']
            pattern=(rf'(\[HighwayIntersectionInfo_0x{puzzle:08X}\][\s\S]*?'
                     rf'AutoTileBase = )0x{correct_base:08X}')
            changed,count=re.subn(pattern,lambda match:match[1]+f'0x{base:08X}',suffix,count=1)
            self.assertEqual(count,1)
            resources[RUL0]=resources[RUL0][:-len(suffix.encode('ascii'))]+changed.encode('ascii')
            manifest['overlay']['rul0']['suffix']=changed
        self.mutate_dat(str(controller),mutate)
        with self.assertRaisesRegex(ValueError,'AutoTileBase|tile|construction|piece asset'):
            verify_build(self.output,write_report=False)

    def test_shifted_mainline_uvs_fail_with_models_preview_and_shadows_consistent(self):
        slug='rail-hsr-adjacent-crossover-right'
        def mutate(resources,manifest):
            for key in list(resources):
                if key[:2]!=S3D:
                    continue
                model=parse_s3d(resources[key])
                for block in model['vertices']:
                    data=bytearray(block['data'])
                    for offset in range(0,len(data),block['stride']):
                        u=struct.unpack_from('<f',data,offset+12)[0]
                        struct.pack_into('<f',data,offset+12,u+.1)
                    block['data']=bytes(data)
                resources[key]=pack_s3d(model)
        self.mutate_piece(slug,mutate)
        with self.assertRaisesRegex(ValueError,'rail texture|texture band|UV'):
            verify_build(self.output,write_report=False)


if __name__=='__main__':
    unittest.main()
