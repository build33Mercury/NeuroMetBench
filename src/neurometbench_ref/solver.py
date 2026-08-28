from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Sequence

import numpy as np
from scipy import sparse

INVALID_FLUX_SHA256 = "5442b218202717f2127f62922d8abecc825d7e33774535fbbe9470003b0a8249"
MRAS_SHA256 = "82506b7a89f4433c2f7596c9fafc4ac74e0e6d4b1f13ae934eee243705ae3dee"
MODEL_SHA256 = "2efd6650f48ee5b57f3c0b95f405308fa3fc9a6ba8f66f3c8b2ff831ea98dd49"


def sha256_file(path: str | Path, block_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        while True:
            block = handle.read(block_size)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def primal_feasibility(stoichiometry, flux: Sequence[float], lower: Sequence[float], upper: Sequence[float], *, tolerance: float = 1e-8) -> dict:
    matrix = sparse.csr_matrix(stoichiometry)
    vector = np.asarray(flux, dtype=float)
    lb = np.asarray(lower, dtype=float)
    ub = np.asarray(upper, dtype=float)
    if vector.ndim != 1 or lb.shape != vector.shape or ub.shape != vector.shape:
        raise ValueError("flux and bounds must be equal-length vectors")
    if matrix.shape[1] != vector.size:
        raise ValueError("stoichiometric columns must match flux length")
    if tolerance < 0 or not np.isfinite(tolerance):
        raise ValueError("tolerance must be finite and non-negative")
    if not np.all(np.isfinite(vector)) or not np.all(np.isfinite(lb)) or not np.all(np.isfinite(ub)):
        raise ValueError("flux and bounds must contain only finite values")
    if np.any(lb > ub):
        raise ValueError("lower bounds cannot exceed upper bounds")
    residual = np.asarray(matrix @ vector).reshape(-1)
    if not np.all(np.isfinite(residual)):
        raise ValueError("stoichiometric residuals must be finite")
    lower_violation = np.maximum(lb - vector, 0.0)
    upper_violation = np.maximum(vector - ub, 0.0)
    max_mass = float(np.max(np.abs(residual))) if residual.size else 0.0
    max_lower = float(np.max(lower_violation)) if vector.size else 0.0
    max_upper = float(np.max(upper_violation)) if vector.size else 0.0
    return {
        "mass_balance_max_abs": max_mass,
        "lower_bound_max_violation": max_lower,
        "upper_bound_max_violation": max_upper,
        "violated_mass_balance_rows": int(np.sum(np.abs(residual) > tolerance)),
        "violated_bounds": int(np.sum(lower_violation > tolerance) + np.sum(upper_violation > tolerance)),
        "feasible": bool(max_mass <= tolerance and max_lower <= tolerance and max_upper <= tolerance),
        "tolerance": tolerance,
    }


def tolerance_based_zero_qp_classification(*, zero_vector_feasible: bool, maximum_feasible_biomass: float, biomass_tolerance: float = 1e-10, identity_quadratic: bool = True) -> dict:
    """Classify zero under a prespecified numerical biomass tolerance, not as an exact optimum proof."""
    if biomass_tolerance < 0 or not np.isfinite(biomass_tolerance):
        raise ValueError("biomass_tolerance must be finite and non-negative")
    if not np.isfinite(maximum_feasible_biomass):
        raise ValueError("maximum_feasible_biomass must be finite")
    classified = bool(zero_vector_feasible and identity_quadratic and maximum_feasible_biomass <= biomass_tolerance)
    return {
        "tolerance_based_zero_classification": classified,
        "zero_vector_feasible": bool(zero_vector_feasible),
        "maximum_feasible_biomass": float(maximum_feasible_biomass),
        "biomass_tolerance": float(biomass_tolerance),
        "identity_quadratic": bool(identity_quadratic),
        "exact_unique_optimum_proven": False,
        "interpretation": "Thresholded numerical classification only. A maximum-biomass result at or below a positive tolerance does not prove that the true maximum is nonpositive and therefore does not, by itself, prove that zero is the exact unique QP optimum.",
    }
