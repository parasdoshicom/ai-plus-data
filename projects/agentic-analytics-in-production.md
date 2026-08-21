# Build One Analytics Agent People Can Trust

## Outcome

Use this project to take one recurring analytics question from a personal workflow to a narrow, reviewable production pilot.

The full guided build, practice data, prompts, and workbook live in the public course companion:

**[World-Class Agentic Analytics in Production](https://parasdoshicom.github.io/world-class-agentic-analytics-in-production/)**

This page maps that course to the reusable AI+Data artifacts behind it.

## Choose The First Workflow

Start with a workflow that:

- repeats often enough to justify the work
- supports a named decision and decision owner
- already has a source or benchmark people trust
- returns a useful result consistently when a skilled person runs it
- has meaningful upside with contained downside if the agent is wrong

A recurring weekly or monthly review question is usually a better first candidate than a chatbot that promises to answer anything.

If people dispute the source, metric, or owner, repair that foundation first. An agent will expose the conflict; it will not settle it.

## Earn Each Level

| Level | What to build | Move on when |
| --- | --- | --- |
| Solo | One question, one approved source, one decision contract, a proof receipt, and a small eval set | The same person can repeatedly get a useful result, catch a known failure, and verify the evidence |
| Small team | Shared versioned context, a flagged-answer inbox, owner review, and a promoted correction | A second person can reproduce the result and reuse an approved correction in a fresh session |
| Production | Permissions, telemetry, versioned releases, review queues, rollback, cost controls, and an incident path | The route works across users, review demand is sustainable, and an owner can stop, repair, and safely resume it |

Do not build enterprise coordination infrastructure before one person has a workflow worth sharing.

## Build Path

| Step | Required output | Use this repo artifact |
| --- | --- | --- |
| 1. Frame the work | Question, decision, owner, frequency, risk, and success measure | [`playbooks/ask-before-building.md`](../playbooks/ask-before-building.md) |
| 2. Write the contract | Scope, authority, allowed sources, human boundary, and stop conditions | [`playbooks/trusted-answer-lifecycle.md`](../playbooks/trusted-answer-lifecycle.md) |
| 3. Bind approved meaning | Metric definition, grain, filters, exclusions, source, freshness, caveats, and owners | [`toolkits/metric-trust-packet-template.md`](../toolkits/metric-trust-packet-template.md) |
| 4. Test the context path | Required, eligible, retrieved, and applied context with a named failure layer | [`playbooks/test-the-context-path.md`](../playbooks/test-the-context-path.md) |
| 5. Run and prove the answer | Executed source, validation results, evidence, caveats, and uncertainty | [`examples/trusted-answer-lifecycle/README.md`](../examples/trusted-answer-lifecycle/README.md) |
| 6. Choose the response state | Answer, Clarify, Review, or Refuse | [`playbooks/when-an-analytics-agent-should-not-answer.md`](../playbooks/when-an-analytics-agent-should-not-answer.md) |
| 7. Turn failures into memory | Flagged answer, owner decision, narrow correction, regression case, and fresh-session rerun | [`playbooks/trusted-answer-lifecycle.md`](../playbooks/trusted-answer-lifecycle.md) |
| 8. Set the launch bar | Case-level results, quiet-failure rate, false blocks, reuse, review burden, latency, and cost | [`toolkits/agentic-analytics-evaluation-scorecard.md`](../toolkits/agentic-analytics-evaluation-scorecard.md) |
| 9. Operate the pilot | Owners, release stages, monitoring, rollback, incident path, and expansion decision | [`toolkits/data-team-ai-rollout-checklist.md`](../toolkits/data-team-ai-rollout-checklist.md) |

If you need a safe practice case before using an approved company source, start with [`examples/synthetic-funnel/README.md`](../examples/synthetic-funnel/README.md) or download the lab from the [course companion](https://parasdoshicom.github.io/world-class-agentic-analytics-in-production/#lab-kit).

## The Feedback Loop

The system should improve the shared answer path, not only the current chat.

`question -> approved context -> execution -> validation -> proof -> response state -> review -> correction -> regression test -> fresh-session reuse`

User feedback does not become shared truth on its own. A data or metric owner reviews the failure, approves the narrow correction, and promotes it into versioned context and evals. Duplicate reports should strengthen one repair instead of creating several competing rules.

## Before You Expand

Do not expand the pilot unless:

- no high-risk case is quietly wrong
- every known unsafe case blocks or escalates correctly
- no output claims a source ran without execution evidence
- repeated runs keep the approved route, caveat, and response state stable
- each failure has one owner and one repair layer
- a second person can reproduce the result without the original chat history
- review time and operating cost are visible enough to make an expansion decision

Track correct answers, correct clarifications, correct review escalations, and correct refusals separately. One blended score can hide the failure that matters most.

## Four-Week Pilot

### Week 1: Lock The Path

Choose the question, decision owner, metric owner, approved source, risk tier, manual baseline, and out-of-scope requests.

### Week 2: Build The Proof

Create the minimum context, proof receipt, eval cases, and launch bar. Test ambiguity, stale or conflicting sources, unsafe requests, and a known bad-data case.

### Week 3: Run In Shadow Mode

Run beside the current process. Review every output before it affects work. Measure answer quality, review burden, latency, source calls, and cost where available.

### Week 4: Release Narrowly

Give the route to a small set of decision makers. Sample live outputs, promote reviewed corrections, and decide whether to expand, hold, narrow, or stop.

## Evidence Boundary

A passing practice-data test, a working personal build, a team pilot, sampled live correctness, and a measured business outcome are different levels of evidence. State which one you have.

