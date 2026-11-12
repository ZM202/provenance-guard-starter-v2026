# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-12 16:41
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `add3a441-3201-4390-935d-a8d15f0ab748` | unsure | 0.000 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `ca4fa204-a557-4e10-82b7-133091422309` | unsure | 0.000 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `1bf05bfa-29f5-4666-a5a2-f2cec4a6a62e` | unsure | 0.000 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `e734bcd1-acbd-45a2-98b2-4eecbc85aff1` | unsure | 0.000 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `178c65d4-304e-48f8-b637-b86f919ba41f` | unsure | 0.000 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `75c313f5-6563-446c-9f24-066519dcc7a6` | unsure | 0.000 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `32ec294f-840b-4827-8394-927d28bb0159` | unsure | 0.000 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `32db8d63-ce62-497c-bc5f-4c85156d0ca3` | unsure | 0.000 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `04178965-396c-457a-87d9-76a611e64aab` | unsure | 0.000 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `95713876-f17b-4e81-9ded-8d6808df9857` | unsure | 0.000 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ce1b85f6-a005-46c6-ac61-4537636ccd27` | unsure | 0.000 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `ba2b5a56-5034-4610-82e4-f1a1b981a428` | unsure | 0.000 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `beffe106-f7a8-4ad6-87a4-05422571b8fa` | unsure | 0.000 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `4137fe64-8acc-4e47-89cd-0f45c2e75deb` | unsure | 0.000 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `a7b4c583-c9c3-46ab-ba32-a4a0edd9568e` | unsure | 0.000 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `58a335fd-ab1b-4903-9c58-fdcc62bb4bd9` | unsure | 0.000 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `e9271621-f35a-4106-8151-31df22f3e2a4` | unsure | 0.000 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `d762ccf1-05ad-49e4-bb54-f143980991b1` | unsure | 0.000 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `15982837-c78a-4192-9b6c-e2dd6f5a1a45` | unsure | 0.000 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d37fc605-2352-4d1a-8839-0711129d9440` | unsure | 0.000 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `3cadb9e2-7e04-4dda-b9ec-9016af1d1629` | unsure | 0.000 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `cba3bb95-4fb4-4b8c-9b94-a88ac9d1db20` | unsure | 0.000 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `73d3f504-a31d-4f89-88f6-d83ffe74cf1f` | unsure | 0.000 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `4f110649-5e58-4b70-ba6d-1a941029afb9` | unsure | 0.000 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 200 | `98873ae3-12ff-46c4-af7b-00253f66f286` | unsure | 0.000 |  |
| MF03 | malformed | text is control characters | 200 | `69b0d6f4-b247-4e23-a76e-508f97122837` | unsure | 0.000 |  |
| MF04 | malformed | text is only punctuation | 200 | `36f7ae18-83c7-42a4-9c1a-4f1d8ea4bc15` | unsure | 0.000 |  |
| MF05 | malformed | text is a very long single word | 200 | `fa069cbb-9ded-4f06-9a50-1eeeeaaf0df3` | unsure | 0.000 |  |
| MF06 | malformed | text is emoji only | 200 | `6e2de180-7773-4a9f-a640-4db36dadeab6` | unsure | 0.000 |  |
| MF07 | malformed | text is right-to-left script | 200 | `73da4b62-c20f-4ef6-8aec-8a99ba3b4992` | unsure | 0.000 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `3987e47e-6569-4f0c-b1d3-67803e92f0d2` | unsure | 0.000 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `d1a7d79f-d5dd-4209-af94-0dc22894abf1` | unsure | 0.000 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1fa37056-6108-465a-95f4-8bd89f2034e8` | unsure | 0.000 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fdb16fc1-8f27-45a1-ab49-8ba0be16f863` | unsure | 0.000 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `36e54331-4612-4bc0-9b68-7cfe56e7bc3c` | unsure | 0.000 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7f0a020f-489e-43f0-a81a-8607728c6d7e` | unsure | 0.000 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e51e70ba-e062-4040-b6f7-e5fb658fe29b` | unsure | 0.000 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e408beed-12d0-4a8a-ab91-69c3f524ee05` | unsure | 0.000 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2f7ba4cb-cf22-4960-a9c2-d93b9cbd3cc5` | unsure | 0.000 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8c2bb4c6-acc0-451a-b790-2f9bcefc8d0c` | unsure | 0.000 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f543e822-db7b-42ec-9865-33993be922be` | unsure | 0.000 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `08251dcc-efc4-4ccc-ba57-33ee9b9bf957` | unsure | 0.000 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "add3a441-3201-4390-935d-a8d15f0ab748",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5651464192844675,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "ca4fa204-a557-4e10-82b7-133091422309",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.29864689965197533,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "1bf05bfa-29f5-4666-a5a2-f2cec4a6a62e",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.459273600195553,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "e734bcd1-acbd-45a2-98b2-4eecbc85aff1",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5572344508235738,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "178c65d4-304e-48f8-b637-b86f919ba41f",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.38199847132029924,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "75c313f5-6563-446c-9f24-066519dcc7a6",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.2833333333333333,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "32ec294f-840b-4827-8394-927d28bb0159",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.6497781692887195,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "32db8d63-ce62-497c-bc5f-4c85156d0ca3",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.4458372739845114,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "04178965-396c-457a-87d9-76a611e64aab",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.44940201220213777,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "95713876-f17b-4e81-9ded-8d6808df9857",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.706879966559558,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "ce1b85f6-a005-46c6-ac61-4537636ccd27",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5080092023250173,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "ba2b5a56-5034-4610-82e4-f1a1b981a428",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5972877784698627,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "beffe106-f7a8-4ad6-87a4-05422571b8fa",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5572392733134813,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "4137fe64-8acc-4e47-89cd-0f45c2e75deb",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5027107925933989,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "a7b4c583-c9c3-46ab-ba32-a4a0edd9568e",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.6244249497303398,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "58a335fd-ab1b-4903-9c58-fdcc62bb4bd9",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.4721443656555656,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "e9271621-f35a-4106-8151-31df22f3e2a4",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.4887631543641078,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "d762ccf1-05ad-49e4-bb54-f143980991b1",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.3156838081320012,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "15982837-c78a-4192-9b6c-e2dd6f5a1a45",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.3407714956844976,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "d37fc605-2352-4d1a-8839-0711129d9440",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.32391747713487185,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "3cadb9e2-7e04-4dda-b9ec-9016af1d1629",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.48145862666530326,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "cba3bb95-4fb4-4b8c-9b94-a88ac9d1db20",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.4719772787066631,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "73d3f504-a31d-4f89-88f6-d83ffe74cf1f",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.3684334968479066,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "4f110649-5e58-4b70-ba6d-1a941029afb9",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5139081182474052,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 200,
  "content_id": "98873ae3-12ff-46c4-af7b-00253f66f286",
  "creator_id": "attacker_MF02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.6000000000000001,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "69b0d6f4-b247-4e23-a76e-508f97122837",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.6000000000000001,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "36f7ae18-83c7-42a4-9c1a-4f1d8ea4bc15",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "fa069cbb-9ded-4f06-9a50-1eeeeaaf0df3",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.6000000000000001,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "6e2de180-7773-4a9f-a640-4db36dadeab6",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "73da4b62-c20f-4ef6-8aec-8a99ba3b4992",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "3987e47e-6569-4f0c-b1d3-67803e92f0d2",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "d1a7d79f-d5dd-4209-af94-0dc22894abf1",
  "creator_id": {
    "id": "x"
  },
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5259259259259259,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "1fa37056-6108-465a-95f4-8bd89f2034e8",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "fdb16fc1-8f27-45a1-ab49-8ba0be16f863",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "36e54331-4612-4bc0-9b68-7cfe56e7bc3c",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "7f0a020f-489e-43f0-a81a-8607728c6d7e",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "e51e70ba-e062-4040-b6f7-e5fb658fe29b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "e408beed-12d0-4a8a-ab91-69c3f524ee05",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "2f7ba4cb-cf22-4960-a9c2-d93b9cbd3cc5",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "8c2bb4c6-acc0-451a-b790-2f9bcefc8d0c",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "f543e822-db7b-42ec-9865-33993be922be",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "08251dcc-efc4-4ccc-ba57-33ee9b9bf957",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5,
  "style_score": 0.5757575757575758,
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
