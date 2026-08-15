# Trusted Answer Lifecycle for AI Analytics

Source access is only the beginning. A reliable analytics agent needs a governed route from the question to a reviewed answer path the next run can reuse.

## Use This When

- the same business question produces different answers across tools
- an agent can query data but cannot explain why its result should be trusted
- review feedback fixes one answer without improving the next run
- teams want recurring answers to become faster without weakening controls

## The Lifecycle

Use one lifecycle for every recurring, decision-relevant question:

`scope -> retrieve -> bind source -> execute -> validate -> record evidence -> review -> reuse -> measure`

Each stage has a distinct job.

| Stage | Required output | Failure to avoid |
| --- | --- | --- |
| Scope | Metric, period, segment, decision, and risk | Answering an ambiguous question |
| Retrieve | Small set of relevant approved context | Pulling every available document |
| Bind source | Named definition and allowed source path | Choosing a convenient source after seeing results |
| Execute | Query or retrieval result with run metadata | Claiming a plan executed the source |
| Validate | Checks for definition, freshness, arithmetic, grain, and caveats | Treating plausible output as correct |
| Record evidence | Compact record of what passed, failed, and remains uncertain | Saving a number with no audit trail |
| Review | Owner decision on the answer and proposed reusable route | Letting feedback rewrite shared context without approval |
| Reuse | Reviewed answer path with limits and expiry | Repeating discovery for a settled question |
| Measure | Offline quality, online correctness, reuse, and review burden | Using answer volume as the quality metric |

## Choose the Answer State Before Writing

Every run should enter one state before the agent polishes the response.

| State | Use when | Required action |
| --- | --- | --- |
| Answer | The route and validation checks pass | Return the answer with evidence and caveats |
| Clarify | Scope is missing or ambiguous | Ask for the smallest missing detail |
| Review | The route is plausible but lacks enough proof | Send the structured work to an owner |
| Refuse | The source is unsafe, stale, contradictory, or outside scope | Name the failed gate and the repair path |

A fluent answer does not get priority over the correct state. Clarification, review, and refusal are valid outcomes.

## Keep Planning Separate From Execution

An agent may prepare a strong route without running the source. The output should say which occurred.

Record at least:

- whether the source ran
- which source and definition were bound
- which context shaped the route
- which validation checks ran
- which checks passed or failed
- which caveats remain

This stops a recommended query from being mistaken for a verified result.

## Build a Compact Evidence Record

The evidence record should answer five questions:

1. What question did the agent answer?
2. Which approved context and source did it use?
3. What validation ran?
4. What remains uncertain?
5. What can a future run reuse?

Keep the record structured enough for evaluation and readable enough for an owner to review quickly.

## Review the Broken Part

Do not make reviewers rewrite the whole answer when one field failed. Let them correct the exact component:

- question scope
- metric definition
- source path
- filter or exclusion
- caveat
- answer state
- recommended reusable route

Positive feedback records evidence. Negative feedback creates review work. Neither should publish shared context without an owner decision.

## Promote Reuse Carefully

Save an answer path only when it includes:

- an owner
- approved definition and source
- validation rules
- known caveats
- freshness or expiry rule
- allowed question scope
- escalation conditions

Reuse should shorten the route while preserving the checks. It should not convert one successful answer into permanent truth.

## Measure the Whole System

Track four layers separately:

1. **Retrieval quality:** Did the agent find the required context?
2. **Application quality:** Did the required context affect the answer?
3. **Answer quality:** Was the answer state and result correct?
4. **Operating value:** Did reviewed reuse reduce time, source reads, or analyst interruptions?

This separation makes the fix easier to identify. A wrong answer may come from a missing artifact, retrieval miss, application error, query error, or source data problem.

## Monday-Morning Application

Pick one question from a weekly operating review. Run it through the lifecycle and save the evidence record. If the route passes owner review twice, convert it into a reusable answer path with an expiry rule. Add every novel failure to the eval set.

## Related Reads

- [`test-the-context-path.md`](./test-the-context-path.md)
- [`when-an-analytics-agent-should-not-answer.md`](./when-an-analytics-agent-should-not-answer.md)
- [`../toolkits/agentic-analytics-evaluation-scorecard.md`](../toolkits/agentic-analytics-evaluation-scorecard.md)
- [`../examples/trusted-answer-lifecycle/README.md`](../examples/trusted-answer-lifecycle/README.md)
