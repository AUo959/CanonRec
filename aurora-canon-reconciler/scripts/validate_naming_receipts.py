#!/usr/bin/env python3
"""Validate CanonRec L2 naming receipts or explicit naming exemptions."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

PROTOCOL_VERSION = "GUMAS_NAMING_PROTOCOL_v0.1"
RECEIPT_VERSION = "1.0"
ALLOWED_SELECTION_MODES = {
    "generated",
    "candidate",
    "owner_selected_from_candidates",
    "owner_locked_existing",
}
ALLOWED_EXEMPTIONS = {
    "owner_locked",
    "recovered_source",
    "legacy_canonical",
    "external_endonym",
}


def _strip_marks(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", _strip_marks(value).casefold())


def tokenize_name(value: str) -> list[str]:
    return [
        token
        for token in re.split(r"[^a-z0-9]+", _strip_marks(value).casefold())
        if token
    ]


def name_root(value: str) -> str:
    tokens = tokenize_name(value)
    if not tokens:
        return ""
    token = tokens[-1]
    for suffix in ("son", "sen", "ian", "ius", "ara", "orin", "en", "an", "ar"):
        if len(token) - len(suffix) >= 3 and token.endswith(suffix):
            token = token[: -len(suffix)]
            break
    return token[:6]


def phonetic_key(value: str) -> str:
    text = normalize_name(value)
    replacements = (
        ("ph", "f"),
        ("th", "t"),
        ("kh", "k"),
        ("q", "k"),
        ("ck", "k"),
        ("c", "k"),
        ("v", "f"),
        ("z", "s"),
        ("ae", "e"),
        ("ai", "e"),
        ("ei", "e"),
        ("y", "i"),
    )
    for source, target in replacements:
        text = text.replace(source, target)
    if not text:
        return ""
    tail = re.sub(r"[aeiou]", "", text[1:])
    tail = re.sub(r"(.)\1+", r"\1", tail)
    return (text[0] + tail)[:10]


def cadence_signature(value: str) -> dict[str, Any]:
    tokens = tokenize_name(value)
    return {
        "token_count": len(tokens),
        "token_lengths": [len(token) for token in tokens],
        "vowel_groups": [
            len(re.findall(r"[aeiouy]+", token)) for token in tokens
        ],
        "initials": "".join(token[0] for token in tokens if token),
        "terminal": tokens[-1][-2:] if tokens else "",
    }


def entity_name(data: dict[str, Any]) -> str | None:
    for field in ("canonical_name", "name", "designation", "title"):
        value = data.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def entity_id(data: dict[str, Any], path: Path) -> str:
    for field in ("canonical_id", "entity_id", "character_id", "vessel_id", "id"):
        value = data.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return path.stem


def finding(level: str, code: str, message: str, path: Path) -> dict[str, str]:
    return {
        "level": level,
        "code": code,
        "message": message,
        "path": path.as_posix(),
    }


def validate_exemption(exemption: Any, path: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(exemption, dict):
        return [
            finding(
                "BLOCK",
                "INVALID_NAMING_EXEMPTION",
                "naming_exemption must be an object",
                path,
            )
        ]
    exemption_type = exemption.get("type")
    if exemption_type not in ALLOWED_EXEMPTIONS:
        findings.append(
            finding(
                "BLOCK",
                "INVALID_NAMING_EXEMPTION_TYPE",
                f"Unsupported exemption type: {exemption_type!r}",
                path,
            )
        )
    for field in ("reason", "authority"):
        if not isinstance(exemption.get(field), str) or not exemption[field].strip():
            findings.append(
                finding(
                    "BLOCK",
                    "INCOMPLETE_NAMING_EXEMPTION",
                    f"naming_exemption.{field} is required",
                    path,
                )
            )
    refs = exemption.get("source_refs")
    if not isinstance(refs, list) or not refs:
        findings.append(
            finding(
                "BLOCK",
                "INCOMPLETE_NAMING_EXEMPTION",
                "naming_exemption.source_refs must be a non-empty list",
                path,
            )
        )
    return findings


def validate_receipt(
    data: dict[str, Any],
    receipt: Any,
    path: Path,
    registry: dict[str, Any],
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(receipt, dict):
        return [
            finding(
                "BLOCK",
                "INVALID_NAMING_RECEIPT",
                "naming_receipt must be an object",
                path,
            )
        ]

    name = entity_name(data)
    current_id = entity_id(data, path)
    if receipt.get("protocol") != PROTOCOL_VERSION:
        findings.append(
            finding(
                "BLOCK",
                "NAMING_PROTOCOL_MISMATCH",
                f"Expected {PROTOCOL_VERSION}",
                path,
            )
        )
    if receipt.get("receipt_version") != RECEIPT_VERSION:
        findings.append(
            finding(
                "BLOCK",
                "NAMING_RECEIPT_VERSION",
                f"Expected receipt_version {RECEIPT_VERSION}",
                path,
            )
        )
    if name and receipt.get("canonical_name") != name:
        findings.append(
            finding(
                "BLOCK",
                "NAMING_NAME_MISMATCH",
                "Receipt canonical_name does not match entity name",
                path,
            )
        )

    request = receipt.get("request")
    if not isinstance(request, dict):
        findings.append(
            finding(
                "BLOCK",
                "NAMING_REQUEST_MISSING",
                "Receipt request object is required",
                path,
            )
        )
    else:
        if request.get("entity_id") != current_id:
            findings.append(
                finding(
                    "BLOCK",
                    "NAMING_ENTITY_ID_MISMATCH",
                    f"Receipt entity_id must be {current_id}",
                    path,
                )
            )
        if not request.get("entity_type"):
            findings.append(
                finding(
                    "BLOCK",
                    "NAMING_ENTITY_TYPE_MISSING",
                    "Receipt request.entity_type is required",
                    path,
                )
            )

    selection_mode = receipt.get("selection_mode")
    if selection_mode not in ALLOWED_SELECTION_MODES:
        findings.append(
            finding(
                "BLOCK",
                "NAMING_SELECTION_MODE",
                f"Unsupported selection_mode: {selection_mode!r}",
                path,
            )
        )

    signature = receipt.get("signature")
    if not isinstance(signature, dict) or not name:
        findings.append(
            finding(
                "BLOCK",
                "NAMING_SIGNATURE_MISSING",
                "Receipt signature is required",
                path,
            )
        )
    else:
        expected = {
            "normalized": normalize_name(name),
            "root": name_root(name),
            "phonetic_key": phonetic_key(name),
            "cadence": cadence_signature(name),
        }
        for key, value in expected.items():
            if signature.get(key) != value:
                findings.append(
                    finding(
                        "BLOCK",
                        "NAMING_SIGNATURE_MISMATCH",
                        f"signature.{key} does not match the canonical name",
                        path,
                    )
                )

    digest = receipt.get("registry_digest")
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        findings.append(
            finding(
                "BLOCK",
                "NAMING_REGISTRY_DIGEST",
                "registry_digest must be a lowercase SHA-256 hex string",
                path,
            )
        )
    elif registry.get("registry_digest") and digest != registry["registry_digest"]:
        findings.append(
            finding(
                "WARN",
                "NAMING_REGISTRY_ADVANCED",
                "Receipt was minted against a different registry snapshot; recheck crowding before merge",
                path,
            )
        )

    candidate_set = receipt.get("candidate_set")
    if not isinstance(candidate_set, list) or not candidate_set:
        findings.append(
            finding(
                "BLOCK",
                "NAMING_CANDIDATE_SET",
                "candidate_set must be non-empty",
                path,
            )
        )
    elif name not in candidate_set:
        findings.append(
            finding(
                "BLOCK",
                "NAMING_CANDIDATE_SELECTION",
                "canonical name must appear in candidate_set",
                path,
            )
        )

    if not isinstance(receipt.get("rejected_candidates"), list):
        findings.append(
            finding(
                "BLOCK",
                "NAMING_REJECTIONS_MISSING",
                "rejected_candidates must be a list",
                path,
            )
        )
    if not isinstance(receipt.get("collisions_checked"), int) or receipt.get(
        "collisions_checked", -1
    ) < 0:
        findings.append(
            finding(
                "BLOCK",
                "NAMING_COLLISION_COUNT",
                "collisions_checked must be a non-negative integer",
                path,
            )
        )

    normalized = normalize_name(name or "")
    for entry in registry.get("entries", []):
        existing_id = str(entry.get("entity_id", ""))
        if existing_id == current_id:
            continue
        existing_name = str(entry.get("canonical_name", ""))
        if normalize_name(existing_name) == normalized:
            findings.append(
                finding(
                    "BLOCK",
                    "NAMING_EXACT_COLLISION",
                    f"Name collides with {existing_id}: {existing_name}",
                    path,
                )
            )
        elif name and phonetic_key(existing_name) == phonetic_key(name):
            findings.append(
                finding(
                    "WARN",
                    "NAMING_PHONETIC_CROWDING",
                    f"Name is phonetically crowded with {existing_id}: {existing_name}",
                    path,
                )
            )
    return findings


def validate_file(
    path: Path,
    registry: dict[str, Any],
    require_receipt: bool,
) -> list[dict[str, str]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [finding("BLOCK", "INVALID_JSON", str(exc), path)]
    if not isinstance(data, dict):
        return [
            finding(
                "BLOCK",
                "ENTITY_NOT_OBJECT",
                "L2 entity file must contain a JSON object",
                path,
            )
        ]
    if not entity_name(data):
        return []
    if "naming_receipt" in data:
        return validate_receipt(data, data["naming_receipt"], path, registry)
    if "naming_exemption" in data:
        return validate_exemption(data["naming_exemption"], path)
    if require_receipt:
        return [
            finding(
                "BLOCK",
                "NAMING_RECEIPT_REQUIRED",
                "New named L2 referents require naming_receipt or naming_exemption",
                path,
            )
        ]
    return [
        finding(
            "INFO",
            "LEGACY_NAME_GRANDFATHERED",
            "Existing record has no naming receipt",
            path,
        )
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--registry", type=Path, required=True)
    parser.add_argument("--require-receipt", action="store_true")
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    findings: list[dict[str, str]] = []
    for path in args.files:
        findings.extend(validate_file(path, registry, args.require_receipt))
    blocks = [item for item in findings if item["level"] == "BLOCK"]
    payload = {"passed": not blocks, "blocks": len(blocks), "findings": findings}
    if args.json_output:
        print(json.dumps(payload, indent=2))
    else:
        for item in findings:
            print(
                f"{item['level']}: {item['code']}: {item['path']}: "
                f"{item['message']}"
            )
        print(
            f"Naming gate: {'PASS' if not blocks else 'BLOCKED'} "
            f"({len(blocks)} block(s))"
        )
    return 0 if not blocks else 1


if __name__ == "__main__":
    raise SystemExit(main())
