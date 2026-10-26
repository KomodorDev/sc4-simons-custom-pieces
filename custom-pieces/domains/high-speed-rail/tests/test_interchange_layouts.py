"""Directional and physical layout invariants for new interchange modules."""
from collections import Counter
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))

from scp_hsr.interchange_layouts import INFO, RECIPES, interchange_layout
from scp.track_paths import encode_paths,_parse_paths


def key(point):
    return tuple(round(value,6) for value in point)


def routes_for(recipe):
    return encoded_layout_routes(interchange_layout(recipe))


def encoded_layout_routes(layout):
    output=[]
    for (x,row),data in layout.items():
        for route in _parse_paths(encode_paths(data['routes'])):
            output.append([(px+16*x,py-16*row,z) for px,py,z in route['points']])
    return output


def reachable(routes,start):
    graph={}
    for route in routes:
        graph.setdefault(key(route[0]),set()).add(key(route[-1]))
    visited,pending=set(),[key(start)]
    while pending:
        point=pending.pop()
        if point not in visited:
            visited.add(point)
            pending.extend(graph.get(point,set())-visited)
    return visited


def radius(points):
    values=[]
    for a,b,c in zip(points,points[1:],points[2:]):
        ab,bc,ac=math.dist(a[:2],b[:2]),math.dist(b[:2],c[:2]),math.dist(a[:2],c[:2])
        cross=abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
        if cross>1e-7:
            values.append(ab*bc*ac/(2*cross))
    return min(values,default=float('inf'))


def branch_points(recipe):
    parts=[]
    for (x,row),data in interchange_layout(recipe).items():
        for route in data['routes']:
            if route['role']=='branch':
                parts.append([(px+16*x,py-16*row,z) for px,py,z in route['points']])
    by_start={key(points[0]):points for points in parts}
    ends={key(points[-1]) for points in parts}
    start=next(point for point in by_start if point not in ends)
    points=[]
    while start in by_start:
        part=by_start.pop(start)
        points.extend(part if not points else part[1:])
        start=key(part[-1])
    if by_start:raise AssertionError('Disconnected branch fixture')
    # Exact grid cuts add points along existing sampled chords. Those points
    # are not additional bends and must not distort the curvature measurement.
    cleaned=[]
    for point in points:
        while len(cleaned)>=2:
            a,b=cleaned[-2:]
            cross=abs((b[0]-a[0])*(point[1]-a[1])-(b[1]-a[1])*(point[0]-a[0]))
            scale=math.dist(a[:2],b[:2])*math.dist(b[:2],point[:2])
            if cross>1e-7*scale:break
            cleaned.pop()
        cleaned.append(point)
    return cleaned


