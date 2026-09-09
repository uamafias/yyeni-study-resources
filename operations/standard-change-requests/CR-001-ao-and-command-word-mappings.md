# CR-001 — Put the AO and command-word mappings into the profiles, not the workspace

**Raised:** 2026-08-31, during Stage 3 of the 9609 AS build.
**Status:** proposed. Implemented provisionally in `work/cie-9609-as-2026-2028/curriculum/assessment-framework.json` so the pilot can proceed; belongs in the profiles before a second subject starts.

## What is missing

The standard already stores the facts. `cambridge_9609_as_2026_2028.yaml` carries the four assessment objectives with weights and all nine command words with their official Cambridge meanings. `business_subject_profile.yaml` carries the fifteen flashcard subtypes.

What nothing carries is the **mapping between them** — the part that actually drives generation:

| Missing mapping | Belongs in | Why there |
|---|---|---|
| flashcard subtype → assessment objectives (`DEF` → AO1, `APP` → AO2, `CHAIN` → AO3, `EVAL` → AO4, …) | **subject profile** | Subtypes are subject pedagogy; the same map should apply to Business under any board |
| command word → primary AO, typical mark tariff, typical paper location, item types it should drive, what a credit-worthy answer contains | **qualification profile** | Command words and their tariffs are board-specific; Cambridge's "Evaluate" is not AQA's |
| AO mark budget per paper, and the target AO share of a topic's learning-item set | **qualification profile** | Derived from paper marks and AO weights, which are already there |

Without these, an agent can read that AO4 is 20% of the qualification and that `EVAL` is a valid subtype, and still generate a deck of ninety definitions, because nothing connects the two. RS-19 says assessment skills must follow the loaded profiles — but the profiles do not currently say enough for that to bite.

## Proposed additions

### To `business_subject_profile.yaml`, under `learning_item_model`

```yaml
subtype_assessment_objectives:
  DEF:    [AO1]      # note: the default card; a deck that is mostly DEF fails the AO profile
  FEATURE:[AO1]
  DIST:   [AO1, AO2]
  PROC:   [AO1]
  WHY:    [AO1, AO3]
  MECH:   [AO3]
  BEN:    [AO1, AO3]
  LIM:    [AO1, AO3]
  APP:    [AO2]
  CHAIN:  [AO3]
  EVAL:   [AO4]
  CALC:   [AO2, AO1]
  INTERP: [AO2, AO3]
  MISCON: [AO1]
  SYNTH:  [AO3, AO4]

item_mix_rules:
  - Every depth-tier-3 or tier-4 objective carries at least one APP item whose context facts change the reasoning.
  - Every objective whose command words include Analyse carries at least one CHAIN item.
  - Every objective whose command words include Evaluate, Assess, Justify or Advise carries at least one EVAL item.
  - Every quantitative objective carries both a CALC and an INTERP item; a calculation without interpretation is incomplete under RS-22.
  - AO1-only subtypes must not exceed the AO1 target share of a topic's item set.
```

### To `cambridge_9609_as_2026_2028.yaml`, extending each `command_words` entry

```yaml
- word: Analyse
  meaning: Examine in detail to show meaning, identify elements and the relationship between them.
  primary_assessment_objectives: [AO3]
  typical_mark_tariff: "5-8"
  typical_paper_location: ["P1 Section B part a", "P2 parts d-e"]
  drives_item_types: ["flashcard:CHAIN", "short_answer", "data_response"]
  credit_worthy_answer: >
    A chain: decision or condition -> immediate effect -> mechanism -> measurable
    consequence -> effect on an objective or stakeholder. Conditional language, and
    no jump straight to profit.
```

All nine are drafted in `assessment-framework.json` and can be lifted across verbatim.

## Two deterministic checks this makes possible

Neither can be written today, because there is nothing to check against.

- **C6 — AO reach.** Every objective's `assessment_objectives` must be non-empty, and every AO listed on an objective must be exercised by at least one learning item mapped to that objective. Catches the failure where an objective is labelled AO4 and receives only definition cards.
- **C7 — topic AO mix.** A topic's item set must fall within tolerance of the qualification's AO shares. Catches the definition-heavy deck at the topic level rather than at review.

## A rounding discrepancy worth a decision

Applying the paper-level AO weights to paper marks gives **AO1 32, AO2 30, AO3 20, AO4 18** out of 100, against stated qualification weights of **30 / 30 / 20 / 20**. Two marks each on AO1 and AO4. Cambridge publishes both figures and rounding across two papers explains it, but the validator already has a "qualification and paper AO totals" check, so the tolerance should be stated rather than discovered. Recommendation: authoring targets the stated 30/30/20/20, and the check allows ±3 marks.
