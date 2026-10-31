"""Independent assembly cycles from one verified, disjoint normal build.

Only menu presentations and the generated RUL0 Ordering insertion change.
The original build and all per-assembly inputs remain frozen verification
proof; no completed menu candidate is used as an intermediate source.
"""
from copy import deepcopy
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

from .catalog import number, safe_relative
from .dbpf import exemplar, pack_dbpf, require
from .menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
from . import menu_experiment as single

KIND = 'assembly-disjoint-button-cycles-v1'
PROOF = 'docs/assembly-menus-source'
GUIDE = 'docs/assembly-menus/README.md'
CHECKS = 'docs/assembly-menus/game-checks.json'


def _groups(base, bundle):
    require(isinstance(bundle, dict) and set(bundle) == {'schema_version', 'domain_id', 'groups'}
            and type(bundle['schema_version']) is int and bundle['schema_version'] == 1,
            'Malformed disjoint assembly layout bundle')
    domain = bundle['domain_id']
    require(isinstance(domain, str) and domain in ('highway', 'high-speed-rail'), 'Unsupported assembly menu domain')
    rows = bundle['groups']
    require(isinstance(rows, list) and len(rows) >= 2, 'Multiple assembly menus need at least two layouts')
    result, identifiers, assemblies, buttons, members, menu_ids, states = [], set(), set(), set(), set(), set(), set()
    from .menu_experiment_resources import member_domain
    for row in rows:
        require(isinstance(row, dict) and set(row) == {'layout_id', 'layout', 'scene'}
                and isinstance(row['layout_id'], str) and row['layout_id'] and row['layout_id'] not in identifiers
                and isinstance(row['scene'], dict),
                'Invalid or repeated assembly menu layout')
        identifiers.add(row['layout_id'])
        layout = single._layout(row['layout'], domain)
        require('submenu' not in layout, 'Disjoint assembly menus do not accept submenu layouts')
        require(layout['assembly_id'] not in assemblies, 'Repeated assembly in menu selection')
        assemblies.add(layout['assembly_id'])
        button = number(layout['cycle_button']['id'])
        require(button not in buttons, 'Duplicate assembly presentation identifier')
        buttons.add(button)
        pieces = single._selected(base, row['scene'])
        require(member_domain(pieces) == domain, 'Assembly member domain differs from menu selection')
        for piece in pieces:
            root, menu_id = number(piece['puzzle_id']), number(piece['menu']['id'])
            rotations = {root + turn * 0x10000 for turn in range(8)}
            require(piece['id'] not in members and menu_id not in menu_ids and not rotations & states,
                    'Assembly menu groups overlap in a member, menu identifier, or construction state')
            members.add(piece['id']); menu_ids.add(menu_id); states.update(rotations)
        result.append((layout, row['scene'], pieces))
    require(not buttons & menu_ids, 'Assembly presentation identifier overlaps a member button')
    return result


