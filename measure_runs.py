import json
import tempfile
from pathlib import Path

import audit
import config
from app import app

original_log = config.AUDIT_LOG

with tempfile.TemporaryDirectory() as temp_dir:
    config.AUDIT_LOG = Path(temp_dir) / "measurements.jsonl"

    try:
        client = app.test_client()

        for run in range(1, 11):
            response = client.post("/submit", json={
                "text": f"This is sample submission number {run} for measuring the performance of Provenance Guard.",
                "creator_id": "capstone-test"
            })

            print(f"Run {run}: HTTP {response.status_code}")

        entries = audit.read_entries()
        durations = [
            entry["duration_seconds"]
            for entry in entries
            if entry.get("status") == "decided"
        ]

        if len(durations) != 10:
            raise RuntimeError("Expected 10 successful timed submissions.")

        average = sum(durations) / len(durations)

        print("\nMEASUREMENT RESULTS")
        print("Successful runs:", len(durations))
        print("Average seconds:", average)
        print("Average milliseconds:", average * 1000)
        print("Projected compute seconds/day at 100 submissions:", average * 100)

        print("\nSTRUCTURED AUDIT LOGS")
        for entry in entries:
            print(json.dumps(entry))
            
        with open("capstone_measurements.jsonl", "w", encoding="utf-8") as file:
            for entry in entries:
                file.write(json.dumps(entry) + "\n")

        print("Saved 10 audit records to capstone_measurements.jsonl")

    finally:
        config.AUDIT_LOG = original_log