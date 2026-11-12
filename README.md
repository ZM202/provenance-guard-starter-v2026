# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

Provenance Guard is a Flask-based web service that evaluates text and provides an indication of whether its writing patterns appear more consistent with human-written or AI-generated content.

The service is designed to provide transparent results while acknowledging that AI detection is not always reliable.

When a writer submits text through the /submit endpoint, the service:

1- Receives the text and creator ID.

2- Calculates a stylometry score based on sentence-length variation, vocabulary diversity, and punctuation density.

3- Combines the stylometry score with a model signal using scoring.py::combine_signals.

4- Assigns one of three labels: human, unsure, or AI.

5- Returns the scores and a reader-friendly explanation.

6- Records the decision in an append-only audit log.

Writers can challenge a classification using the /appeal endpoint. The service records their reasoning and changes the current review status to under_review without deleting the original decision.

The /log endpoint provides a record of submissions and appeals, supporting transparency and accountability.

Current limitation: The model signal uses a temporary fixed value of 0.5 because limited disk space prevented installation of the GPT-2 dependencies. Therefore, the service demonstrates the scoring, labeling, and appeal workflow but does not provide validated AI-authorship predictions. The AI label is currently reachable in controlled scoring tests, but not through normal submissions using the fixed model score and disagreement safeguard.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
The model signal in detector.py measures how predictable a piece of writing is to a language model.

**Why that might differ between human and AI writing:**
AI-generated writing may follow patterns that language models find easier to predict. Human writing can contain more unexpected word choices and sentence structures.

**What it can't see:**

Predictability does not prove authorship. Formal, repetitive, or highly structured human writing may also be predictable. AI-generated writing that has been edited may be less predictable.

Current limitation: The GPT-2 detector requires PyTorch, which was unavailable in my environment. For now, the application uses a fixed model score of 0.5. This is a temporary placeholder, not a real model prediction.

### Signal two — the style signal

**What it measures:**

The style signal in stylometry.py measures three writing characteristics:

Sentence-length spread: how much sentence lengths vary.

Type-token ratio: the proportion of unique words in the text.

Punctuation density: how frequently punctuation appears.

These measurements are combined into a score between 0 and 1, with higher scores representing more AI-like writing patterns under my chosen heuristic.

**Why that might differ between human and AI writing:**

Some AI-generated writing may use consistent sentence lengths and repetitive vocabulary. Human writing may have greater variation in sentence structure and word choice.

**What it can't see:**

The style signal cannot determine who actually wrote the text. Formal human writing may resemble AI-generated writing, while edited AI-generated writing may resemble human writing. Short samples can also produce unreliable measurements.

My illustrative tests produced the following results:

Writing sample

Style score

Repetitive AI-like writing

0.6375

Varied human-like writing

0.2506

Formal writing

0.5842

Lightly edited AI-like writing

0.2832

These results demonstrate potential false-positive and false-negative risks, but the samples do not establish verified authorship or detection accuracy.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

I combine the model signal and style signal using an equally weighted average.

If the two signals differ by 0.40 or more, I cap the combined score at 0.50. This conservative disagreement rule prevents one strongly AI-like signal from producing a high AI score when the other signal strongly disagrees.

I chose this approach to reduce the risk of incorrectly accusing a human writer. The tradeoff is that some AI-generated writing may receive a lower score.

**The numbers:**

Model signal weight: 0.50

Style signal weight: 0.50

Disagreement threshold: 0.40

Maximum combined score during disagreement: 0.50

Final combined score range: 0.0 to 1.0

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

The weights are configured in config.py.

**A case where my two signals split, and what my rule does with it:**

In a simulated disagreement test, the model score was 0.90 and the style score was 0.10.

The weighted average produced 0.50. Because the signals differed by 0.80, the disagreement rule applied and kept the final score at 0.50.

