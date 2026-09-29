# -*- coding: utf-8 -*-
"""Write the 0500 structural exemplar: one small, complete, check-passing slice of topic 1.3.

    python3 exemplar_0500.py            # writes work/cie-0500-igcse-2024-2026/exemplar/
    python3 exemplar_0500.py --prove    # also installs it as topic 1.3 in a scratch copy and runs the suite

It shows the SHAPE an author copies: a claim ledger, two content units, flashcards, two tasks
answered from a practice text, and the text itself with its front matter. Its content is
original. It is not a topic's worth of material; the work orders set the real volume.
"""
import hashlib, json, os, shutil, subprocess, sys
HOME = os.path.expanduser('~')
REPO = os.path.join(HOME, 'mnt', 'YYeni Study Resources')
STD = os.path.join(REPO, 'standard', 'v0.2.0-draft')
WS = os.path.join(REPO, 'work', 'cie-0500-igcse-2024-2026')
EX = os.path.join(WS, 'exemplar')
sys.path.insert(0, os.path.join(STD, 'checks'))
from yyeni_checks import _artefact_text  # noqa: E402

O1, O2 = 'OBJ-0500-1.3.1-01', 'OBJ-0500-1.3.2-01'
TEXT_ID = 'TXT-0500-1.3-EX'
TEXT = '''---
text_id: TXT-0500-1.3-EX
title: The Week the Rain Came
genre: autobiographical prose
setting: Katutura, Windhoek
written_for: Paper 1 Text C-style practice (word-and-phrase items)
words_min: 500
words_max: 650
original: true
---
For three weeks in November the sky over Katutura had been making promises it did not keep. Every afternoon the clouds gathered above the Auas Mountains, swollen and grey, and every evening they drifted apart again as if they had changed their minds. My grandmother, who had lived through forty rainy seasons in the same small house, refused to be fooled. She would stand at the gate with her hands on her hips, study the sky for a long moment and then announce, "Not today," before going back inside to her sewing.

I was eleven that year and less patient. The heat pressed down on the street like a heavy blanket. Dust coated everything: the leaves of the single mopane tree in our yard, the windscreens of the taxis, the tops of our school shoes. Even the dogs had stopped chasing the delivery bicycles and lay flat in whatever shade they could find, their sides rising and falling slowly.

On the Thursday, something was different. The air grew thick and still, and the birds that usually quarrelled in the tree fell silent. My grandmother came out to the gate earlier than usual. She did not put her hands on her hips. Instead she lifted her face and sniffed, like someone trying to name a dish cooking in a neighbour's kitchen.

"Bring in the washing," she said quietly. It was not a request.

I had barely unpegged the last shirt when the wind arrived. It came racing down the street, snatching at plastic bags and flinging grit against the windows. Somewhere a door banged. Then there was a pause, a strange, held breath, and the first drops fell: fat, heavy drops that struck the dust and left dark coins wherever they landed. Within a minute the coins had joined together and the whole yard was dark and shining.

The smell came next. Anyone who has grown up in a dry country knows it: sharp and earthy and sweet all at once, the smell of ground that has been waiting too long. My grandmother closed her eyes and breathed it in. For a woman who rarely wasted words, she said a surprising thing. "That," she told me, "is the smell of the whole year changing its mind."

The storm lasted less than an hour. Water rushed along the gutters, carrying away a month of dust, and small brown rivers crossed the road where the taxis usually waited. Children from three houses down ran out barefoot, shrieking, and stamped in the puddles until their mothers called them back. I wanted to join them. My grandmother caught my sleeve and then, to my astonishment, let it go again.

By evening the clouds had moved on towards Rehoboth. The street steamed gently in the last of the light. The mopane leaves, washed clean, were a green I had forgotten they could be. My grandmother went back to her sewing as if nothing had happened, but I noticed that she was humming, and that the song she chose was one she normally saved for weddings.
'''

VER = {'status': 'unverified', 'method': 'Authored originally for the 0500 structural exemplar under standard v0.2.0-draft. Requires semantic review (RS-28).',
       'reviewer_id': None, 'reviewed_at': None, 'confidence': 0.9}
CLAIMS = [
 ('CLM-0500-1.3-001', [O2], 'The connotation of a word is the set of associations and feelings it carries beyond its literal, dictionary meaning.', 'definition'),
 ('CLM-0500-1.3-002', [O2], 'The meaning of a word in context is the sense it carries in the sentence where the writer uses it, which may differ from its most familiar dictionary sense.', 'definition'),
 ('CLM-0500-1.3-003', [O1], 'To find the word or phrase that carries a given idea, re-read the part of the text the question names, choose a candidate, and test it by putting it in place of the idea.', 'procedural'),
 ('CLM-0500-1.3-004', [O1], 'A word-or-phrase answer is the word or phrase itself; copying the surrounding sentence gives more than the task asks for and does not show which words carry the meaning.', 'misconception_correction'),
 ('CLM-0500-1.3-005', [O2], 'To explain a word in context, read the whole sentence, settle which sense the writer is using, and give an own-words equivalent that fits back into the sentence.', 'procedural'),
 ('CLM-0500-1.3-006', [O2], 'Guessing a meaning from the look or the root of a word, without checking the sentence, can produce a sense the writer did not intend.', 'misconception_correction'),
]


