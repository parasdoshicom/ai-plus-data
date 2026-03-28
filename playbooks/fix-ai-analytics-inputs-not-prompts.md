# Fix AI Analytics Inputs, Not Prompts

**Thesis:** If AI analytics feels unreliable, the highest-leverage fix is usually better context and better inputs, not better phrasing.

## Use This When

- the same business question returns different answers depending on phrasing
- the model can access data but still chooses the wrong source or wrong logic
- the team is debating prompt tactics before cleaning up metric definitions

## Core Operating Pattern

Use a crawl / walk / run rollout:

1. **Crawl:** write structured metric context files for the top recurring questions
2. **Walk:** move trusted dashboard SQL and validated query patterns into version control
3. **Run:** expose governed definitions, lineage, ownership, and approved answer paths through a structured interface

The operating rule is simple: fix ambiguity upstream before scaling AI downstream.

## What AI Actually Needs

AI does not just need access to data. It needs access to structured, trusted inputs:

- definitions
- validated query patterns
- guardrails
- lineage
- ownership
- usage context

## Why Prompts Are The Wrong First Fix

- prompting can improve phrasing, but not solve conflicting definitions
- inconsistent upstream logic becomes confidently inconsistent output
- better prompts do not replace metric hygiene or operating discipline

## Common Failure Modes

- jumping straight to custom tooling before top metrics are defined
- treating the semantic layer as the entire solution
- overengineering retrieval before exposing trusted SQL
- forgetting edge cases like timezone, incomplete periods, or test-data exclusions

## Monday-Morning Rollout

1. Write context files for the top 10 business metrics.
2. Extract the SQL behind the dashboards people already trust.
3. Put those assets in version control.
4. Ask the same question five ways and compare the answers.
5. Fix context gaps before building more tooling.

## Related Next Reads

- [`semantic-layer-is-the-trust-layer.md`](./semantic-layer-is-the-trust-layer.md)
- [`why-agents-need-a-metric-store.md`](./why-agents-need-a-metric-store.md)
- [`../toolkits/metric-skill-file-template.md`](../toolkits/metric-skill-file-template.md)
