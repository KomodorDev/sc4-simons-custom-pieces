"""First-A diagonal transition middle solids, saved paths, and packaging.

Literal native collars are authored separately from the new curved middle.
Every variant is cut on the city grid afresh; retained orthogonal sources
and their default outputs are never patched or selected by this writer.
"""
from collections import defaultdict
from copy import deepcopy
import hashlib
import json
import math
import struct

from scp.dbpf import require
from scp.models import parse_s3d,pack_s3d
from . import diagonal_transition_geometry as geometry
from . import diagonal_transition_layout as layout
from . import diagonal_transition_native as native
from .diagonal_transition_variants import record_for,variant_of
from . import orthogonal_transition,ramp_geometry,ramp_paths

PREFIX='SCP diagonal DD transition '
ATLAS_SIZE=(512,1024)
ATLAS_COLUMN={'upper':8,'lower':264}
ATLAS_ROW=128
BRIDGE=1.
INNER_FOOT=7.171875
INSETS=(0.,.21875,.265625,.5625,.625,.828125)
CROWN={'upper':1.3906240463256836,'lower':1.3906254768371582}
SHOULDER_V=.7119640111923218


def _cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def _sub(a,b):return tuple(x-y for x,y in zip(a,b))

def _quad(points,hint):
    """Keep both actual nonzero triangles and orient each one outward."""
    result=[]
    for indices in ((0,1,2),(0,2,3)):
        triangle=tuple(points[index] for index in indices)
        normal=_cross(_sub(triangle[1][:3],triangle[0][:3]),_sub(triangle[2][:3],triangle[0][:3]))
        if not any(normal):continue
        if sum(a*b for a,b in zip(normal,hint))<0.:triangle=(triangle[0],triangle[2],triangle[1])
        result.append(triangle)
    return result


def _encoded_triangle_normal(triangle):
    """Return the exact3D cross product of the actual local float32 positions."""
    points=[struct.unpack('<3f',struct.pack('<3f',*point[:3]))for point in triangle]
    return _cross(_sub(points[1],points[0]),_sub(points[2],points[0]))


def _encoded_triangle_has_area(triangle):
    """Keep every nonzero3D face after the actual local float32 encoding.

    City clipping can create a positive double-precision sliver whose vertices
    become exactly collinear when saved. Such a triangle has no encoded road
    surface. This uses no projected-area test, distance bound, or area epsilon.
    """
    return any(_encoded_triangle_normal(triangle))


def _triangle_for_packing(triangle,reference_normal=None):
    """Preserve actual source winding and every positive encoded face.

    A very thin child can reverse winding when rounded even though all saved
    points still lie on the original parent. Reordering the complete vertices
    preserves its finite geometry and UV field, and restores outward winding.
    """
    normal=_encoded_triangle_normal(triangle)
    if not any(normal):return None
    reference_normal=reference_normal or _cross(_sub(triangle[1][:3],triangle[0][:3]),
                                               _sub(triangle[2][:3],triangle[0][:3]))
    orientation=sum(a*b for a,b in zip(normal,reference_normal))
    require(orientation!=0.,'Float32 diagonal face has ambiguous original source winding')
    return(triangle[0],triangle[2],triangle[1])if orientation<0. else triangle


def _materials(context,texture_id):
    dd=native.source_faces(context,0x57530200)
    ground=native.source_faces(context,0x57030200)
    body=next(group['material'] for group in dd if group['role']=='body')
    barrier=next(group['material'] for group in dd if group['role']=='barrier')
    atlas=ramp_geometry.road_material(texture_id,ground[0]['material'])
    return {'body':deepcopy(body),'barrier':deepcopy(barrier),'pavement-atlas':atlas}


def _base(deck,s):return geometry.height(deck,s)+geometry.pavement_datum(deck,s)

def _clamp_station(deck):
    lo,hi=geometry.COLLAR,geometry.LENGTH-geometry.COLLAR
    for _ in range(60):
        middle=(lo+hi)/2.
        if _base(deck,middle)>1.:lo=middle
        else:hi=middle
    return (lo+hi)/2.


