"""Declare T1–T6 author completeness only after the saved final proofs pass."""
import json
from analysis_sources import A,WB,ROOT,digest,write
from audit_textbook_completion_r5 import audit

def main():
    inventory=json.loads((A/'textbook-inventory.json').read_text())
    census=json.loads((A/'textbook-page-census.json').read_text())
    answers=json.loads((A/'textbook-answer-verification-r5.json').read_text())['subparts']
    synthesis=json.loads((A/'textbook-families.json').read_text())
    report=audit(inventory['items'],census,answers,synthesis)
    fresh_path=WB/'checks/fresh-copy-verification-r5.json'
    fresh=json.loads(fresh_path.read_text())
    proof_path=A/'history/rebuild-verification-r5-final-fresh-copy.json'
    proof=json.loads(proof_path.read_text())
    assert fresh['status']=='pass'and fresh['double_rebuild']and fresh['matches_author_checkout']
    assert proof['identical']and len(proof['seeded_negative_results'])==38
    assert all(i['design_use_status']=='author-complete; awaiting independent check'for i in inventory['items'])
    for name in ['textbook-inventory.json','textbook-page-census.json','textbook-families.json','textbook-answer-verification-r5.json','textbook-completion-audit-r5.json']:
        relative=str((A/name).relative_to(ROOT))
        assert digest(A/name)==proof['output_hashes'][relative],('author data changed after fresh proof',name)
    result=dict(status='Textbook population complete; ready for Claude’s independent check',
        author='Codex',owner='Vitalis',date='2026-11-21',qualification='Namibia NSSCAS Mathematics8227',
        stages={f'T{n}':'author complete'for n in range(1,7)},counts=report['counts'],
        source_pages=census['coverage']['pages_enumerated'],eligible_response_items_resolved=synthesis['progress']['response_items_with_all_eligible_responses_resolved'],
        whole_source_items_excluded=synthesis['progress']['response_items_explicitly_excluded'],
        source_parts_excluded=synthesis['progress']['source_responses_explicitly_excluded'],
        source_defect_cautions=len(json.loads((A/'textbook-defects-r5.json').read_text())['entries']),
        proof=dict(path=str(fresh_path.relative_to(ROOT)),sha256=digest(fresh_path),
            manifest_path=str(proof_path.relative_to(ROOT)),manifest_sha256=digest(proof_path),
            commands_per_run=fresh['commands_per_run'],byte_identical_outputs=fresh['outputs_compared'],seeded_errors_rejected=38),
        independent_acceptance=False,owner_acceptance=False,review_sample='Not prepared by author;reviewer selects a fresh blind sample of at least10percent with own seed.',
        next_step='Focused cross-vendor check of Part1repairs and both complete textbook analyses. Step3remains deferred until independent acceptance.',
        limitations=['The agreed source envelope is exhaustive;recorded excluded sections/parts are not imported wholesale.',
            'Families are author analysis groups,not approved recipe counts or guaranteed examination equivalence.',
            'Textbook originals stay internal;defects and extra-method restrictions remain visible.',
            'Radian interpretation has teaching-figure support but no separately posed textbook item.',
            'No application/website,runtime marking,installation,publication or production acceptance is claimed.'])
    write(A/'textbook-author-completion-r5.json',result)
    lines=['# Author completion declaration — NSSCAS Mathematics8227','',result['status'],
        '', 'Author:Codex. Owner:Vitalis.21November2026. T1–T6author complete;independent and owner acceptance remain pending.','',
        f'{result["source_pages"]}source-envelope pages,{report["counts"]["source_records"]}source records,{report["counts"]["figure_records"]}figures and{report["counts"]["answers"]}response checks. {report["counts"]["families"]}analysis families;all138demands have teaching insights.','',
        f'Fresh-copy proof:{fresh["commands_per_run"]}commands per run,{fresh["outputs_compared"]}byte-identical outputs,38seeded failures rejected. Copied outputs matched the author checkout.','',
        'No author-selected review sample. Claude must draw its own fresh blind sample and independently check completeness,mapping,qualifiers,answers,families and insights.','',
        '## Limits','']+['- '+v for v in result['limitations']]+['',result['next_step'],'']
    (A/'textbook-author-completion-r5.md').write_text('\n'.join(lines))
    print(json.dumps({'declaration':result['status'],'independent_acceptance':False,'proof':result['proof']},indent=2))
if __name__=='__main__':main()
