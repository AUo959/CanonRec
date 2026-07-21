# L2 Simulation Fabric Invariants — v0.1 (STAGING)

**Purpose:** define the temporal, physical, and corporeal logic that anchors the simulation
fabric, identify where each invariant is (or should be) enforced in code, and verify them —
**Velar Imperium domain pass = first test case.** Owner-scoped 2026-07-21.

## Invariant sets

### T — Temporal
- **T1 Monotonic causality:** no event may reference an effect of a later event. Timeline
  entries ("~N years ago" convention) must totally order within an era where cited by canon.
- **T2 Cycle coherence:** 1 Galactic Cycle = 1 standard year (Marshals Closeout precedent);
  all age/tenure/timeframe fields use this ratio.
- **T3 Snapshot discipline:** World Bible v0.2 ≈ Present; "recent actions" entries must fall
  within ~2 cycles of Present (Marshals precedent UFC-E5).
- **T4 Engine-turn mapping:** engine turns are simulation-local; any canon promotion citing
  turns must state the turn→cycle mapping rule explicitly (no implicit conversion).

### P — Physical
- **P1 Map primacy:** where World Bible and map disagree on placement, the map is source of
  truth (already canon per promotion receipt).
- **P2 Moving entities:** ships/fleets/megafauna never hold fixed coordinates; movement via
  placement_rule only.
- **P3 Adjacency consistency:** location adjacency claims must be symmetric and reference
  existing canonical_ids (no ghost edges).
- **P4 Travel plausibility:** cross-region action in a single event requires a canonical
  drive/route (hyperlane, gravitic-drive, jump) — no untraveled arrivals.

### C — Corporeal
- **C1 One-body-one-place:** a character may occupy exactly one location/vessel per timeline
  moment; simultaneous placements are drift.
- **C2 Continuity of existence:** characters have exactly one living status per moment;
  death events are terminal absent an explicit canonical revival mechanism.
- **C3 Embodied command:** offices (Chief Marshal, Grand Marshal, Lord Marshal) bind to at
  most one living incumbent per moment; succession events must exist for every transition.
- **C4 Roster closure:** new named actors enter canon only via documented source or
  deterministic selection rule (Aric Thal precedent) — never free invention.

## Enforcement map (initial audit targets)

| Layer | Where | Status |
|---|---|---|
| Engine state | `SIM_ENGINE_OUTPUTS/models.py` (LeaderState/FactionState), `engine_base.py` phases | T4 partial (turn-indexed); C1–C3 NOT explicitly enforced — leaders have no location binding |
| Advanced engine | `engine_advanced.py` v3 phases (population, tech, conflicts) | P4 implicit via migration events; verify |
| Implementation code | `aurora-cloudbank-symbolic-main` (ethics engine, drift responder, sensors, file-lock — 4 L2-referencing files + test suite) | UNAUDITED — Velar pass to trace which invariants the symbolic layer enforces |
| Canon records | entity JSONs (status, locked_at, region_id), timeline JSON | T1–T3 verifiable by static check; build `tools/`-style linter |
| Reconciler | aurora-canon-reconciler (moving-entity rule = P2) | P2 enforced at validation |

## Velar test-case plan (next pass)

1. Static-check T1–T3/P1–P3/C1–C4 across all Velar entities (virex_talvaren, internal
   factions, Marshal-Council lineage, ~300-years-ago conquest era vs timeline).
2. Trace cloudbank symbolic layer: which invariants its ethics/drift modules actually
   check; document gaps.
3. Run engine Velar scenario turns; verify no invariant violations in generated events.
4. Findings → claim ledger; violations → drift log; fixes → owner rulings.

**Certainty: STAGING** (spec ratified in scope by owner; verification pending Velar pass).
