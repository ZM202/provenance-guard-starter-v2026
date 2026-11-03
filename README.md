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
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
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

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

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
