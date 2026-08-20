# NeuroMetBench v2.0.0 scientific reproducibility release

NeuroMetBench is a patient-aware evaluation architecture for transcript-derived metabolic inference. This directory records the manuscript-facing v2.0.0 scientific snapshot.

## Article identity

**NeuroMetBench: Patient-Aware Evaluation of Transcript-Derived Metabolic Inference Across Glioma and External Proteogenomic Cohorts**

Author: Abdsalam Bitar, Independent Researcher, Amman, Jordan. ORCID: 0009-0009-9517-636X.

## Public archive identity

GitHub Release: https://github.com/build33Mercury/NeuroMetBench/releases/tag/v2.0.0

Zenodo version DOI: https://doi.org/10.5281/zenodo.22029697

Zenodo concept DOI: https://doi.org/10.5281/zenodo.21830887

Archive: `NeuroMetBench_v2.0.0_reproducibility_release.zip`

SHA256: `63947a8215be91402570a4c724f492242e2a972ca3665fd24271ae3da9eea174`

The GitHub and Zenodo archive copies were independently retrieved through public unauthenticated endpoints and verified to match this SHA256 exactly.

## Locked headline results

- Held-out CPTAC LSCC primary: 89 patients, BSL02 serine de novo Spearman rho = 0.9070558389, 100,000-permutation p = 9.9999e-06, bootstrap 95% CI = [0.8496172720, 0.9387662754].
- Matched random three-gene specificity analysis: observed serine construction at the 99.324th percentile of the matched null, empirical p = 0.00677. The three-gene aggregate did not outperform the best observed single gene, PSAT1.
- Development-to-external transport: 33 matched method-endpoint cells, rank stability rho = 0.6424749164, sign retention 30/33, three sign reversals.
- Hierarchical simulation: the frozen broad and supported-domain calibration criteria were not fully met. The term `reliability-calibrated` is therefore not used for this release.
- Development-disjoint CNS/high-grade-glioma generalization: 90 evaluable patients, rho = 0.6266145830, permutation p = 9.9999e-06, bootstrap 95% CI = [0.4696652581, 0.7506606862].
- Numerical axis: all 113 stored METAFlux vectors passed the frozen 1e-3 primal-feasibility compatibility threshold. A controlled reaction-order swap was not detected, so this is not a claim of comprehensive numerical validation.

## Interpretation boundaries

This release does not claim measured or absolute metabolic flux, universal method superiority, an untouched holdout, external public preregistration, full empirical calibration, or GBM-only generalization for the CNS cohort. Technical non-execution is not counted as adverse biology. ACT03/GSVA and ACT05/MetroSCREEN MetaModule share a GSVA scoring layer and are not independent algorithmic evidence.

## Publication status

The v2.0.0 reproducibility archive is published on GitHub and Zenodo. Historical releases are preserved and are not overwritten.
