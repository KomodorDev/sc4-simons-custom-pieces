"""Highway-menu resources derived from the audited native RHW menu button."""
from __future__ import annotations

from copy import deepcopy
import hashlib
import io
import struct

from PIL import Image, ImageDraw

from scp.dbpf import exemplar, encode_exemplar, require, tgi_string
from scp.menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION

DONOR_MENU_TGI = (*MENU_EXEMPLAR, 0x6A475700)
EDITED = {0x20, 0x8A2602B8, 0x8A2602B9, 0x8A2602BB, 0x8A416A99, 0xCA416AB5}


def portable_baseline():
    """Reconstruct the measured menu descriptor without private binary inputs."""
    values = [(0x10, 0x300, 0, [40]), (0x20, 0xC00, 0x80, 'RHW_QuickChange'),
              (0x4005, 0x300, 0, [0]), (0x49CAC341, 0x800, 0, [0]),
              (0x8A2602B8, 0x300, 0, [0x6A475700]), (0x8A2602B9, 0x300, 0, [0xFFFFFF04]),
              (0x8A2602BB, 0x300, 0, [0x6A475700]),
              (0x8A416A99, 0x300, 0x80, [0x2026960B, 0x123007BB, 0x6A475700]),
              (0x8A94EEE0, 0x900, 0x80, [0.0]),
              (0xCA416AB5, 0x300, 0x80, [0x2026960B, 0x123006AA, 0x6A475700])]
    record = {'parent': [0, 0, 0], 'properties': [
        {'id': f'0x{pid:08x}', 'type': f'0x{kind:04x}', 'key_type': f'0x{key:04x}',
         'values': value, 'repetitions': len(value) if key else None}
        for pid, kind, key, value in values]}
    return encode_exemplar(record)


def menu_donor(context):
    donor = context['rhw_core'][DONOR_MENU_TGI]
    require(donor == portable_baseline(), 'Native Highway menu descriptor changed; re-audit donor')
    return donor


def verification_donor(donors):
    return donors.get(DONOR_MENU_TGI, portable_baseline())


def make_icon(style):
    require(style in {'ddrhw-crossing', 'ddrhw-ramp', 'ddrhw-ghsr-crossing'}, 'Unsupported highway icon style')
    strip = Image.new('RGBA', (176, 44))
    for n in range(4):
        im = Image.new('RGBA', (44, 44), ('#253a4c', '#344f66', '#182a38', '#77818a')[n])
        draw = ImageDraw.Draw(im)
        draw.line((3, 8, 37, 35), fill='#bcc5c9', width=7)
        if style == 'ddrhw-ghsr-crossing':
            draw.line((3, 8, 37, 35), fill='#445a62', width=9)
            for along in range(5, 36, 4):
                y = 8 + (along - 3) * 27 / 34
                draw.line((along - 3, y + 3, along + 3, y - 3), fill='#8d999e', width=2)
            draw.line((2, 9, 36, 36), fill='#f0eeee', width=1)
            draw.line((5, 6, 39, 33), fill='#f0eeee', width=1)
        draw.line((4, 35, 35, 4), fill='#16202c', width=13)
        draw.line((4, 35, 35, 4), fill='#94a9ba', width=9)
        draw.line((4, 32, 32, 4), fill='#263747', width=5)
        draw.line((7, 35, 35, 7), fill='#334858', width=3)
        draw.line((6, 32, 30, 8), fill='#ffffff', width=1)
        if style == 'ddrhw-ramp':
            draw.line((20, 18, 33, 27, 39, 27), fill='#efc773', width=3)
        draw.rectangle((1, 1, 42, 42), outline='#70899c', width=1)
        strip.paste(im, (44 * n, 0))
    out = io.BytesIO(); strip.save(out, format='PNG')
    return out.getvalue()


def _ltext(value):
    require('\0' not in value, 'Highway menu text contains a null')
    raw = value.encode('utf-16-le')
    return struct.pack('<HH', len(raw) // 2, 0x1000) + raw


def _fields(spec):
    menu, puzzle = int(spec['menu']['id'], 16), int(spec['puzzle_id'], 16)
    require(menu == 0x6A470000 | puzzle and 0 < puzzle <= 0xFFFF, 'Wrong highway menu/root relationship')
    title = 'SCP | [HW] ' + spec['name']
    desc = ("Simon's Custom Pieces\nExperimental highway component\n\n" + spec['description'] +
            '\n\nEach click places this component. Four proper rotations repeat across eight states. Game tests are pending.')
    return menu, title, desc


def build_menu_resources(donor_exemplar, spec):
    menu, title, desc = _fields(spec)
    record = deepcopy(exemplar(donor_exemplar))
    replacement = {0x20: title, 0x8A2602B8: [menu], 0x8A2602B9: [int(spec['menu']['order'], 16)],
                   0x8A2602BB: [menu], 0x8A416A99: [*TITLE, menu], 0xCA416AB5: [*DESCRIPTION, menu]}
    for prop in record['properties']:
        if int(prop['id'], 16) in replacement:
            prop['values'] = replacement[int(prop['id'], 16)]
    resources = {(*MENU_EXEMPLAR, menu): encode_exemplar(record), (*ICON, menu): make_icon(spec['menu']['style']),
                 (*TITLE, menu): _ltext(title), (*DESCRIPTION, menu): _ltext(desc)}
    return resources, validate_menu_resources(resources, donor_exemplar, spec)


def validate_menu_resources(resources, donor_exemplar, spec):
    require(donor_exemplar == portable_baseline(), 'Wrong portable highway menu baseline')
    menu, title, desc = _fields(spec)
    actual = exemplar(resources[*MENU_EXEMPLAR, menu]); donor = exemplar(donor_exemplar)
    require(actual['parent'] == donor['parent'], 'Changed highway menu parent')
    a = {int(prop['id'], 16): prop for prop in actual['properties']}
    d = {int(prop['id'], 16): prop for prop in donor['properties']}
    require(list(a) == list(d), 'Changed highway menu property inventory/order')
    replacement = {0x20: title, 0x8A2602B8: [menu], 0x8A2602B9: [int(spec['menu']['order'], 16)],
                   0x8A2602BB: [menu], 0x8A416A99: [*TITLE, menu], 0xCA416AB5: [*DESCRIPTION, menu]}
    for pid, prop in a.items():
        expected = deepcopy(d[pid])
        if pid in replacement:
            expected['values'] = replacement[pid]
        require(prop['values'] == expected['values'] and prop['type'] == expected['type'] and
                prop['key_type'] == expected['key_type'], f'Wrong highway menu property {pid:08X}')
    require(resources[*TITLE, menu] == _ltext(title) and resources[*DESCRIPTION, menu] == _ltext(desc),
            'Wrong highway menu text')
    require(resources[*ICON, menu] == make_icon(spec['menu']['style']), 'Wrong highway menu icon')
    expected = {(*prefix, menu) for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)}
    return {'piece_id': spec['id'], 'title': title, 'menu': 'Highways', 'menu_id': f'{menu:08x}',
            'puzzle_id': spec['puzzle_id'], 'order': spec['menu']['order'], 'icon_style': spec['menu']['style'],
            'retained_native_properties_verified': True, 'donor_menu_exemplar_tgi': tgi_string(DONOR_MENU_TGI),
            'resources': [{'tgi': tgi_string(key), 'bytes': len(resources[key]),
                           'sha256': hashlib.sha256(resources[key]).hexdigest()} for key in sorted(expected)],
            'in_game_menu_tested': False}
