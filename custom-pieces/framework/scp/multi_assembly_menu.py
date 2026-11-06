"""Independent assembly cycles from one verified, disjoint normal build.

Menu presentations, generated RUL0 ordering, and explicitly selected
construction aliases are derived from the verified original build.
The original build and all per-assembly inputs remain frozen verification
proof; no completed menu candidate is used as an intermediate source.
"""
from copy import deepcopy
from functools import partial
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

from .catalog import number, safe_relative
from .dbpf import exemplar, pack_dbpf, require
from .menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
from .piece_menu_families import hidden_members
from . import menu_experiment as single
from . import transport_menu

KIND = 'assembly-disjoint-button-cycles-v1'
PROOF = 'docs/assembly-menus-source'
GUIDE = 'docs/assembly-menus/README.md'
CHECKS = 'docs/assembly-menus/game-checks.json'
DOMAINS = ('highway', 'high-speed-rail')
PREFIXES = (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)


def _root(layout, piece):
    return layout.get('_alias_roots', {}).get(piece['id'], number(piece['puzzle_id']))


def _alias_targets(layout, pieces):
    return {piece['id']: (number(piece['menu']['id']) & 0xffff0000) | _root(layout, piece)
            for piece in pieces if piece['id'] in layout.get('_alias_roots', {})}


def _alias_pairs(groups):
    pairs = []
    for layout, _, pieces in groups:
        sources = {piece['id']: number(piece['puzzle_id']) for piece in pieces}
        pairs.extend((sources[piece['id']], _root(layout, piece)) for piece in pieces
                     if piece['id'] in layout.get('_alias_roots', {}))
        pairs.extend((sources[row['piece_id']], number(row['puzzle_id']))
                     for row in layout.get('_terminals', ()))
    return pairs


def _cycle_roots(layout, pieces):
    return [_root(layout, piece) for piece in pieces] + [number(row['puzzle_id'])
                for row in layout.get('_terminals', ())]


def _terminal_bodies(groups, *, verify=False):
    from .providers import domain_module
    result = {}
    for layout, _, pieces in groups:
        if terminals := layout.get('_terminals'):
            by_id = {piece['id']: piece for piece in pieces}
            provider = domain_module(pieces[0], 'trumpet_terminals')
            for row in terminals:
                root, piece_id = number(row['puzzle_id']), row['piece_id']
                result[root] = (partial(provider.verify_terminal_body, piece_id, row['helper_edge'], piece=by_id[piece_id])
                                if verify else partial(provider.terminal_body, piece_id, row['helper_edge']))
    return result


def _consumed(layout, pieces):
    return [piece for piece in pieces if piece['id'] not in layout.get('component_aliases', {})]


def _scene(scene, layout):
    if 'assembly_variant' not in layout:
        return scene
    variant = scene.get('alternatives', {}).get(layout['assembly_variant'])
    require(isinstance(variant, dict) and isinstance(variant.get('placements'), list)
            and variant['placements'], 'Assembly variant has no declared placement plan')
    return {**scene, 'placements': variant['placements']}


def _alias_roots(layout_id, layout, pieces, reservations):
    requested = layout.get('component_aliases', {})
    require(isinstance(reservations, dict) and set(reservations) == set(requested.values()),
            'Missing or unexpected assembly alias reservations')
    require(set(requested) <= {piece['id'] for piece in pieces}, 'Alias source is outside this assembly layout')
    roots = {}
    for piece_id, name in requested.items():
        row = reservations[name]
        require(isinstance(row, dict) and set(row) == {'piece_id', 'layout_id', 'puzzle_id'}
                and row['piece_id'] == piece_id and row['layout_id'] == layout_id
                and isinstance(row['puzzle_id'], str) and re.fullmatch(r'[0-9a-f]{4}', row['puzzle_id']),
                'Assembly alias reservation differs from the selected component or layout')
        roots[piece_id] = number(row['puzzle_id'])
    return roots


def _terminal_components(layout_id, layout, scene, pieces, reservations):
    from .providers import domain_module
    requested = layout['terminal_components']
    approaches = scene.get('terminal_approaches')
    require(isinstance(approaches, dict) and approaches.keys() == requested.keys(),
            'Assembly terminal selections must match the scene terminal placements')
    require(isinstance(reservations, dict) and set(reservations) == set(requested.values()),
            'Missing or unexpected assembly terminal reservations')
    placements = domain_module(pieces[0], 'trumpet_terminals').terminal_placements(scene)
    components = []
    for index, (label, placement) in enumerate(placements.items(), len(pieces) + 1):
        identifier = requested[label]
        row = reservations[identifier]
        require(isinstance(row, dict) and set(row) == {'piece_id', 'layout_id', 'puzzle_id', 'placement_id'}
                and row['piece_id'] == placement['piece_id'] and row['layout_id'] == layout_id
                and row['placement_id'] == label and isinstance(row['puzzle_id'], str)
                and re.fullmatch(r'[0-9a-f]{4}', row['puzzle_id']),
                'Assembly terminal reservation differs from the selected placement or layout')
        approach = approaches[label]
        origin = placement.get('display_origin_tiles_en')
        rotation = placement.get('rotation_degrees_ccw')
        require(isinstance(approach, dict) and approach.get('helper_edge') in ('north', 'south', 'west')
                and approach.get('arm') in ('S', 'E', 'W', 'N')
                and isinstance(approach.get('helper_cell_xy'), list)
                and len(approach['helper_cell_xy']) == 2
                and all(type(value) is int for value in approach['helper_cell_xy'])
                and isinstance(origin, list) and len(origin) == 2
                and all(type(value) is int or type(value) is float and value.is_integer() for value in origin)
                and type(rotation) is int and rotation in (0, 90, 180, 270),
                'Assembly terminal needs an exact cardinal helper, grid position, and rotation')
        components.append({'id': identifier, 'piece_id': row['piece_id'], 'puzzle_id': row['puzzle_id'],
                           'placement_id': label, 'cycle_position': index, 'arm': approach['arm'],
                           'helper_edge': approach['helper_edge'], 'helper_cell_xy': approach['helper_cell_xy'],
                           'origin_cell_xy': list(map(int, origin)), 'rotation_degrees_ccw': rotation})
    return components


