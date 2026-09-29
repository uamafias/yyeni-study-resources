# Handover prompt — AS Business 9609, command-word repair

Paste everything below the line into Hermes Agent or OpenCode with this repository open. Run it
only once you have decided to change these published cards.

---

You are repairing **107 published flashcards** in Cambridge International AS Level Business, syllabus
code **9609**. Each instructs with a command word the current AS papers never use. Your job is to
reword each one to a command word the papers do use, at the tariff and answer shape Cambridge's own
mark schemes print for it. Nothing else about the resource changes.

## Why

The syllabus's command-word table (page 39) lists nine words. Since 2023 the AS papers — 1 and 2 —
use six: **Identify, Define, Explain, Calculate, Analyse, Evaluate**. These cards open with
*Distinguish*, *State*, *Recommend*, *Advise*, *Describe* or *Suggest*, so they model questions a
learner will never be set.

## Read first

1. `AGENTS.md` (repo root). You are an AUTHOR.
2. `work/cie-9609-as-2026-2028/curriculum/command-word-repair-work-order.json` — **your brief**: all
   107 cards, each with its target command word, tariff, answer shape and AO split.
3. `work/cie-9609-as-2026-2028/curriculum/answer-shapes.json` — the AO split behind each tariff, read
   off the mark schemes' own AO grids. The splits are unanimous; write to them.
4. `work/cie-9609-as-2026-2028/subject-profile.yaml` — the structure your marking guidance must name
   for each subtype.

## For each card in the work order

The card lives in `work/cie-9609-as-2026-2028/topics/<topic_id>/learning-items/topic_<topic_id>_items.json`,
under its `item_id`.

1. **Rewrite the prompt** to open with `rewrite_with` and to be answerable at `mark_tariff`.
   - *Distinguish between X and Y* becomes an **Explain 3**: *Explain the difference between X and Y*,
     answered as one difference identified (AO1, 1 mark) and then taken into a business context
     (AO2, 2 marks). Not two differences.
   - *State* becomes **Identify 1** (one item), **Define 2** (a meaning), or **Explain 3** (a reason),
     as the work order says. If a *State* card asks for several items, split it into single-item
     Identify cards and record the split.
   - *Recommend* on a case analysis becomes **Evaluate 12**: knowledge 2, application 2, analysis 2,
     and six marks of developed judgement in context.
2. **Rewrite the canonical answer and the marking guidance** to that shape and that AO split. The
   guidance must name every part of the subtype's structure in `subject-profile.yaml`.
3. **Set** `assessment_objectives` to the work order's list, `mark_tariff` to its tariff, and keep
   `blooms_level` unless the new form changes what the learner is asked to do — then change it to
   match the Bloom's table in the framework and say why.
4. **Keep** the objective, the claims the card cites, and the teaching point. This is a rewording,
   not a new card.
5. **Recompute** `authored_hash`:
   ```python
   import sys, hashlib
   sys.path.insert(0, 'standard/v0.2.0-draft/checks')
   from yyeni_checks import _artefact_text
   x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
   ```
6. **Record** the change in `topics/<topic_id>/authoring_notes.json` as `{from, to, why}`.

## Rules

- No unqualified universals; conditions travel with every mechanism that needs them.
- A card's answer may not rest on a fact its prompt does not supply.
- Figures carry units or currency (N$). Namibian and southern African contexts.
- No Cambridge question or mark-scheme wording, anywhere.
- Touch only the 107 cards listed. Do not edit anything under `standard/`.

## Finish

For each of the 18 topics you touched:

```bash
python3 standard/v0.2.0-draft/checks/run_checks.py  work/cie-9609-as-2026-2028 <topic_id>
python3 standard/v0.2.0-draft/checks/what_to_fix.py work/cie-9609-as-2026-2028 <topic_id>
```

Fix every FAIL until each reads `PUBLISH`. Then regenerate the upload folder:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-9609-as-2026-2028
```

It must still publish all 19 topics. If it skips one, stop and report why.

## Report back

Under 200 words: cards rewritten, any split into more than one card, the final check line per
topic touched, and any card where the target form did not fit the teaching point — with what you
did instead.
