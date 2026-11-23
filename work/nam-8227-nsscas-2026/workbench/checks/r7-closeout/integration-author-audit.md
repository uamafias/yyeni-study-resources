# Bounded integration AUTHOR audit

Bounded read-only integration audit of closeout helper, relation/synthesis hooks and final checker; not cross-vendor review.

Current authored selectors checked: 33; complete R7-01 family scans: 6 covering 16 members; normalized native readings: 85.

All current source selectors resolve to their intended family, and reader labels normalize correctly. The actual attach helper preserves a positive narrow exception while removing a superseded named rejection. The three declared native DD exceptions exactly equal the missing family demands on unchanged source items.

| Finding | Severity | Result |
|---|---|---|
| IA-01 | low | Duplicate reading equality is checked before Codex AUTHOR is normalized to Codex author. Two identical raw reading rows with the same ID and uppercase label fail after the first row has been normalized. No current collision: the 27 motion/curve reading IDs are disjoint and normalize correctly. This is a reproduced hardening issue for shared readings across the third input. Fix: Normalize a copied row before comparing it with an existing normalized row. |
| IA-02 | low | The synthesis source_inputs array lists the R6/R7 producers but omits textbook_closeout_r7.py and all present closeout authored input JSONs, even though they now alter the family metadata and examination relations. The snapshot may still freeze them and the fresh rebuild still executes them; this is missing direct synthesis provenance rather than proof of nondeterminism. Fix: Append the closeout helper and each consumed closeout JSON to source_inputs with their hashes, using the same deterministic file order as documents(). |
| IA-03 | medium (in-progress integration) | The newly arrived family-gap input declares family_patches, empty_family_dispositions, native_response_demand_exceptions and relation_removals. The helper version read during this audit consumes only relations/readings/gap_patches and prompt policy; these additional declarations are not applied there. Until the root completes these hooks, the assigned exact-angle/product demands and native evidence are absent, and a retired false-positive relation may survive if no explicit replacement targets the same key. The final closeout checker should fail rather than permit completion. Fix: Apply the authored family metadata and exact native DD exceptions before relation assembly; explicitly remove the declared superseded relation, including any conflicting positive member exceptions. |

Limits:

- The third family-gap input arrived during this audit. Its33total raw selectors across all inputs and85normalized readings were checked after arrival; its family metadata/explicit-removal integration was still being completed by root.
- No files outside these audit outputs were changed. No complete builder or pipeline was executed.
- The positive-exception preservation check used the actual attach function with an in-memory normalizer and fixture rows; it is a structural AUTHOR check, not a native-page relation review.
- Findings describe the integration code read in this audit and may already be superseded by root fixes; no independent or cross-vendor review is claimed.
