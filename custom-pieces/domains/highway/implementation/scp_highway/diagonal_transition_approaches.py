"""Three exact native sockets for the first-cut diagonal DD transition.

Ground diagonal helpers reuse original NAM rows. Stacked DD helpers share
the already reviewed Y-junction marker pairs, retaining their exact targets
when either transition direction is selected alongside either Y family.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import re

from scp.dbpf import require
from . import diagonal_transition_native as native
from .diagonal_transition_variants import variant_of

OPT_IN = 'native_diagonal_transition_approaches'
SECTION = 'MonoRailDirtRoadIntersectionSolutions'
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
RUL1 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000001)
RUL2 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000002)
NATIVE_RUL1_SHA256 = '4e44ec44283de6fccc3cd40492fc24154d13fb16a5150e13c201c6e615bba998'
NATIVE_CONTROLLER_SHA256 = {
    RUL0: 'd2a63a6c9070857c5360343cfa07f0be13ef0559fd659e9545c57c15dda672b9',
    RUL2: 'c427c7872743ca4cd9f583adf33c93a320babe37c42061fbd33c905696e7a3b1',
}
NATIVE_DEPENDENCY_SHA256 = dict(native.RESOURCE_SHA256)


def rotate_flags(value, pose):
    shift = 8*(pose % 4)
    return ((value << shift) | (value >> ((32-shift) % 32))) & 0xFFFFFFFF


def _marker(target):
    return {0x57530900: 0x01000400, 0x57530200: 0x04000100,
            0x57030200: 0x04020000, 0x57030900: 0x02040000}[target]


def _reviewed(piece):
    from .diagonal_transition_layout import declaration
    key = variant_of(piece)
    row = declaration(piece)
    require(not any(piece.get(name) for name in ('native_dd_approaches', 'native_ghsr_approaches',
            'native_orthogonal_approaches', 'native_y_junction_approaches', 'adaptive_ground')),
            'Diagonal transition cannot mix native or adaptive approach modes')
    tiles = piece.get('tile_ids')
    require(isinstance(tiles, list) and len(tiles) == len(piece['cells'])
            and len(set(tiles)) == len(tiles)
            and all(isinstance(value, str) and re.fullmatch('[0-9a-fA-F]{8}', value) for value in tiles),
            'Invalid first-cut diagonal transition tile addresses')
    return key, row


def approaches(piece):
    if OPT_IN not in piece:
        return []
    require(type(piece[OPT_IN]) is bool, OPT_IN+' must be an exact boolean')
    if not piece[OPT_IN]:
        return []
    key, row = _reviewed(piece)
    origin = row['world_origin_cell']
    result = []
    for socket in native.socket_specs(key):
        target, pose, world_cell = socket.helper
        cell = [world_cell[i]-origin[i] for i in range(2)]
        end = [socket.core_end_cell[i]-origin[i] for i in range(2)]
        require(cell not in piece['cells'] and end in piece['cells'],
                'Native diagonal helper becomes owned or loses its actual core PATH owner')
        result.append({'cell': cell, 'end_cell': end,
            'end_tile_id': piece['tile_ids'][piece['cells'].index(end)].lower(),
            'outward_edge': socket.outward_edge, 'native_tile_id': f'{target:08x}', 'native_rotation': pose,
            'section': SECTION, 'networks': [
                {'name': 'monorail', 'flags': f'{rotate_flags(_marker(target),pose):08x}'},
                {'name': 'dirtroad', 'flags': f'{rotate_flags(0x03010000,pose):08x}'}],
            'native_exemplar_group': '6be08658', 'native_model_reference': 'rkt0',
            'optional': True, 'experimental': True})
    return result


def rul1_sections(piece):
    rows = approaches(piece)
    if not rows:
        return {}
    targets = sorted({int(row['native_tile_id'],16) for row in rows})
    return {SECTION: tuple((rotate_flags(_marker(target),turn), rotate_flags(0x03010000,turn), target,turn,0)
                           for target in targets for turn in range(4))}


def existing_rul1_sections(piece):
    """Only the ground subset is already present in original NAM RUL1."""
    sections = rul1_sections(piece)
    return {section: tuple(row for row in rows if row[2] >> 16 == 0x5703)
            for section, rows in sections.items()}


def dependency_sha256(piece):
    return dict(NATIVE_DEPENDENCY_SHA256) if approaches(piece) else {}


def additional_dependency_keys(piece):
    declared = {(*prefix,int(row['native_tile_id'],16)) for row in approaches(piece)
                for prefix in (native.S3D,native.PATH,native.EXEMPLAR)}
    return set(dependency_sha256(piece))-declared


def dependency_model_references(piece):
    return {key: 'rkt0' for key in additional_dependency_keys(piece) if key[:2] == native.EXEMPLAR}


def _palette(symbol, row):
    networks = ' '.join(item['name']+': 0x'+item['flags'] for item in reversed(row['networks']))
    return f'{symbol} - {networks},0xFFFFFFFF optional'


def _extent(piece, rows):
    width, depth = piece['footprint']
    left = max(0, -min(row['cell'][0] for row in rows))
    top = max(0, -min(row['cell'][1] for row in rows))
    return left, top, max(width+2,max(row['cell'][0]+1 for row in rows))+left, max(depth+1,max(row['cell'][1]+1 for row in rows))+top


def add_approaches(piece, layout, checks, constraints):
    declared = approaches(piece)
    if not declared:
        return list(layout), list(checks), list(constraints)
    width, depth = piece['footprint']
    require(len(layout) == len(constraints) == depth+1
            and all(len(line) == width+2 for line in [*layout,*constraints]), 'Unexpected first-cut core construction extent')
    for grid in (layout,constraints):
        require([(x,y) for y,line in enumerate(grid) for x,value in enumerate(line) if value=='^'] == [(0,depth)]
                and [(x,y) for y,line in enumerate(grid) for x,value in enumerate(line) if value=='<'] == [(width+1,0)],
                'Diagonal helper cannot move modeled coordinate anchors')
    left,top,columns,rows = _extent(piece,declared)
    def padded(source):
        result = [['.']*columns for _ in range(rows)]
        for y,line in enumerate(source):
            result[y+top][left:left+len(line)] = line
        return result
    layout,constraints = padded(layout),padded(constraints)
    palette = list(checks);used = {value for line in layout for value in line if value.isalpha()}
    for row in declared:
        x,y = row['cell'][0]+left,row['cell'][1]+top
        require(layout[y][x] == constraints[y][x] == '.', 'Native diagonal helper collides with core or anchor')
        symbol = next((char for char in reversed('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') if char not in used),None)
        require(symbol is not None,'No unused native helper symbol remains')
        layout[y][x]=symbol;used.add(symbol);palette.append(_palette(symbol,row))
    return [''.join(line) for line in layout],palette,[''.join(line) for line in constraints]


def check_construction_approaches(fields,piece):
    """Validate helpers/padding exactly and return the untouched core fields."""
    result=deepcopy(fields);declared=approaches(piece)
    if not declared:
        return result
    left,top,columns,rows=_extent(piece,declared);width,depth=piece['footprint']
    layout,constraints=([list(line) for line in fields[name]] for name in ('CellLayout','ConsLayout'))
    require(len(layout)==len(constraints)==rows and all(len(line)==columns for line in [*layout,*constraints]),
            'Diagonal native helper changes the exact construction extent')
    for grid in (layout,constraints):
        require([(x,y) for y,line in enumerate(grid) for x,value in enumerate(line) if value=='^']==[(left,top+depth)]
                and [(x,y) for y,line in enumerate(grid) for x,value in enumerate(line) if value=='<']==[(left+width+1,top)],
                'Diagonal native helper changes the modeled coordinate frame')
    palette=list(fields['CheckType']);removed=set();normalize=lambda value:re.sub(r'\s+','',value).lower()
    for row in declared:
        x,y=row['cell'][0]+left,row['cell'][1]+top;symbol=layout[y][x]
        require(symbol.isascii() and symbol.isalpha() and symbol not in removed and constraints[y][x]=='.'
                and sum(line.count(symbol) for line in layout)==1,'Missing, repeated, or owned diagonal native helper')
        found=[line for line in palette if re.match(r'^\s*'+re.escape(symbol)+r'\s*-',line)]
        require(len(found)==1 and normalize(found[0])==normalize(_palette(symbol,row)),
                'Diagonal native helper changes its exact marker, mask, or optional state')
        palette.remove(found[0]);layout[y][x]='.';removed.add(symbol)
    for grid in (layout,constraints):
        require(all(value=='.' for y,line in enumerate(grid) for x,value in enumerate(line)
                    if not(left<=x<left+width+2 and top<=y<top+depth+1)), 'Undeclared native helper padding cell')
    result['CellLayout']=[''.join(line[left:left+width+2]) for line in layout[top:top+depth+1]]
    result['ConsLayout']=[''.join(line[left:left+width+2]) for line in constraints[top:top+depth+1]]
    result['CheckType']=palette
    return result


def check_native_continuation(controller):
    """Pin the native baseline and its existing diagonal ground marker rows."""
    require(all(key in controller and hashlib.sha256(controller[key]).hexdigest()==value
                for key,value in {**NATIVE_CONTROLLER_SHA256,RUL1:NATIVE_RUL1_SHA256}.items()),
            'Diagonal transition needs the measured original NAM controller resources')
    from scp.native_approaches import _section_span,_solution_rows
    start,end=_section_span(controller[RUL1],SECTION);actual=_solution_rows(controller[RUL1][start:end])
    for target in (0x57030200,0x57030900):
        for turn in range(4):
            wanted=(rotate_flags(_marker(target),turn),rotate_flags(0x03010000,turn),target,turn,0)
            require(actual.count(wanted)==1,'Native diagonal ground RUL1 row changed or is ambiguous')
    for target in (0x57530200,0x57530900):
        for turn in range(4):
            pair=rotate_flags(_marker(target),turn),rotate_flags(0x03010000,turn)
            require(not any(row[:2]==pair for row in actual),'DD diagonal marker collides with native baseline')
    return {'existing_native_diagonal_ground_solutions_checked':8,'stacked_DD_marker_pairs_absent_from_native':8,
            'native_rul0_rul1_rul2_pinned':True,'in_game_behavior_tested':False}