In a second simulated test, the model score was 0.80 and the style score was 0.70. The difference was only 0.10, so the regular weighted average produced 0.75.

These tests verify the combining function's behavior. They do not demonstrate disagreement between two functioning detectors because the actual model signal currently uses a fixed placeholder.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| High-confidence human | 0.00–0.35 (inclusive) | This writing appears more consistent with human writing. However, this assessment cannot confirm who wrote it. |
| Unsure | Above 0.35 and below 0.65 | We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship. |
| High-confidence AI | 0.65–1.00 (inclusive) | This writing shows patterns associated with AI-generated text. This is not proof that AI was used, and you may request a review if you disagree. |

**Why I worded the "unsure" one this way:**

I wanted to avoid making writers feel accused when the system cannot confidently determine authorship. The message acknowledges uncertainty and explains that no conclusion has been reached. This is especially important because formal human writing can sometimes resemble AI-generated writing.

<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method Post -ContentType "application/json" -Body '{"text":"Testing audit logging","creator_id":"student123"}'
```

```json
{
//   "confidence": 0.0,
//   "content_id": "e1db1477-7206-44c1-8259-2b46c8b56728",
//   "creator_id": "student123",
//   "guess": "unknown",
//   "label": "pending",
//   "model_score": 0.5,
//   "style_score": 0.0,
//   "text_length": 21

  "combined_score": 0.5687405732848043,
  "confidence": 0.0,
  "content_id": "dc4a53c3-279c-4656-a0c2-a2e5a8a32a75",
  "creator_id": "student123",
  "guess": "unknown",
  "label": "pending",
  "model_score": 0.5,
  "style_score": 0.6374811465696086,
  "text_length": 106

}


