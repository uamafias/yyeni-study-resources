"""Independent asset integrity and numerical cross-checks; does not grant acceptance."""
from pathlib import Path
import hashlib
import json
import math
import subprocess
import sys
from PIL import Image

W = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(W / 'assets/code'))
import map42

results = []
def check(name, condition, evidence):
    results.append({'check': name, 'passed': bool(condition), 'evidence': evidence})
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

m = json.loads((W / 'assets/asset-manifest-6137.json').read_text())
pngs = set()
for r in m['resources']:
    for rel, digest in r['file_hashes'].items():
        p = W / rel
        check('hash:' + rel, p.is_file() and sha(p) == digest, digest)
        if p.suffix == '.png':
            with Image.open(p) as im:
                im.verify()
            pngs.add(rel)
    if r['kind'] == 'licensed_photo':
        p = W / ('assets/sources/photos/' + r['resource_id'] + '_original.jpg')
        actual = hashlib.sha1(p.read_bytes()).hexdigest()
        check('Commons original:' + r['resource_id'], actual == r['licence']['commons_sha1'], actual)
check('resource/binding/image counts', (len(m['resources']),len(m['item_bindings']),len(pngs)) == (54,107,153), [len(m['resources']),len(m['item_bindings']),len(pngs)])
# PROJ is a separate projection implementation, not the author's Snyder series.
coords = [(-(23+0.5/60),17+0.5/60), (-(23+1.5/60),17+1.5/60), (-(23+1/60),17+1/60)]
raw = ''.join(f'{lon:.12f} {lat:.12f}\n' for lat,lon in coords)
out = subprocess.run(['/opt/homebrew/bin/proj','+proj=tmerc','+ellps=WGS84','+lat_0=-23.0166666666667','+lon_0=17.0166666666667','+k=1','-f','%.6f'], input=raw, text=True, capture_output=True, check=True).stdout
for (lat,lon), line in zip(coords,out.splitlines()):
    independent = tuple(map(float,line.split()[:2]))
    author = map42.tm(lat,lon)
    delta = math.dist(independent,author)
    check('TM vs PROJ:' + str((lat,lon)), delta < 0.001, {'metre_error':delta,'PROJ':independent})
# Integrate the analytic road independently with a 20,000-interval midpoint rule.
_, amplitude, _ = map42.road_ab()
n = 20000
length = sum(math.hypot(2000, amplitude*math.pi*math.cos(math.pi*(j+.5)/n)) for j in range(n))/n
check('road analytic integral', abs(length-3000)<.02, length)
check('terrain endpoints', abs(map42.height(2000,2000)-1500)<1e-8 and abs(map42.height(4000,2000)-1540)<1e-8, [map42.height(2000,2000),map42.height(4000,2000)])
for level in [1500,1510,1520,1530]:
    vertices=map42.contour(level)
    error=max(abs(map42.height(x,y)-level) for x,y in vertices)
    check('contour vertices:' + str(level), error<1e-8, error)
for name, actual, expected in [
    ('straight distance km',4*500/1000,2), ('curved distance km',6*500/1000,3),
    ('square km2',(4*500/1000)**2,4), ('gradient denominator',2000/40,50),
    ('questionnaire quiet percent',12/20*100,60), ('questionnaire busy percent',8/20*100,40),
    ('visitor percent',16/20*100,80), ('reservoir closing stock',100+20-30-10,80),
    ('groyne updrift percent',(30-20)/20*100,50), ('litter reduction percent',(20-8)/20*100,60),
    ('signed tracer mean',(2+4+1-1)/4,1.5), ('second signed tracer mean',(3+2-1+4)/4,2),
    ('tourism receipts',8000+7000+5000,20000), ('farm allocation',1800+200+300+100,2400),
    ('fish allocation',4+5+1,10), ('pyramid A dependants',300+100,400), ('pyramid B dependants',200+200,400),
]:
    check(name,abs(actual-expected)<1e-8,actual)
report={'reviewer':'Codex','result':'PASS' if all(x['passed'] for x in results) else 'FAIL','checks':results}
(W/'review/visual-independent-checks-6137.json').write_text(json.dumps(report,indent=2)+'\n')
print(report['result'],len(results),'checks;',len(pngs),'decoded PNGs')
sys.exit(0 if report['result']=='PASS' else 1)
