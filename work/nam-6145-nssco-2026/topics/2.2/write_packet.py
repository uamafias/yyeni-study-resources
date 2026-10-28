"""Rebuild from the final authored packet; never restore an earlier draft."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from author_support import build
build(Path(__file__).resolve().parent.name)
