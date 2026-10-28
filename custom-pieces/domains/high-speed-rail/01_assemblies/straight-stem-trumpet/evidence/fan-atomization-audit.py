"""Replay the compact-fan atomization measurements from portable saved inputs.

This is a read-only evidence audit, not an assembly builder, source parser,
compatibility selector, or integration-ledger writer. With --record only it
replays continuous cap coverage using the exact saved XYZUV triangles embedded
in the record. With both build arguments it also reads the pinned actual DATs,
compares both full straight surfaces, materials, supports, texture phases,
retained core collar, and full solid across all native height transitions.

Run from the repository root:
  python3 -B custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/evidence/fan-atomization-audit.py
  python3 -B custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/evidence/fan-atomization-audit.py --parent-build custom-pieces/dist/fan-central-parapet-follow-ballast --neighbour-build custom-pieces/dist/straight-stem-trumpet

The second form requires those exact historical saved builds. A different
verified build of the unchanged native neighbour is accepted only if its actual
DAT and selected model hashes match the embedded pins. No private game paths
are assumed. Both modes print their precise scope; record-only replay is not
reported as a fresh full-DAT verification.
"""
from pathlib import Path
import argparse
from collections import Counter
import hashlib
import json
import math
import struct
import sys

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/high-speed-rail/implementation')]
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
import numpy as np
from scp.models import parse_s3d
from scp.render_meshes import _triangles as raw_triangles
from scp_hsr.assembly_inspection import load_build, S3D, number
from scp_hsr.rail_feature_verify import _triangles
from scp_hsr.directional_t_verify import _area, _intersection_polygon
from scp_hsr.hsr_mesh_verify import _component_union_area
from scp_hsr.hsr_compact_fan_verify import _clip_attribute_polygon
from scp_hsr.hsr_trumpet_verify import rotate

TOL = .00002
sha = lambda raw: hashlib.sha256(raw).hexdigest()

def cap(triangle):
    return (max(p[2] for p in triangle) - min(p[2] for p in triangle) < 1e-5
            and abs(abs(triangle[0][2]) - 8.) < 1e-5)

def records(model):
    result = []
    for mesh in model['meshes']:
        frame = mesh['frames'][0]
        material = model['materials'][frame[3]]['raw']
        for triangle in raw_triangles(model, frame):
            result.append((material, tuple(tuple(struct.unpack('<5f', v)) for v in triangle),
                           mesh['name'].decode().rstrip('\0')))
    return result

def support_inventory(model):
    result = Counter()
    for material, triangle, mesh in records(model):
        if 'support' not in mesh:
            continue
        vertices = [struct.pack('<5f', *p) for p in triangle]
        canonical = min(tuple(vertices), tuple(vertices[1:] + vertices[:1]),
                        tuple(vertices[2:] + vertices[:2]))
        result[sha(material + b''.join(canonical))] += 1
    return result

ARRAYS={}

def crossings(triangles,height,south):
 key=id(triangles)
 if key not in ARRAYS:
  t=np.array([[p[:3] for p in tri] for tri in triangles]);a=t[:,0,:];ab=t[:,1,:]-a;ac=t[:,2,:]-a;nx=np.cross(ab,ac)[:,0];mask=np.abs(nx)>1e-10;ARRAYS[key]=(a[mask],ab[mask],ac[mask],nx[mask])
 a,ab,ac,nx=ARRAYS[key];u=((height-a[:,1])*ac[:,2]-(south-a[:,2])*ac[:,1])/nx;v=(ab[:,1]*(south-a[:,2])-ab[:,2]*(height-a[:,1]))/nx;valid=(u>=-1e-10)&(v>=-1e-10)&(u+v<=1+1e-10);xs=a[:,0]+u*ab[:,0]+v*ac[:,0];out=[]
 for x,normal in zip(xs[valid],nx[valid]):
  x=float(x);sign=1 if normal>0 else -1
  if not any(abs(x-p[0])<1e-7 and sign==p[1] for p in out):out.append((x,sign))
 return sorted(out)

def solid_intervals(triangles,height,south):
 cs=crossings(triangles,height,south);level=0;out=[]
 for i,(x,sign) in enumerate(cs):
  level-=sign
  if i+1<len(cs) and level!=0:out.append((x,cs[i+1][0],level))
 merged=[]
 for a,b,count in out:
  if b-a<1e-7:continue
  if merged and abs(merged[-1][1]-a)<1e-6:merged[-1][1]=b
  else:merged.append([a,b])
 return {'intervals_m':merged,'final_oriented_winding':level,'crossings':cs}


