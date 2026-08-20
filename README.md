# NeuroMetBench

NeuroMetBench is a patient-aware evaluation framework for transcript-derived metabolic inference. It separates biological sampling-unit validity, cross-modal concordance, development-to-external transport, comparator compatibility, missingness, multiplicity, and numerical admissibility rather than collapsing heterogeneous tasks into a single leaderboard.

## Current repository status

The **v2.0.0 scientific reproducibility release** is publicly available for:

**NeuroMetBench: Patient-Aware Evaluation of Transcript-Derived Metabolic Inference Across Glioma and External Proteogenomic Cohorts**

GitHub Release: https://github.com/build33Mercury/NeuroMetBench/releases/tag/v2.0.0

Zenodo version DOI: https://doi.org/10.5281/zenodo.22029697

Zenodo concept DOI: https://doi.org/10.5281/zenodo.21830887

Frozen reproducibility archive SHA256:
`63947a8215be91402570a4c724f492242e2a972ca3665fd24271ae3da9eea174`

The GitHub and Zenodo copies of `NeuroMetBench_v2.0.0_reproducibility_release.zip` were independently retrieved through unauthenticated public endpoints and verified to match this SHA256 exactly.

Headline results include the held-out LSCC serine de novo primary (n=89, Spearman rho=0.9071), development-disjoint CNS/high-grade-glioma generalization (n=90, rho=0.6266), a 33-cell development-to-external transport analysis with three sign reversals, and a narrowed numerical compatibility result. The frozen broad calibration criteria were not fully met, so the project does not use `reliability-calibrated` as a scientific claim.

## Software component

The reusable `neurometbench-ref` software component remains **v1.0.1**. The v2.0.0 number refers to the scientific repository and reproducibility release, not a change to that software package API.

## Scientific boundaries

NeuroMetBench is not a flux predictor and does not claim measured or absolute flux, universal method superiority, an untouched holdout, public preregistration, full empirical calibration, or GBM-only generalization for the CNS cohort. Technical non-execution remains separate from biological discordance.

## Historical releases

Historical v1.0.0, v1.0.1, and v1.1.0 artifacts are preserved and are not overwritten by v2.0.0.

## License

Repository-authored software materials are distributed under the MIT License. Third-party data remain under their source-specific terms and are not redistributed where those terms prohibit redistribution.
