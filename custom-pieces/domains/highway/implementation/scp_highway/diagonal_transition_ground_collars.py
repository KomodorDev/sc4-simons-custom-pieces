"""Finite literal ground collars and the named first-A middle bridges.

Only original ground source-parent fragments retain their native host-cell
projection. Newly authored bridge/body faces receive ordinary city clipping.
Already rendered outside native faces are references, never duplicated DATs.
"""
from copy import deepcopy
from collections import defaultdict
import hashlib
import json
import math

from shapely import constrained_delaunay_triangles
from shapely.geometry import Polygon,LineString,box
from shapely.ops import unary_union
from scp.dbpf import require
from . import diagonal_transition_geometry as geometry
from . import diagonal_transition_native as native
from . import diagonal_transition_layout as layout


def _sha(value):return hashlib.sha256(json.dumps(value,separators=(',',':')).encode()).hexdigest()
def _cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def _sub(a,b):return tuple(x-y for x,y in zip(a,b))


def _attribute(parent,east,north):
    a,b,c=parent;d=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
    require(d!=0.,'Ground source-parent has no finite paved plan area')
    u=((b[1]-c[1])*(east-c[0])+(c[0]-b[0])*(north-c[1]))/d
    v=((c[1]-a[1])*(east-c[0])+(a[0]-c[0])*(north-c[1]))/d
    return(east,north,*(u*a[i]+v*b[i]+(1-u-v)*c[i]for i in(2,3,4)))


def _clip(polygon,socket):
    result=list(polygon)
    # Explicit finite source ROI: custom side of the actual city cut and C
    # metres inward, measured along the native directed axis toward custom.
    # Negative station remains valid at the source shoulder; only the finite
    # original parent and north city cut bound that side of the collar.
    q=socket.inward_en;origin=socket.mouth_en
    fields=(lambda p:p[1]-socket.joining_coordinate,
            lambda p:geometry.COLLAR-((p[0]-origin[0])*q[0]+(p[1]-origin[1])*q[1]))
    for distance in fields:
        clipped=[]
        if not result:break
        previous=result[-1];before=distance(previous)
        for current in result:
            after=distance(current)
            if (before>=0.)!=(after>=0.):
                t=before/(before-after)
                clipped.append(tuple(a+t*(b-a)for a,b in zip(previous,current)))
            if after>=0.:clipped.append(current)
            previous,before=current,after
        result=clipped
    return result


def _triangulate(shape,parent):
    result=[]
    parts=[shape]if shape.geom_type=='Polygon'else list(getattr(shape,'geoms',[]))
    for part in parts:
        if part.geom_type!='Polygon'or part.area==0.:continue
        require(part.is_valid,'Ground source clipping produced an invalid finite polygon')
        for triangle in constrained_delaunay_triangles(part).geoms:
            if triangle.area==0.:continue
            points=tuple(_attribute(parent,*point)for point in list(triangle.exterior.coords)[:3])
            normal=_cross(_sub(points[1][:3],points[0][:3]),_sub(points[2][:3],points[0][:3]))
            if normal[2]<0.:points=(points[0],points[2],points[1])
            result.append(points)
    return result


