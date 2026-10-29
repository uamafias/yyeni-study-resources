#!/usr/bin/env python3
"""Generate the human checkpoint brief from the verified 6137 facts."""
import json
from pathlib import Path

W=Path(__file__).resolve().parents[1]
ROOT=W.parents[1]

def main():
    f=json.loads((W/'curriculum/syllabus-facts.json').read_text())
    v=json.loads((W/'planning/syllabus-verification-6137.json').read_text())
    rotation=f['current_paper3_rotation']
    rotation_note=('The later circular dated '+rotation['circular_date']+' was confirmed by Vitalis on '+rotation['confirmation']['confirmed_on']+'. **2026 Paper 3: '+rotation['topics']['physical_geography']+' and '+rotation['topics']['human_geography']+'.** This is circular-sourced, not inferred from the old rotation. Full Paper 1/2 syllabus coverage remains in scope.' if rotation.get('topics') else 'The current-year Paper 3 notice is unconfirmed; do not infer it from the historical cycle.')
    lines=['# 6137 NSSCO Geography - syllabus brief','',
      'Owner: Vitalis P Haupindi. Target: the current learners’ 2026 examination. Step 2 completed 29 October 2026; human table confirmation pending.','',
      f"Source: NIED {f['edition']['value']}, first examination {f['first_examination_year']['value']}; `{f['source_document']}`. PDF page numbers below are one-based; printed page numbers are the footers.",
      '', '## Assessment objectives and marks', '',
      'AO names: printed pages 26-27 / PDF pages 29-30. The grid: **printed page 28 / PDF page 31**. Per-paper cells below are **marks**, not percentages. A dash in the printed grid is represented by 0.', '',
      '| AO | Name | Overall weight | P1 marks | P2 marks | P3 marks |',
      '|---|---|---:|---:|---:|---:|']
    for a in f['assessment_objectives']:
        c=a['code'];m=f['ao_weights']['per_component'];lines.append(f"| {c} | {a['name']} | {a['qualification_weight_percent']}% | {m['1'][c]} | {m['2'][c]} | {m['3'][c]} |")
    lines+=['','## Papers','', '**Printed page 27 / PDF page 30**, with marks and weightings confirmed by the grid on PDF page 31. All three papers are compulsory; grades A*-G.', '',
      '| Paper | Duration | Marks | Weight | Structure |','|---|---|---:|---:|---|']
    descriptions={'1':'Six resource-based questions; answer three, one from each thematic section.','2':'Answer all questions; geographical skills, including a 1:50,000 SADC topographical map with full key.','3':'Answer both geographical-investigation questions: one physical and one human.'}
    for p in f['papers']:lines.append(f"| {p['paper']} | {p['duration']} | {p['marks']} | {p['weight_percent']:g}% | {descriptions[p['paper']]} |")
    lines+=['',f"Totals reconcile: **{sum(p['marks'] for p in f['papers'])} marks**, 100% paper weighting and 100% AO weighting.",
      '', '## Scope and commands', '',
      f"The syllabus has **{len(f['themes'])} themes and {len(f['content_outline'])} numbered topics**: physical geography; economic activities/resources; population/settlements; and integrated research/map skills (PDF pages 7-28).",
      '', f"The teaching/assessment glossary has **{len(f['command_words'])} printed rows** (printed 35-37 / PDF 38-40). It mixes commands, question phrases and nouns such as Factor, Feature and Pattern. Preserve all rows; determine actual prompt-openers, variants and tariffs from the papers at step 3 rather than authorising all glossary entries as commands.",
      '', 'Named case studies are non-prescriptive (PDF 7). Mapwork answers must use map evidence; gradient inputs need matching units; cross-sections are interpreted, not constructed (PDF 33-34). Photographs require simple descriptions in the specified Paper 2 context. Research skills must be integrated with the three content themes (PDF 28). Paper 3 is a written investigation paper, not an assumed coursework option (PDF 30).',
      '', '## Remaining source limits and next checkpoint', '',
      '**The printed syllabus rotation covers only 2020-2024** (printed 34 / PDF 37). '+rotation_note,
      '', 'Vitalis accepted proceeding with the available sources. Full map resources are verified for 2021-2024; the 2020 Amersfoort extract, standalone marking schemes and 2025 materials remain missing. Use 2021-2024 for fully verifiable map-dependent analysis; mark any 2020 map-dependent answer evidence as unavailable.',
      '', f"Verification: **{v['source_quotes_checked']} source-quote checks**, no quote failures; grid row/column sums and stated weights reconcile. Full source facts and the topic outline are in `work/nam-6137-nssco-2026/curriculum/syllabus-facts.json`; verification and rendered source pages are under that workspace’s `planning/` folder.",
      '', 'Next: Vitalis checks the two tables against PDF pages 29-31. TEAM-PLAYBOOK.md section 4, step 2 requires this confirmation before step 3 corpus analysis. No plan, notes or flashcards have been authored.']
    out=ROOT/'operations/analysis/6137-nssco-geography-syllabus-brief.md';out.parent.mkdir(exist_ok=True);out.write_text('\n'.join(lines)+'\n')
    print(out)

if __name__=='__main__':main()
