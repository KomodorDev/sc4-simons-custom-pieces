"""Corrupt reopened pavement UVs, including a tessellated neutral impostor."""
import math
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]
from scp.models import parse_s3d,pack_s3d
from scp.recipes import combine_meshes
from scp_highway.ramp_geometry import pack_road_model, compact_ramps
from scp_highway import wheeltrack_verify as verify
from scp_highway import ramp_verify, native_overhangs

# Frozen numerical UV observations from the independently reopened accepted
# proof. No native image, model buffer, or writer function is imported.
CONTROL_UV = {'lower-off': [(-3, [0.5126940984598444, 1.194577621373781], [0.38769693621494017, 1.1952383099673256]),
               (-2, [0.551919190794614, 1.2448480658775543], [0.4269148673743031, 1.244921786436108]),
               (-1, [0.5903910193580255, 1.2920720850002527], [0.46536659543341785, 1.2920798110819511]),
               (0, [0.6250011046418762, 1.3423836077378226], [0.49999890767768146, 1.3423847376267006]),
               (1, [0.6550182595957884, 1.3971011650025704], [0.530016088119994, 1.3970872208844245]),
               (2, [0.6897305596502221, 1.4512003854885478], [0.5605034806849245, 1.451183360286336]),
               (3, [0.7243380411956281, 1.5047491141682632], [0.5915234300684594, 1.5047505719225511])],
 'lower-on': [(-3, [0.5126940984723535, 4.470764436785358], [0.3876971677074714, 4.470896486285476]),
              (-2, [0.5519191907637614, 4.421312076585796], [0.4269160166110161, 4.4213180877101905]),
              (-1, [0.5903910192094113, 4.37408775022125], [0.46537202794161436, 4.373998683277265]),
              (0, [0.6250011046589111, 4.32377637958115], [0.49999889635713923, 4.323775441880097]),
              (1, [0.6550182596023882, 4.269058724158306], [0.5300160887628703, 4.2690471895066455]),
              (2, [0.6897305596669052, 4.214959429236943], [0.5605034740537758, 4.214946716422896]),
              (3, [0.724338041199141, 4.161410940090963], [0.5915234190899785, 4.161410119783207])],
 'upper-off': [(-3, [0.5479922933813013, 1.8171083305025246], [0.42299026837946097, 1.8171112649821368]),
               (-2, [0.5753585498845856, 1.8729069943182004], [0.4503563707705893, 1.8729297244828897]),
               (-1, [0.6016368674210599, 1.928497769592635], [0.4766190336962076, 1.9285335549651301]),
               (0, [0.6250011359662457, 1.9857278573949881], [0.5000252736351182, 1.9857190436366594]),
               (1, [0.646156601494047, 2.044562957122335], [0.5211542386455892, 2.0445607406354713]),
               (2, [0.6686123712562505, 2.1031565205366545], [0.5424019722663874, 2.1031576354211374]),
               (3, [0.6938077123568123, 2.1615277921224627], [0.5639980447292279, 2.1615010324411017])],
 'upper-on': [(-3, [0.547992293378584, 5.84158488487176], [0.4229902096489949, 5.841533361039962]),
              (-2, [0.5753585498980397, 5.78573580832742], [0.4503546586460208, 5.785688992435388]),
              (-1, [0.6016368674435488, 5.730144834688112], [0.4766166571615095, 5.730132179598815]),
              (0, [0.6250011358485388, 5.6729148899481885], [0.50002522856619, 5.67292370409108]),
              (1, [0.6461565724203983, 5.614079345938985], [0.5211542282523272, 5.614067203916536]),
              (2, [0.6686123661261262, 5.555485662428995], [0.5424019711929158, 5.5554837504158465]),
              (3, [0.6938077329163981, 5.497114253318569], [0.5639980315745047, 5.497125591010325])]}


