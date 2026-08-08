from __future__ import annotations

import json
from pathlib import Path

from .solver import INVALID_FLUX_SHA256, MODEL_SHA256, MRAS_SHA256, sha256_file

ALLOWED_PURPOSES = {
    MODEL_SHA256: {"numerical_model", "audit_fixture", "structural_reproduction"},
    MRAS_SHA256: {"bound_input", "audit_fixture", "transcript_activity_input"},
    INVALID_FLUX_SHA256: {"numerical_failure_fixture", "audit_fixture"},
}


def artifact_disposition(sha256: str) -> str:
    if sha256 == INVALID_FLUX_SHA256:
        return "QUARANTINED_INVALID_NONZERO_FLUX_MATRIX"
    if sha256 == MRAS_SHA256:
        return "PRESERVED_TRANSCRIPT_DERIVED_BOUND_INPUT_NOT_FLUX"
    if sha256 == MODEL_SHA256:
        return "PRESERVED_STRUCTURALLY_VALID_NUMERICAL_MODEL"
    return "UNCLASSIFIED"


def assert_artifact_use_allowed(sha256: str, purpose: str) -> dict:
    purpose = str(purpose)
    allowed = ALLOWED_PURPOSES.get(sha256)
    if allowed is None:
        raise ValueError("artifact hash is not present in the frozen disposition ledger")
    if purpose not in allowed:
        raise PermissionError(
            f"artifact {sha256} is not allowed for purpose {purpose}; "
            f"allowed purposes: {sorted(allowed)}"
        )
    return {
        "sha256": sha256,
        "purpose": purpose,
        "disposition": artifact_disposition(sha256),
        "allowed": True,
    }


def verify_file_use(path: str | Path, purpose: str) -> dict:
    observed = sha256_file(path)
    receipt = assert_artifact_use_allowed(observed, purpose)
    receipt["path"] = str(Path(path).resolve())
    return receipt


def load_claim_boundaries() -> dict:
    path = Path(__file__).parent / "fixtures" / "claim_boundaries.json"
    return json.loads(path.read_text(encoding="utf-8-sig"))


def claim_by_id(claim_id: str) -> dict:
    ledger = load_claim_boundaries()
    for claim in ledger["claims"]:
        if claim["claim_id"] == claim_id:
            return claim
    raise KeyError(claim_id)
