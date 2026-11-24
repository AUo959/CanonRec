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

## Timeline and registry JSON

Preserve existing key order and keep the diff focused on the records being
edited. For new JSON files, use UTF-8, two spaces per indentation level, LF
line endings, and a final newline. The generated L2 name registry uses this
layout through `export_name_registry.py`. Preserve the L1 staff registry's
existing inline arrays and spacing when editing individual records.

The existing L2 timelines use their established layouts, both with ASCII
escapes for non-ASCII characters. The enhanced timeline uses one space per
level and ends in a newline. The original detailed timeline uses two spaces
per level and ends immediately after the closing brace. `make validate`
checks both during repository integrity validation.

To propose one event in the enhanced timeline, provide a JSON file with the
complete event, including its unique `event_id`. Generate the patch from the
repository root, then inspect it before applying it.

```bash
python3 aurora-canon-reconciler/scripts/timeline_json.py \
  --era ERA_ID --event /path/to/event.json > /tmp/canonrec-timeline.patch
cat /tmp/canonrec-timeline.patch
git apply --check /tmp/canonrec-timeline.patch
git apply /tmp/canonrec-timeline.patch
git diff -- canon/L2/timeline/
make validate
```

Pass `--replace` for an existing event in the selected era. Include provenance
and certainty in the resulting pull request. Put any intentional formatting
migration in a separate commit from semantic canon changes.

## Pull-request expectations

A pull request should state:

- the authority and provenance for the change;
- the certainty and layer before and after the change;
- whether canonical facts changed or only tooling/documentation changed;
- the exact validation commands and results;
- any unresolved ambiguity that still requires owner review.

Do not include credentials, private personal material, generated caches, or
unreviewed recovery artifacts.
