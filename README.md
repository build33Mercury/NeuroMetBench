# NeuroMetBench

NeuroMetBench is a patient-aware evaluation framework for transcript-derived metabolic inference. It separates biological sampling-unit validity, cross-modal concordance, development-to-external transport, comparator compatibility, missingness, multiplicity, and numerical admissibility rather than collapsing heterogeneous tasks into a single leaderboard.

## Current repository status

A **v2.0.0 scientific reproducibility release candidate** has been prepared for:

**NeuroMetBench: Patient-Aware Evaluation of Transcript-Derived Metabolic Inference Across Glioma and External Proteogenomic Cohorts**

The candidate package includes the revised manuscript, publication figures and source tables, patient-level derived score authorities for the primary LSCC and CNS analyses, machine-readable claim/adverse/limitation ledgers, and clean-room verification scripts. Publication is controlled by the repository's fail-closed clean-room release workflow. v2.0.0 should be cited only after the public GitHub Release and corresponding archival record exist.

Headline results include the held-out LSCC serine de novo primary (n=89, Spearman rho=0.9071), development-disjoint CNS/high-grade-glioma generalization (n=90, rho=0.6266), a 33-cell development-to-external transport analysis with three sign reversals, and a narrowed numerical compatibility result. The frozen broad calibration criteria were not fully met, so the project does not use `reliability-calibrated` as a scientific claim.

## Software component

The reusable `neurometbench-ref` software component remains **v1.0.1**. The v2.0.0 number refers to the scientific repository/reproducibility release, not a change to that software package API.

## Scientific boundaries

NeuroMetBench is not a flux predictor and does not claim measured or absolute flux, universal method superiority, an untouched holdout, public preregistration, full empirical calibration, or GBM-only generalization for the CNS cohort. Technical non-execution remains separate from biological discordance.

## Historical releases

Historical v1.0.0, v1.0.1, and v1.1.0 artifacts are preserved and are not overwritten by the v2.0.0 release candidate.

## License

Repository-authored software materials are distributed under the MIT License. Third-party data remain under their source-specific terms and are not redistributed where those terms prohibit redistribution.
