"""Re-run whole-subject checks and verify the actual build against approved slots.

Local author verification only. No Claude call, publishing, commit or import.
"""
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

WS=Path(__file__).resolve().parents[1];REPO=WS.parents[1]
STD=REPO/'standard/v0.2.0-draft'
sys.path.insert(0,str(STD/'build'))
from naming import notes_filename

def read(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')

def main():
    perfs={x['slot']:x for x in read(WS/'curriculum/performance-slot-specs.json')['slots']}
    rows=[];mismatches=[];hashes={};over_ceiling=[]
    topic_dirs=sorted([p for p in (WS/'topics').iterdir() if p.is_dir() and (p/'contract.json').exists()],key=lambda p:[int(x) for x in p.name.split('.')])
    for td in topic_dirs:
        tid=td.name;wo=read(td/'work_order.json');contract=read(td/'contract.json')
        proc=subprocess.run([sys.executable,str(STD/'checks/run_checks.py'),str(WS),tid],capture_output=True,text=True)
        qa=read(td/'qa_report.json')
        fix=subprocess.run([sys.executable,str(STD/'checks/what_to_fix.py'),str(WS),tid],capture_output=True,text=True)
        items=read(td/wo['output_files']['learning_items'])['items']
        claims=read(td/'claims/canonical_claim_ledger.json')['claims']
        units=[read(td/u['file']) for u in wo['content_units']]
        slots=wo['item_slots']+wo['performance_tasks'];actual={x['item_id']:x for x in items}
        if len(actual)!=len(items):mismatches.append(tid+': duplicate item IDs')
        if set(actual)!={s['slot'] for s in slots}:mismatches.append(tid+': missing or extra slot')
        for s in slots:
            it=actual[s['slot']];perf='item_type' in s;expected=perfs[s['slot']] if perf else s
            for key in ['assessment_objectives','blooms_level','command_word','mark_tariff']:
                if it[key]!=expected[key]:mismatches.append(s['slot']+': '+key)
            if not perf and (it['subtype']!=s['subtype'] or it['objective_ids']!=[s['objective_id']]):mismatches.append(s['slot']+': subtype/objective')
            if perf and it['item_type']!=s['item_type']:mismatches.append(s['slot']+': task type')
            if not perf and s.get('misconception_entry')!=it.get('misconception_entry'):mismatches.append(s['slot']+': misconception ID')
        for c in claims:
            if c['verification']['status']!='unverified' or c['publishable']:mismatches.append(c['claim_id']+': improperly marked verified/publishable')
        for u in units:
            if u['word_count']>u['word_budget']['max']:over_ceiling.append(u['unit_id'])
        nf=notes_filename(tid,contract['topic_title']);notes=td/nf
        if not notes.exists():mismatches.append(tid+': missing rendered notes')
        counts=Counter(x['status'] for x in qa['deterministic_checks'])
        failures=[x for x in qa['deterministic_checks'] if x['status']=='fail']
        row={'topic_id':tid,'title':contract['topic_title'],'claims':len(claims),'units':len(units),'items':len(items),
             'flashcards':sum(x['item_type']=='flashcard' for x in items),'activities':sum(x['item_type']!='flashcard' for x in items),
             'notes':str(notes.relative_to(WS)),'rendered_words':len(notes.read_text().split()),'block_words':sum(u['word_count'] for u in units),
             'objectives':wo['assessable_objective_count'],'release_decision':qa['release_decision'],
             'runner_exit_code':proc.returncode,'what_to_fix_exit_code':fix.returncode,'check_status_counts':dict(counts),
             'failures':failures,'warnings':[x for x in qa['deterministic_checks'] if x['status']=='warn'],
             'not_run':[x for x in qa['deterministic_checks'] if x['status']=='not_run'],
             'word_allocations':[{'unit_id':u['unit_id'],'actual':u['word_count'],'allocated':u['word_budget']} for u in units]}
        rows.append(row)
        for p in [td/'claims/canonical_claim_ledger.json',td/wo['output_files']['learning_items'],notes,*[td/u['file'] for u in wo['content_units']]]:
            hashes[str(p.relative_to(WS))]=hashlib.sha256(p.read_bytes()).hexdigest()
        print(tid,qa['release_decision'],'failures',len(failures),'items',len(items),flush=True)
    from audit_research import audit as audit_authored_research
    packages,numeric_checks=audit_authored_research()
    totals={k:sum(r[k] for r in rows) for k in ['claims','units','items','flashcards','activities','rendered_words','block_words','objectives']}
    assert len(rows)==18 and totals['objectives']==356 and totals['items']==543 and totals['flashcards']==505 and totals['activities']==38
    assert not mismatches and not over_ceiling and all(numeric_checks.values())
    assert not any(r['failures'] or r['what_to_fix_exit_code'] for r in rows)
    report={'date':'2026-10-21','stage':'Codex repairs after Claude fourth whole-subject review; no fifth review or learner release claimed',
        'topics':rows,'totals':totals,'remaining_topics':0,'remaining_items':0,'slot_metadata_mismatches':mismatches,'over_upper_word_ceiling':over_ceiling,
        'research_packages':packages,'independent_numeric_checks':numeric_checks,'content_sha256':hashes,
        'claude_contacted_during_authoring':False,'review_authorisation':'Fourth whole-subject review completed at Jeremy’s request; no fifth review without his explicit request.',
        'limitations':['Zero deterministic failures is not independent approval of the repaired draft.','Claims remain unverified and non-publishable.',
                      'Advisory minimum-word and local AO-mix warnings retained; see each topic.',
                      'General graph check/renderer unsupported: explicit datasets and construction specifications recomputed locally; no unseen-render PASS claimed.',
                      'Standard profile-schema/runner/template issues remain visible. No pilot completion, learner release, platform import, commit or push claimed.']}
    dump(WS/'authoring-progress.json',report)
    lines=['# Development Studies 6136 — complete authored draft build','',
           'All 18 topics and 543 planned items are authored. Codex repaired the fourth whole-subject Claude review findings; those repairs have not been independently reviewed. See review/CLAUDE-RESOURCE-REVIEW-4.md and review/repairs/round4/REPAIR-REPORT.md. No fifth review or publication approval is claimed.','',
           '| Topic | Notes | Items | Automated failures |','|---|---|---:|---:|']
    for r in rows:
        td=WS/'topics'/r['topic_id'];wo=read(td/'work_order.json')
        lines.append(f'| {r["topic_id"]} {r["title"]} | [Read notes]({r["notes"]}) | [View {r["items"]} items](topics/{r["topic_id"]}/{wo["output_files"]["learning_items"]}) | {len(r["failures"])} |')
    lines+=['',f'Totals: {totals["claims"]} claims, {totals["units"]} content units, {totals["flashcards"]} flashcards, {totals["activities"]} activities, {totals["rendered_words"]:,} rendered-note words.','',
            'The four research packages each contain 35 marks in Section A and 15 in Section B. Fictional models never replace learners’ actual fieldwork.','',
            'Warnings, no-opinion checks, source limitations and compatibility issues are retained in [the build audit](authoring-progress.json) and [status](STATUS.md). Checks returning publish mean zero deterministic failures, not independent approval. No upload folder or learner release is asserted.']
    (WS/'BUILD-INDEX.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(totals),flush=True)

if __name__=='__main__':main()
