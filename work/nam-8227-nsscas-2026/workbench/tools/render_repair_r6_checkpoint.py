"""Render the working R6 report from saved progress; never declare acceptance."""
import collections
import json
import re
from analysis_sources import A,WB,write,digest


def save_status(checkpoint,validation):
    """Keep continuation counters generated alongside the machine checkpoint."""
    c=checkpoint['counts'];m=checkpoint['objective_map_counts']
    n=checkpoint['new_seeded_errors_rejected']
    proof=json.loads((WB/'checks/r6/working-double-rebuild.json').read_text())
    current=proof['ledger_sha256']==digest(WB/'tools/textbook-exam-relations-r6.json')
    current=current and all(digest(WB/'tools'/p)==h
        for p,h in proof.get('tool_sha256',{}).items())
    current=current and all(digest(A/p)==h for p,h in proof.get('analysis_input_sha256',{}).items())
    proof_text=('The scoped double rebuild matches this ledger and its recorded tool hashes.'
        if current else f"The most recent scoped double rebuild covers {proof['pair_decisions']:,} decisions; repeat it for this changed state.")
    facts=(f"The working author analysis contains {checkpoint['families']} families; all "
        f"{checkpoint['source_response_pairs_preserved']:,} original source-response pairs and "
        f"all {validation['accepted_item_links_preserved']:,} accepted source-record link projections remain unchanged. "
        'Structural checks do not certify semantic or independent acceptance.\n\n'
        f"A: {c['decisions_recorded']:,}/{c['candidate_pairs']:,} uncapped family–part decisions saved; "
        f"{c['undecided_pairs']:,} remain. Main decisions: {json.dumps(c['decisions_by_kind'])}. "
        f"There are {c['member_level_exceptions']} member exception rows; their relation counts are "
        f"{json.dumps(c['member_exception_decisions_by_kind'])}. Counting a family/part pair once, "
        f"{c['same_type_family_part_pairs_including_member_exceptions']} have a same-type relation including named exceptions. "
        f"Family summaries: {json.dumps(c['families_by_summary'])}. Incomplete never means no counterpart.\n\n"
        'The generated map retains all 60 objectives/138 demands. Verified same-type comparisons currently reach '
        f"{m['by_objective']['with_same_type_textbook_practice']} objectives/"
        f"{m['by_demand']['with_same_type_textbook_practice']} demands. Counts are author judgements, pending independent review. "
        'Eleven demands have no NSSCAS part; interpreting a radian has no indexed posed practice item.\n\n'
        f"{proof_text} Working checks reject all {n} new negative fixtures. "
        'This does not establish the required final relocated full rebuild or rerun of the prior 38 fixtures. '
        f"The read ledger has {checkpoint['reading_entries']} actually viewed entries "
        f"({checkpoint['unique_read_source_pages']} unique source pages). Rendering alone is not reading. "
        'The live analysis snapshot remains R5.\n')
    (WB/'STATUS.md').write_text('# STATUS — NSSCAS Mathematics 8227 Workbench\n\n'
        'Repair round 6 active. AUTHOR Codex; owner Vitalis. Revised 21 November prompt governs. '
        'Step 3 waits for completion and independent acceptance.\n\n'+facts+'\n'
        'Remaining: finish A and exceptions, B.3–B.5 prose, C figures and D notes/key-page/provenance repairs, '
        'full validation and focused Claude acceptance. No commit/push or step-3 outputs. See HANDOVER.md.\n')
    p=WB/'HANDOVER.md';text=p.read_text()
    a=text.index('## Current saved checkpoint');b=text.index('## Latest content work',a)
    text=text[:a]+'## Current saved checkpoint\n\n'+facts+'\n'+text[b:]
    text=re.sub(r'working structural checks and \d+ new seeded negatives',
        f'working structural checks and {n} new seeded negatives',text)
    p.write_text(text)
    banner=('<!-- R6-ACTIVE-CHECKPOINT -->\nRound 6 remains active. '
        f"{c['decisions_recorded']:,}/{c['candidate_pairs']:,} uncapped family comparisons recorded; "
        f"{c['undecided_pairs']:,} open. Working checks reject {n} new seeded errors. "
        'Final full relocated validation and focused Claude acceptance remain outstanding. Step 3 waits. '
        'See workbench/STATUS.md and workbench/HANDOVER.md. Entries below describe historical stages, '
        'not current R6 completion.\n<!-- /R6-ACTIVE-CHECKPOINT -->')
    for name in ['STATUS.md','README.md']:
        p=WB.parent/name;text=p.read_text()
        text=re.sub(r'<!-- R6-ACTIVE-CHECKPOINT -->.*?<!-- /R6-ACTIVE-CHECKPOINT -->',
            lambda _:banner,text,count=1,flags=re.S)
        p.write_text(text)


