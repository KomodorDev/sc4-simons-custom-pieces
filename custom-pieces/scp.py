#!/usr/bin/env python3
"""One entry point for Simon's Custom Pieces; no implicit installation."""
import argparse
import json
import os
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/high-speed-rail/implementation')]
sys.dont_write_bytecode = True
if sys.version_info < (3, 11):
    raise SystemExit('SCP requires Python 3.11 or newer. Check with: python3 --version')
from scp.catalog import load_catalog, select_pieces, inspect_pieces, release_status, number, piece_cells, tile_base
from scp.build import build_project, doctor, verify_build, package_build
from scp.dbpf import require


def configured_plugins():
    local = ROOT / 'local/settings.json'
    settings = json.loads(local.read_text()) if local.exists() else {}
    value = os.environ.get('SCP_PLUGINS') or settings.get('plugins')
    if value:
        return Path(value).expanduser()
    for path in (Path.home() / 'Documents/SimCity 4 Windows/Plugins', Path.home() / 'Documents/SimCity 4/Plugins'):
        if path.is_dir():
            return path
    raise ValueError('No Plugins folder found. Pass --plugins with its full path.')


def selection(args, catalog):
    if getattr(args, 'piece_sets', None):
        sets = catalog.get('piece_sets', {})
        require(all(name in sets for name in args.piece_sets), 'Unknown piece set; use list to see the available sets')
        return list(dict.fromkeys(slug for name in args.piece_sets for slug in sets[name]))
    return [p['id'] for p in catalog['pieces'] if p['status'] != 'draft'] if getattr(args, 'all', False) else getattr(args, 'include', None)


def scaffold(slug, name, width=1, depth=1, domain='high-speed-rail'):
    import re
    require(re.fullmatch('[a-z][a-z0-9-]{1,63}', slug) is not None, 'Use a lowercase id such as hsr-new-crossing')
    require(isinstance(name, str) and name.strip(), 'A nonempty piece name is required')
    name = name.strip()
    catalog = load_catalog(ROOT)
    domains = catalog.get('domains', {})
    require(domain in domains, 'Unknown transport domain; register it with agent and human guides in project.json first')
    require(type(width) is int and type(depth) is int and 1 <= width <= 16 and 1 <= depth <= 16
            and width * depth <= 16, 'Footprint must have 1–16 cells and width/depth 1–16')
    ledger_path = ROOT / 'config/allocations.json'
    ledger = json.loads(ledger_path.read_text())
    require(slug not in ledger['pieces'], 'This id is already allocated to a current piece. Choose a different id.')
    used_puzzles = {number(p['puzzle_id']) for p in ledger['pieces'].values()}
    puzzle = next((n for n in range(0xF7A0, 0xF900) if n not in used_puzzles), None)
    require(puzzle is not None, 'Local puzzle namespace exhausted; allocate another reviewed namespace')
    used_blocks = {number(iid) & 0xfffff000 for p in ledger['pieces'].values()
                   for iid in [p['preview_id'], *p['tile_ids'], *p.get('resource_blocks', [])]}
    # New drafts receive a whole 0x1000 family. Native two-dimensional
    # AutoTileBase indexing advances 0x100 across and 0x10 down the footprint.
    block = next((n for n in range(0x7F500000, 0x7F600000, 0x1000) if n not in used_blocks), None)
    require(block is not None, 'Local model namespace exhausted')
    # Start from a clean draft. Copying an arbitrary existing recipe would
    # inherit sparse cells or direction policies when the catalog is reordered.
    piece = {'purpose': 'Draft reusable piece definition; implement and independently verify before building.', 'schema_version': 1, 'orientation_count': 8,
             'game_tests': dict(catalog['pieces'][0]['game_tests'])}
    piece.update({'id': slug, 'name': name, 'description': 'Describe the upper/lower networks, geometry and limitations.',
                  'recipe': slug.replace('-', '_'), 'status': 'draft', 'enabled_by_default': False,
                  'puzzle_id': f'{puzzle:04x}', 'tile_ids': [f'{block + x * 256 + y * 16:08x}' for y in range(depth) for x in range(width)], 'preview_id': f'{block + 0xff5:08x}',
                  'effect_name': f'preview_scp_{puzzle:04x}'.ljust(24, '_') + '001',
                  'footprint': [width, depth], 'dependencies': catalog['_domain_records'][domain].get('scaffold', {}).get('dependencies', ['controller']),
                  'menu': {'id': f'{0x6A470000 | puzzle:08x}', 'order': f'{0x70110000 | puzzle:08x}', 'style': catalog['_domain_records'][domain].get('scaffold', {}).get('menu_style', 'draft')},
                  'shadow_mappings': [], 'provenance': {'geometry': 'To be recorded', 'construction': 'To be recorded',
                                                      'redistribution': 'permission-pending'},
                  'game_tests': {key: 'unverified' for key in piece['game_tests']}})
    piece['domain'] = domain
    relative = Path(domains[domain]['path']) / '00_pieces' / slug / 'piece.json'
    target = ROOT / relative
    require(not target.exists(), 'Piece manifest already exists')
    allocation = {key: piece[key] for key in ('puzzle_id', 'tile_ids', 'preview_id')}
    allocation.update({'menu_id': piece['menu']['id'], 'state': 'reserved-locally',
                       'cells': piece_cells(piece), 'tile_base': f'{tile_base(piece):08x}',
                       'resource_blocks': [f'{block:08x}']})
    ledger['pieces'][slug] = allocation
    from scp.registration import apply_registration
    apply_registration(ROOT, [piece], ledger, {}, domain=domain)
    return {'manifest': str(target), 'status': 'draft', 'next': 'Implement recipe and independent verifier, then mark experimental. Identifiers are recorded in config/allocations.json.'}


