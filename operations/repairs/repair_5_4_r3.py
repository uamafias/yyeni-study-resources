#!/usr/bin/env python3
"""Repair topic 5.4 against review SR-9609-5.4-CODEX-R3.

Run from the repository root:  python3 repair_5_4_r3.py

Every edit below answers a numbered finding in
operations/review/cie-9609-as-2026-2028-5.4-review-r3.yaml.
RS-41 propagation is handled at the end: claim revisions are bumped, and every
artefact that cites a revised claim is re-authored (new authored_hash, prior_hash
recording what it looked like before) or honestly stamped reviewed_unchanged.
"""
import glob
import hashlib
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
STD = os.path.join(ROOT, 'standard', 'v0.2.0-draft', 'checks')
sys.path.insert(0, STD)
import yyeni_checks as Y  # noqa: E402

WS = os.path.join(ROOT, 'work', 'cie-9609-as-2026-2028')
TOPIC = os.path.join(WS, 'topics', '5.4')
TODAY = '2026-09-12'


def H(obj):
    return hashlib.sha256(Y._artefact_text(obj).encode('utf-8')).hexdigest()


# --------------------------------------------------------------------------- load
ledger = json.load(open(os.path.join(TOPIC, 'claims', 'canonical_claim_ledger.json')))
claims = {c['claim_id']: c for c in ledger['claims']}
units = {}
for p in sorted(glob.glob(os.path.join(TOPIC, 'content-units', '*.json'))):
    units[p] = json.load(open(p))
items_path = os.path.join(TOPIC, 'learning-items', 'topic_5.4_items.json')
items_doc = json.load(open(items_path))
items = {i['item_id']: i for i in items_doc['items']}

blocks = {}
for p, u in units.items():
    for b in u['blocks']:
        blocks[b['block_id']] = b

# --------------------------------------------------------------------------- self-test
# Before writing anything, confirm H() reproduces the hash formula already on disk.
probe = [x for x in list(items.values()) + list(blocks.values()) if x.get('authored_hash')]
matched = sum(1 for x in probe if H(x) == x['authored_hash'])
if matched < len(probe) * 0.8:
    sys.exit('ABORT: H() reproduces only %d of %d stored authored_hash values - the hash '
             'formula is not sha256(_artefact_text). Fix H() before running.' % (matched, len(probe)))
print('hash self-test: %d/%d stored hashes reproduce' % (matched, len(probe)))

touched = []           # artefacts whose text this repair changed
PRIOR = {}             # id -> authored_hash as it stood before this repair
for d in list(items.values()) + list(blocks.values()):
    key = d.get('item_id') or d.get('block_id')
    PRIOR[key] = d.get('authored_hash')


def set_text(block_id, text, heading=None):
    b = blocks[block_id]
    if heading:
        b['heading'] = heading
    b['text'] = text
    touched.append(block_id)


def set_item(item_id, **kw):
    it = items[item_id]
    it.update(kw)
    touched.append(item_id)


# ============================================================ R3-001 (high, analysis)
# "every decision resting on it is wrong in the same direction" is an invalid universal.
# Under-allocating a shared total to one product over-allocates it to another, so two
# products are distorted in OPPOSITE directions at the same time.

claims['CLM-9609-5.4-003']['text'] = (
    "Inaccurate cost information can mislead any decision that materially depends on the figure, and the "
    "direction of the error follows the direction of the distortion. A product charged with too little cost "
    "looks more profitable than it is, so it may be priced too low or pushed too hard; a product charged with "
    "too much looks like a failure, so it may be dropped although it was helping to cover costs that would be "
    "incurred anyway. Because a shared total divided between products is a fixed sum, understating one "
    "product's share normally overstates another's, so two products can be distorted in opposite directions at "
    "the same time. Whether a particular decision goes wrong depends on whether the error is large enough to "
    "change it."
)
claims['CLM-9609-5.4-003']['revision'] = 2
claims['CLM-9609-5.4-003']['revised_at'] = TODAY
claims['CLM-9609-5.4-003'].setdefault('notes', []).append(
    "Repaired 2026-09-12 after review SR-9609-5.4-CODEX-R3 (R3-001). The original said every decision resting "
    "on an inaccurate figure is wrong in the same direction. Neither half holds: an error need not be material "
    "to every dependent decision, and allocating a fixed shared total is zero-sum, so understating one "
    "product's share overstates another's - opposite directions, not a common one."
)

