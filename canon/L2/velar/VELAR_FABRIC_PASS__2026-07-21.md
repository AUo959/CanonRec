# Velar Fabric Pass — Claim Ledger — 2026-07-21

**Status:** findings receipt (STAGING; no canon records modified by this pass)
**Spec:** `canon/L2/mechanics/FABRIC_INVARIANTS__v0.1__2026-07-21.md` — Velar Imperium = first verification test case
**Method receipts:** root repo `reports/analysis/velar_fabric_pass__2026-07-21.md`;
linter `tools/fabric_invariants_check.py`; engine run GUMASAdvancedEngine seed 42 × 40 turns
(`SIM_ENGINE_OUTPUTS/advanced_event_ledger.ndjson`, 1,349 events / 153 Velar).

## Ledger entries

### LEDGER-VELAR-0001 — P1 placement contradiction (VIOLATION, ruling queued)
`loc_vel_surak` and `loc_vel_surak_megacity_infrastructure_gravity_atmosphere_districts`
carry `canonical_position_status: canon`, but the map authority table
(`canon/L2/map/L2_MAP__LOCATION_AUTHORITY_TABLE__v0.1__2026-02-08__BAY02_0809.md`,
rows 44/54) lists both at **STAGING** with "placement TBD". Under P1 the map is source
of truth → placement is unresolved and the entity records overstate certainty.
**→ RULING-VELAR-P1.**

### LEDGER-VELAR-0002 — P3 adjacency gaps (GAP, ruling queued)
Both Velar locations have `region_id: null`; the map defines Velar Crescent zones
(Core World, Border Worlds, Ruin Worlds, Outer Colony Nodes) but no entity records
anchor to them. Megacity record's promotion note "collapse into vel_surak parent"
was never structurally executed. **→ RULING-VELAR-P3** (depends on 0001).

### LEDGER-VELAR-0003 — C1/P2 schema gaps (GAP, ruling queued)
Character capsules have no location/vessel binding field (C1 unenforceable —
confirmed for virex_talvaren and by engine state: leaders carry no location).
Mobile-asset records have no `placement_rule` field; P2 lives only in reconciler
validation. **→ RULING-FABRIC-SCHEMA.**

### LEDGER-VELAR-0004 — symbolic-layer enforcement trace (finding)
aurora-cloudbank-symbolic enforces **no fabric invariant semantically**: ethics engine =
operational conduct rules; drift responder = generic runbook executor with no
fabric-aware detector; file_lock = write atomicity (structural C2 analogue);
sensors = layer-provenance discipline (nearest to T4, `actionable=False` for L2).
Proposed wiring: fabric checker findings → DriftAlert → DriftResponder runbooks.
**→ RULING-FABRIC-WIRING.**

### LEDGER-VELAR-0005 — engine event verification (PASS with notes)
Seed-42 × 40-turn run: T1 PASS (strict order under (turn, phase, ordinal); unique
hashed event_ids); T4 PASS (turn-indexed only, no calendar claims) with note that all
118 TECH_NODE_UNLOCKED events fire as turn-1 initialization backfill; C4 PASS (no
invented actors). P4 GAP: 420 migration events (57 Velar) cite origin/destination/
reason but never a canonical drive/route. **→ RULING-ENGINE-P4.**

### LEDGER-VELAR-0006 — invariants verified for Velar domain (evidence receipt)
T1 (timeline monotonic both files; cross-file timeframe identity; conquest era ~300 ybp
coheres with Sahn'Darith Accord IA-E1), T2 (no non-1:1 cycle ratio), C2 (status
hygiene), C3 (single incumbents: Lord Marshal = virex_talvaren only), C4 (named-actor
closure incl. "Chancellor Zylox" → zylox_rhaegos) all **PASS**. T3 INFO: virex
recent_actions undated, Present-window assumed. Spec remains STAGING pending owner
review of the queued rulings.

## Open rulings queue

RULING-VELAR-P1, RULING-VELAR-P3, RULING-FABRIC-SCHEMA, RULING-FABRIC-WIRING,
RULING-ENGINE-P4 (details in root report §4).
