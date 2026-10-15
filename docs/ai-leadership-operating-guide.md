# An operating guide for AI and data leaders

Use this guide to turn a broad AI mandate into a small portfolio of workflows that people can run, review, and improve. It combines the public operating patterns already in this repository. It is generalized guidance, not a company's strategy or a claim of a completed deployment.

## 1. Start with the decision and the existing work

For each candidate workflow, identify the person making the decision, how often it recurs, the current process, and the consequence of a wrong answer. Inspect what already works before adding another tool or reporting surface.

Write a [workflow investment brief](../toolkits/workflow-investment-brief.md). A useful candidate has a reachable source, a repeatable input, a checkable output, and someone willing to use the result. A vague ambition such as “transform the function” needs decomposition before it becomes an agent task.

Choose one candidate with a short feedback cycle. Defer work whose required access, business definition, or decision owner is unresolved. Record why it is deferred so a later review can reconsider it.

## 2. Establish the evidence and decision rights

Agree on the approved definitions, data boundaries, reviewer, and authority to act. Permission to analyze does not imply permission to publish, spend, change records, or contact someone.

| Decision | What to record |
| --- | --- |
| Which result counts? | Metric, denominator, observation window, baseline, and source |
| Which inputs can be used? | Approved source, access scope, freshness, and exclusions |
| Who reviews a miss? | Domain reviewer and escalation condition |
| Who can expand the pilot? | Decision owner and evidence required |
| When should work stop? | Quality, cost, access, or adoption condition |

Use the [metric trust packet](../toolkits/metric-trust-packet-template.md) for definitions. Keep unknowns visible. A missing measure is not a measured zero.

### Decision-rights worksheet

Fill in actual names privately; roles below describe decisions, not a required organization chart.

| Role | Decision it carries | Evidence it needs |
| --- | --- | --- |
| Business sponsor | Fund, narrow, expand, or stop the pilot | Business baseline, expected benefit, cost, and risk |
| Process owner | Accept the changed workflow and user handoff | Real use, exceptions, and the effect on existing work |
| Delivery lead | Ship a tested implementation | Acceptance cases, change record, and technical dependencies |
| Data steward | Approve definitions and source use | Meaning, lineage, permissions, and freshness |
| Control reviewer | Accept the applicable controls and exceptions | Risk assessment and observed permission/failure behavior |
| Service owner | Take responsibility after release | Monitoring, support route, fallback, and recovery rehearsal |
| Value reviewer | Classify the observed benefit | Baseline, denominator, comparison window, and attribution limits |

One person may hold several roles in a small pilot. Record that explicitly. Do not let a technical pass silently substitute for business acceptance or authority to act.

## 3. Prove the whole workflow

Run the path from input to decision-ready output. Include retrieval, analysis, verification, review, and any handoff that the real user needs. A demonstration that produces a plausible answer has not yet proved the operating workflow.

Compare against the current process on a small, representative set of cases. Include a normal case, missing context, conflicting evidence, an invalid input, and a case requiring review. Use the [evaluation scorecard](../toolkits/agentic-analytics-evaluation-scorecard.md) to record what passed and what did not run.

Measure elapsed time and human review effort separately. Include rework and support time in the comparison. Describe saved capacity as capacity until someone verifies how it was used; do not turn an estimate of time saved into realized revenue or cost reduction.

## 4. Earn each expansion

| Stage | Evidence needed before the next stage |
| --- | --- |
| One operator | The recurring question can be answered with the required evidence and limits |
| Small team | Another person can run it, recognize a miss, and complete the review handoff |
| Shared service | Permissions, support, cost limits, recovery, and ownership hold across actual users |

Do not build the organization-wide platform to avoid testing the small workflow. Preserve a known-working path while evaluating replacements. Compare reliability, quality, cost, and recovery effort before changing the default.

### A release packet another team can use

Keep a small versioned folder with the investment brief, workflow diagram, authority table, metric/source definitions, evaluation cases and results, change record, support runbook, and value record. Add a retention note specifying which traces and corrections may be saved, for how long, and who can reuse them. Permission to run a workflow is not permission to train on its records.