set_text(
    '5.4.1-b3',
    "Four decisions run on cost figures. What to charge, so the price covers what the product costs. What to "
    "keep making, and what to stop. Where spending is drifting away from plan. And whether the business is "
    "doing better or worse than it was.\n\n"
    "If a figure is wrong, each of those decisions can be misled. Not all of them automatically: a costing "
    "error only changes a decision if it is large enough to matter to that decision. And not all in the same "
    "direction either, because the direction follows the distortion.\n\n"
    "Under-costing. A product carrying too little cost looks more profitable than it is. The business prices it "
    "low, pushes it hard, and loses money faster the more it sells.\n\n"
    "Over-costing. A product carrying too much looks like a failure, so the business drops it - and then finds "
    "the overheads it was helping to cover have not gone anywhere, and now sit on the products that remain. "
    "Whether dropping it was a mistake turns on how much of that cost would genuinely have disappeared with "
    "it: an overhead that is unavoidable over the period in question stays behind, while a lease that could "
    "be given up or a supervisor employed only on that product goes with it.\n\n"
    "The two pathways are connected, and that is the part worth remembering. A shared total divided between "
    "products is a fixed sum. A basis that charges one product too little charges another too much, so the "
    "same allocation can make one product look better than it is and another look worse, at the same time. The "
    "error is not in the arithmetic. It is in how the shared costs were divided up in the first place."
)

set_item(
    'ITEM-9609-5.4-002-WHY',
    canonical_answer=(
        "Because four decisions run on it: what to charge, what to keep making, where spending is drifting from "
        "plan, and whether performance is improving. A wrong figure can mislead any of those decisions that "
        "depends on it materially, and the direction depends on which way the figure is out. Understated, a "
        "product looks profitable, so it is priced low and pushed, and the business loses money faster. "
        "Overstated, it looks like a failure and may be dropped, while any cost it was helping to cover that "
        "would be incurred anyway stays behind. Because a shared total is divided between products, the same "
        "allocation usually does both at once - too little on one product means too much on another."
    ),
    marking_guidance=[
        "Reason: a wrong cost figure can mislead any decision that materially depends on it.",
        "Direction: must condition the error on whether the cost is understated or overstated, not assert a "
        "single common direction.",
        "Purpose: the answer must say why, not only what.",
        "Reward at least one named decision that depends on the figure, developed through one correct pathway.",
    ],
)

# ============================================================ R3-002 (high, analysis)
# Keep-or-drop reasoning needs BOTH conditions: which costs actually disappear, and
# whether the freed capacity could earn more elsewhere.

claims['CLM-9609-5.4-040']['text'] = (
    "A product whose selling price is above its variable cost makes a positive contribution. Dropping it "
    "without putting anything in its place loses that contribution while any fixed cost that would have been "
    "incurred anyway remains, so the business ends up worse off by the contribution lost less whatever cost "
    "genuinely disappears with the product. That is what positive contribution proves. It does not prove that "
    "keeping the product is the best available decision: that also depends on whether the capacity it uses "
    "could earn a larger contribution doing something else."
)
claims['CLM-9609-5.4-040']['revision'] = 2
claims['CLM-9609-5.4-040']['revised_at'] = TODAY
claims['CLM-9609-5.4-040'].setdefault('notes', []).append(
    "Repaired 2026-09-12 after review SR-9609-5.4-CODEX-R3 (R3-002). The original concluded that a "
    "positive-contribution product is worth continuing where the fixed costs would be incurred anyway. "
    "Positive contribution establishes the loss from dropping WITHOUT replacement; it says nothing about "
    "whether the capacity could earn more in another use, which is the second condition of the keep decision."
)

