from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import pandas as pd

from .aggregate import aggregate_patient_correlations
from .firewall import verify_file_use
from .fixtures import fixture_summary
from .schemas import read_and_validate_patient_effect_table
from .solver import tolerance_based_zero_qp_classification
from .statistics import benjamini_hochberg, exact_sign_flip_pvalue


def write_json_output(obj, output: str | None) -> None:
    text = json.dumps(obj, indent=2, sort_keys=True)
    if output:
        Path(output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


def command_self_test() -> dict:
    checks = []
    checks.append(abs(exact_sign_flip_pvalue([-0.0152073958296406, -0.289343094487445]) - 0.5) < 1e-12)
    q = benjamini_hochberg([0.01, 0.04, 0.03])
    checks.append(q.shape == (3,))
    summary = fixture_summary()
    checks.append(summary["regression_expectations"]["numerical_validity"]["infeasible_flux_columns"] == 42)
    edge = tolerance_based_zero_qp_classification(zero_vector_feasible=True, maximum_feasible_biomass=5e-11)
    checks.append(edge["tolerance_based_zero_classification"] and not edge["exact_unique_optimum_proven"])
    if not all(checks):
        raise AssertionError("self-test failed")
    return {"status": "PASS", "checks": len(checks), "version": "1.0.1"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="neurometbench-ref")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("self-test")
    summary = sub.add_parser("fixture-summary"); summary.add_argument("--output")
    verify = sub.add_parser("verify-artifact"); verify.add_argument("--path", required=True); verify.add_argument("--purpose", required=True); verify.add_argument("--output")
    validate = sub.add_parser("validate-patient-table"); validate.add_argument("--input", required=True); validate.add_argument("--output")
    aggregate = sub.add_parser("aggregate-correlations"); aggregate.add_argument("--input", required=True); aggregate.add_argument("--output", required=True)
    bh = sub.add_parser("bh-fdr"); bh.add_argument("--input", required=True, help="CSV with a p_value column"); bh.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "self-test": write_json_output(command_self_test(), None)
        elif args.command == "fixture-summary": write_json_output(fixture_summary(), args.output)
        elif args.command == "verify-artifact": write_json_output(verify_file_use(args.path, args.purpose), args.output)
        elif args.command == "validate-patient-table": _, receipt = read_and_validate_patient_effect_table(args.input); write_json_output(receipt, args.output)
        elif args.command == "aggregate-correlations": frame, _ = read_and_validate_patient_effect_table(args.input); write_json_output(aggregate_patient_correlations(frame), args.output)
        elif args.command == "bh-fdr":
            frame = pd.read_csv(args.input)
            if "p_value" not in frame.columns: raise ValueError("input CSV requires p_value")
            frame["bh_q"] = benjamini_hochberg(frame["p_value"].to_numpy(dtype=float)); frame.to_csv(args.output, index=False)
        return 0
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr); return 2

if __name__ == "__main__":
    raise SystemExit(main())
