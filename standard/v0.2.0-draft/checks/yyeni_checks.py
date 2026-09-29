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
import json, os, re, sys, glob, hashlib, itertools, datetime
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
        notes = self._find_notes()
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

    def _find_notes(self):
        """The notes filename is derived from the contract title (build/naming.py). Older builds
        used notes-<number>.md, so both are accepted and the derived name wins."""
        import sys as _sys
        _sys.path.insert(0, os.path.join(STANDARD, 'build'))
        cands = []
        try:
            from naming import notes_filename
            c = self._json_quiet(os.path.join(self.topic_dir, 'contract.json'))
            if c:
                p = os.path.join(self.topic_dir, notes_filename(self.topic_id, c.get('topic_title', '')))
                if os.path.exists(p):
                    cands.append(p)
        except Exception:
            pass
        cands += sorted(glob.glob(os.path.join(self.topic_dir, 'notes-*.md')))
        cands += [p for p in sorted(glob.glob(os.path.join(self.topic_dir, '*.md')))
                  if os.path.basename(p)[0].isdigit()]
        seen, out = set(), []
        for p in cands:
            if p not in seen:
                seen.add(p); out.append(p)
        return out

    @staticmethod
    def _json_quiet(p):
        try:
            return _json(p)
        except Exception:
            return None

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
    """A claims_seen stamp asserts a re-read. Advancing it while the artefact's own text is byte-identical to what
    it was at the previous stamp records a review that did not happen - unless the artefact says in
    reviewed_unchanged that re-reading genuinely found nothing to change."""
    bad, drift, unauditable, checked = [], [], [], 0
    def look(x, oid):
        nonlocal checked
        h = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
        rec, prior = x.get('authored_hash'), x.get('prior_hash')
        if not rec:
            return
        checked += 1
        if rec != h:
            drift.append(oid)                      # edited after stamping: the stamp no longer describes this text
            return
        advanced = any(v > 1 for v in (x.get('claims_seen') or {}).values())
        if not advanced:
            return
        if prior is None:
            # No record of the text before this stamp, so the stamp cannot be audited. That is a gap, not a
            # proven bulk stamp - the field did not exist when the stamp was made.
            unauditable.append(oid)
            return
        if prior == rec and not x.get('reviewed_unchanged'):
            bad.append(oid)
    for i in b.items:
        look(i, i['item_id'])
    for u in b.units:
        for blk in u.get('blocks', []):
            look(blk, '%s/%s' % (u['unit_id'], blk.get('block_id', '?')))
    if drift:
        return 'fail', ('%d artefacts were edited after their claims_seen stamp was made, so the stamp no longer '
                        'describes the text it certifies.' % len(drift)), drift
    if bad:
        return 'fail', ('%d artefacts advanced a claims_seen stamp while their own text stayed byte-identical, and '
                        'none records reviewed_unchanged. A stamp asserts a re-read; these record one that left no '
                        'trace (RS-41).' % len(bad)), bad
    if unauditable:
        return 'warn', ('%d advanced stamps carry no prior_hash, so they predate the audit trail and cannot be '
                        'verified. %d stamps are auditable and clean. Every stamp made from now on records the text '
                        'it replaced.' % (len(unauditable), checked - len(unauditable))), unauditable
    return 'pass', ('All %d stamped artefacts are consistent: every advanced stamp is matched by changed text or by a '
                    'recorded reviewed_unchanged decision.' % checked), []


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


@check('C-31', 'RS-17', 'Syllabus modality coverage')
def c31(b):
    """A syllabus that names a form - graphic, diagram, chart - makes that form part of the objective."""
    MODALITY = {
        'graph': ['chart', 'graph', 'axis', 'axes', 'plot', 'draw', 'diagram'],
        'graphic': ['chart', 'graph', 'axis', 'axes', 'plot', 'draw', 'diagram'],
        'diagram': ['diagram', 'draw', 'sketch', 'label'],
        'chart': ['chart', 'graph', 'plot', 'axis', 'draw'],
    }
    bad = []
    for oid in sorted(b.assessable):
        syl = (b.objectives[oid].get('syllabus_text') or '').lower()
        needed = set()
        for key, words in MODALITY.items():
            if re.search(r'\b' + key, syl):
                needed |= set(words)
        if not needed:
            continue
        # the modality must appear in an ITEM that practises the objective, not only in prose
        practised = False
        for i in b.items:
            if oid not in i.get('objective_ids', []):
                continue
            txt = (i.get('prompt') or '') + ' ' + (i.get('canonical_answer') or '')
            if any(re.search(r'\b' + w, txt, re.I) for w in needed):
                practised = True
                break
        if not practised:
            bad.append(oid)
    if bad:
        return 'fail', ('%d objectives name a form of representation in their syllabus wording (a chart, graph or '
                        'diagram) and no learning item practises it. Numeric coverage satisfies the calculation half '
                        'of the objective and leaves the other half untested.' % len(bad)), bad
    return 'pass', 'Every objective whose syllabus wording names a chart, graph or diagram is practised in that form.', []


