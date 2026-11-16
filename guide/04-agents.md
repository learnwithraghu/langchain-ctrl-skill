# 30–40 min — Tools, agents and boundaries

**Goal:** students can distinguish fixed workflows from model-directed tool use.

## Timing and speaking notes

- **30–33: Define.** A tool is a callable operation exposed with a name,
  description and inputs (for example, a calculator). The application executes
  the call and returns its result to the model. A tool call is not the model
  magically executing Python by itself.
- **33–36: Contrast.** In a fixed chain, the developer chooses the steps.
  An agent can choose whether and which tool to call, observe the result and
  continue, subject to application limits. Use a fixed chain when the path is
  known; use an agent when dynamic decisions justify the added cost and risk.
- **36–38: Safety.** Tool output and retrieved documents are untrusted data,
  potentially containing instructions. Limit permissions and iterations, validate
  inputs, require approval for consequential actions, and do not expose secrets.
  Prompt instructions alone are not a security boundary.
- **38–40: Check.** “Does today's demo use an agent?” No: Python always retrieves,
  formats and calls the model in the same order. No tool is model-selected.

```text
fixed:  question -> retrieve -> prompt -> model -> answer
agent:  question -> model -> [tool request -> application runs tool -> result] -> model
                              (may repeat, with limits)
```

Further reading: [LangChain agents](https://docs.langchain.com/oss/python/langchain/agents).
