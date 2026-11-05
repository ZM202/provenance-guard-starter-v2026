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



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



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
