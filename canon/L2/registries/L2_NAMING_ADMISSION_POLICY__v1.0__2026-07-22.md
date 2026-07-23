# L2 Naming Admission Policy v1.0

**Protocol:** `GUMAS_NAMING_PROTOCOL_v0.1`  
**Effective:** 2026-07-22  
**Scope:** New named referents admitted under `canon/L2/entities/`

## Rule

Every newly added named L2 referent must contain exactly one of:

1. `naming_receipt` — produced by Aurora's deterministic `NameService` against a current CanonRec registry snapshot; or
2. `naming_exemption` — a reviewable reason the name must be preserved rather than generated.

Existing canonical records are grandfathered. Editing an existing record does not retroactively manufacture a receipt. Renaming an existing record is a separate canon action and must use the gate.

## Exemptions

Permitted exemption types are:

- `owner_locked` — the owner explicitly fixed the name before this gate;
- `recovered_source` — the name is preserved from a cited archive, primary source, or observed-use capture;
- `legacy_canonical` — the referent already existed in canon under that name;
- `external_endonym` — an outside polity, culture, or individual supplied its own name.

Each exemption must record a reason, authority, and at least one source reference. An exemption preserves provenance; it is not a shortcut for ordinary hand-minting.

## Admission sequence

1. Export the current CanonRec registry:
   ```bash
   python aurora-canon-reconciler/scripts/export_name_registry.py \
     --repo-root . --output /tmp/l2_name_registry.json
   ```
2. Generate a deterministic shortlist in Aurora CloudBank:
   ```bash
   python scripts/gumas_name_mint.py \
     --entity-type PERSON \
     --entity-id char_example \
     --faction galactic_union \
     --region kharis_sector \
     --registry /tmp/l2_name_registry.json \
     --seed 4718224 \
     --count 6
   ```
3. Select a candidate when the name is narratively consequential and emit the final receipt with `--select`.
4. Place the emitted `naming_receipt` in the entity record.
5. CanonRec CI recomputes the signature and scans the current registry for exact and phonetic collisions.

## Collision policy

- Exact normalized collision with another entity: **BLOCK**.
- Invalid or mismatched receipt: **BLOCK**.
- Missing receipt or exemption on a newly added named entity: **BLOCK**.
- Phonetic or cadence crowding: **WARN** and requires human review before promotion.
- Registry digest drift after minting: **WARN**; re-run the shortlist when intervening names materially affect the choice.

## Design boundary

The service proposes names. CanonRec admits them. Human selection remains available and preferred for principal characters, major ships, polities, and locations. The receipt records the choice without replacing authorship or owner authority.