set_text(
    '5.4.1-b6',
    "A factory makes two products and pays N$120 000 a year in rent under a lease with six years still to run. "
    "How much of that rent belongs to each product?\n\n"
    "There is no measurement that answers this. The business has to choose a basis: floor space used, machine "
    "hours, labour hours, or simply units produced. Suppose product A occupies 70% of the floor but takes only "
    "30% of the machine hours. On a floor-space basis it carries N$84 000 of rent; on a machine-hours basis it "
    "carries N$36 000. Nothing about the factory has changed. The same real spending has produced two "
    "different costs for the same product.\n\n"
    "That is why the resulting figure is a judgement rather than a measurement, and it matters because of what "
    "happens next. If product A is judged on the floor-space figure it may look unprofitable and be dropped. "
    "The rent does not fall when it goes - the lease is unavoidable for six years and no part of it can be "
    "given up by making less - so it simply lands on product B, which may now look unprofitable in its turn.\n\n"
    "The chain is worth being able to write out: a basis is chosen, the basis sets the overhead each product "
    "carries, that figure drives a decision about the product, and the decision does not change the overhead. "
    "Two things decide whether the chain actually ends in a worse business. First, how much of the cost really "
    "is unavoidable: if dropping A released floor space the business could sublet, part of the rent does "
    "disappear with it. Second, what the freed capacity would earn: if the space and machine time A used could "
    "be turned over to a product earning more than A contributed, dropping A is the right decision even though "
    "the rent stays. And the whole chain matters less the smaller the shared costs are relative to the direct "
    "ones - in a business where overheads are small, the choice of basis barely moves the answer."
)

set_text(
    '5.4.2-b7',
    "A business makes three products. Under full costing, product C shows a loss of N$20 000 after taking its "
    "share of overheads. The obvious move is to stop making it.\n\n"
    "Work through what actually happens. Product C sells for more than its variable cost, so it earns a "
    "positive contribution - say N$60 000 a year. Its share of the overheads was N$80 000, which is where the "
    "reported loss comes from. Stop making it, and the N$60 000 of contribution disappears. The N$80 000 of "
    "overheads does not: the rent and the salaries are unchanged, and are now carried by A and B alone. The "
    "business is N$60 000 worse off than before, and A and B each look less profitable than they did.\n\n"
    "Two conditions are what make this an argument rather than a rule, and an answer that leaves either out is "
    "incomplete.\n\n"
    "The first is avoidability. The reasoning holds while the fixed costs really would be incurred anyway. If "
    "dropping C would let the business give up a warehouse, or lay off a supervisor who works only on C, then "
    "part of that N$80 000 does go, and the calculation has to be done again with only the costs that would "
    "genuinely disappear. If N$50 000 of it is avoidable, the business loses N$60 000 of contribution and saves "
    "N$50 000 of cost, so it is only N$10 000 worse off - and if more than N$60 000 is avoidable, dropping C "
    "improves profit.\n\n"
    "The second is what the capacity would otherwise do. Positive contribution shows what is lost by dropping C "
    "and putting nothing in its place. It does not show that keeping C is the best use of the factory. If the "
    "line, the floor space and the labour C occupies could make a product contributing N$90 000, the "
    "comparison is not N$60 000 against nothing but N$60 000 against N$90 000, and C should go. Keeping a "
    "product because it contributes something is only right when there is nothing better to do with what it "
    "uses."
)

