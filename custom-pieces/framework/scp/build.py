"""Compose all selected author deltas against one audited NAM baseline."""
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import zipfile

from . import jsonc
from .paths import local_settings
from .catalog import load_catalog, select_pieces, release_status
from .dbpf import COMPRESSION_DIRECTORY_TYPE, entries, decompress, index_plugins, pack_dbpf, require, tgi_string
from .menu import build_menu_resources
from .recipes import build_piece
from .rul0 import MARKER, compose_rul0
from .adaptive_network import RUL1, bindings as adaptive_bindings, resource_keys as adaptive_resource_keys, compose_rul1
from . import native_approaches
from . import model_shadows
from . import piece_menu_families, transport_menu

RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
NETWORK_INI = (0, 0x8A5971C5, 0x8A5993B9)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(path, data):
    Path(path).write_text(json.dumps(data, sort_keys=True, indent=2) + '\n')


def merge_resources(target, addition, owner):
    overlap = set(target) & set(addition)
    require(not overlap, f'{owner}: duplicate resources {[tgi_string(x) for x in sorted(overlap)]}')
    target.update(addition)


def roots_for(project_root, plugins, extra_roots=None):
    local = local_settings(project_root)
    settings = jsonc.load(local) if local.is_file() else {}
    extras = settings.get('extra_plugins', []) if extra_roots is None else extra_roots
    roots = [Path(plugins).expanduser().resolve()] + [Path(x).expanduser().resolve() for x in extras]
    require(len(roots) == len(set(roots)), 'Duplicate Plugins scan root')
    require(all(root.is_dir() for root in roots), 'One of the Plugins scan roots is missing')
    require(not any(a != b and a.is_relative_to(b) for a in roots for b in roots), 'Nested Plugins scan roots')
    return roots


def audit_inputs(catalog, plugins, pieces, extra_roots=None):
    roots = roots_for(catalog['_root'], plugins, extra_roots)
    managed = Path(plugins).resolve() / catalog['plugin_folder']
    if managed.exists():
        from .install import _owned
        _owned(managed)  # Exclude only a verified managed installation.
    indexes = [index_plugins(root, exclude=managed if managed.is_relative_to(root) else None) for root in roots]
    installed = {}
    for index in indexes:
        for key, paths in index.items():
            installed.setdefault(key, []).extend(paths)
    context, audit, dependency_paths = {}, [], {}
    needed = sorted({label for piece in pieces for label in piece['dependencies']})
    archives = {path for paths in installed.values() for path in paths}
    for label in needed:
        require(label in catalog['_profile']['files'], f'Unknown dependency: {label}')
        record = catalog['_profile']['files'][label]
        matches = sorted(path for path in archives if path.name == record['filename'])
        require(len(matches) == 1, f"Expected one {record['filename']}, found {len(matches)} across scanned Plugins roots")
        path = matches[0]; raw = path.read_bytes()
        digest = sha(raw)
        require(digest == record['sha256'], f'{path.name} changed. Re-audit this NAM version; do not just change the fingerprint.')
        context[label] = {key: decompress(value) for key, value in entries(raw).items()}
        dependency_paths[label] = path
        audit.append({'filename': path.name, 'path': str(path), 'sha256': digest})
    native = next(Path(x['path']) for x in audit if x['filename'] == 'NetworkAddonMod_Controller.dat')
    shared = (RUL0, NETWORK_INI, RUL1) if any(adaptive_bindings(piece) or native_approaches.approaches(piece)
                                              for piece in pieces) else (RUL0, NETWORK_INI)
    required_controller = native_approaches.required_controller_resources(pieces)
    for key in dict.fromkeys((*shared, *required_controller)):
        require(installed.get(key) == [native],
                f'Conflicting shared NAM overlay {tgi_string(key)} in '
                + ', '.join(str(path) for path in installed.get(key, []))
                + '. Move the old standalone prototype out of Plugins, or merge the other custom controller first.')
    for key, fingerprint in required_controller.items():
        require(key in context['controller'] and sha(context['controller'][key]) == fingerprint,
                'Native approach controller dependency changed: ' + tgi_string(key))
    native_approaches.audit_dependencies(pieces, context, installed, dependency_paths)
    model_shadows.audit_lighting_dependency(context, installed, pieces)
    return context, installed, audit, roots


