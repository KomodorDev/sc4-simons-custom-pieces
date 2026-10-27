"""Prepare and independently check one assembly button with a component cycle.

The normal piece-build contract stays intact. An assembly candidate carries its
original manifest and two original archives outside the installable folder, so
the normal verifier can check the exact underlying build before menu-specific
checks run. No model, PATH, shadow, or construction definition is regenerated.
Frozen historical two-entry menu candidates retain their original verifier.
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
ASSEMBLY_MENU_KIND = 'assembly-single-button-cycle-v1'
PROOF = 'docs/menu-experiment-source'
GUIDE = 'docs/menu-experiment/README.md'
CHECKS = 'docs/menu-experiment/game-checks.json'
ASSEMBLY_PROOF = 'docs/assembly-menu-source'
ASSEMBLY_GUIDE = 'docs/assembly-menu/README.md'
ASSEMBLY_CHECKS = 'docs/assembly-menu/game-checks.json'
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
    required = {'assembly_id', 'member_order', 'cycle_button'}
    require(isinstance(value, dict) and set(value) in (required, required | {'submenu'}),
            'Unsupported menu layout fields')
    require(isinstance(value['assembly_id'], str) and
            re.fullmatch(r'[a-z][a-z0-9-]{1,63}', value['assembly_id']), 'Invalid assembly identifier')
    require(value['member_order'] == 'first-use-in-assembly', 'Unsupported menu member order')
    for key in (('cycle_button', 'submenu') if 'submenu' in value else ('cycle_button',)):
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
    if 'submenu' in value:
        require(value['cycle_button']['id'] != value['submenu']['id'], 'Experimental presentation IDs overlap')
    return deepcopy(value)


def _presentation_kind(layout):
    return KIND if 'submenu' in layout else ASSEMBLY_MENU_KIND


def _presentation_paths(layout):
    return (PROOF, GUIDE, CHECKS) if 'submenu' in layout else (ASSEMBLY_PROOF, ASSEMBLY_GUIDE, ASSEMBLY_CHECKS)


def _source_documentation_path(layout, path):
    return path if 'submenu' in layout else f'{ASSEMBLY_PROOF}/documentation/{path}'


def _assembly_readme(layout, pieces):
    return ('Assembly component menu\nDEVELOPMENT BUILD — NOT GAME-TESTED\n'
            f'Assembly: {layout["assembly_id"]}\n'
            f'Button: {layout["cycle_button"]["title"]}\n'
            f'The single assembly button selects {len(pieces)} reusable component types with Tab and Shift+Tab.\n'
            'Home and End rotate the selected component; each click places one component.\n'
            'Read docs/assembly-menu/README.md for the component order and pending game checks.\n'
            'Original source documents and archives are frozen proof in docs/assembly-menu-source/.\n'
            'Building and packaging do not install anything. Use the receipt-based installer for a complete candidate.\n').encode('utf-8')


def _selected(base, scene):
    identifiers = _members(scene)
    by_id = {piece['id']: piece for piece in base['pieces']}
    require(len(by_id) == len(base['pieces']), 'Source build has repeated piece identifiers')
    require(set(identifiers) <= set(by_id), 'Source build omits an assembly component')
    return [by_id[identifier] for identifier in identifiers]


def _transformed(base, controller, menu, layout, scene, *, cycle_icon=None, expected_cycle_icon=None):
    from .build import RUL0, NETWORK_INI
    from .rul0 import with_feature_sequence
    from .menu_experiment_resources import build_menu_experiment_resources
    from .verify import strict_dbpf
    pieces = _selected(base, scene)
    resources = strict_dbpf(controller)
    require(set(resources) == {RUL0, NETWORK_INI}, 'Original controller has unexpected resources')
    if len(pieces) > 1:
        changed, composition = with_feature_sequence(resources[RUL0], base['overlay']['rul0'],
                                                     [number(piece['puzzle_id']) for piece in pieces])
    else:
        require('submenu' not in layout, 'A legacy cycle experiment needs at least two distinct piece types')
        changed, composition = resources[RUL0], deepcopy(base['overlay']['rul0'])
    controller_resources = {**resources, RUL0: changed}
    cycle = {**layout['cycle_button'], 'target_id': pieces[0]['menu']['id']}
    menu_resources, audit = build_menu_experiment_resources(
        strict_dbpf(menu), pieces, cycle_button=cycle, submenu=layout.get('submenu'),
        cycle_icon=cycle_icon, expected_cycle_icon=expected_cycle_icon)
    return pack_dbpf(controller_resources), pack_dbpf(menu_resources), composition, audit, pieces


def _game_checks(pieces, *, single_button=False):
    if single_button:
        rows = [
            {'id': 'single-assembly-entry', 'description': 'Transportation > Rail has exactly one entry for this assembly, no individual member buttons, and no assembly submenu; unrelated standalone pieces may remain.'},
            {'id': 'first-component', 'description': 'The assembly button starts on the first listed component.'},
            {'id': 'cycle-forward', 'description': f'Tab visits all {len(pieces)} distinct component types in the listed order, then wraps.'},
            {'id': 'cycle-backward', 'description': 'Shift+Tab visits the same component types in reverse order.'},
            {'id': 'rotate-current-type', 'description': 'Home and End rotate the current component without selecting another type.'},
            {'id': 'cancel-and-reselect', 'description': 'Escape cancels placement, and reselecting the assembly button starts on the first component.'},
            {'id': 'save-reload', 'description': 'Place test components, save, quit, reload, and inspect their models and network paths.'},
        ]
        rows += [{'id': 'cycle-component-' + piece['id'], 'piece_id': piece['id'],
                  'description': 'Reach this named component with Tab or Shift+Tab, confirm its preview, and place it at the assembly plan’s specified orientation.'}
                 for piece in pieces]
        return {'schema_version': 1,
                'purpose': 'Frozen pending menu checks at build time; this is not a human observation record or traffic approval.',
                'authority': 'Record explicit human observations separately against the candidate manifest fingerprint; preserve this template.',
                'environment_required': ['platform', 'game_version', 'NAM_profile'],
                'cases': [{**row, 'status': 'unverified', 'observations': []} for row in rows]}
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
    if 'submenu' not in layout:
        rows = [markdown_metadata('Assembly component menu',
                'Place reusable assembly components from one button, using Tab and Shift+Tab to change type.',
                'Players and testers', 'guide').rstrip(), '', '# Assembly component menu', '',
                'This assembly has one menu button. Each click places one reusable component; the button does not place the complete arrangement. The component menu presentations are replaced by this entry, while unrelated standalone piece buttons remain unchanged. Models, PATHs, shadows, and construction definitions retain their source bytes. Actual game behavior remains unverified.', '',
                '1. Open **Transportation → Rail**.',
                f'2. Click **{layout["cycle_button"]["title"]}**. The first component is **{pieces[0]["name"]}**.',
                f'3. Press **Tab** to select the next of {len(pieces)} component types, or **Shift+Tab** to select the previous type. Repeated placements of one type use the same cycle entry.',
                '4. Press **Home** or **End** to rotate the selected component. Follow the assembly placement plan, and click once to place that component.',
                '5. Press **Escape** to cancel placement. Select the assembly button again to start on its first component.',
                '6. Test the single entry, each type, forward and reverse cycling, rotation, cancellation, placement, and save/reload in a disposable city. Bind explicit observations to the candidate manifest and recorded game environment.', '',
                'The menu uses native construction-family ordering and does not require Submenus DLL for this presentation. The complete original menu and controller are retained outside the installable folder as verification proof. Do not install a second controller beside an existing SCP selection; use the receipt-based installer for a complete candidate. Building and packaging do not install anything.', '',
                'The [game-checks.json](game-checks.json) template remains unverified. Software validation does not approve menu activation, visible train operation, or the complete assembly in the game.', '',
                '| Tab position | Component name | Permanent piece ID |', '| --- | --- | --- |']
        rows += [f'| {index} | {piece["name"]} | `{piece["id"]}` |' for index, piece in enumerate(pieces, 1)]
        return ('\n'.join(rows) + '\n').encode()
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
    result['menu_experiment'] = {'kind': _presentation_kind(layout), 'schema_version': 1,
        'assembly_id': layout['assembly_id'], 'member_ids': [piece['id'] for piece in pieces],
        'source_inputs': proof, 'shared_tab_family': True,
        'construction_aliases_created': False, 'in_game_menu_tested': False}
    if 'submenu' not in layout:
        result['assembly_selection'] = {'assembly_id': layout['assembly_id'],
                                        'component_ids': [piece['id'] for piece in pieces]}
        result['source_provenance'] = {'kind': 'frozen-verified-piece-build',
                                       'manifest': proof['manifest']['path'],
                                       'documentation_root': f'{ASSEMBLY_PROOF}/documentation'}
    result['installed'] = False
    result['in_game_tested'] = False
    result['release']['public_release_ready'] = False
    message = ('Experimental menu access paths require explicit in-game observations; public release is blocked.'
               if 'submenu' in layout else 'Assembly menu behavior requires explicit in-game observations; public release is blocked.')
    result['release']['blocked'] = list(dict.fromkeys([*result['release'].get('blocked', []), message]))
    _, guide_path, checks_path = _presentation_paths(layout)
    additions = [*(proof[key] for key in sorted(proof)), _record(guide_path, _guide(layout, pieces)),
                 _record(checks_path, _json_bytes(_game_checks(pieces, single_button='submenu' not in layout)))]
    source_documents = [{**item, 'path': _source_documentation_path(layout, item['path'])}
                        for item in deepcopy(base.get('documentation', []))]
    if 'submenu' not in layout:
        additions.append(_record('README.txt', _assembly_readme(layout, pieces)))
    paths = {item['path'] for item in source_documents}
    require(not paths.intersection(item['path'] for item in additions), 'Experiment evidence overlaps source documentation')
    result['documentation'] = [*source_documents, *additions]
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
    cycle_id = number(layout['cycle_button']['id'])
    submenu_id = number(layout['submenu']['id']) if 'submenu' in layout else None
    presentation_ids = (cycle_id, submenu_id) if submenu_id is not None else (cycle_id,)
    expected_new = {(*prefix, iid) for iid in presentation_ids
                    for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)}
    removed = ({(*prefix, iid) for iid in selected for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)}
               if submenu_id is None else set())
    require(set(current) == (set(old) - removed) | expected_new and not set(old) & expected_new,
            'Experimental menu resource closure mismatch')
    for key in old:
        if key not in removed and (submenu_id is None or key[:2] != MENU_EXEMPLAR or key[2] not in selected):
            require(current[key] == old[key], 'Menu experiment changed an unrelated resource')
    props = lambda raw: {number(prop['id'].removeprefix('0x')): prop for prop in exemplar(raw)['properties']}
    for piece in pieces:
        iid = number(piece['menu']['id']); key = (*MENU_EXEMPLAR, iid)
        if submenu_id is None:
            require(all((*prefix, iid) not in current for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)),
                    'Assembly member retains a duplicate menu presentation')
            continue
        original, actual = props(old[key]), props(current[key])
        require(exemplar(old[key])['parent'] == exemplar(current[key])['parent'], 'Changed original menu parent cohort')
        require(set(actual) == set(original) | {0x8a2602ca, 0x8a2602cc}, 'Changed original button property closure')
        require(all(actual[key] == value for key, value in original.items()), 'Changed original button identity or property')
        require(actual[0x8a2602ca]['values'] == [submenu_id] and actual[0x8a2602cc]['values'] == [2],
                'Individual button has the wrong test submenu or class')
    cycle = props(current[*MENU_EXEMPLAR, cycle_id])
    require(cycle[0x8a2602bb]['values'] == [number(pieces[0]['menu']['id'])]
            and cycle[0x8a2602b8]['values'] == [cycle_id], 'Cycle entry does not target the first existing component')
    if submenu_id is not None:
        submenu = props(current[*MENU_EXEMPLAR, submenu_id])
        require(submenu[0x8a2602bb]['values'] == [submenu_id] and submenu[0x8a2602ca]['values'] == [0x29]
                and submenu[0x8a2602cc]['values'] == [1], 'Wrong test submenu root or class')
    else:
        require(0x8a2602ca not in cycle and 0x8a2602cc not in cycle,
                'Single assembly button unexpectedly requires submenu properties')
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
    require(isinstance(experiment, dict) and experiment.get('kind') in (KIND, ASSEMBLY_MENU_KIND)
            and experiment.get('schema_version') == 1, 'Unsupported menu experiment')
    proof = experiment.get('source_inputs')
    proof_root = PROOF if experiment['kind'] == KIND else ASSEMBLY_PROOF
    expected = {'manifest': f'{proof_root}/manifest.json', 'controller': f'{proof_root}/controller.proof',
                'menu': f'{proof_root}/menu.proof', 'layout': f'{proof_root}/layout.json', 'assembly': f'{proof_root}/assembly.json'}
    # New candidates freeze their source-derived silhouette. Historical
    # candidates without this proof retain exact generic-cycle validation.
    if isinstance(proof, dict) and 'icon' in proof:
        expected['icon'] = f'{proof_root}/icon.png'
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
    # PNG compression may vary between Pillow versions. Validate the saved
    # cycle artwork's exact pixels, then retain its original encoded bytes.
    from .verify import strict_dbpf
    current_menu = strict_dbpf(safe_file(output, f'{base["plugin_folder"]}/{MENU}').read_bytes())
    cycle_key = (*ICON, number(layout['cycle_button']['id']))
    require(cycle_key in current_menu, 'Missing assembly cycle icon resource')
    controller, menu, composition, audit, _ = _transformed(
        base, raw['controller'], raw['menu'], layout, scene, cycle_icon=current_menu[cycle_key],
        expected_cycle_icon=raw.get('icon'))
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
                document = item['path'] in {row['path'] for row in base.get('documentation', [])}
                candidate_path = _source_documentation_path(layout, item['path']) if document else item['path']
                payload = raw['controller'] if item['path'] == controller_path else raw['menu'] if item['path'] == menu_path else safe_file(output, candidate_path).read_bytes()
                destination.write_bytes(payload)
            (restored / 'manifest.json').write_bytes(raw['manifest'])
            if (output / 'input-audit.json').is_file():
                shutil.copy2(output / 'input-audit.json', restored / 'input-audit.json')
            report = verify_build(restored, write_report=False)
        if len(_BASELINE_REPORTS) >= 2:
            _BASELINE_REPORTS.clear()
        _BASELINE_REPORTS[cache_key] = deepcopy(report)
    legacy = 'submenu' in layout
    report = {'schema_version': 1, 'static_checks_passed': True,
        'files_checked': len(manifest['files']), 'documentation_files_checked': len(manifest['documentation']),
        'source_build_verification': report,
        'source_build_verification_reused_in_process': reused,
        'menu_experiment': {'kind': _presentation_kind(layout), 'assembly_id': layout['assembly_id'],
        'source_build_verified': True, 'all_piece_assets_preserved': True, 'piece_types_preserved': len(base['pieces']),
        'component_types_in_cycle': len(pieces), 'individual_submenu_buttons': len(pieces) if legacy else 0,
        'new_presentation_resources': 8 if legacy else 4, 'network_ini_preserved': True, 'construction_definitions_preserved': True,
        'custom_type_families': len(base['pieces']) - len(pieces) + 1,
        'grouped_type_rows': len(pieces), 'add_types_rows': len(pieces) - 1,
        'shared_tab_family': True, 'alias_activation_and_visibility': 'unverified',
        'pending_game_cases': len(_game_checks(pieces, single_button=not legacy)['cases'])},
        'in_game_menu_tested': False,
        'verification_limit': ('Strict source-build validation and exact menu/controller transformation; actual DLL menu visibility, network selection, Tab behavior, and game operation remain unverified.'
            if legacy else 'Strict source-build validation and exact single-button menu/controller transformation; actual menu activation, Tab behavior, and game operation remain unverified.')}
    if not legacy:
        report['menu_experiment'].update(assembly_menu_buttons=1, member_buttons_hidden=len(pieces),
                                         unrelated_piece_buttons_preserved=len(base['pieces']) - len(pieces),
                                         removed_member_presentation_resources=4 * len(pieces),
                                         submenus_dll_required=False)
    if write_report:
        (output / 'verification.json').write_bytes(_json_bytes(report))
    return report


def _assembly_icon_path(root, assembly):
    relative = assembly['path'] + '/icon.png'
    path = Path(root) / relative
    require(path == safe_relative(root, relative) and
            not any(parent.is_symlink() for parent in (path, *path.parents)),
            'Assembly icon path must not redirect through symbolic links')
    return path


def _assembly_icon_routes(assembly, catalog):
    """Ask the owning domain for its placed source routes, without game inputs."""
    from .providers import domain_module
    adapter = domain_module({'domain': assembly['domain']}, 'icons')
    require(hasattr(adapter, 'assembly_icon_routes'),
            f'{assembly["domain"]}: no source-derived assembly icon adapter')
    return adapter.assembly_icon_routes(assembly['scene'], catalog['pieces'])


def _assembly_icon_network(assembly):
    """Require the owning domain's declared network instead of guessing HSR."""
    from .providers import domain_module
    adapter = domain_module({'domain': assembly['domain']}, 'icons')
    require(hasattr(adapter, 'assembly_icon_network'),
            f'{assembly["domain"]}: no declared assembly icon network adapter')
    return adapter.assembly_icon_network(assembly['id'])


