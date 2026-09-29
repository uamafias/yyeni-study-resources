# -*- coding: utf-8 -*-
"""Write the 9093 structural exemplar: one small, complete, check-passing slice of topic 1.5 (text analysis).

    python3 exemplar_9093.py            # writes work/cie-9093-as-2024-2026/exemplar/
    python3 exemplar_9093.py --prove    # also installs it as topic 1.5 in a scratch copy and runs the suite

It shows the SHAPE an author copies: a claim ledger, two content units, flashcards, a Question 2-style task
answered from a practice text, and the text itself with its front matter. Its content is original. It is not a
topic's worth of material; the work orders set the real volume.
"""
import hashlib, json, os, shutil, subprocess, sys
HOME = os.path.expanduser('~')
REPO = os.path.join(HOME, 'mnt', 'YYeni Study Resources')
STD = os.path.join(REPO, 'standard', 'v0.2.0-draft')
WS = os.path.join(REPO, 'work', 'cie-9093-as-2024-2026')
EX = os.path.join(WS, 'exemplar')
sys.path.insert(0, os.path.join(STD, 'checks'))
from yyeni_checks import _artefact_text  # noqa: E402

REG = {o['sub_topic'] + o['syllabus_text'][:12]: o['objective_id'] for o in
       json.load(open(os.path.join(WS, 'curriculum', 'objective_registry.json')))['objectives'] if o.get('parent_id')}
O_A, O_B = 'OBJ-9093-1.5.1-01', 'OBJ-9093-1.5.1-02'
O_C, O_D, O_E = 'OBJ-9093-1.5.2-01', 'OBJ-9093-1.5.2-02', 'OBJ-9093-1.5.2-03'
O_F, O_G = 'OBJ-9093-1.5.3-01', 'OBJ-9093-1.5.3-02'
TEXT_ID = 'TXT-9093-1.5-EX'
TEXT = '''---
text_id: TXT-9093-1.5-EX
title: Drinking the Fog
genre: magazine feature article
setting: the Namib coast
written_for: Paper 1 Question 2-style practice (text analysis)
words_min: 550
words_max: 750
original: true
---
DRINKING THE FOG

On the driest coast on Earth, the water arrives sideways. Our science writer spent a week with the people, and the beetles, who have learned to catch it.

At four in the morning the Namib is silent and cold, and the dunes are the colour of weak tea. Then the fog comes. It rolls in off the Atlantic like a slow grey tide, swallowing the ridges one by one, and for three hours the desert is wet. By nine it has gone. The sand is dry again, the sky is a hard, bright blue, and you would never guess that anything had happened at all.

Something has happened, though. On the crest of a dune near Gobabeb, a beetle no longer than a thumbnail has been standing on its head. Tilted into the wind, its back to the sea, it lets the fog settle on the bumps of its shell. The droplets grow, merge and roll down a groove towards its mouth. It is drinking the weather.

"People laugh when I say a beetle taught me engineering," says Dr Selma Nangolo, who has studied fog in the Namib for eleven years. "But she is the best engineer I know. She has had four million years to get it right."

Rain here is a rumour. Some years it does not come at all; in a good year it might leave less than twenty millimetres. Fog is different. It visits on as many as a hundred mornings a year, and it carries enough water to keep lichens, grasses and a whole community of animals alive. The question that has occupied Dr Nangolo's team is simple to ask and hard to answer: if a beetle can harvest it, why can't we?

The answer, it turns out, is that we can, if we are patient. On a ridge above the research station stand six rectangles of black mesh, each the size of a garage door. They look like tennis nets that have wandered into the desert and lost their way. When the fog passes through them, tiny drops catch on the threads, run together and trickle into a gutter below. On a good morning a single net collects around forty litres.

Forty litres does not sound like much. It is not much, if you have a tap. It is a great deal if the nearest tap is sixty kilometres away across gravel plains. The team is now working with a school in the settlement of Utuseb, where two nets supply water for the vegetable garden. The pupils read the gauges each morning and record the results on a chart by the classroom door.

There are problems, and Dr Nangolo is quick to list them. Nets tear in the strong afternoon winds. Dust clogs the mesh. And fog, unlike a borehole, cannot be switched on. "You cannot build a town on this," she admits. "But you can grow spinach. You can give a school garden a future. That matters."

Her newest design copies the beetle more closely. Instead of flat mesh, the threads are coated in a pattern of water-loving bumps on a water-repelling surface, exactly the arrangement on the beetle's back. Early trials suggest the coated nets collect almost half as much again.

Back on the dune, the sun is climbing and the beetle has gone, burrowed into the cool sand to wait for tomorrow. Below it, in Utuseb, a boy is lifting the lid of the water tank to see how much the night has left. It is not a miracle. It is something better: a small, reliable gift, delivered on the wind, to anyone who has learned how to catch it.
'''

