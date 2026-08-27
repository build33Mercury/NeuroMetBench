# NeuroMetBench v2.1.0

Version 2.1.0 is a new post-rejection scientific state. The rejected Neuroinformatics submission and public v2.0.7 release remain immutable historical evidence.

## Scientific changes

- Reframed the manuscript for a Methodology submission to Functional & Integrative Genomics around patient-aware evidence bounds for transcript-derived metabolic representations across cancer proteogenomic contexts.
- Added a frozen exploratory cross-cohort attenuation analysis comparing the same serine representation in LSCC and CNS/high-grade-glioma cohorts. The observed Spearman difference is 0.2804412558704000 with a 100,000-replicate independent-patient bootstrap 95% interval of [0.14267615, 0.43803676].
- Consolidated the cross-context serine evidence into a revised main figure and moved the METAFlux numerical sensitivity figure to the supplement.
- Narrowed novelty and interpretation claims to the evidence actually supported by the package.

## Preserved adverse boundaries

Version 2.1.0 does not convert adverse or non-admitted findings into positive evidence. It does not claim measured flux, independent biochemical validation, universal superiority, full calibration, solver optimality, clinical validity, or superiority of the three-gene serine aggregate over PSAT1.

## Reproducibility

The revised Online Resource 2 contains deterministic verification of the frozen patient-level statistics, the post-rejection attenuation analysis, cohort reconstruction, transport results, multiplicity families, simulation summaries, specificity provenance, numerical-threshold provenance, figure generation, and a complete checksum manifest.

The reusable `neurometbench-ref` software component remains version 1.0.1 and is versioned separately from the article/reproducibility archive.
