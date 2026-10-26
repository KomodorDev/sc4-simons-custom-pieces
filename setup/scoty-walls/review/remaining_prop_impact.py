from pathlib import Path
import sys,json,zipfile,hashlib
sys.path.insert(0,'setup/cam-install/runtime-audit')
import read_dbpf as d
scope={};src=Path('setup/scoty-walls/review/audit.py').read_text();exec(compile(src.split('files={')[0],'<audit-functions>','exec'),scope)
exemplar=scope['exemplar'];pmap=scope['pmap']
roots=Path('setup/scoty-walls/review')
current=json.loads((roots/'exemplars-all.json').read_text())
missing=json.loads((roots/'resource-audit.json').read_text())['missing_lot_refs']
wanted={int(r['iid'],16) for r in missing}
old={}
with zipfile.ZipFile('setup/sc4pac-local-channel/assets/Scoty Walls Sets_1-1.zip') as z:
 for name in z.namelist():
  if not name.lower().endswith('.dat'):continue
  for tgi,raw in d.entries(z.read(name)).items():
   if tgi[0] not in (0x6534284a,0x05342861):continue
   try:x=exemplar(raw)
   except ValueError:continue
   x['file']=name;x['tgi']=d.tgi_string(tgi);pm=pmap(x)
   old[x['tgi']]=x
report={'missing':[],'ordinary_concrete':[],'affected_lots':[]}
for r in missing:
 iid=int(r['iid'],16);examples=[]
 for ex in current:
  if ex['exemplar_type']!=16:continue
  for p in ex['properties']:
   v=p['values']
   if p['name'].startswith('LotConfigPropertyLotObject') and len(v)>=13 and v[0]==1 and v[12]==iid:
    examples.append({'lot':ex['name'],'tgi':ex['tgi'],'position_metres':[round(n/65536,4) for n in v[3:6]],'footprint_metres':[round((v[8]-v[6])/65536,4),round((v[9]-v[7])/65536,4)],'present_in_1_1':any(op['name'].startswith('LotConfigPropertyLotObject') and len(op['values'])>=13 and op['values'][0]==1 and op['values'][12]==iid for op in old.get(ex['tgi'],{}).get('properties',[]))})
 report['missing'].append({'iid':r['iid'],'unique_lots':len(set(r['lots'])),'examples':examples})
for ex in current:
 if ex['exemplar_type']!=16:continue
 refs=[p['values'][12] for p in ex['properties'] if p['name'].startswith('LotConfigPropertyLotObject') and len(p['values'])>=13 and p['values'][0]==1]
 misses=sorted(set(refs)&wanted)
 if misses:report['affected_lots'].append({'name':ex['name'],'tgi':ex['tgi'],'missing':['%08x'%i for i in misses]})
 if 'beton' in ex['name'].lower() and ('straight' in ex['name'].lower() or 'stairs' in ex['name'].lower()):
  report['ordinary_concrete'].append({'name':ex['name'],'tgi':ex['tgi'],'missing':['%08x'%i for i in misses]})
report['affected_lot_count']=len(report['affected_lots'])
report['all_missing_refs_already_in_1_1']=all(e['present_in_1_1'] for r in report['missing'] for e in r['examples'])
(roots/'remaining-prop-impact.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='missing'},indent=2))
