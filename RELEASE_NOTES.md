# NeuroMetBench v1.0.1

This corrective release addresses a numerical-semantics issue in v1.0.0. A maximum-biomass solver result at or below `1e-10` is now explicitly a tolerance-based numerical classification, not a proof of exact unique optimality.

The release includes complete source, build metadata, a 15-test public regression suite, the corrected wheel, environment specification, and independent release assertions. No biological/statistical benchmark result was recomputed or changed. The separate conclusion that 0/42 archived nonzero METAFlux vectors satisfy the `1e-8` primal-feasibility threshold is unchanged.

## Archived release

Version-specific Zenodo DOI: `10.5281/zenodo.21847978`