class InterchangeLayoutTests(unittest.TestCase):
    def test_every_declared_layout_has_unique_bounded_routes_and_physical_decks(self):
        self.assertEqual(len(RECIPES),len(set(RECIPES)))
        self.assertEqual(len(RECIPES),114)
        for recipe,info in INFO.items():
            layout=interchange_layout(recipe)
            with self.subTest(recipe=recipe):
                self.assertEqual(list(layout),info['cells'])
                width,depth=info['footprint']
                self.assertLessEqual(width,64)
                self.assertLessEqual(depth,16)
                for (x,row),data in layout.items():
                    self.assertTrue(0<=x<width and 0<=row<depth)
                    self.assertTrue(data['routes'] and data['decks'])
                    parsed=_parse_paths(encode_paths(data['routes']))
                    self.assertTrue(all(r['transport']==7 and r['entry']!=r['exit'] for r in parsed))
                    self.assertEqual(len(parsed),len({(r['entry'],r['exit'],r['class']) for r in parsed}))
                    for route in parsed:
                        self.assertTrue(all(abs(p[0])<=8+1e-6 and abs(p[1])<=8+1e-6 for p in route['points']))
                        self.assertTrue(all(math.dist(a,b)>1e-7 for a,b in zip(route['points'],route['points'][1:])))
                    self.assertTrue(all(deck['profile']=='blend' and deck['safe_supports'] for deck in data['decks']))

    def test_single_track_filler_levels_and_paths_are_directed(self):
        for level,height in (('ground',1.),('hsr',15.5),('l3',23.),('l4',30.5)):
            recipe=f'interchange_oneway_{level}_straight'
            routes=routes_for(recipe)
            self.assertIn((0.,8.,height),reachable(routes,(0.,-8.,height)))
            self.assertNotIn((0.,-8.,height),reachable(routes,(0.,8.,height)))
            self.assertTrue(all(len(data['routes'])==1 for data in interchange_layout(recipe).values()))

    def test_every_native_external_port_has_an_exact_flat_cardinal_or_diagonal_collar(self):
        for recipe in RECIPES:
            routes=routes_for(recipe)
            starts=Counter(key(points[0]) for points in routes)
            ends=Counter(key(points[-1]) for points in routes)
            external=(starts.keys()-ends.keys())|(ends.keys()-starts.keys())
            for points in routes:
                for at_start in (True,False):
                    endpoint=points[0 if at_start else -1]
                    if key(endpoint) not in external:continue
                    a,b=points[:2] if at_start else points[-2:]
                    dx,dy=abs(b[0]-a[0]),abs(b[1]-a[1])
                    with self.subTest(recipe=recipe,endpoint=endpoint):
                        self.assertEqual(a[2],b[2])
                        self.assertTrue(min(dx,dy)<1e-7 or abs(dx-dy)<2e-6)

    def test_dual_native_mainline_splits_keep_the_opposite_track_and_no_reverse_branch(self):
        for level,height in (('ground',1.),('hsr',15.5)):
            for angle in (45,90,135):
                for size in ('compact','wide'):
                    for mode in ('split','merge'):
                        recipe=f'interchange_{level}_{mode}_{angle}_{size}'
                        info=INFO[recipe]
                        routes=routes_for(recipe)
                        self.assertEqual(len(info['ports']['in']),3 if mode=='merge' else 2)
                        self.assertEqual(len(info['ports']['out']),3 if mode=='split' else 2)
                        # Opposite-running routes are still the exact native
                        # x=-2 straight lane, shifted only by whole grid cells.
                        shift_x,shift_y=info['origin_shift']
                        opposite=[points for points in routes if all(abs(p[0]-(shift_x-2))<1e-6 for p in points)]
                        self.assertTrue(opposite)
                        self.assertTrue(all(route[-1][1]<route[0][1] for route in opposite))
                        for entry in info['ports']['in']:
                            reached=reachable(routes,entry)
                            self.assertTrue(any(key(exit_) in reached for exit_ in info['ports']['out']))

    def test_l4_split_merge_mainline_is_centered_oneway_and_joins_its_fillers(self):
        for mode in ('split','merge'):
            for angle in (45,90,135):
                recipe=f'interchange_l4_{mode}_{angle}_compact'
                info=INFO[recipe]
                self.assertEqual(len(info['ports']['in']),2 if mode=='merge' else 1)
                self.assertEqual(len(info['ports']['out']),2 if mode=='split' else 1)
                shift_x,shift_y=info['origin_shift']
                main=[r for data in interchange_layout(recipe).values() for r in data['routes'] if r['role']=='main']
                self.assertTrue(all(all(abs(p[0])<1e-7 for p in r['points']) for r in main))
                self.assertTrue(all(r['entry']==3 and r['exit']==1 for r in main))

    def test_left_l4_branches_have_only_the_intended_oneway_split_or_merge(self):
        # These literal source endpoints are independent of the layout's
        # generated port metadata. A left branch is safe here because the
        # centred mainline has only one northbound track.
        endpoints={
            (45,'compact'):(-56.,-40.,0.),(45,'wide'):(-104.,-88.,32.),
            (90,'compact'):(-24.,-24.,0.),(90,'wide'):(-88.,-88.,0.),
            (135,'compact'):(-88.,-88.,-16.),(135,'wide'):(-184.,-184.,-32.),
        }
        for (angle,size),(south,bx,by) in endpoints.items():
            for mode in ('split','merge'):
                recipe=f'interchange_l4_{mode}_{angle}_{size}_left'
                dx,dy=INFO[recipe]['origin_shift']
                point=lambda x,y:(x+dx,y+dy,30.5)
                main_in,main_out=point(0.,south),point(0.,8.)
                branch=point(bx,by if mode=='split' else south+8.-by)
                routes=routes_for(recipe)
                reached=reachable(routes,main_in)
                with self.subTest(recipe=recipe):
                    self.assertIn(key(main_out),reached)
                    self.assertEqual(key(branch) in reached,mode=='split')
                    self.assertEqual(key(main_out) in reachable(routes,branch),mode=='merge')
                    self.assertNotIn(key(main_in),reachable(routes,branch))
                    self.assertNotIn(key(main_in),reachable(routes,main_out))
                    self.assertTrue(all(p[2]==30.5 for route in routes for p in route))
                if mode=='split':
                    right_radius=radius(branch_points(f'interchange_l4_split_{angle}_{size}'))
                    self.assertAlmostEqual(radius(branch_points(recipe)),right_radius,places=5)

    def test_level_grades_change_height_continuously_with_flat_end_stubs(self):
        found=0
        for recipe,info in INFO.items():
            if info['kind']!='oneway_grade':continue
            found+=1
            routes=routes_for(recipe)
            self.assertEqual(len(info['ports']['in']),1)
            self.assertEqual(len(info['ports']['out']),1)
            start,end=info['ports']['in'][0],info['ports']['out'][0]
            self.assertEqual(start[2],info['from_height'])
            self.assertEqual(end[2],info['to_height'])
            self.assertIn(key(end),reachable(routes,start))
            self.assertNotIn(key(start),reachable(routes,end))
            for points in routes:
                for a,b in zip(points,points[1:]):
                    run=math.dist(a[:2],b[:2])
                    self.assertGreater(run,0)
                    self.assertLessEqual(abs(b[2]-a[2])/run,.201)
            first=min(routes,key=lambda points:points[0][1])
            last=max(routes,key=lambda points:points[-1][1])
            self.assertTrue(all(abs(p[2]-info['from_height'])<1e-6 for p in first))
            self.assertTrue(all(abs(p[2]-info['to_height'])<1e-6 for p in last))
        self.assertEqual(found,8)

    def test_real_flyover_crossings_have_independent_tracks_at_safe_actual_heights(self):
        for lower in ('ground','hsr'):
            recipe=f'interchange_l4_oneway_over_{lower}'
            info=INFO[recipe]
            self.assertEqual(info['footprint'],(3,1))
            routes=routes_for(recipe)
            above=[p for p in routes if p[0][2]==30.5]
            below=[p for p in routes if p[0][2]<30.5]
            self.assertTrue(above and below)
            start,end=above[0][0],above[-1][-1]
            self.assertIn(key(end),reachable(routes,start))
            for points in below:
                self.assertNotIn(key(end),reachable(routes,points[0]))
            lower_top=1.98933 if lower=='ground' else 16.98933
            upper_bottom=14.01067+15.
            self.assertGreater(upper_bottom-lower_top,5.)

    def test_added_crossing_matrix_has_exact_native_ports_and_no_height_transfer(self):
        cases={}
        for lower,height in (('ground',1.),('hsr',15.5)):
            for variant in ('upper_grid_lower_diag','upper_diag_lower_grid','upper_diag_lower_diag'):
                upper=((-24.,-16.,30.5),(16.,24.,30.5)) if variant.startswith('upper_diag') else (
                       (-24.,0.,30.5),(24.,0.,30.5))
                lower_routes=([((24.,-13.1,height),(-13.2,24.,height)),
                               ((-18.9,24.,height),(24.,-18.9,height))] if 'lower_diag' in variant else
                              [((2.,-24.,height),(2.,24.,height)),
                               ((-2.,24.,height),(-2.,-24.,height))])
                cases[f'interchange_l4_{variant}_over_{lower}']=[upper,*lower_routes]
        cases['interchange_ground_oneway_under_hsr']=[
            ((-8.,0.,1.),(8.,0.,1.)),((2.,-24.,15.5),(2.,24.,15.5)),
            ((-2.,24.,15.5),(-2.,-24.,15.5))]
        cases['interchange_hsr_oneway_over_ground']=[
            ((-24.,0.,15.5),(24.,0.,15.5)),((2.,-8.,1.),(2.,8.,1.)),
            ((-2.,8.,1.),(-2.,-8.,1.))]
        for recipe,movements in cases.items():
            routes=routes_for(recipe)
            dx,dy=INFO[recipe]['origin_shift']
            moved=lambda p:key((p[0]+dx,p[1]+dy,p[2]))
            movements=[(moved(start),moved(finish)) for start,finish in movements]
            outgoing=Counter(key(route[0]) for route in routes)
            incoming=Counter(key(route[-1]) for route in routes)
            with self.subTest(recipe=recipe):
                self.assertEqual(outgoing.keys()-incoming.keys(),{start for start,_ in movements})
                self.assertEqual(incoming.keys()-outgoing.keys(),{finish for _,finish in movements})
            for start,finish in movements:
                reached=reachable(routes,start)
                with self.subTest(recipe=recipe,start=start):
                    self.assertEqual({target for _,target in movements if target in reached},{finish})
                    self.assertNotIn(start,reachable(routes,finish))

    def test_wide_branch_radius_is_at_least_twice_the_compact_radius(self):
        for level in ('ground','hsr','l4'):
            for angle in (45,90,135):
                measured=[]
                for size in ('compact','wide'):
                    recipe=f'interchange_{level}_split_{angle}_{size}'
                    measured.append(radius(branch_points(recipe)))
                with self.subTest(level=level,angle=angle):
                    self.assertGreaterEqual(measured[1],2*measured[0])


if __name__=='__main__':unittest.main()
