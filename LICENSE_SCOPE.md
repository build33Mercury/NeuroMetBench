# License scope

The MIT `LICENSE` at the root of this release applies only to NeuroMetBench-authored software and documentation for which the author has authority to grant that license.

It does not relicense third-party datasets, source-study material, external software dependencies, repository-hosted molecular matrices, or other third-party content. Those materials remain governed by their original licenses, repository terms, data-use conditions, or access controls.

Version 2.1.2 contains one deliberately narrow redistribution exception to the general raw-data exclusion: Online Resource 2 includes only the minimum cBioPortal DataHub `gbm_cptac_2021` rows needed to reproduce the internally preanalysis-frozen measured-metabolomics sensitivity offline (PHGDH/PSAT1/PSPH RNA rows, PHGDH/PSAT1/PSPH protein rows, and the three prespecified metabolite rows). These files are isolated under `third_party_data/cbioportal_gbm_cptac_2021/`, retain source attribution and license text, and are governed by the cBioPortal DataHub ODC Open Database License (ODbL) 1.0 rather than MIT.

All other source-governed molecular matrices remain represented by provenance/access records or compact NeuroMetBench-derived authorities rather than being relicensed. Source-specific access, rights, identity strength, and redistribution boundaries are recorded in Online Resource 2 and in the embedded immutable historical archive.

The embedded v2.0.7 archive preserves the historical identity/status manifest and related provenance without rewriting the frozen historical state. It does not broaden any rights originally applicable to source-governed materials.

`THIRD_PARTY_NOTICES.md` summarizes the relevant third-party provenance and redistribution boundaries. When a file contains only NeuroMetBench-authored code or documentation, the repository MIT license applies. When rights are mixed or source-governed, the narrower original terms control for the affected material.
