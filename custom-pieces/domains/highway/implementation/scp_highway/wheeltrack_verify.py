"""Independent saved-PATH, pavement-UV, and optional native-colour checks.

This module does not import the wheeltrack writer or its geometry helpers.
RGB measurements require explicitly supplied, pinned native texture images.
"""
from __future__ import annotations

from collections import defaultdict
import hashlib
import math
import struct

from scp.models import parse_s3d
from scp.track_paths import S3D
from .shoulder_uv_verify import _clip, _area

ROOT = math.sqrt(2.)
DD, MIS = 0x5713000E, 0x5712000E
DD_MATERIAL_SHA256 = '307aba7786d4b4f11dbc499eb54f7d05d01a114001919b8a5f7d55970fbb64ca'
RGB_POSITION_LIMIT_M = 2e-6
SAFE_U = (65.5 / 128., 95.5 / 128.)
U_TOLERANCE, PHASE_TOLERANCE = 1e-4, .001
BARYCENTRIC_GUARD = 1e-7
CORRIDOR_GUARD = .001
# Frozen grey-hole locations, independently measured against the unchanged
# saved transfer PATHs. One texel bounds the sampled 0.125 m field's local
# interpolation; retained plain-shoulder UVs differ by more than 0.4 repeats.
LOBE_U_TOLERANCE = 1./128.
GREY_LOBE_CONTROLS = (
    ('lower-on',(21.254410079762906,-105.68518587909168,7.5),.5687933477720377),
    ('lower-on',(21.254410079762906,-105.89820394636709,7.5),.5777470864054529),
    ('lower-on',(21.595238987403576,-105.89820394636709,7.5),.5937987124353005),
    ('lower-off',(105.30175335799592,-21.21180646630782,7.5),.5544650396950171),
    ('lower-off',(105.77039310600185,-21.42482453358324,7.5),.5804925469668532),
)
# Native ports and unchanged saved transfer channels are independent measurements.
MOUTHS = (
    ('lower-off', 75.80184694319789, -1, 1, 7.5, 12., 4., ('HW_NE', 'AVE_NW'), 1.3423847376267006),
    ('lower-on', -75.80184694319789, 1, 1, 7.5, 12., 4., ('AVE_NW', 'HW_SW'), 4.323775441880097),
    ('upper-off', -109.74297244015216, 1, -1, 15., 16., 8., ('HW_SW', 'AVE_SE'), 1.9857190436525767),
    ('upper-on', 109.74297244015214, -1, -1, 15., 16., 8., ('AVE_SE', 'HW_NE'), 5.672923775886127),
)


def _need(value, message):
    if not value:
        raise ValueError(message)


def _cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def local(point, mouth):
    _name, station, direction, side, *_ = mouth
    return (direction*((point[0]+point[1])/ROOT-station),
            side*(point[1]-point[0]+136.)/ROOT, point[2])


def world(s, q, mouth):
    _name, station, direction, side, height, *_ = mouth
    u, v = station+direction*s, side*q
    return 68.+(u-v)/ROOT, -68.+(u+v)/ROOT, height


def reviewed_paths(routes, path_report):
    """Read each accepted outward spine from actual decoded transfer witnesses."""
    witnesses = {(r['from_arm'], r['to_arm']): r['saved_route_ids']
                 for r in path_report['movement_witnesses']}
    result = {}
    for mouth in MOUTHS:
        name, *_ = mouth
        incoming = []
        for identifier in witnesses[mouth[7]]:
            for point in routes[identifier]['points']:
                if not incoming or math.dist(point, incoming[-1]) > 1e-8:
                    incoming.append(tuple(point))
        if name.endswith('-on'):
            incoming.reverse()
        result[name] = incoming
    return result


def _offset_lobes(polygon):
    """Split a self-crossing four-corner offset into its two even-odd lobes."""
    for start in (0,1):
        a,b,c,d=(polygon[(start+i)%4]for i in range(4))
        r=(b[0]-a[0],b[1]-a[1]);s=(d[0]-c[0],d[1]-c[1])
        denominator=_cross(r,s)
        if abs(denominator)<=1e-14:
            continue
        offset=(c[0]-a[0],c[1]-a[1])
        t,u=_cross(offset,s)/denominator,_cross(offset,r)/denominator
        if 1e-12<t<1.-1e-12 and 1e-12<u<1.-1e-12:
            crossing=tuple(x+t*(y-x)for x,y in zip(a,b))
            return [[crossing,b,c],[crossing,d,a]]
    return [polygon]


