import unittest
import numpy as np

from neurometbench_ref.statistics import (
    benjamini_hochberg,
    exact_sign_flip_pvalue,
    fisher_z_equal_weight,
    midrank_percentile,
    pairwise_order_accuracy,
)

class StatisticsTests(unittest.TestCase):
    def test_bh(self):
        observed = benjamini_hochberg([0.01, 0.04, 0.03])
        self.assertTrue(np.allclose(observed, [0.03, 0.04, 0.04]))

    def test_two_patient_sign_flip(self):
        p = exact_sign_flip_pvalue([-0.0152073958296406, -0.289343094487445])
        self.assertAlmostEqual(p, 0.5)

    def test_fisher_z(self):
        value = fisher_z_equal_weight([0.2, 0.4])
        expected = np.tanh((np.arctanh(0.2) + np.arctanh(0.4)) / 2)
        self.assertAlmostEqual(value, expected)

    def test_midranks(self):
        self.assertTrue(np.allclose(midrank_percentile([1, 2, 2, 4]), [0, 0.5, 0.5, 1]))

    def test_pairwise(self):
        result = pairwise_order_accuracy([1,2,3], [4,5,6])
        self.assertEqual(result["concordant"], 3)
        self.assertEqual(result["accuracy"], 1.0)

if __name__ == "__main__": unittest.main()
