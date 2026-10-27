"""Build one assembly cycle entry, or verify the retained legacy submenu form.

This changes presentation resources only. The caller supplies an independently
verified build, allocates IDs, composes the construction cycle, checks installed
resource collisions, and keeps assembly menu preparation after piece compilation.
An alias sharing Item Button ID with a piece is a testable hypothesis, not an
in-game result. Source: https://github.com/memo33/submenus-dll#information-for-modders
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
from io import BytesIO
import math
import struct

from .dbpf import encode_exemplar, exemplar, require, tgi_string
from .menu import DESCRIPTION, ICON, MENU_EXEMPLAR, TITLE

ITEM_SUBMENU_PARENT_ID = 0x8A2602CA
ITEM_BUTTON_CLASS = 0x8A2602CC
RAIL_PARENT_ID = 0x29
_PRESENTATION_PREFIXES = (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)


def _uint(value, name):
    require(isinstance(value, (int, str)) and not isinstance(value, bool),
            f'{name} must be an unsigned 32-bit integer or hexadecimal string')
    try:
        result = int(value, 16) if isinstance(value, str) else value
    except ValueError as error:
        raise ValueError(f'{name} must be a hexadecimal string') from error
    require(0 < result <= 0xFFFFFFFF, f'{name} must be a nonzero unsigned 32-bit value')
    return result


def _props(record):
    result = {int(prop['id'], 16): prop for prop in record['properties']}
    require(len(result) == len(record['properties']), 'Duplicate menu exemplar property')
    return result


def _set(record, prop_id, values):
    props = _props(record)
    if prop_id in props:
        props[prop_id]['values'] = values
    else:
        record['properties'].append({'id': f'0x{prop_id:08x}', 'type': '0x0300',
                                     'key_type': '0x0000', 'values': values,
                                     'repetitions': None})


def _ltext(value):
    require(isinstance(value, str) and value.strip() and '\0' not in value,
            'Menu title and description must be nonempty text without NUL characters')
    raw = value.encode('utf-16-le')
    require(len(raw) // 2 <= 65535, 'Menu LTEXT exceeds its 16-bit length field')
    return struct.pack('<HH', len(raw) // 2, 0x1000) + raw


def _definition(value, name):
    require(isinstance(value, dict), f'{name} must be an object')
    result = dict(value)
    for key in ('id', 'order'):
        require(key in result, f'{name} requires {key}')
        result[key] = _uint(result[key], f'{name}.{key}')
    require(0x70000000 <= result['order'] < 0x80000000,
            f'{name}.order must be in the Rail-menu item-order range')
    for key in ('title', 'description'):
        require(key in result, f'{name} requires {key}')
        _ltext(result[key])
    return result


def _icon(kind):
    """Original four-state 176 by 44 PNG: TAB cycle or individual-piece grid."""
    from PIL import Image, ImageDraw, ImageFont, ImageOps

    strip = Image.new('RGBA', (176, 44))
    font = ImageFont.load_default()
    for number in range(4):
        image = Image.new('RGBA', (44, 44), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        color = ((68, 183, 182), (68, 183, 182), (248, 197, 82), (113, 222, 218))[number]
        draw.rounded_rectangle((1, 1, 42, 42), radius=5, fill=(21, 42, 52), outline=color, width=2)
        label = 'TAB' if kind == 'cycle' else 'PARTS'
        box = draw.textbbox((0, 0), label, font=font)
        draw.text(((44 - (box[2] - box[0])) // 2, 4), label, fill=(244, 249, 249), font=font)
        if kind == 'cycle':
            for x in (6, 17, 28):
                draw.rectangle((x, 19, x + 8, 29), fill=color)
            draw.line((8, 34, 35, 34), fill=color, width=2)
            draw.polygon(((35, 31), (40, 34), (35, 37)), fill=color)
            draw.polygon(((8, 31), (3, 34), (8, 37)), fill=color)
        else:
            for x in (7, 23):
                for y in (19, 30):
                    draw.rectangle((x, y, x + 12, y + 8), fill=color)
        if number == 0:
            alpha = image.getchannel('A')
            image = ImageOps.grayscale(image).convert('RGBA')
            image.putalpha(alpha)
        strip.paste(image, (44 * number, 0))
    output = BytesIO()
    strip.save(output, format='PNG', optimize=False)
    return output.getvalue()


def make_assembly_icon(routes=None):
    """Draw the complete north-up assembly; retain the historical icon on demand.

    ``routes`` contains placed east/north/height polylines. No game resources,
    build outputs, placements, or observations are changed by this illustration.
    Omitting routes reproduces frozen historical menu candidates exactly.
    """
    if routes is None:
        return _icon('cycle')
    from PIL import Image, ImageDraw, ImageOps

    require(isinstance(routes, (list, tuple)) and routes, 'Assembly icon needs actual routes')
    require(all(isinstance(route, (list, tuple)) and len(route) >= 2 for route in routes),
            'Assembly icon routes need at least two points')
    require(all(isinstance(point, (list, tuple)) and len(point) == 3
                and all(isinstance(value, (int, float)) and not isinstance(value, bool)
                        and math.isfinite(value) for value in point)
                for route in routes for point in route), 'Assembly icon needs finite XYZ points')
    points = [point for route in routes for point in route]
    xmin, xmax = min(p[0] for p in points), max(p[0] for p in points)
    ymin, ymax = min(p[1] for p in points), max(p[1] for p in points)
    require(xmax > xmin or ymax > ymin, 'Assembly icon routes have no planar extent')
    factor = min(34 / max(xmax - xmin, 1), 30 / max(ymax - ymin, 1))
    scale = 6
    strip = Image.new('RGBA', (176, 44))
    glyphs = {'T': ('111', '010', '010', '010', '010'),
              'A': ('010', '101', '111', '101', '101'),
              'B': ('110', '101', '110', '101', '110')}

    def screen(point):
        return ((22 + (point[0] - (xmin + xmax) / 2) * factor) * scale,
                (18.5 - (point[1] - (ymin + ymax) / 2) * factor) * scale)

    for number in range(4):
        image = Image.new('RGBA', (44 * scale, 44 * scale))
        draw = ImageDraw.Draw(image)
        border = ((68, 183, 182), (68, 183, 182), (248, 197, 82), (113, 222, 218))[number]
        draw.rounded_rectangle((scale, scale, 42 * scale, 42 * scale), radius=5 * scale,
                               fill=(14, 32, 42), outline=border, width=round(1.5 * scale))
        # Higher tracks cover lower tracks at genuine crossings. Thin dark
        # halos separate the loop from the nearby approach at the native size.
        for route in sorted(routes, key=lambda row: sum(p[2] for p in row) / len(row)):
            planar = [screen(point) for point in route]
            draw.line(planar, fill=(5, 15, 23), width=round(3.0 * scale), joint='curve')
            for first, last, a, b in zip(route, route[1:], planar, planar[1:]):
                upper = min(1., max(0., ((first[2] + last[2]) / 2 - 15.5) / 15.))
                colour = tuple(round(low + (high - low) * upper)
                               for low, high in zip((240, 225, 178), (83, 222, 208)))
                draw.line((a, b), fill=colour, width=round(1.35 * scale))
        image = image.resize((44, 44), Image.Resampling.LANCZOS)
        draw = ImageDraw.Draw(image)
        # Reserve only five pixels for the component-cycle hint, leaving the
        # complete layout enough room to be recognized without a large label.
        draw.rectangle((8, 36, 35, 40), fill=(14, 32, 42))
        for index, letter in enumerate('TAB'):
            for y, row in enumerate(glyphs[letter]):
                for x, value in enumerate(row):
                    if value == '1':
                        draw.point((16 + index * 4 + x, 36 + y), fill=(244, 249, 249))
        draw.line((8, 38, 12, 38), fill=border)
        draw.line((8, 38, 10, 36), fill=border)
        draw.line((8, 38, 10, 40), fill=border)
        draw.line((31, 38, 35, 38), fill=border)
        draw.line((33, 36, 35, 38, 33, 40), fill=border)
        if number == 0:
            alpha = image.getchannel('A')
            image = ImageOps.grayscale(image).convert('RGBA')
            image.putalpha(alpha)
        strip.paste(image, (44 * number, 0))
    output = BytesIO()
    strip.save(output, format='PNG', optimize=False)
    return output.getvalue()


def _validate_icon(raw, kind, expected_icon=None):
    """Check native image bytes while allowing equivalent PNG compression."""
    from PIL import Image

    require(isinstance(raw, bytes), 'Menu icon must be PNG bytes')
    require(len(raw) >= 33 and raw[:16] == b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR',
            'Menu icon must be a valid 176 by 44 RGBA PNG')
    require(struct.unpack('>IIBBBBB', raw[16:29]) == (176, 44, 8, 6, 0, 0, 0),
            'Menu icon must be a 176 by 44 noninterlaced 8-bit RGBA PNG')
    try:
        with Image.open(BytesIO(raw)) as image:
            require(image.format == 'PNG' and image.mode == 'RGBA' and image.size == (176, 44),
                    'Menu icon must be a 176 by 44 RGBA PNG')
            require(image.get_format_mimetype() == 'image/png' and image.n_frames == 1,
                    'Menu icon must be a single static PNG; APNG animation is not supported')
            image.verify()
        with Image.open(BytesIO(raw)) as image:
            actual_pixels = image.tobytes()
    except (OSError, SyntaxError) as error:
        raise ValueError('Menu icon must be a valid 176 by 44 RGBA PNG') from error
    with Image.open(BytesIO(expected_icon if expected_icon is not None else _icon(kind))) as expected:
        require(actual_pixels == expected.tobytes(),
                'Assembly icon differs from the canonical cycle artwork; regenerate it with assembly-icons'
                if kind == 'cycle' else 'Wrong experiment icon')


def validate_assembly_icon(raw, *, routes=None, expected_icon=None):
    """Require exact source-derived artwork pixels and the native PNG format."""
    require(routes is None or expected_icon is None, 'Specify routes or frozen icon proof, not both')
    _validate_icon(raw, 'cycle', expected_icon if expected_icon is not None else make_assembly_icon(routes))


def _new_button(template, definition, *, kind, icon=None):
    record = deepcopy(template)
    button_id = definition['id']
    for prop_id, values in {
            0x20: definition['title'], 0x8A2602B8: [button_id],
            0x8A2602B9: [definition['order']],
            0x8A2602BB: [definition.get('target_id', button_id)],
            0x8A416A99: [*TITLE, button_id],
            0xCA416AB5: [*DESCRIPTION, button_id]}.items():
        _set(record, prop_id, values)
    if kind == 'submenu':
        _set(record, ITEM_SUBMENU_PARENT_ID, [RAIL_PARENT_ID])
        _set(record, ITEM_BUTTON_CLASS, [1])
    return {(*MENU_EXEMPLAR, button_id): encode_exemplar(record),
            (*ICON, button_id): icon if icon is not None else _icon(kind),
            (*TITLE, button_id): _ltext(definition['title']),
            (*DESCRIPTION, button_id): _ltext(definition['description'])}


def build_menu_experiment_resources(source_resources, pieces, *, cycle_button, submenu=None,
                                    cycle_icon=None, expected_cycle_icon=None):
    """Return a new resource mapping and a byte-preservation audit.

    ``pieces`` is the ordered sequence of existing piece definitions. Original
    member menu presentations are removed when ``submenu`` is absent: the
    assembly gets one cycle button, while unrelated standalone pieces remain.
    A supplied ``submenu`` retains the historical two-entry test format.
    Each new button definition supplies ``id``,
    ``order``, ``title``, and ``description``. ``cycle_button`` also requires
    ``target_id`` equal to the first piece's existing menu/root button ID.
    Its distinct presentation ID changes no construction definition itself.
    Nothing is written to disk, and caller-owned mappings are never mutated.
    A supplied ``cycle_icon`` must match every canonical assembly artwork pixel;
    its original PNG encoding is retained exactly in the compiled resource.
    """
    if cycle_icon is not None:
        validate_assembly_icon(cycle_icon, expected_icon=expected_cycle_icon)
    require(isinstance(source_resources, dict) and source_resources,
            'Source resources must be a nonempty mapping from a verified build')
    require(not isinstance(pieces, (str, bytes, dict)), 'Pieces must be an ordered sequence')
    pieces = list(pieces)
    require(pieces, 'At least one piece is required')
    cycle = _definition(cycle_button, 'cycle_button')
    group = _definition(submenu, 'submenu') if submenu is not None else None
    require('target_id' in cycle, 'cycle_button requires target_id')
    cycle['target_id'] = _uint(cycle['target_id'], 'cycle_button.target_id')
    if group is not None:
        require('target_id' not in group, 'Submenu button cannot have a construction target')
        require(cycle['id'] != group['id'], 'Cycle and submenu presentation IDs must be distinct')
    buttons = (cycle, group) if group is not None else (cycle,)
    for button in buttons:
        require(all((*prefix, button['id']) not in source_resources
                    for prefix in _PRESENTATION_PREFIXES),
                f'New menu resource ID collides with source resources: {button["id"]:08x}')
    records, seen_pieces, seen_ids = [], set(), set()
    for piece in pieces:
        require(isinstance(piece, dict) and isinstance(piece.get('menu'), dict) and
                isinstance(piece.get('id'), str) and piece['id'].strip(),
                'Each piece requires an id and menu definition')
        button_id = _uint(piece['menu']['id'], f'{piece["id"]}.menu.id')
        require(piece['id'] not in seen_pieces and button_id not in seen_ids,
                'Duplicate piece identity or original menu button ID')
        require(button_id not in {button['id'] for button in buttons},
                'New presentation ID collides with an original menu button')
        seen_pieces.add(piece['id'])
        seen_ids.add(button_id)
        require(all((*prefix, button_id) in source_resources for prefix in _PRESENTATION_PREFIXES),
                f'Missing original menu resources for {piece["id"]}')
        original = exemplar(source_resources[*MENU_EXEMPLAR, button_id])
        props = _props(original)
        for prop_id in (0x10, 0x20, 0x8A2602B8, 0x8A2602B9, 0x8A2602BB,
                        0x8A416A99, 0xCA416AB5):
            require(prop_id in props, f'Missing native menu property {prop_id:08x}')
        require(props[0x10]['values'] == [40], 'Expected type-40 network catalogue exemplar')
        require(props[0x8A2602BB]['values'] == [button_id] and
                props[0x8A2602B8]['values'] == [button_id] and
                props[0x8A416A99]['values'] == [*TITLE, button_id] and
                props[0xCA416AB5]['values'] == [*DESCRIPTION, button_id],
                'Original button references do not match its registered identity')
        require(ITEM_SUBMENU_PARENT_ID not in props and ITEM_BUTTON_CLASS not in props,
                'Source already contains submenu experiment properties')
        order = _uint(piece['menu']['order'], f'{piece["id"]}.menu.order')
        require(props[0x8A2602B9]['values'] == [order] and 0x70000000 <= order < 0x80000000,
                'Original Rail-menu order differs from piece definition')
        records.append((piece['id'], button_id, original))
    require(cycle['target_id'] == records[0][1],
            'Cycle alias must target the first selected piece\'s existing root button')
    result = dict(source_resources)
    if group is not None:
        for _, button_id, original in records:
            record = deepcopy(original)
            _set(record, ITEM_SUBMENU_PARENT_ID, [group['id']])
            _set(record, ITEM_BUTTON_CLASS, [2])
            result[*MENU_EXEMPLAR, button_id] = encode_exemplar(record)
    else:
        for _, button_id, _ in records:
            for prefix in _PRESENTATION_PREFIXES:
                del result[*prefix, button_id]
    presentations = ((cycle, 'cycle'), (group, 'submenu')) if group is not None else ((cycle, 'cycle'),)
    for button, kind in presentations:
        result.update(_new_button(records[0][2], button, kind=kind,
                                  icon=cycle_icon if kind == 'cycle' else None))
    report = validate_menu_experiment_resources(
        result, source_resources, pieces, cycle_button=cycle, submenu=group,
        expected_cycle_icon=expected_cycle_icon)
    return result, report


def validate_menu_experiment_resources(resources, source_resources, pieces, *, cycle_button, submenu=None,
                                       expected_cycle_icon=None):
    """Inspect the encoded result and reject any change outside presentation."""
    cycle, group = cycle_button, submenu
    cycle_id = _uint(cycle['id'], 'cycle id')
    group_id = _uint(group['id'], 'submenu id') if group is not None else None
    target_id = _uint(cycle['target_id'], 'cycle target')
    changed = ({(*MENU_EXEMPLAR, _uint(p['menu']['id'], 'original id')) for p in pieces}
               if group is not None else set())
    added = {(*prefix, button_id) for prefix in _PRESENTATION_PREFIXES
             for button_id in ((cycle_id, group_id) if group is not None else (cycle_id,))}
    removed = ({(*prefix, _uint(piece['menu']['id'], 'member id'))
                for piece in pieces for prefix in _PRESENTATION_PREFIXES}
               if group is None else set())
    require(set(resources) == (set(source_resources) - removed) | added,
            'Experiment added or removed an unexpected resource')
    for key in set(source_resources) - changed - removed:
        require(resources[key] == source_resources[key],
                f'Changed non-target source resource {tgi_string(key)}')
    individual = []
    for piece in pieces:
        button_id = _uint(piece['menu']['id'], 'original id')
        key = (*MENU_EXEMPLAR, button_id)
        if group is None:
            require(all((*prefix, button_id) not in resources for prefix in _PRESENTATION_PREFIXES),
                    'Assembly member still has an individual menu presentation')
            continue
        before, after = exemplar(source_resources[key]), exemplar(resources[key])
        original, actual = _props(before), _props(after)
        require(after['parent'] == before['parent'] and
                list(actual) == [*original, ITEM_SUBMENU_PARENT_ID, ITEM_BUTTON_CLASS],
                'Original menu parent or property order changed')
        require(all(actual[prop_id] == prop for prop_id, prop in original.items()),
                'Changed original menu properties, encodings, or construction target')
        require(actual[ITEM_SUBMENU_PARENT_ID]['values'] == [group_id] and
                actual[ITEM_BUTTON_CLASS]['values'] == [2], 'Wrong individual submenu membership')
        individual.append({'piece_id': piece['id'], 'button_id': f'{button_id:08x}',
                           'target_id': f'{button_id:08x}', 'parent_id': f'{group_id:08x}'})
    template = exemplar(source_resources[*MENU_EXEMPLAR, _uint(pieces[0]['menu']['id'], 'template id')])
    template_props = _props(template)
    edited = {0x20, 0x8A2602B8, 0x8A2602B9, 0x8A2602BB, 0x8A416A99, 0xCA416AB5}
    presentations = (((cycle, cycle_id, 'cycle'), (group, group_id, 'submenu'))
                     if group is not None else ((cycle, cycle_id, 'cycle'),))
    for button, button_id, kind in presentations:
        actual = exemplar(resources[*MENU_EXEMPLAR, button_id])
        props = _props(actual)
        expected_ids = [*template_props]
        if kind == 'submenu':
            expected_ids.extend((ITEM_SUBMENU_PARENT_ID, ITEM_BUTTON_CLASS))
        require(actual['parent'] == template['parent'] and list(props) == expected_ids,
                'New button changed native parent or retained property ordering')
        require(all(props[prop_id] == value for prop_id, value in template_props.items()
                    if prop_id not in edited), 'New button changed retained native properties')
        for prop_id in edited:
            require(all(props[prop_id][field] == template_props[prop_id][field]
                        for field in ('type', 'key_type')),
                    'New button changed native property encoding')
        require(props[0x20]['values'] == button['title'] and
                props[0x8A2602B8]['values'] == [button_id] and
                props[0x8A2602B9]['values'] == [_uint(button['order'], 'button order')] and
                props[0x8A2602BB]['values'] == [target_id if kind == 'cycle' else button_id] and
                props[0x8A416A99]['values'] == [*TITLE, button_id] and
                props[0xCA416AB5]['values'] == [*DESCRIPTION, button_id],
                'Wrong new button identity, text, icon, order, or construction target')
        if kind == 'submenu':
            require(props[ITEM_SUBMENU_PARENT_ID]['values'] == [RAIL_PARENT_ID] and
                    props[ITEM_BUTTON_CLASS]['values'] == [1], 'Wrong Rail test-submenu properties')
        require(resources[*TITLE, button_id] == _ltext(button['title']) and
                resources[*DESCRIPTION, button_id] == _ltext(button['description']),
                'Wrong new menu localized text')
        _validate_icon(resources[*ICON, button_id], kind,
                       expected_cycle_icon if kind == 'cycle' else None)
    report = {'schema_version': 1, 'individual_buttons': individual,
            'cycle_button': {'presentation_id': f'{cycle_id:08x}', 'target_id': f'{target_id:08x}',
                             'menu': 'Rail', 'construction_alias_verified_in_game': False},
            'submenu': ({'button_id': f'{group_id:08x}', 'parent_id': f'{RAIL_PARENT_ID:08x}'}
                        if group is not None else None),
            'modified_existing_exemplar_tgis': [tgi_string(key) for key in sorted(changed)],
            'added_resource_tgis': [tgi_string(key) for key in sorted(added)],
            'unchanged_source_resource_count': len(source_resources) - len(changed),
            'source_menu_exemplars': [{'tgi': tgi_string(key),
                                       'sha256': hashlib.sha256(source_resources[key]).hexdigest()}
                                      for key in sorted(changed)],
            'in_game_menu_tested': False}
    if group is None:
        report['assembly_menu_buttons'] = 1
        report['member_buttons_hidden'] = len(pieces)
        report['removed_resource_tgis'] = [tgi_string(key) for key in sorted(removed)]
        report['unchanged_source_resource_count'] = len(source_resources) - len(removed)
    return report
