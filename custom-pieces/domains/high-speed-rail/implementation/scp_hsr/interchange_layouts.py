"""Authored directed rail modules and shared layout helpers.

All points use SC4PATH (east, north, height) metres. Layouts expose actual
directed routes separately from physical decks. Current modular recipes retain
their authored geometry and allocated identifiers.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import math

from scp.dbpf import require
from .rail_features import _slice, _record, _curve, _construction_flags, _snap
from scp_hsr.track_shapes import single_track_layout

LEVELS={'ground':1.,'hsr':15.5,'l3':23.,'l4':30.5}
_DEFINITIONS={}


def _point(point):
    return tuple(round(value,6) for value in point)


def _slices(points):
    """Ordered grid fragments, allowing a complete route to re-enter a cell."""
    output=[]
    for a,b in zip(points,points[1:]):
        cuts=[0.,1.]
        for axis in (0,1):
            delta=b[axis]-a[axis]
            if abs(delta)<1e-12:continue
            low,high=sorted((a[axis],b[axis]))
            for n in range(math.floor((low+8)/16),math.ceil((high+8)/16)+1):
                value=(16*n-8-a[axis])/delta
                if 1e-10<value<1-1e-10:cuts.append(value)
        cuts=sorted(set(round(value,13) for value in cuts))
        for low,high in zip(cuts,cuts[1:]):
            middle=[a[j]+(low+high)/2*(b[j]-a[j]) for j in range(3)]
            cell=math.floor((middle[0]+8)/16),math.floor((8-middle[1])/16)
            pair=[(_snap(a[0]+t*(b[0]-a[0])-16*cell[0]),
                   _snap(a[1]+t*(b[1]-a[1])+16*cell[1]),a[2]+t*(b[2]-a[2])) for t in (low,high)]
            if output and output[-1][0]==cell and math.dist(output[-1][1][-1],pair[0])<1e-7:
                if math.dist(output[-1][1][-1],pair[1])>1e-8:output[-1][1].append(pair[1])
            else:output.append((cell,pair))
    return output


def _add_route(layout,points,movement,*,role='branch',width=7.5,deck=True):
    chunks=_slices(points)
    for cell,part in chunks:
        record=_record(part,role,movement)
        layout.setdefault(cell,{'routes':[],'decks':[]})['routes'].append(record)
    if deck:
        for cell,part in chunks:
            tangents=[(part[1][0]-part[0][0],part[1][1]-part[0][1]),
                      (part[-1][0]-part[-2][0],part[-1][1]-part[-2][1])]
            layout[cell]['decks'].append({'points':part,'width':width,'geometry_id':movement,
                'profile':'blend','safe_supports':True,'start_tangent':tangents[0],
                'end_tangent':tangents[1]})


def _dual_mainline(layout,height,south,north=8.):
    _add_route(layout,[(2.,south,height),(2.,north,height)],'S>N',role='main',deck=False)
    _add_route(layout,[(-2.,north,height),(-2.,south,height)],'N>S',role='main',deck=False)
    for cell,points in _slice([(0.,south,height),(0.,north,height)]).items():
        layout[cell]['decks'].append({'points':points,'width':15.,'geometry_id':'dual_main',
            'profile':'blend','safe_supports':True,'start_tangent':(0.,1.),'end_tangent':(0.,1.)})


def _normalize(layout):
    require(layout,'An interchange layout must contain actual network cells')
    minimum_x=min(cell[0] for cell in layout)
    minimum_row=min(cell[1] for cell in layout)
    output={}
    for (x,row),data in sorted(layout.items(),key=lambda item:(item[0][1],item[0][0])):
        unique={}
        for route in data['routes']:
            identity=tuple(map(_point,route['points']))
            if identity not in unique:
                unique[identity]=route
        data['routes']=list(unique.values())
        starts=Counter(_point(route['points'][0]) for route in data['routes'])
        for route in data['routes']:
            if route['role']!='main' and starts[_point(route['points'][0])]>1:
                route['junction']=True
        output[x-minimum_x,row-minimum_row]=data
    return output,(-16.*minimum_x,16.*minimum_row)


def _filler(definition):
    height=definition['height']
    source=definition['source']
    source_layout=single_track_layout(source)
    output={}
    for cell,data in source_layout.items():
        points=[(x,y,height) for x,y,_ in data['branch']]
        output[cell]={'routes':[_record(points,'branch','IN>OUT')],
            'decks':[{'points':points,'width':7.5,'geometry_id':'single',
                'profile':'blend','safe_supports':True,
                'start_tangent':data['tangent_in'],'end_tangent':data['tangent_out']}]}
    return output


def _turn90(definition):
    height=definition['height']
    side=-1 if definition['hand']=='left' else 1
    size=40. if definition['radius']=='compact' else 88.
    control=[(0.,-size),(0.,-size*.4),(side*size*.4,0.),(side*size,0.)]
    output={}
    _add_route(output,[(*p,height) for p in _curve(control)],'IN>OUT')
    return output


def _split(definition):
    angle,radius=definition['angle'],definition['radius']
    controls={
        (45,'compact'):[(2.,-56.),(2.,-24.),(16.,-24.),(40.,0.)],
        (45,'wide'):[(2.,-104.),(2.,-40.),(40.,-16.),(88.,32.)],
        (90,'compact'):[(2.,-24.),(2.,-8.),(8.,0.),(24.,0.)],
        (90,'wide'):[(2.,-88.),(2.,-32.),(32.,0.),(88.,0.)],
        (135,'compact'):[(2.,-88.),(2.,-8.),(40.,32.),(88.,-16.)],
        (135,'wide'):[(2.,-184.),(2.,-16.),(80.,64.),(184.,-32.)],
    }
    control=deepcopy(controls[angle,radius])
    if definition['level']=='l4':
        control[0]=(0.,control[0][1])
        control[1]=(0.,control[1][1])
    points=[(*p,definition['height']) for p in _curve(control)]
    if definition['mode']=='merge':
        mirror=control[0][1]+8.
        points=[(x,mirror-y,z) for x,y,z in reversed(points)]
    if definition.get('hand')=='left':
        require(definition['level']=='l4','An at-grade left branch cannot cross a dual mainline')
        points=[(-x,y,z) for x,y,z in points]
    output={}
    if definition['level']=='l4':
        _add_route(output,[(0.,control[0][1],definition['height']),(0.,8.,definition['height'])],
                   'S>N',role='main')
    else:
        _dual_mainline(output,definition['height'],control[0][1])
    _add_route(output,points,'S>B' if definition['mode']=='split' else 'B>N')
    return output


def _ease_distance(distance,length,edge=8.):
    """Integral of a trapezoidal grade, with continuous zero endpoint grade."""
    edge=min(edge,length/4)
    if distance<=edge:
        return distance*distance/(2*edge)/(length-edge)
    if distance>=length-edge:
        return 1-(length-distance)**2/(2*edge)/(length-edge)
    return (distance-edge/2)/(length-edge)


def _grade(definition):
    first,last=definition['from_height'],definition['to_height']
    depth=math.ceil((abs(last-first)/.20+48.)/16.)
    south=8.-16.*depth
    total=16.*depth
    points=[]
    for index in range(depth*8+1):
        distance=total*index/(depth*8)
        progress=_ease_distance(max(0.,min(total-32.,distance-16.)),total-32.)
        points.append((0.,south+distance,first+(last-first)*progress))
    output={}
    _add_route(output,points,'IN>OUT')
    return output


def _flyover_crossing(definition):
    # The upper route is a centered one-way L4 track. The lower dual track is
    # deliberately real geometry + two directed PATHs, not a visual marker.
    variant=definition.get('crossing_variant')
    lower=definition['lower_height']
    output={}
    if variant=='ground_single_under_hsr_dual':
        _dual_mainline(output,15.5,-24.,24.)
        _add_route(output,[(-8.,0.,1.),(8.,0.,1.)],'W>E')
        return output
    if variant in ('upper_grid_lower_diag','upper_diag_lower_grid','upper_diag_lower_diag'):
        if 'lower_diag' in variant:
            _add_route(output,[(24.,-13.1,lower),(-13.2,24.,lower)],'E>N',role='main',deck=False)
            _add_route(output,[(-18.9,24.,lower),(24.,-18.9,lower)],'N>E',role='main',deck=False)
            for cell,points in _slice([(24.,-16.,lower),(-16.,24.,lower)]).items():
                output.setdefault(cell,{'routes':[],'decks':[]})['decks'].append({
                    'points':points,'width':15.,'geometry_id':'dual_lower_diagonal','profile':'blend',
                    'safe_supports':True,'start_tangent':(-1.,1.),'end_tangent':(-1.,1.)})
        else:_dual_mainline(output,lower,-24.,24.)
        upper_points=([(-24.,-16.,30.5),(16.,24.,30.5)] if variant.startswith('upper_diag') else
                      [(-24.,0.,30.5),(24.,0.,30.5)])
        _add_route(output,upper_points,'UPPER_IN>UPPER_OUT')
        return output
    _dual_mainline(output,lower,-8.,8.)
    # Three upper cells provide land for columns outside the lower 15 m deck.
    upper=definition.get('upper_height',30.5)
    _add_route(output,[(-24.,0.,upper),(24.,0.,upper)],'W>E')
    return output


_SOURCE_SHAPES={
    'straight':'straight','diagonal':'diagonal',
    'diagonal_north_half':'diagonal_north_half',
    'diagonal_east_half':'diagonal_east_half',
    'curve_out_right':'curve_out_right','curve_out_left':'curve_out_left',
    'curve_in_left':'curve_in_left','curve_in_right':'curve_in_right',
}
for _level in ('ground','l3','l4'):
    for _shape,_source in _SOURCE_SHAPES.items():
        _key=f'interchange_oneway_{_level}_{_shape}'
        _DEFINITIONS[_key]={'kind':'oneway_filler','level':_level,'height':LEVELS[_level],
            'source':_source,'shape':_shape,'radius':'compact','category':'oneway-levels'}
    for _hand in ('left','right'):
        _key=f'interchange_oneway_{_level}_turn90_{_hand}'
        _DEFINITIONS[_key]={'kind':'oneway_turn','level':_level,'height':LEVELS[_level],
            'hand':_hand,'angle':90,'radius':'compact','category':'oneway-levels'}
for _level in ('ground','hsr','l4'):
    for _angle in (45,90,135):
        for _radius in ('compact','wide'):
            for _mode in ('split','merge'):
                _key=f'interchange_{_level}_{_mode}_{_angle}_{_radius}'
                _DEFINITIONS[_key]={'kind':'directed_branch','level':_level,'height':LEVELS[_level],
                    'angle':_angle,'radius':_radius,'mode':_mode,'category':'oneway-branches'}
for _start,_finish in (('ground','hsr'),('hsr','ground'),('hsr','l3'),('l3','hsr'),
                      ('l3','l4'),('l4','l3'),('hsr','l4'),('l4','hsr')):
    _key=f'interchange_oneway_grade_{_start}_to_{_finish}'
    _DEFINITIONS[_key]={'kind':'oneway_grade','from_level':_start,'to_level':_finish,
        'from_height':LEVELS[_start],'to_height':LEVELS[_finish],'category':'oneway-grades'}
for _lower in ('ground','hsr'):
    _key=f'interchange_l4_oneway_over_{_lower}'
    _DEFINITIONS[_key]={'kind':'flyover_crossing','height':30.5,'lower_height':LEVELS[_lower],
        'lower_level':_lower,'category':'true-flyovers'}
# Append new families so provisional allocations for the initial 76 recipes
# do not move when the module grows.
for _shape,_source in _SOURCE_SHAPES.items():
    _key=f'interchange_oneway_hsr_{_shape}'
    _DEFINITIONS[_key]={'kind':'oneway_filler','level':'hsr','height':15.5,
        'source':_source,'shape':_shape,'radius':'compact','category':'oneway-levels'}
for _hand in ('left','right'):
    _key=f'interchange_oneway_hsr_turn90_{_hand}'
    _DEFINITIONS[_key]={'kind':'oneway_turn','level':'hsr','height':15.5,
        'hand':_hand,'angle':90,'radius':'compact','category':'oneway-levels'}
for _level in ('ground','hsr','l3','l4'):
    for _hand in ('left','right'):
        _key=f'interchange_oneway_{_level}_turn90_{_hand}_wide'
        _DEFINITIONS[_key]={'kind':'oneway_turn','level':_level,'height':LEVELS[_level],
            'hand':_hand,'angle':90,'radius':'wide','category':'oneway-levels'}
PENDING_CROSSINGS={}
for _lower in ('ground','hsr'):
    for _variant in ('upper_grid_lower_diag','upper_diag_lower_grid','upper_diag_lower_diag'):
        _key=f'interchange_l4_{_variant}_over_{_lower}'
        PENDING_CROSSINGS[_key]={'kind':'flyover_crossing','height':30.5,'lower_height':LEVELS[_lower],
            'upper_heading':'diagonal' if _variant.startswith('upper_diag') else 'straight',
            'lower_heading':'diagonal' if 'lower_diag' in _variant else 'straight',
            'lower_level':_lower,'crossing_variant':_variant,'category':'true-flyovers'}
PENDING_CROSSINGS['interchange_ground_oneway_under_hsr']={
    'kind':'flyover_crossing','height':1.,'lower_height':1.,'upper_height':15.5,
    'lower_level':'ground','crossing_variant':'ground_single_under_hsr_dual','category':'true-flyovers'}
PENDING_CROSSINGS['interchange_hsr_oneway_over_ground']={
    'kind':'flyover_crossing','height':15.5,'lower_height':1.,'upper_height':15.5,
    'lower_level':'ground','crossing_variant':'hsr_single_over_ground_dual','category':'true-flyovers'}
for _recipe,_definition in PENDING_CROSSINGS.items():
    _variant=_definition['crossing_variant']
    if _variant=='ground_single_under_hsr_dual':
        _definition['name']='Ground One-Way Track under HSR'
        _definition['one_way_position']='lower'
    elif _variant=='hsr_single_over_ground_dual':
        _definition['name']='One-Way HSR over GHSR'
        _definition['one_way_position']='upper'
    else:
        _lower_label='GHSR' if _definition['lower_level']=='ground' else 'HSR'
        _upper_label='Diagonal One-Way L4' if _definition['upper_heading']=='diagonal' else 'One-Way L4'
        _lower_shape='Diagonal ' if _definition['lower_heading']=='diagonal' else ''
        _definition['name']=f'{_upper_label} over {_lower_shape}{_lower_label}'
        _definition['one_way_position']='upper'
    _definition['description']='Actual rail geometry and directed train paths at two heights. The one-way track and two-way track cross without a transfer. Experimental fixed piece; test rendering, traffic and shadows in the game.'

_DEFINITIONS.update(PENDING_CROSSINGS)
for _angle in (45,90,135):
    for _radius in ('compact','wide'):
        for _mode in ('split','merge'):
            _key=f'interchange_l4_{_mode}_{_angle}_{_radius}_left'
            _DEFINITIONS[_key]={'kind':'directed_branch','level':'l4','height':30.5,
                'angle':_angle,'radius':_radius,'mode':_mode,'hand':'left','category':'oneway-branches',
                'name':f'One-Way L4 {_mode.title()} {_angle}deg Left {_radius.title()}',
                'description':'A left-hand split or merge on the centered one-way 30.5 m track. No opposing mainline track is crossed. Use matching one-way L4 fillers and level adapters.'}

def _raw_layout(recipe):
    definition=_DEFINITIONS[recipe]
    kind=definition['kind']
    if kind=='oneway_filler':return _filler(definition)
    if kind=='oneway_turn':return _turn90(definition)
    if kind=='directed_branch':return _split(definition)
    if kind=='oneway_grade':return _grade(definition)
    if kind=='flyover_crossing':return _flyover_crossing(definition)
    raise ValueError(f'Unsupported interchange layout: {recipe}')


def _nearest_native_heading(vector):
    angle=math.atan2(vector[1],vector[0])
    snapped=round(angle/(math.pi/4))*(math.pi/4)
    require(abs(math.remainder(angle-snapped,2*math.pi))<math.radians(5.),
            'An authored external port lacks a reviewed cardinal/diagonal heading')
    return tuple(0. if abs(value)<1e-10 else round(value,12)
                 for value in (math.cos(snapped),math.sin(snapped)))


def _native_collars(layout,definition):
    """Encode exact native-facing tangents without moving ports or seams.

    Cubic samples approach a native port at a slightly oblique chord. A
    short straight collar makes the PATH, deck and construction category
    agree on the actual intended cardinal or 45-degree connection.
    """
    starts,ends=Counter(),Counter()
    for (x,row),data in layout.items():
        for route in data['routes']:
            starts[_point((route['points'][0][0]+16*x,route['points'][0][1]-16*row,route['points'][0][2]))]+=1
            ends[_point((route['points'][-1][0]+16*x,route['points'][-1][1]-16*row,route['points'][-1][2]))]+=1
    external=(starts.keys()-ends.keys())|(ends.keys()-starts.keys())
    headings={}
    for (x,row),data in layout.items():
        for route in data['routes']:
            for at_start in (True,False):
                points=route['points']
                p=points[0 if at_start else -1]
                global_point=_point((p[0]+16*x,p[1]-16*row,p[2]))
                if global_point not in external:continue
                a,b=points[:2] if at_start else points[-2:]
                headings[global_point]=_nearest_native_heading((b[0]-a[0],b[1]-a[1]))

    def collar(points,start,end):
        def finish(source,vector):
            if vector is None:return source
            endpoint=source[-1]
            before=source[-2]
            actual=(endpoint[0]-before[0],endpoint[1]-before[1])
            if abs(actual[0]*vector[1]-actual[1]*vector[0])<1e-10 and sum(actual[j]*vector[j] for j in (0,1))>0:
                return source
            # Blend the exact collar into the existing curve. A single new
            # vertex would concentrate the small heading correction into a
            # kink and could reduce the wider 135-degree curve's radius.
            index=len(source)-2
            while index>0 and math.dist(source[index][:2],endpoint[:2])<8.:index-=1
            anchor=source[index]
            old_a,old_b=(source[index-1],anchor) if index else (anchor,source[1])
            direction=(old_b[0]-old_a[0],old_b[1]-old_a[1])
            length=math.hypot(*direction)
            direction=tuple(v/length for v in direction)
            require(abs(anchor[2]-endpoint[2])<1e-7,
                    'A native-facing tangent collar must remain on a flat endpoint approach')
            last=(endpoint[0]-.25*vector[0],endpoint[1]-.25*vector[1],endpoint[2])
            span=math.dist(anchor[:2],last[:2])
            control=[anchor[:2],tuple(anchor[j]+span*direction[j]/3 for j in (0,1)),
                     tuple(last[j]-.45*span*vector[j] for j in (0,1)),last[:2]]
            output=list(source[:index+1])
            count=max(4,math.ceil(span))
            for n in range(1,count+1):
                t=n/count;u=1-t
                output.append((*tuple(u**3*control[0][j]+3*u*u*t*control[1][j]+
                    3*u*t*t*control[2][j]+t**3*control[3][j] for j in (0,1)),endpoint[2]))
            output.append(endpoint)
            return output
        output=finish(list(points),end)
        if start is not None:
            output=list(reversed(finish(list(reversed(output)),tuple(-v for v in start))))
        return output

    for (x,row),data in layout.items():
        for collection in ('routes','decks'):
            for item in data[collection]:
                points=item['points']
                world=lambda p:_point((p[0]+16*x,p[1]-16*row,p[2]))
                first,last=headings.get(world(points[0])),headings.get(world(points[-1]))
                if first is None and last is None:continue
                item['points']=collar(points,first,last)
                points=item['points']
                a,b=(points[0],points[1]);c,d=(points[-2],points[-1])
                if collection=='routes':
                    item['tangent_in']=(b[0]-a[0],b[1]-a[1])
                    item['tangent_out']=(d[0]-c[0],d[1]-c[1])
                else:
                    item['start_tangent']=(b[0]-a[0],b[1]-a[1])
                    item['end_tangent']=(d[0]-c[0],d[1]-c[1])
    return layout


def _layout(recipe):
    return _native_collars(_raw_layout(recipe),_DEFINITIONS[recipe])


def interchange_layout(recipe):
    require(recipe in _DEFINITIONS,f'Unknown interchange recipe: {recipe}')
    return _normalize(_layout(recipe))[0]


RECIPES=tuple(_DEFINITIONS)
INFO={}
for _recipe,_definition in _DEFINITIONS.items():
    _layout_data,_shift=_normalize(_layout(_recipe))
    _cells=list(_layout_data)
    _incoming,_outgoing=Counter(),Counter()
    for (_cx,_row),_data in _layout_data.items():
        for _route in _data['routes']:
            _a,_b=[_point((p[0]+16*_cx,p[1]-16*_row,p[2])) for p in (_route['points'][0],_route['points'][-1])]
            _outgoing[_a]+=1;_incoming[_b]+=1
    _ports={'in':sorted(_outgoing.keys()-_incoming.keys()),'out':sorted(_incoming.keys()-_outgoing.keys())}
    INFO[_recipe]={**deepcopy(_definition),'recipe':_recipe,'cells':_cells,
        'footprint':(max(x for x,_ in _cells)+1,max(y for _,y in _cells)+1),
        'cost':100*len(_cells),'origin_shift':_shift,'ports':_ports,
        'construction_flags':{cell:_construction_flags(data['routes']) for cell,data in _layout_data.items()},
        'orientation_policy':'rotate-only-preserve-direction','structural_cells':[],
        'effect_donor':((0xEA5118B0,0xEA5118B1,0x5DDF0100),'preview_hsr_ofillerpiece000',0x5DD31500),
        'provenance':'Authored directed SC4PATH and native-calibrated swept deck profile; no game-test claim'}
