# Ask Before Building

**Thesis:** Most AI mistakes in data work are requirement failures, not model failures. Clarify first, then build.

## Use This When

- generating dbt models, dashboards, metrics, analyses, or AI readouts
- the request is underspecified and the model would otherwise guess
- you want team-wide consistency in how work gets scoped

## Core Operating Pattern

Before any meaningful build step, clarify:

1. What is the grain?
2. Which source is trusted?
3. Who will use this and what decision will it support?
4. Which edge cases usually break this?
5. What tests, tie-outs, or review steps are required before shipping?

Treat this as mandatory scaffolding, not optional craftsmanship.

## Why It Matters

- AI fills missing requirements with guesses
- small definition gaps can invalidate the entire output
- standardized clarification improves both speed and trust

## Short Question Set

Use these prompts before the first build step:

1. What is the grain?
2. Which source is trusted for this output?
3. Who will use it and what decision will it support?
4. What edge cases matter here?
5. What tests or tie-outs must exist before shipping?

## Common Failure Modes

- the request never defines the metric or time boundary
- source-of-truth ambiguity causes two plausible but different answers
- the team discovers edge cases only after the artifact is shared
- testing expectations stay implicit until the end

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

## Related Next Reads

- [`self-correcting-sql-loop.md`](./self-correcting-sql-loop.md)
- [`fix-ai-analytics-inputs-not-prompts.md`](./fix-ai-analytics-inputs-not-prompts.md)
- [`../toolkits/data-team-ai-rollout-checklist.md`](../toolkits/data-team-ai-rollout-checklist.md)
