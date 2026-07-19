#!/usr/bin/env python3
from pathlib import Path
import shutil

shutil.rmtree("audit-artifacts", ignore_errors=True)

for path in [
    Path("scripts/final_polish.py"),
    Path("scripts/clean_release_tree.py"),
    Path(".github/workflows/release-tree-cleanup.yml"),
    Path("audit-trigger.txt"),
    Path("audit-run.txt"),
]:
    path.unlink(missing_ok=True)
