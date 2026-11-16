# 00–10 min — LLMs and the problem

**Goal:** students can explain what a chat model does and why application context matters.

## Timing and speaking notes

- **0–2: Hook.** Ask: “Could a chatbot tell us the refund policy for a school
  created five minutes ago?” Take two answers.
- **2–5: Explain.** Say: “A language model predicts a response from its input and
  learned patterns. It is not automatically connected to our current documents.
  A fluent answer is not proof of a correct answer.” Define tokens as chunks of
  text; the context window limits how much input and output fits in a request.
- **5–8: Draw and discuss.** A prompt gives instructions and a question; a model
  returns a response. It may invent a plausible policy when the facts are missing.
  Temperature affects randomness, not truth. Model calls have latency, cost and
  data-sharing implications.
- **8–10: Check.** Ask: “How can we supply the new policy without retraining?”
  Expected: include relevant document text in the prompt. Preview retrieval.

```text
question + instructions ---> model ---> plausible answer
                                  ?       (not necessarily factual)
```

**Transition:** We could hand-write every API call, but reusable components make
the application easier to compose and inspect.
