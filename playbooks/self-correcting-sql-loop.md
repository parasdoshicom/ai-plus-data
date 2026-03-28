# Self-Correcting SQL Loop

One of the highest-leverage AI patterns for data work is a closed loop:

1. ask AI to write the first query
2. run it on safe data
3. feed the error or result back into the model
4. let it revise
5. review only once the query works and the logic makes sense

This approach turns AI from a one-shot generator into an iterative analyst partner.

## Why It Works

- Most of the time in analysis is lost in debugging, not in writing the first draft.
- SQL errors are structured feedback. Models improve quickly when they can see the exact failure mode.
- Humans are better used at the end of the loop, where they can validate the business logic instead of hand-fixing syntax.

## Safe Setup

Run this loop on one of the following:

- local DuckDB files
- sanitized CSV extracts
- sampled warehouse tables
- synthetic datasets

Avoid starting on production-scale tables or on data you do not understand well enough to validate.

## Recommended Operating Pattern

1. Define the business question in one sentence.
2. Provide schema context, including grain and key joins.
3. Ask the model to state assumptions before writing SQL.
4. Execute the SQL in a safe environment.
5. Return the exact error or surprising output.
6. Have the model revise.
7. Validate the final result against a known benchmark or a trusted dashboard.

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

## Validation Checklist

Before you trust the final output, check:

- grain: one row per what
- join logic: no accidental duplication
- null handling: explicit rather than implied
- time window: correct timezone and date boundary
- business definition: matches the metric the team actually uses

## Common Failure Modes

- The AI chooses the wrong grain and duplicates counts.
- The query is technically valid but answers a different question.
- Filters are dropped between iterations.
- A warehouse-specific function slips into a local SQL engine.

## Practical Advice

Use the loop on work you already know how to validate. That is where AI gives the most leverage with the least risk. The goal is not blind trust. The goal is faster iteration with stronger human review at the end.
