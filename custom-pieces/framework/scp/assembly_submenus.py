"""Nest independent assembly cycle buttons without exposing their components.

Submenus DLL's documented top-level IDs are Highway 0x31 and Rail 0x29.
The cycle targets and RUL0 families remain the separate assembly menu's work.
Source: https://github.com/memo33/submenus-dll#information-for-modders
"""
from .catalog import number
from .dbpf import encode_exemplar, exemplar, require
from .menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
from .menu_experiment_resources import (
    ITEM_BUTTON_CLASS, ITEM_SUBMENU_PARENT_ID, _definition, _ltext,
    _new_button, _props, _set, _validate_icon)

PARENT_IDS = {'highway': 0x31, 'high-speed-rail': 0x29}
PREFIXES = (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)


def _native_cycle(record, iid, domain):
    props = _props(record)
    require(props.get(0x10, {}).get('values') == [40]
            and props.get(0x8A2602B8, {}).get('values') == [iid]
            and len(props.get(0x8A2602BB, {}).get('values', [])) == 1,
            'Assembly submenu requires an actual network cycle exemplar')
    selector, other, value = (0x4005, 0x4001, 0) if domain == 'highway' else (0x4001, 0x4005, 1)
    require(props.get(selector, {}).get('values') == [value] and other not in props,
            'Assembly cycle differs from its native domain menu')
    require(ITEM_BUTTON_CLASS not in props and ITEM_SUBMENU_PARENT_ID not in props,
            'Assembly cycle already belongs to a submenu')
    return props


def _groups(groups, domain):
    require(domain in PARENT_IDS, 'Unsupported assembly submenu domain')
    require(isinstance(groups, list), 'Assembly submenus need an ordered group list')
    result, parents, children = [], set(), set()
    for row in groups:
        require(isinstance(row, dict) and set(row) == {'definition', 'cycle_ids'},
                'Malformed assembly submenu group')
        definition = _definition(row['definition'], 'cycle_submenu', domain)
        require(set(definition) == {'id', 'order', 'title', 'description'},
                'Assembly submenu presentation fields differ')
        ids = row['cycle_ids']
        require(isinstance(ids, list) and ids, 'Assembly submenu needs at least one cycle button')
        ids = [number(value) if isinstance(value, str) else value for value in ids]
        require(all(type(value) is int and 0 < value <= 0xffffffff for value in ids)
                and len(set(ids)) == len(ids) and not set(ids) & children,
                'Assembly submenu has duplicate or invalid cycle buttons')
        require(definition['id'] not in parents, 'Duplicate assembly submenu presentation')
        parents.add(definition['id']); children.update(ids)
        result.append((definition, ids))
    require(not parents & children, 'Assembly submenu overlaps an assembly cycle button')
    return result


def build_resources(source, groups, *, domain):
    """Add one class-1 parent per group and class-2 membership to its cycles."""
    definitions = _groups(groups, domain)
    result = dict(source)
    for definition, children in definitions:
        iid = definition['id']
        require(all((*prefix, iid) not in source for prefix in PREFIXES),
                'Assembly submenu presentation collides with a source resource')
        for child in children:
            require(all((*prefix, child) in source for prefix in PREFIXES),
                    'Assembly submenu needs each complete cycle presentation')
            record = exemplar(source[*MENU_EXEMPLAR, child])
            _native_cycle(record, child, domain)
            _set(record, ITEM_SUBMENU_PARENT_ID, [iid])
            _set(record, ITEM_BUTTON_CLASS, [2])
            result[*MENU_EXEMPLAR, child] = encode_exemplar(record)
        template = exemplar(source[*MENU_EXEMPLAR, children[0]])
        additions = _new_button(template, definition, kind='submenu')
        record = exemplar(additions[*MENU_EXEMPLAR, iid])
        _set(record, ITEM_SUBMENU_PARENT_ID, [PARENT_IDS[domain]])
        additions[*MENU_EXEMPLAR, iid] = encode_exemplar(record)
        result.update(additions)
    report = validate_resources(result, source, groups, domain=domain)
    return result, report


