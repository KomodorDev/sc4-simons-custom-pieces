#!/usr/bin/env python3
"""Draw an analysis-only finer partition of the unchanged saved DD diamond.

No game recipe, identifier, construction rule, observation, or assembly pose is
written. All road lines and physical outlines come from the pinned saved DATs.
"""
from __future__ import annotations

import argparse
import base64
from collections import Counter, defaultdict
import hashlib
import html
from io import BytesIO
import json
import math
from pathlib import Path
import struct
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.models import parse_s3d, positions
from scp.preview import font
from scp.verify import strict_dbpf
from scp_highway.assembly_verify import decode_placed_routes
from scp_highway.modular_assembly_verify import check_owned_cells

SUBJECT = 'ddrhw-l1-and-l2-diagonal-avenue-modular-diamond'
MANIFEST_SHA = '8daecd166f6acc19c981f3654be9c0ece4b9005be3c29acb5746c7bdc1d8e8e1'
SOURCE_REVISION = '9d4c94c'
S3D = (0x5AD0E817, 0xBADB57F1)
PATH = (0x296678F7, 0xA966883F)
COLOURS = {'C': '#316ea3', 'A1': '#46886a', 'A2': '#46886a',
           'H1': '#6b7f94', 'H2': '#6b7f94', 'H3': '#8a7462', 'H4': '#8a7462',
           'S1': '#7650aa', 'S2': '#7650aa', 'S3': '#aa527f', 'S4': '#aa527f',
           'P02': '#2583a2', 'P03': '#2583a2', 'P04a': '#bb772c', 'P05a': '#bb772c',
           'P04b': '#b68b10', 'P05b': '#b68b10', 'P06': '#59834b', 'P07': '#59834b'}

# Literal reviewed source grid: columns east, rows south; each cell is 16 m.
STAMP_PARTS = {
    'C': ((0, 0), (1, 0), (0, 1)),
    'A1': ((0, -1),), 'A2': ((-1, 0),),
    'H1': ((-1, 1),), 'H2': ((1, -1),),
    'H3': ((-1, 2),), 'H4': ((2, -1),),
    'S1': ((2, -2), (3, -3), (3, -2)),
    'S2': ((-2, 2), (-3, 3), (-2, 3)),
    'S3': ((-4, 4), (-3, 4), (-4, 5)),
    'S4': ((4, -4), (5, -4), (4, -3)),
}
LANDINGS = {
    'P04b': {'old_placement': 3, 'source_cell': (1, 3), 'axis': 0,
             'high': (8., -51.768542495, 3.060945143),
             'ground': (24., -51.768542495, 0.),
             'pier_centre_en': (10., -51.76854249492381),
             'seam_centre': (-5.423929627, -51.768542495, 6.796391707),
             'direction': 'Exit traffic: high end to ground (east).'},
    'P05b': {'old_placement': 4, 'source_cell': (3, 1), 'axis': 1,
             'high': (51.768542495, -8., 3.060945143),
             'ground': (51.768542495, -24., 0.),
             'pier_centre_en': (51.76854249492381, -10.),
             'seam_centre': (51.768542495, 5.423929627, 6.796391707),
             'direction': 'Entry traffic: ground to high end (north).'},
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def stable(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


class Canvas:
    def __init__(self):
        self.image = Image.new('RGB', (3100, 2900), '#f7f9fb')
        self.draw = ImageDraw.Draw(self.image)
        self.svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="3100" height="2900" viewBox="0 0 3100 2900">',
                    '<rect width="3100" height="2900" fill="#f7f9fb"/>']

    def text(self, x, y, value, size=25, colour='#25384b', bold=False):
        self.draw.text((x, y), value, font=font(size, bold), fill=colour)
        self.svg.append(f'<text x="{x}" y="{y + size}" font-family="sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="{colour}">{html.escape(value)}</text>')

    def line(self, points, colour='#25384b', width=2, dash=False):
        if dash:
            for a, b in zip(points, points[1:]):
                length = math.dist(a, b)
                if length < 1e-9:
                    continue
                for start in range(0, math.ceil(length), 13):
                    aa, bb = start / length, min(start + 8, length) / length
                    self.draw.line([(a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])) for t in (aa, bb)], fill=colour, width=width)
        else:
            self.draw.line(points, fill=colour, width=width)
        extra = ' stroke-dasharray="8 5"' if dash else ''
        self.svg.append('<polyline points="' + ' '.join(f'{x:.3f},{y:.3f}' for x, y in points) + f'" fill="none" stroke="{colour}" stroke-width="{width}"{extra}/>')

    def rect(self, box, colour='white', outline=None, width=1):
        self.draw.rectangle(box, fill=colour, outline=outline, width=width)
        x, y, xx, yy = box
        self.svg.append(f'<rect x="{x}" y="{y}" width="{xx-x}" height="{yy-y}" fill="{colour or "none"}" stroke="{outline or colour or "none"}" stroke-width="{width}"/>')

    def circle(self, point, radius, colour, fill='white', width=2):
        x, y = point
        self.draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=fill, outline=colour, width=width)
        self.svg.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{colour}" stroke-width="{width}"/>')

    def raster(self, picture, at=(0, 0)):
        self.image.paste(picture, at, picture if picture.mode == 'RGBA' else None)
        data = BytesIO(); picture.save(data, format='PNG')
        self.svg.append(f'<image x="{at[0]}" y="{at[1]}" width="{picture.width}" height="{picture.height}" href="data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"/>')

    def arrow(self, a, b, colour, width=3):
        self.line([a, b], colour, width)
        dx, dy = b[0]-a[0], b[1]-a[1]
        length = math.hypot(dx, dy)
        if length:
            ux, uy = dx/length, dy/length
            self.line([(b[0]-ux*10+uy*5, b[1]-uy*10-ux*5), b,
                       (b[0]-ux*10-uy*5, b[1]-uy*10+ux*5)], colour, width)


