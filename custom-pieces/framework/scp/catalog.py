"""Current piece registry and identifier collision checks."""
from copy import deepcopy
import json
from pathlib import Path
import re

from .dbpf import require
from .autotile import AutoTileAddressError, validate_auto_tile_addresses


def safe_relative(root, name):
    require(isinstance(name, str) and name and '\\' not in name and not Path(name).is_absolute(), 'Expected relative project path')
    require('..' not in Path(name).parts, 'Parent traversal is not allowed')
    target = (Path(root) / name).resolve()
    require(target.is_relative_to(Path(root).resolve()), 'Project path escapes framework')
    return target


def number(value):
    require(isinstance(value, str) and re.fullmatch('[0-9a-fA-F]{1,8}', value) is not None,
            f'Expected hexadecimal identifier, got {value!r}')
    return int(value, 16)


def piece_cells(piece):
    """Occupied cells may leave the top-left construction anchor empty."""
    width, depth = piece['footprint']
    return piece.get('cells', [[x, y] for y in range(depth) for x in range(width)])


def tile_base(piece):
    x, y = piece_cells(piece)[0]
    return number(piece['tile_ids'][0]) - x * 0x100 - y * 0x10


def auto_tile_base(piece):
    """The engine starts offsets at the modeled cells' bounding-box origin.

    Reserved empty borders still contribute to stored model coordinates, but
    do not contribute to the engine's automatically generated tile offsets.
    """
    cells = piece_cells(piece)
    return tile_base(piece) + min(x for x, _ in cells) * 0x100 + min(y for _, y in cells) * 0x10


def load_catalog(root):
    root = Path(root).resolve()
    project = json.loads((root / 'project.json').read_text())
    domains = project.get('domains', {})
    require(isinstance(domains, dict) and domains, 'Domains must be a nonempty JSON object')
    paths, collections, assemblies, records = [], {}, [], {}
    for slug, domain in domains.items():
        require(re.fullmatch('[a-z][a-z0-9-]{1,63}', slug) is not None
                and isinstance(domain, dict) and domain.get('name'), 'Invalid transport domain')
        directory = safe_relative(root, domain.get('path'))
        require(directory.is_dir(), f'{slug}: domain folder does not exist')
        require(all((directory / name).is_file() for name in ('AGENTS.md', 'README.md')),
                f'{slug}: domain requires agent and human guides')
        registry_path = safe_relative(root, domain.get('registry'))
        require(registry_path == directory / 'domain.json', f'{slug}: registry must be domain.json')
        registry = json.loads(registry_path.read_text())
        require(registry.get('schema_version') == 1 and registry.get('id') == slug,
                f'{slug}: invalid domain registry')
        records[slug] = registry
        listed = registry.get('pieces', [])
        require(isinstance(listed, list) and len(listed) == len(set(listed)),
                f'{slug}: duplicate piece manifest path')
        for relative in listed:
            file = safe_relative(directory, relative)
            piece = json.loads(file.read_text())
            require(isinstance(piece, dict), 'Piece must be a JSON object')
            require(piece.get('domain') == slug, f'{piece.get("id")}: unknown transport domain')
            require(file == directory / '00_pieces' / piece['id'] / 'piece.json',
                    f'{piece.get("id")}: manifest must be 00_pieces/<id>/piece.json in its domain')
            paths.append((file, piece))
        collection_path = safe_relative(directory, registry['collections'])
        selection = json.loads(collection_path.read_text())
        require(selection.get('schema_version') == 1, f'{slug}: unsupported collection schema')
        for name, members in selection.get('collections', {}).items():
            require(name not in collections, f'Duplicate collection: {name}')
            collections[name] = members
        for relative in registry.get('assemblies', []):
            file = safe_relative(directory, relative)
            require(file.name == 'assembly.json' and file.parent.parent == directory / '01_assemblies',
                    f'{slug}: assembly must be 01_assemblies/<id>/assembly.json')
            scene = json.loads(file.read_text())
            assemblies.append({'id': file.parent.name, 'domain': slug,
                               'path': file.parent.relative_to(root).as_posix(), 'scene': scene})
    require(len(paths) == len({p for p, _ in paths}), 'Duplicate piece manifest path')
    project['pieces'] = [piece for _, piece in paths]
    project['piece_sets'] = collections
    project['_domain_records'] = records
    project['_assemblies'] = assemblies
    project['_profile'] = json.loads(safe_relative(root, project['profile']).read_text())
    project['_root'] = root
    if project.get('allocations'):
        project['_allocations'] = json.loads(safe_relative(root, project['allocations']).read_text())
    validate_catalog(project)
    return project