def _terminal_targets(layout, pieces):
    menu_prefixes = {piece['id']: number(piece['menu']['id']) & 0xffff0000 for piece in pieces}
    return {menu_prefixes[row['piece_id']] | number(row['puzzle_id']) for row in layout.get('_terminals', ())}


def _groups(base, bundle):
    require(isinstance(bundle, dict) and type(bundle.get('schema_version')) is int
            and bundle['schema_version'] in (1, 2)
            and set(bundle) == ({'schema_version', 'domain_id', 'groups'}
                                if bundle['schema_version'] == 1 else {'schema_version', 'groups'}),
            'Malformed disjoint assembly layout bundle')
    legacy = bundle['schema_version'] == 1
    if legacy:
        require(isinstance(bundle['domain_id'], str) and bundle['domain_id'] in DOMAINS,
                'Unsupported assembly menu domain')
    rows = bundle['groups']
    require(isinstance(rows, list) and rows, 'Need at least one assembly layout')
    result, identifiers, assemblies, buttons, members, menu_ids, states = [], set(), set(), set(), set(), set(), set()
    canonical_roots = {number(piece['puzzle_id']) for piece in base['pieces']}
    canonical_menu_ids = {number(piece['menu']['id']) for piece in base['pieces']}
    from .menu_experiment_resources import member_domain
    for row in rows:
        fields = {'layout_id', 'layout', 'scene'} if legacy else {'domain_id', 'layout_id', 'layout', 'scene'}
        require(isinstance(row, dict) and set(row) in (fields, fields | {'alias_reservations'})
                and isinstance(row['layout_id'], str) and row['layout_id']
                and isinstance(row['scene'], dict),
                'Invalid or repeated assembly menu layout')
        domain = bundle['domain_id'] if legacy else row['domain_id']
        require(isinstance(domain, str) and domain in DOMAINS, 'Unsupported assembly menu domain')
        identity = row['layout_id'] if legacy else (domain, row['layout_id'])
        require(identity not in identifiers, 'Invalid or repeated assembly menu layout')
        identifiers.add(identity)
        layout = single._layout(row['layout'], domain)
        scene = _scene(row['scene'], layout)
        if 'variant_label' in layout['cycle_button']:
            from .assembly_presentation import validate_cycle_title
            validate_cycle_title(scene, layout['cycle_button'])
        require('submenu' not in layout, 'Disjoint assembly menus do not accept submenu layouts')
        assembly = (layout['assembly_id'], layout.get('assembly_variant'))
        require(assembly not in assemblies, 'Repeated assembly in menu selection')
        assemblies.add(assembly)
        button = number(layout['cycle_button']['id'])
        require(button not in buttons, 'Duplicate assembly presentation identifier')
        buttons.add(button)
        pieces = single._selected(base, scene)
        require(member_domain(pieces) == domain, 'Assembly member domain differs from menu selection')
        require(('terminal_components' in layout) == ('terminal_approaches' in scene),
                'Assembly terminal selections and scene approaches must be declared together')
        reservations = row.get('alias_reservations', {})
        if 'terminal_components' in layout:
            aliases = {}
            layout['_terminals'] = _terminal_components(row['layout_id'], layout, scene, pieces, reservations)
        else:
            aliases = _alias_roots(row['layout_id'], layout, pieces, reservations)
            if aliases:
                layout['_alias_roots'] = aliases
        alias_targets = _alias_targets(layout, pieces)
        for piece in pieces:
            root = _root(layout, piece)
            menu_id = alias_targets.get(piece['id'], number(piece['menu']['id']))
            rotations = {root + turn * 0x10000 for turn in range(8)}
            if piece['id'] in aliases:
                require(root != 0 and root not in canonical_roots and menu_id not in canonical_menu_ids,
                        'Assembly alias collides with an existing piece')
            else:
                require(piece['id'] not in members, 'Assembly menu groups overlap in a member')
                members.add(piece['id'])
            require(menu_id not in menu_ids and not rotations & states,
                    'Assembly menu groups overlap in a member, menu identifier, or construction state')
            menu_ids.add(menu_id); states.update(rotations)
        terminal_targets = _terminal_targets(layout, pieces)
        for terminal in layout.get('_terminals', ()):
            root = number(terminal['puzzle_id'])
            rotations = {root + turn * 0x10000 for turn in range(8)}
            require(root and root not in canonical_roots and not rotations & states,
                    'Assembly terminal collides with an existing construction state')
            states.update(rotations)
        require(not terminal_targets & (menu_ids | canonical_menu_ids),
                'Assembly terminal collides with an existing menu identifier')
        menu_ids.update(terminal_targets)
        result.append((layout, scene, pieces))
    require(len(result) >= 2 or bool(_alias_pairs(result)), 'Multiple assembly menus need at least two layouts')
    require(not buttons & menu_ids, 'Assembly presentation identifier overlaps a member button')
    submenus = _submenus(result)
    submenu_ids = {number(row['definition']['id']) for row in submenus}
    require(not submenu_ids & (buttons | menu_ids),
            'Assembly submenu presentation overlaps a member or assembly button')
    return result


def _submenus(groups):
    """Coalesce identical explicit parent definitions in first-use order."""
    from .menu_experiment_resources import member_domain
    definitions, domains, result = {}, {}, []
    for layout, _scene, pieces in groups:
        if 'cycle_submenu' not in layout:
            continue
        definition = layout['cycle_submenu']
        iid = number(definition['id'])
        normalized = {**definition, 'id': f'{iid:08x}',
                      'order': f'{number(definition["order"]):08x}'}
        if iid not in definitions:
            definitions[iid] = {'definition': normalized, 'cycle_ids': []}
            domains[iid] = member_domain(pieces)
            result.append(definitions[iid])
        require(definitions[iid]['definition'] == normalized and domains[iid] == member_domain(pieces),
                'Repeated assembly submenu identifier has conflicting definitions')
        definitions[iid]['cycle_ids'].append(layout['cycle_button']['id'])
    return result


