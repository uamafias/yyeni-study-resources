# -*- coding: utf-8 -*-
"""Turn each syllabus-stated content limit into something C-11 can actually scan for.

    python3 scope_scan.py            # writes curriculum/scope-scan.json for 0450 and 0455

Two layers, kept apart. The SENTENCE is the syllabus's (curriculum/syllabus-exclusions.json, page
cited, verified against the PDF here). The SCAN is our judgement: the words or pattern that would
appear in learner-facing text if an author taught past the limit. A limit applies to the whole
subject, not only the topic that states it: nothing else in the syllabus teaches marginal cost.

Found 2026-09-29: the contracts carried the sentences themselves, tagged, as excluded_constructs.
C-11 searches learner text for each entry verbatim, so a sentence could never match and the check
passed without looking. An author could have taught the PED formula and every check would pass.
"""
import json, os, re, subprocess, sys
HOME = os.path.expanduser('~')
REPO = os.environ.get('YYENI_REPO') or os.path.join(HOME, 'mnt', 'YYeni Study Resources')
SYL_REPO = os.path.join(HOME, 'mnt', 'YYeni Study Resources')   # the syllabus PDFs are read from the real repo
WS = {'0450': 'work/cie-0450-igcse-2026', '0455': 'work/cie-0455-igcse-2026'}
CS = lambda p: '(?-i:%s)' % p          # a case-sensitive island inside C-11's case-insensitive scan

SCAN = {
 '0450': {
  'Knowledge of the formula and calculations of PED will not be assessed.': (18, 'the PED formula or a PED calculation', '|'.join([
      r'\b(?:PED|price elasticity(?: of demand)?)\s*(?:=|equals\b|is calculated\b|formula\b)',
      r'\bformula (?:for|of) (?:PED|price elasticity)',
      r'(?:percentage|%) change in (?:the )?quantity demanded\s*(?:÷|/|divided by|over)\b',
      r'\bcalculat\w*\s+(?:of\s+)?(?:the |its |a )?(?:PED|price elasticity)'])),
  'Constructing income statements will not be assessed.': (22, 'constructing an income statement', '|'.join([
      r'\b(?:construct\w*|draw(?:s|ing)? up|drew up)\s+(?:an?\s+|the\s+|this\s+|your own\s+|its\s+)?(?:simple\s+)?income statements?\b'])),
  'Constructing statements of financial position will not be assessed.': (22, 'constructing a statement of financial position', '|'.join([
      r'\b(?:construct\w*|draw(?:s|ing)? up|drew up)\s+(?:an?\s+|the\s+|this\s+|your own\s+|its\s+)?(?:simple\s+)?(?:statements? of financial position|balance sheets?)\b'])),
  'Exchange rate calculations will not be assessed.': (24, 'an exchange-rate calculation', '|'.join([
      r'\bexchange[- ]rate calculations?\b',
      r'\bcalculat\w*\b[^.]{0,40}\bexchange rate\b', r'\bexchange rate\b[^.]{0,40}\bcalculat\w*',
      r'\bconvert\w*\b[^.]{0,60}\b(?:at|using)\s+(?:an?\s+|the\s+)?(?:exchange\s+)?rate of\b',
      r'\bat an exchange rate of\b',
      r'(?:N\$|US\$|€|£)\s?\d+(?:\.\d+)?\s*=\s*(?:N\$|US\$|€|£|R)\s?\d'])),
 },
 '0455': {
  'Demand and supply diagrams relating to market failure are not required.': (16, 'a market-failure diagram', '|'.join([
      r'\bmarginal (?:social|private|external) (?:costs?|benefits?)\b', CS(r'\b(?:MSC|MSB|MPC|MPB|MEC|MEB)\b'),
      r'\b(?:welfare|deadweight) loss\b', r'\b(?:market[- ]failure|externality) diagrams?\b'])),
  'Detailed knowledge of different types of structure of a firm is not required.': (18, 'the legal detail of business structures', '|'.join([
      r'\b(?:un)?limited liability\b', r'\bmemorandum of association\b', r'\barticles of association\b',
      r'\bdeed of partnership\b', r'\bpartnership agreement\b', r'\bsleeping partners?\b',
      r'\bcertificate of incorporation\b', r'\bannual general meeting\b'])),
  'Marginal cost is not required.': (18, 'marginal cost', '|'.join([r'\bmarginal costs?\b', CS(r'\bMC\b')])),
  'Marginal revenue is not required.': (18, 'marginal revenue', '|'.join([r'\bmarginal revenues?\b', CS(r'\bMR\b')])),
  'The theory of perfect and imperfect competition and diagrams are not required.': (19, 'the theory of perfect and imperfect competition', '|'.join([
      r'\b(?:perfect|imperfect|monopolistic) competition\b', r'\bperfectly competitive\b', r'\boligopol\w*',
      r'\bprice[- ]takers?\b', r'\b(?:supernormal|abnormal) profits?\b'])),
  'Aggregate demand and aggregate supply are not required.': (20, 'aggregate demand and aggregate supply', '|'.join([
      r'\baggregate (?:demand|supply)\b', CS(r'\bAD\s*(?:/|-|and)\s*AS\b'), CS(r'\b(?:AD|AS|SRAS|LRAS) curves?\b')])),
 },
}