VER = {'status': 'unverified', 'method': 'Authored originally for the 9093 structural exemplar under standard v0.2.0-draft. Requires semantic review (RS-28).',
       'reviewer_id': None, 'reviewed_at': None, 'confidence': 0.9}
CLAIMS = [
 ('CLM-9093-1.5-001', [O_E], 'An effect is what a writer’s choice leads the reader to think, feel or do at that point in the text.', 'definition'),
 ('CLM-9093-1.5-002', [O_E], 'An analytical point moves from the feature to the evidence (the exact words), then to the effect on this reader, then to how that effect serves the text’s purpose.', 'procedural'),
 ('CLM-9093-1.5-003', [O_D], 'Several choices can work together towards one effect, so an analysis is strongest when it shows how a structural choice and a language choice support each other.', 'causal'),
 ('CLM-9093-1.5-004', [O_E], 'Naming a device or a sentence type is not analysis; the point is made only when the writer says what the choice does for this reader.', 'misconception_correction'),
 ('CLM-9093-1.5-005', [O_C], 'Retelling what a text says is summary; analysis is about how the writer’s decisions about form, structure and language make that content land with its audience.', 'misconception_correction'),
 ('CLM-9093-1.5-006', [O_A], 'A text analysis opens by fixing the text’s form, audience, purpose and context, because every feature is later judged by what it does for them.', 'procedural'),
 ('CLM-9093-1.5-007', [O_B], 'A text’s overall style is the manner its choices produce together; it is characterised in a few precise words and then proved through specific examples.', 'definition'),
 ('CLM-9093-1.5-008', [O_A], 'Feature articles for a general magazine readership often combine a narrative frame, expert voices and explanation, so that information arrives through a story.', 'factual'),
 ('CLM-9093-1.5-009', [O_F], 'An analysis organised by effect or purpose builds an argument about the whole text; one that follows the order of the text’s paragraphs tends to become a commentary on each in turn.', 'comparison'),
 ('CLM-9093-1.5-010', [O_G], 'The analytical register is formal and precise: it discusses the writer’s choices in the present tense, names features with exact terms, and avoids chatty asides.', 'definition'),
 ('CLM-9093-1.5-011', [O_A], 'Analysis is about how a text is written; agreeing or disagreeing with its subject, or explaining the subject further, answers a different question.', 'misconception_correction'),
 ('CLM-9093-1.5-012', [O_B], 'A claim about a text’s overall style counts only when specific choices prove it; general adjectives with no example leave the claim unsupported.', 'misconception_correction'),
]


def stamp(x):
    x['claims_seen'] = {c: 1 for c in x.get('claim_ids', [])}
    x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
    return x


def block(bid, btype, heading, text, claims, aos):
    return stamp({'block_id': bid, 'block_type': btype, 'heading': heading, 'text': text, 'claim_ids': claims,
                  'context_tags': [], 'assessment_objectives': aos})