def validate_resources(resources, source, groups, *, domain):
    """Independently inspect saved exemplar properties and complete resources."""
    definitions = _groups(groups, domain)
    additions = {(*prefix, definition['id']) for definition, _ in definitions for prefix in PREFIXES}
    changed = {(*MENU_EXEMPLAR, iid) for _, children in definitions for iid in children}
    require(not additions & source.keys() and resources.keys() == source.keys() | additions,
            'Assembly submenu resource closure differs')
    require(all(resources[key] == source[key] for key in source.keys() - changed),
            'Assembly submenu changed an unrelated presentation resource')
    edited = {0x20, 0x8A2602B8, 0x8A2602B9, 0x8A2602BB, 0x8A416A99, 0xCA416AB5}
    rows = []
    for definition, children in definitions:
        iid = definition['id']
        for child in children:
            before, after = exemplar(source[*MENU_EXEMPLAR, child]), exemplar(resources[*MENU_EXEMPLAR, child])
            original, actual = _native_cycle(before, child, domain), _props(after)
            require(after['parent'] == before['parent']
                    and list(actual) == [*original, ITEM_SUBMENU_PARENT_ID, ITEM_BUTTON_CLASS]
                    and all(actual[key] == value for key, value in original.items()),
                    'Assembly submenu changed a cycle target or native property')
            require(actual[ITEM_SUBMENU_PARENT_ID]['values'] == [iid]
                    and actual[ITEM_BUTTON_CLASS]['values'] == [2],
                    'Assembly cycle has the wrong submenu parent or class')
            require(all(actual[prop]['type'] == '0x0300' and actual[prop]['key_type'] == '0x0000'
                        and actual[prop]['repetitions'] is None
                        for prop in (ITEM_SUBMENU_PARENT_ID, ITEM_BUTTON_CLASS)),
                    'Assembly cycle submenu property encoding differs')
        template = exemplar(source[*MENU_EXEMPLAR, children[0]])
        original = _props(template)
        record = exemplar(resources[*MENU_EXEMPLAR, iid]); actual = _props(record)
        require(record['parent'] == template['parent']
                and list(actual) == [*original, ITEM_SUBMENU_PARENT_ID, ITEM_BUTTON_CLASS],
                'Assembly submenu changed the native parent or property order')
        require(all(actual[key] == value for key, value in original.items() if key not in edited),
                'Assembly submenu changed a retained native property')
        expected = {0x20: definition['title'], 0x8A2602B8: [iid],
                    0x8A2602B9: [definition['order']], 0x8A2602BB: [iid],
                    0x8A416A99: [*TITLE, iid], 0xCA416AB5: [*DESCRIPTION, iid],
                    ITEM_SUBMENU_PARENT_ID: [PARENT_IDS[domain]], ITEM_BUTTON_CLASS: [1]}
        require(all(actual[key]['values'] == value for key, value in expected.items()),
                'Assembly submenu identity, parent, class, order, or text differs')
        require(all(actual[key][field] == original[key][field]
                    for key in edited for field in ('type', 'key_type')),
                'Assembly submenu changed native property encoding')
        require(all(actual[prop]['type'] == '0x0300' and actual[prop]['key_type'] == '0x0000'
                    and actual[prop]['repetitions'] is None
                    for prop in (ITEM_SUBMENU_PARENT_ID, ITEM_BUTTON_CLASS)),
                'Assembly submenu property encoding differs')
        require(resources[*TITLE, iid] == _ltext(definition['title'])
                and resources[*DESCRIPTION, iid] == _ltext(definition['description']),
                'Assembly submenu localized text differs')
        _validate_icon(resources[*ICON, iid], 'submenu')
        rows.append({'button_id': f'{iid:08x}', 'parent_id': f'{PARENT_IDS[domain]:08x}',
                     'assembly_cycle_ids': [f'{child:08x}' for child in children]})
    return {'schema_version': 1, 'submenus': rows, 'submenus_dll_required': bool(rows),
            'assembly_cycle_targets_preserved': True, 'in_game_menu_tested': False}