def _domain_submenus(groups):
    """Keep native menu parents separate while checking identifiers globally."""
    from .menu_experiment_resources import member_domain
    _submenus(groups)
    domains = list(dict.fromkeys(member_domain(pieces) for layout, _scene, pieces in groups
                                 if 'cycle_submenu' in layout))
    return [(domain, _submenus([group for group in groups if member_domain(group[2]) == domain]))
            for domain in domains]


def _transform(base, controller, menu, bundle, icons):
    from .build import RUL0, NETWORK_INI
    from .adaptive_network import RUL1
    from .piece_menu_families import with_feature_sequence_preserving_families as with_feature_sequence
    from .verify import strict_dbpf
    from .menu_experiment_resources import build_menu_experiment_resources
    from .assembly_aliases import add_aliases
    groups = _groups(base, bundle)
    original = strict_dbpf(controller)
    from .native_approaches import needs_rul1
    require(set(original) == {RUL0, NETWORK_INI} | ({RUL1} if needs_rul1(base['overlay']) else set()),
            'Original multi-assembly controller resource closure differs')
    aliases = _alias_pairs(groups)
    source_rules, source_composition = add_aliases(original[RUL0], base['overlay']['rul0'], aliases,
                                                  terminal_bodies=_terminal_bodies(groups))
    roots = [_cycle_roots(layout, pieces) for layout, _, pieces in groups]
    changed, composition = with_feature_sequence(source_rules, source_composition,
                                                  [root for group in roots for root in group])
    insertion = composition['ordering_insertion']
    first_roots = {group[0] for group in roots}
    lines = []
    for line in insertion.splitlines(keepends=True):
        match = re.match(r'^(\s*)(RotationRing|AddTypes)(\s*=\s*)([0-9a-fA-Fx]+)', line)
        if match and int(match[4], 16) in first_roots:
            line = line[:match.start(2)] + 'RotationRing' + line[match.end(2):]
        lines.append(line)
    updated = ''.join(lines)
    changed = changed.replace(insertion.encode('ascii'), updated.encode('ascii'), 1)
    composition.pop('feature_sequence')
    composition.update(ordering_insertion=updated, feature_sequences={
        'schema_version': 1, 'groups': roots, 'previous_ordering_insertion': base['overlay']['rul0']['ordering_insertion'],
        'previous_controller_sha256': single._sha(original[RUL0]), 'shared_between_assemblies': False})
    nested_source = strict_dbpf(menu)
    version = transport_menu.format_version(base)
    plain_source = transport_menu.restore(nested_source, transport_menu.members(base), version=version)
    resources = plain_source
    audits = []
    require(len(icons) == len(groups), 'Missing assembly menu icon')
    for (layout, _scene, pieces), icon in zip(groups, icons):
        targets = _alias_targets(layout, pieces)
        cycle = {**layout['cycle_button'], 'target_id': targets.get(pieces[0]['id'], pieces[0]['menu']['id'])}
        built, audit = build_menu_experiment_resources(plain_source if targets else resources, pieces,
            cycle_button=cycle, cycle_icon=icon, expected_cycle_icon=icon, placement_aliases=targets)
        if targets:
            resources = dict(resources)
            for piece in _consumed(layout, pieces):
                for prefix in PREFIXES:
                    del resources[*prefix, number(piece['menu']['id'])]
            for prefix in PREFIXES:
                key = (*prefix, number(cycle['id']))
                resources[key] = built[key]
        else:
            resources = built
        audits.append(audit)
    if submenus := _submenus(groups):
        from .assembly_submenus import build_resources
        if bundle['schema_version'] == 1:
            resources, audit = build_resources(resources, submenus, domain=bundle['domain_id'])
            audits.append(audit)
        else:
            for domain, domain_submenus in _domain_submenus(groups):
                resources, audit = build_resources(resources, domain_submenus, domain=domain)
                audits.append({'domain_id': domain, **audit})
    resources = transport_menu.arrange(
        resources, transport_menu.members(base, groups), version=version, folder_source=nested_source)
    return pack_dbpf({**original, RUL0: changed}), pack_dbpf(resources), composition, audits


