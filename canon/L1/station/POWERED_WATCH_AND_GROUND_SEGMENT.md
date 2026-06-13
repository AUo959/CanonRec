---
entity_id: "ORION.STATION.OPS.POWERED_WATCH"
entity_type: "doctrine"
layer: "L1"
name: "Powered Watch & the Ground Segment Doctrine"
certainty: "CANON"
registry_authority: "owner_ruling"
ruled_at: "2026-06-13"
doc_sources:
  - "Owner definitional ruling (the Pilot), 2026-06-13"
  - "STATION_PURPOSE_DEFINITION.md (the station is the chassis around the L2 engine)"
  - "ORION__ARCHITECTURE_CONTRACT__L1_L2_L3__v1.0.md (state deltas, never fact overwrites)"
  - "tools/powered_watch.py first run, 2026-06-13 (reports/simulation/powered_watch_v1__2026-06-13)"
---

# Powered Watch & the Ground Segment Doctrine

Two canon additions, both required by a single owner ruling: **Orion Station
is set in our reality and operates as if it is literally on station.** This
is not narrative flourish; it is the coherence guardrail that lets the
station persist as real things are built for it.

## 1. The Powered Watch (operational concept)

A *powered watch* is a watch block during which the L1 chassis actively
operates the L2 GUMAS engine. The two layers are coupled, not merely
co-resident:

- **Chassis → engine.** Crew labor on engine-servicing duties — quantum
  core coherence, ring power and spin, life-support and cooling, comms —
  determines engine throughput for the watch. A well-serviced station runs
  more simulation turns per hour; a station distracted from servicing runs
  fewer. Engine capacity is *earned by the crew*, hour by hour.
- **Engine → chassis.** Notable engine events (insurgencies, civil wars,
  fragmentation in the simulated galaxy) downlink into the watch and inject
  **analysis-cell** tasks onto the next hour's station board. The galaxy's
  crises become the crew's work.
- **Boundary discipline (L3 law).** The engine produces *state deltas* and
  *telemetry*; it never overwrites L1 station facts. Every turn is logged
  as a STAGING chronicle atom (domain `engine`) with a deterministic run
  anchor, promotion-gated like all candidate canon.

First demonstrated 2026-06-13 (seed 808): a four-hour powered watch ran the
`GUMASAdvancedEngine` for 11 turns (throughput 4/4/2/1 by hour, scaling with
crew servicing), the simulated galaxy destabilised 0.608 → 0.571 across the
window, and an hour-2 insurgency pair injected an analysis-cell task back
onto the board. Full souls accounting held (41/41), companions answered the
downlink each hour, and the L3 narrative audit returned *supported*.

## 2. The Ground Segment Doctrine (coherence guardrail)

If the station is literally on station at its Lagrange point, then **this
repository and everything in it is the station's ground segment** — the
Earth-side mission control, flight-operations software, and uplink/downlink
infrastructure that supports a real crewed deep-space facility. This gives
every real-world implementation a literal L1 role, so nothing we build is
"just code":

| Real-world artifact | L1 role aboard the mission |
|---|---|
| CloudBank repo + control plane | Ground-segment flight software & operations |
| The mesh runtime / station_query | Deep-space comms link to Aurora and the crew |
| Sensor Array (`/api/sensors`) | Telemetry downlink, read-only by design (one-way) |
| Station chronicle | Mission log & telemetry archive |
| CI gates / workspace_verify / flight log | Flight rules and go/no-go criteria |
| Pull requests & canon promotion | Change requests through configuration control |
| ORD policy family | Onboard autonomous validation/security |
| GUMAS engine | The payload the whole mission exists to operate |

**The rule going forward:** any new real-world capability must declare its
L1 home — is it *onboard* (a station system the crew operate) or *ground
segment* (Earth-side support)? A capability with no coherent L1 explanation
does not get built into the persistent station; it is reworked until it has
one, or kept outside canon. This is how canon and narrative evolve to absorb
new additions without drift: the map is required to stay whole.

**Boundary of authority.** The ground segment observes and uplinks change
requests; it does not command onboard execution. Onboard autonomy — Aurora
arbitration under Picard Delta 3 — governs what actually happens on station,
exactly as the L3 law requires. Mission control proposes; the station, under
its ethics protocol, disposes.

## Why this pushes forward rather than re-proving the past

Early in the project, the tooling forced the design to be aspirational. The
powered watch is the inverse: a genuinely new capability (bidirectional
L1↔L2 coupling with earned throughput and crisis feedback) that did not
exist before, expressed in working code first and named in canon second.
The ground-segment doctrine then guarantees that *future* real capabilities
— real instruments, real compute, real links — already have a canonical home
the moment they arrive. The frame is built to receive what does not exist
yet, not merely to legitimize what already did.
