"""Independently inspect saved highway pavement, car paths, and solid faces.

No road builder is imported. Indexed S3D triangles and encoded SC4PATH points
are the evidence. Pavement coverage is continuous along every encoded car
segment, rather than a check of its nodes alone. The corridor test intersects
triangle faces with a narrow, graded prism; it is not a full vehicle swept
volume, a closed-solid containment proof, or an in-game observation.
"""
from __future__ import annotations

from collections import OrderedDict
from copy import deepcopy
import importlib
import json
import math
import hashlib
from pathlib import Path
import re
import struct

from scp.dbpf import decompress
from scp.models import parse_s3d, validate_s3d
from scp.track_paths import PATH, S3D

TEXTURE = (0x7AB50E44, 0x1ABE787D)
POSITION_TOLERANCE = 2e-4
UV_TOLERANCE = 1e-6
MARKING_TOLERANCE = 0.03
DD_MATERIAL_SHA256 = '307aba7786d4b4f11dbc499eb54f7d05d01a114001919b8a5f7d55970fbb64ca'
SUPPORT_ENCODING_DISTANCE_M = 2e-6
_SIDES = ((0, -8.0), (1, 8.0), (0, 8.0), (1, -8.0))
_NEIGHBOURS = ((-1, 0), (0, -1), (1, 0), (0, 1))


def _need(condition, message):
    if not condition:
        raise ValueError(message)


def _grade_bound(piece):
    """Keep the compact subject's 30% contract separate from generic probes."""
    compact = piece.get('recipe','').startswith('highway_ddrhw_compact_') or bool(piece.get('geometry_key'))
    ceiling = 30.0 if compact else 40.0
    bound = piece.get('engineering',{}).get('max_grade_percent')
    _need(type(bound) in (int,float) and math.isfinite(bound) and 0.0 < bound <= ceiling,
          f'Highway engineering max_grade_percent must declare a bound no greater than {ceiling:g} percent')
    return bound


def _rotate(point, turns):
    east, north, height = point
    for _ in range(turns % 4):
        east, north = north, -east
    return east, north, height


def _rotate_cell(cell, turns):
    column, row = cell
    for _ in range(turns % 4):
        column, row = -row, column
    return column, row


def _paths(raw):
    """Strictly parse the saved 1.2 road contract, including declared empties."""
    lines = [line.strip() for line in decompress(raw).decode('ascii').splitlines()
             if line.strip() and not line.lstrip().startswith('--')]
    _need(len(lines) >= 5 and lines[:2] == ['SC4PATHS', '1.2']
          and lines[3:5] == ['0', '0'], 'Highway PATH must use flat, zero-stop SC4PATHS 1.2')
    count, cursor = int(lines[2]), 5
    _need(count >= 0, 'Negative highway PATH route count')
    routes, identities = [], set()
    for _ in range(count):
        _need(cursor+6 <= len(lines), 'Truncated highway PATH metadata')
        transport, lane, entry, exit_, junction, size = map(int, lines[cursor:cursor+6])
        cursor += 6
        _need(transport in (1, 2), 'Unexpected highway PATH transport; only car 1 and pedestrian 2 are allowed')
        _need(lane >= 0 and junction in (0, 1), 'Unexpected highway PATH class or junction flag')
        _need(entry in range(4) and exit_ in range(4), 'Unexpected highway PATH entry or exit flag')
        _need(size >= 2 and cursor+size <= len(lines), 'Truncated highway PATH points')
        points = [tuple(map(float, line.split(','))) for line in lines[cursor:cursor+size]]
        cursor += size
        _need(all(len(p) == 3 and all(math.isfinite(v) for v in p) for p in points),
              'Highway PATH coordinates must contain three finite numbers')
        _need(all(abs(p[0]) <= 8.0+POSITION_TOLERANCE and abs(p[1]) <= 8.0+POSITION_TOLERANCE
                  for p in points), 'Highway PATH leaves its owning tile')
        identity = transport, lane, entry, exit_
        _need(identity not in identities, 'Duplicate highway PATH class within a transport/side pair')
        identities.add(identity)
        for first, last in zip(points, points[1:]):
            _need(math.dist(first[:2], last[:2]) > 1e-9, 'Stationary or vertical highway PATH segment')
        for endpoint, other, side, direction in ((points[0], points[1], entry, 'in'),
                                                  (points[-1], points[-2], exit_, 'out')):
            axis, value = _SIDES[side]
            _need(abs(endpoint[axis]-value) <= POSITION_TOLERANCE,
                  'Highway PATH entry or exit flag disagrees with its actual tile boundary')
            inside = other[axis]-endpoint[axis]
            _need(inside*(-1.0 if value > 0.0 else 1.0) > 1e-10,
                  'Highway PATH does not approach the declared tile side from inside')
        routes.append({'transport':transport, 'class':lane, 'entry':entry,
                       'exit':exit_, 'junction':junction, 'points':points})
    _need(cursor == len(lines), 'Unexpected trailing highway PATH data')
    return routes


def _native_signature(points,material):
    vertices = b''.join(struct.pack('<5f',*(0.0 if value == 0.0 else value for value in point))
                        for point in sorted(tuple(point) for point in points))
    return hashlib.sha256(material['raw']+vertices).hexdigest()


