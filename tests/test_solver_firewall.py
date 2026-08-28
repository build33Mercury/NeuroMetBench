import unittest
import numpy as np
from scipy import sparse
from neurometbench_ref.firewall import assert_artifact_use_allowed, claim_by_id
from neurometbench_ref.solver import INVALID_FLUX_SHA256,MODEL_SHA256,MRAS_SHA256,primal_feasibility,tolerance_based_zero_qp_classification
class SolverFirewallTests(unittest.TestCase):
    def test_primal_feasible(self):self.assertTrue(primal_feasibility(sparse.csr_matrix([[1.0,-1.0]]),[1,1],[0,0],[2,2])["feasible"])
    def test_primal_infeasible(self):self.assertFalse(primal_feasibility(sparse.csr_matrix([[1.0,-1.0]]),[1,0],[0,0],[2,2])["feasible"])
    def test_nonfinite_and_invalid_bounds_rejected(self):
        with self.assertRaises(ValueError):primal_feasibility([[1]], [np.nan], [0], [2])
        with self.assertRaises(ValueError):primal_feasibility([[1]], [1], [2], [0])
        with self.assertRaises(ValueError):primal_feasibility([[1]], [1], [0], [2], tolerance=-1)
    def test_tolerance_zero(self):
        r=tolerance_based_zero_qp_classification(zero_vector_feasible=True,maximum_feasible_biomass=0);self.assertTrue(r["tolerance_based_zero_classification"]);self.assertFalse(r["exact_unique_optimum_proven"])
    def test_small_positive_below_tolerance_not_exact(self):
        r=tolerance_based_zero_qp_classification(zero_vector_feasible=True,maximum_feasible_biomass=5e-11,biomass_tolerance=1e-10);self.assertTrue(r["tolerance_based_zero_classification"]);self.assertFalse(r["exact_unique_optimum_proven"])

    def test_nonfinite_biomass_rejected(self):
        with self.assertRaises(ValueError):
            tolerance_based_zero_qp_classification(zero_vector_feasible=True, maximum_feasible_biomass=float("inf"))

    def test_negative_tolerance_rejected(self):
        with self.assertRaises(ValueError):tolerance_based_zero_qp_classification(zero_vector_feasible=True,maximum_feasible_biomass=0,biomass_tolerance=-1)
    def test_invalid_flux_forbidden_for_biology(self):
        with self.assertRaises(PermissionError):assert_artifact_use_allowed(INVALID_FLUX_SHA256,"affirmative_biology")
        self.assertTrue(assert_artifact_use_allowed(INVALID_FLUX_SHA256,"numerical_failure_fixture")["allowed"])
    def test_model_and_mras_roles(self):
        self.assertTrue(assert_artifact_use_allowed(MODEL_SHA256,"numerical_model")["allowed"]);self.assertTrue(assert_artifact_use_allowed(MRAS_SHA256,"bound_input")["allowed"])
    def test_claim_lookup_permitted_and_forbidden(self):
        self.assertEqual(claim_by_id("PATIENT_LEVEL_INFERENCE")["claim_id"],"PATIENT_LEVEL_INFERENCE")
        self.assertEqual(claim_by_id("NO_ABSOLUTE_FLUX")["claim_id"],"NO_ABSOLUTE_FLUX")
        with self.assertRaises(KeyError):claim_by_id("DOES_NOT_EXIST")
if __name__=="__main__":unittest.main()
