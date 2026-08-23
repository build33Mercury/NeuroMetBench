# Release notes

## 2.0.7

Repository-and-publication synchronization correction. Frozen biological endpoints, cohorts, thresholds, canonical intervals, statistical results, adverse results, and interpretation ceilings are unchanged. Public v2.0.6 remains immutable historical evidence.

- repairs the public-repository divergence discovered after v2.0.6 publication: the v2.0.6 GitHub tag still exposed v2.0.4 README, `CITATION.cff`, `.zenodo.json`, release-note, license-scope, changelog, and repository-checksum metadata;
- advances only the article/reproducibility package identity to 2.0.7; the reusable `neurometbench-ref` software remains version 1.0.1;
- adds exact release-critical repository metadata templates plus `audit/repository_sync_manifest.csv`, allowing the eventual GitHub v2.0.7 tag to be checked byte-for-byte against the frozen package before journal submission;
- strengthens registry verification so a current release cannot pass while release-critical repository metadata identifies another package version;
- updates the literature boundary through 23 August 2026 and adds the 12 August 2026 peer-reviewed FEBS Journal study on single-cell metabolic mRNA insufficiency as adjacent evidence for transcript-to-metabolism interpretation limits;
- narrows CNS wording so patient-identifier disjointness is not presented as institution-, platform-, or ecosystem-independent validation;
- aligns the CNS claim-traceability anchor/evidence class and corrects the spatial verification log to report 8/12 genes covered rather than the obsolete misleading label;
- rebuilds manuscript, supplement, Online Resource 2, manifests, checksums, compiled PDFs, and exact submission/reproducibility identities from the synchronized bytes.

No biological endpoint, cohort, threshold, canonical interval, statistical result, or interpretation ceiling is changed by 2.0.7.

## 2.0.6

Post-publication corrective release. Frozen biological endpoints, cohorts, thresholds, statistical results, adverse results, and interpretation ceilings are unchanged. Public v2.0.5 remains immutable historical evidence.

- corrects a stale v2.0.5 repository-tag identity discovered after publication: the v2.0.5 tag did not contain the v2.0.5 package tree even though a v2.0.5 release was created;
- removes the remaining mutable phrase `public publication remains pending` from the immutable manuscript claim-traceability authority and strengthens automated detection of equivalent pending-publication wording;
- advances article-package and reproducibility-package identity to 2.0.6 without changing the reusable `neurometbench-ref` software identity 1.0.1;
- removes redundant final Python stream flush calls immediately before forced clean stage exit, then re-stress-tests the aggregate verifier under repeated fresh extraction;
- hardens the one-command verifier after exact-archive stress testing: a clean coordinator launches one bounded 19-check science/provenance worker and one bounded read-only figure-reconstruction worker as sibling processes; both must validate their original per-check PASS markers and exit 0 before the coordinator emits aggregate 20/20 PASS, and the exact 20 checks are unchanged;
- rebuilds Online Resource 2, all manifests, checksums, article sources, compiled PDFs, and cross-package identities from the corrected bytes;
- preserves v2.0.5 and every earlier public release without retagging, overwriting, or rewriting history.
- removes historical development ZIP payloads containing non-scientific local workflow residue from the v2.0.6 public archive while retaining exact identity/status manifests and the Phase-12 authority crosswalk;
- normalizes submitted PNG figures from fully opaque RGBA to 8-bit RGB without changing visible pixels;
- repairs title-page corresponding-author identification, Fig. 1/Table 1 in-text citations, retrospective chronology wording, spatial coverage field semantics, and current 2026 glioma spatial-omics prior-art coverage;

No biological endpoint, cohort, threshold, canonical interval, statistical result, or interpretation ceiling is changed by 2.0.6.

## 2.0.5

Reviewer-driven corrective archive and reproducibility release. Frozen biological endpoints, cohorts, thresholds, statistical results, adverse results, and interpretation ceilings are unchanged. The published v2.0.4 release remains immutable.

