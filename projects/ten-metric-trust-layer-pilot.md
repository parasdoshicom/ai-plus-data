# 10-Metric Trust Layer Pilot

## Purpose

Use this as the first practical project for a data leader who wants AI analytics without metric chaos.

The pilot asks one forcing question:

**Which 10 metrics must always return the same answer?**

Those 10 metrics become the starting trust layer for AI-assisted analysis: definitions, owners, blessed artifacts, caveats, validation rules, approved answer paths, and eval questions.

## Why This Works

Broad "chat with the warehouse" launches fail when the organization has unresolved definitions, dashboard sprawl, unclear ownership, or weak review habits.

A 10-metric pilot is better because it is:

- small enough to finish
- important enough to matter
- concrete enough for executives to understand
- narrow enough to govern
- reusable across Slack, docs, dashboards, notebooks, and AI assistants

## Ideal Starting Point

Pick one decision forum, not the whole company.

Good first forums:

- weekly business review
- revenue or pipeline review
- growth funnel review
- product activation review
- retention or churn review
- executive operating review

Avoid starting with generic self-serve analytics, one-off dashboard requests, or a domain where nobody owns the official metric definitions.

## Pilot Scope

| Item | Target |
| --- | --- |
| Metrics | 10 decision-critical metrics |
| Eval questions | 30 recurring business questions |
| Business surface | 1 recurring decision forum |
| Review loop | weekly answer-quality review |
| Expansion rule | expand only after the first 10 earn trust |

## Metric Trust Packet

Every pilot metric should have a short packet with:

- metric name
- official definition
- business owner
- data owner
- grain and time zone
- filters and exclusions
- blessed dashboard, query, model, report, or semantic object
- source freshness expectation
- known caveats
- validation tolerance
- approved answer path for recurring questions
- clarification rules
- refusal or escalation rules
- review status

Use [`toolkits/metric-trust-packet-template.md`](../toolkits/metric-trust-packet-template.md) to create the packet.

## Operating Loop

1. Select one decision forum where recurring metric questions already matter.
2. Name the 10 metrics that must return consistent answers.
3. Assign a business owner and data owner for each metric.
4. Reconcile the official definition, grain, filters, and caveats.
5. Bless the source AI should trust first.
6. Write approved answer paths for recurring questions.
7. Create eval questions that test ambiguity, caveats, and source choice.
8. Run the pilot in the actual workflow.
9. Review misses weekly.
10. Promote repeated verified answers into reusable operating knowledge.

## Success Criteria

The pilot is working when:

- leaders can name the official 10 metrics
- each metric has an owner and trusted artifact
- AI answers or clarifies against approved context
- wrong answers are caught by evals or review
- at least one repeated business question becomes faster and safer than the old analyst queue
- the decision forum spends less time debating definitions and more time deciding what to do

## Related Reads

- [`playbooks/semantic-layer-is-the-trust-layer.md`](../playbooks/semantic-layer-is-the-trust-layer.md)
- [`playbooks/why-agents-need-a-metric-store.md`](../playbooks/why-agents-need-a-metric-store.md)
- [`playbooks/dashboard-governance-for-ai-analytics.md`](../playbooks/dashboard-governance-for-ai-analytics.md)
- [`toolkits/metric-trust-packet-template.md`](../toolkits/metric-trust-packet-template.md)
