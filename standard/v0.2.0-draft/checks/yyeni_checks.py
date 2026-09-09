"""
YYeni deterministic check suite - v0.2.0-draft.

Subject-agnostic. Everything the suite needs about a subject comes from the
workspace artifacts and the subject profile, never from this file.

Usage:
    python3 run_checks.py <workspace-dir> <topic-id> [--out qa_report.json]

Each check returns (status, message, affected_ids) and is tagged with the runtime
rule it enforces. Checks that cannot be evaluated because an input is absent
return `not_run` with the reason - never a silent pass.
"""
import json, os, re, glob, hashlib, itertools, datetime
from collections import Counter, defaultdict

try:
    import yaml
except ImportError:
    yaml = None

HERE = os.path.dirname(os.path.abspath(__file__))
STANDARD = os.path.dirname(HERE)
NEAR_DUP_THRESHOLD = 0.85


# ----------------------------------------------------------------------------- loading

def _json(path):
    with open(path) as fh:
        return json.load(fh)


def _yaml(path):
    if yaml is None:
        return None
    with open(path) as fh:
        return yaml.safe_load(fh)


class Build:
    """Everything one topic's checks need, discovered by convention."""

    def __init__(self, workspace, topic_id):
        self.workspace = workspace
        self.topic_id = topic_id
        self.topic_dir = os.path.join(workspace, 'topics', topic_id)
        self.missing = []

        self.registry = self._opt('curriculum/objective_registry.json')
        self.framework = self._opt('curriculum/assessment-framework.json')
        self.exposure = self._opt('curriculum/exam-exposure.json')
        self.glossary = self._opt('curriculum/glossary.json')
        self.budget = self._opt('curriculum/item-budget.json')
        self.evidence = self._opt('assessment-evidence/assessment_evidence.json')
        self.contract = self._opt_topic('contract.json')
        self.ledger = self._opt_topic('claims/canonical_claim_ledger.json')

        self.units = [_json(p) for p in sorted(glob.glob(os.path.join(self.topic_dir, 'content-units', '*.json')))]
        items_files = sorted(glob.glob(os.path.join(self.topic_dir, 'learning-items', '*.json')))
        self.items = []
        for p in items_files:
            d = _json(p)
            self.items.extend(d.get('items', d if isinstance(d, list) else []))
        notes = sorted(glob.glob(os.path.join(self.topic_dir, 'notes-*.md')))
        self.notes = open(notes[0]).read() if notes else None
        if not notes:
            self.missing.append('learner notes (topics/<id>/notes-*.md)')

        self.profile = None
        for cand in ('subject-profile.yaml', 'subject_profile.yaml'):
            p = os.path.join(workspace, cand)
            if os.path.exists(p):
                self.profile = _yaml(p)
                break

        self.patterns = _yaml(os.path.join(STANDARD, 'registers', 'language-patterns.yaml')) or {}

        # --- derived indexes
        self.claims = {c['claim_id']: c for c in (self.ledger or {}).get('claims', [])}
        self.objectives = {o['objective_id']: o for o in (self.registry or {}).get('objectives', [])}
        prefix = 'OBJ-'
        self.branch = {k: v for k, v in self.objectives.items() if v.get('topic_id') == topic_id}
        # assessable = has a parent; the topic container has parent_id None
        self.assessable = {k for k, v in self.branch.items() if v.get('parent_id')}
        self.flashcards = [i for i in self.items if i.get('item_type') == 'flashcard']
        self.performance = [i for i in self.items if i.get('item_type') != 'flashcard']

        self.claim_objs = {cid: set(c.get('objective_ids', [])) for cid, c in self.claims.items()}
        self.unit_claims = set()
        for u in self.units:
            for b in u.get('blocks', []):
                self.unit_claims.update(b.get('claim_ids', []))

    def _opt(self, rel):
        p = os.path.join(self.workspace, rel)
        if os.path.exists(p):
            return _json(p)
        self.missing.append(rel)
        return None

    def _opt_topic(self, rel):
        p = os.path.join(self.topic_dir, rel)
        if os.path.exists(p):
            return _json(p)
        self.missing.append('topics/%s/%s' % (self.topic_id, rel))
        return None

    # --- convenience
    def unit_prose(self):
        out = []
        for u in self.units:
            for b in u.get('blocks', []):
                out.append((u['unit_id'], b.get('block_id', '?'),
                            (b.get('heading') or '') + ' ' + (b.get('text') or '')))
        return out

    def learner_text(self):
        """Everything a learner reads: content-unit prose plus the offline notes."""
        out = self.unit_prose()
        if self.notes:
            out.append(('notes', 'notes', self.notes))
        return out

    def answer_text(self):
        return [(i['item_id'], 'answer', (i.get('prompt') or '') + ' || ' + (i.get('canonical_answer') or ''))
                for i in self.items]


# ----------------------------------------------------------------------------- helpers

def _hedged(span, hedges):
    return any(re.search(r'\b' + h + r'\b', span, re.I) for h in hedges)