@check('C-32', 'RS-22', 'Stated arithmetic is correct')
def c32(b):
    """Recompute every simple equation a model answer states. A wrong number in a worked answer is the worst
    defect a quantitative topic can ship, and it is entirely checkable."""
    NUM = r'[-+]?[\d][\d ,]*\.?\d*'
    def val(t):
        t = t.replace(' ', '').replace(',', '').replace('N$', '').replace('$', '').replace('%', '')
        try:
            return float(t)
        except ValueError:
            return None
    # A percentage result is the same equation scaled by 100; a chained expression (a = b = c) is matched by
    # its final step elsewhere in the string, so only take matches whose left operand starts the expression.
    # CR-006: the multiplication and division signs (x, *, /, and the typeset \u00d7 and \u00f7 a physics answer uses)
    pat = re.compile(r'(?<![\)\d])(?<![x*+/\-\u00d7\u00f7] )(?<!\d )(?:N\$)?(' + NUM + r')\s*([x*+\-/\u00d7\u00f7])\s*(?:N\$)?(' + NUM + r')\s*=\s*(?:N\$)?(' + NUM + r')\s*(%?)')
    bad, checked = [], 0
    for i in b.items:
        txt = (i.get('canonical_answer') or '')
        for m in pat.finditer(txt):
            a, op, c, r = val(m.group(1)), m.group(2), val(m.group(3)), val(m.group(4))
            if m.group(5) == '%' and r is not None:
                r = r / 100.0
            if a is None or c is None or r is None:
                continue
            # CR-006: binary arithmetic (0011 0110 + 0001 1011 = 0101 0001) is checked in base 2, and a result
            # written in a fixed width is checked modulo that width, which is how a register holds it
            raw = [re.sub(r'[ ,]', '', m.group(k)).lstrip('+').rstrip('.') for k in (1, 3, 4)]
            if all(re.fullmatch(r'[01]+', x) for x in raw) and any(len(x) >= 4 for x in raw) and op in '+-':
                checked += 1
                ba, bc, br = (int(x, 2) for x in raw)
                want = ba + bc if op == '+' else ba - bc
                if want != br and want % (2 ** len(raw[2])) != br:
                    bad.append('%s: "%s" gives %s in binary' % (i['item_id'], ' '.join(m.group(0).split()),
                                                              bin(want)[2:] if want >= 0 else '-' + bin(-want)[2:]))
                continue
            try:
                want = {'x': a * c, '*': a * c, '\u00d7': a * c, '+': a + c, '-': a - c, '/': (a / c if c else None),
                        '\u00f7': (a / c if c else None)}[op]
            except ZeroDivisionError:
                continue
            if want is None:
                continue
            checked += 1
            if abs(want - r) > max(0.02, abs(want) * 0.006):
                bad.append('%s: "%s" gives %s' % (i['item_id'], ' '.join(m.group(0).split()), round(want, 2)))
    if bad:
        return 'fail', '%d stated calculations do not evaluate as written: %s' % (len(bad), '; '.join(bad[:5])), \
               sorted({x.split(':')[0] for x in bad})
    return 'pass', 'All %d stated calculations in canonical answers evaluate correctly.' % checked, []


@check('C-33', 'RS-25', 'Flashcards are self-contained')
def c33(b):
    """A card that says "the same business" needs the facts, or a recorded prerequisite."""
    bad = []
    for i in b.items:
        if i.get('item_type') != 'flashcard':
            continue
        p = i.get('prompt') or ''
        # "on the same machines" inside a self-contained case is not a back-reference; a prompt that OPENS
        # with "The same ..." is.
        if not re.match(r'\s*(the same|as above|the above|that business|this business)\b', p, re.I):
            continue
        if i.get('prerequisite_item_ids'):
            continue
        bad.append(i['item_id'])
    if bad:
        return 'fail', ('%d flashcards refer back to an earlier card ("the same ...") without restating the facts, '
                        'recording a prerequisite, or carrying any figure of their own. Scheduled alone they cannot '
                        'be answered.' % len(bad)), bad
    return 'pass', 'No flashcard depends on facts held only in another card.', []


@check('C-34', 'RS-22', 'Interpretation is interpretation, not a second check')
def c34(b):
    """A CALC whose 'interpretation' only re-derives the answer has verified arithmetic, not interpreted it."""
    CHECKY = [r'\bcatch(es)? (an|a|the) (arithmetic )?(slip|error|mistake)\b', r'\bthe (two )?routes agree\b',
              r'\bagreement between\b', r'\bcheck the arithmetic\b', r'\bconfirms the (answer|figure)\b',
              r'\bquick way to catch\b', r'\bsecond route\b']
    bad = []
    for i in b.items:
        if i.get('subtype') not in ('CALC', 'INTERP'):
            continue
        g = ' '.join(i.get('marking_guidance') or [])
        m = re.search(r'Interpretation[:\s].*', g, re.I)
        line = m.group(0) if m else ''
        if re.search(r'\bis a check, not\b|\bnot an interpretation\b|\bnot merely re-derive\b', line, re.I):
            continue
        if line and any(re.search(c, line, re.I) for c in CHECKY):
            bad.append(i['item_id'])
    if bad:
        return 'fail', ('%d quantitative items name arithmetic verification as their interpretation. Re-deriving a '
                        'figure by a second route checks it; interpreting it means saying what it means for the '
                        'business.' % len(bad)), bad
    return 'pass', 'No quantitative item passes off an arithmetic check as interpretation.', []


