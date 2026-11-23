"""Human-readable views of the repaired subject-local analysis records."""
from analysis_sources import A


def cell(value):
    if isinstance(value,list):value='; '.join(map(str,value))
    return str(value).replace('|','&#124;').replace('\n',' ')


def table(title, headings, rows, preface):
    return '\n'.join(['# '+title,'',preface,'','| '+' | '.join(headings)+' |',
                       '|'+'|'.join(['---']*len(headings))+'|',
                       *['| '+' | '.join(cell(v) for v in row)+' |' for row in rows]])+'\n'


def ref(r):
    return (f'{r["board"]} {r["year"]} P{r["paper"]} Q{r["question"]}'
            f'{r["part"] or ""}, printed {r["printed_page"]} / PDF {r["pdf_page"]}')


def render_records(objectives,demands,questions,families,dispositions,coverage,comparable):
    parts={p['part_id']:p for q in questions for p in q['parts']}
    rows=[]
    for f in families:
        members=[parts[k] for k in f['question_parts']]
        paper_refs=[ref(r) for p in members for r in p['examination_references']]
        marking=sorted({q['report_source']+' PDF '+str(n) for q in questions for n in q['marking_excerpt_pdf_pages']
                        if any(p['part_id'] in f['question_parts'] for p in q['parts'])})
        reasoning=(f['discriminating_decision']+'; inputs: '+', '.join(sorted({p['given_representation']['kind'] for p in members}))
                   +'; responses: '+', '.join(f['response_formats'])+'; connected questions: '+', '.join(f['connected_structure_ids']))
        rows.append([f['pattern_id']+' / '+', '.join(f['direct_demand_ids']),
                     f['title']+'; '+('; '.join(paper_refs) or 'No usable NSSCAS exemplar; see Cambridge links / syllabus record'),
                     marking or 'No matching full scheme established; marking remains to reconcile',reasoning,
                     'include; exact held exemplars: '+(', '.join(f['hold_ids']) or 'none'),
                     'Analysis group/module; branches: '+', '.join(f['structural_branches'])+'; '+f['discriminating_decision'],
                     f['evidence_status']+'; '+str(len(f['cambridge_item_ids']))+' Cambridge item(s). Calibration: '+str(f['grade_variation_bounds'])])
    (A/'selection-table.md').write_text(table('Repaired selections: NSSCAS Mathematics 8227',
        ['Selection ID / demand links','Pattern and paper locator','Marking/report locator',
         'Required reasoning, representation, connected parts','Disposition / hold ID',
         'Recipe grouping, distinguishing decision and evidence','Basis, rationale and limits'],rows,
        'Round 2 author analysis, 16 November 2026; owner Vitalis. Include retains a prescribed demand for re-review, not a recipe/work-order approval. '
        'Visual work is included under owner decision 6. Only defective exact exemplars are held. Broad groups retain narrower part references as internal related links unless demands/response match exactly.'))
    (A/'demand-registry.md').write_text(table('Specific-objective demands: Mathematics 8227',
        ['Demand','Learner action','Syllabus PDF / printed page','Source/evidence role'],
        [[d['demand_id'],d['learner_action'],str(d['source']['pdf_page'])+' / '+str(d['source']['printed_page']),
          'Author decomposition of syllabus; assess per part; see demand-dispositions.json'] for d in demands],
        '138 stable specific-objective demands; separate cross-cutting modelling and NSSCO prerequisite records do not inflate AS-objective coverage. '
        'D03 under circular measure is now specifically segment area; compound sector sums do not fill it. Stationary classification retains a separately visible inflexion facet.'))
    first=table('Demand-based coverage: Mathematics 8227',
        ['Objective','Usable NSSCAS parts','Comparable Cambridge items','Demands without usable NSSCAS parts'],
        [[r['objective_id'],len(r['observed_part_links']),len(r['cambridge_item_links']),r['unobserved_demand_ids']] for r in coverage],
        'Computed only from directly assessed part→demand links. Family membership, prerequisites and context do not create coverage. '
        'Held defective parts are shown separately and do not establish usable examination evidence. Links never certify the full range of a demand.')
    second=table('Demand dispositions', ['Demand','Status','Usable NSSCAS parts','Held parts','Cambridge items','Decision / reason'],
        [[r['demand_id'],r['status'],r['observed_part_links'],r['held_source_part_links'],r['cambridge_item_links'],
          r['disposition']+': '+r['reason']] for r in dispositions],
        'Every prescribed demand has exactly one evidence status. Inflexion remains an unobserved facet even though maxima/minima give the compound D02 an observed status.')
    (A/'coverage-matrix.md').write_text(first+'\n'+second)
    (A/'question-index.md').write_text(table('Question index: NSSCAS Mathematics 8227',
        ['Question','PDF pages','Connected structure','Parts and marks','Award-excerpt PDF pages','Dependency edges'],
        [[q['source_key'],q['pdf_pages'],q['pattern_summary'],
          [str(p['source_label'] or 'unlabelled')+': '+str(p['printed_marks']) for p in q['parts']],
          q['marking_excerpt_pdf_pages'] or 'none verified',
          [e['from_part']+' -> '+e['to_part']+' ('+e['type']+')' for e in q['dependencies']]] for q in questions],
        '119 connected questions and 250 assessed parts. Exact source hashes, directly assessed demand links, representation/assets and generated examination labels are in question-analysis.json.'))
    unobserved=[r for r in dispositions if not r['observed_part_links']]
    (A/'corpus-analysis.md').write_text('\n'.join([
        '# Corpus analysis: Namibia NSSCAS Mathematics 8227','',
        'Round 2 author repair, 16 November 2026. Owner Vitalis; independent re-review pending. No PLAN, work orders, recipes or runtime generators.','',
        'The controlling syllabus is NIED December 2020, Grade 12, first examination 2021. The ten 2021–2025 NSSCAS papers contain 119 connected questions, 250 labelled parts and 750 marks. '
        'Proof/final equivalence and missing full mark schemes remain explicit source limitations.','',
        '## What changed','',
        'Part-level direct demand links are authored independently of family membership. All 138 demands now have evidence statuses and reasoned dispositions; source holds do not delete the valid syllabus demand. '
        f'The {len(unobserved)} zero-usable-part demands reflect a stricter per-part annotation than the review’s eight examples. Segment D03 was clarified; inflexion is an additional unobserved facet of compound stationary-classification D02. '
        'See coverage-matrix.md and gap-demand-reconciliation.json for exact differences and subsequent Cambridge evidence.','',
        f'There are {len(unobserved)} demands without usable NSSCAS links and {len(families)} revised analysis groups/modules. Neither figure is a recipe count. '
        'Splits preserve different evidence (proof/range, reading/sketch, diagram coordinates/given vectors, motion/rates, standard integration/reversal/preprocessing). '
        'Connected function, progression and numerical structures remain connected. Every group has a discriminating decision, source links and grade-descriptor bounds.','',
        '## Marking, methods and sources','',
        'The original native-text scan located 24 Paper2 excerpts; round4 rendered-page analysis supersedes that limited scan with119question tables,821rows and250part reconciliations. See marking-conventions.json for two absent part breakdowns and a missing alternative-path row. '
        'R3 criterion transcriptions and reconciled part/path totals are in marking-conventions.json/.md; these are not a complete official memo bank. Method/answer-only restrictions and follow-through are question/criterion-specific. '
        'The 2023 Q6(d) graph-consistency condition does not literally say F.T.; it is a cue/graph dependency. Formal F.T. edges are separately sourced from the 2024 tables.','',
        'Source defects are in source-defects.json with independent symbolic/numeric recomputations. The inverse-sine question, degenerate discriminant proof and incompatible-domain curve exemplar remain held. '
        'Vitalis rejected the 2023 degree-mode award alternative. The polynomial-name typo and external division are disclosed; textbook cross-reference and convention conflicts are recorded.','',
        '## Representations and assessment conditions','',
        'Every part records given representation, required reading, response format, diagram parameters/assets and examination attribution. '
        'Eleven explicit sketch parts and two sketch-dependent parts are included under owner decision 6; source diagrams are rendered crops with source/page/box/hash provenance. '
        'The app change is announced for 17 November; this repair does not claim local runtime validation.','',
        'Assessment conditions are recorded per year/paper, including the formula-list reduction from 2023, precision/angle instructions and calculator/working wording. '
        'MF9 and supplied formulas do not extend syllabus scope. Theme 1 content can be directly assessed on Paper 2; do not equate theme with paper when composing future decks/tests.','',
        '## Textbook and Cambridge scope','',
        f'{len(comparable)} Cambridge items are separately labelled and scoped in cambridge-evidence.json/.md. Discovery leads are not source evidence or verified originals. '
        'The full local discovery corpus and unresolved searches are recorded; no claim to exhaustive future examination coverage is made.','',
        'Nineteen historical scoped samples remain separate from the R3 item inventory in textbook-inventory.json/.md. '
        'textbook-reading-r3.json exposes classified page evidence and remaining unclassified heading leads. '
        'OCR and native headings are discovery aids, not a complete verified item/figure census. '
        'Source-analysis completion, outstanding answer checks and independent classification remain open under textbook-completion-method.md; no sampling stop rule is claimed. '
        'The separate nsscas-cambridge-provenance.json register records source correspondences and draft internal attributions, not additional examination coverage.','',
        '## Next checkpoint','',
        'Focused cross-vendor check of the R3 repairs/registers, then complete and accept remaining textbook source analysis before step3 PLAN/contract. '
        'Author checks do not independently accept the repair. No source acquisition completeness, app activation or recipe release is inferred.'
    ])+'\n')
