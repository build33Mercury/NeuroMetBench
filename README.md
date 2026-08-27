# NeuroMetBench v2.1.0

NeuroMetBench v2.1.0 is the post-rejection scientific revision of the NeuroMetBench manuscript and reproducibility package, prepared for submission as a Methodology article to Functional & Integrative Genomics.

The historical v2.0.7 state remains immutable and corresponds to the manuscript rejected by Neuroinformatics. Version 2.1.0 is a new scientific state. It does not overwrite or relabel v2.0.7.

## Scientific scope

The revision reframes NeuroMetBench as a patient-aware evidence-bounding methodology for transcript-derived metabolic representations across cancer proteogenomic contexts. Glioma remains a principal biological context, but the article no longer claims a generally validated neuroinformatics framework.

The package preserves adverse and non-admitted findings. In particular, it does not claim measured metabolic flux, universal method superiority, independent biochemical validation, full calibration, solver optimality, general clinical validity, or superiority of the three-gene serine aggregate over PSAT1.

## New post-rejection analysis

A frozen exploratory cross-cohort attenuation analysis compares the same serine representation across the LSCC and CNS/high-grade-glioma cohorts. The frozen authorities are:

- LSCC: n=89, Spearman rho=0.9070558388598963
- CNS/high-grade-glioma: n=90, Spearman rho=0.6266145829894963
- Difference in rho: 0.2804412558704000
- 100,000-replicate independent-patient bootstrap 95% interval: [0.14267615, 0.43803676]

The post-rejection analysis is exploratory and is not represented as preregistered confirmation.

## Reproducibility

The v2.1.0 release archive contains the exact revised manuscript, supplementary information, a clean-room reproducibility package with source data, code, checksums, deterministic verifiers, and a final verification record.

## Reusable software component

The repository also contains `neurometbench-ref` version 1.0.1, a separately versioned Python reference component for patient-level aggregation/statistics, FDR utilities, artifact checks, schema validation, and numerical edge-case classification. The article/reproducibility archive version (2.1.0) and software component version (1.0.1) are intentionally distinct.

## Public lineage

Stable Zenodo concept DOI: 10.5281/zenodo.21830887

Historical releases remain immutable. The exact v2.1.0 version DOI and public asset hash are recorded only after hosted publication and independent public-download verification.
