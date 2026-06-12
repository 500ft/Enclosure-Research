#!/usr/bin/env python3
"""Check that every bibliography entry has a ProConsList analysis file."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIBLIOGRAPHY = ROOT / "paper" / "references.bib"
PRO_CONS_DIRECTORY = ROOT / "ProConsList"


def main() -> None:
    bibliography = BIBLIOGRAPHY.read_text(encoding="utf-8")
    citation_keys = set(re.findall(r"@[A-Za-z]+\{([^,]+),", bibliography))
    analysis_keys = {
        path.stem
        for path in PRO_CONS_DIRECTORY.glob("*.md")
        if path.name not in {"README.md", "TEMPLATE.md", "consolidated_selections.md"}
    }

    missing = sorted(citation_keys - analysis_keys)
    unknown = sorted(analysis_keys - citation_keys)

    print(f"Bibliography entries: {len(citation_keys)}")
    print(f"Per-paper analyses: {len(analysis_keys)}")

    if missing:
        print("Missing ProConsList analyses: " + ", ".join(missing))
    if unknown:
        print("Analyses without bibliography entries: " + ", ".join(unknown))
    if missing or unknown:
        raise SystemExit(1)

    print("Coverage complete.")


if __name__ == "__main__":
    main()