@check('C-35', 'RS-22', 'Graphical stimulus is consistent and necessary')
def c35(b):
    """Prose cannot be checked algebraically, so a graphical item declares its chart in context.chart:
    {price, variable_cost, fixed_costs, current_output, asks}. The check recomputes every labelled value and
    fails a stem that states the value it asks the learner to read."""
    bad, checked = [], 0
    # CR-006: the declared-chart model is break-even (9609). A subject whose profile says
    # depictions.chart_model: none has no generated chart type, so C-35 checks only items that declare one,
    # and a fenced code block (```pseudocode) is code, not a chart.
    model = (((b.profile or {}).get('depictions') or {}).get('chart_model') or 'break_even')
    for i in b.items:
        txt = (i.get('prompt') or '')
        if model != 'break_even':
            if not (i.get('context') or {}).get('chart'):
                continue
            looks_graphical = True
        else:
            looks_graphical = bool(re.search(r'```(?!\s*(?:pseudocode|sql|text)\b)|\bchart\b|\bgraph\b', txt, re.I))
        ch = (i.get('context') or {}).get('chart')
        if not looks_graphical:
            continue
        if not ch:
            bad.append('%s presents a chart but declares no context.chart, so its coordinates cannot be verified'
                       % i['item_id'])
            continue
        checked += 1
        try:
            price, var, fc = float(ch['price']), float(ch['variable_cost']), float(ch['fixed_costs'])
        except (KeyError, TypeError, ValueError):
            bad.append('%s declares an unusable context.chart' % i['item_id'])
            continue
        if price <= var:
            bad.append('%s declares a chart whose revenue line never overtakes total cost' % i['item_id'])
            continue
        be = fc / (price - var)
        fc_cross = fc / price          # revenue also crosses the FIXED-COST line, and that is a real point
        # every number the stem or answer labels as a chart value must be one the chart actually produces
        body = txt + ' ' + (i.get('canonical_answer') or '')
        for m in re.finditer(r'(?:cross(?:ing|es)?|meet(?:s)?)(?:[^.]{0,40}?)at ([\d][\d ,]*) units', body, re.I):
            try:
                q = float(m.group(1).replace(' ', '').replace(',', ''))
            except ValueError:
                continue
            tol = max(1.0, be * 0.01)
            if abs(q - be) <= tol or abs(q - fc_cross) <= tol:
                continue               # the TR/TC crossing or the TR/FC crossing: both are on the chart
            bad.append('%s labels a crossing at %d units; its declared chart crosses total cost at %d and '
                       'fixed costs at %d' % (i['item_id'], round(q), round(be), round(fc_cross)))
        for m in re.finditer(r'At ([\d][\d ,]*) units[^.]{0,120}?revenue[^.]{0,40}?(?:N\$)?([\d][\d ,]*)', body, re.I):
            try:
                q = float(m.group(1).replace(' ', '').replace(',', ''))
                r = float(m.group(2).replace(' ', '').replace(',', ''))
            except ValueError:
                continue
            if abs(price * q - r) > max(1.0, r * 0.01):
                bad.append('%s reads revenue %d at %d units; its declared chart gives %d'
                           % (i['item_id'], round(r), round(q), round(price * q)))
        asks = ch.get('asks') or ''
        if 'break-even' in asks and re.search(r'(?:cross(?:ing)?|meet)(?:[^.]{0,40}?)at [\d][\d ,]* units', txt, re.I):
            bad.append('%s states the crossing point it asks the learner to read' % i['item_id'])
        if 'margin' in asks and re.search(r'(?:cross(?:ing)?|meet)(?:[^.]{0,40}?)at [\d][\d ,]* units', txt, re.I) \
                and re.search(r'current(?:ly)? (?:sells|output)', txt, re.I):
            bad.append('%s states both values its margin of safety is derived from' % i['item_id'])
        if 'profit' in asks and re.search(r'revenue line reads', txt, re.I) and re.search(r'cost line reads', txt, re.I):
            bad.append('%s states both line readings its profit is derived from' % i['item_id'])
    if bad:
        return 'fail', '%d graphical tasks are unsound: %s' % (len(bad), '; '.join(bad[:4])), \
               sorted({x.split(' ')[0] for x in bad})
    if not checked:
        return 'not_run', 'No graphical task in this topic, so nothing to verify.', []
    return 'pass', ('All %d graphical tasks declare their chart, every labelled coordinate recomputes correctly, and '
                    'none states the value it asks the learner to read.' % checked), []