def stamp(x):
    x['claims_seen'] = {c: 1 for c in x.get('claim_ids', [])}
    x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
    return x


def block(bid, btype, heading, text, claims, aos):
    return stamp({'block_id': bid, 'block_type': btype, 'heading': heading, 'text': text, 'claim_ids': claims,
                  'context_tags': [], 'assessment_objectives': aos})


U1 = [
 block('1.3.1-b1', 'learner_objective', 'What this section covers', 'Find the exact word or phrase in a text that carries a given meaning.', [], ['AO1']),
 block('1.3.1-b2', 'plain_explanation', 'What the item asks for',
       'Some short questions on Text C, which is 500–650 words long, give you an idea in other words and ask you to find the word or phrase the writer used for it. The answer is short on purpose: a single word, or a phrase of a few words, taken straight from the text. You are not being asked to explain anything. You are being asked to point to the exact words that carry the idea.',
       [], ['AO1']),
 block('1.3.1-b3', 'process', 'How to find it',
       'Work in three steps. First, re-read only the part of the text the question names, because the answer sits there and a similar word elsewhere does not answer this question. Second, choose the word or phrase you think carries the idea. Third, test it: put your choice in place of the idea in the question and check that the meaning holds. If it does, write that word or phrase and nothing else.',
       ['CLM-0500-1.3-003'], ['AO1']),
 block('1.3.1-b4', 'worked_application', 'Worked example',
       'Take this sentence: "The old bus groaned up the hill, its engine protesting at each bend." Suppose the question asks for the word that shows the engine was complaining. "Groaned" is a sound, but it belongs to the bus. "Protesting" belongs to the engine and means objecting, which is a kind of complaint. Put it in place of the idea: the engine was complaining at each bend, the engine was protesting at each bend. The meaning holds, so the answer is "protesting".',
       ['CLM-0500-1.3-003'], ['AO1']),
 block('1.3.1-b5', 'misconception', 'Common errors',
       'The commonest error is copying out the whole sentence. A word-or-phrase answer is the word or phrase itself, and copying the sentence around it gives more than the task asks for without showing which words carry the meaning. The substitution test catches this: a sentence cannot be put in place of an idea, but the right word can.',
       ['CLM-0500-1.3-004'], ['AO1']),
]
U2 = [
 block('1.3.2-b1', 'learner_objective', 'What this section covers', 'Explain in your own words what a word means in the sentence where the writer uses it.', [], ['AO1']),
 block('1.3.2-b2', 'definition', 'Meaning in context, and connotation',
       'Many English words have more than one sense. The meaning of a word in context is the sense it carries in the sentence where the writer uses it, and that may not be the sense you know best. "Hungry" is about food in "a hungry child", but in "the farmers watched the sky with a hungry patience" it means longing: they want rain the way a hungry person wants food. That extra layer is connotation, the associations and feelings a word carries beyond its literal, dictionary meaning.',
       ['CLM-0500-1.3-002', 'CLM-0500-1.3-001'], ['AO1']),
 block('1.3.2-b3', 'process', 'How to explain a word',
       'Read the whole sentence, not just the word. Decide which sense the writer is using, because the sentence settles it. Then give an equivalent in your own words that could fit back into the sentence. If you can drop your explanation into the writer’s sentence and it still makes sense, it is very likely right.',
       ['CLM-0500-1.3-005'], ['AO1']),
 block('1.3.2-b4', 'worked_application', 'Worked example',
       'In "the crowd grew restless as the speeches went on", what does "restless" mean? Reading the sentence tells you the crowd has been kept waiting. "Restless" here means impatient and unable to keep still. Test it: the crowd grew impatient and fidgety as the speeches went on. It fits.',
       ['CLM-0500-1.3-005', 'CLM-0500-1.3-002'], ['AO1']),
 block('1.3.2-b5', 'misconception', 'Common errors',
       'A common mistake is to guess from the look of a word. "Restless" contains "rest", so a learner may write that the crowd had not rested. Guessing a meaning from the look or the root of a word, without checking the sentence, can produce a sense the writer did not intend. The fix is the same check as before: put your meaning back into the sentence and see whether it still makes sense there.',
       ['CLM-0500-1.3-006'], ['AO1']),
]


