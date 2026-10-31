"""Refresh the exact missing-credit demand list in GAPS.md from canonical evidence."""
from pathlib import Path
from collections import Counter
import json
W=Path(__file__).resolve().parents[1]
records=json.loads((W/'assessment-evidence/assessment_evidence.json').read_text())['records']
missing=sorted((r for r in records if not r['creditworthy_points']),key=lambda r:(int(r['paper_id']),r['year'],r['evidence_id']))
assert len(missing)==267,len(missing)
counts=Counter(r['paper_id'] for r in missing)
assert counts=={'1':41,'2':147,'3':79},counts
out=['## Exact demands still lacking entered marking evidence','',
     'Generated from records with an empty `creditworthy_points` array in `assessment_evidence.json`. Every demand is listed individually below; existing examiner commentary is not counted as a marking key or checked credit structure. This is the outstanding list before Step 4, not a claim that all remaining source tables are absent.','',
     '| Group | Demands |','|---|---:|','| 2020 Paper 1: no key, difficulty or answer evidence held | 40 |',
     '| 2024 Paper 1 Q9: officially compensated, excluded from usable exposure | 1 |',
     '| Paper 2: no entered checked credit structure | 147 |',
     '| Paper 3: no entered checked credit structure | 79 |','| **Total** | **267** |','',
     'The compensated 2024 MC item remains in this raw census list but does not need a replacement key and must not become a usable assessment item. The other 266 entries remain unkeyed or lack entered checked marking architecture. No calculate, define or explain primary-command demand is outstanding.','']
for paper,title in [('1','Paper 1 — unkeyed items and compensation'),('2','Paper 2 — structured demands'),('3','Paper 3 — practical-skills demands')]:
    out.extend([f'### {title}',''])
    for year in sorted({r['year'] for r in missing if r['paper_id']==paper}):
        rows=[r for r in missing if r['paper_id']==paper and r['year']==year]
        out.extend([f'#### {year} ({len(rows)} demands)','',
                    '| Demand ID | Question reference | Primary command | Marks |',
                    '|---|---|---|---:|'])
        for r in rows:
            command=r['command_word'] or ('MC option selection' if paper=='1' else 'Interrogative; no primary imperative')
            if r['evidence_id']=='6118-2024-P1-009':command+=' — compensated; excluded'
            out.append(f"| `{r['evidence_id']}` | {r['question_ref']} | {command} | {r['mark_tariff']} |")
        out.append('')
path=W/'assessment-evidence/GAPS.md';base=path.read_text().split('## Exact demands still lacking entered marking evidence',1)[0].rstrip()
path.write_text(base+'\n\n'+'\n'.join(out).rstrip()+'\n')
text=path.read_text();assert all(text.count('`'+r['evidence_id']+'`')==1 for r in missing)
print(f'Listed {len(missing)} unique demands: P1={counts["1"]}, P2={counts["2"]}, P3={counts["3"]}.')
