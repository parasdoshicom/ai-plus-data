# Metric Trust Packet Template

Use this template for any metric that an AI assistant, analyst, dashboard, or executive review should treat as decision-critical.

The packet is intentionally small. It should be readable by a business owner, a data owner, and an AI assistant.

## Metric

- **Metric name:**
- **Business question it supports:**
- **Business owner:**
- **Data owner:**
- **Review status:** Draft / Benchmarked / Verified / Trusted
- **Last reviewed:**

## Official Definition

- **Plain-English definition:**
- **Formula:**
- **Numerator:**
- **Denominator:**
- **Grain:**
- **Time zone:**
- **Required filters:**
- **Required exclusions:**

## Trusted Source Path

- **Blessed dashboard, report, query, model, or semantic object:**
- **Source freshness expectation:**
- **Primary warehouse/model/table if relevant:**
- **Known upstream dependencies:**
- **Lineage or impact-analysis pointer:**

## Caveats

- **Known caveats:**
- **Segments where the metric is unreliable:**
- **Recent definition changes:**
- **Data quality watchouts:**

## Validation Rules

- **Expected range:**
- **Accepted tolerance versus trusted source:**
- **Regression checks:**
- **Minimum freshness required before answering:**
- **When to refuse or escalate:**

## Approved Answer Paths

List the recurring questions this metric should answer and the source path AI should use first.

| Recurring question | Approved source path | Clarify first? | Answer state | Review status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Answer State Rules

Use these states when reviewing answers:

| State | Use when | Required action |
| --- | --- | --- |
| Verified | The answer matches the approved path and validation rule | Save for reuse |
| Clarify | The question lacks grain, period, segment, or metric definition | Ask a narrowing question |
| Unanswered | The packet does not contain enough trusted context | Route to owner or backlog |
| Wrong | The answer conflicts with a benchmark, caveat, or owner review | Block reuse and repair the packet |

## Eval Questions

Create questions that test ambiguity, caveats, source choice, and refusal behavior.

1.
2.
3.
4.
5.

## Owner Review

- **Business owner signoff:**
- **Data owner signoff:**
- **Next review date:**
- **Open issues:**
