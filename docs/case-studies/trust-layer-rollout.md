# Case Study: Rolling Out A Trust Layer For AI Analytics

## Situation

An organization wants better AI-assisted analytics, but the same business question still returns different answers depending on which dashboard, query, or analyst gets used.

Symptoms:

- metric definitions drift by team
- dashboards conflict
- AI answers are fast but not reliably trusted
- stakeholders ask which number is official

## Intervention

The rollout starts with the smallest useful trust layer:

1. choose the top recurring metrics
2. document one official definition for each
3. assign owners and caveats
4. reconcile trusted dashboards to those definitions
5. expose that context to AI workflows before broad rollout

## Before And After

| Dimension | Before | After |
| --- | --- | --- |
| Metric definitions | drift by team | one official definition per critical metric |
| Trusted source | ambiguous | named and governed |
| AI answers | fast but inconsistent | more repeatable across phrasings |
| Stakeholder trust | low | improving because ambiguity is reduced |

## Example Timeline

| Week | Operating move | Output |
| --- | --- | --- |
| 1 | Inventory recurring metric questions and conflicting dashboards | candidate top-10 metric list |
| 2 | Assign business and data owners | owner map and open definition gaps |
| 3 | Reconcile definitions and bless source paths | first verified metric packets |
| 4 | Add eval questions and review misses | trust review with expansion decision |

## Example Public-Safe Metrics

These numbers are synthetic, but the measurement pattern is the point.

| Measure | Start | 30-day target |
| --- | ---: | ---: |
| Critical metrics with named owner | 3 / 10 | 10 / 10 |
| Critical metrics with blessed source path | 2 / 10 | 8 / 10 |
| Repeated phrasing consistency | 70% | 90% |
| Reconciliation loops on pilot metrics | 14/month | <5/month |

## Signals Of Change

The organization gets a better base layer for both humans and AI:

- fewer reconciliation loops
- more consistent answers across phrasings
- clearer ownership of critical metrics
- higher confidence in AI-assisted workflows

## How To Measure The Shift

If you run this change for real, track:

- repeated-question consistency rate for the top metrics
- number of reconciliation loops on recurring KPI questions
- share of critical metrics with a named owner and official definition
- share of AI-assisted answers that cite an approved metric source

## Constraints And Tradeoffs

- The first 10 metrics must be narrow enough to govern. If every team gets to add "just one more," the pilot turns into catalog sprawl.
- A blessed source path is not always the same as the most complete source. Choose the source that is trusted for the decision forum.
- Some AI answers should escalate instead of answer. Refusal is a trust feature when freshness, caveats, or ownership are unclear.

## What Did Not Work

- Starting with broad warehouse chat before definitions were reconciled.
- Asking analysts to review every message instead of reviewing reusable answer paths.
- Treating dashboard cleanup as optional cleanup work. Conflicting dashboards were the root cause of many answer conflicts.

## Transferable Lesson

AI reliability usually improves more from stronger definitions and stronger context than from more elaborate prompting. Trust is built upstream.

## Related Reads

- [`../public-safe-impact-patterns.md`](../public-safe-impact-patterns.md)
- [`../../playbooks/semantic-layer-is-the-trust-layer.md`](../../playbooks/semantic-layer-is-the-trust-layer.md)
- [`../../playbooks/fix-ai-analytics-inputs-not-prompts.md`](../../playbooks/fix-ai-analytics-inputs-not-prompts.md)
