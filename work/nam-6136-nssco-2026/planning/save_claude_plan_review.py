"""Save Claude's returned plan review verbatim with auditable provenance."""
import hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
repo=P.parents[2]
raw=json.loads((P/'claude-plan-review-response.json').read_text())
if raw.get('is_error'):raise SystemExit(raw.get('result','Claude CLI reported an error'))
report=raw.get('result')
if not isinstance(report,str) or not report.strip():raise SystemExit('No final Claude report returned')
(P/'CLAUDE-PLAN-REVIEW.md').write_text(report)
manifest=json.loads((P/'claude-plan-review-input-manifest.json').read_text())
changed=[e['path'] for e in manifest['files'] if hashlib.sha256((repo/e['path']).read_bytes()).hexdigest()!=e['sha256']]
provenance={k:raw.get(k) for k in ['session_id','is_error','duration_ms','num_turns','modelUsage','permission_denials']}
provenance.update({'report_sha256':hashlib.sha256(report.encode()).hexdigest(),'submitted_files_changed_before_collection':changed,
 'scope':'Independent Step 4 plan review; not final resource review or plan approval','report_saved_verbatim':True})
(P/'claude-plan-review-provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(report)
