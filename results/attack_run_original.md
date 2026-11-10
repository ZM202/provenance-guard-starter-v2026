# Attack run

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 11:33
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `14dac31c-1127-491b-b9d6-8a81bd6a6af5` | unsure | 0.000 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `359a9e9b-c26b-410f-8c8d-adca330359ad` | unsure | 0.000 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `3ec817cb-012f-4826-93ea-d259eb13f601` | unsure | 0.000 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `6dda8f57-24ce-469e-adf6-0ed7cb8a4a53` | unsure | 0.000 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `db9c3be4-1d8e-4348-a2ab-c1047997f2eb` | unsure | 0.000 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `47d1da41-9839-4ade-89c3-8f58855df81d` | unsure | 0.000 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `f29ea5e3-bb14-4730-bd40-92982366a025` | unsure | 0.000 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `fae4c369-0958-4902-8ae5-16a8e6d0bcba` | unsure | 0.000 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `06851480-bf4b-42ca-8f2e-6b16032ff73a` | unsure | 0.000 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `f102d61e-6049-4869-bb7f-2d75e07e71a2` | unsure | 0.000 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `b06c74ff-2bd0-4baf-813b-ecd84dfa9357` | unsure | 0.000 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `839cd2e9-f1a4-41f4-9777-edbc29427f9f` | unsure | 0.000 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `bbbe3b74-a65e-4023-a65e-ef0175aa38d9` | unsure | 0.000 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `11012970-e02a-4716-b36c-4151e78d584e` | unsure | 0.000 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `a144edfa-1f54-4f5e-8a73-89429cb4037e` | unsure | 0.000 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `fdc97cca-cda0-42fd-bf53-73688c880c2f` | unsure | 0.000 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `b8c6a513-a31e-45a6-bf5f-f59d1226bca3` | unsure | 0.000 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `9cc0f0f5-8044-494f-8ba6-720d13611e8c` | unsure | 0.000 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f6d82b70-1200-4d52-ad88-d13b9399fce4` | unsure | 0.000 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `8c09fd4c-1d50-4991-8a0a-301ab7052fb7` | unsure | 0.000 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f8ef3d3b-26bf-43cd-af7b-c7018d38982a` | unsure | 0.000 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `e7b856cd-67c6-4025-89ed-ff73c0369799` | unsure | 0.000 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `3f2ef3f9-0f12-4e7f-986e-a06362ca9cc9` | unsure | 0.000 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `f3d67a83-bcb9-4c68-b3d8-fca09224b953` | unsure | 0.000 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 200 | `498c8712-bbec-4041-a2c2-284c3c489908` | unsure | 0.000 |  |
| MF03 | malformed | text is control characters | 200 | `282facea-1956-4da4-b708-945fb0970baa` | unsure | 0.000 |  |
| MF04 | malformed | text is only punctuation | 200 | `c6c5fe64-8389-43b6-a923-1287c19a2351` | unsure | 0.000 |  |
| MF05 | malformed | text is a very long single word | 200 | `849a75f6-c9d4-41d3-81f4-d938fa3cc446` | unsure | 0.000 |  |
| MF06 | malformed | text is emoji only | 200 | `322bef09-f332-4a0e-b90f-2c0b68bb6d8f` | unsure | 0.000 |  |
| MF07 | malformed | text is right-to-left script | 200 | `5dd1ce54-3ae1-4476-bed4-794f9e144885` | unsure | 0.000 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `1ccf308c-3534-44b1-8c22-4fa630f78b6f` | ai | 0.650 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `c1699e65-2ffb-4a7a-8013-8f018a2657a0` | unsure | 0.000 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `426642f2-7278-49d4-a6ec-012f38986b32` | unsure | 0.000 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `11c07277-9bc2-42c4-a602-c20c3efbf42a` | unsure | 0.000 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `13c7a599-5c5e-4071-85b6-ff215510b5b8` | unsure | 0.000 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a29d96f3-9c8e-45ba-94ad-b66e943f4181` | unsure | 0.000 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9bd96e6c-d9c3-4230-8aba-c1b4727b567e` | unsure | 0.000 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `34264558-a77f-4f71-adec-e6b2ca2c8bf7` | unsure | 0.000 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `eb3d652a-7f31-4d79-bd50-9697d01ddb26` | unsure | 0.000 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9ff0a49a-32dc-42fb-b9dc-033309f15042` | unsure | 0.000 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5c344568-c3fe-4d63-8d05-f2695686d56d` | unsure | 0.000 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `93125dab-8293-4103-afcd-e5cdecb42ab9` | unsure | 0.000 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `81a72b2a-f974-44a5-b6dc-b4a3b96e1581` | unsure | 0.000 |  |
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
  "content_id": "14dac31c-1127-491b-b9d6-8a81bd6a6af5",
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
  "content_id": "359a9e9b-c26b-410f-8c8d-adca330359ad",
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
  "content_id": "3ec817cb-012f-4826-93ea-d259eb13f601",
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
  "content_id": "6dda8f57-24ce-469e-adf6-0ed7cb8a4a53",
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
  "content_id": "db9c3be4-1d8e-4348-a2ab-c1047997f2eb",
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
  "content_id": "47d1da41-9839-4ade-89c3-8f58855df81d",
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
  "content_id": "f29ea5e3-bb14-4730-bd40-92982366a025",
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
  "content_id": "fae4c369-0958-4902-8ae5-16a8e6d0bcba",
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
  "content_id": "06851480-bf4b-42ca-8f2e-6b16032ff73a",
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
  "content_id": "f102d61e-6049-4869-bb7f-2d75e07e71a2",
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
  "content_id": "b06c74ff-2bd0-4baf-813b-ecd84dfa9357",
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
  "content_id": "839cd2e9-f1a4-41f4-9777-edbc29427f9f",
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
  "content_id": "bbbe3b74-a65e-4023-a65e-ef0175aa38d9",
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
  "content_id": "11012970-e02a-4716-b36c-4151e78d584e",
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
  "content_id": "a144edfa-1f54-4f5e-8a73-89429cb4037e",
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
  "content_id": "fdc97cca-cda0-42fd-bf53-73688c880c2f",
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
  "content_id": "b8c6a513-a31e-45a6-bf5f-f59d1226bca3",
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
  "content_id": "9cc0f0f5-8044-494f-8ba6-720d13611e8c",
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
  "content_id": "f6d82b70-1200-4d52-ad88-d13b9399fce4",
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
  "content_id": "8c09fd4c-1d50-4991-8a0a-301ab7052fb7",
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
  "content_id": "f8ef3d3b-26bf-43cd-af7b-c7018d38982a",
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
  "content_id": "e7b856cd-67c6-4025-89ed-ff73c0369799",
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
  "content_id": "3f2ef3f9-0f12-4e7f-986e-a06362ca9cc9",
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
  "content_id": "f3d67a83-bcb9-4c68-b3d8-fca09224b953",
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
  "content_id": "498c8712-bbec-4041-a2c2-284c3c489908",
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
  "content_id": "282facea-1956-4da4-b708-945fb0970baa",
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
  "content_id": "c6c5fe64-8389-43b6-a923-1287c19a2351",
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
  "content_id": "849a75f6-c9d4-41d3-81f4-d938fa3cc446",
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
  "content_id": "322bef09-f332-4a0e-b90f-2c0b68bb6d8f",
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
  "content_id": "5dd1ce54-3ae1-4476-bed4-794f9e144885",
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
  "status": 200,
  "content_id": "1ccf308c-3534-44b1-8c22-4fa630f78b6f",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.65,
  "model_score": 0.5,
  "style_score": 0.8006977110073221,
  "label": "This writing shows patterns associated with AI-generated text. This is not proof that AI was used, and you may request a review if you disagree.",
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
  "content_id": "c1699e65-2ffb-4a7a-8013-8f018a2657a0",
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
  "content_id": "426642f2-7278-49d4-a6ec-012f38986b32",
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
  "content_id": "11c07277-9bc2-42c4-a602-c20c3efbf42a",
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
  "content_id": "13c7a599-5c5e-4071-85b6-ff215510b5b8",
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
  "content_id": "a29d96f3-9c8e-45ba-94ad-b66e943f4181",
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
  "content_id": "9bd96e6c-d9c3-4230-8aba-c1b4727b567e",
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
  "content_id": "34264558-a77f-4f71-adec-e6b2ca2c8bf7",
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
  "content_id": "eb3d652a-7f31-4d79-bd50-9697d01ddb26",
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
  "content_id": "9ff0a49a-32dc-42fb-b9dc-033309f15042",
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
  "content_id": "5c344568-c3fe-4d63-8d05-f2695686d56d",
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
  "content_id": "93125dab-8293-4103-afcd-e5cdecb42ab9",
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
  "content_id": "81a72b2a-f974-44a5-b6dc-b4a3b96e1581",
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
