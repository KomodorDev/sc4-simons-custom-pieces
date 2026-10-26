"""Read-only Yunika lot/prop/model dependency audit; writes scratch JSON only."""
from pathlib import Path
import collections
import json
import re
import struct
import sys

project = Path('/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City')
sys.path.insert(0, str(project / 'setup/cam-install/runtime-audit'))
import read_dbpf as dbpf

records = project / 'setup/tokyo-hub-install/records'
plugins = Path('/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins')
game = Path('/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/SharedSupport/prefix/drive_c/GOG Games/SimCity 4 Deluxe Edition')
target = plugins / '300-commercial/PC Yunika Building Shinjuku'
index = {}
instances = collections.defaultdict(list)
files_scanned = 0
for path in [*game.glob('*.dat'), *(game / 'Plugins').rglob('*'), *plugins.rglob('*')]:
    if not path.is_file() or path.suffix.lower() not in ('.dat', '.sc4lot', '.sc4desc', '.sc4model'):
        continue
    with path.open('rb') as stream:
        header = stream.read(96)
        if header[:4] != b'DBPF':
            continue
        count, offset, size = struct.unpack_from('<3I', header, 36)
        assert not count or size // count == 20, str(path)
        stream.seek(offset)
        for kind, group, instance, offset, length in struct.iter_unpack('<5I', stream.read(size)):
            tgi = kind, group, instance
            index[tgi] = str(path), offset, length
            if kind == 0x6534284a:
                instances[instance].append(tgi)
    files_scanned += 1

def read(tgi):
    path, offset, length = index[tgi]
    with open(path, 'rb') as stream:
        stream.seek(offset)
        return dbpf.decompress(stream.read(length))

def properties(tgi):
    data = read(tgi)
    if data[:4] in (b'EQZB', b'CQZB'):
        return {int(p['id'], 16): p['values'] for p in dbpf.exemplar(data)['properties']}
    result = {}
    for line in data.decode('utf-8', errors='replace').splitlines():
        match = re.match(r'(0x[\da-fA-F]+):\{"[^"]*"\}=([^:]+):[^:]+:\{(.*)\}', line)
        if not match:
            continue
        pid, kind, body = match.groups()
        if kind == 'String':
            result[int(pid, 16)] = body.strip('"')
        elif kind.startswith(('Uint', 'Sint')):
            result[int(pid, 16)] = [int(v.strip(), 0) for v in body.split(',')]
    return result

refs = collections.defaultdict(set)
models = set()
names = []
for tgi, (path, _, _) in index.items():
    if not Path(path).is_relative_to(target) or tgi[0] != 0x6534284a:
        continue
    props = properties(tgi)
    if 0x27812821 in props:
        models.add(tuple(props[0x27812821]))
    if props.get(0x00000010) == [2] and 'PLOP_' in path:
        names.append(props.get(0x899afbad, props.get(0x00000020)))
    for pid, values in props.items():
        if 0x88edc900 <= pid <= 0x88edcfff:
            refs[values[0]].update(values[12:])

result = {'scanned_files': files_scanned, 'display_names': sorted(names), 'menu': 'Commercial → Ploppable CS$$ (automatic Submenus DLL routing)', 'lot_refs': [], 'model_refs': [], 'unresolved': []}
for object_type, identifiers in refs.items():
    for identifier in sorted(identifiers):
        matches = ([t for t in index if t[0] == 0x7ab50e44 and t[2] == identifier]
                   if object_type == 2 else instances.get(identifier, []))
        row = {'object_type': object_type, 'instance': f'{identifier:08x}',
               'matches': [{'tgi': dbpf.tgi_string(t), 'file': index[t][0]} for t in matches]}
        result['lot_refs'].append(row)
        if not matches:
            result['unresolved'].append(row)
        if object_type == 1:
            for tgi in matches:
                props = properties(tgi)
                if 0x27812821 in props:
                    models.add(tuple(props[0x27812821]))
                if 0x27812824 in props:
                    row['timed_prop_resource'] = {'source': index[tgi][0], 'values': props[0x27812824]}
for tgi in sorted(models):
    row = {'tgi': dbpf.tgi_string(tgi), 'file': index.get(tgi, [None])[0]}
    result['model_refs'].append(row)
    if tgi not in index:
        result['unresolved'].append(row)

(records / 'yunika-resource-audit.json').write_text(json.dumps(result, indent=2))
print(json.dumps({'scanned_files': files_scanned, 'display_names': sorted(names), 'unresolved': result['unresolved']}, indent=2))