@check('C-36', 'RS-22', 'Magnitude claims carry their figure')
def c36(b):
    """"Most of it", "almost nothing", "wipes out" - a claim about how big a change is must state the number,
    because a vague magnitude is where a correct calculation acquires a wrong conclusion."""
    VAGUE = [r'\bmost of (?:it|the profit|that)\b', r'(?<!tells you )(?<!says )\balmost nothing\b', r'\bwipes? out\b', r'\bvirtually none\b',
             r'\bbarely anything\b', r'\bwould remove most\b', r'\bleaves? (?:it )?with almost\b',
             r'\bnearly all of\b', r'\bhardly any\b']
    bad = []
    for i in b.items:
        if i.get('subtype') not in ('CALC', 'INTERP') and i.get('item_type') == 'flashcard':
            continue
        ans = i.get('canonical_answer') or ''
        for v in VAGUE:
            for m in re.finditer(v, ans, re.I):
                window = ans[max(0, m.start() - 160): m.end() + 160]
                if re.search(r'\d+\s*%|\bper cent\b|N\$\s?[\d ,]+', window):
                    continue
                bad.append('%s: "%s"' % (i['item_id'], ' '.join(window[max(0, m.start() - (m.start() - 40)):][:70].split())))
    if bad:
        return 'fail', ('%d quantitative answers make a claim about magnitude without the figure that supports it: '
                        '%s' % (len(bad), '; '.join(bad[:4]))), sorted({x.split(':')[0] for x in bad})
    return 'pass', 'Every magnitude claim in a quantitative answer is backed by a stated figure.', []


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
    """Nothing the contract excludes may appear in learner-facing text. An entry is a short term, or a
    declared {construct, pattern}. An entry written as a sentence or a tagged label can never match
    learner text, so it is reported as a failure rather than allowed to pass without looking: found
    2026-09-29, when every 0450 and 0455 contract carried syllabus notes and adjacent-topic guards in
    this list and C-11 had passed on all of them without enforcing anything."""
    entries = []
    dc = (b.contract or {}).get('depth_constraints', {}) or {}
    for key in ('excluded_constructs', 'out_of_scope_terms', 'excluded'):
        v = dc.get(key) or (b.contract or {}).get(key)
        if isinstance(v, list):
            entries.extend(v)
    if not entries:
        return 'not_run', 'The topic contract declares no excluded constructs, so nothing to scan for.', []
    scans, unscannable = [], []
    for e in entries:
        if isinstance(e, dict):
            name, pat = e.get('construct') or e.get('pattern'), e.get('pattern')
            try:
                scans.append((name, re.compile(pat, re.I)))
            except (re.error, TypeError):
                unscannable.append('%s (no pattern that compiles)' % name)
        elif isinstance(e, str):
            if '[' in e or e.rstrip().endswith('.') or len(e.split()) > 6:
                unscannable.append(e[:70])
            else:
                scans.append((e, re.compile(re.escape(e), re.I)))
    if unscannable:
        return 'fail', ('%d excluded_constructs entries are sentences or labels, not terms, so nothing can '
                        'enforce them: %s. Declare each as a short term or as {construct, pattern}; put '
                        'adjacent-topic guidance under depth_constraints.adjacent_topics.'
                        % (len(unscannable), '; '.join(unscannable[:4]))), []
    hits = []
    for owner, loc, text in b.learner_text() + b.answer_text():
        for name, rx in scans:
            if rx.search(text or ''):
                hits.append('%s:%s' % (owner, name))
    if hits:
        return 'fail', '%d excluded constructs appear in learner-facing material: %s' % (len(hits), ', '.join(sorted(set(hits))[:8])), sorted({h.split(':')[0] for h in hits})
    return 'pass', 'None of the %d constructs the contract excludes appears in learner-facing material.' % len(scans), []


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
    # AO4 is deliberately excluded from the deviation test. The framework's own rule is that the AO4 share is
    # met in practice time - essay plans, data-response tasks, case analyses - not by multiplying evaluation
    # flashcards. Measuring it by item count would push a build to do exactly what that rule forbids.
    measured = [a for a in tgt if a != 'AO4']
    worst = max(abs(share[a] - tgt[a]) for a in measured)
    perf = [i for i in b.items if i.get('item_type') != 'flashcard']
    ao4_items = [i for i in b.items if 'AO4' in i.get('assessment_objectives', [])]
    st = 'pass' if worst <= 6 else 'warn'
    msg = ('AO mix by item count %s against target %s; largest deviation across AO1-AO3 is %d points. AO4 is '
           'reported, not tested by count: %d items carry it, of which %d are performance tasks (%s). RS-19 '
           'measures the AO4 share in practice time.'
           % (share, tgt, worst, len(ao4_items), len(perf),
              ', '.join(sorted({i['item_type'] for i in perf})) or 'none'))
    if not perf:
        return 'warn', msg + ' No performance task exists, so no practice time carries AO4 at all.', []
    return st, msg, []


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
    """An exposure class names the subtypes an objective gets as a floor. Where a named subtype does not fit
    the objective, or would duplicate a card already held elsewhere, the topic contract waives it IN WRITING -
    padding the bank to satisfy a count teaches nothing, and a silent gap hides a real one. Waivers are
    reported on every run so they stay visible rather than becoming permanent."""
    if not b.exposure:
        return 'not_run', 'No exposure map, so no required subtypes to check.', []
    have = {}
    for i in b.items:
        for o in i.get('objective_ids', []):
            if i.get('subtype'):
                have.setdefault(o, set()).add(i['subtype'])
    waived = {(w.get('objective_id'), w.get('subtype')): w.get('reason', '')
              for w in ((b.contract or {}).get('subtype_waivers') or [])}
    missing, used, unreasoned = [], [], []
    for o in b.exposure.get('objectives', []):
        oid = o.get('objective_id')
        if oid not in b.branch:
            continue
        for st in (o.get('required_subtypes') or []):
            if st in have.get(oid, set()):
                continue
            if (oid, st) in waived:
                if len((waived[(oid, st)] or '').split()) < 12:
                    unreasoned.append('%s:%s' % (oid, st))
                used.append('%s:%s' % (oid, st))
            else:
                missing.append('%s:%s' % (oid, st))
    if unreasoned:
        return 'fail', ('%d subtype waivers carry no usable reason: %s. A waiver is a written justification, '
                        'not a switch.' % (len(unreasoned), ', '.join(sorted(unreasoned)))), sorted(unreasoned)
    if missing:
        return 'fail', ('%d exposure-required subtypes are missing and unwaived: %s'
                        % (len(missing), ', '.join(sorted(missing)[:8]))),\
               sorted({m.split(':')[0] for m in missing})
    stale = [k for k in waived if k[0] in b.branch and k[1] in have.get(k[0], set())]
    msg = 'Every exposure-required subtype is present or waived in writing.'
    if used:
        msg += ' %d waived: %s.' % (len(used), ', '.join(sorted(used)))
    if stale:
        msg += (' %d waivers are now redundant - the card exists: %s.'
                % (len(stale), ', '.join('%s:%s' % k for k in sorted(stale))))
    return 'pass', msg, sorted({u.split(':')[0] for u in used})


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


