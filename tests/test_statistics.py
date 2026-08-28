import unittest
import numpy as np
from neurometbench_ref.statistics import benjamini_hochberg, exact_sign_flip_pvalue, fisher_z_equal_weight, midrank_percentile, pairwise_order_accuracy
class StatisticsTests(unittest.TestCase):
    def test_bh(self):self.assertTrue(np.allclose(benjamini_hochberg([0.01,0.04,0.03]),[0.03,0.04,0.04]))

    def test_bh_rejects_infinity(self):
        with self.assertRaises(ValueError):
            benjamini_hochberg([0.1, np.inf])

    def test_two_patient_sign_flip(self):self.assertAlmostEqual(exact_sign_flip_pvalue([-0.0152073958296406,-0.289343094487445]),0.5)
    def test_fisher_z(self):
        v=fisher_z_equal_weight([0.2,0.4]);exp=np.tanh((np.arctanh(0.2)+np.arctanh(0.4))/2);self.assertAlmostEqual(v,exp)
    def test_fisher_z_rejects_impossible_correlations(self):
        for vals in [[1.01,0.2],[-1.01,0.2]]:
            with self.assertRaises(ValueError):fisher_z_equal_weight(vals)
    def test_midranks(self):self.assertTrue(np.allclose(midrank_percentile([1,2,2,4]),[0,0.5,0.5,1]))
    def test_midranks_reject_empty(self):
        with self.assertRaises(ValueError):midrank_percentile([])
    def test_pairwise(self):
        result=pairwise_order_accuracy([1,2,3],[4,5,6]);self.assertEqual(result["concordant"],3);self.assertEqual(result["accuracy"],1.0)
    def test_pairwise_rejects_nonfinite(self):
        with self.assertRaises(ValueError):pairwise_order_accuracy([1,np.nan],[2,3])
if __name__=="__main__":unittest.main()