def _patch(s,q,uv,mouth,origin,ds=.02,dq=.000008):
    corners=[]
    for x,y in ((s-ds,q-dq),(s+ds,q-dq),(s+ds,q+dq),(s-ds,q+dq)):
        east,north,h=verify.world(x,y,mouth)
        corners.append((east-origin[0],h,-(north-origin[1]),uv[0],uv[1]+(x-s)*.001))
    result=[]
    for a,b,c in ((0,1,2),(0,2,3)):
        tri=tuple(corners[i] for i in (a,b,c))
        up=(tri[1][2]-tri[0][2])*(tri[2][0]-tri[0][0])-(tri[1][0]-tri[0][0])*(tri[2][2]-tri[0][2])
        result.append(tri if up>0 else (tri[0],tri[2],tri[1]))
    return result


def fixture(extra_outside=False,tessellated=False):
    owners,resources,paths={},{},{};ramps={r['id']:r for r in compact_ramps()}
    for index,mouth in enumerate(verify.MOUTHS):
        name=mouth[0];key=name.replace('-off','-exit-branch').replace('-on','-entry-branch')
        pid='ddrhw-diagonal-'+key;origin=verify._BRANCH_ORIGINS[key]
        taper,parallel=mouth[5:7];seam=20.112386349087025 if name.startswith('lower') else 30.81888787568175
        onset=7.259615248962954 if name.startswith('lower') else 9.67958761329412
        spine=ramps[name]['points'] if name.endswith('-off') else list(reversed(ramps[name]['points']))
        paths[name]=[(p[0]+64.,p[1]-64.,p[2]) for p in spine]
        dd,mis=[],[]
        for delta,duv,muv in CONTROL_UV[name]:
            dd.extend(_patch(seam+delta,8.-2e-5,duv,mouth,origin))
            mis.extend(_patch(seam+delta,8.+2e-5,muv,mouth,origin))
        for s in (taper/2,taper,taper+1,taper+parallel/2,taper+parallel,taper+parallel+2):
            dd.extend(_patch(s,4.5+.0001,(95.5/128.,.25),mouth,origin))
        for control_name,point,u in verify.GREY_LOBE_CONTROLS:
            if control_name==name:
                s,q,_h=verify.local(point,mouth)
                dd.extend(_patch(s,q,(u,.25),mouth,origin,ds=.0002,dq=.0002))
        if extra_outside and index==0:dd.extend(_patch(-5.,6.,(.625,.25),mouth,origin,ds=.04,dq=.04))
        if tessellated and index==0:
            for ix in range(40):
                for iy in range(20):
                    dd.extend(_patch(12.1+(ix+.5)*.08,4.7+(iy+.5)*.08,(95.5/128.,.25),mouth,origin,ds=.04,dq=.04))
        models=[parse_s3d(pack_road_model(faces,texture)) for faces,texture in ((dd,verify.DD),(mis,verify.MIS))]
        model=combine_meshes([(m,m['meshes'],(0.,0.,0.)) for m in models]);tile=0x7F710000+index*0x100
        owners[index,0]={'piece_id':pid,'tile':tile,'local_cell':(0,0),'angle':0,'origin':origin}
        resources[pid]={(*verify.S3D,tile+4):pack_s3d(model)}
    return owners,resources,paths


def mutate(resources,change):
    for pid,records in resources.items():
        key=next(iter(records));model=parse_s3d(records[key])
        for mesh in model['meshes']:
            vi,_ii,_pi,mi=mesh['frames'][0]
            if model['materials'][mi]['textures']!=[verify.DD]:continue
            block=model['vertices'][vi];raw=bytearray(block['data'])
            for offset in range(0,len(raw),block['stride']):
                p=struct.unpack_from('<5f',raw,offset);struct.pack_into('<5f',raw,offset,*change(pid,p))
            block['data']=bytes(raw)
        records[key]=pack_s3d(model)


def checked(owners,resources,paths):
    return verify.check_uv(verify.saved_faces(owners,resources),paths,verify.corridor_regions(paths))


def neutral_face(size=.05,u=65.5/128.,height=7.5):
    return {'texture':verify.DD,'material_sha256':'307aba7786d4b4f11dbc499eb54f7d05d01a114001919b8a5f7d55970fbb64ca',
            'upward':True,'points':((0.,0.,height),(size,0.,height),(0.,size,height)),
            'uv':((u,.25),(u,.25),(u,.25))}


