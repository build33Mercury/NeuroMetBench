# NeuroMetBench v2.1.2 reproducibility release

NeuroMetBench is a patient-aware evidence-bounding methodology for evaluating transcript-derived metabolic representations without allowing evidence on one axis to compensate for failure, non-admission, or absence on another.

This release accompanies the manuscript:

**NeuroMetBench: Patient-aware evidence bounds for transcript-derived metabolic representations across cancer proteogenomic contexts**

Target article type: Methodology, *Functional & Integrative Genomics*.

## What v2.1.2 adds

Version 2.1.2 extends, rather than rewrites, the v2.1.1 evidence state. It adds four post-result revision-stage evidence modules with fixed, machine-verifiable authorities:

- exhaustive patient-influence stress tests for the LSCC and CNS/HGG primary RNA-protein endpoints and their cross-cohort attenuation;
- paired pathway-specificity and structured-missingness sensitivities, with LSCC specificity supported only as exploratory/post-outcome evidence and CNS specificity replication not supported;
- an internally preanalysis-frozen same-cohort measured-metabolomics sensitivity in 75 Wang/CPTAC GBM patients, where the transcript-derived serine score shows weak and uncertain association with measured L-serine;
- a recovered historical METAFlux reaction-identity and cryptographic artifact-integrity firewall that complements, but does not replace, the historical primal-feasibility audit.

These additions preserve adverse evidence. They do not retroactively create prospective validation, measured flux, solver optimality/KKT certificates, universal pathway specificity, clinical validity, or broad framework calibration.

## Package contents

- exact manuscript, Supplementary Information, and prospective reuse-template sources and PDFs under `article/`;
- manuscript figures in PNG and EPS formats;
- `online_resources/ESM_2.zip`, containing inherited v2.1.1 authorities plus the v2.1.2 revision-stage authorities, executable verifiers, the `neurometbench-ref` 1.0.2 helper software, recovered historical numerical artifacts, and a narrowly scoped third-party ODbL input subset required for offline reproduction of the measured-metabolomics sensitivity;
- the exact immutable public v2.0.7 archive under `historical/`;
- manuscript-to-evidence and cross-package identity maps;
- closed-world SHA-256 verification for the outer release.

## Principal scientific boundaries

The principal external endpoint remains same-gene RNA-protein rank concordance. It is not measured metabolic flux. The new orthogonal metabolomics sensitivity makes that distinction empirically sharper: despite strong RNA-protein concordance, RNA BSL02 versus measured L-serine in 75 Wang/CPTAC GBM patients is weak and uncertain (Spearman rho=0.15343471285861396; 95% patient-bootstrap interval -0.08031096546314256 to 0.37371682988386595; 100,000-permutation p=0.1852581474185258).

The frozen three-gene serine aggregate still does not demonstrate superiority over PSAT1 alone. Broad and supported-domain calibration remain not earned. Three of 33 matched development-to-LSCC transport effects reverse sign. Historical reaction-order swaps remain undetected by primal feasibility alone. The new artifact-integrity firewall detects identity corruption after outputs are frozen, but does not establish historical solver optimality, dual feasibility, KKT consistency, or biological validity.

## Reusable software

`neurometbench-ref` remains version 1.0.2. It provides patient-aware aggregation, multiplicity utilities, coverage checks, artifact-use firewalls, numerical compatibility checks, and regression fixtures. It is not a universal automated implementation of every NeuroMetBench adjudication decision.

## Verification

From the extracted release root, run:

```bash
python reproducibility/verify_outer_release.py
```

For the deeper chain, run:

```bash
python reproducibility/verify_everything.py
```

Online Resource 2 contains its own scientific, provenance, software, and v2.1.2 revision-stage verifiers.

## Data and licensing

The root MIT license applies only to NeuroMetBench-authored material for which the author can grant that license. Most third-party raw molecular matrices are not redistributed. Version 2.1.2 includes only the minimal cBioPortal/Wang-CPTAC rows necessary to reproduce the new orthogonal metabolomics sensitivity offline; those rows remain governed by the cBioPortal DataHub ODbL 1.0 terms and are isolated under `third_party_data/` inside Online Resource 2. See `LICENSE_SCOPE.md` and `THIRD_PARTY_NOTICES.md`.

Stable Zenodo concept DOI: `10.5281/zenodo.21830887`.

Immutable Zenodo version DOI: `10.5281/zenodo.22147971`.
