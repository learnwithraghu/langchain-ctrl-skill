# 50–60 min — Evaluate, improve, and wrap up

**Goal:** students can diagnose a retrieval or generation failure and propose a next step.

## Timing and speaking notes

- **50–53: Evaluate together.** For the refund question, compare the answer to
  `[refunds]`: is the 14-day window and email action present? Is the citation
  real? For the parking question, check that it admits insufficient information.
  A good-looking answer or citation alone is not evidence of correctness.
- **53–56: Diagnose.** Ask students to inspect `--dry-run` first. If the correct
  snippet is absent, improve retrieval; if present but the answer is wrong, examine
  the prompt/model. Keyword overlap is brittle: try a synonym such as “money back”
  and compare it with “refund.” A semantic retriever, curated evaluation set and
  citation verification are possible improvements, not features of this demo.
- **56–58: Discuss production concerns.** Mention prompt injection, access control
  on retrieved content, secret handling, provider data policies, costs, latency,
  tracing/redaction and regression tests. Never assume a prompt enforces security.
- **58–60: Exit ticket.** Ask each student: (1) What is the difference between
  LangChain and a model? (2) What does retrieval contribute? (3) When would an
  agent be more appropriate than a fixed chain? Expected: orchestration vs
  generation; relevant context; dynamic tool selection when justified.

```text
wrong answer?
  |-- wrong / missing context -> improve retrieval or sources
  `-- right context           -> inspect prompt, model and output validation
```

**Optional after class:** add a fictional snippet, rehearse a new question with
`--dry-run`, and write an evaluation case with the expected source and facts.
