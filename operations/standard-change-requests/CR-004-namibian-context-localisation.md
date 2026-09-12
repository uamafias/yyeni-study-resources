# CR-004 — Notes and items should be able to draw on Namibian context, not only generic international context

**Raised:** 2026-09-12, during planning for the learning-item generation framework.
**Status:** proposed. No implementation yet.

## The problem

RS-20 requires "genuine context" — worked examples must use contextual facts that
change or sharpen the reasoning, not just name a business. Right now the only
context vocabulary that exists is generic-international (`business_subject_profile.yaml`'s
`sector` / `business_size` / `ownership`, e.g. `"tertiary"`, `"private"`, `"medium or
large"`), aimed at a Cambridge-international learner with no particular home
market in mind.

YYeni serves Namibian learners directly (NIED/DNEA syllabi, NSSCO, NSSCAS are
already in scope per the top-level README). A worked example about "a private
hospital" or "a clothing retailer" is syllabus-valid but does nothing to make the
content *relatable* — a Namibian learner reasons faster and retains more from a
vignette set at a cuca shop, a Windhoek retailer, an NamPower/NamWater-type
utility, a communal-land farming cooperative, or a mining-sector employer than
from an unplaced "medium or large private business." This is a real gap between
what RS-20 asks for and what the profile vocabulary can currently express.

## What's needed

A **locale/context profile** — the same kind of machine-readable, human-maintained
input as `variant_register` (RS-35) — supplying Namibian-relatable context
vocabulary that the authoring step (`author_items.py`, and content-unit authoring
generally) can draw `context.sector` / `context.business_size` /
`context.ownership` / `context.situation` / `context.facts` from, alongside or
instead of the generic set. Likely shape:

- named sectors and business types that are common and recognisable in Namibia
  (informal trade, communal farming, tourism/lodges, mining, fishing, retail
  chains present locally, parastatals);
- Namibian-plausible facts to ground a scenario (currency in N$, typical scale
  language, regional/ownership structures that actually exist there);
- a rule for *when* to use localised vs generic-international context — a
  Cambridge international qualification's mark schemes are written against
  generic scenarios, so this must sharpen relatability without drifting into
  content a mark scheme wouldn't recognise (the same tension RS-23,
  jurisdiction awareness, already names for legal content).

## Why this is a CR and not just an authoring instruction

If this only lives as a prompt-level nudge to the authoring agent, it will be
inconsistent across topics and impossible to check. It needs to be a maintained
input file (like `variant_register`) so:

- coverage of localisation is auditable (which topics/objectives have a
  localised context item vs. only generic);
- it doesn't silently drift into inventing "facts" about Namibia that aren't
  actually representative — this needs the same human-maintained authority as
  the variant register, not model improvisation per item.

## Open questions (for the team, not decided here)

- Does every core item need a localised variant, or only the `case_analysis` /
  `worked_application`-derived items where context actually changes the
  reasoning (RS-20 already limits which items context-sharpening applies to)?
- Who maintains the Namibian context vocabulary, and against what authority
  (is there a Namibian-context equivalent of an "approved business reference"
  the way `variant_register` cites one)?
- Should this be one shared cross-subject locale profile, or per-subject
  (Business's Namibian vocabulary looks nothing like Geography's or English's)?

## Relationship to the item-planning work in progress

`build/plan_items.py` (Step A of the flashcard framework) decides *which claims
and shape* an item needs, not its prose. This CR is a Step-B-and-later concern:
once a locale profile exists, the authoring step should be able to request "a
Namibian-context variant" for context-bearing candidates the same way it already
requests a canonical answer, cross-checked against this profile rather than
invented per call.
