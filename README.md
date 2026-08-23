# NeuroMetBench derived-results verification and provenance package

Version 2.0.7

Article: *NeuroMetBench: Patient-aware benchmarking reveals interpretation limits of transcript-derived metabolic representations in glioma*

Author: Abdsalam Bitar, Independent Researcher, Amman, Jordan. ORCID: 0009-0009-9517-636X.

## Scope

This archive accompanies a retrospective case study. It verifies supplied patient-level derived authorities, statistical summaries, multiplicity results, claim traceability, cohort accounting, figure generation, and named adverse findings. It also preserves a hash-locked identity/status record for 25 exact historical project artifacts: 12 source or runner-package identities, 12 corresponding result-authority identities recognized by the Phase-12 result lock, and the Phase-12 lock identity. The development ZIP payloads are omitted from v2.0.7 public distribution because they contain non-scientific local workflow residue; exact predecessor byte identities remain preserved. Raw third-party molecular matrices are not redistributed; contemporary raw-to-final execution remains conditional on source availability, historical environments and dependencies, and applicable external licenses.

The package preserves the frozen biological endpoints, cohorts, thresholds, canonical percentile intervals, statistical results, and adverse results inherited from v2.0.0. The public v2.0.6 release is retained immutable as the immediate historical predecessor. Version 2.0.7 is a corrective synchronization release created after a post-publication audit found that the v2.0.6 GitHub tag still exposed stale v2.0.4 repository metadata. Live publication state is not asserted inside this immutable archive. Version 2.0.7 contains:

- the exact submitted manuscript and supplementary LaTeX sources under `article/`;
- an exact copy of Online Resource 2 as `online_resource_2.zip`, bound by `cross_package_identity.csv`;
- corrected LSCC flow semantics: the ordered proteomic path is 115 to 110 to 91 to 89, while 108 of 110 is a parallel GDC-eligibility branch;
- dependence-aware multiplicity reporting with the 34-row deduplicated family primary and the 39-row inherited family retained as a provenance sensitivity;
- deterministic retrospective BCa interval sensitivity while leaving the canonical percentile intervals unchanged;
- explicit prior-art, validation-scope, data-access, claim-ceiling, and non-admission boundaries;
- deterministic verifiers for scientific results, exact resampling, registries, traceability, numerical sensitivity, scenario summaries, cohort reconstruction, internal identities, figures, and the historical identity/status record;
- a repository synchronization manifest and exact release-critical GitHub metadata templates so the public tag can be checked against the frozen archive before submission.
- a recovered 25-artifact historical identity/status record with SHA-256, Phase-12-authority, and adverse-status verification; development ZIP payloads are not bundled in v2.0.7.

The article and package are version 2.0.7. The reusable `neurometbench-ref` software component remains version 1.0.1. These identities are not interchangeable.

## Frozen results and adverse findings

- LSCC development-unused internal stress test: n=89, serine-de-novo Spearman rho=0.9070558388598963, zero exceedances in 100,000 permutations, reported Monte Carlo floor p=1/100001, canonical patient-bootstrap percentile 95% CI [0.8496172720469373, 0.9387662754309077], and retrospective BCa sensitivity [0.8549569717100521, 0.9419991215859146].
- CNS/high-grade-glioma external case study: n=90, rho=0.6266145829894963, zero exceedances in 100,000 permutations, reported Monte Carlo floor p=1/100001, canonical percentile 95% CI [0.4696652580556697, 0.7506606861648679], and retrospective BCa sensitivity [0.4593163084727422, 0.7440560575519283].
- Dependence-aware external family: 32/34 BH-supported and 26/34 BY-supported. The inherited 39-row family gives 37/39 BH-supported and 30/39 BY-supported and is retained as a provenance sensitivity.
- Development-to-LSCC transport: 33 matched cells, 30 sign-retained, three reversed, and effect-rank stability rho=0.6424749163879598.
- Broad calibration was not earned. Supported-scenario power was 0.48705882352941177. The stylized simulation used a Pearson/t/Fisher-z proxy rather than the empirical Spearman/permutation/bootstrap engine.
- METAFlux numerical sensitivity: 113/113 archived vectors pass the project-defined 1e-3 compatibility threshold, 112/113 at 1e-4, and 0/113 at 1e-5 or tighter tested tolerances. Reaction-order swaps remain undetected in 0/113 units.
- The spatial module is structurally non-admitted under the frozen coverage rule. Three-gene serine aggregation did not outperform PSAT1.

## Verification

Follow `reproducibility/CLEAN_ROOM_INSTRUCTIONS.md` in a clean environment, then run:

```bash
python reproducibility/verify_everything.py
```

The command verifies the derived package and the recovered historical project record. It does not redistribute third-party raw molecular matrices or guarantee contemporary raw-to-final execution across changed source repositories, environments, dependencies, or external licenses.

## Interpretation boundaries

Supported statements are limited to the named case-study associations, task-specific transport observations, explicit non-admission states, the stylized simulation summary, and the named numerical compatibility test. The evidence does not establish measured metabolic flux, universal method superiority, public preregistration, a prospective external holdout, independent biochemical validation, full calibration, GBM-only replication, solver optimality, comprehensive numerical validation, or a generally validated benchmarking framework. The same-gene RNA-protein comparison is cross-modal but not an orthogonal biochemical endpoint.

## Data and rights

Third-party raw molecular matrices are not redistributed. `scientific_authority/data_access_provenance_ledger.csv` records accessions, persistent routes, access class, identity strength, rights, redistribution status, and not-used boundaries. `LICENSE_SCOPE.md` and `THIRD_PARTY_NOTICES.md` state the licensing boundary and identify historical third-party-origin fragment provenance explicitly. The repository MIT license applies only to NeuroMetBench-authored code and documentation for which the author can grant that license; it does not relicense source datasets, dependencies, source-study materials, or differently governed content preserved inside historical provenance packages.

## Publication identity boundary

- Archive release identifier: `2.0.7`
- Stable Zenodo concept DOI: `10.5281/zenodo.21830887`
- Repository: `https://github.com/build33Mercury/NeuroMetBench`
- Live publication state, exact version DOI, release URLs, outer archive size, and outer SHA-256 are intentionally not asserted inside this immutable archive.
- After publication and independent public download verification, those live facts are recorded only in a detached `publication_receipt.txt` distributed beside the archive.

The outer archive cannot contain its own final hash without changing the bytes being identified. Internal identities are recorded in `SHA256SUMS.txt`; article/Online Resource identities are recorded in `cross_package_identity.csv`; the exact 22-file journal package is bound by `audit/final_submission_identity.csv` and can be checked with `reproducibility/verify_submission_identity.py`; public release-state identity is detached.
