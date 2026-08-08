from __future__ import annotations

import json
from pathlib import Path

FIXTURE_ROOT = Path(__file__).parent / "fixtures"


def load_json(relative: str) -> dict:
    return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8-sig"))


def fixture_summary() -> dict:
    return {
        "claim_boundaries": load_json("claim_boundaries.json"),
        "quarantine_manifest": load_json("quarantine_manifest.json"),
        "regression_expectations": load_json("regression_expectations.json"),
        "numerical_zero_classification": load_json("numerical_zero_classification.json"),
    }
