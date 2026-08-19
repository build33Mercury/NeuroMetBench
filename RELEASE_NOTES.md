# NeuroMetBench v2.0.0 release candidate

NeuroMetBench v2.0.0 is the manuscript-facing scientific reproducibility release for the rebuilt study. The public GitHub Release and version-specific Zenodo DOI are not considered final until the clean-room publication workflow completes and the public assets are independently re-downloaded and hash-verified.

## Scientific scope

The release adds a development-to-external transport analysis, serine-specificity stress testing, external missingness and comparator-fairness audits, dependence-sensitive multiplicity checks, hierarchical simulations, framework ablations, a narrowed numerical compatibility analysis, and development-disjoint CNS/high-grade-glioma generalization.

The frozen broad reliability-calibration criteria were not fully met. The term `reliability-calibrated` is therefore not used as a scientific claim.

## Locked headline results

- Held-out LSCC serine de novo primary: n=89, Spearman rho=0.9070558389, 100,000-permutation p=9.9999e-06, bootstrap 95% CI [0.849617, 0.938766].
- Development-disjoint CNS/high-grade-glioma serine de novo generalization: n=90, rho=0.6266145830, 100,000-permutation p=9.9999e-06, bootstrap 95% CI [0.469665, 0.750661].
- Development-to-external transport: 33 matched method-endpoint cells, sign agreement 30/33, three sign reversals, effect-rank Spearman rho=0.642475.
- Numerical axis: primal-feasibility compatibility check at the frozen 1e-3 project threshold only.

## Preserved limiting evidence

The release retains the lack of aggregation superiority over PSAT1, three transport reversals, algorithmic dependence of ACT03 and ACT05 through GSVA, batch-structured TCA/OXPHOS evaluability, unsupported CNS OXPHOS, calibration failure under the frozen criteria, and failure of the primal-feasibility gate to detect reaction-order swaps.

Historical v1.0.0, v1.0.1, and v1.1.0 artifacts are preserved unchanged.
