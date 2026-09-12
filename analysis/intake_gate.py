"""Compatibility entrypoint; colocation_intake owns all pilot admission rules.

Run from the repository root:
    python -m analysis.intake_gate CSV_PATH --metadata METADATA_JSON
"""

from analysis.colocation_intake import evaluate, main

__all__ = ["evaluate", "main"]


if __name__ == "__main__":
    main()