def _scan(texts, patterns, hedges=(), window=90):
    """Return [(owner, pattern, excerpt)] for every unhedged pattern hit."""
    hits = []
    for owner, loc, text in texts:
        if not text:
            continue
        for pat in patterns:
            for m in re.finditer(pat, text, re.I):
                span = text[max(0, m.start() - window): m.end() + window]
                if hedges and _hedged(span, hedges):
                    continue
                hits.append((owner, pat, ' '.join(span.split())))
    return hits


def _norm_tokens(s):
    return re.sub(r'[^a-z0-9 ]', '', (s or '').lower()).split()


# ----------------------------------------------------------------------------- checks

CHECKS = []


def check(cid, rule, title):
    def deco(fn):
        CHECKS.append((cid, rule, title, fn))
        return fn
    return deco


# --- structure and traceability -------------------------------------------------

@check('C-00', 'RS-27', 'Schema validity')
def c00(b):
    try:
        import jsonschema
    except ImportError:
        return 'not_run', 'jsonschema is not installed; run pip3 install --user "jsonschema>=4.18".', []
    sd = os.path.join(STANDARD, 'schemas')
    pairs = [
        ('canonical_claim_ledger', os.path.join(b.topic_dir, 'claims/canonical_claim_ledger.json')),
        ('objective_registry', os.path.join(b.workspace, 'curriculum/objective_registry.json')),
    ]
    pairs += [('content_unit', p) for p in sorted(glob.glob(os.path.join(b.topic_dir, 'content-units', '*.json')))]
    pairs += [('learning_items', p) for p in sorted(glob.glob(os.path.join(b.topic_dir, 'learning-items', '*.json')))]
    bad = []
    checked = 0
    for name, path in pairs:
        sp = os.path.join(sd, name + '.schema.json')
        if not (os.path.exists(sp) and os.path.exists(path)):
            continue
        checked += 1
        errs = list(jsonschema.Draft202012Validator(_json(sp)).iter_errors(_json(path)))
        for e in errs[:3]:
            bad.append('%s %s: %s' % (os.path.basename(path), list(e.path)[:4], e.message[:120]))
    if bad:
        return 'fail', '%d schema violations: %s' % (len(bad), ' | '.join(bad[:4])), []
    return 'pass', 'All %d structured artifacts validate against the v0.2.0 schemas.' % checked, []


@check('C-01', 'RS-07', 'Objective referential integrity')
def c01(b):
    bad = set()
    for src in (b.items, b.units, list(b.claims.values())):
        for x in src:
            for o in x.get('objective_ids', []):
                if o not in b.objectives:
                    bad.add(o)
    if bad:
        return 'fail', '%d cited objective_ids do not resolve in the registry.' % len(bad), sorted(bad)
    return 'pass', ('Every objective_id cited by %d content units, %d items and %d claims resolves in the registry '
                    '(%d nodes in this topic branch, %d assessable).'
                    % (len(b.units), len(b.items), len(b.claims), len(b.branch), len(b.assessable))), []


@check('C-02', 'RS-07', 'Claim referential integrity')
def c02(b):
    dang = {c for i in b.items for c in i.get('claim_ids', []) if c not in b.claims}
    dang |= {c for c in b.unit_claims if c not in b.claims}
    if dang:
        return 'fail', '%d dangling claim references.' % len(dang), sorted(dang)
    return 'pass', 'Every claim_id cited by a content-unit block or learning item exists in the topic ledger.', []


@check('C-03', 'RS-07', 'Claim orphans')
def c03(b):
    cited = {c for i in b.items for c in i.get('claim_ids', [])} | b.unit_claims
    orph = sorted(set(b.claims) - cited)
    if orph:
        return 'warn', '%d ledger claims are cited by no block and no item.' % len(orph), orph
    return 'pass', 'All %d ledger claims are cited by at least one block or item.' % len(b.claims), []


@check('C-04', 'RS-40', 'Meaningful objective mapping')
def c04(b):
    """An item may only claim an objective one of its cited claims also serves."""
    bad = []
    for i in b.items:
        served = set()
        for cid in i.get('claim_ids', []):
            served |= b.claim_objs.get(cid, set())
        for o in i.get('objective_ids', []):
            if o not in served:
                bad.append('%s->%s' % (i['item_id'], o))
    if bad:
        holders = sorted({h.split('->')[0] for h in bad})
        return 'fail', ('%d (item, objective) mappings are not backed by any claim the item cites. '
                        'Coverage credit for those objectives is manufactured, not real. '
                        'Worst offenders: %s.'
                        % (len(bad), ', '.join(sorted(holders, key=lambda x: -sum(1 for h in bad if h.startswith(x)))[:3]))), holders
    return 'pass', 'Every (item, objective) mapping is backed by a cited claim that serves that objective.', []


