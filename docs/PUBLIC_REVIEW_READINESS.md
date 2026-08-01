# Public-review readiness

Status as of 2026-08-01: **open-source review ready under the MIT License**.
Both the normal and strict repository-integrity gates are clean.

## Confirmed working surfaces

- CanonRec `main` is the authority source for the CloudBank canonical
  validation mirror managed by the Aurora root workspace.
- Repository-wide parse and capsule-integrity checks have a deterministic
  entrypoint: `make validate`.
- New L2 referents are protected by the naming admission workflow.
- Historical secret-scan matches have been individually triaged; new history
  findings are CI-blocking.
- GitHub private vulnerability reporting is enabled so reviewers can disclose
  security findings without opening a public issue.
- Repository contents are licensed under the MIT License.

## Resolved integrity recovery

The two legacy zero-byte defects were recovered on 2026-08-01 from committed
authority evidence:

1. `canon/L2/entities/anaya_ral_seyr/capsule/state.bin` was restored with the
   exact 42-byte state vector named by its locked manifest. Eight intact peer
   capsules carry the same byte-identical object and digest.
2. `canon/L2/entities/organizations/org_tactical_enforcement_officers.json` was
   reconstructed from its CANON lock record, the original Marshals ledger, and
   the schema of the adjacent locked Marshal sub-unit records.

No certainty, identity, or authority transition was made. The temporary
integrity baseline is now empty, and `make validate-strict` passes. See
`reports/CANON_INTEGRITY_RECOVERY__2026-08-01.md` for the receipt.

The L2 fabric also reports a pre-existing status-vocabulary violation for
`char_selene_ark` (`alive_in_union_medical_custody`). That value requires a
canon vocabulary decision rather than an automatic rewrite.

## Cross-repository decision still required

CanonRec's L1 station staff registry and CloudBank's reconstructed staff
registry differ materially and are not part of the current propagation
contract. One authority must be selected or a deterministic merge contract
must be approved before either file is presented as the sole staff SSOT.

## Remaining owner action before a sole staff-SSOT claim

- Resolve the staff-registry authority decision described above. This does not
  block repository review, but it does block presenting either registry as the
  sole cross-repository staff SSOT.