def actual_triangles(model, source_cell):
    """Decode only referenced first-frame triangle-list indices."""
    result = []
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        vertices = positions(model['vertices'][vi])
        indices = model['indices'][ii]['values']
        name = mesh['name'].rstrip(b'\0').decode('ascii', 'replace')
        textures = model['materials'][mi]['textures']
        for kind, start, count in model['primitives'][pi]:
            if kind != 0 or count % 3:
                raise ValueError('Review requires actual indexed triangle primitives')
            for at in range(start, start + count, 3):
                points = [(vertices[i][0] + 16*source_cell[0],
                           -vertices[i][2] - 16*source_cell[1], vertices[i][1])
                          for i in indices[at:at+3]]
                result.append({'mesh': name, 'textures': textures, 'points': points})
    return result


def saved_inputs(build):
    raw_manifest = (build / 'manifest.json').read_bytes()
    if digest(raw_manifest) != MANIFEST_SHA:
        raise ValueError('This review is pinned to the accepted straight-diamond manifest')
    scene_path = ROOT / 'domains/highway/01_assemblies' / SUBJECT / 'assembly.jsonc'
    scene = jsonc.load(scene_path)
    pieces = {p['id']: p for p in json.loads(raw_manifest)['pieces']}
    owners, _ = check_owned_cells(pieces, scene)
    resources = {p['piece_id']: strict_dbpf((build / pieces[p['piece_id']]['asset_file']).read_bytes())
                 for p in scene['placements']}
    routes = decode_placed_routes(owners, resources)
    cells, provenance = {}, []
    for assembly_cell, owner in sorted(owners.items()):
        source = assembly_cell[0]-4, assembly_cell[1]-4
        raw_model = resources[owner['piece_id']][*S3D, owner['tile']]
        raw_path = resources[owner['piece_id']][*PATH, owner['tile']]
        cells[source] = {'owner': owner, 'triangles': actual_triangles(parse_s3d(raw_model), source)}
        provenance.append({'source_cell': list(source), 'piece_id': owner['piece_id'],
                           'tile_id': f'{owner["tile"]:08x}', 'model_sha256': digest(raw_model),
                           'path_sha256': digest(raw_path)})
    for route in routes:
        route['source_points'] = [(e-64., n+64., h) for e, n, h in route['points']]
        route['source_cell'] = (route['cell'][0]-4, route['cell'][1]-4)
    return scene_path, scene, pieces, owners, resources, routes, cells, provenance


def proposed_owners(cells):
    result = {}
    for label, owned in STAMP_PARTS.items():
        for cell in owned:
            if cell in result:
                raise ValueError('The proposed highway partition duplicates a cell')
            result[cell] = label
    if len(result) != 21 or {c for c, v in cells.items() if v['owner']['placement'] == 0} != set(result):
        raise ValueError('Proposed stamp partition differs from the actual 21 saved cells')
    for cell, record in cells.items():
        if record['owner']['placement'] == 0:
            continue
        index = record['owner']['placement']
        label = f'P{index+1:02d}'
        if index in (3, 4):
            label += 'b' if cell == LANDINGS[label+'b']['source_cell'] else 'a'
        result[cell] = label
    if len(result) != 62 or set(result) != set(cells):
        raise ValueError('The finer partition changes the 62-cell assembly union')
    return result