@check('C-05', 'RS-05', 'Coverage floor - items (meaningful mappings only)')
def c05(b):
    covered = set()
    for i in b.items:
        served = set()
        for cid in i.get('claim_ids', []):
            served |= b.claim_objs.get(cid, set())
        covered |= (set(i.get('objective_ids', [])) & served)
    miss = sorted(b.assessable - covered)
    if miss:
        return 'fail', ('%d of %d assessable objectives have no learning item that genuinely practises them '
                        '(RS-40 mappings only).' % (len(miss), len(b.assessable))), miss
    return 'pass', 'All %d assessable objectives are practised by at least one item under RS-40.' % len(b.assessable), []


@check('C-06', 'RS-05', 'Coverage floor - content units')
def c06(b):
    cu = {o for u in b.units for o in u.get('objective_ids', [])}
    miss = sorted(b.assessable - cu)
    if miss:
        return 'fail', '%d assessable objectives are taught by no content unit.' % len(miss), miss
    return 'pass', 'All %d assessable objectives are taught by at least one content unit.' % len(b.assessable), []


@check('C-07', 'RS-39', 'Offline reconstructibility')
def c07(b):
    """Every claim an item leans on must also be taught in a content-unit block."""
    bad = []
    for i in b.items:
        for cid in i.get('claim_ids', []):
            if cid not in b.unit_claims:
                bad.append('%s:%s' % (i['item_id'], cid))
    if bad:
        items = sorted({x.split(':')[0] for x in bad})
        claims = sorted({x.split(':')[1] for x in bad})
        return 'fail', ('%d item-claim pairs rely on %d claims that no content-unit block teaches, across %d items. '
                        'A learner working offline from the notes cannot reconstruct those answers.'
                        % (len(bad), len(claims), len(items))), items
    return 'pass', 'Every claim cited by a learning item is also taught in a content-unit block.', []


def _artefact_text(x):
    if 'item_id' in x:
        return (x.get('prompt') or '') + '|' + (x.get('canonical_answer') or '') + '|' + '|'.join(x.get('marking_guidance') or [])
    return (x.get('heading') or '') + '|' + (x.get('text') or '')


@check('C-30', 'RS-41', 'No bulk stamp')
def c30(b):
    """A claims_seen stamp asserts a re-read. If the artefact's own text did not change, it did not happen."""
    checked, bad, unstamped = 0, [], 0
    def look(x, oid):
        nonlocal checked, unstamped
        h = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
        rec = x.get('authored_hash')
        if not rec:
            unstamped += 1
            return
        checked += 1
        if rec != h:
            return                       # text changed since stamping - that is a re-author, which is fine
        # text unchanged: the stamp is only credible if it was never advanced past revision 1
        if any(v > 1 for v in (x.get('claims_seen') or {}).values()):
            bad.append(oid)
    for i in b.items:
        look(i, i['item_id'])
    for u in b.units:
        for blk in u.get('blocks', []):
            look(blk, '%s/%s' % (u['unit_id'], blk.get('block_id', '?')))
    if bad:
        return 'fail', ('%d artefacts carry a claims_seen stamp above revision 1 while their own text is unchanged '
                        'from when the stamp was made. A stamp asserts a re-read; these record one that did not '
                        'happen (RS-41).' % len(bad)), bad
    if unstamped:
        return 'warn', ('%d artefacts carry no authored_hash, so their claims_seen stamps cannot be audited. '
                        '%d are auditable and clean.' % (unstamped, checked)), []
    return 'pass', 'Every claims_seen stamp is backed by an authored_hash and no bulk stamp was found.', []


@check('C-29', 'RS-41', 'No stale derivative')
def c29(b):
    """A claim whose text changed leaves every block and item citing it stale until re-authored."""
    rev = {cid: c.get('revision') for cid, c in b.claims.items()}
    if not any(rev.values()):
        return 'not_run', ('No claim carries a revision, so staleness cannot be computed. Bootstrap RS-41 revision '
                           'tracking on the ledger before relying on this check.'), []
    stale = []
    for i in b.items:
        seen = i.get('claims_seen') or {}
        for cid in i.get('claim_ids', []):
            cur = rev.get(cid) or 1
            if seen.get(cid, 0) != cur:
                stale.append('%s<-%s(r%s vs seen r%s)' % (i['item_id'], cid, cur, seen.get(cid, '-')))
    for u in b.units:
        for blk in u.get('blocks', []):
            seen = blk.get('claims_seen') or {}
            for cid in blk.get('claim_ids', []):
                cur = rev.get(cid) or 1
                if seen.get(cid, 0) != cur:
                    stale.append('%s/%s<-%s(r%s vs seen r%s)'
                                 % (u['unit_id'], blk.get('block_id', '?'), cid, cur, seen.get(cid, '-')))
    if stale:
        owners = sorted({x.split('<-')[0] for x in stale})
        return 'fail', ('%d citations are stale: the claim was rewritten and the block or item citing it was not. '
                        '%d artefacts affected. Correcting a claim is not a repair; propagating it is. First: %s'
                        % (len(stale), len(owners), ', '.join(stale[:6]))), owners
    return 'pass', 'No stale derivative: every block and item was authored against the current revision of every claim it cites.', []


