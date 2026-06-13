---
entity_id: "ORION.STATION.PURPOSE"
entity_type: "definition"
layer: "L1"
name: "Station Purpose — Orion Station (ORH-07)"
certainty: "CANON"
registry_authority: "owner_ruling"
ruled_at: "2026-06-13"
doc_sources:
  - "Owner definitional ruling (the Pilot), 2026-06-13"
  - "ORION__CANON__ORION_STATION_ENVIRONMENT__v2.0__2026-04-08.md (role: simulation-oriented station environment)"
  - "ORION__ARCHITECTURE_CONTRACT__L1_L2_L3__v1.0.md"
---

# Station Purpose — Orion Station (ORH-07)

**Owner canonical ruling (2026-06-13):**

> Orion Station exists to run high-fidelity galactic simulations — so
> advanced that the facility is operated at a Lagrange point in space.
> The whole station is a chassis around L2.

## What this means architecturally

- **L1 is the chassis.** The station — ring, core, crew, dispatch, life
  support — is the operational facility that hosts and sustains the engine.
  Crew operations are, ultimately, engine operations: power, cooling,
  coherence, custody, watch discipline.
- **L2 is the payload.** The GUMAS galactic simulation is the station's
  reason for existence. The 240-step simulation reference day already in
  canon is the engine clock the station's 22.1-hour day serves.
- **L3 is the law.** THREADCORE/Picard Delta 3 governs what the engine may
  do and what crosses layer boundaries (state deltas, never fact
  overwrites).

This inverts nothing in the recovered canon — it names it: the environment
packet already records the station role as a "simulation-oriented station
environment," Node 7 of 9 in the GUMAS orbital chain. The quantum core,
the Observatory designation, and the deep-space siting all exist because
the engine requires them.

## Open reconciliation (logged, not overwritten)

The staged April 2026 environment packet records **altitude: 38,600 km**,
which is not a Lagrange-point figure if Earth-referenced. Owner ruling
takes precedence on siting (Lagrange point); the altitude datum remains
recorded as a staged parameter pending reconciliation — candidate
resolutions include a local/halo-orbit figure about the libration point or
a superseded early datum. See DRIFT_LOG entry 2026-06-13.
