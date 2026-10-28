# Subject tracker

Who is doing which subject. Claim a subject **before** you start it (playbook step 0): add or edit its row, then commit and push this file on its own straight away. Two people must never work on the same subject.

Each subject's detailed progress is in `work/<workspace>/STATUS.md`. This file only records who owns what.

- **Status values:** `in progress`, `blocked` (with a note), `complete` (content authored and reviewed; repository release and platform import tracked separately), `published`.
- **Team:** Vitalis, Jeremy, Justus, Lotto.

## Pilots

The first subject of each new kind is run by Vitalis before the team scales that kind (playbook section 6). Mark a kind `piloted` when its pilot publishes.

| Kind | Pilot subject | Status |
|---|---|---|
| Cambridge IGCSE / AS | 9702 AS Physics and others below | piloted |
| Namibia NSSCO | 6144 Business Studies | piloted |
| Namibia NSSCAS | | not yet |
| Junior secondary, grades 8 to 9 | | not yet |
| Upper primary, grades 4 to 7 | | not yet |

## In progress and backlog

| Board and level | Code | Subject | Workspace | Owner | Authoring tool | Status | Notes |
|---|---|---|---|---|---|---|---|
| Cambridge IGCSE | 0500 | First Language English | `cie-0500-igcse-2024-2026` | Vitalis | | in progress | planned; check its STATUS.md or the latest run before claiming |
| Namibia NSSCO | 6138 | History | `nam-6138-nssco-2026` | Jeremy | Codex | in progress | Claimed 26 October 2026; source inventory started. Jeremy explicitly instructed claim/start; NSSCO pilot remains unconfirmed. |
| | | | | | | | |

## Published

| Board and level | Code | Subject | Workspace | Authoring tool | Reviewed by | Items | Notes |
|---|---|---|---|---|---|---:|---|
| Namibia NSSCO | 6144 | Business Studies | `nam-6144-nssco-2026` | Codex | Claude | 562 | Vitalis; 474 flashcards + 88 practice packages. Reviewed resources pushed 28 October 2026 (47403a3). Non-blocking review follow-ups retained; YYeni import pending. |
| Namibia NSSCO | 6145 | Economics | `nam-6145-nssco-2026` | Codex; Claude diagrams | Claude; Codex visual and repair checks | 625 | Vitalis; 513 flashcards + 112 practice packages. Reviewed and published locally; all 28 topics PUBLISH. Final Git checkpoint pending; YYeni image upload/classroom import deferred. |
| Cambridge AS | 9609 | Business | `cie-9609-as-2026-2028` | | Codex | | pilot subject |
| Cambridge AS | 9618 | Computer Science | `cie-9618-as-2026` | Hermes / OpenCode | Claude | 759 | |
| Cambridge AS | 9702 | Physics | `cie-9702-as-2025-2027` | Hermes / OpenCode | Claude | 860 | |
| Cambridge AS | 9093 | English Language | `cie-9093-as-2024-2026` | Hermes / OpenCode | Claude | 417 | |
| Cambridge IGCSE | 0460 | Geography | `cie-0460-igcse-2025-2026` | Hermes / OpenCode | Claude | 629 | |
| Cambridge IGCSE | 0450 | Business Studies | `cie-0450-igcse-2026` | Hermes / OpenCode | Claude | 913 | |
| Cambridge IGCSE | 0455 | Economics | `cie-0455-igcse-2026` | Hermes, then Codex | Claude | 674 | 46 diagrams in `publish/cie-0455-igcse-2026/diagrams/` |
