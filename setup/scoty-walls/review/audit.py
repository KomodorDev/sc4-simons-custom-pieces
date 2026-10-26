from pathlib import Path
import sys,json,re,struct,collections
sys.path.insert(0,'setup/cam-install/runtime-audit')
import read_dbpf as d
ROOT=Path('setup/scoty-walls/review')
PLUGIN=Path('/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins')
GAME=Path('/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/SharedSupport/prefix/drive_c/GOG Games/SimCity 4 Deluxe Edition')
def exemplar(raw):
 raw=d.decompress(raw)
 if raw[:4] in (b'EQZB',b'CQZB'):return d.exemplar(raw)
 if raw[:4] not in (b'EQZT',b'CQZT'):raise ValueError(raw[:50])
 t=raw.decode('utf-8','replace'); m=re.search(r'ParentCohort=Key:\{([^}]+)\}',t)
 out={'parent':[int(a.strip(),0) for a in m.group(1).split(',')] if m else [],'properties':[]}
 for line in t.splitlines():
  m=re.match(r'(0x[0-9a-fA-F]+):\{"(.*?)"\}=(\w+):(\d+):\{(.*)\}',line)
  if not m:continue
  pid,name,typ,count,vals=m.groups()
  if typ=='String': vals=vals.strip('"')
  elif typ.startswith('Float'):vals=[float(v.strip()) for v in vals.split(',') if v.strip()]
  else:vals=[int(v.strip(),0) for v in vals.split(',') if v.strip()]
  out['properties'].append({'id':f'0x{int(pid,0):08x}','name':d.NAMES.get(int(pid,0),name),'type':typ,'values':vals})
 return out

def pmap(ex):return {int(p['id'],16):p['values'] for p in ex['properties']}
def index(path):
 with path.open('rb') as f:
  header=f.read(96)
  if header[:4]!=b'DBPF':return {}
  count,off,sz=struct.unpack_from('<3I',header,36)
  if count==0:return{}
  if sz//count!=20:return{}
  f.seek(off);raw=f.read(sz)
  return {(t,g,i):(start,l) for t,g,i,start,l in struct.iter_unpack('<5I',raw)}
def entriesfor(path,idx,types):
 with path.open('rb') as f:
  for tgi,(off,size) in idx.items():
   if tgi[0] not in types:continue
   f.seek(off);yield tgi,f.read(size)

files={str(p):index(p) for p in sorted(ROOT.rglob('*.dat'))}
allidx=collections.defaultdict(list)
for p,idx in files.items():
 for tgi in idx:allidx[tgi].append(p)
exs=[];ltext={}
for p,idx in files.items():
 for tgi,raw in entriesfor(Path(p),idx,{0x6534284a,0x05342861,0x2026960b}):
  if tgi[0]==0x2026960b:
   raw=d.decompress(raw); ltext[tgi]=raw[4:].decode('utf-16le','replace').rstrip('\x00');continue
  x=exemplar(raw);x['tgi']=d.tgi_string(tgi);x['file']=p
  pm=pmap(x);x['name']=pm.get(0x20,'');x['exemplar_type']=pm.get(0x10,[None])[0]
  exs.append(x)
for x in exs:
 pm=pmap(x); nkey=pm.get(0x8a416a99)
 if nkey:x['display_name']=ltext.get(tuple(nkey))
refs={}
for x in exs:
 if x['exemplar_type']!=0x10:continue
 for p in x['properties']:
  pid=int(p['id'],16);v=p['values']
  if 0x88edc900 <= pid <= 0x88edcfff and len(v)>=13 and v[0] in (0,1,2):
   refs.setdefault((v[0],v[12]),{'kind':v[0],'iid':f'{v[12]:08x}','lots':[]})['lots'].append(x['name'])
# Include source and active game index; never modify game files.
for origin,base in [('plugins',PLUGIN),('game',GAME)]+[('extra',Path(a)) for a in sys.argv[1:]]:
 for p in base.rglob('*'):
  if p.suffix.lower() not in {'.dat','.sc4lot','.sc4desc','.sc4model'}:continue
  idx=index(p)
  if not idx:continue
  files[str(p)]=idx
  for tgi in idx:allidx[tgi].append(str(p))
by_iid=collections.defaultdict(list)
for tgi,paths in allidx.items():
 by_iid[tgi[0],tgi[2]].extend(paths)
for (kind,iid),ref in refs.items():
 typ=0x7ab50e44 if kind==2 else 0x6534284a
 matches=by_iid.get((typ,iid),[])
 if kind==2 and not matches:
  matches=[p for j in range(5) for p in by_iid.get((typ,(iid&~0xf)+j),[])]
 ref['files']=sorted(set(matches))
unresolved=[r for r in refs.values() if not r['files']]
# Check unresolved prop/building families against all exemplar membership declarations.
wanted={int(r['iid'],16) for r in unresolved if r['kind'] in (0,1)}
for p,idx in files.items():
 if not wanted:break
 for tgi,raw in entriesfor(Path(p),idx,{0x6534284a}):
  try:x=exemplar(raw)
  except Exception:continue
  pm=pmap(x)
  for fam in pm.get(0x27812870,[]):
   if fam in wanted:
    for kind in (0,1):
     if (kind,fam) in refs:refs[kind,fam]['files'].append(p);refs[kind,fam]['family']=True
unresolved=[r for r in refs.values() if not r['files']]
counts=collections.Counter((Path(x['file']).name,x['exemplar_type']) for x in exs)
report={'counts':[{ 'file':k[0],'type':k[1],'count':v} for k,v in sorted(counts.items())],'missing_lot_refs':unresolved,'refs':list(refs.values()),'names':[{'file':Path(x['file']).name,'tgi':x['tgi'],'type':x['exemplar_type'],'name':x['name'],'display_name':x.get('display_name')} for x in exs]}
(ROOT/'resource-audit.json').write_text(json.dumps(report,indent=2))
(ROOT/'exemplars-all.json').write_text(json.dumps(exs,indent=2))
print(json.dumps({'counts': report['counts'], 'missing_lot_refs': [{'kind': r['kind'], 'iid': r['iid'], 'lot_count': len(set(r['lots']))} for r in report['missing_lot_refs']]},indent=2))
print('Distinct refs',len(refs),'missing',len(unresolved))
print('Display names are recorded in resource-audit.json')
print('Custom props:',[(x['name'],x['tgi']) for x in exs if x['exemplar_type']==0x1e])