def validate_catalog(catalog):
    require(catalog.get('schema_version') == 1, 'Unsupported project schema')
    require(catalog.get('plugin_folder') == 'zzz_Simons_Custom_Pieces', 'Unexpected managed folder name')
    require(isinstance(catalog.get('pieces'), list) and catalog['pieces'], 'Project has no pieces')
    require(catalog.get('_profile', {}).get('schema_version') == 1, 'Unsupported compatibility profile schema')
    ids, names, puzzles, resources, effects, menus = set(), set(), set(), {}, set(), set()
    if '_allocations' in catalog:
        ledger = catalog['_allocations']
        require(ledger.get('schema_version') == 1, 'Unsupported allocation ledger schema')
        reserved, reserved_puzzles, reserved_menus = set(), set(), set()
        reserved_blocks, allocated_resources = {}, []
        for slug, allocation in ledger['pieces'].items():
            puzzle, menu = number(allocation['puzzle_id']), number(allocation['menu_id'])
            require(puzzle not in reserved_puzzles and menu not in reserved_menus, 'Identifier reservation collision')
            reserved_puzzles.add(puzzle); reserved_menus.add(menu)
            blocks = list(map(number, allocation.get('resource_blocks', [])))
            require(len(blocks) == len(set(blocks)) and all(value & 0xfff == 0 for value in blocks),
                    'Invalid whole-family resource reservation')
            if blocks:
                require(blocks == list(range(blocks[0], blocks[-1]+0x1000, 0x1000)),
                        'Multi-family resource reservations must be contiguous')
            for block in blocks:
                require(block not in reserved_blocks, 'Whole-family resource reservation collision')
                reserved_blocks[block] = slug
            for iid in [number(allocation['preview_id'])] + [number(base) + zoom for base in allocation['tile_ids'] for zoom in range(5)]:
                require(iid not in reserved, 'Resource reservation overlap')
                reserved.add(iid)
                allocated_resources.append((iid, slug))
                require(not blocks or iid & 0xfffff000 in blocks,
                        'Resource lies outside its reserved families')
        require(all(reserved_blocks.get(iid & 0xfffff000, slug) == slug for iid, slug in allocated_resources),
                'Resource occupies another piece\'s reserved family')
        require(set(ledger['pieces']) == {piece['id'] for piece in catalog['pieces']},
                'Allocation ledger must match current piece IDs exactly')
    game_keys = {'placement', 'traffic_both_directions', 'no_unwanted_transfers',
                 'rotations_and_mirrors', 'shadows', 'demolition', 'save_reload'}
    for piece in catalog['pieces']:
        require(isinstance(piece, dict), 'Piece must be a JSON object')
        require(piece.get('schema_version') == 1, 'Unsupported piece schema')
        slug = piece.get('id', '')
        require(re.fullmatch('[a-z][a-z0-9-]{1,63}', slug) is not None, 'Invalid piece id')
        require(slug not in ids, f'Duplicate piece id: {slug}'); ids.add(slug)
        require(isinstance(piece.get('enabled_by_default'), bool), f'{slug}: missing enabled_by_default')
        require(piece.get('status') in {'draft', 'experimental', 'tested'}, f'{slug}: invalid status')
        require(re.fullmatch('[a-z][a-z0-9_]+', piece.get('recipe', '')) is not None, 'Invalid recipe name')
        require(piece.get('name') and piece.get('description'), f'{slug}: name and description required')
        require(piece['name'].casefold() not in names, 'Duplicate display name')
        names.add(piece['name'].casefold())
        from .design_review import validate_review
        validate_review(piece)
        puzzle = number(piece['puzzle_id'])
        require(0 < puzzle <= 0xffff and puzzle not in puzzles, f'Duplicate/invalid puzzle id: {slug}')
        puzzles.add(puzzle)
        require(piece.get('orientation_count') == 8, 'Current framework supports eight orientations')
        footprint = piece.get('footprint')
        require(isinstance(footprint, list) and len(footprint) == 2 and
                all(type(n) is int for n in footprint) and
                1 <= footprint[0] <= 64 and 1 <= footprint[1] <= 16, 'Invalid footprint')
        tiles = piece.get('tile_ids', [])
        cells = piece_cells(piece)
        require(isinstance(cells, list) and cells and all(
            isinstance(cell, list) and len(cell) == 2 and
            all(type(n) is int for n in cell) and
            0 <= cell[0] < footprint[0] and 0 <= cell[1] < footprint[1] for cell in cells),
            f'{slug}: invalid occupied cells')
        require(len({tuple(cell) for cell in cells}) == len(cells),
                f'{slug}: occupied cells must be unique')
        require(len(tiles) == len(cells), f'{slug}: tile count does not match footprint cells')
        base = tile_base(piece)
        require(0 <= base <= 0xffffffff and all(number(tile) == base + x * 0x100 + y * 0x10
                    for tile, (x, y) in zip(tiles, cells)), f'{slug}: tile IDs do not match AutoTileBase cell offsets')
        try:
            validate_auto_tile_addresses(piece)
        except AutoTileAddressError:
            # Keep a known failed prototype inspectable in the registry. It
            # cannot be selected for building; do not hide this failure with
            # a special case for a particular piece ID or base address.
            if piece.get('game_tests', {}).get('placement') != 'failed':
                raise
        allocated = []
        for tile in tiles:
            tile_iid = number(tile)
            require(tile_iid & 0xf == 0, 'Tile base must end in hexadecimal 0')
            allocated += list(range(tile_iid, tile_iid + 5))
        allocated.append(number(piece['preview_id']))
        for iid in allocated:
            require(iid not in resources, f'Resource identifier overlap: {iid:08x} ({slug})')
            resources[iid] = slug
        effect = piece.get('effect_name', '')
        require(re.fullmatch('[a-z0-9_]+', effect) is not None and effect not in effects,
                'Invalid or duplicate preview effect name'); effects.add(effect)
        menu = piece.get('menu', {})
        iid = number(menu['id'])
        require(iid not in menus and iid & 0xffff == puzzle, 'Menu id must be unique and target puzzle low16')
        menus.add(iid); number(menu['order'])
        require(menu.get('style'), 'Missing icon style')
        require(set(piece.get('game_tests', {})) == game_keys, f'{slug}: incomplete game test matrix')
        require(all(v in {'unverified', 'passed', 'failed'} for v in piece['game_tests'].values()), 'Invalid game test status')
        require(isinstance(piece.get('dependencies'), list) and 'controller' in piece['dependencies'], 'Missing dependencies')
        for shadow in piece.get('shadow_mappings', []):
            require(shadow.get('tile') in tiles and shadow.get('rotation') in range(4), 'Invalid shadow mapping')
            number(shadow['source'])
        require(piece.get('provenance', {}).get('redistribution'), 'Missing provenance/permission status')
        if '_allocations' in catalog:
            allocation = catalog['_allocations']['pieces'].get(slug)
            require(allocation is not None, f'{slug}: missing permanent identifier reservation')
            require(all(allocation.get(k) == piece[k] for k in ('puzzle_id', 'tile_ids', 'preview_id'))
                    and allocation.get('menu_id') == piece['menu']['id'],
                    f'{slug}: saved-city identifiers changed; create a new piece instead')
            if 'cells' in allocation or 'tile_base' in allocation:
                require(allocation.get('cells') == cells and number(allocation['tile_base']) == base,
                        f'{slug}: saved-city construction coordinates changed')
    sets = catalog.get('piece_sets', {})
    require(isinstance(sets, dict), 'Piece sets must be a JSON object')
    for name, members in sets.items():
        require(re.fullmatch('[a-z][a-z0-9-]{1,63}', name) is not None,
                'Invalid piece-set name')
        require(isinstance(members, list) and members and all(isinstance(x, str) for x in members)
                and len(members) == len(set(members)) and set(members) <= ids,
                f'{name}: piece set has duplicate, missing or unknown members')


