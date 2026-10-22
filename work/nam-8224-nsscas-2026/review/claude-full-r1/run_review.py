"""Snapshot-preflight and fresh Claude review; no commits or external writes."""
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[4]
WS=ROOT/'work/nam-8224-nsscas-2026'
RUN=WS/'review/claude-full-r1'
checks=[];metadata=[]
for p in sorted((WS/'topics').iterdir(),key=lambda p:tuple(map(int,p.name.split('.')))):
 with (RUN/f'check-{p.name}.log').open('w') as out:
  subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/checks/run_checks.py'),str(WS),p.name],cwd=ROOT,stdout=out,stderr=subprocess.STDOUT)
 q=json.loads((p/'qa_report.json').read_text())
 checks.append({'topic':p.name,'decision':q['release_decision'],'checks':q['deterministic_checks']})
 assert q['release_decision']=='publish' and not any(c['status']=='fail' for c in q['deterministic_checks'])
 wo=json.loads((p/'work_order.json').read_text());items=json.loads((p/'learning-items'/f'topic_{p.name}_items.json').read_text())['items'];by={i['item_id']:i for i in items};slots=wo['item_slots']+wo['performance_tasks'];assert len(by)==len(items)==len(slots)
 assert set(by)=={s['slot'] for s in slots}
 changed=[]
 for s in slots:
  i=by[s['slot']]
  for k in ['assessment_objectives','blooms_level','command_word','mark_tariff']:assert i[k]==s[k],(i['item_id'],k)
  assert i['objective_ids']==(s.get('objective_ids') or [s['objective_id']])
  if s.get('subtype') and i.get('subtype')!=s['subtype']:changed.append({'item_id':i['item_id'],'planned':s['subtype'],'actual':i.get('subtype')})
 metadata.append({'topic':p.name,'count':len(items),'metadata_mismatches':[],'subtype_changes':changed})
(RUN/'preflight-checks.json').write_text(json.dumps(checks,indent=1)+'\n')
(RUN/'metadata-completeness.json').write_text(json.dumps(metadata,indent=1)+'\n')
with (RUN/'copied-wording.log').open('w') as out:
 result=subprocess.run([sys.executable,str(ROOT/'operations/tools/check_copied_wording.py'),str(WS),str(ROOT/'Question Banks/Namibian Curricula/NSSCAS/Chemistry (8224)'),str(WS/'sources/reference-pack/NSSCASExaminersReport2025.pdf')],cwd=ROOT,stdout=out,stderr=subprocess.STDOUT)
print('Preflight complete:21 topics; copied-wording exit',result.returncode,flush=True)
with (RUN/'REVIEW-BRIEF.md').open() as inp,(RUN/'claude-stream.jsonl').open('w') as out,(RUN/'claude-stderr.log').open('w') as err:
 args=['claude','--safe-mode','--restricted','--strict-mcp-config','--tools','Read,Glob,Grep,Write,Edit','--allowedTools','Read','Glob','Grep','Write','Edit','--permission-mode','acceptEdits','--model','opus','--effort','medium','--print','--verbose','--output-format','stream-json']
 result=subprocess.run(args,cwd=ROOT,stdin=inp,stdout=out,stderr=err)
print('Claude exit',result.returncode,flush=True)
sys.exit(result.returncode)
