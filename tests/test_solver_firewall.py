import unittest
import numpy as np
from scipy import sparse

from neurometbench_ref.firewall import assert_artifact_use_allowed
from neurometbench_ref.solver import (
    INVALID_FLUX_SHA256,
    MODEL_SHA256,
    MRAS_SHA256,
    primal_feasibility,
    tolerance_based_zero_qp_classification,
)

class SolverFirewallTests(unittest.TestCase):
    def test_primal_feasible(self):
        result = primal_feasibility(
            sparse.csr_matrix([[1.0, -1.0]]),
            [1.0, 1.0],
            [0.0, 0.0],
            [2.0, 2.0],
        )
        self.assertTrue(result["feasible"])

    def test_primal_infeasible(self):
        result = primal_feasibility(
            sparse.csr_matrix([[1.0, -1.0]]),
            [1.0, 0.0],
            [0.0, 0.0],
            [2.0, 2.0],
        )
        self.assertFalse(result["feasible"])

    def test_tolerance_based_zero_classification(self):
        result = tolerance_based_zero_qp_classification(
            zero_vector_feasible=True,
            maximum_feasible_biomass=0.0,
        )
        self.assertTrue(result["tolerance_based_zero_classification"])
        self.assertFalse(result["exact_unique_optimum_proven"])

    def test_small_positive_biomass_below_tolerance_is_not_exact_proof(self):
        result = tolerance_based_zero_qp_classification(
            zero_vector_feasible=True,
            maximum_feasible_biomass=5e-11,
            biomass_tolerance=1e-10,
        )
        self.assertTrue(result["tolerance_based_zero_classification"])
        self.assertFalse(result["exact_unique_optimum_proven"])
        self.assertGreater(result["maximum_feasible_biomass"], 0.0)

    def test_invalid_flux_forbidden_for_biology(self):
        with self.assertRaises(PermissionError):
            assert_artifact_use_allowed(INVALID_FLUX_SHA256, "affirmative_biology")
        self.assertTrue(assert_artifact_use_allowed(INVALID_FLUX_SHA256, "numerical_failure_fixture")["allowed"])

    def test_model_and_mras_roles(self):
        self.assertTrue(assert_artifact_use_allowed(MODEL_SHA256, "numerical_model")["allowed"])
        self.assertTrue(assert_artifact_use_allowed(MRAS_SHA256, "bound_input")["allowed"])

if __name__ == "__main__": unittest.main()
