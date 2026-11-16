# 40–50 min — Live demo: ask a fictional academy

**Goal:** trace a real question through retrieval, prompt, OpenRouter model and parser.
Prepare the environment and key before class using the [README](../README.md).

## Timing and speaking notes

- **40–42: Show the input.** Open `demo.py` and point to `DOCUMENTS`: four small,
  fictional policy snippets with labels. Say: “This is sample data, not a real policy.”
- **42–44: Reveal retrieval and prompt without an API call.**

  ```sh
  uv run --locked python demo.py --dry-run "How do I get a refund?"
  ```

  Show the `[refunds]` snippet and the system instruction. Explain that `prepare`
  passes the question to both `RunnableLambda(retrieve)` and `RunnablePassthrough`,
  then formats messages with `ChatPromptTemplate`.
- **44–47: Run live.**

  ```sh
  uv run --locked python demo.py "How do I get a refund?"
  ```

  Expect a paraphrase of “within 14 days of enrollment, email student support,”
  ideally citing `[refunds]`. Exact text and even correctness can vary; compare
  against the source rather than promising a specific answer. Point to
  `prepare | model | StrOutputParser()` and `.invoke`.
- **47–49: Test a different question and a gap.**

  ```sh
  uv run --locked python demo.py "When are Python workshops?"
  uv run --locked python demo.py "What is the parking fee?"
  ```

  The first should use `[schedule]`; the second has no matching snippet and should
  say it does not know. If it does not, call that a failure, not a feature. Use
  `--dry-run` on either to inspect the retrieved context.
- **49–50: Check.** “Where did the 14-day fact come from?” The supplied snippet,
  not a built-in model memory. Citations are generated text, not independently verified.

If the live service is unavailable, show dry-run outputs for all three questions,
explain that no answer was generated, and walk through the expected answer using
the snippets. Do not claim the model was called.
