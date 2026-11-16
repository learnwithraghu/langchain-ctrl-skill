# 10–20 min — LangChain building blocks

**Goal:** students can describe the data flowing through a LangChain pipeline.

## Timing and speaking notes

- **10–12: Why LangChain?** Say: “LangChain provides interfaces for prompts,
  chat models, retrieval and tools. It orchestrates model calls; it is not itself
  the model or a guarantee of accuracy.” OpenRouter routes API requests to models
  from providers; the API key belongs to OpenRouter.
- **12–16: Walk the chain.** A `ChatPromptTemplate` formats messages from inputs;
  `ChatOpenRouter` sends them to a selected model; `StrOutputParser` extracts text
  from the model message. The `|` operator composes runnables in order; `.invoke`
  executes the chain. Inputs and outputs must match between steps.
- **16–18: Board exercise.** Ask students to point out which step needs a network
  and which substitutes variables. In the demo only the model call needs the network.
- **18–20: Check.** “If we change provider, which component changes?” Usually the
  model integration/configuration, while prompt and parser can remain.

```text
{question, context} --> prompt template --> chat model --> text parser --> answer
                           messages          API call       string
```

**Caveat:** providers and models differ in features, costs, and response behavior;
an interface does not make them identical. See the [OpenRouter integration](https://docs.langchain.com/oss/python/integrations/chat/openrouter).
