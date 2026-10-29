"""Independent source/numeric reconciliation for Step 3, not a learner PUBLISH gate."""
from pathlib import Path
from collections import Counter
import hashlib,json,re
import pdfplumber

W=Path(__file__).resolve().parents[1];ROOT=W.parents[1];E=W/'assessment-evidence';C=W/'curriculum'
def read(p):return json.loads(p.read_text())
def norm(s):return re.sub(r'\s+',' ',s).strip()
errors=[];results={}
def check(ok,message):
    if not ok:errors.append(message)

manifest=read(E/'extraction-manifest.json')
sources=read(W/'source-inventory.json')['files']
for s in sources:check(hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest()==s['sha256'],f"Hash drift: {s['path']}")
results['source_files_hash_checked']=len(sources)
rs=read(E/'assessment_evidence.json')['records'];byid={r['evidence_id']:r for r in rs}
check(len(byid)==len(rs),'Duplicate evidence IDs')
objectives=read(C/'mining-objectives.json')['objectives'];oids={o['objective_id'] for o in objectives}
for r in rs:
    check(bool(r['objective_ids']) and all(x in oids for x in r['objective_ids']),f"Bad objective mapping {r['evidence_id']}")
    check(bool(r['command_word']),f"Missing command {r['evidence_id']}")
    check(r['mark_tariff']>0,f"Invalid tariff {r['evidence_id']}")

# Independent PDF engine and raw bracket inventory: figures must agree without trusting the parser.
bracket_audits=[]
for s in manifest:
    if s['type']!='question_paper':continue
    with pdfplumber.open(ROOT/s['path']) as pdf:
        text='\n'.join(p.extract_text() or '' for p in pdf.pages)
    nums=[int(n) for n in re.findall(r'\[\s*(\d+)\s*\]',text)]
    parts=[r for r in rs if r['source_id']==s['source_id']]
    total=sum(r['mark_tariff'] for r in parts)
    expected=150 if s['paper_id']=='1' else (65 if s['paper_id']=='2' else 60)
    check(total==expected,f"Offered tariff drift {s['source_id']}: {total}")
    check(sum(nums)==2*total,f"PDF bracket sum (parts plus printed totals) differs: {s['source_id']}: {sum(nums)}")
    q=Counter()
    for r in parts:q[r['question_ref'][0]]+=r['mark_tariff']
    check(len(nums)==len(parts)+len(q),f"Bracket/part count differs {s['source_id']}")
    if s['paper_id']=='1':check(set(q.values())=={25} and len(q)==6,f"Paper 1 choice structure differs {s['source_id']}")
    bracket_audits.append({'source_id':s['source_id'],'pdfplumber_brackets':len(nums),'source_bracket_sum':sum(nums),
        'terminal_allocations':len(parts),'offered_marks':total,'printed_question_totals':len(q),'pass':sum(nums)==2*total and total==expected})
results['paper_reconciliation']=bracket_audits

for o in read(C/'exam-exposure.json')['objectives']:
    matched=[r for r in rs if o['objective_id'] in r['objective_ids']];e=o['evidence']
    expected={'question_parts_naming_it':len(matched),'distinct_series':len({r['exam_series'] for r in matched}),
        'max_mark_tariff':max([r['mark_tariff'] for r in matched] or [0]),
        'command_words_observed':dict(Counter(r['command_word'] for r in matched)),
        'total_associated_offered_marks':sum(r['mark_tariff'] for r in matched),
        'evidence_ids':[r['evidence_id'] for r in matched]}
    check(e==expected,f"Exposure drift {o['objective_id']}")
    mx=expected['max_mark_tariff'];n=expected['distinct_series']
    klass='unprobed_2020_2024' if not matched else ('probed_high' if mx>=5 or n>=3 else ('probed_low' if mx<=2 else 'probed_mid'))
    check(o['exam_exposure']==klass,f"Class drift {o['objective_id']}")
results['exposure_entries_recomputed']=len(read(C/'exam-exposure.json')['objectives'])

# Check all source outcome quotes against the source column on their named PDF page.
syll=read(C/'syllabus-facts.json')
with pdfplumber.open(ROOT/syll['source_document']) as pdf:
    for o in objectives:
        p=pdf.pages[o['source']['pdf_page']-1]
        quote=o['source']['verbatim']
        if o['objective_id'].startswith('X.'):text=p.extract_text() or ''
        else:
            sx=next(w['x0'] for w in p.extract_words() if w['text']=='Specific')
            text=p.crop((sx-1,65,775,550)).extract_text() or ''
        check(norm(quote) in norm(text),f"Objective source quote absent {o['objective_id']}")
results['syllabus_objective_quotes_checked']=len(objectives)

fs=read(E/'examiner-findings.json')['records'];fids={f['finding_block_id'] for f in fs}
for f in fs:
    pages=read(E/'extracted'/f"6137-{f['year']}-ER.json")
    source='\n'.join(p['text'] for p in pages if p['pdf_page'] in f['source_locator']['pdf_pages'])
    for line in f['text'].splitlines():
        if line.strip():check(norm(line) in norm(source),f"Report line absent from cited pages {f['finding_block_id']}: {line[:60]}")
    check(all(i in byid for i in f['evidence_ids']),f"Unresolvable finding link {f['finding_block_id']}")
results['report_blocks_source_checked']=len(fs)
for shape in read(C/'answer-shapes.json')['shapes']:
    check(all(i in byid for i in shape['evidence_ids']),f"Bad shape part {shape['shape_id']}")
    check(all(i in fids for i in shape['finding_ids']),f"Bad shape finding {shape['shape_id']}")
for m in read(C/'misconceptions.json')['misconceptions']:
    check(bool(m['objective_ids']) and all(i in oids for i in m['objective_ids']),f"Bad misconception outcome {m['misconception_id']}")
    check(all(i in fids for i in m['finding_ids']),f"Bad misconception finding {m['misconception_id']}")
for rule in read(C/'scope-scan.json')['rules']:
    for t in rule['must_catch']:check(bool(re.search(rule['pattern'],t,re.I)),f"Scope false negative {rule['limit_id']}")
    for t in rule['must_leave']:check(not re.search(rule['pattern'],t,re.I),f"Scope false positive {rule['limit_id']}")
results['scope_limits_checked']=len(read(C/'scope-scan.json')['rules'])
check(len(read(C/'command-word-verdicts.json')['verdicts'])==38,'Not all syllabus glossary rows have verdicts')
commands=read(C/'command-word-observations.json')['commands']
check(sum(c['count'] for c in commands)==len(rs),'Command count drift')
results.update(question_parts=len(rs),offered_marks=sum(r['mark_tariff'] for r in rs),failures=errors,
    status='PASS' if not errors else 'FAIL',
    limits=['Semantic mappings and classified findings were checked by the authoring miner only, not independently cross-reviewed.',
      'No standalone mark schemes. Only the explicitly curated examiner-backed answer shapes are populated as creditworthy_points.',
      'This is Step 3 source/numeric verification, not Step 5/6 topic checks or PUBLISH approval.'])
(E/'verification-6137.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
