# CONFLICT MATRIX — GUMAS Staging Bay (v0.2)

## Snapshot
- Date: 2026-02-08
- Build: BAY02_0809
- Anchor: EOS_SEED_ORION
- Ethics: Picard_Delta_3

## Active Conflicts (this snapshot)

| Area | Conflict | Status | Resolution Direction |
|---|---|---|---|
| L2 map primacy | `gumas_l_2_galactic_map_source_of_truth.md` self-declares precedence, but `L3_GOV__CANON_INDEX_L2_Primacy__v0.1__2026-02-06__BAY01_1609.md` does not yet reference it | **Open** | Patch CANON INDEX to explicitly rank this map doc at the top of L2 physical placement authority |
| Location placement language | Origin dossier v0.5 often says “placement TBD” while the map Source of Truth provides **macro-zone placement** (not precise coordinates) | **Resolved** | Treat as compatible: macro placement fixed; micro placement TBD. Recorded in LAT v0.1 |
| World bible invariants | `GUMAS_L2_World_Bible.md` lacks ORION invariants (anchor/ethics/layer notes) | **Open** | Use patched wrapper `L2_SYSTEM__GUMAS_L2_World_Bible__v0.2__2026-02-08__BAY02_0809.md` for all downstream work; keep original as legacy artifact |
| Naming normalization | Curly quotes / apostrophes / hyphen semantics may diverge across docs vs `GUMAS_NAMING_PROTOCOL_v0.1.md` | **Open** | Run a normalization sweep prior to promotion; keep canonical names stable and log any alias merges |

## De-duplication notes (not conflicts, but risk)
- Multiple Origin Dossier revisions exist (`v0.3`, `v0.5`, plus the repaired `v0.5.1` synthesis packet). Prefer the repaired packet for promotion; keep earlier drafts only as provenance.

---

Built for consistency, clarity, and care.
