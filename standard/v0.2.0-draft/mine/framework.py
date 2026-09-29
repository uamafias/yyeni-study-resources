# -*- coding: utf-8 -*-
"""The assessment framework: what the syllabus says, reconciled with what the papers do.

Every value in the output carries its provenance, one of three:

  syllabus   transcribed from the syllabus, with the page that states it. The
             authority. Never typed from recall, never inferred from a paper's
             name. Read out of curriculum/syllabus-facts.json, which mine_syllabus.py
             produced by reading the PDF.
  corpus     measured by counting the published papers and mark schemes.
  judgement  neither stated nor measured - our reading. Labelled so that nobody
             downstream mistakes it for either of the above.

The rule that produced this design: assessment values were once written from
recall and two were wrong. A value that cannot name where it came from is a
value we do not have.
"""
import json, os, collections, datetime

ROOT = os.path.expanduser('~/mine')
REPO = os.path.expanduser('~/mnt/YYeni Study Resources')
WS = {'0450': 'work/cie-0450-igcse-2026', '0455': 'work/cie-0455-igcse-2026'}

# The one thing the syllabus does NOT state: which assessment objectives a given
# command word mainly serves. Cambridge publishes the words and it publishes the
# AO weights, but it does not join them. This mapping is therefore OUR READING,
# tagged 'judgement' in the output so it is never mistaken for a transcription,
# and it is checked against the corpus: a word's tariff and the band descriptors
# of the questions it opens have to be consistent with the AOs claimed here.
AO_JUDGEMENT = {
    '0450': {'Define': ['AO1'], 'Identify': ['AO1'], 'State': ['AO1'],
             'Outline': ['AO1', 'AO2'], 'Calculate': ['AO2', 'AO1'],
             'Explain': ['AO1', 'AO2', 'AO3'], 'Consider': ['AO2', 'AO3', 'AO4'],
             'Using': ['AO2', 'AO3', 'AO4'], 'Justify': ['AO4']},
    '0455': {'Define': ['AO1'], 'Identify': ['AO1'], 'State': ['AO1'],
             'Give': ['AO1'], 'Describe': ['AO1'], 'Calculate': ['AO1', 'AO2'],
             'Draw': ['AO2'], 'Explain': ['AO1', 'AO2'], 'Analyse': ['AO2'],
             'Discuss': ['AO2', 'AO3']},
}
AO_JUDGEMENT_BASIS = (
    'The syllabus publishes the command words and it publishes the AO weights, but it '
    'does not join them. This mapping is our reading, not a transcription. It is '
    'constrained by the corpus: each word is assigned the objectives consistent with '
    'the tariffs it actually carries and, for banded questions, with what the level '
    'descriptors demand.')


def rd(p):
    with open(p, encoding='utf-8') as fh:
        return json.load(fh)


def facts(code):
    p = os.path.join(REPO, WS[code], 'curriculum', 'syllabus-facts.json')
    if not os.path.exists(p):
        raise SystemExit(
            'STEP ZERO missing: %s\n'
            'Run  python3 mine_syllabus.py %s  first. The framework is not allowed to '
            'invent assessment objectives, weights, paper structures or command words; '
            'it can only read the ones transcribed from the syllabus.' % (p, code))
    return rd(p)


