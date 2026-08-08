from __future__ import annotations

from itertools import product
import math
from typing import Iterable, Sequence

import numpy as np
from scipy.stats import rankdata, spearmanr


def benjamini_hochberg(p_values: Sequence[float]) -> np.ndarray:
    """Return BH-FDR q-values in the original order, preserving NaNs."""
    values = np.asarray(p_values, dtype=float)
    output = np.full(values.shape, np.nan, dtype=float)
    finite = np.flatnonzero(np.isfinite(values))
    if finite.size == 0:
        return output
    p = values[finite]
    if np.any((p < 0) | (p > 1)):
        raise ValueError("p-values must be between 0 and 1")
    order = np.argsort(p, kind="mergesort")
    ranked = p[order]
    m = ranked.size
    adjusted = ranked * m / np.arange(1, m + 1)
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    adjusted = np.clip(adjusted, 0.0, 1.0)
    restored = np.empty_like(adjusted)
    restored[order] = adjusted
    output[finite] = restored
    return output


def exact_sign_flip_pvalue(
    effects: Sequence[float],
    *,
    alternative: str = "two-sided",
) -> float:
    """Exact equal-unit sign-flip p-value for the arithmetic mean effect."""
    x = np.asarray(effects, dtype=float)
    if x.ndim != 1 or x.size == 0 or not np.all(np.isfinite(x)):
        raise ValueError("effects must be a non-empty finite vector")
    if x.size > 20:
        raise ValueError("exact enumeration is capped at 20 independent units")
    observed = float(np.mean(x))
    null = np.asarray([
        np.mean(x * np.asarray(signs, dtype=float))
        for signs in product((-1.0, 1.0), repeat=x.size)
    ])
    tolerance = 1e-15
    if alternative == "two-sided":
        extreme = np.abs(null) >= abs(observed) - tolerance
    elif alternative == "greater":
        extreme = null >= observed - tolerance
    elif alternative == "less":
        extreme = null <= observed + tolerance
    else:
        raise ValueError("alternative must be two-sided, greater, or less")
    return float(np.mean(extreme))


def fisher_z_equal_weight(correlations: Sequence[float]) -> float:
    """Equal-weight Fisher-z synthesis for independent-unit correlations."""
    r = np.asarray(correlations, dtype=float)
    if r.ndim != 1 or r.size == 0 or not np.all(np.isfinite(r)):
        raise ValueError("correlations must be a non-empty finite vector")
    clipped = np.clip(r, -1 + 1e-12, 1 - 1e-12)
    return float(np.tanh(np.mean(np.arctanh(clipped))))


def spearman_safe(x: Sequence[float], y: Sequence[float]) -> float:
    a = np.asarray(x, dtype=float)
    b = np.asarray(y, dtype=float)
    if a.shape != b.shape or a.ndim != 1:
        raise ValueError("x and y must be one-dimensional and equally sized")
    keep = np.isfinite(a) & np.isfinite(b)
    if keep.sum() < 2:
        return float("nan")
    if np.unique(a[keep]).size < 2 or np.unique(b[keep]).size < 2:
        return float("nan")
    return float(spearmanr(a[keep], b[keep]).statistic)


def midrank_percentile(values: Sequence[float]) -> np.ndarray:
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or not np.all(np.isfinite(x)):
        raise ValueError("values must be a finite one-dimensional vector")
    if x.size == 1:
        return np.asarray([0.5])
    return (rankdata(x, method="average") - 1.0) / (x.size - 1.0)


def pairwise_order_accuracy(x: Sequence[float], y: Sequence[float]) -> dict:
    a = np.asarray(x, dtype=float)
    b = np.asarray(y, dtype=float)
    if a.shape != b.shape or a.ndim != 1:
        raise ValueError("x and y must be equally sized vectors")
    concordant = discordant = ties = 0
    for i in range(a.size):
        for j in range(i + 1, a.size):
            dx = np.sign(a[i] - a[j])
            dy = np.sign(b[i] - b[j])
            if dx == 0 or dy == 0:
                ties += 1
            elif dx == dy:
                concordant += 1
            else:
                discordant += 1
    informative = concordant + discordant
    return {
        "accuracy": concordant / informative if informative else float("nan"),
        "concordant": concordant,
        "discordant": discordant,
        "ties": ties,
        "informative_pairs": informative,
    }
