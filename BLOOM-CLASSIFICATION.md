# Shared Bloom classification rule

Owner decision: Vitalis, 15 November 2026. Applies to all subjects and all card/
problem-set generation workflows, including ordinary flashcards and Workbench
Mathematics, Chemistry and Physics. This is an authoring and review requirement;
existing banks are not automatically reclassified by this document.

## One whole-card level

Assign each assessed part its warranted Bloom level: Remember (1), Understand (2),
Apply (3), Analyse (4), Evaluate (5), Create (6). Assign the whole card the highest
level assessed by any of its parts. A small but genuinely assessed higher-level
component is sufficient; do not average levels or weight the card label by marks.

Example: Apply + Analyse + Evaluate is one Level 5 Evaluate card. Retain all part
labels and show the lower-level mix in its preview. The summary label identifies
its highest assessed thinking; it does not say every part or mark is at that level.
Teacher filters, topic counts and deck composition count the card once under its
whole-card level. Detailed part/mark analyses use the individual part labels.

Classify the learner's assessed work, not the sophistication of the model solution,
a prerequisite, a topic title, an incidental command word or numerical difficulty.
A hint mentioning evaluation does not make a calculation question Evaluate.
The marking scheme must require the evidence used to justify the classification.

## Recipe inheritance

Classify the reviewed recipe version, structural branch and its assessed parts.
Generated instances inherit the approved part labels and highest whole-card level
when permitted changes preserve the assessed demands. If branches differ in their
assessed levels, resolve the selected branch before assigning the generated card's
level. Do not give every branch the maximum level of another branch it never asks.

Changes to reasoning, scaffolding, response requirements or assessed parts require
classification review. Normal/boundary examples must verify demand preservation.
Store the approved labels, rationale and classification version with generated
content. Preserve historical question/marking/classification snapshots; a later
review must not silently relabel a learner's past work.

If an assessed part has not been classified, the whole-card maximum is not yet
established. Keep the item explicitly unclassified pending review rather than
silently deriving a maximum from only the known parts.

## Authoring and review evidence

For each part record its level, the required learner action/decision, the relevant
marking criterion and a short rationale. Record the derived whole-card maximum,
recipe/branch/version where applicable, representative and boundary instances,
review provenance and unresolved classification questions.

Reviewers verify that every assessed part is covered, the summary is the maximum,
and generated variations preserve the approved demands. Classifications may be
proposed by AI but require the existing independent review process. The examples
and domains must justify a label; no subject needs an artificial equal quota of
all six levels.

Bloom labels do not alter exam mark tariffs, assessment objectives, difficulty,
memory boxes or assignment completion rules. Ordinary Studio marking rules and
subject-specific Workbench marking schemes retain their existing authority.

## Implementation status

Policy approved; automated schema/checker changes, bank classification and UI/API
propagation remain separately tracked implementation work. No claim is made that
existing validators enforce this new rule yet.