def support_measurements(cells):
    seeds = [((c, r), (16.*c, -16.*r)) for c, r in
             ((-1,1),(-1,2),(1,-1),(2,-1),(-4,4),(4,-4))]
    seeds += [((0,-2),(6.,35.76854249492381)),
              ((-2,0),(-35.76854249492381,-6.)),
              ((1,3),(10.,-51.76854249492381)),
              ((3,1),(51.76854249492381,-10.))]
    result=[]
    for index,(cell,centre) in enumerate(seeds):
        faces=[tri for tri in cells[cell]['triangles']
               if 'concrete' in tri['mesh'].lower() and
               all(abs(p[0]-centre[0])<=.401 and abs(p[1]-centre[1])<=.401 for p in tri['points'])]
        expected=8 if index<6 else 12
        if len(faces)!=expected:
            raise ValueError(f'Retained support {cell} has {len(faces)} faces, expected {expected}')
        points=[p for tri in faces for p in tri['points']]
        result.append({'source_cell':list(cell),'indexed_triangle_count':len(faces),
                       'triangles_sha256':digest(stable(faces)),
                       'bounds_ENH_m':[[min(p[i] for p in points) for i in range(3)],
                                        [max(p[i] for p in points) for i in range(3)]]})
    return result


def profile_measurements(label, routes, cells):
    declaration = LANDINGS[label]
    matching = [r for r in routes if r['source_cell'] == declaration['source_cell'] and r['transport'] == 1]
    if len(matching) != 1:
        raise ValueError('A landing must retain its one complete saved car PATH')
    route = matching[0]
    points = list(route['source_points'])
    if points[0][2] < points[-1][2]:
        points.reverse()
    runs = [0.]
    for first, last in zip(points, points[1:]):
        runs.append(runs[-1] + math.dist(first[:2], last[:2]))
    grades = [100*(z[2]-a[2])/(runs[i+1]-runs[i]) for i, (a, z) in enumerate(zip(points, points[1:]))]
    if abs(runs[-1]-16.) > 1e-8 or math.dist(points[0], declaration['high']) > 1e-7:
        raise ValueError('Saved landing differs from the independently measured 16 m split')
    triangles = cells[declaration['source_cell']]['triangles']
    cut_value = 8. if declaration['axis'] == 0 else -8.
    section, section_points, pier = [], [], []
    centre = declaration['pier_centre_en']
    for triangle in triangles:
        at_cut = [p for p in triangle['points'] if abs(p[declaration['axis']]-cut_value) < 1e-7]
        if len(at_cut) >= 2:
            ends = max(((a, b) for a in at_cut for b in at_cut), key=lambda pair: math.dist(*pair))
            section.append({'mesh': triangle['mesh'], 'points': ends})
            section_points.extend(at_cut)
        if ('concrete' in triangle['mesh'].lower() and
                all(abs(p[0]-centre[0]) <= .401 and abs(p[1]-centre[1]) <= .401 for p in triangle['points'])):
            pier.append(triangle)
    if len(pier) != 12:
        raise ValueError('The actual isolated landing pier is not twelve indexed triangles')
    pier_points = [p for tri in pier for p in tri['points']]
    transverse = 1-declaration['axis']
    section_width = max(p[transverse] for p in section_points)-min(p[transverse] for p in section_points)
    if abs(section_width-6.) > 1e-5:
        raise ValueError('Landing cut does not contain the complete 6 m outer profile')
    # Optional B: preserve the actual sampled mesh miter, not an invented
    # perpendicular section. Its original vertices occur in the preceding cell.
    preceding_cell = (0, 3) if label == 'P04b' else (3, 0)
    seam = declaration['seam_centre']
    seam_points = {tuple(p) for tri in cells[preceding_cell]['triangles'] if tri['mesh'] == 'SCP NAM ramp'
                   for p in tri['points'] if abs(p[2]-seam[2]) < 1e-6 and math.dist(p[:2], seam[:2]) <= 3.0001}
    low = min(seam_points, key=lambda p: p[transverse]); high = max(seam_points, key=lambda p: p[transverse])
    vector = (high[0]-low[0], high[1]-low[1])
    norm = math.hypot(*vector)
    across = (vector[0]/norm, vector[1]/norm)
    return {'label': label, 'source_cell': list(declaration['source_cell']),
            'display_XY': [declaration['source_cell'][0]+4, 5-declaration['source_cell'][1]],
            'points_source_ENH_m': points, 'run_m': runs, 'point_count': len(points),
            'plan_length_m': runs[-1], 'outward_high_grade_percent': grades[0],
            'outward_ground_grade_percent': grades[-1], 'maximum_grade_percent': max(map(abs, grades)),
            'actual_cut_profile_outer_width_m': section_width,
            'model_pavement_height_m': min(p[2] for p in section_points if p[2] > 3.),
            'model_underside_height_m': min(p[2] for p in section_points),
            'model_barrier_crown_height_m': max(p[2] for p in section_points),
            'section_segments': section,
            'pier': {'indexed_triangle_count': len(pier), 'triangles': pier,
                     'bounds_ENH_m': [[min(p[i] for p in pier_points) for i in range(3)],
                                      [max(p[i] for p in pier_points) for i in range(3)]]},
            'optional_full_straight': {'status': 'conditional model repartition; not implemented',
                'centre_source_ENH_m': list(seam), 'actual_surface_miter_ends_ENH_m': [low, high],
                'actual_surface_miter_width_m': norm, 'unit_across_miter': across,
                'visual_straight_length_m': 29.423929627, 'model_overhang_length_m': 13.423929627,
                'owned_cells': [list(declaration['source_cell'])],
                'overhung_body_cell': list(preceding_cell),
                'preceding_whole_PATH_cell_stays_with_body': True}}