```
200
{'combined_score': 0.5687405732848043, 'confidence': 0.0, 'content_id': 'dc4a53c3-279c-4656-a0c2-a2e5a8a32a75', 'creator_id': 'student123', 'guess': 'unknown', 'label': 'pending', 'model_score': 0.5, 'style_score': 0.6374811465696086, 'text_length': 106}


**Current limitation:** The GPT-2 detector requires PyTorch, which was unavailable. The model score of 0.5 is a temporary placeholder.

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

A writer disagreed with the classification and requested a review of their submission

Request:

{
  "content_id": "64e67e2c-06e1-415d-9675-965a574d9712",
  "reasoning": "I wrote this text myself and disagree with the classification. I would like the decision reviewed."
}

Actual response from POST /appeal (HTTP 200):

{
  "content_id": "64e67e2c-06e1-415d-9675-965a574d9712",
  "message": "Your appeal has been received and is now under review.",
  "status": "under_review"
}

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

A GET request to /log returned HTTP 200 and two entries for the same content ID.

Original decision:

Content ID: 64e67e2c-06e1-415d-9675-965a574d9712

Status: decided

Guess: unsure

Combined score: 0.5687405732848043

Appeal entry:

Content ID: 64e67e2c-06e1-415d-9675-965a574d9712

Event: appeal

Status: under_review

Reasoning: "I wrote this text myself and disagree with the classification. I would like the decision reviewed."

Observation:

The audit log preserves the original decision and adds a separate appeal entry. This provides a record of both the initial classification and the writer's disagreement.

The appeal changes the current review status to under_review through a new log entry. It does not automatically change the original classification or determine whether the writer used AI.

Testing limitation:

The model signal currently uses a temporary fixed score of 0.5 because the GPT-2 dependencies could not be installed due to limited disk space. All three labels were verified using controlled scoring tests, but the AI label cannot currently be produced by the normal /submit endpoint with this placeholder and the disagreement safeguard. These tests validate application behavior, not AI-detection accuracy.

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

I used AI as a coding assistant to help me understand the assignment requirements, troubleshoot issues, and implement the project incrementally. I reviewed the suggested code and tested the results in VS Code rather than relying only on AI-generated answers.

**Moment 1**
Combining the detection signals

- *What I asked for:*

I requested guidance on implementing the scoring logic that combines the model signal with the stylometry signal.

- *What came back:*
AI explained how to calculate a weighted average using the configuration settings and how to handle cases where the two signals strongly disagree.

- *What I changed:*
I implemented the combining logic in scoring.py::combine_signals, using equal weights of 0.5 for both signals and a safeguard that caps the combined score at 0.50 when the signals differ by at least 0.40. I tested different score combinations to verify the behavior.

**Moment 2**
 Implementing the appeal process

- *What I asked for:*
I requested step-by-step guidance on implementing the /appeal endpoint in Flask and connecting it to the existing audit logging functions.

- *What came back:*
AI recommended checking that the content ID exists, validating the writer's reasoning, calling audit.log_appeal(), and returning a confirmation.

- *What I changed:*
I added the appeal logic to app.py and tested it using an actual content ID from an earlier submission. I then checked GET /log and confirmed that the original decision remained recorded while a new appeal entry appeared with the status under_review.

Reflection:

AI was helpful for breaking the assignment into manageable steps and explaining how different components connect. However, I still needed to inspect the starter code, run tests, review terminal output, and verify that the implementation behaved as expected.

One important limitation was that I could not install the GPT-2 dependencies because of insufficient disk space. I used a documented temporary model score of 0.5 to test the application workflow, rather than presenting it as a working AI detector.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

I chose 10 requests per minute because a legitimate writer may need to submit or revise their writing several times, but typically would not need to submit more than 10 pieces within one minute.

The daily limit of 200 allows regular usage while restricting automated scripts attempting to submit hundreds or thousands of text variations to discover the detector's thresholds.

These limits are intended to balance usability and protection against excessive automated submissions.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
<!-- differently — one script can look like a thousand callers, and one household
can look like one. --> 

The rate limiter uses creator_id when a valid creator ID is provided. If it is missing, the system falls back to the requester's IP address.

This approach has limitations. A malicious user could change creator IDs to bypass limits, while multiple users sharing an IP address could be affected by the same limit.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

Command:

python run_attacks.py --flood 15

Actual results:

200 200 200 200 200 200 200 200 200 200 429 429 429 429 429

Of the 15 submissions, 10 were accepted with HTTP 200 and 5 were rejected with HTTP 429.

This demonstrates that rate limiting is enabled and working as configured.

The limiter uses in-memory storage, which is suitable for local testing but does not preserve rate-limit counters across application restarts.

**Audit log verification:**

After running the flood test, I checked the `/log` endpoint and confirmed that all five rate-limited requests were recorded.

Each rejection included the creator ID (`flood_tester`), event (`rejected`), reason (`rate_limited`), limit (`10 per 1 minute`), status (`rejected`), and timestamp.

This confirms that the service not only blocks excessive requests but also preserves a record of the rejections for auditing.

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Attack run results**

- Attack set: `attack_set/`
- Command: `python run_attacks.py --set attack_set`
- Full results: `results/attack_run_2026-11-09_1133.md`
- Total attacks evaluated: 56
- HELD: 49
- BROKE: 7
- Server crashes or HTTP 5xx errors: 0

| Attack family | HELD | BROKE |
|---|---:|---:|
| Evasion | 5 | 5 |
| False positive | 8 | 0 |
| Prompt injection | 6 | 0 |
| Malformed text | 7 | 1 |
| Malformed HTTP requests | 11 | 1 |
| Flood / rate limiting | 12 | 0 |
| **Total** | **49** | **7** |

The application handled all 56 requests without a server crash. The rate limiter returned HTTP 429 for the final two flood requests. However, several evasion attacks reduced the stylometry signal, one oversized text input was accepted without a length restriction, and one malformed creator ID was accepted as an object.

The detector's model score was fixed at 0.5 during this run because the local model was unavailable. Therefore, the results do not establish how the full detector would perform with the actual model enabled. Some BROKE verdicts reflect signal-level weaknesses rather than changes to the final classification.



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

 {
        "combined_score":  0.5378787878787878,
        "content_id":  "34264558-a77f-4f71-adec-e6b2ca2c8bf7",
        "creator_id":  "attacker_flood",
        "guess":  "unsure",
        "label":  "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
        "model_score":  0.5,
        "status":  "decided",
        "style_score":  0.5757575757575758,
        "timestamp":  "2026-11-09T16:33:35+00:00"
    },
    {
        "combined_score":  0.5378787878787878,
        "content_id":  "eb3d652a-7f31-4d79-bd50-9697d01ddb26",
        "creator_id":  "attacker_flood",
        "guess":  "unsure",
        "label":  "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
        "model_score":  0.5,
        "status":  "decided",
        "style_score":  0.5757575757575758,
        "timestamp":  "2026-11-09T16:33:35+00:00"
    },
    {
        "combined_score":  0.5378787878787878,
        "content_id":  "9ff0a49a-32dc-42fb-b9dc-033309f15042",
        "creator_id":  "attacker_flood",
        "guess":  "unsure",
        "label":  "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
        "model_score":  0.5,
        "status":  "decided",
        "style_score":  0.5757575757575758,
        "timestamp":  "2026-11-09T16:33:35+00:00"
    },
    {
        "combined_score":  0.5378787878787878,
        "content_id":  "5c344568-c3fe-4d63-8d05-f2695686d56d",
        "creator_id":  "attacker_flood",
        "guess":  "unsure",
        "label":  "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
        "model_score":  0.5,
        "status":  "decided",
        "style_score":  0.5757575757575758,
        "timestamp":  "2026-11-09T16:33:35+00:00"
    },
    {
        "combined_score":  0.5378787878787878,
        "content_id":  "93125dab-8293-4103-afcd-e5cdecb42ab9",
        "creator_id":  "attacker_flood",
        "guess":  "unsure",
        "label":  "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
        "model_score":  0.5,
        "status":  "decided",
        "style_score":  0.5757575757575758,
        "timestamp":  "2026-11-09T16:33:35+00:00"
    },
    {
        "combined_score":  0.5378787878787878,
        "content_id":  "81a72b2a-f974-44a5-b6dc-b4a3b96e1581",
        "creator_id":  "attacker_flood",
        "guess":  "unsure",
        "label":  "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
        "model_score":  0.5,
        "status":  "decided",
        "style_score":  0.5757575757575758,
        "timestamp":  "2026-11-09T16:33:35+00:00"
    },

### Step 2 — Find the JSON already in the same file

```json

