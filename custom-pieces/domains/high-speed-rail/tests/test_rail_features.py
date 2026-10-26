"""Grid placement and train movement checks for the rail expansion."""
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import unittest

FRAMEWORK=next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(FRAMEWORK / 'framework'))

from scp_hsr.rail_features import (INFO, RECIPES, PATH, S3D, feature_layout, build_feature,
                               build_rules, native_paths, native_model)
from scp.track_paths import encode_paths,_parse_paths


def spec_for(recipe):
    index=RECIPES.index(recipe)
    info=INFO[recipe]
    base=0x7F50D000+index*0x1000
    return {'id':recipe.replace('_','-'),'name':recipe,'recipe':recipe,
            'puzzle_id':f'{0xF7AF+index:04x}','preview_id':f'{base+0xFF5:08x}',
            'tile_ids':[f'{base+0x100*x+0x10*y:08x}' for x,y in info['cells']],
            'cells':[list(cell) for cell in info['cells']],'footprint':list(info['footprint']),
            'effect_name':f'preview_scp_railnew_{index:07d}'}


def key(point):
    return tuple(round(value,6) for value in point)


def global_routes(recipe,resources=None):
    spec=spec_for(recipe)
    output=[]
    for cell,tile in zip(INFO[recipe]['cells'],spec['tile_ids']):
        if resources is None:
            routes=feature_layout(recipe)[cell]['routes']
            if not routes:
                raise AssertionError('A native fixture needs its actual encoded resources')
            routes=_parse_paths(encode_paths(routes))
        else:
            routes=_parse_paths(resources[*PATH,int(tile,16)])
        for route in routes:
            output.append([(x+16*cell[0],y-16*cell[1],z) for x,y,z in route['points']])
    return output


def reachable(routes,start):
    graph={}
    for points in routes:
        graph.setdefault(key(points[0]),set()).add(key(points[-1]))
    pending=[key(start)]
    seen=set()
    while pending:
        point=pending.pop()
        if point not in seen:
            seen.add(point)
            pending.extend(graph.get(point,set())-seen)
    return seen


def rotate(point,times):
    x,y,z=point
    for _ in range(times%4):
        x,y=y,-x
    return x,y,z


