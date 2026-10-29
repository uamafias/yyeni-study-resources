"""Build Geography mining artefacts from source extracts and explicit miner decisions.

No learner notes/cards and no standard/ files are written. Run from repository root.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib, json, re
import pdfplumber
from semantic_mappings_6137 import mapped, REF_NOTES

W=Path(__file__).resolve().parents[1]
ROOT=W.parents[1]
E=W/'assessment-evidence'
C=W/'curriculum'
def read(p):return json.loads(p.read_text())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def norm(s):return re.sub(r'\s+',' ',s).strip()

def catalogue():
    """Read the actual right-hand specific-objective column, not general objectives."""
    objs=[];topic=None;ns=Counter()
    with pdfplumber.open(ROOT/read(C/'syllabus-facts.json')['source_document']) as pdf:
        for pn in range(8,29):
            pg=pdf.pages[pn-1];words=pg.extract_words()
            sx=next(w['x0'] for w in words if w['text']=='Specific')
            heads=[(w['top'],w['text']) for w in words if w['x0']<210 and re.fullmatch(r'[1-4]\.[1-7]',w['text'])]
            buf=[];active=False;bt=None
            def flush():
                if buf:
                    ns[bt]+=1
                    objs.append({'objective_id':f'{bt}.{ns[bt]:02d}','topic_id':bt,
                        'text':' '.join(buf),'provenance':'syllabus',
                        'source':{'path':read(C/'syllabus-facts.json')['source_document'],
                            'pdf_page':pn,'printed_page':pn-3,
                            'extraction':'pdfplumber specific-objective column',
                            'verbatim':' '.join(buf)}})
            for l in pg.crop((sx-1,65,775,550)).extract_text_lines():
                line=l['text'].strip();hs=[t for y,t in heads if y<=l['top']+2]
                if hs:topic=hs[-1]
                if line.startswith(('\uf0b7','•')):
                    flush();bt=topic;buf=[line[1:].strip()];active=True
                elif re.match(r'Case stud|Practical activity',line,re.I):flush();buf=[];active=False
                elif active and not re.match(r'^[abc]\)',line):buf.append(line)
            flush()
    # Cross-cutting aims cover actual demands not reducible to a specific content bullet.
    # Do not file coastal opportunities under beach formation, or coastal climate impacts under wildlife.
    for oid,topic,label,quote in [
        ('X.01','1.5','Opportunities and limitations of physical environments',
         'an appreciation of the potentialities and limitations of the physical environment for human activities;'),
        ('X.02','1.6','Environmental enhancement/degradation including human climate impacts',
         'an appreciation of how human use and abuse of the environment can lead to various forms of environmental enhancement and degradation;')]:
        objs.append({'objective_id':oid,'topic_id':topic,'text':label,'provenance':'syllabus aim; topic assignment is miner judgement',
           'source':{'path':read(C/'syllabus-facts.json')['source_document'],'pdf_page':5,'printed_page':2,
                     'extraction':'whole-page aim','verbatim':quote}})
    dump(C/'mining-objectives.json',{'purpose':'Source specific-objective bullets plus two explicit cross-cutting aims for semantic mining; planner must carry IDs forward or supply an explicit crosswalk. Not a card plan.',
          'resolution':'One source bullet, including nested examples, per numeric ID. X.01/X.02 are broader source aims, deliberately not evidence that any one nested content bullet was examined. Practical methods are mapped to the integrated 4.1 outcomes; practical-context requirements remain in the full syllabus.',
          'objectives':objs})
    return {o['objective_id']:o for o in objs}

# Human reading of the report blocks: explicit category lists, not keyword-to-objective mapping.
# Omission is used for a reported missing element/knowledge; mere performance remarks are excluded.
COMMAND=set(map(int,'''4 5 6 12 14 17 19 23 37 40 41 43 54 55 61 65 68 71 72 75 78 79 80 86 89 90 97 102 103 104
107 109 110 113 116 120 122 124 131 132 142 144 147 149 150 161 162 164 166 170 176 184 192 197 198 200 203 204 208 209
214 215 219 222 224 227 230 232 233 235 237 240 242 244 245 247 249 250 252 253 256 258 259 261 262 263 264 267 268 270 271 272 273 274 275 277 278 280 281 282 284 285 286 290 294 295 296 297 298 299 300 301 302 304 305 306 307 308 309 311 312
318 320 321 322 327 328 329 330 331 332 333 334 336 337 338 339 340 341 342 343 344 345 347 348 350 351 352 354 355 356 357 358 359 363 364 365 367 368 369 371 372 375 376 377 378 379 384 385 388 389 390 392 393 394 395 396 397 398 399 400 402 403 404 405 408 409 411 412 414 415 417 419 420 422 423 424 425 426 427 428 430 431 432 433 434 435
439 441 442 443 446 449 450 452 453 454 455 456 457 459 460 461 462 463 464 466 467 468 469 470 471 473 474 475 477 478 480 481 483 484 485 486 488 489 490 491 492 494 495 496 499 500 501 502 504 505 506 507 508 510 511 512 513 514 515 516 517 518 519 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546'''.split()))
SHALLOW=set(map(int,'''11 18 20 28 29 34 36 42 77 83 91 92 94 96 98 100 112 115 118 126 130 134 135 136 137 138 143 156 157 158 175 190 195 199 201 207 213 216 217 220 221 223 225 228 229 231 236 241 243 246 248 260 266 269 283 288 289 291 293 297 298 299 301 306 311 316 317 320 329 334 337 341 343 344 345 347 348 349 350 351 352 355 358 359 370 378 391 407 408 413 417 418 421 422 431 432 434 435 439 440 442 443 446 447 448 450 454 457 460 462 464 468 469 471 475 478 480 481 482 484 486 492 493 494 495 496 497 502 508 511 514 518 519 522 523 524 526 528 529 530 531 533 536 538 540 541 543 544 545 546'''.split()))
CONCEPT=set(map(int,'''8 21 26 35 59 73 115 122 127 151 157 158 175 212 216 218 223 230 238 239 242 243 246 248 249 260 266 269 275 277 278 279 289 291 312 315 316 317 318 326 330 335 337 341 345 346 351 355 358 363 366 378 384 385 388 389 398 402 403 404 405 409 416 418 421 428 429 437 438 440 442 444 445 447 448 451 457 465 468 472 474 478 480 481 484 488 491 493 497 498 501 502 503 509 510 516 517 519 520 522 524 529 530 535 538 543 544'''.split()))
PERFORMANCE=set(map(int,'''3 9 16 24 27 30 31 32 38 39 44 49 52 56 57 58 60 62 63 66 69 70 74 76 82 84 85 88 93 95 99 101 106 108 111 114 117 119 121 123 125 128 129 133 139 140 141 145 146 148 153 154 155 159 160 163 165 167 168 169 171 172 173 174 177 178 179 180 181 182 183 186 187 188 189 191 193 194 196 202 205 206 211 226 234 254 255 257 265 276 279 287 292 303 310 313 314 319 323 353 360 361 362 373 374 380 381 382 383 386 387 401 406 410 416 420 429 430 433 436 445 448 449 451 458 459 465 467 472 473 479 482 485 487 489 503 504 507 508 510 513 515 517 520 521 523 525 527 529 530 532 534 535 537 539 541 542 543 544'''.split()))

def report_crosswalk(b):
    """Known layout/source-numbering fixes verified against the actual question demand."""
    n=int(b['finding_block_id'].split('-')[-1]); ref=b['question_ref']
    replacements={}
    if 139<=n<=144:ref='5'+ref[1:]
    if 238<=n<=244:
        ref='5'+ref[1:]
        if n==239:ref='5(a)(ii)(bb)' # both outcomes share one tariff in QP
        if n==243:ref='5(b)(iii)'
    if 245<=n<=250:ref='6'+ref[1:]
    if 252<=n<=258:ref='1(a)'+ref
    if 259<=n<=264:ref='1'+ref
    if n==331:ref='3(a)(i)'
    if 339<=n<=345:ref='4'+ref[1:]
    if 346<=n<=352:ref='5'+ref[1:]
    if 353<=n<=359:ref='6'+ref[1:]
    if 380<=n<=390:ref='2'+ref[1:]
    if 391<=n<=393:ref='3'+ref[1:]
    if 394<=n<=398:ref='4'+ref[1:]
    if 399<=n<=405:ref='5'+ref[1:]
    if 406<=n<=409:ref='6'+ref[1:]
    if n==301:ref='2(a)(i)#2'
    if n==302:ref='2(a)(ii)'
    if n==305:ref='2(b)(iii)(bb)'
    if n==494:ref='3(a)(ii)'
    if n==495:ref='3(a)(iii)'
    if n==506:ref='5(a)(iv)'
    return ref

def findings(records):
    blocks=read(E/'report-blocks.json');result=[]
    for b in blocks:
        n=int(b['finding_block_id'].split('-')[-1]);ref=report_crosswalk(b)
        if n==101:ref='2(b)' # report explicitly covers all three subparts in one block
        matches=[r for r in records if r['year']==b['year'] and r['paper_id']==b['paper_id'] and ref
             and (r['question_ref']==ref or r['question_ref'].startswith(ref+'(') or r['question_ref'].startswith(ref+'#'))]
        cats=[]
        if n in COMMAND:cats.append('command-word miss')
        if n in SHALLOW:cats.append('shallow development')
        if n in CONCEPT:cats.append('misconception')
        if not cats and n not in PERFORMANCE:cats=['omission']
        # Original narrative and answer lists remain audit evidence, not modelled learner answers.
        item={**b,'matched_question_ref':ref,'evidence_ids':[r['evidence_id'] for r in matches],
          'objective_ids':sorted({oid for r in matches for oid in r['objective_ids']}),
          'source_locator':{'path':next(s['path'] for s in read(E/'extraction-manifest.json') if s['year']==b['year'] and s['type']=='annual_examiner_report'),
                            'pdf_pages':b['pdf_pages']},
          'classifications':cats,'classification_method':'Miner block-level judgement; multiple categories may apply. Performance-only/answer-list blocks have no error category. This is not a claim that every quoted wrong answer is factually false.',
          'mapping_method':'Question-reference crosswalk checked against meaning and source page; not text-token matching.',
          'scope':'question-specific' if matches else 'paper-level or unlinked block'}
        if ref!=b['question_ref']:item['crosswalk_note']='Report extraction/source reference differs from QP; attached by actual task, with original reference retained.'
        result.append(item)
    dump(E/'examiner-findings.json',{'unit':'Complete source block; classification applies to the substantive candidate-performance comments, not its expected-answer lists.',
       'warning':'Wrong answers can be true statements that do not answer this particular task. A conceptual misconception card requires separate curation.',
       'records':result})
    return result

# Assessment operation normalization is distinct from semantic objective mapping.
# The literal stem remains available. Supporting instructions such as Study/Use are not
# credited operations when they introduce a substantive command.
VERBS=r'describe and explain|describe and suggest|name and describe|identify and describe|name and explain|measure and calculate|find and calculate|determine|distinguish|differentiate|calculate|compare|contrast|define|demonstrate|describe|devise|design|discuss|draw|estimate|explain|identify|insert|label|list|locate|mark|match|measure|name|outline|plot|rank|select|shade|show|state|support|suggest|tick|write|complete|give'
INHERITED={
 '6137-2020-P1-3(a)(ii)':'describe',
 '6137-2020-P2-1(b)(iii)':'what','6137-2020-P2-6(a)':'how','6137-2020-P2-6(b)':'how',
 '6137-2020-P3-1(c)(ii)':'how','6137-2020-P3-2(a)(iii)':'how','6137-2020-P3-2(b)(ii)':'add',
 '6137-2021-P2-2(a)':'name','6137-2021-P2-3(a)':'which','6137-2021-P2-6(b)(ii)':'which',
 '6137-2021-P3-1(d)(iii)':'what','6137-2021-P3-1(e)(ii)':'describe',
 '6137-2022-P3-2(a)(i)#2':'name and describe','6137-2022-P3-2(b)(iv)':'do you think','6137-2022-P3-2(c)(iv)':'which',
 '6137-2023-P2-3(a)':'state','6137-2023-P3-1(b)(i)':'which','6137-2023-P3-1(e)':'explain',
 '6137-2023-P3-1(d)(ii)':'do the results support','6137-2023-P3-1(f)(iii)':'what',
 '6137-2023-P3-2(d)(iii)':'do you agree','6137-2023-P3-2(e)(ii)':'do you accept or reject',
 '6137-2024-P2-2(b)(i)':'add','6137-2024-P2-7(b)(i)':'which',
 '6137-2024-P3-1(b)(iii)':'explain','6137-2024-P3-1(d)(i)':'what','6137-2024-P3-1(d)(iii)':'what',
 '6137-2024-P3-2(d)(iv)':'what','6137-2024-P3-2(e)(iv)':'what',
 '6137-2020-P1-1(a)(ii)#2':'give','6137-2020-P1-5(a)(ii)#2':'name','6137-2020-P1-5(a)(ii)#3':'name','6137-2020-P1-5(a)(ii)#4':'name',
 '6137-2020-P1-6(a)(ii)#2':'name','6137-2020-P1-6(a)(ii)#3':'name','6137-2021-P1-1(a)(iii)(aa)':'name','6137-2021-P1-1(a)(iii)(bb)':'name','6137-2021-P1-1(a)(iii)(cc)':'name',
 '6137-2021-P1-2(a)(ii)#2':'what','6137-2022-P1-5(a)(ii)(bb)':'name',
 '6137-2024-P3-1(a)(ii)#2':'explain','6137-2024-P3-1(b)(iii)#2':'explain',
 '6137-2020-P3-2(b)(i)':'write',
}
def command(r):
    if r['evidence_id'] in INHERITED:return INHERITED[r['evidence_id']]
    t=norm(r['source_excerpt']).lower()
    # Primary assessed task, not labels in figures or background.
    if re.search(r'how far do you agree',t):return 'how far do you agree'
    if t.startswith('discuss how far'):return 'discuss how far you agree'
    # Subordinate response slots inherit the overarching instruction from the QP.
    y,p,ref=r['year'],r['paper_id'],r['question_ref']
    if p=='2' and y in (2022,2023) and ref.startswith('1(a)'):return 'identify'
    if y==2021 and p=='2' and ref.startswith('3(b)'):return 'describe'
    if y==2022 and p=='2' and ref.startswith('4(b)'):return 'describe'
    if y==2020 and p=='2' and ref.startswith('2(b)'):return 'suggest'
    if y==2023 and p=='2' and ref.startswith('2(a)'):return 'state'
    if y==2023 and p=='2' and ref.startswith('2(b)'):return 'what'
    if y==2023 and p=='2' and ref.startswith('5(c)'):return 'explain'
    if y==2022 and p=='3' and ref.startswith('1(b)(iii)'):return 'label'
    if y==2022 and p=='3' and ref.startswith('2(b)(iii)'):return 'complete'
    # Imperative following source carrier or contextual sentence. Avoid own studied etc.
    m=re.search(r'\b('+VERBS+r')\b',t)
    if m:
        v=m[1]
        # Study commands occur only before the tested verb; 'name of...' is an answer label.
        return v
    for v in ('what','which','how','where','why'):
        if re.search(r'\b'+v+r'\b',t):return v
    raise ValueError(('Unresolved command',r['evidence_id'],t))

CONTEXT={2020:{'1':'1.3','2':'3.3'},2021:{'1':'1.5','2':'3.3'},2022:{'1':'1.6','2':'2.3'},2023:{'1':'1.3','2':'3.3'},2024:{'1':'1.5','2':'3.3'}}
def primary_topic(r,catalog):
    if r['paper_id']=='3':return CONTEXT[r['year']][r['question_ref'][0]]
    if r['paper_id']=='2' and r['question_ref'].startswith('1('):return '4.2'
    return catalog[r['objective_ids'][0]]['topic_id']

def build():
    cat=catalogue();records=read(E/'parsed-question-parts.json')['records']
    for r in records:
        ids,selector=mapped(r)
        assert all(i in cat for i in ids),(r['evidence_id'],ids)
        r.update(objective_ids=ids,mapping_method='Miner semantic reading of the question demand and source specific-objective bullet; explicit reference selector '+selector+' in planning/semantic_mappings_6137.py. No token-matched first pass.',
            mapping_confidence='source-bullet resolution; examples within compound bullets are not separately measured',
            command_word=command(r),creditworthy_points=[],examiner_findings=[],common_errors=[],strong_response_features=[],notes=[])
        r['primary_context_topic']=primary_topic(r,cat)
        r['context_type']='topographic_map' if r['paper_id']=='2' and r['question_ref'].startswith('1(') else ('geographical_investigation' if r['paper_id']=='3' else 'knowledge_and_resource_application')
        v=r['command_word'];t=norm(r['source_excerpt']).lower()
        ao='A'
        if re.search(r'fig\.|photograph|table |graph|map|data|evidence',t):ao='B'
        if r['context_type']=='geographical_investigation' and any(x.startswith('4.1.') for x in ids):ao='D'
        if v in ('how far do you agree','discuss how far you agree') or any(x=='4.1.08' for x in ids):ao='C'
        r['ao_focus']=[ao];r['ao_provenance']='judgement: primary focus only, not an official per-part split; report labels appended separately where available'
        r['parse_status']='tariff and reference audited; shared marked units retained once'
        if r['evidence_id'] in REF_NOTES:r['notes'].append(REF_NOTES[r['evidence_id']])
        if r['year']==2020 and r['context_type']=='topographic_map':r['notes'].append('2020 Amersfoort insert absent: demand analysed, map-dependent answer not independently verified.')
    fs=findings(records)
    byid={r['evidence_id']:r for r in records}
    for f in fs:
        for rid in f['evidence_ids']:
            r=byid[rid];r['examiner_findings'].append(f['finding_block_id'])
            if f['classifications']:r['common_errors'].append({'finding_id':f['finding_block_id'],'classifications':f['classifications']})
            heading=re.split(r'comments?\s+on|general comments?',f['text'],flags=re.I)[0][:350]
            labels=sorted(set(re.findall(r'\bAO\s*([ABCD])\b',heading)))
            if labels:
                r.setdefault('report_ao_labels',[]).append({'finding_id':f['finding_block_id'],'labels':labels})
    for r in records:
        if r.get('report_ao_labels'):
            r['ao_focus']=sorted({a for s in r['report_ao_labels'] for a in s['labels']})
            r['ao_provenance']='corpus: labels printed in linked examiner-report question heading; not an inferred mark allocation'
        if r['evidence_id'] in ('6137-2022-P1-5(a)(ii)(bb)','6137-2022-P3-2(b)(iii)(bb)'):
            r['canonical_question_ref']=r['question_ref'].replace('(bb)','')
            pages=read(E/'extracted'/f"{r['source_id']}.json")
            # Preserve the complete shared stem, including its unmarked (aa) clause.
            page=next(p for p in pages if p['pdf_page']==r['source_locator']['pdf_pages'][0])
            a=page['text'].find('(ii)' if r['paper_id']=='1' else '(iii)')
            z=page['text'].find('[2]',a)+3
            r['shared_allocation_source_excerpt']=page['text'][a:z]
    # Explicit answer shapes/curated misconceptions are stored in a separate human decision file.
    decisions=read(E/'curated-decisions.json')
    for d in decisions['answer_shapes']:
        for rid in d['evidence_ids']:
            byid[rid]['creditworthy_points'].append({'shape_id':d['shape_id'],'shape':d['credit_shape'],'provenance':'corpus: examiner report, not standalone mark scheme','sources':d['finding_ids']})
            byid[rid]['strong_response_features'].append(d['credit_shape'])
    dump(E/'assessment_evidence.json',{'syllabus_code':'6137','years':list(range(2020,2025)),
        'unit':'One terminal bracketed mark allocation; lettered sub-responses with one shared allocation are not double-counted. #2 etc distinguish separately marked occurrences under the same printed reference.',
        'ao_note':'Official route and per-paper AO weights remain in syllabus-facts.json. Inferred primary AO labels are not a mark allocation and must not be used to replace that grid.',
        'records':records})
    (E/'command-review.txt').write_text('\n'.join(r['evidence_id']+' '+r['command_word']+' :: '+norm(r['source_excerpt'])[:140] for r in records)+'\n')
    dump(C/'answer-shapes.json',{'source_kind':'examiner_report','standalone_mark_schemes_available':False,
       'rules':'These are tariff-specific observed credit shapes, not a universal one-point-per-mark rule. Use the live task wording and named source, not the command word alone.',
       'shapes':decisions['answer_shapes']})
    fby={f['finding_block_id']:f for f in fs}
    misconceptions=[]
    for m in decisions['misconceptions']:
        misconceptions.append({**m,'objective_ids':sorted({o for fid in m['finding_ids'] for o in fby[fid]['objective_ids']}),
               'source_locators':[fby[fid]['source_locator'] for fid in m['finding_ids']]})
    dump(C/'misconceptions.json',{'curation':'Conceptual confusions only. Exam habits, missing units, unsupported hypotheses and contextually irrelevant true facts stay in examiner-findings.json.',
       'misconceptions':misconceptions})
    exposure=[]
    for oid,o in cat.items():
        rs=[r for r in records if oid in r['objective_ids']];mx=max([r['mark_tariff'] for r in rs] or [0]);series={r['exam_series'] for r in rs}
        klass='unprobed_2020_2024' if not rs else ('probed_high' if mx>=5 or len(series)>=3 else ('probed_low' if mx<=2 else 'probed_mid'))
        exposure.append({'objective_id':oid,'exam_exposure':klass,'evidence':{
            'question_parts_naming_it':len(rs),'distinct_series':len(series),'max_mark_tariff':mx,
            'command_words_observed':dict(Counter(r['command_word'] for r in rs)),
            'total_associated_offered_marks':sum(r['mark_tariff'] for r in rs),
            'evidence_ids':[r['evidence_id'] for r in rs]}})
    dump(C/'exam-exposure.json',{'generated_by':'planning/build_analysis_6137.py','provenance':'corpus',
         'resolution':'Source specific-objective bullet, plus two explicitly marked cross-cutting aims; not each nested example. Multiple objective tags share marks, so associated marks must not be summed across objectives. Topic shares use one primary context only.',
         'classes':{'probed_high':'5 marks or more, or 3 or more distinct series','probed_mid':'Observed, maximum 3 or 4 marks and fewer than 3 distinct series','probed_low':'2 marks or fewer and fewer than 3 distinct series','unprobed_2020_2024':'No mapped part in the available 2020-2024 corpus; remains compulsory syllabus coverage'},'objectives':exposure})
    commands=[]
    for v in sorted({r['command_word'] for r in records}):
        rs=[r for r in records if r['command_word']==v];tariffs=Counter(r['mark_tariff'] for r in rs)
        commands.append({'command_word':v,'count':len(rs),'modal_tariffs':sorted(k for k,n in tariffs.items() if n==max(tariffs.values())),
             'tariffs_seen':sorted(tariffs),'tariff_counts':dict(tariffs),'paper_counts':dict(Counter(r['paper_id'] for r in rs)),
             'use_in_prompts':True,'evidence_ids':[r['evidence_id'] for r in rs]})
    dump(C/'command-word-observations.json',{'unit':'One primary assessed operation per marked allocation. Compound verbs remain compound; instruction carriers Study/Use are retained in the excerpt but not double-counted as operations. This is not a count of every lexical occurrence.',
       'provenance':'corpus, with normalized operation assigned by miner','commands':commands})
    aliases={'Explain / Account for':['explain','name and explain','describe and explain'],
       'Describe':['describe','describe and explain','describe and suggest','name and describe','identify and describe'],
       'Insert or label':['label'],'Calculate':['calculate','measure and calculate','find and calculate'],
       'Measure':['measure','measure and calculate'],'Giving your View':['how far do you agree','discuss how far you agree','do you agree','do you accept or reject','do you think'],
       'Name':['name','name and describe','name and explain'],'Identify':['identify','identify and describe'],
       'How':['how','how far do you agree']}
    verdicts=[]
    for row in read(C/'syllabus-facts.json')['command_words']:
        forms=aliases.get(row['word'],[row['word'].lower()])
        rs=[r for r in records if r['command_word'] in forms]
        tariffs=Counter(r['mark_tariff'] for r in rs)
        verdicts.append({'syllabus_row':row['word'],'source':row['source'],
            'observed_assessed_forms':sorted({r['command_word'] for r in rs}),
            'question_parts':len(rs),'tariffs_seen':sorted(tariffs),
            'modal_tariffs':sorted(k for k,v in tariffs.items() if v==max(tariffs.values())) if tariffs else [],
            'use_in_prompts':bool(rs),'allowed_forms':sorted({r['command_word'] for r in rs}),
            'note':'Allow only the observed forms listed, not every synonym in the glossary row. Nouns, source carriers and illustrative phrases are not credited commands.'})
    dump(C/'command-word-verdicts.json',{'verdicts':verdicts,'family_counts_overlap':True,
        'additional_observed_forms':[c for c in commands if not any(c['command_word'] in v['allowed_forms'] for v in verdicts)]})
    papers=[]
    for sid in sorted({r['source_id'] for r in records}):
        rs=[r for r in records if r['source_id']==sid];p=rs[0]['paper_id'];q=Counter()
        for r in rs:q[r['question_ref'][0]]+=r['mark_tariff']
        papers.append({'source_id':sid,'question_parts':len(rs),'offered_marks':sum(q.values()),'marks_by_question':dict(q),'sat_marks':75 if p=='1' else sum(q.values()),
                       'expected_offered_marks':150 if p=='1' else (65 if p=='2' else 60)})
    topics=defaultdict(lambda:Counter())
    for r in records:topics[r['primary_context_topic']][r['paper_id']]+=r['mark_tariff']
    dump(E/'corpus-statistics.json',{'question_parts':len(records),'offered_marks':sum(r['mark_tariff'] for r in records),'papers':papers,
         'primary_context_marks_by_topic':{k:dict(v) for k,v in sorted(topics.items())},
         'report_blocks':len(fs),'report_blocks_linked':sum(bool(f['evidence_ids']) for f in fs),
         'parts_with_report_blocks':sum(bool(r['examiner_findings']) for r in records),
         'parts_with_error_findings':sum(bool(r['common_errors']) for r in records),
         'parts_with_explicit_credit_shapes':sum(bool(r['creditworthy_points']) for r in records),
         'specific_objective_bullets':sum(not x.startswith('X.') for x in cat),'cross_cutting_aims':sum(x.startswith('X.') for x in cat),'objective_mappings_changed_from_token_match':0,
         'token_match_note':'No token-matched baseline was created. Zero means not applicable, not zero mapping repairs.'})
    print(json.dumps(read(E/'corpus-statistics.json'),indent=2))

if __name__=='__main__':build()
