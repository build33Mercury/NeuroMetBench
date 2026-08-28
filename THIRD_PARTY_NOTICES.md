# Third-party notices

The MIT license at the root of this release applies only to NeuroMetBench-authored material for which the author can grant that license. It does not relicense third-party material. Original upstream terms control.

## cBioPortal / Wang-CPTAC GBM subset added in v2.1.2

Online Resource 2 contains a minimal third-party input subset derived from the public cBioPortal DataHub study `gbm_cptac_2021`, used to reproduce the internally preanalysis-frozen orthogonal measured-metabolomics sensitivity. cBioPortal documents the study as derived from Wang et al. 2021 supplementary Table S2, including mRNA, normalized proteome, and normalized metabolome assays. The DataHub study license states ODC Open Database License (ODbL) 1.0 terms.

Only the exact rows required by the frozen analysis are included: PHGDH, PSAT1, and PSPH for RNA and protein, plus L-serine, glycine, and 3-phosphoglycerate for metabolomics. They are isolated under `third_party_data/cbioportal_gbm_cptac_2021/` inside Online Resource 2 together with attribution/license provenance. They are **not** covered by NeuroMetBench's MIT license.

Upstream study: Wang et al. 2021, integrated proteogenomic characterization of glioblastoma. The package records the exact acquisition URLs and full-source SHA-256 receipts used for extraction.

## Historical third-party provenance

The embedded immutable v2.0.7 historical archive contains provenance records for three small third-party-origin fragments present in historical development packages associated with scCellFie, scMetabolism, and Compass. Those historical development ZIP payloads are not redistributed by the historical archive or by v2.1.2; identities and license observations are retained as provenance only.

- scCellFie: upstream `earmingol/scCellFie`; historical version 0.6.2; MIT license observed at the recorded commit.
- scMetabolism: historical fragment metadata reported GPL-3 while the upstream repository license observed during the historical audit was BSD-3-Clause. NeuroMetBench does not resolve that upstream discrepancy and does not redistribute the fragment.
- Compass: historical version 1.0.0; BSD-3-Clause license observed. Compass was not executed in the external family because the required external solver license was unavailable.

Full source-specific provenance is retained in Online Resource 2 and the embedded v2.0.7 archive.
