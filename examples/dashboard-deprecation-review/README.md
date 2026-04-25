# Synthetic Dashboard Deprecation Review

This example shows how a data team can reduce AI confusion by removing or relabeling conflicting dashboards.

All names and metrics are synthetic.

## Scenario

Three dashboards answer versions of the same recurring question:

**"What happened to qualified signup conversion last week?"**

| Dashboard | Current use | Issue | Decision |
| --- | --- | --- | --- |
| Growth weekly review | Executive and manager review | Uses the approved definition | Keep and bless |
| Acquisition experiment dashboard | Experiment deep dives | Uses a narrower paid-only population | Keep, relabel as paid acquisition only |
| Legacy signup dashboard | Occasional ad hoc pulls | Uses an old denominator | Deprecate |

## Review Steps

1. Inventory all dashboards that claim to answer the same question.
2. Compare definitions, filters, time zones, freshness, and owners.
3. Pick the blessed artifact for the recurring executive question.
4. Relabel useful but narrower dashboards.
5. Deprecate stale dashboards that create conflict.
6. Update the metric trust packet so AI knows which source to trust first.

## Output

| Action | Owner | Due date | Evidence update |
| --- | --- | --- | --- |
| Bless Growth weekly review dashboard | Data owner | This week | Add to metric trust packet |
| Relabel Acquisition experiment dashboard | Growth analytics | This week | Add scope note to dashboard |
| Deprecate Legacy signup dashboard | BI owner | Next week | Replace links with blessed artifact |

## What Good Looks Like

- AI assistants cite the blessed dashboard first.
- Analysts stop reconciling the same denominator debate.
- Managers know which artifact belongs in weekly review.
- Narrow dashboards remain available but cannot masquerade as the official metric.

## Related Reads

- [`../../playbooks/dashboard-governance-for-ai-analytics.md`](../../playbooks/dashboard-governance-for-ai-analytics.md)
- [`../../projects/ten-metric-trust-layer-pilot.md`](../../projects/ten-metric-trust-layer-pilot.md)
- [`../metric-trust-packet/README.md`](../metric-trust-packet/README.md)
