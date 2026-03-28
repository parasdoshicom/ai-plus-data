# Self-Correcting SQL Loop

**Thesis:** The most reliable way to use AI for SQL is not one-shot generation. It is a closed loop with execution feedback and human validation at the end.

## Use This When

- you want faster analysis on work you already know how to validate
- the model can write a first draft, but still needs help getting details right
- you are working on local, sampled, sanitized, or synthetic data

## Core Operating Pattern

1. Define the business question in one sentence.
2. Provide schema context, including grain, key joins, and naming conventions.
3. Ask the model to state assumptions before writing SQL.
4. Run the query in a safe environment.
5. Return the exact error or surprising output to the model.
6. Repeat until the query works and the logic makes sense.
7. Validate the final result against a trusted benchmark, dashboard, or known answer.

## Why It Works

- most analysis time is lost in debugging, not in writing the first draft
- SQL errors are structured feedback that models can use well
- human review is most valuable at the end, where business logic can be checked

## Safe Setup

Run this workflow on:

- local DuckDB files
- sanitized CSV extracts
- sampled warehouse tables
- synthetic datasets

Avoid starting on production-scale or business-critical data you cannot confidently validate.

## Common Failure Modes

- wrong grain creates duplicated counts
- the query is valid but answers a different question
- filters or time windows change between iterations
- warehouse-specific syntax slips into the wrong execution engine

## Good Prompt Skeleton

```text
You are helping with a data analysis task.

Question:
Why did weekly conversion fall in the last four weeks?

Tables:
- sessions: one row per session
- signups: one row per signup
- orders: one row per order

Before writing SQL:
- state the grain you plan to use
- list the joins you expect
- call out any assumptions

Then write a DuckDB-compatible query.
```

## Related Next Reads

- [`ask-before-building.md`](./ask-before-building.md)
- [`fix-ai-analytics-inputs-not-prompts.md`](./fix-ai-analytics-inputs-not-prompts.md)
- [`../examples/synthetic-funnel/README.md`](../examples/synthetic-funnel/README.md)
