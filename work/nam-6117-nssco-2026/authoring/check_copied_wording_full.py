"""Full local corpus scan with reproducible paths and SHA-256, including duplicate copies."""
import json,hashlib,subprocess,sys
from pathlib import Path
W=Path(__file__).resolve().parents[1];R=W.parents[1]
records=json.loads((W/'assessment-evidence/assessment_evidence.json').read_text())['records']
prior={r['source_locator'].split('.pdf')[0]+'.pdf' for r in records if '.pdf' in r['source_locator']}
paths=set(prior)|{str(p.relative_to(R)) for p in (R/'Question Banks/Namibian Curricula/NSSCO (New)/Chemistry (6117)').rglob('*.pdf')}
for year in range(2020,2026):paths.update(str(p.relative_to(R)) for p in (R/'Question Banks/Namibian Examiner Reports/NSSCO (New) '/str(year)).glob('*.pdf'))
rows=[];groups={}
for name in sorted(paths):
 p=R/name;digest=hashlib.sha256(p.read_bytes()).hexdigest();groups.setdefault(digest,[]).append(name)
 rows.append({'path':name,'sha256':digest,'bytes':p.stat().st_size,'in_previous_24_path_scan':name in prior,'kind':'examiner_report' if 'Report' in name or 'NSSCO' in p.name else 'question_paper'})
for row in rows:row['byte_identical_other_paths']=[s for s in groups[row['sha256']] if s!=row['path']]
assert len(rows)==28 and len(groups)==24
assert all(r['byte_identical_other_paths'] for r in rows if not r['in_previous_24_path_scan'])
manifest={'scope':'All 22 PDFs in the Chemistry question-bank folder plus six annual examiner-report archive PDFs, 2020–2025. No separate mark schemes are held; reports supply marking guidance.','paths_scanned':28,'distinct_file_contents':24,'previous_scan_paths':sorted(prior),'explanation':'The prior 24-path scan selected the source_locator paths used by the evidence records. The four other archive paths for 2020–2023 are byte-identical copies of reports in the Chemistry folder. They were not dropped for relevance or results. All 28 paths are explicitly scanned now.','sources':rows}
(W/'review/copied-wording-sources.json').write_text(json.dumps(manifest,indent=2)+'\n')
lines=['# Exact copied-wording source manifest','','28 paths; 24 distinct file contents. Four archive copies are byte-identical to 2020–2023 reports in the Chemistry folder. The 2024/2025 reports reside only in the annual report archive. SHA-256 values and the previous 24-path list are in copied-wording-sources.json.','']
for r in rows:lines += ['- `'+r['path']+'`','  - SHA-256: `'+r['sha256']+'`'+(' — additional duplicate archive path' if not r['in_previous_24_path_scan'] else '')]
(W/'review/copied-wording-sources.md').write_text('\n'.join(lines)+'\n')
r=subprocess.run([sys.executable,str(R/'operations/tools/check_copied_wording.py'),str(W),*[str(R/n) for n in sorted(paths)]],cwd=R,capture_output=True,text=True)
print(r.stdout);print(r.stderr,file=sys.stderr);raise SystemExit(r.returncode)
