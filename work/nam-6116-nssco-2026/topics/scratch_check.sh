#!/bin/bash
# Isolated build check for one topic. Usage (from the repository root):
#   work/nam-6116-nssco-2026/topics/scratch_check.sh <topic> [author script paths relative to the workspace, e.g. topics/3/author_3A.py ...]
# Copies the workspace to a temp directory, runs the named author scripts there, merges topic 3 groups,
# renders the notes, runs the required checks, the unit-budget check and the hygiene gate, prints only what needs fixing.
# Nothing in the real workspace changes.
# Exit status: 0 only if every step succeeded and what_to_fix, the unit-budget check and the hygiene gate are clean.
# run_checks.py itself is NOT used for the verdict: it exits 1 on a clean PUBLISH (it compares the decision with
# "pass", a framework report; standard/ is not edited here), so its exit code is deliberately ignored and
# what_to_fix.py, which reads the same report and exits 0 only when nothing is left to fix, decides.
set -uo pipefail
T=${1:?topic}; shift
REPO=$(pwd); PY="$REPO/.venv/bin/python"
[ -x "$PY" ] || { echo "missing $PY (system python3 has no PyYAML: the checker would run without the profile)"; exit 2; }
S=$(mktemp -d); trap 'rm -rf "$S"' EXIT
mkdir -p "$S/work"
rsync -a --exclude 'visuals' --exclude '__pycache__' work/nam-6116-nssco-2026 "$S/work/" || { echo "COPY FAILED"; exit 2; }
cp -R standard "$S/standard" || { echo "COPY FAILED"; exit 2; }
cd "$S"
WS=work/nam-6116-nssco-2026
for a in "$@"; do "$PY" "$WS/$a" || { echo "AUTHOR SCRIPT FAILED: $a"; exit 2; }; done
if [ "$T" = "3" ] && [ $# -gt 0 ]; then "$PY" "$WS/topics/3/merge_topic3.py" || { echo "MERGE FAILED"; exit 2; }; fi
"$PY" standard/v0.2.0-draft/build/render_notes.py $WS $T > render.log 2>&1 || { echo "RENDER FAILED"; tail -20 render.log; exit 2; }
"$PY" standard/v0.2.0-draft/checks/run_checks.py $WS $T > run_checks.log 2>&1
[ -s $WS/topics/$T/qa_report.json ] || { echo "RUN_CHECKS WROTE NO REPORT"; tail -20 run_checks.log; exit 2; }
rc=0
"$PY" standard/v0.2.0-draft/checks/what_to_fix.py $WS $T 2>&1 | tail -40; [ "${PIPESTATUS[0]}" -eq 0 ] || rc=1
"$PY" $WS/planning/check_unit_budgets.py $WS $T 2>&1 | tail -12; [ "${PIPESTATUS[0]}" -eq 0 ] || rc=1
"$PY" $WS/topics/check_release_hygiene.py $T 2>&1 | tail -60; [ "${PIPESTATUS[0]}" -eq 0 ] || rc=1
exit $rc
