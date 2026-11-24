#!/usr/bin/env python3
"""Same-vendor independent recomputation, not learner-marker acceptance.

Independent oracles recover graph coefficients from points, use Euclidean cosine
law for the origin angle, and sum individual trapezium areas at 90-digit precision.
The source generator's answer function is never used as its own oracle.
"""
import argparse
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
import hashlib
import importlib.util
import importlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import mpmath as mp

WB=Path(__file__).resolve().parents[1]
from build_source import load_source
V=importlib.import_module(load_source().__package__+'.groups.visual')
mp.mp.dps=90

def sf(x, n=3):
    dec=Decimal(str(x)); exponent=dec.adjusted()-n+1
    return format(dec.quantize(Decimal(1).scaleb(exponent),rounding=ROUND_HALF_UP),'f')

def main():
    choices=V.choices(); checks=[]; frozen=[]; assets=[]
    assert [len(c['parameters']) for c in choices]==[44,22,30]
    oracle=json.loads((WB/'planning/d4/visual-domain-checks.json').read_text())
    expected={r['recipe_id']:{json.dumps(q['parameters'],sort_keys=True) for q in r['admitted'] if not(r['recipe_id']=='WB8227-trapezium-sketch-estimate' and q['parameters']['h']==2)} for r in oracle['branches']}
    for c in choices:
        assert {json.dumps(p,sort_keys=True)for p in c['parameters']}==expected[c['recipe_id']]
        complete_keys=set(); by_part={}
        for i,p in enumerate(c['parameters']):
            q=V.build(c['recipe_id'],c['branch_id'],p)
            again=V.build(c['recipe_id'],c['branch_id'],dict(p))
            assert json.dumps(q,sort_keys=True)==json.dumps(again,sort_keys=True)
            assert len(q['parts'])=={'WB8227-modulus-graph-recovery':1,'WB8227-trapezium-sketch-estimate':4,'WB8227-vector-geometry':2}[c['recipe_id']]
            marks=sum(z['marks']for part in q['parts']for z in part['criteria'])
            assert marks=={'WB8227-modulus-graph-recovery':3,'WB8227-trapezium-sketch-estimate':10,'WB8227-vector-geometry':7}[c['recipe_id']]
            if c['recipe_id']=='WB8227-modulus-graph-recovery':
                pts=q['private_math']['given_points']; vx,vy=pts['V']; zx,zy=pts['R']
                aa=Fraction(zy-vy,zx-vx); bb=-vx; cc=vy
                # All four labelled points checked independently from recovery.
                assert all(aa*abs(x+bb)+cc==y for x,y in pts.values())
                assert [aa,bb,cc]==[p['a'],p['b'],-p['a']*p['d']]
                assert q['private_math']['coefficients']==dict(a=int(aa),b=bb,c=cc)
                assert aa/p['d']!=aa and aa/abs(bb)!=aa
                assert bb!=pts['Y'][1]
                result={'coefficients':[str(aa),bb,cc],'point_residuals':[0]*4}
            elif c['recipe_id']=='WB8227-vector-geometry':
                uv=q['private_math']['vectors']; u,v,w=[uv[k]for k in ('OA','OB','OC')]
                exact_p=Fraction(q['private_math']['p_fraction'])
                resultant=[exact_p*u[j]-v[j]for j in range(3)]
                assert sum(resultant[j]*w[j]for j in range(3))==0
                # Angle by three Euclidean side lengths: not runtime dot formula.
                ua=sum(mp.mpf(x)**2 for x in u); vb=sum(mp.mpf(x)**2 for x in v)
                ab=sum(mp.mpf(u[j]-v[j])**2 for j in range(3))
                angle=mp.acos((ua+vb-ab)/(2*mp.sqrt(ua*vb)))*180/mp.pi
                expected_display=str(90 if abs(angle-90)<mp.mpf('1e-80') else 60) if abs(angle-90)<mp.mpf('1e-80') or abs(angle-60)<mp.mpf('1e-80') else format(Decimal(str(angle)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP),'f')
                assert expected_display==q['private_math']['angle_display']
                assert abs(angle-mp.mpf(q['private_math']['angle_degrees']))<mp.mpf('4e-14')
                assert exact_p!=0 and u!=w
                result={'resultant_dot_OC':'0','angle_cosine_law':str(angle),'display':expected_display}
            else:
                h,L,n,k=[p[x]for x in ('h','L','n','k')]
                assert h!=2
                lo=h+1; dx=mp.mpf(L)/n
                # Independently add each area; runtime uses composite weighting.
                total=mp.fsum(dx*(mp.log(lo+j*dx-h)+mp.log(lo+(j+1)*dx-h))/2 for j in range(n))
                actual=mp.quad(lambda x:mp.log(x-h),[lo,lo+L])
                assert total<actual
                assert sf(total)==q['private_math']['a_3sf']
                assert sf(2*k*total)==q['private_math']['b_guard_3sf']
                assert sf(total**2)!=sf(2*k*total)
                assert sf(k*total)!=sf(2*k*total)
                result={'individual_area_sum':str(total),'numerical_integral':str(actual),'underestimate':True,'a_3sf':sf(total),'b_3sf':sf(2*k*total)}
            for part in q['parts']:
                assert part['prompt']and part['reference_answer']and part['worked_steps']
                assert all(all(s.get(k) for k in ('action','reason','result'))for s in part['worked_steps'])
            ids=[z['criterion_id']for part in q['parts']for z in part['criteria']]
            assert len(ids)==len(set(ids))
            # Transport/control characters and doubled TeX command escapes.
            for text in _strings(q):
                assert not any(ord(ch)<32 and ch not in '\n\t' for ch in text)
                assert '\\\\frac' not in text and '\\\\begin' not in text
            for a in q['assets']:
                root=ET.fromstring(a['svg']); assert root.tag.endswith('svg')
                assert a['role'] in ('question','solution') and a['must_read_givens']
                assert '<script'not in a['svg'] and 'http://'not in a['svg'].replace('http://www.w3.org/2000/svg','')
                name=f"{c['recipe_id']}-{i:02d}-{a['asset_id']}.svg"
                asset_file=WB/'authoring/visual'/name;asset_file.write_text(a['svg'])
                assets.append({'path':str(asset_file.relative_to(WB)), 'sha256':hashlib.sha256(a['svg'].encode()).hexdigest(),'parameters':p,'role':a['role']})
            complete_keys.add(json.dumps(q['exposure_keys']))
            for part,key in q['part_exposure_keys'].items():by_part.setdefault(part,set()).add(key)
            checks.append({'recipe_id':c['recipe_id'],'parameters':p,'status':'pass','oracle':result})
            if i in (0,len(c['parameters'])//2,len(c['parameters'])-1):
                frozen.append({'recipe_id':c['recipe_id'],'branch_id':c['branch_id'],'parameters':p,'question':q})
        expected_parts={'WB8227-modulus-graph-recovery':{'a':44},'WB8227-vector-geometry':{'a':30,'b':17},'WB8227-trapezium-sketch-estimate':{'a':4,'b':11,'c':2,'d':8}}
        assert {k:len(v)for k,v in by_part.items()}==expected_parts[c['recipe_id']]
    # Explicit negative fixtures: out-of-domain and blocked exact original sketch.
    rejected=[]
    for rid,branch,p in [(V.RECIPES[0],'vertex-intercepts',dict(a=0,b=3,d=2)),(V.RECIPES[0],'vertex-intercepts',dict(a=True,b=3,d=2)),(V.RECIPES[0],'vertex-intercepts',dict(a=-2,b=3,d=1)),(V.RECIPES[1],'logarithmic-hence-chain',dict(h=2,L=4,n=2,k=1)),(V.RECIPES[1],'logarithmic-hence-chain',dict(h=1,L=4,n=4,k=2)),(V.RECIPES[2],'scalar-combination-and-origin-angle',dict(r=2,s=2,t=2))]:
        try:V.build(rid,branch,p)
        except ValueError:rejected.append({'recipe_id':rid,'parameters':p,'rejected':True})
        else:raise AssertionError('Bad parameters admitted')
    out=WB/'authoring/visual';out.mkdir(exist_ok=True)
    write=lambda n,d:(out/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
    write('independent-recomputation.json',{'status':'pass','scope':'Same-vendor all-domain mathematical recomputation and structural author checks; not independent content acceptance, actual app rendering or submission recognition.','instances':len(checks),'checks':checks,'negative_fixtures':rejected,'part_semantic_counts':{'modulus':[44],'trapezium':[4,11,2,8],'vector':[30,17]}})
    write('frozen-examples.json',frozen)
    write('asset-index.json',assets)
    (WB/'source/domains/visual.json').write_text(json.dumps({'version':'0.1.4','approval_manifest':'4a0548320dcb9209dcd28e18bd4f6c77423480de6538fcbf1b0f8b6d0e17d8ec','choices':choices,'rights':'Purpose-built questions and original generated SVGs. Textbook originals internal only. h=2 original-subtask route not enabled.'},indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':'pass','all_domain_instances':len(checks),'assets':len(assets),'negatives_rejected':len(rejected)}))

def _strings(x):
    if isinstance(x,str):yield x
    elif isinstance(x,dict):
        for v in x.values():yield from _strings(v)
    elif isinstance(x,list):
        for v in x:yield from _strings(v)

if __name__=='__main__':main()