A release review should answer: can the user complete the task, can the reviewer detect a material miss, can support recover from a failure, and can the next team reproduce the evidence? Test the failure and fallback path as well as the successful path. Record which configuration, model, tools, retrieval rules, and memory behavior produced the result.

### Portfolio gate worksheet

| Gate | Minimum evidence | Possible decision |
| --- | --- | --- |
| Discovery | A recurring problem, a willing user, and a process owner | Investigate or decline |
| Feasibility | Accessible approved data, a baseline, and a simple alternative | Pilot, narrow, or stop |
| Release | Accepted workflow, checks, control review, and support readiness | Bounded release or repair |
| Expansion | Repeat usage, measured quality/value, and a successful handoff | Expand or hold |
| Retirement | Sustained non-use, unresolved degradation, or a better replacement | Retire with a safe transition |

Scale the evidence to the consequence of failure. The gates should expose a missing decision, not create paperwork that nobody uses.

## 5. Run a decision cadence

- **Weekly:** inspect one real run, the current constraint, and the next bounded improvement. Close or reassign outstanding actions.
- **Monthly:** review measured value, quality, adoption, support load, and operating cost. Decide Scale, Hold, Repair, or Stop for each pilot.
- **Quarterly:** revisit the portfolio and shared definitions. Retire stale assets before adding new ones.

Use the [decision memo](../projects/decision-memo-operating-loop.md) for choices and the [board brief](ai-adoption-board-brief.md) for executive review. Adoption counts are useful context; they do not by themselves establish business value.

### Measure depth of adoption

Use this scorecard as a starting template, with a consistent cohort and observation window.

| Measure | Definition to agree on | What it does not establish |
| --- | --- | --- |
| Workflow coverage | Eligible cases processed through the workflow / eligible cases | Quality or value |
| Repeat use | Users returning to the workflow / users with another eligible task | An endorsed business outcome |
| Acceptable outputs | Outputs meeting the agreed review bar / outputs reviewed | Performance on unreviewed cases |
| Exception burden | Cases requiring escalation / cases processed | Severity of each exception |
| Human effort | Review, correction, and support minutes per accepted result | Realized cash savings |
| Unit cost | Agreed build/run/support cost allocation per accepted result | Profitability |
| Business outcome | Existing process measure against its baseline and window | Causation without an appropriate comparison |

Report the counts behind each rate, skipped cases, and missing instrumentation. Keep forecast benefit, released capacity, avoided cost, and realized financial value as separate fields. The value reviewer should accept the category and evidence before it enters an executive scorecard.

## 6. Make feedback change the next run

A flagged answer needs a source, a description of the gap, and a reviewer. After review, update the canonical definition, approved example, permission rule, or check that caused the miss. Add a regression case and rerun it in a fresh session before calling the correction reusable.

Keep unreviewed feedback separate from approved context. Do not promote a confident agent summary into policy. Repeated instructions that can be enforced belong in a schema, validation step, or executable check; lessons requiring judgment need clear examples and review.

## A first-week sequence

1. Inventory the decisions and recurring workflows already in use.
2. Choose one candidate and capture its current baseline.
3. Complete the investment brief and confirm the data and action boundaries.
4. Run a small evaluation with independent checks.
5. Present one decision: continue, repair, or stop, with the next owner and date.

This is a proposed sequence. Adjust it to the organization's risk and review needs rather than claiming a fixed timeline guarantees readiness.

## Public foundations

[CDO operating system](cdo-operating-system.md) · [Operating cadence](../playbooks/ai-operating-cadence-for-data-leaders.md) · [Trusted answer lifecycle](../playbooks/trusted-answer-lifecycle.md) · [Close-the-loop template](../toolkits/analysis-close-the-loop-template.md) · [Hands-on workshop](https://parasdoshicom.github.io/world-class-agentic-analytics-in-production/)
