"""Run the canonical R8 author checks from the resource package."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parents[1]/"package/services/api/scripts/check_math_workbench_r8.py"),run_name="__main__")