# NOTE (RS-39). A deeper reconstructibility check was written and withdrawn: flagging canonical
# answers that use vocabulary the notes never use fired on 47 of 68 items on the pilot topic,
# because ordinary English variation swamps genuinely untaught mechanisms. C-07 is therefore the
# mechanical floor for RS-39 - every claim an item cites must also be taught - and the deeper
# question ("could an offline learner actually build this answer from the notes?") is a named
# reviewer task in the review brief. Recorded here so nobody rewrites the same failed check.

# --- language and claim discipline ----------------------------------------------

@check('C-08', 'RS-33', 'Unqualified universals')
def c08(b):
    pats = b.patterns.get('unqualified_universals', [])
    hedges = b.patterns.get('hedges', [])
    texts = [(cid, 'claim', c.get('text', '')) for cid, c in b.claims.items()
             if not c.get('generality')] + b.learner_text() + b.answer_text()
    hits = _scan(texts, pats, hedges)
    if hits:
        owners = sorted({h[0] for h in hits})
        return 'fail', ('%d unqualified universal or exclusivity statements across %d locations. '
                        'Each is either a tendency written as a rule, or a genuine universal that must declare '
                        'generality: definitional | legal | arithmetic. First: "%s"'
                        % (len(hits), len(owners), hits[0][2][:160])), owners
    return 'pass', 'No unqualified universal or exclusivity statement found in claims, learner prose or answers.', []


@check('C-09', 'RS-21', 'Third-party certainty')
def c09(b):
    pats = b.patterns.get('third_party_certainty', [])
    hedges = b.patterns.get('hedges', [])
    hits = _scan([(cid, 'claim', c.get('text', '')) for cid, c in b.claims.items()] + b.learner_text() + b.answer_text(),
                 pats, hedges)
    if hits:
        owners = sorted({h[0] for h in hits})
        return 'fail', ('%d statements assert what an independent third party will do, across %d locations. '
                        'These must be likelihood with a reason. First: "%s"'
                        % (len(hits), len(owners), hits[0][2][:160])), owners
    return 'pass', 'No statement asserts a third party\'s decision as certain.', []


@check('C-10', 'RS-36', 'Assessment-priority claims need assessment evidence')
def c10(b):
    pats = b.patterns.get('assessment_priority', [])
    status = (b.evidence or {}).get('status')
    hits = _scan(b.learner_text(), pats)
    if not hits:
        return 'pass', 'No learner-facing claim about examiner behaviour, mark priority or question frequency.', []
    owners = sorted({h[0] for h in hits})
    if status and status != 'complete':
        return 'fail', ('%d learner-facing assessment-priority claims across %d locations, while assessment_evidence '
                        'status is "%s". RS-36 forbids these until mapped evidence exists. First: "%s"'
                        % (len(hits), len(owners), status, hits[0][2][:160])), owners
    return 'warn', ('%d learner-facing assessment-priority claims across %d locations; each needs a mapped '
                    'assessment-evidence record.' % (len(hits), len(owners))), owners


@check('C-11', 'RS-15', 'Scope discipline - excluded constructs')
def c11(b):
    excl = []
    dc = (b.contract or {}).get('depth_constraints', {}) or {}
    for key in ('excluded_constructs', 'out_of_scope_terms', 'excluded'):
        v = dc.get(key) or (b.contract or {}).get(key)
        if isinstance(v, list):
            excl.extend([x for x in v if isinstance(x, str)])
    if not excl:
        return 'not_run', 'The topic contract declares no excluded constructs, so nothing to scan for.', []
    hits = []
    for owner, loc, text in b.learner_text() + b.answer_text():
        for t in excl:
            if re.search(re.escape(t), text or '', re.I):
                hits.append('%s:%s' % (owner, t))
    if hits:
        return 'fail', '%d excluded constructs appear in learner-facing material: %s' % (len(hits), ', '.join(sorted(set(hits))[:8])), sorted({h.split(':')[0] for h in hits})
    return 'pass', 'None of the %d constructs the contract excludes appears in learner-facing material.' % len(excl), []


