# NeuroMetBench v2.1.1

Version 2.1.1 is a corrective reproducibility and manuscript-synchronization release. It supersedes v2.1.0 as the current scientific package while preserving all prior public versions as immutable historical states.

## Changes from v2.1.0

- Adds a machine-readable current article claim-evidence ledger, study-specific state-assignment specification, and consistency verifier.
- Clarifies that BSL02 bootstrap intervals characterize patient-resampling uncertainty conditional on frozen cohort-relative score construction and do not propagate re-estimation of percentile transforms within each bootstrap replicate.
- Reframes cross-cohort wording to refer to the same frozen three-gene serine scoring rule rather than implying numerically identical cohort-relative scores.
- Updates `neurometbench-ref` from 1.0.1 to 1.0.2 with validation-only corrections to claim lookup and invalid-input handling, additional edge-case tests, and source-excluded wheel verification.
- Strengthens closed-world checksum verification and package provenance.
- Embeds the exact immutable public v2.0.7 archive to make the historical provenance chain physically auditable from the current release.
- Synchronizes manuscript, supplementary material, figures, Online Resource 2, software, and cross-package identities.

## Frozen public release asset

`NeuroMetBench_v2.1.1_reproducibility_release.zip`

- Size: 36,623,018 bytes
- SHA-256: `beb2a2e53c45bb141f03c30cf8097b33372d454dba86f542253b5a1dcb3f732f`

## Scientific results

No frozen article-level scientific estimate, cohort definition, adverse result, multiplicity family, simulation outcome, numerical conclusion, or claim ceiling was changed to obtain v2.1.1.

Principal frozen values include:

- LSCC serine: n=89, Spearman rho=0.9070558388598963.
- CNS/high-grade-glioma serine: n=90, Spearman rho=0.6266145829894963.
- Exploratory cross-cohort delta rho=0.2804412558703999; 100,000-resample percentile interval 0.1426761482234506 to 0.438036759223711.
- Three-gene aggregation does not demonstrate superiority over PSAT1 alone.
- Three of 33 matched development-to-LSCC effects reverse sign.
- Broad and supported-domain calibration remain not earned.
- Reaction-order swaps remain undetected by the tested primal-feasibility check.
