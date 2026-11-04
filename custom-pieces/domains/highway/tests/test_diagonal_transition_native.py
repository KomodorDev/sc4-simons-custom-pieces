"""Finite first-cut native source and mixed reused/inserted helper controls."""
from copy import deepcopy
import math
import re
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0,SourcePackages(ROOT))
from scp import jsonc,native_approaches as framework
from scp.dbpf import entries,decompress
from scp.paths import local_settings
from scp_highway import diagonal_transition_native as native
from scp_highway import diagonal_transition_approaches as helpers
from scp_highway import diagonal_transition_layout as layout
from scp_highway import diagonal_transition_variants as variants


def piece(key='original'):
    value=deepcopy(next(row for row in layout.module_catalog()['types'] if row['key']==key))
    value.update(domain='highway',native_diagonal_transition_approaches=True,
                 tile_ids=[f'{0x7FD00000+index*0x100:08x}' for index in range(len(value['cells']))])
    return value


def core_fields(spec):
    width,depth=spec['footprint'];rows=[['.']*(width+2) for _ in range(depth+1)]
    constraints=deepcopy(rows);rows[0][-1]=constraints[0][-1]='<';rows[-1][0]=constraints[-1][0]='^'
    checks=[]
    for index,(x,y) in enumerate(spec['cells']):
        symbol='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[index]
        rows[y][x]=symbol;constraints[y][x]='#';checks.append(f'{symbol} - dirtroad: 0x02000200')
    return {'CellLayout':[''.join(row) for row in rows],'ConsLayout':[''.join(row) for row in constraints],'CheckType':checks}


class DiagonalNativeDeclarationTests(unittest.TestCase):
    def test_portable_native_contract_contains_only_finite_profiles_and_cannot_be_mutably_cached(self):
        report=native.measured_contract()
        self.assertFalse(report['scope']['complete_model_assets_included'])
        for row in report['resources'].values():
            self.assertNotIn('meshes',row['S3D'])
            self.assertIn('mesh_inventory',row['S3D'])
        profiles=native.measured_profiles('dd','original',deck='upper')
        self.assertTrue(profiles)
        self.assertTrue(all('source_parent_ENHUV_sha256' in row and 'parent_triangle' not in row for row in profiles))
        report['resources'].clear()
        self.assertEqual(len(native.measured_contract()['resources']),4)

    def test_exact_first_cut_sockets_keep_fixed_DD_axis_and_separate_side_from_traffic(self):
        expected={
            'original':(0x57530900,0x57030900,(-5,4),0x57030200),
            'mirrored':(0x57530200,0x57030200,(-3,6),0x57030900),
            'opposite-side':(0x57530900,0x57030900,(-3,6),0x57030200),
            'opposite-side-mirrored':(0x57530200,0x57030200,(-5,4),0x57030900)}
        for key,(dd,upper,upper_cell,lower) in expected.items():
            a,b,c=native.socket_specs(key)
            self.assertEqual((a.helper,b.helper,c.helper),((dd,2,(1,0)),(upper,2,upper_cell),(lower,2,(-4,5))))
            self.assertEqual(a.mouth_en,(8.,0.))
            self.assertEqual(b.mouth_en[0]-b.mouth_en[1],40. if upper_cell==(-3,6) else -24.)
            self.assertEqual(c.mouth_en[0]-c.mouth_en[1],8.)
        with self.assertRaises(ValueError):native.socket_specs('alignment-b')

    def test_helpers_round_trip_exact_core_and_reject_owned_or_wrong_marker_cells(self):
        for key in variants.VARIANTS:
            spec=piece(key);original=core_fields(spec)
            rows,checks,cons=helpers.add_approaches(spec,original['CellLayout'],original['CheckType'],original['ConsLayout'])
            reverse=key in ('mirrored','opposite-side-mirrored')
            expected_markers=([0x01000400,0x00000402,0x00000204] if reverse
                              else [0x04000100,0x00000204,0x00000402])
            for text,marker in zip(checks[-3:],expected_markers):
                fields=re.findall(r'\b(dirtroad|monorail):\s*(0x[0-9a-fA-F]{8})(?=\s|,)',text)
                self.assertEqual([(name,int(flags,16)) for name,flags in fields],
                                 [('dirtroad',0x00000301),('monorail',marker)])
                self.assertRegex(text,r',0xFFFFFFFF optional$')
            fields={'CellLayout':rows,'CheckType':checks,'ConsLayout':cons}
            self.assertEqual(helpers.check_construction_approaches(fields,spec),original)
            broken=deepcopy(fields);broken['CheckType'][-1]=broken['CheckType'][-1].replace(' optional','')
            with self.assertRaisesRegex(ValueError,'exact marker'):helpers.check_construction_approaches(broken,spec)
            mixed=deepcopy(spec);mixed['native_orthogonal_approaches']=True
            with self.assertRaisesRegex(ValueError,'Mixed native'):framework.approaches(mixed)

    def test_mixed_existing_ground_subset_does_not_change_legacy_or_conflict_with_either_Y(self):
        for key in variants.VARIANTS:
            spec=piece(key);expected=framework.expected_solution_sections([spec])
            existing=framework._existing_solution_sections([spec])
            self.assertEqual(sum(map(len,expected.values())),12)
            self.assertEqual(sum(map(len,existing.values())),8)
            self.assertEqual({value[0] for table in existing.values() for value in table.values()}, {0x57030200,0x57030900})
        ys=[jsonc.load(path) for path in (ROOT/'domains/highway/00_pieces').glob('ddrhw-y-*/piece.jsonc')]
        selected=[*ys,*(piece(key) for key in variants.VARIANTS)]
        self.assertEqual(sum(map(len,framework.expected_solution_sections(selected).values())),20)
        for spec in ({'domain':'highway'},{'native_diagonal_transition_approaches':False}):
            self.assertEqual(framework.approaches(spec),[])
        broken=piece();broken['id']+='-unreviewed'
        with self.assertRaises(ValueError):framework.approaches(broken)


class ActualDiagonalNativeInputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings=local_settings(ROOT)
        if not settings.is_file():raise unittest.SkipTest('Original NAM50 native inputs are not supplied in a source-only clone')
        settings=jsonc.load(settings);roots=[Path(settings['plugins']).expanduser(),*(Path(p).expanduser() for p in settings.get('extra_plugins',[]))]
        cls.context={}
        for label,name in [('dd_rhw','RealHighway_DD_RHW-4.dat'),('rhw4','RealHighway_RHW-4.dat'),('controller','NetworkAddonMod_Controller.dat')]:
            found={p for root in roots if root.is_dir() for p in root.rglob(name)}
            if len(found)!=1:raise unittest.SkipTest('Exactly one original '+name+' is required')
            cls.context[label]={key:decompress(raw) for key,raw in entries(found.pop().read_bytes()).items()}

    def test_actual_pins_ground_reuse_and_native_exemplar_model_references(self):
        result=helpers.check_native_continuation(self.context['controller'])
        self.assertEqual(result['existing_native_diagonal_ground_solutions_checked'],8)
        resources={key:value for source in self.context.values() for key,value in source.items()}
        checked=framework.dependency_records([piece()],resources)
        self.assertEqual(len(checked),12)
        for target,expected in [(0x57530200,4),(0x57530900,4),(0x57030200,2),(0x57030900,2)]:
            self.assertEqual(len(native.source_paths(self.context,target)),expected)
            self.assertEqual(native.source_paths(self.context,target),native.source_paths(None,target))
        broken={**self.context,'dd_rhw':{**self.context['dd_rhw'],(*native.S3D,0x57530200):b'wrong source'}}
        with self.assertRaisesRegex(ValueError,'differs from its measured'):native.source_faces(broken,0x57530200)

    def test_actual_rule_composition_inserts_only_DD_rows_and_reuses_every_ground_row(self):
        resources={key:value for source in self.context.values() for key,value in source.items()}
        baseline=self.context['controller'][helpers.RUL1]
        for key in variants.VARIANTS:
            spec=piece(key);raw,proof=framework.compose_rul1(baseline,[spec],resources)
            self.assertEqual(proof['schema_version'],3)
            self.assertEqual(sum(len(section['native_solutions']) for section in proof['sections']),4)
            report=framework.verify_rul1({helpers.RUL1:raw},[spec],{framework.OVERLAY:proof},resources)
            self.assertEqual(report['existing_native_rul1_solutions_reused'],8)
            self.assertEqual(report['native_diagonal_transition_approach_cells_checked'],3)
            self.assertEqual(report['native_ground_rhw_approach_cells_checked'],2)
            self.assertEqual(report['native_dd_rul1_solutions_checked'],4)
            self.assertEqual(report['native_ground_rhw_dependencies_checked'],6)
            self.assertEqual(report['native_dd_dependencies_checked'],6)
        broken=baseline.replace(b'0x04020000,0x03010000,0x57030200',b'0x04020000,0x03010000,0x57030900',1)
        self.assertNotEqual(broken,baseline)
        with self.assertRaises(ValueError):framework.compose_rul1(broken,[piece()],resources)

    def test_all_actual_member_endpoints_match_the_exact_first_socket_planes_and_directions(self):
        for key in variants.VARIANTS:
            for socket in native.socket_specs(key):
                target,pose,cell=socket.helper;routes=native.source_paths(self.context,target,pose,cell)
                endpoints=[point for row in routes for point in (row['points'][0],row['points'][-1])
                           if abs(point[socket.joining_axis]-socket.joining_coordinate)<1e-9]
                self.assertEqual(len(endpoints),4 if socket.arm=='dd' else 2)
                expected_axis=8. if socket.arm!='upper' else (40. if variants.record_for(key).physical_reflection else -24.)
                self.assertTrue(all(abs((point[0]-point[1])-expected_axis) in (4.8,11.2) or
                                    abs(abs((point[0]-point[1])-expected_axis)-3.2)<1e-12 for point in endpoints))
                for route in routes:
                    a,b=route['points'];self.assertAlmostEqual(abs(b[0]-a[0]),abs(b[1]-a[1]),places=12)
                    self.assertEqual(a[2],b[2])

    def test_finite_source_profiles_preserve_distinct_pavement_datums_and_attribute_parents(self):
        roof={}
        for target in (0x57530200,0x57530900):
            groups=native.source_faces(self.context,target)
            roof[target]=min(p[2] for group in groups if group['deck']=='upper' and group['role']=='pavement'
                             for triangle in group['triangles'] for p in triangle)
        self.assertEqual(roof,{0x57530200:15.,0x57530900:15.00100040435791})
        for key in variants.VARIANTS:
            for arm,deck in [('dd','upper'),('dd','lower'),('upper','ground'),('lower','ground')]:
                profiles=native.forward_profiles(self.context,arm,key,deck=deck)
                self.assertTrue(profiles)
                self.assertTrue(all(all(point in row['parent_triangle'] for point in row['points']) for row in profiles))


if __name__=='__main__':unittest.main()