U1 = [
 block('1.5.1-b1', 'learner_objective', 'What this section covers',
       'Identify a text’s characteristic features and relate each to its meaning, context and audience; characterise its overall style and prove it through specific language choices.', [], ['AO1', 'AO3']),
 block('1.5.1-b2', 'process', 'The opening move',
       'Before you look for a single feature, fix four things: the form of the text, who it is for, what it sets out to do, and the situation it comes from. A text analysis opens by fixing the text’s form, audience, purpose and context, because every feature you discuss later is judged by what it does for them. Write this as one or two sentences at the start of your answer, and end it with the overall effect the text has on its reader.',
       ['CLM-9093-1.5-006'], ['AO1', 'AO3']),
 block('1.5.1-b3', 'definition', 'Style',
       'A text’s overall style is the manner its choices produce together. You characterise it in a few precise words (wry and conversational; urgent and formal) and then prove it through specific examples. Tone is part of style but not the whole of it: tone is the attitude, style is the whole manner, including sentence patterns, vocabulary and structure.',
       ['CLM-9093-1.5-007'], ['AO1', 'AO3']),
 block('1.5.1-b4', 'worked_application', 'Worked example',
       'Take this opening, written for the purpose: "Nobody warns you that the hardest part of running a marathon is the week before it." The form is a first-person column, the audience is general readers who may never have run one, and the purpose is to entertain as much as inform. The overall style is confiding and wry: "Nobody warns you" draws the reader into a shared secret, and the joke lies in placing the difficulty before the race rather than in it. An opening sentence of analysis could say: the column adopts a confiding, wry style to make an endurance event feel familiar to readers who have never run one.',
       ['CLM-9093-1.5-006', 'CLM-9093-1.5-007'], ['AO1', 'AO3']),
 block('1.5.1-b5', 'plain_explanation', 'Feature articles',
       'Feature articles for a general magazine readership often combine a narrative frame, expert voices and explanation, so that information arrives through a story. When you meet one, look for where the story frame opens and closes, whose voices are quoted, and where the explanation sits between them.',
       ['CLM-9093-1.5-008'], ['AO1']),
 block('1.5.1-b6', 'misconception', 'Two ways to miss the whole',
       'Analysis is about how a text is written; agreeing or disagreeing with its subject, or explaining the subject further, answers a different question. If a sentence of your answer would still make sense in an essay about fog harvesting, it is about the topic, not the text. The second risk is an unproved claim about style: a claim about a text’s overall style counts only when specific choices prove it, so every adjective you use for the style needs at least one quotation behind it.',
       ['CLM-9093-1.5-011', 'CLM-9093-1.5-012'], ['AO1', 'AO3']),
]
U2 = [
 block('1.5.2-b1', 'learner_objective', 'What this section covers',
       'Analyse form, structure and language and how they work together; show how several choices combine to create one effect; write precisely about effects.', [], ['AO3']),
 block('1.5.2-b2', 'definition', 'Effect',
       'An effect is what a writer’s choice leads the reader to think, feel or do at that point in the text. It is not the same as the meaning of the words. "The water arrives sideways" means that it comes as fog; its effect is to surprise the reader into reading on, because water is not supposed to arrive that way.',
       ['CLM-9093-1.5-001'], ['AO3']),
 block('1.5.2-b3', 'process', 'The analytical sequence',
       'An analytical point moves from the feature to the evidence (the exact words), then to the effect on this reader, then to how that effect serves the text’s purpose. Write the four moves in that order until they become habit: name the choice, quote the few words that carry it, say what it makes this reader think or feel, and connect that to what the text is for.',
       ['CLM-9093-1.5-002'], ['AO3']),
 block('1.5.2-b4', 'analysis_chain', 'Choices that work together',
       'Several choices can work together towards one effect, so an analysis is strongest when it shows how a structural choice and a language choice support each other. A text that opens and closes in the same place (a structural choice) and uses the same image in both (a language choice) can make its ending feel like an arrival rather than a stop. Point to both, and say what they achieve together.',
       ['CLM-9093-1.5-003'], ['AO3']),
 block('1.5.2-b5', 'misconception', 'Two ways to lose the marks',
       'Naming a device or a sentence type is not analysis; the point is made only when the writer says what the choice does for this reader. Delete the name of the device from your sentence: if nothing about meaning or effect is left, nothing was analysed. The second error is summary. Retelling what a text says is summary; analysis is about how the writer’s decisions about form, structure and language make that content land with its audience.',
       ['CLM-9093-1.5-004', 'CLM-9093-1.5-005'], ['AO3']),
]
U3 = [
 block('1.5.3-b1', 'learner_objective', 'What this section covers',
       'Organise an analysis around the text’s purpose and effect, not the order of its paragraphs, and write it in a formal, precise analytical register.', [], ['AO3']),
 block('1.5.3-b2', 'comparison', 'Organising by effect',
       'An analysis organised by effect or purpose builds an argument about the whole text; one that follows the order of the text’s paragraphs tends to become a commentary on each in turn. Plan by effect first: decide the two or three things the text does to its reader, and give each a section that gathers evidence from wherever it occurs.',
       ['CLM-9093-1.5-009'], ['AO3']),
 block('1.5.3-b3', 'definition', 'The analytical register',
       'The analytical register is formal and precise: it discusses the writer’s choices in the present tense, names features with exact terms, and avoids chatty asides. “The writer personifies rain as a rumour” is in the register; “I think this bit is really clever” is not.',
       ['CLM-9093-1.5-010'], ['AO3']),
 block('1.5.3-b4', 'misconception', 'The walkthrough',
       'The commonest organising error is the walkthrough: “In the first paragraph… in the second paragraph…”. It follows the text instead of arguing about it, so points about the same effect end up far apart. The test is to read the first sentence of each of your paragraphs in turn; together they should state a view of the whole text.',
       ['CLM-9093-1.5-009'], ['AO3']),
]


