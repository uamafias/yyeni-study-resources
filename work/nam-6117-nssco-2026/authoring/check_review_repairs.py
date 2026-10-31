"""Regression checks for the reported key-pattern, learner-panel and template defects."""
from pathlib import Path
import json,re,collections,xml.etree.ElementTree as ET
W=Path(__file__).resolve().parents[1]
errors=[];sets=[];longest=0;tied=0;n=0
manifest=json.loads((W/'planning/visual-delivery-audit.json').read_text())
allowed={x['file'] for x in manifest['files'] if x['role']=='learner_stimulus'}
for t in range(1,13):
 T=W/f'topics/{t}';bank=json.loads((T/f'learning-items/topic_{t}_items.json').read_text())['items'];parts=json.loads((T/'authored_assessment_parts.json').read_text())['parts']
 for x in bank:
  if '(rounded where needed)' in x['canonical_answer']:errors.append(x['item_id']+' rounding placeholder')
  if re.search(r'(?:Yield|mass) fraction=[^.]*=\d+(?:\.\d+)?%',x['canonical_answer'],re.I):errors.append(x['item_id']+' fraction/percentage')
  if any(re.match(r'(?:Cause/reason|Given case and|Meaning or identity|Diagram/data interpretation)',s) for s in x['marking_guidance']):errors.append(x['item_id']+' template prefix')
  for link in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',x['prompt']):
   p=T/link
   if not p.exists() or str(p.relative_to(W)) not in allowed:errors.append(x['item_id']+' unsafe/missing learner asset '+link)
  if x['item_type']=='multiple_choice_set':
   pp=[p for p in parts if p['task_id']==x['item_id']];keys=''
   for p in pp:
    opts=re.findall(r'^([A-D])\. (.+)$',p['prompt'],re.M);key=p['canonical_answer'][0];keys+=key
    if len(opts)!=4 or not p['canonical_answer'].startswith(key+'. '+dict(opts)[key]):errors.append(x['item_id']+' inconsistent key')
    lengths=[len(v.split()) for k,v in opts];kl=lengths[ord(key)-65];longest+=kl>max(v for j,v in enumerate(lengths) if j!=ord(key)-65);tied+=kl==max(lengths);n+=1
   if collections.Counter(keys)!=collections.Counter('AAABBBCCCDDD'):errors.append(x['item_id']+' unbalanced')
   if any(all(keys[i]==keys[i%period] for i in range(len(keys))) for period in range(1,7)):errors.append(x['item_id']+' cyclic')
   sets.append({'item_id':x['item_id'],'keys':keys})
for f in allowed:
 text=' '.join(ET.parse(W/f).getroot().itertext())
 if '-learner.svg' in f and re.search(r'Answer (?:overlay|readings|curves)|Rf 0\.|0\.40 cm³|6\.40 cm³',text):errors.append(f+' keyed text leak')
report={'status':'pass' if not errors else 'fail','sets':sets,'questions':n,'correct_uniquely_longest':longest,'correct_longest_including_ties':tied,'errors':errors,'limits':'Checks key consistency, periodicity, visible answer text and explicit asset allowlist. Does not independently establish option science, distractor quality or visual correctness.'}
(W/'planning/review-repairs-check.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));raise SystemExit(bool(errors))
