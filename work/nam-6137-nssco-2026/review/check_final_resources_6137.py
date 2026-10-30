"""Independent checks for the final-resource review; never grants acceptance."""
from pathlib import Path
import collections
import hashlib
import json
import math
import zipfile
import shapefile
from shapely.geometry import shape
from shapely.ops import transform
from PIL import Image

W = Path(__file__).resolve().parents[1]
checks = []
def check(name, passed, evidence):
    checks.append(dict(check=name, passed=bool(passed), evidence=evidence))
def read(p): return json.loads(p.read_text())
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

m = read(W/'assets/asset-manifest-6137.json')
old = read(W/'review/codex-final-resources-input-manifest-6137.json')
for r in m['resources']:
    for rel, h in r['file_hashes'].items():
        check('file hash: '+rel, digest(W/rel)==h, h)
        if rel.endswith('.png'):
            with Image.open(W/rel) as im: im.verify()
check('active resource and binding totals', (len(m['resources']),len(m['item_bindings']))==(56,112), [len(m['resources']),len(m['item_bindings'])])
original = {r['resource_id']:r for r in old['resources']}
unchanged_pngs = []
for rid in ['VIS-6137-2.3-01','VIS-6137-2.3-02']:
    for p,h in original[rid]['file_hashes'].items():
        if p.endswith('.png') and '-P04-' not in p and '-P05-' not in p:
            unchanged_pngs.append(p)
            check('unrelated practical image unchanged: '+p,digest(W/p)==h,h)

src = W/'assets/sources/maps'
new = read(src/'geoBoundaries-gbHumanitarian-NAM-ADM1.geojson')['features']
rejected = read(src/'geoBoundaries-NAM-ADM1.geojson')['features']
names = [f['properties']['shapeName'] for f in new]
check('NSA base contains 14 named regions',len(new)==14 and {'Zambezi','Kavango East','Kavango West'}<=set(names),names)
check('rejected old base really has 13 regions',len(rejected)==13,len(rejected))

# Cylindrical equal-area transform with authalic spherical radius, independent
# of the author's centroid-cosine area approximation.
def project(x,y,z=None): return 6371.0072*math.radians(x),6371.0072*math.sin(math.radians(y))
atlas=src/'atlas'
conservation=atlas/'Figure 8_09 Conservation areas 2020'
for file,targets,field in [('Protected_Areas_Atlas.shp',['Etosha National Park'],'AREA_KM2_'),('Communal_Conservancies_Atlas.shp',['Torra','Salambala'],'AREA_KM2')]:
    r=shapefile.Reader(str(conservation/file), encoding='latin1')
    found=[]
    for sr in r.iterShapeRecords():
        d=sr.record.as_dict()
        if d['NAME'] in targets:
            found.append(d['NAME']);g=shape(sr.shape.__geo_interface__)
            area=transform(project,g).area
            check('independent equal-area check: '+d['NAME'],abs(area/d[field]-1)<.05,{'km2':area,'attribute':d[field]})
            if d['NAME'] in ['Torra','Salambala']:
                expected_region={'Torra':'Kunene','Salambala':'Zambezi'}[d['NAME']]
                check('conservancy registration: '+d['NAME'],(d['YEAR_REG'],d['MONTH_REG'],d['REGION'])==(1998,6,expected_region),d)
    check('named conservation features found: '+file,set(found)==set(targets),found)
r=shapefile.Reader(str(conservation/'Communal_Conservancies_Atlas.shp'), encoding='latin1')
counts=collections.Counter(d.as_dict()['NAME'] for d in r.records())
check('conservancy records distinguished from unique names',len(r)==89 and len(counts)==87,{'records':len(r),'unique_names':len(counts),'repeated_names':[n for n,c in counts.items() if c>1],'interpretation':'These are dataset records, not a taught national total.'})

coords={}
with zipfile.ZipFile(src/'geonames-NA.zip') as z:
    for line in z.read('NA.txt').decode().splitlines():
        f=line.split('\t')
        if f[0] in ['12761849','3353811']:coords[f[0]]=(float(f[4]),float(f[5]))
a,b=coords['3353811'],coords['12761849']
dot=math.sin(math.radians(a[0]))*math.sin(math.radians(b[0]))+math.cos(math.radians(a[0]))*math.cos(math.radians(b[0]))*math.cos(math.radians(b[1]-a[1]))
distance=6371.0072*math.acos(dot)
check('CCF farm is about 40 km east of Otjiwarongo',38<distance<43 and b[1]>a[1] and abs(b[0]-a[0])<.04,{'km':distance,'town_latlon':a,'farm_latlon':b,'limit':'Farm location, not a surveyed building coordinate.'})

s=read(W/'assets/specs/ITEM-6137-2.3-036-PROC.json')['p04']
totals=[sum(row[2]) for row in s['sites']]
check('P04 independently summed scores',totals==[-6,-3,1,5,8] and sum(totals)/5==1,totals)
check('P04 systematic sites and facilities counterexample',[r[1] for r in s['sites']]==[0,100,200,300,400] and {r[2][4] for r in s['sites']}=={1},s['sites'])
check('P04 genuine facilities opposites',s['grid']['rows'][-1]==['Facilities clean','Facilities dirty'],s['grid']['rows'][-1])
s=read(W/'assets/specs/ITEM-6137-2.3-038-PROC.json')['p05']
means=[sum(row[2])/3 for row in s['stations']]
check('P05 independently averaged widths',means==[220,170,140,155,95],means)
check('P05 independently averaged depth',abs(sum(s['S3_depth_readings_cm'])/5-4.2)<1e-12,s['S3_depth_readings_cm'])
check('P05 systematic sites and non-monotone width',[r[1] for r in s['stations']]==[0,30,60,90,120] and means[3]>means[2],s['answer'])

summary={}
for td in sorted((W/'topics').iterdir()):
    q=read(td/'qa_report.json');c=collections.Counter(x['status'] for x in q['deterministic_checks'])
    summary[td.name]={'release_decision':q['release_decision'],'counts':dict(c),'metrics':q['metrics']}
    check('topic check suite: '+td.name,q['release_decision']=='publish' and c['fail']==0,dict(c))
(W/'review/codex-final-resource-check-summary-6137.json').write_text(json.dumps(summary,indent=2)+'\n')
check('all 801 items retained',sum(x['metrics']['learning_item_count'] for x in summary.values())==801, sum(x['metrics']['learning_item_count'] for x in summary.values()))
result={'reviewer':'Codex','result':'PASS' if all(c['passed'] for c in checks) else 'FAIL','checks':checks}
(W/'review/codex-final-resource-independent-checks-6137.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['result'],len(checks),'checks')
for c in checks:
    if not c['passed']:print(c)
