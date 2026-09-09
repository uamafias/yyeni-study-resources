# CR-003 — Turn the topic 5.2 review defects into runtime rules and deterministic checks

**Raised:** 2026-09-08 · **Against:** standard v0.1.0-draft · **Delivers:** standard **v0.2.0-draft**
**Trigger:** the RS-28 independent review of the pilot topic (`operations/review/codex-review-9609-5.2.yaml`) returned **reject** with 15 open issues — 3 critical, 10 high, 2 medium — on a build whose deterministic pass had reported 22 of 25 checks passing.

## 1. The problem this change request exists to fix

The v0.1.0 deterministic suite checked that the build was **well-formed**. The review found that it was **wrong**. Nothing in the suite could see the difference, and in one case the suite actively said the opposite: coverage passed because three shared items each cited fifteen objectives while practising three to five, so "all 24 objectives covered" was manufactured by breadth of mapping.

At one topic that is an embarrassment. At the scale this pipeline is being built for — 160-plus subjects, authored by teams who will not each rediscover these lessons — it is a defect factory. Every one of the fifteen issues is a *habit*, not a fact about sources of finance, so every one of them would have been reproduced across every remaining topic in every remaining subject.

This CR converts the review's findings into machinery: eight new runtime rules, two rule amendments, and a rebuilt check suite that catches thirteen of the fifteen before a reviewer is ever asked.

## 2. New runtime rules