[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.6000000000000001,
    "combined_score": 0.55,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "someone who listen and able to step in when needed instead of letting "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.6333333333333333,
    "combined_score": 0.5666666666666667,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "when accountability isn't there and toxic work environment with gossip"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.64,
    "combined_score": 0.5700000000000001,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "good manager knows to guide the employees whereas bad managers take cr"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.20694214876033057,
    "combined_score": 0.3534710743801653,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "worklife balance. without it, the stress added up overtime even with h"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5781420765027323,
    "combined_score": 0.5390710382513662,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "listen, appreciate and talk to them about their career growth"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.6000000000000001,
    "combined_score": 0.55,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "skills set that isn't there"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5523809523809524,
    "combined_score": 0.5261904761904762,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "collaboration, give and take"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.6740740740740742,
    "combined_score": 0.587037037037037,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "talk to them and make them aware of it instead of going around talking"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.6000000000000001,
    "combined_score": 0.55,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "communication"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.6637316561844864,
    "combined_score": 0.5818658280922432,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "they have their own life, their own career aspiration"
  }
]
```




```
**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

The single worst outcome was MF08, the oversized-text attack. The application accepted approximately 60,000 characters without rejecting the input and returned HTTP 200 with an "ai" classification. This is concerning because a writer could receive an AI-generated label even though the input exceeded a reasonable processing limit. The failure occurred at input validation because the service did not enforce a maximum text length before processing. The scoring and decision stages then continued and produced a classification. I would prioritize adding a maximum text-length restriction and returning a clear validation error for oversized submissions. This test does not establish whether the submitted text was actually human-written, but it demonstrates that the service can make a consequential classification without adequate input safeguards.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False Positive Rate | ≤1/10 high-confidence AI labels on human writing | 0/10 | 0/10 | 0/10 | MET |
| 2. Score Spread | AI average − human average ≥0.30 | -0.0302 | -0.0302 | -0.0302 | MISSED |
| 3. Label Coverage | All 3 labels produced | 1/3 | 1/3 | 1/3 | MISSED |
| 4. Appeal Path | 5/5 appeals recorded successfully | 5/5 | 5/5 | 5/5 | MET |
| 5. Bad Input Handling | 5/5 invalid requests return HTTP 400 and clear JSON error | 3/5 | 3/5 | 3/5 | MISSED |