set_item(
    'ITEM-9609-5.4-003-CHAIN',
    canonical_answer=(
        "A product is charged with more of the shared costs than it would carry under a different basis, so its "
        "recorded cost per unit is overstated and it shows a loss. On that figure the business stops making it. "
        "The sales and the contribution from that product go. The shared costs do not, so far as they are "
        "unavoidable - a rent fixed by a lease, or salaries that do not fall with output, are unchanged and now "
        "fall on the products that remain. Those products' costs rise in turn, so the business ends with less "
        "contribution, the same unavoidable overheads, and a second product that now looks unprofitable. The "
        "chain only reaches that ending for the part of the cost that would have been incurred anyway: "
        "whatever would genuinely have disappeared with the product is saved and has to be set against the "
        "contribution lost."
    ),
    marking_guidance=[
        "Condition: the shared costs are divided using a chosen basis, and the part that stays behind is the "
        "part that is unavoidable.",
        "Mechanism: an overstated share makes a viable product show a loss.",
        "Consequence: the contribution is lost while the unavoidable overhead stays and is redistributed.",
        "Objective or stakeholder: the chain must reach the profit of the business and the apparent cost of the "
        "remaining products.",
    ],
)

set_item(
    'ITEM-9609-5.4-017-CHAIN',
    canonical_answer=(
        "The business picks a basis for dividing the overheads - say floor space. A product that takes a lot of "
        "space but little machine time is charged with a large share. Added to its direct costs, that share "
        "pushes its recorded cost above its selling price, so it shows a loss. That recorded loss is an "
        "accounting result, not the effect of stopping: the product still sells for more than the cost of "
        "making it, so it is still contributing towards overheads the business would pay anyway. If the "
        "business acts on the recorded figure and drops it, the contribution goes while the unavoidable part of "
        "the overhead stays, so the business is worse off by the difference - unless enough of the overhead "
        "would disappear with the product, or the capacity it used could earn more on something else."
    ),
    marking_guidance=[
        "Condition: overheads are divided on a chosen basis, and the overhead that stays behind is the part "
        "that would be incurred anyway.",
        "Mechanism: a large share pushes recorded cost above selling price.",
        "Consequence: the product shows an accounting loss that is not the incremental effect of stopping.",
        "Objective or stakeholder: the chain must reach the profit of the business if the product is dropped, "
        "and must not treat the allocated loss as the cash effect.",
    ],
)

set_item(
    'ITEM-9609-5.4-025-EVAL',
    canonical_answer=(
        "It should not decide on that figure alone. Two questions decide it, and the full-costing loss answers "
        "neither. The first is how much of the cost in that loss would actually disappear if the line stopped. "
        "The recorded loss includes a share of overheads divided on a chosen basis; where those overheads "
        "continue regardless, stopping the line removes its contribution and leaves the costs behind, so the "
        "business ends up worse off and the remaining lines look less profitable in turn. The second is what "
        "the freed capacity would earn. Positive contribution shows what is lost by stopping and replacing the "
        "line with nothing; if the plant, space and labour it uses could carry a product contributing more, "
        "stopping is right even though the overhead stays. The strongest argument for acting on the figure is "
        "that a line failing to cover its full share indefinitely is being carried by the others, and a "
        "business cannot carry it forever. On balance the decision should rest on avoidable cost measured "
        "against the best alternative use of the capacity, not on the allocated figure. The judgement changes "
        "if a real cost would go with the line - a warehouse that could be given up, a supervisor employed only "
        "on it - or if a better use of the capacity appears."
    ),
    marking_guidance=[
        "Judgement: a plain recommendation is required, not a balanced list.",
        "Context: the answer must be argued for a business whose overheads are shared across three lines.",
        "Criterion: the decisive test is the contribution lost against the cost avoided AND the best "
        "alternative use of the capacity freed.",
        "Counterargument: must acknowledge that a line permanently carried by the others is a real problem.",
        "Condition: must name what would change the judgement - avoidable fixed costs, or a better use of the "
        "capacity.",
    ],
)

