# Canon integrity recovery — 2026-08-01

## Scope

This receipt records recovery of the two legacy zero-byte artifacts that were
temporarily baselined by the public-readiness integrity gate. It does not
promote, demote, rename, or otherwise change canon authority.

## Recovered artifacts

### Anaya Ral-Seyr capsule state

- Target: `canon/L2/entities/anaya_ral_seyr/capsule/state.bin`
- Prior state: zero bytes; manifest mismatch
- Authority: the locked capsule manifest requires SHA-256
  `1571a3933d7f344c8facd70a26620283268d2cdc34f569f21b1c06cb1a6afb73`
- Recovery object: the byte-identical 42-byte state object already committed in
  eight intact peer capsules
- Result: restored object matches the existing manifest; the manifest was not
  rewritten

### Tactical Enforcement Officers organization record

- Target: `canon/L2/entities/organizations/org_tactical_enforcement_officers.json`
- Prior state: zero-byte tracked CANON record
- Identity and authority: fixed by
  `canon/L2/entities/CANON_LOCK_RECORD__2026-03-19.json`
- Descriptive source: `canon/L2/marshals_sentinels/marshals_sentinel_ledger.md`,
  line 125
- Structure: matched to adjacent locked Marshal sub-units, including
  `org_interceptor_squads` and `org_the_black_hand`
- Result: the locked id, name, type, faction, parent, certainty, promotion note,
  and timestamp are preserved; only source-supported alias and structural fields
  were reconstructed

## Reconciliation assessment

- Conflict classification: none found
- Certainty transition: none (`CANON` remains `CANON`)
- Authority transition: none
- New narrative claim: none
- Manifest modification: none
- Temporary integrity baseline: cleared only after both artifacts validated

## Validation

Run from the repository root:

- `make validate`: 837 tracked files, zero findings, baseline matched zero,
  three reconciler tests passed
- `make validate-strict`: 837 tracked files, zero findings
- `make secrets`: 230 commits scanned, no leaks found
- restored state SHA-256 and byte count: expected digest, 42 bytes
- JSON parse and `git diff --check`: passed