@check('C-12', 'RS-35', 'Variant completeness')
def c12(b):
    reg = ((b.profile or {}).get('variant_register') or [])
    if not reg:
        return 'not_run', ('The subject profile declares no variant_register. RS-35 cannot be checked until a human '
                           'records which terms in this subject have consequential variants.'), []
    # Scan per content-unit block, not per character window: a block is the unit a learner reads as one
    # passage, so a variant named three sections away has not been named where the term is taught.
    passages = [(u['unit_id'] + '/' + blk.get('block_id', '?'), (blk.get('heading') or '') + ' ' + (blk.get('text') or ''))
                for u in b.units for blk in u.get('blocks', [])]
    bad = []
    for entry in reg:
        term = entry.get('term') if isinstance(entry, dict) else entry
        variants = (entry.get('variants') or []) if isinstance(entry, dict) else []
        if not term or len(variants) < 2:
            continue
        here = [(oid, txt) for oid, txt in passages if re.search(r'\b' + re.escape(term) + r'\b', txt, re.I)]
        if not here:
            continue
        local = ' '.join(txt for _, txt in here)
        named = [v for v in variants if re.search(r'\b' + re.escape(v) + r'\b', local, re.I)]
        if len(named) < len(variants):
            bad.append('%s (names %d of %d forms: missing %s)'
                       % (term, len(named), len(variants),
                          ', '.join(v for v in variants if v not in named)))
    if bad:
        return 'fail', 'Terms taught in only one of their consequential forms: %s.' % '; '.join(bad), [x.split(' (')[0] for x in bad]
    return 'pass', 'Every variant-register term used in this topic names its consequential forms.', []


@check('C-13', 'RS-34', 'Generalisations declare their scope')
def c13(b):
    # Markers of a grouping or across-the-board statement. Kept narrow on purpose: a marker that fires on
    # ordinary prose ("every source" as a reading instruction, "family" meaning relatives) trains people to
    # add generalisation_scope to blocks that make no generalisation, which defeats the rule.
    markers = [r'\b(?:all|every|each) (?:internal|external) sources?\b',
               r'\b(?:every|each) (?:source|method|type|form) (?:is|are|has|have|shares?|carries|costs?|can|must|needs?)\b',
               r'\b(?:two|three|four|five) (?:families|groups|categories|kinds)\b',
               r'\bfamilies of\b', r'\bsort any\b',
               r'\b(?:they|these|all of them) (?:all )?share (?:the same|one)\b',
               r'\bin every case\b', r'\bwithout exception\b']
    flagged = []
    for u in b.units:
        for blk in u.get('blocks', []):
            text = (blk.get('heading') or '') + ' ' + (blk.get('text') or '')
            if any(re.search(m, text, re.I) for m in markers) and not blk.get('generalisation_scope'):
                flagged.append('%s/%s' % (u['unit_id'], blk.get('block_id', '?')))
    if flagged:
        return 'fail', ('%d content blocks make a grouping or across-the-board statement without declaring '
                        'generalisation_scope, so no check can confirm the grouping holds for its members (RS-34).'
                        % len(flagged)), flagged
    return 'pass', 'Every grouping or across-the-board statement declares the members it claims to hold for.', []


# --- assessment alignment --------------------------------------------------------

def _cw_used(b):
    return [c for c in (b.framework or {}).get('command_words', []) if c.get('used_at_as') or c.get('used_at_level')]


def _cw_unused(b):
    return [c for c in (b.framework or {}).get('command_words', [])
            if not (c.get('used_at_as') or c.get('used_at_level'))]


@check('C-14', 'RS-19', 'Command-word discipline')
def c14(b):
    if not b.framework:
        return 'not_run', 'No assessment framework in the workspace.', []
    forb = [c['word'] for c in _cw_unused(b)]
    hits = []
    for i in b.items:
        for w in forb:
            if re.search(r'(^|[.;:]\s*|\band\s+)' + w + r'\b', i.get('prompt', ''), re.I):
                hits.append('%s:%s' % (i['item_id'], w))
    if hits:
        return 'fail', ('%d item prompts instruct with a command word this level does not use (%s): %s'
                        % (len(hits), ', '.join(forb), ', '.join(hits))), sorted({h.split(':')[0] for h in hits})
    return 'pass', 'No item prompt instructs with a command word absent from this level (%s).' % ', '.join(forb), []


@check('C-15', 'RS-37', 'Command-word-shaped practice')
def c15(b):
    if not b.framework:
        return 'not_run', 'No assessment framework in the workspace.', []
    used = {c['word'].lower() for c in _cw_used(b)}
    by_obj = defaultdict(list)
    for i in b.items:
        served = set()
        for cid in i.get('claim_ids', []):
            served |= b.claim_objs.get(cid, set())
        for o in set(i.get('objective_ids', [])) & served:
            by_obj[o].append(i)
    bad = []
    for o in sorted(b.assessable):
        cws = [w.lower() for w in (b.objectives[o].get('command_words') or []) if w.lower() in used]
        if not cws:
            continue
        ok = False
        for i in by_obj.get(o, []):
            p = i.get('prompt', '')
            if any(re.search(r'\b' + w + r'\b', p, re.I) for w in cws):
                ok = True
                break
        if not ok:
            bad.append('%s (needs %s)' % (o, '/'.join(cws)))
    if bad:
        return 'fail', ('%d objectives have no item whose prompt instructs with one of their own command words, '
                        'so they are covered but not practised in the shape the paper asks for: %s'
                        % (len(bad), '; '.join(bad[:6]) + (' ...' if len(bad) > 6 else ''))), [x.split(' ')[0] for x in bad]
    return 'pass', 'Every objective with a command word carries an item that instructs with one of them.', []