# ============================================================ R3-003 (high, evaluation)
# ITEM-055 asserted N$5 was the complete incremental cost; the stem never said so.

set_item(
    'ITEM-9609-5.4-055-EVAL',
    prompt=(
        "A bakery sells bread rolls to cafes at N$14 a roll. Its total variable cost is N$5 a roll, including "
        "oven energy and every other input that rises with output. The baker is on a fixed monthly salary that "
        "does not change with output. The oven stands idle three mornings a week, with capacity for 1 200 rolls "
        "a morning and no other work waiting, and filling an idle morning creates no setup, overtime or other "
        "extra fixed cost. A hotel offers a standing weekly order of 900 rolls at N$9.80 a roll, collected from "
        "the bakery. Evaluate whether the bakery should accept."
    ),
    canonical_answer=(
        "It should accept, as a fixed-term arrangement rather than an open one. The decisive criterion is the "
        "incremental comparison: the total cost these rolls cause is the N$5 a roll of variable cost, because "
        "that figure already includes oven energy and every other input that rises with output, the baker's "
        "salary does not change, the hotel collects so there is no delivery cost, the order creates no setup or "
        "overtime, and 900 rolls fit inside a single idle morning's 1 200 with no full-price work displaced. At "
        "N$9.80 each roll leaves N$4.80, so 900 rolls add N$4 320 a week that the bakery would not otherwise "
        "have. The strongest argument against is that this is a standing order rather than a one-off - the "
        "arrangement most likely to become known to the cafes paying N$14, and hardest to withdraw once the "
        "hotel has built it into its plans. That is why the term matters. The judgement changes if full-price "
        "demand grows into those mornings, because the capacity would then be earning N$9 a roll rather than "
        "N$4.80, or if the order grew beyond what the idle capacity holds and overtime had to be paid."
    ),
    marking_guidance=[
        "Judgement: a plain recommendation is required, not a balanced list.",
        "Context: must use the N$14, N$5 and N$9.80 figures, the fixed salary, the collection, and the 1 200-roll "
        "capacity.",
        "Criterion: the comparison must be against the total cost the order causes, which the stem gives as the "
        "N$5 total variable cost with no extra fixed cost, and must confirm that no full-price work is "
        "displaced.",
        "Counterargument: must address the standing nature of the order and the cafes paying full price.",
        "Condition: must state what would change the judgement.",
    ],
)
items['ITEM-9609-5.4-055-EVAL']['context']['facts'] = [
    "normal price N$14",
    "total variable cost N$5 a roll, including oven energy",
    "no setup, overtime or other extra fixed cost",
    "offer N$9.80",
    "900 rolls a week",
    "three idle mornings",
    "capacity 1 200 rolls a morning",
    "baker on fixed salary",
    "hotel collects, no delivery cost",
]

# ============================================================ R3-005 (medium, quantitative)
# 60 haircuts is a margin of safety, not profit; and break-even is about the business,
# not about what the owner personally receives.

set_item(
    'ITEM-9609-5.4-064-APP',
    canonical_answer=(
        "It tells her that at 240 haircuts a month the salon's revenue exactly covers its total cost - the "
        "rent, the electricity and the chair rental are paid and the business makes neither a profit nor a "
        "loss. Every haircut after the 240th adds its contribution to profit. Against an expectation of 300, "
        "that is a margin of safety of 60 haircuts: sales can fall by 60 before the salon is back at "
        "break-even, and a quiet month of 230 puts it into a loss. How much profit those 60 haircuts represent "
        "cannot be worked out from these two figures - that needs the contribution per haircut, which the "
        "break-even output does not give her. What the figure does tell her is that the margin is thin, so she "
        "needs to know early in the month whether she is on pace."
    ),
    marking_guidance=[
        "Context: must use the 240 and 300 figures.",
        "Reasoning: the mechanism is that fixed costs are covered before profit begins.",
        "Quantity: 60 is a margin of safety in haircuts, not an amount of profit; profit is a currency amount "
        "and cannot be calculated without contribution per haircut.",
        "Conclusion: must reach what the owner should watch or do.",
    ],
)

