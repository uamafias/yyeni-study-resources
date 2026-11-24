"""Scoped runtime-prose/source comparison; extraction limitations stay explicit."""
import hashlib,re
from build_source import WB,load_source,read,dump

def words(text):
 text=re.sub(r'\$.*?\$',' ',text,flags=re.S)
 return re.findall(r"[a-z]+(?:'[a-z]+)?",text.lower())
def check():
 source={str(p.relative_to(WB)):p.read_text()for p in sorted((WB/'analysis/extracted').glob('*-questions.txt'))}
 source.update({str(p.relative_to(WB)):p.read_text()for p in sorted((WB/'analysis/extracted').glob('report-*-mathematics.txt'))})
 for item in read(WB/'analysis/cambridge-evidence.json')['items']:
  source['cambridge-evidence:'+item['item_id']]=item['verbatim_text']
 index={}
 for name,text in source.items():
  tokens=words(text)
  for i in range(len(tokens)-7):index.setdefault(tuple(tokens[i:i+8]),set()).add(name)
 texts={};count=0
 for group,c in load_source().all_choices():
  for params in c['parameters']:
   q=group.build(c['recipe_id'],c['branch_id'],params);count+=1
   fields=[('stem',q['stem']),('help-title',q['practice_help']['title'])]+[('help',x)for x in q['practice_help']['prompts']]
   for part in q['parts']:
    fields += [(part['local_part_id']+':prompt',part['prompt']),(part['local_part_id']+':answer',part['reference_answer'])]
    fields += [(part['local_part_id']+':step:'+key,value)for step in part['worked_steps']for key,value in step.items()]
   for field,text in fields:texts.setdefault(text,set()).add(c['selection_id']+':'+field)
 hits=[];claims=[]
 for text,locations in sorted(texts.items()):
  if re.search(r'examiners? (?:reward|require)|will (?:appear|come up)|guaranteed',text,re.I):claims.append({'text':text,'locations':sorted(locations)})
  tokens=words(text);runs=[];i=0
  while i<=len(tokens)-8:
   candidates=index.get(tuple(tokens[i:i+8]),set())
   if not candidates:i+=1;continue
   best=8;matches=[]
   for name in candidates:
    source_tokens=words(source[name]);length=8
    for start in range(len(source_tokens)-7):
     if source_tokens[start:start+8]!=tokens[i:i+8]:continue
     n=8
     while start+n<len(source_tokens)and i+n<len(tokens)and source_tokens[start+n]==tokens[i+n]:n+=1
     if n>length:length=n
    if length>best:best=length;matches=[name]
    elif length==best:matches.append(name)
   runs.append({'words':best,'run':' '.join(tokens[i:i+best]),'sources':sorted(matches)})
   i+=best
  if runs:hits.append({'text':text,'locations':sorted(locations),'runs':runs})
 result={'status':'scan-complete-manual-disposition-required'if hits or claims else'pass-scoped-prose-scan','instances':count,'distinct_learner_strings':len(texts),'source_text_records':len(source),'runs_8_or_more':hits,'assessment_claim_candidates':claims,'source_extraction_sha256':{k:hashlib.sha256(v.encode()).hexdigest()for k,v in source.items()},'limits':['English prose8-word scan with dollar-delimited mathematics excluded; no mathematics-copying or visual OCR certification.','Source input is existing accepted extraction,10NSSCASpapers/fivereportmathematicssections and selected Cambridge verbatim transcriptions; no claim to re-read rendered source PDFs.','Runtime feedback is app-owned; no model-generated feedback was produced or scanned.','Exact attributed exam reuse is owner-authorized; textbook originals remain internal. Any long common/necessary instruction still needs manual disposition.']}
 dump(WB/'checks/stage-e/wording.json',result);print({k:v for k,v in result.items()if k not in ('source_extraction_sha256','limits','runs_8_or_more')});print('HITS',hits)
if __name__=='__main__':check()
