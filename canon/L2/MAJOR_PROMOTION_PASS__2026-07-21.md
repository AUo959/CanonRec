# Major Promotion Pass — 2026-07-21

**Authorization:** owner directive — "promote anything staged that does not conflict with canon."
**Scope:** all `STAGING` L2 entity records. `UNCONFIRMED` and `SUPERSEDED` explicitly held.

## Conflict scan (pre-promotion gate)

Deterministic scan across all STAGING records — **zero conflicts found**:

- **Name collisions:** none. No STAGING name/alias equals a *different* canonical entity's name.
- **Office / incumbency collisions (C3):** none. No STAGING active character shares a
  canonical office (Chancellor, Chief/Grand/Lord Marshal, Supreme Military Commander, Fleet
  Admiral, High Strategos, etc.) with a different living canonical incumbent.
- **Fabric invariants:** linter clean (only the pre-existing `char_selene_ark` C2
  vocabulary item, owner-owned and separately queued).
- **Identity dimensions:** honored (species ≠ polity ≠ culture ≠ region; de-flattening pass
  already applied).

## Promoted: 50 entity records (STAGING → CANON)

| Kind | Count |
|---|---|
| location | 19 |
| character | 16 |
| polity | 6 |
| species | 6 |
| mobile_asset | 2 (G.U.S. Kharon, G.U.S. Sablewake) |
| anomaly | 1 (Eltari Nexus) |

Plus 2 character **capsule** identities re-promoted and manifest-re-hashed
(char_eriana_vos, char_selia_trask).

Each promoted record preserves `prev_certainty: STAGING` and carries a `promotion_to_canon`
block recording this pass and the clean conflict scan.

## Position axis preserved (not auto-placed)

Certainty (CANON) and `canonical_position_status` are **orthogonal**. 10 promoted locations
remain `unplaced`/`staging` on the map axis — they are now canonical *referents* but their
physical placement still awaits a map §8 entry (map-primacy discipline unchanged). Promotion
did **not** place anything on the map.

## Held (not promoted)

- **UNCONFIRMED (4):** `char_haden_korr`, `char_iskar_veyr`, `char_vaxtan_rhel` (generative /
  design-menu characters), `polity_shroudborn` (myth-only precursor). These are below STAGING
  by design and await owner affirmation.
- **SUPERSEDED (3):** alias-forward records (Xelvani-3, Torix-7, Vel-Surak megacity) — terminal.

## Naming gate

All promoted records that are salvage/map-derived carry `recovered_source` naming exemptions
(11 pre-gate records retrofitted this pass); the naming gate passes on the full promoted set.
Pre-2026-03-19 original canon and owner-authored records remain grandfathered (unmodified by
this pass; CI checks PR-diff files only).

## Certainty of this receipt: CANON (locked at commit).
