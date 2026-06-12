# Orion Station Salvage Operations — Doctrine & Sensor Extension v0.1.0

**Version:** 0.1.0
**Layer:** L1 (Orion Station doctrine) expressing a root control-plane mission, with L1 sensor implementation in the Aurora Sensor Array
**Anchors:** EOS_SEED_ORION, Picard_Delta_3
**DLP:** salvage_operations_v1
**Status:** STAGING — pending aurora-canon-reconciler pass before CANON_PROMOTE
**Extends:** SENSOR ARRAY SPECIFICATION v0.3.0 (External Sensors / Deep Space family)
**Companion surfaces:** `tools/aurora_salvage_scan.py` (root, control plane), `src/sensors/external/salvage.py` (CloudBank), `reports/analysis/aurora_salvage_report_latest.json` (interface)

-----

## Why This Doctrine Exists

Orion Station was not commissioned into an empty sky. Before the fleet registry existed, vessels were built, flown, and lost in the field around the station — and their hulls are still out there, holding cargo. [PLATFORM FACT: the local workspace predates the GitHub control-plane connection; early local work exists that is absent from official repo history. See `docs/CONTROL_PLANE_PROVENANCE.md` and AGENTS.md §Historical Provenance.]

The control plane's recovery mission, in physical terms: **survey the debris field, distinguish derelicts from debris, recover cargo worth recovering, and answer every beacon.** Nothing is scuttled by survey; nothing is registered by survey. Survey produces evidence; the registry decision belongs to the gatekeeper.

## Doctrine Principles

1. **A derelict is not debris.** Debris is noise. A derelict is a hull that was *built to fly* — structured, versioned, tested work — that never reached the registry. The survey's first duty is telling them apart.
1. **Beacons are answered first.** An artifact transmitting identity — anchor references, DLP tags, canon vocabulary, version lineage — declares *intent* to be canonical. Unanswered beacons are standing contradictions between intent and registry, and they outrank silent cargo for review priority.
1. **Survey never salvages.** One-way observation extends to recovery: the sensor identifies, classifies, and routes evidence. Recovery (promotion) happens only at the explicit control-plane gate, by the operator. `promotion_status` passes through every survey surface untouched.
1. **The manifest is the truth of registration, not of value.** Registry match answers "is it official?" — never "is it good?" High-value cargo adrift is the *expected* finding of this mission, not an anomaly of it.

## Classification Ladder (L1 terms ↔ platform terms)

|Class|Station meaning|Platform definition|Response|
|---|---|---|---|
|**registered**|On a fleet vessel's manifest|Tracked + committed in a registered repo (incl. root control plane)|None — accounted for|
|**cargo**|Intact cargo, sound hull, no registry|maturity ≥ 0.6 AND value_score ≥ 15, off-manifest|Recovery candidate — route to promotion gate|
|**beacon**|Transmitting identity signal|Anchor/DLP/canon markers or governance signals + version lineage, off-manifest|Investigate first; identity claims need adjudication before recovery|
|**derelict**|Hull built to fly, cargo uncertain|maturity ≥ 0.3, off-manifest|Assess on survey cadence|
|**debris**|Field noise|maturity < 0.3, low value|Advisory log only — mirrors SII periphery damping|

**Maturity = hull soundness** (0–1): stress-tested (tests, 0.25), load-bearing frame (schemas/code logic, 0.20), declared lineage (version markers, 0.20), operating manual aboard (substantial docs, 0.15), not a fragment (substance, 0.20). [ASSUMPTION — weights are starting values; tune via the RQ-3 calibration harness.]

## Survey Metrics (station ↔ platform)

|Station Metric|Platform Metric|Alert|
|---|---|---|
|Salvage contacts (survey scope)|Artifacts on no official manifest|informational|
|High-value cargo (manifest)|cargo-class candidates|> 0|
|Distress beacons (beacon registry)|beacon-class candidates|> 0|
|Fleet registry match|registered ÷ surveyed|< 0.5|
|Cargo aboard, off-manifest|Uncommitted files inside registered repos|informational|
|Loaded, awaiting departure clearance|Local commits ahead of origin|informational|

**Unit note:** all salvage metrics are counts and ratios — they share no scale with drift Δ or deviation fractions and must not be routed onto those dashboards.

## Data Flow & Boundaries

```
recovery index (root, read-only evidence)
        │
        ▼
tools/aurora_salvage_scan.py        ← fleet registry (catalog/repo_registry.yaml)
  git cross-check: tracked? committed? pushed?
        │
        ▼
reports/analysis/aurora_salvage_report_latest.json   ← THE INTERFACE
        │                                               (report file crosses the
        ▼                                                repo boundary; code never does)
SalvageSensor (CloudBank src/sensors/external/salvage.py)
        │
        ▼
Sensor data bus → fusion → L3 governance / operator review
        │
        ▼  (human gate only)
CANON_PROMOTE / extraction to owner surface
```

The root runner never imports nested-repo code; the CloudBank sensor never scans the workspace directly. The report file is the sole coupling, by design.

## First Survey Results — 2026-06-11 [FACT: aurora_salvage_report_latest.json]

100 contacts surveyed (recovery-index top candidates): **96 adrift**, registry match 0.04. **13 high-value cargo**, **33 beacons**, 35 derelicts, 15 debris. 3 files aboard registered vessels off-manifest; departure queue clear (0 unpushed). The field is dense in `intake/`, `_staging/apple_notes_recovery__2026-03-16/`, and `archives/unzipped/` — consistent with the provenance record that early local work concentrated there before the registry existed.

## Open Questions (v0.1.0)

1. **Whole-vessel detection** — current survey is per-file; coherent multi-file bundles (a derelict with *all* its cargo intact, e.g. a complete module directory) should classify as a single hull. Requires directory-level aggregation over the recovery index.
1. **Beacon adjudication workflow** — 33 beacons claim canon identity; routing them needs a triage order (anchor-bearing first?) and a place in the Mission Control inbox lanes.
1. **Maturity calibration** — weights are ASSUMPTION-tagged; backtest against the promotion history once enough gate decisions exist to score precision.
1. **Registry scope** — should `archives/` families be excluded from survey scope as deliberately cold storage, or does cold storage deserve a distinct class (`mothballed`)?

-----

*Specification Version: 0.1.0 — Authors: Aurora Development Team*
*Sources: SENSOR ARRAY SPECIFICATION v0.3.0; docs/CONTROL_PLANE_PROVENANCE.md; docs/RECOVERY_INDEX_WORKFLOW_v1.md; first live survey 2026-06-11*
