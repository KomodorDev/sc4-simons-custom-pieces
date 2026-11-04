"""Reopen complete saved paint, then corrupt indexed geometry at real joins."""
import math
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]

from scp.models import pack_s3d, parse_s3d
from scp_highway import marking_verify as check
from scp_highway import ramp_geometry as fixture_writer
from scp_highway.slip_lanes import surfaces


def fixture(width=.25):
    """Author the fixture separately; expected measurements never call it."""
    owners, resources = {}, {}
    for index,ramp in enumerate(fixture_writer.compact_ramps()):
        name,station,direction,side,height,*_ = check.MOUTHS[index]
        faces = []
        for triangle in surfaces([ramp]):
            if abs(triangle[0][3]-1.375)>1e-8:
                continue
            saved=[]
            for point in triangle:
                x,h,z,_semantic,across=point
                s=direction*((x-z)/math.sqrt(2.)-station)
                q=side*(-z-x+8.)/math.sqrt(2.)
                first=8. if name.startswith('lower') else 12.
                if first-1e-5<=s<=first+2.+1e-5 and abs(q-4.5)<.13 and width!=.25:
                    q=4.5+(q-4.5)*width/.25
                    u=station+direction*s;v=side*q
                    x,z=4.+(u-v)/math.sqrt(2.),4.-(u+v)/math.sqrt(2.)
                saved.append((x,h,z,.21484375+.0078125*across,(x-z)/(16.*math.sqrt(2.))))
            faces.append(tuple(saved))
        tile=0x7F740000+index*0x100
        raw=fixture_writer.pack_road_model(faces,0x5713000E)
        owners[index,0]={'piece_id':name,'tile':tile,'local_cell':(0,0),'angle':0,'origin':(64.,-64.)}
        resources[name]={(*check.S3D,tile+4):raw}
    return owners,resources


def revise(resources,name,select,transform=None):
    """Select actual saved triangles in the reviewed outward local frame."""
    key=next(iter(resources[name]));model=parse_s3d(resources[name][key]);changed=0
    _,station,direction,side,*_=next(row for row in check.MOUTHS if row[0]==name)
    for mesh in model['meshes']:
        vi,ii,pi,_mi=mesh['frames'][0];block=model['vertices'][vi]
        vertices=[struct.unpack_from('<5f',block['data'],off) for off in range(0,len(block['data']),block['stride'])]
        local=[(direction*((p[0]-p[2])/math.sqrt(2.)-station),side*(-p[2]-p[0]+8.)/math.sqrt(2.)) for p in vertices]
        indices=model['indices'][ii]['values'];new=[];selected=set()
        for kind,start,count in model['primitives'][pi]:
            for off in range(start,start+count,3):
                ids=indices[off:off+3]
                if select([local[i] for i in ids]):
                    changed+=1
                    if transform is not None:new.extend(ids);selected.update(ids)
                else:new.extend(ids)
        if transform is not None:
            for index in selected:
                s,q=transform(local[index]);u,v=station+direction*s,side*q
                old=vertices[index];vertices[index]=(4.+(u-v)/math.sqrt(2.),old[1],4.-(u+v)/math.sqrt(2.),*old[3:])
            block['data']=b''.join(struct.pack('<5f',*p) for p in vertices)
        model['indices'][ii]['values']=tuple(new);model['primitives'][pi]=[(0,0,len(new))]
    if not changed:raise AssertionError('Mutation changed no saved indexed triangle')
    resources[name][key]=pack_s3d(model)
    return changed


class SavedMarkingWidthTests(unittest.TestCase):
    def test_complete_saved_paint_has_native_width_gore_angles_and_handoffs(self):
        owners,resources=fixture();report=check.check_saved_markings(owners,resources)
        self.assertTrue(report['passed']);self.assertEqual(report['perpendicular_width_sections_checked'],76)
        self.assertEqual(report['hatches_checked'],12);self.assertEqual(report['nose_and_handoff_points_checked'],44)
        self.assertFalse(report['game_rendering_tested'])

    def test_old_ten_and_twelve_centimetre_strokes_fail_after_binary_save(self):
        for width in (.10,.12):
            with self.subTest(width=width):
                owners,resources=fixture(width)
                with self.assertRaisesRegex(ValueError,'white-stripe width'):check.check_saved_markings(owners,resources)

    def test_an_overwide_stroke_is_rejected(self):
        owners,resources=fixture(.4)
        with self.assertRaisesRegex(ValueError,'white-stripe width'):check.check_saved_markings(owners,resources)

    def test_removing_a_saved_dash_is_rejected(self):
        owners,resources=fixture();revise(resources,'upper-off',lambda t:all(11.9<p[0]<14.1 and abs(p[1]-4.5)<.14 for p in t))
        with self.assertRaisesRegex(ValueError,'missing or disconnected'):check.check_saved_markings(owners,resources)

    def test_a_skewed_saved_hatch_is_rejected(self):
        owners,resources=fixture();name='upper-off';a,b=check.CONTRACTS[name]['hatches'][0]
        centre=tuple((x+y)/2 for x,y in zip(a,b));angle=math.radians(10.)
        def select(t):
            span=check._section(t,centre,(1.,1.));return span is not None and span[1]-span[0]>1e-5
        def rotate(p):
            x,y=p[0]-centre[0],p[1]-centre[1]
            return centre[0]+x*math.cos(angle)-y*math.sin(angle),centre[1]+x*math.sin(angle)+y*math.cos(angle)
        revise(resources,name,select,rotate)
        with self.assertRaisesRegex(ValueError,'45 degrees'):check.check_saved_markings(owners,resources)

    def test_a_missing_saved_gore_nose_is_rejected(self):
        owners,resources=fixture();name='lower-off';nose=check.CONTRACTS[name]['nose']
        revise(resources,name,lambda t:any(math.dist(p,nose)<.6 for p in t))
        with self.assertRaisesRegex(ValueError,'gore nose'):check.check_saved_markings(owners,resources)

    def test_a_displaced_saved_gore_rail_is_rejected(self):
        owners,resources=fixture();name='upper-on';centre=check.CONTRACTS[name]['inner_pre_ease_sections'][0]['point']
        def select(t):
            span=check._section(t,centre,(1.,0.));return span is not None and span[1]-span[0]>1e-5
        revise(resources,name,select,lambda p:(p[0]+.5,p[1]+.5))
        with self.assertRaisesRegex(ValueError,'missing|offset|width'):check.check_saved_markings(owners,resources)

    def test_a_disconnected_saved_handoff_is_rejected(self):
        owners,resources=fixture();name='lower-on';end=check.CONTRACTS[name]['outer_controls'][-1][0]
        revise(resources,name,lambda t:any(p[1]>7.9 for p in t) and all(end-1.5<p[0]<end+.5 for p in t))
        with self.assertRaisesRegex(ValueError,'handoff is disconnected'):check.check_saved_markings(owners,resources)

    def test_missing_paint_cannot_pass(self):
        with self.assertRaisesRegex(ValueError,'geometry is absent'):check.check_faces([])


if __name__=='__main__':unittest.main()
