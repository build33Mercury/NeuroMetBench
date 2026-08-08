# Changelog

## 1.0.1 - 2026-08-08

Corrective maintenance release.

- Replaced over-strong exact/unique-zero language with tolerance-based zero-solution classification.
- Removed the misleading legacy exact-certificate helper from the public API; `tolerance_based_zero_qp_classification` is the supported numerical-threshold interface.
- Added a regression case with a small positive biomass below the tolerance, demonstrating that the threshold classification is not an exact-optimum proof.
- Published a complete conventional source tree and build metadata.
- Published the complete 15-test regression suite used for this release.
- Retained the independent 42/42 saved-vector primal-infeasibility result and all biological/statistical benchmark values.
- Removed development/cache residue from the release surface.

## 1.0.0 - 2026-08-06

Historical initial release. Superseded for manuscript use by v1.0.1 because the original numerical certificate terminology was too strong.
