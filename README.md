# LangChain in one hour: instructor guide

A 60-minute theory + live demo for students comfortable with basic Python (functions,
dictionaries, and the command line). No previous LLM framework experience is assumed.
By the end, students should be able to explain a prompt–model–parser pipeline, trace a
retrieval-augmented answer, and describe when to use a tool or agent.

## Run of show

| Time | Block | Outcome |
|---|---|---|
| 00–10 | [LLMs and the problem](guide/01-llms.md) | Explain why model-only answers can fail |
| 10–20 | [LangChain building blocks](guide/02-building-blocks.md) | Trace prompt, model, and parser |
| 20–30 | [Retrieval and RAG](guide/03-retrieval.md) | Explain grounding and retrieval limitations |
| 30–40 | [Tools and agents](guide/04-agents.md) | Distinguish a fixed chain from an agent |
| 40–50 | [Live demo](guide/05-demo.md) | Run and inspect the Python chain |
| 50–60 | [Evaluation and wrap-up](guide/06-wrap-up.md) | Identify failures and next steps |

Each block includes timings, speaking notes, a diagram or board sketch, and a student
check. The diagrams are original text diagrams: copy them into slides or draw them on
the board. See [LangChain concepts](https://docs.langchain.com/oss/python/langchain/overview)
and [retrieval documentation](https://docs.langchain.com/oss/python/langchain/retrieval)
for further reading.

## Instructor preparation (before the hour)

1. Install Python 3.12+ and [uv](https://docs.astral.sh/uv/getting-started/installation/).
   From the repository root, run:

   ```sh
   uv sync --locked
   uv run --locked python -m unittest discover -s tests -v
   uv run --locked python demo.py --dry-run "How do I get a refund?"
   ```

2. Create an [OpenRouter API key](https://openrouter.ai/keys). In your terminal
   (macOS/Linux), set it **without putting it in the command history**:

   ```sh
   read -rs OPENROUTER_API_KEY; export OPENROUTER_API_KEY; echo
   ```

   Paste the key and press Enter. In PowerShell, use
   `$env:OPENROUTER_API_KEY = Read-Host "OpenRouter key"` in a private terminal.
   Never display, share, or commit the key. Run from a terminal that is not
   being projected when entering it.
3. Rehearse a live call:

   ```sh
   uv run --locked python demo.py "How do I get a refund?"
   ```

   The default is `openrouter/free`, whose availability and rate limits can change.
   Select a model available to your account with `export OPENROUTER_MODEL="provider/model"`
   (PowerShell: `$env:OPENROUTER_MODEL = "provider/model"`). Check
   [models and pricing](https://openrouter.ai/models) before using a paid model;
   API calls send the question and snippets to OpenRouter and its chosen provider.
   Use only the fictional sample data, never private student data.
4. Have the dry-run output ready in case of network, key, quota, or model failure.
   It displays the actual prepared messages **without** calling a model; it does not
   generate an answer. Clear your key from the environment after class (`unset
   OPENROUTER_API_KEY`, or `Remove-Item Env:OPENROUTER_API_KEY` in PowerShell).

## Files and constraints

`demo.py` uses four fictional academy snippets, a simple keyword retriever, a
`ChatPromptTemplate`, `ChatOpenRouter`, and `StrOutputParser` joined with LangChain
Expression Language (LCEL). The Python code and lockfile are intentionally small in
scope: no vector database, embeddings, tool calls, or autonomous agent are required.
`--dry-run` shows the exact prompt; `--help` lists options. Model answers are
non-deterministic and citations are requested, not verified.

If a call fails, check the key, internet access, selected model, account balance,
and rate limits. Retry with an available model or continue with `--dry-run`.
Do not paste error logs containing secrets into slides or chat.
