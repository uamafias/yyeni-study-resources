#!/usr/bin/env python3
"""
Generate the independent-review brief and the reviewer prompt for one topic.

The brief is assembled from the build's own artifacts, so it is correct for any
board, subject, level and topic without editing. Run it AFTER run_checks.py, so
the brief can tell the reviewer what code already found.

    python3 make_review_packet.py <repo-root> <workspace-rel> <topic-id>
"""
import sys, os, json, glob, argparse
from collections import Counter

try:
    import yaml
except ImportError:
    yaml = None

HERE = os.path.dirname(os.path.abspath(__file__))
STANDARD = os.path.dirname(HERE)


def j(p):
    return json.load(open(p)) if os.path.exists(p) else None


def y(p):
    return yaml.safe_load(open(p)) if (yaml and os.path.exists(p)) else None


def build(root, wsrel, topic):
    ws = os.path.join(root, wsrel)
    td = os.path.join(ws, 'topics', topic)
    d = dict(
        root=root, wsrel=wsrel, ws=ws, td=td, topic=topic,
        contract=j(os.path.join(td, 'contract.json')) or {},
        framework=j(os.path.join(ws, 'curriculum/assessment-framework.json')) or {},
        registry=j(os.path.join(ws, 'curriculum/objective_registry.json')) or {},
        exposure=j(os.path.join(ws, 'curriculum/exam-exposure.json')) or {},
        glossary=j(os.path.join(ws, 'curriculum/glossary.json')) or {},
        evidence=j(os.path.join(ws, 'assessment-evidence/assessment_evidence.json')) or {},
        ledger=j(os.path.join(td, 'claims/canonical_claim_ledger.json')) or {},
        qa=j(os.path.join(td, 'qa_report.json')) or {},
        profile=y(os.path.join(ws, 'subject-profile.yaml')) or {},
        qual=y(os.path.join(ws, 'qualification-profile.yaml')) or {},
    )
    d['units'] = [j(p) for p in sorted(glob.glob(os.path.join(td, 'content-units', '*.json')))]
    d['items'] = []
    for p in sorted(glob.glob(os.path.join(td, 'learning-items', '*.json'))):
        blob = j(p)
        d['items'].extend(blob.get('items', []))
    return d


