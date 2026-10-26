from pathlib import Path
import sys,json,struct,re,collections
sys.path.insert(0,'setup/cam-install/runtime-audit')
import read_dbpf as d
src=Path('setup/scoty-walls/review/audit.py').read_text()
scope={}
exec(compile(src.split('files={')[0],'<audit-functions>','exec'),scope)
index=scope['index'];entriesfor=scope['entriesfor'];exemplar=scope['exemplar'];pmap=scope['pmap']
IIDS=['be202bdb','156a22b6','98184c27','dcd62688','fcc26c91','3e227745','da3159ff']
TARGETS={i:struct.pack('<I',int(i,16)) for i in IIDS}
roots=[Path('/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins'),Path('/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/SharedSupport/prefix/drive_c/GOG Games/SimCity 4 Deluxe Edition'),Path('setup/scoty-walls/staging-plugins')]
found=[];failures=[]
for root in roots:
 for p in root.rglob('*'):
  if p.suffix.lower() not in ('.dat','.sc4lot','.sc4desc','.sc4model'):continue
  idx=index(p)
  for tgi,raw in entriesfor(p,idx,{0x6534284a,0x05342861}):
   raw=d.decompress(raw)
   hits=[iid for iid,b in TARGETS.items() if b in raw or iid.encode() in raw.lower()]
   if not hits:continue
   try:x=exemplar(raw);pm=pmap(x)
   except Exception as e:failures.append({'file':str(p),'tgi':d.tgi_string(tgi),'error':str(e),'hits':hits});continue
   props=[v for v in x['properties'] if any((isinstance(v['values'],list) and int(iid,16) in v['values']) or (isinstance(v['values'],str) and iid in v['values'].lower()) for iid in hits)]
   found.append({'file':str(p),'tgi':d.tgi_string(tgi),'name':pm.get(0x20),'type':pm.get(0x10),'hits':hits,'props':props})
report={'found':found,'parse_failures':failures}
Path('setup/scoty-walls/review/remaining-prop-investigation.json').write_text(json.dumps(report,indent=2))
print('Matches',len(found),'parsefailures',len(failures))
for x in found:
 if x['type']!=[0x10]: print(json.dumps(x,indent=2))
print(json.dumps(failures,indent=2))