def _transform(base, controller, menu, bundle, icons):
    from .build import RUL0, NETWORK_INI
    from .adaptive_network import RUL1
    from .rul0 import with_feature_sequence
    from .verify import strict_dbpf
    from .menu_experiment_resources import build_menu_experiment_resources
    groups = _groups(base, bundle)
    original = strict_dbpf(controller)
    require(set(original) == {RUL0, NETWORK_INI} | ({RUL1} if 'rul1' in base['overlay'] else set()),
            'Original multi-assembly controller resource closure differs')
    roots = [[number(piece['puzzle_id']) for piece in pieces] for _, _, pieces in groups]
    changed, composition = with_feature_sequence(original[RUL0], base['overlay']['rul0'],
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
    resources, audits = strict_dbpf(menu), []
    require(len(icons) == len(groups), 'Missing assembly menu icon')
    for (layout, _scene, pieces), icon in zip(groups, icons):
        cycle = {**layout['cycle_button'], 'target_id': pieces[0]['menu']['id']}
        resources, audit = build_menu_experiment_resources(resources, pieces, cycle_button=cycle,
                                                          cycle_icon=icon, expected_cycle_icon=icon)
        audits.append(audit)
    return pack_dbpf({**original, RUL0: changed}), pack_dbpf(resources), composition, audits


def _documents(groups):
    from .content import markdown_metadata
    from .menu_experiment_resources import member_domain
    network_menu = 'Highways' if member_domain(groups[0][2]) == 'highway' else 'Rail'
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
        f'1. Open **Transportation → {network_menu}**.',
        '2. Click one of the exact assembly buttons listed below. It starts on that assembly’s first component.',
        '3. Press **Tab** for the next component, or **Shift+Tab** for the previous component. Cycling stays within the selected assembly.',
        '4. Press **Home** or **End** to rotate the current component, then click clear terrain to place it.',
        '5. Press **Escape** to cancel. Select another assembly button to begin its separate component cycle.', '']
    cases = []
    for index, (layout, _scene, pieces) in enumerate(groups, 2):
        lines += [f'<a id="{index}-{layout["assembly_id"]}"></a>', '',
                  f'## {index}. ' + layout['cycle_button']['title'], '',
                  'Assembly: `' + layout['assembly_id'] + '`. The cycle follows this component order:', '']
        lines += [f'{index}. {piece["name"]} (`{piece["id"]}`).' for index, piece in enumerate(pieces, 1)]
        lines += ['']
        for case in single._game_checks(pieces, single_button=True)['cases']:
            cases.append({**case, 'id': layout['assembly_id'] + ':' + case['id'],
                          'assembly_id': layout['assembly_id']})
    lines += [f'<a id="{len(groups) + 2}-verification"></a>', '',
              f'## {len(groups) + 2}. Verification and observations', '',
              'The original source documents and archives are frozen under `../assembly-menus-source/`. All piece DATs are unchanged. This candidate does not require Submenus DLL. Building and packaging do not install anything.', '',
              'The [game-checks.json](game-checks.json) template lists pending checks separately for each assembly. Record explicit observations against the candidate manifest fingerprint, platform, game version, and NAM profile. Software checks do not approve menu activation, visible traffic, or save/reload behavior.', '']
    guide = '\n'.join(lines).encode('utf8')
    checks = single._json_bytes({'schema_version': 1, 'purpose': 'Frozen pending checks; no human observations.',
        'authority': 'Record explicit human observations separately against the candidate manifest fingerprint; preserve this template.',
        'environment_required': ['platform', 'game_version', 'NAM_profile'], 'cases': cases})
    readme = ('Assembly component menus\nDEVELOPMENT BUILD — NOT GAME-TESTED\n'
              + ''.join(f'{layout["cycle_button"]["title"]}: {len(pieces)} components\n' for layout, _, pieces in groups)
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
    selection = [{'assembly_id': layout['assembly_id'], 'member_ids': [piece['id'] for piece in pieces]}
                 for layout, _, pieces in groups]
    result['menu_experiment'] = {'kind': KIND, 'schema_version': 1, 'assemblies': selection,
        'source_inputs': proof, 'construction_aliases_created': False, 'in_game_menu_tested': False}
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
                 *(single._record(name, raw) for name, raw in _documents(groups).items())]
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
    groups = _groups(base, bundle)
    old_c, new_c = strict_dbpf(old_controller), strict_dbpf(controller)
    require(set(old_c) == set(new_c) and all(old_c[key] == new_c[key] for key in old_c if key != RUL0),
            'Multiple assembly menus changed non-RUL0 controller resources')
    old_insert = base['overlay']['rul0']['ordering_insertion'].encode('ascii')
    new_insert = composition['ordering_insertion'].encode('ascii')
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
    selections = [[number(piece['puzzle_id']) for piece in pieces] for _, _, pieces in groups]
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
    before, after = strict_dbpf(old_menu), strict_dbpf(menu)
    prefixes = (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)
    removed = {(*prefix, number(piece['menu']['id'])) for _, _, pieces in groups for piece in pieces for prefix in prefixes}
    added = {(*prefix, number(layout['cycle_button']['id'])) for layout, _, _ in groups for prefix in prefixes}
    require(not set(before) & added and set(after) == (set(before) - removed) | added,
            'Multiple assembly menu resource closure differs')
    require(all(before[key] == after[key] for key in set(before) - removed), 'An unrelated menu resource changed')
    for layout, _scene, pieces in groups:
        iid = number(layout['cycle_button']['id'])
        properties = {number(prop['id'].removeprefix('0x')): prop['values']
                      for prop in exemplar(after[*MENU_EXEMPLAR, iid])['properties']}
        require(properties[0x8A2602BB] == [number(pieces[0]['menu']['id'])]
                and properties[0x8A2602B8] == [iid] and properties[0x8A2602B9] == [number(layout['cycle_button']['order'])]
                and 0x8A2602CA not in properties and 0x8A2602CC not in properties,
                'Assembly button has a wrong target, order, or submenu property')
        if bundle['domain_id'] == 'highway':
            require(properties.get(0x4005) == [0] and 0x4001 not in properties, 'Assembly button left the Highways menu')


