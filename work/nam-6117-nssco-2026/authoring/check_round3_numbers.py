"""Independent arithmetic for the 26 revised numerical stimuli."""
import json,math
from pathlib import Path
W=Path(__file__).resolve().parents[1]
# Values recomputed from prompt data; expected values transcribed from answers.
cases={
'1-001':((34-7)-3,24),'1-002':((48-6)/(18-4),3),'1-003':((18.8+19+19.2)/3-.2,18.8),'1-004':((30-6)/30*100,80),
'1-005':(.020*(200-50)/100,.030),'1-006':(60/5+4,16),'1-007':(300*.002-.10,.50),'1-008':(.008/(200/1000),.040),
'1-009':((20-5)/3,5),'1-010':((10-2)*2,16),'1-011':((51-15)/3,12),'1-012':(45/(35-20),3),
'1-032':(175/1000+.100,.275),'1-033':(.00216/3,.00072),'1-034':(2.4e3+1.2e3,3600),'1-038':(25.50-.50+273.15,298.15),'1-039':(310.15-273.15-12,25),
'1-073':((4.6-1)/(7-1),.60),'1-074':(.40*(8.5-1)+1,4),'4-017':((.300-.050)*24,6),'4-033':((10-2)/10*100,80),
'4-034':((6-1.24)/5.60*100,85),'4-035':((11-2)/.75,12),'4-037':((15-3)/15*100,80),'4-038':(4.25/(7.5-2.5)*100,85),'4-039':((30-10)*.90,18)}
for key,(actual,expected) in cases.items():assert math.isclose(actual,expected,rel_tol=1e-10,abs_tol=1e-10),key
# Four additional Ar-only edits: formula answers are unchanged and recomputed here.
items=json.loads((W/'topics/4/learning-items/topic_4_items.json').read_text())['items']
ar_cases={'025':(180/(12+2+16),6,'C6H12O6'),'026':(56/(12+2),4,'C4H8'),'027':(92/(14+32),2,'N2O4'),'028':(78/(12+1),6,'C6H6')}
for number,(factor,expected,formula) in ar_cases.items():
 assert factor==expected
 item=next(x for x in items if x['item_id'].split('-')[3]==number)
 assert formula in item['canonical_answer'],item['item_id']
report={'status':'pass','additional_Ar_only_edits':{k:{'formula_multiplier':a,'unchanged_formula':c} for k,(a,b,c) in ar_cases.items()},'cases':{k:{'recomputed':a,'answer':b} for k,(a,b) in cases.items()},'limitations':'Arithmetic for revised prompts; does not certify the cognitive-demand labels.'}
(W/'planning/round3-numerical-check.json').write_text(json.dumps(report,indent=2)+'\n');print('26 revised numerical answers plus 4 Ar-only formula checks verified')
