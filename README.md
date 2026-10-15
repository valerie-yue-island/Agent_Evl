# Agent_Evl

A lightweight, model-agnostic harness for evaluating how well an AI agent performs on a given task.

**Why:** Most agent evals are one-off scripts tied to a specific model. This project treats evaluation like a data pipeline — test cases in, agent outputs, scores out — so the same harness can be reused across different agents and use cases.

**Who it's for:** Engineers who want a quick, reproducible way to measure an agent before and after a change.

## Quick start

```bash
uv run hello.py
```

Currently runs a fake (rule-based) agent so the pipeline can be built and tested without calling any LLM. Swapping in a real model only requires replacing `fake_agent()`.

## Roadmap
- [x] Project setup + fake agent
- [ ] Test case schema (JSONL)
- [ ] Runner
- [ ] Graders (exact match → LLM-as-judge)
- [ ] Report
