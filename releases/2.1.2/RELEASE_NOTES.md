# NeuroMetBench v2.1.2

Immutable Zenodo version DOI: `10.5281/zenodo.22147971`.

Version 2.1.2 is a scientific/reproducibility extension of v2.1.1 derived from a fresh post-result methodological audit. It preserves v2.1.1 as an immutable historical public state and adds both favorable and unfavorable revision-stage evidence without retuning thresholds or replacing adverse results.

## New revision-stage evidence

### Patient influence and attenuation robustness

- LSCC full rho remains 0.9070558388598963; exhaustive leave-two-patient values range from 0.9006831055648825 to 0.9251917372732197.
- CNS/HGG full rho remains 0.6266145829894963; exhaustive leave-two-patient values range from 0.6017393219779715 to 0.6869264642192787.
- The LSCC-minus-CNS/HGG attenuation remains positive after every single-patient deletion and every one-LSCC-plus-one-CNS deletion tested; the smallest latter delta is 0.2421057127942533.

### Pathway specificity and missingness

- In LSCC, the frozen serine-de-novo endpoint exceeds serine transport, glycolysis, TCA, and OXPHOS under paired 100,000-patient bootstraps; all four 95% intervals remain above zero and all four exploratory contrasts remain supported under a conservative four-test Holm sensitivity.
- In CNS/HGG, all four contrasts are directionally positive but their uncertainty intervals include zero and none survives the same four-test Holm sensitivity; specificity replication is therefore not claimed.
- Restricted TCA/OXPHOS-evaluable subsets retain strong primary serine RNA-protein concordance.

### Orthogonal measured metabolomics

An internally dated preanalysis contract froze L-serine as the sole primary metabolite before association inspection. In 75 Wang/CPTAC GBM patients:

- RNA BSL02 vs measured L-serine: rho=0.15343471285861396; 95% bootstrap interval -0.08031096546314256 to 0.37371682988386595; 100,000-permutation p=0.1852581474185258.
- Protein BSL02 vs measured L-serine: rho=0.20186070363850933; interval -0.038820130120841546 to 0.4299262938217029; p=0.08206917930820692.
- RNA BSL02 vs glycine is essentially null.
- RNA BSL02 vs 3-phosphoglycerate is negative with nominal p=0.04060959390406096 but does not survive the fixed two-test Holm family (adjusted p=0.08121918780812191).

These results do not earn measured-metabolite, flux, causal, or clinical validation. They strengthen the empirical rationale for claim bounding.

### Historical numerical-integrity recovery

The successful historical Phase-10 execution artifact and original full METAFlux matrices were recovered. The record confirms that historical solver status, objective values, dual variables, and KKT receipts were not preserved and that reaction-order swaps were detected in 0/113 units by the primal-feasibility check. Version 2.1.2 adds a separate reaction-identity and cryptographic artifact-integrity firewall over the recovered frozen outputs. This detects post-freeze identity/value corruption but does not retroactively establish solver optimality or comprehensive numerical validity.

## Reproducibility changes

- Article claim-evidence ledger expanded from 18 to 21 claims, including explicit unsupported states for measured-L-serine validation and CNS specificity replication.
- Online Resource 2 closed world contains 183 hash-bound files (excluding its checksum file itself).
- Four new executable v2.1.2 verifier modules added.
- Minimal cBioPortal/Wang-CPTAC input rows required for offline metabolomics reproduction are isolated under ODbL 1.0 with attribution and are not covered by the root MIT license.

## Preserved adverse conclusions

No previously frozen principal estimate or adverse conclusion was altered to create v2.1.2. Aggregation superiority over PSAT1 remains unsupported; broad and supported-domain calibration remain not earned; transport sign reversals remain; the historical primal-feasibility reaction-order blind spot remains; and no universal automated adjudication, measured flux, clinical utility, or universal validation claim is made.