@check('C-16', 'RS-38', 'Declared answer structures')
def c16(b):
    structs = ((b.profile or {}).get('answer_structures') or {})
    if not structs:
        return 'not_run', ('The subject profile declares no answer_structures. RS-38 cannot be checked until the '
                           'required parts of each item subtype are written down.'), []
    bad = []
    for i in b.items:
        parts = structs.get(i.get('subtype') or i.get('item_type'))
        if not parts:
            continue
        # Guidance only, deliberately. This checks that the RUBRIC tells a marker what to look for.
        # Whether the answer actually DOES each part is a semantic judgement and belongs to the reviewer;
        # scanning the answer for part keywords rewards vocabulary rather than structure.
        guidance = ' '.join(i.get('marking_guidance') or []).lower()
        missing = []
        for part in parts:
            alts = [a.strip().lower() for a in str(part).split('|') if a.strip()]
            if not any(re.search(r'\b' + re.escape(a) + r'\b', guidance) for a in alts):
                missing.append(alts[0])
        if missing:
            bad.append('%s (missing: %s)' % (i['item_id'], ', '.join(missing)))
    if bad:
        return 'fail', ('%d items do not name every declared part of their subtype answer structure in marking '
                        'guidance: %s' % (len(bad), '; '.join(bad[:6]) + (' ...' if len(bad) > 6 else ''))), [x.split(' ')[0] for x in bad]
    return 'pass', 'Every item names all declared parts of its subtype answer structure.', []


@check('C-17', 'RS-19', 'Subtype to AO consistency')
def c17(b):
    if not b.framework:
        return 'not_run', 'No assessment framework.', []
    smap = {m['subtype']: set(m['assessment_objectives']) for m in b.framework.get('flashcard_subtype_ao_map', [])}
    if not smap:
        return 'not_run', 'The framework declares no subtype-to-AO map.', []
    bad = [i['item_id'] for i in b.items if i.get('subtype')
           and (i['subtype'] not in smap or not set(i.get('assessment_objectives', [])) <= smap[i['subtype']])]
    if bad:
        return 'fail', '%d items assert an assessment objective their subtype does not carry.' % len(bad), bad
    return 'pass', "Every item's assessment objectives are permitted by its subtype.", []


@check('C-18', 'RS-19', 'AO mix against target')
def c18(b):
    tgt = ((b.framework or {}).get('item_mix_target') or {}).get('target_share_percent')
    if not tgt:
        return 'not_run', 'The framework declares no AO target share.', []
    aoc = Counter(a for i in b.items for a in i.get('assessment_objectives', []))
    tot = sum(aoc.values()) or 1
    share = {a: round(100 * aoc[a] / tot) for a in tgt}
    worst = max(abs(share[a] - tgt[a]) for a in tgt)
    st = 'pass' if worst <= 6 else 'warn'
    return st, 'AO mix by item count %s against target %s; largest deviation %d points.' % (share, tgt, worst), []


# --- item integrity ---------------------------------------------------------------

@check('C-19', 'RS-25', 'Flashcard integrity')
def c19(b):
    bad = [i['item_id'] for i in b.flashcards if not i.get('canonical_answer') or not i.get('subtype')]
    if bad:
        return 'fail', '%d flashcards lack a canonical answer or a subtype.' % len(bad), bad
    return 'pass', 'All %d flashcards carry a non-null canonical answer and a declared subtype.' % len(b.flashcards), []


@check('C-20', 'RS-25', 'One target per flashcard')
def c20(b):
    bad = []
    for i in b.flashcards:
        p = i.get('prompt', '')
        if re.search(r'\b(three|four|five|both|each of the)\b.*\b(and|,)\b', p, re.I) and re.search(r'\bmatch|list|name\b', p, re.I):
            bad.append(i['item_id'])
    if bad:
        return 'warn', ('%d flashcards ask for several separate answers in one card, which is hard to retrieve and '
                        'hard to diagnose; consider a performance item instead.' % len(bad)), bad
    return 'pass', 'No flashcard asks for several separate answers in one card.', []


@check('C-21', 'RS-25', 'Duplicate prompts')
def c21(b):
    pr = [(i['item_id'], _norm_tokens(i.get('prompt'))) for i in b.items]
    seen, exact, near = {}, [], []
    for iid, tk in pr:
        k = ' '.join(tk)
        if k in seen:
            exact.append('%s|%s' % (seen[k], iid))
        seen[k] = iid
    for (a, ta), (bb, tb) in itertools.combinations(pr, 2):
        sa, sb = set(ta), set(tb)
        if sa and sb and len(sa & sb) / len(sa | sb) > NEAR_DUP_THRESHOLD:
            near.append('%s|%s' % (a, bb))
    if exact or near:
        return 'fail', '%d exact and %d near-duplicate prompt pairs.' % (len(exact), len(near)), exact + near
    return 'pass', 'No exact duplicate and no near-duplicate prompt pair above %.2f Jaccard across %d items.' % (NEAR_DUP_THRESHOLD, len(b.items)), []


