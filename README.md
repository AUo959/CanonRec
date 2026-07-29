# Aurora CanonRec

CanonRec is the authoritative canon repository for the Aurora / ORIONCORE
workspace. It preserves source material, certainty labels, promotion receipts,
and reconciliation tooling for the L1 station, L2 simulation, and L3 protocol
layers.

## Relationship to CloudBank

CanonRec and CloudBank have different jobs:

```text
CanonRec authority
  -> Aurora root propagation and integration checks
    -> CloudBank in-repo canon mirrors and runtime consumers
```

CloudBank can start from its checked-in mirrors without cloning CanonRec.
CanonRec is nevertheless required for authoritative canon changes, provenance
review, and the full root integration/simulation suite.

The root workspace currently propagates two managed payload families:

- `canon/L3/canonical_validation.yaml` into CloudBank's
  `config/canonical_validation.yaml`;
- L1 persona memories generated from the root L1 entity ledger into
  CloudBank's `config/mesh/memory/`.

CloudBank and CanonRec also contain staff-registry surfaces that are not yet in
that propagation contract. They must be reconciled before either is described
as the sole machine-readable staff source of truth.

## Repository map

- `canon/L1/`: Orion Station operational canon and staged source packets.
- `canon/L2/`: GUMAS galactic entities, events, mechanics, maps, and receipts.
- `canon/L3/`: protocols, validation contracts, and higher-layer governance.
- `aurora-canon-reconciler/`: reconciliation skill, validators, schemas, and
  receipt templates.
- `reports/`: deterministic reconciliation and governance receipts.
- `CERTAINTY_TAGS.md`: certainty vocabulary used to distinguish CANON,
  STAGING, DRAFT, and related states.
- `DRIFT_LOG.md`: recorded conflicts and their evidence-backed dispositions.

Versioned ZIP and `.skill` files at the repository root are historical release
artifacts. They are not the canonical working source; the expanded tracked
files take precedence.

## Validate a checkout

Python 3.12 is the supported validation environment.

```bash
python3 -m pip install -r requirements-dev.txt
make validate
```

`make validate` performs repository-wide JSON/YAML/JSONL parsing, capsule hash
verification, known-integrity-debt comparison, and naming-gate unit tests.

For a release/publication gate that permits no known integrity debt:

```bash
make validate-strict
```

The strict gate is intentionally red while the explicitly documented legacy
items in `docs/PUBLIC_REVIEW_READINESS.md` remain unresolved. The normal CI gate
baselines only those exact items and fails on any new or unexpectedly changed
integrity defect.

If `gitleaks` is installed locally, scan the complete history with:

```bash
make secrets
```

## Canon changes

CanonRec does not promote material merely because it is present in the tree.
Every change must preserve its certainty label, authority source, layer, and
provenance. See `CONTRIBUTING.md` and `aurora-canon-reconciler/SKILL.md` before
changing canonical records.

## Security and licensing

Report suspected vulnerabilities privately as described in `SECURITY.md`.
Never commit operational credentials or private source material.

No open-source license has been selected yet. Public visibility permits review
but does not grant reuse rights by itself. The repository owner must choose and
add a license before describing CanonRec as open source.