def build(code):
    f = facts(code)
    ms = rd(os.path.join(ROOT, '%s_markscheme.json' % code))

    listed = {c['word']: c for c in f['command_words']}
    obs = collections.defaultdict(collections.Counter)
    by_paper = collections.defaultdict(collections.Counter)
    for r in ms:
        if r['cw'] and r['marks']:
            obs[r['cw']][r['marks']] += 1
            by_paper[r['cw']][r['paper']] += 1

    words = []
    for w in sorted(set(obs) | set(listed)):
        t = obs.get(w, collections.Counter())
        n = sum(t.values())
        in_table = w in listed
        words.append({
            'word': w,
            'meaning': listed[w]['meaning'] if in_table else None,
            'meaning_provenance': ('syllabus, page %d' % listed[w]['source']['page']
                                   if in_table else
                                   'not in the syllabus table; no published meaning'),
            'in_syllabus_table': in_table,
            'syllabus_page': listed[w]['source']['page'] if in_table else None,
            'syllabus_verbatim': listed[w]['verbatim'] if in_table else None,
            'primary_assessment_objectives': AO_JUDGEMENT[code].get(w, []),
            'assessment_objectives_provenance': 'judgement',
            'observed_count': n,
            'observed_tariffs': {str(k): v for k, v in sorted(t.items())},
            'modal_tariff': t.most_common(1)[0][0] if t else None,
            'papers': dict(sorted(by_paper.get(w, {}).items())),
            'observation_provenance': 'corpus: %d published mark schemes, 2020-2025'
                                      % len({r['file'] for r in ms}),
        })

    n_tot = sum(w['observed_count'] for w in words) or 1
    for w in words:
        share = 100.0 * w['observed_count'] / n_tot
        w['share_of_question_parts_percent'] = round(share, 1)
        if w['in_syllabus_table'] and w['observed_count'] == 0:
            w['verdict'], w['use_in_prompts'] = 'listed_not_observed', False
        elif not w['in_syllabus_table'] and w['observed_count'] >= 5:
            w['verdict'], w['use_in_prompts'] = 'observed_not_listed', True
        elif not w['in_syllabus_table']:
            w['verdict'], w['use_in_prompts'] = 'extraction_noise', False
        elif share >= 8:
            w['verdict'], w['use_in_prompts'] = 'primary', True
        else:
            w['verdict'], w['use_in_prompts'] = 'secondary', True
        # what the generator reads
        w['exact_mark_tariff'] = w['modal_tariff']
        w['used_at_level'] = w['observed_count'] > 0
    words.sort(key=lambda w: -w['observed_count'])

    aos = [{'code': a['code'], 'name': a['name'],
            'description': ' '.join(a['can_do']),
            'qualification_weight_percent': a['qualification_weight_percent'],
            'provenance': 'syllabus, page %d' % a['source']['page']}
           for a in f['assessment_objectives']]

    papers = [{'paper': p['paper'], 'name': p['name'], 'marks': p['marks'],
               'duration_minutes': p['duration_minutes'],
               'weight_percent': p['weight_percent'],
               'ao_split': p['ao_split'],
               'structure': p['description'],
               'provenance': 'syllabus, page %d; AO split from the per-component '
                             'weighting table on page %d'
                             % (p['source']['page'],
                                f['ao_weights']['source']['per_component']['page'])}
              for p in f['papers']]

    return {
        'framework_id': 'ASSESS-CIE-%s-IGCSE-2026' % code,
        'generated_at': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'generated_by': 'framework.py, from curriculum/syllabus-facts.json',
        'authority': f['authority'],
        'provenance_rule':
            'Every value carries one of three provenances. "syllabus" is transcribed '
            'from the named page and is the authority. "corpus" is counted from the '
            'published papers. "judgement" is our reading and is neither. Nothing here '
            'is written from recall. A value that cannot name where it came from is a '
            'value we do not have.',
        'syllabus_facts_ref': 'curriculum/syllabus-facts.json',
        'assessment_objectives': aos,
        'papers': papers,
        'command_word_table_source':
            '%s section 4, Command words, page %s. %d words.'
            % (f['authority'].rstrip('.'), f['command_word_table']['page'],
               f['command_word_table']['count']),
        'command_word_reconciliation':
            'Each word carries what the syllabus says it means and the page that says '
            'it, the objectives we judge it to serve, and what the corpus shows it '
            'actually does. The verdict is the reconciliation. Only a word with '
            'use_in_prompts true may appear in a generated prompt.',
        'command_word_ao_mapping_basis': AO_JUDGEMENT_BASIS,
        'command_words': words,
    }


if __name__ == '__main__':
    for code in ('0450', '0455'):
        fw = build(code)
        json.dump(fw, open(os.path.join(ROOT, 'out',
                                        '%s_assessment_framework.json' % code), 'w'), indent=1)
        print('\n%s  %s' % (code, fw['command_word_table_source']))
        print('  %-10s %-6s %-7s %-30s %-20s %s'
              % ('word', 'n', 'modal', 'tariffs', 'verdict', 'in table'))
        for w in fw['command_words']:
            if w['verdict'] == 'extraction_noise':
                continue
            print('  %-10s %-6d %-7s %-30s %-20s %s'
                  % (w['word'], w['observed_count'], w['modal_tariff'] or '-',
                     str(w['observed_tariffs'])[:30], w['verdict'],
                     'p.%s' % w['syllabus_page'] if w['in_syllabus_table'] else 'NOT LISTED'))
