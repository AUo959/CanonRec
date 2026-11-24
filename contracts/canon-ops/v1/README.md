# Canon Operations v1

CanonRec owns query semantics, staging request validation, and promotion decisions for the bridge. A valid request supplies evidence for staging intake. Only a separate, human-authorized Git change can create or amend CANON. [CanonRec #5](https://github.com/AUo959/CanonRec/issues/5) · [ORIONCORE bridge #47](https://github.com/AUo959/Aurora_ORIONCORE_Directory_Main/issues/47)

## Queries

`CanonQuery` identifies the query and its idempotency key, names one layer, pins a full CanonRec commit, and declares the paths in scope. A path admits that exact path or its descendants. Filters can name entity kinds, IDs, aliases, directed relationships, certainty tags, and inclusive time bounds. A ref supplied by a client must be resolved to its full commit before submission. A repeated idempotency key must identify the same query or fail as a conflict.

Each `CanonQueryResult` keeps canonical facts, operational atoms, staging material, assumptions, and unknowns in separate named arrays. Entries preserve their certainty tag and a layer-, path-, commit-, and digest-bearing source pointer. A canonical fact requires `CANON`. An operational atom records an event within its declared layer and authority. A staged request, assumption, or unknown carries its own source and does not gain authority from its inclusion in a result.

The total order is collection in the schema order shown below, then `kind`, `record_id`, and `source_path`, compared by Unicode code point. A pointer of this form uniquely identifies a result entry in the pinned snapshot. Pagination resumes strictly after the last returned key. Return up to the total requested `limit` entries across all arrays. If a next page exists, return the cursor of the last entry. At the end, return `null`. Clients must keep the commit and filters fixed while advancing the cursor.

1. `canonical_facts`
2. `operational_atoms`
3. `staging_material`
4. `assumptions`
5. `unknowns`

## Mutation requests

A `MutationRequest` identifies the request, submitting system, actor and optional relay, single target layer, target records, operation, source artifacts, approval state, execution mode, and gate receipt set. Source and receipt references pin a repository, full Git commit, path, layer, and SHA-256 digest of the exact blob bytes. References under `canon/` must explicitly match the requested layer. For other paths, the source's declared layer and supporting layer-integrity receipt are required.

| Operation | Expected current state | Proposed effect |
| --- | --- | --- |
| `create_staging_claim` | `null` | Create a STAGING claim. New L2 referents require a naming receipt or exemption. |
| `amend_staging_claim` | UNCONFIRMED or STAGING and current revision digest | Update a provisional claim in STAGING. |
| `supersede_staging_record` | UNCONFIRMED or STAGING and current revision digest | Record a staged replacement and preserve the superseded record's lineage. |
| `request_promotion_review` | UNCONFIRMED or STAGING and current revision digest | Record a request for human review. |
| `attach_outcome` | UNCONFIRMED or STAGING and current revision digest | Attach provenance and an outcome to a provisional claim. Deterministic simulations require a run receipt. |

The request describes expected state for each target. A consumer that writes staging state must compare the expected state against the current record in the same transaction as the write, rejecting mismatches. An approval carries its state and, for a decision, an authority identifier. The bridge must verify the issuing authority and applicable scope. A positive receipt or an `approved` value cannot perform promotion. CANON_PROMOTE represents an owner-approved handoff to a human-gated Git commit. CANON and terminal SUPERSEDED records remain under existing CanonRec reconciliation rules. [Certainty vocabulary](../../../CERTAINTY_TAGS.md)

Compute the request hash from all fields except `content_hash`. Serialize UTF-8 JSON with object keys sorted by Unicode code point, arrays in submitted order, no insignificant whitespace, and literal Unicode except JSON-required string escapes. The mutation envelope contains strings, arrays, objects, and JSON null. The digest is lowercase hexadecimal SHA-256. Artifact digests bind raw bytes and remain distinct from legacy semantic receipt hashes.

Verify the request digest and all source and receipt digests before intake, including on replay. The ledger writes at most one intake receipt for a request ID. A replay with identical verified content returns that receipt. A changed request with the same ID fails as a conflict. Validation and intake do not write canon or apply an operation to the target record.

## Receipt compatibility

The gate set requires evidence, layer integrity, schema validation, identity collision review, authorization or approval, and a final reconciliation recommendation. It includes a naming receipt or exemption when required and a deterministic run receipt for simulation. Each referenced receipt is a JSON object carrying a stable `receipt_id` and a `gate` matching its gate key, case-insensitively. A naming exemption uses `naming_exemption`. Preserve its verdict and provenance in the receipt. The validator verifies scope, bytes, identifier, and gate assignment. The bridge verifies that receipts apply to the actual actor, sources, target revision, and operation before acting.

- Existing evidence receipts already supply `gate: EVIDENCE` and a stable `receipt_id`. Preserve their original content hash and record the file digest separately. [Evidence receipt template](../../../aurora-canon-reconciler/assets/templates/evidence_receipt.json)
- Keep claim ledger entries and their per-claim provenance intact. Reference them as source artifacts or normalization inputs. [Claim ledger template](../../../aurora-canon-reconciler/assets/templates/claim_ledger_entry.json)
- Adapt naming receipts and exemptions to receipt objects that identify the gate, preserve the original source pointer and verdict, and use a stable ID. The existing naming validator remains authoritative for naming admission. [L2 naming schema](../../../aurora-canon-reconciler/references/l2_naming_receipt_schema.json)
- Return Station Chronicle entries as operational atoms when the requested scope covers them. Preserve their native identity, order within a source record, and L1 authority. [Station Chronicle](../../../canon/L1/station/chronicle/README.md)

## Offline validation

The validator loads the Draft 2020-12 schemas from this directory. It resolves references locally and reads only explicitly mapped Git repositories for mutation artifacts. It also provides a local SQLite intake ledger for adapters and integration tests.

```bash
python aurora-canon-reconciler/scripts/canon_ops.py query contracts/canon-ops/v1/fixtures/valid-l1-query.json
python aurora-canon-reconciler/scripts/canon_ops.py query-result result.json --query query.json
python aurora-canon-reconciler/scripts/canon_ops.py mutation request.json --repository AUo959/CanonRec=.
python aurora-canon-reconciler/scripts/canon_ops.py submit request.json --repository AUo959/CanonRec=. --ledger staging.sqlite3
make validate
```

Mutation validation accepts a repeatable `--repository OWNER/REPO=PATH` mapping, one per referenced repository. The fixture mutations use synthetic commit IDs and blob values from `fixtures/artifacts.json`. The test suite exercises them through an in-memory resolver and separately verifies the local Git resolver. Invalid fixture patches apply to the valid QGIA request before recomputing its digest.
