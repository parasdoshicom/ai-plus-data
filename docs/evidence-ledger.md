# Evidence Ledger

Use this ledger to trace a public-facing statement to its supporting artifact or source, then read the caveat before repeating the claim.

## Evidence Strength

| Strength | Meaning |
| --- | --- |
| Direct repo artifact | Demonstrated directly by files in this repo |
| Public external source | Supported by a public third-party, professional-body, company-authored, or self-authored source |
| Inference | Reasonable conclusion from artifacts, but not independently proven |
| Not stated | Deliberately excluded from public statements |

## Ledger

| Statement | Where it appears | Evidence | Strength | Caveat |
| --- | --- | --- | --- | --- |
| The repo contains a coherent operating thesis for AI-native data leadership | [`README.md`](../README.md), [`evidence-and-scope.md`](./evidence-and-scope.md) | README, operating-system guide, playbooks, toolkits | Direct repo artifact | Quality still depends on reader judgment |
| The repo is public-safe by design | [`README.md`](../README.md), [`repo-privacy-policy.md`](./repo-privacy-policy.md) | Privacy policy, publication checklist, synthetic examples | Direct repo artifact | Manual ZIP/upload outside git could bypass safeguards |
| The 2026 public-work archive contains 34 verified channel publications through August 3 | [`../publications/2026.md`](../publications/2026.md) | Public LinkedIn activity records and Insight Extractor RSS entries | Public external source | Channel count includes cross-platform releases of the same underlying idea |
| Paras has a long-running public writing archive | [`README.md`](../README.md), [`public-source-inventory.md`](./public-source-inventory.md) | Insight Extractor archive | Public external source | Archive metrics are self-published on the site |
| Paras has senior analytics/community recognition | [`external-evidence-of-impact.md`](./external-evidence-of-impact.md) | Institute of Analytics profile, Evanta page, Globee pages | Public external source | Recognition does not by itself prove current operating scope |
| AI analytics needs trusted metric/context infrastructure before broad rollout | [`playbooks/semantic-layer-is-the-trust-layer.md`](../playbooks/semantic-layer-is-the-trust-layer.md), [`projects/ten-metric-trust-layer-pilot.md`](../projects/ten-metric-trust-layer-pilot.md) | Repo argument plus public research notes | Direct repo artifact | This is an operator thesis, not a universal law |
| A 10-metric trust layer is a practical first pilot | [`projects/ten-metric-trust-layer-pilot.md`](../projects/ten-metric-trust-layer-pilot.md) | Generalized pattern from adjacent work and repo playbooks | Direct repo artifact | Public repo does not state that a named customer deployed this exact pilot |
| Decision memos improve executive use of AI-assisted analysis | [`projects/decision-memo-operating-loop.md`](../projects/decision-memo-operating-loop.md), [`sample-monthly-cdo-review.md`](./sample-monthly-cdo-review.md) | Repo artifact and synthetic example | Direct repo artifact | External adoption examples would make this stronger |
| The repo reports current private company performance | Nowhere | Excluded by policy | Not stated | Private/confidential results are intentionally not published |
| The repo contains customer data, internal SQL, private schemas, or confidential dashboards | Nowhere | Excluded by policy | Not stated | Keep publishing from tracked files only |

## Review Rule

When adding a new strong statement to the README or executive reading path, add it here first. If the statement cannot be supported by a public source, direct repo artifact, or clearly marked inference, revise it.