def unit(uid, title, objs, blocks):
    wc = sum(len((b['heading'] + ' ' + b['text']).split()) for b in blocks)
    return {'unit_id': uid, 'title': title, 'objective_ids': objs, 'level': 'IGCSE', 'core_status': 'core',
            'objective_type': 'reading_skill', 'depth_tier': 2,
            'word_budget': {'min': wc - 20, 'target': wc, 'max': wc + 400}, 'blocks': blocks, 'word_count': wc,
            'qa_status': 'review_required',
            'notes': ['Structural exemplar. Take its shape, not its length: your word budget is in the work order.']}


CTX = lambda tid=None: dict({'sector': None, 'business_size': None, 'ownership': None, 'situation': None, 'facts': []},
                            **({'text_id': tid} if tid else {}))


def item(iid, objs, claims, itype, st, subs, cw, tar, diff, bloom, prompt, answer, guidance, tid=None):
    return stamp({'item_id': iid, 'objective_ids': objs, 'claim_ids': claims, 'item_type': itype, 'subtype': st,
                  'assessment_objectives': ['AO1'], 'sub_objectives': subs, 'blooms_level': bloom,
                  'command_word': cw, 'mark_tariff': tar, 'difficulty': diff, 'prompt': prompt,
                  'canonical_answer': answer, 'marking_guidance': guidance, 'context': CTX(tid),
                  'prerequisite_item_ids': [], 'core_status': 'core', 'intentional_duplicate_group': None,
                  'provenance': 'Authored for the 0500 structural exemplar from the topic 1.3 claim ledger.',
                  'qa_status': 'review_required'})


ITEMS = [
 item('ITEM-0500-1.3-EX1-DEF', [O2], ['CLM-0500-1.3-001'], 'flashcard', 'DEF', ['R1', 'R2'], None, None, 1, 'Remember',
      'What is the connotation of a word?',
      'The connotation of a word is the set of associations and feelings it carries beyond its literal, dictionary meaning. "House" and "home" can name the same building, but "home" carries warmth and belonging.',
      ['Credit the meaning: associations and feelings beyond the literal sense.', 'An example on its own is not a definition.']),
 item('ITEM-0500-1.3-EX2-APP', [O1], ['CLM-0500-1.3-003'], 'flashcard', 'APP', ['R1'], 'Identify', 1, 3, 'Apply',
      'Read this sentence: "The old bus groaned up the hill, its engine protesting at each bend." Identify the word that shows the engine was complaining.',
      'protesting',
      ['1 mark for "protesting" only.', '"Groaned" is a sound, but it belongs to the bus, not the engine, so it does not answer the question because the question names the engine.', 'Do not credit the whole sentence.']),
 item('ITEM-0500-1.3-EX3-APP', [O2], ['CLM-0500-1.3-005', 'CLM-0500-1.3-002'], 'flashcard', 'APP', ['R1', 'R2'], 'Explain', 1, 3, 'Apply',
      'In the sentence "After the long drought the farmers watched the sky with a hungry patience", explain in your own words what "hungry" means as it is used here.',
      'It means eager or longing: the farmers badly want the rain to come, the way a hungry person wants food. It does not mean they want to eat.',
      ['1 mark for an own-words meaning such as eager, longing or desperate for rain.', 'The sentence shows it is rain they want, so the literal sense of wanting food is not credited.']),
 item('ITEM-0500-1.3-EX4-MISCON', [O1], ['CLM-0500-1.3-004'], 'flashcard', 'MISCON', ['R1'], None, None, 3, 'Understand',
      'A learner is asked for the word in a sentence that means "very tired", and copies out the whole sentence. What is wrong with the answer, and what should they have done?',
      'The error is giving the whole sentence instead of the single word or phrase the task asks for. A word-or-phrase answer should be something you could put in place of the given idea, and a sentence cannot be put in its place. They should have found the one word, such as "exhausted", and written only that.',
      ['Must name the error: the whole sentence copied instead of the word.', 'Must give the substitution test that tells a word-or-phrase answer from a copied sentence.']),
 item('ITEM-0500-1.3-EX5-MISCON', [O2], ['CLM-0500-1.3-006', 'CLM-0500-1.3-002'], 'flashcard', 'MISCON', ['R1', 'R2'], None, None, 3, 'Understand',
      'A learner writes that "the crowd grew restless" means the crowd had not rested, because "restless" contains "rest". What is the mistake, and how could they check their answer?',
      'The mistake is taking the meaning from how the word looks instead of from the sentence it is in. In this sentence "restless" means impatient and unable to keep still. The check is to put the meaning back into the sentence: "the crowd grew impatient" fits a crowd kept waiting, while "the crowd had not rested" does not.',
      ['Must name the mistake: meaning taken from the look or root of the word, not its context.', 'Must give the check: the meaning put back into the sentence.']),
 item('ITEM-0500-1.3-EX-P01', [O1], ['CLM-0500-1.3-003'], 'short_answer', None, ['R1'], 'Identify', 1, 2, 'Understand',
      'Re-read the first paragraph of "The Week the Rain Came". Identify the word that tells you the clouds were full of rain.',
      'swollen',
      ['1 mark for "swollen".', 'Do not credit "grey" or "gathered": they describe the colour and the movement of the clouds in the text, not how full they are.', 'Do not credit the whole sentence.'], tid=TEXT_ID),
 item('ITEM-0500-1.3-EX-P02', [O2], ['CLM-0500-1.3-005'], 'short_answer', None, ['R1', 'R2'], 'Explain', 1, 2, 'Understand',
      'Explain, in your own words, what "astonishment" means as it is used in the seventh paragraph of "The Week the Rain Came".',
      'Great surprise. The narrator is amazed that the grandmother lets go of the sleeve after catching it.',
      ['1 mark for an own-words meaning such as great surprise or amazement.', 'Do not credit "astonished" or any form of the word itself.', 'Do not credit "confusion": the sentence in the text shows surprise at the grandmother changing her mind, not uncertainty.'], tid=TEXT_ID),
]