def section_factory(context,texture_id,*,variant='original'):
    """Return the explicit closed middle ring callback used by the collars."""
    record=record_for(variant);materials=_materials(context,texture_id)
    asphalt_breaks=sorted({-INNER_FOOT,INNER_FOOT,0.,
        *(sign*(geometry.LANE_OFFSET+offset) for sign in(-1,1)for offset in(-1.25,0.,1.25))})
    roof_breaks=sorted({*asphalt_breaks,*(sign*(8.-inset)for sign in(-1,1)for inset in INSETS)})
    def section(deck,s):
        require(deck in('upper','lower'),'Unknown diagonal middle deck')
        base=_base(deck,s);floor=max(0.,base-1.);taper=geometry.cubic(geometry.height(deck,s)/2.)
        centre,normal=geometry.frame(deck,s,variant=variant)
        def point(u,h,uv):return(centre[0]+u*normal[0],centre[1]+u*normal[1],h,*uv)
        def uv(role,u,h,v=None):
            if role=='pavement-atlas':
                t=(u+8.)/16.
                if record.physical_reflection!=record.traffic_reversed:t=1.-t
                if deck=='lower':t=1.-t
                return((ATLAS_COLUMN[deck]+128.*t)/ATLAS_SIZE[0],(ATLAS_ROW+8.*s)/ATLAS_SIZE[1])
            if role=='barrier':return(s/16.,v)
            return(u/8.,(s+h)/8.)
        segments=[]
        def add(role,a,b,kind='roof'):
            u0,h0,v0=a;u1,h1,v1=b
            segments.append({'role':deck+'-'+role,'deck':deck,'material':materials[role],
                'a':point(u0,h0,uv(role,u0,h0,v0)),'b':point(u1,h1,uv(role,u1,h1,v1)),
                'surface_kind':kind,
                'outward_hint_ENH':(-(h1-h0)*normal[0],-(h1-h0)*normal[1],u1-u0)})
        rises=(0.,.328125,CROWN[deck],CROWN[deck],.328125,0.)
        # Each shoulder/crown face keeps its own V phase at repeated crest vertices.
        bands=((1.,SHOULDER_V),(SHOULDER_V,0.),(.32499998807907104,.625),(0.,SHOULDER_V),(SHOULDER_V,1.))
        for side in(-1,1):
            nodes=[(side*(8.-inset),base+rise*taper)for inset,rise in zip(INSETS,rises)]
            for index,((u0,h0),(u1,h1))in enumerate(zip(nodes,nodes[1:])):
                v0,v1=bands[index]
                a,b=(u0,h0,v0),(u1,h1,v1)
                if side>0:a,b=b,a
                add('barrier',a,b)
        # Sort roof faces into a single left-to-right ring, preserving separate UV endpoints.
        for a,b in zip(asphalt_breaks,asphalt_breaks[1:]):add('pavement-atlas',(a,base,None),(b,base,None))
        segments.sort(key=lambda row:sum((row['a'][i]-centre[i])*normal[i] for i in range(2)))
        add('body',(8.,base,None),(8.,floor,None),'sidewall')
        for a,b in zip(reversed(roof_breaks),list(reversed(roof_breaks))[1:]):add('body',(a,floor,None),(b,floor,None),'underside')
        add('body',(-8.,floor,None),(-8.,base,None),'sidewall')
        require(all(math.dist(a['b'][:3],b['a'][:3])<1e-9 for a,b in zip(segments,(*segments[1:],segments[0]))),
                'Diagonal middle section is not geometrically closed')
        return segments
    return section