def unit(uid, title, objs, blocks):
    wc = sum(len((b['heading'] + ' ' + b['text']).split()) for b in blocks)
    return {'unit_id': uid, 'title': title, 'objective_ids': objs, 'level': 'AS', 'core_status': 'core',
            'objective_type': 'reading_and_analysis', 'depth_tier': 3,
            'word_budget': {'min': wc - 20, 'target': wc, 'max': wc + 400}, 'blocks': blocks, 'word_count': wc,
            'qa_status': 'review_required',
            'notes': ['Structural exemplar. Take its shape, not its length: your word budget is in the work order.']}


CTX = lambda tid=None: dict({'sector': None, 'business_size': None, 'ownership': None, 'situation': None, 'facts': []},
                            **({'text_id': tid} if tid else {}))


def item(iid, objs, claims, itype, st, aos, cw, tar, diff, bloom, prompt, answer, guidance, tid=None):
    return stamp({'item_id': iid, 'objective_ids': objs, 'claim_ids': claims, 'item_type': itype, 'subtype': st,
                  'assessment_objectives': aos, 'blooms_level': bloom,
                  'command_word': cw, 'mark_tariff': tar, 'difficulty': diff, 'prompt': prompt,
                  'canonical_answer': answer, 'marking_guidance': guidance, 'context': CTX(tid),
                  'prerequisite_item_ids': [], 'core_status': 'core', 'intentional_duplicate_group': None,
                  'provenance': 'Authored for the 9093 structural exemplar from the topic 1.5 claim ledger.',
                  'qa_status': 'review_required'})


MODEL = (
 '“Drinking the Fog” is a magazine feature article for general readers with an interest in science, and its purpose is to inform '
 'them about fog harvesting while making them care about it. Its style is vivid and conversational, and it delivers its '
 'information through a story that begins and ends on the same dune.\n\n'
 'The form is signalled at once. The headline, “DRINKING THE FOG”, is a paradox that makes the reader ask how fog can be drunk, '
 'and the standfirst answers only half the question: water “arrives sideways”. Withholding the explanation turns the article’s '
 'information into a mystery the reader wants solved, which suits a magazine reader who has chosen to read for interest rather '
 'than need.\n\n'
 'Structurally, the article is framed by a narrative. It opens at “four in the morning” with the fog arriving and closes with “the '
 'sun climbing” and the beetle gone, so the whole piece follows one desert morning. Inside that frame the writer alternates '
 'scene, expert voice and explanation. Dr Nangolo’s quoted words give the science authority, but because she speaks in a '
 'relaxed, humorous way (“People laugh when I say a beetle taught me engineering”) the authority never becomes remote. The '
 'frame and the voices work together: the reader learns the engineering inside a story, not a lecture.\n\n'
 'The language builds a contrast between scarcity and plenty. Rain is personified as “a rumour”, a single noun that makes '
 'rain sound unreliable and half-imagined, whereas fog “visits”, a verb that suggests a regular, almost friendly caller. The '
 'semantic field of engineering (“harvest”, “gutter”, “design”, “coated”) is applied to a beetle, which raises the insect '
 'to the status of an expert and prepares the reader for the article’s central idea that the animal is the model for the machine.\n\n'
 'Similes make the unfamiliar concrete for readers who have never seen the Namib: the fog rolls in “like a slow grey tide” and '
 'the nets “look like tennis nets that have wandered into the desert”. The second image is gently comic, and its humour keeps '
 'the tone warm at the point where the article turns technical.\n\n'
 'Short sentences are used for emphasis where the argument turns. After a long description of the nets, “Forty litres does '
 'not sound like much.” stands out by contrast, and the repetition that follows (“It is not much, if you have a tap. It is a '
 'great deal if…”) forces the reader to re-measure the figure against life sixty kilometres from a tap.\n\n'
 'The ending returns to the opening image and resolves it. The final sentence moves from “miracle” to “something better”, and '
 'the phrase “a small, reliable gift, delivered on the wind” gathers the article’s contrast into one line: what seemed like '
 'nothing becomes something the reader can value. The cyclical structure and the closing image together leave the reader with '
 'the article’s purpose achieved: informed about fog harvesting, and persuaded that small solutions matter.')
