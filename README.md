# NeuroMetBench v2.1.1

NeuroMetBench is a patient-aware evidence-bounding methodology for evaluating transcript-derived metabolic representations across heterogeneous proteogenomic contexts. It keeps biological unit, endpoint identity, data-domain compatibility, uncertainty, multiplicity, transport, missingness, numerical diagnostics, provenance, and permitted claim wording distinct rather than collapsing them into a universal performance score.

The associated manuscript is:

**NeuroMetBench: Patient-aware evidence bounds for transcript-derived metabolic representations across cancer proteogenomic contexts**

The current article/reproducibility version is **2.1.1**. Historical public releases remain immutable.

## Scientific scope

The principal external endpoint is same-gene RNA-protein rank concordance. It is not measured metabolic flux, direct metabolomics, isotope-flux validation, clinical validation, or evidence of universal method superiority. Broad workflow calibration was not earned, some transport effects reverse sign, and the three-gene serine aggregate does not demonstrate superiority over PSAT1 alone.

The exploratory cross-cohort analysis compares the same frozen three-gene serine scoring rule across an LSCC stress-test cohort and a CNS/high-grade-glioma cohort. Because BSL02 uses cohort-relative percentile scores, its bootstrap intervals are conditional on the frozen cohort score constructions rather than uncertainty for a newly recalibrated deployable score.

## Reproducibility release

The frozen v2.1.1 public release asset is:

`NeuroMetBench_v2.1.1_reproducibility_release.zip`

- Size: **36,623,555 bytes**
- SHA-256: **cd809679d268674d45aa1c1e2f23de32146f0c59261b5137b5f25d7672848bef**

The release contains the manuscript and supplementary sources/PDFs, deterministic figures, Online Resource 2, closed-world verification, cross-package provenance, and the exact immutable v2.0.7 historical archive.

Stable Zenodo concept DOI: **10.5281/zenodo.21830887**

## Reusable software component

The repository source tree contains **`neurometbench-ref` 1.0.2**, a separately versioned Python helper implementation for patient-aware aggregation/statistics, multiplicity utilities, coverage checks, artifact-use firewalls, numerical compatibility checks, and regression fixtures.

Version 1.0.2 is a validation-only corrective patch. It repairs claim lookup and strengthens rejection of empty, non-finite, and out-of-range inputs in affected helper paths. It does **not** change any frozen article-level scientific authority.

The tested software stack is Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, and pandas 2.2.3. The exact tested wheel and verification logs are included in Online Resource 2 and the v2.1.1 reproducibility release.

`neurometbench-ref` is a reusable helper layer, not a universal automated implementation of every NeuroMetBench adjudication decision.

## Verification

The full v2.1.1 release is closed-world verified. From an extracted release root, run:

```bash
python reproducibility/verify_outer_release.py
```

Online Resource 2 contains deeper scientific, figure, claim-ledger, and software verification scripts.

## Data and licensing

Third-party raw molecular matrices are not redistributed where source terms, repository policy, or access conditions govern redistribution. The repository license applies to NeuroMetBench-authored code/documentation and does not relicense third-party datasets, dependencies, or source-study material.