def _recut_literal(groups,variant):
    """Use every real planned free host; retain overhang only into native cells."""
    from .orthogonal_transition import _clip_plane
    owned=set(layout.world_cells(variant=variant));result=[]
    for group in groups:
        original_host=tuple(group['host_world_cell']);by_host=defaultdict(list)
        reserved_by_host=defaultdict(set)
        for triangle in group['triangles_ENHUV']:
            east,north=[p[0]for p in triangle],[p[1]for p in triangle]
            c0,c1=math.floor((min(east)+8.)/16.),math.floor((max(east)+8.-1e-12)/16.)
            r0,r1=math.floor((8.-max(north))/16.),math.floor((8.-min(north)-1e-12)/16.)
            for c in range(c0,max(c0,c1)+1):
                for r in range(r0,max(r0,r1)+1):
                    polygon=list(triangle)
                    for axis,boundary,sign in((0,16*c-8.,1.),(0,16*c+8.,-1.),(1,-16*r-8.,1.),(1,-16*r+8.,-1.)):
                        polygon=_clip_plane(polygon,axis,boundary,sign)
                    if len(polygon)<3 or Polygon([p[:2]for p in polygon]).area==0.:continue
                    cell=(c,r)
                    if cell in owned:host=cell
                    else:
                        require(layout.is_reserved_native_cell(cell,variant=variant) and original_host in owned,
                                f'Literal ground source needs an unreviewed free host:{cell}')
                        host=original_host;reserved_by_host[host].add(cell)
                    for index in range(1,len(polygon)-1):
                        child=(polygon[0],polygon[index],polygon[index+1])
                        if Polygon([p[:2]for p in child]).area:by_host[host].append(child)
        for host,triangles in by_host.items():
            provenance=deepcopy(group['source_provenance'])
            provenance.update(actual_host_world_cell=host,original_source_host_world_cell=original_host,
                retained_overhang_only_into_reserved_cells=sorted(reserved_by_host[host]),
                source_fragment_geometry=unary_union([Polygon([p[:2]for p in tri])for tri in triangles]).__geo_interface__)
            result.append({**group,'role':group['role']+f'-host-{host[0]}-{host[1]}','host_world_cell':host,
                           'triangles_ENHUV':triangles,'source_provenance':provenance})
    return result


def _profile_segments(groups,socket):
    q=socket.inward_en;origin=socket.mouth_en;rows=[]
    for group in groups:
        for triangle in group['triangles_ENHUV']:
            points=[]
            for a,b in zip(triangle,(*triangle[1:],triangle[0])):
                x=sum((a[i]-origin[i])*q[i]for i in range(2))-geometry.COLLAR
                y=sum((b[i]-origin[i])*q[i]for i in range(2))-geometry.COLLAR
                x=0. if abs(x)<2e-10 else x
                y=0. if abs(y)<2e-10 else y
                if x==0.:points.append(a)
                if x*y<0.:
                    t=x/(x-y);points.append(tuple(a[i]+t*(b[i]-a[i])for i in range(5)))
            unique=[]
            for point in points:
                if not any(math.dist(point[:3],other[:3])<1e-10 for other in unique):unique.append(point)
            if len(unique)>2:
                unique=list(max(((a,b)for i,a in enumerate(unique)for b in unique[i+1:]),key=lambda row:math.dist(row[0][:3],row[1][:3])))
            if len(unique)==2 and math.dist(unique[0][:3],unique[1][:3])>1e-10:
                rows.append({'role':group['role'],'deck':socket.arm,'material':group['material'],
                             'a':unique[0],'b':unique[1],'source_provenance':group['source_provenance']})
    require(rows,'Ground literal collar has no complete inner joining profile')
    return rows