def _documents(groups, base):
    from .content import markdown_metadata
    from .menu_experiment_resources import member_domain
    nested_domains = transport_menu.members(base)
    first_domain = member_domain(groups[0][2])
    network_menu = 'Highways' if first_domain == 'highway' else 'Rail'
    if first_domain in nested_domains:
        network_menu += ' → SCP → Assemblies'
    mixed = len({member_domain(pieces) for _layout, _scene, pieces in groups}) > 1
    opening = ('1. Open **Transportation**, then choose **Rail** or **Highways** as listed for the assembly below.'
               if mixed else f'1. Open **Transportation → {network_menu}**.')
    submenus = _submenus(groups)
    chapters = [('Placement', '1-placement')]
    chapters += [(layout['cycle_button']['title'], f'{index}-{layout["assembly_id"]}')
                 for index, (layout, _, _) in enumerate(groups, 2)]
    chapters += [('Verification and observations', f'{len(groups) + 2}-verification')]
    navigation = ' · '.join(f'[{index}. {title}](#{anchor})' for index, (title, anchor) in enumerate(chapters, 1))
    lines = [markdown_metadata('Assembly component menus',
        'Select separately verified assembly component cycles from one combined plugin.',
        'Players and testers', 'guide').rstrip(), '', '# Assembly component menus', '',
        '<!-- BEGIN DOCUMENT NAVIGATION -->', navigation, '<!-- END DOCUMENT NAVIGATION -->', '',
        '<a id="1-placement"></a>', '', '## 1. Placement', '',
        'Each assembly has its own button. Each click places one reusable component. Use the owning assembly placement plan to choose its position and orientation. Actual game behavior remains unverified.', '',
        opening,
        '2. Click one of the exact assembly buttons listed below. It starts on that assembly’s first component.',
        '3. Press **Tab** for the next component, or **Shift+Tab** for the previous component. Cycling stays within the selected assembly.',
        '4. Press **Home** or **End** to rotate the current component, then click clear terrain to place it.',
        '5. Press **Escape** to cancel. Select another assembly button to begin its separate component cycle.', '']
    if submenus:
        lines += ['Assemblies assigned to a submenu appear inside the named submenu below. Open that submenu, then choose its assembly button. The Submenus DLL, SC4ResourceLoadingHooks DLL, and `submenu-essentials.dat` must be installed and active for this nested presentation. Software verification does not establish runtime DLL loading.', '']
    cases = []
    for index, (layout, _scene, pieces) in enumerate(groups, 2):
        domain = member_domain(pieces)
        nested = domain in nested_domains
        network_menu = 'Highways' if domain == 'highway' else 'Rail'
        if nested:
            network_menu += ' → SCP → Assemblies'
        lines += [f'<a id="{index}-{layout["assembly_id"]}"></a>', '',
                  f'## {index}. ' + layout['cycle_button']['title'], '',
                  'Assembly: `' + layout['assembly_id'] + '`. The cycle follows this component order:', '']
        if 'cycle_submenu' in layout:
            lines += [f'Open **Transportation → {network_menu} → {layout["cycle_submenu"]["title"]}**, then click **{layout["cycle_button"]["title"]}**. Tab and Shift+Tab stay inside this assembly’s component cycle.', '']
        elif mixed or nested:
            lines += [f'Open **Transportation → {network_menu}**, then click **{layout["cycle_button"]["title"]}**. Tab and Shift+Tab stay inside this assembly’s component cycle.', '']
        lines += [f'{index}. {piece["name"]} (`{piece["id"]}`).' for index, piece in enumerate(pieces, 1)]
        terminals = layout.get('_terminals', ())
        base_by_id = {piece['id']: piece for piece in pieces}
        terminal_by_id = {terminal['id']: terminal for terminal in terminals}
        terminal_members = []
        for terminal in terminals:
            piece = base_by_id[terminal['piece_id']]
            label, direction = terminal['placement_id'], terminal['arm']
            title = f'{piece["name"]} — Native HSR starter for {label} ({direction})'
            x, y = terminal['origin_cell_xy']
            helper_x, helper_y = terminal['helper_cell_xy']
            turns = terminal['rotation_degrees_ccw']
            lines.append(f'{terminal["cycle_position"]}. {title} (`{terminal["id"]}`). Place the component at reference (X{x}, Y{y}), at {turns}° counterclockwise. Keep (X{helper_x}, Y{helper_y}) clear for the native starter tile. The component uses the same model as its ordinary selection.')
            terminal_members.append({'id': terminal['id'], 'name': title, 'domain': domain})
        lines += ['']
        if terminals:
            lines += ['The native starter is a NAM HSR track tile placed immediately outside the assembly. After placing each terminal selection, choose the **Monorail** tool and drag from the starter outward along the same track axis. Check that the new track takes on the HSR appearance, then test train travel in both directions.', '']
        for case in single._game_checks([*pieces, *terminal_members], single_button=True, nested=nested)['cases']:
            if terminal := terminal_by_id.get(case.get('piece_id')):
                case = {**case, 'piece_id': terminal['piece_id'], 'selection_id': terminal['id'],
                        'placement_id': terminal['placement_id'],
                        'description': (f'Reach cycle selection {terminal["cycle_position"]} for '
                                        f'{terminal["placement_id"]}, then place it at the reference and rotation '
                                        'listed in this guide. Confirm that the native starter tile appears.')}
            if 'cycle_submenu' in layout and case['id'] == 'single-assembly-entry':
                case = {**case, 'description': f'Transportation > {network_menu} > {layout["cycle_submenu"]["title"]} has exactly one button named {layout["cycle_button"]["title"]} for this assembly; no individual member buttons appear. Selecting this button and using Tab or Shift+Tab stays within its listed component cycle.'}
            key = layout['assembly_id'] + (':' + layout['assembly_variant'] if 'assembly_variant' in layout else '')
            cases.append({**case, 'id': key + ':' + case['id'],
                          'assembly_id': layout['assembly_id']})
    for row in submenus:
        domain = next(domain for domain, parents in _domain_submenus(groups)
                      if any(number(parent['definition']['id']) == number(row['definition']['id'])
                             for parent in parents))
        network_menu = 'Highways' if domain == 'highway' else 'Rail'
        cases.append({'id': 'submenu:' + row['definition']['id'],
                      'description': f'Transportation > {network_menu} shows {row["definition"]["title"]}; it opens and contains exactly the selected {len(row["cycle_ids"])} assembly buttons, each starting its own isolated component cycle.',
                      'status': 'unverified', 'observations': []})
    dependency = ('This candidate requires the Submenus DLL, SC4ResourceLoadingHooks DLL, and `submenu-essentials.dat` for its nested assembly menus.'
                  if submenus or nested_domains else 'This candidate does not require Submenus DLL.')
    lines += [f'<a id="{len(groups) + 2}-verification"></a>', '',
              f'## {len(groups) + 2}. Verification and observations', '',
              'The original source documents and archives are frozen under `../assembly-menus-source/`. All piece DATs are unchanged. ' + dependency + ' Building and packaging do not install anything.', '',
              'The [game-checks.json](game-checks.json) template lists pending checks separately for each assembly. Record explicit observations against the candidate manifest fingerprint, platform, game version, and NAM profile. Software checks do not approve menu activation, visible traffic, or save/reload behavior.', '']
    guide = '\n'.join(lines).encode('utf8')
    checks = single._json_bytes({'schema_version': 1, 'purpose': 'Frozen pending checks; no human observations.',
        'authority': 'Record explicit human observations separately against the candidate manifest fingerprint; preserve this template.',
        'environment_required': ['platform', 'game_version', 'NAM_profile'] + (['Submenus_DLL_version'] if nested_domains else []),
        'cases': cases})
    readme = ('Assembly component menus\nDEVELOPMENT BUILD — NOT GAME-TESTED\n'
              + ''.join(f'{layout["cycle_button"]["title"]}: {len(_cycle_roots(layout, pieces))} components\n'
                        for layout, _, pieces in groups)
              + 'Read docs/assembly-menus/README.md. Tab cycles within the selected assembly.\n'
              + 'Building and packaging do not install anything.\n').encode('utf8')
    return {GUIDE: guide, CHECKS: checks, 'README.txt': readme}


