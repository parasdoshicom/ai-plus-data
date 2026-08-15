# Agentic Analytics Evaluation Scorecard

Choose a fixed set of recurring business questions, then score the route, answer state, result, and operating behavior separately. A correct number can still arrive through an unsafe route.

## Eval Case Header

- **Case ID:**
- **Business question:**
- **Decision supported:**
- **Risk tier:** Low / Medium / High
- **Expected answer state:** Answer / Clarify / Review / Refuse
- **Expected result or range:**
- **Approved source route:**
- **Owner:**
- **Source snapshot date:**

## Context Path

- **Required context IDs:**
- **Eligible context IDs:**
- **Retrieved context IDs:**
- **Applied context IDs:**
- **Primary failure layer:** None / Missing asset / Retrieval miss / Context conflict / Application error / Query error / Source data error

## Route Checks

Mark each check Pass, Fail, or Not applicable.

| Check | Result | Evidence |
| --- | --- | --- |
| Scope includes period, segment, grain, and metric |  |  |
| Approved definition selected |  |  |
| Approved source selected |  |  |
| Freshness requirement met |  |  |
| Required filters and exclusions applied |  |  |
| Source execution confirmed |  |  |
| Arithmetic and reconciliation checks passed |  |  |
| Caveats surfaced near the claim |  |  |
| Answer state matches the expected state |  |  |
| Evidence record names passed and failed checks |  |  |

## Answer Review

Choose one outcome:

- Correct answer
- Correct clarification
- Correct review escalation
- Correct refusal
- Quietly wrong
- Loud failure

Then record:

- **Observed result:**
- **Difference from expected:**
- **Unsupported claim count:**
- **Reviewer correction:**
- **Proposed durable repair:**

## Efficiency And Stability

- **Context tokens:**
- **Source calls:**
- **Latency:**
- **Repeated-run state stability:**
- **Repeated-run result stability:**
- **Used a reviewed answer path:** Yes / No

## Aggregate Scorecard

Report these measures as separate lines.

| Measure | Formula |
| --- | --- |
| Retrieval recall | Required context retrieved / required context |
| Context precision | Relevant context retrieved / all context retrieved |
| Application rate | Relevant retrieved context applied / relevant context retrieved |
| Correct-state rate | Runs with the expected answer state / all runs |
| Quietly wrong rate | Plausible wrong answers / all runs |
| Bad-data block rate | Known unsafe cases blocked / known unsafe cases |
| False-block rate | Safe cases blocked / safe cases |
| Conditional correctness | Correct answers / runs with successful retrieval |
| Reviewed reuse rate | Runs using an approved answer path / eligible recurring runs |

## Release Gate

Set thresholds before running the eval. A sample gate:

- zero quietly wrong results in high-risk cases
- all known unsafe cases blocked
- no source execution claims without execution evidence
- correct answer state at or above the agreed threshold
- every new failure assigned to one repair layer

Do not use one blended score to hide a failure in a high-risk category.

## Production Follow-Through

Offline evals do not prove online correctness. Sample live answers by domain, risk tier, answer state, and saved-path use. Audit every high-risk output, then turn each new production failure into a safe regression case.
