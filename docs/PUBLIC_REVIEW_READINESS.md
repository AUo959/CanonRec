# Public-review readiness

Status as of 2026-07-29: **bounded review only**. CanonRec is suitable for
owner/reviewer inspection, but the strict publication gate remains blocked by
the items below.

## Confirmed working surfaces

- CanonRec `main` is the authority source for the CloudBank canonical
  validation mirror managed by the Aurora root workspace.
- Repository-wide parse and capsule-integrity checks have a deterministic
  entrypoint: `make validate`.
- New L2 referents are protected by the naming admission workflow.
- Historical secret-scan matches have been individually triaged; new history
  findings are CI-blocking.

## Known integrity debt

The baseline file records exact machine-checkable findings so that CI can stop
new regressions without hiding old ones:

1. `canon/L2/entities/anaya_ral_seyr/capsule/state.bin` is empty and does not
   match its capsule manifest. The defect predates the current review and is
   already recorded in canon promotion documentation.
2. `canon/L2/entities/organizations/org_tactical_enforcement_officers.json` is
   an empty legacy record. Its intended content cannot be reconstructed from
   repository evidence without inventing canon.

`make validate-strict` fails until both are repaired from authoritative source
material and their baseline entries are removed.

The L2 fabric also reports a pre-existing status-vocabulary violation for
`char_selene_ark` (`alive_in_union_medical_custody`). That value requires a
canon vocabulary decision rather than an automatic rewrite.

## Cross-repository decision still required

CanonRec's L1 station staff registry and CloudBank's reconstructed staff
registry differ materially and are not part of the current propagation
contract. One authority must be selected or a deterministic merge contract
must be approved before either file is presented as the sole staff SSOT.

## Owner actions before calling the repository open source

- Choose and add a license. Public GitHub visibility alone does not grant reuse
  rights.
- Decide whether GitHub private vulnerability reporting should be enabled.
- Resolve the two strict integrity blockers and the staff-registry authority
  decision.
