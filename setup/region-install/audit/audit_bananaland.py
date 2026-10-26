"""Read-only analysis of the downloaded region. Sources: Killeroo/SC4Parser."""
import sys, zipfile, struct, json, hashlib
from pathlib import Path
import numpy as np
BASE=Path('/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City')
sys.path.insert(0,str(BASE/'setup/cam-install/runtime-audit'))
import read_dbpf as dbpf
OUT=BASE/'setup/region-install/audit'
ARCHIVE=Path('/Users/simonhinterreiter/Downloads/Bananaland-V2.zip')
TYPES={0xc9bd5d4a:'lots',0xa9bd882d:'buildings',0xc9c05c6e:'surface_networks',0xca16374f:'underground_networks',0x49c1a034:'prebuilt_networks',0x49cc1bcd:'bridges',0x8a4bd52b:'tunnels',0xc9c05c5d:'power_lines'}
report={'archive':str(ARCHIVE),'sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'schema_sources':['https://github.com/Killeroo/SC4Parser/blob/master/SC4Parser/SubFiles/RegionViewSubfile.cs','https://github.com/Killeroo/SC4Parser/blob/master/SC4Parser/Constants.cs','https://github.com/Killeroo/SC4Parser/blob/master/SC4Parser/SubFiles/TerrainMapSubfile.cs'],'terrain_metrics':'Each building grid cell has four terrain corner heights; flat means <=1 metre total corner height variation. Land means all corners >250m (standard sea level). One city grid cell is 16m wide. Grid positions are config.bmp coordinates, in units of small cities.','cities':[]}
with zipfile.ZipFile(ARCHIVE) as z:
 for name in sorted(n for n in z.namelist() if n.endswith('.sc4')):
  file=z.read(name); entries=dbpf.entries(file)
  region=dbpf.decompress(entries[0xca027edb,0xca027ee1,0])
  major,minor=struct.unpack_from('<HH',region)
  assert (major,minor)==(1,13)
  x,y,sx,sy,r,c,i=struct.unpack_from('<7I',region,4)
  pos=63; mode=region[pos]; pos+=1
  strings=[]
  for _ in range(5):
   n=struct.unpack_from('<I',region,pos)[0];pos+=4
   strings.append(region[pos:pos+n].decode('utf-8','replace'));pos+=n
  terrain=dbpf.decompress(entries[0xa9dd6ff4,0xe98f9525,1])
  h=np.frombuffer(terrain,dtype='<f4',offset=2).reshape((sx*64+1,sy*64+1))
  corners=[h[:-1,:-1],h[1:,:-1],h[:-1,1:],h[1:,1:]]
  lo=np.minimum.reduce(corners); hi=np.maximum.reduce(corners)
  land=lo>250
  flat=land&((hi-lo)<=1)
  # Sliding 64x64 cell (1.024km square) windows; select most flat land in window.
  summed=np.pad(flat.astype(np.int32).cumsum(0).cumsum(1),((1,0),(1,0)))
  w=64;window=summed[w:,w:]-summed[:-w,w:]-summed[w:,:-w]+summed[:-w,:-w]
  best=np.unravel_index(window.argmax(),window.shape)
  development={label:sum(len(dbpf.decompress(data)) for tgi,data in entries.items() if tgi[0]==tid) for tid,label in TYPES.items()}
  city={'filename':name,'sha256':hashlib.sha256(file).hexdigest(),'position':[x,y],'size':[sx,sy],'population':{'residential':r,'commercial':c,'industrial':i},'mode_flag':mode,'city_name':strings[0],'former_city_name':strings[1],'mayor_name':strings[2],'development_subfile_bytes':development,'terrain':{'min_height_m':float(h.min()),'max_height_m':float(h.max()),'land_percent':round(land.mean()*100,2),'flat_land_percent_of_city':round(flat.mean()*100,2),'best_1024m_square_flat_percent':round(int(window[best])/4096*100,2),'best_square_origin_cell':[int(a) for a in best]}}
  report['cities'].append(city)
summary={'city_count':len(report['cities']),'mode_flags':sorted(set(c['mode_flag'] for c in report['cities'])),'population_totals':{n:sum(c['population'][n] for c in report['cities']) for n in ['residential','commercial','industrial']},'development_subfile_bytes':{n:sum(c['development_subfile_bytes'][n] for c in report['cities']) for n in TYPES.values()},'city_sizes':sorted(set(tuple(c['size']) for c in report['cities'])),'best_flat_tiles':sorted(report['cities'],key=lambda c:(c['terrain']['flat_land_percent_of_city'],c['terrain']['land_percent']),reverse=True)[:12]}
report['summary']=summary
(OUT/'bananaland-audit.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in summary.items() if k!='best_flat_tiles'},indent=2))
for c in summary['best_flat_tiles']:
 print(c['filename'],c['position'],c['terrain'])