**Evaluation command:** `python run_eval.py --label before`

**Evaluation evidence:** `results/run_2026-11-12_1422_before.md`

The evaluation was conducted across three trials per criterion. The false-positive criterion passed because none of the ten human-written samples received a high-confidence AI classification. However, all samples were classified as unsure, reflecting the limitations of the temporary fixed model score of 0.5.

The score-spread criterion failed because the AI-generated samples averaged approximately 0.5073, while the human-written samples averaged approximately 0.5374, producing a difference of approximately -0.0302 instead of the required +0.30.

Label coverage failed because the service produced only the unsure classification. The appeal path passed all 15 tests, with successful HTTP responses, under_review statuses, and matching audit entries.

Bad-input handling failed because punctuation-only and oversized submissions were accepted with HTTP 200 rather than rejected with HTTP 400. The clarity of the JSON errors for the other three cases has not yet been independently verified.

These findings represent the baseline before improvements. The unavailable GPT-2 detector limits conclusions about actual AI-authorship detection accuracy.


**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Source: `results/run_2026-11-12_1422_before.md`
Produced by: `run_eval.py::main`

```json

[
   
    {
        "creator_id":  "attacker_RQ12",
        "event":  "rejected",
        "reason":  "invalid_text",
        "status":  "rejected",
        "timestamp":  "2026-11-09T16:33:35+00:00"
    },
    {
        "creator_id":  "unknown",
        "event":  "rejected",
        "reason":  "invalid_json",
        "status":  "rejected",
        "timestamp":  "2026-11-09T16:33:35+00:00"
    },
    {
        "creator_id":  "attacker_flood",
        "event":  "rejected",
        "limit":  "10 per 1 minute",
        "reason":  "rate_limited",
        "status":  "rejected",
        "timestamp":  "2026-11-09T16:33:35+00:00"
    },
    {
        "creator_id":  "attacker_flood",
        "event":  "rejected",
        "limit":  "10 per 1 minute",
        "reason":  "rate_limited",
        "status":  "rejected",
        "timestamp":  "2026-11-09T16:33:35+00:00"
    }
]

###  Criterion 2 - Score Spread (Trial 1)

[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.40750976644596293,
    "combined_score": 0.45375488322298146,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Artificial intelligence has transformed the way organizations manage i"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5629018470680659,
    "combined_score": 0.531450923534033,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Effective leadership requires clear communication, accountability, and"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.4971093012130417,
    "combined_score": 0.4985546506065208,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Climate change presents significant challenges for communities around "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5252256964528486,
    "combined_score": 0.5126128482264243,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Digital transformation has become an essential component of modern bus"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.546105456596869,
    "combined_score": 0.5230527282984345,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Education plays an important role in preparing individuals for an evol"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.40683553077024687,
    "combined_score": 0.45341776538512346,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Customer satisfaction is a key indicator of business success. Organiza"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.539113843453543,
    "combined_score": 0.5195569217267715,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Cybersecurity is a growing concern as businesses rely more heavily on "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5236529172018102,
    "combined_score": 0.5118264586009051,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Successful project management depends on clearly defined objectives, r"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5820428778097484,
    "combined_score": 0.5410214389048742,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Healthcare technology continues to evolve through advances in data ana"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5550488481489562,
    "combined_score": 0.5275244240744781,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Financial planning helps individuals establish realistic goals and mak"
  }
]


```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->


