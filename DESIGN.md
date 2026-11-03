# Week 7 — Service Design

## 1. Text Processing Flow

The service processes submitted text through seven steps:

1. **Text submission:** A user submits text and a creator ID through the `/submit` endpoint.
2. **Input validation:** The service checks whether the required fields are present and valid.
3. **Model-based detection:** `detector.py` analyzes how predictable the submitted text is to a language model.
4. **Stylometric analysis:** `stylometry.py` examines writing characteristics such as sentence length, vocabulary, and punctuation.
5. **Score combination:** The service combines the two detection signals into an overall score.
6. **Classification:** The service applies thresholds to determine an appropriate label while accounting for uncertainty.
7. **Response:** The service returns the result so the reader can see the classification.

This design uses two different signals because neither model predictability nor writing style alone can reliably determine whether text was written by a human or AI.


## 2. Detection Signals and Blind Spots

### Signal 1: Model-Based Detection (`detector.py`)

**What it measures:**

The detector uses a local language model (GPT-2) to measure how predictable the submitted text is. One measurement is perplexity, which evaluates how surprising the text is to the model.

**Why human and AI writing might differ:**

AI-generated writing can follow predictable patterns because language models generate text based on learned statistical relationships. Human writing may contain more unexpected word choices and variations.

**Blind spot:**

Predictability does not prove authorship. A human writing a formal, structured document might receive a score suggesting AI-generated text. Similarly, AI-generated writing can be edited to become less predictable.

### Signal 2: Stylometric Analysis (`stylometry.py`)

**What it measures:**

Stylometry examines writing characteristics such as sentence length, vocabulary diversity, punctuation, and sentence structure.

**Why human and AI writing might differ:**

Human writers may have individual writing habits, while AI-generated writing may exhibit consistent sentence structures and word choices. However, both can vary significantly.

**Blind spot:**

Stylometry cannot reliably identify who wrote a text. A human can write in a highly consistent style, and AI can imitate human writing patterns. Short texts may also provide insufficient information for meaningful analysis.

### Conclusion

Both signals provide useful information about writing patterns, but neither can definitively determine whether a text was written by a human or AI. Combining the signals may provide additional evidence, but the result must still be treated as uncertain.

## 3. False Positive Scenario

**Scenario:**

A student writes an original essay without using AI. The essay is well-structured, uses formal language, and follows consistent writing patterns.

**Step 1: Text Submission**

The student submits the essay through the `/submit` endpoint with their creator ID.

**Step 2: Detection**

The system analyzes the essay using `detector.py` and `stylometry.py`.

**Step 3: Scoring**

Suppose the system assigns a hypothetical combined AI-likelihood score of 0.85 (85%). This is an example, not an actual result.

**Step 4: Classification**

If the system uses a threshold of 0.80, the essay receives a label such as `likely_ai`, even though the student wrote it themselves.

**Step 5: Impact on the Student**

The student may be unfairly accused of using AI. This could affect their academic reputation or grades if the result is treated as proof.

**Step 6: Addressing the False Positive**

The system should communicate that detection results are estimates, not proof of authorship.

The student should have an opportunity to request human review and provide supporting evidence, such as drafts, notes, or document revision history.

**Conclusion:**

False positives demonstrate why detection thresholds must be selected carefully. A higher threshold may reduce false positives but could also allow more AI-generated text to go undetected. The system should prioritize transparency and avoid making definitive accusations based solely on automated detection.

## 4. API Endpoint Contracts

### Endpoint 1: POST /ping

**Purpose:**

Checks whether the web service is running and responding to requests.

**Request:**

- Method: POST
- URL: `/ping`
- Content-Type: `application/json`
- Field: `message` (string) — a test message sent by the client.

Example request:

```json
{
  "message": "hello"
}
```

**Response:**

- HTTP status: 200 OK
- Format: JSON
- Purpose: Confirms that the service is working.

The exact response fields are defined by the existing `app.py` implementation. This endpoint should remain unchanged.

### Endpoint 2: POST /submit

**Purpose:**

Accepts text from a creator and initiates analysis using the detection service.

**Request:**

- Method: POST
- URL: `/submit`
- Content-Type: `application/json`
- Field: `text` (string) — the content being analyzed.
- Field: `creator_id` (string) — identifies the creator submitting the text.

Example request:

```json
{
  "text": "This is a sample of my writing.",
  "creator_id": "student123"
}
```

**Current Response:**

- HTTP status: 501 Not Implemented
- Meaning: The endpoint exists, but its functionality has not yet been built.

**Proposed Future Response:**

- HTTP status: 200 OK
- Format: JSON
- Field: `creator_id` (string) — identifies the creator.
- Field: