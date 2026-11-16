# 40–50 min — Live demo: build a question-answering chain

**Goal:** build from one model call to a context-grounded answer, introducing one
LangChain idea per file. Prepare an OpenAI API key before class using the
[README](../README.md).

## Timing and speaking notes

- **40–41: Start with the model.** Open `demos/demo-01.py`. The question goes
  straight to `model.invoke`; the model returns a message, and `.content` is its text.
- **41–42: Add a prompt template.** Compare `demos/demo-02.py`. The template turns
  the question into model messages before the model call.
- **42–43: Parse the output.** Compare `demos/demo-03.py`. `StrOutputParser` turns
  the model message into plain text; `|` connects the steps.
- **43–46: Add retrieval.** Open `demos/demo-04.py`. The new idea is the small
  `retrieve` function: it selects one matching snippet and supplies it as context.
  The search is intentionally simple, not a general search system. The snippets
  are fictional, not real academy policy. Run:

  ```sh
  uv run --locked python demos/demo-04.py
  ```

- **46–48: Switch providers.** Open `demos/demo-05.py`. The prompt and chain stay
  the same; only the chat model changes. Run with the OpenAI key, then, if configured,
  set `LLM_PROVIDER=openrouter` and run again to compare.

  ```sh
  uv run --locked python demos/demo-05.py
  LLM_PROVIDER=openrouter uv run --locked python demos/demo-05.py
  ```

- **48–50: Check.** “Where did the 14-day fact come from?” The supplied snippet,
  not a built-in model memory. Ask what would need to change to replace the toy
  keyword lookup with a vector search.

All examples call the selected model API. If it is unavailable, explain the code
flow without claiming an answer was generated.
