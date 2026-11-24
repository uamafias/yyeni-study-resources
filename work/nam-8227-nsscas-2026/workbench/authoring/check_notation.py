"""Extract actual generated learner text, excluding provenance/source notes."""
import re,json
from build_source import load_source,WB,dump
m=load_source();expressions=set();count=0
for group,c in m.all_choices():
 for params in c['parameters']:
  q=group.build(c['recipe_id'],c['branch_id'],params);count+=1
  texts=[q['stem'],q['practice_help']['title'],*q['practice_help']['prompts']]
  for p in q['parts']:
   texts += [p['prompt'],p['reference_answer']]
   texts += [v for s in p['worked_steps']for v in s.values()]
  for text in texts:
   assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',text)
   assert len(re.findall(r'(?<!\\)\$',text))%2==0,repr(text)
   expressions.update(re.findall(r'(?<!\\)\$(.+?)(?<!\\)\$',text,flags=re.S))
dump(WB/'authoring/math-expressions.json',sorted(expressions))
print(json.dumps({'instances':count,'unique_expressions':len(expressions)}))