def middle_groups(context,texture_id,*,variant='original',section=None,start=None,end=None):
    section=section or section_factory(context,texture_id,variant=variant)
    start=geometry.COLLAR+BRIDGE if start is None else start
    end=geometry.LENGTH-geometry.COLLAR-BRIDGE if end is None else end
    stations=sorted({start,end,*(s for s in geometry.STATIONS if start<s<end),
                     *(_clamp_station(deck)for deck in('upper','lower'))})
    stations=[s for s in stations if start<=s<=end]
    groups={}
    for deck in('upper','lower'):
        for first,last in zip(stations,stations[1:]):
            a,b=section(deck,first),section(deck,last)
            require(len(a)==len(b),'Middle cross-section topology changes within a slab')
            for left,right in zip(a,b):
                require(left['role']==right['role'],'Middle material ordering changed')
                if left['surface_kind']=='underside' and _base(deck,first)==_base(deck,last)==0.:
                    # The flat ground road is a zero-depth sheet. It has no
                    # coincident opposite-facing concrete underside; positive
                    # slabs, including their clamped H=0 bottom, remain closed.
                    continue
                row=groups.setdefault(left['role'],{'role':left['role'],'deck':deck,'material':left['material'],
                                                    'kind':'authored-middle','triangles_ENHUV':[]})
                points=(left['a'],left['b'],right['b'],right['a'])
                if left['surface_kind']=='underside':
                    # The closed ring traverses the floor right-to-left. Keep
                    # the roof's A_low-to-B_high diagonal before flipping its
                    # winding downward; rotating corners would change planes.
                    points=(left['b'],left['a'],right['a'],right['b'])
                row['triangles_ENHUV'].extend(_quad(points,left['outward_hint_ENH']))
    return list(groups.values())


def support_groups(context,*,variant='original'):
    body=next(group['material']for group in native.source_faces(context,0x57530200)if group['role']=='body')
    result=[]
    for record in geometry.support_specifications(variant=variant):
        vertices=[(e,n,h,e/8.,(-n+h)/8.)for h in(record['bottom_m'],record['top_m'])for e,n in record['corners_EN_m']]
        centre=tuple(sum(p[i]for p in vertices)/8. for i in range(3));triangles=[]
        for indices in((0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,0)):
            points=[vertices[i]for i in indices];hint=tuple(sum(p[i]for p in points)/4.-centre[i]for i in range(3))
            triangles.extend(_quad(points,hint))
        result.append({'role':record['id'],'deck':record['deck'],'material':body,'kind':'authored-support','triangles_ENHUV':triangles})
    return result


def encode_paths(routes,world_cell,*,variant='original'):
    sources={row['id']:row for row in geometry.traffic_routes(variant=variant)}
    def contact(row):
        first,last=sources[row['id']]['points'][0],sources[row['id']]['points'][-1]
        points=[(p[0]+16.*world_cell[0],p[1]-16.*world_cell[1],p[2])for p in(row['points'][0],row['points'][-1])]
        return next((target for target in(first,last)if any(math.dist(p,target)<1e-7 for p in points)),None)
    ordered=sorted(deepcopy(routes),key=lambda row:(contact(row)is None,row['id']))
    used=defaultdict(set);lines=['SC4PATHS','1.2',str(len(ordered)),'0','1']
    for row in ordered:
        endpoint=contact(row);lane=row['lane']+(1 if endpoint is not None and abs(endpoint[2])<1e-9 else 0)
        pair=row.get('transport',1),row['entry'],row['exit']
        if endpoint is not None:require(lane not in used[pair],'Two native diagonal contacts request one engine lane class')
        else:
            while lane in used[pair]:lane+=1
        used[pair].add(lane)
        lines.extend((f"-- SCP diagonal transition {row['id']} source_lane={row['lane']}",str(pair[0]),str(lane),
                      str(row['entry']),str(row['exit']),'0',str(len(row['points']))))
        lines.extend(','.join(format(float(v),'.9f').rstrip('0').rstrip('.')if v else'0'for v in point)for point in row['points'])
    return ('\r\n'.join(lines)+'\r\n').encode('ascii')


def construction_fields(spec,compiled):
    from scp.verify import parse_paths
    width,depth=spec['footprint'];rows=[['.']*(width+2)for _ in range(depth+1)];cons=deepcopy(rows)
    rows[0][-1]=cons[0][-1]='<';rows[-1][0]=cons[-1][0]='^';checks=[]
    for index,(cell,_model,raw)in enumerate(compiled):
        symbol=ramp_paths.construction_symbol(index);rows[cell[1]][cell[0]]=symbol;cons[cell[1]][cell[0]]='#'
        routes=[ramp_paths._route_metadata(row,'saved-diagonal')for row in parse_paths(raw)['routes']]
        checks.append(f'{symbol} - dirtroad: 0x{ramp_paths.construction_flags(routes):08X}')
    return [''.join(row)for row in rows],checks,[''.join(row)for row in cons]


