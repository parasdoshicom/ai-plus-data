# Evaluate the Context Path

An answer-level eval tells you whether the output was right. A context-path eval shows where the route broke: availability, retrieval, conflict, application, query logic, or source data.

## Use This When

- the correct definition exists but the agent still misses it
- teams keep adding documents after wrong answers
- retrieval metrics look healthy while answers remain inconsistent
- a large context bundle makes it hard to locate the failure

## Track Four Context Sets

For every golden question, record:

- **Required context:** artifacts needed for a defensible answer
- **Eligible context:** relevant artifacts available before the run
- **Retrieved context:** artifacts the agent pulled
- **Applied context:** artifacts that changed the answer, caveat, state, or refusal

These sets separate availability, retrieval, and use.

## Classify the Failure Layer

Use one primary failure class and add a secondary class only when needed.

| Failure class | Meaning | Typical repair |
| --- | --- | --- |
| Missing asset | The required definition, caveat, or route does not exist | Create and review the missing artifact |
| Retrieval miss | The artifact exists but the agent did not pull it | Repair ranking, filters, or routing |
| Context conflict | Two eligible artifacts disagree | Resolve ownership, status, or precedence |
| Application error | The agent retrieved the right context but ignored or misused it | Improve instructions, structure, or evals |
| Query error | The source route or calculation was wrong | Fix the query and add a regression case |
| Source data error | The source itself is stale, incomplete, or inconsistent | Block the answer and repair upstream data |

This classification prevents a common waste pattern: adding more context when the right context already existed.

## Report the Funnel

Keep these measures beside final answer correctness:

```text
retrieval recall = required context retrieved / required context
context precision = relevant context retrieved / all context retrieved
application rate = relevant retrieved context applied / relevant context retrieved
conditional correctness = correct answers / runs with successful retrieval
```

Do not merge them into one score. A team needs to see whether the system found too little, pulled too much, or failed to use what it found.

## Run Context Ablations

Treat context bundles like tested product features. Hold the question, source snapshot, model class, temperature, and permissions constant. Compare:

1. minimal approved context
2. full approved context
3. full context minus one bundle
4. one-bundle-added runs when needed

Measure:

- correct answer state
- correct result
- quietly wrong rate
- context tokens
- latency
- source calls
- stability across repeated runs

A useful bundle reduces the probability of a quietly wrong answer enough to justify its cost and conflict risk.

## Freeze Production Misses Into Evals

When review finds a new failure:

1. preserve a safe snapshot of the question and expected route
2. remove sensitive values
3. add the failure to the eval set
4. prove the proposed fix changes the failed layer
5. rerun nearby cases to catch regressions

This turns review work into a compounding reliability asset.

## Related Reads

- [`trusted-answer-lifecycle.md`](./trusted-answer-lifecycle.md)
- [`../toolkits/context-ablation-test-template.md`](../toolkits/context-ablation-test-template.md)
- [`../toolkits/agentic-analytics-evaluation-scorecard.md`](../toolkits/agentic-analytics-evaluation-scorecard.md)
