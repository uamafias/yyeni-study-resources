#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from yyeni_validation import validate_project


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a YYeni study-resource project build.")
    parser.add_argument("manifest", help="Path to build_manifest.json or YAML")
    parser.add_argument("--strict-warnings", action="store_true", help="Return a non-zero status when warnings are present")
    args = parser.parse_args()

    result = validate_project(args.manifest)
    for issue in result.issues:
        suffix = f" [{', '.join(issue.affected_ids)}]" if issue.affected_ids else ""
        print(f"{issue.severity.upper():7} {issue.code}: {issue.message}{suffix}")

    print(f"\nErrors: {len(result.errors)} | Warnings: {len(result.warnings)}")
    if result.errors:
        print("RESULT: FAIL")
        return 1
    if args.strict_warnings and result.warnings:
        print("RESULT: FAIL (strict warnings)")
        return 2
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
