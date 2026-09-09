from __future__ import annotations

import difflib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml
from jsonschema import Draft202012Validator, FormatChecker


@dataclass
class ValidationIssue:
    severity: str
    code: str
    message: str
    affected_ids: list[str] = field(default_factory=list)


@dataclass
class ValidationResult:
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def errors(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "error"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "warning"]

    @property
    def passed(self) -> bool:
        return not self.errors

    def add(self, severity: str, code: str, message: str, affected_ids: Iterable[str] = ()) -> None:
        self.issues.append(ValidationIssue(severity, code, message, list(affected_ids)))


def load_document(path: Path) -> Any:
    suffix = path.suffix.lower()
    text = path.read_text(encoding="utf-8")
    if suffix == ".json":
        return json.loads(text)
    if suffix in {".yaml", ".yml"}:
        return yaml.safe_load(text)
    raise ValueError(f"Unsupported structured file type: {path}")


def normalise_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9%]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE))


def _validate_schema(instance: Any, schema_path: Path, result: ValidationResult, label: str) -> None:
    schema = load_document(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        result.add("error", "SCHEMA", f"{label} failed schema validation at {location}: {error.message}")


def _ids(records: Iterable[dict[str, Any]], key: str) -> list[str]:
    return [record[key] for record in records]


def _check_unique(values: list[str], code: str, label: str, result: ValidationResult) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    if duplicates:
        result.add("error", code, f"Duplicate {label}: {sorted(duplicates)}", sorted(duplicates))


def _check_reference_set(
    refs: Iterable[str],
    valid: set[str],
    code: str,
    label: str,
    owner_id: str,
    result: ValidationResult,
) -> None:
    missing = sorted(set(refs) - valid)
    if missing:
        result.add("error", code, f"{owner_id} contains unknown {label}: {missing}", [owner_id, *missing])


def validate_project(manifest_path: str | Path) -> ValidationResult:
    manifest_path = Path(manifest_path).resolve()
    project_dir = manifest_path.parent
    package_root = Path(__file__).resolve().parent
    schema_dir = package_root / "schemas"
    result = ValidationResult()

    if not manifest_path.exists():
        result.add("error", "FILE_MISSING", f"Manifest not found: {manifest_path}")
        return result

    manifest = load_document(manifest_path)
    _validate_schema(manifest, schema_dir / "build_manifest.schema.json", result, "build manifest")
    if result.errors:
        return result

    def resolve(relative_path: str) -> Path:
        return (project_dir / relative_path).resolve()

    artifacts = {
        "qualification_profile": (resolve(manifest["qualification_profile"]), "qualification_profile.schema.json"),
        "subject_profile": (resolve(manifest["subject_profile"]), "subject_profile.schema.json"),
        "source_inventory": (resolve(manifest["source_inventory"]), "source_inventory.schema.json"),
        "objective_registry": (resolve(manifest["objective_registry"]), "objective_registry.schema.json"),
        "assessment_evidence": (resolve(manifest["assessment_evidence"]), "assessment_evidence.schema.json"),
        "claim_ledger": (resolve(manifest["claim_ledger"]), "canonical_claim_ledger.schema.json"),
        "qa_report": (resolve(manifest["qa_report"]), "qa_report.schema.json"),
    }

    loaded: dict[str, Any] = {}
    for label, (path, schema_name) in artifacts.items():
        if not path.exists():
            result.add("error", "FILE_MISSING", f"Required artifact missing: {path}")
            continue
        try:
            loaded[label] = load_document(path)
        except Exception as exc:  # pragma: no cover - defensive path
            result.add("error", "FILE_READ", f"Could not read {path}: {exc}")
            continue
        _validate_schema(loaded[label], schema_dir / schema_name, result, label)

    content_units: list[dict[str, Any]] = []
    for relative_path in manifest["content_units"]:
        path = resolve(relative_path)
        if not path.exists():
            result.add("error", "FILE_MISSING", f"Content unit missing: {path}")
            continue
        unit = load_document(path)
        _validate_schema(unit, schema_dir / "content_unit.schema.json", result, str(path.name))
        content_units.append(unit)

    learning_datasets: list[dict[str, Any]] = []
    for relative_path in manifest["learning_items"]:
        path = resolve(relative_path)
        if not path.exists():
            result.add("error", "FILE_MISSING", f"Learning-item dataset missing: {path}")
            continue
        dataset = load_document(path)
        _validate_schema(dataset, schema_dir / "learning_items.schema.json", result, str(path.name))
        learning_datasets.append(dataset)

    if result.errors:
        return result

    qualification = loaded["qualification_profile"]
    subject = loaded["subject_profile"]
    source_inventory = loaded["source_inventory"]
    registry = loaded["objective_registry"]
    assessment = loaded["assessment_evidence"]
    ledger = loaded["claim_ledger"]
    qa_report = loaded["qa_report"]

    # Qualification-level arithmetic.
    ao_total = sum(item["qualification_weight_percent"] for item in qualification["assessment_objectives"])
    if abs(ao_total - 100) > 1e-9:
        result.add("error", "AO_TOTAL", f"Qualification AO weights sum to {ao_total}, not 100.")
    for paper in qualification["papers"]:
        total = sum(paper["assessment_objective_weights"].values())
        if abs(total - 100) > 1e-9:
            result.add("error", "PAPER_AO_TOTAL", f"{paper['paper_id']} AO weights sum to {total}, not 100.", [paper["paper_id"]])

    # Sources.
    sources = source_inventory["sources"]
    source_ids = _ids(sources, "source_id")
    _check_unique(source_ids, "DUP_SOURCE_ID", "source IDs", result)
    source_id_set = set(source_ids)
    hashes: dict[str, list[dict[str, Any]]] = {}
    for source in sources:
        hashes.setdefault(source["content_hash"]["value"], []).append(source)
    for digest, group in hashes.items():
        if len(group) > 1 and not any(item["status"] == "duplicate" for item in group):
            ids = [item["source_id"] for item in group]
            result.add("error", "UNMARKED_DUPLICATE_SOURCE", f"Sources share SHA-256 {digest} but none is marked duplicate.", ids)

    # Objectives and graph references.
    objectives = registry["objectives"]
    objective_ids = _ids(objectives, "objective_id")
    _check_unique(objective_ids, "DUP_OBJECTIVE_ID", "objective IDs", result)
    objective_id_set = set(objective_ids)
    for objective in objectives:
        owner = objective["objective_id"]
        if objective["parent_id"] is not None and objective["parent_id"] not in objective_id_set:
            result.add("warning", "UNKNOWN_PARENT", f"{owner} has a parent not present in this registry subset: {objective['parent_id']}", [owner])
        _check_reference_set(objective["prerequisite_ids"], objective_id_set, "BAD_PREREQ", "prerequisite IDs", owner, result)
        _check_reference_set(objective["related_ids"], objective_id_set, "BAD_RELATED", "related IDs", owner, result)

    included_ids = set(manifest["scope"]["included_objective_ids"])
    excluded_ids = set(manifest["scope"]["excluded_objective_ids"])
    _check_reference_set(included_ids, objective_id_set, "BAD_SCOPE_INCLUDED", "included objective IDs", manifest["build_id"], result)
    _check_reference_set(excluded_ids, objective_id_set, "BAD_SCOPE_EXCLUDED", "excluded objective IDs", manifest["build_id"], result)
    overlap = included_ids & excluded_ids
    if overlap:
        result.add("error", "SCOPE_OVERLAP", f"Objectives are both included and excluded: {sorted(overlap)}", sorted(overlap))

    # Claims and evidence.
    claims = ledger["claims"]
    claim_ids = _ids(claims, "claim_id")
    _check_unique(claim_ids, "DUP_CLAIM_ID", "claim IDs", result)
    claim_id_set = set(claim_ids)
    evidence_required = {
        "syllabus_direct",
        "source_derived",
        "source_synthesised",
        "source_corrected",
        "generated_gap",
        "generated_quality",
        "verified_external",
    }
    for claim in claims:
        owner = claim["claim_id"]
        _check_reference_set(claim["objective_ids"], objective_id_set, "BAD_CLAIM_OBJECTIVE", "objective IDs", owner, result)
        _check_reference_set(claim["derived_from_claim_ids"], claim_id_set, "BAD_CLAIM_DERIVATION", "claim IDs", owner, result)
        for evidence in claim["evidence"]:
            if evidence["source_id"] not in source_id_set:
                result.add("error", "BAD_CLAIM_SOURCE", f"{owner} cites unknown source {evidence['source_id']}", [owner, evidence["source_id"]])
        if claim["provenance"] in evidence_required and not claim["evidence"] and not claim["derived_from_claim_ids"]:
            result.add("error", "UNSUPPORTED_CLAIM", f"{owner} has provenance {claim['provenance']} but no evidence or derivation.", [owner])
        if claim["provenance"] == "reasoned_extension" and not claim["evidence"] and not claim["derived_from_claim_ids"]:
            result.add("error", "UNSUPPORTED_EXTENSION", f"{owner} is a reasoned extension without evidence or verified premises.", [owner])
        if claim["publishable"] and claim["verification"]["status"] not in {"verified", "human_approved"}:
            result.add("error", "UNVERIFIED_PUBLISHABLE_CLAIM", f"{owner} is publishable but verification status is {claim['verification']['status']}.", [owner])
        if claim["verification"]["status"] == "rejected" and claim["publishable"]:
            result.add("error", "REJECTED_PUBLISHABLE_CLAIM", f"{owner} is rejected but marked publishable.", [owner])

    # Assessment evidence.
    for record in assessment["records"]:
        owner = record["evidence_id"]
        if record["source_id"] not in source_id_set:
            result.add("error", "BAD_ASSESSMENT_SOURCE", f"{owner} cites unknown source {record['source_id']}", [owner, record["source_id"]])
        _check_reference_set(record["objective_ids"], objective_id_set, "BAD_ASSESSMENT_OBJECTIVE", "objective IDs", owner, result)

    # Content units.
    unit_ids = _ids(content_units, "unit_id")
    _check_unique(unit_ids, "DUP_UNIT_ID", "content-unit IDs", result)
    unit_id_set = set(unit_ids)
    covered_by_content: set[str] = set()
    context_min = subject["application_model"]["worked_application_policy"]["minimum_per_major_objective"]
    for unit in content_units:
        owner = unit["unit_id"]
        _check_reference_set(unit["objective_ids"], objective_id_set, "BAD_UNIT_OBJECTIVE", "objective IDs", owner, result)
        covered_by_content.update(unit["objective_ids"])
        if unit["core_status"] == "core" and unit["level"] != manifest["scope"]["selected_level"]:
            result.add("error", "CORE_LEVEL_MISMATCH", f"{owner} is core but level is {unit['level']}, expected {manifest['scope']['selected_level']}.", [owner])
        if unit["word_budget"]["min"] > unit["word_budget"]["target"] or unit["word_budget"]["target"] > unit["word_budget"]["max"]:
            result.add("error", "BAD_WORD_BUDGET", f"{owner} has an invalid min/target/max word budget.", [owner])
        actual_unit_words = sum(count_words(block["text"]) for block in unit["blocks"])
        if unit["word_count"] != actual_unit_words:
            result.add("error", "UNIT_WORD_COUNT_MISMATCH", f"{owner} records word_count {unit['word_count']}, calculated value is {actual_unit_words}.", [owner])
        if unit["qa_status"] == "approved" and not (unit["word_budget"]["min"] <= actual_unit_words <= unit["word_budget"]["max"]):
            result.add("error", "WORD_BUDGET_BREACH", f"Approved unit {owner} has calculated word count {actual_unit_words} outside its budget.", [owner])
        block_ids = _ids(unit["blocks"], "block_id")
        _check_unique(block_ids, "DUP_BLOCK_ID", f"block IDs in {owner}", result)
        for block in unit["blocks"]:
            _check_reference_set(block["claim_ids"], claim_id_set, "BAD_BLOCK_CLAIM", "claim IDs", block["block_id"], result)
            if unit["core_status"] == "core" and block["block_type"] == "enrichment":
                result.add("error", "ENRICHMENT_IN_CORE", f"Core unit {owner} contains an enrichment block {block['block_id']}.", [owner, block["block_id"]])
        major_objectives = [obj for obj in objectives if obj["objective_id"] in unit["objective_ids"] and obj["depth_tier"] >= 3 and obj["mandatory"]]
        if major_objectives:
            application_count = sum(1 for block in unit["blocks"] if block["block_type"] == "worked_application")
            if application_count < context_min:
                ids = [obj["objective_id"] for obj in major_objectives]
                result.add("error", "INSUFFICIENT_WORKED_APPLICATION", f"{owner} covers major objectives but has {application_count} worked applications; minimum is {context_min}.", [owner, *ids])

    # Learning items.
    all_items: list[dict[str, Any]] = []
    for dataset in learning_datasets:
        all_items.extend(dataset["items"])
    item_ids = _ids(all_items, "item_id")
    _check_unique(item_ids, "DUP_ITEM_ID", "learning-item IDs", result)
    item_id_set = set(item_ids)
    covered_by_items: set[str] = set()
    normalised_prompts: dict[str, list[dict[str, Any]]] = {}
    for item in all_items:
        owner = item["item_id"]
        _check_reference_set(item["objective_ids"], objective_id_set, "BAD_ITEM_OBJECTIVE", "objective IDs", owner, result)
        _check_reference_set(item["claim_ids"], claim_id_set, "BAD_ITEM_CLAIM", "claim IDs", owner, result)
        _check_reference_set(item["prerequisite_item_ids"], item_id_set, "BAD_ITEM_PREREQ", "learning-item IDs", owner, result)
        covered_by_items.update(item["objective_ids"])
        normalised_prompts.setdefault(normalise_text(item["prompt"]), []).append(item)
        if item["core_status"] == "core":
            for objective_id in item["objective_ids"]:
                if objective_id in excluded_ids:
                    result.add("error", "CORE_ITEM_EXCLUDED_OBJECTIVE", f"Core item {owner} maps to excluded objective {objective_id}.", [owner, objective_id])
        vague_patterns = [r"^what is its\b", r"^what are its\b", r"^state them\b", r"^explain this\b"]
        if any(re.search(pattern, normalise_text(item["prompt"])) for pattern in vague_patterns):
            result.add("warning", "VAGUE_PROMPT", f"{owner} may not be self-contained: {item['prompt']}", [owner])

    for prompt, group in normalised_prompts.items():
        if len(group) > 1:
            duplicate_groups = {item["intentional_duplicate_group"] for item in group}
            if None in duplicate_groups or len(duplicate_groups) != 1:
                ids = [item["item_id"] for item in group]
                result.add("error", "DUPLICATE_PROMPT", f"Duplicate normalised prompt: '{prompt}'", ids)

    # Near-duplicate prompts are warnings, not automatic blockers.
    unique_prompts = [(key, values[0]) for key, values in normalised_prompts.items()]
    for index, (prompt_a, item_a) in enumerate(unique_prompts):
        for prompt_b, item_b in unique_prompts[index + 1:]:
            if len(prompt_a) < 25 or len(prompt_b) < 25:
                continue
            ratio = difflib.SequenceMatcher(None, prompt_a, prompt_b).ratio()
            if ratio >= 0.94 and item_a["intentional_duplicate_group"] != item_b["intentional_duplicate_group"]:
                result.add("warning", "NEAR_DUPLICATE_PROMPT", f"Possible near-duplicate prompts ({ratio:.2f}).", [item_a["item_id"], item_b["item_id"]])

    # Mandatory objective coverage.
    for objective in objectives:
        oid = objective["objective_id"]
        if not objective["mandatory"] or oid not in included_ids:
            continue
        if oid not in covered_by_content:
            result.add("error", "OBJECTIVE_NO_CONTENT", f"Mandatory objective {oid} has no content unit.", [oid])
        if oid not in covered_by_items:
            result.add("error", "OBJECTIVE_NO_ITEM", f"Mandatory objective {oid} has no learning item.", [oid])

    # Metrics must be calculated from structured artifacts.
    calculated_metrics = {
        "objective_count": len(included_ids),
        "claim_count": len(claims),
        "content_unit_count": len(content_units),
        "learning_item_count": len(all_items),
        "word_count": sum(sum(count_words(block["text"]) for block in unit["blocks"]) for unit in content_units),
    }
    for key, calculated in calculated_metrics.items():
        if manifest["metrics"][key] != calculated:
            result.add("error", "MANIFEST_METRIC_MISMATCH", f"Manifest {key} is {manifest['metrics'][key]}, calculated value is {calculated}.")
        if qa_report["metrics"][key] != calculated:
            result.add("error", "QA_METRIC_MISMATCH", f"QA report {key} is {qa_report['metrics'][key]}, calculated value is {calculated}.")

    # Release-state consistency.
    if manifest["status"] in {"approved", "published"}:
        if assessment["status"] != "complete":
            result.add("error", "ASSESSMENT_MINING_INCOMPLETE", "Approved or published builds require a complete assessment-evidence map.")
        if qa_report["release_decision"] != "pass":
            result.add("error", "QA_NOT_PASS", "Approved or published build has not received a pass release decision.")
        if qa_report["blockers"]:
            result.add("error", "OPEN_BLOCKERS", "Approved or published build contains QA blockers.")
        for review in qa_report["semantic_reviews"]:
            if review["status"] != "pass":
                result.add("error", "SEMANTIC_REVIEW_NOT_PASS", f"Reviewer {review['review_id']} status is {review['status']}.", [review["review_id"]])
        for output in manifest["outputs"]:
            if output["status"] in {"verified", "published"} and output["sha256"] is None:
                result.add("error", "OUTPUT_HASH_MISSING", f"Verified output {output['path']} has no SHA-256.")
    if manifest["status"] == "published":
        for output in manifest["outputs"]:
            if output["status"] != "published":
                result.add("error", "OUTPUT_NOT_PUBLISHED", f"Build is published but output {output['path']} status is {output['status']}.")

    # Registry/profile consistency.
    if registry["qualification_profile_id"] != qualification["profile_id"]:
        result.add("error", "QUALIFICATION_PROFILE_MISMATCH", "Objective registry qualification_profile_id does not match the loaded profile.")
    if registry["subject_profile_id"] != subject["profile_id"]:
        result.add("error", "SUBJECT_PROFILE_MISMATCH", "Objective registry subject_profile_id does not match the loaded profile.")

    return result
