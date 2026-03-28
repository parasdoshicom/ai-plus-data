# Funnel Leakage Analysis

AI is especially useful when a team knows there is leakage in a funnel but does not yet know where to focus.

This playbook turns that into a repeatable workflow.

## Goal

Find the biggest source of loss in a funnel, estimate the opportunity size, and identify the next investigation path.

## Basic Workflow

1. Define the funnel stages clearly.
2. Calculate conversion between each stage.
3. Measure change versus a benchmark period.
4. Split the leakage into a few major buckets.
5. Use AI to draft likely causes and follow-up queries.
6. Validate the highest-impact findings with trusted checks.

## Recommended Leakage Buckets

For most funnels, useful buckets include:

- never reached the next stage
- reached the next stage late
- dropped after qualification
- dropped after a product or pricing interaction
- segment-specific decline
- operational delay or system issue

## AI’s Best Role

AI can help by:

- drafting the initial analysis plan
- generating SQL for each bucket
- summarizing where the largest losses occur
- proposing follow-up segment cuts
- turning analysis into a short narrative for stakeholders

AI should not be trusted to invent stage definitions or business rules from scratch.

## Questions to Ask

- Which bucket explains the largest absolute loss?
- Which bucket changed most versus the prior period?
- Is the issue broad or concentrated in a few segments?
- What is the rough opportunity if the affected stage returns to baseline?
- Which operational signal best explains the observed drop?

## Opportunity Sizing

Do not stop at "conversion is down." Translate the leakage into something operationally useful, such as:

- extra signups needed to recover the gap
- incremental orders or contracts available at baseline performance
- revenue or margin impact at current mix

## Common Mistakes

- using aggregate trending data for stage-level diagnosis
- comparing different cohort definitions
- mixing volume and rate effects
- skipping denominator checks
- overfitting the explanation to the first visible segment

## Simple Output Format

```text
Largest leakage:
Offer to demo booking is the biggest source of loss this week.

What changed:
Conversion at that stage is down 6.4 points versus the trailing baseline.

Where it is concentrated:
Mostly on mobile and in the self-serve segment.

Estimated opportunity:
Returning to baseline would recover roughly 180 bookings per week.

Next step:
Review mobile scheduling friction and response-time delays for self-serve users.
```

That is enough to move a team from vague concern to focused action.
