"""Independent literal saved-resource contracts for the parallel HSR/Road tile."""
from collections import Counter
import hashlib,json,math,struct
from scp.dbpf import require,exemplar
from scp.models import parse_s3d,positions,validate_s3d
from scp.track_paths import S3D,PATH,EXEMPLAR

# Measured independently from the pinned native PATHs, not the recipe writer.
EXPECTED = [
 (7,3,1,((2.,-8.,15.5),(2.,8.,15.5))),
 (7,1,3,((-2.,8.,15.5),(-2.,-8.,15.5))),
 (1,3,1,((2.5,-8.,0.),(2.5,8.,0.))),
 (1,1,3,((-2.5,8.,0.),(-2.5,-8.,0.))),
 (2,3,1,((6.39,-8.,0.),(6.39,8.,0.))),
 (2,1,3,((-6.39,8.,0.),(-6.39,-8.,0.))),
 (2,1,0,((-6.39,8.,0.),(-6.39,2.5,0.),(-8.,2.5,0.))),
 (2,0,3,((-8.,-2.5,0.),(-6.39,-2.5,0.),(-6.39,-8.,0.))),
 (2,2,1,((8.,2.5,0.),(6.39,2.5,0.),(6.39,8.,0.))),
 (2,3,2,((6.39,-8.,0.),(6.39,-2.5,0.),(8.,-2.5,0.))),
]
HSR_MESH_SHA='e1c02cc06b3115c575d320cab1f8188bc01e68afd6c0fd9ef27323ec623ddc8d'


def _digest(item):
    return hashlib.sha256(json.dumps(item,default=lambda b:{'bytes':b.hex()},sort_keys=True,separators=(',',':')).encode()).hexdigest()


def check_paths(resources,spec,donors=None):
    from scp.verify import parse_paths,edge
    require(spec['recipe']=='rail_hsr_road_stack','Unknown parallel recipe')
    parsed=parse_paths(resources[*PATH,int(spec['tile_ids'][0],16)])
    routes=parsed['routes']
    actual=[(r['transport'],r['entry'],r['exit'],tuple(map(tuple,r['points']))) for r in routes]
    require(parsed['version']=='1.2' and Counter(actual)==Counter(EXPECTED),'Native HSR/Road/pedestrian route contract changed')
    require(all(r['lane']==0 and r['compatibility']==0 for r in routes),'Native lane or junction convention changed')
    for turns in range(4):
        for r in routes:
            for point,port in ((r['points'][0],r['entry']),(r['points'][-1],r['exit'])):
                x,y,z=point
                for _ in range(turns):x,y=-y,x
                require(edge((x,y,z))==(port-turns)%4,'Proper rotation broke native endpoint direction')
            require(len({p[2] for p in r['points']})==1,'Unwanted cross-level transfer')
    return {'route_count':10,'hsr_routes':2,'road_vehicle_routes':2,'native_pedestrian_routes':6,'proper_rotations_checked':4,'native_offsets_and_directions_preserved':True,'no_hsr_road_transfers':True}


