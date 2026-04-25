# Evidence Ledger

This ledger maps public-facing statements to the artifact or source that supports them.

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
| The repo contains a coherent operating thesis for AI-native data leadership | [`README.md`](../README.md), [`evidence-and-scope.md`](./evidence-and-scope.md) | README, CDO OS, playbooks, toolkits | Direct repo artifact | Quality still depends on reader judgment |
| The repo is public-safe by design | [`README.md`](../README.md), [`repo-privacy-policy.md`](./repo-privacy-policy.md) | Privacy policy, publication checklist, synthetic examples | Direct repo artifact | Manual ZIP/upload outside git could bypass safeguards |
| Paras has a long-running public writing archive | [`README.md`](../README.md), [`public-source-inventory.md`](./public-source-inventory.md) | Insight Extractor archive | Public external source | Archive metrics are self-published on the site |
| Paras has senior analytics/community recognition | [`external-evidence-of-impact.md`](./external-evidence-of-impact.md) | Institute of Analytics profile, Evanta page, Globee pages | Public external source | Recognition does not by itself prove current operating scope |
| There is externally visible outcome evidence beyond self-authored writing | [`external-evidence-of-impact.md`](./external-evidence-of-impact.md) | Select Star case study, Opendoor public article | Public external source | Vendor case studies and company articles are not audited financial evidence |
| The repo includes a public-source case read-through tied to measurable outcomes | [`case-studies/public-analytics-platform-transformation.md`](./case-studies/public-analytics-platform-transformation.md) | Select Star case study | Public external source | Vendor-authored source, so caveats stay explicit |
| AI analytics needs trusted metric/context infrastructure before broad rollout | [`playbooks/semantic-layer-is-the-trust-layer.md`](../playbooks/semantic-layer-is-the-trust-layer.md), [`projects/ten-metric-trust-layer-pilot.md`](../projects/ten-metric-trust-layer-pilot.md) | Repo argument plus public research notes | Direct repo artifact | This is an operator thesis, not a universal law |
| A 10-metric trust layer is a practical first pilot | [`projects/ten-metric-trust-layer-pilot.md`](../projects/ten-metric-trust-layer-pilot.md) | Generalized pattern from adjacent work and repo playbooks | Direct repo artifact | Public repo does not state that a named customer deployed this exact pilot |
| Decision memos improve executive use of AI-assisted analysis | [`projects/decision-memo-operating-loop.md`](../projects/decision-memo-operating-loop.md), [`sample-monthly-cdo-review.md`](./sample-monthly-cdo-review.md) | Repo artifact and synthetic example | Direct repo artifact | External adoption examples would make this stronger |
| The repo reports current private company performance | Nowhere | Excluded by policy | Not stated | Private/confidential results are intentionally not published |
| The repo contains customer data, internal SQL, private schemas, or confidential dashboards | Nowhere | Excluded by policy | Not stated | Keep publishing from tracked files only |

## Review Rule

When adding a new strong statement to the README or executive reading path, add it here first. If the statement cannot be supported by a public source, direct repo artifact, or clearly marked inference, revise it.