def _atlas_native_fields(context,texture_id,*,variant='original'):
    """Measure finite native UV owners at the two actual atlas interfaces.

    The native alternating halves have different signed longitudinal fields.
    A single global phase cannot represent them. These small interval records
    retain each selected original parent's field, without copying its mesh.
    They affect owned texture pixels only, never the model or path geometry.
    """
    from .diagonal_transition_collars import build_collars
    from shapely.geometry import LineString,shape
    collars=build_collars(context,variant=variant,
                          middle_section=section_factory(context,texture_id,variant=variant))
    direction=geometry.LONGITUDINAL_EN
    fields={}
    def section_points(triangle,centre,station):
        result=[]
        values=[sum((p[i]-centre[i])*direction[i]for i in range(2))-station for p in triangle]
        values=[0. if abs(value)<=2e-10 else value for value in values]
        for index,a in enumerate(triangle):
            b=triangle[(index+1)%3];x,y=values[index],values[(index+1)%3]
            if x==0.:result.append(a)
            if x*y<0.:
                t=x/(x-y);result.append(tuple(u+t*(v-u)for u,v in zip(a,b)))
        unique=[]
        for p in result:
            if not any(math.dist(p[:3],q[:3])<1e-10 for q in unique):unique.append(p)
        if len(unique)<2:return None
        return max(((a,b)for i,a in enumerate(unique)for b in unique[i+1:]),key=lambda x:math.dist(x[0][:3],x[1][:3]))
    for deck in('upper','lower'):
        fields[deck]={}
        centre,normal=geometry.frame(deck,geometry.COLLAR,variant=variant)
        lateral=lambda p:sum((p[i]-centre[i])*normal[i]for i in range(2))
        line=LineString([tuple(centre[i]-30.*normal[i]for i in range(2)),
                         tuple(centre[i]+30.*normal[i]for i in range(2))])
        bounds=[]
        for patch in collars['source_scopes']['DD_phase_floor_patches']:
            if patch['deck']!=deck:continue
            cross=shape(patch['plan_geometry']).intersection(line)
            parts=[cross]if cross.geom_type=='LineString'else list(getattr(cross,'geoms',[]))
            bounds.extend(lateral(p)for part in parts if part.geom_type=='LineString'for p in part.coords)
        require(bounds,'Native DD atlas has no measured complete floor section')
        low,high=min(bounds),max(bounds)
        anchors=((low,-8.),(-geometry.LANE_OFFSET,-geometry.LANE_OFFSET),(0.,0.),
                 (geometry.LANE_OFFSET,geometry.LANE_OFFSET),(high,8.))
        def mapped(u):
            for(a,x),(b,y)in zip(anchors,anchors[1:]):
                if a-1e-8<=u<=b+1e-8:return x+(u-a)*(y-x)/(b-a)
            raise ValueError(f'Native DD UV owner escapes its measured floor section: {deck},u={u},bounds={(low,high)}')
        rows=[];reference=geometry.COLLAR+1.
        refcentre,refnormal=geometry.frame(deck,reference,variant=variant)
        for group in collars['groups']:
            if group['deck']!=deck or not group['role'].startswith(f'dd-{deck}-pavement-native-profile-loft-'):continue
            provenance=group['source_provenance'];parent=provenance['parent_triangle']
            for triangle in group['triangles_ENHUV']:
                points=section_points(triangle,centre,0.)
                if points is None:continue
                a,b=sorted(points,key=lateral)
                u0,u1=max(low,lateral(a)),min(high,lateral(b))
                if u1-u0<=1e-10:continue
                # The same anchor mapping as the physical1m bridge; it keeps
                # the native lane positions and maps only the outer shoulders.
                split=sorted({u0,u1,*(u for u,_v in anchors if u0<u<u1)})
                for x,y in zip(split,split[1:]):
                    nominal=(mapped(x),mapped(y))
                    rows.append((nominal,parent,provenance,reference,refcentre,refnormal))
        require(rows,'Native DD atlas has no finite source-parent pavement owner')
        ground=collars['ground_inner_profiles'][deck]
        ground_centre,ground_normal=geometry.frame(deck,geometry.LENGTH-geometry.COLLAR,variant=variant)
        local=lambda p:sum((p[i]-ground_centre[i])*ground_normal[i]for i in range(2))
        g_low=min(local(p)for row in ground for p in(row['a'],row['b']))
        g_high=max(local(p)for row in ground for p in(row['a'],row['b']))
        phases={'dd':rows,'ground':[]}
        for row in ground:
            a,b=sorted((row['a'],row['b']),key=local);x,y=local(a),local(b)
            if y-x<=1e-10:continue
            nominal=(-8.+16.*(x-g_low)/(g_high-g_low),-8.+16.*(y-g_low)/(g_high-g_low))
            phases['ground'].append((nominal,None,row['source_provenance'],geometry.LENGTH-geometry.COLLAR,
                                     ground_centre,ground_normal,(a,b)))
        for kind,source_rows in phases.items():
            measured=[]
            for row in source_rows:
                (x,y),parent,provenance,reference,refcentre,refnormal,*ground_points=row
                affine=native.surface_fields(parent)['source_affine_UV_ENH']if parent else provenance['source_affine_UV_ENH']
                if ground_points:
                    a,b=ground_points[0]
                    start_uv=a[3:];du=tuple((b[i]-a[i])/(y-x)for i in(3,4))
                else:
                    start=(*tuple(refcentre[i]+x*refnormal[i]for i in range(2)),parent[0][2])
                    start_uv=tuple(sum(a*b for a,b in zip(affine[label]['gradient_ENH'],start))+affine[label]['offset']for label in('U','V'))
                    du=tuple(sum(affine[label]['gradient_ENH'][i]*refnormal[i]for i in range(2))for label in('U','V'))
                measured.append({'lateral_interval_m':(x,y),'reference_station_m':reference,
                    'UV_at_first_lateral':start_uv,'dUV_d_lateral_m':du,
                    'dUV_d_station_m':tuple(sum(affine[label]['gradient_ENH'][i]*direction[i]for i in range(2))for label in('U','V')),
                    'source_model_sha256':provenance['source_model_sha256'],
                    'source_parent_ENHUV_sha256':provenance.get('source_parent_ENHUV_sha256',
                        hashlib.sha256(json.dumps(parent,separators=(',',':')).encode()).hexdigest()),
                    'native_tile_id':provenance['native_tile_id'],'pose':provenance['pose'],
                    'source_world_cell':provenance['world_cell']})
            fields[deck][kind]=sorted(measured,key=lambda row:row['lateral_interval_m'])
    return fields