# --- conditions, completeness, derived metadata, units -------------------------

def _all_artefacts(b):
    """(owner_id, kind, text) for every authored artefact whose prose a learner or marker sees."""
    out = [(cid, 'claim', c.get('text') or '') for cid, c in b.claims.items()]
    for u in b.units:
        for blk in u.get('blocks', []):
            out.append((blk.get('block_id', '?'), 'block',
                        (blk.get('heading') or '') + ' ' + (blk.get('text') or '')))
    for i in b.items:
        out.append((i['item_id'], 'item',
                    (i.get('prompt') or '') + ' ' + (i.get('canonical_answer') or '') + ' '
                    + ' '.join(i.get('marking_guidance') or [])))
    return out


@check('C-37', 'RS-43', 'Conditioned mechanisms carry their conditions')
def c37(b):
    """A mechanism whose conclusion holds only under stated conditions is a different claim once the
    conditions are dropped. Repairing the condition into the claim and leaving the cards that teach the
    same mechanism unconditioned is how a fixed defect survives: the subject registers each such
    mechanism, and every artefact that asserts it must carry every condition."""
    reg = (b.profile or {}).get('conditioned_mechanisms') or []
    if not reg:
        return 'not_run', ('The subject profile registers no conditioned mechanisms, so there is nothing to '
                           'enforce. A subject with none has either no conditional reasoning or an unwritten '
                           'register.'), []
    bad, asserted = [], 0
    for owner, kind, text in _all_artefacts(b):
        if not text:
            continue
        for m in reg:
            trig = m.get('asserted_when') or []
            if not trig or not all(re.search(p, text, re.I) for p in trig):
                continue
            asserted += 1
            missing = [c['name'] for c in (m.get('required_conditions') or [])
                       if not any(re.search(p, text, re.I) for p in (c.get('any_of') or []))]
            if missing:
                bad.append('%s (%s) asserts %s without %s'
                           % (owner, kind, m.get('mechanism_id', '?'), ' or '.join(missing)))
    if bad:
        return 'fail', ('%d artefacts assert a registered conditioned mechanism without carrying its conditions: '
                        '%s' % (len(bad), '; '.join(bad[:5]))), sorted({x.split(' ')[0] for x in bad})
    if not asserted:
        return 'pass', ('No artefact asserts any of the %d registered conditioned mechanisms in this topic.'
                        % len(reg)), []
    return 'pass', ('All %d assertions of a registered conditioned mechanism carry every condition the register '
                    'requires.' % asserted), []


@check('C-38', 'RS-44', 'Answers do not supply their own facts')
def c38(b):
    """An answer that asserts a figure is the ONLY or TOTAL cost, when the stem never said so, rewards a
    learner for inventing the decisive fact. Either the stem establishes completeness, or the recommendation
    is explicitly conditional on checking it."""
    CLAIMS_COMPLETE = [
        r'\bthe only (?:cost|costs|factor|change|difference|expense)\b',
        r'\bno other (?:cost|costs|factor|expense|outlay)\b',
        r'\bnothing else (?:changes|is caused|is created|it causes)\b',
        r'\bno (?:further|additional) (?:cost|costs|expense)\b',
        r'\bmust establish that no other cost is created\b',
        r'\b(?:is|are) the (?:complete|total|whole) (?:variable|incremental|extra) cost\b',
    ]
    STEM_ESTABLISHES = [
        r'\btotal (?:variable|incremental|extra|additional) cost\b', r'\bin total\b',
        r'\bthe only (?:cost|costs|expense|charge|outlay)\b',
        r'\bno other (?:cost|costs|expense|charge|outlay)\b',
        r'\ball (?:its|the|other) (?:costs|variable costs|expenses)\b',
        r'\bcomplete (?:variable|incremental|per-unit)\b',
        r'\bnothing else (?:costs|is spent)\b', r'\ball in\b',
        r'\bcome to\b.{0,40}\bin all\b', r'\bevery other cost\b',
        # naming the cost CATEGORY states its total; enumerating named inputs does not
        r'\b(?:its|the) (?:total )?variable cost (?:is|of|comes to)\b',
        r'\bneed(?:ing|s)? no (?:setup|overtime|extra)\b', r'\bno setup\b', r'\bno overtime\b',
    ]
    CONDITIONAL = [r'\bprovided\b', r'\bassuming\b', r'\bif no other\b', r'\bsubject to\b',
                   r'\bconditional on\b', r'\bonce (?:it|she|he|they) (?:has|have) checked\b',
                   r'\bafter checking\b', r'\bso long as\b']
    bad, checked = [], 0
    for i in b.items:
        ans = (i.get('canonical_answer') or '') + ' || ' + ' '.join(i.get('marking_guidance') or [])
        stem = i.get('prompt') or ''
        for pat in CLAIMS_COMPLETE:
            m = re.search(pat, ans, re.I)
            if not m:
                continue
            checked += 1
            if any(re.search(p, stem, re.I) for p in STEM_ESTABLISHES):
                break
            if any(re.search(p, ans, re.I) for p in CONDITIONAL):
                break
            bad.append('%s: answer asserts "%s" but its prompt never establishes completeness'
                       % (i['item_id'], ' '.join(ans[max(0, m.start() - 30): m.end() + 30].split())))
            break
    if bad:
        return 'fail', ('%d answers rest on a completeness fact their own prompt does not supply: %s'
                        % (len(bad), '; '.join(bad[:4]))), sorted({x.split(':')[0] for x in bad})
    if not checked:
        return 'pass', 'No answer in this topic asserts a completeness fact.', []
    return 'pass', ('All %d completeness assertions are either established by the prompt or made conditional in '
                    'the answer.' % checked), []