# ============================================================ R3-006 (medium, quantitative)
# "The lowest price that still adds to profit" has no determinate answer, and N$360 was
# invented in the answer. The offer now sits in the stem and every question asked has one
# derivable answer.

set_item(
    'ITEM-9609-5.4-046-CALC',
    prompt=(
        "A furniture maker's variable cost is N$310 a chair and its fixed costs work out at N$140 a chair at "
        "current output. A customer offers N$360 a chair for a one-off order at a time when the workshop has "
        "idle time and the order causes no other cost. Calculate the price that covers all costs, the price at "
        "which the order would neither add to profit nor reduce it, and what the offer adds per chair."
    ),
    canonical_answer=(
        "Full cost per chair = N$310 + N$140 = N$450, so N$450 is the price that covers all costs at the output "
        "the N$140 was calculated at. The price at which the order neither adds to profit nor reduces it is the "
        "cost the order itself causes, which here is the variable cost of N$310: at exactly N$310 the "
        "contribution is N$310 - N$310 = nil, so the order changes nothing. The offer is N$360, so contribution "
        "per chair = N$360 - N$310 = N$50, and the order improves profit by N$50 a chair if the workshop is "
        "profitable or reduces the loss by N$50 a chair if it is not. Note what each figure is for: N$450 is a "
        "long-run price and only holds at the assumed volume, while N$310 is a floor and not a price to charge, "
        "because at the floor itself the order is not worth taking."
    ),
    marking_guidance=[
        "Formula: full cost = variable cost per unit + fixed cost per unit; the no-gain price is the cost the "
        "order itself causes.",
        "Substitution must be shown, not only the answer.",
        "Units: the currency must appear on every figure.",
        "Interpretation: must state that the full-cost figure depends on the assumed output, that N$310 leaves "
        "nil contribution, and that a positive margin above it improves profit or reduces a loss either way.",
    ],
)
items['ITEM-9609-5.4-046-CALC'].setdefault('context', {})
items['ITEM-9609-5.4-046-CALC']['context']['facts'] = [
    "variable cost N$310 a chair",
    "fixed costs N$140 a chair at current output",
    "one-off offer N$360 a chair",
    "idle time, order causes no other cost",
]

# ============================================================ R3-007 (medium, accuracy)
# Bank charges and accountancy fees were classified as fixed by their label, against the
# topic's own behaviour-based rule.

set_item(
    'ITEM-9609-5.4-087-SHOR',
    canonical_answer=(
        "Where did the price come from? A price taken from a competitor or a wish is weaker than one already "
        "being achieved. Where did the variable cost come from? Quoted, or estimated - and does it hold at the "
        "volume planned, or does it assume a bulk discount not yet agreed? Are all the fixed costs of the "
        "business in there, and is each one actually fixed? The test is how the amount behaves as output "
        "changes, not what the expense is called. An insurance premium and an annual accountancy retainer do "
        "not change with output, so they belong in the fixed total. Bank charges are usually a mixture: a "
        "monthly account fee is fixed, while charges levied per transaction rise with activity and belong with "
        "variable costs, so only the fixed part goes in the numerator. Anything genuinely fixed that is left "
        "out understates fixed costs and so understates the break-even output. Note that the owner's own "
        "drawings are not a business cost and do not belong in this calculation - they are a withdrawal of "
        "profit, and they belong in the cash-flow forecast, which answers a different question. Is everything "
        "produced assumed to be sold? If stock builds, the real figure is higher. Is this one product or "
        "several? A single chart across several products assumes a sales mix that will move. And how far above "
        "break-even is the plan? A margin of safety of a few per cent means the whole plan rests on estimates "
        "being right."
    ),
    marking_guidance=[
        "State each question plainly before explaining it.",
        "Give the reason each question matters - what a bad answer would mean for the figure.",
        "Use the context: these are questions a lender asks about a plan, not about a trading business.",
        "Classification must turn on how a cost behaves as output changes, not on the name of the expense; "
        "only the fixed part of a mixed charge belongs in the fixed-cost total.",
        "Owner's drawings must be excluded from fixed costs and placed in the cash-flow forecast.",
    ],
)

