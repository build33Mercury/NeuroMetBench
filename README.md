# NeuroMetBench Reference Implementation v1.0.1

NeuroMetBench is a patient-aware validation and numerical-auditing framework for transcript-derived metabolic inference in glioblastoma. Version 1.0.1 is a corrective maintenance release that narrows the numerical zero-solution terminology and makes the complete public source/test state reproducible. It does not change the biological or statistical result values reported by the benchmark.

## Important v1.0.1 correction

A solver-reported maximum biomass at or below a positive tolerance is now treated only as a **tolerance-based zero-solution classification**. It is **not** treated as proof that the true maximum biomass is nonpositive and therefore is not an exact proof that zero is the unique QP optimum. The independent result that all 42 archived nonzero METAFlux vectors failed the prespecified `1e-8` primal-feasibility criterion is unchanged.

## Contents

- `src/neurometbench_ref/` - complete source tree
- `tests/` - complete public regression suite (15 tests)
- `dist/` - version-specific pure-Python wheel
- `verification/` - independent release assertions and verification record
- `environment.yml` - frozen dependency specification
- `CITATION.cff` - software citation metadata
- `SHA256SUMS.txt` - release-file checksums

## Installation

```bash
python -m pip install --no-cache-dir dist/neurometbench_ref-1.0.1-py3-none-any.whl
neurometbench-ref self-test
python -m pytest -q
```

The public test suite is expected to report **15 passed**.

## Scientific scope

The software enforces patient/equal-patient inference, exact finite-sample procedures, pathway-coverage checks, primal-feasibility auditing, tolerance-based numerical classification, and artifact-use safeguards. It is not a metabolic-flux predictor, does not establish transcript-derived scores as measured or absolute flux, and is not intended for clinical decision support.

## Archive

The corrected v1.0.1 release is archived under the version-specific Zenodo DOI [10.5281/zenodo.21847978](https://doi.org/10.5281/zenodo.21847978). The historical v1.0.0 archive remains unchanged.