def build():
    f=json.loads((A/'textbook-families.json').read_text())
    c=json.loads((WB/'checks/r6/comparison-progress.json').read_text())['counts']
    m=json.loads((A/'objective-problem-map.json').read_text())
    ledger=json.loads((WB/'tools/textbook-exam-relations-r6.json').read_text())
    inventory=json.loads((A/'textbook-inventory.json').read_text())
    validation=json.loads((WB/'checks/r6/working-validation.json').read_text())
    negatives=len(validation['negative_fixtures'])
    assert validation['pair_decisions']==c['decisions_recorded']==len(ledger['relations']), \
        'working checkpoint inputs belong to different comparison states'
    figures=[i for i in inventory['items']if i.get('item_kind')in ['teaching-figure','given-figure']]
    figure_counts=dict(total=len(figures),by_graphic_text_class=dict(collections.Counter(
        i.get('figure_record_type','not yet classified')for i in figures)),
        containing_pending_actual_value=sum('pending actual-value screening'in json.dumps(i)for i in figures),
        pending_representation_comparison=sum('pending'in str(i.get('exam_representation_check','')).lower()for i in figures),
        explicit_content_check_field=sum('content_check'in i for i in figures))
    checkpoint=dict(new_seeded_errors_rejected=negatives,stage='B.3–B.5/C/D active; all uncapped family-exam candidates decided',completion=False,
        families=len(f['families']),counts=c,objective_map_counts=m['counts'],figure_counts=figure_counts,
        source_response_pairs_preserved=5744,accepted_item_links_unchanged=True,
        reading_entries=len(ledger['readings']),unique_read_source_pages=len({
            (r['source_path'],r['pdf_page'])for r in ledger['readings']}),
        note_spacing_repairs=len(json.loads((WB/'tools/textbook-note-spacing-r6.json').read_text())['entries']),
        provenance_pair_records=len(json.loads((A/'nsscas-cambridge-provenance.json').read_text())['matches']),
        single_member_families_normalised=sum(len(row['members'])==1 and row['difficulty_progression']=='single item' for row in f['families']),
        next='Finish family-specific B.3–B.5 prose, figure taxonomy/comparison and remaining notes/key-page audit, then full relocated rebuild and independent focused check.')
    write(WB/'checks/r6/checkpoint.json',checkpoint)
    save_status(checkpoint,validation)
    lines=['# Repair round 6 — working checkpoint, NSSCAS Mathematics 8227','',
        '**In progress. This is not a completion handback or independent acceptance request.** '
        'Authority: owner-revised 21 November prompt. Step 3 waits. No commit or push.','',
        '| Finding | Saved work and check | Remaining |','|---|---|---|',
        '| R5-01 | Uncapped candidates; explicit family decisions and rendered readings; generated objective map; '
        '58 derived insight exam sections. `checks/r6/working-validation.json`. | '
        f"{c['undecided_pairs']} candidate decisions, remaining member exceptions, final insight proposals and representation pointers. |",
        '| R5-02 | Explicit membership repairs in `tools/textbook_family_repairs_r6.py`; '
        '0 unsupported common-demand memberships under accepted direct links; all 5,744 source-response pairs retained. '
        'Mixed part selections also repaired on inspected pages. | B.3–B.5 prose, difficulty ordering, '
        'units/precision and individual membership reasons; independent semantic check. |',
        '| R5-03 | Accepted assessed/component/objective/learner-display links unchanged for all 3,940 records; '
        'item-union support and its limitation remain in the map. | Registry overlaps resolved in step 3; no R6 retagging. |',
        '| R5-04 | The prior 9 checked figure errors remain in the preserved 11-entry '
        '`analysis/textbook-corrections-r6.json`. | Graphic/text classification, honest content checks, '
        'stale statuses, worked-solution roles and representation links. Incidental YM PDF396 factor-box '
        'typo captured in checks/r6; integrate during C. No full figure-content audit. |',
        '| R5-05 | Both named key-page fixes remain in canonical authors (Goldie PDF346, YM PDF599); '
        'both slips remain in the 11-entry correction register. | All applicable top-of-answer-page checks, '
        '634 spaced notes, eventual propagation through the full rebuild. |',
        '| R5-06 | Accepted R5 provenance preserved. | New 2023 P2 Q4(b) pair, both source reads, '
        'hidden label, measured recall limitation and pair021 correction. |','',
        '## Counts before and at this checkpoint','',
        '| Measure | R5 | Working R6 |','|---|---:|---:|',
        f"| Families (analysis groups, not recipe counts) | 380 | {len(f['families'])} |",
        '| Families with unsupported per-member common demand claims | 90 | 0 |',
        '| Unsupported memberships under accepted direct-link check | 374 | 0 |',
        '| Unique source-response pairs preserved | 5,744 | 5,744 |',
        '| Incorrect no-exam insight sections | 6 | 0 |',
        '| Genuine no-exam insight sections | 2 | 2 |',
        f"| Uncapped family–part candidates | 2,080 (reviewer recomputation) | {c['candidate_pairs']} |",
        f"| Explicit family–part decisions | 0 at required grain | {c['decisions_recorded']} |",
        f"| Member exception rows | 0 | {c['member_level_exceptions']} |",'',
        'Decisions and derived family summaries:','',
        '```json',json.dumps(c,indent=2),'```','',
        'R5 had 219 structural-branch and 161 textbook-only labels, without the required pair decisions. '
        'The R6 incomplete category is deliberate: lack of a recorded match is not a no-counterpart finding. '
        'The former 16,246 item/exam workload is archived, superseded discovery.','',
        '## Objective problem map (working)','',
        '```json',json.dumps(m['counts'],indent=2),'```','',
        'All 60 objectives and 138 demands are present. Eleven demands have no NSSCAS part; '
        'the held principal-value part is visible but is not a usable learner anchor. '
        'Interpreting a radian has no recorded posed practice item in the indexed sources. '
        'Teaching illustrations are not automatically practice. Same-type/variant counts are provisional '
        'until the comparison ledger is complete.','',
        '## Figure work still open','',
        '```json',json.dumps(figure_counts,indent=2),'```','',
        'These are the existing records, not a completed C-stage classification or content audit.','',
        '## Checks and limits','',
        'The working check preserves source links and source responses, validates recorded positive reads, '
        f'covers every demand in the map and rejects all {negatives} new seeded errors '
        '(the six commissioned cases plus wrong-sibling-page, future-source-read, '
        'divergent-integral and implicit-seed-choice regressions). '
        '`checks/r6/working-double-rebuild.json` names the scope and output hashes of the most recent '
        'scoped double rebuild. It is not the final fresh-copy full rebuild. The previous 38 seeded '
        'fixtures have not yet been rerun for the final R6 state.','',
        'The R5 snapshot and original R6 baseline are preserved. The owner-revised prompt is the sole '
        'baseline review-file hash difference, recorded in checks/r6/prompt-revision.json; Codex has '
        'not edited review folders. The live analysis snapshot remains the R5 snapshot and does '
        'not freeze this working analysis. No educational acceptance or production readiness is inferred.','']
    (WB/'checks/repair-r6-report.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(dict(families=len(f['families']),counts=c),indent=2))


if __name__=='__main__':build()
