import unittest
from neurometbench_ref.coverage import coverage_gate
class CoverageTests(unittest.TestCase):
    def test_exact_minimum_pass(self):
        r=coverage_gate(["A","B","C"],["A","B"],2);self.assertTrue(r.passed);self.assertEqual(r.fraction,2/3)
    def test_below_minimum_fail(self):self.assertFalse(coverage_gate(["A","B","C"],["A"],2).passed)
if __name__=="__main__":unittest.main()