def overhang_fixture(s=18.,q=7.5):
    """Synthetic frozen donor plane and serialized contained UV-only fragment."""
    import hashlib
    from scp_highway.ramp_geometry import road_material
    mouth=verify.MOUTHS[0];origin=verify._BRANCH_ORIGINS['lower-exit-branch'];cell=(1,0)
    def vertex(station,lateral,u,v):
        east,north,h=verify.world(station,lateral,mouth)
        return east-origin[0]-16*cell[0],h,-(north-origin[1])-16*cell[1],u,v
    donor=tuple(vertex(station,lateral,.2+index*.1,.3+index*.1)
                for index,(station,lateral) in enumerate(((s-1,q-1),(s+1,q-1),(s,q+1))))
    face=tuple(vertex(station,lateral,.625+index*.0001,.25+index*.0001)
               for index,(station,lateral) in enumerate(((s-.01,q-.01),(s+.01,q-.01),(s,q+.01))))
    face=(face[0],face[2],face[1])
    material=road_material(verify.DD)
    expected={(hashlib.sha256(material['raw']).hexdigest(),donor)}
    raw=pack_road_model([face],verify.DD)
    piece={'geometry_key':'lower-exit-branch'}
    ramp=next(r for r in compact_ramps() if r['id']=='lower-off')
    # Convert the portable saved traffic spine to the piece's preview frame.
    routes={(0,0):[{'transport':1,'points':[(p[0]+64-origin[0],p[1]-64-origin[1],p[2])
                                         for p in ramp['points']]}]}
    return raw,cell,expected,piece,routes


