from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class CoverageResult:
    total: int
    present: int
    minimum_required: int
    fraction: float
    passed: bool
    present_items: tuple[str, ...]
    missing_items: tuple[str, ...]


def coverage_gate(
    frozen_items: Sequence[str],
    available_items: Iterable[str],
    minimum_required: int,
) -> CoverageResult:
    frozen = tuple(dict.fromkeys(str(item) for item in frozen_items))
    available = {str(item) for item in available_items}
    if not frozen:
        raise ValueError("frozen_items cannot be empty")
    if minimum_required < 1 or minimum_required > len(frozen):
        raise ValueError("minimum_required must be within the frozen set")
    present = tuple(item for item in frozen if item in available)
    missing = tuple(item for item in frozen if item not in available)
    return CoverageResult(
        total=len(frozen),
        present=len(present),
        minimum_required=minimum_required,
        fraction=len(present) / len(frozen),
        passed=len(present) >= minimum_required,
        present_items=present,
        missing_items=missing,
    )