def coverage(source,target):
 target=np.array([[p[:3] for p in t] for t in target]);uncovered=0.;maximum=0.;checked=0;cache={};failures=[]
 for triangle in source:
  p=np.array([p[:3] for p in triangle]);n=np.cross(p[1]-p[0],p[2]-p[0]);length=np.linalg.norm(n)
  if length<1e-10:continue
  n=n/length
  if n[np.argmax(np.abs(n))]<0:n=-n
  offset=float(n@p[0]);key=tuple(round(float(x),8) for x in [*n,offset])
  if key not in cache:
   mask=np.max(np.abs(target@n-offset),axis=1)<=TOL
   targets=target[mask]
   axis=np.eye(3)[int(np.argmin(np.abs(n)))];u=np.cross(n,axis);u=u/np.linalg.norm(u);v=np.cross(n,u)
   polygons=[]
   for q in targets:
    poly=[tuple(v) for v in np.column_stack((q@u,q@v))]
    if _area(poly)<1e-12:continue
    if sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(poly,poly[1:]+poly[:1]))<0:poly.reverse()
    lines=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
     edge=np.array(b)-a;inside=np.array([-edge[1],edge[0]])/np.linalg.norm(edge);lines.append((inside,float(inside@a)-TOL))
    expanded=[]
    for i in range(3):
     first,second=lines[i-1],lines[i];expanded.append(tuple(np.linalg.solve(np.array([first[0],second[0]]),np.array([first[1],second[1]]))))
    polygons.append(expanded)
   cache[key]=(u,v,polygons)
  u,v,polygons=cache[key];polygon=[tuple(x) for x in np.column_stack((p@u,p@v))]
  overlaps=[_intersection_polygon(list(polygon),clip) for clip in polygons];overlaps=[q for q in overlaps if len(q)>=3 and _area(q)>1e-12];missing=max(0.,_area(polygon)-_component_union_area(overlaps))
  uncovered+=missing;maximum=max(maximum,missing);checked+=1
  if missing>1e-6 and len(failures)<12:failures.append({'triangle_xyz':p.tolist(),'normal':n.tolist(),'plane_offset':offset,'area':float(_area(polygon)),'missing':float(missing),'target_triangles_near_plane':len(polygons)})
 return {'saved_triangles_checked':checked,'uncovered_surface_area_m2':uncovered,'maximum_uncovered_triangle_area_m2':maximum,'planar_matching_tolerance_m':TOL,'in_plane_coverage_tolerance_m':TOL,'conservative_3d_distance_bound_m':math.sqrt(2)*TOL,'all_faces_covered':bool(maximum<1e-10),'first_uncovered_faces':failures}

def uv_audit(source,target):
 # Sample every actual face at vertices, centroid, and three edge midpoints.
 # Match the original material and oriented surface, then compare UV modulo
 # whole texture repeats. The continuous XYZ proof is performed separately.
 targ=np.array([[p[:3] for p in t] for _,t,_ in target]);uvs=np.array([[p[3:] for p in t] for _,t,_ in target]);a=targ[:,0];ab=targ[:,1]-a;ac=targ[:,2]-a;n=np.cross(ab,ac);length=np.linalg.norm(n,axis=1);unit=n/np.maximum(length[:,None],1e-30);matkeys=[sha(m) for m,_,_ in target]
 maxu=maxv=0.;counts=Counter();failures=[];checked=0;missing=0;shifts=Counter();badfaces=[];maxu_nonsliver=maxv_nonsliver=0.
 weights=np.array([[1,0,0],[0,1,0],[0,0,1],[1/3]*3,[.5,.5,0],[0,.5,.5],[.5,0,.5]])
 for mat,t,mesh in source:
  if cap(t):continue
  p=np.array([v[:3] for v in t]);sourceuv=np.array([v[3:] for v in t]);sn=np.cross(p[1]-p[0],p[2]-p[0]);slen=np.linalg.norm(sn)
  if slen<1e-10:continue
  trierror=0.;sn/=slen;mask=(unit@sn>.99999)&np.array([sha(mat)==k for k in matkeys]);inds=np.flatnonzero(mask)
  for w in weights:
   point=w@p;uv=w@sourceuv;valid=[]
   for i in inds:
    if abs(unit[i]@(point-a[i]))>2e-5:continue
    d=point-a[i];v0=ab[i];v1=ac[i];d00=v0@v0;d01=v0@v1;d11=v1@v1;d20=d@v0;d21=d@v1;den=d00*d11-d01*d01
    if abs(den)<1e-18:continue
    u=(d11*d20-d01*d21)/den;v=(d00*d21-d01*d20)/den
    # Permit only the same20micrometre positional tolerance at tile cuts.
    btol=2e-5/max(min(np.linalg.norm(v0),np.linalg.norm(v1)),1e-5)
    if u< -btol or v< -btol or u+v>1+btol:continue
    uv2=(1-u-v)*uvs[i,0]+u*uvs[i,1]+v*uvs[i,2];delta=uv-uv2;wrapped=delta-np.rint(delta);valid.append((float(np.linalg.norm(wrapped)),float(abs(wrapped[0])),float(abs(wrapped[1])),tuple(int(round(x)) for x in delta)))
   checked+=1
   if not valid:
    missing+=1
    if len(failures)<8:failures.append({'xyz':point.tolist(),'uv':uv.tolist(),'mesh':mesh,'reason':'no same-oriented material face'})
    continue
   best=min(valid);maxu=max(maxu,best[1]);maxv=max(maxv,best[2]);trierror=max(trierror,best[1],best[2]);shifts[str(best[3])]+=1
   if slen/2>1e-5:maxu_nonsliver=max(maxu_nonsliver,best[1]);maxv_nonsliver=max(maxv_nonsliver,best[2])
   if max(best[1:3])>1e-4 and len(failures)<8:failures.append({'xyz':point.tolist(),'uv':uv.tolist(),'mesh':mesh,'reason':'UV differs','wrapped_difference':best[1:3]})
  if trierror>1e-4:badfaces.append({'area_m2':float(slen/2),'xyzuv':t,'maximum_uv_error':trierror})
 return {'mismatching_faces':badfaces,'mismatching_face_count':len(badfaces),'sum_mismatching_face_areas_m2':sum(x['area_m2'] for x in badfaces),'largest_mismatching_face_area_m2':max((x['area_m2'] for x in badfaces),default=0.),'maximum_wrapped_u_error_excluding_faces_below_0_00001_m2':maxu_nonsliver,'maximum_wrapped_v_error_excluding_faces_below_0_00001_m2':maxv_nonsliver,'sample_points':checked,'unmatched_samples':missing,'maximum_wrapped_u_error':maxu,'maximum_wrapped_v_error':maxv,'whole_repeat_shifts':dict(shifts),'first_failures':failures}


