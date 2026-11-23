"""Promote completed author records for independent review, never accept them."""
import json
from analysis_sources import A,write
from audit_textbook_completion_r5 import audit

def main():
    path=A/'textbook-inventory.json';inventory=json.loads(path.read_text())
    census=json.loads((A/'textbook-page-census.json').read_text())
    answers=json.loads((A/'textbook-answer-verification-r5.json').read_text())['subparts']
    synthesis=json.loads((A/'textbook-families.json').read_text())
    audit(inventory['items'],census,answers,synthesis)
    inventory['status']='author textbook population and analysis complete; independent acceptance pending'
    inventory['coverage'].update(exhaustive=True,formal_stop_rule_applied=False,
        stop_rule_reason='No sampling stop rule. Every page and inventory entry in the agreed source envelope is enumerated; every eligible response has an explicit analysis disposition. This is author completeness,not educational acceptance.',
        exhaustive_definition='Complete author inventory of the agreed in-scope envelope; explicitly excluded parent sections/parts and the duplicate scan remain recorded. It does not mean all content in excluded sections is prescribed.')
    for item in inventory['items']:
        item['pre_completion_design_use_status']=item['design_use_status']
        item['design_use_status']='author-complete; awaiting independent check'
        item['design_use_limits']='Internal source evidence only. Original scope exclusions,source defects,method conditions and ambiguities remain binding. No recipe or learner-display acceptance is granted.'
    for chapter in inventory['coverage']['chapters']:
        chapter['author_chapter_analysis_complete']=True
        chapter['whole_chapter_complete']=False
        chapter['remaining']='Independent completeness/classification/answer/family acceptance. Author analysis is complete; final round-level fresh-copy proof and snapshot are recorded separately.'
    inventory['next_required']='Focused Claude short cross-vendor check of the R7 repaired gap searches, disputed relations and named records, after final fresh-copy proof and snapshot. Previously accepted scope remains accepted; step 3 waits for this repair acceptance.'
    write(path,inventory)
    md=A/'textbook-inventory.md';text=md.read_text()
    text=text.replace('**Bounded author inventory. Whole-book source analysis remains incomplete.** No sampling stop rule is claimed.',
        '**Author textbook population and analysis complete; independent acceptance pending.** No sampling stop rule was used. Every item is author-complete and awaiting independent check; exclusions and defects remain binding.')
    start=text.find('## Completion limits')
    assert start>=0
    text=text[:start]+'## Completion and acceptance boundary\n\n'+inventory['next_required']+'\n\n'+inventory['coverage']['exhaustive_definition']+'\n\nThe objective problem map records current practice support and relation limits. Radian interpretation has supporting teaching figures but no posed textbook question recorded; other unmatched exam tasks retain direct-search notes in textbook-gap-search-r7.json. No one-field or topic tag is an exhaustive gap verdict. A supporting drill or source-family membership does not certify a full examination demand.\n'
    md.write_text(text)
    print(json.dumps(dict(author_complete_items=len(inventory['items']),independently_accepted_items=0,source_envelope_pages=census['coverage']['pages_enumerated'],synthesis=synthesis['progress']),indent=2))
if __name__=='__main__':main()
