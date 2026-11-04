"""Shared SCP > Pieces / Assemblies presentation for migrated native menus.

Folder and child exemplar properties follow the Submenus DLL modding reference:
https://github.com/memo33/submenus-dll#information-for-modders
"""
from io import BytesIO

from .assembly_submenus import PARENT_IDS, PREFIXES, _native_cycle
from .catalog import number
from .dbpf import encode_exemplar, exemplar, require
from .menu import ICON, MENU_EXEMPLAR
from .menu_experiment_resources import (
    ITEM_BUTTON_CLASS, ITEM_SUBMENU_PARENT_ID, _assembly_label, _new_button,
    _props, _set, _validate_icon)
from .piece_menu_families import hidden_members

KEY = 'transport_menu'
CURRENT_VERSION = 2
LEGACY_ROOT_ORDER = 0xFFFFFFF4
# SC4 sorts network and folder order as signed 32-bit values. The NAM 50
# Highway entries audited for this layout start at -255.
HIGHWAY_ROOT_ORDER = 0xFFFFFE00
HIGHWAY = (0x6A47FEF4, 0x6A47FEF5, 0x6A47FEF6)
FOLDER_IDS = {'highway': HIGHWAY}
LEAVES = ('pieces', 'assemblies')


def plan(catalog, pieces):
    domains = {piece.get('domain', 'high-speed-rail') for piece in pieces}
    active = sorted(domain for domain in domains if
                    catalog.get('_domain_records', {}).get(domain, {}).get('scp_transport_menu', False))
    require(all(domain in FOLDER_IDS for domain in active), 'Unallocated SCP transportation folders')
    return {'schema_version': CURRENT_VERSION, 'domains': active} if active else None


def format_version(manifest):
    return manifest.get(KEY, {}).get('schema_version', CURRENT_VERSION)


def members(manifest, groups=()):
    """Get the visible piece and assembly buttons from the construction selection."""
    if KEY not in manifest:
        return {}
    marker = manifest[KEY]
    require(isinstance(marker, dict) and set(marker) == {'schema_version', 'domains'}
            and type(marker['schema_version']) is int and marker['schema_version'] in (1, CURRENT_VERSION),
            'Malformed SCP transportation menu declaration')
    domains = marker['domains']
    available = {piece.get('domain', 'high-speed-rail') for piece in manifest['pieces']}
    require(isinstance(domains, list) and domains
            and all(isinstance(domain, str) and domain in FOLDER_IDS and domain in available for domain in domains)
            and sorted(set(domains)) == domains, 'Invalid SCP transportation menu domains')
    roster = {domain: {leaf: [] for leaf in LEAVES} for domain in domains}
    hidden = hidden_members(manifest['pieces']) | {
        piece['id'] for _, _, pieces in groups for piece in pieces}
    for piece in manifest['pieces']:
        if piece.get('domain') in roster and piece['id'] not in hidden:
            roster[piece['domain']]['pieces'].append(number(piece['menu']['id']))
    for layout, _, pieces in groups:
        domain = pieces[0].get('domain')
        if domain in roster:
            require('cycle_submenu' not in layout and 'submenu' not in layout,
                    'SCP assemblies must sit directly in Assemblies')
            roster[domain]['assemblies'].append(number(layout['cycle_button']['id']))
    return roster


def require_current_source(catalog, manifest):
    current = plan(catalog, manifest['pieces'])
    require(current is None or current == manifest.get(KEY),
            'Rebuild the normal source with the current SCP transportation folders before preparing assemblies')


def check_ids(roster, used_ids, new_ids=()):
    require(not {key[2] for key in folder_keys(roster)} & (set(used_ids) | set(new_ids)),
            'SCP transportation folder identifiers collide with existing content')


