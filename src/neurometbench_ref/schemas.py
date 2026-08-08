from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

PATIENT_CORRELATION_COLUMNS = {
    "metric", "patient", "patient_effect"
}
SECTION_CORRELATION_COLUMNS = {
    "metric", "patient", "section", "section_effect"
}


def require_columns(frame: pd.DataFrame, required: Iterable[str]) -> None:
    required_set = set(required)
    missing = sorted(required_set - set(frame.columns))
    if missing:
        raise ValueError(f"missing required columns: {missing}")


def validate_patient_effect_table(frame: pd.DataFrame) -> dict:
    require_columns(frame, PATIENT_CORRELATION_COLUMNS)
    if frame[["metric", "patient"]].duplicated().any():
        duplicates = frame.loc[
            frame[["metric", "patient"]].duplicated(keep=False),
            ["metric", "patient"],
        ].drop_duplicates().to_dict(orient="records")
        raise ValueError(f"duplicate independent patient rows: {duplicates}")
    if frame["patient"].isna().any() or frame["metric"].isna().any():
        raise ValueError("metric and patient identifiers cannot be missing")
    effects = pd.to_numeric(frame["patient_effect"], errors="coerce")
    if effects.isna().any():
        raise ValueError("patient_effect must be numeric and finite")
    return {
        "rows": int(len(frame)),
        "metrics": int(frame["metric"].nunique()),
        "patients": int(frame["patient"].nunique()),
        "patient_level_unit_enforced": True,
    }


def read_and_validate_patient_effect_table(path: str | Path) -> tuple[pd.DataFrame, dict]:
    frame = pd.read_csv(path)
    return frame, validate_patient_effect_table(frame)
