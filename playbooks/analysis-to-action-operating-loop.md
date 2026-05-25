# Analysis To Action Operating Loop

AI-assisted analysis should not end with a clever answer, a chart, or a deck. It should end with a decision-ready recommendation and a follow-up plan.

This loop turns a vague question into a closed operating artifact:

1. frame the decision
2. design the analysis
3. run and validate the work
4. build the story
5. close the loop
6. save the reusable pattern

## Use This When

- a metric moved and the team needs to decide what to do
- a product or growth question has ambiguous scope
- an executive review needs a recommendation, not a data dump
- an AI analyst produced a finding that may change prioritization
- a team keeps revisiting the same question without a durable answer path

## Step 1: Frame The Decision

Start by asking what decision the analysis will inform.

Weak:

```text
Why is conversion down?
```

Stronger:

```text
Should we roll back the checkout change, invest in a fix, or treat the conversion drop as unrelated noise?
```

If the decision is not clear, do not run a deep dive yet. Convert the request into one of three lanes:

| Lane | Use when | Output |
| --- | --- | --- |
| Monitoring | The team wants a current read | One metric with comparison and threshold |
| Exploration | The team is forming hypotheses | Short finding list with caveats |
| Decision analysis | The team will act on the answer | Full analysis-to-action loop |

## Step 2: Design The Analysis

Before touching data, write a short analysis design spec.

Required fields:

- question
- decision
- data needed
- metric definition
- segments or cohorts to inspect
- time period and comparison period
- success criteria for the analysis
- known risks, confounders, or baseline gaps

The design spec prevents the common failure mode where AI moves fast on the wrong question.

## Step 3: Validate The Work

Validation is not a final polish step. It is the gate between analysis and recommendation.

Minimum checks:

- source table or reference path is trusted
- denominator matches the metric definition
- date range matches the question
- result ties out to a known dashboard, report, or prior baseline when one exists
- surprising result has at least one independent sanity check
- caveats are written plainly

If a finding would change a decision, validate it before turning it into a story.

## Step 4: Build The Story

The story should answer four questions:

1. What changed?
2. Why did it change?
3. Who or what is affected?
4. What should the team do next?

Cut anything that does not help the audience make the decision. A chart that does not change the recommendation belongs in the appendix or nowhere.

## Step 5: Close The Loop

Every recommendation needs a measurement contract.

Use this checklist:

| Field | Standard |
| --- | --- |
| Recommendation | The concrete action or decision path |
| Decision owner | One named person or role that can approve, reject, or defer |
| Decision deadline | The latest date the decision should be made |
| Success metric | The metric that will show whether the recommendation worked |
| Current baseline | The metric value before the action |
| Target | The expected value or threshold |
| Measurement window | When the metric should move |
| Follow-up owner | The person responsible for checking the result |
| Check-back date | The calendar date for review |
| Guardrail | The metric that must not degrade |
| Fallback | What the team will do if the result fails or is inconclusive |

If any field is missing, the recommendation is not done.

## Step 6: Save The Reusable Pattern

At the end, save what should compound:

- final decision
- metric definition or trust packet
- query or validation path
- known caveats
- correction log entry if AI made a mistake
- reusable prompt, skill, or checklist

The goal is not one good answer. The goal is a stronger operating system for the next answer.

## Anti-Patterns

- "We should monitor this" with no threshold or date.
- "Improve conversion" with no baseline.
- "Product owns it" with no named decision owner.
- "By Q3" when the metric needs a weekly read.
- A deck that presents evidence but never names the ask.
- A recommendation with no fallback if it fails.

## Related

- [`plan-review-execute-review.md`](./plan-review-execute-review.md)
- [`self-correcting-sql-loop.md`](./self-correcting-sql-loop.md)
- [`funnel-leakage-analysis.md`](./funnel-leakage-analysis.md)
- [`agent-patterns-are-table-stakes-trust-is-the-differentiator.md`](./agent-patterns-are-table-stakes-trust-is-the-differentiator.md)
- [`../toolkits/analysis-close-the-loop-template.md`](../toolkits/analysis-close-the-loop-template.md)