def preflight_allocations(context, installed, selected):
    """Reject identifier conflicts before spending time on large junction models."""
    from .track_paths import S3D, PATH, EXEMPLAR, LTEXT, EFFECT
    from .menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
    native = context['controller'][RUL0]
    native_puzzles = {int(value,16) & 0xffff for value in
                      re.findall(rb'\[HighwayIntersectionInfo_0x([0-9a-f]+)\]', native, re.I)}
    planned = set()
    for piece in selected:
        puzzle = int(piece['puzzle_id'],16)
        require(puzzle not in native_puzzles, f'{piece["id"]}: puzzle ID already used by NAM')
        require(piece['effect_name'].encode('ascii') not in native,
                f'{piece["id"]}: preview effect name already used by NAM')
        menu, preview = int(piece['menu']['id'],16), int(piece['preview_id'],16)
        planned.update({(*prefix,menu) for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)})
        planned.update({(*S3D,preview),(*EFFECT,preview)})
        for raw_tile in piece['tile_ids']:
            tile = int(raw_tile,16)
            planned.update({(*S3D,tile+zoom) for zoom in range(5)})
            planned.update({(*prefix,tile) for prefix in (PATH, EXEMPLAR, LTEXT)})
            if piece.get('shadow_mode') == 'generated' or piece['recipe'].startswith(('rail_', 'interchange_', 'directional_', 'hsr_component_')):
                planned.update({(0x7AB50E44,0x2BC2759A,tile+zoom) for zoom in range(5)})
        planned.update({(0x7AB50E44, 0x1ABE787D, int(value, 16))
                        for value in piece.get('authored_texture_ids', [])})
        planned.update(adaptive_resource_keys(piece))
        planned.update(model_shadows.resource_keys(piece))
    conflicts = planned & set(installed)
    require(not conflicts, 'Allocated resource identifiers collide with installed content: '
            + ', '.join(tgi_string(key) for key in sorted(conflicts)[:8]))
    return {'allocated_resources_checked':len(planned),'native_puzzle_ids_checked':len(selected),
            'allocated_identifier_conflicts':0}


def doctor(project_root, plugins, include=None, extra_roots=None):
    catalog = load_catalog(project_root); selected = select_pieces(catalog, include)
    require(selected, 'No pieces selected')
    context, installed, donors, roots = audit_inputs(catalog, plugins, selected, extra_roots)
    allocation_report = preflight_allocations(context, installed, selected)
    return {'compatible': True, 'profile': catalog['_profile']['id'],
            'pieces': [x['id'] for x in selected], 'archives': len({p for paths in installed.values() for p in paths}),
            'scanned_roots': [str(p) for p in roots], 'donors': donors,
            'public_ids_reserved': catalog.get('public_ids_reserved', False), **allocation_report,
            'scan_coverage': 'Only the explicitly listed roots; configure every active Plugins root.'}


