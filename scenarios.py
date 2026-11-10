"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    
        {
        "name": "score spread AI",
        "criterion": 2,
        "texts": [
            "Artificial intelligence has transformed the way organizations manage information. By automating repetitive tasks, companies can improve operational efficiency while allowing employees to focus on strategic priorities.",
            "Effective leadership requires clear communication, accountability, and the ability to adapt to changing circumstances. Leaders who encourage collaboration can build stronger teams and improve organizational performance.",
            "Climate change presents significant challenges for communities around the world. Rising temperatures, shifting weather patterns, and environmental degradation highlight the importance of sustainable development.",
            "Digital transformation has become an essential component of modern business strategy. Organizations increasingly invest in cloud computing, data analytics, and automation to remain competitive.",
            "Education plays an important role in preparing individuals for an evolving workforce. Developing critical thinking, communication, and technical skills can help students navigate future career opportunities.",
            "Customer satisfaction is a key indicator of business success. Organizations that consistently gather feedback and improve service quality are better positioned to establish long-term customer relationships.",
            "Cybersecurity is a growing concern as businesses rely more heavily on digital infrastructure. Implementing strong security practices can reduce vulnerabilities and protect sensitive information.",
            "Successful project management depends on clearly defined objectives, realistic timelines, and effective stakeholder communication. Regular progress reviews help teams identify challenges and make necessary adjustments.",
            "Healthcare technology continues to evolve through advances in data analysis and digital services. These innovations have the potential to improve access to care and support better decision-making.",
            "Financial planning helps individuals establish realistic goals and make informed decisions about their resources. Consistent budgeting, saving, and monitoring can contribute to long-term financial stability.",
        ],
    },
        
    
     {
        "name": "score spread human",
        "criterion": 2,
        "texts": [
            "someone who listen and able to step in when needed instead of letting staff handles it themselves",
            "when accountability isn't there and toxic work environment with gossips and backstabbing",
            "good manager knows to guide the employees whereas bad managers take credits and use the employees for their own benefits",
            "worklife balance. without it, the stress added up overtime even with high salary, employees can't enjoy the benefit of it",
            "listen, appreciate and talk to them about their career growth",
            "skills set that isn't there",
            "collaboration, give and take",
            "talk to them and make them aware of it instead of going around talking to others about it.",
            "communication",
            "they have their own life, their own career aspiration",
        ],
    },
    
    
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "someone who listen and able to step in when needed instead of letting staff handles it themselves",
            "when accountability isn't there and toxic work environment with gossips and backstabbing",
            "good manager knows to guide the employees whereas bad managers take credits and use the employees for their own benefits",
            "worklife balance. without it, the stress added up overtime even with high salary, employees can't enjoy the benefit of it",
            "listen, appreciate and talk to them about their career growth",
            "skills set that isn't there",
            "collaboration, give and take",
            "talk to them and make them aware of it instead of going around talking to others about it.",
            "communication",
            "they have their own life, their own career aspiration",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            # 5 human-written samples
            "someone who listen and able to step in when needed instead of letting staff handles it themselves",
            "when accountability isn't there and toxic work environment with gossips and backstabbing",
            "skills set that isn't there",
            "collaboration, give and take",
            "communication",

            # 5 AI-generated samples
            "Artificial intelligence has transformed the way organizations manage information. By automating repetitive tasks, companies can improve operational efficiency while allowing employees to focus on strategic priorities.",
            "Effective leadership requires clear communication, accountability, and the ability to adapt to changing circumstances. Leaders who encourage collaboration can build stronger teams and improve organizational performance.",
            "Climate change presents significant challenges for communities around the world. Rising temperatures, shifting weather patterns, and environmental degradation highlight the importance of sustainable development.",
            "Digital transformation has become an essential component of modern business strategy. Organizations increasingly invest in cloud computing, data analytics, and automation to remain competitive.",
            "Education plays an important role in preparing individuals for an evolving workforce. Developing critical thinking, communication, and technical skills can help students navigate future career opportunities.",

            # 5 borderline or ambiguous samples
            "Good communication matters, but it doesn't always solve every problem.",
            "Some teams work well together while others struggle even when everyone has experience.",
            "Technology can help people finish work faster, although it sometimes creates new problems.",
            "A manager should listen to employees and understand what is happening before making decisions.",
            "There are different ways to measure success, and not everyone agrees on which one matters most.",
        ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    # {
    #     "name": "bad input",
    #     "criterion": 3,
    #     "bodies": [
    #         {"text": "", "creator_id": "eval_bad_empty"},
    #         {"creator_id": "eval_bad_missing"},          # no text field at all
    #         {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
    #         {"text": None, "creator_id": "eval_bad_null"},
    #     ],
    # },
    
    
    {
        "name": "bad input handling",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_missing_text"},
            {"text": "", "creator_id": "eval_empty_text"},
            {"text": "   ", "creator_id": "eval_whitespace"},
            {"text": "!!!???...", "creator_id": "eval_punctuation"},
            {"text": "word " * 2500, "creator_id": "eval_oversized"},
        ],
    },


    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
