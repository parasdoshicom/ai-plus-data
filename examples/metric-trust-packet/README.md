# Synthetic Metric Trust Packet

This completed packet uses synthetic data to show how the definition, source route, caveats, validation, ownership, and eval questions fit together.

## Metric

- **Metric name:** Qualified signup conversion
- **Business question it supports:** Are high-intent visitors completing signup at the expected rate?
- **Business owner:** Growth lead
- **Data owner:** Analytics engineering lead
- **Review status:** Verified
- **Last reviewed:** 2026-04-25

## Official Definition

- **Plain-English definition:** The share of qualified sessions that complete signup.
- **Formula:** completed_signups / qualified_sessions
- **Numerator:** sessions with completed signup event
- **Denominator:** sessions that meet the qualified traffic rule
- **Grain:** daily and weekly
- **Time zone:** business reporting time zone
- **Required filters:** exclude test accounts, internal traffic, and bot traffic
- **Required exclusions:** incomplete event payloads and known tracking outages

## Trusted Source Path

- **Blessed artifact:** Growth weekly review dashboard
- **Source freshness expectation:** complete through prior business day
- **Primary model:** synthetic_funnel_daily
- **Known upstream dependencies:** web events, account creation events, traffic quality classification
- **Lineage pointer:** dashboard metric tile to semantic definition to modeled table

## Caveats

- Paid and organic traffic should be reviewed separately during campaign mix changes.
- Mobile web completion is sensitive to tracking changes.
- Any denominator change above 15% week over week requires traffic-quality review before interpreting conversion.

## Validation Rules

- **Expected range:** 3% to 15%
- **Accepted tolerance versus dashboard:** 0.2 percentage points
- **Regression checks:** compare weekly result against prior approved dashboard export
- **Minimum freshness:** prior day complete
- **Escalate when:** source freshness is stale, dashboard and query disagree beyond tolerance, or campaign tagging changed during the period

## Approved Answer Paths

| Recurring question | Approved source path | Clarify first? | Trust state |
| --- | --- | --- | --- |
| Why did signup conversion change last week? | Weekly dashboard, segment by channel and device | Yes, confirm week and segment | Verified |
| Is paid traffic quality hurting conversion? | Traffic-quality report plus conversion dashboard | Yes, confirm paid channel definition | Benchmarked |
| Did mobile conversion move differently from desktop? | Device segment in weekly dashboard | No, unless date scope is missing | Verified |

## Eval Questions

1. Why did signup conversion drop last week?
2. Did paid traffic quality explain the change?
3. Is mobile web the issue, or is desktop also down?
4. Can we compare this week to the same week last quarter?
5. Should the assistant answer if dashboard freshness is two days behind?

## Example Context-Path Record

For the first eval question:

- **Required context:** official definition, weekly source route, channel rules, freshness rule, denominator-change caveat
- **Eligible context:** all five required items plus an unrelated campaign naming guide
- **Retrieved context:** all five required items
- **Applied context:** definition, source route, channel rules, and freshness rule
- **Expected answer state:** Clarify until the week and requested segment are confirmed
- **Primary failure layer if the agent answers immediately:** Application error

## Related Reads

- [`../../toolkits/metric-trust-packet-template.md`](../../toolkits/metric-trust-packet-template.md)
- [`../../projects/ten-metric-trust-layer-pilot.md`](../../projects/ten-metric-trust-layer-pilot.md)
- [`../synthetic-funnel/README.md`](../synthetic-funnel/README.md)
- [`../trusted-answer-lifecycle/README.md`](../trusted-answer-lifecycle/README.md)
