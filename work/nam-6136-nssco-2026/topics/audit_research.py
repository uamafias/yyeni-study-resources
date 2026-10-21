"""Recompute from authored stimuli and compare authored answers, not literals."""
import json
import re
from collections import Counter
from pathlib import Path

WS=Path(__file__).resolve().parents[1]
def nums(s):
    words={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'ten':10,'twelve':12}
    for word,n in words.items():s=re.sub(r'\b'+word+r'\b',str(n),s,flags=re.I)
    return [float(x) for x in re.findall(r'(?<!\w)-?\d+(?:\.\d+)?',s)]

def match(pattern,text):
    m=re.search(pattern,text,re.I)
    if not m:raise ValueError('Authored source not recognised: '+pattern)
    return tuple(float(x) for x in m.groups())

def audit(packages_override=None, write_report=True):
    items=json.loads((WS/'topics/10.1/learning-items/topic_10.1_items.json').read_text())['items']
    packages={i['item_id'].rsplit('-',1)[-1]:i for i in items if i['item_type']!='flashcard'}
    if packages_override is not None:packages=packages_override
    answers={code:dict(re.findall(r'^(A[12]\(\d+\))\s+(.+)$',i['canonical_answer'],re.M)) for code,i in packages.items()}
    source={code:i['prompt'] for code,i in packages.items()}
    checks={};details={}
    def check(name,condition,inputs,result):
        checks[name]=bool(condition);details[name]={'authored_inputs':inputs,'computed':result}
    def answer_has(code,part,values):return all(v in nums(answers[code][part]) for v in values)
    pop,sample=match(r'population is (\d+) listed households.*?sample (\d+)',source['P01'])
    start,=match(r'random start is (\d+)',source['P01'])
    interval=pop/sample;selection=list(range(int(start),int(pop)+1,int(interval)))
    stated=re.search(r'with start \d+ select ([\d,]+)',answers['P01']['A1(3)']).group(1)
    check('systematic_selection',selection==[int(x) for x in stated.split(',')] and len(selection)==sample,
          {'population':pop,'sample':sample,'start':start},selection)
    categories=match(r'below 10 minutes (\d+) households, 10–29 minutes (\d+), 30\+ minutes (\d+)',source['P01'])
    pct=categories[-1]/sum(categories)*100
    check('water_categories_and_percent',sum(categories)==sample and answer_has('P01','A1(6)',[pct]),categories,pct)
    heights=match(r'heights (\d+),(\d+),(\d+)',answers['P01']['A1(7)'])
    check('water_bar_heights',heights==categories,categories,heights)
    cost,available=match(r'costs N\$(\d+); N\$(\d+) is available',source['P01'])
    check('water_funding_gap',answer_has('P01','A2(3)',[cost-available]),[cost,available],cost-available)
    total,a,b,s=match(r'(\d+) listed grower households, village A (\d+) and B (\d+); sample (\d+)',source['P02'])
    alloc=[a/total*s,b/total*s]
    check('stratified_allocation',a+b==total and sum(alloc)==s and answer_has('P02','A1(3)',alloc),[total,a,b,s],alloc)
    old,new=match(r'Earlier (?:total )?output (\d+) bags, later (\d+)',source['P02'])
    check('output_totals_include_spoiled','these totals include spoiled bags' in source['P02'].lower(),
          {'prompt':source['P02'].split('A1(1)',1)[0]},'Spoiled bags explicitly included in the output totals.')
    oldloss,newloss=match(r'Earlier (\d+) bags spoiled, later (\d+)',source['P02'])
    usable=[old-oldloss,new-newloss]
    check('output_and_usable_output',answer_has('P02','A2(1)',[new-old]) and answer_has('P02','A2(2)',usable),[old,new,oldloss,newloss],{'difference':new-old,'usable':usable})
    shares=match(r'water (\d+)%, land preparation (\d+)%, storage (\d+)%',source['P02'])
    length,=match(r'Use a (\d+) cm rectangle',answers['P02']['A2(3)'])
    lengths=[length*v/100 for v in shares]
    check('rectangle_lengths',sum(shares)==100 and answer_has('P02','A2(3)',lengths+[lengths[0]+lengths[1]]),{'shares':shares,'length':length},lengths)
    journeys,=match(r'record (\d+) learner journeys',source['P03'])
    modes=match(r'walk (\d+), bus (\d+), other (\d+)',source['P03'])
    angles=[v/journeys*360 for v in modes]
    check('pie_angles',sum(modes)==journeys and answer_has('P03','A1(6)',angles),{'journeys':journeys,'modes':modes},angles)
    short,long,exception=match(r'shorter routes (\d+)%, longer routes (\d+)%; School R on a longer route records (\d+)%',source['P03'])
    check('attendance_gap_exception',answer_has('P03','A1(7)',[short-long,exception]),[short,long,exception],short-long)
    cost,available=match(r'N\$(\d+) record/material cost with N\$(\d+) already',source['P03'])
    check('book_project_funding',answer_has('P03','A2(3)',[cost-available]),[cost,available],cost-available)
    before,after=match(r'periods show (\d+) then (\d+) visible',source['P04'])
    check('waste_difference',answer_has('P04','A1(8)',[after-before]),[before,after],after-before)
    population_items=json.loads((WS/'topics/7.1/learning-items/topic_7.1_items.json').read_text())['items']
    table=next(i['prompt'] for i in population_items if i['item_id'].startswith('ITEM-6136-7.1-026-'))
    atext,btext=table.split('A,',1)[1].split('; B,')
    avalues=[float(v) for v in re.findall(r'(?:male|female) (\d+)%',atext)]
    bvalues=[float(v) for v in re.findall(r'(?:male|female) (\d+)%',btext)]
    check('population_age_sex_totals',len(avalues)==len(bvalues)==6 and sum(avalues)==sum(bvalues)==100,
          {'A':avalues,'B':bvalues},[sum(avalues),sum(bvalues)])
    spec=json.loads((WS/'curriculum/performance-slot-specs.json').read_text())['slots']
    sectionrows=[]
    for code,i in packages.items():
        parts=re.findall(r'^(A[12]|B)\((\d+)\).*?\[(\d+)\]',i['prompt'],re.M)
        actual={(sec,int(n)):int(mark) for sec,n,mark in parts}
        planned=next(s for s in spec if s['slot']==i['item_id'])
        # Component order is retained separately within each section.
        expected={};counter=Counter()
        for p in planned['subparts']:
            counter[p['section']]+=1;expected[(p['section'],counter[p['section']])]=p['mark_tariff']
        secs=Counter()
        for (section,_),mark in actual.items():secs[section]+=mark
        check(code+'_authored_tariffs',len(actual)==len(parts) and actual==expected and secs['A1']+secs['A2']==35 and secs['B']==15,
            {'authored_parts':len(actual),'planned_parts':len(expected)},dict(secs))
        sectionrows.append({'slot':i['item_id'],'section_marks':dict(secs),'total':sum(secs.values()),'authority':'Parsed from authored question subparts, compared with plan.'})
    result={'checks':checks,'details':details,'packages':sectionrows,'method':'Parse actual authored stimuli, recompute, and compare canonical answers and actual question tariffs. No execution attributed to Claude.'}
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    if write_report:
        out=WS/'review/repairs/authored-numerical-audit.json';out.write_text(json.dumps(result,indent=2)+'\n')
    return sectionrows,checks

if __name__=='__main__':
    rows,checks=audit();print(f'{len(checks)} authored-data checks passed; {len(rows)} package tariff sets reconciled.')
