from __future__ import annotations
import json, numpy as np
from neurometbench_ref import __version__
from neurometbench_ref.firewall import assert_artifact_use_allowed, claim_by_id
from neurometbench_ref.fixtures import fixture_summary
from neurometbench_ref.solver import INVALID_FLUX_SHA256, tolerance_based_zero_qp_classification
from neurometbench_ref.statistics import benjamini_hochberg, exact_sign_flip_pvalue
summary=fixture_summary();r=summary["regression_expectations"]
checks={
"version_1_0_2":__version__=="1.0.2",
"human_isotope_rho":r["human_isotope"]["A_primary_rho"]==1.0,
"human_isotope_exact_p":abs(r["human_isotope"]["A_primary_exact_p"]-1/3)<1e-15,
"cptac_transport":abs(r["cptac_rna_protein"]["transport_rho"]-0.6032900004412324)<1e-15,
"spatial_primary":abs(r["spatial_association"]["primary_effect"]+0.1552628978138)<1e-15,
"saved_vector_infeasibility":r["numerical_validity"]["infeasible_flux_columns"]==42,
"tolerance_classification_count":r["numerical_validity"]["tolerance_based_zero_classifications"]==42,
"no_exact_optimum_claim":r["numerical_validity"]["exact_unique_optimum_proven_count"]==0,
"small_positive_edge_case":not tolerance_based_zero_qp_classification(zero_vector_feasible=True,maximum_feasible_biomass=5e-11)["exact_unique_optimum_proven"],
"bh_known_answer":bool(np.allclose(benjamini_hochberg([0.01,0.04,0.03]),[0.03,0.04,0.04])),
"claim_firewall":assert_artifact_use_allowed(INVALID_FLUX_SHA256,"numerical_failure_fixture")["allowed"],
"claim_lookup":claim_by_id("NO_ABSOLUTE_FLUX")["claim_id"]=="NO_ABSOLUTE_FLUX",
}
failed=[n for n,ok in checks.items() if not ok];record={"check_count":len(checks),"passed_count":len(checks)-len(failed),"status":"PASS" if not failed else "FAIL","checks":checks};print(json.dumps(record,indent=2));
if failed:raise SystemExit("failed: "+", ".join(failed))