def _bridge(deck,variant,profiles,middle_section):
    from .diagonal_transition import _quad
    first=geometry.LENGTH-geometry.COLLAR-1.;last=geometry.LENGTH-geometry.COLLAR
    target=middle_section(deck,first)
    centre,normal=geometry.frame(deck,last,variant=variant)
    lateral=lambda p:sum((p[i]-centre[i])*normal[i]for i in range(2))
    source=[]
    for row in profiles:
        a,b=row['a'],row['b']
        if lateral(a)>lateral(b):a,b=b,a
        source.append((lateral(a),lateral(b),a,b))
    low=min(row[0]for row in source);high=max(row[1]for row in source)
    require(high>low,'Ground joining profile has no physical width')
    roof=[(index,row)for index,row in enumerate(target)if row.get('surface_kind')=='roof']
    require(roof and all(0.<=p[2]<1. for _,row in roof for p in(row['a'],row['b'])),
            'Ground bridge must retain its reviewed sub-one-metre ground-clamped body scope')
    start_centre,start_normal=geometry.frame(deck,first,variant=variant)
    local=lambda p:sum((p[i]-start_centre[i])*start_normal[i]for i in range(2))
    cuts={0.,1.}
    for a,b,_x,_y in source:cuts.update(((a-low)/(high-low),(b-low)/(high-low)))
    for _index,row in roof:cuts.update(((local(row['a'])+8.)/16.,(local(row['b'])+8.)/16.))
    cuts=sorted(value for value in cuts if -1e-10<=value<=1.+1e-10);cuts=[min(1.,max(0.,value))for value in cuts]
    unique=[]
    for value in cuts:
        if not unique or abs(value-unique[-1])>1e-12:unique.append(value)
    groups={};all_edges=[]
    def at_native(t):
        u=low+(high-low)*t
        for a,b,x,y in source:
            if a-2e-9<=u<=b+2e-9:
                v=(u-a)/(b-a);return tuple(x[i]+v*(y[i]-x[i])for i in range(5))
        raise ValueError('Finite native ground cross-profile contains an uncovered interval')
    def at_middle(row,t):
        u=-8.+16.*t;a,b=local(row['a']),local(row['b']);v=(u-a)/(b-a)
        return tuple(row['a'][i]+v*(row['b'][i]-row['a'][i])for i in range(5))
    stations=sorted({first,last,*(s for s in geometry.STATIONS if first<s<last)})
    def ring_point(row_index,t,s):
        current=middle_section(deck,s)[row_index]
        p=at_middle(current,t);native_point=at_native(t)
        alpha=(s-first)/(last-first)
        c,n=geometry.frame(deck,s,variant=variant)
        u=(1.-alpha)*(-8.+16.*t)+alpha*(low+(high-low)*t)
        xy=(c[0]+u*n[0],c[1]+u*n[1])
        if s==first:xy=p[:2]
        if s==last:xy=native_point[:2]
        return(*xy,p[2],p[3],p[4])
    body=next(item['material']for item in target if item['role']==deck+'-body')
    for a,b in zip(unique,unique[1:]):
        if a==b:continue
        u=-8.+8.*(a+b)
        index,row=next((i,r)for i,r in roof if local(r['a'])-1e-8<=u<=local(r['b'])+1e-8)
        group=groups.setdefault(row['role'],{'role':row['role'],'deck':deck,'material':row['material'],
                'kind':'authored-ground-bridge','triangles_ENHUV':[]})
        for sa,sb in zip(stations,stations[1:]):
            x,y=ring_point(index,a,sa),ring_point(index,b,sa)
            z,w=ring_point(index,b,sb),ring_point(index,a,sb)
            # Each source station has its actual cubic height. No single1m
            # chord replaces the saved0.125m driving samples.
            group['triangles_ENHUV'].extend(_quad((x,y,z,w),(0.,0.,1.)))
            if max(x[2],y[2],z[2],w[2])>0.:
                role=deck+'-body'
                floor=groups.setdefault(role,{'role':role,'deck':deck,'material':body,
                      'kind':'authored-ground-bridge','triangles_ENHUV':[]})
                points=[]
                for node,t,station in((x,a,sa),(y,b,sa),(z,b,sb),(w,a,sb)):
                    alpha=(station-first)/(last-first)
                    lateral=(1.-alpha)*(-8.+16.*t)+alpha*(low+(high-low)*t)
                    points.append((node[0],node[1],0.,lateral/8.,station/8.))
                # Same A_low-to-B_high base diagonal, downward winding only.
                floor['triangles_ENHUV'].extend(_quad(points,(0.,0.,-1.)))
            all_edges.append((a,b,x,y,z,w,sa,sb))
    group=groups.setdefault(deck+'-body',{'role':deck+'-body','deck':deck,'material':body,
          'kind':'authored-ground-bridge','triangles_ENHUV':[]})
    for t in(0.,1.):
        for edge in all_edges:
            if abs((edge[0]if t==0. else edge[1])-t)>=1e-10:continue
            a,b=(edge[2],edge[5])if t==0. else(edge[3],edge[4])
            points=(a,b,(b[0],b[1],0.,b[3],b[4]),(a[0],a[1],0.,a[3],a[4]))
            group['triangles_ENHUV'].extend(_quad(points,tuple((1. if t else -1.)*v for v in(*normal,0.))))
    return list(groups.values())