def write_assembly_icons(project_root, *, domain_id='high-speed-rail'):
    """Refresh canonical assembly icons and their source-schematic provenance."""
    from . import menu_experiment_resources
    from .menu_experiment_resources import make_assembly_icon, validate_assembly_icon
    root = Path(project_root).resolve()
    catalog = load_catalog(root)
    require(domain_id in catalog['domains'], 'Unknown assembly icon domain')
    assemblies = [assembly for assembly in catalog['_assemblies'] if assembly['domain'] == domain_id]
    targets = [_assembly_icon_path(root, assembly) for assembly in assemblies]
    # Resolve every assembly before changing any icon; malformed source data
    # must not leave a partly refreshed selection behind.
    routes = [_assembly_icon_routes(assembly, catalog) for assembly in assemblies]
    networks = [_assembly_icon_network(assembly) for assembly in assemblies]
    artworks = [make_assembly_icon(points, network_label=network)
                for points, network in zip(routes, networks)]
    evidence_paths = []
    for assembly, points, network, path, raw in zip(assemblies, routes, networks, targets, artworks):
        current = None
        if path.is_file():
            try:
                validate_assembly_icon(path.read_bytes(), expected_icon=raw)
            except ValueError:
                pass
            else:
                current = path.read_bytes()
        if current is None:
            path.write_bytes(raw)
            current = raw
        member_ids = set(_members(assembly['scene']))
        evidence = {'schema_version': 1,
            'purpose': 'Reproduce the assembly menu schematic from the current placed source routes.',
            'basis': 'Authored complete routes transformed by assembly.json placements; no compiled model rendering.',
            'generator': 'scp.menu_experiment.write_assembly_icons',
            'generator_sha256': {'scp.menu_experiment': _sha(Path(__file__).read_bytes()),
                'scp.menu_experiment_resources': _sha(Path(menu_experiment_resources.__file__).read_bytes())},
            'assembly_source_sha256': _sha(_json_bytes(assembly['scene'])),
            'placed_routes_sha256': _sha(_json_bytes(points)),
            'labels': {'brand': 'SCP', 'brand_position': 'top-left',
                       'category': 'ASM', 'network': network, 'footer_position': 'bottom-centre'},
            'footer_ink_rows_px': [33, 37],
            'piece_definitions_sha256': {piece['id']: _sha(_json_bytes(piece))
                for piece in catalog['pieces'] if piece['id'] in member_ids},
            'output': {'path': 'icon.png', 'sha256': _sha(current), 'dimensions_px': [176, 44],
                'frame_order': ['locked', 'normal', 'selected', 'highlighted'], 'frame_size_px': [44, 44]},
            'compiled_resource_verification': 'separate', 'in_game_appearance': 'unverified'}
        evidence_relative = assembly['path'] + '/evidence/icon.json'
        evidence_path = root / evidence_relative
        require(evidence_path == safe_relative(root, evidence_relative)
                and not any(parent.is_symlink() for parent in (evidence_path, *evidence_path.parents)),
                'Assembly icon evidence path must not redirect through symbolic links')
        evidence_path.parent.mkdir(parents=True, exist_ok=True)
        evidence_path.write_bytes(_json_bytes(evidence))
        evidence_paths.append(evidence_path.relative_to(root).as_posix())
    return {'domain': domain_id, 'icons': [path.relative_to(root).as_posix() for path in targets],
            'evidence': evidence_paths, 'built': False, 'installed': False}


