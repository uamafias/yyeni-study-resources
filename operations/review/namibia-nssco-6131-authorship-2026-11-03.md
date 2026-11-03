# Maths cleanup authorship check — 3 November 2026

Jeremy's instruction: delete only material he authored **or committed**, using Git
records. Preserve other/unknown authorship and all outstanding Claude repair work.

All 10 deleted app files have only Jeremy Tiboth as both author and committer:

| Files | First commit | Later modifying commit |
| --- | --- | --- |
| 3 bank/checksum files; 3 import/build scripts | 31315909 | — |
| 2 obsolete generator modules; 2 importer test files | 31315909 | 1d591356 |

The bank and generator files containing removed examples/branches were introduced
by Jeremy in 1d591356, with no other recorded authors in their file histories.
The JSON companion lists exact paths and full author/committer records.

Eight untracked resource files were restored from the archive to their original
locations because their authorship cannot be verified. Fifteen deleted scratch
links were restored exactly from the initial audit (their targets remain missing).
Archive copies are retained as recovery records; these are not extra active banks.

Six Claude R7 graph recipes / 60 examples, seed plans and frozen generator source
are preserved in workbench/repairs/claude-r7, excluded from assignment until fixed.
The full review and repair register retain all other outstanding review findings.
No new deletion was performed during this authorship check. No commit or push.
