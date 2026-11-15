
import tempfile
import threading
import uuid
from pathlib import Path

import audit
import config
from app import app


def main():
    original_log = config.AUDIT_LOG

    with tempfile.TemporaryDirectory() as temp_dir:
        config.AUDIT_LOG = Path(temp_dir) / "concurrent.jsonl"

        try:
            content_id = str(uuid.uuid4())

            audit.log_decision(
                content_id=content_id,
                creator_id="capstone-test",
                guess="unsure",
            )

            audit.log_appeal(
                content_id=content_id,
                creator_id="capstone-test",
                reasoning="Requesting a human review.",
            )

            barrier = threading.Barrier(2)
            results = []
            results_lock = threading.Lock()

            def submit_review(reviewer_id, decision):
                with app.test_client() as client:
                    barrier.wait()

                    response = client.post(
                        f"/appeals/{content_id}/review",
                        json={
                            "reviewer_id": reviewer_id,
                            "decision": decision,
                        },
                    )

                    with results_lock:
                        results.append(response.status_code)

            threads = [
                threading.Thread(
                    target=submit_review,
                    args=("reviewer-A", "upheld"),
                ),
                threading.Thread(
                    target=submit_review,
                    args=("reviewer-B", "overturned"),
                ),
            ]

            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()

            history = audit.entries_for(content_id)
            resolutions = [
                entry for entry in history
                if entry.get("event") == "appeal_resolution"
            ]

            print("HTTP responses:", sorted(results))
            print("Review records:", len(resolutions))

            passed = (
                sorted(results) == [200, 409]
                and len(resolutions) == 1
            )

            print("Concurrent review test:", "MET" if passed else "MISSED")

        finally:
            config.AUDIT_LOG = original_log


if __name__ == "__main__":
    main()
