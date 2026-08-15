# Synthetic Trusted Answer Lifecycle

This synthetic example follows one recurring metric question from clarification through validation, owner correction, and reviewed reuse.

## Scenario

A growth team asks:

> Why did qualified signup conversion fall last week?

The team already has a synthetic metric packet for qualified signup conversion. The approved source is complete through the prior business day.

## 1. Scope

The first request is missing two details:

- which week
- whether the team wants the total or a channel breakdown

The agent chooses **Clarify** and asks:

> Which reporting week should I use, and should I break the result out by channel?

The requester confirms the most recent complete week and asks for a channel breakdown.

## 2. Retrieve

Required context:

- qualified signup conversion definition
- approved weekly source route
- paid and organic channel rules
- freshness requirement
- known tracking caveat

The agent retrieves all five items and applies four. The tracking caveat does not apply because no tracking change occurred during the selected week.

## 3. Bind and Execute

The agent binds the approved weekly source and runs the synthetic route.

Illustrative result:

| Segment | Prior week | Current week | Change |
| --- | ---: | ---: | ---: |
| Total | 8.0% | 6.8% | -1.2 pp |
| Paid | 7.2% | 5.1% | -2.1 pp |
| Organic | 8.8% | 8.5% | -0.3 pp |

These values are fake and exist only for this example.

## 4. Validate

The agent checks:

- the same qualified-session definition appears in both periods
- both weeks are complete
- internal and bot traffic remain excluded
- paid and organic totals reconcile to the overall result
- no denominator jump crosses the metric packet's review threshold

All checks pass.

## 5. Record Evidence

```text
State: Answer
Question: Why did qualified signup conversion fall in the most recent complete week?
Result: The decline came primarily from paid traffic.
Source: Approved weekly conversion route
Validation: Definition, freshness, exclusions, and reconciliation passed
Caveat: This identifies the segment driving the change, not the campaign-level cause
Next step: Review paid campaign mix and landing-page completion by campaign
Reuse: Eligible after owner review
```

## 6. Review

The growth owner accepts the result but narrows the next step. Campaign mix review should come before landing-page diagnosis because spend shifted during the week.

The correction changes the recommendation, not the metric definition or result.

## 7. Reuse

The reviewed answer path now includes:

- the approved weekly source
- required paid and organic segmentation
- reconciliation checks
- campaign-mix check before landing-page diagnosis
- a freshness requirement
- an expiry date for owner review

The next run can reuse this route without skipping validation.

## 8. Add the New Failure Risk to Evals

Add one regression question:

> If paid conversion falls after a large spend-mix shift, should the agent recommend landing-page work before checking campaign mix?

Expected state: **Answer**, with campaign mix checked first.

## Context-Path Summary

| Measure | Result |
| --- | ---: |
| Required context retrieved | 5 / 5 |
| Relevant retrieved context applied | 4 / 4 |
| Correct answer state | Yes |
| Quietly wrong | No |
| Owner correction captured | Yes |
| Reviewed route saved | Yes |

## Related Reads

- [`../../playbooks/trusted-answer-lifecycle.md`](../../playbooks/trusted-answer-lifecycle.md)
- [`../../playbooks/test-the-context-path.md`](../../playbooks/test-the-context-path.md)
- [`../../toolkits/agentic-analytics-evaluation-scorecard.md`](../../toolkits/agentic-analytics-evaluation-scorecard.md)
- [`../metric-trust-packet/README.md`](../metric-trust-packet/README.md)
