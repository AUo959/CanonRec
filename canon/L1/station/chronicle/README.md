# Station Chronicle — Persistent History of Orion Station

**Ledger:** `STATION_CHRONICLE.ndjson` (`station-chronicle-v1`)
**Built by:** root `tools/station_chronicle.py build` (deterministic reconstruction)

Everything that has happened aboard the station, as immutable event atoms —
the L2 GUMAS event-ledger pattern (event atoms, payload hashes, run anchors
from `DETERMINISTIC_EVENT_RECONSTRUCTION_SPEC`) applied to L1 under the
Architecture Contract: **state deltas never overwrite L1 facts; promotion
is gated.**

## Tiers

| Tier | Meaning | Home |
|---|---|---|
| CANON | Reconstructed from canon sources: the March 2026 mesh era transcripts (Captain-era identifiers preserved verbatim per `../PILOT_ROLE_DEFINITION.md`), CanonRec drift entries | this ledger |
| OPERATIONAL | Real station operations: the 2026-06-11 activation pulse `#808//.`, companion roll calls, flight log | this ledger |
| STAGING | Simulated hours aboard (`tools/hour_aboard.py` runs) — candidate canon, promotion-gated | root `catalog/station_chronicle_staging.ndjson` + derived live |

## How history becomes behavior

`tools/station_chronicle.py state` derives `catalog/station_state.json`
from all tiers: pair familiarity (co-work hours + emergent syncs), crew
completions, per-scenario task memory. `tools/hour_aboard.py` loads that
state before every run — crew who worked together in past hours enter the
next hour as collaborators, raising real collaboration-boost odds. Past
actions influence current behavior persistently, while the chronicle's
CANON tier remains append-only and owner-gated.

## Span at first reconstruction (2026-06-13)

2026-03-06 → 2026-06-13: the station's first live days on the mesh, the
June reactivation, all flights, and the first simulated watch blocks.