def md(d):
    t, C, F = d['topic'], d['contract'], d['framework']
    objs = [o for o in d['registry'].get('objectives', []) if o.get('topic_id') == t]
    assessable = [o for o in objs if o.get('parent_id')]
    claims = d['ledger'].get('claims', [])
    gap = [c for c in claims if c.get('provenance') == 'generated_gap']
    jur = [c for c in claims if 'jurisdiction' in json.dumps(c.get('notes', [])).lower()]
    used = [c for c in F.get('command_words', []) if c.get('used_at_as') or c.get('used_at_level')]
    unused = [c for c in F.get('command_words', []) if not (c.get('used_at_as') or c.get('used_at_level'))]
    EX = {e['objective_id']: e for e in d['exposure'].get('objectives', [])}
    cls = Counter(EX[o['objective_id']]['exam_exposure'] for o in assessable if o['objective_id'] in EX)
    rare = [o['objective_id'] for o in assessable
            if 'rarely-examined' in (EX.get(o['objective_id'], {}).get('review_sets') or [])]
    excl = (C.get('depth_constraints') or {}).get('excluded_constructs') or []
    homs = [x['term'] for x in d['glossary'].get('terms', []) if (x.get('disambiguation') or '').strip()]
    variants = d['profile'].get('variant_register') or []
    structs = d['profile'].get('answer_structures') or {}
    qa = d['qa']
    checks = qa.get('deterministic_checks', [])
    bad = [c for c in checks if c['status'] in ('fail', 'warn')]
    notrun = [c for c in checks if c['status'] == 'not_run']

    L = []
    A = L.append
    A('# Independent review brief — %s, topic %s' % (C.get('qualification', d['wsrel']), t))
    A('')
    A('**Topic:** %s · **Standard:** %s · **Build state:** %s'
      % (C.get('topic_title', '?'), C.get('standard_version', 'v0.2.0-draft'), qa.get('release_decision', 'unknown')))
    A('**Deterministic report:** `%s/topics/%s/qa_report.json` · **Packet hashes:** `%s/topics/%s/packet.sha256`'
      % (d['wsrel'], t, d['wsrel'], t))
    A('')
    A('*This brief is generated from the build. Do not hand-edit it — change the build or the standard instead.*')
    A('')
    A('---')
    A('')
    A('## 1. What this review is')
    A('')
    A('You are the independent semantic reviewer required by RS-28. The build cannot reach `REVIEWED` without your '
      'report and cannot reach `APPROVED` until the human decisions in §7 are made.')
    A('')
    A('**Do not re-count what code counted.** %d deterministic checks have already run (%s). RS-30 says mechanical '
      'claims must be confirmed by code; the corollary is that your budget belongs to the questions code cannot '
      'answer. If you think a mechanical result is wrong, file it as an issue with the input that contradicts it.'
      % (len(checks), ', '.join('%d %s' % (n, s) for s, n in Counter(c['status'] for c in checks).items())))
    A('')
    A('**The question you are being asked:** does this material teach the syllabus to a learner who has no other '
      'source, and will a learner who masters it write credit-worthy answers?')
    A('')
    A('Three consequences. Read the objective branch before the notes — a reviewer without the objective map cannot '
      'detect omission. Judge against the syllabus, not a textbook you know: more than the objective requires is a '
      'defect here, not a bonus. And report evidence, never impressions.')
    A('')
    A('## 2. Scope')
    A('')
    A('- Objectives in this topic: **%d assessable** (plus %d container node(s)).' % (len(assessable), len(objs) - len(assessable)))
    A('- Material under review: %d content units, %d learning items, %d ledger claims.'
      % (len(d['units']), len(d['items']), len(claims)))
    A('- %d of %d claims are `generated_gap` — authored because no supplied source covers them. An empty `evidence` '
      'array is expected and is **not** a defect. Judge instead: is it true, is it inside the objective, does it say '
      'enough, does it say more than the objective requires?' % (len(gap), len(claims)))
    if excl:
        A('- **Excluded from this topic** (higher level, or belongs elsewhere): %s. Content beyond the objective and '
          'content short of it are both defects, with different repairs.' % ', '.join('`%s`' % x for x in excl))
    A('')
    A('## 3. What code already found')
    A('')
    if bad:
        A('These need your judgement — code sees the pattern, not the intent:')
        A('')
        for c in bad:
            A('- **%s (%s)** — %s' % (c['check_id'], c['status'].upper(), c['message']))
        A('')
    else:
        A('Every deterministic check passed.')
        A('')
    if notrun:
        A('Checks that could **not** run, and why. A `not_run` is not a pass — treat each as an area where you are the '
          'only line of defence:')
        A('')
        for c in notrun:
            A('- **%s** — %s' % (c['check_id'], c['message']))
        A('')
    prior = [r for r in qa.get('semantic_reviews', []) if r.get('issues')]
    if prior:
        res = [i for r in prior for i in r['issues'] if i.get('status') == 'resolved']
        opn = [i for r in prior for i in r['issues'] if i.get('status') not in ('resolved',)]
        A('## 3a. What a previous review found, and what was done')
        A('')
        A('This topic has been reviewed before. **Your job includes checking the repairs, not only looking for new '
          'defects** - a repair that removes a symptom and leaves the cause is a finding, and so is a repair that '
          'introduces something new.')
        A('')
        if res:
            A('%d issues are marked **resolved by the author**. That is a claim, not a verdict:' % len(res))
            A('')
            for i in res:
                fix = next((e for e in i.get('evidence', []) if str(e).startswith('REPAIRED')), '')
                A('- **%s** (%s, %s) — %s' % (i['issue_id'], i['severity'], i['category'], i['finding'][:200]))
                if fix:
                    A('  - %s' % fix)
            A('')
        if opn:
            A('%d issues remain open:' % len(opn))
            A('')
            for i in opn:
                A('- **%s** (%s) — %s' % (i['issue_id'], i['severity'], i['finding'][:200]))
            A('')

    A('## 4. Build-specific checks')
    A('')
    if used:
        A('### Command words actually used at this level')
        A('')
        A('| Command word | Tariff | A credit-worthy answer |')
        A('|---|---|---|')
        for c in used:
            A('| %s | **%s** | %s |' % (c['word'], c.get('exact_mark_tariff') or c.get('typical_mark_tariff') or '?',
                                        (c.get('a_credit_worthy_answer') or '').replace('|', '/')))
        A('')
    if unused:
        A('**Must not appear as instructions:** %s. %s'
          % (', '.join('`%s`' % c['word'] for c in unused),
             ' '.join(c.get('evidence_note', '') for c in unused)[:400]))
        A('')
    psv = F.get('paper_structure_verified') or {}
    if psv:
        A('**Paper structure, verified.** ' + (psv.get('note') or ''))
        for k, v in psv.items():
            if isinstance(v, dict):
                A('- **%s** — %s' % (k, '; '.join(str(x) for x in v.values())))
        A('')
    if cls:
        A('### Exposure is evidence, never priority')
        A('')
        A('Classes in this topic: %s. %s' % (dict(cls), d['exposure'].get('why_silence_is_weak_evidence', '')))
        A('')
        if rare:
            A('**%d objectives sit in the rarely-examined review set** and must be taught to full depth: %s. '
              'An objective taught thinly because it has never been examined is a **critical** finding, not a low one '
              '(RS-05).' % (len(rare), ', '.join('`%s`' % r for r in rare)))
            A('')
    if jur:
        A('### Jurisdiction (RS-23)')
        A('')
        A('%d claims are jurisdiction-flagged. Learners sit an international paper from one country: a claim true of '
          'one jurisdiction and stated flatly is **critical**, because the learner will write it in an exam marked '
          'against an international standard.' % len(jur))
        A('')
    if variants:
        A('### Variant completeness (RS-35)')
        A('')
        A('Terms in this subject whose forms change a learner-relevant consequence. Where the topic uses one, check '
          'that the forms are named and every benefit and limitation is conditioned on the form:')
        A('')
        for v in variants:
            A('- **%s** — %s → *%s*' % (v.get('term'), ' / '.join(v.get('variants') or []), v.get('consequence', '')))
        A('')
        A('The register is human-maintained and deliberately incomplete: **an unlisted consequential variant is a gap '
          'in the register, and reporting it is part of this review.**')
        A('')
    if structs:
        A('### Declared answer structures (RS-38)')
        A('')
        for k, parts in structs.items():
            A('- **%s** — %s' % (k, ' · '.join(str(p).split('|')[0] for p in parts)))
        A('')
        A('C-16 checks that each part is *named*. You judge whether each part is *done*: a judgement that never says '
          'what to do, a context that names a business without changing the reasoning, or a counterargument that is '
          'the same point restated all pass the mechanical check and fail the learner.')
        A('')
    if homs:
        A('### Homonyms (RS-08)')
        A('')
        A('Cross-topic terms carrying a disambiguation warning: %s. Where this topic uses one, judge whether the sense '
          'is right here and whether it collides with the sense the learner meets elsewhere.' % ', '.join('**%s**' % h for h in homs))
        A('')
    A('### Conditional causal language (RS-21)')
    A('')
    A('Every analysis chain and every applied answer must reason conditionally, with a mechanism. An asserted outcome '
      'is a defect even when it is usually true. Statements about what a lender, investor, buyer, supplier, employer '
      'or regulator will do must be likelihood with a reason.')
    A('')
    A('## 5. The five reviewer roles')
    A('')
    for n, (name, body) in enumerate([
        ('Curriculum and omission', 'correct board, version, level, route and topic scope; every mandatory objective '
         'adequately taught *and* practised; nothing covered only nominally; no out-of-level content as core; '
         'prerequisites and cross-topic terms consistent; nothing supplied dropped without a recorded reason.'),
        ('Accuracy and evidence', 'definitions, classifications, formulas, dates and factual relationships; whether '
         'generated claims are adequately verified; whether inferences follow from their premises; whether legal and '
         'jurisdictional claims are properly qualified; whether contradictions between claims are resolved. '
         '**Check mechanisms in both directions — a fluent sentence can state a true relationship backwards.**'),
        ('Pedagogy and accessibility', 'clarity for the intended learner; conceptual progression and prerequisite '
         'order; whether mechanisms are explained rather than listed; whether distinctions and misconceptions are '
         'taught explicitly; proportionality and cognitive load; whether the learner could reconstruct the knowledge '
         'without the source notes.'),
        ('Assessment alignment', 'alignment to assessment objectives and command words; use of paper, mark-scheme and '
         'examiner-report evidence; genuine contextual application rather than an industry name dropped in; causal '
         'validity of chains; decisiveness of evaluation; whether practice matches paper formats and tariffs.'),
        ('Learning-item integrity', 'objective and claim mapping; atomicity and self-containment; answer completeness; '
         'prompt ambiguity or answer leakage; *semantic* duplication, which code cannot see; progression from recall '
         'to transfer; the balance of flashcards against performance tasks; one consistent item architecture.'),
    ], 1):
        A('**%d. %s** — %s' % (n, name, body))
        A('')
    A('### Bidirectional audit')
    A('')
    A('1. **Objective → content.** For each of the %d assessable objectives, name exactly where it is adequately '
      'taught and where it is practised. Code proved a link exists and that the link is claim-backed; you judge '
      'adequacy.' % len(assessable))
    A('2. **Content → objective.** For each substantial block, name the objective, prerequisite or approved enrichment '
      'that justifies it. A block that justifies nothing is scope creep.')
    A('')
    A('### Reconstruction test — the highest-value part of this review')
    A('')
    A('Using **only** the generated resource, with no outside knowledge, construct answers across the tariff range: a '
      'recall item, several short explanations on different objectives, an analysis on an unfamiliar case, an '
      'evaluation, and one application to a context the material never mentions.')
    A('')
    A('Report every objective for which the resource does not contain enough knowledge or reasoning support to build a '
      'strong answer. **This is also the RS-39 check that code could not do:** where a canonical answer leans on a '
      'mechanism, distinction or figure the notes never teach, the offline learner cannot get there. Name each one.')
    A('')
    A('## 6. How to report')
    A('')
    A('```yaml')
    A('issue_id: unique-id')
    A('severity: critical | high | medium | low')
    A('category: curriculum | accuracy | evidence | pedagogy | application | analysis | evaluation | quantitative | learning-item | coherence | publishing')
    A('affected_ids:')
    A('  - objective-or-claim-or-item-id')
    A('finding: precise description of the defect')
    A('evidence:')
    A('  - exact block, claim, card or line reference')
    A('educational_consequence: how this could affect learner understanding or exam performance')
    A('recommended_repair: specific corrective action')
    A('confidence: 0.0-1.0')
    A('status: open')
    A('```')
    A('')
    A('**Severity.** *Critical* — wrong scope; dangerous misinformation; materially wrong definition, formula or '
      'mechanism; missing compulsory objective; unqualified jurisdiction-specific claim; a rarely-examined objective '
      'taught thinly. *High* — major omission; invalid causal reasoning; misleading evaluation; systematic application '
      'failure. *Medium* — limited example range; structural inconsistency; semantically repeated items. *Low* — '
      'wording, formatting, sequencing.')
    A('')
    A('**The release bar for this build is: no critical and no high issue open.** Medium and low issues are logged '
      'against the topic and cleared in a later maintenance pass. That is not licence to downgrade a real defect - '
      'grade on the harm to the learner, and if something belongs at high, put it at high.')
    A('')
    A('**Decision.** *Pass* — no open critical, high or medium issues. *Conditional pass* — only bounded issues remain; '
      'publication stays blocked. *Reject* — any critical, any unresolved high, systematic failure, or inability to '
      'verify coverage.')
    A('')
    A('## 7. What a pass does not release')
    A('')
    A('%d generated-gap claims still need documented human approval (RS-13)%s. Those are human decisions outside this '
      'review.' % (len(gap), ', and %d jurisdiction-sensitive claims need a human wording decision (RS-23)' % len(jur) if jur else ''))
    A('')
    A('## 8. Independence')
    A('')
    A('This material and this brief were produced by the same system. **If a decision recorded here looks wrong — the '
      'decomposition, the exposure position, the depth, the item allocation, the variant register, a check that '
      'passed — file it as an issue against the decision rather than working around it.** A review that only finds '
      'defects the brief pointed at has not been independent.')
    A('')
    return '\n'.join(L)


