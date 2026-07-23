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
TARGET_REF = "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_UNIFIED__v1.1__2026-07-22.md"
OLD_REF = "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_CHAPTER_03_THIRD_SILENCE__v1.0__2026-07-22.md"


def normalized(path: Path) -> bytes:
    return b"".join(path.read_bytes().split())


def materialize_manuscript() -> None:
    chunks = [normalized(part) for part in PARTS]
    payload = b"".join(chunks)
    diagnostics = {
        "part_lengths": [len(chunk) for chunk in chunks],
        "payload_length": len(payload),
        "payload_sha256": hashlib.sha256(payload).hexdigest(),
    }
    try:
        compressed = base64.b64decode(payload, validate=True)
        diagnostics["decoded_length"] = len(compressed)
        diagnostics["decoded_sha256"] = hashlib.sha256(compressed).hexdigest()
        content_bytes = bz2.decompress(compressed)
        diagnostics["bz2_integrity"] = "PASS"
    except Exception as exc:
        diagnostics["bz2_integrity"] = "FAIL"
        diagnostics["error"] = repr(exc)
        DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2) + "\n", encoding="utf-8")
        raise
    content = content_bytes.decode("utf-8")
    digest = hashlib.sha256(content_bytes).hexdigest()
    diagnostics["manuscript_length"] = len(content_bytes)
    diagnostics["manuscript_sha256"] = digest
    DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2) + "\n", encoding="utf-8")
    if digest != "51cb8369217d7054da1514074eb4d7df9b9c55cf1d31e4e237bcbf3b808e235e":
        raise RuntimeError(f"Materialized manuscript checksum mismatch: {digest}")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(content, encoding="utf-8")


def supersede_old_chapter() -> None:
    text = OLD.read_text(encoding="utf-8")
    text = text.replace("status: canon", "status: superseded", 1)
    marker = "parent_event: event_dark_star_incident_4718_224\n"
    addition = marker + f"superseded_by: {TARGET_REF}\n" + "supersession_note: Preserved for provenance; the unified v1.1 manuscript governs narrative wording, translation behavior, and continuity.\n"
    if "superseded_by:" not in text:
        text = text.replace(marker, addition, 1)
    OLD.write_text(text, encoding="utf-8")


def update_event_graph() -> None:
    data = json.loads(EVENT.read_text(encoding="utf-8"))
    refs = [ref for ref in data.get("source_refs", []) if ref != OLD_REF]
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
    with DRIFT.open("a", encoding="utf-8") as handle:
        handle.write("\n\n" + heading + "\n")
        handle.write("- **Source:** Owner-directed full narrative improvement pass following review of Shadow-captain translation behavior.\n")
        handle.write("- **Type:** narrative supersession / translation-recording correction / continuity consolidation\n")
        handle.write("- **Entities affected:** event_dark_star_incident_4718_224; unified Dark Star narrative; prior Third Silence chapter source\n")
        handle.write("- **Description:** Committed a unified three-chapter v1.1 manuscript covering The Dark Star, Valkyrie, and Third Silence. Revised Shadow communications so speaker intelligence and professional cadence remain intact while uncertainty appears through delayed live translation, substitutions, confidence warnings, competing terms, and later corrections. Applied a general prose, rhythm, viewpoint, repetition, and evidentiary-clarity improvement pass without changing the locked event outcome.\n")
        handle.write("- **Resolution:** Unified v1.1 manuscript is the governing narrative source. The prior chapter-three file remains in place as superseded provenance. Translation output is an evidentiary instrument record, not an omniscient narrator.\n")


def main() -> None:
    materialize_manuscript()
    supersede_old_chapter()
    update_event_graph()
    update_drift_log()


if __name__ == "__main__":
    main()
