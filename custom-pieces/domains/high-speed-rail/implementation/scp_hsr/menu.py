"""Native Rail-menu buttons for Simon's Custom Pieces.

Only labels, icon/button IDs, order, and label references change from the native
NAM Rail-menu exemplar. The root builder owns each separate RUL0 rotation ring.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import struct

from scp.dbpf import exemplar, encode_exemplar, tgi_string
from .icons import icon_identity, make_icon, validate_icon

from scp.menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
DONOR_MENU_TGI = (*MENU_EXEMPLAR, 0x6A47C200)
EDITED_PROPERTIES = {0x20, 0x8A2602B8, 0x8A2602B9, 0x8A2602BB, 0x8A416A99, 0xCA416AB5}


def _require(condition: bool, message: str):
    if not condition:
        raise ValueError(message)


def _hex(value) -> int:
    return int(value, 16) if isinstance(value, str) else int(value)


def _properties(record: dict) -> dict:
    props = {_hex(prop['id']): prop for prop in record['properties']}
    _require(len(props) == len(record['properties']), 'Duplicate menu exemplar property')
    return props


def _ltext(value: str) -> bytes:
    encoded = value.encode('utf-16-le')
    length = len(encoded) // 2
    _require(length <= 65535 and '\0' not in value, 'Invalid LTEXT text')
    return struct.pack('<HH', length, 0x1000) + encoded


def _read_ltext(raw: bytes) -> str:
    _require(len(raw) >= 4, 'Truncated menu LTEXT')
    length, control = struct.unpack_from('<HH', raw)
    _require(control == 0x1000 and len(raw) == 4 + length * 2, 'Invalid menu LTEXT header')
    return raw[4:].decode('utf-16-le')


def _spec_fields(spec: dict) -> dict:
    menu = spec['menu']
    menu_id, puzzle_id, order = _hex(menu['id']), _hex(spec['puzzle_id']), _hex(menu['order'])
    _require(0 < puzzle_id <= 0xFFFF and menu_id == (0x6A470000 | puzzle_id),
             'Menu button ID must retain the native 6A47 prefix and match its RUL0 root')
    _require(0x70000000 <= order < 0x80000000, 'SCP network buttons require a Rail-menu item order')
    _require(bool(spec['name'].strip()) and bool(spec['description'].strip()), 'Missing piece name or description')
    from scp.design_review import review_label, review_note
    warning = review_label(spec)
    identity = icon_identity(menu['style'])
    title = ('SCP | [' + identity['badge'] + '] ' +
             (f'[{warning}] ' if warning else '') + spec['name'].strip())
    experimental = spec.get('experimental', spec.get('status', 'experimental') == 'experimental')
    status = 'Experimental' if experimental else 'Custom network piece'
    category_note = (identity['meaning'] + ' (' + identity['badge'] + '). ' +
                     ('Place the full junction with one click.' if identity['category'] == 'pnp'
                      else 'Places this component; an interchange blueprint requires multiple pieces.'))
    description = ("Simon's Custom Pieces\n" + status + '\n' + category_note +
                   '\n\n' + spec['description'].strip())
    if warning:
        description = review_note(spec) + '\n\n' + description
    return {'menu_id': menu_id, 'puzzle_id': puzzle_id, 'order': order,
            'style': menu['style'], 'title': title, 'description': description,
            'icon_identity': identity}


def build_menu_resources(donor_exemplar: bytes, spec: dict) -> tuple[dict, dict]:
    """Build four native resources from one registry entry and a NAM donor.

    The resources are the type-40 Rail-menu exemplar, the 176×44 RGBA icon
    strip, and its two UTF-16 localized-text resources. No disk or game writes
    occur here. The caller must check all resulting TGIs for collisions.
    """
    data = _spec_fields(spec)
    record = deepcopy(exemplar(donor_exemplar))
    props = _properties(record)
    _require(props[0x10]['values'] == [40], 'Expected native network-menu exemplar type 40')
    _require(set(props) == {0x10, 0x20, 0x4001, 0x49CAC341, 0x8A2602B8, 0x8A2602B9,
                           0x8A2602BB, 0x8A416A99, 0x8A94EEE0, 0xCA416AB5},
             'Native NAM menu exemplar properties changed; re-audit donor')
    replacements = {
        0x20: data['title'], 0x8A2602B8: [data['menu_id']], 0x8A2602B9: [data['order']],
        0x8A2602BB: [data['menu_id']], 0x8A416A99: [*TITLE, data['menu_id']],
        0xCA416AB5: [*DESCRIPTION, data['menu_id']],
    }
    for prop_id, values in replacements.items():
        props[prop_id]['values'] = values
    resources = {
        (*MENU_EXEMPLAR, data['menu_id']): encode_exemplar(record),
        (*ICON, data['menu_id']): make_icon(data['style']),
        (*TITLE, data['menu_id']): _ltext(data['title']),
        (*DESCRIPTION, data['menu_id']): _ltext(data['description']),
    }
    metadata = validate_menu_resources(resources, donor_exemplar, spec)
    return resources, metadata


def validate_menu_resources(resources: dict, donor_exemplar: bytes, spec: dict) -> dict:
    """Inspect actual resource contents, including all retained donor fields."""
    data = _spec_fields(spec)
    expected = {(*prefix, data['menu_id']) for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)}
    _require(expected <= set(resources), 'Missing native menu resources')
    donor = exemplar(donor_exemplar)
    actual = exemplar(resources[*MENU_EXEMPLAR, data['menu_id']])
    a, d = _properties(actual), _properties(donor)
    _require(actual['parent'] == donor['parent'] and list(a) == list(d),
             'Menu parent cohort or property ordering changed')
    _require(a[0x10]['values'] == [40], 'Wrong menu exemplar type')
    for prop_id in d:
        if prop_id not in EDITED_PROPERTIES:
            _require(a[prop_id] == d[prop_id], f'Changed retained native menu property {prop_id:08x}')
        else:
            _require(a[prop_id]['type'] == d[prop_id]['type'] and
                     a[prop_id]['key_type'] == d[prop_id]['key_type'], 'Changed property encoding')
    _require(a[0x20]['values'] == data['title'], 'Wrong exemplar name')
    for prop_id in (0x8A2602B8, 0x8A2602BB):
        _require(a[prop_id]['values'] == [data['menu_id']], 'Wrong icon or root-button reference')
    _require(a[0x8A2602B9]['values'] == [data['order']], 'Wrong Rail-menu order')
    _require(a[0x8A416A99]['values'] == [*TITLE, data['menu_id']] and
             a[0xCA416AB5]['values'] == [*DESCRIPTION, data['menu_id']], 'Wrong menu LTEXT references')
    _require(_read_ltext(resources[*TITLE, data['menu_id']]) == data['title'] and
             _read_ltext(resources[*DESCRIPTION, data['menu_id']]) == data['description'],
             'Wrong piece title or description')
    icon = validate_icon(resources[*ICON, data['menu_id']])
    _require(resources[*ICON, data['menu_id']] == make_icon(data['style']),
             'Menu artwork does not match the registered procedural icon style')
    return {'piece_id': spec['id'], 'title': data['title'], 'menu': 'Rail',
            'menu_id': f"{data['menu_id']:08x}", 'puzzle_id': f"{data['puzzle_id']:04x}",
            'order': f"{data['order']:08x}", 'icon_style': data['style'], 'icon': icon,
            'icon_identity': data['icon_identity'],
            'retained_native_properties_verified': True,
            'donor_menu_exemplar_tgi': tgi_string(DONOR_MENU_TGI),
            'resources': [{'tgi': tgi_string(key), 'bytes': len(resources[key]),
                           'sha256': hashlib.sha256(resources[key]).hexdigest()} for key in sorted(expected)],
            'in_game_menu_tested': False}


def menu_donor(context):
    """Use the audited native Rail button template for this transport domain."""
    return context['hsr'][DONOR_MENU_TGI]
