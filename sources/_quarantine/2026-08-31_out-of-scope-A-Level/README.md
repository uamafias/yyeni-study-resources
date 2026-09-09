# Out of scope — moved 2026-08-31

A Level papers (paper 3 and 4), inserts, examiner report and grade thresholds,
acquired before the scope was narrowed to **question papers and mark schemes for
Papers 1 and 2 only**.

Moved rather than deleted. Every file is in `_harvest/logs/harvest_log.csv` with
its source URL, so any of them can be restored or re-acquired.

Scope is now enforced by `_harvest/rules/cambridge-question-bank.toml`:

    [filter]
    include = { kind = "qp|ms", paper = "[12]" }
