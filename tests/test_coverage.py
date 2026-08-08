import unittest
from neurometbench_ref.coverage import coverage_gate

class CoverageTests(unittest.TestCase):
    def test_exact_minimum_pass(self):
        result = coverage_gate(["A","B","C"], ["A","B"], 2)
        self.assertTrue(result.passed)
        self.assertEqual(result.fraction, 2/3)

    def test_below_minimum_fail(self):
        result = coverage_gate(["A","B","C"], ["A"], 2)
        self.assertFalse(result.passed)

if __name__ == "__main__": unittest.main()
