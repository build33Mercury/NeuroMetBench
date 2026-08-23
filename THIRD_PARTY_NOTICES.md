# Third-party notices

The MIT license at the root of this release applies only to NeuroMetBench-authored material for which the author can grant that license. It does not relicense third-party material. Original upstream terms control.

A historical NeuroMetBench source-identity package contained three small third-party-origin fragments associated with scCellFie, scMetabolism, and Compass. Version 2.0.7 does not redistribute that development ZIP or those fragments. The exact historical package and fragment identities are retained as provenance; the governing license observations below document the redistribution boundary. Full license texts are retained in `third_party_licenses/` as provenance notices, not as a claim that third-party source payloads are bundled.

## scCellFie

- Historical fragment: `frozen_source/ACT06_sccellfie_init.py`
- Purpose: version and source-API identity receipt
- Upstream source: `https://github.com/earmingol/scCellFie`
- Historical version: 0.6.2
- Historical exact commit: `bad8ea9afcd898c8633dac7d3ab1f83dc086b9b1`
- Fragment SHA-256: `62b2aa99dc38281c3459ae551e0d044a5abfcec3ef0926386139372fa4a2c338`
- License observed at that exact commit: MIT

## scMetabolism

- Historical fragment: `frozen_source/ACT07_DESCRIPTION`
- Purpose: package-version and dependency identity receipt
- Historical version: 0.2.1
- Fragment SHA-256: `9338adbac172ef95792814ef9f98663e8fac57f29a1053acc70e1377beefb225`
- Historical fragment declaration: GPL-3
- Upstream repository LICENSE observed during the 2026-08-23 audit: BSD-3-Clause
- Boundary: the upstream signals conflict, so NeuroMetBench does not resolve the discrepancy on the upstream authors' behalf and does not redistribute the fragment in v2.0.7.

## Compass

- Historical fragment: `frozen_source/FLX02_compass_version.py`
- Purpose: package-version identity receipt; Compass was not executed in the external family because the required solver license was unavailable
- Historical version: 1.0.0
- Fragment SHA-256: `dcd3a342a543cf2d93a0ec44cd7731cd22f058ed5125475c46326359e4946cbd`
- Upstream license observed during the audit: BSD-3-Clause

Version 2.0.7 preserves these provenance facts without redistributing the historical third-party fragments and without granting rights beyond applicable upstream terms.
