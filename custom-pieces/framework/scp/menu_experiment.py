"""Build and independently check an opt-in assembly-parts menu experiment.

The normal build contract stays intact. An experimental candidate carries its
original manifest and two original archives outside the installable folder, so
the normal verifier can check the exact underlying build before menu-specific
checks run. No model, PATH, shadow, or construction definition is regenerated.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

from .catalog import load_catalog, number, safe_relative
from .dbpf import exemplar, pack_dbpf, require, tgi_string
from .menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION


KIND = 'assembly-parts-cycle-and-submenu-v1'
PROOF = 'docs/menu-experiment-source'
GUIDE = 'docs/menu-experiment/README.md'
CHECKS = 'docs/menu-experiment/game-checks.json'
CONTROLLER = '00_SCP_Controller_NAM50.dat'
MENU = '10_SCP_Menu.dat'
_BASELINE_REPORTS = {}


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _json_bytes(value):
    return (json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + '\n').encode()


def _record(path, raw):
    return {'path': path, 'bytes': len(raw), 'sha256': _sha(raw)}


def _check_source_files(source, base):
    """Fail before staging on changed bytes, links, or unexpected source files."""
    from .verify import safe_file
    require(not any(path.is_symlink() for path in source.rglob('*')), 'Source build contains a symlink')
    records = [*base['files'], *base.get('documentation', [])]
    names = {item['path'] for item in records}
    require(len(names) == len(records), 'Source build has repeated file records')
    actual = {path.relative_to(source).as_posix() for path in source.rglob('*') if path.is_file()}
    require(actual - {'manifest.json', 'verification.json', 'input-audit.json'} == names,
            'Source build file closure mismatch')
    for item in records:
        file = safe_file(source, item['path'])
        require(file.is_file() and item == _record(item['path'], file.read_bytes()),
                f'Source build file hash/size mismatch: {item["path"]}')


def _baseline_cache_key(output, proof, validator):
    """Reuse only in this process after exact candidate-file checks succeeded.

    The source manifest binds every unchanged asset and document; original
    archive proof binds the two changed files. External donor bytes are checked
    afresh too. A new CLI process always performs its own canonical validation.
    """
    audit_file = output / 'input-audit.json'
    require(not audit_file.exists() or audit_file.is_file() and not audit_file.is_symlink(),
            'Input audit must be a regular unlinked file')
    audit = audit_file.read_bytes() if audit_file.is_file() else b''
    donors = []
    if audit:
        for item in json.loads(audit).get('donors', []):
            file = Path(item['path'])
            require(file.is_file() and not file.is_symlink(), 'Local donor archive must be a regular unlinked file')
            digest = _sha(file.read_bytes())
            require(digest == item.get('sha256'), 'Local donor archive differs from its recorded fingerprint')
            donors.append((str(file), digest))
    return (validator, tuple((key, proof[key]['sha256']) for key in sorted(proof)),
            _sha(audit), tuple(donors))


def _read_json(path):
    return json.loads(Path(path).read_text())


def _members(scene):
    placements = scene.get('placements', scene.get('instances'))
    require(isinstance(placements, list) and placements, 'Assembly needs actual placements')
    require(all(isinstance(row, dict) and isinstance(row.get('piece_id'), str)
                and row['piece_id'] for row in placements), 'Invalid assembly member')
    return list(dict.fromkeys(row['piece_id'] for row in placements))


def _layout(value):
    require(isinstance(value, dict) and set(value) ==
            {'assembly_id', 'member_order', 'cycle_button', 'submenu'}, 'Unsupported menu layout fields')
    require(isinstance(value['assembly_id'], str) and
            re.fullmatch(r'[a-z][a-z0-9-]{1,63}', value['assembly_id']), 'Invalid assembly identifier')
    require(value['member_order'] == 'first-use-in-assembly', 'Unsupported menu member order')
    for key in ('cycle_button', 'submenu'):
        entry = value[key]
        require(isinstance(entry, dict) and set(entry) == {'id', 'order', 'title', 'description'},
                'Menu presentation needs id, order, title, and description')
        require(isinstance(entry['id'], str) and isinstance(entry['order'], str)
                and len(entry['id']) == 8 and len(entry['order']) == 8,
                'Menu presentation identifiers must use eight hexadecimal digits')
        require(number(entry['id']) != 0 and 0x70000000 <= number(entry['order']) < 0x80000000,
                'Invalid experimental Rail-menu identifier/order')
        require(all(isinstance(entry[field], str) and entry[field].strip()
                    and '\0' not in entry[field] for field in ('title', 'description')),
                'Experimental menu titles and descriptions must be nonempty')
    require(value['cycle_button']['id'] != value['submenu']['id'], 'Experimental presentation IDs overlap')
    return deepcopy(value)


def _selected(base, scene):
    identifiers = _members(scene)
    by_id = {piece['id']: piece for piece in base['pieces']}
    require(len(by_id) == len(base['pieces']), 'Source build has repeated piece identifiers')
    require(set(identifiers) <= set(by_id), 'Source build omits an assembly component')
    require(len(identifiers) >= 2, 'A cycle experiment needs at least two distinct piece types')
    return [by_id[identifier] for identifier in identifiers]


def _transformed(base, controller, menu, layout, scene):
    from .build import RUL0, NETWORK_INI
    from .rul0 import with_feature_sequence
    from .menu_experiment_resources import build_menu_experiment_resources
    from .verify import strict_dbpf
    pieces = _selected(base, scene)
    resources = strict_dbpf(controller)
    require(set(resources) == {RUL0, NETWORK_INI}, 'Original controller has unexpected resources')
    changed, composition = with_feature_sequence(resources[RUL0], base['overlay']['rul0'],
                                                 [number(piece['puzzle_id']) for piece in pieces])
    controller_resources = {**resources, RUL0: changed}
    cycle = {**layout['cycle_button'], 'target_id': pieces[0]['menu']['id']}
    menu_resources, audit = build_menu_experiment_resources(
        strict_dbpf(menu), pieces, cycle_button=cycle, submenu=layout['submenu'])
    return pack_dbpf(controller_resources), pack_dbpf(menu_resources), composition, audit, pieces


def _game_checks(pieces):
    rows = [
        {'id': 'rail-entry-points', 'description': 'Both the cycle button and the test submenu are visible in Transportation > Rail.'},
        {'id': 'submenu-contents', 'description': f'The test submenu opens and shows exactly {len(pieces)} distinct named component buttons.'},
        {'id': 'cycle-forward', 'description': f'Tab visits all {len(pieces)} component types once in the listed order, then wraps.'},
        {'id': 'cycle-backward', 'description': 'Shift+Tab traverses the same component types in reverse order.'},
        {'id': 'shared-first-root', 'description': 'The cycle button and the first individual button are both visible and activate the same first component.'},
        {'id': 'rotate-current-type', 'description': 'Home and End rotate the current component without switching to another type.'},
        {'id': 'cancel-and-reselect', 'description': 'Escape cancels placement; reselecting either entry point activates the expected component.'},
        {'id': 'save-reload', 'description': 'After placing test components, save, quit, reload, and confirm that their models and network paths remain present.'},
    ]
    rows += [{'id': 'individual-' + piece['id'], 'piece_id': piece['id'],
              'description': 'Click this individual button, confirm its named preview, and place the component at each of its four proper rotations.'}
             for piece in pieces]
    return {'schema_version': 1, 'purpose': 'Immutable list of pending game checks at build time; this is not an observation record or an assembly or piece traffic approval.',
            'authority': 'Record explicitly confirmed human observations separately, bound to this candidate manifest fingerprint; preserve this frozen template.',
            'environment_required': ['platform', 'game_version', 'NAM_profile', 'Submenus_DLL_version'],
            'cases': [{**row, 'status': 'unverified', 'observations': []} for row in rows]}


def _guide(layout, pieces):
    from .content import markdown_metadata
    rows = [markdown_metadata('Trumpet menu experiment',
            'Try the same reusable trumpet components through a shared Tab family and individual submenu buttons.',
            'Players and testers', 'experiment-guide').rstrip(), '', '# Trumpet menu experiment', '',
            'This candidate changes menu access only. It places one reusable component at a time; it does not construct the complete trumpet in one click. The compiled models, traffic paths, shadows, tile ownership, and construction definitions are unchanged. Actual game behavior is unverified.', '',
            'Verification and installation require the current project checkout that created this candidate. The source build\'s copied documentation is frozen historical evidence and does not include the new menu-test command. Use the current checkout\'s custom-pieces/scp.py, its BUILD_AND_INSTALL.md menu-experiment instructions, and an external backup folder. Keep the existing Submenus DLL, Resource Loading Hooks DLL, and submenu-essentials.dat installed. Use a disposable test city. Do not copy a second controller overlay beside an existing SCP installation.', '',
            '1. Open **Transportation → Rail**.',
            f'2. Click **{layout["cycle_button"]["title"]}**. Its first component is **{pieces[0]["name"]}**.',
            f'3. Press **Tab** to select the next of {len(pieces)} types, or **Shift+Tab** to select the previous type. Press **Home** or **End** to rotate the current type. Click clear terrain to place one component.',
            f'4. Open **{layout["submenu"]["title"]}** to see one button per reusable type. Each button should start on its named type. These entries share the same Tab family; Tab can change to another trumpet component after either entry point.',
            '5. Check both presentations of the first component, every individual button, forward and reverse cycling, rotation, cancellation, placement, and save/reload. Report the exact title, component, controls, and game/DLL versions when something fails.', '',
            'The two access paths intentionally share construction targets. The DLL\'s documented submenu properties and the saved archive structure are checked in software; the game still needs to confirm that both presentations remain visible and select the expected network tool. The immutable [game-checks.json](game-checks.json) lists pending checks at build time. Record explicitly confirmed observations separately against the candidate manifest fingerprint; do not edit this frozen template. No piece or assembly test result is inherited from this menu experiment.', '',
            '| Tab position | Individual button title | Permanent piece ID |', '| --- | --- | --- |']
    rows += [f'| {index} | {piece["name"]} | `{piece["id"]}` |' for index, piece in enumerate(pieces, 1)]
    return ('\n'.join(rows) + '\n').encode()


def _expected_manifest(base, layout, scene, proof, controller, menu, composition, audit):
    result = deepcopy(base)
    require('menu_experiment' not in result, 'Cannot nest menu experiments')
    folder = base['plugin_folder']
    replacements = {f'{folder}/{CONTROLLER}': controller, f'{folder}/{MENU}': menu}
    result['files'] = [_record(item['path'], replacements[item['path']])
                       if item['path'] in replacements else deepcopy(item) for item in base['files']]
    pieces = _selected(base, scene)
    result['overlay']['rul0'] = composition
    result['menu_audit'] = audit
    result['menu_experiment'] = {'kind': KIND, 'schema_version': 1,
        'assembly_id': layout['assembly_id'], 'member_ids': [piece['id'] for piece in pieces],
        'source_inputs': proof, 'shared_tab_family': True,
        'construction_aliases_created': False, 'in_game_menu_tested': False}
    result['installed'] = False
    result['in_game_tested'] = False
    result['release']['public_release_ready'] = False
    result['release']['blocked'] = list(dict.fromkeys([*result['release'].get('blocked', []),
        'Experimental menu access paths require explicit in-game observations; public release is blocked.']))
    additions = [*(proof[key] for key in sorted(proof)), _record(GUIDE, _guide(layout, pieces)),
                 _record(CHECKS, _json_bytes(_game_checks(pieces)))]
    paths = {item['path'] for item in base.get('documentation', [])}
    require(not paths.intersection(item['path'] for item in additions), 'Experiment evidence overlaps source documentation')
    result['documentation'] = [*deepcopy(base.get('documentation', [])), *additions]
    return result


def _check_actual_resources(base_controller, base_menu, controller, menu, base, layout, pieces):
    """Inspect actual encoded facts independently of the generation functions."""
    from .build import RUL0, NETWORK_INI
    from .rul0 import ordering_span, _ring
    from .verify import strict_dbpf
    old_controller, current_controller = strict_dbpf(base_controller), strict_dbpf(controller)
    require(set(current_controller) == set(old_controller) == {RUL0, NETWORK_INI}, 'Controller resource closure changed')
    require(current_controller[NETWORK_INI] == old_controller[NETWORK_INI], 'Menu experiment changed NetworkINI')
    old = strict_dbpf(base_menu); current = strict_dbpf(menu)
    selected = {number(piece['menu']['id']) for piece in pieces}
    cycle_id, submenu_id = number(layout['cycle_button']['id']), number(layout['submenu']['id'])
    expected_new = {(*prefix, iid) for iid in (cycle_id, submenu_id)
                    for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)}
    require(set(current) == set(old) | expected_new and not set(old) & expected_new,
            'Experimental menu resource closure mismatch')
    for key in old:
        if key[:2] != MENU_EXEMPLAR or key[2] not in selected:
            require(current[key] == old[key], 'Menu experiment changed an unrelated resource')
    props = lambda raw: {number(prop['id'].removeprefix('0x')): prop for prop in exemplar(raw)['properties']}
    for piece in pieces:
        iid = number(piece['menu']['id']); key = (*MENU_EXEMPLAR, iid)
        original, actual = props(old[key]), props(current[key])
        require(exemplar(old[key])['parent'] == exemplar(current[key])['parent'], 'Changed original menu parent cohort')
        require(set(actual) == set(original) | {0x8a2602ca, 0x8a2602cc}, 'Changed original button property closure')
        require(all(actual[key] == value for key, value in original.items()), 'Changed original button identity or property')
        require(actual[0x8a2602ca]['values'] == [submenu_id] and actual[0x8a2602cc]['values'] == [2],
                'Individual button has the wrong test submenu or class')
    cycle = props(current[*MENU_EXEMPLAR, cycle_id]); submenu = props(current[*MENU_EXEMPLAR, submenu_id])
    require(cycle[0x8a2602bb]['values'] == [number(pieces[0]['menu']['id'])]
            and cycle[0x8a2602b8]['values'] == [cycle_id], 'Cycle entry does not target the first existing component')
    require(submenu[0x8a2602bb]['values'] == [submenu_id] and submenu[0x8a2602ca]['values'] == [0x29]
            and submenu[0x8a2602cc]['values'] == [1], 'Wrong test submenu root or class')
    def ordering_rows(raw):
        start, end = ordering_span(raw)
        rows = []
        for line in raw[start:end].decode('ascii').splitlines():
            active = line.split(';', 1)[0].strip()
            match = re.fullmatch(r'(RotationRing|AddTypes)\s*=\s*(.+)', active, re.I)
            if match:
                rows.append((match[1].lower(), _ring('RotationRing=' + match[2])))
        return rows

    roots = {number(piece['puzzle_id']) for piece in pieces}
    original_rows = ordering_rows(old_controller[RUL0])
    all_rows = ordering_rows(current_controller[RUL0])
    positions = [index for index, row in enumerate(all_rows) if row[1][0] in roots]
    require(positions and positions == list(range(positions[0], positions[-1] + 1)),
            'Assembly feature rows must occupy one uninterrupted ordering block')
    rows = [all_rows[index] for index in positions]
    original_states = {row[1][0]: row[1] for row in original_rows if row[1][0] in roots}
    require(len(original_states) == len(pieces) and
            all(row[1] == original_states.get(row[1][0]) for row in rows),
            'Assembly type family changed an original rotation state')
    require([row for row in all_rows if row[1][0] not in roots] ==
            [row for row in original_rows if row[1][0] not in roots], 'An unrelated construction family changed')
    require(len(rows) == len(pieces) and [row[1][0] for row in rows] ==
            [number(piece['puzzle_id']) for piece in pieces], 'Wrong actual Tab sequence or membership')
    require([row[0] for row in rows] == ['rotationring'] + ['addtypes'] * (len(pieces) - 1),
            'Assembly components are not one actual feature family')


def verify_menu_experiment(output, write_report=True):
    from .verify import safe_file, verify_build
    output = Path(output).resolve()
    require(not any(path.is_symlink() for path in output.rglob('*')), 'Menu experiment contains a symlink')
    manifest = _read_json(output / 'manifest.json')
    experiment = manifest.get('menu_experiment')
    require(isinstance(experiment, dict) and experiment.get('kind') == KIND
            and experiment.get('schema_version') == 1, 'Unsupported menu experiment')
    proof = experiment.get('source_inputs')
    expected = {'manifest': f'{PROOF}/manifest.json', 'controller': f'{PROOF}/controller.proof',
                'menu': f'{PROOF}/menu.proof', 'layout': f'{PROOF}/layout.json', 'assembly': f'{PROOF}/assembly.json'}
    require(isinstance(proof, dict) and set(proof) == set(expected), 'Incomplete experiment source evidence')
    raw = {}
    for key, name in expected.items():
        item = proof[key]
        require(isinstance(item, dict) and set(item) == {'path', 'bytes', 'sha256'} and item['path'] == name,
                'Unexpected experiment source evidence path')
        file = safe_file(output, name)
        require(file.is_file(), f'Missing experimental source evidence: {name}')
        raw[key] = file.read_bytes()
        require(item == _record(name, raw[key]), 'Experimental source evidence fingerprint mismatch')
    base, layout, scene = json.loads(raw['manifest']), _layout(json.loads(raw['layout'])), json.loads(raw['assembly'])
    require('menu_experiment' not in base, 'Nested experiment source manifest')
    pieces = _selected(base, scene)
    controller, menu, composition, audit, _ = _transformed(base, raw['controller'], raw['menu'], layout, scene)
    require(manifest == _expected_manifest(base, layout, scene, proof, controller, menu, composition, audit),
            'Experimental manifest differs from the exact allowed menu transformation')
    allowed = {'manifest.json', 'verification.json', 'input-audit.json'} | {
        item['path'] for item in [*manifest['files'], *manifest['documentation']]}
    actual = {path.relative_to(output).as_posix() for path in output.rglob('*') if path.is_file()}
    require(actual - {'verification.json', 'input-audit.json'} == allowed - {'verification.json', 'input-audit.json'},
            'Experimental output file closure mismatch')
    for item in [*manifest['files'], *manifest['documentation']]:
        require(item == _record(item['path'], safe_file(output, item['path']).read_bytes()),
                f'Experimental file hash/size mismatch: {item["path"]}')
    folder = base['plugin_folder']; controller_path = f'{folder}/{CONTROLLER}'; menu_path = f'{folder}/{MENU}'
    require(safe_file(output, controller_path).read_bytes() == controller
            and safe_file(output, menu_path).read_bytes() == menu, 'Actual menu/controller differs from verified transformation')
    _check_actual_resources(raw['controller'], raw['menu'], controller, menu, base, layout, pieces)
    cache_key = _baseline_cache_key(output, proof, verify_build)
    reused = cache_key in _BASELINE_REPORTS
    if reused:
        report = deepcopy(_BASELINE_REPORTS[cache_key])
    else:
        with tempfile.TemporaryDirectory(prefix='scp-menu-baseline-') as directory:
            restored = Path(directory)
            for item in [*base['files'], *base.get('documentation', [])]:
                destination = safe_relative(restored, item['path']); destination.parent.mkdir(parents=True, exist_ok=True)
                payload = raw['controller'] if item['path'] == controller_path else raw['menu'] if item['path'] == menu_path else safe_file(output, item['path']).read_bytes()
                destination.write_bytes(payload)
            (restored / 'manifest.json').write_bytes(raw['manifest'])
            if (output / 'input-audit.json').is_file():
                shutil.copy2(output / 'input-audit.json', restored / 'input-audit.json')
            report = verify_build(restored, write_report=False)
        if len(_BASELINE_REPORTS) >= 2:
            _BASELINE_REPORTS.clear()
        _BASELINE_REPORTS[cache_key] = deepcopy(report)
    report = {'schema_version': 1, 'static_checks_passed': True,
        'files_checked': len(manifest['files']), 'documentation_files_checked': len(manifest['documentation']),
        'source_build_verification': report,
        'source_build_verification_reused_in_process': reused,
        'menu_experiment': {'kind': KIND, 'assembly_id': layout['assembly_id'],
        'source_build_verified': True, 'all_piece_assets_preserved': True, 'piece_types_preserved': len(base['pieces']),
        'component_types_in_cycle': len(pieces), 'individual_submenu_buttons': len(pieces),
        'new_presentation_resources': 8, 'network_ini_preserved': True, 'construction_definitions_preserved': True,
        'custom_type_families': len(base['pieces']) - len(pieces) + 1,
        'grouped_type_rows': len(pieces), 'add_types_rows': len(pieces) - 1,
        'shared_tab_family': True, 'alias_activation_and_visibility': 'unverified',
        'pending_game_cases': len(_game_checks(pieces)['cases'])},
        'in_game_menu_tested': False,
        'verification_limit': 'Strict source-build validation and exact menu/controller transformation; actual DLL menu visibility, network selection, Tab behavior, and game operation remain unverified.'}
    if write_report:
        (output / 'verification.json').write_bytes(_json_bytes(report))
    return report


def build_menu_experiment(project_root, source, output, *, layout_id='trumpet-menu-test',
                          domain_id='high-speed-rail', plugins=None, extra_roots=None):
    from .build import audit_inputs, roots_for
    from .verify import verify_build
    root, source = Path(project_root).resolve(), Path(source).resolve()
    output = Path(output).expanduser().absolute()
    require(not any(path.is_symlink() for path in (output, *output.parents)), 'Output path contains a symlink')
    output = output.resolve()
    require(not output.exists(), 'Menu experiment output already exists; choose a new test build name')
    require(not output.is_relative_to(source) and not source.is_relative_to(output)
            and not root.is_relative_to(output), 'Menu experiment output overlaps source or project')
    require(plugins is not None, 'Menu experiment needs Plugins roots for presentation identifier collision checks')
    roots = roots_for(root, plugins, extra_roots)
    require(not any(output.is_relative_to(path) or path.is_relative_to(output) for path in roots),
            'Menu experiment output must stay outside Plugins')
    catalog = load_catalog(root)
    require(domain_id in catalog['domains'], 'Unknown menu experiment domain')
    config_path = safe_relative(root, catalog['domains'][domain_id]['path'] + '/menu-layout.json')
    config = _read_json(config_path)
    require(config.get('schema_version') == 1 and isinstance(config.get('layouts'), dict), 'Unsupported menu layout registry')
    require(layout_id in config['layouts'], 'Unknown experimental menu layout')
    layout = _layout(config['layouts'][layout_id])
    assemblies = [assembly for assembly in catalog['_assemblies']
                  if assembly['id'] == layout['assembly_id'] and assembly['domain'] == domain_id]
    require(len(assemblies) == 1, 'Menu experiment must select one registered assembly')
    scene = assemblies[0]['scene']
    base = _read_json(source / 'manifest.json')
    require('menu_experiment' not in base, 'Source must be a normal verified build')
    _check_source_files(source, base)
    pieces = _selected(base, scene)
    current = {piece['id']: piece for piece in catalog['pieces']}
    for piece in pieces:
        require({key: value for key, value in piece.items() if key != 'asset_file'} == current.get(piece['id']),
                'Assembly component definition differs from current authoring metadata')
    _, installed, donors, _ = audit_inputs(catalog, plugins, base['pieces'], extra_roots)
    proposed = {number(layout[key]['id']) for key in ('cycle_button', 'submenu')}
    used_ids = {key[2] for key in installed} | {number(piece['menu']['id']) for piece in catalog['pieces']}
    require(not proposed & used_ids, 'Experimental presentation identifier collides with existing content')
    folder = base['plugin_folder']
    original_controller = (source / folder / CONTROLLER).read_bytes()
    original_menu = (source / folder / MENU).read_bytes()
    controller, menu, composition, audit, pieces = _transformed(base, original_controller, original_menu, layout, scene)
    proof_raw = {'manifest': (source / 'manifest.json').read_bytes(), 'controller': original_controller,
                 'menu': original_menu, 'layout': _json_bytes(layout), 'assembly': _json_bytes(scene)}
    proof_names = {'manifest': 'manifest.json', 'controller': 'controller.proof', 'menu': 'menu.proof',
                   'layout': 'layout.json', 'assembly': 'assembly.json'}
    proof = {key: _record(f'{PROOF}/{proof_names[key]}', raw) for key, raw in proof_raw.items()}
    manifest = _expected_manifest(base, layout, scene, proof, controller, menu, composition, audit)
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.scp-menu-test-', dir=output.parent))
    try:
        shutil.copytree(source, stage, dirs_exist_ok=True)
        for key, raw in proof_raw.items():
            target = stage / proof[key]['path']; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(raw)
        for name, raw in ((f'{folder}/{CONTROLLER}', controller), (f'{folder}/{MENU}', menu),
                          (GUIDE, _guide(layout, pieces)), (CHECKS, _json_bytes(_game_checks(pieces)))):
            target = stage / name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(raw)
        (stage / 'manifest.json').write_bytes(_json_bytes(manifest))
        report = verify_build(stage)
        os.replace(stage, output)
    finally:
        if stage.exists(): shutil.rmtree(stage)
    return {'output': str(output), 'guide': str(output / GUIDE), 'assembly_id': layout['assembly_id'],
            'piece_types_preserved': len(base['pieces']), 'assembly_component_types': len(pieces),
            'cycle_button': layout['cycle_button']['title'], 'test_submenu': layout['submenu']['title'],
            'static_checks_passed': report['static_checks_passed'], 'in_game_menu_tested': False,
            'presentation_identifier_conflicts': 0,
            'dependency_donors_checked': len(donors), 'installed': False}
