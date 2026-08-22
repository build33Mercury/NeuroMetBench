# Release notes

## 2.0.2, 22 August 2026

Scientific reproducibility, provenance, traceability, and figure-semantics repair. Frozen scientific results are unchanged from v2.0.0.

Changes:

- replaced stale active evidence paths with exact current manuscript, authority, selector, and method-result-claim mappings;
- reconstructed LSCC and CNS/HGG cohort flows from archived metadata and selection locks, including reason-level and identifier-level exclusions;
- exposed all 432 simulation scenarios and the concentrated supported-domain and broad-domain failures;
- disclosed that the broad simulation used a Pearson/t/Fisher-z proxy rather than the empirical Spearman/permutation/bootstrap engine;
- specified the exact external BSL01 construction and the MetroSCREEN v0.91 released `cal_MetaModule` implementation, including its GSVA dependence;
- retained and reverified the full 39-cell external family and the 34-cell ACT05-excluded dependence sensitivity;
- corrected Figure 2 and Figure 5 missing-value semantics so not-evaluated quantities are not plotted as zero;
- supplied portal-ready alternative descriptions for Figures 1-7 without claiming tagged-PDF accessibility;
- added complete checksum inventories, registry verification, exact cohort reconstruction, and a 16-check `verify_everything.py` clean-room entry point;
- preserved all adverse findings, non-admissions, technical failures, version boundaries, and source-rights limitations.

The reusable `neurometbench-ref` software component remains version 1.0.1. Historical releases are not rewritten or retagged.

## 2.0.1, 21 August 2026

Documentation and reproducibility correction. Scientific results remained unchanged from v2.0.0.
