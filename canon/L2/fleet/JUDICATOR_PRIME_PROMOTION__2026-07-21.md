# G.U.S. Judicator Prime — Promotion Pass Receipt — 2026-07-21

**Authorization:** owner rulings, 2026-07-21. Gap analysis: root
`reports/analysis/judicator_prime_context_report__2026-07-21.md`.

## Rulings executed

### RULING-JUDICATOR-SPECS (J1) — specifications promoted
Full specification block promoted into `vessel_gu_001` from two mutually corroborating
sources (World Bible §4.2 + Ship Registry v1.0): long-range plasma lances and AI-coordinated
point defence; multi-layered energy shields and ablative armour; dual FTL cores with
emergency jump; full Sentinel deployment wing and tactical interceptors; AI-Vanguard
countermeasures and encrypted battle network.

### RULING-JUDICATOR-CREW-COUNT (J5) — 12,000 governs
The vessel's `crew_approx: ~12,000` (APPROX, owner-approved 2026-07-20 archive mining)
**supersedes** the Ship Registry's class baseline of 2,500 for this vessel. The 2,500 figure
is retained only on `cls_judicator` for lineage, marked `SUPERSEDED`.

### RULING-JUDICATOR-CREW (J2) — senior staff bound
`vessel_gu_001` now carries `crew_ids` for the eight World Bible §4.2 officers. All eight
capsules rebuilt with `location_binding → vessel_gu_001` and re-derived manifest hashes
(no state or behavioural changes):

| Officer | Role | Binding |
|---|---|---|
| Alric Tann | Commanding Officer | ship's company |
| Lyra Voss | Executive Officer | ship's company |
| Elias Radek | Sentinel-Commander | ship's company |
| Adrienne Kovas | Chief Science Officer | ship's company |
| Nia Veran | Chief Medical Officer | ship's company |
| Rhen Kailo | Chief Engineer | ship's company |
| Arin Tavos | Tactical Ops & Gunnery Chief | ship's company |
| Elias Drayen | Marshal-Captain, Sentinel SpecOps | **embarked** (not ship's company) |

### RULING-SHIP-REGISTRY (J3) — registry landed
`L2_GUMAS_SHIP_REGISTRY_v1.0.md` landed at `canon/L2/fleet/L2_GUMAS_SHIP_REGISTRY__v1.0.md`.
Its §7 senior-staff sign-off block remains historically unsigned; this pass supersedes that
route via direct owner ruling.

### RULING-SHIP-CLASSES (J4) — all 12 class records created
`canon/L2/entities/ship_classes/` — `cls_judicator`, `cls_sentinel`, `cls_aegis`,
`cls_palisade`, `cls_vanguard`, `cls_obsidian`, `cls_diplomatic`, `cls_peregrine`,
`cls_bastion`, `cls_reliant`, `cls_leviathan`, `cls_dreadraider`. Every vessel with a known
class now carries `class_entity_id`; class references resolve fleet-wide.

## Open items carried forward

- **G.U.S. Kharon / G.U.S. Sablewake** — class unknown (Registry §5.1 P2). Both records now
  carry an explicit `class_open_item` marker rather than a silent null.
- **Capsule integrity defect (NEW FINDING, unrelated to this pass):** `anaya_ral_seyr`'s
  `state.bin` is **0 bytes** and has been since the original L2 promotion commit `e34ec16` —
  its 21-slot state vector was never written, so the capsule fails manifest verification.
  Not repaired here (would launder a build defect); queued for owner decision.