def _atlas_field_at(rows,lateral):
    """Select the finite owner; only unused atlas gutters use nearest fields."""
    require(rows,'Missing native atlas field intervals')
    return min(rows,key=lambda row:max(row['lateral_interval_m'][0]-lateral,
                                       lateral-row['lateral_interval_m'][1],0.))


def build_textures(context,texture_id,*,variant='original'):
    """Generate an owned atlas from pinned native pixels, without public assets."""
    from PIL import Image
    from scp.preview import decode_fsh
    record=record_for(variant);sources={}
    for iid,pin in native.TEXTURE_SHA256.items():
        raw=context['rhw4_textures'][*native.TEXTURE,iid]
        require(hashlib.sha256(raw).hexdigest()==pin,'Native diagonal asphalt pixels changed')
        image=decode_fsh(raw).convert('RGBA');require(image.size==(128,128),'Native asphalt resolution changed')
        sources[iid]=image.load()
    fields=_atlas_native_fields(context,texture_id,variant=variant)
    atlas=Image.new('RGBA',ATLAS_SIZE,(0,0,0,0));target=atlas.load()
    def sample(image,u,v):
        x,y=(u%1.)*128.-.5,(v%1.)*128.-.5;ix,iy=math.floor(x),math.floor(y);fx,fy=x-ix,y-iy
        return tuple(sum(image[(ix+a)%128,(iy+b)%128][c]*(fx if a else 1.-fx)*(fy if b else 1.-fy)
                         for a,b in((0,0),(1,0),(0,1),(1,1)))for c in range(4))
    for deck in('upper','lower'):
        columns={}
        for column in range(-2,130):
            t=((column%128)+.5)/128.
            if record.physical_reflection!=record.traffic_reversed:t=1.-t
            if deck=='lower':t=1.-t
            lateral=-8.+16.*t
            columns[column]=(lateral,{kind:_atlas_field_at(fields[deck][kind],lateral)for kind in('dd','ground')})
        for row in range(ATLAS_SIZE[1]):
            s=(row-ATLAS_ROW+.5)/8.;height=geometry.height(deck,s);native_height=15. if deck=='upper' else 7.5
            blend=1.-height/native_height;alpha=1.-geometry.cubic(height/.25)
            for column in range(-2,130):
                lateral,owners=columns[column];pixels=[]
                for kind,iid in(('dd',0x5713000E),('ground',0x5703000E)):
                    field=owners[kind];du=lateral-field['lateral_interval_m'][0];ds=s-field['reference_station_m']
                    uv=tuple(field['UV_at_first_lateral'][i]+du*field['dUV_d_lateral_m'][i]+ds*field['dUV_d_station_m'][i]for i in range(2))
                    pixels.append(sample(sources[iid],*uv))
                a,b=pixels
                target[ATLAS_COLUMN[deck]+column,row]=tuple(min(255,max(0,round(x+(alpha if i==3 else blend)*(y-x))))
                                                          for i,(x,y)in enumerate(zip(a,b)))
    return {(*native.TEXTURE,texture_id):orthogonal_transition._encode_fsh(atlas)}