def _icon(label):
    from PIL import Image, ImageDraw, ImageOps

    strip = Image.new('RGBA', (176, 44))
    for state in range(4):
        image = Image.new('RGBA', (44, 44))
        draw = ImageDraw.Draw(image)
        edge = ((70, 151, 162), (70, 151, 162), (226, 239, 240), (255, 255, 255))[state]
        background = ((16, 32, 40), (16, 32, 40), (68, 95, 105), (28, 60, 70))[state]
        draw.rounded_rectangle((1, 1, 42, 42), radius=5, fill=background, outline=edge, width=2)
        draw.rounded_rectangle((11, 13, 32, 27), radius=2, fill=(65, 145, 154), outline=edge)
        draw.rectangle((12, 10, 21, 14), fill=(65, 145, 154))
        draw.line((13, 10, 20, 10), fill=edge)
        draw.line((15, 20, 28, 20), fill=edge)
        _assembly_label(draw, label, (45 - 4 * len(label)) // 2, 32, (248, 253, 253))
        if state == 0:
            alpha = image.getchannel('A')
            image = ImageOps.grayscale(image).convert('RGBA')
            image.putalpha(alpha)
        strip.paste(image, (44 * state, 0))
    output = BytesIO()
    strip.save(output, format='PNG', optimize=False)
    return output.getvalue()


def _entries(roster):
    require(isinstance(roster, dict) and roster.keys() <= FOLDER_IDS.keys(),
            'Unsupported SCP transportation menu')
    for domain, leaves in sorted(roster.items()):
        require(isinstance(leaves, dict) and leaves.keys() == set(LEAVES)
                and all(isinstance(ids, list) for ids in leaves.values()),
                'SCP transportation menu needs Pieces and Assemblies rosters')
        root, pieces, assemblies = FOLDER_IDS[domain]
        children = [(iid, parent) for leaf, parent in zip(LEAVES, (pieces, assemblies))
                    for iid in leaves[leaf]]
        ids = [iid for iid, _ in children]
        require(ids and all(type(iid) is int and 0 < iid <= 0xFFFFFFFF for iid in ids)
                and len(set(ids)) == len(ids) and not set(ids) & set(FOLDER_IDS[domain]),
                'Missing, invalid, or repeated SCP transportation menu buttons')
        folders = ((root, PARENT_IDS[domain], 'SCP', 'Simon’s Custom Pieces for this transportation network.'),
                   (pieces, root, 'Pieces', 'Individual SCP pieces and alternative piece families.'),
                   (assemblies, root, 'Assemblies', 'SCP assemblies; use Tab to cycle through their components.'))
        yield domain, folders, children


def _native_buttons(resources, domain):
    selector = {'highway': 0x4005}[domain]
    native = set()
    for key, raw in resources.items():
        if key[:2] != MENU_EXEMPLAR:
            continue
        props = _props(exemplar(raw))
        if selector in props:
            native.add(key[2])
        parent = props.get(ITEM_SUBMENU_PARENT_ID, {}).get('values', [])
        require(not any(iid in FOLDER_IDS[domain] for iid in parent),
                'A source button already points into the SCP transportation folders')
    return native


def folder_keys(roster):
    return {(*prefix, iid) for _, folders, _ in _entries(roster)
            for iid, *_ in folders for prefix in PREFIXES}


def arrange(source, roster, *, version=CURRENT_VERSION, folder_source=None):
    """Return a nested menu while preserving every existing leaf identity."""
    require(type(version) is int and version in (1, CURRENT_VERSION), 'Unknown SCP menu format')
    result = dict(source)
    for domain, folders, children in _entries(roster):
        require(_native_buttons(source, domain) == {iid for iid, _ in children},
                'Unlisted or missing native SCP transportation buttons')
        for iid, parent in children:
            require(all((*prefix, iid) in source for prefix in PREFIXES),
                    'SCP menu button presentation is incomplete')
            key = (*MENU_EXEMPLAR, iid)
            record = exemplar(source[key])
            _native_cycle(record, iid, domain)
            _set(record, ITEM_SUBMENU_PARENT_ID, [parent])
            _set(record, ITEM_BUTTON_CLASS, [2])
            result[key] = encode_exemplar(record)
        template = exemplar(source[*MENU_EXEMPLAR, min(iid for iid, _ in children)])
        for offset, (iid, parent, title, description) in enumerate(folders):
            require(all((*prefix, iid) not in result for prefix in PREFIXES),
                    'SCP folder ID collides with an existing menu resource')
            icon = _icon(title.upper())
            if folder_source is not None:
                icon_key = (*ICON, iid)
                require(icon_key in folder_source, 'SCP source folder icon is missing')
                _validate_icon(folder_source[icon_key], 'submenu', icon)
                icon = folder_source[icon_key]
            order = LEGACY_ROOT_ORDER + offset
            if offset == 0 and version == CURRENT_VERSION:
                order = HIGHWAY_ROOT_ORDER
            additions = _new_button(template, {'id': iid, 'order': order,
                                              'title': title, 'description': description},
                                    kind='submenu', icon=icon)
            key = (*MENU_EXEMPLAR, iid)
            record = exemplar(additions[key])
            _set(record, ITEM_SUBMENU_PARENT_ID, [parent])
            additions[key] = encode_exemplar(record)
            result.update(additions)
    return result


def restore(resources, roster, *, version=CURRENT_VERSION):
    """Validate the saved hierarchy and recover plain entries for existing validators."""
    plain = dict(resources)
    icons = {}
    for domain, folders, children in _entries(roster):
        for iid, *_ in folders:
            require(all((*prefix, iid) in plain for prefix in PREFIXES), 'SCP folder presentation is incomplete')
            for prefix in PREFIXES:
                raw = plain.pop((*prefix, iid))
                if prefix == ICON:
                    icons[(*prefix, iid)] = raw
        for iid, _ in children:
            key = (*MENU_EXEMPLAR, iid)
            require(key in plain, 'SCP menu child exemplar is missing')
            record = exemplar(plain[key])
            record['properties'] = [prop for prop in record['properties']
                                    if int(prop['id'], 16) not in (ITEM_SUBMENU_PARENT_ID, ITEM_BUTTON_CLASS)]
            plain[key] = encode_exemplar(record)
    expected = arrange(plain, roster, version=version)
    require(expected.keys() == resources.keys()
            and all(resources[key] == expected[key] for key in expected.keys() - icons.keys()),
            'Saved SCP folder or child parent, class, order, or presentation differs')
    for key, raw in icons.items():
        _validate_icon(raw, 'submenu', expected[key])
    return plain
