"""Build and qualify one authored topic, then record actual subject progress."""
import json
import subprocess
import sys
from pathlib import Path
WS=Path(__file__).resolve().parents[2];ROOT=WS.parents[1]
tid=sys.argv[1];td=WS/'topics'/tid
def run(script,*args,check=True):
    return subprocess.run([sys.executable,str(script),*map(str,args)],cwd=ROOT,check=check)
run(td/'build_authored.py')
run(ROOT/'standard/v0.2.0-draft/build/render_notes.py',WS,tid)
run(ROOT/'standard/v0.2.0-draft/checks/run_checks.py',WS,tid,'--quiet',check=False)
q=json.loads((td/'qa_report.json').read_text())
run(ROOT/'standard/v0.2.0-draft/checks/what_to_fix.py',WS,tid,check=False)
if q['release_decision']!='publish' or any(c['status']=='fail' for c in q['deterministic_checks']):
    raise SystemExit(1)
rows=[]
for p in sorted((WS/'topics').glob('*/qa_report.json'),key=lambda p:list(map(int,p.parent.name.split('.')))):
    report=json.loads(p.read_text())
    if report['release_decision']!='publish':continue
    note=json.loads((p.parent/'authoring_notes.json').read_text())
    rows.append({'topic':p.parent.name,**note['counts'],'deterministic_failures':0,
      'warning_checks':[c['check_id'] for c in report['deterministic_checks'] if c['status']=='warn'],
      'not_run_checks':[c['check_id'] for c in report['deterministic_checks'] if c['status']=='not_run']})
progress={'completed_topics':len(rows),'required_topics':28,'rows':rows,
 'totals':{k:sum(r[k] for r in rows) for k in ['claims','units','items','notes_words']},
 'note':'Deterministic success is not independent semantic review. Authoring remains in progress until all 28 topics are finished.'}
(WS/'authoring-progress.json').write_text(json.dumps(progress,indent=2)+'\n')
status=(WS/'STATUS.md').read_text()
import re
status=re.sub(r'- \[ \] 5 Topics authored:.*',f'- [ ] 5 Topics authored: {len(rows)} / 28 — current qualified topics and exact totals in authoring-progress.json.',status)
(WS/'STATUS.md').write_text(status)
print(json.dumps({'qualified_topics':len(rows),'totals':progress['totals']}))
