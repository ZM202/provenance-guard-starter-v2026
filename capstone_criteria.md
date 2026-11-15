# Capstone Milestone 4 — Acceptance Criteria

Project: Provenance Guard  
Extension: Human Appeal Review Workflow

### Criterion 1 — Pending Appeals
When a writer submits an appeal, the appeal should appear in the pending review list with the correct `content_id`. The pending endpoint should return HTTP `200`.

### Criterion 2 — Human Review
A reviewer should be able to uphold or overturn an appeal. After a successful review, the appeal should no longer appear in the pending list, but the original appeal and review decision must remain in the audit history.

### Criterion 3 — Audit Trail
Every completed review should preserve the reviewer's ID, the decision, the review timestamp, and the resolution time. This information should remain available for investigating discrepancies.

### Criterion 4 — Invalid Decisions
If a reviewer submits an unsupported decision, the system should return HTTP `400` with an error explanation. The appeal should remain pending, and no review decision should be recorded.

### Criterion 5 — Duplicate Reviews
If someone attempts to review an already resolved appeal, the system should return HTTP `409`. The original decision must remain unchanged, and no second review decision should be recorded.