def native_overhang_contract(donors,*,include_surfaces=False):
    """Pin original overhanging faces from externally audited native inputs.

    Only the fixed measured DD/Avenue donor families and their four proper
    rotations are admitted. Material bytes and every XYZ/UV attribute must
    match. Callers must supply the build's fingerprint-verified donor map.
    """
    result,surfaces = set(),set()
    for iid in (0x5753A380,0x5753A300,0x5753A305,0x57530200):
        raw = donors.get((*S3D,iid))
        if raw is None:
            continue
        model = parse_s3d(decompress(raw))
        # The pinned native source retains unused buffers. Inspect only its
        # actual referenced faces; output models still receive full validation.
        for mesh in model['meshes']:
            vi,ii,pi,mi = mesh['frames'][0]
            block = model['vertices'][vi]
            points = [struct.unpack_from('<5f',block['data'],offset)
                      for offset in range(0,len(block['data']),block['stride'])]
            indices = model['indices'][ii]['values']
            for _kind,first,count in model['primitives'][pi]:
                for offset in range(first,first+count,3):
                    triangle = [points[index] for index in indices[offset:offset+3]]
                    for quarter in range(4):
                        rotated = []
                        for x,height,z,u,v in triangle:
                            for _ in range(quarter):
                                x,z = -z,x
                            rotated.append((x,height,z,u,v))
                        if any(abs(p[0]) > 8.0+POSITION_TOLERANCE or abs(p[2]) > 8.0+POSITION_TOLERANCE
                               for p in rotated):
                            result.add(_native_signature(rotated,model['materials'][mi]))
                            surfaces.add((hashlib.sha256(model['materials'][mi]['raw']).hexdigest(),tuple(rotated)))
    return (result,surfaces) if include_surfaces else result


def _native_fragment(points,material,*,preserve_uv=True):
    from .native_overhangs import NATIVE_OVERHANG_SURFACES
    digest = hashlib.sha256(material['raw']).hexdigest()
    for expected,triangle in NATIVE_OVERHANG_SURFACES:
        if expected != digest:
            continue
        a,b,c = triangle
        u,v = [b[i]-a[i] for i in range(3)],[c[i]-a[i] for i in range(3)]
        uu,uv,vv = sum(x*x for x in u),sum(x*y for x,y in zip(u,v)),sum(x*x for x in v)
        determinant = uu*vv-uv*uv
        if determinant <= 1e-16:
            continue
        matched = True
        for point in points:
            w = [point[i]-a[i] for i in range(3)]
            wu,wv = sum(x*y for x,y in zip(w,u)),sum(x*y for x,y in zip(w,v))
            second,third = (vv*wu-uv*wv)/determinant,(uu*wv-uv*wu)/determinant
            first = 1.0-second-third
            reconstructed = [first*a[i]+second*b[i]+third*c[i] for i in range(5)]
            bounded_distance = math.dist(point[:3],reconstructed[:3])
            if min(first,second,third) < 0.0:
                distances = []
                for begin,end in ((a,b),(b,c),(c,a)):
                    edge = [end[i]-begin[i] for i in range(3)]
                    square = sum(value*value for value in edge)
                    fraction = max(0.0,min(1.0,sum((point[i]-begin[i])*edge[i] for i in range(3))/square)) if square else 0.0
                    distances.append(math.dist(point[:3],[begin[i]+fraction*edge[i] for i in range(3)]))
                bounded_distance = min(distances)
            if (bounded_distance > 2e-5 or math.dist(point[:3],reconstructed[:3]) > 2e-5
                    or (preserve_uv and max(abs(point[i]-reconstructed[i]) for i in (3,4)) > 2e-6)):
                matched = False
                break
        if matched:
            return True
    return False


def _triangles(raw, cell, native_overhangs=(),*,pending_native_uv=False):
    """Read actual indexed faces, mapping S3D south=-PATH north explicitly."""
    model = parse_s3d(decompress(raw))
    validate_s3d(model)
    result = []
    for mesh in model['meshes']:
        _need(len(mesh['frames']) == 1, 'Highway pavement checker requires static S3D meshes')
        vi, ii, pi, mi = mesh['frames'][0]
        block = model['vertices'][vi]
        _need(block['stride'] >= 20, 'Highway mesh needs position and UV coordinates')
        vertices = [struct.unpack_from('<5f', block['data'], offset)
                    for offset in range(0, len(block['data']), block['stride'])]
        _need(all(all(math.isfinite(v) for v in p) for p in vertices), 'Nonfinite highway S3D position or UV')
        textures = model['materials'][mi]['textures']
        _need(len(textures) == 1, 'Highway pavement requires one texture per mesh material')
        indices = model['indices'][ii]['values']
        for kind, first, size in model['primitives'][pi]:
            _need(kind == 0 and size % 3 == 0, 'Highway S3D needs indexed triangle lists')
            for offset in range(first, first+size, 3):
                source = [vertices[index] for index in indices[offset:offset+3]]
                deferred=False
                if any(abs(p[0]) > 8.0+POSITION_TOLERANCE or abs(p[2]) > 8.0+POSITION_TOLERANCE for p in source):
                    strict=(_native_signature(source,model['materials'][mi]) in native_overhangs
                            or _native_fragment(source,model['materials'][mi]))
                    if not strict:
                        deferred=(pending_native_uv and textures==[0x5713000E]
                                  and min(abs(source[0][1]-7.5),abs(source[0][1]-15.))<=1e-5
                                  and all(abs(p[1]-source[0][1])<=1e-6 for p in source)
                                  and _native_fragment(source,model['materials'][mi],preserve_uv=False))
                    _need(strict or deferred,
                          'Highway model leaves its owned source tile without an exact audited native overhang triangle/material match')
                # World (east, north, height), keeping the actual winding.
                points = tuple((p[0]+16.0*cell[0], -p[2]-16.0*cell[1], p[1]) for p in source)
                area = ((points[1][0]-points[0][0])*(points[2][1]-points[0][1])
                        -(points[1][1]-points[0][1])*(points[2][0]-points[0][0]))
                result.append({'points':points, 'upward':area > 1e-12,
                               'texture':textures[0], 'uv':tuple((p[3],p[4]) for p in source),
                               'material_sha256':hashlib.sha256(model['materials'][mi]['raw']).hexdigest(),
                               'pending_native_uv_fragment':deferred})
    _need(result, 'Highway model contains no indexed triangles')
    return result


