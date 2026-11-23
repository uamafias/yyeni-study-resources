"""Assemble author-confirmed paired-page matches and internal draft references."""
import json
import hashlib
from analysis_sources import A, WB, ROOT, digest, write, reference_label
from provenance_inputs import SPEC, PART_MAP, PAIR_PART_MAP
SESSIONS={'m':'Feb/March','s':'May/June','w':'Oct/Nov'}

def build(questions=None):
    if questions is None:questions=json.loads((A/'question-analysis.json').read_text())['questions']
    qs={q['source_key']:q for q in questions};matches=[]
    for q in questions:
        for p in q['parts']:p['examination_references']=[r for r in p['examination_references']if not r.get('provenance_match_id')]
    structural=[]
    audit=json.loads((A/'provenance-reading-r5.json').read_text())['entries']
    for n,line in enumerate(SPEC.strip().splitlines(),1):
        key,stem,num,pgs,confidence,shared,changed,defect=line.split('|')
        check=audit[f'8227:PROVENANCE:{n:03}']
        expected_input=hashlib.sha256(line.encode()).hexdigest()
        if n==37 and check['input_sha256']!=expected_input:
            repair=json.loads((WB/'tools/provenance-037-text-repair-r7.json').read_text())
            assert repair['previous_input_sha256']==check['input_sha256']and repair['corrected_input_sha256']==expected_input and repair['corrected_input_line']==line and repair['render_sha256']==check['image_sha256'],'unregistered provenance037 text change'
        else:assert check['input_sha256']==expected_input,('provenance input changed after rendered check',n)
        assert digest(ROOT/check['image_path'])==check['image_sha256']
        cb=json.loads(next((A/'cambridge-discovery').glob(stem+'-*.json')).read_text());q=qs[key]
        assert digest(ROOT/cb['path'])==cb['sha256'] and digest(ROOT/q['question_source_path'])==q['source_sha256']
        pages=[int(p) for p in pgs.split(',')]
        evidence=ROOT/check['image_path'];assert evidence.exists()
        mapping=PAIR_PART_MAP.get(n,PART_MAP.get(key,{p['source_label'] or 'answer':p['source_label'] for p in q['parts']}))
        part_pages={'2024-2-Q5':{'c':9},'2022-2-Q3':{'c':11},'2022-2-Q10':{'b':9},'2023-2-Q5':{'b':9},'2024-2-Q7':{'c':9},'2025-1-Q9':{'b':11,'c':11}}
        part_pages.update({'2025-2-Q12':{'c':7,'d':7},'2022-2-Q7':{'b':11},'2023-2-Q3':{'b.ii':11,'b.iii':11},'2021-2-Q12':{'b':11}})
        refs=[];part_links=[]
        for p in q['parts']:
            label=p['source_label'] or 'answer'
            if label not in mapping:continue
            if confidence.startswith(('structurally similar','possible source')) or n==4:continue
            actual_page=part_pages.get(key,{}).get(label,pages[0])
            ref={'board':'Cambridge International','syllabus_code':'9709','year':cb['year'],
                 'session':SESSIONS[cb['session_code']],'paper':cb['component'],'question':num,'part':mapping[label],
                 'printed_page':actual_page,'pdf_page':actual_page,'question_pdf_pages':pages,
                 'source_path':cb['path'],'source_sha256':cb['sha256'],'relation':'derived-from',
                 'verified_by':f"Codex author, {check['date']}; paired page-image check {evidence.name}; independent check pending",
                 'learner_display':False,'learner_display_reason':'Draft Adapted from attribution; display policy deferred to step 3 PLAN. Held-source prohibition also applies.',
                 'provenance_match_id':f'8227:PROVENANCE:{n:03}'}
            ref['learner_label']=reference_label(ref)
            # Repeated standalone builds are idempotent; old derived refs are regenerated, not appended twice.
            p['examination_references']=[r for r in p['examination_references'] if r.get('provenance_match_id')!=ref['provenance_match_id']]+[ref]
            refs.append(ref);part_links.append({'nsscas_part_id':p['part_id'],'cambridge_part':mapping[label]})
        matches.append({'match_id':f'8227:PROVENANCE:{n:03}','nsscas_question_key':key,
             'nsscas_locator':{'source_path':q['question_source_path'],'source_sha256':q['source_sha256'],
                    'year':q['year'],'paper':str(q['paper']),'question':q['question'],'pdf_pages':q['pdf_pages'],'printed_pages':q['pdf_pages']},
             'cambridge_locator':{'source_path':cb['path'],'source_sha256':cb['sha256'],'year':cb['year'],
                    'session':SESSIONS[cb['session_code']],'paper':cb['component'],'question':num,'pdf_pages':pages,'printed_pages':pages},
             'shared':shared,'changed':changed,'confidence':confidence,
             'confidence_basis':'Author inference from distinctive expressions, values, diagram and/or connected part sequence; paired documents verify correspondence, not the examiner authorship history.',
             'explains_source_defect':None if defect=='None' else defect,
             'part_correspondence':part_links,'rendered_confirmation':{'status':check['status'],
                    'path':str(evidence.relative_to(ROOT)),'sha256':digest(evidence),'reviewer':'Codex','date':check['date']},
             'examination_references':refs})
    for q in questions:
        if q['source_key']=='2024-2-Q7':
            for p in q['parts']:
                for r in p['examination_references']:
                    if r['relation']=='original':
                        r['source_defect_ids']=['SRC-8227-DIAGRAM-2024-P2-Q7']
                        r['source_note']='Printed diagram misplaces P: y=1/4 gives x≈-2.50, left of y-axis and below the y-intercept≈0.79. Read the equations and stated coordinate.'
    for m in matches:
        m['duplicate_variant_leads']=[{'file_stem':stem,'verification':'local corpus duplicate-variant lead; not a separate breadth item or additional attribution'}for stem in {3:['9709_s16_qp_23'],4:['9709_s16_qp_22'],12:['9709_s19_qp_23'],15:['9709_w23_qp_23'],16:['9709_w22_qp_21'],25:['9709_s15_qp_23'],28:['9709_s19_qp_23'],31:['9709_s18_qp_23'],33:['9709_w22_qp_23'],35:['9709_s19_qp_23'],37:['9709_s20_qp_23']}.get(int(m['match_id'].rsplit(':',1)[1]),[])]
    extra=json.loads((WB/'checks/r6/provenance-additional-pages.json').read_text())
    current=next(m for m in matches if m['match_id']=='8227:PROVENANCE:037')
    duplicate=next(r for r in extra if r['stem']=='9709_s20_qp_23')
    lead=next(r for r in extra if r['stem']=='9709_s17_qp_21')
    for r in [duplicate,lead]:
        assert digest(ROOT/r['path'])==r['sha256']
        assert digest(ROOT/r['source_path'])==r['source_sha256']
    current['text_spacing_correction_r7']=json.loads((WB/'tools/provenance-037-text-repair-r7.json').read_text())
    current['duplicate_variant_leads']=[dict(duplicate,
        verification='author read 2026-11-22: identical Q1; duplicate variant, not independent breadth')]
    current['weaker_template_leads']=[dict(lead,
        status='weaker template lead, not confirmed specific source; no derived-from reference',
        reason='2017/21 Q1 has 5^x = 3^(4y) and y = mx; 2020/22 Q1 shares the more distinctive y-on-the-left, 3x-on-the-right and y = kx structure.',
        learner_display=False)]
    folded=[m for m in matches if m['match_id']=='8227:PROVENANCE:004']
    for m in folded:m['folded_into']='8227:PROVENANCE:003'
    possible=[m for m in matches if m['confidence'].startswith('possible source')]
    structural=[m for m in matches if m['confidence'].startswith('structurally similar')]
    matches=[m for m in matches if m not in structural+possible+folded]
    leads=json.loads((A/'provenance-search-leads.json').read_text());matched={m['nsscas_question_key'] for m in matches}
    search=[{'nsscas_question_key':r['source_key'],'candidate_pages_ranked':len(r['candidates']),
              'search_basis':'Automated distinctive-word/value TF-IDF discovery ranking; selected leads and reviewer leads checked by the author. Eight ranked candidates do not mean eight visually read pages.',
              'status':'paired-page match confirmed' if r['source_key'] in matched else 'no match confirmed in this pass',
              'full_screen_candidate_pages_read':sum(c['disposition']!='unread' for rr in json.loads((A/'provenance-full-screen-r5.json').read_text())['results']if rr['source_key']==r['source_key']for c in rr['candidates']),
              'unresolved':'No confirmed match does not establish originality; lower ranked pages and image-only matches may remain.',
              'lead_record':'provenance-search-leads.json#'+r['source_key']} for r in leads['results']]
    lead_dispositions=[]
    for r in leads['results']:
        for rank,c in enumerate(r['candidates'][:4],1):
            confirmed=[m['match_id']for m in matches if m['nsscas_question_key']==r['source_key']and m['cambridge_locator']['source_path']==c['source_path']and c['pdf_page']in m['cambridge_locator']['pdf_pages']]
            similar=[m['match_id']for m in structural if m['nsscas_question_key']==r['source_key']and m['cambridge_locator']['source_path']==c['source_path']]
            lead_dispositions.append({'nsscas_question_key':r['source_key'],'rank':rank,'source_path':c['source_path'],'pdf_page':c['pdf_page'],
              'disposition':'confirmed paired-page correspondence'if confirmed else 'structural comparison; no specific source'if similar else 'unread',
              'match_ids':confirmed+similar,'reason':'See paired-page record'if confirmed or similar else 'Similarity ranking alone cannot establish an adapted source; no visual confirmation recorded for this pair. Remains an unresolved provenance lead, not rejected or original.'})
    screen=json.loads((A/'provenance-full-screen-r5.json').read_text())
    read_leads={(r['source_key'],c['source_sha256'],c['pdf_page']):c for r in screen['results']for c in r['candidates']if c['disposition']!='unread'}
    for entry in lead_dispositions:
        c=next((c for (key,sha,pg),c in read_leads.items()if key==entry['nsscas_question_key']and c['source_path']==entry['source_path']and pg==entry['pdf_page']),None)
        if c:entry.update(disposition=c['disposition'],reason=c['reason'],render_reading=c['render_reading'])
    write(A/'provenance-lead-dispositions-r4.json',{'leads':lead_dispositions,'limits':'Only explicitly confirmed pairs support attribution. Unpromoted leads remain unresolved.'})
    result={'schema_version':'8227-source-analysis-r5','status':'author pass; focused cross-vendor check pending',
          'coverage':{'nsscas_questions_searched':len(search),'legacy_cambridge_discovery_pages_ranked':leads['cambridge_search_pages'],
                'legacy_ranked_candidate_pages_per_question':8,'full_page_comparison':{k:v for k,v in screen.items()if k not in ['results']},'confirmed_pair_records':len(matches),'nsscas_questions_with_confirmed_match':len(matched),
                'unmatched_questions':len(search)-len(matched),'limits':'Every indexed local QPpage compared; every above-threshold candidate read. Lower-threshold leads stay unread unless a paired record proves reading. Local indexed2015–2025corpus only, not a proof of exhaustive provenance or original authorship. Duplicate Cambridge variants do not add independent breadth. Only visually confirmed pairs are promoted to matches.'},
          'full_page_screen':'provenance-full-screen-r5.json','rank1_to4_lead_dispositions':'provenance-lead-dispositions-r4.json','matches':matches,'structural_comparisons_without_source_claim':structural,'possible_sources_wording_only':possible,'folded_duplicate_records':folded,'question_search_register':search,'display_policy':'All derived-from references are draft/internal (learner_display false); PLAN decides display. Source attribution does not license textbook reproduction.'}
    write(A/'nsscas-cambridge-provenance.json',result)
    out=['# NSSCAS → Cambridge provenance pass — 8227','',
         'Author inference from paired source images, 17–22 November 2026; focused independent check pending. All 119 questions searched. Confirmed pairs and demoted structural comparisons are counted separately in the JSON; duplicate variants do not add breadth. Missing matches are unresolved, never proof of originality.','',
         '| NSSCAS | Cambridge | Confidence | Shared / changed | Source defect |','|---|---|---|---|---|']
    for m in matches:
        c=m['cambridge_locator'];out.append(f'| {m["nsscas_question_key"]} | 9709/{c["paper"]} {c["session"]} {c["year"]} Q{c["question"]}, PDF {c["pdf_pages"]} | {m["confidence"]} | {m["shared"]}. Changes: {m["changed"]} | {m["explains_source_defect"] or "None established"} |')
    out+=['','## Structural comparisons without a source claim','']
    for m in structural+possible:out.append(f'- {m["match_id"]}: {m["nsscas_question_key"]}; {m["changed"]}. No derived-from reference.')
    out+=['','## Search coverage and limits','',result['coverage']['limits'],'',
          '| Question | Pass result |','|---|---|']
    out += [f'| {s["nsscas_question_key"]} | {s["status"]} |' for s in search]
    out+=['',result['display_policy'],'']
    (A/'nsscas-cambridge-provenance.md').write_text('\n'.join(out))
    return result
if __name__=='__main__':
    data=json.loads((A/'question-analysis.json').read_text())
    result=build(data['questions'])
    write(A/'question-analysis.json',data)
    print(json.dumps(result['coverage'],indent=2))