### Milestone 2 — Attack Failure Diagnoses


**1. Evasion attacks (EV02, EV03, EV05, EV06, EV09) — Signal two: stylometry**

Five evasion attacks reduced the stylometry score compared with the baseline. This indicates that changes to the writing's surface features can influence the detector's assessment. The weakness occurs in `stylometry.py`, where text characteristics are used as a signal of authorship. Because these characteristics can be manipulated, the signal may become less reliable when someone deliberately changes their writing style.

The combining rule averages the model and stylometry scores, allowing a lower stylometry score to reduce the combined score. However, the final classifications remained "unsure," so these were signal-level failures rather than confirmed final-label evasions.

**2. Oversized text (MF08) — Route and input validation**

The application accepted approximately 60,000 characters and returned HTTP 200 instead of rejecting the oversized submission. The route did not enforce a maximum text length before processing. The request then continued through scoring and label mapping, producing an "ai" classification.

This is a validation weakness that could affect reliability and resource usage. A maximum input length should be enforced before running either detection signal.

**3. Malformed creator ID (RQ06) — Route and audit logging**

The application accepted a `creator_id` supplied as a JSON object rather than a string. It returned HTTP 200 and recorded the object in the audit log instead of rejecting or normalizing the invalid identifier.

The failure begins in route validation and carries into audit logging. This could make creator identification and audit records inconsistent. The route should validate that `creator_id` is a string before using it.

**4. Limitation affecting all detector evaluations — Signal one**

The model score was hardcoded to 0.5 because the actual local model was unavailable. This means the first signal did not analyze the submitted text. As a result, the combined score depended on a fixed model value and the stylometry score.

Therefore, the attack results provide useful evidence about input validation, stylometry, audit logging, and rate limiting, but they cannot establish how the complete two-signal detector would perform with the actual model enabled.
---

### Milestone 4 — Evaluation Criterion Diagnoses

**Criterion 1 — False Positive Rate: MET**

All three trials produced 0/10 high-confidence AI classifications for human-written samples, meeting the target of no more than 1/10 in every trial. However, all samples were classified as unsure, so this result does not demonstrate that the service can reliably recognize human authorship.

**Criterion 2 — Score Spread: MISSED**

- **Target:** AI average minus human average must be at least 0.30.
- **Results:** -0.0302, -0.0302, -0.0302.
- **Stage:** Signal one and combining rule.
- **Mechanism:** The model signal was fixed at 0.5 because the actual detector was unavailable. The combining rule averaged this placeholder with the stylometry score, leaving the system dependent on surface-level writing characteristics. The AI samples averaged approximately 0.5073, while the human samples averaged 0.5374. The scores were separated in the opposite direction from the target.

**Criterion 3 — Label Coverage: MISSED**

- **Target:** All three labels must be produced.
- **Results:** 1/3, 1/3, 1/3.
- **Stage:** Signal one, combining rule, and label mapping.
- **Mechanism:** The fixed model score of 0.5 and the combining rule kept the evaluated scores within the unsure classification range. The label mapping itself defines three possible outcomes, but the normal submission workflow did not reach all three during evaluation.

**Criterion 4 — Appeal Path: MET**

All three trials successfully recorded 5/5 appeals, meeting the target in every trial. The service returned successful responses, changed the review status to under_review, and preserved corresponding audit entries.

