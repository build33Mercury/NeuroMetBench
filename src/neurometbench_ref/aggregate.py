from __future__ import annotations

import pandas as pd

from .schemas import validate_patient_effect_table
from .statistics import exact_sign_flip_pvalue, fisher_z_equal_weight


def aggregate_patient_correlations(frame: pd.DataFrame) -> list[dict]:
    validate_patient_effect_table(frame)
    results = []
    for metric, group in frame.groupby("metric", sort=True):
        effects = pd.to_numeric(group["patient_effect"]).to_numpy(dtype=float)
        results.append({
            "metric": str(metric),
            "n_patients": int(len(group)),
            "overall_effect_fisher_z": fisher_z_equal_weight(effects),
            "exact_sign_flip_p": exact_sign_flip_pvalue(effects),
            "direction_consistent": bool((effects > 0).all() or (effects < 0).all()),
        })
    return results
