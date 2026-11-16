# 20–30 min — Retrieval-augmented generation (RAG)

**Goal:** students can explain how source text becomes model context and where it can fail.

## Timing and speaking notes

- **20–22: Set up.** Say: “RAG retrieves potentially relevant source material at
  question time, then asks a model to answer using that material. The model is not
  retrained and retrieval is not a truth guarantee.”
- **22–26: Draw the two paths.** In larger systems, documents are split into
  chunks and indexed ahead of time; a query retrieves some chunks, which are
  included with the question in the prompt. Semantic search often uses embeddings
  and a vector store. Explain embeddings as numeric representations useful for
  similarity search, not perfect meaning detectors.
- **26–28: Compare the demo.** It uses four prewritten fictional snippets and a
  deterministic keyword-overlap function returning at most two labeled snippets.
  There are no embeddings or vector store. It may miss synonyms or select an
  irrelevant chunk because of shared words.
- **28–30: Check.** Ask “What happens if the right chunk is missing?” The model
  cannot reliably infer the answer; ask it to say it does not know and inspect
  retrieval separately from generation.

```text
documents --> chunks --> index (prepared ahead of time)
question  --> retrieve relevant chunks --> prompt + question --> model --> answer
```

**Transition:** RAG is a fixed sequence; some problems require a decision about
which external action to take instead.