def main_map(canvas, proposed, cells, routes, profiles, supports):
    def point(e, n):
        return 90+(e+72)*8, 1510-(n+88)*8
    for cell, label in proposed.items():
        e, n = 16*cell[0], -16*cell[1]
        x, y = point(e-8, n+8); xx, yy = point(e+8, n-8)
        colour = COLOURS[label]
        rgb = [int(colour[i:i+2], 16) for i in (1, 3, 5)]
        pastel = '#'+''.join(f'{round(.15*v+.85*255):02x}' for v in rgb)
        canvas.rect((x, y, xx, yy), pastel)
    for i in range(11):
        e = -72+16*i; n = -88+16*i
        canvas.line([point(e, -88), point(e, 72)], '#bbc7d3')
        canvas.line([point(-72, n), point(88, n)], '#bbc7d3')
    for cell, label in proposed.items():
        e, n = 16*cell[0], -16*cell[1]
        for neighbour, edge in (((cell[0]-1, cell[1]), ((e-8,n-8),(e-8,n+8))),
                                ((cell[0]+1, cell[1]), ((e+8,n-8),(e+8,n+8))),
                                ((cell[0], cell[1]-1), ((e-8,n+8),(e+8,n+8))),
                                ((cell[0], cell[1]+1), ((e-8,n-8),(e+8,n-8)))):
            if proposed.get(neighbour) != label:
                canvas.line([point(*p) for p in edge], '#3a4653', 3)
    # Raster outlines are the union of actual indexed faces of each owner.
    # The SVG retains editable vector routes, axes, ownership, and labels.
    layer = Image.new('RGBA', canvas.image.size, (0,0,0,0))
    masks = {}; counts = Counter()
    for label in sorted(set(proposed.values())):
        mask = Image.new('L', canvas.image.size, 0); draw = ImageDraw.Draw(mask)
        for cell, assigned in proposed.items():
            if assigned != label:
                continue
            for tri in cells[cell]['triangles']:
                draw.polygon([point(*p[:2]) for p in tri['points']], fill=255)
                counts[label] += 1
        masks[label] = mask
        edge = ImageChops.subtract(mask.filter(ImageFilter.MaxFilter(3)), mask.filter(ImageFilter.MinFilter(3)))
        layer.paste(COLOURS[label], (0,0), edge)
    canvas.raster(layer)
    for route in routes:
        upper=route['placement'] in (3,4) or max(p[2] for p in route['source_points'])>8
        colour = '#56824e' if route['transport'] == 2 else '#c56f2c' if upper else '#237da2' if max(p[2] for p in route['source_points']) > .001 else '#526270'
        pts = [point(*p[:2]) for p in route['source_points']]
        canvas.line(pts, colour, 2 if route['transport'] == 2 else 3)
        lengths = [math.dist(a,b) for a,b in zip(pts, pts[1:])]
        if sum(lengths) > 42:
            distance = sum(lengths)*.58
            for a,b,length in zip(pts,pts[1:],lengths):
                if distance <= length:
                    t=distance/length; end=(a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1]))
                    canvas.arrow((end[0]-(b[0]-a[0])/length*13,end[1]-(b[1]-a[1])/length*13),end,colour,2)
                    break
                distance -= length
    for support in supports:
        low,high=support['bounds_ENH_m']
        x,y=point(low[0],high[1]);xx,yy=point(high[0],low[1])
        canvas.rect((x-2,y-2,xx+2,yy+2),'white')
        canvas.rect((x,y,xx,yy),'#23374d')
    for cell,label in proposed.items():
        e,n=16*cell[0],-16*cell[1];x,y=point(e-8,n+8)
        size=20 if len(label)>3 else 22
        box=canvas.draw.textbbox((0,0),label,font=font(size,True))
        canvas.rect((x+4,y+4,x+box[2]+12,y+32),'#ffffff')
        canvas.text(x+7,y+3,label,size,COLOURS[label],True)
        if cell in ((-3,5),(5,-3)):
            canvas.text(x+7,y+38,'M',20,'#657482',True)
    for label,decl in LANDINGS.items():
        cell=decl['source_cell'];e,n=16*cell[0],-16*cell[1]
        a=point(e-8,n+8);b=point(e+8,n-8)
        canvas.rect((a[0]+2,a[1]+2,b[0]-2,b[1]-2),None, '#b58a08', 6)
        high=decl['high'];axis=1-decl['axis']
        ends=[list(high),list(high)];ends[0][axis]-=3;ends[1][axis]+=3
        canvas.line([point(*q[:2]) for q in ends],'#762e84',6)
        pos=point(*high[:2]);canvas.circle(pos,7,'#762e84',width=3)
        canvas.text(pos[0]+12,pos[1]-28,'K'+label[2],23,'#762e84',True)
        seam=decl['seam_centre'];ends=profiles[label]['optional_full_straight']['actual_surface_miter_ends_ENH_m']
        canvas.line([point(*q[:2]) for q in ends],'#b58a08',4,True)
        pos=point(*seam[:2]);canvas.text(pos[0]+10,pos[1]+(10 if decl['axis'] else -30),'B'+label[2],23,'#8a6909',True)
    for i in range(10):
        x,y=point(16*(i-4),-88);canvas.text(x-9,y+18,str(i),25)
        x,y=point(-72,16*(i-5));canvas.text(x-38,y-17,str(i),25)
    canvas.text(410,1570,'X — east | fixed tile centres | 16 m per tile',27)
    canvas.text(25,250,'Y',27,bold=True);canvas.arrow((38,345),(38,290),'#25384b',3);canvas.text(24,355,'N',23,bold=True)
    return point, counts


