from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from yyeni_validation import load_document


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
PROFILE_DIR = ROOT / "profiles"


def test_all_schemas_are_valid_json_schemas() -> None:
    for path in SCHEMA_DIR.glob("*.schema.json"):
        Draft202012Validator.check_schema(load_document(path))


def test_business_subject_profile_validates() -> None:
    schema = load_document(SCHEMA_DIR / "subject_profile.schema.json")
    profile = yaml.safe_load((PROFILE_DIR / "business_subject_profile.yaml").read_text(encoding="utf-8"))
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(profile)


def test_cambridge_qualification_profile_validates() -> None:
    schema = load_document(SCHEMA_DIR / "qualification_profile.schema.json")
    profile = yaml.safe_load((PROFILE_DIR / "cambridge_9609_as_2026_2028.yaml").read_text(encoding="utf-8"))
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(profile)


def test_machine_readable_runtime_standard_validates() -> None:
    schema = load_document(SCHEMA_DIR / "runtime_standard.schema.json")
    standard = yaml.safe_load((ROOT / "RUNTIME_STANDARD.yaml").read_text(encoding="utf-8"))
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(standard)