| Rule | Requirement | Born from |
|---|---|---|
| **RS-33 Bounded generality** | No claim of exclusivity or universality unless definitional, legal or arithmetic — and where genuine, the claim records which. | 002 (sole trader "only"; plc "more than any other form"; grants "closed to an ordinary business") |
| **RS-34 Generalisations survive their members** | Any summary, family, taxonomy or mnemonic must hold for every member it covers and must declare `generalisation_scope`. The exception must not simply be taught later in the same material. | 003, 004 (internal sources "cost nothing" beside sale-and-leaseback's lease payments; factoring filed under borrow-and-repay-with-interest then said to borrow nothing) |
| **RS-35 Variant completeness** | Where a term names forms that change a learner-relevant consequence, name the forms and condition every benefit and limitation on the form. Consequential variants live in the subject profile's human-maintained `variant_register`. | 005 (recourse vs non-recourse factoring), 006 (four crowd-funding models) |
| **RS-36 Assessment claims need assessment evidence** | No claim about what examiners reward, what carries most marks or what a paper contains without a mapped evidence record; where evidence status is `partial`, no such claim at all. | 014, 015 ("the factor examiners reward most consistently", "more marks than any other single idea", "reach every command word" followed by four of six) |
| **RS-37 Command-word-shaped practice** | Every objective carries an item whose prompt instructs with one of that objective's own command words, at that tariff and answer shape. | 010 (an Explain objective practised only by a context-free Distinguish card) |
| **RS-38 Declared answer structures** | Where a profile declares an answer's required parts for a subtype, every item models all parts and names each in marking guidance, or is reclassified. | 011 (three EVAL cards missing parts; one is a WHY card wearing an EVAL label) |
| **RS-39 Offline reconstructibility** | Every canonical answer must be derivable from the topic's own content units; an item must not be the sole place a learner meets an idea. | 012 (cards leaning on lessor margins, group guarantees, debenture tradability — none taught in the notes) |
| **RS-40 Meaningful traceability** | `objective_ids` limited to what is actually taught or practised; coverage credit only where a cited claim also serves that objective. | 013 (three items citing 15 objectives each) |

**Amendments.** RS-07 now says a mapping counts only where the content or item actually teaches the objective. RS-21 now says statements about what an independent third party will do — lender, investor, buyer, supplier, employer, regulator, customer — must be likelihood with a reason, never certainty, and must not prescribe a provider's internal method unless it is evidenced for the named context (issues 007, 008).

Six new hard release blockers follow from these and are listed in §5 of the runtime standard.

## 3. New check suite

`standard/v0.2.0-draft/checks/` — 28 checks, subject-agnostic, driven entirely by workspace artifacts, the subject profile and one shared language register. No board, subject or topic is named in the code.

Run it with:

```bash
python3 standard/v0.2.0-draft/checks/run_checks.py work/<workspace> <topic-id>
```

It writes a schema-valid `qa_report.json` and exits non-zero unless every check passes.

Three design decisions worth recording:

- **`not_run` is never a pass.** A check whose input is missing says so, names the missing input, and holds the release. The old suite's silence about things it could not see is what let the build look healthy.
- **A check that raises is a failed check**, not a skipped one.
- **The suite writes the critic-packet hash manifest itself**, so the reviewer verifies the same bytes the checks ran on.

Two new human-maintained inputs make the language rules checkable, and both are deliberately per-subject rather than global:

- `subject-profile.yaml → variant_register` — the terms in this subject whose forms change a consequence (RS-35).
- `subject-profile.yaml → answer_structures` — the required parts of each item subtype, each part carrying alternative keywords (RS-38).

And one per-topic input: `contract.json → depth_constraints.excluded_constructs`. On 5.2 the exclusions existed only as prose inside each content unit, where nothing could enforce them.

## 4. Proof — the suite fired at the unrepaired pilot

The suite was run against topic 5.2 **before any repair**, with the review's findings withheld from the code. Result: 28 checks, **16 pass, 11 fail, 1 warn**, decision **reject**.

| Review issue | Caught by | Notes |
|---|---|---|
| 001 inverted lender-risk mechanism | — | **Not mechanisable.** Reviewer-only. |
| 002 categorical availability | C-08 | Named CLM-003, CLM-006 directly |
| 003 internal-source contradiction | C-13 | Flags the undeclared generalisation; does not itself prove the contradiction |
| 004 three-family taxonomy | C-13 | Flagged block `5.2.2e-b3` |
| 005 recourse factoring | C-12 | "names 0 of 2 forms: missing recourse, non-recourse" |
| 006 crowd-funding models | C-12, C-11 | "missing loan"; and `cost of capital` as an excluded construct |
| 007 provider certainty | C-09 | Found "No lender will touch it" |
| 008 unconditional chains | C-08, C-09 | Caught ITEM-015-CHAIN among others |
| 009 retired command word | C-14, C-20 | Both prompts, plus the compound card |
| 010 no command-word practice | C-15 | Found the 2 Codex named **plus 6 more** |
| 011 EVAL parts missing | C-16 | Found 9 EVAL items including the mislabelled -068 |
| 012 cards not reconstructible | — | **Not mechanisable.** See below. |
| 013 inflated mappings | C-04 | Named -059, -058, -057 as worst offenders; 41 bad mappings |
| 014 assessment-priority claims | C-10 | 20 hits, blocked because evidence status is `partial` |
| 015 incomplete tariff map | C-10 | "reach every command word" |

**Thirteen of fifteen.** On issue 010 the suite is stronger than the reviewer.

### The two that stayed human, and why that is the finding

**001** is an inverted causal mechanism stated in fluent, well-formed prose. No pattern separates a true mechanism from its exact inverse.

**012** was attempted. A check flagging canonical answers that use vocabulary the notes never use fired on **47 of 68 items**, because ordinary English variation swamps genuinely untaught mechanisms. It was withdrawn rather than shipped as noise, and the reason is written into the source at the point where it would otherwise be rewritten. C-07 (every claim an item cites must also be taught in a block) is the mechanical floor; the real question stays a named reviewer task.

The honest reading: **code can enforce shape, discipline and traceability; it cannot tell truth from its inverse, and it cannot tell whether a learner could actually build an answer.** That is a stable boundary, and the pipeline should be designed around it rather than repeatedly attempting to cross it.

## 5. What this changes about the pipeline at scale

The review-and-repair loop is no longer "author, then hope a reviewer catches it". It is:

1. Author against the contract.
2. Run the suite. It fails loudly on eleven classes of defect and holds on anything it cannot see.
3. Fix what the suite names — cheaply, because it names IDs.
4. Send the reviewer a packet that has already had those eleven classes removed, so the review spends its attention on truth, teaching quality and reconstructibility.
5. Repair against the review. Re-run the suite. Re-review only what changed.

Step 4 is the point. A reviewer given a build full of mechanical defects spends its budget on them and finds fewer of the defects only it can find.

## 6. Status

- Runtime standard: **v0.2.0-draft**, 40 rules, validates against `runtime_standard.schema.json`.
- Check suite: 28 checks, proven against the unrepaired pilot.
- Topic 5.2: still `reject`, now on 11 mechanical grounds and 15 semantic ones. Repair is the next step and happens under these rules.
- **Not yet done:** the v0.1.0 pytest suite has not been extended to cover the new checks, and no second topic has been authored under v0.2.0, so the rules are proven against defects that already existed and not yet against defects they were meant to prevent.