# ============================================================ RS-41 propagation
REVISED = {'CLM-9609-5.4-003': 2, 'CLM-9609-5.4-040': 2}
rev = {cid: (c.get('revision') or 1) for cid, c in claims.items()}

stale = []
for d in list(items.values()) + list(blocks.values()):
    key = d.get('item_id') or d.get('block_id')
    seen = d.get('claims_seen') or {}
    if any(seen.get(cid, 0) != rev.get(cid, 1) for cid in d.get('claim_ids', [])):
        stale.append(key)

REVIEWED_UNCHANGED = {
    # Artefacts a revised claim makes stale that this repair genuinely re-read and left as they
    # were, with the reason. Anything not listed here and not in `touched` will abort the run.
    'ITEM-9609-5.4-026-CHAIN':
        "Re-read 2026-09-12 against the revised CLM-040. This card already fixes the six-year lease and the "
        "absence of dedicated staff or equipment, and asks only how dropping changes the recorded cost of the "
        "products that remain. It reaches no keep-or-drop verdict, so the opportunity-cost condition the claim "
        "now adds does not apply to it and nothing needed changing.",
    'ITEM-9609-5.4-040-EVAL':
        "Re-read 2026-09-12 against the revised CLM-040. Its criterion is already the contribution lost "
        "against the cost avoided, and it names the alternative use of the capacity as the condition that "
        "reverses the judgement, so the revised claim states what this answer already required.",
    'ITEM-9609-5.4-085-ESSA':
        "Re-read 2026-09-12 against the revised CLM-040. The task already ends on both conditions - which "
        "costs are avoidable, and whether the freed capacity has a better use - which is why review R3 cited "
        "it as the model the other chains should follow.",
}

for key in stale:
    if key not in touched and key not in REVIEWED_UNCHANGED:
        sys.exit('ABORT: %s is stale under RS-41 but this repair neither re-authored it nor recorded an '
                 'honest reviewed_unchanged reason. Read it and decide before rerunning.' % key)

for d in list(items.values()) + list(blocks.values()):
    key = d.get('item_id') or d.get('block_id')
    if key not in stale and key not in touched:
        continue
    d['claims_seen'] = {cid: rev.get(cid, 1) for cid in d.get('claim_ids', [])}
    prior = PRIOR.get(key)
    new = H(d)
    if prior and prior != new:
        d['prior_hash'] = prior
        d.pop('reviewed_unchanged', None)
    elif key in REVIEWED_UNCHANGED:
        d['prior_hash'] = prior
        d['reviewed_unchanged'] = REVIEWED_UNCHANGED[key]
    d['authored_hash'] = new

# --------------------------------------------------------------------------- write
json.dump(ledger, open(os.path.join(TOPIC, 'claims', 'canonical_claim_ledger.json'), 'w'),
          indent=2, ensure_ascii=False)
for p, u in units.items():
    json.dump(u, open(p, 'w'), indent=2, ensure_ascii=False)
json.dump(items_doc, open(items_path, 'w'), indent=2, ensure_ascii=False)

print('claims revised : CLM-9609-5.4-003, CLM-9609-5.4-040')
print('re-authored    : %d artefacts' % len(set(touched)))
print('               : %s' % ', '.join(sorted(set(touched))))
print('reviewed unchanged: %s' % ', '.join(sorted(k for k in REVIEWED_UNCHANGED if k in stale)))
print('done. next: rebuild the exposure map, re-render the notes, run the checks.')