def clip_patch(triangles, low, high):
    result = []
    for triangle in triangles:
        polygon = _clip_attribute_polygon(list(triangle), lambda p: p[2] - low, True)
        if polygon:
            polygon = _clip_attribute_polygon(polygon, lambda p: high - p[2], True)
        for a, b in zip(polygon[1:], polygon[2:]):
            triangle = (polygon[0], a, b)
            area2 = np.linalg.norm(np.cross(np.array(a[:3]) - polygon[0][:3],
                                           np.array(b[:3]) - polygon[0][:3]))
            if area2 > 1e-10:
                result.append(triangle)
    return result

def outer_solid_summary(first, second, south_pairs):
    heights = sorted({p[1] for triangles in (first, second) for t in triangles for p in t})
    levels = sorted({h + delta for h in heights for delta in (-.0001, 0., .0001)
                     if h + delta >= 0.} | {(a + b) / 2 for a, b in zip(heights, heights[1:])
                                           if b - a > .00004})
    all_count = robust_count = mismatches = 0
    maximum = 0.
    witness = None
    for first_south, second_south in south_pairs:
        for height in levels:
            all_count += 1
            x = solid_intervals(first, height, first_south)
            y = solid_intervals(second, height, second_south)
            if (min(abs(height - h) for h in heights) <= .00002
                    or x['final_oriented_winding'] or y['final_oriented_winding']):
                continue
            robust_count += 1
            if len(x['intervals_m']) != len(y['intervals_m']):
                mismatches += 1
                continue
            difference = max((abs(a - b) for xx, yy in zip(x['intervals_m'], y['intervals_m'])
                              for a, b in zip(xx, yy)), default=0.)
            if difference > maximum:
                maximum = difference
                witness = {'height_m': height, 'first': x, 'second': y,
                           'first_south_m': first_south, 'second_south_m': second_south}
    return {'all_sections': all_count, 'robust_closed_sections': robust_count,
            'robust_interval_count_mismatches': mismatches,
            'maximum_robust_edge_difference_m': maximum, 'worst_section': witness}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path, default=Path(__file__).with_name('fan-atomization-review.json'))
    parser.add_argument('--parent-build', type=Path)
    parser.add_argument('--neighbour-build', type=Path)
    args = parser.parse_args()
    if bool(args.parent_build) != bool(args.neighbour_build):
        parser.error('Supply both saved-build directories, or neither for embedded cap replay only.')
    record = json.loads(args.record.read_text())
    closure = record['existing_external_north_join']
    caps = closure['old_caps_xyzuv']
    native_faces = closure['native_covering_faces_xyzuv_in_original_fan_local_coordinates']
    result = {'scope': 'Embedded saved-face cap-coverage replay only; actual DATs not loaded.',
              'record_sha256': sha(args.record.read_bytes()),
              'embedded_cap_coverage': coverage(caps, native_faces)}
    assert len(caps) == 14 and len(native_faces) == 10
    assert result['embedded_cap_coverage']['all_faces_covered']
    if args.parent_build:
        parent = load_build(args.parent_build)
        piece = parent['pieces'][record['decision']['retained_full_fan_id']]
        saved = parent['resources'](piece)
        assert saved['sha256'] == record['saved_input']['full_fan_dat_sha256']
        models = []
        triangles = []
        for cell in ([3, 0], [3, 1], [3, 2]):
            iid = number(piece['tile_ids'][piece['cells'].index(cell)])
            raw = saved['resources'][*S3D, iid]
            expected = next(item for item in record['saved_input']['candidate_tiles']
                            if item['source_cell'] == cell)
            assert sha(raw) == expected['model_sha256']
            model = parse_s3d(raw)
            models.append(model)
            triangles.append(list(_triangles(model)))
        zero, one, core = triangles
        north_build = load_build(args.neighbour_build)
        north_piece = north_build['pieces'][closure['neighbour_piece_id']]
        north_saved = north_build['resources'](north_piece)
        assert north_saved['sha256'] == closure['neighbour_dat_sha256']
        ni = number(north_piece['tile_ids'][north_piece['cells'].index([3, 0])])
        native_raw = north_saved['resources'][*S3D, ni]
        assert sha(native_raw) == closure['neighbour_model_sha256']
        native = []
        for triangle in _triangles(parse_s3d(native_raw)):
            converted = []
            for x, height, south, u, v in triangle:
                east, north, _ = rotate((x, -south, 0.), 3)
                converted.append((east, height, -north, u, v))
            native.append(tuple(converted))
        actual_native_faces = []
        for triangle in native:
            a, b, c = np.array([p[:3] for p in triangle])
            normal = np.cross(b - a, c - a)
            length = np.linalg.norm(normal)
            if (length > 1e-10 and normal[2] / length > .999999
                    and all(abs(p[2] - 8.) < 1e-7 for p in triangle)):
                actual_native_faces.append(tuple((x, h, z - 16., u, v) for x, h, z, u, v in triangle))
        actual_caps = [t for t in zero if cap(t)]
        assert actual_caps == [tuple(tuple(p) for p in t) for t in caps]
        assert actual_native_faces == [tuple(tuple(p) for p in t) for t in native_faces]
        result.update(scope='Actual pinned parent and native-neighbour DAT verification.',
                      parent_dat_sha256=saved['sha256'], neighbour_dat_sha256=north_saved['sha256'],
                      actual_cap_coverage=coverage(actual_caps, actual_native_faces),
                      non_cap_zero_to_one=coverage([t for t in zero if not cap(t)], [t for t in one if not cap(t)]),
                      non_cap_one_to_zero=coverage([t for t in one if not cap(t)], [t for t in zero if not cap(t)]),
                      all_support_triangles_material_uv_exact=support_inventory(models[0]) == support_inventory(models[1]),
                      support_triangle_count=sum(support_inventory(models[0]).values()),
                      all_material_bytes_exact=[m['raw'] for m in models[0]['materials']] == [m['raw'] for m in models[1]['materials']],
                      uv_zero_to_one=uv_audit(records(models[0]), records(models[1])),
                      uv_one_to_zero=uv_audit(records(models[1]), records(models[0])),
                      full_straight_solid=outer_solid_summary(zero, one, [(z, z) for z in (-7.99, -6., -4., -2., .1234567, 2., 4., 6., 7.99)]),
                      retained_core_collar_to_straight=coverage(clip_patch(core, -8., -7.75), clip_patch(one, -8., -7.75)),
                      straight_to_retained_core_collar=coverage(clip_patch(one, -8., -7.75), clip_patch(core, -8., -7.75)),
                      core_straight_actual_seam_solid=outer_solid_summary(one, core, [(7.99, -7.99)]),
                      inherited_native_seam_solid=outer_solid_summary(native, zero, [(7.99, -7.99)]))
        for key in ('actual_cap_coverage', 'non_cap_zero_to_one', 'non_cap_one_to_zero',
                    'retained_core_collar_to_straight', 'straight_to_retained_core_collar'):
            assert result[key]['all_faces_covered'], key
        assert result['all_support_triangles_material_uv_exact'] and result['support_triangle_count'] == 26
        assert result['all_material_bytes_exact']
        assert result['full_straight_solid']['robust_interval_count_mismatches'] == 0
        assert result['full_straight_solid']['maximum_robust_edge_difference_m'] < TOL
        assert result['core_straight_actual_seam_solid']['robust_interval_count_mismatches'] == 0
        assert result['core_straight_actual_seam_solid']['maximum_robust_edge_difference_m'] < TOL
        assert result['uv_zero_to_one']['mismatching_face_count'] == 10
        assert result['uv_zero_to_one']['sum_mismatching_face_areas_m2'] < 2e-6
        assert result['uv_one_to_zero']['mismatching_face_count'] == 0
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
