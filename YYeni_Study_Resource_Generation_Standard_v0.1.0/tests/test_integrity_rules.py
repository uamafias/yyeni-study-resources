from pathlib import Path

from yyeni_validation import validate_project


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tests" / "fixtures" / "valid_project" / "build_manifest.json"


def test_valid_draft_project_passes_deterministic_validation() -> None:
    result = validate_project(MANIFEST)
    assert result.passed, [f"{issue.code}: {issue.message}" for issue in result.errors]


def test_valid_draft_project_has_no_warnings() -> None:
    result = validate_project(MANIFEST)
    assert not result.warnings, [f"{issue.code}: {issue.message}" for issue in result.warnings]