ITEMS = [
 item('ITEM-9093-1.5-EX1-DEF', [O_E], ['CLM-9093-1.5-001'], 'flashcard', 'DEF', ['AO3'], None, None, 1, 'Remember',
      'In text analysis, what is an effect?',
      'An effect is what a writer’s choice leads the reader to think, feel or do at that point in the text. It is different from what the words mean: a phrase can mean one thing and have the effect of surprising, reassuring or unsettling the reader.',
      ['Credit the meaning: what the choice makes the reader think, feel or do.', 'An answer that gives only what the words mean has not defined effect.']),
 item('ITEM-9093-1.5-EX2-PROC', [O_E], ['CLM-9093-1.5-002'], 'flashcard', 'PROC', ['AO3'], None, None, 2, 'Remember',
      'What are the four moves of an analytical point, in order?',
      'First name the feature; then quote the evidence, the exact few words that carry it; then state the effect on this reader; then link that effect to the text’s purpose.',
      ['All four steps are needed, in this order: feature, evidence, effect, link to purpose.', 'An answer that stops at the evidence has left out the analysis.']),
 item('ITEM-9093-1.5-EX3-MECH', [O_E], ['CLM-9093-1.5-001', 'CLM-9093-1.5-002'], 'flashcard', 'MECH', ['AO3'], None, None, 3, 'Analyse',
      'Read this sentence, written for the purpose: “Rain here is a rumour.” How does the choice of the noun “rumour” shape the reader’s view of rain in this place?',
      'The noun treats rain as talk rather than fact: something people mention but cannot rely on. It suggests that rain is so rare it is half-believed, so the reader grasps the dryness of the place without being given a figure.',
      ['Must name the effect on the reader: rain made to seem unreliable or half-imagined.', 'Must point to the word “rumour” as the evidence, and say what it suggests beyond its literal meaning.']),
 item('ITEM-9093-1.5-EX4-MISCON', [O_E], ['CLM-9093-1.5-004'], 'flashcard', 'MISCON', ['AO3'], None, None, 3, 'Understand',
      'A learner writes: “The writer uses a simile, a short sentence and a rhetorical question.” What is wrong with this as analysis, and how can they test their own sentences?',
      'The error is feature-spotting: the learner names three devices and says nothing about what any of them does for the reader. The test is to delete the device names from the sentence; if nothing about meaning or effect is left, nothing was analysed. Instead they should quote each choice and say what it leads this reader to think or feel.',
      ['Must name the error: devices named without their effect.', 'Must give the deletion test, or an equivalent that separates naming from analysing.']),
 item('ITEM-9093-1.5-EX5-MISCON', [O_C], ['CLM-9093-1.5-005'], 'flashcard', 'MISCON', ['AO3'], None, None, 3, 'Understand',
      'A learner’s answer on an article about fog nets says: “The writer explains that the nets collect forty litres, which helps a school garden.” Why is this summary rather than analysis?',
      'The sentence only reports what the article says, so it is summary. It says nothing about how the writer presents the figure. An analytical sentence would instead point to the choices, for example the short sentence that plays the figure down before the next sentences re-measure it, and say what that does to the reader’s sense of its value.',
      ['Must name the error: content retold instead of choices analysed.', 'Must show the change needed: a choice of form, structure or language, with its effect.']),
 item('ITEM-9093-1.5-EX6-DIST', [O_B], ['CLM-9093-1.5-007'], 'flashcard', 'DIST', ['AO1', 'AO3'], None, None, 2, 'Understand',
      'What is the difference between a text’s style and its tone, and how can you tell them apart?',
      'Tone is the attitude a text conveys towards its subject or reader, such as warm or urgent. Style is the whole manner the choices produce together, including sentence patterns, vocabulary and structure, of which tone is one part. The test: tone answers “what attitude?”, style answers “what manner of writing, and made of which choices?”.',
      ['Must distinguish attitude (tone) from the whole manner of writing (style).', 'Must give a test or example that separates them.']),
 item('ITEM-9093-1.5-EX7-MISCON', [O_A], ['CLM-9093-1.5-011'], 'flashcard', 'MISCON', ['AO1', 'AO3'], None, None, 3, 'Understand',
      'In an answer on an article about fog nets, a learner writes: “Fog harvesting is a brilliant idea and every dry country should use it.” What has gone wrong, and how can the learner check for it?',
      'The error is responding to the topic instead of analysing the writing: the sentence gives the learner’s opinion of fog harvesting and says nothing about the writer’s choices. The check is to ask whether the sentence would still fit an essay about the subject; if it would, it is not analysis of this text.',
      ['Must name the error: an opinion on the topic instead of analysis of the writing.', 'Must give a test that separates the two.']),
 item('ITEM-9093-1.5-EX8-MISCON', [O_B], ['CLM-9093-1.5-012'], 'flashcard', 'MISCON', ['AO1', 'AO3'], None, None, 3, 'Understand',
      'A learner opens an analysis with: “The style is lively, engaging and effective.” and never returns to it. What is the mistake, and what should replace it?',
      'The mistake is an unproved claim about style: three general adjectives with no choice from the text behind them. Instead of stopping there, the learner should use one or two precise words for the style and prove each with a specific choice, for example the conversational expert quotations that make the article lively.',
      ['Must name the mistake: a style claim with no evidence.', 'Must show the fix: precise description proved by specific choices.']),
 item('ITEM-9093-1.5-EX9-MISCON', [O_F], ['CLM-9093-1.5-009'], 'flashcard', 'MISCON', ['AO3'], None, None, 3, 'Understand',
      'A learner’s analysis has five paragraphs that begin “In the first paragraph…”, “In the second paragraph…” and so on. What is the problem, and how can they test a plan before writing?',
      'The error is a walkthrough: the answer follows the order of the text instead of arguing about it, so points about the same effect are scattered. The test is to read the first sentence of each paragraph in turn; together they should state a view of the whole text. A better plan groups evidence by effect, instead of by paragraph.',
      ['Must name the error: organised by paragraph order, not by effect.', 'Must give the test: the paragraph openings should state an argument.']),
 item('ITEM-9093-1.5-EX10-FEATURE', [O_G], ['CLM-9093-1.5-010'], 'flashcard', 'FEATURE', ['AO3'], None, None, 2, 'Remember',
      'What features mark the analytical register an analysis should be written in?',
      'It is shaped by the purpose of an analysis and its reader, who is weighing an argument about a text: so it is formal and precise, discusses the writer’s choices in the present tense, names features with exact terms, keeps to the third person, and avoids chatty asides such as “I think this bit is clever”.',
      ['Credit at least three of the features: formal, present tense, exact terms, no chatty asides.', 'An answer about the text’s own register, not the analysis, has misread the question.']),
 item('ITEM-9093-1.5-EX-P01', [O_A, O_B, O_C, O_D, O_E, O_F, O_G], ['CLM-9093-1.5-002', 'CLM-9093-1.5-003', 'CLM-9093-1.5-005', 'CLM-9093-1.5-006', 'CLM-9093-1.5-007', 'CLM-9093-1.5-009', 'CLM-9093-1.5-010'],
      'source_analysis', None, ['AO1', 'AO3'], 'Analyse', 25, 5, 'Analyse',
      'Read “Drinking the Fog”, a feature article from a general-interest science magazine. Analyse how its writer uses form, structure and language to inform readers about fog harvesting and make them care about it. [25]',
      MODEL,
      ['Mark against both columns of the 25-mark table in curriculum/answer-shapes.json (P1-Q2): reading out of 5, analysis out of 20.',
       'Reading (AO1): credit a clear statement of the text’s form, audience and purpose and a secure grasp of its meaning; the model answer sits at the top level.',
       'Analysis (AO3): credit form (headline, standfirst, expert voice), structure (the morning frame, the alternation of scene and explanation, the cyclical ending) and language (personification, semantic field, similes, sentence length), each with a short quotation and its effect on this audience.',
       'The model answer reaches the top levels because its points are organised by effect rather than by paragraph order, and each quotation is analysed for its meaning and effect.',
       'Do not credit summary of the article’s content, or devices named without what they do.'], tid=TEXT_ID),
]


