# Ask Before Building

A small but important AI habit for data teams: before generating a model, dashboard, analysis, or metric definition, ask clarifying questions first.

This is the difference between getting something fast and getting something useful.

## What to Ask

Before any meaningful build step, the model or operator should clarify:

- grain: one row per what
- user or stakeholder: who consumes this output
- source of truth: which tables or models matter
- success criteria: what "done" looks like
- edge cases: nulls, late-arriving data, deleted records, timezone issues
- refresh pattern: ad hoc, scheduled, or incremental
- required tests: uniqueness, accepted values, row counts, tie-outs

## Why It Matters

Many AI mistakes are not model failures. They are requirement failures.

If the workflow never pinned down grain, join strategy, or business definition, the model is forced to guess. Once it guesses, teams often lose time correcting the entire approach rather than a small implementation detail.

## Use This for

- dbt model generation
- metric specification
- dashboard rebuilds
- exploratory analysis
- semantic layer definitions
- AI-generated stakeholder readouts

## Short Question Set

Use this before the first build step:

1. What is the grain?
2. Which source is trusted for this output?
3. Who will use it and what decision will it support?
4. What are the edge cases that usually break this?
5. What tests or tie-outs must exist before shipping?

## Good Team Habit

If you are rolling AI out across a team, treat these questions as mandatory scaffolding rather than optional craftsmanship. The fastest reliable teams standardize their clarification step.

## Example

Bad request:

```text
Build me a customer retention model.
```

Better request:

```text
Build a weekly retention model with one row per signup cohort week.
Use signups as the source of truth for cohort assignment.
Use active sessions as the retained action.
Timezone is America/Los_Angeles.
We need a 12-week retention curve and tests for duplicate cohorts and null cohort dates.
```

The second request gives AI enough structure to help, rather than improvise.