def _manifest(base, bundle, proof, controller, menu, composition, audits):
    require('menu_experiment' not in base, 'Cannot nest assembly menu candidates')
    result = deepcopy(base)
    folder = base['plugin_folder']
    changed = {f'{folder}/{single.CONTROLLER}': controller, f'{folder}/{single.MENU}': menu}
    result['files'] = [single._record(row['path'], changed[row['path']]) if row['path'] in changed else row
                       for row in deepcopy(base['files'])]
    groups = _groups(base, bundle)
    from .menu_experiment_resources import member_domain
    selection = [{**({'domain_id': member_domain(pieces)} if bundle['schema_version'] == 2 else {}),
                  'assembly_id': layout['assembly_id'], 'member_ids': [piece['id'] for piece in pieces],
                  **({'assembly_variant': layout['assembly_variant'],
                      'component_aliases': layout['component_aliases']} if 'assembly_variant' in layout else {}),
                  **({'terminal_components': layout['_terminals']} if '_terminals' in layout else {})}
                 for layout, _, pieces in groups]
    result['menu_experiment'] = {'kind': KIND, 'schema_version': bundle['schema_version'], 'assemblies': selection,
        'source_inputs': proof, 'construction_aliases_created': bool(_alias_pairs(groups)), 'in_game_menu_tested': False}
    result['assembly_selections'] = deepcopy(selection)
    result['overlay']['rul0'] = composition
    result['menu_audit'] = audits
    result['source_provenance'] = {'kind': 'frozen-verified-piece-build', 'manifest': proof['manifest']['path'],
                                   'documentation_root': PROOF + '/documentation'}
    result['installed'] = result['in_game_tested'] = False
    result['release']['public_release_ready'] = False
    result['release']['blocked'] = list(dict.fromkeys([*result['release'].get('blocked', []),
        'Assembly menu behavior requires explicit in-game observations; public release is blocked.']))
    documents = [{**row, 'path': PROOF + '/documentation/' + row['path']} for row in base.get('documentation', [])]
    additions = [*(proof[key] for key in sorted(proof)),
                 *(single._record(name, raw) for name, raw in _documents(groups, base).items())]
    require(len({row['path'] for row in documents + additions}) == len(documents + additions),
            'Multiple assembly proof paths overlap source documentation')
    result['documentation'] = documents + additions
    return result


def _actual(base, bundle, old_controller, old_menu, controller, menu, composition):
    """Independently inspect the complete original-to-final transformation."""
    from .build import RUL0, NETWORK_INI
    from .adaptive_network import RUL1
    from .verify import strict_dbpf
    from .rul0 import _ring
    from .menu_experiment_resources import member_domain
    from .assembly_aliases import verify_aliases
    groups = _groups(base, bundle)
    old_c, new_c = strict_dbpf(old_controller), strict_dbpf(controller)
    require(set(old_c) == set(new_c) and all(old_c[key] == new_c[key] for key in old_c if key != RUL0),
            'Multiple assembly menus changed non-RUL0 controller resources')
    aliases = _alias_pairs(groups)
    original_composition = base['overlay']['rul0']
    old_insert = original_composition['ordering_insertion'].encode('ascii')
    new_insert = composition['ordering_insertion'].encode('ascii')
    if aliases:
        verify_aliases(old_c[RUL0], original_composition, new_c[RUL0], composition, aliases,
                       terminal_bodies=_terminal_bodies(groups, verify=True))
    else:
        require(old_c[RUL0].count(old_insert) == 1 and new_c[RUL0] == old_c[RUL0].replace(old_insert, new_insert, 1),
                'Multiple assembly menus changed native bytes or construction definitions')
    def rows(raw):
        output = []
        for line in raw.decode('ascii').splitlines():
            match = re.fullmatch(r'\s*(RotationRing|AddTypes)\s*=\s*(.+)', line, re.I)
            if match:
                output.append((match[1].lower(), _ring('RotationRing=' + match[2])))
        return output
    original, actual = rows(old_insert), rows(new_insert)
    original.extend(('rotationring', [alias + turn * 0x10000 for turn in range(8)])
                    for _, alias in aliases)
    selections = [_cycle_roots(layout, pieces) for layout, _, pieces in groups]
    selected = {root for roots in selections for root in roots}
    by_root = {states[0]: states for _, states in original}
    require(len(by_root) == len(original) and all(root in by_root for root in selected), 'Invalid original rotation roots')
    first = min(index for index, (_, states) in enumerate(original) if states[0] in selected)
    expected = []
    for index, row in enumerate(original):
        if index == first:
            for roots in selections:
                expected += [('rotationring' if at == 0 else 'addtypes', by_root[root]) for at, root in enumerate(roots)]
        if row[1][0] not in selected:
            expected.append(row)
    require(actual == expected, 'Actual disjoint assembly cycles differ in membership, order, family, or rotation states')
    version = transport_menu.format_version(base)
    before = transport_menu.restore(strict_dbpf(old_menu), transport_menu.members(base), version=version)
    after = transport_menu.restore(strict_dbpf(menu), transport_menu.members(base, groups), version=version)
    prefixes = PREFIXES
    removed = {(*prefix, number(piece['menu']['id'])) for layout, _, pieces in groups
               for piece in _consumed(layout, pieces) for prefix in prefixes}
    added = {(*prefix, number(layout['cycle_button']['id'])) for layout, _, _ in groups for prefix in prefixes}
    submenus = _submenus(groups)
    added |= {(*prefix, number(row['definition']['id'])) for row in submenus for prefix in prefixes}
    require(not set(before) & added and set(after) == (set(before) - removed) | added,
            'Multiple assembly menu resource closure differs')
    require(all(before[key] == after[key] for key in set(before) - removed), 'An unrelated menu resource changed')
    for layout, _scene, pieces in groups:
        iid = number(layout['cycle_button']['id'])
        record = exemplar(after[*MENU_EXEMPLAR, iid])
        property_records = {number(prop['id'].removeprefix('0x')): prop
                            for prop in record['properties']}
        properties = {number(prop['id'].removeprefix('0x')): prop['values']
                      for prop in record['properties']}
        target = _alias_targets(layout, pieces).get(pieces[0]['id'], number(pieces[0]['menu']['id']))
        require(properties[0x8A2602BB] == [target]
                and properties[0x8A2602B8] == [iid] and properties[0x8A2602B9] == [number(layout['cycle_button']['order'])],
                'Assembly button has a wrong target, order, or submenu property')
        if 'cycle_submenu' in layout:
            require(properties.get(0x8A2602CA) == [number(layout['cycle_submenu']['id'])]
                    and properties.get(0x8A2602CC) == [2],
                    'Assembly cycle has the wrong parent submenu or network class')
        else:
            require(0x8A2602CA not in properties and 0x8A2602CC not in properties,
                    'Ungrouped assembly button unexpectedly belongs to a submenu')
        if member_domain(pieces) == 'highway':
            require(properties.get(0x4005) == [0] and 0x4001 not in properties, 'Assembly button left the Highways menu')
        elif bundle['schema_version'] == 2:
            # The actual NAM 50 Rail donor uses selector value 0; retained
            # historical fixtures use 1. Preserve the verified source's full
            # selector encoding and parent instead of inventing a new value.
            original = exemplar(before[*MENU_EXEMPLAR, number(pieces[0]['menu']['id'])])
            original_properties = {number(prop['id'].removeprefix('0x')): prop
                                   for prop in original['properties']}
            selector = original_properties.get(0x4001, {})
            require(selector.get('values') in ([0], [1]) and 0x4005 not in original_properties
                    and property_records.get(0x4001) == selector and 0x4005 not in properties
                    and record['parent'] == original['parent'], 'Assembly button left the Rail menu')
    if submenus:
        # Strip only the inspected additions from actual bytes, then use the
        # separate saved-resource validator against that original cycle map.
        from .assembly_submenus import validate_resources
        from .dbpf import encode_exemplar
        unnested = {key: value for key, value in after.items()
                    if key not in {(*prefix, number(row['definition']['id']))
                                   for row in submenus for prefix in prefixes}}
        for layout, _scene, _pieces in groups:
            if 'cycle_submenu' in layout:
                key = (*MENU_EXEMPLAR, number(layout['cycle_button']['id']))
                record = exemplar(unnested[key])
                record['properties'] = [prop for prop in record['properties']
                                        if number(prop['id'].removeprefix('0x')) not in (0x8A2602CA, 0x8A2602CC)]
                unnested[key] = encode_exemplar(record)
        if bundle['schema_version'] == 1:
            validate_resources(after, unnested, submenus, domain=bundle['domain_id'])
        else:
            for domain, domain_submenus in _domain_submenus(groups):
                parents = {(*prefix, number(row['definition']['id']))
                           for row in domain_submenus for prefix in prefixes}
                source = {key: value for key, value in after.items() if key not in parents}
                for row in domain_submenus:
                    for child in row['cycle_ids']:
                        key = (*MENU_EXEMPLAR, number(child))
                        source[key] = unnested[key]
                validate_resources(after, source, domain_submenus, domain=domain)