def verify(output, write_report=True):
    from .verify import safe_file, strict_dbpf, verify_build
    output = Path(output).resolve()
    require(not any(path.is_symlink() for path in output.rglob('*')), 'Multiple assembly candidate contains a symlink')
    manifest = single._read_json(output / 'manifest.json')
    experiment = manifest.get('menu_experiment')
    require(isinstance(experiment, dict) and experiment.get('kind') == KIND
            and type(experiment.get('schema_version')) is int and experiment['schema_version'] == 1,
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
    count = sum(len(pieces) for _, _, pieces in groups)
    report = {'schema_version': 1, 'static_checks_passed': True, 'files_checked': len(manifest['files']),
        'documentation_files_checked': len(manifest['documentation']), 'source_build_verification': baseline,
        'source_build_verification_reused_in_process': reused,
        'menu_experiment': {'kind': KIND, 'assembly_menu_buttons': len(groups), 'member_buttons_hidden': count,
            'piece_types_preserved': len(base['pieces']), 'all_piece_assets_preserved': True,
            'new_presentation_resources': 4 * len(groups), 'removed_member_presentation_resources': 4 * count,
            'custom_type_families': len(base['pieces']) - count + len(groups), 'add_types_rows': count - len(groups),
            'unrelated_piece_buttons_preserved': len(base['pieces']) - count, 'submenus_dll_required': False,
            'construction_definitions_preserved': True, 'network_ini_preserved': True,
            'assemblies': manifest['menu_experiment']['assemblies']},
        'in_game_menu_tested': False,
        'verification_limit': 'Strict frozen source-build validation and independent disjoint menu/Ordering checks; activation, Tab behavior, appearance, traffic, and save/reload remain unverified.'}
    if write_report:
        (output / 'verification.json').write_bytes(single._json_bytes(report))
    return report


def build(project_root, source, output, *, layout_ids, domain_id='high-speed-rail', plugins=None, extra_roots=None):
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
    require(isinstance(layout_ids, (list, tuple)) and len(layout_ids) >= 2
            and all(isinstance(value, str) and value for value in layout_ids)
            and len(set(layout_ids)) == len(layout_ids), 'Need at least two distinct explicit assembly layouts')
    catalog = single.load_catalog(root)
    require(domain_id in catalog['domains'], 'Unknown assembly menu domain')
    config = single._read_json(safe_relative(root, catalog['domains'][domain_id]['path'] + '/menu-layout.jsonc'))
    require(config.get('schema_version') == 1 and isinstance(config.get('layouts'), dict), 'Unsupported menu layout registry')
    bundle = {'schema_version': 1, 'domain_id': domain_id, 'groups': []}
    icons = []
    for identifier in layout_ids:
        require(identifier in config['layouts'], 'Unknown assembly menu layout')
        layout = single._layout(config['layouts'][identifier], domain_id)
        assemblies = [row for row in catalog['_assemblies'] if row['id'] == layout['assembly_id'] and row['domain'] == domain_id]
        require(len(assemblies) == 1, 'Layout must select one registered assembly')
        assembly = assemblies[0]
        bundle['groups'].append({'layout_id': identifier, 'layout': layout, 'scene': assembly['scene']})
        path = single._assembly_icon_path(root, assembly)
        require(path.is_file(), 'Missing canonical assembly icon; generate it with assembly-icons')
        raw = path.read_bytes()
        expected = make_assembly_icon(single._assembly_icon_routes(assembly, catalog),
                                      network_label=single._assembly_icon_network(assembly))
        validate_assembly_icon(raw, expected_icon=expected)
        icons.append(raw)
    base = single._read_json(source / 'manifest.json')
    require('menu_experiment' not in base, 'Source must be a normal build; nested assembly menus are unsupported')
    single._check_source_files(source, base)
    groups = _groups(base, bundle)
    current = {piece['id']: piece for piece in catalog['pieces']}
    for _, _, pieces in groups:
        for piece in pieces:
            require({k: v for k, v in piece.items() if k != 'asset_file'} == current.get(piece['id']),
                    'Assembly member differs from current authoring metadata')
    _, installed, donors, _ = audit_inputs(catalog, plugins, base['pieces'], extra_roots)
    proposed = {number(layout['cycle_button']['id']) for layout, _, _ in groups}
    used = {key[2] for key in installed} | {number(piece['menu']['id']) for piece in catalog['pieces']}
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
        documents = _documents(groups)
        for name, value in {f'{folder}/{single.CONTROLLER}': controller, f'{folder}/{single.MENU}': menu, **documents}.items():
            path = safe_relative(stage, name); path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(value)
        (stage / 'manifest.json').write_bytes(single._json_bytes(manifest))
        report = verify_build(stage)
        os.replace(stage, output)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return {'output': str(output), 'guide': str(output / GUIDE), 'static_checks_passed': report['static_checks_passed'],
        'assembly_menu_buttons': len(groups), 'member_buttons_hidden': sum(len(p) for _, _, p in groups),
        'piece_types_preserved': len(base['pieces']), 'assembly_ids': [layout['assembly_id'] for layout, _, _ in groups],
        'presentation_identifier_conflicts': 0, 'dependency_donors_checked': len(donors),
        'installed': False, 'in_game_menu_tested': False, 'submenus_dll_required': False}