def prompt(d):
    t = d['topic']; w = d['wsrel']
    done = len([r for r in d['qa'].get('semantic_reviews', []) if r.get('issues')])
    rnd = done + 1
    return '\n'.join([
        'Repo root: %s' % d['root'], '',
        'You are the independent semantic reviewer for %s, topic %s.'
        % (d['contract'].get('qualification', w), t), '',
        '1. Read the framework first and follow it exactly:',
        '   operations/review/%s-%s-BRIEF.md' % (os.path.basename(w), t), '',
        '2. Verify the packet hashes, then read every packet file before judging:',
        '   %s/topics/%s/packet.sha256' % (w, t), '',
        '3. The deterministic pass has already run. Read it and do NOT re-count what it counted:',
        '   %s/topics/%s/qa_report.json' % (w, t),
        '   Its failures and warnings need your judgement; its not_run checks are areas where you are the only',
        '   line of defence. Both are listed in section 3 of the brief.', '',
        '4. The material under review:',
        '   %s/topics/%s/notes-*.md              (learner notes)' % (w, t),
        '   %s/topics/%s/content-units/*.json    (content units)' % (w, t),
        '   %s/topics/%s/learning-items/*.json   (flashcards and tasks)' % (w, t),
        '   %s/topics/%s/claims/canonical_claim_ledger.json' % (w, t), '',
        'Run the five reviewer roles, the bidirectional audit and the reconstruction test as section 5 of the brief',
        'describes. Apply the build-specific checks in section 4.', '',
        'Write your result to operations/review/%s-%s-review-r%d.yaml in the format given in section 6 of the'
        % (os.path.basename(w), t, rnd),
        'brief. Do not overwrite an earlier round; %d review(s) are already on file.' % done,
        'Fields: review_id, reviewer_role, packet_hash_verified, status, coverage_confirmed, reconstruction_test, issues.',
        'Change nothing else in the repository.', ''])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('root', help='repository root on THIS filesystem (used to read and write files)')
    ap.add_argument('workspace'); ap.add_argument('topic')
    ap.add_argument('--display-root', default=None,
                    help='the repository root as the REVIEWER will see it, when that differs from --root '
                         '(for example when this process runs inside a container mount). Written into the prompt.')
    a = ap.parse_args()
    d = build(a.root, a.workspace, a.topic)
    d['root'] = a.display_root or a.root
    if '/mnt/' in d['root'] or d['root'].startswith('/sessions/'):
        print('WARNING: the repo root written into the prompt looks like a container mount path (%s).\n'
              '         Pass --display-root with the path the reviewer will actually open.' % d['root'])
    outdir = os.path.join(a.root, 'operations', 'review')
    os.makedirs(outdir, exist_ok=True)
    tag = '%s-%s' % (os.path.basename(a.workspace.rstrip('/')), a.topic)
    bp = os.path.join(outdir, tag + '-BRIEF.md')
    pp = os.path.join(outdir, tag + '-PROMPT.txt')
    open(bp, 'w').write(md(d))
    open(pp, 'w').write(prompt(d))
    print('brief  -> operations/review/%s-BRIEF.md  (%d words)' % (tag, len(md(d).split())))
    print('prompt -> operations/review/%s-PROMPT.txt' % tag)


if __name__ == '__main__':
    main()