def verify(output, write_report=True):
    from .verify import safe_file, strict_dbpf, verify_build
    output = Path(output).resolve()
    require(not any(path.is_symlink() for path in output.rglob('*')), 'Multiple assembly candidate contains a symlink')
    manifest = single._read_json(output / 'manifest.json')
    experiment = manifest.get('menu_experiment')
    require(isinstance(experiment, dict) and experiment.get('kind') == KIND
            and type(experiment.get('schema_version')) is int and experiment['schema_version'] in (1, 2),
            'Unsupported multiple assembly menu discriminator')
    proof = experiment.get('source_inputs')
    require(isinstance(proof, dict) and {'manifest', 'controller', 'menu', 'groups'} <= set(proof), 'Incomplete multiple assembly source proof')
    names = {'manifest': 'manifest.json', 'controller': 'controller.proof', 'menu': 'menu.proof', 'groups': 'groups.json'}
    raw = {}
    for key, record in proof.items():
        relative = PROOF + '/' + (names[key] if key in names else key + '.png')
        require(key in names or re.fullmatch(r'icon-[0-9]{3}', key), 'Unknown multiple assembly proof key')
        require(isinstance(record, dict) and set(record) == {'path', 'bytes', 'sha256'} and record['path'] == relative,
                'Unexpected multiple assembly source proof path')
        source_file = safe_file(output, relative)
        require(source_file.is_file(), 'Missing multiple assembly source proof: ' + relative)
        raw[key] = source_file.read_bytes()
        require(record == single._record(relative, raw[key]), 'Multiple assembly proof fingerprint mismatch')
    base, bundle = json.loads(raw['manifest']), json.loads(raw['groups'])
    require('menu_experiment' not in base, 'Cannot nest multiple assembly candidates')
    groups = _groups(base, bundle)
    require(experiment['schema_version'] == bundle['schema_version'],
            'Multiple assembly schema differs from its frozen domain declarations')
    require(set(proof) == set(names) | {f'icon-{index:03d}' for index in range(len(groups))}, 'Missing or extra assembly icon proof')
    folder = base['plugin_folder']; controller_name = f'{folder}/{single.CONTROLLER}'; menu_name = f'{folder}/{single.MENU}'
    icons = [raw[f'icon-{index:03d}'] for index in range(len(groups))]
    controller, menu, composition, audits = _transform(base, raw['controller'], raw['menu'], bundle, icons)
    require(manifest == _manifest(base, bundle, proof, controller, menu, composition, audits), 'Multiple assembly manifest transformation differs')
    records = [*manifest['files'], *manifest['documentation']]
    expected = {row['path'] for row in records} | {'manifest.json', 'verification.json', 'input-audit.json'}
    actual = {path.relative_to(output).as_posix() for path in output.rglob('*') if path.is_file()}
    require(actual - {'verification.json', 'input-audit.json'} == expected - {'verification.json', 'input-audit.json'},
            'Multiple assembly file closure differs')
    for row in records:
        require(row == single._record(row['path'], safe_file(output, row['path']).read_bytes()), 'Multiple assembly file fingerprint mismatch')
    require(safe_file(output, controller_name).read_bytes() == controller and safe_file(output, menu_name).read_bytes() == menu,
            'Actual multiple assembly archives differ from transformation')
    _actual(base, bundle, raw['controller'], raw['menu'], controller, menu, composition)
    key = single._baseline_cache_key(output, proof, verify_build)
    reused = key in single._BASELINE_REPORTS
    if reused:
        baseline = deepcopy(single._BASELINE_REPORTS[key])
    else:
        with tempfile.TemporaryDirectory(prefix='scp-multi-menu-baseline-') as directory:
            restored = Path(directory)
            documents = {row['path'] for row in base.get('documentation', [])}
            for row in [*base['files'], *base.get('documentation', [])]:
                name = row['path']; target = safe_relative(restored, name); target.parent.mkdir(parents=True, exist_ok=True)
                payload = raw['controller'] if name == controller_name else raw['menu'] if name == menu_name else safe_file(
                    output, PROOF + '/documentation/' + name if name in documents else name).read_bytes()
                target.write_bytes(payload)
            (restored / 'manifest.json').write_bytes(raw['manifest'])
            if (output / 'input-audit.json').is_file():
                shutil.copy2(output / 'input-audit.json', restored / 'input-audit.json')
            baseline = verify_build(restored, write_report=False)
        if len(single._BASELINE_REPORTS) >= 2:
            single._BASELINE_REPORTS.clear()
        single._BASELINE_REPORTS[key] = deepcopy(baseline)
    count = sum(len(_consumed(layout, pieces)) for layout, _, pieces in groups)
    aliases = _alias_pairs(groups)
    submenus = _submenus(groups)
    report = {'schema_version': 1, 'static_checks_passed': True, 'files_checked': len(manifest['files']),
        'documentation_files_checked': len(manifest['documentation']), 'source_build_verification': baseline,
        'source_build_verification_reused_in_process': reused,
        'menu_experiment': {'kind': KIND, 'assembly_menu_buttons': len(groups), 'member_buttons_hidden': count,
            'piece_types_preserved': len(base['pieces']), 'all_piece_assets_preserved': True,
            'new_presentation_resources': 4 * (len(groups) + len(submenus)), 'removed_member_presentation_resources': 4 * count,
            'custom_type_families': len(base['pieces']) - count + len(groups) - len(hidden_members(base['pieces'])),
            'add_types_rows': count + len(aliases) - len(groups) + len(hidden_members(base['pieces'])),
            'unrelated_piece_buttons_preserved': len(base['pieces']) - count - len(hidden_members(base['pieces'])),
            'submenus_dll_required': bool(submenus or transport_menu.members(base)),
            'construction_definitions_preserved': True, 'network_ini_preserved': True,
            'assemblies': manifest['menu_experiment']['assemblies']},
        'in_game_menu_tested': False,
        'verification_limit': 'Strict frozen source-build validation and independent disjoint menu/Ordering checks; activation, Tab behavior, appearance, traffic, and save/reload remain unverified.'}
    if aliases:
        report['menu_experiment']['construction_aliases_checked'] = len(aliases)
    terminals = sum(len(layout.get('_terminals', ())) for layout, _, _ in groups)
    if terminals:
        report['menu_experiment']['native_terminal_roots_checked'] = terminals
        report['menu_experiment']['native_terminal_construction_states_checked'] = terminals * 8
    if submenus:
        if bundle['schema_version'] == 1:
            report['menu_experiment']['assembly_submenus'] = audits[-1]['submenus']
        else:
            report['menu_experiment']['assembly_submenus'] = [
                {'domain_id': audit['domain_id'], **row} for audit in audits if 'submenus' in audit
                for row in audit['submenus']]
    if bundle['schema_version'] == 2:
        from .menu_experiment_resources import member_domain
        report['menu_experiment']['domain_ids'] = list(dict.fromkeys(member_domain(pieces)
            for _layout, _scene, pieces in groups))
    if write_report:
        (output / 'verification.json').write_bytes(single._json_bytes(report))
    return report


