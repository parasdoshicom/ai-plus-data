# Semantic Layer and Skill Files Are Complementary

One of the most useful lessons in AI analytics is that semantic layers and skill files solve different problems.

Teams often try to make one do the job of both.

That usually creates gaps.

## The short version

A semantic layer handles **what a metric is**.
A skill file handles **what the AI should watch out for**.

You usually need both.

## What the semantic layer is good at

A semantic layer is strong at:

- metric definitions
- relationships between tables
- reusable dimensions and measures
- governed query generation
- consistency across tools

This is the structural definition layer.

## What the skill file is good at

A skill file is strong at:

- edge cases
- filter rules
- caveats
- approved query patterns
- practical interpretation notes
- domain-specific guardrails

This is the operating context layer.

## Why one layer is not enough

A metric can be perfectly defined and still be misused.

For example, an AI system may know:

- the numerator
- the denominator
- the right source model

But still miss:

- which segments to exclude
- which timezone to use
- how to treat incomplete periods
- when a sudden move is mechanical rather than meaningful
- which known query pattern is safest for a recurring question

Those details are often the difference between a technically valid answer and a trusted business answer.

## Recommended split

### Put in the semantic layer

- official metric definitions
- source relationships
- dimensions and measures
- reusable governed logic
- structural query rules

### Put in skill files

- domain gotchas
- interpretation warnings
- temporary business rules
- operational caveats
- example queries
- “never do this” guidance

## Why this matters for AI

AI systems perform better when each layer has a clear job.

If everything is forced into the semantic layer, it becomes hard to maintain and weak at practical guidance.

If everything is forced into skill files, consistency and governance break down.

The two layers work best together:

- semantic layer for governed meaning
- skill files for business-safe execution context

## Bottom line

Do not treat semantic layers and skill files as substitutes.

Treat them as complementary layers in a reliable AI analytics stack.
