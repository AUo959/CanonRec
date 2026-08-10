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

## Velar test-case results & ruling batch (2026-07-21)

Velar pass executed (receipts: `canon/L2/velar/VELAR_FABRIC_PASS__2026-07-21.md`; root
`reports/analysis/velar_fabric_pass__2026-07-21.md`; linter `tools/fabric_invariants_check.py`).

| Invariant | Velar verification | Enforcement decision (owner rulings) |
|---|---|---|
| T1, T2 | PASS (static; both timeline files) | Linter enforces |
| T3 | INFO — undated recent_actions unverifiable | Assumed Present-window; linter flags |
| T4 | PASS (engine seed-42×40; turn-indexed only) | Turn-1 tech backfill = initialization; mapping rule required at promotion |
| P1 | 2 violations found → RESOLVED by downgrade | Map primacy confirmed; entity position status must not exceed map row status (linter enforces) |
| P2 | Schema gap → `placement_rule` added to all 16 mobile assets | Reconciler check implementation queued |
| P3 | Gaps documented; megacity collapse executed (SUPERSEDED alias-forward) | region_id anchoring deferred until placement ruling |
| P4 | Engine migration events carry no route | **Promotion gate:** engine flows acceptable; route/drive citation required at canon promotion (reconciler checklist queued) |
| C1 | Gap confirmed (capsules + engine) | `location_binding` approved; requires capsule rebuild (queued — capsules are sha256-manifested) |
| C2, C3, C4 | PASS (incl. engine C4: no invented actors) | Linter enforces; `alias_forward_only` admitted to status vocabulary |
| Symbolic layer | Zero semantic fabric enforcement (4-module trace) | Checker→DriftAlert→DriftResponder wiring approved, implementation queued |

**Certainty: STAGING → verified-in-scope for the Velar domain.** Spec v0.1 text unchanged;
promotion of the spec itself remains an owner gate after a second domain pass (AI Warlords
queued as next candidate).

## Ruling batch closure — 2026-08-09

All five rulings from the 2026-07-21 batch are now implemented.

| Ruling | Implementation | Where |
|---|---|---|
| RULING-VELAR-P1 (placement) | Map primacy enforced at validation; 19 overstating records downgraded | `validate_entity.py` FABRIC_P1_*; canon `p1_downgrade` blocks |
| RULING-VELAR-P3 (adjacency/collapse) | Megacity collapse executed; region anchoring still deferred to placement | canon (SUPERSEDED alias-forward) |
| RULING-FABRIC-SCHEMA (a) placement_rule | All mobile assets carry `placement_rule`; P2 enforced at validation | `validate_entity.py` FABRIC_P2_* |
| RULING-FABRIC-SCHEMA (b) location_binding | All 40 capsules bound; capsules rebuilt (sha256 manifests re-derived) | canon capsules; `fabric_invariants_check.py` C1 |
| RULING-ENGINE-P4 (route citation) | Promotion gate live; satisfiable by route citation **or** explicit `route_exemption` | `validate_entity.py` FABRIC_P4_*; `ROUTE_REGISTRY v0.1` |
| RULING-FABRIC-WIRING (checker→responder) | Findings routed to `DriftAlert` → `DriftResponder` with dedicated fabric runbooks | cloudbank `src/monitoring/fabric_invariant_bridge.py` |

**Enforcement now exists at three points**, and they share semantics deliberately:

1. **Static** — `tools/fabric_invariants_check.py` over committed canon (T/P/C).
2. **Pre-canon** — `aurora-canon-reconciler` blocks P1/P2/P4 breaches at validation.
3. **Runtime** — CloudBank converts findings into DriftAlerts and runs fabric runbooks.

**A design principle earned across this batch:** three invariants (P1 placement, P4
route, C1 binding) each hit the same wall — canon establishes a *fact* without
establishing the *referent* the invariant wants cited. The resolution in every case was
to require the question be **answered**, not fabricated: `canonical_position_status:
unplaced`, `route_exemption`, and `location_binding: undetermined` are all explicit,
reasoned answers carrying the evidence that does exist and what would resolve them. A
gate that can only be satisfied by invention is a defect — it either produces false
canon or gets switched off.

**Certainty: STAGING → verified-in-scope for the Velar domain, implemented across all
three enforcement points.** Spec v0.1 text unchanged; promotion of the spec itself
remains an owner gate after a second domain pass (AI Warlords queued).
