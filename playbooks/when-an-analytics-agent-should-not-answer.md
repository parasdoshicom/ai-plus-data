# When an Analytics Agent Should Not Answer

**Thesis:** An analytics agent earns trust by blocking unsafe answers with the same consistency it uses to return valid ones.

## Use This When

- an agent answers from stale or contradictory sources
- stakeholders reward response speed more than decision quality
- the system has no clear rule for ambiguity or broken data
- reviewers discover plausible wrong answers after distribution

## Four Valid States

An agent should choose among answer, clarify, review, and refuse.

Use **clarify** when the question lacks a period, segment, grain, comparison, or metric definition.

Use **review** when the source route is plausible but the owner, benchmark, caveat, or validation remains unresolved.

Use **refuse** when the request cannot be answered safely with the available context. The refusal should name the failed check and the next repair step.

## Hard Refusal Gates

Refuse when any of these conditions holds:

- the requested source does not match the approved source for the metric
- freshness falls below the metric's minimum requirement
- required filters or exclusions cannot be applied
- two approved artifacts conflict and no precedence rule exists
- arithmetic, reconciliation, or known-range checks fail
- the request asks for action under unresolved high-impact ambiguity
- credentials, personal data, or restricted fields appear in the input
- the system has a plan but no evidence that the source ran

## Review Gates

Route to review when:

- a definition exists but has no current owner
- the question needs a novel join or segment
- the route passes technical checks but lacks business-context confirmation
- uncertainty is too wide for the decision at hand
- the agent found a possible correction that has not been approved

## A Useful Refusal Format

Keep refusals short and operational.

```text
State: Refuse
Failed gate: Source freshness
Observed: The approved source is incomplete for the requested period
Risk: A partial period would understate the result
Next step: Refresh the source or narrow the question to the last complete period
```

Do not bury the failed gate in a long apology. Do not offer an unverified number after refusing.

## Evaluate Blocking Quality

Track both sides:

- **Bad-data block rate:** How often did the agent stop a known unsafe answer?
- **False-block rate:** How often did it block a route that should have passed?

High blocking with no false-block measure can make a system safe but unusable. Low blocking can make it fast and quietly wrong.

## Match the Gate to the Stakes

| Risk tier | Example | Minimum gate |
| --- | --- | --- |
| Low | exploratory internal trend | source, freshness, and caveat checks |
| Medium | recurring operating review | approved route, validation, and owner review rule |
| High | finance, board, customer, or irreversible action | approved route, independent validation, named owner, and mandatory review |

The same numerical result may need a different answer state when the decision risk changes.

## Related Reads

- [`trusted-answer-lifecycle.md`](./trusted-answer-lifecycle.md)
- [`test-the-context-path.md`](./test-the-context-path.md)
- [`../toolkits/agentic-analytics-evaluation-scorecard.md`](../toolkits/agentic-analytics-evaluation-scorecard.md)
