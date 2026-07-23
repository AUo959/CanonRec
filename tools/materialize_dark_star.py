from __future__ import annotations

import base64
import bz2
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TARGET = REPO / "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_UNIFIED__v1.1__2026-07-22.md"
OLD = REPO / "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_CHAPTER_03_THIRD_SILENCE__v1.0__2026-07-22.md"
EVENT = REPO / "canon/L2/events/event_dark_star_incident_4718_224.json"
DRIFT = REPO / "DRIFT_LOG.md"
DIAGNOSTICS = REPO / "tools/dark_star_payload_diagnostics.json"
PARTS = [REPO / f"tools/dark_star_bz2_{i:02d}.b64" for i in range(6)]
EXPECTED = {
    "dark_star_bz2_00.b64": (7000, "0d9450b276a6e83fb38300538b8f71e597fc64d26d30c6880b682178ef592bdd"),
    "dark_star_bz2_01.b64": (7000, "88c04f7fbbde782cc89c4e2e3e3f3f103f0f3af017c40537827a9169b2540ae9"),
    "dark_star_bz2_02.b64": (7000, "668c80008fb07a6bee5d3b451f4debb9e508cbf0de7a844c39ef1cbb4ce3e8c9"),
    "dark_star_bz2_03.b64": (7000, "c69bf37ddda75cf375cdadca7d34fc76c56bf623b58f246ac804064130d7d11b"),
    "dark_star_bz2_04.b64": (7000, "ced5708a92e3111ac24796fcf44a15a91b86391d547e2af95bed10adab9d0229"),
    "dark_star_bz2_05.b64": (6240, "d6c2dc876d0f082e42b1454d8f0fce2f8d52bb18f962e0316fdaf2f6947676cb"),
}
TARGET_REF = "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_UNIFIED__v1.1__2026-07-22.md"
OLD_REF = "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_CHAPTER_03_THIRD_SILENCE__v1.0__2026-07-22.md"


def normalized(path: Path) -> bytes:
    return b"".join(path.read_bytes().split())


def validate_payloads() -> bytes:
    results = {}
    failures = []
    chunks = []
    for part in PARTS:
        data = normalized(part)
        chunks.append(data)
        expected_length, expected_sha = EXPECTED[part.name]
        actual_sha = hashlib.sha256(data).hexdigest()
        match = len(data) == expected_length and actual_sha == expected_sha
        results[part.name] = {
            "length": len(data),
            "sha256": actual_sha,
            "expected_length": expected_length,
            "expected_sha256": expected_sha,
            "match": match,
        }
        if not match:
            failures.append(part.name)
    DIAGNOSTICS.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    if failures:
        raise RuntimeError(f"Payload checksum mismatch: {', '.join(failures)}")
    return b"".join(chunks)


def materialize_manuscript() -> None:
    payload = validate_payloads()
    content = bz2.decompress(base64.b64decode(payload)).decode("utf-8")
    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
    if digest != "51cb8369217d7054da1514074eb4d7df9b9c55cf1d31e4e237bcbf3b808e235e":
        raise RuntimeError(f"Materialized manuscript checksum mismatch: {digest}")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(content, encoding="utf-8")


def supersede_old_chapter() -> None:
    text = OLD.read_text(encoding="utf-8")
    text = text.replace("status: canon", "status: superseded", 1)
    marker = "parent_event: event_dark_star_incident_4718_224\n"
    addition = (
        marker
        + f"superseded_by: {TARGET_REF}\n"
        + "supersession_note: Preserved for provenance; the unified v1.1 manuscript governs narrative wording, translation behavior, and continuity.\n"
    )
    if "superseded_by:" not in text:
        text = text.replace(marker, addition, 1)
    OLD.write_text(text, encoding="utf-8")


def update_event_graph() -> None:
    data = json.loads(EVENT.read_text(encoding="utf-8"))
    refs = [r for r in data.get("source_refs", []) if r != OLD_REF]
    if TARGET_REF not in refs:
        refs.insert(1 if refs else 0, TARGET_REF)
    data["source_refs"] = refs
    data["governing_narrative_ref"] = TARGET_REF
    superseded = data.setdefault("superseded_narrative_refs", [])
    if OLD_REF not in superseded:
        superseded.append(OLD_REF)
    data["translation_recording_policy"] = {
        "status": "CANON",
        "rule": "Shadow personnel speak fluently in their own language. Fragmentation, substitutions, confidence warnings, and subtle errors belong to the live Union translation system rather than to speaker competence.",
        "evidentiary_boundary": "Translated output is a provisional instrument record and may be revised by later context; it does not function as an omniscient gloss.",
    }
    label = "Dark Star Unified Manuscript and Translation Improvement Pass — 2026-07-22"
    passes = data.get("promotion_pass", "")
    if label not in passes:
        data["promotion_pass"] = f"{passes}; {label}" if passes else label
    data["updated_at"] = "2026-07-22"
    extra = "Unified narrative v1.1 governs prose and live-translation presentation; prior chapter-only narrative remains provenance only."
    notes = data.get("notes", "")
    if extra not in notes:
        data["notes"] = (notes.rstrip() + " " + extra).strip()
    EVENT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_drift_log() -> None:
    heading = "## Drift Entry — 2026-07-22 (Dark Star Unified Manuscript and Translation Improvement Pass)"
    if DRIFT.exists() and heading in DRIFT.read_text(encoding="utf-8"):
        return
    entry = (
        "\n\n" + heading + "\n"
        "- **Source:** Owner-directed full narrative improvement pass following review of Shadow-captain translation behavior.\n"
        "- **Type:** narrative supersession / translation-recording correction / continuity consolidation\n"
        "- **Entities affected:** event_dark_star_incident_4718_224; unified Dark Star narrative; prior Third Silence chapter source\n"
        "- **Description:** Committed a unified three-chapter v1.1 manuscript covering The Dark Star, Valkyrie, and Third Silence. Revised Shadow communications so speaker intelligence and professional cadence remain intact while uncertainty appears through delayed live translation, substitutions, confidence warnings, competing terms, and later corrections. Applied a general prose, rhythm, viewpoint, repetition, and evidentiary-clarity improvement pass without changing the locked event outcome.\n"
        "- **Resolution:** Unified v1.1 manuscript is the governing narrative source. The prior chapter-three file remains in place as superseded provenance. Translation output is an evidentiary instrument record, not an omniscient narrator.\n"
    )
    with DRIFT.open("a", encoding="utf-8") as handle:
        handle.write(entry)


def main() -> None:
    materialize_manuscript()
    supersede_old_chapter()
    update_event_graph()
    update_drift_log()


if __name__ == "__main__":
    main()
