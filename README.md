# NeuroMetBench

NeuroMetBench is a patient-aware neuroinformatics framework for evaluating transcript-derived metabolic inference. It separates biological sampling-unit validity, cross-modal concordance, development-to-external transport, comparator compatibility, missingness, multiplicity, and numerical admissibility rather than collapsing heterogeneous tasks into a single leaderboard.

## Current scientific reproducibility release

Version 2.0.2 is a scientific reproducibility and traceability repair to v2.0.1. It does not change any frozen biological endpoint, cohort, threshold, statistical result, adverse result, or interpretation boundary from v2.0.0.

Article identity:

**NeuroMetBench: A patient-aware neuroinformatics framework for multi-axis evaluation of transcript-derived metabolic inference in glioma**

Zenodo version DOI: https://doi.org/10.5281/zenodo.22058177

Zenodo concept DOI: https://doi.org/10.5281/zenodo.21830887

Release asset: `reproducibility_release.zip`

SHA-256:

`a7f65a28d633441f0900f68957500022b0835aa2b38a8f558b1630b6ceade8b9`

Version 2.0.2 repairs current method-result-claim traceability, reconstructs exact LSCC and CNS/HGG cohort flow from archived metadata and selection locks, exposes all scenario-level simulation failures, expands comparator execution and licensing provenance, corrects figure missing-value semantics, supplies portal-ready figure descriptions, and adds complete-inventory clean-room verification.

## Frozen headline results

- LSCC cross-cancer stress test: n=89, serine de novo Spearman rho=0.9070558388598963, 100,000-permutation p=9.99990000099999e-06, bootstrap 95% CI [0.8496172720469373, 0.9387662754309077].
- CNS/high-grade-glioma generalization: n=90, serine de novo Spearman rho=0.6266145829894963, 100,000-permutation p=9.99990000099999e-06, bootstrap 95% CI [0.4696652580556697, 0.7506606861648679].
- Development-to-external transport: 33 matched method-endpoint cells, 30/33 sign retention, three reversals, effect-rank Spearman rho=0.6424749163879598.
- Numerical axis: 113/113 archived METAFlux vectors pass the frozen 1e-3 primal-feasibility compatibility threshold; the reaction-order-swap stress test remains undetected, so solver optimality or comprehensive numerical validity is not claimed.

## Reproduction

Extract `reproducibility_release.zip`, install the pinned dependencies, and run:

```text
python reproducibility/verify_everything.py
```

A passing run ends with `NEUROMETBENCH_V2_0_2_EVERYTHING_PASS` after 16 independent and cross-linked checks, including two consecutive byte-identical figure reconstructions.

The root `SHA256SUMS.txt` covers the current reusable software and current v2.0.2 metadata. Immutable historical-release directories remain outside that current-state manifest.

## Software component

The reusable `neurometbench-ref` software component remains version 1.0.1. Version 2.0.2 refers to the scientific repository and reproducibility release, not a change to that software package API.

## Scientific boundaries

NeuroMetBench is not a flux predictor and does not claim measured or absolute flux, universal method superiority, an untouched holdout, public preregistration, full empirical calibration, or GBM-only generalization for the CNS cohort. The broad simulation used a Pearson/t/Fisher-z proxy rather than the empirical Spearman/permutation/bootstrap engine. Technical non-execution remains separate from biological discordance.

## Historical releases

Historical v1.0.0, v1.0.1, v1.1.0, v2.0.0, and v2.0.1 artifacts remain immutable. Version 2.0.2 does not overwrite or retag them.

## License and data rights

Repository-authored software materials are distributed under the MIT License. The license does not relicense third-party datasets, dependencies, or source-study materials. Raw third-party molecular matrices are not redistributed where source terms or repository policy govern access.