def corridor_regions(paths, *, mouths=MOUTHS):
    """Derive six-metre mitered strips from saved PATHs, then clip q=4.5..8.

    These mathematical offsets are independently constructed from the saved
    traffic spine. They do not read a writer-supplied exception mask.
    """
    result = []
    for mouth in mouths:
        name, _station, _direction, side, height, *_ = mouth
        points = paths[name]
        tangents = []
        for a, b in zip(points, points[1:]):
            length = math.dist(a[:2], b[:2])
            _need(length > 1e-9, 'Saved wheeltrack spine has a stationary planar segment')
            tangents.append(((b[0]-a[0])/length, (b[1]-a[1])/length))
        normals = []
        for i in range(len(points)):
            a, b = tangents[max(0,i-1)], tangents[min(i,len(tangents)-1)]
            n0, n1 = (-a[1],a[0]), (-b[1],b[0])
            denominator = 1.+sum(x*y for x,y in zip(n0,n1))
            _need(denominator > .25, 'Saved wheeltrack spine has an invalid offset miter')
            normals.append(tuple((x+y)/denominator for x,y in zip(n0,n1)))
        for i, (a,b) in enumerate(zip(points, points[1:])):
            if any(abs(p[2]-height)>1e-5 for p in (a,b)):
                continue
            for low,high in ((-3.,0.),(0.,3.)):
                offset_quad = [(p[0]+offset*n[0],p[1]+offset*n[1],height)
                           for p,n,offset in ((a,normals[i],low),(a,normals[i],high),
                                              (b,normals[i+1],high),(b,normals[i+1],low))]
                for polygon in _offset_lobes(offset_quad):
                    polygon = _clip(polygon, lambda p: local(p,mouth)[0])
                    polygon = _clip(polygon, lambda p: local(p,mouth)[1]-4.5)
                    polygon = _clip(polygon, lambda p: 8.-local(p,mouth)[1])
                    if len(polygon)<3 or _area(polygon)<1e-10:
                        continue
                    if sum(_cross(a,b) for a,b in zip(polygon,polygon[1:]+polygon[:1]))<0:
                        polygon.reverse()
                    result.append({'height':height, 'mouth':name, 'boundary':[(p[0],p[1]) for p in polygon],
                                   'bounds':(min(p[0] for p in polygon),max(p[0] for p in polygon),min(p[1] for p in polygon),max(p[1] for p in polygon))})
    _need(result, 'Saved wheeltrack check has no independent authorized corridor')
    return result


def inside_region(point, region, guard=CORRIDOR_GUARD):
    if abs(point[2]-region['height'])>1e-5:
        return False
    polygon=region['boundary']
    if 'bounds' in region:
        x0,x1,y0,y1=region['bounds']
        if not x0-guard<=point[0]<=x1+guard or not y0-guard<=point[1]<=y1+guard:
            return False
    return all(_cross((b[0]-a[0],b[1]-a[1]),(point[0]-a[0],point[1]-a[1]))
               >= -guard*math.dist(a,b) for a,b in zip(polygon,polygon[1:]+polygon[:1]))


class SurfaceIndex:
    """Index actual placed, indexed, flat pavement faces in two-metre bins."""
    def __init__(self, faces):
        self.faces, self.bins = list(faces), defaultdict(list)
        self.rgb_position_adjustments=[]
        for face in self.faces:
            points=face['points']
            for x in range(math.floor(min(p[0] for p in points)/2.),math.floor(max(p[0] for p in points)/2.)+1):
                for y in range(math.floor(min(p[1] for p in points)/2.),math.floor(max(p[1] for p in points)/2.)+1):
                    self.bins[x,y].append(face)

    def sample(self, point, texture=None):
        result=[]
        for face in self.bins.get((math.floor(point[0]/2.),math.floor(point[1]/2.)),()):
            if texture is not None and face['texture']!=texture:
                continue
            a,b,c=face['points']
            if abs(a[2]-point[2])>1e-5:
                continue
            determinant=_cross((b[0]-a[0],b[1]-a[1]),(c[0]-a[0],c[1]-a[1]))
            if abs(determinant)<1e-12:
                continue
            u=_cross((point[0]-a[0],point[1]-a[1]),(c[0]-a[0],c[1]-a[1]))/determinant
            v=_cross((b[0]-a[0],b[1]-a[1]),(point[0]-a[0],point[1]-a[1]))/determinant
            # Controls lie inside the saved surface. Do not extrapolate
            # through narrow native seam remnants using a distance guard.
            if min(u,v,1.-u-v)<-BARYCENTRIC_GUARD:
                continue
            uv=tuple((1-u-v)*face['uv'][0][i]+u*face['uv'][1][i]+v*face['uv'][2][i] for i in (0,1))
            if not any(old['texture']==face['texture'] and math.dist(old['uv'],uv)<1e-7 for old in result):
                result.append({'texture':face['texture'],'uv':uv})
        return result


