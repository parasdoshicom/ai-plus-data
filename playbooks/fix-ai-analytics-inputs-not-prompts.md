# Fix AI Analytics Inputs, Not Prompts

If your AI cannot reliably answer business questions, the problem is usually not the model.

It is the context layer the model sees before it answers.

## The failure pattern

Teams ask a simple question like:

- What is our conversion rate this week?
- Which metric moved most?
- What breaks if we change this table?

Then AI produces different answers depending on phrasing, source choice, or hidden assumptions.

That does not usually mean the model is broken.

It usually means the system has:

- ambiguous metric definitions
- multiple competing sources of truth
- dashboard logic trapped inside BI tools
- missing business rules, edge cases, and exclusion logic
- no portable context for timezone, fiscal calendar, or filter rules

## The key idea

AI does not just need access to data.

It needs access to **structured, trusted inputs**:

- definitions
- validated query patterns
- guardrails
- lineage
- ownership
- usage context

That is what makes answers repeatable.

## Why prompts are the wrong first fix

Prompting can improve phrasing.
It cannot solve foundational ambiguity.

If “conversion rate” means different things across teams, no prompt can consistently recover the right answer.

The real work is upstream.

## Crawl / Walk / Run

### Crawl: metric skill files
Start with structured text files that define your top metrics.

A good metric skill file should include:

- metric name
- business definition
- source table or trusted source
- required filters
- common gotchas
- example validated query
- guardrails such as joins to avoid or segments to exclude

This is the fastest safe way to improve answer quality.

Why it works:

- no new infrastructure required
- forces definition alignment
- easy to validate quickly
- immediately improves consistency

### Walk: dashboards as code
Move trusted dashboard SQL into version control.

The goal is simple:

- extract the logic your team already trusts
- keep it in Git
- let AI read raw validated queries
- keep the repo synced with the BI layer as dashboards evolve

This often works better than teams expect.

AI does surprisingly well when given the exact SQL behind trusted dashboards.

### Run: custom catalog + AI access layer
Only after Crawl and Walk are working should you build custom tooling.

At this stage, the system can expose:

- metric definitions
- lineage
- table ownership
- usage patterns
- trusted dashboard queries
- impact analysis context

This can be delivered through APIs, MCP tools, or another structured interface that AI can query directly.

## Why the semantic layer is not enough by itself

A semantic layer helps with:

- canonical definitions
- governed access
- consistent formulas

But AI also needs:

- real query patterns
- domain-specific business rules
- practical guardrails
- examples of how analysts actually answer recurring questions

A good rule of thumb:

**definitions are necessary, but not sufficient**

AI needs definitions + recipes + guardrails.

## What to measure first

Do not start by measuring only accuracy benchmarks.

First measure adoption and trust.

Questions that matter early:

- Are people actually using the system?
- Do they trust the answers enough to act on them?
- Do repeated phrasings return the same answer?
- Are analysts seeing fewer escalations on routine questions?

If adoption is weak at Crawl, building Run will not fix it.

## Common mistakes

### 1. Jumping straight to custom tooling
A custom AI catalog or MCP layer is attractive, but it is premature if top metrics are still loosely defined.

### 2. Treating the semantic layer as the whole solution
It handles formulas, not full operating context.

### 3. Overengineering retrieval
You often do not need RAG, embeddings, or a vector database to get started.

Trusted structured files and validated SQL can carry far more value than expected.

### 4. Ignoring edge cases
AI fails in the same places analysts do:

- timezone mismatches
- incomplete periods
- test-data contamination
- special-case segments
- near-real-time freshness issues

These need to be written down.

## Monday-morning rollout

1. Write skill files for the top 10 business metrics.
2. Extract SQL from the dashboards the team already trusts.
3. Put those queries in version control.
4. Ask the same question 5 ways and check whether AI returns 1 answer.
5. Fix context gaps before building more tooling.

## Bottom line

If AI feels unreliable in analytics, do not start by tweaking prompts.

Start by fixing the metrics layer and the context layer around it.

That means:

- clear definitions
- validated query patterns
- explicit guardrails
- portable business context
- structured access to trusted sources

Once those inputs are clean, the model becomes much more useful.