def build(project_root, source, output, *, layout_ids=None, domain_id=None, selections=None,
          plugins=None, extra_roots=None):
    from .build import roots_for, audit_inputs
    from .verify import verify_build
    from .menu_experiment_resources import make_assembly_icon, validate_assembly_icon
    root, source = Path(project_root).resolve(), Path(source).resolve()
    output = Path(output).expanduser().absolute()
    require(not any(path.is_symlink() for path in (output, *output.parents)), 'Output path contains a symlink')
    output = output.resolve()
    require(not output.exists() and not output.is_relative_to(source) and not source.is_relative_to(output)
            and not root.is_relative_to(output), 'Multiple assembly output exists or overlaps source/project')
    require(plugins is not None, 'Assembly menus need Plugins roots for identifier collision checks')
    roots = roots_for(root, plugins, extra_roots)
    require(not any(output.is_relative_to(path) or path.is_relative_to(output) for path in roots), 'Assembly output must stay outside Plugins')
    if selections is None:
        require(isinstance(layout_ids, (list, tuple)) and len(layout_ids) >= 2
                and all(isinstance(value, str) and value for value in layout_ids)
                and len(set(layout_ids)) == len(layout_ids), 'Need at least two distinct explicit assembly layouts')
        domain_id = 'high-speed-rail' if domain_id is None else domain_id
        selected = [(domain_id, identifier) for identifier in layout_ids]
        bundle = {'schema_version': 1, 'domain_id': domain_id, 'groups': []}
    else:
        require(layout_ids is None and domain_id is None,
                'Domain-qualified selections cannot be combined with layout_ids or domain_id')
        require(isinstance(selections, (list, tuple)) and selections,
                'Need at least one explicit domain-qualified assembly selection')
        selected = []
        for row in selections:
            require(isinstance(row, dict) and set(row) == {'domain_id', 'layout_id'}
                    and isinstance(row['domain_id'], str) and row['domain_id'] in DOMAINS
                    and isinstance(row['layout_id'], str) and row['layout_id'],
                    'Malformed or unsupported domain-qualified assembly selection')
            selected.append((row['domain_id'], row['layout_id']))
        require(len(set(selected)) == len(selected), 'Repeated domain-qualified assembly selection')
        bundle = {'schema_version': 2, 'groups': []}
    catalog = single.load_catalog(root)
    icons, configurations = [], {}
    for selected_domain, identifier in selected:
        require(isinstance(selected_domain, str) and selected_domain in DOMAINS
                and selected_domain in catalog['domains'], 'Unknown assembly menu domain')
        if selected_domain not in configurations:
            config = single._read_json(safe_relative(root, catalog['domains'][selected_domain]['path'] + '/menu-layout.jsonc'))
            require(config.get('schema_version') == 1 and isinstance(config.get('layouts'), dict), 'Unsupported menu layout registry')
            configurations[selected_domain] = config
        config = configurations[selected_domain]
        require(identifier in config['layouts'], 'Unknown assembly menu layout')
        layout = single._layout(config['layouts'][identifier], selected_domain)
        assemblies = [row for row in catalog['_assemblies']
                      if row['id'] == layout['assembly_id'] and row['domain'] == selected_domain]
        require(len(assemblies) == 1, 'Layout must select one registered assembly')
        assembly = assemblies[0]
        row = {**({'domain_id': selected_domain} if bundle['schema_version'] == 2 else {}),
               'layout_id': identifier, 'layout': layout, 'scene': assembly['scene']}
        reservation_keys = layout.get('component_aliases', layout.get('terminal_components', {})).values()
        if reservation_keys:
            reservations = catalog.get('_allocations', {}).get('assembly_aliases', {})
            require(all(key in reservations for key in reservation_keys), 'Assembly component alias has no ID reservation')
            row['alias_reservations'] = {key: reservations[key] for key in reservation_keys}
        bundle['groups'].append(row)
        path = single._assembly_icon_path(root, assembly, layout.get('assembly_variant'))
        require(path.is_file(), 'Missing canonical assembly icon; generate it with assembly-icons')
        raw = path.read_bytes()
        expected = make_assembly_icon(single._assembly_icon_routes(
            {**assembly, 'scene': _scene(assembly['scene'], layout)}, catalog),
                                      network_label=single._assembly_icon_network(assembly))
        validate_assembly_icon(raw, expected_icon=expected)
        icons.append(raw)
    base = single._read_json(source / 'manifest.json')
    require('menu_experiment' not in base, 'Source must be a normal build; nested assembly menus are unsupported')
    single._check_source_files(source, base)
    transport_menu.require_current_source(catalog, base)
    groups = _groups(base, bundle)
    current = {piece['id']: piece for piece in catalog['pieces']}
    for _, _, pieces in groups:
        for piece in pieces:
            require({k: v for k, v in piece.items() if k != 'asset_file'} == current.get(piece['id']),
                    'Assembly member differs from current authoring metadata')
    context, installed, donors, _ = audit_inputs(catalog, plugins, base['pieces'], extra_roots)
    for layout, _, pieces in groups:
        if layout.get('_terminals'):
            from .providers import domain_module
            domain_module(pieces[0], 'trumpet_terminals').verify_native_inputs(context, installed, donors)
    proposed = {number(layout['cycle_button']['id']) for layout, _, _ in groups}
    proposed |= {number(row['definition']['id']) for row in _submenus(groups)}
    proposed |= {target for layout, _, pieces in groups for target in _alias_targets(layout, pieces).values()}
    proposed |= {target for layout, _, pieces in groups for target in _terminal_targets(layout, pieces)}
    used = {key[2] for key in installed} | {number(piece['menu']['id']) for piece in catalog['pieces']}
    transport_menu.check_ids(transport_menu.members(base), used, proposed)
    require(not proposed & used, 'Assembly presentation identifier collides with existing content')
    folder = base['plugin_folder']
    original_controller = (source / folder / single.CONTROLLER).read_bytes()
    original_menu = (source / folder / single.MENU).read_bytes()
    controller, menu, composition, audits = _transform(base, original_controller, original_menu, bundle, icons)
    raw = {'manifest': (source / 'manifest.json').read_bytes(), 'controller': original_controller,
           'menu': original_menu, 'groups': single._json_bytes(bundle),
           **{f'icon-{index:03d}': icon for index, icon in enumerate(icons)}}
    names = {'manifest': 'manifest.json', 'controller': 'controller.proof', 'menu': 'menu.proof', 'groups': 'groups.json'}
    proof = {key: single._record(PROOF + '/' + (names[key] if key in names else key + '.png'), value) for key, value in raw.items()}
    manifest = _manifest(base, bundle, proof, controller, menu, composition, audits)
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.scp-assembly-menus-', dir=output.parent))
    try:
        shutil.copytree(source, stage, dirs_exist_ok=True)
        for row in base.get('documentation', []):
            destination = safe_relative(stage, PROOF + '/documentation/' + row['path'])
            destination.parent.mkdir(parents=True, exist_ok=True)
            require(not destination.exists(), 'Frozen documentation collides with source file')
            safe_relative(stage, row['path']).replace(destination)
        for key, value in raw.items():
            path = safe_relative(stage, proof[key]['path']); path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(value)
        documents = _documents(groups, base)
        for name, value in {f'{folder}/{single.CONTROLLER}': controller, f'{folder}/{single.MENU}': menu, **documents}.items():
            path = safe_relative(stage, name); path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(value)
        (stage / 'manifest.json').write_bytes(single._json_bytes(manifest))
        report = verify_build(stage)
        os.replace(stage, output)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return {'output': str(output), 'guide': str(output / GUIDE), 'static_checks_passed': report['static_checks_passed'],
        'assembly_menu_buttons': len(groups),
        'member_buttons_hidden': sum(len(_consumed(layout, pieces)) for layout, _, pieces in groups),
        'piece_types_preserved': len(base['pieces']), 'assembly_ids': [layout['assembly_id'] for layout, _, _ in groups],
        'presentation_identifier_conflicts': 0, 'dependency_donors_checked': len(donors),
        'installed': False, 'in_game_menu_tested': False, 'submenus_dll_required': bool(_submenus(groups) or transport_menu.members(base))}