def source_package(destination):
    destination = Path(destination).absolute()
    from scp.export import public_files, portable_bytes
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative, path in public_files(ROOT):
            info = zipfile.ZipInfo((Path('custom-pieces') / relative).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100755 if path.suffix == '.command' else 0o100644) << 16
            archive.writestr(info, portable_bytes(ROOT, path))
    with zipfile.ZipFile(destination) as archive:
        require(archive.testzip() is None, 'Source ZIP integrity failure')
        require(not any(name.lower().endswith(('.dat', '.sc4model', '.sc4lot')) for name in archive.namelist()), 'Source package contains binary NAM assets')
    return {'output': str(destination), 'contains_NAM_binary_assets': False, 'published': False,
            'note': 'Development source export; not a declaration that publication permissions are cleared.'}


def main():
    require(__debug__, 'Run without Python -O; development assertions must remain enabled')
    parser = argparse.ArgumentParser(description="Simon's Custom Pieces — build, verify, package, and manage a coordinated plugin.")
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('list', 'doctor', 'build', 'verify', 'package', 'release-check', 'source-package', 'install', 'uninstall', 'rollback', 'scaffold', 'check', 'inventory'):
        cmd = sub.add_parser(name)
        if name in {'doctor', 'build', 'install', 'uninstall', 'rollback'}:
            cmd.add_argument('--plugins', type=Path)
            cmd.add_argument('--extra-plugins', action='append', type=Path, default=None)
        if name in {'doctor', 'build', 'release-check'}:
            group = cmd.add_mutually_exclusive_group()
            group.add_argument('--all', action='store_true')
            group.add_argument('--include', action='append', help='Exact piece id; repeat for multiple pieces')
            group.add_argument('--set', dest='piece_sets', action='append', help='Named piece set from list; repeat to combine sets')
        if name in {'build', 'verify', 'package', 'install', 'release-check'}:
            cmd.add_argument('--output', type=Path, default=ROOT / 'dist/development')
        if name == 'build':
            cmd.add_argument('--progress', action='store_true', help='Show build progress on standard error; keep JSON on standard output')
        if name == 'package':
            cmd.add_argument('--destination', type=Path, default=ROOT / 'dist/Simons-Custom-Pieces-development.zip')
            cmd.add_argument('--release', action='store_true')
            cmd.add_argument('--refresh-docs', action='store_true', help='Package current portable guides, images, and records without rebuilding compiled payloads')
        if name == 'source-package':
            cmd.add_argument('--destination', type=Path, default=ROOT / 'dist/Simons-Custom-Pieces-source.zip')
        if name in {'install', 'uninstall', 'rollback'}:
            cmd.add_argument('--backup-root', type=Path, required=True)
        if name == 'rollback':
            cmd.add_argument('--backup-id', required=True)
        if name == 'check':
            cmd.add_argument('--scope', default='all', help='all, framework, domain ID or assembly ID')
            cmd.add_argument('--verbose', action='store_true', help='Show each individual check as it starts')
        if name == 'scaffold':
            cmd.add_argument('--id', required=True); cmd.add_argument('--name', required=True)
            cmd.add_argument('--width', type=int, default=1); cmd.add_argument('--depth', type=int, default=1)
            cmd.add_argument('--domain', default='high-speed-rail', help='Transport domain registered in project.json')
    connector_cmd = sub.add_parser('connectors', help='Refresh or check source-owned connection data and overviews')
    connector_cmd.add_argument('action', choices=('refresh', 'check'))
    connector_cmd.add_argument('--piece', action='append', required=True, dest='connector_pieces', help='Exact registered piece ID; repeat for multiple pieces')
    connector_cmd.add_argument('--domain', default='high-speed-rail')
    connector_cmd.add_argument('--build', type=Path, default=Path('dist/current'), help='Existing compiled build, relative to custom-pieces unless absolute')
    connector_cmd.add_argument('--plugins', type=Path, help='Texture source for rendering or overview freshness checks; never installs anything')
    connector_cmd.add_argument('--no-render', action='store_true', help='Refresh/check consumer data without artwork or README generation')
    observations_cmd = sub.add_parser('observations', help='Maintain observation records without extracting resources or computing compatibility')
    observations_cmd.add_argument('action', choices=('retire-connections', 'refresh-images'))
    observations_cmd.add_argument('--piece', action='append', dest='observation_pieces', help='Exact registered piece ID; repeat to select more')
    observations_cmd.add_argument('--assembly', action='append', dest='observation_assemblies', help='Exact registered assembly ID; repeat to select more')
    observations_cmd.add_argument('--all', action='store_true', help='Apply this observation maintenance operation to every registered subject')
    icons_cmd = sub.add_parser('assembly-icons', help='Refresh canonical assembly icons without building or installing game resources')
    icons_cmd.add_argument('--domain', default='high-speed-rail', help='Transport domain registered in project.json')
    for command in ('assembly-menu', 'menu-test'):
        menu_cmd = sub.add_parser(command, help=('Prepare one assembly button with Tab/Shift+Tab component cycling'
            if command == 'assembly-menu' else 'Compatibility command for assembly menu preparation'))
        menu_cmd.add_argument('--source', type=Path, default=ROOT / 'dist/current', help='Existing normal verified build; all selected piece assets are preserved')
        menu_cmd.add_argument('--output', type=Path, default=ROOT / ('dist/trumpet-assembly-menu' if command == 'assembly-menu' else 'dist/trumpet-menu-test'))
        menu_cmd.add_argument('--layout', default='trumpet', help='Exact entry in the owning domain menu-layout.json')
        menu_cmd.add_argument('--domain', default='high-speed-rail')
        menu_cmd.add_argument('--plugins', type=Path)
        menu_cmd.add_argument('--extra-plugins', action='append', type=Path, default=None)
    args = parser.parse_args()
    if args.command == 'assembly-icons':
        from scp.menu_experiment import write_assembly_icons
        result = write_assembly_icons(ROOT, domain_id=args.domain)
        print(json.dumps(result, indent=2))
        return 0
    if args.command in ('assembly-menu', 'menu-test'):
        from scp.menu_experiment import build_assembly_menu, build_menu_experiment
        operation = build_assembly_menu if args.command == 'assembly-menu' else build_menu_experiment
        result = operation(ROOT, args.source, args.output, layout_id=args.layout,
            domain_id=args.domain, plugins=args.plugins or configured_plugins(), extra_roots=args.extra_plugins)
        print(json.dumps(result, indent=2))
        return 0
    if args.command == 'observations':
        from scp.content import retire_connection_cases_in_catalog, refresh_image_reviews_in_catalog
        operation = (refresh_image_reviews_in_catalog if args.action == 'refresh-images'
                     else retire_connection_cases_in_catalog)
        result = operation(ROOT, piece_ids=args.observation_pieces,
            assembly_ids=args.observation_assemblies, all_subjects=args.all)
        print(json.dumps(result, indent=2))
        return 0
    if args.command == 'connectors':
        from scp.connector_metadata import refresh_connections, check_connections
        build = args.build if args.build.is_absolute() else ROOT / args.build
        options = {'domain_id': args.domain, 'render': not args.no_render}
        if args.action == 'refresh':
            result = refresh_connections(ROOT, args.connector_pieces, build, plugins=args.plugins, **options)
        else:
            result = check_connections(ROOT, args.connector_pieces, build, plugins=args.plugins, **options)
        print(json.dumps(result, indent=2))
        return 0
    if args.command == 'uninstall':
        from scp.install import uninstall
        local = json.loads((ROOT / 'local/settings.json').read_text()) if (ROOT / 'local/settings.json').exists() else {}
        result = uninstall(args.plugins or configured_plugins(), args.backup_root,
                           extra_roots=args.extra_plugins if args.extra_plugins is not None else local.get('extra_plugins', []))
        print(json.dumps(result, indent=2))
        return 0
    catalog = load_catalog(ROOT)
    if args.command == 'list':
        result = {'name': catalog['name'], 'version': catalog['version'],
                  'domains': catalog.get('domains', {}), 'piece_sets': catalog.get('piece_sets', {}), 'pieces': [
            {k: p[k] for k in ('id', 'name', 'status', 'enabled_by_default', 'puzzle_id', 'menu',
                               'domain', 'category', 'footprint') if k in p} for p in catalog['pieces']]}
    elif args.command == 'check':
        from scp.checks import run_checks
        result = run_checks(ROOT, args.scope, args.verbose)
        print(json.dumps(result, indent=2))
        return 0 if result['all_passed'] else 1
    elif args.command == 'inventory':
        from scp.inventory import write_inventories
        result = write_inventories(ROOT)
    elif args.command == 'doctor':
        result = doctor(ROOT, args.plugins or configured_plugins(), selection(args, catalog), args.extra_plugins)
    elif args.command == 'build':
        def progress(update):
            if update['phase'] == 'compile':
                message = f"[{update['index']}/{update['pieces']}] {update['piece']}"
            else:
                message = f"{update['phase'].title()}: {update['pieces']} pieces"
            print(message, file=sys.stderr, flush=True)
        result = build_project(ROOT, args.plugins or configured_plugins(), args.output, selection(args, catalog),
                               args.extra_plugins, progress=progress if args.progress else None)
    elif args.command == 'verify':
        result = verify_build(args.output)
    elif args.command == 'package':
        result = package_build(args.output, args.destination, args.release, ROOT, refresh_docs=args.refresh_docs)
    elif args.command == 'release-check':
        inspected = inspect_pieces(catalog, selection(args, catalog))
        result = release_status(ROOT, inspected)
        if (args.output / 'manifest.json').is_file():
            from scp.release import assess_build
            verify_build(args.output)
            manifest = json.loads((args.output / 'manifest.json').read_text())
            requested = {p['id'] for p in inspected}
            if requested == {p['id'] for p in manifest['pieces']}:
                result = assess_build(ROOT, manifest)
            else:
                result['public_release_ready'] = False
                result['blocked'].append('Build the selected piece set first, then assess its exact output')
    elif args.command == 'source-package':
        result = source_package(args.destination)
    elif args.command == 'scaffold':
        result = scaffold(args.id, args.name, args.width, args.depth, args.domain)
    elif args.command == 'install':
        from scp.install import install_build
        local = json.loads((ROOT / 'local/settings.json').read_text()) if (ROOT / 'local/settings.json').exists() else {}
        result = install_build(args.output, args.plugins or configured_plugins(), args.backup_root,
                               extra_roots=args.extra_plugins if args.extra_plugins is not None else local.get('extra_plugins', []))
    else:
        from scp.install import rollback_install
        local = json.loads((ROOT / 'local/settings.json').read_text()) if (ROOT / 'local/settings.json').exists() else {}
        result = rollback_install(args.plugins or configured_plugins(), args.backup_root, args.backup_id,
                                  extra_roots=args.extra_plugins if args.extra_plugins is not None else local.get('extra_plugins', []))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, ImportError) as error:
        print(f'SCP: {error}', file=sys.stderr)
        raise SystemExit(1)
