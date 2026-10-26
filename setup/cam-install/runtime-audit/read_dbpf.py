"""Read-only DBPF index, QFS and binary exemplar inspection for this audit.

This module never modifies an archive, game file, or save. Adapted from the
formats used by the already checked-out official DBPFKit source. Only ordinary
SC4 DBPF v1/20-byte index entries and EQZB/CQZB properties are supported.
"""
from pathlib import Path
import struct
import xml.etree.ElementTree as ET


def property_names():
    mapper = Path('/Users/simonhinterreiter/Applications/SC4 Plop and Paint Tools/PropertyMapper.xml')
    names = {}
    for item in ET.parse(mapper).iter('PROPERTY'):
        if item.get('ID', '').startswith('0x') and item.get('Name'):
            names.setdefault(int(item.get('ID'), 16), item.get('Name'))
    return names


NAMES = property_names()


def decompress(data):
    signature = data.find(b'\x10\xfb', 0, 16)
    if signature < 0:
        return data
    data = data[signature:]
    pos = 5
    output = bytearray()
    while pos < len(data):
        control = data[pos]
        pos += 1
        length = offset = 0
        if control < 128:
            second = data[pos]
            pos += 1
            literal = control & 3
            offset = ((control & 96) << 3) + second + 1
            length = ((control & 28) >> 2) + 3
        elif control < 192:
            second, third = data[pos:pos + 2]
            pos += 2
            literal = second >> 6
            offset = ((second & 63) << 8) + third + 1
            length = (control & 63) + 4
        elif control < 224:
            second, third, fourth = data[pos:pos + 3]
            pos += 3
            literal = control & 3
            offset = ((control & 16) << 12) + (second << 8) + third + 1
            length = ((control & 12) << 6) + fourth + 5
        elif control < 252:
            literal = ((control & 31) << 2) + 4
        else:
            literal = control & 3
        output.extend(data[pos:pos + literal])
        pos += literal
        for _ in range(length):
            output.append(output[-offset])
        if control >= 252:
            break
    assert len(output) == int.from_bytes(data[2:5], 'big'), 'QFS size mismatch'
    return bytes(output)


def entries(data):
    assert data[:4] == b'DBPF', 'Not a DBPF file'
    count, offset, size = struct.unpack_from('<3I', data, 36)
    if not count:
        return {}
    assert size // count == 20, 'Unsupported DBPF index layout'
    result = {}
    for i in range(count):
        kind, group, instance, start, length = struct.unpack_from('<5I', data, offset + i * 20)
        assert start + length <= len(data), 'Entry outside file'
        result[kind, group, instance] = data[start:start + length]
    return result


def exemplar(data):
    data = decompress(data)
    assert data[:4] in (b'EQZB', b'CQZB'), 'Not a binary exemplar or cohort'
    count = struct.unpack_from('<I', data, 20)[0]
    result = {
        'parent': list(struct.unpack_from('<3I', data, 8)),
        'properties': [],
    }
    pos = 24
    formats = {0x100: 'B', 0x200: 'H', 0x300: 'I', 0x700: 'i', 0x800: 'q', 0x900: 'f', 0xb00: 'B'}
    for _ in range(count):
        prop_id, value_type, key_type, flag = struct.unpack_from('<IHHB', data, pos)
        pos += 9
        repetitions = 1
        if key_type == 0x80:
            repetitions = struct.unpack_from('<I', data, pos)[0]
            pos += 4
        else:
            assert key_type == 0, f'Unsupported property key type {key_type:x}'
        if value_type == 0xc00:
            length = repetitions if key_type == 0x80 else flag
            values = data[pos:pos + length].decode('utf-8', 'replace')
            pos += length
        else:
            fmt = formats[value_type]
            values = list(struct.unpack_from('<' + fmt * repetitions, data, pos))
            pos += struct.calcsize(fmt) * repetitions
        result['properties'].append({
            'id': f'0x{prop_id:08x}',
            'name': NAMES.get(prop_id, f'0x{prop_id:08x}'),
            'type': f'0x{value_type:04x}',
            'key_type': f'0x{key_type:04x}',
            'repetitions': repetitions if key_type == 0x80 else None,
            'values': values,
        })
    assert pos == len(data), f'Unexpected exemplar trailing bytes: {len(data) - pos}'
    return result


def tgi_string(tgi):
    return '-'.join(f'{value:08x}' for value in tgi)