def saved_faces(owners, resources):
    result=[]
    for owner in owners.values():
        model=parse_s3d(resources[owner['piece_id']][*S3D,owner['tile']+4])
        for mesh in model['meshes']:
            _need(len(mesh['frames'])==1,'Saved wheeltrack model must be static')
            vi,ii,pi,mi=mesh['frames'][0];textures=model['materials'][mi]['textures']
            if textures not in ([DD],[MIS]):
                continue
            block=model['vertices'][vi]
            vertices=[struct.unpack_from('<5f',block['data'],offset)
                      for offset in range(0,len(block['data']),block['stride'])]
            indices=model['indices'][ii]['values']
            for kind,start,count in model['primitives'][pi]:
                _need(kind==0 and count%3==0,'Saved wheeltrack model must use indexed triangles')
                for offset in range(start,start+count,3):
                    points,uv=[],[]
                    for i in indices[offset:offset+3]:
                        p=vertices[i];x,y=p[0]+16*owner['local_cell'][0],-p[2]-16*owner['local_cell'][1]
                        for _ in range(owner['angle']//90):x,y=-y,x
                        points.append((x+owner['origin'][0],y+owner['origin'][1],p[1]));uv.append(p[3:])
                    height=points[0][2]
                    if (min(abs(height-7.5),abs(height-15.))>1e-5
                            or any(abs(p[2]-height)>1e-5 for p in points)):
                        continue
                    if _cross((points[1][0]-points[0][0],points[1][1]-points[0][1]),
                              (points[2][0]-points[0][0],points[2][1]-points[0][1]))<=1e-12:
                        continue
                    result.append({'texture':textures[0],'points':points,'uv':uv,
                                   'material_sha256':hashlib.sha256(model['materials'][mi]['raw']).hexdigest()})
    return result


def at_s(points, s, mouth):
    for a,b in zip(points,points[1:]):
        x,y=local(a,mouth),local(b,mouth)
        if x[0]-1e-7<=s<=y[0]+1e-7 and y[0]-x[0]>1e-9:
            t=(s-x[0])/(y[0]-x[0]);q=x[1]+t*(y[1]-x[1])
            length=math.dist(x[:2],y[:2])
            return q, (y[0]-x[0])/length, (y[1]-x[1])/length
    raise ValueError('Saved wheeltrack PATH does not cover a required station')


def crossing(points, q, mouth):
    for a,b in zip(points,points[1:]):
        x,y=local(a,mouth),local(b,mouth)
        if x[1]<=q<=y[1] and y[1]-x[1]>1e-9 and x[0]>=-1e-5:
            return x[0]+(q-x[1])/(y[1]-x[1])*(y[0]-x[0])
    raise ValueError('Saved wheeltrack PATH does not cross a required lateral station')


def _target_u(mis_u):
    column=128.*mis_u-.5
    column=min(95.,max(65.,column+16.+min(1.,max(0.,(column-68.)/6.))))
    return (column+.5)/128.


def _one(index,point,texture):
    samples=index.sample(point,texture)
    _need(samples,'Saved wheeltrack pavement is missing at a reviewed control')
    return samples[0]


def _mouth_controls(index, mouth, seam):
    name=mouth[0];seams,boundaries=[],[]
    for offset in (-3.,-2.,-1.,0.,1.,2.,3.):
        dd=_one(index,world(seam+offset,8.-2e-5,mouth),DD)
        mis=_one(index,world(seam+offset,8.+2e-5,mouth),MIS)
        error=abs(dd['uv'][0]-_target_u(mis['uv'][0]))
        phase=abs((dd['uv'][1]-mis['uv'][1]+.5)%1.-.5)
        _need(error<=U_TOLERANCE,'Saved wheeltrack seam does not continue the native ramp transverse field')
        _need(phase<=PHASE_TOLERANCE,'Saved wheeltrack seam restarts the native ramp longitudinal phase')
        if offset==0.:
            _need(abs((mis['uv'][1]-mouth[8]+.5)%1.-.5)<=PHASE_TOLERANCE,
                  'Saved native ramp phase changed from the independently measured baseline')
        seams.append({'mouth':name,'s_offset_m':offset,'u_error':error,'phase_error_repeats':phase})
    taper,parallel=mouth[5:7]
    for s in (taper/2.,taper,taper+1.,taper+parallel/2.,taper+parallel,taper+parallel+2.):
        uv=_one(index,world(s,4.5+.0001,mouth),DD)['uv']
        _need(min(abs(uv[0]-end) for end in SAFE_U)<=U_TOLERANCE,
              'Saved wheeltrack inner boundary is dark instead of a neutral atlas edge')
        boundaries.append({'mouth':name,'s_m':s,'u':uv[0]})
    return seams,boundaries


def check_uv(faces, paths, regions):
    index=SurfaceIndex(faces);safe_faces=0;region_bins=defaultdict(list)
    for region in regions:
        x0,x1,y0,y1=region['bounds']
        for x in range(math.floor((x0-CORRIDOR_GUARD)/2),math.floor((x1+CORRIDOR_GUARD)/2)+1):
            for y in range(math.floor((y0-CORRIDOR_GUARD)/2),math.floor((y1+CORRIDOR_GUARD)/2)+1):
                region_bins[x,y].append(region)
    for face in faces:
        if face['texture']!=DD:
            continue
        height=face['points'][0][2];side=1 if abs(height-7.5)<1e-5 else -1
        polygon=[(*p,*uv) for p,uv in zip(face['points'],face['uv'])]
        polygon=_clip(_clip(polygon,lambda p:side*(p[1]-p[0]+136)/ROOT-4.5),
                      lambda p:8.-side*(p[1]-p[0]+136)/ROOT)
        if len(polygon)<3 or _area(polygon)<1e-9:
            continue
        def original(point):
            q=side*(point[1]-point[0]+136)/ROOT
            return (abs(point[3]-(.5-q/16.))<=3e-6
                    or (4.3125-2e-4<=q<=4.8125+2e-4 and abs(point[3]-29.5/128.)<=3e-6))
        if all(original(point) for point in polygon):
            continue
        _need(all(SAFE_U[0]-3e-6<=p[3]<=SAFE_U[1]+3e-6 for p in polygon),
              'Saved wheeltrack pavement crosses a native paint column or collapses its safe crop')
        _need(all(any(inside_region(p,r) for r in region_bins.get((math.floor(p[0]/2),math.floor(p[1]/2)),())) for p in polygon),
              'Saved wheeltrack UV changed pavement outside its authorized route corridor')
        safe_faces+=1
    _need(safe_faces,'Saved wheeltrack field is absent')
    seams,boundaries=[],[]
    for mouth in MOUTHS:
        rows,edges=_mouth_controls(index,mouth,crossing(paths[mouth[0]],8.,mouth))
        seams.extend(rows);boundaries.extend(edges)
    lobes=[]
    for name,point,expected_u in GREY_LOBE_CONTROLS:
        _need(any(r['mouth']==name and inside_region(point,r,guard=0.)for r in regions),
              'Independent folded-strip corridor omits a measured even-odd lobe')
        sample=_one(index,point,DD);error=abs(sample['uv'][0]-expected_u)
        _need(error<=LOBE_U_TOLERANCE,'Saved wheeltrack lobe retains a grey shoulder hole')
        lobes.append({'mouth':name,'point_m':list(point),'expected_u':expected_u,
                      'actual_uv':list(sample['uv']),'absolute_u_error':error})
    return {'passed':True,'safe_asphalt_faces_checked':safe_faces,'seam_controls_checked':len(seams),
            'neutral_inner_boundary_controls_checked':len(boundaries),'safe_u_range':list(SAFE_U),
            'u_tolerance':U_TOLERANCE,'phase_tolerance_repeats':PHASE_TOLERANCE,
            'saved_path_corridor_regions':len(regions),'corridor_reference_guard_m':CORRIDOR_GUARD,
            'sample_barycentric_guard':BARYCENTRIC_GUARD,'seams':seams,'boundaries':boundaries,
            'folded_strip_lobe_controls_checked':len(lobes),'folded_strip_lobe_u_tolerance':LOBE_U_TOLERANCE,
            'folded_strip_lobes':lobes,
            'native_rgb_tested':False,'game_rendering_tested':False,
            'coverage_limit':'Safe indexed asphalt crops, independent saved-PATH even-odd corridor membership, 28 measured seam UV/phase controls, 24 neutral inner-boundary controls, and five former grey-lobe locations; actual RGB, continuous field appearance, and game rendering require separate evidence.'}


def check_saved_wheeltracks(owners, resources, routes, path_report):
    paths=reviewed_paths(routes,path_report);regions=corridor_regions(paths)
    return check_uv(saved_faces(owners,resources),paths,regions),regions


# Independently checked canonical assembly poses, not recipe-generated origins.
_BRANCH_ORIGINS={'lower-exit-branch':(96.,-16.),'lower-entry-branch':(16.,-96.),
                 'upper-exit-branch':(0.,-112.),'upper-entry-branch':(112.,0.)}


def check_piece_controls(triangles,piece):
    key=piece.get('geometry_key')
    if key not in _BRANCH_ORIGINS:
        return None
    origin=_BRANCH_ORIGINS[key]
    name=key.replace('-exit-branch','-off').replace('-entry-branch','-on')
    mouth=next(row for row in MOUTHS if row[0]==name)
    faces=[]
    for face in triangles:
        if face['texture'] not in (DD,MIS) or not face.get('upward',False):
            continue
        if any(abs(p[2]-mouth[4])>1e-5 for p in face['points']):
            continue
        faces.append({**face,'points':[(p[0]+origin[0],p[1]+origin[1],p[2]) for p in face['points']]})
    _need(faces,'Saved branch has no pavement for affirmative wheeltrack controls')
    seam=20.112386349087025 if name.startswith('lower') else 30.81888787568175
    rows,edges=_mouth_controls(SurfaceIndex(faces),mouth,seam)
    return {'passed':True,'seam_uv_phase_controls':len(rows),'neutral_boundary_controls':len(edges),
            'scope':'Literal native seam and boundary controls from decoded branch pavement; complete corridor membership and native RGB require the separate assembly checks.'}


def check_piece_overhangs(triangles,piece,routes,controls):
    """Discharge pending UV-only native fragments using the actual car PATH."""
    pending=[face for face in triangles if face.get('pending_native_uv_fragment')]
    if not pending:
        return {'checked':True,'uv_only_native_fragments':0}
    key=piece.get('geometry_key')
    _need(key in _BRANCH_ORIGINS and controls is not None and controls.get('passed') is True,
          'Native overhang UV exception requires affirmative served-branch field controls')
    origin=_BRANCH_ORIGINS[key]
    name=key.replace('-exit-branch','-off').replace('-entry-branch','-on')
    mouth=next(row for row in MOUTHS if row[0]==name)
    points=[]
    for records in routes.values():
        for route in records:
            if route['transport']!=1:
                continue
            placed=[(p[0]+origin[0],p[1]+origin[1],p[2]) for p in route['points']]
            q=[local(p,mouth)[1] for p in placed]
            # Native through lanes are straight, constant-q routes. Only
            # the actual curved transfer channel defines this UV exception.
            if max(q)-min(q)<=.001:
                continue
            points.extend(p for p in placed if abs(p[2]-mouth[4])<=1e-5)
    ordered=[]
    for point in sorted(points,key=lambda p:local(p,mouth)[0]):
        if not ordered or math.dist(point,ordered[-1])>1e-6:
            ordered.append(point)
    _need(len(ordered)>2 and min(local(p,mouth)[1] for p in ordered)<4.5
          and max(local(p,mouth)[1] for p in ordered)>8.,
          'Native overhang UV exception has no complete saved curved transfer PATH')
    _need(all(math.dist(a,b)<1. for a,b in zip(ordered,ordered[1:])),
          'Native overhang UV exception has a disconnected saved transfer PATH')
    regions=corridor_regions({name:ordered},mouths=(mouth,))
    bins=defaultdict(list)
    for region in regions:
        x0,x1,y0,y1=region['bounds']
        for x in range(math.floor((x0-CORRIDOR_GUARD)/2.),math.floor((x1+CORRIDOR_GUARD)/2.)+1):
            for y in range(math.floor((y0-CORRIDOR_GUARD)/2.),math.floor((y1+CORRIDOR_GUARD)/2.)+1):
                bins[x,y].append(region)
    for face in pending:
        placed=[(p[0]+origin[0],p[1]+origin[1],p[2]) for p in face['points']]
        _need(face.get('upward',False) and face['texture']==DD
              and all(abs(p[2]-mouth[4])<=1e-5 for p in placed),
              'Native overhang UV exception requires upward served-deck DD asphalt')
        _need(all(SAFE_U[0]-3e-6<=u<=SAFE_U[1]+3e-6 for u,_v in face['uv']),
              'Native overhang UV exception leaves the safe native asphalt crop')
        _need(all(4.5-CORRIDOR_GUARD<=local(p,mouth)[1]<=8.+CORRIDOR_GUARD
                  and any(inside_region(p,r) for r in bins.get((math.floor(p[0]/2.),math.floor(p[1]/2.)),()))
                  for p in placed),
              'Native overhang UV exception leaves its saved curved transfer corridor')
    return {'checked':True,'uv_only_native_fragments':len(pending),
            'saved_curved_transfer_corridor_regions':len(regions),
            'corridor_reference_guard_m':CORRIDOR_GUARD,
            'scope':'Each pending fragment retains the exact pinned native material and lies on one original bounded XYZ donor triangle; only its UVs may change within the independently decoded served-deck car-PATH corridor. Native RGB remains a separate audit.'}


FSH_SHA256 = {DD:'25a91179a26a82ba6307777b1957c5862bee61daf55c7638c4487d64b275c7b8',
              MIS:'050264fbfd4aa3dbc9da4989c602b926abaab58cd18bc4747a6e19fb78a2bc8a'}
EMBEDDED_FSH_SHA256 = {DD:'6539c7d6d5a33e157c842724799a326f9f392a8282b0bbe27f74a2fe96ec6e7d',
                       MIS:'676fd00d3e3d608917274ed742ecf75e8253b4d6be20586a1eb19db5c3222105'}
RGBA_SHA256 = {DD:'3ff0c1dcdd4e987dd50c51f240055cccad5c0531619ce626f96447b5d33d1d11',
               MIS:'4356005bdc0f7ed5e5b96f9bb1274acb7afbf502266360dbbad0744ef51a5210'}


def _native_rgb_inputs(textures,provenance):
    """Pin the actual FSH encoding and the exact decoded first RGBA image."""
    records={int(row['instance'],16):row for row in provenance}
    actual={}
    for iid in (DD,MIS):
        digest=records.get(iid,{}).get('fsh_sha256')
        _need(iid in textures and digest in (FSH_SHA256[iid],EMBEDDED_FSH_SHA256[iid]),
              'Native RGB audit texture fingerprint differs')
        image=textures[iid]
        _need(tuple(image.shape)==(128,128,4),'Native RGB audit requires the pinned first128x128RGBA image')
        channels=[255.*float(value)for value in image.flat]
        _need(all(math.isfinite(value) and 0.<=value<=255. and abs(value-round(value))<=1e-5
                  for value in channels),'Native RGB audit image is not normalized byte RGBA')
        rgba=hashlib.sha256(bytes(round(value)for value in channels)).hexdigest()
        _need(rgba==RGBA_SHA256[iid],'Native RGB audit decoded first-image fingerprint differs')
        actual[iid]={'fsh_sha256':digest,'decoded_first_image_rgba_sha256':rgba}
    return actual


def sample_rgb(image, uv):
    """Sample a normalized native RGBA image using repeat/bilinear filtering."""
    _need(tuple(image.shape)==(128,128,4),'Native RGB audit requires the pinned 128-pixel RGBA images')
    x,y=128.*uv[0]-.5,128.*uv[1]-.5
    ix,iy=math.floor(x),math.floor(y);a,b=x-ix,y-iy
    colour=((1-a)*(1-b)*image[iy%128,ix%128]+a*(1-b)*image[iy%128,(ix+1)%128]
            +(1-a)*b*image[(iy+1)%128,ix%128]+a*b*image[(iy+1)%128,(ix+1)%128])
    return [255.*float(v) for v in colour[:3]]


def _nearest_rgb_surface(index,point,texture):
    """Project onto actual pinned pavement, never extrapolate its UVs."""
    _need(texture==DD and min(abs(point[2]-7.5),abs(point[2]-15.))<=1e-5,
          'RGB control has no eligible native DD deck for a bounded projection')
    candidates=[];seen=set()
    bx,by=math.floor(point[0]/2.),math.floor(point[1]/2.)
    for x in range(bx-1,bx+2):
        for y in range(by-1,by+2):
            for face in index.bins.get((x,y),()):
                if id(face) in seen:
                    continue
                seen.add(id(face));points=face['points']
                if (face['texture']!=DD or face.get('material_sha256')!=DD_MATERIAL_SHA256
                        or any(p[2]!=points[0][2]for p in points)
                        or abs(points[0][2]-point[2])>RGB_POSITION_LIMIT_M):
                    continue
                for i,j in ((0,1),(1,2),(2,0)):
                    a,b=points[i],points[j];edge=[v-u for u,v in zip(a,b)];square=sum(v*v for v in edge)
                    fraction=max(0.,min(1.,sum((p-u)*v for p,u,v in zip(point,a,edge))/square)) if square else 0.
                    actual=tuple(u+fraction*v for u,v in zip(a,edge));distance=math.dist(point,actual)
                    if distance<=RGB_POSITION_LIMIT_M:
                        uv=tuple((1.-fraction)*face['uv'][i][axis]+fraction*face['uv'][j][axis]for axis in (0,1))
                        candidates.append((distance,actual,uv))
    _need(candidates,'RGB control is farther than two micrometres from pinned native pavement')
    distance,actual,uv=min(candidates,key=lambda row:row[0])
    adjustment={'requested_point_m':list(point),'actual_point_m':list(actual),'distance_m':distance,
                'texture':f'{texture:08x}','native_material_sha256':DD_MATERIAL_SHA256}
    index.rgb_position_adjustments.append(adjustment)
    return {'uv':uv,'position_adjustment':adjustment}


def _rgb(index,point,texture,textures):
    samples=index.sample(point,texture)
    surface=samples[0] if samples else _nearest_rgb_surface(index,point,texture)
    result={'uv':list(surface['uv']),'rgb':sample_rgb(textures[texture],surface['uv'])}
    if 'position_adjustment' in surface:
        result['position_adjustment']=surface['position_adjustment']
    return result


def _difference(a,b):
    return max(abs(x-y) for x,y in zip(a['rgb'],b['rgb']))


def audit_native_rgb(faces, paths, textures, provenance):
    """Measure pinned native RGB from actual saved triangles, never UV alone.

    These are unlit software samples at explicit positions. They do not
    establish the game's filtering, camera appearance, or every field point.
    """
    actual_inputs=_native_rgb_inputs(textures,provenance)
    index=SurfaceIndex(faces);central=[];dense=[];boundaries=[];onsets=[];internal=[]
    for mouth in MOUTHS:
        name=mouth[0];points=paths[name];seam=crossing(points,8.,mouth)
        for delta in (-3.,-2.,-1.,0.,1.,2.,3.):
            dd=_rgb(index,world(seam+delta,8.-2e-5,mouth),DD,textures)
            mis=_rgb(index,world(seam+delta,8.+2e-5,mouth),MIS,textures)
            jump=_difference(dd,mis)
            _need(jump<=4.,'Native RGB wheeltrack central seam exceeds four channel levels')
            central.append({'mouth':name,'s_offset_m':delta,'dd':dd,'mis':mis,'maximum_channel_jump':jump})
        for step in range(-48,49):
            s=seam+step*.125
            samples=index.sample(world(s,8.+2e-5,mouth),MIS)
            if not samples:
                continue  # Outside the measured ramp's physical pavement.
            if not 48.5/128.-3e-6<=samples[0]['uv'][0]<=78.5/128.+3e-6:
                continue
            dd=_rgb(index,world(s,8.-2e-5,mouth),DD,textures)
            mis={'uv':list(samples[0]['uv']),'rgb':sample_rgb(textures[MIS],samples[0]['uv'])}
            jump=_difference(dd,mis)
            _need(jump<=6.,'Native RGB wheeltrack dense unpainted seam exceeds six channel levels')
            dense.append({'mouth':name,'s_m':s,'dd':dd,'mis':mis,'maximum_channel_jump':jump})
        taper,parallel=mouth[5:7]
        for s in (taper/2.,taper,taper+1.,taper+parallel/2.,taper+parallel,taper+parallel+2.):
            before=_rgb(index,world(s,4.5-.0001,mouth),DD,textures)
            after=_rgb(index,world(s,4.5+.0001,mouth),DD,textures)
            jump=_difference(before,after)
            _need(jump<=8.,'Native RGB wheeltrack exterior boundary exceeds eight channel levels')
            boundaries.append({'mouth':name,'s_m':s,'before':before,'after':after,'maximum_channel_jump':jump})
        onset=crossing(points,4.5,mouth);rows=[]
        for step in range(-10,21):
            s=onset+step*.05;q,tx,tq=at_s(points,s,mouth)
            tracks=[]
            for offset in (-.2,-.0001,0.,.0001,.2):
                target=world(s-offset*tq,q+offset*tx,mouth)
                tracks.append({'normal_offset_m':offset,**_rgb(index,target,DD,textures)})
            rows.append({'s_offset_from_q4_5_path_m':step*.05,'s_m':s,'q_m':q,'tracks':tracks})
            jump=_difference(tracks[1],tracks[3])
            _need(jump<=10.,'Native RGB wheeltrack internal half-ribbon seam exceeds ten channel levels')
            internal.append({'mouth':name,'s_offset_from_q4_5_path_m':step*.05,'maximum_channel_jump':jump})
        changes=[]
        for first,last in zip(rows,rows[1:]):
            for a,b in zip(first['tracks'],last['tracks']):
                jump=_difference(a,b)
                _need(jump<=12.,'Native RGB wheeltrack longitudinal onset exceeds twelve channel levels')
                changes.append(jump)
        onsets.append({'mouth':name,'s_at_q4_5_path_m':onset,'rows':rows,
                       'maximum_adjacent_channel_change':max(changes)})
    _need(len(dense)>=250,'Native RGB audit did not cover the reviewed full-width seam sample set')
    return {'passed':True,'native_inputs':{f'{k:08x}':v for k,v in actual_inputs.items()},
            'native_fsh_sha256':{f'{k:08x}':v['fsh_sha256']for k,v in actual_inputs.items()},
            'native_first_image_rgba_sha256':{f'{k:08x}':v for k,v in RGBA_SHA256.items()},
            'embedded_mipmap_levels_sampled':False,
            'central_seam_pairs_checked':len(central),'central_seam_limit':4.,
            'maximum_central_seam_channel_jump':max(r['maximum_channel_jump'] for r in central),
            'dense_unpainted_seam_pairs_checked':len(dense),'dense_seam_step_s_m':.125,
            'dense_mis_u_window':[48.5/128.,78.5/128.],'dense_u_selection_guard':3e-6,'dense_seam_limit':6.,
            'maximum_dense_seam_channel_jump':max(r['maximum_channel_jump'] for r in dense),
            'exterior_boundary_pairs_checked':len(boundaries),'exterior_boundary_limit':8.,
            'maximum_exterior_boundary_channel_jump':max(r['maximum_channel_jump'] for r in boundaries),
            'onset_path_centres_checked':sum(len(r['rows']) for r in onsets),'onset_step_s_m':.05,
            'onset_s_window_m':[-.5,1.],'onset_normal_offsets_m':[-.2,-.0001,0.,.0001,.2],
            'onset_adjacent_step_limit':12.,'maximum_onset_adjacent_channel_change':max(r['maximum_adjacent_channel_change'] for r in onsets),
            'internal_half_ribbon_pairs_checked':len(internal),'internal_seam_limit':10.,
            'maximum_internal_half_ribbon_channel_jump':max(r['maximum_channel_jump'] for r in internal),
            'accepted_private_proof04_sampled_internal_residual':8.808628556549046,
            'position_adjustment_limit_m':RGB_POSITION_LIMIT_M,
            'position_adjustments':index.rgb_position_adjustments,
            'maximum_position_adjustment_m':max((r['distance_m']for r in index.rgb_position_adjustments),default=0.),
            'central':central,'dense':dense,'boundaries':boundaries,'onsets':onsets,'internal':internal,
            'native_pixels_included':False,'game_rendering_tested':False,
            'coverage_limit':'Pinned unlit native RGB at the reported saved-face seam, boundary, and longitudinal controls, including both internal UV flanks. These sampled limits do not prove continuous full-field colour, game filtering, every camera view, or exact colour equality across the internal UV seam.'}


def export_corridors(owners, regions, baseline_sha256, candidate_sha256):
    """Neutral preview-coordinate exception geometry for a separate UV audit."""
    branch_ids={'ddrhw-diagonal-'+key for key in _BRANCH_ORIGINS}
    branch_owners={owner['piece_id']:owner for owner in owners.values()
                   if owner['piece_id'] in branch_ids}
    _need(branch_owners, 'Independent corridor export has no placed branch owner')
    pieces=defaultdict(list)
    for region in regions:
        # Offset crossings were already split into their exact even-odd
        # lobes before clipping. Normalize each resulting convex directed
        # boundary for the separate polygon audit, without adding the
        # checker's reference-position guard or a convex-hull expansion.
        boundary=region['boundary']
        x0,x1=min(p[0] for p in boundary),max(p[0] for p in boundary)
        y0,y1=min(p[1] for p in boundary),max(p[1] for p in boundary)
        effective=[(x0,y0),(x1,y0),(x1,y1),(x0,y1)]
        for a,b in zip(boundary,boundary[1:]+boundary[:1]):
            effective=_clip(effective,lambda p,a=a,b=b:
                            _cross((b[0]-a[0],b[1]-a[1]),(p[0]-a[0],p[1]-a[1])))
        unique=[]
        for point in effective:
            if not unique or math.dist(point,unique[-1])>1e-12:
                unique.append(point)
        if len(unique)>1 and math.dist(unique[0],unique[-1])<=1e-12:
            unique.pop()
        effective=unique
        if len(effective)<3 or _area(effective)<1e-10:
            continue
        # A branch retains native surfaces on both decks. An owned tile can
        # therefore carry another mouth's field; nominal mouth names do not
        # define physical ownership. Export the identical world polygons in
        # every actual branch pose, then let the consumer intersect matching
        # saved pavement heights. This adds no world-space exception area.
        for pid,owner in branch_owners.items():
            polygon=[]
            for east,north in effective:
                x,y=east-owner['origin'][0],north-owner['origin'][1]
                for _ in range(owner['angle']//90):x,y=y,-x
                polygon.append([x,-y])
            pieces[pid].append({'height_m':region['height'],'boundary_xz_m':polygon})
    return {'baseline_manifest_sha256':baseline_sha256,'candidate_manifest_sha256':candidate_sha256,
            'pieces':dict(pieces),'scope':'Convex even-odd lobes of offset strips independently reconstructed from unchanged saved transfer PATHs, split at actual nonadjacent-edge intersections before clipping q4.5..8 and s>=0. The same world regions are transformed into each actual branch pose because retained native decks can carry another mouth field; consumers still intersect actual saved surfaces at matching heights. There is no convex-hull or reference-position-guard expansion; these are permitted UV regions, not a writer-generated exception mask.'}
