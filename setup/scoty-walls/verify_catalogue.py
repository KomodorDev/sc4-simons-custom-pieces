"""Read the rebuilt CBOR catalogue and verify every source wall lot is indexed."""
from pathlib import Path
import json
import struct

TASK = Path(__file__).resolve().parent
PLUGINS = Path('/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins')
data = (PLUGINS / 'lots.cbor').read_bytes()
pos = 0
STOP = object()

def take(n):
    global pos
    out = data[pos:pos+n]
    assert len(out) == n
    pos += n
    return out

def read():
    b = take(1)[0]
    major, ai = b >> 5, b & 31
    if b == 255:
        return STOP
    if major == 7:
        if ai in (20, 21): return ai == 21
        if ai in (22, 23): return None
        if ai in (25, 26, 27):
            return struct.unpack({25:'>e', 26:'>f', 27:'>d'}[ai], take({25:2,26:4,27:8}[ai]))[0]
        raise ValueError(('simple', ai))
    n = ai if ai < 24 else (int.from_bytes(take({24:1,25:2,26:4,27:8}[ai]), 'big') if ai != 31 else None)
    if major == 0: return n
    if major == 1: return -1-n
    if major in (2,3):
        assert n is not None
        raw = take(n)
        return raw.decode('utf8') if major == 3 else raw
    if major in (4,5):
        out = [] if major == 4 else {}
        count = 0
        while n is None or count < n:
            item = read()
            if item is STOP:
                assert n is None
                break
            if major == 4: out.append(item)
            else: out[item] = read()
            count += 1
        return out
    if major == 6: return read()
    raise ValueError((major, ai))

catalogue = read()
assert pos == len(data)
source = json.loads((TASK / 'review/resource-audit.json').read_text())
buildings = [x for x in source['names'] if x['type'] == 2]
lot_ids = {x['tgi'].split('-')[-1].removeprefix('0x').lower() for x in source['names'] if x['type'] == 16}
indexed_lots = {str(lot['instanceId']).lower().zfill(8): (b, lot) for b in catalogue for lot in b.get('lots', [])}
assert len(lot_ids) == 210, (len(lot_ids), list(lot_ids)[:3])
missing = sorted(lot_ids - set(indexed_lots))
assert not missing, missing
wall_entries = [{'name': indexed_lots[i][0]['name'], 'lotName': indexed_lots[i][1]['name'], 'lotId': i} for i in sorted(lot_ids)]
report = {'catalogueBuildings': len(catalogue), 'catalogueLots': sum(len(b.get('lots', [])) for b in catalogue),
          'wallLotsVerified': len(lot_ids), 'wallEntries': wall_entries,
          'unresolvedSourcePropReferences': [x['iid'] for x in source['missing_lot_refs']]}
(TASK / 'catalogue-verification.json').write_text(json.dumps(report, indent=2))
print(json.dumps({k:v for k,v in report.items() if k != 'wallEntries'}, indent=2))