def legend(canvas):
    x=1480
    canvas.text(x,235,'Proposed split of the current 21 highway-owned cells',31,bold=True)
    rows=[('C','Mixed crossing: 3 cells, sparse 2×2 owned footprint'),
          ('A1','A1 + A2: two Avenue halves; one future type at 0° / 180°'),
          ('H1','H1 + H2: existing DD highway half A, used twice'),
          ('H3','H3 + H4: existing DD highway half B, used twice'),
          ('S1','S1: lower exit slip lane — 3 contiguous cells'),
          ('S2','S2: lower entry slip lane — 3 contiguous cells'),
          ('S3','S3: upper exit slip lane — 3 contiguous cells'),
          ('S4','S4: upper entry slip lane — 3 contiguous cells')]
    for i,(label,text) in enumerate(rows):
        y=294+i*46;canvas.line([(x,y+16),(x+25,y+16)],COLOURS[label],6);canvas.text(x+40,y,text,26)
    canvas.text(x,684,'3 + 2 + 4 + 12 = 21 cells; every road stays in place.',27,bold=True)
    canvas.text(x,752,'Other parts: retain, or split only the upper landings',30,bold=True)
    rows=[('P02','P02 / P03: current lower full exit / entry ramps, 4 cells each'),
          ('P04a','P04a / P05a: proposed upper curved bodies, 5 cells each'),
          ('P04b','P04b / P05b: proposed straight landings, 1 cell each'),
          ('P06','P06 / P07: current Avenue terminals, 9 / 12 cells')]
    for i,(label,text) in enumerate(rows):
        y=809+i*46;canvas.line([(x,y+16),(x+25,y+16)],COLOURS[label],6);canvas.text(x+40,y,text,26)
    canvas.text(x,1011,'M = retained model-only wing; do not remove its cell.',25)
    canvas.text(x,1060,'Same 62 occupied cells, same 10×10 rectangle.',29,bold=True)
    canvas.text(x,1105,'The fully shown proposal has 19 separate placements.',26)
    canvas.line([(x,1167),(x+48,1167)],'#237da2',4);canvas.text(x+64,1147,'Lower road, 7.5 m; arrows show saved traffic',25)
    canvas.line([(x,1211),(x+48,1211)],'#c56f2c',4);canvas.text(x+64,1191,'Upper road, 15 m; ramps retain their saved heights',25)
    canvas.line([(x,1255),(x+48,1255)],'#526270',4);canvas.text(x+64,1235,'Ground cars; green lines are pedestrian routes',25)
    canvas.text(x,1295,'Dark thick borders = owned tiles. Thin coloured outlines = actual models.',24)
    canvas.text(x,1337,'Black squares = actual piers. Model overhang shares no PATH tile.',25)
    canvas.text(x,1390,'Placement bounds are conditional:',27,bold=True)
    canvas.text(x,1432,'C and the Avenue halves contain only adaptive Avenue cells.',24)
    canvas.text(x,1471,'The writer adds a Road handle at (width,0); the verifier assumes (3,0).',24)
    canvas.text(x,1510,'New widths 2 / 1 need construction changes and game validation.',24)
    canvas.text(x,1549,'Owned minimum ≠ already proven placement bounds.',25,bold=True)