@check('C-39', 'RS-45', 'Derived exposure metadata recomputes')
def c39(b):
    """Exposure metrics are derived data. Every figure must recompute from the evidence records, satisfy the
    file's own class definitions, and stand alone - a superseded figure retained beside the new one is a
    second source of truth waiting to be read. The canonical location is the nested `evidence` object; a
    metric duplicated at the top level of an entry is a leftover from a partial repair."""
    if not b.exposure or not b.evidence:
        return 'not_run', 'Exposure map or assessment evidence absent, so derived metrics cannot be recomputed.', []
    recs = b.evidence.get('records', b.evidence if isinstance(b.evidence, list) else [])
    agg = {}
    for r in recs:
        for oid in r.get('objective_ids', []):
            a = agg.setdefault(oid, {'parts': 0, 'series': set(), 'max': 0, 'cw': Counter()})
            a['parts'] += 1
            a['series'].add(r.get('exam_series'))
            a['max'] = max(a['max'], r.get('mark_tariff') or 0)
            if r.get('command_word'):
                a['cw'][r['command_word']] += 1
    classes = b.exposure.get('classes') or {}
    hi = re.search(r'(\d+) marks? or more', classes.get('probed_high', '') or '')
    hi_series = re.search(r'(\d+) or more distinct series', classes.get('probed_high', '') or '')
    lo = re.search(r'(\d+) marks? or fewer', classes.get('probed_low', '') or '')
    hi, lo = (int(hi.group(1)) if hi else None), (int(lo.group(1)) if lo else None)
    hi_series = int(hi_series.group(1)) if hi_series else None
    DUP = ('question_parts_naming_it', 'distinct_series', 'max_mark_tariff', 'max_tariff_observed',
           'command_words_observed')
    UNCOMPUTED = ('unmeasured_bullet_level', 'unmeasured_homonym_risk')
    bad, checked = [], 0
    for o in b.exposure.get('objectives', []):
        oid = o.get('objective_id')
        if oid not in b.branch:
            continue
        klass = o.get('exam_exposure')
        dup = [k for k in DUP if k in o]
        if dup:
            bad.append('%s duplicates %s at the top level of its entry, beside the nested evidence object the '
                       'rest of the file uses' % (oid, ', '.join(sorted(dup))))
        if klass in UNCOMPUTED:
            continue                       # a judgement about what the probe cannot distinguish, not a metric
        checked += 1
        a = agg.get(oid) or {'parts': 0, 'series': set(), 'max': 0, 'cw': Counter()}
        e = o.get('evidence') or {}
        if (e.get('question_parts_naming_it') or 0) != a['parts']:
            bad.append('%s records %s question parts; the evidence map has %d'
                       % (oid, e.get('question_parts_naming_it'), a['parts']))
        if (e.get('distinct_series') or 0) != len(a['series']):
            bad.append('%s records %s series; the evidence map has %d'
                       % (oid, e.get('distinct_series'), len(a['series'])))
        if (e.get('max_mark_tariff') or 0) != a['max']:
            bad.append('%s records a maximum tariff of %s; the evidence map has %d'
                       % (oid, e.get('max_mark_tariff'), a['max']))
        if dict(e.get('command_words_observed') or {}) != dict(a['cw']):
            bad.append('%s records a command-word mix the evidence map does not produce' % oid)
        if klass == 'probed_high' and hi is not None:
            if a['max'] < hi and not (hi_series and len(a['series']) >= hi_series):
                bad.append('%s is classed probed_high on %d marks across %d series; the file defines it as %d '
                           'marks or more, or %s or more series'
                           % (oid, a['max'], len(a['series']), hi, hi_series))
        if klass == 'probed_low' and lo is not None:
            if a['max'] > lo or (hi_series and len(a['series']) >= hi_series):
                bad.append('%s is classed probed_low on %d marks across %d series, which the file\'s own '
                           'definition puts above that class' % (oid, a['max'], len(a['series'])))
        if klass and klass.startswith('probed') and a['parts'] == 0:
            bad.append('%s is classed %s but no evidence record names it' % (oid, klass))
        if klass == 'unprobed_2020_2025' and a['parts'] > 0:
            bad.append('%s is classed unprobed but %d evidence records name it' % (oid, a['parts']))
    if bad:
        return 'fail', ('%d derived exposure figures do not recompute or contradict the file\'s own definitions: '
                        '%s' % (len(bad), '; '.join(bad[:5]))), sorted({x.split(' ')[0] for x in bad})
    if not checked:
        return 'not_run', 'No computed exposure entry for this topic branch.', []
    return 'pass', ('All %d computed exposure entries for this topic recompute from the evidence map, satisfy '
                    'the file\'s own class definitions, and keep no superseded figures.' % checked), []


