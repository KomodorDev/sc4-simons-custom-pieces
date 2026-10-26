"""Small, bounded DBPF/QFS/exemplar tools. No game files are modified here."""
from pathlib import Path
import struct

EXTENSIONS = {'.dat', '.sc4model', '.sc4lot', '.sc4desc'}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def tgi_string(key):
    return '-'.join(f'{n:08x}' for n in key)


def read_index(path):
    with Path(path).open('rb') as stream:
        header = stream.read(96)
        require(len(header) == 96 and header[:4] == b'DBPF', f'Invalid DBPF: {Path(path).name}')
        count, offset, size = struct.unpack_from('<3I', header, 36)
        require(size == count * 20 and size < 128 * 1024 * 1024, 'Unsupported DBPF index')
        require(offset >= 96 and offset + size <= Path(path).stat().st_size, 'DBPF index outside file')
        stream.seek(offset)
        data = stream.read(size)
        require(len(data) == size, 'Truncated DBPF index')
    result = [struct.unpack_from('<5I', data, n * 20) for n in range(count)]
    # Some historical installed DATs contain repeated IDs. Preserve the index
    # for auditing rather than rejecting an otherwise usable NAM installation.
    # Newly generated archives are checked strictly by the output verifier.
    require(all(start >= 96 and length > 0 and start + length <= Path(path).stat().st_size
                for _, _, _, start, length in result), 'DBPF resource outside file')
    return result


def entries(raw):
    require(len(raw) >= 96 and raw[:4] == b'DBPF', 'Invalid DBPF header')
    count, offset, size = struct.unpack_from('<3I', raw, 36)
    require(size == count * 20 and offset >= 96 and offset + size <= len(raw), 'Invalid DBPF index')
    result = {}
    for n in range(count):
        kind, group, iid, start, length = struct.unpack_from('<5I', raw, offset + n * 20)
        key = kind, group, iid
        require(start >= 96 and length > 0 and start + length <= len(raw),
                'Out-of-bounds DBPF resource')
        result[key] = raw[start:start + length]
    return result


def decompress(raw):
    signature = raw.find(b'\x10\xfb', 0, 16)
    if signature < 0:
        return raw
    data = raw[signature:]
    require(len(data) >= 5, 'Truncated QFS header')
    expected = int.from_bytes(data[2:5], 'big')
    require(expected <= 128 * 1024 * 1024, 'QFS resource too large')
    out, pos = bytearray(), 5
    try:
        while pos < len(data):
            control = data[pos]; pos += 1
            count = offset = 0
            if control < 128:
                second = data[pos]; pos += 1
                literal = control & 3
                offset = ((control & 96) << 3) + second + 1
                count = ((control & 28) >> 2) + 3
            elif control < 192:
                second, third = data[pos:pos + 2]; pos += 2
                literal = second >> 6
                offset = ((second & 63) << 8) + third + 1
                count = (control & 63) + 4
            elif control < 224:
                second, third, fourth = data[pos:pos + 3]; pos += 3
                literal = control & 3
                offset = ((control & 16) << 12) + (second << 8) + third + 1
                count = ((control & 12) << 6) + fourth + 5
            elif control < 252:
                literal = ((control & 31) << 2) + 4
            else:
                literal = control & 3
            require(pos + literal <= len(data) and len(out) + literal + count <= expected,
                    'Invalid QFS literal/length')
            out.extend(data[pos:pos + literal]); pos += literal
            require(not count or 0 < offset <= len(out), 'Invalid QFS back-reference')
            for _ in range(count):
                out.append(out[-offset])
            if control >= 252:
                break
    except (IndexError, ValueError) as error:
        raise ValueError(f'Malformed QFS resource: {error}') from error
    require(len(out) == expected, 'QFS size mismatch')
    return bytes(out)


FORMATS = {0x100: 'B', 0x200: 'H', 0x300: 'I', 0x700: 'i', 0x800: 'q', 0x900: 'f', 0xB00: 'B'}