def landing_panel(canvas, label, profile, cells, routes, point, x, y):
    decl=LANDINGS[label];number=label[2]
    canvas.rect((x,y,x+1440,y+1060),'#ffffff','#c4cfd9',2)
    canvas.text(x+24,y+20,f'P0{number}: upper {"exit" if number=="4" else "entry"} — review two possible cuts',30,bold=True)
    canvas.text(x+24,y+69,'A / K'+number+': whole-cell split. B'+number+': optional full visual straight, with model overhang.',24)
    canvas.text(x+24,y+109,'Both options retain all road positions, complete profiles, and the existing pier.',24)
    # A magnified crop retains the actual main drawing and equal X/Y scale.
    e,n=16*decl['source_cell'][0],-16*decl['source_cell'][1]
    left,top=point(e-24,n+24);right,bottom=point(e+24,n-24)
    crop=canvas.image.crop((round(left),round(top),round(right),round(bottom)))
    crop=crop.resize((540,540),Image.Resampling.LANCZOS)
    canvas.raster(crop,(x+28,y+163))
    for delta in (-1,0,1):
        canvas.text(x+28+(delta+1.5)*180-6,y+706,str(decl['source_cell'][0]+4+delta),18)
        canvas.text(x+5,y+163+(1.5-delta)*180-10,str(5-decl['source_cell'][1]+delta),18)
    canvas.text(x+28,y+739,'3×3 tiles; same fixed X/Y grid and north.',22)
    canvas.text(x+28,y+776,'Gold border: one owned landing tile.',23)
    canvas.text(x+28,y+813,'K'+number+': full-width city-tile cut.',23, '#762e84',True)
    canvas.text(x+28,y+850,'B'+number+': actual sampled miter seam.',23,'#8a6909',True)
    pier=profile['pier'];centre=decl['pier_centre_en'];px,py=point(*centre)
    px=x+28+(px-left)*540/(right-left);py=y+163+(py-top)*540/(bottom-top)
    canvas.rect((px-5,py-5,px+5,py+5),'#23374d')
    label_at=(x+330,y+575) if number=='4' else (x+410,y+500)
    canvas.line([(px,py),label_at],'#23374d',2)
    canvas.rect((label_at[0]-4,label_at[1]-6,label_at[0]+43,label_at[1]+25),'white')
    canvas.text(*label_at,'pier',20,'#23374d',True)
    canvas.text(x+28,y+909,'Pier: actual 0.8×0.8 m column',23,bold=True)
    canvas.text(x+28,y+947,'Top corners: 1.393103–1.615717 m.',22)
    canvas.text(x+28,y+986,'Its 12 saved triangles stay with the landing.',22)
    # Side profile: all actual indexed landing faces, not an inferred height box.
    gx,gy=x+662,y+218;gw,gh=695,310
    def side(s,h):return gx+s/16*gw,gy+gh-h/5*gh
    for h in range(6):
        canvas.line([side(0,h),side(16,h)],'#d4dde5');canvas.text(gx-42,side(0,h)[1]-14,str(h),21)
    for s in (0,4,8,12,16):
        canvas.line([side(s,0),side(s,5)],'#e3e8ed');canvas.text(side(s,0)[0]-12,gy+gh+10,str(s),21)
    layer=Image.new('RGBA',canvas.image.size,(0,0,0,0));draw=ImageDraw.Draw(layer)
    for tri in cells[decl['source_cell']]['triangles']:
        projected=[]
        for e,n,h in tri['points']:
            distance=e-8 if decl['axis']==0 else -n-8
            projected.append(side(distance,h))
        draw.polygon(projected,fill=(174,186,197,90))
    canvas.raster(layer)
    poly=[side(s,p[2]) for s,p in zip(profile['run_m'],profile['points_source_ENH_m'])]
    canvas.line(poly,'#c56f2c',5)
    a,b=(poly[8],poly[12]) if number=='4' else (poly[-12],poly[-16])
    canvas.arrow(a,b,'#c56f2c',4)
    canvas.text(gx,gy-58,'Actual saved 16 m side profile',26,bold=True)
    canvas.text(gx,gy+gh+49,'Run from high end (m); height axis in metres',22)
    canvas.text(gx,gy+gh+88,decl['direction'],23)
    canvas.text(gx,gy+gh+128,'3.060945 m → 0 m; high grade 27.8268%, ground 0%.',23,bold=True)
    canvas.text(gx,gy+gh+168,'The grade eases to ground; this is not a repeatable slope.',23)
    # Transverse section is a projection of actual saved boundary segments.
    sx,sy=gx+52,y+839;sw,sh=575,145
    transverse=1-decl['axis'];centre_trans=decl['high'][transverse]
    def front(point):return sx+(point[transverse]-centre_trans+3)/6*sw,sy+sh-(point[2]-2)/2.6*sh
    for segment in profile['section_segments']:
        colour='#c56f2c' if segment['mesh']=='SCP NAM ramp' else '#526b83'
        canvas.line([front(p) for p in segment['points']],colour,2)
    canvas.text(gx,y+765,'K'+number+': complete saved pavement / slab / Jersey section',24,bold=True)
    canvas.text(gx,y+803,'6.000 m outer width; slab thickness 1.000 m',23)
    canvas.line([(sx,sy+sh+14),(sx+sw,sy+sh+14)],'#526b83',2)
    canvas.text(gx,y+996,'Heights: underside 2.060945; pavement 3.060945 m;',21)
    canvas.text(gx,y+1026,'barrier crown 4.451570 m.',21)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build',type=Path,required=True)
    parser.add_argument('--destination',type=Path)
    args=parser.parse_args()
    build=args.build.resolve()
    dest=args.destination or ROOT/'domains/highway/01_assemblies'/SUBJECT
    scene_path,scene,pieces,owners,resources,routes,cells,source_records=saved_inputs(build)
    proposed=proposed_owners(cells)
    profiles={label:profile_measurements(label,routes,cells) for label in LANDINGS}
    supports=support_measurements(cells)
    canvas=Canvas()
    canvas.text(65,30,'Assembly - DD RHW-4 — Modular Diagonal Avenue Diamond',43,bold=True)
    canvas.text(65,92,'Component guide | Further atomization proposal | Top view | North up | Existing geometry unchanged',29)
    canvas.text(65,144,'Actual saved S3D + PATH | 1 tile = 16 m | Fixed X/Y grid | Draft labels identify proposed owners, not existing game buttons',25)
    point,counts=main_map(canvas,proposed,cells,routes,profiles,supports)
    legend(canvas)
    landing_panel(canvas,'P04b',profiles['P04b'],cells,routes,point,60,1650)
    landing_panel(canvas,'P05b',profiles['P05b'],cells,routes,point,1600,1650)
    canvas.text(70,2745,'Option B: all 29.423930 m of visual straight can belong to the landing; it still owns only the final one-cell plot.',27,bold=True)
    canvas.text(70,2790,'The first 13.423930 m overhang the curve-body tile, whose complete PATH stays with that body. Preserve the actual 0.088128° miter; audit the new split.',25)
    canvas.text(70,2834,'Software analysis only. The minimum adaptive core, Avenue half, helper placement, new interfaces, and optional model repartition are proposals.',24)
    previews=dest/'previews';evidence=dest/'evidence';previews.mkdir(parents=True,exist_ok=True);evidence.mkdir(parents=True,exist_ok=True)
    png=previews/'further-atomization-review.png';svg=previews/'further-atomization-review.svg'
    canvas.image.save(png);svg.write_text('\n'.join(canvas.svg+['</svg>'])+'\n')
    partition=[]
    for label in sorted(set(proposed.values())):
        owned=[c for c,v in proposed.items() if v==label]
        partition.append({'label':label,'source_cells':[list(c) for c in sorted(owned)],
                          'display_XY':[[c[0]+4,5-c[1]] for c in sorted(owned)],
                          'owned_cell_count':len(owned),'actual_indexed_model_triangles':counts[label]})
    public_profiles={label:{k:v for k,v in profile.items() if k!='section_segments'} for label,profile in profiles.items()}
    for profile in public_profiles.values():
        profile['section_segments_sha256']=digest(stable(profiles[profile['label']]['section_segments']))
        profile['pier']['triangles_sha256']=digest(stable(profile['pier'].pop('triangles')))
    report={'schema_version':1,'purpose':'Analysis-only finer atomization of the unchanged accepted saved diamond; no new game implementation.',
            'source_revision':SOURCE_REVISION,'source_manifest_sha256':MANIFEST_SHA,
            'source_scene_sha256':digest(scene_path.read_bytes()),
            'source_dat_sha256':{p['piece_id']:digest((build/pieces[p['piece_id']]['asset_file']).read_bytes()) for p in scene['placements']},
            'source_saved_cells':source_records,'source_saved_route_count':len(routes),
            'source_saved_routes_sha256':digest(stable(routes)),
            'generator_sha256':digest(Path(__file__).read_bytes()),
            'coordinate_contract':{'tile_size_m':16,'rectangle_tiles':[10,10],
                'source_grid':'Columns east, rows south; source east=16*column,north=−16*row.',
                'display_grid':'X=source column+4;Y=5−source row. Labels mark tile centres.',
                'equal_XY_scale':True,'main_map_pixels_per_m':8},
            'proposal':{'implemented':False,'occupied_cell_union_equals_saved_assembly':True,
                'occupied_cells':62,'placements_if_all_shown_splits_are_adopted':19,
                'former_stamp_cells':21,'former_stamp_proposed_placements':11,
                'parts':partition,'minimum_core':{'owned_cells':3,'owned_footprint_tiles':[2,2],
                    'car_fragments':20,'pedestrian_fragments':4,'central_piers':0,
                    'native_model_overhang_beyond_owned_bounding_rectangle_m':1.656854629516602,
                    'actual_placement_bounds_verified':False},
                'adaptive_construction_caveat':{'all_adaptive_types':['C','Avenue-half'],
                    'current_writer_handle':'(footprint width,0)',
                    'current_verifier_handle':'(3,0)',
                    'proposed_widths':[2,1],
                    'requires_construction_update_and_game_validation':True},
                'retained_model_only_wing_cells':[[-3,5],[5,-3]],
                'no_shared_construction_or_PATH_cell':True},
            'landings':public_profiles,'actual_physical_supports':supports,
            'rendering':{'canvas_pixels':[3100,2900],
                'road_lines':'Every actual saved route, including both elevated decks, ground cars, pedestrian paths, and traffic arrows.',
                'model_outlines':'Union of actual indexed saved triangle projections per proposed whole-cell owner; not inferred tile rectangles.',
                'svg_editability':'Ownership, routes, grid, labels, dimensions, and profiles are vectors; model outlines and actual indexed profile faces are embedded PNG layers.',
                'profile_axes':'Run 0–16 m; height 0–5 m; separate horizontal and vertical scales.'},
            'outputs':{'png':{'path':str(png.relative_to(dest)),'sha256':digest(png.read_bytes())},
                       'svg':{'path':str(svg.relative_to(dest)),'sha256':digest(svg.read_bytes())}},
            'game_resources_changed':False,'manual_observations_changed':False,'installed':False}
    (evidence/'further-atomization-review.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'saved_routes':len(routes),'proposed_placements':len(partition),
                      'occupied_cells':len(proposed),'source_manifest_sha256':MANIFEST_SHA,
                      'outputs':[str(p.relative_to(dest)) for p in (png,svg)]}))


if __name__=='__main__':
    main()