# Controls for every pattern: text it must catch, and in-scope text it must leave alone. Checked here
# and again by verify.py, so a pattern that drifts is caught before an author meets it.
EXAMPLES = {
 'Knowledge of the formula and calculations of PED will not be assessed.': (
  ['PED = % change in quantity demanded \u00f7 % change in price', 'Calculate the PED for the product.',
   'The formula for price elasticity is simple.', 'percentage change in quantity demanded divided by percentage change in price'],
  ['Price elastic demand means customers respond strongly to a price change.',
   'When demand is price inelastic, a price rise increases revenue.']),
 'Constructing income statements will not be assessed.': (
  ['Construct an income statement for Kalahari Crafts.', 'Draw up the income statement for the year.'],
  ['The income statement shows revenue, cost of sales and gross profit.',
   'Accountants prepare the income statement at the end of the year.', 'Calculate the gross profit from the income statement.']),
 'Constructing statements of financial position will not be assessed.': (
  ['Draw up a statement of financial position for the shop.', 'Construct the balance sheet.'],
  ['Use the statement of financial position to decide how the business is financed.']),
 'Exchange rate calculations will not be assessed.': (
  ['At an exchange rate of N$18 = US$1, the price rises.', 'Convert US$200 into Namibian dollars at a rate of 18 to 1.',
   'Calculate the new price after the exchange rate changes.'],
  ['A weaker Namibian dollar makes Namibian exports cheaper abroad.', 'The exchange rate fell, so imported fuel became more expensive.',
   'Mr Nangolo imports car parts.']),
 'Demand and supply diagrams relating to market failure are not required.': (
  ['Draw the marginal social cost curve.', 'The MSC lies above MPC.', 'There is a welfare loss.'],
  ['External costs fall on third parties.', 'Social costs are private costs plus external costs.']),
 'Detailed knowledge of different types of structure of a firm is not required.': (
  ['Owners have limited liability.', 'The memorandum of association sets out the company name.'],
  ['Firms in the private sector aim for profit.', 'Small firms often find it hard to raise finance.']),
 'Marginal cost is not required.': (['Marginal cost rises with output.', 'where MC is lowest'],
                                    ['Total cost is fixed cost plus variable cost.', 'Average cost falls as output rises.']),
 'Marginal revenue is not required.': (['marginal revenue falls', 'where MR equals zero'],
                                       ['Mr Shikongo runs a small firm.', 'Average revenue equals price.']),
 'The theory of perfect and imperfect competition and diagrams are not required.': (
  ['Under perfect competition firms are price takers.', 'An oligopoly has few firms.', 'firms earn supernormal profit'],
  ['Competitive markets have many firms, so prices tend to be lower.', 'A monopoly is the only supplier.']),
 'Aggregate demand and aggregate supply are not required.': (
  ['Fiscal policy shifts aggregate demand.', 'The AD/AS model', 'The AD curve shifts right.'],
  ['Total demand in the economy rises when taxes fall.', 'This is as true as it was.']),
}

# Objectives the plan typed as calculations although the syllabus states the calculation is not
# assessed. Typed business_quantitative_measure, each got a CALC slot instructing with Calculate:
# a work order that told the author to write exactly what the syllabus rules out.
PLAN_CORRECTIONS = {
 '0450': {
  'OBJ-0450-3.3.2-03': ('business_comparison', 'syllabus p18: knowledge of the formula and calculations of PED will not '
                        'be assessed; the objective is the elastic/inelastic distinction and its use in pricing'),
  'OBJ-0450-6.3.3-01': ('business_comparison', 'syllabus p24: exchange rate calculations will not be assessed; the '
                        'objective is the difference between depreciation and appreciation'),
 },
}


