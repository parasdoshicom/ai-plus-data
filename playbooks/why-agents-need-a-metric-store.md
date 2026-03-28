# Why AI Analytics Agents Need a Metric Store

A semantic layer improves definitions.
A catalog improves discovery.
A skill file improves guardrails.

But once you start building conversational agents for business questions, you often discover one more missing layer:

A **metric store** for approved answers.

## The problem

An AI agent can be good at finding data and still be bad at answering correctly.

That usually happens when the agent can discover many plausible tables, dashboards, or query paths, but has no strong mechanism for choosing the approved one.

The result is familiar:

- the agent answers from the wrong table
- the answer is directionally reasonable but not official
- two tools give two different answers to the same question
- trust collapses even though the system feels technically impressive

## What a metric store does

A metric store sits between raw discovery and final answers.

For an important business question, it should know:

- the approved metric definition
- the preferred source table or model
- the approved SQL pattern or retrieval method
- required filters and exclusions
- caveats and interpretation warnings
- freshness expectations
- ownership and status

In other words, it does not just define the metric.
It defines the **approved answer path**.

## Why the semantic layer is not enough

A semantic layer is foundational, but its job is usually narrower:

- define metrics
- encode relationships
- support governed query generation

What it may not fully capture:

- practical query recipes analysts actually trust
- context-specific exclusions
- issue-specific caveats
- which answer path should win when multiple valid ones exist
- approved answer behavior for recurring executive questions

That is where a metric store becomes useful.

## How the layers fit together

A useful mental model:

### Semantic layer
What does the metric mean?

### Skill file / domain context
What should the AI watch out for?

### Catalog
Where can the AI find the relevant assets and lineage?

### Metric store
Which answer path is officially approved for this question?

### Agent
How do we turn all of that into a fast, usable experience?

## When you need this layer

You probably need a metric store if:

- an agent gives plausible but unofficial answers
- teams keep asking which source is right
- the same business question is asked repeatedly
- multiple dashboards or models are still in play
- you want an agent to answer with confidence and auditability

## What to store first

Do not start with everything.

Start with:

- top executive questions
- top recurring KPI questions
- metrics tied to real decisions
- metrics with known ambiguity or historical disagreement

For each one, encode the full approved answer path.

## Example shape

A metric store entry might contain:

- business question: "What is conversion this week?"
- official metric: `seller_conversion_rate`
- approved source: `seller_funnel_agg`
- approved query reference: `weekly_conversion.sql`
- required filters: exclude test data, use business timezone, ignore incomplete periods
- caveats: unstable on partial weekends, compare against matured cohorts for trend interpretation
- owner: revenue analytics
- status: official

## Why this matters for adoption

People do not adopt AI analytics because the architecture is elegant.

They adopt it when the same question returns the same trusted answer.

A metric store helps make that happen.

## Bottom line

If your AI analytics agent is conversationally strong but answer-quality weak, the missing piece may not be a better prompt or a bigger model.

It may be a metric store that defines the approved answer path between your semantic layer and your agent.