def _partition(triangles):
    """Exact-sign clipping retaining every actual nonzero clipped triangle."""
    result=defaultdict(list)
    for triangle in triangles:
        points=[]
        for point in triangle:
            vertex=list(point)
            for axis in(0,2):
                boundary=round((vertex[axis]+8.)/16.)*16.-8.
                if abs(vertex[axis]-boundary)<=1e-9:vertex[axis]=boundary
            points.append(tuple(vertex))
        xs,zs=[p[0]for p in points],[p[2]for p in points]
        a,b=math.floor((min(xs)+8.)/16.),math.floor((max(xs)+8.-1e-12)/16.)
        c,d=math.floor((min(zs)+8.)/16.),math.floor((max(zs)+8.-1e-12)/16.)
        for column in range(a,max(a,b)+1):
            for row in range(c,max(c,d)+1):
                polygon=points
                for axis,boundary,sign in((0,16.*column-8.,1.),(0,16.*column+8.,-1.),(2,16.*row-8.,1.),(2,16.*row+8.,-1.)):
                    polygon=orthogonal_transition._clip_plane(polygon,axis,boundary,sign)
                local=[(p[0]-16.*column,p[1],p[2]-16.*row,*p[3:])for p in polygon]
                for index in range(1,len(local)-1):
                    tri=(local[0],local[index],local[index+1])
                    if any(_cross(_sub(tri[1][:3],tri[0][:3]),_sub(tri[2][:3],tri[0][:3]))):result[column,row].append(tri)
    return dict(result)


class _Painter:
    def __init__(self,groups):
        self.materials={}
        for group in groups:
            role,material=group['role'],group['material']
            require(role not in self.materials or self.materials[role]==material,'One diagonal mesh role has different materials')
            self.materials[role]=deepcopy(material)
        self.roles=tuple(self.materials)