@check('C-22', 'RS-30', 'Marking guidance present')
def c22(b):
    bad = [i['item_id'] for i in b.items if not i.get('marking_guidance')]
    if bad:
        return 'fail', '%d items carry no marking guidance.' % len(bad), bad
    return 'pass', 'All %d items carry marking guidance.' % len(b.items), []


@check('C-23', 'RS-12', 'Items cite a claim')
def c23(b):
    bad = [i['item_id'] for i in b.items if not i.get('claim_ids')]
    if bad:
        return 'fail', '%d items cite no ledger claim.' % len(bad), bad
    return 'pass', 'Every item cites at least one ledger claim.', []


# --- publication state --------------------------------------------------------------

@check('C-24', 'RS-13', 'Publication gate')
def c24(b):
    pub = [c for c, v in b.claims.items() if v.get('publishable')]
    ver = [c for c, v in b.claims.items() if (v.get('verification') or {}).get('status') not in (None, 'unverified')]
    gap = [c for c, v in b.claims.items() if v.get('provenance') == 'generated_gap']
    if pub or ver:
        return 'fail', '%d claims marked publishable and %d marked verified before review.' % (len(pub), len(ver)), pub + ver
    return 'pass', ('Gate holds: 0 of %d claims are publishable or verified. %d are generated_gap and need documented '
                    'human approval (RS-13).' % (len(b.claims), len(gap))), []


@check('C-25', 'RS-31', 'QA status consistency')
def c25(b):
    bad = [i['item_id'] for i in b.items if i.get('qa_status') not in ('review_required', 'reviewed', 'approved')]
    bad += [u['unit_id'] for u in b.units if u.get('qa_status') not in ('review_required', 'reviewed', 'approved')]
    if bad:
        return 'fail', '%d artifacts carry an unrecognised qa_status.' % len(bad), bad
    return 'pass', 'Every content unit and item carries a recognised qa_status.', []


@check('C-26', 'RS-09', 'Word budget')
def c26(b):
    bad = [u['unit_id'] for u in b.units
           if u.get('word_budget') and not (u['word_budget'].get('min', 0) <= u.get('word_count', 0) <= u['word_budget'].get('max', 10 ** 9))]
    if bad:
        return 'warn', '%d content units sit outside their declared word budget.' % len(bad), bad
    return 'pass', 'All %d content units sit inside their declared word budget (%d words total).' % (len(b.units), sum(u.get('word_count', 0) for u in b.units)), []


@check('C-27', 'RS-05', 'Exposure required subtypes')
def c27(b):
    if not b.exposure:
        return 'not_run', 'No exposure artifact in the workspace.', []
    EX = {e['objective_id']: e for e in b.exposure.get('objectives', [])}
    by_obj = defaultdict(set)
    for i in b.items:
        for o in i.get('objective_ids', []):
            by_obj[o].add(i.get('subtype'))
    bad = []
    for o in sorted(b.assessable):
        for s in (EX.get(o, {}).get('required_subtypes') or []):
            if s not in by_obj[o]:
                bad.append('%s:%s' % (o, s))
    if bad:
        return 'fail', '%d exposure-required subtypes are missing: %s' % (len(bad), ', '.join(bad[:8])), sorted({x.split(':')[0] for x in bad})
    mapped = sum(1 for o in b.assessable if o in EX)
    return 'pass', 'Exposure required-subtype floor honoured for all %d mapped objectives; exposure changes item type, never item presence (RS-05).' % mapped, []


@check('C-28', 'RS-32', 'Packet hash manifest')
def c28(b):
    files = []
    for rel in ('qualification-profile.yaml', 'subject-profile.yaml', 'curriculum/objective_registry.json',
                'curriculum/assessment-framework.json', 'curriculum/exam-exposure.json', 'curriculum/glossary.json',
                'curriculum/dependency_graph.json', 'curriculum/item-budget.json', 'inventory/source_inventory.json',
                'assessment-evidence/assessment_evidence.json'):
        p = os.path.join(b.workspace, rel)
        if os.path.exists(p):
            files.append((rel, p))
    for p in sorted(glob.glob(os.path.join(b.topic_dir, '**', '*.*'), recursive=True)):
        files.append((os.path.relpath(p, b.workspace), p))
    lines = []
    for rel, p in files:
        # A manifest cannot contain its own hash - the file changes the moment the line is written,
        # so the entry is unverifiable by construction. The manifest's own hash is written beside it.
        if os.path.basename(p) in ('qa_report.json', 'packet.sha256', 'packet.sha256.hash'):
            continue
        with open(p, 'rb') as fh:
            lines.append('%s  %s' % (hashlib.sha256(fh.read()).hexdigest(), rel))
    out = os.path.join(b.topic_dir, 'packet.sha256')
    body = '\n'.join(sorted(lines)) + '\n'
    with open(out, 'w') as fh:
        fh.write(body)
    own = hashlib.sha256(body.encode()).hexdigest()
    with open(out + '.hash', 'w') as fh:
        fh.write('%s  packet.sha256\n' % own)
    return 'pass', ('Critic-packet hash manifest written for %d files to topics/%s/packet.sha256; the manifest\'s own '
                    'SHA-256 is detached in packet.sha256.hash (%s) so the whole packet is verifiable.'
                    % (len(lines), b.topic_id, own[:16])), []


