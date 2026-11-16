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
   ```

2. Create an [OpenAI API key](https://platform.openai.com/api-keys). In your
   terminal (macOS/Linux), set it **without putting it in the command history**:

   ```sh
   read -rs OPENAI_API_KEY; export OPENAI_API_KEY; echo
   ```

   Paste the key and press Enter. In PowerShell, use
   `$env:OPENAI_API_KEY = Read-Host "OpenAI key"` in a private terminal. Never
   display, share, or commit the key. Run from a terminal that is not being
   projected when entering it.
3. Optionally create an [OpenRouter API key](https://openrouter.ai/keys) to compare
   providers in `demo-05.py`. Set it in macOS/Linux with
   `read -rs OPENROUTER_API_KEY; export OPENROUTER_API_KEY; echo` or in PowerShell
   with `$env:OPENROUTER_API_KEY = Read-Host "OpenRouter key"`. Then choose
   `openrouter` as the provider. The first four examples use OpenAI.
4. Rehearse a live call:

   ```sh
   uv run --locked python demos/demo-04.py
   uv run --locked python demos/demo-05.py
   ```

   `demo-05.py` uses OpenAI by default. To switch it to OpenRouter, set
   `LLM_PROVIDER=openrouter` (PowerShell: `$env:LLM_PROVIDER = "openrouter"`).
   Calls send the question and demo context to the selected provider. Use only the
   fictional sample data, never private student data. Check provider pricing and
   model availability before class. Clear API keys from the environment afterward.

## Files and constraints

The [demos](demos/) folder builds the idea in five short, runnable steps. Each file
stands alone and adds one LangChain concept to the previous example: model call,
prompt template, output parser, retrieval, then provider choice. The first four use
OpenAI; the last can use OpenAI or OpenRouter. Each makes a live model call with a
hard-coded question, so set the relevant API key first. Run the files in order:

```sh
uv run --locked python demos/demo-01.py
uv run --locked python demos/demo-02.py
uv run --locked python demos/demo-03.py
uv run --locked python demos/demo-04.py
uv run --locked python demos/demo-05.py
```

`demo-04.py` uses two fictional academy snippets and a tiny keyword lookup to
illustrate adding retrieved context. No vector database, embeddings, tool calls, or
autonomous agent are required.

If a call fails, check the key, internet access, selected model, account balance,
and rate limits. Do not paste error logs containing secrets into slides or chat.