def _atlas(resources, piece, engineering, triangles):
    """Check authored atlas bytes independently of a mesh name or UV label."""
    ids = piece.get('authored_texture_ids', [])
    if not ids:
        if piece.get('recipe', '').startswith('highway_ddrhw_compact_') or piece.get('geometry_key'):
            from .wheeltrack_verify import check_piece_controls
            controls=check_piece_controls(triangles,piece)
            return _native_appearance(triangles,neutral_field_controls=controls)
        return {'checked':False, 'reason':'No authored atlas declared; support uses actual upward saved faces.'}
    _need(ids == [piece['tile_ids'][0]], 'Authored highway atlas must use the first reserved tile ID')
    iid = int(ids[0], 16)
    _need((*TEXTURE,iid) in resources, 'Missing saved authored highway atlas')
    raw = decompress(resources[*TEXTURE,iid])
    _need(len(raw) >= 40 and raw[:4] == b'SHPI', 'Invalid saved highway FSH atlas')
    size, count = struct.unpack_from('<II', raw, 4)
    offset, = struct.unpack_from('<I', raw, 20)
    _need(size == len(raw) and count == 1 and offset+16 <= len(raw), 'Unexpected highway atlas directory')
    code, width, height = struct.unpack_from('<IHH', raw, offset)
    _need(code & 255 == 0x7D and width >= 4 and height > 0
          and offset+16+width*height*4 == len(raw), 'Highway atlas must contain one complete opaque BGRA image')
    pavement_u = engineering.get('pavement_uv_u', 0.125)
    solid_u = engineering.get('solid_uv_u', 0.375)
    _need(pavement_u == 0.125 and solid_u == 0.375, 'Unexpected authored pavement or solid atlas column')
    colors = ((53,55,58,255), (147,151,153,255), (235,235,218,255), (231,176,44,255))
    pixels = raw[offset+16:]
    for row in range(height):
        for column in range(width):
            red, green, blue, alpha = colors[min(3,column*4//width)]
            index = 4*(row*width+column)
            _need(pixels[index:index+4] == bytes((blue,green,red,alpha)), 'Saved highway atlas color or opacity changed')
    owned = [face for face in triangles if face['texture'] == iid]
    _need(owned, 'Authored highway atlas is not referenced by any saved triangle')
    for face in owned:
        _need(all(abs(v-0.5) <= UV_TOLERANCE
                  and any(abs(u-center) <= UV_TOLERANCE for center in (0.125,0.375,0.625,0.875))
                  and abs(u-face['uv'][0][0]) <= UV_TOLERANCE
                  for u,v in face['uv']), 'Authored road triangle uses an unexpected atlas sample')
    return {'checked':True, 'texture_id':ids[0], 'pavement_uv_u':pavement_u,
            'solid_uv_u':solid_u, 'owned_triangles':len(owned)}


def _native_appearance(triangles, *, neutral_field_controls=None):
    """Pin actual native flags and require spatial UVs, independently of names.

    These measured fingerprints come from the retained DD crossing and the
    genuine NAM MIS slope 57722000. Native FSH images stay in NAM; the saved
    custom resource must reference their existing identities directly.
    """
    allowed = {
        0x5713000E: DD_MATERIAL_SHA256,
        0x5712000E: 'ed1b4a35ab986ff74a56ac79a1a33f579c31bf9630e7bb2b79ad4a4d9b6739ca',
        0x5EB4BEE9: 'd81e8d70e3ab9182adb393f2bc6a61608c70f8129cdb06631409a4b19c73e306',
        0x5EB4BEEE: 'cf4e393b8ca3a2b3d0edba0f86bb197ddf82b65e85cf73cfa13ebd4d2a8c6f6e',
        0x0400020E: 'b9e662590684786bfeca084538ef53fcd70c9c6beb489c2ea94f3d001ea2a6e5',
        0x0400380E: 'e481f8838ddc4e494a5fc2854007dbc319541a70d11ea3cbfd01f03c7a57bda1',
    }
    counts = {};neutral_fragments=0
    for face in triangles:
        iid = face['texture']
        _need(iid in allowed and face['material_sha256'] == allowed[iid],
              'Saved highway material differs from the measured native NAM surface')
        spatial=any(max(uv[axis] for uv in face['uv'])-min(uv[axis] for uv in face['uv'])>1e-8 for axis in (0,1))
        if not spatial:
            points=face['points']
            neutral=(neutral_field_controls is not None and neutral_field_controls.get('passed') is True
                     and iid==0x5713000E and face.get('upward',False)
                     and all(abs(p[2]-points[0][2])<=1e-6 for p in points)
                     and min(abs(points[0][2]-7.5),abs(points[0][2]-15.))<=1e-5
                     and face['uv'][0][0] in (65.5/128.,95.5/128.)
                     and all(uv==face['uv'][0] for uv in face['uv'])
                     and max(math.dist(a,b) for a,b in zip(points,points[1:]+points[:1]))<=.125+2e-5)
            _need(neutral,'Native highway UVs collapse to a flat colour sample')
            neutral_fragments+=1
        if iid == 0x5712000E:
            _need(all(0.125-UV_TOLERANCE <= u <= 0.875+UV_TOLERANCE for u,_v in face['uv']),
                  'MIS ramp UVs leave the measured one-lane pavement strip')
        counts[f'{iid:08X}'] = counts.get(f'{iid:08X}',0)+1
    _need(counts, 'Native highway appearance has no actual saved faces')
    return {'checked':True, 'style':'native NAM DD RHW-4 and MIS slope',
            'native_slope_s3d_instance':'57722000', 'native_texture_triangles':counts,
            'owned_texture_resources':0, 'spatial_uvs_checked':True,
            'neutral_one_texel_fragments_checked':neutral_fragments,
            'neutral_field_controls':neutral_field_controls}


def _barycentric(point, triangle):
    a,b,c = triangle
    determinant = (b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
    if abs(determinant) <= 1e-12:
        return None
    one = ((b[1]-c[1])*(point[0]-c[0])+(c[0]-b[0])*(point[1]-c[1]))/determinant
    two = ((c[1]-a[1])*(point[0]-c[0])+(a[0]-c[0])*(point[1]-c[1]))/determinant
    return one,two,1.0-one-two


def _interval(first, last, triangle):
    """Return where the complete linear PATH segment lies on this triangle."""
    start, end = _barycentric(first,triangle), _barycentric(last,triangle)
    if start is None:
        return None
    low, high = 0.0, 1.0
    for a,b in zip(start,end):
        delta = b-a
        if abs(delta) < 1e-14:
            if a < -1e-7:
                return None
        elif delta > 0.0:
            low = max(low,(-1e-7-a)/delta)
        else:
            high = min(high,(-1e-7-a)/delta)
    if low > high or high < 0.0 or low > 1.0:
        return None
    low,high = max(0.0,low),min(1.0,high)
    for fraction in (low,high):
        weights = [a+fraction*(b-a) for a,b in zip(start,end)]
        pavement = sum(weight*point[2] for weight,point in zip(weights,triangle))
        route = first[2]+fraction*(last[2]-first[2])
        if abs(pavement-route) > POSITION_TOLERANCE:
            return None
    return low,high


def _edge_capsule_intervals(first,last,a,b,radius):
    """Exact line intervals within a finite edge's rectangle or endpoint discs."""
    dx,dy=last[0]-first[0],last[1]-first[1]
    length_squared=dx*dx+dy*dy
    if length_squared<=1e-24:
        return []
    ex,ey=b[0]-a[0],b[1]-a[1];edge=math.hypot(ex,ey)
    result=[]
    if edge>1e-15:
        ex,ey=ex/edge,ey/edge
        low,high=0.,1.
        for value,delta,minimum,maximum in (
                ((first[0]-a[0])*ex+(first[1]-a[1])*ey,dx*ex+dy*ey,0.,edge),
                (ex*(first[1]-a[1])-ey*(first[0]-a[0]),ex*dy-ey*dx,-radius,radius)):
            if abs(delta)<=1e-18:
                if not minimum<=value<=maximum:
                    low,high=1.,0.;break
            else:
                begin,end=(minimum-value)/delta,(maximum-value)/delta
                low,high=max(low,min(begin,end)),min(high,max(begin,end))
        if low<=high:
            result.append((low,high))
    for vertex in (a,b):
        vx,vy=vertex[0]-first[0],vertex[1]-first[1]
        centre=(vx*dx+vy*dy)/length_squared
        perpendicular_squared=(dx*vy-dy*vx)**2/length_squared
        remaining=radius*radius-perpendicular_squared
        if remaining<0.:
            continue
        half=math.sqrt(remaining/length_squared)
        low,high=max(0.,centre-half),min(1.,centre+half)
        if low<=high:
            result.append((low,high))
    return result


def _point_triangle_distance(point,triangle):
    """Euclidean distance to one horizontal, closed triangle footprint."""
    weights=_barycentric(point,triangle)
    if weights is not None and min(weights)>=0.:
        return abs(point[2]-triangle[0][2])
    distances=[]
    for a,b in zip(triangle,triangle[1:]+triangle[:1]):
        edge=[y-x for x,y in zip(a,b)];square=sum(x*x for x in edge)
        fraction=max(0.,min(1.,sum((p-x)*d for p,x,d in zip(point,a,edge))/square)) if square else 0.
        distances.append(math.dist(point,[x+fraction*d for x,d in zip(a,edge)]))
    return min(distances)


def _covered(first,last,triangles,*,encoding=None,precision_report=None):
    """Keep strict support, with a separate bounded native-footprint distance proof.

    Only strict uncovered spans on affirmative flat served-deck branches may
    use the union of pinned DD triangle-edge capsules. Finite edge rectangles
    plus endpoint discs prove distance at most two micrometres without acute
    corner/miter extrapolation. Barycentric and height tests stay unchanged.
    """
    from .wheeltrack_verify import _BRANCH_ORIGINS
    enabled=(encoding is not None and encoding.get('geometry_key') in _BRANCH_ORIGINS
             and encoding.get('field_controls') is not None
             and encoding['field_controls'].get('passed') is True)
    deck=(7.5 if encoding['geometry_key'].startswith('lower') else 15.) if enabled else None
    enabled=(enabled and abs(first[2]-deck)<=1e-5 and abs(last[2]-deck)<=1e-5
             and first[2]==last[2])
    def native_top(face):
        return (face is not None and face.get('upward',False)
                and face['texture']==0x5713000E
                and face.get('material_sha256')==DD_MATERIAL_SHA256
                and all(abs(p[2]-deck)<=1e-5 for p in face['points'])
                and all(p[2]==face['points'][0][2]for p in face['points']))
    triangles=list(triangles)
    intervals=sorted(((*interval,face) for face in triangles if face['upward']
                      if (interval:=_interval(first,last,face['points'])) is not None),
                     key=lambda row:row[:2])
    gaps=[];end=0.
    for low,high,_face in intervals:
        if low>end+1e-7:
            gaps.append((end,low))
        end=max(end,high)
    if end<1.-1e-7:
        gaps.append((end,1.))
    if not gaps:
        return True
    if not enabled:
        return False
    qualified=[face for face in triangles if native_top(face)]
    admitted=[];sampled=[]
    def at(fraction):
        return tuple(a+fraction*(b-a)for a,b in zip(first,last))
    for low,high in gaps:
        begin,end=at(low),at(high);near=[];capsules=[]
        for face in qualified:
            points=face['points'];height=abs(first[2]-points[0][2])
            if height>SUPPORT_ENCODING_DISTANCE_M or any(
                    max(p[axis]for p in points)<min(begin[axis],end[axis])-SUPPORT_ENCODING_DISTANCE_M
                    or min(p[axis]for p in points)>max(begin[axis],end[axis])+SUPPORT_ENCODING_DISTANCE_M
                    for axis in (0,1)):
                continue
            near.append(face)
            radius=math.sqrt(max(0.,SUPPORT_ENCODING_DISTANCE_M**2-height**2))
            for a,b in zip(points,points[1:]+points[:1]):
                capsules.extend((max(low,x),min(high,y)) for x,y in
                                _edge_capsule_intervals(first,last,a,b,radius)
                                if y>=low and x<=high)
        reached=low
        for x,y in sorted(capsules):
            if x>reached+1e-12:
                break
            reached=max(reached,y)
            if reached>=high-1e-12:
                break
        if reached<high-1e-12:
            return False
        admitted.append((high-low)*math.dist(first,last))
        for fraction in (low,(low+high)/2.,high):
            sampled.append(min(_point_triangle_distance(at(fraction),f['points'])for f in near))
    if precision_report is not None:
        precision_report['admitted_spans']+=len(gaps)
        precision_report['admitted_endpoint_spans']+=sum(low==0. or high==1. for low,high in gaps)
        precision_report['maximum_admitted_along_path_span_m']=max(precision_report['maximum_admitted_along_path_span_m'],max(admitted))
        precision_report['distance_samples_checked']+=len(sampled)
        precision_report['maximum_sampled_distance_m']=max(precision_report['maximum_sampled_distance_m'],max(sampled))
    return True


def _clip(polygon, axis, bound, sign):
    if not polygon:
        return []
    output, previous = [], polygon[-1]
    last = sign*(previous[axis]-bound)
    for point in polygon:
        current = sign*(point[axis]-bound)
        if (last >= 0.0) != (current >= 0.0):
            fraction = last/(last-current)
            output.append(tuple(a+fraction*(b-a) for a,b in zip(previous,point)))
        if current >= 0.0:
            output.append(point)
        previous,last = point,current
    return output


def _intrudes(first,last,triangle,half_width,height):
    """Intersect one actual triangle with the interior of a graded corridor."""
    dx,dy = last[0]-first[0],last[1]-first[1]
    length = math.hypot(dx,dy)
    polygon = []
    for point in triangle:
        east,north = point[0]-first[0],point[1]-first[1]
        along = (east*dx+north*dy)/(length*length)
        lateral = (dx*north-dy*east)/length
        above = point[2]-first[2]-along*(last[2]-first[2])
        polygon.append((along,lateral,above))
    for axis,bound,sign in ((0,1e-8,1),(0,1.0-1e-8,-1),
                            (1,-half_width+1e-5,1),(1,half_width-1e-5,-1),
                            (2,MARKING_TOLERANCE,1),(2,height-1e-5,-1)):
        polygon = _clip(polygon,axis,bound,sign)
        if not polygon:
            return False
    return True


def _endpoints(routes):
    output = []
    for cell,records in routes.items():
        for index,route in enumerate(records):
            for direction,point,other,side in (('in',route['points'][0],route['points'][1],route['entry']),
                                               ('out',route['points'][-1],route['points'][-2],route['exit'])):
                tangent = ((other[0]-point[0],other[1]-point[1],other[2]-point[2]) if direction == 'in'
                           else (point[0]-other[0],point[1]-other[1],point[2]-other[2]))
                length = math.hypot(*tangent[:2])
                output.append({'cell':cell, 'route':index, 'direction':direction, 'side':side,
                               'transport':route['transport'], 'point_m':point,
                               'tangent':tuple(value/length for value in tangent[:2]), 'grade':tangent[2]/length})
    return output


def _continuity(routes,ports):
    endpoints = _endpoints(routes)
    opened,matched = [],0
    for endpoint in endpoints:
        dx,dy = _NEIGHBOURS[endpoint['side']]
        neighbor = endpoint['cell'][0]+dx,endpoint['cell'][1]+dy
        candidates = [other for other in endpoints
                      if other['transport'] == endpoint['transport']
                      and other['direction'] != endpoint['direction']
                      and other['side'] == (endpoint['side']+2)%4
                      and other['cell'] == neighbor
                      and math.dist(other['point_m'],endpoint['point_m']) <= POSITION_TOLERANCE]
        if candidates:
            _need(any(sum(a*b for a,b in zip(other['tangent'],endpoint['tangent'])) >= 0.9998
                      and abs(other['grade']-endpoint['grade']) <= 0.005 for other in candidates),
                  'Saved highway tile seam has discontinuous travel tangent or grade')
            matched += 1
        else:
            opened.append(endpoint)
    # Several directed movements can share one physical entrance or exit.
    # Compare the measured boundary once, retaining its actual route count.
    distinct = []
    for endpoint in opened:
        existing = next((other for other in distinct
                         if other['transport'] == endpoint['transport']
                         and other['direction'] == endpoint['direction']
                         and other['side'] == endpoint['side']
                         and math.dist(other['point_m'],endpoint['point_m']) <= POSITION_TOLERANCE
                         and sum(a*b for a,b in zip(other['tangent'],endpoint['tangent'])) >= 0.9998
                         and abs(other['grade']-endpoint['grade']) <= 0.005),None)
        if existing is None:
            distinct.append({**endpoint,'path_ends':1})
        else:
            existing['path_ends'] += 1
    opened = distinct
    if ports is not None:
        remaining = list(ports)
        for endpoint in opened:
            matches = [port for port in remaining if port.get('transport',1) == endpoint['transport']
                       and port.get('direction') == endpoint['direction']
                       and math.dist(port['point_m'],endpoint['point_m']) <= POSITION_TOLERANCE]
            _need(matches, 'Saved highway open endpoint differs from the measured external port contract')
            port = matches[0]
            if 'tangent' in port:
                length = math.hypot(*port['tangent'])
                _need(length > 0.0 and sum(a*b/length for a,b in zip(port['tangent'],endpoint['tangent'])) >= 0.9998,
                      'Saved highway endpoint travel tangent differs from the measured native port')
            if 'grade' in port:
                _need(abs(port['grade']-endpoint['grade']) <= 0.005,
                      'Saved highway endpoint grade differs from the measured native port')
            remaining.remove(port)
        _need(not remaining, 'A measured highway external port is absent from saved PATHs')
    else:
        for endpoint in opened:
            dx,dy = _NEIGHBOURS[endpoint['side']]
            neighbor = endpoint['cell'][0]+dx,endpoint['cell'][1]+dy
            _need(neighbor not in routes or not routes[neighbor],
                  'Unjoined saved highway PATH endpoint inside the owned tile grid')
    return opened,matched//2


def check_pavement(resources,piece,*,ports=None,empty_path_cells=None,rotations=(0,1,2,3),native_overhangs=()):
    """Check actual saved road resources with an explicit engineering contract.

    ``ports`` contains independently measured world points, directed tangents,
    and optional grades. Omitting it verifies internal seams and reports open
    endpoints without claiming native external compatibility. Empty PATH cells
    require exact declaration through ``engineering.model_only_cells`` or the
    supplied ``empty_path_cells`` contract. Rotations are proper clockwise
    quarter turns of the actual decoded geometry and traffic, never mirrors.
    """
    engineering = piece.get('engineering',{})
    if not native_overhangs:
        from .native_overhangs import NATIVE_OVERHANG_TRIANGLES
        native_overhangs = NATIVE_OVERHANG_TRIANGLES
    maximum = _grade_bound(piece)
    _need(engineering.get('pavement_path_offset_m') == 0.0, 'Highway pavement/PATH datum offset must be exactly zero')
    half_width = engineering.get('car_corridor_half_width_m')
    corridor_height = engineering.get('car_corridor_height_m')
    _need(all(type(value) in (int,float) and math.isfinite(value) and value > 0.0
              for value in (half_width,corridor_height)), 'Declare a finite positive highway car corridor')
    _need(rotations and len(rotations) == len(set(rotations)) and set(rotations) <= {0,1,2,3},
          'Highway rotations must be unique proper quarter turns')
    cells = [tuple(cell) for cell in piece['cells']]
    _need(len(cells) == len(set(cells)) == len(piece['tile_ids']), 'Highway saved-resource cell contract differs from tile IDs')
    empty = {tuple(cell) for cell in (engineering.get('model_only_cells',[]) if empty_path_cells is None else empty_path_cells)}
    _need(empty <= set(cells), 'Declared model-only highway cells are outside the piece')
    routes,faces = {},{}
    from .wheeltrack_verify import _BRANCH_ORIGINS, check_piece_overhangs
    for cell,identifier in zip(cells,piece['tile_ids']):
        iid = int(identifier,16)
        _need((*S3D,iid) in resources and (*PATH,iid) in resources, 'Missing saved highway S3D or PATH resource')
        for zoom in range(1,5):
            if (*S3D,iid+zoom) in resources:
                _need(decompress(resources[*S3D,iid+zoom]) == decompress(resources[*S3D,iid]),
                      'Saved highway zoom model differs from its independently checked base model')
        faces[cell] = _triangles(resources[*S3D,iid],cell,native_overhangs,
                                 pending_native_uv=piece.get('geometry_key') in _BRANCH_ORIGINS)
        local = _paths(resources[*PATH,iid])
        _need(bool(local) == (cell not in empty), 'Empty highway PATH differs from the declared model-only cell contract')
        routes[cell] = [{**route,'points':[(p[0]+16*cell[0],p[1]-16*cell[1],p[2]) for p in route['points']]}
                        for route in local]
    triangles=[face for group in faces.values() for face in group]
    atlas = _atlas(resources,piece,engineering,triangles)
    atlas['native_overhang_uv_field']=check_piece_overhangs(triangles,piece,routes,atlas.get('neutral_field_controls'))
    support_encoding={'geometry_key':piece.get('geometry_key'),'field_controls':atlas.get('neutral_field_controls')}
    precision_report={'euclidean_distance_limit_m':SUPPORT_ENCODING_DISTANCE_M,'admitted_spans':0,
                      'admitted_endpoint_spans':0,'maximum_admitted_along_path_span_m':0.,
                      'distance_samples_checked':0,'maximum_sampled_distance_m':0.,
                      'enabled_for_piece':piece.get('geometry_key') in _BRANCH_ORIGINS
                          and atlas.get('neutral_field_controls',{}).get('passed') is True,
                      'capsule_union_fraction_guard':1e-12,
                      'scope':'Only strict uncovered spans on affirmative flat served-deck branches receive a separate distance-to-pinned-DD-footprints proof using finite edge rectangles plus endpoint discs. The two-micrometre Euclidean bound is proved by interval union; reported endpoint/midpoint distances are samples, and along-PATH span lengths are disclosed separately. Barycentric and height checks remain unchanged.'}
    if ports is None:
        ports = engineering.get('external_ports')
    opened,seams = _continuity(routes,ports)
    maximum_actual,car_count,segments = 0.0,0,0
    for records in routes.values():
        for route in records:
            if route['transport'] != 1:
                continue
            car_count += 1
            for first,last in zip(route['points'],route['points'][1:]):
                grade = 100.0*abs(last[2]-first[2])/math.dist(first[:2],last[:2])
                maximum_actual = max(maximum_actual,grade)
                _need(grade <= maximum+1e-5, 'Saved highway PATH exceeds its declared maximum grade')
                segments += 1
    _need(car_count > 0, 'Highway pavement verification needs at least one actual saved car route')
    counts = []
    radius = max(1,math.ceil(half_width/16.0))
    for quarter in rotations:
        rotated_routes = {_rotate_cell(cell,quarter):[
            {**route,'points':[_rotate(point,quarter) for point in route['points']],
             'entry':(route['entry']+quarter)%4,'exit':(route['exit']+quarter)%4} for route in records]
            for cell,records in routes.items()}
        rotated_ports = None if ports is None else [
            {**port,'point_m':_rotate(port['point_m'],quarter),
             **({'tangent':_rotate((*port['tangent'],0.0),quarter)[:2]} if 'tangent' in port else {})}
            for port in ports]
        _continuity(rotated_routes,rotated_ports)
        rotated_faces = {_rotate_cell(cell,quarter):[
            {**face,'points':tuple(_rotate(point,quarter) for point in face['points'])} for face in group]
            for cell,group in faces.items()}
        checked = 0
        for cell,records in routes.items():
            rotated_cell = _rotate_cell(cell,quarter)
            nearby = [face for dx in range(-radius,radius+1) for dy in range(-radius,radius+1)
                      for face in rotated_faces.get((rotated_cell[0]+dx,rotated_cell[1]+dy),[])]
            for route_index,route in enumerate(records):
                if route['transport'] != 1:
                    continue
                points = [_rotate(point,quarter) for point in route['points']]
                for first,last in zip(points,points[1:]):
                    # A rectangle broad phase preserves all candidate faces;
                    # the exact clipping tests below make the final decision.
                    low = min(first[0],last[0])-half_width,min(first[1],last[1])-half_width
                    high = max(first[0],last[0])+half_width,max(first[1],last[1])+half_width
                    candidates = [face for face in nearby if all(
                        max(point[axis] for point in face['points']) >= low[axis]-POSITION_TOLERANCE
                        and min(point[axis] for point in face['points']) <= high[axis]+POSITION_TOLERANCE for axis in (0,1))]
                    _need(_covered(first,last,candidates,encoding=support_encoding,precision_report=precision_report),
                          f'Saved highway pavement does not continuously support an encoded car PATH segment at zero datum offset; cell={cell}, route={route_index}, rotation={quarter}, points={first}->{last}')
                    for face in candidates:
                        _need(not _intrudes(first,last,face['points'],half_width,corridor_height),
                              f'Saved highway solid triangle intrudes into the declared car corridor; cell={cell}, route={route_index}, rotation={quarter}, points={first}->{last}, triangle={face["points"]}')
                    checked += 1
        counts.append({'quarter_turns_clockwise':quarter,'car_segments_checked':checked})
    return {'passed':True,'car_paths':car_count,'car_segments':segments,'maximum_grade_percent':maximum_actual,
            'grade_bound_percent':maximum,'pavement_path_offset_m':0.0,'continuous_segment_support':True,
            'support_encoding_precision':precision_report,
            'car_corridor_half_width_m':half_width,'car_corridor_height_m':corridor_height,
            'marking_tolerance_m':MARKING_TOLERANCE,'atlas':atlas,'internal_seams':seams,
            'native_external_ports_checked':ports is not None,
            'open_endpoints':[{key:value for key,value in endpoint.items() if key not in {'route'}} for endpoint in opened],
            'model_only_cells':[list(cell) for cell in sorted(empty)],'rotations':counts,
            'audited_native_overhang_signatures_available':len(native_overhangs),
            'coverage_limit':'Actual indexed face intersections and car PATH spine support, with only the explicitly reported two-micrometre encoding allowance on affirmative flat served-deck DD branches; no closed-solid containment, complete vehicle swept-body safety, native placement, or in-game observation is established.'}


def check_paths(resources,piece):
    """Provider entry point for actual road metadata, grades, and tile seams."""
    engineering = piece.get('engineering',{})
    bound = _grade_bound(piece)
    empty = {tuple(cell) for cell in engineering.get('model_only_cells',[])}
    routes,maximum = {},0.0
    for cell,identifier in zip(map(tuple,piece['cells']),piece['tile_ids']):
        parsed = _paths(resources[*PATH,int(identifier,16)])
        _need(bool(parsed) == (cell not in empty),'Empty highway PATH differs from declared model-only cells')
        routes[cell] = []
        for route in parsed:
            world = [(p[0]+16*cell[0],p[1]-16*cell[1],p[2]) for p in route['points']]
            routes[cell].append({**route,'points':world})
            if route['transport'] == 1:
                for first,last in zip(world,world[1:]):
                    grade = 100.0*abs(last[2]-first[2])/math.dist(first[:2],last[:2])
                    maximum = max(maximum,grade)
                    _need(grade <= bound+1e-5,'Saved highway PATH exceeds its declared maximum grade')
    opened,seams = _continuity(routes,engineering.get('external_ports'))
    return {'actual_road_transport_flags_checked':True,'maximum_grade_percent':maximum,
            'internal_route_seams_checked':seams,'open_directional_ports':len(opened),
            'native_external_contract_checked':engineering.get('external_ports') is not None,
            'model_only_cells_checked':len(empty),'game_operation_tested':False}


_MODEL_AUDIT_CACHE = OrderedDict()
_MODEL_AUDIT_CACHE_LIMIT = 32
_MODEL_AUDIT_MODULES = (
    'scp_highway.ramp_verify', 'scp_highway.native_overhangs',
    'scp_highway.wheeltrack_verify', 'scp_highway.shoulder_uv_verify',
    'scp.dbpf', 'scp.models', 'scp.track_paths', 'scp.verify',
)


def _model_audit_context():
    """Pin loaded validator identities, source bytes, and live audit constants.

    These modules own the complete check_models call graph and its frozen
    native-overhang evidence. This process-local cache never survives an
    import/process restart. Source/constant changes and replaced validators
    invalidate it, including test patches. No donor argument is read by this
    audit: the independently pinned native contract lives in these modules.
    """
    result = []
    for name in _MODEL_AUDIT_MODULES:
        module = importlib.import_module(name)
        constants = [(key,value) for key,value in vars(module).items()
                     if key.isupper() and not key.startswith('_MODEL_AUDIT_')]
        functions = tuple((key,id(value)) for key,value in sorted(vars(module).items())
                          if callable(value))
        result.append((name,hashlib.sha256(Path(module.__file__).read_bytes()).digest(),
                       hashlib.sha256(repr(sorted(constants)).encode()).digest(),functions))
    return tuple(result)


def check_models(resources,piece,donors=None):
    """Audit exact immutable inputs; reuse successful reports only in memory.

    Hash every supplied resource, including unreferenced exemplars, textures,
    PATHs, zooms, and previews. Cache only small reports, never native/model
    byte buffers. Snapshots prevent caller mutation from changing an audit's
    specification or resource bytes, and every caller receives a fresh report.
    Direct check_pavement calls always execute their complete checks.
    """
    specification = json.dumps(piece,sort_keys=True,separators=(',',':'),allow_nan=False)
    immutable = {key:bytes(raw) for key,raw in resources.items()}
    context = _model_audit_context()
    key = (specification,tuple((identifier,len(raw),hashlib.sha256(raw).digest())
                              for identifier,raw in sorted(immutable.items())),context)
    if key in _MODEL_AUDIT_CACHE:
        _MODEL_AUDIT_CACHE.move_to_end(key)
        return deepcopy(_MODEL_AUDIT_CACHE[key])
    report = _check_models_uncached(immutable,json.loads(specification))
    if report.get('passed') is True and _model_audit_context() == context:
        _MODEL_AUDIT_CACHE[key] = deepcopy(report)
        while len(_MODEL_AUDIT_CACHE) > _MODEL_AUDIT_CACHE_LIMIT:
            _MODEL_AUDIT_CACHE.popitem(last=False)
    return deepcopy(report)


def _check_models_uncached(resources,piece):
    """Execute the unchanged full saved-resource and preview audit."""
    from scp.verify import mesh_data,translated
    report = check_pavement(resources,piece)
    textures,expected = set(),[]
    checked = 0
    for cell,identifier in zip(piece['cells'],piece['tile_ids']):
        iid = int(identifier,16)
        for zoom in range(5):
            _need((*S3D,iid+zoom) in resources,'Missing saved highway zoom model')
            model = parse_s3d(resources[*S3D,iid+zoom])
            validate_s3d(model)
            textures.update(texture for material in model['materials'] for texture in material['textures'])
            checked += 1
            if zoom == 0:
                expected.extend((mesh_data(model,mesh),(16.0*cell[0],0.0,16.0*cell[1])) for mesh in model['meshes'])
    preview = parse_s3d(resources[*S3D,int(piece['preview_id'],16)])
    validate_s3d(preview)
    textures.update(texture for material in preview['materials'] for texture in material['textures'])
    _need(len(preview['meshes']) == len(expected),'Saved highway preview omits or adds source-cell meshes')
    for mesh,(source,delta) in zip(preview['meshes'],expected):
        _need(translated(mesh_data(preview,mesh),source,delta),
              'Saved highway preview differs from its actual translated source-cell meshes, UVs, indices, or materials')
    return {**report,'texture_ids':sorted(textures),'preview_matches_all_cells':True,
            'model_resources_checked':checked+1,'game_rendering_tested':False}


# Independent retained construction-grid origins for the reviewed thirteen
# reusable module cuts. These are source-layout contracts, not builder output.
_ORIGINS = {'access-core':(-1,-1),'northwest-junction':(-2,-2),'southeast-junction':(1,1),
            'lower-exit-branch':(2,-2),'lower-entry-branch':(-2,2),'lower-exit-grade':(1,-2),
            'lower-entry-grade':(-2,1),'upper-exit-branch':(-3,3),'upper-entry-branch':(3,-3),
            'upper-exit-grade':(-1,2),'upper-entry-grade':(2,-1),
            'diagonal-half-a':(-1,1),'diagonal-half-b':(-1,2)}


def _road_word(routes):
    values = [0,0,0,0]
    for route in routes:
        for side,first,last in ((route['entry'],*route['points'][:2]),
                                (route['exit'],*route['points'][-2:])):
            dx,dy = last[0]-first[0],last[1]-first[1]
            if abs(dx) < 1e-7 or abs(dy) < 1e-7:
                flag = 2
            elif side in (0,2):
                flag = 1 if dx*dy > 0.0 else 3
            else:
                flag = 3 if dx*dy > 0.0 else 1
            values[side] = 2 if flag == 2 or values[side] == 2 else flag
    return sum(value << (8*side) for side,value in enumerate(values))


def check_construction_fields(fields,piece,resources):
    """Check saved ownership and road flags without calling their generator."""
    key = piece.get('geometry_key')
    _need(key in _ORIGINS,'Unknown independently reviewed compact module construction origin')
    origin = _ORIGINS[key]
    width,depth = piece['footprint']
    rows,cons = fields.get('CellLayout',[]),fields.get('ConsLayout',[])
    _need(len(rows) == len(cons) == depth+1 and all(len(row) == width+2 for row in rows+cons),
          'Saved compact highway construction dimensions differ from the piece footprint')
    expected = [['.']*(width+2) for _ in range(depth+1)]
    expected[0][-1],expected[-1][0] = '<','^'
    expected_cons = [list(row) for row in expected]
    checks = fields.get('CheckType',[])
    _need(len(checks) == len(piece['cells']),'Compact highway construction palette differs from owned cells')
    for index,(cell,identifier) in enumerate(zip(piece['cells'],piece['tile_ids'])):
        symbol = chr(ord('a')+index)
        expected[cell[1]][cell[0]] = symbol
        match = re.fullmatch(re.escape(symbol)+r' - (.+)',checks[index])
        _need(match is not None,'Compact highway construction symbol is missing or reordered')
        words = re.findall(r'(dirtroad|avenue): 0x([0-9a-fA-F]{8})',match.group(1))
        _need(' '.join(name+': 0x'+word for name,word in words) == match.group(1)
              and len(words) == len({name for name,_word in words}),'Invalid compact highway network flags')
        saved = {name:int(word,16) for name,word in words}
        routes = _paths(resources[*PATH,int(identifier,16)])
        world = cell[0]+origin[0],cell[1]+origin[1]
        avenue = world[0]-world[1] in (-1,0,1)
        highway = sum(world) in (0,1)
        road = [route for route in routes if route['points'][0][2] != 0.0 or route['points'][-1][2] != 0.0]
        road += [route for route in routes if route['transport'] == 1 and route['junction']]
        if not highway and not road and not avenue:
            road = routes
        required = {}
        if highway or road or not avenue:
            required['dirtroad'] = _road_word(road)
        if avenue:
            required['avenue'] = {0:0x01030103,1:0x01000003,-1:0x00030100}[world[0]-world[1]]
        _need(saved == required,'Saved highway or measured Avenue construction flags differ from actual road approaches')
        expected_cons[cell[1]][cell[0]] = '+' if 'dirtroad' in required else '\\'
    _need(rows == [''.join(row) for row in expected] and cons == [''.join(row) for row in expected_cons],
          'Compact highway construction cells, network ownership, or anchors changed')
    _need(fields.get('Costs') == ['1000'],'Unexpected compact highway construction cost')
    return {'occupied_cells_checked':len(piece['cells']),'actual_saved_route_flags_checked':True,
            'native_avenue_flags_checked':True,'independent_module_origin_checked':True}