@check('C-40', 'RS-46', 'Quantities are named in their own units')
def c40(b):
    """A margin of safety is units; a profit is currency. An answer that calls sixty haircuts "sixty haircuts
    of profit" teaches the learner to lose the mark that distinguishes them."""
    MONEY_IN_UNITS = r'\b\d[\d ,]*\s+([a-z]{3,}s)\s+of\s+(profit|loss|contribution|revenue|turnover)\b'
    UNITS_IN_MONEY = r'N\$\s?\d[\d ,]*\s+(?:units|haircuts|rolls|chairs|customers|items|hours)\b'
    ALLOWED = {'cents', 'dollars', 'rands', 'thousands', 'millions', 'units'}
    bad = []
    for owner, kind, text in _all_artefacts(b):
        for m in re.finditer(MONEY_IN_UNITS, text or '', re.I):
            if m.group(1).lower() in ALLOWED:
                continue
            bad.append('%s: "%s" names a currency amount in %s' % (owner, ' '.join(m.group(0).split()), m.group(1)))
        for m in re.finditer(UNITS_IN_MONEY, text or '', re.I):
            bad.append('%s: "%s" names a count in currency' % (owner, ' '.join(m.group(0).split())))
    if bad:
        return 'fail', ('%d quantities are named in the wrong units: %s' % (len(bad), '; '.join(bad[:4]))), \
               sorted({x.split(':')[0] for x in bad})
    return 'pass', 'No quantity is named in units it is not measured in.', []



@check('C-41', 'RS-47', 'Depictions are generated, not authored')
def c41(b):
    """C-35 verified a chart's declared parameters against the arithmetic stated about them, and passed four
    items whose learner-visible plot did not cross at all (SR-9609-5.4-CODEX-R4-001). Metadata checked against
    metadata cannot see the picture. So the picture is generated: this check re-renders every declared chart
    and fails any prompt whose plot is not byte-identical to what the renderer produces."""
    try:
        sys.path.insert(0, os.path.join(STANDARD, 'build'))
        from render_chart import render_break_even
    except Exception as exc:
        return 'fail', 'The chart renderer could not be loaded (%s), so no depiction can be verified.' % exc, []
    bad, checked = [], 0
    shown = [(i['item_id'], i.get('prompt') or '', (i.get('context') or {}).get('chart')) for i in b.items]
    for u in b.units:                       # the notes are rendered from blocks, so a block's plot counts too
        for blk in u.get('blocks', []):
            shown.append((blk.get('block_id', '?'), blk.get('text') or '', blk.get('chart')))
    model = (((b.profile or {}).get('depictions') or {}).get('chart_model') or 'break_even')
    code_langs = tuple(((b.profile or {}).get('depictions') or {}).get('code_fence_languages') or ('pseudocode', 'sql'))
    for oid, txt, ch in shown:
        if '```' not in txt:
            continue
        # CR-006: a fence that names a code language (```pseudocode) holds code, which is text, not a picture
        fences = re.findall(r'```([^\n`]*)\n', txt)
        if fences and all(f.strip().lower() in code_langs for f in fences[::2]) and not ch:
            continue
        if not ch:
            bad.append('%s shows a plot but declares no chart to render it from%s' % (
                oid, '' if model == 'break_even' else ' (this subject has no chart renderer: present data as a table, and label code fences with their language)'))
            continue
        try:
            want, _ = render_break_even(ch)
        except Exception as exc:
            bad.append('%s declares a chart the renderer rejects: %s' % (oid, exc))
            continue
        checked += 1
        if want not in txt:
            bad.append('%s shows a plot that is not what its declared parameters render to' % oid)
    if bad:
        return 'fail', ('%d depictions were authored rather than generated: %s. Regenerate them from '
                        'build/render_chart.py; do not hand-correct the characters.'
                        % (len(bad), '; '.join(bad[:4]))), sorted({x.split(' ')[0] for x in bad})
    if not checked:
        return 'not_run', 'No item in this topic shows a generated depiction.', []
    return 'pass', ('All %d depicted charts are byte-identical to what their declared parameters render to.'
                    % checked), []



@check('C-42', 'RS-45', 'Contract counts match the live build')
def c42(b):
    """A contract that authorises 92 items beside a bank of 105 has two numbers where a later rebuild, pacing
    calculation or publication gate needs one (SR-9609-5.4-CODEX-R4-004). Counts in the contract are derived
    data like any other: they are recomputed from the build, never left behind by it."""
    if not b.contract:
        return 'not_run', 'No topic contract, so there are no authorised counts to reconcile.', []
    dc = b.contract.get('depth_constraints') or {}
    ro = b.contract.get('required_outputs') or {}
    checks = [('depth_constraints.item_budget', dc.get('item_budget'), len(b.items), 'learning items'),
              ('required_outputs.learning_items', ro.get('learning_items'), len(b.items), 'learning items'),
              ('required_outputs.content_units', ro.get('content_units'), len(b.units), 'content units')]
    bad = [('%s says %s; the build has %d %s' % (name, got, want, what))
           for name, got, want, what in checks if got is not None and got != want]
    if bad:
        return 'fail', ('%d contract counts do not describe this build: %s. Recompute them from the build '
                        'rather than editing the build to match.' % (len(bad), '; '.join(bad))),                [n for n, g, w, _ in checks if g is not None and g != w]
    stated = [n for n, g, _, _ in checks if g is not None]
    if not stated:
        return 'warn', 'The contract authorises no counts, so nothing can be reconciled against the build.', []
    return 'pass', ('All %d counts the contract authorises match the build: %d learning items, %d content units.'
                    % (len(stated), len(b.items), len(b.units))), []