# ----------------------------------------------------------------------------- runner

def run(workspace, topic_id):
    b = Build(workspace, topic_id)
    results, rule_index = [], {}
    for cid, rule, title, fn in CHECKS:
        try:
            status, msg, ids = fn(b)
        except Exception as exc:                                  # a broken check is a failed check
            status, msg, ids = 'fail', 'Check raised %s: %s' % (type(exc).__name__, exc), []
        results.append({'check_id': cid, 'status': status,
                        'message': '[%s %s] %s' % (rule, title, msg),
                        'affected_ids': sorted(str(x) for x in ids)[:200]})
        rule_index.setdefault(rule, []).append((cid, status))

    counts = Counter(r['status'] for r in results)
    blockers = []
    for r in results:
        if r['status'] == 'fail':
            blockers.append('%s %s' % (r['check_id'], r['message']))
    if b.missing:
        blockers.append('Packet incomplete - absent inputs: %s.' % ', '.join(sorted(set(b.missing))))

    # Carry forward any semantic review already on file. A deterministic run must never erase a
    # reviewer's verdict, and must never upgrade the release decision past an open review.
    prev = {}
    prev_path = os.path.join(b.topic_dir, 'qa_report.json')
    if os.path.exists(prev_path):
        try:
            prev = _json(prev_path)
        except Exception:
            prev = {}
    reviews = [r for r in prev.get('semantic_reviews', []) if r.get('issues') or r.get('status') != 'not_run']
    if not reviews:
        reviews = [{'review_id': 'SR-%s-PENDING' % topic_id, 'reviewer_role': 'combined',
                    'status': 'not_run', 'issues': []}]

    decision = 'reject' if counts['fail'] else ('hold' if counts['warn'] or counts['not_run'] else 'pass')
    # A stored verdict applies to the version it reviewed. What still blocks release is an UNRESOLVED
    # issue; a review that said reject and whose issues are all resolved leaves the build awaiting a
    # re-review, not rejected forever. Resolution is the author's claim, so it can never reach 'pass'
    # on its own.
    open_issues = [i for r in reviews for i in r.get('issues', []) if i.get('status') not in ('resolved', 'rejected')]
    blocking = [i for i in open_issues if i.get('severity') in ('critical', 'high')]
    carried = [i for i in open_issues if i.get('severity') in ('medium', 'low')]
    reviewed = [r for r in reviews if r.get('status') != 'not_run']
    if blocking:
        decision = 'reject'
        blockers.insert(0, 'RS-42 - %d blocking review issues open (%d critical, %d high).'
                        % (len(blocking), sum(1 for i in blocking if i['severity'] == 'critical'),
                           sum(1 for i in blocking if i['severity'] == 'high')))
    elif not reviewed:
        decision = 'hold' if decision == 'pass' else decision
        blockers.insert(0, 'RS-28 - no independent semantic review has been run on this topic.')
    elif carried:
        if decision == 'pass':
            decision = 'hold'
        blockers.insert(0, 'RS-42 - releasable on severity (%d medium/low issues carried open), but the repaired '
                           'build has not been re-reviewed. Carried issues stay open in this report.' % len(carried))
    elif any(r.get('issues') for r in reviewed):
        if decision == 'pass':
            decision = 'hold'
        blockers.insert(0, 'RS-28 - every issue from the last review is marked resolved by the author, which is a '
                           'claim rather than a verdict. The repaired build has not been re-reviewed.')
    elif any(r.get('status') == 'reject' for r in reviewed):
        decision = 'reject'
        blockers.insert(0, 'RS-28 - a semantic review stands as reject.')

    return {
        'qa_report_id': 'QA-%s-%s' % (os.path.basename(workspace.rstrip('/')), topic_id),
        'build_id': '%s/topic-%s' % (os.path.basename(workspace.rstrip('/')), topic_id),
        'generated_at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'deterministic_checks': results,
        'semantic_reviews': reviews,
        'blockers': blockers,
        'metrics': {'objective_count': len(b.assessable), 'claim_count': len(b.claims),
                    'content_unit_count': len(b.units), 'learning_item_count': len(b.items),
                    'word_count': sum(u.get('word_count', 0) for u in b.units)},
        'release_decision': decision,
        'notes': ['Standard v0.2.0-draft check suite. %d checks: %d pass, %d fail, %d warn, %d not_run.'
                  % (len(results), counts['pass'], counts['fail'], counts['warn'], counts['not_run']),
                  'A not_run check means an input the check needs is absent. It is never a pass.',
                  'RS-30: these are mechanical results computed by code. They say nothing about whether the '
                  'material teaches the subject well.'],
    }
