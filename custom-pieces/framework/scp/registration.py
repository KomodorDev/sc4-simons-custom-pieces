"""Register new domain pieces and collections without editing global routing."""
from copy import deepcopy
import json
from pathlib import Path
from .catalog import load_catalog, safe_relative, validate_catalog
from .dbpf import require


def apply_registration(root, additions, ledger, collections, icons=None, *, domain):
    """Validate the proposed catalogue before writing any reserved identity."""
    root = Path(root).resolve()
    current = load_catalog(root)
    candidate = deepcopy(current)
    candidate['pieces'].extend(additions)
    candidate['_allocations'] = ledger
    candidate['piece_sets'].update(collections)
    validate_catalog(candidate)
    route = current['domains'][domain]
    directory = safe_relative(root, route['path'])
    registry_file = safe_relative(root, route['registry'])
    registry = json.loads(registry_file.read_text())
    collection_file = safe_relative(directory, registry['collections'])
    selections = json.loads(collection_file.read_text())
    pending = {}
    for piece in additions:
        require(piece['domain'] == domain, 'New piece is assigned to the wrong domain')
        target = safe_relative(directory, f'00_pieces/{piece["id"]}/piece.json')
        require(not target.exists(), 'An unregistered piece manifest already exists')
        record = {'purpose': 'Authoritative build definition and permanent game-resource identity for '+piece['name']+'.', **piece}
        pending[target] = (json.dumps(record, indent=2)+'\n').encode()
        overview = target.parent/'README.md'
        for name in ('README.md', 'TESTING.md'):
            document = safe_relative(root, (target.parent/name).relative_to(root).as_posix())
            require(not document.is_symlink(), 'Registration document cannot be a symbolic link')
        if not overview.exists():
            from .content import piece_document_scaffold
            for name, text in piece_document_scaffold(piece).items():
                document = target.parent/name
                if not document.exists():
                    pending[document] = text.encode()
        registry['pieces'].append(target.relative_to(directory).as_posix())
    selections['collections'].update(collections)
    pending[root / current['allocations']] = (json.dumps(ledger, indent=2)+'\n').encode()
    pending[registry_file] = (json.dumps(registry, indent=2)+'\n').encode()
    pending[collection_file] = (json.dumps(selections, indent=2)+'\n').encode()
    for identifier, raw in (icons or {}).items():
        require(identifier in {p['id'] for p in candidate['pieces'] if p['domain'] == domain},
                'Icon does not identify a piece in this domain')
        pending[directory/'00_pieces'/identifier/'icon.png'] = raw
    require(all(isinstance(raw, bytes) for raw in pending.values()),
            'Registration outputs must be fully serialized bytes before writing')
    for path in pending:
        checked = safe_relative(root, path.relative_to(root).as_posix())
        require(checked == path and not path.is_symlink(),
                'Registration paths must not redirect through symbolic links')
        require(not path.with_name(path.name+'.tmp').is_symlink(),
                'Registration temporary file cannot be a symbolic link')
    for path, raw in pending.items():
        if path.is_file() and path.read_bytes() == raw:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(path.name+'.tmp')
        require(not temporary.is_symlink(), 'Registration temporary file cannot be a symbolic link')
        temporary.write_bytes(raw)
        temporary.replace(path)
    load_catalog(root)
