# Contributing to CanonRec

CanonRec is an authority-bearing repository. Contributions are welcome, but a
merged file is not automatically canon unless its record and promotion evidence
say so.

## Before opening a pull request

1. Identify the affected layer: L1 station, L2 simulation, or L3 protocol.
2. Preserve the source material's existing certainty label. Do not silently
   convert DRAFT, STAGING, recovered, or generated material to CANON.
3. Record provenance and authority. Owner rulings, committed canonical records,
   schemas, and deterministic receipts outrank summaries or narrative notes.
4. For new L2 referents, include a valid naming receipt under the naming
   admission policy.
5. Keep generated receipts reproducible and avoid hand-editing generated
   hashes.

## Validation

```bash
python3 -m pip install -r requirements-dev.txt
make validate
```

Run `make validate-strict` when preparing a public release. It will remain red
until every item in the integrity baseline is resolved and removed from the
baseline in the same change.

For a single entity or reconciliation packet, use the validators documented in
`aurora-canon-reconciler/SKILL.md` in addition to the repository gate.

## Pull-request expectations

A pull request should state:

- the authority and provenance for the change;
- the certainty and layer before and after the change;
- whether canonical facts changed or only tooling/documentation changed;
- the exact validation commands and results;
- any unresolved ambiguity that still requires owner review.

Do not include credentials, private personal material, generated caches, or
unreviewed recovery artifacts.
