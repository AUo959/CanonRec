"""Offline validation and idempotent staging intake for Canon Operations v1."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import subprocess
from collections.abc import Callable, Iterable, Mapping
from contextlib import closing
from datetime import datetime
from functools import cache
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource


CONTRACT_PATH = Path(__file__).resolve().parents[2] / "contracts" / "canon-ops" / "v1"
COLLECTIONS = (
    "canonical_facts",
    "operational_atoms",
    "staging_material",
    "assumptions",
    "unknowns",
)
STAGING_STATES = {"UNCONFIRMED", "STAGING"}
ArtifactReader = Callable[[dict], bytes]


class ContractError(ValueError):
    """A contract error with a JSON pointer into the submitted document."""


def _pointer(parts: Iterable[int | str]) -> str:
    return "".join(
        "/" + str(part).replace("~", "~0").replace("/", "~1") for part in parts
    ) or "/"


@cache
def _validators() -> dict[str, Draft202012Validator]:
    schemas = {
        path.name.removesuffix(".schema.json"): json.loads(path.read_text(encoding="utf-8"))
        for path in CONTRACT_PATH.glob("*.schema.json")
    }
    registry = Registry().with_resources(
        (schema["$id"], Resource.from_contents(schema)) for schema in schemas.values()
    )
    return {
        name: Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
        for name, schema in schemas.items()
    }


def _validate_schema(name: str, payload: dict) -> None:
    errors = sorted(
        _validators()[name].iter_errors(payload),
        key=lambda error: (_pointer(error.absolute_path), error.message),
    )
    if errors:
        raise ContractError(
            "\n".join(f"{_pointer(error.absolute_path)}: {error.message}" for error in errors)
        )


def _encoded_json(payload: dict) -> bytes:
    return json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")


def _unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def mutation_hash(payload: dict) -> str:
    """Hash the UTF-8 JSON encoding with the self-referential digest omitted."""
    return hashlib.sha256(
        _encoded_json({key: value for key, value in payload.items() if key != "content_hash"})
    ).hexdigest()


def _path_matches_layer(path: str, layer: str) -> bool:
    parts = path.split("/")
    return parts[0] != "canon" or parts[1:2] == [layer]


def validate_query(query: dict) -> None:
    _validate_schema("canon-query", query)
    for index, path in enumerate(query["source_paths"]):
        if not _path_matches_layer(path, query["layer"]):
            raise ContractError(f"/source_paths/{index}: {path} is outside layer {query['layer']}")
    filters = query.get("filters", {})
    if "since" in filters and "until" in filters:
        since = datetime.fromisoformat(filters["since"].upper())
        until = datetime.fromisoformat(filters["until"].upper())
        if since > until:
            raise ContractError("/filters/until: precedes the lower time bound")


def cursor_key(cursor: dict) -> tuple[int, str, str, str]:
    """Expose the ordering key used by pagination and result validation."""
    return (
        COLLECTIONS.index(cursor["collection"]),
        cursor["kind"],
        cursor["record_id"],
        cursor["source_path"],
    )


def _check_source_layer(reference: dict, layer: str, pointer: str) -> None:
    if reference["layer"] != layer or not _path_matches_layer(reference["path"], layer):
        raise ContractError(f"{pointer}/layer: {reference['path']} is outside layer {layer}")


def validate_query_result(result: dict, query: dict) -> None:
    validate_query(query)
    _validate_schema("canon-query-result", result)
    for field in ("query_id", "layer", "commit"):
        if result[field] != query[field]:
            raise ContractError(f"/{field}: does not match the query")

    page = query["page"]
    filters = query.get("filters", {})
    previous = cursor_key(page["after"]) if "after" in page else None
    last_cursor = None
    count = 0
    for collection in COLLECTIONS:
        for index, item in enumerate(result["results"][collection]):
            pointer = f"/results/{collection}/{index}"
            source = item["source"]
            _check_source_layer(source, query["layer"], pointer + "/source")
            if source["commit"] != query["commit"]:
                raise ContractError(f"{pointer}/source/commit: does not match the query")
            if not any(
                source["path"] == path or source["path"].startswith(path + "/")
                for path in query["source_paths"]
            ):
                raise ContractError(f"{pointer}/source/path: outside the requested source paths")
            if collection == "canonical_facts" and item["certainty"] != "CANON":
                raise ContractError(f"{pointer}/certainty: canonical facts require CANON")
            for item_key, filter_key in (
                ("kind", "entity_kinds"),
                ("record_id", "entity_ids"),
                ("certainty", "certainty_states"),
            ):
                if filter_key in filters and item[item_key] not in filters[filter_key]:
                    raise ContractError(f"{pointer}/{item_key}: outside the requested {filter_key}")
            last_cursor = {
                "collection": collection,
                "kind": item["kind"],
                "record_id": item["record_id"],
                "source_path": source["path"],
            }
            current = cursor_key(last_cursor)
            if previous is not None and current <= previous:
                raise ContractError(f"{pointer}: entry is out of order or repeats a cursor")
            previous = current
            count += 1
    if count > page["limit"]:
        raise ContractError("/results: exceeds the requested page size")
    if result["next_after"] is not None and result["next_after"] != last_cursor:
        raise ContractError("/next_after: must identify the last entry returned")


def _verified_artifact(
    reference: dict, layer: str, pointer: str, read_artifact: ArtifactReader
) -> bytes:
    _check_source_layer(reference, layer, pointer)
    try:
        content = read_artifact(reference)
    except (OSError, subprocess.CalledProcessError, KeyError) as exc:
        raise ContractError(f"{pointer}: could not read {reference['path']}") from exc
    if hashlib.sha256(content).hexdigest() != reference["sha256"]:
        raise ContractError(f"{pointer}/sha256: digest mismatch for {reference['path']}")
    return content


def _verify_receipt(
    reference: dict, layer: str, gate: str, pointer: str, read_artifact: ArtifactReader
) -> None:
    content = _verified_artifact(reference["artifact"], layer, pointer + "/artifact", read_artifact)
    try:
        receipt = json.loads(content, object_pairs_hook=_unique_object)
    except (ValueError, UnicodeError) as exc:
        raise ContractError(f"{pointer}/artifact: receipt is not valid JSON") from exc
    if not isinstance(receipt, dict) or receipt.get("receipt_id") != reference["receipt_id"]:
        raise ContractError(f"{pointer}/receipt_id: does not match the receipt artifact")
    actual_gate = receipt.get("gate")
    if not isinstance(actual_gate, str) or actual_gate.lower() != gate:
        raise ContractError(f"{pointer}/artifact: receipt does not attest the {gate} gate")


def validate_mutation(request: dict, read_artifact: ArtifactReader) -> None:
    _validate_schema("mutation-request", request)
    if mutation_hash(request) != request["content_hash"]:
        raise ContractError("/content_hash: does not match the request content")
    if request["approval"]["state"] != "pending" and "authority" not in request["approval"]:
        raise ContractError("/approval/authority: required for an approval decision")

    layer = request["layer"]
    create = request["operation"] == "create_staging_claim"
    seen_targets = set()
    for index, target in enumerate(request["targets"]):
        pointer = f"/targets/{index}"
        if target["layer"] != layer:
            raise ContractError(f"{pointer}/layer: target {target['record_id']} crosses layers")
        identity = (target["kind"], target["record_id"])
        if identity in seen_targets:
            raise ContractError(f"{pointer}/record_id: target is repeated")
        seen_targets.add(identity)
        expected = target["expected_state"]
        if create and expected is not None:
            raise ContractError(f"{pointer}/expected_state: a new staging claim expects no record")
        if not create and (expected is None or expected["certainty"] not in STAGING_STATES):
            raise ContractError(f"{pointer}/expected_state: operation requires a staged record")

    for index, source in enumerate(request["sources"]):
        _verified_artifact(source, layer, f"/sources/{index}", read_artifact)

    receipts = request["gate_receipts"]
    naming = receipts.get("naming")
    if create and layer == "L2" and naming is None:
        raise ContractError("/gate_receipts/naming: a new L2 claim requires naming evidence")
    if request["execution_mode"] == "deterministic_simulation" and "deterministic_run" not in receipts:
        raise ContractError("/gate_receipts/deterministic_run: required for simulation")
    for name, receipt in receipts.items():
        if name == "naming":
            variant, reference = next(iter(receipt.items()))
            gate = "naming" if variant == "receipt" else "naming_exemption"
            _verify_receipt(reference, layer, gate, f"/gate_receipts/naming/{variant}", read_artifact)
        else:
            _verify_receipt(receipt, layer, name, f"/gate_receipts/{name}", read_artifact)


def record_staging_request(
    ledger_path: Path, request: dict, read_artifact: ArtifactReader
) -> dict:
    """Record a validated request once and return its existing receipt on replay."""
    validate_mutation(request, read_artifact)
    receipt = {
        "request_id": request["request_id"],
        "content_hash": request["content_hash"],
        "status": "recorded_for_staging",
        "layer": request["layer"],
    }
    with closing(sqlite3.connect(ledger_path)) as connection, connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS staging_intake "
            "(request_id TEXT PRIMARY KEY, content_hash TEXT NOT NULL, receipt TEXT NOT NULL)"
        )
        connection.execute(
            "INSERT INTO staging_intake VALUES (?, ?, ?) ON CONFLICT(request_id) DO NOTHING",
            (receipt["request_id"], receipt["content_hash"], _encoded_json(receipt).decode("utf-8")),
        )
        existing_hash, existing_receipt = connection.execute(
            "SELECT content_hash, receipt FROM staging_intake WHERE request_id = ?",
            (receipt["request_id"],),
        ).fetchone()
        if existing_hash != receipt["content_hash"]:
            raise ContractError("/request_id: already recorded with a different content hash")
        return json.loads(existing_receipt)


def git_artifact_reader(repositories: Mapping[str, Path]) -> ArtifactReader:
    """Read blobs from allowlisted local Git repositories and pinned commits."""

    def read(reference: dict) -> bytes:
        return subprocess.check_output(
            [
                "git",
                "-C",
                str(repositories[reference["repository"]]),
                "cat-file",
                "blob",
                f"{reference['commit']}:{reference['path']}",
            ],
            env={**os.environ, "GIT_NO_LAZY_FETCH": "1"},
            stderr=subprocess.DEVNULL,
        )

    return read


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    for command in ("query", "query-result", "mutation", "submit"):
        subcommand = subcommands.add_parser(command)
        subcommand.add_argument("document", type=Path)
        if command == "query-result":
            subcommand.add_argument("--query", type=Path, required=True)
        if command in {"mutation", "submit"}:
            subcommand.add_argument(
                "--repository", action="append", default=[], metavar="OWNER/REPO=PATH"
            )
        if command == "submit":
            subcommand.add_argument("--ledger", type=Path, required=True)
    args = parser.parse_args()

    try:
        payload = json.loads(
            args.document.read_text(encoding="utf-8"), object_pairs_hook=_unique_object
        )
        if args.command == "query":
            validate_query(payload)
        elif args.command == "query-result":
            query = json.loads(
                args.query.read_text(encoding="utf-8"), object_pairs_hook=_unique_object
            )
            validate_query_result(payload, query)
        else:
            repositories = {
                name: Path(path) for name, path in (arg.split("=", 1) for arg in args.repository)
            }
            reader = git_artifact_reader(repositories)
            if args.command == "submit":
                receipt = record_staging_request(args.ledger, payload, reader)
                print(_encoded_json(receipt).decode("utf-8"))
                return 0
            validate_mutation(payload, reader)
    except (OSError, ValueError, sqlite3.Error) as exc:
        parser.exit(1, f"{exc}\n")
    print("valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
