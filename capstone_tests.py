
import json
import tempfile
import uuid
from pathlib import Path

import audit
import config
from app import app


def create_appeal():
    """Create a real audit submission and appeal for an isolated test."""
    content_id = str(uuid.uuid4())

    audit.log_decision(
        content_id=content_id,
        creator_id="capstone-test",
        guess="unsure",
    )

    audit.log_appeal(
        content_id=content_id,
        creator_id="capstone-test",
        reasoning="I would like a human review.",
    )

    return content_id


def review(client, content_id, decision="upheld", reviewer="reviewer-1"):
    return client.post(
        f"/appeals/{content_id}/review",
        json={"decision": decision, "reviewer_id": reviewer},
    )


def test_criterion(client, number):
    content_id = create_appeal()
    pending_url = "/appeals/pending"

    if number == 1:
        response = client.get(pending_url)
        data = response.get_json()
        passed = (
            response.status_code == 200
            and any(
                item.get("content_id") == content_id
                for item in data.get("appeals", [])
            )
        )
        return passed, f"Pending HTTP {response.status_code}"

    if number == 2:
        decision = "upheld"
        response = review(client, content_id, decision)
        pending = client.get(pending_url).get_json()
        history = audit.entries_for(content_id)

        passed = (
            response.status_code == 200
            and not any(
                item.get("content_id") == content_id
                for item in pending.get("appeals", [])
            )
            and any(item.get("event") == "appeal" for item in history)
            and any(
                item.get("event") == "appeal_resolution"
                and item.get("decision", item.get("status")) == decision
                for item in history
            )
        )
        return passed, f"Review HTTP {response.status_code}"

    if number == 3:
        response = review(client, content_id, "overturned", "reviewer-3")
        history = audit.entries_for(content_id)
        resolutions = [
            item for item in history
            if item.get("event") == "appeal_resolution"
        ]

        passed = (
            response.status_code == 200
            and len(resolutions) == 1
            and resolutions[0].get("reviewer_id") == "reviewer-3"
            and resolutions[0].get(
                "decision", resolutions[0].get("status")
            ) == "overturned"
            and bool(resolutions[0].get("timestamp"))
            and isinstance(resolutions[0].get("resolution_seconds"), (int, float))
        )
        return passed, f"Review HTTP {response.status_code}; records {len(resolutions)}"

    if number == 4:
        response = review(client, content_id, "approved")
        pending = client.get(pending_url).get_json()
        history = audit.entries_for(content_id)

        passed = (
            response.status_code == 400
            and bool(response.get_json().get("error"))
            and any(
                item.get("content_id") == content_id
                for item in pending.get("appeals", [])
            )
            and not any(
                item.get("event") == "appeal_resolution"
                for item in history
            )
        )
        return passed, f"Invalid review HTTP {response.status_code}"

    if number == 5:
        first = review(client, content_id, "upheld")
        second = review(client, content_id, "overturned", "reviewer-2")
        history = audit.entries_for(content_id)
        resolutions = [
            item for item in history
            if item.get("event") == "appeal_resolution"
        ]

        passed = (
            first.status_code == 200
            and second.status_code == 409
            and len(resolutions) == 1
            and resolutions[0].get(
                "decision", resolutions[0].get("status")
            ) == "upheld"
        )
        return passed, f"First HTTP {first.status_code}; second HTTP {second.status_code}"

    raise ValueError(f"Unknown criterion: {number}")


def main():
    original_log = config.AUDIT_LOG
    results = []

    with tempfile.TemporaryDirectory() as temp_dir:
        config.AUDIT_LOG = Path(temp_dir) / "acceptance.jsonl"

        try:
            client = app.test_client()

            for criterion in range(1, 6):
                for trial in range(1, 4):
                    try:
                        passed, evidence = test_criterion(client, criterion)
                    except Exception as error:
                        passed = False
                        evidence = f"{type(error).__name__}: {error}"

                    result = {
                        "criterion": criterion,
                        "trial": trial,
                        "verdict": "MET" if passed else "MISSED",
                        "evidence": evidence,
                    }
                    results.append(result)

                    print(
                        f"Criterion {criterion}, Trial {trial}: "
                        f"{result['verdict']} — {evidence}"
                    )

        finally:
            config.AUDIT_LOG = original_log

    output = Path("capstone_before_results.json")
    output.write_text(json.dumps(results, indent=2), encoding="utf-8")

    met = sum(result["verdict"] == "MET" for result in results)
    print(f"\nTOTAL: {met}/15 MET")
    print(f"Saved results to {output}")


if __name__ == "__main__":
    main()
