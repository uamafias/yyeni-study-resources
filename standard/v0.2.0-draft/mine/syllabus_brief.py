# -*- coding: utf-8 -*-
"""Step zero's written output: one syllabus brief per code, from the verified facts.

Everything here is read out of syllabus-facts.json, which was transcribed from the
PDF with a page and a verbatim line for every value. The brief adds nothing of its
own except the 'what this means for the plan' lines, which are labelled as ours.
"""
import json, os, sys, datetime
sys.path.insert(0, os.path.expanduser('~/mine'))
import mine_syllabus as MS
REPO = os.path.expanduser('~/mnt/YYeni Study Resources')

SLUG = {'9709': 'as-mathematics', '0500': 'igcse-first-language-english', '9618': 'as-computer-science',
        '9702': 'as-physics', '0460': 'igcse-geography', '9093': 'as-english-language'}

# What each subject's own assessment pages imply for the plan. Our reading, not
# the syllabus's words - so it is labelled that way in the brief.
IMPLICATIONS = {
 '9709': ["Two AOs only. Every card is either recall of a technique (AO1) or choosing and applying one to a problem and presenting it (AO2); balance 55/45.",
          "Cards are practice problems: the question on the front, a full worked solution on the back, so the learner attempts it and checks.",
          "'Show (that)' is in the command table: a result is given and the working is what earns marks. Show-that cards must print the target and mark the steps.",
          "Scope is Paper 1 (Pure 1) and Paper 5 (Probability & Statistics 1) only. Paper 1 is 60% of this learner's AS, Paper 5 40%."],
 '0500': ["The assessed grain is R1-R5 and W1-W5, not AO1 and AO2. Every item names the sub-objectives it practises.",
          "The syllabus prints each question's marks and sub-objectives; the plan is built on that question architecture, not on topics.",
          "Only four command words. Most tasks are instructions (write a letter, summarise), so tasks are planned by text type, purpose and word limit.",
          "Speaking and Listening is separately endorsed and not part of this learner's entry."],
 '9618': ["AOs are numbered, not named. Roles are our reading: AO1 knowledge, AO2 application, AO3 design, programming and evaluation.",
          "Paper 1 (sections 1-8) has no AO3; Paper 2 (sections 9-12) has no AO1. The two papers need different kinds of card.",
          "Paper 2 is answered in pseudocode, never program code, with an insert of built-in functions. Its cards are pseudocode and algorithm problems.",
          "27 command words, including Write, Complete, Draw and State."],
 '9702': ["Three AOs, 40/40/20. Paper 3 is 100% AO3: experimental skills only.",
          "Paper 3 is two 20-mark experiments. The syllabus prints minimum marks per skill: Question 2 gives 10 of 20 to conclusions, uncertainties, limitations and improvements.",
          "Practical cards cover every technique: reading instruments, repeat readings, tables, graphs, gradients, uncertainties, limitations, improvements.",
          "Paper weights are stated as 31/46/23, not proportional to marks."],
 '0460': ["Three AOs, 30/52/18. Skills and analysis is over half the qualification.",
          "Paper 2 is 80% AO2: map, data and graph skills. Its cards are technique cards and worked data problems.",
          "Paper 1 is 75 marks weighted to 100: three 25-mark questions, one from each section.",
          "Paper 4 (Alternative to Coursework) is fieldwork method: hypotheses, sampling, recording, presenting, concluding, evaluating."],
 '9093': ["Five AOs, but AO4 and AO5 are 0% at AS. The AS plan uses AO1, AO2 and AO3 only.",
          "Only three command words: Analyse, Compare, Discuss. The papers are task-led, and the syllabus prints each part's marks and AOs.",
          "Paper 1 is 60% AO3: analysing form, structure and language. Paper 2 is 80% AO2: writing to a brief.",
          "Every writing task has a word limit and a form, purpose and audience; cards and tasks carry all four."],
}

def brief(code):
    m = MS.SUBJECTS[code]
    F = json.load(open(os.path.join(REPO, m['ws'], 'curriculum', 'syllabus-facts.json')))
    L = []; a = L.append
    a('# Syllabus brief — %s' % m['title']); a('')
    a('Step zero for this subject: what the syllabus says about how it is assessed, transcribed '
      'from the document with the page for every value. Read this before any past paper. '
      'Generated %s from `curriculum/syllabus-facts.json`.' % datetime.date.today().strftime('%d %B %Y')); a('')
    a('| | |'); a('|---|---|')
    a('| syllabus | `%s` |' % m['pdf'])
    a('| route | %s |' % (F.get('route') or 'single route'))
    if F.get('papers_sat'):
        a('| this learner sits | %s |' % '; '.join(F['papers_sat']))
    if F.get('first_exam'):
        a('| first exam | %s |' % F['first_exam'])
    a('')
    a('## Assessment objectives'); a('')
    pc = F['ao_weights']['per_component_percent']
    papers = [p['paper'] for p in F['papers']]
    a('| AO | what it assesses | weight | %s |' % ' | '.join('Paper %s' % p for p in papers))
    a('|---|---|---:|%s' % ('---:|' * len(papers)))
    for x in F['assessment_objectives']:
        what = x['name'] or ' '.join(x['can_do'])[:90]
        w = x.get('weight_note') or '%s%%' % x['qualification_weight_percent']
        a('| %s | %s | %s | %s |' % (x['code'], what, w,
          ' | '.join('%s%%' % pc.get('P' + p, {}).get(x['code'], '—') for p in papers)))
    src = F['ao_weights']['source']
    a('')
    a('Weights from page %s%s.' % ((src.get('qualification') or {}).get('page', '?'),
                                   ', per-paper split from page %s' % src['per_component']['page']
                                   if src.get('per_component', {}).get('page') else ''))
    a('')
    a('## Papers in this route'); a('')
    for p in F['papers']:
        a('**Paper %s — %s.** %d marks, %d minutes, **%s%%** of the qualification (%s). %s'
          % (p['paper'], p['name'], p['marks'], p['duration_minutes'], p['weight_percent'],
             p.get('weight_provenance', '').split(':')[0], p['description'][:520]))
        a('')
    notes = F.get('transcribed_notes') or []
    if notes:
        a('## Structure the syllabus prints'); a('')
        for n in notes:
            a('- **%s** (page %d). %s' % (n['topic'], n['page'], n['fact']))
        a('')
    a('## Command words'); a('')
    a('Page %s. The complete list the syllabus publishes: **%d**.'
      % (F['command_word_table']['page'], len(F['command_words']))); a('')
    a('| command word | what it means |'); a('|---|---|')
    for c in F['command_words']:
        a('| %s | %s |' % (c['word'], c['meaning']))
    a('')
    a('Next: reconcile these against the past papers — how often each opens a question, at what '
      'tariff, on which paper. That verdict, not this list alone, decides what goes in a prompt.'); a('')
    a('## What this means for the plan'); a('')
    a('*Our reading of the pages above — not a transcription.*'); a('')
    for x in IMPLICATIONS.get(code, []):
        a('- %s' % x)
    a('')
    return '\n'.join(L)

if __name__ == '__main__':
    for code in (sys.argv[1:] or list(SLUG)):
        m = MS.SUBJECTS[code]
        p = os.path.join(REPO, m['ws'], 'SYLLABUS-BRIEF-%s-%s.md' % (code, SLUG[code]))
        open(p, 'w', encoding='utf-8').write(brief(code))
        print('%6d  %s' % (os.path.getsize(p), p.replace(REPO + '/', '')))
