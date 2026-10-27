"""Fixed double-track switches, diagonal shifts and native height adapters.

SC4PATH coordinates are (east, north, height), in metres. A cell (x,row)
is centred at (16*x,-16*row). Proper rotations preserve right-hand running;
the second four construction slots are clones rather than reflections.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import math
import struct

from scp.dbpf import require
from scp.track_paths import S3D, PATH, EXEMPLAR, EFFECT, LTEXT, encode_paths
from scp_hsr.track_shapes import _flag, _edge

EPS = 1e-6
RECIPES = (
    'rail_hsr_diagonal_s_left', 'rail_hsr_diagonal_s_right',
    'rail_ghsr_diagonal_s_left', 'rail_ghsr_diagonal_s_right',
    'rail_hsr_adjacent_crossover_right', 'rail_hsr_adjacent_crossover_left',
    'rail_ghsr_adjacent_crossover_right',
    'rail_ghsr_adjacent_crossover_left',
    'rail_hsr_ghsr_transition',
)


def _bezier(control, t):
    u = 1-t
    return tuple(u**3*control[0][a]+3*u*u*t*control[1][a]+
                 3*u*t*t*control[2][a]+t**3*control[3][a] for a in range(2))


class _Centerline(list):
    pass


def _curve(control):
    result=_Centerline(_bezier(control,n/64) for n in range(65))
    result.start_tangent=_unit((control[1][0]-control[0][0],control[1][1]-control[0][1]))
    result.end_tangent=_unit((control[3][0]-control[2][0],control[3][1]-control[2][1]))
    return result


def _unit(vector):
    length = math.hypot(*vector)
    require(length > 1e-10, 'Zero-length rail tangent')
    return tuple(value/length for value in vector)


def _tangents(points):
    result=[_unit((points[min(n+1,len(points)-1)][0]-points[max(0,n-1)][0],
                   points[min(n+1,len(points)-1)][1]-points[max(0,n-1)][1]))
            for n in range(len(points))]
    result[0]=getattr(points,'start_tangent',result[0])
    result[-1]=getattr(points,'end_tangent',result[-1])
    return result


def _clip(points, bounds):
    """Clip an ordered polyline against the declared rectangle, preserving joins."""
    xmin, xmax, ymin, ymax = bounds
    output = []
    for a, b in zip(points, points[1:]):
        low, high = 0., 1.
        for axis, lower, upper in ((0,xmin,xmax),(1,ymin,ymax)):
            delta = b[axis]-a[axis]
            if abs(delta) < 1e-12:
                if not lower-EPS <= a[axis] <= upper+EPS:
                    low, high = 1., 0.; break
            else:
                first, last = sorted(((lower-a[axis])/delta, (upper-a[axis])/delta))
                low, high = max(low,first), min(high,last)
        if high-low > 1e-10:
            for value in (low,high):
                point = tuple(a[i]+value*(b[i]-a[i]) for i in range(len(a)))
                if not output or math.dist(output[-1],point)>1e-8:
                    output.append(point)
    require(len(output)>1, 'Rail curve lies outside its declared footprint')
    return output


def _pair(center, height, bounds, diagonal=False):
    """Offset a physical dual-track centreline into its two directed lanes."""
    tangents = _tangents(center)
    physical_start,physical_end=center[0],center[-1]
    # Extra straight ends allow offset diagonal lanes to meet the SAME native
    # grid edges as their physical centreline, rather than stopping inside it.
    start_tangent, end_tangent = tangents[0], tangents[-1]
    center = [(center[0][0]-20*start_tangent[0],center[0][1]-20*start_tangent[1]),
              *center,(center[-1][0]+20*end_tangent[0],center[-1][1]+20*end_tangent[1])]
    tangents = [start_tangent,*tangents,end_tangent]
    distance = 2.9/math.sqrt(2) if diagonal else 2.
    lanes = []
    for direction in (1,-1):
        points = [(p[0]+direction*distance*t[1],p[1]-direction*distance*t[0],height)
                  for p,t in zip(center,tangents)]
        points = _clip(points,bounds)
        if diagonal and direction == 1:
            # Native 5dd01a00/5dc01a00 have an intentional 2.8 m coordinate on
            # the east port of this half, while the other ports use 2.9 m.
            # Blend that 0.1 m discrepancy through the last 8 m; externals are
            # exactly native, and internal shared endpoints remain identical.
            finish = points[-1]
            points = [(x,y+.1*max(0.,1-math.dist((x,y),finish[:2])/8),z) for x,y,z in points]
        if diagonal:
            # Offset curves cross their end plane slightly beyond the physical
            # centreline's parameter endpoint. Pin those four external ports to
            # the audited native half-diagonal coordinates, not an approximation.
            points[0]=(physical_start[0]+direction*2.9,physical_start[1],height)
            points[-1]=(physical_end[0],physical_end[1]-(2.8 if direction==1 else -2.9),height)
        lanes.append(points if direction == 1 else list(reversed(points)))
    return lanes


def _snap(value):
    boundary = round((value+8)/16)*16-8
    return boundary if abs(value-boundary)<1e-7 else value


def _slice(points):
    """Cut a sampled polyline exactly at every 16 m grid boundary."""
    output = {}
    for a,b in zip(points,points[1:]):
        cuts = [0.,1.]
        for axis in range(2):
            delta = b[axis]-a[axis]
            if abs(delta)<1e-12:
                continue
            lower,upper=sorted((a[axis],b[axis]))
            for n in range(math.floor((lower+8)/16),math.ceil((upper+8)/16)+1):
                value=(16*n-8-a[axis])/delta
                if 1e-10<value<1-1e-10:
                    cuts.append(value)
        cuts=sorted(set(round(value,13) for value in cuts))
        for low,high in zip(cuts,cuts[1:]):
            middle=[a[i]+(low+high)/2*(b[i]-a[i]) for i in range(3)]
            cell=(math.floor((middle[0]+8)/16),math.floor((8-middle[1])/16))
            pair=[(_snap(a[0]+t*(b[0]-a[0])-16*cell[0]),
                   _snap(a[1]+t*(b[1]-a[1])+16*cell[1]),a[2]+t*(b[2]-a[2]))
                  for t in (low,high)]
            if cell not in output:
                output[cell]=[]
            if output[cell] and math.dist(output[cell][-1],pair[0])>EPS:
                raise ValueError('A rail curve re-enters a tile; split its physical route')
            if not output[cell]:
                output[cell].append(pair[0])
            if math.dist(output[cell][-1],pair[1])>1e-8:
                output[cell].append(pair[1])
    return output


def _record(points, role, movement, junction=False):
    tangents=_tangents(points)
    return {'transport':7,'entry':_edge(points[0]),'exit':_edge(points[-1]),
            'points':points,'role':role,'movement':movement,'junction':junction,
            'tangent_in':tangents[0],'tangent_out':tangents[-1]}


def _add_pair(layout, center, height, bounds, movements, *, role='branch', diagonal=False):
    for points,movement in zip(_pair(center,height,bounds,diagonal),movements):
        chunks=_slice(points)
        for index,(cell,part) in enumerate(chunks.items()):
            record=_record(part,role,movement,index==0 and role=='branch')
            if index==0:
                record['tangent_in']=tuple(value*(1 if movement==movements[0] else -1)
                                           for value in _tangents(center)[0 if movement==movements[0] else -1])
            if index==len(chunks)-1:
                record['tangent_out']=tuple(value*(1 if movement==movements[0] else -1)
                                            for value in _tangents(center)[-1 if movement==movements[0] else 0])
            layout.setdefault(cell,{'routes':[],'decks':[]})['routes'].append(record)
    center3=[(*point,height) for point in center]
    physical_chunks=_slice(center3)
    for index,(cell,part) in enumerate(physical_chunks.items()):
        tangents=_tangents(part)
        if index==0:
            tangents[0]=_tangents(center)[0]
        if index==len(physical_chunks)-1:
            tangents[-1]=_tangents(center)[-1]
        layout.setdefault(cell,{'routes':[],'decks':[]})['decks'].append(
            {'points':part,'width':15.,'geometry_id':'/'.join(movements),
             'start_tangent':tangents[0],'end_tangent':tangents[-1]})


def _level(recipe):
    return 1. if recipe.startswith('rail_ghsr_') else 15.5


def _procedural(recipe):
    h=_level(recipe)
    layout={}
    if '_diagonal_s_' in recipe:
        bounds=(-8.,40.,-40.,8.)
        if recipe.endswith('_left'):
            control=[(16.,-40.),(30.,-26.),(26.,-14.),(40.,0.)]
        else:
            control=[(0.,-40.),(14.,-26.),(26.,-30.),(40.,-16.)]
        _add_pair(layout,_curve(control),h,bounds,('S>E','E>S'),role='main',diagonal=True)
    elif '_adjacent_crossover_' in recipe:
        return _adjacent_layout(h, recipe.rsplit('_', 1)[1])
    else:
        raise ValueError(f'No procedural layout for {recipe}')
    return _finalize_layout(layout)


def _adjacent_layout(height, side):
    """Current shared geometry for one transfer hand or a scissors switch."""
    require(side in {'right', 'left', 'both'}, 'Unknown adjacent-switch transfer hand')
    h = height
    layout = {}
    bounds = (-8.,24.,-40.,8.)
    for x,label in ((0.,'A'),(16.,'B')):
        _add_pair(layout,[(x,-40.),(x,8.)],h,bounds,
                  (f'{label}S>{label}N',f'{label}N>{label}S'),role='main')
    if side in ('right', 'both'):
        _add_pair(layout,_curve([(0.,-40.),(0.,-24.),(16.,-8.),(16.,8.)]),h,bounds,
                  ('AS>BN','BN>AS'))
    if side in ('left', 'both'):
        # Stagger the opposing curve so crossings stay inside cells and only
        # encoded train movements connect at cell boundaries.
        _add_pair(layout,_curve([(16.,-40.),(16.,-28.),(0.,-12.),(0.,8.)]),h,bounds,
                  ('BS>AN','AN>BS'))
    return _finalize_layout(layout)


def _finalize_layout(layout):
    # Junction flags belong at every actual boundary where a choice begins,
    # including a shared approach that spans more than one tile.
    for data in layout.values():
        starts=Counter(tuple(round(value,6) for value in route['points'][0]) for route in data['routes'])
        for route in data['routes']:
            if route['role']=='branch' and starts[tuple(round(value,6) for value in route['points'][0])]>1:
                route['junction']=True
    # Stable row-major order matches native AutoTileBase allocation.
    return dict(sorted(layout.items(),key=lambda pair:(pair[0][1],pair[0][0])))


def feature_layout(recipe):
    require(recipe in RECIPES,f'Unknown rail feature recipe: {recipe}')
    if recipe=='rail_hsr_ghsr_transition':
        return {(0,row):{'routes':[],'decks':[],'native_source':0x5DCF1700+row*0x10,
                         'native_rotation':0} for row in range(8)}
    return _procedural(recipe)


def _construction_flags(routes):
    categories=[set() for _ in range(4)]
    for route in routes:
        categories[route['entry']].add(_flag(route['entry'],route['tangent_in']))
        categories[route['exit']].add(_flag(route['exit'],route['tangent_out']))
    # Native same-network intersections use category 2 where a straight and
    # diagonal share an edge. Extend that explicit precedence to a fixed
    # authored edge carrying BOTH diagonal headings; it cannot be represented
    # by arbitrarily retaining the final heading encountered in a loop.
    sides=[2 if len(values)>1 or 2 in values else next(iter(values),0) for values in categories]
    return sides[3]<<24|sides[2]<<16|sides[1]<<8|sides[0]


def _layout_info(layout, height):
    cells = list(layout)
    footprint = (max(cell[0] for cell in cells)+1,max(cell[1] for cell in cells)+1)
    return {'cells':cells,'footprint':footprint,'height':height,
                   'cost':100*len(cells),'construction_flags':{
                       cell: (0x02000200 if data.get('native_rotation')==0 else 0x00020002)
                       if 'native_source' in data else _construction_flags(data['routes'])
                       for cell,data in layout.items()},
                   'effect_donor':((*EFFECT,0x5DDF0100),'preview_hsr_ofillerpiece000',0x5DD31500),
                   'provenance':'NAM 50 right-hand HSR/GHSR ports; authored fixed construction and paths',
                   'native_adapter_cells':{cell:(data['native_source'],data['native_rotation'])
                                           for cell,data in layout.items() if 'native_source' in data}}


INFO = {_recipe: _layout_info(feature_layout(_recipe), _level(_recipe)) for _recipe in RECIPES}


def _ports(recipe):
    height=_level(recipe)
    if recipe=='rail_hsr_ghsr_transition':
        return {'N':{'in':(-2.,8.,15.5),'out':(2.,8.,15.5)},
                'S':{'in':(2.,-120.,1.),'out':(-2.,-120.,1.)}}, [('N','S'),('S','N')]
    if '_diagonal_s_' in recipe:
        start_x,end_y=(16.,0.) if recipe.endswith('_left') else (0.,-16.)
        return {'S':{'in':(start_x+2.9,-40.,height),'out':(start_x-2.9,-40.,height)},
                'E':{'in':(40.,end_y+2.9,height),'out':(40.,end_y-2.8,height)}}, [('S','E'),('E','S')]
    return _adjacent_ports(height, recipe.rsplit('_', 1)[1])


def _adjacent_ports(height, side):
    ports={}
    for x,label in ((0.,'A'),(16.,'B')):
        ports[label+'N']={'in':(x-2.,8.,height),'out':(x+2.,8.,height)}
        ports[label+'S']={'in':(x+2.,-40.,height),'out':(x-2.,-40.,height)}
    movements=[('AS','AN'),('AN','AS'),('BS','BN'),('BN','BS')]
    if side in ('right', 'both'):
        movements += [('AS','BN'),('BN','AS')]
    if side in ('left', 'both'):
        movements += [('BS','AN'),('AN','BS')]
    return ports,movements


for _recipe,_info in INFO.items():
    _info['ports'],_info['movements']=_ports(_recipe)


def _number(value):
    return int(value,16) if isinstance(value,str) else int(value)


def _spec(spec):
    recipe=spec['recipe']
    require(recipe in INFO,'Unknown rail feature recipe')
    info=INFO[recipe]
    cells=[tuple(cell) for cell in spec.get('cells',info['cells'])]
    require(cells==info['cells'] and tuple(spec['footprint'])==info['footprint'],
            'Rail feature footprint/cells differ from the implemented layout')
    tiles=list(map(_number,spec['tile_ids']))
    base=tiles[0]-0x100*cells[0][0]-0x10*cells[0][1]
    require(len(tiles)==len(cells) and tiles==[base+0x100*x+0x10*y for x,y in cells],
            'Rail feature allocation differs from native AutoTileBase grid')
    return recipe,info,dict(zip(cells,tiles))


def build_rules(spec):
    _,info,tiles=_spec(spec)
    return _construction_rules(spec, info, tiles)


def _construction_rules(spec, info, tiles):
    width,depth=info['footprint']
    letters={cell:chr(65+n) for n,cell in enumerate(info['cells'])}
    def grid(construct=False):
        rows=['.'*(width+3)]
        for y in range(depth):
            rows.append('.'+''.join(('+' if construct else letters[(x,y)])
                         if (x,y) in letters else '.' for x in range(width))+'.'+('<' if y==0 else '.'))
        rows.append('.^'+'.'*(width+1))
        return rows
    puzzle,preview=_number(spec['puzzle_id']),_number(spec['preview_id'])
    lines=[f'[HighwayIntersectionInfo_0x{puzzle:08X}]',
           f'Piece = 0.0, 0.0, 0, 0, 0x{preview:08X}',f"PreviewEffect = {spec['effect_name']}",'']
    lines += ['CellLayout = '+row for row in grid()]
    lines += ['']+[f'CheckType = {letters[cell]} - monorail: 0x{info["construction_flags"][cell]:08X}'
                    for cell in info['cells']]
    lines += ['']+['ConsLayout = '+row for row in grid(True)]
    first_x,first_y=info['cells'][0]
    origin_x=min(x for x,y in info['cells'])
    origin_y=min(y for x,y in info['cells'])
    base=next(iter(tiles.values()))-0x100*(first_x-origin_x)-0x10*(first_y-origin_y)
    lines += ['',f'AutoTileBase = 0x{base:08X}','ReplacementIntersection = 0, 0',
              f'PlaceQueryID = 0x{next(iter(tiles.values())):08X}',f'Costs = {info["cost"]}']
    for n in range(1,8):
        lines += ['',f'[HighwayIntersectionInfo_0x{puzzle+n*0x10000:08X}]',
                  f'CopyFrom = 0x{puzzle+(n%4)*0x10000 if n>=4 else puzzle:X}']
        if n<4:
            lines.append(f'Rotate = {n}')
    return '\r\n'.join(lines)+'\r\n'


def _rotate_path(point,turns):
    x,y,z=point
    for _ in range(turns%4):
        x,y=y,-x
    return x,y,z


def native_paths(raw,turns=0):
    from .crossings import _read_paths
    result=[]
    for route in _read_paths(raw)[2]:
        require(route['transport']==7,'Native adapter has a foreign transport')
        points=[_rotate_path(point,turns) for point in route['points']]
        result.append(_record(points,'adapter','adapter'))
    return result


def native_model(raw,turns=0):
    from scp.models import parse_s3d,pack_s3d,valid_frame
    from scp.recipes import combine_meshes
    model=parse_s3d(raw)
    meshes=[mesh for mesh in model['meshes'] if all(valid_frame(model,frame) for frame in mesh['frames'])]
    require(meshes,'Native adapter has no valid model mesh')
    output=combine_meshes([(model,meshes,(0.,0.,0.))])
    for vertices in output['vertices']:
        data=bytearray(vertices['data'])
        for offset in range(0,len(data),vertices['stride']):
            x,height,z=struct.unpack_from('<3f',data,offset)
            for _ in range(turns%4):
                x,z=-z,x
            struct.pack_into('<3f',data,offset,x,height,z)
        vertices['data']=bytes(data)
    return pack_s3d(output)


def build_feature(spec,context):
    if spec['recipe'] == 'rail_hsr_road_stack':
        from .road_stack import build
        return build(spec, context)
    from .rail_geometry import build_tiled_geometry
    from scp.shadows import build_shadows
    from scp.models import parse_s3d,pack_s3d
    from scp.recipes import combine_meshes,effect_clone,label,tile_exemplar
    recipe,info,tiles=_spec(spec)
    layout=feature_layout(recipe)
    hsr=context['hsr']
    assets,parts={},[]
    procedural={cell:data for cell,data in layout.items() if 'native_source' not in data}
    geometry=build_tiled_geometry(hsr[*S3D,0x5DD31500],procedural,
                                  ground=info['height']==1.,supports=info['height']>1.) if procedural else {}
    for cell,tile in tiles.items():
        data=layout[cell]
        if 'native_source' in data:
            source,rotation=data['native_source'],data['native_rotation']
            raw=native_model(hsr[*S3D,source],rotation)
            routes=native_paths(hsr[*PATH,source],rotation)
        else:
            raw=geometry[cell]
            routes=data['routes']
        for zoom in range(5):
            assets[*S3D,tile+zoom]=raw
        assets.update(build_shadows(raw,tile))
        assets[*PATH,tile]=encode_paths(routes)
        assets[*EXEMPLAR,tile]=tile_exemplar(hsr[*EXEMPLAR,0x5DCF0A00],tile,'SCP | '+spec['name'])
        assets[*LTEXT,tile]=label('SCP | '+spec['name']+' (Experimental)')
        model=parse_s3d(raw)
        parts.append((model,model['meshes'],(16.*cell[0],0.,16.*cell[1])))
    preview=_number(spec['preview_id'])
    assets[*S3D,preview]=pack_s3d(combine_meshes(parts))
    donor_tgi,name,model=info['effect_donor']
    assets[*EFFECT,preview]=effect_clone(hsr[donor_tgi],name,spec['effect_name'],model,preview)
    return assets,build_rules(spec)


# The mixed-network module has its own independent geometry and route contract.
from .road_stack import INFO as ROAD_STACK_INFO
INFO['rail_hsr_road_stack'] = ROAD_STACK_INFO