def build_menu_experiment(project_root, source, output, *, layout_id='trumpet-menu-test',
                          domain_id='high-speed-rail', plugins=None, extra_roots=None,
                          single_button_only=False):
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
    if layout_id == 'trumpet-menu-test' and layout_id not in config['layouts'] and 'trumpet' in config['layouts']:
        layout_id = 'trumpet'
    require(layout_id in config['layouts'], 'Unknown assembly menu layout')
    layout = _layout(config['layouts'][layout_id])
    require(not single_button_only or 'submenu' not in layout,
            'Assembly delivery requires one cycle button; legacy submenu layouts are not supported by assembly-menu')
    assemblies = [assembly for assembly in catalog['_assemblies']
                  if assembly['id'] == layout['assembly_id'] and assembly['domain'] == domain_id]
    require(len(assemblies) == 1, 'Menu experiment must select one registered assembly')
    scene = assemblies[0]['scene']
    from .menu_experiment_resources import make_assembly_icon, validate_assembly_icon
    icon_path = _assembly_icon_path(root, assemblies[0])
    require(icon_path.is_file(), 'Missing canonical assembly icon; generate it with assembly-icons')
    cycle_icon = icon_path.read_bytes()
    expected_cycle_icon = make_assembly_icon(_assembly_icon_routes(assemblies[0], catalog),
                                            network_label=_assembly_icon_network(assemblies[0]))
    validate_assembly_icon(cycle_icon, expected_icon=expected_cycle_icon)
    base = _read_json(source / 'manifest.json')
    require('menu_experiment' not in base,
            'Source must be a normal verified build; combining assembly cycles or reusing their shared types is unsupported')
    _check_source_files(source, base)
    pieces = _selected(base, scene)
    current = {piece['id']: piece for piece in catalog['pieces']}
    for piece in pieces:
        require({key: value for key, value in piece.items() if key != 'asset_file'} == current.get(piece['id']),
                'Assembly component definition differs from current authoring metadata')
    _, installed, donors, _ = audit_inputs(catalog, plugins, base['pieces'], extra_roots)
    proposed = {number(layout[key]['id']) for key in ('cycle_button', 'submenu') if key in layout}
    used_ids = {key[2] for key in installed} | {number(piece['menu']['id']) for piece in catalog['pieces']}
    require(not proposed & used_ids, 'Experimental presentation identifier collides with existing content')
    folder = base['plugin_folder']
    original_controller = (source / folder / CONTROLLER).read_bytes()
    original_menu = (source / folder / MENU).read_bytes()
    controller, menu, composition, audit, pieces = _transformed(
        base, original_controller, original_menu, layout, scene, cycle_icon=cycle_icon,
        expected_cycle_icon=expected_cycle_icon)
    proof_raw = {'manifest': (source / 'manifest.json').read_bytes(), 'controller': original_controller,
                 'menu': original_menu, 'layout': _json_bytes(layout), 'assembly': _json_bytes(scene),
                 'icon': cycle_icon}
    proof_names = {'manifest': 'manifest.json', 'controller': 'controller.proof', 'menu': 'menu.proof',
                   'layout': 'layout.json', 'assembly': 'assembly.json', 'icon': 'icon.png'}
    proof_root, guide_path, checks_path = _presentation_paths(layout)
    proof = {key: _record(f'{proof_root}/{proof_names[key]}', raw) for key, raw in proof_raw.items()}
    manifest = _expected_manifest(base, layout, scene, proof, controller, menu, composition, audit)
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.scp-menu-test-', dir=output.parent))
    try:
        shutil.copytree(source, stage, dirs_exist_ok=True)
        if 'submenu' not in layout:
            for item in base.get('documentation', []):
                original = safe_relative(stage, item['path'])
                frozen = safe_relative(stage, _source_documentation_path(layout, item['path']))
                frozen.parent.mkdir(parents=True, exist_ok=True)
                require(not frozen.exists(), 'Frozen source documentation path collides with source content')
                original.replace(frozen)
            for directory in sorted(stage.rglob('*'), key=lambda path: len(path.parts), reverse=True):
                if directory.is_dir() and not any(directory.iterdir()):
                    directory.rmdir()
            (stage / 'README.txt').write_bytes(_assembly_readme(layout, pieces))
        for key, raw in proof_raw.items():
            target = stage / proof[key]['path']; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(raw)
        for name, raw in ((f'{folder}/{CONTROLLER}', controller), (f'{folder}/{MENU}', menu),
                          (guide_path, _guide(layout, pieces)),
                          (checks_path, _json_bytes(_game_checks(pieces, single_button='submenu' not in layout)))):
            target = stage / name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(raw)
        (stage / 'manifest.json').write_bytes(_json_bytes(manifest))
        report = verify_build(stage)
        os.replace(stage, output)
    finally:
        if stage.exists(): shutil.rmtree(stage)
    result = {'output': str(output), 'guide': str(output / guide_path), 'assembly_id': layout['assembly_id'],
            'piece_types_preserved': len(base['pieces']), 'assembly_component_types': len(pieces),
            'cycle_button': layout['cycle_button']['title'],
            'static_checks_passed': report['static_checks_passed'], 'in_game_menu_tested': False,
            'presentation_identifier_conflicts': 0,
            'dependency_donors_checked': len(donors), 'installed': False}
    if 'submenu' in layout:
        result['test_submenu'] = layout['submenu']['title']
    else:
        result.update(assembly_menu_buttons=1, member_buttons_hidden=len(pieces), submenus_dll_required=False)
    return result


def build_assembly_menu(project_root, source, output, *, layout_id='trumpet',
                        domain_id='high-speed-rail', plugins=None, extra_roots=None):
    """Prepare one assembly entry and hide its members, preserving source proof."""
    return build_menu_experiment(project_root, source, output, layout_id=layout_id,
                                domain_id=domain_id, plugins=plugins, extra_roots=extra_roots,
                                single_button_only=True)