def build_ground_collars(context,*,variant,middle_section):
    groups=[];references=[];scopes=[];ownership=[];inner_profiles={}
    for socket in native.socket_specs(variant):
        if socket.arm=='dd':continue
        deck=socket.arm;reference_polygons=[]
        for kind,placement in(('helper',socket.helper),('outward-peer',socket.outward_peer)):
            for source in native.source_faces(context,*placement):
                for index,parent in enumerate(source['triangles']):
                    polygon=_clip(parent,socket)
                    if len(polygon)<3:continue
                    shape=Polygon([p[:2]for p in polygon])
                    if shape.area==0.:continue
                    reference_polygons.append(shape)
                    provenance={'native_tile_id':source['native_tile_id'],'pose':source['pose'],'world_cell':source['world_cell'],
                        'source_mesh_index':source['mesh_index'],'source_parent_face_index':index,'source_parent_ENHUV_sha256':_sha(parent),
                        'source_model_sha256':source['source_model_sha256'],'roi':{'native_inward_station_max_m':geometry.COLLAR,'station_lower_bound':'finite original parent and north cut only',
                        'north_min_m':socket.joining_coordinate,'mouth_EN_m':socket.mouth_en,'inward_EN':socket.inward_en}}
                    provenance.update(native.surface_fields(parent),source_fragment_geometry=shape.__geo_interface__,
                                      material_sha256=hashlib.sha256(source['material']['raw']).hexdigest(),texture_ids=source['material']['textures'])
                    references.append({'role':f'native-ground-reference-{deck}-{kind}-{index}','deck':deck,'material':source['material'],
                        'triangles_ENHUV':_triangulate(shape,parent),'analysis_only':True,'source_provenance':provenance})
        unavailable=unary_union(reference_polygons);literal=[]
        first=socket.coreward_source;target,pose,cell=first
        opposite=0x57030900 if target==0x57030200 else 0x57030200
        second=(opposite,(pose+2)%4,(cell[0]+1,cell[1]))
        for placement in(first,second):
            for source in native.source_faces(context,*placement):
                for index,parent in enumerate(source['triangles']):
                    polygon=_clip(parent,socket)
                    if len(polygon)<3:continue
                    shape=Polygon([p[:2]for p in polygon]).difference(unavailable)
                    if shape.area==0.:continue
                    triangles=_triangulate(shape,parent)
                    provenance={'native_tile_id':source['native_tile_id'],'pose':source['pose'],'world_cell':source['world_cell'],
                        'source_mesh_index':source['mesh_index'],'source_parent_face_index':index,'source_parent_ENHUV_sha256':_sha(parent),
                        'source_model_sha256':source['source_model_sha256'],'material_sha256':hashlib.sha256(source['material']['raw']).hexdigest(),
                        'roi':{'native_inward_station_max_m':geometry.COLLAR,'station_lower_bound':'finite original parent and north cut only','north_min_m':socket.joining_coordinate,
                               'mouth_EN_m':socket.mouth_en,'inward_EN':socket.inward_en},'already_rendered_native_footprints_subtracted':True}
                    provenance.update(native.surface_fields(parent),source_fragment_geometry=shape.__geo_interface__,texture_ids=source['material']['textures'])
                    role=f'native-ground-literal-{deck}-{source["native_tile_id"]}-{source["mesh_index"]}-{index}'
                    group={'role':role,'deck':deck,'material':source['material'],'kind':'literal-native','triangles_ENHUV':triangles,
                           'host_world_cell':source['world_cell'],'source_provenance':provenance}
                    literal.append(group)
                    unavailable=unary_union([unavailable,shape])
        literal=_recut_literal(literal,variant)
        for group in literal:
            scopes.append({'role':group['role'],**group['source_provenance']})
            host=group['host_world_cell']
            shape=unary_union([Polygon([p[:2]for p in triangle])for triangle in group['triangles_ENHUV']])
            outside=shape.difference(box(16*host[0]-8,-16*host[1]-8,16*host[0]+8,-16*host[1]+8))
            if outside.area:
                ownership.append({'role':group['role'],'host_world_cell':host,'source_only_overhang_area_m2':outside.area,
                                  'source_only_overhang_geometry':outside.__geo_interface__,'certificate':group['source_provenance']})
        profile=_profile_segments(literal,socket);inner_profiles[deck]=profile
        groups.extend(literal);groups.extend(_bridge(deck,variant,profile,middle_section))
    return {'groups':groups,'references':references,'source_scopes':scopes,'ownership':ownership,
            'inner_profiles':inner_profiles,'middle_end_s':geometry.LENGTH-geometry.COLLAR-1.,
            'scope':'Finite source-ground collars and authored sub-one-metre bridges; no source-only closure/clearance waiver.'}
