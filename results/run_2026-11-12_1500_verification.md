# Run log — verification

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-12 15:00

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 2. score spread AI |  |   |   |   |  |
| 2. score spread human |  |   |   |   |  |
| 1. my own writing |  |   |   |   |  |
| 3. label coverage |  |   |   |   |  |
| 5. bad input handling |  |   |   |   |  |
| 4. appeal path |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### score spread AI

**Trial 1**

```json
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

**Trial 2**

```json
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

**Trial 3**

```json
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

### score spread human

**Trial 1**

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

**Trial 2**

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

**Trial 3**

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

### my own writing

**Trial 1**

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

**Trial 2**

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

**Trial 3**

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

### label coverage

**Trial 1**

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
    "style_score": 0.5619047619047619,
    "combined_score": 0.530952380952381,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Good communication matters, but it doesn't always solve every problem."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5844961240310078,
    "combined_score": 0.5422480620155039,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Some teams work well together while others struggle even when everyone"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5703703703703704,
    "combined_score": 0.5351851851851852,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Technology can help people finish work faster, although it sometimes c"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5858156028368795,
    "combined_score": 0.5429078014184398,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "A manager should listen to employees and understand what is happening "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5719298245614035,
    "combined_score": 0.5359649122807018,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "There are different ways to measure success, and not everyone agrees o"
  }
]
```

**Trial 2**

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
    "style_score": 0.5619047619047619,
    "combined_score": 0.530952380952381,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Good communication matters, but it doesn't always solve every problem."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5844961240310078,
    "combined_score": 0.5422480620155039,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Some teams work well together while others struggle even when everyone"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5703703703703704,
    "combined_score": 0.5351851851851852,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Technology can help people finish work faster, although it sometimes c"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5858156028368795,
    "combined_score": 0.5429078014184398,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "A manager should listen to employees and understand what is happening "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5719298245614035,
    "combined_score": 0.5359649122807018,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "There are different ways to measure success, and not everyone agrees o"
  }
]
```

**Trial 3**

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
    "style_score": 0.5619047619047619,
    "combined_score": 0.530952380952381,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Good communication matters, but it doesn't always solve every problem."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5844961240310078,
    "combined_score": 0.5422480620155039,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Some teams work well together while others struggle even when everyone"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5703703703703704,
    "combined_score": 0.5351851851851852,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "Technology can help people finish work faster, although it sometimes c"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5858156028368795,
    "combined_score": 0.5429078014184398,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "A manager should listen to employees and understand what is happening "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5719298245614035,
    "combined_score": 0.5359649122807018,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "There are different ways to measure success, and not everyone agrees o"
  }
]
```

### bad input handling

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "sent": "   "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5,
    "combined_score": 0.5,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "!!!???..."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.9998400000000001,
    "combined_score": 0.5,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "sent": "   "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5,
    "combined_score": 0.5,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "!!!???..."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.9998400000000001,
    "combined_score": 0.5,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "sent": "   "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.5,
    "combined_score": 0.5,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "!!!???..."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5,
    "style_score": 0.9998400000000001,
    "combined_score": 0.5,
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion has been made about its authorship.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

### appeal path

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "8bf47f60-491c-442a-a877-3ce3c598b1ef",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "This is my original writing about teamwork and collaboration."
  },
  {
    "status": 200,
    "content_id": "dd0daa14-b3fc-49ab-914a-349b50b3c7a9",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "I believe managers should listen carefully to their employees."
  },
  {
    "status": 200,
    "content_id": "619e0ab7-7819-4769-bea1-f8e2f36485c3",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "Work-life balance is important for long-term employee well-being."
  },
  {
    "status": 200,
    "content_id": "05725751-179b-41f0-bb58-d09755ee3503",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "Clear communication helps teams avoid unnecessary confusion."
  },
  {
    "status": 200,
    "content_id": "8f0d4223-613b-486a-bc86-0b7696567971",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "Employees deserve recognition for the work they contribute."
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "2b0168a8-251e-47ea-9e07-c04b639c88c0",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "This is my original writing about teamwork and collaboration."
  },
  {
    "status": 200,
    "content_id": "e90be729-fde0-4cbb-9823-38f2c766f1c5",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "I believe managers should listen carefully to their employees."
  },
  {
    "status": 200,
    "content_id": "66487163-4a65-4f07-9845-f923068cc8c7",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "Work-life balance is important for long-term employee well-being."
  },
  {
    "status": 200,
    "content_id": "82f4da94-1454-4804-9f25-eb8031d62422",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "Clear communication helps teams avoid unnecessary confusion."
  },
  {
    "status": 200,
    "content_id": "32e3861d-d633-4fe6-b30f-4960d70eea21",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "Employees deserve recognition for the work they contribute."
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "6cc9309a-2146-495b-85f8-21049895e9bf",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "This is my original writing about teamwork and collaboration."
  },
  {
    "status": 200,
    "content_id": "e610843d-8081-4e9e-b9a3-f653c7130f7c",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "I believe managers should listen carefully to their employees."
  },
  {
    "status": 200,
    "content_id": "47bb554b-63a2-4f83-a1b2-a321f7e95e86",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "Work-life balance is important for long-term employee well-being."
  },
  {
    "status": 200,
    "content_id": "8d84f0f6-3739-45a1-b2c8-b24b5bf5c375",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "Clear communication helps teams avoid unnecessary confusion."
  },
  {
    "status": 200,
    "content_id": "c292d420-3226-4932-be46-45be92b1c597",
    "appeal_status_code": 200,
    "appeal_status": "under_review",
    "appeal_message": "Your appeal has been received and is now under review.",
    "appeal_logged": true,
    "passed": true,
    "sent": "Employees deserve recognition for the work they contribute."
  }
]
```