def world_geometry(context,texture_id,*,variant='original'):
    """Combine the complete authored middle with explicit finite native collars."""
    from .diagonal_transition_collars import build_collars
    # The collar author controls finite source regions, never this nominal mask.
    section=section_factory(context,texture_id,variant=variant)
    collars=build_collars(context,variant=variant,middle_section=section)
    groups=[*middle_groups(context,texture_id,variant=variant,section=section,
                           start=collars['middle_start_s'],end=collars['middle_end_s']),
            *collars['groups'],*support_groups(context,variant=variant)]
    require(all(not group.get('analysis_only')for group in groups),'Native reference geometry cannot be packed into the DAT')
    painter=_Painter(groups);owned=set(layout.world_cells(variant=variant));tiles=defaultdict(list)
    for group in groups:
        code=painter.roles.index(group['role'])
        triangles=[tuple((p[0],p[2],-p[1],p[3],p[4],float(code))for p in triangle)for triangle in group['triangles_ENHUV']]
        if 'host_world_cell'in group:
            host=tuple(group['host_world_cell'])
            require(group.get('kind')=='literal-native'and group.get('source_provenance')and host in owned,
                    'Only a scoped literal native source fragment can retain its original overhang host')
            tiles[host].extend(tuple((p[0]-16.*host[0],p[1],p[2]-16.*host[1],*p[3:])for p in tri)for tri in triangles)
            continue
        for cell,faces in _partition(triangles).items():
            if cell not in owned:
                # A vertical face on a city boundary has no positive plan area;
                # host it on an actual neighboring owner rather than invent a tile.
                candidates=[]
                for host in owned:
                    moved=[tuple((p[0]+16.*(cell[0]-host[0]),p[1],p[2]+16.*(cell[1]-host[1]),*p[3:])for p in tri)for tri in faces]
                    if all(abs(p[0])<=8.+1e-9 and abs(p[2])<=8.+1e-9 for tri in moved for p in tri):candidates.append((host,moved))
                require(candidates,f'Authored diagonal geometry enters an unowned/native cell:{cell}')
                host,moved=min(candidates,key=lambda item:item[0]);tiles[host].extend(moved)
            else:tiles[cell].extend(faces)
    require(set(tiles)==owned,'Actual diagonal positive-area model hosts differ from the declared source mask: '
            f'missing={sorted(owned-set(tiles))},extra={sorted(set(tiles)-owned)}')
    paths=ramp_paths.slice_routes(geometry.traffic_routes(variant=variant))
    require(set(paths)<=owned,'A saved diagonal car path enters an unowned/native cell')
    template=parse_s3d(native.resource(context,(*native.S3D,0x57530200)))
    return {'tiles':dict(tiles),'paths':paths,'painter':painter,'template':template,'collars':collars,
            'groups':groups,'variant':variant,'source_only':True}


def compile_module(spec,context):
    variant=variant_of(spec);record=layout.declaration(spec)
    texture_id=int(spec['authored_texture_ids'][0],16)
    world=world_geometry(context,texture_id,variant=variant);origin=record['world_origin_cell'];compiled=[]
    references={}
    for group in world['groups']:
        parent=group.get('source_provenance',{}).get('parent_triangle')
        if parent is not None:
            points=[(p[0],p[2],-p[1])for p in parent]
            references[group['role']]=_cross(_sub(points[1],points[0]),_sub(points[2],points[0]))
    for local in map(tuple,spec['cells']):
        cell=(local[0]+origin[0],local[1]+origin[1])
        triangles=[]
        for face in world['tiles'][cell]:
            role=world['painter'].roles[round(face[0][5])]
            encoded=_triangle_for_packing(face,references.get(role))
            if encoded is not None:triangles.append(encoded)
        require(triangles,'A diagonal owned host contains no finite encoded model face')
        raw=orthogonal_transition._pack_model(triangles,world['painter'],world['template'])
        model=parse_s3d(raw)
        for mesh in model['meshes']:mesh['name']=mesh['name'].replace(b'SCP DD transition ',PREFIX.encode(),1)
        compiled.append((local,pack_s3d(model),encode_paths(world['paths'].get(cell,[]),cell,variant=variant)))
    return compiled


def build_piece(spec,context):
    from .recipes import finish_piece,construction
    from .model_shadows import add_shadows
    from .diagonal_transition_approaches import add_approaches,check_native_continuation
    check_native_continuation(context['controller'])
    compiled=compile_module(spec,context);assets=finish_piece(spec,context,compiled)
    assets.update(build_textures(context,int(spec['authored_texture_ids'][0],16),variant=variant_of(spec)))
    rows,checks,cons=add_approaches(spec,*construction_fields(spec,compiled))
    return add_shadows(spec,context,compiled,assets),construction(spec,rows,checks,cons)