class RailTopologyTests(unittest.TestCase):

    def test_adjacent_switches_keep_both_lines_and_only_declared_transfer_hand(self):
        for level,height in (('hsr',15.5),('ghsr',1.)):
            incoming={'AS':(2,-40,height),'AN':(-2,8,height),
                      'BS':(18,-40,height),'BN':(14,8,height)}
            outgoing={'AS':(-2,-40,height),'AN':(2,8,height),
                      'BS':(14,-40,height),'BN':(18,8,height)}
            straight={('AS','AN'),('AN','AS'),('BS','BN'),('BN','BS')}
            right={('AS','BN'),('BN','AS')}
            left={('BS','AN'),('AN','BS')}
            for suffix,extra in (('crossover_right',right),('crossover_left',left)):
                recipe=f'rail_{level}_adjacent_{suffix}'
                self.assertEqual(INFO[recipe]['footprint'],(2,3))
                for turns in range(4):
                    routes=[[rotate(p,turns) for p in points] for points in global_routes(recipe)]
                    for source,start in incoming.items():
                        reached=reachable(routes,rotate(start,turns))
                        for target,finish in outgoing.items():
                            with self.subTest(recipe=recipe,rotation=turns,source=source,target=target):
                                self.assertEqual(key(rotate(finish,turns)) in reached,
                                                 (source,target) in straight|extra)

    def test_diagonal_shift_joins_exact_native_asymmetric_ports_in_both_directions(self):
        for level,height in (('hsr',15.5),('ghsr',1.)):
            for side in ('left','right'):
                recipe=f'rail_{level}_diagonal_s_{side}'
                start_x,end_y=(16.,0.) if side=='left' else (0.,-16.)
                forward_in=(start_x+2.9,-40,height)
                forward_out=(40,end_y-2.8,height)
                reverse_in=(40,end_y+2.9,height)
                reverse_out=(start_x-2.9,-40,height)
                for turns in range(4):
                    routes=[[rotate(p,turns) for p in points] for points in global_routes(recipe)]
                    self.assertIn(key(rotate(forward_out,turns)),reachable(routes,rotate(forward_in,turns)))
                    self.assertIn(key(rotate(reverse_out,turns)),reachable(routes,rotate(reverse_in,turns)))
                    self.assertNotIn(key(rotate(reverse_out,turns)),reachable(routes,rotate(forward_in,turns)))
                # Lines retain NE heading but change x-y by one 16 m grid step.
                self.assertEqual((40-end_y)-(start_x+40),-16 if side=='left' else 16)

    def test_shared_internal_routes_are_exact_and_canonical_classes_are_unique(self):
        for recipe in RECIPES[:-1]:
            starts,ends=Counter(),Counter()
            for points in global_routes(recipe):
                starts[key(points[0])]+=1
                ends[key(points[-1])]+=1
                self.assertTrue(all(all(math.isfinite(value) for value in p) for p in points))
                self.assertTrue(all(math.dist(a,b)>1e-8 for a,b in zip(points,points[1:])))
            external_count=4 if '_diagonal_s_' in recipe else 8
            self.assertEqual(len((starts.keys()-ends.keys())|(ends.keys()-starts.keys())),external_count)
            for data in feature_layout(recipe).values():
                routes=_parse_paths(encode_paths(data['routes']))
                identities=[(r['entry'],r['exit'],r['class']) for r in routes]
                self.assertEqual(len(identities),len(set(identities)))
                self.assertTrue(all(r['entry']!=r['exit'] and r['transport']==7 for r in routes))

    def test_sparse_empty_origin_keeps_real_query_tile_and_grid_base(self):
        for recipe,base in zip(RECIPES[:4],(0x7F50D100,0x7F50E010,0x7F50F100,0x7F510010)):
            spec=spec_for(recipe)
            first=INFO[recipe]['cells'][0]
            self.assertNotEqual(first,(0,0))
            rules=build_rules(spec)
            first_tile=int(spec['tile_ids'][0],16)
            self.assertIn(f'AutoTileBase = 0x{base:08X}',rules)
            self.assertIn(f'PlaceQueryID = 0x{first_tile:08X}',rules)
            self.assertEqual(rules.count('CheckType ='),4)

    def test_every_new_ring_has_four_proper_rotations_and_four_clones(self):
        self.assertEqual(len(RECIPES),9)
        for recipe in RECIPES:
            rules=build_rules(spec_for(recipe))
            self.assertEqual(rules.count('[HighwayIntersectionInfo_'),8)
            self.assertEqual(rules.count('Rotate ='),3)
            self.assertNotIn('Transpose',rules)
            self.assertNotIn('RotationRing',rules)
            self.assertEqual(rules.count('CheckType ='),len(INFO[recipe]['cells']))


class NativeRailBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings=json.loads((FRAMEWORK/'local/settings.json').read_text()) if (FRAMEWORK/'local/settings.json').is_file() else {}
        plugins=os.environ.get('SCP_TEST_NAM_PLUGINS',settings.get('plugins'))
        if not plugins or not Path(plugins).is_dir():
            raise unittest.SkipTest('Audited NAM donors unavailable')
        profile=json.loads((FRAMEWORK/'config/profiles/nam50-rhd.json').read_text())['files']['hsr']
        candidates=list(Path(plugins).rglob(profile['filename']))
        if len(candidates)!=1:
            raise RuntimeError('Expected one audited HSR donor')
        raw=candidates[0].read_bytes()
        if hashlib.sha256(raw).hexdigest()!=profile['sha256']:
            raise RuntimeError('HSR donor differs from audited profile')
        from scp.dbpf import entries,decompress
        cls.hsr={k:decompress(v) for k,v in entries(raw).items()}

    def test_native_adapter_all_eight_cells_share_exact_heights_and_both_directions(self):
        recipe='rail_hsr_ghsr_transition'
        spec=spec_for(recipe)
        resources={}
        for row,tile in enumerate(spec['tile_ids']):
            resources[*PATH,int(tile,16)]=encode_paths(native_paths(self.hsr[*PATH,0x5DCF1700+row*0x10]))
        routes=global_routes(recipe,resources)
        self.assertIn(key((2,8,15.5)),reachable(routes,(2,-120,1.)))
        self.assertIn(key((-2,-120,1.)),reachable(routes,(-2,8,15.5)))
        self.assertNotIn(key((-2,-120,1.)),reachable(routes,(2,-120,1.)))
        self.assertTrue(all(abs(b[2]-a[2])<=.629 for path in routes for a,b in zip(path,path[1:])))



if __name__=='__main__':
    unittest.main()