def write(root):
    os.makedirs(os.path.join(root, 'claims'), exist_ok=True)
    os.makedirs(os.path.join(root, 'content-units'), exist_ok=True)
    os.makedirs(os.path.join(root, 'learning-items'), exist_ok=True)
    os.makedirs(os.path.join(root, 'texts'), exist_ok=True)
    led = {'ledger_id': 'CLM-LEDGER-0500-IGCSE-1.3', 'claims': [
        {'claim_id': c, 'objective_ids': o, 'text': t, 'claim_type': k, 'provenance': 'generated_gap', 'evidence': [],
         'derived_from_claim_ids': [], 'revision': 1, 'verification': VER, 'publishable': False, 'notes': []}
        for c, o, t, k in CLAIMS]}
    json.dump(led, open(os.path.join(root, 'claims', 'canonical_claim_ledger.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(unit('CU-0500-1.3.1', 'Finding the word or phrase', [O1], U1),
              open(os.path.join(root, 'content-units', 'CU-0500-1.3.1.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(unit('CU-0500-1.3.2', 'Explaining a word in its context', [O2], U2),
              open(os.path.join(root, 'content-units', 'CU-0500-1.3.2.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump({'dataset_id': 'ITEMS-0500-1.3', 'topic_id': '1.3', 'items': ITEMS},
              open(os.path.join(root, 'learning-items', 'topic_1.3_items.json'), 'w'), indent=1, ensure_ascii=False)
    open(os.path.join(root, 'texts', TEXT_ID + '.md'), 'w').write(TEXT)


write(EX)
open(os.path.join(EX, 'README.md'), 'w').write(
    '# 0500 structural exemplar\n\nA small, complete slice of topic 1.3 that passes the full check suite. Copy its '
    '**shape**: the field set of every claim, block and item; how a task names its practice text with '
    '`context.text_id`; the front matter of a text; how `claims_seen` and `authored_hash` are set. Do not copy its '
    'volume (the work orders set that) or its content (write your own).\n\nProof: `python3 '
    'standard/v0.2.0-draft/mine/exemplar_0500.py --prove` installs it as topic 1.3 in a scratch copy of the '
    'workspace and runs the suite.\n')
print('exemplar written: %d claims, %d blocks, %d items, 1 text (%d words)'
      % (len(CLAIMS), len(U1) + len(U2), len(ITEMS), len(TEXT.split('---', 2)[2].split())))

if '--prove' in sys.argv:
    scratch = os.path.join(HOME, 'ex0500', 'cie-0500-igcse-2024-2026')
    if os.path.exists(os.path.dirname(scratch)):
        shutil.rmtree(os.path.dirname(scratch))
    shutil.copytree(WS, scratch, ignore=shutil.ignore_patterns('exemplar'))
    td = os.path.join(scratch, 'topics', '1.3')
    write(td)
    c = json.load(open(os.path.join(td, 'contract.json')))
    c['depth_constraints']['item_budget'] = len(ITEMS)
    c['required_outputs']['learning_items'] = len(ITEMS)
    c['required_outputs']['content_units'] = 2
    json.dump(c, open(os.path.join(td, 'contract.json'), 'w'), indent=1, ensure_ascii=False)
    subprocess.run([sys.executable, os.path.join(STD, 'build', 'render_notes.py'), scratch, '1.3'], check=True)
    r = subprocess.run([sys.executable, os.path.join(STD, 'checks', 'run_checks.py'), scratch, '1.3',
                        '--out', os.path.join(td, 'qa_report.json')], capture_output=True, text=True)
    print(r.stdout)