def exemplar(raw):
    raw = decompress(raw)
    require(len(raw) >= 24 and raw[:4] in {b'EQZB', b'CQZB'}, 'Unsupported exemplar format')
    parent = list(struct.unpack_from('<3I', raw, 8))
    count = struct.unpack_from('<I', raw, 20)[0]
    result, pos = [], 24
    try:
        for _ in range(count):
            pid, kind, key, flag = struct.unpack_from('<IHHB', raw, pos); pos += 9
            require(key in {0, 0x80}, 'Unsupported exemplar key type')
            n = 1
            if key == 0x80:
                n = struct.unpack_from('<I', raw, pos)[0]; pos += 4
            require(n <= len(raw), 'Invalid exemplar count')
            if kind == 0xC00:
                length = n if key == 0x80 else flag
                require(pos + length <= len(raw), 'Truncated exemplar string')
                values = raw[pos:pos + length].decode('utf8'); pos += length
            else:
                require(kind in FORMATS, f'Unsupported exemplar property type {kind:04x}')
                fmt = '<' + FORMATS[kind] * n
                values = list(struct.unpack_from(fmt, raw, pos)); pos += struct.calcsize(fmt)
            result.append({'id': f'0x{pid:08x}', 'type': f'0x{kind:04x}', 'key_type': f'0x{key:04x}',
                           'values': values, 'repetitions': n if key == 0x80 else None})
    except (struct.error, UnicodeError) as error:
        raise ValueError(f'Malformed exemplar: {error}') from error
    require(pos == len(raw), 'Unexpected exemplar trailing bytes')
    return {'parent': parent, 'properties': result}


def encode_exemplar(record):
    out = bytearray(b'EQZB1###' + struct.pack('<3I', *record['parent']) + struct.pack('<I', len(record['properties'])))
    for p in record['properties']:
        pid, kind, key = (int(p[name], 16) if isinstance(p[name], str) else p[name]
                          for name in ('id', 'type', 'key_type'))
        values = p['values']
        if kind == 0xC00:
            require(key == 0x80, 'String exemplar must use array key')
            values = values.encode('utf8')
        out.extend(struct.pack('<IHHB', pid, kind, key, 0))
        if key == 0x80:
            out.extend(struct.pack('<I', len(values)))
        out.extend(values if kind == 0xC00 else struct.pack('<' + FORMATS[kind] * len(values), *values))
    return bytes(out)


def pack_dbpf(resources):
    require(resources, 'Cannot write an empty DBPF')
    header = bytearray(96); header[:4] = b'DBPF'
    struct.pack_into('<2I', header, 4, 1, 0); struct.pack_into('<I', header, 32, 7)
    body, index = bytearray(), bytearray()
    for key, data in sorted(resources.items()):
        require(len(key) == 3 and data, 'Invalid resource')
        index.extend(struct.pack('<5I', *key, 96 + len(body), len(data))); body.extend(data)
    struct.pack_into('<3I', header, 36, len(resources), 96 + len(body), len(index))
    return bytes(header + body + index)


def index_plugins(plugins, exclude=None):
    root = Path(plugins)
    require(root.is_dir(), f'Plugins folder does not exist: {root}')
    result = {}
    for path in sorted(root.rglob('*')):
        if exclude is not None and path.is_relative_to(Path(exclude)):
            continue
        # Reject symlinked archive/folder content instead of overlooking loaded files.
        if path.is_symlink():
            if path.is_dir() or path.suffix.lower() in EXTENSIONS:
                raise ValueError(f'Symlinked resource content must be audited explicitly: {path}')
            continue  # DLLs and other non-DBPF links do not define network IDs.
        if path.is_file() and path.suffix.lower() in EXTENSIONS:
            for kind, group, iid, start, length in read_index(path):
                paths = result.setdefault((kind, group, iid), [])
                if path not in paths:
                    paths.append(path)
    return result