def read_practice_text(path):
    """A practice text is markdown with a YAML front-matter block. Returns (meta, body)."""
    raw = open(path, encoding='utf-8').read()
    if raw.startswith('---'):
        _, fm, body = raw.split('---', 2)
        meta = (yaml.safe_load(fm) if yaml else None) or {}
        return meta, body.strip()
    return {}, raw.strip()


@check('C-43', 'RS-48', 'Practice texts are declared, original and the stated length')
def c43(b):
    """A task answered from a text names it by context.text_id. The text is a file in the topic's texts/
    folder, declares itself original, and sits inside the length its task states - a 400-word "Text A"
    practises a different reading load from the 700-750 the paper sets. A text no task uses is waste."""
    tdir = os.path.join(b.topic_dir, 'texts')
    refs = {}
    for i in b.items:
        t = (i.get('context') or {}).get('text_id')
        if t:
            refs.setdefault(t, []).append(i['item_id'])
    files = {os.path.splitext(os.path.basename(p))[0]: p for p in glob.glob(os.path.join(tdir, '*.md'))}
    if not refs and not files:
        return 'not_run', 'No item in this topic is answered from a practice text.', []
    bad = []
    for t, owners in sorted(refs.items()):
        if t not in files:
            bad.append('%s: cited by %s but topics/%s/texts/%s.md does not exist' % (t, owners[0], b.topic_id, t))
            continue
        meta, body = read_practice_text(files[t])
        n = len(body.split())
        lo, hi = meta.get('words_min'), meta.get('words_max')
        if meta.get('text_id') != t:
            bad.append('%s: front matter text_id is %r' % (t, meta.get('text_id')))
        if meta.get('original') is not True:
            bad.append('%s: does not declare original: true' % t)
        if not isinstance(lo, int) or not isinstance(hi, int):
            bad.append('%s: declares no words_min/words_max' % t)
        elif not lo <= n <= hi:
            bad.append('%s: %d words, outside its stated %d-%d' % (t, n, lo, hi))
    orphans = sorted(set(files) - set(refs))
    if bad:
        return 'fail', '%d practice-text problems: %s' % (len(bad), '; '.join(bad[:6])), sorted({x.split(':')[0] for x in bad})
    if orphans:
        return 'warn', '%d practice texts are used by no item: %s' % (len(orphans), ', '.join(orphans)), orphans
    return 'pass', ('All %d practice texts cited by %d items exist, declare themselves original and sit inside '
                    'their stated length.' % (len(refs), sum(len(v) for v in refs.values()))), []


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

    # RS-42 (amended 2026-09-12). The deterministic suite gates publication. Semantic review does
    # not: it runs on published material and its findings are debt the topic carries visibly.
    # The decision Vitalis took, in his words: learners having thorough material with some errors
    # beats waiting months for material with fewer. Four rounds on two topics established that the
    # review loop does not converge - each round reviews what the last repair touched - so holding
    # publication behind it costs a subject that never ships.
    # A not_run check no longer holds publication. It used to, so that a missing input could never
    # pass silently - but most not_run results say the input genuinely does not apply ("no chart in
    # this topic"), and holding a whole subject for that costs more than it protects. They are named
    # in the blockers instead, so a reviewer knows exactly where code gave no opinion.
    decision = 'reject' if counts['fail'] else 'publish'
    silent = [r['check_id'] for r in results if r['status'] == 'not_run']
    if silent:
        blockers.append('No deterministic opinion on %d checks (%s) - on these a human or model reviewer is '
                        'the only line of defence.' % (len(silent), ', '.join(silent)))
    open_issues = [i for r in reviews for i in r.get('issues', []) if i.get('status') not in ('resolved', 'rejected')]
    blocking = [i for i in open_issues if i.get('severity') in ('critical', 'high')]
    reviewed = [r for r in reviews if r.get('status') != 'not_run']
    if counts['fail']:
        blockers.insert(0, 'Deterministic checks failed. This is the publication gate and it is not waivable.')
    if blocking:
        blockers.append('RS-42 - %d unresolved review issues ride with this release (%d critical, %d high). '
                        'They are debt, not a block: fix them in the maintenance pass and keep them open here '
                        'until they are fixed.'
                        % (len(blocking), sum(1 for i in blocking if i['severity'] == 'critical'),
                           sum(1 for i in blocking if i['severity'] == 'high')))
    carried = [i for i in open_issues if i.get('severity') in ('medium', 'low')]
    if carried:
        blockers.append('RS-42 - %d medium/low review issues carried open.' % len(carried))
    if not reviewed:
        blockers.append('RS-28 - no semantic review has run on this topic yet. Under the amended RS-42 that '
                        'does not hold publication; it schedules one.')

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
