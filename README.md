# NeuroMetBench

NeuroMetBench is a patient-aware neuroinformatics framework for evaluating transcript-derived metabolic inference. It separates biological sampling-unit validity, cross-modal concordance, development-to-external transport, comparator compatibility, missingness, multiplicity, and numerical admissibility rather than collapsing heterogeneous tasks into a single leaderboard.

## Current scientific reproducibility release

Version 2.0.1 is a documentation, reproducibility, and metadata correction to v2.0.0. It does not change any frozen biological endpoint, cohort, threshold, statistical result, adverse result, or claim ceiling.

Article identity:

**NeuroMetBench: A patient-aware neuroinformatics framework for multi-axis evaluation of transcript-derived metabolic inference in glioma**

Zenodo version DOI: https://doi.org/10.5281/zenodo.22036411

Zenodo concept DOI: https://doi.org/10.5281/zenodo.21830887

Release asset: `reproducibility_release.zip`

SHA-256:

`9037a5fb31f0ba2dd3e62d5cfca1604620c2cb8bcaa26ecbfa19fea657027514`

Version 2.0.1 adds parser-independent primary float64 statistical authorities, exact statistics verification, synchronized release metadata, and the exact scCellFie v0.6.2 source commit used by the historical execution.

## Frozen headline results

- LSCC cross-cancer external stress test: n=89, serine de novo Spearman rho=0.9070558388598963, 100,000-permutation p=9.99990000099999e-06, bootstrap 95% CI [0.8496172720469373, 0.9387662754309077].
- CNS/high-grade-glioma generalization: n=90, serine de novo Spearman rho=0.6266145829894963, 100,000-permutation p=9.99990000099999e-06, bootstrap 95% CI [0.4696652580556697, 0.7506606861648679].
- Development-to-external transport: 33 matched method-endpoint cells, 30/33 sign retention, three reversals, effect-rank Spearman rho=0.6424749163879598.
- Numerical axis: 113/113 archived METAFlux vectors pass the frozen 1e-3 primal-feasibility threshold; the reaction-order-swap stress test remains undetected, so solver optimality or comprehensive numerical validity is not claimed.

## Software component

The reusable `neurometbench-ref` software component remains version 1.0.1. Version 2.0.1 refers to the scientific repository and reproducibility release, not a change to that software package API.

## Scientific boundaries

NeuroMetBench is not a flux predictor and does not claim measured or absolute flux, universal method superiority, an untouched holdout, public preregistration, full empirical calibration, or GBM-only generalization for the CNS cohort. Technical non-execution remains separate from biological discordance.

## Historical releases

Historical v1.0.0, v1.0.1, v1.1.0, and v2.0.0 artifacts remain preserved. Version 2.0.1 does not overwrite or retag them.

## License

Repository-authored software materials are distributed under the MIT License. Third-party data remain under their source-specific terms and are not redistributed where those terms prohibit redistribution.
