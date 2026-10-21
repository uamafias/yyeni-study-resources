# 6136 Development Studies planning reproducibility

Step 2 and Step 3 are approved. Step 4 is drafted for approval; STATUS.md is the
current workflow record. Older corpus prose describes its own stage at creation.

The Step 3 source-bullet evidence/exposure/misconceptions are preserved unchanged
as source-bullet-*.json here. The rejected submitted plan is frozen under reviewed-plan-v1/ and the original Claude report remains unchanged. The canonical curriculum and assessment evidence now
use the Step 4 registry. verify_corpus.py checks the original snapshots, while
finalise_plan.py independently checks the canonical registry map, every slot,
performance subparts, exact AO arithmetic and all scope/coverage invariants.

Human semantic inputs: registry_decisions.json, member_evidence_decisions.json
and glossary_decisions.json. Current member-level evidence is conservative and
incomplete; zero direct assignments never implies absence from the papers.

Rebuild from repository root, in order:

```bash
python3 work/nam-6136-nssco-2026/planning/build_plan.py
python3 work/nam-6136-nssco-2026/planning/build_exemplar.py
python3 work/nam-6136-nssco-2026/planning/finalise_plan.py
python3 work/nam-6136-nssco-2026/planning/verify_corpus.py
python3 work/nam-6136-nssco-2026/planning/verify_syllabus_facts.py
```

build_plan invokes the unchanged conform_registry, make_contract and
make_work_order tools. Do not run old Step 3 miners alone over the canonical
Step 4 outputs: they produce bridge IDs. Preserve the Step 3 snapshots when
rebuilding. Final teaching prose is designated for Codex; Claude Code reviews the authored resources.

Read plan-validation.json and standard-compatibility.json together. Profile
schema incompatibility is recorded as an error, not filtered into a pass.
Exemplar no-opinion checks and the wrapper exit discrepancy are explicit.
No full-topic or publication gate has been claimed. No source or standard file
was edited, and no commit, push, publishing or platform import was performed.
