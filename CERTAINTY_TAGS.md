# CanonRec Certainty Tag Vocabulary (authoritative)

Owner-ratified 2026-07-21 (L2 Audit Ruling Batch). This file is the single source of truth
for valid certainty tags; validators and reconcilers should treat anything else as drift.

| Tag | Meaning | Terminal? |
|---|---|---|
| `CANON` | Confirmed and locked; created only by Git commit. | No (evolves via new commits) |
| `CANON_PROMOTE` | Owner-approved; next commit locks as CANON. | No |
| `LOCKED_POSITION` | (L2 map) Placement frozen; attributes may evolve. | No |
| `PLACED` | (L2 map) In current layout, revisable. | No |
| `STAGING` | Validated, usable, revisable. Default for new content. | No |
| `UNCONFIRMED` | Mentioned/implied, not validated. | No |
| `LEGEND_CONTESTED` | In-world rumor, myth, propaganda, or disputed account. | No |
| `APPROX` | Approximate quantity/date/extent (incl. tilde-dated timeline events). | No |
| `SUPERSEDED` | **Admitted 2026-07-21:** retired/renamed record kept for lineage; content frozen; points to its successor. Not an in-world dispute (contrast LEGEND_CONTESTED). | Yes |

Deprecated/invalid forms seen in the wild: `STAGING_CONFIRMED` (normalized to `STAGING`,
2026-07-21 audit).
