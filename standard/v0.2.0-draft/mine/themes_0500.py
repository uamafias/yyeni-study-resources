# -*- coding: utf-8 -*-
import json, re, os, collections
ROOT = os.path.expanduser('~/mine')
rows = json.load(open(os.path.join(ROOT, '0500_examiner_statements.json')))
T = {
 'P1 Q1(a-e) comprehension': [
  ('answers from the part of the text the question names', r'(?:specified|indicated|identified|relevant|named|given|particular|correct|right) (?:paragraph|section|part|lines?)|(?:paragraph|section|lines?) (?:specified|indicated|identified|given|named)|outside the (?:paragraph|section|lines)|wrong (?:paragraph|section|part)'),
  ('gives only what is asked; extra material can undo a correct answer', r'additional|extra\b|excess|extraneous|irrelevant|too much|unnecessary|contradict|negat|lengthy'),
  ('explains both parts of a two-part idea', r'both (?:parts|elements|halves|strands|ideas|aspects)|two (?:parts|elements|ideas|aspects|points)|only one (?:part|element|aspect|idea)|partial(?:ly)?\b'),
  ('restates in own words rather than copying', r'own words|lift|copied|copying|recycl'),
  ('reads implied meaning as well as stated meaning', r'implicit|implied|infer|inference|between the lines'),
 ],
 'P1 Q1(f) summary': [
  ('own words, not lifted', r'own words|lift|copied|copying|language of the text'),
  ('concise; within the word limit', r'concis|word limit|120 words|over.?long|length|too long'),
  ('selects only relevant points; no examples or excess', r'excess|examples?|irrelevant|redundant|repetit|unnecessary detail'),
  ('an overview, not a list', r'overview|list|organis|connect|linked|fluent'),
  ('no added opinion or comment', r'opinion|comment|own views|evaluat|introduc'),
  ('range of points; answers the focus of the question', r'range of|number of (?:relevant )?(?:ideas|points)|focus|misread|both|advantages|positives|negatives'),
 ],
 'P1 Q2(d) language task': [
  ('selects precise words and phrases, not long quotations', r'long quotation|lengthy|whole sentence|single words|precise|choices|selection'),
  ('explains meaning AND effect, not meaning alone', r'effect|meaning|connotation|associat|suggest'),
  ('names devices without explaining them', r'device|technique|simile|metaphor|personification|alliteration|label|identif(?:y|ied) (?:the )?(?:use|techniques)'),
  ('tackles imagery', r'imag(?:e|ery)|figurative'),
  ('covers both paragraphs, around three choices each', r'both (?:parts|paragraphs|halves)|each paragraph|three choices|one paragraph|second paragraph|first paragraph|imbalan|uneven'),
  ('specific, not general, comment', r'general|generic|vague|overall|whole paragraph|atmosphere'),
 ],
 'P1 Q2(c) one example, explain the effect': [
  ('uses one example only', r'one example|more than one|several|multiple'),
  ('explains how it creates the effect', r'explain|effect|how the writer|suggest'),
  ('chooses an appropriate example', r'appropriate|selected|chose|choice'),
 ],
 'P1 Q2(a) word or phrase with the same meaning': [
  ('the exact word or phrase, not extra text', r'extra|additional|whole|sentence|too much|longer|more than'),
  ('reads the underlined idea carefully', r'underlined|idea|sense|meaning'),
 ],
 'P1 Q2(b) own-words meaning of single words': [
  ('own words, not the word itself', r'own words|repeat|same word|root'),
  ('meaning in this context', r'context|sense|meaning|precise'),
 ],
 'P1 Q3 extended response to reading': [
  ('covers all three bullets, evenly', r'three bullets|all three|bullet|uneven|balance|each of the'),
  ('develops and evaluates ideas, not just repeats them', r'develop|evaluat|infer|analys|beyond|extend'),
  ('uses details from the text, not copying', r'lift|copied|copying|reproduc|own words|text details|supporting detail|evidence'),
  ('stays tethered to the text; no invention', r'invent|untethered|not in the text|made up|outside the text|irrelevant'),
  ('convincing voice, form and register', r'voice|register|form|audience|persona|style|tone|convincing'),
 ],
 'P2 Section A directed writing': [
  ('evaluates the ideas, not just summarises them', r'evaluat|summar|reproduc|list(?:ed)?|merely|simply repeat|critical'),
  ('uses both texts', r'both texts|one text|Text A|Text B|each text'),
  ('own words, not lifting', r'own words|lift|copied|copying'),
  ('form, register and audience', r'register|form|audience|letter|speech|article|tone|formal|informal|convention'),
  ('structure and a line of argument', r'structur|organis|sequenc|paragraph|argument|coheren|conclusion|introduction'),
  ('addresses both bullets', r'both bullet|second bullet|first bullet|bullet'),
  ('accuracy of spelling, punctuation and grammar', r'spelling|punctuation|grammar|accura|errors|comma|sentence'),
 ],
 'P2 Section B composition': [
  ('descriptive: images and detail, not a plot', r'narrative|story|plot|event'),
  ('description: sensory, precise detail', r'sens|detail|image|evocative|atmosphere|sound|smell|colour|vivid'),
  ('narrative: a credible, controlled plot', r'credib|plot|events|realistic|complicat|too many|pace|pacing'),
  ('narrative: character and tension, a real ending', r'character|tension|climax|ending|resolution|suspense'),
  ('structure and deliberate shaping', r'structur|organis|opening|beginning|shape|cohes|paragraph'),
  ('vocabulary: precise, not overwritten', r'vocabular|adjective|overwrit|clich|elaborate|ambitious|precise|thesaurus'),
  ('varied, accurate sentences', r'sentence|punctuat|grammar|spelling|tense|accura|comma splice'),
 ],
}
MAP = {'P2 Section B composition': ('P2 Section B composition (either)', 'P2 Section B descriptive composition',
                                    'P2 Section B narrative composition')}
out = {}
for task, themes in T.items():
    src = MAP.get(task, (task,))
    pool = [r for r in rows if r['task'] in src]
    ser_all = {r['series'] for r in pool}
    print('\n=== %s: %d sentences, %d series ===' % (task, len(pool), len(ser_all)))
    out[task] = []
    for name, rx in themes:
        hits = [r for r in pool if re.search(rx, r['text'], re.I)]
        ser = {r['series'] for r in hits}
        st = [r for r in hits if r['kind'] == 'strong']; wk = [r for r in hits if r['kind'] == 'weak']
        print('  %-58s %2d/%-2d series  strong %-4d weak %-4d' % (name, len(ser), len(ser_all), len(st), len(wk)))
        ex_s = next((r['text'] for r in st if 60 < len(r['text']) < 260), '')
        ex_w = next((r['text'] for r in wk if 60 < len(r['text']) < 260), '')
        print('      + %s' % ex_s[:230]); print('      - %s' % ex_w[:230])
        out[task].append({'theme': name, 'series': len(ser), 'of': len(ser_all), 'strong': len(st), 'weak': len(wk)})
json.dump(out, open(os.path.join(ROOT, 'out', '0500_themes.json'), 'w'), indent=1)
