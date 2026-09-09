from __future__ import annotations

import json
import shutil
from pathlib import Path

from yyeni_validation import validate_project


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PROJECT = ROOT / "tests" / "fixtures" / "valid_project"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def copy_project(tmp_path: Path) -> Path:
    target = tmp_path / "project"
    shutil.copytree(SOURCE_PROJECT, target)
    # Profiles are referenced three levels above the original fixture. Copy the package
    # profile folder into the relative location expected by the copied manifest.
    expected_root = target.parents[2]
    profile_target = expected_root / "profiles"
    if not profile_target.exists():
        shutil.copytree(ROOT / "profiles", profile_target)
    return target


def codes(project: Path) -> set[str]:
    return {issue.code for issue in validate_project(project / "build_manifest.json").issues}


def test_unsupported_generated_claim_is_blocked(tmp_path: Path) -> None:
    project = copy_project(tmp_path)
    path = project / "canonical_claim_ledger.json"
    ledger = load(path)
    claim = next(item for item in ledger["claims"] if item["claim_id"] == "CLAIM-LOW-LT-BENEFIT")
    claim["evidence"] = []
    claim["derived_from_claim_ids"] = []
    dump(path, ledger)
    assert "UNSUPPORTED_CLAIM" in codes(project)


def test_publishable_unverified_claim_is_blocked(tmp_path: Path) -> None:
    project = copy_project(tmp_path)
    path = project / "canonical_claim_ledger.json"
    ledger = load(path)
    ledger["claims"][0]["verification"]["status"] = "unverified"
    dump(path, ledger)
    assert "UNVERIFIED_PUBLISHABLE_CLAIM" in codes(project)


def test_missing_objective_content_is_detected(tmp_path: Path) -> None:
    project = copy_project(tmp_path)
    manifest_path = project / "build_manifest.json"
    manifest = load(manifest_path)
    manifest["content_units"] = ["content_units/workforce_planning.json"]
    manifest["metrics"]["content_unit_count"] = 1
    manifest["metrics"]["word_count"] = load(project / "content_units" / "workforce_planning.json")["word_count"]
    dump(manifest_path, manifest)
    qa_path = project / "qa_report.json"
    qa = load(qa_path)
    qa["metrics"] = manifest["metrics"]
    dump(qa_path, qa)
    assert "OBJECTIVE_NO_CONTENT" in codes(project)


def test_duplicate_flashcard_prompt_is_detected(tmp_path: Path) -> None:
    project = copy_project(tmp_path)
    item_path = project / "learning_items" / "topic_2.1.2_items.json"
    dataset = load(item_path)
    duplicate = dict(dataset["items"][0])
    duplicate["item_id"] = "FC-WP-DEF-DUP"
    dataset["items"].append(duplicate)
    dump(item_path, dataset)
    manifest_path = project / "build_manifest.json"
    manifest = load(manifest_path)
    manifest["metrics"]["learning_item_count"] += 1
    dump(manifest_path, manifest)
    qa_path = project / "qa_report.json"
    qa = load(qa_path)
    qa["metrics"]["learning_item_count"] += 1
    dump(qa_path, qa)
    assert "DUPLICATE_PROMPT" in codes(project)


def test_core_level_mismatch_is_detected(tmp_path: Path) -> None:
    project = copy_project(tmp_path)
    path = project / "content_units" / "workforce_planning.json"
    unit = load(path)
    unit["level"] = "A Level"
    dump(path, unit)
    assert "CORE_LEVEL_MISMATCH" in codes(project)


def test_enrichment_block_inside_core_unit_is_detected(tmp_path: Path) -> None:
    project = copy_project(tmp_path)
    path = project / "content_units" / "workforce_planning.json"
    unit = load(path)
    unit["blocks"][0]["block_type"] = "enrichment"
    dump(path, unit)
    assert "ENRICHMENT_IN_CORE" in codes(project)


def test_incorrect_manifest_metric_is_detected(tmp_path: Path) -> None:
    project = copy_project(tmp_path)
    path = project / "build_manifest.json"
    manifest = load(path)
    manifest["metrics"]["claim_count"] = 999
    dump(path, manifest)
    assert "MANIFEST_METRIC_MISMATCH" in codes(project)
