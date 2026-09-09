#!/bin/sh
set -eu
python3 validate_project.py tests/fixtures/valid_project/build_manifest.json
pytest -q