class SavedWheeltrackTests(unittest.TestCase):
    def test_crossing_offset_fills_two_even_odd_lobes_without_filling_the_hull(self):
        polygon=[(0.,0.,7.5),(2.,2.,7.5),(0.,2.,7.5),(2.,0.,7.5)]
        lobes=verify._offset_lobes(polygon)
        self.assertEqual(len(lobes),2)
        regions=[]
        for lobe in lobes:
            if sum(verify._cross(a,b)for a,b in zip(lobe,lobe[1:]+lobe[:1]))<0:lobe.reverse()
            regions.append({'height':7.5,'boundary':[p[:2]for p in lobe]})
        self.assertTrue(any(verify.inside_region((1.,1.5,7.5),r,guard=0)for r in regions))
        self.assertTrue(any(verify.inside_region((1.,.5,7.5),r,guard=0)for r in regions))
        self.assertFalse(any(verify.inside_region((.1,1.,7.5),r,guard=0)for r in regions))

    def test_old_plain_uv_inside_a_folded_lobe_is_rejected_after_reopening(self):
        o,r,p=fixture();target=verify.GREY_LOBE_CONTROLS[0][1]
        def old(pid,v):
            if pid!='ddrhw-diagonal-lower-entry-branch':return v
            origin=verify._BRANCH_ORIGINS['lower-entry-branch'];point=(v[0]+origin[0],-v[2]+origin[1],v[1])
            if math.dist(point,target)>.001:return v
            q=verify.local(point,verify.MOUTHS[1])[1]
            return (*v[:3],.5-q/16.,v[4])
        mutate(r,old)
        with self.assertRaisesRegex(ValueError,'lobe retains'):checked(o,r,p)

    def test_rgb_rounding_control_projects_onto_a_real_saved_edge_without_uv_extrapolation(self):
        raw=pack_road_model([((0.,15.,0.,.6,0.),(1.,15.,0.,.7,0.),(0.,15.,-1.,.6,.1))],verify.DD)
        faces=ramp_verify._triangles(raw,(0,0));index=verify.SurfaceIndex(faces)
        point=(.25,-5e-7,15.)
        self.assertFalse(index.sample(point,verify.DD))
        with patch.object(verify,'DD_MATERIAL_SHA256',faces[0]['material_sha256']):
            surface=verify._nearest_rgb_surface(index,point,verify.DD)
            self.assertAlmostEqual(surface['uv'][0],.625,places=6)
            self.assertEqual(surface['position_adjustment']['actual_point_m'],[.25,0.,15.])
            self.assertAlmostEqual(surface['position_adjustment']['distance_m'],5e-7)
            with self.assertRaisesRegex(ValueError,'two micrometres'):
                verify._nearest_rgb_surface(index,(.25,-2.1e-6,15.),verify.DD)
            with self.assertRaisesRegex(ValueError,'two micrometres'):
                verify._nearest_rgb_surface(index,(.25,-5e-7,7.5),verify.DD)
        with self.assertRaisesRegex(ValueError,'two micrometres'):
            verify._nearest_rgb_surface(index,point,verify.DD)

    def test_only_measured_fsh_encodings_with_the_exact_decoded_image_are_accepted(self):
        import hashlib
        class Image:
            shape=(128,128,4)
            flat=(.2,.4,.6,1.)*(128*128)
        images={verify.DD:Image(),verify.MIS:Image()}
        rgba=hashlib.sha256(bytes((51,102,153,255))*(128*128)).hexdigest()
        expected={verify.DD:rgba,verify.MIS:rgba}
        def provenance(encodings):
            return [{'instance':f'{iid:08x}','fsh_sha256':encodings[iid]}for iid in (verify.DD,verify.MIS)]
        with patch.object(verify,'RGBA_SHA256',expected):
            for encodings in (verify.FSH_SHA256,verify.EMBEDDED_FSH_SHA256):
                actual=verify._native_rgb_inputs(images,provenance(encodings))
                self.assertEqual(actual[verify.DD]['fsh_sha256'],encodings[verify.DD])
            with self.assertRaisesRegex(ValueError,'texture fingerprint'):
                verify._native_rgb_inputs(images,provenance({verify.DD:'0'*64,verify.MIS:'0'*64}))
        with self.assertRaisesRegex(ValueError,'decoded first-image fingerprint'):
            verify._native_rgb_inputs(images,provenance(verify.FSH_SHA256))

    def test_folded_corridor_export_preserves_the_effective_half_planes(self):
        # The concave loop's directed half-planes restrict the intersection
        # to x<=1. Exporting its full area would permit the lower right spur.
        boundary=[(0.,0.),(2.,0.),(1.,1.),(1.,2.),(0.,2.)]
        region={'height':7.5,'mouth':'lower-off','boundary':boundary}
        owner={'piece_id':'ddrhw-diagonal-lower-exit-branch','origin':(0.,0.),'angle':0}
        result=verify.export_corridors({(0,0):owner},[region],'old','new')
        exported=result['pieces'][owner['piece_id']][0]['boundary_xz_m']
        polygon=[(x,-z) for x,z in exported]
        self.assertTrue(all(math.dist(a,b)>1e-12 for a,b in zip(polygon,polygon[1:]+polygon[:1])))
        self.assertTrue(all(verify._cross((b[0]-a[0],b[1]-a[1]),(c[0]-b[0],c[1]-b[1]))>=-1e-9
                            for a,b,c in zip(polygon,polygon[1:]+polygon[:1],polygon[2:]+polygon[:2])))
        normalized={'height':7.5,'boundary':polygon}
        for x in (i*.125 for i in range(17)):
            for y in (i*.125 for i in range(17)):
                self.assertEqual(verify.inside_region((x,y,7.5),region,guard=0),
                                 verify.inside_region((x,y,7.5),normalized,guard=0))

    def test_export_retains_other_mouth_deck_regions_in_each_actual_branch_pose(self):
        # The upper branch's retained lower deck can carry a lower mouth's
        # field. Nominal mouth ownership must not erase that exception.
        owners={
            (0,0):{'piece_id':'ddrhw-diagonal-lower-exit-branch','origin':(96.,-16.),'angle':0},
            (1,0):{'piece_id':'ddrhw-diagonal-upper-entry-branch','origin':(112.,0.),'angle':90},
            (2,0):{'piece_id':'unrelated-ground-piece','origin':(0.,0.),'angle':0},
        }
        boundary=[(120.,-8.),(121.,-8.),(120.,-7.)]
        regions=[{'height':height,'mouth':mouth,'boundary':boundary}
                 for height,mouth in ((7.5,'lower-off'),(15.,'upper-on'))]
        result=verify.export_corridors(owners,regions,'old','new')
        self.assertEqual(set(result['pieces']),
                         {owners[(0,0)]['piece_id'],owners[(1,0)]['piece_id']})
        for owner in (owners[(0,0)],owners[(1,0)]):
            rows=result['pieces'][owner['piece_id']]
            self.assertEqual(sorted(row['height_m']for row in rows),[7.5,15.])
            for row in rows:
                restored=[]
                for x,z in row['boundary_xz_m']:
                    y=-z
                    for _ in range(owner['angle']//90):x,y=-y,x
                    restored.append((x+owner['origin'][0],y+owner['origin'][1]))
                self.assertEqual(set(restored),set(boundary))

    def test_reopened_control_surfaces_pass_without_native_pixels(self):
        o,r,p=fixture();report=checked(o,r,p)
        self.assertEqual(report['seam_controls_checked'],28)
        self.assertEqual(report['neutral_inner_boundary_controls_checked'],24)
        self.assertFalse(report['native_rgb_tested']);self.assertFalse(report['game_rendering_tested'])
        for owner in o.values():
            local_owner={**owner,'origin':(0.,0.)}
            faces=verify.saved_faces({(0,0):local_owner},r)
            triangles=[{**f,'upward':True} for f in faces]
            controls=verify.check_piece_controls(triangles,{'geometry_key':owner['piece_id'].removeprefix('ddrhw-diagonal-')})
            self.assertEqual(controls['seam_uv_phase_controls'],7)
            self.assertEqual(controls['neutral_boundary_controls'],6)

    def test_saved_phase_restart_is_rejected(self):
        o,r,p=fixture();mutate(r,lambda pid,v:(*v[:4],v[4]+.25))
        with self.assertRaisesRegex(ValueError,'longitudinal phase'):checked(o,r,p)

    def test_saved_phantom_dashed_stripe_is_rejected(self):
        o,r,p=fixture();mutate(r,lambda pid,v:(*v[:3],62.5/128.,v[4]))
        with self.assertRaisesRegex(ValueError,'paint column'):checked(o,r,p)

    def test_saved_dark_inner_boundary_is_rejected(self):
        o,r,p=fixture()
        def dark(pid,v):
            key=pid.removeprefix('ddrhw-diagonal-');origin=verify._BRANCH_ORIGINS[key]
            mouth=next(m for m in verify.MOUTHS if m[0]==key.replace('-exit-branch','-off').replace('-entry-branch','-on'))
            q=verify.local((v[0]+origin[0],-v[2]+origin[1],v[1]),mouth)[1]
            return (*v[:3],.625 if abs(q-4.5)<.001 else v[3],v[4])
        mutate(r,dark)
        with self.assertRaisesRegex(ValueError,'inner boundary'):checked(o,r,p)

    def test_saved_rectangle_outside_the_route_corridor_is_rejected(self):
        o,r,p=fixture(extra_outside=True)
        with self.assertRaisesRegex(ValueError,'outside.*corridor'):checked(o,r,p)

    def test_a_tessellated_broad_neutral_patch_cannot_use_the_one_texel_exception(self):
        o,r,p=fixture(tessellated=True);mutate(r,lambda pid,v:(*v[:3],95.5/128.,v[4]))
        with self.assertRaisesRegex(ValueError,'transverse field'):checked(o,r,p)
        owner=next(iter(o.values()));pid=owner['piece_id'];local_owner={**owner,'origin':(0.,0.)}
        faces=verify.saved_faces({(0,0):local_owner},r)
        triangles=[{**f,'upward':True} for f in faces]
        with self.assertRaisesRegex(ValueError,'transverse field'):
            ramp_verify._atlas(r,{'geometry_key':'lower-exit-branch'}, {},triangles)

    def test_small_neutral_clamp_needs_affirmative_controls(self):
        face=neutral_face()
        with self.assertRaisesRegex(ValueError,'flat colour'):ramp_verify._native_appearance([face])
        report=ramp_verify._native_appearance([face],neutral_field_controls={'passed':True})
        self.assertEqual(report['neutral_one_texel_fragments_checked'],1)
        other=neutral_face(u=95.5/128.)
        self.assertEqual(ramp_verify._native_appearance([other],neutral_field_controls={'passed':True})['neutral_one_texel_fragments_checked'],1)

    def test_broad_dark_paint_or_wrong_height_flat_fragments_still_fail(self):
        for face in (neutral_face(size=.2),neutral_face(u=.625),neutral_face(u=27.5/128.),neutral_face(height=7.51)):
            with self.subTest(face=face),self.assertRaisesRegex(ValueError,'flat colour'):
                ramp_verify._native_appearance([face],neutral_field_controls={'passed':True})

    def test_one_texel_bound_allows_only_a_small_encoding_tolerance(self):
        face=neutral_face()
        face['points']=((0.,0.,7.5),(.12501,0.,7.5),(.0625,.01,7.5))
        self.assertEqual(ramp_verify._native_appearance([face],neutral_field_controls={'passed':True})['neutral_one_texel_fragments_checked'],1)
        face['points']=((0.,0.,7.5),(.12503,0.,7.5),(.0625,.01,7.5))
        with self.assertRaisesRegex(ValueError,'flat colour'):
            ramp_verify._native_appearance([face],neutral_field_controls={'passed':True})

    def test_material_pin_and_positive_winding_still_apply(self):
        face=neutral_face();face['material_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'native NAM'):ramp_verify._native_appearance([face],neutral_field_controls={'passed':True})
        face=neutral_face();face['upward']=False
        with self.assertRaisesRegex(ValueError,'flat colour'):ramp_verify._native_appearance([face],neutral_field_controls={'passed':True})

    def test_serialized_native_uv_only_fragment_requires_deferred_branch_proof(self):
        raw,cell,expected,piece,routes=overhang_fixture()
        with patch.object(native_overhangs,'NATIVE_OVERHANG_SURFACES',expected):
            with self.assertRaisesRegex(ValueError,'overhang'):
                ramp_verify._triangles(raw,cell)
            faces=ramp_verify._triangles(raw,cell,pending_native_uv=True)
        self.assertTrue(faces[0]['pending_native_uv_fragment'])
        with self.assertRaisesRegex(ValueError,'affirmative'):
            verify.check_piece_overhangs(faces,piece,routes,None)
        report=verify.check_piece_overhangs(faces,piece,routes,{'passed':True})
        self.assertEqual(report['uv_only_native_fragments'],1)

    def test_serialized_overhang_translation_height_expansion_and_material_fail(self):
        raw,cell,expected,_piece,_routes=overhang_fixture()
        def translated(p):return (p[0]-10.,*p[1:])
        def raised(p):return (p[0],p[1]+.001,*p[2:])
        def expanded(p):return (p[0]*10.,p[1],p[2]*10.,*p[3:])
        for change in (translated,raised,expanded):
            model=parse_s3d(raw);block=model['vertices'][0];data=bytearray(block['data'])
            for offset in range(0,len(data),block['stride']):
                struct.pack_into('<5f',data,offset,*change(struct.unpack_from('<5f',data,offset)))
            block['data']=bytes(data)
            with patch.object(native_overhangs,'NATIVE_OVERHANG_SURFACES',expected),self.assertRaisesRegex(ValueError,'overhang'):
                ramp_verify._triangles(pack_s3d(model),cell,pending_native_uv=True)
        model=parse_s3d(raw);material=model['materials'][0];data=bytearray(material['raw']);data[4]^=1;material['raw']=bytes(data)
        with patch.object(native_overhangs,'NATIVE_OVERHANG_SURFACES',expected),self.assertRaisesRegex(ValueError,'overhang'):
            ramp_verify._triangles(pack_s3d(model),cell,pending_native_uv=True)

    def test_native_uv_overhang_outside_actual_transfer_corridor_fails(self):
        raw,cell,expected,piece,routes=overhang_fixture(s=-2.,q=7.5)
        with patch.object(native_overhangs,'NATIVE_OVERHANG_SURFACES',expected):
            faces=ramp_verify._triangles(raw,cell,pending_native_uv=True)
        with self.assertRaisesRegex(ValueError,'curved transfer corridor'):
            verify.check_piece_overhangs(faces,piece,routes,{'passed':True})


if __name__=='__main__':unittest.main()
