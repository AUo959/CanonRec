import hashlib
import json
import sqlite3
import subprocess
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from canon_ops import (
    CONTRACT_PATH,
    ContractError,
    git_artifact_reader,
    mutation_hash,
    record_staging_request,
    validate_mutation,
    validate_query,
    validate_query_result,
)


def fixture(name):
    return json.loads((CONTRACT_PATH / "fixtures" / f"{name}.json").read_text(encoding="utf-8"))


def fixture_reader(artifacts):
    def read(reference):
        content = artifacts[reference["repository"]][reference["path"]]
        return json.dumps(
            content, sort_keys=True, separators=(",", ":"), ensure_ascii=False
        ).encode("utf-8")

    return read


class CanonOperationsContractTests(unittest.TestCase):
    def test_schemas_use_valid_draft_2020_12(self):
        for path in sorted(CONTRACT_PATH.glob("*.schema.json")):
            with self.subTest(path=path.name):
                Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))

    def test_l1_and_l2_queries_and_results(self):
        for layer in ("l1", "l2"):
            with self.subTest(layer=layer):
                validate_query_result(
                    fixture(f"valid-{layer}-result"), fixture(f"valid-{layer}-query")
                )

    def test_query_validates_time_bounds(self):
        query = fixture("valid-l1-query")
        query["filters"].update(since="2026-07-02T00:00:00Z", until="2026-07-01T23:59:00Z")
        with self.assertRaisesRegex(ContractError, "/filters/until"):
            validate_query(query)

    def test_query_rejects_source_paths_in_another_layer(self):
        query = fixture("valid-l1-query")
        query["source_paths"] = ["canon/L2/entities"]
        with self.assertRaisesRegex(ContractError, "/source_paths/0"):
            validate_query(query)

    def test_query_results_require_unique_cursors_in_ascending_order(self):
        query = fixture("valid-l2-query")
        result = fixture("valid-l2-result")
        facts = result["results"]["canonical_facts"]
        item = deepcopy(facts[0])
        item["record_id"] = "VESSEL-GU-002"
        query["filters"]["entity_ids"].append(item["record_id"])
        facts.append(item)
        cursor = {
            "collection": "canonical_facts",
            "kind": item["kind"],
            "record_id": item["record_id"],
            "source_path": item["source"]["path"],
        }
        result["next_after"] = cursor
        validate_query_result(result, query)

        facts.reverse()
        with self.assertRaisesRegex(ContractError, "/results/canonical_facts/1"):
            validate_query_result(result, query)

        facts[:] = [item]
        query["page"]["after"] = cursor
        with self.assertRaisesRegex(ContractError, "/results/canonical_facts/0"):
            validate_query_result(result, query)

    def test_qgia_and_gumas_mutations(self):
        read = fixture_reader(fixture("artifacts"))
        for system in ("qgia", "gumas"):
            with self.subTest(system=system):
                request = fixture(f"valid-{system}-mutation")
                validate_mutation(request, read)
                self.assertEqual(
                    mutation_hash(dict(reversed(list(request.items())))), request["content_hash"]
                )

    def test_invalid_mutation_fixtures(self):
        read = fixture_reader(fixture("artifacts"))
        for name, case in fixture("invalid-mutation-cases").items():
            with self.subTest(case=name):
                request = fixture("valid-qgia-mutation")
                for pointer, value in case["patch"].items():
                    *parts, field = pointer.lstrip("/").split("/")
                    current = request
                    for part in parts:
                        current = current[int(part)] if isinstance(current, list) else current[part]
                    current[field] = value
                request["content_hash"] = mutation_hash(request)
                with self.assertRaisesRegex(ContractError, case["error"]):
                    validate_mutation(request, read)

    def test_l2_create_and_simulation_require_their_receipts(self):
        read = fixture_reader(fixture("artifacts"))
        for gate in ("naming", "deterministic_run"):
            with self.subTest(gate=gate):
                request = fixture("valid-gumas-mutation")
                del request["gate_receipts"][gate]
                request["content_hash"] = mutation_hash(request)
                with self.assertRaisesRegex(ContractError, f"/gate_receipts/{gate}"):
                    validate_mutation(request, read)

    def test_duplicate_requests_share_one_intake_record(self):
        request = fixture("valid-qgia-mutation")
        read = fixture_reader(fixture("artifacts"))
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "staging.sqlite3"
            with ThreadPoolExecutor(max_workers=2) as executor:
                futures = [
                    executor.submit(record_staging_request, database, request, read)
                    for _ in range(2)
                ]
                first, replay = (future.result() for future in futures)
            self.assertEqual(first, replay)
            with closing(sqlite3.connect(database)) as connection:
                (count,) = connection.execute("SELECT COUNT(*) FROM staging_intake").fetchone()
            self.assertEqual(count, 1)

    def test_reused_id_rejects_changed_source_even_with_an_updated_digest(self):
        request = fixture("valid-qgia-mutation")
        artifacts = fixture("artifacts")
        read = fixture_reader(artifacts)
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "staging.sqlite3"
            record_staging_request(database, request, read)

            source = request["sources"][0]
            artifacts[source["repository"]][source["path"]]["review_note"] = "new content"
            with self.assertRaisesRegex(ContractError, "/sources/0/sha256"):
                record_staging_request(database, request, read)
            source["sha256"] = hashlib.sha256(read(source)).hexdigest()
            request["content_hash"] = mutation_hash(request)
            with self.assertRaisesRegex(ContractError, "/request_id"):
                record_staging_request(database, request, read)

    def test_git_reader_uses_pinned_blobs_from_allowlisted_local_repositories(self):
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)

            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", directory, *args], stderr=subprocess.DEVNULL
                )

            git("init", "-q")
            path = repository / "artifact.json"
            path.write_bytes(b"previous version\n")
            git("add", "artifact.json")
            git(
                "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                "commit", "--no-gpg-sign", "-qm", "Add fixture blob",
            )
            commit = git("rev-parse", "HEAD").decode("ascii").strip()
            path.write_bytes(b"working copy\n")
            reader = git_artifact_reader({"Example/CanonRec": repository})
            reference = {
                "repository": "Example/CanonRec", "commit": commit, "path": path.name
            }
            self.assertEqual(reader(reference), b"previous version\n")
            with self.assertRaises(KeyError):
                reader({**reference, "repository": "Example/Unmapped"})


if __name__ == "__main__":
    unittest.main()