def correct_registry(code, ws):
    p = os.path.join(REPO, ws, 'curriculum', 'objective_registry.json')
    reg = json.load(open(p))
    before = json.dumps(reg, sort_keys=True)
    done = []
    notes = [r'\s*\(\s*' + r'\s+'.join(map(re.escape, x.rstrip('.').split())) + r'\s*\)' for x in SCAN[code]]
    for o in reg['objectives']:
        # learner_objective is our restatement and is shown to learners (published objective_titles, a
        # notes heading). The syllabus's own "will not be assessed" aside stays in syllabus_text only.
        lo = o.get('learner_objective') or ''
        for n in notes:
            lo = re.sub(n, '', lo, flags=re.I)
        if lo != o.get('learner_objective'):
            o['learner_objective'] = lo.strip()
        if any(re.search(n, o.get('syllabus_text') or '', re.I) for n in notes):
            done.append({'objective_id': o['objective_id'], 'learner_objective': 'syllabus aside on an excluded construct removed; syllabus_text unchanged'})
        fix = PLAN_CORRECTIONS.get(code, {}).get(o['objective_id'])
        if not fix:
            continue
        typ, why = fix
        if o['objective_type'] != typ or 'Calculate' in o['command_words']:
            o['objective_type'] = typ
            o['command_words'] = [w for w in o['command_words'] if w != 'Calculate']
        done.append({'objective_id': o['objective_id'], 'objective_type': typ, 'removed_command_word': 'Calculate', 'why': why})
    if json.dumps(reg, sort_keys=True) != before:
        json.dump(reg, open(p, 'w'), indent=1, ensure_ascii=False)
    return done

def norm(s):
    return re.sub(r'\s+', ' ', s.replace('’', "'")).strip().lower()


def main():
    bad = []
    for code, ws in WS.items():
        stated = json.load(open(os.path.join(REPO, ws, 'curriculum', 'syllabus-exclusions.json')))
        facts = json.load(open(os.path.join(REPO, ws, 'curriculum', 'syllabus-facts.json')))
        pages = subprocess.run(['pdftotext', '-layout', os.path.join(SYL_REPO, facts['source_document']), '-'],
                               capture_output=True, text=True, check=True).stdout.split('\f')
        sentences = {x: tid for tid, xs in stated.items() for x in xs}
        if set(sentences) != set(SCAN[code]):
            bad.append('%s: scan entries %s do not match the stated limits %s'
                       % (code, sorted(set(SCAN[code]) ^ set(sentences)), ''))
        out = []
        for sent, (page, construct, pattern) in SCAN[code].items():
            if norm(sent).rstrip('.') not in norm(pages[page - 1]):
                bad.append('%s: "%s" is not on page %d' % (code, sent, page))
            rx = re.compile(pattern, re.I)
            catch, allow = EXAMPLES[sent]
            bad += ['%s: pattern for "%s" misses "%s"' % (code, construct, x) for x in catch if not rx.search(x)]
            bad += ['%s: pattern for "%s" wrongly catches "%s"' % (code, construct, x) for x in allow if rx.search(x)]
            out.append({'construct': construct, 'pattern': pattern, 'applies_to': 'subject',
                        'controls': {'must_catch': catch, 'must_allow': allow},
                        'source': 'syllabus, page %d, topic %s' % (page, sentences.get(sent)),
                        'syllabus_sentence': sent, 'provenance': {'sentence': 'syllabus', 'pattern': 'judgement'}})
        doc = {'scope_scan_id': 'SCOPE-SCAN-CIE-%s' % code,
               'rule': ('RS-15. Each entry is one limit the syllabus states, with the pattern C-11 scans learner-facing '
                        'text for. The sentence is the syllabus’s; the pattern is our judgement of what teaching past '
                        'the limit would look like. Every contract in the subject carries every entry.'),
               'entries': out, 'plan_corrections': correct_registry(code, ws)}
        json.dump(doc, open(os.path.join(REPO, ws, 'curriculum', 'scope-scan.json'), 'w'), indent=1, ensure_ascii=False)
        print('%s: %d limits, scan written' % (code, len(out)))
    if bad:
        for b in bad:
            print('  PROBLEM', b)
        sys.exit(1)


if __name__ == '__main__':
    main()