def check_models(resources,spec,donors=None):
    from scp.verify import mesh_data
    require(spec['footprint']==[1,1] and len(spec['tile_ids'])==1,'Unexpected occupied footprint')
    tile=int(spec['tile_ids'][0],16);preview=int(spec['preview_id'],16)
    raw=resources[*S3D,tile]
    require(all(resources[*S3D,tile+z]==raw for z in range(5)),'Missing or differing zoom geometry')
    require(resources[*S3D,preview]==raw,'Cursor preview differs from the complete owned tile')
    model=parse_s3d(raw);validate_s3d(model)
    items=[mesh_data(model,m) for m in model['meshes']]
    require(len(items)==7,'Expected native deck, Road band, two pavement bands, two side pillars, and cap')
    require(_digest(items[0])==HSR_MESH_SHA,'Native HSR geometry, topology, UVs, or material changed')
    # The Road overlay has transparent shoulders. Give each ground band one
    # owner, retaining the original world-to-texture scale across their seams.
    bands=((-5.,5.,0x4b0e),(-8.,-5.,0x08200004),(5.,8.,0x08200004))
    for item,(west,east,texture) in zip(items[1:4],bands):
        points=positions(item[0])
        require(set(points)=={(west,0.,-8.),(east,0.,-8.),(east,0.,8.),(west,0.,8.)},
                'Road/pavement band bounds or ground height changed')
        require(item[3]['textures']==[texture],'Road/pavement surface uses an unaudited material')
        for offset in range(0,len(item[0]['data']),item[0]['stride']):
            x,h,z,u,v=struct.unpack_from('<5f',item[0]['data'],offset)
            require(abs(u-(x+8.)/16.)<2e-6 and abs(v-(z+8.)/16.)<2e-6,
                    'Road/pavement texture mapping changed native lane scale or alignment')
        triangles=[]
        for kind,start,count in item[2]:
            require(kind==0 and count%3==0,'Ground surface is not a triangle list')
            for offset in range(start,start+count,3):
                triangles.append(tuple(points[i] for i in item[1]['values'][offset:offset+3]))
        area=sum(abs((b[0]-a[0])*(c[2]-a[2])-(b[2]-a[2])*(c[0]-a[0]))/2
                 for a,b,c in triangles)
        require(len(triangles)==2 and abs(area-16.*(east-west))<1e-6,
                'Ground surface is missing or duplicates a pavement face')
        shared=set(triangles[0])&set(triangles[1])
        require(len(shared)==2 and len(set(triangles[0])|set(triangles[1]))==4,
                'Ground triangles do not cover all four band corners')
        a,b=sorted(shared)
        require(a[0]!=b[0] and a[2]!=b[2],
                'Ground triangles overlap instead of meeting at their diagonal')
    for transport,_,_,points in EXPECTED:
        if transport!=2:continue
        require(all(5.<=abs(point[0])<=8. and point[2]==0. for point in points),
                'Native pedestrian route leaves its explicit pavement band')
    clearance=[]
    for item,expected in zip(items[4:],(((-7.9,-7.4),(0.,13.5),(-.65,.65)),
                                      ((7.4,7.9),(0.,13.5),(-.65,.65)),
                                      ((-7.9,7.9),(13.5,14.01067066192627),(-.65,.65)))):
        p=positions(item[0]); limits=[(min(q[a] for q in p),max(q[a] for q in p)) for a in range(3)]
        require(all(abs(actual-wanted)<2e-6 for pair,goal in zip(limits,expected) for actual,wanted in zip(pair,goal)),'Support bounds or deck contact changed')
        # Bounds alone do not establish the support: inspect all saved faces,
        # surface areas, and manifold edge multiplicity of the full solid.
        triangles=[]
        for kind,start,count in item[2]:
            require(kind==0 and count%3==0,'Support is not a triangle list')
            for offset in range(start,start+count,3):
                triangles.append(tuple(p[i] for i in item[1]['values'][offset:offset+3]))
        require(len(p)==8 and len(triangles)==12,'Support must retain the entire closed box geometry')
        faces=Counter();edges=Counter()
        for tri in triangles:
            planes=[(axis,side) for axis in range(3) for side in range(2) if all(abs(q[axis]-limits[axis][side])<2e-6 for q in tri)]
            require(len(planes)==1,'Support face leaves its audited box plane')
            u=[tri[1][i]-tri[0][i] for i in range(3)];v=[tri[2][i]-tri[0][i] for i in range(3)]
            area=math.sqrt(sum((u[(i+1)%3]*v[(i+2)%3]-u[(i+2)%3]*v[(i+1)%3])**2 for i in range(3)))/2
            require(area>1e-8,'Degenerate support triangle')
            faces[planes[0]]+=area
            for first,second in zip(tri,tri[1:]+tri[:1]):edges[tuple(sorted((first,second)))]+=1
        require(all(count==2 for count in edges.values()),'Support mesh is not closed')
        for axis in range(3):
            other=[i for i in range(3) if i!=axis]
            area=math.prod(limits[i][1]-limits[i][0] for i in other)
            require(all(abs(faces[axis,side]-area)<2e-5 for side in range(2)),'Support is missing or duplicates a solid face')
        # A full-height sweep is checked against the saved solid, including cap.
        for transport,entry,exit_,points in EXPECTED:
            if transport==7:continue
            radius=.9 if transport==2 else 1.5
            height=2.2 if transport==2 else 4.5
            if limits[1][0]>=height:
                clearance.append({'transport':transport,'vertical_clearance_m':limits[1][0]-height})
                continue
            for a,b in zip(points,points[1:]):
                ax,ay=a[:2];bx,by=b[:2]
                if abs(ax-bx)<1e-6:
                    dx=max(limits[0][0]-ax,0.,ax-limits[0][1]);dy=max(limits[2][0]-max(ay,by),min(ay,by)-limits[2][1],0.)
                else:
                    dx=max(limits[0][0]-max(ax,bx),min(ax,bx)-limits[0][1],0.);dy=max(limits[2][0]-ay,ay-limits[2][1],0.)
                margin=math.hypot(dx,dy)-radius
                require(margin>0,'Support intrudes into an audited ground route corridor')
                clearance.append({'transport':transport,'horizontal_margin_m':margin,
                                  'lateral_access':transport==2 and {entry,exit_}!={1,3}})
    for turns in range(4):
        for item in items:
            for x,h,z in positions(item[0]):
                for _ in range(turns):x,z=-z,x
                require(abs(x)<=8.000002 and abs(z)<=8.000002,'Rotated geometry leaves the owned tile')
    props={int(p['id'],16):p['values'] for p in exemplar(resources[*EXEMPLAR,tile])['properties']}
    require(props[0x10]==[11] and props[0x27812823]==[*S3D,*range(tile,tile+5)],'Exemplar zoom references changed')
    textures=sorted({t for material in model['materials'] for t in material['textures']})
    return {'models_checked':6,'exact_native_visible_hsr_mesh':True,'native_road_material_and_uv_range':True,
        'explicit_native_pavement_bands':True,'nonoverlapping_ground_bands':True,'side_pillars':2,
        'ground_route_pier_clearance':True,'proper_rotations_geometry_checked':4,'preview_matches_tiles':True,
        'texture_ids':textures,'support_closed_solid_faces_checked':36,
        'clearance_margins_m':{'minimum_vehicle_horizontal':min(v['horizontal_margin_m'] for v in clearance if v['transport']==1 and 'horizontal_margin_m' in v),
            'minimum_pedestrian_horizontal':min(v['horizontal_margin_m'] for v in clearance if v['transport']==2 and 'horizontal_margin_m' in v),
            'minimum_lateral_pedestrian_horizontal':min(v['horizontal_margin_m'] for v in clearance if v.get('lateral_access')),
            'minimum_cap_vertical':min(v['vertical_clearance_m'] for v in clearance if 'vertical_clearance_m' in v)},
        'audit_envelopes_m':{'pedestrian_width':1.8,'pedestrian_height':2.2,'vehicle_width':3.0,'vehicle_height':4.5},
        'game_collision_envelopes_known':False}


def construction_expectations(spec):
    require(spec['recipe']=='rail_hsr_road_stack','Unknown parallel construction')
    return ['....','.a.<','.^..'],['....','.+.<','.^..'],{'a-monorail:0x02000200road:0x02000200'},150