- removes mutable live-publication assertions from machine-readable archive authorities and delegates live release state to a detached receipt;
- uses two bounded process-isolated verification stages, one for complete figure reconstruction and one fresh process for the remaining scientific/provenance checks, while preserving the exact 20-check set and requiring real zero exit codes;
- makes figure verification read-only with respect to the distributed archive by regenerating into external temporary directories;
- adds deliberate interruption testing that requires the archive tree to remain byte-identical;
- changes the 10,000-resample percentile-bootstrap implementation to bounded chunks while preserving every bootstrap value, canonical quantiles, and all 21 reference figure bytes in the reference environment;
- adds `THIRD_PARTY_NOTICES.md` for the small scCellFie, scMetabolism, and Compass source-identity fragments embedded inside one historical provenance package, including source/version/commit availability, governing-license boundary, and non-relicensing language;
- clarifies that CNS patient-identifier disjointness does not establish independence of institution, platform, acquisition ecosystem, or all upstream processing choices;
- states the retrospective research question explicitly without implying preregistration or prospective prespecification;
- corrects alphabetical ordering of the two Liu Y references.

## 2.0.4

Post-audit publication-identity and reproducibility-hardening repair. Frozen canonical scientific results are unchanged from v2.0.3.

- retains the already-published v2.0.3 release unchanged and advances the current article package to a new immutable version rather than rewriting history;
- carries the final patient-aware benchmarking title and the completed 2026 prior-art boundary, including the non-peer-reviewed SynTrustBench comparison and peer-reviewed evidence-admissibility precedent;
- preserves the recovered 25-artifact historical identity/status record while omitting development ZIP payloads containing non-scientific local workflow residue, and preserves the 20-check aggregate verification suite;
- makes parser-independent hexadecimal float64 authorities canonical for exact primary resampling verification;
- hardens the one-command verifier for reliable fresh-extraction execution and keeps all 21 generated PNG/SVG/EPS figure bytes unchanged;
- preserves every frozen positive, adverse, unsupported, non-admitted, and technical-failure result;
- updates article, Online Resource 2, checksum, citation, Zenodo, and public-release identities to v2.0.4.

No biological endpoint, cohort, threshold, canonical interval, statistical result, or interpretation ceiling was changed to obtain this release.

## 2.0.3

Derived-results verification, provenance, and submission-integrity repair. Frozen canonical scientific results are unchanged.

- reframed the work as a retrospective case study and removed claims of general framework validation;
- synchronized the exact submitted manuscript, supplementary source, and Online Resource 2 identities;
- corrected LSCC accounting so 115 to 110 to 91 to 89 is the ordered proteomic path and 108 of 110 is a parallel GDC branch;
- made the 34-row dependence-aware family primary and retained the inherited 39-row family as a provenance sensitivity;
- added deterministic retrospective BCa interval sensitivity without changing the canonical percentile intervals;
- expanded current prior-art, validation-scope, evidence-ceiling, same-gene endpoint, and historical-pipeline recovery and remaining raw-source/environment boundary disclosures;
- replaced the impossible embedded outer-archive hash design with an internal cross-package manifest and detached publication receipt;
- retained every adverse result and frozen threshold.
- Final clean-room hardening vectorizes the frozen-seed primary bootstrap calculation inside figure generation; exact CI values and all 21 PNG/SVG/EPS figure bytes are unchanged, while the reference verification run is substantially faster and less resource-sensitive.

This package verifies supplied derived authorities and preserves a hash-locked 25-artifact historical identity/status record tied to the Phase-12 result lock. It does not redistribute third-party raw molecular matrices or guarantee contemporary raw-to-final execution across changed source repositories, historical environments, dependencies, or external licenses. Historical releases are not rewritten or retagged. Version 2.0.3 is retained immutable; v2.0.7 is the current corrective article package.

## 2.0.2

Claim-traceability, cohort-accounting, comparator-provenance, accessibility, and release-metadata repair. Superseded by 2.0.7 for the current article.

## 2.0.1

Primary-statistics parser correction and exact software provenance. Superseded by 2.0.7 for the current article.
