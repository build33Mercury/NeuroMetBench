# NeuroMetBench v2.0.0

Major scientific reproducibility release for the rebuilt NeuroMetBench manuscript.

## Added

- Primary serine-specificity stress testing with gene decomposition, leave-one-gene-out analysis, matched random three-gene controls, global-concordance adjustment, and influence diagnostics.
- Explicit development-to-external transport analysis across 33 matched method-endpoint cells, including three retained sign reversals.
- External missingness/evaluability and native-domain comparator fairness audits.
- Benjamini-Yekutieli dependence sensitivity for the external method-endpoint family.
- Frozen hierarchical simulation and component ablation analyses. Calibration criteria were not fully met, so calibration wording was removed.
- Narrowed numerical claim supported by a primal-feasibility tolerance sweep and controlled corruption tests.
- Development-disjoint CNS/high-grade-glioma generalization analysis with 90 evaluable patients.
- Rebuilt patient-level figures, machine-readable claim ledger, adverse-result ledger, limitations ledger, and manuscript claim traceability.

## Preserved adverse and limiting evidence

- The three-gene serine aggregate did not outperform PSAT1.
- Three development-to-external sign reversals are retained.
- TCA and OXPHOS protein evaluability is strongly PDC-plex structured in external analyses.
- OXPHOS is not supported in the CNS generalization cohort.
- Broad framework calibration is not earned.
- Reaction-order swaps are not detected by the frozen primal-feasibility gate.
- ACT03 and ACT05 are algorithmically dependent through GSVA.

## Archive identity

Zenodo version DOI: https://doi.org/10.5281/zenodo.22029697

Archive SHA256: `63947a8215be91402570a4c724f492242e2a972ca3665fd24271ae3da9eea174`

## Versioning

This is a new scientific release. It does not rewrite or replace historical v1.0.0, v1.0.1, or v1.1.0 artifacts. The `neurometbench-ref` software component remains version 1.0.1 unless separately changed in a future software release.
