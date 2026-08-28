import unittest
import numpy as np
import pandas as pd
from neurometbench_ref.aggregate import aggregate_patient_correlations
from neurometbench_ref.schemas import validate_patient_effect_table

class SchemaAggregateTests(unittest.TestCase):
    def test_patient_level(self):
        frame=pd.DataFrame({"metric":["M","M"],"patient":["P1","P2"],"patient_effect":[-0.0152073958296406,-0.289343094487445]})
        receipt=validate_patient_effect_table(frame);self.assertTrue(receipt["patient_level_unit_enforced"])
        result=aggregate_patient_correlations(frame)[0];self.assertEqual(result["n_patients"],2);self.assertAlmostEqual(result["exact_sign_flip_p"],0.5)
    def test_duplicate_patient_rejected(self):
        frame=pd.DataFrame({"metric":["M","M"],"patient":["P1","P1"],"patient_effect":[0.1,0.2]})
        with self.assertRaises(ValueError):validate_patient_effect_table(frame)
    def test_nonfinite_effects_rejected(self):
        for bad in [np.inf,-np.inf,np.nan]:
            frame=pd.DataFrame({"metric":["M"],"patient":["P1"],"patient_effect":[bad]})
            with self.assertRaises(ValueError):validate_patient_effect_table(frame)

    def test_blank_identifier_rejected(self):
        frame = pd.DataFrame({"metric":["M"," "],"patient":["P1","P2"],"patient_effect":[0.1,0.2]})
        with self.assertRaises(ValueError):
            validate_patient_effect_table(frame)

    def test_empty_table_rejected(self):
        frame=pd.DataFrame(columns=["metric","patient","patient_effect"])
        with self.assertRaises(ValueError):validate_patient_effect_table(frame)
    def test_out_of_range_correlation_rejected_during_aggregation(self):
        frame=pd.DataFrame({"metric":["M","M"],"patient":["P1","P2"],"patient_effect":[0.2,1.1]})
        with self.assertRaises(ValueError):aggregate_patient_correlations(frame)
if __name__=="__main__":unittest.main()
