# Raw Queries Beat Overengineered Retrieval More Often Than Teams Expect

Before building a complicated retrieval system, give AI access to the validated SQL your team already trusts. That smaller move often produces useful results sooner.

## The common assumption

Teams often assume AI analytics needs one or more of the following before it can be reliable:

- RAG pipelines
- vector databases
- semantic search layers
- custom retrieval orchestration
- heavy metadata infrastructure

Sometimes those things help.

But very often, the highest-leverage input is much simpler:

**the exact SQL behind trusted dashboards and recurring analyses**

## Why this works

Trusted dashboard SQL already contains a large amount of real business judgment.

It usually encodes:

- the right tables
- the right joins
- the right filters
- the right time logic
- the logic people already act on

That is much more useful than generic table discovery.

If AI can read the query that already produces a trusted metric, it has a much better starting point for answering related business questions.

## What raw queries provide

Raw queries give AI something many analytics stacks otherwise hide:

- validated logic
- portable context
- repeatable patterns
- examples grounded in real work

This is especially valuable when SQL is otherwise trapped inside BI tools or scattered across analyst notebooks.

## When this is better than a more complex setup

Start with raw queries when:

- you already have dashboards your team trusts
- metric definitions are mostly stable
- analysts repeatedly answer similar questions
- AI is finding plausible but unofficial answers
- you want a fast path to better answer consistency

In those cases, moving trusted SQL into version control often creates immediate value.

## What to do in practice

1. Identify the dashboards or analyses people trust most.
2. Extract the underlying SQL.
3. Put it in version control.
4. Name it clearly by business question or metric.
5. Give AI access to those queries as approved reference patterns.
6. Keep the repo synced as dashboard logic changes.

## Important caveat

Raw queries are not a full substitute for semantic definitions or domain guardrails.

They work best alongside:

- metric definitions
- skill files or context files
- ownership and trust signals
- dashboard governance

But as a practical input layer, they are often far more useful than teams expect.

## Common mistake

A lot of teams overcomplicate early retrieval design.

They spend too long designing a sophisticated AI architecture before exposing the few artifacts that already encode trusted business logic.

That delays value and increases risk.

## Try This First

Put the raw, validated queries behind your most trusted dashboards in version control and make them available as approved references. Run that for a month before deciding you need a more elaborate retrieval layer.