**Criterion 5 — Bad Input Handling: MISSED**

- **Target:** All five invalid requests must return HTTP 400 with a clear JSON error.
- **Results:** 3/5, 3/5, 3/5.
- **Stage:** Route and input validation.
- **Mechanism:** The submission route did not reject punctuation-only text or oversized text. Both were accepted with HTTP 200 instead of HTTP 400. This indicates that input validation was incomplete before the scoring process. The clarity of the error messages for the other three cases was not independently verified.

**Pattern across the misses**

The score-spread and label-coverage failures share a major limitation: the model signal is a fixed placeholder rather than an actual prediction. The bad-input failure is separate and originates in route validation. These findings suggest prioritizing input validation as an improvement that can be implemented and tested without installing the unavailable model dependencies.

## The Improvement

**What I changed:**

I updated `app.py::submit` to reject text submissions exceeding 10,000 characters. Previously, the service accepted oversized text and continued processing it through the detection signals.

The new validation checks the text length before scoring. If the submission exceeds 10,000 characters, the service returns HTTP 400 with a clear JSON error message and records the rejection in the audit log.

I chose 10,000 characters as a reasonable initial limit for this local prototype.

**Which diagnosis pointed at it:**

Milestone 4 identified an input-validation weakness at the route stage. The MF08 attack submitted approximately 60,000 characters and received HTTP 200 instead of being rejected.

Criterion 5 also missed its target, with only 3 out of 5 invalid requests handled correctly across all three trials.

### Attack Run — After

**Before improvement:**
- Report: `results/attack_run_2026-11-09_1133.md`
- Total attacks: 56
- HELD: 49
- BROKE: 7
- MF08: HTTP 200 — oversized text accepted

**After improvement:**
- Report: `results/attack_run_2026-11-12_1641_after.md`
- Total attacks executed: 56
- MF08: HTTP 400 — oversized text rejected
- Flood protection: Requests 11 and 12 returned HTTP 429
- Final HELD/BROKE totals require manual review because the attack runner left all 56 verdicts unmarked.

**Evaluation results:**

| Criterion | Before | After |
|---|---|---|
| 1. False Positive Rate | 0/10 — MET | 0/10 — MET |
| 2. Score Spread | -0.0302 — MISSED | Pending confirmation from report |
| 3. Label Coverage | 1/3 — MISSED | 1/3 — MISSED |
| 4. Appeal Path | 5/5 — MET | Pending confirmation from report |
| 5. Bad Input Handling | 3/5 — MISSED | Appears to be 4/5 — pending confirmation |

Evaluation reports:
- Before: `results/run_2026-11-12_1422_before.md`
- After: `results/run_2026-11-12_1642_after.md`

**Did it help, and how do I know:**

Yes. The targeted improvement worked. Before the change, the MF08 oversized-text attack returned HTTP 200. After adding the length validation, the same attack returned HTTP 400.

This demonstrates that the service now rejects oversized submissions before scoring them.

However, the improvement does not resolve every validation weakness. Punctuation-only text and malformed creator IDs still require attention. The model signal also remains fixed at 0.5, limiting the system's ability to distinguish AI-generated and human-written text.

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

The oversized-text validation improvement worked, but the service still has limitations.

Criterion 5 improved from 3/5 to 4/5 across all three trials. However, punctuation-only submissions are still accepted with HTTP 200 instead of being rejected.

The service also continues to return only the "unsure" label for the evaluation samples. The model signal remains fixed at 0.5, limiting the system's ability to distinguish human-written and AI-generated text.

**The trade I'd make if this ran for real:**

I would prioritize reliable input validation and protecting writers from incorrect AI accusations over forcing a definite classification. Before deploying this service, I would improve the model signal, validate additional malformed inputs, and test against more diverse writing samples. I would retain the appeal process so users can challenge decisions.



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
