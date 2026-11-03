# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False Positive Rate

<!-- Your criterion. It must name a number. -->


In each of the three trials, no more than 1 out of 10 human-written submissions should be labeled as high-confidence AI-generated.

**Why this target:**

I want to minimize false accusations because incorrectly labeling someone's original writing as AI-generated can damage their credibility. I chose a maximum of 10% as a measurable target, while recognizing that AI detection is not perfect.

---

## 2. Score Spread

<!-- Your criterion. -->

In each of the three trials, the average score for 10 clearly AI-generated texts should be at least 0.30 higher than the average score for 10
clearly human-written texts.


**Why this target:**

I chose a difference of 0.30 because I want the system to show a measurable distinction between human and AI writing. The scores do not need to
be perfect, but there should be enough separation to make the results meaningful.

---

## 3. Label Coverage

<!-- Your criterion. -->

In each of the three trials, the system should produce all three classification labels at least once when tested with a set of 15 submissions
containing human-written, AI-generated, and borderline text.

**Why this target:**

I chose this target because the system should recognize different levels of uncertainty rather than classify every submission as either human
or AI. All three labels should be reachable so the system can provide more meaningful results.

---

## 4. Appeal Path

<!-- Your criterion. -->

In each of the three trials, all 5 valid appeal requests must successfully update the submission's appeal status and create a record of the appeal.


**Why this target:**

I chose a 100% success rate because users should have a reliable way to challenge an incorrect AI classification. Every appeal should be recorded so that the process is transparent and can be reviewed later.

---

## 5. Bad Input Handling

<!-- Your criterion. -->

In each of the three trials, the system should reject all 5 invalid submissions with an HTTP 400 error and a clear JSON error message.

The test cases will include:
1. Missing text field
2. Empty text
3. Whitespace-only text
4. Text containing only punctuation
5. Text exceeding 10,000 characters



**Why this target:**


I chose a 100% rejection rate because invalid inputs should not be processed by the detection system. Clear error messages help users understand what went wrong and how to correct their submission.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