def _prepare_output(output, project_root, roots):
    path = Path(output).expanduser().absolute()
    require(not any(x.is_symlink() for x in (path, *path.parents)), 'Output path contains a symlink')
    output = path.resolve()
    project_root = Path(project_root).resolve()
    require(output != project_root and not project_root.is_relative_to(output), 'Output cannot contain framework sources')
    for root in roots:
        require(not output.is_relative_to(root) and not root.is_relative_to(output), 'Build output must stay outside Plugins')
    if output.exists():
        require((output / 'manifest.json').is_file(), 'Output directory is not an SCP build; refusing to replace it')
        previous = json.loads((output / 'manifest.json').read_text())
        require(previous.get('plugin_folder') == 'zzz_Simons_Custom_Pieces' and previous.get('schema_version') == 1,
                'Output directory is not an owned SCP build')
        verify_build(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    return output


def _compile_piece(piece, context, donors, plugin_folder):
    model_report = None
    try:
        resources, delta = build_piece(piece, context)
        record = {**deepcopy(piece), 'asset_file': f"{plugin_folder}/20_Pieces/SCP_{piece['id']}.dat"}
        if (piece.get('domain', 'high-speed-rail') != 'high-speed-rail' or
                piece['recipe'].startswith(('interchange_', 'directional_', 'hsr_component_')) or
                piece['recipe'].startswith('rail_') and piece['recipe'].endswith('_revised')):
            # Fail on invalid per-piece geometry before staging. Saved-build
            # verification still checks the actual DATs and coordinated rules.
            from .verify import check_piece_paths, check_piece_models
            check_piece_paths(resources, record)
            checked = check_piece_models(resources, record, donors)
            if piece.get('domain') == 'highway':
                model_report = checked
    except ValueError as error:
        raise ValueError(f'{piece["id"]}: {error}') from error
    return resources, delta, record, model_report


def _compile_groups(pieces):
    """Keep pieces that share costly recipe geometry in one worker."""
    from .providers import domain_module

    groups = {}
    for piece in pieces:
        group = getattr(domain_module(piece, 'recipes'), 'compilation_group', None)
        family = group(piece) if group is not None else None
        key = (piece['domain'], family) if family is not None else piece['id']
        groups.setdefault(key, []).append(piece)
    return sorted(groups.values(),
                  key=lambda group: sum(len(piece['tile_ids']) for piece in group), reverse=True)


def _init_build_worker(context, donors, plugin_folder, source_root):
    from .check_bootstrap import SourcePackages

    # A fresh Python process does not inherit the installer's import finder.
    sys.meta_path.insert(0, SourcePackages(source_root))
    global _worker_inputs
    _worker_inputs = (context, donors, plugin_folder)


def _compile_group(pieces):
    from .shadows import compiled_shadow_sets

    with compiled_shadow_sets() as shadows:
        compiled = [_compile_piece(piece, *_worker_inputs) for piece in pieces]
    return compiled, shadows


def _compile_in_parallel(groups, workers, context, donors, plugin_folder, progress):
    from concurrent.futures import ProcessPoolExecutor, as_completed
    from concurrent.futures.process import BrokenProcessPool
    from multiprocessing import get_context
    from .paths import project_root

    compiled, shadows = {}, {}
    count = sum(len(group) for group in groups)
    pool = ProcessPoolExecutor(
        max_workers=workers, mp_context=get_context('spawn'),
        initializer=_init_build_worker, initargs=(context, donors, plugin_folder, project_root()))
    try:
        futures = [pool.submit(_compile_group, group) for group in groups]
        for future in as_completed(futures):
            results, group_shadows = future.result()
            shadows.update(group_shadows)
            for resources, delta, record, model_report in results:
                identifier = record['id']
                compiled[identifier] = (resources, delta, record, model_report)
                if progress:
                    progress({'phase': 'compile', 'index': len(compiled), 'pieces': count,
                              'piece': identifier})
    except BrokenProcessPool as error:
        raise ValueError('A build worker stopped unexpectedly. Retry with --jobs 1 for a serial build.') from error
    finally:
        pool.shutdown(cancel_futures=True)
    return compiled, shadows


def build_project(project_root, plugins, output, include=None, extra_roots=None, progress=None, *, jobs=1):
    """Compile one deterministic build, optionally using separate Python processes."""
    require(jobs is None or type(jobs) is int and jobs > 0, 'Build jobs must be a positive integer')
    catalog = load_catalog(project_root); selected = select_pieces(catalog, include)
    require(selected, 'No pieces selected')
    piece_menu_families.declarations(selected, available=catalog['pieces'])
    if progress:
        progress({'phase':'audit','pieces':len(selected)})
    context, installed, donor_audit, roots = audit_inputs(catalog, plugins, selected, extra_roots)
    preflight_allocations(context, installed, selected)
    hierarchy = transport_menu.plan(catalog, selected)
    roster = transport_menu.members({'pieces': selected, transport_menu.KEY: hierarchy}) if hierarchy else {}
    if roster:
        used_ids = {key[2] for key in installed} | {int(piece['menu']['id'], 16) for piece in catalog['pieces']}
        transport_menu.check_ids(roster, used_ids)
    output = _prepare_output(output, project_root, roots)
    baseline = context['controller']
    labels = sorted({label for piece in selected for label in piece['dependencies']})
    donors = {key: raw for label in labels for key, raw in context[label].items()}
    model_donors = {key: raw for key, raw in donors.items() if key[0] != COMPRESSION_DIRECTORY_TYPE}
    assets_by_piece, menu_resources, all_resources, rules, menu_audit = {}, {}, {}, [], []
    rul1_rules = []
    records = []
    # Check every selected identifier against the native rules before dispatch.
    native_rul = baseline[RUL0].decode('ascii')
    for piece in selected:
        require(not re.search(r'HighwayIntersectionInfo_0x[0-9a-f]{4}' + piece['puzzle_id'] + r'\]', native_rul, re.I),
                f"Puzzle id {piece['puzzle_id']} already used by NAM")
        require(piece['effect_name'].encode() not in baseline[RUL0], 'Preview effect name already used')
    compiled, shadow_sets = None, {}
    if jobs != 1 and len(selected) > 1 and not getattr(sys, 'frozen', False):
        cpus = getattr(os, 'process_cpu_count', os.cpu_count)() or 1
        limit = min(cpus, 61) if sys.platform == 'win32' else cpus
        workers = min(limit, jobs if jobs is not None else 4)
        if workers > 1:
            groups = _compile_groups(selected)
            workers = min(workers, len(groups))
            if workers > 1:
                compiled, shadow_sets = _compile_in_parallel(
                    groups, workers, context, model_donors, catalog['plugin_folder'], progress)
    from .providers import domain_module
    highway_audits = {}
    for index, piece in enumerate(selected):
        if compiled is None:
            if progress:
                progress({'phase':'compile','index':index+1,'pieces':len(selected),'piece':piece['id']})
            resources, delta, record, _ = _compile_piece(piece, context, model_donors, catalog['plugin_folder'])
        else:
            resources, delta, record, model_report = compiled.pop(piece['id'])
            if model_report is not None:
                highway_audits[piece['id']] = (record, resources, model_report)
        try:
            donor = domain_module(piece, 'menu').menu_donor(context)
            menus, metadata = build_menu_resources(donor, piece)
        except ValueError as error:
            raise ValueError(f'{piece["id"]}: {error}') from error
        merge_resources(all_resources, resources, piece['id']); merge_resources(all_resources, menus, piece['id'])
        merge_resources(menu_resources, menus, piece['id'])
        if isinstance(delta, dict):
            require(set(delta) == {'rul0', 'rul1'} and adaptive_bindings(piece)
                    and all(isinstance(value, str) and value for value in delta.values()),
                    'Only explicitly adaptive pieces may emit RUL0/RUL1 delta objects')
            rules.append(delta['rul0']); rul1_rules.append(delta['rul1'])
        else:
            require(isinstance(delta, str) and not adaptive_bindings(piece),
                    'Adaptive pieces must declare their RUL1 construction delta')
            rules.append(delta)
        assets_by_piece[piece['id']] = resources; menu_audit.append(metadata)
        records.append(record)
    require(not (set(all_resources) & set(installed)), 'Allocated resource identifiers collide with installed content')
    rul0, rul0_delta = compose_rul0(baseline[RUL0], rules)
    rul0, rul0_delta, menu_resources, menu_families = piece_menu_families.apply(
        rul0, rul0_delta, menu_resources, selected, available=catalog['pieces'])
    menu_resources = transport_menu.arrange(menu_resources, roster)
    shadow_lines = []
    for piece in selected:
        for mapping in piece['shadow_mappings']:
            shadow_lines.append(f"scp_{piece['id']} = 0x{mapping['tile']},0xFFFFFFF0,0x{mapping['source']},0x0000000F,{mapping['rotation']},0\r\n")
    insertion = ';BEGIN SIMONS CUSTOM PIECES SHADOWS\r\n' + ''.join(shadow_lines) + ';END SIMONS CUSTOM PIECES SHADOWS\r\n'
    anchor = b'[Shadow remapping]\r\n'
    require(baseline[NETWORK_INI].count(anchor) == 1, 'Shadow mapping anchor missing or ambiguous')
    network_ini = baseline[NETWORK_INI].replace(anchor, anchor + insertion.encode('ascii'), 1)
    require(network_ini.replace(insertion.encode('ascii'), b'', 1) == baseline[NETWORK_INI], 'Shadow patch is not reversible')
    controller = {RUL0: rul0, NETWORK_INI: network_ini}
    rul1_delta = None
    if rul1_rules:
        controller[RUL1], rul1_delta = compose_rul1(baseline[RUL1], rul1_rules, selected)
    native_approach_delta = None
    if native_approaches.declarations(selected):
        controller[RUL1], native_approach_delta = native_approaches.compose_rul1(
            controller.get(RUL1, baseline[RUL1]), selected, donors)
    texture_ids = set()
    from .models import parse_s3d
    for resources in assets_by_piece.values():
        for key, raw in resources.items():
            if key[0] == 0x5AD0E817:
                texture_ids |= {t for mat in parse_s3d(raw)['materials'] for t in mat['textures']}
    textures = []
    for iid in sorted(texture_ids):
        key = (0x7AB50E44, 0x1ABE787D, iid)
        if key in all_resources:
            continue
        require(key in installed, f'Missing model texture {iid:08x}')
        textures.append(tgi_string(key))
    shadows = sorted({(0x7AB50E44, 0x2BC2759A, int(m['source'], 16) + zoom)
                      for piece in selected for m in piece['shadow_mappings'] for zoom in range(5)
                      if (0x7AB50E44, 0x2BC2759A, int(m['source'], 16) + zoom) not in all_resources})
    require(all(key in installed for key in shadows), 'Missing native HSR shadow dependency')
    stage = Path(tempfile.mkdtemp(prefix='.scp-build-', dir=output.parent))
    old = None
    try:
        folder = stage / catalog['plugin_folder']; (folder / '20_Pieces').mkdir(parents=True)
        payloads = {f"{catalog['plugin_folder']}/00_SCP_Controller_NAM50.dat": pack_dbpf(controller),
                    f"{catalog['plugin_folder']}/10_SCP_Menu.dat": pack_dbpf(menu_resources)}
        for record in records:
            payloads[record['asset_file']] = pack_dbpf(assets_by_piece[record['id']])
        file_records = []
        for relative, raw in sorted(payloads.items()):
            (stage / relative).write_bytes(raw)
            file_records.append({'path': relative, 'sha256': sha(raw), 'bytes': len(raw)})
        profile = {'id': catalog['_profile']['id'], 'donors': [{k: x[k] for k in ('filename', 'sha256')} for x in donor_audit]}
        domains = {piece.get('domain', 'high-speed-rail') for piece in selected}
        placement = ("In Transportation > Rail, find the separate SCP icons.\n"
                     "One-way tracks are fixed click-to-place pieces. Join them to the mainline through SCP Split/Merge.\n"
                     "Their eight button states are four rotations repeated; there are no directional reflections.\n"
                     "Custom shadow projection and wheel/rail fit still need in-game inspection.\n"
                     if domains == {'high-speed-rail'} else
                     "Highway components are in Transportation > Highways. Rail components, if selected, are in Transportation > Rail.\n"
                     "Place the reusable components in the order and orientation shown in their assembly guide.\n"
                     "Eight highway button states repeat four proper rotations; they do not reflect traffic directions.\n"
                     "Placement, vehicle travel, custom shadows, and save/reload still need in-game inspection.\n")
        if hierarchy:
            for domain, category in (('high-speed-rail', 'Rail'), ('highway', 'Highways')):
                if domain in hierarchy['domains']:
                    path = f'Transportation > {category}'
                    placement = placement.replace(path, f'{path} > SCP > Pieces')
            placement += ("SCP folders require Submenus DLL, SC4ResourceLoadingHooks DLL, "
                          "and submenu-essentials.dat.\n")
        readme = ("Simon's Custom Pieces\nDEVELOPMENT BUILD — NOT GAME-TESTED\n"
                  "Requires the exact NAM profile recorded in manifest.json.\n"
                  "Use scp.py install with an external backup folder; test in a disposable city.\n"
                  + placement +
                  "Use only the single coordinated controller overlay included in this build.\n"
                  "Public binary redistribution is not cleared. See framework docs/RELEASE.md.\n").encode('utf8')
        (stage / 'README.txt').write_bytes(readme)
        documentation = [{'path': 'README.txt', 'sha256': sha(readme), 'bytes': len(readme)}]
        from .export import copy_documentation
        documentation.extend(copy_documentation(project_root, stage, sha))
        manifest = {'schema_version': 1, 'name': catalog['name'], 'version': catalog['version'],
                    'plugin_folder': catalog['plugin_folder'], 'profile': profile, 'pieces': records,
                    'files': file_records, 'documentation': documentation, 'menu_audit': menu_audit,
                    'overlay': {'rul0': rul0_delta,
                                'network_ini': {'base_sha256': sha(baseline[NETWORK_INI]), 'insertion': insertion}},
                    'dependency_audit': {'textures': textures, 'shadows': [tgi_string(k) for k in shadows]},
                    'release': release_status(project_root, selected),
                    'installed': False, 'in_game_tested': False}
        if hierarchy:
            manifest[transport_menu.KEY] = hierarchy
        if rul1_delta is not None:
            manifest['overlay']['rul1'] = rul1_delta
        if native_approach_delta is not None:
            manifest['overlay'][native_approaches.OVERLAY] = native_approach_delta
        if menu_families is not None:
            manifest[piece_menu_families.KEY] = menu_families
        from .release import assess_build
        manifest['release'] = assess_build(Path(project_root), manifest)
        write_json(stage / 'manifest.json', manifest)
        write_json(stage / 'input-audit.json', {'donors': donor_audit, 'scanned_roots': [str(x) for x in roots]})
        if progress:
            progress({'phase':'verify','pieces':len(selected)})
        from .shadows import compiled_shadow_sets
        from .verify import compiled_highway_model_audits
        with compiled_shadow_sets(shadow_sets), compiled_highway_model_audits() as audits:
            if highway_audits:
                audits['donors'] = model_donors
                audits['pieces'] = highway_audits
            report = verify_build(stage)
        # Transaction: complete verification precedes any replacement of old build.
        if output.exists():
            old = Path(tempfile.mkdtemp(prefix='.scp-old-', dir=output.parent)); old.rmdir()
            os.replace(output, old)
        try:
            os.replace(stage, output)
        except BaseException:
            if old is not None:
                os.replace(old, output); old = None
            raise
        if old is not None:
            shutil.rmtree(old)
        return {'output': str(output), 'pieces': [x['id'] for x in selected],
                'separate_menu_buttons': len(selected) - len(piece_menu_families.hidden_members(selected)),
                'static_checks_passed': report['static_checks_passed'],
                'installed': False, 'public_release_ready': manifest['release']['public_release_ready']}
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def verify_build(output, *, write_report=True):
    from .verify import verify_build as verify
    return verify(Path(output), write_report=write_report)


def package_build(output, destination, release=False, project_root=None, *, refresh_docs=False):
    output, destination = Path(output).resolve(), Path(destination).absolute()
    verify_build(output, write_report=False)
    manifest = json.loads((output / 'manifest.json').read_text())
    if 'menu_experiment' in manifest:
        require(not release and not refresh_docs,
                'Menu experiments require their frozen proof documentation and cannot be public releases')
        from .dbpf import EXTENSIONS
        require(all(Path(item['path']).suffix.lower() not in EXTENSIONS
                    for item in manifest.get('documentation', [])),
                'Menu experiment evidence must not use loadable plugin extensions')
    require(type(refresh_docs) is bool, 'refresh_docs must be a boolean')
    require(not refresh_docs or project_root is not None, 'Refreshing package documentation needs the current project root')
    if release:
        require(project_root is not None, 'Release needs current project evidence')
        current = load_catalog(project_root)
        require(current['version'] == manifest['version'], 'Rebuild after changing project version')
        from .release import assess_build
        status = assess_build(Path(project_root), manifest)
        require(status['public_release_ready'], 'Public release is blocked: ' + ', '.join(status['blocked']))
        require(manifest['release']['public_release_ready'], 'Rebuild after recording release evidence')
    require(not destination.is_symlink() and not destination.is_relative_to(output), 'ZIP destination must be outside build folder')
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Public-style binary ZIP contains no local paths, caches, or NAM source tree.
    members = {item['path']: (output / item['path']).read_bytes() for item in manifest['files']}
    members['manifest.json'] = (output / 'manifest.json').read_bytes()
    members.update({item['path']: (output / item['path']).read_bytes() for item in manifest.get('documentation', [])})
    packaged = deepcopy(manifest)
    if refresh_docs:
        # Capture final artwork and views without rebuilding DATs or changing
        # the original manifest against which connector extraction ran.
        from .export import documentation_members, compiled_manifest_sha256
        members = {name: raw for name, raw in members.items() if not name.startswith('docs/')}
        current_docs = documentation_members(project_root)
        members.update(current_docs)
        packaged['documentation'] = [item for item in manifest.get('documentation', []) if item['path'] == 'README.txt']
        packaged['documentation'] += [{'path': name, 'sha256': sha(raw), 'bytes': len(raw)}
                                     for name, raw in sorted(current_docs.items())]
        require(compiled_manifest_sha256(packaged) == compiled_manifest_sha256(manifest),
                'Documentation handoff changed compiled build facts')
        members['manifest.json'] = (json.dumps(packaged, sort_keys=True, indent=2) + '\n').encode()
    if release:
        # Published documentation reflects recorded game evidence. The DATs
        # remain byte-identical to the verified, evidence-bound candidate.
        published = deepcopy(packaged)
        published['release'] = status
        published['in_game_tested'] = True
        domains = {piece.get('domain', 'high-speed-rail') for piece in manifest['pieces']}
        folders = manifest.get(transport_menu.KEY, {}).get('domains', ())
        menu_paths = [f'Transportation > {category}' + (' > SCP > Pieces' if domain in folders else '')
                      for domain, category in (('high-speed-rail', 'Rail'), ('highway', 'Highways'))
                      if domain in domains]
        raw = ("Simon's Custom Pieces\n" + manifest['version'] + "\n"
               "Requires the exact supported NAM profile in manifest.json.\n"
               + '\n'.join(f'Standalone SCP buttons appear under {path}.' for path in menu_paths) + '\n'
               "Install the coordinated plugin as a unit; never stack standalone prototype overlays.\n"
               "Back up cities and retain a complete previous plugin before upgrading.\n").encode('utf8')
        members['README.txt'] = raw
        published['documentation'] = [{'path': 'README.txt', 'sha256': sha(raw), 'bytes': len(raw)}] + [
            item for item in packaged.get('documentation', []) if item['path'] != 'README.txt']
        members['manifest.json'] = (json.dumps(published, sort_keys=True, indent=2) + '\n').encode()
    with tempfile.NamedTemporaryFile(prefix='.scp-package-', dir=destination.parent, delete=False) as stream:
        temporary = Path(stream.name)
    try:
        with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name, raw in sorted(members.items()):
                info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED; info.external_attr = 0o100644 << 16
                archive.writestr(info, raw)
        with zipfile.ZipFile(temporary) as archive:
            require(archive.testzip() is None, 'ZIP integrity failure')
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)
    return {'output': str(destination), 'sha256': sha(destination.read_bytes()), 'public_release': release,
            'documentation_refreshed': refresh_docs, 'compiled_payloads_changed': False}
