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

## Ruling resolutions — owner, 2026-07-21

- **RULING-VELAR-P1 — RESOLVED (downgrade):** both Vel-Surak location records set
  `canonical_position_status: staging` (prev preserved) to match the map authority table.
  Map remains source of truth; placement stays genuinely open until a placement ruling.
  Closes the two P1 violations (LEDGER-VELAR-0001).
- **RULING-VELAR-P3 — RESOLVED (collapse + defer):** megacity record collapsed into
  `loc_vel_surak` per the original 2026-03-19 plan — `certainty: SUPERSEDED`,
  `forwarded_to: loc_vel_surak`, `status: alias_forward_only` (Xelvani-3 precedent).
  `region_id` population deferred until P1 placement is settled (LEDGER-VELAR-0002 partially
  closed; region anchoring remains open by design).
- **RULING-FABRIC-SCHEMA — RESOLVED (approve both):** `placement_rule` added to all 16
  mobile-asset records (no-fixed-coordinates rule with per-event route citation).
  Character-capsule `location_binding` approved but NOT hand-edited: capsules are
  sha256-manifested (charforge-capsule-v1.0); rollout requires a capsule rebuild —
  implementation queued (LEDGER-VELAR-0003 → implementation tasks).
- **RULING-ENGINE-P4 — RESOLVED (promotion gate):** reason-tagged faction-level flows
  satisfy P4 at engine layer; canonical route/drive citation is required at
  canon-promotion time (reconciler checklist addition queued). No engine change.
- **RULING-FABRIC-WIRING — RESOLVED (approve):** fabric checker → DriftAlert →
  DriftResponder integration approved; implementation queued
  (aurora-cloudbank-symbolic, severity map: VIOLATION→alert/escalate, GAP→log/notify).

**Remaining open in Velar domain:** placement ruling for Vel-Surak (map row promotion),
region anchoring after placement, capsule location_binding rebuild, reconciler P2/P4/C1
check implementation, cloudbank wiring implementation.

## RULING-VELAR-PLACEMENT — owner, 2026-07-21

**Evidence surfaced during placement review:** primary sources (Physical Galaxy Packet
§3.2 CANON; knowledge-bundle excerpts) describe Vel-Surak as the **Union** economic
capital — "Engine of the Union", Trade Coalition HQ, core world alongside Prime
Ascendancy. The 2026-03-19 `velar_imperium` binding and "Velar economic capital" note
were **name-prefix drift** ("Vel-" = Velari cultural heritage, not Imperium jurisdiction).

**Ruling (executed):**
1. Vel-Surak placed in the **Inner Mid-Disk Core Zone**; map source-of-truth §2.1
   occupants updated; placed-system entry **§8.7 GU-ECON-01** added with heritage note.
2. `loc_vel_surak` faction binding corrected `velar_imperium → galactic_union`
   (prev preserved); `region_id = loc_zone_inner_mid_disk_core`;
   `canonical_position_status` restored to `canon` (map now actually places it).
3. Authority-table row 44 promoted **STAGING → CANON** (both file copies);
   row 54 (megacity) marked SUPERSEDED/collapsed.
4. **Seven macro-zone entities** created at STAGING from map §2.1–2.7
   (`loc_zone_*`) so region_id anchors resolve (P3); map remains geometry authority.

**Domain consequence:** Vel-Surak leaves the Velar Imperium domain. The Velar Crescent's
map anchors (VEL-CORE-01, VEL-BORDER-01 placed systems; Ruin World and Outer Colony Node
requirements) still lack entity records — queued as follow-up.
Closes: LEDGER-VELAR-0001 residual (placement), LEDGER-VELAR-0002 residual (region anchoring).

## Velar Crescent Anchor Pass — 2026-07-21 (closes queue item velar-crescent-anchor-entities)

Four entity records created at **STAGING**, derived strictly from the map source of truth
(epistemic rule: detail discovered, not invented):

1. **loc_vel_core_01** — Velar Core World System (VEL-CORE-01, map §8.6, Placed). Former
   Imperial Heartland; Throne World; contested continuity claims. Position: canon (map-placed).
2. **loc_vel_border_01** — Velar Border World System (VEL-BORDER-01, map §8.5, Placed).
   Forced adjacency to GU-FRONT-01; non-negotiable instability constraints. Position: canon.
3. **loc_velar_ruin_worlds** — anchor-class record (§2.3/§4); NO placed system; position
   staging until a map §8 entry places one.
4. **loc_velar_outer_colony_nodes** — anchor-class record (§2.3/§4); forced adjacency to
   Contested Frontier (§5); coheres with virex recent_actions (Outer Colony trade-route
   destabilization). Position staging.

All four anchored to `loc_zone_velar_crescent` (P3 resolved for the Velar domain).
Authority-table rows added (both copies). The Velar Imperium's §4 anchor requirements now
all have records: Core ✓ Border ✓ Ruin (class) ✓ Outer Colony (class) ✓.

**Vel-Surak lineage note:** `heritage_lineage_note` added to loc_vel_surak at STAGING with
basis INFERENCE_PENDING_SOURCE — reformist-founding transfer hypothesis recorded, explicitly
non-citable until sourced or owner-ratified.
