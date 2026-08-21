# Changelog

## 2.0.1 - 2026-08-21

Documentation and reproducibility correction. Scientific results are unchanged from v2.0.0.

- Synchronized the scientific release title, version, DOI, and repository metadata with the current manuscript identity.
- Added parser-independent hexadecimal float64 authorities for the LSCC and CNS/HGG primary patient-level analyses.
- Added exact bit-identity and statistics verification.
- Changed final figure generation so primary headline statistics are computed from verified authorities rather than supplied as literal annotations.
- Recorded the exact historical scCellFie 0.6.2 source commit `bad8ea9afcd898c8633dac7d3ab1f83dc086b9b1`.
- Preserved all v2.0.0 biological endpoints, cohorts, thresholds, results, adverse findings, and claim ceilings unchanged.

## 2.0.0 - 2026-08-20

Major scientific reproducibility release for the rebuilt NeuroMetBench study.

- Added serine-specificity stress testing, gene decomposition, leave-one-gene-out analysis, matched random three-gene controls, global-concordance adjustment, and influence diagnostics.
- Added explicit development-to-external transport across 33 matched method-endpoint cells, including three retained sign reversals.
- Added external missingness/evaluability and native-domain comparator fairness audits.
- Added Benjamini-Yekutieli dependence sensitivity for the external method-endpoint family.
- Added frozen hierarchical simulation and component ablation analyses. Broad reliability calibration was not earned and is not claimed.
- Narrowed the numerical claim to a primal-feasibility compatibility check at the frozen 1e-3 project threshold.
- Added development-disjoint CNS/high-grade-glioma generalization with 90 evaluable primary patients.
- Added rebuilt patient-level figures, machine-readable claim, adverse-result, and limitation ledgers, and clean-room reproduction scripts.
- Preserved adverse findings, including lack of aggregation superiority over PSAT1, batch-structured TCA/OXPHOS evaluability, unsupported CNS OXPHOS, and failure of the primal-feasibility gate to detect reaction-order swaps.

The reusable `neurometbench-ref` software component remains version 1.0.1. Version 2.0.0 refers to the scientific repository and reproducibility release.

## 1.1.0 - 2026-08-18

Historical project reproducibility authority adding the frozen post-development external proteogenomic evaluation. Preserved unchanged under `releases/1.1.0/`.

## 1.0.1 - 2026-08-08

Corrective maintenance release.

- Replaced over-strong exact/unique-zero language with tolerance-based zero-solution classification.
- Removed the misleading legacy exact-certificate helper from the public API.
- Added a regression case showing that a positive threshold classification is not an exact-optimum proof.
- Published the complete 15-test software regression suite and conventional source/build metadata.

## 1.0.0 - 2026-08-06

Historical initial release. Superseded for software use by v1.0.1 because the original numerical certificate terminology was too strong.
