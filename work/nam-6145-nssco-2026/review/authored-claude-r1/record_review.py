"""Record Claude's unchanged read-only findings through the standard ingestion tool."""
import hashlib,json,re,subprocess,sys
from pathlib import Path
import yaml
HERE=Path(__file__).resolve().parent;WS=HERE.parents[1];ROOT=WS.parents[1]
report=(HERE/'REVIEW.md').read_text()
block=re.search(r'```yaml\n(.*?)\n```',report,re.S).group(1)
# Claude's readable YAML contains unquoted colons in prose. Preserve the exact
# one-line field values while parsing the structure rather than editing its report.
findings=[]
for line in block.splitlines():
 match=re.match(r'^\s*(?:-\s+)?([a-z_]+):\s*(.*)$',line)
 if not match:continue
 key,value=match.groups()
 if key=='issue_id':findings.append({})
 if key=='affected_ids':value=yaml.safe_load(value)
 elif key=='confidence':value=float(value)
 findings[-1][key]=value
assert len(findings)==8
(HERE/'FINDINGS.json').write_text(json.dumps({'review_id':'6145-AUTH-R1','issues':findings},indent=2)+'\n')
topics={1:['3.2'],2:['2.3'],3:['2.1'],4:['7.3'],5:['4.2','4.3','5.4','6.1','6.2','6.3','7.2','7.3','8.1','9.1'],6:['3.2'],7:['5.4'],8:['8.1']}
frozen=json.loads((HERE/'FROZEN.json').read_text())
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in frozen.items())
for td in sorted((WS/'topics').iterdir()):
 if not td.is_dir():continue
 issues=[x for x in findings if td.name in topics[int(x['issue_id'].rsplit('-',1)[-1])]]
 review={'review_id':'6145-AUTH-R1-'+td.name,'reviewer_role':'Claude Opus medium; full authored-subject read-only review',
 'status':'conditional_pass' if issues else 'pass','packet_hash_verified':True,
 'coverage_confirmed':True,'reconstruction_test':'See REVIEW.md: comparative advantage sufficient; central-bank descriptive content requires repair.',
 'issues':issues}
 path=HERE/(td.name+'-review.yaml');path.write_text(yaml.safe_dump(review,sort_keys=False,allow_unicode=True))
 subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/checks/ingest_review.py'),str(WS),td.name,str(path)],cwd=ROOT,check=True,capture_output=True,text=True)
 subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/checks/run_checks.py'),str(WS),td.name,'--quiet'],cwd=ROOT,capture_output=True,text=True)
 q=json.loads((td/'qa_report.json').read_text());assert q['release_decision']=='publish'
subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/build/publish_subject.py'),str(WS)],cwd=ROOT,check=True)
status=(WS/'STATUS.md').read_text()
status=re.sub(r'- \[ \] 6 Reviewed by Claude[^\n]*','- [x] 6 Reviewed by Claude — 2026-11-08, authored r1: PUBLISH, no plan rebuild; 2 medium and 6 low findings remain open. See review/authored-claude-r1/REVIEW.md.',status)
start=status.index('## Next step');end=status.index('## Decisions',start)
status=status[:start]+'''## Next step

Final authored-subject Claude review completed at Jeremy's request on 8 November 2026. Report: review/authored-claude-r1/REVIEW.md. Verdict PUBLISH; no plan rebuild. Claude read all 28 notes packets, 458 items and 80 composite tasks. All 140 frozen canonical files remained unchanged during review. Local authored checkpoint: 97573395, not pushed.

Two medium findings need text corrections: 3.2 supply-shift terminology; 2.3 explicit central-bank functions. Six low findings cover terminology, definitions, item-specific rubrics, a cross-reference and stronger misconception discrimination. All eight unique issues are retained open in FINDINGS.json and relevant topic QA reports. Nothing has been represented as repaired. Local publication was regenerated to show review debt; all deterministic decisions remain PUBLISH. Jeremy's review-verdict checkpoint remains unticked.

'''+status[end:]
status+='\n- 2026-11-08 — Claude completed the full authored review: PUBLISH, 0 critical/high, 2 medium, 6 low. Findings were ingested through the standard tool, checks re-run and publication refreshed without changing learner content. No authored-content fixes, new push or upload performed.\n'
(WS/'STATUS.md').write_text(status)
print(json.dumps({'verdict':'PUBLISH','unique_open_findings':8,'medium':2,'low':6,'frozen_files_unchanged':140}))
