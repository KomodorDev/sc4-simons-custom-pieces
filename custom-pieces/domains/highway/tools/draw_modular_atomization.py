#!/usr/bin/env python3
"""Draw the actual saved modular routes, ownership, physical obstacles, and cuts."""
from __future__ import annotations
import argparse
import base64
import hashlib
import html
import json
import math
from io import BytesIO
from pathlib import Path
import sys
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0,SourcePackages(ROOT))
from scp import jsonc
from scp.models import parse_s3d,positions
from scp.preview import font
from scp.verify import parse_paths,strict_dbpf
from scp_highway.modular_assembly_verify import check_owned_cells
from scp_highway.assembly_verify import decode_placed_routes
from scp_hsr_tools.assembly_annotations import colour_assignment_for_sources

SUBJECT='ddrhw-l1-and-l2-diagonal-avenue-modular-diamond'
CUT_PAIRS=(('P01','P02'),('P01','P03'),('P01','P04'),('P01','P05'),
           ('P02','P06'),('P03','P06'),('P04','P07'),('P05','P07'))


def saved_grade_profile(routes, placement):
    """Stitch the actual full ramp, including its stamp-owned middle interval."""
    lower=placement in (1,2);side=1 if lower else -1
    positive_u=placement in (1,4)
    selected=[]
    # In the fixed 0-degree saved layout the measured native side coordinate
    # is v=(north-east+136)/sqrt(2). No candidate writer is imported.
    def q(point):return side*(point[1]-point[0]+136.)/math.sqrt(2.)-8.
    for route in routes:
        if route['transport']!=1 or route['placement'] not in (0,placement):continue
        if route['placement']==0 and max(p[2] for p in route['points'])<6.4:continue
        midpoint=route['points'][len(route['points'])//2]
        if ((midpoint[0]+midpoint[1])>0)!=positive_u:continue
        parts=[]
        for first,last in zip(route['points'],route['points'][1:]):
            a,b=q(first),q(last)
            if max(a,b)<-1e-7:continue
            start,end=first,last
            if a<0:
                fraction=-a/(b-a);start=tuple(first[i]+fraction*(last[i]-first[i]) for i in range(3))
            if b<0:
                fraction=-a/(b-a);end=tuple(first[i]+fraction*(last[i]-first[i]) for i in range(3))
            if math.dist(start[:2],end[:2])<1e-9:continue
            if not parts:parts.append(start)
            parts.append(end)
        if parts:selected.append({**route,'points':parts})
    key=lambda point:tuple(round(v,6) for v in point)
    starts={key(r['points'][0]):i for i,r in enumerate(selected)}
    ends={key(r['points'][-1]) for r in selected}
    initial=list(starts.keys()-ends)
    if len(initial)!=1 or len(starts)!=len(selected):
        raise ValueError('A full saved ramp is not one unambiguous directed car chain')
    index=starts[initial[0]];points=[];seen=set()
    while True:
        if index in seen:raise ValueError('A saved grade contains a route cycle')
        seen.add(index);route=selected[index]
        points.extend(route['points'] if not points else route['points'][1:])
        index=starts.get(key(points[-1]))
        if index is None:break
    if len(seen)!=len(selected):raise ValueError('A full saved ramp contains disconnected car paths')
    reverse=points[0][2]<points[-1][2]
    if reverse:points.reverse()
    run=[0.];grades=[]
    for first,last in zip(points,points[1:]):
        length=math.dist(first[:2],last[:2]);run.append(run[-1]+length)
        grades.append((last[2]-first[2])/length*100.)
    return {'placement':f'P{placement+1:02d}','points_enh_m':points,'run_m':run,
            'source_route_ids':[selected[i]['id'] for i in sorted(seen)],
            'source_placements':sorted({selected[i]['placement'] for i in seen}),
            'length_plan_m':run[-1],'maximum_grade_percent':max(map(abs,grades)),
            'ground_endpoint_grade_percent':grades[-1],
            'physical_mouth_enh_m':points[0],
            'native_outer_edge_distance_m':8.,
            'profile_direction':'Flat native-edge physical mouth to ground; on-ramp traffic travels in reverse.',
            'traffic_direction':'ground to stamp' if reverse else 'stamp to ground'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--build',type=Path,required=True)
    p.add_argument('--destination',type=Path)
    a=p.parse_args()
    dest=a.destination or ROOT/'domains/highway/01_assemblies'/SUBJECT
    scene=jsonc.load(ROOT/'domains/highway/01_assemblies'/SUBJECT/'assembly.jsonc')
    raw=(a.build/'manifest.json').read_bytes();manifest=json.loads(raw)
    pieces={p['id']:p for p in manifest['pieces']}
    owners,_=check_owned_cells(pieces,scene)
    colour_sources=[{'label':f'P{index+1:02d}',
                    'occupied_world_cells':[[16*cell[0],-16*cell[1]] for cell,owner in owners.items() if owner['placement']==index]}
                   for index in range(len(scene['placements']))]
    colour_assignment=colour_assignment_for_sources(colour_sources)
    colours=[colour_assignment['palette'][f'P{index+1:02d}'] for index in range(len(scene['placements']))]
    selected={p['piece_id'] for p in scene['placements']}
    resources={key:strict_dbpf((a.build/piece['asset_file']).read_bytes()) for key,piece in pieces.items() if key in selected}
    routes=decode_placed_routes(owners,resources)
    profiles=[saved_grade_profile(routes,placement) for placement in range(1,5)]
    canvas_height=2400
    image=Image.new('RGB',(2400,canvas_height),'#f7f9fb');d=ImageDraw.Draw(image)
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="{canvas_height}" viewBox="0 0 2400 {canvas_height}"><rect width="2400" height="{canvas_height}" fill="#f7f9fb"/>']
    def text(x,y,value,size=24,fill='#23374d',bold=False):
        d.text((x,y),value,font=font(size,bold),fill=fill)
        svg.append(f'<text x="{x}" y="{y+size}" font-family="sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="{fill}">{html.escape(value)}</text>')
    def line(points,fill,width=2,vector=True):
        d.line(points,fill=fill,width=width)
        if vector:svg.append('<polyline points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+f'" fill="none" stroke="{fill}" stroke-width="{width}"/>')
    def rect(box,fill,outline=None):
        d.rectangle(box,fill=fill,outline=outline)
        x,y,xx,yy=box;svg.append(f'<rect x="{x}" y="{y}" width="{xx-x}" height="{yy-y}" fill="{fill}" stroke="{outline or fill}"/>')
    def point(e,n):return (120+(e+8)*6,1190-(n+152)*6)
    def arrow(x,y,dx,dy,fill):
        length=math.hypot(dx,dy)
        if length<=1e-9:return
        ux,uy=dx/length,dy/length
        line([(x-ux*8+uy*4,y-uy*8-ux*4),(x,y),(x-ux*8-uy*4,y-uy*8+ux*4)],fill,3)
    text(55,28,'Assembly - DD RHW-4 — Modular Diagonal Avenue Diamond',36,bold=True)
    text(55,82,'Component guide | Atomization review | Actual saved routes, physical obstacles, and selected cuts',26)
    text(55,130,'Fixed X/Y tile grid | 1 tile = 16 m | Actual saved DAT/PATH geometry',23)
    pose_by_id={p['instance_id']:p for p in scene['placements']}
    for cell,owner in owners.items():
        # Independent ownership records use source world east/north tile indices.
        idx=owner['placement'];placement=f'P{idx+1:02d}'
        e,n=16*cell[0],-16*cell[1]
        x,y=point(e-8,n+8);xx,yy=point(e+8,n-8)
        col=colours[idx];rgb=tuple(int(col[i:i+2],16) for i in (1,3,5))
        pastel='#'+''.join(f'{round(.18*v+.82*255):02x}' for v in rgb)
        rect((x,y,xx,yy),pastel)
        text(x+4,y+4,placement,18,col)
    for i in range(11):
        e=-8+16*i;line([point(e,-152),point(e,8)],'#bcc9d5')
        n=-152+16*i;line([point(-8,n),point(152,n)],'#bcc9d5')
    for cell,owner in owners.items():
        e,n=16*cell[0],-16*cell[1]
        for neighbour,edge in (((cell[0]-1,cell[1]),((e-8,n-8),(e-8,n+8))),
                               ((cell[0]+1,cell[1]),((e+8,n-8),(e+8,n+8))),
                               ((cell[0],cell[1]-1),((e-8,n+8),(e+8,n+8))),
                               ((cell[0],cell[1]+1),((e-8,n-8),(e+8,n-8)))):
            if neighbour not in owners or owners[neighbour]['placement']!=owner['placement']:
                line([point(*q) for q in edge],'#314559',3)
    for i in range(10):
        x,y=point(16*i,-152);text(x-8,y+15,str(i),22)
        x,y=point(-8,-144+16*i);text(x-35,y-12,str(i),22)
    text(560,1260,'X (east) — tile centres, 16 m per tile',24)
    text(55,190,'Y',23);line([(75,275),(75,225)],'#23374d',3);arrow(75,225,0,-1,'#23374d');text(61,280,'N',22,bold=True)
    obstacles=[]
    physical_image=Image.new('RGBA',image.size,(0,0,0,0));physical_draw=ImageDraw.Draw(physical_image)
    # Outline the saved indexed structural model groups. This is a plan projection,
    # not an inferred load-capacity claim or an occlusion rendering.
    for cell,owner in owners.items():
        piece=pieces[owner['piece_id']];local=owner['local_cell']
        tile=int(piece['tile_ids'][piece['cells'].index(list(local))],16)
        model=parse_s3d(resources[piece['id']][0x5ad0e817,0xbadb57f1,tile])
        for mesh in model['meshes']:
            name=mesh['name'].rstrip(b'\0').decode('ascii','replace')
            material=model['materials'][mesh['frames'][0][3]]
            structural=bool(set(material['textures']) & {0x5eb4bee9,0x5eb4beee}) or any(token in name.lower() for token in ('barrier','pier','pillar','column','support','substructure'))
            pavement=bool(set(material['textures']) & {0x5713000e,0x5712000e,0x0400020e,0x0400380e})
            if not structural and not pavement:continue
            # Independent position decode, with indexed faces retained below.
            vertices=positions(model['vertices'][mesh['frames'][0][0]])
            indices=model['indices'][mesh['frames'][0][1]]['values']
            projected=[]
            for kind,start,count in model['primitives'][mesh['frames'][0][2]]:
                if kind!=0 or count%3:raise ValueError('Physical projection requires indexed triangle primitives')
                for j in range(start,start+count,3):
                    tri=[vertices[k] for k in indices[j:j+3]]
                    xy=[point(v[0]+16*cell[0],-v[2]-16*cell[1]) for v in tri]
                    colour='#abb3bd' if structural else '#dce1e7'
                    line(xy+[xy[0]],colour,1,vector=False);physical_draw.line(xy+[xy[0]],fill=colour,width=1)
                    projected.append([[v[0]+16*cell[0],-v[2]-16*cell[1],v[1]] for v in tri])
            obstacles.append({'placement':owner['placement'],'cell':list(cell),'mesh':name,
                'classification':'structural/concrete obstacle' if structural else 'pavement footprint',
                'indexed_triangle_count':len(projected),
                'triangles_enh_sha256':hashlib.sha256(json.dumps(projected,separators=(',',':')).encode()).hexdigest()})
    physical_png=BytesIO();physical_image.save(physical_png,format='PNG')
    svg.append(f'<image x="0" y="0" width="2400" height="{canvas_height}" href="data:image/png;base64,'+base64.b64encode(physical_png.getvalue()).decode('ascii')+'"/>')
    for route in routes:
        heights=[p[2] for p in route['points']]
        upper=route['placement'] in (3,4) or (route['placement']==0 and max(heights)>8)
        colour=('#54834d' if route['transport']==2 else '#c66c27' if upper else '#1978ac' if route['placement'] in (1,2) or max(heights)>.001 else '#52616d')
        projected=[point(*q[:2]) for q in route['points']]
        line(projected,colour,2 if upper or route['transport']==2 else 4)
        lengths=[math.dist(x,y) for x,y in zip(projected,projected[1:])]
        station=sum(lengths)*.6
        if sum(lengths)>=30:
            for first,last,length in zip(projected,projected[1:],lengths):
                if station<=length:
                    fraction=station/length
                    arrow(first[0]+fraction*(last[0]-first[0]),first[1]+fraction*(last[1]-first[1]),last[0]-first[0],last[1]-first[1],colour);break
                station-=length
    # A cut is an actual directed car seam between independently placed parts.
    endpoints={}
    for route in routes:
        if route['transport']!=1:continue
        for side,q in (('in',route['points'][0]),('out',route['points'][-1])):
            k=tuple(round(v,6) for v in q);endpoints.setdefault(k,[]).append((f"P{route['placement']+1:02d}",side))
    cuts=[]
    for index,pair in enumerate(CUT_PAIRS,1):
        selected=[(q,ends) for q,ends in endpoints.items() if set(pair)=={row[0] for row in ends}]
        expected=3 if index in (1,2) else 1
        if len(selected)!=expected:raise ValueError(f'Expected {expected} directed saved car seams for {pair}')
        for q,ends in sorted(selected,key=lambda item:(-item[0][2],item[0][0],item[0][1])):
            cuts.append({'id':f'T{len(cuts)+1}','position_enh_m':list(q),'placements':list(pair),
                         'display_XY_tiles':[q[0]/16,q[1]/16+9],
                         'decision':'Retained city-tile traffic boundary',
                         'implementation':'Full ramp and stamp share no PATH tile' if index<=4 else 'Flat R40 grade/terminal traffic port'})
    mouths=[{'id':f'H{index+1}','position_enh_m':profile['physical_mouth_enh_m'],
             'display_XY_tiles':[profile['physical_mouth_enh_m'][0]/16,profile['physical_mouth_enh_m'][1]/16+9],
             'placements':['P01',profile['placement']],
             'decision':'Move all curved roadway into the separate full ramp',
             'implementation':'Flat physical opening at native outer deck edge; complete profiles checked separately'}
            for index,profile in enumerate(profiles)]
    used_labels=[]
    marker_positions=[point(*record['position_enh_m'][:2]) for record in cuts+mouths]
    for record in cuts+mouths:
        label=record['id'];x,y=point(*record['position_enh_m'][:2]);physical=label.startswith('H')
        colour='#7d278f' if physical else '#9d2544';radius=8 if physical else 6
        d.ellipse((x-radius,y-radius,x+radius,y+radius),fill='white',outline=colour,width=3)
        svg.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="white" stroke="{colour}" stroke-width="3"/>')
        width=d.textbbox((0,0),label,font=font(21,True))[2]+8
        candidates=[]
        for dx,dy in ((16,-31),(16,13),(-width-15,-31),(-width-15,13),(25,-58),(-width-25,43),(42,28),(-width-42,-58)):
            box=(x+dx,y+dy,x+dx+width,y+dy+29)
            overlap=any(not(box[2]+5<a or c+5<box[0] or box[3]+5<b or e+5<box[1]) for a,b,c,e in used_labels)
            hidden=any(box[0]-8<xx<box[2]+8 and box[1]-8<yy<box[3]+8 for xx,yy in marker_positions)
            if not overlap and not hidden and 110<box[0]<box[2]<1110 and 195<box[1]<box[3]<1235:candidates.append(box)
        if not candidates:raise ValueError('Traffic/physical cut labels need a reviewed nonoverlapping layout')
        box=candidates[0];used_labels.append(box);rect(box,'#ffffff')
        line([(x,y),((box[0]+box[2])/2,(box[1]+box[3])/2)],colour,1)
        text(box[0]+4,box[1],label,21,colour,True)
        record['label_box_pixels']=list(box)
    text(1170,160,'Selected split: seven independent clicks',29,bold=True)
    for idx,p in enumerate(scene['placements']):
        text(1170,215+idx*42,p['instance_id']+'  '+p['menu_name'],23,colours[idx])
    text(1170,535,'H: physical mouth. T: city-tile traffic cut.',25,bold=True)
    text(1170,576,'Grey outlines: indexed pavement, barriers, concrete, and supports.',22)
    text(1170,614,'Dark borders and coloured fills: exclusive tile ownership.',22)
    text(1170,652,'Blue: lower roads. Orange: upper roads.',22)
    text(1170,690,'Grey: ground roads. Green: pedestrian paths.',22)
    text(1170,742,'Candidate decisions',26,bold=True)
    decisions=[
      'Retain: straight decks, inside slip lanes, and cutouts.',
      'Move: every curved slab, underside, barrier, and bridge.',
      'Model overhang shares no construction or PATH tile.',
      'Physical mouths: flat at 7.5 m / 15 m; distinct from T cuts.',
      'PATH kinks: lower 1.735 m / upper 3.500 m; new circles R40.',
      'Obstacle: complete Jersey profiles and real supports.',
      'Unverified: universal graded / FLEX building blocks.',
    ]
    for i,value in enumerate(decisions):text(1170,790+i*38,value,22)
    text(1170,1060,'H mouths: X, Y tiles; flat pavement height',23,bold=True)
    for i,mouth in enumerate(mouths):
        x,y=mouth['display_XY_tiles'];z=mouth['position_enh_m'][2]
        text(1170+(i//2)*570,1102+(i%2)*35,f'{mouth["id"]}  ({x:.3f}, {y:.3f})  h {z:.3f} m',21,'#7d278f')
    text(1170,1205,'T traffic cuts: X, Y tiles; actual PATH height',23,bold=True)
    for i,cut in enumerate(cuts):
        x,y=cut['display_XY_tiles'];z=cut['position_enh_m'][2]
        text(1170+(i//6)*570,1250+(i%6)*31,f'{cut["id"]}  ({x:.3f}, {y:.3f})  h {z:.3f} m',21,'#9d2544')
    text(60,1460,'Straight highway stamp: 21 owned tiles. Full R40 attachments: 41. Complete reference: 62 unique construction tiles.',24)
    text(60,1504,'Each lower ramp has 4 traffic ports and 2 intrinsic fragments joined through a stamp-owned middle tile.',24)
    text(60,1548,'The complete visible curved ramps belong to separate pieces; their models deliberately overhang highway-owned tiles.',23)
    profile_run_max=math.ceil(max(profile['length_plan_m'] for profile in profiles)/8)*8
    for number,profile in enumerate(profiles):
        left=100+(number%2)*1180;top=1620+(number//2)*320
        title=('Lower' if number<2 else 'Upper')+(' exit' if number%2==0 else ' entry')
        direction='traffic stamp → ground' if number%2==0 else 'traffic ground → stamp'
        text(left,top,f'{profile["placement"]} — {title}; {direction}',26,bold=True)
        def project(run,height):return left+60+run/profile_run_max*950,top+230-height/15*165
        for height in (0,7.5,15):
            first,last=project(0,height),project(profile_run_max,height);line([first,last],'#d4dce4')
            text(first[0]-55,first[1]-12,f'{height:g}',18)
        for run in range(0,profile_run_max+1,8):
            first,last=project(run,0),project(run,15);line([first,last],'#d4dce4')
            text(first[0]-8,first[1]+6,str(run),18)
        profile_points=[project(run,q[2]) for run,q in zip(profile['run_m'],profile['points_enh_m'])]
        colour='#1978ac' if number<2 else '#c66c27';line(profile_points,colour,4)
        for idx,label in ((0,f'H{number+1}'),(-1,f'T{number+9}')):
            x,y=profile_points[idx];d.ellipse((x-5,y-5,x+5,y+5),fill='white',outline='#9d2544',width=2)
            svg.append(f'<circle cx="{x}" cy="{y}" r="5" fill="white" stroke="#9d2544" stroke-width="2"/>')
            text(x+8,y-28,label,20,'#9d2544')
        middle=len(profile_points)//2;first,last=profile_points[middle:middle+2];sign=1 if number%2==0 else -1
        arrow(last[0],last[1],sign*(last[0]-first[0]),sign*(last[1]-first[1]),colour)
        text(left,top+270,f'Actual run {profile["length_plan_m"]:.3f} m; peak grade {profile["maximum_grade_percent"]:.3f}%; ground join 0%.',22)
    text(100,2340,'Profiles: run from physical H mouth (m), height above pavement datum (m); horizontal and vertical scales are independent.',22)
    svg.append('</svg>');(dest/'previews').mkdir(parents=True,exist_ok=True);(dest/'evidence').mkdir(parents=True,exist_ok=True)
    image.save(dest/'previews/modular-atomization.png');(dest/'previews/modular-atomization.svg').write_text('\n'.join(svg))
    evidence={'schema_version':2,'subject_id':SUBJECT,'source_manifest_sha256':hashlib.sha256(raw).hexdigest(),'scene_sha256':hashlib.sha256((ROOT/'domains/highway/01_assemblies'/SUBJECT/'assembly.jsonc').read_bytes()).hexdigest(),'source_dat_sha256':{key:hashlib.sha256((a.build/piece['asset_file']).read_bytes()).hexdigest() for key,piece in pieces.items() if key in {p['piece_id'] for p in scene['placements']}},'coordinates':'Absolute saved assembly east,north,height in metres; displayed X=east/16,Y=north/16+9.','actual_saved_routes':routes,'physical_obstacle_projections':obstacles,'candidate_cut_decisions':cuts,'physical_mouth_decisions':mouths,'actual_saved_grade_profiles':profiles,'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'plan_scale_pixels_per_metre':[6,6],'profile_scales':f'{profile_run_max}m horizontal,15m vertical, explicitly independent','svg_editing_scope':'Vector ownership, routes, labels, cut markers, and profiles; saved indexed-face projection is an embedded transparent PNG generated by this script.','outputs':{'png_sha256':hashlib.sha256((dest/'previews/modular-atomization.png').read_bytes()).hexdigest(),'svg_sha256':hashlib.sha256((dest/'previews/modular-atomization.svg').read_bytes()).hexdigest(),'image_size_px':[2400,canvas_height]},'interpretation':'One completely straight highway stamp, four separately attached complete visual ramps, and two Avenue terminals. Construction ownership, saved traffic cuts, flat physical mouths, and model overhang are distinct.','manual_game_results_changed':False}
    evidence['colour_assignment']=colour_assignment
    evidence['owned_cell_counts']={f'P{i+1:02d}':sum(owner['placement']==i for owner in owners.values()) for i in range(len(scene['placements']))}
    evidence['native_highway_edge_frame']={'u':'(east+north)/sqrt(2)','v':'(north-east+136)/sqrt(2)','physical_mouth_abs_v_m':8.}
    evidence['physical_mouth_marker_basis']='Actual saved traffic-centreline intersection with the measured native outer-edge plane; complete pavement and barrier openings are represented by the indexed model faces and verified separately.'
    (dest/'evidence/modular-atomization.json').write_text(json.dumps(evidence,indent=2)+'\n')
    print(json.dumps({'routes':len(routes),'traffic_cuts':len(cuts),'physical_mouths':len(mouths),'grade_profiles':len(profiles),'physical_mesh_groups':len(obstacles),'destination':dest.relative_to(ROOT).as_posix()},indent=2))


if __name__=='__main__':main()
