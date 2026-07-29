#!/usr/bin/env python3
"""Validate repository-wide CanonRec data and capsule integrity.

The default mode compares findings with an exact legacy baseline: new findings
and stale baseline entries fail. ``--strict`` ignores the baseline and fails on
every finding, making it suitable for a publication/release gate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

try:
    import yaml
except ImportError:  # pragma: no cover - exercised through the CLI error path
    yaml = None


DEFAULT_BASELINE = Path(
    "aurora-canon-reconciler/references/repository_integrity_baseline.json"
)


@dataclass(frozen=True, order=True)
class Finding:
    check: str
    path: str
    detail: str

    @property
    def key(self) -> tuple[str, str]:
        return self.check, self.path


def tracked_files(repo_root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(repo_root), "ls-files", "-z"],
        check=True,
        capture_output=True,
    )
    return [repo_root / item.decode() for item in result.stdout.split(b"\0") if item]


def display_path(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_data_files(repo_root: Path, files: Iterable[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        relative = display_path(path, repo_root)
        if not path.is_file():
            continue

        if relative.startswith("canon/") and path.stat().st_size == 0:
            findings.append(Finding("empty_file", relative, "tracked canon file is empty"))
            continue

        try:
            if path.suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
            elif path.suffix == ".jsonl":
                for line_number, line in enumerate(
                    path.read_text(encoding="utf-8").splitlines(), start=1
                ):
                    if line.strip():
                        json.loads(line)
            elif path.suffix in {".yaml", ".yml"}:
                if yaml is None:
                    raise RuntimeError(
                        "PyYAML is required; install requirements-dev.txt before validation"
                    )
                list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
        except (UnicodeDecodeError, json.JSONDecodeError, yaml.YAMLError if yaml else ValueError) as exc:
            findings.append(
                Finding("parse_error", relative, f"{type(exc).__name__}: {exc}")
            )
        except RuntimeError:
            raise
    return findings


def validate_capsules(repo_root: Path, files: Iterable[Path]) -> list[Finding]:
    findings: list[Finding] = []
    manifests = sorted(
        path
        for path in files
        if path.name == "manifest.json" and "capsule" in path.parts and path.is_file()
    )
    for manifest_path in manifests:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue  # Already reported by the repository parse pass.

        records = manifest.get("records", [])
        if not isinstance(records, list):
            findings.append(
                Finding(
                    "capsule_manifest_shape",
                    display_path(manifest_path, repo_root),
                    "records must be a list",
                )
            )
            continue

        for record in records:
            if not isinstance(record, dict):
                continue
            record_path = record.get("path")
            expected = record.get("sha256")
            if not isinstance(record_path, str) or not isinstance(expected, str):
                findings.append(
                    Finding(
                        "capsule_manifest_shape",
                        display_path(manifest_path, repo_root),
                        "record requires string path and sha256",
                    )
                )
                continue
            if record_path == "manifest.json":
                continue

            target = manifest_path.parent / record_path
            relative = display_path(target, repo_root)
            if not target.is_file():
                findings.append(Finding("capsule_missing_file", relative, "manifest target missing"))
                continue
            actual = sha256_file(target)
            if actual != expected:
                findings.append(
                    Finding(
                        "capsule_hash_mismatch",
                        relative,
                        f"expected {expected}; got {actual}",
                    )
                )
    return findings


def load_baseline(repo_root: Path, baseline_path: Path) -> dict[tuple[str, str], str]:
    resolved = baseline_path if baseline_path.is_absolute() else repo_root / baseline_path
    payload = json.loads(resolved.read_text(encoding="utf-8"))
    return {
        (entry["check"], entry["path"]): entry.get("reason", "")
        for entry in payload.get("known_issues", [])
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on every finding instead of accepting the exact legacy baseline.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = args.repo_root.resolve()
    files = tracked_files(repo_root)

    try:
        findings = sorted(
            set(parse_data_files(repo_root, files) + validate_capsules(repo_root, files))
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"tracked_files={len(files)} findings={len(findings)} strict={args.strict}")
    for finding in findings:
        print(f"{finding.check}: {finding.path}: {finding.detail}")

    if args.strict:
        return 1 if findings else 0

    baseline = load_baseline(repo_root, args.baseline)
    current = {finding.key for finding in findings}
    unexpected = sorted(current - set(baseline))
    stale = sorted(set(baseline) - current)

    if unexpected:
        print("Unexpected findings:", file=sys.stderr)
        for check, path in unexpected:
            print(f"- {check}: {path}", file=sys.stderr)
    if stale:
        print("Resolved findings still present in baseline:", file=sys.stderr)
        for check, path in stale:
            print(f"- {check}: {path}", file=sys.stderr)

    if unexpected or stale:
        return 1

    print(f"baseline_matched={len(baseline)} new_findings=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