def inspect_pieces(catalog, include=None):
    """Select records for read-only reporting, including known failed pieces.

    Identifier validation and selection order are shared with building. A
    release-status report must still be able to explain why an unsafe or
    failed prototype cannot be built; build eligibility is checked separately.
    """
    known = {piece['id']: piece for piece in catalog['pieces']}
    if include is None:
        selected = [p for p in catalog['pieces'] if p['enabled_by_default']]
    else:
        require(len(include) == len(set(include)), 'Duplicate piece selection')
        require(set(include) <= set(known), f'Unknown pieces: {sorted(set(include) - set(known))}')
        selected = [known[slug] for slug in include]
    return deepcopy(selected)


def select_pieces(catalog, include=None):
    """Select build-eligible pieces; reporting never bypasses this guard."""
    selected = inspect_pieces(catalog, include)
    require(all(p['status'] != 'draft' for p in selected), 'Draft pieces need implementation and verification first')
    failures = [p['id'] for p in selected if p['game_tests']['placement'] == 'failed']
    require(not failures, f'Pieces with failed placement tests cannot be built: {", ".join(failures)}')
    for piece in selected:
        validate_auto_tile_addresses(piece)
    return selected


def release_status(root, pieces):
    gates = json.loads((Path(root) / 'config/release.json').read_text())
    blocked = []
    current_reviews = {}
    if (Path(root) / 'project.json').is_file():
        try:
            current_reviews = {piece['id']:piece.get('design_review')
                               for piece in load_catalog(root)['pieces']}
        except (OSError, ValueError, KeyError, TypeError):
            blocked.append('current design-review registry is missing or invalid')
    for name in ('public_name_checked', 'ids_allocated', 'nam_derivatives_permission',
                 'supported_platform_tests', 'simtropolis_description_and_game_images'):
        item = gates.get(name, {})
        if item.get('status') != 'passed' or not item.get('evidence'):
            blocked.append(name)
    for piece in pieces:
        review = current_reviews.get(piece['id']) or piece.get('design_review')
        if review:
            from .design_review import review_note
            blocked.append(f"{piece['id']}: {review_note({'design_review':review})}")
        if piece['status'] != 'tested' or any(v != 'passed' for v in piece['game_tests'].values()):
            blocked.append(f"{piece['id']}: in-game test matrix")
        if piece.get('provenance', {}).get('redistribution') != 'permission-recorded':
            blocked.append(f"{piece['id']}: redistribution evidence")
    return {'public_release_ready': not blocked, 'blocked': blocked,
            'note': 'Static checks do not constitute game testing or redistribution permission.'}