def write(root):
    for d in ('claims', 'content-units', 'learning-items', 'texts'):
        os.makedirs(os.path.join(root, d), exist_ok=True)
    led = {'ledger_id': 'CLM-LEDGER-9093-AS-1.5', 'claims': [
        {'claim_id': c, 'objective_ids': o, 'text': t, 'claim_type': k, 'provenance': 'generated_gap', 'evidence': [],
         'derived_from_claim_ids': [], 'revision': 1, 'verification': VER, 'publishable': False, 'notes': []}
        for c, o, t, k in CLAIMS]}
    json.dump(led, open(os.path.join(root, 'claims', 'canonical_claim_ledger.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(unit('CU-9093-1.5.1', 'Reading the text as a whole', [O_A, O_B], U1),
              open(os.path.join(root, 'content-units', 'CU-9093-1.5.1.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(unit('CU-9093-1.5.2', 'Analysing form, structure and language', [O_C, O_D, O_E], U2),
              open(os.path.join(root, 'content-units', 'CU-9093-1.5.2.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(unit('CU-9093-1.5.3', 'Organising the analysis', [O_F, O_G], U3),
              open(os.path.join(root, 'content-units', 'CU-9093-1.5.3.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump({'dataset_id': 'ITEMS-9093-1.5', 'topic_id': '1.5', 'items': ITEMS},
              open(os.path.join(root, 'learning-items', 'topic_1.5_items.json'), 'w'), indent=1, ensure_ascii=False)
    open(os.path.join(root, 'texts', TEXT_ID + '.md'), 'w').write(TEXT)


write(EX)
open(os.path.join(EX, 'README.md'), 'w').write(
    '# 9093 structural exemplar\n\nA small, complete slice of topic 1.5 (text analysis) that passes the full check suite. Copy its '
    '**shape**: the field set of every claim, block and item; how a task names its practice text with `context.text_id`; the '
    'front matter of a text; how `claims_seen` and `authored_hash` are set; how a 25-mark model answer quotes the text and '
    'organises by effect. Do not copy its volume (the work orders set that) or its content (write your own).\n\nProof: `python3 '
    'standard/v0.2.0-draft/mine/exemplar_9093.py --prove` installs it as topic 1.5 in a scratch copy of the workspace and runs the suite.\n')
body = TEXT.split('---', 2)[2]
print('exemplar written: %d claims, %d blocks, %d items, 1 text (%d words), model answer %d words'
      % (len(CLAIMS), len(U1) + len(U2) + len(U3), len(ITEMS), len(body.split()), len(MODEL.split())))

if '--prove' in sys.argv:
    scratch = os.path.join(HOME, 'ex9093', 'cie-9093-as-2024-2026')
    if os.path.exists(os.path.dirname(scratch)):
        shutil.rmtree(os.path.dirname(scratch))
    os.makedirs(os.path.join(HOME, 'ex9093', 'operations', 'analysis'))
    shutil.copy(os.path.join(REPO, 'operations', 'analysis', '9093-as-english-language-corpus-analysis.md'),
                os.path.join(HOME, 'ex9093', 'operations', 'analysis'))
    shutil.copytree(WS, scratch, ignore=shutil.ignore_patterns('exemplar'))
    td = os.path.join(scratch, 'topics', '1.5')
    write(td)
    c = json.load(open(os.path.join(td, 'contract.json')))
    c['depth_constraints']['item_budget'] = len(ITEMS)
    c['required_outputs']['learning_items'] = len(ITEMS)
    c['required_outputs']['content_units'] = 3
    c['required_outputs']['practice_texts'] = 1
    json.dump(c, open(os.path.join(td, 'contract.json'), 'w'), indent=1, ensure_ascii=False)
    subprocess.run([sys.executable, os.path.join(STD, 'build', 'render_notes.py'), scratch, '1.5'], check=True)
    r = subprocess.run([sys.executable, os.path.join(STD, 'checks', 'run_checks.py'), scratch, '1.5',
                        '--out', os.path.join(td, 'qa_report.json')], capture_output=True, text=True)
    print(r.stdout[-3000:])
    print(r.stderr[-2000:])
